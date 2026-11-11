# Términos · Q

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · **Q** · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### Q

- Cambio de velocidad `ΔV`: integral de la aceleración. Q: factor de calidad del oscilador de análisis.

💡 **Contexto en la clase [B90-C10](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md):**
- 🎯 **Por qué importa:** Dos pulsos con distinta forma pueden dañar lo mismo si sus SRS coinciden, y un pulso con gran aceleración pico puede ser inofensivo para un equipo de baja frecuencia. La decisión central: ¿qué frecuencias de mi equipo están amenazadas por este choque y con qué nivel?
- 🔗 **Se estudia junto con:** Choque, SRS, Pulso semisenoidal, Cambio de velocidad ΔV.

📘 **Dónde se aprende** (1 clase): [B90-C10 · Ensayos de choque](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md).

### Q10

- La energía de activación `Eₐ` es la barrera de la ecuación de Arrhenius. Q10 es `k(T+10)/k(T)`.
- Vida útil: tiempo hasta un criterio de calidad (aquí 80 % de retención). Q10: factor por 10 °C.

💡 **Cómo se explica en la clase [B64-C03](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md):**
- Q10 no es constante: sube de 4,2 a 10,3 al bajar.
- *Descripción textual:* la energía de activación y la temperatura dan el factor de Arrhenius; de él salen el Q10 y, combinado con el régimen de actividad, el tiempo de renovación.
- ⚠️ **Error frecuente:** Creer que Q10 vale 2. Aquí varía de 4 a 10 (sección 8.2).
- 🎯 **Por qué importa:** El frío no detiene la vida de golpe: la ralentiza. La pregunta motivadora: ¿cuánto más lento es el metabolismo a −40 °C que a 25 °C, y qué significa «vivir» a esa velocidad?
- 🔗 **Se estudia junto con:** psicrófilo, energía de activación, tiempo de renovación, Crecimiento, mantenimiento y supervivencia.

📘 **Dónde se aprende** (2 clases): [B64-C03 · Psicrófilos y vida en frío](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md); [B106-C11 · Almacenamiento de alimentos](../programa/clases/B106/B106-C11-almacenamiento-de-alimentos/CLASE.md).

### QNFMT

- El TAG identifica la especie; su signo negativo indica frecuencia medida. QNFMT declara el formato de los números cuánticos.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- Leer los campos de una línea JPL (`FREQ`, `ERR`, `LGINT`, `DR`, `ELO`, `GUP`, `TAG`, `QNFMT`, cuantos).
- FREQ [MHz] ERR [MHz] LGINT DR ELO [cm^-1] GUP TAG QNFMT J' J'' nu [GHz] E_sup [cm^-1]
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.
- 🔗 **Se estudia junto con:** banco de datos espectroscópicos, CDMS, JPL, HITRAN.

📘 **Dónde se aprende** (1 clase): [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### QP condensado

- El QP condensado tiene como variables solo las acciones `a = (a₀…a_{N−1})`.

💡 **Cómo se explica en la clase [B87-C21](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md):**
- X["estado actual (theta, w)"] --> Q["QP condensado, horizonte N"]
- Resolver el QP condensado con gradiente proyectado acelerado (FISTA).
- 🎯 **Por qué importa:** Un PD satura el par y no sabe de límites de velocidad: puede superar el máximo de la rueda o de la carga útil. La decisión central: ¿cómo formular un problema que respete par y velocidad, cuánto cuesta calcularlo y qué se gana?
- 🔗 **Se estudia junto con:** MPC, horizonte, restricción dura, restricción blanda.

📘 **Dónde se aprende** (1 clase): [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md).

### QPSK

- BPSK usa 2 fases (1 bit/símbolo); QPSK, 4 (2 bits);

💡 **Cómo se explica en la clase [B89-C08](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md):**
- BPSK y QPSK: `Q(√(2γ))`, con `γ = Eb/N0`. 8PSK: `erfc(√(3γ) sin(π/8))/3`. 16QAM: `(3/8) erfc(√(0,4γ))` (aproximaciones con Gray, relaciones estándar no consultadas).
- Para BER 10⁻⁵ (bisección): BPSK/QPSK `9,588 dB`; 8PSK `12,97 dB`; 16QAM `13,43 dB`.
- 🎯 **Por qué importa:** La elección de la modulación fija el `Eb/N0` requerido en el presupuesto de enlace y el ancho de banda ocupado; es la base de la codificación y la sincronización siguientes. La decisión central: ¿qué modulación da la tasa que necesito con el `Eb/N0` que mi enlace puede ofrecer?
- 🔗 **Se estudia junto con:** BPSK, 8PSK, 16QAM, BER.

📘 **Dónde se aprende** (1 clase): [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md).

### QR

- LU: `P A = L U` con `L` triangular inferior de unos en la diagonal, `U` triangular superior y `P` una matriz de permutación (reordena filas) —es la eliminación gaussiana guardada—. QR: `A = Q R` con `Q` de columnas ortonormales y `R` triangular superior.

💡 **Cómo se explica en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- Aproximadamente: LU cuesta `2n³/3` operaciones, Cholesky `n³/3` (la mitad, por usar la simetría), QR cerca de `4n³/3` para matrices cuadradas.
- B -->|"rectangular o<br/>mínimos cuadrados"| D["QR<br/>A = Q R"]
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.
- 🔗 **Se estudia junto con:** factorización, LU, matriz de permutación, Cholesky.

📘 **Dónde se aprende** (1 clase): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md).

### Quantum

- El quantum es una dosis infecciosa definida de forma que un quantum inhalado causa infección con probabilidad `1 − e⁻¹`; es una unidad modelística y no se mide directamente.

💡 **Contexto en la clase [B110-C02](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md):**
- 🎯 **Por qué importa:** Aislar a alguien en una cabina cuesta espacio, tiempo y trabajo de la tripulación; no aislar cuesta exposición. La decisión central: ¿cuánta exposición evita cada barrera y con qué incertidumbre?
- 🔗 **Se estudia junto con:** mezcla perfecta, tasa de eliminación, intercambio, dosis.

📘 **Dónde se aprende** (1 clase): [B110-C02 · Protocolos operativos de aislamiento de un tripulante enfermo o contaminado](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md).

### Quark

- Un quark `u` o `d`.

💡 **Cómo se explica en la clase [B31-C10](../programa/clases/B31/B31-C10-modelo-estandar-de-particulas/CLASE.md):**
- *Descripción textual:* los quarks forman hadrones con números cuánticos; para una reacción se comparan las sumas inicial y final y se declara permitida o prohibida.
- Las cargas de los quarks (+2/3 y −1/3) y los números cuánticos son valores estándar no consultados.
- 🎯 **Por qué importa:** Antes de calcular una sección eficaz, una reacción debe respetar las leyes de conservación. La decisión central: ¿está permitida esta reacción por las reglas de conservación?
- 🔗 **Se estudia junto con:** hadrón, leptón, número bariónico, número leptónico.

📘 **Dónde se aprende** (1 clase): [B31-C10 · Modelo estándar de partículas](../programa/clases/B31/B31-C10-modelo-estandar-de-particulas/CLASE.md).

### Quema prógrada

- La quema prógrada empuja en el sentido de la velocidad.

💡 **Contexto en la clase [B75-C10](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md):**
- 🎯 **Por qué importa:** El modelo impulsivo es útil, pero ¿cuándo es un buen modelo? La decisión central: ¿cuánto delta-v se pierde por quemar durante un tiempo finito y de qué depende, en particular del cociente empuje/peso?
- 🔗 **Se estudia junto con:** empuje finito, pérdida por empuje finito, cociente empuje/peso, flujo másico.

📘 **Dónde se aprende** (1 clase): [B75-C10 · Maniobras impulsivas](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md).

### Quemado en capa

- El quemado en capa es la fusión en una capa que envuelve el núcleo.

💡 **Cómo se explica en la clase [B24-C16](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md):**
- Describir la secuencia: fin del hidrógeno, quemado en capa, expansión.
- Estimar el crecimiento del núcleo por quemado de hidrógeno en capa.
- 🎯 **Por qué importa:** Una gigante roja es mucho mayor y más luminosa que su estrella original y tiene una densidad media ínfima. Entender su tamaño, su gravedad y cómo crece su núcleo permite interpretar las gigantes observadas, usarlas como sondas asterosísmicas y anticipar el destino del Sol.
- 🔗 **Se estudia junto con:** gigante roja, núcleo inerte de helio, rama de las gigantes rojas, gravedad superficial.

📘 **Dónde se aprende** (1 clase): [B24-C16 · Gigantes rojas](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md).

### Quiebre

- Un quiebre (*break*) es un cambio brusco en una serie.

💡 **Cómo se explica en la clase [B57-C27](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md):**
- La regla «3 observaciones consecutivas con |z| > 3» da una alarma en `t = 6,089` años (quiebre en 6,000), con un retraso de `1,1 meses`, y `0` falsas alarmas entre los años 3 y 6.
- Con la cadencia de 16 días de este ejemplo, la regla necesita tres observaciones tras el quiebre, un retraso del orden de uno a dos meses.
- 🎯 **Por qué importa:** Un umbral bajo llena el mapa de falsas alarmas; uno alto deja pasar cambios reales. La decisión central: ¿qué umbral equilibra falsas alarmas y detecciones para el cambio que me interesa?
- 🔗 **Se estudia junto con:** diferencia de imágenes, umbral, tasa de falsa alarma, detección.

📘 **Dónde se aprende** (1 clase): [B57-C27 · Detección de cambios en series de imágenes](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md).

### Química de radiación

- La fotoquímica es la que inicia una excitación electrónica inducida por un fotón sin ionizar; la química de radiación estudia los cambios por absorción de radiación capaz de ionizar (definiciones de Arumainayagam y colaboradores).

💡 **Cómo se explica en la clase [B68-C03](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md):**
- Arumainayagam y colaboradores (2019) definen la química de radiación como el estudio de los cambios por absorción de radiación con energía suficiente para ionizar y la fotoquímica como la iniciada por excitación electrónica sin ionización.
- Señalan que la luz ultravioleta de vacío (6,2–12,4 eV) puede además iniciar química de radiación, porque el umbral para producir electrones secundarios es más bajo en fase condensada que en fase gaseosa.
- 🎯 **Por qué importa:** Un hielo en una nube densa recibe poca luz ultravioleta externa, pero sigue recibiendo partículas energéticas y fotones secundarios. Esas dosis lentas transforman la composición del hielo durante millones de años.
- 🔗 **Se estudia junto con:** radiación ionizante, fotoquímica, poder de frenado electrónico, pulverización.

📘 **Dónde se aprende** (1 clase): [B68-C03 · Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md).

### Química orgánica

- La química orgánica estudia los compuestos del carbono (con H, O, N, S, P…).

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- python programa/clases/B06/B06-C16-quimica-organica-esencial/moleculas_organicas.py
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).
- 🔗 **Se estudia junto con:** hidrocarburo, alcano, alqueno, alquino.

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Quimiolitótrofo

- Un quimiolitótrofo obtiene energía de reacciones inorgánicas.

💡 **Contexto en la clase [B56-C07](../programa/clases/B56/B56-C07-energia-quimica-para-la-vida/CLASE.md):**
- **Idea central (modelo mental):** `ΔG°` es la altura de la cascada con todo a 1 bar; las concentraciones cambian la altura efectiva. Con mucho H₂ la cascada es alta; con poco, se aplana y a una concentración crítica el agua deja de caer.
- 🎯 **Por qué importa:** Un ambiente con agua pero sin fuente de energía química es un desierto para la vida. En un océano sin luz, la energía viene de reacciones entre compuestos reducidos y oxidados.
- 🔗 **Se estudia junto con:** energía libre de reacción, cociente de reacción, constante de equilibrio, potencia de mantenimiento.

📘 **Dónde se aprende** (1 clase): [B56-C07 · Energía química para la vida](../programa/clases/B56/B56-C07-energia-quimica-para-la-vida/CLASE.md).

### Quinto orden

- El tercer orden es el término en `h²`; el quinto orden, el de `h⁴`.

💡 **Contexto en la clase [B50-C01](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md):**
- **Idea central (modelo mental):** Como medir un balcón con una regla recta (paraxial) o siguiendo su curva real (exacto): cerca del eje coinciden; lejos del eje la regla se equivoca.
- 🎯 **Por qué importa:** Un diseño que solo se calcula en aproximación paraxial es optimista: ignora lo que ocurre lejos del eje. La decisión central: ¿cuánta de la aberración de una lente es de tercer orden y cuánta es de orden superior?
- 🔗 **Se estudia junto con:** trazado exacto, aberración esférica longitudinal, tercer orden, foco paraxial.

📘 **Dónde se aprende** (1 clase): [B50-C01 · Trazado exacto de rayos y aberraciones de orden superior](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md).
