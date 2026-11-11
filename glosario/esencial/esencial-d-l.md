# Glosario esencial · D – L

[⬅️ Índice del glosario esencial](README.md) · [Glosario completo](../README.md)

Mismo esquema: **en una frase**, **cómo pensarlo**, **fórmula y unidades**, **ejemplo con números**, **error frecuente**, **relacionados**. Los valores son redondeados y orientativos.

---

### Delta-v (Δv)

**En una frase.** El cambio total de velocidad que una nave debe producir con su propulsión para completar una maniobra o misión.

**Cómo pensarlo.** Es la "moneda" de la astronáutica. Cada maniobra tiene un costo en Δv y el cohete es una máquina que convierte masa de propelente en Δv. Sumar Δv de maniobras sucesivas da el presupuesto de la misión, y la ecuación del cohete lo convierte en masa de combustible.

**Fórmula.** Δv = Isp · g₀ · ln(m₀ / m_f). Unidades: m/s (Isp en s, g₀ = 9,806 65 m/s²).

**Ejemplo.** De la órbita baja terrestre a la órbita geoestacionaria: ≈ 3,9 km/s. Con Isp = 450 s, la razón de masas necesaria es e^(3900/(450·9,81)) ≈ 2,4: más de la mitad de la masa inicial es propelente.

**Error frecuente.** Sumar el Δv como si fuera una distancia; no lo es: depende de la órbita de partida y llegada y de las pérdidas por gravedad y arrastre.

**Relacionados:** ecuación del cohete, impulso específico, transferencia de Hohmann.
📘 [B77](../../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B78](../../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial"), [B75](../../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias").

---

### Densidad

**En una frase.** Cantidad de masa por unidad de volumen.

**Cómo pensarlo.** Dice de qué está hecho un cuerpo sin importar su tamaño. Un planeta de baja densidad es gaseoso o helado; uno de alta densidad es rocoso y metálico. Con solo la masa y el radio de un exoplaneta ya se puede inferir si es rocoso o una mini-Neptuno.

**Fórmula.** ρ = M / V; para una esfera V = (4/3)π R³. Unidades: kg/m³.

**Ejemplo.** Agua: 1 000 kg/m³. Tierra: 5 514. Luna: 3 344. Saturno: 687 (menos que el agua: "flotaría"). Una estrella de neutrones: ≈ 10¹⁷ kg/m³.

**Error frecuente.** Confundir densidad con masa: Saturno tiene 95 masas terrestres, pero su densidad es menor que la del agua.

**Relacionados:** masa, volumen, estructura interna.
📘 [B52](../../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B65](../../programa/tronco-comun/B65-geofisica-de-interiores-planetarios.md "Geofísica de interiores planetarios").

---

### Difracción

**En una frase.** Desviación y reparto de una onda al pasar por una abertura o rodear un obstáculo.

**Cómo pensarlo.** La luz es una onda: al pasar por una apertura finita (la abertura de un telescopio), no se concentra en un punto perfecto sino en un disco rodeado de anillos (disco de Airy). Por tanto, hay un límite fundamental a la nitidez que depende solo del tamaño de la apertura y de la longitud de onda.

**Fórmula.** Resolución angular (criterio de Rayleigh): θ = 1,22 λ / D. Unidades: radianes (1 rad = 206 265″).

**Ejemplo.** Un telescopio de 1 m a 550 nm: θ = 1,22 · 550 × 10⁻⁹ / 1 = 6,7 × 10⁻⁷ rad ≈ 0,14″. Hubble (2,4 m) ≈ 0,06″. Con la atmósfera turbulenta (seeing ≈ 1″) un telescopio terrestre no alcanza ese límite sin óptica adaptativa.

**Error frecuente.** Creer que más aumento mejora el detalle: el límite lo fija la apertura, no el ocular.

**Relacionados:** resolución angular, disco de Airy, óptica adaptativa, seeing.
📘 [B42](../../programa/tronco-comun/B42-optica-fisica-y-optica-adaptativa.md "Óptica física y óptica adaptativa"), [B46](../../programa/tronco-comun/B46-radioastronomia-e-interferometria.md "Radioastronomía e interferometría").

---

### Distancia focal y número f

**En una frase.** La distancia focal (f) es la que hay entre el espejo o lente y el punto donde enfoca la luz paralela; el número f es f / D.

**Cómo pensarlo.** Un telescopio de focal larga da una imagen grande y estrecha (más "zoom") y uno de focal corta da una imagen pequeña y luminosa para objetos extensos. El número f controla el brillo de los objetos extensos: f/4 recoge 4 veces más luz por área de imagen que f/8.

**Fórmulas.** N = f / D (sin unidades). Escala de placa: 206 265 / f[mm] (arcsec/mm).

**Ejemplo.** Un espejo de D = 200 mm y f = 1 000 mm es f/5; su escala de placa es 206 265 / 1 000 ≈ 206″ por mm.

**Error frecuente.** Pensar que el diámetro y la distancia focal son lo mismo: el diámetro da la luz y la resolución; la focal, el tamaño de la imagen.

**Relacionados:** aberración esférica, escala de placa, apertura.
📘 [B41](../../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md "Óptica geométrica y diseño de telescopios"), [B44](../../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md "Detectores y adquisición astronómica").

---

### Doppler (efecto)

**En una frase.** Cambio de frecuencia que percibe un observador cuando la fuente y él se acercan o se alejan.

**Cómo pensarlo.** Si la fuente se aleja, las crestas llegan más espaciadas (frecuencia menor, luz más roja). Si se acerca, más juntas (más azul). Solo la componente de la velocidad a lo largo de la línea de visión (velocidad radial) produce el efecto.

**Fórmula.** Para v ≪ c: Δλ / λ ≈ v_r / c.

**Ejemplo.** Un planeta tira de su estrella con v_r = 12,5 m/s (Júpiter sobre el Sol): Δλ/λ ≈ 4 × 10⁻⁸. Es el cambio que detectó 51 Pegasi b en 1995 con espectrógrafos de alta precisión.

**Error frecuente.** Creer que una estrella que da vueltas en círculo en el plano del cielo muestra Doppler: solo se detecta la velocidad en la visual.

**Relacionados:** velocidad radial, corrimiento al rojo, espectroscopía.
📘 [B45](../../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md "Espectroscopía, fotometría y polarimetría"), [B29](../../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md "Astronomía temporal y exoplanetas"), [B74](../../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md "Estimación de órbitas y navegación espacial").

---

### Ecuación del cohete (Tsiolkovski)

**En una frase.** Relación entre el cambio de velocidad que logra un cohete y la fracción de su masa que es propelente.

**Cómo pensarlo.** Para acelerar, un cohete expulsa masa hacia atrás; cada kilo de propelente que se quema debe antes ser acelerado junto con la nave. Por eso la velocidad ganada crece solo con el **logaritmo** de la razón de masas: duplicar el Δv exige elevar al cuadrado esa razón. De ahí las etapas.

**Fórmula.** Δv = v_e ln(m₀ / m_f) = Isp g₀ ln(m₀ / m_f).

**Ejemplo.** Con Isp = 350 s y m₀/m_f = 5: Δv = 350 · 9,81 · ln 5 ≈ 5,5 km/s. Para llegar a órbita baja (≈ 9,4 km/s con pérdidas) con una sola etapa se necesitaría m₀/m_f ≈ 15: casi todo el cohete debería ser propelente.

**Error frecuente.** Usar masa total en lugar de masa seca final, o ignorar que la gravedad y el arrastre aumentan el Δv necesario.

**Relacionados:** delta-v, impulso específico, etapas.
📘 [B77](../../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B78](../../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial").

---

### Efecto invernadero

**En una frase.** Calentamiento de una superficie porque la atmósfera deja pasar la luz visible pero retiene parte de la radiación infrarroja que emite el suelo.

**Cómo pensarlo.** El suelo absorbe luz visible y la devuelve como infrarrojo. Ciertos gases (CO₂, vapor de agua, metano) absorben ese infrarrojo y lo reemiten en todas direcciones, parte hacia el suelo. El resultado: una superficie más caliente que la temperatura de equilibrio sin atmósfera.

**Ejemplo numérico.** Tierra: T_eq ≈ 255 K sin efecto invernadero, T_media ≈ 288 K: +33 K. Venus: T_eq ≈ 230 K, T_superficie ≈ 737 K: más de +500 K con 92 bar de CO₂.

**Error frecuente.** Confundirlo con la capa de ozono, o con "cristales de invernadero": son procesos físicos distintos.

**Relacionados:** albedo, temperatura de equilibrio, balance radiativo.
📘 [B54](../../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria"), [B57](../../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md "Observación terrestre y geociencias orbitales").

---

### Enana blanca

**En una frase.** Remanente denso de una estrella de masa baja o media que ya no fusiona y se enfría lentamente.

**Cómo pensarlo.** Tiene la masa del Sol en el tamaño de la Tierra. No la sostiene la fusión, sino la **presión de degeneración de los electrones**. Existe un límite de masa, el límite de Chandrasekhar (≈ 1,4 M☉), por encima del cual esa presión no basta y colapsa.

**Ejemplo.** Sirio B: M ≈ 1,0 M☉, R ≈ 0,008 R☉ ≈ 5 600 km; densidad media ≈ 3 × 10⁹ kg/m³ (una cucharadita pesaría toneladas).

**Error frecuente.** Pensar que una enana blanca es una "estrella apagada": brilla por calor residual durante miles de millones de años.

**Relacionados:** límite de Chandrasekhar, supernova tipo Ia, evolución estelar.
📘 [B24](../../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B27](../../programa/tronco-comun/B27-objetos-compactos-y-altas-energias.md "Objetos compactos y altas energías").

---

### Equinoccio y solsticio

**En una frase.** Los equinoccios son los dos momentos del año en que el Sol cruza el ecuador celeste; los solsticios, cuando se aleja más de él.

**Cómo pensarlo.** Por la inclinación del eje terrestre (≈ 23,4°), el Sol parece subir y bajar en declinación durante el año. En el equinoccio la declinación es 0° y día y noche duran casi lo mismo. En el solsticio es ±23,4°. El punto vernal (equinoccio de marzo) es el origen de la ascensión recta.

**Ejemplo.** En Santiago de Chile (33,4° S) el 21 de diciembre el Sol culmina a 90° − 33,4° + 23,4° = 80° de altura.

**Error frecuente.** Atribuir las estaciones a la distancia al Sol: la Tierra está más cerca en enero; las estaciones se deben a la inclinación.

**Relacionados:** eclíptica, oblicuidad, precesión, año tropical.
📘 [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica"), [B02](../../programa/tronco-comun/B02-historia-arqueoastronomia-y-culturas-del-cielo.md "Historia, arqueoastronomía y culturas del cielo").

---

### Espectro y espectroscopía

**En una frase.** El espectro es la luz repartida por longitud de onda; la espectroscopía es el análisis de ese reparto.

**Cómo pensarlo.** Un espectro tiene un **continuo** (por la temperatura), **líneas de absorción** (gas frío delante de una fuente caliente) y **líneas de emisión** (gas caliente). Cada elemento deja su huella a longitudes de onda precisas. De ahí se obtienen composición, temperatura, densidad, velocidad (Doppler) y campos magnéticos.

**Ejemplo.** La serie de Balmer del hidrógeno: Hα 656,3 nm; Hβ 486,1 nm. Su ancho y desplazamiento dan la velocidad y las condiciones del gas.

**Error frecuente.** Interpretar una sola línea sin considerar mezclas, ensanchamiento o desplazamiento.

**Relacionados:** Doppler, fotometría, resolución espectral.
📘 [B45](../../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md "Espectroscopía, fotometría y polarimetría"), [B32](../../programa/tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md "Atmósferas estelares y espectroscopía estelar cuantitativa").

---

### Estrella de neutrones y púlsar

**En una frase.** Remanente extremadamente denso de una estrella masiva; si gira y emite haces de radio visibles desde la Tierra, se observa como púlsar.

**Cómo pensarlo.** Una masa de 1,4 M☉ en ≈ 12 km de radio: densidad ≈ 10¹⁷ kg/m³. Se conserva el momento angular y el flujo magnético al colapsar: giran rápido y tienen campos de 10⁸–10¹⁵ T. Los haces barren el espacio como un faro.

**Ejemplo.** El púlsar del Cangrejo gira unas 30 veces por segundo (P ≈ 33 ms). Jocelyn Bell detectó el primero en 1967.

**Error frecuente.** Imaginar que "pulsan" por latidos: es rotación con un haz fijo en el cuerpo.

**Relacionados:** supernova, agujero negro, ondas gravitacionales.
📘 [B27](../../programa/tronco-comun/B27-objetos-compactos-y-altas-energias.md "Objetos compactos y altas energías"), [B28](../../programa/tronco-comun/B28-astronomia-multimensajero.md "Astronomía multimensajero").

---

### Exoplaneta

**En una frase.** Planeta que orbita una estrella distinta del Sol.

**Cómo pensarlo.** Casi nunca se ven directamente: se infieren por su efecto sobre la estrella. Los métodos principales son **tránsito** (la estrella se atenúa), **velocidad radial** (la estrella se tambalea por Doppler), **imagen directa**, **microlente** y **astrometría**. Cada método favorece planetas distintos, y el conjunto de planetas conocidos está sesgado por esos métodos.

**Ejemplo.** Un planeta tipo Tierra en 1 año alrededor de una estrella solar produce un tránsito de 84 ppm y un tirón de 9 cm/s: casi al límite de las técnicas actuales.

**Error frecuente.** Concluir que "los planetas gigantes calientes son los más comunes" porque son los más fáciles de detectar.

**Relacionados:** tránsito, velocidad radial, zona habitable.
📘 [B29](../../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md "Astronomía temporal y exoplanetas"), [B52](../../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios").

---

### Excentricidad

**En una frase.** Número que mide cuán alargada es una órbita: 0 es un círculo; entre 0 y 1, una elipse; 1, una parábola; mayor que 1, una hipérbola.

**Cómo pensarlo.** Define la forma, no el tamaño (eso lo hace el semieje mayor). Una órbita con e = 0 siempre va a la misma distancia; una con e alto pasa de cerca a lejos y la velocidad cambia mucho.

**Fórmula.** e = (r_a − r_p) / (r_a + r_p).

**Ejemplo.** Tierra e = 0,017; Mercurio 0,206; cometa Halley 0,967; transferencia a GEO ≈ 0,73.

**Error frecuente.** Creer que una excentricidad alta significa una órbita "grande".

**Relacionados:** semieje mayor, apoapsis, periapsis.
📘 [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental").

---

### Flujo y luminosidad

**En una frase.** La luminosidad (L) es la potencia total que emite un astro; el flujo (F) es la potencia que llega por unidad de área.

**Cómo pensarlo.** La luz se reparte en una esfera cada vez mayor, de modo que el flujo cae con el cuadrado de la distancia. Dos estrellas iguales vistas a distancias distintas parecen de brillos distintos: por eso se necesitan distancias para conocer su verdadera luminosidad.

**Fórmula.** F = L / (4π d²). Unidades: W/m².

**Ejemplo.** Constante solar: S = L☉ / (4π (1 UA)²) = 3,828 × 10²⁶ / (4π · (1,496 × 10¹¹)²) ≈ 1 361 W/m². A Marte (1,52 UA) llega 1361 / 1,52² ≈ 590 W/m².

**Error frecuente.** Confundir brillo aparente (flujo) con luminosidad (propiedad intrínseca).

**Relacionados:** magnitud, módulo de distancia, cuerpo negro.
📘 [B24](../../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B86](../../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md "Sistemas de potencia y energía espacial").

---

### Fotometría

**En una frase.** Medición del brillo de los astros.

**Cómo pensarlo.** Se cuenta la luz que llega en una banda de colores (U, B, V, R, I…) con un detector, se resta el cielo y se calibra con estrellas patrón. De las diferencias entre bandas salen los índices de color (temperatura). De la variación en el tiempo salen los tránsitos, las pulsaciones y las eclipses.

**Fórmula.** m₁ − m₂ = −2,5 log₁₀(F₁ / F₂).

**Ejemplo.** Una estrella que pasa de F₁ a 0,99 F₁ tiene Δm = −2,5 log₁₀ 0,99 = 0,011 mag (11 milimagnitudes).

**Error frecuente.** Olvidar la extinción atmosférica, que depende de la masa de aire (altura sobre el horizonte).

**Relacionados:** magnitud, curva de luz, extinción.
📘 [B45](../../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md "Espectroscopía, fotometría y polarimetría"), [B44](../../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md "Detectores y adquisición astronómica").

---

### Galaxia

**En una frase.** Conjunto enorme de estrellas, gas, polvo y materia oscura unido por la gravedad.

**Cómo pensarlo.** Hay espirales (con disco y brazos), elípticas (sin disco, estrellas viejas) e irregulares. La Vía Láctea es una espiral con ≈ 10¹¹ estrellas y un diámetro de ≈ 30 kpc. Las curvas de rotación muestran que la masa visible no basta: hay materia oscura.

**Ejemplo.** Andrómeda (M31) está a ≈ 0,78 Mpc (2,5 millones de años luz) y se acerca a ≈ 110 km/s.

**Error frecuente.** Confundir "universo" con "galaxia" y creer que todo lo que se ve en el cielo está fuera de la Vía Láctea: casi todas las estrellas visibles a simple vista son de nuestra galaxia.

**Relacionados:** materia oscura, curva de rotación, cúmulo.
📘 [B25](../../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md "Galaxias y medio interestelar"), [B38](../../programa/tronco-comun/B38-poblaciones-estelares-y-simulacion-de-galaxias.md "Poblaciones estelares y simulación de galaxias").

---

### Gravedad y peso

**En una frase.** La gravedad es la atracción entre masas; el peso es la fuerza con que un cuerpo es atraído.

**Cómo pensarlo.** La masa es una propiedad del objeto y no cambia. El peso depende de dónde esté: en la Luna pesa 1/6 que en la Tierra. En órbita se está en **caída libre** continua: por eso se flota, aunque la gravedad a 400 km sea casi 90 % de la superficial.

**Fórmula.** g = GM / r²; peso W = m g (N).

**Ejemplo.** Un astronauta de 80 kg: peso en la Tierra ≈ 785 N; en la Luna (g = 1,62 m/s²) ≈ 130 N; en la ISS (g ≈ 8,7 m/s²) el peso "verdadero" sería ≈ 696 N, pero su peso aparente es ≈ 0.

**Error frecuente.** Decir que en la ISS "no hay gravedad".

**Relacionados:** microgravedad, caída libre, parámetro gravitacional.
📘 [B05](../../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md "Física fundamental para el espacio"), [B105](../../programa/tronco-comun/B105-medicina-y-biologia-espacial.md "Medicina y biología espacial").

---

### Habitabilidad y zona habitable

**En una frase.** La zona habitable es la franja de distancias a una estrella donde un planeta podría tener agua líquida en su superficie.

**Cómo pensarlo.** Depende de la luminosidad de la estrella, del albedo y de la atmósfera del planeta. Es una condición necesaria, no suficiente: también cuentan el campo magnético, la presión, la composición y la actividad geológica. No dice que haya vida.

**Ejemplo.** Para el Sol, la zona habitable conservadora va de ≈ 0,95 a ≈ 1,7 UA (según el modelo). En una enana roja de 0,1 L☉, a ≈ 0,3 UA.

**Error frecuente.** Equiparar "zona habitable" con "planeta habitable".

**Relacionados:** exoplaneta, efecto invernadero, astrobiología.
📘 [B56](../../programa/tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md "Astrobiología y vida extraterrestre"), [B29](../../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md "Astronomía temporal y exoplanetas").

---

### Hohmann (transferencia)

**En una frase.** La transferencia entre dos órbitas circulares coplanares que usa la menor energía con dos impulsos.

**Cómo pensarlo.** Se sube a una elipse que toca la órbita de partida en el periapsis y la de llegada en el apoapsis. Un primer impulso en el punto de partida alarga la órbita; un segundo en el punto de llegada la circulariza. Es lenta pero económica.

**Fórmulas.** Δv₁ = √(GM/r₁) (√(2r₂/(r₁+r₂)) − 1); Δv₂ = √(GM/r₂) (1 − √(2r₁/(r₁+r₂))); tiempo de vuelo = π √(a³/GM) con a = (r₁+r₂)/2.

**Ejemplo.** LEO (6 678 km) → GEO (42 164 km): Δv₁ ≈ 2,43 km/s, Δv₂ ≈ 1,46 km/s, total ≈ 3,89 km/s, tiempo ≈ 5,3 h.

**Error frecuente.** Aplicarla a órbitas no coplanares o con impulsos largos sin corregir.

**Relacionados:** delta-v, vis-viva, ventana de lanzamiento.
📘 [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B75](../../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias").

---

### Impulso específico (Isp)

**En una frase.** La eficiencia de un propulsor: cuánto impulso se obtiene por unidad de peso de propelente consumido.

**Cómo pensarlo.** Un Isp alto significa que cada kilo de propelente da más empuje durante más tiempo; equivale a una velocidad de escape de gases mayor. Los motores químicos están en 250–450 s; los iónicos, 1 500–4 000 s, pero con empuje muy pequeño.

**Fórmula.** Isp = F / (ṁ g₀) = v_e / g₀. Unidades: s.

**Ejemplo.** Motor de hidrógeno–oxígeno: Isp ≈ 450 s → v_e ≈ 4,4 km/s. Motor iónico: Isp ≈ 3 000 s → v_e ≈ 29 km/s.

**Error frecuente.** Quedarse con el Isp más alto: el empuje también cuenta. Un motor iónico no puede despegar de la Tierra.

**Relacionados:** ecuación del cohete, empuje, propulsión eléctrica.
📘 [B78](../../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial").

---

### Inclinación orbital

**En una frase.** El ángulo entre el plano de la órbita y un plano de referencia (en la Tierra, el ecuador).

**Cómo pensarlo.** Define cuánto cubre la órbita. Con inclinación 0° la nave sobrevuela solo el ecuador; con 90° pasa por los polos. Un satélite no puede sobrevolar latitudes mayores que su inclinación (o 180° − i si es retrógrada).

**Ejemplo.** ISS: 51,6°; órbita heliosíncrona típica: ≈ 98°; geoestacionaria: 0°. Lanzar desde Kourou (5° N) permite alcanzar 5° sin maniobra de cambio de plano.

**Error frecuente.** Olvidar que cambiar la inclinación en órbita es muy costoso en Δv.

**Relacionados:** elementos orbitales, ascensión del nodo, sincronía solar.
📘 [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B77](../../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada").

---

### Interferometría

**En una frase.** Técnica que combina la señal de varios telescopios para obtener la resolución de uno del tamaño de su separación.

**Cómo pensarlo.** Cada par de antenas mide un patrón de interferencia que codifica un detalle del objeto. Al combinar muchos pares se reconstruye una imagen. La resolución depende de la **línea de base** B (distancia entre antenas), no del diámetro de cada una.

**Fórmula.** θ ≈ λ / B.

**Ejemplo.** El Event Horizon Telescope: λ = 1,3 mm, B ≈ 10 000 km → θ ≈ 1,3 × 10⁻³ / 10⁷ = 1,3 × 10⁻¹⁰ rad ≈ 27 µas, suficiente para resolver la sombra de M87*.

**Error frecuente.** Pensar que se obtiene la luz de una apertura grande: se pierde sensibilidad por la falta de área colectora.

**Relacionados:** radioastronomía, línea de base, síntesis de apertura.
📘 [B46](../../programa/tronco-comun/B46-radioastronomia-e-interferometria.md "Radioastronomía e interferometría"), [B51](../../programa/tronco-comun/B51-interferometria-avanzada-y-reduccion-de-datos-de-radio.md "Interferometría avanzada y reducción de datos de radio").

---

### Kepler (leyes de)

**En una frase.** Tres reglas empíricas del movimiento planetario: órbitas elípticas, áreas iguales en tiempos iguales y T² ∝ a³.

**Cómo pensarlo.** (1) El Sol ocupa un foco de la elipse. (2) El radio vector barre áreas iguales en tiempos iguales: la conservación del momento angular, el planeta va más rápido cerca del Sol. (3) El cuadrado del período es proporcional al cubo del semieje: T² = (4π² / GM) a³.

**Ejemplo.** Marte: a = 1,524 UA → T = 1,524^1,5 ≈ 1,88 años.

**Error frecuente.** Aplicar la tercera ley con unidades mezcladas; en unidades de años y UA, T² = a³ solo para el Sol.

**Relacionados:** excentricidad, momento angular, problema de dos cuerpos.
📘 [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B05](../../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md "Física fundamental para el espacio").

---

### Lagrange (puntos de)

**En una frase.** Cinco posiciones, en un sistema de dos cuerpos masivos, donde un cuerpo pequeño mantiene su posición relativa a ellos.

**Cómo pensarlo.** En el sistema rotante de, digamos, Sol–Tierra, la gravedad de ambos y la fuerza centrífuga se compensan en cinco puntos. L1, L2 y L3 están sobre la línea que une los dos cuerpos y son inestables (hace falta corregir la posición); L4 y L5 forman triángulos equiláteros y son estables si la razón de masas es grande.

**Ejemplo.** El telescopio James Webb orbita L2 Sol–Tierra, a ≈ 1,5 millones de km; SOHO está en L1, que ve el Sol sin interrupción. Los asteroides troyanos de Júpiter están en L4 y L5.

**Error frecuente.** Pensar que son "lugares sin gravedad".

**Relacionados:** problema de tres cuerpos restringido, órbitas halo, esfera de Hill.
📘 [B73](../../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md "Mecánica celeste, resonancias y caos"), [B76](../../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md "Dinámica cislunar y operaciones de proximidad").

---

### Longitud de onda y frecuencia

**En una frase.** La longitud de onda (λ) es la distancia entre dos crestas; la frecuencia (ν) es el número de crestas por segundo.

**Cómo pensarlo.** Para la luz y toda la radiación electromagnética, λ ν = c. Más frecuencia significa menor longitud de onda y más energía por fotón (E = h ν). Todo el espectro (radio, microondas, infrarrojo, visible, UV, X, gamma) es lo mismo: solo cambia λ.

**Ejemplo.** Visible: 400–700 nm. Línea de hidrógeno de 21 cm: ν = c/λ ≈ 1 420 MHz. Rayos X de 1 nm: E ≈ 1,24 keV.

**Error frecuente.** Confundir frecuencia con velocidad: la luz viaja siempre a c en el vacío; cambian λ y ν.

**Relacionados:** espectro, energía del fotón, Doppler.
📘 [B05](../../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md "Física fundamental para el espacio"), [B45](../../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md "Espectroscopía, fotometría y polarimetría").

---

### Luminosidad

Ver [Flujo y luminosidad](#flujo-y-luminosidad).

---

### Lente gravitacional

**En una frase.** Desviación de la luz por la gravedad de una masa, que puede magnificar o distorsionar la imagen de un objeto de fondo.

**Cómo pensarlo.** La relatividad general dice que la masa curva el espacio-tiempo y la luz sigue esa curvatura. Una masa intermedia (galaxia, cúmulo) actúa como lente: puede formar arcos, anillos de Einstein o imágenes múltiples. Sirve para medir masa (incluida la materia oscura) y para ver galaxias muy lejanas.

**Fórmula.** Ángulo de desviación para un rayo que pasa a distancia b de una masa M: α = 4GM / (c² b). Para el Sol en su borde: 1,75″, medidos en el eclipse de 1919.

**Error frecuente.** Considerarla un efecto óptico "de ilusión": es un fenómeno físico medible.

**Relacionados:** relatividad general, materia oscura, anillo de Einstein.
📘 [B26](../../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología"), [B39](../../programa/tronco-comun/B39-relatividad-general-avanzada.md "Relatividad general avanzada").

---

[← A – C](esencial-a-c.md) · [Índice del glosario esencial](README.md) · [Siguiente: M – Z →](esencial-m-z.md)
