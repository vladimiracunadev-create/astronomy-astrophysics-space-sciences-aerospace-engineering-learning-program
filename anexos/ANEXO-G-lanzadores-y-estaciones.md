# Anexo G · Lanzadores, estaciones espaciales y puertos espaciales

[⬅️ Anexo F](ANEXO-F-telescopios-y-observatorios.md) · [Índice de anexos](README.md)

Llegar al espacio es un problema de **velocidad** (unos 7,8 km/s para una órbita baja) y de **masa**: la mayor parte de un cohete es propelente. Este anexo cuenta la historia de los lanzadores, de las estaciones que se habitaron y de los lugares desde donde se despega, siempre con la pregunta: **¿qué restricción física o de diseño explica esta solución?**

> **Estado del texto.** Síntesis histórica propia, cifras redondeadas, pendiente de revisión disciplinar y de contraste con fuentes primarias (nivel E0). Capacidades y estados operativos de lanzadores comerciales cambian rápido: confirma en la fuente del operador.

---

## 1. Ideas físicas que organizan todo

- **Ecuación del cohete (Tsiolkovski):** Δv = v_e · ln(m₀ / m_f). Duplicar la velocidad requiere aumentar la masa de combustible de forma exponencial.
- **Etapas:** descartar masa muerta a mitad de camino mejora la razón de masas.
- **Impulso específico (Isp):** eficiencia del propulsor; los motores de hidrógeno-oxígeno son más eficientes, los de queroseno-oxígeno más densos y baratos.
- **Relación empuje-peso:** el cohete debe superar su peso para despegar.
- **Pérdidas:** gravedad y arrastre atmosférico exigen unos 9–10 km/s de Δv reales para llegar a órbita baja.

📘 [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial"), [B79](../programa/tronco-comun/B79-fluidos-termodinamica-y-aerotermodinamica-de-propulsion.md "Fluidos, termodinámica y aerotermodinámica de propulsión").

---

## 2. Familias históricas de lanzadores

### V-2 (Alemania, 1942–1945)
Primer misil balístico de largo alcance; alcanzó el espacio suborbital. Su tecnología sirvió de base a los programas de EE. UU. y la URSS tras la guerra. Su producción usó trabajo forzado, algo que forma parte de su historia. 📘 [B132](../programa/tronco-comun/B132-historia-y-arqueoastronomia-aplicadas.md "Historia y arqueoastronomía aplicadas").

### R-7 / Soyuz (URSS / Rusia, desde 1957)
Misil intercontinental convertido en lanzador de Sputnik y Vostok. La familia Soyuz es la de más lanzamientos en la historia; su diseño de cuatro propulsores laterales y una etapa central es reconocible. Sigue usándose para llevar tripulación. 📘 [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada").

### Redstone, Atlas, Titan y Saturn (EE. UU., 1950–1970)
Mercury voló con Redstone y Atlas; Gemini con Titan II; **Saturn V** (111 m de altura, empuje al despegue cercano a 34 MN) llevó a Apollo a la Luna: 13 lanzamientos entre 1967 y 1973, ningún fallo que perdiera tripulación. 📘 [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial"), [B83](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md "Ingeniería de sistemas y diseño de misiones").

### Transbordador espacial (EE. UU., 1981–2011)
Orbitador reutilizable con tanque externo y dos propulsores sólidos. 135 vuelos; el costo y los tiempos de reacondicionamiento fueron mayores de lo previsto. 📘 [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada").

### Proton (URSS / Rusia, desde 1965)
Lanzador pesado de propelentes hipergólicos, usado en módulos de estaciones y satélites geoestacionarios. 📘 [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial").

### Ariane y Vega (Europa)
Ariane 1 (1979) abrió el mercado comercial europeo; Ariane 5 (primer vuelo en 1996 con fallo por un error de software de reutilización de código) voló hasta 2023; Ariane 6 debutó en 2024; Vega lleva satélites pequeños. El fallo de Ariane 5 es un caso clásico de **verificación de software**. 📘 [B88](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md "Aviónica y software crítico espacial"), [B23](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md "Verificación y validación de software científico").

### Larga Marcha (China, desde 1970)
Familia de lanzadores; la serie CZ-5 y CZ-7 llevó módulos de Tiangong y misiones lunares. 📘 [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada").

### PSLV y GSLV (India), H-IIA/H3 (Japón), Nuri (Corea del Sur)
Cada país construyó una familia a su ritmo; el PSLV puso 104 satélites en un lanzamiento (2017). 📘 [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial").

### Falcon 9 y Falcon Heavy (SpaceX)
Reutilización de la primera etapa: el primer aterrizaje de un propulsor orbital ocurrió en diciembre de 2015, y las reutilizaciones sucesivas bajaron el costo por kilo. Falcon Heavy voló en 2018. **Starship** es un sistema totalmente reutilizable en desarrollo, con pruebas en curso. 📘 [B124](../programa/tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md "Industria, economía, ética y proyectos espaciales"), [B126](../programa/tronco-comun/B126-financiamiento-de-proyectos-y-negocios-espaciales.md "Financiamiento de proyectos y negocios espaciales").

### New Shepard, Electron, Vulcan y otros
Vuelos suborbitales turísticos, lanzamientos dedicados a satélites pequeños, cohetes pesados nuevos. 📘 [B124](../programa/tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md "Industria, economía, ética y proyectos espaciales"), [B125](../programa/tronco-comun/B125-creacion-y-operacion-de-empresas-espaciales.md "Creación y operación de empresas espaciales").

### SLS (EE. UU.)
Cohete de altísimo empuje para el programa Artemis; voló por primera vez el 16 de noviembre de 2022. 📘 [B76](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md "Dinámica cislunar y operaciones de proximidad").

---

## 3. Estaciones espaciales

| Estación | Años | País | Rasgo |
|---|---|---|---|
| Salyut 1 | 1971 | URSS | Primera estación; la tripulación de Soyuz 11 murió al volver |
| Skylab | 1973–1974 (reentró 1979) | EE. UU. | Taller y observatorio solar; reparó con una sombrilla tras daño al lanzamiento |
| Mir | 1986–2001 | URSS / Rusia | Modular; estancias de más de un año; sobrevivió a incendios y colisiones |
| ISS | 1998– | EE. UU., Rusia, Europa, Japón y Canadá | Laboratorio de unas 420 toneladas y casi el largo de una cancha de fútbol, ocupado de forma continua desde noviembre de 2000 |
| Tiangong | 2021– | China | Módulos Tianhe, Wentian, Mengtian |

- **ISS en síntesis:** ocupa una órbita a unos 400 km con inclinación de 51,6°, da una vuelta a la Tierra cada ~ 92 minutos y alberga alrededor de siete personas. Se usa para fisiología, materiales, biología y observación de la Tierra. Su fin de vida está previsto a comienzos de la década de 2030 con una reentrada controlada.
- **Estaciones comerciales:** varias empresas desarrollan sucesores privados.
- **Enseña:** soporte vital, energía, térmica, mantenimiento y logística. 📘 [B105](../programa/tronco-comun/B105-medicina-y-biologia-espacial.md "Medicina y biología espacial"), [B106](../programa/tronco-comun/B106-habitats-espaciales-y-soporte-vital.md "Hábitats espaciales y soporte vital"), [B100](../programa/tronco-comun/B100-logistica-y-cadena-de-suministro-extraterrestre.md "Logística y cadena de suministro extraterrestre").

---

## 4. Puertos espaciales: por qué ahí

La rotación terrestre ayuda más cerca del ecuador, y el sitio debe tener mar o desierto despoblado hacia donde cae la etapa o un cohete fallido.

| Puerto | Lugar | Nota |
|---|---|---|
| Baikonur | Kazajistán | Mayor puerto histórico (Sputnik, Gagarin) |
| Cabo Cañaveral / Kennedy | Florida, EE. UU. | Apollo, transbordador, comerciales |
| Vandenberg | California, EE. UU. | Órbitas polares |
| Kourou (CSG) | Guayana Francesa | Latitud ≈ 5° N, ventaja para órbita geoestacionaria; Ariane y Vega |
| Tanegashima y Uchinoura | Japón | Lanzadores japoneses |
| Jiuquan, Taiyuan, Xichang, Wenchang | China | Wenchang, isla de Hainan, para lanzadores pesados |
| Satish Dhawan | India | Lanzadores indios |
| Alcântara | Brasil | Muy cerca del ecuador |
| Mahia y otros | Nueva Zelanda | Lanzadores pequeños |

📘 [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B121](../programa/tronco-comun/B121-regulacion-nacional-de-actividades-espaciales.md "Regulación nacional de actividades espaciales").

---

## 5. Reentrada y aterrizaje

- **Balística:** cápsulas Vostok, Mercury, Soyuz (sufren hasta 4–8 g).
- **Planeo:** transbordador, con protección térmica de losetas.
- **Escudos ablativos:** Apollo y Orion; el material se erosiona y se lleva el calor.
- **Aterrizaje propulsado:** los propulsores de SpaceX y las cápsulas de Marte con "grúa aérea" (Curiosity, Perseverance).

📘 [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B85](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md "Gestión térmica y entorno espacial").

---

## 6. A fondo: anatomía de un lanzamiento

Un lanzamiento dura unos nueve minutos hasta la órbita, pero esconde una secuencia exacta de decisiones. Se describe un perfil típico de un cohete de dos etapas con primera etapa recuperable; los tiempos son del orden de magnitud y varían con la misión.

### 6.1 Línea de tiempo (aproximada)

| Tiempo | Evento | Qué ocurre y por qué |
|---|---|---|
| T−10 s a T−0 | Encendido | Los motores se encienden y el sistema verifica empuje antes de soltar el cohete |
| T+0 | Despegue | El empuje (≈ 7,6 MN en un cohete de 550 t) supera el peso: relación empuje-peso ≈ 1,4 |
| T+10 s | Giro programado | Se inclina para ganar velocidad horizontal |
| ≈ T+70 s | Max-Q | Máxima presión dinámica; se reduce el empuje para limitar la carga |
| ≈ T+2:30 | Corte de motores de la 1ª etapa | Ya ≈ 2 km/s y ≈ 70 km de altura; combustible casi agotado |
| ≈ T+2:35 | Separación y encendido de la 2ª etapa | Se descarta masa muerta: es la razón de usar etapas |
| ≈ T+3:30 | Separación de la cofia | A esa altura el aire ya es tan tenue que no daña la carga |
| ≈ T+8:30 | Corte de la 2ª etapa | Velocidad orbital ≈ 7,8 km/s |
| ≈ T+9 min | Separación de la carga útil | Libera el satélite en su órbita |

La primera etapa puede volver a la Tierra y aterrizar con un encendido de frenado; recuperar equivale a gastar propelente adicional y reducir la carga útil, con un ahorro económico al reutilizarla.

### 6.2 Dónde se va el Δv

Para llegar a órbita baja a 400 km hacen falta unos **9,3–9,5 km/s** de Δv, aunque la velocidad orbital es solo ≈ 7,7 km/s:

| Componente | Valor aproximado |
|---|---|
| Velocidad orbital | ≈ 7,7 km/s |
| Pérdidas por gravedad (se gasta empuje en contrarrestar el peso mientras se sube) | ≈ 1,2–1,8 km/s |
| Pérdidas por arrastre atmosférico | ≈ 0,1–0,2 km/s |
| Ayuda de la rotación terrestre (hacia el este) | − hasta ≈ 0,46 km/s |

**La ayuda de la rotación** depende de la latitud del puerto: v = 465 m/s × cos φ. Kourou (5° N): ≈ 463 m/s; Cabo Cañaveral (28,5° N): ≈ 408 m/s; Vandenberg (34,7° N): ≈ 382 m/s. Por eso los puertos cercanos al ecuador son ventajosos para órbitas ecuatoriales.

### 6.3 Por qué casi todo el cohete es combustible

Un cohete de ≈ 550 t que pone ≈ 22 t en órbita baja (versión sin recuperar) tiene una fracción de carga útil de ≈ 4 %. La ecuación de Tsiolkovski explica por qué: con un Isp medio de 300 s, Δv = 9,4 km/s requiere una razón de masas e^(9 400 / (300 · 9,81)) ≈ 24 en una sola etapa; con dos etapas se reparte en razones menores y la carga útil crece.

**Ejercicio resuelto.** ¿Qué razón de masas necesita una sola etapa para Δv = 9,4 km/s con Isp = 300 s? v_e = 300 · 9,81 = 2 943 m/s → m₀/m_f = e^(9 400 / 2 943) = e^3,19 ≈ **24**. Comprobación: `calc "exp(9400/(300*g0))"`.

### 6.4 Seguridad de alcance

- Se calcula la **zona de caída** de etapas y escombros; las autoridades cierran espacio aéreo y marítimo.
- Un **sistema de terminación de vuelo** destruye el cohete si se sale de la trayectoria permitida.
- Se fijan **criterios de lanzamiento** (meteorológicos, de seguridad y técnicos) que cualquier responsable puede detener.

### 6.5 Ejercicios

1. Calcula la ayuda de rotación en Baikonur (45,6° N).
2. ¿Qué pasaría con la razón de masas si el Isp subiera a 450 s?
3. Explica por qué la cofia se separa cuando ya hay poco aire y no antes.

📘 [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial"), [B84](../programa/tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md "Estructuras, materiales y fabricación espacial"), [B110](../programa/tronco-comun/B110-emergencias-y-seguridad-de-tripulacion.md "Emergencias y seguridad de tripulación").

[⬅️ Anexo F](ANEXO-F-telescopios-y-observatorios.md) · [Índice de anexos](README.md) · [Siguiente: Anexo H · Cronología →](ANEXO-H-cronologia.md)
