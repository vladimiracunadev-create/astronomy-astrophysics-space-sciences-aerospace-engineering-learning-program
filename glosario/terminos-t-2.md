# Términos · T (parte 2 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · **T** · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-t.md) · **2**

### Transformada de Fourier continua

- La transformada de Fourier continua de una función `f(t)` es, con la convención de S1 (DLMF §1.14), `F(x) = (1/√(2π)) ∫ f(t) e^{ixt} dt`; otras referencias usan el signo contrario en el exponente.

🎯 **Por qué importa (clase B15-C04):** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.

📘 **Dónde se aprende** (1 clase): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md).

### Transformada de Laplace

- La transformada de Laplace de una función `f(t)` definida para `t ≥ 0` es `F(s) = ∫₀^∞ e^(−st) f(t) dt` (S1, ec. 1.14.17), con `s` un número complejo cuya parte real es suficientemente grande para que la integral converja; sus unidades son s⁻¹.

💡 **Cómo se explica en la clase [B16-C05](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md):**
- El límite de la analogía: la transformada de Laplace es una herramienta para sistemas LTI con condiciones iniciales nulas; una saturación o una condición inicial no nula no se resumen con un solo cociente.
- 🎯 **Por qué importa:** Un ingeniero que diseña el control de actitud de un telescopio revisa decenas de variantes de ganancias.

📘 **Dónde se aprende** (1 clase): [B16-C05 · Funciones de transferencia](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md).

### Transformada discreta

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B33-C06):** El campo eléctrico depende de la conductividad y de la frecuencia. La decisión central: ¿cuánto vale el campo geoeléctrico y la corriente en una línea para un campo magnético dado?

📘 **Dónde se aprende** (1 clase): [B33-C06 · Corrientes geomagnéticas inducidas (GIC)](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md).

### Transformada discreta de Fourier

- La transformada discreta de Fourier (DFT) da los coeficientes `f̂_k`; la transformada rápida (FFT) la calcula con `O(N log N)` operaciones.

🎯 **Por qué importa (clase B11-C16):** Cuando la solución es suave y periódica —una señal a lo largo de una órbita, un perfil de temperatura alrededor de un vehículo que gira, el campo en una caja periódica—, un método espectral logra con 24 puntos lo que unas diferencias finitas lograrían con millones.

📘 **Dónde se aprende** (1 clase): [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md).

### Transformada discreta de Fourier (DFT)

- La transformada discreta de Fourier (DFT) de `N` muestras es `X[k] = Σ_{n=0}^{N−1} x[n] e^{−2π i k n/N}`, para `k = 0, …, N − 1`; es la convención usada en NumPy y en esta clase.

🎯 **Por qué importa (clase B15-C04):** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.

📘 **Dónde se aprende** (1 clase): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md).

### Transformada inversa

- La transformada inversa genera una muestra aplicando la inversa de la acumulada a números uniformes.

🎯 **Por qué importa (clase B52-C13):** Cómo se reparte la masa entre tamaños indica qué cuerpos dominan una población y qué mide un censo incompleto. La decisión central: ¿cómo se estima el exponente de una ley de potencias y qué tan fiable es la masa que implica?

📘 **Dónde se aprende** (1 clase): [B52-C13 · Pequeños cuerpos remanentes](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md).

### Transformada rápida

- La transformada discreta de Fourier (DFT) da los coeficientes `f̂_k`; la transformada rápida (FFT) la calcula con `O(N log N)` operaciones.

🎯 **Por qué importa (clase B11-C16):** Cuando la solución es suave y periódica —una señal a lo largo de una órbita, un perfil de temperatura alrededor de un vehículo que gira, el campo en una caja periódica—, un método espectral logra con 24 puntos lo que unas diferencias finitas lograrían con millones.

📘 **Dónde se aprende** (1 clase): [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md).

### Transformada unscented

- La transformada unscented aproxima la distribución con `2n+1` puntos sigma y los pesos `w_m`, `w_c`.
- La transformada unscented propaga `2n+1` puntos.

🎯 **Por qué importa (clase B74-C10):** Un filtro puede dar una estimación aceptable y una covarianza falsa. La decisión central: ¿cuándo basta el EKF y cuándo la covarianza obliga a usar un filtro no lineal, y cómo lo verifico con una referencia?

📘 **Dónde se aprende** (2 clases): [B74-C10 · Filtro de Kalman no lineal](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md); [B74-C12 · Propagación de incertidumbre — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Transición

- Una transición es el salto de un electrón entre dos niveles.
- La transición es el paso de laminar a turbulento, convencionalmente en `Re_x ≈ 5 × 10⁵` en placa y `Re ≈ 2300` en tubo.
- Una transición es un cambio de modo.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Con `h c = 1239,84 eV·nm` (que sale de las constantes exactas del SI, S1), una transición de 1,89 eV corresponde a `λ = 1239,84/1,89 ≈ 656 nm`, justamente la línea H-alfa.
- Dato de partida: la transición 3→2 del hidrógeno, con constantes CODATA 2022 (S1).
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.

📘 **Dónde se aprende** (6 clases): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B46-C12 · Emisiones moleculares](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md); [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md); [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md); [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md); [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md).

### Transición simple–compleja

- La transición simple–compleja es el diámetro `D_sc` en que cambia la forma.

🎯 **Por qué importa (clase B61-C03):** Sin la transición simple–compleja no se puede interpretar la forma de un cráter grande ni comparar cuerpos. La decisión central: ¿a qué diámetro cambia la morfología y cómo depende de la gravedad?

📘 **Dónde se aprende** (1 clase): [B61-C03 · Cráteres complejos: colapso, picos centrales y terrazas](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md).

### Tránsito

- El ángulo horario `H` es el ángulo, medido hacia el oeste, entre el meridiano y el círculo que pasa por el astro y los polos; vale cero cuando el astro cruza el meridiano (tránsito o culminación, S2).
- El tránsito es la disminución de brillo cuando un cuerpo pasa por delante de su estrella; su profundidad es la fracción de flujo que se pierde.
- El tránsito es el paso de un planeta frente a su estrella.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C04](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md):**
- Un barrido minuto a minuto del programa (interpolando linealmente la tabla S1 entre filas de 2 h; ±5 min) da: salida a las 22:26 UT, tránsito a las 03:57 UT y puesta a las 09:26 UT.
- El intervalo salida–tránsito (5,5 h) supera las 5,3 h porque la Luna avanza hacia el este entre las estrellas (≈ 0,6° por hora) y su ángulo horario crece algo más despacio que el del cielo.
- 🎯 **Por qué importa:** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».

📖 **Explicado a fondo:** [Tránsito](esencial/esencial-m-z.md#tránsito) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md); [B48-C04 · Planificación por visibilidad](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md); [B56-C14 · Biofirmas espectrales](../programa/clases/B56/B56-C14-biofirmas-espectrales/CLASE.md); [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Transitoria

- La transitoria es el tiempo que tarda la velocidad en llegar al equilibrio.

💡 **Cómo se explica en la clase [B102-C07](../programa/clases/B102/B102-C07-simulacion-de-movilidad-sobre-pendientes-y-terreno/CLASE.md):**
- Descripción larga: el patinaje crece rápido cerca de la pendiente máxima, que no depende de `g`; la gravedad solo cambia la rapidez de la transitoria.
- 🎯 **Por qué importa:** Un rover no sube cualquier pendiente aunque no vuelque. La decisión central: ¿a qué pendiente se agota la tracción, cuánto patina antes y cuánto tarda una ruta con tramos de distinta inclinación?

📘 **Dónde se aprende** (1 clase): [B102-C07 · Simulación de movilidad sobre pendientes y terreno](../programa/clases/B102/B102-C07-simulacion-de-movilidad-sobre-pendientes-y-terreno/CLASE.md).

### Transitorio

- Un transitorio es una fuente de brillo variable en escala corta.

🎯 **Por qué importa (clase B28-C08):** Un transitorio que dura menos que el intervalo entre visitas se pierde. El índice de caída decide cuánto dura un evento sobre el límite de detección.

📘 **Dónde se aprende** (1 clase): [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md).

### Transmisibilidad

- La transmisibilidad es `T = √((1 + (2ζr)²)/((1 − r²)² + (2ζr)²))` con `r = f/f_n`.
- Factor `Q`: amplificación en resonancia. Transmisibilidad: cociente respuesta/entrada en función de la frecuencia.

💡 **Cómo se explica en la clase [B47-C11](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md):**
- Con una frecuencia natural de `10 Hz` (ilustrativa) y `ζ = 0,05`, la transmisibilidad es `10,05` en la resonancia, `1` en `r = √2` y `0,0143` en `r = 10`; con `ζ = 0,5` esas cifras son `1,414`, `1` y `0,1010`.
- 🎯 **Por qué importa:** Un aislador mal sintonizado amplifica en vez de atenuar. La decisión central: ¿qué frecuencia natural y qué amortiguamiento aíslan sin amplificar demasiado en la resonancia?

📘 **Dónde se aprende** (3 clases): [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B84-C11 · Vibraciones y resonancias](../programa/clases/B84/B84-C11-vibraciones-y-resonancias/CLASE.md); [B90-C09 · Ensayos de vibración](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md).

### Transmisión

- La transmisión `T = e^{−τ/μ}` con `μ = cos χ` es la fracción que atraviesa.
- La transmisión `T(λ)`.
- La transmisión `e^(−τ)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B45-C03](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md):**
- Una transmisión residual de `10⁻³` sobre 700 nm aumenta el flujo medido un `0,794 %` para 3000 K y un `0,1123 %` para 10 000 K.
- 🎯 **Por qué importa:** Una banda se describe por su curva completa, no por dos números. La decisión central: ¿cómo se combinan las curvas y qué longitud de onda se asigna a una banda?

📘 **Dónde se aprende** (4 clases): [B45-C03 · Curvas de transmisión](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md); [B45-C11 · Líneas de absorción](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md); [B47-C01 · Ventajas de observación fuera de atmósfera](../programa/clases/B47/B47-C01-ventajas-de-observacion-fuera-de-atmosfera/CLASE.md); [B54-C12 · Interacción con radiación solar](../programa/clases/B54/B54-C12-interaccion-con-radiacion-solar/CLASE.md).

### Transmisión de poro

- La transmisión de poro `W = 1/(1 + 3d/(8 r_p))` es la fracción de moléculas que, saliendo del hielo, atraviesan una capa de espesor `d` con poros de radio `r_p`.

🎯 **Por qué importa (clase B67-C06):** Una oscilación de temperatura de pocos kelvin cambia la pérdida en órdenes de magnitud, y esa oscilación decae con la profundidad. La decisión central: ¿a qué profundidad el hielo es estable, y cuánto engaña usar la temperatura media?

📘 **Dónde se aprende** (1 clase): [B67-C06 · Pérdida de volátiles por sublimación y migración térmica](../programa/clases/B67/B67-C06-perdida-de-volatiles-por-sublimacion-y-migracion-termica/CLASE.md).

### Transmitancia

- La reflectancia `R` y la transmitancia `T`.
- La transmitancia `t(x)`.

🎯 **Por qué importa (clase B41-C02):** Un telescopio refractor y los recubrimientos dependen de cuánta luz se refleja y a qué ángulo se dobla. La decisión central: ¿qué fracción de luz se pierde por reflexión y cuándo hay reflexión total?

📘 **Dónde se aprende** (2 clases): [B41-C02 · Índice de refracción y ley de Snell](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md); [B42-C04 · Difracción de aperturas](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md).

### Transmitancia total

- La transmitancia total `T_d T_u` es la fracción que baja y sube.

💡 **Cómo se explica en la clase [B57-C26](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md):**
- La transmitancia total del rojo es `T_d T_u = 0,4704` y la reflectancia de trayectoria `0,01920`: la neblina atmosférica aporta casi la mitad de la señal de una superficie oscura.
- 🎯 **Por qué importa:** Comparar imágenes de fechas distintas con atmósferas distintas confunde atmósfera con cambio. La decisión central: ¿cuánto sesga la atmósfera y cómo se estima y descuenta con la información disponible?

📘 **Dónde se aprende** (1 clase): [B57-C26 · Corrección atmosférica de imágenes](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md).

### Transparencia

- La transparencia es la fracción de luz que llega.
- La transparencia es informar con apertura y a tiempo.
- La transparencia es la apertura de información.

💡 **Cómo se explica en la clase [B45-C17](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md):**
- La variación de la transparencia fuera de tránsito es `3,410 %` RMS.
- Límite: transparencia igual para todas las estrellas.
- 🎯 **Por qué importa:** La atmósfera varía más que la señal; sin una referencia, la curva de luz no sirve. La decisión central: ¿qué comparaciones y qué precisión se necesitan para una profundidad dada?

📘 **Dónde se aprende** (3 clases): [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md); [B56-C19 · Ética del descubrimiento de vida](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md); [B119-C18 · Ética y derechos en actividades espaciales](../programa/clases/B119/B119-C18-etica-y-derechos-en-actividades-espaciales/CLASE.md).

### Transpuesta

- La transpuesta `Aᵀ` intercambia filas y columnas.

🎯 **Por qué importa (clase B10-C03):** Una estación terrestre está fija respecto de la Tierra, pero la Tierra gira respecto del espacio inercial. Para saber dónde está la estación en el sistema inercial a cada instante hay que aplicar una transformación que depende del tiempo.

📘 **Dónde se aprende** (1 clase): [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md).

### Transversal

- La velocidad radial es `μ e sin ν/h` y la transversal `h/r`.
- La componente de línea de visión y la transversal son las incertidumbres a lo largo de la dirección de la nave y perpendicular a ella.
- En una onda transversal, el medio se mueve perpendicular a la propagación (cuerda); en una longitudinal, paralelo (sonido).

💡 **Cómo se explica en la clase [B74-C15](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md):**
- Para una nave a `ρ` y estaciones separadas `B`, la incertidumbre transversal es del orden `σρ/B`: `85,5 m` para la red amplia y `1096,6 m` para la agrupada.
- *Descripción textual:* las posiciones de estaciones y nave definen las líneas de visión, de ellas sale la matriz de información, su inversa da la covarianza y el DOP; la línea de base domina la componente transversal.
- 🎯 **Por qué importa:** La precisión de seguimiento no se compra solo con mejores receptores. La decisión central: ¿qué configuración de estaciones y qué observables dan información en las tres direcciones, y cuánto vale la línea de base?

📘 **Dónde se aprende** (3 clases): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B71-C17 · Movimientos en planos orbitales](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md); [B74-C15 · Geometría de la red de seguimiento](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md).

### Trapezoidal

- BDF2 (fórmula de diferenciación hacia atrás de orden 2): `y_{n+1} = (4 y_n − y_{n−1})/3 + (2h/3) f(t_{n+1}, y_{n+1})`. Trapezoidal: `y_{n+1} = y_n + (h/2)[f(t_n, y_n) + f(t_{n+1}, y_{n+1})]`.
- El perfil triangular acelera y frena sin crucero; el trapezoidal incluye un tramo a velocidad máxima.

💡 **Cómo se explica en la clase [B11-C22](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md):**
- BDF2 `1,6 × 10⁻⁸ … 2,5 × 10⁻¹⁰`, órdenes `2,00`; trapezoidal `4,0 × 10⁻⁹ … 6,3 × 10⁻¹¹`, órdenes `2,00`.
- Euler implícito (`2,7 × 10⁻⁷` en `t = 2`), igual; el trapezoidal conserva una oscilación de `0,157` que no se apaga, porque su factor de amplificación tiende a `−1`, no a 0 (por ejemplo, con `z = −100`, `(1 − 50)/(1 + 50) = −0,96`).
- ⚠️ **Error frecuente:** Elegir el trapezoidal con transitorios. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Los modelos térmicos, de combustión, de propulsión y de química atmosférica mezclan escalas de microsegundos con horas. Un integrador explícito pagaría el paso del más rápido durante toda la simulación.

📘 **Dónde se aprende** (2 clases): [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md); [B87-C11 · Ruedas de reacción](../programa/clases/B87/B87-C11-ruedas-de-reaccion/CLASE.md).

### Traspuesta

- La inversa de una rotación es su traspuesta: `R⁻¹ = Rᵀ`.

💡 **Cómo se explica en la clase [B04-C15](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md):**
- Girar los ejes `+0,5 rad` alrededor de `x` equivale a girar el punto `−0,5 rad`; la matriz de la segunda es la traspuesta de la primera.
- *Descripción textual:* de las componentes ecuatoriales se pasa a las eclípticas con la rotación pasiva `R_x(ε)`; la traspuesta devuelve las ecuatoriales; de las eclípticas salen longitud y latitud con `atan2` y `arcsen`; y la matriz se comprueba con ortogonalidad y determinante 1.
- 🎯 **Por qué importa:** El ecuador de la Tierra y el plano de su órbita (la eclíptica) forman un ángulo de unos 23,4°. Los catálogos de estrellas se dan en coordenadas ecuatoriales; el movimiento del Sol, la Luna y los planetas es más simple en coordenadas eclípticas.

📘 **Dónde se aprende** (1 clase): [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md).

### Tratado del Espacio Ultraterrestre

- El Tratado del Espacio Ultraterrestre (1967) establece principios para la actividad de los estados en el espacio (S5).

🎯 **Por qué importa (clase B02-C19):** La exploración espacial es una historia científica y también política. La pregunta motivadora es: ¿qué cambió, para la astronomía y para la sociedad, cuando los instrumentos y las personas empezaron a salir de la atmósfera, y qué reglas se acordaron?

📘 **Dónde se aprende** (1 clase): [B02-C19 · Historia de la exploración espacial](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md).

### Traversabilidad

- La traversabilidad es la capacidad de un vehículo de cruzar una celda.

🎯 **Por qué importa (clase B103-C04):** El ruido del MDE crece con el cuadrado del rango y, a partir de cierta distancia, la señal de un obstáculo queda por debajo del ruido. La decisión central: ¿hasta qué rango se puede clasificar el terreno de forma útil, y qué política (conservadora o corregida) elegir más allá?

📘 **Dónde se aprende** (1 clase): [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Traversable

- Rugosidad: dispersión de la altura respecto de un plano local. Traversable: celda que cumple los umbrales de pendiente y rugosidad.

💡 **Cómo se explica en la clase [B99-C05](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md):**
- Con umbrales de 15° y 5 cm (sintéticos) se declara traversable 96 % del interior; la roca (pendiente máxima 22,9°) queda no traversable en 8 de sus 12 celdas, por pendiente y no por rugosidad (rugosidad máxima 4,9 cm).
- 🎯 **Por qué importa:** Un mapa útil para navegar distingue lo ocupado, lo libre y lo que no se sabe, y dice si el terreno es pisable. La decisión central: ¿cómo fusionar medidas ruidosas en cada celda y qué umbrales de pendiente y rugosidad declaran un terreno traversable?

📘 **Dónde se aprende** (1 clase): [B99-C05 · Mapas de ocupación y rejillas de elevación](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md).

### Trayectorias vecinas

- Con trayectorias vecinas, se mide `d_n/d_0` y se renormaliza la separación.

💡 **Cómo se explica en la clase [B73-C14](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md):**
- Para `K = 5` el exponente medio es `0,9741` por iteración con el vector tangente y `0,9741` con trayectorias vecinas (`0,00%` de diferencia); la estimación `ln(K/2)` da `0,9163`.
- 🎯 **Por qué importa:** El exponente de Lyapunov es el número que cuantifica el caos: fija el horizonte de predicción y distingue una trayectoria regular de una caótica. En un espacio de fases mixto, un solo exponente no basta.

📘 **Dónde se aprende** (1 clase): [B73-C14 · Exponentes de Lyapunov](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md).

### Traza

- Una traza es una tabla que anota el valor de las variables después de cada paso.
- La traza es la suma de la diagonal.
- La traza es la contracción `Tᵢᵢ` (S1: suma de la diagonal, §1.2(vi), ec. 1.2.62).
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C01](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md):**
- La traza para los datos de la sección 5 empieza con «mejor = Mercurio, 87,969».
- Una traza te permite descubrir errores de lógica sin que el computador intervenga.
- 🎯 **Por qué importa:** En astronomía casi todo resultado pasa por un procedimiento repetible: reducir imágenes, ajustar una órbita, buscar el máximo de una curva de luz. Si no puedes describir el procedimiento con precisión, no puedes ejecutarlo en un computador ni dárselo a otra persona para que lo repita.

📘 **Dónde se aprende** (9 clases): [B07-C01 · Pensamiento algorítmico](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md); [B07-C12 · Manejo de errores y excepciones](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md); [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md); [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md); [B106-C21 · Depuración de trazas gaseosas de la atmósfera de cabina](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md) y 3 más.

### Traza al suelo

- La traza al suelo es el recorrido de la proyección de la nave sobre la superficie.

🎯 **Por qué importa (clase B75-C17):** Cada metro de altitud cuesta resolución, y cada segundo de ventana cuesta datos. La decisión central: ¿qué altitud de máxima aproximación equilibra resolución, cobertura y volumen de datos en un sobrevuelo?

📘 **Dónde se aprende** (1 clase): [B75-C17 · Oportunidades científicas de sobrevuelo](../programa/clases/B75/B75-C17-oportunidades-cientificas-de-sobrevuelo/CLASE.md).

### Traza repetida

- La traza repetida `N/D` significa `N` órbitas en `D` días.

💡 **Cómo se explica en la clase [B57-C23](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md):**
- Si Landsat 8 repitiera 233 órbitas en 16 días (esta cifra no se consultó; es una hipótesis de la clase), la altitud de traza repetida sería `699,6 km` y el espaciado `172,0 km`, menor que el barrido de 185 km.
- 🎯 **Por qué importa:** Si la órbita no repite sus trazas o el barrido no cubre el espacio entre ellas, quedan huecos. La decisión central: ¿qué altitud e inclinación dan un ciclo de repetición que cubre todo con el barrido disponible?

📘 **Dónde se aprende** (1 clase): [B57-C23 · Diseño de órbita y revisita para observación terrestre](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md).

### Trazabilidad

- La trazabilidad es la capacidad de seguir una afirmación hasta su origen.
- La trazabilidad es poder seguir cada requisito hasta su comprobación.
- La trazabilidad es la capacidad de reconstruir, para una cifra, los datos, el código, los parámetros y el entorno que la produjeron.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C19](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md):**
- Lo que decide es la trazabilidad, no el peldaño.
- 🎯 **Por qué importa:** Un titular dice: «Neutrinos superan la velocidad de la luz: Einstein estaba equivocado». Es una afirmación fuerte.

📘 **Dónde se aprende** (10 clases): [B01-C19 · Fuentes confiables y desinformación espacial](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md); [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md); [B90-C18 · Trazabilidad de evidencias](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md); [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md) y 4 más.

### Trazabilidad documentada

- La trazabilidad documentada exige que cada calibración deje constancia (S2, 2.41).

🎯 **Por qué importa (clase B13-C19):** Dentro de un año alguien usará los datos de un fotodiodo calibrado hoy. Necesitará saber con qué patrones, a qué temperatura, con qué incertidumbre y hasta cuándo es válida la calibración.

📘 **Dónde se aprende** (1 clase): [B13-C19 · Metadatos y registros de calibración](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md).

### Trazabilidad metrológica

- La trazabilidad metrológica es la propiedad de un resultado de medida por la cual puede relacionarse con una referencia mediante una cadena ininterrumpida y documentada de calibraciones, cada una de las cuales contribuye a la incertidumbre (S2, 2.41).

🎯 **Por qué importa (clase B13-C02):** Un satélite recibe un comando con un tiempo de encendido de motor; el ingeniero de tierra usó una fórmula del periodo orbital copiada de una hoja de cálculo. Si la fórmula está mal dimensionada, el resultado sale en «segundos al cuadrado» o en «metros por segundo» sin que nadie lo note.

📘 **Dónde se aprende** (1 clase): [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md).

### Trazable

- Una cifra trazable puede rastrearse hasta sus entradas.

🎯 **Por qué importa (clase B126-C06):** [B124-C19](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) redacta propuestas de misión, no financieras. La decisión central: ¿qué cifra se muestra, con qué rótulo y con qué rango, de modo que un tercero pueda comprobarla?

📘 **Dónde se aprende** (1 clase): [B126-C06 · Presentación financiera ante inversionistas con evidencia](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md).

### Trazado exacto

- El trazado exacto resuelve la intersección rayo–superficie sin aproximar.

🎯 **Por qué importa (clase B41-C08):** Los programas de diseño óptico trazan rayos exactos. La decisión central: ¿cuándo se separa el rayo real del paraxial y cómo crece esa diferencia?

📘 **Dónde se aprende** (2 clases): [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md); [B50-C01 · Trazado exacto de rayos y aberraciones de orden superior](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md).

### Trazado óptimo

- Un trazado óptimo es el de menor coste.

💡 **Cómo se explica en la clase [B109-C02](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md):**
- El trazado óptimo deja Dormitorios junto a Higiene y Cocina-mesa, y la Esclusa en la esquina opuesta.
- 🎯 **Por qué importa:** Un buen plano ahorra pasos, separa lo sucio de lo limpio y deja las zonas tranquilas lejos de las ruidosas. La decisión central: ¿dónde pongo cada zona para que los recorridos frecuentes sean cortos y las zonas incompatibles estén lejos?

📘 **Dónde se aprende** (1 clase): [B109-C02 · Zonificación y distribución funcional de módulos de un hábitat](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md).

### Trazador

- Un trazador es una especie fácil de observar que sirve para inferir otra difícil de ver.

💡 **Cómo se explica en la clase [B25-C04](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md):**
- El `H₂` carece de emisión útil a 10 K, y el `CO` es el trazador más usado.
- Piensa en una nube de humo en una habitación: no ves el gas, ves cómo oscurece una lámpara detrás (sombra) o cómo brilla un trazador que añadiste (CO).
- 🎯 **Por qué importa:** El hidrógeno molecular `H₂`, el componente principal de las nubes donde nacen las estrellas, casi no emite en el gas frío. Por eso la masa de una nube se estima con un trazador indirecto, el monóxido de carbono `CO`, y con el polvo que apaga la luz de fondo.

📘 **Dónde se aprende** (1 clase): [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md).

### TRIAD

- El problema de Wahba minimiza `Σ wᵢ |bᵢ − A rᵢ|²` sobre matrices de rotación `A`. TRIAD construye dos ternas ortonormales con dos estrellas.
- El método q halla el autovector de mayor autovalor de la matriz `K` de Davenport. TRIAD construye ternas ortonormales con dos vectores.

💡 **Cómo se explica en la clase [B74-C14](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md):**
- Con dos vectores medidos `b₁, b₂` y sus catálogos `r₁, r₂`, TRIAD toma `b₁` como eje principal y construye la terna con `b₁ × b₂`.
- Con solo dos estrellas, las desviaciones son de `10,1″` (TRIAD) y `12,0″` (SVD), dominadas por pares casi colineales (colas pesadas).
- 🎯 **Por qué importa:** Un error de actitud de unos segundos de arco desplaza a un objeto a un millón de kilómetros por decenas de metros, y un error de giro mayor en el eje óptico es normal. La decisión central: ¿cuántas estrellas y qué campo de visión hacen falta para cada eje de la actitud?

📘 **Dónde se aprende** (2 clases): [B74-C14 · Navegación con cámaras estelares](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md); [B87-C09 · Estimación de actitud](../programa/clases/B87/B87-C09-estimacion-de-actitud/CLASE.md).

### Triage

- Triage es la clasificación de casos por urgencia para decidir el orden y el tipo de atención.

💡 **Cómo se explica en la clase [B116-C04](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md):**
- Sensibilidad `(1132 + 1240 + 1013)/3978 = 0,851`; especificidad `15822/16022 = 0,988`; sub-triage `593/20000 = 2,96 %`.
- El ruido del sensor produce sobre-triage de personas estables, con el coste de alertas y consultas, más que sub-triage.
- 🎯 **Por qué importa:** Un puntaje simple ayuda a decidir rápido y de forma homogénea, pero un fallo por defecto (sub-triage) deja sin atender a quien lo necesita y uno por exceso (sobre-triage) agota recursos y atención. Y si la respuesta de tierra tarda decenas de minutos, no se puede esperar a tierra para lo que no admite espera.

📘 **Dónde se aprende** (1 clase): [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Trial

- El trial es un valor de prueba de DM.

🎯 **Por qué importa (clase B29-C17):** La medida de dispersión informa de la distancia a la fuente y de la materia que atravesó. Sin desdispersión, un pulso breve se pierde entre canales.

📘 **Dónde se aprende** (1 clase): [B29-C17 · Fenómenos transitorios rápidos](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md).

### Triangulación

- La triangulación es la medición de la distancia a un objeto a partir de una base conocida y de los ángulos que forman con ella las visuales desde sus extremos.

💡 **Cómo se explica en la clase [B04-C20](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md):**
- Un plan de triangulación fija: el objeto y su distancia esperada, la base disponible, la precisión angular del instrumento, el error relativo exigido, la base necesaria, la comprobación (simulación o caso conocido), los supuestos (plano, sin error de base, ruido gaussiano) y las fuentes de cada cifra.
- Paso 2 · Comprobar la triangulación. `h = B/(cot A + cot B') = 6000/(2 × 0,007805) = 384 400 km` ✓ (`cot 89,553° = 0,007805`).
- 🎯 **Por qué importa:** Las distancias a las estrellas más cercanas se obtienen con un triángulo (el paralaje de C07): la base es la órbita de la Tierra y el ángulo es lo que cambia la dirección de la estrella.

📘 **Dónde se aprende** (1 clase): [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md).

### Triangular

- Una duración triangular tiene mínimo, moda y máximo.

🎯 **Por qué importa (clase B124-C16):** Un plazo prometido sin ruta crítica ni incertidumbre es una apuesta. La decisión central: ¿qué actividades controlan el plazo y con qué probabilidad se cumple?

📘 **Dónde se aprende** (1 clase): [B124-C16 · Planificación de cronograma y entregables](../programa/clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md).

### Triangulares

- Los colineales L1, L2, L3 están sobre el eje que une los primarios; los triangulares L4 y L5 forman con ellos un triángulo equilátero.

🎯 **Por qué importa (clase B73-C03):** Los puntos de Lagrange son donde se estacionan observatorios y donde se acumulan asteroides troyanos. Un error de signo en la ecuación mueve L2 al otro lado.

📘 **Dónde se aprende** (1 clase): [B73-C03 · Puntos de equilibrio de Lagrange](../programa/clases/B73/B73-C03-puntos-de-equilibrio-de-lagrange/CLASE.md).

### Triángulo esférico

- Un triángulo esférico está formado por tres arcos de círculo máximo.

🎯 **Por qué importa (clase B04-C16):** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.

📘 **Dónde se aprende** (1 clase): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md).

### Triángulo rectángulo

- En un triángulo rectángulo, el cateto opuesto a un ángulo `θ` es el lado frente a él, el cateto adyacente es el lado que lo forma junto con la hipotenusa, y la hipotenusa es el lado mayor, frente al ángulo recto.
- Un triángulo rectángulo tiene un ángulo de 90°; el lado opuesto a él es la hipotenusa y los otros dos son los catetos.

💡 **Cómo se explica en la clase [B03-C18](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md):**
- Visto desde una distancia `d`, el radio `r` forma un triángulo rectángulo con la visual tangente: `tan(θ/2) = r/d`, luego `θ = 2·atan(r/d)`.
- 🎯 **Por qué importa:** El Sol y la Luna se ven en el cielo con tamaños angulares muy parecidos, de alrededor de medio grado. ¿Es casualidad que midan lo mismo en el cielo siendo tan distintos?

📘 **Dónde se aprende** (2 clases): [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md); [B04-C07 · Triángulos y distancias angulares](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md).

### Tridiagonal

- Un sistema tridiagonal solo tiene tres diagonales distintas de cero y se resuelve con el algoritmo de Thomas (eliminación sin pivoteo, `O(N)`).

💡 **Cómo se explica en la clase [B11-C12](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md):**
- C --> D["Sistema tridiagonal<br/>(Thomas)"]
- *Descripción textual:* un BVP se resuelve de dos maneras: con diferencias finitas se plantea una ecuación en cada nodo y se resuelve un sistema tridiagonal; con tiro se prueba una condición inicial, se integra y se corrige según el desvío en el extremo hasta que se anule.
- 🎯 **Por qué importa:** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Trigonal plana

- Las formas básicas son lineal (2 dominios, 180°), trigonal plana (3, 120°) y tetraédrica (4, 109,47°).

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- Con 3 sin pares solitarios, trigonal plana (120°).
- D2["2 dominios: lineal, 180°"] --> D3["3 dominios: trigonal plana, 120°"]
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### TRIMP

- El rendimiento es aptitud menos fatiga. TRIMP es una carga basada en frecuencia cardiaca.

🎯 **Por qué importa (clase B104-C04):** Entrenar más no siempre significa rendir más el día que importa. La decisión central: ¿cómo distribuir una misma carga total para llegar con la mejor combinación de aptitud y fatiga?

📘 **Dónde se aprende** (1 clase): [B104-C04 · Acondicionamiento físico general](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md).

### Triple alfa

- El triple alfa es la fusión `3 ⁴He → ¹²C`, con ayuda del berilio-8 inestable como paso intermedio.

💡 **Cómo se explica en la clase [B24-C08](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md):**
- La energía por kilogramo del triple alfa es `ε c² = 5,85 × 10¹³ J/kg`, frente a `6,40 × 10¹⁴` del hidrógeno.
- Cinética con una ecuación (triple alfa): da la forma de la caída de abundancia.
- ⚠️ **Error frecuente:** Olvidar que el triple alfa es de tres cuerpos. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** El carbono de tu cuerpo, el oxígeno que respiras y el hierro de tus huesos se forjaron en estrellas. Entender cómo, y cuánta energía rinde cada etapa, explica por qué la vida de una estrella se acorta con cada combustible y por qué el hierro es el final de la cadena.

📘 **Dónde se aprende** (1 clase): [B24-C08 · Nucleosíntesis estelar](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md).

### Triplete

- El triplete (`s = 1`) y el singlete (`s = 0`).

💡 **Cómo se explica en la clase [B31-C05](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md):**
- S2["S = S₁ + S₂"] --> T["triplete s=1, singlete s=0"]
- *Descripción textual:* el ángulo da la probabilidad en un analizador; la suma de espines da triplete y singlete; el campo da el desdoblamiento Zeeman y su frecuencia.
- 🎯 **Por qué importa:** El espín explica los desdoblamientos de líneas espectrales y la estructura de la materia. La decisión central: ¿qué probabilidades y qué energías resultan de un espín en un campo?

📘 **Dónde se aprende** (1 clase): [B31-C05 · Espín y momento angular](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md).

### Triplete apocromático

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C15):** Un refractor sin color necesita combinar vidrios. La decisión central: ¿cuánto color queda con dos o tres vidrios?

📘 **Dónde se aprende** (1 clase): [B41-C15 · Refractores acromáticos y apocromáticos](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md).

### Trípode

- La estabilización de imagen o un trípode reducen el temblor.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- NASA recomienda, para empezar, entre 7×35 y 10×50: con más aumento el campo es más estrecho, pesan más y se sacuden, salvo con estabilización o trípode (S2, S3).
- Apoya los codos, o el cuerpo en un muro; a mayor aumento, el temblor se nota más, y NASA sugiere trípode para 10× o 15× en la Luna (S4).
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?

📘 **Dónde se aprende** (1 clase): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md).

### TRL

- El TRL es el nivel de 1 a 9 de madurez.
- Los TRL (S6): 1 principios básicos; 2 concepto; 3 prueba de concepto; 4 componentes probados; 5 maqueta en entorno relevante; 6 prototipo representativo; 7 prototipo en el espacio; 8 calificado para vuelo; 9 probado en misión.

💡 **Cómo se explica en la clase [B78-C19](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md):**
- El TRL es la longitud de la cadena contigua de hitos desde el 1.
- Un sistema formado por A, B y C tiene componentes `[9, 7, 3]` y TRL `min = 3`; la media daría `6,33`.
- ⚠️ **Error frecuente:** Dar el TRL por el máximo con evidencia. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una tecnología con un buen desempeño en papel puede estar lejos de volar. La decisión central: ¿en qué nivel está una tecnología según la evidencia que tiene, y qué nivel tiene un sistema formado por componentes de madureces distintas?

📘 **Dónde se aprende** (2 clases): [B78-C19 · Madurez tecnológica TRL](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md); [B83-C18 · Niveles de madurez tecnológica](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md).

### TRL del sistema

- El TRL del sistema es el mínimo de sus elementos (S5).

💡 **Cómo se explica en la clase [B83-C18](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md):**
- El TRL del sistema es 4 (el del detector).
- 🎯 **Por qué importa:** Un elemento «con herencia de vuelo» que se usa en otro entorno no es TRL 9. La decisión central: ¿cuál es el TRL real del sistema, qué elementos lo frenan y cuánto cuesta llevarlos al nivel que pide la revisión?

📘 **Dónde se aprende** (1 clase): [B83-C18 · Niveles de madurez tecnológica](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md).

### Tropopausa

- La tropopausa es el techo de la capa donde `T` desciende con la altura.

💡 **Cómo se explica en la clase [B54-C01](../programa/clases/B54/B54-C01-estructura-vertical-de-atmosferas/CLASE.md):**
- La temperatura baja hasta `216,65 K` a 11 km (la tropopausa del modelo), sube con el gradiente positivo de las capas superiores hasta `270,65 K` a 47 km y vuelve a bajar.
- 🎯 **Por qué importa:** Todo lo que sigue en el bloque (balance de energía, convección, nubes, escape) ocurre en una columna de gas con una presión y una temperatura que dependen de la altura. La pregunta motivadora: ¿cómo cae la presión con la altura cuando la temperatura también cambia?

📘 **Dónde se aprende** (1 clase): [B54-C01 · Estructura vertical de atmósferas](../programa/clases/B54/B54-C01-estructura-vertical-de-atmosferas/CLASE.md).

### Trozo

- Un trozo (*chunk*) es una porción independiente de trabajo.
- SHA-256: hash de 256 bits. Trozo: unidad de transferencia.

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Con cuatro procesos no hubo ganancia. No es un fallo: en Windows el método de arranque es `spawn` (S1), cada trabajador es un intérprete nuevo que debe importar NumPy, y ese arranque cuesta una fracción de segundo por proceso, del orden del trabajo útil de cada trozo.
- Lo que hace al paralelismo reproducible: semilla por trozo (no una global compartida), reparto determinista de trozos y combinación en un orden fijo.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.

📘 **Dónde se aprende** (2 clases): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md); [B96-C22 · Transferencia de datos entre estación y centro de datos](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md).

### TRR

- La TRR revisa la preparación de cada ensayo.

💡 **Cómo se explica en la clase [B83-C14](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md):**
- La TRR de los ensayos requeridos no está lista hasta resolver E3 y E4.
- *Descripción textual:* cada requisito recibe un método; los de ensayo se asocian a un ensayo con su lista de preparación y su veredicto de TRR; si es de vibración, el perfil se integra para dar los niveles de carga.
- ⚠️ **Error frecuente:** Convocar la TRR sin la lista. Verifica las cinco condiciones
- 🎯 **Por qué importa:** Un ensayo mal preparado destruye hardware o no demuestra nada. La decisión central: ¿cada requisito tiene un método asignado, y cada ensayo está listo (procedimiento, equipo, configuración, personal e instalación) y con un nivel de carga definido?

📘 **Dónde se aprende** (1 clase): [B83-C14 · Revisiones CDR y TRR](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md).

### Truncada

- Una distribución es truncada si tiene tamaños mínimo y máximo.

🎯 **Por qué importa (clase B52-C13):** Cómo se reparte la masa entre tamaños indica qué cuerpos dominan una población y qué mide un censo incompleto. La decisión central: ¿cómo se estima el exponente de una ley de potencias y qué tan fiable es la masa que implica?

📘 **Dónde se aprende** (1 clase): [B52-C13 · Pequeños cuerpos remanentes](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md).

### Tubo

- El tubo sostiene el detector respecto del espejo.

💡 **Cómo se explica en la clase [B50-C12](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md):**
- Un espejo y un tubo del mismo material (homólogo) no se desenfocan.
- E["espejo α_m y tubo α_t"] --> D2["defocus = f ΔT (α_m − α_t)"]
- 🎯 **Por qué importa:** Un telescopio que se enfría de noche se desenfoca si sus materiales se dilatan distinto. La decisión central: ¿qué dilatación debe tener la estructura para que el foco no se mueva?

📘 **Dónde se aprende** (1 clase): [B50-C12 · Sensibilidad térmica del desempeño óptico y atermalización](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md).

### Tubo de flujo

- Un tubo de flujo es un haz de líneas de campo.

🎯 **Por qué importa (clase B30-C05):** Que el gas domine al campo en la fotosfera y el campo al gas en la corona explica por qué la corona se estructura en lazos y por qué las erupciones liberan energía magnética. La decisión central: ¿en qué capa manda el campo y cuánta energía guarda?

📘 **Dónde se aprende** (2 clases): [B30-C05 · Campos magnéticos solares](../programa/clases/B30/B30-C05-campos-magneticos-solares/CLASE.md); [B34-C03 · Bucles magnéticos coronales](../programa/clases/B34/B34-C03-bucles-magneticos-coronales/CLASE.md).

### Tubo delgado

- El tubo delgado `I = π r³ t`.

🎯 **Por qué importa (clase B43-C10):** Lo que decolima no es la flexión sino la flexión diferencial entre primario y secundario. La decisión central: ¿qué rigideces hacen que los dos extremos se muevan lo mismo, de modo que el eje óptico solo se desplace en paralelo?

📘 **Dónde se aprende** (1 clase): [B43-C10 · Estructura de tubo óptico](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md).

### Tubo testigo

- Un tubo testigo (*witness tube*) es un tubo que registra contaminación de la propia nave.

🎯 **Por qué importa (clase B63-C02):** Un rover tiene un número limitado de tubos. La decisión central: ¿cuántas muestras hacen falta para no perderse una litología rara con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B63-C02 · Muestreo superficial y estrategias de recolección](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md).

### Tupla

- Una tupla es una secuencia ordenada e inmutable, entre paréntesis (S3).

💡 **Cómo se explica en la clase [B07-C07](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md):**
- Una tupla `(nombre, valor)` no se puede modificar.
- Una tupla de un elemento necesita coma final: `(5,)` es tupla, `(5)` es el entero 5.
- 🎯 **Por qué importa:** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.

📘 **Dónde se aprende** (1 clase): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md).

### Turbulento

- El flujo es laminar si las capas no se mezclan y turbulento si hay mezcla caótica.

💡 **Cómo se explica en la clase [B79-C04](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md):**
- Con `Re_L = 2 × 10⁶` el `C_f` turbulento es `4,33` veces el laminar.
- El régimen turbulento tiene más fricción (en placa, `C_f` mayor y decae más despacio con `Re`) pero también retrasa el desprendimiento.
- ⚠️ **Error frecuente:** Usar `f = 64/Re` en régimen turbulento. Se corrige con 8.1.
- 🎯 **Por qué importa:** El régimen cambia el arrastre y la transferencia de calor por factores de varios; no distinguirlo lleva a subestimar el calentamiento de una pared o la pérdida de presión de un conducto. El tronco no lo trata.

📘 **Dónde se aprende** (1 clase): [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md).

### Turno

- Horas efectivas: jornada menos ausencias. Turno: bloque de 8 h.

💡 **Cómo se explica en la clase [B96-C03](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md):**
- Con 21 turnos semanales y 6 personas se asignan por turno y en rotación.
- 🎯 **Por qué importa:** Un rol vacío durante un contacto es un contacto perdido. La decisión central: ¿cuánto personal exige cubrir una posición 24/7 y cómo se comprueba que el cronograma no deja huecos?

📘 **Dónde se aprende** (1 clase): [B96-C03 · Roles de control de misión](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md).
