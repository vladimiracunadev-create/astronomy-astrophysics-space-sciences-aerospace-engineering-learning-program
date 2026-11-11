# Glosario esencial · A – C

[⬅️ Índice del glosario esencial](README.md) · [Glosario completo](../README.md)

Cada entrada sigue el mismo esquema: **en una frase**, **cómo pensarlo**, **fórmula y unidades** (cuando existe), **ejemplo con números**, **error frecuente** y **términos relacionados**. Los valores numéricos son redondeados y orientativos; la calculadora del programa ([`calculadora_cientifica.py`](../../herramientas/calculadora_cientifica.py)) permite comprobarlos.

---

### Aberración cromática

**En una frase.** Defecto de una lente en el que los colores no enfocan en el mismo punto.

**Cómo pensarlo.** El vidrio desvía más la luz azul que la roja (su índice de refracción depende de la longitud de onda). Una lente simple actúa como un prisma débil: cada color tiene su propio foco, y la imagen de una estrella aparece con un halo coloreado. Los espejos no tienen este defecto porque reflejan todos los colores con el mismo ángulo; por eso los telescopios grandes son reflectores.

**Se corrige con** un doblete acromático (dos vidrios de dispersión distinta) o con espejos.

**Ejemplo.** En un refractor simple de 100 mm y f/10, el foco azul y el rojo pueden diferir en varios milímetros, suficiente para ver un borde violeta alrededor de la Luna.

**Error frecuente.** Confundirla con la aberración esférica (que ocurre también con luz de un solo color).

**Relacionados:** aberración esférica, refracción, dispersión, doblete acromático.
📘 [B41](../../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md "Óptica geométrica y diseño de telescopios"), [B42](../../programa/tronco-comun/B42-optica-fisica-y-optica-adaptativa.md "Óptica física y óptica adaptativa").

---

### Aberración esférica

**En una frase.** Defecto de una superficie esférica en el que los rayos que llegan por el borde enfocan en un punto distinto de los que llegan por el centro.

**Cómo pensarlo.** Una esfera no es la forma perfecta para concentrar luz paralela en un punto; esa forma es la parábola. Cuanto más abierto es el espejo o la lente (número f pequeño), más se nota. Por eso los espejos primarios de los telescopios se pulen como paraboloides, no como esferas.

**Medida.** La aberración esférica longitudinal (LSA) es la diferencia entre el cruce con el eje de un rayo de altura *h* y el de un rayo paraxial.

**Ejemplo histórico.** El espejo del telescopio Hubble se pulió con la forma equivocada por unos 2 µm; en 1990 produjo imágenes borrosas hasta que, en 1993, se instaló óptica correctora.

**Error frecuente.** Pensar que "más pulido" la arregla: el problema es de forma, no de rugosidad.

**Relacionados:** aberración cromática, parábola, número f, coma.
📘 [B41](../../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md "Óptica geométrica y diseño de telescopios"), [B50](../../programa/tronco-comun/B50-diseno-optico-computacional-y-tolerancias.md "Diseño óptico computacional y tolerancias").

---

### Aceleración centrípeta

**En una frase.** La aceleración que apunta al centro de una trayectoria circular y cambia la dirección de la velocidad, no su módulo.

**Cómo pensarlo.** Un cuerpo que sigue una curva está acelerando aunque su rapidez sea constante, porque su velocidad (un vector) cambia de dirección. Esa aceleración la debe producir una fuerza hacia el centro: la gravedad en una órbita, la tensión de una cuerda en una honda.

**Fórmula.** a = v² / r = ω² r. Unidades: m/s².

**Ejemplo.** La Estación Espacial Internacional (v ≈ 7,67 km/s, r ≈ 6 778 km) tiene a ≈ 8,68 m/s², casi igual a la gravedad en la superficie. Por eso no "escapa" de la gravedad: cae continuamente alrededor de la Tierra.

**Error frecuente.** Llamarla "fuerza centrífuga". La centrífuga es una fuerza aparente que se introduce solo en un sistema de referencia que gira.

**Relacionados:** velocidad circular, fuerza centrípeta, microgravedad.
📘 [B05](../../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md "Física fundamental para el espacio"), [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental").

---

### Albedo

**En una frase.** Fracción de la luz incidente que un cuerpo refleja.

**Cómo pensarlo.** Va de 0 (negro perfecto, absorbe todo) a 1 (espejo difuso perfecto). Lo que no se refleja se absorbe y calienta el cuerpo. Es el puente entre cuánta luz recibe un planeta y qué temperatura alcanza.

**Fórmula.** A = luz reflejada / luz incidente (adimensional). La temperatura de equilibrio es T = [S (1 − A) / (4 σ)]^¼, con S el flujo solar recibido.

**Ejemplo.** Tierra A ≈ 0,3; Luna ≈ 0,12; Venus ≈ 0,76 por sus nubes. Con A = 0,3 y S = 1361 W/m² la Tierra tendría unos 255 K (−18 °C) sin efecto invernadero.

**Error frecuente.** Mezclar albedo de Bond (todas las longitudes y ángulos) con albedo geométrico (solo en oposición); no son iguales.

**Relacionados:** temperatura de equilibrio, efecto invernadero, cuerpo negro.
📘 [B54](../../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria"), [B85](../../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md "Gestión térmica y entorno espacial").

---

### Apoapsis y periapsis

**En una frase.** Los puntos de una órbita más lejano (apoapsis) y más cercano (periapsis) al cuerpo central.

**Cómo pensarlo.** Una órbita elíptica tiene dos extremos. Por la segunda ley de Kepler el cuerpo va más rápido en el periapsis y más lento en el apoapsis. Los nombres cambian con el cuerpo: perigeo y apogeo (Tierra), perihelio y afelio (Sol), periselenio y aposelenio (Luna).

**Fórmulas.** r_p = a(1 − e), r_a = a(1 + e), con *a* el semieje mayor y *e* la excentricidad. Unidades: m.

**Ejemplo.** Órbita de transferencia geoestacionaria: perigeo ≈ 6 678 km del centro y apogeo ≈ 42 164 km; a = 24 421 km y e ≈ 0,73.

**Error frecuente.** Medir la altura desde la superficie y mezclarla con la distancia al centro: en las fórmulas se usa la distancia al **centro**.

**Relacionados:** excentricidad, semieje mayor, vis-viva, leyes de Kepler.
📘 [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental").

---

### Ascensión recta y declinación

**En una frase.** El par de coordenadas que da la posición de un astro en la esfera celeste, equivalente a la longitud y latitud terrestres.

**Cómo pensarlo.** Se proyecta el ecuador terrestre al cielo (ecuador celeste) y se mide **hacia el norte o sur desde él** (declinación, de −90° a +90°) y **hacia el este desde el punto vernal** (ascensión recta, en horas, de 0 h a 24 h). Como el cielo gira, estas coordenadas no cambian por la hora ni el lugar del observador, a diferencia de altura y acimut.

**Conversión.** 1 h = 15°. Una estrella a 6 h de ascensión recta está a 90° del punto vernal.

**Ejemplo.** Betelgeuse: AR ≈ 5 h 55 min, Dec ≈ +7° 24′.

**Error frecuente.** Olvidar que las coordenadas varían lentamente por la precesión; por eso se indica la época (por ejemplo, J2000.0).

**Relacionados:** esfera celeste, precesión, altura y acimut, tiempo sidéreo.
📘 [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica"), [B13](../../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas").

---

### Asistencia gravitatoria

**En una frase.** Maniobra en la que una nave gana (o pierde) velocidad respecto al Sol al pasar cerca de un planeta en movimiento.

**Cómo pensarlo.** En el sistema de referencia del planeta, la nave entra y sale con la misma rapidez, pero con la dirección girada. Al volver al sistema del Sol, esa rotación de la velocidad relativa se suma a la velocidad del planeta, y la nave sale con otra velocidad. El planeta cede una fracción inconmensurable de su energía: no hay "magia", hay intercambio de momento.

**Fórmula (aproximada).** Giro δ con sen(δ/2) = 1 / (1 + r_p v∞² / GM). El cambio máximo de velocidad es del orden de 2 v_planeta.

**Ejemplo.** Voyager 2 usó asistencias de Júpiter, Saturno y Urano para llegar a Neptuno en 12 años; con propulsión directa habría tomado mucho más tiempo y combustible.

**Error frecuente.** Creer que la nave "roba" energía de la nada: la ganan del movimiento orbital del planeta.

**Relacionados:** velocidad hiperbólica en exceso, esfera de influencia, delta-v.
📘 [B75](../../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias").

---

### Astrometría

**En una frase.** La medición precisa de las posiciones y movimientos de los astros.

**Cómo pensarlo.** Es la rama más antigua de la astronomía. De ella salen la paralaje (distancia), el movimiento propio (velocidad transversal) y la órbita de las binarias. Gaia mide posiciones con precisión de decenas de microsegundos de arco para miles de millones de estrellas.

**Ejemplo.** Paralaje p = 0,1″ → d = 10 pc. Una precisión de 10 µas permite medir distancias confiables hasta decenas de kpc.

**Error frecuente.** Pensar que la posición medida es la real: hay que corregir por aberración, refracción atmosférica, precesión y movimiento propio.

**Relacionados:** paralaje, movimiento propio, parsec.
📘 [B74](../../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md "Estimación de órbitas y navegación espacial"), [B25](../../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md "Galaxias y medio interestelar").

---

### Atmósfera: altura de escala

**En una frase.** La distancia en la que la presión o la densidad de una atmósfera disminuye en un factor *e* ≈ 2,718.

**Cómo pensarlo.** El aire más alto pesa menos aire encima, de modo que la presión cae de forma exponencial con la altura. La altura de escala resume cuán "gruesa" es una atmósfera: grande si es caliente o de gas ligero, pequeña si es fría o pesada.

**Fórmula.** H = k_B T / (μ m_H g). Unidades: m.

**Ejemplo.** Tierra: H ≈ 8,4 km (T ≈ 288 K, μ ≈ 29). Marte: H ≈ 11 km con presión superficial del 0,6 % de la terrestre. A una altura H la presión del aire es ≈ 37 % de la del suelo.

**Error frecuente.** Creer que la atmósfera "termina" en un punto; se adelgaza sin límite nítido (la línea de Kármán a 100 km es una convención).

**Relacionados:** arrastre atmosférico, escape atmosférico, presión.
📘 [B54](../../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria"), [B72](../../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md "Perturbaciones y evolución de órbitas").

---

### Balance de enlace

**En una frase.** La cuenta de cuánta potencia sale del transmisor, cuánta se pierde en el camino y cuánta llega al receptor, para saber si la señal será útil.

**Cómo pensarlo.** Se suman ganancias y se restan pérdidas en decibelios (dB): potencia transmitida + ganancia de antenas − pérdida en el espacio libre − otras pérdidas = potencia recibida, que se compara con el ruido del receptor.

**Fórmula.** Pérdida en espacio libre: L_fs = (4π d / λ)². En dB: 20 log₁₀(4π d / λ). Relación señal-ruido: SNR = P_r / (k_B T B).

**Ejemplo.** A 2,3 GHz y 400 000 km (Luna), L_fs ≈ 211 dB; una antena parabólica de 34 m gana unos 56 dB a esa frecuencia (con eficiencia de 60 %), compensando buena parte.

**Error frecuente.** Olvidar márgenes (clima, apuntamiento) o sumar dB y vatios en la misma cuenta.

**Relacionados:** decibelio, ancho de banda, señal-ruido.
📘 [B89](../../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital"), [B91](../../programa/tronco-comun/B91-antenas-y-propagacion-para-enlaces-espaciales.md "Antenas y propagación para enlaces espaciales"), [B94](../../programa/tronco-comun/B94-modulacion-codificacion-y-protocolos-de-enlace.md "Modulación, codificación y protocolos de enlace").

---

### Big Bang

**En una frase.** Modelo según el cual el universo observable se expandió desde un estado muy denso y caliente hace unos 13 800 millones de años.

**Cómo pensarlo.** No fue una explosión en un lugar del espacio, sino la expansión del espacio mismo. Se sostiene con tres evidencias: la expansión (ley de Hubble), la radiación de fondo cósmico y la abundancia de elementos ligeros (hidrógeno, helio, litio). Sobre el "instante cero" no sabemos: el modelo describe bien lo que sigue, no el origen.

**Ejemplo.** Hoy el fondo cósmico tiene T ≈ 2,725 K; en la recombinación (≈ 380 000 años) era ≈ 3 000 K, un factor ≈ 1 100 mayor.

**Error frecuente.** Imaginar un centro desde el cual todo se aleja; en la expansión cada punto ve que los demás se alejan.

**Relacionados:** corrimiento al rojo, radiación cósmica de fondo, ley de Hubble.
📘 [B26](../../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología"), [B40](../../programa/tronco-comun/B40-universo-temprano-y-radiacion-cosmica-de-fondo.md "Universo temprano y radiación cósmica de fondo").

---

### Brillo superficial

**En una frase.** El brillo por unidad de área angular de un objeto extenso, como una galaxia o el cielo nocturno.

**Cómo pensarlo.** Una estrella es un punto: se mide su flujo total. Una galaxia o una nebulosa se extiende: importa cuánta luz llega por cada segundo de arco cuadrado. Un objeto puede ser brillante en total y casi invisible si su luz está muy extendida. Se mide en magnitudes por segundo de arco cuadrado (mag/arcsec²).

**Ejemplo.** Un cielo oscuro natural ≈ 21,9 mag/arcsec²; una ciudad, ≈ 18. Una diferencia de 4 mag es un factor ≈ 40 en brillo.

**Error frecuente.** Esperar que una galaxia de magnitud 8 sea fácil de ver: su brillo superficial puede ser menor que el del cielo.

**Relacionados:** magnitud, cielo oscuro, Bortle, contaminación lumínica.
📘 [B44](../../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md "Detectores y adquisición astronómica"), [B45](../../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md "Espectroscopía, fotometría y polarimetría").

---

### Campo magnético

**En una frase.** Región del espacio donde una carga en movimiento siente una fuerza perpendicular a su velocidad.

**Cómo pensarlo.** El campo magnético no cambia la energía de una partícula cargada, solo curva su trayectoria. Las partículas giran en espiral alrededor de las líneas de campo. Un campo como el terrestre atrapa partículas (cinturones de Van Allen) y desvía el viento solar (magnetosfera).

**Fórmula.** Fuerza de Lorentz F = q (v × B). Unidades: B en tesla (T); 1 T = 10⁴ gauss.

**Ejemplo.** El campo en la superficie terrestre ≈ 25–65 µT. El radio de giro de un protón de 1 MeV en 50 µT es ≈ 2,9 km.

**Error frecuente.** Decir que el campo magnético "acelera" partículas: cambia su dirección; la aceleración de energía requiere campos eléctricos o reconexión.

**Relacionados:** magnetosfera, plasma, viento solar, radiación.
📘 [B30](../../programa/tronco-comun/B30-heliofisica-y-fisica-de-plasmas.md "Heliofísica y física de plasmas"), [B33](../../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md "Clima espacial: impactos, pronóstico y riesgo"), [B35](../../programa/tronco-comun/B35-fisica-avanzada-de-plasmas-y-mhd-espacial.md "Física avanzada de plasmas y MHD espacial").

---

### Cefeida

**En una frase.** Estrella variable pulsante cuyo período de variación está ligado a su luminosidad.

**Cómo pensarlo.** Se hinchan y contraen con regularidad. Las más luminosas pulsan más despacio. Si mides el período en el cielo, sabes la luminosidad real, y comparándola con el brillo aparente obtienes la distancia: son "velas estándar". Henrietta Leavitt descubrió esta relación en 1912.

**Fórmula (forma típica).** M_V ≈ −2,43 (log₁₀ P − 1) − 4,05, con P en días. La relación exacta depende de la banda y de la metalicidad.

**Ejemplo.** Una cefeida de P = 10 d tiene M_V ≈ −4,05; si se ve con m = 14,0, entonces m − M = 18,05 → d ≈ 10^((18,05+5)/5) pc ≈ 40 kpc. (Ejemplo sin extinción.)

**Error frecuente.** Ignorar el polvo, que enrojece y atenúa, y confundir cefeidas clásicas con las de tipo II (más débiles).

**Relacionados:** vela estándar, módulo de distancia, escalera de distancias.
📘 [B25](../../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md "Galaxias y medio interestelar"), [B26](../../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología").

---

### Cinturones de Van Allen

**En una frase.** Zonas en forma de rosquilla alrededor de la Tierra donde el campo magnético atrapa partículas cargadas de alta energía.

**Cómo pensarlo.** Las partículas rebotan entre los polos magnéticos y derivan lentamente alrededor de la Tierra. Hay un cinturón interior (protones, ~ 1 000 a 6 000 km de altura) y uno exterior (electrones, más variable, hasta ~ 60 000 km). Una nave que los cruza recibe dosis de radiación que dañan electrónica y personas.

**Historia.** Explorer 1 (1958) detectó el cinturón por la saturación de su contador Geiger; James Van Allen interpretó la causa.

**Ejemplo.** Los astronautas de Apolo los cruzaron en horas, por una trayectoria rápida, con dosis bajas. La ISS (≈ 400 km) queda por debajo, salvo en la Anomalía del Atlántico Sur.

**Error frecuente.** Pensar que impiden viajar a la Luna: se cruzan rápido y con trayectorias de bajo tiempo de exposición.

**Relacionados:** magnetosfera, radiación espacial, viento solar.
📘 [B33](../../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md "Clima espacial: impactos, pronóstico y riesgo"), [B112](../../programa/tronco-comun/B112-radiobiologia-y-proteccion-radiologica-espacial.md "Radiobiología y protección radiológica espacial").

---

### Constante de gravitación (G) y parámetro gravitacional (GM)

**En una frase.** *G* es la constante que fija la intensidad de la gravedad; *GM* es el producto con la masa de un cuerpo, mucho mejor conocido que cada factor por separado.

**Cómo pensarlo.** La ley de Newton F = G m₁ m₂ / r² contiene *G*, que es difícil de medir (incertidumbre relativa ~ 2 × 10⁻⁵). Pero el movimiento orbital depende solo de *GM*, que se mide con gran precisión siguiendo satélites. Por eso en mecánica orbital se usa *GM* y se evita separar *G* y *M*.

**Valores.** G = 6,674 30 × 10⁻¹¹ m³ kg⁻¹ s⁻² (CODATA 2018). GM_Tierra = 3,986 004 × 10¹⁴ m³ s⁻². GM_Sol = 1,327 124 4 × 10²⁰ m³ s⁻².

**Ejemplo.** Con *GM* se obtiene la gravedad en la superficie terrestre: g = GM / R² = 3,986 × 10¹⁴ / (6,378 × 10⁶)² ≈ 9,80 m/s².

**Error frecuente.** Confundir *G* (universal) con *g* (aceleración local, varía con el cuerpo y la altura).

**Relacionados:** ley de gravitación universal, masa, peso.
📘 [B05](../../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md "Física fundamental para el espacio"), [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental").

---

### Corrimiento al rojo (redshift)

**En una frase.** Aumento de la longitud de onda de la luz recibida respecto de la emitida.

**Cómo pensarlo.** Tiene tres orígenes: el **Doppler** (fuente que se aleja), el **cosmológico** (el espacio se expande mientras la luz viaja) y el **gravitacional** (la luz sale de un pozo de potencial). En cosmología, 1 + z indica cuánto se ha estirado el universo desde que la luz salió.

**Fórmula.** z = (λ_obs − λ_emit) / λ_emit. Doppler, z pequeño: z ≈ v/c. Relativista: 1 + z = √[(1 + β)/(1 − β)].

**Ejemplo.** La línea Hα (656,3 nm) observada en 721,9 nm → z = 0,10, v ≈ 0,095 c ≈ 28 500 km/s.

**Error frecuente.** Interpretar siempre z como velocidad: a z grande la "velocidad" depende del modelo cosmológico.

**Relacionados:** Doppler, ley de Hubble, expansión del universo.
📘 [B26](../../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología"), [B45](../../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md "Espectroscopía, fotometría y polarimetría").

---

### Cuerpo negro

**En una frase.** Objeto ideal que absorbe toda la radiación que recibe y emite un espectro que depende solo de su temperatura.

**Cómo pensarlo.** Es el patrón con el que se compara a las estrellas, los planetas y el fondo cósmico. Dos reglas: la potencia emitida crece como T⁴ (Stefan–Boltzmann) y el color dominante se desplaza hacia el azul al subir la temperatura (Wien).

**Fórmulas.** Potencia por área: j = σ T⁴, σ = 5,670 374 × 10⁻⁸ W m⁻² K⁻⁴. Pico: λ_máx = b / T, b = 2,897 77 × 10⁻³ m K.

**Ejemplo.** Sol, T ≈ 5 772 K → λ_máx ≈ 502 nm (verde). Cuerpo humano, T = 310 K → ≈ 9,3 µm (infrarrojo). Fondo cósmico, 2,725 K → ≈ 1,06 mm.

**Error frecuente.** Creer que el color de una estrella coincide con su pico de Wien; el ojo integra todo el espectro y el Sol se ve blanco-amarillo.

**Relacionados:** luminosidad, temperatura efectiva, albedo.
📘 [B24](../../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B05](../../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md "Física fundamental para el espacio").

---

### Curva de luz

**En una frase.** Gráfico del brillo de un objeto en función del tiempo.

**Cómo pensarlo.** Muchos fenómenos (tránsitos de exoplanetas, binarias eclipsantes, supernovas, estrellas pulsantes, rotación de asteroides) se identifican por su forma: una caída periódica y plana, un pico rápido con decaimiento lento, una oscilación regular.

**Ejemplo.** Un planeta del tamaño de Júpiter que transita una estrella como el Sol oscurece (R_p / R_*)² ≈ (0,10)² ≈ 1 %. Un planeta como la Tierra produce ≈ 0,008 %, que solo se mide desde el espacio.

**Error frecuente.** Concluir con muy pocos puntos; se necesitan varios ciclos y una evaluación del ruido.

**Relacionados:** tránsito, fotometría, periodograma.
📘 [B29](../../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md "Astronomía temporal y exoplanetas"), [B15](../../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md "Señales, imágenes y estimación científica").

---

[⬅️ Índice del glosario esencial](README.md) · [Siguiente: D – L →](esencial-d-l.md)
