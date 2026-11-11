# Términos · E (parte 3 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · **E** · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-e.md) · [2](terminos-e-2.md) · **3**

### Espacio profundo

- El espacio profundo se aproxima aquí como un sumidero a `3 K`.

💡 **Cómo se explica en la clase [B85-C07](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md):**
- Un radiador de `500 W` a `290 K` con `ε = 0,85` necesita `1,47 m²` en espacio profundo, `1,89 m²` en órbita baja con valores iniciales y `2,38 m²` con valores de fin de vida.
- Descripción larga: el entorno y el envejecimiento añaden más de la mitad del área respecto del espacio profundo; subir 20 K la reduce un tercio.
- 🎯 **Por qué importa:** El área del radiador manda en masa, volumen y costo. La decisión central: ¿cuánta área necesita un radiador en el caso caliente de fin de vida y qué la reduce?
- 🔗 **Se estudia junto con:** flujo neto, área requerida, aleta radiante, eficiencia.

📘 **Dónde se aprende** (1 clase): [B85-C07 · Radiadores espaciales](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md).

### Espacio vectorial real

- Un espacio vectorial real es un conjunto `V` con una suma `u + v` y un producto por escalares reales `a·u` que cumplen ocho propiedades: la suma es conmutativa y asociativa; existe un vector cero que no cambia nada; todo vector tiene un opuesto; y el producto por escalares es distributivo sobre la suma de vectores y de escalares, asociativo y con `1·u = u` (S1 usa `ℝⁿ` con estas operaciones en §1.2(v)).

💡 **Cómo se explica en la clase [B10-C01](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md):**
- Enunciar los ocho axiomas de un espacio vectorial real y reconocerlos en `ℝⁿ`.
- 🎯 **Por qué importa:** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.
- 🔗 **Se estudia junto con:** cero, opuesto, escalar, subespacio.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Espacio-tiempo de Minkowski

- El espacio-tiempo de Minkowski es el conjunto de eventos con la métrica `s² = (ct)² − x² − y² − z²`.

💡 **Cómo se explica en la clase [B26-C04](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md):**
- Definir el espacio-tiempo de Minkowski y el intervalo.
- python programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/gemelos.py
- 🎯 **Por qué importa:** Comunicar con una sonda, sincronizar relojes de dos estaciones o decidir si un evento puede haber causado otro exige saber cuándo dos sucesos están conectados por una señal. El intervalo lo decide para todos los observadores.
- 🔗 **Se estudia junto con:** intervalo de género tiempo, género espacio, género luz, cono de luz.

📘 **Dónde se aprende** (1 clase): [B26-C04 · Espacio-tiempo de Minkowski](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md).

### Especie traza

- Una especie traza es una con fracción mucho menor que 1.

💡 **Contexto en la clase [B54-C02](../programa/clases/B54/B54-C02-composicion-quimica-atmosferica/CLASE.md):**
- **Idea central (modelo mental):** Una mezcla de gases es como una receta: el peso medio por moléculas depende de cuánto hay de cada ingrediente.
- 🎯 **Por qué importa:** Dos atmósferas con la misma temperatura y gravedad tienen alturas de escala distintas si sus gases pesan distinto. La pregunta motivadora: ¿qué parte de la diferencia entre las atmósferas de los planetas viene solo de la composición?
- 🔗 **Se estudia junto con:** masa molar media, fracción por volumen, renormalización, altura de escala.

📘 **Dónde se aprende** (1 clase): [B54-C02 · Composición química atmosférica](../programa/clases/B54/B54-C02-composicion-quimica-atmosferica/CLASE.md).

### Especificidad

- La especificidad `e` es `P(negativo | no H)`.
- La sensibilidad, la especificidad, el VPP y el VPN miden un umbral.
- Sensibilidad `TP/(TP+FN)` y especificidad `TN/(TN+FP)`.

💡 **Cómo se explica en la clase [B63-C06](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md):**
- Un marco sintético: la probabilidad previa de peligro es `10⁻³`, cada prueba tiene sensibilidad `0,90` y especificidad `0,95`, y el costo de retener es `1` frente a `10⁵` de liberar una muestra peligrosa (unidades arbitrarias).
- Aplicar el teorema de Bayes a una prueba con sensibilidad y especificidad conocidas.
- 🎯 **Por qué importa:** Ninguna prueba demuestra que no hay peligro; solo reduce la incertidumbre. La decisión central: ¿cuántas pruebas negativas hacen falta antes de que liberar sea preferible a retener, y de qué dependen?
- 🔗 **Se estudia junto con:** probabilidad previa, sensibilidad, posterior, momios.

📘 **Dónde se aprende** (3 clases): [B63-C06 · Evaluación de riesgos biológicos de muestras: marcos de decisión](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md); [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md); [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Específico

- Un comentario es específico si cita un dato verificable del trabajo.

💡 **Cómo se explica en la clase [B131-C10](../programa/clases/B131/B131-C10-retroalimentacion-efectiva/CLASE.md):**
- 12 comentarios reescritos: 4 de tarea, 3 de proceso, 4 de autorregulación y 1 de persona (`8,3 %`); 7 son específicos (`58 %`).
- Reescribir mueve el foco de la persona a la acción, y aumenta lo específico.
- 🎯 **Por qué importa:** Un comentario como «muy bien» o «desastre» no dice qué hacer. La decisión central: ¿qué información da este comentario al estudiante para su próximo paso?
- 🔗 **Se estudia junto con:** de tarea, de proceso, de autorregulación, de persona.

📘 **Dónde se aprende** (1 clase): [B131-C10 · Retroalimentación efectiva](../programa/clases/B131/B131-C10-retroalimentacion-efectiva/CLASE.md).

### Espectro

- El espectro es la luz descompuesta por longitud de onda.
- Un espectro es la distribución de la luz por longitud de onda.
- El espectro es el conjunto de autovalores.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- Observa que el patrón (la distancia relativa entre líneas) se conserva aunque todo el espectro se corra.
- Si todas dan el mismo `z` dentro del error, el corrimiento es de todo el espectro, no un error de identificación.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).
- 🔗 **Se estudia junto con:** longitud de onda, frecuencia, espectro continuo, emisión.

📖 **Explicado a fondo:** [Espectro y espectroscopía](esencial/esencial-d-l.md#espectro-y-espectroscopía) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (9 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md); [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md); [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B35-C09 · Turbulencia en plasmas y MHD](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md); [B36-C02 · Función de transferencia y espectro de materia](../programa/clases/B36/B36-C02-funcion-de-transferencia-y-espectro-de-materia/CLASE.md) y 3 más.

### Espectro angular

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B40-C07](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md):**
- La evidencia es la ficha del espectro angular del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha del espectro angular*: `θ*`, `ℓ_A`, picos y ida y vuelta.
- 🎯 **Por qué importa:** Los picos acústicos fijan la geometría y el contenido del universo. La decisión central: ¿dónde caen los picos (`ℓ_A = π/θ*`) y cómo se pasa del espectro a la correlación y de vuelta?
- 🔗 **Se estudia junto con:** horizonte sonoro, distancia comóvil, escala acústica, polinomios de Legendre.

📘 **Dónde se aprende** (1 clase): [B40-C07 · Espectro angular de potencias del CMB](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md).

### Espectro continuo

- Un espectro continuo tiene luz en todas las longitudes de onda; uno de emisión muestra líneas brillantes sobre fondo oscuro; uno de absorción muestra líneas oscuras sobre un fondo continuo.
- Un espectro continuo tiene todos los colores; uno de absorción tiene líneas oscuras donde un gas absorbe; uno de emisión tiene líneas brillantes donde un gas emite.
- Un espectro continuo tiene luz en todos los colores; un espectro de emisión muestra líneas brillantes (un gas caliente emite sólo a ciertas longitudes de onda); uno de absorción muestra líneas oscuras (un gas más frío delante de una fuente continua absorbe esas mismas longitudes).

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- Distinguir espectro continuo, de emisión y de absorción.
- Ejercicio 12 · integrador. Elabora tu interpretación de un espectro sencillo: con un espectro sintético dado (o uno que construyas con tres líneas), calcula `z` por línea, verifica un corrimiento común, estima velocidad aparente, indica una estimación de temperatura si hay continuo y rotula cada resultado O, I o M con supuestos.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).
- 🔗 **Se estudia junto con:** longitud de onda, frecuencia, espectro, emisión.

📘 **Dónde se aprende** (3 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md); [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Espectro cruzado

- El espectro cruzado es `conj(F₁) F₂`.
- El espectro cruzado `B A*`.

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- F --> X["Espectro cruzado<br/>normalizado R"]
- *Descripción textual:* con las dos imágenes se calcula el espectro cruzado normalizado, cuyo pico da el desplazamiento entero, que se refina de forma local; alternativamente, con pares de puntos homólogos se estiman ángulo y traslación por Procrustes.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».
- 🔗 **Se estudia junto con:** registro, desplazamiento, transformación rígida, afín.

📘 **Dónde se aprende** (3 clases): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md); [B36-C08 · Sesgo de galaxias y trazadores de la materia](../programa/clases/B36/B36-C08-sesgo-de-galaxias-y-trazadores-de-la-materia/CLASE.md); [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Espectro de emisión

- Un espectro continuo tiene luz en todos los colores; un espectro de emisión muestra líneas brillantes (un gas caliente emite sólo a ciertas longitudes de onda); uno de absorción muestra líneas oscuras (un gas más frío delante de una fuente continua absorbe esas mismas longitudes).

💡 **Cómo se explica en la clase [B06-C17](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md):**
- Distinguir un espectro continuo, de emisión y de absorción, y decir qué indica cada uno.
- 🎯 **Por qué importa:** En B01-C01 estimaste la velocidad de una galaxia con una sola línea, H-alfa en 662,9 nm. Pero ¿cómo se sabe que esa línea es H-alfa y no otra?
- 🔗 **Se estudia junto con:** espectro, espectro continuo, absorción, línea espectral.

📘 **Dónde se aprende** (1 clase): [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Espectro de masas

- Fuente metabólica: CO₂, vapor y trazas de las personas. Espectro de masas: huella de un compuesto.

💡 **Contexto en la clase [B106-C22](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md):**
- 🎯 **Por qué importa:** Nada sale al exterior de una cabina cerrada: los materiales emiten gases durante meses, los equipos liberan trazas y las personas emiten vapor y CO₂. La decisión central: ¿qué fuentes dominan en cada momento y cómo se identifican los compuestos para decidir qué retirar?
- 🔗 **Se estudia junto con:** Desgasificación, Fuente metabólica, Biblioteca, NNLS.

📘 **Dónde se aprende** (1 clase): [B106-C22 · Fuentes e identificación de contaminantes del aire de cabina](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md).

### Espectro de potencia

- El espectro de potencia de Kolmogorov.

💡 **Contexto en la clase [B42-C11](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md):**
- **Idea central (modelo mental):** Como un río con remolinos de todos los tamaños: los grandes llevan la mayor parte de la energía y los pequeños la completan.
- 🎯 **Por qué importa:** La atmósfera fija el límite de resolución de los telescopios terrestres y es la perturbación que corrige la óptica adaptativa. La decisión central: ¿cómo se simula una pantalla de fase con la estadística correcta y qué errores introduce la malla?
- 🔗 **Se estudia junto con:** pantalla de fase, función de estructura, parámetro, subarmónicos.

📘 **Dónde se aprende** (1 clase): [B42-C11 · Turbulencia atmosférica](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md).

### Espectro de potencias

- El espectro de potencias `P(k)`.

💡 **Contexto en la clase [B40-C05](../programa/clases/B40/B40-C05-perturbaciones-primordiales-y-espectro-escalar/CLASE.md):**
- **Idea central (modelo mental):** Como una cuerda cuya amplitud de cada armónico es aleatoria pero con una varianza que depende de la frecuencia: el espectro es esa varianza.
- 🎯 **Por qué importa:** El espectro es el vínculo entre la inflación y las anisotropías. La decisión central: ¿qué predice el modelo para `n_s` y `r`, y es compatible con los límites publicados?
- 🔗 **Se estudia junto con:** índice espectral, razón tensor-escalar, amplitud.

📘 **Dónde se aprende** (1 clase): [B40-C05 · Perturbaciones primordiales y espectro escalar](../programa/clases/B40/B40-C05-perturbaciones-primordiales-y-espectro-escalar/CLASE.md).

### Espectro diferencial

- El espectro diferencial es `dΦ/dL = 2Φ₁L⁻³` si `Φ(>L) = Φ₁L⁻²`.

💡 **Contexto en la clase [B85-C21](../programa/clases/B85/B85-C21-efectos-de-particulas-energeticas-en-electronica-y-materiales/CLASE.md):**
- 🎯 **Por qué importa:** Un upset en un procesador o en una memoria puede reiniciar un instrumento o corromper un dato. La decisión central: ¿con qué frecuencia ocurre un evento único en un dispositivo dado y cuánto cambia si se elige un componente de mayor umbral de LET?
- 🔗 **Se estudia junto con:** sección eficaz de Weibull, tasa por bit, upset, probabilidad de al menos un evento.

📘 **Dónde se aprende** (1 clase): [B85-C21 · Efectos de partículas energéticas en electrónica y materiales](../programa/clases/B85/B85-C21-efectos-de-particulas-energeticas-en-electronica-y-materiales/CLASE.md).

### Espectro dinámico

- El espectro dinámico muestra la deriva.

💡 **Cómo se explica en la clase [B30-C21](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md):**
- *Descripción textual:* la posición del haz fija la densidad y la frecuencia; de ahí salen la deriva y el espectro dinámico, del que se recupera la cresta y la velocidad.
- Construir un espectro dinámico sintético con ruido.
- 🎯 **Por qué importa:** Una frecuencia es una altura, y la deriva en frecuencia da la velocidad del haz. La decisión central: ¿cómo se convierte un espectro dinámico en la velocidad de los electrones?
- 🔗 **Se estudia junto con:** estallido tipo III, deriva en frecuencia, emisión fundamental, armónico.

📘 **Dónde se aprende** (1 clase): [B30-C21 · Radioemisión solar: estallidos de radio y su observación](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md).

### Espectro electromagnético

- El espectro electromagnético ordena las ondas por frecuencia: radio, microondas, infrarrojo, visible, ultravioleta, rayos X y gamma.

💡 **Contexto en la clase [B05-C18](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md):**
- **Idea central (modelo mental):** La misma radiación tiene dos descripciones: como onda (frecuencia, longitud de onda) y como flujo de fotones (energía por fotón). Más frecuencia, más energía por fotón.
- 🎯 **Por qué importa:** Un satélite se comunica con ondas de radio, un telescopio observa luz y rayos X, y la misma radiación a otras energías puede dañar electrónica y tejidos. La pregunta motivadora es: ¿qué es la radiación electromagnética, cómo se ordena por frecuencia y energía, cómo decae con la distancia y qué la hace peligrosa?
- 🔗 **Se estudia junto con:** onda electromagnética, magnitudes, fotón, intensidad o flujo.

📘 **Dónde se aprende** (1 clase): [B05-C18 · Electromagnetismo y radiación](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md).

### Espectro molecular

- Un espectro molecular tiene además líneas por la rotación y la vibración de la molécula, que caen en el infrarrojo y las microondas.

💡 **Cómo se explica en la clase [B06-C17](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md):**
- python programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/identificar_lineas.py
- 🎯 **Por qué importa:** En B01-C01 estimaste la velocidad de una galaxia con una sola línea, H-alfa en 662,9 nm. Pero ¿cómo se sabe que esa línea es H-alfa y no otra?
- 🔗 **Se estudia junto con:** espectro, espectro continuo, espectro de emisión, absorción.

📘 **Dónde se aprende** (1 clase): [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Espectro secundario

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C15](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md):**
- Hay espectro secundario porque las dispersiones parciales no son proporcionales.
- ⚠️ **Error frecuente:** Creer que el doblete elimina todo el color. Queda espectro secundario.
- 🎯 **Por qué importa:** Un refractor sin color necesita combinar vidrios. La decisión central: ¿cuánto color queda con dos o tres vidrios?
- 🔗 **Se estudia junto con:** doblete acromático, triplete apocromático, potencia, factor de forma.

📘 **Dónde se aprende** (1 clase): [B41-C15 · Refractores acromáticos y apocromáticos](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md).

### Espectro sintético

- Espesor másico: densidad × espesor (g/cm²). Espectro sintético: distribución de energías inventada.

💡 **Cómo se explica en la clase [B106-C14](../programa/clases/B106/B106-C14-proteccion-contra-radiacion/CLASE.md):**
- S["espectro sintetico E^-2.5"] --> B["blindaje x g/cm2"]
- *Descripción textual:* el espesor fija la energía mínima que lo atraviesa; con el espectro sintético se obtiene la fracción detenida y con la geometría, la masa.
- ⚠️ **Error frecuente:** Tomar el espectro sintético como real. Es inventado (sección 10).
- 🎯 **Por qué importa:** Las paredes y el regolito detienen partículas, pero con límites: la masa es costosa y las partículas secundarias complican el panorama. La decisión central: ¿cuánta masa por área detiene qué parte de las partículas, y dónde el modelo deja de valer?
- 🔗 **Se estudia junto con:** Alcance CSDA, Espesor másico, Partícula secundaria, Rango de validez.

📘 **Dónde se aprende** (1 clase): [B106-C14 · Protección contra radiación](../programa/clases/B106/B106-C14-proteccion-contra-radiacion/CLASE.md).

### Espectrograma

- El espectrograma es la fotografía de un espectro (C16).

💡 **Contexto en la clase [B02-C17](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md):**
- **Idea central (modelo mental):** La placa acumula luz mientras el cielo gira; si el instrumento no sigue el giro, cada estrella se convierte en una raya.
- 🎯 **Por qué importa:** Un dibujo depende de quien lo hace; una placa registra lo que llegó. La pregunta motivadora es: ¿qué cambia cuando la observación puede guardarse, compararse años después y medirse?
- 🔗 **Se estudia junto con:** astrofotografía, daguerrotipo, placa seca de gelatina, exposición.

📘 **Dónde se aprende** (1 clase): [B02-C17 · Nacimiento de la astrofotografía](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md).

### Espectrometría de masas

- La espectrometría de masas separa iones por su relación masa/carga (`m/z`); cada especie deja un patrón de fragmentación en varios canales.

💡 **Cómo se explica en la clase [B67-C07](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md):**
- B) Espectrometria de masas: desmezcla de 5 especies en 6 canales
- python programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/sensores.py
- 🎯 **Por qué importa:** Un sensor no mide «agua»: mide cuentas, y de ellas se infiere la abundancia con un modelo. La decisión central: ¿cuánto tiempo de medición y qué canales hacen falta para detectar y separar un volátil con la incertidumbre requerida?
- 🔗 **Se estudia junto con:** tasa de neutrones epitérmicos, abundancia equivalente en agua (WEH), conteo de Poisson, patrón de fragmentación.

📘 **Dónde se aprende** (1 clase): [B67-C07 · Sensores para volátiles: espectrometría de neutrones y de masas](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md).

### Espectrómetro de masas cuadrupolar (QMS)

- El espectrómetro de masas cuadrupolar (QMS) mide el gas por masa.

💡 **Cómo se explica en la clase [B68-C04](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md):**
- Kruczkiewicz y colaboradores (2024) hacen TPD a `0,2 K s⁻¹` desde 10 K y detectan los gases con un espectrómetro de masas cuadrupolar;
- 🎯 **Por qué importa:** Un hielo de 10 ML de CO sobre una superficie a 10 K se contamina con agua residual en horas si la presión de fondo no es lo bastante baja, y una TPD con bombeo insuficiente deforma el pico que se mide.
- 🔗 **Se estudia junto con:** ultra alto vacío (UHV), flujo de Hertz–Knudsen, probabilidad de adhesión, langmuir.

📘 **Dónde se aprende** (1 clase): [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### Espectroscopio

- Un espectroscopio descompone la luz.

💡 **Cómo se explica en la clase [B02-C16](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md):**
- A["Luz del astro"] --> B["Espectroscopio:<br/>separa por longitud de onda"]
- *Descripción textual:* la luz del astro pasa por un espectroscopio que la separa por longitud de onda; se miden posiciones e intensidades de líneas; se comparan con las del laboratorio para identificar elementos; la conclusión sobre composición tiene límites.
- 🎯 **Por qué importa:** Hasta 1859 se pensaba, con razones, que nunca sabríamos de qué están hechas las estrellas: estaban demasiado lejos para tocarlas. La pregunta motivadora es: ¿cómo se puede conocer la composición de un objeto que solo se ve como luz?
- 🔗 **Se estudia junto con:** espectro, espectro continuo, absorción, emisión.

📘 **Dónde se aprende** (1 clase): [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md).

### Espejo cóncavo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C04](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md):**
- **Idea central (modelo mental):** Como una antena parabólica de TV: todas las señales paralelas al eje convergen en el mismo punto; con un plato esférico la señal de los bordes llega antes.
- 🎯 **Por qué importa:** El espejo primario de un telescopio reflector es una superficie cónica. La decisión central: ¿por qué se usa un paraboloide y no una esfera?
- 🔗 **Se estudia junto con:** sagita, constante cónica, foco paraxial, aberración esférica longitudinal.

📘 **Dónde se aprende** (1 clase): [B41-C04 · Espejos esféricos y parabólicos](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md).

### Espejo deformable

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C15](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md):**
- La evidencia es la ficha del espejo deformable del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha del espejo deformable*: paso, error de ajuste y escala.
- 🎯 **Por qué importa:** El número de actuadores fija el error de ajuste que ninguna medición mejora. La decisión central: ¿cuántos actuadores se necesitan para un `r₀` dado?
- 🔗 **Se estudia junto con:** función de influencia, paso, acoplamiento, error de ajuste.

📘 **Dónde se aprende** (1 clase): [B42-C15 · Espejos deformables](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md).

### Espejo magnético

- El espejo magnético refleja partículas con ángulo de paso grande.

💡 **Cómo se explica en la clase [B30-C06](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md):**
- *Descripción textual:* la fuerza de Lorentz integrada con Boris da el giro, la deriva y el rebote en el espejo, con el momento magnético conservado.
- 🎯 **Por qué importa:** El movimiento de las partículas explica cómo se atrapan en los cinturones, cómo derivan y cómo se aceleran. La decisión central: ¿cuándo queda atrapada una partícula y cuánto vale su radio de giro?
- 🔗 **Se estudia junto con:** radio de Larmor, frecuencia de giro, deriva E×B, momento magnético.

📘 **Dónde se aprende** (1 clase): [B30-C06 · Partículas cargadas y movimientos](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md).

### Espejo solar óptico (OSR)

- Un espejo solar óptico (OSR) es un radiador de `α` bajo y `ε` alta.

💡 **Contexto en la clase [B85-C05](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md):**
- 🎯 **Por qué importa:** Cambiar un recubrimiento es la forma más barata de mover la temperatura de una superficie decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la superficie dentro del intervalo al principio y al final de la vida?
- 🔗 **Se estudia junto con:** cociente α/ε, envejecimiento, BOL, EOL.

📘 **Dónde se aprende** (1 clase): [B85-C05 · Recubrimientos ópticos térmicos](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md).

### Espera en cola

- Ocupación `ρ`: tasa de llegada por tiempo de servicio. Espera en cola `W_q`.

💡 **Cómo se explica en la clase [B48-C16](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md):**
- En un programa real los cuadros llegan a cadencia fija (cola D/D/1, sin espera si `D` es menor que la cadencia): el modelo de Poisson sobreestima la espera y sirve para ráfagas, no para el régimen estable.
- *Descripción textual:* la ocupación determina la espera de la cola: pequeña con carga baja, divergente cerca de uno; la recursión de Lindley la verifica.
- ⚠️ **Error frecuente:** Confundir espera en cola con tiempo total. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Si la reducción no sigue el ritmo, se acumulan cuadros y el resultado llega tarde. La decisión central: ¿hasta qué ocupación del procesador es tolerable la espera?
- 🔗 **Se estudia junto con:** Cola M/D/1, Ocupación, Recursión de Lindley, Tasa de datos.

📘 **Dónde se aprende** (1 clase): [B48-C16 · Procesamiento de datos en línea](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md).

### Espera fría

- Repuesto: unidad de reemplazo. Espera fría: unidad apagada que se conecta al fallar la principal.

💡 **Cómo se explica en la clase [B106-C18](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md):**
- La espera fría perfecta da 0,97977 y con conmutador de 0,95, 0,97107: el conmutador limita la mejora.
- Incluir la causa común (factor β) y un conmutador imperfecto en la espera fría.
- 🎯 **Por qué importa:** Ningún equipo es perfecto y una misión larga no se puede reparar con repuestos de la Tierra. La decisión central: ¿qué configuración redundante y cuántos repuestos dan una probabilidad objetivo de cumplir la misión?
- 🔗 **Se estudia junto con:** Fiabilidad, Tasa de falla λ, Redundancia k de n, Causa común (β).

📘 **Dónde se aprende** (1 clase): [B106-C18 · Fiabilidad y redundancia](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md).

### Espera media

- Función de distribución: probabilidad de no superar un valor. Espera media: inversa de la probabilidad por noche.

💡 **Cómo se explica en la clase [B48-C11](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md):**
- Calcular la espera media hasta una clase dada.
- Espera media hasta una noche A = 4.97 noches; noches A por año = 73.4
- 🎯 **Por qué importa:** Un programa que exige la mejor calidad espera mucho; uno que acepta cualquiera desperdicia las buenas noches. La decisión central: ¿con qué frecuencia se da cada clase y cuánto hay que esperar?
- 🔗 **Se estudia junto con:** Clase de calidad, Lognormal, Mediana, Función de distribución.

📘 **Dónde se aprende** (1 clase): [B48-C11 · Calidad y clasificación de datos](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md).

### Espera Wq

- Utilización: `ρ = λ/μ`. Espera `Wq`: tiempo en cola.

💡 **Cómo se explica en la clase [B96-C26](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md):**
- La prioridad no reduce la espera global (1,491 y 1,492 h); la redistribuye: la alta espera la mitad y la baja espera 17 % más.
- *Descripción textual:* los incidentes de dos prioridades entran a una sola cola y un equipo los atiende de a uno; la teoría de colas da la espera por clase y la simulación la verifica.
- 🎯 **Por qué importa:** Sin un procedimiento de priorización, un incidente leve puede retrasar a uno grave. La decisión central: ¿cuánto esperan los incidentes de alta y de baja prioridad y cuánto mejora la priorización al grave sin colapsar al leve?
- 🔗 **Se estudia junto con:** Incidente, M/M/1, Utilización, Prioridad no expropiativa.

📘 **Dónde se aprende** (1 clase): [B96-C26 · Gestión de incidentes en la operación de estaciones](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md).

### Esperanza

- La esperanza (o valor esperado) `E[X]` es el promedio de los valores ponderado por su probabilidad (S1, C.2.9): `Σ x p(x)` en una discreta, `∫ x f(x) dx` en una continua.
- La esperanza por orden es `E = T_ok + (1/q − 1) T_to`.

💡 **Cómo se explica en la clase [B12-C04](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md):**
- Aquí `E[X] = 2,7` no es un valor que `X` pueda tomar: la esperanza es un promedio a largo plazo, no un valor típico.
- La esperanza es el punto de equilibrio de la distribución, como el centro de masa de una barra con pesos; la varianza es su momento de inercia respecto de ese centro, y la desviación típica su radio de giro.
- 🎯 **Por qué importa:** Un ingeniero no maneja distribuciones completas; maneja «la medida es 150,0 m con una incertidumbre de 3 m». Esa frase usa exactamente una esperanza y una desviación típica.
- 🔗 **Se estudia junto con:** varianza, desviación típica, estimador, desviación típica experimental.

📘 **Dónde se aprende** (2 clases): [B12-C04 · Esperanza y varianza](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md); [B98-C06 · Simulación de teleoperación con retardo](../programa/clases/B98/B98-C06-simulacion-de-teleoperacion-con-retardo/CLASE.md).

### Esperanza de bajas

- La esperanza de bajas `E_c` es el número medio de víctimas.
- La esperanza de bajas `Ec = Pf·ρ·Ac·(1 − refugio)` usa la probabilidad de falla, la densidad de población, el área de baja efectiva y la fracción de refugio.

💡 **Cómo se explica en la clase [B83-C21](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md):**
- T["Trayectoria: Pf, densidad, area"] --> E["Esperanza de bajas Ec"]
- *Descripción textual:* la operación se divide en nodos y se recorre con palabras guía para listar peligros con severidad y verosimilitud; los de severidad alta se revisan aunque su índice sea bajo; por separado, la esperanza de bajas de la trayectoria se compara con el umbral y su incertidumbre se estudia por Monte Carlo y por fórmula.
- 🎯 **Por qué importa:** Los peligros que no se identifican no se pueden controlar. La decisión central: ¿qué puede salir mal en cada fase, qué tan grave y probable es, y el riesgo para terceros cabe en el umbral que el proyecto adoptó?
- 🔗 **Se estudia junto con:** HAZID, peligro, riesgo, índice.

📘 **Dónde se aprende** (2 clases): [B83-C21 · Identificación de peligros en sistemas de lanzamiento (HAZID)](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md); [B119-C22 · Seguridad de instalaciones y operaciones de sitio de lanzamiento](../programa/clases/B119/B119-C22-seguridad-de-instalaciones-y-operaciones-de-sitio-de-lanzamiento/CLASE.md).

### Espesor crítico

- El espesor crítico `h_c` es aquel por debajo del cual la colada se detiene.

💡 **Cómo se explica en la clase [B70-C07](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md):**
- *Descripción textual:* la pendiente, el espesor y la reología dan el caudal si el espesor supera el crítico; la velocidad, el ángulo, la gravedad y el aire dan el alcance de los clastos.
- Calcular el espesor crítico de Bingham `h_c = τ_y/(ρ g sinθ)`.
- 🎯 **Por qué importa:** La misma lava fluye distinto según la pendiente, el espesor y la reología; los piroclastos llegan más lejos si no hay aire. La decisión central: ¿cuánto fluye una colada y hasta dónde llegan los clastos en cada mundo?
- 🔗 **Se estudia junto con:** colada, modelo de Bingham, clasto balístico, depósito piroclástico.

📘 **Dónde se aprende** (1 clase): [B70-C07 · Flujos de lava y depósitos piroclásticos](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md).

### Espesor de equilibrio

- El espesor de equilibrio `t_eq = P/(ρ g)` sería el que contiene la presión interna solo con peso.

💡 **Cómo se explica en la clase [B97-C14](../programa/clases/B97/B97-C14-construccion-con-regolito-robotica-y-construccion-extraterrestre/CLASE.md):**
- cuerpo sobrecarga [kPa] fraccion de P espesor de equilibrio [m] presion neta hacia arriba [kPa]
- 🎯 **Por qué importa:** Quien cree que el regolito «sostiene» el hábitat se equivoca: con baja gravedad, el peso de una cubierta de poco más de un metro cubre solo una pequeña fracción de la presión interna. La estructura debe resistir la diferencia por tracción o anclaje.
- 🔗 **Se estudia junto con:** densidad superficial, sobrecarga, blindaje.

📘 **Dónde se aprende** (1 clase): [B97-C14 · Construcción con regolito — Robótica y construcción extraterrestre](../programa/clases/B97/B97-C14-construccion-con-regolito-robotica-y-construccion-extraterrestre/CLASE.md).

### Espesor del hielo

- El espesor del hielo `d_h` es la profundidad de la capa sólida.

💡 **Cómo se explica en la clase [B56-C09](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md):**
- El volumen fija casi todo; el espesor del hielo pesa menos en la profundidad y más en la presión.
- Descripción larga: la profundidad del océano casi no depende del espesor del hielo; la presión sí, porque suma la columna de hielo.
- ⚠️ **Error frecuente:** Presentar el espesor del hielo como dato. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un océano global bajo el hielo es un candidato a hábitat, protegido de la radiación y del vacío. Saber cuán profundo es y qué presión soporta fija qué sondas podrían llegar y qué ambientes existen.
- 🔗 **Se estudia junto con:** océano subsuperficial, cascarón esférico, profundidad del océano, presión hidrostática.

📘 **Dónde se aprende** (1 clase): [B56-C09 · Océanos de Europa](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md).

### Espesor en el borde

- El espesor en el borde `t_rim` es la referencia.

💡 **Cómo se explica en la clase [B61-C04](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md):**
- Con `t_rim` = 0,04 R, el espesor cae de 0,0400 R en el borde a 0,0050 R en 2 R y 0,0015 R en 3 R.
- ⚠️ **Error frecuente:** Olvidar que el borde es el espesor máximo. Se corrige con 8.1.
- 🎯 **Por qué importa:** El manto de ejecta es un marcador estratigráfico: cubre lo anterior y es cubierto por lo posterior. La decisión central: ¿cómo decae el espesor con la distancia y cuánto volumen contiene el manto?
- 🔗 **Se estudia junto con:** manto de ejecta, ejecta distal, estratigrafía invertida, ley de −3.

📘 **Dónde se aprende** (1 clase): [B61-C04 · Mantos de ejecta y depósitos de impacto](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md).

### Espesor gobernante

- El espesor gobernante es el mayor de los requeridos.

💡 **Cómo se explica en la clase [B85-C28](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md):**
- Con un factor de atenuación `2,2` veces el del aluminio por milímetro y densidad `950 kg/m³`, el polietileno cumple la dosis con `5,33 mm`, pero la perforación impone `21,5 mm` y el espesor gobernante es `21,5 mm`: masa `10,20 kg`, menos de la mitad.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de diseño de una protección pasiva*: espesores por requisito, gobernante, masa por material, contraste Poisson–Monte Carlo y lista de lo sintético.
- 🎯 **Por qué importa:** Cada milímetro de blindaje cuesta masa, y el requisito que manda cambia con el entorno. La decisión central: ¿qué espesor y qué material cumplen la dosis y la probabilidad de perforación con la menor masa?
- 🔗 **Se estudia junto con:** atenuación, flujo de micrometeoritos, diámetro crítico, probabilidad de perforación.

📘 **Dónde se aprende** (1 clase): [B85-C28 · Protección pasiva frente al ambiente espacial](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md).

### Espesor másico

- Alcance CSDA: distancia media recorrida frenándose de forma continua. Espesor másico: densidad × espesor (g/cm²).
- Cubierta: capa de regolito sobre el habitat. Espesor másico: densidad por espesor (g/cm²).

💡 **Cómo se explica en la clase [B106-C19](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md):**
- Relacionar el espesor másico con el modelo de blindaje (C14).
- Espesor masico de la cubierta: 450 g/cm2 (ver C14: fuera del rango de validez del modelo de protones)
- 🎯 **Por qué importa:** La Luna cambia las reglas: noches de dos semanas, gravedad de un sexto y un regolito que protege pero no contiene la presión. La decisión central: ¿qué recursos (energía, masa de cubierta, esfuerzo de excavación) exige un asentamiento enterrado y qué parte soporta cada elemento?
- 🔗 **Se estudia junto con:** Noche lunar, Regolito, Cubierta, Profundidad de descarga.

📘 **Dónde se aprende** (2 clases): [B106-C14 · Protección contra radiación](../programa/clases/B106/B106-C14-proteccion-contra-radiacion/CLASE.md); [B106-C19 · Arquitectura de asentamiento lunar conceptual](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md).

### Espesor opaco

- El espesor opaco deja pasar menos de un umbral.

💡 **Cómo se explica en la clase [B43-C07](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md):**
- Ejercicio 5. Espesor opaco para `T ≤ 10⁻³`.
- Ejercicio 12. Integrador. Elabora tu *ficha de aluminizado*: reflectancia, espesor opaco y uniformidad.
- 🎯 **Por qué importa:** Una película delgada deja pasar luz; una gruesa refleja pero no se adhiere ni es uniforme. La decisión central: ¿qué espesor es opaco, qué reflectancia da y cuánto varía de centro a borde por la geometría del evaporador?
- 🔗 **Se estudia junto con:** índice complejo, reflectancia, profundidad de penetración, matriz de transferencia.

📘 **Dónde se aprende** (1 clase): [B43-C07 · Aluminizado y recubrimientos](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md).

### Espesor óptico

- El espesor óptico `n t`.

💡 **Cómo se explica en la clase [B43-C24](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir espesor físico y óptico. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Cada reflexión sin tratar pierde luz y añade luz parásita. La decisión central: ¿cuántas capas y con qué índices y espesores se logra baja reflectancia en la banda visible?
- 🔗 **Se estudia junto con:** matriz característica, capa de cuarto de onda, reflectancia mínima, recubrimiento en V.

📘 **Dónde se aprende** (1 clase): [B43-C24 · Recubrimientos antirreflectantes de capas múltiples](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md).

### Espesor óptico de aerosoles

- El espesor óptico de aerosoles (AOD) `τ` es la integral vertical de la extinción.

💡 **Contexto en la clase [B57-C13](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md):**
- **Idea central (modelo mental):** El vaho del vidrio quita luz directa y la reparte en todas direcciones; cuanto más vaho, menos pasa. Si el vaho es de gotas finas, quita más luz azul que roja.
- 🎯 **Por qué importa:** Un satélite que mira un incendio, un volcán o el mar tiene que descontar la atmósfera, y los aerosoles son lo más variable. La decisión central: ¿cuánto aerosol hay y qué tipo, con qué incertidumbre, a partir de pocas longitudes de onda?
- 🔗 **Se estudia junto con:** ley de Beer–Lambert, exponente de Ångström, albedo de dispersión simple, función de fase.

📘 **Dónde se aprende** (1 clase): [B57-C13 · Atmósfera y aerosoles](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md).

### Espín

- El espín es el momento angular interno que absorbe el orbital relativo.
- El espín `a = cJ/(GM²)`.
- El espín `s = 1/2`.

💡 **Cómo se explica en la clase [B27-C07](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md):**
- Sin espín, `r₊ = 2` (el radio de Schwarzschild).
- Con espín prógrado crece la energía liberable y el ISCO baja: `4,2330` (`a = 0,5`), `2,3209` (`0,9`), `1,2370` (`0,998`).
- ⚠️ **Error frecuente:** Olvidar el signo del espín. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El espín cambia el ISCO y, con él, cuánta energía se libera: de `5,7 %` a más de `30 %` de la masa en reposo. La decisión central: ¿dónde están el horizonte y el ISCO para un espín dado y qué eficiencia implica?
- 🔗 **Se estudia junto con:** radio gravitacional, horizonte de sucesos, ISCO, órbita prógrada.

📘 **Dónde se aprende** (3 clases): [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md); [B31-C05 · Espín y momento angular](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md); [B52-C20 · Simulación de formación planetaria simplificada](../programa/clases/B52/B52-C20-simulacion-de-formacion-planetaria-simplificada/CLASE.md).

### Espiral

- Los tipos espiral, elíptica e irregular describen su forma (S1).

💡 **Cómo se explica en la clase [B01-C15](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md):**
- NASA agrupa las galaxias en espirales, elípticas e irregulares (S1).
- Por forma (espiral, elíptica): visual, pero superficial.
- 🎯 **Por qué importa:** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?
- 🔗 **Se estudia junto con:** galaxia, elíptica, irregular, grupo de galaxias.

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Espiral de Edelbaum

- La espiral de Edelbaum es la trayectoria de empuje tangencial entre órbitas circulares coplanares; su delta-v es `|V₁ − V₂|` cuando la aceleración es mucho menor que la gravedad local.

💡 **Cómo se explica en la clase [B75-C11](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md):**
- *Descripción textual:* Se integra la espiral hasta el radio de Marte; el tiempo y la aceleración dan el delta-v; se compara con Edelbaum y se convierte en fracción de propulsante.
- Ejercicio 12 · integrador. Elabora tu *comparación de la espiral de bajo empuje y la transferencia impulsiva*: tabla de tiempo, delta-v, propulsante (dos `I_sp`) y desviación con Edelbaum para tres aceleraciones, con tus conclusiones.
- 🎯 **Por qué importa:** Un motor de alta `I_sp` ahorra propulsante pero tarda mucho. La decisión central: ¿cuánto delta-v y cuánto tiempo cuesta una espiral y cuándo es válida la fórmula de Edelbaum?
- 🔗 **Se estudia junto con:** propulsión de bajo empuje, fracción de propulsante, cociente a/g☉.

📘 **Dónde se aprende** (1 clase): [B75-C11 · Propulsión de bajo empuje](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md).

### Espiral de Parker

- La espiral de Parker es la forma de la línea de campo arrastrada por el viento con el Sol rotando.

💡 **Cómo se explica en la clase [B30-C10](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md):**
- *Descripción textual:* la temperatura da la velocidad del sonido y el radio crítico; la ecuación de Parker da `v(r)`, del que salen el flujo de masa y la espiral.
- Ejercicio 12. Integrador. Elabora tu *ficha del viento de Parker*: tabla de velocidades, perfil, flujo de masa y espiral.
- 🎯 **Por qué importa:** El viento solar es el vehículo que lleva la actividad del Sol a la Tierra. La decisión central: ¿cuándo pasa el viento a supersónico y qué velocidad alcanza a 1 au?
- 🔗 **Se estudia junto con:** punto crítico, viento subsónico/supersónico, flujo de masa, ángulo.

📘 **Dónde se aprende** (1 clase): [B30-C10 · Viento solar y heliosfera](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md).

### Espiral logarítmica

- Una espiral logarítmica es una curva de ángulo de paso constante, `ln(R/R_k) = −(β − β_k) tan ψ`, donde `β` es el acimut galactocéntrico en radianes (0 hacia el Sol, creciente en el sentido de rotación) y `R_k` el radio en el acimut `β_k`.

💡 **Cómo se explica en la clase [B25-C02](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md):**
- Espiral logarítmica con nudos (esta clase y S2): se ajusta a máseres, con pocos parámetros.
- Definir ángulo de paso, espiral logarítmica, barra y brazo.
- 🎯 **Por qué importa:** Los brazos espirales son lo más llamativo de una galaxia de disco, pero la rotación diferencial debería enrollarlos hasta borrarlos en unas pocas vueltas. Entender esa paradoja es entender qué es un brazo: no un montón fijo de materia, sino un patrón.
- 🔗 **Se estudia junto con:** ángulo de paso, nudo, barra, rotación diferencial.

📘 **Dónde se aprende** (1 clase): [B25-C02 · Brazos espirales y barra galáctica](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md).

### Espiral tangencial

- La espiral tangencial mantiene el empuje en la dirección de la velocidad.

💡 **Cómo se explica en la clase [B81-C04](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md):**
- El script [espiral.py](espiral.py) calcula el `Δv` coplanar y con plano, integra la ecuación promediada e integra el movimiento de dos cuerpos con empuje tangencial hasta alcanzar el semieje final (comprueba las tolerancias de la cabecera).
- 🎯 **Por qué importa:** Una espiral de bajo empuje cuesta más `Δv` que un impulso (Hohmann) pero ahorra propelente por su alto `Isp`. La decisión central: ¿cuánto `Δv` y cuánto tiempo cuesta pasar de una órbita circular a otra, y cuánto más si además hay que cambiar el plano?
- 🔗 **Se estudia junto con:** fórmula de Edelbaum, ecuación promediada.

📘 **Dónde se aprende** (1 clase): [B81-C04 · Trayectorias espirales de bajo empuje](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md).

### Espora

- Una espora (en el sentido de la política) es el indicador definido en 5.
- Protección planetaria: control de la contaminación hacia adelante (de la Tierra a otro cuerpo) y hacia atrás. Espora: forma latente resistente.

💡 **Cómo se explica en la clase [B56-C17](../programa/clases/B56/B56-C17-control-de-contaminacion-biologica/CLASE.md):**
- Tras ese tiempo, la forma cerrada da `12 000` esporas (`300/m²`);
- Para una muestra de `0,01 m²` a `300/m²` (media 3), la probabilidad de no hallar ninguna espora es `e^{−3} = 0,050`.
- 🎯 **Por qué importa:** Una nave que lleva microorganismos terrestres puede contaminar otro mundo y confundir una futura búsqueda de vida. La política fija límites cuantitativos.
- 🔗 **Se estudia junto con:** carga biológica, valor D, reducción logarítmica, densidad.

📘 **Dónde se aprende** (2 clases): [B56-C17 · Control de contaminación biológica](../programa/clases/B56/B56-C17-control-de-contaminacion-biologica/CLASE.md); [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md).

### Esporádicos

- Los meteoros esporádicos (SPO) no pertenecen a una lluvia (S4).

💡 **Cómo se explica en la clase [B08-C18](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md):**
- La IMO (S4) pide estimar la magnitud límite en áreas definidas (dos o tres) y revisarla al menos cada hora, anotar el tipo (lluvia o esporádico) y el brillo de cada meteoro comparándolo con estrellas conocidas, tomar la hora y observar al menos una hora.
- 🎯 **Por qué importa:** Cada año, titulares prometen «cientos de estrellas fugaces por hora». Con un cielo contaminado o con el radiante bajo el horizonte, verás muy pocas.
- 🔗 **Se estudia junto con:** meteoroide, meteoro, meteorito, lluvia de meteoros.

📘 **Dónde se aprende** (1 clase): [B08-C18 · Introducción a meteoros y lluvias](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md).

### Espurio

- Un espurio es un producto no deseado `|m f_RF ± n f_OL|`.

💡 **Cómo se explica en la clase [B49-C11](../programa/clases/B49/B49-C11-mezcladores-de-frecuencia-perdida-de-conversion-y-productos-espurios/CLASE.md):**
- *Descripción textual:* la multiplicación crea suma y diferencia; los armónicos del OL crean espurios; la pérdida de conversión escala el ruido de la FI.
- Paso 4 · Espurio m = 3. `(2/π)/3 = 0,2122`.
- 🎯 **Por qué importa:** Cada producto no deseado puede caer en la banda de FI. La decisión central: ¿qué pérdida de conversión tiene el mezclador y dónde caen sus productos?
- 🔗 **Se estudia junto con:** pérdida de conversión, oscilador local, fuga, balanceado.

📘 **Dónde se aprende** (1 clase): [B49-C11 · Mezcladores de frecuencia: pérdida de conversión y productos espurios](../programa/clases/B49/B49-C11-mezcladores-de-frecuencia-perdida-de-conversion-y-productos-espurios/CLASE.md).

### Esquema

- Un esquema es el documento que dice qué etiquetas XML son válidas; este laboratorio no usa ninguno.
- Un esquema describe la forma de los datos.
- El esquema es la lista de campos exigidos.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C21](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md):**
- Límites: etiqueta inventada; sin esquema; sin SPICE; el valor del máximo depende de la semilla y de la versión de NumPy.
- 🎯 **Por qué importa:** Un archivo binario de una sonda planetaria son bytes sin significado: ¿cuántas filas?, ¿enteros o reales?, ¿qué orden de bytes?, ¿qué número indica «no hay dato»?, ¿qué unidad? Y para interpretarlo, hace falta saber dónde estaba la nave y hacia dónde apuntaba.
- 🔗 **Se estudia junto con:** producto, etiqueta, orden de bytes, valor especial.

📘 **Dónde se aprende** (4 clases): [B14-C21 · Datos de misiones planetarias: PDS4, etiquetas y SPICE](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md); [B14-C31 · APIs de servicios de datos](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md); [B120-C04 · Documentación regulatoria de un sistema satelital](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md); [B129-C04 · Contribución de medidas voluntarias con control de calidad](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md).

### Esquema BTCS

- El esquema BTCS (*backward time, centered space*) evalúa el término espacial en el instante nuevo: `−r u_{i−1}^{n+1} + (1 + 2r) u_i^{n+1} − r u_{i+1}^{n+1} = u_i^n`.

💡 **Cómo se explica en la clase [B11-C14](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md):**
- Usar el esquema implícito BTCS con un sistema tridiagonal.
- 🎯 **Por qué importa:** Casi todo código de simulación de calor, fluidos o plasma en una malla regular usa diferencias finitas. Elegir el paso de tiempo equivocado no da un resultado ligeramente malo: da un resultado que explota.
- 🔗 **Se estudia junto con:** malla, esquema FTCS, error de truncamiento, consistencia.

📘 **Dónde se aprende** (1 clase): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md).

### Esquema de diferencias centrales

- El esquema de diferencias centrales aproxima `y″(x_i) ≈ (y_{i+1} − 2y_i + y_{i−1})/h²`, con error `O(h²)` (S1, §3.4).

💡 **Contexto en la clase [B11-C12](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md):**
- **Idea central (modelo mental):** El problema de valor inicial es disparar y mirar dónde cae. El de frontera es acertar a un blanco fijo: se dispara, se mide la desviación y se corrige el ángulo. El método de diferencias finitas es distinto: se pide a todos los puntos de la malla que se acomoden a la vez entre las dos paredes.
- 🎯 **Por qué importa:** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.
- 🔗 **Se estudia junto con:** problema de frontera, Dirichlet, Neumann, mixtas.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Esquema de Horn

- El esquema de Horn calcula derivadas con una ventana de 3 × 3 ponderada.

💡 **Cómo se explica en la clase [B53-C20](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md):**
- Calcular la pendiente de un MDE con el esquema de Horn.
- 🎯 **Por qué importa:** Un derivado sin verificar propaga errores a la decisión. La decisión central: ¿qué parte del terreno cumple un criterio de pendiente y existe un camino que lo respete?
- 🔗 **Se estudia junto con:** sombreado, máscara de transitabilidad, búsqueda en anchura.

📘 **Dónde se aprende** (1 clase): [B53-C20 · Proyecto SIG de terreno extraterrestre](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md).

### Esquema de Horner

- El esquema de Horner reescribe `a₀ + a₁x + a₂x² + a₃x³` como `a₀ + x(a₁ + x(a₂ + x a₃))`, lo que evita calcular potencias altas por separado.

💡 **Cómo se explica en la clase [B04-C01](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md):**
- El esquema de Horner es más económico y estable con coeficientes de órdenes de magnitud muy distintos.
- Evaluar un polinomio con el esquema de Horner y comprobar el resultado con la forma directa.
- 🎯 **Por qué importa:** Cuando un observatorio publica dónde está inclinado el eje de la Tierra, no da un solo número: da una *fórmula* para cada fecha, porque ese eje se mueve lentamente. Esa fórmula es un polinomio.
- 🔗 **Se estudia junto con:** polinomio, coeficientes, término independiente, grado.

📘 **Dónde se aprende** (1 clase): [B04-C01 · Polinomios y factorización](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md).

### Esquema de salto de rana

- El esquema de salto de rana avanza en tres niveles de tiempo.

💡 **Cómo se explica en la clase [B30-C09](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md):**
- Simular el pulso con un esquema de salto de rana y la condición CFL.
- 🎯 **Por qué importa:** La velocidad de Alfvén fija cuánto tarda una perturbación en recorrer un lazo coronal o una línea de campo del viento solar. La decisión central: ¿con qué velocidad viaja una perturbación magnética y cómo cambia el tiempo de viaje en un medio estratificado?
- 🔗 **Se estudia junto con:** MHD ideal, onda de Alfvén, condición CFL, aproximación WKB.

📘 **Dónde se aprende** (1 clase): [B30-C09 · Magnetohidrodinámica](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md).

### Esquema FTCS

- El esquema FTCS (*forward time, centered space*) es `u_i^{n+1} = u_i^n + r (u_{i+1}^n − 2u_i^n + u_{i−1}^n)`, con `r = α Δt/Δx²`.

💡 **Cómo se explica en la clase [B11-C14](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md):**
- *Descripción textual:* con FTCS, cada nodo se actualiza con sus vecinos; si `r ≤ 1/2` el esquema es estable y suaviza, y si no, las oscilaciones de nodo a nodo crecen;
- Con el esquema FTCS y `r = 0,4`, una malla de 10, 20 y 40 intervalos da `0,670709`, `0,673056` y `0,673634`: el error baja a la cuarta parte cada vez que se duplica la malla.
- 🎯 **Por qué importa:** Casi todo código de simulación de calor, fluidos o plasma en una malla regular usa diferencias finitas. Elegir el paso de tiempo equivocado no da un resultado ligeramente malo: da un resultado que explota.
- 🔗 **Se estudia junto con:** malla, esquema BTCS, error de truncamiento, consistencia.

📘 **Dónde se aprende** (1 clase): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md).

### Esquina

- El centro del píxel es su punto medio; la esquina su punto superior izquierdo.
- Característica local: punto distintivo de una imagen y su entorno. Esquina: punto donde la intensidad varía en dos direcciones.

💡 **Cómo se explica en la clase [B14-C26](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md):**
- La geotransformación del ejemplo: origen en la esquina superior izquierda `(10,0°; 40,0°)` y píxel de 0,001° con el norte arriba.
- Con la convención «el píxel `(fila, col)` cubre desde `lon0 + col·dx` hasta `lon0 + (col+1)·dx` y desde `lat0 − (fila+1)·dy` hasta `lat0 − fila·dy`», el centro del píxel `(0, 0)` es `(10,0005°; 39,9995°)` y la esquina `(10,0°; 40,0°)` cae en el píxel `(0, 0)`.
- ⚠️ **Error frecuente:** Confundir esquina y centro del píxel. Se corrige con los ejercicios 6 y 10.
- 🎯 **Por qué importa:** Una escena de satélite pesa cientos de megabytes y tú necesitas un recuadro de 100 × 120 píxeles. Si el formato obliga a leer todo el archivo, gastas tiempo y ancho de banda.
- 🔗 **Se estudia junto con:** ráster, GeoTIFF, tesela, directorio de teselas.

📘 **Dónde se aprende** (2 clases): [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md); [B99-C02 · Detección y descriptores de características](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md).

### Estabilidad

- La masa formular es la masa molar de la fórmula; la estabilidad de un hielo, en esta clase, es el intervalo de presiones y temperaturas donde no sublima (C11).
- La estabilidad (no explotar) es distinta de la precisión (parecerse a la solución).
- La consistencia es que el error de truncamiento tienda a cero; la estabilidad, que los errores no crezcan.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Sólo toma dos cifras (la temperatura de 176 K y la clasificación de las especies) para ejercitar el cálculo de energías y de estabilidad.
- Ejercicio 6. Calcula la presión mínima de estabilidad del hielo de CO₂ a 170 K con `ΔH_sub = 26,1 kJ/mol`.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).
- 🔗 **Se estudia junto con:** hielo, mineral, olivino, forsterita.

📘 **Dónde se aprende** (8 clases): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md); [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md); [B13-C23 · Estabilidad y deriva temporal de instrumentos](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md); [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md); [B84-C24 · Factores de seguridad y márgenes estructurales](../programa/clases/B84/B84-C24-factores-de-seguridad-y-margenes-estructurales/CLASE.md) y 2 más.

### Estabilidad asintótica global

- La estabilidad asintótica global significa que toda trayectoria tiende al equilibrio.

💡 **Contexto en la clase [B16-C17](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md):**
- **Idea central (modelo mental):** La función de Lyapunov es como la altura de una bola en un paisaje: si el control garantiza que la bola siempre baja (o se queda), y el único punto de reposo es el fondo, la bola termina en el fondo sin importar de dónde parta. No hace falta resolver las ecuaciones.
- 🎯 **Por qué importa:** Cuando un satélite se separa del cohete puede salir girando de forma desordenada («volteando»).
- 🔗 **Se estudia junto con:** ecuaciones de Euler, momento angular, energía cinética de rotación, eje principal.

📘 **Dónde se aprende** (1 clase): [B16-C17 · Control no lineal](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md).

### Estabilidad de frecuencia

- La estabilidad de frecuencia describe cómo fluctúa `y` en el tiempo.

💡 **Contexto en la clase [B13-C07](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md):**
- **Idea central (modelo mental):** La desviación de Allan es una lupa con la que miras la serie a distintas escalas de tiempo. A escalas cortas domina el ruido rápido; a largas, la deriva. La curva ADEV frente a `τ` suele tener forma de «V»: baja mientras el promedio reduce el ruido y sube cuando la deriva empieza a pesar.
- 🎯 **Por qué importa:** Dos relojes pueden tener la misma desviación de frecuencia media y comportarse de forma muy distinta: uno oscila alrededor de su valor y otro se aleja de él con el tiempo. La desviación típica ordinaria no sirve para describirlo, porque en un reloj con deriva no converge.
- 🔗 **Se estudia junto con:** promedio, varianza de Allan, desviación de Allan, ruido blanco de frecuencia.

📘 **Dónde se aprende** (1 clase): [B13-C07 · Relojes atómicos y frecuencia](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md).

### Estabilidad estática

- La estabilidad estática exige `Cm_α < 0`: un aumento de `α` genera un par que lo reduce.

💡 **Cómo se explica en la clase [B77-C17](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md):**
- Definir estabilidad estática por el signo de `Cm_α`.
- ⚠️ **Error frecuente:** Confundir estabilidad estática con ausencia de oscilación. Se corrige con 8.3.
- 🎯 **Por qué importa:** Una cápsula inestable no entra con el escudo hacia delante. La decisión central: ¿qué pendiente de momento da una oscilación acotada y cuánto tarda en divergir una inestable?
- 🔗 **Se estudia junto con:** ángulo de equilibrio, frecuencia natural, amortiguamiento, divergencia.

📘 **Dónde se aprende** (1 clase): [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md).

### Estabilidad lineal

- La estabilidad lineal no garantiza la estabilidad no lineal.

💡 **Cómo se explica en la clase [B73-C04](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de estabilidad de cinco puntos y tres sistemas*: tabla de autovalores, tiempos de crecimiento, indicador de Routh, validación por diferencias finitas y por integración no lineal, y lista de límites.
- ⚠️ **Error frecuente:** Concluir estabilidad total de un centro×centro lineal. Se corrige con 8.5.
- 🎯 **Por qué importa:** Que un punto sea de equilibrio no dice si una nave se queda o se va. Los autovalores dicen cuánto tiempo tienes antes de corregir la posición y si un grupo de asteroides puede quedarse en L4.
- 🔗 **Se estudia junto con:** ecuación característica, silla×centro, centro×centro, tiempo de crecimiento.

📘 **Dónde se aprende** (1 clase): [B73-C04 · Estabilidad local de Lagrange](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md).

### Estabilidad numérica

- La estabilidad numérica es la capacidad de un cálculo de no perder cifras.

💡 **Cómo se explica en la clase [B07-C17](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md):**
- ⚠️ **Error frecuente:** Ignorar la estabilidad numérica. Se corrige con la sección 8.6 y el ejercicio 8.
- 🎯 **Por qué importa:** Una función matemática puede dar el resultado correcto en el único caso que probaste y estar mal en los demás. Y es fácil escribir una prueba que no puede fallar: la que compara la función contra sí misma o contra un caso donde el error se esconde.
- 🔗 **Se estudia junto con:** prueba, parametrización, caso analítico, propiedad.

📘 **Dónde se aprende** (1 clase): [B07-C17 · Pruebas de funciones matemáticas](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md).

### Estabilidad progrado y retrógrada

- La estabilidad progrado y retrógrada se mide por el semieje máximo de una órbita circular que no escapa.

💡 **Contexto en la clase [B73-C18](../programa/clases/B73/B73-C18-satelites-irregulares/CLASE.md):**
- 🎯 **Por qué importa:** Los satélites irregulares son capturas: están lejos, en órbitas que ningún proceso de formación local explica. Ocupan una fracción de la esfera de Hill que depende del sentido de giro.
- 🔗 **Se estudia junto con:** satélites irregulares, radio de Hill, grupos de inclinación, inclinación crítica de Kozai.

📘 **Dónde se aprende** (1 clase): [B73-C18 · Satélites irregulares](../programa/clases/B73/B73-C18-satelites-irregulares/CLASE.md).

### Estabilización

- La estabilización de imagen o un trípode reducen el temblor.
- La estabilización se da cuando `|dT/dt|` cae bajo el criterio.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- NASA recomienda, para empezar, entre 7×35 y 10×50: con más aumento el campo es más estrecho, pesan más y se sacuden, salvo con estabilización o trípode (S2, S3).
- Trípode con adaptador estabiliza y permite 10× o más, a costa de comodidad.
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?
- 🔗 **Se estudia junto con:** aumento, objetivo, pupila de salida, campo de visión.

📘 **Dónde se aprende** (2 clases): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md); [B85-C19 · Ensayos de vacío térmico](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md).

### Estable

- Un ordenamiento es estable si los elementos con la misma clave conservan su orden relativo (S2).
- El método es estable para un `z` si `|R(z)| ≤ 1`; la región de estabilidad es el conjunto de `z` donde ocurre.
- Un LTI es estable (en el sentido que usaremos) si su respuesta al impulso tiende a cero.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- Es estable si, en un empate, se toma primero el elemento de la mitad izquierda (como hace el laboratorio).
- Explicar el significado de «estable» y verificarlo.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.
- 🔗 **Se estudia junto con:** búsqueda lineal, búsqueda binaria, ordenada, ordenamiento por inserción.

📘 **Dónde se aprende** (6 clases): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md); [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B54-C19 · Modelos climáticos planetarios](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md); [B73-C06 · Variedades invariantes](../programa/clases/B73/B73-C06-variedades-invariantes/CLASE.md); [B77-C21 · Centro de presión y margen estático](../programa/clases/B77/B77-C21-centro-de-presion-y-margen-estatico/CLASE.md).

### Estación

- Pasada: ventana de visibilidad de un satélite. Estación: antena que atiende una pasada a la vez.

💡 **Cómo se explica en la clase [B96-C17](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md):**
- El capítulo de la NASA sobre sistemas terrestres (S1) describe redes de estaciones, como la Near Space Network y proveedores comerciales, y servicios de planificación y programación; también indica que la licencia de bandas tarda meses.
- Se maximiza `Σ wᵢ` sobre las pasadas atendidas con la restricción de no solape por estación.
- ⚠️ **Error frecuente:** Asignar sin comprobar solapes. Verifica cada estación (8.2)
- 🎯 **Por qué importa:** Dos pasadas que se solapan en la misma antena obligan a elegir; sin coordinación se pierde la más valiosa. La decisión central: ¿qué pasadas se atienden y desde qué estación para maximizar el valor sin solapes?
- 🔗 **Se estudia junto con:** Pasada, Asignación, Peso, Brecha.

📘 **Dónde se aprende** (1 clase): [B96-C17 · Coordinación de múltiples estaciones](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md).

### Estación de eclipses

- Una estación de eclipses es el período en que la órbita de la Luna cruza el plano de la órbita de la Tierra; ocurre dos veces al año (S3).

💡 **Cómo se explica en la clase [B08-C09](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md):**
- Para las lunas llenas, el criterio de umbra (separación con el punto antisolar menor que ≈ 0,9°–1,0°) da dos candidatas en 2025: 14 de marzo (0,56°) y 7 de septiembre (0,72°); la confirmación con la lista de eclipses lunares de la NASA no se consultó en esta clase.
- Ejercicio 4. Con la inclinación de 5,145° (S4) y el límite de ≈ 1,5° para el eclipse solar, explica por qué hay eclipses solo en estaciones.
- 🎯 **Por qué importa:** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?
- 🔗 **Se estudia junto con:** umbra, penumbra, solar, lunar.

📘 **Dónde se aprende** (1 clase): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md).

### Estación de mantenimiento

- Una estación de mantenimiento permite diagnosticar y reparar equipos.

💡 **Cómo se explica en la clase [B109-C11](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md):**
- La estación de mantenimiento ocupa `3,28 m³` en `1,37 m²`, es decir, `2,394 m` de altura: coincide con la altura estándar `2,4 m` (tolerancia del `0,5 %`).
- Ejercicio 6 · autónomo. Altura implícita de la estación de mantenimiento.
- 🎯 **Por qué importa:** Un equipo que no se puede abrir o extraer no se puede reparar, y en un hábitat sin taller externo eso es un riesgo de misión. La decisión central: ¿hay área, paso y holgura para trabajar y mantener cada equipo, y dónde falta?
- 🔗 **Se estudia junto con:** estación de trabajo, holgura, extracción, accesibilidad de un equipo.

📘 **Dónde se aprende** (1 clase): [B109-C11 · Diseño de espacios de trabajo, mantenimiento y laboratorio](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md).

### Estación de seguimiento

- Estación de seguimiento: antena, receptor y software que rastrean la nave.

💡 **Cómo se explica en la clase [B96-C05](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md):**
- python programa/clases/B96/B96-C05-estaciones-de-seguimiento/pasada_con_doppler.py
- 🎯 **Por qué importa:** Para que una antena apunte y un receptor enganche, la estación debe conocer de antemano el azimut, la elevación y el corrimiento de frecuencia. La decisión central: ¿hacia dónde apuntar y qué frecuencia esperar en cada instante?
- 🔗 **Se estudia junto con:** Azimut/elevación, Rango, Doppler, Velocidad radial.

📘 **Dónde se aprende** (1 clase): [B96-C05 · Estaciones de seguimiento](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md).

### Estación de trabajo

- Una estación de trabajo es el lugar donde se hace una tarea.

💡 **Contexto en la clase [B109-C11](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md):**
- 🎯 **Por qué importa:** Un equipo que no se puede abrir o extraer no se puede reparar, y en un hábitat sin taller externo eso es un riesgo de misión. La decisión central: ¿hay área, paso y holgura para trabajar y mantener cada equipo, y dónde falta?
- 🔗 **Se estudia junto con:** estación de mantenimiento, holgura, extracción, accesibilidad de un equipo.

📘 **Dónde se aprende** (1 clase): [B109-C11 · Diseño de espacios de trabajo, mantenimiento y laboratorio](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md).

### Estacionaria

- La respuesta transitoria es la parte que se extingue con el tiempo; la estacionaria es la que queda cuando el transitorio desapareció.

💡 **Cómo se explica en la clase [B16-C04](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md):**
- Para nuestro estudio, esas dos fases son exactamente la respuesta transitoria (cómo llega) y la respuesta estacionaria (dónde se queda).
- Distinguir la parte transitoria de la estacionaria de una respuesta.
- 🎯 **Por qué importa:** Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación.
- 🔗 **Se estudia junto con:** respuesta transitoria, constante de tiempo, frecuencia natural, amortiguamiento.

📘 **Dónde se aprende** (1 clase): [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md).

### Estadio

- La circunferencia es la longitud del contorno de un círculo; el estadio es una unidad antigua de longitud cuyo valor exacto se discute.

💡 **Cómo se explica en la clase [B02-C03](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md):**
- La distancia cenital en Alejandría fue de 7°12′ (7,2°, o 1/50 de círculo); con unos 5 000 estadios entre las ciudades la circunferencia sale `5 000 × 50 = 250 000` estadios, la cifra que se le atribuye (S2).
- MacTutor recoge además la tesis de Rawlins de que esa medición angular fue la única que Eratóstenes hizo por sí mismo, con un error de unos 16′ (S2); los 5 000 estadios aparecen en la fuente solo de forma indirecta, en el título de una referencia.
- ⚠️ **Error frecuente:** Decir que acertó con un error de 1 %. Depende del estadio.
- 🎯 **Por qué importa:** Un modelo geométrico responde a «¿qué figura reproduce estos movimientos?». Es una forma nueva de preguntar frente a la regla puramente numérica.
- 🔗 **Se estudia junto con:** circunferencia, meridiano, precesión de los equinoccios, catálogo estelar.

📘 **Dónde se aprende** (1 clase): [B02-C03 · Astronomía griega y helenística](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md).

### Estadística

- Una estadística es una función de los datos de la muestra; una estimación es la operación de asignar valores numéricos a los parámetros a partir de una muestra, un estimador es la estadística usada para ello y una estimación (resultado) es su valor para una muestra concreta (S1, C.2.23–C.2.26).

💡 **Contexto en la clase [B12-C07](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md):**
- **Idea central (modelo mental):** Dado un modelo, cada valor posible del parámetro asigna una probabilidad a los datos que viste. El MLE es el valor que le da la mayor. La curvatura de `ℓ` alrededor del máximo dice cuánto confiar: un pico agudo indica un parámetro bien determinado; uno plano, poco.
- 🎯 **Por qué importa:** Una misión no «conoce» la tasa de impactos ni el ruido de su sensor: los estima a partir de unas decenas de datos. Un estimador mal elegido, o mal interpretado, da parámetros sesgados o con una confianza injustificada.
- 🔗 **Se estudia junto con:** estimación, estimador, estimación, verosimilitud.

📘 **Dónde se aprende** (1 clase): [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md).

### Estadística de Cash

- La estadística de Cash `C = 2Σ(μ − n ln μ)`.

💡 **Cómo se explica en la clase [B27-C22](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md):**
- Con pocas cuentas, el `χ²` con varianza igual a las observadas da un espectro sistemáticamente más blando (`Γ` mayor) y más disperso; la estadística de Cash casi no tiene sesgo.
- Escribir la estadística de Cash y el `χ²` con varianza igual a las cuentas.
- 🎯 **Por qué importa:** Ajustar un espectro «de fotones» directamente a las cuentas da resultados engañosos; hay que plegar el modelo con la respuesta y usar la estadística correcta para conteos pequeños. La decisión central: ¿qué parámetros recupera cada estadística y con qué sesgo cuando las cuentas son pocas?
- 🔗 **Se estudia junto con:** ARF, RMF, plegado, χ² con varianza igual a las cuentas.

📘 **Dónde se aprende** (1 clase): [B27-C22 · Análisis espectral de rayos X y gamma: ajuste con respuesta instrumental](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md).

### Estadística de Poisson

- La estadística de Poisson: media igual a varianza.

💡 **Cómo se explica en la clase [B47-C03](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md):**
- Simular la estadística de Poisson con semilla fija.
- 🎯 **Por qué importa:** En el ultravioleta cada fotón es valioso: las tasas son bajas y el ruido es de Poisson. La decisión central: ¿cuánto hay que exponer para llegar a una relación señal/ruido de 10?
- 🔗 **Se estudia junto con:** ultravioleta, serie de Lyman, constante de Rydberg, fotón detectado.

📘 **Dónde se aprende** (1 clase): [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md).

### Estadísticas zonales

- Las estadísticas zonales resumen una capa por zona.

💡 **Cómo se explica en la clase [B57-C19](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de análisis de riesgo*: la tabla de pesos y consistencia, el solape entre métodos, la sensibilidad a pesos y las estadísticas zonales.
- 🎯 **Por qué importa:** Los mapas de riesgo orientan decisiones y presupuestos, pero dependen de supuestos de ponderación que suelen quedar ocultos. La decisión central: ¿cómo combino capas y cuánto cambian las zonas prioritarias si cambio los pesos?
- 🔗 **Se estudia junto con:** amenaza, exposición, vulnerabilidad, proceso analítico jerárquico (AHP).

📘 **Dónde se aprende** (1 clase): [B57-C19 · SIG y análisis de riesgo](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md).

### Estadístico

- El perfilado determinista instrumenta cada evento de llamada; el estadístico muestrea.

💡 **Cómo se explica en la clase [B18-C04](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md):**
- El perfilado estadístico perturba menos y sirve para programas largos, pero da solo proporciones aproximadas y no cuenta llamadas (S1).
- El estadístico muestrea periódicamente el puntero de instrucciones y deduce dónde se gasta el tiempo; añade menos sobrecoste, pero da solo indicaciones relativas.
- 🎯 **Por qué importa:** Casi todo programa científico tiene un cuello de botella que el autor no sospecha. Optimizar a ojo suele mejorar lo que no importa.
- 🔗 **Se estudia junto con:** perfil, perfilador, cuello de botella, perfilado determinista.

📘 **Dónde se aprende** (1 clase): [B18-C04 · Perfilado de rendimiento](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md).

### Estadístico de chequeo

- Un estadístico de chequeo `T(y)` resume una característica de los datos que importa para la pregunta (aquí, el índice de dispersión `T = varianza/media`).

💡 **Cómo se explica en la clase [B19-C06](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md):**
- Límite de la analogía: el chequeo es siempre *relativo a un estadístico*.
- Diseñar un estadístico de chequeo y calcular un valor p predictivo posterior por simulación.
- ⚠️ **Error frecuente:** Elegir el estadístico después de ver el resultado. Sesga el chequeo: se declara antes.
- 🎯 **Por qué importa:** El contador de partículas lleva 12 horas midiendo. Con la posterior de la tasa `λ`, la pregunta práctica es: ¿cuántos eventos esperar en la hora 13, y qué tan sorprendente sería ver 8?
- 🔗 **Se estudia junto con:** distribución predictiva posterior, réplica, predictiva a priori, valor p predictivo posterior.

📘 **Dónde se aprende** (1 clase): [B19-C06 · Distribución predictiva posterior](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md).

### Estadístico de detección

- El estadístico de detección `J = |r|²/σ²` sigue una chi-cuadrado con `n − 3` grados de libertad sin falla.

💡 **Contexto en la clase [B80-C05](../programa/clases/B80/B80-C05-redundancia-de-sensores-y-arbitraje-de-mediciones/CLASE.md):**
- 🎯 **Por qué importa:** B88-C12 trata la detección y recuperación de fallas en general, no el arbitraje de las mediciones que alimentan la navegación. La decisión central: ¿cómo sabe el sistema que un sensor miente, y cuál es, sin una referencia externa?
- 🔗 **Se estudia junto con:** espacio de paridad, residuo, aislamiento.

📘 **Dónde se aprende** (1 clase): [B80-C05 · Redundancia de sensores y arbitraje de mediciones](../programa/clases/B80/B80-C05-redundancia-de-sensores-y-arbitraje-de-mediciones/CLASE.md).

### Estadístico de Grubbs

- El estadístico de Grubbs es `G = máx|Yᵢ − Ȳ| / s` (S2).

💡 **Cómo se explica en la clase [B12-C19](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md):**
- Calcular el estadístico de Grubbs y compararlo con su valor crítico.
- 🎯 **Por qué importa:** Un dato aberrante puede ser un error del instrumento, una pérdida de sincronía o el primer indicio de un fenómeno real. Eliminarlo sin criterio esconde información; conservarlo sin revisar contamina el resultado.
- 🔗 **Se estudia junto con:** valor atípico, un solo, puntaje z modificado, distancia de Mahalanobis.

📘 **Dónde se aprende** (1 clase): [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md).

### Estadístico de habilidad verdadera

- El estadístico de habilidad verdadera `TSS = POD − POFD` no depende de la tasa base.

💡 **Contexto en la clase [B12-C24](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md):**
- **Idea central (modelo mental):** Una métrica de habilidad pregunta: ¿cuánto mejor es este pronóstico que uno trivial que ignora los datos del día? El trivial más usual es la climatología (siempre la tasa histórica) o la persistencia (lo que pasó ayer). Un pronóstico útil le gana, y la medida es cuánto.
- 🎯 **Por qué importa:** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.
- 🔗 **Se estudia junto con:** puntaje de Brier, referencia climatológica, puntaje de habilidad de Brier, tabla de contingencia.

📘 **Dónde se aprende** (1 clase): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md).

### Estadístico de Mann–Whitney

- El estadístico de Mann–Whitney es la probabilidad de que una puntuación de suceso supere a una de no suceso.

💡 **Contexto en la clase [B33-C14](../programa/clases/B33/B33-C14-verificacion-de-alertas-con-tablas-de-contingencia/CLASE.md):**
- **Idea central (modelo mental):** Girar la perilla de sensibilidad recorre la curva ROC: más sensibilidad, más detecciones y más falsas alarmas.
- 🎯 **Por qué importa:** La verificación decide si una alerta merece confianza. La decisión central: ¿cómo resumir la capacidad de discriminar de un pronóstico?
- 🔗 **Se estudia junto con:** curva ROC, AUC, sesgo de frecuencia.

📘 **Dónde se aprende** (1 clase): [B33-C14 · Verificación de alertas con tablas de contingencia](../programa/clases/B33/B33-C14-verificacion-de-alertas-con-tablas-de-contingencia/CLASE.md).

### Estadístico de prueba

- Un estadístico de prueba es una función de los datos con distribución conocida bajo `H₀`; aquí `z = (H₂ − H₁)/√(s₁² + s₂²)`.

💡 **Cómo se explica en la clase [B12-C09](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md):**
- Con un efecto real `δ = 1 m`, `σ = 3 m` y `n = 25`, el estadístico se desplaza `δ√n/σ = 1,667` errores típicos y la potencia de la prueba bilateral al 5 % es `0,385` (simulada `0,387`): la prueba pasa por alto el efecto el 61 % de las veces.
- 🎯 **Por qué importa:** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.
- 🔗 **Se estudia junto con:** hipótesis nula, alternativa, valor p, si H₀ fuera cierta.

📘 **Dónde se aprende** (1 clase): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md).

### Estadístico R̂

- El estadístico `R̂` (Gelman–Rubin) compara la varianza entre cadenas con la de dentro de cada una: si todas las cadenas muestrean la misma distribución, `R̂ ≈ 1`; si están en regiones distintas, `R̂ > 1`.

💡 **Contexto en la clase [B12-C23](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md):**
- **Idea central (modelo mental):** Si cuatro exploradores salen de puntos distintos de un territorio y, tras un tiempo, describen el mismo paisaje, es creíble que lo conocen. Si cada uno describe un valle distinto, no. `R̂` es esa comparación;
- 🎯 **Por qué importa:** Un análisis MCMC cuya cadena no convergió da intervalos falsos con apariencia de precisión; y uno que no se puede repetir es irrevisable. En una misión, un parámetro estimado con cadenas defectuosas puede determinar una maniobra o un diagnóstico de salud de un instrumento.
- 🔗 **Se estudia junto con:** tiempo de autocorrelación integrado, tamaño muestral efectivo, reproducibilidad, huella.

📘 **Dónde se aprende** (1 clase): [B12-C23 · Diagnóstico de convergencia y reproducibilidad de cadenas MCMC](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md).

### Estado

- El estado es el conjunto de esos valores.
- El estado `x` es el menor conjunto de variables que, junto con la entrada futura, determina todo el futuro del sistema.
- El estado es el par posición–velocidad en un instante.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C02](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md):**
- A["EDO de orden m"] --> B["Estado inicial:<br/>y y sus m−1 derivadas<br/>en t₀"]
- *Descripción textual:* para una EDO de orden `m` se fija el estado inicial; si la función `f` es lipschitziana la solución es única; luego se pregunta cuánto crece una diferencia inicial, lo que limita el horizonte útil de predicción.
- 🎯 **Por qué importa:** Una nave no sigue «la» solución de las ecuaciones del movimiento: sigue la que corresponde a *su* posición y velocidad en el instante en que se midieron. Saber cuántos datos exige la ecuación, cuándo garantizan una única trayectoria y cuánto se amplifica su error es la base de toda predicción de trayectoria.
- 🔗 **Se estudia junto con:** problema de valor inicial, instante inicial, bien planteada, constante de Lipschitz.

📘 **Dónde se aprende** (6 clases): [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md); [B71-C10 · Semieje mayor y excentricidad](../programa/clases/B71/B71-C10-semieje-mayor-y-excentricidad/CLASE.md); [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md); [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md).

### Estado aumentado

- El sesgo (*bias*) `b` es un offset de la medida del giróscopo; se modela como un estado constante `ḃ = 0` (estado aumentado).

💡 **Contexto en la clase [B16-C14](../programa/clases/B16/B16-C14-observadores-de-estados/CLASE.md):**
- **Idea central (modelo mental):** Haz funcionar una copia del sistema en el computador de a bordo, alimentada con las mismas órdenes. Si la copia coincidiera exactamente con la realidad, no haría falta medir. Como nunca coincide, se compara su salida con la medida y se usa la diferencia para empujar la copia hacia la realidad.
- 🎯 **Por qué importa:** Los sensores miden poco y mal: un rastreador de estrellas da la orientación, pero a baja frecuencia y con ruido; un giróscopo da la velocidad con un sesgo que deriva. El controlador necesita el estado completo (C15) y limpio.
- 🔗 **Se estudia junto con:** observador de estados, ganancia del observador, error de estimación, sesgo.

📘 **Dónde se aprende** (1 clase): [B16-C14 · Observadores de estados](../programa/clases/B16/B16-C14-observadores-de-estados/CLASE.md).

### Estado de carga

- El estado de carga (SOC) es la fracción restante.

💡 **Contexto en la clase [B86-C05](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md):**
- 🎯 **Por qué importa:** Una batería de órbita baja hace unos `5400` ciclos al año. Dimensionarla por la energía de un solo eclipse sin mirar la profundidad de descarga la agota mucho antes del fin de la misión.
- 🔗 **Se estudia junto con:** capacidad, energía, DoD, tensión de circuito abierto.

📘 **Dónde se aprende** (1 clase): [B86-C05 · Baterías de ion-litio](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md).

### Estado de error

- El estado de error es `(δθ, Δb)` con `A_true = (I − [δθ×]) Â`.

💡 **Cómo se explica en la clase [B87-C10](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md):**
- Plantear el estado de error `x = (δθ, Δb)` y su dinámica `δθ̇ = −ω̂×δθ − Δb − η_v`.
- El script [mekf.py](mekf.py) simula la actitud verdadera, el giroscopio con ARW, RRW y sesgo, y los vectores con ruido; ejecuta el MEKF de 6 estados, el giroscopio solo y el SVD por época; y calcula el NEES (comprueba error del giroscopio solo `> 10×` el del filtro, filtro mejor que el SVD, error de sesgo `< 30 %` y NEES razonable).
- ⚠️ **Error frecuente:** Filtrar el cuaternión como si fuera un vector de 4 estados. Filtra el error de 3 componentes (8.1)
- 🎯 **Por qué importa:** Un giroscopio sin corregir se desvía decenas de grados en minutos; un vector solo da `~1°` por época. La decisión central: ¿cómo se combinan para obtener una actitud mejor que cada uno, y cómo se sabe que el filtro es honesto?
- 🔗 **Se estudia junto con:** estado nominal, propagación, actualización, reinicio.

📘 **Dónde se aprende** (1 clase): [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md).

### Estado de lanzamiento

- El Estado de lanzamiento es el que lanza, hace lanzar o cede territorio o instalación.
- El Estado de lanzamiento es el que lanza o hace lanzar.
- El Estado de lanzamiento y el Estado de registro pueden ser distintos.

💡 **Cómo se explica en la clase [B118-C18](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md):**
- II (el Estado de lanzamiento registra el objeto).
- II: responsabilidad absoluta del Estado de lanzamiento por el daño en la superficie.
- ⚠️ **Error frecuente:** Confundir Estado de lanzamiento y de registro. Se corrige con el vocabulario y el ejercicio 6.
- 🎯 **Por qué importa:** Con decenas de miles de objetos, comparar todos los pares es costoso; un buen cribado descarta de entrada los pares imposibles sin perder ninguno posible. Y cuando algo sale mal, los tratados determinan responsabilidad y jurisdicción.
- 🔗 **Se estudia junto con:** cribado, filtro de apsis, Estado de registro, responsabilidad absoluta.

📘 **Dónde se aprende** (3 clases): [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md); [B119-C04 · Convenio de Registro](../programa/clases/B119/B119-C04-convenio-de-registro/CLASE.md); [B119-C33 · Matriz comparativa de obligaciones jurídicas por actor](../programa/clases/B119/B119-C33-matriz-comparativa-de-obligaciones-juridicas-por-actor/CLASE.md).

### Estado de registro

- El Estado de registro lleva el registro y conserva jurisdicción y control.
- El Estado de lanzamiento y el Estado de registro pueden ser distintos.

💡 **Cómo se explica en la clase [B118-C18](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md):**
- VIII: el Estado de registro conserva jurisdicción y control.
- VIII (jurisdicción y control del Estado de registro) y art.
- ⚠️ **Error frecuente:** Confundir Estado de lanzamiento y de registro. Se corrige con el vocabulario y el ejercicio 6.
- 🎯 **Por qué importa:** Con decenas de miles de objetos, comparar todos los pares es costoso; un buen cribado descarta de entrada los pares imposibles sin perder ninguno posible. Y cuando algo sale mal, los tratados determinan responsabilidad y jurisdicción.
- 🔗 **Se estudia junto con:** cribado, filtro de apsis, Estado de lanzamiento, responsabilidad absoluta.

📘 **Dónde se aprende** (2 clases): [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md); [B119-C33 · Matriz comparativa de obligaciones jurídicas por actor](../programa/clases/B119/B119-C33-matriz-comparativa-de-obligaciones-juridicas-por-actor/CLASE.md).

### Estado donde la unidad ya no cambia apreciablemente

- Estabilización: estado donde la unidad ya no cambia apreciablemente. Margen de ensayo: diferencia entre la temperatura de ensayo y la prevista en órbita.

💡 **Contexto en la clase [B90-C11](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md):**
- 🎯 **Por qué importa:** Una prueba funcional hecha antes de que la unidad se estabilice no demuestra nada sobre la temperatura extrema; una espera excesiva consume cámara y calendario. La decisión central: ¿cuánto debe esperar el ensayo para que la temperatura de la unidad sea la de la prueba?
- 🔗 **Se estudia junto con:** Nodo concentrado, Constante de tiempo τ, Rampa, tiempo a temperatura constante.

📘 **Dónde se aprende** (1 clase): [B90-C11 · Ensayos térmicos](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md).

### Estado estacionario

- El estado estacionario es `n_ss = P/D`.
- Un estado estacionario es el valor al que tiende la respuesta.
- El estado estacionario `x* = a d / r` es la carga a la que tiende el sistema con demanda constante.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B55-C04](../programa/clases/B55/B55-C04-quimica-de-nubes-moleculares/CLASE.md):**
- Hallar el estado estacionario `n = P/D` y la escala `τ = 1/D`.
- 🎯 **Por qué importa:** Una nube molecular fría es un reactor lento sostenido por una fuente débil de ionización. Entender el balance de una sola especie clave enseña a leer cualquier red.
- 🔗 **Se estudia junto con:** balance, ionización por rayos cósmicos, recombinación disociativa.

📘 **Dónde se aprende** (4 clases): [B55-C04 · Química de nubes moleculares](../programa/clases/B55/B55-C04-quimica-de-nubes-moleculares/CLASE.md); [B77-C23 · Estabilidad de vuelo de lanzadores en ascenso](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md); [B106-C04 · Control de dióxido de carbono](../programa/clases/B106/B106-C04-control-de-dioxido-de-carbono/CLASE.md); [B113-C01 · Estrés operacional y estrategias de afrontamiento](../programa/clases/B113/B113-C01-estres-operacional-y-estrategias-de-afrontamiento/CLASE.md).

### Estado estándar

- Un estado estándar es una condición de referencia definida (aquí, 1 bar y 298,15 K).

💡 **Cómo se explica en la clase [B06-C12](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md):**
- E["Elementos en estado estándar (H = 0)"] -->|"formar CH4: −74,87"| R["Reactivos: CH4 + 2 O2"]
- Límites: 298 K, estado estándar, incertidumbres independientes; no calcula temperaturas de llama, rendimiento ni velocidad.
- 🎯 **Por qué importa:** Cualquier combustible, de una hoguera a un cohete, libera energía porque los productos están en un estado más estable que los reactivos. ¿Cuánta energía por kilogramo?
- 🔗 **Se estudia junto con:** entalpía, entalpía de reacción, negativa, positiva.

📘 **Dónde se aprende** (1 clase): [B06-C12 · Termoquímica y energía de reacción](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md).

### Estado fundamental

- El estado fundamental es el de menor energía (`n = 1`).

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- La energía de ionización del hidrógeno en su estado fundamental es entonces 13,606 eV (S1); el valor medido que publica la NIST es 13,5984 eV (S2), 0,05 % menor por la misma corrección de masa del núcleo que verás en 8.3.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.
- 🔗 **Se estudia junto con:** átomo, núcleo, protones, neutrones.

📘 **Dónde se aprende** (1 clase): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md).

### Estado nominal

- El estado nominal es `(q̂, b̂)`.

💡 **Contexto en la clase [B87-C10](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR G["giroscopio w_m"] --> P["propagar q y P"] P --> U["actualizar con Sol y campo"] V["vectores b_m, r"] --> U U --> R["reiniciar: q, sesgo"] R --> P ``` *Descripción textual:* el giroscopio propaga la actitud y la covarianza; cada segundo, las medidas de vector corrigen la actitud y el sesgo y se reinicia el error.
- 🎯 **Por qué importa:** Un giroscopio sin corregir se desvía decenas de grados en minutos; un vector solo da `~1°` por época. La decisión central: ¿cómo se combinan para obtener una actitud mejor que cada uno, y cómo se sabe que el filtro es honesto?
- 🔗 **Se estudia junto con:** estado de error, propagación, actualización, reinicio.

📘 **Dónde se aprende** (1 clase): [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md).

### Estado oculto

- El estado oculto es el conjunto de variables que existen en el kernel y que no se ven en el texto del cuaderno: pueden haber sido creadas por celdas borradas o ejecutadas en otro orden.

💡 **Cómo se explica en la clase [B14-C09](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md):**
- Esto muestra el estado oculto: el generador conserva su posición entre ejecuciones.
- A["Archivo .ipynb<br/>celdas y salidas guardadas"] -->|"abrir y ejecutar celdas<br/>en cualquier orden"| K["Kernel con estado oculto"]
- 🎯 **Por qué importa:** Alguien te manda un cuaderno con un gráfico que apoya una conclusión. Lo abres, ejecutas las celdas y el gráfico sale distinto.
- 🔗 **Se estudia junto con:** cuaderno, kernel, Reiniciar y ejecutar todo, semilla.

📘 **Dónde se aprende** (1 clase): [B14-C09 · Jupyter y experimentos reproducibles](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md).

### Estado parte

- Un Estado parte ha ratificado el tratado.

💡 **Contexto en la clase [B119-C01](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md):**
- 🎯 **Por qué importa:** Casi todo el derecho espacial posterior (salvamento, responsabilidad, registro, Luna) desarrolla principios de este tratado, y ninguna otra clase del programa lo estudia como instrumento jurídico. La decisión central: ¿qué obligación del tratado se infringe en una misión dada y qué cambio mínimo la devuelve a la conformidad?
- 🔗 **Se estudia junto con:** autorización y supervisión continua, Jurisdicción y control, Apropiación nacional, regla comprobable.

📘 **Dónde se aprende** (1 clase): [B119-C01 · Tratado del Espacio Ultraterrestre](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md).

### Estado/modo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B96-C08](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md):**
- 🎯 **Por qué importa:** Un comando válido en un estado puede ser peligroso en otro; y un modo seguro al que no se puede volver es una trampa. La decisión central: ¿qué transiciones existen y se puede siempre llegar al estado seguro?
- 🔗 **Se estudia junto con:** Transición, Alcanzabilidad, Sumidero, Propiedad de seguridad.

📘 **Dónde se aprende** (1 clase): [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md).

### Estados

- La materia puede estar en distintos estados, que se distinguen por la libertad de movimiento de sus partículas.

💡 **Cómo se explica en la clase [B06-C10](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md):**
- En el universo observable, la materia ordinaria que brilla, como las estrellas y el gas entre ellas, está en gran parte en estado de plasma (se estudia en B30).
- La energía para ionizar el hidrógeno desde su estado fundamental es 13,598 eV (S6).
- 🎯 **Por qué importa:** En Marte, la temperatura media es 214 K y la presión media en superficie 6,36 mb (S1). Ese valor está casi en el punto triple del agua, la presión mínima a la que puede existir agua líquida (S2).
- 🔗 **Se estudia junto con:** materia, sólido, líquido, gas.

📘 **Dónde se aprende** (1 clase): [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md).

### Estallido tipo III

- Un estallido tipo III es el producido por un haz de electrones rápidos.

💡 **Cómo se explica en la clase [B30-C21](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md):**
- Un estudio describe las clases de estallidos solares de tipo I a V (S3, solo resumen).
- 🎯 **Por qué importa:** Una frecuencia es una altura, y la deriva en frecuencia da la velocidad del haz. La decisión central: ¿cómo se convierte un espectro dinámico en la velocidad de los electrones?
- 🔗 **Se estudia junto con:** espectro dinámico, deriva en frecuencia, emisión fundamental, armónico.

📘 **Dónde se aprende** (1 clase): [B30-C21 · Radioemisión solar: estallidos de radio y su observación](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md).

### Estándar

- El estándar es una fuente de flujo conocido.
- Un estándar tiene magnitud conocida.

💡 **Cómo se explica en la clase [B45-C09](../programa/clases/B45/B45-C09-calibracion-de-respuesta-instrumental/CLASE.md):**
- E["estándar conocido"] --> S["S = cuentas/flujo"]
- *Descripción textual:* el estándar da la sensibilidad, que se suaviza y se divide en el blanco, con el ruido propagado de ambos.
- ⚠️ **Error frecuente:** Ignorar el ruido del estándar. Se corrige con 8.1.
- 🎯 **Por qué importa:** Sin respuesta, un espectro en cuentas no es un espectro físico. La decisión central: ¿cómo se pasa de cuentas a flujo y con qué incertidumbre?
- 🔗 **Se estudia junto con:** respuesta, sensibilidad, campo plano, propagación de errores.

📘 **Dónde se aprende** (2 clases): [B45-C09 · Calibración de respuesta instrumental](../programa/clases/B45/B45-C09-calibracion-de-respuesta-instrumental/CLASE.md); [B45-C21 · Estándares fotométricos y sistemas de referencia](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md).

### Estandarización

- La estandarización resta a cada columna su media y divide por su desviación estándar (`z = (x − μ)/σ`), de modo que queda con media 0 y desviación 1.

💡 **Cómo se explica en la clase [B17-C01](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md):**
- La estandarización lo resuelve: al dividir cada columna por su desviación estándar, las unidades se cancelan y todas las columnas pesan igual.
- La física aportó más que la sola estandarización.
- 🎯 **Por qué importa:** Un modelo de aprendizaje automático no sabe física: solo ve números. Si le das la duración de un tránsito en segundos y el periodo en días, la columna con números más grandes domina cualquier cálculo de distancias, y la clasificación depende de una elección de unidades que nada tiene que ver con el cielo.
- 🔗 **Se estudia junto con:** característica, variable objetivo, adimensional, modelo basado en distancias.

📘 **Dónde se aprende** (1 clase): [B17-C01 · Ingeniería de características científicas](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md).

### Estandarizar

- El teorema central del límite afirma que, para variables independientes con varianza finita, la distribución de su suma (o promedio) se aproxima a una normal cuando el número de términos crece; el GUM lo enuncia así: la distribución de una combinación lineal de variables independientes es aproximadamente normal aunque las variables no lo sean (S1, G.2). Estandarizar el promedio `X̄` significa formar `Z = (X̄ − μ)/(σ/√n)`, que se acerca a una normal estándar.

💡 **Cómo se explica en la clase [B12-C06](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md):**
- Paso 2 · Estandarizar. `0,1/0,0527 = 1,897` desviaciones.
- Estandarizar un promedio y calcular probabilidades con la normal.
- 🎯 **Por qué importa:** Ningún instrumento tiene ruido exactamente normal, y sin embargo casi todas las incertidumbres se expresan con campanas. La razón es que se reportan promedios y sumas de muchas contribuciones pequeñas.
- 🔗 **Se estudia junto con:** teorema central del límite, distancia de Kolmogorov–Smirnov, asimetría, colas pesadas.

📘 **Dónde se aprende** (1 clase): [B12-C06 · Teorema central del límite](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md).

### Este

- La elongación es el ángulo en el cielo entre un planeta y el Sol; es este si el planeta sale después que el Sol y se ve en el cielo vespertino, y oeste si sale antes y se ve en el cielo matutino.

💡 **Cómo se explica en la clase [B08-C10](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md):**
- Mercurio estaba a 22,7° al este del Sol (S5), casi su máximo del modelo circular (22,8°).
- Con la efeméride integrada en astropy (S5) obtienes, para esa noche, la elongación de cada planeta y su altura en los crepúsculos astronómicos: Saturno estaba a 132,75° al este del Sol y a 61,6° de altura al anochecer;
- 🎯 **Por qué importa:** Los planetas parecen «estrellas errantes» y un titular promete «alineación de planetas». La pregunta motivadora: ¿qué planetas puedo ver esta noche, dónde y a qué hora?
- 🔗 **Se estudia junto con:** elongación, oeste, planeta interior, exterior.

📘 **Dónde se aprende** (1 clase): [B08-C10 · Planetas observables y elongación](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md).

### Estela

- La estela es la longitud en píxeles que recorre una estrella durante una exposición sin seguimiento: `Ω cos δ · t / escala`, con `Ω = 15,041″/s` (S2).

💡 **Cómo se explica en la clase [B08-C19](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md):**
- Con 50 mm (17,74″/px) se desplaza `0,85 px/s`: en 1,18 s la estela es de 1 píxel (`t = escala/Ω`).
- Con 24 mm, 1 píxel de estela tarda 2,5 s en el ecuador; con 200 mm, 0,3 s; con el telescopio de 1000 mm, 0,07 s.
- 🎯 **Por qué importa:** Un teléfono o una cámara réflex puede captar la Vía Láctea o la Luna con detalle, pero una exposición demasiado larga convierte las estrellas en rayas. La pregunta motivadora: ¿cuánto puedo exponer y con qué focal para obtener estrellas puntuales, y qué debo anotar para que la foto sirva como dato?
- 🔗 **Se estudia junto con:** distancia focal, tamaño del píxel, escala de placa, campo.

📘 **Dónde se aprende** (1 clase): [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md).

### Estema

- Un estema es el árbol de copias entre testimonios.

💡 **Contexto en la clase [B132-C01](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md):**
- 🎯 **Por qué importa:** Un relato histórico es tan fiable como las fuentes que lo sostienen, y tres copias de una misma fuente no son tres fuentes. La decisión central: ¿cuánto apoyo da realmente un conjunto de fuentes a una afirmación y cuánto de ese apoyo es robusto ante cambios razonables de criterio?
- 🔗 **Se estudia junto con:** crítica de fuentes, fuente primaria, secundaria, terciaria.

📘 **Dónde se aprende** (1 clase): [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Estencil de cinco puntos

- El estencil de cinco puntos aproxima el laplaciano con el nodo y sus cuatro vecinos.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- Plantear la ecuación de Poisson con condiciones de frontera de Dirichlet y discretizarla con el estencil de cinco puntos.
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;
- 🔗 **Se estudia junto con:** ecuación de Poisson, elíptico, de Dirichlet, método iterativo.

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Estequiometría

- La estequiometría estudia las proporciones en que se combinan las sustancias.
- La estequiometría relaciona masas de reactivos y productos.

💡 **Cómo se explica en la clase [B06-C07](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md):**
- python programa/clases/B06/B06-C07-estequiometria-elemental/composicion_atmosferas.py
- 🎯 **Por qué importa:** Si quieres saber cuánto pesa una columna de atmósfera de Marte, necesitas su masa molar media, y para eso, su composición. La NASA publica la composición en volumen de las atmósferas de Marte, Venus y la Tierra y también un «peso molecular» medio (S1, S2, S3).
- 🔗 **Se estudia junto con:** fórmula molecular, fórmula empírica, composición porcentual, fracción molar.

📘 **Dónde se aprende** (2 clases): [B06-C07 · Estequiometría elemental](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md); [B119-C23 · Protección ambiental de las actividades de lanzamiento](../programa/clases/B119/B119-C23-proteccion-ambiental-de-las-actividades-de-lanzamiento/CLASE.md).

### Estequiométrica

- La mezcla estequiométrica consume ambos por completo.

💡 **Cómo se explica en la clase [B78-C05](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md):**
- Con el modelo ilustrativo H₂/O₂, la relación estequiométrica en masa es `7,936`.
- Calcular la relación estequiométrica `O/F` de H₂/O₂.
- 🎯 **Por qué importa:** Un motor puede quemar mezclas con exceso de combustible o de oxidante. La decisión central: ¿qué `O/F` maximiza el escape en un modelo sin disociación y por qué los motores reales operan en otro punto?
- 🔗 **Se estudia junto con:** bipropelente, relación O/F, rica, pobre.

📘 **Dónde se aprende** (1 clase): [B78-C05 · Propulsión bipropelente conceptual](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md).

### Estiba

- La estiba es la colocación de lo transportado.

💡 **Cómo se explica en la clase [B104-C21](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md):**
- Consumo normal sin tendencias, un solo consumible, sin falla del reabastecimiento, sin masa ni centro de gravedad en la estiba y sin accesibilidad.
- En la estiba, 60 objetos de 1,063 m³ en total caben en 22 bolsas de 0,05 m³ (cota inferior 22; llenado de 96,6 %).
- 🎯 **Por qué importa:** Quedarse sin un consumible a bordo no se arregla enviando a alguien a comprarlo. La decisión central: ¿con qué punto de reorden se pide para que el faltante sea raro, y cuánto volumen cuesta guardar lo pedido?
- 🔗 **Se estudia junto con:** punto de reorden, existencias de seguridad, plazo de entrega, empaquetado en bolsas.

📘 **Dónde se aprende** (1 clase): [B104-C21 · Inventario, logística y estiba a bordo](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md).

### Estimación

- Una estimación (o estimación de Fermi) es un cálculo con números redondos para obtener el orden de magnitud.
- Una estadística es una función de los datos de la muestra; una estimación es la operación de asignar valores numéricos a los parámetros a partir de una muestra, un estimador es la estadística usada para ello y una estimación (resultado) es su valor para una muestra concreta (S1, C.2.23–C.2.26).
- La estimación es el promedio ponderado `Σ w_i x_i`.

💡 **Cómo se explica en la clase [B03-C11](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md):**
- El valor exacto es 499,005 s: la estimación acierta al 0,2 %.
- Primero se estima con una cifra; luego se calcula sin redondear; se compara con la estimación; se redondea al final según la calidad de los datos; y se reporta con unidad, cifras y cota.
- 🎯 **Por qué importa:** Si te piden el tiempo que tarda la luz del Sol en llegar a la Tierra y respondes «499,004783836 s», parece muy preciso, pero tus datos (1 au y `c`) son exactos; en cambio, si respondes lo mismo para la distancia a la Luna, que varía entre unos 357 000 y 407 000 km, esas cifras serían falsas.
- 🔗 **Se estudia junto con:** cifra significativa, Redondear, cota, error de redondeo.

📘 **Dónde se aprende** (3 clases): [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md); [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md).

### Estimación virial

- La estimación virial da la temperatura típica `T ~ GMμu/(kR)`.

💡 **Cómo se explica en la clase [B30-C01](../programa/clases/B30/B30-C01-estructura-interna-del-sol/CLASE.md):**
- temperatura central (politropo, mu = 0.6) = 1.1760e+07 K ; estimacion virial G M mu u/(k R) = 1.3766e+07 K ; cociente = 0.854
- 🎯 **Por qué importa:** Un Sol que pudiera colapsar en media hora, que tardara miles de años en dejar salir su luz y cuya energía no pudiera venir de la gravedad obliga a entender qué sostiene a una estrella. Sin un modelo mínimo de estructura, la actividad de las demás clases queda sin base.
- 🔗 **Se estudia junto con:** politropo, ecuación de Lane–Emden, tiempo de caída libre, difusión de fotones.

📘 **Dónde se aprende** (1 clase): [B30-C01 · Estructura interna del Sol](../programa/clases/B30/B30-C01-estructura-interna-del-sol/CLASE.md).

### Estimado

- observado, el medido; estimado, el calculado a partir de otros con supuestos;

💡 **Cómo se explica en la clase [B01-C20](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md):**
- De la bitácora salen los datos observados; lo que calcules a partir de ellos es estimado.
- 🎯 **Por qué importa:** Entender el método no es lo mismo que aplicarlo. Cuando mides de verdad, aparecen problemas que los ejercicios no tienen: el cielo se nubla, el palo no está del todo vertical, la regla se mueve, los datos no coinciden con lo que predijiste.
- 🔗 **Se estudia junto con:** protocolo, bitácora, incidencia, criterio de rechazo de datos.

📘 **Dónde se aprende** (1 clase): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md).

### Estimador

- Un estimador del valor esperado a partir de `n` observaciones independientes en las mismas condiciones es la media aritmética (S1, 4.2.1); la desviación típica experimental estima `σ` con denominador `n − 1` (S1, 4.2.2).
- Una estadística es una función de los datos de la muestra; una estimación es la operación de asignar valores numéricos a los parámetros a partir de una muestra, un estimador es la estadística usada para ello y una estimación (resultado) es su valor para una muestra concreta (S1, C.2.23–C.2.26).
- Un estimador `θ̂(datos)` es una función de los datos.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C07](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md):**
- La cota de Cramér–Rao —que fija la menor varianza posible de un estimador insesgado— coincide con `λ/n` para este modelo: la media es el mejor estimador insesgado posible.
- Esa es la forma de comprobar un estimador: simular muchas muestras de un modelo conocido y ver si el estimador acierta en promedio y con la dispersión esperada.
- ⚠️ **Error frecuente:** Creer que un estimador insesgado siempre es mejor. Se corrige con 8.6 y el ejercicio 11.
- 🎯 **Por qué importa:** Una misión no «conoce» la tasa de impactos ni el ruido de su sensor: los estima a partir de unas decenas de datos. Un estimador mal elegido, o mal interpretado, da parámetros sesgados o con una confianza injustificada.
- 🔗 **Se estudia junto con:** estadística, estimación, estimación, verosimilitud.

📘 **Dónde se aprende** (7 clases): [B12-C04 · Esperanza y varianza](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md); [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md); [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md); [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md); [B36-C04 · Espectro de potencia de materia](../programa/clases/B36/B36-C04-espectro-de-potencia-de-materia/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md) y 1 más.

### Estimador de Hill

- El estimador de Hill es `b̂ = n/Σ ln(D/D_min)`.

💡 **Cómo se explica en la clase [B53-C08](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md):**
- El script [crateres.py](crateres.py) genera 2000 catálogos sintéticos de 500 cráteres y compara los dos estimadores (comprueba sesgo de Hill < 2 errores típicos y dispersión dentro de 5 % de `b/√n`).
- 🎯 **Por qué importa:** Un conteo no es un número, es una distribución con incertidumbre. La decisión central: ¿qué estimador de la pendiente es fiable y a partir de qué diámetro el catálogo es completo?
- 🔗 **Se estudia junto con:** distribución acumulada, pendiente, completitud.

📘 **Dónde se aprende** (1 clase): [B53-C08 · Cartografía de cráteres](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md).

### Estimador de Kaplan–Meier

- El estimador de Kaplan–Meier estima la curva de permanencia con datos censurados.

💡 **Contexto en la clase [B129-C06](../programa/clases/B129/B129-C06-motivacion-y-permanencia-de-participantes/CLASE.md):**
- 🎯 **Por qué importa:** Los equipos de un proyecto quieren retener voluntarios y a menudo añaden insignias, rachas o clasificaciones sin medir si sirven. La decisión central: ¿cómo medir la permanencia y cuándo se puede decir que algo la mejoró?
- 🔗 **Se estudia junto con:** permanencia, riesgo, razón de riesgos, índice de Gini.

📘 **Dónde se aprende** (1 clase): [B129-C06 · Motivación y permanencia de participantes](../programa/clases/B129/B129-C06-motivacion-y-permanencia-de-participantes/CLASE.md).

### Estimador de máxima verosimilitud

- El estimador de máxima verosimilitud (MLE) `θ̂` es el valor que maximiza `L`.
- La verosimilitud `L(θ)` es la probabilidad de los datos observados en función de `θ`; el estimador de máxima verosimilitud (MLE) es el valor que la maximiza; para muestras grandes sus propiedades son buenas, y con muestras pequeñas puede estar muy sesgado (S1).
- El estimador de máxima verosimilitud `α̂ = 1 + n/Σln(F/F_min)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C07](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md):**
- Dar el error típico de un estimador de máxima verosimilitud y compararlo con la cota de Cramér–Rao en un caso.
- 🎯 **Por qué importa:** Una misión no «conoce» la tasa de impactos ni el ruido de su sensor: los estima a partir de unas decenas de datos. Un estimador mal elegido, o mal interpretado, da parámetros sesgados o con una confianza injustificada.
- 🔗 **Se estudia junto con:** estadística, estimación, estimador, estimación.

📘 **Dónde se aprende** (4 clases): [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md); [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md); [B30-C12 · Erupciones y fulguraciones solares](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md); [B52-C13 · Pequeños cuerpos remanentes](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md).

### Estimador de una probabilidad

- El estimador de una probabilidad es la frecuencia `p̂ = (aciertos)/N`; su error típico es `√(p(1−p)/N)`.

💡 **Contexto en la clase [B12-C14](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md):**
- **Idea central (modelo mental):** Si lanzas dardos al azar sobre una diana de área conocida y cuentas la fracción que cae en una zona, estimas el área de la zona. Cuantos más dardos, mejor, pero con rendimiento decreciente: para dividir el error por 10 hay que lanzar 100 veces más.
- 🎯 **Por qué importa:** Casi ningún modelo de misión admite una fórmula cerrada para la incertidumbre de su salida: hay no linealidades, restricciones y combinaciones de entradas. La simulación Monte Carlo reemplaza el álgebra por repetición: se sortean entradas, se evalúa el modelo y se resume la salida.
- 🔗 **Se estudia junto con:** simulación Monte Carlo, generador pseudoaleatorio, semilla, error de Monte Carlo.

📘 **Dónde se aprende** (1 clase): [B12-C14 · Simulación Monte Carlo](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md).

### Estimador de Wolf

- El estimador de Wolf es `M₁/₂ = 3σ²_los r₁/₂/G ≈ 4σ²_los R_e/G` (S2).

💡 **Cómo se explica en la clase [B25-C10](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md):**
- Estimador de Wolf (esta clase): sencillo y casi independiente de la anisotropía, según S2.
- Calcular la masa dentro del radio de media luz con el estimador de Wolf.
- 🎯 **Por qué importa:** Las galaxias enanas son las más abundantes y las más ricas en materia oscura según su masa dinámica; además son los sitios donde las predicciones del modelo cosmológico se ponen a prueba. Pero con pocas estrellas medidas y sin rotación ordenada, su masa depende de un estimador.
- 🔗 **Se estudia junto con:** galaxia irregular, galaxia enana, enanas esferoidales, ultratenues.

📘 **Dónde se aprende** (1 clase): [B25-C10 · Galaxias irregulares y enanas](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md).

### Estimador estratificado

- El estimador estratificado es `p = Σ W_h p_h`, con `p_h` medido en la muestra de referencia.

💡 **Cómo se explica en la clase [B57-C33](../programa/clases/B57/B57-C33-deforestacion-y-cambio-de-uso-del-suelo/CLASE.md):**
- Con una muestra de 350 celdas, el estimador estratificado da `5,412 % ± 2,222` (IC 95 %), o `7,793 km²`.
- Por estimador estratificado: insesgado con referencia.
- 🎯 **Por qué importa:** Las cifras de deforestación orientan políticas y compromisos. La decisión central: ¿cómo estimo el área de cambio con su intervalo, sin fiarme del conteo directo de un mapa imperfecto?
- 🔗 **Se estudia junto con:** estrato, peso, varianza, cobertura.

📘 **Dónde se aprende** (1 clase): [B57-C33 · Deforestación y cambio de uso del suelo](../programa/clases/B57/B57-C33-deforestacion-y-cambio-de-uso-del-suelo/CLASE.md).

### Estimador natural

- El estimador natural es `ξ = DD/RR − 1`, con `DD` los pares de datos y `RR` los esperados al azar.
- El estimador natural `DD/RR − 1`.

💡 **Cómo se explica en la clase [B36-C03](../programa/clases/B36/B36-C03-funciones-de-correlacion-de-galaxias/CLASE.md):**
- Calcular el estimador natural y el de Landy–Szalay.
- El script [correlacion.py](correlacion.py) genera 8 maquetas, estima ξ con el estimador natural y Landy–Szalay y las compara con la forma analítica (comprueba que los `pull` son menores que 3,5 y que la integral queda dentro del 10 %).
- 🎯 **Por qué importa:** Medir la agrupación exige un estimador sin sesgo y con error conocido. La decisión central: ¿concuerda el estimador con la verdad analítica dentro de su error?
- 🔗 **Se estudia junto con:** Landy–Szalay, proceso de Thomas, caja periódica, catálogo aleatorio.

📘 **Dónde se aprende** (2 clases): [B25-C18 · Estructura cósmica a gran escala](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md); [B36-C03 · Funciones de correlación de galaxias](../programa/clases/B36/B36-C03-funciones-de-correlacion-de-galaxias/CLASE.md).

### Estimador por mínimos cuadrados

- El estimador por mínimos cuadrados resuelve `N s ≈ I` con las celdas iluminadas, y se normaliza.

💡 **Contexto en la clase [B87-C03](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md):**
- 🎯 **Por qué importa:** Un satélite que sale de un eclipse o de un modo seguro necesita saber hacia dónde está el Sol para orientar sus paneles. La decisión central: ¿con qué precisión angular se obtiene el vector solar de las corrientes de las fotoceldas y cuánto ruido tolera el diseño?
- 🔗 **Se estudia junto con:** ley del coseno, vector solar, campo de visión, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B87-C03 · Sensores solares](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md).

### Estiramiento

- Astropy llama a esa operación «normalización» y la separa del estiramiento (*stretch*), que es la función `f` aplicada después sobre [0, 1] (S1, que subraya su finalidad de visualización).
- El estiramiento `s` ensancha o estrecha.

💡 **Cómo se explica en la clase [B15-C10](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md):**
- Una figura publicada debe indicar los límites, el estiramiento y su parámetro (por ejemplo, «percentiles 1–99,5, asinh con `b = 0,02`»).
- El estiramiento hace eso con los brillos.
- ⚠️ **Error frecuente:** No declarar límites ni estiramiento. Sección 8.7.
- 🎯 **Por qué importa:** Tienes una imagen con un cielo de 50 ADU, una estructura difusa tenue 15 ADU por encima y una estrella de 9000 ADU. Si la muestras con una escala lineal entre mínimo y máximo, el cielo y la estructura quedan en los niveles de gris 1 y 2 de 255: parece una pantalla negra con un punto.
- 🔗 **Se estudia junto con:** histograma, normalización, intervalo, límite.

📘 **Dónde se aprende** (2 clases): [B15-C10 · Histogramas y normalización](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md).

### Estocasticidad

- La estocasticidad es la parte de `δ_g` no explicada por `δ_m`.

💡 **Contexto en la clase [B36-C08](../programa/clases/B36/B36-C08-sesgo-de-galaxias-y-trazadores-de-la-materia/CLASE.md):**
- **Idea central (modelo mental):** Es como mirar solo las cumbres de un paisaje: se ven más contrastadas que el terreno medio, y eso hay que corregir al medir la altura del terreno.
- 🎯 **Por qué importa:** Si se ignora el sesgo, la amplitud de la materia se sobreestima. La decisión central: ¿qué sesgo corresponde a un trazador y cómo se mide?
- 🔗 **Se estudia junto con:** sesgo lineal, espectro cruzado, teorema de Bussgang, separación pico–fondo.

📘 **Dónde se aprende** (1 clase): [B36-C08 · Sesgo de galaxias y trazadores de la materia](../programa/clases/B36/B36-C08-sesgo-de-galaxias-y-trazadores-de-la-materia/CLASE.md).

### Estrangulamiento

- El estrangulamiento es la expansión sin trabajo ni calor (`h₁ = h₂`).
- El estrangulamiento reduce el empuje.

💡 **Cómo se explica en la clase [B77-C10](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md):**
- El límite axial no cambia la presión dinámica máxima, porque el estrangulamiento solo actúa al final.
- Cuantificar el costo en velocidad y tiempo del estrangulamiento.
- 🎯 **Por qué importa:** El mayor empuje reduce las pérdidas pero carga la estructura, sobre todo al final del quemado, cuando la masa es menor. La decisión central: ¿qué límite de carga impone la estructura y cuánta velocidad cuesta respetarlo?
- 🔗 **Se estudia junto con:** aceleración axial, carga lateral, factor de seguridad, carga límite.

📘 **Dónde se aprende** (2 clases): [B77-C10 · Restricciones de cargas estructurales](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md); [B79-C10 · Primera ley de la termodinámica en sistemas abiertos](../programa/clases/B79/B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md).

### Estrategia

- La estrategia es la combinación de coberturas contratadas.

💡 **Cómo se explica en la clase [B127-C08](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md):**
- *Descripción textual:* el mismo conjunto de eventos aleatorios se aplica a cuatro estrategias que añaden coberturas de a una; para cada una se simula el costo del operador y se resumen su media, su desviación, su cuantil 99 % y la probabilidad de superar `60 MUSD`.
- Comparar estrategias por costo medio, desviación, cuantil 99 % y probabilidad de superar un umbral.
- ⚠️ **Error frecuente:** Tomar la estrategia «ganadora» del modelo como recomendación. Se corrige con 8.5 y la sección 21.
- 🎯 **Por qué importa:** Integrar los seguros de una misión en un caso permite practicar la decisión; no existía tal caso. La decisión central: ¿cuánto se paga de más por reducir el riesgo y qué riesgo se está dispuesto a retener?
- 🔗 **Se estudia junto con:** costo del operador, pérdida retenida, riesgo retenido, autoseguro.

📘 **Dónde se aprende** (1 clase): [B127-C08 · Simulación de cobertura de seguros para una misión](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md).

### Estratificación

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B34-C03](../programa/clases/B34/B34-C03-bucles-magneticos-coronales/CLASE.md):**
- **Idea central (modelo mental):** Como una pelota que sube por un tobogán semicircular: la gravedad que siente a lo largo del camino cambia con el ángulo.
- 🎯 **Por qué importa:** La densidad en el ápice limita la luz que se ve. La decisión central: ¿cuánto cae la presión de la base al ápice y cómo cambia el campo con la sección?
- 🔗 **Se estudia junto con:** altura de escala, gravedad efectiva, tubo de flujo, conservación del flujo.

📘 **Dónde se aprende** (1 clase): [B34-C03 · Bucles magnéticos coronales](../programa/clases/B34/B34-C03-bucles-magneticos-coronales/CLASE.md).

### Estratificado

- Un pliegue estratificado conserva en cada parte la proporción de clases.

💡 **Cómo se explica en la clase [B17-C02](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md):**
- Los pliegues estratificados reparten cada clase proporcionalmente (S2).
- Paso 2 · pliegues estratificados. Cada pliegue tiene 4000 ejemplos, la mitad de cada clase.
- 🎯 **Por qué importa:** Un modelo que clasifica señales como «candidata» o «no candidata» puede acertar el 100 % de los ejemplos con los que se entrenó y fallar la cuarta parte de los nuevos: memorizó. Lo que importa a un equipo científico es el desempeño en datos que el modelo no vio.
- 🔗 **Se estudia junto con:** aprendizaje supervisado, etiquetas, clasificación, regresión.

📘 **Dónde se aprende** (1 clase): [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md).

### Estratigrafía invertida

- La estratigrafía invertida es el orden volcado de las capas en el borde.

💡 **Contexto en la clase [B61-C04](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md):**
- **Idea central (modelo mental):** Un esquema del flujo de cálculo de la clase; el texto equivalente está debajo.
- 🎯 **Por qué importa:** El manto de ejecta es un marcador estratigráfico: cubre lo anterior y es cubierto por lo posterior. La decisión central: ¿cómo decae el espesor con la distancia y cuánto volumen contiene el manto?
- 🔗 **Se estudia junto con:** manto de ejecta, ejecta distal, espesor en el borde, ley de −3.

📘 **Dónde se aprende** (1 clase): [B61-C04 · Mantos de ejecta y depósitos de impacto](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md).

### Estrato

- Un estrato es una clase del mapa.

💡 **Cómo se explica en la clase [B57-C33](../programa/clases/B57/B57-C33-deforestacion-y-cambio-de-uso-del-suelo/CLASE.md):**
- Los pesos de los estratos (pérdida, bosque estable, no bosque) son `0,0320; 0,7680; 0,2000`.
- Repetido 1000 veces, el estimador tiene sesgo `-0,0285` puntos y desviación `0,788` puntos; el intervalo cubre la verdad en `88,9%` de las repeticiones, algo por debajo del 95 % nominal: en estratos donde la proporción es pequeña la aproximación normal del intervalo es optimista.
- 🎯 **Por qué importa:** Las cifras de deforestación orientan políticas y compromisos. La decisión central: ¿cómo estimo el área de cambio con su intervalo, sin fiarme del conteo directo de un mapa imperfecto?
- 🔗 **Se estudia junto con:** peso, estimador estratificado, varianza, cobertura.

📘 **Dónde se aprende** (1 clase): [B57-C33 · Deforestación y cambio de uso del suelo](../programa/clases/B57/B57-C33-deforestacion-y-cambio-de-uso-del-suelo/CLASE.md).

### Estrella

- Una estrella es una bola de gas caliente, en su mayor parte hidrógeno y helio, cuya energía viene de la fusión nuclear en su núcleo, que compensa su propia gravedad (S2).
- La malla completa tiene `n(n−1)/2` enlaces; el anillo, `n`; la estrella, `n − 1`.

💡 **Cómo se explica en la clase [B01-C03](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md):**
- El primer criterio, orbitar el Sol, separa los objetos de nuestro sistema solar de los de otras estrellas.
- Además, la B5 dice «en nuestro sistema solar»: no define qué es un planeta alrededor de otras estrellas.
- ⚠️ **Error frecuente:** Pensar que la IAU define cualquier planeta. Se aplica la B5 a otras estrellas.
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».
- 🔗 **Se estudia junto con:** planeta, planeta enano, cuerpo menor del sistema solar, satélite.

📘 **Dónde se aprende** (2 clases): [B01-C03 · Objetos celestes y sus diferencias](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md); [B88-C31 · Topologías de red de datos a bordo](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md).

### Estrella con helio en el núcleo

- La estrella con helio en el núcleo quema helio (C08).

💡 **Cómo se explica en la clase [B24-C16](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md):**
- Los modos de gravedad mixtos de las gigantes tienen espaciados de periodo de ~`50 s` si la estrella solo quema hidrógeno en capa y de `100–300 s` si quema helio en el núcleo (S2, resumen).
- *Descripción textual:* al agotarse el hidrógeno del núcleo, este se contrae y la fusión se desplaza a una capa; la luminosidad sube, la envoltura se hincha y la estrella se vuelve una gigante, mientras el núcleo de helio crece con la masa que la capa va convirtiendo.
- 🎯 **Por qué importa:** Una gigante roja es mucho mayor y más luminosa que su estrella original y tiene una densidad media ínfima. Entender su tamaño, su gravedad y cómo crece su núcleo permite interpretar las gigantes observadas, usarlas como sondas asterosísmicas y anticipar el destino del Sol.
- 🔗 **Se estudia junto con:** gigante roja, núcleo inerte de helio, quemado en capa, rama de las gigantes rojas.

📘 **Dónde se aprende** (1 clase): [B24-C16 · Gigantes rojas](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md).

### Estrella de carbono

- Una estrella de carbono es una estrella con `C/O > 1` en la superficie.

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- Una estrella de masa baja o media que ha agotado el helio del núcleo (C16, C08) tiene un núcleo de carbono y oxígeno.
- Una envoltura con `C/O > 1` corresponde a una estrella de carbono.
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.
- 🔗 **Se estudia junto con:** rama asintótica de gigantes (AGB), pulso térmico, dragado, proceso s.

📘 **Dónde se aprende** (1 clase): [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### Estrella de comparación

- Una estrella de comparación debe ser constante.

💡 **Cómo se explica en la clase [B45-C17](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md):**
- ⚠️ **Error frecuente:** Usar como comparación una estrella variable. Se corrige con la pregunta de transferencia.
- 🎯 **Por qué importa:** La atmósfera varía más que la señal; sin una referencia, la curva de luz no sirve. La decisión central: ¿qué comparaciones y qué precisión se necesitan para una profundidad dada?
- 🔗 **Se estudia junto con:** curva diferencial, transparencia, conjunto, ruido de fotones.

📘 **Dónde se aprende** (1 clase): [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md).

### Estrella de neutrones

- Una estrella de neutrones es un remanente más compacto, de unos 10 km, sostenido por neutrones.
- Una estrella de neutrones es aún más compacta (B27).
- La estrella de neutrones es el remanente.

💡 **Cómo se explica en la clase [B24-C18](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md):**
- Formar una estrella de neutrones de `1,4 M☉` y `10 km` (valores ilustrativos) libera una energía gravitatoria del orden de `3,1 × 10⁴⁶ J` (esfera uniforme), el `12,4 %` de `Mc²`.
- B -- "> M_Ch" --> D["Colapso: estrella de<br/>neutrones o agujero negro"]
- ⚠️ **Error frecuente:** Confundir enana blanca con estrella de neutrones. Se corrige con la tabla de la sección 12.
- 🎯 **Por qué importa:** El destino de una estrella es una enana blanca, una estrella de neutrones o un agujero negro; hay una masa límite que separa los dos primeros destinos. Calcularla muestra cómo la mecánica cuántica (presión de degeneración) sostiene a una estrella cuando ya no hay fusión.
- 🔗 **Se estudia junto con:** enana blanca, agujero negro, presión de degeneración, masa de Chandrasekhar.

📖 **Explicado a fondo:** [Estrella de neutrones y púlsar](esencial/esencial-d-l.md#estrella-de-neutrones-y-púlsar) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md); [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md); [B27-C15 · Supernovas de colapso](../programa/clases/B27/B27-C15-supernovas-de-colapso/CLASE.md).

### Estrella de Wolf–Rayet

- Una estrella de Wolf–Rayet es una estrella masiva que ha perdido su envoltura de hidrógeno.

💡 **Contexto en la clase [B24-C17](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md):**
- **Idea central (modelo mental):** Cuanto más brilla la estrella, más empuja la luz sobre su atmósfera; si la luz casi iguala a la gravedad, el gas escapa con facilidad.
- 🎯 **Por qué importa:** La masa que una estrella conserva hasta su final decide el destino: remanente, tipo de supernova, enriquecimiento del medio. Y las estrellas masivas no la conservan: pierden masa por vientos, erupciones y transferencia a una compañera.
- 🔗 **Se estudia junto con:** viento estelar, factor de Eddington, pérdida de masa, erupciones.

📘 **Dónde se aprende** (1 clase): [B24-C17 · Estrellas masivas y pérdida de masa](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md).

### Estrella enana roja

- Una estrella enana roja es fría y pequeña; una estrella tipo solar, de unos 5 000 a 6 000 K.

💡 **Cómo se explica en la clase [B01-C14](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md):**
- Una enana roja cercana puede verse tan o más brillante que una estrella mucho más luminosa y lejana.
- 🎯 **Por qué importa:** Dos estrellas pueden verse igual de brillantes y ser totalmente distintas: una pequeña y cercana, otra enorme y lejana (C09). Para saber cómo es una estrella necesitas separar lo que ves (flujo) de lo que ella es (luminosidad, temperatura, radio) y de dónde está (distancia).
- 🔗 **Se estudia junto con:** temperatura efectiva, luminosidad, radio, constante de Stefan–Boltzmann.

📘 **Dónde se aprende** (1 clase): [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md).

### Estrella guía láser

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B42-C17](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md):**
- **Idea central (modelo mental):** Como una linterna que ilumina un cono: lo que ve el sensor es el cilindro de luz de una estrella lejana, pero solo recibe un cono desde una fuente cercana.
- 🎯 **Por qué importa:** Sin estrella guía no hay corrección en casi todo el cielo. La decisión central: ¿a qué altitud conviene crear la estrella y qué error de cono y qué elongación trae?
- 🔗 **Se estudia junto con:** efecto cono, altitud, sodio, retrodispersión Rayleigh.

📘 **Dónde se aprende** (1 clase): [B42-C17 · Estrellas guía artificiales](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md).

### Estrella tipo solar

- Una estrella enana roja es fría y pequeña; una estrella tipo solar, de unos 5 000 a 6 000 K.

💡 **Cómo se explica en la clase [B01-C14](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md):**
- Descripción larga: las estrellas están ordenadas por temperatura; las frías son mucho menos luminosas porque son más pequeñas y más frías; las de tipo solar rondan 1 `L⊙`.
- 🎯 **Por qué importa:** Dos estrellas pueden verse igual de brillantes y ser totalmente distintas: una pequeña y cercana, otra enorme y lejana (C09). Para saber cómo es una estrella necesitas separar lo que ves (flujo) de lo que ella es (luminosidad, temperatura, radio) y de dónde está (distancia).
- 🔗 **Se estudia junto con:** temperatura efectiva, luminosidad, radio, constante de Stefan–Boltzmann.

📘 **Dónde se aprende** (1 clase): [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md).

### Estrella variable pulsante

- Una estrella variable pulsante cambia de tamaño y temperatura de forma periódica.

💡 **Cómo se explica en la clase [B24-C13](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md):**
- Definir estrella variable pulsante, periodo y relación periodo–luminosidad.
- 🎯 **Por qué importa:** Las cefeidas y otras estrellas pulsantes cumplen que cuanto más largo es el periodo, mayor es la luminosidad. Medir un periodo equivale entonces a conocer la luminosidad intrínseca y, por comparación con el brillo aparente, la distancia.
- 🔗 **Se estudia junto con:** cefeida clásica, periodo, relación periodo–luminosidad, dispersión intrínseca.

📘 **Dónde se aprende** (1 clase): [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md).

### Estrella visitante

- Una estrella visitante (en chino, «huésped») es un objeto nuevo y transitorio en el cielo, generalmente una supernova o un cometa.

💡 **Cómo se explica en la clase [B02-C04](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md):**
- Los astrónomos chinos registraron en 1054 una «estrella visitante» que hoy se identifica con la supernova que produjo la nebulosa del Cangrejo.
- 🎯 **Por qué importa:** Contar la historia de la astronomía como una línea recta de Grecia a Europa deja fuera lo que otras sociedades observaron, calcularon y construyeron. La pregunta motivadora es: ¿qué sabemos con precisión de estas tradiciones, qué falta y cómo evitar contar la historia desde un solo lado?
- 🔗 **Se estudia junto con:** instrumento, gnomon, cuadrante, observatorio.

📘 **Dónde se aprende** (1 clase): [B02-C04 · Astronomía de India, China y mundo islámico](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md).

### Estrés operacional

- El estrés operacional es la carga que impone el trabajo, el entorno y las condiciones de una misión.

💡 **Cómo se explica en la clase [B113-C01](../programa/clases/B113/B113-C01-estres-operacional-y-estrategias-de-afrontamiento/CLASE.md):**
- python programa/clases/B113/B113-C01-estres-operacional-y-estrategias-de-afrontamiento/estres.py
- 🎯 **Por qué importa:** B105-C09 presenta la salud mental en aislamiento, pero no el estrés operacional. La decisión central: ¿sobre qué palanca actuar, bajar la demanda vivida o acelerar la recuperación, y cómo saber si funcionó?
- 🔗 **Se estudia junto con:** afrontamiento, valoración, recuperación, estado estacionario.

📘 **Dónde se aprende** (1 clase): [B113-C01 · Estrés operacional y estrategias de afrontamiento](../programa/clases/B113/B113-C01-estres-operacional-y-estrategias-de-afrontamiento/CLASE.md).

### Estresor agudo

- El estresor agudo `S(t) = 1` durante 2 h y el crónico `S = 0,5` durante 7 días.

💡 **Cómo se explica en la clase [B105-C22](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md):**
- Descripción: la salida del laboratorio con el ritmo por `g`, el aumento por el estresor agudo y el efecto del crónico.
- Calcular la respuesta máxima y el aumento del área diaria a un estresor agudo.
- 🎯 **Por qué importa:** Una medición de cortisol sin hora del día no se interpreta: el ritmo diario domina. Y un estresor crónico cambia el nivel medio de una forma distinta que uno agudo.
- 🔗 **Se estudia junto con:** cortisol relativo, entrada, ganancia de retroalimentación, semivida.

📘 **Dónde se aprende** (1 clase): [B105-C22 · Sistema neuroendocrino y respuesta al estrés en vuelo](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md).

### Estructura de Lewis

- La estructura de Lewis dibuja los átomos con sus pares de enlace y solitarios.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- Dibujar la estructura de Lewis de H₂O, NH₃, CO₂ y NH₄⁺ contando pares.
- Ejercicio 1 · con los pasos indicados. Dibuja la estructura de Lewis del amoníaco.
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).
- 🔗 **Se estudia junto con:** electrones de valencia, regla del octeto, ion, catión.

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Estructura en grumos

- La estructura en grumos (*clumping*) es la heterogeneidad del viento.

💡 **Contexto en la clase [B24-C17](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md):**
- **Idea central (modelo mental):** Cuanto más brilla la estrella, más empuja la luz sobre su atmósfera; si la luz casi iguala a la gravedad, el gas escapa con facilidad.
- 🎯 **Por qué importa:** La masa que una estrella conserva hasta su final decide el destino: remanente, tipo de supernova, enriquecimiento del medio. Y las estrellas masivas no la conservan: pierden masa por vientos, erupciones y transferencia a una compañera.
- 🔗 **Se estudia junto con:** viento estelar, factor de Eddington, pérdida de masa, erupciones.

📘 **Dónde se aprende** (1 clase): [B24-C17 · Estrellas masivas y pérdida de masa](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md).

### Estructura hiperfina

- La estructura hiperfina es el desdoblamiento por el espín nuclear.

💡 **Cómo se explica en la clase [B55-C09](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md):**
- Reconocer la estructura hiperfina del HCN y su separación en velocidad.
- 🎯 **Por qué importa:** Las moléculas del espacio frío se detectan casi siempre por sus líneas de rotación en milimétrico y submilimétrico. Para identificar una línea hay que saber de dónde sale su frecuencia, qué fracción de niveles está poblada y cómo corregirla por la velocidad de la nube.
- 🔗 **Se estudia junto con:** rotor rígido, constante rotacional, distorsión centrifugal, catálogo JPL.

📘 **Dónde se aprende** (1 clase): [B55-C09 · Espectros moleculares de radio](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md).

### Estudio de compromiso

- Un estudio de compromiso (*trade study*) compara candidatas con criterios.

💡 **Cómo se explica en la clase [B83-C07](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md):**
- Plantear criterios y alternativas para un estudio de compromiso.
- 🎯 **Por qué importa:** Elegir una arquitectura «porque sí» es una decisión sin rastro. La decisión central: ¿qué arquitectura conviene, con qué criterios y qué tan firme es la elección?
- 🔗 **Se estudia junto con:** arquitectura candidata, AHP, razón de consistencia, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B83-C07 · Arquitecturas de sistemas](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md).

### Estudio de refinamiento

- Un estudio de refinamiento repite el cálculo con mallas cada vez más finas y mide cómo baja el error.

💡 **Cómo se explica en la clase [B23-C04](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md):**
- Hacer estudios de refinamiento separados en espacio y en tiempo y estimar el orden observado de cada uno.
- Ejercicio 3 · casi autónomo. En un estudio de refinamiento los errores son `1,2e-2` (N=20), `3,0e-3` (N=40), `7,5e-4` (N=80).
- 🎯 **Por qué importa:** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.
- 🔗 **Se estudia junto con:** solución fabricada, término fuente, condiciones de frontera, nodo fantasma.

📘 **Dónde se aprende** (1 clase): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md).

### ETag

- Un ETag es una etiqueta que identifica una versión de un recurso; con `If-None-Match`, el cliente pregunta «¿sigue siendo esta versión?» y el servidor responde 304 sin cuerpo si sí.

💡 **Cómo se explica en la clase [B14-C31](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md):**
- La respuesta de `/v1/escenas/escena-042` lleva `ETag: "c7eb868fbc6e529d"`, los primeros 16 caracteres del SHA-256 del cuerpo (C11).
- (Lo que significan 304, ETag e `If-None-Match` es conocimiento general; el RFC 9110 solo lo vi de forma parcial y no lo uso como respaldo.)
- 🎯 **Por qué importa:** Tu catálogo de escenas tiene 250 000 ítems y un programa ajeno quiere recorrerlos. Si le entregas una lista de golpe, se cae; si cada petición repite lo que ya tiene, desperdicias ancho de banda; si cambia un parámetro y falla sin explicación, nadie sabe qué hizo mal.
- 🔗 **Se estudia junto con:** API, recurso, ruta, Paginar.

📘 **Dónde se aprende** (1 clase): [B14-C31 · APIs de servicios de datos](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md).

### Etapa

- Una etapa es cada evaluación dentro del paso.
- Una etapa es un bloque de motor, tanque y estructura que se descarta al agotarse.
- Una etapa es un paso de la respuesta.

💡 **Cómo se explica en la clase [B11-C07](../programa/clases/B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md):**
- RK4 es unas 77 veces mejor con el doble de etapas.
- Que el orden observado es una prueba del código: un error en una etapa reduce el orden sin que el programa falle.
- ⚠️ **Error frecuente:** Usar `k₁` en lugar de `k₂` o `k₃` al construir una etapa. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** La mayoría de los programas de simulación científica usa, de forma directa o como base, un método de la familia Runge–Kutta. Entender RK4 permite leer cualquier código de propagación, estimar cuántos pasos necesita una órbita y saber en qué punto empieza a ser conveniente algo más sofisticado.
- 🔗 **Se estudia junto con:** método RK4 clásico, punto medio, familia Runge–Kutta, orden p.

📘 **Dónde se aprende** (3 clases): [B11-C07 · Runge-Kutta de cuarto orden](../programa/clases/B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md); [B77-C01 · Sistemas de lanzamiento](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md); [B119-C20 · Simulación de respuesta institucional a incidentes](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md).

### Etapa de multiplicación

- La etapa de multiplicación da a cada electrón una probabilidad `p` de producir otro.

💡 **Cómo se explica en la clase [B44-C09](../programa/clases/B44/B44-C09-ganancia-electronica/CLASE.md):**
- *Descripción textual:* cada etapa multiplica la carga con probabilidad `p`; tras `N` etapas la media crece como `(1+p)^N` y la varianza da el factor de ruido en exceso.
- 🎯 **Por qué importa:** Para señales muy débiles el ruido de lectura domina. La decisión central: ¿cuándo compensa multiplicar la carga a costa del ruido en exceso?
- 🔗 **Se estudia junto con:** ganancia, factor de ruido en exceso, proceso de ramificación.

📘 **Dónde se aprende** (1 clase): [B44-C09 · Ganancia electrónica](../programa/clases/B44/B44-C09-ganancia-electronica/CLASE.md).

### ETC

- El EAC es la estimación del costo final; el ETC, lo que falta gastar; el VAC, `BAC − EAC`.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- Si el rendimiento de costo se mantiene, `EAC = BAC/CPI = 100,63` Mum (ETC `40,63`, VAC `-20,63`), idéntico a `AC + (BAC − EV)/CPI` (error `0,0e+00`).
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, EV, AC.

📘 **Dónde se aprende** (1 clase): [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### Étendue

- La étendue `A·Ω` es el producto del área de la abertura y el ángulo sólido de un píxel.

💡 **Cómo se explica en la clase [B57-C04](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md):**
- Con `A = π(0,05)² m²` y `Ω = IFOV²`, la étendue vale `1,422e-11 m² sr`.
- Calcular el tiempo de integración de un sensor de barrido y la étendue de un píxel.
- 🎯 **Por qué importa:** Un sensor puede tener muchos píxeles y aun así ser inútil porque cada píxel recoge pocos fotones. La decisión central: ¿cuánta apertura y cuánto tiempo de integración hacen falta para que la señal supere el ruido de fotones?
- 🔗 **Se estudia junto con:** barredor, tiempo de integración, eficiencia cuántica, ruido de fotones.

📘 **Dónde se aprende** (1 clase): [B57-C04 · Satélites ópticos de observación](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md).

### Etiqueta

- Una etiqueta (*label*) es la descripción en XML.
- Una etiqueta (*tag*) nombra una versión de imagen;
- La etiqueta `T = trunc(HMAC-SHA256(K, cnt ‖ cmd), b)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- El laboratorio aplica seis reglas, convenciones de esta clase: imagen base con versión fija (no `latest` ni sin etiqueta);
- Otra: «exponer la versión del código en una etiqueta».
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?
- 🔗 **Se estudia junto con:** imagen, contenedor, Dockerfile, capa.

📘 **Dónde se aprende** (4 clases): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md); [B14-C21 · Datos de misiones planetarias: PDS4, etiquetas y SPICE](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md); [B88-C17 · Ciberseguridad de aviónica](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md); [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md).

### Etiqueta de oro

- Una etiqueta de oro es la de mayor confianza (de expertos), usada para auditar.

💡 **Cómo se explica en la clase [B17-C10](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md):**
- Con dos anotadores que aciertan cada uno con probabilidad `p = 0,8` e independientes, ambos coinciden si los dos aciertan o los dos fallan (en el caso binario eso lleva a la misma etiqueta): `pₒ = p² + (1 − p)² = 0,64 + 0,04 = 0,68`.
- En el laboratorio, un modelo entrenado con etiquetas con 20 % de ruido simétrico, y evaluado con etiquetas limpias, dio 0,843, igual que uno entrenado con etiquetas limpias (0,843): el ruido simétrico apenas afectó el entrenamiento en este caso (muchos datos, un modelo simple).
- ⚠️ **Error frecuente:** Evaluar con etiquetas ruidosas sin auditar. Ejercicio 3.
- 🎯 **Por qué importa:** Se quiere entrenar un modelo que distinga galaxias espirales de elípticas. Hay un millón de imágenes y nadie las ha etiquetado.
- 🔗 **Se estudia junto con:** protocolo de etiquetado, anotador, acuerdo observado, acuerdo esperado por azar.

📘 **Dónde se aprende** (1 clase): [B17-C10 · Conjuntos de datos etiquetados para aprendizaje supervisado](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md).

### Etiquetas

- El aprendizaje supervisado ajusta un modelo a pares (entrada, respuesta): las respuestas se llaman etiquetas.

💡 **Cómo se explica en la clase [B17-C02](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md):**
- Un clasificador de un vecino guarda todos los ejemplos y predice la etiqueta del más cercano: acierta el 100 % en entrenamiento por construcción.
- A["Datos con etiqueta"] --> B["Reservar prueba final"]
- 🎯 **Por qué importa:** Un modelo que clasifica señales como «candidata» o «no candidata» puede acertar el 100 % de los ejemplos con los que se entrenó y fallar la cuarta parte de los nuevos: memorizó. Lo que importa a un equipo científico es el desempeño en datos que el modelo no vio.
- 🔗 **Se estudia junto con:** aprendizaje supervisado, clasificación, regresión, conjunto de entrenamiento.

📘 **Dónde se aprende** (1 clase): [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md).

### ETL

- El ETL supone que las poblaciones siguen la temperatura local.
- El ETL reparte la población con `(2J+1) exp(−E_J/kT)`.

💡 **Cómo se explica en la clase [B32-C02](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué falla si no hay ETL?
- ⚠️ **Error frecuente:** Aplicar ETL sin discutirlo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Si el ETL falla, las abundancias que se derivan son erróneas. La decisión central: ¿cuánto hidrógeno está ionizado a cada temperatura y densidad?
- 🔗 **Se estudia junto con:** ecuación de Boltzmann, ecuación de Saha, fracción ionizada, desviación no ETL.

📘 **Dónde se aprende** (2 clases): [B32-C02 · Equilibrio termodinámico local y desviaciones no LTE](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md); [B46-C12 · Emisiones moleculares](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md).

### Euler explícito

- El método de Cowell integra directamente `r̈ = −μ r/r³ + a_p`. Euler explícito es de orden 1.
- La respuesta a un escalón `T(t) = T_eq + (T₀ − T_eq)e^(−t/τ)`. Euler explícito es estable si `Δt < 2τ`.
- El paso de integración `dt` es el intervalo entre estados. Euler explícito avanza con la pendiente inicial;
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B10-C20](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md):**
- Euler explícito multiplica la norma por `√(1 + (h|ω|/2)²) > 1` en cada paso; sin renormalizar, `q` deja de ser unitario y deja de representar una rotación pura.
- Es una propiedad de este caso de eje fijo y de la métrica; en general el Euler explícito es de primer orden, y hay que medirlo con el laboratorio.
- 🎯 **Por qué importa:** Los giróscopos de un satélite miden la velocidad angular en ejes del cuerpo. Para saber hacia dónde apunta una cámara, hay que integrar esa velocidad en el tiempo, miles de veces.
- 🔗 **Se estudia junto con:** ecuación cinemática del cuaternión, constante, método de un paso, Runge–Kutta de cuarto orden (RK4).

📘 **Dónde se aprende** (5 clases): [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md); [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md); [B85-C26 · Análisis térmico transitorio y casos extremos](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md); [B97-C23 · Diseño de simulador de misión robótica](../programa/clases/B97/B97-C23-diseno-de-simulador-de-mision-robotica/CLASE.md).

### Euler implícito

- Euler explícito es estable si `Δt < 2τ`. Euler implícito es estable siempre (aquí, `x₊ = (x + Δt(q + G T_ref)/C)/(1 + Δt G/C)`).
- RK4 `R = 1 + z + z²/2 + z³/6 + z⁴/24`; Euler implícito `y_{k+1} = y_k + h λ y_{k+1}` da `R = 1/(1 − z)`.
- Un método implícito define el nuevo estado mediante una ecuación que lo contiene. Euler implícito: `y_{n+1} = y_n + h f(t_{n+1}, y_{n+1})`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C09](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md):**
- Implícitos (Euler implícito, y sus relativos de orden alto): resuelven una ecuación por paso, estables en problemas rígidos.
- RK4, en `−2,785`; el Euler implícito no la cruza jamás para `z` negativo.
- 🎯 **Por qué importa:** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.
- 🔗 **Se estudia junto con:** ecuación de prueba, factor de amplificación, estable, región de estabilidad.

📘 **Dónde se aprende** (5 clases): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md); [B55-C20 · Modelo simplificado de red astroquímica](../programa/clases/B55/B55-C20-modelo-simplificado-de-red-astroquimica/CLASE.md); [B85-C18 · Modelado térmico por nodos](../programa/clases/B85/B85-C18-modelado-termico-por-nodos/CLASE.md); [B85-C26 · Análisis térmico transitorio y casos extremos](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md).

### Euler propio

- Una secuencia de tipo Tait–Bryan usa tres ejes distintos (3‑2‑1: `z`, `y`, `x`); una de Euler propio repite el primero y el tercero (3‑1‑3: `z`, `x`, `z`).

💡 **Cómo se explica en la clase [B10-C14](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md):**
- Es la singularidad típica de las secuencias de Euler propio (resultado estándar).
- 🎯 **Por qué importa:** Un satélite que apunta una antena al cenit tiene el cabeceo cerca de `90°`; si la actitud se guarda con ángulos de Euler, justo ahí el cálculo se vuelve inestable: ángulos que cambian muy rápido para movimientos pequeños, o dos conjuntos de ángulos distintos para la misma orientación.
- 🔗 **Se estudia junto con:** ángulos de Euler, tipo Tait–Bryan, guiñada, cabeceo.

📘 **Dónde se aprende** (1 clase): [B10-C14 · Ángulos de Euler y singularidades](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md).

### Euler simpléctico

- El Euler simpléctico actualiza primero la velocidad y luego la posición con la velocidad nueva, orden 1.

💡 **Cómo se explica en la clase [B11-C11](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md):**
- El Euler simpléctico queda acotado también, pero en un valor mucho mayor (`3,95 × 10⁻³`), porque es de orden 1.
- El script [leapfrog_frente_a_rk4.py](leapfrog_frente_a_rk4.py) compara leapfrog, Euler simpléctico y RK4 en 1 000 vueltas, comprueba la reversibilidad y mide el error de fase.
- 🎯 **Por qué importa:** Para el sistema solar, anillos planetarios o constelaciones se necesitan integraciones de millones de vueltas. Un método que añade o quita un poco de energía en cada vuelta termina destruyendo la órbita.
- 🔗 **Se estudia junto con:** hamiltoniano, simpléctico, leapfrog, reversibilidad temporal.

📘 **Dónde se aprende** (1 clase): [B11-C11 · Métodos simplécticos](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md).

### EV

- El PV es el valor del trabajo planificado a la fecha; el EV, el valor del trabajo logrado; el AC, el costo real.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- La suma de los paquetes coincide con la de los elementos y con el proyecto para BAC, PV, EV y AC (error `0,0e+00`): lo que está en los hijos es todo lo que está en el padre.
- Con `PV = 57,00`, `EV = 47,70` y `AC = 60,00`: `CV = EV − AC = -12,30` y `SV = EV − PV = -9,30` Mum;
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, AC, CPI.

📘 **Dónde se aprende** (1 clase): [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### Evalúa

- Una expresión es una combinación de valores, variables y operadores que Python evalúa a un valor: `2 + 3 * 4` evalúa a `14`.

💡 **Cómo se explica en la clase [B07-C03](../programa/clases/B07/B07-C03-operadores-y-expresiones/CLASE.md):**
- Fíjate en que `t_anios  2 / a_rel  3` se evalúa como `(t_anios  2) / (a_rel  3)`, porque `` precede a `/`.
- Una expresión se evalúa como un árbol: las operaciones de mayor precedencia son ramas bajas que se resuelven primero y alimentan a las de arriba.
- 🎯 **Por qué importa:** Casi cualquier resultado científico es una expresión: una masa dividida por un volumen, un cociente de períodos. Si no sabes en qué orden Python evalúa `a / b  3`, escribirás una fórmula distinta de la que piensas y no recibirás ningún aviso: el programa funcionará y dará un número equivocado.
- 🔗 **Se estudia junto con:** operador, operando, expresión, sentencia.

📘 **Dónde se aprende** (1 clase): [B07-C03 · Operadores y expresiones](../programa/clases/B07/B07-C03-operadores-y-expresiones/CLASE.md).

### Evaluación con maqueta

- La evaluación con maqueta prueba un diseño con una representación física o virtual antes de construirlo.

💡 **Cómo se explica en la clase [B109-C12](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md):**
- *Descripción textual:* cada evaluador puntúa ambas maquetas; la diferencia pareada se contrasta con un test exacto y se acota con un bootstrap; una lista de verificación aparte se evalúa con el acuerdo entre inspectores; todo termina en un informe que rotula qué es simulado.
- La evidencia es tu informe de evaluación de dos maquetas del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Sin medir, «esta distribución es mejor» es una opinión. La decisión central: ¿la diferencia entre dos maquetas es mayor que lo que daría el azar, y las personas que la evalúan coinciden entre sí?
- 🔗 **Se estudia junto con:** lista de verificación, NMSUS, prueba pareada, kappa de Cohen.

📘 **Dónde se aprende** (1 clase): [B109-C12 · Evaluación de factores humanos de maquetas y distribuciones](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md).

### Evaluación de la función

- Una evaluación de la función es una llamada a `F`.

💡 **Contexto en la clase [B11-C05](../programa/clases/B11/B11-C05-metodo-de-euler/CLASE.md):**
- **Idea central (modelo mental):** Euler es caminar siguiendo la dirección que marca el terreno *en el punto donde estás*, sin mirar cómo cambia durante el paso. En un terreno que se curva, te desvías siempre hacia el lado convexo.
- 🎯 **Por qué importa:** La mayoría de las ecuaciones del movimiento no tiene solución en forma cerrada. Un computador no resuelve la ecuación: da pasos pequeños, y cada paso usa la pendiente conocida para estimar el estado siguiente.
- 🔗 **Se estudia junto con:** paso, método de Euler explícito, error local de truncamiento, error global.

📘 **Dónde se aprende** (1 clase): [B11-C05 · Método de Euler](../programa/clases/B11/B11-C05-metodo-de-euler/CLASE.md).

### Evaluación de madurez

- La evaluación de madurez debe estar lista antes del PDR.

💡 **Cómo se explica en la clase [B83-C18](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md):**
- La evidencia es la evaluación de madurez tecnológica con plan de madurización del ejercicio 12 (sección 20).
- Ejercicio 8 · autónomo. ¿Cuándo debe estar lista la evaluación de madurez según S5?
- 🎯 **Por qué importa:** Un elemento «con herencia de vuelo» que se usa en otro entorno no es TRL 9. La decisión central: ¿cuál es el TRL real del sistema, qué elementos lo frenan y cuánto cuesta llevarlos al nivel que pide la revisión?
- 🔗 **Se estudia junto con:** TRL, TRL del sistema, herencia, AD2.

📘 **Dónde se aprende** (1 clase): [B83-C18 · Niveles de madurez tecnológica](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md).

### Evaluación formativa

- La evaluación formativa del plan es el tiempo dedicado a diagnóstico y evaluación.

💡 **Cómo se explica en la clase [B131-C11](../programa/clases/B131/B131-C11-plan-completo-de-una-clase-de-astronomia/CLASE.md):**
- La evaluación formativa (B1 + B6) ocupa `20` min, el `22 %`.
- (3) La evaluación formativa ocupa al menos el 10 % del tiempo.
- 🎯 **Por qué importa:** Un buen plan se puede revisar: sus tiempos suman, cada resultado tiene actividad y evaluación, y nada pone en riesgo a nadie. La decisión central: ¿este plan es coherente y seguro antes de entrar al aula?
- 🔗 **Se estudia junto con:** bloque, alineación, plan defectuoso.

📘 **Dónde se aprende** (1 clase): [B131-C11 · Plan completo de una clase de astronomía](../programa/clases/B131/B131-C11-plan-completo-de-una-clase-de-astronomia/CLASE.md).

### Evaluación tipo A

- La evaluación tipo A estima `u` de una serie de lecturas (S1, 2.3.2); la tipo B, de información como certificados, hojas técnicas o juicio (S1, 2.3.3).

💡 **Contexto en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- **Idea central (modelo mental):** Imagina disparar a una diana: un grupo de impactos muy juntos pero lejos del centro es preciso con error sistemático; impactos dispersos alrededor del centro es exacto con error aleatorio. La incertidumbre cubre ambos y se expresa como un intervalo alrededor del valor.
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.
- 🔗 **Se estudia junto con:** error, incertidumbre, incertidumbre estándar, tipo B.

📘 **Dónde se aprende** (1 clase): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md).

### Evaluar

- Una identidad es una igualdad válida para cualquier valor (`(a + b)² = a² + 2ab + b²`). Evaluar es sustituir variables por valores y calcular.

💡 **Cómo se explica en la clase [B03-C13](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md):**
- X --> V["Evaluar con a₁ = 149,598 y a₂ = 227,956 (10⁶ km)"]
- Evaluar una expresión sustituyendo valores con sus unidades.
- ⚠️ **Error frecuente:** Evaluar sin unidades. Ejercicio 11.
- 🎯 **Por qué importa:** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.
- 🔗 **Se estudia junto con:** expresión algebraica, término, términos semejantes, coeficiente.

📘 **Dónde se aprende** (1 clase): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md).

### Evanescente

- Un modo evanescente decae.

💡 **Cómo se explica en la clase [B37-C08](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md):**
- p y g viven en cavidades separadas por una zona evanescente; si esa zona es delgada, los modos se acoplan y se vuelven mixtos (C12).
- Clasificar un modo como p, g o evanescente.
- 🎯 **Por qué importa:** Los modos p y g sondean regiones distintas. La decisión central: ¿en qué cavidad se propaga un modo de frecuencia y grado dados?
- 🔗 **Se estudia junto con:** armónico esférico, modo p, g, frecuencia de Lamb.

📘 **Dónde se aprende** (1 clase): [B37-C08 · Oscilaciones no radiales: modos p, g y mixtos](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md).

### Evaporación

- La evaporación (*boil-off*) es la masa de criógeno que se vaporiza por el calor que entra: `ṁ = Q̇/h_fg`.
- La evaporación del lubricante sigue `J = P √(M/(2πRT))`.

💡 **Cómo se explica en la clase [B84-C14](../programa/clases/B84/B84-C14-rodamientos-y-lubricacion-espacial/CLASE.md):**
- La evaporación (cota superior) es menor que la vida mecánica de 4 años a 20 °C y más de dos órdenes de magnitud menor a 80 °C: el lubricante limita la vida.
- *Descripción textual:* Hertz da el contacto, la capacidad dinámica da la vida L10 y la presión de vapor da el tiempo de evaporación del lubricante; la menor de las dos vidas gobierna.
- ⚠️ **Error frecuente:** Usar la cota superior de evaporación como cálculo de vida. Se corrige con la sección de transferencia.
- 🎯 **Por qué importa:** La vida de un rodamiento espacial la limita el lubricante, no la fatiga: un cálculo de evaporación de un minuto dice si basta 2 mg o hace falta un depósito. La decisión central: ¿qué presión de contacto soporta el rodamiento y cuánto dura su lubricante en vacío?
- 🔗 **Se estudia junto con:** contacto de Hertz, vida L10, conformidad.

📘 **Dónde se aprende** (2 clases): [B84-C14 · Rodamientos y lubricación espacial](../programa/clases/B84/B84-C14-rodamientos-y-lubricacion-espacial/CLASE.md); [B100-C04 · Almacenamiento remoto y depósitos de suministros](../programa/clases/B100/B100-C04-almacenamiento-remoto-y-depositos-de-suministros/CLASE.md).

### Evapotranspiración

- La evapotranspiración `ET` es el agua perdida por m² y día.

💡 **Contexto en la clase [B59-C14](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md):**
- **Idea central (modelo mental):** Como cultivar bajo una lámpara: lo que crece depende de la luz recibida y esa luz se paga con electricidad. Límite: aquí la luz es el único factor limitante; en un cultivo real también lo son el CO₂, los nutrientes y la temperatura.
- 🎯 **Por qué importa:** Cultivar exige luz, y la luz eléctrica cuesta potencia. La decisión central: ¿cuántos metros cuadrados y cuántos kilovatios necesita un cultivo para producir el oxígeno de una persona?
- 🔗 **Se estudia junto con:** PPFD, fotones por O₂, eficacia, sustrato.

📘 **Dónde se aprende** (1 clase): [B59-C14 · Agricultura y sustratos artificiales](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md).

### Evapotranspiración de referencia (ETo)

- La evapotranspiración de referencia (ETo) es la de un cultivo hipotético bien regado; la del cultivo (ETc) es `Kc·ETo`.

💡 **Cómo se explica en la clase [B115-C06](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md):**
- Casos de referencia consultados: el capítulo 2 de FAO-56 define la evapotranspiración de referencia (ETo en mm/día), el coeficiente de cultivo `Kc = ETc/ETo` y un cultivo hipotético de 0,12 m de altura, 70 s/m de resistencia superficial y albedo de 0,23.
- Calcular la evapotranspiración de referencia con Penman–Monteith y separar el término radiativo y el aerodinámico.
- 🎯 **Por qué importa:** El cultivo es el mayor flujo de agua de un hábitat con plantas. La decisión central: ¿cuánta agua transpira el cultivo, cuánta se recupera y cuánta hay que reponer, y con qué incertidumbre?
- 🔗 **Se estudia junto con:** del cultivo (ETc), radiación neta (Rn), déficit de presión de vapor, pendiente Δ.

📘 **Dónde se aprende** (1 clase): [B115-C06 · Balance de agua y evapotranspiración en cultivos](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md).

### Evento

- Un evento es un subconjunto de `Ω`: «ocurre» si el resultado pertenece a él.
- Un evento es algo que ocurre en un lugar y un instante.
- El evento es la curva completa.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C01](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md):**
- Para dos eventos cualquiera, `P(A∪B) = P(A) + P(B) − P(A∩B)`: al sumar `P(A)` y `P(B)` se cuenta dos veces la intersección.
- Un evento es una etiqueta que pones a un grupo de historias; su probabilidad es la suma de los pesos de ese grupo.
- ⚠️ **Error frecuente:** Confundir excluyentes con independientes. Se corrige con los ejercicios 7 y 8: eventos excluyentes con probabilidad positiva son dependientes.
- 🎯 **Por qué importa:** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.
- 🔗 **Se estudia junto con:** experimento aleatorio, espacio muestral, probabilidad, complemento.

📘 **Dónde se aprende** (6 clases): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md); [B26-C01 · Postulados de relatividad especial](../programa/clases/B26/B26-C01-postulados-de-relatividad-especial/CLASE.md); [B29-C05 · Microlentes gravitacionales](../programa/clases/B29/B29-C05-microlentes-gravitacionales/CLASE.md); [B77-C20 · Simulación académica de una trayectoria de vuelo](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md); [B96-C20 · Simulación de jornada de control de misión](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md); [B106-C10 · Gestión de residuos humanos](../programa/clases/B106/B106-C10-gestion-de-residuos-humanos/CLASE.md).

### Evento de partícula simple

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C14](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md):**
- Simular eventos de partícula simple con Poisson.
- 🎯 **Por qué importa:** El blindaje reduce la dosis hasta que el protón se detiene; los eventos de partícula simple, en cambio, son aleatorios. La decisión central: ¿qué espesor de blindaje y qué probabilidad de eventos son aceptables?
- 🔗 **Se estudia junto con:** dosis ionizante total, fluencia, blindaje, sección eficaz.

📘 **Dónde se aprende** (1 clase): [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md).

### Evento de partículas solares

- El límite de carrera de 600 mSv y el de un evento de partículas solares (SPE) de 250 mSv son los citados en un resumen de la NASA.
- Un evento de partículas solares (SPE) es una ráfaga de protones de energía muy variable.

💡 **Contexto en la clase [B105-C06](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md):**
- 🎯 **Por qué importa:** La dosis no se «lee»: se calcula a partir de una dosis absorbida, de factores de calidad y de ponderación, y esos factores tienen incertidumbre. La decisión central: ¿qué fracción del límite de carrera consume una misión y con qué probabilidad lo supera una secuencia de misiones?
- 🔗 **Se estudia junto con:** dosis absorbida, dosis equivalente, dosis efectiva, límite de carrera.

📘 **Dónde se aprende** (2 clases): [B105-C06 · Radiación ionizante y exposición](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md); [B112-C03 · Efectos agudos de la radiación](../programa/clases/B112/B112-C03-efectos-agudos-de-la-radiacion/CLASE.md).

### Evento fuera del eje

- Un evento fuera del eje se ve con `θ_v > θ_c`.

💡 **Cómo se explica en la clase [B28-C12](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md):**
- Un evento con brillo bajo no implica una energía baja: puede estar visto fuera del eje.
- 🎯 **Por qué importa:** Un destello gamma débil puede ser un evento normal visto de lado. Un modelo de emisión conjunta permite relacionar qué se ve en cada mensajero con el ángulo de visión.
- 🔗 **Se estudia junto con:** chorro estructurado, núcleo, ángulo de visión, exponente Doppler.

📘 **Dónde se aprende** (1 clase): [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md).

### Evento tope

- El evento tope es la falla del sistema.

💡 **Cómo se explica en la clase [B88-C16](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md):**
- Se enumeran los `2⁵ = 32` estados de los 5 eventos básicos, con producto de probabilidades: `P(tope) = 2,6995×10⁻³`.
- Evento tope sintético «pérdida de control» = (fallo de computador `A ∧ B`) ∨ (fallo de actuadores `C ∨ (D ∧ E)`) con `P(A) = P(B) = 10⁻²`, `P(C) = 10⁻⁴`, `P(D) = P(E) = 5×10⁻²`.
- 🎯 **Por qué importa:** Una nave tolera fallos si ninguno solo provoca la pérdida y las combinaciones peligrosas son improbables. La decisión central: ¿qué combinaciones mínimas de fallos causan la pérdida y cuál elemento merece más protección?
- 🔗 **Se estudia junto con:** eventos básicos, conjunto mínimo de corte, importancia de Birnbaum, matriz severidad–probabilidad.

📘 **Dónde se aprende** (1 clase): [B88-C16 · Ingeniería de seguridad funcional](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md).

### Eventos básicos

- Los eventos básicos son los fallos elementales.
- Un árbol de fallos descompone un evento superior con compuertas Y y O hasta eventos básicos.

💡 **Cómo se explica en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- *Descripción textual:* el evento superior se descompone con compuertas en eventos básicos; la expansión da los conjuntos de corte, reducidos por absorción a mínimos; con ellos y las probabilidades se calcula `P(top)` por tres vías y la importancia indica qué proteger primero.
- Un FMEA (C22) alimenta los eventos básicos.
- ⚠️ **Error frecuente:** Tratar un evento repetido como independiente. Usa cortes o enumeración sobre los eventos básicos
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?
- 🔗 **Se estudia junto con:** árbol de fallos, conjunto de corte, mínimo, MOCUS.

📘 **Dónde se aprende** (2 clases): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md); [B88-C16 · Ingeniería de seguridad funcional](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md).

### Eventos esperados

- Los eventos esperados son `μ = λ n T` con `T` en años.

💡 **Cómo se explica en la clase [B105-C14](../programa/clases/B105/B105-C14-atencion-de-urgencia-remota/CLASE.md):**
- *Descripción textual:* la tasa, la tripulación y la duración dan los eventos esperados; el número de eventos es de Poisson; cada uno tiene una gravedad y un coste, y el total se compara con la reserva.
- Calcular los eventos esperados `μ = λ n T` y las probabilidades de Poisson `P(0)`, `P(≥1)` y `P(≥k)`.
- 🎯 **Por qué importa:** La atención remota se diseña para eventos poco frecuentes pero casi seguros a lo largo de una misión. La decisión central: ¿cuántos eventos se esperan, con qué probabilidad hay al menos uno grave y qué reserva de recursos cubre el 99 % de las misiones?
- 🔗 **Se estudia junto con:** proceso de Poisson, tasa, gravedad, reserva.

📘 **Dónde se aprende** (1 clase): [B105-C14 · Atención de urgencia remota](../programa/clases/B105/B105-C14-atencion-de-urgencia-remota/CLASE.md).

### Evidencia

- Una evidencia es un dato que apoya o contradice una afirmación.
- El prior `P(θ)` expresa lo que se sabe de `θ` antes de ver los datos; la verosimilitud `P(datos | θ)` es el modelo de los datos (C07); la posterior `P(θ | datos)` es el conocimiento actualizado; el denominador, la evidencia o verosimilitud marginal, normaliza (y es clave en C22).
- La evidencia (o verosimilitud marginal) de un modelo `M` es `Z = ∫ p(datos | θ, M) p(θ | M) dθ`: promedia la verosimilitud sobre el prior.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C05](../programa/clases/B01/B01-C05-observacion-frente-a-interpretacion/CLASE.md):**
- La evidencia es la tabla O/I/M del ejercicio 12 (sección 20).
- La conclusión sobra respecto de la evidencia.
- 🎯 **Por qué importa:** En septiembre de 2011 la colaboración OPERA publicó que neutrinos enviados desde el CERN habían llegado a su detector, a unos 730 km, 60,7 ns antes de lo que tardaría la luz (S1, versión 1). Una cifra medida pasó rápidamente a titulares que decían otra cosa.
- 🔗 **Se estudia junto con:** observación, dato, inferencia, modelo.

📘 **Dónde se aprende** (5 clases): [B01-C05 · Observación frente a interpretación](../programa/clases/B01/B01-C05-observacion-frente-a-interpretacion/CLASE.md); [B12-C12 · Inferencia bayesiana](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md); [B12-C22 · Comparación de modelos: evidencia bayesiana y criterios de información](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md); [B19-C07 · Comparación de modelos bayesianos](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Evidencia huérfana

- Cobertura: requisitos cerrados/total. Evidencia huérfana: registro sin requisito.

💡 **Cómo se explica en la clase [B90-C18](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md):**
- Las evidencias huérfanas son las que no aparecen en la matriz (aquí, E8 declarada para la comprobación).
- Ejercicio 7 · autónomo. ¿Qué es una evidencia huérfana y por qué importa?
- 🎯 **Por qué importa:** Una campaña de ensayos produce informes, fotos y registros; si no se sabe qué requisito respalda cada uno o si un informe fue editado después, la verificación no vale como evidencia. La decisión central: ¿qué requisitos faltan por verificar y cómo se demuestra que la evidencia no fue alterada?
- 🔗 **Se estudia junto con:** Trazabilidad, Matriz de verificación, Cobertura, SHA-256.

📘 **Dónde se aprende** (1 clase): [B90-C18 · Trazabilidad de evidencias](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md).

### Evidencias

- Las evidencias son los resultados trazables que sostienen cada veredicto.

💡 **Cómo se explica en la clase [B23-C08](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md):**
- Esta sección es parte de la evidencia: un informe sin límites es sospechoso.
- Nuestro ejemplo conductor es el propagador de dos cuerpos de C02–C05: se declara apto o no para un uso previsto concreto —«propagar la Tierra hasta 91 d con error ≤ 10⁻³ au»— con evidencia de verificación (solución exacta, orden de convergencia, energía) y de validación (efeméride de Horizons).
- 🎯 **Por qué importa:** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.
- 🔗 **Se estudia junto con:** uso previsto, criterio de aceptación, regla de decisión, advertencia.

📘 **Dónde se aprende** (1 clase): [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Evolución darwiniana

- Homeostasis es la regulación del medio interno. Evolución darwiniana es el cambio de una población por variación heredable y reproducción diferencial.

💡 **Cómo se explica en la clase [B56-C01](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md):**
- La NASA describe la astrobiología como el estudio del origen, la evolución y la distribución de la vida en el universo, y cita como definición de trabajo frecuente «un sistema autosostenido capaz de evolución darwiniana»; añade que existen varios cientos de otras definiciones (S1, consultada el 2026-11-09).
- Explicar por qué una definición que depende de la evolución darwiniana deja fuera a un individuo estéril.
- 🎯 **Por qué importa:** Una misión que busca vida necesita saber qué buscar y qué contará como hallazgo. Si el criterio es vago, cualquier resultado se puede discutir; si es demasiado estrecho, se pasa por alto lo que no se parece a la vida terrestre.
- 🔗 **Se estudia junto con:** definición operativa, criterio necesario, suficiente, caso límite.

📘 **Dónde se aprende** (1 clase): [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md).

### Evolución térmica parametrizada

- La evolución térmica parametrizada reemplaza la convección completa por una ley `Nu(Ra)`.

💡 **Contexto en la clase [B65-C01](../programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/CLASE.md):**
- **Idea central (modelo mental):** Como una olla calentada por abajo: mientras el fondo esté poco más caliente que la tapa, el calor sube por conducción; al superar un umbral, el fluido se pone en movimiento y el calor sube mucho más rápido.
- 🎯 **Por qué importa:** Sin convección, el interior de un planeta rocoso solo perdería calor por conducción y se enfriaría con una escala de tiempo mucho mayor. La decisión central: ¿cuánto calor saca la convección y a qué temperatura se estabiliza un manto que sigue produciendo calor radiactivo?
- 🔗 **Se estudia junto con:** número de Rayleigh, Rayleigh crítico, número de Nusselt, viscosidad de Arrhenius.

📘 **Dónde se aprende** (1 clase): [B65-C01 · Convección del manto y evolución térmica de interiores planetarios](../programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/CLASE.md).

### EWMA

- La EWMA usa `z_t = λ x̄_t + (1−λ) z_{t−1}`.
- La EWMA pondera con `λ = 2/(N + 1)`.

💡 **Cómo se explica en la clase [B84-C35](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md):**
- Shewhart señala en los subgrupos `22, 29, 31, 32, 34, 36, 37`; la EWMA, de forma sostenida desde el `22`.
- Con `ARL₀` iguales (~370), la EWMA detecta desplazamientos pequeños mucho antes que Shewhart.
- 🎯 **Por qué importa:** Un proceso con `Cpk` de 1,33 puede desplazarse 1σ sin dejar piezas fuera de tolerancia durante semanas si solo se inspecciona el producto; la carta lo detecta en pocos subgrupos. La decisión central: ¿qué carta detecta antes un desplazamiento del proceso y qué capacidad tiene el proceso antes y después?
- 🔗 **Se estudia junto con:** carta X-barra, ARL.

📘 **Dónde se aprende** (2 clases): [B84-C35 · Control de procesos de fabricación y calidad](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md); [B107-C05 · Prevención de lesiones en entrenamiento y trabajo operativo](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md).

### Exacta por definición

- Una constante es un valor que no cambia: exacta por definición (como `c = 299 792 458 m/s` en el SI, S4), medida (como `G`, con incertidumbre) o nominal (valor de conversión fijado por acuerdo, como el `(GM)☉` de la IAU).

💡 **Cómo se explica en la clase [B03-C12](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md):**
- Clasificar una constante como exacta por definición, medida o nominal.
- 🎯 **Por qué importa:** La masa del Sol se conoce con unas cinco cifras. Sin embargo, el producto `GM` del Sol se conoce con diez, y la constante `G` por sí sola con apenas cinco.
- 🔗 **Se estudia junto con:** variable, parámetro, constante, medida.

📘 **Dónde se aprende** (1 clase): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md).

### Exactitud

- La exactitud `(a+d)/N` es la fracción de aciertos totales.
- La exactitud es la fracción de predicciones correctas.
- La exactitud es `(TP + TN)/total`; la precisión, `TP/(TP + FP)`; la exhaustividad (*recall*), `TP/(TP + FN)`; el F1, la media armónica de las dos últimas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C24](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md):**
- La exactitud engaña: un pronóstico «siempre no» tiene `TSS = 0` y una exactitud de `0,899` en los datos sintéticos.
- Exactitud: simple, engañosa con eventos raros.
- ⚠️ **Error frecuente:** Usar la exactitud con eventos raros. Se corrige con 8.3 y el ejercicio 4.
- 🎯 **Por qué importa:** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.
- 🔗 **Se estudia junto con:** puntaje de Brier, referencia climatológica, puntaje de habilidad de Brier, tabla de contingencia.

📘 **Dónde se aprende** (4 clases): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md); [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B129-C07 · Proyecto de ciencia ciudadana validable](../programa/clases/B129/B129-C07-proyecto-de-ciencia-ciudadana-validable/CLASE.md).

### Exactitud de medida

- La exactitud de medida es la cercanía entre un valor medido y un valor verdadero del mensurando (S1, 2.13); no es una cantidad, y una medida es «más exacta» cuando su error es menor.

💡 **Contexto en la clase [B13-C03](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md):**
- **Idea central (modelo mental):** Una diana: el centro es el valor verdadero. Los disparos agrupados lejos del centro son precisos y poco veraces; los dispersos alrededor del centro son veraces en promedio y poco precisos; agrupados en el centro, ambas cosas; dispersos y desplazados, ninguna.
- 🎯 **Por qué importa:** Un telémetro láser que mide la distancia a un reflector de prueba puede dar lecturas muy agrupadas pero todas desplazadas: es repetible y, aun así, está mal. Otro puede dar lecturas dispersas que, en promedio, caen sobre el valor correcto.
- 🔗 **Se estudia junto con:** veracidad, precisión de medida, error de medida, sesgo.

📘 **Dónde se aprende** (1 clase): [B13-C03 · Exactitud frente a precisión](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md).

### Exactitud del registro

- La exactitud del registro es la fracción de posiciones cuyo conteo físico coincide con el registro.

💡 **Cómo se explica en la clase [B100-C01](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md):**
- Calcular la exactitud del registro con un conteo cíclico.
- Ejercicio 12 · integrador. Elabora tu *registro de lotes con consulta de trazabilidad*: tabla de recepciones, conservación FIFO y FEFO, trazabilidad de un lote y exactitud, con lo sintético rotulado.
- 🎯 **Por qué importa:** Un inventario que solo sabe «cuántas unidades hay» no puede decir de qué lote vienen, cuándo caducan ni dónde se usaron. La decisión central: ¿qué registro mínimo hace falta para emitir primero lo que caduca antes y para encontrar, si un lote resulta defectuoso, adónde fue?
- 🔗 **Se estudia junto con:** lote, FIFO, FEFO, Caducado.

📘 **Dónde se aprende** (1 clase): [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Exactitud global

- La exactitud global es la fracción de aciertos.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- La exactitud global (90,3 %) oculta esa asimetría.
- Ejercicio 9 · transferencia. Un mapa tiene el 95 % de exactitud global, pero la clase «cultivo de interés» ocupa el 2 % del área.
- ⚠️ **Error frecuente:** Reportar solo la exactitud global. Se corrige con los ejercicios 5, 6 y 9.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, NDVI, clase, muestras de entrenamiento.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Exacto

- Una constante definitoria es una constante física a la que el SI asigna un valor numérico exacto; las unidades se definen fijándola (S2).
- Un valor exacto no tiene incertidumbre porque es una definición; un valor medido sí la tiene.

💡 **Cómo se explica en la clase [B13-C01](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md):**
- Según la página del BIPM sobre las constantes definitorias (S2) y la tabla CODATA 2022 (S1), los valores exactos son: `Δν_Cs = 9 192 631 770 Hz`, `c = 299 792 458 m/s`, `h = 6,626 070 15 × 10⁻³⁴ J s`, `e = 1,602 176 634 × 10⁻¹⁹ C`, `k = 1,380 649 × 10⁻²³ J/K`, `N_A = 6,022 140 76 × 10²³ mol⁻¹` y `K_cd = 683 lm/W`.
- Si el factor es exacto (`1 km = 10³ m`), el resultado conserva todas las cifras del dato.
- 🎯 **Por qué importa:** Una señal de radio o de láser viaja a la Luna y regresa. Para decir «la Luna está a 384 400 km» hay que haber acordado qué es un kilómetro, qué es un segundo y a qué velocidad viaja la señal.
- 🔗 **Se estudia junto con:** Sistema Internacional de Unidades (SI), unidad base, constante definitoria, magnitud.

📘 **Dónde se aprende** (1 clase): [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md).

### Excedente

- El excedente es `v(N) − Σ v(i)`.

💡 **Cómo se explica en la clase [B125-C04](../programa/clases/B125/B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md):**
- El socio C, que solo no vale nada, recibe `20` porque sin él el excedente cae: el reparto proporcional a lo individual lo dejaría sin nada.
- Definir una función de coalición `v(S)` y calcular el excedente de la alianza.
- 🎯 **Por qué importa:** Las empresas espaciales dependen de alianzas con socios de otros países y la clase de gobierno no explica cómo se reparte el valor ni cuánta dependencia se acepta; no está tratado. La decisión central: ¿cómo se reparte de forma justa el excedente de una alianza y cuánta dependencia de un solo socio o país es prudente?
- 🔗 **Se estudia junto con:** alianza, función de coalición, valor de Shapley, núcleo.

📘 **Dónde se aprende** (1 clase): [B125-C04 · Alianzas y cooperación internacional empresarial](../programa/clases/B125/B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md).

### Excedente público

- El excedente público es el pago del Estado por encima del seguro.

💡 **Cómo se explica en la clase [B127-C03](../programa/clases/B127/B127-C03-seguros-de-responsabilidad-civil-espacial/CLASE.md):**
- Un evento de `800 MUSD` se reparte `500` (seguro), `300` (excedente público) y `0` no cubierto.
- *Descripción textual:* el cuantil `1 − 10⁻⁷` define la MPL; el seguro exigido `S` es su mínimo con el tope de 500; la pérdida de un evento se reparte en seguro, excedente público y resto.
- ⚠️ **Error frecuente:** Tratar el excedente público como un derecho automático. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** La responsabilidad por daños a terceros se asegura aparte y ninguna clase la trataba. La decisión central: ¿cuánto seguro de terceros se exige y quién paga lo que lo supera?
- 🔗 **Se estudia junto con:** responsabilidad absoluta, responsabilidad por culpa, pérdida máxima probable, seguro exigido.

📘 **Dónde se aprende** (1 clase): [B127-C03 · Seguros de responsabilidad civil espacial](../programa/clases/B127/B127-C03-seguros-de-responsabilidad-civil-espacial/CLASE.md).

### Excéntrica

- La excéntrica `E` es el ángulo auxiliar sobre el círculo circunscrito.

💡 **Cómo se explica en la clase [B71-C13](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md):**
- En la órbita excéntrica, un cuarto de vuelta angular se recorre en solo el 3,8 % del período, y `M` correspondiente es `13.74°`.
- Límite: la pista elíptica no explica la anomalía excéntrica, que es una construcción geométrica.
- ⚠️ **Error frecuente:** Aplicar la serie de `e²` a órbitas muy excéntricas. Se corrige con 8.3.
- 🎯 **Por qué importa:** Confundir una anomalía con otra es el error más común al propagar órbitas. La decisión central: ¿cómo conviertes entre `ν`, `E` y `M` sin ambigüedad y cuánto difieren cuando `e` es grande?
- 🔗 **Se estudia junto con:** anomalía verdadera, media, ecuación del centro, movimiento medio.

📘 **Dónde se aprende** (1 clase): [B71-C13 · Anomalías orbitales](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md).

### Excentricidad

- La excentricidad `e` mide cuánto se aparta la órbita de un círculo (0 es círculo).
- La excentricidad `e` mide su achatamiento: la distancia entre focos es `2ae`.
- La excentricidad `e = c/a` mide cuánto se aleja la elipse de una circunferencia: `e = 0` es una circunferencia y `e` cercano a 1 es una elipse muy alargada.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C13](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md):**
- La ficha de planetas de NASA (actualizada el 18 de marzo de 2025) tabula masa, diámetro, densidad, período orbital, distancia al Sol, excentricidad y número de lunas para los ocho planetas y Plutón (S1).
- 🎯 **Por qué importa:** Se dice que el sistema solar «está vacío», y es verdad en un sentido preciso: si el Sol midiera 9 mm, la Tierra sería un grano de 0,085 mm a un metro de distancia, y la estrella más cercana quedaría a más de 260 km. Pero esa imagen solo se entiende si la construyes tú con números.
- 🔗 **Se estudia junto con:** sistema solar, semieje mayor, período orbital, tercera ley de Kepler.

📖 **Explicado a fondo:** [Excentricidad](esencial/esencial-d-l.md#excentricidad) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (9 clases): [B01-C13 · Sistema solar como sistema físico](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md); [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B26-C08 · Geodésicas gravitacionales](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md) y 3 más.

### Excentricidad congelada

- La excentricidad congelada `e_f` cumple `ω̇_J2 + ω̇_J3 = 0`.

💡 **Cómo se explica en la clase [B72-C14](../programa/clases/B72/B72-C14-orbitas-congeladas/CLASE.md):**
- A `700 km` y `98,188°` (heliosíncrona), la excentricidad congelada con `ω = 90°` vale `0,001046`, y la raíz numérica de las ecuaciones de Gauss con J2 y J3 coincide (`0,00 %` en cuatro cifras).
- Descripción larga: La excentricidad congelada es del orden de 10⁻³ y depende de la razón J3/(2 J2); el efecto de J3 invierte el signo del giro del perigeo para excentricidades mayores que la congelada.
- 🎯 **Por qué importa:** Un altímetro o un radar que observa la misma traza necesita pasar por cada latitud a la misma altitud; si el perigeo girara, la altitud sobre un punto cambiaría decenas de kilómetros. La decisión central: ¿qué excentricidad y argumento del perigeo congelan la órbita para una inclinación y altitud dadas?
- 🔗 **Se estudia junto con:** órbita congelada, efecto de J3, promedio de Gauss.

📘 **Dónde se aprende** (1 clase): [B72-C14 · Órbitas congeladas](../programa/clases/B72/B72-C14-orbitas-congeladas/CLASE.md).

### Excentricidad forzada

- La excentricidad forzada es el vector de excentricidad que crece por una fuerza casi constante.

💡 **Cómo se explica en la clase [B72-C08](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md):**
- La aceleración es `10⁻⁸`–`10⁻⁶ m/s²`, minúscula frente a `0,22 m/s²` de la gravedad en GEO, pero sin freno acumula el desplazamiento: en un año la excentricidad forzada sin compensación llegaría a décimas de milésima por mes.
- Ejercicio 8 · autónomo. ¿Por qué la excentricidad forzada no crece indefinidamente en la realidad?
- 🎯 **Por qué importa:** En órbita geoestacionaria no hay arrastre, y el empuje solar domina las maniobras de mantenimiento de un satélite con paneles grandes; en una vela solar es el propulsor. La decisión central: ¿cuánto vale la aceleración por presión de radiación y cuánto deforma una órbita alta en semanas?
- 🔗 **Se estudia junto con:** irradiancia, presión de radiación, coeficiente de reflectividad, sombra cilíndrica.

📘 **Dónde se aprende** (1 clase): [B72-C08 · Presión de radiación solar](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md).

### Excentricidad hiperbólica

- La excentricidad hiperbólica es `e = 1 + r v_inf²/GM_L`.

💡 **Cómo se explica en la clase [B76-C07](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md):**
- Obtener la velocidad de llegada relativa a la Luna `v_inf` y la excentricidad hiperbólica.
- Llegada: v_inf = 0.8378 km/s ; excentricidad hiperbolica = 1.2630
- 🎯 **Por qué importa:** Un diseño preliminar de misión empieza por el presupuesto de velocidad. La decisión central: ¿cuánto `Δv` cuestan la salida de la Tierra y la captura en la Luna, y cuánto cambia la segunda según la órbita lunar elegida?
- 🔗 **Se estudia junto con:** inyección translunar (TLI), inserción en órbita lunar (LOI), velocidad de llegada, fracción de propergol.

📘 **Dónde se aprende** (1 clase): [B76-C07 · Maniobras de inserción cislunar](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md).

### Excéntrico

- Un excéntrico y un epiciclo son dos recursos geométricos para describir el movimiento de un cuerpo (C10).

💡 **Contexto en la clase [B02-C03](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md):**
- **Idea central (modelo mental):** Si el Sol está tan lejos que sus rayos llegan paralelos, la diferencia entre el ángulo que forman los rayos con la vertical en dos ciudades es igual al ángulo que separa esas ciudades visto desde el centro de la Tierra.
- 🎯 **Por qué importa:** Un modelo geométrico responde a «¿qué figura reproduce estos movimientos?». Es una forma nueva de preguntar frente a la regla puramente numérica.
- 🔗 **Se estudia junto con:** circunferencia, estadio, meridiano, precesión de los equinoccios.

📘 **Dónde se aprende** (1 clase): [B02-C03 · Astronomía griega y helenística](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md).

### Excepción

- Un error de sintaxis ocurre cuando el código no es Python válido, antes de ejecutarse; una excepción ocurre durante la ejecución y puede tratarse (S2, §8.1–8.2).

💡 **Cómo se explica en la clase [B07-C12](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md):**
- Los nombres de las excepciones estándar no son palabras reservadas (S2).
- Una excepción es una alarma que sube por la pila de llamadas hasta que alguien la atiende.
- 🎯 **Por qué importa:** Un programa científico recibe archivos con huecos, texto donde esperaba un número y valores imposibles (un período negativo). Hay dos malas respuestas: dejar que el programa se caiga sin explicar nada y, peor, seguir en silencio con un valor inválido (`nan`, `0`) que contamina el resultado final.
- 🔗 **Se estudia junto con:** error de sintaxis, traza, excepción propia, Validar.

📘 **Dónde se aprende** (1 clase): [B07-C12 · Manejo de errores y excepciones](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md).

### Excepción propia

- Una excepción propia es una clase que heredas de otra (aquí `DatoInvalido(ValueError)`).

💡 **Cómo se explica en la clase [B07-C12](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md):**
- Lanzar `ValueError` u otra excepción propia con un mensaje útil.
- 🎯 **Por qué importa:** Un programa científico recibe archivos con huecos, texto donde esperaba un número y valores imposibles (un período negativo). Hay dos malas respuestas: dejar que el programa se caiga sin explicar nada y, peor, seguir en silencio con un valor inválido (`nan`, `0`) que contamina el resultado final.
- 🔗 **Se estudia junto con:** error de sintaxis, excepción, traza, Validar.

📘 **Dónde se aprende** (1 clase): [B07-C12 · Manejo de errores y excepciones](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md).

### Exceso

- Un exceso es la diferencia entre lo observado y `b`.

💡 **Cómo se explica en la clase [B31-C16](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md):**
- *Descripción textual:* el campo y el tamaño fijan la energía máxima; el decaimiento del pion da la fracción del neutrino; el flujo y el área dan el número de eventos y la probabilidad de un exceso.
- 🎯 **Por qué importa:** Para decir si una fuente puede producir rayos cósmicos de cierta energía y cuántos neutrinos habría, se necesitan estimaciones cuantitativas. La decisión central: ¿hasta qué energía acelera una fuente y cuántos eventos se esperan?
- 🔗 **Se estudia junto con:** criterio de Hillas, energía del neutrino, área efectiva, flujo.

📘 **Dónde se aprende** (1 clase): [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md).

### Exceso angular

- El exceso angular de un triángulo es la suma de sus ángulos menos `π`, y vale `K A`, con `A` el área.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- Medir la curvatura de una esfera con el exceso angular de un triángulo.
- Ejercicio 4. ¿Cuánto vale el exceso angular del octante?
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.
- 🔗 **Se estudia junto con:** métrica, distancia propia, curvatura gaussiana, métrica de Schwarzschild.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### Exceso de energía

- La falta de fusión ocurre con `E_v` bajo y el exceso de energía (ojo de cerradura) con `E_v` alto.

💡 **Cómo se explica en la clase [B84-C15](../programa/clases/B84/B84-C15-manufactura-aditiva/CLASE.md):**
- Exceso de energía y poros de ojo de cerradura; baja `P` o sube `v`.
- 🎯 **Por qué importa:** Dos piezas idénticas con otra velocidad de barrido pueden salir porosas; una ventana de proceso bien trazada evita el desperdicio, y la rugosidad escalonada decide qué superficies se mecanizan. La decisión central: ¿con qué potencia y velocidad se imprime dentro de la ventana y cuánto tarda y qué acabado deja?
- 🔗 **Se estudia junto con:** densidad de energía volumétrica, falta de fusión, efecto escalera, separación entre pasadas.

📘 **Dónde se aprende** (1 clase): [B84-C15 · Manufactura aditiva](../programa/clases/B84/B84-C15-manufactura-aditiva/CLASE.md).

### Exceso de pérdida

- El exceso de pérdida (*per risk*) paga por siniestro `min(max(X − P, 0), L)`, con prioridad `P` y límite `L`.

💡 **Cómo se explica en la clase [B127-C07](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md):**
- La cuota parte lo hace barato porque la comisión es generosa (dato sintético); el exceso de pérdida lo hace caro pero solo protege contra siniestros grandes, como los que dominan este tipo de cartera, y deja intacta la frecuencia de los pequeños.
- X --> E["exceso de pérdida: paga min(max(X - P, 0), L)"]
- 🎯 **Por qué importa:** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?
- 🔗 **Se estudia junto con:** cesión, cuota parte, prioridad, límite.

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Exceso de velocidad hiperbólica

- El exceso de velocidad hiperbólica `v∞` es la velocidad lejos del cuerpo.

💡 **Contexto en la clase [B71-C09](../programa/clases/B71/B71-C09-orbitas-parabolicas-e-hiperbolicas/CLASE.md):**
- 🎯 **Por qué importa:** Las trayectorias de escape y de sobrevuelo son hipérbolas respecto del cuerpo local. La decisión central: ¿qué velocidad en el periapsis produce un exceso `v∞` dado y cuánto se desvía la trayectoria?
- 🔗 **Se estudia junto con:** energía característica, excentricidad, ángulo de giro, parámetro de impacto.

📘 **Dónde se aprende** (1 clase): [B71-C09 · Órbitas parabólicas e hiperbólicas](../programa/clases/B71/B71-C09-orbitas-parabolicas-e-hiperbolicas/CLASE.md).

### Exceso enantiomérico

- El exceso enantiomérico es `ee = (L−D)/(L+D)`.

💡 **Cómo se explica en la clase [B55-C17](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md):**
- *Descripción textual:* la tasa y el tiempo dan la dosis, de la que sale la supervivencia; en paralelo, el número de moléculas contadas fija la incertidumbre del exceso enantiomérico.
- Un aminoácido hipotético con dosis característica `D₀ = 10⁶ Gy` y tasa de dosis de `10⁻³ Gy/año` (ambas ilustrativas), y una proporción verdadera de forma L de 0,55 (exceso enantiomérico 0,10).
- 🎯 **Por qué importa:** Que un compuesto prebiótico llegue intacto hasta nosotros depende de cuánta radiación recibió, y que un exceso entre dos formas quirales sea real depende de cuántas moléculas se contaron. La decisión central: ¿cuánto sobrevive y con qué incertidumbre puedo afirmar un exceso enantiomérico distinto de cero?
- 🔗 **Se estudia junto con:** radiólisis, dosis característica, desviación del conteo, distinguible de cero.

📘 **Dónde se aprende** (1 clase): [B55-C17 · Compuestos prebióticos](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md).

### Exceso hiperbólico

- El exceso hiperbólico `v∞` es lo que sobra tras escapar.
- El exceso hiperbólico `v∞` es la velocidad respecto a la Tierra lejos de ella.

💡 **Cómo se explica en la clase [B75-C23](../programa/clases/B75/B75-C23-energia-caracteristica-c3-y-exceso-hiperbolico/CLASE.md):**
- python programa/clases/B75/B75-C23-energia-caracteristica-c3-y-exceso-hiperbolico/c3.py
- 🎯 **Por qué importa:** Un lanzador entrega una masa distinta según la energía que se le pida. La decisión central: ¿cuánta energía característica y cuánto delta-v hay que dar desde una órbita baja para alcanzar un destino?
- 🔗 **Se estudia junto con:** energía característica, delta-v de salida, capacidad de un lanzador.

📘 **Dónde se aprende** (2 clases): [B71-C15 · Velocidad de escape](../programa/clases/B71/B71-C15-velocidad-de-escape/CLASE.md); [B75-C23 · Energía característica C3 y exceso hiperbólico](../programa/clases/B75/B75-C23-energia-caracteristica-c3-y-exceso-hiperbolico/CLASE.md).

### Exceso hiperbólico de velocidad

- El exceso hiperbólico de velocidad `v∞` es la velocidad de la nave respecto al planeta, lejos de él: aquí, la diferencia entre la velocidad heliocéntrica de la nave y la del planeta.

💡 **Cómo se explica en la clase [B75-C01](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md):**
- *Descripción textual:* Los dos radios dan el semieje de la transferencia; del semieje salen las velocidades en los extremos (vis-viva) y el tiempo de vuelo; la diferencia con las velocidades circulares da los excesos hiperbólicos.
- Obtener los excesos hiperbólicos de salida y de llegada (`v∞`) como diferencia con la velocidad circular del planeta.
- 🎯 **Por qué importa:** Para ir a Marte no se apunta a donde está Marte: se elige una elipse alrededor del Sol que toque la órbita de la Tierra al salir y la de Marte al llegar. La decisión central: ¿cuál es la elipse de menor energía que une dos órbitas circulares, cuánto dura el viaje y qué velocidad exige a la salida y a la llegada?
- 🔗 **Se estudia junto con:** elipse de transferencia de Hohmann, perihelio, afelio, tiempo de vuelo.

📘 **Dónde se aprende** (1 clase): [B75-C01 · Geometría de transferencias heliocéntricas](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md).

### Exclusión

- La exclusión deja sin pago un evento.

💡 **Cómo se explica en la clase [B127-C04](../programa/clases/B127/B127-C04-exclusiones-deducibles-y-limites-de-polizas/CLASE.md):**
- La exclusión y el coaseguro actúan multiplicando: `0,9 × 0,8 = 0,72` sobre el pago de C.
- *Descripción textual:* una pérdida primero se comprueba contra las exclusiones; si no está excluida, se resta el deducible, se topa en el límite y se multiplica por la fracción coasegurada.
- 🎯 **Por qué importa:** Leer una póliza exige entender sus exclusiones, deducibles y límites; el catálogo no lo trataba. La decisión central: ¿qué parte de la pérdida retiene el asegurado y cómo cambia el precio al cambiar las condiciones?
- 🔗 **Se estudia junto con:** deducible, límite, coaseguro, valor esperado limitado.

📘 **Dónde se aprende** (1 clase): [B127-C04 · Exclusiones, deducibles y límites de pólizas](../programa/clases/B127/B127-C04-exclusiones-deducibles-y-limites-de-polizas/CLASE.md).

### Exclusiva

- La licencia exclusiva se da a un solo licenciatario; la no exclusiva, a varios.

💡 **Cómo se explica en la clase [B124-C09](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md):**
- Exclusiva: un licenciatario con ventas 1,6 veces mayores, regalía de 6 % y cuota de 5 Mum, vale `45,997` Mum para el licenciante.
- No exclusiva: tres licenciatarios, regalía de 4 % y cuota de 1 Mum cada uno, valen `54,247` Mum.
- ⚠️ **Error frecuente:** Suponer que la exclusiva siempre vale más. Se corrige con 8.3–8.4.
- 🎯 **Por qué importa:** La propiedad intelectual es un activo, pero su valor depende de cuánto se vende con ella y de cuánto del margen se queda el que la usa. La decisión central: ¿qué licencia conviene ofrecer y cuántas regalías soporta el licenciatario?
- 🔗 **Se estudia junto con:** licencia, cuota inicial, regalía, valor actual.

📘 **Dónde se aprende** (1 clase): [B124-C09 · Propiedad intelectual y licencias](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md).

### Exhaustiva

- La exhaustiva requiere `2ⁿ`.

💡 **Cómo se explica en la clase [B88-C39](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md):**
- Descripción larga: MC/DC cuesta el doble de la cobertura de decisión y la mitad de la exhaustiva en este caso.
- Cobertura de condiciones exhaustiva (todas las combinaciones) = 8 pruebas ;
- 🎯 **Por qué importa:** Elegir el nivel de cobertura determina el esfuerzo de prueba. La decisión central: ¿qué cobertura piden los distintos niveles y cuánto cuesta cada una en pruebas?
- 🔗 **Se estudia junto con:** cobertura de decisión, MC/DC, tamaño mínimo.

📘 **Dónde se aprende** (1 clase): [B88-C39 · Normas de aseguramiento de software (ECSS, DO-178C)](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md).

### Exhaustividad

- La exhaustividad (*recall*, sensibilidad, tasa de verdaderos positivos) es `TP/(TP + FN)`: de los reales, cuántos se encontraron (S2).
- La exactitud es `(TP + TN)/total`; la precisión, `TP/(TP + FP)`; la exhaustividad (*recall*), `TP/(TP + FN)`; el F1, la media armónica de las dos últimas.
- La precisión es `TP/(TP + FP)`, la exhaustividad `TP/(TP + FN)` y `F1 = 2PR/(P + R)`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Precisión `3/(3 + 1) = 0,75`; exhaustividad `3/(3 + 2) = 0,6`;
- Con `β = 2` (más peso a la exhaustividad): `F₂ = 5(0,75)(0,6)/(4 × 0,75 + 0,6) = 2,25/3,6 = 0,625`; con `β = 0,5`: `F₀,₅ = 1,25 × 0,45/(0,25 × 0,75 + 0,6) = 0,714`.
- ⚠️ **Error frecuente:** Confiar en el AUC sin mirar precisión–exhaustividad. Ejercicio 5.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.
- 🔗 **Se estudia junto con:** matriz de confusión, verdaderos positivos, falsos positivos, verdaderos negativos.

📘 **Dónde se aprende** (5 clases): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md); [B104-C03 · Selección y aptitud](../programa/clases/B104/B104-C03-seleccion-y-aptitud/CLASE.md); [B119-C07 · Registro nacional de objetos](../programa/clases/B119/B119-C07-registro-nacional-de-objetos/CLASE.md).

### Existencias de seguridad

- Las existencias de seguridad cubren la variación.

💡 **Cómo se explica en la clase [B104-C21](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md):**
- Calcular el punto de reorden con existencias de seguridad `μL + zσ√L`.
- 🎯 **Por qué importa:** Quedarse sin un consumible a bordo no se arregla enviando a alguien a comprarlo. La decisión central: ¿con qué punto de reorden se pide para que el faltante sea raro, y cuánto volumen cuesta guardar lo pedido?
- 🔗 **Se estudia junto con:** punto de reorden, plazo de entrega, estiba, empaquetado en bolsas.

📘 **Dónde se aprende** (1 clase): [B104-C21 · Inventario, logística y estiba a bordo](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md).

### Exitancia

- La exitancia `M` es la potencia emitida por área (`π B` si es lambertiana).

💡 **Cómo se explica en la clase [B45-C01](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md):**
- Con `x = hc/(λkT)`, la exitancia es `2π k⁴T⁴/(h³c²) ∫ x³/(eˣ − 1) dx`.
- Como el agua: la radiancia es el chorro por unidad de sección y ángulo; la exitancia, el caudal total del grifo por área; la irradiancia, lo que cae sobre una hoja de papel a cierta distancia.
- ⚠️ **Error frecuente:** Olvidar el factor `π` entre radiancia y exitancia. Se corrige con 8.2.
- 🎯 **Por qué importa:** Todo flujo medido en un telescopio es una cantidad radiométrica o fotométrica con una definición precisa; confundir vatios, lúmenes y fotones arruina la calibración. La decisión central: ¿en qué unidades se expresa lo que llega al detector y cómo se pasa de una a otra?
- 🔗 **Se estudia junto con:** radiancia, irradiancia, flujo luminoso, fotón.

📘 **Dónde se aprende** (1 clase): [B45-C01 · Radiometría y fotometría](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md).

### Exitancia espectral

- La exitancia espectral de Planck es `M_λ = 2πhc²/(λ⁵(e^(hc/λkT) − 1))`.

💡 **Cómo se explica en la clase [B85-C04](../programa/clases/B85/B85-C04-radiacion-termica-de-superficies/CLASE.md):**
- Calcular la exitancia espectral de Planck y localizar su máximo con la ley de Wien.
- 🎯 **Por qué importa:** La mitad del control térmico es elegir cuánto emite o absorbe cada superficie. La decisión central: ¿cuánto calor intercambian dos superficies y cómo lo cambia poner una emisividad baja entre ellas?
- 🔗 **Se estudia junto con:** ley de Wien, emisividad, intercambio entre placas paralelas, cavidad.

📘 **Dónde se aprende** (1 clase): [B85-C04 · Radiación térmica de superficies](../programa/clases/B85/B85-C04-radiacion-termica-de-superficies/CLASE.md).

### Éxito

- El éxito es un mejor valor menor que `10⁻³`.
- El éxito exige residuo relativo `< 10⁻⁸`.

💡 **Cómo se explica en la clase [B81-C13](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md):**
- G --> R["éxitos y evaluaciones en 30 semillas"]
- *Descripción textual:* la misma función se resuelve con tres métodos, cada uno repetido con 30 semillas; se comparan la tasa de éxito y las evaluaciones.
- 🎯 **Por qué importa:** Un método heurístico no garantiza el óptimo, pero puede evitar los mínimos locales. La decisión central: ¿qué método global elegir y cuántas evaluaciones se gastan para una tasa de éxito dada?
- 🔗 **Se estudia junto con:** algoritmo genético, enjambre de partículas, arranque múltiple.

📘 **Dónde se aprende** (2 clases): [B81-C13 · Optimización heurística (algoritmos genéticos y enjambres)](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md); [B82-C07 · Benchmark entre solucionadores de Lambert](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md).

### Éxito de la maniobra

- Recalibración: actualizar los parámetros del gemelo. Éxito de la maniobra: error menor que el umbral.

💡 **Contexto en la clase [B101-C08](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md):**
- 🎯 **Por qué importa:** Una reparación robótica no se improvisa: se ensaya. Pero un ensayo vale solo si el gemelo se parece a la realidad.
- 🔗 **Se estudia junto con:** Gemelo digital, Realidad sintética, Discrepancia, Recalibración.

📘 **Dónde se aprende** (1 clase): [B101-C08 · Gemelo digital para ensayo de reparaciones robóticas](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md).

### Exobase

- El exobase es la altura sobre la cual las colisiones son raras.
- La exobase es la altura sobre la cual las colisiones son raras.

💡 **Cómo se explica en la clase [B54-C11](../programa/clases/B54/B54-C11-escape-atmosferico/CLASE.md):**
- Límite: los corredores no chocan entre sí; las moléculas del exobase casi no lo hacen, pero la atmósfera debajo sí.
- Temperaturas de exobase sintéticas: 1000 K para la Tierra y 200 K para Marte y Venus.
- ⚠️ **Error frecuente:** Usar el radio de la superficie como si fuera el del exobase. Se corrige con la sección 10: es una aproximación declarada.
- 🎯 **Por qué importa:** Por qué la Tierra retiene el N₂ pero pierde el H depende de una razón entre energías. La pregunta motivadora: ¿qué especies puede retener un planeta a cierta temperatura?
- 🔗 **Se estudia junto con:** velocidad de escape, parámetro de Jeans, escape de Jeans, velocidad térmica más probable.

📘 **Dónde se aprende** (2 clases): [B54-C11 · Escape atmosférico](../programa/clases/B54/B54-C11-escape-atmosferico/CLASE.md); [B56-C11 · Atmósfera y superficie de Titán](../programa/clases/B56/B56-C11-atmosfera-y-superficie-de-titan/CLASE.md).

### Exotérmico

- En modo endotérmico (`V < E_tn`) la celda absorbe calor; en exotérmico (`V > E_tn`) lo cede.

💡 **Cómo se explica en la clase [B59-C10](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md):**
- Distinguir los modos endotérmico y exotérmico.
- 🎯 **Por qué importa:** La electrólisis es el mayor consumidor de energía de la planta. La decisión central: ¿a qué densidad de corriente conviene operar, entre una celda pequeña que gasta más electricidad y una grande que gasta menos?
- 🔗 **Se estudia junto con:** tensión termoneutra, modo endotérmico, curva de polarización, eficiencia farádica.

📘 **Dónde se aprende** (1 clase): [B59-C10 · Electrólisis y balances energéticos](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md).

### Expandida

- La incertidumbre combinada es la raíz de la suma cuadrática de los términos independientes; la expandida la multiplica por un factor de cobertura `k` (aquí 2).

💡 **Cómo se explica en la clase [B91-C05](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md):**
- Construir un presupuesto de incertidumbre combinada y expandida.
- incertidumbre tipica combinada = 0.274 dB ; expandida (k = 2) = 0.548 dB
- ⚠️ **Error frecuente:** Confundir incertidumbre combinada con expandida. Ver la sección 6.
- 🎯 **Por qué importa:** Una antena se acepta si su ganancia y su patrón medidos cumplen la especificación dentro de una incertidumbre conocida. La decisión central: ¿a qué distancia medir y con qué incertidumbre, para poder afirmar que la antena cumple?
- 🔗 **Se estudia junto con:** distancia de campo lejano, error de fase en el borde, transferencia de ganancia, incertidumbre combinada.

📘 **Dónde se aprende** (1 clase): [B91-C05 · Medición y calibración de antenas](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md).

### Expansión

- La expansión del universo es el aumento de las distancias entre galaxias no ligadas.
- La expansión produce `n` bytes con `T(i) = HMAC(PRK, T(i−1) ‖ info ‖ i)`.

💡 **Cómo se explica en la clase [B01-C16](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md):**
- Explicar por qué una expansión uniforme no tiene centro.
- Observamos −100: la velocidad peculiar domina, la galaxia está ligada a un grupo y no sigue la expansión (C01, C15).
- 🎯 **Por qué importa:** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).
- 🔗 **Se estudia junto con:** constante de Hubble, ley de Hubble, tiempo de Hubble, velocidad peculiar.

📘 **Dónde se aprende** (2 clases): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md); [B88-C38 · Gestión de claves y secretos en aviónica](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md).

### Expansión de Prandtl–Meyer

- Una expansión de Prandtl–Meyer es el giro continuo de un flujo supersónico alrededor de una esquina convexa.

💡 **Cómo se explica en la clase [B79-C06](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md):**
- La expansión de Prandtl–Meyer es isentrópica: no hay pérdida de presión total, a diferencia del choque (C07).
- Calcular la función de Prandtl–Meyer y el Mach tras una expansión.
- 🎯 **Por qué importa:** El comportamiento de un flujo a `M > 1` en toberas y vehículos no lo trata ninguna clase del tronco. Sin él no se entiende por qué una tobera necesita una parte divergente.
- 🔗 **Se estudia junto con:** relación área–Mach, ángulo de Mach, función de Prandtl–Meyer.

📘 **Dónde se aprende** (1 clase): [B79-C06 · Flujos supersónicos](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md).

### Expansión por cofactores

- El determinante de `[[a, b], [c, d]]` es `ad − bc`; el de una matriz `3×3` se obtiene por expansión por cofactores: se desarrolla por una fila sumando cada elemento por el determinante de la submatriz que queda al tachar su fila y columna, con signo alterno (S1, §1.3(i), ecs. 1.3.1–1.3.4).

💡 **Cómo se explica en la clase [B10-C04](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md):**
- Calcular determinantes `2×2` y `3×3` por expansión en cofactores.
- 🎯 **Por qué importa:** Dos estaciones terrestres miden la dirección hacia un mismo objeto y quieren fijar su posición cruzando las visuales. Si el objeto está cerca y las visuales forman un buen ángulo, el cruce es nítido.
- 🔗 **Se estudia junto con:** determinante, menor, singular, regular.

📘 **Dónde se aprende** (1 clase): [B10-C04 · Determinantes y soluciones](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md).

### Expectativa de gas uniforme

- La expectativa de gas uniforme estima los pares por razón de volúmenes.

💡 **Cómo se explica en la clase [B118-C15](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md):**
- *Descripción textual:* se genera la constelación, se cuentan los pares cercanos en varias instantáneas y se comparan con la expectativa de un gas uniforme; por separado se estima el crecimiento de pares a cribar.
- Comparar con la expectativa de un gas uniforme en la capa (10,9; cociente 1,44).
- 🎯 **Por qué importa:** La sección 5.5 de la IADC Rev. 4 pide planificar y operar las constelaciones para minimizar la probabilidad de colisión entre sus miembros, en los cruces de planos y con otras constelaciones, y minimizar el riesgo acumulado de reentradas.
- 🔗 **Se estudia junto con:** constelación, Walker-delta, cruce de planos, par cercano.

📘 **Dónde se aprende** (1 clase): [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md).

### Expediente

- El expediente es el conjunto de documentos y datos de un trámite.

💡 **Cómo se explica en la clase [B120-C04](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md):**
- El expediente base tiene 0 faltantes (100 %).
- *Descripción textual:* el expediente se compara con el esquema (completitud) y consigo mismo (coherencia); la mutación prueba al verificador.
- 🎯 **Por qué importa:** El expediente regulatorio es un entregable del rol; B90-C05 documenta interfaces, no trámites regulatorios.
- 🔗 **Se estudia junto con:** completitud, coherencia, esquema, diligencia debida.

📘 **Dónde se aprende** (1 clase): [B120-C04 · Documentación regulatoria de un sistema satelital](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md).

### Experimento aleatorio

- Un experimento aleatorio es un proceso cuyo resultado no se puede predecir con certeza aunque se conozcan sus condiciones.

💡 **Contexto en la clase [B12-C01](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md):**
- **Idea central (modelo mental):** Imagina una caja con todas las historias posibles de la misión; cada historia tiene un peso, y los pesos suman 1. Un evento es una etiqueta que pones a un grupo de historias; su probabilidad es la suma de los pesos de ese grupo.
- 🎯 **Por qué importa:** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.
- 🔗 **Se estudia junto con:** espacio muestral, evento, probabilidad, complemento.

📘 **Dónde se aprende** (1 clase): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md).

### Explicabilidad

- Aporte: `log₁₀` de la razón de verosimilitud de un síntoma. Explicabilidad: capacidad de justificar una conclusión.

💡 **Contexto en la clase [B96-C21](../programa/clases/B96/B96-C21-diagnostico-explicable-de-anomalias/CLASE.md):**
- 🎯 **Por qué importa:** C13 detecta que algo anda mal; esta clase responde por qué la máquina cree lo que cree. La decisión central: ¿qué hipótesis es la más probable y qué evidencia la sostiene, de modo que un operador pueda aceptarla o refutarla?
- 🔗 **Se estudia junto con:** Hipótesis, Síntoma, Prior, Posterior.

📘 **Dónde se aprende** (1 clase): [B96-C21 · Diagnóstico explicable de anomalías](../programa/clases/B96/B96-C21-diagnostico-explicable-de-anomalias/CLASE.md).

### Explícita

- Una relación explícita da `y` en función de `x`; una implícita la define mediante `F(x, y) = 0` (S1, §1.5(i)).

💡 **Contexto en la clase [B09-C06](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md):**
- **Idea central (modelo mental):** El tiempo `t` fija `M`; `M` fija `E` (por la ecuación de Kepler); `E` fija la posición.
- 🎯 **Por qué importa:** Para saber dónde está un planeta en su órbita en un instante dado hay que resolver la ecuación de Kepler, `M = E − e sin E`, que no tiene solución en funciones elementales: no se puede despejar `E`.
- 🔗 **Se estudia junto con:** implícita, derivación implícita, tasa relacionada, anomalía media.

📘 **Dónde se aprende** (1 clase): [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md).

### Explícito

- Un método explícito calcula el nuevo estado solo con valores ya conocidos.

💡 **Contexto en la clase [B11-C06](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md):**
- **Idea central (modelo mental):** Euler decide con la pendiente del punto de partida. Heun se asoma al punto de llegada estimado, mide la pendiente allí y avanza con el promedio de las dos. Es como ajustar el rumbo a medio tramo.
- 🎯 **Por qué importa:** Una evaluación de `F` en un cálculo de trayectorias es cara cuando incluye gravedad de varios cuerpos o un modelo de atmósfera. La pregunta práctica es siempre cuánta precisión compra cada evaluación.
- 🔗 **Se estudia junto con:** método de Heun, predictor, corrector, pendiente.

📘 **Dónde se aprende** (1 clase): [B11-C06 · Método de Heun](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md).

### Exploratorio

- Un análisis confirmatorio sigue el plan; uno exploratorio no.
- El análisis confirmatorio prueba lo especificado antes; el exploratorio busca patrones sin plan previo (S1).

💡 **Cómo se explica en la clase [B14-C23](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md):**
- No prohíbe lo exploratorio (S1): permite explorar si se etiqueta.
- E --> X["Resultado exploratorio<br/>declarado como tal"]
- ⚠️ **Error frecuente:** Ocultar lo exploratorio. Se corrige con los ejercicios 3 y 10.
- 🎯 **Por qué importa:** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.
- 🔗 **Se estudia junto con:** protocolo preregistrado, confirmatorio, desviación, falso positivo.

📘 **Dónde se aprende** (2 clases): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md).

### Exponencial

- El modelo exponencial es `BMD(t) = BMD₀ (1 − r)^t` y el lineal `BMD₀ (1 − r t)`, con `t` en meses.

💡 **Cómo se explica en la clase [B105-C02](../programa/clases/B105/B105-C02-perdida-de-masa-osea/CLASE.md):**
- El exponencial da menos pérdida acumulada que el lineal porque cada mes se pierde una fracción del saldo restante; a 12 meses la diferencia es 0,99 puntos con `r = 1,25 %`.
- R --> M["modelo exponencial<br/>o lineal"]
- 🎯 **Por qué importa:** Un porcentaje por mes parece simple, pero hay que decidir cómo se acumula (lineal o exponencial), para quién vale (promedio o individuo) y qué recupera el cuerpo al volver. La decisión central: ¿qué pérdida esperar a 6 y 12 meses, con qué dispersión y qué parte se recupera?
- 🔗 **Se estudia junto con:** densidad mineral ósea, lineal, semivida de recuperación, desviación estándar.

📘 **Dónde se aprende** (1 clase): [B105-C02 · Pérdida de masa ósea](../programa/clases/B105/B105-C02-perdida-de-masa-osea/CLASE.md).

### Exponencial matricial

- La exponencial matricial es `exp(A t) = Σ (A t)ᵏ/k!`; si `A = V Λ V⁻¹`, entonces `exp(A t) = V exp(Λ t) V⁻¹`.
- La exponencial matricial `e^(At)` se define con la serie `I + At + (At)²/2! + …`.

💡 **Cómo se explica en la clase [B16-C02](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md):**
- Porque las dimensiones crecen y las mismas rutinas (exponencial matricial, simulación, análisis) siguen valiendo con matrices más grandes; con ecuaciones sueltas habría que rehacer el análisis a mano.
- 🎯 **Por qué importa:** El computador de a bordo de un satélite no maneja ecuaciones sueltas: maneja vectores y matrices, y una sola rutina sirve para cualquier eje, rueda o sensor que se le añada.
- 🔗 **Se estudia junto con:** representación en espacio de estados, matriz de transición, retenedor de orden cero, transformación de semejanza.

📘 **Dónde se aprende** (2 clases): [B10-C09 · Diagonalización y estabilidad](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md); [B16-C02 · Representaciones en espacio de estados](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md).

### Exponente

- `a` es la base y `n` el exponente.
- La mantisa `m` cumple `1 ≤ |m| < 10` en la forma normalizada; el exponente `e` es un entero.
- El exponente es `β = (1/m₁₆ − 1/m₁₇)/(1/m₁₆ − 1/m₁₈)`.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Con exponente fraccionario (`a1.5`) es directo y cabe en una línea.
- Ninguno es mejor siempre: para ver el principio, descompone; para calcular muchos casos, usa el exponente.
- ⚠️ **Error frecuente:** Multiplicar la base por el exponente (`2⁵ = 10`).
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.
- 🔗 **Se estudia junto con:** potencia, base, cuadrado, cubo.

📘 **Dónde se aprende** (3 clases): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md); [B03-C05 · Notación científica y órdenes de magnitud](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md); [B55-C13 · Isótopos como trazadores](../programa/clases/B55/B55-C13-isotopos-como-trazadores/CLASE.md).

### Exponente de acoplamiento

- `π₂ = g a/U²` es el grupo adimensional de gravedad. μ es el exponente de acoplamiento entre energía y momento.

💡 **Contexto en la clase [B61-C01](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md):**
- **Idea central (modelo mental):** Un esquema del flujo de cálculo de la clase; el texto equivalente está debajo.
- 🎯 **Por qué importa:** Para leer un cráter hay que invertir la pregunta: del tamaño observado al proyectil. Sin las leyes de escalado no hay estimación de energía ni de la cantidad de material que sale despedido.
- 🔗 **Se estudia junto con:** cráter transitorio, régimen de gravedad, resistencia, grupo adimensional de gravedad.

📘 **Dónde se aprende** (1 clase): [B61-C01 · Dinámica de eyección y escalado de cráteres](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md).

### Exponente de Ångström

- El exponente de Ångström `α` ajusta `τ ∝ λ^{−α}`; valores altos indican partículas pequeñas.

💡 **Cómo se explica en la clase [B57-C13](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md):**
- *Descripción textual:* el espesor óptico determina la transmitancia, el exponente de Ångström y, cuando es pequeño, la reflectancia dispersada, mientras el ruido de medición se propaga al exponente.
- Una columna de aire con `AOD(550 nm) = 0,30` y exponente de Ångström `1,3` (ambos ilustrativos) se mide en `440` y `870 nm` con un ruido de `0,01`.
- 🎯 **Por qué importa:** Un satélite que mira un incendio, un volcán o el mar tiene que descontar la atmósfera, y los aerosoles son lo más variable. La decisión central: ¿cuánto aerosol hay y qué tipo, con qué incertidumbre, a partir de pocas longitudes de onda?
- 🔗 **Se estudia junto con:** espesor óptico de aerosoles, ley de Beer–Lambert, albedo de dispersión simple, función de fase.

📘 **Dónde se aprende** (1 clase): [B57-C13 · Atmósfera y aerosoles](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md).

### Exponente de Lyapunov máximo

- El exponente de Lyapunov máximo es `λ = lim (1/n) ln(|δ_n|/|δ_0|)`.

💡 **Cómo se explica en la clase [B73-C14](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md):**
- El script [lyapunov.py](lyapunov.py) calcula el exponente máximo por vector tangente y por trayectorias vecinas para cinco valores de `K` y 8 condiciones iniciales (comprueba A frente a B `< 5 %` para `K ≥ 2`, suma de exponentes `< 10⁻¹⁰` y `λ < 0,02` para `K = 0,5`).
- 🎯 **Por qué importa:** El exponente de Lyapunov es el número que cuantifica el caos: fija el horizonte de predicción y distingue una trayectoria regular de una caótica. En un espacio de fases mixto, un solo exponente no basta.
- 🔗 **Se estudia junto con:** vector tangente, trayectorias vecinas, tiempo de Lyapunov, espacio de fases mixto.

📘 **Dónde se aprende** (1 clase): [B73-C14 · Exponentes de Lyapunov](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md).

### Exponente de temperatura

- El exponente de temperatura `ν` es el valor de `d ln(tasa)/d ln T`.

💡 **Cómo se explica en la clase [B24-C07](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md):**
- Calcular el exponente de temperatura `ν` de una tasa de reacción.
- 🎯 **Por qué importa:** Dos protones se repelen con una fuerza eléctrica enorme; a las temperaturas de una estrella casi ninguno tiene energía para acercarse lo suficiente. Aun así la fusión ocurre, por efecto túnel.
- 🔗 **Se estudia junto con:** cadena protón–protón (p–p), ciclo CNO, barrera de Coulomb, efecto túnel.

📘 **Dónde se aprende** (1 clase): [B24-C07 · Ciclo CNO y cadena protón-protón](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md).

### Exponente de transporte

- El exponente de transporte `α` cumple `⟨(Δp)²⟩ ∝ n^α`: `α = 1` es difusión normal, `α = 2` es balístico.

💡 **Cómo se explica en la clase [B73-C15](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md):**
- Calcular el exponente de transporte `α` y reconocer difusión normal, ausente y anómala.
- Ejercicio 12 · integrador. Integrador. Elabora tu *tabla de difusión frente a `K`*: `D`, error, cociente con la teoría, exponente de transporte, validación por fases aleatorias y tiempos de difusión.
- 🎯 **Por qué importa:** Un conjunto de cuerpos en una región caótica no escapa de golpe: su excentricidad o su semieje se esparce como una caminata aleatoria, y el tiempo que tarda en recorrer una región fija la escala de supervivencia de la población. La decisión central: ¿cómo medir un coeficiente de difusión y cuándo no tiene sentido hablar de él?
- 🔗 **Se estudia junto con:** difusión del momento, teoría cuasi-lineal, modos aceleradores, tiempo de difusión.

📘 **Dónde se aprende** (1 clase): [B73-C15 · Difusión orbital](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md).

### Exponente Doppler

- El exponente Doppler `p` de `δ^p`.

💡 **Cómo se explica en la clase [B28-C12](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md):**
- Esta clase no ajusta ninguna observación: con `Γ = 100`, `θ_c = 0,1 rad` y exponente Doppler `3` (ilustrativos) calcula cómo cae el brillo con el ángulo de visión.
- 🎯 **Por qué importa:** Un destello gamma débil puede ser un evento normal visto de lado. Un modelo de emisión conjunta permite relacionar qué se ve en cada mensajero con el ángulo de visión.
- 🔗 **Se estudia junto con:** chorro estructurado, núcleo, ángulo de visión, brillo relativo.

📘 **Dónde se aprende** (1 clase): [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md).

### Exponente fraccionario

- Un exponente fraccionario como `3/2` combina una potencia y una raíz.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Con exponente fraccionario (`a1.5`) es directo y cabe en una línea.
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.
- 🔗 **Se estudia junto con:** potencia, base, exponente, cuadrado.

📘 **Dónde se aprende** (1 clase): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md).

### Exponente inestable

- `λ` es el exponente inestable real, `ω` la frecuencia en el plano y `ν = √c2` la frecuencia vertical.

💡 **Contexto en la clase [B76-C04](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR G["gamma, mu"] --> C["c2"] C --> E["ecuacion caracteristica"] E --> L["lambda (inestable)"] E --> W["omega (plano)"] C --> N["nu (vertical)"] W --> H["omega = nu : halo"] N --> H ``` *Descripción textual:* la distancia `γ` da `c2`; `c2` da la ecuación característica, de la que salen `λ` y `ω`;
- 🎯 **Por qué importa:** Una órbita halo no es un círculo: es un compromiso entre un modo inestable y dos oscilaciones. La decisión central: ¿qué dicen los modos lineales de `L2` sobre el tiempo de crecimiento de un error y sobre los periodos de la órbita?
- 🔗 **Se estudia junto con:** ecuación característica, frecuencia en el plano, frecuencia vertical, halo.

📘 **Dónde se aprende** (1 clase): [B76-C04 · Órbitas halo](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md).

### Exportación

- La exportación es el envío de un artículo o la transferencia de tecnología a un destino extranjero.

💡 **Cómo se explica en la clase [B125-C05](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md):**
- Se controlan objetos, pero también tecnología: según el Reglamento 2021/821, enviar por correo, subir a un servicio en línea o describir por teléfono una tecnología a alguien fuera de la UE cuenta como exportación.
- La evidencia es la ficha de ruta de exportación esquemática con su costo esperado del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** La tecnología espacial está sujeta a controles de exportación que condicionan el negocio, y las alianzas de la clase anterior chocan con ellos; ninguna clase los trata. La decisión central: ¿qué ruta de exportación debe esperar un producto o una transferencia de tecnología y cuánto cuesta, en promedio, esperar la licencia?
- 🔗 **Se estudia junto con:** doble uso, transferencia intangible, licencia, denegación.

📘 **Dónde se aprende** (1 clase): [B125-C05 · Control de exportaciones y transferencia de tecnología](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md).

### Exposición

- La exposición es el tiempo de captura.
- La exposición es el tiempo con el obturador abierto; el ISO es la amplificación de la señal; la apertura relativa del objetivo (f/) controla la luz.
- La amenaza es la probabilidad e intensidad del fenómeno; la exposición es lo que está en su camino; la vulnerabilidad es cuán dañable es.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C17](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md):**
- Para exposiciones largas, como las de S5 y S6, el instrumento tuvo que seguir el cielo; no sabemos cómo lo hizo cada autor, porque las fuentes consultadas no lo detallan.
- En una exposición, lo que se acumula es luz: un objeto de la mitad de brillo necesita el doble de tiempo para dejar la misma marca (aproximación válida mientras la placa responda de forma lineal, lo que no siempre ocurre con las emulsiones antiguas).
- 🎯 **Por qué importa:** Un dibujo depende de quien lo hace; una placa registra lo que llegó. La pregunta motivadora es: ¿qué cambia cuando la observación puede guardarse, compararse años después y medirse?
- 🔗 **Se estudia junto con:** astrofotografía, daguerrotipo, placa seca de gelatina, seguimiento.

📘 **Dónde se aprende** (4 clases): [B02-C17 · Nacimiento de la astrofotografía](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md); [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md); [B57-C19 · SIG y análisis de riesgo](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md); [B127-C05 · Evaluación actuarial básica del riesgo espacial](../programa/clases/B127/B127-C05-evaluacion-actuarial-basica-del-riesgo-espacial/CLASE.md).

### Exposición característica

- `E₀` es la exposición característica.

💡 **Contexto en la clase [B85-C14](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md):**
- 🎯 **Por qué importa:** Un recubrimiento que cumple al inicio puede salirse del intervalo con la exposición. La decisión central: ¿cuánto sube `α` y cuánto sube la temperatura al final de la misión, y qué incertidumbre trae el ajuste?
- 🔗 **Se estudia junto con:** ley saturante, ajuste, RMS, saturación.

📘 **Dónde se aprende** (1 clase): [B85-C14 · Degradación ultravioleta](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md).

### Exposición de neutrones

- La exposición de neutrones `τ = ∫ σ n_n v dt` mide cuántas capturas ocurren por núcleo.

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- Definir proceso s, exposición de neutrones y flujo estacionario.
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.
- 🔗 **Se estudia junto con:** rama asintótica de gigantes (AGB), pulso térmico, dragado, proceso s.

📘 **Dónde se aprende** (1 clase): [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### Exposición esperada

- La exposición esperada es `p×impacto`.

💡 **Cómo se explica en la clase [B83-C16](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md):**
- La exposición esperada es `Σ p·d = 89,35` días, mayor que la reserva de 60 días: en media la reserva no alcanza.
- Exposición esperada (esta clase): suma lineal.
- 🎯 **Por qué importa:** Una lista de riesgos sin números no dice cuánta reserva hace falta ni qué mitigar primero. La decisión central: ¿qué riesgos mitigar primero y alcanza la reserva de calendario para los que no se mitiguen?
- 🔗 **Se estudia junto con:** riesgo, puntaje, reserva, simulación de Monte Carlo.

📘 **Dónde se aprende** (1 clase): [B83-C16 · Gestión de riesgos técnicos](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md).

### Exposición limitada por el cielo

- La exposición limitada por el cielo es aquella en que el fondo supera con holgura a la lectura.

💡 **Cómo se explica en la clase [B44-C11](../programa/clases/B44/B44-C11-tiempo-de-exposicion/CLASE.md):**
- Hallar la exposición mínima limitada por el cielo.
- exposicion minima limitada por el cielo (k = 10): 171.4 s
- 🎯 **Por qué importa:** Exponer poco multiplica el ruido de lectura; exponer mucho arriesga la saturación. La decisión central: ¿cuánto debe durar cada cuadro dentro de un tiempo total dado?
- 🔗 **Se estudia junto con:** SNR, cielo, oscuridad, serie de cuadros.

📘 **Dónde se aprende** (1 clase): [B44-C11 · Tiempo de exposición](../programa/clases/B44/B44-C11-tiempo-de-exposicion/CLASE.md).

### Expresión

- Una expresión es una cadena de números y operaciones.
- Una expresión es una combinación de valores, variables y operadores que Python evalúa a un valor: `2 + 3 * 4` evalúa a `14`.

💡 **Cómo se explica en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- Esta convención existe para que todas las personas lean igual una misma expresión; no es una ley de la naturaleza, es un acuerdo, como el idioma.
- Piensa en una expresión como una receta con pasos ordenados.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.
- 🔗 **Se estudia junto con:** número natural, entero, número racional, número irracional.

📘 **Dónde se aprende** (2 clases): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md); [B07-C03 · Operadores y expresiones](../programa/clases/B07/B07-C03-operadores-y-expresiones/CLASE.md).

### Expresión algebraica

- Una expresión algebraica combina números, variables y operaciones (`a₁ + a₂`).

💡 **Cómo se explica en la clase [B03-C13](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md):**
- Traducir un enunciado verbal a una expresión algebraica y viceversa.
- python programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/laboratorio_expresiones.py
- 🎯 **Por qué importa:** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.
- 🔗 **Se estudia junto con:** término, términos semejantes, coeficiente, propiedad distributiva.

📘 **Dónde se aprende** (1 clase): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md).

### Extensión

- Una extensión (`.csv`) es el sufijo del nombre.

💡 **Cómo se explica en la clase [B07-C15](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md):**
- El laboratorio imprime la ruta relativa a la raíz del repositorio, el nombre, la extensión y la carpeta del CSV; y comprueba las diferencias Windows/POSIX con rutas «puras».
- Nombre: planetas_nssdc.csv | extensión: .csv | carpeta: B07-C08-lectura-de-archivos-csv
- 🎯 **Por qué importa:** Una causa muy común de «el programa no encuentra el archivo» es que la ruta funciona en el computador del autor y no en otro: se escribió con `C:\Usuarios\ana\datos\...`, o se asumió que el programa se ejecuta desde cierta carpeta.
- 🔗 **Se estudia junto con:** terminal, intérprete de comandos, directorio de trabajo, ruta.

📘 **Dónde se aprende** (1 clase): [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md).

### Extensión de reacción

- La extensión de reacción `p` es la probabilidad de que un extremo haya reaccionado.

💡 **Cómo se explica en la clase [B56-C21](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md):**
- Definir monómero, oligómero, extensión de reacción y ciclo húmedo–seco.
- 🎯 **Por qué importa:** C03 trata el origen de autorreplicantes, pero ninguna clase trata la polimerización experimental y sus límites. Antes de que un replicador pueda copiarse, hay que formar cadenas lo bastante largas.
- 🔗 **Se estudia junto con:** monómero, oligómero, ciclo húmedo–seco, distribución de Flory.

📘 **Dónde se aprende** (1 clase): [B56-C21 · Polimerización prebiótica experimental: oligómeros y condiciones de laboratorio](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md).

### Exterior

- La función interior es `g`, la exterior `f`.
- Un planeta interior (Mercurio, Venus) tiene su órbita dentro de la de la Tierra; uno exterior (Marte, Júpiter, Saturno), fuera.
- Un destino exterior (Marte, Júpiter) tiene `φ` positivo; un destino interior (Venus), negativo.

💡 **Cómo se explica en la clase [B08-C10](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md):**
- Un planeta exterior corre más lento y la Tierra lo alcanza una vez por período sinódico: en ese momento está en oposición.
- C["Planeta exterior"] --> D["Puede estar a cualquier ángulo<br/>0°–180°<br/>oposición = 180°"]
- 🎯 **Por qué importa:** Los planetas parecen «estrellas errantes» y un titular promete «alineación de planetas». La pregunta motivadora: ¿qué planetas puedo ver esta noche, dónde y a qué hora?
- 🔗 **Se estudia junto con:** elongación, este, oeste, planeta interior.

📘 **Dónde se aprende** (3 clases): [B08-C10 · Planetas observables y elongación](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md); [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md); [B75-C02 · Ángulos de fase planetaria](../programa/clases/B75/B75-C02-angulos-de-fase-planetaria/CLASE.md).

### Externo

- El borde interno es la pérdida de agua; el externo, el máximo invernadero de CO₂.

💡 **Cómo se explica en la clase [B56-C12](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md):**
- Con `T_ef = 5780 K` y `L = 1`: borde interno `0,993 UA`, externo `1,705 UA`.
- Los límites a 3300 K son `0,234` (externo) y `0,863` (interno) en unidades de `S_⊕`;
- 🎯 **Por qué importa:** Elegir blancos para buscar biofirmas exige un criterio objetivo. La zona habitable lo ofrece, con limitaciones.
- 🔗 **Se estudia junto con:** flujo estelar efectivo, zona habitable, borde interno, distancia límite.

📘 **Dónde se aprende** (1 clase): [B56-C12 · Exoplanetas potencialmente habitables](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md).

### Extinción

- La extinción es la pérdida de luz por absorción y dispersión en el camino; si es exponencial, `I = I₀ e^(−τ)` con `τ` la profundidad óptica.
- La extinción `A` (en magnitudes) mide la pérdida de luz: `A = −2,5 log₁₀(F/F₀)`;
- La extinción `A_V` mide el polvo atravesado.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- Extinción: I/I0 = 0.7788; pérdida = 0.2714 mag (= 1,0857 tau = 0.2714)
- Límites: magnitud bolométrica, sin extinción interestelar ni correcciones bolométricas por banda; las estrellas son sintéticas; no es una herramienta de fotometría.
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.
- 🔗 **Se estudia junto con:** función exponencial, número de Euler, logaritmo en base b, logaritmo decimal.

📘 **Dónde se aprende** (6 clases): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md); [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B48-C05 · Ventanas atmosféricas](../programa/clases/B48/B48-C05-ventanas-atmosfericas/CLASE.md); [B55-C08 · Fotoquímica cósmica](../programa/clases/B55/B55-C08-fotoquimica-cosmica/CLASE.md).

### Extracción

- La extracción es el espacio frente a un equipo para abrirlo o sacarlo.
- La extracción `PRK = HMAC(sal, IKM)`.

💡 **Cómo se explica en la clase [B109-C11](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md):**
- Con `0,50 m` de profundidad de cuerpo y extracciones ilustrativas de `0,30` a `0,90 m`, la profundidad necesaria va de `0,80` a `1,40 m`.
- Desde una pista de `1,00 m`, cinco de siete equipos son accesibles; la unidad sustituible (`1,30 m`) y la extracción de paleta (`1,40 m`) no.
- ⚠️ **Error frecuente:** Presentar las extracciones ilustrativas como requisitos. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Un equipo que no se puede abrir o extraer no se puede reparar, y en un hábitat sin taller externo eso es un riesgo de misión. La decisión central: ¿hay área, paso y holgura para trabajar y mantener cada equipo, y dónde falta?
- 🔗 **Se estudia junto con:** estación de trabajo, estación de mantenimiento, holgura, accesibilidad de un equipo.

📘 **Dónde se aprende** (2 clases): [B88-C38 · Gestión de claves y secretos en aviónica](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md); [B109-C11 · Diseño de espacios de trabajo, mantenimiento y laboratorio](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md).

### Extracción óptima

- La extracción óptima (de Horne, citada de memoria) usa `F = Σ P D/V / Σ P²/V`.

💡 **Cómo se explica en la clase [B45-C18](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md):**
- Para una columna de 400 e⁻ con perfil gaussiano de `σ = 2` píxeles, cielo de 60 e⁻/píxel y ruido de lectura de 6 e⁻, la suma da `σ = 40,18 e⁻` y la extracción óptima `33,22 e⁻`: mejora de `1,209`.
- Calcular la extracción óptima y su varianza.
- 🎯 **Por qué importa:** Una extracción ingenua pierde señal a ruido y es sensible a defectos. La decisión central: ¿qué pesos dan la menor varianza y cómo se protege la extracción de valores atípicos?
- 🔗 **Se estudia junto con:** perfil espacial, suma de apertura, varianza, rayo cósmico.

📘 **Dónde se aprende** (1 clase): [B45-C18 · Extracción de espectros](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md).

### Extrae el calor que entra. El

- Un refrigerador de cero evaporación extrae el calor que entra. El COP de Carnot es `T_c/(T_h − T_c)`.

💡 **Contexto en la clase [B59-C21](../programa/clases/B59/B59-C21-almacenamiento-criogenico-y-aislado-de-volatiles-extraidos/CLASE.md):**
- **Idea central (modelo mental):** Como un termo que deja pasar un poco de calor y pierde hielo: un refrigerador sería una nevera enchufada que lo repone. Límite: el termo no tiene que rechazar el calor a 250 K.
- 🎯 **Por qué importa:** Lo extraído sirve si se conserva. La decisión central: ¿se acepta la evaporación o se paga la potencia de un refrigerador de cero evaporación?
- 🔗 **Se estudia junto con:** es el líquido que se vaporiza por el calor que entra. El, son láminas reflectantes que reducen la radiación. Un, es T_c/(T_h − T_c). La.

📘 **Dónde se aprende** (1 clase): [B59-C21 · Almacenamiento criogénico y aislado de volátiles extraídos](../programa/clases/B59/B59-C21-almacenamiento-criogenico-y-aislado-de-volatiles-extraidos/CLASE.md).

### Extrapolación

- Una extrapolación es usar el modelo fuera de su dominio.
- La extrapolación es predecir fuera del rango de entrenamiento.
- La extrapolación va más allá del registro.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B17-C08](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md):**
- Extrapolación: pide predicciones fuera del rango y compáralas con la ley.
- A --> C["¿Respeta la física?<br/>Exponentes, monotonía, extrapolación"]
- 🎯 **Por qué importa:** Dos modelos pueden tener el mismo error en validación y haber aprendido cosas muy distintas: uno la ley física, otro un atajo que funciona en el rango visto. Si solo miras la métrica, no los distingues, y el atajo falla al primer dato fuera de rango.
- 🔗 **Se estudia junto con:** importancia por permutación, variable espuria, consistencia física, dependencia parcial.

📘 **Dónde se aprende** (4 clases): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B17-C08 · Interpretabilidad con consistencia física](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md); [B30-C19 · Impactos del clima espacial](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md); [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md).

### Extrapolación de banda limitada

- La extrapolación de banda limitada (*Gerchberg–Papoulis*) alterna dos operaciones: imponer los datos conocidos y filtrar a la banda de frecuencias donde se sabe que está la señal.

💡 **Cómo se explica en la clase [B15-C19](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md):**
- *Descripción textual:* según lo que se sepa de la señal se elige interpolación, ajuste de modelo o extrapolación de banda limitada; el resultado se verifica con una simulación de hueco conocido y con los residuos en los puntos medidos, y lo reconstruido se marca.
- Aplicar la extrapolación de banda limitada de Gerchberg–Papoulis y ver su convergencia.
- 🎯 **Por qué importa:** Si falta el 8 % de una serie, ¿se puede rellenar sin contaminar el análisis? Depende de lo que se sepa de la señal: si es suave y se conoce su forma, el relleno es casi exacto; si es un evento breve que cayó en el hueco, no hay método que lo recupere.
- 🔗 **Se estudia junto con:** hueco, interpolación, reconstrucción, regularización.

📘 **Dónde se aprende** (1 clase): [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md).

### Extrapolación de Richardson

- La extrapolación de Richardson estima el error de un método de orden `p` comparando resultados con `h` y `h/2`: `error(h/2) ≈ |y_{h/2} − y_h|/(2^p − 1)`.
- Esa propiedad permite la extrapolación de Richardson repetida: `T_{k,j} = T_{k,j−1} + (T_{k,j−1} − T_{k−1,j−1})/((n_k/n_{k−j})² − 1)`, y la columna `j` tiene orden `2j`.
- La extrapolación de Richardson combina un paso completo y dos medios para ganar un orden.

💡 **Cómo se explica en la clase [B11-C19](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md):**
- Estimar el error por extrapolación de Richardson.
- 🎯 **Por qué importa:** Un resultado numérico sin cota de error es una cifra sin sentido. Y gastar horas de cálculo para reducir un error de método que ya es menor que la incertidumbre de los datos es un desperdicio.
- 🔗 **Se estudia junto con:** error de truncamiento, error de redondeo, error de modelo, error de datos.

📘 **Dónde se aprende** (3 clases): [B11-C19 · Estimación de error y convergencia](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md); [B11-C21 · Integración numérica de alta precisión](../programa/clases/B11/B11-C21-integracion-numerica-de-alta-precision/CLASE.md); [B60-C03 · Integración numérica de redes químicas rígidas](../programa/clases/B60/B60-C03-integracion-numerica-de-redes-quimicas-rigidas/CLASE.md).

### Extrapolar

- Interpolar es evaluar dentro del intervalo de los nodos; extrapolar, fuera.
- El dominio de entrenamiento es el rango de entradas cubierto. Extrapolar es predecir fuera de él.

💡 **Cómo se explica en la clase [B11-C18](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md):**
- La regla práctica: no extrapolar; si hace falta, ampliar la tabla.
- No extrapolar: ampliar la tabla (generar más filas con el integrador).
- ⚠️ **Error frecuente:** Extrapolar sin cota. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.
- 🔗 **Se estudia junto con:** polinomio de Lagrange, polinomio nodal, error, Interpolar.

📘 **Dónde se aprende** (2 clases): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md); [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### Extremo aislado

- El extremo aislado no intercambia calor.

💡 **Cómo se explica en la clase [B85-C02](../programa/clases/B85/B85-C02-conduccion-termica-en-estructuras/CLASE.md):**
- Calcular el flujo y la eficiencia de una aleta con extremo aislado.
- 🎯 **Por qué importa:** El calor generado por un equipo debe llegar al radiador por algún camino; una unión mal conductora puede ser la resistencia dominante. La decisión central: ¿qué parte del camino de conducción limita el flujo y qué cambio lo mejora más?
- 🔗 **Se estudia junto con:** conducción, resistencia térmica, aleta, eficiencia.

📘 **Dónde se aprende** (1 clase): [B85-C02 · Conducción térmica en estructuras](../programa/clases/B85/B85-C02-conduccion-termica-en-estructuras/CLASE.md).

### Extremo global

- Un máximo (mínimo) local es un valor mayor (menor) que sus vecinos; un extremo global lo es en todo el dominio.

💡 **Cómo se explica en la clase [B09-C07](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md):**
- Sobre un intervalo cerrado `[a, b]` el extremo global está entre los puntos críticos y los bordes.
- 🎯 **Por qué importa:** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.
- 🔗 **Se estudia junto con:** función objetivo, punto crítico, máximo (mínimo) local, prueba de la segunda derivada.

📘 **Dónde se aprende** (1 clase): [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md).

### Extremófilo

- Un extremófilo es un organismo que prospera o se replica en condiciones extremas para la mayoría.

💡 **Cómo se explica en la clase [B56-C05](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md):**
- Definir extremófilo, actividad del agua, temperatura cardinal y límite de replicación.
- python programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/temperatura_cardinal.py
- 🎯 **Por qué importa:** Decidir si un ambiente es habitable, o si una nave puede contaminarlo, exige umbrales de temperatura y de agua disponible. La decisión central: dada la temperatura y la actividad del agua de un ambiente, ¿está dentro de los límites en que la vida terrestre puede replicarse?
- 🔗 **Se estudia junto con:** actividad del agua, temperatura cardinal, límite de replicación, Sobrevivir.

📘 **Dónde se aprende** (1 clase): [B56-C05 · Extremófilos y límites ambientales](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md).

### Eyecta

- La eyecta es el material lanzado.
- La eyecta es el material expulsado; su velocidad `v` decrece con la distancia `x` al punto de impacto.

💡 **Cómo se explica en la clase [B59-C17](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md):**
- Con `300 m/s` el alcance es `56 km`: un sitio a esa distancia de una zona sensible ya recibe eyecta.
- Estimar fracciones de eyecta con una distribución lognormal.
- 🎯 **Por qué importa:** Sin atmósfera, la eyecta viaja lejos y sin frenar. La decisión central: ¿a qué distancia de una zona sensible, como una sombra permanente, hay que operar para que la eyecta no la alcance?
- 🔗 **Se estudia junto con:** alcance, fórmula plana, deriva de energía, protección planetaria.

📘 **Dónde se aprende** (2 clases): [B59-C17 · Impacto ambiental extraterrestre](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md); [B61-C01 · Dinámica de eyección y escalado de cráteres](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md).
