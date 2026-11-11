# Anexo M · Estrellas, galaxias y cosmología a fondo

[⬅️ Anexo L](ANEXO-L-sistema-solar-a-fondo.md) · [Índice de anexos](README.md)

Este anexo sigue la historia de la materia a gran escala: cómo nacen, viven y mueren las estrellas, cómo se organizan en galaxias y qué sabemos del universo como un todo. En cada sección se indica **qué se mide**, **con qué instrumento** y **qué se concluye**, con ejercicios que puedes comprobar con la [calculadora](../herramientas/calculadora_cientifica.py).

> **Estado del texto.** Síntesis propia con cifras redondeadas, pendiente de revisión disciplinar y de contraste con fuentes primarias (nivel E0). Los parámetros cosmológicos se actualizan con cada análisis; confirma el valor vigente (por ejemplo, el de la colaboración Planck) antes de citarlo.

---

## 1. La vida de una estrella

### 1.1 Nacimiento
Una nube molecular fría y densa se fragmenta cuando su masa supera la **masa de Jeans**: la gravedad vence a la presión del gas. Los fragmentos colapsan y se calientan; se forma una **protoestrella** rodeada por un disco, de donde pueden salir planetas. Cuando el núcleo alcanza ≈ 10⁷ K comienza la fusión del hidrógeno y nace una estrella de **secuencia principal**.

### 1.2 Equilibrio y secuencia principal
Una estrella es un equilibrio entre la gravedad (hacia adentro) y la presión del gas caliente (hacia afuera). La fusión es su termostato: si el núcleo se calienta, la estrella se expande y se enfría. En la secuencia principal la luminosidad crece muy rápido con la masa: **L ∝ M^3,5** (aproximado). Como el combustible crece como M, la vida crece como M/L ∝ **M^−2,5**.

| Masa | Tipo | Tiempo en secuencia principal | Destino |
|---|---|---|---|
| 0,1 M☉ | Enana roja | Billones de años | Enana blanca de helio (más lento que la edad del universo) |
| 1 M☉ | Tipo solar | ≈ 10 mil millones de años | Gigante roja → nebulosa planetaria → enana blanca |
| 10 M☉ | Estrella masiva | ≈ 30 millones de años | Supergigante → supernova → estrella de neutrones |
| 30 M☉ o más | Muy masiva | Pocos millones de años | Supernova o colapso directo → agujero negro |

### 1.3 Después del hidrógeno
- **Estrellas de masa baja e intermedia:** al agotar el hidrógeno del núcleo, este se contrae y la envoltura se expande: **gigante roja**. Se enciende el helio, se forman carbono y oxígeno. La estrella expulsa sus capas (**nebulosa planetaria**) y deja un núcleo caliente que se enfría como **enana blanca**, sostenida por la presión de degeneración de los electrones.
- **Estrellas masivas:** fusionan sucesivamente helio, carbono, neón, oxígeno y silicio hasta formar un núcleo de hierro, del que no se extrae energía. El núcleo colapsa en fracciones de segundo, rebota y la estrella explota como **supernova de colapso de núcleo**. Queda una estrella de neutrones o un agujero negro.

### 1.4 Límites de masa
- **Límite de Chandrasekhar** ≈ 1,4 M☉: masa máxima de una enana blanca.
- **Límite de Tolman–Oppenheimer–Volkoff** ≈ 2,2–2,3 M☉ (incierto): masa máxima de una estrella de neutrones.

### 1.5 El futuro del Sol
- Su luminosidad crece ≈ 1 % cada 100 millones de años; en ≈ 1 000 millones de años la Tierra será demasiado cálida para tener océanos.
- En ≈ 5 000 millones de años será gigante roja con un radio de hasta ≈ 1 UA o más, y acabará como enana blanca de ≈ 0,5 M☉ del tamaño de la Tierra.

### 1.6 Ejercicios
1. **Masa de un sistema binario.** Para Sirio, el semieje de la órbita relativa es a ≈ 19,8 UA y el período P ≈ 50,1 años. La tercera ley de Kepler da M₁ + M₂ = a³ / P² (en UA, años y masas solares). *Solución:* 19,8³ / 50,1² = 7 762 / 2 510 ≈ **3,1 M☉** (compatible con las masas conocidas de Sirio A y B). Comprobación: `calc "19.8**3/50.1**2"`.
2. **Vida de una estrella.** Estima la vida en secuencia principal de una estrella de 5 M☉ si el Sol vive 10 mil millones de años. *Solución:* 10 × 5^−2,5 = 10 × 0,0179 = **≈ 0,18 mil millones** (180 millones de años).
3. **Energía de la fusión.** El Sol convierte unos 4,3 × 10⁹ kg de masa en energía cada segundo. Calcula su potencia. *Solución:* P = Δm c² = 4,3 × 10⁹ × (3 × 10⁸)² ≈ **3,9 × 10²⁶ W**. Comprobación: `calc "4.3e9*c**2"`.

📘 [B24](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B31](../programa/tronco-comun/B31-fisica-cuantica-nuclear-y-astroparticulas.md "Física cuántica, nuclear y astropartículas"), [B37](../programa/tronco-comun/B37-interiores-estelares-y-asterosismologia.md "Interiores estelares y asterosismología").

---

## 2. Cómo conocemos las estrellas

| Magnitud | Cómo se mide | Qué revela |
|---|---|---|
| Distancia | Paralaje (cercanas); cefeidas, supernovas Ia (lejanas) | Luminosidad real |
| Temperatura | Color y espectro | Clase espectral (O B A F G K M) |
| Composición | Líneas de absorción | Metalicidad y edad |
| Masa | Órbitas de binarias | Evolución futura |
| Radio | Luminosidad y temperatura (L = 4πR²σT⁴); interferometría | Tipo (enana, gigante, supergigante) |
| Edad | Posición en el diagrama H-R de un cúmulo | Historia de la galaxia |
| Interior | Asterosismología (oscilaciones) y neutrinos | Estructura y composición del núcleo |

**El diagrama de Hertzsprung–Russell** agrupa a las estrellas por luminosidad y temperatura. En un cúmulo, todas las estrellas nacieron juntas: el punto donde las estrellas dejan la secuencia principal («punto de desviación») da su edad. Es uno de los métodos más usados para fechar cúmulos.

📘 [B24](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B32](../programa/tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md "Atmósferas estelares y espectroscopía estelar cuantitativa"), [B37](../programa/tronco-comun/B37-interiores-estelares-y-asterosismologia.md "Interiores estelares y asterosismología"), [B45](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md "Espectroscopía, fotometría y polarimetría").

---

## 3. Las galaxias

### 3.1 Tipos
- **Espirales:** disco con brazos, estrellas jóvenes y gas; ≈ 10¹⁰–10¹² estrellas.
- **Elípticas:** sin disco, estrellas viejas, poco gas; las más grandes resultan de fusiones.
- **Irregulares:** forma caótica, con formación estelar intensa (las Nubes de Magallanes).

### 3.2 La Vía Láctea
- Disco de ≈ 30 kpc de diámetro (≈ 100 000 años luz) y centro con una barra.
- El Sol está a ≈ 8,2 kpc del centro y orbita a ≈ 230 km/s: una vuelta en ≈ 220 millones de años (un «año galáctico»).
- Contiene ≈ 10¹¹ estrellas y, en el centro, un agujero negro supermasivo (Sagitario A*, ≈ 4,3 millones de M☉).
- Su masa total, incluyendo materia oscura, es del orden de 10¹² M☉.

**Ejercicio.** Calcula el año galáctico. *Solución:* T = 2π r / v = 2π × 8,2 kpc / 230 km/s. Con 1 kpc = 3,086 × 10¹⁶ km: T = 2π × 2,53 × 10¹⁷ km / 230 = 6,9 × 10¹⁵ s ≈ **220 millones de años**. Comprobación: `calc "2*pi*8.2*3.086e16/230/(365.25*86400)/1e6"`.

### 3.3 La materia oscura
Las curvas de rotación son planas lejos del centro; los cúmulos curvan la luz más de lo esperado; el fondo cósmico exige más materia que la visible. La materia ordinaria (bariones) es ≈ 5 % del contenido del universo; la materia oscura, ≈ 27 %. Su naturaleza se desconoce; se buscan partículas con detectores subterráneos y en aceleradores.

### 3.4 Evolución y entorno
- Las galaxias crecen por **fusiones** y por acreción de gas.
- Andrómeda se acerca a ≈ 110 km/s; las proyecciones indican una posible fusión con la Vía Láctea en unos 4 000–5 000 millones de años, aunque estudios recientes la ven menos segura.
- **Estructura a gran escala:** las galaxias forman grupos, cúmulos y supercúmulos, enlazados en filamentos alrededor de vacíos gigantes: la **red cósmica**.

📘 [B25](../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md "Galaxias y medio interestelar"), [B36](../programa/tronco-comun/B36-formacion-de-estructuras-cosmicas-y-materia-oscura.md "Formación de estructuras cósmicas y materia oscura"), [B38](../programa/tronco-comun/B38-poblaciones-estelares-y-simulacion-de-galaxias.md "Poblaciones estelares y simulación de galaxias").

---

## 4. El universo como un todo

### 4.1 Los pilares del modelo estándar
1. **La expansión** (Hubble, 1929): las galaxias se alejan con v = H₀ d.
2. **El fondo cósmico de microondas** (1965): radiación a 2,725 K.
3. **La abundancia de elementos ligeros:** ≈ 75 % hidrógeno y ≈ 25 % helio (en masa), producidos en los primeros minutos.
4. **La estructura:** galaxias y cúmulos que crecen a partir de pequeñas fluctuaciones iniciales.

### 4.2 Línea de tiempo del universo

| Cuándo | Qué ocurrió |
|---|---|
| ≈ 10⁻³⁶–10⁻³² s | Inflación (hipótesis): expansión exponencial |
| Segundos a minutos | Nucleosíntesis primordial: se forman H, He y trazas de Li |
| ≈ 380 000 años (z ≈ 1 090) | Recombinación: el universo se vuelve transparente; nace el fondo de microondas |
| ≈ 100–200 millones de años | Primeras estrellas |
| ≈ 0,2–1 mil millones de años | Primeras galaxias; reionización |
| ≈ 9 mil millones de años | La energía oscura comienza a dominar y la expansión se acelera |
| 13 800 millones de años | Hoy |

### 4.3 La composición del universo (hoy)
- **Energía oscura:** ≈ 68 %.
- **Materia oscura:** ≈ 27 %.
- **Materia ordinaria:** ≈ 5 %, de la cual las estrellas son una fracción pequeña.

**Densidad crítica:** ρ_c = 3H² / (8πG). Con H₀ = 70 km s⁻¹ Mpc⁻¹ = 2,27 × 10⁻¹⁸ s⁻¹: ρ_c ≈ **9,2 × 10⁻²⁷ kg/m³**, unos 5 átomos de hidrógeno por metro cúbico. Comprobación: `calc "3*(2.268e-18)**2/(8*pi*G)"`.

### 4.4 Problemas abiertos
- **Tensión de Hubble:** las mediciones locales (cefeidas y supernovas) dan H₀ ≈ 73 km s⁻¹ Mpc⁻¹; el fondo cósmico, ≈ 67. ¿Error sistemático o física nueva?
- **Naturaleza de la materia y la energía oscuras.**
- **Inflación:** ¿ocurrió? ¿qué la causó?
- **Asimetría materia-antimateria:** ¿por qué el universo es de materia?

### 4.5 Ejercicios
1. **Ley de Hubble.** Una galaxia a 200 Mpc, con H₀ = 70. ¿A qué velocidad se aleja? *Solución:* v = 70 × 200 = **14 000 km/s** (z ≈ 0,047).
2. **Mirada hacia atrás.** Si z = 1, la luz salió cuando el universo tenía la mitad de su tamaño actual. El tiempo de retrospección es ≈ 7,9 mil millones de años (modelo estándar).
3. **Temperatura del fondo.** T(z) = 2,725 K (1 + z). ¿Cuál era a z = 1 090? *Solución:* 2,725 × 1 091 ≈ **2 973 K**. Comprobación: `calc "2.725*1091"`.
4. **Luz y distancia.** ¿Cuánto tarda la luz de Andrómeda (0,78 Mpc) en llegar? *Solución:* 0,78 × 3,26 millones de años luz ≈ **2,5 millones de años**.

📘 [B26](../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología"), [B36](../programa/tronco-comun/B36-formacion-de-estructuras-cosmicas-y-materia-oscura.md "Formación de estructuras cósmicas y materia oscura"), [B40](../programa/tronco-comun/B40-universo-temprano-y-radiacion-cosmica-de-fondo.md "Universo temprano y radiación cósmica de fondo").

---

## 5. Cómo se mide el universo: la escalera de distancias

| Peldaño | Rango aproximado | Método |
|---|---|---|
| 1 | Hasta ≈ kpc | Paralaje (Gaia) |
| 2 | Hasta ≈ 100 kpc | Estrellas variables RR Lyrae y cefeidas |
| 3 | Hasta ≈ 100 Mpc | Cefeidas en galaxias cercanas; punta de la rama de las gigantes rojas |
| 4 | Hasta ≈ miles de Mpc | Supernovas tipo Ia, calibradas por los peldaños anteriores |
| 5 | Cosmológico | Corrimiento al rojo y ley de Hubble |

**Lección:** cada peldaño se calibra con el anterior; un error del primero se propaga a todos. Por eso la tensión de Hubble se estudia con tanto cuidado.

📘 [B25](../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md "Galaxias y medio interestelar"), [B26](../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología").

---

## 6. Preguntas para estudiar

1. ¿Por qué las estrellas más masivas viven menos aunque tengan más combustible?
2. ¿Qué diferencia hay entre una enana blanca, una estrella de neutrones y un agujero negro como destino?
3. ¿Qué evidencias independientes apoyan la existencia de materia oscura?
4. ¿Por qué decimos que el Big Bang no fue una explosión en un punto?
5. ¿Qué mediría la mejor prueba para decidir entre los dos valores de H₀?

[⬅️ Anexo L](ANEXO-L-sistema-solar-a-fondo.md) · [Índice de anexos](README.md)
