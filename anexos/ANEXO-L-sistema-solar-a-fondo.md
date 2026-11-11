# Anexo L · El Sistema Solar a fondo

[⬅️ Anexo K](ANEXO-K-perfiles-a-fondo.md) · [Índice de anexos](README.md)

Este anexo recorre el Sistema Solar como un **sistema físico**: qué lo forma, cómo se organizan sus cuerpos, qué los distingue y qué sabemos de cada uno gracias a las misiones descritas en los [anexos B](ANEXO-B-misiones-espaciales.md) y [E](ANEXO-E-satelites-y-sondas.md). No es un catálogo: cada sección explica **por qué** los planetas son como son y deja cálculos que puedes repetir con la [calculadora](../herramientas/calculadora_cientifica.py).

> **Estado del texto.** Síntesis propia con cifras redondeadas (valores de referencia de la literatura y de las resoluciones de la UAI), pendiente de revisión disciplinar y de contraste con fuentes primarias (nivel E0). Los datos de lunas y objetos menores cambian con nuevos descubrimientos: confirma en la fuente oficial (NASA/JPL, ESA, UAI) antes de citarlos.

---

## 1. Cómo se formó: una historia en cinco pasos

1. **Una nube de gas y polvo** colapsó por su propia gravedad hace unos **4 567 millones de años** (edad de los meteoritos más antiguos).
2. **Un disco protoplanetario** se formó porque la nube conservaba su momento angular: al contraerse giró más rápido y se aplanó.
3. **El Sol se encendió** en el centro y concentró el 99,86 % de la masa del sistema.
4. **Los granos de polvo se pegaron** hasta formar planetesimales de kilómetros, que crecieron por colisiones hasta formar protoplanetas.
5. **La línea de nieve (≈ 3 UA)** separó dos mundos: cerca del Sol solo sobrevivieron rocas y metales (planetas rocosos); más lejos, el hielo ayudó a formar núcleos grandes capaces de atrapar hidrógeno y helio (gigantes).

**Pruebas:** los planetas giran en el mismo sentido y casi en el mismo plano (herencia del disco); la edad de los meteoritos coincide con la del Sol; los discos protoplanetarios se observan en otras estrellas jóvenes.

**Lo que aún se discute:** cómo crecen los núcleos de los gigantes antes de que el gas se disipe (acreción de guijarros), cuánto migraron Júpiter y Saturno (modelos como el «Gran giro» de Júpiter) y el origen del agua terrestre.

📘 [B52](../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B55](../programa/tronco-comun/B55-astroquimica-y-geoquimica-extraterrestre.md "Astroquímica y geoquímica extraterrestre").

---

## 2. Visión de conjunto

| Cuerpo | Distancia al Sol (UA) | Radio ecuatorial (km) | Masa (masas terrestres) | Período orbital | Rasgo distintivo |
|---|---|---|---|---|---|
| Mercurio | 0,387 | 2 440 | 0,055 | 88 d | Resonancia 3:2 entre rotación y órbita |
| Venus | 0,723 | 6 052 | 0,815 | 225 d | Rotación retrógrada; efecto invernadero extremo |
| Tierra | 1,000 | 6 378 | 1,000 | 365,26 d | Agua líquida, vida, tectónica de placas |
| Marte | 1,524 | 3 396 | 0,107 | 687 d | Atmósfera tenue, cauces secos, volcanes gigantes |
| Júpiter | 5,203 | 71 492 | 317,8 | 11,86 años | Planeta más masivo; campo magnético enorme |
| Saturno | 9,537 | 60 268 | 95,2 | 29,46 años | Anillos; densidad menor que el agua |
| Urano | 19,19 | 25 559 | 14,5 | 84,0 años | Eje inclinado 97,8° |
| Neptuno | 30,07 | 24 764 | 17,1 | 164,8 años | Vientos más rápidos del sistema |

**Masa del sistema:** el Sol contiene el 99,86 % de la masa; Júpiter, ≈ 71 % de la masa planetaria total.

**Tres familias:**
- **Rocosos (terrestres):** Mercurio, Venus, Tierra, Marte. Pequeños, densos, con superficie sólida.
- **Gigantes gaseosos:** Júpiter y Saturno, formados sobre todo por hidrógeno y helio.
- **Gigantes helados:** Urano y Neptuno, con mucha agua, amoníaco y metano bajo una envoltura de gas.

### La definición de planeta (UAI, 2006)

Un planeta (1) orbita el Sol, (2) tiene masa suficiente para ser casi esférico por su propia gravedad (equilibrio hidrostático) y (3) ha despejado su vecindad orbital. Un **planeta enano** cumple (1) y (2) pero no (3). Plutón pasó a esta categoría porque comparte su región con otros cuerpos de hielo del cinturón de Kuiper.

**Lección:** una categoría científica es una convención útil; cambia cuando se descubre que hay más objetos de los que se creía (Eris, ligeramente más masivo que Plutón, forzó el debate).

---

## 3. Qué determina cómo es un planeta

### 3.1 La gravedad de superficie y la capacidad de retener atmósfera

g = GM / R². La velocidad de escape v_e = √(2GM/R) y la temperatura determinan qué gases se pierden (los más ligeros escapan primero).

| Cuerpo | g (m/s²) | Velocidad de escape (km/s) | Consecuencia |
|---|---|---|---|
| Mercurio | 3,70 | 4,25 | Casi sin atmósfera |
| Venus | 8,87 | 10,36 | Atmósfera densa de CO₂ (92 bar) |
| Tierra | 9,81 | 11,19 | Retiene nitrógeno y oxígeno |
| Luna | 1,62 | 2,38 | Sin atmósfera |
| Marte | 3,71 | 5,03 | Atmósfera delgada (≈ 600 Pa) |
| Júpiter (1 bar) | 24,8 | 59,5 | Retiene hidrógeno y helio |

**Ejercicio.** Calcula g en Marte. *Solución:* GM = 4,283 × 10¹³ m³/s², R = 3,3895 × 10⁶ m → g = 3,73 m/s² (con el radio ecuatorial, 3,71). Comprobación: `calc "4.283e13/3.3895e6**2"`.

### 3.2 La temperatura de equilibrio y el efecto invernadero

T_eq = [S (1 − A) / (4σ)]^¼. Con el albedo medio de cada planeta: Mercurio ≈ 440 K, Venus ≈ 230 K, Tierra ≈ 255 K, Marte ≈ 210 K. La temperatura de la **superficie** difiere cuando hay atmósfera: Tierra 288 K (+33 K) y Venus 737 K (+500 K).

**Lección:** Venus no es caliente por estar más cerca; es más caliente que Mercurio de día por su atmósfera (92 bar de CO₂), que atrapa el calor.

### 3.3 El interior y la actividad geológica

El calor interno viene de la formación (calor residual), de la desintegración radiactiva y de las mareas. Un planeta pequeño pierde su calor antes: por eso la Luna y Mercurio están geológicamente casi muertos, Marte ha tenido volcanismo pero no actual, y la Tierra, más grande, mantiene tectónica de placas. Marte tuvo un campo magnético global que desapareció, y su atmósfera se perdió en gran parte (la misión MAVEN lo estudió).

📘 [B53](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md "Astrogeología y geodesia planetaria"), [B54](../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria"), [B65](../programa/tronco-comun/B65-geofisica-de-interiores-planetarios.md "Geofísica de interiores planetarios"), [B70](../programa/tronco-comun/B70-vulcanismo-planetario.md "Vulcanismo planetario").

---

## 4. Los planetas rocosos, uno por uno

### Mercurio
Densidad alta (5,4 g/cm³): un núcleo de hierro enorme (≈ 85 % del radio). Orbita en resonancia 3:2: gira tres veces cada dos años, con un **día solar de 176 días**, más largo que su año (88 días). La misión MESSENGER halló hielo de agua en cráteres polares siempre en sombra. **Enseña:** un planeta sin atmósfera tiene temperaturas extremas (de ≈ 100 K a ≈ 700 K).

### Venus
Casi gemelo terrestre en tamaño y masa, pero con 92 bar de CO₂ y nubes de ácido sulfúrico. Rotación **retrógrada** de 243 días. Los radares (Magellan) revelaron una superficie joven, remodelada por vulcanismo hace unos cientos de millones de años. **Enseña:** una advertencia sobre un efecto invernadero descontrolado y sobre cuán distintos pueden ser planetas parecidos.

### Tierra
Único planeta con tectónica de placas activa, océanos y vida. Su campo magnético y su gran Luna estabilizan el clima (la Luna estabiliza la inclinación del eje en torno a 23,4°). **Enseña:** la habitabilidad es resultado de muchas condiciones a la vez.

### Marte
Un planeta frío y seco hoy, con evidencias de agua líquida en el pasado (cauces, minerales formados en agua, delta de Jezero). Dos lunas pequeñas, Fobos y Deimos. La mayor montaña del sistema, el Monte Olimpo (≈ 22 km de altura). **Enseña:** un planeta puede ser habitable en una época y dejar de serlo.

📘 [B53](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md "Astrogeología y geodesia planetaria"), [B54](../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria"), [B56](../programa/tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md "Astrobiología y vida extraterrestre"), [B66](../programa/tronco-comun/B66-geomorfologia-y-procesos-superficiales-planetarios.md "Geomorfología y procesos superficiales planetarios").

---

## 5. Los gigantes

### Júpiter y Saturno
Hidrógeno y helio, con un posible núcleo de roca y hielo. Júpiter radia más calor del que recibe del Sol (energía de contracción). Tiene un campo magnético intenso y una radiación peligrosa para las naves (por eso Juno usa una bóveda de titanio). Saturno tiene los anillos más extensos: de hielo de agua, casi planos (decenas de metros de grosor para cientos de miles de km de ancho).

**Anillos:** se mantienen por dentro del límite de Roche y con **lunas pastoras** que los confinan; su edad se discute (¿jóvenes de cientos de millones de años o primordiales?).

### Urano y Neptuno
Gigantes helados. Urano gira «de lado» (97,8° de inclinación), probablemente por un gran impacto. Neptuno tiene los vientos más veloces (> 2 000 km/h). Solo la Voyager 2 los ha visitado de cerca. Una misión orbital a Urano es una prioridad científica declarada en el último estudio decenal de EE. UU.

📘 [B52](../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B54](../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria"), [B73](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md "Mecánica celeste, resonancias y caos").

---

## 6. Las lunas: mundos con actividad propia

| Luna | Planeta | Diámetro (km) | Por qué importa |
|---|---|---|---|
| Luna | Tierra | 3 475 | Origen por gran impacto; mareas; estabiliza el eje |
| Ío | Júpiter | 3 643 | El cuerpo más volcánico del sistema (calentado por mareas) |
| Europa | Júpiter | 3 122 | Océano subterráneo bajo una corteza de hielo |
| Ganímedes | Júpiter | 5 268 | La luna mayor; tiene campo magnético propio |
| Calisto | Júpiter | 4 821 | Superficie muy antigua; posible océano profundo |
| Titán | Saturno | 5 150 | Atmósfera densa (1,5 bar), lagos de metano y etano |
| Encélado | Saturno | 504 | Géiseres de agua que salen de un océano subterráneo |
| Tritón | Neptuno | 2 707 | Órbita retrógrada: probablemente un objeto capturado |

**Calentamiento por mareas.** La excentricidad de Ío, mantenida por su resonancia 4:2:1 con Europa y Ganímedes, hace que su forma se deforme cada vuelta. La fricción interna la calienta: ≈ 20 veces el flujo medio de calor de la Tierra por unidad de área. **Enseña:** un cuerpo pequeño y lejano del Sol puede estar geológicamente activo.

**Dónde buscar vida:** Europa, Encélado y quizás Titán combinan agua líquida bajo la superficie, calor y química orgánica; por eso son objetivos de las misiones Europa Clipper y JUICE.

📘 [B52](../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B56](../programa/tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md "Astrobiología y vida extraterrestre"), [B65](../programa/tronco-comun/B65-geofisica-de-interiores-planetarios.md "Geofísica de interiores planetarios"), [B70](../programa/tronco-comun/B70-vulcanismo-planetario.md "Vulcanismo planetario").

---

## 7. Cuerpos pequeños: los fósiles del sistema

- **Cinturón principal de asteroides (≈ 2,1–3,3 UA):** masa total ≈ 4 % de la de la Luna. Ceres (940 km) es un planeta enano. Hay huecos (Kirkwood) donde las resonancias con Júpiter expulsan asteroides.
- **Troyanos de Júpiter:** miles de cuerpos en los puntos de Lagrange L4 y L5.
- **Cinturón de Kuiper (≈ 30–50 UA):** reserva de cuerpos helados; Plutón, Haumea, Makemake. Arrokoth, visitado por New Horizons, es un objeto «bilobulado» formado por una fusión suave.
- **Nube de Oort (≈ 2 000–100 000 UA):** hipotética; origen de los cometas de largo período.
- **Cometas:** cuerpos de hielo y polvo; al acercarse al Sol forman coma y colas.
- **Meteoroides, meteoros y meteoritos:** el objeto en el espacio, el rastro luminoso y el fragmento que llega al suelo.

**Por qué importan:** son material sin procesar de la formación; las misiones de retorno de muestras (Hayabusa2, OSIRIS-REx) traen ese material a laboratorios.

**Riesgo de impacto:** los grandes asteroides (> 1 km) están casi todos catalogados y no hay amenaza conocida a corto plazo; la vigilancia de los cuerpos menores de unas decenas de metros es un desafío abierto. DART demostró desviar un asteroide.

📘 [B58](../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md "Asteroides, cometas y defensa planetaria"), [B61](../programa/tronco-comun/B61-crateres-de-impacto-y-geologia-de-impactos.md "Cráteres de impacto y geología de impactos").

---

## 8. Las escalas del Sistema Solar

Imagina el Sol del tamaño de una pelota de 20 cm. A esa escala:
- Tierra: una cabeza de alfiler de ≈ 2 mm a unos **21 m**.
- Júpiter: una canica de ≈ 2 cm a ≈ 110 m.
- Neptuno: a ≈ 640 m.
- Próxima Centauri: a ≈ 5 600 km (de Chile a Europa).

**Ejercicio.** Con R_Sol = 6,957 × 10⁸ m, ¿a qué escala está la Tierra si el Sol mide 20 cm de diámetro? *Solución:* factor = 0,20 / (2 × 6,957 × 10⁸) = 1,44 × 10⁻¹⁰; 1 UA × factor = 1,496 × 10¹¹ × 1,44 × 10⁻¹⁰ ≈ **21,5 m**. Comprobación: `calc "UA*0.2/(2*R_sol)"`.

**Lección:** el espacio es casi vacío y las distancias entre planetas son enormes frente a sus tamaños; por eso los diagramas de libros «comprimen» la escala.

---

## 9. Ejercicios integradores

1. **Kepler:** el período orbital de un planeta a 5,2 UA, en años, según T² = a³. *Solución:* T = 5,2^1,5 = **11,9 años**.
2. **Gravedad:** calcula la velocidad de escape de Ceres (M = 9,38 × 10²⁰ kg, R = 470 km). *Solución:* √(2GM/R) = **0,52 km/s**. Comprobación: `calc "sqrt(2*G*9.38e20/470e3)"`.
3. **Temperatura:** calcula T_eq de Marte con S = 590 W/m² y A = 0,25. *Solución:* [590 × 0,75 / (4 × 5,67 × 10⁻⁸)]^¼ = **210 K**.
4. **Comparación:** explica por qué Titán retiene atmósfera con una gravedad menor que la de Marte (pista: temperatura baja de 94 K reduce la velocidad térmica de las moléculas).
5. **Diseño:** ¿qué tipo de misión (sobrevuelo, orbitador, módulo, rover, retorno de muestras) elegirías para cada cuerpo de las secciones 4 a 7 y por qué?

📘 [B52](../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B53](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md "Astrogeología y geodesia planetaria"), [B54](../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria"), [B55](../programa/tronco-comun/B55-astroquimica-y-geoquimica-extraterrestre.md "Astroquímica y geoquímica extraterrestre"), [B58](../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md "Asteroides, cometas y defensa planetaria"), [B71](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental").

[⬅️ Anexo K](ANEXO-K-perfiles-a-fondo.md) · [Índice de anexos](README.md)
