# Términos · M (parte 1 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · **M** · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: **1** · [2](terminos-m-2.md) · [3](terminos-m-3.md)

### M

- Una dimensión es la clase física de una magnitud; aquí usamos tres dimensiones base: M (masa), L (longitud) y T (tiempo).

💡 **Contexto en la clase [B13-C02](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md):**
- **Idea central (modelo mental):** El análisis dimensional es un filtro de sentido que se aplica en papel, antes de calcular. La trazabilidad es una cadena de custodia de la confianza: cada eslabón compara un instrumento con otro más preciso hasta llegar a la definición de la unidad.
- 🎯 **Por qué importa:** Un satélite recibe un comando con un tiempo de encendido de motor; el ingeniero de tierra usó una fórmula del periodo orbital copiada de una hoja de cálculo. Si la fórmula está mal dimensionada, el resultado sale en «segundos al cuadrado» o en «metros por segundo» sin que nadie lo note.
- 🔗 **Se estudia junto con:** dimensión, L, T, vector de exponentes.

📘 **Dónde se aprende** (1 clase): [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md).

### MAC

- El MAC es `(φᵀψ)²/((φᵀφ)(ψᵀψ))`.

💡 **Cómo se explica en la clase [B84-C30](../programa/clases/B84/B84-C30-correlacion-modelo-ensayo-y-actualizacion-de-modelos/CLASE.md):**
- MAC `1,0000; 0,9998; 0,9996`; fuera de la diagonal `0,0018`.
- El MAC cercano a 1 no distingue estos modelos: es insensible a escalas globales.
- ⚠️ **Error frecuente:** Confiar en el MAC solo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un MAC de 0,999 no basta: puede coexistir con un error de 3,6 % en frecuencia, y actualizar parámetros que no se pueden identificar da un modelo que ajusta pero no es físico. La decisión central: ¿cumple el modelo los criterios de correlación y qué parámetros se pueden actualizar con los datos?
- 🔗 **Se estudia junto con:** ortogonalidad cruzada, actualización.

📘 **Dónde se aprende** (1 clase): [B84-C30 · Correlación modelo-ensayo y actualización de modelos](../programa/clases/B84/B84-C30-correlacion-modelo-ensayo-y-actualizacion-de-modelos/CLASE.md).

### Mach

- El Mach del frente es `Ṙ/c₀`.

💡 **Cómo se explica en la clase [B58-C16](../programa/clases/B58/B58-C16-consecuencias-geofisicas-de-impactos/CLASE.md):**
- *Descripción textual:* la energía se reparte en una parte sísmica y otra en la onda; la solución autosemejante da el radio del frente y se busca donde su velocidad cae a Mach 2.
- Escala cúbica: `R ∝ E^(1/3)` a Mach fijo.
- ⚠️ **Error frecuente:** Aplicar Sedov a Mach bajo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Las consecuencias se miden por zonas: sismo, onda de choque, calor. Las escalas con la energía son lo que permite comparar casos.
- 🔗 **Se estudia junto con:** magnitud sísmica equivalente, solución de Sedov–Taylor, relaciones de Rankine–Hugoniot, radio de Mach 2.

📘 **Dónde se aprende** (1 clase): [B58-C16 · Consecuencias geofísicas de impactos](../programa/clases/B58/B58-C16-consecuencias-geofisicas-de-impactos/CLASE.md).

### Macronutrientes

- Los macronutrientes (N, P, K, Ca, Mg, S) se dan en mM; los micronutrientes (B, Mn, Zn, Cu, Mo, Fe) en décimas o centésimas de mg/L.

💡 **Contexto en la clase [B115-C03](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md):**
- 🎯 **Por qué importa:** Una solución nutritiva que se repone «por conductividad» puede parecer estable y estar desequilibrada. La decisión central: ¿qué se mide, cada cuánto y qué se repone para que cada ion se mantenga cerca de su objetivo, y cuándo conviene renovar la solución?
- 🔗 **Se estudia junto con:** solución nutritiva, micronutrientes, solución madre, conductividad eléctrica (EC).

📘 **Dónde se aprende** (1 clase): [B115-C03 · Control de nutrientes y solución nutritiva](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md).

### Macropartícula

- Una macropartícula representa muchas reales.

💡 **Cómo se explica en la clase [B35-C05](../programa/clases/B35/B35-C05-simulacion-de-plasmas-por-particulas-pic/CLASE.md):**
- Ejercicio 7. Número de macropartículas por celda en dos haces.
- 🎯 **Por qué importa:** Un código sin validar produce figuras bonitas y físicas falsas. La decisión central: ¿reproduce el código la frecuencia y la tasa de crecimiento conocidas?
- 🔗 **Se estudia junto con:** ponderación CIC, salto de rana, ruido de partículas, deriva de energía.

📘 **Dónde se aprende** (1 clase): [B35-C05 · Simulación de plasmas por partículas (PIC)](../programa/clases/B35/B35-C05-simulacion-de-plasmas-por-particulas-pic/CLASE.md).

### Macro-paso

- Un macro-paso es el avance `H`.

💡 **Cómo se explica en la clase [B11-C21](../programa/clases/B11/B11-C21-integracion-numerica-de-alta-precision/CLASE.md):**
- Con `K = 4` (`n = 2, 4, 6, 8`): `3 + 5 + 7 + 9 = 24` evaluaciones por macro-paso; con 10 macro-pasos, 240.
- Con macro-pasos relativamente grandes (`M = 40`, `K = 3`) la ventaja es de solo 2,4 veces (`1,56 m` frente a `3,7 m`), y con `M = 80` es de 9,6 veces: aún no está en régimen asintótico.
- ⚠️ **Error frecuente:** Usar orden alto con macro-pasos enormes. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Una trayectoria de millones de vueltas, un encuentro cercano que exige metros de precisión o una comprobación contra otro código piden errores de truncamiento muy por debajo del que da RK4 a costo razonable. A orden alto el costo por precisión baja mucho, pero el error de redondeo pasa a ser el límite.
- 🔗 **Se estudia junto con:** punto medio modificado, extrapolación de Richardson, Gragg–Bulirsch–Stoer, aritmética extendida.

📘 **Dónde se aprende** (1 clase): [B11-C21 · Integración numérica de alta precisión](../programa/clases/B11/B11-C21-integracion-numerica-de-alta-precision/CLASE.md).

### Macroturbulencia

- La macroturbulencia es a escalas mayores.

💡 **Cómo se explica en la clase [B32-C06](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md):**
- La macroturbulencia domina el ancho y su efecto se confunde con el de la rotación (B32-C11).
- *Descripción textual:* la velocidad térmica y la microturbulencia se suman en cuadratura; la macroturbulencia se convoluciona y suma otra varianza sin cambiar el área.
- 🎯 **Por qué importa:** Atribuir mal el ensanchamiento sesga la rotación y la abundancia. La decisión central: ¿cuánto aporta cada efecto al ancho de la línea?
- 🔗 **Se estudia junto con:** velocidad térmica, microturbulencia, convolución, cuadratura.

📘 **Dónde se aprende** (1 clase): [B32-C06 · Micro y macroturbulencia y granulación estelar](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md).

### MAD

- La MAD es la mediana de las desviaciones absolutas respecto de la mediana;
- La MAD (desviación absoluta mediana) es la mediana de `|x − mediana|`; multiplicada por 1,4826 estima la desviación típica de una distribución normal (el factor 1,4826 lo doy como conocido; no lo verifiqué en una fuente en esta clase).
- La MAD es la mediana de las desviaciones absolutas;
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C11](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md):**
- Paso 4 · Diagnóstico. Los residuos de OLS son grandes en los tres puntos y mucho menores en los demás; los residuos de Huber destacan los tres atípicos (`MAD` pequeña).
- Calcular la mediana, la MAD y una desviación robusta `σ̂ = MAD/0,6745`.
- 🎯 **Por qué importa:** Los datos reales traen errores de transmisión, rayos cósmicos en un detector, una lectura perdida o un salto del sensor. Un solo punto muy alejado puede torcer la recta de mínimos cuadrados y producir parámetros y predicciones erróneos con errores típicos pequeños y engañosos.
- 🔗 **Se estudia junto con:** valor atípico, punto de ruptura, pendiente de Theil–Sen, M-estimador.

📘 **Dónde se aprende** (4 clases): [B12-C11 · Regresión robusta](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md); [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md); [B44-C15 · Píxeles defectuosos](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md); [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md).

### Maduración

- La maduración es el cambio espectral con la exposición.

💡 **Cómo se explica en la clase [B53-C22](../programa/clases/B53/B53-C22-meteorizacion-espacial-micrometeoritos-viento-solar-y-maduracion-del-regolito/CLASE.md):**
- Límite de la analogía: la maduración real depende de la composición, el flujo de partículas y la lejanía al Sol.
- Descripción larga: el ajuste recupera la escala de maduración y la mezcla coincide con la solución analítica.
- 🎯 **Por qué importa:** Una superficie «vieja» se ve distinta de una «fresca» aunque tenga la misma composición. La decisión central: ¿cuánto del cambio espectral se debe al tiempo de exposición y con qué incertidumbre se estima su escala?
- 🔗 **Se estudia junto con:** enrojecimiento, jardinería, reflexión.

📘 **Dónde se aprende** (1 clase): [B53-C22 · Meteorización espacial: micrometeoritos, viento solar y maduración del regolito](../programa/clases/B53/B53-C22-meteorizacion-espacial-micrometeoritos-viento-solar-y-maduracion-del-regolito/CLASE.md).

### Madurez

- La madurez (heredado, modificado, nuevo diseño, nueva tecnología) fija el crecimiento esperado.

💡 **Cómo se explica en la clase [B124-C19](../programa/clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md):**
- La CBE total es `355,0` kg y cada componente se infla según su madurez: 5 % heredado, 10 % modificado, 20 % nuevo diseño, 30 % nueva tecnología (ilustrativos).
- *Descripción textual:* los objetivos se descomponen en requisitos que las secciones deben citar, y la matriz revela cobertura y huérfanas; por otro lado, las estimaciones de masa se inflan por madurez, se comparan con el límite y se prueban con simulación.
- 🎯 **Por qué importa:** Una propuesta pierde puntos cuando algo prometido no tiene sección que lo sostenga o cuando el presupuesto no tiene margen. La decisión central: ¿está todo lo prometido cubierto y cuánta reserva necesita el diseño para ser creíble?
- 🔗 **Se estudia junto con:** trazabilidad, cobertura, sección huérfana, CBE.

📘 **Dónde se aprende** (1 clase): [B124-C19 · Redacción de propuesta de misión](../programa/clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md).

### MAE

- `AP50` y `AP75` exigen IoU de 0,50 y 0,75. MAE es el error absoluto medio, RMSE el cuadrático medio, AbsRel la media de `|ẑ − z|/z` y delta1 la fracción de puntos con `máx(z/ẑ, ẑ/z) < 1,25`.

💡 **Cómo se explica en la clase [B33-C12](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md):**
- Ejercicio 2 · con una pista. MAE de `γ`/2.
- Ejercicio 6. Cociente RMSE/MAE de `γ` × 2.
- ⚠️ **Error frecuente:** Confundir sesgo y MAE. Se corrige con 8.1.
- 🎯 **Por qué importa:** Saber cómo falla un modelo orienta su mejora. La decisión central: ¿qué sesgo y qué precisión tiene cada especificación del arrastre?
- 🔗 **Se estudia junto con:** sesgo, RMSE, ventana de acierto, mala especificación.

📘 **Dónde se aprende** (2 clases): [B33-C12 · Pronóstico de llegada y severidad de CME](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md).

### Maestro

- Un maestro (*master*) es la combinación (promedio o mediana) de varias exposiciones de calibración.

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- La varianza de un píxel de cielo es: lectura `σ_L²` + fotones (`cielo + oscuro`) + el ruido del oscuro maestro, que vale `(σ_L² + oscuro)/K` si se promedian `K` oscuros.
- R["Imagen cruda"] --> A["− oscuro maestro<br/>(incluye bias)"]
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.
- 🔗 **Se estudia junto con:** imagen digital, píxel, ADU, ganancia.

📘 **Dónde se aprende** (1 clase): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md).

### Magnetar

- Un magnetar es una estrella de neutrones cuyo campo alimenta su emisión.

💡 **Cómo se explica en la clase [B27-C06](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md):**
- Para un magnetar de periodo `5 s` (ilustrativo), la energía rotacional es `½Iω² = 7,9 × 10³⁷ J`: la energía magnética es unas `210` veces mayor; por eso la emisión del magnetar no la alimenta la rotación.
- Con ese mecanismo y campos iniciales algo mayores se alcanzan campos de magnetar; el origen real del campo sigue siendo tema abierto, y aquí solo se muestra la aritmética.
- 🎯 **Por qué importa:** Los magnetares producen estallidos y llamaradas gigantes que alimenta su campo, no su rotación. Entender la escala del campo y de su energía explica por qué son una familia aparte y cómo se interpretan sus espectros.
- 🔗 **Se estudia junto con:** campo crítico cuántico, energía ciclotrónica, niveles de Landau relativistas, energía magnética.

📘 **Dónde se aprende** (1 clase): [B27-C06 · Magnetares y campos extremos](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md).

### Magnetización remanente

- La magnetización remanente es la que una roca conserva sin campo externo.

💡 **Contexto en la clase [B65-C03](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md):**
- **Idea central (modelo mental):** Un imán enterrado desvía un compás que pasa por encima; cuanto más alto pasa el compás, más suave es la desviación.
- 🎯 **Por qué importa:** La corteza magnetizada permite reconstruir campos de cuerpos que hoy no tienen dinamo. La decisión central: ¿qué parte de un mapa de anomalías es información sobre la magnetización y qué parte es ambigüedad geométrica?
- 🔗 **Se estudia junto con:** anomalía magnética, temperatura de Curie, momento magnético, profundidad de Curie.

📘 **Dónde se aprende** (1 clase): [B65-C03 · Magnetismo cortical remanente y anomalías magnéticas](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md).

### Magnetizado

- Un electrón está magnetizado si `r ≪ L`.

💡 **Cómo se explica en la clase [B78-C08](../programa/clases/B78/B78-C08-propulsores-hall/CLASE.md):**
- En un canal ilustrativo de `25 mm` con `B = 0,015 T` y electrones de `10 eV`, el radio de giro del electrón es `0,711 mm` y el del ion de xenón a `300 V`, `1807 mm`: el electrón está magnetizado y el ion no.
- Ejercicio 3 · guiado (casi autónomo). ¿Por qué el ion no está magnetizado?
- 🎯 **Por qué importa:** Sin rejillas no hay límite de Child–Langmuir, pero el propulsor depende de que los electrones giren en un radio pequeño y los iones pasen casi rectos. La decisión central: ¿cuánto vale cada radio de giro frente al largo del canal y qué cambia al subir la tensión?
- 🔗 **Se estudia junto con:** radio de giro, frecuencia de ciclotrón, parámetro de Hall, deriva E×B.

📘 **Dónde se aprende** (1 clase): [B78-C08 · Propulsores Hall](../programa/clases/B78/B78-C08-propulsores-hall/CLASE.md).

### Magnetograma

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C21](../programa/clases/B47/B47-C21-magnetografos-y-medicion-de-campos-solares/CLASE.md):**
- **Idea central (modelo mental):** Es como dos peines idénticos desplazados en sentidos opuestos: si el desplazamiento es pequeño la diferencia entre ambos es proporcional a la pendiente de los dientes (campo débil), y se satura si es grande.
- 🎯 **Por qué importa:** El campo solar se infiere de una señal diminuta: una diferencia de polarización circular. La decisión central: ¿cuántas posiciones espectrales y qué ruido permiten medir el campo con una incertidumbre dada, y hasta qué campo vale la aproximación débil?
- 🔗 **Se estudia junto con:** efecto Zeeman, factor de Landé efectivo, desdoblamiento, parámetro de Stokes V.

📘 **Dónde se aprende** (1 clase): [B47-C21 · Magnetógrafos y medición de campos solares](../programa/clases/B47/B47-C21-magnetografos-y-medicion-de-campos-solares/CLASE.md).

### Magnetómetro

- Un magnetómetro mide `B`.

💡 **Cómo se explica en la clase [B05-C17](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md):**
- Ejercicio 10 · transferencia. Un magnetómetro registra 20 µT extra cuando se enciende un cable de 10 A a 10 cm.
- 🎯 **Por qué importa:** La Tierra tiene un campo magnético que un satélite puede medir con un magnetómetro y que actúa sobre las partículas cargadas que lo atraviesan; además, una corriente a bordo crea su propio campo, que puede perturbar esas medidas.
- 🔗 **Se estudia junto con:** campo magnético, fuerza magnética, radio de giro, frecuencia ciclotrónica.

📘 **Dónde se aprende** (1 clase): [B05-C17 · Campos magnéticos](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md).

### Magnetómetro fluxgate

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C24](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md):**
- **Idea central (modelo mental):** El analizador es una criba que deja pasar solo las partículas de una energía por carga; barriendo la criba se cuenta cuántas hay de cada energía y de ahí se deducen la velocidad media y la dispersión.
- 🎯 **Por qué importa:** La energía por carga elegida por el analizador determina qué se mide; la resolución de los canales limita la temperatura que se recupera. La decisión central: ¿cuántos canales y qué corrección dan la velocidad y la temperatura del plasma con error aceptable?
- 🔗 **Se estudia junto con:** analizador electrostático, energía por carga, copa de Faraday, distribución de velocidades.

📘 **Dónde se aprende** (1 clase): [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md).

### Magnetón de Bohr

- El magnetón de Bohr `μ_B = eħ/(2m_e)`.

💡 **Cómo se explica en la clase [B31-C05](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md):**
- Comparar con el magnetón de Bohr de NIST.
- 🎯 **Por qué importa:** El espín explica los desdoblamientos de líneas espectrales y la estructura de la materia. La decisión central: ¿qué probabilidades y qué energías resultan de un espín en un campo?
- 🔗 **Se estudia junto con:** espín, analizador de Stern–Gerlach, triplete, singlete.

📘 **Dónde se aprende** (1 clase): [B31-C05 · Espín y momento angular](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md).

### Magnetopausa

- La magnetopausa es la frontera con el viento solar.
- La magnetopausa es la frontera entre el viento y el campo terrestre.

💡 **Cómo se explica en la clase [B30-C15](../programa/clases/B30/B30-C15-magnetosfera-terrestre/CLASE.md):**
- Con `21 nPa` ilustrativos la magnetopausa (`6,455 R_⊕`) queda dentro del radio geosíncrono (`6,611 R_⊕`): un satélite ahí quedaría expuesto al viento.
- Con un campo ecuatorial superficial ilustrativo `B₀ = 31 200 nT` y un viento de `5 × 10⁶ m⁻³` a `400 km/s` (presión dinámica `1,338 nPa`) la magnetopausa queda a `10,25 R_⊕`.
- ⚠️ **Error frecuente:** Pensar que la magnetopausa nunca llega a la órbita geosíncrona. Se corrige con 8.4.
- 🎯 **Por qué importa:** Los satélites geosíncronos están cerca del borde de la magnetosfera cuando el viento es fuerte. La decisión central: ¿dónde está la magnetopausa y qué pasa cuando se comprime?
- 🔗 **Se estudia junto con:** dipolo, capa L, presión dinámica, órbita geosíncrona.

📘 **Dónde se aprende** (2 clases): [B30-C15 · Magnetosfera terrestre](../programa/clases/B30/B30-C15-magnetosfera-terrestre/CLASE.md); [B35-C08 · Flujos de plasma estacionarios y balance de presiones](../programa/clases/B35/B35-C08-flujos-de-plasma-estacionarios-y-balance-de-presiones/CLASE.md).

### Magnificación

- La magnificación `μ` es el cociente entre el brillo de la imagen y el de la fuente sin lente.

💡 **Cómo se explica en la clase [B25-C14](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md):**
- La magnificación de cada imagen es el cociente entre el área de la imagen y la de la fuente: `μ = (θ/β)(dθ/dβ)`.
- Cuando `u → 0` la magnificación crece sin límite (en la realidad la fuente es extensa y está limitada).
- 🎯 **Por qué importa:** La luz de una galaxia lejana se curva al pasar cerca de una masa, y la masa interior se deduce del tamaño de la distorsión sin importar si es luminosa u oscura ni si está en equilibrio. Por eso las lentes son una prueba directa de la distribución de masa.
- 🔗 **Se estudia junto con:** lente gravitacional, ángulo de desviación, ecuación de la lente, radio de Einstein.

📘 **Dónde se aprende** (2 clases): [B25-C14 · Lentes gravitacionales galácticas](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md); [B29-C05 · Microlentes gravitacionales](../programa/clases/B29/B29-C05-microlentes-gravitacionales/CLASE.md).

### Magnitud

- La magnitud es una escala de brillo en la que una diferencia de 5 magnitudes equivale a un factor 100 en flujo; mayor magnitud = más débil.
- La magnitud es una escala logarítmica de brillo (C10).
- Una magnitud es una propiedad medible (longitud, masa, tiempo).
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C10](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md):**
- En magnitudes, `Δm = 2,5·log₁₀(204) = 5,77`: ve objetos 5,8 magnitudes más débiles.
- Paso 5 · Luz. `Δm = 2,5·log₁₀(204) = 5,77` magnitudes.
- 🎯 **Por qué importa:** Si el ojo bastara, no habría observatorios. La luz visible es una franja pequeña del espectro electromagnético (S1, S2); además, tu pupila recoge poca luz, separa detalles hasta cierto tamaño y puede engañarte.
- 🔗 **Se estudia junto con:** rango espectral, sensibilidad, apertura, resolución angular.

📘 **Dónde se aprende** (8 clases): [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md); [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md); [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md); [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md); [B45-C02 · Magnitudes y sistemas de filtros](../programa/clases/B45/B45-C02-magnitudes-y-sistemas-de-filtros/CLASE.md) y 2 más.

### Magnitud absoluta

- La magnitud aparente `m` mide cuán brillante *se ve* un objeto desde donde se mide; la magnitud absoluta `M` es la que tendría a 10 parsecs; la diferencia `m − M` es el módulo de distancia.
- La magnitud absoluta `H` mide el brillo intrínseco.

💡 **Cómo se explica en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- La magnitud absoluta es la que daría a `d = 10 pc`, de modo que `m − M = −2,5 log₁₀[(10/d)²] = 5 log₁₀(d/10 pc)`.
- *Descripción textual:* se parte de un flujo, se divide por el flujo de referencia, se aplica `−2,5 log₁₀` para obtener la magnitud, y restando la magnitud absoluta se obtiene el módulo de distancia, de donde sale la distancia.
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.
- 🔗 **Se estudia junto con:** función exponencial, número de Euler, logaritmo en base b, logaritmo decimal.

📘 **Dónde se aprende** (2 clases): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B58-C01 · Clasificación de cuerpos menores](../programa/clases/B58/B58-C01-clasificacion-de-cuerpos-menores/CLASE.md).

### Magnitud absoluta bolométrica

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B38-C01](../programa/clases/B38/B38-C01-funciones-de-luminosidad-estelar/CLASE.md):**
- **Idea central (modelo mental):** Como contar linternas de noche: las potentes se ven a gran distancia, las débiles solo a pocos pasos; para saber cuántas linternas de cada potencia hay, cada una cuenta con el peso del volumen en que podrías haberla visto.
- 🎯 **Por qué importa:** Contar las estrellas que se ven no es contar las que hay: las brillantes se ven desde lejos y las débiles solo de cerca. La decisión central: ¿cómo corrijo la selección para recuperar la densidad real por intervalo de luminosidad?
- 🔗 **Se estudia junto con:** función de luminosidad, magnitud aparente, límite de magnitud, volumen máximo.

📘 **Dónde se aprende** (1 clase): [B38-C01 · Funciones de luminosidad estelar](../programa/clases/B38/B38-C01-funciones-de-luminosidad-estelar/CLASE.md).

### Magnitud absoluta límite

- La magnitud absoluta límite a la distancia `d` es `M_lim(d) = m_lim − 5 log₁₀(d/10 pc)`.

💡 **Cómo se explica en la clase [B25-C19](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md):**
- *Descripción textual:* el límite de brillo aparente fija un límite de magnitud absoluta que depende de la distancia; con él se calcula la fracción detectada y la media sesgada; el peso `1/V_max` restituye la media de la población.
- El ejemplo conductor es un catálogo sintético: galaxias con densidad uniforme y magnitudes absolutas normales (media `−20,0`, dispersión `1,0`, ilustrativas), con límite aparente `m_lim = 17,0`.
- 🎯 **Por qué importa:** Un catálogo limitado por flujo ve las galaxias brillantes a gran distancia y casi solo ellas; si se promedian sus luminosidades sin cuidado, el resultado depende de la distancia del catálogo y no de las galaxias. Saber qué falta es tan importante como saber qué hay.
- 🔗 **Se estudia junto con:** catálogo, límite de flujo, completitud, sesgo de selección.

📘 **Dónde se aprende** (1 clase): [B25-C19 · Catálogos y sesgos de selección](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md).

### Magnitud aparente

- La magnitud aparente `m` mide cuán brillante *se ve* un objeto desde donde se mide; la magnitud absoluta `M` es la que tendría a 10 parsecs; la diferencia `m − M` es el módulo de distancia.
- La magnitud aparente `m` es una medida logarítmica del flujo de luz que llega de un objeto, como se ve desde la Tierra; la escala crece al disminuir el brillo y los valores negativos son más brillantes que el cero (S3).
- La magnitud aparente `m` mide el brillo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- Paso 2 · Magnitud aparente. `S_☉/f₀ = 1361/2,518021 × 10⁻⁸ = 5,405 × 10¹⁰`;
- Paso 4 · Comprobar. `M + (m − M) = 4,740 − 31,572 = −26,832` ✓: la magnitud aparente, la absoluta y la distancia son coherentes entre sí.
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.
- 🔗 **Se estudia junto con:** función exponencial, número de Euler, logaritmo en base b, logaritmo decimal.

📘 **Dónde se aprende** (4 clases): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B08-C11 · Magnitudes aparentes y brillo](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md); [B38-C01 · Funciones de luminosidad estelar](../programa/clases/B38/B38-C01-funciones-de-luminosidad-estelar/CLASE.md); [B118-C03 · Detección y seguimiento óptico](../programa/clases/B118/B118-C03-deteccion-y-seguimiento-optico/CLASE.md).

### Magnitud con unidad

- Una magnitud con unidad (`Quantity` en Astropy) es un número, o un arreglo, junto con una unidad.

💡 **Cómo se explica en la clase [B14-C04](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md):**
- En Astropy (S2), una magnitud se crea multiplicando un número o un arreglo por una unidad: `5 * u.km`.
- Crear y convertir magnitudes con unidades en Astropy y leer su valor numérico en una unidad elegida.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió al llegar a Marte. NASA atribuye la pérdida a un error de navegación causado por no traducir unidades inglesas a métricas: el software en tierra usaba unidades inglesas y el de a bordo, métricas (S1).
- 🔗 **Se estudia junto con:** unidad, dimensión, conversión, equivalencia.

📘 **Dónde se aprende** (1 clase): [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### Magnitud conservada

- Una magnitud conservada (o *invariante*) es una cantidad que no cambia a lo largo del movimiento.

💡 **Cómo se explica en la clase [B23-C02](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md):**
- Enumerar las magnitudes conservadas y las simetrías de un problema de dos cuerpos.
- 🔗 **Se estudia junto con:** energía específica, momento angular específico, simetría, equivariante.

📘 **Dónde se aprende** (1 clase): [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md).

### Magnitud de momento

- La magnitud de momento `Mw` es una función logarítmica de `M0`.

💡 **Cómo se explica en la clase [B57-C17](../programa/clases/B57/B57-C17-terremotos-y-deformacion/CLASE.md):**
- Una zona de subducción acumula deformación lentamente y la libera de golpe: el momento sísmico es cuánta regla se rompió, la magnitud es su logaritmo.
- *Descripción textual:* la magnitud fija el momento, que con el área da el deslizamiento; el deslizamiento deforma la superficie, y esa deformación se proyecta a la línea de visión del radar.
- 🎯 **Por qué importa:** Medir la deformación permite saber cuánto deslizó la falla y cuánta tensión queda. La decisión central: ¿cómo se pasa de un número de magnitud al deslizamiento y a la deformación que verá un satélite?
- 🔗 **Se estudia junto con:** momento sísmico, profundidad de bloqueo, deslizamiento, deformación cosísmica.

📘 **Dónde se aprende** (1 clase): [B57-C17 · Terremotos y deformación](../programa/clases/B57/B57-C17-terremotos-y-deformacion/CLASE.md).

### Magnitud derivada

- Una magnitud derivada se forma multiplicando potencias de las base: la fuerza se mide en newton, `1 N = 1 kg·m/s²`.

💡 **Cómo se explica en la clase [B05-C01](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md):**
- Esta tabla es la versión accesible de un diagrama que une cada magnitud derivada con las tres base.
- 🎯 **Por qué importa:** La pregunta motivadora es: ¿cómo sé que una fórmula o un cálculo tiene sentido antes de confiar en su resultado? La decisión central es qué declarar junto a cada número (magnitud, unidad y dimensión) y cómo comprobar que las ecuaciones son coherentes.
- 🔗 **Se estudia junto con:** magnitud física, unidad, valor numérico, dimensión.

📘 **Dónde se aprende** (1 clase): [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md).

### Magnitud diferencial

- La magnitud diferencial es `m_v = m_c − 2,5 log₁₀(F_v/F_c)`.

💡 **Cómo se explica en la clase [B129-C02](../programa/clases/B129/B129-C02-fotometria-participativa/CLASE.md):**
- F["Flujos F_v y F_c"] --> D["Magnitud diferencial"]
- *Descripción textual:* los flujos dan la magnitud diferencial y su error fotónico; con ellos se combinan los voluntarios con pesos y se obtiene la curva de luz y el periodo, afectados por el sesgo de cada observador.
- 🎯 **Por qué importa:** Una curva de luz de una estrella variable se construye con medidas de muchas personas con instrumentos distintos. La decisión central: ¿cómo se combinan sus medidas para que la curva sea más precisa que cada una, y qué error no se puede promediar?
- 🔗 **Se estudia junto con:** error fotónico, peso, media ponderada, sesgo.

📘 **Dónde se aprende** (1 clase): [B129-C02 · Fotometría participativa](../programa/clases/B129/B129-C02-fotometria-participativa/CLASE.md).

### Magnitud física

- Una magnitud física es una propiedad medible de un sistema, como la longitud o la masa.

💡 **Cómo se explica en la clase [B05-C01](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md):**
- python programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/analisis_dimensional.py
- 🎯 **Por qué importa:** La pregunta motivadora es: ¿cómo sé que una fórmula o un cálculo tiene sentido antes de confiar en su resultado? La decisión central es qué declarar junto a cada número (magnitud, unidad y dimensión) y cómo comprobar que las ecuaciones son coherentes.
- 🔗 **Se estudia junto con:** unidad, valor numérico, dimensión, Sistema Internacional (SI).

📘 **Dónde se aprende** (1 clase): [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md).

### Magnitud límite

- La magnitud límite de un catálogo es el brillo mínimo que incluye (C11).
- La magnitud límite es la del objeto más débil que se puede ver en un cielo y con un instrumento dados; la IMO usa 6,5 como referencia en su definición de ZHR (S4).
- La magnitud límite (MLE) es la de la estrella más débil visible; depende del cielo, del ojo y del instrumento; la IMO la define como la estrella más débil que se ve durante una sesión (S3).
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C11](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md):**
- Con 200 mm: 7,28 magnitudes y límite ideal ≈ 13,8.
- Pero esa noche la Luna llena aclara el cielo, y la magnitud límite del ojo no sería 6,5 sino menor (C12 lo mide).
- 🎯 **Por qué importa:** Un informe dice «cometa de magnitud 6» y otro «galaxia de magnitud 9». Sin entender la escala, no sabrás si los verás a simple vista, con binoculares o solo con telescopio.
- 🔗 **Se estudia junto con:** magnitud aparente, flujo, ganancia, fuente puntual.

📘 **Dónde se aprende** (6 clases): [B08-C06 · Constelaciones y catálogos estelares](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md); [B08-C11 · Magnitudes aparentes y brillo](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md); [B08-C12 · Limitación por contaminación lumínica](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md); [B41-C10 · Apertura y relación focal](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md); [B42-C21 · Estrellas guía naturales y cobertura de cielo](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md); [B129-C03 · Seguimiento ciudadano de meteoros](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md).

### Magnitud observable

- Una magnitud observable es la que algún instrumento puede registrar directamente.

💡 **Contexto en la clase [B01-C06](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md):**
- **Idea central (modelo mental):** Imagina un embudo: arriba entra la curiosidad amplia; en cada nivel pasas un filtro y queda algo más estrecho; abajo sale una pregunta que puedes responder.
- 🎯 **Por qué importa:** «¿Hay vida en otros planetas?» es una pregunta legítima y apasionante, pero nadie puede responderla con un cuaderno y una cámara de teléfono. «¿Cambia el tamaño aparente de la Luna a lo largo de un mes?» sí puede responderse con una cámara y un trípode, y su respuesta enseña algo real sobre la órbita lunar.
- 🔗 **Se estudia junto con:** pregunta investigable, variable, variable dependiente, independiente.

📘 **Dónde se aprende** (1 clase): [B01-C06 · Preguntas investigables en astronomía](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md).

### Magnitud sísmica equivalente

- La magnitud sísmica equivalente traduce una energía sísmica en una magnitud.

💡 **Cómo se explica en la clase [B58-C16](../programa/clases/B58/B58-C16-consecuencias-geofisicas-de-impactos/CLASE.md):**
- El de 140 m libera `179 Mt`; con eficiencia sísmica ilustrativa de `10⁻⁴` su magnitud equivalente es `3.43`, y con la mitad de la energía en la onda, el frente llega a Mach 2 a `5.0 km` a los `3 s`.
- Calcular la magnitud sísmica equivalente de una energía.
- 🎯 **Por qué importa:** Las consecuencias se miden por zonas: sismo, onda de choque, calor. Las escalas con la energía son lo que permite comparar casos.
- 🔗 **Se estudia junto con:** solución de Sedov–Taylor, Mach, relaciones de Rankine–Hugoniot, radio de Mach 2.

📘 **Dónde se aprende** (1 clase): [B58-C16 · Consecuencias geofísicas de impactos](../programa/clases/B58/B58-C16-consecuencias-geofisicas-de-impactos/CLASE.md).

### Magnitudes

- Sus magnitudes son frecuencia `f`, longitud de onda `λ = c/f` y energía de cada fotón `E = h f`, con `h = 6,626 070 15 × 10⁻³⁴ J·s` (exacta, S3).

💡 **Contexto en la clase [B05-C18](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md):**
- **Idea central (modelo mental):** La misma radiación tiene dos descripciones: como onda (frecuencia, longitud de onda) y como flujo de fotones (energía por fotón). Más frecuencia, más energía por fotón.
- 🎯 **Por qué importa:** Un satélite se comunica con ondas de radio, un telescopio observa luz y rayos X, y la misma radiación a otras energías puede dañar electrónica y tejidos. La pregunta motivadora es: ¿qué es la radiación electromagnética, cómo se ordena por frecuencia y energía, cómo decae con la distancia y qué la hace peligrosa?
- 🔗 **Se estudia junto con:** onda electromagnética, fotón, intensidad o flujo, fuente isótropa.

📘 **Dónde se aprende** (1 clase): [B05-C18 · Electromagnetismo y radiación](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md).

### Makespan

- El makespan es el tiempo total.

💡 **Cómo se explica en la clase [B97-C13](../programa/clases/B97/B97-C13-ensamblaje-de-estructuras-en-orbita/CLASE.md):**
- Ejercicio 3 · casi autónomo. ¿Por qué con 1 robot el makespan es el trabajo total?
- Ejercicio 12 · integrador. Elabora tu *ficha de cronograma de ensamblaje de una armadura*: ruta crítica, makespan con 1–4 robots, cotas y eficiencia, todo rotulado como sintético.
- 🎯 **Por qué importa:** Añadir robots no acorta el trabajo indefinidamente: hay un punto en que la ruta crítica manda. Conocerlo evita lanzar una flota de robots que quedan esperando.
- 🔗 **Se estudia junto con:** tarea, ruta crítica, planificación por lista, eficiencia.

📘 **Dónde se aprende** (1 clase): [B97-C13 · Ensamblaje de estructuras en órbita](../programa/clases/B97/B97-C13-ensamblaje-de-estructuras-en-orbita/CLASE.md).

### Mal condicionado

- Un sistema mal condicionado es aquel cuya solución cambia mucho ante cambios pequeños de los datos.
- Un problema bien planteado puede ser mal condicionado: pequeñas variaciones de los datos producen variaciones grandes de la solución; un número de condición grande lo indica (S1).

💡 **Cómo se explica en la clase [B04-C03](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md):**
- F -->|Sí| G["Mal condicionado: error amplificado"]
- Todos dan lo mismo si el sistema es bien condicionado.
- 🎯 **Por qué importa:** Un detector no entrega «brillo»: entrega cuentas. Para convertir cuentas en flujo hay que descubrir dos números, una pendiente y un desfase, y para ello se miden dos fuentes de referencia.
- 🔗 **Se estudia junto con:** sistema de ecuaciones, lineal, solución, compatible determinado.

📘 **Dónde se aprende** (2 clases): [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md); [B22-C01 · Problemas directos e inversos y mal condicionamiento](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md).

### Mal condicionamiento

- El mal condicionamiento mide la amplificación del error.

💡 **Contexto en la clase [B71-C12](../programa/clases/B71/B71-C12-argumento-del-periapsis/CLASE.md):**
- 🎯 **Por qué importa:** Un elemento mal condicionado puede dar un valor sin sentido aunque el estado sea exacto. La decisión central: ¿cuándo puedes fiarte de `ω` y qué ángulo usas cuando no?
- 🔗 **Se estudia junto con:** argumento del periapsis, argumento de latitud, inclinación crítica, elemento indefinido.

📘 **Dónde se aprende** (1 clase): [B71-C12 · Argumento del periapsis](../programa/clases/B71/B71-C12-argumento-del-periapsis/CLASE.md).

### Mal planteado

- Si falla alguna, está mal planteado.

💡 **Cómo se explica en la clase [B22-C01](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md):**
- Fíjate en el orden de la cadena: el problema es «bien planteado» según Hadamard (existe, es única y es continua) y, sin embargo, mal condicionado, que es lo que realmente impide usarlo.
- En (b) formalmente se cumplen las tres, y esa es la diferencia entre mal planteado y mal condicionado (sección 6).
- ⚠️ **Error frecuente:** Confundir mal planteado con mal condicionado. Se corrige con el ejercicio 2(b).
- 🎯 **Por qué importa:** Un telescopio nunca entrega la imagen verdadera del cielo: la entrega emborronada por su respuesta óptica y con ruido. Calcular lo que verá el telescopio si conoces el objeto es fácil; el camino contrario, recuperar el objeto desde lo que vio, es el que interesa a la ciencia y el que se complica.
- 🔗 **Se estudia junto con:** problema directo, problema inverso, incógnita, datos.

📘 **Dónde se aprende** (1 clase): [B22-C01 · Problemas directos e inversos y mal condicionamiento](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md).

### Mala especificación

- La mala especificación del modelo.

💡 **Contexto en la clase [B33-C12](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md):**
- **Idea central (modelo mental):** Un reloj adelantado o atrasado tiene un sesgo constante, y su error depende de cuánto se desvíe.
- 🎯 **Por qué importa:** Saber cómo falla un modelo orienta su mejora. La decisión central: ¿qué sesgo y qué precisión tiene cada especificación del arrastre?
- 🔗 **Se estudia junto con:** sesgo, MAE, RMSE, ventana de acierto.

📘 **Dónde se aprende** (1 clase): [B33-C12 · Pronóstico de llegada y severidad de CME](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md).

### Malentendido

- Un malentendido es un comentario que surge de una lectura errónea del texto.

💡 **Cómo se explica en la clase [B20-C03](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md):**
- Antes de contestar, numera cada comentario y asígnale una de cuatro clases: mayor (afecta una conclusión), menor (forma, aclaración), malentendido (el texto no era claro o fue mal leído) y fuera de alcance.
- Un malentendido es casi siempre una señal de que tu texto debe aclararse, aunque tengas razón.
- 🎯 **Por qué importa:** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.
- 🔗 **Se estudia junto con:** revisión por pares, autor, árbitro, editor.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Malla

- Una malla es el conjunto de nodos `x_i = i h`, `h = L/N`.
- Una malla es una superficie tejida que refleja a radiofrecuencia y pesa poco.
- Una malla uniforme tiene nodos `x_i = i Δx`, `Δx = L/N`, e instantes `t^n = n Δt`;
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C12](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md):**
- Diferencias finitas: robusto para problemas lineales y para mallas con muchos nodos; produce toda la solución a la vez.
- El método de diferencias finitas es distinto: se pide a todos los puntos de la malla que se acomoden a la vez entre las dos paredes.
- 🎯 **Por qué importa:** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.
- 🔗 **Se estudia junto con:** problema de frontera, Dirichlet, Neumann, mixtas.

📘 **Dónde se aprende** (4 clases): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md); [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md); [B11-C15 · Elementos finitos introductorios](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md); [B91-C04 · Antenas desplegables y estructuras de gran apertura](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md).

### Malla adaptativa

- Una malla adaptativa (AMR, *adaptive mesh refinement*) cambia su resolución durante el cálculo.

💡 **Cómo se explica en la clase [B21-C05](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md):**
- Una malla uniforme con ese error necesita 2 048 celdas; la adaptativa, 96.
- Descripción larga: al aumentar los niveles permitidos, el error de la malla adaptativa baja hasta quedar fijo en `C/2 = 0,025`, y el número de celdas se estabiliza en 96; la uniforme necesitaría 2 048.
- 🎯 **Por qué importa:** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.
- 🔗 **Se estudia junto con:** nivel, criterio de refinamiento, suavizado de malla, restricción.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Malla colocada

- Una malla colocada guarda todas las variables en los mismos puntos.

💡 **Cómo se explica en la clase [B21-C04](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md):**
- Se usa una malla colocada con `N × N` puntos en el cuadrado periódico `[0, 2π)²`, `h = 2π/N`.
- La malla colocada con diferencias centradas puede admitir modos de damero en la presión; con campos suaves no se excitan, pero un flujo con escalones sí podría excitarlos (por eso muchos códigos usan mallas desplazadas).
- 🎯 **Por qué importa:** Un fluido aparece en casi toda la ingeniería aeroespacial: el aire alrededor de un cohete, el propelente que se mueve en un tanque, el refrigerante de un satélite.
- 🔗 **Se estudia junto con:** ecuaciones de Navier–Stokes, ecuaciones de Euler, incompresible, viscosidad cinemática.

📘 **Dónde se aprende** (1 clase): [B21-C04 · Ecuaciones de Navier-Stokes y dinámica de fluidos computacional](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md).

### Malla completa

- La malla completa tiene `n(n−1)/2` enlaces; el anillo, `n`; la estrella, `n − 1`.

💡 **Contexto en la clase [B88-C31](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md):**
- 🎯 **Por qué importa:** Una red con un enlace crítico único pierde un subsistema entero con una sola falla. La decisión central: ¿qué topología da la tolerancia y la latencia necesarias con el menor número de enlaces?
- 🔗 **Se estudia junto con:** topología, diámetro, saltos medios, puente.

📘 **Dónde se aprende** (1 clase): [B88-C31 · Topologías de red de datos a bordo](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md).

### Malla escalonada

- Una malla escalonada coloca `v` y `b` en puntos distintos.

💡 **Contexto en la clase [B35-C10](../programa/clases/B35/B35-C10-condiciones-de-frontera-en-modelos-mhd/CLASE.md):**
- **Idea central (modelo mental):** Una frontera rígida devuelve un eco; una frontera que absorbe como un acantilado de arena deja pasar el sonido sin eco. En un modelo, el eco es una onda falsa que contamina la solución.
- 🎯 **Por qué importa:** Las fronteras de los modelos heliosféricos deben dejar salir las ondas. La decisión central: ¿refleja la frontera la onda y con qué signo y amplitud?
- 🔗 **Se estudia junto con:** condición de pared, gradiente nulo, característica saliente, coeficiente de reflexión.

📘 **Dónde se aprende** (1 clase): [B35-C10 · Condiciones de frontera en modelos MHD](../programa/clases/B35/B35-C10-condiciones-de-frontera-en-modelos-mhd/CLASE.md).

### Malla fina

- La malla fina es la de menor `h`.

💡 **Cómo se explica en la clase [B84-C26](../programa/clases/B84/B84-C26-generacion-de-mallas-y-convergencia-en-elementos-finitos/CLASE.md):**
- Se reporta el valor de la malla fina, `p`, la extrapolación y el GCI; si `p` difiere mucho del teórico se investiga (singularidad, malla pobre).
- Extrapolar con Richardson al límite de malla infinitamente fina.
- 🎯 **Por qué importa:** Una malla más gruesa puede errar 30 % en tensión sin que el resultado «parezca» mal; la convergencia dice cuánto y cuánto refinar. La decisión central: ¿cuántos elementos hacen falta para que la magnitud de interés cambie menos que una tolerancia dada?
- 🔗 **Se estudia junto con:** orden observado, Richardson, GCI.

📘 **Dónde se aprende** (1 clase): [B84-C26 · Generación de mallas y convergencia en elementos finitos](../programa/clases/B84/B84-C26-generacion-de-mallas-y-convergencia-en-elementos-finitos/CLASE.md).

### Mancha

- Una mancha es una región de la fotosfera más fría que su entorno por un campo magnético intenso que inhibe la convección.

💡 **Cómo se explica en la clase [B24-C12](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md):**
- Con `T_m = 4500 K` y `T_ef = 5772 K`, `c = (4500/5772)⁴ = 0,369`: la mancha emite el `37 %` de lo que emite su entorno.
- Si una mancha circular de radio angular `ρ` está en el centro del disco, su área proyectada es la de un disco de radio `R sen ρ`, `π R² sen²ρ`, y el flujo total del disco sin manchas es `π R²` (sin oscurecimiento al limbo).
- 🎯 **Por qué importa:** La modulación del brillo por manchas permite medir el periodo de rotación de miles de estrellas sin necesitar espectros, pero también contamina la búsqueda de exoplanetas y limita la precisión de las velocidades radiales.
- 🔗 **Se estudia junto con:** contraste, modulación rotacional, radio angular, periodograma.

📘 **Dónde se aprende** (1 clase): [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md).

### Manchas solares

- Las manchas solares son zonas oscuras en la superficie del Sol.
- Las manchas solares son zonas oscuras de la superficie; el número de manchas es un índice de actividad que publica el centro SILSO (S5).

💡 **Cómo se explica en la clase [B02-C13](../programa/clases/B02/B02-C13-galileo-y-primeras-observaciones-telescopicas/CLASE.md):**
- S3 indica que Galileo vio manchas pequeñas jamás vistas y observó que el ancho de las líneas oscuras que las rodean cambiaba con el ángulo de la luz solar, de lo que concluyó que eran sombras y que la superficie lunar tiene montañas y valles.
- S4 recoge una polémica con Christoph Scheiner por las manchas solares: Scheiner sostuvo que eran satélites muy cercanos al Sol, preservando la perfección solar;
- 🎯 **Por qué importa:** Un instrumento nuevo da datos nuevos, pero los datos nuevos no se interpretan solos. La pregunta motivadora es: ¿qué podía concluir Galileo de lo que veía, y qué le faltaba para convencer a quienes no creían?
- 🔗 **Se estudia junto con:** telescopio refractor, ampliación, campo de visión, satélites galileanos.

📘 **Dónde se aprende** (2 clases): [B02-C13 · Galileo y primeras observaciones telescópicas](../programa/clases/B02/B02-C13-galileo-y-primeras-observaciones-telescopicas/CLASE.md); [B08-C16 · Observación solar con filtros certificados](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md).

### Manifiesto

- Un manifiesto es una lista que asigna nombres lógicos (`flujo.npy`) a hashes.
- Un manifiesto guarda la configuración, las versiones del software y la huella.
- Un manifiesto lista los archivos con su huella (C11).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C20](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md):**
- A --> F["Manifiesto:<br/>configuración + versiones + huella"]
- Ejercicio 12 · integrador. Elabora tu *propagador con pruebas y huella reproducible*: configuración inmutable, dos métodos, pruebas contra Kepler (circular y elíptica), orden de convergencia, conservación, reversibilidad, huella, manifiesto con versiones y una sección que declare qué no valida.
- 🎯 **Por qué importa:** Un resultado numérico que nadie puede reproducir no es ciencia. Si dentro de un año hay que saber por qué una trayectoria salió así, hacen falta la configuración exacta, las versiones del software y pruebas que digan si el programa sigue funcionando.
- 🔗 **Se estudia junto con:** configuración, huella, referencia independiente, prueba de regresión.

📘 **Dónde se aprende** (5 clases): [B11-C20 · Propagador reproducible de trayectoria](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md); [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md); [B14-C19 · Publicación de código y datos](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md); [B88-C18 · Control de configuración de firmware](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md); [B130-C06 · Publicación de un proyecto educativo](../programa/clases/B130/B130-C06-publicacion-de-un-proyecto-educativo/CLASE.md).

### Maniobra de evasión

- Una maniobra de evasión cambia la órbita para evitar una conjunción.

💡 **Cómo se explica en la clase [B118-C07](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md):**
- La directriz 3 de la COPUOS (2010, consultada) indica que, si los datos orbitales señalan una colisión potencial, se debe considerar el ajuste del instante de lanzamiento o una maniobra de evasión en órbita.
- La evidencia es la ficha de maniobra de evasión del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** La evasión es la respuesta operativa a una conjunción, pero cada maniobra cuesta combustible y vida útil. La decisión central: ¿cuánto Δv hace falta para lograr una separación dada y cuánto más cuesta decidir tarde?
- 🔗 **Se estudia junto con:** Δv, deriva a lo largo de la traza, Isp, ecuación de Tsiolkovsky.

📘 **Dónde se aprende** (1 clase): [B118-C07 · Estrategias de evasión](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md).

### Manipulabilidad w

- Singularidad: `rango(J) < 6`. Manipulabilidad `w`: `√det(J Jᵀ)`.

💡 **Cómo se explica en la clase [B101-C03](../programa/clases/B101/B101-C03-singularidades-y-manipulabilidad-de-brazos-roboticos/CLASE.md):**
- Manipulabilidad `w`: el volumen de la elipse (esta clase).
- Calcular el índice de manipulabilidad `w = √det(J Jᵀ)` y compararlo con el valor analítico de un brazo planar.
- 🎯 **Por qué importa:** Con el brazo casi estirado, pedirle un movimiento de 5 cm/s a lo largo de su eje exige velocidades articulares de varios rad/s. La decisión central: ¿cuán cerca de una singularidad estoy y qué error de seguimiento acepto para no exigir lo imposible?
- 🔗 **Se estudia junto con:** Jacobiano geométrico, Singularidad, Valor singular σ, Número de condición.

📘 **Dónde se aprende** (1 clase): [B101-C03 · Singularidades y manipulabilidad de brazos robóticos](../programa/clases/B101/B101-C03-singularidades-y-manipulabilidad-de-brazos-roboticos/CLASE.md).

### Maniquí

- Un maniquí es un modelo físico del paciente.

💡 **Cómo se explica en la clase [B117-C01](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md):**
- Un estudio en maniquí en vuelos parabólicos (comunicado del 2025-08-27) midió profundidades de compresión medianas de 34,5 mm con el método manual «handstand», 53,0 mm con un pistón mecánico estándar y 29 mm con otros dos dispositivos, con unos 22 s de microgravedad por parábola.
- Comparar un método manual con un dispositivo mecánico con datos de maniquí.
- ⚠️ **Error frecuente:** Creer que las medianas de maniquí describen a pacientes. Se corrige con la sección 11.
- 🎯 **Por qué importa:** Ninguna clase anterior trata primeros auxilios en microgravedad. La decisión central: ¿cuánto tiempo puede sostener un reanimador una compresión de calidad y cuándo hay que relevarlo?
- 🔗 **Se estudia junto con:** profundidad de compresión, fatiga, tiempo de calidad, relevo.

📘 **Dónde se aprende** (1 clase): [B117-C01 · Primeros auxilios y procedimientos básicos en entorno espacial](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md).

### Mano de obra mínima

- aceptación el de la unidad de vuelo; mano de obra mínima (*workmanship*) el nivel mínimo para detectar defectos de fabricación.

💡 **Cómo se explica en la clase [B84-C01](../programa/clases/B84/B84-C01-entorno-mecanico-de-lanzamiento/CLASE.md):**
- Predice antes de ejecutar: ¿qué `g` rms dará el perfil de mano de obra mínima?
- Mano de obra minima (Tabla 2.4-4) 6.784 6.8 -0.016
- 🎯 **Por qué importa:** Un satélite no falla en órbita por el empuje del motor sino por la sacudida de la subida; esa sacudida se especifica con un espectro, no con un número. Un espectro con 0,16 g²/Hz de meseta no dice nada hasta que se integra.
- 🔗 **Se estudia junto con:** ASD, valor eficaz, Calificación, aceptación.

📘 **Dónde se aprende** (1 clase): [B84-C01 · Entorno mecánico de lanzamiento](../programa/clases/B84/B84-C01-entorno-mecanico-de-lanzamiento/CLASE.md).

### Manta multicapa (MLI)

- La manta multicapa (MLI) es un apilado de láminas reflectantes separadas por espaciadores.

💡 **Cómo se explica en la clase [B85-C06](../programa/clases/B85/B85-C06-aislamiento-multicapa/CLASE.md):**
- La evidencia es la ficha de dimensionado de una manta multicapa del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de dimensionado de una manta multicapa*: `q`, `ε_eff` y temperaturas para `N` capas, número de capas para un objetivo, efecto de la compresión y lista de lo consultado e ilustrativo.
- 🎯 **Por qué importa:** Aislar una caja que opera a `300 K` de un entorno a `100 K` con una sola superficie cuesta cientos de W/m²; con unas pocas capas cuesta unidades. La decisión central: ¿cuántas capas y de qué emisividad hacen falta para limitar el flujo, y cuánto se pierde si se comprimen?
- 🔗 **Se estudia junto con:** emisividad efectiva, compresión.

📘 **Dónde se aprende** (1 clase): [B85-C06 · Aislamiento multicapa](../programa/clases/B85/B85-C06-aislamiento-multicapa/CLASE.md).

### Mantenimiento

- El mantenimiento es el conjunto de maniobras que mantiene la órbita cerca de la referencia.

💡 **Cómo se explica en la clase [B76-C19](../programa/clases/B76/B76-C19-orbitas-de-mantenimiento/CLASE.md):**
- La evidencia es la ficha de una campaña de mantenimiento del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de una campaña de mantenimiento*: crecimiento sin control, impulsos, desviación con control y límites, con fuentes.
- 🎯 **Por qué importa:** Una órbita periódica inestable no se mantiene sola. La decisión central: ¿con qué frecuencia y qué impulso hay que corregir para que el error no crezca?
- 🔗 **Se estudia junto con:** apuntamiento, error de ejecución, cociente de desviaciones.

📘 **Dónde se aprende** (1 clase): [B76-C19 · Órbitas de mantenimiento](../programa/clases/B76/B76-C19-orbitas-de-mantenimiento/CLASE.md).

### Mantisa

- La mantisa `m` cumple `1 ≤ |m| < 10` en la forma normalizada; el exponente `e` es un entero.

💡 **Cómo se explica en la clase [B03-C05](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md):**
- Se multiplican las mantisas y se suman los exponentes: `(2 × 10⁵)(3 × 10⁻³) = 6 × 10²`.
- Al dividir, se dividen mantisas y se restan exponentes.
- ⚠️ **Error frecuente:** Mantisa fuera de rango (`20 × 10⁵`).
- 🎯 **Por qué importa:** Las fichas de la NASA publican las masas en «10²⁴ kg»: la Tierra es 5,9722, el Sol 1 988 400. Si no sabes leer ese `10²⁴`, tampoco sabrás si 1 988 400 es «un poco más» o «mucho más».
- 🔗 **Se estudia junto con:** notación científica, normalizada, exponente, orden de magnitud.

📘 **Dónde se aprende** (1 clase): [B03-C05 · Notación científica y órdenes de magnitud](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md).

### Manto

- La superficie es la capa química activa en contacto con el gas (aquí, una monocapa); el manto es el hielo enterrado bajo ella.

💡 **Cómo se explica en la clase [B60-C04](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md):**
- El de dos fases libera todo entre 20 y 25 K; el de tres fases libera la superficie y deja el manto, que sale con la lentitud del intercambio.
- Según el resumen consultado de Ruaud, Wakelam y Hersant (2016), su modelo Nautilus de tres fases trata superficie y manto como químicamente activos con reacción, difusión y evaporación, y reporta efectos sobre las abundancias de superficie y gas frente al de dos fases.
- 🎯 **Por qué importa:** Un modelo de dos fases trata todo el hielo como si estuviera expuesto en la superficie; en la realidad la mayor parte queda enterrada bajo capas posteriores. La decisión central: ¿qué cambia en la predicción de cuánto hielo se libera al calentar si se distingue la superficie del manto?
- 🔗 **Se estudia junto con:** acreción, desorción térmica, superficie, modelo de tres fases.

📘 **Dónde se aprende** (1 clase): [B60-C04 · Balance químico gas-grano: modelos de tres fases](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md).

### Manto de ejecta

- El manto de ejecta es el depósito continuo; la ejecta distal es la que llega más lejos.

💡 **Cómo se explica en la clase [B61-C04](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md):**
- La evidencia es la ficha del manto de ejecta del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha del manto de ejecta*: ley de espesor, volumen del manto, razón con el bol, exponente derivado de la balística y su comparación con −3, con rótulos.
- 🎯 **Por qué importa:** El manto de ejecta es un marcador estratigráfico: cubre lo anterior y es cubierto por lo posterior. La decisión central: ¿cómo decae el espesor con la distancia y cuánto volumen contiene el manto?
- 🔗 **Se estudia junto con:** ejecta distal, espesor en el borde, estratigrafía invertida, ley de −3.

📘 **Dónde se aprende** (1 clase): [B61-C04 · Mantos de ejecta y depósitos de impacto](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md).

### Mapa

- El mapa de Tisserand reúne las curvas de `T` constante de cada planeta.

💡 **Cómo se explica en la clase [B75-C08](../programa/clases/B75/B75-C08-secuencias-multiples-de-sobrevuelos/CLASE.md):**
- Por mapa: las curvas de `T` constante en el plano perihelio–afelio.
- La evidencia es tu mapa de Tisserand de una secuencia del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Una misión que usa sobrevuelos de la Tierra, Venus o Júpiter no puede ir a cualquier órbita: depende del `v∞` con el que llega a cada planeta. La decisión central: ¿qué órbitas puede alcanzar una nave con un sobrevuelo de un planeta y cuánto `v∞` hace falta para llegar a una órbita dada?
- 🔗 **Se estudia junto con:** parámetro de Tisserand, conserva, cadena de sobrevuelos.

📘 **Dónde se aprende** (1 clase): [B75-C08 · Secuencias múltiples de sobrevuelos](../programa/clases/B75/B75-C08-secuencias-multiples-de-sobrevuelos/CLASE.md).

### Mapa de bytes

- El mapa de bytes es la lista de intervalos `(inicio, fin)` de cada campo.

💡 **Cómo se explica en la clase [B88-C21](../programa/clases/B88/B88-C21-interfaces-y-documentos-de-control-de-software-de-vuelo/CLASE.md):**
- *Descripción textual:* la misma tabla alimenta al productor y al consumidor; los bytes viajan entre ellos y los mapas de bytes se comparan para detectar desfases.
- Comparar mapas de bytes productor–consumidor.
- 🎯 **Por qué importa:** La mayoría de los errores de integración nacen en la interfaz: un campo de otro ancho, un orden de bytes invertido o una unidad distinta. La decisión central: ¿la tabla de interfaz deja un solo significado posible para cada bit?
- 🔗 **Se estudia junto con:** campo, orden de bytes, cuantización, ICD.

📘 **Dónde se aprende** (1 clase): [B88-C21 · Interfaces y documentos de control de software de vuelo](../programa/clases/B88/B88-C21-interfaces-y-documentos-de-control-de-software-de-vuelo/CLASE.md).

### Mapa de error de forma

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B43-C22](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md):**
- python programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/interferometria.py
- 🎯 **Por qué importa:** El mapa de error de forma es la prueba de aceptación de un espejo. La decisión central: ¿cómo se recupera la fase, qué se descuenta y qué PV y RMS quedan?
- 🔗 **Se estudia junto con:** desplazamiento de fase, fase, desenvolvimiento, ajuste de modos.

📘 **Dónde se aprende** (1 clase): [B43-C22 · Interferometría de superficie y mapas de error de forma](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md).

### Mapa de flujo

- El mapa de flujo da la tasa de dosis en cada longitud y latitud; aquí es una gaussiana centrada en `(−45°, −25°)` que crece con `exp((h − 500 km)/250 km)`.

💡 **Cómo se explica en la clase [B85-C22](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md):**
- Mapa de flujo SINTETICO (anomalia gaussiana en lon -45, lat -25; crece con exp(h/250 km));
- 🎯 **Por qué importa:** La dosis anual decide el blindaje y la vida de la electrónica y los materiales. La decisión central: ¿cuánta dosis acumula una órbita al año y cuánto la reduce un milímetro más de blindaje?
- 🔗 **Se estudia junto con:** curva dosis-profundidad, promedio orbital, inclinación.

📘 **Dónde se aprende** (1 clase): [B85-C22 · Modelos de exposición a radiación en órbita](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md).

### Mapa estándar

- El mapa estándar es `p' = p + K sen θ`, `θ' = θ + p'` (módulo `2π`).

💡 **Cómo se explica en la clase [B73-C13](../programa/clases/B73/B73-C13-caos-determinista/CLASE.md):**
- I["(theta, p) y copia a 1e-10"] --> M["mapa estandar con K"]
- Con el mapa estándar, dos trayectorias que parten a `10⁻¹⁰` terminan separadas `5,20e-02` a las 20 iteraciones si `K = 5` y solo `2,9e-08` a las 40 si `K = 0,5`.
- 🎯 **Por qué importa:** Un sistema determinista puede ser impredecible a largo plazo: el error de medida se amplifica exponencialmente y fija un horizonte más allá del cual la predicción no vale, por más cómputo que se use. La decisión central: ¿hasta cuándo puedo confiar en una integración y cómo reconozco el régimen caótico?
- 🔗 **Se estudia junto con:** régimen regular, caótico, horizonte de predicción, reversibilidad.

📘 **Dónde se aprende** (1 clase): [B73-C13 · Caos determinista](../programa/clases/B73/B73-C13-caos-determinista/CLASE.md).

### Mapa inverso

- El mapa inverso pasa de la imagen distorsionada a la ideal.

💡 **Cómo se explica en la clase [B50-C08](../programa/clases/B50/B50-C08-distorsion-geometrica-y-su-calibracion/CLASE.md):**
- En la esquina (15, 15) mm la distorsión desplaza la estrella `0,2578 mm` y el mapa inverso la recupera con error `2,5 × 10⁻¹⁵ mm`.
- 🎯 **Por qué importa:** En astrometría y en mosaicos una distorsión de 0,1 % mueve las estrellas decenas de píxeles. La decisión central: ¿qué modelo describe la distorsión y con qué precisión se puede calibrar?
- 🔗 **Se estudia junto con:** distorsión, de barril, de cojín, modelo radial.

📘 **Dónde se aprende** (1 clase): [B50-C08 · Distorsión geométrica y su calibración](../programa/clases/B50/B50-C08-distorsion-geometrica-y-su-calibracion/CLASE.md).

### Mapeo

- El mapeo asocia un valor a un tono.

💡 **Cómo se explica en la clase [B128-C07](../programa/clases/B128/B128-C07-modelos-tactiles-y-sonificacion/CLASE.md):**
- La decisión de qué mapeo es más comprensible requiere probarlo con personas; esta clase no lo hizo.
- Límite: la elección de mapeo (subir el tono con el brillo) es una convención que debe explicarse; no es universal.
- ⚠️ **Error frecuente:** Dar el mapeo por universal. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Un mapeo sin reglas explícitas engaña: si la escala de tono se estira para que se oiga una caída de 1 %, el oyente puede creer que la caída fue enorme. La decisión central: ¿qué se mapea a qué, con qué escala, y cómo se avisa de la amplificación?
- 🔗 **Se estudia junto con:** sonificación, semitono, relieve, cuantización.

📘 **Dónde se aprende** (1 clase): [B128-C07 · Modelos táctiles y sonificación](../programa/clases/B128/B128-C07-modelos-tactiles-y-sonificacion/CLASE.md).

### Maqueta a escala

- Una maqueta a escala conserva todas las razones entre longitudes.

💡 **Cómo se explica en la clase [B03-C20](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md):**
- Solución habitual: dos maquetas (una de distancias y otra de tamaños) o aceptar una escala distinta para los tamaños, declarándolo.
- *Descripción textual:* de los requisitos se calcula el factor de escala; con él se construye la tabla de maqueta; la tabla pasa por tres verificaciones (razones, Kepler y espacio/tiempo de luz); y todo se resume en un informe con límites y conflictos.
- 🎯 **Por qué importa:** Un ingeniero no recibe un ejercicio con una sola fórmula: recibe requisitos («que quepa en un patio de 350 m», «que se vea el Sol», «que Neptuno esté a su sitio») y debe decidir qué se puede cumplir y qué no.
- 🔗 **Se estudia junto con:** requisito, componente, criterio de comprobación, factor de escala.

📘 **Dónde se aprende** (1 clase): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md).

### Máquina de estados

- Una máquina de estados es un conjunto finito de estados y una función de transición `(estado, evento) → estado`.

💡 **Cómo se explica en la clase [B98-C02](../programa/clases/B98/B98-C02-sistemas-de-decision-autonomos-y-maquinas-de-estados-de-comportamiento/CLASE.md):**
- Límite: el rover real tiene muchos más estados y eventos asíncronos, y varios subsistemas con sus propias máquinas.
- python programa/clases/B98/B98-C02-sistemas-de-decision-autonomos-y-maquinas-de-estados-de-comportamiento/maquina_estados.py
- 🎯 **Por qué importa:** Una cadena de `if` crece sin control y nadie puede decir si un estado inseguro es alcanzable. La decisión central: ¿cómo se estructura la decisión para que se pueda comprobar que nunca se conduce sin energía ni se sale del modo seguro sin orden de Tierra?
- 🔗 **Se estudia junto con:** guarda, modo seguro, árbol de comportamiento, invariante.

📘 **Dónde se aprende** (1 clase): [B98-C02 · Sistemas de decisión autónomos y máquinas de estados de comportamiento](../programa/clases/B98/B98-C02-sistemas-de-decision-autonomos-y-maquinas-de-estados-de-comportamiento/CLASE.md).

### Marca falsa

- La marca falsa es una lectura marcada como anómala que en realidad es normal y solo está desplazada por el ruido.

💡 **Cómo se explica en la clase [B116-C02](../programa/clases/B116/B116-C02-signos-vitales-medicion-interpretacion-y-limites/CLASE.md):**
- Reducir el ruido de 0,2 a 0,05 °C baja la marca falsa del 31 % al 2,3 %.
- *Descripción textual:* el valor verdadero se mide con ruido; la lectura se compara con un rango poblacional o con la línea base personal; ambas dan marcas con distinta sensibilidad y distintas falsas alarmas.
- ⚠️ **Error frecuente:** Ignorar el ruido cerca del borde. Calcula la marca falsa (8.3).
- 🎯 **Por qué importa:** Un panel que marca en rojo todo lo que sale de «60–100 lpm» genera cientos de marcas por ruido en una persona sana, y puede no ver que un atleta con 52 lpm pasó a 64: sigue «dentro del rango». La decisión central: ¿con respecto a qué se compara una medida y cuánto de la desviación es ruido?
- 🔗 **Se estudia junto con:** signos vitales, rango de referencia, presión de pulso, presión arterial media.

📘 **Dónde se aprende** (1 clase): [B116-C02 · Signos vitales: medición, interpretación y límites](../programa/clases/B116/B116-C02-signos-vitales-medicion-interpretacion-y-limites/CLASE.md).

### Marcador

- El marcador es un elemento del lugar (un agujero, una cumbre) usado para seguir el orto.

💡 **Cómo se explica en la clase [B133-C01](../programa/clases/B133/B133-C01-relaciones-entre-cielo-y-territorio-en-los-saberes-tradicionales/CLASE.md):**
- La evidencia es la ficha de un marcador solar sintético con su ventana de incertidumbre del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de un marcador solar sintético con su ventana de incertidumbre*: tabla de `A` para los tres horizontes, `x` del rayo, ventana de días indistinguibles para el umbral que elijas, la segunda vía y una lista de qué es documentado, qué es modelo y qué no se sabe.
- 🎯 **Por qué importa:** Los saberes del cielo se enseñan a menudo como listas de constelaciones o de relatos sueltos, sin el territorio que los sostiene. La decisión central: ¿qué puede decir una geometría astronómica sobre una práctica ligada a un lugar, y qué le corresponde decir solo a quienes la portan?
- 🔗 **Se estudia junto con:** acimut, declinación, elevación del horizonte, orto.

📘 **Dónde se aprende** (1 clase): [B133-C01 · Relaciones entre cielo y territorio en los saberes tradicionales](../programa/clases/B133/B133-C01-relaciones-entre-cielo-y-territorio-en-los-saberes-tradicionales/CLASE.md).

### Marcador de sincronización de palabra

- El marcador de sincronización de palabra (CSM) son `W` símbolos PPM antepuestos a cada palabra.

💡 **Contexto en la clase [B92-C06](../programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/CLASE.md):**
- 🎯 **Por qué importa:** En un canal con pocos fotones, la eficiencia es bits por fotón, no bits por hercio. La decisión central: ¿qué orden PPM y qué tasa de código elegir para equilibrar tasa de información, fotones por bit y potencia de pico?
- 🔗 **Se estudia junto con:** orden PPM, ranura de guarda, tasa de código, bloque de información.

📘 **Dónde se aprende** (1 clase): [B92-C06 · Modulación y codificación en enlaces ópticos](../programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/CLASE.md).

### Marcar

- El piso de escala (0,10 mag) impide dividir por una escala diminuta. Marcar no es borrar: el dato queda con una etiqueta para su revisión.

💡 **Contexto en la clase [B129-C04](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR R["Registro voluntario"] --> E["Esquema y rangos"] E --> D["Duplicados"] D --> A["Atipicos robustos MAD"] A --> OK["Aceptado"] E --> X["Marcado para revision"] D --> X A --> X ``` *Descripción textual:* cada registro pasa por tres etapas; en cualquiera de ellas puede quedar marcado para revisión, y si las supera se acepta.
- 🎯 **Por qué importa:** Un lote de contribuciones trae errores de tecleo, duplicados, fechas imposibles y mediciones erróneas. La decisión central: ¿qué filtro aplicar para atrapar los errores sin tirar datos buenos, y cómo se sabe que funciona?
- 🔗 **Se estudia junto con:** esquema, duplicado, valor atípico, escala robusta.

📘 **Dónde se aprende** (1 clase): [B129-C04 · Contribución de medidas voluntarias con control de calidad](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md).

### Marcha aleatoria

- La marcha aleatoria es un recorrido de pasos de dirección al azar.
- La marcha aleatoria de fase y el puente browniano.

💡 **Cómo se explica en la clase [B24-C05](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md):**
- En una marcha aleatoria de `N` pasos de longitud `ℓ`, la distancia cuadrática media es `⟨r²⟩ = Nℓ²`.
- Un fotón producido en el centro del Sol avanza solo una distancia minúscula antes de ser absorbido y reemitido en otra dirección, de modo que sigue una marcha aleatoria.
- 🎯 **Por qué importa:** La energía generada en el núcleo tarda milenios en salir y el modo de transporte decide la estructura: si el interior de una estrella es convectivo, su composición se mezcla; si es radiativo, no. De ello depende cuánto combustible alcanza el núcleo, y por tanto la vida de la estrella.
- 🔗 **Se estudia junto con:** recorrido libre medio, tiempo de difusión, gradiente adiabático, gradiente radiativo.

📘 **Dónde se aprende** (2 clases): [B24-C05 · Transporte radiativo y convectivo](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md); [B46-C17 · Calibración de fase](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md).

### Marcha aleatoria de frecuencia

- La marcha aleatoria de frecuencia (pendiente +1/2).

💡 **Cómo se explica en la clase [B46-C08](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md):**
- Con 65 536 muestras sintéticas, el ruido blanco de frecuencia tiene pendiente `-0,498` y la marcha aleatoria `0,459`; ambas vías coinciden a 10⁻⁹.
- 🎯 **Por qué importa:** El tiempo de coherencia de un instrumento depende de cómo se acumula el error de un oscilador. La decisión central: ¿a qué escala de tiempo domina cada tipo de ruido y cuánto se puede integrar?
- 🔗 **Se estudia junto con:** frecuencia fraccional, error de tiempo, varianza de Allan, ruido blanco de frecuencia.

📘 **Dónde se aprende** (1 clase): [B46-C08 · Osciladores y estabilidad](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md).

### Marco {0}

- Transformación homogénea: matriz `T = [R p; 0 1]` de 4×4. Marco `{0}`: marco de la base.

💡 **Cómo se explica en la clase [B101-C01](../programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/CLASE.md):**
- B["Marco 0<br/>base"] -->|"T1(q1)"| M1["Marco 1"]
- M6 -->|"T7(q7)"| E["Marco E<br/>extremo"]
- 🎯 **Por qué importa:** Para mover un brazo hay que saber dónde está su extremo. Si el marco de cada eslabón está mal puesto, todo lo que sigue (cinemática inversa, singularidades, calibración) hereda el error.
- 🔗 **Se estudia junto con:** Transformación homogénea, Marco {E}, Parámetros D-H, Cinemática directa.

📘 **Dónde se aprende** (1 clase): [B101-C01 · Transformaciones homogéneas y parametrización de eslabones (Denavit-Hartenberg)](../programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/CLASE.md).

### Marco Celeste de Referencia Internacional (ICRF)

- El Marco Celeste de Referencia Internacional (ICRF) es su realización: un conjunto de coordenadas precisas de fuentes extragalácticas compactas de radio, medidas con interferometría de línea de base muy larga (VLBI) (S1, 2.2).

💡 **Contexto en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
- **Idea central (modelo mental):** Imagina fijar un mapa a las fuentes más lejanas, que casi no se mueven. Las coordenadas de cada cuásar son las marcas del mapa; los ejes salen de ellas. Cualquier dirección que midas es relativa a esas marcas; cualquier error común de las marcas es un giro de todo el mapa.
- 🎯 **Por qué importa:** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.
- 🔗 **Se estudia junto con:** Sistema Celeste de Referencia Internacional (ICRS), fuente definidora, cuásar, suelo de ruido.

📘 **Dónde se aprende** (1 clase): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### Marco de referencia

- Un marco de referencia es el conjunto de convenciones que permite asignar una posición: un origen, unos ejes, una unidad y un sentido positivo.
- Un marco de referencia es un conjunto de ejes coordenados ligado a un punto; el subsistema de marcos de SPICE define cómo se relacionan para que las transformaciones sean automáticas (S2).
- El marco de referencia (por ejemplo, el ICRS) fija dónde están el ecuador, los ejes y el origen; la época dice a qué fecha se refieren las posiciones, porque las estrellas se mueven.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- Un marco de referencia fija cuatro cosas: un origen, la orientación de sus ejes, una unidad y un sentido positivo.
- Describir un marco de referencia con origen, ejes, unidad y convención de signo.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).
- 🔗 **Se estudia junto con:** ciclo, período, día solar medio, día sidéreo.

📘 **Dónde se aprende** (5 clases): [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md); [B10-C16 · Transformación de marcos de referencia](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md); [B14-C21 · Datos de misiones planetarias: PDS4, etiquetas y SPICE](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Marco de referencia inercial

- Un marco de referencia inercial es uno donde un cuerpo libre se mueve en línea recta con rapidez constante; lo definimos con rigor en C04.

💡 **Contexto en la clase [B05-C02](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md):**
- **Idea central (modelo mental):** Solo se mide posición contra tiempo. Todo lo demás se deduce de esa tabla, igual que una película da la rapidez de un coche a partir de fotogramas.
- 🎯 **Por qué importa:** Cuando una agencia dice que un satélite «va a 7,7 km/s», ¿respecto de qué y en qué dirección? La pregunta motivadora es: ¿cómo describo un movimiento de forma que otra persona lo reconstruya sin ambigüedad?
- 🔗 **Se estudia junto con:** posición, desplazamiento, distancia recorrida, velocidad media.

📘 **Dónde se aprende** (1 clase): [B05-C02 · Posición, velocidad y aceleración](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md).

### Marco del cuerpo

- Deriva: error acumulado al integrar movimientos (F6). Marco del cuerpo: ejes fijos al robot.

💡 **Cómo se explica en la clase [B99-C01](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md):**
- Dadas dos nubes de puntos `P` (instante `k`) y `Q` (instante `k+1`), ambas en el marco del cuerpo, se busca `Q ≈ R P + t`.
- 🎯 **Por qué importa:** Una trayectoria se obtiene sumando movimientos pequeños, y cada uno trae un error; esos errores no se corrigen solos. La decisión central: ¿con qué calidad de correspondencias y de medida puedo confiar en la odometría, y cuándo necesito corregirla con cierres de bucle (C04)?
- 🔗 **Se estudia junto con:** Odometría visual, Correspondencia, Ajuste de cuerpo rígido, RANSAC.

📘 **Dónde se aprende** (1 clase): [B99-C01 · Odometría visual](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md).

### Marco {E}

- Marco `{0}`: marco de la base. Marco `{E}`: marco del extremo.

💡 **Cómo se explica en la clase [B101-C01](../programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/CLASE.md):**
- B["Marco 0<br/>base"] -->|"T1(q1)"| M1["Marco 1"]
- M6 -->|"T7(q7)"| E["Marco E<br/>extremo"]
- 🎯 **Por qué importa:** Para mover un brazo hay que saber dónde está su extremo. Si el marco de cada eslabón está mal puesto, todo lo que sigue (cinemática inversa, singularidades, calibración) hereda el error.
- 🔗 **Se estudia junto con:** Transformación homogénea, Marco {0}, Parámetros D-H, Cinemática directa.

📘 **Dónde se aprende** (1 clase): [B101-C01 · Transformaciones homogéneas y parametrización de eslabones (Denavit-Hartenberg)](../programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/CLASE.md).

### Marco en caída libre

- Un marco en caída libre no siente gravedad.

💡 **Contexto en la clase [B26-C06](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md):**
- **Idea central (modelo mental):** Dentro de un ascensor sin ventanas no puedes decir si estás parado en la Tierra o si un cohete te acelera con `a = g`. Un haz de luz que sube desde el piso llega al techo con la frecuencia reducida porque el techo, que acelera, se aleja del haz.
- 🎯 **Por qué importa:** Los relojes de los satélites de navegación van a un ritmo ligeramente distinto de los terrestres, y un maser en una torre ve su frecuencia cambiar con la altura. Todo eso se deduce de la equivalencia entre aceleración y gravedad.
- 🔗 **Se estudia junto con:** principio de equivalencia (débil), principio de equivalencia de Einstein (local), corrimiento gravitacional al rojo, aceleración del cohete.

📘 **Dónde se aprende** (1 clase): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md).

### Marco ENU

- El marco ENU (Este, Norte, Cenit) es el marco topocéntrico local de la estación.

💡 **Cómo se explica en la clase [B74-C01](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md):**
- Escribir `h(x)` para alcance, azimut y elevación en el marco ENU de una estación.
- El vector relativo debe expresarse en el mismo marco que el estado en el instante de la medida;
- 🎯 **Por qué importa:** Todo método de B74 (mínimos cuadrados, filtros, validación) deriva del par `h` y `H = ∂h/∂x`. La decisión central: ¿qué función y qué derivadas describen la medida, y cómo sé que están bien escritas antes de dárselas a un estimador?
- 🔗 **Se estudia junto con:** modelo de observación, residuo, jacobiano, covarianza de medida.

📘 **Dónde se aprende** (1 clase): [B74-C01 · Modelos de observación](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md).

### Marco giratorio

- El marco giratorio de una luna sincrónica gira con `ω = 2π/P`.

💡 **Cómo se explica en la clase [B75-C16](../programa/clases/B75/B75-C16-navegacion-relativa-a-lunas/CLASE.md):**
- A `t = 3 d` la posición relativa inercial `(502 296,6; 790 561,9) km` se vuelve `(−339 118,8; 873 091,3) km` en el marco giratorio; la ida y vuelta recupera el vector con error `0`.
- M["omega = 2 pi / P"] --> R["marco giratorio de la luna"]
- 🎯 **Por qué importa:** Para navegar en un sistema de lunas hay que saber en qué marco se mide cada cosa y qué tan grande es la esfera de influencia de cada luna. La decisión central: ¿con qué velocidad relativa llega una nave a cada luna y cuán grande es la región donde la luna manda?
- 🔗 **Se estudia junto con:** radio de Hill, velocidad orbital, velocidad relativa, elementos medios.

📘 **Dónde se aprende** (1 clase): [B75-C16 · Navegación relativa a lunas](../programa/clases/B75/B75-C16-navegacion-relativa-a-lunas/CLASE.md).

### Marco inercial

- Un marco inercial es aquel en que se cumple la primera ley.
- Un marco inercial es un marco en el que se cumple la primera ley de Newton.
- Un marco inercial no acelera ni gira; el marco sinódico gira con velocidad angular constante `ω = n` alrededor del baricentro.

💡 **Cómo se explica en la clase [B05-C04](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md):**
- Eso solo ocurre en un marco inercial; en un marco que gira o acelera aparecen movimientos sin causa aparente.
- A["Elegir cuerpo y marco inercial"] --> B["Listar fuerzas sobre ese cuerpo"]
- 🎯 **Por qué importa:** Un satélite no tiene motor encendido y aun así gira. Una nave en el espacio vacío mantiene su velocidad sin esfuerzo.
- 🔗 **Se estudia junto con:** fuerza, masa inercial, fuerza neta, peso.

📘 **Dónde se aprende** (3 clases): [B05-C04 · Leyes del movimiento de Newton](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md); [B26-C01 · Postulados de relatividad especial](../programa/clases/B26/B26-C01-postulados-de-relatividad-especial/CLASE.md); [B73-C02 · Marcos rotatorios sinódicos](../programa/clases/B73/B73-C02-marcos-rotatorios-sinodicos/CLASE.md).

### Marco LVLH

- El marco LVLH tiene `x` radial saliente, `y` a lo largo de la trayectoria y `z` normal.

💡 **Cómo se explica en la clase [B76-C17](../programa/clases/B76/B76-C17-sistemas-de-referencia-relativos/CLASE.md):**
- Un punto quieto en LVLH en `(120, −800, 40)` se mueve en el marco inercial con velocidad relativa a la referencia `n × r = (0,905093; 0,135764; 0) m/s`: coincide con el resultado de la conversión.
- I["marco inercial"] --> L["LVLH: rotar y restar w x r"]
- 🎯 **Por qué importa:** Una posición correcta en el marco equivocado es una colisión. La decisión central: ¿cómo se convierten posición y velocidad entre los marcos de la misión y cómo se comprueba la conversión?
- 🔗 **Se estudia junto con:** marco sinódico, velocidad de arrastre, Jacobi inercial.

📘 **Dónde se aprende** (1 clase): [B76-C17 · Sistemas de referencia relativos](../programa/clases/B76/B76-C17-sistemas-de-referencia-relativos/CLASE.md).

### Marco ME

- El marco ME y el marco PA son dos conjuntos de ejes ligados al cuerpo que difieren en una rotación pequeña.

💡 **Cómo se explica en la clase [B53-C05](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md):**
- Si el marco no se declara, ese error pasa inadvertido.
- *Descripción textual:* Las coordenadas geográficas se convierten a cartesianas, se rotan entre marcos y se vuelven a convertir o se proyectan.
- ⚠️ **Error frecuente:** No declarar el marco. se corrige con la sección 10
- 🎯 **Por qué importa:** Dos productos en marcos distintos no se superponen sin corregir. La decisión central: ¿en qué marco, con qué figura y con qué convención está cada coordenada, y cuánto se desplaza un punto al cambiar de marco?
- 🔗 **Se estudia junto con:** marco PA, longitud este, proyección estereográfica, cota.

📘 **Dónde se aprende** (1 clase): [B53-C05 · Sistemas de coordenadas lunares](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md).

### Marco PA

- El marco ME y el marco PA son dos conjuntos de ejes ligados al cuerpo que difieren en una rotación pequeña.

💡 **Cómo se explica en la clase [B53-C05](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md):**
- Si el marco no se declara, ese error pasa inadvertido.
- *Descripción textual:* Las coordenadas geográficas se convierten a cartesianas, se rotan entre marcos y se vuelven a convertir o se proyectan.
- ⚠️ **Error frecuente:** No declarar el marco. se corrige con la sección 10
- 🎯 **Por qué importa:** Dos productos en marcos distintos no se superponen sin corregir. La decisión central: ¿en qué marco, con qué figura y con qué convención está cada coordenada, y cuánto se desplaza un punto al cambiar de marco?
- 🔗 **Se estudia junto con:** marco ME, longitud este, proyección estereográfica, cota.

📘 **Dónde se aprende** (1 clase): [B53-C05 · Sistemas de coordenadas lunares](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md).

### Marco RTN

- El marco RTN descompone el error en radial, transversal y normal.

💡 **Contexto en la clase [B74-C28](../programa/clases/B74/B74-C28-medidas-de-rango-y-doppler-para-determinar-la-orbita/CLASE.md):**
- 🎯 **Por qué importa:** Un único pase desde una única estación puede no determinar la órbita completa, aunque la medida sea muy precisa. La decisión central: ¿qué combinación de observables y de estaciones hace observable el estado y con qué precisión en cada dirección?
- 🔗 **Se estudia junto con:** matriz de información, rango numérico, número de condición, normalización.

📘 **Dónde se aprende** (1 clase): [B74-C28 · Medidas de rango y Doppler para determinar la órbita](../programa/clases/B74/B74-C28-medidas-de-rango-y-doppler-para-determinar-la-orbita/CLASE.md).

### Marco sinódico

- En el marco sinódico (baricéntrico, rotatorio) los primarios están fijos en `(−μ, 0)` y `(1−μ, 0)`.
- Un marco inercial no acelera ni gira; el marco sinódico gira con velocidad angular constante `ω = n` alrededor del baricentro.
- El marco sinódico gira con la Luna a `n`.

💡 **Cómo se explica en la clase [B73-C01](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md):**
- En el marco sinódico, con `r₁ = √((x+μ)²+y²)` y `r₂ = √((x−1+μ)²+y²)`:
- Se pasa el estado inicial al marco inercial (`v_in = R(v_rot + ω×r)`), se integra y se devuelve el resultado al sinódico.
- 🎯 **Por qué importa:** Con tres cuerpos no hay solución cerrada, pero sí una cantidad conservada que organiza todo lo demás: puntos de equilibrio, regiones prohibidas y transferencias de bajo costo. La decisión central: ¿cuándo basta el modelo de tres cuerpos restringido, y cómo sé que mi integración no inventa dinámica?
- 🔗 **Se estudia junto con:** CR3BP, parámetro de masa, constante de Jacobi, unidades adimensionales.

📘 **Dónde se aprende** (3 clases): [B73-C01 · Problema restringido de tres cuerpos](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md); [B73-C02 · Marcos rotatorios sinódicos](../programa/clases/B73/B73-C02-marcos-rotatorios-sinodicos/CLASE.md); [B76-C17 · Sistemas de referencia relativos](../programa/clases/B76/B76-C17-sistemas-de-referencia-relativos/CLASE.md).

### Marea

- La marea es la deformación de un cuerpo por el campo gravitatorio de otro.

💡 **Cómo se explica en la clase [B65-C06](../programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/CLASE.md):**
- El satélite tiene un tensor de cuadrupolo `Q_ij` en su sistema fijo que relaja hacia el equilibrio de marea `Q_eq = (k₂R⁵/3G)(GM_p/r³)(3r̂r̂ − I)` con un retardo `τ = 1/(Qn)`: `dQ/dt = (Q_eq − Q)/τ`.
- La segunda forma de la potencia, `⟨F:dQ/dt⟩` (trabajo de la marea sobre la deformación), coincide con la primera a `10⁻⁸`.
- ⚠️ **Error frecuente:** Pensar que una órbita circular da calor de marea. Se corrige con la dependencia en `e²`.
- 🎯 **Por qué importa:** Un satélite pequeño se enfría rápido; si aun así tiene un interior caliente, algo lo calienta. La decisión central: ¿cuánto calor produce una marea y a qué temperatura de equilibrio llevaría la superficie?
- 🔗 **Se estudia junto con:** número de Love, factor de calidad, excentricidad, equilibrio térmico.

📖 **Explicado a fondo:** [Marea](esencial/ampliacion-a-m.md#marea) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B65-C06 · Calentamiento por marea y equilibrio térmico en satélites](../programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/CLASE.md).

### Marea de equilibrio

- La marea de equilibrio es la deformación estática que seguiría el potencial de marea.

💡 **Cómo se explica en la clase [B72-C16](../programa/clases/B72/B72-C16-modelado-de-mareas/CLASE.md):**
- La marea de equilibrio con `h₂ = 0,6` (ilustrativo) es `(3/2) h₂ (m/M)(R/d)³ R = 0,323 m`.
- Calcular la aceleración de marea en la superficie y la marea de equilibrio.
- 🎯 **Por qué importa:** La marea alarga el día, aleja a la Luna y calienta a Ío y Europa; en un satélite bajo el radio síncrono (como Fobos) hace lo contrario y lo acerca. La decisión central: ¿hacia dónde y a qué velocidad cambia el semieje por la marea, según esté el satélite dentro o fuera del radio síncrono?
- 🔗 **Se estudia junto con:** retardo de marea, par de marea, radio síncrono.

📘 **Dónde se aprende** (1 clase): [B72-C16 · Modelado de mareas](../programa/clases/B72/B72-C16-modelado-de-mareas/CLASE.md).

### Marea de Júpiter

- La marea de Júpiter relativa es `2 GM_J r/a³ ÷ (GM_E/r²)`.

💡 **Cómo se explica en la clase [B73-C21](../programa/clases/B73/B73-C21-pasos-cercanos-a-satelites-naturales-en-integracion-de-n-cuerpos/CLASE.md):**
- La marea de Júpiter es `8,3%` de la gravedad de Europa a `r₀` y `0,12%` en el periapsis: para una predicción de precisión hay que integrar el sistema de varios cuerpos de [B73-C08](../B73-C08-sistemas-de-n-cuerpos/CLASE.md), con paso adaptativo, y la solución analítica deja de ser la referencia.
- G["marea de Jupiter"] --> L["limite del modelo"]
- ⚠️ **Error frecuente:** Olvidar la marea de Júpiter. Se corrige con 8.5.
- 🎯 **Por qué importa:** Un encuentro con una luna cambia la dirección y la energía de un cuerpo en pocos minutos, y un paso de tiempo fijado para el resto del sistema puede dar un resultado muy erróneo allí. Pero un paso adaptativo también cuesta.
- 🔗 **Se estudia junto con:** hipérbola, deflexión asintótica, paso adaptativo.

📘 **Dónde se aprende** (1 clase): [B73-C21 · Pasos cercanos a satélites naturales en integración de N cuerpos](../programa/clases/B73/B73-C21-pasos-cercanos-a-satelites-naturales-en-integracion-de-n-cuerpos/CLASE.md).

### Marea solar

- La marea solar es `a = μ_s [(d−r)/|d−r|³ − d/|d|³]`.

💡 **Cómo se explica en la clase [B72-C09](../programa/clases/B72/B72-C09-perturbaciones-solares/CLASE.md):**
- La marea solar no es despreciable en órbitas altas (`10⁻⁶ m/s²` en GEO), pero actúa lentamente: el polo tarda siglos en dar una vuelta.
- A GEO la marea solar es `3,34 × 10⁻⁶ m/s²`, `1,5 × 10⁻⁵` de la gravedad.
- 🎯 **Por qué importa:** En órbitas altas el Sol y la Luna compiten con J2 y gobiernan la evolución de la inclinación y del nodo. La decisión central: ¿cuánto gira el plano de una órbita por la marea solar y qué fórmula sirve para predecirlo?
- 🔗 **Se estudia junto con:** aproximación cuadrupolar, polo orbital, precesión luni-solar.

📘 **Dónde se aprende** (1 clase): [B72-C09 · Perturbaciones solares](../programa/clases/B72/B72-C09-perturbaciones-solares/CLASE.md).

### Margen

- El margen es la diferencia.
- El margen es el requisito menos el total.
- El margen es la parte añadida por incertidumbre.
- *(y 27 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C20](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md):**
- El requisito `S ≥ 0,8` exige `σ ≤ 41,35 nm`; el margen es `14,89 nm`.
- El frente de onda suma `26,46 nm` RMS (Monte Carlo: `26,45 nm`), Strehl `0,913` frente al requisito `0,8` (`σ ≤ 41,35 nm`; margen `14,89 nm`).
- ⚠️ **Error frecuente:** Ignorar el margen. Se corrige con 8.1.
- 🎯 **Por qué importa:** El proyecto completo exige que los errores se sumen, se verifiquen y se comparen con los requisitos. La decisión central: ¿qué fuente domina el error, cuánto margen queda y la estructura es lo bastante rígida para el servo?
- 🔗 **Se estudia junto con:** presupuesto de error, suma en cuadratura (RSS), requisito, frecuencia estructural.

📘 **Dónde se aprende** (30 clases): [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md); [B47-C02 · Requisitos de instrumentos orbitales](../programa/clases/B47/B47-C02-requisitos-de-instrumentos-orbitales/CLASE.md); [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md); [B50-C15 · Presupuesto de error de frente de onda de un instrumento](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md); [B75-C09 · Presupuestos de delta-v](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md); [B83-C09 · Presupuestos de masa](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md) y 24 más.

### Margen bruto

- El margen bruto `g` es la fracción de ingreso que queda tras los costos directos.

💡 **Cómo se explica en la clase [B126-C04](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md):**
- El ejemplo conductor es un servicio sintético de datos de observación de la Tierra por suscripción: gasto de captación de 240 000 USD por trimestre con 60 clientes nuevos, ingreso mensual por cliente (ARPA) de 900 USD, margen bruto de 70 % y abandono mensual de 2 %.
- Ejercicio 2 · con una pista. Margen bruto mensual por cliente.
- 🎯 **Por qué importa:** Un negocio espacial debe medir cuánto cuesta ganar un cliente; el catálogo no lo trata. La decisión central: ¿vale la pena el gasto de captación, dado cuánto tiempo se queda el cliente y cuánto margen deja?
- 🔗 **Se estudia junto con:** CAC, ARPA, abandono, LTV.

📘 **Dónde se aprende** (1 clase): [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### Margen de coordinación

- El margen de coordinación es el tiempo que sobra tras coordinar y examinar.

💡 **Cómo se explica en la clase [B120-C06](../programa/clases/B120/B120-C06-caso-de-planificacion-regulatoria-de-un-sistema-satelital/CLASE.md):**
- Con la BIU fija, el margen de coordinación es `L − (6 + 4 + 14 + 6) = L − 30` meses (espera de 6, respuesta de 4, negociación de 14 y examen de 6) y la holgura es `84 − L`.
- Encontrar la ventana de anticipación que cumple a la vez un riesgo objetivo y un margen de coordinación.
- 🎯 **Por qué importa:** Integrar licencias, frecuencias y plazos en un plan es el cierre del módulo y no existe un caso integrador regulatorio. La decisión central: ¿cuándo debe presentarse la publicación anticipada para que haya tiempo de coordinar y holgura frente al plazo, y qué riesgo restante queda?
- 🔗 **Se estudia junto con:** plan regresivo, ventana de anticipación, holgura, hito.

📘 **Dónde se aprende** (1 clase): [B120-C06 · Caso de planificación regulatoria de un sistema satelital](../programa/clases/B120/B120-C06-caso-de-planificacion-regulatoria-de-un-sistema-satelital/CLASE.md).

### Margen de datos

- El margen de datos es la razón capacidad/demanda; la regla del ejemplo exige 1,3 (30 %).
- Eficiencia de protocolo: fracción de la tasa que lleva datos útiles. Margen de datos: `capacidad/demanda − 1`.

💡 **Cómo se explica en la clase [B83-C08](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md):**
- *Descripción textual:* cada interfaz se describe con parámetros; de ellos se calculan la caída de tensión y el margen de datos, y de ahí un veredicto; la caída se comprueba por una segunda formulación.
- Comprobar el margen de capacidad de un enlace de datos.
- 🎯 **Por qué importa:** La mayoría de los fallos de integración aparecen en las interfaces: un conector mal definido, una tensión fuera de rango o una tasa de datos insuficiente. La decisión central: ¿cada interfaz cumple en su caso más desfavorable, con margen, antes de construir?
- 🔗 **Se estudia junto con:** interfaz, ICD, caída de tensión, rango de la carga.

📘 **Dónde se aprende** (2 clases): [B83-C08 · Interfaz entre subsistemas](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md); [B96-C02 · Concepto de operaciones de misión](../programa/clases/B96/B96-C02-concepto-de-operaciones-de-mision/CLASE.md).

### Margen de desarrollo

- El margen de desarrollo (aquí `20 %`, ilustrativo) cubre la incertidumbre.

💡 **Cómo se explica en la clase [B85-C20](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar el margen de desarrollo. el margen cubre incertidumbre (8.1)
- 🎯 **Por qué importa:** Un presupuesto sin margen no resiste un cambio de diseño. La decisión central: ¿qué modo gobierna el caso caliente, con cuánto margen cierra y qué calentador pide el frío?
- 🔗 **Se estudia junto con:** disipación del modo, capacidad del radiador, margen de potencia, modo gobernante.

📘 **Dónde se aprende** (1 clase): [B85-C20 · Presupuesto térmico de carga útil](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md).

### Margen de diseño

- El margen de diseño es el que se reserva para una probabilidad de salida objetivo.

💡 **Contexto en la clase [B92-C08](../programa/clases/B92/B92-C08-margenes-y-disponibilidad-de-enlaces-opticos/CLASE.md):**
- 🎯 **Por qué importa:** El contrato de un servicio de comunicaciones dice «99 % de disponibilidad», no «4 W». La decisión central: ¿cuántos decibelios de margen y cuántas estaciones terrestres hacen falta para cumplir una disponibilidad objetivo, y qué parte de la salida de servicio es del enlace y qué parte del clima y del hardware?
- 🔗 **Se estudia junto con:** presupuesto de enlace, margen, salida de servicio, disponibilidad.

📖 **Explicado a fondo:** [Margen de diseño](esencial/ampliacion-a-m.md#margen-de-diseño) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B92-C08 · Márgenes y disponibilidad de enlaces ópticos](../programa/clases/B92/B92-C08-margenes-y-disponibilidad-de-enlaces-opticos/CLASE.md).

### Margen de estabilidad

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B42-C16](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md):**
- **Idea central (modelo mental):** Como regular una ducha con agua que tarda en llegar: si giras la llave muy rápido, oscilas; muy lento, no sigues la temperatura.
- 🎯 **Por qué importa:** El lazo decide qué tan rápido es el rechazo y cuánto ruido se amplifica. La decisión central: ¿qué ganancia da el mejor compromiso entre rechazo, ruido y estabilidad con retardo?
- 🔗 **Se estudia junto con:** integrador, retardo, función de rechazo, ruido.

📘 **Dónde se aprende** (1 clase): [B42-C16 · Lazo de control de óptica adaptativa](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md).

### Margen de fase

- El margen de fase (MF) es `180° + fase(ω_gc)`; el margen de ganancia (MG) es `1/|L(jω_pc)|`.
- El margen de fase `PM = 180° + ∠L(jω_c)` y el de ganancia `GM = −20 log|L|` donde `∠L = −180°`.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- El margen de fase se mide en `ω_gc`, donde `|L| = 1`; se calcula numéricamente.
- Un margen de fase de unos 45° a 60° y uno de ganancia de unos 6 a 10 dB son valores de práctica habituales como orientación, no como norma.
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.
- 🔗 **Se estudia junto con:** respuesta en frecuencia, diagrama de Bode, cruce de ganancia, cruce de fase.

📘 **Dónde se aprende** (2 clases): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md); [B87-C19 · Verificación de ley de control](../programa/clases/B87/B87-C19-verificacion-de-ley-de-control/CLASE.md).

### Margen de ganancia

- El margen de fase (MF) es `180° + fase(ω_gc)`; el margen de ganancia (MG) es `1/|L(jω_pc)|`.
- El margen de ganancia es `G − G_requerida`.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- Un margen de fase de unos 45° a 60° y uno de ganancia de unos 6 a 10 dB son valores de práctica habituales como orientación, no como norma.
- El margen de ganancia es cuánto se puede estirar la curva en el eje real negativo antes de tocar `−1`; el margen de fase es cuánto se puede girar.
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.
- 🔗 **Se estudia junto con:** respuesta en frecuencia, diagrama de Bode, cruce de ganancia, cruce de fase.

📘 **Dónde se aprende** (2 clases): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md); [B91-C06 · Selección y compromiso de diseño de antenas](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md).

### Margen de par

- Arrastre: par resistente (fricción, arnés). Margen de par: par mínimo disponible dividido por el arrastre.

💡 **Cómo se explica en la clase [B90-C15](../programa/clases/B90/B90-C15-pruebas-de-despliegue/CLASE.md):**
- El criterio de margen ≥ 2 es de ejemplo.
- Incluso con margen 0,84 el panel llega, porque el par es mayor al principio; pero el margen se define en el punto más desfavorable y falla el criterio de ejemplo (≥ 2).
- ⚠️ **Error frecuente:** Evaluar el margen al inicio. Es mínimo en la traba (8.2)
- 🎯 **Por qué importa:** Un mecanismo que despliega en el laboratorio con un margen justo puede quedarse a medio camino con lubricación degradada o arrastre de un arnés. La decisión central: ¿cuánto par sobra frente al arrastre y con qué velocidad llega a la traba?
- 🔗 **Se estudia junto con:** Despliegue, Par de resorte, Arrastre, tope que fija el panel desplegado.

📘 **Dónde se aprende** (1 clase): [B90-C15 · Pruebas de despliegue](../programa/clases/B90/B90-C15-pruebas-de-despliegue/CLASE.md).

### Margen de potencia

- El margen de potencia es capacidad menos demanda.

💡 **Cómo se explica en la clase [B85-C20](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md):**
- Calcular el margen de potencia y reconocer el modo que gobierna.
- supervivencia : margen de potencia = +162.64 W (+98.5 % de la capacidad)
- 🎯 **Por qué importa:** Un presupuesto sin margen no resiste un cambio de diseño. La decisión central: ¿qué modo gobierna el caso caliente, con cuánto margen cierra y qué calentador pide el frío?
- 🔗 **Se estudia junto con:** disipación del modo, margen de desarrollo, capacidad del radiador, modo gobernante.

📘 **Dónde se aprende** (1 clase): [B85-C20 · Presupuesto térmico de carga útil](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md).

### Margen de preparación

- El margen de preparación es lo que sobra del período tras sumar `t_co`, el establecimiento y `t_su`.

💡 **Cómo se explica en la clase [B93-C03](../programa/clases/B93/B93-C03-integridad-de-senal-en-electronica-embarcada/CLASE.md):**
- En un reloj de 100 MHz, el margen de preparación pasa de `4,05 ns` a `0,26 ns`.
- Calcular el margen de preparación (*setup*) de un enlace síncrono.
- 🎯 **Por qué importa:** El tronco no incluía reflexiones, diafonía ni temporización de señales. La decisión central: ¿cuánto se deforma una señal por una terminación mal adaptada, cuánto se acopla a la pista vecina y cuánto margen de reloj queda?
- 🔗 **Se estudia junto con:** coeficiente de reflexión, diagrama de rebotes, diafonía cercana, longitud de saturación.

📘 **Dónde se aprende** (1 clase): [B93-C03 · Integridad de señal en electrónica embarcada](../programa/clases/B93/B93-C03-integridad-de-senal-en-electronica-embarcada/CLASE.md).

### Margen de resistencia

- El margen de resistencia `M = G_p − J/S − (E_b/N_0)_req` es lo que sobra.

💡 **Cómo se explica en la clase [B119-C15](../programa/clases/B119/B119-C15-interferencias-y-resiliencia-de-comunicaciones/CLASE.md):**
- Calcular la ganancia de procesamiento y el margen de resistencia.
- 🎯 **Por qué importa:** C09 calcula interferencia entre sistemas lícitos; esta clase extiende el cálculo a un escenario de degradación deliberada para razonar sobre resiliencia. La respuesta jurídica se aborda en C17 y C27.
- 🔗 **Se estudia junto con:** relación J/S, ganancia de procesamiento, resiliencia.

📘 **Dónde se aprende** (1 clase): [B119-C15 · Interferencias y resiliencia de comunicaciones](../programa/clases/B119/B119-C15-interferencias-y-resiliencia-de-comunicaciones/CLASE.md).

### Margen de respuesta

- El margen de respuesta es el tiempo hasta el umbral menos el tiempo de respuesta.

💡 **Cómo se explica en la clase [B114-C05](../programa/clases/B114/B114-C05-despresurizacion-escenarios-tiempos-y-respuesta/CLASE.md):**
- Con una respuesta ilustrativa de `300 s`, el margen hasta `34,5 kPa` es `1858 s` con `20 mm` y negativo (`−213,7 s`) con `100 mm`.
- *Descripción textual:* el volumen y el área dan `τ`; con el umbral se obtiene el tiempo y, restando la respuesta, el margen; el RK4 lo comprueba.
- 🎯 **Por qué importa:** Entre una grieta de `1 mm` y una brecha de `100 mm` el tiempo disponible pasa de días a segundos. La decisión central: ¿cuánto tiempo hay hasta un umbral de presión y alcanza para responder?
- 🔗 **Se estudia junto con:** despresurización, constante de tiempo, modelo isotermo, adiabático.

📘 **Dónde se aprende** (1 clase): [B114-C05 · Despresurización: escenarios, tiempos y respuesta](../programa/clases/B114/B114-C05-despresurizacion-escenarios-tiempos-y-respuesta/CLASE.md).

### Margen de retardo

- Un margen de retardo es el retardo adicional que consume el margen de fase.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- Convertir un margen de fase en un margen de retardo.
- Ejercicio 3 · casi autónomo. Con `ω_gc = 0,5 rad/s` y `MF = 60°`, calcula el margen de retardo.
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.
- 🔗 **Se estudia junto con:** respuesta en frecuencia, diagrama de Bode, cruce de ganancia, cruce de fase.

📘 **Dónde se aprende** (1 clase): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).

### Margen de seguridad

- El margen de seguridad `MS = σ_adm/(FS σ_lim) − 1` es positivo si hay reserva.
- El margen de seguridad es un porcentaje sobre ese mínimo.

💡 **Cómo se explica en la clase [B84-C09](../programa/clases/B84/B84-C09-analisis-de-cargas/CLASE.md):**
- *Descripción textual:* los factores de carga dan fuerzas y momento, de los cuales salen la carga equivalente y la tensión; con los factores de seguridad se calcula el margen.
- Calcular el margen de seguridad `MS = σ_adm/(FS σ) − 1`.
- 🎯 **Por qué importa:** Un margen sin una carga bien planteada no vale: la carga lateral actúa con brazo de palanca y puede exigir más al anillo que la axial. La decisión central: ¿qué margen tiene el anillo de interfaz con las cargas límite y los factores de seguridad estándar?
- 🔗 **Se estudia junto con:** carga límite, carga última, carga axial equivalente.

📘 **Dónde se aprende** (2 clases): [B84-C09 · Análisis de cargas](../programa/clases/B84/B84-C09-analisis-de-cargas/CLASE.md); [B126-C03 · Proyección de flujos de caja de un proyecto espacial](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md).

### Margen de separación

- Factor de carga `φ`: fracción de una carga externa que absorbe el perno. Margen de separación: margen de que la unión no se abra.

💡 **Cómo se explica en la clase [B90-C06](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md):**
- Calcular la carga de separación de una unión con el factor de carga `φ` y su margen.
- Ejercicio 5 · autónomo. Calcula el margen de separación con `P_ext = 800 N` por perno, FS 1,4 y `P_sep = 1 667 N`.
- 🎯 **Por qué importa:** Un perno mal apretado se afloja con la vibración o se rompe por exceso de carga; un centro de masa fuera de rango desvía la nave en el despliegue. La decisión central: ¿qué par de apriete garantiza que la unión no se separe ni se plastifique, y el conjunto queda dentro de los límites de masa?
- 🔗 **Se estudia junto con:** Precarga, Coeficiente de par K, Factor de carga φ, Centro de masa (CG).

📘 **Dónde se aprende** (1 clase): [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md).

### Margen de vuelco

- El margen de vuelco es la distancia de esa proyección al borde más próximo.

💡 **Cómo se explica en la clase [B102-C05](../programa/clases/B102/B102-C05-distribucion-de-cargas-y-estabilidad-ante-vuelco/CLASE.md):**
- *Descripción textual:* la inclinación y la geometría fijan dónde cae la proyección del centro de masas; la distancia al borde es el margen y el vuelco ocurre cuando es nulo; además la inclinación reparte las cargas entre ejes y lados.
- Ejercicio 12 · integrador. Integrador. Elabora tu *tabla de márgenes de estabilidad*: ángulos de vuelco, margen a 30°, cargas por eje en tres cuerpos, transferencia lateral, aceleración crítica y lista de qué es consultado e ilustrativo.
- 🎯 **Por qué importa:** Las leyes de operación de un rover fijan un máximo de inclinación. La decisión central: ¿cuánto margen queda frente al vuelco en una pendiente dada, y qué parte de ese margen depende de la gravedad?
- 🔗 **Se estudia junto con:** proyección del centro de masas, cabeceo, balanceo, transferencia de carga.

📘 **Dónde se aprende** (1 clase): [B102-C05 · Distribución de cargas y estabilidad ante vuelco](../programa/clases/B102/B102-C05-distribucion-de-cargas-y-estabilidad-ante-vuelco/CLASE.md).

### Margen de Δv

- El margen de Δv es un porcentaje sobre el Δv nominal.

💡 **Cómo se explica en la clase [B78-C17](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md):**
- Sin margen ni residuo, la opción química pide `431,40 kg` en lugar de `511,91 kg`: los márgenes de `10 %` de Δv y `2 %` de residuo cuestan `80,5 kg` de propelente.
- MF --> MP2["m_p = (1+res) m_f (exp(dv(1+margen)/Ve) - 1)"]
- ⚠️ **Error frecuente:** Quitar márgenes sin cuantificarlos. Se corrige con 8.4.
- 🎯 **Por qué importa:** Una hoja de presupuesto honesta incluye márgenes y reservas, y esos márgenes cuestan masa. La decisión central: ¿cuánto propelente, tanques y planta hacen falta para un Δv con margen, y qué arquitectura da la menor masa total en cada caso?
- 🔗 **Se estudia junto con:** masa seca, residuo, fracción de tanques, planta.

📘 **Dónde se aprende** (1 clase): [B78-C17 · Masa de propelente y presupuesto](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md).

### Margen estático

- El margen estático es `(x_cp − x_cg)/d`, positivo si el centro de presión va detrás.

💡 **Cómo se explica en la clase [B77-C21](../programa/clases/B77/B77-C21-centro-de-presion-y-margen-estatico/CLASE.md):**
- El margen estático es `0,731` calibres y `Cm_α = -5,849 /rad`.
- Obtener el margen estático en calibres y `Cm_α`.
- 🎯 **Por qué importa:** Un lanzador sin margen estático positivo se voltea con la primera ráfaga; con demasiado margen es rígido y carga mucho el control. La decisión central: ¿dónde está el centro de presión, cuánto margen hay y qué lo cambia?
- 🔗 **Se estudia junto con:** pendiente de fuerza normal, pendiente de momento, calibre, estable.

📘 **Dónde se aprende** (1 clase): [B77-C21 · Centro de presión y margen estático](../programa/clases/B77/B77-C21-centro-de-presion-y-margen-estatico/CLASE.md).

### Margen sobre precio

- El margen sobre precio `m` fija `p = costo medio/(1 − m)`.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- Con margen sobre precio de 25 %, `p = costo medio/0,75`: `78,67` um a 1 000, `37,60` a 2 500 y `23,20` a 5 000 productos.
- Paso 3 · Precio. Con margen sobre precio de 20 %: `4/0,8 = 5`.
- ⚠️ **Error frecuente:** Confundir margen sobre precio con margen sobre costo. Se corrige con 8.2: aquí `p = costo/(1 − m)`.
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?
- 🔗 **Se estudia junto con:** costo fijo, variable, escalonado, costo medio.

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Marginalización

- La marginalización de la constante `M` se hace restando la media de los residuos.

💡 **Cómo se explica en la clase [B26-C20](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md):**
- Con `μ_i` observados, `μ_t(z_i; Ω_m)` teóricos (C19) y error `σ = 0,15 mag`, `χ²(Ω_m) = Σ[(μ_i − μ_t,i) − ⟨μ − μ_t⟩]²/σ²`: restar la media de los residuos marginaliza la constante de calibración.
- 🎯 **Por qué importa:** Una cifra cosmológica sin incertidumbre no significa nada. Para decidir si dos resultados concuerdan, o si un modelo queda excluido, hay que saber construir y leer un intervalo de confianza.
- 🔗 **Se estudia junto con:** χ², grados de libertad, mejor ajuste, intervalo de 68 %.

📘 **Dónde se aprende** (1 clase): [B26-C20 · Límites observacionales de modelos cosmológicos](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md).

### Marginalmente estable

- Un sistema `y′ = A y` es asintóticamente estable si todos los autovalores tienen parte real negativa, marginalmente estable si alguno tiene parte real cero y ninguno positiva (con autovectores completos), e inestable si alguno tiene parte real positiva.
- Es marginalmente estable si no crece pero tampoco decae (polos simples sobre el eje imaginario).

💡 **Cómo se explica en la clase [B16-C07](../programa/clases/B16/B16-C07-realimentacion-y-estabilidad/CLASE.md):**
- Explicar por qué un control proporcional sobre un doble integrador es marginalmente estable.
- 🎯 **Por qué importa:** Un lazo de control puede estabilizar un sistema inestable o desestabilizar uno estable. Un telescopio con el lazo mal diseñado no solo apunta mal: oscila, consume propergol o energía de las ruedas y puede perder el objetivo.
- 🔗 **Se estudia junto con:** asintóticamente estable, inestable, realimentación de estados, sensibilidad.

📘 **Dónde se aprende** (2 clases): [B10-C09 · Diagonalización y estabilidad](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md); [B16-C07 · Realimentación y estabilidad](../programa/clases/B16/B16-C07-realimentacion-y-estabilidad/CLASE.md).

### Mariposa

- Una mariposa (*butterfly*) es la operación básica: combina un par de valores con un factor de giro `W^k = e^{−2πi k/N}`.

💡 **Cómo se explica en la clase [B15-C05](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md):**
- Si `T(N)` es el número de mariposas, `T(N) = 2 T(N/2) + N/2`, con `T(1) = 0`.
- El laboratorio cuenta las mariposas de su propia implementación y coinciden con la fórmula en todos los tamaños.
- 🎯 **Por qué importa:** Una curva de luz de 27 días con cadencia de 2 minutos tiene 19 440 muestras. La suma directa de la DFT necesita unos 378 millones de multiplicaciones complejas; una imagen de 1024 × 1024 necesitaría muchísimas más.
- 🔗 **Se estudia junto con:** FFT, base 2, relleno con ceros, orden estándar.

📘 **Dónde se aprende** (1 clase): [B15-C05 · Transformada rápida de Fourier](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md).

### Martingala

- Una martingala conserva el valor esperado.

💡 **Cómo se explica en la clase [B58-C19](../programa/clases/B58/B58-C19-comunicacion-publica-del-riesgo/CLASE.md):**
- Verificar que la probabilidad es una martingala.
- Es una martingala: la información promedio no cambia la media.
- 🎯 **Por qué importa:** El público oye «1 %» y a veces «ahora 0 %». Si no se explica que las probabilidades cambian con los datos y que la media se conserva, bajar a cero parece un error.
- 🔗 **Se estudia junto con:** frecuencia natural, actualización, escala de Torino, comunicación del riesgo.

📘 **Dónde se aprende** (1 clase): [B58-C19 · Comunicación pública del riesgo](../programa/clases/B58/B58-C19-comunicacion-publica-del-riesgo/CLASE.md).

### Mas

- Un mas es un milisegundo de arco.
- El mas: milisegundo de arco.

💡 **Cómo se explica en la clase [B42-C10](../programa/clases/B42/B42-C10-interferometria-de-multiples-telescopios/CLASE.md):**
- El primer nulo está en `λ/(2B) = 4,538 mas`.
- `|uv|_máx = 5,8992 × 10⁷ λ` y `λ/|uv|_máx = 3,4965 mas`.
- 🎯 **Por qué importa:** La resolución depende de la línea base, no del diámetro de cada telescopio, y la calidad de la imagen de la cobertura uv. La decisión central: ¿qué resolución y qué calidad de imagen da una disposición de telescopios?
- 🔗 **Se estudia junto con:** línea base, visibilidad, uv, síntesis de apertura.

📘 **Dónde se aprende** (2 clases): [B42-C10 · Interferometría de múltiples telescopios](../programa/clases/B42/B42-C10-interferometria-de-multiples-telescopios/CLASE.md); [B72-C17 · Efectos relativistas orbitales](../programa/clases/B72/B72-C17-efectos-relativistas-orbitales/CLASE.md).

### Masa

- La masa es `ρ t A`.

💡 **Cómo se explica en la clase [B85-C28](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md):**
- Con un factor de atenuación `2,2` veces el del aluminio por milímetro y densidad `950 kg/m³`, el polietileno cumple la dosis con `5,33 mm`, pero la perforación impone `21,5 mm` y el espesor gobernante es `21,5 mm`: masa `10,20 kg`, menos de la mitad.
- *Descripción textual:* cada requisito da un espesor; el mayor gobierna el diseño; con la densidad del material se obtiene la masa, que decide entre materiales.
- ⚠️ **Error frecuente:** Comparar materiales por espesor. se compara por masa (8.3)
- 🎯 **Por qué importa:** Cada milímetro de blindaje cuesta masa, y el requisito que manda cambia con el entorno. La decisión central: ¿qué espesor y qué material cumplen la dosis y la probabilidad de perforación con la menor masa?
- 🔗 **Se estudia junto con:** atenuación, flujo de micrometeoritos, diámetro crítico, probabilidad de perforación.

📖 **Explicado a fondo:** [Masa, inercia y peso](esencial/esencial-m-z.md#masa-inercia-y-peso) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B85-C28 · Protección pasiva frente al ambiente espacial](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md).

### Masa añadida

- La masa añadida `m_a` es la inercia del fluido arrastrado.

💡 **Cómo se explica en la clase [B104-C15](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md):**
- N --> D["en el agua: masa añadida<br/>+ arrastre cuadrático"]
- *Descripción textual:* del volumen y la masa se obtiene el lastre que da flotabilidad neutra; en el agua, la masa añadida y el arrastre hacen que el movimiento difiera del que habría en el vacío.
- ⚠️ **Error frecuente:** Olvidar la masa añadida. Inclúyela (8.3).
- 🎯 **Por qué importa:** El agua anula el peso neto, pero también se opone al movimiento. La decisión central: ¿qué aspectos de una tarea espacial se pueden entrenar bien en el agua y cuáles quedan distorsionados por la inercia y el arrastre del fluido?
- 🔗 **Se estudia junto con:** flotabilidad neutra, lastre, arrastre, presión absoluta.

📘 **Dónde se aprende** (1 clase): [B104-C15 · Entrenamiento subacuático como analogía](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md).

### Masa atómica relativa

- La masa atómica relativa de un isótopo es su masa dividida entre la doceava parte de la masa del ¹²C (por eso ¹²C vale exactamente 12).

💡 **Contexto en la clase [B06-C03](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md):**
- **Idea central (modelo mental):** Imagina una bolsa con canicas de dos pesos casi iguales, mezcladas siempre en la misma proporción. Si pesas muchas, el peso medio de una canica depende del peso de cada tipo y de su proporción. Eso es la masa atómica de las tablas: un promedio ponderado.
- 🎯 **Por qué importa:** El carbono del Sol, ¿es igual que el de la Tierra? Una forma de preguntarlo con rigor es comparar cuántos átomos de carbono-12 hay por cada uno de carbono-13.
- 🔗 **Se estudia junto con:** nucleón, número másico, isótopos, abundancia isotópica.

📘 **Dónde se aprende** (1 clase): [B06-C03 · Isótopos y masa atómica](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md).

### Masa CBE

- La masa CBE (*current best estimate*) es la estimación actual.

💡 **Cómo se explica en la clase [B83-C09](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md):**
- Masa de lanzamiento MEV = 72,156 kg; margen 7,844 kg = 9,80 %.
- Con 20 000 muestras triangulares la masa tiene media 70,340 kg y percentil 95 de 73,744 kg; la probabilidad de caber en 80 kg es 100,0 %.
- ⚠️ **Error frecuente:** Calcular el propelente sobre la masa seca sin reserva. Usa la masa seca esperada máxima
- 🎯 **Por qué importa:** La masa crece durante el diseño casi siempre; un presupuesto sin reserva se rompe en la revisión crítica. La decisión central: ¿cuánto margen queda frente al límite si cada elemento crece como su madurez sugiere?
- 🔗 **Se estudia junto con:** reserva de crecimiento, MEV, margen, ecuación del cohete.

📘 **Dónde se aprende** (1 clase): [B83-C09 · Presupuestos de masa](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md).

### Masa con helio

- La masa con helio se obtiene multiplicando por una masa media por molécula `μ_H₂ m_H` (aquí `μ_H₂ = 2,72`, es decir, dos átomos por molécula por 1,36 de factor de helio, valor ilustrativo).

💡 **Cómo se explica en la clase [B25-C04](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar el helio en la masa. Se corrige con el ejercicio 2.
- 🎯 **Por qué importa:** El hidrógeno molecular `H₂`, el componente principal de las nubes donde nacen las estrellas, casi no emite en el gas frío. Por eso la masa de una nube se estima con un trazador indirecto, el monóxido de carbono `CO`, y con el polvo que apaga la luz de fondo.
- 🔗 **Se estudia junto con:** nube molecular, trazador, intensidad integrada, factor de conversión.

📘 **Dónde se aprende** (1 clase): [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md).

### Masa de aire

- La masa de aire `X` mide el camino en la atmósfera.
- La masa de aire relativa es `1/μ`.
- La masa de aire `X ≈ sec z` para `z` pequeño.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B45-C20](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md):**
- *Descripción textual:* la geometría fija la masa de aire y la ventana; el flujo con extinción fija el tiempo de exposición; ambos dan el número de puntos.
- Un objetivo de V = 14,0 a declinación −10° desde latitud −30° (ilustrativos) tiene una ventana de `6,30 h` con masa de aire ≤ 1,5; a `X = 1,25` la exposición para S/N = 100 es `76,5 s` y caben `234` exposiciones con `10,9 mmag` por punto.
- 🎯 **Por qué importa:** Una campaña mal planificada gasta noches sin llegar a la precisión pedida. La decisión central: ¿cuánto exponer, durante cuánto tiempo y con qué precisión por punto?
- 🔗 **Se estudia junto con:** fórmula de Kasten y Young, ángulo horario, extinción, punto cero.

📘 **Dónde se aprende** (5 clases): [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B45-C22 · Extinción atmosférica, masa de aire y coeficientes de color](../programa/clases/B45/B45-C22-extincion-atmosferica-masa-de-aire-y-coeficientes-de-color/CLASE.md); [B47-C01 · Ventajas de observación fuera de atmósfera](../programa/clases/B47/B47-C01-ventajas-de-observacion-fuera-de-atmosfera/CLASE.md); [B48-C04 · Planificación por visibilidad](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md); [B54-C12 · Interacción con radiación solar](../programa/clases/B54/B54-C12-interaccion-con-radiacion-solar/CLASE.md).

### Masa de aislamiento

- La masa de aislamiento es la masa a la que el embrión ha agotado su franja: `M_iso = 2π a b Σ_p`.

💡 **Cómo se explica en la clase [B52-C05](../programa/clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md):**
- *Descripción textual:* el radio y el enfoque determinan la tasa; sus dos límites tienen solución analítica, el de enfoque diverge en tiempo finito, y el crecimiento termina en la masa de aislamiento.
- Descripción larga: el enfoque gravitacional hace el crecimiento miles de veces más rápido que el límite geométrico, aun llegando a una masa un millón de veces mayor, y el crecimiento acaba en la masa de aislamiento.
- ⚠️ **Error frecuente:** Tratar la masa de aislamiento como universal. Se corrige con 8.4.
- 🎯 **Por qué importa:** El tiempo de crecimiento decide si un núcleo existe antes de que el gas se disipe. La decisión central: ¿cómo cambia la tasa de acreción con la masa y cuándo se detiene?
- 🔗 **Se estudia junto con:** enfoque gravitacional, crecimiento descontrolado, zona de alimentación.

📘 **Dónde se aprende** (1 clase): [B52-C05 · Crecimiento de embriones planetarios](../programa/clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md).

### Masa de Chandrasekhar

- La masa de Chandrasekhar `M_Ch` es la masa máxima de una enana blanca.
- La masa de Chandrasekhar es el límite del politropo `n = 3`.

💡 **Cómo se explica en la clase [B24-C18](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md):**
- *Descripción textual:* según la masa del núcleo al fin de la fusión, queda una enana blanca (por debajo de la masa de Chandrasekhar) o se produce un colapso a una estrella de neutrones o un agujero negro, con una liberación de energía de una fracción apreciable de `Mc²`.
- Descripción larga: la masa de Chandrasekhar separa el primer caso de los otros dos; el valor de `μ_e` lo desplaza (`1,456 → 1,260 M☉`).
- 🎯 **Por qué importa:** El destino de una estrella es una enana blanca, una estrella de neutrones o un agujero negro; hay una masa límite que separa los dos primeros destinos. Calcularla muestra cómo la mecánica cuántica (presión de degeneración) sostiene a una estrella cuando ya no hay fusión.
- 🔗 **Se estudia junto con:** enana blanca, estrella de neutrones, agujero negro, presión de degeneración.

📘 **Dónde se aprende** (2 clases): [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md); [B27-C02 · Enanas blancas y límite de Chandrasekhar](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md).

### Masa de chirrido

- La masa de chirrido `M_c = (m₁m₂)^{3/5}/(m₁+m₂)^{1/5}`.

💡 **Cómo se explica en la clase [B27-C13](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md):**
- Calcular la masa de chirrido y el tiempo hasta la fusión desde una frecuencia.
- GW170817 (masas iguales 1.37 Msol): masa de chirrido = 1.1927 Msol
- 🎯 **Por qué importa:** La fusión de dos estrellas de neutrones fue el primer evento detectado en ondas gravitacionales y en luz. Saber cuánto falta para una fusión, a qué frecuencia, y cómo la excentricidad la acelera, es la base de toda búsqueda.
- 🔗 **Se estudia junto con:** frecuencia gravitacional, tiempo de fusión, orden de cuadrupolo, chirrido.

📘 **Dónde se aprende** (1 clase): [B27-C13 · Binarias compactas](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md).

### Masa de columna

- La masa de columna `Σ(h₀)` es la masa de aire sobre una área unidad por encima de `h₀`.

💡 **Cómo se explica en la clase [B09-C09](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md):**
- La presión que ejerce una atmósfera en equilibrio es el peso de la columna de aire por unidad de área: `p = g Σ`, con `Σ` la masa de columna (kg/m²).
- Calcular la masa de columna de una atmósfera exponencial.
- 🎯 **Por qué importa:** La densidad del aire decae con la altitud de forma exponencial, y la masa de aire sobre un punto determina la presión y la extinción de la luz. Para obtenerla hay que integrar `e^{−h/H}`, que no es una integral básica: la variable aparece dentro de un exponente.
- 🔗 **Se estudia junto con:** sustitución, diferencial, función interior, exterior.

📘 **Dónde se aprende** (1 clase): [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md).

### Masa de despegue

- La masa de despegue (GLOW) es la masa total en el instante de ignición.
- La masa de despegue es la masa total al inicio.

💡 **Cómo se explica en la clase [B77-C01](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md):**
- La carga útil es `2,32 %` de la masa de despegue.
- La masa de despegue depende de cómo se reparta `ΔV`.
- ⚠️ **Error frecuente:** Tomar la masa de despegue sintética por la de un vehículo real. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Un requisito de velocidad no dice cuánto pesa el vehículo. La decisión central: ¿cómo se reparte la velocidad entre dos etapas para que la masa de despegue sea mínima, y qué parte de esa masa es carga útil?
- 🔗 **Se estudia junto con:** etapa, coeficiente estructural, razón de carga útil, relación empuje–peso.

📘 **Dónde se aprende** (2 clases): [B77-C01 · Sistemas de lanzamiento](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md); [B77-C07 · Separación de etapas conceptual](../programa/clases/B77/B77-C07-separacion-de-etapas-conceptual/CLASE.md).

### Masa de equilibrio

- La masa de equilibrio de la planta es la que anula el ahorro.

💡 **Cómo se explica en la clase [B59-C01](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *ficha del concepto ISRU*: propelente, partición O/F, masas aterrizada y en LEO con y sin ISRU, masa de equilibrio y sensibilidad al Isp.
- Masa de planta de equilibrio para un solo ascenso = 4267 kg
- 🎯 **Por qué importa:** Cada kilogramo que se lanza arrastra consigo más propelente para lanzarlo. La decisión central: ¿cuánta masa de planta de producción compensa el oxidante que dejas de llevar?
- 🔗 **Se estudia junto con:** utilización de recursos in situ (ISRU), propelente, razón O/F, apalancamiento.

📘 **Dónde se aprende** (1 clase): [B59-C01 · Concepto de utilización de recursos in situ](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md).

### Masa de Hills

- La masa de Hills es el valor para el que `r_t = r_s`.

💡 **Cómo se explica en la clase [B27-C16](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md):**
- *Descripción textual:* de la estrella y la masa del agujero se obtienen el radio de marea y la dispersión de energía; de ahí salen el tiempo mínimo y la ley de caída; igualar `r_t` con el radio de Schwarzschild da la masa de Hills.
- Obtener la masa de Hills por fórmula y por bisección.
- ⚠️ **Error frecuente:** Ignorar la masa de Hills. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Estos eventos iluminan agujeros negros inactivos y permiten estimar su masa. Gezari revisa 56 de ellos (S3, resumen).
- 🔗 **Se estudia junto con:** radio de marea, dispersión de energía, tiempo mínimo de retorno, tasa de retorno.

📘 **Dónde se aprende** (1 clase): [B27-C16 · Eventos de disrupción por marea](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md).

### Masa de Jeans

- La masa de Jeans `M_J` es la masa contenida en una esfera de diámetro `λ_J`.
- La masa de Jeans es la masa mínima que una nube isoterma necesita para que su gravedad venza a la presión del gas.

💡 **Cómo se explica en la clase [B24-C01](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md):**
- La masa de Jeans es la de una esfera de diámetro `λ_J`: `M_J = (4π/3) ρ (λ_J/2)³ = π^{5/2} c_s³ / (6 G^{3/2} ρ^{1/2})`.
- El criterio de Jeans da una escala de referencia, no una predicción exacta de la masa de las estrellas.
- 🎯 **Por qué importa:** Toda estrella es un trozo de gas interestelar que se contrajo. Sin saber cuándo la gravedad vence a la presión no se entiende por qué las estrellas nacen en nubes frías y densas y no en el gas tenue del medio interestelar, ni por qué la masa de las estrellas depende del entorno.
- 🔗 **Se estudia junto con:** nube molecular, núcleo denso, velocidad del sonido isoterma, longitud de Jeans.

📘 **Dónde se aprende** (2 clases): [B24-C01 · Colapso de nubes moleculares](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md); [B52-C01 · Colapso de nebulosa protosolar](../programa/clases/B52/B52-C01-colapso-de-nebulosa-protosolar/CLASE.md).

### Masa de la atmósfera

- La masa de la atmósfera es la columna `P₀/g` por la superficie `4πr²`.
- La masa de la atmósfera es `A P/g` con `A = 4πr²`.

💡 **Cómo se explica en la clase [B54-C13](../programa/clases/B54/B54-C13-atmosfera-de-venus/CLASE.md):**
- *Descripción textual:* la ficha y el `c_p` ilustrativo dan `κ`; con él se obtiene `T(P)` y por integración `z(P)`; la ficha da también la masa de la atmósfera.
- Calcular la masa de la atmósfera `4πr²P₀/g`.
- 🎯 **Por qué importa:** Venus es el caso extremo de atmósfera densa y caliente. La pregunta motivadora: ¿cómo se enfría su atmósfera con la altura y cuánto pesa?
- 🔗 **Se estudia junto con:** adiabata, altura sobre la superficie, CO₂ supercrítico.

📘 **Dónde se aprende** (2 clases): [B54-C13 · Atmósfera de Venus](../programa/clases/B54/B54-C13-atmosfera-de-venus/CLASE.md); [B54-C14 · Atmósfera de Marte](../programa/clases/B54/B54-C14-atmosfera-de-marte/CLASE.md).

### Masa de la batería

- La masa de la batería es `E/(DoD η ρ)`.

💡 **Cómo se explica en la clase [B86-C22](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md):**
- *Descripción textual:* el periodo sinódico da la duración de la noche; con la carga de supervivencia se obtiene la energía; ésta fija la masa de batería y de pila, mientras el RTG se dimensiona por potencia; la comparación da el mejor sistema y los cruces.
- Descripción larga: la masa de la batería crece en proporción a la energía y la noche la hace muy pesada; el generador radioisotópico tiene una masa fija por unidad y supera a la batería desde unos pocos vatios; en este modelo la pila es la más liviana, pero es una cota optimista.
- 🎯 **Por qué importa:** Una batería dimensionada para un eclipse orbital no sirve para una noche lunar: la energía crece unas doscientas veces y la masa de la batería deja de ser razonable. Por eso la estrategia cambia de almacenar a generar de otra manera.
- 🔗 **Se estudia junto con:** noche lunar, carga de supervivencia, unidad, cruce.

📘 **Dónde se aprende** (1 clase): [B86-C22 · Suministro de energía durante la noche lunar](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md).

### Masa de potencia

- La masa de potencia es la masa de la fuente que alimenta la planta.

💡 **Cómo se explica en la clase [B59-C19](../programa/clases/B59/B59-C19-evaluacion-logistica-de-una-instalacion/CLASE.md):**
- Ejercicio 1 · con los pasos indicados. Masa de potencia (8.1).
- Masa total = planta 2000 + potencia 360 = 2360 kg ; disponibilidad u = 0.9259
- ⚠️ **Error frecuente:** Olvidar la masa de la fuente de potencia. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una planta que produce 10 kg/día no se paga sola si está parada. La decisión central: ¿cuántos días de operación hacen falta para que la masa de producto evitada iguale la masa de la planta?
- 🔗 **Se estudia junto con:** amortización, apalancamiento, paradas.

📘 **Dónde se aprende** (1 clase): [B59-C19 · Evaluación logística de una instalación](../programa/clases/B59/B59-C19-evaluacion-logistica-de-una-instalacion/CLASE.md).

### Masa de propelente

- La masa de propelente es `m_p = m₀(1 − 1/MR)`.

💡 **Cómo se explica en la clase [B77-C05](../programa/clases/B77/B77-C05-ecuacion-de-cohete-ideal/CLASE.md):**
- Eso implica que el propelente es `89,1 %` de la masa de despegue.
- *Descripción textual:* el impulso específico da la velocidad equivalente de escape; con la razón de masas se obtiene el `Δv` ideal, al que se resta la pérdida por gravedad y del que sale la masa de propelente.
- 🎯 **Por qué importa:** El propelente es casi toda la masa de un lanzador porque la velocidad crece solo con el logaritmo de la razón de masas. La decisión central: ¿qué razón de masas y qué `Isp` hacen falta para un `ΔV` dado, y qué parte se pierde por gravedad?
- 🔗 **Se estudia junto con:** velocidad de escape equivalente, razón de masas, cambio de velocidad ideal, tiempo de combustión.

📘 **Dónde se aprende** (1 clase): [B77-C05 · Ecuación de cohete ideal](../programa/clases/B77/B77-C05-ecuacion-de-cohete-ideal/CLASE.md).

### Masa del disco

- La masa del disco es `2π∫Σ r dr`.

💡 **Cómo se explica en la clase [B52-C02](../programa/clases/B52/B52-C02-discos-protoplanetarios/CLASE.md):**
- Con `Σ = 10⁴ kg/m²·(r/ua)^(−1,5)` y `T = 280 K·(r/ua)^(−1/2)` entre 0,1 y 100 ua, el disco sintético tiene `0.01370 M☉` (unos 14 masas de Júpiter si se cuenta `M☉/M_J ≈ 1050`, valor que se da solo como orden de magnitud no consultado).
- Descripción larga: la masa del disco es un pequeño porcentaje de la estelar, el disco se ensancha hacia afuera y `Q` se mantiene muy por encima de 1.
- 🎯 **Por qué importa:** Todo lo que sigue —deriva del polvo, crecimiento, migración— ocurre dentro de un disco y depende de cuánta masa tiene, cuán caliente y cuán grueso es. La decisión central: ¿cómo se resume un disco con tres funciones del radio y cuándo es estable?
- 🔗 **Se estudia junto con:** densidad superficial, escala de altura, parámetro de Toomre, ley de potencias.

📘 **Dónde se aprende** (1 clase): [B52-C02 · Discos protoplanetarios](../programa/clases/B52/B52-C02-discos-protoplanetarios/CLASE.md).

### Masa dinámica

- La masa dinámica dentro de `r` es `v²r/G`.

💡 **Cómo se explica en la clase [B26-C18](../programa/clases/B26/B26-C18-materia-oscura-y-evidencias/CLASE.md):**
- Es decir, tres cuartas partes de la masa dinámica de este ejemplo no son barionicas.
- Dinámica (curvas de rotación): la masa total dentro de un radio.
- 🎯 **Por qué importa:** Si las estrellas y el gas fueran toda la masa, las estrellas de los bordes de una galaxia irían más despacio que las del centro; observaciones de este tipo y de lentes gravitacionales indican que hay mucha más masa que la que se ve.
- 🔗 **Se estudia junto con:** curva de rotación, materia oscura, halo, halo pseudo-isotermo.

📘 **Dónde se aprende** (1 clase): [B26-C18 · Materia oscura y evidencias](../programa/clases/B26/B26-C18-materia-oscura-y-evidencias/CLASE.md).

### Masa efectiva

- La masa efectiva de un modo es `(φᵀ M r)²` con `φ` normalizado a masa unitaria y `r` la traslación de sólido rígido; mide cuánta masa mueve el modo.

💡 **Cómo se explica en la clase [B84-C10](../programa/clases/B84/B84-C10-analisis-modal/CLASE.md):**
- *Descripción textual:* se ensamblan `K` y `M`, se restringe el empotramiento, se resuelve el problema generalizado y se calculan frecuencias y masas efectivas, que se comparan con la solución analítica.
- Calcular factores de participación y masas efectivas.
- ⚠️ **Error frecuente:** Ignorar la masa efectiva. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un satélite cuyo primer modo cae dentro del rango excitado por el lanzador se amplifica; los modos con más masa efectiva son los que importan. La decisión central: ¿qué modos importan, con qué frecuencia y qué fracción de masa mueven?
- 🔗 **Se estudia junto con:** modo, significativo.

📘 **Dónde se aprende** (1 clase): [B84-C10 · Análisis modal](../programa/clases/B84/B84-C10-analisis-modal/CLASE.md).

### Masa encerrada

- La masa encerrada `M(<r)` es la masa dentro del radio `r`.
- La masa encerrada `M(<r)`.

💡 **Cómo se explica en la clase [B09-C20](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md):**
- *Descripción textual:* según el punto esté fuera o dentro, el campo depende de la masa total o de la masa encerrada; las correcciones por achatamiento y rotación se añaden afuera y el perfil de densidad decide dentro; se comprueba con casos límite.
- Teorema de la capa y masa encerrada: sirve para esferas con perfil radial.
- 🎯 **Por qué importa:** Una sonda en órbita, un satélite geodésico o un gravímetro en una montaña reciben la atracción de un cuerpo que no es un punto: tiene tamaño, forma achatada, rotación y estructura interna. Reducirlo a un punto es correcto fuera de una esfera homogénea, pero deja de serlo cuando importa el achatamiento o el interior.
- 🔗 **Se estudia junto con:** teorema de la capa, potencial de una capa, achatamiento, J₂.

📘 **Dónde se aprende** (2 clases): [B09-C20 · Aplicaciones a campos gravitatorios](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md); [B38-C05 · Potenciales galácticos: Plummer, Miyamoto-Nagai y NFW](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md).

### Masa específica

- La masa específica `α` es kg de planta por kW.
- La masa específica de la potencia convierte kW en kg.

💡 **Contexto en la clase [B59-C20](../programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/CLASE.md):**
- **Idea central (modelo mental):** Como un presupuesto donde cada partida es un gasto y el total debe cuadrar: se ve qué partida pesa más y qué ahorro importa. Límite: aquí no hay costes monetarios, solo masa y energía.
- 🎯 **Por qué importa:** Un diseño conceptual no es un número sino un conjunto coherente. La decisión central: ¿qué potencia y qué masa necesita una planta que produce 10 t de agua al año, y qué parámetro la gobierna?
- 🔗 **Se estudia junto con:** libro de energía, potencia de diseño, diseño conceptual, sensibilidad.

📘 **Dónde se aprende** (2 clases): [B59-C20 · Diseño conceptual de planta ISRU](../programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/CLASE.md); [B78-C15 · Propulsión nuclear eléctrica conceptual](../programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/CLASE.md).

### Masa final

- La masa inicial `m₀` incluye el propelente; la masa final `m_f`, no.

💡 **Cómo se explica en la clase [B78-C02](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md):**
- *Descripción textual:* la carga útil, el motor y los tanques fijan la masa final; sumada al propelente da la masa inicial; el cociente y el `Isp` dan el Δv.
- ⚠️ **Error frecuente:** Contar el propelente en la masa final. Se corrige con 8.1.
- 🎯 **Por qué importa:** Más propelente da más Δv, pero cada kilo de propelente exige tanques, y esos tanques también se aceleran. La decisión central: ¿cuánto propelente hace falta para un Δv dado y existe un máximo de Δv que ninguna cantidad de propelente supera?
- 🔗 **Se estudia junto con:** ecuación del cohete, masa inicial, fracción de tanques, cota de Δv.

📘 **Dónde se aprende** (1 clase): [B78-C02 · Propulsión química como sistema físico](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md).

### Masa formular

- La masa formular es la masa molar de la fórmula; la estabilidad de un hielo, en esta clase, es el intervalo de presiones y temperaturas donde no sublima (C11).

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Un olivino con 90 % de forsterita y 10 % de fayalita (Fo₉₀) tiene una masa formular que es el promedio ponderado de las dos: `0,9 × 140,6936 + 0,1 × 203,7726 = 147,0015 g/mol`.
- Calcular la masa formular y el porcentaje en masa de elementos en un hielo o un mineral.
- ⚠️ **Error frecuente:** Confundir la masa formular de olivino con la de piroxeno. Se corrige con el ejercicio 1.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).
- 🔗 **Se estudia junto con:** hielo, mineral, olivino, forsterita.

📘 **Dónde se aprende** (1 clase): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md).

### Masa hidrostática

- La masa hidrostática es `M(<r) = −(kT r/(G μ m_p)) d ln ρ/d ln r`, con `μ = 0,6` la masa media por partícula en unidades de `m_p` (valor ilustrativo).

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- Supone esferidad, isotermia y equilibrio, sin presión no térmica (turbulencia, rayos cósmicos, campo) que, si existe, hace que la masa hidrostática subestime la verdadera.
- *Descripción textual:* con la temperatura y la forma del gas se obtiene la masa hidrostática; con la dispersión de las galaxias, la de una esfera isoterma; se comparan, y el perfil de gas da su masa y la fracción respecto del total.
- ⚠️ **Error frecuente:** Tomar la masa hidrostática como exacta. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.
- 🔗 **Se estudia junto con:** cúmulo de galaxias, medio intracúmulo (ICM), temperatura, equilibrio hidrostático.

📘 **Dónde se aprende** (1 clase): [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md).

### Masa inercial

- La masa inercial `m` mide la resistencia de un cuerpo a cambiar su velocidad (kg).

💡 **Contexto en la clase [B05-C04](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md):**
- **Idea central (modelo mental):** La mecánica newtoniana es una receta repetible: eliges el cuerpo, enumeras lo que lo empuja o tira, sumas y obtienes la aceleración; luego integras en el tiempo para obtener velocidad y posición.
- 🎯 **Por qué importa:** Un satélite no tiene motor encendido y aun así gira. Una nave en el espacio vacío mantiene su velocidad sin esfuerzo.
- 🔗 **Se estudia junto con:** fuerza, fuerza neta, marco inercial, peso.

📘 **Dónde se aprende** (1 clase): [B05-C04 · Leyes del movimiento de Newton](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md).

### Masa inicial

- La masa inicial `m₀` incluye el propelente; la masa final `m_f`, no.

💡 **Cómo se explica en la clase [B78-C02](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md):**
- *Descripción textual:* la carga útil, el motor y los tanques fijan la masa final; sumada al propelente da la masa inicial; el cociente y el `Isp` dan el Δv.
- 🎯 **Por qué importa:** Más propelente da más Δv, pero cada kilo de propelente exige tanques, y esos tanques también se aceleran. La decisión central: ¿cuánto propelente hace falta para un Δv dado y existe un máximo de Δv que ninguna cantidad de propelente supera?
- 🔗 **Se estudia junto con:** ecuación del cohete, masa final, fracción de tanques, cota de Δv.

📘 **Dónde se aprende** (1 clase): [B78-C02 · Propulsión química como sistema físico](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md).

### Masa interior

- La masa interior `M(<R)` es la masa dentro de la esfera de radio `R`.
- La masa interior NFW es `M(<r) = 4πρ_s r_s³ [ln(1 + x) − x/(1 + x)]`, con `x = r/r_s`.

💡 **Cómo se explica en la clase [B25-C01](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md):**
- A["Medir R0 y Theta0<br/>(máseres, órbitas, cefeidas)"] --> B["Masa interior<br/>M(<R) = Theta² R / G"]
- *Descripción textual:* de la distancia y la velocidad del Sol se obtiene la masa interior; del disco exponencial, la masa estelar; si la segunda es mucho menor que la primera, hay masa no luminosa.
- 🎯 **Por qué importa:** Estamos dentro de la galaxia y no podemos fotografiarla desde fuera: su forma se reconstruye midiendo distancias y velocidades desde un punto que no es el centro. Sin un esquema claro de componentes (bulbo, barra, disco, halo) y de cifras de referencia, el resto del bloque carece de escala.
- 🔗 **Se estudia junto con:** Vía Láctea, bulbo, barra, disco.

📘 **Dónde se aprende** (2 clases): [B25-C01 · Estructura de la Vía Láctea](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md); [B25-C15 · Materia oscura en galaxias](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md).

### Masa invariante

- La masa invariante de un sistema es `√(E² − (pc)²)/c²`: puede ser mayor que la suma de las masas en reposo.

💡 **Cómo se explica en la clase [B26-C05](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md):**
- El sistema de dos fotones tiene masa invariante `2m_e`, pese a que cada fotón no tiene masa.
- Distinguir masa invariante de masa «relativista».
- ⚠️ **Error frecuente:** Decir que la masa «crece» con la velocidad. Se corrige con la sección 6: la masa invariante no cambia.
- 🎯 **Por qué importa:** El Sol, un acelerador de partículas y la fusión de dos agujeros negros son balances de masa y energía. Para calcularlos hay que saber cuánta energía tiene una partícula en reposo y en movimiento, y por qué no puede acelerarse hasta `c`.
- 🔗 **Se estudia junto con:** energía de reposo, energía total, momento relativista, energía cinética.

📘 **Dónde se aprende** (2 clases): [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md); [B31-C12 · Antimateria y aniquilación](../programa/clases/B31/B31-C12-antimateria-y-aniquilacion/CLASE.md).

### Masa M₂₀₀

- La masa `M₂₀₀` es la contenida en el radio `r₂₀₀` dentro del cual la densidad media es `200 ρ_crit`.

💡 **Cómo se explica en la clase [B25-C15](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md):**
- Ese es el ejemplo conductor: un halo NFW con `M₂₀₀ = 1,3 × 10¹² M☉` (simplificación de esta clase: se usa la masa virial de S4 como `M₂₀₀`) y `c = 16`.
- Límites: halo esférico sin bariones, `M₂₀₀` tomado de la masa virial de S4.
- ⚠️ **Error frecuente:** Tomar la masa virial como `M₂₀₀` sin avisar. Se corrige en la sección 5 y la 10.
- 🎯 **Por qué importa:** Varias medidas independientes (rotación, dispersión, lentes, fondo cósmico) piden más masa de la que se ve. Un halo con un perfil de densidad concreto permite comparar esas medidas entre sí y con las simulaciones.
- 🔗 **Se estudia junto con:** materia oscura, halo, perfil NFW, densidad crítica.

📘 **Dónde se aprende** (1 clase): [B25-C15 · Materia oscura en galaxias](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md).

### Masa máxima

- La masa máxima es la mayor masa estable.
- La masa máxima `M_max` y el radio de 1,4 `M☉` `R_{1,4}` son los dos resúmenes de una EOS.

💡 **Cómo se explica en la clase [B27-C03](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md):**
- La masa máxima de esta EOS (`1,055 M☉`) queda por debajo de `2,01` y `2,14 M☉` (S3, S4): esta ecuación de estado queda excluida.
- *Descripción textual:* con la ecuación de estado y una densidad central se integra TOV hasta que la presión se anula; la familia `(M, R)` tiene una masa máxima, y se contrasta con las medidas.
- 🎯 **Por qué importa:** Las masas y radios de las estrellas de neutrones son la mejor ventana a la materia a densidades nucleares. Para interpretarlos hay que saber qué cambia la relatividad respecto de Newton y por qué existe una masa máxima.
- 🔗 **Se estudia junto con:** ecuación TOV, densidad de energía, ecuación de estado, politropo.

📘 **Dónde se aprende** (2 clases): [B27-C03 · Estrellas de neutrones](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md); [B27-C04 · Ecuación de estado nuclear](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md).

### Masa media

- La masa media `m(z)` decrece con la altitud al dominar los gases ligeros.

💡 **Cómo se explica en la clase [B72-C07](../programa/clases/B72/B72-C07-modelos-de-densidad-atmosferica/CLASE.md):**
- *Descripción textual:* la temperatura, la masa media y la gravedad entran en la ecuación hidrostática; su integral da la densidad; la versión isoterma sirve de verificación.
- Las temperaturas, la base de `2,2 × 10⁻⁸ kg/m³` a `120 km` y la masa media son ilustrativas.
- 🎯 **Por qué importa:** El arrastre es tan incierto como la densidad que se le da. La decisión central: ¿cuánto puede variar la densidad a una altitud dada si cambia la temperatura de la termosfera, y qué incertidumbre hereda por eso un cálculo de decaimiento?
- 🔗 **Se estudia junto con:** temperatura exosférica, perfil de Bates, altura de escala, modelo empírico operativo.

📘 **Dónde se aprende** (1 clase): [B72-C07 · Modelos de densidad atmosférica](../programa/clases/B72/B72-C07-modelos-de-densidad-atmosferica/CLASE.md).

### Masa mínima

- La masa mínima `Mp sin i`.

💡 **Cómo se explica en la clase [B29-C03](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md):**
- Una semiamplitud de `10 m/s` con `P = 30 d` alrededor de una estrella de `1 M☉` corresponde a una masa mínima de `0,153 M_J` (valor derivado del cociente con el `K` de Júpiter a ese periodo).
- Ejercicio 8. Masa mínima si `K` se triplica a igual `P`.
- 🎯 **Por qué importa:** La velocidad radial da la masa mínima del planeta, que el tránsito no da. Combinados, dan la densidad.
- 🔗 **Se estudia junto con:** semiamplitud, anomalía media, ecuación de Kepler, argumento del periastro.

📘 **Dónde se aprende** (1 clase): [B29-C03 · Velocidad radial estelar](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md).

### Masa molar

- La masa molar `M` es la masa de un mol de una sustancia: se mide en g/mol y, para un elemento, coincide numéricamente con su peso atómico (C03).
- La masa molar `M` es la del gas de escape.
- La masa molar `M` se expresa en g/mol.

💡 **Cómo se explica en la clase [B06-C06](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md):**
- Por eso «el peso atómico en u» y «la masa molar en g/mol» tienen el mismo número.
- De masa a cantidad se divide entre la masa molar; de cantidad a número de partículas se multiplica por la constante de Avogadro; las flechas inversas deshacen cada paso.
- 🎯 **Por qué importa:** La misión OSIRIS-REx trajo a la Tierra 121,6 g de material del asteroide Bennu. Los análisis de laboratorio de una parte de esa muestra encontraron entre 4,5 y 4,7 % de carbono y entre 0,23 y 0,25 % de nitrógeno en masa (S1).
- 🔗 **Se estudia junto con:** cantidad de sustancia, mol, constante de Avogadro, unidad de masa atómica.

📘 **Dónde se aprende** (3 clases): [B06-C06 · Cantidad de sustancia y mol](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md); [B78-C03 · Termodinámica de cámaras](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md); [B119-C23 · Protección ambiental de las actividades de lanzamiento](../programa/clases/B119/B119-C23-proteccion-ambiental-de-las-actividades-de-lanzamiento/CLASE.md).

### Masa molar baja

- La masa molar baja del hidrógeno sube el escape.

💡 **Cómo se explica en la clase [B78-C14](../programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md):**
- A igual `T`, `Vₑ(H₂)/Vₑ(CH₄) = 2,8207 = √(16,04/2,016)`: la masa molar baja es la clave.
- Descripción larga: el escape crece con `√(T/M)`; la masa molar baja del hidrógeno aporta un factor 2,8 sobre el metano.
- 🎯 **Por qué importa:** Un cohete químico limita su `Isp` por la química del propelente; uno térmico lo limita por la temperatura que aguanta el núcleo. La decisión central: ¿cuánto `Isp` puede dar un gas de baja masa molar calentado a una temperatura dada y qué empuje corresponde a una potencia térmica?
- 🔗 **Se estudia junto con:** cohete térmico, núcleo, temperatura del núcleo, empuje por potencia térmica.

📘 **Dónde se aprende** (1 clase): [B78-C14 · Propulsión nuclear térmica conceptual](../programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md).

### Masa molar media

- La masa molar media de una mezcla es `M̄ = Σ y_i M_i`.
- La masa molar media `M` es el promedio de las masas molares ponderado por las fracciones.
- La masa molar media es la masa de los productos entre sus moles.

💡 **Cómo se explica en la clase [B06-C07](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md):**
- Un componente «importa» según su fracción y según cuánto se aparta su masa molar de la media.
- G["Mezcla: fracciones molares y_i"] -->|"suma de y_i × M_i"| MM["Masa molar media M̄"]
- 🎯 **Por qué importa:** Si quieres saber cuánto pesa una columna de atmósfera de Marte, necesitas su masa molar media, y para eso, su composición. La NASA publica la composición en volumen de las atmósferas de Marte, Venus y la Tierra y también un «peso molecular» medio (S1, S2, S3).
- 🔗 **Se estudia junto con:** fórmula molecular, fórmula empírica, composición porcentual, fracción molar.

📘 **Dónde se aprende** (3 clases): [B06-C07 · Estequiometría elemental](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md); [B54-C02 · Composición química atmosférica](../programa/clases/B54/B54-C02-composicion-quimica-atmosferica/CLASE.md); [B78-C04 · Propulsión monopropelente conceptual](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md).

### Masa molecular media

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B29-C11](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md):**
- **Idea central (modelo mental):** Una moneda con un halo borroso tapa un poco más que la moneda sola. El ancho del halo es el espesor de la atmósfera efectiva, de unas cuantas alturas de escala.
- 🎯 **Por qué importa:** Los planetas inflados y calientes tienen señales de cientos de ppm; las Tierras alrededor de estrellas como el Sol, de ~1 ppm, que no se alcanzan. La decisión central: ¿qué señal produce una atmósfera dada y cuántos tránsitos hacen falta para verla?
- 🔗 **Se estudia junto con:** altura de escala, señal de transmisión, anillo atmosférico, detección a 5σ.

📘 **Dónde se aprende** (1 clase): [B29-C11 · Atmósferas exoplanetarias](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md).

### Masa neta

- La masa neta es la de los consumibles.

💡 **Cómo se explica en la clase [B100-C02](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md):**
- *Descripción textual:* la carga neta se infla por el embalaje y los repuestos, y luego se calcula, tramo a tramo y hacia atrás, la masa que debe existir antes de cada maniobra.
- Añadir embalaje y repuestos como factores sobre la masa neta.
- 🎯 **Por qué importa:** La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: ¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?
- 🔗 **Se estudia junto con:** factor de embalaje, repuestos, ecuación ideal del cohete, factor de crecimiento de masa.

📘 **Dónde se aprende** (1 clase): [B100-C02 · Dimensionamiento de carga y volumen de misión](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md).

### Masa perdida total (TML)

- La masa perdida total (TML) y los volátiles condensables (CVCM) miden la desgasificación de un material.

💡 **Contexto en la clase [B85-C12](../programa/clases/B85/B85-C12-entorno-de-vacio/CLASE.md):**
- 🎯 **Por qué importa:** El vacío cambia cómo el gas conduce el calor, cómo se desgasifican los materiales y cuánto tarda un ensayo. La decisión central: ¿cuánto tarda una cámara en llegar a la presión de ensayo y qué la limita?
- 🔗 **Se estudia junto con:** camino libre medio, número de Knudsen, velocidad de bombeo, carga de gas.

📘 **Dónde se aprende** (1 clase): [B85-C12 · Entorno de vacío](../programa/clases/B85/B85-C12-entorno-de-vacio/CLASE.md).

### Masa por área

- La masa por área (espesor másico) es lo que cuenta para el blindaje.

💡 **Cómo se explica en la clase [B59-C11](../programa/clases/B59/B59-C11-construccion-con-regolito/CLASE.md):**
- RHO["ρ(z)"] --> INT["∫ρ dz: masa por área"]
- *Descripción textual:* la densidad integrada da la masa por área; con la gravedad da la sobrecarga; con la presión interna fija la profundidad de equilibrio; en g/cm² fija la transmisión de radiación.
- 🎯 **Por qué importa:** Enterrar o cubrir un hábitat con regolito protege, pero no sustituye a la estructura. La decisión central: ¿cuánto espesor de regolito hace falta para blindar y cuánto para contener la presión interna?
- 🔗 **Se estudia junto con:** sobrecarga, densidad aparente, esfuerzo de aro, longitud de atenuación.

📘 **Dónde se aprende** (1 clase): [B59-C11 · Construcción con regolito](../programa/clases/B59/B59-C11-construccion-con-regolito/CLASE.md).

### Masa proyectada

- La masa proyectada es `m_reg = m_agua/x`.

💡 **Cómo se explica en la clase [B59-C02](../programa/clases/B59/B59-C02-prospeccion-de-hielo-lunar/CLASE.md):**
- Despejar la masa de regolito proyectada desde la masa de agua y la abundancia.
- Ejercicio 12 · integrador. Elabora tu *ficha de la prospección de hielo*: datos observados con fuente, masa proyectada, incertidumbre por dos métodos, rango de un depósito hipotético y límites.
- 🎯 **Por qué importa:** Un recurso no se planifica con un valor central sino con un rango. La decisión central: ¿cuánto regolito hay que procesar si la abundancia es 2,7 % en vez de 5,6 %?
- 🔗 **Se estudia junto con:** abundancia, propagación de primer orden, cola larga, zonas de sombra permanente.

📘 **Dónde se aprende** (1 clase): [B59-C02 · Prospección de hielo lunar](../programa/clases/B59/B59-C02-prospeccion-de-hielo-lunar/CLASE.md).

### Masa reducida

- La masa reducida `m₁m₂/(m₁ + m₂)` es la masa del cuerpo ficticio.
- La masa reducida `R_M = R_∞/(1 + m_e/M)`.
- La masa reducida `μ` resume las dos masas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B45-C10](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md):**
- El factor de masa reducida del hidrógeno es `0,99945568`.
- *Descripción textual:* la constante de Rydberg con masa reducida da las longitudes de onda y el ruido de fotones fija la precisión del centroide.
- ⚠️ **Error frecuente:** Olvidar la masa reducida. Se corrige con 8.2.
- 🎯 **Por qué importa:** Las líneas de emisión identifican elementos y miden velocidad y flujo. La decisión central: ¿dónde está cada línea del hidrógeno y con qué precisión se mide su posición?
- 🔗 **Se estudia junto con:** serie de Lyman, Balmer, Paschen, constante de Rydberg.

📘 **Dónde se aprende** (6 clases): [B36-C10 · Búsqueda directa de materia oscura en laboratorio](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md); [B45-C10 · Líneas de emisión](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md); [B60-C01 · Colisiones moleculares y secciones eficaces en gas interestelar](../programa/clases/B60/B60-C01-colisiones-moleculares-y-secciones-eficaces-en-gas-interestelar/CLASE.md); [B71-C02 · Ley de gravitación universal](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md); [B71-C03 · Ecuación de movimiento de dos cuerpos](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md); [B76-C16 · Acoplamiento y captura](../programa/clases/B76/B76-C16-acoplamiento-y-captura/CLASE.md).

### Masa seca

- La masa seca es la de la nave sin propelente.
- La masa seca es la masa final sin propulsante.
- La masa seca es la masa sin propelente.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B56-C20](../programa/clases/B56/B56-C20-diseno-de-mision-astrobiologica-conceptual/CLASE.md):**
- Con `Isp = 320 s` y masa seca `1000 kg` (sintéticos): para `Δv = 2,945 km/s`, `m₀/m_f = 2,556` y propelente `1556 kg`; para `Δv = 5,594 km/s` (salida más llegada), `5,946` y `4946 kg`.
- *Descripción textual:* de la pregunta salen requisitos, categoría y carga útil; de la trayectoria, el Δv; con la masa seca se obtiene el propelente.
- 🎯 **Por qué importa:** Una misión que busca vida combina ciencia, ingeniería y protección planetaria. Para decidir si es viable hay que traducir la pregunta científica en requisitos y comprobar que el presupuesto cierra.
- 🔗 **Se estudia junto con:** requisito, verificación, Δv, transferencia de Hohmann.

📘 **Dónde se aprende** (5 clases): [B56-C20 · Diseño de misión astrobiológica conceptual](../programa/clases/B56/B56-C20-diseno-de-mision-astrobiologica-conceptual/CLASE.md); [B75-C09 · Presupuestos de delta-v](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md); [B78-C02 · Propulsión química como sistema físico](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md); [B78-C17 · Masa de propelente y presupuesto](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md); [B106-C10 · Gestión de residuos humanos](../programa/clases/B106/B106-C10-gestion-de-residuos-humanos/CLASE.md).

### Masa térmica

- La masa térmica `M_th = c_s³/(GΩ) = h³M*` es la masa donde `R_B ~ R_H`.

💡 **Cómo se explica en la clase [B52-C08](../programa/clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md):**
- La masa térmica es `h³M* = 42.44 M⊕`; la otra vía, `c_s³/(GΩ)`, da lo mismo.
- *Descripción textual:* el disco da la masa térmica y el radio de Bondi; con el de Hill se obtiene el radio de captura; los guijarros fijan el tiempo de crecimiento.
- 🎯 **Por qué importa:** El orden de magnitud de la masa del núcleo y el tiempo en alcanzarlo deciden si hay gigantes gaseosos. La decisión central: ¿a qué masa un núcleo pasa de capturar gas hasta Bondi a capturarlo hasta Hill, y cuánto tarda en crecer?
- 🔗 **Se estudia junto con:** radio de Bondi, radio de Hill, acreción de guijarros.

📘 **Dónde se aprende** (1 clase): [B52-C08 · Formación de gigantes gaseosos](../programa/clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md).

### Máscara

- La máscara es la imagen binaria resultante.
- Una máscara es la imagen de etiquetas.
- La máscara es una imagen binaria de agua.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C13](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md):**
- Una máscara vacía («no hay manchas») acierta el 98,8 % de los píxeles del disco, porque las manchas ocupan el 1,165 % (179 de 15 361).
- El área medida es la suma de los píxeles de la máscara: 178 px, 1,159 % del disco (verdad: 179, 1,165 %).
- 🎯 **Por qué importa:** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.
- 🔗 **Se estudia junto con:** segmentación, umbralización, método de Otsu, varianza entre clases.

📘 **Dónde se aprende** (7 clases): [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md); [B40-C12 · Análisis de mapas del CMB: pixelización esférica y máscaras](../programa/clases/B40/B40-C12-analisis-de-mapas-del-cmb-pixelizacion-esferica-y-mascaras/CLASE.md); [B44-C15 · Píxeles defectuosos](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md); [B44-C20 · Pipeline inicial de calibración de imágenes](../programa/clases/B44/B44-C20-pipeline-inicial-de-calibracion-de-imagenes/CLASE.md); [B57-C15 · Sequías e inundaciones](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md) y 1 más.

### Máscara de elevación

- La máscara de elevación es el ángulo mínimo útil.
- El paso y la máscara de elevación.

💡 **Cómo se explica en la clase [B89-C14](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md):**
- Calcular el semiángulo central y la duración de una pasada cenital según la máscara de elevación.
- Duracion de una pasada cenital segun la mascara de elevacion:
- ⚠️ **Error frecuente:** Ignorar la máscara de elevación. Se corrige con 8.2.
- 🎯 **Por qué importa:** El tiempo de contacto es el recurso más escaso de un satélite de órbita baja: define cuántos datos bajan por día y cuántas estaciones se necesitan. La decisión central: ¿cuánto contacto y cuántos datos da una estación a un satélite de órbita baja?
- 🔗 **Se estudia junto con:** ángulo central, pasada, duración cenital, volumen de datos.

📘 **Dónde se aprende** (2 clases): [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md); [B89-C14 · Estaciones terrestres](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md).

### Máscara de transitabilidad

- La máscara de transitabilidad marca las celdas con pendiente menor que el umbral.

💡 **Cómo se explica en la clase [B53-C20](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md):**
- Definir y aplicar una máscara de transitabilidad.
- 🎯 **Por qué importa:** Un derivado sin verificar propaga errores a la decisión. La decisión central: ¿qué parte del terreno cumple un criterio de pendiente y existe un camino que lo respete?
- 🔗 **Se estudia junto con:** esquema de Horn, sombreado, búsqueda en anchura.

📘 **Dónde se aprende** (1 clase): [B53-C20 · Proyecto SIG de terreno extraterrestre](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md).

### Materia

- La materia puede estar en distintos estados, que se distinguen por la libertad de movimiento de sus partículas.
- Un campo oscilante en potencial cuadrático se comporta como materia (`w = 0`).

💡 **Cómo se explica en la clase [B06-C10](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md):**
- En el universo observable, la materia ordinaria que brilla, como las estrellas y el gas entre ellas, está en gran parte en estado de plasma (se estudia en B30).
- python programa/clases/B06/B06-C10-estados-de-la-materia/energia_termica.py
- 🎯 **Por qué importa:** En Marte, la temperatura media es 214 K y la presión media en superficie 6,36 mb (S1). Ese valor está casi en el punto triple del agua, la presión mínima a la que puede existir agua líquida (S2).
- 🔗 **Se estudia junto con:** estados, sólido, líquido, gas.

📘 **Dónde se aprende** (2 clases): [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md); [B40-C02 · Recalentamiento y transición a la era de radiación](../programa/clases/B40/B40-C02-recalentamiento-y-transicion-a-la-era-de-radiacion/CLASE.md).

### Materia oscura

- La materia oscura es materia que gravita pero no emite luz detectable; su naturaleza no se trata aquí.
- La materia oscura es materia que no emite ni absorbe luz de forma apreciable y se detecta por su gravedad.

💡 **Cómo se explica en la clase [B25-C15](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md):**
- La densidad del halo en `R₀` resulta `0,0130 M☉/pc³`, dentro de la barra de `0,013 ± 0,003` que S4 cita para la densidad local de materia oscura.
- La materia oscura es el `84 %` de la materia.
- ⚠️ **Error frecuente:** Concluir que el halo prueba la materia oscura. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Varias medidas independientes (rotación, dispersión, lentes, fondo cósmico) piden más masa de la que se ve. Un halo con un perfil de densidad concreto permite comparar esas medidas entre sí y con las simulaciones.
- 🔗 **Se estudia junto con:** halo, perfil NFW, densidad crítica, masa M₂₀₀.

📖 **Explicado a fondo:** [Materia oscura](esencial/esencial-m-z.md#materia-oscura) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B25-C15 · Materia oscura en galaxias](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md); [B26-C18 · Materia oscura y evidencias](../programa/clases/B26/B26-C18-materia-oscura-y-evidencias/CLASE.md).

### Matriz

- Una matriz `m × n` es una tabla de números con `m` filas y `n` columnas; actúa sobre un vector de `n` componentes y produce uno de `m` (S1 trata matrices como operadores lineales en §1.3(iv)).

💡 **Cómo se explica en la clase [B10-C03](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md):**
- Su matriz tiene esas imágenes en las columnas:
- Una matriz dice qué hace el operador con cada vector de la base; todo lo demás sale por linealidad.
- ⚠️ **Error frecuente:** Leer la matriz por filas en vez de por columnas. Se corrige con el ejercicio 1.
- 🎯 **Por qué importa:** Una estación terrestre está fija respecto de la Tierra, pero la Tierra gira respecto del espacio inercial. Para saber dónde está la estación en el sistema inercial a cada instante hay que aplicar una transformación que depende del tiempo.
- 🔗 **Se estudia junto con:** operador lineal, matriz de T en una base, producto matricial, matriz identidad.

📘 **Dónde se aprende** (1 clase): [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md).

### Matriz A

- La matriz `A` es la rigidez de membrana del laminado (N/m).

💡 **Cómo se explica en la clase [B84-C03](../programa/clases/B84/B84-C03-materiales-compuestos/CLASE.md):**
- Calcular la matriz de rigidez reducida `Q` de una lámina ortótropa.
- 🎯 **Por qué importa:** Un panel de fibra con las capas mal orientadas puede ser 14 veces más blando en una dirección que en otra sin que el material cambie. La decisión central: ¿cómo cambia la rigidez efectiva de un laminado según el ángulo de sus capas?
- 🔗 **Se estudia junto con:** lámina, matriz de rigidez reducida, cuasi-isótropo.

📘 **Dónde se aprende** (1 clase): [B84-C03 · Materiales compuestos](../programa/clases/B84/B84-C03-materiales-compuestos/CLASE.md).

### Matriz ABCD

- La matriz ABCD describe un bipuerto.

💡 **Contexto en la clase [B49-C10](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md):**
- **Idea central (modelo mental):** Como un colador: deja pasar lo que cabe y detiene lo demás; uno más fino detiene mejor pero deja pasar menos agua.
- 🎯 **Por qué importa:** Más orden rechaza más, pero también pierde más señal. La decisión central: ¿qué orden y qué ancho de banda dan el rechazo de imagen necesario con una pérdida aceptable?
- 🔗 **Se estudia junto con:** filtro de Butterworth, prototipo pasabajos, banda imagen, pérdida de inserción.

📘 **Dónde se aprende** (1 clase): [B49-C10 · Filtros de radiofrecuencia pasabanda y rechazo de banda imagen](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md).

### Matriz ampliada

- La matriz ampliada `[A | b]` junta los coeficientes y los términos independientes.

💡 **Cómo se explica en la clase [B10-C05](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md):**
- A["Matriz ampliada [A | b]"] --> B["Elegir pivote<br/>(mayor valor de la columna)"]
- 🎯 **Por qué importa:** Para fijar la posición de un objeto a partir de las distancias a tres estaciones se plantean tres ecuaciones con dos incógnitas (plano). Los sistemas reales tienen decenas o miles de incógnitas: parámetros orbitales, sesgos de relojes, coeficientes de calibración.
- 🔗 **Se estudia junto con:** sistema lineal, operación elemental de fila, eliminación gaussiana, sustitución hacia atrás.

📘 **Dónde se aprende** (1 clase): [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md).

### Matriz característica

- La matriz característica de una capa `[[cos δ, i sen δ/n],[i n sen δ, cos δ]]`.

💡 **Cómo se explica en la clase [B43-C24](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md):**
- Construir la matriz característica de una capa.
- 🎯 **Por qué importa:** Cada reflexión sin tratar pierde luz y añade luz parásita. La decisión central: ¿cuántas capas y con qué índices y espesores se logra baja reflectancia en la banda visible?
- 🔗 **Se estudia junto con:** espesor óptico, capa de cuarto de onda, reflectancia mínima, recubrimiento en V.

📘 **Dónde se aprende** (1 clase): [B43-C24 · Recubrimientos antirreflectantes de capas múltiples](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md).

### Matriz de actitud

- La matriz de actitud `A` (3×3, ortogonal, `det = +1`) lleva coordenadas de `I` a `B`.

💡 **Cómo se explica en la clase [B87-C02](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md):**
- Construir la matriz de actitud 3-2-1 y extraer de ella los tres ángulos.
- 🎯 **Por qué importa:** Casi todos los errores de actitud en software vienen de convenciones mezcladas: orden de ejes, sentido de la rotación, posición de la parte escalar. La decisión central: ¿qué representación uso para integrar, cuál para filtrar y cuál para mostrar?
- 🔗 **Se estudia junto con:** ángulos de Euler 3-2-1, cuaternión, eje-ángulo, doble cobertura.

📘 **Dónde se aprende** (1 clase): [B87-C02 · Representaciones de orientación](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md).

### Matriz de coherencia

- La matriz de coherencia `T = ⟨k kᴴ⟩` promedia.

💡 **Cómo se explica en la clase [B69-C04](../programa/clases/B69/B69-C04-polarimetria-sar/CLASE.md):**
- *Descripción textual:* la matriz de dispersión se transforma en el vector de Pauli, cuyas potencias identifican mecanismos, y su promedio da la matriz de coherencia y la entropía.
- Calcular la matriz de coherencia y la entropía.
- 🎯 **Por qué importa:** Con un solo canal no se distingue un suelo desnudo de un edificio. La decisión central: ¿qué mecanismo de dispersión domina en un pixel y qué conclusiones se pueden sacar con seguridad de las potencias de los canales?
- 🔗 **Se estudia junto con:** matriz de dispersión, vector de Pauli, span, entropía.

📘 **Dónde se aprende** (1 clase): [B69-C04 · Polarimetría SAR](../programa/clases/B69/B69-C04-polarimetria-sar/CLASE.md).

### Matriz de compatibilidad

- Holgura: diferencia de radio entre agujero y perno. Matriz de compatibilidad: tabla que cruza cada interfaz con su verificación.

💡 **Cómo se explica en la clase [B90-C05](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md):**
- La evidencia es el ICD verificado con su matriz de compatibilidad del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ICD verificado con su matriz de compatibilidad*: rangos, corrientes, margen, pila de tolerancias (WC y RSS), probabilidad de interferencia, hallazgos y lista de qué es consultado y sintético.
- 🎯 **Por qué importa:** La mayoría de los problemas de integración nacen en interfaces mal definidas: un equipo entrega 4,8 V y el otro necesita 4,9 V; un agujero admite 0,25 mm de desalineación y la pila de tolerancias llega a 0,40 mm. La decisión central: ¿las interfaces del ICD son compatibles antes de unir el hardware?
- 🔗 **Se estudia junto con:** ICD, Proveedor y consumidor, Margen, Peor caso.

📘 **Dónde se aprende** (1 clase): [B90-C05 · Documentación de interfaces](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md).

### Matriz de comprobación

- Un requisito es una condición medible que el sistema debe cumplir; una matriz de comprobación liga cada requisito con la prueba que lo verifica.

💡 **Cómo se explica en la clase [B25-C20](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md):**
- Redactar requisitos medibles para un clasificador y una matriz de comprobación.
- Ejercicio 8. Escribe la matriz de comprobación de R1–R6: ¿qué prueba verifica cada requisito?
- 🎯 **Por qué importa:** Clasificar galaxias a gran escala exige algo más que una regla que parezca razonable: hay que decir qué debe cumplir, probarlo contra casos de respuesta conocida y evaluar con honestidad cómo se comporta donde los datos son malos.
- 🔗 **Se estudia junto con:** concentración, descriptor, umbral, matriz de confusión.

📘 **Dónde se aprende** (1 clase): [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md).

### Matriz de confusión

- La matriz de confusión cuenta verdaderos positivos (`TP`), falsos negativos (`FN`), falsos positivos (`FP`) y verdaderos negativos (`TN`); aquí «positivo» es «esferoide».
- La matriz de confusión cuenta aciertos y confusiones.
- La matriz de confusión cuenta aciertos y errores: verdaderos positivos (TP), falsos positivos (FP), verdaderos negativos (TN) y falsos negativos (FN) (S2).
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- T["Muestras de prueba<br/>independientes"] --> V["Matriz de confusión,<br/>exactitud, kappa"]
- *Descripción textual:* las muestras etiquetadas entrenan un clasificador que se aplica a los píxeles; las muestras de prueba independientes, comparadas con la predicción, dan la matriz de confusión, la exactitud y el kappa.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, NDVI, clase, muestras de entrenamiento.

📘 **Dónde se aprende** (4 clases): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md); [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B96-C29 · Diagnóstico de fallas de enlace](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md).

### Matriz de control

- La matriz de control `C = (MᵀM+εI)⁻¹Mᵀ`.

💡 **Contexto en la clase [B42-C23](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md):**
- **Idea central (modelo mental):** Como afinar un piano tocando cada tecla: se aprende la respuesta de cada una, pero hay notas que el oído no distingue.
- 🎯 **Por qué importa:** Una matriz mal calibrada degrada el lazo y las aberraciones del camino de ciencia no las ve el sensor. La decisión central: ¿con qué amplitud calibrar y cómo corregir lo que el sensor no ve?
- 🔗 **Se estudia junto con:** matriz de interacción, empuje-tirón, valores singulares, NCPA.

📘 **Dónde se aprende** (1 clase): [B42-C23 · Calibración de la matriz de interacción y aberraciones no comunes](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md).

### Matriz de controlabilidad

- La matriz de controlabilidad es `𝒞 = [B, AB, A²B, …, Aⁿ⁻¹B]` y la de observabilidad es `𝒪 = [C;

💡 **Contexto en la clase [B16-C13](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md):**
- **Idea central (modelo mental):** Controlabilidad pregunta si tus palancas alcanzan todas las direcciones del espacio de estados. Observabilidad pregunta si tus ventanas ven todas las direcciones. Una variable que ni se mueve con tus palancas ni se ve con tus ventanas es invisible e incontrolable.
- 🎯 **Por qué importa:** Un satélite puede perder actuadores o sensores en vuelo. Antes de diseñar una ley de control conviene saber si el problema tiene solución: ninguna ley, por ingeniosa que sea, mueve un estado que ningún actuador alcanza, ni estima uno que ningún sensor ve.
- 🔗 **Se estudia junto con:** controlable, observable, observabilidad, prueba de Kalman.

📘 **Dónde se aprende** (1 clase): [B16-C13 · Observabilidad y controlabilidad](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md).

### Matriz de controlabilidad promedio

- La matriz de controlabilidad promedio `P̄` suma las proyecciones en una órbita.

💡 **Cómo se explica en la clase [B87-C12](../programa/clases/B87/B87-C12-magnetopares/CLASE.md):**
- Evaluar la controlabilidad con la matriz promedio `P̄ = ⟨I − B̂B̂ᵀ⟩`.
- matriz de controlabilidad promedio P = mean(I - Bh Bh^T): autovalores = [0.6015 0.6118 0.7867] ; suma = 2.0000 ; rango = 3
- 🎯 **Por qué importa:** Los magnetopares descargan ruedas (C14) y hacen detumbling (C16) con muy poca masa. La decisión central: ¿qué par se puede generar en cada instante, qué dirección queda inaccesible y basta una órbita para cubrir los tres ejes?
- 🔗 **Se estudia junto con:** momento dipolar, par magnético, par realizable, ley de proyección.

📘 **Dónde se aprende** (1 clase): [B87-C12 · Magnetopares](../programa/clases/B87/B87-C12-magnetopares/CLASE.md).

### Matriz de correlación

- La matriz de correlación tiene unos en la diagonal y los coeficientes `r = cov/(σσ)` fuera de ella (S1, C.3.6).

💡 **Cómo se explica en la clase [B12-C18](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md):**
- Una «matriz de correlación» con `r₁₂ = 0,9`, `r₁₃ = 0,9`, `r₂₃ = −0,9` parece razonable pero tiene un autovalor `−0,8`: no es semidefinida positiva, y la factorización de Cholesky falla.
- El suplemento 2 advierte que, al redondear una matriz de correlación, hay que cuidar que siga siendo semidefinida positiva (S2).
- 🎯 **Por qué importa:** El resultado de una determinación de órbita o de un ajuste no es un número sino un vector con una matriz de covarianza; sin ella no se puede propagar, comparar con otro resultado ni calcular probabilidades.
- 🔗 **Se estudia junto con:** matriz de covarianza, simétrica, semidefinida positiva, descomposición espectral.

📘 **Dónde se aprende** (1 clase): [B12-C18 · Matrices de covarianza](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md).

### Matriz de covarianza

- Una matriz de covarianza es simétrica y semidefinida positiva (S1: matrices simétricas, §1.2(vi), ecs. 1.2.54–1.2.56).
- La matriz de covarianza `P` de un vector aleatorio tiene como elementos diagonales las varianzas y como elementos fuera de la diagonal las covarianzas (S1, C.3.5).
- La matriz de covarianza da las incertidumbres.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C18](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md):**
- La matriz de covarianza es la «forma» de la nube de errores posibles: sus ejes principales dicen hacia dónde es más larga (incertidumbre máxima) y hacia dónde más estrecha.
- Construir una matriz de covarianza a partir de desviaciones y correlaciones, y viceversa.
- 🎯 **Por qué importa:** El resultado de una determinación de órbita o de un ajuste no es un número sino un vector con una matriz de covarianza; sin ella no se puede propagar, comparar con otro resultado ni calcular probabilidades.
- 🔗 **Se estudia junto con:** simétrica, semidefinida positiva, matriz de correlación, descomposición espectral.

📘 **Dónde se aprende** (5 clases): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md); [B12-C18 · Matrices de covarianza](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md); [B14-C20 · Proyecto reproducible de análisis astronómico](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md); [B15-C16 · Ajuste de curvas](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md); [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Matriz de cumplimiento

- La matriz de cumplimiento cruza requisitos y jurisdicciones.

💡 **Cómo se explica en la clase [B121-C05](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md):**
- La evidencia es tu *matriz de cumplimiento de una misión sintética* del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *matriz de cumplimiento de una misión sintética*: requisitos, diseño, incumplimientos, envolvente, trámites en serie y paralelo, ajustes mínimos y lista de qué es consultado e hipotético, con el aviso de que no es asesoría legal.
- 🎯 **Por qué importa:** Ninguna clase trata el análisis de cumplimiento. La decisión central: ¿cuál es el requisito más estricto de cada tipo, qué incumple el diseño y cuánto tardan los trámites?
- 🔗 **Se estudia junto con:** envolvente, jurisdicción, camino crítico, recomendación.

📘 **Dónde se aprende** (1 clase): [B121-C05 · Cumplimiento regulatorio en varias jurisdicciones](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md).

### Matriz de decisión

- La matriz de decisión (suma ponderada).
- La matriz de decisión puntúa `Σ wᵢ xᵢ/max(xᵢ)`.
- Una matriz de decisión tabula sitios y criterios.

💡 **Cómo se explica en la clase [B47-C20](../programa/clases/B47/B47-C20-caso-comparativo-de-observatorios-espaciales/CLASE.md):**
- *Descripción textual:* las métricas físicas describen lo que cada observatorio puede ver y la matriz de decisión resume una elección cuya robustez se mide cambiando los pesos.
- Construir una matriz de decisión ponderada.
- 🎯 **Por qué importa:** Un ranking depende de los pesos elegidos. La decisión central: ¿qué conclusión sobrevive cuando los pesos cambian?
- 🔗 **Se estudia junto con:** banda espectral, década, límite de difracción, peso.

📘 **Dónde se aprende** (3 clases): [B47-C20 · Caso comparativo de observatorios espaciales](../programa/clases/B47/B47-C20-caso-comparativo-de-observatorios-espaciales/CLASE.md); [B84-C05 · Selección de materiales](../programa/clases/B84/B84-C05-seleccion-de-materiales/CLASE.md); [B109-C01 · Selección de emplazamiento para un asentamiento extraterrestre](../programa/clases/B109/B109-C01-seleccion-de-emplazamiento-para-un-asentamiento-extraterrestre/CLASE.md).

### Matriz de decisión ponderada

- Una matriz de decisión ponderada puntúa alternativas con pesos de criterio.

💡 **Contexto en la clase [B83-C01](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md):**
- 🎯 **Por qué importa:** Un equipo sabe que quiere «mirar la costa» pero no cuánto debe resolver ni qué objetivo merece el presupuesto. La decisión central: ¿qué requisito de medición se deduce de la pregunta científica y qué objetivo conviene perseguir primero?
- 🔗 **Se estudia junto con:** necesidad de misión, caso científico, requisito de medición, GSD.

📘 **Dónde se aprende** (1 clase): [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md).

### Matriz de diferenciación

- La matriz de diferenciación `D` de `(N + 1) × (N + 1)` satisface `(D f)_i ≈ f′(x_i)`: `D_ij = (c_i/c_j) (−1)^{i+j}/(x_i − x_j)` para `i ≠ j`, `D_ii = −Σ_{j≠i} D_ij`, con `c₀ = c_N = 2` y `c_j = 1` en los demás.

💡 **Cómo se explica en la clase [B11-C24](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md):**
- Paso 4 · Costo del sistema. Chebyshev: matriz densa de `15 × 15`, `O(N³) = 3 400` operaciones; diferencias: tridiagonal de `3 × 10⁵`, `O(N)`.
- Construir los nodos y la matriz de diferenciación de Chebyshev.
- 🎯 **Por qué importa:** Cuando la solución es suave, un método espectral reduce un problema que necesita miles de puntos con diferencias a una docena con Chebyshev. Pero tiene un costo: el paso máximo estable de un esquema explícito baja como `1/N⁴`, y funciona mal si la solución no es suave.
- 🔗 **Se estudia junto con:** nodos de Chebyshev–Gauss–Lobatto, colocación, condicionamiento, convergencia exponencial.

📘 **Dónde se aprende** (1 clase): [B11-C24 · Métodos espectrales avanzados (Chebyshev y Fourier)](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md).

### Matriz de diseño

- La matriz de diseño `A` tiene como columnas las funciones del modelo evaluadas en los instantes (`1, t, t²`).
- La matriz de diseño relaciona los parámetros con los datos: `ν = A·p`.
- La matriz de diseño `H` tiene por filas las líneas de visión.

💡 **Cómo se explica en la clase [B29-C04](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md):**
- *Descripción textual:* la firma depende de las masas y de a/d; el modelo lineal define una matriz de diseño cuya covarianza se compara con la dispersión del Monte Carlo; el cociente entre la amplitud y su error da la significancia.
- 🎯 **Por qué importa:** La astrometría mide la inclinación y la masa verdadera, pero la señal es diminuta. La decisión central: ¿cuál es la firma de un planeta a una distancia dada y con qué incertidumbre se recupera su órbita junto al paralaje y el movimiento propio?
- 🔗 **Se estudia junto con:** firma astrométrica, paralaje, movimiento propio, covarianza.

📘 **Dónde se aprende** (5 clases): [B10-C07 · Proyecciones y mínimos cuadrados](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md); [B29-C04 · Astrometría de exoplanetas](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md); [B42-C13 · Medición de frente de onda](../programa/clases/B42/B42-C13-medicion-de-frente-de-onda/CLASE.md); [B62-C05 · Constantes espectroscópicas y ajuste de espectros](../programa/clases/B62/B62-C05-constantes-espectroscopicas-y-ajuste-de-espectros/CLASE.md); [B74-C05 · Sesgos de estaciones terrestres](../programa/clases/B74/B74-C05-sesgos-de-estaciones-terrestres/CLASE.md).

### Matriz de dispersión

- La matriz de dispersión `S` da la respuesta del blanco para cada par de polarizaciones.

💡 **Cómo se explica en la clase [B69-C04](../programa/clases/B69/B69-C04-polarimetria-sar/CLASE.md):**
- *Descripción textual:* la matriz de dispersión se transforma en el vector de Pauli, cuyas potencias identifican mecanismos, y su promedio da la matriz de coherencia y la entropía.
- Escribir la matriz de dispersión `S` y la reciprocidad `Shv = Svh`.
- 🎯 **Por qué importa:** Con un solo canal no se distingue un suelo desnudo de un edificio. La decisión central: ¿qué mecanismo de dispersión domina en un pixel y qué conclusiones se pueden sacar con seguridad de las potencias de los canales?
- 🔗 **Se estudia junto con:** vector de Pauli, span, matriz de coherencia, entropía.

📘 **Dónde se aprende** (1 clase): [B69-C04 · Polarimetría SAR](../programa/clases/B69/B69-C04-polarimetria-sar/CLASE.md).

### Matriz de EPS

- Una matriz de EPS es el material que envuelve las células.

💡 **Cómo se explica en la clase [B64-C06](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md):**
- Flemming y Wingender [S1] describen la matriz del biofilm como un conjunto de polisacáridos, proteínas, ácidos nucleicos y lípidos que da estabilidad mecánica, fija las células a superficies, forma una red tridimensional y retiene enzimas cerca de las células.
- Describir la matriz de sustancias poliméricas extracelulares (EPS) y sus funciones.
- 🎯 **Por qué importa:** Una película de células y matriz crea su propio microambiente. La pregunta motivadora: ¿hasta qué profundidad llega un nutriente en un biofilm y qué sucede con las células que quedan más adentro?
- 🔗 **Se estudia junto con:** difusividad efectiva, constante de consumo, módulo de Thiele, factor de efectividad.

📘 **Dónde se aprende** (1 clase): [B64-C06 · Biofilms en ambientes extremos](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md).

### Matriz de evidencia

- La matriz de evidencia lista cada cifra con su rótulo y su fuente.

💡 **Cómo se explica en la clase [B126-C06](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md):**
- Armar una matriz de evidencia donde cada cifra tiene valor, rótulo (consultada, sintética o calculada) y fuente.
- La evidencia es la anexo financiero con matriz de evidencia del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** [B124-C19](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) redacta propuestas de misión, no financieras. La decisión central: ¿qué cifra se muestra, con qué rótulo y con qué rango, de modo que un tercero pueda comprobarla?
- 🔗 **Se estudia junto con:** rótulo, trazable, rango de incertidumbre, solicitación general.

📘 **Dónde se aprende** (1 clase): [B126-C06 · Presentación financiera ante inversionistas con evidencia](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md).

### Matriz de Fisher

- La matriz de Fisher `F_ij = Σ (∂μ/∂p_i)(∂μ/∂p_j)/σ²` mide la información de los datos.

💡 **Cómo se explica en la clase [B26-C22](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md):**
- *Descripción textual:* los datos dan la matriz de Fisher, cuya inversa es la covarianza y muestra una fuerte correlación negativa; sumar un a priori sobre `Ω_m` corta el valle y reduce las incertidumbres.
- Calcular la matriz de Fisher con derivadas numéricas y marginalizando una constante.
- 🎯 **Por qué importa:** Una incertidumbre marginal puede ser mucho mayor que la que se obtendría si el otro parámetro estuviera fijo, porque ambos se compensan. Sin analizar la degeneración se interpretan mal las barras de error y se desaprovechan las combinaciones de datos.
- 🔗 **Se estudia junto con:** degeneración, covarianza, incertidumbre marginal, coeficiente de correlación.

📘 **Dónde se aprende** (1 clase): [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md).

### Matriz de geometría

- La matriz de geometría `G` tiene por fila el vector unitario receptor–satélite (con signo opuesto) y un 1 para el reloj.
- La matriz de geometría `G` tiene filas `[−uᵢ, 1]` con `uᵢ` el vector unitario al satélite.

💡 **Cómo se explica en la clase [B57-C10](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md):**
- Calcular HDOP, VDOP, PDOP y TDOP desde la matriz de geometría.
- 🎯 **Por qué importa:** La geodesia con GNSS mide posiciones de estaciones con precisión de milímetros a centímetros y sirve para ver cómo se mueve la corteza. Pero la precisión depende de la geometría de los satélites.
- 🔗 **Se estudia junto con:** pseudodistancia, DOP, HDOP, VDOP.

📘 **Dónde se aprende** (2 clases): [B57-C10 · Geodesia mediante GNSS](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md); [B89-C16 · GNSS como navegación de satélites](../programa/clases/B89/B89-C16-gnss-como-navegacion-de-satelites/CLASE.md).

### Matriz de Gram

- La matriz de Gram `G` reúne los productos de los vectores de frente de onda.

💡 **Cómo se explica en la clase [B50-C13](../programa/clases/B50/B50-C13-analisis-monte-carlo-de-tolerancias-opticas/CLASE.md):**
- Construir la matriz de Gram de los vectores de frente de onda.
- 🎯 **Por qué importa:** Una tolerancia individual no dice cuántos instrumentos cumplirán. La decisión central: ¿qué fracción de los telescopios construidos con estas tolerancias cumple el requisito?
- 🔗 **Se estudia junto con:** método de Monte Carlo, rendimiento, percentil.

📘 **Dónde se aprende** (1 clase): [B50-C13 · Análisis Monte Carlo de tolerancias ópticas](../programa/clases/B50/B50-C13-analisis-monte-carlo-de-tolerancias-opticas/CLASE.md).

### Matriz de información

- La matriz de información es `HᵀWH`.
- La matriz de información `A = Σ (I − uuᵀ)/(ρσ)²` suma la información transversal de cada imagen.
- La matriz de información `HᵀWH` suma las contribuciones de los observables.

💡 **Cómo se explica en la clase [B74-C13](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md):**
- *Descripción textual:* las imágenes de las balizas dan líneas de visión; su información transversal suma la matriz `A`, de la que salen la posición y su covarianza; la geometría decide la forma de `A`.
- 🎯 **Por qué importa:** Una dirección conocida con un microrradián son cientos de kilómetros a la distancia de un planeta. La decisión central: ¿cuánta incertidumbre de posición produce una cierta incertidumbre angular y cómo depende de la geometría de las balizas?
- 🔗 **Se estudia junto con:** línea de visión, navegación óptica, geometría, baliza.

📘 **Dónde se aprende** (3 clases): [B74-C07 · Ajuste por mínimos cuadrados](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md); [B74-C13 · Navegación óptica](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md); [B74-C28 · Medidas de rango y Doppler para determinar la órbita](../programa/clases/B74/B74-C28-medidas-de-rango-y-doppler-para-determinar-la-orbita/CLASE.md).

### Matriz de información de Fisher

- La matriz de información de Fisher es `F = Jᵀ J / σ²` (ruido gaussiano independiente); la cota de Cramér–Rao dice que la covarianza de cualquier estimador insesgado es al menos `F⁻¹`.

💡 **Cómo se explica en la clase [B22-C03](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md):**
- Construir la matriz de información de Fisher y leer incertidumbres mínimas (cota de Cramér–Rao).
- 🎯 **Por qué importa:** Un ajuste siempre devuelve números. Que el programa converja no demuestra que esos números signifiquen algo: si dos parámetros se compensan, el ajuste elige uno cualquiera de infinitas combinaciones igual de buenas.
- 🔗 **Se estudia junto con:** modelo, parámetros, datos, jacobiano.

📘 **Dónde se aprende** (1 clase): [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md).

### Matriz de interacción

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C23](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md):**
- matriz de interaccion 200 x 36 ; suma de autovalores = 61.862181 ; traza de M^T M = 61.862181 ; ortogonalidad de Jacobi = 2.0e-15
- python programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/calibracion.py
- 🎯 **Por qué importa:** Una matriz mal calibrada degrada el lazo y las aberraciones del camino de ciencia no las ve el sensor. La decisión central: ¿con qué amplitud calibrar y cómo corregir lo que el sensor no ve?
- 🔗 **Se estudia junto con:** empuje-tirón, matriz de control, valores singulares, NCPA.

📘 **Dónde se aprende** (1 clase): [B42-C23 · Calibración de la matriz de interacción y aberraciones no comunes](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md).

### Matriz de Jones

- La matriz de Jones: generalización 2×2 de `g_i` que incluye polarización.

💡 **Cómo se explica en la clase [B51-C03](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué añade una matriz de Jones 2×2?
- 🎯 **Por qué importa:** Sin ganancias el conjunto de datos no sirve para formar imágenes. La decisión central: ¿cómo se estiman las ganancias a partir de un modelo de cielo conocido y qué precisión se alcanza?
- 🔗 **Se estudia junto con:** ecuación de medida, ganancia compleja, antena de referencia, mínimos cuadrados alternados.

📘 **Dónde se aprende** (1 clase): [B51-C03 · Ganancias complejas por antena y soluciones de calibración](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md).

### Matriz de Lorentz

- Una matriz de Lorentz `Λ` tiene determinante 1 y deja invariante `s²`.

💡 **Cómo se explica en la clase [B26-C02](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md):**
- *Descripción textual:* la matriz de Lorentz transforma las coordenadas del evento; el intervalo calculado antes y después es el mismo.
- 🎯 **Por qué importa:** Para comparar la hora de un reloj en órbita con la de uno en tierra, o la dirección de una señal vista desde dos naves, hace falta una fórmula que traduzca coordenadas entre marcos. Esa fórmula debe respetar los postulados de C01.
- 🔗 **Se estudia junto con:** boost de Lorentz, intervalo, transformación inversa, composición.

📘 **Dónde se aprende** (1 clase): [B26-C02 · Transformaciones de Lorentz](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md).

### Matriz de masa

- La matriz de masa es la métrica con la que se mide la energía cinética (aquí, la identidad).
- La matriz de masa `M(q)` es simétrica y definida positiva y recoge la inercia.

💡 **Cómo se explica en la clase [B19-C03](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md):**
- Solución: reescalar el parámetro pequeño (cambio de unidades, p. ej. de K a mK) o usar una matriz de masa que adapte la métrica, de modo que ambas escalas valgan ≈ 1.
- 🎯 **Por qué importa:** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.
- 🔗 **Se estudia junto con:** posición, momento, energía potencial, cinética.

📘 **Dónde se aprende** (2 clases): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md); [B102-C01 · Dinámica multicuerpo de rovers y manipuladores](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md).

### Matriz de medida

- La matriz de medida `H` dice qué parte del estado se mide.

💡 **Contexto en la clase [B15-C17](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md):**
- **Idea central (modelo mental):** El modelo es un testigo que dice «el objeto debería estar aquí» con una fiabilidad `P⁻`; el sensor es otro testigo que dice «lo medí aquí» con fiabilidad `R`. La ganancia pesa cada testigo según su fiabilidad: si el modelo es más fiable, `K` es pequeña; si el sensor lo es, `K` es grande. Analogía: dos testigos ponderados.
- 🎯 **Por qué importa:** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.
- 🔗 **Se estudia junto con:** estado, matriz de transición, covarianza del ruido de proceso, covarianza del ruido de medida.

📘 **Dónde se aprende** (1 clase): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md).

### Matriz de mezcla

- La matriz de mezcla `U` (PMNS) los relaciona.

💡 **Cómo se explica en la clase [B28-C03](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md):**
- Construir la matriz de mezcla `U` de tres sabores.
- 🎯 **Por qué importa:** Un detector que ve neutrinos muónicos de una fuente lejana no ve lo que salió de ella. Para interpretar la razón de sabores hay que conocer la mezcla.
- 🔗 **Se estudia junto con:** sabor, autoestado de masa, fase de oscilación, probabilidad promediada.

📘 **Dónde se aprende** (1 clase): [B28-C03 · Neutrinos astrofísicos](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md).

### Matriz de Mueller

- La matriz de Mueller 4×4 actúa sobre Stokes; el cálculo de Jones actúa sobre el campo.

💡 **Contexto en la clase [B45-C15](../programa/clases/B45/B45-C15-polarizacion-lineal-y-circular/CLASE.md):**
- **Idea central (modelo mental):** Como unas gafas polarizadas: dejan pasar solo la vibración alineada, y girarlas cambia cuánta luz pasa según el coseno al cuadrado.
- 🎯 **Por qué importa:** La polarización informa de campos magnéticos, dispersión y geometría. La decisión central: ¿cómo se calcula el estado de polarización tras cada elemento?
- 🔗 **Se estudia junto con:** parámetros de Stokes, grado de polarización, ángulo, cálculo de Jones.

📘 **Dónde se aprende** (1 clase): [B45-C15 · Polarización lineal y circular](../programa/clases/B45/B45-C15-polarizacion-lineal-y-circular/CLASE.md).

### Matriz de Pauli

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B31-C03](../programa/clases/B31/B31-C03-estados-y-observables-cuanticos/CLASE.md):**
- **Idea central (modelo mental):** Como una moneda en el aire que, al caer, da cara o cruz con cierta probabilidad que depende de cómo giraba; la medida fija el resultado, y la evolución es un giro continuo.
- 🎯 **Por qué importa:** Un cúbit, un espín o un átomo de dos niveles obedecen estas reglas, y la medida cambia el estado. La decisión central: ¿cómo se calculan probabilidades y evolución en un sistema de dos niveles?
- 🔗 **Se estudia junto con:** regla de Born, oscilación de Rabi, detuning, desigualdad de Robertson.

📘 **Dónde se aprende** (1 clase): [B31-C03 · Estados y observables cuánticos](../programa/clases/B31/B31-C03-estados-y-observables-cuanticos/CLASE.md).

### Matriz de permutación

- LU: `P A = L U` con `L` triangular inferior de unos en la diagonal, `U` triangular superior y `P` una matriz de permutación (reordena filas) —es la eliminación gaussiana guardada—.

💡 **Contexto en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- **Idea central (modelo mental):** Factorizar es pagar un costo inicial para que cada resolución posterior sea barata.
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.
- 🔗 **Se estudia junto con:** factorización, LU, QR, Cholesky.

📘 **Dónde se aprende** (1 clase): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md).

### Matriz de proyección

- La matriz de proyección `P = A(AᵀA)⁻¹Aᵀ` es simétrica e idempotente (`P² = P`).

💡 **Cómo se explica en la clase [B10-C07](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md):**
- Ejercicio 4. Escribe la matriz de proyección sobre `u = (1, 1)/√2` y comprueba `P² = P` y la traza.
- 🎯 **Por qué importa:** Una estación mide la distancia a un satélite cada segundo durante diez segundos. Hay once medidas y solo tres parámetros que describir (posición, velocidad y aceleración radiales).
- 🔗 **Se estudia junto con:** proyección ortogonal, matriz de diseño, mínimos cuadrados, ecuaciones normales.

📘 **Dónde se aprende** (1 clase): [B10-C07 · Proyecciones y mínimos cuadrados](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md).

### Matriz de rasgos

- Una matriz de rasgos tabula regímenes por rasgos.

💡 **Cómo se explica en la clase [B119-C19](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md):**
- Construir una matriz de rasgos binarios de regímenes sintéticos.
- Ejercicio 12 · integrador. Integrador. Elabora tu *matriz comparada de cinco regímenes sintéticos*: rasgos, Jaccard, par más parecido y distinto, rasgos únicos y aviso de que es educativa.
- 🎯 **Por qué importa:** Los tratados fijan principios y dejan la aplicación a los Estados (art. VI; art.
- 🔗 **Se estudia junto con:** rasgo, similitud de Jaccard, distancia de Jaccard, rasgo único.

📘 **Dónde se aprende** (1 clase): [B119-C19 · Legislación comparada y casos nacionales](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md).

### Matriz de rayos

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C05](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md):**
- **Idea central (modelo mental):** Como unas gafas gruesas frente a unas finas: el aumento depende de cuánto vidrio atraviesa la luz entre las dos caras; el espesor desplaza los planos desde donde se mide la focal.
- 🎯 **Por qué importa:** El objetivo de un refractor es una lente. La decisión central: ¿cuánto se equivoca la fórmula de lente delgada cuando la lente es gruesa?
- 🔗 **Se estudia junto con:** lente delgada, ecuación del fabricante, planos principales, distancia focal posterior.

📘 **Dónde se aprende** (1 clase): [B41-C05 · Lentes delgadas y gruesas](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md).

### Matriz de resolución

- La matriz de resolución `R = A(AᵀA + λI)⁻¹Aᵀ` dice cuánta información hay por dato.

💡 **Cómo se explica en la clase [B37-C10](../programa/clases/B37/B37-C10-inversion-asterosismica-de-perfiles-internos/CLASE.md):**
- Calcular la traza de la matriz de resolución.
- 🎯 **Por qué importa:** Los datos son pocos y ruidosos y las incógnitas muchas. La decisión central: ¿cuánta regularización aplicar para no ajustar el ruido ni borrar la señal?
- 🔗 **Se estudia junto con:** problema inverso, problema mal planteado, regularización de Tikhonov, principio de discrepancia.

📘 **Dónde se aprende** (1 clase): [B37-C10 · Inversión asterosísmica de perfiles internos](../programa/clases/B37/B37-C10-inversion-asterosismica-de-perfiles-internos/CLASE.md).

### Matriz de rigidez

- La matriz de rigidez `K_ij = ∫ φ_i′ φ_j′ dx` y el vector de carga `b_i = ∫ f φ_i dx` forman `K u = b`.

💡 **Cómo se explica en la clase [B11-C15](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md):**
- Ensamblar la matriz de rigidez y el vector de carga y resolver.
- Ejercicio 7. Escribe la matriz de rigidez de `N = 4` en `[0, 1]`.
- 🎯 **Por qué importa:** Las estructuras y los escudos de una nave no son barras rectas con mallas regulares. El análisis térmico y estructural de ingeniería espacial se hace casi siempre con elementos finitos sobre geometrías reales.
- 🔗 **Se estudia junto con:** forma débil, función de prueba, malla, elementos.

📘 **Dónde se aprende** (1 clase): [B11-C15 · Elementos finitos introductorios](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md).

### Matriz de rigidez reducida

- La matriz de rigidez reducida `Q` relaciona tensión y deformación en el plano.

💡 **Cómo se explica en la clase [B84-C03](../programa/clases/B84/B84-C03-materiales-compuestos/CLASE.md):**
- Calcular la matriz de rigidez reducida `Q` de una lámina ortótropa.
- 🎯 **Por qué importa:** Un panel de fibra con las capas mal orientadas puede ser 14 veces más blando en una dirección que en otra sin que el material cambie. La decisión central: ¿cómo cambia la rigidez efectiva de un laminado según el ángulo de sus capas?
- 🔗 **Se estudia junto con:** lámina, matriz A, cuasi-isótropo.

📘 **Dónde se aprende** (1 clase): [B84-C03 · Materiales compuestos](../programa/clases/B84/B84-C03-materiales-compuestos/CLASE.md).

### Matriz de rotación

- Una matriz de rotación `R` es una tabla 3×3 que, al multiplicarse por un vector, lo gira sin cambiar su módulo.

💡 **Cómo se explica en la clase [B04-C15](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md):**
- *Descripción textual:* de las componentes ecuatoriales se pasa a las eclípticas con la rotación pasiva `R_x(ε)`; la traspuesta devuelve las ecuatoriales; de las eclípticas salen longitud y latitud con `atan2` y `arcsen`; y la matriz se comprueba con ortogonalidad y determinante 1.
- Matriz 3×3: general, sirve para encadenar rotaciones.
- 🎯 **Por qué importa:** El ecuador de la Tierra y el plano de su órbita (la eclíptica) forman un ángulo de unos 23,4°. Los catálogos de estrellas se dan en coordenadas ecuatoriales; el movimiento del Sol, la Luna y los planetas es más simple en coordenadas eclípticas.
- 🔗 **Se estudia junto con:** ortogonal, determinante, inversa, traspuesta.

📘 **Dónde se aprende** (1 clase): [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md).

### Matriz de rotación elemental

- Una matriz de rotación elemental `R₁`, `R₂`, `R₃` gira alrededor de `x`, `y` o `z`.

💡 **Contexto en la clase [B13-C22](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md):**
- **Idea central (modelo mental):** Piensa en tres engranajes encadenados: el primero (`W`) mueve el eje dentro de la Tierra, el segundo (`R`) gira la Tierra alrededor de ese eje, el tercero (`Q`) mueve el eje respecto de las estrellas. El orden importa; cada engranaje tiene su propia incertidumbre y su propio periodo.
- 🎯 **Por qué importa:** Una estación terrestre apunta a una nave en el sistema celeste. Para ello debe saber cuánto ha girado la Tierra, hacia dónde apunta su eje en el cielo y dónde está ese eje dentro de la corteza.
- 🔗 **Se estudia junto con:** parámetros de orientación terrestre (EOP), CIP, movimiento polar, UT1 − UTC.

📘 **Dónde se aprende** (1 clase): [B13-C22 · Parámetros de orientación terrestre: precesión, nutación, UT1 y movimiento polar](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md).

### Matriz de sensibilidades

- La matriz de sensibilidades `G` contiene las derivadas de la posición en el cielo respecto de los elementos.

💡 **Cómo se explica en la clase [B58-C08](../programa/clases/B58/B58-C08-propagacion-de-incertidumbre-orbital/CLASE.md):**
- Propagar una covarianza con la matriz de sensibilidades `G`.
- 🎯 **Por qué importa:** La incertidumbre tiende a crecer con el tiempo y se estira a lo largo de la órbita, aunque la geometría con la Tierra la modula. La decisión central: ¿cuánto se estira la región de búsqueda en cada fecha y hasta cuándo sirve la covarianza lineal?
- 🔗 **Se estudia junto con:** elipse de incertidumbre, propagación lineal, Monte Carlo, incertidumbre a lo largo de la traza.

📘 **Dónde se aprende** (1 clase): [B58-C08 · Propagación de incertidumbre orbital](../programa/clases/B58/B58-C08-propagacion-de-incertidumbre-orbital/CLASE.md).

### Matriz de T en una base

- La matriz de `T` en una base tiene como `k`‑ésima columna las coordenadas de `T(b_k)`.

💡 **Cómo se explica en la clase [B10-C03](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md):**
- Una matriz dice qué hace el operador con cada vector de la base; todo lo demás sale por linealidad.
- Construir la matriz de un operador a partir de su efecto sobre una base.
- 🎯 **Por qué importa:** Una estación terrestre está fija respecto de la Tierra, pero la Tierra gira respecto del espacio inercial. Para saber dónde está la estación en el sistema inercial a cada instante hay que aplicar una transformación que depende del tiempo.
- 🔗 **Se estudia junto con:** operador lineal, matriz, producto matricial, matriz identidad.

📘 **Dónde se aprende** (1 clase): [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md).

### Matriz de tasas

- La matriz de tasas `M` cumple `dy/dt = M y`; cada reacción `i→j` con constante `k` resta `k` en `M_ii` y suma `k` en `M_ji`.

💡 **Cómo se explica en la clase [B55-C20](../programa/clases/B55/B55-C20-modelo-simplificado-de-red-astroquimica/CLASE.md):**
- *Descripción textual:* el CO es el centro de una cadena que se conecta con C⁺, HCO⁺ y el hielo; la matriz de tasas se integra en el tiempo y se resuelve algebraicamente en el estacionario, y ambos resultados se comparan.
- Construir la matriz de tasas de una red lineal.
- 🎯 **Por qué importa:** Una red de reacciones es la herramienta con que se comparan modelos y observaciones, pero un error de signo o de conservación pasa inadvertido. La decisión central: ¿cómo sé que mi red está bien construida?
- 🔗 **Se estudia junto con:** conservación, Euler implícito, balance detallado.

📘 **Dónde se aprende** (1 clase): [B55-C20 · Modelo simplificado de red astroquímica](../programa/clases/B55/B55-C20-modelo-simplificado-de-red-astroquimica/CLASE.md).

### Matriz de transferencia

- La matriz de transferencia relaciona los campos en la película.

💡 **Cómo se explica en la clase [B43-C07](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md):**
- El script [aluminizado.py](aluminizado.py) calcula `R`, la transmisión por matriz de transferencia y la uniformidad con Monte Carlo (comprueba `1e-4` y `4 %`).
- 🎯 **Por qué importa:** Una película delgada deja pasar luz; una gruesa refleja pero no se adhiere ni es uniforme. La decisión central: ¿qué espesor es opaco, qué reflectancia da y cuánto varía de centro a borde por la geometría del evaporador?
- 🔗 **Se estudia junto con:** índice complejo, reflectancia, profundidad de penetración, espesor opaco.

📘 **Dónde se aprende** (1 clase): [B43-C07 · Aluminizado y recubrimientos](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md).

### Matriz de transformación

- La matriz de transformación `A` pasa componentes de un sistema a otro.

💡 **Cómo se explica en la clase [B04-C19](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md):**
- Antes comprueba: `A_G` es ortogonal (5 × 10⁻¹⁰); la matriz construida coincide con la publicada (2 × 10⁻⁹); el polo está en `b = 90°` (con `atan2`); la ida y vuelta (con la publicada, a 10⁻⁶°; con la construida, a 10⁻¹⁰°); el nodo está en `δ = 0°` y la cadena es igual a la transformación directa (10⁻¹²).
- 🎯 **Por qué importa:** Un catálogo da las posiciones en ecuatoriales; un estudio de la Vía Láctea necesita galácticas; un análisis del plano del sistema solar usa eclípticas. Cambiar de sistema es rutina, y un error de signo o de matriz mueve el objeto decenas de grados.
- 🔗 **Se estudia junto con:** sistema de coordenadas esféricas, polo, círculo fundamental, origen de longitud.

📘 **Dónde se aprende** (1 clase): [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md).

### Matriz de transformación de estado

- La matriz de transformación de estado `6×6` lleva posición y velocidad de un marco a otro.

💡 **Cómo se explica en la clase [B10-C16](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md):**
- El estado `x = (r, v)` se transforma con la matriz de `6×6` (la idea de la función `sxform` de SPICE, S2):
- Armar la matriz de transformación de estado `6×6` y componer cadenas de marcos.
- 🎯 **Por qué importa:** Una estación terrestre tiene coordenadas fijas en la Tierra. Un satélite se propaga en un sistema inercial, donde las leyes de Newton valen.
- 🔗 **Se estudia junto con:** marco de referencia, inercial, GCRS, ITRS.

📘 **Dónde se aprende** (1 clase): [B10-C16 · Transformación de marcos de referencia](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md).

### Matriz de transformación de marco

- La matriz de transformación de marco (convención de SPICE) es la transpuesta de la activa; sus filas son los ejes del marco nuevo expresados en el viejo (S2).

💡 **Contexto en la clase [B10-C13](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md):**
- **Idea central (modelo mental):** Una matriz de rotación dice dónde caen los tres ejes del cuerpo: su primera columna es el eje `x` del cuerpo en el sistema inercial, la segunda el `y`, la tercera el `z`.
- 🎯 **Por qué importa:** La actitud de un satélite (hacia dónde apuntan sus ejes) se guarda como una matriz de rotación: sus columnas son los ejes del cuerpo expresados en el sistema inercial. Con ella, un seguidor estelar, un panel o una antena se orientan sin ambigüedad.
- 🔗 **Se estudia junto con:** rotaciones elementales, grupo SO(3), antisimétrica, fórmula de Rodrigues.

📘 **Dónde se aprende** (1 clase): [B10-C13 · Matrices de rotación tridimensional](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md).

### Matriz de transición

- La matriz de transición es `Φ(t) = e^(At)`.
- La matriz de transición `Φ` es la derivada de la posición de llegada respecto a la velocidad de salida.
- La matriz de transición `P` tiene entradas `Pᵢⱼ = P(siguiente = j | actual = i)` y cada fila suma 1.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C13](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md):**
- Definir una cadena de Markov y su matriz de transición, y calcular sus probabilidades de `n` pasos.
- 🎯 **Por qué importa:** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.
- 🔗 **Se estudia junto con:** cadena de Markov, distribución estacionaria, irreducible, aperiódica.

📘 **Dónde se aprende** (7 clases): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B16-C02 · Representaciones en espacio de estados](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md); [B74-C09 · Filtro de Kalman extendido](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md); [B74-C12 · Propagación de incertidumbre — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md); [B75-C18 · Propagación de dispersión inicial](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md) y 1 más.

### Matriz de transición de estado

- La matriz de transición de estado reúne las sensibilidades respecto al estado inicial.

💡 **Contexto en la clase [B72-C19](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md):**
- 🎯 **Por qué importa:** Las incertidumbres de la órbita inicial y de los parámetros determinan cuánto tiempo vale una predicción. La decisión central: ¿cómo crece con el tiempo el error de posición por cada fuente de incertidumbre y cuál de ellas manda?
- 🔗 **Se estudia junto con:** sensibilidad, error radial, crecimiento secular, linealidad.

📘 **Dónde se aprende** (1 clase): [B72-C19 · Análisis de sensibilidad orbital](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md).

### Matriz de trazabilidad

- Una matriz de trazabilidad lista esos enlaces.

💡 **Cómo se explica en la clase [B83-C05](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md):**
- La evidencia es la matriz de trazabilidad con análisis de impacto del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *matriz de trazabilidad con análisis de impacto*: enlaces, huecos, cobertura, impacto de un cambio por dos vías y lista de qué es sintético.
- 🎯 **Por qué importa:** Cuando cambia un requisito, ¿qué piezas y qué pruebas hay que revisar? Sin trazabilidad, nadie lo sabe y el cambio rompe algo en silencio.
- 🔗 **Se estudia junto con:** trazabilidad, Aguas arriba, aguas abajo, análisis de impacto.

📘 **Dónde se aprende** (1 clase): [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md).

### Matriz de verificación

- Una matriz de verificación lista cada requisito, el método de comprobación, el criterio de aceptación y el resultado.
- La matriz de verificación asigna a cada requisito un método.
- La matriz de verificación vincula cada requisito con su método y evidencia.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C19](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md):**
- *Descripción textual:* cada requisito se comprueba por cuatro vías (fórmula, simulación continua, lazo muestreado y barrido de parámetros) y los resultados se reúnen en la matriz de verificación.
- Ejercicio 12 · integrador. Entrega un informe de verificación: para un lazo de tu elección, escribe cinco requisitos con criterio, verifica el simulador (fórmula y orden de convergencia), ejecuta la matriz con barrido y versión muestreada, informa los incumplimientos, rediseña y repite.
- 🎯 **Por qué importa:** Un lazo que «se ve bien» en una simulación puede estar mal por tres razones: el diseño no cumple un requisito en parte del rango de parámetros, la discretización en el computador de vuelo cambia el comportamiento, o el simulador tiene un error numérico.
- 🔗 **Se estudia junto con:** requisito, verificación, validación, convergencia.

📘 **Dónde se aprende** (8 clases): [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md); [B83-C14 · Revisiones CDR y TRR](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md); [B87-C19 · Verificación de ley de control](../programa/clases/B87/B87-C19-verificacion-de-ley-de-control/CLASE.md); [B88-C20 · Plan de verificación de computador de vuelo](../programa/clases/B88/B88-C20-plan-de-verificacion-de-computador-de-vuelo/CLASE.md); [B90-C18 · Trazabilidad de evidencias](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md) y 2 más.

### Matriz del modelo directo

- `A` es la matriz del modelo directo, de tamaño `m × n`.

💡 **Contexto en la clase [B22-C01](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md):**
- **Idea central (modelo mental):** Piensa en un embudo: muchos objetos distintos desembocan en casi los mismos datos. Ir de arriba abajo (problema directo) es fácil y estable. Subir es ambiguo, porque cada dato de salida corresponde a muchos objetos de entrada que difieren en detalles que el instrumento aplasta.
- 🎯 **Por qué importa:** Un telescopio nunca entrega la imagen verdadera del cielo: la entrega emborronada por su respuesta óptica y con ruido. Calcular lo que verá el telescopio si conoces el objeto es fácil; el camino contrario, recuperar el objeto desde lo que vio, es el que interesa a la ciencia y el que se complica.
- 🔗 **Se estudia junto con:** problema directo, problema inverso, incógnita, datos.

📘 **Dónde se aprende** (1 clase): [B22-C01 · Problemas directos e inversos y mal condicionamiento](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md).

### Matriz estado–comando

- La matriz estado–comando es la tabla de aceptación.

💡 **Cómo se explica en la clase [B88-C09](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md):**
- Construir la matriz de aceptación estado–comando.
- El script [telecomandos_modos.py](telecomandos_modos.py) imprime la matriz estado–comando, ejecuta un guion de nueve telecomandos con CRC y secuencia y comprueba 11 celdas aceptadas, el modo final `SAFE` y el CRC-8 de prueba `0xF4`.
- 🎯 **Por qué importa:** Un telecomando aceptado en el estado equivocado puede dañar la nave; uno rechazado en el estado correcto puede perderla. La decisión central: ¿qué comando es válido en cada modo y qué comprobaciones lo protegen?
- 🔗 **Se estudia junto con:** modo, transición, contador de secuencia, CRC-8.

📘 **Dónde se aprende** (1 clase): [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md).

### Matriz fundamental

- La matriz fundamental `N = (I − Q)^−1` da las visitas esperadas a los estados transitorios.

💡 **Cómo se explica en la clase [B119-C29](../programa/clases/B119/B119-C29-escalada-desescalada-y-medidas-de-fomento-de-la-confianza/CLASE.md):**
- Calcular las probabilidades de absorción con la matriz fundamental y verificarlas con simulación.
- Ejercicio 9 · transferencia. Transferencia. ¿Por qué la simulación confirma la matriz fundamental?
- 🎯 **Por qué importa:** C28 y C27 tratan conductas y negociación; ninguna clase muestra la dinámica de escalada ni el valor de las medidas de confianza, que se apoyan en el principio de informar (art. XI) y consultar (art.
- 🔗 **Se estudia junto con:** nivel de escalada, desescalada, medida de fomento de la confianza, absorción.

📘 **Dónde se aprende** (1 clase): [B119-C29 · Escalada, desescalada y medidas de fomento de la confianza](../programa/clases/B119/B119-C29-escalada-desescalada-y-medidas-de-fomento-de-la-confianza/CLASE.md).

### Matriz geométrica

- La matriz geométrica `K_g` hace que `K φ = λ K_g φ` dé `λ = P_cr/P`.

💡 **Contexto en la clase [B84-C23](../programa/clases/B84/B84-C23-vigas-y-placas-flexion-y-pandeo/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR A["E, I, L, K"] --> B["P_cr Euler"] C["n elementos"] --> D["K, Kg"] D --> E["K phi = lambda Kg phi"] E --> F["P_cr FE"] B --> G["comparar"] F --> G H["E, t, b, nu, a"] --> I["sigma_cr placa"] ``` *Descripción textual:* Euler y los autovalores dan la misma carga crítica; la placa se calcula con su fórmula de `k`.
- 🎯 **Por qué importa:** Una columna de aluminio de 30 × 10 mm y 0,5 m se pandea a 6810 N, cuando su sección podría soportar 82 500 N en compresión simple: el 8 %. La decisión central: ¿a qué carga pandea un elemento esbelto y cómo cambia con los apoyos y con el espesor?
- 🔗 **Se estudia junto con:** carga crítica de Euler, tensión crítica de placa.

📘 **Dónde se aprende** (1 clase): [B84-C23 · Vigas y placas: flexión y pandeo](../programa/clases/B84/B84-C23-vigas-y-placas-flexion-y-pandeo/CLASE.md).

### Matriz identidad

- La matriz identidad `I` no cambia nada.

💡 **Contexto en la clase [B10-C03](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md):**
- **Idea central (modelo mental):** Una matriz dice qué hace el operador con cada vector de la base; todo lo demás sale por linealidad.
- 🎯 **Por qué importa:** Una estación terrestre está fija respecto de la Tierra, pero la Tierra gira respecto del espacio inercial. Para saber dónde está la estación en el sistema inercial a cada instante hay que aplicar una transformación que depende del tiempo.
- 🔗 **Se estudia junto con:** operador lineal, matriz, matriz de T en una base, producto matricial.

📘 **Dónde se aprende** (1 clase): [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md).

### Matriz intrínseca

- La matriz intrínseca `K` reúne `fx`, `fy`, `cx`, `cy`.

💡 **Contexto en la clase [B103-C01](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md):**
- 🎯 **Por qué importa:** Un rover que mide una distancia con un error de focal del 1 % comete un error del 1 % en la distancia. La decisión central: ¿cuántas vistas y qué modelo de distorsión hacen falta para que la focal y el punto principal sean fiables, y cómo se comprueba?
- 🔗 **Se estudia junto con:** modelo estenopeico, distorsión radial, homografía, error de reproyección.

📘 **Dónde se aprende** (1 clase): [B103-C01 · Calibración intrínseca de cámaras](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md).

### Matriz ortogonal

- Una matriz ortogonal conserva longitudes y su determinante es ±1.

💡 **Cómo se explica en la clase [B71-C17](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md):**
- En 500 estados sintéticos, la matriz es ortogonal con `4e-16` de error y `h` es paralelo a `W` con `3e-16`.
- Construir la matriz 3‑1‑3 y comprobar que es ortogonal con determinante +1.
- 🎯 **Por qué importa:** Casi todo error de signo o de orden en una rotación aparece como un plano equivocado. La decisión central: ¿cómo pasas del plano orbital al marco inercial y cómo compruebas que la transformación es correcta?
- 🔗 **Se estudia junto con:** sistema perifocal, rotación 3‑1‑3, velocidad radial, transversal.

📘 **Dónde se aprende** (1 clase): [B71-C17 · Movimientos en planos orbitales](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md).

### Matriz poder/interés

- La matriz poder/interés las clasifica: *gestionar de cerca* (poder e interés altos), *mantener satisfecha* (poder alto), *mantener informada* (interés alto) y *monitorear*.

💡 **Cómo se explica en la clase [B83-C02](../programa/clases/B83/B83-C02-partes-interesadas-y-usuarios/CLASE.md):**
- Porque la matriz poder/interés separa quien puede bloquear (poder) de quien más se verá afectado (interés).
- 🎯 **Por qué importa:** Cuando las necesidades de dos partes chocan (alta resolución frente a bajo costo), alguien debe decidir con criterio. La decisión central: ¿qué necesidades pasan a requisitos primero y cuánto confías en ese orden?
- 🔗 **Se estudia junto con:** parte interesada, poder, interés, peso.

📘 **Dónde se aprende** (1 clase): [B83-C02 · Partes interesadas y usuarios](../programa/clases/B83/B83-C02-partes-interesadas-y-usuarios/CLASE.md).

### Matriz severidad–probabilidad

- La matriz severidad–probabilidad clasifica el riesgo.

💡 **Cómo se explica en la clase [B88-C16](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md):**
- Clasificar el riesgo con una matriz severidad–probabilidad.
- 🎯 **Por qué importa:** Una nave tolera fallos si ninguno solo provoca la pérdida y las combinaciones peligrosas son improbables. La decisión central: ¿qué combinaciones mínimas de fallos causan la pérdida y cuál elemento merece más protección?
- 🔗 **Se estudia junto con:** evento tope, eventos básicos, conjunto mínimo de corte, importancia de Birnbaum.

📘 **Dónde se aprende** (1 clase): [B88-C16 · Ingeniería de seguridad funcional](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md).

### Matriz triangular

- La matriz triangular aparece porque una estrella viva con edad `a` pertenece a un intervalo de masa de vida mayor que `a`.

💡 **Cómo se explica en la clase [B38-C04](../programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/CLASE.md):**
- T["t_MS = 10 Gyr · M^-2,5"] --> A["matriz triangular A"]
- Construir la matriz triangular de conteos.
- 🎯 **Por qué importa:** Los conteos de estrellas son una suma sobre edades y la inversión amplifica el ruido. La decisión central: ¿con qué resolución en edad se puede recuperar la historia con un número dado de estrellas?
- 🔗 **Se estudia junto con:** historia de formación estelar, vida en la secuencia principal, población resuelta, inversión.

📘 **Dónde se aprende** (1 clase): [B38-C04 · Historia de formación estelar a partir de poblaciones resueltas](../programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/CLASE.md).

### Máxima verosimilitud

- La máxima verosimilitud estima `α`.
- La máxima verosimilitud da `α̂ = 1 + n/Σ ln(m_i/m_min)` con error `(α̂ − 1)/√n`.
- La máxima verosimilitud para una ley de Pareto da `b = n/Σ ln(D_i/D_min)` con error `b/√n`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B29-C15](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md):**
- Estimar el índice `α` por máxima verosimilitud truncada.
- 🎯 **Por qué importa:** La distribución de energías de las llamaradas determina cuánta energía total reciben los planetas cercanos. Estimar su índice con poco sesgo exige usar el estimador correcto.
- 🔗 **Se estudia junto con:** llamarada, subida rápida y caída exponencial, energía, índice.

📘 **Dónde se aprende** (5 clases): [B29-C15 · Eventos eruptivos estelares](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md); [B33-C03 · Eventos extremos históricos de clima espacial](../programa/clases/B33/B33-C03-eventos-extremos-historicos-de-clima-espacial/CLASE.md); [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md); [B103-C06 · Detección y catalogación de rocas en imágenes de superficie](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md); [B118-C23 · Cobertura, sesgos y límites de las redes de vigilancia](../programa/clases/B118/B118-C23-cobertura-sesgos-y-limites-de-las-redes-de-vigilancia/CLASE.md).

### Máxima verosimilitud gaussiana

- El de máxima verosimilitud gaussiana (QDA) usa media y covarianza de cada clase.

💡 **Contexto en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- **Idea central (modelo mental):** Para separar naranjas, limones y limas por color, miras dónde cae cada fruta en un gráfico de color. Si los tres grupos están lejos, cualquier regla funciona; si se solapan, algunas frutas quedan en tierra de nadie y cualquier regla se equivoca con ellas. Analogía: frutas en un gráfico de color.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, NDVI, clase, muestras de entrenamiento.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Máximo

- El aumento mínimo y el máximo.

💡 **Cómo se explica en la clase [B41-C20](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md):**
- Aumento mínimo (pupila de 7 mm) `35,7`; máximo orientativo `500`.
- aumento minimo (pupila 7 mm) = 35.7 ; maximo orientativo 2 D[mm] = 500
- 🎯 **Por qué importa:** Un diseño es un conjunto de compromisos. La decisión central: ¿qué apertura y qué focal cumplen el objetivo y qué defecto domina?
- 🔗 **Se estudia junto con:** presupuesto de diseño, corrector de coma, Strehl de Maréchal, suma en cuadratura (RSS).

📘 **Dónde se aprende** (1 clase): [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md).

### Máximo de Wien

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B34-C02](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md):**
- A `10⁶ K` el máximo de Wien está en `2,898 nm` y `kT = 86,2 eV`; a `10⁷ K`, en `0,290 nm` y `0,86 keV`.
- Ejercicio 1 · con los pasos indicados. Máximo de Wien a 10⁷ K.
- 🎯 **Por qué importa:** Cada banda del espectro traza una temperatura. La decisión central: ¿en qué banda emite el plasma a una temperatura dada y cuánta potencia radia?
- 🔗 **Se estudia junto con:** medida de emisión, energía térmica, bremsstrahlung, plasma ópticamente delgado.

📘 **Dónde se aprende** (1 clase): [B34-C02 · Emisión EUV y rayos X de la corona](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md).

### Máximo (mínimo) local

- Un máximo (mínimo) local es un valor mayor (menor) que sus vecinos; un extremo global lo es en todo el dominio.
- Un máximo (mínimo) local es un punto cuyo valor supera (es inferior a) el de sus vecinos en todas las direcciones.

💡 **Contexto en la clase [B09-C07](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md):**
- **Idea central (modelo mental):** En la cima de una colina la pendiente es cero; en la subida es positiva y en la bajada negativa. Si la pendiente pasa de positiva a negativa, es un máximo; si pasa de negativa a positiva, un mínimo. La segunda derivada resume lo mismo: mide cómo cambia la pendiente.
- 🎯 **Por qué importa:** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.
- 🔗 **Se estudia junto con:** función objetivo, punto crítico, extremo global, prueba de la segunda derivada.

📘 **Dónde se aprende** (2 clases): [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md); [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md).

### Máximo promedio de diseño

- Máximo promedio de diseño: cota usada para dimensionar.

💡 **Cómo se explica en la clase [B106-C10](../programa/clases/B106/B106-C10-gestion-de-residuos-humanos/CLASE.md):**
- Son máximos promedio de diseño del resumen consultado (requisito citado V2 7102).
- Límite: el máximo de diseño es una cota promedio, no un evento puntual.
- 🎯 **Por qué importa:** Los residuos no desaparecen: hay que contenerlos, almacenarlos o procesarlos. La decisión central: ¿qué masa y volumen de residuos hay que contener en una misión y cuánto margen tiene el máximo de diseño sobre el uso típico?
- 🔗 **Se estudia junto con:** Evento, Contención, Masa seca, Salmuera.

📘 **Dónde se aprende** (1 clase): [B106-C10 · Gestión de residuos humanos](../programa/clases/B106/B106-C10-gestion-de-residuos-humanos/CLASE.md).

### Máximos principales

- Los máximos principales (`u = n/d`) y secundarios.

💡 **Cómo se explica en la clase [B42-C04](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md):**
- Para una red de 5 rendijas el máximo secundario entre principales es `0,0613` (cota de la fórmula: `0,0611`) y hay `3 = N − 2` secundarios; la diferencia máxima con la fórmula es `1,32 × 10⁻⁴`.
- Los máximos principales se afinan: su ancho es `∼λ/(Nd)`.
- 🎯 **Por qué importa:** La pupila de un telescopio es una apertura: su forma fija la imagen de una estrella. La decisión central: ¿cómo cambia el patrón cuando cambia la forma o el número de aberturas?
- 🔗 **Se estudia junto con:** transmitancia, frecuencia espacial, rendija, doble rendija.

📘 **Dónde se aprende** (1 clase): [B42-C04 · Difracción de aperturas](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md).

### Max-q

- La fuerza aerodinámica se descompone en arrastre `D = Cd·q·A` y sustentación `L = CL·q·A`. Max-q es el instante en que `q` es máximo.

💡 **Cómo se explica en la clase [B77-C03](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md):**
- Deducir el instante de max-q en un ascenso de aceleración constante.
- Interpretar por qué max-q ocurre a una altitud igual a la altura de escala en este modelo.
- ⚠️ **Error frecuente:** Pensar que max-q es el instante de mayor velocidad. Se corrige con 8.2.
- 🎯 **Por qué importa:** El momento de mayor carga aerodinámica no es el de mayor velocidad ni el de menor altitud. La decisión central: ¿cuándo ocurre el máximo de la presión dinámica y qué fuerzas produce?
- 🔗 **Se estudia junto con:** presión dinámica, fuerza aerodinámica, arrastre, sustentación.

📖 **Explicado a fondo:** [Presión dinámica y Max-Q](esencial/ampliacion-n-z.md#presión-dinámica-y-max-q) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md).

### Maxwell

- En una distribución de Maxwell con escala `σ` por componente, la fracción con `v > v_esc` es `erfc(x/√2) + √(2/π) x e^(−x²/2)` con `x = v_esc/σ`.

💡 **Cómo se explica en la clase [B53-C15](../programa/clases/B53/B53-C15-geologia-de-encelado/CLASE.md):**
- Con granos de velocidad Maxwell de escala `σ = 100 m/s` (sintética), escapa `0,1282` (Monte Carlo `0,1277`).
- Obtener la fracción que escapa para una distribución de Maxwell.
- 🎯 **Por qué importa:** La fracción que escapa decide cuánto material llega al anillo y cuánto se deposita en la superficie. La decisión central: ¿qué parte de los granos supera la velocidad de escape y a qué altura llegan los demás?
- 🔗 **Se estudia junto con:** velocidad de escape, altura balística.

📘 **Dónde se aprende** (1 clase): [B53-C15 · Geología de Encélado](../programa/clases/B53/B53-C15-geologia-de-encelado/CLASE.md).

### Maxwell–Boltzmann

- La distribución de Bose–Einstein, la de Fermi–Dirac y la de Maxwell–Boltzmann.

💡 **Contexto en la clase [B31-C06](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md):**
- **Idea central (modelo mental):** Los fermiones son personas que no comparten asiento: ocupan los más bajos hasta llenar el nivel de Fermi. Los bosones se agolpan en el mismo asiento, sobre todo con baja energía.
- 🎯 **Por qué importa:** La radiación de las estrellas y la presión de degeneración de los remanentes estelares dependen de estas estadísticas. La decisión central: ¿qué distribución usar y qué constantes se derivan?
- 🔗 **Se estudia junto con:** distribución de Bose–Einstein, Fermi–Dirac, integral de Planck, energía de Fermi.

📘 **Dónde se aprende** (1 clase): [B31-C06 · Estadísticas cuánticas](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md).

### Maxwelliana

- La maxwelliana es la del equilibrio.

💡 **Cómo se explica en la clase [B35-C01](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md):**
- Con `v` en unidades de `v_t` la maxwelliana 3D es `f = (2π)^(−3/2) exp(−v²/2)`.
- La temperatura cinética es la misma en todas las filas, pero una maxwelliana que iguala el valor central de la kappa da una temperatura menor (`0,74 T` si `κ = 5`).
- 🎯 **Por qué importa:** Los instrumentos miden distribuciones, y casi todas las fórmulas de fluido son momentos de ellas. La decisión central: ¿basta una maxwelliana o hay que conservar la cola?
- 🔗 **Se estudia junto con:** función de distribución, distribución kappa, momento, rapidez térmica.

📘 **Dónde se aprende** (1 clase): [B35-C01 · Funciones de distribución de velocidades en plasmas](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md).

### Mayor

- El ciclo menor es el `mcd` de los períodos y el mayor el `mcm`.

💡 **Cómo se explica en la clase [B88-C23](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md):**
- El ejecutivo tiene ciclo menor de 100 ms, mayor de 400 ms y 4 tramas con cargas de 62, 12, 37 y 12 ms.
- Predice antes de ejecutar: ¿qué trama tiene mayor carga?
- 🎯 **Por qué importa:** Las dependencias hacia arriba y los ciclos hacen imposible probar un módulo por separado y convierten un cambio en riesgo global. La decisión central: ¿qué módulo depende de quién, y puede ordenarse el sistema en capas sin ciclos?
- 🔗 **Se estudia junto con:** capa, dependencia hacia arriba, nivel topológico, ciclo menor.

📘 **Dónde se aprende** (1 clase): [B88-C23 · Arquitectura de software de vuelo: capas y ejecutivo](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md).

### Mayoría de k de n

- La mayoría de `k` de `n` con `k = ⌊n/2⌋ + 1`.

💡 **Cómo se explica en la clase [B88-C33](../programa/clases/B88/B88-C33-votacion-y-redundancia-modular-triple-tmr/CLASE.md):**
- Un canal con un bit invertido se corrige; dos canales con bits distintos invertidos también (cada bit tiene mayoría); dos con el mismo bit invertido no se corrigen.
- Con `r = 0,9`: 3 canales `0,972`; 5 canales (mayoría de 3) `0,991440`.
- 🎯 **Por qué importa:** TMR enmascara el fallo de un canal sin interrupción, pero solo si los canales son suficientemente fiables y el votador no es el punto débil. La decisión central: ¿para qué fiabilidad de módulo TMR mejora y cuánto aporta?
- 🔗 **Se estudia junto con:** votador, cruce.

📘 **Dónde se aprende** (1 clase): [B88-C33 · Votación y redundancia modular triple (TMR)](../programa/clases/B88/B88-C33-votacion-y-redundancia-modular-triple-tmr/CLASE.md).

### MBSE

- Un modelo de sistema reúne parámetros, relaciones y restricciones en un solo lugar. MBSE es la práctica de usarlo como fuente central.

💡 **Cómo se explica en la clase [B83-C12](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md):**
- SysML y herramientas MBSE: añaden bloques, interfaces, requisitos y simulación (no usados aquí).
- 🎯 **Por qué importa:** Cuando los presupuestos viven en hojas distintas, un cambio de requisito se propaga a mano y algo se olvida. La decisión central: ¿qué parámetros cambian si cambia este requisito, y siguen cumpliéndose todos los presupuestos?
- 🔗 **Se estudia junto con:** modelo de sistema, parámetro de entrada, derivado, restricción.

📘 **Dónde se aprende** (1 clase): [B83-C12 · Model-Based Systems Engineering](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md).

### MCAO

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C18](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md):**
- El modelo es solo una ilustración; un resumen de Rigaut y Neichel (solo resumen) indica que la MCAO busca campos 10 a 20 veces mayores en área que la óptica adaptativa clásica.
- *Descripción textual:* el anisoplanatismo crece como `(θ/θ₀)^{5/3}`; la MCAO lo reduce hasta que la huella queda fuera de las guías.
- ⚠️ **Error frecuente:** Confundir `θ₀` con el campo MCAO. Son conceptos distintos.
- 🎯 **Por qué importa:** Una sola corrección solo vale dentro del ángulo isoplanático (unos segundos de arco). La decisión central: ¿cómo se amplía el campo y qué parte de la turbulencia queda sin restricción?
- 🔗 **Se estudia junto con:** anisoplanatismo, ángulo isoplanático, altura efectiva, huella.

📘 **Dónde se aprende** (1 clase): [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### MC/DC

- La cobertura de decisión exige `D = V` y `D = F`. MC/DC (condición/decisión modificada) exige para cada condición un par de pruebas que difieran solo en ella y cambien `D`.

💡 **Cómo se explica en la clase [B88-C39](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md):**
- MC/DC mínimo: `4`; el conjunto `{(0,1,0), (0,1,1), (1,0,0), (1,1,0)}` lo cumple.
- `{(1,1,0), (0,0,0)}` y `{(1,1,1), (0,0,0)}` cubren decisión y no MC/DC.
- 🎯 **Por qué importa:** Elegir el nivel de cobertura determina el esfuerzo de prueba. La decisión central: ¿qué cobertura piden los distintos niveles y cuánto cuesta cada una en pruebas?
- 🔗 **Se estudia junto con:** cobertura de decisión, tamaño mínimo, exhaustiva.

📘 **Dónde se aprende** (1 clase): [B88-C39 · Normas de aseguramiento de software (ECSS, DO-178C)](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md).

### M/D/1

- En M/D/1, `W_q = ρS/(2(1 − ρ))`.

💡 **Cómo se explica en la clase [B88-C43](../programa/clases/B88/B88-C43-pruebas-de-carga-y-estres-del-software-de-vuelo/CLASE.md):**
- La espera real es mayor que la de M/D/1.
- El script [carga_estres.py](carga_estres.py) simula una cola M/D/1 con cinco cargas, compara con la teoría y estudia el descarte con cola de 16, y comprueba que el error relativo es menor que 10 % para `ρ < 0,9`.
- 🎯 **Por qué importa:** Un sistema que funciona al 50 % de carga puede volverse inutilizable al 95 %. La decisión central: ¿a qué tasa de llegada se degrada la latencia y qué política de descarte conviene al saturarse?
- 🔗 **Se estudia junto con:** utilización, p99, descarte, saturación.

📘 **Dónde se aprende** (1 clase): [B88-C43 · Pruebas de carga y estrés del software de vuelo](../programa/clases/B88/B88-C43-pruebas-de-carga-y-estres-del-software-de-vuelo/CLASE.md).

### MDC95

- El MDC95 es `1,96 √2 SEM`: el cambio mínimo que supera el ruido con 95 % de confianza.
- El MDC95 es el cambio mínimo detectable al 95 %.

💡 **Cómo se explica en la clase [B105-C26](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md):**
- Promediar `k` sesiones da `SEM = 4/√k`: 4,00 (1); 2,83 (2) y 2,00 (4); el MDC95 baja a 11,09; 7,84 y 5,54.
- Una medida sintética con variación entre individuos `SD = 10` y variación dentro de individuos `SD = 4`: ICC verdadero `100/(100 + 16) = 0,862`, SEM = 4,00 y MDC95 = 11,09.
- 🎯 **Por qué importa:** Un biomarcador con alta variación interna no detecta cambios pequeños aunque sea «preciso». Con pocos participantes, además, el propio ICC es incierto.
- 🔗 **Se estudia junto con:** ICC(1,1), SEM, límites de acuerdo, Bland–Altman.

📘 **Dónde se aprende** (2 clases): [B105-C26 · Medidas fisiológicas y biomarcadores en investigación espacial](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md); [B107-C08 · Evaluación funcional posterior al vuelo](../programa/clases/B107/B107-C08-evaluacion-funcional-posterior-al-vuelo/CLASE.md).

### MDS

- Un MDS (modelo digital de superficie) incluye árboles y edificios; un MDT (de terreno) los quita.

💡 **Cómo se explica en la clase [B57-C28](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md):**
- A["arboles y edificios"] --> S["MDS = MDT + objetos"]
- *Descripción textual:* la rejilla y el tamaño de celda alimentan el operador de Horn, que da pendiente y orientación; un paso mayor las subestima, y los objetos sobre el terreno distinguen el MDS del MDT.
- ⚠️ **Error frecuente:** Usar un MDS como MDT. Se corrige con 8.4.
- 🎯 **Por qué importa:** La pendiente decide dónde se produce un deslizamiento, cómo corre el agua o si una antena ve el horizonte. La decisión central: ¿qué resolución y qué tipo de modelo necesito para la pendiente que me importa?
- 🔗 **Se estudia junto con:** MDT, pendiente, orientación, operador de Horn.

📘 **Dónde se aprende** (1 clase): [B57-C28 · Modelos digitales de elevación](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md).

### MDT

- Un MDS (modelo digital de superficie) incluye árboles y edificios; un MDT (de terreno) los quita.

💡 **Cómo se explica en la clase [B57-C28](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md):**
- A["arboles y edificios"] --> S["MDS = MDT + objetos"]
- *Descripción textual:* la rejilla y el tamaño de celda alimentan el operador de Horn, que da pendiente y orientación; un paso mayor las subestima, y los objetos sobre el terreno distinguen el MDS del MDT.
- ⚠️ **Error frecuente:** Usar un MDS como MDT. Se corrige con 8.4.
- 🎯 **Por qué importa:** La pendiente decide dónde se produce un deslizamiento, cómo corre el agua o si una antena ve el horizonte. La decisión central: ¿qué resolución y qué tipo de modelo necesito para la pendiente que me importa?
- 🔗 **Se estudia junto con:** MDS, pendiente, orientación, operador de Horn.

📘 **Dónde se aprende** (1 clase): [B57-C28 · Modelos digitales de elevación](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md).

### Mecanización

- La mecanización es el conjunto de ecuaciones `q̇ = ½ q ⊗ (0, ω)`, `v̇ = R(q) f + g` y `ṗ = v`.

💡 **Cómo se explica en la clase [B80-C03](../programa/clases/B80/B80-C03-mecanizacion-strapdown-e-integracion-de-actitud-y-velocidad/CLASE.md):**
- En caída libre `f_b = 0` y la mecanización devuelve `a_z = −9,80665 m/s²`: es la gravedad modelada la que acelera al vehículo, no un valor medido.
- La mecanización con la exponencial del cuaternión y actitud de punto medio (`Δt = 0,01 s`) tiene un error de posición de `4,014 × 10⁻⁵ m`; la integración con Euler y actitud de inicio de paso, `0,1071 m`.
- 🎯 **Por qué importa:** Las clases B10-C12..C15 dan las rotaciones y los cuaterniones, pero ninguna construye la cadena completa actitud → velocidad → posición. La decisión central: ¿cómo se integra la actitud para que el error numérico no domine al error del sensor?
- 🔗 **Se estudia junto con:** cuaternión, actitud de punto medio.

📘 **Dónde se aprende** (1 clase): [B80-C03 · Mecanización strapdown e integración de actitud y velocidad](../programa/clases/B80/B80-C03-mecanizacion-strapdown-e-integracion-de-actitud-y-velocidad/CLASE.md).

### Media

- La media es la suma dividida por el número de lecturas; la desviación estándar experimental `s` mide su dispersión; la incertidumbre de la media es `s/√n`.
- El cociente de diferencias de `f` entre `x` y `x + h` es `[f(x + h) − f(x)]/h`: la tasa de cambio media en ese intervalo.
- La media (o esperanza) de la espera es `∫₀^∞ t f(t) dt`.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- Para `n` lecturas `x_i`: `media = Σx_i/n`;
- Caso analítico: `{1, 2, 3, 4, 5}` da `media = 3`, `s = 1,581`, `u = 0,707`.
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.
- 🔗 **Se estudia junto con:** error, incertidumbre, incertidumbre estándar, evaluación tipo A.

📖 **Explicado a fondo:** [Media y desviación estándar](esencial/cuarta-fundamentos.md#media-y-desviación-estándar) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (8 clases): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B09-C03 · Derivada como tasa de cambio](../programa/clases/B09/B09-C03-derivada-como-tasa-de-cambio/CLASE.md); [B09-C10 · Integración por partes](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B71-C13 · Anomalías orbitales](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md); [B71-C14 · Ecuación de Kepler](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md) y 2 más.

### Media de Rosseland

- La media de Rosseland pondera `1/κ_ν` con `dB/dT`.

💡 **Cómo se explica en la clase [B32-C03](../programa/clases/B32/B32-C03-opacidad-continua-ligado-libre-libre-libre-y-h/CLASE.md):**
- La media de Rosseland está dominada por las frecuencias donde la opacidad es menor.
- Una atmósfera es como un filtro que deja pasar mejor unos colores que otros; la media de Rosseland dice cuánto deja pasar «en promedio» cuando el calor fluye por difusión.
- ⚠️ **Error frecuente:** Confundir media aritmética y de Rosseland. Se corrige con 8.3.
- 🎯 **Por qué importa:** La opacidad fija la profundidad desde la que escapa la luz. La decisión central: ¿cómo se promedia una opacidad que depende de la frecuencia?
- 🔗 **Se estudia junto con:** opacidad continua, H⁻, escalado de Kramers.

📘 **Dónde se aprende** (1 clase): [B32-C03 · Opacidad continua: ligado-libre, libre-libre y H-](../programa/clases/B32/B32-C03-opacidad-continua-ligado-libre-libre-libre-y-h/CLASE.md).

### Media móvil

- La media móvil de `M` puntos es el FIR con `h[m] = 1/M`.

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- La respuesta de la media móvil de `M` puntos es `H(f) = sen(π f M)/(M sen(π f)) · e^{−iπ f (M−1)}`, con `f` en ciclos por muestra.
- Si `y = x − MA_W(x)` con una media móvil centrada de `W` muestras, el filtro es paso alto con `H_alto(f) = 1 − H_MA(f)`.
- ⚠️ **Error frecuente:** Tratar las salidas de una media móvil como independientes. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.
- 🔗 **Se estudia junto con:** filtro digital, lineal, invariante, FIR.

📘 **Dónde se aprende** (1 clase): [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### Media ponderada

- La media ponderada `x_w = Σ(xᵢ/uᵢ²)/Σ(1/uᵢ²)` pesa cada medida por `1/uᵢ²`; su incertidumbre es `u_w = 1/√Σ(1/uᵢ²)`.
- La media ponderada es `μ = Σ(μ_i/σ_i²)/Σ(1/σ_i²)` y su incertidumbre, `σ = 1/√Σ(1/σ_i²)`.
- La media ponderada es `Σ w m / Σ w` y su varianza es `1/Σ w`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C09](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md):**
- Explicar la diferencia entre media simple y media ponderada.
- 🎯 **Por qué importa:** Calcular la densidad de ocho planetas con un `for` funciona, pero a escala de millones de datos es lento y verboso. NumPy opera sobre arreglos completos con una sola expresión y es la base de casi toda la ciencia con Python.
- 🔗 **Se estudia junto con:** NumPy, arreglo, vectorizada, difusión.

📘 **Dónde se aprende** (4 clases): [B07-C09 · Cálculos científicos básicos con Python](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md); [B13-C18 · Intercomparación de instrumentos](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md); [B26-C21 · Verosimilitud cosmológica con datos combinados](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md); [B129-C02 · Fotometría participativa](../programa/clases/B129/B129-C02-fotometria-participativa/CLASE.md).

### Media simple

- Una media ponderada pesa cada valor por su importancia; una media simple los trata igual.

💡 **Cómo se explica en la clase [B07-C09](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md):**
- La media simple de las ocho densidades es `3129,8 kg/m³`, pero no es la densidad media del conjunto.
- Explicar la diferencia entre media simple y media ponderada.
- 🎯 **Por qué importa:** Calcular la densidad de ocho planetas con un `for` funciona, pero a escala de millones de datos es lento y verboso. NumPy opera sobre arreglos completos con una sola expresión y es la base de casi toda la ciencia con Python.
- 🔗 **Se estudia junto con:** NumPy, arreglo, vectorizada, difusión.

📘 **Dónde se aprende** (1 clase): [B07-C09 · Cálculos científicos básicos con Python](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md).

### Mediación temprana

- La mediación temprana actúa antes del umbral.

💡 **Cómo se explica en la clase [B104-C16](../programa/clases/B104/B104-C16-manejo-de-conflictos/CLASE.md):**
- En 180 días y 4 personas (1 500 tripulaciones sintéticas, semilla 104), sin intervención hay en promedio 1,55 episodios y el 78,7 % de las tripulaciones tiene al menos uno; con una reunión semanal que reduce la tensión a la mitad, 0,40 y 32,8 %; con mediación temprana al cruzar 1,2 (reduce 20 %), 0,00 y 0,3 %.
- Ejercicio 6 · autónomo. ¿Por qué la mediación temprana casi elimina los episodios?
- 🎯 **Por qué importa:** Un conflicto abierto cuesta tiempo, errores y confianza; prevenirlo cuesta pequeñas conversaciones continuas. La decisión central: ¿cuánto reduce una intervención temprana la probabilidad de que la tensión llegue al conflicto abierto, frente a no hacer nada o reunirse una vez por semana?
- 🔗 **Se estudia junto con:** tensión, persistencia, conflicto abierto, reunión de revisión.

📘 **Dónde se aprende** (1 clase): [B104-C16 · Manejo de conflictos](../programa/clases/B104/B104-C16-manejo-de-conflictos/CLASE.md).

### Mediana

- Un cuantil `q_α` cumple `F(q_α) = α`; la mediana es `q_0,5`.
- La mediana es el valor central.
- La mediana resiste valores atípicos pero es `√(π/2) = 1,2533` veces más ruidosa.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- `P(T > 7) = 3 · 0,1 = 0,3`; mediana `5 s`.
- P(Y = 0) = 0 (un punto); mediana = 0.0; cuantil 0.95 = 1.7999999999999998
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.
- 🔗 **Se estudia junto con:** variable aleatoria, discreta, continua, función de masa de probabilidad.

📘 **Dónde se aprende** (6 clases): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md); [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md); [B44-C12 · Calibración con bias](../programa/clases/B44/B44-C12-calibracion-con-bias/CLASE.md); [B45-C23 · Fotometría de apertura y estimación del cielo](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md); [B48-C11 · Calidad y clasificación de datos](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md); [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md).

### Mediana de la pila

- La mediana de la pila ignora valores atípicos si menos de la mitad de los cuadros los tienen.

💡 **Cómo se explica en la clase [B44-C16](../programa/clases/B44/B44-C16-ruido-cosmico-e-identificacion/CLASE.md):**
- *Descripción textual:* la mediana de la pila da el valor esperado por píxel; los residuos grandes se marcan como impactos.
- 🎯 **Por qué importa:** Un impacto fuerte parece una estrella o un defecto. La decisión central: ¿cuántos cuadros hacen falta para identificar los impactos y cuándo falla la mediana?
- 🔗 **Se estudia junto con:** rayo cósmico, pila, coincidencia.

📘 **Dónde se aprende** (1 clase): [B44-C16 · Ruido cósmico e identificación](../programa/clases/B44/B44-C16-ruido-cosmico-e-identificacion/CLASE.md).

### Mediana temporal

- La mediana temporal de las imágenes alineadas es una estimación del cielo estático.

💡 **Cómo se explica en la clase [B15-C20](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md):**
- C --> D["Cielo estático:<br/>mediana temporal"]
- *Descripción textual:* las imágenes se registran y alinean, se obtiene el cielo estático con la mediana temporal, se resta, se filtra y se umbraliza para obtener detecciones, que alimentan un filtro de Kalman; el informe recoge los errores de cada etapa y el total.
- 🎯 **Por qué importa:** Detectar y seguir un objeto móvil —un asteroide, un fragmento de basura espacial, un satélite— combina varios problemas: la cámara no apunta exactamente igual en cada imagen, las estrellas fijas saturan la escena, el objeto es débil y la medida es ruidosa.
- 🔗 **Se estudia junto con:** requisito, prueba de extremo a extremo, imagen de diferencia, detección.

📘 **Dónde se aprende** (1 clase): [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md).

### Medias por unidad

- El GUM estima la esperanza con la media de observaciones y la desviación experimental con `n − 1` (S1, 4.2.1–4.2.2) y describe la `t` con `n − 1` grados de libertad (S1, G.3.2): aquí «observaciones independientes» son las medias por unidad.

💡 **Cómo se explica en la clase [B12-C25](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md):**
- El intervalo correcto para el nivel medio trata las medias por unidad como la muestra y usa la `t` con `m − 1 = 5` grados de libertad (`t = 2,571`, S1, G.3.2).
- El análisis de medias por unidad (resumir cada unidad y analizar los resúmenes) es simple y robusto con muestras pequeñas.
- 🎯 **Por qué importa:** Seis personas medidas cuatro veces dan 24 números, pero no 24 piezas de información independientes: las de una misma persona se parecen. Ignorar eso produce intervalos demasiado angostos para el nivel medio y, paradójicamente, demasiado anchos para los cambios dentro de cada persona.
- 🔗 **Se estudia junto con:** diseño longitudinal, modelo de intercepto aleatorio, efectos fijos, efecto aleatorio.

📘 **Dónde se aprende** (1 clase): [B12-C25 · Modelos longitudinales y de efectos mixtos para muestras pequeñas](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md).

### Medida

- Una constante es un valor que no cambia: exacta por definición (como `c = 299 792 458 m/s` en el SI, S4), medida (como `G`, con incertidumbre) o nominal (valor de conversión fijado por acuerdo, como el `(GM)☉` de la IAU).
- La medida reduce `P` (prevención) o `S` (mitigación).

💡 **Cómo se explica en la clase [B03-C12](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md):**
- K --> ME["Medida: G, con incertidumbre"]
- Un símbolo se pregunta si cambia en el problema (variable); si no, si es propio del caso (parámetro) o universal (constante); y la constante universal se clasifica en exacta, medida o nominal.
- 🎯 **Por qué importa:** La masa del Sol se conoce con unas cinco cifras. Sin embargo, el producto `GM` del Sol se conoce con diez, y la constante `G` por sí sola con apenas cinco.
- 🔗 **Se estudia junto con:** variable, parámetro, constante, exacta por definición.

📘 **Dónde se aprende** (2 clases): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B114-C06 · Matriz de riesgo ambiental de un hábitat](../programa/clases/B114/B114-C06-matriz-de-riesgo-ambiental-de-un-habitat/CLASE.md).

### Medida de dispersión

- La medida de dispersión (DM) es la columna de electrones.
- La medida de dispersión `DM = ∫ n_e dl` (pc cm⁻³).

💡 **Cómo se explica en la clase [B29-C17](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md):**
- La desdispersión recupera la medida de dispersión con una incertidumbre de pocos `pc/cm³` y más que duplica la relación señal-ruido.
- *Descripción textual:* la constante de dispersión y la medida de dispersión dan el retardo por canal; se desplazan los canales, se suman y se mide la relación señal-ruido; el máximo del barrido en `DM` da la medida recuperada.
- 🎯 **Por qué importa:** La medida de dispersión informa de la distancia a la fuente y de la materia que atravesó. Sin desdispersión, un pulso breve se pierde entre canales.
- 🔗 **Se estudia junto con:** dispersión, desdispersión, ensanchamiento intra-canal, resolución en DM.

📘 **Dónde se aprende** (3 clases): [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md); [B29-C17 · Fenómenos transitorios rápidos](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md); [B46-C02 · Propagación de ondas de radio](../programa/clases/B46/B46-C02-propagacion-de-ondas-de-radio/CLASE.md).

### Medida de emisión

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B34-C02](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md):**
- *Descripción textual:* la temperatura fija la banda y la energía térmica; la densidad y el volumen fijan la medida de emisión y la potencia.
- El script [emision.py](emision.py) calcula las escalas y la medida de emisión (comprueba Wien a `10⁻⁹`).
- 🎯 **Por qué importa:** Cada banda del espectro traza una temperatura. La decisión central: ¿en qué banda emite el plasma a una temperatura dada y cuánta potencia radia?
- 🔗 **Se estudia junto con:** máximo de Wien, energía térmica, bremsstrahlung, plasma ópticamente delgado.

📘 **Dónde se aprende** (1 clase): [B34-C02 · Emisión EUV y rayos X de la corona](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md).

### Medida de fomento de la confianza

- Una medida de fomento de la confianza reduce la incertidumbre sobre las intenciones.

💡 **Cómo se explica en la clase [B119-C29](../programa/clases/B119/B119-C29-escalada-desescalada-y-medidas-de-fomento-de-la-confianza/CLASE.md):**
- No se consultaron documentos sobre medidas de transparencia y fomento de la confianza ni teoría de la disuasión.
- python programa/clases/B119/B119-C29-escalada-desescalada-y-medidas-de-fomento-de-la-confianza/laboratorio.py
- 🎯 **Por qué importa:** C28 y C27 tratan conductas y negociación; ninguna clase muestra la dinámica de escalada ni el valor de las medidas de confianza, que se apoyan en el principio de informar (art. XI) y consultar (art.
- 🔗 **Se estudia junto con:** nivel de escalada, desescalada, matriz fundamental, absorción.

📘 **Dónde se aprende** (1 clase): [B119-C29 · Escalada, desescalada y medidas de fomento de la confianza](../programa/clases/B119/B119-C29-escalada-desescalada-y-medidas-de-fomento-de-la-confianza/CLASE.md).

### Medida de rotación

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B51-C05](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md):**
- **Idea central (modelo mental):** Como un prisma que desvía más la luz azul que la roja: la ionosfera retrasa más las frecuencias bajas, y por eso dos frecuencias bastan para medir cuánto prisma hay en el camino.
- 🎯 **Por qué importa:** A frecuencias bajas la ionosfera domina el error de fase y de polarización. La decisión central: ¿cómo se mide y se quita el efecto con las propias frecuencias de la observación?
- 🔗 **Se estudia junto con:** contenido electrónico total, retardo dispersivo, rotación de Faraday, ambigüedad nπ.

📘 **Dónde se aprende** (1 clase): [B51-C05 · Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md).

### Medida F

- La medida F con parámetro `β` es `(1 + β²) P R/(β² P + R)`;

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Una exhaustividad medida sobre 50 positivos tiene error estándar `√(0,5 × 0,5/50) = 0,07`.
- Ejercicio 9 · transferencia. El estudio de Kepler informa 98,8 % en una medida de ordenamiento.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.
- 🔗 **Se estudia junto con:** matriz de confusión, verdaderos positivos, falsos positivos, verdaderos negativos.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Medida por ida y vuelta

- La medida por ida y vuelta divide entre dos: `d = c t/2`.

💡 **Contexto en la clase [B13-C06](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md):**
- **Idea central (modelo mental):** Piensa en una distancia como una cuerda que se mide con el tiempo que una señal tarda en recorrerla. Si el cronómetro tiene un error, la «cuerda» se alarga o se acorta en `c` veces ese error.
- 🎯 **Por qué importa:** Cuando un telémetro láser mide la distancia a la Luna, lo que mide es el tiempo que tarda un pulso en ir y volver. Un error de un nanosegundo en ese tiempo equivale a 15 centímetros de distancia.
- 🔗 **Se estudia junto con:** segundo, metro, realización, desviación relativa de frecuencia.

📘 **Dónde se aprende** (1 clase): [B13-C06 · Patrones de longitud y tiempo](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md).

### Medida provisional

- Una medida provisional (art. 26) puede exigir daño irreparable probable y posibilidad razonable de éxito (art. 26(3)).

💡 **Cómo se explica en la clase [B123-C04](../programa/clases/B123/B123-C04-arbitraje-y-resolucion-de-controversias-espaciales/CLASE.md):**
- Para ciertas medidas provisionales se exige daño irreparable probable y posibilidad razonable de éxito (art. 26(3)); en el laboratorio se usan umbrales `0,5` y `0,3`, que son convención didáctica, no del texto.
- *Descripción textual:* una controversia puede seguir la negociación, la comisión del Convenio o el arbitraje; en el arbitraje se pactan el tribunal, las medidas provisionales y la confidencialidad.
- 🎯 **Por qué importa:** Elegir la vía condiciona plazo, costo, confidencialidad y fuerza obligatoria de la decisión. La decisión central: ¿qué vía y qué reglas conviene pactar, y con qué compromisos?
- 🔗 **Se estudia junto con:** Reglas Opcionales, Secretario General de la CPA, confidencialidad, peritos.

📘 **Dónde se aprende** (1 clase): [B123-C04 · Arbitraje y resolución de controversias espaciales](../programa/clases/B123/B123-C04-arbitraje-y-resolucion-de-controversias-espaciales/CLASE.md).

### Medida z_ij

- Grafo de poses: nodos = poses, aristas = restricciones relativas (F4). Medida `z_ij`: pose relativa medida entre `i` y `j`.

💡 **Cómo se explica en la clase [B99-C03](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md):**
- (F4) formulan el SLAM como un grafo: los nodos son las poses `x_i`, una arista `(i, j)` lleva una medida virtual `z_ij` (la transformación que hace coincidir las observaciones de `i` y de `j`) con su matriz de información `Ω_ij`, y el error `e_ij(x_i, x_j)` es la diferencia entre la medida y la predicha.
- 🎯 **Por qué importa:** Sumar movimientos da una trayectoria que no cierra el lazo; una medida de cierre de bucle dice que la pose final es la inicial. La decisión central: ¿cómo repartir el desacuerdo entre cientos de poses de modo coherente con la incertidumbre de cada medida?
- 🔗 **Se estudia junto con:** Grafo de poses, Información Ω_ij, Error de arista e_ij, Gauss–Newton.

📘 **Dónde se aprende** (1 clase): [B99-C03 · SLAM basado en grafos de poses](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md).

### Medido

- Un valor exacto no tiene incertidumbre porque es una definición; un valor medido sí la tiene.
- Un dato reconstruido nunca es un dato medido: debe marcarse con una bandera.

💡 **Cómo se explica en la clase [B13-C01](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md):**
- Si el factor es medido, la incertidumbre se hereda.
- Con factores medidos (`G`): la incertidumbre se hereda.
- 🎯 **Por qué importa:** Una señal de radio o de láser viaja a la Luna y regresa. Para decir «la Luna está a 384 400 km» hay que haber acordado qué es un kilómetro, qué es un segundo y a qué velocidad viaja la señal.
- 🔗 **Se estudia junto con:** Sistema Internacional de Unidades (SI), unidad base, constante definitoria, exacto.

📘 **Dónde se aprende** (2 clases): [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md); [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md).

### Medio homogéneo e isótropo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C01](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md):**
- **Idea central (modelo mental):** Como un socorrista que corre más rápido en la arena que nadando: para llegar antes al bañista no va en línea recta, sino que entra al agua en el punto que minimiza el tiempo; la luz hace lo mismo entre medios de distinta velocidad.
- 🎯 **Por qué importa:** Sin un modelo de rayos no se puede diseñar un telescopio. La decisión central: ¿cuándo basta con rayos y cuánto tarda la luz en cada medio?
- 🔗 **Se estudia junto con:** rayo, índice de refracción, camino óptico, principio de Fermat.

📘 **Dónde se aprende** (1 clase): [B41-C01 · Naturaleza y propagación de la luz](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md).

### Medio interestelar (MIS)

- El medio interestelar (MIS) es la materia (gas y polvo), los rayos cósmicos y el campo magnético entre las estrellas.

💡 **Cómo se explica en la clase [B25-C03](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md):**
- python programa/clases/B25/B25-C03-medio-interestelar-multifasico/fases_ism.py
- 🎯 **Por qué importa:** Las estrellas nacen del gas y devuelven gas enriquecido; el medio interestelar (MIS) es el almacén y el escenario de ese ciclo. Pero «gas» sirve de poco: un volumen del MIS puede estar a `10 K` o a `10⁶ K`, y su densidad variar un factor 10⁷ de un punto a otro.
- 🔗 **Se estudia junto con:** fase, medio neutro frío, medio neutro tibio, medio ionizado tibio.

📘 **Dónde se aprende** (1 clase): [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md).

### Medio intracúmulo (ICM)

- El medio intracúmulo (ICM) es ese gas caliente, ionizado, que emite en rayos X.

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- Definir cúmulo de galaxias, medio intracúmulo, equilibrio hidrostático y perfil beta.
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.
- 🔗 **Se estudia junto con:** cúmulo de galaxias, temperatura, equilibrio hidrostático, perfil beta.

📘 **Dónde se aprende** (1 clase): [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md).

### Medio ionizado tibio

- El medio neutro frío (CNM) y el medio neutro tibio (WNM) son gas de hidrógeno atómico; el medio ionizado tibio (WIM) y el ionizado caliente (HIM) están ionizados.

💡 **Contexto en la clase [B25-C03](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md):**
- **Idea central (modelo mental):** Piensa en una olla con agua y vapor a la misma presión: dos fases muy distintas en densidad conviven si la presión coincide. Analogía: la fase fría es el agua (densa, fría) y la tibia es el vapor (tenue, caliente).
- 🎯 **Por qué importa:** Las estrellas nacen del gas y devuelven gas enriquecido; el medio interestelar (MIS) es el almacén y el escenario de ese ciclo. Pero «gas» sirve de poco: un volumen del MIS puede estar a `10 K` o a `10⁶ K`, y su densidad variar un factor 10⁷ de un punto a otro.
- 🔗 **Se estudia junto con:** medio interestelar (MIS), fase, medio neutro frío, medio neutro tibio.

📘 **Dónde se aprende** (1 clase): [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md).

### Medio neutro frío

- El medio neutro frío (CNM) y el medio neutro tibio (WNM) son gas de hidrógeno atómico; el medio ionizado tibio (WIM) y el ionizado caliente (HIM) están ionizados.

💡 **Contexto en la clase [B25-C03](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md):**
- **Idea central (modelo mental):** Piensa en una olla con agua y vapor a la misma presión: dos fases muy distintas en densidad conviven si la presión coincide. Analogía: la fase fría es el agua (densa, fría) y la tibia es el vapor (tenue, caliente).
- 🎯 **Por qué importa:** Las estrellas nacen del gas y devuelven gas enriquecido; el medio interestelar (MIS) es el almacén y el escenario de ese ciclo. Pero «gas» sirve de poco: un volumen del MIS puede estar a `10 K` o a `10⁶ K`, y su densidad variar un factor 10⁷ de un punto a otro.
- 🔗 **Se estudia junto con:** medio interestelar (MIS), fase, medio neutro tibio, medio ionizado tibio.

📘 **Dónde se aprende** (1 clase): [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md).

### Medio neutro tibio

- El medio neutro frío (CNM) y el medio neutro tibio (WNM) son gas de hidrógeno atómico; el medio ionizado tibio (WIM) y el ionizado caliente (HIM) están ionizados.

💡 **Contexto en la clase [B25-C03](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md):**
- **Idea central (modelo mental):** Piensa en una olla con agua y vapor a la misma presión: dos fases muy distintas en densidad conviven si la presión coincide. Analogía: la fase fría es el agua (densa, fría) y la tibia es el vapor (tenue, caliente).
- 🎯 **Por qué importa:** Las estrellas nacen del gas y devuelven gas enriquecido; el medio interestelar (MIS) es el almacén y el escenario de ese ciclo. Pero «gas» sirve de poco: un volumen del MIS puede estar a `10 K` o a `10⁶ K`, y su densidad variar un factor 10⁷ de un punto a otro.
- 🔗 **Se estudia junto con:** medio interestelar (MIS), fase, medio neutro frío, medio ionizado tibio.

📘 **Dónde se aprende** (1 clase): [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md).

### Mediodía solar

- El mediodía solar es el instante en que el Sol cruza el meridiano local, la línea imaginaria norte–sur sobre tu cabeza; el USNO lo llama *tránsito* (S3).

💡 **Cómo se explica en la clase [B08-C01](../programa/clases/B08/B08-C01-orientacion-geografica-y-puntos-cardinales/CLASE.md):**
- Ejercicio 2 · con pista. La sombra de una vara de 1,20 m mide 0,50 m al mediodía solar.
- Ejercicio 5. ¿Qué altura tiene el Sol al mediodía solar del 21 de diciembre a −30°?
- 🎯 **Por qué importa:** Una persona que llega de noche a un lugar oscuro sin saber dónde está el este no sabe dónde buscar una salida de Luna, ni hacia dónde apuntar un telescopio, ni qué rumbo debe tomar si pierde el sendero. La pregunta motivadora es: ¿cómo sé hacia dónde miro, sin depender de un aparato que se puede descargar o descalibrar?
- 🔗 **Se estudia junto con:** norte geográfico (verdadero), norte magnético, declinación magnética, acimut.

📘 **Dónde se aprende** (1 clase): [B08-C01 · Orientación geográfica y puntos cardinales](../programa/clases/B08/B08-C01-orientacion-geografica-y-puntos-cardinales/CLASE.md).
