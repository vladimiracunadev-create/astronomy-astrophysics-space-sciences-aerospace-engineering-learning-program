# Anexo N · Exoplanetas y astrobiología a fondo

[⬅️ Anexo M](ANEXO-M-estrellas-galaxias-y-cosmologia.md) · [Índice de anexos](README.md)

Desde 1995, la pregunta «¿hay otros mundos?» pasó de la filosofía a la medición. Este anexo explica **cómo se detectan los planetas de otras estrellas**, qué hemos aprendido de ellos, **qué significa que un planeta sea habitable** y cómo se busca vida con rigor científico. Incluye cálculos para comprobar las ideas con la [calculadora](../herramientas/calculadora_cientifica.py).

> **Estado del texto.** Síntesis propia con cifras redondeadas, pendiente de revisión disciplinar y de contraste con fuentes primarias (nivel E0). El número de exoplanetas confirmados y muchas detecciones de atmósferas se actualizan constantemente y algunas son motivo de debate: confirma en los archivos oficiales (por ejemplo, el NASA Exoplanet Archive y la Enciclopedia de Planetas Extrasolares).

---

## 1. Cómo se detecta un planeta que no se ve

Un planeta es un millón o mil millones de veces más débil que su estrella y está pegado a ella en el cielo. Casi siempre se detecta por su **efecto** sobre la estrella.

| Método | Qué mide | Favorece | Limitación |
|---|---|---|---|
| **Tránsito** | Caída de brillo cuando el planeta pasa por delante | Planetas grandes, cercanos a su estrella | Solo si la órbita está de canto |
| **Velocidad radial** | Vaivén de la estrella por efecto Doppler | Planetas masivos y cercanos | Da la masa mínima (m sen i) |
| **Imagen directa** | Luz del planeta con coronógrafo | Planetas jóvenes, grandes y lejanos | Contraste extremo |
| **Microlente gravitacional** | Aumento de brillo cuando el sistema pasa delante de otra estrella | Planetas lejanos de su estrella; incluso errantes | Evento único, no repetible |
| **Astrometría** | Pequeño movimiento de la estrella en el cielo | Planetas masivos a distancia | Requiere precisión extrema (Gaia) |
| **Cronometría** | Variación en la señal periódica (púlsares, pulsaciones) | Casos especiales | Pocos objetos |

**Cifras de referencia:**
- Un planeta como Júpiter (R = 0,1 R☉) eclipsa ≈ **1 %** del brillo de una estrella solar.
- Un planeta como la Tierra eclipsa ≈ **0,008 %** (84 ppm) y tira de su estrella con ≈ **9 cm/s**.
- Más de **5 800 planetas** confirmados al momento de redactar este texto, en más de 4 000 sistemas.

### Fórmulas clave

- **Profundidad del tránsito:** δ = (R_p / R_*)².
- **Probabilidad geométrica de tránsito:** ≈ R_* / a.
- **Semiamplitud de la velocidad radial:** K ≈ 28,4 m/s × (M_p sen i / M_Júpiter) × (P / 1 año)^(−1/3) × (M_* / M☉)^(−2/3).

### Ejercicios
1. **Tránsito en una estrella pequeña.** Un planeta del tamaño de la Tierra frente a una enana roja de 0,12 R☉ (como TRAPPIST-1). *Solución:* R_Tierra / R_* = 6 371 / (0,12 × 695 700) = 0,0763; δ = 0,0763² ≈ **0,58 %**, unas 70 veces mayor que frente al Sol: por eso las enanas rojas son tan buenos blancos.
2. **Velocidad radial.** ¿Qué K produce Júpiter sobre el Sol? *Solución:* con M = M_J, P = 11,86 años: K = 28,4 × (11,86)^(−1/3) ≈ **12,5 m/s**. Para la Tierra, K ≈ **0,09 m/s**.
3. **Probabilidad de tránsito.** Una Tierra a 1 UA del Sol: R_* / a = 6,957 × 10⁸ / 1,496 × 10¹¹ ≈ **0,46 %**. Por eso hay que mirar miles de estrellas.

📘 [B29](../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md "Astronomía temporal y exoplanetas"), [B52](../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios").

---

## 2. Qué hemos encontrado

### 2.1 Una historia en fechas
- **1992:** primeros planetas, alrededor de un púlsar (Wolszczan y Frail).
- **1995:** **51 Pegasi b**, primer planeta alrededor de una estrella de tipo solar (Mayor y Queloz): un «Júpiter caliente» con un período de 4,2 días. Nadie lo esperaba, y obligó a revisar las teorías de formación (los planetas migran).
- **2009–2018:** **Kepler** vigila una región del cielo y descubre miles de planetas por tránsito. Muestra que los planetas son habituales y que los más comunes son de tamaño entre la Tierra y Neptuno, un tipo que **no existe en nuestro sistema**.
- **2018–:** **TESS** busca planetas cerca del Sol; **JWST** (desde 2022) analiza atmósferas.

### 2.2 El zoo de planetas
- **Júpiteres calientes:** gigantes con períodos de pocos días.
- **Supertierras y minineptunos (1–4 R⊕):** los más abundantes. Existe un «valle» de radios (≈ 1,5–2 R⊕) que separa planetas rocosos de los envueltos en gas: sugiere pérdida de atmósfera por la radiación de la estrella.
- **Planetas con órbitas muy excéntricas o inclinadas:** evidencia de interacciones dinámicas.
- **Planetas errantes:** sin estrella, detectados por microlente.
- **Sistemas compactos:** TRAPPIST-1 tiene siete planetas rocosos en órbitas tan cercanas que cabrían dentro de la órbita de Mercurio; a ≈ 12 pc.

**Lección:** la diversidad supera lo que se imaginó con nuestro sistema como único ejemplo. También hay un **sesgo de detección**: vemos más lo fácil de ver.

### 2.3 Atmósferas
El espectro de transmisión (la luz que atraviesa el borde de la atmósfera durante el tránsito) revela gases. JWST detectó dióxido de carbono en el planeta WASP-39 b (2022), la primera detección clara de CO₂ en la atmósfera de un exoplaneta. La señal en un Júpiter caliente es ≈ 100 ppm; en un planeta terrestre, ≈ 0,2 ppm, aún fuera de alcance salvo en casos favorables.

📘 [B29](../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md "Astronomía temporal y exoplanetas"), [B52](../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B54](../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria").

---

## 3. Habitabilidad: qué significa y qué no

### 3.1 La zona habitable
Franja de órbitas donde un planeta podría tener agua líquida en su superficie. Para estrellas distintas del Sol, la escala sigue la luminosidad: d ≈ √(L/L☉) × (0,95 a 1,67) UA como primera aproximación.

**Ejemplo.** Próxima Centauri tiene L ≈ 0,0017 L☉: la zona habitable queda en √0,0017 × (0,95–1,67) ≈ **0,04–0,07 UA**. Próxima b orbita a 0,049 UA con un período de 11,2 días, dentro de esa franja, pero la estrella emite llamaradas intensas y el planeta probablemente está acoplado por marea (una cara siempre al día).

### 3.2 Lo que la zona habitable no dice
- Que el planeta **tenga** atmósfera o agua.
- Que la atmósfera tenga presión suficiente.
- Que su estrella sea tranquila.
- Que haya un campo magnético o geología activa.
- Que exista vida.

La habitabilidad es una **condición necesaria, no suficiente**.

### 3.3 Ingredientes de la vida (tal como la conocemos)
1. **Un solvente líquido** (agua).
2. **Energía** (luz, química).
3. **Elementos** (C, H, N, O, P, S).
4. **Estabilidad en el tiempo** (millones a miles de millones de años).

### 3.4 Extremófilos: los límites de la vida
Organismos que viven en condiciones que antes se consideraban imposibles: bacterias en fuentes hidrotermales a > 100 °C (el récord de temperatura ronda los 122 °C), microbios en ácidos de pH cercano a 0, en hielo, sal, subsuelo profundo y en el desierto de Atacama. **Enseña:** la vida puede ser más resistente que lo que se creía, lo que amplía los lugares donde podría existir.

📘 [B56](../programa/tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md "Astrobiología y vida extraterrestre"), [B64](../programa/tronco-comun/B64-extremofilos-y-limites-de-la-vida.md "Extremófilos y límites de la vida").

---

## 4. Buscar vida con método

### 4.1 Biosignaturas
Señales que sugieren vida: gases en desequilibrio (por ejemplo O₂ y CH₄ juntos), patrones químicos, estructuras. Cada una puede tener una explicación **abiótica** (falso positivo). El criterio es que una afirmación extraordinaria exige evidencia múltiple e independiente.

### 4.2 Los experimentos de Viking (1976)
Tres experimentos buscaron metabolismo en suelo de Marte. Uno dio una señal inicialmente interpretada como positiva y, al no detectarse materia orgánica, se interpretó después como una reacción química del suelo (se descubrieron percloratos años más tarde). **Lección:** una prueba de vida debe ser concluyente y coherente con otras mediciones.

### 4.3 Dónde buscar en el Sistema Solar
- **Marte:** rastros fósiles en rocas (Perseverance recoge muestras para un posible retorno).
- **Europa y Encélado:** océanos bajo el hielo.
- **Titán:** química orgánica compleja; posible vida muy distinta.

### 4.4 La ecuación de Drake
Frank Drake propuso (1961) organizar nuestra ignorancia: N = R* · f_p · n_e · f_l · f_i · f_c · L, donde N es el número de civilizaciones detectables en la galaxia.

**Ejemplo ilustrativo (valores inventados):** R* = 1,5 estrellas/año, f_p = 1, n_e = 0,2, f_l = 0,1, f_i = 0,1, f_c = 0,1, L = 10 000 años → N = 1,5 × 1 × 0,2 × 0,1 × 0,1 × 0,1 × 10 000 = **3**. Los primeros factores hoy se conocen mejor (R*, f_p); los otros siguen siendo suposiciones.

**Enseña:** la ecuación no predice; sirve para identificar qué hay que medir.

### 4.5 La paradoja de Fermi y la búsqueda de señales (SETI)
Si la vida inteligente fuese común, ¿dónde está? Hay muchas respuestas posibles (rara, efímera, silenciosa, lejos). La búsqueda de señales de radio y de «tecnofirmas» se ha hecho en una fracción minúscula del espacio de posibilidades. La señal «Wow!» (1977) nunca se repitió y sigue sin explicación.

### 4.6 Protección planetaria
Para no contaminar otros mundos (y no traer organismos a la Tierra) las misiones siguen categorías de protección planetaria (COSPAR). Las que visitan lugares de interés para la vida deben esterilizar la nave; las que traen muestras exigen contención.

📘 [B56](../programa/tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md "Astrobiología y vida extraterrestre"), [B63](../programa/tronco-comun/B63-exploracion-in-situ-y-analisis-de-muestras-planetarias.md "Exploración in situ y análisis de muestras planetarias"), [B119](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md "Derecho, seguridad y geopolítica espacial").

---

## 5. Preguntas para discutir

1. ¿Por qué el método de tránsito favorece los planetas cercanos a su estrella?
2. ¿Qué diferencia hay entre un planeta «en la zona habitable» y un planeta «habitable»?
3. ¿Qué evidencias necesitarías para afirmar que una atmósfera tiene una biosignatura?
4. ¿Qué implicaría descubrir vida microbiana en Marte? ¿Y vida inteligente?
5. ¿Cómo debería una misión equilibrar la búsqueda de vida con la protección planetaria?

[⬅️ Anexo M](ANEXO-M-estrellas-galaxias-y-cosmologia.md) · [Índice de anexos](README.md)
