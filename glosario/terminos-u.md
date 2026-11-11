# Términos · U

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · **U** · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### U

- Las U miden el volumen del satélite.

🎯 **Por qué importa (clase B78-C11):** Un propulsor de alto `Isp` ahorra propelente pero empuja poco y tarda semanas; uno de empuje alto gasta más volumen de propelente. La decisión central: ¿qué tecnología cumple un Δv dado con una masa, un volumen y una potencia que un CubeSat sí puede dar?

📘 **Dónde se aprende** (1 clase): [B78-C11 · Micropropulsión para CubeSat](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md).

### UA

- La UA es la unidad astronómica.

💡 **Cómo se explica en la clase [B89-C04](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md):**
- Pasar de X a Ka a 2,5 UA cuesta `11,617 dB` más de espacio libre (`20 log₁₀(32/8,4)`).
- A la Luna (384 400 km) la pérdida en banda X es de `222,63 dB` y la luz tarda `1,282 s`; a Neptuno (30 UA) la pérdida es de `303,97 dB` y el viaje de ida dura `4,16 h`.
- 🎯 **Por qué importa:** La pérdida de espacio libre domina cualquier presupuesto de enlace de espacio profundo y fija la potencia, la ganancia y el tiempo de ida y vuelta que tendrá una misión. La decisión central: ¿cuántos decibelios se pierden entre transmisor y receptor y cuánto tarda la señal en llegar?

📘 **Dónde se aprende** (1 clase): [B89-C04 · Propagación y pérdidas de espacio libre](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md).

### UFC

- Espora: forma latente resistente. UFC: unidad formadora de colonias.
- UFC: unidad formadora de colonia.

💡 **Cómo se explica en la clase [B106-C28](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md):**
- Si se muestrea cada 24 h la población llega a 3,3 UFC/mL; cada 72 h, 36,6; cada 168 h, 4427, sobre el umbral.
- Con una contaminación de 0,01 UFC/mL (1 UFC por 100 mL) y una recuperación de 0,7, una muestra de 100 mL la detecta con probabilidad 0,503 y una de 1000 mL con 0,9991.
- 🎯 **Por qué importa:** Una muestra pequeña puede no contener ningún organismo de una contaminación real, y un muestreo espaciado deja crecer la población. La decisión central: ¿qué volumen y qué intervalo de muestreo dan una confianza dada de detectar una contaminación antes de que supere el umbral de acción?

📘 **Dónde se aprende** (2 clases): [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md); [B106-C28 · Monitoreo microbiológico de agua y superficies del hábitat](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md).

### UHF

- Las bandas VHF (~145 MHz), UHF (~401 MHz), S (~2,2 GHz), X (~8,4 GHz) y Ka (~32 GHz) se tratan aquí con frecuencias centrales ilustrativas.

💡 **Cómo se explica en la clase [B89-C03](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md):**
- La ganancia es `1,4` dBi en VHF, `10,3` en UHF, `25,0` en S, `36,7` en X y `48,3` en Ka; el haz pasa de `144,7°` a `0,66°`.
- De UHF a X, `20 log₁₀(8400/401) = 26,423 dB`; el laboratorio obtiene `26,423 dB`: la misma cifra, porque la ganancia depende de `f²`.
- 🎯 **Por qué importa:** Elegir la banda es la primera decisión de diseño de un enlace y determina el tamaño de la antena y la tasa alcanzable. La decisión central: ¿qué banda usar para una ganancia de antena dada y qué se paga en apuntamiento por usarla?

📘 **Dónde se aprende** (1 clase): [B89-C03 · Bandas VHF UHF S X Ka](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md).

### UKF

- El UKF la aplica a la propagación y a la medida.

💡 **Cómo se explica en la clase [B74-C10](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md):**
- En 400 casos el error rms es casi idéntico: `295,61 km` (EKF), `295,53 km` (UKF) y `296,67 km` (Bayes), porque la previa domina.
- La diferencia está en la covarianza: el NEES medio vale `7,359` para el EKF (sobreconfiado, 3,7 veces el esperado), `1,995` para el UKF y `2,070` para la referencia.
- 🎯 **Por qué importa:** Un filtro puede dar una estimación aceptable y una covarianza falsa. La decisión central: ¿cuándo basta el EKF y cuándo la covarianza obliga a usar un filtro no lineal, y cómo lo verifico con una referencia?

📘 **Dónde se aprende** (1 clase): [B74-C10 · Filtro de Kalman no lineal](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md).

### Ulp

- El ulp (unidad en el último lugar) es ese espaciado a una magnitud dada; vale `2⁻⁵² · 2^e` para un número en `[2^e, 2^{e+1})`.
- El ulp (*unit in the last place*, S2) de un número es la distancia al siguiente representable: crece con el tamaño del número.

💡 **Cómo se explica en la clase [B11-C25](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md):**
- El ulp vale `2,2 × 10⁻¹⁶` en 1, `1,5 × 10⁻⁸` en `10⁸` y `2` en `10¹⁶`: por eso `10¹⁶ + 1 = 10¹⁶`.
- Paso 2 · Resolución. El ulp en `7 × 10⁶` es `9,3 × 10⁻¹⁰ m`: las diferencias de `10⁻¹³` ni siquiera son representables.
- 🎯 **Por qué importa:** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.

📘 **Dónde se aprende** (2 clases): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md); [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md).

### Ultra alto vacío (UHV)

- El ultra alto vacío (UHV) es el régimen de presiones por debajo de `10⁻⁹` mbar, donde el gas residual casi no cubre la superficie durante un experimento.

💡 **Cómo se explica en la clase [B68-C04](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md):**
- Los experimentos de las clases anteriores se hacen en cámaras de ultra alto vacío con una superficie enfriada a 10–18 K.
- python programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/montaje_uhv.py
- 🎯 **Por qué importa:** Un hielo de 10 ML de CO sobre una superficie a 10 K se contamina con agua residual en horas si la presión de fondo no es lo bastante baja, y una TPD con bombeo insuficiente deforma el pico que se mide.

📘 **Dónde se aprende** (1 clase): [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### Ultrarrelativista

- El régimen no relativista es `x ≪ 1`; el ultrarrelativista, `x ≫ 1`.

💡 **Cómo se explica en la clase [B27-C01](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md):**
- Descripción larga: la fórmula no relativista sirve para `x` pequeño y la ultrarrelativista para `x` grande; en el medio ninguna de las dos basta.
- Reconocer los límites no relativista (`P ∝ n^{5/3}`) y ultrarrelativista (`P ∝ n^{4/3}`).
- 🎯 **Por qué importa:** Una estrella sin fusión no se desploma porque los electrones (o neutrones) no pueden apretarse más allá de lo que permite el principio de exclusión, aunque la temperatura sea cero. La decisión central: dada la densidad de un gas degenerado, ¿cuánto vale el momento de Fermi, la presión y cuál de los dos límites aplica?

📘 **Dónde se aprende** (1 clase): [B27-C01 · Presión de degeneración](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md).

### Ultrasonido

- El ultrasonido son ondas sonoras de más de 20 kHz; el ecógrafo emite pulsos y mide los ecos.

💡 **Cómo se explica en la clase [B116-C06](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md):**
- Las páginas de la NASA sobre el sistema flexible de ultrasonido y sobre Ultrasound-2 no se consultaron (la primera no respondió a la lectura y la segunda dio error 404); lo que de ellas se sabe viene de un resumen de búsqueda no verificado.
- python programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/ecografo.py
- 🎯 **Por qué importa:** Un equipo no es solo su ficha técnica: lo que ve depende de la frecuencia elegida, quién lo maneja, cuánto entrena y qué retardo tiene el apoyo experto. Y una prueba con buenos números de sensibilidad y especificidad puede dar mayoría de falsos positivos si la condición es rara.

📘 **Dónde se aprende** (1 clase): [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### Ultratenues

- Una galaxia enana es una galaxia de baja masa y luminosidad; las enanas esferoidales (dSph) son pobres en gas y se sostienen por agitación; las ultratenues son las menos luminosas.

💡 **Cómo se explica en la clase [B25-C10](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md):**
- S2 ubica el mínimo en `≈ 3` y el máximo en `≈ 3200` para ultratenues: un valor de `27` está entre ambos.
- 🎯 **Por qué importa:** Las galaxias enanas son las más abundantes y las más ricas en materia oscura según su masa dinámica; además son los sitios donde las predicciones del modelo cosmológico se ponen a prueba. Pero con pocas estrellas medidas y sin rotación ordenada, su masa depende de un estimador.

📘 **Dónde se aprende** (1 clase): [B25-C10 · Galaxias irregulares y enanas](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md).

### Ultravioleta

- El ultravioleta (aquí 91–300 nm).

💡 **Cómo se explica en la clase [B47-C03](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md):**
- Lectura. Cae en el ultravioleta lejano, absorbido por el aire.
- La evidencia es la ficha del telescopio ultravioleta del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** En el ultravioleta cada fotón es valioso: las tasas son bajas y el ruido es de Poisson. La decisión central: ¿cuánto hay que exponer para llegar a una relación señal/ruido de 10?

📘 **Dónde se aprende** (1 clase): [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md).

### U.m

- El regreso es la reclamación entre responsables. u.m. es la unidad monetaria sintética.

💡 **Cómo se explica en la clase [B119-C03](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md):**
- Culpas 0,7 y 0,3: cuotas internas `A = 70.0` y `B = 30.0` u.m.; la víctima puede cobrar los 100 de A o de B.
- Si A no puede pagar, B paga `100.0` u.m. a la víctima; su cuota interna es `30.0`; reclama a A el regreso de `70.0` u.m.
- 🎯 **Por qué importa:** El art. VII del tratado de 1967 (no discutido en la fuente de C01) fundamenta la responsabilidad; el convenio de 1972 la desarrolla, y la cuantificación del daño se trata en el bloque de reclamaciones (B123); esta clase fija la regla de reparto.

📘 **Dónde se aprende** (1 clase): [B119-C03 · Convenio de Responsabilidad](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md).

### Umbra

- La umbra es la zona de sombra total, de donde el Sol queda completamente cubierto; la penumbra es la zona de sombra parcial que la rodea.
- La umbra es la parte central oscura.

💡 **Cómo se explica en la clase [B08-C09](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md):**
- Con triángulos semejantes, la umbra tiene longitud `L = R_L · D / (R_S − R_L)`, donde `R_L = 1737,4 km` (S4), `R_S = 695 700 km` (S5) y `D ≈ 149,6 × 10⁶ km` (S5, distancia media).
- El radio de la umbra de la Tierra a una distancia `x` es `R⊕ − x (R_S − R⊕)/D`.
- 🎯 **Por qué importa:** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?

📘 **Dónde se aprende** (2 clases): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md); [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md).

### Umbral

- Un umbral es la energía mínima para un proceso (ionizar, evaporar, superar una barrera); dado un umbral `E_u`, la longitud de onda umbral es `λ_u = h c/E_u`, y sólo fotones con `λ ≤ λ_u` lo superan.
- Un umbral es el valor que separa dos casos.
- El umbral es el valor del descriptor que separa las dos clases.
- *(y 19 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C18](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md):**
- El umbral para ionizar el hidrógeno desde el estado fundamental es `λ = 1239,84/13,5984 = 91,175 nm`; por otro camino, `1/R_H = 91,176 nm` (C01): ambos coinciden a 0,001 nm, lo que valida las constantes y la energía de la NIST.
- Esta clase no da límites de dosis ni umbrales numéricos de daño, porque no se consultó una fuente reguladora; para ellos hay que acudir a los organismos competentes.
- ⚠️ **Error frecuente:** Creer que el umbral energético basta. Se corrige con la sección 5 y la 7.
- 🎯 **Por qué importa:** El hidrógeno de una nube o de una atmósfera puede ser ionizado por un fotón de longitud de onda menor que 91,2 nm. Un fotón de Lyman-alfa (121,6 nm) no lo ioniza desde el estado fundamental, pero tiene 22 veces la energía necesaria para evaporar una molécula de agua.

📘 **Dónde se aprende** (23 clases): [B06-C18 · Fotoquímica y radiación](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md); [B07-C04 · Condicionales y decisiones](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md); [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B25-C16 · Retroalimentación estelar](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B28-C09 · Alertas científicas en tiempo real](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md) y 17 más.

### Umbral de acción

- Crecimiento logístico: curva en S. Umbral de acción: nivel que exige respuesta.

💡 **Cómo se explica en la clase [B106-C28](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md):**
- Calcular el crecimiento logístico y el tiempo hasta el umbral de acción.
- Ejercicio 11 · transferencia. ¿Qué datos necesitas para fijar el umbral de acción?
- 🎯 **Por qué importa:** Una muestra pequeña puede no contener ningún organismo de una contaminación real, y un muestreo espaciado deja crecer la población. La decisión central: ¿qué volumen y qué intervalo de muestreo dan una confianza dada de detectar una contaminación antes de que supere el umbral de acción?

📘 **Dónde se aprende** (1 clase): [B106-C28 · Monitoreo microbiológico de agua y superficies del hábitat](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md).

### Umbral de alarma

- Dilución: menor concentración por más caudal. Umbral de alarma: concentración que activa el detector.

💡 **Cómo se explica en la clase [B106-C17](../programa/clases/B106/B106-C17-prevencion-y-respuesta-a-incendios/CLASE.md):**
- *Descripción textual:* el combustible libera calor, produce gases y humo; el humo se diluye con la ventilación y suena la alarma si supera el umbral.
- Con 0,6 m³/s de ventilación y 2 mg/s de humo, una alarma de 1 mg/m³ suena en 59 s; con más de 2,0 m³/s el humo se diluye bajo el umbral y no suena.
- 🎯 **Por qué importa:** Un incendio en una cabina cerrada no puede salir al exterior: calienta, sube la presión, consume oxígeno y produce CO₂ y humo. La decisión central: ¿qué efectos tiene una cantidad dada de combustible y con qué tiempo y ventilación se puede detectar?

📘 **Dónde se aprende** (1 clase): [B106-C17 · Prevención y respuesta a incendios](../programa/clases/B106/B106-C17-prevencion-y-respuesta-a-incendios/CLASE.md).

### Umbral de colapso

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B36-C06](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md):**
- *Descripción textual:* el colapso esférico fija el umbral, que junto con σ(M) da la fracción de masa y la función de masa; las caminatas lo verifican.
- 🎯 **Por qué importa:** Contar halos exige un umbral de colapso y una función de masa. La decisión central: ¿cuánta masa del universo está en halos de más de cierta masa?

📘 **Dónde se aprende** (1 clase): [B36-C06 · Formación de halos y función de masa](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md).

### Umbral de comunicación

- Un umbral de comunicación es la probabilidad desde la cual se informa.

💡 **Cómo se explica en la clase [B56-C19](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md):**
- Definir log-odds, razón de verosimilitud, evidencia independiente y umbral de comunicación.
- Ejercicio 12 · integrador. Elabora tu *protocolo de comunicación de un candidato*: define previa, cuatro líneas con `LR` y tus umbrales de comunicación (sintéticos), calcula las posteriores, y escribe quién informa a quién en cada umbral y qué límites declara.
- 🎯 **Por qué importa:** Anunciar demasiado pronto un hallazgo puede dañar la ciencia y la confianza pública; ocultarlo puede dañar la transparencia. Hace falta una forma explícita de saber cuánta evidencia hay.

📘 **Dónde se aprende** (1 clase): [B56-C19 · Ética del descubrimiento de vida](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md).

### Umbral de corte

- El umbral de corte deja pasar a una fracción.

💡 **Cómo se explica en la clase [B104-C03](../programa/clases/B104/B104-C03-seleccion-y-aptitud/CLASE.md):**
- Simular un embudo con aptitud latente, puntaje ruidoso y umbral de corte.
- 🎯 **Por qué importa:** Si una prueba tiene ruido, ¿cuántos de los elegidos serán de verdad aptos? La decisión central: ¿cuánto ruido tolera un embudo antes de que la elección se parezca a un sorteo?

📘 **Dónde se aprende** (1 clase): [B104-C03 · Selección y aptitud](../programa/clases/B104/B104-C03-seleccion-y-aptitud/CLASE.md).

### Umbral de cruce

- Un umbral de cruce es la separación máxima aceptada.

💡 **Cómo se explica en la clase [B14-C05](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md):**
- El cruce por radio (todas las fuentes dentro del umbral) detecta ambigüedades: si dos fuentes de A caen dentro, el emparejamiento no es único.
- Un cruce posicional con umbral, más una comprobación de ambigüedad.
- 🎯 **Por qué importa:** Un catálogo de estrellas no es una lista de números: cada columna tiene una unidad, algunas filas no tienen paralaje, y la tabla viene de un instrumento, una época y una versión. Si pierdes eso al copiar los datos a un arreglo, pierdes la mitad del significado.

📘 **Dónde se aprende** (1 clase): [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md).

### Umbral de decisión

- `k` es el margen y `h` el umbral de decisión.

💡 **Cómo se explica en la clase [B33-C05](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md):**
- *Descripción textual:* el cociente costo/pérdida fija el umbral de decisión, que da el gasto; el Brier y la fiabilidad miden la calidad de las probabilidades.
- umbral de decision p > C/L = 0.10 ; frecuencia climatologica = 0.2978
- 🎯 **Por qué importa:** La mejor comunicación de riesgo da probabilidades calibradas y deja decidir al usuario. La decisión central: ¿cuándo conviene proteger y cuán fiables son las probabilidades?

📘 **Dónde se aprende** (2 clases): [B33-C05 · Comunicación de riesgo y alertas de clima espacial](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md); [B97-C22 · Detección autónoma de eventos científicos](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md).

### Umbral de descarte

- Un umbral de descarte es una restricción dura que excluye un sitio aunque brille en otros criterios.

💡 **Cómo se explica en la clase [B109-C01](../programa/clases/B109/B109-C01-seleccion-de-emplazamiento-para-un-asentamiento-extraterrestre/CLASE.md):**
- S["Sitios<br/>y atributos"] --> U["Umbrales<br/>de descarte"]
- Aplicar umbrales de descarte (restricciones duras) antes de puntuar.
- 🎯 **Por qué importa:** Un asentamiento no se puede mover una vez construido. La decisión central: ¿cómo comparar sitios con criterios distintos sin esconder los juicios de valor en un número?

📘 **Dónde se aprende** (1 clase): [B109-C01 · Selección de emplazamiento para un asentamiento extraterrestre](../programa/clases/B109/B109-C01-seleccion-de-emplazamiento-para-un-asentamiento-extraterrestre/CLASE.md).

### Umbral de detección

- El umbral de detección del ejemplo es CNR ≥ 5 (criterio de Rose, valor estándar no consultado).
- El umbral de detección y la probabilidad de falsa alarma.

💡 **Cómo se explica en la clase [B51-C11](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md):**
- falsa deteccion con umbral |z|^2 > 6.0 sobre M = 1024 celdas: prediccion = 0.9212 ;
- umbral |z|^2 para 1 % de falsas detecciones con M = 1024: 11.532 (|z| = 3.396)
- ⚠️ **Error frecuente:** Declarar detección sin umbral. Se corrige con 8.3.
- 🎯 **Por qué importa:** Declarar una detección sin umbral estadístico es un riesgo de falsos positivos. La decisión central: ¿qué pico es una señal y cuál es ruido, y con qué precisión se estiman retardo y tasa?

📘 **Dónde se aprende** (2 clases): [B51-C11 · Búsqueda de franjas VLBI: ajuste de retardo y tasa](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md); [B83-C17 · Verificación frente a validación](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md).

### Umbral de error

- El umbral de error es la longitud a partir de la cual la maestra desaparece de la población.

💡 **Cómo se explica en la clase [B56-C03](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md):**
- Definir replicador, secuencia maestra, fidelidad, calidad de copia y umbral de error.
- La evidencia es la ficha del umbral de error del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un replicador que copia mal pierde su información; uno que copia bien necesita una maquinaria que, sin vida previa, aún no existe. Esa tensión limita el tamaño de los primeros genomas.

📘 **Dónde se aprende** (1 clase): [B56-C03 · Origen de moléculas autorreplicantes](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md).

### Umbral de generalidad

- El umbral de generalidad aquí es una convención didáctica.

💡 **Cómo se explica en la clase [B119-C31](../programa/clases/B119/B119-C31-practica-estatal-y-costumbre-internacional-en-el-derecho-espacial/CLASE.md):**
- *Descripción textual:* la adopción espontánea y la imitación hacen crecer la fracción de adoptantes hasta cruzar un umbral ilustrativo de generalidad.
- 🎯 **Por qué importa:** B119 presenta los tratados; no enseña la costumbre ni la práctica estatal, que complementan a los tratados en un campo donde los Estados no son partes de todos ellos. La decisión central: ¿qué factores aceleran o frenan que una práctica se vuelva general?

📘 **Dónde se aprende** (1 clase): [B119-C31 · Práctica estatal y costumbre internacional en el derecho espacial](../programa/clases/B119/B119-C31-practica-estatal-y-costumbre-internacional-en-el-derecho-espacial/CLASE.md).

### Umbral de linealidad

- El umbral de linealidad es el flujo donde la desviación llega a un límite.

💡 **Cómo se explica en la clase [B44-C10](../programa/clases/B44/B44-C10-no-linealidad-y-saturacion/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de la linealidad y la saturación*: ajuste, umbral y coeficiente.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de la linealidad y la saturación*: ajuste, umbral y coeficiente.
- 🎯 **Por qué importa:** Si la respuesta se curva, la fotometría se sesga mucho antes del pozo lleno. La decisión central: ¿hasta qué flujo puedo confiar en la respuesta lineal?

📘 **Dónde se aprende** (1 clase): [B44-C10 · No linealidad y saturación](../programa/clases/B44/B44-C10-no-linealidad-y-saturacion/CLASE.md).

### Umbral de Otsu

- El umbral de Otsu es el valor que maximiza la varianza entre las dos clases.

💡 **Cómo se explica en la clase [B57-C15](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md):**
- Para dos gaussianas de igual varianza y peso, el umbral óptimo es el punto medio, `0,050`; en una imagen mitad agua y mitad tierra Otsu da `0,048`.
- Otsu elige el umbral, la máscara da el área y la diferencia entre fechas es la inundación; la lluvia se estandariza para declarar años secos.
- ⚠️ **Error frecuente:** Fijar el umbral a ojo sin declararlo. Usa Otsu u otro criterio documentado (8.1).
- 🎯 **Por qué importa:** Las agencias necesitan mapas de inundación en horas y alertas de sequía en meses. La decisión central: ¿cómo se fija el umbral entre agua y tierra sin fijarlo a ojo, y cómo se declara que un año es seco?

📘 **Dónde se aprende** (1 clase): [B57-C15 · Sequías e inundaciones](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md).

### Umbral de presión

- El umbral de presión es el valor cuyo cruce se evalúa.

💡 **Cómo se explica en la clase [B114-C05](../programa/clases/B114/B114-C05-despresurizacion-escenarios-tiempos-y-respuesta/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué los umbrales de presión de la clase no son un criterio de seguridad para personas?
- ⚠️ **Error frecuente:** Mezclar el umbral de presión con un criterio fisiológico. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Entre una grieta de `1 mm` y una brecha de `100 mm` el tiempo disponible pasa de días a segundos. La decisión central: ¿cuánto tiempo hay hasta un umbral de presión y alcanza para responder?

📘 **Dónde se aprende** (1 clase): [B114-C05 · Despresurización: escenarios, tiempos y respuesta](../programa/clases/B114/B114-C05-despresurizacion-escenarios-tiempos-y-respuesta/CLASE.md).

### Umbral de revisión

- Un umbral de revisión es la altura o energía desde la cual conviene consultar la reglamentación.

💡 **Cómo se explica en la clase [B119-C24](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md):**
- Descripción larga: la resistencia reduce el apogeo, pero el impulso mayor aún cruza el umbral de revisión.
- Estimar una distancia de seguridad ilustrativa y el umbral de revisión.
- 🎯 **Por qué importa:** Ninguna clase trata los límites de la experimentación educativa; el art. VI del tratado exige autorización y supervisión de las actividades no gubernamentales, y la escala pequeña no exime de ella.

📘 **Dónde se aprende** (1 clase): [B119-C24 · Límites legales y de seguridad de la experimentación educativa](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md).

### Umbral de seguimiento

- La SNR del lazo es `C/N₀/B_L`; un umbral de seguimiento típico es de unos 10 dB (valor estándar no consultado).

💡 **Cómo se explica en la clase [B89-C24](../programa/clases/B89/B89-C24-recepcion-de-telemetria-debil/CLASE.md):**
- LAZO --> UM["umbral ~ 10 dB: seguimiento"]
- 🎯 **Por qué importa:** Cuando una nave está lejos o en emergencia, recibir su portadora a unos pocos dB-Hz marca la diferencia entre confirmar su estado o perderla; el costo es tiempo de integración o un lazo difícil de enganchar. La decisión central: ¿cómo detectar y seguir una portadora muy débil sin tantas falsas alarmas?

📘 **Dónde se aprende** (1 clase): [B89-C24 · Recepción de telemetría débil](../programa/clases/B89/B89-C24-recepcion-de-telemetria-debil/CLASE.md).

### Umbral óptimo

- El umbral óptimo minimiza el costo esperado.

💡 **Cómo se explica en la clase [B57-C34](../programa/clases/B57/B57-C34-alertas-tempranas-y-etica-en-el-monitoreo-de-desastres/CLASE.md):**
- Con `d' = 3`, `π = 0,01`, `c_fa = 1` y `c_om = 100`, el umbral óptimo analítico es `t* = d'/2 + ln[c_fa(1−π)/(c_om π)]/d' = 1,4966`; la búsqueda numérica da `1,4966`.
- Con el umbral óptimo, solo `12,3%` de las alertas corresponde a un evento.
- 🎯 **Por qué importa:** Un detector excelente puede producir una mayoría de falsas alarmas si el evento es raro, y las alertas repetidas y falsas se ignoran. La decisión central: ¿qué umbral y qué comunicación equilibran el costo de omitir y el de alarmar en falso, y quién decide?

📘 **Dónde se aprende** (1 clase): [B57-C34 · Alertas tempranas y ética en el monitoreo de desastres](../programa/clases/B57/B57-C34-alertas-tempranas-y-etica-en-el-monitoreo-de-desastres/CLASE.md).

### Umbrales

- Los umbrales `C_i = 2Ω(L_i)` marcan la apertura de los cuellos de L1, L2 y L3 al bajar `C`.
- La dosis total ionizante acumulada se compara con umbrales de material.

💡 **Cómo se explica en la clase [B73-C07](../programa/clases/B73/B73-C07-constante-de-jacobi/CLASE.md):**
- *Descripción textual:* el estado fija `C`; al compararlo con cuatro umbrales se obtiene qué cuellos están abiertos y, con ello, las regiones accesibles.
- Paso 1 · Umbrales. `C₁ = 3,188341` y `C₂ = 3,172161`.
- ⚠️ **Error frecuente:** Usar `Ω − v²/2` con los umbrales de `2Ω`. Se corrige con la sección 10.
- 🎯 **Por qué importa:** La constante de Jacobi es la única cantidad conservada del CR3BP y decide, sin integrar, si una nave puede ir de la Tierra a la Luna o escapar. La decisión central: ¿qué dice un número `C` sobre las regiones por las que se puede mover una partícula?

📘 **Dónde se aprende** (2 clases): [B73-C07 · Constante de Jacobi](../programa/clases/B73/B73-C07-constante-de-jacobi/CLASE.md); [B85-C24 · Efectos de la radiación ionizante en materiales y electrónica](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md).

### Umbralización

- La umbralización clasifica con una regla `I < T`.

🎯 **Por qué importa (clase B15-C13):** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.

📘 **Dónde se aprende** (1 clase): [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md).

### Un eje

- La ala fija no se mueve respecto del cuerpo; un eje gira para seguir al Sol en el plano;

💡 **Cómo se explica en la clase [B86-C04](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md):**
- Con dos ejes el coseno medio es `1 − f`; con un eje es `(1 − f) cosβ`; con el ala fija al cenit es mucho menor (`≈ cosβ/π` antes de restar el eclipse).
- Calcular el coseno medio por órbita para un ala fija, de un eje y de dos ejes.
- 🎯 **Por qué importa:** El eclipse más largo fija el tamaño de la batería y el peor `β` fija el de la ala. Un diseño que mire solo `β = 0` ignora que a `β` alto no hay eclipse pero el coseno cae.

📘 **Dónde se aprende** (1 clase): [B86-C04 · Orientación solar y eclipses](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md).

### Un solo

- El NIST describe un apartado «Detection of Outliers» y recomienda la prueba de Grubbs cuando se busca un solo atípico (S1).

💡 **Cómo se explica en la clase [B12-C19](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md):**
- Solo `7,46` supera `3,5`: el mismo dato se marca, con una puntuación tres veces superior al umbral.
- Por eso Grubbs sirve para un solo atípico y, cuando se sospechan varios, se usan versiones secuenciales o métodos robustos.
- 🎯 **Por qué importa:** Un dato aberrante puede ser un error del instrumento, una pérdida de sincronía o el primer indicio de un fenómeno real. Eliminarlo sin criterio esconde información; conservarlo sin revisar contamina el resultado.

📘 **Dónde se aprende** (1 clase): [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md).

### UNDRIP

- La UNDRIP es la Declaración de la ONU sobre los derechos de los pueblos indígenas.

💡 **Cómo se explica en la clase [B02-C20](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md):**
- S2 cita el artículo 32.2 de la UNDRIP, que pide a los estados obtener consentimiento libre e informado antes de aprobar proyectos que afecten sus tierras o territorios, y propone no tratar a los pueblos indígenas solo como «partes interesadas» o «compromiso cultural».
- Hecho: que la astronomía canadiense usa Maunakea y que hay tensiones por el TMT; propuesta: que la sociedad adopte una posición guiada por UNDRIP y use las directrices como modelo.
- 🎯 **Por qué importa:** Los sitios, instrumentos, archivos, saberes y hasta la oscuridad del cielo son patrimonio, y los telescopios, el turismo y las constelaciones de satélites pueden dañarlo. La pregunta motivadora es: ¿qué debo preguntar, a quién y antes de qué, cuando mi trabajo toca un cielo o un lugar que importa a otras personas?

📘 **Dónde se aprende** (1 clase): [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md).

### Unicidad

- La unicidad es la fracción de registros con grupo de tamaño 1.

💡 **Cómo se explica en la clase [B105-C19](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md):**
- Cohorte de 6 con edad exacta, sexo, profesión y misión: `k = 1` y 100 % de unicidad.
- Generalizar reduce la unicidad a costa de detalle; el ruido de Laplace protege con `ε` pero pierde utilidad: con `n = 6`, el error medio esperado de una media con rango 100 es 166,5; 33,3; 16,7 y 3,3 puntos para `ε = 0,1; 0,5; 1; 5`.
- 🎯 **Por qué importa:** No basta con quitar el nombre: con edad, sexo, profesión y misión, una persona de una cohorte de 6 suele ser única. La decisión central: ¿qué se puede publicar de una cohorte pequeña sin identificar a nadie y cuánta utilidad se pierde al protegerla?

📘 **Dónde se aprende** (1 clase): [B105-C19 · Bioética en investigación tripulada](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md).

### Unidad

- Una unidad es una cantidad de referencia de esa magnitud (metro, kilogramo, segundo).
- Una unidad es una cantidad de referencia de la misma naturaleza que se adopta por convención para medirla; el valor numérico es cuántas veces cabe la unidad.
- Una unidad es una magnitud de referencia (metro, kilogramo, segundo).
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C06](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md):**
- De ahí se obtienen las unidades: el segundo cuenta períodos de la radiación del cesio y el metro se deriva de `c` y del segundo.
- Importa porque ya no existe un objeto físico patrón que pueda deteriorarse: cualquier laboratorio puede reproducir la unidad.
- 🎯 **Por qué importa:** El 23 de septiembre de 1999 la NASA perdió contacto con la sonda Mars Climate Orbiter. Según la agencia, un error de navegación se debió a no traducir unidades inglesas a métricas: el programa en tierra usaba unas y el de la nave otras, y la sonda pasó demasiado cerca de Marte y se quemó en su atmósfera (S1).

📘 **Dónde se aprende** (8 clases): [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md); [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md); [B07-C11 · Gestión de unidades en programas](../programa/clases/B07/B07-C11-gestion-de-unidades-en-programas/CLASE.md); [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md); [B75-C28 · Restricciones de radiación en trayectorias](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md) y 2 más.

### Unidad astronómica

- La unidad astronómica (au) es la distancia convencional de 149 597 870 700 m, cercana a la distancia media entre la Tierra y el Sol.
- Una unidad astronómica (au) es una unidad de longitud definida exactamente como 149 597 870 700 m.
- Una unidad astronómica (au) es una unidad de longitud con valor exacto 149 597 870 700 m (S2).

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Si pasas el semieje a unidades astronómicas (1 au = 149 597 870 700 m exactos, S2) y el período a años terrestres (365,256 d), ocurre algo notable: el cuadrado del período y el cubo del semieje salen casi iguales para los ocho planetas.
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.

📖 **Explicado a fondo:** [Unidad astronómica (UA)](esencial/esencial-m-z.md#unidad-astronómica-ua) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B01-C02 · Escalas desde la Tierra al cosmos observable](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md); [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md); [B03-C07 · Conversión de distancia y velocidad](../programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/CLASE.md).

### Unidad astronómica (au)

- Una unidad no SI aceptada es una unidad histórica o práctica reconocida para su uso con el SI; la unidad astronómica (au) es una de ellas y vale exactamente 149 597 870 700 m (S2, S3).

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- La unidad astronómica nació como la distancia media Tierra–Sol, y hoy es una longitud definida: `1 au = 149 597 870 700 m` exactamente (S2, S3).
- Imagina una escalera con peldaños de unidades; el metro está abajo y cada unidad astronómica es un peldaño que se alcanza multiplicando por un factor definido.
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.

📘 **Dónde se aprende** (1 clase): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md).

### Unidad base

- Una unidad base es una de las siete unidades fundamentales: segundo (s), metro (m), kilogramo (kg), amperio (A), kelvin (K), mol (mol) y candela (cd).

💡 **Cómo se explica en la clase [B13-C01](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md):**
- A["7 constantes definitorias<br/>(valores exactos)"] --> B["7 unidades base"]
- *Descripción textual:* arriba, las siete constantes exactas; debajo, las unidades base que definen; luego las derivadas; al final, mediciones reales.
- 🎯 **Por qué importa:** Una señal de radio o de láser viaja a la Luna y regresa. Para decir «la Luna está a 384 400 km» hay que haber acordado qué es un kilómetro, qué es un segundo y a qué velocidad viaja la señal.

📘 **Dónde se aprende** (1 clase): [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md).

### Unidad de masa atómica

- La unidad de masa atómica `u` es la masa de un doceavo del átomo de ¹²C (C03); vale 1,660 539 068 92 × 10⁻²⁷ kg (S3).

💡 **Cómo se explica en la clase [B06-C06](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md):**
- Con ese valor exacto y con la unidad de masa atómica `u`, el producto `N_A · u` es muy cercano a 1 g/mol: con los valores CODATA 2022 resulta `1,000 000 001 1 g/mol` (el laboratorio de la sección 17 lo calcula).
- El mol es lo mismo pero con 6,022 × 10²³ partículas: si conoces la masa de un átomo en unidades de masa atómica, la masa de un mol en gramos es ese mismo número.
- 🎯 **Por qué importa:** La misión OSIRIS-REx trajo a la Tierra 121,6 g de material del asteroide Bennu. Los análisis de laboratorio de una parte de esa muestra encontraron entre 4,5 y 4,7 % de carbono y entre 0,23 y 0,25 % de nitrógeno en masa (S1).

📘 **Dónde se aprende** (1 clase): [B06-C06 · Cantidad de sustancia y mol](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md).

### Unidad de vuelo (FM)

- Protovuelo: calificación aplicada a la unidad de vuelo. Unidad de vuelo (FM): la que vuela.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- La CDS (F8) distingue calificación (con una unidad de ingeniería idéntica a la de vuelo y luego aceptación de la unidad de vuelo) y protovuelo (sobre la unidad de vuelo, que luego no se desmonta ni modifica), y señala que el flujo varía de una misión a otra.
- E -- "escapa 0.20" --> F["Unidad de vuelo<br/>detecta 0.70"]
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?

📘 **Dónde se aprende** (1 clase): [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### Unidad derivada

- Una unidad derivada es un producto de potencias de unidades base (m/s, J = kg m² s⁻²).
- Una unidad derivada se forma con las base (m/s).
- Una unidad derivada combina unidades base: m/s, m/s², N = kg·m/s², J = N·m, W = J/s.

💡 **Cómo se explica en la clase [B03-C06](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md):**
- B["Unidades base: m, kg, s…"] --> D["Unidades derivadas: m/s, m/s², N, J, W"]
- *Descripción textual:* las unidades base generan las derivadas; estas aparecen en una fórmula; una pregunta decide si ambos lados tienen la misma dimensión: si sí, la fórmula es coherente; si no, hay un error.
- 🎯 **Por qué importa:** El 23 de septiembre de 1999 la NASA perdió contacto con la sonda Mars Climate Orbiter. Según la agencia, un error de navegación se debió a no traducir unidades inglesas a métricas: el programa en tierra usaba unas y el de la nave otras, y la sonda pasó demasiado cerca de Marte y se quemó en su atmósfera (S1).

📘 **Dónde se aprende** (3 clases): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md); [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md); [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md).

### Unidad mínima cartografiable

- La unidad mínima cartografiable es el menor elemento representable.

💡 **Cómo se explica en la clase [B53-C26](../programa/clases/B53/B53-C26-publicacion-de-mapas-geologicos-planetarios-estandares-y-leyendas/CLASE.md):**
- A escala `1:1 000 000`, con una convención ilustrativa de `0,5 mm` de ancho mínimo, la unidad mínima cartografiable es `500 m` (área `1,00 km²`).
- Relacionar escala, resolución y unidad mínima cartografiable.
- 🎯 **Por qué importa:** Un mapa excelente mal publicado no se puede reutilizar. La decisión central: ¿qué escala justifica el detalle mostrado, qué leyenda es legible y qué metadatos hacen el mapa reproducible?

📘 **Dónde se aprende** (1 clase): [B53-C26 · Publicación de mapas geológicos planetarios: estándares y leyendas](../programa/clases/B53/B53-C26-publicacion-de-mapas-geologicos-planetarios-estandares-y-leyendas/CLASE.md).

### Unidad no SI aceptada

- Una unidad no SI aceptada es una unidad histórica o práctica reconocida para su uso con el SI; la unidad astronómica (au) es una de ellas y vale exactamente 149 597 870 700 m (S2, S3).

🎯 **Por qué importa (clase B01-C08):** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.

📘 **Dónde se aprende** (1 clase): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md).

### Unidad reemplazable (ORU)

- La unidad reemplazable (ORU) es la que un robot puede cambiar.

🎯 **Por qué importa (clase B97-C12):** Pocos repuestos dejan la misión sin reparación posible; demasiados cargan masa. La confianza del conjunto, no la de cada pieza, es la que importa, y se obtiene con el producto de las probabilidades.

📘 **Dónde se aprende** (1 clase): [B97-C12 · Robots de mantenimiento](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md).

### Unidad U

- La unidad U es el módulo de `100 × 100 × 113,5 mm` (1U).

💡 **Cómo se explica en la clase [B95-C01](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md):**
- python programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/formato_cubesat.py
- 🎯 **Por qué importa:** Un CubeSat que no cumple el estándar no entra en el dispensador, aunque funcione perfectamente. La decisión central: ¿esta configuración cabe, pesa y se equilibra dentro de lo que el estándar permite, y cuándo puede encenderse, desplegar y transmitir?

📘 **Dónde se aprende** (1 clase): [B95-C01 · Unidad CubeSat, dimensiones y formatos](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md).

### Unidades adimensionales

- Las unidades adimensionales fijan la distancia entre primarios y la velocidad angular media en 1.

🎯 **Por qué importa (clase B73-C01):** Con tres cuerpos no hay solución cerrada, pero sí una cantidad conservada que organiza todo lo demás: puntos de equilibrio, regiones prohibidas y transferencias de bajo costo. La decisión central: ¿cuándo basta el modelo de tres cuerpos restringido, y cómo sé que mi integración no inventa dinámica?

📘 **Dónde se aprende** (1 clase): [B73-C01 · Problema restringido de tres cuerpos](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md).

### Unidades base

- El Sistema Internacional (SI) es el conjunto de unidades coherentes acordado por la comunidad internacional; sus siete unidades base son segundo, metro, kilogramo, amperio, kelvin, mol y candela (S1, S2).
- El SI (Sistema Internacional de Unidades) es el sistema acordado internacionalmente; sus siete unidades base son el segundo (s), el metro (m), el kilogramo (kg), el amperio (A), el kelvin (K), el mol (mol) y la candela (cd), definidas a partir de siete constantes definitorias de valor exacto (S2).
- El Sistema Internacional (SI) es el conjunto de unidades acordado internacionalmente; tiene siete unidades base: segundo, metro, kilogramo, amperio, kelvin, mol y candela (S1).

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- Enumerar las siete unidades base del SI y decir cuáles usa esta clase.
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.

📘 **Dónde se aprende** (3 clases): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md); [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md); [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md).

### Unidades del sistema

- Las unidades del sistema: longitud `a`, tiempo `1/n`, velocidad `a n`.

💡 **Cómo se explica en la clase [B76-C02](../programa/clases/B76/B76-C02-escalas-sinodicas-de-referencia/CLASE.md):**
- *Descripción textual:* el mes sideral y el año dan el mes sinódico; de él sale el periodo de la órbita resonante; las unidades del sistema permiten expresar todo sin dimensiones.
- Convertir longitudes, tiempos y velocidades a unidades adimensionales del sistema y de vuelta.
- 🎯 **Por qué importa:** Un equipo que mezcla el mes sideral con el sinódico desplaza una resonancia en medio día y pierde una geometría de eclipses. La decisión central: ¿qué escala de tiempo corresponde a cada pregunta y cómo se convierte sin error?

📘 **Dónde se aprende** (1 clase): [B76-C02 · Escalas sinódicas de referencia](../programa/clases/B76/B76-C02-escalas-sinodicas-de-referencia/CLASE.md).

### Unidades geométricas

- Las unidades geométricas fijan `G = c = M = 1`.

💡 **Cómo se explica en la clase [B27-C07](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md):**
- Calcular el horizonte `r₊ = M(1 + √(1 − a²))` en unidades geométricas.
- Convertir unidades geométricas a metros, segundos y unidades astronómicas.
- ⚠️ **Error frecuente:** Mezclar unidades geométricas y SI. Se corrige con la sección 10.
- 🎯 **Por qué importa:** El espín cambia el ISCO y, con él, cuánta energía se libera: de `5,7 %` a más de `30 %` de la masa en reposo. La decisión central: ¿dónde están el horizonte y el ISCO para un espín dado y qué eficiencia implica?

📘 **Dónde se aprende** (1 clase): [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md).

### Unidimensionalidad

- La unidimensionalidad se examina con el primer valor propio de la matriz de correlaciones.

💡 **Cómo se explica en la clase [B105-C27](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md):**
- D --> E["valores propios:<br/>unidimensionalidad"]
- Examinar la unidimensionalidad con los valores propios.
- 🎯 **Por qué importa:** Un cuestionario con ítems que no miden lo mismo produce una puntuación poco fiable, y con pocos participantes su fiabilidad ni siquiera se puede estimar. La decisión central: ¿qué ítems sobran, cuántos ítems hacen falta y cuántos participantes se necesitan para estimar el alfa con una incertidumbre aceptable?

📘 **Dónde se aprende** (1 clase): [B105-C27 · Instrumentos validados y psicometría en investigación](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md).

### Uniformes

- Si el procedimiento es correcto, los rangos son uniformes sobre `0..L`.

🎯 **Por qué importa (clase B19-C08):** Un intervalo del 90 % que cubre el valor verdadero solo la mitad de las veces es peor que no tener intervalo: transmite una seguridad falsa. Los diagnósticos de C04 dicen si el cómputo funcionó; los chequeos de C06 si el modelo reproduce los datos.

📘 **Dónde se aprende** (1 clase): [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md).

### Uniformidad

- La uniformidad compara espesores de centro y borde.

💡 **Cómo se explica en la clase [B43-C07](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md):**
- *Descripción textual:* el índice complejo da la reflectancia y la transmisión de la película; la geometría del evaporador da la uniformidad.
- Predecir la uniformidad de una fuente puntual `h/(h²+ρ²)^(3/2)`.
- 🎯 **Por qué importa:** Una película delgada deja pasar luz; una gruesa refleja pero no se adhiere ni es uniforme. La decisión central: ¿qué espesor es opaco, qué reflectancia da y cuánto varía de centro a borde por la geometría del evaporador?

📘 **Dónde se aprende** (1 clase): [B43-C07 · Aluminizado y recubrimientos](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md).

### Unilateral

- Una prueba bilateral rechaza para desviaciones en ambos sentidos; una unilateral, en uno solo.

💡 **Cómo se explica en la clase [B12-C09](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md):**
- Ejercicio 3 · casi autónomo. Con `z = 1,8`, calcula los valores `p` bilateral y unilateral y compara con 0,05.
- Bilateral `0,072` (no rechaza); unilateral `0,036` (rechaza).
- 🎯 **Por qué importa:** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.

📘 **Dónde se aprende** (1 clase): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md).

### Unimodal

- La hipótesis nula de Rayleigh es que la población está distribuida uniformemente en el círculo; la prueba detecta una desviación unimodal (la documentación de astropy lo declara, consultada).

💡 **Cómo se explica en la clase [B132-C04](../programa/clases/B132/B132-C04-estadistica-de-orientaciones-en-arqueoastronomia/CLASE.md):**
- No: Rayleigh detecta solo una desviación unimodal; la muestra es bimodal y requiere otra prueba.
- 🎯 **Por qué importa:** Si se mira un conjunto de ejes y se busca «algo», casi siempre se encuentra. La decisión central: ¿la agrupación observada supera lo esperable por azar, una vez descontado que se probaron varias hipótesis?

📘 **Dónde se aprende** (1 clase): [B132-C04 · Estadística de orientaciones en arqueoastronomía](../programa/clases/B132/B132-C04-estadistica-de-orientaciones-en-arqueoastronomia/CLASE.md).

### Unión

- La unión `A∪B` ocurre si ocurre `A` o `B`; la intersección `A∩B`, si ocurren ambos.

💡 **Cómo se explica en la clase [B12-C01](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md):**
- Usar complemento, unión y probabilidad condicional, y aplicar la regla de Bayes en un caso de dos eventos.
- Ejercicio 8. Calcula `P(C1 falla ∪ C2 falla)` con la fórmula de unión y con el complemento.
- 🎯 **Por qué importa:** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.

📘 **Dónde se aprende** (1 clase): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md).

### Unión de extremos no homólogos

- La reparación devuelve la integridad al ADN: la unión de extremos no homólogos (NHEJ) reúne los extremos directamente y puede cometer errores.

🎯 **Por qué importa (clase B112-C05):** Falta la clase de mecanismos moleculares de daño y reparación. Sin ella, la diferencia de eficacia biológica entre fotones e iones pesados (B112-C01, C02) y la incertidumbre del riesgo (C04) parecen cifras arbitrarias.

📘 **Dónde se aprende** (1 clase): [B112-C05 · Daño y reparación del ADN por radiación espacial](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md).

### Unitario

- Un cuaternión es unitario si `|q| = 1`.

💡 **Cómo se explica en la clase [B10-C15](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md):**
- Un cuaternión unitario tiene tres grados de libertad reales (cuatro números, una restricción de norma), igual que una rotación.
- Los cuaterniones unitarios forman una esfera de cuatro dimensiones.
- 🎯 **Por qué importa:** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.

📘 **Dónde se aprende** (1 clase): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md).

### Universo

- El universo es todo: el espacio, la materia, la energía y el tiempo.

💡 **Cómo se explica en la clase [B01-C01](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md):**
- Pero `t_H` no es exactamente la edad del universo: la expansión no ha tenido siempre el mismo ritmo.
- Para fijar ideas hay un caso límite con solución exacta: un universo hecho *solo de materia* (el llamado modelo de Einstein–de Sitter).
- ⚠️ **Error frecuente:** Pensar que hay un centro del universo. Viene de imaginar una explosión que se expande desde un punto.
- 🎯 **Por qué importa:** Seguramente has leído que «el universo tiene 13 800 millones de años» o que «el universo observable mide 93 000 millones de años luz». Son frases que se repiten con total seguridad.

📘 **Dónde se aprende** (1 clase): [B01-C01 · Naturaleza del universo](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md).

### Universo de Friedmann plano

- Un universo de Friedmann plano tiene `a(t)`.

🎯 **Por qué importa (clase B39-C05):** Las ecuaciones de campo conectan la geometría con la materia. La decisión central: ¿en qué régimen la gravedad de Einstein se reduce a la de Newton y qué garantiza la consistencia de las ecuaciones?

📘 **Dónde se aprende** (1 clase): [B39-C05 · Ecuaciones de campo de Einstein y límite newtoniano](../programa/clases/B39/B39-C05-ecuaciones-de-campo-de-einstein-y-limite-newtoniano/CLASE.md).

### Universo observable

- El universo observable es solo la parte de la que ha tenido tiempo de llegarnos luz desde que empezó la expansión.

💡 **Cómo se explica en la clase [B01-C01](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md):**
- Si el universo tiene unos 13,8 Gyr, uno esperaría que lo observable llegara a 13,8 mil millones de años luz de distancia.
- Lo que llamamos distancia comóvil es justamente la distancia *de hoy* a un punto, descontando el efecto de la expansión que ya ocurrió; es la que describe el borde del universo observable, el horizonte de partículas.
- 🎯 **Por qué importa:** Seguramente has leído que «el universo tiene 13 800 millones de años» o que «el universo observable mide 93 000 millones de años luz». Son frases que se repiten con total seguridad.

📘 **Dónde se aprende** (1 clase): [B01-C01 · Naturaleza del universo](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md).

### UNOOSA

- COPUOS es la Comisión sobre la Utilización del Espacio Ultraterrestre con Fines Pacíficos. UNOOSA es la Oficina de Asuntos del Espacio Ultraterrestre, su secretaría.

💡 **Cómo se explica en la clase [B119-C06](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md):**
- 18 miembros en 1958, permanente en 1959, dos subcomités y secretaría UNOOSA.
- Según el resumen de búsqueda de las páginas de UNOOSA (2026-11-11), la Asamblea General creó COPUOS como órgano ad hoc con 18 miembros por la res. 1348 (XIII) del 13-12-1958 y lo hizo permanente por la res. 1472 (XIV) del 12-12-1959; tiene un Subcomité Científico y Técnico y un Subcomité Jurídico, y UNOOSA es su secretaría.
- ⚠️ **Error frecuente:** Atribuir la decisión a UNOOSA y no a COPUOS. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** Quien estudia el derecho espacial necesita saber dónde se negocia y cómo se decide; ninguna clase anterior trata los organismos. La decisión central: ¿cómo cambia la probabilidad de bloqueo cuando crece el número de miembros que deben consentir?

📘 **Dónde se aprende** (1 clase): [B119-C06 · Organismos UNOOSA y COPUOS](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md).

### Upset

- Un upset es un cambio de estado reversible.

💡 **Cómo se explica en la clase [B85-C21](../programa/clases/B85/B85-C21-efectos-de-particulas-energeticas-en-electronica-y-materiales/CLASE.md):**
- La probabilidad de al menos un upset en un año es `93,16 %` y en cinco, `99,9998 %`: ocurrirá, y hay que diseñar para ello.
- Una memoria sintética de `64 Mbit` con `σ_sat = 10⁻⁷ cm²/bit`, `L₀ = 1,5 MeV cm²/mg` y un espectro `Φ(>L) = 10⁻⁶ L⁻² cm⁻² s⁻¹` sufre `2,68` upsets al año (MTBF `136` días) y la probabilidad de al menos uno en un año es `93,2 %`.
- 🎯 **Por qué importa:** Un upset en un procesador o en una memoria puede reiniciar un instrumento o corromper un dato. La decisión central: ¿con qué frecuencia ocurre un evento único en un dispositivo dado y cuánto cambia si se elige un componente de mayor umbral de LET?

📘 **Dónde se aprende** (1 clase): [B85-C21 · Efectos de partículas energéticas en electrónica y materiales](../programa/clases/B85/B85-C21-efectos-de-particulas-energeticas-en-electronica-y-materiales/CLASE.md).

### Uso del color

- El uso del color pide que el color no sea el único medio de transmitir información.

💡 **Cómo se explica en la clase [B128-C06](../programa/clases/B128/B128-C06-contraste-y-color-accesibles/CLASE.md):**
- La razón es `(L₁ + 0,05)/(L₂ + 0,05)` con `L₁` el color más claro.
- El color no puede ser el único medio de transmitir información (1.4.1).
- ⚠️ **Error frecuente:** Usar el color como único medio. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Un texto gris claro sobre blanco, un azul puro sobre negro o una leyenda donde solo cambia el tono se pierden para quien tiene baja visión, daltonismo o una pantalla poco luminosa. La decisión central: ¿cómo compruebo con números que un par de colores se lee, y cuándo el color no basta?

📘 **Dónde se aprende** (1 clase): [B128-C06 · Contraste y color accesibles](../programa/clases/B128/B128-C06-contraste-y-color-accesibles/CLASE.md).

### Uso previsto

- El uso previsto es la decisión o el cálculo para el que se evalúa el software.

💡 **Cómo se explica en la clase [B23-C08](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md):**
- Regla: «apto para el uso previsto» solo si todos los criterios marcados «uso» se cumplen.
- Aquí se cumplen, así que la decisión es APTO para el uso previsto.
- 🎯 **Por qué importa:** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.

📘 **Dónde se aprende** (1 clase): [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Usuario de pie

- Un usuario de pie y uno sentado tienen rangos de alcance distintos.

💡 **Cómo se explica en la clase [B109-C08](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md):**
- Con usuarios sintéticos (de pie: alcance inferior `700 ± 50 mm`, superior `1750 ± 90`; sentados: `450 ± 40` y `1300 ± 70`; mezcla `85 %` y `15 %`), la cobertura de una altura `h` es `Σ w (P(inferior ≤ h) · P(superior ≥ h))`.
- Una simulación de `100 000` usuarios (semilla `109008`) coincide con la analítica en menos de `0,01`.
- ⚠️ **Error frecuente:** Dimensionar para el usuario medio. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un control puesto «a la altura normal» deja fuera a quien no la alcanza. La decisión central: ¿a qué altura (o con qué ajuste) un puesto sirve al mayor número de usuarios y a quién deja fuera?

📘 **Dónde se aprende** (1 clase): [B109-C08 · Diseño inclusivo en hábitats](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md).

### UT1

- El ángulo de rotación terrestre (ERA) es el ángulo entre un origen celeste de referencia y un origen terrestre, que describe la rotación de la Tierra en torno a su eje; la convención IERS lo define como una función lineal de `UT1` (S1, ec. 5.14). UT1 es la escala de tiempo ligada a la rotación de la Tierra;

💡 **Cómo se explica en la clase [B13-C10](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md):**
- Según las Convenciones IERS 2010 (S1, ec. 5.14), `ERA(Tu) = 2π (0,779 057 273 264 0 + 1,002 737 811 911 354 48 Tu)` radianes, con `Tu = JD(UT1) − 2 451 545,0`.
- Las dos constantes (`0,7790572732640` vueltas en J2000.0 y `1,00273781191135448` vueltas por día de UT1) son definiciones (S1, Tabla 1.1).
- ⚠️ **Error frecuente:** Usar UTC como UT1 sin cuantificar el error. Se corrige con los ejercicios 8 y 11.
- 🎯 **Por qué importa:** Un telescopio en el desierto debe saber cuándo un objeto pasa por su meridiano, que es cuando está más alto y se observa mejor. Esa hora no es la del reloj civil: el cielo se adelanta casi cuatro minutos cada día.

📘 **Dónde se aprende** (1 clase): [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md).

### UT1 − UTC

- El movimiento polar `(x_p, y_p)` es el movimiento del CIP respecto de la corteza; está dominado por el bamboleo de Chandler (periodo de unos `435 d`) y una componente anual (S1, glosario y cap. 5). UT1 − UTC es la diferencia entre el tiempo de rotación terrestre y el civil; se mantiene por debajo de `0,9 s` con segundos intercalares (C09).

💡 **Cómo se explica en la clase [B13-C22](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md):**
- El ERA es función de UT1 (C10, S1 ec. 5.14); con `UT1 = UTC + (UT1 − UTC)` hay que sumar el valor publicado.
- Un error `δ` en `UT1 − UTC` gira la estación en `ω δ` radianes: con `ω = 7,292 115 × 10⁻⁵ rad/s` (S1, Tabla 1.2), `0,9 s` mueven un punto del ecuador `0,9 × 7,292 115 × 10⁻⁵ × 6 378 137 = 418,6 m`.
- ⚠️ **Error frecuente:** Omitir UT1 − UTC. Se corrige con los ejercicios 2, 7 y 9.
- 🎯 **Por qué importa:** Una estación terrestre apunta a una nave en el sistema celeste. Para ello debe saber cuánto ha girado la Tierra, hacia dónde apunta su eje en el cielo y dónde está ese eje dentro de la corteza.

📘 **Dónde se aprende** (1 clase): [B13-C22 · Parámetros de orientación terrestre: precesión, nutación, UT1 y movimiento polar](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md).

### UTC

- Muestra de auditoría: entradas revisadas. UTC: tiempo universal coordinado.

💡 **Cómo se explica en la clase [B96-C30](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué las marcas de tiempo deben ser UTC y no decrecientes?
- Datos SINTETICOS: operadores, acciones y marcas de tiempo ficticios (UTC fijo); semilla 96
- 🎯 **Por qué importa:** Sin registro verificable no se puede reconstruir un incidente ni demostrar quién aprobó un comando. La decisión central: ¿cómo se registra para que una alteración se detecte y cuánto hay que revisar en una auditoría?

📘 **Dónde se aprende** (1 clase): [B96-C30 · Registro y auditoría de operaciones](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md).

### Utilidad esperada

- La utilidad esperada de proceder es `(1 − p_f)·B − p_f·C`, que es positiva si `p_f < B/(B + C)`.

💡 **Cómo se explica en la clase [B111-C05](../programa/clases/B111/B111-C05-toma-de-decisiones-con-incertidumbre-en-equipo/CLASE.md):**
- *Descripción textual:* si los miembros son independientes, el grupo mejora al individuo; si siguen una señal común, no; la creencia se actualiza con Bayes y se decide comparando la utilidad esperada.
- Paso 4 · Decisión. `0,3333 > 0,20`: la utilidad esperada es `−66,667`; no proceder.
- 🎯 **Por qué importa:** B12 da herramientas estadísticas, no la decisión grupal bajo presión. La decisión central: ¿cuándo vale más el grupo que el individuo y cuándo la correlación borra esa ventaja?

📘 **Dónde se aprende** (1 clase): [B111-C05 · Toma de decisiones con incertidumbre en equipo](../programa/clases/B111/B111-C05-toma-de-decisiones-con-incertidumbre-en-equipo/CLASE.md).

### Utilización

- La utilización es la fracción de tiempo que la excavadora está ocupada.
- La utilización de una ventana es la suma de las demandas de las tareas activas (1,0 = capacidad).
- La utilización `U = Σ Cᵢ/Tᵢ`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B88-C01](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md):**
- T["Tareas: periodo y WCET"] --> U["Utilizacion de CPU"]
- *Descripción textual:* tres entradas (tareas, memorias y tasa de fallo) producen tres resultados (utilización, márgenes y fiabilidad) que se reúnen en una ficha de arquitectura.
- ⚠️ **Error frecuente:** Confundir utilización con margen. Un margen de 30 % significa `U = 0,70`, no `U = 0,30`
- 🎯 **Por qué importa:** Un computador de vuelo no se puede reparar en órbita, así que su arquitectura se decide con números antes de construirlo. La decisión central: ¿alcanzan la CPU y la memoria con margen, y qué redundancia compra qué fiabilidad?

📘 **Dónde se aprende** (5 clases): [B88-C01 · Arquitectura de computador de vuelo](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md); [B88-C43 · Pruebas de carga y estrés del software de vuelo](../programa/clases/B88/B88-C43-pruebas-de-carga-y-estres-del-software-de-vuelo/CLASE.md); [B96-C26 · Gestión de incidentes en la operación de estaciones](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md); [B97-C27 · Simulación de productividad de flotas de maquinaria](../programa/clases/B97/B97-C27-simulacion-de-productividad-de-flotas-de-maquinaria/CLASE.md); [B111-C03 · Carga cognitiva y gestión de la atención](../programa/clases/B111/B111-C03-carga-cognitiva-y-gestion-de-la-atencion/CLASE.md).

### Utilización de masa

- La utilización de masa `η_m` es la fracción del propelente que se ioniza y sale como ion.

💡 **Cómo se explica en la clase [B78-C07](../programa/clases/B78/B78-C07-motores-ionicos/CLASE.md):**
- Como el consumo total publicado es `3,25 mg/s`, la utilización de masa es `0,696`.
- *Descripción textual:* la tensión y la masa del ion dan su velocidad; el empuje fija el caudal de iones y la corriente; la ley de Child–Langmuir da la densidad máxima y con ella el área mínima; el caudal total da la utilización de masa.
- 🎯 **Por qué importa:** La velocidad de escape iónica crece con la raíz de la tensión, pero la corriente que cabe en una rejilla está limitada por la carga espacial. La decisión central: ¿qué tensión y qué área de rejilla se necesitan para un empuje dado y qué fracción del propelente llega a ser ion?

📘 **Dónde se aprende** (1 clase): [B78-C07 · Motores iónicos](../programa/clases/B78/B78-C07-motores-ionicos/CLASE.md).

### Utilización de recursos in situ

- La utilización de recursos in situ (ISRU) obtiene insumos fuera de la Tierra.

🎯 **Por qué importa (clase B119-C25):** B119 trata los tratados en general (C01, C05) y ninguna clase enseña los marcos de recursos ni el razonamiento económico que los motiva. La gobernanza se desarrolla en C36 y los aspectos técnicos en B59.

📘 **Dónde se aprende** (1 clase): [B119-C25 · Derecho y marcos de recursos espaciales](../programa/clases/B119/B119-C25-derecho-y-marcos-de-recursos-espaciales/CLASE.md).

### Utilización de recursos in situ (ISRU)

- La utilización de recursos in situ (ISRU) es el aprovechamiento de los recursos naturales locales del destino, según la definición que usa NASA (S2).

💡 **Cómo se explica en la clase [B59-C01](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md):**
- python programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/apalancamiento.py
- 🎯 **Por qué importa:** Cada kilogramo que se lanza arrastra consigo más propelente para lanzarlo. La decisión central: ¿cuánta masa de planta de producción compensa el oxidante que dejas de llevar?

📘 **Dónde se aprende** (1 clase): [B59-C01 · Concepto de utilización de recursos in situ](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md).

### Uv

- El plano uv (frecuencias espaciales en longitudes de onda).

💡 **Cómo se explica en la clase [B42-C10](../programa/clases/B42/B42-C10-interferometria-de-multiples-telescopios/CLASE.md):**
- Entre `−4 h` y `+4 h` hay `1164` puntos uv (con simetría hermitiana);
- `|uv|_máx = 5,8992 × 10⁷ λ` y `λ/|uv|_máx = 3,4965 mas`.
- ⚠️ **Error frecuente:** Olvidar la simetría hermitiana. Cada base da dos puntos uv.
- 🎯 **Por qué importa:** La resolución depende de la línea base, no del diámetro de cada telescopio, y la calidad de la imagen de la cobertura uv. La decisión central: ¿qué resolución y qué calidad de imagen da una disposición de telescopios?

📘 **Dónde se aprende** (1 clase): [B42-C10 · Interferometría de múltiples telescopios](../programa/clases/B42/B42-C10-interferometria-de-multiples-telescopios/CLASE.md).
