# Glosario esencial (tercera tanda) · A – E

[⬅️ Índice del glosario esencial](README.md) · [Glosario completo](../README.md)

Astrofísica, instrumentos, ciencias planetarias y vuelo humano. Mismo esquema: **en una frase**, **cómo pensarlo**, **fórmula y unidades**, **ejemplo con números**, **error frecuente**, **relacionados**. Valores redondeados y orientativos.

---

### Anomalía y ecuación de Kepler

**En una frase.** Las anomalías son ángulos que indican en qué punto de su órbita está un cuerpo; la ecuación de Kepler conecta el tiempo con la posición.

**Cómo pensarlo.** La **anomalía media** M crece de manera uniforme con el tiempo (como si el cuerpo fuese por un círculo a velocidad constante). Pero el movimiento real es más rápido cerca del periapsis. La **anomalía excéntrica** E y la **verdadera** ν describen la posición real. Para pasar del tiempo a la posición hay que resolver la ecuación de Kepler, que no tiene solución algebraica simple y se resuelve por iteración.

**Fórmula.** M = n (t − t₀) con n = √(GM/a³); M = E − e sen E.

**Ejemplo.** e = 0,5 y M = 1 rad: se itera E = M + e sen E → E ≈ **1,4987 rad**.

**Error frecuente.** Confundir M (tiempo) con ν (posición): coinciden solo si e = 0.

**Relacionados:** excentricidad, elementos orbitales, leyes de Kepler.
📘 [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B74](../../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md "Estimación de órbitas y navegación espacial").

---

### Asteroides y cometas

**En una frase.** Los asteroides son cuerpos rocosos o metálicos pequeños; los cometas son cuerpos de hielo y polvo que desarrollan atmósfera y cola cerca del Sol.

**Cómo pensarlo.** Son restos de la formación del sistema solar. La mayoría de los asteroides orbita entre Marte y Júpiter (≈ 2,1–3,3 UA); su masa total es de solo ≈ 4 % de la lunar. Un cometa se calienta, sublima su hielo y forma una **coma** y dos colas: la de polvo (curva) y la de iones (recta, empujada por el viento solar, siempre en dirección opuesta al Sol).

**Ejemplo.** El cometa Halley tiene un período de ≈ 76 años y un núcleo de ≈ 15 km. Ceres, el mayor asteroide, mide ≈ 940 km.

**Error frecuente.** Creer que la cola de un cometa va detrás de él como la estela de un avión; apunta en dirección opuesta al Sol.

**Relacionados:** cinturón de Kuiper, defensa planetaria, DART.
📘 [B58](../../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md "Asteroides, cometas y defensa planetaria").

---

### Aurora

**En una frase.** Luz producida cuando partículas cargadas del viento solar chocan con la atmósfera superior cerca de los polos magnéticos.

**Cómo pensarlo.** El campo magnético terrestre canaliza las partículas hacia dos óvalos alrededor de los polos. Al chocar con átomos de oxígeno y nitrógeno los excitan y estos emiten luz: verde (oxígeno, 557,7 nm, a ≈ 100–150 km), rojo (oxígeno, 630 nm, a mayores alturas) y azul o violeta (nitrógeno).

**Ejemplo.** Durante tormentas geomagnéticas intensas se han visto auroras a latitudes medias, por ejemplo en 1859 (evento Carrington).

**Error frecuente.** Creer que es un reflejo de luz en el hielo: es emisión de luz por átomos excitados.

**Relacionados:** viento solar, magnetosfera, clima espacial.
📘 [B33](../../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md "Clima espacial: impactos, pronóstico y riesgo"), [B30](../../programa/tronco-comun/B30-heliofisica-y-fisica-de-plasmas.md "Heliofísica y física de plasmas").

---

### Biosignatura

**En una frase.** Señal que sugiere la presencia de procesos biológicos, ya sea en una muestra o en una atmósfera lejana.

**Cómo pensarlo.** Se busca algo que sea difícil de explicar sin vida: por ejemplo, **gases en desequilibrio** (oxígeno y metano juntos, que reaccionarían rápido si no se repusieran). Una sola señal rara vez basta: hay que descartar procesos no biológicos (falsos positivos) y entender el contexto del planeta.

**Ejemplo.** En la Tierra el oxígeno es mayoritariamente biológico, pero un planeta sin agua o con ciertos procesos de fotólisis puede generarlo sin vida.

**Error frecuente.** Tratar una detección como prueba de vida; la afirmación extraordinaria exige evidencia múltiple y verificable.

**Relacionados:** zona habitable, astrobiología, espectro de transmisión.
📘 [B56](../../programa/tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md "Astrobiología y vida extraterrestre"), [B63](../../programa/tronco-comun/B63-exploracion-in-situ-y-analisis-de-muestras-planetarias.md "Exploración in situ y análisis de muestras planetarias").

---

### CCD y detectores de imagen

**En una frase.** Sensor que convierte fotones en electrones y los cuenta píxel a píxel.

**Cómo pensarlo.** Cada píxel acumula carga proporcional a la luz recibida durante la exposición. Después se lee y se convierte en un número con un conversor analógico-digital. Magnitudes clave: **eficiencia cuántica** (fracción de fotones detectados), **ruido de lectura**, **corriente oscura**, **capacidad del pozo** y **ganancia** (electrones por unidad digital).

**Ejemplo.** Un pozo de 100 000 e⁻ con un conversor de 16 bits (65 536 niveles) da una ganancia de ≈ 1,5 e⁻/ADU. Saturación: más de 100 000 e⁻ en un píxel.

**Error frecuente.** Confundir una imagen saturada con una más brillante: el valor deja de crecer y se pierde información.

**Relacionados:** señal-ruido, fotometría, campo plano.
📘 [B44](../../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md "Detectores y adquisición astronómica").

---

### Clase espectral

**En una frase.** Clasificación de las estrellas por su espectro, que refleja su temperatura superficial.

**Cómo pensarlo.** La secuencia O B A F G K M va de las más calientes (azules) a las más frías (rojas). Cada clase tiene subdivisiones de 0 a 9. Un mnemotécnico clásico: "Oh Be A Fine Girl/Guy, Kiss Me".

**Ejemplo.** Estrellas azules clase O: > 30 000 K; Sol, G2: 5 772 K; enanas rojas M: 2 400–3 700 K.

**Error frecuente.** Creer que el orden es alfabético: es histórico y se reordenó por temperatura.

**Relacionados:** temperatura efectiva, diagrama H-R, espectroscopía.
📘 [B24](../../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B32](../../programa/tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md "Atmósferas estelares y espectroscopía estelar cuantitativa").

---

### Cinturón de Kuiper y nube de Oort

**En una frase.** El cinturón de Kuiper es una región de cuerpos helados más allá de Neptuno; la nube de Oort es una envoltura hipotética mucho más lejana, fuente de cometas de largo período.

**Cómo pensarlo.** Kuiper se extiende desde ≈ 30 hasta ≈ 50 UA e incluye a Plutón y otros planetas enanos. La nube de Oort, con objetos a ≈ 2 000–100 000 UA, no se ha observado directamente; su existencia se infiere de las órbitas de los cometas.

**Ejemplo.** New Horizons visitó Plutón (≈ 33 UA en 2015) y Arrokoth (≈ 44 UA en 2019). Voyager 1 está a ≈ 165 UA, aún muy lejos de la parte interior de la nube de Oort.

**Error frecuente.** Pensar que Voyager "ya salió del sistema solar": salió de la heliosfera, pero no de la influencia gravitatoria del Sol.

**Relacionados:** cometas, heliosfera, planetas enanos.
📘 [B52](../../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B58](../../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md "Asteroides, cometas y defensa planetaria").

---

### Código de corrección de errores

**En una frase.** Técnica que añade redundancia a los datos para detectar y corregir errores de transmisión.

**Cómo pensarlo.** El ruido voltea bits. Un código añade bits extra con una estructura que permite al receptor reconocer y reparar errores. Los códigos modernos (turbo, LDPC) se acercan al límite de Shannon. El **BER** (tasa de error de bit) es la fracción de bits recibidos mal. Usar código reduce la potencia necesaria para un BER dado: ganancia de codificación de varios dB.

**Ejemplo.** Código de repetición ×3 con voto de mayoría y p = 0,01: probabilidad de error = 3p²(1 − p) + p³ ≈ **2,98 × 10⁻⁴**, unas 34 veces menor, a costa de triplicar los bits.

**Error frecuente.** Pensar que más redundancia es siempre mejor: reduce la tasa útil.

**Relacionados:** ancho de banda, señal-ruido, balance de enlace.
📘 [B94](../../programa/tronco-comun/B94-modulacion-codificacion-y-protocolos-de-enlace.md "Modulación, codificación y protocolos de enlace").

---

### Cráter de impacto

**En una frase.** Depresión producida por la colisión de un cuerpo a alta velocidad contra una superficie.

**Cómo pensarlo.** A velocidades de kilómetros por segundo, la energía cinética se libera casi instantáneamente como onda de choque; el cráter es mucho mayor que el impactor. Los cráteres sin erosión (Luna, Mercurio) son un registro del bombardeo: cuantos más hay, más antigua es la superficie (conteo de cráteres como reloj).

**Fórmula.** E = ½ m v². Ejemplo: asteroide de 10 km, densidad 3 000 kg/m³ → m ≈ 1,6 × 10¹⁵ kg; a 20 km/s: E ≈ 3 × 10²³ J ≈ 7,5 × 10⁷ megatones de TNT.

**Ejemplo.** Chicxulub (México, ≈ 66 millones de años, ≈ 180 km de diámetro) se asocia con la extinción de los dinosaurios no avianos. Meteor Crater (Arizona, ≈ 1,2 km, ≈ 50 000 años).

**Error frecuente.** Pensar que la Tierra "no tiene cráteres": la erosión y la tectónica los borran.

**Relacionados:** defensa planetaria, geología de impactos, edad de superficies.
📘 [B61](../../programa/tronco-comun/B61-crateres-de-impacto-y-geologia-de-impactos.md "Cráteres de impacto y geología de impactos"), [B58](../../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md "Asteroides, cometas y defensa planetaria").

---

### Cúmulo globular

**En una frase.** Agrupación esférica y muy densa de cientos de miles de estrellas viejas.

**Cómo pensarlo.** Se formaron hace 11–13 mil millones de años, casi al mismo tiempo, y por eso sirven como laboratorios de evolución estelar: todas las estrellas tienen la misma edad y composición, y solo cambia su masa. Orbitan en el halo de la galaxia (la Vía Láctea tiene ≈ 150).

**Ejemplo.** Omega Centauri contiene unos 10 millones de estrellas y es el mayor de la Vía Láctea.

**Error frecuente.** Confundirlo con un cúmulo abierto (joven, disperso, en el disco).

**Relacionados:** evolución estelar, edad del universo, metalicidad.
📘 [B25](../../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md "Galaxias y medio interestelar"), [B38](../../programa/tronco-comun/B38-poblaciones-estelares-y-simulacion-de-galaxias.md "Poblaciones estelares y simulación de galaxias").

---

### Descompresión (enfermedad por)

**En una frase.** Formación de burbujas de gas en los tejidos cuando la presión ambiente baja demasiado rápido.

**Cómo pensarlo.** Con aire a presión normal el cuerpo disuelve nitrógeno. Si la presión baja de golpe (como al salir a una caminata espacial con traje a menor presión), el nitrógeno forma burbujas que causan dolor articular o daños graves. Se previene con **prerrespiración de oxígeno puro** antes de salir, que elimina el nitrógeno disuelto.

**Ejemplo.** La cabina de la ISS está a ≈ 101 kPa; el traje de caminata espacial opera a ≈ 30 kPa, y por eso los astronautas respiran oxígeno antes de salir durante varias horas.

**Error frecuente.** Pensar que ocurre por falta de oxígeno; es un problema del nitrógeno disuelto.

**Relacionados:** traje espacial, caminata espacial, soporte vital.
📘 [B108](../../programa/tronco-comun/B108-actividades-extravehiculares-y-trajes-espaciales.md "Actividades extravehiculares y trajes espaciales"), [B110](../../programa/tronco-comun/B110-emergencias-y-seguridad-de-tripulacion.md "Emergencias y seguridad de tripulación").

---

### Diagrama de Hertzsprung–Russell (H-R)

**En una frase.** Gráfico de luminosidad frente a temperatura de las estrellas.

**Cómo pensarlo.** Las estrellas no se reparten al azar: la mayoría cae en la **secuencia principal** (fusionando hidrógeno), otras son gigantes o supergigantes (más brillantes por tamaño) y enanas blancas (calientes pero débiles). La posición de una estrella dice su masa y su fase evolutiva. En la secuencia principal L ∝ M^3,5 aproximadamente, así que las estrellas masivas viven poco: t ∝ M/L ∝ M^−2,5.

**Ejemplo.** Una estrella de 10 M☉ vive ≈ 10 mil millones de años × 10^−2,5 ≈ **30 millones de años**.

**Error frecuente.** Interpretarlo como un mapa del cielo; no lo es: es un gráfico de propiedades.

**Relacionados:** clase espectral, luminosidad, evolución estelar.
📘 [B24](../../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B37](../../programa/tronco-comun/B37-interiores-estelares-y-asterosismologia.md "Interiores estelares y asterosismología").

---

### Disco de acreción y límite de Eddington

**En una frase.** Un disco de acreción es el gas que cae en espiral hacia un objeto compacto; el límite de Eddington es la luminosidad máxima a la que la presión de la radiación equilibra la gravedad.

**Cómo pensarlo.** El gas que cae se calienta por fricción y radia, a veces con eficiencias de ≈ 10 % de mc². Si la luminosidad es demasiado alta, la radiación empuja el gas y frena la acreción.

**Fórmula.** L_Edd ≈ 1,26 × 10³¹ W · (M / M☉) ≈ 3,3 × 10⁴ L☉ · (M / M☉).

**Ejemplo.** Un agujero negro de 10⁹ M☉ puede alcanzar L_Edd ≈ 1,3 × 10⁴⁰ W: es la potencia de un quásar.

**Error frecuente.** Considerarlo un límite absoluto: puede superarse por períodos con geometría no esférica.

**Relacionados:** agujero negro, quásar, estrella de neutrones.
📘 [B27](../../programa/tronco-comun/B27-objetos-compactos-y-altas-energias.md "Objetos compactos y altas energías").

---

### DTN (redes tolerantes a retardos)

**En una frase.** Protocolo que guarda los datos en cada nodo hasta que el siguiente enlace esté disponible.

**Cómo pensarlo.** Internet asume enlaces continuos y retardos cortos. En el espacio hay demoras de minutos y desconexiones (rotación de planetas, ocultaciones). DTN usa "almacenar y reenviar" con paquetes llamados *bundles*, de modo que la información avanza por etapas y no se pierde por interrupciones.

**Ejemplo.** Un mensaje de un rover a la Tierra puede esperar en un orbitador hasta que este tenga visibilidad con la antena terrestre.

**Error frecuente.** Pensar que DTN acelera el tránsito: soporta las demoras, no las reduce.

**Relacionados:** latencia, telemetría, CCSDS.
📘 [B94](../../programa/tronco-comun/B94-modulacion-codificacion-y-protocolos-de-enlace.md "Modulación, codificación y protocolos de enlace"), [B89](../../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital").

---

### Elementos orbitales keplerianos

**En una frase.** Seis números que determinan una órbita y la posición del cuerpo en ella.

**Cómo pensarlo.** Dos describen la forma y el tamaño (excentricidad *e*, semieje mayor *a*), tres orientan el plano y la elipse en el espacio (inclinación *i*, ascensión del nodo Ω, argumento del periapsis ω) y uno da la posición en el tiempo (anomalía verdadera ν o media M). Son la forma más compacta de describir una órbita ideal.

**Ejemplo.** ISS: a ≈ 6 780 km, e ≈ 0,0005, i = 51,6°. El conjunto se publica en formatos como los elementos de dos líneas (TLE).

**Error frecuente.** Olvidar que con perturbaciones los elementos cambian con el tiempo (elementos osculadores).

**Relacionados:** anomalía de Kepler, perturbaciones, TLE.
📘 [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B74](../../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md "Estimación de órbitas y navegación espacial").

---

### Energía oscura

**En una frase.** Componente desconocida que causa la aceleración de la expansión del universo.

**Cómo pensarlo.** En 1998 dos equipos midieron supernovas tipo Ia lejanas y las encontraron más débiles de lo esperado: el universo se expande cada vez más rápido (Nobel de Física 2011). La causa se llama energía oscura; su explicación más simple es una constante cosmológica Λ, pero su valor no se entiende. Aporta ≈ 68 % del contenido del universo.

**Ejemplo.** Densidad crítica ≈ 9 × 10⁻²⁷ kg/m³; la energía oscura aporta ≈ 6 × 10⁻²⁷ kg/m³ equivalentes.

**Error frecuente.** Confundirla con la materia oscura: la primera acelera la expansión; la segunda agrupa galaxias.

**Relacionados:** ley de Hubble, supernova tipo Ia, cosmología.
📘 [B26](../../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología"), [B36](../../programa/tronco-comun/B36-formacion-de-estructuras-cosmicas-y-materia-oscura.md "Formación de estructuras cósmicas y materia oscura").

---

### Equilibrio hidrostático

**En una frase.** Balance entre la gravedad que comprime una estrella y la presión interna que la expande.

**Cómo pensarlo.** Cada capa soporta el peso de las superiores: la presión crece hacia el centro. Si la fusión aumenta, la estrella se expande y se enfría, reduciendo la fusión: un termostato natural. Cuando se agota el combustible, el equilibrio se rompe y la estrella cambia de fase.

**Fórmula.** dP/dr = −ρ g(r) = −ρ G M(r)/r².

**Ejemplo.** Estimación de orden: P ~ GM²/R⁴ para el Sol da ~ 10¹⁵ Pa; el valor real en el centro es ≈ 2,5 × 10¹⁶ Pa.

**Error frecuente.** Pensar que la estrella está "quieta": es un equilibrio dinámico.

**Relacionados:** fusión estelar, evolución estelar, asterosismología.
📘 [B24](../../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B37](../../programa/tronco-comun/B37-interiores-estelares-y-asterosismologia.md "Interiores estelares y asterosismología").

---

### Espectro de transmisión (atmósferas de exoplanetas)

**En una frase.** Cuánta luz estelar absorbe la atmósfera de un planeta en tránsito a cada longitud de onda.

**Cómo pensarlo.** Durante el tránsito, parte de la luz de la estrella pasa por el borde de la atmósfera. Donde un gas absorbe, el planeta parece un poco más grande. La profundidad de la señal depende del tamaño de la atmósfera (altura de escala H) y de la estrella.

**Fórmula.** Señal ≈ 2 R_p H / R_*².

**Ejemplo.** Júpiter caliente con H ≈ 500 km alrededor de una estrella solar: ≈ 1,4 × 10⁻⁴ (140 ppm). Planeta tipo Tierra: ≈ 2 × 10⁻⁷ (0,2 ppm), casi imposible hoy.

**Error frecuente.** Esperar atmósferas claras: las nubes y las brumas aplanan el espectro.

**Relacionados:** exoplaneta, altura de escala, biosignatura.
📘 [B29](../../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md "Astronomía temporal y exoplanetas"), [B54](../../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria").

---

### Espectrógrafo y rejilla de difracción

**En una frase.** Instrumento que separa la luz por longitudes de onda, con un prisma o con una rejilla de difracción.

**Cómo pensarlo.** Una rejilla tiene miles de ranuras por milímetro; la luz de cada color se desvía en un ángulo distinto. La resolución depende del número de ranuras iluminadas y del orden: más líneas, más resolución.

**Fórmulas.** m λ = d (sen α + sen β); R = λ/Δλ = m N.

**Ejemplo.** 10 000 ranuras iluminadas en segundo orden: R = 2 × 10⁴, equivalente a distinguir ≈ 15 km/s en velocidad.

**Error frecuente.** Olvidar que los órdenes pueden solaparse en longitudes de onda distintas.

**Relacionados:** espectroscopía, resolución, Doppler.
📘 [B45](../../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md "Espectroscopía, fotometría y polarimetría").

---

### Eyección de masa coronal (CME)

**En una frase.** Expulsión de una gran nube de plasma magnetizado desde la corona solar.

**Cómo pensarlo.** A diferencia de una llamarada (luz), una CME es materia: del orden de 10¹²–10¹³ kg a 300–3 000 km/s. Si llega a la Tierra con el campo magnético apropiado, comprime la magnetosfera y causa tormentas geomagnéticas, auroras y corrientes inducidas.

**Ejemplo.** Tiempo de viaje: 1 UA / 1 000 km/s ≈ 1,5 × 10⁵ s ≈ **42 h**. La tormenta de marzo de 1989 dejó sin electricidad a Quebec durante ≈ 9 horas.

**Error frecuente.** Confundirla con la llamarada; pueden coincidir, pero son procesos distintos.

**Relacionados:** viento solar, reconexión magnética, clima espacial.
📘 [B34](../../programa/tronco-comun/B34-corona-solar-y-erupciones-diagnostico-y-modelos.md "Corona solar y erupciones: diagnóstico y modelos"), [B33](../../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md "Clima espacial: impactos, pronóstico y riesgo").

---

[← Ampliación N – Z](ampliacion-n-z.md) · [Índice](README.md) · [Siguiente: tercera tanda F – T →](tercera-f-t.md)
