# Glosario esencial (ampliación) · N – Z

[⬅️ Índice del glosario esencial](README.md) · [Glosario completo](../README.md)

Continuación de la ampliación. Mismo esquema: **en una frase**, **cómo pensarlo**, **fórmula y unidades**, **ejemplo con números**, **error frecuente**, **relacionados**. Valores redondeados y orientativos.

---

### Navegación inercial

**En una frase.** Estimación de la posición y la velocidad integrando las aceleraciones y giros medidos a bordo, sin ayuda externa.

**Cómo pensarlo.** Acelerómetros y giróscopos miden el movimiento; integrando una vez se obtiene la velocidad y dos veces la posición. Funciona sin señal externa (útil en lanzamiento y reentrada), pero los errores se acumulan con el tiempo y se corrigen con otros sensores (estrellas, GPS, radar).

**Fórmula.** Error de posición por un sesgo de acelerómetro *b*: Δx = ½ b t².

**Ejemplo.** b = 10⁻³ m/s² (≈ 100 µg): tras 1 hora, Δx ≈ ½ · 10⁻³ · 3 600² ≈ **6,5 km**.

**Error frecuente.** Creer que un sensor inercial "no se equivoca" por ser interno: su deriva crece sin límite.

**Relacionados:** filtro de Kalman, giróscopo, fusión de sensores.
📘 [B80](../../programa/tronco-comun/B80-navegacion-inercial-y-fusion-multisensorial.md "Navegación inercial y fusión multisensorial"), [B74](../../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md "Estimación de órbitas y navegación espacial").

---

### Nivel de madurez tecnológica (TRL)

**En una frase.** Escala de 1 a 9 que indica cuán desarrollada y probada está una tecnología.

**Cómo pensarlo.** TRL 1 es un principio básico observado; TRL 4, validación en laboratorio; TRL 6, prototipo demostrado en un entorno relevante; TRL 9, sistema probado en misión real. Sirve para decidir cuándo una tecnología está lista para incorporarse a una misión sin añadir demasiado riesgo.

**Ejemplo.** Un instrumento que solo se probó en un banco (TRL 4) y que se incorpora a una misión con lanzamiento en dos años lleva un riesgo alto; suele exigirse TRL 6 antes de la revisión crítica de diseño.

**Error frecuente.** Tomar el TRL como una medida de calidad: mide madurez, no mérito.

**Relacionados:** margen, riesgo, ingeniería de sistemas.
📘 [B83](../../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md "Ingeniería de sistemas y diseño de misiones"), [B90](../../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md "Integración, ensayos y calificación espacial").

---

### Período sinódico

**En una frase.** Tiempo entre dos alineaciones idénticas de dos planetas respecto del Sol.

**Cómo pensarlo.** Los períodos orbitales son respecto de las estrellas (sidéreos); pero lo que importa para planear viajes es cada cuánto vuelven a alinearse. La Tierra gana vueltas sobre un planeta exterior más lento, y el período sinódico sale de la diferencia de sus velocidades angulares.

**Fórmula.** 1/S = |1/P₁ − 1/P₂|.

**Ejemplo.** Marte: P = 1,881 años → S = 1 / (1 − 1/1,881) ≈ **2,135 años ≈ 780 días**. Por eso hay ventanas de lanzamiento a Marte cada ≈ 26 meses. Un viaje tipo Hohmann Tierra–Marte dura ≈ 259 días.

**Error frecuente.** Usar P₂ − P₁ en vez de las frecuencias.

**Relacionados:** ventana de lanzamiento, oposición, Hohmann.
📘 [B75](../../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias"), [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica").

---

### Presión dinámica y Max-Q

**En una frase.** La presión dinámica (q) es la energía cinética del aire por unidad de volumen que choca contra el cohete; "Max-Q" es el instante en que es máxima.

**Cómo pensarlo.** Al subir, el cohete gana velocidad (q crece con v²) pero el aire se hace más tenue (q baja con ρ). El producto tiene un máximo, a menudo un minuto después del despegue, y es el momento de mayor esfuerzo estructural. A veces se reduce el empuje para pasar Max-Q con menos carga.

**Fórmula.** q = ½ ρ v². Unidades: Pa.

**Ejemplo.** ρ = 0,4 kg/m³ (≈ 9–10 km de altura) y v = 400 m/s: q = 32 kPa, del orden de 0,3 atmósferas.

**Error frecuente.** Pensar que el máximo está en la mayor velocidad: ocurre antes, cuando aún hay aire denso.

**Relacionados:** carga aerodinámica, ascenso, estructuras.
📘 [B77](../../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B84](../../programa/tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md "Estructuras, materiales y fabricación espacial").

---

### Propulsión eléctrica

**En una frase.** Sistema que acelera el propelente con campos eléctricos o magnéticos en lugar de quemarlo.

**Cómo pensarlo.** Expulsa iones o plasma a velocidades 5–10 veces mayores que un motor químico (Isp 1 500–4 000 s), por lo que gasta muy poco propelente, pero el empuje es mínimo (milinewtons) y limitado por la potencia eléctrica. Sirve para maniobras largas y suaves en el espacio, no para despegar.

**Ejemplo.** Un motor con 90 mN en una nave de 1 000 kg da una aceleración de 9 × 10⁻⁵ m/s²: ≈ **7,8 m/s por día**, es decir, ≈ 2,8 km/s al año de empuje continuo.

**Error frecuente.** Pensar que empuje bajo significa poca capacidad: con meses de funcionamiento puede superar el Δv de un motor químico.

**Relacionados:** impulso específico, ecuación del cohete, Dawn.
📘 [B78](../../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial").

---

### Radioisótopos (RTG)

**En una frase.** Generador que convierte en electricidad el calor de un material radiactivo.

**Cómo pensarlo.** El plutonio-238 emite calor al decaer durante décadas, sin depender de la luz solar. Termopares transforman ese calor en electricidad con baja eficiencia (≈ 6 %), pero con enorme fiabilidad. Es la solución cuando el Sol está lejos o hay largas noches.

**Ejemplo.** MMRTG de Curiosity y Perseverance: ≈ 2 kW térmicos → ≈ 110 W eléctricos. La potencia cae lentamente (vida media del Pu-238 ≈ 87,7 años más degradación).

**Error frecuente.** Confundirlo con un reactor nuclear: un RTG no tiene reacción en cadena.

**Relacionados:** energía solar, Voyager, seguridad nuclear.
📘 [B86](../../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md "Sistemas de potencia y energía espacial").

---

### Reconexión magnética

**En una frase.** Proceso por el que las líneas de campo magnético se rompen y se reconectan, liberando energía magnética en forma de calor y partículas aceleradas.

**Cómo pensarlo.** En un plasma con campos opuestos, las líneas se acercan, se rompen y se reorganizan en una configuración de menor energía; la diferencia se libera. Es el motor de las erupciones solares, de las subtormentas magnetosféricas y de las auroras.

**Ejemplo.** Una llamarada solar clase X libera del orden de 10²⁴–10²⁵ J en minutos.

**Error frecuente.** Imaginar que las líneas de campo son objetos físicos: son una representación del campo.

**Relacionados:** plasma, viento solar, clima espacial.
📘 [B35](../../programa/tronco-comun/B35-fisica-avanzada-de-plasmas-y-mhd-espacial.md "Física avanzada de plasmas y MHD espacial"), [B34](../../programa/tronco-comun/B34-corona-solar-y-erupciones-diagnostico-y-modelos.md "Corona solar y erupciones: diagnóstico y modelos").

---

### Redundancia y fiabilidad

**En una frase.** La redundancia es duplicar funciones para que el fallo de una parte no sea el fallo del sistema; la fiabilidad es la probabilidad de funcionar durante un tiempo.

**Cómo pensarlo.** Si un componente tiene fiabilidad R, dos en paralelo (basta uno) tienen 1 − (1 − R)². En serie (se necesitan todos) la fiabilidad es el producto, que cae rápido. Con tasa de fallo constante λ, R(t) = e^(−λt) y el MTBF = 1/λ.

**Ejemplo.** R = 0,90 → dos unidades en paralelo: 0,99. Diez componentes en serie con R = 0,99 cada uno: 0,99¹⁰ ≈ 0,904.

**Error frecuente.** Creer que duplicar protege de cualquier fallo: una causa común (el mismo software o una misma pieza) fallará en ambos (caso del Ariane 5).

**Relacionados:** puntos únicos de fallo, margen, verificación.
📘 [B88](../../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md "Aviónica y software crítico espacial"), [B83](../../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md "Ingeniería de sistemas y diseño de misiones").

---

### Rover y movilidad planetaria

**En una frase.** Vehículo robótico que se desplaza por la superficie de otro cuerpo.

**Cómo pensarlo.** Se mueven despacio y con autonomía, porque la latencia impide manejarlos en tiempo real. Evalúan el terreno con cámaras, calculan un camino seguro y avanzan por tramos de decenas de metros. Los factores críticos son el deslizamiento de las ruedas, la energía y la temperatura.

**Ejemplo.** El rover Opportunity recorrió ≈ 45 km en 14 años (2004–2018); Curiosity avanza como máximo ≈ 4 cm/s.

**Error frecuente.** Esperar que sean rápidos: sus decisiones se apoyan en seguridad, no en velocidad.

**Relacionados:** latencia, percepción, localización.
📘 [B102](../../programa/tronco-comun/B102-movilidad-de-robots-planetarios.md "Movilidad de robots planetarios"), [B99](../../programa/tronco-comun/B99-localizacion-y-mapeo-robotico.md "Localización y mapeo robótico"), [B98](../../programa/tronco-comun/B98-autonomia-y-teleoperacion-espacial.md "Autonomía y teleoperación espacial").

---

### Seeing (calidad de imagen atmosférica)

**En una frase.** La borrosidad que la turbulencia de la atmósfera produce en las imágenes de los astros.

**Cómo pensarlo.** Capas de aire con temperaturas distintas desvían la luz de forma variable; la imagen de una estrella se agita y se ensancha. Se mide por el ancho a media altura de su perfil (FWHM), en segundos de arco. El parámetro de Fried *r₀* (≈ 10–20 cm en visible) es el tamaño a partir del cual aumentar la apertura ya no mejora la nitidez, salvo con óptica adaptativa.

**Fórmula.** θ_seeing ≈ λ / r₀.

**Ejemplo.** λ = 500 nm y r₀ = 10 cm: θ ≈ 5 × 10⁻⁶ rad ≈ **1″**. Un telescopio de 8 m (límite de difracción ≈ 0,016″) está limitado a ≈ 1″ sin corrección.

**Error frecuente.** Pensar que un telescopio más grande siempre da más detalle desde la superficie.

**Relacionados:** óptica adaptativa, difracción, sitio astronómico.
📘 [B42](../../programa/tronco-comun/B42-optica-fisica-y-optica-adaptativa.md "Óptica física y óptica adaptativa"), [B48](../../programa/tronco-comun/B48-operaciones-de-observatorios-cientificos.md "Operaciones de observatorios científicos").

---

### Telemetría y telecomando

**En una frase.** La telemetría es el conjunto de datos de estado que la nave envía a tierra; el telecomando son las órdenes que recibe.

**Cómo pensarlo.** La telemetría dice cómo está la nave (temperaturas, tensiones, actitud); el telecomando la guía. Ambos usan protocolos con corrección de errores y, a veces, cifrado. Las operaciones de una misión consisten en vigilar la telemetría y enviar telecomandos dentro de límites seguros.

**Ejemplo.** Una nave envía 1 kbit/s de telemetría de estado; en 10 minutos acumula 600 kbit (≈ 75 kB).

**Error frecuente.** Confundir telemetría de estado con datos científicos, que suelen ir en canales distintos.

**Relacionados:** operaciones de misión, enlace de comunicaciones, CCSDS.
📘 [B96](../../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md "Control y operación de misiones espaciales"), [B94](../../programa/tronco-comun/B94-modulacion-codificacion-y-protocolos-de-enlace.md "Modulación, codificación y protocolos de enlace").

---

### Torque (momento de una fuerza)

**En una frase.** Efecto de giro que produce una fuerza aplicada a cierta distancia de un eje.

**Cómo pensarlo.** Igual que una llave larga facilita aflojar una tuerca. En una nave, los torques cambian la actitud (orientación). Una rueda de reacción gira en un sentido y la nave en el contrario, conservando el momento angular total.

**Fórmula.** τ = r × F = I α. Unidades: N·m.

**Ejemplo.** Un satélite con I = 0,01 kg·m² que debe acelerar su giro a 1 rad/s² requiere τ = 0,01 N·m.

**Error frecuente.** Olvidar que la rueda no "crea" giro: lo intercambia con la nave.

**Relacionados:** momento angular, control de actitud, rueda de reacción.
📘 [B87](../../programa/tronco-comun/B87-sensores-y-control-de-actitud.md "Sensores y control de actitud"), [B05](../../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md "Física fundamental para el espacio").

---

### Tratado del Espacio Exterior (1967)

**En una frase.** Acuerdo de las Naciones Unidas que establece los principios básicos del derecho espacial.

**Cómo pensarlo.** Fija que el espacio es de uso libre para todos los Estados, que no puede ser apropiado por soberanía, que se usa con fines pacíficos (sin armas de destrucción masiva en órbita ni en cuerpos celestes), que los Estados son responsables de las actividades de sus nacionales (incluso privados) y que deben autorizarlas y supervisarlas.

**Ejemplo.** Una empresa privada que lanza un satélite necesita una autorización y supervisión continuas de su Estado; si causa un daño, el Estado responde internacionalmente.

**Error frecuente.** Creer que prohíbe toda actividad militar: prohíbe armas nucleares y de destrucción masiva, pero no el uso militar de satélites.

**Relacionados:** responsabilidad, registro de objetos, recursos espaciales.
📘 [B119](../../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md "Derecho, seguridad y geopolítica espacial"), [B121](../../programa/tronco-comun/B121-regulacion-nacional-de-actividades-espaciales.md "Regulación nacional de actividades espaciales"), [B123](../../programa/tronco-comun/B123-responsabilidad-danos-y-controversias-espaciales.md "Responsabilidad, daños y controversias espaciales").

---

### Ventana de lanzamiento

**En una frase.** Intervalo de tiempo en el que un lanzamiento puede alcanzar su objetivo con los recursos disponibles.

**Cómo pensarlo.** La Tierra gira y los planetas se mueven. Para ir a una órbita concreta, el cohete debe salir cuando el plano de la órbita pasa sobre la plataforma (ventana diaria). Para un viaje interplanetario, los planetas deben estar bien alineados (ventana según el período sinódico). Fuera de la ventana, el Δv requerido crece mucho.

**Ejemplo.** Marte: una ventana cada ≈ 26 meses. Una ventana lunar o de estación puede durar minutos al día.

**Error frecuente.** Pensar que es una cuestión de clima: el tiempo meteorológico es otra restricción, adicional.

**Relacionados:** período sinódico, Hohmann, azimut de lanzamiento.
📘 [B75](../../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias"), [B77](../../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada").

---

[← A – M de la ampliación](ampliacion-a-m.md) · [Índice](README.md) · [Siguiente: tercera tanda A – E →](tercera-a-e.md)
