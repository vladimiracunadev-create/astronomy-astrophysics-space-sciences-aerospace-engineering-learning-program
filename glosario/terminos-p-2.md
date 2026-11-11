# Términos · P (parte 2 de 4)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · **P** · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-p.md) · **2** · [3](terminos-p-3.md) · [4](terminos-p-4.md)

### Pico

- El pico `x_p = −b/(2c)`.

💡 **Cómo se explica en la clase [B27-C20](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md):**
- *Descripción textual:* cada joroba se ajusta con una parábola y su pico se calcula con una fórmula; la banda 2 es una copia retrasada de la banda 1 y el retardo se recupera maximizando la correlación.
- Aquí no se usa ninguna cifra de esos resultados: la SED es sintética, con picos verdaderos en `log ν = 15` y `22` y ruido de `0,03` dex, y las curvas de luz tienen un retardo verdadero de `7` muestras.
- ⚠️ **Error frecuente:** Confundir el pico en `νF_ν` y en `F_ν`. Se corrige con la sección 6.
- 🎯 **Por qué importa:** El caso de GW170817 con GRB 170817A mostró el valor de combinar mensajeros y bandas. La decisión central: ¿dónde están los picos de las dos jorobas y qué retardo hay entre dos bandas?
- 🔗 **Se estudia junto con:** SED, log-parábola, correlación cruzada, retardo.

📘 **Dónde se aprende** (1 clase): [B27-C20 · Análisis multibanda de un evento extremo](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md).

### Pico 3σ

- El pico 3σ es `3 g_rms`.

💡 **Cómo se explica en la clase [B84-C32](../programa/clases/B84/B84-C32-vibracion-aleatoria-y-densidad-espectral-de-potencia/CLASE.md):**
- La señal gaussiana justifica `3σ` como pico estadístico, pero los 4,69σ muestran que en 32 768 muestras aparecen picos mayores; el diseño usa `3σ` por convención (GEVS), no como cota.
- *Descripción textual:* la ASD genera la señal; de la señal se miden rms, curtosis y picos y se estima de nuevo la ASD para compararla con la original.
- ⚠️ **Error frecuente:** Confundir rms con pico. Se corrige con el ejemplo 13.
- 🎯 **Por qué importa:** Un ensayo se controla con una ASD pero el daño lo producen los picos de la señal: saber que la señal es gaussiana (curtosis 3, 0,27 % fuera de 3σ) justifica usar `3σ` como pico de diseño. La decisión central: ¿qué valor eficaz, qué picos y qué incertidumbre espectral tiene una vibración aleatoria definida por una ASD?
- 🔗 **Se estudia junto con:** síntesis espectral, periodograma de Welch, curtosis.

📘 **Dónde se aprende** (1 clase): [B84-C32 · Vibración aleatoria y densidad espectral de potencia](../programa/clases/B84/B84-C32-vibracion-aleatoria-y-densidad-espectral-de-potencia/CLASE.md).

### Pico al cargar un capacitor de entrada

- Corriente de arranque (*inrush*): pico al cargar un capacitor de entrada. Limitador: resistencia o circuito que reduce ese pico.

💡 **Contexto en la clase [B90-C07](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR B["Bateria<br/>Vs = 8.4 V<br/>R interna"] --> H["Arnes<br/>R = 84 mohm"] H --> L["Cargas<br/>P = 12 W<br/>V carga"] L --> H H --> B ``` *Descripción textual:* la batería entrega corriente por el arnés a las cargas y esta vuelve por el retorno; la tensión en la carga es la de la batería menos la caída en las resistencias.
- 🎯 **Por qué importa:** Una carga de potencia constante pide más corriente cuando baja la tensión, de modo que un arnés largo o delgado puede hundir el bus justo cuando más se necesita. Y al conectar una carga con capacitor, la corriente inicial puede ser decenas de amperios.
- 🔗 **Se estudia junto con:** Bus de potencia, Arnés, Carga de potencia constante, Caída de tensión.

📘 **Dónde se aprende** (1 clase): [B90-C07 · Integración eléctrica de buses](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md).

### Pico central

- Un pico central es una elevación en el centro; las terrazas son escalones de la pared.

💡 **Cómo se explica en la clase [B61-C03](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md):**
- El pico central y la fluidización quedan fuera del modelo.
- Describir la morfología simple y la compleja (terrazas, fondo plano, pico central).
- ⚠️ **Error frecuente:** Creer que la relajación explica el pico central. Se corrige con 8.3.
- 🎯 **Por qué importa:** Sin la transición simple–compleja no se puede interpretar la forma de un cráter grande ni comparar cuerpos. La decisión central: ¿a qué diámetro cambia la morfología y cómo depende de la gravedad?
- 🔗 **Se estudia junto con:** transición simple–compleja, terrazas, resistencia efectiva, ángulo crítico.

📘 **Dónde se aprende** (1 clase): [B61-C03 · Cráteres complejos: colapso, picos centrales y terrazas](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md).

### Pico de Bragg

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C09](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md):**
- **Idea central (modelo mental):** Una partícula que atraviesa materia es como un coche en barro: frena más cuanto más lento va, y al final se detiene de golpe, depositando casi toda su energía.
- 🎯 **Por qué importa:** Medir ΔE y E permite identificar la partícula. La decisión central: ¿qué espesor de detector y qué energía separan protones de partículas alfa?
- 🔗 **Se estudia junto con:** poder de frenado, fórmula de Bethe-Bloch, alcance CSDA, telescopio ΔE–E.

📘 **Dónde se aprende** (2 clases): [B47-C09 · Detectores de partículas — Instrumentación y observatorios espaciales](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md); [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md).

### Pico de Gamow

- El pico de Gamow `E₀` es la energía a la que ocurre la mayoría de las reacciones: compromiso entre pocas partículas muy energéticas y muchas poco energéticas.
- El pico de Gamow `E₀ = (E_G(kT)²/4)^(1/3)`.

💡 **Cómo se explica en la clase [B24-C07](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md):**
- A["Distribución de energías<br/>exp(−E/kT)"] --> C["Producto = pico<br/>de Gamow E₀"]
- *Descripción textual:* la tasa de reacción es el producto de la distribución térmica de energías, que cae con `E`, y de la probabilidad de túnel, que crece con `E`; el máximo es el pico de Gamow y su anchura fija cómo crece la tasa con la temperatura.
- 🎯 **Por qué importa:** Dos protones se repelen con una fuerza eléctrica enorme; a las temperaturas de una estrella casi ninguno tiene energía para acercarse lo suficiente. Aun así la fusión ocurre, por efecto túnel.
- 🔗 **Se estudia junto con:** cadena protón–protón (p–p), ciclo CNO, barrera de Coulomb, efecto túnel.

📘 **Dónde se aprende** (2 clases): [B24-C07 · Ciclo CNO y cadena protón-protón](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md); [B31-C07 · Estructura nuclear](../programa/clases/B31/B31-C07-estructura-nuclear/CLASE.md).

### Pico relativo

- El pico relativo (Strehl por jitter).

💡 **Cómo se explica en la clase [B47-C10](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md):**
- Paso 1 · Condición. pico relativo `= (FWHM_D/FWHM_tot)² = 0,9`.
- Ejercicio 5. Pico relativo con `σ = 0,020`.
- 🎯 **Por qué importa:** Una buena óptica con mal apuntamiento da imágenes borrosas. La decisión central: ¿qué RMS de *jitter* se puede tolerar para perder menos del 10 % del pico?
- 🔗 **Se estudia junto con:** jitter, deriva, densidad espectral de potencia, RMS.

📘 **Dónde se aprende** (1 clase): [B47-C10 · Estabilidad de apuntamiento](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md).

### PID

- La ley PID es `u(t) = Kp e(t) + Ki ∫₀ᵗ e(τ) dτ + Kd ė(t)`, con `e = r − y` el error;

💡 **Cómo se explica en la clase [B16-C11](../programa/clases/B16/B16-C11-control-proporcional-integral-derivativo/CLASE.md):**
- Paso 2 · PID. Se agrega `Ki = 2` y la integral `ξ`.
- Paso 4 · simulación. A los 600 s, `θ = 25,000000 mrad` con PD y `−0,000000 mrad` con PID (error < 10⁻⁶ rad);
- 🎯 **Por qué importa:** En el espacio actúan pares pequeños pero persistentes: presión de radiación solar, gradiente de gravedad, fugas de un propulsor. Un lazo PD termina con un error constante `d/Kp` (C04).
- 🔗 **Se estudia junto con:** derivada sobre la medida, tipo, tiempo integral, derivativo.

📘 **Dónde se aprende** (1 clase): [B16-C11 · Control proporcional integral derivativo](../programa/clases/B16/B16-C11-control-proporcional-integral-derivativo/CLASE.md).

### Pie

- El pie es el texto que acompaña a una figura o tabla.

💡 **Cómo se explica en la clase [B20-C04](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md):**
- Cada figura o tabla se entiende sola con su pie: qué muestra, qué son los ejes, con unidades, cuántos datos, de qué origen (observado, simulado, etc.).
- Descripción larga alternativa: el pie de la figura debe poder leerse sin ver la imagen.
- ⚠️ **Error frecuente:** Figuras que dependen del color o sin pie. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Un resultado correcto mal comunicado se pierde: nadie sabe qué se midió, con qué incertidumbre ni qué supuestos hay detrás, y no puede reproducirse ni usarse.
- 🔗 **Se estudia junto con:** artículo de investigación original, IMRaD, resumen, afirmación.

📘 **Dónde se aprende** (1 clase): [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### PIL

- SIL: software en el computador de desarrollo. PIL: en el procesador objetivo o en un modelo de su aritmética.

💡 **Cómo se explica en la clase [B88-C41](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md):**
- PIL, de aritmética y de tamaño de datos;
- Por ejecución en el procesador (PIL real): exige hardware.
- ⚠️ **Error frecuente:** Creer que SIL basta. Hace falta PIL y HIL (8.4)
- 🎯 **Por qué importa:** La aritmética del procesador objetivo puede ser distinta de la del escritorio. La decisión central: ¿cuánto se aparta la respuesta con la precisión del objetivo y cumple la tolerancia?
- 🔗 **Se estudia junto con:** SIL, HIL, épsilon, LSB.

📘 **Dónde se aprende** (1 clase): [B88-C41 · Pruebas SIL y PIL del software de vuelo](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md).

### Pila

- La pila son varios cuadros del mismo campo.

💡 **Cómo se explica en la clase [B44-C16](../programa/clases/B44/B44-C16-ruido-cosmico-e-identificacion/CLASE.md):**
- *Descripción textual:* la mediana de la pila da el valor esperado por píxel; los residuos grandes se marcan como impactos.
- Simular impactos independientes en una pila.
- 🎯 **Por qué importa:** Un impacto fuerte parece una estrella o un defecto. La decisión central: ¿cuántos cuadros hacen falta para identificar los impactos y cuándo falla la mediana?
- 🔗 **Se estudia junto con:** rayo cósmico, mediana de la pila, coincidencia.

📘 **Dónde se aprende** (1 clase): [B44-C16 · Ruido cósmico e identificación](../programa/clases/B44/B44-C16-ruido-cosmico-e-identificacion/CLASE.md).

### Pila máxima

- La pila máxima es la suma de los marcos activos a la vez.
- La pila máxima es el camino de llamadas con mayor suma de marcos.

💡 **Cómo se explica en la clase [B88-C22](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md):**
- Con anidamiento, la pila máxima es `80 B` y la UART termina a 220 µs; sin anidar, `48 B`, pero TIMER2 espera 40 µs.
- Calcular la pila máxima con anidamiento.
- 🎯 **Por qué importa:** Las interrupciones fijan cuánto tarda el sistema en reaccionar y cuánta pila usa. La decisión central: ¿se permite que una interrupción de mayor prioridad interrumpa a otra, y qué cuesta eso en latencia y pila?
- 🔗 **Se estudia junto con:** latencia, tiempo de respuesta, anidamiento, cota de pila.

📘 **Dónde se aprende** (2 clases): [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md); [B88-C29 · Gestión de memoria determinista en software de vuelo](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md).

### Pipeline

- El pipeline es la secuencia de calibración.
- Una Pipeline encadena transformaciones y modelo y los reajusta dentro de cada pliegue (S1, S2).

💡 **Cómo se explica en la clase [B17-C09](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md):**
- Si divides primero y eliges solo con el entrenamiento, o encadenas la selección y el modelo en una `Pipeline`, la exactitud vuelve a 0,513 y 0,514.
- Paso 4 · repetir. Se rehace la validación con `Pipeline` y particiones por grupo y tiempo.
- 🎯 **Por qué importa:** Un equipo anuncia una exactitud del 95 % para clasificar señales; al aplicarlo a datos de una campaña nueva, baja al 55 %. Nadie mintió: la validación estaba mal hecha.
- 🔗 **Se estudia junto con:** fuga de datos, Preprocesamiento global, autocorrelación, grupo.

📘 **Dónde se aprende** (2 clases): [B17-C09 · Prevención de fuga de datos](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md); [B44-C20 · Pipeline inicial de calibración de imágenes](../programa/clases/B44/B44-C20-pipeline-inicial-de-calibracion-de-imagenes/CLASE.md).

### Piramidal

- Con pares solitarios aparecen la forma angular (como el agua) y la piramidal (como el amoníaco).

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- Con 4, la geometría electrónica es tetraédrica; si todos son enlaces, la forma también lo es (109,47°); si hay un par solitario, la forma es piramidal; si hay dos, angular.
- D4 --> NH3["NH3: 3 enlaces + 1 solitario → piramidal"]
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).
- 🔗 **Se estudia junto con:** dominio de electrones, modelo de repulsión de pares de valencia, geometría electrónica, forma molecular.

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Pirámide

- Una pirámide (*overviews*) son copias a resolución reducida.

💡 **Cómo se explica en la clase [B14-C26](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md):**
- Explicar una pirámide de resoluciones y verificarla con un cálculo independiente.
- Ejercicio 5. ¿Cuántos bytes tiene el nivel de pirámide a un cuarto de resolución (por lado)?
- 🎯 **Por qué importa:** Una escena de satélite pesa cientos de megabytes y tú necesitas un recuadro de 100 × 120 píxeles. Si el formato obliga a leer todo el archivo, gastas tiempo y ancho de banda.
- 🔗 **Se estudia junto con:** ráster, GeoTIFF, tesela, directorio de teselas.

📘 **Dónde se aprende** (1 clase): [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md).

### PIRE

- La PIRE es `P_t − L_t + G_t` (dBW).
- La PIRE es la potencia isótropa radiada equivalente, en dBW.
- PIRE: potencia isotrópica radiada equivalente.

💡 **Cómo se explica en la clase [B89-C05](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md):**
- PT["Pt, perdidas Tx, Gt"] --> PIRE["PIRE"]
- PIRE --> CN0["C/N0 = PIRE - L + G/T - 10 log k"]
- 🎯 **Por qué importa:** El presupuesto de enlace es el documento donde se decide si una misión puede transmitir; un error de 3 dB equivale a duplicar la potencia o el tamaño de la antena. La decisión central: ¿cuánto margen queda y qué tasa de datos máxima admite este enlace?
- 🔗 **Se estudia junto con:** pérdida de espacio libre, G/T, C/N0 = PIRE − L_total + G/T − 10 log₁₀ k, Eb/N0 = C/N0 − 10 log₁₀ R_b.

📘 **Dónde se aprende** (4 clases): [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md); [B89-C05 · Presupuesto de enlace](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md); [B96-C27 · Operación de equipos de radiofrecuencia en la estación](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md); [B120-C02 · Zonas de coordinación entre servicios radioeléctricos](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md).

### Piroxeno

- Un mineral es un sólido cristalino natural de composición química definida: el olivino `(Mg,Fe)₂SiO₄` es una serie entre la forsterita `Mg₂SiO₄` y la fayalita `Fe₂SiO₄`; el piroxeno más sencillo es `MgSiO₃`; la calcita es `CaCO₃`.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Con los pesos atómicos de la NIST (C03): `H₂O = 18,0153`, `CO₂ = 44,0094`, `NH₃ = 17,0308`, forsterita `Mg₂SiO₄ = 2 × 24,3055 + 28,085 + 4 × 15,9994 = 140,6936`, fayalita `Fe₂SiO₄ = 203,7726`, piroxeno `MgSiO₃ = 100,3887` y calcita `CaCO₃ = 100,0868 g/mol`.
- La razón Mg/Si de la forsterita es 2 y la del piroxeno `MgSiO₃` es 1.
- ⚠️ **Error frecuente:** Confundir la masa formular de olivino con la de piroxeno. Se corrige con el ejercicio 1.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).
- 🔗 **Se estudia junto con:** hielo, mineral, olivino, forsterita.

📘 **Dónde se aprende** (1 clase): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md).

### Piso de escala

- El piso de escala (0,10 mag) impide dividir por una escala diminuta.

💡 **Cómo se explica en la clase [B129-C04](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md):**
- Detectar valores atípicos con la mediana de otros observadores y la MAD, con un piso de escala.
- Ejercicio 3 · casi autónomo. Calcula la escala robusta con piso 0,10.
- 🎯 **Por qué importa:** Un lote de contribuciones trae errores de tecleo, duplicados, fechas imposibles y mediciones erróneas. La decisión central: ¿qué filtro aplicar para atrapar los errores sin tirar datos buenos, y cómo se sabe que funciona?
- 🔗 **Se estudia junto con:** esquema, duplicado, valor atípico, escala robusta.

📘 **Dónde se aprende** (1 clase): [B129-C04 · Contribución de medidas voluntarias con control de calidad](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md).

### Piso de ruido

- Fuente y víctima: quien emite y quien sufre. Piso de ruido: `k T B`.
- Identificable: parámetro que cambia las mediciones. Piso de ruido: error que queda por el ruido de medida.

💡 **Cómo se explica en la clase [B90-C14](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md):**
- Calcular el piso de ruido `kTB` en W y en dBm.
- Piso de ruido -174 dBm/Hz a 290 K = -173.98 dBm/Hz ;
- 🎯 **Por qué importa:** Un transmisor de 1 W deja un armónico de −30 dBm; el piso de ruido de un receptor estrecho está cerca de −132 dBm. La diferencia de más de 100 dB se pierde con facilidad en un chasis de 10 cm.
- 🔗 **Se estudia junto con:** EMI, Fuente y víctima, I/N, Desensibilización.

📘 **Dónde se aprende** (2 clases): [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md); [B101-C05 · Calibración cinemática de manipuladores](../programa/clases/B101/B101-C05-calibracion-cinematica-de-manipuladores/CLASE.md).

### Pista

- Una pista (*track*) es la trayectoria estimada.
- Una pista es un objeto seguido con estado y covarianza.
- Una pista es un conjunto de observaciones de un objeto.

💡 **Cómo se explica en la clase [B15-C20](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md):**
- (R4) RMSE de la pista menor que el de las detecciones sin filtrar;
- Descripción larga: la imagen original es un campo con seis estrellas brillantes y un objeto débil; tras restar el cielo solo quedan el ruido y un punto que cruza la escena de izquierda a derecha y ligeramente hacia abajo; la pista del filtro es una línea casi recta que atraviesa esos puntos.
- 🎯 **Por qué importa:** Detectar y seguir un objeto móvil —un asteroide, un fragmento de basura espacial, un satélite— combina varios problemas: la cámara no apunta exactamente igual en cada imagen, las estrellas fijas saturan la escena, el objeto es débil y la medida es ruidosa.
- 🔗 **Se estudia junto con:** requisito, prueba de extremo a extremo, mediana temporal, imagen de diferencia.

📘 **Dónde se aprende** (3 clases): [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md); [B74-C30 · Asociación de observaciones y correlación de pistas](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md); [B118-C02 · Catálogos de objetos espaciales](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md).

### Pistón

- El pistón es el bloque cilíndrico del techo que desciende.

💡 **Cómo se explica en la clase [B70-C03](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md):**
- Tras el colapso, el pistón baja `d = V_ev/(πR²)`.
- Resulta `ΔP_c = 4 MPa` (basta evacuar `0,2 km³`) y, evacuados `50 km³`, el pistón baja `159,2 m`.
- 🎯 **Por qué importa:** Evacuar magma no siempre hunde el techo. La decisión central: ¿cuánta subpresión resiste un techo y cuánto magma hay que sacar para vencerla?
- 🔗 **Se estudia junto con:** falla anular, subpresión, balance de volumen.

📘 **Dónde se aprende** (1 clase): [B70-C03 · Calderas planetarias: formación y colapso](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md).

### Pivote

- El pivote es el coeficiente que se usa para eliminar.
- Un pivote es el elemento de la diagonal usado para eliminar.
- El pivote es el apoyo único de la balanza.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C03](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md):**
- Al elegir en cada paso el pivote de mayor tamaño (pivoteo parcial) se reducen errores de redondeo.
- 🎯 **Por qué importa:** Un detector no entrega «brillo»: entrega cuentas. Para convertir cuentas en flujo hay que descubrir dos números, una pendiente y un desfase, y para ello se miden dos fuentes de referencia.
- 🔗 **Se estudia junto con:** sistema de ecuaciones, lineal, solución, compatible determinado.

📘 **Dónde se aprende** (5 clases): [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md); [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md); [B43-C09 · Celdas y soporte de espejos](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md); [B48-C08 · Automatización de cúpulas](../programa/clases/B48/B48-C08-automatizacion-de-cupulas/CLASE.md); [B50-C11 · Errores de inclinación de elementos y superficies](../programa/clases/B50/B50-C11-errores-de-inclinacion-de-elementos-y-superficies/CLASE.md).

### Pivote libre de coma

- El pivote libre de coma anula ese coeficiente.

💡 **Cómo se explica en la clase [B50-C11](../programa/clases/B50/B50-C11-errores-de-inclinacion-de-elementos-y-superficies/CLASE.md):**
- Hallar el pivote libre de coma por secante.
- Ejercicio 8. Reducción del RMS en el pivote libre de coma.
- 🎯 **Por qué importa:** Un telescopio se alinea corrigiendo inclinaciones y descentramientos. La decisión central: ¿alrededor de qué punto conviene inclinar el secundario para no generar coma?
- 🔗 **Se estudia junto con:** inclinación, pivote, descentrarlo, coeficiente de coma firmado.

📘 **Dónde se aprende** (1 clase): [B50-C11 · Errores de inclinación de elementos y superficies](../programa/clases/B50/B50-C11-errores-de-inclinacion-de-elementos-y-superficies/CLASE.md).

### Pivoteo parcial

- El pivoteo parcial elige como pivote el mayor valor absoluto de la columna.

💡 **Contexto en la clase [B10-C05](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md):**
- **Idea central (modelo mental):** Eliminar es convertir el sistema en una escalera; luego bajas escalón por escalón.
- 🎯 **Por qué importa:** Para fijar la posición de un objeto a partir de las distancias a tres estaciones se plantean tres ecuaciones con dos incógnitas (plano). Los sistemas reales tienen decenas o miles de incógnitas: parámetros orbitales, sesgos de relojes, coeficientes de calibración.
- 🔗 **Se estudia junto con:** sistema lineal, matriz ampliada, operación elemental de fila, eliminación gaussiana.

📘 **Dónde se aprende** (1 clase): [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md).

### Píxel

- Un píxel es una celda.

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- La varianza de un píxel de cielo es: lectura `σ_L²` + fotones (`cielo + oscuro`) + el ruido del oscuro maestro, que vale `(σ_L² + oscuro)/K` si se promedian `K` oscuros.
- Se suman los píxeles de una apertura de radio 5 px (81 píxeles) y se resta el fondo estimado como la mediana de un anillo (de 8 a 12 píxeles de radio): `F = Σ_ap (I − fondo)`.
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.
- 🔗 **Se estudia junto con:** imagen digital, ADU, ganancia, bias.

📘 **Dónde se aprende** (1 clase): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md).

### Píxel caliente

- Un píxel caliente tiene una tasa mucho mayor que la media.
- El píxel caliente da más señal que el vecino; el muerto, menos o ninguna.

💡 **Cómo se explica en la clase [B44-C13](../programa/clases/B44/B44-C13-calibracion-con-dark/CLASE.md):**
- Ejercicio 5. Tasa de un píxel caliente que acumula `600 e⁻` en `300 s`.
- Ejercicio 10 · transferencia. Transferencia. ¿Qué hace un píxel caliente en la imagen?
- 🎯 **Por qué importa:** La oscuridad depende de la exposición y de la temperatura, y algunos píxeles son muy calientes. La decisión central: ¿se puede reutilizar un dark de otra exposición, y a qué costo en ruido?
- 🔗 **Se estudia junto con:** dark maestro, reescalado, amplificación del ruido.

📘 **Dónde se aprende** (2 clases): [B44-C13 · Calibración con dark](../programa/clases/B44/B44-C13-calibracion-con-dark/CLASE.md); [B44-C15 · Píxeles defectuosos](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md).

### Píxel mixto

- El píxel mixto suma la emisión de fondo y de lava.

💡 **Contexto en la clase [B70-C05](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md):**
- **Idea central (modelo mental):** Una brasa muy brillante en un cuarto ya tibio se nota si ocupa algo de la vista; cuanto más corta la longitud de onda, más contrasta, porque la emisión crece de forma exponencial con la temperatura.
- 🎯 **Por qué importa:** Un punto brillante o un vent que cambia no prueba una erupción. La decisión central: ¿cuánta lava caliente hace falta en un píxel para producir un aumento medible de radiancia, y qué otras explicaciones hay que descartar?
- 🔗 **Se estudia junto con:** corona, llanura, radiancia, fracción.

📘 **Dónde se aprende** (1 clase): [B70-C05 · Actividad volcánica venusina: llanuras, coronas e indicios de actividad reciente](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md).

### Placa de Kirchhoff

- La placa de Kirchhoff es un disco delgado.

💡 **Contexto en la clase [B43-C03](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md):**
- **Idea central (modelo mental):** Como una tabla de cocina apoyada en dos bordes que se comba por su propio peso: al duplicar el espesor la flecha cae a la cuarta parte; el material solo fija la constante.
- 🎯 **Por qué importa:** Un buen material no es el más duro ni el más estable: es el que deja el menor error de forma para una masa y un presupuesto. La decisión central: ¿qué material y qué espesor mantienen la flexión y la deriva térmica por debajo de la tolerancia?
- 🔗 **Se estudia junto con:** módulo de Young, rigidez específica, figura de mérito térmica, ecuación biarmónica.

📘 **Dónde se aprende** (1 clase): [B43-C03 · Materiales para espejos](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md).

### Placa de media onda

- La placa de media onda gira el plano; con un analizador fijo la señal es `I_k = ½[I + Q cos 4θ_k + U sin 4θ_k]`.

💡 **Contexto en la clase [B45-C16](../programa/clases/B45/B45-C16-polarimetros-astronomicos/CLASE.md):**
- **Idea central (modelo mental):** Como un faro que gira: la luz recibida sube y baja con el ángulo; la amplitud y la fase de esa oscilación dan la polarización.
- 🎯 **Por qué importa:** La polarización medida es siempre positiva y por eso sesgada hacia arriba cuando el ruido es comparable a la señal. La decisión central: ¿cómo se miden Q y U y cómo se corrige el sesgo?
- 🔗 **Se estudia junto con:** analizador fijo, demodulación, polarización instrumental, sesgo.

📘 **Dónde se aprende** (1 clase): [B45-C16 · Polarímetros astronómicos](../programa/clases/B45/B45-C16-polarimetros-astronomicos/CLASE.md).

### Placa de Schmidt

- La placa de Schmidt es un elemento delgado cuya forma `s(r) = a r⁴ + b r²` desvía los rayos en `−(n − 1) ∇s`.

💡 **Cómo se explica en la clase [B50-C03](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md):**
- La placa de Schmidt aquí es un modelo de espesor delgado (desviación y camino óptico), no una placa trazada superficie por superficie.
- Una placa de Schmidt lo lleva a `0,0031` ondas en el eje.
- ⚠️ **Error frecuente:** Creer que la placa de Schmidt es una lente trazada. Se corrige con 8.4.
- 🎯 **Por qué importa:** Combinar espejos y elementos refractivos permite campos amplios con superficies fáciles de fabricar. La decisión central: ¿dónde va el diafragma y qué corrige el elemento refractivo?
- 🔗 **Se estudia junto con:** centro de curvatura, diafragma, menisco, RMS sin enfoque.

📘 **Dónde se aprende** (1 clase): [B50-C03 · Sistemas catadióptricos: Schmidt y Maksutov](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md).

### Placa seca de gelatina

- La placa seca de gelatina es una placa de vidrio con emulsión que se desarrolló a comienzos de la década de 1870 (Maddox) y que, según S5, llegó a ser más sensible y barata.

💡 **Cómo se explica en la clase [B02-C17](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md):**
- S5 lo califica de primera persona en fotografiar un objeto celeste); 1850, Vega con 90 s (Bond y Whipple, S4); comienzos de la década de 1870, placas secas de gelatina desarrolladas por Maddox (S5); 1880, la nebulosa de Orión de Henry Draper, hijo de John W.
- El daguerrotipo (Draper 1840, Bond y Whipple 1850) fue el primer registro; las placas secas de gelatina de la década de 1870 llegaron a ser más sensibles y baratas, y con una de ellas Henry Draper expuso 51 minutos la nebulosa de Orión (S5).
- 🎯 **Por qué importa:** Un dibujo depende de quien lo hace; una placa registra lo que llegó. La pregunta motivadora es: ¿qué cambia cuando la observación puede guardarse, compararse años después y medirse?
- 🔗 **Se estudia junto con:** astrofotografía, daguerrotipo, exposición, seguimiento.

📘 **Dónde se aprende** (1 clase): [B02-C17 · Nacimiento de la astrofotografía](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md).

### Plan

- La verdad es la integración no lineal; el plan usa HCW con el estado estimado.
- Un plan es un subconjunto de objetivos con un orden y unos instantes de inicio.

💡 **Cómo se explica en la clase [B76-C20](../programa/clases/B76/B76-C20-simulacion-de-encuentro-seguro/CLASE.md):**
- Es el cambio que el ejercicio 10 desaconseja: con `15 m` el plan no cumple.
- Descripción larga: el plan cumple los criterios supuestos, pero el margen con el fallo del último impulso es de solo seis metros.
- 🎯 **Por qué importa:** Cada pieza del bloque funciona en su caso ideal; la seguridad se juega en la combinación con errores. La decisión central: ¿llega el perseguidor con la precisión pedida y se mantiene fuera de la esfera de exclusión incluso si falla un impulso?
- 🔗 **Se estudia junto con:** Monte Carlo, percentil 95, verdad, incursión.

📘 **Dónde se aprende** (2 clases): [B76-C20 · Simulación de encuentro seguro](../programa/clases/B76/B76-C20-simulacion-de-encuentro-seguro/CLASE.md); [B98-C01 · Planificación por objetivos a bordo](../programa/clases/B98/B98-C01-planificacion-por-objetivos-a-bordo/CLASE.md).

### Plan de contactos

- Un plan de contactos es la lista de contactos previstos.
- El plan de contactos es la lista de contactos futuros.

💡 **Cómo se explica en la clase [B89-C13](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md):**
- Un paquete creado a las 26 h ya no tiene contacto con el rover en este plan y no llega.
- PL["plan de contactos"] --> RT["llegada mas temprana"]
- 🎯 **Por qué importa:** Sin almacenamiento y reenvío, un rover marciano no podría comunicarse con Tierra: nunca hay una ruta continua. Entender los contactos, las capacidades y el encaminamiento es la base del diseño de redes interplanetarias.
- 🔗 **Se estudia junto con:** Bundle Protocol (BP), almacenamiento y reenvío, contacto, capacidad.

📘 **Dónde se aprende** (2 clases): [B89-C13 · Protocolos para espacio profundo](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md); [B94-C04 · Redes con retardo y desconexión: enrutamiento y almacenamiento](../programa/clases/B94/B94-C04-redes-con-retardo-y-desconexion-enrutamiento-y-almacenamiento/CLASE.md).

### Plan de contingencia

- Un plan de contingencia dice qué se hace si falla algo (nubes, equipo, lesión).

💡 **Cómo se explica en la clase [B08-C20](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md):**
- *Descripción textual:* el objetivo se traduce en requisitos, que se cumplen mediante componentes y se demuestran con comprobaciones; si todos los requisitos críticos se cumplen, la campaña sale (GO), si no, se cancela con un plan de contingencia, y en ambos casos se escribe un informe.
- Plan de contingencia: si hay más del 50 % de nubes a las 23:00 UT, se cancela y se hace una sesión de datos.
- 🎯 **Por qué importa:** Una salida sin plan termina en una noche perdida o en un accidente. La pregunta motivadora: ¿cómo preparo una salida de observación para que sea segura, útil, accesible y reproducible?
- 🔗 **Se estudia junto con:** requisito, verificable, criterio de comprobación, método de comprobación.

📘 **Dónde se aprende** (1 clase): [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md).

### Plan de continuidad de operaciones

- El plan de continuidad de operaciones define cómo seguir funcionando.

💡 **Cómo se explica en la clase [B122-C10](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md):**
- La evidencia es la plan de continuidad de operaciones sintético del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *plan de continuidad de operaciones sintético*: funciones, plantillas, efecto de `p`, probabilidad conjunta, supuestos y lo consultado o sintético, con el aviso de que no es asesoría.
- 🎯 **Por qué importa:** No hay clase equivalente sobre continuidad de funciones institucionales. La decisión central: ¿qué dotación mínima asegura que cada función esencial se cubra con al menos el 99 %?
- 🔗 **Se estudia junto con:** función esencial, dotación mínima, plantilla, disponibilidad individual.

📘 **Dónde se aprende** (1 clase): [B122-C10 · Planes de continuidad institucional y de operaciones](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md).

### Plan de operación

- Eficiencia de carga: parte de la energía generada que se almacena. Plan de operación: cuándo se enciende la carga útil.

💡 **Cómo se explica en la clase [B96-C12](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md):**
- El script [balance_de_energia.py](balance_de_energia.py) simula el SOC de la batería durante 30 órbitas con cuatro planes de operación, calcula la DoD máxima y la contrasta con la fórmula analítica;
- 🎯 **Por qué importa:** Una batería descargada en exceso se degrada y una nave sin energía deja de ser comandable. La decisión central: ¿qué plan de operación mantiene la batería dentro de su criterio de descarga y recupera la carga en cada órbita?
- 🔗 **Se estudia junto con:** SOC, DoD, Carga base, Balance neto.

📘 **Dónde se aprende** (1 clase): [B96-C12 · Gestión de energía en operaciones](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md).

### Plan defectuoso

- Un plan defectuoso es un contraejemplo que incumple reglas a propósito para probar el validador.

💡 **Cómo se explica en la clase [B131-C11](../programa/clases/B131/B131-C11-plan-completo-de-una-clase-de-astronomia/CLASE.md):**
- Descripción larga: el plan propuesto pasa las cinco reglas; el defectuoso incumple tiempos, alineación, exposición continua y seguridad.
- Ejercicio 6 · autónomo. ¿Qué fallos encuentra el validador en el plan defectuoso?
- 🎯 **Por qué importa:** Un buen plan se puede revisar: sus tiempos suman, cada resultado tiene actividad y evaluación, y nada pone en riesgo a nadie. La decisión central: ¿este plan es coherente y seguro antes de entrar al aula?
- 🔗 **Se estudia junto con:** bloque, alineación, evaluación formativa.

📘 **Dónde se aprende** (1 clase): [B131-C11 · Plan completo de una clase de astronomía](../programa/clases/B131/B131-C11-plan-completo-de-una-clase-de-astronomia/CLASE.md).

### Plan regresivo

- El plan regresivo parte de la fecha final.

💡 **Contexto en la clase [B120-C06](../programa/clases/B120/B120-C06-caso-de-planificacion-regulatoria-de-un-sistema-satelital/CLASE.md):**
- 🎯 **Por qué importa:** Integrar licencias, frecuencias y plazos en un plan es el cierre del módulo y no existe un caso integrador regulatorio. La decisión central: ¿cuándo debe presentarse la publicación anticipada para que haya tiempo de coordinar y holgura frente al plazo, y qué riesgo restante queda?
- 🔗 **Se estudia junto con:** ventana de anticipación, holgura, margen de coordinación, hito.

📘 **Dónde se aprende** (1 clase): [B120-C06 · Caso de planificación regulatoria de un sistema satelital](../programa/clases/B120/B120-C06-caso-de-planificacion-regulatoria-de-un-sistema-satelital/CLASE.md).

### Planeta

- Un planeta (según la IAU, en nuestro sistema solar) es un cuerpo que orbita el Sol, tiene masa suficiente para que su gravedad lo vuelva casi redondo y ha *despejado la vecindad* de su órbita.

💡 **Cómo se explica en la clase [B01-C03](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md):**
- Planeta enano cumple (a) y (b), pero no (c), y no es satélite.
- Con esas reglas, Plutón es un planeta enano porque la propia resolución B6 lo declara así al aplicarlas (S1).
- ⚠️ **Error frecuente:** Confundir tamaño con categoría. «La Luna es mayor que Plutón, entonces es un planeta».
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».
- 🔗 **Se estudia junto con:** planeta enano, cuerpo menor del sistema solar, satélite, estrella.

📘 **Dónde se aprende** (1 clase): [B01-C03 · Objetos celestes y sus diferencias](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md).

### Planeta enano

- Un planeta enano orbita el Sol y es casi redondo, pero no ha despejado su vecindad y no es satélite.

💡 **Cómo se explica en la clase [B01-C03](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md):**
- Planeta enano cumple (a) y (b), pero no (c), y no es satélite.
- Con esas reglas, Plutón es un planeta enano porque la propia resolución B6 lo declara así al aplicarlas (S1).
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».
- 🔗 **Se estudia junto con:** planeta, cuerpo menor del sistema solar, satélite, estrella.

📘 **Dónde se aprende** (1 clase): [B01-C03 · Objetos celestes y sus diferencias](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md).

### Planeta exterior

- Un planeta exterior orbita más lejos del Sol que la Tierra; uno interior, más cerca.

💡 **Cómo se explica en la clase [B02-C11](../programa/clases/B02/B02-C11-revolucion-copernicana-y-metodos/CLASE.md):**
- Deducir el sinódico de un planeta exterior desde los períodos orbitales.
- Ejercicio 12 · integrador. Elabora la *ficha del método sinódico* (sección 20): elige un planeta exterior con datos publicados que consultes, calcula `S`, compara con el valor publicado y declara los supuestos.
- 🎯 **Por qué importa:** La «revolución copernicana» suele resumirse como «el Sol en el centro». Pero lo que cambió la ciencia fue que el modelo permitió calcular cosas nuevas: convertir lo observado en lo real.
- 🔗 **Se estudia junto con:** período sidéreo, período sinódico, interior, oposición.

📘 **Dónde se aprende** (1 clase): [B02-C11 · Revolución copernicana y métodos](../programa/clases/B02/B02-C11-revolucion-copernicana-y-metodos/CLASE.md).

### Planeta interior

- Un planeta interior (Mercurio, Venus) tiene su órbita dentro de la de la Tierra; uno exterior (Marte, Júpiter, Saturno), fuera.

💡 **Cómo se explica en la clase [B08-C10](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md):**
- Un planeta interior corre más rápido y da vueltas a la Tierra; visto desde esta, parece oscilar a un lado y otro del Sol sin alejarse más que un cierto ángulo.
- A["Planeta interior"] --> B["Oscila a ambos lados del Sol<br/>elongación ≤ ε_max<br/>sen ε_max = a / 1 UA"]
- 🎯 **Por qué importa:** Los planetas parecen «estrellas errantes» y un titular promete «alineación de planetas». La pregunta motivadora: ¿qué planetas puedo ver esta noche, dónde y a qué hora?
- 🔗 **Se estudia junto con:** elongación, este, oeste, exterior.

📘 **Dónde se aprende** (1 clase): [B08-C10 · Planetas observables y elongación](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md).

### Planetocéntrica

- La latitud planetográfica `φg` mide el ángulo de la normal al elipsoide con el plano ecuatorial; la planetocéntrica `φc`, del radio vector.

💡 **Cómo se explica en la clase [B53-C06](../programa/clases/B53/B53-C06-geodesia-de-marte/CLASE.md):**
- C["lat planetocentrica"] --> G["lat planetografica"]
- Convertir latitud planetocéntrica y planetográfica.
- 🎯 **Por qué importa:** Una altura de 1 km no significa lo mismo sobre una esfera que sobre un elipsoide. La decisión central: ¿qué latitud y qué referencia usa cada producto, y cuánto difieren?
- 🔗 **Se estudia junto con:** latitud planetográfica, altura elipsoidal, areoide.

📘 **Dónde se aprende** (1 clase): [B53-C06 · Geodesia de Marte](../programa/clases/B53/B53-C06-geodesia-de-marte/CLASE.md).

### Planificable

- Una tarea planificable cumple `Rᵢ ≤ Dᵢ`.

💡 **Contexto en la clase [B88-C05](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md):**
- 🎯 **Por qué importa:** En una nave, una tarea de control que llega tarde puede ser tan mala como una que da un resultado incorrecto. La decisión central: ¿cada tarea termina siempre antes de su plazo, aun cuando las de mayor prioridad la interrumpen?
- 🔗 **Se estudia junto con:** tiempo de respuesta, plazo duro, blando, hiperperiodo.

📘 **Dónde se aprende** (1 clase): [B88-C05 · Sistemas de tiempo real](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md).

### Planificación a priori

- La planificación a priori reserva capacidad para todos antes de que la pidan.

💡 **Contexto en la clase [B120-C03](../programa/clases/B120/B120-C03-posiciones-orbitales-y-espectro-como-recursos-limitados/CLASE.md):**
- 🎯 **Por qué importa:** Las posiciones orbitales y el espectro son recursos escasos con reglas de asignación y no están tratados como concepto jurídico. La decisión central: ¿cuánto recurso hay, quién lo obtiene bajo cada régimen y qué mide la desigualdad del reparto?
- 🔗 **Se estudia junto con:** recurso limitado, acceso equitativo, orden de llegada, diligencia debida.

📘 **Dónde se aprende** (1 clase): [B120-C03 · Posiciones orbitales y espectro como recursos limitados](../programa/clases/B120/B120-C03-posiciones-orbitales-y-espectro-como-recursos-limitados/CLASE.md).

### Planificación por lista

- La planificación por lista asigna tareas listas al robot libre.

💡 **Contexto en la clase [B97-C13](../programa/clases/B97/B97-C13-ensamblaje-de-estructuras-en-orbita/CLASE.md):**
- 🎯 **Por qué importa:** Añadir robots no acorta el trabajo indefinidamente: hay un punto en que la ruta crítica manda. Conocerlo evita lanzar una flota de robots que quedan esperando.
- 🔗 **Se estudia junto con:** tarea, ruta crítica, makespan, eficiencia.

📘 **Dónde se aprende** (1 clase): [B97-C13 · Ensamblaje de estructuras en órbita](../programa/clases/B97/B97-C13-ensamblaje-de-estructuras-en-orbita/CLASE.md).

### Planificador

- Un planificador asigna recursos a trabajos en cola.

💡 **Cómo se explica en la clase [B14-C16](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md):**
- El guion no se envía a ningún planificador.
- Describir un clúster en términos de nodos, particiones, planificador y trabajos.
- 🎯 **Por qué importa:** Una simulación de la población de escombros orbitales requiere cien veces más cálculo del que tu equipo puede dar en una semana. Pides tiempo en un clúster y debes decidir: ¿cuántos procesos pido?
- 🔗 **Se estudia junto con:** clúster, escalado fuerte, escalado débil, ley de Gustafson.

📘 **Dónde se aprende** (1 clase): [B14-C16 · Computación distribuida y HPC](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md).

### Planisferio

- Un planisferio (carta celeste giratoria) tiene un disco con el mapa del cielo y una máscara con una ventana ovalada que representa el horizonte; al girar el disco hasta alinear fecha y hora, la ventana deja ver lo que está sobre el horizonte.

💡 **Cómo se explica en la clase [B08-C07](../programa/clases/B08/B08-C07-planisferios-y-aplicaciones-celestes/CLASE.md):**
- Pausa. Si usas un planisferio hecho para −45° en tu lugar a −30°, ¿cuánto se equivoca la altura del polo? <details><summary>Respuesta</summary>15°: el polo estaría dibujado a 45° y en tu cielo está a 30°.</details>
- Falla porque un planisferio muestra el cielo a una latitud; fuera de esa latitud la ventana ya no coincide con tu horizonte.
- ⚠️ **Error frecuente:** Usar un planisferio de otra latitud. Ejercicio 11.
- 🎯 **Por qué importa:** Una herramienta que no entiendes es una caja negra: si la aplicación se equivoca de ubicación o de hora, no lo notarás. La pregunta motivadora: ¿puedo confiar en lo que me muestra la herramienta, y qué hago si no hay batería?
- 🔗 **Se estudia junto con:** aplicación de planetario, Stellarium, modo nocturno rojo, hora oficial.

📘 **Dónde se aprende** (1 clase): [B08-C07 · Planisferios y aplicaciones celestes](../programa/clases/B08/B08-C07-planisferios-y-aplicaciones-celestes/CLASE.md).

### Planitud

- La planitud es el rango de los residuos al plano.

💡 **Cómo se explica en la clase [B84-C18](../programa/clases/B84/B84-C18-control-dimensional/CLASE.md):**
- Con 49 puntos y alabeo de 8 µm más ruido de 2 µm, la planitud (máx − mín de residuos) es `10,72 µm`.
- Calcular redondez y planitud de los residuos.
- 🎯 **Por qué importa:** Una pieza «dentro de tolerancia» con una medida que tiene 5 µm de incertidumbre en una tolerancia de 10 µm no está demostrada. La decisión central: ¿qué diámetro tiene el agujero, con qué incertidumbre y cuántos puntos hacen falta?
- 🔗 **Se estudia junto con:** ajuste algebraico (Kåsa), redondez, incertidumbre expandida.

📘 **Dónde se aprende** (1 clase): [B84-C18 · Control dimensional](../programa/clases/B84/B84-C18-control-dimensional/CLASE.md).

### Plano

- Un espacio es plano si el Riemann es cero.
- El plano corrige la ganancia por píxel.
- Ruido de disparo: fluctuación de Poisson de los fotones. Plano (*flat*): imagen de iluminación uniforme.

💡 **Cómo se explica en la clase [B39-C03](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md):**
- Un cilindro de papel se desenrolla sin deformarse (plano); una pelota no (curva): el Riemann detecta esa diferencia.
- Ejercicio 9 · transferencia. Transferencia. Un compañero dice que vacío significa espacio plano.
- ⚠️ **Error frecuente:** Confundir Ricci cero con plano. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un espacio-tiempo es curvo si el Riemann no se anula. La decisión central: ¿qué mide cada contracción del Riemann y cómo se comprueba un cálculo de curvatura?
- 🔗 **Se estudia junto con:** tensor de Riemann, tensor de Ricci, curvatura escalar, escalar de Kretschmann.

📘 **Dónde se aprende** (3 clases): [B39-C03 · Tensor de Riemann, Ricci y curvatura escalar](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md); [B45-C19 · Reducción e incertidumbre instrumental](../programa/clases/B45/B45-C19-reduccion-e-incertidumbre-instrumental/CLASE.md); [B48-C13 · Calibraciones nocturnas](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md).

### Plano B

- El plano B es el plano perpendicular a la velocidad relativa del objeto en el infinito y que pasa por el centro de la Tierra.
- El plano B pasa por el centro del planeta y es perpendicular a `S`.

💡 **Cómo se explica en la clase [B58-C09](../programa/clases/B58/B58-C09-probabilidades-de-impacto/CLASE.md):**
- N["nube gaussiana en el plano B"] --> I["integral sobre el disco"]
- Definir el plano B y el radio efectivo con enfoque gravitatorio.
- 🎯 **Por qué importa:** La probabilidad de impacto resume la incertidumbre en un número que alimenta las escalas (C10) y las decisiones (C17–C19). La decisión central: ¿qué área de la nube de posibles posiciones cae sobre la Tierra, y cuánto cambia si la nube se achica o se desplaza?
- 🔗 **Se estudia junto con:** radio efectivo, probabilidad de impacto, cuadratura, encuentro rápido.

📘 **Dónde se aprende** (2 clases): [B58-C09 · Probabilidades de impacto](../programa/clases/B58/B58-C09-probabilidades-de-impacto/CLASE.md); [B75-C24 · Plano B y parámetro de impacto](../programa/clases/B75/B75-C24-plano-b-y-parametro-de-impacto/CLASE.md).

### Plano cartesiano

- Un plano cartesiano tiene dos ejes perpendiculares que se cortan en el origen `(0, 0)`.

💡 **Contexto en la clase [B03-C15](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md):**
- **Idea central (modelo mental):** Cada punto es el resultado de dos conversiones, una por eje, y debe poder invertirse. ```mermaid flowchart LR D["Dato (a = 5,2038 au;
- 🎯 **Por qué importa:** Las fichas de la NASA dan semiejes y períodos de los ocho planetas. En una tabla son 16 números.
- 🔗 **Se estudia junto con:** origen, par ordenado, abscisa, ordenada.

📘 **Dónde se aprende** (1 clase): [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md).

### Plano de tierra

- El monopolo es la mitad de un dipolo sobre un plano de tierra.

💡 **Cómo se explica en la clase [B49-C01](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar el plano de tierra del monopolo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Sin la resistencia de radiación no se sabe qué carga ve la línea ni cuánta potencia se irradia. La decisión central: ¿de qué longitud hacer el hilo y qué impedancia presentará a la línea?
- 🔗 **Se estudia junto con:** dipolo, monopolo, resistencia de radiación, corriente de alimentación.

📘 **Dónde se aprende** (1 clase): [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md).

### Plano orbital con β = 0

- El plano orbital con `β = 0` es el de eclipse máximo.

💡 **Contexto en la clase [B78-C22](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md):**
- 🎯 **Por qué importa:** El Δv diario de un propulsor eléctrico es el ideal multiplicado por el ciclo de trabajo, y este puede ser menos de la mitad. La decisión central: ¿cuánto tiempo del día puede empujar un propulsor ilustrativo y cuánto tarda entonces en elevar la órbita?
- 🔗 **Se estudia junto con:** ciclo de trabajo, eclipse, fracción útil, elevación de órbita.

📘 **Dónde se aprende** (1 clase): [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md).

### Plano uv

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B46-C16](../programa/clases/B46/B46-C16-sintesis-de-apertura/CLASE.md):**
- La aproximación de plano del cielo falla en campos grandes.
- *Descripción textual:* las posiciones de las antenas y la rotación definen el muestreo del plano `uv`, cuya transformada es el haz sucio.
- 🎯 **Por qué importa:** Un interferómetro con pocas antenas solo muestrea unos puntos del plano `uv`; la rotación de la Tierra los multiplica. La decisión central: ¿qué cobertura `uv` y qué haz sucio da una disposición de antenas?
- 🔗 **Se estudia junto con:** síntesis de rotación, haz sucio, lóbulo lateral, resolución.

📘 **Dónde se aprende** (1 clase): [B46-C16 · Síntesis de apertura](../programa/clases/B46/B46-C16-sintesis-de-apertura/CLASE.md).

### Planos principales

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C05](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md):**
- En la biconvexa gruesa, `f = 103,786 mm`, la distancia focal posterior medida desde el vértice es `89,638 mm` y el plano principal posterior está `14,148 mm` dentro de la lente (fórmula de libro `−14,148 mm`).
- El espesor mueve los planos principales y cambia la focal efectiva.
- ⚠️ **Error frecuente:** Medir `f` desde el vértice. Se mide desde el plano principal.
- 🎯 **Por qué importa:** El objetivo de un refractor es una lente. La decisión central: ¿cuánto se equivoca la fórmula de lente delgada cuando la lente es gruesa?
- 🔗 **Se estudia junto con:** lente delgada, ecuación del fabricante, matriz de rayos, distancia focal posterior.

📘 **Dónde se aprende** (1 clase): [B41-C05 · Lentes delgadas y gruesas](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md).

### Planta

- La planta es la fuente de potencia, con masa `α P`.

💡 **Cómo se explica en la clase [B78-C17](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md):**
- *Descripción textual:* el propelente fija la potencia y la planta, que suman a la masa final, que a su vez fija el propelente: se resuelve iterando o por bisección.
- Por masas: propelente, tanques y planta.
- ⚠️ **Error frecuente:** Olvidar tanques y planta. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una hoja de presupuesto honesta incluye márgenes y reservas, y esos márgenes cuestan masa. La decisión central: ¿cuánto propelente, tanques y planta hacen falta para un Δv con margen, y qué arquitectura da la menor masa total en cada caso?
- 🔗 **Se estudia junto con:** masa seca, margen de Δv, residuo, fracción de tanques.

📘 **Dónde se aprende** (1 clase): [B78-C17 · Masa de propelente y presupuesto](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md).

### Planta de potencia

- La planta de potencia es la fuente que alimenta al propulsor.

💡 **Cómo se explica en la clase [B78-C06](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md):**
- No: faltan la masa de la planta de potencia, la vida útil y la madurez (C15, C19, C21).
- Límites: chorro monoenergético, `η` constante, masa constante en el cálculo de tiempo; no incluye la masa de la planta de potencia.
- 🎯 **Por qué importa:** Subir el `Isp` ahorra propelente, pero el mismo vatio produce menos empuje y la maniobra tarda más. La decisión central: ¿cuánto empuje da cada kilovatio, cómo cae con el `Isp` y qué pasa con el tiempo de maniobra?
- 🔗 **Se estudia junto con:** potencia del chorro, eficiencia total, empuje por potencia, limitado por potencia.

📘 **Dónde se aprende** (1 clase): [B78-C06 · Propulsión eléctrica general](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md).

### Plantilla

- La plantilla es la forma de onda modelada.
- La plantilla es el trozo de referencia.
- La plantilla `n` es el equipo total.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C21](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md):**
- Para `M ≥ 0,97` (pérdida del 3 % de la señal-ruido) con el tiempo de coalescencia fijo, la masa de chirrido debe conocerse con `0,15 %`: el banco necesita plantillas muy próximas.
- *Descripción textual:* la masa de chirrido da la frecuencia y la fase, de ahí la forma de onda; el filtro acoplado la correlaciona con los datos y el desajuste con plantillas vecinas fija el banco.
- ⚠️ **Error frecuente:** Normalizar mal la plantilla. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Una plantilla ligeramente errada pierde mucha señal-ruido, porque la fase acumula miles de ciclos. Entender cuánto determina cuántas plantillas hacen falta.
- 🔗 **Se estudia junto con:** chirrido, filtro acoplado, desajuste, banco.

📘 **Dónde se aprende** (4 clases): [B28-C21 · Formas de onda gravitacionales y filtro acoplado](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md); [B74-C26 · Navegación por hitos y correlación de terreno](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md); [B122-C10 · Planes de continuidad institucional y de operaciones](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md).

### Plasma

- En un sólido las partículas ocupan posiciones casi fijas; en un líquido están juntas pero se deslizan; en un gas están lejos y se mueven libres; en un plasma el gas está parcialmente o totalmente ionizado, es decir, hay electrones libres e iones.

💡 **Cómo se explica en la clase [B06-C10](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md):**
- El plasma se obtiene cuando la agitación (o la radiación) es tan intensa que arranca electrones de los átomos.
- En el universo observable, la materia ordinaria que brilla, como las estrellas y el gas entre ellas, está en gran parte en estado de plasma (se estudia en B30).
- ⚠️ **Error frecuente:** Afirmar que el plasma es raro. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** En Marte, la temperatura media es 214 K y la presión media en superficie 6,36 mb (S1). Ese valor está casi en el punto triple del agua, la presión mínima a la que puede existir agua líquida (S2).
- 🔗 **Se estudia junto con:** materia, estados, sólido, líquido.

📖 **Explicado a fondo:** [Plasma](esencial/esencial-m-z.md#plasma) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md).

### Plasma ópticamente delgado

- Un plasma ópticamente delgado deja escapar su radiación.

💡 **Cómo se explica en la clase [B34-C02](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md):**
- Límite: plasma isotermo y ópticamente delgado.
- 🎯 **Por qué importa:** Cada banda del espectro traza una temperatura. La decisión central: ¿en qué banda emite el plasma a una temperatura dada y cuánta potencia radia?
- 🔗 **Se estudia junto con:** medida de emisión, máximo de Wien, energía térmica, bremsstrahlung.

📘 **Dónde se aprende** (1 clase): [B34-C02 · Emisión EUV y rayos X de la corona](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md).

### Plástico perfecto

- Un material plástico perfecto fluye a esfuerzo constante `τ`.

💡 **Cómo se explica en la clase [B70-C02](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md):**
- El modelo plástico perfecto procede de la mecánica del hielo (Nye 1952; solo metadatos consultados [S4]); su uso aquí a un domo de lava es una analogía de modelado, no una medida.
- Límites: plástico perfecto, base plana, sin enfriamiento.
- 🎯 **Por qué importa:** Una colina empinada de lava puede tener una altura que solo depende del material y de `g`. La decisión central: ¿qué altura puede alcanzar un domo de resistencia dada y qué cambiaría en otro mundo?
- 🔗 **Se estudia junto con:** domo, resistencia a la fluencia, vulcanismo evolucionado.

📘 **Dónde se aprende** (1 clase): [B70-C02 · Domos volcánicos y vulcanismo evolucionado](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md).

### Plazo

- El plazo es el tiempo hasta que la consecuencia ocurre si no se atiende.
- El plazo es de un año desde el daño o desde la identificación del Estado de lanzamiento responsable (art.
- El plazo (*latency*) es el tiempo entre la captura y la entrega del producto.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B96-C22](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md):**
- El plazo de 6,5 h se cumple con amplio margen (0,52 h).
- Paso 4 · Plazo. `4 768 × 0,373/0,95 = 0,52 h`.
- ⚠️ **Error frecuente:** Ignorar el plazo. Calcula el tiempo esperado (8.3)
- 🎯 **Por qué importa:** Un dato dañado que se acepta sin verificar contamina los productos científicos; y una transferencia lenta rompe el plazo de entrega. La decisión central: ¿cómo se comprueba la integridad y cuánto tarda la transferencia con reintentos?
- 🔗 **Se estudia junto con:** Hash, SHA-256, Trozo, Reenvío.

📘 **Dónde se aprende** (4 clases): [B96-C22 · Transferencia de datos entre estación y centro de datos](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md); [B110-C04 · Priorización y decisiones bajo emergencia](../programa/clases/B110/B110-C04-priorizacion-y-decisiones-bajo-emergencia/CLASE.md); [B123-C03 · Mecanismos de reclamación entre Estados](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md); [B124-C21 · Acuerdos de nivel de servicio para productos de datos](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md).

### Plazo comprometido

- El plazo comprometido `T₀` es la fecha pactada con el cliente.

💡 **Cómo se explica en la clase [B125-C05](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md):**
- El ejemplo conductor es sintético: un trámite con media de 45 días y un plazo comprometido de 60 días cuesta, en promedio, `21 826` u.m. de penalizaciones.
- Calcular la demora esperada de un trámite exponencial sobre un plazo comprometido: `E[max(0, T − T₀)] = μ e^(−T₀/μ)`.
- 🎯 **Por qué importa:** La tecnología espacial está sujeta a controles de exportación que condicionan el negocio, y las alianzas de la clase anterior chocan con ellos; ninguna clase los trata. La decisión central: ¿qué ruta de exportación debe esperar un producto o una transferencia de tecnología y cuánto cuesta, en promedio, esperar la licencia?
- 🔗 **Se estudia junto con:** exportación, doble uso, transferencia intangible, licencia.

📘 **Dónde se aprende** (1 clase): [B125-C05 · Control de exportaciones y transferencia de tecnología](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md).

### Plazo de entrega

- El plazo de entrega `L` es el tiempo hasta recibir.

💡 **Cómo se explica en la clase [B104-C21](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md):**
- Un consumible sintético con consumo medio de 12 kg/d y desviación de 3 kg/d, plazo de entrega de 14 días y pedidos de 300 kg.
- Simular un inventario con consumo variable y plazo de entrega.
- 🎯 **Por qué importa:** Quedarse sin un consumible a bordo no se arregla enviando a alguien a comprarlo. La decisión central: ¿con qué punto de reorden se pide para que el faltante sea raro, y cuánto volumen cuesta guardar lo pedido?
- 🔗 **Se estudia junto con:** punto de reorden, existencias de seguridad, estiba, empaquetado en bolsas.

📘 **Dónde se aprende** (1 clase): [B104-C21 · Inventario, logística y estiba a bordo](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md).

### Plazo de recuperación

- El plazo de recuperación son los meses de margen necesarios para devolver el CAC.

💡 **Cómo se explica en la clase [B126-C04](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md):**
- Por mes: margen y plazo de recuperación.
- Ninguna cifra ni definición de esta clase viene de una fuente consultada: CAC, LTV y plazo de recuperación son métricas de uso común en empresas de suscripción, pero no se consultaron en una fuente primaria; se verifican por dos vías de cálculo (serie y simulación).
- 🎯 **Por qué importa:** Un negocio espacial debe medir cuánto cuesta ganar un cliente; el catálogo no lo trata. La decisión central: ¿vale la pena el gasto de captación, dado cuánto tiempo se queda el cliente y cuánto margen deja?
- 🔗 **Se estudia junto con:** CAC, ARPA, margen bruto, abandono.

📘 **Dónde se aprende** (1 clase): [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### Plazo de recuperación descontado

- El plazo de recuperación descontado es el primer año en que el VPN acumulado es positivo.

💡 **Cómo se explica en la clase [B126-C05](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md):**
- Calcular el plazo de recuperación descontado.
- 🎯 **Por qué importa:** [B124-C12](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) evalúa retorno científico, no viabilidad económica. La decisión central: ¿vale hoy más lo que el negocio devolverá que lo que cuesta, y cuánto pueden equivocarse los supuestos antes de que deje de valer?
- 🔗 **Se estudia junto con:** VPN, TIR, tasa real, nominal.

📘 **Dónde se aprende** (1 clase): [B126-C05 · Evaluación de viabilidad económica de un negocio espacial](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md).

### Plazo duro

- El plazo duro no admite incumplimiento; el blando lo tolera con degradación.

💡 **Contexto en la clase [B88-C05](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md):**
- 🎯 **Por qué importa:** En una nave, una tarea de control que llega tarde puede ser tan mala como una que da un resultado incorrecto. La decisión central: ¿cada tarea termina siempre antes de su plazo, aun cuando las de mayor prioridad la interrumpen?
- 🔗 **Se estudia junto con:** tiempo de respuesta, blando, hiperperiodo, planificable.

📘 **Dónde se aprende** (1 clase): [B88-C05 · Sistemas de tiempo real](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md).

### Plegado

- El plegado (*forward folding*) es aplicar el modelo y la respuesta para predecir cuentas.
- El plegado a enteros no negativos.

💡 **Cómo se explica en la clase [B27-C22](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md):**
- Con respuesta identidad, el plegado coincide con el cálculo directo a `10⁻⁹`; las columnas de la RMF suman 1;
- Que el plegado y el minimizador recuperan los parámetros; no el comportamiento con ruido.
- 🎯 **Por qué importa:** Ajustar un espectro «de fotones» directamente a las cuentas da resultados engañosos; hay que plegar el modelo con la respuesta y usar la estadística correcta para conteos pequeños. La decisión central: ¿qué parámetros recupera cada estadística y con qué sesgo cuando las cuentas son pocas?
- 🔗 **Se estudia junto con:** ARF, RMF, estadística de Cash, χ² con varianza igual a las cuentas.

📘 **Dónde se aprende** (2 clases): [B27-C22 · Análisis espectral de rayos X y gamma: ajuste con respuesta instrumental](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md); [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md).

### PLSS

- El PLSS (*portable life support system*) es la mochila del traje.

💡 **Cómo se explica en la clase [B108-C01](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md):**
- En la prueba PLSS 1.0 la inyección de CO₂ se ajustó entre 28 y 280 g/h, el agua de vapor entre 35 y 89 g/h, la fuga del traje entre 2,1 y 4,2 g/h y el rechazo de diseño del evaporador fue 810 W.
- El perfil es ilustrativo; las potencias 469 W y 700 W son las de las pruebas PLSS 1.0.
- 🎯 **Por qué importa:** B106-C09 trata el soporte vital de hábitat; el del traje no tiene clase. La decisión central: ¿cuánto oxígeno, cuánto calor a rechazar y cuánto CO₂ genera una EVA con un perfil de esfuerzo dado, y qué margen deja el sistema?
- 🔗 **Se estudia junto con:** oxígeno, ventilación, térmico, cociente respiratorio.

📘 **Dónde se aprende** (1 clase): [B108-C01 · Sistemas portátiles de soporte vital (PLSS)](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md).

### Plutino

- Un plutino es un objeto en 3:2 con Neptuno; esta clase no usa su catálogo.

💡 **Cómo se explica en la clase [B52-C15](../programa/clases/B52/B52-C15-cinturon-de-kuiper/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. Transferencia. Un colega usa el cálculo para afirmar cuántos plutinos hay.
- 🎯 **Por qué importa:** Las resonancias con Neptuno protegen a cuerpos cuyos perihelios cruzan su órbita, y la temperatura fija qué hielos sobreviven. La decisión central: ¿en qué semiejes están las resonancias exteriores y qué temperatura tiene el cinturón?
- 🔗 **Se estudia junto con:** resonancia exterior p:q, temperatura de equilibrio, albedo de Bond.

📘 **Dónde se aprende** (1 clase): [B52-C15 · Cinturón de Kuiper](../programa/clases/B52/B52-C15-cinturon-de-kuiper/CLASE.md).

### PnP

- La pose `(R, t)` cumple `p_cam = R p_obj + t`. PnP es estimar la pose a partir de correspondencias 2D–3D.

💡 **Contexto en la clase [B103-C07](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md):**
- 🎯 **Por qué importa:** A 8 m un marcador de 10 cm mide 10 px y su pose es casi indeterminada; a 1 m, el error de profundidad es de unos 3 mm. La decisión central: ¿hasta qué distancia es fiable la pose estimada con un objeto de cierto tamaño, y cuándo hay que dudar de ella?
- 🔗 **Se estudia junto con:** pose, PnP plano, radio cuadrático medio, vuelco.

📘 **Dónde se aprende** (1 clase): [B103-C07 · Estimación de pose de objetos y objetivos por visión](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md).

### PnP plano

- El PnP plano usa puntos coplanares y una homografía.

💡 **Cómo se explica en la clase [B103-C07](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md):**
- El método parte de una sola solución (la de la homografía) y no explora la alternativa; un sistema real calcula ambas o usa un objeto no plano.
- O["puntos del objeto<br/>(3x3, plano)"] --> H["homografía<br/>DLT"]
- 🎯 **Por qué importa:** A 8 m un marcador de 10 cm mide 10 px y su pose es casi indeterminada; a 1 m, el error de profundidad es de unos 3 mm. La decisión central: ¿hasta qué distancia es fiable la pose estimada con un objeto de cierto tamaño, y cuándo hay que dudar de ella?
- 🔗 **Se estudia junto con:** pose, PnP, radio cuadrático medio, vuelco.

📘 **Dónde se aprende** (1 clase): [B103-C07 · Estimación de pose de objetos y objetivos por visión](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md).

### Población estelar

- Una población estelar es un conjunto de estrellas con propiedades comunes (edad, composición, cinemática).

💡 **Cómo se explica en la clase [B25-C07](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md):**
- Definir población estelar, órbita circular, epiciclo, frecuencia epicíclica y constantes de Oort.
- python programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/epiciclos_e_imf.py
- 🎯 **Por qué importa:** Las estrellas de una galaxia no giran en círculos perfectos: oscilan alrededor de una órbita circular, y su agitación revela la edad y la historia de la población. Además, no nacen todas con la misma masa: la función de masa inicial fija cuántas hay de cada tipo y cuánta luz y metales producirán.
- 🔗 **Se estudia junto con:** órbita circular, epiciclo, radio guía, frecuencia epicíclica.

📘 **Dónde se aprende** (1 clase): [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### Población mixta

- Una población mixta combina grupos con pesos.

💡 **Contexto en la clase [B109-C06](../programa/clases/B109/B109-C06-antropometria-y-dimensionamiento-para-tripulacion/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR H["Hombres:<br/>media y sd"] --> M["Mezcla 50/50"] W["Mujeres:<br/>media y sd"] --> M M --> P["Percentiles<br/>P1 ..
- 🎯 **Por qué importa:** Si se dimensiona para la media, la mitad de las personas no cabe o no alcanza. La decisión central: ¿qué percentil de qué población usar para cada dimensión?
- 🔗 **Se estudia junto con:** percentil, antropometría, holgura, alcance.

📘 **Dónde se aprende** (1 clase): [B109-C06 · Antropometría y dimensionamiento para tripulación](../programa/clases/B109/B109-C06-antropometria-y-dimensionamiento-para-tripulacion/CLASE.md).

### Población resuelta

- Una población resuelta es aquella cuyas estrellas se miden individualmente.

💡 **Cómo se explica en la clase [B38-C04](../programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/CLASE.md):**
- python programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/sfh.py
- 🎯 **Por qué importa:** Los conteos de estrellas son una suma sobre edades y la inversión amplifica el ruido. La decisión central: ¿con qué resolución en edad se puede recuperar la historia con un número dado de estrellas?
- 🔗 **Se estudia junto con:** historia de formación estelar, vida en la secuencia principal, inversión, Richardson–Lucy.

📘 **Dónde se aprende** (1 clase): [B38-C04 · Historia de formación estelar a partir de poblaciones resueltas](../programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/CLASE.md).

### Pobre

- Una mezcla rica tiene exceso de combustible; una pobre, de oxidante.

💡 **Cómo se explica en la clase [B78-C05](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md):**
- Del lado rico la masa molar baja y ayuda; del pobre sube y perjudica.
- Descripción larga: el escape sube hasta el punto estequiométrico y cae después; la caída del lado pobre es mayor que la mejora del lado rico en este modelo.
- 🎯 **Por qué importa:** Un motor puede quemar mezclas con exceso de combustible o de oxidante. La decisión central: ¿qué `O/F` maximiza el escape en un modelo sin disociación y por qué los motores reales operan en otro punto?
- 🔗 **Se estudia junto con:** bipropelente, relación O/F, estequiométrica, rica.

📘 **Dónde se aprende** (1 clase): [B78-C05 · Propulsión bipropelente conceptual](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md).

### POD

- El POD es la fracción de eventos detectados, el FAR la de alertas falsas y el CSI la de aciertos sobre todos los casos relevantes.
- La POD es `P(detectar | a)`.
- El POD, el FAR y el Heidke.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- *Descripción textual:* las medidas se convierten en escalas G, S y R; la regla y lo observado forman la tabla de contingencia, de la que salen POD, FAR y Heidke.
- Calcular POD, FAR, CSI y la puntuación de Heidke por dos fórmulas.
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?
- 🔗 **Se estudia junto con:** escala, acierto, falsa alarma, fallo.

📘 **Dónde se aprende** (3 clases): [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B33-C13 · Pronóstico de actividad geomagnética](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md); [B84-C19 · Inspección no destructiva](../programa/clases/B84/B84-C19-inspeccion-no-destructiva/CLASE.md).

### Poder

- El poder es su capacidad de influir; el interés, cuánto le afecta.

💡 **Cómo se explica en la clase [B83-C02](../programa/clases/B83/B83-C02-partes-interesadas-y-usuarios/CLASE.md):**
- Con `poder×interés` (15, 20, 6, 8, 10, 10) y suma 69, los pesos son 21,7 %, 29,0 %, 8,7 %, 11,6 %, 14,5 % y 14,5 %.
- Solo la agencia financiadora cae en «gestionar de cerca» (poder 5, interés 4): hay 1 parte en esa casilla.
- 🎯 **Por qué importa:** Cuando las necesidades de dos partes chocan (alta resolución frente a bajo costo), alguien debe decidir con criterio. La decisión central: ¿qué necesidades pasan a requisitos primero y cuánto confías en ese orden?
- 🔗 **Se estudia junto con:** parte interesada, interés, matriz poder/interés, peso.

📘 **Dónde se aprende** (1 clase): [B83-C02 · Partes interesadas y usuarios](../programa/clases/B83/B83-C02-partes-interesadas-y-usuarios/CLASE.md).

### Poder de frenado

- El poder de frenado `S = −dE/(ρ dx)`.

💡 **Cómo se explica en la clase [B47-C09](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md):**
- Calcular el poder de frenado de Bethe-Bloch.
- 🎯 **Por qué importa:** Medir ΔE y E permite identificar la partícula. La decisión central: ¿qué espesor de detector y qué energía separan protones de partículas alfa?
- 🔗 **Se estudia junto con:** fórmula de Bethe-Bloch, alcance CSDA, pico de Bragg, telescopio ΔE–E.

📘 **Dónde se aprende** (1 clase): [B47-C09 · Detectores de partículas — Instrumentación y observatorios espaciales](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md).

### Poder de frenado electrónico

- El poder de frenado electrónico `Se` es la energía depositada por unidad de recorrido (aquí, eV por `10¹⁵` moléculas cm⁻²).

💡 **Cómo se explica en la clase [B68-C03](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md):**
- Calcular el rendimiento de pulverización de una película gruesa de CO, CO₂ o H₂O con el poder de frenado electrónico.
- 🎯 **Por qué importa:** Un hielo en una nube densa recibe poca luz ultravioleta externa, pero sigue recibiendo partículas energéticas y fotones secundarios. Esas dosis lentas transforman la composición del hielo durante millones de años.
- 🔗 **Se estudia junto con:** radiación ionizante, fotoquímica, química de radiación, pulverización.

📘 **Dónde se aprende** (1 clase): [B68-C03 · Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md).

### Poder de resolución

- El poder de resolución de un prisma es `R = b|dn/dλ|` con `b` la base.
- El poder de resolución `R = λ/δλ = mN`.

💡 **Contexto en la clase [B45-C04](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md):**
- **Idea central (modelo mental):** Como una fila de remeros: las palas sincronizadas empujan más fuerte en una sola dirección que depende de la longitud de onda y del ritmo.
- 🎯 **Por qué importa:** La red es el elemento dispersor de casi todos los espectrógrafos. La decisión central: ¿en qué ángulo sale cada longitud de onda y qué resolución se obtiene?
- 🔗 **Se estudia junto con:** ecuación de la red, orden, dispersión angular, Littrow.

📘 **Dónde se aprende** (2 clases): [B45-C04 · Redes de difracción](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md); [B45-C05 · Prismas y dispersión](../programa/clases/B45/B45-C05-prismas-y-dispersion/CLASE.md).

### Poder de voto

- El poder de voto es la fracción de los votos totales que controla un grupo.

💡 **Cómo se explica en la clase [B125-C03](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md):**
- Si una fracción `b` de las acciones es Clase B con `k` votos y el resto (`1 − b`) tiene un voto: `poder = k b / (k b + 1 − b)`.
- *Descripción textual:* la fracción de acciones con `k` votos se compara con el resto de las acciones; el cociente da el poder de voto y, despejando, la participación mínima para controlar.
- ⚠️ **Error frecuente:** Confundir poder de voto con participación económica. Se corrige con 8.2 y el ejercicio 9.
- 🎯 **Por qué importa:** Las decisiones de una empresa se estructuran en su gobierno y, en el espacio, el capital intensivo hace que quien controla la votación controle el rumbo de misiones de años; ninguna clase lo trata.
- 🔗 **Se estudia junto con:** clase de acciones, consejo, cuota, índice de Banzhaf.

📘 **Dónde se aprende** (1 clase): [B125-C03 · Gobierno corporativo de una empresa espacial](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md).

### Poder separador

- El poder separador (de Rayleigh) es el ángulo mínimo entre dos puntos que el telescopio, perfecto, puede distinguir: `θ = 1,22 λ/D`.

💡 **Cómo se explica en la clase [B08-C14](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md):**
- El poder separador teórico es `θ = 1,22 λ/D` (ecuación de la teoría de la difracción; la desarrolla B42).
- Del reflector de 114 mm al Dobson de 200 mm: la luz recogida crece `(200/114)² = 3,08` veces (1,22 mag de ganancia: `5 log₁₀(200/114) = 1,22`), y el poder separador mejora de 1,21″ a 0,69″ (el límite teórico lunar pasa de 2,1 a 1,2 km).
- 🎯 **Por qué importa:** Un telescopio de juguete anuncia «600×» y decepciona. La pregunta motivadora: ¿qué telescopio me conviene y qué podré ver con él?
- 🔗 **Se estudia junto con:** refractor, reflector, Dobson, apertura.

📘 **Dónde se aprende** (1 clase): [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md).

### Poiseuille

- El flujo de Couette lo arrastra una placa; el de Poiseuille lo impulsa un gradiente de presión.
- Reserva: agua almacenada para operar sin reciclaje. Poiseuille: caída de presión laminar.

💡 **Cómo se explica en la clase [B79-C03](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md):**
- Paso 2 · Término de Poiseuille. `2000 × 0,002 × 0,008/(2 × 0,05) = 0,32 m/s`.
- Obtener el perfil de Couette–Poiseuille analítico.
- 🎯 **Por qué importa:** Casi todo flujo de ingeniería tiene paredes, y en ellas la viscosidad impone velocidad cero. Sin Navier–Stokes no hay arrastre ni fricción ni calentamiento por pared.
- 🔗 **Se estudia junto con:** ecuación de Navier–Stokes, viscosidad cinemática, Couette, tensión viscosa.

📘 **Dónde se aprende** (2 clases): [B79-C03 · Ecuaciones de Navier-Stokes](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md); [B106-C29 · Almacenamiento y distribución de agua potable en hábitats](../programa/clases/B106/B106-C29-almacenamiento-y-distribucion-de-agua-potable-en-habitats/CLASE.md).

### Poisson compuesto

- El Poisson compuesto combina una frecuencia de Poisson con una severidad.

💡 **Cómo se explica en la clase [B127-C05](../programa/clases/B127/B127-C05-evaluacion-actuarial-basica-del-riesgo-espacial/CLASE.md):**
- *Descripción textual:* una historia da la frecuencia estimada; con la severidad forma la pérdida agregada de Poisson compuesto, cuya media y varianza tienen fórmula cerrada; de ellas sale la prima y una simulación lo comprueba.
- La independencia entre siniestros; la correlación engorda la cola de `S` y el modelo de Poisson compuesto la subestima.
- 🎯 **Por qué importa:** Estimar primas y pérdidas requiere nociones actuariales; B12 trata estadística sin su aplicación a seguros.
- 🔗 **Se estudia junto con:** frecuencia, severidad, exposición, pérdida agregada.

📘 **Dónde se aprende** (1 clase): [B127-C05 · Evaluación actuarial básica del riesgo espacial](../programa/clases/B127/B127-C05-evaluacion-actuarial-basica-del-riesgo-espacial/CLASE.md).

### Poisson–Gamma

- Un prior es conjugado si la posterior pertenece a su misma familia: Beta–Binomial (prior `Beta(a,b)`, `s` éxitos en `n` ensayos → `Beta(a+s, b+n−s)`) y Poisson–Gamma (prior `Gamma(α,β)` con forma `α` y tasa `β`, conteos con suma `S` en `n` intervalos → `Gamma(α+S, β+n)`).

💡 **Cómo se explica en la clase [B12-C12](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md):**
- Paso 1 · Modelo y prior. Conteos Poisson; prior `Gamma(8; 2)` de pruebas en tierra.
- Calcular la posterior en los modelos Beta–Binomial y Poisson–Gamma.
- 🎯 **Por qué importa:** Una misión rara vez parte de cero: hay pruebas en tierra, misiones anteriores y física conocida. Y a menudo el dato es escaso (diez intervalos, treinta pruebas).
- 🔗 **Se estudia junto con:** teorema de Bayes, prior, verosimilitud, posterior.

📘 **Dónde se aprende** (1 clase): [B12-C12 · Inferencia bayesiana](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md).

### Polar

- Una molécula es polar si la suma de esos vectores no es cero.

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- En el CO₂ lineal, los dos vectores se anulan: molécula no polar.
- En el agua angular con 104,48°, la suma tiene módulo `2 cos(52,24°) = 1,2247` (en unidades del dipolo de enlace): molécula polar.
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).
- 🔗 **Se estudia junto con:** dominio de electrones, modelo de repulsión de pares de valencia, geometría electrónica, forma molecular.

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Polar de arrastre

- La polar de arrastre modela `CD = CD₀ + k·CL²`.

💡 **Cómo se explica en la clase [B77-C04](../programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/CLASE.md):**
- Ajustar la polar de arrastre `CD = CD₀ + k·CL²`.
- python programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/polar.py
- 🎯 **Por qué importa:** Un coeficiente se mide en un túnel y se usa en vuelo. La decisión central: ¿cómo se obtienen y se declaran `Cd` y `CL` para que las fuerzas calculadas sean reproducibles y de qué dependen?
- 🔗 **Se estudia junto con:** coeficiente de arrastre, sustentación, eficiencia aerodinámica, número de Mach.

📘 **Dónde se aprende** (1 clase): [B77-C04 · Coeficientes de arrastre y sustentación](../programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/CLASE.md).

### Polarización

- La polarización es la orientación del campo eléctrico.

💡 **Cómo se explica en la clase [B89-C01](../programa/clases/B89/B89-C01-electromagnetismo-aplicado-a-enlaces/CLASE.md):**
- POL["polarizacion"] --> PLF["PLF = cos^2 psi"]
- *Descripción textual:* la frecuencia da la longitud de onda; la potencia, la ganancia y la distancia dan la densidad de flujo; la polarización fija qué fracción capta la antena receptora.
- 🎯 **Por qué importa:** Todo presupuesto de enlace, toda antena y toda banda parten de la misma onda. Confundir longitud de onda con frecuencia, o potencia con densidad de flujo, rompe los cálculos de las clases siguientes.
- 🔗 **Se estudia junto con:** longitud de onda, densidad de flujo de potencia, ganancia, factor de pérdida por polarización.

📘 **Dónde se aprende** (2 clases): [B28-C05 · Ondas gravitacionales](../programa/clases/B28/B28-C05-ondas-gravitacionales/CLASE.md); [B89-C01 · Electromagnetismo aplicado a enlaces](../programa/clases/B89/B89-C01-electromagnetismo-aplicado-a-enlaces/CLASE.md).

### Polarización circular

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B32-C12](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md):**
- **Idea central (modelo mental):** Un campo magnético hace que la cuerda del átomo vibre con dos tonos ligeramente distintos según la polarización; la diferencia entre ambos tonos es el signo del campo.
- 🎯 **Por qué importa:** Medir campos estelares exige saber cuándo el desdoblamiento se resuelve y cuándo basta la polarización. La decisión central: ¿qué campo produce un desdoblamiento comparable al ancho de la línea?
- 🔗 **Se estudia junto con:** efecto Zeeman, factor de Landé efectivo, desdoblamiento, aproximación de campo débil.

📘 **Dónde se aprende** (1 clase): [B32-C12 · Efecto Zeeman y diagnóstico de campos magnéticos estelares](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md).

### Polarización instrumental

- La polarización instrumental suma un `(q_i, u_i)`.

💡 **Cómo se explica en la clase [B45-C16](../programa/clases/B45/B45-C16-polarimetros-astronomicos/CLASE.md):**
- Con una polarización instrumental sumada de `(+0,005; −0,002)` se mide `q = 0,03498`, `u = -0,01201`; tras restar el instrumento, `q = 0,02998` y `u = -0,01001`, con ángulo `-9,229°`.
- Para modular sin mover el detector y reducir la polarización instrumental.
- ⚠️ **Error frecuente:** Olvidar la polarización instrumental. Se corrige con 8.1.
- 🎯 **Por qué importa:** La polarización medida es siempre positiva y por eso sesgada hacia arriba cuando el ruido es comparable a la señal. La decisión central: ¿cómo se miden Q y U y cómo se corrige el sesgo?
- 🔗 **Se estudia junto con:** placa de media onda, analizador fijo, demodulación, sesgo.

📘 **Dónde se aprende** (1 clase): [B45-C16 · Polarímetros astronómicos](../programa/clases/B45/B45-C16-polarimetros-astronomicos/CLASE.md).

### Polarización lineal

- La polarización lineal `P = Q + iU`, con ángulo `χ = ½ arg P`.

💡 **Contexto en la clase [B46-C13](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md):**
- **Idea central (modelo mental):** El ángulo de la veleta depende del cuadrado de la longitud de onda; mirando a muchas longitudes, se ve cuántas vueltas ha dado.
- 🎯 **Por qué importa:** El ángulo de polarización gira con `λ²`, y hay que medirlo en varias frecuencias para saber cuánto. La decisión central: ¿cómo se obtiene la medida de rotación sin ambigüedad de `nπ`?
- 🔗 **Se estudia junto con:** parámetros de Stokes, rotación de Faraday, síntesis de RM, función de dispersión de Faraday.

📘 **Dónde se aprende** (1 clase): [B46-C13 · Polarimetría de radio](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md).

### Polarizador

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C08](../programa/clases/B42/B42-C08-polarizacion-de-la-luz/CLASE.md):**
- Con un polarizador a 30° de luz lineal horizontal pasa el `0,7500`; una lámina de cuarto de onda a 45° la vuelve circular (`S₃ = −1`) y una mezcla con 60 % polarizado da un grado de polarización muestral de `0,5941`.
- Aplicar polarizadores y láminas con matrices de Jones.
- 🎯 **Por qué importa:** La polarización cambia cuánto flujo pasa por un instrumento (espejos, divisores, filtros) y revela procesos físicos de la fuente. La decisión central: ¿cómo se describe y se mide un estado de polarización y cómo lo transforma un elemento óptico?
- 🔗 **Se estudia junto con:** vector de Jones, parámetros de Stokes, lámina de retardo, ley de Malus.

📘 **Dónde se aprende** (1 clase): [B42-C08 · Polarización de la luz](../programa/clases/B42/B42-C08-polarizacion-de-la-luz/CLASE.md).

### Polhodia

- La polhodia es la curva que describe `ω` en el cuerpo.

💡 **Cómo se explica en la clase [B87-C01](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md):**
- La intersección de la esfera `|Iω| = H` con el elipsoide `ω·Iω = 2T`: una curva cerrada llamada polhodia.
- 🎯 **Por qué importa:** Un diseñador de actitud necesita saber qué hace el vehículo cuando nadie lo controla: ¿cuánto vale el momento angular, cómo se mueve el eje de giro y cuándo un giro aparentemente tranquilo se desestabiliza?
- 🔗 **Se estudia junto con:** tensor de inercia, ejes principales, momento angular, energía de rotación.

📘 **Dónde se aprende** (1 clase): [B87-C01 · Dinámica de cuerpo rígido](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md).

### Polinomio

- Un polinomio en la variable `x` es una suma de términos `aₖ xᵏ`, con `k` entero no negativo.

💡 **Cómo se explica en la clase [B04-C01](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md):**
- Regla de las raíces racionales. Si el polinomio tiene coeficientes enteros y una raíz `p/q` en fracción irreducible, `p` divide al término independiente y `q` al coeficiente principal.
- Su límite: en un polinomio la fórmula crece sin freno cuando `t` es grande, y la naturaleza no; por eso toda fórmula publicada trae un intervalo de validez.
- 🎯 **Por qué importa:** Cuando un observatorio publica dónde está inclinado el eje de la Tierra, no da un solo número: da una *fórmula* para cada fecha, porque ese eje se mueve lentamente. Esa fórmula es un polinomio.
- 🔗 **Se estudia junto con:** coeficientes, término independiente, grado, raíz.

📘 **Dónde se aprende** (1 clase): [B04-C01 · Polinomios y factorización](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md).

### Polinomio característico

- Los autovalores son las raíces de la ecuación característica `det(A − λI) = 0` (S1, 1.2.71); el polinomio correspondiente es el polinomio característico.
- El polinomio característico de un lazo cerrado es el numerador de `1 + L(s)`; sus raíces son los polos del lazo cerrado.

💡 **Cómo se explica en la clase [B10-C08](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md):**
- Para matrices grandes nunca se usa el polinomio característico: es inestable.
- ⚠️ **Error frecuente:** Usar el polinomio característico para matrices grandes. Se corrige en la sección 14.
- 🎯 **Por qué importa:** Un satélite que rota libremente no gira igual alrededor de cualquier eje: tiene tres ejes especiales —los ejes principales de inercia— en los que la rotación es simple. Conocerlos permite diseñar su estabilización, decidir dónde colocar instrumentos sensibles al giro y entender por qué ciertos giros se desestabilizan.
- 🔗 **Se estudia junto con:** autovector, autovalor, ecuación característica, espectro.

📘 **Dónde se aprende** (2 clases): [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B16-C08 · Criterio de Routh-Hurwitz](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md).

### Polinomio de Lagrange

- Dados `n + 1` nodos distintos `x_k` con valores `f_k`, el polinomio de Lagrange `P_n` es el único polinomio de grado `≤ n` con `P_n(x_k) = f_k` (S1, §3.3(i), ec. 3.3.1).

💡 **Cómo se explica en la clase [B11-C18](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md):**
- El polinomio de Lagrange pasa por *todos* los puntos, incluido el ruido.
- A["Tabla (xₖ, fₖ)"] --> B["Polinomio de Lagrange Pₙ"]
- 🎯 **Por qué importa:** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.
- 🔗 **Se estudia junto con:** polinomio nodal, error, Interpolar, extrapolar.

📘 **Dónde se aprende** (1 clase): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md).

### Polinomio de Legendre

- El polinomio de Legendre `P_n(s)` con `s = sin φ` da la forma del término.

💡 **Cómo se explica en la clase [B72-C02](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md):**
- *Descripción textual:* los parámetros y los polinomios de Legendre construyen el potencial; su gradiente es la aceleración, que se verifica numéricamente.
- 🎯 **Por qué importa:** Sin un potencial no hay perturbación gravitatoria que calcular, y los números de la bibliografía (J2, J3, J4) dependen de un convenio de signos y de un radio de referencia. La decisión central: ¿qué términos del potencial incluir y con qué radio y convenio, para que J2 signifique lo mismo en tu código y en la fuente?
- 🔗 **Se estudia junto con:** armónico zonal, J2, convenio de signos, gradiente.

📘 **Dónde se aprende** (1 clase): [B72-C02 · Potencial gravitatorio no esférico](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md).

### Polinomio de Taylor

- El polinomio de Taylor de grado `n` de `f` en torno a `a` es `Σ_{k=0}^{n} f^{(k)}(a) (x − a)ᵏ/k!`.

💡 **Cómo se explica en la clase [B09-C14](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md):**
- Un polinomio de Taylor se usa cerca del centro.
- Escribir el polinomio de Taylor de una función en torno a un punto.
- 🎯 **Por qué importa:** Un cálculo orbital rápido usa `g(h) = g₀(1 − 2h/R)` para una altitud baja; uno más exigente necesita el siguiente término. Sin una cota del error no se sabe cuál usar.
- 🔗 **Se estudia junto con:** serie de Maclaurin, resto, Lagrange, radio de convergencia.

📘 **Dónde se aprende** (1 clase): [B09-C14 · Series y aproximaciones](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md).

### Polinomio generador

- El polinomio generador es `g(x) = ∏ (x − α^(11 j))` para `j = 128 − E, …, 127 + E`.

💡 **Cómo se explica en la clase [B94-C01](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md):**
- Construir GF(2⁸) a partir de un polinomio generador de campo y comprobar que `α` es primitivo.
- 🎯 **Por qué importa:** Un enlace profundo opera con relaciones señal-ruido bajas y no puede reenviar cada trama. La decisión central: ¿cuántos símbolos erróneos tolera una palabra de código, cuánta redundancia cuesta y qué ocurre cuando se supera esa capacidad?
- 🔗 **Se estudia junto con:** código RS(n, k), capacidad, síndrome, localizador de errores.

📘 **Dónde se aprende** (1 clase): [B94-C01 · Códigos Reed-Solomon y LDPC](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md).

### Polinomio nodal

- El polinomio nodal es `ω(x) = Π (x − x_k)`.

💡 **Cómo se explica en la clase [B11-C18](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md):**
- *Descripción textual:* de la tabla se construye el polinomio; si el punto está dentro del intervalo, el error está dado por la derivada de orden `n + 1` y el polinomio nodal; si está fuera, `|ω|` crece muy rápido; con nodos equiespaciados y grado alto aparece Runge, y con Chebyshev el error decrece.
- 🎯 **Por qué importa:** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.
- 🔗 **Se estudia junto con:** polinomio de Lagrange, error, Interpolar, extrapolar.

📘 **Dónde se aprende** (1 clase): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md).

### Polinomios de Legendre

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B40-C07](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md):**
- Construir `C(θ)` desde `C_ℓ` con polinomios de Legendre.
- 🎯 **Por qué importa:** Los picos acústicos fijan la geometría y el contenido del universo. La decisión central: ¿dónde caen los picos (`ℓ_A = π/θ*`) y cómo se pasa del espectro a la correlación y de vuelta?
- 🔗 **Se estudia junto con:** espectro angular, horizonte sonoro, distancia comóvil, escala acústica.

📘 **Dónde se aprende** (1 clase): [B40-C07 · Espectro angular de potencias del CMB](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md).

### Polinomios de Shomate

- Los polinomios de Shomate son `c_p = A + B t + C t² + D t³ + E/t²` con `t = T/1000` y coeficientes por rango de temperatura.

💡 **Cómo se explica en la clase [B79-C14](../programa/clases/B79/B79-C14-propiedades-de-gases-calientes/CLASE.md):**
- Evaluar `c_p(T)` y `H(T) − H₂₉₈` con un polinomio de Shomate.
- 🎯 **Por qué importa:** B06-C09 trata gases en general; aquí hacen falta propiedades termofísicas a alta temperatura con fuente. Sin ellas, las toberas y las turbinas se dimensionan con un `γ` que no existe a 2000–3000 K.
- 🔗 **Se estudia junto con:** entalpía sensible, mezcla ideal, disociación.

📘 **Dónde se aprende** (1 clase): [B79-C14 · Propiedades de gases calientes](../programa/clases/B79/B79-C14-propiedades-de-gases-calientes/CLASE.md).

### Política de acceso

- La política de acceso dice quién ve qué.

💡 **Cómo se explica en la clase [B119-C35](../programa/clases/B119/B119-C35-seguridad-y-gobernanza-de-datos-espaciales/CLASE.md):**
- El ejemplo conductor: 5000 registros sintéticos de acceso a estaciones terrenas, con una característica binaria («fuera de horario») de prevalencia 0,08, y una política de 3 roles por 3 niveles.
- La evidencia es la política de acceso con compromiso privacidad–error del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** B124-C13 trata ética de datos de investigación; los datos espaciales requieren políticas de acceso y seguridad específicas. Esta clase mide el compromiso entre transparencia y protección.
- 🔗 **Se estudia junto con:** nivel, privacidad diferencial, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B119-C35 · Seguridad y gobernanza de datos espaciales](../programa/clases/B119/B119-C35-seguridad-y-gobernanza-de-datos-espaciales/CLASE.md).

### Política de alerta

- La política de alerta compara el límite inferior del intervalo con un horizonte.

💡 **Cómo se explica en la clase [B88-C44](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md):**
- La política «alertar si el límite inferior es menor de 100 días» activa la alerta (`86,5`).
- Paso 4 · Política. Límite inferior `86,5 < 100`: alerta.
- 🎯 **Por qué importa:** Detectar una falla (C12) llega tarde para planificar; anticiparla da tiempo para actuar. La decisión central: ¿cuándo cruzará el umbral y con qué incertidumbre, para decidir si alertar?
- 🔗 **Se estudia junto con:** RUL, ajuste, cruce, remuestreo.

📘 **Dónde se aprende** (1 clase): [B88-C44 · Mantenimiento predictivo y pronóstico de salud de sistemas](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md).

### Política de modos

- La política de modos decide cuándo cambiar según el SOC.

💡 **Cómo se explica en la clase [B86-C21](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md):**
- Con una generación de `125 W` en luz, el modo nominal pierde `16,4 Wh` por órbita y la batería sin política se agota en la órbita `13` (día `0,80`).
- Implementar una política de cambio de modo por umbrales de SOC con histéresis.
- 🎯 **Por qué importa:** Cuando la energía escasea, apagar la carga útil a tiempo mantiene viva la nave. Un umbral único hace oscilar al sistema entre modos; la histéresis lo evita.
- 🔗 **Se estudia junto con:** modo de operación, modo seguro, histéresis, transición.

📘 **Dónde se aprende** (1 clase): [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md).

### Política nacional

- La política nacional orienta sin crear derechos y obligaciones por sí sola.

💡 **Cómo se explica en la clase [B121-C04](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md):**
- Es un decreto del Ministerio de Defensa Nacional (Subsecretaría de Aviación) que crea un comité asesor: propone política, coordina y debe elaborar un proyecto de ley.
- Una Política Nacional Espacial figura como aprobada en fuentes de prensa y de búsqueda; su decreto y fecha no se verificaron (nivel 1).
- 🎯 **Por qué importa:** Un marco nacional se conoce por sus instrumentos, y cada instrumento debe leerse en su texto vigente. La decisión central: ¿qué funciones regulatorias tienen un instrumento chileno identificado y con qué nivel de evidencia?
- 🔗 **Se estudia junto con:** nivel de evidencia, función regulatoria, instrumento, traducción no oficial.

📘 **Dónde se aprende** (1 clase): [B121-C04 · Marco legal espacial en Chile](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md).

### Politrópico

- Un proceso politrópico sigue `p v^n = constante`, con `n` entre 1 (isotermo) y `γ` (isentrópico).

💡 **Cómo se explica en la clase [B79-C12](../programa/clases/B79/B79-C12-procesos-adiabaticos-e-isentropicos/CLASE.md):**
- Comprimir aire de `300 K` y `100 kPa` a un décimo de su volumen da `753,57 K` y `2511,9 kPa` con `325,49 kJ/kg` si es isentrópico, `533,48 K` y `1778,3 kPa` con `268,09 kJ/kg` si es politrópico con `n = 1,25` y `300 K` y `1000 kPa` con `198,29 kJ/kg` si es isotermo.
- Comparar isotermo, politrópico e isentrópico.
- 🎯 **Por qué importa:** Las relaciones isentrópicas son el núcleo del análisis de toberas, compresores y turbinas; el tronco no las trata. Aquí se obtienen desde primeros principios y se ve cuándo valen.
- 🔗 **Se estudia junto con:** isentrópico, relación de volúmenes, trabajo de compresión.

📘 **Dónde se aprende** (1 clase): [B79-C12 · Procesos adiabáticos e isentrópicos](../programa/clases/B79/B79-C12-procesos-adiabaticos-e-isentropicos/CLASE.md).

### Politropo

- El politropo `P = Kρ^Γ` con `Γ = 2` es el caso `n = 1`.
- El politropo de índice `n` cumple `P = Kρ^{1+1/n}`; reduce el problema a Lane–Emden.
- Un politropo satisface `P = Kρ^(1+1/n)`.

💡 **Cómo se explica en la clase [B24-C20](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md):**
- El politropo da `0,47` de `ρ_c`, `0,50` de `P_c` y `0,75` de `T_c` del modelo solar.
- Un politropo fija una relación entre presión y densidad en toda la estrella.
- ⚠️ **Error frecuente:** Tomar el politropo por un modelo solar. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un modelo de estructura real resuelve cuatro ecuaciones acopladas con física detallada; un politropo sustituye esa física por una sola relación `P ∝ ρ^{1+1/n}` y permite resolver todo con una ecuación. Es el mejor modo de ver qué se obtiene con poco y qué falta.
- 🔗 **Se estudia junto con:** ecuaciones de estructura estelar, modelo estándar de Eddington, escala, densidad central.

📘 **Dónde se aprende** (3 clases): [B24-C20 · Modelo simplificado de estructura estelar](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md); [B27-C03 · Estrellas de neutrones](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md); [B30-C01 · Estructura interna del Sol](../programa/clases/B30/B30-C01-estructura-interna-del-sol/CLASE.md).

### Politropo n = 3

- El politropo `n = 3` (`P = Kρ^{4/3}`) describe un gas degenerado ultrarrelativista.

💡 **Cómo se explica en la clase [B24-C18](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md):**
- Politropo `n = 3` (esta clase): analítico y didáctico.
- El ejemplo conductor es el cálculo del límite de masa: un politropo `n = 3` de electrones degenerados ultrarrelativistas con `μ_e = 2` da `1,456 M☉`.
- 🎯 **Por qué importa:** El destino de una estrella es una enana blanca, una estrella de neutrones o un agujero negro; hay una masa límite que separa los dos primeros destinos. Calcularla muestra cómo la mecánica cuántica (presión de degeneración) sostiene a una estrella cuando ya no hay fusión.
- 🔗 **Se estudia junto con:** enana blanca, estrella de neutrones, agujero negro, presión de degeneración.

📘 **Dónde se aprende** (1 clase): [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md).

### Polo

- Un sistema de coordenadas esféricas se define por un polo (el eje de la latitud), un círculo fundamental (el «ecuador» del sistema, a 90° del polo) y un origen de longitud sobre él.
- El polo es la dirección del eje de rotación.
- Las coordenadas polares `(r, θ)` la dan por la distancia `r` a un origen (el polo) y el ángulo `θ` medido desde un eje polar.

💡 **Cómo se explica en la clase [B04-C10](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md):**
- Su límite: `θ` es periódico (360° es 0°), a diferencia de `x` e `y`, y en el polo `θ` no está definido.
- 🎯 **Por qué importa:** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.
- 🔗 **Se estudia junto con:** coordenadas cartesianas, coordenadas polares, eje polar, anomalía verdadera.

📘 **Dónde se aprende** (3 clases): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md); [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md); [B53-C21 · Rotación y orientación de cuerpos planetarios: polos y meridiano origen](../programa/clases/B53/B53-C21-rotacion-y-orientacion-de-cuerpos-planetarios-polos-y-meridiano-origen/CLASE.md).

### Polo celeste

- El polo celeste es el punto en torno al cual giran las estrellas.

💡 **Cómo se explica en la clase [B01-C11](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md):**
- El eje de rotación apunta a un lugar del cielo, el polo celeste, y todos los astros giran en torno a él.
- R["Rotación de la Tierra: una vuelta en 23,9345 h"] --> E["Estrellas: giran 15,04°/h alrededor del polo celeste"]
- 🎯 **Por qué importa:** Antes de cualquier telescopio, la humanidad dedujo mucho del cielo a simple vista. Que el Sol «salga» y «se ponga» es una observación; que la Tierra gire es una interpretación (C05) que explica además el movimiento de todas las estrellas.
- 🔗 **Se estudia junto con:** horizonte, cénit, meridiano, altura.

📘 **Dónde se aprende** (1 clase): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md).

### Polo celeste sur

- El polo celeste sur es la prolongación del eje de la Tierra hacia el sur y el ecuador celeste es la prolongación del plano ecuatorial.

💡 **Cómo se explica en la clase [B08-C02](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md):**
- Si estás en el polo sur, el polo celeste está sobre tu cabeza (altura 90°), y el horizonte coincide con el ecuador celeste.
- Entre ambos, la altura del polo sur celeste es `|φ|`.
- 🎯 **Por qué importa:** Alguien en Punta Arenas ve girar algunas estrellas sin ponerse jamás; alguien en el valle del Elqui las ve rozar el horizonte, y alguien en el hemisferio norte no las ve nunca. Entender por qué evita comprar un telescopio para un objeto que no sale en tu cielo.
- 🔗 **Se estudia junto con:** esfera celeste, horizonte local, cenit, nadir.

📘 **Dónde se aprende** (1 clase): [B08-C02 · Esfera celeste y horizonte local](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md).

### Polo orbital

- El polo orbital `ĥ` es la dirección de `r × v`.

💡 **Cómo se explica en la clase [B72-C09](../programa/clases/B72/B72-C09-perturbaciones-solares/CLASE.md):**
- *Descripción textual:* el factor `κ`, el polo orbital y la normal del Sol determinan el giro del polo; de él salen las tasas, que se verifican con la integración con el Sol.
- Deducir la precesión del polo orbital `dĥ/dt = κ cosγ (ĥ × ĥ_p)` con `κ = ¾ μ_p/(d³ n)`.
- 🎯 **Por qué importa:** En órbitas altas el Sol y la Luna compiten con J2 y gobiernan la evolución de la inclinación y del nodo. La decisión central: ¿cuánto gira el plano de una órbita por la marea solar y qué fórmula sirve para predecirlo?
- 🔗 **Se estudia junto con:** marea solar, aproximación cuadrupolar, precesión luni-solar.

📘 **Dónde se aprende** (1 clase): [B72-C09 · Perturbaciones solares](../programa/clases/B72/B72-C09-perturbaciones-solares/CLASE.md).

### Polos

- Los polos son los puntos `δ = ±90°`, donde `α` no está definida.
- Sus polos son las raíces del denominador; sus ceros, las del numerador.

💡 **Cómo se explica en la clase [B04-C11](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md):**
- Esas son las fórmulas que se usarán a partir de aquí; el eje `x` apunta a `(α, δ) = (0°, 0°)`, el `y` a `(90°, 0°)` y el `z` al polo celeste norte, que es la convención del catálogo Hipparcos (S2).
- En los polos (`δ = ±90°`) `x = y = 0` y `α` es indeterminada: la convención es dar `α = 0` o dejar la de entrada.
- 🎯 **Por qué importa:** Un catálogo de estrellas da para cada una dos números: dónde está en el cielo. Pero un programa que cruza catálogos, calcula separaciones o apunta un telescopio no trabaja con horas y grados: trabaja con vectores.
- 🔗 **Se estudia junto con:** coordenadas esféricas, ángulo polar, ángulo azimutal, ascensión recta.

📘 **Dónde se aprende** (2 clases): [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md); [B16-C05 · Funciones de transferencia](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md).

### Polvo

- El polvo interestelar son granos sólidos muy pequeños, a menudo cubiertos de hielos.
- El polvo son granos sólidos de tamaño inferior a una micra que absorben y dispersan la luz.
- El regolito es el suelo suelto de la Luna; el polvo es su fracción fina.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Distinguir hielo, mineral, roca y polvo con ejemplos.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).
- 🔗 **Se estudia junto con:** hielo, mineral, olivino, forsterita.

📘 **Dónde se aprende** (4 clases): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md); [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md); [B40-C10 · Emisiones de primer plano galácticas y su separación](../programa/clases/B40/B40-C10-emisiones-de-primer-plano-galacticas-y-su-separacion/CLASE.md); [B109-C04 · Mitigación de polvo lunar en accesos y hábitats](../programa/clases/B109/B109-C04-mitigacion-de-polvo-lunar-en-accesos-y-habitats/CLASE.md).

### Polvo respirable

- Cambios de aire por hora: `3600 Q/V`. Polvo respirable: partículas que llegan al pulmón.

💡 **Cómo se explica en la clase [B106-C23](../programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/CLASE.md):**
- python programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/particulas_y_polvo.py
- 🎯 **Por qué importa:** En 1 g las partículas grandes caen al suelo; en microgravedad no, y en gravedad parcial caen más despacio. La decisión central: ¿qué eficiencia de filtro y qué caudal limpian la cabina en un tiempo dado según la gravedad y el tamaño?
- 🔗 **Se estudia junto con:** Velocidad de Stokes, Aerosol, HEPA, Cambios de aire por hora.

📘 **Dónde se aprende** (1 clase): [B106-C23 · Control de partículas y polvo respirable en cabina](../programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/CLASE.md).

### Ponderación

- La ponderación (apodización) baja los lóbulos y ensancha el haz.

💡 **Contexto en la clase [B49-C04](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md):**
- **Idea central (modelo mental):** Como un coro: si todos cantan en fase se oye fuerte en una dirección; cambiar los retardos orienta el sonido sin mover a nadie.
- 🎯 **Por qué importa:** El arreglo cambia ancho de haz, lóbulos laterales y ganancia según los pesos. La decisión central: ¿qué pesos y qué separación dan el haz y el nivel de lóbulos que se necesitan?
- 🔗 **Se estudia junto con:** factor de arreglo, peso, nulo, lóbulo lateral.

📘 **Dónde se aprende** (1 clase): [B49-C04 · Arreglos de antenas: factor de arreglo y formación de haz](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md).

### Ponderación CIC

- La ponderación CIC reparte la carga entre dos nodos.

💡 **Contexto en la clase [B35-C05](../programa/clases/B35/B35-C05-simulacion-de-plasmas-por-particulas-pic/CLASE.md):**
- **Idea central (modelo mental):** Las partículas son cuentas sobre un hilo que sienten el campo de una malla; la malla se calcula con las cuentas. Si las cuentas son pocas, el campo tiembla.
- 🎯 **Por qué importa:** Un código sin validar produce figuras bonitas y físicas falsas. La decisión central: ¿reproduce el código la frecuencia y la tasa de crecimiento conocidas?
- 🔗 **Se estudia junto con:** macropartícula, salto de rana, ruido de partículas, deriva de energía.

📘 **Dónde se aprende** (1 clase): [B35-C05 · Simulación de plasmas por partículas (PIC)](../programa/clases/B35/B35-C05-simulacion-de-plasmas-por-particulas-pic/CLASE.md).

### Pool

- El pool reparte bloques fijos.

💡 **Cómo se explica en la clase [B88-C29](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md):**
- Si 1 de cada 3 ciclos no libera, tras 100 ciclos quedan 6 bloques libres de 40: el pool se agota en pocos ciclos más; el conteo de bloques vivos detecta la fuga.
- *Descripción textual:* un mismo pedido se atiende buscando un hueco en el montón (con riesgo de fragmentación) o tomando un bloque fijo del pool.
- 🎯 **Por qué importa:** Un montón puede fallar después de horas por fragmentación aunque haya memoria libre; un pool de bloques fijos no. La decisión central: ¿qué esquema de memoria garantiza que una asignación nunca falle en vuelo?
- 🔗 **Se estudia junto con:** regla R3, fragmentación externa, pila máxima.

📘 **Dónde se aprende** (1 clase): [B88-C29 · Gestión de memoria determinista en software de vuelo](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md).

### Por pares

- Una función fija no depende del número de tripulantes; una lineal crece con él; una por pares crece por cada dos tripulantes; una logística crece con tripulantes por días.

💡 **Cómo se explica en la clase [B109-C05](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md):**
- Por pares (`⌈N/2⌉`): ejercicio, higiene y gestión de residuos.
- Paso 2 · Por pares. Con `⌈4/2⌉ = 2`: `(2,09 + 1,04 + 1,04) × 2 = 8,34 m²`.
- 🎯 **Por qué importa:** Si el primer módulo no admite ampliación, crecer obliga a desechar lo construido. La decisión central: ¿qué funciones se duplican con la tripulación, cuáles no, y cómo se añaden módulos sin rediseñar?
- 🔗 **Se estudia junto con:** módulo, fase, crecimiento aditivo, escalabilidad.

📘 **Dónde se aprende** (1 clase): [B109-C05 · Crecimiento modular y escalabilidad de asentamientos](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md).

### Porcentaje

- Un porcentaje es una razón expresada «por cada cien»: `25 % = 25/100 = 0,25`.

💡 **Cómo se explica en la clase [B03-C03](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md):**
- Multiplicar por 100 pasa de razón a porcentaje; dividir entre 100 lo devuelve.
- Paso 3 · porcentaje. `42 200 / 363 300 = 0,1162 → +11,6 %`.
- ⚠️ **Error frecuente:** Confundir punto porcentual con porcentaje. Ejercicio 6.
- 🎯 **Por qué importa:** La Tierra no gira en un círculo: su distancia al Sol varía a lo largo del año. ¿Mucho o poco?
- 🔗 **Se estudia junto con:** base, cambio absoluto, cambio relativo, cambio porcentual.

📘 **Dónde se aprende** (1 clase): [B03-C03 · Porcentajes y escalas comparativas](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md).

### Porcentaje del previo

- El porcentaje del previo normaliza cada prueba.

💡 **Cómo se explica en la clase [B107-C08](../programa/clases/B107/B107-C08-evaluacion-funcional-posterior-al-vuelo/CLASE.md):**
- En R+1 el porcentaje del previo medio es `69,5 %`, `77,3 %` y `62,7 %`, y el compuesto geométrico `69,4 %` (62,0–75,2).
- Normalizar tiempos como porcentaje del valor previo `100·previo/posterior`.
- 🎯 **Por qué importa:** El fragmento de Mulavara et al. (2018) describe una batería con siete pruebas funcionales y 15 medidas fisiológicas para entender el desempeño de tareas tras el vuelo, y Clément et al.
- 🔗 **Se estudia junto con:** R+1, compuesto, Bland–Altman, MDC95.

📘 **Dónde se aprende** (1 clase): [B107-C08 · Evaluación funcional posterior al vuelo](../programa/clases/B107/B107-C08-evaluacion-funcional-posterior-al-vuelo/CLASE.md).

### Porosidad

- La porosidad `φ = 1 − ρ_b/ρ_g` es la fracción de vacío.

💡 **Cómo se explica en la clase [B58-C03](../programa/clases/B58/B58-C03-composicion-de-asteroides/CLASE.md):**
- Con `ρ_g = 3300` la porosidad es `0.421`; con `2700`, `0.293`; con `7500`, `0.745`.
- El resultado depende del material supuesto: sin composición no hay porosidad.
- 🎯 **Por qué importa:** La densidad aparente de un asteroide es casi siempre menor que la de sus rocas: la diferencia es porosidad, y de ella depende cuánta energía hace falta para desviarlo o fragmentarlo (C17). La decisión central: ¿cuánto de lo que parece masa es vacío, y cuánta incertidumbre arrastra la masa?
- 🔗 **Se estudia junto con:** densidad aparente, densidad de grano, cúmulo de escombros, propagación de errores.

📘 **Dónde se aprende** (1 clase): [B58-C03 · Composición de asteroides](../programa/clases/B58/B58-C03-composicion-de-asteroides/CLASE.md).

### Porosidad residual

- La porosidad residual son los huecos que quedan tras compactar.

💡 **Cómo se explica en la clase [B84-C37](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar la porosidad residual. Se corrige con 8.4.
- 🎯 **Por qué importa:** La resistencia de un compuesto cae exponencialmente con la porosidad: pasar de 10 a 25 % de huecos divide la resistencia por 2,4. La decisión central: ¿qué porosidad máxima permite cumplir una resistencia mínima y cuánto ligante hay que transportar?
- 🔗 **Se estudia junto con:** relación de Ryshkewitch, cotas de Voigt y Reuss, intervalo de predicción.

📘 **Dónde se aprende** (1 clase): [B84-C37 · Compuestos y aglomerantes a base de regolito](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md).

### Porro

- Los prismas pueden ser porro (más anchos, a menudo con mejor campo) o de techo (más compactos) (S2).

💡 **Contexto en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- **Idea central (modelo mental):** El objetivo recoge luz; el ocular la concentra en un haz que debe entrar en tu pupila. Si el haz (la pupila de salida) es mayor que tu pupila, parte de la luz se pierde. Si es menor, aprovechas toda.
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?
- 🔗 **Se estudia junto con:** aumento, objetivo, pupila de salida, campo de visión.

📘 **Dónde se aprende** (1 clase): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md).

### Portador del saber

- El portador del saber es la persona o grupo que sostiene el saber en su comunidad.

💡 **Contexto en la clase [B133-C03](../programa/clases/B133/B133-C03-colaboracion-con-comunidades-en-investigacion-y-educacion/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR C["consulta"] --> A["acuerdo"] A --> R["recolección"] R --> V["revisión comunitaria"] V --> P["publicación"] V --> D["devolución"] ``` *Descripción textual:* primero se consulta, luego se acuerda, después se recoge; los resultados vuelven a la comunidad para su revisión, y solo entonces se publican o se devuelven en su forma final.
- 🎯 **Por qué importa:** Los saberes del cielo han sido registrados muchas veces sin que las comunidades decidieran qué, cómo ni para qué. La decisión central: ¿qué debe estar acordado, y en qué orden, antes de recoger, usar o enseñar un saber ajeno?
- 🔗 **Se estudia junto con:** consentimiento libre, previo e informado, principios CARE, devolución de resultados, protocolo.

📘 **Dónde se aprende** (1 clase): [B133-C03 · Colaboración con comunidades en investigación y educación](../programa/clases/B133/B133-C03-colaboracion-con-comunidades-en-investigacion-y-educacion/CLASE.md).

### Pose

- La pose `(R, t)` cumple `p_cam = R p_obj + t`.

💡 **Cómo se explica en la clase [B103-C07](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md):**
- Un solo punto de vista mide mal la profundidad; la pose lateral es precisa.
- H --> P["pose inicial<br/>r1, r2, t + SVD"]
- 🎯 **Por qué importa:** A 8 m un marcador de 10 cm mide 10 px y su pose es casi indeterminada; a 1 m, el error de profundidad es de unos 3 mm. La decisión central: ¿hasta qué distancia es fiable la pose estimada con un objeto de cierto tamaño, y cuándo hay que dudar de ella?
- 🔗 **Se estudia junto con:** PnP, PnP plano, radio cuadrático medio, vuelco.

📘 **Dónde se aprende** (1 clase): [B103-C07 · Estimación de pose de objetos y objetivos por visión](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md).

### Pose rígida

- Una pose rígida es un par `(R, t)`.

💡 **Contexto en la clase [B103-C02](../programa/clases/B103/B103-C02-calibracion-extrinseca-y-registro-multisensor/CLASE.md):**
- 🎯 **Por qué importa:** Un error de 0,02° en la rotación entre una cámara y el brazo de un robot parece nada, pero a 10 m son 3,5 mm de error de posición, y a más distancia crece sin límite. La decisión central: ¿cuántas correspondencias y con qué geometría hacen falta para que la pose entre sensores cumpla un presupuesto de error dado?
- 🔗 **Se estudia junto con:** calibración extrínseca, registro, Kabsch, brazo de palanca.

📘 **Dónde se aprende** (1 clase): [B103-C02 · Calibración extrínseca y registro multisensor](../programa/clases/B103/B103-C02-calibracion-extrinseca-y-registro-multisensor/CLASE.md).

### Poseer

- Comprar un servicio es pagar un precio por un resultado, sin poseer el sistema. Poseer es financiar el sistema y operarlo.

💡 **Cómo se explica en la clase [B124-C02](../programa/clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md):**
- Si `K` es lognormal de mediana 2 000 y `σ = 0,35`, poseer es más barato cuando `K < N(p − c) = 2 450`.
- Que poseer «ahorre» en la mediana no es una garantía: con esta dispersión hay una probabilidad de `28,1%` de que comprar hubiera sido más barato.
- 🎯 **Por qué importa:** Las agencias científicas y las empresas cumplen papeles distintos: la agencia fija objetivos y paga; la empresa ofrece capacidad y asume parte del riesgo. La decisión central: ¿cuándo conviene comprar un servicio en vez de poseer el sistema, y con qué probabilidad?
- 🔗 **Se estudia junto con:** Comprar un servicio, capex, punto de equilibrio, Precio fijo.

📘 **Dónde se aprende** (1 clase): [B124-C02 · Agencias científicas y empresas](../programa/clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md).

### Posición

- La posición `r` es el vector que va desde el origen del marco hasta el cuerpo; sus componentes son `(x, y)`.
- La posición `q` es el vector de parámetros.
- Posición: puesto de la sala de control.

💡 **Cómo se explica en la clase [B05-C02](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md):**
- Si entre `t₁` y `t₂` la posición cambia `Δr`, la velocidad media es `v̄ = Δr/Δt`, con unidad m/s.
- Con tres posiciones consecutivas puedes estimarla: `a(t) ≈ [r(t+Δt) − 2r(t) + r(t−Δt)] / Δt²`.
- 🎯 **Por qué importa:** Cuando una agencia dice que un satélite «va a 7,7 km/s», ¿respecto de qué y en qué dirección? La pregunta motivadora es: ¿cómo describo un movimiento de forma que otra persona lo reconstruya sin ambigüedad?
- 🔗 **Se estudia junto con:** desplazamiento, distancia recorrida, velocidad media, velocidad instantánea.

📘 **Dónde se aprende** (3 clases): [B05-C02 · Posición, velocidad y aceleración](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md); [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md); [B96-C03 · Roles de control de misión](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md).

### Posición lagrangiana

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B36-C05](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md):**
- En Einstein–de Sitter (`4πGρ̄ = 1,5 H²`) la ecuación de cada lámina es `x'' + (3/2a) x' = (3/2) a⁻² (x − q)` en la variable `a`, donde `q` es la posición lagrangiana del rango (la fuerza en 1D es exacta incluso después del cruce).
- 🎯 **Por qué importa:** Una simulación sin comprobar contra un caso exacto no es una prueba. La decisión central: ¿converge el integrador al resultado analítico y qué pasa cuando las láminas se cruzan?
- 🔗 **Se estudia junto con:** lámina, aproximación de Zel'dovich, caja periódica, salto de rana.

📘 **Dónde se aprende** (1 clase): [B36-C05 · Simulaciones cosmológicas de N cuerpos: condiciones iniciales y caja periódica](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md).

### Positiva

- La entalpía de reacción `Δ_rH` es el cambio de entalpía por mol de reacción tal como está escrita; es negativa si la reacción libera energía (exotérmica) y positiva si la absorbe (endotérmica).

💡 **Contexto en la clase [B06-C12](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md):**
- **Idea central (modelo mental):** Piensa en un valle: los reactivos están en una altura y los productos en otra. Lo que importa para la energía liberada es el desnivel, no el camino. Los elementos puros son el «nivel del mar»; cada compuesto tiene una altura medida desde ahí (su entalpía de formación).
- 🎯 **Por qué importa:** Cualquier combustible, de una hoguera a un cohete, libera energía porque los productos están en un estado más estable que los reactivos. ¿Cuánta energía por kilogramo?
- 🔗 **Se estudia junto con:** entalpía, entalpía de reacción, negativa, entalpía de formación estándar.

📘 **Dónde se aprende** (1 clase): [B06-C12 · Termoquímica y energía de reacción](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md).

### Positividad

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B34-C06](../programa/clases/B34/B34-C06-tomografia-coronal/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Qué aporta la positividad?
- ⚠️ **Error frecuente:** Ignorar la positividad. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Más ángulos dan mejores imágenes, pero las vistas disponibles son pocas. La decisión central: ¿cuánto mejora la reconstrucción con más direcciones de vista?
- 🔗 **Se estudia junto con:** tomografía, proyección, método ART/Kaczmarz, no unicidad.

📘 **Dónde se aprende** (1 clase): [B34-C06 · Tomografía coronal](../programa/clases/B34/B34-C06-tomografia-coronal/CLASE.md).

### Positrón

- Un positrón (`e⁺`) es la antipartícula del electrón; al encontrar un electrón se aniquilan y liberan `2 m_e c²`.

💡 **Cómo se explica en la clase [B24-C06](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md):**
- El resultado neto de las cadenas de fusión es `4 ¹H → ⁴He + 2 e⁺ + 2 ν_e`, con `Q` total contando la aniquilación de los positrones con los electrones del plasma.
- *Descripción textual:* cuatro átomos de hidrógeno se convierten en un helio-4; los positrones se aniquilan con electrones; la energía total liberada, `26,73 MeV`, se reparte entre fotones y neutrinos y sostiene la luminosidad.
- ⚠️ **Error frecuente:** Olvidar la aniquilación de los positrones. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una estrella como el Sol brilla desde hace miles de millones de años; ninguna fuente química ni gravitatoria alcanza (C02). La fusión nuclear sí.
- 🔗 **Se estudia junto con:** fusión nuclear, defecto de masa, protón, partícula alfa.

📘 **Dónde se aprende** (1 clase): [B24-C06 · Fusión de hidrógeno](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md).

### Postefecto

- El postefecto es `−x` al retirar `p`.

💡 **Cómo se explica en la clase [B105-C25](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md):**
- X --> A["adaptacion x*<br/>y postefecto"]
- *Descripción textual:* el error entre la perturbación y el estado actualiza el estado con una retención y una sensibilidad; el estado converge a un estado estacionario y deja un postefecto al retirar la perturbación.
- ⚠️ **Error frecuente:** Ignorar el postefecto. Aparece al retirar la perturbación (8.3).
- 🎯 **Por qué importa:** Quien se adapta a un entorno nuevo comete errores al volver al anterior. Entender el ritmo de adaptación y el postefecto permite diseñar el entrenamiento y anticipar las torpezas.
- 🔗 **Se estudia junto con:** estado, error, retención, sensibilidad al error.

📘 **Dónde se aprende** (1 clase): [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md).

### Posterior

- El prior `P(θ)` expresa lo que se sabe de `θ` antes de ver los datos; la verosimilitud `P(datos | θ)` es el modelo de los datos (C07); la posterior `P(θ | datos)` es el conocimiento actualizado; el denominador, la evidencia o verosimilitud marginal, normaliza (y es clave en C22).
- El posterior es el producto de verosimilitud y prior normalizado.
- El posterior es `P(H | datos)`.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C12](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md):**
- Con prior débil `Gamma(1; 0,1)` (media 10, muy difuso), `S = 37` y `n = 10`: posterior `Gamma(38; 10,1)`, media `3,7624`, intervalo creíble 95 % `[2,662; 5,049]`.
- Con prior informativo `Gamma(8; 2)` (media 4): posterior `Gamma(45; 12)`, media `3,750`, intervalo `[2,735; 4,922]`.
- 🎯 **Por qué importa:** Una misión rara vez parte de cero: hay pruebas en tierra, misiones anteriores y física conocida. Y a menudo el dato es escaso (diez intervalos, treinta pruebas).
- 🔗 **Se estudia junto con:** teorema de Bayes, prior, verosimilitud, evidencia.

📘 **Dónde se aprende** (8 clases): [B12-C12 · Inferencia bayesiana](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md); [B19-C01 · Priors físicamente informados](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md); [B28-C22 · Inferencia bayesiana conjunta de parámetros de fuente multimensajero](../programa/clases/B28/B28-C22-inferencia-bayesiana-conjunta-de-parametros-de-fuente-multimensajero/CLASE.md); [B56-C15 · Falsos positivos de biofirmas](../programa/clases/B56/B56-C15-falsos-positivos-de-biofirmas/CLASE.md); [B63-C06 · Evaluación de riesgos biológicos de muestras: marcos de decisión](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md); [B67-C02 · Diseño de un programa de prospección por fases](../programa/clases/B67/B67-C02-diseno-de-un-programa-de-prospeccion-por-fases/CLASE.md) y 2 más.

### Post-money

- El pre-money y el post-money son las valoraciones antes y después de la ronda.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- Serie A: 10,0 Mum con pre-money 40,0 ⇒ post-money 50,0; el inversionista recibe el 20 %, la bolsa de opciones el 10 % y los existentes quedan con el 70 %: `1785714,3` acciones posteriores y un precio de `28,0000` um por acción.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?
- 🔗 **Se estudia junto con:** VAN, TIR, MOIC, pre-money.

📘 **Dónde se aprende** (1 clase): [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md).

### Postulado de la constancia de c

- El postulado de la constancia de `c` afirma que la velocidad de la luz en el vacío tiene el mismo valor `c` en todos los marcos inerciales, sin depender del movimiento de la fuente ni del observador.

💡 **Cómo se explica en la clase [B26-C01](../programa/clases/B26/B26-C01-postulados-de-relatividad-especial/CLASE.md):**
- Enunciar el principio de relatividad y el postulado de la constancia de `c`.
- 🎯 **Por qué importa:** Una nave espacial, un satélite de navegación y un rayo gamma comparten un problema: decir cómo se ve el mismo fenómeno desde marcos que se mueven entre sí. Si las velocidades se sumaran siempre como `u + v`, la luz de una nave que viaja al `90 %` de `c` iría más rápido que `c`.
- 🔗 **Se estudia junto con:** marco inercial, principio de relatividad, composición de velocidades, rapidez.

📘 **Dónde se aprende** (1 clase): [B26-C01 · Postulados de relatividad especial](../programa/clases/B26/B26-C01-postulados-de-relatividad-especial/CLASE.md).

### Postura

- La rigidez es el par por grado. Postura es la configuración de los ángulos articulares.

💡 **Cómo se explica en la clase [B107-C02](../programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/CLASE.md):**
- python programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/movilidad.py
- 🎯 **Por qué importa:** Los fragmentos consultados indican que tras el vuelo hay alteraciones del control postural y locomotor por adaptaciones sensoriomotoras (Macaulay et al., 2021) y que existen baterías funcionales con pruebas y medidas fisiológicas (Mulavara et al., 2018).
- 🔗 **Se estudia junto con:** rango libre, rango útil, espacio de trabajo, rigidez.

📘 **Dónde se aprende** (1 clase): [B107-C02 · Movilidad articular, flexibilidad y postura](../programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/CLASE.md).

### Potencia

- Una potencia `aⁿ` es `a` multiplicado por sí mismo `n` veces;
- La potencia `P = W/t` (o `F v`) se mide en vatios (W).
- La potencia eléctrica es `P = V I = I² R = V²/R`.
- *(y 10 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Producto de potencias de igual base: `aᵐ · aⁿ = aᵐ⁺ⁿ`.
- Potencia de un producto: `(ab)ⁿ = aⁿbⁿ`.
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.
- 🔗 **Se estudia junto con:** base, exponente, cuadrado, cubo.

📘 **Dónde se aprende** (14 clases): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md); [B05-C06 · Trabajo y energía](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md); [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md); [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md); [B12-C26 · Sesgos y potencia estadística en poblaciones pequeñas](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md) y 8 más.

### Potencia de Carnot

- La potencia de Carnot es la mínima para extraer calor.

💡 **Contexto en la clase [B49-C07](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md):**
- **Idea central (modelo mental):** Como un termo: lo que importa es cuánto calor se cuela por conducción y radiación, no solo cuán frío esté el líquido.
- 🎯 **Por qué importa:** Cada kelvin ahorrado exige vatios en la cabeza fría, y cada vatio de carga reduce el margen. La decisión central: ¿a qué temperatura enfriar y cuánta carga admite el criostato?
- 🔗 **Se estudia junto con:** ruido de Johnson, potencia disponible, cabeza fría, carga térmica.

📘 **Dónde se aprende** (1 clase): [B49-C07 · Criogenia y refrigeración de receptores de radio](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md).

### Potencia de diseño

- La potencia de diseño es la media dividida por la disponibilidad.

💡 **Cómo se explica en la clase [B59-C20](../programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/CLASE.md):**
- Potencia media `87 101/8 760 = 9,94 kW`; de diseño con disponibilidad `0,85`, `11,70 kW`.
- La energía es `87 101 kWh/año` (extracción `42,7 %`, electrólisis `41,1 %`), la potencia media `9,94 kW` y la de diseño `11,70 kW`; la planta pesa `1 551 kg` y amortiza su masa en `57 días` de producción.
- 🎯 **Por qué importa:** Un diseño conceptual no es un número sino un conjunto coherente. La decisión central: ¿qué potencia y qué masa necesita una planta que produce 10 t de agua al año, y qué parámetro la gobierna?
- 🔗 **Se estudia junto con:** libro de energía, masa específica, diseño conceptual, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B59-C20 · Diseño conceptual de planta ISRU](../programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/CLASE.md).

### Potencia de enfriamiento

- La potencia de enfriamiento `Q` extrae calor.

💡 **Cómo se explica en la clase [B44-C08](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md):**
- Límite: una sola masa térmica y potencia de enfriamiento constante.
- 🎯 **Por qué importa:** La cámara no está fría al encenderla. La decisión central: ¿cuánto hay que esperar antes de calibrar y qué temperatura final se alcanza?
- 🔗 **Se estudia junto con:** capacidad térmica, conductancia, constante de tiempo, temperatura límite.

📘 **Dónde se aprende** (1 clase): [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md).

### Potencia de frenado

- La potencia de frenado es `Ė = −Iωω̇`.

💡 **Cómo se explica en la clase [B27-C05](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md):**
- Calcular la edad característica y la potencia de frenado.
- 🎯 **Por qué importa:** Un púlsar da, a la vez, un reloj de precisión, la medida de su campo magnético y, en una binaria, la masa de las estrellas y una prueba de la relatividad general. La decisión central: dados el periodo y su derivada, ¿qué campo, edad y potencia de frenado tiene el púlsar y qué se aprende de su binaria?
- 🔗 **Se estudia junto con:** púlsar, periodo, dipolo magnético en rotación, campo ecuatorial.

📘 **Dónde se aprende** (1 clase): [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md).

### Potencia de mantenimiento

- La potencia de mantenimiento es la energía por segundo que una célula necesita solo para sobrevivir.

💡 **Cómo se explica en la clase [B56-C07](../programa/clases/B56/B56-C07-energia-quimica-para-la-vida/CLASE.md):**
- Con una potencia de mantenimiento de `10⁻¹⁹ W` (valor ilustrativo no consultado) y `39,3 kJ/mol`, hacen falta `10⁻¹⁹/39 300 = 2,5 × 10⁻²⁴ mol/s`, unas 2 moléculas de CH₄ por segundo.
- Definir energía libre de reacción, cociente de reacción, constante de equilibrio y potencia de mantenimiento.
- ⚠️ **Error frecuente:** Presentar la potencia de mantenimiento como dato. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Un ambiente con agua pero sin fuente de energía química es un desierto para la vida. En un océano sin luz, la energía viene de reacciones entre compuestos reducidos y oxidados.
- 🔗 **Se estudia junto con:** energía libre de reacción, cociente de reacción, constante de equilibrio, quimiolitótrofo.

📘 **Dónde se aprende** (1 clase): [B56-C07 · Energía química para la vida](../programa/clases/B56/B56-C07-energia-quimica-para-la-vida/CLASE.md).

### Potencia de pico

- La potencia de pico es la media dividida por el factor de trabajo.

💡 **Cómo se explica en la clase [B92-C01](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md):**
- *Descripción textual:* la semilla pasa por el amplificador; la potencia media, con el factor de trabajo de PPM, da la potencia de pico y la energía por pulso; con la energía del fotón da la tasa de fotones.
- Paso 2 · Potencia de pico. `4/0,0125 = 320 W`.
- ⚠️ **Error frecuente:** Confundir potencia media con potencia de pico. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un enlace óptico se dimensiona con fotones, no con vatios. La decisión central: ¿cuánta potencia de pico y cuánta energía por pulso debe entregar la fuente para una potencia media dada, y hasta dónde sirve aumentar la ganancia del amplificador?
- 🔗 **Se estudia junto con:** rejilla de frecuencias, energía del fotón, factor de trabajo, energía de saturación.

📘 **Dónde se aprende** (1 clase): [B92-C01 · Fuentes láser y amplificadores para enlaces espaciales](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md).

### Potencia de reposo

- La potencia de reposo crece con la masa (`25 W + 0,35 W/kg`, sintético).

💡 **Cómo se explica en la clase [B83-C20](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md):**
- La potencia de reposo es `25 + 0,35 m` W; la energía requerida por orbita en el eclipse máximo (β = 0°, 35,61 min de eclipse) es 93,05 Wh; el panel se dimensiona con 20 % de margen de diseño y se divide por 30 W/kg; la batería, con un DoD del 30 % y 120 Wh/kg.
- M["Masa seca"] --> P["Potencia de reposo"]
- 🎯 **Por qué importa:** Cada presupuesto aislado puede cerrar y el conjunto no. La decisión central: ¿existe una masa seca que sea coherente con la potencia, las baterías, la estructura y el propelente que ella misma exige, y cabe en el límite?
- 🔗 **Se estudia junto con:** diseño preliminar, lazo de diseño, iteración de punto fijo, bisección.

📘 **Dónde se aprende** (1 clase): [B83-C20 · Diseño preliminar completo de misión](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md).

### Potencia del chorro

- La potencia del chorro `P_jet = ½ ṁ Vₑ²` es la energía cinética por segundo del escape.

💡 **Cómo se explica en la clase [B78-C06](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md):**
- *Descripción textual:* la potencia de entrada, por la eficiencia, da la potencia del chorro; con la velocidad de escape fija el empuje; el empuje por potencia cae como `1/Vₑ` y fija el tiempo de maniobra.
- Paso 1 · Potencia del chorro. `½ × 0,091 × 28 000 = 1274 W`.
- ⚠️ **Error frecuente:** Confundir potencia de entrada con potencia del chorro. Se corrige con 8.2.
- 🎯 **Por qué importa:** Subir el `Isp` ahorra propelente, pero el mismo vatio produce menos empuje y la maniobra tarda más. La decisión central: ¿cuánto empuje da cada kilovatio, cómo cae con el `Isp` y qué pasa con el tiempo de maniobra?
- 🔗 **Se estudia junto con:** eficiencia total, empuje por potencia, limitado por potencia, planta de potencia.

📘 **Dónde se aprende** (1 clase): [B78-C06 · Propulsión eléctrica general](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md).

### Potencia del panel

- La potencia del panel es `S₀·η·f_emp·f_cos·f_deg·A`.

💡 **Cómo se explica en la clase [B83-C10](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md):**
- Calcular la potencia del panel al final de vida con eficiencia, empaquetado, coseno y degradación.
- Periodo = 95.65 min ; potencia del panel al final de vida = 126.10 W ; energia de carga por orbita = 91.07 Wh
- 🎯 **Por qué importa:** Un satélite sin energía suficiente en el peor eclipse se apaga y no vuelve. La decisión central: ¿el panel y la batería cierran el balance en el caso más desfavorable, con margen y con una descarga que la batería soporte?
- 🔗 **Se estudia junto con:** eclipse, ángulo beta, energía requerida, profundidad de descarga.

📘 **Dónde se aprende** (1 clase): [B83-C10 · Presupuestos de energía](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md).

### Potencia disipada

- La potencia disipada por unidad de masa es `½ ρ v³/β`.

💡 **Cómo se explica en la clase [B75-C15](../programa/clases/B75/B75-C15-aerofrenado-conceptual/CLASE.md):**
- Verificar el cambio de energía con la integral de la potencia disipada.
- 🎯 **Por qué importa:** Cada pasada baja el apoapsis un poco, y hace falta algún margen de seguridad con la densidad. La decisión central: ¿cuántas pasadas y cuánto tiempo hacen falta para bajar el apoapsis, y qué delta-v propulsivo se ahorra?
- 🔗 **Se estudia junto con:** aerofrenado, coeficiente balístico, densidad exponencial, corredor de aerofrenado.

📘 **Dónde se aprende** (1 clase): [B75-C15 · Aerofrenado conceptual](../programa/clases/B75/B75-C15-aerofrenado-conceptual/CLASE.md).

### Potencia disponible

- La potencia disponible es `k T B`.
- La potencia disponible es `P(r) = P₁ (1 UA/r)²`.

💡 **Contexto en la clase [B49-C07](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md):**
- **Idea central (modelo mental):** Como un termo: lo que importa es cuánto calor se cuela por conducción y radiación, no solo cuán frío esté el líquido.
- 🎯 **Por qué importa:** Cada kelvin ahorrado exige vatios en la cabeza fría, y cada vatio de carga reduce el margen. La decisión central: ¿a qué temperatura enfriar y cuánta carga admite el criostato?
- 🔗 **Se estudia junto con:** ruido de Johnson, cabeza fría, carga térmica, aislamiento multicapa.

📘 **Dónde se aprende** (2 clases): [B49-C07 · Criogenia y refrigeración de receptores de radio](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md); [B81-C05 · Limitaciones de potencia en propulsión eléctrica](../programa/clases/B81/B81-C05-limitaciones-de-potencia-en-propulsion-electrica/CLASE.md).

### Potencia específica

- La potencia específica es `P/m`.

💡 **Cómo se explica en la clase [B86-C03](../programa/clases/B86/B86-C03-arreglos-fotovoltaicos-desplegables/CLASE.md):**
- Con `2,2 kg/m²`, la masa es `2,64 kg` y la potencia específica `155,1 W/kg` (solo paneles).
- Calcular la potencia específica en W/kg.
- ⚠️ **Error frecuente:** Confundir potencia específica de paneles con la del subsistema. Se corrige con 8.2: aquí solo cuentan los paneles.
- 🎯 **Por qué importa:** El ala es el mayor elemento del satélite y su geometría define la potencia, el volumen de lanzamiento y la dinámica. Un ala mal orientada pierde potencia con el coseno y un ala demasiado flexible interactúa con el control de actitud.
- 🔗 **Se estudia junto con:** panel, ala, desplegado, primer modo.

📘 **Dónde se aprende** (1 clase): [B86-C03 · Arreglos fotovoltaicos desplegables](../programa/clases/B86/B86-C03-arreglos-fotovoltaicos-desplegables/CLASE.md).

### Potencia máxima de carga

- La potencia máxima de carga limita la recuperación.

💡 **Cómo se explica en la clase [B86-C13](../programa/clases/B86/B86-C13-energia-durante-eclipse/CLASE.md):**
- Calcular el tiempo de recarga con una potencia máxima de carga.
- 🎯 **Por qué importa:** Una batería que cubre bien un eclipse puede fallar tras cien porque cada órbita pierde un poco más de lo que recupera. El cierre del ciclo es la prueba de que el diseño es sostenible.
- 🔗 **Se estudia junto con:** cierre del ciclo, déficit por órbita, régimen periódico, generación mínima.

📘 **Dónde se aprende** (1 clase): [B86-C13 · Energía durante eclipse](../programa/clases/B86/B86-C13-energia-durante-eclipse/CLASE.md).

### Potencia normalizada

- La potencia normalizada `z = P/σ²`.

💡 **Cómo se explica en la clase [B29-C19](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md):**
- *Descripción textual:* con los tiempos se calcula la potencia de Lomb–Scargle, que coincide con el ajuste de mínimos cuadrados; la función ventana explica los alias; bajo el ruido la potencia normalizada es exponencial.
- 🎯 **Por qué importa:** Un periodograma sin cuidado señala alias en lugar del periodo verdadero, y una potencia alta puede ser una fluctuación del ruido. La decisión central: ¿qué picos son del periodo verdadero, cuáles son alias y qué potencia es significativa?
- 🔗 **Se estudia junto con:** periodograma, desfase, función ventana, alias.

📘 **Dónde se aprende** (1 clase): [B29-C19 · Análisis de series temporales irregularmente muestreadas](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md).

### Potencia permisible

- La potencia permisible es el nivel máximo de interferencia aceptado en la estación afectada.

💡 **Cómo se explica en la clase [B120-C02](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md):**
- Ejercicio 2 · con una pista. ¿Qué `d` resulta si la potencia permisible sube 6 dB (a −104 dBW)?
- 🎯 **Por qué importa:** Coordinar con otros servicios define dónde y cómo se puede operar y ninguna clase lo trata. La decisión central: ¿con qué administraciones hay que coordinar una estación terrena y en cuánto tiempo deben responder?
- 🔗 **Se estudia junto con:** zona de coordinación, distancia de coordinación, PIRE, pérdida de espacio libre.

📘 **Dónde se aprende** (1 clase): [B120-C02 · Zonas de coordinación entre servicios radioeléctricos](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md).

### Potencia total

- La potencia total `P_GW` es el flujo integrado sobre la esfera.
- La potencia total mide sin conmutar.

💡 **Cómo se explica en la clase [B28-C05](../programa/clases/B28/B28-C05-ondas-gravitacionales/CLASE.md):**
- *Descripción textual:* la masa de chirrido, la frecuencia y la distancia dan la amplitud; de ella salen el flujo, la potencia total y el desplazamiento; la potencia total se contrasta con la fórmula de Peters.
- Calcular el flujo `F = (πc³/4G) f²h²` y la potencia total.
- 🎯 **Por qué importa:** La amplitud de una señal real es de `10⁻²¹` a `10⁻²³`: un cambio de longitud mil veces menor que un protón en un brazo de kilómetros. Entender esa escala explica por qué hace falta un instrumento extraordinario.
- 🔗 **Se estudia junto con:** deformación, polarización, flujo, vista de frente.

📘 **Dónde se aprende** (2 clases): [B28-C05 · Ondas gravitacionales](../programa/clases/B28/B28-C05-ondas-gravitacionales/CLASE.md); [B49-C08 · Estabilidad de ganancia de receptores y variaciones de ganancia](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md).

### Potencial

- El potencial `V(φ)`.
- La energía cinética `K = φ̇²/2` y la potencial `V`.
- El potencial gravitatorio `Φ`.

💡 **Cómo se explica en la clase [B38-C05](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md):**
- Cada potencial es una función cerrada, su fuerza se puede verificar de dos maneras y la órbita conserva lo que debe.
- Un potencial así no incluye el gas ni los brazos espirales.
- 🎯 **Por qué importa:** Toda simulación de estrellas necesita una fuerza. La decisión central: ¿qué potencial simple reproduce una curva de rotación plana y cuánto aporta cada componente?
- 🔗 **Se estudia junto con:** velocidad circular, bulbo de Plummer, disco de Miyamoto–Nagai, halo NFW.

📘 **Dónde se aprende** (4 clases): [B38-C05 · Potenciales galácticos: Plummer, Miyamoto-Nagai y NFW](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md); [B40-C01 · Inflación cósmica: motivación y dinámica básica](../programa/clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md); [B40-C06 · Campos escalares en cosmología: potenciales y evolución](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md); [B40-C09 · Efecto Sachs-Wolfe y efecto Sachs-Wolfe integrado](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md).

### Potencial de corrosión

- El potencial de corrosión ordena los metales en una serie galvánica.

💡 **Cómo se explica en la clase [B84-C21](../programa/clases/B84/B84-C21-compatibilidad-quimica-y-galvanica-de-materiales/CLASE.md):**
- *Descripción textual:* la diferencia de potencial y las áreas dan la corriente, que se convierte en densidad anódica y en velocidad de corrosión.
- 🎯 **Por qué importa:** Un tornillo de acero inoxidable en un panel de aluminio puede corroerlo 90 veces más rápido que otro de aluminio, y la corrosión ocurre en tierra, antes del lanzamiento. La decisión central: ¿qué pares de materiales pueden ir en contacto y cómo debe ser la relación de áreas?
- 🔗 **Se estudia junto con:** corriente galvánica, velocidad de corrosión, relación de áreas.

📘 **Dónde se aprende** (1 clase): [B84-C21 · Compatibilidad química y galvánica de materiales](../programa/clases/B84/B84-C21-compatibilidad-quimica-y-galvanica-de-materiales/CLASE.md).

### Potencial de la nave

- El potencial de la nave desplaza la energía por carga.

💡 **Cómo se explica en la clase [B35-C06](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md):**
- Reconocer el efecto del potencial de la nave.
- (3) potencial de la nave de +10 V: la energia por carga medida difiere en 10 eV ; sobre 400 km/s (E = 835 eV) la velocidad aparente cambia en 2.388 km/s
- ⚠️ **Error frecuente:** Olvidar el potencial de la nave. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un momento sin su incertidumbre ni sus sesgos no es una medición. La decisión central: ¿cuántas cuentas hacen falta y qué sesgos introduce el instrumento?
- 🔗 **Se estudia junto con:** cuentas, momento, ventana, ruido de Poisson.

📘 **Dónde se aprende** (1 clase): [B35-C06 · Mediciones in situ de plasmas espaciales](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md).

### Potencial de Roche

- El potencial de Roche es el potencial efectivo en el sistema que rota con la binaria: la gravedad de las dos estrellas más el término centrífugo.

💡 **Cómo se explica en la clase [B24-C22](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md):**
- A["Masas y semieje"] --> B["Potencial de Roche"]
- Definir potencial de Roche, punto de Lagrange L1 y lóbulo de Roche.
- 🎯 **Por qué importa:** Una estrella que se expande (C16) o se hincha en una binaria puede llenar la región donde su gravedad domina y verter gas sobre su compañera. Esa transferencia cambia las masas, la órbita y el destino de ambas, y es el camino hacia muchos objetos exóticos.
- 🔗 **Se estudia junto con:** punto de Lagrange L1, lóbulo de Roche, radio del lóbulo, razón de masas.

📘 **Dónde se aprende** (1 clase): [B24-C22 · Evolución binaria: lóbulo de Roche y transferencia de masa](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md).

### Potencial de una capa

- El potencial de una capa de masa `M_s` y radio `a` es `−GM_s/r` si `r > a` y `−GM_s/a` si `r < a`.

💡 **Cómo se explica en la clase [B09-C20](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md):**
- El potencial en el punto a distancia `r` de una capa de radio `a` y masa `M_s` es `Φ(r) = −(GM_s/2) ∫₀^π sin θ dθ / √(r² + a² − 2 r a cos θ)` (se integró ya en el ángulo azimutal).
- Ejercicio 1 · con los pasos indicados. Para una capa de radio `a = 10⁷ m` y `GM_s = 3,986 004 × 10¹⁴ m³/s²`, ¿cuánto vale el potencial en `r = 0,5a` y la gravedad allí?
- 🎯 **Por qué importa:** Una sonda en órbita, un satélite geodésico o un gravímetro en una montaña reciben la atracción de un cuerpo que no es un punto: tiene tamaño, forma achatada, rotación y estructura interna. Reducirlo a un punto es correcto fuera de una esfera homogénea, pero deja de serlo cuando importa el achatamiento o el interior.
- 🔗 **Se estudia junto con:** teorema de la capa, masa encerrada, achatamiento, J₂.

📘 **Dónde se aprende** (1 clase): [B09-C20 · Aplicaciones a campos gravitatorios](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md).

### Potencial de Yukawa

- El potencial de Yukawa `e^(−r/λ)/r`.

💡 **Contexto en la clase [B31-C09](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md):**
- **Idea central (modelo mental):** Un mediador pesado es un grito que no llega lejos; uno sin masa (el fotón) llega a cualquier distancia.
- 🎯 **Por qué importa:** Saber qué interacción domina en cada escala explica por qué los núcleos, los átomos y las estrellas son como son. La decisión central: ¿cuánto más fuerte es la fuerza eléctrica que la gravitatoria y qué fija el alcance de una fuerza?
- 🔗 **Se estudia junto con:** constante de estructura fina, radio de Bohr, longitud de Compton, alcance.

📘 **Dónde se aprende** (1 clase): [B31-C09 · Interacciones fundamentales](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md).

### Potencial eléctrico

- El potencial eléctrico `V` es energía por carga (J/C = V); un campo uniforme `E` da una caída de potencial `E d` en una distancia `d`.

💡 **Contexto en la clase [B05-C15](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md):**
- **Idea central (modelo mental):** Una carga fuente modifica el espacio alrededor; una carga de prueba colocada en un punto siente la fuerza `q E`. La separación evita recalcular la fuente en cada caso.
- 🎯 **Por qué importa:** El espacio está lleno de partículas cargadas que un satélite atraviesa, y un satélite puede acumular carga. La pregunta motivadora es: ¿cómo describir la fuerza eléctrica sobre una carga sin conocer a la vez todas las demás, y cuánto más fuerte es que la gravedad?
- 🔗 **Se estudia junto con:** carga eléctrica, carga elemental, ley de Coulomb, campo eléctrico.

📘 **Dónde se aprende** (1 clase): [B05-C15 · Campos eléctricos](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md).

### Potencial flotante

- El potencial flotante `V` anula la corriente neta: `J_e0 e^(V/T_e) = J_i`.

💡 **Cómo se explica en la clase [B85-C15](../programa/clases/B85/B85-C15-electrificacion-superficial/CLASE.md):**
- *Descripción textual:* el plasma define las corrientes de electrones e iones; su igualdad da el potencial flotante, del que se deriva el campo y el riesgo de descarga.
- Calcular el potencial flotante en LEO con iones de proa y electrones retardados.
- 🎯 **Por qué importa:** Una carga diferencial de kilovoltios entre superficies puede producir una descarga que daña la electrónica. La decisión central: ¿a qué potencial flota una superficie en un plasma dado y es probable que alcance un umbral de riesgo?
- 🔗 **Se estudia junto con:** carga diferencial, descarga, tiempo de carga.

📘 **Dónde se aprende** (1 clase): [B85-C15 · Electrificación superficial](../programa/clases/B85/B85-C15-electrificacion-superficial/CLASE.md).

### Potencial gravitatorio

- El potencial gravitatorio de una masa puntual es `Φ(r) = −GM/r`.
- El potencial gravitatorio `Φ` es la función cuya derivada, cambiada de signo, es la aceleración de la gravedad: `g = −dΦ/dr` para un campo radial atractivo.
- El potencial gravitatorio `Φ` es la energía potencial por unidad de masa.

💡 **Cómo se explica en la clase [B09-C08](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md):**
- Un segundo ejemplo usa el potencial gravitatorio terrestre con los valores nominales de la IAU, `(GM)_E^N = 3,986 004 × 10¹⁴ m³ s⁻²` y `R_eE^N = 6,3781 × 10⁶ m` (S2).
- Interpretar el potencial gravitatorio como antiderivada de `g`.
- 🎯 **Por qué importa:** Un acelerómetro mide aceleración; lo que se necesita es velocidad y posición. Una gravedad `g(r)` se conoce; lo que decide si una sonda escapa es la energía, que sale de «deshacer» esa derivada.
- 🔗 **Se estudia junto con:** antiderivada, integral indefinida, constante de integración, condición inicial.

📘 **Dónde se aprende** (3 clases): [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md); [B09-C08 · Integrales indefinidas](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md); [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md).

### Pozo de carga

- El pozo de carga es el máximo de electrones que un píxel puede acumular antes de saturar.

💡 **Cómo se explica en la clase [B13-C15](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md):**
- El canal UVIS de la cámara WFC3 del telescopio espacial Hubble tiene un ruido de lectura de `2,90 a 3,01 e⁻` por amplificador (medidas de 2009 en el manual del instrumento, S1) y una ganancia de `1,584 a 1,615 e⁻/DN` (septiembre de 2025, S1); el pozo de carga llega como máximo a unos `72 400 e⁻` (S1).
- 🎯 **Por qué importa:** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.
- 🔗 **Se estudia junto con:** ruido de disparo, fondo de cielo B, corriente de oscuridad D, ruido de lectura R.

📘 **Dónde se aprende** (1 clase): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md).

### Pozo infinito

- El pozo infinito confina entre dos paredes.

💡 **Contexto en la clase [B31-C02](../programa/clases/B31/B31-C02-ecuacion-de-schrodinger/CLASE.md):**
- **Idea central (modelo mental):** Como una cuerda de guitarra fija en sus extremos, solo ciertas ondas caben y cada una tiene su energía; la barrera es una zona donde la onda decae, pero no se anula.
- 🎯 **Por qué importa:** Los espectros de los átomos y los niveles de los núcleos salen de esta ecuación. La decisión central: ¿cómo se obtiene la energía de un estado ligado y cuánto atraviesa una barrera?
- 🔗 **Se estudia junto con:** hamiltoniano, autovalor, oscilador armónico, efecto túnel.

📘 **Dónde se aprende** (1 clase): [B31-C02 · Ecuación de Schrödinger](../programa/clases/B31/B31-C02-ecuacion-de-schrodinger/CLASE.md).

### Pozo lleno

- El pozo lleno es la carga máxima por píxel.

💡 **Cómo se explica en la clase [B44-C05](../programa/clases/B44/B44-C05-pozo-lleno-y-rango-dinamico/CLASE.md):**
- FW["pozo lleno"] --> DR["rango dinámico"]
- La evidencia es la ficha del pozo lleno y el rango dinámico del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Una cámara debe medir a la vez estrellas débiles y brillantes sin saturar. La decisión central: ¿hasta qué señal media puedo exponer sin saturar el pozo?
- 🔗 **Se estudia junto con:** rango dinámico, ganancia, saturación, paso.

📘 **Dónde se aprende** (1 clase): [B44-C05 · Pozo lleno y rango dinámico](../programa/clases/B44/B44-C05-pozo-lleno-y-rango-dinamico/CLASE.md).

### PpCO₂

- ppCO₂: presión parcial de CO₂ en mmHg.

💡 **Cómo se explica en la clase [B106-C04](../programa/clases/B106/B106-C04-control-de-dioxido-de-carbono/CLASE.md):**
- En estado estacionario `x_ss = g/(n k)` y en mmHg `ppCO₂ = x P`.
- Sin depurador, `d(ppCO₂)/dt = g P/n = 0,624 mmHg/h`.
- ⚠️ **Error frecuente:** Usar la fracción en % sin pasar a mmHg. ppCO₂ = x·P (8.1).
- 🎯 **Por qué importa:** Una cabina cerrada acumula el CO₂ de la tripulación hasta que un depurador lo retira. Si el depurador es insuficiente o falla, hay un tiempo finito antes de pasar los límites.
- 🔗 **Se estudia junto con:** Depurador, Caudal Q, Eficiencia η, Estado estacionario.

📘 **Dónde se aprende** (1 clase): [B106-C04 · Control de dióxido de carbono](../programa/clases/B106/B106-C04-control-de-dioxido-de-carbono/CLASE.md).

### PPFD

- El PPFD mide la luz útil para la fotosíntesis.
- PPFD: flujo de fotones útiles.

💡 **Cómo se explica en la clase [B59-C14](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md):**
- AREA --> P["× PPFD ÷ eficacia: potencia"]
- ⚠️ **Error frecuente:** Confundir PPFD con iluminancia. El PPFD mide fotones útiles; sección 6.
- 🎯 **Por qué importa:** Cultivar exige luz, y la luz eléctrica cuesta potencia. La decisión central: ¿cuántos metros cuadrados y cuántos kilovatios necesita un cultivo para producir el oxígeno de una persona?
- 🔗 **Se estudia junto con:** fotones por O₂, eficacia, evapotranspiración, sustrato.

📘 **Dónde se aprende** (2 clases): [B59-C14 · Agricultura y sustratos artificiales](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md); [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md).

### Ppm

- La altitud equivalente sigue la atmósfera estándar ISA: `p = 101,325 (1 − 2,25577·10⁻⁵ h)^5,25588 kPa`. ppm son partes por millón: `p_CO₂ = ppm·10⁻⁶·P_total`.
- Índice de riesgo aditivo: suma de razones concentración/límite. ppm: partes por millón en volumen.

💡 **Cómo se explica en la clase [B105-C21](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md):**
- Con CO₂ ambiente de 400; 2.000; 5.000; 10.000 y 20.000 ppm en la cabina A (elevación didáctica `PaCO₂ = 5,33 + 0,9·p_CO₂`): `PAO₂` de 13,25; 13,07; 12,73; 12,16 y 11,02 kPa.
- Con 5.000 ppm de CO₂ en la cabina A, la presión parcial de CO₂ ambiente es 0,507 kPa y `PAO₂` baja a 12,73 kPa (modelo didáctico).
- 🎯 **Por qué importa:** La misma cantidad de oxígeno inspirado no significa lo mismo a 101 kPa que a 70 kPa: importa la presión parcial. La decisión central: ¿qué presión parcial de oxígeno alveolar resulta de una atmósfera dada y cómo cambia con el CO₂ ambiente y la ventilación?
- 🔗 **Se estudia junto con:** ecuación del gas alveolar, presión inspirada, altitud equivalente, hipoventilación.

📘 **Dónde se aprende** (2 clases): [B105-C21 · Fisiología respiratoria en microgravedad y atmósferas de cabina](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md); [B106-C24 · Calidad del aire y límites de exposición en cabina](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md).

### PPM de orden M

- El PPM de orden `M` coloca un pulso en una de `M` ranuras (`log₂ M` bits).

💡 **Contexto en la clase [B89-C18](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md):**
- 🎯 **Por qué importa:** Las comunicaciones ópticas prometen más tasa por masa y potencia que la radio; entender el presupuesto de fotones y la modulación por posición de pulso explica por qué y a qué costo (apuntamiento, nubes). La decisión central: ¿cuántos fotones por bit llegan y qué error de símbolo implica la modulación PPM elegida?
- 🔗 **Se estudia junto con:** banda C óptica, detección de fotones, error de símbolo sin fondo, fotones por bit.

📘 **Dónde se aprende** (1 clase): [B89-C18 · Comunicaciones ópticas espaciales](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md).

### Práctica estatal

- La práctica estatal es lo que hacen los Estados.

💡 **Cómo se explica en la clase [B119-C31](../programa/clases/B119/B119-C31-practica-estatal-y-costumbre-internacional-en-el-derecho-espacial/CLASE.md):**
- ese debate, el art. 38 del Estatuto de la Corte Internacional de Justicia, la jurisprudencia y la práctica estatal no se consultaron.
- Estatuto de la CIJ, jurisprudencia y practica estatal NO consultados (notas de UNOOSA y legal.un.org consultadas 2026-11-11).
- 🎯 **Por qué importa:** B119 presenta los tratados; no enseña la costumbre ni la práctica estatal, que complementan a los tratados en un campo donde los Estados no son partes de todos ellos. La decisión central: ¿qué factores aceleran o frenan que una práctica se vuelva general?
- 🔗 **Se estudia junto con:** opinio juris, difusión, imitación, umbral de generalidad.

📘 **Dónde se aprende** (1 clase): [B119-C31 · Práctica estatal y costumbre internacional en el derecho espacial](../programa/clases/B119/B119-C31-practica-estatal-y-costumbre-internacional-en-el-derecho-espacial/CLASE.md).

### Precarga

- La precarga `T₀` es el par del resorte con el mecanismo plegado.
- La precarga es el llenado del corazón antes de contraerse.
- Precarga: fuerza de tracción que el apriete deja en el perno.

💡 **Cómo se explica en la clase [B84-C13](../programa/clases/B84/B84-C13-mecanismos-desplegables/CLASE.md):**
- Con fricción triple o precarga −20 % el margen es menor que 1: el panel puede no llegar al tope.
- Subir la precarga a `0,4289 N·m` da razón 2,0 con `3,746 rad/s` y energía de impacto `0,3509 J` (más impacto): se compensan margen y carga de choque.
- 🎯 **Por qué importa:** Un mecanismo que se despliega bien en el banco puede quedarse trabado en órbita si la fricción sube o la precarga baja; el margen de par lo cuantifica. La decisión central: ¿qué razón de par tiene el despliegue y qué precarga hace falta para cumplir el requisito?
- 🔗 **Se estudia junto con:** razón de par, tope, balance de energía.

📘 **Dónde se aprende** (3 clases): [B84-C13 · Mecanismos desplegables](../programa/clases/B84/B84-C13-mecanismos-desplegables/CLASE.md); [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md); [B105-C01 · Respuesta cardiovascular a microgravedad](../programa/clases/B105/B105-C01-respuesta-cardiovascular-a-microgravedad/CLASE.md).

### Precaución

- La precaución es evitar daños aunque la evidencia sea incompleta.

💡 **Contexto en la clase [B56-C19](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md):**
- **Idea central (modelo mental):** Cada línea de evidencia añade peso (positivo si favorece, negativo si refuta). El umbral es la marca en la balanza a partir de la cual se actúa.
- 🎯 **Por qué importa:** Anunciar demasiado pronto un hallazgo puede dañar la ciencia y la confianza pública; ocultarlo puede dañar la transparencia. Hace falta una forma explícita de saber cuánta evidencia hay.
- 🔗 **Se estudia junto con:** log-odds, línea de evidencia, umbral de comunicación, transparencia.

📘 **Dónde se aprende** (1 clase): [B56-C19 · Ética del descubrimiento de vida](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md).

### Precedencia

- La precedencia es el orden en que se evalúan los operadores; la asociatividad dice hacia qué lado se agrupan los de igual precedencia.

💡 **Cómo se explica en la clase [B07-C03](../programa/clases/B07/B07-C03-operadores-y-expresiones/CLASE.md):**
- Una expresión se evalúa como un árbol: las operaciones de mayor precedencia son ramas bajas que se resuelven primero y alimentan a las de arriba.
- Aplicar las reglas de precedencia y usar paréntesis para fijar el orden.
- ⚠️ **Error frecuente:** Olvidar la precedencia de `` frente al signo. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** Casi cualquier resultado científico es una expresión: una masa dividida por un volumen, un cociente de períodos. Si no sabes en qué orden Python evalúa `a / b  3`, escribirás una fórmula distinta de la que piensas y no recibirás ningún aviso: el programa funcionará y dará un número equivocado.
- 🔗 **Se estudia junto con:** operador, operando, expresión, evalúa.

📘 **Dónde se aprende** (1 clase): [B07-C03 · Operadores y expresiones](../programa/clases/B07/B07-C03-operadores-y-expresiones/CLASE.md).

### Precesión

- Una época es la fecha a la que se refieren las coordenadas; la precesión es el lento giro del eje de la Tierra, que desplaza el sistema entero unos 50″ al año.
- La precesión es el avance angular del perihelio entre dos pasos.
- La precesión es el avance del periastro por vuelta.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C03](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md):**
- Se rompe en que el origen de la AR no está pegado al suelo: se desplaza por la precesión, y por eso importa la época.
- Estimar el efecto de la precesión entre épocas.
- 🎯 **Por qué importa:** Un catálogo no puede decir «a la izquierda de la Luna», porque eso cambia a cada minuto. Necesita direcciones fijas.
- 🔗 **Se estudia junto con:** declinación, ecuador celeste, ascensión recta, punto vernal.

📖 **Explicado a fondo:** [Precesión](esencial/esencial-m-z.md#precesión) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B08-C03 · Ascensión recta y declinación](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md); [B26-C08 · Geodésicas gravitacionales](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md); [B27-C09 · Órbitas en campos fuertes](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md); [B53-C21 · Rotación y orientación de cuerpos planetarios: polos y meridiano origen](../programa/clases/B53/B53-C21-rotacion-y-orientacion-de-cuerpos-planetarios-polos-y-meridiano-origen/CLASE.md).

### Precesión apsidal por J₂

- La regresión nodal por `J₂` es `Ω̇ = −(3/2) J₂ (R/a)² n` y la precesión apsidal por `J₂`, `ϖ̇ ≈ 3 J₂ (R/a)² n`.

💡 **Cómo se explica en la clase [B73-C19](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md):**
- Calcular la regresión nodal y la precesión apsidal por `J₂` de una luna.
- 🎯 **Por qué importa:** Un sistema lunar es un problema de varios perturbadores: el achatamiento del planeta aleja los nodos y los ápsides, el Sol los tira, y las lunas se perturban entre sí. Saber cuál domina a cada distancia decide en qué plano y con qué precesión se mueve una luna.
- 🔗 **Se estudia junto con:** radio de Hill, regresión nodal por J₂, regresión nodal solar, radio de Laplace.

📘 **Dónde se aprende** (1 clase): [B73-C19 · Mecánica de sistemas lunares](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md).

### Precesión de Lense–Thirring

- La precesión de Lense–Thirring (arrastre de marcos por la rotación del cuerpo) y la precesión geodésica de un giroscopio no se calculan aquí.

💡 **Cómo se explica en la clase [B72-C17](../programa/clases/B72/B72-C17-efectos-relativistas-orbitales/CLASE.md):**
- La rotación de la Tierra añade el arrastre de marcos (Lense–Thirring) y un giroscopio sufre la precesión geodésica; ninguno se calculó ni se consultó en esta clase.
- Lense-Thirring y precesion geodesica: NO calculadas ni consultadas en esta clase.
- 🎯 **Por qué importa:** La corrección relativista es un test histórico de la teoría y, en navegación por satélite, un término que los modelos de precisión no pueden ignorar. La decisión central: ¿cuánto vale el avance relativista del periapsis, cuándo es relevante y qué parte de la relatividad queda fuera de este cálculo?
- 🔗 **Se estudia junto con:** avance relativista del periapsis, aceleración de Schwarzschild post-newtoniana, precesión geodésica, mas.

📘 **Dónde se aprende** (1 clase): [B72-C17 · Efectos relativistas orbitales](../programa/clases/B72/B72-C17-efectos-relativistas-orbitales/CLASE.md).

### Precesión de los equinoccios

- La precesión de los equinoccios es el lento desplazamiento de los puntos de equinoccio sobre las estrellas; se detecta comparando posiciones de estrellas medidas con siglos de diferencia.

💡 **Contexto en la clase [B02-C03](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md):**
- **Idea central (modelo mental):** Si el Sol está tan lejos que sus rayos llegan paralelos, la diferencia entre el ángulo que forman los rayos con la vertical en dos ciudades es igual al ángulo que separa esas ciudades visto desde el centro de la Tierra.
- 🎯 **Por qué importa:** Un modelo geométrico responde a «¿qué figura reproduce estos movimientos?». Es una forma nueva de preguntar frente a la regla puramente numérica.
- 🔗 **Se estudia junto con:** circunferencia, estadio, meridiano, catálogo estelar.

📘 **Dónde se aprende** (1 clase): [B02-C03 · Astronomía griega y helenística](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md).

### Precesión del perigeo

- La precesión del perigeo es la variación de `ω`.
- La precesión del perigeo es `dω/dt`.

💡 **Cómo se explica en la clase [B72-C05](../programa/clases/B72/B72-C05-precesion-del-argumento-del-periapsis/CLASE.md):**
- La evidencia es la ficha de precesión del perigeo del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de precesión del perigeo*: tasas por altitud e inclinación, inclinación crítica, caso Molniya y la lista de lo consultado, lo ilustrativo y lo no consultado.
- 🎯 **Por qué importa:** Si el perigeo de una órbita muy excéntrica girara, el satélite dejaría de pasar por la región que interesa. La decisión central: ¿a qué inclinación el perigeo deja de moverse y cuánto se mueve en otras?
- 🔗 **Se estudia junto con:** inclinación crítica, órbita tipo Molniya, factor 5 cos² i − 1, línea de ápsides.

📘 **Dónde se aprende** (2 clases): [B72-C03 · Perturbación J2 terrestre](../programa/clases/B72/B72-C03-perturbacion-j2-terrestre/CLASE.md); [B72-C05 · Precesión del argumento del periapsis](../programa/clases/B72/B72-C05-precesion-del-argumento-del-periapsis/CLASE.md).

### Precesión geodésica

- La precesión de Lense–Thirring (arrastre de marcos por la rotación del cuerpo) y la precesión geodésica de un giroscopio no se calculan aquí.

💡 **Cómo se explica en la clase [B72-C17](../programa/clases/B72/B72-C17-efectos-relativistas-orbitales/CLASE.md):**
- La rotación de la Tierra añade el arrastre de marcos (Lense–Thirring) y un giroscopio sufre la precesión geodésica; ninguno se calculó ni se consultó en esta clase.
- Lense-Thirring y precesion geodesica: NO calculadas ni consultadas en esta clase.
- 🎯 **Por qué importa:** La corrección relativista es un test histórico de la teoría y, en navegación por satélite, un término que los modelos de precisión no pueden ignorar. La decisión central: ¿cuánto vale el avance relativista del periapsis, cuándo es relevante y qué parte de la relatividad queda fuera de este cálculo?
- 🔗 **Se estudia junto con:** avance relativista del periapsis, aceleración de Schwarzschild post-newtoniana, precesión de Lense–Thirring, mas.

📘 **Dónde se aprende** (1 clase): [B72-C17 · Efectos relativistas orbitales](../programa/clases/B72/B72-C17-efectos-relativistas-orbitales/CLASE.md).

### Precesión luni-solar

- La precesión luni-solar es el giro de `ĥ` alrededor de la normal de la órbita del perturbador.

💡 **Contexto en la clase [B72-C09](../programa/clases/B72/B72-C09-perturbaciones-solares/CLASE.md):**
- 🎯 **Por qué importa:** En órbitas altas el Sol y la Luna compiten con J2 y gobiernan la evolución de la inclinación y del nodo. La decisión central: ¿cuánto gira el plano de una órbita por la marea solar y qué fórmula sirve para predecirlo?
- 🔗 **Se estudia junto con:** marea solar, aproximación cuadrupolar, polo orbital.

📘 **Dónde se aprende** (1 clase): [B72-C09 · Perturbaciones solares](../programa/clases/B72/B72-C09-perturbaciones-solares/CLASE.md).

### Precesión-nutación

- La precesión-nutación es el movimiento del CIP en el sistema celeste; el IERS publica además desplazamientos del polo celeste (*celestial pole offsets*) respecto del modelo IAU 2006/2000A (S1, glosario).

💡 **Cómo se explica en la clase [B13-C22](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md):**
- Un `1 mas` de error en el polo celeste (precesión-nutación) es `3,09 cm` en la superficie; el vínculo celeste–terrestre del IERS, `±0,1 mas`, equivale a `3,1 mm` en la superficie.
- C -->|"Q(t): precesión-nutación<br/>+ offsets del polo celeste"| G["[GCRS]<br/>(ligado a los cuásares)"]
- 🎯 **Por qué importa:** Una estación terrestre apunta a una nave en el sistema celeste. Para ello debe saber cuánto ha girado la Tierra, hacia dónde apunta su eje en el cielo y dónde está ese eje dentro de la corteza.
- 🔗 **Se estudia junto con:** parámetros de orientación terrestre (EOP), CIP, movimiento polar, UT1 − UTC.

📘 **Dónde se aprende** (1 clase): [B13-C22 · Parámetros de orientación terrestre: precesión, nutación, UT1 y movimiento polar](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md).

### Precio fijo

- El punto de equilibrio `N*` es la cantidad de asientos en que ambas vías cuestan lo mismo. Precio fijo es el contrato en que el pago no sigue al costo real.

💡 **Cómo se explica en la clase [B124-C02](../programa/clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md):**
- El informe IG-20-005 de la OIG de la NASA (noviembre de 2019) describe que la NASA pasó de operar vehículos propios a pagar a empresas un precio fijo por transportar astronautas, y que desde 2006 compró 70 asientos Soyuz por unos 3 900 millones de USD; el costo medio informado fue `55,4` millones por asiento.
- Ejercicio 11 · transferencia. Transferencia. Un contrato de precio fijo traslada riesgo a la empresa.
- 🎯 **Por qué importa:** Las agencias científicas y las empresas cumplen papeles distintos: la agencia fija objetivos y paga; la empresa ofrece capacidad y asume parte del riesgo. La decisión central: ¿cuándo conviene comprar un servicio en vez de poseer el sistema, y con qué probabilidad?
- 🔗 **Se estudia junto con:** Comprar un servicio, Poseer, capex, punto de equilibrio.

📘 **Dónde se aprende** (1 clase): [B124-C02 · Agencias científicas y empresas](../programa/clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md).

### Precio fijo (FFP)

- Precio fijo (FFP): el pago no depende del costo real.

💡 **Cómo se explica en la clase [B124-C10](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md):**
- El precio fijo da certeza de gasto al comprador pero un precio mayor; el CPIF reparte el desvío (el contratista asume el 20 % hasta el techo) pero deja el gasto expuesto.
- El informe IG-20-005 de la OIG de la NASA (2019) señala que la NASA pasó a un enfoque comercial en que paga un precio fijo por el servicio de transporte de tripulación, como ya hacía con la carga.
- ⚠️ **Error frecuente:** Creer que el precio fijo es siempre el más barato. Se corrige con 8.1 y 8.4.
- 🎯 **Por qué importa:** El tipo de contrato reparte el riesgo de sobrecosto entre quien compra y quien vende. La decisión central: ¿cuánto riesgo asume cada parte con cada tipo de contrato y cuánto cuesta ese reparto en promedio?
- 🔗 **Se estudia junto con:** Costo más incentivo (CPIF), honorario objetivo, razón de reparto, techo.

📘 **Dónde se aprende** (1 clase): [B124-C10 · Contratos y compras espaciales](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md).

### Precio máximo

- El precio máximo es el que iguala el ahorro.

💡 **Cómo se explica en la clase [B119-C25](../programa/clases/B119/B119-C25-derecho-y-marcos-de-recursos-espaciales/CLASE.md):**
- Si el propergol se obtiene en el espacio, el ahorro es `3.95 M u.m.`, es decir `2500 u.m./kg` de propergol: es el precio máximo del propergol en el depósito.
- *Descripción textual:* el recurso produce propergol en un depósito, lo que ahorra lanzamientos; el ahorro fija el precio máximo; el marco legal condiciona el acceso al recurso.
- ⚠️ **Error frecuente:** Tomar el precio máximo como precio de mercado. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** B119 trata los tratados en general (C01, C05) y ninguna clase enseña los marcos de recursos ni el razonamiento económico que los motiva. La gobernanza se desarrolla en C36 y los aspectos técnicos en B59.
- 🔗 **Se estudia junto con:** utilización de recursos in situ, propergol, razón de masas, régimen internacional.

📘 **Dónde se aprende** (1 clase): [B119-C25 · Derecho y marcos de recursos espaciales](../programa/clases/B119/B119-C25-derecho-y-marcos-de-recursos-espaciales/CLASE.md).

### Precisión

- La estabilidad (no explotar) es distinta de la precisión (parecerse a la solución).
- La precisión es `TP/(TP + FP)`: de las alertas, cuántas son reales.
- La precisión (*sharpness*) es qué tan estrechos son los intervalos: un procedimiento puede estar calibrado y ser inútil (intervalos enormes).
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C09](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md):**
- D --> F["Luego revisar precisión<br/>(C19)"]
- *Descripción textual:* la ecuación de prueba reduce cada paso a una multiplicación por `R(hλ)`; si su módulo es menor o igual que uno el método es estable y se pasa a comprobar la precisión; si no, hay que reducir el paso o cambiar a un método implícito.
- ⚠️ **Error frecuente:** Pensar que un paso más pequeño siempre arregla la precisión sin pagar costo. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.
- 🔗 **Se estudia junto con:** ecuación de prueba, factor de amplificación, estable, región de estabilidad.

📘 **Dónde se aprende** (8 clases): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md); [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md) y 2 más.

### Precisión angular

- La precisión angular es el error típico de una medida de posición, en minutos de arco (′).

💡 **Contexto en la clase [B02-C12](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md):**
- **Idea central (modelo mental):** Un dato sirve en proporción a su incertidumbre conocida.
- 🎯 **Por qué importa:** Una teoría solo es tan buena como los datos con que se contrasta. La pregunta motivadora es: ¿qué diferencia hay entre «mirar el cielo» y «observar sistemáticamente», y por qué esa diferencia cambió la astronomía?
- 🔗 **Se estudia junto con:** observación sistemática, minuto de arco, refracción atmosférica, supernova.

📘 **Dónde se aprende** (1 clase): [B02-C12 · Tycho Brahe y observaciones sistemáticas](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md).

### Precisión de máquina

- La precisión de máquina `u` es la distancia relativa entre 1 y el siguiente número representable (≈ 2,2 × 10⁻¹⁶ en 64 bits).

💡 **Cómo se explica en la clase [B23-C01](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md):**
- Predecir el orden de magnitud del error de redondeo de un cálculo con la precisión de máquina y el *ulp*.
- 🎯 **Por qué importa:** Una prueba con tolerancia muy holgada pasa siempre y no protege nada; una con tolerancia demasiado estricta falla por ruido de redondeo y se termina desactivando. La pregunta motivadora es: ¿cómo elijo una tolerancia que sea lo bastante estricta para detectar un error real y lo bastante amplia para no fallar por redondeo?
- 🔗 **Se estudia junto con:** error absoluto, error relativo, tolerancia, ulp.

📘 **Dónde se aprende** (1 clase): [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md).

### Precisión de medida

- La precisión de medida es la cercanía entre indicaciones obtenidas por mediciones repetidas bajo condiciones especificadas (S1, 2.15); se expresa con una desviación típica o una varianza.

💡 **Contexto en la clase [B13-C03](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md):**
- **Idea central (modelo mental):** Una diana: el centro es el valor verdadero. Los disparos agrupados lejos del centro son precisos y poco veraces; los dispersos alrededor del centro son veraces en promedio y poco precisos; agrupados en el centro, ambas cosas; dispersos y desplazados, ninguna.
- 🎯 **Por qué importa:** Un telémetro láser que mide la distancia a un reflector de prueba puede dar lecturas muy agrupadas pero todas desplazadas: es repetible y, aun así, está mal. Otro puede dar lecturas dispersas que, en promedio, caen sobre el valor correcto.
- 🔗 **Se estudia junto con:** exactitud de medida, veracidad, error de medida, sesgo.

📘 **Dónde se aprende** (1 clase): [B13-C03 · Exactitud frente a precisión](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md).

### Precisión de una amplitud

- La precisión de una amplitud `σ(A)/A = √(2/Σ(2ℓ+1) f_sky)`.

💡 **Cómo se explica en la clase [B40-C15](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de la varianza cósmica*: dispersión, percentiles y precisión de la amplitud.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de la varianza cósmica*: dispersión, percentiles y precisión de la amplitud.
- 🎯 **Por qué importa:** La varianza cósmica es el límite fundamental de la medición del fondo. La decisión central: ¿qué precisión máxima permite el número de modos disponibles?
- 🔗 **Se estudia junto con:** varianza cósmica, grados de libertad, distribución χ², percentil.

📘 **Dónde se aprende** (1 clase): [B40-C15 · Varianza cósmica y límites de las mediciones del fondo](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md).

### Precisión promedio

- La curva de precisión–exhaustividad grafica precisión contra exhaustividad, y la precisión promedio resume su área (S2).

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Pero la precisión promedio, que depende de la prevalencia, es 0,271 (el azar daría 0,01).
- AUC ROC 0,9223 (teoría 0,9214); precisión promedio 0,271; umbral de mínimo costo 1,50 (costo 43 616).
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.
- 🔗 **Se estudia junto con:** matriz de confusión, verdaderos positivos, falsos positivos, verdaderos negativos.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Precisión relativa

- La precisión relativa es el error típico dividido por el valor de la cantidad.

💡 **Cómo se explica en la clase [B12-C14](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md):**
- Predecir el número de muestras para una precisión relativa dada.
- 🎯 **Por qué importa:** Casi ningún modelo de misión admite una fórmula cerrada para la incertidumbre de su salida: hay no linealidades, restricciones y combinaciones de entradas. La simulación Monte Carlo reemplaza el álgebra por repetición: se sortean entradas, se evalúa el modelo y se resume la salida.
- 🔗 **Se estudia junto con:** simulación Monte Carlo, estimador de una probabilidad, generador pseudoaleatorio, semilla.

📘 **Dónde se aprende** (1 clase): [B12-C14 · Simulación Monte Carlo](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md).

### Precisión simple

- La precisión simple (`float32`) es habitual en procesadores de vuelo.

💡 **Cómo se explica en la clase [B74-C18](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md):**
- Con medidas de 5 cm y `P₀` de 10 km, las tres variantes (doble precisión con Joseph, simple con Joseph y simple con la forma simple) terminan con el mismo error rms de `0,0235 m` y un menor autovalor de `P` de `1,55e-09 m²`: no hay diferencia práctica.
- El mismo filtro de 6 estados con medidas de posición de 5 cm termina con `P` de menor autovalor `1,55e-09` con la forma simple en simple precisión, igual que con Joseph.
- 🎯 **Por qué importa:** Una covarianza con un autovalor negativo no es una covarianza: el filtro deja de ser fiable sin avisar. La decisión central: ¿qué formulación numérica y qué coste permite el procesador de a bordo sin perder consistencia?
- 🔗 **Se estudia junto con:** forma de Joseph, rango dinámico, asimetría relativa, coste.

📘 **Dónde se aprende** (1 clase): [B74-C18 · Estimación autónoma a bordo](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md).

### Precisión subpíxel

- La precisión subpíxel es la fracción de píxel con la que se estima.

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- La biblioteca scikit-image implementa el mismo esquema (S1): una correlación por FFT y un refinado subpíxel con precisión `1/upsample_factor`.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».
- 🔗 **Se estudia junto con:** registro, desplazamiento, transformación rígida, afín.

📘 **Dónde se aprende** (1 clase): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md).

### Precisión y exhaustividad

- Repetibilidad: fracción de puntos de una imagen que se detectan también en la otra. Precisión y exhaustividad: ver sección 4.

💡 **Cómo se explica en la clase [B99-C02](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md):**
- Precisión `= correctos/aceptados`; exhaustividad `= correctos/(puntos de A repetidos en B)`.
- Con ruido 6 y razón 0,8, el laboratorio da precisión 94,70 % y exhaustividad 50,46 %: aceptar menos pares da más precisión y menos exhaustividad.
- 🎯 **Por qué importa:** Una esquina de una roca puede verse distinta cuando cambian el brillo, el ruido o el punto de vista, y dos rocas parecidas se confunden. La decisión central: ¿qué puntos conviene usar, cómo se describen y cuándo se acepta un emparejamiento?
- 🔗 **Se estudia junto con:** Característica local, Esquina, Tensor de estructura, Descriptor.

📘 **Dónde se aprende** (1 clase): [B99-C02 · Detección y descriptores de características](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md).

### Precondición

- Tiempo límite: plazo de un paso. Precondición: condición previa.

💡 **Cómo se explica en la clase [B96-C24](../programa/clases/B96/B96-C24-operacion-remota-y-automatizada-de-estaciones/CLASE.md):**
- P3 --> P4["Enviar comando<br/>precondicion: enganche"]
- *Descripción textual:* los cinco pasos se ejecutan en orden; el comando exige el enganche como precondición; un fallo con reintentos agotados aborta y el operador puede cancelar en cualquier paso; ambos terminan en estado seguro.
- ⚠️ **Error frecuente:** Comandar sin precondición. Exige el enganche (8.2)
- 🎯 **Por qué importa:** Un ejecutor automático sin límites puede colgarse o comandar con el enlace caído. La decisión central: ¿qué debe garantizar el ejecutor ante cualquier combinación de fallos y cómo se prueba?
- 🔗 **Se estudia junto con:** Ejecutor, Tiempo límite, Cancelación manual, Propiedad de seguridad.

📘 **Dónde se aprende** (1 clase): [B96-C24 · Operación remota y automatizada de estaciones](../programa/clases/B96/B96-C24-operacion-remota-y-automatizada-de-estaciones/CLASE.md).

### Predicción

- Una predicción es una consecuencia medible de la hipótesis en condiciones declaradas.
- El arco de ajuste es donde hay datos; la predicción es fuera de él.
- La predicción produce `x⁻ = F x` y `P⁻ = F P Fᵀ + Q`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C07](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md):**
- La predicción cuantitativa es `R_pred = d_apogeo/d_perigeo = 1,116`, porque `θ ≈ D/d` y `D` no cambia.
- Fíjate en que la predicción es un número con unidad (adimensional) que no depende de tu cámara.
- ⚠️ **Error frecuente:** Predicción sin número ni unidad. Ejercicio 1.
- 🎯 **Por qué importa:** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.
- 🔗 **Se estudia junto con:** hipótesis, hipótesis alternativa, criterio de refutación, falsable.

📘 **Dónde se aprende** (5 clases): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B58-C11 · Observaciones de seguimiento](../programa/clases/B58/B58-C11-observaciones-de-seguimiento/CLASE.md); [B74-C08 · Filtrado recursivo de estados](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md); [B74-C20 · Validación frente a efemérides de referencia](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md).

### Predicción inversa

- La predicción inversa `F = (V − a)/b` mide una fuerza desconocida.

💡 **Cómo se explica en la clase [B102-C06](../programa/clases/B102/B102-C06-dinamometria-y-medicion-de-fuerzas-de-traccion/CLASE.md):**
- La incertidumbre tipo A de la predicción inversa con una lectura por punto de calibración y `m = 4` lecturas de la medida es `u_A = (σ/b) √(1/m + 1/n + (F − F̄)²/S_xx)`; la tipo B es `u_B = F u_ref` con `u_ref = 5,8 × 10⁻⁴`.
- 🎯 **Por qué importa:** Un tiro de barra de `176,8 N` sin incertidumbre no se puede comparar con un modelo. La decisión central: ¿con qué incertidumbre se mide una fuerza de tracción y qué parte viene del ruido, de la calibración y de la referencia?
- 🔗 **Se estudia junto con:** sensibilidad, ajuste lineal, incertidumbre tipo A, tipo B.

📘 **Dónde se aprende** (1 clase): [B102-C06 · Dinamometría y medición de fuerzas de tracción](../programa/clases/B102/B102-C06-dinamometria-y-medicion-de-fuerzas-de-traccion/CLASE.md).

### Predicción lineal

- La predicción lineal `(p − Z) × s`.

💡 **Cómo se explica en la clase [B43-C17](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md):**
- Una estrella en el meridiano deriva en declinación `0,04375"/s` (`0,04375"/s` en la predicción lineal) por el error de acimut; a 6 h del meridiano, el error de altura da `0,02625"/s`.
- El script [alineacion_polar.py](alineacion_polar.py) simula la deriva con rotaciones de Rodrigues, la compara con la predicción lineal e invierte para estimar el error (comprueba `1 %`).
- 🎯 **Por qué importa:** La alineación polar se corrige midiendo la deriva de una estrella. La decisión central: ¿qué deriva produce un error de acimut o de altura y cómo se invierte para corregirlo?
- 🔗 **Se estudia junto con:** error de acimut, error de altura, método de la deriva, rotación de Rodrigues.

📘 **Dónde se aprende** (1 clase): [B43-C17 · Alineación polar](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md).

### Predictiva a priori

- La predictiva a priori es la distribución de los datos antes de medir: `p(n) = ∫ p(n | λ) p(λ) dλ`.
- La predictiva a priori (C01) es la misma integral con el prior en lugar de la posterior.

💡 **Cómo se explica en la clase [B19-C01](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md):**
- P --> PP["Predictiva a priori<br/>¿qué conteos esperaría?"]
- *Descripción textual:* la física del problema alimenta el prior; del prior se deduce la predictiva a priori, que se revisa y puede devolverte a corregir el prior (flecha de retorno).
- ⚠️ **Error frecuente:** Escoger un prior enorme «para ser prudente». Gamma(0,01; 0,001), ejercicio 10: se detecta con la predictiva a priori.
- 🎯 **Por qué importa:** Un contador de partículas a bordo de un CubeSat registra 3 eventos en 1 hora. ¿Cuál es la tasa verdadera `λ`, en eventos por hora?
- 🔗 **Se estudia junto con:** parámetro, datos, verosimilitud, prior.

📘 **Dónde se aprende** (2 clases): [B19-C01 · Priors físicamente informados](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md); [B19-C06 · Distribución predictiva posterior](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md).

### Predictor

- `s̃ = s_k + h k₁` (predictor: un paso de Euler);

💡 **Cómo se explica en la clase [B11-C06](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md):**
- B --> C["Predictor:<br/>s̃ = s_k + h·k₁"]
- Paso 3 · Predictor. `s̃ = (6 778 100; 76 685,8; −86,76; 7 668,58)`.
- 🎯 **Por qué importa:** Una evaluación de `F` en un cálculo de trayectorias es cara cuando incluye gravedad de varios cuerpos o un modelo de atmósfera. La pregunta práctica es siempre cuánta precisión compra cada evaluación.
- 🔗 **Se estudia junto con:** método de Heun, corrector, pendiente, de dos etapas.

📘 **Dónde se aprende** (1 clase): [B11-C06 · Método de Heun](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md).

### Preferencia de liquidación

- La preferencia de liquidación `1x` da al inversionista el derecho de cobrar primero hasta lo invertido.

💡 **Contexto en la clase [B126-C02](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md):**
- 🎯 **Por qué importa:** El capital de riesgo tiene lógica y condiciones propias que el catálogo no trata. La decisión central: ¿cuánto recibe cada parte en una salida según las condiciones pactadas, y qué retorno cabe esperar de una cartera cuando casi todo el valor viene de pocos casos?
- 🔗 **Se estudia junto con:** Sin participación, Con participación, salida, múltiplo de cartera.

📘 **Dónde se aprende** (1 clase): [B126-C02 · Capital de riesgo en empresas espaciales](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md).

### Prefijo

- Un prefijo (kilo, mega, nano…) multiplica la unidad por una potencia de diez.

💡 **Cómo se explica en la clase [B03-C06](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md):**
- Un prefijo multiplica la unidad: kilo `10³`, mega `10⁶`, giga `10⁹`; mili `10⁻³`, micro `10⁻⁶`, nano `10⁻⁹`.
- Regla importante: el prefijo y el símbolo de la unidad forman un símbolo inseparable;
- ⚠️ **Error frecuente:** Olvidar elevar el prefijo al cubo. Ejercicio 7.
- 🎯 **Por qué importa:** El 23 de septiembre de 1999 la NASA perdió contacto con la sonda Mars Climate Orbiter. Según la agencia, un error de navegación se debió a no traducir unidades inglesas a métricas: el programa en tierra usaba unas y el de la nave otras, y la sonda pasó demasiado cerca de Marte y se quemó en su atmósfera (S1).
- 🔗 **Se estudia junto con:** magnitud, unidad, SI, unidades base.

📘 **Dónde se aprende** (1 clase): [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md).

### Prefijo SI

- Un prefijo SI es un múltiplo de diez con nombre (kilo `10³`, mega `10⁶`, nano `10⁻⁹`;

💡 **Cómo se explica en la clase [B03-C05](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md):**
- El prefijo SI (Mm, nm) sirve para leer una cifra con pocos dígitos en un informe.
- Para cálculos extensos se evita el prefijo y se pasa todo a unidades SI base con potencias de diez, porque mezclar prefijos es una fuente de error.
- 🎯 **Por qué importa:** Las fichas de la NASA publican las masas en «10²⁴ kg»: la Tierra es 5,9722, el Sol 1 988 400. Si no sabes leer ese `10²⁴`, tampoco sabrás si 1 988 400 es «un poco más» o «mucho más».
- 🔗 **Se estudia junto con:** notación científica, mantisa, normalizada, exponente.

📘 **Dónde se aprende** (1 clase): [B03-C05 · Notación científica y órdenes de magnitud](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md).

### Pregunta de revisión

- Una pregunta de revisión es la pregunta que guía la búsqueda («¿qué métodos de búsqueda de períodos se han evaluado con muestreo irregular?»).

💡 **Contexto en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- **Idea central (modelo mental):** Piensa en un embudo de cuatro etapas. Arriba entran todos los resultados que devuelven las consultas; cada etapa descarta algo por una razón que se escribe; abajo queda el conjunto que se leerá.
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.
- 🔗 **Se estudia junto con:** cadena de consulta, operador lógico, criterios de inclusión y exclusión, cribado.

📘 **Dónde se aprende** (1 clase): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md).

### Pregunta investigable

- Una pregunta investigable es una pregunta cuya respuesta puede apoyarse en datos que se pueden obtener.

💡 **Cómo se explica en la clase [B01-C06](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md):**
- Una pregunta es investigable en tu situación cuando cumple, a la vez:
- Una pregunta investigable dice qué dato la contestaría. «¿Cambia el tamaño?» queda contestada por una serie de diámetros angulares en función del día.
- 🎯 **Por qué importa:** «¿Hay vida en otros planetas?» es una pregunta legítima y apasionante, pero nadie puede responderla con un cuaderno y una cámara de teléfono. «¿Cambia el tamaño aparente de la Luna a lo largo de un mes?» sí puede responderse con una cámara y un trípode, y su respuesta enseña algo real sobre la órbita lunar.
- 🔗 **Se estudia junto con:** variable, variable dependiente, independiente, magnitud observable.

📘 **Dónde se aprende** (1 clase): [B01-C06 · Preguntas investigables en astronomía](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md).

### Pre-money

- El pre-money y el post-money son las valoraciones antes y después de la ronda.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- Semilla: 2,0 Mum con pre-money 8,0 ⇒ `8,00` um por acción y 250 000 acciones nuevas (20 %).
- Serie A: 10,0 Mum con pre-money 40,0 ⇒ post-money 50,0; el inversionista recibe el 20 %, la bolsa de opciones el 10 % y los existentes quedan con el 70 %: `1785714,3` acciones posteriores y un precio de `28,0000` um por acción.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?
- 🔗 **Se estudia junto con:** VAN, TIR, MOIC, post-money.

📘 **Dónde se aprende** (1 clase): [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md).

### Preoxigenación

- La preoxigenación es respirar oxígeno antes de bajar la presión.

💡 **Cómo se explica en la clase [B104-C11](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md):**
- La preoxigenación real la define la medicina de la agencia.
- Ejercicio 10 · transferencia. ¿Por qué el modelo no sirve para decidir un tiempo de preoxigenación real?
- 🎯 **Por qué importa:** Un traje presurizado a una fracción de la presión de la cabina deja al nitrógeno disuelto en sobresaturación si no se elimina antes. La decisión conceptual: ¿cómo depende el tiempo de eliminación del nitrógeno del compartimento, de la razón crítica y de la presión de la cabina?
- 🔗 **Se estudia junto con:** tiempo medio, razón crítica, compartimento.

📘 **Dónde se aprende** (1 clase): [B104-C11 · Trajes espaciales](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md).

### Preparado

- Tus archivos pasan por tres estados: modificado (editado, aún no registrado), preparado (*staged*, marcado para el próximo commit) y confirmado (guardado en la base local) (S2).

💡 **Contexto en la clase [B07-C14](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR T["árbol de trabajo<br/>lo que editas"] -->|"git add"| A["área de preparación<br/>lo que irá en el commit"] A -->|"git commit"| H["historial<br/>cadena de commits"] H -->|"git restore"| T ``` *Descripción textual:* tres zonas conectadas en círculo.
- 🎯 **Por qué importa:** Sin control de versiones, un proyecto científico acumula archivos como `analisis_final.py`, `analisis_final2.py` y `analisis_final_ahora_si.py`, y nadie sabe cuál produjo la figura del artículo. Con Git, cada estado importante queda guardado con un mensaje, una fecha y un autor, y puedes comparar o recuperar cualquier versión.
- 🔗 **Se estudia junto con:** repositorio, commit, modificado, confirmado.

📘 **Dónde se aprende** (1 clase): [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md).

### Preprint

- Un preprint es una versión difundida antes de la revisión por pares; puede cambiar.
- Un preprint es un manuscrito difundido antes de su publicación en una revista.
- Un preprint, que difundes antes del arbitraje, no ha pasado por esta evaluación; arXiv describe su proceso como revisión de relevancia y adecuación de lo enviado (S2), lo que a nuestro juicio es una moderación y no un arbitraje científico.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- Un preprint y su artículo publicado son dos registros de la misma obra: conserva uno para el análisis y anota el identificador del otro, para citar la versión que realmente leíste.
- Un preprint no es arbitrado; arXiv describe su proceso como una revisión de relevancia y adecuación de lo enviado (S3), que a nuestro juicio es una moderación y no una evaluación científica por pares (la diferencia se desarrolla en C03).
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.
- 🔗 **Se estudia junto con:** pregunta de revisión, cadena de consulta, operador lógico, criterios de inclusión y exclusión.

📘 **Dónde se aprende** (4 clases): [B01-C19 · Fuentes confiables y desinformación espacial](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md); [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md); [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Preprocesamiento global

- La fuga de datos (*data leakage*) es el uso, al entrenar o ajustar, de información que no estará disponible al predecir (S1). Preprocesamiento global es calcular transformaciones (escala, selección, reducción) con todo el conjunto antes de dividirlo.

💡 **Cómo se explica en la clase [B17-C09](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md):**
- Definir fuga de datos y reconocer sus tres formas más comunes: preprocesamiento global, dependencia temporal y dependencia por fuente.
- 🎯 **Por qué importa:** Un equipo anuncia una exactitud del 95 % para clasificar señales; al aplicarlo a datos de una campaña nueva, baja al 55 %. Nadie mintió: la validación estaba mal hecha.
- 🔗 **Se estudia junto con:** fuga de datos, Pipeline, autocorrelación, grupo.

📘 **Dónde se aprende** (1 clase): [B17-C09 · Prevención de fuga de datos](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md).

### Preregistro

- Un preregistro es un plan fechado y archivado en un registro externo antes de analizar.

💡 **Cómo se explica en la clase [B20-C02](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md):**
- S2 (resumen) afirma que hay estrategias prácticas para aprovechar el preregistro cuando los datos ya existen; el detalle de cada estrategia no se leyó, y no lo enseñamos.
- B --> C["Archivar con fecha: preregistro"]
- 🎯 **Por qué importa:** Un grupo mide cinco variantes razonables de un mismo análisis y publica la que da «un resultado significativo». Nadie mintió con un número, y sin embargo el resultado ya no significa lo que dice.
- 🔗 **Se estudia junto con:** hipótesis de investigación, hipótesis nula, alternativa, variable principal.

📘 **Dónde se aprende** (1 clase): [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md).

### Prescaler

- El prescaler divide el reloj.

💡 **Cómo se explica en la clase [B88-C02](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md):**
- Con prescaler 64 la cuenta es exactamente 250; con prescaler 256 es 62,5 y se redondea a 62 (error −0,8 %).
- Ejercicio 1 · con los pasos indicados. Calcula la cuenta para 100 µs con prescaler 8.
- 🎯 **Por qué importa:** Un error de configuración (un divisor mal calculado, una resolución insuficiente) no se ve en el escritorio y aparece en órbita. La decisión central: ¿qué valores de registro dan la temporización, la velocidad y la resolución que exige el requisito, con qué error?
- 🔗 **Se estudia junto con:** cuenta, divisor, LSB, error de cuantización.

📘 **Dónde se aprende** (1 clase): [B88-C02 · Microcontroladores embarcados](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md).

### Pre-secuencia principal

- Un objeto pre-secuencia principal es una estrella joven que aún se contrae hacia el equilibrio.

💡 **Cómo se explica en la clase [B24-C02](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md):**
- Una estrella joven observada ya puede ser más fría que una enana de la secuencia principal del mismo tipo espectral: las estrellas pre-secuencia principal de tipos G5 a K6 resultan unos `250 K` más frías que las enanas (S3, resumen).
- *Descripción textual:* al contraerse, la energía gravitatoria liberada se reparte: una mitad aumenta la temperatura del gas y la otra sale como luz; si la temperatura central alcanza el umbral de la fusión de hidrógeno, el objeto pasa a la secuencia principal.
- 🎯 **Por qué importa:** Una protoestrella brilla, pero no por el motor que alimenta al Sol. Para saber de dónde sale su energía, cuánto tiempo puede brillar así y cómo distinguirla de una estrella ya estable hay que seguir la energía gravitatoria.
- 🔗 **Se estudia junto con:** protoestrella, energía gravitatoria, teorema del virial, tiempo de Kelvin–Helmholtz.

📘 **Dónde se aprende** (1 clase): [B24-C02 · Formación de protoestrellas](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md).

### Presentación

- La presentación de la reclamación se hace por vía diplomática (art.

💡 **Cómo se explica en la clase [B123-C03](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md):**
- El año de negociación se cuenta desde la presentación: hasta el `2027-11-20` en el primer caso.
- D["Dano"] --> P["Presentacion diplomatica"]
- 🎯 **Por qué importa:** Un derecho a reclamar se pierde o se debilita si no se ejerce por la vía y en el plazo previstos. La decisión central: ¿cuándo y cómo se presenta la reclamación, cuándo se puede pedir una comisión y qué valor tiene su decisión?
- 🔗 **Se estudia junto con:** plazo, comisión de reclamaciones, costos.

📘 **Dónde se aprende** (1 clase): [B123-C03 · Mecanismos de reclamación entre Estados](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md).

### Presión

- La presión es la fuerza normal por unidad de área, `p = F/A`; en el SI, pascal (`1 Pa = 1 N/m²`).
- La densidad `ρ`, la presión `p` y el parámetro `w = p/ρ`.

💡 **Cómo se explica en la clase [B05-C14](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md):**
- Boyle (`T` constante): `p₁V₁ = p₂V₂`; comprimir un gas a un tercio de su volumen triplica su presión.
- Por eso las cabinas se tratan como recipientes a presión: una fuga o una puerta mal cerrada es un problema de ingeniería serio.
- ⚠️ **Error frecuente:** Confundir presión y fuerza. Ejercicios 1 y 8.
- 🎯 **Por qué importa:** La cabina de una nave contiene aire a una presión que debe mantenerse, y una escotilla soporta decenas de miles de newtons. La pregunta motivadora es: ¿qué relaciona presión, volumen, temperatura y cantidad de gas, y cómo cambia la presión con la altura en una atmósfera?
- 🔗 **Se estudia junto con:** milibar, gas ideal, ley de Boyle, densidad.

📘 **Dónde se aprende** (2 clases): [B05-C14 · Gases y presión](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md); [B39-C04 · Tensor de energía-momento y fuentes de curvatura](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md).

### Presión absoluta

- La presión absoluta suma la atmosférica y la hidrostática.

💡 **Cómo se explica en la clase [B104-C15](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md):**
- En el fondo la presión absoluta es de 220,5 kPa (2,18 atm).
- Calcular la presión absoluta a una profundidad dada.
- 🎯 **Por qué importa:** El agua anula el peso neto, pero también se opone al movimiento. La decisión central: ¿qué aspectos de una tarea espacial se pueden entrenar bien en el agua y cuáles quedan distorsionados por la inercia y el arrastre del fluido?
- 🔗 **Se estudia junto con:** flotabilidad neutra, lastre, masa añadida, arrastre.

📘 **Dónde se aprende** (1 clase): [B104-C15 · Entrenamiento subacuático como analogía](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md).

### Presión alveolar

- La presión alveolar `PAO₂` es la presión de O₂ en el alvéolo.

💡 **Cómo se explica en la clase [B117-C04](../programa/clases/B117/B117-C04-problemas-respiratorios-simulados/CLASE.md):**
- *Descripción textual:* la cabina fija la fracción de O₂ inspirada; con la ventilación (CO₂) se obtiene la presión alveolar, después la arterial y la saturación; una fuga reduce `Pb` con el tiempo.
- Paso 2 · Presión alveolar. `0,2105 × (760 − 47) − 40/0,8 = 150,1 − 50 = 100,1 mmHg`.
- ⚠️ **Error frecuente:** Usar la presión total en vez de `Pb − 47` en la ecuación alveolar. Se corrige con 8.1.
- 🎯 **Por qué importa:** Ninguna clase anterior simula problemas respiratorios. La decisión central: ¿cuánto margen de oxigenación hay entre la atmósfera nominal de la cabina y una condición peligrosa, y qué variable lo consume más rápido?
- 🔗 **Se estudia junto con:** fracción inspirada, gradiente alvéolo-arterial, saturación, hipoventilación.

📘 **Dónde se aprende** (1 clase): [B117-C04 · Problemas respiratorios simulados](../programa/clases/B117/B117-C04-problemas-respiratorios-simulados/CLASE.md).

### Presión arterial media

- La presión arterial media es `PAM = GC·RVS` (resistencia vascular sistémica).
- La presión de pulso es `PAS − PAD`; la presión arterial media aproximada `PAM = PAD + (PAS − PAD)/3`.
- La presión arterial media `PAM` es la presión promedio.

💡 **Cómo se explica en la clase [B105-C01](../programa/clases/B105/B105-C01-respuesta-cardiovascular-a-microgravedad/CLASE.md):**
- Calcular gasto cardíaco `GC = FC·VS` y presión arterial media `PAM = GC·RVS` con unidades.
- 🎯 **Por qué importa:** En la Tierra la gravedad empuja la sangre hacia los pies y el sistema cardiovascular lo compensa en cada postura. En microgravedad esa carga desaparece y el cuerpo se reajusta; al volver, la compensación puede no bastar.
- 🔗 **Se estudia junto con:** presión hidrostática, gasto cardíaco, intolerancia ortostática, barorreflejo.

📘 **Dónde se aprende** (3 clases): [B105-C01 · Respuesta cardiovascular a microgravedad](../programa/clases/B105/B105-C01-respuesta-cardiovascular-a-microgravedad/CLASE.md); [B116-C02 · Signos vitales: medición, interpretación y límites](../programa/clases/B116/B116-C02-signos-vitales-medicion-interpretacion-y-limites/CLASE.md); [B117-C03 · Emergencia cardiovascular simulada](../programa/clases/B117/B117-C03-emergencia-cardiovascular-simulada/CLASE.md).

### Presión basal

- La presión basal es `ρ g H`.

💡 **Cómo se explica en la clase [B53-C14](../programa/clases/B53/B53-C14-geologia-de-europa/CLASE.md):**
- *Descripción textual:* El flujo de calor fija el espesor; el espesor decide el número de Rayleigh y la presión basal.
- El script [europa.py](europa.py) calcula `H(q)` por la fórmula y por Simpson, y `Ra` y presión basal (comprueba 10⁻⁹ relativa).
- 🎯 **Por qué importa:** El espesor de la capa de hielo controla qué mide un radar, cómo se fractura la superficie y si el océano se comunica con ella. La decisión central: ¿qué espesor corresponde a un flujo de calor dado y si ese espesor sería conductivo o convectivo?
- 🔗 **Se estudia junto con:** conducción, número de Rayleigh.

📘 **Dónde se aprende** (1 clase): [B53-C14 · Geología de Europa](../programa/clases/B53/B53-C14-geologia-de-europa/CLASE.md).

### Presión central

- La presión central `P_c` es el valor en `r = 0`.

💡 **Cómo se explica en la clase [B24-C04](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md):**
- La presión central es `P_c = 3GM²/(8πR⁴)`.
- Paso 4 · Sentido. Una estrella pequeña necesita una presión central 48 veces mayor que la del Sol uniforme porque es mucho más compacta, aunque tiene menos masa.
- 🎯 **Por qué importa:** Una estrella es una bola de gas que lleva miles de millones de años sin cambiar de tamaño. Eso exige que, en cada capa, la presión hacia fuera compense el peso del gas de encima.
- 🔗 **Se estudia junto con:** equilibrio hidrostático, tiempo dinámico, teorema del virial, densidad uniforme.

📘 **Dónde se aprende** (1 clase): [B24-C04 · Equilibrio hidrostático estelar](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md).

### Presión cinemática

- La presión cinemática `p` es aquí la presión dividida por la densidad.

💡 **Cómo se explica en la clase [B21-C04](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md):**
- Si la densidad es constante y los efectos térmicos no importan, quedan las ecuaciones incompresibles (en 2D, con presión cinemática):
- 🎯 **Por qué importa:** Un fluido aparece en casi toda la ingeniería aeroespacial: el aire alrededor de un cohete, el propelente que se mueve en un tanque, el refrigerante de un satélite.
- 🔗 **Se estudia junto con:** ecuaciones de Navier–Stokes, ecuaciones de Euler, incompresible, viscosidad cinemática.

📘 **Dónde se aprende** (1 clase): [B21-C04 · Ecuaciones de Navier-Stokes y dinámica de fluidos computacional](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md).

### Presión de Casimir

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B31-C19](../programa/clases/B31/B31-C19-vacio-cuantico-y-limites-conceptuales/CLASE.md):**
- *Descripción textual:* la energía de punto cero suma sobre modos; la regularización aísla la parte finita, que produce la presión de Casimir con escala `d⁻⁴`.
- El script [vacio.py](vacio.py) calcula la presión de Casimir y las partes finitas de las sumas (comprueba el escalado `d⁻⁴` a `10⁻¹²` y las partes finitas a `10⁻³`).
- 🎯 **Por qué importa:** Las sumas infinitas de la teoría cuántica de campos exigen regularización, y el vacío tiene consecuencias medibles. La decisión central: ¿cuánto vale la presión de Casimir y qué parte de una suma divergente es física?
- 🔗 **Se estudia junto con:** energía de punto cero, regularización, parte finita, función zeta.

📘 **Dónde se aprende** (1 clase): [B31-C19 · Vacío cuántico y límites conceptuales](../programa/clases/B31/B31-C19-vacio-cuantico-y-limites-conceptuales/CLASE.md).

### Presión de degeneración

- La presión de degeneración es la que ejercen los fermiones por llenar estados de momento alto.
- La presión de degeneración surge del principio de Pauli: los electrones ocupan estados de momento creciente aunque la temperatura sea cero.

💡 **Cómo se explica en la clase [B24-C18](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md):**
- Explicar la presión de degeneración de electrones.
- ⚠️ **Error frecuente:** Creer que la presión de degeneración depende de la temperatura. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** El destino de una estrella es una enana blanca, una estrella de neutrones o un agujero negro; hay una masa límite que separa los dos primeros destinos. Calcularla muestra cómo la mecánica cuántica (presión de degeneración) sostiene a una estrella cuando ya no hay fusión.
- 🔗 **Se estudia junto con:** enana blanca, estrella de neutrones, agujero negro, masa de Chandrasekhar.

📘 **Dónde se aprende** (2 clases): [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md); [B27-C01 · Presión de degeneración](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md).

### Presión de equilibrio

- La presión de equilibrio es la presión del reactivo agotable que daría `ΔG = 0`.

💡 **Cómo se explica en la clase [B56-C13](../programa/clases/B56/B56-C13-biofirmas-quimicas/CLASE.md):**
- Al poner CH₄ en su presión de equilibrio (`10^{−146,3}`, representable en coma flotante), `ΔG` vale `−1,1 × 10⁻¹³ kJ/mol` (cero numérico).
- Hallar la presión de CH₄ de equilibrio con logaritmos.
- 🎯 **Por qué importa:** Una biosfera mantiene en la atmósfera gases que reaccionarían entre sí (como oxígeno y metano) y por eso la composición se aleja del equilibrio. La decisión central: dadas las presiones parciales, ¿cuánta energía libre por mol de CH₄ hay en el desequilibrio CH₄–O₂?
- 🔗 **Se estudia junto con:** biofirma, gas de desequilibrio, desequilibrio químico, falso positivo.

📘 **Dónde se aprende** (1 clase): [B56-C13 · Biofirmas químicas](../programa/clases/B56/B56-C13-biofirmas-quimicas/CLASE.md).

### Presión de pulso

- La presión de pulso es `PAS − PAD`; la presión arterial media aproximada `PAM = PAD + (PAS − PAD)/3`.
- La presión de pulso `PP = VS/C` es la diferencia entre sistólica y diastólica.

💡 **Cómo se explica en la clase [B116-C02](../programa/clases/B116/B116-C02-signos-vitales-medicion-interpretacion-y-limites/CLASE.md):**
- MedlinePlus da para el adulto sano en reposo: pulso 60–100 lpm, frecuencia respiratoria 12–18 resp/min, temperatura 36,5–37,3 °C y presión 90/60 a 120/80 mmHg, y advierte que los valores normales cambian con la edad, el sexo, el peso, la capacidad de ejercicio y la salud general.
- Calcular la presión de pulso y la presión arterial media aproximada.
- 🎯 **Por qué importa:** Un panel que marca en rojo todo lo que sale de «60–100 lpm» genera cientos de marcas por ruido en una persona sana, y puede no ver que un atleta con 52 lpm pasó a 64: sigue «dentro del rango». La decisión central: ¿con respecto a qué se compara una medida y cuánto de la desviación es ruido?
- 🔗 **Se estudia junto con:** signos vitales, rango de referencia, presión arterial media, línea base personal.

📘 **Dónde se aprende** (2 clases): [B116-C02 · Signos vitales: medición, interpretación y límites](../programa/clases/B116/B116-C02-signos-vitales-medicion-interpretacion-y-limites/CLASE.md); [B117-C03 · Emergencia cardiovascular simulada](../programa/clases/B117/B117-C03-emergencia-cardiovascular-simulada/CLASE.md).

### Presión de radiación

- La presión de radiación es la que ejerce la luz atrapada, `aT⁴/3`, con `a = 4σ/c` la constante de radiación.
- La presión de radiación es `P = S/c`.
- La presión de radiación es `I/c` si la luz se absorbe y `2I/c` si se refleja de forma ideal.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C04](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md):**
- Ejercicio 9 · transferencia. Calcula la presión de radiación en el centro solar y su fracción de la presión del modelo.
- Ejercicio 12 · integrador. Elabora tu *ficha de equilibrio de una estrella*: elige `M` y `R` (ilustrativos), calcula `g`, `P_c` uniforme, `T̄` virial y `t_dyn`, compara con el Sol, indica si la presión de radiación importa y qué omite el modelo uniforme.
- 🎯 **Por qué importa:** Una estrella es una bola de gas que lleva miles de millones de años sin cambiar de tamaño. Eso exige que, en cada capa, la presión hacia fuera compense el peso del gas de encima.
- 🔗 **Se estudia junto con:** equilibrio hidrostático, tiempo dinámico, presión central, teorema del virial.

📘 **Dónde se aprende** (4 clases): [B24-C04 · Equilibrio hidrostático estelar](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md); [B37-C02 · Ecuaciones de estado estelares: gas ideal, radiación y degeneración](../programa/clases/B37/B37-C02-ecuaciones-de-estado-estelares-gas-ideal-radiacion-y-degeneracion/CLASE.md); [B72-C08 · Presión de radiación solar](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md); [B78-C12 · Velas solares](../programa/clases/B78/B78-C12-velas-solares/CLASE.md).

### Presión de saturación

- La presión de saturación `p` es la presión a la que el agua líquida y su vapor coexisten a una temperatura dada.

💡 **Cómo se explica en la clase [B64-C02](../programa/clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md):**
- *Descripción textual:* la temperatura entra en un modelo cardinal que da la tasa; de la rama ascendente sale la energía de activación aparente, del máximo la temperatura óptima, y por separado la temperatura fija la presión de saturación que exige el medio.
- Calcular la presión de saturación del agua entre 100 y 121 °C con Clausius–Clapeyron y verificarla por integración numérica.
- 🎯 **Por qué importa:** Un hipertermófilo crece donde casi todo lo demás muere, pero el agua hierve a 100 °C a presión ambiente. La pregunta motivadora: ¿qué fija el límite superior de temperatura de la vida y cómo se mide ese límite?
- 🔗 **Se estudia junto con:** temperaturas cardinales, termófilo, hipertermófilo, energía de activación aparente.

📘 **Dónde se aprende** (1 clase): [B64-C02 · Termófilos e hipertermófilos](../programa/clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md).

### Presión de saturación e_s(T)

- Presión de saturación `e_s(T)`: presión de vapor del aire saturado.

💡 **Cómo se explica en la clase [B106-C07](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md):**
- Calcular la presión de saturación (Magnus), el punto de rocío y la relación de humedad.
- 🎯 **Por qué importa:** Sin convección y con 4 personas, el vapor se acumula, sube la humedad relativa y se condensa en superficies frías. La decisión central: ¿cuánto vapor hay que retirar y con qué superficie fría, sin condensar sobre las paredes?
- 🔗 **Se estudia junto con:** Humedad relativa, Punto de rocío, Relación de humedad w, Carga latente.

📘 **Dónde se aprende** (1 clase): [B106-C07 · Gestión de humedad](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md).

### Presión de sueño

- La presión de sueño `S` sube despierto y baja dormido.

💡 **Cómo se explica en la clase [B104-C17](../programa/clases/B104/B104-C17-gestion-de-fatiga/CLASE.md):**
- Dormir menos deja una presión de sueño mayor al despertar y menos alerta durante el día.
- *Descripción textual:* la presión de sueño sube despierto y baja dormido; el ritmo circadiano la compensa o la agrava; la alerta es su diferencia.
- 🎯 **Por qué importa:** NASA reconoce la pérdida de sueño, la desincronización circadiana y la sobrecarga como un riesgo del vuelo. La decisión conceptual: ¿cuánta alerta se pierde en el trabajo diurno al acortar el sueño unas horas, y por qué el modelo no sustituye a la medición?
- 🔗 **Se estudia junto con:** ritmo circadiano, alerta, deuda de sueño, desincronización circadiana.

📘 **Dónde se aprende** (1 clase): [B104-C17 · Gestión de fatiga](../programa/clases/B104/B104-C17-gestion-de-fatiga/CLASE.md).

### Presión de vapor

- La presión de vapor `P_v(T)` es la presión de equilibrio líquido–vapor.

💡 **Cómo se explica en la clase [B56-C06](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md):**
- Definir punto triple, presión de vapor, temperatura de ebullición y calor latente.
- Calcular la presión de vapor con Clausius–Clapeyron y verificarla integrando la ecuación diferencial.
- 🎯 **Por qué importa:** «Sigue el agua» es una consigna de la exploración, pero tener hielo o vapor no es tener un líquido. La presión y la temperatura mandan.
- 🔗 **Se estudia junto con:** punto triple, temperatura de ebullición, calor latente de vaporización, Clausius–Clapeyron.

📘 **Dónde se aprende** (1 clase): [B56-C06 · Agua líquida y solventes alternativos](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md).

### Presión de vapor del hielo

- La presión de vapor del hielo `p(T)` es la de equilibrio.

💡 **Cómo se explica en la clase [B67-C03](../programa/clases/B67/B67-C03-muestreo-criogenico-y-preservacion-de-volatiles-en-muestras/CLASE.md):**
- La presión de vapor del hielo en el punto triple (`273,16 K`) que da la ecuación es `611,657 Pa`.
- Evaluar la presión de vapor del hielo con la ecuación de Murphy y Koop (2005).
- 🎯 **Por qué importa:** Un error de manipulación de unos grados puede cambiar la pérdida en órdenes de magnitud, porque la presión de vapor del hielo crece exponencialmente con la temperatura. La decisión central: ¿hasta qué temperatura y por cuánto tiempo se puede manipular una muestra sin que la pérdida invalide la medida?
- 🔗 **Se estudia junto con:** flujo de Hertz–Knudsen, presupuesto de pérdida, entalpia de sublimación.

📘 **Dónde se aprende** (1 clase): [B67-C03 · Muestreo criogénico y preservación de volátiles en muestras](../programa/clases/B67/B67-C03-muestreo-criogenico-y-preservacion-de-volatiles-en-muestras/CLASE.md).

### Presión dinámica

- La presión dinámica del viento es `ρv²`.
- La presión dinámica es `q = ρV²/2`.

💡 **Cómo se explica en la clase [B30-C15](../programa/clases/B30/B30-C15-magnetosfera-terrestre/CLASE.md):**
- Con un campo ecuatorial superficial ilustrativo `B₀ = 31 200 nT` y un viento de `5 × 10⁶ m⁻³` a `400 km/s` (presión dinámica `1,338 nPa`) la magnetopausa queda a `10,25 R_⊕`.
- Comprobar el exponente `1/6` de la presión dinámica.
- 🎯 **Por qué importa:** Los satélites geosíncronos están cerca del borde de la magnetosfera cuando el viento es fuerte. La decisión central: ¿dónde está la magnetopausa y qué pasa cuando se comprime?
- 🔗 **Se estudia junto con:** dipolo, capa L, magnetopausa, órbita geosíncrona.

📖 **Explicado a fondo:** [Presión dinámica y Max-Q](esencial/ampliacion-n-z.md#presión-dinámica-y-max-q) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B30-C15 · Magnetosfera terrestre](../programa/clases/B30/B30-C15-magnetosfera-terrestre/CLASE.md); [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md).

### Presión dinámica máxima

- La presión dinámica máxima `q_max` mide la carga del aire.

💡 **Cómo se explica en la clase [B77-C09](../programa/clases/B77/B77-C09-perdidas-aerodinamicas/CLASE.md):**
- Relacionar la pérdida con la presión dinámica máxima y la altitud.
- 🎯 **Por qué importa:** La velocidad final de un ascenso es el `Δv` ideal menos dos pérdidas. La decisión central: ¿cuánto vale la pérdida aerodinámica frente a la gravitacional y de qué depende?
- 🔗 **Se estudia junto con:** pérdida aerodinámica, arrastre, identidad contable, altitud de quemado.

📘 **Dónde se aprende** (1 clase): [B77-C09 · Pérdidas aerodinámicas](../programa/clases/B77/B77-C09-perdidas-aerodinamicas/CLASE.md).

### Presión electrónica

- La presión electrónica `P_e = n_e k T`.

💡 **Contexto en la clase [B45-C14](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md):**
- **Idea central (modelo mental):** Como una escalera con una puerta: con poca energía casi nadie sube al peldaño 2; con demasiada, los átomos salen por la puerta (ionización) y ya no hay quien absorba.
- 🎯 **Por qué importa:** Las líneas de Balmer son más fuertes en estrellas A que en estrellas frías o calientes. La decisión central: ¿por qué hay un máximo de temperatura y cómo se pasa de intensidades a abundancias?
- 🔗 **Se estudia junto con:** ecuación de Boltzmann, ecuación de Saha, función de partición, abundancia.

📘 **Dónde se aprende** (1 clase): [B45-C14 · Composición química por espectros](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md).

### Presión hidrostática

- La presión hidrostática es la que crece con la profundidad (o decrece con la altura) por el peso del fluido.
- La presión hidrostática es `p = gΣ` con `g` constante.
- La presión hidrostática en el fondo es `P = ρ_h g d_h + ρ_a g d_o`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C14](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md):**
- El script [gas_ideal_y_presion.py](gas_ideal_y_presion.py) calcula densidad y número de moléculas, integra con RK4 la presión hidrostática y la compara con `p₀ e^{−z/H}` a 1, 8 y 20 km (< 10⁻⁴), y la fuerza sobre una escotilla.
- 🎯 **Por qué importa:** La cabina de una nave contiene aire a una presión que debe mantenerse, y una escotilla soporta decenas de miles de newtons. La pregunta motivadora es: ¿qué relaciona presión, volumen, temperatura y cantidad de gas, y cómo cambia la presión con la altura en una atmósfera?
- 🔗 **Se estudia junto con:** presión, milibar, gas ideal, ley de Boyle.

📘 **Dónde se aprende** (4 clases): [B05-C14 · Gases y presión](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md); [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md); [B56-C09 · Océanos de Europa](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md); [B105-C01 · Respuesta cardiovascular a microgravedad](../programa/clases/B105/B105-C01-respuesta-cardiovascular-a-microgravedad/CLASE.md).

### Presión inspirada

- La presión inspirada de O₂ es `PIO₂ = FiO₂ (Pb − PH₂O)`.

💡 **Cómo se explica en la clase [B105-C21](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md):**
- *Descripción textual:* la presión y la fracción de oxígeno de la cabina dan la presión inspirada; la ventilación y el CO₂ ambiente fijan el CO₂ alveolar; la ecuación del gas alveolar combina ambos para dar el oxígeno alveolar.
- Calcular la presión inspirada `PIO₂ = FiO₂ (Pb − PH₂O)` y la alveolar `PAO₂` con la ecuación del gas alveolar.
- 🎯 **Por qué importa:** La misma cantidad de oxígeno inspirado no significa lo mismo a 101 kPa que a 70 kPa: importa la presión parcial. La decisión central: ¿qué presión parcial de oxígeno alveolar resulta de una atmósfera dada y cómo cambia con el CO₂ ambiente y la ventilación?
- 🔗 **Se estudia junto con:** ecuación del gas alveolar, altitud equivalente, ppm, hipoventilación.

📘 **Dónde se aprende** (1 clase): [B105-C21 · Fisiología respiratoria en microgravedad y atmósferas de cabina](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md).

### Presión intracraneal

- La presión intracraneal es la presión del líquido cefalorraquídeo (LCR), cuya columna hidrostática depende de la gravedad.

💡 **Cómo se explica en la clase [B105-C05](../programa/clases/B105/B105-C05-cambios-de-vision/CLASE.md):**
- Es un ejemplo del cambio de gradiente, no una medición de presión intracraneal.
- ¿Por qué eso no implica que la presión intracraneal sea cero?
- 🎯 **Por qué importa:** Una variación de décimas de milímetro puede cambiar la refracción en fracciones de dioptría y comparar eso con el error de medida decide si un cambio es real. La decisión central: ¿cuántos milímetros de acortamiento equivalen a una dioptría y cuántas personas la superarían?
- 🔗 **Se estudia junto con:** ojo reducido, desplazamiento hipermetrópico, dioptría, acortamiento axial.

📘 **Dónde se aprende** (1 clase): [B105-C05 · Cambios de visión](../programa/clases/B105/B105-C05-cambios-de-vision/CLASE.md).

### Presión límite

- Ciclado: repetición de ciclos entre dos temperaturas. Presión límite: `Q_gas/S`.

💡 **Cómo se explica en la clase [B90-C12](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md):**
- Una cámara de 2 m³ pasa de 10⁵ a 10 Pa en 368 s con una bomba de desbaste de 0,05 m³/s y de 10 a 10⁻³ Pa en 37,7 s con una de alto vacío de 0,5 m³/s (presión límite 2 × 10⁻⁴ Pa): 6,8 min en total.
- Calcular el tiempo de evacuación de una cámara con dos etapas y la presión límite por gas liberado.
- ⚠️ **Error frecuente:** Ignorar el gas liberado. Fija la presión límite (8.2)
- 🎯 **Por qué importa:** Una nave en órbita baja sufre unos 16 ciclos térmicos por día; no se pueden repetir 5 840 ciclos en tierra. La decisión central: ¿cuántos ciclos de ensayo con mayor amplitud representan un año de órbita y cuánto tarda la campaña?
- 🔗 **Se estudia junto con:** Vacío térmico (TVAC), Bakeout, Ciclado, Factor de aceleración (AF).

📘 **Dónde se aprende** (1 clase): [B90-C12 · Vacío térmico y ciclos](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md).

### Presión magnética

- La presión magnética es `B²/(2μ₀)`.

💡 **Cómo se explica en la clase [B30-C04](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md):**
- *Descripción textual:* el campo da una presión magnética que, por el equilibrio, reduce la presión de gas interior; el contraste y el área dan el déficit de irradiancia.
- Calcular la presión magnética `B²/(2μ₀)` y la presión de gas dentro de la mancha.
- 🎯 **Por qué importa:** Las manchas son la huella visible del campo magnético y las más fáciles de contar. Cuantificar su presión, su brillo y su flujo permite relacionarlas con la irradiancia.
- 🔗 **Se estudia junto con:** umbra, penumbra, contraste, flujo magnético.

📘 **Dónde se aprende** (2 clases): [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md); [B35-C08 · Flujos de plasma estacionarios y balance de presiones](../programa/clases/B35/B35-C08-flujos-de-plasma-estacionarios-y-balance-de-presiones/CLASE.md).

### Presión máxima

- La presión máxima `p₀ = 3F/(2πa²)`.

💡 **Cómo se explica en la clase [B43-C25](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md):**
- Con `100 N` el contacto tiene radio `127,0 µm`, acercamiento `5,375 µm`, presión máxima `2,96 GPa` y rigidez `27,9 N/µm`.
- 🎯 **Por qué importa:** La rigidez del contacto determina cuánto se mueve el eje bajo carga y la frecuencia de resonancia. La decisión central: ¿cuánto se deforma el contacto, cuánta rigidez aporta y qué fracción de la carga soporta la bola más cargada?
- 🔗 **Se estudia junto con:** contacto de Hertz, acercamiento, rigidez, reparto de Stribeck.

📘 **Dónde se aprende** (1 clase): [B43-C25 · Rodamientos y apoyos de precisión en telescopios](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md).

### Presión media de llenado circulatorio

- La presión media de llenado circulatorio `P_mcf` es la presión a la que se equilibra el sistema sin flujo.

💡 **Contexto en la clase [B117-C03](../programa/clases/B117/B117-C03-emergencia-cardiovascular-simulada/CLASE.md):**
- 🎯 **Por qué importa:** Ninguna clase anterior simula una emergencia cardiovascular. La decisión central: ¿qué señales de un modelo simple delatan un problema de circulación y cuáles lo esconden?
- 🔗 **Se estudia junto con:** gasto cardíaco, resistencia vascular sistémica, presión arterial media, presión de pulso.

📘 **Dónde se aprende** (1 clase): [B117-C03 · Emergencia cardiovascular simulada](../programa/clases/B117/B117-C03-emergencia-cardiovascular-simulada/CLASE.md).

### Presión negativa

- La presión negativa es una presión interior menor que la exterior.

💡 **Cómo se explica en la clase [B63-C05](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. ¿Por qué se prefiere presión negativa para contener, y qué falla si el extractor se detiene?
- Ejercicio 11 · transferencia. Transferencia. Proteger a la Tierra (presión negativa) y proteger la muestra de la contaminación terrestre (aire limpio) pueden pedir cosas opuestas.
- 🎯 **Por qué importa:** Contener no es un adjetivo: es un conjunto de diferencias de presión, flujos y filtros que se pueden calcular. La decisión central: ¿qué impide que el aire de la sala salga, y cuánto tarda en limpiarse si se contamina?
- 🔗 **Se estudia junto con:** contención, ACH, mezcla perfecta, eficiencia.

📘 **Dónde se aprende** (1 clase): [B63-C05 · Contención de muestras extraterrestres: instalaciones y principios](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md).

### Presión osmótica

- La presión osmótica `Π` es la presión que debe soportar la membrana.

💡 **Cómo se explica en la clase [B64-C04](../programa/clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md):**
- *Descripción textual:* la sal y su coeficiente osmótico fijan la actividad del agua; de ella salen la presión osmótica y la condición de equilibrio que la célula cumple con KCl o con solutos compatibles.
- Oren [S1] revisa los halófilos de los tres dominios y describe dos estrategias para equilibrar la presión osmótica: acumular concentraciones altas de KCl, lo que exige proteínas adaptadas a la sal, o excluir la sal y acumular solutos orgánicos compatibles.
- 🎯 **Por qué importa:** En una salmuera concentrada el agua existe pero «no está disponible» del mismo modo. La pregunta motivadora: ¿cuánta sal puede haber en el exterior antes de que el agua deje de bastar para la célula?
- 🔗 **Se estudia junto con:** actividad del agua, molalidad, coeficiente osmótico, «salt-in».

📘 **Dónde se aprende** (1 clase): [B64-C04 · Halófilos y vida en salmueras](../programa/clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md).

### Presión parcial

- La presión parcial `p_i = x_i p` es la contribución de cada gas.
- La presión parcial `ppCO₂` es la contribución del CO₂ a la presión total, en mmHg.
- La presión parcial `pᵢ = xᵢ P`.

💡 **Cómo se explica en la clase [B64-C07](../programa/clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md):**
- *Descripción textual:* la mezcla, la presión, el volumen y la temperatura dan los moles y las presiones parciales; de ellos salen el CO₂ disuelto y el oxígeno disponible; el crecimiento logístico da la demanda, que se compara con el oxígeno.
- Calcular moles y presiones parciales de una mezcla de gases con la ley del gas ideal.
- 🎯 **Por qué importa:** Un análogo no es el otro mundo: reproduce algunas variables y deja otras. La pregunta motivadora: ¿qué parte del ambiente real estás imitando, qué parte no y qué puedes concluir de un cultivo en la cámara?
- 🔗 **Se estudia junto con:** cámara análoga, ley de Henry, capacidad de carga, nivel de bioseguridad 1.

📘 **Dónde se aprende** (3 clases): [B64-C07 · Cultivo de extremófilos no patógenos en condiciones análogas](../programa/clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md); [B104-C05 · Sistemas de vehículos tripulados](../programa/clases/B104/B104-C05-sistemas-de-vehiculos-tripulados/CLASE.md); [B114-C03 · Alarmas y procedimientos ante desviaciones atmosféricas](../programa/clases/B114/B114-C03-alarmas-y-procedimientos-ante-desviaciones-atmosfericas/CLASE.md).

### Presión parcial inspirada de O₂ (PIO₂)

- Presión parcial inspirada de O₂ (`PIO₂`): presión de O₂ en el aire inspirado y saturado de vapor.

💡 **Cómo se explica en la clase [B106-C03](../programa/clases/B106/B106-C03-composicion-atmosferica-respirable/CLASE.md):**
- Calcular la presión parcial inspirada de oxígeno `PIO₂ = (P_B − P_H₂O)·F_IO₂`.
- 🎯 **Por qué importa:** El cuerpo no responde a la fracción de oxígeno sino a su presión parcial; bajar la presión total exige subir la fracción, y eso trae riesgo de incendio (C17). La decisión central: ¿qué par presión–composición da normoxia dentro de los límites consultados?
- 🔗 **Se estudia junto con:** Normoxia, Diluyente, Psia, Ebullismo.

📘 **Dónde se aprende** (1 clase): [B106-C03 · Composición atmosférica respirable](../programa/clases/B106/B106-C03-composicion-atmosferica-respirable/CLASE.md).

### Presión solar

- La presión solar da `τ_s = P A (1+ρ_r)(cp−cg)`.

💡 **Cómo se explica en la clase [B87-C18](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md):**
- A `500 km`, con `I = diag(0,35; 0,40; 0,30)`: gradiente de gravedad `184 nN·m`, resistencia `19,1 nN·m`, presión solar `4,10 nN·m` y dipolo residual `498 nN·m`.
- Descripción larga: el dipolo residual y el gradiente de gravedad dominan; la presión solar es dos órdenes menor.
- 🎯 **Por qué importa:** El presupuesto de par decide el tamaño de las ruedas y de los magnetopares. La decisión central: ¿qué perturbación domina, qué error permanente deja en el lazo y se mantiene la estabilidad?
- 🔗 **Se estudia junto con:** gradiente de gravedad, resistencia, dipolo residual, error permanente.

📘 **Dónde se aprende** (1 clase): [B87-C18 · Estabilidad ante perturbaciones](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md).

### Presión térmica

- La presión térmica se escribe `p/k = nT` en `K cm⁻³`;

💡 **Cómo se explica en la clase [B25-C03](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md):**
- El criterio de estabilidad térmica (que explica por qué hay dos fases atómicas) no se desarrolla; solo se comprueba el equilibrio de presión.
- *Descripción textual:* de la más fría y densa a la más caliente y tenue hay cinco fases; las atómicas fría y tibia, y el medio caliente, tienen presión térmica del mismo orden de magnitud.
- ⚠️ **Error frecuente:** Concluir que la presión térmica es la única. Se corrige en 8.5.
- 🎯 **Por qué importa:** Las estrellas nacen del gas y devuelven gas enriquecido; el medio interestelar (MIS) es el almacén y el escenario de ese ciclo. Pero «gas» sirve de poco: un volumen del MIS puede estar a `10 K` o a `10⁶ K`, y su densidad variar un factor 10⁷ de un punto a otro.
- 🔗 **Se estudia junto con:** medio interestelar (MIS), fase, medio neutro frío, medio neutro tibio.

📘 **Dónde se aprende** (1 clase): [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md).

### Presión total

- La presión total `p_t = p + ½ ρ u²` es esa constante.

💡 **Cómo se explica en la clase [B79-C02](../programa/clases/B79/B79-C02-ecuaciones-de-euler-para-flujo-no-viscoso/CLASE.md):**
- La presión total no cambia y la presión estática se recupera por completo: `p(L) − p₁ = 0`.
- Eso es una consecuencia de quitar la viscosidad, no un hecho de la naturaleza; en un Venturi real hay pérdidas de presión total por fricción y desprendimiento.
- 🎯 **Por qué importa:** Las ecuaciones de flujo ideal son la base del análisis de toberas y del reconocimiento de cuándo la viscosidad importa. Sin Euler no se sabe qué ignora cada modelo posterior.
- 🔗 **Se estudia junto con:** ecuaciones de Euler, ecuación de Bernoulli, Venturi.

📘 **Dónde se aprende** (1 clase): [B79-C02 · Ecuaciones de Euler para flujo no viscoso](../programa/clases/B79/B79-C02-ecuaciones-de-euler-para-flujo-no-viscoso/CLASE.md).

### Presión útil

- La presión útil es la fracción de presión del tanque que el regulador puede aprovechar.

💡 **Cómo se explica en la clase [B108-C01](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md):**
- La presión de suministro va de 25,86 MPa a 1,72 MPa, de modo que la fracción útil es `0,9335`.
- Dimensionar el volumen de un tanque con la ley de gas ideal y la presión útil.
- 🎯 **Por qué importa:** B106-C09 trata el soporte vital de hábitat; el del traje no tiene clase. La decisión central: ¿cuánto oxígeno, cuánto calor a rechazar y cuánto CO₂ genera una EVA con un perfil de esfuerzo dado, y qué margen deja el sistema?
- 🔗 **Se estudia junto con:** PLSS, oxígeno, ventilación, térmico.

📘 **Dónde se aprende** (1 clase): [B108-C01 · Sistemas portátiles de soporte vital (PLSS)](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md).

### Presunción protectora

- La presunción protectora es tratar como civil en caso de duda.

💡 **Cómo se explica en la clase [B119-C17](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md):**
- Por norma: presunción protectora (no consultada).
- 🎯 **Por qué importa:** C11 trata los límites militares del tratado; esta clase aborda cómo razonar la distinción bajo incertidumbre, un tema que ninguna clase del bloque cubre y que exige cautela jurídica. La decisión central: ¿cómo cambia el umbral de decisión cuando equivocarse en un sentido es mucho más grave que en el otro?
- 🔗 **Se estudia junto con:** Doble uso, umbral, falso positivo, coste asimétrico.

📘 **Dónde se aprende** (1 clase): [B119-C17 · Conflictos y normas humanitarias aplicables](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md).

### Presupuesto

- El presupuesto es la tabla de todas las contribuciones.
- El presupuesto (de masa, potencia, datos).

💡 **Cómo se explica en la clase [B13-C13](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md):**
- El presupuesto mide el movimiento total de cada palanca y los suma en cuadratura.
- Construir una tabla de presupuesto con la contribución porcentual de cada fuente.
- 🎯 **Por qué importa:** Un telémetro láser mide la distancia a un reflector a unos 10 km. Una mejora costosa del cronómetro podría no servir si la mayor parte de la incertidumbre viene del retardo electrónico o del aire.
- 🔗 **Se estudia junto con:** mensurando, modelo de medida, coeficiente de sensibilidad, incertidumbre combinada.

📘 **Dónde se aprende** (2 clases): [B13-C13 · Presupuestos de incertidumbre](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md); [B47-C02 · Requisitos de instrumentos orbitales](../programa/clases/B47/B47-C02-requisitos-de-instrumentos-orbitales/CLASE.md).

### Presupuesto al 99 %

- El presupuesto al 99 % es la cuantila `q₀,₉₉`.

💡 **Cómo se explica en la clase [B81-C14](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md):**
- Sumar cuantilas sobredimensiona el presupuesto; el RSS lo subdimensiona porque las magnitudes se suman, no sus cuadrados.
- La evidencia es la presupuesto de corrección al 99 % del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un presupuesto muy bajo deja a la nave sin propelente; uno muy alto la lastra. La decisión central: ¿qué cuantila de `Δv` reservar para una o varias correcciones, y cómo se combinan?
- 🔗 **Se estudia junto con:** Δv de corrección, magnitud, suma de cuantilas, raíz de la suma de cuadrados.

📘 **Dónde se aprende** (1 clase): [B81-C14 · Presupuestos de maniobras de corrección](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md).

### Presupuesto de consumibles

- Un presupuesto de consumibles suma lo que se gasta por tarea.

💡 **Cómo se explica en la clase [B104-C10](../programa/clases/B104/B104-C10-actividades-extravehiculares-eva/CLASE.md):**
- La evidencia es la presupuesto de consumibles de una EVA del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *presupuesto de consumibles de una EVA*: perfil por tarea, oxígeno por tarea, percentil 95, margen en horas, comparación con las duraciones consultadas y lista de qué es sintético, estándar e ilustrativo.
- 🎯 **Por qué importa:** El oxígeno de un traje es finito y el trabajo manual consume más que el reposo. La decisión central: ¿cuánto margen queda sobre el consumo esperado si la tasa metabólica de cada tarea varía?
- 🔗 **Se estudia junto con:** tasa metabólica, equivalente energético, percentil 95, esclusa.

📘 **Dónde se aprende** (1 clase): [B104-C10 · Actividades extravehiculares EVA](../programa/clases/B104/B104-C10-actividades-extravehiculares-eva/CLASE.md).

### Presupuesto de datos

- El presupuesto de datos compara lo que se genera con lo que se puede bajar.

💡 **Cómo se explica en la clase [B57-C24](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de una carga útil*: la cadena de requisitos a datos, la geometría óptica y el presupuesto de bajada, con una propuesta explícita de qué relajar si no cierra.
- 🎯 **Por qué importa:** Cada requisito empuja a los demás: más resolución exige más datos, más barrido exige un campo de visión mayor, y el enlace de bajada limita cuánto se puede adquirir. La decisión central: ¿qué requisito se relaja cuando el presupuesto de datos no cierra?
- 🔗 **Se estudia junto con:** carga útil, ciclo de trabajo, focal, campo de visión.

📘 **Dónde se aprende** (1 clase): [B57-C24 · Diseño de una carga útil de observación terrestre](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md).

### Presupuesto de delta-v

- El presupuesto de delta-v es la lista de maniobras con su delta-v.

💡 **Cómo se explica en la clase [B75-C09](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md):**
- La evidencia es tu presupuesto de delta-v con margen del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *presupuesto de delta-v con margen* para una misión Tierra–Venus o Tierra–Marte: fases, determinista, margen, masa inicial y qué es consultado, calculado y sintético.
- 🎯 **Por qué importa:** Un presupuesto de delta-v decide el tamaño del cohete. La decisión central: ¿cuánto delta-v hay que reservar en cada fase y cuánta masa de propulsante implica?
- 🔗 **Se estudia junto con:** margen, delta-v determinista, razón de masa, impulso específico.

📘 **Dónde se aprende** (1 clase): [B75-C09 · Presupuestos de delta-v](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md).

### Presupuesto de diseño

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C20](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md):**
- **Idea central (modelo mental):** Como un presupuesto familiar: cada partida (espejo, plano, enfoque) gasta una parte del error total, y se suman en cuadratura; se mira cuál gasta más.
- 🎯 **Por qué importa:** Un diseño es un conjunto de compromisos. La decisión central: ¿qué apertura y qué focal cumplen el objetivo y qué defecto domina?
- 🔗 **Se estudia junto con:** corrector de coma, Strehl de Maréchal, suma en cuadratura (RSS), aumento mínimo.

📘 **Dónde se aprende** (1 clase): [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md).

### Presupuesto de enlace

- El presupuesto de enlace es el volumen que se puede transmitir.
- El presupuesto de enlace suma ganancias y pérdidas en decibelios.

💡 **Cómo se explica en la clase [B47-C18](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha del enlace de bajada*: presupuesto, margen, BER, Shannon, paso y límites.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha del enlace de bajada*: presupuesto, margen, BER, Shannon, paso y límites.
- 🎯 **Por qué importa:** Los datos que no caben en un paso se pierden o se acumulan. La decisión central: ¿cuántos bits por paso admite el enlace con margen suficiente?
- 🔗 **Se estudia junto con:** pérdida de espacio libre, PIRE, relación G/T, relación C/N₀.

📘 **Dónde se aprende** (3 clases): [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md); [B92-C08 · Márgenes y disponibilidad de enlaces ópticos](../programa/clases/B92/B92-C08-margenes-y-disponibilidad-de-enlaces-opticos/CLASE.md); [B97-C21 · Clasificación y priorización autónoma de muestras a bordo](../programa/clases/B97/B97-C21-clasificacion-y-priorizacion-autonoma-de-muestras-a-bordo/CLASE.md).

### Presupuesto de error

- El presupuesto de error es el tiempo de caída que el SLO tolera.
- Un presupuesto de error suma (o combina en cuadratura) las contribuciones de cada fuente.
- Un presupuesto de error distribuye el error total entre etapas.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C19](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md):**
- *Descripción textual:* con pasos grandes domina el error de truncamiento; con pasos muy pequeños, el de redondeo; el error total tiene un mínimo; el presupuesto compara todas las fuentes para decidir dónde invertir.
- Armar un presupuesto de error con truncamiento, redondeo e incertidumbre de datos.
- 🎯 **Por qué importa:** Un resultado numérico sin cota de error es una cifra sin sentido. Y gastar horas de cálculo para reducir un error de método que ya es menor que la incertidumbre de los datos es un desperdicio.
- 🔗 **Se estudia junto con:** error de truncamiento, error de redondeo, error de modelo, error de datos.

📘 **Dónde se aprende** (6 clases): [B11-C19 · Estimación de error y convergencia](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md); [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md); [B43-C01 · Requisitos ópticos y mecánicos](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md); [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md); [B73-C20 · Proyecto de integración celeste de precisión](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md); [B124-C21 · Acuerdos de nivel de servicio para productos de datos](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md).

### Presupuesto de error de frente de onda

- El presupuesto de error de frente de onda reparte el RMS total entre términos.

💡 **Cómo se explica en la clase [B50-C15](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md):**
- python programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/presupuesto.py
- 🎯 **Por qué importa:** El requisito de un instrumento se cumple o no según cómo se reparta el error entre diseño, fabricación y alineación. La decisión central: ¿cuánto frente de onda se puede gastar en cada etapa sin superar el requisito?
- 🔗 **Se estudia junto con:** conversión superficie–frente de onda, suma cuadrática, margen, Strehl.

📘 **Dónde se aprende** (1 clase): [B50-C15 · Presupuesto de error de frente de onda de un instrumento](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md).

### Presupuesto de fiabilidad

- El presupuesto de fiabilidad reparte la meta entre las funciones.

💡 **Cómo se explica en la clase [B118-C11](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md):**
- La evidencia es la ficha de presupuesto de fiabilidad de disposición del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de presupuesto de fiabilidad de disposición*: tasas, fiabilidad en serie y con redundancia, comparación con la meta de la IADC, tiempo máximo y la lista de qué es consultado, ilustrativo y no consultado.
- 🎯 **Por qué importa:** Una disposición solo es posible si el satélite sigue funcionando al final de su vida. La probabilidad de éxito de la PMD no es la fiabilidad de la misión, sino la de las funciones necesarias para disponer.
- 🔗 **Se estudia junto con:** disposición posmisión, fiabilidad, modo de falla, redundancia.

📘 **Dónde se aprende** (1 clase): [B118-C11 · Diseño para mitigación de desechos](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md).

### Presupuesto de fotones

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B42-C21](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md):**
- **Idea central (modelo mental):** Como buscar una farola en la niebla: solo las más brillantes guían, y hay pocas.
- 🎯 **Por qué importa:** La mayoría del cielo no tiene una estrella brillante cerca: la cobertura limita a la óptica adaptativa natural. La decisión central: ¿hasta qué magnitud corrige el lazo y qué fracción del cielo queda cubierta?
- 🔗 **Se estudia junto con:** punto cero, magnitud límite, ley de cuentas, cobertura de cielo.

📘 **Dónde se aprende** (1 clase): [B42-C21 · Estrellas guía naturales y cobertura de cielo](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md).

### Presupuesto de incertidumbre

- El presupuesto de incertidumbre es la tabla que enumera cada componente, su distribución, su valor, su coeficiente de sensibilidad, su contribución y sus grados de libertad.

💡 **Contexto en la clase [B12-C20](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md):**
- **Idea central (modelo mental):** El presupuesto es un libro contable: cada fuente de duda se anota con su monto (contribución a la varianza), su origen (cómo se evaluó) y su peso en el total. Quien lo audita puede seguir cada partida y volver a sumar. ```mermaid flowchart LR A["1.
- 🎯 **Por qué importa:** Una cifra sin incertidumbre es una opinión; una incertidumbre sin presupuesto es una cifra sin respaldo. Quien revise la misión —otro ingeniero, un cliente o uno mismo dentro de un año— debe poder ver qué componentes se consideraron, cómo se evaluó cada uno, cuál domina y si el requisito se cumple.
- 🔗 **Se estudia junto con:** mensurando, modelo de medida, tipo A, tipo B.

📘 **Dónde se aprende** (1 clase): [B12-C20 · Informe de incertidumbre de una misión](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md).

### Presupuesto de latencia

- ARQ: retransmisión automática. Presupuesto de latencia: suma de retardos de la cadena.

💡 **Cómo se explica en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- Presupuesto de latencia de un telecomando con acuse [s]:
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?
- 🔗 **Se estudia junto con:** Prueba de extremo a extremo, CRC, BER, FER.

📘 **Dónde se aprende** (1 clase): [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### Presupuesto de pérdida

- El presupuesto de pérdida es el tiempo o la temperatura que se permiten para perder una fracción dada.

💡 **Cómo se explica en la clase [B67-C03](../programa/clases/B67/B67-C03-muestreo-criogenico-y-preservacion-de-volatiles-en-muestras/CLASE.md):**
- La evidencia es la ficha del presupuesto de pérdida de una muestra del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha del presupuesto de pérdida de una muestra*: tabla de flujos y tiempos, temperatura máxima, efecto del tamaño y límites del modelo.
- 🎯 **Por qué importa:** Un error de manipulación de unos grados puede cambiar la pérdida en órdenes de magnitud, porque la presión de vapor del hielo crece exponencialmente con la temperatura. La decisión central: ¿hasta qué temperatura y por cuánto tiempo se puede manipular una muestra sin que la pérdida invalide la medida?
- 🔗 **Se estudia junto con:** presión de vapor del hielo, flujo de Hertz–Knudsen, entalpia de sublimación.

📘 **Dónde se aprende** (1 clase): [B67-C03 · Muestreo criogénico y preservación de volátiles en muestras](../programa/clases/B67/B67-C03-muestreo-criogenico-y-preservacion-de-volatiles-en-muestras/CLASE.md).

### Presupuesto de peso

- Un presupuesto de peso es el peso máximo que se acepta.

💡 **Cómo se explica en la clase [B128-C10](../programa/clases/B128/B128-C10-acceso-con-baja-conectividad/CLASE.md):**
- *Descripción textual:* el peso, las peticiones, el ancho de banda y la latencia dan el tiempo; se compara con el presupuesto y se reduce el peso, se agrupan las peticiones o se usa la caché.
- Fijar un presupuesto de tiempo y obtener el peso máximo permitido.
- 🎯 **Por qué importa:** Una persona sin conexión estable queda fuera de un curso aunque los contenidos sean excelentes. La decisión central: ¿cuánto puede pesar una página para cargar a tiempo en la peor conexión del grupo, y qué se puede guardar para no volver a descargarlo?
- 🔗 **Se estudia junto con:** ancho de banda, latencia (RTT), petición, caché.

📘 **Dónde se aprende** (1 clase): [B128-C10 · Acceso con baja conectividad](../programa/clases/B128/B128-C10-acceso-con-baja-conectividad/CLASE.md).

### Presupuesto de sensibilidad

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B46-C20](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md):**
- **Idea central (modelo mental):** Se parte del destino (la sensibilidad), se calcula el consumo (el tiempo) y se añade reserva (la eficiencia) antes de partir.
- 🎯 **Por qué importa:** Un proyecto viable cuadra objetivo, sensibilidad, tiempo y datos. La decisión central: ¿cuánto tiempo de observación pide el objetivo y con qué margen?
- 🔗 **Se estudia junto con:** objetivo científico, criterio de detección, conmutación en posición, eficiencia de observación.

📘 **Dónde se aprende** (1 clase): [B46-C20 · Proyecto de observación radioastronómica](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md).

### Presupuesto de tiempo

- El presupuesto de tiempo es el tiempo de habla menos la reserva.

💡 **Cómo se explica en la clase [B130-C03](../programa/clases/B130/B130-C03-comunicacion-oral-de-la-ciencia/CLASE.md):**
- Calcular el presupuesto de tiempo de una charla con reserva para preguntas.
- Ejercicio 12 · integrador. Integrador. Elabora tu *guion con tiempos y métricas*: presupuesto de tiempo, versión inicial y reescrita con IFSZ y jerga, lista de términos definidos y qué es consultado o ilustrativo.
- 🎯 **Por qué importa:** Presentar ante público requiere técnicas propias; la clase de comunicación escrita general no cubre el tiempo, el ritmo ni la jerga hablada. La decisión central: ¿qué cabe en el tiempo disponible y qué entenderá una persona que oye el guion una sola vez?
- 🔗 **Se estudia junto con:** índice de Szigriszt-Pazos, escala INFLESZ, densidad de jerga.

📘 **Dónde se aprende** (1 clase): [B130-C03 · Comunicación oral de la ciencia](../programa/clases/B130/B130-C03-comunicacion-oral-de-la-ciencia/CLASE.md).

### Presupuesto de velocidad

- El presupuesto de velocidad reparte el `Δv` ideal.

💡 **Cómo se explica en la clase [B77-C20](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *informe de simulación de vuelo*: modelo y datos, eventos, presupuesto de velocidad, estudio de convergencia, comprobaciones de conservación y límites declarados.
- 🎯 **Por qué importa:** Una simulación solo vale si se sabe cuánto error numérico tiene y a dónde va cada metro por segundo. La decisión central: ¿cómo se verifica que una simulación de vuelo es numéricamente fiable y cómo se lee su presupuesto de pérdidas?
- 🔗 **Se estudia junto con:** simulación académica, convergencia en el paso, pérdida por dirección, evento.

📘 **Dónde se aprende** (1 clase): [B77-C20 · Simulación académica de una trayectoria de vuelo](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md).

### Presupuesto RSS

- El presupuesto RSS suma errores independientes.

💡 **Cómo se explica en la clase [B91-C04](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md):**
- Los términos independientes del presupuesto se combinan en un `ε` único.
- Combinar términos independientes de error en un presupuesto RSS.
- 🎯 **Por qué importa:** Una malla desplegable pesa poco y cabe plegada, pero su precisión de forma limita la frecuencia útil. La decisión central: ¿hasta qué frecuencia vale la pena usar un reflector con un error de superficie dado, y qué término del presupuesto de error conviene reducir?
- 🔗 **Se estudia junto con:** error rms de superficie, fórmula de Ruze, frecuencia óptima, malla.

📘 **Dónde se aprende** (1 clase): [B91-C04 · Antenas desplegables y estructuras de gran apertura](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md).

### Prevalencia

- La prevalencia `π` es la fracción de positivos.
- La prevalencia es la fracción de la clase positiva en la población.
- La prevalencia es la proporción de una población con una condición.

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Por la regla de Bayes, la precisión depende de la prevalencia: `precisión = π·TPR/(π·TPR + (1 − π)·FPR)`.
- Con prevalencia 50 %, la precisión sería `0,5/(0,5 + 0,0228) = 0,956`.
- ⚠️ **Error frecuente:** Ignorar la prevalencia al reportar la precisión. Ejercicio 2.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.
- 🔗 **Se estudia junto con:** matriz de confusión, verdaderos positivos, falsos positivos, verdaderos negativos.

📘 **Dónde se aprende** (3 clases): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B109-C08 · Diseño inclusivo en hábitats](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md).

### Previa

- La previa `p` es la probabilidad de vida antes de observar.
- La previa `p0` es la probabilidad de recurso antes de medir.

💡 **Cómo se explica en la clase [B56-C15](../programa/clases/B56/B56-C15-falsos-positivos-de-biofirmas/CLASE.md):**
- Una detección sensible puede dejar la posterior baja si la previa es pequeña y `f` es grande.
- La independencia entre señales (el oxígeno y el ozono dependen del mismo proceso), la incertidumbre sobre `f` y sobre la previa, y el hecho de que `f` depende del contexto planetario.
- ⚠️ **Error frecuente:** Ignorar la previa. Se corrige con la sección 8.3.
- 🎯 **Por qué importa:** Una detección no es una prueba. Si la señal puede producirse por procesos sin vida, su significado depende de cuán frecuentes son.
- 🔗 **Se estudia junto con:** sensibilidad, tasa de falsos positivos, posterior, odds.

📘 **Dónde se aprende** (2 clases): [B56-C15 · Falsos positivos de biofirmas](../programa/clases/B56/B56-C15-falsos-positivos-de-biofirmas/CLASE.md); [B67-C02 · Diseño de un programa de prospección por fases](../programa/clases/B67/B67-C02-diseno-de-un-programa-de-prospeccion-por-fases/CLASE.md).

### Previa difusa

- Una previa difusa tiene una covarianza enorme.

💡 **Cómo se explica en la clase [B74-C08](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md):**
- Con previa difusa y sin ruido de proceso, mínimos cuadrados recursivos y el ajuste por lotes coinciden con diferencia máxima `1,78e-10`.
- Con covarianza muy grande (previa difusa), cuidando la estabilidad numérica.
- 🎯 **Por qué importa:** Una nave en vuelo recibe medidas continuamente y necesita su estado ahora. La decisión central: ¿cuándo es el filtro equivalente al ajuste por lotes, qué añade el ruido de proceso y cómo evito que una previa errónea domine?
- 🔗 **Se estudia junto con:** predicción, corrección, ganancia de Kalman, ruido de proceso.

📘 **Dónde se aprende** (1 clase): [B74-C08 · Filtrado recursivo de estados](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md).

### Previsibilidad

- La previsibilidad es la facilidad de anticipar una maniobra.

💡 **Cómo se explica en la clase [B119-C28](../programa/clases/B119/B119-C28-normas-de-comportamiento-responsable-en-el-espacio/CLASE.md):**
- Por conducta: previsibilidad y consulta.
- Ejercicio 9 · transferencia. Transferencia. ¿Por qué la previsibilidad es relevante para la conducta responsable?
- 🎯 **Por qué importa:** B119-C11 trata límites militares; las normas voluntarias de conducta responsable no tienen clase y se apoyan en conceptos físicos (distancia relativa, deriva, previsibilidad) que esta clase muestra. La decisión central: ¿qué condiciones iniciales mantienen al vecino a distancia constante y cuáles lo hacen derivar o acercarse?
- 🔗 **Se estudia junto con:** movimiento relativo, ecuaciones de Clohessy–Wiltshire, deriva, zona de exclusión.

📘 **Dónde se aprende** (1 clase): [B119-C28 · Normas de comportamiento responsable en el espacio](../programa/clases/B119/B119-C28-normas-de-comportamiento-responsable-en-el-espacio/CLASE.md).

### PRF

- La PRF (frecuencia de repetición de pulsos) es el muestreo del tiempo lento.
- La PRF es la frecuencia de repetición de pulsos.

💡 **Cómo se explica en la clase [B69-C01](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md):**
- El tiempo lento se muestrea a la `PRF`; para no tener aliasing hace falta `PRF ≥ Ba`.
- Una antena más corta ensancha el haz, aumenta `Ba` y mejora la resolución, pero exige una `PRF` mayor, y eso reduce la franja de terreno que puede observarse sin ambigüedad (ejercicio 10).
- 🎯 **Por qué importa:** Sin el principio Doppler, la resolución en azimut de un radar quedaría fijada por el ancho del haz de la antena: a 850 km, una antena de 12 m (λ = 0,0555 m) iluminaría una franja de unos 3,9 km. La decisión central: ¿qué resolución obtiene el sistema, de qué depende y qué hay que muestrear para no perderla?
- 🔗 **Se estudia junto con:** dirección de azimut, alcance oblicuo, apertura sintética, frecuencia Doppler.

📘 **Dónde se aprende** (2 clases): [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md); [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### Prima

- La prima es el precio del seguro.

💡 **Cómo se explica en la clase [B124-C08](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md):**
- Por satélite, `p V = 0,04 · 300 = 12` um y la prima con recargo del 35 % es `16,20` um.
- Para 20 satélites la prima total es `324,0` um frente a una pérdida esperada de `240,0`: ganancia esperada `84,0` um.
- 🎯 **Por qué importa:** El seguro no elimina el riesgo: lo traslada a quien puede juntarlo. La decisión central: ¿cuánto cobrar por cubrir un riesgo y con qué probabilidad el asegurador se queda sin capital?
- 🔗 **Se estudia junto con:** pérdida esperada, recargo, capital, ruina.

📘 **Dónde se aprende** (1 clase): [B124-C08 · Seguros y riesgo espacial](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md).

### Prima pura

- La prima pura es la pérdida esperada.
- La prima pura es `E[S]`.

💡 **Cómo se explica en la clase [B127-C01](../programa/clases/B127/B127-C01-seguros-de-lanzamiento/CLASE.md):**
- PP --> PC["prima comercial = prima pura x (1 + recargo)"]
- *Descripción textual:* los resultados con su probabilidad y su pago dan la tasa pura; multiplicada por el valor asegurado es la prima pura; el recargo da la comercial; una simulación comprueba la cuenta.
- ⚠️ **Error frecuente:** Confundir prima pura con prima comercial. Se corrige con 8.1–8.2.
- 🎯 **Por qué importa:** B124-C08 presenta el riesgo y los seguros en general; el seguro de lanzamiento tiene estructura y coberturas propias. La decisión central: ¿qué prima es coherente con la probabilidad de fallo y qué parte de ella es recargo?
- 🔗 **Se estudia junto con:** valor asegurado, tasa, recargo, pérdida parcial.

📘 **Dónde se aprende** (2 clases): [B127-C01 · Seguros de lanzamiento](../programa/clases/B127/B127-C01-seguros-de-lanzamiento/CLASE.md); [B127-C05 · Evaluación actuarial básica del riesgo espacial](../programa/clases/B127/B127-C05-evaluacion-actuarial-basica-del-riesgo-espacial/CLASE.md).

### Primer cruce

- El primer cruce de la barrera `δc`.

💡 **Contexto en la clase [B36-C06](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md):**
- **Idea central (modelo mental):** Es como una piscina con un borde: el agua (la densidad) sube al azar y la fracción de caminos que alguna vez pasan el borde es la fracción de masa en halos.
- 🎯 **Por qué importa:** Contar halos exige un umbral de colapso y una función de masa. La decisión central: ¿cuánta masa del universo está en halos de más de cierta masa?
- 🔗 **Se estudia junto con:** umbral de colapso, altura, fracción de masa, función de masa.

📘 **Dónde se aprende** (1 clase): [B36-C06 · Formación de halos y función de masa](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md).

### Primer impulso

- El primer impulso es el de la salida.
- El primer impulso es `Δv1 = v0⁺ − v0`.

💡 **Cómo se explica en la clase [B75-C22](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md):**
- La NASA describe la transferencia de Hohmann como la ruta de menor propulsante [S4]; aquí se comprueba para el primer impulso.
- python programa/clases/B75/B75-C22-modelos-de-primer-impulso/primer_impulso.py
- 🎯 **Por qué importa:** Antes de optimizar toda la misión conviene entender el primer impulso. La decisión central: ¿qué módulo y qué dirección del primer impulso alcanzan un radio dado con el menor delta-v y en cuánto tiempo?
- 🔗 **Se estudia junto con:** dirección, familia tangencial, apoapsis alcanzado, tiempo hasta el apoapsis.

📘 **Dónde se aprende** (2 clases): [B75-C22 · Modelos de primer impulso](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md); [B76-C12 · Guiado relativo](../programa/clases/B76/B76-C12-guiado-relativo/CLASE.md).

### Primer modo

- El primer modo es la forma de vibrar de menor frecuencia, `f1`.

💡 **Cómo se explica en la clase [B86-C03](../programa/clases/B86/B86-C03-arreglos-fotovoltaicos-desplegables/CLASE.md):**
- Plegado ocupa `0,085 m` de altura y, desplegada, cada ala vibra a `4,059 Hz` en su primer modo de flexión.
- 🎯 **Por qué importa:** El ala es el mayor elemento del satélite y su geometría define la potencia, el volumen de lanzamiento y la dinámica. Un ala mal orientada pierde potencia con el coseno y un ala demasiado flexible interactúa con el control de actitud.
- 🔗 **Se estudia junto con:** panel, ala, desplegado, potencia específica.

📘 **Dónde se aprende** (1 clase): [B86-C03 · Arreglos fotovoltaicos desplegables](../programa/clases/B86/B86-C03-arreglos-fotovoltaicos-desplegables/CLASE.md).

### Primer orden

- Una reacción de primer orden `A → productos` tiene velocidad `v = −d[A]/dt = k[A]`, con `k` la constante de velocidad (en 1/s).

💡 **Cómo se explica en la clase [B06-C14](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md):**
- Se trabajó con un solo paso de primer orden, a temperatura constante y sin reacción inversa.
- Calcular concentración, fracción restante y vida media en un proceso de primer orden.
- 🎯 **Por qué importa:** Que una reacción sea posible (energía favorable, `K` grande) no significa que ocurra: puede ser tan lenta que no ocurra nunca en la edad del universo. En una nube molecular a 10 K, la energía térmica es de apenas 0,86 meV (C10).
- 🔗 **Se estudia junto con:** velocidad de reacción, constante de velocidad, vida media, energía de activación.

📘 **Dónde se aprende** (1 clase): [B06-C14 · Cinética química inicial](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md).

### Primera variación

- La primera variación `δJ = dJ(u + εη)/dε` en `ε = 0`.

💡 **Cómo se explica en la clase [B81-C08](../programa/clases/B81/B81-C08-validacion-de-trayectorias-de-empuje-continuo/CLASE.md):**
- El balance de energía valida la integración numérica; la convergencia de RK4 valida el orden del integrador; la primera variación valida que el control es un punto estacionario.
- *Descripción textual:* la trayectoria se reintegra con dos métodos, se verifica el balance de energía y la convergencia, se comprueba la primera variación del coste y todo se resume en un informe.
- 🎯 **Por qué importa:** Un resultado que solo se ha verificado con el mismo código no está validado. La decisión central: ¿qué chequeos independientes demuestran que una trayectoria de empuje continuo es correcta y que es un óptimo local?
- 🔗 **Se estudia junto con:** trabajo del empuje, orden, admisible.

📘 **Dónde se aprende** (1 clase): [B81-C08 · Validación de trayectorias de empuje continuo](../programa/clases/B81/B81-C08-validacion-de-trayectorias-de-empuje-continuo/CLASE.md).

### Principio de desviación estándar

- El principio de desviación estándar cobra `E[S] + k·sd[S]`.

💡 **Cómo se explica en la clase [B127-C05](../programa/clases/B127/B127-C05-evaluacion-actuarial-basica-del-riesgo-espacial/CLASE.md):**
- Fijar una prima con el principio de desviación estándar.
- Prima por principio de desviacion estandar (k = 0.5) = 119.206 MUSD ; recargo = 75.1%
- 🎯 **Por qué importa:** Estimar primas y pérdidas requiere nociones actuariales; B12 trata estadística sin su aplicación a seguros.
- 🔗 **Se estudia junto con:** frecuencia, severidad, exposición, pérdida agregada.

📘 **Dónde se aprende** (1 clase): [B127-C05 · Evaluación actuarial básica del riesgo espacial](../programa/clases/B127/B127-C05-evaluacion-actuarial-basica-del-riesgo-espacial/CLASE.md).

### Principio de discrepancia

- El principio de discrepancia elige `λ` de modo que el residuo iguale el tamaño esperado del ruido.
- El principio de discrepancia elige `λ` con residuo igual al ruido.

💡 **Cómo se explica en la clase [B22-C02](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md):**
- Elegir `λ` por el principio de discrepancia y por el vértice de la curva L, y compararlos.
- 🎯 **Por qué importa:** Si no puedes confiar en `x = A⁻¹ b` y no puedes bajar el ruido a voluntad, necesitas una regla que ignore lo que los datos no pueden decir. Esa regla debe tener una perilla: cuánto ignorar.
- 🔗 **Se estudia junto con:** solución regularizada, desajuste, penalización, parámetro de regularización.

📘 **Dónde se aprende** (2 clases): [B22-C02 · Regularización de Tikhonov](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md); [B37-C10 · Inversión asterosísmica de perfiles internos](../programa/clases/B37/B37-C10-inversion-asterosismica-de-perfiles-internos/CLASE.md).

### Principio de equivalencia de Einstein (local)

- El principio de equivalencia de Einstein (local) dice que, en una región pequeña, los efectos de un campo gravitatorio son indistinguibles de los de una aceleración.

💡 **Contexto en la clase [B26-C06](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md):**
- **Idea central (modelo mental):** Dentro de un ascensor sin ventanas no puedes decir si estás parado en la Tierra o si un cohete te acelera con `a = g`. Un haz de luz que sube desde el piso llega al techo con la frecuencia reducida porque el techo, que acelera, se aleja del haz.
- 🎯 **Por qué importa:** Los relojes de los satélites de navegación van a un ritmo ligeramente distinto de los terrestres, y un maser en una torre ve su frecuencia cambiar con la altura. Todo eso se deduce de la equivalencia entre aceleración y gravedad.
- 🔗 **Se estudia junto con:** principio de equivalencia (débil), marco en caída libre, corrimiento gravitacional al rojo, aceleración del cohete.

📘 **Dónde se aprende** (1 clase): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md).

### Principio de equivalencia (débil)

- El principio de equivalencia (débil) dice que todos los cuerpos caen con la misma aceleración en un campo gravitatorio.

💡 **Cómo se explica en la clase [B26-C06](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md):**
- Enunciar el principio de equivalencia en su forma local.
- El principio de equivalencia dice que el efecto es universal: depende de `g` y `h`, no del material (el valor se verifica con el cohete, 8.3).
- 🎯 **Por qué importa:** Los relojes de los satélites de navegación van a un ritmo ligeramente distinto de los terrestres, y un maser en una torre ve su frecuencia cambiar con la altura. Todo eso se deduce de la equivalencia entre aceleración y gravedad.
- 🔗 **Se estudia junto con:** principio de equivalencia de Einstein (local), marco en caída libre, corrimiento gravitacional al rojo, aceleración del cohete.

📘 **Dónde se aprende** (1 clase): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md).

### Principio de Fermat

- El principio de Fermat: el tiempo de tránsito es estacionario.

💡 **Cómo se explica en la clase [B41-C01](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md):**
- Aplicar el principio de Fermat con una búsqueda numérica.
- 🎯 **Por qué importa:** Sin un modelo de rayos no se puede diseñar un telescopio. La decisión central: ¿cuándo basta con rayos y cuánto tarda la luz en cada medio?
- 🔗 **Se estudia junto con:** rayo, índice de refracción, camino óptico, medio homogéneo e isótropo.

📘 **Dónde se aprende** (1 clase): [B41-C01 · Naturaleza y propagación de la luz](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md).

### Principio de Franck-Condon

- El principio de Franck-Condon dice que, como los núcleos son mucho más lentos que los electrones, la transición electrónica ocurre a geometría fija («vertical»).

💡 **Cómo se explica en la clase [B62-C03](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md):**
- Enunciar el principio de Franck-Condon y la aproximación de Condon.
- 🎯 **Por qué importa:** Las bandas electrónicas aparecen en el ultravioleta y el visible; su forma, una serie de picos, revela cuánto cambia la geometría de la molécula. La decisión central: ¿qué picos de la progresión serán intensos?
- 🔗 **Se estudia junto con:** factor de Franck-Condon, aproximación de Condon, factor de Huang-Rhys, progresión.

📘 **Dónde se aprende** (1 clase): [B62-C03 · Transiciones electrónicas moleculares](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md).
