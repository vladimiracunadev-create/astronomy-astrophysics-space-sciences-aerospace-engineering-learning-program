# Términos · J

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · **J** · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### J₂

- El coeficiente `J₂` mide el exceso de masa ecuatorial: en el potencial, `V = (GM/r)[1 − J₂ (a/r)² P₂(sin φ)]` con `P₂(s) = (3s² − 1)/2` y `φ` la latitud.

💡 **Cómo se explica en la clase [B09-C20](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md):**
- Para un punto del eje del polo (`φ = 90°`, `P₂ = 1`) y del ecuador (`φ = 0`, `P₂ = −1/2`), el módulo de la atracción es `g = GM/r² [1 − 3 J₂ (a/r)² P₂]`.
- Para la Tierra, el error de usar `GM/R²` con un `R` genérico es del orden de 0,5 %; la corrección de `J₂` en órbita decae como `(a/r)²` (a 400 km de altitud, `J₂ (a/r)² ≈ 9,6 × 10⁻⁴`): una corrección de esa magnitud no puede ignorarse en un seguimiento orbital preciso (B11, B13).
- 🎯 **Por qué importa:** Una sonda en órbita, un satélite geodésico o un gravímetro en una montaña reciben la atracción de un cuerpo que no es un punto: tiene tamaño, forma achatada, rotación y estructura interna. Reducirlo a un punto es correcto fuera de una esfera homogénea, pero deja de serlo cuando importa el achatamiento o el interior.
- 🔗 **Se estudia junto con:** teorema de la capa, potencial de una capa, masa encerrada, achatamiento.

📘 **Dónde se aprende** (1 clase): [B09-C20 · Aplicaciones a campos gravitatorios](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md).

### J2

- Un armónico zonal `J_n` es el coeficiente de un término que solo depende de la latitud. J2 mide el achatamiento dinámico.
- El J2 causa la precesión de la línea de nodos.

💡 **Cómo se explica en la clase [B72-C02](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md):**
- La forma general con `n = 2` coincide con la fórmula cerrada de J2 en `0` (diferencia relativa exacta).
- J2 es unas `300` a `500` veces mayor que J3 y J4.
- ⚠️ **Error frecuente:** Creer que J2 es igual en todas las latitudes. Se corrige con 8.4.
- 🎯 **Por qué importa:** Sin un potencial no hay perturbación gravitatoria que calcular, y los números de la bibliografía (J2, J3, J4) dependen de un convenio de signos y de un radio de referencia. La decisión central: ¿qué términos del potencial incluir y con qué radio y convenio, para que J2 signifique lo mismo en tu código y en la fuente?
- 🔗 **Se estudia junto con:** armónico zonal, polinomio de Legendre, convenio de signos, gradiente.

📘 **Dónde se aprende** (2 clases): [B72-C02 · Potencial gravitatorio no esférico](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md); [B74-C20 · Validación frente a efemérides de referencia](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md).

### J2000

- Una época es la fecha a la que se refieren las coordenadas; la precesión es el lento giro del eje de la Tierra, que desplaza el sistema entero unos 50″ al año. J2000 es la época del 1 de enero de 2000, 12:00 (D. juliano 2451545,0); el IAU la usa en los datos de límites de las constelaciones (S2).
- La anchura de ventana es el intervalo de fechas que cumple una tolerancia angular. J2000 es el origen de tiempos. «Oportunidad» y «ventana» se usan aquí como sinónimos.

💡 **Cómo se explica en la clase [B08-C03](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md):**
- La AR y la Dec de la tabla están en J2000.
- Para la Luna del 5 de noviembre de 2025 (25,8 años después de J2000), el laboratorio da un cambio de `1272″` en AR y `443″` en Dec: una separación de `0,360°`.
- 🎯 **Por qué importa:** Un catálogo no puede decir «a la izquierda de la Luna», porque eso cambia a cada minuto. Necesita direcciones fijas.
- 🔗 **Se estudia junto con:** declinación, ecuador celeste, ascensión recta, punto vernal.

📘 **Dónde se aprende** (2 clases): [B08-C03 · Ascensión recta y declinación](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md); [B75-C03 · Ventanas de lanzamiento](../programa/clases/B75/B75-C03-ventanas-de-lanzamiento/CLASE.md).

### Jackknife

- El jackknife (o *leave-one-out*) repite el ajuste quitando una observación cada vez.

💡 **Cómo se explica en la clase [B20-C03](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md):**
- En el jackknife se calcula `b₋ᵢ` sin el punto `i` para cada `i`.
- Ejercicio 4. Calcula a mano el jackknife de la pendiente para los puntos `(0,0), (1,1), (2,2), (3,6)`: la pendiente completa y la que resulta al quitar cada punto.
- 🎯 **Por qué importa:** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.
- 🔗 **Se estudia junto con:** revisión por pares, autor, árbitro, editor.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Jacobi

- El error `e = u_exacta − u` es la diferencia con la solución del sistema. Jacobi y Gauss–Seidel son métodos de relajación.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- En Jacobi los cuatro vecinos son de la iteración anterior.
- Jacobi tiene la ventaja de que todos los puntos se calculan a la vez.
- ⚠️ **Error frecuente:** Medir el progreso por el cambio entre iteraciones y no por el residuo. Un cambio pequeño no significa solución cercana: Jacobi cambia poco por iteración justo cuando está lejos (ejercicio 4).
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;
- 🔗 **Se estudia junto con:** ecuación de Poisson, elíptico, de Dirichlet, estencil de cinco puntos.

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Jacobi inercial

- El Jacobi inercial es `−2(E_in − h_z)` con `E_in = ½ v² − (1−μ)/r1 − μ/r2`.

💡 **Cómo se explica en la clase [B76-C17](../programa/clases/B76/B76-C17-sistemas-de-referencia-relativos/CLASE.md):**
- *Descripción textual:* se convierte entre el marco inercial y los rotantes (LVLH y sinódico) rotando y restando la velocidad de arrastre; dos invariantes (la velocidad de un punto fijo y Jacobi) comprueban cada conversión.
- Un estado cislunar convertido a inercial recupera su valor con error `10⁻¹⁶` y la constante de Jacobi coincide en las dos formas (`3,0007976884`).
- 🎯 **Por qué importa:** Una posición correcta en el marco equivocado es una colisión. La decisión central: ¿cómo se convierten posición y velocidad entre los marcos de la misión y cómo se comprueba la conversión?
- 🔗 **Se estudia junto con:** marco LVLH, marco sinódico, velocidad de arrastre.

📘 **Dónde se aprende** (1 clase): [B76-C17 · Sistemas de referencia relativos](../programa/clases/B76/B76-C17-sistemas-de-referencia-relativos/CLASE.md).

### Jacobiano

- El jacobiano es el factor que corrige el elemento de área o volumen al cambiar de coordenadas: `r` en polares, `r² sin θ` en esféricas (ecs. 1.5.39 y 1.5.41).
- El jacobiano de `f: ℝⁿ → ℝᵐ` es la matriz `m × n` de derivadas parciales `Jᵢⱼ = ∂fᵢ/∂pⱼ`.
- El jacobiano `J` es la matriz de derivadas `Jᵢⱼ = ∂y(tᵢ; p)/∂pⱼ`: cuánto cambia cada predicción si se mueve cada parámetro.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C18](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md):**
- *Descripción textual:* se elige el sistema de coordenadas según la simetría, se escribe el elemento de volumen con su jacobiano, se integra iterativamente y se verifica con un caso conocido.
- Su límite: si olvidas el jacobiano, las capas externas pesan igual que las internas, lo cual es falso.
- ⚠️ **Error frecuente:** Olvidar el jacobiano. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** La masa de la Tierra se conoce mucho mejor que la distribución de esa masa en su interior. Un solo número, la densidad media, no basta: el momento de inercia depende de cómo se reparte la masa.
- 🔗 **Se estudia junto con:** integral doble, integración iterada, integral triple, teorema de Fubini.

📘 **Dónde se aprende** (12 clases): [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md); [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md); [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md); [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md); [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md) y 6 más.

### Jacobiano de medida

- El jacobiano de medida `H` se evalúa en el estado predicho.

💡 **Cómo se explica en la clase [B74-C09](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md):**
- Escribir los pasos del EKF con matriz de transición y jacobiano de medida.
- 🎯 **Por qué importa:** Una órbita no es lineal en el estado, pero a cortos intervalos y con errores pequeños se comporta casi como tal. La decisión central: ¿hasta cuándo es válida la linealización del EKF y cómo me doy cuenta de que dejó de serlo?
- 🔗 **Se estudia junto con:** EKF, matriz de transición, NEES, forma de Joseph.

📘 **Dónde se aprende** (1 clase): [B74-C09 · Filtro de Kalman extendido](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md).

### Jacobiano geométrico

- Jacobiano geométrico: `J(q)` de 6×7, con filas de velocidad lineal y angular.

💡 **Cómo se explica en la clase [B101-C03](../programa/clases/B101/B101-C03-singularidades-y-manipulabilidad-de-brazos-roboticos/CLASE.md):**
- Calcular el jacobiano geométrico de 6×7 y verificarlo por diferencias finitas.
- 🎯 **Por qué importa:** Con el brazo casi estirado, pedirle un movimiento de 5 cm/s a lo largo de su eje exige velocidades articulares de varios rad/s. La decisión central: ¿cuán cerca de una singularidad estoy y qué error de seguimiento acepto para no exigir lo imposible?
- 🔗 **Se estudia junto con:** Singularidad, Manipulabilidad w, Valor singular σ, Número de condición.

📘 **Dónde se aprende** (1 clase): [B101-C03 · Singularidades y manipulabilidad de brazos robóticos](../programa/clases/B101/B101-C03-singularidades-y-manipulabilidad-de-brazos-roboticos/CLASE.md).

### Janski

- El janski `1 Jy = 10⁻²⁶ W m⁻² Hz⁻¹` (definición).

💡 **Contexto en la clase [B51-C01](../programa/clases/B51/B51-C01-calibracion-de-amplitud-y-escala-de-flujo-con-calibradores-primarios/CLASE.md):**
- **Idea central (modelo mental):** Como medir con una regla sin números: primero la comparas con una regla patrón (el primario) para saber cuánto vale cada marca (la ganancia), y después mides con ella el objeto desconocido.
- 🎯 **Por qué importa:** Sin una escala de flujo, dos observaciones de la misma fuente en días distintos no se pueden comparar. La decisión central: ¿cómo se fija y se propaga una escala absoluta, y con qué incertidumbre?
- 🔗 **Se estudia junto con:** calibrador primario, ganancia de amplitud, bootstrap de flujo, índice espectral.

📘 **Dónde se aprende** (1 clase): [B51-C01 · Calibración de amplitud y escala de flujo con calibradores primarios](../programa/clases/B51/B51-C01-calibracion-de-amplitud-y-escala-de-flujo-con-calibradores-primarios/CLASE.md).

### Jansky

- El jansky vale `10⁻²⁶ W m⁻² Hz⁻¹`.

💡 **Contexto en la clase [B46-C01](../programa/clases/B46/B46-C01-espectro-radioastronomico/CLASE.md):**
- **Idea central (modelo mental):** Rayleigh–Jeans es una regla que mide temperatura con una escala lineal; funciona en el centro de la escala y se deforma al borde, cuando el fotón tiene energía comparable a la térmica.
- 🎯 **Por qué importa:** Casi toda la radioastronomía usa Rayleigh–Jeans porque convierte brillo en temperatura de forma lineal, pero deja de valer cuando `hν` se acerca a `kT`. La decisión central: ¿en qué frecuencia y temperatura es válida la aproximación de Rayleigh–Jeans?
- 🔗 **Se estudia junto con:** brillo, flujo, temperatura de brillo, Rayleigh–Jeans.

📘 **Dónde se aprende** (1 clase): [B46-C01 · Espectro radioastronómico](../programa/clases/B46/B46-C01-espectro-radioastronomico/CLASE.md).

### Jardinería

- La jardinería es la mezcla vertical por impactos.
- La jardineria es la mezcla vertical del regolito por impactos.

💡 **Cómo se explica en la clase [B55-C14](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md):**
- Jardineria: fraccion de una capa de 1 cm que sigue sin voltear (lambda = 1/1e8 anos, ILUSTRATIVA)
- 🎯 **Por qué importa:** El regolito es el suelo de un cuerpo sin atmósfera y su química depende de qué impactos lo removieron y de qué componentes lo formaron. La decisión central: ¿cuánto tiempo hace falta para que una capa se voltee y qué mezcla de componentes explica la composición medida?
- 🔗 **Se estudia junto con:** tasa de volteo, fracción sin voltear, componente, mezcla lineal.

📘 **Dónde se aprende** (2 clases): [B53-C22 · Meteorización espacial: micrometeoritos, viento solar y maduración del regolito](../programa/clases/B53/B53-C22-meteorizacion-espacial-micrometeoritos-viento-solar-y-maduracion-del-regolito/CLASE.md); [B55-C14 · Química de regolitos](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md).

### Jeffries–Matusita

- La distancia de Jeffries–Matusita es `JM = 2(1 − e^{−B})`, entre 0 (idénticas) y 2 (perfectamente separables).

💡 **Cómo se explica en la clase [B57-C25](../programa/clases/B57/B57-C25-seleccion-de-bandas-espectrales-segun-el-fenomeno/CLASE.md):**
- Calcular la distancia de Bhattacharyya y la de Jeffries–Matusita entre clases gaussianas.
- El script [bandas.py](bandas.py) calcula la separabilidad Jeffries–Matusita entre cuatro clases sintéticas y busca el mejor subconjunto de bandas por fuerza bruta y por búsqueda voraz (comprueba la JM calculada frente a la fórmula analítica a 1e-12 y que el óptimo exhaustivo no es peor que el voraz).
- 🎯 **Por qué importa:** Cada banda cuesta datos, masa y complejidad. La decisión central: ¿con qué menor número de bandas se separan las clases que me interesan y cuál es el par más difícil de distinguir?
- 🔗 **Se estudia junto con:** separabilidad, Bhattacharyya, objetivo mínimo, búsqueda voraz.

📘 **Dónde se aprende** (1 clase): [B57-C25 · Selección de bandas espectrales según el fenómeno](../programa/clases/B57/B57-C25-seleccion-de-bandas-espectrales-segun-el-fenomeno/CLASE.md).

### Jerarquía de memoria

- La jerarquía de memoria es la escalera de almacenamientos de la CPU: registros, cachés de nivel 1, 2 y 3, memoria principal; cuanto más cerca de la CPU, más pequeña y rápida.

💡 **Cómo se explica en la clase [B18-C03](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md):**
- Describir la jerarquía de memoria y la función de la línea de caché.
- python programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/memoria_y_cache.py
- 🎯 **Por qué importa:** Un catálogo con millones de estrellas o una rejilla de simulación pasan cada dato por la CPU una o pocas veces. Cuando las operaciones por dato son pocas, el tiempo no lo fija la CPU sino el viaje de los datos.
- 🔗 **Se estudia junto con:** caché, línea de caché, localidad espacial, temporal.

📘 **Dónde se aprende** (1 clase): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md).

### Jerárquica

- La binaria de fondo y la jerárquica imitan un tránsito.

💡 **Cómo se explica en la clase [B29-C07](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md):**
- Esta clase no reproduce ese método: usa tres escenarios sintéticos (planeta `0,30`, binaria de fondo `0,40`, binaria jerárquica `0,30`) y un observable `x` normal en cada uno.
- 🎯 **Por qué importa:** Hay muchos más candidatos que posibilidades de seguimiento. Validar bien exige probabilidades honestas: ni optimistas ni conservadoras en exceso.
- 🔗 **Se estudia junto con:** validación, FPP, escenario, prior.

📘 **Dónde se aprende** (1 clase): [B29-C07 · Métodos de validación planetaria](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md).

### Jerga

- La jerga es vocabulario no compartido.

💡 **Cómo se explica en la clase [B128-C08](../programa/clases/B128/B128-C08-lenguaje-claro-y-redaccion-accesible/CLASE.md):**
- Palabras por frase, frases de más de 25 palabras (umbral del curso), pasivas (heurística con `fue/fueron/es/son/siendo` + participio), nominalizaciones (`realización de`, `utilización de`…) y términos de jerga de una lista corta.
- La jerga baja de 3 a 2: «elongación angular» y «paralaje» siguen, y deben definirse en un glosario ([C09](../B128-C09-apoyo-multilingue-y-glosarios/CLASE.md)).
- ⚠️ **Error frecuente:** Dejar la jerga sin definir. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** El lenguaje claro ayuda a personas con dificultades de lectura, a quienes leen en una segunda lengua, a quien lee con prisa y a quien usa un lector de pantalla. La decisión central: ¿qué cambios hacen el texto más claro sin perder ninguna cifra ni ningún aviso de seguridad?
- 🔗 **Se estudia junto con:** lenguaje claro, voz activa, verbo escondido, métrica de superficie.

📘 **Dónde se aprende** (1 clase): [B128-C08 · Lenguaje claro y redacción accesible](../programa/clases/B128/B128-C08-lenguaje-claro-y-redaccion-accesible/CLASE.md).

### Jitter

- El jitter es el componente rápido.
- El jitter es su variación.
- El jitter es la desviación aleatoria rápida del eje.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B47-C10](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md):**
- El modelo supone PSF gaussiana y *jitter* independiente por eje; ignora la deriva y la dependencia temporal con el tiempo de exposición.
- *Descripción textual:* la PSD describe cómo se reparte la potencia del *jitter* en frecuencia; integrada da el RMS y este ensancha la imagen.
- 🎯 **Por qué importa:** Una buena óptica con mal apuntamiento da imágenes borrosas. La decisión central: ¿qué RMS de *jitter* se puede tolerar para perder menos del 10 % del pico?
- 🔗 **Se estudia junto con:** deriva, densidad espectral de potencia, RMS, proceso de Ornstein-Uhlenbeck.

📘 **Dónde se aprende** (6 clases): [B47-C10 · Estabilidad de apuntamiento](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md); [B48-C10 · Redes de instrumentos](../programa/clases/B48/B48-C10-redes-de-instrumentos/CLASE.md); [B87-C15 · Apuntamiento de alta precisión](../programa/clases/B87/B87-C15-apuntamiento-de-alta-precision/CLASE.md); [B88-C19 · Simulación hardware-in-the-loop](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md); [B88-C26 · Latencia de interrupciones y jitter](../programa/clases/B88/B88-C26-latencia-de-interrupciones-y-jitter/CLASE.md); [B92-C03 · Adquisición, apuntamiento y seguimiento ópticos](../programa/clases/B92/B92-C03-adquisicion-apuntamiento-y-seguimiento-opticos/CLASE.md).

### Jitter de fase

- El jitter de fase teórico es `σ_φ ≈ 1/√SNR_L`.

💡 **Cómo se explica en la clase [B89-C10](../programa/clases/B89/B89-C10-sincronizacion-de-portadora/CLASE.md):**
- PD --> E["error de fase: media y jitter"]
- *Descripción textual:* el detector de fase compara la señal con el NCO; el filtro proporcional-integral corrige el NCO; el ancho de lazo fija el error medio por la rampa y el jitter por ruido.
- 🎯 **Por qué importa:** Un lazo demasiado ancho deja pasar ruido; uno demasiado estrecho pierde el Doppler. Ajustarlo es el equilibrio central de la sincronización y condiciona la recepción de señales débiles (C24).
- 🔗 **Se estudia junto con:** lazo de enganche de fase (PLL), segundo orden, ancho de banda de lazo, frecuencia natural.

📘 **Dónde se aprende** (1 clase): [B89-C10 · Sincronización de portadora](../programa/clases/B89/B89-C10-sincronizacion-de-portadora/CLASE.md).

### JPL

- CDMS (Cologne Database for Molecular Spectroscopy) y JPL son catálogos de líneas milimétricas y submilimétricas.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- LAMDA da las energías de los niveles; la diferencia entre dos niveles debería reproducir la frecuencia de JPL.
- Las frecuencias de transición que LAMDA lista aparte (`230,5380000` y `345,7959899 GHz`) sí coinciden con JPL: la discrepancia está en la precisión de las energías de nivel, no en las frecuencias de línea.
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.
- 🔗 **Se estudia junto con:** banco de datos espectroscópicos, CDMS, HITRAN, LAMDA.

📘 **Dónde se aprende** (1 clase): [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### JSON

- JSON es un formato de texto para intercambiar datos entre lenguajes; sus valores son objeto, arreglo, número, texto, `true`, `false` y `null` (S2, S3).

💡 **Cómo se explica en la clase [B07-C16](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md):**
- Las claves son siempre texto: `json.dumps({1: "a"})` da `{"1": "a"}`, y al leerlo vuelve `{'1': 'a'}` (S2).
- `json.dumps(obj, indent=2, ensure_ascii=False)` da una escritura legible con tildes.
- ⚠️ **Error frecuente:** Esperar comentarios en JSON. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** Una simulación tiene decenas de parámetros. Si están enterrados en el código, cambiar uno obliga a editar el programa y es fácil olvidar con qué valores se obtuvo cada resultado.
- 🔗 **Se estudia junto con:** YAML, sangría, comentario, Serializar.

📘 **Dónde se aprende** (1 clase): [B07-C16 · Formatos JSON y YAML](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md).

### Júpiter caliente

- Un Júpiter caliente es un gigante muy cercano a su estrella.

💡 **Cómo se explica en la clase [B29-C11](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md):**
- Para el Júpiter caliente: `H = 285,86 km` a 1000 K, `428,78` a 1500 K, `571,71` a 2000 K (con `μ = 2,3`);
- La aproximación `2RNH/R_s²` es buena a `1 %` para el Júpiter caliente y a `0,3 %` para la Tierra.
- 🎯 **Por qué importa:** Los planetas inflados y calientes tienen señales de cientos de ppm; las Tierras alrededor de estrellas como el Sol, de ~1 ppm, que no se alcanzan. La decisión central: ¿qué señal produce una atmósfera dada y cuántos tránsitos hacen falta para verla?
- 🔗 **Se estudia junto con:** altura de escala, masa molecular media, señal de transmisión, anillo atmosférico.

📘 **Dónde se aprende** (1 clase): [B29-C11 · Atmósferas exoplanetarias](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md).

### Jurisdicción

- Una jurisdicción es un régimen aplicable.

💡 **Cómo se explica en la clase [B121-C05](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md):**
- Cumplir la envolvente equivale a cumplir todas las jurisdicciones (el laboratorio lo comprueba).
- R["Requisitos por jurisdicción"] --> M["Matriz requisito x jurisdicción"]
- ⚠️ **Error frecuente:** Tomar la jurisdicción hipotética como real. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Ninguna clase trata el análisis de cumplimiento. La decisión central: ¿cuál es el requisito más estricto de cada tipo, qué incumple el diseño y cuánto tardan los trámites?
- 🔗 **Se estudia junto con:** matriz de cumplimiento, envolvente, camino crítico, recomendación.

📘 **Dónde se aprende** (1 clase): [B121-C05 · Cumplimiento regulatorio en varias jurisdicciones](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md).

### Jurisdicción y control

- VI). Jurisdicción y control es la potestad del Estado de registro sobre el objeto y su personal (art.

💡 **Cómo se explica en la clase [B119-C01](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md):**
- VI); el Estado de registro mantiene jurisdicción y control (art.
- 🎯 **Por qué importa:** Casi todo el derecho espacial posterior (salvamento, responsabilidad, registro, Luna) desarrolla principios de este tratado, y ninguna otra clase del programa lo estudia como instrumento jurídico. La decisión central: ¿qué obligación del tratado se infringe en una misión dada y qué cambio mínimo la devuelve a la conformidad?
- 🔗 **Se estudia junto con:** Estado parte, autorización y supervisión continua, Apropiación nacional, regla comprobable.

📘 **Dónde se aprende** (1 clase): [B119-C01 · Tratado del Espacio Ultraterrestre](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md).

### Justicia

- El informe Belmont nombra tres principios: respeto por las personas (autonomía y protección de quienes tienen autonomía disminuida), beneficencia (no dañar y maximizar beneficios) y justicia (reparto equitativo de cargas y beneficios).

💡 **Cómo se explica en la clase [B105-C19](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md):**
- Un resumen de búsqueda web (2026-11-10) del informe Belmont indica tres principios: respeto por las personas (voluntariedad e información adecuada; protección de quienes tienen autonomía disminuida), beneficencia (no dañar y maximizar beneficios minimizando daños) y justicia (quién carga con los riesgos y quién recibe los beneficios).
- B["principios Belmont:<br/>respeto, beneficencia,<br/>justicia"] --> D["decisiones del estudio"]
- 🎯 **Por qué importa:** No basta con quitar el nombre: con edad, sexo, profesión y misión, una persona de una cohorte de 6 suele ser única. La decisión central: ¿qué se puede publicar de una cohorte pequeña sin identificar a nadie y cuánta utilidad se pierde al protegerla?
- 🔗 **Se estudia junto con:** informe Belmont, respeto por las personas, beneficencia, cuasi-identificador.

📘 **Dónde se aprende** (1 clase): [B105-C19 · Bioética en investigación tripulada](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md).
