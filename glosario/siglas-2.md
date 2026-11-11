# Siglas y acrónimos (parte 2 de 2)

[⬅️ Índice del glosario](README.md)

Siglas y acrónimos que las clases definen en su vocabulario, en orden alfabético. Si una sigla no aparece, ninguna clase la presentó en su vocabulario.

Partes: [1](siglas.md) · **2**

### PDR

- La PDR revisa el diseño preliminar, los presupuestos con márgenes, las interfaces, la madurez tecnológica y el plan de verificación.

💡 **Cómo se explica en la clase [B83-C13](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md):**
- PDR: margen de masa ≥ 10 %, de energía ≥ 20 %, de datos ≥ 25 %, interfaces verificadas al 100 %, TRL mínimo ≥ 5, plan de verificación con línea base y cero acciones críticas abiertas.
- Resultado: SRR 2/5 y PDR 2/7; ninguna lista.
- 🎯 **Por qué importa:** Una revisión aprobada sin criterios es un trámite; una revisión con criterios medibles es una decisión. La decisión central: ¿el proyecto cumple los criterios de entrada de la SRR y de la PDR y qué falta para llegar?
- 🔗 **Se estudia junto con:** SRR, criterio, crítico, RID.

📘 **Dónde se aprende:** [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md).

### PFA

- **Significa:** Falsa aceptación (PFA).
- Banda de guarda `w`: margen que se resta al límite para aceptar. Falsa aceptación (PFA): aceptar una unidad realmente fuera de especificación.

💡 **Cómo se explica en la clase [B90-C08](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md):**
- Sin banda de guarda se acepta el 0,012 % de unidades malas y se rechaza el 0,019 % de buenas; con guarda `U` la falsa aceptación baja a 0,0003 % y el falso rechazo sube a 0,128 %.
- Descripción larga: al subir la banda de guarda la falsa aceptación se acerca a cero y el falso rechazo crece de 0,019 % a 0,37 %.
- 🎯 **Por qué importa:** Toda medida tiene incertidumbre. Si se acepta con el límite exacto, algunas unidades malas pasan; si se endurece el criterio, algunas buenas se rechazan y cuesta tiempo.
- 🔗 **Se estudia junto con:** Procedimiento de prueba, Tolerancia, Incertidumbre de medida, Banda de guarda w.

📘 **Dónde se aprende:** [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### PFR

- **Significa:** Falso rechazo (PFR); Flujo pistón (PFR).
- Falsa aceptación (PFA): aceptar una unidad realmente fuera de especificación. Falso rechazo (PFR): rechazar una unidad conforme.
- Mezcla completa (CSTR): tanque uniforme. Flujo pistón (PFR): flujo sin mezcla longitudinal.

💡 **Cómo se explica en la clase [B90-C08](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md):**
- Sin banda de guarda se acepta el 0,012 % de unidades malas y se rechaza el 0,019 % de buenas; con guarda `U` la falsa aceptación baja a 0,0003 % y el falso rechazo sube a 0,128 %.
- Descripción larga: al subir la banda de guarda la falsa aceptación se acerca a cero y el falso rechazo crece de 0,019 % a 0,37 %.
- 🎯 **Por qué importa:** Toda medida tiene incertidumbre. Si se acepta con el límite exacto, algunas unidades malas pasan; si se endurece el criterio, algunas buenas se rechazan y cuesta tiempo.
- 🔗 **Se estudia junto con:** Procedimiento de prueba, Tolerancia, Incertidumbre de medida, Banda de guarda w.

📘 **Dónde se aprende:** [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md); [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### PGM

- El código de estado resume el resultado (200, 400, 404). PGM es un formato de imagen gris muy simple.

💡 **Cómo se explica en la clase [B14-C29](../programa/clases/B14/B14-C29-servicios-de-datos-geoespaciales-estandar-ogc/CLASE.md):**
- Para la caja completa y 64 × 64 píxeles, el servicio devuelve 200 con una imagen PGM de forma `(64, 64)`, valores entre 28 y 228.
- 🎯 **Por qué importa:** Has producido un mosaico de imágenes y varias organizaciones quieren verlo en sus propios visores. Enviar archivos a cada una no escala, y cada una usa un programa distinto.
- 🔗 **Se estudia junto con:** servicio, capacidades, petición de mapa, capa.

📘 **Dónde se aprende:** [B14-C29 · Servicios de datos geoespaciales estándar (OGC)](../programa/clases/B14/B14-C29-servicios-de-datos-geoespaciales-estandar-ogc/CLASE.md).

### PHA

- Un PHA es un asteroide cercano a la Tierra con `MOID ≤ 0,05 au` y `H ≤ 22` [S3].

💡 **Cómo se explica en la clase [B58-C05](../programa/clases/B58/B58-C05-orbitas-cercanas-a-la-tierra/CLASE.md):**
- SINT-A (`H = 21`, MOID `0.080`) no es PHA;
- SINT-D (`H = 21,5`, MOID `0.021`) es PHA;
- ⚠️ **Error frecuente:** Declarar PHA sin comprobar `H`. Se corrige con 8.5.
- 🎯 **Por qué importa:** Dos órbitas pueden cruzarse en proyección sin que los cuerpos coincidan nunca, y pueden no cruzarse y estar a una distancia pequeña. El MOID separa los casos geométricamente.
- 🔗 **Se estudia junto con:** MOID, nodo, sección áurea.

📘 **Dónde se aprende:** [B58-C05 · Órbitas cercanas a la Tierra](../programa/clases/B58/B58-C05-orbitas-cercanas-a-la-tierra/CLASE.md).

### PID

- La ley PID es `u(t) = Kp e(t) + Ki ∫₀ᵗ e(τ) dτ + Kd ė(t)`, con `e = r − y` el error;

💡 **Cómo se explica en la clase [B16-C11](../programa/clases/B16/B16-C11-control-proporcional-integral-derivativo/CLASE.md):**
- Paso 2 · PID. Se agrega `Ki = 2` y la integral `ξ`.
- Paso 4 · simulación. A los 600 s, `θ = 25,000000 mrad` con PD y `−0,000000 mrad` con PID (error < 10⁻⁶ rad);
- 🎯 **Por qué importa:** En el espacio actúan pares pequeños pero persistentes: presión de radiación solar, gradiente de gravedad, fugas de un propulsor. Un lazo PD termina con un error constante `d/Kp` (C04).
- 🔗 **Se estudia junto con:** derivada sobre la medida, tipo, tiempo integral, derivativo.

📘 **Dónde se aprende:** [B16-C11 · Control proporcional integral derivativo](../programa/clases/B16/B16-C11-control-proporcional-integral-derivativo/CLASE.md).

### PIL

- SIL: software en el computador de desarrollo. PIL: en el procesador objetivo o en un modelo de su aritmética.

💡 **Cómo se explica en la clase [B88-C41](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md):**
- PIL, de aritmética y de tamaño de datos;
- Por ejecución en el procesador (PIL real): exige hardware.
- ⚠️ **Error frecuente:** Creer que SIL basta. Hace falta PIL y HIL (8.4)
- 🎯 **Por qué importa:** La aritmética del procesador objetivo puede ser distinta de la del escritorio. La decisión central: ¿cuánto se aparta la respuesta con la precisión del objetivo y cumple la tolerancia?
- 🔗 **Se estudia junto con:** SIL, HIL, épsilon, LSB.

📘 **Dónde se aprende:** [B88-C41 · Pruebas SIL y PIL del software de vuelo](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md).

### PIRE

- La PIRE es `P_t − L_t + G_t` (dBW).
- La PIRE es la potencia isótropa radiada equivalente, en dBW.
- PIRE: potencia isotrópica radiada equivalente.

💡 **Cómo se explica en la clase [B89-C05](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md):**
- PT["Pt, perdidas Tx, Gt"] --> PIRE["PIRE"]
- PIRE --> CN0["C/N0 = PIRE - L + G/T - 10 log k"]
- 🎯 **Por qué importa:** El presupuesto de enlace es el documento donde se decide si una misión puede transmitir; un error de 3 dB equivale a duplicar la potencia o el tamaño de la antena. La decisión central: ¿cuánto margen queda y qué tasa de datos máxima admite este enlace?
- 🔗 **Se estudia junto con:** pérdida de espacio libre, G/T, C/N0 = PIRE − L_total + G/T − 10 log₁₀ k, Eb/N0 = C/N0 − 10 log₁₀ R_b.

📘 **Dónde se aprende:** [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md); [B89-C05 · Presupuesto de enlace](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md); [B96-C27 · Operación de equipos de radiofrecuencia en la estación](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md); [B120-C02 · Zonas de coordinación entre servicios radioeléctricos](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md).

### PLL

- **Significa:** lazo de enganche de fase (PLL).
- El lazo de enganche de fase (PLL) compara la fase de entrada con la de un NCO y corrige.

💡 **Contexto en la clase [B89-C10](../programa/clases/B89/B89-C10-sincronizacion-de-portadora/CLASE.md):**
- 🎯 **Por qué importa:** Un lazo demasiado ancho deja pasar ruido; uno demasiado estrecho pierde el Doppler. Ajustarlo es el equilibrio central de la sincronización y condiciona la recepción de señales débiles (C24).
- 🔗 **Se estudia junto con:** segundo orden, ancho de banda de lazo, frecuencia natural, SNR del lazo.

📘 **Dónde se aprende:** [B89-C10 · Sincronización de portadora](../programa/clases/B89/B89-C10-sincronizacion-de-portadora/CLASE.md).

### PLSS

- El PLSS (*portable life support system*) es la mochila del traje.

💡 **Cómo se explica en la clase [B108-C01](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md):**
- En la prueba PLSS 1.0 la inyección de CO₂ se ajustó entre 28 y 280 g/h, el agua de vapor entre 35 y 89 g/h, la fuga del traje entre 2,1 y 4,2 g/h y el rechazo de diseño del evaporador fue 810 W.
- El perfil es ilustrativo; las potencias 469 W y 700 W son las de las pruebas PLSS 1.0.
- 🎯 **Por qué importa:** B106-C09 trata el soporte vital de hábitat; el del traje no tiene clase. La decisión central: ¿cuánto oxígeno, cuánto calor a rechazar y cuánto CO₂ genera una EVA con un perfil de esfuerzo dado, y qué margen deja el sistema?
- 🔗 **Se estudia junto con:** oxígeno, ventilación, térmico, cociente respiratorio.

📘 **Dónde se aprende:** [B108-C01 · Sistemas portátiles de soporte vital (PLSS)](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md).

### PNP

- **Significa:** Probabilidad de no penetración (PNP).
- Parachoques: pared de sacrificio. Probabilidad de no penetración (PNP): `exp(−N)`.

💡 **Cómo se explica en la clase [B106-C15](../programa/clases/B106/B106-C15-proteccion-frente-a-micrometeoritos/CLASE.md):**
- Descripción larga: la probabilidad de no penetración cae con la superficie y el tiempo y sube con el diámetro crítico; la separación es la palanca más eficaz del modelo.
- 🎯 **Por qué importa:** Los impactos son raros pero catastróficos; el diseño elige espesor y separación para una probabilidad de no penetración. La decisión central: ¿qué pared y qué separación dan una probabilidad objetivo en la duración y la superficie de la misión?
- 🔗 **Se estudia junto con:** Micrometeoroide, desecho orbital, Diámetro crítico, Parachoques.

📘 **Dónde se aprende:** [B106-C15 · Protección frente a micrometeoritos](../programa/clases/B106/B106-C15-proteccion-frente-a-micrometeoritos/CLASE.md).

### POD

- El POD es la fracción de eventos detectados, el FAR la de alertas falsas y el CSI la de aciertos sobre todos los casos relevantes.
- La POD es `P(detectar | a)`.
- El POD, el FAR y el Heidke.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- *Descripción textual:* las medidas se convierten en escalas G, S y R; la regla y lo observado forman la tabla de contingencia, de la que salen POD, FAR y Heidke.
- Calcular POD, FAR, CSI y la puntuación de Heidke por dos fórmulas.
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?
- 🔗 **Se estudia junto con:** escala, acierto, falsa alarma, fallo.

📘 **Dónde se aprende:** [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B33-C13 · Pronóstico de actividad geomagnética](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md); [B84-C19 · Inspección no destructiva](../programa/clases/B84/B84-C19-inspeccion-no-destructiva/CLASE.md).

### PPFD

- **Significa:** flujo de fotones fotosintéticos (PPFD).
- El PPFD mide la luz útil para la fotosíntesis.
- PPFD: flujo de fotones útiles.
- El flujo de fotones fotosintéticos (PPFD) cuenta los fotones de 400–700 nm que llegan a una superficie (µmol m⁻² s⁻¹).

💡 **Cómo se explica en la clase [B59-C14](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md):**
- AREA --> P["× PPFD ÷ eficacia: potencia"]
- ⚠️ **Error frecuente:** Confundir PPFD con iluminancia. El PPFD mide fotones útiles; sección 6.
- 🎯 **Por qué importa:** Cultivar exige luz, y la luz eléctrica cuesta potencia. La decisión central: ¿cuántos metros cuadrados y cuántos kilovatios necesita un cultivo para producir el oxígeno de una persona?
- 🔗 **Se estudia junto con:** fotones por O₂, eficacia, evapotranspiración, sustrato.

📘 **Dónde se aprende:** [B59-C14 · Agricultura y sustratos artificiales](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md); [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md); [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### PPG

- **Significa:** fotopletismografía (PPG).
- La fotopletismografía (PPG) mide con luz los cambios de volumen de sangre en la piel.

💡 **Contexto en la clase [B116-C01](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md):**
- 🎯 **Por qué importa:** Una pulsera que da «72 lpm» no dice «72 ± 0,1». Con movimiento puede dar 120 cuando el pulso real es 70.
- 🔗 **Se estudia junto con:** frecuencia cardiaca, artefacto de movimiento, resolución espectral, Bland–Altman.

📘 **Dónde se aprende:** [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### PRF

- La PRF (frecuencia de repetición de pulsos) es el muestreo del tiempo lento.
- La PRF es la frecuencia de repetición de pulsos.

💡 **Cómo se explica en la clase [B69-C01](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md):**
- El tiempo lento se muestrea a la `PRF`; para no tener aliasing hace falta `PRF ≥ Ba`.
- Una antena más corta ensancha el haz, aumenta `Ba` y mejora la resolución, pero exige una `PRF` mayor, y eso reduce la franja de terreno que puede observarse sin ambigüedad (ejercicio 10).
- 🎯 **Por qué importa:** Sin el principio Doppler, la resolución en azimut de un radar quedaría fijada por el ancho del haz de la antena: a 850 km, una antena de 12 m (λ = 0,0555 m) iluminaría una franja de unos 3,9 km. La decisión central: ¿qué resolución obtiene el sistema, de qué depende y qué hay que muestrear para no perderla?
- 🔗 **Se estudia junto con:** dirección de azimut, alcance oblicuo, apertura sintética, frecuencia Doppler.

📘 **Dónde se aprende:** [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md); [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### PRNU

- La PRNU es la variación de sensibilidad entre píxeles.

💡 **Cómo se explica en la clase [B44-C14](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md):**
- Con una respuesta de `3,77 %` de dispersión (PRNU de `1,5 %` y viñeteo de `15 %`) y `20 000 e⁻` por píxel, un flat de `80` cuadros deja una no uniformidad residual de `0,00738`, frente a `0,0386` sin flat.
- respuesta verdadera: std relativa 0.0377 (PRNU + vineteo)
- 🎯 **Por qué importa:** Los píxeles no responden igual y el campo se oscurece hacia el borde. La decisión central: ¿cuántos flats hacen falta para que el ruido del flat no domine?
- 🔗 **Se estudia junto con:** flat, viñeteo, normalización, no uniformidad residual.

📘 **Dónde se aprende:** [B44-C14 · Calibración con flat](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md).

### PSD

- La PSD `S(f)`;
- PSD: densidad espectral de potencia, g²/Hz.

💡 **Cómo se explica en la clase [B43-C23](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md):**
- PS["PSD A/f²"] --> P["perfil con fases aleatorias"]
- *Descripción textual:* una PSD fija la rugosidad en una banda; la TIS la convierte en luz dispersa por la fórmula escalar.
- ⚠️ **Error frecuente:** Confundir PSD con la amplitud de un modo. Se corrige con 8.1.
- 🎯 **Por qué importa:** La luz dispersa reduce el contraste y la reflectancia especular. La decisión central: ¿qué rugosidad RMS, en qué banda de frecuencias espaciales, deja la luz dispersa por debajo del presupuesto?
- 🔗 **Se estudia junto con:** rugosidad RMS, TIS, banda, reflectancia especular.

📘 **Dónde se aprende:** [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md); [B90-C09 · Ensayos de vibración](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md).

### PSF

- La PSF (*point spread function*) es la imagen que el sistema da de una fuente puntual; en el modelo, la respuesta impulsional bidimensional de C08.
- La PSF es la respuesta del instrumento a una fuente puntual.
- La PSF es la respuesta a una fuente puntual.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- Con PSF gaussiana: `FWHM = 2,355 σ` y pico normalizado `1/(2πσ²)`.
- donde `⋆` es la correlación con la PSF (convolución con la PSF volteada).
- ⚠️ **Error frecuente:** Usar una PSF que no corresponde al instrumento y al campo. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.
- 🔗 **Se estudia junto con:** gaussiana, FWHM, desenfoque, función de transferencia.

📘 **Dónde se aprende:** [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md); [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md); [B45-C24 · Fotometría por ajuste de PSF](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md); [B74-C02 · Observación angular y astrometría](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md); [B74-C25 · Detección de limbo y bordes planetarios en imágenes de navegación](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md).

### PSLR

- El PSLR es la razón entre el mayor lóbulo lateral y el pico principal.

💡 **Cómo se explica en la clase [B69-C02](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md):**
- Medir anchuras a −3 dB y el nivel del lóbulo lateral (PSLR).
- Ejercicio 8 · autónomo. ¿A qué amplitud corresponde un PSLR de −13,26 dB?
- 🎯 **Por qué importa:** Sin procesamiento, un eco crudo parece ruido. La decisión central: ¿qué operaciones convierten el eco crudo en una imagen con la resolución teórica, y cuándo fallan?
- 🔗 **Se estudia junto con:** chirp, compresión en alcance, compresión en azimut, migración de celda.

📘 **Dónde se aprende:** [B69-C02 · Formación de imágenes SAR](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md).

### PV

- El PV es el valor del trabajo planificado a la fecha; el EV, el valor del trabajo logrado; el AC, el costo real.
- El PV y el RMS del resto.

💡 **Cómo se explica en la clase [B43-C22](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md):**
- La superficie tiene `14,84` franjas (PV total/(λ/2)); el resto, `0,308`.
- La superficie tiene `14,8` franjas en total; tras ajustar piston, inclinaciones y desenfoque queda un resto de `97,3 nm` PV y `19,90 nm` RMS (`0,0314 λ`).
- 🎯 **Por qué importa:** El mapa de error de forma es la prueba de aceptación de un espejo. La decisión central: ¿cómo se recupera la fase, qué se descuenta y qué PV y RMS quedan?
- 🔗 **Se estudia junto con:** desplazamiento de fase, fase, desenvolvimiento, ajuste de modos.

📘 **Dónde se aprende:** [B43-C22 · Interferometría de superficie y mapas de error de forma](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md); [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### Q10

- La energía de activación `Eₐ` es la barrera de la ecuación de Arrhenius. Q10 es `k(T+10)/k(T)`.
- Vida útil: tiempo hasta un criterio de calidad (aquí 80 % de retención). Q10: factor por 10 °C.

💡 **Cómo se explica en la clase [B64-C03](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md):**
- Q10 no es constante: sube de 4,2 a 10,3 al bajar.
- *Descripción textual:* la energía de activación y la temperatura dan el factor de Arrhenius; de él salen el Q10 y, combinado con el régimen de actividad, el tiempo de renovación.
- ⚠️ **Error frecuente:** Creer que Q10 vale 2. Aquí varía de 4 a 10 (sección 8.2).
- 🎯 **Por qué importa:** El frío no detiene la vida de golpe: la ralentiza. La pregunta motivadora: ¿cuánto más lento es el metabolismo a −40 °C que a 25 °C, y qué significa «vivir» a esa velocidad?
- 🔗 **Se estudia junto con:** psicrófilo, energía de activación, tiempo de renovación, Crecimiento, mantenimiento y supervivencia.

📘 **Dónde se aprende:** [B64-C03 · Psicrófilos y vida en frío](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md); [B106-C11 · Almacenamiento de alimentos](../programa/clases/B106/B106-C11-almacenamiento-de-alimentos/CLASE.md).

### QM

- **Significa:** Modelo de calificación (QM).
- Modelo de ingeniería (EM): modelo funcionalmente representativo para probar el diseño. Modelo de calificación (QM): unidad idéntica a la de vuelo para calificar.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- Distinguir prototipo, modelo de ingeniería, modelo de calificación, protovuelo y unidad de vuelo.
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?
- 🔗 **Se estudia junto con:** Prototipo, Modelo de ingeniería (EM), Protovuelo, Unidad de vuelo (FM).

📘 **Dónde se aprende:** [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### QMS

- **Significa:** espectrómetro de masas cuadrupolar (QMS).
- El espectrómetro de masas cuadrupolar (QMS) mide el gas por masa.

💡 **Cómo se explica en la clase [B68-C04](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md):**
- Kruczkiewicz y colaboradores (2024) hacen TPD a `0,2 K s⁻¹` desde 10 K y detectan los gases con un espectrómetro de masas cuadrupolar;
- 🎯 **Por qué importa:** Un hielo de 10 ML de CO sobre una superficie a 10 K se contamina con agua residual en horas si la presión de fondo no es lo bastante baja, y una TPD con bombeo insuficiente deforma el pico que se mide.
- 🔗 **Se estudia junto con:** ultra alto vacío (UHV), flujo de Hertz–Knudsen, probabilidad de adhesión, langmuir.

📘 **Dónde se aprende:** [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### QNFMT

- El TAG identifica la especie; su signo negativo indica frecuencia medida. QNFMT declara el formato de los números cuánticos.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- Leer los campos de una línea JPL (`FREQ`, `ERR`, `LGINT`, `DR`, `ELO`, `GUP`, `TAG`, `QNFMT`, cuantos).
- FREQ [MHz] ERR [MHz] LGINT DR ELO [cm^-1] GUP TAG QNFMT J' J'' nu [GHz] E_sup [cm^-1]
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.
- 🔗 **Se estudia junto con:** banco de datos espectroscópicos, CDMS, JPL, HITRAN.

📘 **Dónde se aprende:** [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### QPSK

- BPSK usa 2 fases (1 bit/símbolo); QPSK, 4 (2 bits);

💡 **Cómo se explica en la clase [B89-C08](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md):**
- BPSK y QPSK: `Q(√(2γ))`, con `γ = Eb/N0`. 8PSK: `erfc(√(3γ) sin(π/8))/3`. 16QAM: `(3/8) erfc(√(0,4γ))` (aproximaciones con Gray, relaciones estándar no consultadas).
- Para BER 10⁻⁵ (bisección): BPSK/QPSK `9,588 dB`; 8PSK `12,97 dB`; 16QAM `13,43 dB`.
- 🎯 **Por qué importa:** La elección de la modulación fija el `Eb/N0` requerido en el presupuesto de enlace y el ancho de banda ocupado; es la base de la codificación y la sincronización siguientes. La decisión central: ¿qué modulación da la tasa que necesito con el `Eb/N0` que mi enlace puede ofrecer?
- 🔗 **Se estudia junto con:** BPSK, 8PSK, 16QAM, BER.

📘 **Dónde se aprende:** [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md).

### QR

- LU: `P A = L U` con `L` triangular inferior de unos en la diagonal, `U` triangular superior y `P` una matriz de permutación (reordena filas) —es la eliminación gaussiana guardada—. QR: `A = Q R` con `Q` de columnas ortonormales y `R` triangular superior.

💡 **Cómo se explica en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- Aproximadamente: LU cuesta `2n³/3` operaciones, Cholesky `n³/3` (la mitad, por usar la simetría), QR cerca de `4n³/3` para matrices cuadradas.
- B -->|"rectangular o<br/>mínimos cuadrados"| D["QR<br/>A = Q R"]
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.
- 🔗 **Se estudia junto con:** factorización, LU, matriz de permutación, Cholesky.

📘 **Dónde se aprende:** [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md).

### R2

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Cómo se explica en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- Se toman del texto de Holzmann: flujo simple sin recursión (R1), bucles con cota (R2), unas 60 líneas por función (R4), mínimo de dos aserciones por función (R5) y comprobar valores devueltos (R7).
- Paso 2 · Bucle. `while True` sin `break` ni `return`: R2.
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?
- 🔗 **Se estudia junto con:** R1, R3, R4, R5.

📘 **Dónde se aprende:** [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R3

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Contexto en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?
- 🔗 **Se estudia junto con:** R1, R2, R4, R5.

📘 **Dónde se aprende:** [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R4

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Cómo se explica en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- Se toman del texto de Holzmann: flujo simple sin recursión (R1), bucles con cota (R2), unas 60 líneas por función (R4), mínimo de dos aserciones por función (R5) y comprobar valores devueltos (R7).
- Ejercicio 10 · transferencia. Transferencia. ¿Qué cambia si se aplica R4 con 10 líneas?
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?
- 🔗 **Se estudia junto con:** R1, R2, R3, R5.

📘 **Dónde se aprende:** [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R5

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Cómo se explica en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- Se toman del texto de Holzmann: flujo simple sin recursión (R1), bucles con cota (R2), unas 60 líneas por función (R4), mínimo de dos aserciones por función (R5) y comprobar valores devueltos (R7).
- Paso 3 · Aserciones. Ninguna función tiene 2: R5 ×4.
- ⚠️ **Error frecuente:** Poner aserciones vacías. Deben comprobar algo real (R5)
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?
- 🔗 **Se estudia junto con:** R1, R2, R3, R4.

📘 **Dónde se aprende:** [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R6

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Contexto en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?
- 🔗 **Se estudia junto con:** R1, R2, R3, R4.

📘 **Dónde se aprende:** [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R7

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Cómo se explica en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- Se toman del texto de Holzmann: flujo simple sin recursión (R1), bucles con cota (R2), unas 60 líneas por función (R4), mínimo de dos aserciones por función (R5) y comprobar valores devueltos (R7).
- Paso 4 · Retorno. `leer(x)` se llama como sentencia y devuelve valor: R7.
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?
- 🔗 **Se estudia junto con:** R1, R2, R3, R4.

📘 **Dónde se aprende:** [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### RAIRS

- La RAIRS es una espectroscopía infrarroja de reflexión sobre una superficie metálica.

💡 **Cómo se explica en la clase [B68-C04](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md):**
- En RAIRS la calibración del espesor es distinta: Fayolle y colaboradores calibran la absorbancia de 1 ML con una desorción isotérmica monitoreada por RAIRS y la verifican con la TPD y con la exposición (9–10 ML).
- Fayolle y colaboradores (2011) vigilan el hielo con espectroscopía infrarroja de absorción–reflexión (RAIRS) y espectrometría de masas al mismo tiempo, con un flujo de sincrotrón del orden de `10¹⁴` fotones s⁻¹; Öberg y colaboradores (2009) usan una lámpara de hidrógeno de 7–10,5 eV a 15–60 K.
- 🎯 **Por qué importa:** Un hielo de 10 ML de CO sobre una superficie a 10 K se contamina con agua residual en horas si la presión de fondo no es lo bastante baja, y una TPD con bombeo insuficiente deforma el pico que se mide.
- 🔗 **Se estudia junto con:** ultra alto vacío (UHV), flujo de Hertz–Knudsen, probabilidad de adhesión, langmuir.

📘 **Dónde se aprende:** [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### RANSAC

- Un RANSAC (*random sample consensus*) ajusta un modelo a muestras mínimas aleatorias y elige el que más puntos explica.
- Ajuste de cuerpo rígido: transformación `(R, t)` que mejor lleva un conjunto al otro. RANSAC: ajusta con muestras mínimas aleatorias y se queda con el modelo de más inliers.
- Huber / IRLS: pesos `w = min(1, δ/|r|)` reajustados iterativamente (la teoría de M-estimadores no se consultó). RANSAC: ajuste con muestras mínimas aleatorias y recuento de inliers (F6).

💡 **Cómo se explica en la clase [B57-C30](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md):**
- Sobre el suelo filtrado, RANSAC recupera pendientes `0,1000` y `0,0500` (verdaderas: 0,1000 y 0,0500) con error máximo `0,0000` y `99,6%` de inliers.
- Sobre toda la nube, sin filtrar, el error máximo es `0,0002`: aquí el suelo es el 73 % de los puntos y RANSAC lo encuentra igual; con menos suelo (un bosque denso o una ciudad) fallaría.
- 🎯 **Por qué importa:** Un modelo de terreno malo hace que las pendientes y las alturas de los árboles salgan mal. La decisión central: ¿cómo se separa el suelo del resto con la menor contaminación y qué densidad de puntos hace falta?
- 🔗 **Se estudia junto con:** nube de puntos, filtro de suelo, recall, contaminación.

📘 **Dónde se aprende:** [B57-C30 · Nubes de puntos tridimensionales](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md); [B99-C01 · Odometría visual](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md); [B99-C07 · Robustez del mapeo ante entornos degradados](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md).

### RBF

- **Significa:** base radial (RBF).
- Un proceso gaussiano es un modelo que para cada entrada da una distribución normal; su núcleo (*kernel*) define cuánto se parecen las salidas de dos entradas cercanas, y el de base radial (RBF) tiene una longitud de escala por variable (S1).

💡 **Contexto en la clase [B17-C04](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md):**
- 🎯 **Por qué importa:** Un simulador de trayectoria, de aerodinámica o de transporte de radiación puede tardar minutos u horas por ejecución. Para explorar miles de combinaciones de parámetros (un análisis de sensibilidad, una propagación de incertidumbre, una optimización) no alcanza el tiempo.
- 🔗 **Se estudia junto con:** simulador, modelo sustituto, diseño de experimentos, secuencia de Sobol.

📘 **Dónde se aprende:** [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### RC

- **Significa:** Ritchey-Chrétien (RC).
- El Ritchey-Chrétien (RC) usa dos hiperboloides.

💡 **Cómo se explica en la clase [B43-C02](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md):**
- Obtener las conicidades de un Ritchey-Chrétien resolviendo dos condiciones.
- 🎯 **Por qué importa:** La geometría decide qué aberraciones quedan y cuánto mide el tubo. La decisión central: ¿qué conicidades de primario y secundario anulan la aberración esférica y el coma, y qué se paga en largo y obstrucción?
- 🔗 **Se estudia junto con:** cónica, Cassegrain clásico, aumento, coma.

📘 **Dónde se aprende:** [B43-C02 · Selección de geometría instrumental](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md).

### RCMC

- La RCMC es su corrección.

💡 **Cómo se explica en la clase [B69-C02](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md):**
- RC --> RCMC["corrección de migración (RCMC)"]
- Por el laboratorio: con y sin RCMC se compara la anchura.
- 🎯 **Por qué importa:** Sin procesamiento, un eco crudo parece ruido. La decisión central: ¿qué operaciones convierten el eco crudo en una imagen con la resolución teórica, y cuándo fallan?
- 🔗 **Se estudia junto con:** chirp, compresión en alcance, compresión en azimut, migración de celda.

📘 **Dónde se aprende:** [B69-C02 · Formación de imágenes SAR](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md).

### RCV

- El RCV es `√2·z·√(CVa² + CVi²)` (fórmula estándar, no consultada aquí).

💡 **Cómo se explica en la clase [B105-C24](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md):**
- I["CVi, CVa"] --> V["RCV = raiz2 z raiz(CVa^2+CVi^2)"]
- *Descripción textual:* el intervalo poblacional y el RCV personal son dos reglas para decidir si un valor es anómalo o ha cambiado; un umbral se evalúa con sensibilidad, especificidad y valor predictivo según la prevalencia.
- ⚠️ **Error frecuente:** Usar solo el intervalo poblacional para vigilar a una persona. Usa la línea base y el RCV (8.2).
- 🎯 **Por qué importa:** Con tripulaciones pequeñas, el intervalo de la población general es poco sensible a los cambios personales, y un umbral con baja prevalencia da más falsas alarmas que aciertos. La decisión central: ¿cuándo un cambio de un indicador es real y qué umbral equilibra sensibilidad y valor predictivo?
- 🔗 **Se estudia junto con:** intervalo de referencia, índice de individualidad, sensibilidad, especificidad.

📘 **Dónde se aprende:** [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md).

### RDM

- El RDM (*radiation design margin*) es el cociente exigido entre la dosis tolerada y la de misión.
- El RDM (*radiation design margin*) `= dosis de fallo / dosis de misión`.

💡 **Cómo se explica en la clase [B88-C03](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md):**
- D["Dosis de mision y de fallo"] --> M["RDM"]
- La misión acumula 20 krad(Si) y el componente falla a 60 krad(Si): `RDM = 3`.
- 🎯 **Por qué importa:** Un procesador comercial puede fallar en órbita por una sola partícula. La decisión central: ¿cuántos eventos esperar al año y qué margen de dosis hay respecto del fallo del componente?
- 🔗 **Se estudia junto con:** SEU, sección eficaz, LET umbral, Weibull.

📘 **Dónde se aprende:** [B88-C03 · Procesadores tolerantes a radiación](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md); [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### README

- Un README es el archivo de entrada de un proyecto: qué es, cómo instalarlo, cómo ejecutarlo y de dónde vienen los datos.

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Un README no sustituye las docstrings: el README describe el proyecto; las docstrings, cada pieza.
- Reproducir exige que otra persona, con tu README y tu registro, llegue al mismo resultado en su máquina.
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.
- 🔗 **Se estudia junto con:** Documentar, docstring, semilla, huella.

📘 **Dónde se aprende:** [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md).

### RID

- Un RID (*review item discrepancy*) es un hallazgo que debe cerrarse. «Lista» significa que pasan todos los criterios críticos; los no críticos se registran.

💡 **Cómo se explica en la clase [B83-C13](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md):**
- Estimar el tiempo para cerrar las acciones de revisión (RID).
- Acciones (RID): 10 en total, 3 criticas, capacidad 2 por semana -> 5 semanas para cerrar todas, 2 para las criticas
- ⚠️ **Error frecuente:** Cerrar RID sin evidencia. Registra la evidencia del cierre
- 🎯 **Por qué importa:** Una revisión aprobada sin criterios es un trámite; una revisión con criterios medibles es una decisión. La decisión central: ¿el proyecto cumple los criterios de entrada de la SRR y de la PDR y qué falta para llegar?
- 🔗 **Se estudia junto con:** SRR, PDR, criterio, crítico.

📘 **Dónde se aprende:** [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md).

### RK4

- **Significa:** Runge–Kutta de cuarto orden (RK4).
- La temperatura límite es `T_a − Q/G`. RK4 es un integrador de cuarto orden.
- El baricentro es el centro de masas del par. RK4 es el método de Runge–Kutta de cuarto orden.
- Euler explícito es de orden 1. RK4 es de orden 4.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B44-C08](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md):**
- Con paso de `0,5 s`, el error máximo de Euler es `0,01380 K` y el de RK4 `4,8 × 10⁻¹³ K`.
- Ejercicio 7. Error de Euler frente a RK4.
- 🎯 **Por qué importa:** La cámara no está fría al encenderla. La decisión central: ¿cuánto hay que esperar antes de calibrar y qué temperatura final se alcanza?
- 🔗 **Se estudia junto con:** capacidad térmica, conductancia, potencia de enfriamiento, constante de tiempo.

📘 **Dónde se aprende:** [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md); [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md); [B71-C03 · Ecuación de movimiento de dos cuerpos](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md); [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md); [B85-C26 · Análisis térmico transitorio y casos extremos](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md); [B97-C23 · Diseño de simulador de misión robótica](../programa/clases/B97/B97-C23-diseno-de-simulador-de-mision-robotica/CLASE.md) y 1 más.

### RMF

- La RMF es la matriz de redistribución de energía a canal.

💡 **Cómo se explica en la clase [B27-C22](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md):**
- RMF gaussiana con `σ = 0,1E`, normalizada de modo que cada columna suma 1.
- Con respuesta identidad, el plegado coincide con el cálculo directo a `10⁻⁹`; las columnas de la RMF suman 1;
- 🎯 **Por qué importa:** Ajustar un espectro «de fotones» directamente a las cuentas da resultados engañosos; hay que plegar el modelo con la respuesta y usar la estadística correcta para conteos pequeños. La decisión central: ¿qué parámetros recupera cada estadística y con qué sesgo cuando las cuentas son pocas?
- 🔗 **Se estudia junto con:** ARF, plegado, estadística de Cash, χ² con varianza igual a las cuentas.

📘 **Dónde se aprende:** [B27-C22 · Análisis espectral de rayos X y gamma: ajuste con respuesta instrumental](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md).

### RML

- WVR, el vapor de agua recuperado; RML `= TML − WVR`;

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- A["pesadas mi, mf, mh, dc"] --> B["TML, WVR, RML, CVCM"]
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?
- 🔗 **Se estudia junto con:** TML, WVR, CVCM, bakeout.

📘 **Dónde se aprende:** [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md).

### RMS

- El RMS mide la calidad.
- El sesgo es el residuo medio; el RMS, su raíz cuadrática media.
- El RMS mide la energía de la señal.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C22](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md):**
- La diferencia punto a punto entre ambos restos tiene `1,011 nm` RMS (ruido inyectado de 0,02 rad, equivalente a `0,02 λ/(4π) = 1,01 nm` por píxel).
- La superficie tiene `14,8` franjas en total; tras ajustar piston, inclinaciones y desenfoque queda un resto de `97,3 nm` PV y `19,90 nm` RMS (`0,0314 λ`).
- 🎯 **Por qué importa:** El mapa de error de forma es la prueba de aceptación de un espejo. La decisión central: ¿cómo se recupera la fase, qué se descuenta y qué PV y RMS quedan?
- 🔗 **Se estudia junto con:** desplazamiento de fase, fase, desenvolvimiento, ajuste de modos.

📘 **Dónde se aprende:** [B43-C22 · Interferometría de superficie y mapas de error de forma](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md); [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md); [B47-C10 · Estabilidad de apuntamiento](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md); [B85-C14 · Degradación ultravioleta](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md); [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md); [B97-C26 · Monitoreo de condición de maquinaria extraterrestre](../programa/clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md).

### RMSE

- **Significa:** error cuadrático medio (RMSE).
- El error cuadrático medio (RMSE) es `√[Σ(xᵢ − x_ref)²/n]`.
- El RMSE es la raíz del error cuadrático medio.
- MAE es el error absoluto medio, RMSE el cuadrático medio, AbsRel la media de `|ẑ − z|/z` y delta1 la fracción de puntos con `máx(z/ẑ, ẑ/z) < 1,25`.

💡 **Cómo se explica en la clase [B13-C03](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md):**
- *Descripción textual:* de una serie salen dos cantidades independientes, el sesgo y la desviación típica; juntas componen el error cuadrático medio.
- Calcular sesgo, desviación típica y error cuadrático medio de una serie.
- 🎯 **Por qué importa:** Un telémetro láser que mide la distancia a un reflector de prueba puede dar lecturas muy agrupadas pero todas desplazadas: es repetible y, aun así, está mal. Otro puede dar lecturas dispersas que, en promedio, caen sobre el valor correcto.
- 🔗 **Se estudia junto con:** exactitud de medida, veracidad, precisión de medida, error de medida.

📘 **Dónde se aprende:** [B13-C03 · Exactitud frente a precisión](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md); [B33-C01 · Validación de modelos MHD con eventos solares documentados](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md); [B33-C12 · Pronóstico de llegada y severidad de CME](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md); [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md).

### RMSF

- La RMSF es su respuesta a una fuente puntual.

💡 **Cómo se explica en la clase [B46-C13](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md):**
- Con una fuente sintética de `RM = 60 rad/m²` y `p = 0,3`, la síntesis da el pico en `59,5 rad/m²` (amplitud `0,297`) y el ajuste `59,54 rad/m²`; la RMSF mide `61,3 rad/m²`.
- Ejercicio 6. ¿Cuánto vale la RMSF para `Δλ² = 0,113 m²`?
- 🎯 **Por qué importa:** El ángulo de polarización gira con `λ²`, y hay que medirlo en varias frecuencias para saber cuánto. La decisión central: ¿cómo se obtiene la medida de rotación sin ambigüedad de `nπ`?
- 🔗 **Se estudia junto con:** parámetros de Stokes, polarización lineal, rotación de Faraday, síntesis de RM.

📘 **Dónde se aprende:** [B46-C13 · Polarimetría de radio](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md).

### ROE

- La ROE (razón de onda estacionaria) `(1 + |Γ|)/(1 − |Γ|)`.

💡 **Cómo se explica en la clase [B49-C02](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md):**
- El patrón de ondas estacionarias de esa carga da ROE muestreada `1,64872`, igual a la analítica (`|Γ| = 0,24492`).
- Una ROE de 1,46 pierde solo 0,155 dB; una de 5 pierde 2,55 dB.
- ⚠️ **Error frecuente:** Confundir ROE y pérdida de retorno. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una antena desadaptada devuelve potencia y empeora la sensibilidad. La decisión central: ¿cuánta potencia se refleja y cómo se adapta con un tramo de línea?
- 🔗 **Se estudia junto con:** coeficiente de reflexión, pérdida de retorno, carta de Smith, longitud eléctrica.

📘 **Dónde se aprende:** [B49-C02 · Adaptación de impedancias y líneas de transmisión en antenas](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md).

### RPE

- ATE: RMSE de la traslación tras alinear la estimación con la verdad por cuerpo rígido (F2). RPE: error del movimiento relativo entre pares de poses separados por una ventana (F2).

💡 **Cómo se explica en la clase [B99-C06](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md):**
- Para el RPE se mide el error del movimiento relativo entre pares de poses, y la opción de ventana fija permite comparar cada pose con otra posterior a una separación dada (en segundos, metros, radianes o cuadros), útil para estimar la deriva.
- La página no escribe las fórmulas del RMSE ni del RPE; las que siguen son las del laboratorio.
- ⚠️ **Error frecuente:** Creer que ATE bajo implica RPE bajo. El grafo bajó el ATE sin cambiar el RPE (8.5).
- 🎯 **Por qué importa:** «Mi robot deriva poco» no es una afirmación comprobable. La decisión central: ¿qué métrica, con qué alineación y con qué ventana, describe el error que importa para la tarea?
- 🔗 **Se estudia junto con:** ATE, Alineación, Ventana (delta), Deriva.

📘 **Dónde se aprende:** [B99-C06 · Evaluación de deriva y error de trayectoria](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md).

### RPN

- El RPN es `S×O×D`.

💡 **Cómo se explica en la clase [B83-C22](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md):**
- Ejemplo: rueda de reacción, modo «fricción creciente», efecto «apuntamiento degradado», `S = 6`, `O = 5`, `D = 5`: `RPN = 150`, el mayor.
- La batería (cortocircuito de celda, `S = 9`) tiene RPN 135 y `p = 1,56 %`.
- ⚠️ **Error frecuente:** Multiplicar escalas ordinales como si fueran números exactos. Usa el RPN para priorizar, no como medida absoluta
- 🎯 **Por qué importa:** Los fallos que no se anticipan se descubren en órbita. La decisión central: ¿qué modos de fallo hay que atacar primero, cuánta probabilidad tienen en la vida de la misión y qué cambia si mejoro su detección?
- 🔗 **Se estudia junto con:** modo de fallo, efecto, S, O.

📘 **Dónde se aprende:** [B83-C22 · Análisis de modos y efectos de fallo (FMEA) en sistemas espaciales](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md).

### RPO

- El RPO es la pérdida máxima de datos aceptable, medida en tiempo.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- Con RPO de 4 h, una copia cada 1 h cumple (pérdida máxima 1 h) y cada 6 h o 24 h no.
- D["copias cada T"] --> P["perdida maxima = T vs RPO"]
- ⚠️ **Error frecuente:** Confundir RPO con RTO. El RPO es de datos y el RTO de servicio; ver sección 6.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?
- 🔗 **Se estudia junto con:** disponibilidad, MTBF, MTTR, RTO.

📘 **Dónde se aprende:** [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### RQ

- **Significa:** Cociente respiratorio (RQ).
- Consumo específico de oxígeno: O₂ por kilogramo y minuto. Cociente respiratorio (RQ): mol de CO₂ por mol de O₂.

💡 **Cómo se explica en la clase [B106-C01](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md):**
- Obtener el CO₂ exhalado con un cociente respiratorio y escalar el balance a una tripulación.
- 🎯 **Por qué importa:** Un hábitat se diseña de adentro hacia afuera: primero lo que consume y emite la tripulación, después la máquina que lo repone. Si el balance humano está mal, todo el ECLSS queda mal dimensionado.
- 🔗 **Se estudia junto con:** Consumo específico de oxígeno, Normoxia, Zona de salud, zona de desempeño.

📘 **Dónde se aprende:** [B106-C01 · Requisitos de habitabilidad](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md).

### RRW

- El RRW (*rate random walk*) `K` es la deriva aleatoria del sesgo, en `rad/s/√s`.

💡 **Cómo se explica en la clase [B87-C06](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md):**
- G["tasa medida = verdad + ARW + sesgo RRW"] --> P["promedios de duracion tau"]
- Analogía: un reloj que se adelanta con un tic aleatorio (ARW) y que además cambia de ritmo a lo largo del día (RRW): para periodos cortos domina el tic y para largos domina el cambio de ritmo.
- 🎯 **Por qué importa:** Entre dos medidas de un sensor de vector, la actitud se propaga integrando el giroscopio, y esa integración se desvía. La decisión central: ¿cada cuánto hay que corregir con otro sensor, y qué parte de la deriva es ruido blanco y cuál sesgo?
- 🔗 **Se estudia junto con:** ARW, varianza de Allan, inestabilidad de sesgo, tasa de muestreo.

📘 **Dónde se aprende:** [B87-C06 · Giroscopios MEMS](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md).

### RSET

- El RSET (*required safe egress time*) es el tiempo necesario: detección, reunión, traslado, paso por escotilla y verificación.

💡 **Cómo se explica en la clase [B110-C03](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md):**
- Con `N = 4` y sin varianza, `RSET = 20 + 60 + 90 + 4 × 20 + 120 = 370 s`; el laboratorio lo reproduce de forma exacta.
- Pasar de 2 a 6 personas añade `1,78 min` al RSET mediano por el cuello de botella de la escotilla y por el máximo de las reuniones.
- ⚠️ **Error frecuente:** Tomar el RSET como un número único. Es una distribución con cola larga (8.2 y 8.3).
- 🎯 **Por qué importa:** Ninguna clase anterior trata evacuación, refugio y vehículos de escape. La decisión central: ¿alcanza el margen entre ASET y RSET, y cuánto de ese margen depende de supuestos que no se conocen?
- 🔗 **Se estudia junto con:** ASET, margen, refugio, cuello de botella.

📘 **Dónde se aprende:** [B110-C03 · Evacuación y refugio de emergencia](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md).

### RSS

- **Significa:** suma en cuadratura (RSS).
- La RSS es `√Σtᵢ²`.
- El RSS suma errores independientes en cuadratura.
- El RSS (raíz de la suma de cuadrados) combina contribuyentes independientes.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B84-C16](../programa/clases/B84/B84-C16-tolerancias-de-fabricacion/CLASE.md):**
- Si D pasa a `± 0,04`: RSS `0,1382` y peor caso `0,290 mm`, que ya cumple.
- RSS o Monte Carlo cuando el proceso está controlado y se acepta un riesgo declarado.
- ⚠️ **Error frecuente:** Sumar tolerancias por RSS en funciones críticas. Se corrige con 8.4.
- 🎯 **Por qué importa:** El peor caso rechaza diseños que en la práctica funcionan y la RSS acepta riesgos que hay que cuantificar; elegir sin cálculo cuesta o dinero o fallas. La decisión central: ¿cumple el hueco del ensamble y con qué probabilidad, según el método de apilamiento?
- 🔗 **Se estudia junto con:** peor caso, Monte Carlo, contribución.

📘 **Dónde se aprende:** [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md); [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md); [B84-C16 · Tolerancias de fabricación](../programa/clases/B84/B84-C16-tolerancias-de-fabricacion/CLASE.md); [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md); [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md); [B90-C05 · Documentación de interfaces](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md).

### RTG

- Un RTG (*radioisotope thermoelectric generator*) convierte el calor del decaimiento en electricidad sin partes móviles.

💡 **Contexto en la clase [B86-C16](../programa/clases/B86/B86-C16-generadores-radioisotopicos/CLASE.md):**
- 🎯 **Por qué importa:** Un generador radioisotópico no depende de la distancia al Sol ni del eclipse, pero su potencia decae con el combustible y con los termopares y su eficiencia es baja. Entender esa curva decide qué misiones lo usan.
- 🔗 **Se estudia junto con:** GPHS, vida media, degradación del termopar, eficiencia de sistema.

📘 **Dónde se aprende:** [B86-C16 · Generadores radioisotópicos](../programa/clases/B86/B86-C16-generadores-radioisotopicos/CLASE.md).

### RTLT

- El RTLT es el tiempo de ida y vuelta de la luz.

💡 **Cómo se explica en la clase [B75-C19](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md):**
- `50,6 %` por muestreo) tiene un RTLT mayor que 30 min.
- Reacción = `RTLT + 1800 s` (sintético): `2323 s` en el mínimo, `3489 s` en el medio y `4319 s` en el máximo.
- ⚠️ **Error frecuente:** Confundir retardo unidireccional con RTLT. Se corrige con la sección 6.
- 🎯 **Por qué importa:** No se puede dirigir desde la Tierra lo que sucede en minutos. La decisión central: ¿qué eventos duran menos que el tiempo mínimo de reacción desde tierra y por tanto deben ser autónomos?
- 🔗 **Se estudia junto con:** retardo unidireccional, tiempo de reacción, autonomía, conjunción solar.

📘 **Dónde se aprende:** [B75-C19 · Restricciones de navegación autónoma](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md).

### RTO

- El RTO es el tiempo objetivo para restablecer el servicio; el WRT es el tiempo adicional para recuperar el trabajo; el MTD es el tiempo máximo tolerable de interrupción.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- F["fallo"] --> R["recuperar el servicio: RTO"]
- *Descripción textual:* desde el fallo corren el RTO y el WRT, cuya suma no debe pasar del MTD, mientras el costo crece; el RPO limita el intervalo entre copias.
- ⚠️ **Error frecuente:** Confundir RTO con MTTR. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?
- 🔗 **Se estudia junto con:** disponibilidad, MTBF, MTTR, WRT.

📘 **Dónde se aprende:** [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### RTT

- **Significa:** Ida y vuelta (RTT); latencia (RTT).
- La latencia (RTT) es el tiempo de ida y vuelta.
- Retardo de propagación: `d/c`. Ida y vuelta (RTT): `2d/c`.

💡 **Cómo se explica en la clase [B96-C01](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md):**
- Un satélite geoestacionario está a 35 786 km: la ida y vuelta es de 0,239 s.
- Marte, entre 5,5×10⁷ y 4×10⁸ km, impone de 367 s a 2 669 s de ida y vuelta.
- ⚠️ **Error frecuente:** Confundir ida con ida y vuelta. El ciclo de un comando usa `2d/c` (8.2)
- 🎯 **Por qué importa:** Quien opera una nave no puede tratarla como un equipo de laboratorio: cada comando viaja a la velocidad de la luz y cada contacto dura minutos. La decisión central: ¿qué segmento hace qué y cuánto tardan en comunicarse?
- 🔗 **Se estudia junto con:** Segmento espacial, Segmento terrestre, MOC/SOC, Retardo de propagación.

📘 **Dónde se aprende:** [B96-C01 · Segmento espacial y segmento terrestre](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md); [B128-C10 · Acceso con baja conectividad](../programa/clases/B128/B128-C10-acceso-con-baja-conectividad/CLASE.md).

### RUE

- **Significa:** eficiencia de uso de la radiación (RUE).
- La eficiencia de uso de la radiación (RUE) son los gramos de biomasa por mol de fotones.

💡 **Cómo se explica en la clase [B115-C02](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md):**
- Wheeler (NASA/KSC) tabula el área necesaria para el oxígeno de una persona: con 500 µmol m⁻² s⁻¹ y una eficiencia de uso de la radiación de 0,75 g/mol, 31,5 m².
- 🎯 **Por qué importa:** La luz es el mayor consumo eléctrico de un cultivo cerrado. La decisión central: ¿cuántos fotones por metro cuadrado y día hacen falta, con qué eficacia se producen y qué potencia y calor suponen para el hábitat?
- 🔗 **Se estudia junto con:** flujo de fotones fotosintéticos (PPFD), integral diaria de luz (DLI), fotoperiodo, eficacia fotónica.

📘 **Dónde se aprende:** [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### RUL

- **Significa:** vida útil restante (RUL).
- La vida útil restante (RUL) es el tiempo hasta que el indicador cruza su umbral.
- La RUL `= t_cruce − t_actual`.

💡 **Cómo se explica en la clase [B88-C44](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md):**
- *Descripción textual:* la serie se ajusta con un modelo exponencial; el cruce del umbral da la RUL; el remuestreo da su intervalo y la política decide si alertar.
- El ajuste da `a = 1,9958`, `b = 0,000601 /h`; la RUL estimada es `88,1` días (real `88,2`); el intervalo de remuestreo 95 % es `[86,5; 89,6]` días.
- 🎯 **Por qué importa:** Detectar una falla (C12) llega tarde para planificar; anticiparla da tiempo para actuar. La decisión central: ¿cuándo cruzará el umbral y con qué incertidumbre, para decidir si alertar?
- 🔗 **Se estudia junto con:** ajuste, cruce, remuestreo, política de alerta.

📘 **Dónde se aprende:** [B88-C44 · Mantenimiento predictivo y pronóstico de salud de sistemas](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md); [B97-C26 · Monitoreo de condición de maquinaria extraterrestre](../programa/clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md).

### SA

- **Significa:** asociación de seguridad (SA).
- Una asociación de seguridad (SA) fija algoritmo, clave, tamaño de etiqueta y ventana.

💡 **Cómo se explica en la clase [B89-C25](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md):**
- Los parámetros de la asociación de seguridad incluyen algoritmo, clave, máscara de autenticación y ventana de secuencia.
- SA["asociacion de seguridad: SPI, clave, ventana"] --> TX["emisor: etiqueta = MAC(clave, SPI, ASN, carga)"]
- 🎯 **Por qué importa:** Los comandos son la superficie más sensible de una misión; sin autenticación y sin protección contra repetición, una trama capturada podría reutilizarse, y un CRC solo detecta errores, no ataques (C12). La decisión central: ¿cómo garantizar que una trama es auténtica, íntegra y no repetida, y cuánto cuesta en sobrecarga?
- 🔗 **Se estudia junto con:** protocolo de seguridad de enlace de datos (SDLS), cifrado autenticado AES en modo Galois/Counter (GCM), SPI, ventana anti-repetición.

📘 **Dónde se aprende:** [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md).

### SAFE

- Un SAFE es un instrumento que se convierte en acciones en una ronda posterior.

💡 **Cómo se explica en la clase [B126-C01](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md):**
- Con `C` acciones previas, el SAFE recibe `s` acciones tales que `s/(C+s) = INV/CAP`.
- Si el precio de la ronda es `P = V/(C+s)` y el SAFE paga `(1 − d)P`, entonces `s = INV/((1 − d)P)`.
- 🎯 **Por qué importa:** El catálogo trata el financiamiento privado en general (B124-C07, «Financiamiento privado», en la [guía del bloque B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md)), no la mecánica de las etapas iniciales.
- 🔗 **Se estudia junto con:** tope de valoración, descuento, ronda con precio, tabla de capitalización.

📘 **Dónde se aprende:** [B126-C01 · Capital semilla y financiamiento inicial](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md).

### SAM

- **Significa:** ángulo espectral (SAM).
- El ángulo espectral (SAM) es `arccos(u·v/(|u||v|))`.

💡 **Cómo se explica en la clase [B53-C29](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md):**
- Los ángulos espectrales entre miembros son `11,3°`, `13,6°` y `9,3°`.
- Calcular el ángulo espectral entre miembros extremos.
- 🎯 **Por qué importa:** Un píxel gris puede ser una mezcla de tres minerales. La decisión central: ¿qué abundancias explican el espectro de un píxel y con qué error, dado el ruido y la similitud entre miembros extremos?
- 🔗 **Se estudia junto con:** miembro extremo, abundancia, mezcla lineal.

📘 **Dónde se aprende:** [B53-C29 · Imágenes hiperespectrales de superficies planetarias](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md).

### SAVI

- El SAVI agrega una constante `L` al denominador para atenuar el efecto del suelo.

💡 **Cómo se explica en la clase [B57-C06](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md):**
- Con SAVI (`L = 0,5`) las cifras son `0,404` y `0,387`: diferencia `0,017`.
- Descripción larga: la curva del NDVI sube rápido y se aplana, y el SAVI reduce la diferencia entre suelos a cerca de una quinta parte.
- 🎯 **Por qué importa:** Un índice facilita comparar fechas y lugares, pero también esconde supuestos. La decisión central: ¿cuándo el NDVI mide de verdad la cantidad de vegetación y cuándo lo engañan la saturación o el suelo?
- 🔗 **Se estudia junto con:** NDVI, LAI, saturación, suelo de fondo.

📘 **Dónde se aprende:** [B57-C06 · Índices de vegetación](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md).

### SBC

- En SBC se repite `R` veces: (1) sortear un parámetro `θ̃` del prior, (2) simular datos `ỹ` con `θ̃`, (3) obtener `L` sorteos de la posterior dado `ỹ`, (4) calcular el rango de `θ̃` entre ellos (cuántos sorteos son menores).

💡 **Cómo se explica en la clase [B19-C08](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md):**
- SBC es hacer esa prueba de forma sistemática.
- Límite de la analogía: la calibración que prueba SBC es *promedio sobre el prior*.
- 🎯 **Por qué importa:** Un intervalo del 90 % que cubre el valor verdadero solo la mitad de las veces es peor que no tener intervalo: transmite una seguridad falsa. Los diagnósticos de C04 dicen si el cómputo funcionó; los chequeos de C06 si el modelo reproduce los datos.
- 🔗 **Se estudia junto con:** calibrado, cobertura, precisión, rango.

📘 **Dónde se aprende:** [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md).

### SCID

- El SCID identifica la nave; el VCID, el canal virtual.

💡 **Cómo se explica en la clase [B94-C03](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md):**
- Paso 2 · Primeros 16 bits. `0x2A53 = 0010 1010 0101 0011`: versión `00`, SCID `10 1010 0101 = 0x2A5`, VCID `001`, OCF `1`.
- Una trama sintética de 64 octetos lleva SCID `0x2A5`, canal virtual 1, contadores 255 y 7 y puntero 10.
- 🎯 **Por qué importa:** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?
- 🔗 **Se estudia junto con:** trama de transferencia de telemetría, VCID, contador de canal maestro, canal virtual.

📘 **Dónde se aprende:** [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### SCLK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- En el laboratorio se resuelven 6 archivos; todos existen y LSK y SCLK están antes que los SPK (las dos comprobaciones valen 1 = sí: `1` y `1`).
- Por tipo: SPK, CK, PCK, IK, FK, LSK, SCLK.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, CK, PCK.

📘 **Dónde se aprende:** [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### SDLS

- **Significa:** protocolo de seguridad de enlace de datos (SDLS).
- El protocolo de seguridad de enlace de datos (SDLS) de la CCSDS protege tramas con autenticación y/o cifrado.

💡 **Cómo se explica en la clase [B89-C25](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md):**
- Explicar qué servicios da el protocolo de seguridad de enlace de datos según la CCSDS 355.0-B-2.
- 🎯 **Por qué importa:** Los comandos son la superficie más sensible de una misión; sin autenticación y sin protección contra repetición, una trama capturada podría reutilizarse, y un CRC solo detecta errores, no ataques (C12). La decisión central: ¿cómo garantizar que una trama es auténtica, íntegra y no repetida, y cuánto cuesta en sobrecarga?
- 🔗 **Se estudia junto con:** cifrado autenticado AES en modo Galois/Counter (GCM), asociación de seguridad (SA), SPI, ventana anti-repetición.

📘 **Dónde se aprende:** [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md).

### SDP4

- SGP4 es el modelo para periodos menores de `225 min`; SDP4 añade efectos lunisolares y resonantes para los demás.

💡 **Cómo se explica en la clase [B72-C21](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md):**
- Con `n = 6,4 rev/día` el periodo es exactamente `225 min` y se clasifica como SDP4;
- *Descripción textual:* el conjunto de dos líneas se lee y valida; el movimiento medio publicado se convierte al de Brouwer; el periodo decide entre SGP4 y SDP4; con el semieje corregido se obtienen las tasas seculares.
- 🎯 **Por qué importa:** Un error clásico es tomar los elementos de dos líneas como elementos keplerianos y propagarlos con dos cuerpos: el error es de kilómetros en minutos. La decisión central: ¿qué propagador corresponde a un conjunto de elementos y qué transformaciones previas exige antes de usarlo?
- 🔗 **Se estudia junto con:** conjunto de dos líneas, SGP4, movimiento medio de Kozai, Brouwer.

📘 **Dónde se aprende:** [B72-C21 · Propagador SGP4 y teoría general de perturbaciones](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md).

### SECDED

- La paridad global distingue uno de dos errores. SECDED corrige uno y detecta dos.

💡 **Cómo se explica en la clase [B88-C04](../programa/clases/B88/B88-C04-memorias-y-correccion-de-errores/CLASE.md):**
- Codificar y decodificar una palabra con SECDED.
- Ejercicio 9 · transferencia. Transferencia. Un colega dice que SECDED protege contra cualquier radiación.
- ⚠️ **Error frecuente:** Creer que SECDED corrige dos errores. Corrige uno y detecta dos (8.2)
- 🎯 **Por qué importa:** Sin corrección, un SEU corrompe un dato; con SECDED lo corrige al leerlo, pero si dos errores se acumulan en la misma palabra el código ya no corrige. La decisión central: ¿cada cuánto hay que barrer la memoria para que la probabilidad de doble error sea aceptable?
- 🔗 **Se estudia junto con:** código Hamming, síndrome, paridad global, barrido.

📘 **Dónde se aprende:** [B88-C04 · Memorias y corrección de errores](../programa/clases/B88/B88-C04-memorias-y-correccion-de-errores/CLASE.md).

### SED

- La SED es `νF_ν` frente a `ν`.

💡 **Cómo se explica en la clase [B27-C20](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md):**
- La SED tiene dos jorobas; cada una es casi una parábola cerca de su máximo.
- SED["SED sintética + ruido"] --> LP["ajuste log-parábola por joroba"]
- ⚠️ **Error frecuente:** Ajustar toda la SED con una parábola. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El caso de GW170817 con GRB 170817A mostró el valor de combinar mensajeros y bandas. La decisión central: ¿dónde están los picos de las dos jorobas y qué retardo hay entre dos bandas?
- 🔗 **Se estudia junto con:** log-parábola, pico, correlación cruzada, retardo.

📘 **Dónde se aprende:** [B27-C20 · Análisis multibanda de un evento extremo](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md).

### SEE

- El SEE es el error estándar de la estimación en escala logarítmica.

💡 **Cómo se explica en la clase [B124-C05](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md):**
- La desviación de predicción incluye el SEE y la distancia al centro de los datos; con `z = 1,2816` el intervalo al 80 % es `[22,27, 39,07]` y contiene el valor verdadero `30,35`.
- Que la masa explica solo parte del costo; el resto está en el SEE y en atributos no incluidos (complejidad, madurez tecnológica).
- 🎯 **Por qué importa:** Un costo sin banda de incertidumbre parece más preciso de lo que es. La decisión central: ¿cuánto cuesta esta misión, con qué banda y cuánto baja el costo unitario si se fabrican varias unidades?
- 🔗 **Se estudia junto con:** relación de estimación de costo (CER), escala log-log, intervalo de predicción, curva de aprendizaje.

📘 **Dónde se aprende:** [B124-C05 · Estimación de costos de misión](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md).

### SEFD

- El SEFD `2kT_sys/A_e`.

💡 **Cómo se explica en la clase [B46-C20](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md):**
- I["conjunto de 6 antenas"] --> SS["sigma_S con SEFD"]
- Ejercicio 8. SEFD si `T_sys` sube de 35 a 70 K.
- 🎯 **Por qué importa:** Un proyecto viable cuadra objetivo, sensibilidad, tiempo y datos. La decisión central: ¿cuánto tiempo de observación pide el objetivo y con qué margen?
- 🔗 **Se estudia junto con:** objetivo científico, criterio de detección, presupuesto de sensibilidad, conmutación en posición.

📘 **Dónde se aprende:** [B46-C20 · Proyecto de observación radioastronómica](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md).

### SEL

- El SEU es un cambio de estado de un bit por una partícula, no destructivo; el SEL (*latch-up*) es un estado de corriente alta potencialmente destructivo.

💡 **Cómo se explica en la clase [B95-C02](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md):**
- Límite: el modelo usa tasa constante y conmutador ideal; no incluye SEL ni SEU, que se mitigan con detección y reinicio.
- No: la TID no cubre el SEL, que es otro mecanismo; se necesita detección y corte de corriente o un ensayo de SEL.
- 🎯 **Por qué importa:** Un componente comercial puede funcionar bien en tierra y degradarse o fallar en órbita. La decisión central: ¿qué componente comercial se puede usar en esta misión, con qué margen de radiación y con qué fiabilidad del conjunto?
- 🔗 **Se estudia junto con:** COTS, TID, SEU, RDM.

📘 **Dónde se aprende:** [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### SEM

- El SEM es `SD √(1 − ICC)`.

💡 **Cómo se explica en la clase [B105-C26](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md):**
- Promediar `k` sesiones da `SEM = 4/√k`: 4,00 (1); 2,83 (2) y 2,00 (4); el MDC95 baja a 11,09; 7,84 y 5,54.
- *Descripción textual:* la variación entre y dentro de individuos da el ICC; con él se calcula el SEM y el cambio mínimo detectable; promediar sesiones lo reduce, y el número de participantes determina la incertidumbre de la fiabilidad estimada.
- 🎯 **Por qué importa:** Un biomarcador con alta variación interna no detecta cambios pequeños aunque sea «preciso». Con pocos participantes, además, el propio ICC es incierto.
- 🔗 **Se estudia junto con:** ICC(1,1), MDC95, límites de acuerdo, Bland–Altman.

📘 **Dónde se aprende:** [B105-C26 · Medidas fisiológicas y biomarcadores en investigación espacial](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md).

### SEP

- El CEP es el radio del círculo horizontal con 50 % de probabilidad; el SEP, de la esfera con 50 %.

💡 **Cómo se explica en la clase [B74-C19](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md):**
- Con `σ = (3; 1,2; 2) m`: RMS 3D `3,8000 m` (muestral `3,8012 m`), percentil 95 de la norma 3D `6,493 m`, SEP (50 %) `3,190 m`, CEP (50 %, horizontal) `2,425 m`.
- Un error de posición sintético con `σ = (3,0; 1,2; 2,0) m` tiene RMS 3D `3,8000 m`, CEP `2,425 m`, SEP `3,190 m` y percentil 95 3D de `6,493 m`.
- 🎯 **Por qué importa:** Dos informes pueden decir «3 m» y referirse a cosas distintas (RMS, 50 %, 95 %). La decisión central: ¿qué métrica comunica el riesgo que importa, con qué probabilidad y con qué incertidumbre muestral?
- 🔗 **Se estudia junto con:** RMS 3D, CEP, 2DRMS, percentil.

📘 **Dónde se aprende:** [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md).

### SEU

- El SEU es un cambio de estado de un bit por una partícula, no destructivo; el SEL (*latch-up*) es un estado de corriente alta potencialmente destructivo.
- El SEU (*single event upset*) invierte un bit.

💡 **Cómo se explica en la clase [B88-C03](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md):**
- S["Seccion eficaz por bit"] --> R["Tasa SEU = sigma x bits x flujo"]
- *Descripción textual:* la sección eficaz, los bits y el flujo dan la tasa de SEU y sus conteos anuales; la dosis da el margen; ambos forman la ficha de radiación.
- ⚠️ **Error frecuente:** Confundir SEU con TID. SEU es instantáneo y TID acumulativo (ejercicio 11)
- 🎯 **Por qué importa:** Un procesador comercial puede fallar en órbita por una sola partícula. La decisión central: ¿cuántos eventos esperar al año y qué margen de dosis hay respecto del fallo del componente?
- 🔗 **Se estudia junto con:** sección eficaz, LET umbral, Weibull, RDM.

📘 **Dónde se aprende:** [B88-C03 · Procesadores tolerantes a radiación](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md); [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### SGP4

- El conjunto de dos líneas (TLE) son dos líneas de 69 caracteres con los elementos medios. SGP4 es el modelo para periodos menores de `225 min`;

💡 **Cómo se explica en la clase [B72-C21](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md):**
- El periodo es `2π/n₀″ = 92,914 min`, menor de `225 min`: SGP4.
- Con las constantes de SGP4: `Ω̇ = −4,9580 °/día`, `ω̇ = 3,7081 °/día`.
- ⚠️ **Error frecuente:** Creer que el laboratorio valida SGP4. Se corrige con la sección 11.
- 🎯 **Por qué importa:** Un error clásico es tomar los elementos de dos líneas como elementos keplerianos y propagarlos con dos cuerpos: el error es de kilómetros en minutos. La decisión central: ¿qué propagador corresponde a un conjunto de elementos y qué transformaciones previas exige antes de usarlo?
- 🔗 **Se estudia junto con:** conjunto de dos líneas, SDP4, movimiento medio de Kozai, Brouwer.

📘 **Dónde se aprende:** [B72-C21 · Propagador SGP4 y teoría general de perturbaciones](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md).

### SHA-256

- Una huella (*hash*) es un número de longitud fija calculado a partir del contenido de un archivo; si el contenido cambia, la huella cambia. SHA-256 es una función de huella de 256 bits.
- Un hash (huella) es una función que resume un contenido; SHA-256 produce 256 bits, que se escriben como 64 caracteres hexadecimales.
- Un manifiesto lista cada archivo con su huella. SHA-256 es una función hash de 256 bits.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Por ejemplo: `"""Devuelve la huella SHA-256 (hexadecimal) del contenido de un archivo."""`.
- D["datos<br/>+ huella SHA-256"] --> E["ejecución"]
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.
- 🔗 **Se estudia junto con:** Documentar, docstring, README, semilla.

📘 **Dónde se aprende:** [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md); [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B48-C17 · Gestión de archivos observacionales](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md); [B90-C18 · Trazabilidad de evidencias](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md); [B96-C22 · Transferencia de datos entre estación y centro de datos](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md); [B130-C06 · Publicación de un proyecto educativo](../programa/clases/B130/B130-C06-publicacion-de-un-proyecto-educativo/CLASE.md).

### SI

- **Significa:** Sistema Internacional (SI); Sistema Internacional de Unidades (SI).
- El Sistema Internacional (SI) es el conjunto de unidades coherentes acordado por la comunidad internacional; sus siete unidades base son segundo, metro, kilogramo, amperio, kelvin, mol y candela (S1, S2).
- El SI (Sistema Internacional de Unidades) es el sistema acordado internacionalmente; sus siete unidades base son el segundo (s), el metro (m), el kilogramo (kg), el amperio (A), el kelvin (K), el mol (mol) y la candela (cd), definidas a partir de siete constantes definitorias de valor exacto (S2).
- El Sistema Internacional (SI) es el conjunto de unidades acordado internacionalmente; tiene siete unidades base: segundo, metro, kilogramo, amperio, kelvin, mol y candela (S1).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C06](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md):**
- Para saber si una unidad es coherente basta con reconstruirla desde las base.
- La tabla del SI llega hoy hasta ronna `10²⁷`, quetta `10³⁰`, ronto `10⁻²⁷` y quecto `10⁻³⁰` (S2).
- 🎯 **Por qué importa:** El 23 de septiembre de 1999 la NASA perdió contacto con la sonda Mars Climate Orbiter. Según la agencia, un error de navegación se debió a no traducir unidades inglesas a métricas: el programa en tierra usaba unas y el de la nave otras, y la sonda pasó demasiado cerca de Marte y se quemó en su atmósfera (S1).
- 🔗 **Se estudia junto con:** magnitud, unidad, unidades base, constantes definitorias.

📘 **Dónde se aprende:** [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md); [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md); [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md); [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### SIL

- SIL: software en el computador de desarrollo.

💡 **Cómo se explica en la clase [B88-C41](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md):**
- L["Misma ley de control"] --> S["SIL: doble precision"]
- La evidencia es la presupuesto de error numérico SIL/PIL del ejercicio 12 (sección 20).
- ⚠️ **Error frecuente:** Creer que SIL basta. Hace falta PIL y HIL (8.4)
- 🎯 **Por qué importa:** La aritmética del procesador objetivo puede ser distinta de la del escritorio. La decisión central: ¿cuánto se aparta la respuesta con la precisión del objetivo y cumple la tolerancia?
- 🔗 **Se estudia junto con:** PIL, HIL, épsilon, LSB.

📘 **Dónde se aprende:** [B88-C41 · Pruebas SIL y PIL del software de vuelo](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md).

### SIS

- **Significa:** esfera isoterma singular (SIS).
- La esfera isoterma singular (SIS) tiene `ρ ∝ r⁻²` y `M(<r) = 2σ² r/G`.
- Para una esfera isoterma singular (SIS) con dispersión `σ`, `θ_E = 4π(σ/c)² D_ls/D_s`.

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- Comparar esa masa con la de una esfera isoterma singular obtenida de la dispersión de las galaxias.
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.
- 🔗 **Se estudia junto con:** cúmulo de galaxias, medio intracúmulo (ICM), temperatura, equilibrio hidrostático.

📘 **Dónde se aprende:** [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md); [B25-C14 · Lentes gravitacionales galácticas](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md).

### SLA

- El SLO es el objetivo de nivel de servicio; el SLA, el acuerdo que fija consecuencias si no se cumple.

💡 **Cómo se explica en la clase [B124-C21](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md):**
- Que el servicio puede estar «arriba» pero entregando datos lentos o incompletos; el SLA debería incluir el plazo y la calidad del producto.
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué conviene un SLO interno más estricto que el SLA?
- 🎯 **Por qué importa:** B124 trata propuestas de valor, pero un servicio de observación se compromete con plazos y calidad, y esos compromisos tienen una aritmética precisa. La decisión central: ¿qué disponibilidad y qué plazo puede prometer un servicio sin incumplir seguido y cuánto cuesta cada incumplimiento?
- 🔗 **Se estudia junto con:** disponibilidad, SLO, presupuesto de error, redundancia.

📘 **Dónde se aprende:** [B124-C21 · Acuerdos de nivel de servicio para productos de datos](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md).

### SLERP

- La doble cobertura significa que `q` y `−q` representan la misma rotación (S1). SLERP es la interpolación esférica entre dos cuaterniones.

💡 **Cómo se explica en la clase [B10-C15](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md):**
- SLERP entre `(1, 0, 0, 0)` (sin giro) y `q_y(100°)` en `t = 0,5` da una rotación de `50,000 000 000°`: gira a velocidad angular constante.
- Convertir entre cuaternión, matriz y eje–ángulo, e interpolar con SLERP.
- 🎯 **Por qué importa:** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.
- 🔗 **Se estudia junto con:** cuaternión, parte escalar, parte vectorial, escalar primero.

📘 **Dónde se aprende:** [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md).

### SLO

- El SLO es el objetivo de nivel de servicio; el SLA, el acuerdo que fija consecuencias si no se cumple.

💡 **Cómo se explica en la clase [B124-C21](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md):**
- Un SLO de 99,5 % en un mes de 720 h tolera `3,60` h de caída; la caída esperada es `13,88` h.
- Prometer un SLO por encima de lo que el diseño sostiene convierte el crédito en un costo recurrente.
- ⚠️ **Error frecuente:** Prometer el SLO de un componente para todo el sistema. Se corrige con 8.1.
- 🎯 **Por qué importa:** B124 trata propuestas de valor, pero un servicio de observación se compromete con plazos y calidad, y esos compromisos tienen una aritmética precisa. La decisión central: ¿qué disponibilidad y qué plazo puede prometer un servicio sin incumplir seguido y cuánto cuesta cada incumplimiento?
- 🔗 **Se estudia junto con:** disponibilidad, SLA, presupuesto de error, redundancia.

📘 **Dónde se aprende:** [B124-C21 · Acuerdos de nivel de servicio para productos de datos](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md).

### SMAC

- El SMAC es la concentración máxima permitida en nave de la NASA para una duración dada.
- SMAC: concentración máxima permitida en nave.

💡 **Cómo se explica en la clase [B106-C24](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md):**
- La página consultada dice qué son los SMAC y quién los fija; no da valores (los oficiales están en JSC 20584 y los de agua, SWEG, en JSC 63414).
- Los límites de la tabla son inventados y no deben usarse como SMAC.
- ⚠️ **Error frecuente:** Tomar los límites del laboratorio como SMAC. Son inventados.
- 🎯 **Por qué importa:** Evaluar el aire exige límites y una regla para combinar contaminantes; ninguno basta por sí solo. La decisión central: ¿cumple una mezcla de contaminantes su límite combinado y qué compuesto la domina?
- 🔗 **Se estudia junto con:** SWEG, Índice de riesgo aditivo, ppm, mg/m³.

📘 **Dónde se aprende:** [B106-C24 · Calidad del aire y límites de exposición en cabina](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md); [B117-C02 · Contención de riesgos biológicos y químicos en cabina](../programa/clases/B117/B117-C02-contencion-de-riesgos-biologicos-y-quimicos-en-cabina/CLASE.md).

### SMPAG

- IAWN es la red internacional de alerta de asteroides, coordinada por NASA, creada por recomendación de un grupo de trabajo de la ONU [S7]. SMPAG es el grupo asesor de planificación de misiones espaciales que implementa una respuesta internacional [S7].

💡 **Cómo se explica en la clase [B58-C18](../programa/clases/B58/B58-C18-marco-internacional-de-defensa-planetaria/CLASE.md):**
- SMPAG implementa la respuesta internacional, con UNOOSA como secretaría permanente.
- Describir qué son IAWN y SMPAG según la fuente consultada.
- 🎯 **Por qué importa:** Un umbral de notificación decide cuántos casos entran en el circuito internacional y cuántos tienen tiempo suficiente. La decisión central: ¿qué umbral activa la alerta y qué margen de tiempo deja para actuar?
- 🔗 **Se estudia junto con:** IAWN, notificación, tiempo de aviso.

📘 **Dónde se aprende:** [B58-C18 · Marco internacional de defensa planetaria](../programa/clases/B58/B58-C18-marco-internacional-de-defensa-planetaria/CLASE.md).

### SNR

- **Significa:** relación señal-ruido (SNR).
- La relación señal-ruido (SNR) es la señal dividida por su incertidumbre típica.
- La SNR es señal sobre ruido total.
- La SNR compara la potencia recibida con el ruido `k T B`.

💡 **Cómo se explica en la clase [B44-C11](../programa/clases/B44/B44-C11-tiempo-de-exposicion/CLASE.md):**
- A esa duración, la SNR total es `147,486` frente a `152,155` de un único cuadro (cociente `0,9693`).
- SNR simulada `24,007` frente a `24,042` analítica.
- 🎯 **Por qué importa:** Exponer poco multiplica el ruido de lectura; exponer mucho arriesga la saturación. La decisión central: ¿cuánto debe durar cada cuadro dentro de un tiempo total dado?
- 🔗 **Se estudia junto con:** cielo, oscuridad, exposición limitada por el cielo, serie de cuadros.

📘 **Dónde se aprende:** [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md); [B44-C11 · Tiempo de exposición](../programa/clases/B44/B44-C11-tiempo-de-exposicion/CLASE.md); [B118-C04 · Detección por radar](../programa/clases/B118/B118-C04-deteccion-por-radar/CLASE.md).

### SOC

- SOC: estado de carga.

💡 **Cómo se explica en la clase [B96-C12](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md):**
- Por simulación: SOC a lo largo del tiempo (esta clase).
- El script [balance_de_energia.py](balance_de_energia.py) simula el SOC de la batería durante 30 órbitas con cuatro planes de operación, calcula la DoD máxima y la contrasta con la fórmula analítica;
- 🎯 **Por qué importa:** Una batería descargada en exceso se degrada y una nave sin energía deja de ser comandable. La decisión central: ¿qué plan de operación mantiene la batería dentro de su criterio de descarga y recupera la carga en cada órbita?
- 🔗 **Se estudia junto con:** DoD, Carga base, Balance neto, Eficiencia de carga.

📘 **Dónde se aprende:** [B96-C12 · Gestión de energía en operaciones](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md).

### SPH

- La onda de rarefacción, la discontinuidad de contacto y el choque son las tres ondas del tubo de Sod. SPH es un método de partículas con kernel de suavizado `W` y longitud `h`.

💡 **Cómo se explica en la clase [B38-C06](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md):**
- El error L1 del SPH se pondera por el volumen de cada partícula y se mide en `|x| < 0,45`.
- El SPH conserva la masa por construcción y la energía a 0,2 %.
- 🎯 **Por qué importa:** Cada método tiene errores distintos en choques y discontinuidades de contacto. La decisión central: ¿qué error comete cada método frente a una solución exacta y cómo cambia con la resolución?
- 🔗 **Se estudia junto con:** problema de Riemann, onda de rarefacción, discontinuidad de contacto, choque.

📘 **Dónde se aprende:** [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md).

### SPI

- El CPI es `EV/AC`; el SPI, `EV/PV`.
- El SPI identifica la SA.

💡 **Cómo se explica en la clase [B89-C25](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md):**
- Con campos ilustrativos (SPI 2, IV 12, etiqueta 16 octetos = `30`), un bloque de `1115` octetos con cabecera de 8 deja `1077` octetos de datos: la eficiencia baja de `0,9928` a `0,9659`.
- SA["asociacion de seguridad: SPI, clave, ventana"] --> TX["emisor: etiqueta = MAC(clave, SPI, ASN, carga)"]
- 🎯 **Por qué importa:** Los comandos son la superficie más sensible de una misión; sin autenticación y sin protección contra repetición, una trama capturada podría reutilizarse, y un CRC solo detecta errores, no ataques (C12). La decisión central: ¿cómo garantizar que una trama es auténtica, íntegra y no repetida, y cuánto cuesta en sobrecarga?
- 🔗 **Se estudia junto con:** protocolo de seguridad de enlace de datos (SDLS), cifrado autenticado AES en modo Galois/Counter (GCM), asociación de seguridad (SA), ventana anti-repetición.

📘 **Dónde se aprende:** [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md); [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### SPK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- En el laboratorio se resuelven 6 archivos; todos existen y LSK y SCLK están antes que los SPK (las dos comprobaciones valen 1 = sí: `1` y `1`).
- Con dos SPK de «NAVE» solapados, en `t = 500 s` los datos vienen de `spk_nave_v2_sint,bsp`.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, CK, PCK, IK.

📘 **Dónde se aprende:** [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### SPMD

- El tamaño es cuántos procesos hay y el rango (*rank*) es el número de cada uno, de 0 a tamaño−1. SPMD (un programa, muchos datos) significa que todos ejecutan el mismo código y se comportan distinto según su rango.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Explicar el modelo SPMD, el rango y el tamaño de un comunicador.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.
- 🔗 **Se estudia junto con:** comunicador, tamaño, rango, punto a punto.

📘 **Dónde se aprende:** [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md).

### SQNR

- La SQNR es el cociente entre la potencia de la señal y la del error de cuantización.

💡 **Cómo se explica en la clase [B57-C03](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md):**
- Para una sinusoide a plena escala, la SQNR teórica es `6,02 N + 1,76 dB`.
- Ejercicio 2 · con una pista. Calcula la SQNR teórica de 10 bits.
- 🎯 **Por qué importa:** Dos sensores con el mismo píxel pueden dar información muy distinta si uno distingue 256 niveles y otro 65.536, o si una banda es ancha y otra estrecha. La decisión central: ¿cuántos bits y qué ancho de banda hacen falta para ver el cambio que me interesa?
- 🔗 **Se estudia junto con:** cuantización, paso de cuantización, banda espectral, respuesta espectral.

📘 **Dónde se aprende:** [B57-C03 · Resolución radiométrica y espectral](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md).

### SQP

- El multiplicador mide la sensibilidad: `dDv*/dT_max = −μ`. SQP (programación cuadrática secuencial) resuelve la secuencia de problemas cuadráticos que salen de aplicar Newton al sistema KKT; con solo igualdades es Newton sobre `[∇f + λ∇g; g] = 0`.

💡 **Cómo se explica en la clase [B11-C23](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md):**
- D --> G["Resolver con SQP/Newton<br/>sobre las condiciones KKT"]
- SQP converge más rápido pero necesita derivadas y un buen punto de partida.
- 🎯 **Por qué importa:** Casi todo problema de diseño de trayectorias tiene límites: tiempo máximo, combustible disponible, distancia mínima a un cuerpo. Un optimizador que ignora las restricciones devuelve un resultado imposible; uno que las trata mal da un resultado que parece factible y no es óptimo.
- 🔗 **Se estudia junto con:** con restricción de igualdad, Lagrangiano, multiplicador de Lagrange, desigualdad.

📘 **Dónde se aprende:** [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md).

### SRR

- La SRR revisa requisitos y concepto de operaciones.

💡 **Cómo se explica en la clase [B83-C13](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md):**
- SRR: requisitos verificables (≥ 95 %), necesidades con requisito (100 %), requisitos con origen (100 %), CONOPS documentado y estabilidad del orden de necesidades (≥ 70 %, no crítico).
- Resultado: SRR 2/5 y PDR 2/7; ninguna lista.
- 🎯 **Por qué importa:** Una revisión aprobada sin criterios es un trámite; una revisión con criterios medibles es una decisión. La decisión central: ¿el proyecto cumple los criterios de entrada de la SRR y de la PDR y qué falta para llegar?
- 🔗 **Se estudia junto con:** PDR, criterio, crítico, RID.

📘 **Dónde se aprende:** [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md).

### SRS

- Choque: excitación transitoria breve. SRS: espectro de respuesta al choque, pico del oscilador según su frecuencia.

💡 **Cómo se explica en la clase [B90-C10](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md):**
- Con `z'' + 2ζω z' + ω² z = −a(t)`, `ζ = 1/(2Q) = 0,05` y aceleración absoluta `a_abs = 2ζω z' + ω² z`, el SRS de frecuencia `fn = ω/2π` es `máx |a_abs|`.
- A 10 Hz: SRS `= 7,45 g`; respuesta analítica del impulso `= 7,45 g` (diferencia 0,01 %); el SRS queda 6,9 % por debajo de la cota sin amortiguamiento `ω ΔV = 8,00 g`.
- ⚠️ **Error frecuente:** Confundir la aceleración pico con la amenaza. Calcula el SRS (8.4)
- 🎯 **Por qué importa:** Dos pulsos con distinta forma pueden dañar lo mismo si sus SRS coinciden, y un pulso con gran aceleración pico puede ser inofensivo para un equipo de baja frecuencia. La decisión central: ¿qué frecuencias de mi equipo están amenazadas por este choque y con qué nivel?
- 🔗 **Se estudia junto con:** Choque, Pulso semisenoidal, Cambio de velocidad ΔV, Q.

📘 **Dónde se aprende:** [B90-C10 · Ensayos de choque](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md).

### SSD

- Información `JᵀJ`: matriz cuyos autovalores miden la certeza por dirección. SSD: suma de diferencias al cuadrado.

💡 **Cómo se explica en la clase [B99-C07](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md):**
- Con cambio de ganancia `g` y sesgo `b` (`I → gI + b`) la ZNCC no cambia, y la SSD sí.
- En el laboratorio (100 parches de `11×11`, ruido de 4 niveles): a contraste 40 y sin cambio ambos aciertan 100 %; con `g = 1,5` y `b = 25` la SSD baja a 80 % y a 4 % con contraste 10, mientras la ZNCC mantiene 100 %.
- 🎯 **Por qué importa:** Un estimador que funciona en el laboratorio puede fallar sin avisar cuando el entorno empeora. La decisión central: ¿qué estimador usar, cómo detectar que el entorno no determina el movimiento y cuándo dejar de confiar en el mapa?
- 🔗 **Se estudia junto con:** Atípico, Huber / IRLS, RANSAC, Degeneración.

📘 **Dónde se aprende:** [B99-C07 · Robustez del mapeo ante entornos degradados](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md).

### STRIDE

- La probabilidad de acierto al azar es `2^−b`. STRIDE son seis categorías de amenaza.

💡 **Cómo se explica en la clase [B88-C17](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md):**
- Escribir un modelo de amenazas STRIDE con mitigaciones.
- Ejercicio 11 · transferencia. Transferencia. ¿Qué amenaza de STRIDE no cubre el HMAC?
- 🎯 **Por qué importa:** Una orden falsa o repetida puede apagar un subsistema o poner la nave en riesgo. La decisión central: ¿qué comprobaciones aseguran que cada comando viene de quien tiene la clave y no es una repetición?
- 🔗 **Se estudia junto con:** etiqueta, ventana, probabilidad de acierto al azar, comando de resincronización.

📘 **Dónde se aprende:** [B88-C17 · Ciberseguridad de aviónica](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md).

### SVD

- La SVD de una matriz real `A` de `m × n` es `A = U Σ Vᵀ`, con `U` (`m × m`, o `m × r` en la versión «económica») y `V` (`n × n`) de columnas ortonormales, y `Σ` diagonal con los valores singulares `σ₁ ≥ σ₂ ≥ … ≥ 0`.
- La solución por SVD usa `B = Σ bᵢ rᵢᵀ = U S Vᵀ` y `A = U diag(1,1,det) Vᵀ`.

💡 **Cómo se explica en la clase [B10-C11](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md):**
- La SVD nunca engaña, pero hay que elegir el umbral.
- Ninguno es dato real; sirven para ver qué dice la SVD.
- 🎯 **Por qué importa:** Un instrumento entrega una imagen de miles de píxeles; la mayor parte de su estructura se puede describir con muy pocos patrones. Una matriz de medidas puede tener columnas casi redundantes, de modo que un cálculo «técnicamente posible» sea inútil.
- 🔗 **Se estudia junto con:** valores singulares, vectores singulares izquierdos, derechos, rango efectivo.

📘 **Dónde se aprende:** [B10-C11 · Valores singulares y SVD](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md); [B74-C14 · Navegación con cámaras estelares](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md).

### SWEG

- SMAC: concentración máxima permitida en nave. SWEG: guía de agua potable.

💡 **Cómo se explica en la clase [B106-C24](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md):**
- La página consultada dice qué son los SMAC y quién los fija; no da valores (los oficiales están en JSC 20584 y los de agua, SWEG, en JSC 63414).
- 🎯 **Por qué importa:** Evaluar el aire exige límites y una regla para combinar contaminantes; ninguno basta por sí solo. La decisión central: ¿cumple una mezcla de contaminantes su límite combinado y qué compuesto la domina?
- 🔗 **Se estudia junto con:** SMAC, Índice de riesgo aditivo, ppm, mg/m³.

📘 **Dónde se aprende:** [B106-C24 · Calidad del aire y límites de exposición en cabina](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md).

### TAG

- El TAG identifica la especie; su signo negativo indica frecuencia medida.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- El laboratorio las lee con ancho fijo y comprueba, para las seis líneas, que `GUP = 2J'+1`, que `TAG = −28001` (negativo: frecuencia medida en laboratorio) y que `DR = 2`.
- Leer los campos de una línea JPL (`FREQ`, `ERR`, `LGINT`, `DR`, `ELO`, `GUP`, `TAG`, `QNFMT`, cuantos).
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.
- 🔗 **Se estudia junto con:** banco de datos espectroscópicos, CDMS, JPL, HITRAN.

📘 **Dónde se aprende:** [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### TAI

- **Significa:** Tiempo Atómico Internacional (TAI).
- El Tiempo Atómico Internacional (TAI) es una cuenta continua de segundos del SI desde un origen (medianoche del 1 de enero de 1958 según S3).

💡 **Contexto en la clase [B13-C08](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md):**
- **Idea central (modelo mental):** TAI es el reloj continuo. UTC es TAI menos un entero de segundos (con saltos). TT es TAI más una constante.
- 🎯 **Por qué importa:** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.
- 🔗 **Se estudia junto con:** Tiempo Universal Coordinado (UTC), Tiempo Terrestre (TT), Tiempo Dinámico Baricéntrico (TDB), segundo intercalar.

📘 **Dónde se aprende:** [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### TAP

- ADQL es el lenguaje de consultas astronómicas del IVOA y TAP el protocolo para enviarlas (S1).

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- Consultar en el servidor (TAP/ADQL) reduce lo transferido pero depende de la disponibilidad y del servicio.
- La Alianza Internacional del Observatorio Virtual (IVOA) define el Table Access Protocol (TAP), un protocolo de servicio para acceder a datos de tablas generales: catálogos astronómicos y tablas de bases de datos, con acceso a los metadatos y a los datos (S1).
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.
- 🔗 **Se estudia junto con:** flujo de datos, adquisición, verificación, caché.

📘 **Dónde se aprende:** [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md).

### TCA

- El TCA es el instante de mínima distancia `ρ_min`; allí `ṙ = 0`.
- El TCA es el instante de mínima distancia.

💡 **Cómo se explica en la clase [B89-C15](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md):**
- Un transpondedor con razón `880/749 = 1,17490` devuelve la portadora ascendente (7,19 GHz, ilustrativa) multiplicada por la razón; el Doppler de ida y vuelta en el TCA es `-0,000 kHz` y en el AOS `376,4 kHz`: más del doble del de ida porque cuenta dos trayectos.
- FD --> TASA["tasa de Doppler en el TCA"]
- 🎯 **Por qué importa:** El Doppler es la medida básica de rastreo: se usa para determinar la órbita y obliga a diseñar los lazos de portadora y los planes de frecuencia. La decisión central: ¿cuánto se desplaza la frecuencia durante una pasada y qué información de la órbita contiene?
- 🔗 **Se estudia junto con:** Doppler de ida, tasa de Doppler, Doppler de ida y vuelta.

📘 **Dónde se aprende:** [B89-C15 · Rastreo y Doppler](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md); [B118-C05 · Conjunciones orbitales](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md).

### TCPI

- El TCPI es el rendimiento de costo que se necesita para terminar en el BAC.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- El TCPI necesario para terminar en el BAC es `1,615`, mucho más que el rendimiento actual.
- Paso 4 · TCPI. `(100 − 30)/(100 − 45) = 1,273`.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, EV, AC.

📘 **Dónde se aprende:** [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### TDB

- **Significa:** Tiempo Dinámico Baricéntrico (TDB).
- El Tiempo Dinámico Baricéntrico (TDB) es la escala uniforme de las efemérides del sistema solar; en SPICE, `ET` significa TDB (S3).

💡 **Contexto en la clase [B13-C08](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md):**
- **Idea central (modelo mental):** TAI es el reloj continuo. UTC es TAI menos un entero de segundos (con saltos). TT es TAI más una constante.
- 🎯 **Por qué importa:** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.
- 🔗 **Se estudia junto con:** Tiempo Universal Coordinado (UTC), Tiempo Atómico Internacional (TAI), Tiempo Terrestre (TT), segundo intercalar.

📘 **Dónde se aprende:** [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### TECU

- Un TECU es `10¹⁶` electrones por metro cuadrado.

💡 **Cómo se explica en la clase [B57-C29](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md):**
- Con 50 TECU el retardo es `0,1093 m` en Ku y `0,6885 m` en C; con 20 TECU, `0,0437` y `0,2754 m`.
- Un altímetro ilustrativo mide a `13,575 GHz` (Ku) y `5,41 GHz` (C) con un ruido de `2 cm` por frecuencia, con un contenido electrónico de `50 TECU` y presiones de `1013,25`, `1000` y `700 hPa`.
- 🎯 **Por qué importa:** Un error de decímetros en la distancia equivale a decímetros de error en la altura del mar, mayor que las señales que se buscan. La decisión central: ¿qué corrección aplicar a cada retardo y cuánto ruido agrega?
- 🔗 **Se estudia junto con:** retardo ionosférico, retardo troposférico seco (hidrostático), combinación libre de ionosfera, barometría inversa.

📘 **Dónde se aprende:** [B57-C29 · Correcciones atmosféricas en altimetría](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md).

### TED

- A2 es el valor de actividad de la tabla de la IAEA SSR-6. TED es la dosis efectiva total.

💡 **Contexto en la clase [B86-C18](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md):**
- 🎯 **Por qué importa:** Los límites de la energía nuclear en el espacio son tanto jurídicos y de seguridad como técnicos: quién aprueba, con qué análisis y con qué umbrales. Un ingeniero de potencia debe saber que estas decisiones existen y qué datos las gobiernan.
- 🔗 **Se estudia junto con:** NSPM-20, niveles I, II y III, A2, LEU.

📘 **Dónde se aprende:** [B86-C18 · Seguridad y licenciamiento energético](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md).

### TF

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?
- 🔗 **Se estudia junto con:** términos, IA, IE, CA.

📘 **Dónde se aprende:** [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### TGA

- **Significa:** termogravimetría (TGA).
- La termogravimetría (TGA) mide la masa de una muestra mientras sube la temperatura.

💡 **Contexto en la clase [B59-C03](../programa/clases/B59/B59-C03-agua-en-regolito-y-minerales/CLASE.md):**
- **Idea central (modelo mental):** Como vaciar tres depósitos cuyos grifos se abren a temperaturas distintas: al subir la temperatura se vacía primero el más fácil. Límite: los reservorios reales se solapan; aquí están separados por construcción.
- 🎯 **Por qué importa:** No toda el agua es igual de fácil de extraer: el hielo sale con poco calor y el hidroxilo exige temperaturas casi de fusión. La decisión central: ¿qué parte del agua total se obtiene calentando solo hasta 300 K?
- 🔗 **Se estudia junto con:** hielo, agua de hidrato, hidroxilo, escalón.

📘 **Dónde se aprende:** [B59-C03 · Agua en regolito y minerales](../programa/clases/B59/B59-C03-agua-en-regolito-y-minerales/CLASE.md).

### TID

- La TID es la dosis ionizante total.

💡 **Cómo se explica en la clase [B88-C03](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué diferencia hay entre SEU y TID?
- TID es acumulativa y degrada el componente.
- ⚠️ **Error frecuente:** Confundir SEU con TID. SEU es instantáneo y TID acumulativo (ejercicio 11)
- 🎯 **Por qué importa:** Un procesador comercial puede fallar en órbita por una sola partícula. La decisión central: ¿cuántos eventos esperar al año y qué margen de dosis hay respecto del fallo del componente?
- 🔗 **Se estudia junto con:** SEU, sección eficaz, LET umbral, Weibull.

📘 **Dónde se aprende:** [B88-C03 · Procesadores tolerantes a radiación](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md); [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### TIR

- La TIR es la `r` con VAN igual a cero.
- La TIR es la tasa que hace el VPN igual a cero.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- La TIR por bisección es `23,8799` %; por Newton, `23,8799` %; el error de `VAN(TIR)` es `8,2e-14`.
- Este flujo cambia de signo una sola vez, así que la TIR es única; con varios cambios de signo puede haber varias.
- ⚠️ **Error frecuente:** Reportar la TIR sin el flujo. Se corrige con 8.1.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?
- 🔗 **Se estudia junto con:** VAN, MOIC, pre-money, post-money.

📘 **Dónde se aprende:** [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md); [B126-C05 · Evaluación de viabilidad económica de un negocio espacial](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md).

### TIS

- La TIS `(4πσ cos θ/λ)²`.

💡 **Cómo se explica en la clase [B43-C23](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md):**
- A igual `σ`, la TIS cambia por `(λ₂/λ₁)² = 4,0` entre 400 y 800 nm.
- *Descripción textual:* una PSD fija la rugosidad en una banda; la TIS la convierte en luz dispersa por la fórmula escalar.
- 🎯 **Por qué importa:** La luz dispersa reduce el contraste y la reflectancia especular. La decisión central: ¿qué rugosidad RMS, en qué banda de frecuencias espaciales, deja la luz dispersa por debajo del presupuesto?
- 🔗 **Se estudia junto con:** rugosidad RMS, PSD, banda, reflectancia especular.

📘 **Dónde se aprende:** [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md).

### TLE

- El TLE son dos líneas de 69 columnas con elementos medios para el modelo SGP4.
- Una TLE (*two-line element set*) es un formato de dos líneas con elementos medios.

💡 **Cómo se explica en la clase [B74-C29](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md):**
- El TLE sintético da `5` (línea 1) y `1` (línea 2).
- EL["elementos"] --> TLE["TLE: 2 lineas de 69 columnas"]
- ⚠️ **Error frecuente:** Leer un TLE como elementos osculadores. Son medios para SGP4; ver 8.4.
- 🎯 **Por qué importa:** Un TLE mal copiado o mal leído da una órbita equivocada sin avisar. La decisión central: ¿qué errores detecta la suma de verificación, qué resolución tiene cada campo y qué significan realmente esos «elementos medios»?
- 🔗 **Se estudia junto con:** checksum, movimiento medio, OMM, teoría de elementos medios.

📘 **Dónde se aprende:** [B74-C29 · Formatos TLE y OMM de elementos orbitales](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md); [B118-C02 · Catálogos de objetos espaciales](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md).

### TLI

- **Significa:** inyección translunar (TLI).
- La inyección translunar (TLI) es el impulso en el perigeo.

💡 **Cómo se explica en la clase [B76-C07](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md):**
- Calcular el `Δv` de inyección translunar con una elipse de Hohmann hasta la distancia lunar.
- 🎯 **Por qué importa:** Un diseño preliminar de misión empieza por el presupuesto de velocidad. La decisión central: ¿cuánto `Δv` cuestan la salida de la Tierra y la captura en la Luna, y cuánto cambia la segunda según la órbita lunar elegida?
- 🔗 **Se estudia junto con:** inserción en órbita lunar (LOI), velocidad de llegada, excentricidad hiperbólica, fracción de propergol.

📘 **Dónde se aprende:** [B76-C07 · Maniobras de inserción cislunar](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md).

### TML

- **Significa:** masa perdida total (TML).
- TML (*total mass loss*) es la pérdida total de masa;
- La masa perdida total (TML) y los volátiles condensables (CVCM) miden la desgasificación de un material.
- Desgasificación: liberación de gases de un material en vacío. TML: pérdida total de masa, `100 (mᵢ − m_f)/mᵢ`.

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- La silicona B pasa en `TML` y falla en `CVCM`: por eso se exigen ambos criterios.
- ⚠️ **Error frecuente:** Usar solo TML. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?
- 🔗 **Se estudia junto con:** WVR, RML, CVCM, bakeout.

📘 **Dónde se aprende:** [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md); [B85-C12 · Entorno de vacío](../programa/clases/B85/B85-C12-entorno-de-vacio/CLASE.md); [B90-C04 · Control de contaminación](../programa/clases/B90/B90-C04-control-de-contaminacion/CLASE.md).

### TOA

- **Significa:** tiempo de llegada (TOA).
- El tiempo de llegada (TOA) es el instante de un pulso.

💡 **Cómo se explica en la clase [B27-C05](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md):**
- En el púlsar binario PSR B1913+16, `9257` tiempos de llegada durante unos `35` años dieron masas de `1,438` y `1,390 M☉` y un decaimiento orbital que coincide con la relatividad general con razón `0,9983 ± 0,0016` (S4, resumen).
- Interpretar una prueba de la radiación gravitacional con tiempos de llegada.
- 🎯 **Por qué importa:** Un púlsar da, a la vez, un reloj de precisión, la medida de su campo magnético y, en una binaria, la masa de las estrellas y una prueba de la relatividad general. La decisión central: dados el periodo y su derivada, ¿qué campo, edad y potencia de frenado tiene el púlsar y qué se aprende de su binaria?
- 🔗 **Se estudia junto con:** púlsar, periodo, dipolo magnético en rotación, campo ecuatorial.

📘 **Dónde se aprende:** [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md).

### TPD

- La TPD (desorción programada por temperatura) calienta con rampa lineal `T = T₀ + βt` y mide la tasa de salida.
- La TPD es la desorción programada por temperatura (B68-C01).

💡 **Cómo se explica en la clase [B68-C01](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md):**
- El máximo de la TPD cumple, con buena aproximación, `E = T_p [ln(ν₁ T_p/β) − 3,46]` (aproximación de Redhead, relación estándar que no se consultó y que el laboratorio verifica).
- Con una TPD sintética de `E = 1040 K` y `ν₁ = 10¹³ s⁻¹` (sintéticos), el pico sale a `32,927 K` y la fórmula devuelve `1039,7 K`: error `0,02 %`.
- 🎯 **Por qué importa:** Un hielo de CO que dura mil millones de años a 15 K desaparece en un segundo a 30 K. Esa sensibilidad exponencial decide dónde está la «línea de nieve» de cada molécula y qué hay en el gas.
- 🔗 **Se estudia junto con:** desorción, energía de enlace, factor preexponencial, orden cero.

📘 **Dónde se aprende:** [B68-C01 · Desorción térmica de hielos interestelares](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md); [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### TRIAD

- El problema de Wahba minimiza `Σ wᵢ |bᵢ − A rᵢ|²` sobre matrices de rotación `A`. TRIAD construye dos ternas ortonormales con dos estrellas.
- El método q halla el autovector de mayor autovalor de la matriz `K` de Davenport. TRIAD construye ternas ortonormales con dos vectores.

💡 **Cómo se explica en la clase [B74-C14](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md):**
- Con dos vectores medidos `b₁, b₂` y sus catálogos `r₁, r₂`, TRIAD toma `b₁` como eje principal y construye la terna con `b₁ × b₂`.
- Con solo dos estrellas, las desviaciones son de `10,1″` (TRIAD) y `12,0″` (SVD), dominadas por pares casi colineales (colas pesadas).
- 🎯 **Por qué importa:** Un error de actitud de unos segundos de arco desplaza a un objeto a un millón de kilómetros por decenas de metros, y un error de giro mayor en el eje óptico es normal. La decisión central: ¿cuántas estrellas y qué campo de visión hacen falta para cada eje de la actitud?
- 🔗 **Se estudia junto con:** problema de Wahba, SVD, giro, campo de visión.

📘 **Dónde se aprende:** [B74-C14 · Navegación con cámaras estelares](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md); [B87-C09 · Estimación de actitud](../programa/clases/B87/B87-C09-estimacion-de-actitud/CLASE.md).

### TRIMP

- El rendimiento es aptitud menos fatiga. TRIMP es una carga basada en frecuencia cardiaca.

💡 **Cómo se explica en la clase [B104-C04](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md):**
- Calcular la fracción de reserva de frecuencia cardiaca (Karvonen) y una carga tipo TRIMP.
- Ejercicio 2 · con una pista. Calcula el TRIMP de 30 min a 110 lpm.
- 🎯 **Por qué importa:** Entrenar más no siempre significa rendir más el día que importa. La decisión central: ¿cómo distribuir una misma carga total para llegar con la mejor combinación de aptitud y fatiga?
- 🔗 **Se estudia junto con:** carga, aptitud, fatiga, rendimiento.

📘 **Dónde se aprende:** [B104-C04 · Acondicionamiento físico general](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md).

### TRL

- El TRL es el nivel de 1 a 9 de madurez.
- Los TRL (S6): 1 principios básicos; 2 concepto; 3 prueba de concepto; 4 componentes probados; 5 maqueta en entorno relevante; 6 prototipo representativo; 7 prototipo en el espacio; 8 calificado para vuelo; 9 probado en misión.

💡 **Cómo se explica en la clase [B78-C19](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md):**
- El TRL es la longitud de la cadena contigua de hitos desde el 1.
- Un sistema formado por A, B y C tiene componentes `[9, 7, 3]` y TRL `min = 3`; la media daría `6,33`.
- ⚠️ **Error frecuente:** Dar el TRL por el máximo con evidencia. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una tecnología con un buen desempeño en papel puede estar lejos de volar. La decisión central: ¿en qué nivel está una tecnología según la evidencia que tiene, y qué nivel tiene un sistema formado por componentes de madureces distintas?
- 🔗 **Se estudia junto con:** hito de evidencia, cadena contigua, eslabón más débil, entorno relevante.

📘 **Dónde se aprende:** [B78-C19 · Madurez tecnológica TRL](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md); [B83-C18 · Niveles de madurez tecnológica](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md).

### TRR

- La TRR revisa la preparación de cada ensayo.

💡 **Cómo se explica en la clase [B83-C14](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md):**
- La TRR de los ensayos requeridos no está lista hasta resolver E3 y E4.
- *Descripción textual:* cada requisito recibe un método; los de ensayo se asocian a un ensayo con su lista de preparación y su veredicto de TRR; si es de vibración, el perfil se integra para dar los niveles de carga.
- ⚠️ **Error frecuente:** Convocar la TRR sin la lista. Verifica las cinco condiciones
- 🎯 **Por qué importa:** Un ensayo mal preparado destruye hardware o no demuestra nada. La decisión central: ¿cada requisito tiene un método asignado, y cada ensayo está listo (procedimiento, equipo, configuración, personal e instalación) y con un nivel de carga definido?
- 🔗 **Se estudia junto con:** matriz de verificación, CDR, vibración aleatoria, Grms.

📘 **Dónde se aprende:** [B83-C14 · Revisiones CDR y TRR](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md).

### TSL

- **Significa:** tiempo sidéreo local (TSL).
- El tiempo sidéreo local (TSL) es el ángulo horario del punto vernal en tu lugar, expresado en horas; en el meridiano, el TSL es igual a la AR del astro que culmina.

💡 **Cómo se explica en la clase [B08-C05](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md):**
- A las 00:00 UT del 5 de noviembre, el tiempo sidéreo local fue `22,25 h` (laboratorio, simulado).
- Calcular el tiempo sidéreo local a una hora UT y usarlo para ubicar el tránsito de un objeto.
- 🎯 **Por qué importa:** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.
- 🔗 **Se estudia junto con:** día solar, día solar medio, día sidéreo, tiempo sidéreo de Greenwich (GMST).

📘 **Dónde se aprende:** [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md).

### TT

- **Significa:** Tiempo Terrestre (TT).
- El Tiempo Terrestre (TT) avanza al mismo ritmo que TAI con un desfase fijo `TT = TAI + 32,184 s` (S2, S3).

💡 **Contexto en la clase [B13-C08](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md):**
- **Idea central (modelo mental):** TAI es el reloj continuo. UTC es TAI menos un entero de segundos (con saltos). TT es TAI más una constante.
- 🎯 **Por qué importa:** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.
- 🔗 **Se estudia junto con:** Tiempo Universal Coordinado (UTC), Tiempo Atómico Internacional (TAI), Tiempo Dinámico Baricéntrico (TDB), segundo intercalar.

📘 **Dónde se aprende:** [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### TVAC

- **Significa:** Vacío térmico (TVAC).
- Vacío térmico (TVAC): ensayo de temperatura en vacío.

💡 **Cómo se explica en la clase [B90-C12](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md):**
- python programa/clases/B90/B90-C12-vacio-termico-y-ciclos/vacio_y_ciclos.py
- 🎯 **Por qué importa:** Una nave en órbita baja sufre unos 16 ciclos térmicos por día; no se pueden repetir 5 840 ciclos en tierra. La decisión central: ¿cuántos ciclos de ensayo con mayor amplitud representan un año de órbita y cuánto tarda la campaña?
- 🔗 **Se estudia junto con:** Bakeout, Ciclado, Presión límite, Factor de aceleración (AF).

📘 **Dónde se aprende:** [B90-C12 · Vacío térmico y ciclos](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md).

### UA

- La UA es la unidad astronómica.

💡 **Cómo se explica en la clase [B89-C04](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md):**
- Pasar de X a Ka a 2,5 UA cuesta `11,617 dB` más de espacio libre (`20 log₁₀(32/8,4)`).
- A la Luna (384 400 km) la pérdida en banda X es de `222,63 dB` y la luz tarda `1,282 s`; a Neptuno (30 UA) la pérdida es de `303,97 dB` y el viaje de ida dura `4,16 h`.
- 🎯 **Por qué importa:** La pérdida de espacio libre domina cualquier presupuesto de enlace de espacio profundo y fija la potencia, la ganancia y el tiempo de ida y vuelta que tendrá una misión. La decisión central: ¿cuántos decibelios se pierden entre transmisor y receptor y cuánto tarda la señal en llegar?
- 🔗 **Se estudia junto con:** pérdida de espacio libre, retardo de luz, atenuación atmosférica, tiempo de ida y vuelta.

📘 **Dónde se aprende:** [B89-C04 · Propagación y pérdidas de espacio libre](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md).

### UFC

- Espora: forma latente resistente. UFC: unidad formadora de colonias.
- UFC: unidad formadora de colonia.

💡 **Cómo se explica en la clase [B106-C28](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md):**
- Si se muestrea cada 24 h la población llega a 3,3 UFC/mL; cada 72 h, 36,6; cada 168 h, 4427, sobre el umbral.
- Con una contaminación de 0,01 UFC/mL (1 UFC por 100 mL) y una recuperación de 0,7, una muestra de 100 mL la detecta con probabilidad 0,503 y una de 1000 mL con 0,9991.
- 🎯 **Por qué importa:** Una muestra pequeña puede no contener ningún organismo de una contaminación real, y un muestreo espaciado deja crecer la población. La decisión central: ¿qué volumen y qué intervalo de muestreo dan una confianza dada de detectar una contaminación antes de que supere el umbral de acción?
- 🔗 **Se estudia junto con:** Recuperación ε, Confianza, Crecimiento logístico, Umbral de acción.

📘 **Dónde se aprende:** [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md); [B106-C28 · Monitoreo microbiológico de agua y superficies del hábitat](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md).

### UHF

- Las bandas VHF (~145 MHz), UHF (~401 MHz), S (~2,2 GHz), X (~8,4 GHz) y Ka (~32 GHz) se tratan aquí con frecuencias centrales ilustrativas.

💡 **Cómo se explica en la clase [B89-C03](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md):**
- La ganancia es `1,4` dBi en VHF, `10,3` en UHF, `25,0` en S, `36,7` en X y `48,3` en Ka; el haz pasa de `144,7°` a `0,66°`.
- De UHF a X, `20 log₁₀(8400/401) = 26,423 dB`; el laboratorio obtiene `26,423 dB`: la misma cifra, porque la ganancia depende de `f²`.
- 🎯 **Por qué importa:** Elegir la banda es la primera decisión de diseño de un enlace y determina el tamaño de la antena y la tasa alcanzable. La decisión central: ¿qué banda usar para una ganancia de antena dada y qué se paga en apuntamiento por usarla?
- 🔗 **Se estudia junto con:** ganancia de apertura, eficiencia de apertura, ancho de haz, VHF.

📘 **Dónde se aprende:** [B89-C03 · Bandas VHF UHF S X Ka](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md).

### UHV

- **Significa:** ultra alto vacío (UHV).
- El ultra alto vacío (UHV) es el régimen de presiones por debajo de `10⁻⁹` mbar, donde el gas residual casi no cubre la superficie durante un experimento.

💡 **Cómo se explica en la clase [B68-C04](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md):**
- Los experimentos de las clases anteriores se hacen en cámaras de ultra alto vacío con una superficie enfriada a 10–18 K.
- python programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/montaje_uhv.py
- 🎯 **Por qué importa:** Un hielo de 10 ML de CO sobre una superficie a 10 K se contamina con agua residual en horas si la presión de fondo no es lo bastante baja, y una TPD con bombeo insuficiente deforma el pico que se mide.
- 🔗 **Se estudia junto con:** flujo de Hertz–Knudsen, probabilidad de adhesión, langmuir, RAIRS.

📘 **Dónde se aprende:** [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### UKF

- El UKF la aplica a la propagación y a la medida.

💡 **Cómo se explica en la clase [B74-C10](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md):**
- En 400 casos el error rms es casi idéntico: `295,61 km` (EKF), `295,53 km` (UKF) y `296,67 km` (Bayes), porque la previa domina.
- La diferencia está en la covarianza: el NEES medio vale `7,359` para el EKF (sobreconfiado, 3,7 veces el esperado), `1,995` para el UKF y `2,070` para la referencia.
- 🎯 **Por qué importa:** Un filtro puede dar una estimación aceptable y una covarianza falsa. La decisión central: ¿cuándo basta el EKF y cuándo la covarianza obliga a usar un filtro no lineal, y cómo lo verifico con una referencia?
- 🔗 **Se estudia junto con:** transformada unscented, puntos sigma, muestreo de importancia, ECM.

📘 **Dónde se aprende:** [B74-C10 · Filtro de Kalman no lineal](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md).

### UNDRIP

- La UNDRIP es la Declaración de la ONU sobre los derechos de los pueblos indígenas.

💡 **Cómo se explica en la clase [B02-C20](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md):**
- S2 cita el artículo 32.2 de la UNDRIP, que pide a los estados obtener consentimiento libre e informado antes de aprobar proyectos que afecten sus tierras o territorios, y propone no tratar a los pueblos indígenas solo como «partes interesadas» o «compromiso cultural».
- Hecho: que la astronomía canadiense usa Maunakea y que hay tensiones por el TMT; propuesta: que la sociedad adopte una posición guiada por UNDRIP y use las directrices como modelo.
- 🎯 **Por qué importa:** Los sitios, instrumentos, archivos, saberes y hasta la oscuridad del cielo son patrimonio, y los telescopios, el turismo y las constelaciones de satélites pueden dañarlo. La pregunta motivadora es: ¿qué debo preguntar, a quién y antes de qué, cuando mi trabajo toca un cielo o un lugar que importa a otras personas?
- 🔗 **Se estudia junto con:** patrimonio astronómico, conocimiento tradicional, consentimiento libre, previo e informado, contaminación lumínica.

📘 **Dónde se aprende:** [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md).

### UNOOSA

- COPUOS es la Comisión sobre la Utilización del Espacio Ultraterrestre con Fines Pacíficos. UNOOSA es la Oficina de Asuntos del Espacio Ultraterrestre, su secretaría.

💡 **Cómo se explica en la clase [B119-C06](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md):**
- 18 miembros en 1958, permanente en 1959, dos subcomités y secretaría UNOOSA.
- Según el resumen de búsqueda de las páginas de UNOOSA (2026-11-11), la Asamblea General creó COPUOS como órgano ad hoc con 18 miembros por la res. 1348 (XIII) del 13-12-1958 y lo hizo permanente por la res. 1472 (XIV) del 12-12-1959; tiene un Subcomité Científico y Técnico y un Subcomité Jurídico, y UNOOSA es su secretaría.
- ⚠️ **Error frecuente:** Atribuir la decisión a UNOOSA y no a COPUOS. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** Quien estudia el derecho espacial necesita saber dónde se negocia y cómo se decide; ninguna clase anterior trata los organismos. La decisión central: ¿cómo cambia la probabilidad de bloqueo cuando crece el número de miembros que deben consentir?
- 🔗 **Se estudia junto con:** COPUOS, consenso, Bloqueo.

📘 **Dónde se aprende:** [B119-C06 · Organismos UNOOSA y COPUOS](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md).

### UT1

- El ángulo de rotación terrestre (ERA) es el ángulo entre un origen celeste de referencia y un origen terrestre, que describe la rotación de la Tierra en torno a su eje; la convención IERS lo define como una función lineal de `UT1` (S1, ec. 5.14). UT1 es la escala de tiempo ligada a la rotación de la Tierra;

💡 **Cómo se explica en la clase [B13-C10](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md):**
- Según las Convenciones IERS 2010 (S1, ec. 5.14), `ERA(Tu) = 2π (0,779 057 273 264 0 + 1,002 737 811 911 354 48 Tu)` radianes, con `Tu = JD(UT1) − 2 451 545,0`.
- Las dos constantes (`0,7790572732640` vueltas en J2000.0 y `1,00273781191135448` vueltas por día de UT1) son definiciones (S1, Tabla 1.1).
- ⚠️ **Error frecuente:** Usar UTC como UT1 sin cuantificar el error. Se corrige con los ejercicios 8 y 11.
- 🎯 **Por qué importa:** Un telescopio en el desierto debe saber cuándo un objeto pasa por su meridiano, que es cuando está más alto y se observa mejor. Esa hora no es la del reloj civil: el cielo se adelanta casi cuatro minutos cada día.
- 🔗 **Se estudia junto con:** ángulo de rotación terrestre (ERA), día sidéreo, longitud este, ángulo horario.

📘 **Dónde se aprende:** [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md).

### UTC

- **Significa:** Tiempo Universal Coordinado (UTC).
- El Tiempo Universal Coordinado (UTC) es una forma de nombrar instantes con fecha y hora civil que sigue a TAI con saltos de un segundo para mantenerse a menos de `0,9 s` de UT1 (S3); no es una escala continua.
- Muestra de auditoría: entradas revisadas. UTC: tiempo universal coordinado.

💡 **Cómo se explica en la clase [B96-C30](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué las marcas de tiempo deben ser UTC y no decrecientes?
- Datos SINTETICOS: operadores, acciones y marcas de tiempo ficticios (UTC fijo); semilla 96
- 🎯 **Por qué importa:** Sin registro verificable no se puede reconstruir un incidente ni demostrar quién aprobó un comando. La decisión central: ¿cómo se registra para que una alteración se detecte y cuánto hay que revisar en una auditoría?
- 🔗 **Se estudia junto con:** Bitácora, Cadena de hashes, Anexado solo, Hash anclado.

📘 **Dónde se aprende:** [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md); [B96-C30 · Registro y auditoría de operaciones](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md).

### VAC

- El EAC es la estimación del costo final; el ETC, lo que falta gastar; el VAC, `BAC − EAC`.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- Si el rendimiento de costo se mantiene, `EAC = BAC/CPI = 100,63` Mum (ETC `40,63`, VAC `-20,63`), idéntico a `AC + (BAC − EV)/CPI` (error `0,0e+00`).
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, EV, AC.

📘 **Dónde se aprende:** [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### VAN

- El VAN es `Σ F_t/(1 + r)^t`.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- Con flujos `(−100, −40, 30, 70, 90, 110)` Mum, el VAN al 12 % es `57,6397` Mum.
- La TIR por bisección es `23,8799` %; por Newton, `23,8799` %; el error de `VAN(TIR)` es `8,2e-14`.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?
- 🔗 **Se estudia junto con:** TIR, MOIC, pre-money, post-money.

📘 **Dónde se aprende:** [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md).

### VCID

- El SCID identifica la nave; el VCID, el canal virtual.

💡 **Cómo se explica en la clase [B94-C03](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md):**
- Paso 2 · Primeros 16 bits. `0x2A53 = 0010 1010 0101 0011`: versión `00`, SCID `10 1010 0101 = 0x2A5`, VCID `001`, OCF `1`.
- Ejercicio 5 · autónomo. Calcula `0x2A5 << 4` y súmale VCID = 3 desplazado 1 bit y OCF = 0.
- 🎯 **Por qué importa:** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?
- 🔗 **Se estudia junto con:** trama de transferencia de telemetría, SCID, contador de canal maestro, canal virtual.

📘 **Dónde se aprende:** [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### VDOP

- HDOP y VDOP separan lo horizontal de lo vertical.

💡 **Cómo se explica en la clase [B57-C10](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md):**
- Calcular HDOP, VDOP, PDOP y TDOP desde la matriz de geometría.
- Ejercicio 6. ¿Qué mide el VDOP frente al HDOP?
- 🎯 **Por qué importa:** La geodesia con GNSS mide posiciones de estaciones con precisión de milímetros a centímetros y sirve para ver cómo se mueve la corteza. Pero la precisión depende de la geometría de los satélites.
- 🔗 **Se estudia junto con:** pseudodistancia, matriz de geometría, DOP, HDOP.

📘 **Dónde se aprende:** [B57-C10 · Geodesia mediante GNSS](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md).

### VHF

- Las bandas VHF (~145 MHz), UHF (~401 MHz), S (~2,2 GHz), X (~8,4 GHz) y Ka (~32 GHz) se tratan aquí con frecuencias centrales ilustrativas.

💡 **Cómo se explica en la clase [B89-C03](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md):**
- La ganancia es `1,4` dBi en VHF, `10,3` en UHF, `25,0` en S, `36,7` en X y `48,3` en Ka; el haz pasa de `144,7°` a `0,66°`.
- Ejercicio 3 · casi autónomo. ¿Por qué una antena de 1 m en VHF tiene un haz tan ancho?
- 🎯 **Por qué importa:** Elegir la banda es la primera decisión de diseño de un enlace y determina el tamaño de la antena y la tasa alcanzable. La decisión central: ¿qué banda usar para una ganancia de antena dada y qué se paga en apuntamiento por usarla?
- 🔗 **Se estudia junto con:** ganancia de apertura, eficiencia de apertura, ancho de haz, UHF.

📘 **Dónde se aprende:** [B89-C03 · Bandas VHF UHF S X Ka](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md).

### VPN

- **Significa:** negativo (VPN).
- El valor predictivo positivo (VPP) es la fracción de positivos que son verdaderos; el negativo (VPN), la de negativos que son verdaderos.
- El VPN es la suma de los flujos descontados.
- La sensibilidad, la especificidad, el VPP y el VPN miden un umbral.

💡 **Cómo se explica en la clase [B105-C24](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md):**
- Calcular sensibilidad, especificidad, VPP y VPN de un umbral con una prevalencia dada.
- umbral sensibilidad especificidad VPP (prevalencia 2 %) VPN
- 🎯 **Por qué importa:** Con tripulaciones pequeñas, el intervalo de la población general es poco sensible a los cambios personales, y un umbral con baja prevalencia da más falsas alarmas que aciertos. La decisión central: ¿cuándo un cambio de un indicador es real y qué umbral equilibra sensibilidad y valor predictivo?
- 🔗 **Se estudia junto con:** intervalo de referencia, índice de individualidad, RCV, sensibilidad.

📘 **Dónde se aprende:** [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md); [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md); [B126-C05 · Evaluación de viabilidad económica de un negocio espacial](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md).

### VPP

- **Significa:** valor predictivo positivo (VPP).
- El valor predictivo positivo (VPP) es la fracción de positivos que son verdaderos; el negativo (VPN), la de negativos que son verdaderos.
- La sensibilidad, la especificidad, el VPP y el VPN miden un umbral.

💡 **Cómo se explica en la clase [B105-C24](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md):**
- Subir el umbral sube la especificidad y el VPP y baja la sensibilidad.
- T["umbral"] --> S["sensibilidad, especificidad,<br/>VPP segun prevalencia"]
- ⚠️ **Error frecuente:** Ignorar la prevalencia al evaluar un umbral. El VPP depende de ella (8.3).
- 🎯 **Por qué importa:** Con tripulaciones pequeñas, el intervalo de la población general es poco sensible a los cambios personales, y un umbral con baja prevalencia da más falsas alarmas que aciertos. La decisión central: ¿cuándo un cambio de un indicador es real y qué umbral equilibra sensibilidad y valor predictivo?
- 🔗 **Se estudia junto con:** intervalo de referencia, índice de individualidad, RCV, sensibilidad.

📘 **Dónde se aprende:** [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md); [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### WAIC

- LOO: `elpd_loo = Σ_i log p(y_i | y_{−i})`. WAIC: `elpd_waic = lppd − p_waic`, con `lppd = Σ_i log E_post[p(y_i | θ)]` y `p_waic = Σ_i Var_post[log p(y_i | θ)]`, la penalización por complejidad efectiva.

💡 **Cómo se explica en la clase [B19-C07](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md):**
- LOO/WAIC responden «¿qué modelo predecirá mejor datos nuevos?»; son menos sensibles al prior y adecuadas para elegir con fines predictivos (S2).
- LOO y WAIC miran hacia adelante: «con lo aprendido de estos datos, ¿cómo predice un dato nuevo?».
- 🎯 **Por qué importa:** Miras 10 mediciones de la amplitud de una señal y el promedio es 0,57 con ruido conocido 1. ¿Hay señal (`μ ≠ 0`) o solo ruido (`μ = 0`)?
- 🔗 **Se estudia junto con:** evidencia, factor de Bayes, odds posteriores, factor de Occam.

📘 **Dónde se aprende:** [B19-C07 · Comparación de modelos bayesianos](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md).

### WCET

- El WCET es la cota superior.

💡 **Cómo se explica en la clase [B88-C30](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md):**
- Analogía: el WCET es como el tiempo del viaje más lento posible con todos los semáforos en rojo: puede no ocurrir nunca, pero el horario se arma con él.
- Calcular el WCET como camino más largo con cotas de bucle.
- ⚠️ **Error frecuente:** Medir y llamar WCET al máximo. Una cota se calcula (8.1)
- 🎯 **Por qué importa:** El análisis de planificación (C05) necesita `C` de cada tarea, y medir no basta porque el peor camino puede no ejercitarse. La decisión central: ¿cuál es una cota segura del tiempo de ejecución y cuánto pesimismo trae?
- 🔗 **Se estudia junto con:** BCET, camino más largo, pesimismo, fallo de caché.

📘 **Dónde se aprende:** [B88-C30 · Análisis de peor caso de tiempo de ejecución (WCET)](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md).

### WCS

- Una WCS (*World Coordinate System*) asocia píxeles con coordenadas del cielo mediante palabras clave como `CRPIX`, `CRVAL`, `CDELT` y `CTYPE`.

💡 **Cómo se explica en la clase [B14-C06](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md):**
- Para el campo pequeño del ejemplo, la WCS es: `CRPIX = (33, 25)` (píxel de referencia, numerado desde 1), `CRVAL = (150°, 2°)` (coordenadas del cielo de ese píxel), `CDELT = (−1″, +1″)` expresadas en grados, `CTYPE = RA---TAN, DEC--TAN`.
- (No consulté el estándar de WCS: lo uso como convención y verifico su resultado, ver sección 11.)
- 🎯 **Por qué importa:** Una imagen astronómica es una matriz de números, pero esos números no significan nada sin su encabezado: ¿qué unidad tienen?, ¿cuánto duró la exposición?, ¿a qué punto del cielo apunta el píxel central? Si el encabezado miente o se pierde, la imagen no sirve.
- 🔗 **Se estudia junto con:** HDU, HDU primario, encabezado, tarjetas.

📘 **Dónde se aprende:** [B14-C06 · Formato FITS y encabezados](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md).

### WEH

- **Significa:** abundancia equivalente en agua (WEH).
- La abundancia equivalente en agua (WEH) es la masa de agua que daría la misma señal por cada 100 de regolito.

💡 **Contexto en la clase [B67-C07](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md):**
- **Idea central (modelo mental):** Contar neutrones es como estimar cuánta gente hay en una sala por el ruido: más personas, más ruido; y el ruido tiene su propia variabilidad. Separar especies en un espectro es distinguir voces que se solapan.
- 🎯 **Por qué importa:** Un sensor no mide «agua»: mide cuentas, y de ellas se infiere la abundancia con un modelo. La decisión central: ¿cuánto tiempo de medición y qué canales hacen falta para detectar y separar un volátil con la incertidumbre requerida?
- 🔗 **Se estudia junto con:** tasa de neutrones epitérmicos, conteo de Poisson, espectrometría de masas, patrón de fragmentación.

📘 **Dónde se aprende:** [B67-C07 · Sensores para volátiles: espectrometría de neutrones y de masas](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md).

### WER

- El WER es `(S + D + I)/N`: sustituciones, borrados e inserciones sobre las palabras de referencia.

💡 **Cómo se explica en la clase [B128-C05](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md):**
- Con referencia de 12 palabras y una hipótesis sin «no»: `D = 1`, `WER = 1/12 = 8,3 %`.
- Un WER pequeño puede ocultar un error que invierte el sentido.
- 🎯 **Por qué importa:** Un subtítulo mal sincronizado o demasiado rápido no se alcanza a leer, y una transcripción automática sin revisar puede decir lo contrario de lo dicho. La decisión central: ¿cómo compruebo que los subtítulos se pueden leer y que no cambian el sentido?
- 🔗 **Se estudia junto con:** subtítulos, transcripción, audiodescripción, WebVTT.

📘 **Dónde se aprende:** [B128-C05 · Subtítulos y transcripciones](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md).

### WRT

- El RTO es el tiempo objetivo para restablecer el servicio; el WRT es el tiempo adicional para recuperar el trabajo; el MTD es el tiempo máximo tolerable de interrupción.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- *Descripción textual:* desde el fallo corren el RTO y el WRT, cuya suma no debe pasar del MTD, mientras el costo crece; el RPO limita el intervalo entre copias.
- Analogía: un grifo roto que inunda más cada minuto: arreglarlo (RTO) y secar (WRT) debe caber antes del daño inaceptable (MTD).
- ⚠️ **Error frecuente:** Olvidar el WRT. Se corrige con 8.2.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?
- 🔗 **Se estudia junto con:** disponibilidad, MTBF, MTTR, RTO.

📘 **Dónde se aprende:** [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### WVR

- TML (*total mass loss*) es la pérdida total de masa; WVR, el vapor de agua recuperado;

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- A["pesadas mi, mf, mh, dc"] --> B["TML, WVR, RML, CVCM"]
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?
- 🔗 **Se estudia junto con:** TML, RML, CVCM, bakeout.

📘 **Dónde se aprende:** [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md).

### XF

- El correlador XF correlaciona en el tiempo y luego transforma; el FX transforma y luego multiplica.

💡 **Cómo se explica en la clase [B46-C15](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md):**
- La diferencia máxima relativa entre el espectro cruzado FX y la FFT de la correlación XF es `5,6 × 10^-16` (error de redondeo).
- FX y XF difieren `5,6 × 10^-16` y el retardo de 5 muestras se recupera.
- ⚠️ **Error frecuente:** Creer que FX y XF difieren. Se corrige con 8.2.
- 🎯 **Por qué importa:** La visibilidad es el dato básico de la imagen, y su ruido determina la sensibilidad. La decisión central: ¿cuántas muestras hay que correlacionar para fijar amplitud y fase con la precisión requerida?
- 🔗 **Se estudia junto con:** visibilidad, ruido de correlación, FX, lag.

📘 **Dónde se aprende:** [B46-C15 · Correladores y visibilidades](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md).

### YAML

- JSON es un formato de texto para intercambiar datos entre lenguajes; sus valores son objeto, arreglo, número, texto, `true`, `false` y `null` (S2, S3). YAML es un formato legible por personas para serializar datos con tres estructuras: mapeos (clave-valor), secuencias (listas) y escalares (valores simples); la estructura se marca con sangría y no admite tabulaciones en ella (S4).

💡 **Cómo se explica en la clase [B07-C16](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md):**
- Nunca uses tabulaciones para sangrar: YAML no las admite (S4);
- La versión 1.2 de YAML es un superconjunto de JSON (todo JSON válido es YAML válido), según la especificación (S4).
- ⚠️ **Error frecuente:** Usar `yaml.load` con datos ajenos. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Una simulación tiene decenas de parámetros. Si están enterrados en el código, cambiar uno obliga a editar el programa y es fácil olvidar con qué valores se obtuvo cada resultado.
- 🔗 **Se estudia junto con:** JSON, sangría, comentario, Serializar.

📘 **Dónde se aprende:** [B07-C16 · Formatos JSON y YAML](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md).

### YORP

- El efecto Yarkovsky es el empuje por la reemisión térmica anisótropa de un cuerpo que rota. YORP es el torque análogo que cambia la rotación.

💡 **Cómo se explica en la clase [B58-C14](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md):**
- La evidencia es la ficha de Yarkovsky y YORP del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de Yarkovsky y YORP*: comparación integrada–fórmula, tabla física y barrera.
- 🎯 **Por qué importa:** Una deriva de decenas de kilómetros en un siglo puede decidir si un acercamiento ocurre. La decisión central: ¿cuánto se desplaza un asteroide por empuje térmico y por qué los cuerpos pequeños son más sensibles?
- 🔗 **Se estudia junto con:** efecto Yarkovsky, ecuación de Gauss, barrera de rotación.

📘 **Dónde se aprende:** [B58-C14 · Efectos Yarkovsky y YORP](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md).

### ZHR

- La ZHR (*zenithal hourly rate*) es el número de meteoros de la lluvia por hora que vería un observador con magnitud límite 6,5 y el radiante en el cenit (S3).
- La ZHR es la tasa horaria cenital: recuentos por hora bajo cielo ideal (`lm = 6,5`) y con el radiante en el cenit.

💡 **Cómo se explica en la clase [B08-C18](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md):**
- La página consultada no da radiantes ni ZHR, y tiene una incoherencia interna en el período de las Alfa Capricórnidas, por lo que su detalle no se reproduce aquí.
- De la definición de ZHR (S3) se deduce, bajo supuestos declarados, que `ZHR = N · r^(6,5 − lm) / (T · sen h · (1 − c))`, donde `N` es el número de meteoros de la lluvia en `T` horas, `lm` la magnitud límite, `r` el índice de población (aquí 2,5, valor de ejemplo), `h` la altura del radiante y `c` la fracción de cielo cubierta por nubes.
- 🎯 **Por qué importa:** Cada año, titulares prometen «cientos de estrellas fugaces por hora». Con un cielo contaminado o con el radiante bajo el horizonte, verás muy pocas.
- 🔗 **Se estudia junto con:** meteoroide, meteoro, meteorito, lluvia de meteoros.

📘 **Dónde se aprende:** [B08-C18 · Introducción a meteoros y lluvias](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md); [B129-C03 · Seguimiento ciudadano de meteoros](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md).

### ZNCC

- SSD: suma de diferencias al cuadrado. ZNCC: correlación normalizada de media cero.

💡 **Cómo se explica en la clase [B99-C07](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md):**
- Con cambio de ganancia `g` y sesgo `b` (`I → gI + b`) la ZNCC no cambia, y la SSD sí.
- En el laboratorio (100 parches de `11×11`, ruido de 4 niveles): a contraste 40 y sin cambio ambos aciertan 100 %; con `g = 1,5` y `b = 25` la SSD baja a 80 % y a 4 % con contraste 10, mientras la ZNCC mantiene 100 %.
- ⚠️ **Error frecuente:** Confiar en ZNCC cuando el contraste es menor que el ruido. A contraste 1 el acierto cae a 55 % (8.4).
- 🎯 **Por qué importa:** Un estimador que funciona en el laboratorio puede fallar sin avisar cuando el entorno empeora. La decisión central: ¿qué estimador usar, cómo detectar que el entorno no determina el movimiento y cuándo dejar de confiar en el mapa?
- 🔗 **Se estudia junto con:** Atípico, Huber / IRLS, RANSAC, Degeneración.

📘 **Dónde se aprende:** [B99-C07 · Robustez del mapeo ante entornos degradados](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md).
