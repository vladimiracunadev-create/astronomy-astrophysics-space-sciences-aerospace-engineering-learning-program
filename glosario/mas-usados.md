# Los términos más usados del programa (parte 1 de 2)

[⬅️ Índice del glosario](README.md)

Los 179 términos que más clases comparten (desde 6 clases), en orden alfabético. Son el vocabulario transversal del programa: conviene dominarlos primero.

Partes: **1** · [2](mas-usados-2.md)

### Abundancia

*Aparece en 6 clases.*

- La abundancia es cuánto hay de un elemento; puede darse en número (átomos), en masa (kg) o con la escala logarítmica astronómica: ```text A(X) = log10(N_X / N_H) + 12 ``` donde `N_X` y `N_H` son números de átomos por unidad de volumen.
- La abundancia `Y` es cuántos núcleos de helio quedan, en unidades relativas.
- La abundancia es su fracción.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C02](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md):**
- Los astrónomos dan la abundancia de un elemento X respecto de hidrógeno con `A(X) = log10(N_X/N_H) + 12`.
- Concluyeron que las abundancias de carbono, nitrógeno, oxígeno y neón eran significativamente más bajas que las de valores usados una década antes; el nuevo resultado concuerda con las del vecindario solar y con meteoritos poco alterados, pero choca con los modelos del interior del Sol basados en heliosismología (S1).
- 🎯 **Por qué importa:** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?

📘 **Dónde se aprende:** [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md); [B24-C08 · Nucleosíntesis estelar](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md); [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B45-C14 · Composición química por espectros](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md); [B53-C29 · Imágenes hiperespectrales de superficies planetarias](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md); [B59-C02 · Prospección de hielo lunar](../programa/clases/B59/B59-C02-prospeccion-de-hielo-lunar/CLASE.md).

### Acoplamiento

*Aparece en 8 clases.*

- El acoplamiento mide cuánto depende una parte de otra: bajo acoplamiento significa que puedes cambiar una sin romper la otra.
- El acoplamiento `q` mide cuánto se filtran.
- El acoplamiento `χ` es la fracción de ese ritmo que se acumula.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C01](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md):**
- Detectar acoplamientos que impiden probar (estado global, entrada/salida dentro del cálculo).
- Ejercicio 8. Detecta dos acoplamientos en: `GM = 3.986e14` a nivel de módulo, `def T(a): print(...); return 2*pi*sqrt(a3/GM)`.
- 🎯 **Por qué importa:** Un script de 300 líneas que lee un archivo, calcula una órbita, dibuja una figura y escribe un informe funciona hasta el día en que cambias el archivo de entrada. Entonces no sabes si un resultado distinto viene de los datos, de la fórmula o de un error nuevo.

📘 **Dónde se aprende:** [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md); [B37-C12 · Gigantes rojas oscilantes y modos mixtos](../programa/clases/B37/B37-C12-gigantes-rojas-oscilantes-y-modos-mixtos/CLASE.md); [B42-C15 · Espejos deformables](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md); [B57-C20 · Caso de estudio climático o geológico de Chile](../programa/clases/B57/B57-C20-caso-de-estudio-climatico-o-geologico-de-chile/CLASE.md); [B78-C17 · Masa de propelente y presupuesto](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md); [B97-C15 · Impresión 3D espacial](../programa/clases/B97/B97-C15-impresion-3d-espacial/CLASE.md) y 2 más.

### Afelio

*Aparece en 6 clases.*

- El perihelio es el punto más cercano al Sol (`a(1−e)`) y el afelio, el más lejano (`a(1+e)`).
- El perihelio `q` es el punto de la órbita más cercano al Sol (que está en un foco) y el afelio `Q` el más lejano.
- El perihelio es el punto más cercano al Sol; el afelio, el más lejano.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C14](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md):**
- Con `a = 227,956` millones de km (Marte, S3) y una excentricidad sintética `e = 0,2`: perihelio `a(1−e) = 182,4` y afelio `a(1+e) = 273,5` millones de km.
- El laboratorio calcula el área barrida durante un décimo del período partiendo del perihelio y durante otro décimo partiendo del afelio: ambas valen `1,5995×10⁴` (unidades de 10¹² km²) y su razón es `1,000000`.
- 🎯 **Por qué importa:** Para Kepler, como para todos antes, el círculo era la figura natural del cielo. Los datos de Tycho no se dejaban describir con círculos.

📘 **Dónde se aprende:** [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md); [B75-C01 · Geometría de transferencias heliocéntricas](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md); [B131-C03 · Conocimientos previos y concepciones alternativas](../programa/clases/B131/B131-C03-conocimientos-previos-y-concepciones-alternativas/CLASE.md).

### Ajuste

*Aparece en 7 clases.*

- El ajuste es el procedimiento que elige los parámetros que dejan menores residuos.
- Un ajuste es la curva que mejor representa los datos según un criterio.
- El ajuste de `AVAR` es lineal en `N²` y `K²`.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- Con 8 planetas (S3), el ajuste da `p = 1,4978` y `k = 0,9998`, es decir, `T = 0,9998·a^1,4978`.
- El ajuste mejora apenas, a costa de un parámetro más: no hay motivo para preferirlo.
- ⚠️ **Error frecuente:** Exigir un ajuste perfecto. Ejercicio 11.
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?

📘 **Dónde se aprende:** [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md); [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md); [B85-C14 · Degradación ultravioleta](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md); [B87-C04 · Sensores terrestres](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md); [B87-C06 · Giroscopios MEMS](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md) y 1 más.

### Alcance

*Aparece en 13 clases.*

- El alcance es hasta dónde pretende llegar la respuesta.
- El alcance (*scope*) es la región donde un nombre existe: una variable creada dentro de la función es local.
- El alcance (o distancia de horizonte) es hasta donde se supera el umbral.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C06](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md):**
- La pregunta cambia de medir a calcular con datos publicados; sigue siendo investigable y declara su alcance.
- 🎯 **Por qué importa:** «¿Hay vida en otros planetas?» es una pregunta legítima y apasionante, pero nadie puede responderla con un cuaderno y una cámara de teléfono. «¿Cambia el tamaño aparente de la Luna a lo largo de un mes?» sí puede responderse con una cámara y un trípode, y su respuesta enseña algo real sobre la órbita lunar.

📘 **Dónde se aprende:** [B01-C06 · Preguntas investigables en astronomía](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md); [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md); [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md); [B31-C09 · Interacciones fundamentales](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md); [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md); [B53-C07 · Topografía por altimetría](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md) y 7 más.

### Altura de escala

*Aparece en 18 clases.*

- La altura de escala `H` es la distancia en que la presión baja un factor `e` en una atmósfera isoterma.
- La altura de escala `H` es la altura a la que la presión de una atmósfera isoterma cae por un factor `e ≈ 2,718`.
- La altura de escala `H` de una atmósfera exponencial es la altitud en la que la densidad cae a `1/e`.
- *(y 8 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C14](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md):**
- La atmósfera real no es isoterma: la temperatura cambia con la altura, así que el modelo solo sirve a escala didáctica y a altitudes moderadas; a 100 km da 0,72 Pa, un valor que no debe tomarse como medida (el modelo ya no vale).
- Deducir y usar la atmósfera isoterma (presión frente a altura) y su altura de escala.
- 🎯 **Por qué importa:** La cabina de una nave contiene aire a una presión que debe mantenerse, y una escotilla soporta decenas de miles de newtons. La pregunta motivadora es: ¿qué relaciona presión, volumen, temperatura y cantidad de gas, y cómo cambia la presión con la altura en una atmósfera?

📘 **Dónde se aprende:** [B05-C14 · Gases y presión](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md); [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md); [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md); [B29-C11 · Atmósferas exoplanetarias](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md); [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md); [B30-C17 · Auroras y corrientes ionosféricas](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md) y 12 más.

### Amortiguamiento

*Aparece en 6 clases.*

- El amortiguamiento disipa energía; su medida adimensional es `ζ` (razón de amortiguamiento).
- La rigidez `Kp` y el amortiguamiento `Kd` son las ganancias del control.
- En un sistema de segundo orden, la frecuencia natural `ωn` (rad/s) y el amortiguamiento `ζ` (adimensional) fijan la forma: `θ̈ + 2ζωn θ̇ + ωn² θ = ωn² r`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- Menos amortiguamiento, más amplificación; por eso se evita excitar una estructura en su frecuencia propia.
- Los resultados valen si `F = −k x` (resorte lineal, deformaciones pequeñas) y si el amortiguamiento es simple.
- ⚠️ **Error frecuente:** Ignorar el amortiguamiento al hablar de resonancia. Ejercicio 7.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende:** [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md); [B87-C17 · Control de tres ejes](../programa/clases/B87/B87-C17-control-de-tres-ejes/CLASE.md); [B107-C07 · Rehabilitación vestibular y del equilibrio posterior al vuelo](../programa/clases/B107/B107-C07-rehabilitacion-vestibular-y-del-equilibrio-posterior-al-vuelo/CLASE.md).

### Amplitud

*Aparece en 8 clases.*

- La amplitud `A` es el desplazamiento máximo;
- La amplitud `A` es su valor máximo desde el centro.
- La amplitud `A_x` es la distancia de partida a L1.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- El período es `T = 2π√(m/k)`, independiente de la amplitud.
- Con roce proporcional a la velocidad, la amplitud decae exponencialmente.
- ⚠️ **Error frecuente:** Pensar que el período depende de la amplitud. Ejercicio 9.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende:** [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md); [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md); [B40-C05 · Perturbaciones primordiales y espectro escalar](../programa/clases/B40/B40-C05-perturbaciones-primordiales-y-espectro-escalar/CLASE.md); [B73-C05 · Órbitas periódicas](../programa/clases/B73/B73-C05-orbitas-periodicas/CLASE.md) y 2 más.

### Ángulo

*Aparece en 7 clases.*

- Un ángulo es adimensional en el SI; el radián es la unidad coherente.
- El ángulo `ψ` es el que forma con la dirección radial.
- El ángulo entre vectores no nulos cumple `cos θ = ⟨u, v⟩/(‖u‖‖v‖)`.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B10-C06](../programa/clases/B10/B10-C06-producto-interno-y-ortogonalidad/CLASE.md):**
- Gracias a ella el coseno de la fórmula del ángulo nunca sale de `[−1, 1]`.
- C -->|"> 0"| D["ángulo agudo:<br/>apuntan hacia el mismo lado"]
- 🎯 **Por qué importa:** La potencia que recibe un panel solar depende del ángulo entre su normal y la dirección al Sol: más inclinado, menos luz. El control de actitud, la orientación de antenas y de instrumentos usan el mismo cálculo.

📘 **Dónde se aprende:** [B10-C06 · Producto interno y ortogonalidad](../programa/clases/B10/B10-C06-producto-interno-y-ortogonalidad/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md); [B30-C10 · Viento solar y heliosfera](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md); [B32-C01 · Ecuación de transferencia radiativa en atmósferas estelares](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md); [B40-C08 · Polarización E y B del fondo cósmico](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md); [B45-C15 · Polarización lineal y circular](../programa/clases/B45/B45-C15-polarizacion-lineal-y-circular/CLASE.md) y 1 más.

### Ángulo horario

*Aparece en 7 clases.*

- El ángulo horario `H` es el ángulo, medido hacia el oeste, entre el meridiano y el círculo que pasa por el astro y los polos; vale cero cuando el astro cruza el meridiano (tránsito o culminación, S2).
- La declinación `δ` de un astro es su latitud celeste; el ángulo horario `H` crece con la rotación de la Tierra.
- El ángulo horario `H` de una dirección es el ángulo local menos su ascensión recta: `H = 0` en la culminación.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C04](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md):**
- El intervalo salida–tránsito (5,5 h) supera las 5,3 h porque la Luna avanza hacia el este entre las estrellas (≈ 0,6° por hora) y su ángulo horario crece algo más despacio que el del cielo.
- El ángulo horario es el puente: `H = TSL − α`.
- ⚠️ **Error frecuente:** Confundir el ángulo horario con la AR. Ejercicio 2.
- 🎯 **Por qué importa:** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».

📘 **Dónde se aprende:** [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md); [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B46-C14 · Líneas de base interferométricas](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md); [B48-C04 · Planificación por visibilidad](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md) y 1 más.

### Apertura

*Aparece en 8 clases.*

- La apertura `D` es el diámetro de la abertura que recoge la luz (pupila o espejo).
- La apertura `D` es el diámetro del objetivo o espejo; la distancia focal `F`, la longitud del camino óptico; la razón focal `N = F/D`.
- La exposición es el tiempo con el obturador abierto; el ISO es la amplificación de la señal; la apertura relativa del objetivo (f/) controla la luz.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C10](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md):**
- La luz del objeto pasa por el rango espectral del detector, por la apertura que fija cuánta luz entra, por la resolución que decide qué detalle se separa y por la percepción que interpreta; al final hay un registro o una impresión.
- Límite: los cuellos no son independientes; por ejemplo, ampliar la apertura mejora a la vez la luz captada y la resolución.
- 🎯 **Por qué importa:** Si el ojo bastara, no habría observatorios. La luz visible es una franja pequeña del espectro electromagnético (S1, S2); además, tu pupila recoge poca luz, separa detalles hasta cierto tamaño y puede engañarte.

📘 **Dónde se aprende:** [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md); [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md); [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md); [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md); [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B42-C02 · Principio de Huygens-Fresnel](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md) y 2 más.

### Arrastre

*Aparece en 9 clases.*

- El arrastre es la traza que deja un objeto que se mueve durante la exposición.
- El arrastre `φ` es la fracción de la concentración de la salmuera que pasa al vapor.
- El arrastre es `D = Cd·(ρV²/2)·A`.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B54-C07](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md):**
- Límite: el globo es un objeto cerrado; la parcela se mezcla y pierde energía por arrastre y por el peso de las gotas.
- Por balance de momento con arrastre: incluye mezcla (no se desarrolla aquí).
- 🎯 **Por qué importa:** La energía convectiva disponible decide si una tormenta tiene vigor o no. La pregunta motivadora: ¿cuánta velocidad puede alcanzar el aire que sube si toda la flotabilidad se convierte en movimiento?

📘 **Dónde se aprende:** [B54-C07 · Dinámica de tormentas](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md); [B58-C06 · Astrometría de objetos menores](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md); [B59-C07 · Purificación de agua](../programa/clases/B59/B59-C07-purificacion-de-agua/CLASE.md); [B77-C02 · Movimiento en atmósfera](../programa/clases/B77/B77-C02-movimiento-en-atmosfera/CLASE.md); [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md); [B77-C09 · Pérdidas aerodinámicas](../programa/clases/B77/B77-C09-perdidas-aerodinamicas/CLASE.md) y 3 más.

### Autocorrelación

*Aparece en 6 clases.*

- La autocorrelación `r_k` mide cuánto se parece la serie a sí misma desplazada `k` muestras; el número `k` es el retardo (en inglés *lag*).
- La autocorrelación es la semejanza entre observaciones cercanas en el tiempo.
- La autocorrelación mide la repetición.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C01](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md):**
- Con la media `x̄`, la autocorrelación muestral al retardo `k` es
- C --> E["Memoria:<br/>autocorrelación r_k"]
- 🎯 **Por qué importa:** Un telescopio espacial mide el brillo de una estrella cada dos minutos durante semanas. Lo que llega a tierra no es una curva continua, sino una tabla de números.

📘 **Dónde se aprende:** [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B17-C09 · Prevención de fuga de datos](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md); [B30-C03 · Ciclo de actividad solar](../programa/clases/B30/B30-C03-ciclo-de-actividad-solar/CLASE.md); [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md); [B48-C06 · Meteorología de observatorios](../programa/clases/B48/B48-C06-meteorologia-de-observatorios/CLASE.md); [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md).

### Banda

*Aparece en 6 clases.*

- Una banda es un intervalo de energía.
- La banda es el intervalo de longitudes de onda observado.
- Una banda es una imagen en un intervalo espectral.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C02](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md):**
- Cada banda es una ventana distinta al mismo objeto: el radio ve gas frío y electrones en campos magnéticos, el óptico ve estrellas, los rayos X ven gas a millones de grados.
- La evidencia es la ficha de bandas y temperaturas del ejercicio 12 (sección 20).
- ⚠️ **Error frecuente:** Tomar las bandas ilustrativas por límites oficiales. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Cada banda revela un proceso distinto; combinarlas exige convertir bien las unidades y saber qué banda corresponde a qué temperatura. La decisión central: ¿en qué banda emite un objeto de temperatura dada y cómo se pasa de una magnitud a otra sin error?

📘 **Dónde se aprende:** [B28-C02 · Fotones en múltiples longitudes de onda](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md); [B40-C14 · Productos de datos de Planck y misiones del CMB](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md); [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md); [B44-C04 · Eficiencia cuántica espectral](../programa/clases/B44/B44-C04-eficiencia-cuantica-espectral/CLASE.md); [B57-C05 · Imágenes multiespectrales](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md); [B75-C29 · Análisis de calendario con gráficos pork-chop](../programa/clases/B75/B75-C29-analisis-de-calendario-con-graficos-pork-chop/CLASE.md).

### Barrido

*Aparece en 6 clases.*

- El barrido es la medición paso a paso.
- El barrido es el ancho de la franja que se imagina en cada pasada.
- El barrido repite el método con resoluciones distintas (`N = 2ᵏ`).
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C26](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md):**
- Barrido: `N = 2ᵏ` pasos para los fijos y tolerancias `10⁻⁴ … 10⁻¹⁰` para el adaptativo.
- Evaluaciones mínimas del barrido para alcanzar cada error objetivo:
- 🎯 **Por qué importa:** «El método A es mejor que el B» es una afirmación vacía sin el problema, la métrica, la tolerancia y el costo. Una comparación mal diseñada lleva a elegir el algoritmo equivocado para una misión.

📘 **Dónde se aprende:** [B11-C26 · Benchmark de algoritmos numéricos](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md); [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B49-C05 · Medición y calibración de patrones de antena](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md); [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md); [B75-C12 · Optimización de trayectoria](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md); [B88-C04 · Memorias y corrección de errores](../programa/clases/B88/B88-C04-memorias-y-correccion-de-errores/CLASE.md).

### Base

*Aparece en 8 clases.*

- La base (o referencia) es la cantidad respecto de la cual se expresa el porcentaje.
- `a` es la base y `n` el exponente.
- El paralaje es el cambio de dirección de un objeto visto desde dos puntos distintos; la base es la distancia entre ellos.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C03](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md):**
- Los mismos dos valores dan dos porcentajes distintos porque la base cambia.
- No se anulan, porque la segunda operación toma como base el valor ya modificado.
- ⚠️ **Error frecuente:** Olvidar la base. Ejercicios 4 y 11.
- 🎯 **Por qué importa:** La Tierra no gira en un círculo: su distancia al Sol varía a lo largo del año. ¿Mucho o poco?

📘 **Dónde se aprende:** [B03-C03 · Porcentajes y escalas comparativas](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md); [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md); [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md); [B04-C07 · Triángulos y distancias angulares](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md); [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md); [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md) y 2 más.

### Bootstrap

*Aparece en 9 clases.*

- El filtro bootstrap es la versión que propaga con el modelo y pesa con la verosimilitud (S1 lo atribuye a Gordon y colaboradores, 1993).
- Un bootstrap remuestrea los pares (pronóstico, evento) con reemplazo para estimar la variabilidad de una métrica.
- El bootstrap estima la incertidumbre de una métrica remuestreando.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C24](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md):**
- El bootstrap con 1 000 remuestras da un intervalo del 95 % para el BSS de `[0,020; 0,064]`: la habilidad es positiva con la muestra dada, pero pequeña y con un rango relativo amplio.
- *Descripción textual:* de los pronósticos y eventos se calcula el puntaje de Brier y, con una referencia, el BSS; con un umbral se arma la tabla de contingencia y de ella POD, POFD, TSS y HSS; un bootstrap da la incertidumbre de las métricas; el informe declara referencia, umbral, muestra y límites.
- 🎯 **Por qué importa:** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.

📘 **Dónde se aprende:** [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md); [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md); [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md); [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md); [B103-C06 · Detección y catalogación de rocas en imágenes de superficie](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md) y 3 más.

### Cadencia

*Aparece en 6 clases.*

- La cadencia es el intervalo entre observaciones;
- La cadencia `Δt` es el intervalo entre muestras consecutivas.
- La cadencia `D_cad` es el intervalo entre visitas.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C22](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md):**
- El laboratorio lo comprueba: entre `t = 3600 s` y `7200 s`, un instrumento con cadencia de 12 s tiene `3600/12 = 300` registros, con el último en `7188 s`; el de `7200 s` no cuenta.
- Antes de ejecutar, calcula cuántos registros esperas. 24 h con cadencia de 12 s: 7200 registros por banda; la búsqueda devuelve 7200.
- 🎯 **Por qué importa:** Quieres estudiar una región activa del Sol durante un día usando imágenes ultravioleta. Hay cientos de miles de archivos repartidos en varios proveedores.

📘 **Dónde se aprende:** [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md); [B34-C09 · Integración multiinstrumento de datos heliofísicos](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md); [B37-C13 · Series fotométricas de Kepler, TESS y PLATO para asterosismología](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md); [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Calibración

*Aparece en 14 clases.*

- La calibración es la operación que, bajo condiciones especificadas, establece primero una relación entre los valores de los patrones (con sus incertidumbres) y las indicaciones correspondientes (con las suyas) y luego usa esa relación para obtener un resultado de medida a partir de una indicación (S1, 2.39).
- La calibración de un intervalo es su cobertura empírica frente a su cobertura declarada.
- La calibración es el trabajo conjunto de los evaluadores con ejemplares.
- *(y 11 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C05](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md):**
- Para una indicación media `y₀` de `m` lecturas de una fuente desconocida: `x̂₀ = (y₀ − â)/b̂`, con `u(x̂₀) = (s/|b̂|) √(1/m + 1/n + (x̂₀ − x̄)²/Sxx)` (fórmula clásica de la calibración lineal inversa; no se consultó una fuente específica en esta clase).
- Se interpreta así: el primer término es el ruido de las `m` lecturas nuevas, el segundo es la incertidumbre de la recta en su centro, y el tercero crece cuando `x̂₀` se aleja del centro de calibración.
- ⚠️ **Error frecuente:** Extrapolar fuera del intervalo de calibración. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Un sensor solar de una nave devuelve cuentas digitales (DN), no vatios por metro cuadrado. Para saber cuánta luz recibe hay que haberlo expuesto antes a fuentes de irradiancia conocida y haber establecido la relación entre ambas.

📘 **Dónde se aprende:** [B13-C05 · Calibración instrumental](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md); [B13-C20 · Validación de una cadena de medida](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md); [B28-C22 · Inferencia bayesiana conjunta de parámetros de fuente multimensajero](../programa/clases/B28/B28-C22-inferencia-bayesiana-conjunta-de-parametros-de-fuente-multimensajero/CLASE.md); [B29-C07 · Métodos de validación planetaria](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md); [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md); [B38-C09 · Validación de galaxias simuladas frente a observaciones](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md) y 8 más.

### Campo de visión

*Aparece en 6 clases.*

- El campo de visión es el ángulo de cielo visible.
- El campo de visión (real) es el ángulo de cielo que ves; el campo aparente es el ángulo que ocupa la imagen en tu vista; el real es aproximadamente `aparente/M`.
- El campo de visión es el ángulo total de la línea.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B57-C24](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md):**
- El campo de visión de la línea es `20,90°` (Tierra plana).
- G["paso de pixel"] --> F["focal y campo de vision"]
- 🎯 **Por qué importa:** Cada requisito empuja a los demás: más resolución exige más datos, más barrido exige un campo de visión mayor, y el enlace de bajada limita cuánto se puede adquirir. La decisión central: ¿qué requisito se relaja cuando el presupuesto de datos no cierra?

📘 **Dónde se aprende:** [B02-C13 · Galileo y primeras observaciones telescópicas](../programa/clases/B02/B02-C13-galileo-y-primeras-observaciones-telescopicas/CLASE.md); [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md); [B57-C24 · Diseño de una carga útil de observación terrestre](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md); [B58-C11 · Observaciones de seguimiento](../programa/clases/B58/B58-C11-observaciones-de-seguimiento/CLASE.md); [B74-C14 · Navegación con cámaras estelares](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md); [B87-C03 · Sensores solares](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md).

### Capa

*Aparece en 7 clases.*

- Una capa es el resultado de una instrucción apilada sobre las anteriores.
- Una capa es un conjunto de datos servido.
- Una capa es un cascarón de densidad uniforme.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- Si cambia solo `analisis.py`, se reutilizan 4 capas y se reconstruyen 3; si cambia `uv.lock`, se reutilizan 2 y se reconstruyen 5 (incluida la instalación, la lenta).
- El orden «dependencias primero, código después» ahorra la capa lenta cuando cambia el código.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende:** [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md); [B14-C29 · Servicios de datos geoespaciales estándar (OGC)](../programa/clases/B14/B14-C29-servicios-de-datos-geoespaciales-estandar-ogc/CLASE.md); [B53-C01 · Interior de planetas rocosos](../programa/clases/B53/B53-C01-interior-de-planetas-rocosos/CLASE.md); [B88-C23 · Arquitectura de software de vuelo: capas y ejecutivo](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md); [B118-C01 · Población de objetos orbitales](../programa/clases/B118/B118-C01-poblacion-de-objetos-orbitales/CLASE.md); [B122-C04 · Seguridad de estaciones terrestres y segmento de control](../programa/clases/B122/B122-C04-seguridad-de-estaciones-terrestres-y-segmento-de-control/CLASE.md) y 1 más.

### Ciclo

*Aparece en 8 clases.*

- Un ciclo es un fenómeno que se repite, como una vuelta de la Tierra sobre su eje o de la Luna alrededor de la Tierra.
- Un ciclo es una contradicción.
- Un ciclo es un paso al caliente y al frío.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- El tiempo se mide contando ciclos regulares.
- Pero cada ciclo se puede medir de más de una manera, y eso produce unidades distintas.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).

📘 **Dónde se aprende:** [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B30-C03 · Ciclo de actividad solar](../programa/clases/B30/B30-C03-ciclo-de-actividad-solar/CLASE.md); [B53-C09 · Estratigrafía planetaria](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md); [B85-C19 · Ensayos de vacío térmico](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md); [B97-C25 · Excavación y manejo de regolito con robots](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md); [B109-C03 · Accesos, esclusas y transferencia entre ambientes presurizados](../programa/clases/B109/B109-C03-accesos-esclusas-y-transferencia-entre-ambientes-presurizados/CLASE.md) y 2 más.

### Cobertura

*Aparece en 29 clases.*

- La cobertura es la fracción real de intervalos que contienen el parámetro; la cobertura nominal es la que se declara.
- La cobertura de un intervalo es esa fracción.
- La cobertura de un intervalo es la fracción de repeticiones en que contiene la verdad.
- *(y 26 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C08](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md):**
- Con 100 000 repeticiones del experimento: la cobertura del intervalo `t` es `0,9507`; con `σ` conocida y 1,96, `0,9518`; con `s` estimada pero 1,96 (error común), `0,9199`: un «95 %» que en realidad es 92 %.
- D --> E["Cobertura:<br/>≈ 95 % contienen μ"]
- 🎯 **Por qué importa:** Un número sin rango es una afirmación sin evidencia de su precisión. «La distancia es 148,5 m» no dice si el valor es fiable al metro o al decámetro. Un intervalo con su nivel de confianza lo dice, y permite decidir si una medición cumple un requisito o si hay que tomar más datos.

📘 **Dónde se aprende:** [B12-C08 · Intervalos de confianza](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md); [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md); [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md); [B26-C20 · Límites observacionales de modelos cosmológicos](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md); [B28-C10 · Localización probabilística de eventos](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md); [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md) y 23 más.

### Coeficiente balístico

*Aparece en 7 clases.*

- El coeficiente balístico `B = m/(Cd A)` (kg/m²) mide cuánto resiste un cuerpo al frenado: a mayor `B`, menos arrastre.
- El coeficiente balístico es `β = m/(Cd A)`.
- El coeficiente balístico `m/(Cd·A)` mide qué tan fácil lo frena el aire.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B72-C06](../programa/clases/B72/B72-C06-arrastre-atmosferico/CLASE.md):**
- *Descripción textual:* la densidad y el coeficiente balístico dan la aceleración; esta da el decaimiento por vuelta, corregido por la rotación del aire, y de él sale la vida útil.
- Por coeficiente balístico: `B` en kg/m².
- 🎯 **Por qué importa:** Una estación o una constelación baja debe reimpulsarse y un satélite sin propulsión debe reentrar a tiempo. La decisión central: ¿cuánto baja un satélite por vuelta y en cuántos días reentra, según su masa, su área y la densidad del aire?

📘 **Dónde se aprende:** [B72-C06 · Arrastre atmosférico](../programa/clases/B72/B72-C06-arrastre-atmosferico/CLASE.md); [B75-C15 · Aerofrenado conceptual](../programa/clases/B75/B75-C15-aerofrenado-conceptual/CLASE.md); [B77-C02 · Movimiento en atmósfera](../programa/clases/B77/B77-C02-movimiento-en-atmosfera/CLASE.md); [B77-C14 · Dinámica de reentrada](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md); [B96-C18 · Fin de vida y disposición orbital](../programa/clases/B96/B96-C18-fin-de-vida-y-disposicion-orbital/CLASE.md); [B118-C12 · Disposición al fin de vida](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md) y 1 más.

### Completitud

*Aparece en 9 clases.*

- La completitud es la fracción de fuentes reales de un flujo dado que se detectan.
- La completitud es la fracción de los objetos que cumplen el criterio y están en el catálogo.
- La completitud es el diámetro por encima del cual no falta ningún cráter.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- La completitud es 50 % cuando la SNR iguala al umbral y sube rápido unas unidades por encima.
- Predecir la tasa de falsas alarmas y la completitud para un umbral dado.
- ⚠️ **Error frecuente:** Reportar el catálogo sin completitud ni falsas alarmas. Se corrige con el ejercicio 12.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.

📘 **Dónde se aprende:** [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B25-C19 · Catálogos y sesgos de selección](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md); [B53-C08 · Cartografía de cráteres](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md); [B74-C22 · Informe de navegación verificable](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md); [B96-C16 · Gestión de datos científicos](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md); [B118-C21 · Calidad, latencia y trazabilidad de datos de vigilancia espacial](../programa/clases/B118/B118-C21-calidad-latencia-y-trazabilidad-de-datos-de-vigilancia-espacial/CLASE.md) y 3 más.

### Composición

*Aparece en 6 clases.*

- Una composición es una función dentro de otra.
- La composición de *boosts* es el producto de matrices.
- La composición `g(f(x))` aplica primero `f` y luego `g`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Una composición típica: pasar de `P` en días a años con `g(P) = P/365,25` y luego aplicar otra regla.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.

📘 **Dónde se aprende:** [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md); [B09-C04 · Reglas de derivación](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md); [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md); [B26-C02 · Transformaciones de Lorentz](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md); [B57-C05 · Imágenes multiespectrales](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md).

### Concentración

*Aparece en 6 clases.*

- La concentración es `c = r₂₀₀/r_s`.
- La concentración `C = R80/R20` es el cociente entre los radios que contienen el 80 % y el 20 % de la luz.
- La concentración `C` es masa por volumen (mg/m³) o fracción de volumen (ppm).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- Si un ácido fuerte monoprótico tiene concentración `c`, `[H⁺] ≈ c` y `pH = −log₁₀ c`.
- Para `HA ⇌ H⁺ + A⁻` con `K_a` y concentración inicial `c`, si se ioniza `x`: `K_a = x²/(c − x)`, es decir, `x² + K_a x − K_a c = 0`, con solución `x = [−K_a + √(K_a² + 4K_a c)]/2`.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.

📘 **Dónde se aprende:** [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md); [B25-C15 · Materia oscura en galaxias](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md); [B117-C02 · Contención de riesgos biológicos y químicos en cabina](../programa/clases/B117/B117-C02-contencion-de-riesgos-biologicos-y-quimicos-en-cabina/CLASE.md); [B122-C01 · Dependencias de proveedores y cadena de suministro de infraestructura espacial](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md).

### Constante de tiempo

*Aparece en 11 clases.*

- La constante de tiempo `τ` es el tiempo en que la diferencia con el equilibrio se reduce a `1/e ≈ 36,8 %`.
- La constante de tiempo `τ` de un sensor de primer orden es el tiempo en que recorre el 63,2 % de un cambio brusco (`1 − e^{−1}`).
- La constante de tiempo `τ_c` de un sistema de primer orden es el tiempo en el que la respuesta a un escalón alcanza el 63,2 % de su valor final.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C03](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md):**
- La velocidad terminal es `g m/c = 196,1 m/s`, se alcanza con una constante de tiempo `m/c = 20 s`, y a los 30 s la velocidad es `152,4 m/s`.
- Interpretar la constante de tiempo y el equilibrio.
- ⚠️ **Error frecuente:** Mezclar la constante de tiempo con la velocidad. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Muchos procesos espaciales relajan hacia un equilibrio: una cápsula que cae frena hasta una velocidad terminal, un instrumento se enfría hacia la temperatura de su entorno, una población de partículas decae.

📘 **Dónde se aprende:** [B11-C03 · Ecuaciones de primer orden](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md); [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B43-C11 · Dilatación térmica y estabilidad](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md); [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md); [B85-C11 · Ciclos térmicos](../programa/clases/B85/B85-C11-ciclos-termicos/CLASE.md) y 5 más.

### Contraste

*Aparece en 8 clases.*

- El contraste `c = (T_m/T_ef)⁴` es el cociente entre el flujo por unidad de área de la mancha y el del entorno.
- El contraste es el cociente de flujos planeta/estrella.
- El contraste WCAG es `(L₁ + 0,05)/(L₂ + 0,05)` con `L` la luminancia relativa.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C12](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md):**
- A["Mancha: radio ρ,<br/>contraste c"] --> B["Área proyectada<br/>A cos γ(t)"]
- Definir mancha, contraste y modulación rotacional.
- 🎯 **Por qué importa:** La modulación del brillo por manchas permite medir el periodo de rotación de miles de estrellas sin necesitar espectros, pero también contamina la búsqueda de exoplanetas y limita la precisión de las velocidades radiales.

📘 **Dónde se aprende:** [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md); [B29-C06 · Imagen directa de exoplanetas](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md); [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md); [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md); [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md); [B53-C26 · Publicación de mapas geológicos planetarios: estándares y leyendas](../programa/clases/B53/B53-C26-publicacion-de-mapas-geologicos-planetarios-estandares-y-leyendas/CLASE.md) y 2 más.

### Convolución

*Aparece en 7 clases.*

- La convolución de `x` y `h` es `(x ∗ h)[n] = Σ_m x[m] h[n − m]` (la definición de NumPy en S2 es la misma con otro orden de nombres: se voltea una secuencia y se desliza sobre la otra).
- La convolución de `h` y `u` es `(h∗u)(t) = ∫₀ᵗ h(t−s) u(s) ds` (fuente S2).
- La convolución (en redes, una correlación cruzada: producto punto de un núcleo con cada ventana de la imagen, sin invertir el núcleo) produce un mapa de respuestas; en modo válido la salida mide `N − k + 1` por lado.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- Resulta `y[n] = Σ_m x[m] h[n − m]`: la convolución.
- La media móvil de C07 es la convolución con `h[m] = 1/M`.
- ⚠️ **Error frecuente:** Multiplicar DFT sin rellenar y creer que se obtiene la convolución lineal. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.

📘 **Dónde se aprende:** [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md); [B32-C06 · Micro y macroturbulencia y granulación estelar](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md); [B32-C11 · Ensanchamiento rotacional y v sin i](../programa/clases/B32/B32-C11-ensanchamiento-rotacional-y-v-sin-i/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md) y 1 más.

### Corrección

*Aparece en 6 clases.*

- La corrección es el valor que se suma para compensar un sesgo conocido.
- La corrección en el instante `t` es `dv(t) = −Φ_rv(T,t)⁻¹ [Φ_rr(T,t) δr(t) + Φ_rv(T,t) δv(t)]`.
- La detección es que el error se advierta; la corrección, que se acepte y se repare.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C04](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md):**
- La corrección resultante hereda esa incertidumbre;
- *Descripción textual:* una lectura se descompone en verdad, sesgo y ruido; el promedio solo reduce el ruido; el sesgo se elimina con una corrección obtenida de un patrón.
- 🎯 **Por qué importa:** Una estación mide el instante de llegada de un pulso de una baliza. Cada lectura fluctúa por ruido electrónico, y además hay un retardo constante del cable que nadie incluyó.

📘 **Dónde se aprende:** [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B74-C08 · Filtrado recursivo de estados](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md); [B81-C15 · Robustez de trayectoria ante fallas](../programa/clases/B81/B81-C15-robustez-de-trayectoria-ante-fallas/CLASE.md); [B104-C07 · Factores de liderazgo](../programa/clases/B104/B104-C07-factores-de-liderazgo/CLASE.md); [B104-C12 · Robótica tripulada](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md).

### Correlación

*Aparece en 7 clases.*

- La correlación `ρ` entre dos medidas cambia la incertidumbre combinada: `σ² = 1/(1ᵀC⁻¹1)`.
- La correlación de Pearson.
- Ruido: error independiente de cada revisor. Correlación: acuerdo lineal entre nota y mérito.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B26-C21](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md):**
- Con dos medidas de `σ = 0,018` y `0,015` y correlación `ρ`, la incertidumbre combinada es `0,01152` si `ρ = 0`, `0,01400` si `ρ = 0,5` y `0,01483` si `ρ = 0,9`: la correlación quita información.
- Incluir una correlación entre dos medidas.
- 🎯 **Por qué importa:** Ninguna sonda fija sola todos los parámetros; combinarlas reduce la incertidumbre, pero solo si son compatibles entre sí y si se tratan bien sus correlaciones. La decisión central: dadas tres restricciones sobre `Ω_m`, ¿cuál es el valor combinado, qué incertidumbre tiene y son consistentes entre sí?

📘 **Dónde se aprende:** [B26-C21 · Verosimilitud cosmológica con datos combinados](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md); [B33-C01 · Validación de modelos MHD con eventos solares documentados](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md); [B34-C07 · Comparación de modelos coronales con observaciones](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md); [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md); [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md) y 1 más.

### Cota

*Aparece en 7 clases.*

- Una cota es un valor que el resultado no debería superar (superior) o no debería bajar de él (inferior).
- Un error de redondeo es la diferencia entre el valor y su redondeo; su cota es el máximo posible: ±media unidad de la última cifra conservada (`365` → ±0,5).
- La cota es un límite superior, no una medición del valor.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C11](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md):**
- D --> E["Reportar con unidad, cifras y cota"]
- Primero se estima con una cifra; luego se calcula sin redondear; se compara con la estimación; se redondea al final según la calidad de los datos; y se reporta con unidad, cifras y cota.
- 🎯 **Por qué importa:** Si te piden el tiempo que tarda la luz del Sol en llegar a la Tierra y respondes «499,004783836 s», parece muy preciso, pero tus datos (1 au y `c`) son exactos; en cambio, si respondes lo mismo para la distancia a la Luna, que varía entre unos 357 000 y 407 000 km, esas cifras serían falsas.

📘 **Dónde se aprende:** [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md); [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md); [B53-C05 · Sistemas de coordenadas lunares](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md); [B81-C12 · Restricciones dinámicas en optimización](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md) y 1 más.

### Cota de Cramér–Rao

*Aparece en 6 clases.*

- La matriz de información de Fisher es `F = Jᵀ J / σ²` (ruido gaussiano independiente); la cota de Cramér–Rao dice que la covarianza de cualquier estimador insesgado es al menos `F⁻¹`.
- La cota de Cramér–Rao es el límite de precisión.
- La cota de Cramér–Rao (CRB) dice que cualquier estimador sin sesgo cumple `Var(θ̂) ≥ 1/I(θ)`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C15](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md):**
- *Descripción textual:* los datos con ruido alimentan un estimador; de su sesgo y su varianza sale el error cuadrático medio; la varianza de un estimador sin sesgo se compara con la cota de Cramér–Rao.
- Calcular la información de Fisher y la cota de Cramér–Rao.
- 🎯 **Por qué importa:** Un telescopio recoge 100 fotones de una estrella y quieres su posición con la mayor exactitud posible. ¿Basta con promediar las posiciones?

📘 **Dónde se aprende:** [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md); [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md); [B46-C18 · VLBI y geodesia](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md); [B74-C03 · Medición de alcance por radio](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md); [B74-C27 · Navegación por púlsares de rayos X como técnica de investigación](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md).

### Covarianza

*Aparece en 13 clases.*

- La covarianza estimada de los parámetros es `σ̂² (JᵀJ)⁻¹`.
- La covarianza `Cov(X,Y) = E[(X − E[X])(Y − E[Y])] = E[XY] − E[X]E[Y]` mide la variación conjunta; su unidad es el producto de las unidades; el GUM la define y tabula su papel en la propagación (S1, C.3.4; 5.2.2).
- Su inversa es la covarianza (cota de Cramér–Rao).
- *(y 10 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C05](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md):**
- Con 1 000 000 de pares normales con `ρ = 0,8`, la correlación simulada es `0,8002` y la covarianza `9,609` (exacta `9,600`).
- La covarianza es la mitad «sin escala» de esa inclinación, y `r` la normaliza.
- ⚠️ **Error frecuente:** Sumar varianzas ignorando la covarianza. Se corrige con 8.3 y el ejercicio 2.
- 🎯 **Por qué importa:** En navegación espacial, la posición y la velocidad estimadas por un filtro no tienen errores independientes: un error de posición hacia delante suele ir acompañado de uno de velocidad. Ignorar esa relación da incertidumbres falsas, a veces demasiado optimistas y a veces demasiado pesimistas.

📘 **Dónde se aprende:** [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md); [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md); [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md); [B29-C04 · Astrometría de exoplanetas](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md); [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md) y 7 más.

### Criterio

*Aparece en 6 clases.*

- Un criterio es una propiedad que se compara (reserva, pendiente, iluminación, riesgo).
- El criterio es el nivel de desempeño exigido.
- Un criterio es un aspecto de comparación.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- Para un criterio donde más es mejor, `z = (x − mín)/(máx − mín)`; donde menos es mejor, `z = 1 − (x − mín)/(máx − mín)`.
- S7 (90 kt, 7°, 35 %, riesgo 5) está dominado por S4 (95 kt, 6°, 40 %, riesgo 4): S4 es mejor en los cuatro criterios.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?

📘 **Dónde se aprende:** [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md); [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md); [B104-C09 · Entrenamiento en simuladores](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md); [B124-C04 · Diseño de propuesta de valor](../programa/clases/B124/B124-C04-diseno-de-propuesta-de-valor/CLASE.md); [B128-C11 · Auditoría de accesibilidad de un recurso educativo](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md).

### Cruce

*Aparece en 6 clases.*

- Un cruce es el punto donde dos pasadas se intersecan.
- El cruce es la potencia a partir de la cual otra fuente pesa menos.
- El cruce es la `c` donde ambas valen lo mismo.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C17](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md):**
- REG --> CRU["cruce: |Δt| ≤ ventana y separación ≤ radio"]
- *Descripción textual:* cada registro se serializa de forma canónica y se firma con SHA-256; el validador revisa esquema, rangos, formato de tiempo, versión y huella; el cruce busca pares de mensajeros distintos.
- 🎯 **Por qué importa:** Un catálogo sin identificadores estables, versiones ni huellas no se puede citar ni auditar. La decisión central: ¿cómo se guarda un evento para que se pueda verificar, actualizar y cruzar con otros?

📘 **Dónde se aprende:** [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md); [B53-C07 · Topografía por altimetría](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md); [B86-C22 · Suministro de energía durante la noche lunar](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md); [B88-C32 · Redundancia fría y caliente: estrategias y conmutación](../programa/clases/B88/B88-C32-redundancia-fria-y-caliente-estrategias-y-conmutacion/CLASE.md); [B88-C33 · Votación y redundancia modular triple (TMR)](../programa/clases/B88/B88-C33-votacion-y-redundancia-modular-triple-tmr/CLASE.md); [B88-C44 · Mantenimiento predictivo y pronóstico de salud de sistemas](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md).

### Cuantización

*Aparece en 9 clases.*

- La cuantización es el redondeo del ADC, con varianza `1/12 ADU²`.
- La cuantización reemplaza el valor por el nivel más cercano.
- La cuantización con pérdida.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B44-C06](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md):**
- La cuantización importa solo si el ruido es menor que unos `1 ADU`.
- Ejercicio 2 · con una pista. Cuantización de un ADC.
- ⚠️ **Error frecuente:** Ignorar la cuantización con ruido pequeño. Se corrige con 8.2.
- 🎯 **Por qué importa:** Sin conocer el ruido de lectura no se puede planificar una exposición ni estimar una incertidumbre. La decisión central: ¿cómo medirlo sin que el patrón fijo del sensor lo contamine?

📘 **Dónde se aprende:** [B44-C06 · Ruido de lectura](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md); [B46-C09 · Conversión analógica digital](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md); [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md); [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md); [B57-C03 · Resolución radiométrica y espectral](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md); [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md) y 3 más.

### Cuello de botella

*Aparece en 7 clases.*

- Un cuello de botella es la parte que domina el tiempo.
- Un cuello de botella es la parte que fija el tiempo total.
- El cuello de botella es el eslabón de menor capacidad.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C14](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md):**
- Y si el cuello de botella es leer un archivo (C06–C07), vectorizar el cálculo no cambia nada.
- Optimizar es un ciclo de cuatro pasos y el orden importa: medir el tiempo actual, localizar el cuello de botella, cambiar solo eso y verificar que el resultado no cambió y que el tiempo bajó.
- 🎯 **Por qué importa:** Una función que calcula la distancia de 200 000 posiciones tarda medio minuto en tu cuaderno, y alguien propone «comprar un servidor». La pregunta motivadora es: ¿es el cálculo lento por su matemática o por cómo lo escribí, y cuánto puedo ganar sin cambiar el resultado?

📘 **Dónde se aprende:** [B14-C14 · Vectorización y rendimiento](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md); [B18-C04 · Perfilado de rendimiento](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md); [B89-C20 · Diseño de red de comunicaciones de misión](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md); [B97-C27 · Simulación de productividad de flotas de maquinaria](../programa/clases/B97/B97-C27-simulacion-de-productividad-de-flotas-de-maquinaria/CLASE.md); [B110-C03 · Evacuación y refugio de emergencia](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md); [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md) y 1 más.

### Declinación

*Aparece en 11 clases.*

- La declinación `δ` de un astro es su ángulo norte–sur en el cielo; la del Sol varía entre `−23,44°` y `+23,44°` a lo largo del año.
- La declinación de una estrella es su ángulo al norte o al sur del ecuador celeste (C08).
- La declinación `δ` es la coordenada celeste norte–sur.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C11](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md):**
- Por geometría (nuestra), las estrellas de declinación `|δ| > 90° − |φ| = 56,55°`, en el mismo hemisferio que el polo visible, son circumpolares: nunca se ponen.
- I["Eje inclinado 23,44°"] --> D["Declinación solar entre −23,44° y +23,44°"]
- 🎯 **Por qué importa:** Antes de cualquier telescopio, la humanidad dedujo mucho del cielo a simple vista. Que el Sol «salga» y «se ponga» es una observación; que la Tierra gire es una interpretación (C05) que explica además el movimiento de todas las estrellas.

📖 **Explicado a fondo:** [Ascensión recta y declinación](esencial/esencial-a-c.md#ascensión-recta-y-declinación).

📘 **Dónde se aprende:** [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B02-C07 · Observaciones de Polinesia y navegación oceánica](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md); [B02-C08 · Arqueoastronomía y sus métodos](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md); [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md); [B08-C02 · Esfera celeste y horizonte local](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md); [B08-C03 · Ascensión recta y declinación](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md) y 5 más.

### Degeneración

*Aparece en 9 clases.*

- La degeneración es la compensación entre parámetros (C22).
- La degeneración es la compensación entre parámetros que deja los datos casi iguales.
- La degeneración aparece cuando el principio de exclusión impide ocupar los estados bajos; se mide con `η = μ_químico/kT`.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C18](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md):**
- Las ideas generales —pesos de verosimilitud, remuestreo, degeneración, aptitud para modelos no lineales— son las descritas en S1.
- 🎯 **Por qué importa:** Un sensor mide la distancia oblicua a un objeto que pasa junto a él. Cuando el objeto está justo frente al sensor, un pequeño cambio de posición casi no cambia la distancia: la medida no distingue bien un lado del otro, y la incertidumbre de la posición deja de ser una campana.

📘 **Dónde se aprende:** [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md); [B26-C20 · Límites observacionales de modelos cosmológicos](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md); [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md); [B31-C05 · Espín y momento angular](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md); [B37-C02 · Ecuaciones de estado estelares: gas ideal, radiación y degeneración](../programa/clases/B37/B37-C02-ecuaciones-de-estado-estelares-gas-ideal-radiacion-y-degeneracion/CLASE.md); [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md) y 3 más.

### Densidad

*Aparece en 13 clases.*

- La densidad es masa por volumen.
- La densidad es masa dividida entre volumen, `ρ = M/V`.
- La densidad `ρ` es la masa por unidad de volumen.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C13](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md):**
- La ficha de planetas de NASA (actualizada el 18 de marzo de 2025) tabula masa, diámetro, densidad, período orbital, distancia al Sol, excentricidad y número de lunas para los ocho planetas y Plutón (S1).
- 🎯 **Por qué importa:** Se dice que el sistema solar «está vacío», y es verdad en un sentido preciso: si el Sol midiera 9 mm, la Tierra sería un grano de 0,085 mm a un metro de distancia, y la estrella más cercana quedaría a más de 260 km. Pero esa imagen solo se entiende si la construyes tú con números.

📖 **Explicado a fondo:** [Densidad](esencial/esencial-d-l.md#densidad).

📘 **Dónde se aprende:** [B01-C13 · Sistema solar como sistema físico](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md); [B03-C17 · Áreas y volúmenes elementales](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md); [B05-C14 · Gases y presión](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md); [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md); [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md); [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md) y 7 más.

### Deriva

*Aparece en 18 clases.*

- La deriva es la diferencia acumulada entre un calendario y el fenómeno que pretende seguir.
- Una deriva es la pérdida acumulada de ortogonalidad por redondeo.
- La deriva es su cambio numérico.
- *(y 15 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C01](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md):**
- El año juliano promedia 365,25 d (un día cada cuatro años); la deriva baja a `365,242 − 365,25 = −0,008 d` por año, es decir, un día de exceso cada 125 años.
- El calendario gregoriano usa 97 años bisiestos cada 400, con promedio `(97 × 366 + 303 × 365)/400 = 365,2425 d`, y su deriva baja a `−0,0005 d` por año, un día cada 2 000 años aproximadamente.
- ⚠️ **Error frecuente:** Creer que la deriva es un defecto. Puede ser una estrategia (sección 8.3).
- 🎯 **Por qué importa:** Un calendario es una promesa: «dentro de tantos días ocurrirá tal cosa en el cielo o en la tierra». Esa promesa solo se cumple si el calendario sigue algún ciclo natural.

📘 **Dónde se aprende:** [B02-C01 · Calendarios astronómicos en civilizaciones antiguas](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md); [B10-C13 · Matrices de rotación tridimensional](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md); [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md); [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md); [B13-C23 · Estabilidad y deriva temporal de instrumentos](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md); [B43-C12 · Montura ecuatorial](../programa/clases/B43/B43-C12-montura-ecuatorial/CLASE.md) y 12 más.

### Desfase

*Aparece en 6 clases.*

- El desfase es el retraso entre modelo y observación.
- El desfase `x(t)` es la diferencia de tiempo entre el reloj y la referencia.
- El desfase `τ` hace ortogonales los términos coseno y seno.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B29-C19](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md):**
- Calcular la potencia de Lomb–Scargle con el desfase `τ`.
- Ejercicio 10 · transferencia. ¿Por qué el desfase `τ`?
- 🎯 **Por qué importa:** Un periodograma sin cuidado señala alias en lugar del periodo verdadero, y una potencia alta puede ser una fluctuación del ruido. La decisión central: ¿qué picos son del periodo verdadero, cuáles son alias y qué potencia es significativa?

📘 **Dónde se aprende:** [B29-C19 · Análisis de series temporales irregularmente muestreadas](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md); [B33-C01 · Validación de modelos MHD con eventos solares documentados](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md); [B43-C16 · Encoders y medición angular](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md); [B48-C10 · Redes de instrumentos](../programa/clases/B48/B48-C10-redes-de-instrumentos/CLASE.md); [B57-C32 · Sitios de calibración terrestres](../programa/clases/B57/B57-C32-sitios-de-calibracion-terrestres/CLASE.md); [B74-C16 · Sincronización temporal](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md).

### Desplazamiento

*Aparece en 6 clases.*

- El desplazamiento `Δr = r₂ − r₁` es el cambio de posición, y la distancia recorrida es la longitud del camino, que puede ser mayor.
- Un desplazamiento `(dy, dx)` es una traslación; una transformación rígida añade rotación; una afín añade escala y cizalla.
- El desplazamiento es la separación entre el centroide de la masa y el del gas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C02](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md):**
- Distinguir desplazamiento de distancia recorrida y rapidez de velocidad.
- ¿Distancia recorrida y módulo del desplazamiento?
- ⚠️ **Error frecuente:** Mezclar distancia y desplazamiento. Ejercicio 4.
- 🎯 **Por qué importa:** Cuando una agencia dice que un satélite «va a 7,7 km/s», ¿respecto de qué y en qué dirección? La pregunta motivadora es: ¿cómo describo un movimiento de forma que otra persona lo reconstruya sin ambigüedad?

📘 **Dónde se aprende:** [B05-C02 · Posición, velocidad y aceleración](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md); [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md); [B28-C05 · Ondas gravitacionales](../programa/clases/B28/B28-C05-ondas-gravitacionales/CLASE.md); [B34-C07 · Comparación de modelos coronales con observaciones](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md); [B36-C09 · Cúmulos en colisión como prueba de materia oscura](../programa/clases/B36/B36-C09-cumulos-en-colision-como-prueba-de-materia-oscura/CLASE.md); [B39-C06 · Introducción a la relatividad numérica: formalismo 3+1](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md).

### Detección

*Aparece en 8 clases.*

- Una detección es un máximo local de la imagen filtrada sobre el umbral.
- La tasa de falsa alarma es la probabilidad de marcar un píxel sin cambio; la de detección, la de marcar uno con cambio.
- La detección es que el error se advierta; la corrección, que se acepte y se repare.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C20](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md):**
- (R3) a lo sumo una detección falsa en toda la secuencia;
- (R4) RMSE de la pista menor que el de las detecciones sin filtrar;
- 🎯 **Por qué importa:** Detectar y seguir un objeto móvil —un asteroide, un fragmento de basura espacial, un satélite— combina varios problemas: la cámara no apunta exactamente igual en cada imagen, las estrellas fijas saturan la escena, el objeto es débil y la medida es ruidosa.

📘 **Dónde se aprende:** [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md); [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md); [B57-C27 · Detección de cambios en series de imágenes](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md); [B88-C40 · Auditoría de software espacial](../programa/clases/B88/B88-C40-auditoria-de-software-espacial/CLASE.md); [B96-C25 · Seguridad física y control de acceso de estaciones terrestres](../programa/clases/B96/B96-C25-seguridad-fisica-y-control-de-acceso-de-estaciones-terrestres/CLASE.md); [B104-C07 · Factores de liderazgo](../programa/clases/B104/B104-C07-factores-de-liderazgo/CLASE.md) y 2 más.

### Disponibilidad

*Aparece en 11 clases.*

- La disponibilidad es la probabilidad de que el sitio funcione.
- La disponibilidad es `MTBF/(MTBF + MTTR)`.
- (Es la convención de este curso, didáctica.) La disponibilidad a una demanda `D` es `P(M ≥ D)`.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C16](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md):**
- Descripción larga: la disponibilidad reduce la cobertura en un cuarto; la distribución en longitud hace casi válida la independencia.
- Incorporar la disponibilidad de cada sitio.
- ⚠️ **Error frecuente:** Ignorar la disponibilidad. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** La cobertura de una red depende de su distribución geográfica, no solo del número de telescopios. La decisión central: ¿qué probabilidad hay de que, al llegar una alerta, al menos un sitio de la red pueda observar la fuente?

📘 **Dónde se aprende:** [B28-C16 · Redes internacionales de alertas](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md); [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B59-C18 · Fiabilidad de equipos mineros](../programa/clases/B59/B59-C18-fiabilidad-de-equipos-mineros/CLASE.md); [B67-C08 · Informe de disponibilidad de volátiles con incertidumbre](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md); [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md) y 5 más.

### Eclipse

*Aparece en 6 clases.*

- Un eclipse es el alineamiento en que un cuerpo proyecta su sombra sobre otro.
- El eclipse es el tiempo en sombra; su fracción en sombra cilíndrica es `asin(R/a)/π`.
- El eclipse es el tramo de la órbita en que la Tierra tapa al Sol.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- No es la sombra de la Tierra: esa sombra solo cae sobre la Luna en un eclipse lunar, que es raro, y las fases ocurren todos los meses.
- Solo cuando la luna nueva o llena ocurre cerca de donde los dos planos se cruzan hay eclipse.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📖 **Explicado a fondo:** [Eclipse](esencial/ampliacion-a-m.md#eclipse).

📘 **Dónde se aprende:** [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B02-C02 · Observación mesopotámica y egipcia](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md); [B47-C02 · Requisitos de instrumentos orbitales](../programa/clases/B47/B47-C02-requisitos-de-instrumentos-orbitales/CLASE.md); [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md); [B83-C10 · Presupuestos de energía](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md); [B96-C11 · Operación durante eclipse](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md).

### Ecuación vis-viva

*Aparece en 6 clases.*

- La ecuación vis-viva `v² = GM (2/r − 1/a)` da la rapidez en cualquier punto (se deduce con la conservación de la energía, C07).
- La ecuación vis‑viva `v² = μ(2/r − 1/a)` liga velocidad y distancia.
- La ecuación vis-viva relaciona velocidad, radio y semieje.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B71-C05](../programa/clases/B71/B71-C05-energia-orbital-especifica/CLASE.md):**
- *Descripción textual:* de la energía salen el semieje, la ecuación vis‑viva y las velocidades extremas; que la energía sea constante es la prueba de la integración.
- Aplicar la ecuación vis‑viva `v² = μ(2/r − 1/a)`.
- 🎯 **Por qué importa:** El semieje fija el período y la energía; cambiar de órbita es cambiar de energía. La decisión central: ¿cuánta energía por kilogramo tiene una órbita y qué velocidad corresponde a cada distancia?

📘 **Dónde se aprende:** [B05-C20 · Problema físico integrado de satélite ideal](../programa/clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md); [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md); [B47-C23 · Sondas heliosféricas: Parker Solar Probe y Voyager](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md); [B71-C05 · Energía orbital específica](../programa/clases/B71/B71-C05-energia-orbital-especifica/CLASE.md); [B75-C01 · Geometría de transferencias heliocéntricas](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md); [B77-C12 · Perfil de ascenso orbital](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md).

### Eficiencia

*Aparece en 12 clases.*

- La eficiencia es `E = S/p`.
- La eficiencia es `E = S/N`.
- La eficiencia es obturador/(obturador + sobrecarga).
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Aceleración: `S(2) = 1,16` y `S(4) = 0,99`, con eficiencias de 0,58 y 0,25.
- Calcular aceleración y eficiencia a partir de tiempos medidos.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.

📘 **Dónde se aprende:** [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md); [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md); [B27-C10 · Discos de acreción](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md); [B38-C07 · Modelos submalla de formación estelar y retroalimentación](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B56-C02 · Bioquímica y metabolismo terrestre](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md) y 6 más.

### Emisividad

*Aparece en 7 clases.*

- La emisividad `ε` es la razón entre lo que emite un cuerpo y lo que emitiría un cuerpo negro.
- La emisividad es la fracción de lo que emitiría un cuerpo negro.
- La emisividad `ε` es el cociente con el cuerpo negro.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C17](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md):**
- Su límite: un cuerpo negro real tiene emisividad algo menor que 1 y un campo no uniforme; ambos son una fuente de incertidumbre (C13).
- Paso 4 · Efecto de la emisividad. Si el cuerpo negro real tiene `ε = 0,95` y se supone 1, las radiancias reales son `5 %` menores que las asumidas: la ganancia estimada sale `5 %` mayor (`≈ 0,84`).
- 🎯 **Por qué importa:** Una cámara infrarroja de una nave mide el calor emitido por la superficie de un planeta. Sus cuentas no significan nada hasta saberse cuánta radiancia corresponde a cada una.

📘 **Dónde se aprende:** [B13-C17 · Calibración radiométrica](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md); [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md); [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md); [B47-C23 · Sondas heliosféricas: Parker Solar Probe y Voyager](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md); [B57-C01 · Fundamentos de teledetección](../programa/clases/B57/B57-C01-fundamentos-de-teledeteccion/CLASE.md); [B85-C04 · Radiación térmica de superficies](../programa/clases/B85/B85-C04-radiacion-termica-de-superficies/CLASE.md) y 1 más.

### Empuje

*Aparece en 7 clases.*

- El empuje es la fuerza de un motor o un fluido.
- El empuje es `E = ṁ v_e`, con `ṁ` el flujo de masa expulsada.
- El empuje `F` es la fuerza que el motor ejerce sobre la nave.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- Un cohete de masa `m` en una plataforma, con empuje vertical `E` y peso `m g_n`, tiene `a = (E − m g_n)/m`.
- En el espacio, el satélite ideal bajo gravedad y un empuje tangencial pequeño tiene `ΣF` con dos componentes: una radial (gravedad) y otra tangencial (empuje).
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?

📘 **Dónde se aprende:** [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md); [B05-C08 · Momento lineal e impulsos](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md); [B78-C01 · Empuje e impulso específico](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md); [B79-C08 · Flujo en toberas convergente-divergentes](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md); [B81-C05 · Limitaciones de potencia en propulsión eléctrica](../programa/clases/B81/B81-C05-limitaciones-de-potencia-en-propulsion-electrica/CLASE.md); [B97-C06 · Control de movilidad sobre regolito](../programa/clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md) y 1 más.

### Energía específica

*Aparece en 8 clases.*

- La energía específica es energía por unidad de masa (J/kg).
- La energía específica es energía por unidad de masa (J/kg), útil porque no depende de `m`.
- La energía específica (por unidad de masa) es `E = v²/2 − GM/r` y el momento angular específico, `L = x·vy − y·vx`; ambos se conservan en un campo central.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C09](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md):**
- La energía específica de un cuerpo que se mueve a rapidez `v` a distancia `r` del centro es `e = v²/2 − GM/r`.
- El script [laboratorio_signos.py](laboratorio_signos.py) calcula la energía específica de la Luna de las dos maneras de la sección 8.7, la corrección por tiempo de luz y el formato T−/T+.
- 🎯 **Por qué importa:** Cuando observas una llamarada solar a las 12:00:00, el evento ocurrió antes: su tiempo es el observado menos 499 s. Si sumas en vez de restar, afirmas que la llamarada ocurre en el futuro.

📘 **Dónde se aprende:** [B03-C09 · Operaciones con números negativos](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md); [B05-C07 · Conservación de energía mecánica](../programa/clases/B05/B05-C07-conservacion-de-energia-mecanica/CLASE.md); [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md); [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md); [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md) y 2 más.

### Error

*Aparece en 6 clases.*

- El error de una medición es la diferencia entre el valor medido y el verdadero (desconocido).
- El error es la diferencia entre el resultado simulado y el exacto.
- Si `f` tiene derivada continua de orden `n + 1`, el error es `f(x) − P_n(x) = f^{(n+1)}(ξ) ω(x)/(n + 1)!` para algún `ξ` en el intervalo (S1, ec. 3.3.5).
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- Repetir lecturas reduce el error aleatorio, no el sistemático (S1).
- Imagina disparar a una diana: un grupo de impactos muy juntos pero lejos del centro es preciso con error sistemático; impactos dispersos alrededor del centro es exacto con error aleatorio.
- ⚠️ **Error frecuente:** Creer que más lecturas eliminan todo error. Ejercicio 8.
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.

📘 **Dónde se aprende:** [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B07-C05 · Bucles y simulaciones sencillas](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md); [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md); [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md); [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md); [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md).

### Error relativo

*Aparece en 7 clases.*

- El error relativo es `(aproximado − exacto)/exacto`.
- El error relativo es `σ_h/h`.
- El error relativo es `|aprox − exacto|/|exacto|`.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C03](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md):**
- Para evaluar un cálculo frente a una referencia: `error relativo = |calculado − referencia| / referencia`.
- Calcular un error relativo porcentual frente a un valor de referencia.
- 🎯 **Por qué importa:** La Tierra no gira en un círculo: su distancia al Sol varía a lo largo del año. ¿Mucho o poco?

📘 **Dónde se aprende:** [B03-C03 · Porcentajes y escalas comparativas](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B04-C06 · Identidades trigonométricas](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md); [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md); [B09-C14 · Series y aproximaciones](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md); [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md) y 1 más.

### Escala

*Aparece en 7 clases.*

- Una escala de un eje indica cuánto vale cada marca; en una escala logarítmica cada marca multiplica por un factor fijo (B01-C02).
- Una escala es una clasificación por umbrales.
- El sesgo `o` es un desplazamiento y la escala `s` un factor por eje.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Antes de interpretar, lee: ¿qué magnitud hay en cada eje, con qué unidad, con qué escala (lineal o logarítmica), y desde dónde empieza el eje?
- En escala log-log, una función de potencia aparece como una recta cuya pendiente es el exponente; entre Venus y Júpiter esa pendiente da 1,499, muy cerca de 1,5 (sección 17).
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.

📘 **Dónde se aprende:** [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B24-C20 · Modelo simplificado de estructura estelar](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md); [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B33-C04 · Escalas de severidad de clima espacial](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md); [B53-C26 · Publicación de mapas geológicos planetarios: estándares y leyendas](../programa/clases/B53/B53-C26-publicacion-de-mapas-geologicos-planetarios-estandares-y-leyendas/CLASE.md); [B80-C06 · Fusión IMU-cámara](../programa/clases/B80/B80-C06-fusion-imu-camara/CLASE.md) y 1 más.

### Espectro

*Aparece en 9 clases.*

- El espectro es la luz descompuesta por longitud de onda.
- Un espectro es la distribución de la luz por longitud de onda.
- El espectro es el conjunto de autovalores.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- Observa que el patrón (la distancia relativa entre líneas) se conserva aunque todo el espectro se corra.
- Si todas dan el mismo `z` dentro del error, el corrimiento es de todo el espectro, no un error de identificación.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📖 **Explicado a fondo:** [Espectro y espectroscopía](esencial/esencial-d-l.md#espectro-y-espectroscopía).

📘 **Dónde se aprende:** [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md); [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md); [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B35-C09 · Turbulencia en plasmas y MHD](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md); [B36-C02 · Función de transferencia y espectro de materia](../programa/clases/B36/B36-C02-funcion-de-transferencia-y-espectro-de-materia/CLASE.md) y 3 más.

### Estabilidad

*Aparece en 8 clases.*

- La masa formular es la masa molar de la fórmula; la estabilidad de un hielo, en esta clase, es el intervalo de presiones y temperaturas donde no sublima (C11).
- La estabilidad (no explotar) es distinta de la precisión (parecerse a la solución).
- La consistencia es que el error de truncamiento tienda a cero; la estabilidad, que los errores no crezcan.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Sólo toma dos cifras (la temperatura de 176 K y la clasificación de las especies) para ejercitar el cálculo de energías y de estabilidad.
- Ejercicio 6. Calcula la presión mínima de estabilidad del hielo de CO₂ a 170 K con `ΔH_sub = 26,1 kJ/mol`.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).

📘 **Dónde se aprende:** [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md); [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md); [B13-C23 · Estabilidad y deriva temporal de instrumentos](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md); [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md); [B84-C24 · Factores de seguridad y márgenes estructurales](../programa/clases/B84/B84-C24-factores-de-seguridad-y-margenes-estructurales/CLASE.md) y 2 más.

### Estable

*Aparece en 6 clases.*

- Un ordenamiento es estable si los elementos con la misma clave conservan su orden relativo (S2).
- El método es estable para un `z` si `|R(z)| ≤ 1`; la región de estabilidad es el conjunto de `z` donde ocurre.
- Un LTI es estable (en el sentido que usaremos) si su respuesta al impulso tiende a cero.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- Es estable si, en un empate, se toma primero el elemento de la mitad izquierda (como hace el laboratorio).
- Explicar el significado de «estable» y verificarlo.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.

📘 **Dónde se aprende:** [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md); [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B54-C19 · Modelos climáticos planetarios](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md); [B73-C06 · Variedades invariantes](../programa/clases/B73/B73-C06-variedades-invariantes/CLASE.md); [B77-C21 · Centro de presión y margen estático](../programa/clases/B77/B77-C21-centro-de-presion-y-margen-estatico/CLASE.md).

### Estado

*Aparece en 6 clases.*

- El estado es el conjunto de esos valores.
- El estado `x` es el menor conjunto de variables que, junto con la entrada futura, determina todo el futuro del sistema.
- El estado es el par posición–velocidad en un instante.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C02](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md):**
- A["EDO de orden m"] --> B["Estado inicial:<br/>y y sus m−1 derivadas<br/>en t₀"]
- *Descripción textual:* para una EDO de orden `m` se fija el estado inicial; si la función `f` es lipschitziana la solución es única; luego se pregunta cuánto crece una diferencia inicial, lo que limita el horizonte útil de predicción.
- 🎯 **Por qué importa:** Una nave no sigue «la» solución de las ecuaciones del movimiento: sigue la que corresponde a *su* posición y velocidad en el instante en que se midieron. Saber cuántos datos exige la ecuación, cuándo garantizan una única trayectoria y cuánto se amplifica su error es la base de toda predicción de trayectoria.

📘 **Dónde se aprende:** [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md); [B71-C10 · Semieje mayor y excentricidad](../programa/clases/B71/B71-C10-semieje-mayor-y-excentricidad/CLASE.md); [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md); [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md).

### Estimador

*Aparece en 7 clases.*

- Un estimador del valor esperado a partir de `n` observaciones independientes en las mismas condiciones es la media aritmética (S1, 4.2.1); la desviación típica experimental estima `σ` con denominador `n − 1` (S1, 4.2.2).
- Una estadística es una función de los datos de la muestra; una estimación es la operación de asignar valores numéricos a los parámetros a partir de una muestra, un estimador es la estadística usada para ello y una estimación (resultado) es su valor para una muestra concreta (S1, C.2.23–C.2.26).
- Un estimador `θ̂(datos)` es una función de los datos.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C07](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md):**
- La cota de Cramér–Rao —que fija la menor varianza posible de un estimador insesgado— coincide con `λ/n` para este modelo: la media es el mejor estimador insesgado posible.
- Esa es la forma de comprobar un estimador: simular muchas muestras de un modelo conocido y ver si el estimador acierta en promedio y con la dispersión esperada.
- ⚠️ **Error frecuente:** Creer que un estimador insesgado siempre es mejor. Se corrige con 8.6 y el ejercicio 11.
- 🎯 **Por qué importa:** Una misión no «conoce» la tasa de impactos ni el ruido de su sensor: los estima a partir de unas decenas de datos. Un estimador mal elegido, o mal interpretado, da parámetros sesgados o con una confianza injustificada.

📘 **Dónde se aprende:** [B12-C04 · Esperanza y varianza](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md); [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md); [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md); [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md); [B36-C04 · Espectro de potencia de materia](../programa/clases/B36/B36-C04-espectro-de-potencia-de-materia/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md) y 1 más.

### Evento

*Aparece en 6 clases.*

- Un evento es un subconjunto de `Ω`: «ocurre» si el resultado pertenece a él.
- Un evento es algo que ocurre en un lugar y un instante.
- El evento es la curva completa.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C01](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md):**
- Para dos eventos cualquiera, `P(A∪B) = P(A) + P(B) − P(A∩B)`: al sumar `P(A)` y `P(B)` se cuenta dos veces la intersección.
- Un evento es una etiqueta que pones a un grupo de historias; su probabilidad es la suma de los pesos de ese grupo.
- ⚠️ **Error frecuente:** Confundir excluyentes con independientes. Se corrige con los ejercicios 7 y 8: eventos excluyentes con probabilidad positiva son dependientes.
- 🎯 **Por qué importa:** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.

📘 **Dónde se aprende:** [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md); [B26-C01 · Postulados de relatividad especial](../programa/clases/B26/B26-C01-postulados-de-relatividad-especial/CLASE.md); [B29-C05 · Microlentes gravitacionales](../programa/clases/B29/B29-C05-microlentes-gravitacionales/CLASE.md); [B77-C20 · Simulación académica de una trayectoria de vuelo](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md); [B96-C20 · Simulación de jornada de control de misión](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md); [B106-C10 · Gestión de residuos humanos](../programa/clases/B106/B106-C10-gestion-de-residuos-humanos/CLASE.md).

### Excentricidad

*Aparece en 9 clases.*

- La excentricidad `e` mide cuánto se aparta la órbita de un círculo (0 es círculo).
- La excentricidad `e` mide su achatamiento: la distancia entre focos es `2ae`.
- La excentricidad `e = c/a` mide cuánto se aleja la elipse de una circunferencia: `e = 0` es una circunferencia y `e` cercano a 1 es una elipse muy alargada.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C13](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md):**
- La ficha de planetas de NASA (actualizada el 18 de marzo de 2025) tabula masa, diámetro, densidad, período orbital, distancia al Sol, excentricidad y número de lunas para los ocho planetas y Plutón (S1).
- 🎯 **Por qué importa:** Se dice que el sistema solar «está vacío», y es verdad en un sentido preciso: si el Sol midiera 9 mm, la Tierra sería un grano de 0,085 mm a un metro de distancia, y la estrella más cercana quedaría a más de 260 km. Pero esa imagen solo se entiende si la construyes tú con números.

📖 **Explicado a fondo:** [Excentricidad](esencial/esencial-d-l.md#excentricidad).

📘 **Dónde se aprende:** [B01-C13 · Sistema solar como sistema físico](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md); [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B26-C08 · Geodésicas gravitacionales](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md) y 3 más.

### Extinción

*Aparece en 6 clases.*

- La extinción es la pérdida de luz por absorción y dispersión en el camino; si es exponencial, `I = I₀ e^(−τ)` con `τ` la profundidad óptica.
- La extinción `A` (en magnitudes) mide la pérdida de luz: `A = −2,5 log₁₀(F/F₀)`;
- La extinción `A_V` mide el polvo atravesado.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- Extinción: I/I0 = 0.7788; pérdida = 0.2714 mag (= 1,0857 tau = 0.2714)
- Límites: magnitud bolométrica, sin extinción interestelar ni correcciones bolométricas por banda; las estrellas son sintéticas; no es una herramienta de fotometría.
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.

📘 **Dónde se aprende:** [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md); [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B48-C05 · Ventanas atmosféricas](../programa/clases/B48/B48-C05-ventanas-atmosfericas/CLASE.md); [B55-C08 · Fotoquímica cósmica](../programa/clases/B55/B55-C08-fotoquimica-cosmica/CLASE.md).

### Falsa alarma

*Aparece en 11 clases.*

- Una falsa alarma es una detección que no corresponde a ninguna fuente; su tasa es la fracción de píxeles (o el número por imagen) que superan el umbral solo por ruido.
- Una falsa alarma es un punto normal señalado como anómalo.
- Un falso «seguro» es un peligro declarado transitable; una falsa alarma es una celda segura declarada peligrosa.
- *(y 8 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- Paso 6 · Falsas alarmas del umbral. `Q(4) = 3,17 × 10⁻⁵` por píxel: 1,3 por imagen de 40 000 píxeles.
- Predecir la tasa de falsas alarmas y la completitud para un umbral dado.
- ⚠️ **Error frecuente:** Reportar el catálogo sin completitud ni falsas alarmas. Se corrige con el ejercicio 12.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.

📘 **Dónde se aprende:** [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md); [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B48-C23 · Observabilidad del software de observatorio: registros, métricas y alertas](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md); [B88-C12 · Detección aislamiento y recuperación de fallos](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md); [B89-C24 · Recepción de telemetría débil](../programa/clases/B89/B89-C24-recepcion-de-telemetria-debil/CLASE.md) y 5 más.

### Falso positivo

*Aparece en 8 clases.*

- Un falso positivo es una alarma sin error real; un falso negativo, un error que pasa inadvertido.
- Un falso positivo es declarar un efecto que no existe.
- Un falso positivo es un píxel marcado que no es objeto.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C10](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md):**
- Muy bajo, suena con el redondeo (falsos positivos).
- 🎯 **Por qué importa:** Cambias una línea de un propagador orbital «solo para ordenarlo» y el período de una órbita pasa de 5553,624562 s a 5553,627342 s (situación ilustrativa con cifras de esta clase). ¿Es un error o ruido?

📘 **Dónde se aprende:** [B14-C10 · Pruebas de regresión numérica](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md); [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md); [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md); [B29-C08 · Falsos positivos de tránsito](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md); [B56-C13 · Biofirmas químicas](../programa/clases/B56/B56-C13-biofirmas-quimicas/CLASE.md) y 2 más.

### Fase

*Aparece en 17 clases.*

- La fase es la parte del disco lunar iluminada que vemos.
- La fase es la fracción del disco lunar que ves iluminada; se da como porcentaje de 0 % (nueva) a 100 % (llena).
- Una fase es un estado del gas con un rango de temperatura y densidad.
- *(y 13 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- No es la sombra de la Tierra: esa sombra solo cae sobre la Luna en un eclipse lunar, que es raro, y las fases ocurren todos los meses.
- Paso 6 · Comprobación. Observa la fase cada noche cerca de la fecha; anota la noche en que el disco se ve completo; compara con la predicción y con una tabla publicada que cites.
- ⚠️ **Error frecuente:** Atribuir las fases a la sombra de la Tierra. Ejercicio 8.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende:** [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md); [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md); [B29-C06 · Imagen directa de exoplanetas](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md); [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md) y 11 más.

### Fiabilidad

*Aparece en 7 clases.*

- La fiabilidad `R(t)` es la probabilidad de funcionar hasta `t`.
- La fiabilidad `r` es la proporción de la varianza que es real.
- La fiabilidad `r` es la probabilidad de que una fuente informe correctamente.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C05](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md):**
- *Descripción textual:* el cociente costo/pérdida fija el umbral de decisión, que da el gasto; el Brier y la fiabilidad miden la calidad de las probabilidades.
- Ejercicio 12. Integrador. Elabora tu *ficha del riesgo y las alertas*: umbral, gasto, Brier y fiabilidad.
- 🎯 **Por qué importa:** La mejor comunicación de riesgo da probabilidades calibradas y deja decidir al usuario. La decisión central: ¿cuándo conviene proteger y cuán fiables son las probabilidades?

📖 **Explicado a fondo:** [Redundancia y fiabilidad](esencial/ampliacion-n-z.md#redundancia-y-fiabilidad).

📘 **Dónde se aprende:** [B33-C05 · Comunicación de riesgo y alertas de clima espacial](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md); [B59-C18 · Fiabilidad de equipos mineros](../programa/clases/B59/B59-C18-fiabilidad-de-equipos-mineros/CLASE.md); [B88-C01 · Arquitectura de computador de vuelo](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md); [B106-C18 · Fiabilidad y redundancia](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md); [B107-C04 · Evaluación del rendimiento físico y cognitivo de tripulantes](../programa/clases/B107/B107-C04-evaluacion-del-rendimiento-fisico-y-cognitivo-de-tripulantes/CLASE.md); [B118-C11 · Diseño para mitigación de desechos](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md) y 1 más.

### Fluencia

*Aparece en 6 clases.*

- La fluencia es el número de neutrinos por unidad de área.
- La fluencia es el flujo integrado en el tiempo.
- La fluencia `Φ` es el número de fotones acumulados por cm².
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B27-C18](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md):**
- A `d = 10 kpc = 3,0857 × 10²⁰ m`, la fluencia es `2,1735 × 10¹⁵ m⁻² = 2,1735 × 10¹¹ cm⁻²`.
- *Descripción textual:* de la energía y la energía media se obtiene el número de neutrinos y su fluencia; con la sección eficaz y los protones del detector, los sucesos; el retraso por masa se calcula con una forma algebraica estable.
- 🎯 **Por qué importa:** Los neutrinos de una supernova galáctica serían una señal de cientos de sucesos en unos segundos, mensajera del interior de la estrella. La decisión central: ¿cuántos neutrinos llegan, qué retraso produce su masa y cómo se calcula sin perder precisión?

📘 **Dónde se aprende:** [B27-C18 · Neutrinos de supernova](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md); [B30-C12 · Erupciones y fulguraciones solares](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md); [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md); [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md); [B85-C13 · Efectos de oxígeno atómico](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md); [B112-C01 · Magnitudes dosimétricas: dosis absorbida, LET y eficacia biológica](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md).

### Flujo

*Aparece en 13 clases.*

- El flujo es la energía de luz recibida por unidad de área y tiempo; el brillo aparente es lo que percibimos de él.
- El flujo `F` es la energía recibida por unidad de área y tiempo (W/m²) y cae con el cuadrado de la distancia.
- El flujo `F` es la energía luminosa que llega por unidad de área y tiempo.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- El brillo da el flujo recibido, pero un objeto débil puede estar lejos o ser intrínsecamente poco luminoso: brillo y distancia están mezclados.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📖 **Explicado a fondo:** [Flujo y luminosidad](esencial/esencial-d-l.md#flujo-y-luminosidad).

📘 **Dónde se aprende:** [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B08-C11 · Magnitudes aparentes y brillo](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md); [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md); [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md); [B28-C05 · Ondas gravitacionales](../programa/clases/B28/B28-C05-ondas-gravitacionales/CLASE.md) y 7 más.

### Fondo

*Aparece en 6 clases.*

- El fondo (*background*) es el nivel del cielo sin fuentes; el ruido `σ` su desviación.
- Los conteos oscuros y el fondo son eventos sin señal.
- Un fotón de señal viene del láser reflejado; uno de fondo viene del Sol o del ruido del detector.

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- En el laboratorio, 100 fuentes brillantes de flujo 1000 ADU elevan la media del fondo a 102,50 ADU (real 100,0) y la desviación global a 10,34 (real 5,0).
- Ninguno es perfecto: las alas débiles de las fuentes siguen contaminando, por lo que en la práctica se enmascaran las fuentes y se repite (S1 usa un recorte a 3σ para el fondo).
- ⚠️ **Error frecuente:** Estimar el fondo con la media en un campo con fuentes. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.

📘 **Dónde se aprende:** [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md); [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md); [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md); [B57-C11 · LiDAR satelital](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md); [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Frecuencia natural

*Aparece en 7 clases.*

- La frecuencia natural `ω₀ = √(k/m)` es la del sistema libre.
- La frecuencia natural es `ω_n² = −Cm_α q S d/I_y`.
- La frecuencia natural de lazo cerrado es `ω_n² = μ_c Kp − μ_α`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- Planteamiento. Hallar la frecuencia natural del mástil, su energía a 10 mm de amplitud y el efecto de una excitación a esa frecuencia.
- Aquí lo calcularás en dos pasos y verás qué pasa si la excitación coincide con la frecuencia natural.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende:** [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B58-C19 · Comunicación pública del riesgo](../programa/clases/B58/B58-C19-comunicacion-publica-del-riesgo/CLASE.md); [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md); [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md) y 1 más.

### Fuga

*Aparece en 6 clases.*

- La fuga E→B es la potencia de B espuria que produce una máscara.
- Una fuga es transmisión residual fuera de banda.
- La fuga es la señal que pasa al puerto de salida sin mezclar.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B40-C08](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md):**
- Las dos máscaras no tienen la misma área, así que la comparación indica la dirección (apodizar reduce la fuga) y no una ley cuantitativa.
- Descripción larga: apodizar reduce la fuga a la mitad aproximadamente.
- ⚠️ **Error frecuente:** Medir B en un mapa enmascarado sin corregir la fuga. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un modo B primordial sería una huella de ondas gravitacionales, pero las máscaras filtran E hacia B. La decisión central: ¿cómo se separan E y B y cuánto contamina una máscara?

📘 **Dónde se aprende:** [B40-C08 · Polarización E y B del fondo cósmico](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md); [B45-C03 · Curvas de transmisión](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md); [B49-C11 · Mezcladores de frecuencia: pérdida de conversión y productos espurios](../programa/clases/B49/B49-C11-mezcladores-de-frecuencia-perdida-de-conversion-y-productos-espurios/CLASE.md); [B104-C05 · Sistemas de vehículos tripulados](../programa/clases/B104/B104-C05-sistemas-de-vehiculos-tripulados/CLASE.md); [B117-C04 · Problemas respiratorios simulados](../programa/clases/B117/B117-C04-problemas-respiratorios-simulados/CLASE.md); [B118-C10 · Síndrome de Kessler como escenario](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md).

### FWHM

*Aparece en 7 clases.*

- El FWHM es la anchura a media altura.
- La FWHM es el ancho a media altura.
- Una PSF gaussiana de desviación `σ` tiene FWHM `= 2√(2 ln 2) σ = 2,355 σ`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- Con PSF gaussiana: `FWHM = 2,355 σ` y pico normalizado `1/(2πσ²)`.
- Para `σ = 1`: FWHM 2,35 y pico 0,1592; para `σ = 1,5`: 3,53 y 0,0707; para `σ = 2`: 4,71 y 0,0398.
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.

📘 **Dónde se aprende:** [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md); [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md); [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md) y 1 más.

### Ganancia

*Aparece en 16 clases.*

- La ganancia es cuántas magnitudes más débil se llega con un instrumento.
- La ganancia es cuántos electrones corresponden a un ADU; aquí se supone 1 e⁻/ADU.
- La ganancia es `G = η e^{−(4πσ/λ)²} (πD/λ)²`.
- *(y 12 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C11](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md):**
- Un instrumento de apertura `D` recoge más luz que la pupila del ojo (`d ≈ 7 mm` totalmente dilatada, supuesto de esta clase, no una cifra de fuente): el cociente de flujos es `(D/d)²`, y la ganancia en magnitudes es `Δm = 2,5 log₁₀((D/d)²) = 5 log₁₀(D/d)`.
- La ganancia teórica supone cielo perfectamente oscuro, instrumento sin pérdidas de luz, pupila de salida menor que la del ojo, ojo adaptado y fuente puntual.
- ⚠️ **Error frecuente:** Creer que la ganancia teórica es la real. Ejercicio 9.
- 🎯 **Por qué importa:** Un informe dice «cometa de magnitud 6» y otro «galaxia de magnitud 9». Sin entender la escala, no sabrás si los verás a simple vista, con binoculares o solo con telescopio.

📘 **Dónde se aprende:** [B08-C11 · Magnitudes aparentes y brillo](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md); [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md); [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B15-C24 · Fusión de imágenes de distintos sensores](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md); [B42-C14 · Sensores Shack-Hartmann](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md); [B42-C20 · Laboratorio de corrección óptica simulada](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md) y 10 más.

### Grados de libertad

*Aparece en 6 clases.*

- `χ²` reducido es `χ²` entre los grados de libertad (número de datos menos de parámetros).
- Los grados de libertad son `N − p`.
- Los grados de libertad son datos menos parámetros ajustados.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C20](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md):**
- Ejercicio 2 · con una pista. ¿Cuántos grados de libertad tiene el ajuste?
- Con 19 997 grados de libertad, la desviación estándar esperada de `χ²/gl` es `√(2/19 997) = 0,010`; 1,186 está a unas 19 σ de 1: rechazo claro (la fórmula `√(2/gl)` es conocimiento general, no consultado aquí).
- 🎯 **Por qué importa:** Un análisis reproducible no es un conjunto de herramientas: es una cadena de comprobaciones donde cada eslabón puede fallar a la vista. La pregunta motivadora es: ¿cómo demuestro, con evidencia revisable, que mi resultado se obtuvo de estos datos, con este modelo y este software, y que otra persona lo repetirá?

📘 **Dónde se aprende:** [B14-C20 · Proyecto reproducible de análisis astronómico](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md); [B15-C16 · Ajuste de curvas](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md); [B26-C20 · Límites observacionales de modelos cosmológicos](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md); [B40-C15 · Varianza cósmica y límites de las mediciones del fondo](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md); [B51-C07 · Evaluación de residuos y diagnóstico de calidad de calibración](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md); [B101-C01 · Transformaciones homogéneas y parametrización de eslabones (Denavit-Hartenberg)](../programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/CLASE.md).

### GSD

*Aparece en 6 clases.*

- El GSD es el tamaño de píxel proyectado `H p/f`.
- El GSD (*ground sampling distance*) es la distancia en el suelo entre centros de píxeles contiguos.
- El GSD (*ground sample distance*) es el tamaño sobre el terreno que cubre un píxel.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B47-C25](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md):**
- Paso 2 · Fórmula. `GSD = h p/f = 5 × 10⁵ × 3,45 × 10⁻⁶/0,10`.
- Con la cámara ilustrativa (`h = 500 km`, píxel 3,45 µm, focal 0,10 m) el GSD es `17,25 m` y la franja `35,3 km`.
- 🎯 **Por qué importa:** Muchos CubeSat universitarios fracasan por requisitos sin cifra o sin evidencia. La decisión central: ¿qué requisitos medibles se fijan, cómo se verifican y cuáles cumple un diseño preliminar?

📘 **Dónde se aprende:** [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md); [B53-C25 · Corrección geométrica y ortorrectificación de imágenes planetarias](../programa/clases/B53/B53-C25-correccion-geometrica-y-ortorrectificacion-de-imagenes-planetarias/CLASE.md); [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md); [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md); [B121-C02 · Licenciamiento de actividades de teledetección](../programa/clases/B121/B121-C02-licenciamiento-de-actividades-de-teledeteccion/CLASE.md).

### Hash

*Aparece en 7 clases.*

- Fijar una versión es exigir exactamente esa. Hash es la suma de verificación (C11) de cada archivo descargable.
- Un hash (huella) es una función que resume un contenido;
- Un hash es un resumen de tamaño fijo de unos datos.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B23-C07](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md):**
- El registro agrupa: la cifra y su unidad, los parámetros, los hashes de datos y código, las versiones y el valor.
- La verificación numérica dice «reproducida dentro de tolerancia», porque la cifra casi no se mueve; pero el hash de los datos cambia, y la verificación lista «datos».
- 🎯 **Por qué importa:** Un informe dice «el modelo reproduce la posición con un error de 8,21 × 10⁻⁴ au». Seis meses después, nadie sabe con qué versión del código, qué archivo de datos ni qué tolerancia se calculó, y el número no se puede reproducir ni defender.

📘 **Dónde se aprende:** [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md); [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md); [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md); [B96-C22 · Transferencia de datos entre estación y centro de datos](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md); [B116-C03 · Historia clínica remota y registros médicos de misión](../programa/clases/B116/B116-C03-historia-clinica-remota-y-registros-medicos-de-mision/CLASE.md) y 1 más.

### Histéresis

*Aparece en 9 clases.*

- La histéresis es el camino distinto de ida y vuelta al variar `S`.
- La histéresis es un segundo umbral más bajo para desactivarla.
- Autocorrelación: dependencia con el pasado. Histéresis: umbrales distintos para cerrar y abrir.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B48-C06](../programa/clases/B48/B48-C06-meteorologia-de-observatorios/CLASE.md):**
- La histéresis reduce los cambios en 30,7 %, pero cuesta 3,3 puntos de tiempo abierto.
- Un termostato que se enciende y apaga en el mismo umbral parpadea; con dos umbrales (histéresis) espera a que el cambio sea claro.
- 🎯 **Por qué importa:** Un cierre que oscila abre y cierra la cúpula cientos de veces y desgasta el equipo. La decisión central: ¿qué regla de cierre evita el parpadeo sin perder tiempo útil?

📘 **Dónde se aprende:** [B48-C06 · Meteorología de observatorios](../programa/clases/B48/B48-C06-meteorologia-de-observatorios/CLASE.md); [B54-C19 · Modelos climáticos planetarios](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md); [B85-C08 · Calentadores y termostatos](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md); [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md); [B96-C06 · Telemetría operativa](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md); [B98-C05 · Autonomía de bajo nivel y comportamientos reactivos](../programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/CLASE.md) y 3 más.

### Holgura

*Aparece en 16 clases.*

- La holgura es el juego entre dientes.
- La ruta crítica es el camino de mayor duración; la holgura es el margen de una actividad fuera de ella.
- La holgura es el exceso de horas sobre las tareas.
- *(y 13 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C14](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md):**
- Una holgura de `0,01 mm` sobre un radio primitivo de `72 mm` equivale a `28,65"`.
- Descripción larga: la resolución por micropaso es sub-segundo de arco y la holgura supera ese valor en dos órdenes.
- ⚠️ **Error frecuente:** Olvidar la holgura. Se corrige con 8.3.
- 🎯 **Por qué importa:** El reductor fija la resolución, la fuerza disponible y el comportamiento dinámico. La decisión central: ¿qué relación, qué rendimiento y qué rigidez permiten apuntar con la resolución pedida sin resonancias?

📘 **Dónde se aprende:** [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md); [B83-C06 · Descomposición funcional](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md); [B90-C01 · Plan de ensamblaje e integración](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md); [B90-C05 · Documentación de interfaces](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md); [B96-C09 · Secuencias de misión](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md); [B101-C04 · Límites articulares, espacio de trabajo y evitación de colisiones](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md) y 10 más.

### Huella

*Aparece en 14 clases.*

- Una huella (*hash*) es un número de longitud fija calculado a partir del contenido de un archivo; si el contenido cambia, la huella cambia.
- Una huella (*hash*) es un resumen criptográfico (aquí SHA-256) de la configuración y de la trayectoria redondeada; si cualquier cosa cambia, cambia la huella.
- Una huella (*hash*) es un resumen que cambia si cambia el contenido.
- *(y 11 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Por ejemplo: `"""Devuelve la huella SHA-256 (hexadecimal) del contenido de un archivo."""`.
- (fuente, fecha, huella y licencia), ¿qué resultados produce y cómo se comprueban?
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.

📘 **Dónde se aprende:** [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md); [B11-C20 · Propagador reproducible de trayectoria](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md); [B12-C23 · Diagnóstico de convergencia y reproducibilidad de cadenas MCMC](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md); [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md); [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md); [B42-C17 · Estrellas guía artificiales](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md) y 8 más.

### Impulso total

*Aparece en 6 clases.*

- El impulso total es `I = ∫F dt = m_p·Isp·g₀`.
- El impulso total `I = ∫F dt` se mide en N·s.
- El impulso total `I` es el empuje por el tiempo.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B77-C06](../programa/clases/B77/B77-C06-relacion-masa-impulso/CLASE.md):**
- Analogía: un grifo y un balde: el caudal es el gasto, el agua total es la masa y el balde lleno es el impulso.
- Calcular el impulso total `I = m_p·Isp·g₀`.
- 🎯 **Por qué importa:** Con el mismo propelente, un motor de empuje alto lo quema rápido y uno de empuje bajo lo quema lento, pero el impulso total es el mismo. La decisión central: ¿cuánto impulso entrega una masa de propelente y qué empuje hace falta para despegar?

📘 **Dónde se aprende:** [B77-C06 · Relación masa-impulso](../programa/clases/B77/B77-C06-relacion-masa-impulso/CLASE.md); [B78-C01 · Empuje e impulso específico](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md); [B78-C10 · Propulsión de gas frío](../programa/clases/B78/B78-C10-propulsion-de-gas-frio/CLASE.md); [B78-C11 · Micropropulsión para CubeSat](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md); [B78-C21 · Erosión y vida útil de propulsores eléctricos](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md); [B119-C24 · Límites legales y de seguridad de la experimentación educativa](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md).

### Incertidumbre

*Aparece en 7 clases.*

- Y la incertidumbre es la forma honesta de decir cuánto conocemos un valor: un intervalo asociado a la medida, no un defecto de la medida.
- La incertidumbre es la estimación de qué tan lejos puede estar el valor medido del verdadero.
- Un error de redondeo es la diferencia entre el número y su redondeo. Incertidumbre es la duda sobre el valor; el SI y la guía de la metrología recomiendan reportarla con a lo sumo dos cifras significativas (S2).
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C01](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md):**
- El análisis completo de Planck publica 13,797 ± 0,023 Gyr (fuente S1, Tabla 1): nuestro cálculo simplificado coincide con él dentro de esa incertidumbre.
- Cada resultado depende de datos con incertidumbre, y esa incertidumbre se traslada al resultado.
- ⚠️ **Error frecuente:** Dar una cifra sin unidad ni incertidumbre. Se copia de un titular tal cual.
- 🎯 **Por qué importa:** Seguramente has leído que «el universo tiene 13 800 millones de años» o que «el universo observable mide 93 000 millones de años luz». Son frases que se repiten con total seguridad.

📘 **Dónde se aprende:** [B01-C01 · Naturaleza del universo](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md); [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md); [B31-C04 · Principio de incertidumbre](../programa/clases/B31/B31-C04-principio-de-incertidumbre/CLASE.md); [B71-C02 · Ley de gravitación universal](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md) y 1 más.

### Incertidumbre combinada

*Aparece en 8 clases.*

- La incertidumbre combinada de una función es la combinación de las `u` de sus datos (S2, apdo. 5.1.2).
- La incertidumbre combinada `u_c(y)` es la raíz cuadrada de `Σ c_i² u²(x_i)` cuando las entradas son independientes (S1, 2.3.4 y 5.1.2).
- La incertidumbre combinada de errores independientes es la raíz de la suma de sus cuadrados.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- Comparar dos resultados en unidades de incertidumbre combinada.
- Ejercicio 7. Compara 67,4 ± 0,5 con 73,04 ± 1,04 en unidades de incertidumbre combinada.
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.

📘 **Dónde se aprende:** [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B12-C16 · Propagación de incertidumbre](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md); [B13-C13 · Presupuestos de incertidumbre](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md); [B57-C32 · Sitios de calibración terrestres](../programa/clases/B57/B57-C32-sitios-de-calibracion-terrestres/CLASE.md); [B91-C05 · Medición y calibración de antenas](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md) y 2 más.

### Invariante

*Aparece en 6 clases.*

- Es lineal si la salida de una suma es la suma de las salidas, e invariante si no depende de cuándo empieza la serie.
- Un modelo es lineal si cumple superposición (lo precisa C03), invariante si sus parámetros no cambian con el tiempo, continuo si el tiempo es una variable real `t` y discreto si solo existe en instantes `kT`.
- Un invariante es una cantidad que la transformación no debe cambiar.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C01](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md):**
- El modelo de la sección 8.2 es lineal (el estado aparece solo multiplicado por constantes), invariante (`J` no cambia), continuo y de orden 2.
- Clasificar un modelo como lineal o no lineal, continuo o discreto, invariante o variante.
- 🎯 **Por qué importa:** Un telescopio espacial tiene que apuntar a una estrella y mantenerse allí. El telescopio Hubble lo hace con una desviación de no más de 0,007 segundos de arco durante al menos 24 horas (fuente S2).

📘 **Dónde se aprende:** [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md); [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md); [B71-C17 · Movimientos en planos orbitales](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md); [B71-C20 · Propagador kepleriano verificable](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md); [B96-C20 · Simulación de jornada de control de misión](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md); [B98-C02 · Sistemas de decisión autónomos y máquinas de estados de comportamiento](../programa/clases/B98/B98-C02-sistemas-de-decision-autonomos-y-maquinas-de-estados-de-comportamiento/CLASE.md).

### Irradiancia

*Aparece en 10 clases.*

- La irradiancia es la potencia por unidad de área (W/m²).
- La irradiancia `f` es la potencia por unidad de área que llega (W/m²) y la luminosidad `L` la potencia total que emite (W).
- La irradiancia `S` es la potencia por unidad de área (W/m²).
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C10](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md):**
- La irradiancia es `S = P/(4πd²)`, que es proporcional a `1/d²`.
- Pregunta. ¿Qué fracción de la irradiancia terrestre recibe Marte?
- 🎯 **Por qué importa:** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?

📘 **Dónde se aprende:** [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md); [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md); [B45-C01 · Radiometría y fotometría](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md); [B54-C03 · Equilibrio radiativo](../programa/clases/B54/B54-C03-equilibrio-radiativo/CLASE.md); [B56-C08 · Habitabilidad de Marte](../programa/clases/B56/B56-C08-habitabilidad-de-marte/CLASE.md) y 4 más.

### Jacobiano

*Aparece en 12 clases.*

- El jacobiano es el factor que corrige el elemento de área o volumen al cambiar de coordenadas: `r` en polares, `r² sin θ` en esféricas (ecs. 1.5.39 y 1.5.41).
- El jacobiano de `f: ℝⁿ → ℝᵐ` es la matriz `m × n` de derivadas parciales `Jᵢⱼ = ∂fᵢ/∂pⱼ`.
- El jacobiano `J` es la matriz de derivadas `Jᵢⱼ = ∂y(tᵢ; p)/∂pⱼ`: cuánto cambia cada predicción si se mueve cada parámetro.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C18](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md):**
- *Descripción textual:* se elige el sistema de coordenadas según la simetría, se escribe el elemento de volumen con su jacobiano, se integra iterativamente y se verifica con un caso conocido.
- Su límite: si olvidas el jacobiano, las capas externas pesan igual que las internas, lo cual es falso.
- ⚠️ **Error frecuente:** Olvidar el jacobiano. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** La masa de la Tierra se conoce mucho mejor que la distribución de esa masa en su interior. Un solo número, la densidad media, no basta: el momento de inercia depende de cómo se reparte la masa.

📘 **Dónde se aprende:** [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md); [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md); [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md); [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md); [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md) y 6 más.

### Jitter

*Aparece en 6 clases.*

- El jitter es el componente rápido.
- El jitter es su variación.
- El jitter es la desviación aleatoria rápida del eje.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B47-C10](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md):**
- El modelo supone PSF gaussiana y *jitter* independiente por eje; ignora la deriva y la dependencia temporal con el tiempo de exposición.
- *Descripción textual:* la PSD describe cómo se reparte la potencia del *jitter* en frecuencia; integrada da el RMS y este ensancha la imagen.
- 🎯 **Por qué importa:** Una buena óptica con mal apuntamiento da imágenes borrosas. La decisión central: ¿qué RMS de *jitter* se puede tolerar para perder menos del 10 % del pico?

📘 **Dónde se aprende:** [B47-C10 · Estabilidad de apuntamiento](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md); [B48-C10 · Redes de instrumentos](../programa/clases/B48/B48-C10-redes-de-instrumentos/CLASE.md); [B87-C15 · Apuntamiento de alta precisión](../programa/clases/B87/B87-C15-apuntamiento-de-alta-precision/CLASE.md); [B88-C19 · Simulación hardware-in-the-loop](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md); [B88-C26 · Latencia de interrupciones y jitter](../programa/clases/B88/B88-C26-latencia-de-interrupciones-y-jitter/CLASE.md); [B92-C03 · Adquisición, apuntamiento y seguimiento ópticos](../programa/clases/B92/B92-C03-adquisicion-apuntamiento-y-seguimiento-opticos/CLASE.md).

### Latencia

*Aparece en 10 clases.*

- La latencia es el tiempo entre el suceso y la alerta.
- La latencia es `N·Δt` para una falla persistente.
- La latencia es el retardo del lazo.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C09](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md):**
- ET["etapas: 10+20+10+30 s"] --> L["latencia total = 70 s"]
- *Descripción textual:* las etapas suman la latencia; el FAR se traduce a probabilidad y sigmas; el umbral sale de la cola del ruido y se contrasta por Monte Carlo; el factor de pruebas pasa de p local a global.
- ⚠️ **Error frecuente:** Tomar las latencias por medidas. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Una alerta tardía pierde el evento; una alerta con muchas falsas alarmas agota a los observadores. La decisión central: ¿qué umbral produce una tasa de falsas alarmas aceptable y cuánto tarda la alerta en llegar?

📖 **Explicado a fondo:** [Latencia](esencial/ampliacion-a-m.md#latencia).

📘 **Dónde se aprende:** [B28-C09 · Alertas científicas en tiempo real](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md); [B88-C12 · Detección aislamiento y recuperación de fallos](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md); [B88-C19 · Simulación hardware-in-the-loop](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md); [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md); [B88-C25 · Redundancia de procesamiento y ejecución en paralelo (lockstep)](../programa/clases/B88/B88-C25-redundancia-de-procesamiento-y-ejecucion-en-paralelo-lockstep/CLASE.md); [B88-C26 · Latencia de interrupciones y jitter](../programa/clases/B88/B88-C26-latencia-de-interrupciones-y-jitter/CLASE.md) y 4 más.

### Ley de Wien

*Aparece en 7 clases.*

- La ley de Wien relaciona la longitud de onda del máximo con la temperatura, `λ_max·T = b`.
- La ley de Wien dice que el máximo de `L_λ` está en `λ_max = b/T`, con `b = hc/(k x)` y `x` la solución de `x = 5(1 − e⁻ˣ)`.
- La ley de Wien liga la temperatura de un cuerpo negro con la longitud de onda del máximo: `λ_max T = b`, con `b = 2,897 771 955 × 10⁻³ m·K` (S1).
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- Y el cuerpo negro es una aproximación: las estrellas tienen líneas y la temperatura de Wien es solo una estimación del color dominante.
- Estimar una temperatura con la ley de Wien y decir cuándo no aplica.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📘 **Dónde se aprende:** [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B13-C17 · Calibración radiométrica](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md); [B24-C10 · Espectros y clasificación estelar](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md); [B28-C02 · Fotones en múltiples longitudes de onda](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md); [B45-C13 · Temperatura y espectro de cuerpo negro](../programa/clases/B45/B45-C13-temperatura-y-espectro-de-cuerpo-negro/CLASE.md); [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md) y 1 más.

### Límite

*Aparece en 7 clases.*

- El límite de `f(x)` cuando `x` tiende a `a`, escrito `lim_{x→a} f(x) = L`, significa que `f(x)` se acerca a `L` tanto como se quiera al acercar `x` a `a`, sin importar el valor de `f` en `a` (S1).
- Un intervalo o límite define `lo` y `hi`: mínimo–máximo o por percentiles (el percentil `p` es el valor bajo el cual está `p`% de los datos).
- Una afirmación es lo que el artículo sostiene; la evidencia es lo que la apoya; el límite es lo que la evidencia no permite concluir.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C01](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md):**
- Si existen `lim f = L` y `lim g = M`: el límite de una suma, producto o cociente (con `M ≠ 0`) es la suma, el producto o el cociente de los límites (S1, §1.4(ii)).
- El límite matemático es correcto; la fórmula ingenua falla en la máquina.
- ⚠️ **Error frecuente:** Afirmar que el límite existe porque la tabla «se ve» estable. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Los astrónomos miden distancias a estrellas cercanas por paralaje: un ángulo diminuto, de fracciones de segundo de arco. Con ángulos tan pequeños, `sin t`, `tan t` y `t` casi coinciden, y casi todos los cálculos prácticos los sustituyen.

📘 **Dónde se aprende:** [B09-C01 · Límites de funciones reales](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md); [B15-C10 · Histogramas y normalización](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md); [B90-C13 · Compatibilidad electromagnética EMC](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md); [B96-C06 · Telemetría operativa](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md); [B127-C04 · Exclusiones, deducibles y límites de pólizas](../programa/clases/B127/B127-C04-exclusiones-deducibles-y-limites-de-polizas/CLASE.md) y 1 más.

### Línea base

*Aparece en 7 clases.*

- La línea base (*baseline*) es la versión de referencia contra la que se mide una mejora.
- La línea base es el mejor código serie, no el código paralelo con un proceso.
- La línea base es el nivel sin perturbación.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B18-C04](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md):**
- Línea base<br/>correcta y cronometrada"] --> B["2.
- Se parte de una línea base correcta y cronometrada; se perfila para ver qué concentra el tiempo; se decide qué cambiar (algoritmo, estructura de datos o implementación); se cambia una sola cosa; se verifica que el resultado no cambió y se vuelve a medir, lo que lleva de nuevo a perfilar.
- 🎯 **Por qué importa:** Casi todo programa científico tiene un cuello de botella que el autor no sospecha. Optimizar a ojo suele mejorar lo que no importa.

📘 **Dónde se aprende:** [B18-C04 · Perfilado de rendimiento](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md); [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md); [B30-C23 · Índices geomagnéticos Kp y Dst](../programa/clases/B30/B30-C23-indices-geomagneticos-kp-y-dst/CLASE.md); [B42-C10 · Interferometría de múltiples telescopios](../programa/clases/B42/B42-C10-interferometria-de-multiples-telescopios/CLASE.md); [B57-C27 · Detección de cambios en series de imágenes](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md); [B83-C15 · Gestión de configuración](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md) y 1 más.

### Lineal

*Aparece en 12 clases.*

- Una relación lineal es `y = kx + b`; es proporcional solo si `b = 0`.
- Una ecuación es lineal si la incógnita aparece solo a la primera potencia, y cuadrática si el mayor exponente es 2.
- Las formas básicas son lineal (2 dominios, 180°), trigonal plana (3, 120°) y tetraédrica (4, 109,47°).
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C10](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md):**
- En cambio `y = 3, 5, 7` da `3; 2,5; 2,33`: no es proporcional (es lineal con `b = 1`).
- El límite: en una pizza el reparto es lineal en el número de personas; la luz se reparte sobre una superficie esférica cuya área crece con el cuadrado de la distancia (C17), de ahí `1/d²`.
- 🎯 **Por qué importa:** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?

📘 **Dónde se aprende:** [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md); [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md); [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md); [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md); [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md); [B11-C03 · Ecuaciones de primer orden](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md) y 6 más.

### Magnitud

*Aparece en 8 clases.*

- La magnitud es una escala de brillo en la que una diferencia de 5 magnitudes equivale a un factor 100 en flujo; mayor magnitud = más débil.
- La magnitud es una escala logarítmica de brillo (C10).
- Una magnitud es una propiedad medible (longitud, masa, tiempo).
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C10](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md):**
- En magnitudes, `Δm = 2,5·log₁₀(204) = 5,77`: ve objetos 5,8 magnitudes más débiles.
- Paso 5 · Luz. `Δm = 2,5·log₁₀(204) = 5,77` magnitudes.
- 🎯 **Por qué importa:** Si el ojo bastara, no habría observatorios. La luz visible es una franja pequeña del espectro electromagnético (S1, S2); además, tu pupila recoge poca luz, separa detalles hasta cierto tamaño y puede engañarte.

📘 **Dónde se aprende:** [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md); [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md); [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md); [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md); [B45-C02 · Magnitudes y sistemas de filtros](../programa/clases/B45/B45-C02-magnitudes-y-sistemas-de-filtros/CLASE.md) y 2 más.

### Magnitud límite

*Aparece en 6 clases.*

- La magnitud límite de un catálogo es el brillo mínimo que incluye (C11).
- La magnitud límite es la del objeto más débil que se puede ver en un cielo y con un instrumento dados; la IMO usa 6,5 como referencia en su definición de ZHR (S4).
- La magnitud límite (MLE) es la de la estrella más débil visible; depende del cielo, del ojo y del instrumento; la IMO la define como la estrella más débil que se ve durante una sesión (S3).
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C11](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md):**
- Con 200 mm: 7,28 magnitudes y límite ideal ≈ 13,8.
- Pero esa noche la Luna llena aclara el cielo, y la magnitud límite del ojo no sería 6,5 sino menor (C12 lo mide).
- 🎯 **Por qué importa:** Un informe dice «cometa de magnitud 6» y otro «galaxia de magnitud 9». Sin entender la escala, no sabrás si los verás a simple vista, con binoculares o solo con telescopio.

📘 **Dónde se aprende:** [B08-C06 · Constelaciones y catálogos estelares](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md); [B08-C11 · Magnitudes aparentes y brillo](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md); [B08-C12 · Limitación por contaminación lumínica](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md); [B41-C10 · Apertura y relación focal](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md); [B42-C21 · Estrellas guía naturales y cobertura de cielo](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md); [B129-C03 · Seguimiento ciudadano de meteoros](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md).

### Margen

*Aparece en 30 clases.*

- El margen es la diferencia.
- El margen es el requisito menos el total.
- El margen es la parte añadida por incertidumbre.
- *(y 27 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C20](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md):**
- El requisito `S ≥ 0,8` exige `σ ≤ 41,35 nm`; el margen es `14,89 nm`.
- El frente de onda suma `26,46 nm` RMS (Monte Carlo: `26,45 nm`), Strehl `0,913` frente al requisito `0,8` (`σ ≤ 41,35 nm`; margen `14,89 nm`).
- ⚠️ **Error frecuente:** Ignorar el margen. Se corrige con 8.1.
- 🎯 **Por qué importa:** El proyecto completo exige que los errores se sumen, se verifiquen y se comparen con los requisitos. La decisión central: ¿qué fuente domina el error, cuánto margen queda y la estructura es lo bastante rígida para el servo?

📘 **Dónde se aprende:** [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md); [B47-C02 · Requisitos de instrumentos orbitales](../programa/clases/B47/B47-C02-requisitos-de-instrumentos-orbitales/CLASE.md); [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md); [B50-C15 · Presupuesto de error de frente de onda de un instrumento](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md); [B75-C09 · Presupuestos de delta-v](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md); [B83-C09 · Presupuestos de masa](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md) y 24 más.

### Masa reducida

*Aparece en 6 clases.*

- La masa reducida `m₁m₂/(m₁ + m₂)` es la masa del cuerpo ficticio.
- La masa reducida `R_M = R_∞/(1 + m_e/M)`.
- La masa reducida `μ` resume las dos masas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B45-C10](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md):**
- El factor de masa reducida del hidrógeno es `0,99945568`.
- *Descripción textual:* la constante de Rydberg con masa reducida da las longitudes de onda y el ruido de fotones fija la precisión del centroide.
- ⚠️ **Error frecuente:** Olvidar la masa reducida. Se corrige con 8.2.
- 🎯 **Por qué importa:** Las líneas de emisión identifican elementos y miden velocidad y flujo. La decisión central: ¿dónde está cada línea del hidrógeno y con qué precisión se mide su posición?

📘 **Dónde se aprende:** [B36-C10 · Búsqueda directa de materia oscura en laboratorio](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md); [B45-C10 · Líneas de emisión](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md); [B60-C01 · Colisiones moleculares y secciones eficaces en gas interestelar](../programa/clases/B60/B60-C01-colisiones-moleculares-y-secciones-eficaces-en-gas-interestelar/CLASE.md); [B71-C02 · Ley de gravitación universal](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md); [B71-C03 · Ecuación de movimiento de dos cuerpos](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md); [B76-C16 · Acoplamiento y captura](../programa/clases/B76/B76-C16-acoplamiento-y-captura/CLASE.md).

### Máscara

*Aparece en 7 clases.*

- La máscara es la imagen binaria resultante.
- Una máscara es la imagen de etiquetas.
- La máscara es una imagen binaria de agua.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C13](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md):**
- Una máscara vacía («no hay manchas») acierta el 98,8 % de los píxeles del disco, porque las manchas ocupan el 1,165 % (179 de 15 361).
- El área medida es la suma de los píxeles de la máscara: 178 px, 1,159 % del disco (verdad: 179, 1,165 %).
- 🎯 **Por qué importa:** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.

📘 **Dónde se aprende:** [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md); [B40-C12 · Análisis de mapas del CMB: pixelización esférica y máscaras](../programa/clases/B40/B40-C12-analisis-de-mapas-del-cmb-pixelizacion-esferica-y-mascaras/CLASE.md); [B44-C15 · Píxeles defectuosos](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md); [B44-C20 · Pipeline inicial de calibración de imágenes](../programa/clases/B44/B44-C20-pipeline-inicial-de-calibracion-de-imagenes/CLASE.md); [B57-C15 · Sequías e inundaciones](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md) y 1 más.

### Matriz de transición

*Aparece en 7 clases.*

- La matriz de transición es `Φ(t) = e^(At)`.
- La matriz de transición `Φ` es la derivada de la posición de llegada respecto a la velocidad de salida.
- La matriz de transición `P` tiene entradas `Pᵢⱼ = P(siguiente = j | actual = i)` y cada fila suma 1.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C13](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md):**
- Definir una cadena de Markov y su matriz de transición, y calcular sus probabilidades de `n` pasos.
- 🎯 **Por qué importa:** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.

📘 **Dónde se aprende:** [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B16-C02 · Representaciones en espacio de estados](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md); [B74-C09 · Filtro de Kalman extendido](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md); [B74-C12 · Propagación de incertidumbre — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md); [B75-C18 · Propagación de dispersión inicial](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md) y 1 más.

### Matriz de verificación

*Aparece en 8 clases.*

- Una matriz de verificación lista cada requisito, el método de comprobación, el criterio de aceptación y el resultado.
- La matriz de verificación asigna a cada requisito un método.
- La matriz de verificación vincula cada requisito con su método y evidencia.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C19](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md):**
- *Descripción textual:* cada requisito se comprueba por cuatro vías (fórmula, simulación continua, lazo muestreado y barrido de parámetros) y los resultados se reúnen en la matriz de verificación.
- Ejercicio 12 · integrador. Entrega un informe de verificación: para un lazo de tu elección, escribe cinco requisitos con criterio, verifica el simulador (fórmula y orden de convergencia), ejecuta la matriz con barrido y versión muestreada, informa los incumplimientos, rediseña y repite.
- 🎯 **Por qué importa:** Un lazo que «se ve bien» en una simulación puede estar mal por tres razones: el diseño no cumple un requisito en parte del rango de parámetros, la discretización en el computador de vuelo cambia el comportamiento, o el simulador tiene un error numérico.

📘 **Dónde se aprende:** [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md); [B83-C14 · Revisiones CDR y TRR](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md); [B87-C19 · Verificación de ley de control](../programa/clases/B87/B87-C19-verificacion-de-ley-de-control/CLASE.md); [B88-C20 · Plan de verificación de computador de vuelo](../programa/clases/B88/B88-C20-plan-de-verificacion-de-computador-de-vuelo/CLASE.md); [B90-C18 · Trazabilidad de evidencias](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md) y 2 más.

### Media

*Aparece en 8 clases.*

- La media es la suma dividida por el número de lecturas; la desviación estándar experimental `s` mide su dispersión; la incertidumbre de la media es `s/√n`.
- El cociente de diferencias de `f` entre `x` y `x + h` es `[f(x + h) − f(x)]/h`: la tasa de cambio media en ese intervalo.
- La media (o esperanza) de la espera es `∫₀^∞ t f(t) dt`.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- Para `n` lecturas `x_i`: `media = Σx_i/n`;
- Caso analítico: `{1, 2, 3, 4, 5}` da `media = 3`, `s = 1,581`, `u = 0,707`.
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.

📘 **Dónde se aprende:** [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B09-C03 · Derivada como tasa de cambio](../programa/clases/B09/B09-C03-derivada-como-tasa-de-cambio/CLASE.md); [B09-C10 · Integración por partes](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B71-C13 · Anomalías orbitales](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md); [B71-C14 · Ecuación de Kepler](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md) y 2 más.

### Mediana

*Aparece en 6 clases.*

- Un cuantil `q_α` cumple `F(q_α) = α`; la mediana es `q_0,5`.
- La mediana es el valor central.
- La mediana resiste valores atípicos pero es `√(π/2) = 1,2533` veces más ruidosa.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- `P(T > 7) = 3 · 0,1 = 0,3`; mediana `5 s`.
- P(Y = 0) = 0 (un punto); mediana = 0.0; cuantil 0.95 = 1.7999999999999998
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.

📘 **Dónde se aprende:** [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md); [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md); [B44-C12 · Calibración con bias](../programa/clases/B44/B44-C12-calibracion-con-bias/CLASE.md); [B45-C23 · Fotometría de apertura y estimación del cielo](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md); [B48-C11 · Calidad y clasificación de datos](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md); [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md).

### Modelo

*Aparece en 6 clases.*

- Un modelo es una representación simplificada del mundo, con reglas y parámetros, que sirve para predecir y que sólo vale dentro de ciertos límites.
- Un modelo es una simplificación que permite pasar de datos a magnitudes que no se miden directamente: «la distancia es `v/H₀`».
- El modelo es la función `F(t) = 1 − δ·clip((D/2 − |t − t₀|)/τ, 0, 1)` con `δ` (profundidad), `t₀` (centro), `D` (duración) y `τ = 1000 s` (ingreso, fijo).
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C01](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md):**
- Fíjate cómo se encadenan las tres capas: Hα en 662,9 nm (observación) → `z` y `v` (inferencia) → `d` con `H₀` (modelo).
- En el modelo ΛCDM la expansión se frenó al principio por la atracción de la materia, y más tarde se aceleró por la llamada energía oscura; ambos efectos se compensan en parte, y por eso `1/H₀` queda cerca de la edad, pero sin igualarla.
- 🎯 **Por qué importa:** Seguramente has leído que «el universo tiene 13 800 millones de años» o que «el universo observable mide 93 000 millones de años luz». Son frases que se repiten con total seguridad.

📘 **Dónde se aprende:** [B01-C01 · Naturaleza del universo](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md); [B01-C05 · Observación frente a interpretación](../programa/clases/B01/B01-C05-observacion-frente-a-interpretacion/CLASE.md); [B14-C20 · Proyecto reproducible de análisis astronómico](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md); [B15-C16 · Ajuste de curvas](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md); [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md); [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### Módulo de distancia

*Aparece en 6 clases.*

- La magnitud aparente `m` mide cuán brillante *se ve* un objeto desde donde se mide; la magnitud absoluta `M` es la que tendría a 10 parsecs; la diferencia `m − M` es el módulo de distancia.
- El módulo de distancia es `m − M = 5 log₁₀(d/10 pc)`.
- El módulo de distancia es `5 log₁₀(d/10 pc)`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- *Descripción textual:* se parte de un flujo, se divide por el flujo de referencia, se aplica `−2,5 log₁₀` para obtener la magnitud, y restando la magnitud absoluta se obtiene el módulo de distancia, de donde sale la distancia.
- Paso 3 · Módulo de distancia. `d = 1 au = 4,848 × 10⁻⁶ pc`;
- ⚠️ **Error frecuente:** Olvidar el −5 del módulo de distancia o usar `d` en au. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.

📘 **Dónde se aprende:** [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md); [B25-C19 · Catálogos y sesgos de selección](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md); [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md); [B28-C19 · Limitaciones y sesgos de detección](../programa/clases/B28/B28-C19-limitaciones-y-sesgos-de-deteccion/CLASE.md); [B45-C02 · Magnitudes y sistemas de filtros](../programa/clases/B45/B45-C02-magnitudes-y-sistemas-de-filtros/CLASE.md).

### Momento angular específico

*Aparece en 6 clases.*

- El momento angular específico es `h = L/m` (m²/s).
- La energía específica (por unidad de masa) es `E = v²/2 − GM/r` y el momento angular específico, `L = x·vy − y·vx`; ambos se conservan en un campo central.
- El momento angular específico `j` es el momento angular por unidad de masa.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C09](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md):**
- El script [momento_angular_orbita.py](momento_angular_orbita.py) integra una órbita elíptica con velocity-Verlet y comprueba que el momento angular específico no varíe (< 10⁻⁹), que el apoapsis integrado coincida con el analítico (10⁻³) y que `h/2 = área/T` (10⁻⁶).
- 🎯 **Por qué importa:** Un satélite en órbita elíptica va más rápido cerca de la Tierra que lejos; un patinador gira más rápido al recoger los brazos. La pregunta motivadora es: ¿qué cantidad se mantiene constante cuando algo gira bajo una fuerza central, y qué hace falta para cambiar un giro?

📘 **Dónde se aprende:** [B05-C09 · Momento angular y torque](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md); [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md); [B26-C08 · Geodésicas gravitacionales](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md); [B52-C01 · Colapso de nebulosa protosolar](../programa/clases/B52/B52-C01-colapso-de-nebulosa-protosolar/CLASE.md); [B71-C06 · Momento angular específico](../programa/clases/B71/B71-C06-momento-angular-especifico/CLASE.md).

### Monte Carlo

*Aparece en 18 clases.*

- Una Monte Carlo es una simulación con muestras aleatorias para estimar una distribución.
- La propagación lineal de la covarianza es `P(t) = Φ P₀ Φᵀ`. Monte Carlo propaga muestras.
- La RSS es `√Σtᵢ²`. Monte Carlo muestrea cada dimensión.
- *(y 15 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B10-C19](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md):**
- No: `r cos(el)` vale `1,75 km`, el jacobiano casi pierde rango (azimut mal definido) y la distribución no es gaussiana; usar Monte Carlo o otra parametrización (8.5).
- Ejercicio 12 · integrador. Elabora tu informe de linealización: una función de tres entradas y tres salidas, su jacobiano analítico verificado con diferencias finitas, la tabla de error de linealización para tres pasos, la propagación de covarianza contrastada con Monte Carlo y los casos en que falla.
- 🎯 **Por qué importa:** Una estación mide la distancia, el azimut y la elevación de un objeto con incertidumbres. Para decir dónde está en coordenadas cartesianas y cuánta incertidumbre tiene esa posición, hay que transformar los números y sus errores.

📘 **Dónde se aprende:** [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md); [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B26-C12 · Escalas de distancia cosmológicas](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md); [B30-C03 · Ciclo de actividad solar](../programa/clases/B30/B30-C03-ciclo-de-actividad-solar/CLASE.md); [B58-C08 · Propagación de incertidumbre orbital](../programa/clases/B58/B58-C08-propagacion-de-incertidumbre-orbital/CLASE.md); [B74-C12 · Propagación de incertidumbre — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md) y 12 más.

### Movimiento medio

*Aparece en 6 clases.*

- El movimiento medio `n` es la velocidad angular promedio de la órbita (rad/d).
- El movimiento medio `n = 2π/P` es la velocidad angular media.
- El movimiento medio es `n = √(μ/a³)`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C06](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md):**
- Movimiento medio n = 1.990976e-07 rad/s -> periodo 365.258 d
- 🎯 **Por qué importa:** Para saber dónde está un planeta en su órbita en un instante dado hay que resolver la ecuación de Kepler, `M = E − e sin E`, que no tiene solución en funciones elementales: no se puede despejar `E`.

📘 **Dónde se aprende:** [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B23-C03 · Casos analíticos de validación](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md); [B52-C07 · Resonancias orbitales](../programa/clases/B52/B52-C07-resonancias-orbitales/CLASE.md); [B71-C13 · Anomalías orbitales](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md); [B74-C29 · Formatos TLE y OMM de elementos orbitales](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md); [B75-C02 · Ángulos de fase planetaria](../programa/clases/B75/B75-C02-angulos-de-fase-planetaria/CLASE.md).

### MTBF

*Aparece en 6 clases.*

- El MTBF (o MTTF) es `1/λ` en el modelo exponencial.
- Cota superior de confianza: valor que, con probabilidad `CL`, no es inferior a la tasa verdadera. MTBF: tiempo medio entre fallas.
- La tasa de falla `λ` es la probabilidad de fallar por unidad de tiempo; el MTBF es `1/λ` con tasa constante.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C09](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md):**
- M["MTBF, MTTR"] --> A["A = MTBF/(MTBF+MTTR)"]
- Ejercicio 5. `A` con MTBF = 2000 h y MTTR = 24 h.
- 🎯 **Por qué importa:** Una unidad adicional mejora menos que la anterior y las fallas comunes limitan la ganancia. La decisión central: ¿cuántas unidades de respaldo valen la pena?

📘 **Dónde se aprende:** [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B86-C11 · Redundancia eléctrica](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md); [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md); [B93-C04 · Análisis de confiabilidad de electrónica (MTBF y derating)](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md); [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### Muestreo de Nyquist

*Aparece en 6 clases.*

- El muestreo de Nyquist: al menos 2 píxeles por `λ/D`.
- El muestreo de Nyquist pide al menos dos píxeles por elemento resoluble.
- El muestreo de Nyquist pide al menos `2` píxeles por FWHM.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C01](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md):**
- Decidir el tamaño de píxel por muestreo de Nyquist.
- 🎯 **Por qué importa:** Sin requisitos escritos, cada pieza del telescopio se fabrica «lo mejor posible» y no se sabe cuándo basta. La decisión central: ¿qué error de frente de onda, qué escala de imagen y qué tolerancia mecánica hay que pedir, y cómo se reparte el error entre las piezas?

📘 **Dónde se aprende:** [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md); [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md); [B43-C01 · Requisitos ópticos y mecánicos](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md); [B44-C17 · Escala de imagen y muestreo](../programa/clases/B44/B44-C17-escala-de-imagen-y-muestreo/CLASE.md); [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md); [B46-C09 · Conversión analógica digital](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md).

### Núcleo

*Aparece en 10 clases.*

- El núcleo es el conjunto de funciones puras que contiene la ciencia.
- Un proceso gaussiano es un modelo que para cada entrada da una distribución normal; su núcleo (*kernel*) define cuánto se parecen las salidas de dos entradas cercanas, y el de base radial (RBF) tiene una longitud de escala por variable (S1).
- El núcleo es la zona donde el gas gana calor.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- La masa está casi toda en el núcleo: un protón pesa unas 1836 veces más que un electrón (S1).
- Por eso, a la primera aproximación, el electrón se mueve alrededor de un núcleo que apenas se mueve.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.

📘 **Dónde se aprende:** [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md); [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md); [B27-C12 · Radiación sincrotrón](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md); [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md) y 4 más.

### Número de condición

*Aparece en 9 clases.*

- El número de condición `κ(A)` mide cuánto puede amplificarse el error relativo (se define con valores singulares en C11).
- El número de condición es `κ = σ₁/σ_r`.
- El número de condición `κ` de una cuadrática `½ xᵀ A x` es la razón entre su mayor y menor valor propio.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B10-C05](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md):**
- El número de condición es `κ = 1,67`: bien condicionado.
- Estimar la pérdida de cifras con el número de condición.
- ⚠️ **Error frecuente:** Ignorar el número de condición. Se corrige con los ejercicios 9 y 10.
- 🎯 **Por qué importa:** Para fijar la posición de un objeto a partir de las distancias a tres estaciones se plantean tres ecuaciones con dos incógnitas (plano). Los sistemas reales tienen decenas o miles de incógnitas: parámetros orbitales, sesgos de relojes, coeficientes de calibración.

📘 **Dónde se aprende:** [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md); [B10-C11 · Valores singulares y SVD](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md); [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md); [B57-C22 · Espectrómetros de imagen e hiperespectrales](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md); [B59-C05 · Minerales marcianos](../programa/clases/B59/B59-C05-minerales-marcianos/CLASE.md); [B74-C15 · Geometría de la red de seguimiento](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md) y 3 más.

### Orden

*Aparece en 18 clases.*

- El orden de un método indica cómo disminuye su error al reducir `dt`: orden 1, error ∝ `dt`; orden 2, error ∝ `dt²`.
- El orden de un método es el exponente `p` tal que el error escala como `hᵖ`.
- Un orden de aproximación es el grado del polinomio.
- *(y 14 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C20](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md):**
- (3) Orden de convergencia: al reducir `dt` a la mitad, el error de cierre de leapfrog debe dividirse por 4 y el de Euler por 2.
- M --> V{"¿cumple las referencias?<br/>T analítico, conservación,<br/>orden de convergencia"}
- 🎯 **Por qué importa:** Un simulador es la forma de explorar un fenómeno cuya solución no tienes a mano, y de comprobar que entiendes uno cuya solución sí conoces. Aquí conoces la respuesta (una órbita circular se repite con un período dado por una fórmula), así que puedes verificar el simulador antes de confiar en él para casos que no conoces.

📘 **Dónde se aprende:** [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md); [B09-C14 · Series y aproximaciones](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md); [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md); [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md); [B11-C05 · Método de Euler](../programa/clases/B11/B11-C05-metodo-de-euler/CLASE.md) y 12 más.

### Paralaje

*Aparece en 8 clases.*

- El paralaje es el pequeño cambio en la posición aparente de una estrella cercana, respecto de las lejanas, cuando la Tierra se mueve de un lado a otro de su órbita.
- El paralaje es el cambio de dirección de un objeto visto desde dos puntos distintos; la base es la distancia entre ellos.
- El paralaje `p` es el ángulo que subtiende la base vista desde el objeto (o, equivalentemente, el cambio de dirección del objeto al cambiar de punto de vista).
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C02](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md):**
- Paralaje. Mira un dedo estirado primero con un ojo y luego con el otro: parece moverse respecto del fondo.
- A["Radar y geometría directa: Luna, planetas"] --> B["Paralaje: estrellas cercanas, hasta cientos de pc"]
- ⚠️ **Error frecuente:** Creer que un método vale en todo rango. Por ejemplo, usar paralaje para Virgo.
- 🎯 **Por qué importa:** Cuando alguien dice que Próxima Centauri está «a cuatro años luz» y que Andrómeda está «a dos millones y medio», es fácil oír solo «lejos» y «más lejos». Pero entre una y otra hay un factor de casi seis cien mil.

📖 **Explicado a fondo:** [Paralaje y parsec](esencial/esencial-m-z.md#paralaje-y-parsec).

📘 **Dónde se aprende:** [B01-C02 · Escalas desde la Tierra al cosmos observable](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md); [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md); [B04-C07 · Triángulos y distancias angulares](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md); [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md); [B29-C04 · Astrometría de exoplanetas](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md) y 2 más.

### Parámetro

*Aparece en 12 clases.*

- Un parámetro es un número fijo del modelo que se ajusta (la constante `k` o el exponente `p`).
- Un parámetro es un símbolo cuyo valor se fija para un problema concreto pero puede cambiar entre problemas (el semieje `a` de un planeta).
- Un parámetro es el nombre que la función da a un dato de entrada; un argumento es el valor concreto que le pasas al llamarla.
- *(y 8 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- En el modelo `T = k·a^p`: las variables son `a` (en au) y `T` (en años); los parámetros son `k` y `p`; los supuestos, que los planetas orbitan el Sol, que sus masas son despreciables frente a la solar y que los datos son comparables entre sí.
- El ajuste mejora apenas, a costa de un parámetro más: no hay motivo para preferirlo.
- ⚠️ **Error frecuente:** Confundir parámetro con variable. Ejercicio 1.
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?

📘 **Dónde se aprende:** [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md); [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md); [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md); [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md) y 6 más.

### Paso

*Aparece en 10 clases.*

- El paso `dt` es el intervalo de tiempo de cada iteración.
- Un paso es el avance de `t_k` a `t_{k+1} = t_k + h`.
- Un paso es el avance en `t` entre dos evaluaciones del integrador; un método de paso adaptativo lo ajusta para controlar el error.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C05](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md):**
- Con ese orden de actualización, la suma de los pasos da `x = (g t² / 2)(1 − dt/t)`.
- Reducir el paso a la décima parte reduce el error a la décima parte (la regla del método de primer orden).
- 🎯 **Por qué importa:** Una simulación es un bucle: calcula el estado siguiente a partir del actual, una y otra vez. Si el paso es demasiado grande, el resultado se aparta de la realidad; si es demasiado pequeño, tarda.

📘 **Dónde se aprende:** [B07-C05 · Bucles y simulaciones sencillas](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md); [B11-C05 · Método de Euler](../programa/clases/B11/B11-C05-metodo-de-euler/CLASE.md); [B14-C03 · Análisis numérico con SciPy](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md); [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md); [B42-C15 · Espejos deformables](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md); [B43-C15 · Motores paso a paso y servomotores](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md) y 4 más.

### Pendiente

*Aparece en 9 clases.*

- La pendiente `m` de una recta que pasa por `(x₁, y₁)` y `(x₂, y₂)` es `m = (y₂ − y₁)/(x₂ − x₁)`: el cambio de `y` por cada unidad de `x`.
- La pendiente de una recta en log-log es el exponente de la ley de potencias.
- Una pendiente es el valor de `F` en un punto.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C16](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md):**
- Con la pendiente `m` y un punto, `y = y₁ + m(x − x₁)`.
- Con medias `x̄`, `ȳ` y sumas `S_xx = Σ(x − x̄)²` y `S_xy = Σ(x − x̄)(y − ȳ)`, la pendiente de mínimos cuadrados es `m = S_xy/S_xx` y la ordenada `b = ȳ − m x̄`.
- ⚠️ **Error frecuente:** Hablar de «la pendiente» de una curva. Ejercicio 8.
- 🎯 **Por qué importa:** Si sitúas en un gráfico logarítmico el período frente al semieje de los planetas, los puntos forman una recta. Su pendiente es 1,5: ese número es el exponente de la tercera ley de Kepler.

📘 **Dónde se aprende:** [B03-C16 · Pendiente e interpretación de gráficos](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md); [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md); [B11-C06 · Método de Heun](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md); [B53-C08 · Cartografía de cráteres](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md); [B57-C28 · Modelos digitales de elevación](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md); [B102-C08 · Traversabilidad y evaluación de riesgo de terreno](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md) y 3 más.

### Percentil

*Aparece en 7 clases.*

- Un percentil es el valor bajo el cual cae esa fracción de miembros.
- Un percentil es el valor bajo el cual cae esa fracción.
- El percentil P80 es la duración que se cumple con 80 % de probabilidad.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C02](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md):**
- Tránsito central `52,92 h`; conjunto: media `53,41 h`, desviación `7,09 h`, percentiles 5/50/95 `42,0/53,3/65,2 h`.
- Obtener media, desviación y percentiles.
- 🎯 **Por qué importa:** Un pronóstico de llegada sin incertidumbre es engañoso. La decisión central: ¿qué parámetro domina la incertidumbre del tiempo de llegada?

📘 **Dónde se aprende:** [B33-C02 · Modelos de propagación de CME](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md); [B40-C15 · Varianza cósmica y límites de las mediciones del fondo](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md); [B50-C13 · Análisis Monte Carlo de tolerancias ópticas](../programa/clases/B50/B50-C13-analisis-monte-carlo-de-tolerancias-opticas/CLASE.md); [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md); [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md); [B109-C06 · Antropometría y dimensionamiento para tripulación](../programa/clases/B109/B109-C06-antropometria-y-dimensionamiento-para-tripulacion/CLASE.md) y 1 más.

### Percentil 95

*Aparece en 6 clases.*

- El percentil 95 (p95) es el valor que supera el 5 % de las corridas.
- El percentil 95 es el tiempo que se supera solo el 5 % de las veces.
- El percentil 95 es el valor superado en el 5 % de los casos.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B76-C20](../programa/clases/B76/B76-C20-simulacion-de-encuentro-seguro/CLASE.md):**
- Resumir el error final, el `Δv` y la distancia mínima con media, percentil 95 y máximo.
- 🎯 **Por qué importa:** Cada pieza del bloque funciona en su caso ideal; la seguridad se juega en la combinación con errores. La decisión central: ¿llega el perseguidor con la precisión pedida y se mantiene fuera de la esfera de exclusión incluso si falla un impulso?

📘 **Dónde se aprende:** [B76-C20 · Simulación de encuentro seguro](../programa/clases/B76/B76-C20-simulacion-de-encuentro-seguro/CLASE.md); [B97-C20 · Misión robótica integrada simulada](../programa/clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md); [B98-C06 · Simulación de teleoperación con retardo](../programa/clases/B98/B98-C06-simulacion-de-teleoperacion-con-retardo/CLASE.md); [B104-C10 · Actividades extravehiculares EVA](../programa/clases/B104/B104-C10-actividades-extravehiculares-eva/CLASE.md); [B118-C21 · Calidad, latencia y trazabilidad de datos de vigilancia espacial](../programa/clases/B118/B118-C21-calidad-latencia-y-trazabilidad-de-datos-de-vigilancia-espacial/CLASE.md); [B119-C20 · Simulación de respuesta institucional a incidentes](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md).

### Pérdida de espacio libre

*Aparece en 6 clases.*

- La pérdida de espacio libre `FSPL = (4π d/λ)²` expresada en dB es el cociente entre la potencia transmitida y la recibida con antenas isótropas.
- La pérdida de espacio libre es `20 log(4πd/λ)`.
- La pérdida de espacio libre `L` es la atenuación por propagación en el vacío.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B47-C18](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md):**
- Calcular la distancia oblicua y la pérdida de espacio libre.
- distancia oblicua a 10 grados = 1932.25 km ; perdida de espacio libre = 176.45 dB
- 🎯 **Por qué importa:** Los datos que no caben en un paso se pierden o se acumulan. La decisión central: ¿cuántos bits por paso admite el enlace con margen suficiente?

📘 **Dónde se aprende:** [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md); [B47-C23 · Sondas heliosféricas: Parker Solar Probe y Voyager](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md); [B89-C04 · Propagación y pérdidas de espacio libre](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md); [B89-C05 · Presupuesto de enlace](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md); [B91-C08 · Antenas de gran apertura y estaciones de espacio profundo](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md); [B120-C02 · Zonas de coordinación entre servicios radioeléctricos](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md).

### Perihelio

*Aparece en 9 clases.*

- El perihelio es el punto más cercano al Sol (`a(1−e)`) y el afelio, el más lejano (`a(1+e)`).
- El perihelio `q` es el punto de la órbita más cercano al Sol (que está en un foco) y el afelio `Q` el más lejano.
- El perihelio es el punto más cercano al Sol; el afelio, el más lejano.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C14](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md):**
- Con `a = 227,956` millones de km (Marte, S3) y una excentricidad sintética `e = 0,2`: perihelio `a(1−e) = 182,4` y afelio `a(1+e) = 273,5` millones de km.
- El laboratorio calcula el área barrida durante un décimo del período partiendo del perihelio y durante otro décimo partiendo del afelio: ambas valen `1,5995×10⁴` (unidades de 10¹² km²) y su razón es `1,000000`.
- 🎯 **Por qué importa:** Para Kepler, como para todos antes, el círculo era la figura natural del cielo. Los datos de Tycho no se dejaban describir con círculos.

📘 **Dónde se aprende:** [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B26-C08 · Geodésicas gravitacionales](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md); [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md); [B47-C23 · Sondas heliosféricas: Parker Solar Probe y Voyager](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md) y 3 más.

### Período

*Aparece en 12 clases.*

- Un período es el tiempo que dura un ciclo.
- El período `T` es el tiempo de una vuelta; la frecuencia `f = 1/T` es el número de vueltas por segundo (hertz, Hz); la velocidad angular `ω = 2π/T` (rad/s) es el ángulo recorrido por unidad de tiempo.
- Una fila se llama periodo; una columna, grupo.
- *(y 8 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- La Luna da una vuelta alrededor de la Tierra respecto de las estrellas en 27,3217 días (el período sidéreo, S3).
- Hoy el Sistema Internacional lo define con un átomo: el segundo es la duración de 9 192 631 770 períodos de la radiación asociada a la transición hiperfina del estado fundamental del cesio 133 (S4).
- ⚠️ **Error frecuente:** Restar períodos en vez de frecuencias. En el mes lunar se resta 27,3 − 365,3.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).

📘 **Dónde se aprende:** [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md); [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md); [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md); [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md) y 6 más.

### Período sinódico

*Aparece en 11 clases.*

- El período sinódico de la Luna es el tiempo entre dos fases iguales (29,53 días), y el sidéreo es el que tarda en volver a la misma posición respecto de las estrellas (27,3217 días) (S3).
- El período sinódico (29,53 d) es el tiempo entre dos fases iguales; el sidéreo (27,3217 d), el de una vuelta respecto de las estrellas (C04).
- El período sidéreo `T` de un planeta es su tiempo de vuelta respecto de las estrellas; el período sinódico `S` es el tiempo entre dos configuraciones iguales vistas desde la Tierra (por ejemplo, dos oposiciones).
- *(y 8 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- Calcular cuánto difieren el día solar y el sidéreo, y deducir el período sinódico lunar a partir de dos ciclos.
- Ejercicio 4. Deduce el período sinódico lunar con la fórmula de la sección 8.2 y compáralo con el publicado.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).

📖 **Explicado a fondo:** [Período sinódico](esencial/ampliacion-n-z.md#período-sinódico).

📘 **Dónde se aprende:** [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B02-C11 · Revolución copernicana y métodos](../programa/clases/B02/B02-C11-revolucion-copernicana-y-metodos/CLASE.md); [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md); [B08-C10 · Planetas observables y elongación](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md); [B53-C27 · Detección remota de océanos subsuperficiales: inducción magnética, libración y radar](../programa/clases/B53/B53-C27-deteccion-remota-de-oceanos-subsuperficiales-induccion-magnetica-libracion-y-radar/CLASE.md) y 5 más.

### Persistencia

*Aparece en 6 clases.*

- La persistencia `ρ` es la fracción que sobrevive de un día al siguiente.
- La persistencia repite el valor de hace 24 h.
- La persistencia repite el último valor.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C01](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md):**
- Sesgo `−5,22 km/s`, RMSE `39,39 km/s`, correlación `0,8059`, `MSSS` frente a la climatología `0,5907` y frente a la persistencia de 24 h `0,3341`.
- Calcular MSSS frente a climatología y persistencia.
- 🎯 **Por qué importa:** Un modelo sin validación no sirve para pronosticar. La decisión central: ¿cuán bien reproduce el modelo la serie y con qué desfase?

📘 **Dónde se aprende:** [B33-C01 · Validación de modelos MHD con eventos solares documentados](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md); [B33-C11 · Modelos empíricos y de persistencia en clima espacial](../programa/clases/B33/B33-C11-modelos-empiricos-y-de-persistencia-en-clima-espacial/CLASE.md); [B48-C20 · Diseño de una campaña observacional profesional](../programa/clases/B48/B48-C20-diseno-de-una-campana-observacional-profesional/CLASE.md); [B88-C12 · Detección aislamiento y recuperación de fallos](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md); [B104-C16 · Manejo de conflictos](../programa/clases/B104/B104-C16-manejo-de-conflictos/CLASE.md); [B116-C05 · Alertas de salud y umbrales de monitorización](../programa/clases/B116/B116-C05-alertas-de-salud-y-umbrales-de-monitorizacion/CLASE.md).

### Peso

*Aparece en 16 clases.*

- El peso es la fuerza gravitatoria sobre un cuerpo, `W = m g`; la masa no cambia con el lugar, el peso sí.
- El peso es la amplitud y fase de cada uno.
- El peso `W_h` es la fracción del área total de cada estrato.
- *(y 12 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C04](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md):**
- La masa es propiedad del cuerpo; el peso depende de dónde esté.
- Y el peso en la superficie, `9806,65 N`, es solo un 13 % mayor que la fuerza a 400 km: la altura no es «salir de la gravedad».
- ⚠️ **Error frecuente:** Confundir masa y peso. Ejercicio 2.
- 🎯 **Por qué importa:** Un satélite no tiene motor encendido y aun así gira. Una nave en el espacio vacío mantiene su velocidad sin esfuerzo.

📖 **Explicado a fondo:** [Gravedad y peso](esencial/esencial-d-l.md#gravedad-y-peso).

📘 **Dónde se aprende:** [B05-C04 · Leyes del movimiento de Newton](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md); [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md); [B12-C15 · Muestreo de importancia](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md); [B47-C20 · Caso comparativo de observatorios espaciales](../programa/clases/B47/B47-C20-caso-comparativo-de-observatorios-espaciales/CLASE.md); [B48-C19 · Divulgación y ciencia ciudadana](../programa/clases/B48/B48-C19-divulgacion-y-ciencia-ciudadana/CLASE.md); [B49-C04 · Arreglos de antenas: factor de arreglo y formación de haz](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md) y 10 más.

### Posterior

*Aparece en 8 clases.*

- El prior `P(θ)` expresa lo que se sabe de `θ` antes de ver los datos; la verosimilitud `P(datos | θ)` es el modelo de los datos (C07); la posterior `P(θ | datos)` es el conocimiento actualizado; el denominador, la evidencia o verosimilitud marginal, normaliza (y es clave en C22).
- El posterior es el producto de verosimilitud y prior normalizado.
- El posterior es `P(H | datos)`.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C12](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md):**
- Con prior débil `Gamma(1; 0,1)` (media 10, muy difuso), `S = 37` y `n = 10`: posterior `Gamma(38; 10,1)`, media `3,7624`, intervalo creíble 95 % `[2,662; 5,049]`.
- Con prior informativo `Gamma(8; 2)` (media 4): posterior `Gamma(45; 12)`, media `3,750`, intervalo `[2,735; 4,922]`.
- 🎯 **Por qué importa:** Una misión rara vez parte de cero: hay pruebas en tierra, misiones anteriores y física conocida. Y a menudo el dato es escaso (diez intervalos, treinta pruebas).

📘 **Dónde se aprende:** [B12-C12 · Inferencia bayesiana](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md); [B19-C01 · Priors físicamente informados](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md); [B28-C22 · Inferencia bayesiana conjunta de parámetros de fuente multimensajero](../programa/clases/B28/B28-C22-inferencia-bayesiana-conjunta-de-parametros-de-fuente-multimensajero/CLASE.md); [B56-C15 · Falsos positivos de biofirmas](../programa/clases/B56/B56-C15-falsos-positivos-de-biofirmas/CLASE.md); [B63-C06 · Evaluación de riesgos biológicos de muestras: marcos de decisión](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md); [B67-C02 · Diseño de un programa de prospección por fases](../programa/clases/B67/B67-C02-diseno-de-un-programa-de-prospeccion-por-fases/CLASE.md) y 2 más.

### Potencia

*Aparece en 14 clases.*

- Una potencia `aⁿ` es `a` multiplicado por sí mismo `n` veces;
- La potencia `P = W/t` (o `F v`) se mide en vatios (W).
- La potencia eléctrica es `P = V I = I² R = V²/R`.
- *(y 10 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Producto de potencias de igual base: `aᵐ · aⁿ = aᵐ⁺ⁿ`.
- Potencia de un producto: `(ab)ⁿ = aⁿbⁿ`.
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.

📘 **Dónde se aprende:** [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md); [B05-C06 · Trabajo y energía](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md); [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md); [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md); [B12-C26 · Sesgos y potencia estadística en poblaciones pequeñas](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md) y 8 más.

### Precisión

*Aparece en 8 clases.*

- La estabilidad (no explotar) es distinta de la precisión (parecerse a la solución).
- La precisión es `TP/(TP + FP)`: de las alertas, cuántas son reales.
- La precisión (*sharpness*) es qué tan estrechos son los intervalos: un procedimiento puede estar calibrado y ser inútil (intervalos enormes).
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C09](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md):**
- D --> F["Luego revisar precisión<br/>(C19)"]
- *Descripción textual:* la ecuación de prueba reduce cada paso a una multiplicación por `R(hλ)`; si su módulo es menor o igual que uno el método es estable y se pasa a comprobar la precisión; si no, hay que reducir el paso o cambiar a un método implícito.
- ⚠️ **Error frecuente:** Pensar que un paso más pequeño siempre arregla la precisión sin pagar costo. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.

📘 **Dónde se aprende:** [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md); [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md) y 2 más.

### Presupuesto de error

*Aparece en 6 clases.*

- El presupuesto de error es el tiempo de caída que el SLO tolera.
- Un presupuesto de error suma (o combina en cuadratura) las contribuciones de cada fuente.
- Un presupuesto de error distribuye el error total entre etapas.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C19](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md):**
- *Descripción textual:* con pasos grandes domina el error de truncamiento; con pasos muy pequeños, el de redondeo; el error total tiene un mínimo; el presupuesto compara todas las fuentes para decidir dónde invertir.
- Armar un presupuesto de error con truncamiento, redondeo e incertidumbre de datos.
- 🎯 **Por qué importa:** Un resultado numérico sin cota de error es una cifra sin sentido. Y gastar horas de cálculo para reducir un error de método que ya es menor que la incertidumbre de los datos es un desperdicio.

📘 **Dónde se aprende:** [B11-C19 · Estimación de error y convergencia](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md); [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md); [B43-C01 · Requisitos ópticos y mecánicos](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md); [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md); [B73-C20 · Proyecto de integración celeste de precisión](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md); [B124-C21 · Acuerdos de nivel de servicio para productos de datos](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md).

### Procedencia

*Aparece en 6 clases.*

- Un `with` abre un archivo y garantiza que se cierre al terminar. Procedencia es de dónde vienen los datos, quién los publicó y cuándo.
- Un registro de ejecución guarda entradas, entorno y resultado. Procedencia es el origen y la historia de los datos.
- La procedencia (*provenance*) es el registro de cómo se obtuvo un resultado: entradas, parámetros, versiones y salida.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C08](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md):**
- Un CSV sin procedencia no es un dato científico.
- Ejercicio 12 · integrador. Entrega un informe de lectura: función que lea un CSV propio (de al menos 5 filas y 4 columnas) con encabezados y unidades, validaciones con `assert`, un caso defectuoso reportado con número de línea, y una nota de procedencia con fecha y fuente.
- 🎯 **Por qué importa:** Un archivo CSV parece trivial y por eso engaña: todo se lee como texto, un decimal con coma rompe una columna, una línea vacía pasa inadvertida, y una codificación equivocada convierte «Júpiter» en símbolos raros. Un análisis hecho sobre datos mal leídos puede ser plausible y erróneo a la vez.

📘 **Dónde se aprende:** [B07-C08 · Lectura de archivos CSV](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md); [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md); [B08-C17 · Registro sistemático en bitácora](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md); [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md); [B74-C22 · Informe de navegación verificable](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md); [B124-C14 · Ciencia abierta y reproducibilidad](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md).

### Proceso de Poisson

*Aparece en 6 clases.*

- Un proceso de Poisson es la descripción conjunta: eventos independientes, tasa constante y sin eventos simultáneos.
- Distribución exponencial: duración sin memoria. Proceso de Poisson: llegada aleatoria de cortes.
- Un proceso de Poisson modela llegadas independientes.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C03](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md):**
- *Descripción textual:* según el mecanismo, la variable se modela con cuatro familias; la binomial con muchos ensayos y probabilidad pequeña tiende a la de Poisson; la espera entre los eventos de un proceso de Poisson es exponencial; el ruido que acumula muchos efectos pequeños tiende a la normal (C06).
- 🎯 **Por qué importa:** Cada vez que un detector cuenta fotones, una nave registra impactos o un instrumento mide con ruido, el patrón de la incertidumbre se parece a uno de unos pocos moldes. Reconocer el molde permite calcular probabilidades sin construir todo desde cero y entender qué supuesto físico lo respalda.

📘 **Dónde se aprende:** [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md); [B42-C21 · Estrellas guía naturales y cobertura de cielo](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md); [B48-C07 · Seguridad en instalaciones remotas](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md); [B58-C20 · Simulador de riesgo de impacto basado en datos](../programa/clases/B58/B58-C20-simulador-de-riesgo-de-impacto-basado-en-datos/CLASE.md); [B104-C20 · Misión tripulada simulada](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md); [B105-C14 · Atención de urgencia remota](../programa/clases/B105/B105-C14-atencion-de-urgencia-remota/CLASE.md).

### Profundidad

*Aparece en 10 clases.*

- El tránsito es la disminución de brillo cuando un cuerpo pasa por delante de su estrella; su profundidad es la fracción de flujo que se pierde.
- La profundidad es la caída relativa de flujo.
- La profundidad es `1 − F_en/F_fuera`.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C07](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md):**
- Estima la profundidad: `0,01006` frente a la verdadera 0,01.
- Paso final · incertidumbre. La profundidad estimada concuerda con la verdadera dentro de 6 × 10⁻⁵, pero una sola realización del ruido no dice cuánto varía esa estimación; para eso habría que repetir con varias semillas (B12).
- 🎯 **Por qué importa:** Una simulación o un instrumento moderno produce series de millones de muestras con sus metadatos. Guardarlas en texto es lento y pesado; cargarlas enteras en memoria para leer un fragmento es inviable.

📘 **Dónde se aprende:** [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md); [B28-C15 · Búsqueda de contrapartidas ópticas](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md); [B29-C01 · Tránsitos planetarios](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md); [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md); [B53-C17 · Mineralogía espectral](../programa/clases/B53/B53-C17-mineralogia-espectral/CLASE.md); [B53-C24 · Sondeo radar de penetración de hielo](../programa/clases/B53/B53-C24-sondeo-radar-de-penetracion-de-hielo/CLASE.md) y 4 más.

### Profundidad óptica

*Aparece en 13 clases.*

- La extinción es la pérdida de luz por absorción y dispersión en el camino; si es exponencial, `I = I₀ e^(−τ)` con `τ` la profundidad óptica.
- La profundidad óptica `τ` mide cuánta opacidad se atraviesa desde fuera: `τ = ∫ κ ρ dr`; con `τ = 1` la intensidad cae un factor `e`.
- La profundidad óptica `τ` es el exponente de atenuación `F = F₀ e^{−τ}`.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C09](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md):**
- *Descripción textual:* la temperatura crece con la profundidad óptica; la luz que llega al observador proviene sobre todo de `τ ≈ 2/3`, donde `T = T_ef`.
- En el modelo gris, la luz que vemos sale de la capa de profundidad óptica `τ ≈ 2/3`, a `5772 K`; la capa más externa (`τ = 0`) está a `4854 K`, y a `τ = 10` la temperatura es `9707 K`.
- 🎯 **Por qué importa:** Toda temperatura o composición que atribuimos a una estrella se infiere de una capa delgada. Saber de qué profundidad viene la luz, cuánto vale la opacidad y cuánto puede brillar una estrella sin expulsar su atmósfera es lo que permite interpretar espectros (C10) y entender los vientos (C17).

📘 **Dónde se aprende:** [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B24-C09 · Atmósferas y opacidades](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md); [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md); [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B32-C01 · Ecuación de transferencia radiativa en atmósferas estelares](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md); [B32-C05 · Relación T-τ y estructura térmica de la fotosfera](../programa/clases/B32/B32-C05-relacion-t-y-estructura-termica-de-la-fotosfera/CLASE.md) y 7 más.

### PSF

*Aparece en 6 clases.*

- La PSF (*point spread function*) es la imagen que el sistema da de una fuente puntual; en el modelo, la respuesta impulsional bidimensional de C08.
- La PSF es la respuesta del instrumento a una fuente puntual.
- La PSF es la respuesta a una fuente puntual.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- Con PSF gaussiana: `FWHM = 2,355 σ` y pico normalizado `1/(2πσ²)`.
- donde `⋆` es la correlación con la PSF (convolución con la PSF volteada).
- ⚠️ **Error frecuente:** Usar una PSF que no corresponde al instrumento y al campo. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.

📘 **Dónde se aprende:** [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md); [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md); [B45-C24 · Fotometría por ajuste de PSF](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md); [B74-C02 · Observación angular y astrometría](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md); [B74-C25 · Detección de limbo y bordes planetarios en imágenes de navegación](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md).

### Punto de equilibrio

*Aparece en 8 clases.*

- El punto de equilibrio es el tamaño o la intensidad a partir de la cual compensa.
- El punto de equilibrio es `N* = M_planta/M_pieza`.
- El punto de equilibrio es `t_eq = M_eq/(D η − repuestos)`.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- Paso final · incertidumbre. Los parámetros del modelo son inventados: con valores reales, el equilibrio será otro; la ganancia y el punto de equilibrio dependen del hardware, de los costes de lanzamiento y de la memoria.
- Plantear un modelo de tiempo con transferencia y calcular el punto de equilibrio.
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?

📘 **Dónde se aprende:** [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md); [B84-C38 · Producción de piezas y repuestos con materia prima in situ](../programa/clases/B84/B84-C38-produccion-de-piezas-y-repuestos-con-materia-prima-in-situ/CLASE.md); [B100-C07 · Dependencia de suministros terrestres y cierre de lazos logísticos](../programa/clases/B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md); [B106-C06 · Reciclaje de agua](../programa/clases/B106/B106-C06-reciclaje-de-agua/CLASE.md); [B124-C02 · Agencias científicas y empresas](../programa/clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md); [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md) y 2 más.

### Radio de Hill

*Aparece en 6 clases.*

- El radio de Hill `R_H` es el límite gravitatorio frente a la estrella.
- El radio de Hill de un planeta es `R_H = a_p (GM_p/(3GM_☉))^{1/3}`.
- El radio de Hill es `R_H = a_p (GM_p/(3GM_☉))^{1/3}`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B52-C08](../programa/clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md):**
- *Descripción textual:* el disco da la masa térmica y el radio de Bondi; con el de Hill se obtiene el radio de captura; los guijarros fijan el tiempo de crecimiento.
- Un núcleo de `10 M⊕` captura gas hasta su radio de Bondi (`8.87e+06 km`); uno de `100 M⊕`, hasta su radio de Hill (`3.47e+07 km`).
- 🎯 **Por qué importa:** El orden de magnitud de la masa del núcleo y el tiempo en alcanzarlo deciden si hay gigantes gaseosos. La decisión central: ¿a qué masa un núcleo pasa de capturar gas hasta Bondi a capturarlo hasta Hill, y cuánto tarda en crecer?

📘 **Dónde se aprende:** [B52-C08 · Formación de gigantes gaseosos](../programa/clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md); [B73-C18 · Satélites irregulares](../programa/clases/B73/B73-C18-satelites-irregulares/CLASE.md); [B73-C19 · Mecánica de sistemas lunares](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md); [B75-C16 · Navegación relativa a lunas](../programa/clases/B75/B75-C16-navegacion-relativa-a-lunas/CLASE.md); [B76-C01 · Sistema Tierra-Luna](../programa/clases/B76/B76-C01-sistema-tierra-luna/CLASE.md); [B76-C03 · Órbitas alrededor de la Luna](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md).

### Rango

*Aparece en 7 clases.*

- Un rango es el intervalo de valores mostrado.
- Una función `f` asigna a cada valor `x` de un conjunto (el dominio) un único valor `f(x)`; el conjunto de los resultados es el rango.
- El rango de un conjunto de vectores es la dimensión de su espacio generado; la nulidad es el número de relaciones de dependencia independientes.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C15](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md):**
- Elige el rango para incluir todos los datos y dejar un margen.
- Un gráfico honesto: ejes rotulados con unidad, rango y escala declarados, datos y fuente citados, y sin ocultar los puntos que no encajan.
- 🎯 **Por qué importa:** Las fichas de la NASA dan semiejes y períodos de los ocho planetas. En una tabla son 16 números.

📘 **Dónde se aprende:** [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md); [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md); [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md); [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md); [B67-C05 · Modelos geoestadísticos de distribución de volátiles](../programa/clases/B67/B67-C05-modelos-geoestadisticos-de-distribucion-de-volatiles/CLASE.md) y 1 más.

### Recuperación

*Aparece en 8 clases.*

- La recuperación `r` es la fracción de la alimentación que sale como destilado.
- La recuperación es el retorno de una función a su valor previo.
- La recuperación `r` es la fracción de la carga que se disipa cada día.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B54-C18](../programa/clases/B54/B54-C18-medicion-remota-atmosferica/CLASE.md):**
- Interpretar la dispersión de la recuperación con ruido.
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué repetir cinco veces la recuperación?
- 🎯 **Por qué importa:** Cada canal 've' una capa distinta según su absorción. La pregunta motivadora: ¿a qué altura 'mira' cada canal y cómo se recupera la altura de escala con ruido?

📘 **Dónde se aprende:** [B54-C18 · Medición remota atmosférica](../programa/clases/B54/B54-C18-medicion-remota-atmosferica/CLASE.md); [B59-C07 · Purificación de agua](../programa/clases/B59/B59-C07-purificacion-de-agua/CLASE.md); [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md); [B90-C02 · Buenas prácticas de sala limpia](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md); [B107-C06 · Estimación y modelado de la recuperación posterior al vuelo](../programa/clases/B107/B107-C06-estimacion-y-modelado-de-la-recuperacion-posterior-al-vuelo/CLASE.md); [B113-C01 · Estrés operacional y estrategias de afrontamiento](../programa/clases/B113/B113-C01-estres-operacional-y-estrategias-de-afrontamiento/CLASE.md) y 2 más.

### Redundancia

*Aparece en 8 clases.*

- La carga visual es el número de elementos que compiten por la atención a la vez. Redundancia: transmitir un estado por más de un canal (color y texto).
- La redundancia es el número de observadores que ven a la vez.
- La redundancia (respaldo frío, `k` de `n`).
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C09](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md):**
- Porque la causa común anula la redundancia.
- Ejercicio 12. Integrador. Elabora tu *ficha de la continuidad*: redundancia, causa común y disponibilidad.
- 🎯 **Por qué importa:** Una unidad adicional mejora menos que la anterior y las fallas comunes limitan la ganancia. La decisión central: ¿cuántas unidades de respaldo valen la pena?

📖 **Explicado a fondo:** [Redundancia y fiabilidad](esencial/ampliacion-n-z.md#redundancia-y-fiabilidad).

📘 **Dónde se aprende:** [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B47-C19 · Mantenimiento y vida útil](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B101-C02 · Cinemática inversa y redundancia de manipuladores](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md); [B116-C07 · Diseño de paneles de monitoreo de salud](../programa/clases/B116/B116-C07-diseno-de-paneles-de-monitoreo-de-salud/CLASE.md); [B118-C11 · Diseño para mitigación de desechos](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md) y 2 más.

### Registro

*Aparece en 9 clases.*

- Un registro es una observación anotada con fecha.
- Un registro describe un archivo (instrumento, tiempo, banda).
- Un registro es un evento de un mensajero.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C02](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md):**
- A["Registro largo<br/>de eclipses"] --> B["Regularidad:<br/>intervalo ≈ 6 585 d"]
- *Descripción textual:* de un registro largo de eclipses sale una regularidad (un intervalo de unos 6 585 días); de ella pueden surgir una explicación por casi-igualdad de tres períodos lunares y un uso predictivo con incertidumbre.
- 🎯 **Por qué importa:** Una predicción necesita una larga memoria. Para decir que un fenómeno volverá, alguien tuvo que anotarlo muchas veces y compararlo.

📘 **Dónde se aprende:** [B02-C02 · Observación mesopotámica y egipcia](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md); [B08-C17 · Registro sistemático en bitácora](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md); [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md); [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md); [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md); [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md) y 3 más.

### Relación señal/ruido

*Aparece en 8 clases.*

- La relación señal–ruido (SNR) de una medida es su valor dividido por su incertidumbre.
- La relación señal/ruido (SNR) es señal dividida entre la desviación del ruido.
- La relación señal/ruido (`SNR`) es la señal media dividida por la desviación estándar del ruido.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- Calcular la relación señal–ruido de una fuente de flujo conocido.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.

📘 **Dónde se aprende:** [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B29-C20 · Proyecto de detección exoplanetaria](../programa/clases/B29/B29-C20-proyecto-de-deteccion-exoplanetaria/CLASE.md); [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md); [B48-C18 · Protección del cielo oscuro](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md); [B56-C14 · Biofirmas espectrales](../programa/clases/B56/B56-C14-biofirmas-espectrales/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md) y 2 más.

### Rendimiento

*Aparece en 9 clases.*

- El rendimiento `y` es la masa de metales producida y liberada por cada unidad de masa que queda en estrellas.
- El rendimiento es el número de fotones por unidad de longitud.
- El rendimiento es la fracción de sistemas que cumple.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B25-C17](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md):**
- Paso 5 · Sentido. Con ese rendimiento ilustrativo, una caja cerrada que ha convertido el `70 %` de su gas en estrellas alcanza casi el valor solar; con salida de gas `λ = 1` sería la mitad.
- El ejemplo conductor es una galaxia sintética de caja cerrada con rendimiento efectivo `y = 0,010` (ilustrativo) y gas restante `μ = 0,3`.
- 🎯 **Por qué importa:** Cada generación de estrellas fabrica elementos pesados y los devuelve al gas; la proporción de metales de una galaxia cuenta cuánto se ha procesado su gas. En astronomía, «metales» son todos los elementos más pesados que el helio.

📘 **Dónde se aprende:** [B25-C17 · Metalicidad y evolución química](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md); [B31-C14 · Detectores de partículas](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md); [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md); [B50-C13 · Análisis Monte Carlo de tolerancias ópticas](../programa/clases/B50/B50-C13-analisis-monte-carlo-de-tolerancias-opticas/CLASE.md); [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md); [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md) y 3 más.

### Reproducibilidad

*Aparece en 7 clases.*

- La reproducibilidad es la posibilidad de que otra persona repita tu procedimiento y obtenga un resultado compatible.
- La reproducibilidad es la posibilidad de que otra persona repita tu observación o tu cálculo con tus registros.
- Una prueba de regresión vuelve a ejecutar un caso conocido y exige el mismo resultado. Reproducibilidad es obtener el mismo resultado con los mismos datos y código;
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C26](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md):**
- Paso 5 · Reproducibilidad. Ambos pasaron la repetición exacta.
- Verificar la reproducibilidad del benchmark.
- 🎯 **Por qué importa:** «El método A es mejor que el B» es una afirmación vacía sin el problema, la métrica, la tolerancia y el costo. Una comparación mal diseñada lleva a elegir el algoritmo equivocado para una misión.

📘 **Dónde se aprende:** [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md); [B08-C17 · Registro sistemático en bitácora](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md); [B11-C20 · Propagador reproducible de trayectoria](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md); [B11-C26 · Benchmark de algoritmos numéricos](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md); [B12-C23 · Diagnóstico de convergencia y reproducibilidad de cadenas MCMC](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md); [B74-C22 · Informe de navegación verificable](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md) y 1 más.

### Requisito

*Aparece en 13 clases.*

- Un requisito es una condición que la solución debe cumplir.
- Un requisito es una condición que la campaña debe cumplir; debe ser verificable: tener un criterio de comprobación (un número o un sí/no) y un método de comprobación.
- Un requisito es una condición medible que la cadena debe cumplir.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C20](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md):**
- Con R1, la Tierra mide 0,85 mm: el requisito de ver los planetas (si se pidiera que fuesen visibles, por ejemplo, de 1 cm) choca con R2.
- R["Requisitos: 1 au = 10 m; cabe en 350 m; misma escala para todo"] --> E["Factor de escala E = 1 au / 10 m"]
- ⚠️ **Error frecuente:** No declarar el conflicto de requisitos. Ejercicio 6.
- 🎯 **Por qué importa:** Un ingeniero no recibe un ejercicio con una sola fórmula: recibe requisitos («que quepa en un patio de 350 m», «que se vea el Sol», «que Neptuno esté a su sitio») y debe decidir qué se puede cumplir y qué no.

📘 **Dónde se aprende:** [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md); [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md) y 7 más.

### Residuo

*Aparece en 23 clases.*

- Un residuo es la diferencia entre el dato y la predicción.
- Un residuo es la diferencia entre un dato y el valor de la recta.
- El residuo es `y − A x`.
- *(y 19 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- El residuo cuadrático medio de los logaritmos es 0,0051.
- Que Neptuno tenga el mayor residuo no desprestigia al modelo: puede deberse a la magnitud tabulada (C13), y lo correcto es investigarlo.
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?

📘 **Dónde se aprende:** [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B03-C16 · Pendiente e interpretación de gráficos](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md); [B10-C07 · Proyecciones y mínimos cuadrados](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md); [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md); [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md); [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md) y 17 más.

### Restricción

*Aparece en 6 clases.*

- Una restricción es una condición que liga las variables (por ejemplo, un volumen fijo).
- Un ciclo V baja de la malla fina a la más gruesa y vuelve a subir. Restricción es pasar un campo a la malla gruesa;
- Una restricción limita el espacio de soluciones.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C07](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md):**
- Paso 1 · Objetivo y restricción. Minimizar `A = 2πr² + 2πrL` con `π r² L = 10`.
- Sentido: el cilindro óptimo es «tan alto como ancho»; un tanque real tiene casquetes esféricos y otras restricciones.
- ⚠️ **Error frecuente:** Optimizar con dos variables sin usar la restricción. Se corrige en el paso 2 del ejemplo trabajado.
- 🎯 **Por qué importa:** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.

📘 **Dónde se aprende:** [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md); [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md); [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md); [B50-C02 · Optimización de superficies: función de mérito y restricciones](../programa/clases/B50/B50-C02-optimizacion-de-superficies-funcion-de-merito-y-restricciones/CLASE.md); [B83-C12 · Model-Based Systems Engineering](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md).

### Retardo

*Aparece en 15 clases.*

- La autocorrelación `r_k` mide cuánto se parece la serie a sí misma desplazada `k` muestras; el número `k` es el retardo (en inglés *lag*).
- El retardo es cuánto desplaza el filtro la señal en el tiempo.
- Un retardo de `d` muestras de periodo `T` es una demora `d·T` entre medir y actuar.
- *(y 10 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C01](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md):**
- Con la media `x̄`, la autocorrelación muestral al retardo `k` es
- Calcular la autocorrelación a un retardo dado y leer qué periodicidad sugiere.
- 🎯 **Por qué importa:** Un telescopio espacial mide el brillo de una estrella cada dos minutos durante semanas. Lo que llega a tierra no es una curva continua, sino una tabla de números.

📘 **Dónde se aprende:** [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md); [B15-C21 · Series temporales multivariadas y regresión dinámica](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md); [B16-C07 · Realimentación y estabilidad](../programa/clases/B16/B16-C07-realimentacion-y-estabilidad/CLASE.md); [B27-C20 · Análisis multibanda de un evento extremo](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md); [B34-C09 · Integración multiinstrumento de datos heliofísicos](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md) y 9 más.

### Retrógrada

*Aparece en 6 clases.*

- Una órbita es directa si `i < 90°` y retrógrada si `i > 90°`.
- Prógrada es `i < 90°`; retrógrada, `i > 90°`.
- Una transferencia es prógrada si `n` apunta hacia el eje de referencia `+z` (`h_z > 0`) y retrógrada si apunta hacia `−z`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- La componente `z` es `cos i`: positiva si `i < 90°` (directa) y negativa si `i > 90°` (retrógrada).
- E -->|"< 0"| G["Órbita retrógrada (i > 90°)"]
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?

📘 **Dónde se aprende:** [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md); [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md); [B52-C11 · Formación de satélites naturales](../programa/clases/B52/B52-C11-formacion-de-satelites-naturales/CLASE.md); [B71-C11 · Inclinación y nodo ascendente](../programa/clases/B71/B71-C11-inclinacion-y-nodo-ascendente/CLASE.md); [B76-C03 · Órbitas alrededor de la Luna](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md); [B82-C02 · Lambert de arco largo](../programa/clases/B82/B82-C02-lambert-de-arco-largo/CLASE.md).

### Riesgo

*Aparece en 7 clases.*

- Un riesgo es un evento posible con consecuencia; se acompaña de una mitigación.
- Un riesgo es un escenario con verosimilitud (L, 1–5) y consecuencia (C, 1–5).
- Un peligro es una fuente de daño; el riesgo combina severidad y verosimilitud.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C20](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md):**
- Riesgos: sol y calor de día, frío y oscuridad de noche, caídas en terreno, vehículos, equipo volcado, fatiga al regresar, pérdida de adaptación a la oscuridad por luces; cada uno con su mitigación.
- 🎯 **Por qué importa:** Una salida sin plan termina en una noche perdida o en un accidente. La pregunta motivadora: ¿cómo preparo una salida de observación para que sea segura, útil, accesible y reproducible?

📘 **Dónde se aprende:** [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B83-C16 · Gestión de riesgos técnicos](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md); [B83-C21 · Identificación de peligros en sistemas de lanzamiento (HAZID)](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md); [B110-C02 · Protocolos operativos de aislamiento de un tripulante enfermo o contaminado](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md); [B114-C06 · Matriz de riesgo ambiental de un hábitat](../programa/clases/B114/B114-C06-matriz-de-riesgo-ambiental-de-un-habitat/CLASE.md); [B120-C05 · Riesgos de incumplimiento regulatorio](../programa/clases/B120/B120-C05-riesgos-de-incumplimiento-regulatorio/CLASE.md) y 1 más.

### RK4

*Aparece en 6 clases.*

- La temperatura límite es `T_a − Q/G`. RK4 es un integrador de cuarto orden.
- El baricentro es el centro de masas del par. RK4 es el método de Runge–Kutta de cuarto orden.
- Euler explícito es de orden 1. RK4 es de orden 4.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B44-C08](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md):**
- Con paso de `0,5 s`, el error máximo de Euler es `0,01380 K` y el de RK4 `4,8 × 10⁻¹³ K`.
- Ejercicio 7. Error de Euler frente a RK4.
- 🎯 **Por qué importa:** La cámara no está fría al encenderla. La decisión central: ¿cuánto hay que esperar antes de calibrar y qué temperatura final se alcanza?

📘 **Dónde se aprende:** [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md); [B71-C03 · Ecuación de movimiento de dos cuerpos](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md); [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md); [B85-C26 · Análisis térmico transitorio y casos extremos](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md); [B97-C23 · Diseño de simulador de misión robótica](../programa/clases/B97/B97-C23-diseno-de-simulador-de-mision-robotica/CLASE.md); [B101-C06 · Simulación de un brazo robótico espacial](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md).

### RMS

*Aparece en 6 clases.*

- El RMS mide la calidad.
- El sesgo es el residuo medio; el RMS, su raíz cuadrática media.
- El RMS mide la energía de la señal.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C22](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md):**
- La diferencia punto a punto entre ambos restos tiene `1,011 nm` RMS (ruido inyectado de 0,02 rad, equivalente a `0,02 λ/(4π) = 1,01 nm` por píxel).
- La superficie tiene `14,8` franjas en total; tras ajustar piston, inclinaciones y desenfoque queda un resto de `97,3 nm` PV y `19,90 nm` RMS (`0,0314 λ`).
- 🎯 **Por qué importa:** El mapa de error de forma es la prueba de aceptación de un espejo. La decisión central: ¿cómo se recupera la fase, qué se descuenta y qué PV y RMS quedan?

📘 **Dónde se aprende:** [B43-C22 · Interferometría de superficie y mapas de error de forma](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md); [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md); [B47-C10 · Estabilidad de apuntamiento](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md); [B85-C14 · Degradación ultravioleta](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md); [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md); [B97-C26 · Monitoreo de condición de maquinaria extraterrestre](../programa/clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md).

### Ruido

*Aparece en 9 clases.*

- El ruido es una perturbación aleatoria de las muestras.
- El ruido es la parte de la serie que no se explica con el modelo.
- El fondo (*background*) es el nivel del cielo sin fuentes; el ruido `σ` su desviación.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C11](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md):**
- Si cada muestra tiene ruido independiente de desviación `σ` y paso `Δt`, el error en la integral crece como `σ Δt √N` (no como `N`).
- La elección del método importa más que añadir ruido o decimales.
- ⚠️ **Error frecuente:** Esperar que más puntos eliminen el ruido. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.

📘 **Dónde se aprende:** [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B22-C01 · Problemas directos e inversos y mal condicionamiento](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md); [B42-C16 · Lazo de control de óptica adaptativa](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md) y 3 más.

### Ruido de lectura

*Aparece en 6 clases.*

- El ruido de lectura viene de la electrónica; el ruido de Poisson (de fotones), de la naturaleza discreta de la luz: su varianza es igual a la señal en electrones.
- El ruido de lectura es constante por pixel.
- El ruido de lectura es la parte aleatoria de cada lectura.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- La varianza de un píxel de cielo es: lectura `σ_L²` + fotones (`cielo + oscuro`) + el ruido del oscuro maestro, que vale `(σ_L² + oscuro)/K` si se promedian `K` oscuros.
- Ejercicio 4. En un píxel de cielo de 50 e⁻ con lectura 5 ADU, ¿domina el ruido de lectura o el de fotones?
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.

📘 **Dónde se aprende:** [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B29-C02 · Curvas de luz fotométricas](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md); [B44-C06 · Ruido de lectura](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md); [B47-C15 · Calibración a bordo](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md); [B48-C13 · Calibraciones nocturnas](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md).

### Saturación

*Aparece en 19 clases.*

- La saturación es el nivel máximo de actividad que se alcanza cuando `Ro` es pequeño.
- La saturación: el centro de la línea ya es negro.
- La saturación es la pérdida de sensibilidad del índice cuando la vegetación es densa.
- *(y 15 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C18](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md):**
- Sin anti-windup, `ξ̇ = e` todo el tiempo, también durante la saturación.
- `K_aw` es un parámetro de diseño: muy pequeño no corrige, muy grande puede inducir un comportamiento brusco al entrar y salir de saturación.
- 🎯 **Por qué importa:** Una rueda de reacción entrega un par máximo y almacena un momento angular máximo (el Hubble usa ruedas de hasta unas 3000 rpm, y magnetopares para gestionar su velocidad, S1). Cuando el controlador pide más de lo que el actuador puede dar, el lazo deja de comportarse como se diseñó.

📘 **Dónde se aprende:** [B16-C18 · Saturación y anti-windup](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md); [B24-C11 · Rotación y campos magnéticos](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md); [B34-C05 · Diagnóstico de densidad electrónica coronal](../programa/clases/B34/B34-C05-diagnostico-de-densidad-electronica-coronal/CLASE.md); [B44-C05 · Pozo lleno y rango dinámico](../programa/clases/B44/B44-C05-pozo-lleno-y-rango-dinamico/CLASE.md); [B45-C11 · Líneas de absorción](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md); [B57-C06 · Índices de vegetación](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md) y 13 más.

### Sección eficaz

*Aparece en 8 clases.*

- La sección eficaz mide la probabilidad de interacción.
- La sección eficaz mide cuánta señal devuelve el objeto.
- La sección eficaz `σ` (m² o cm²) es el área efectiva de colisión.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B27-C18](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md):**
- *Descripción textual:* de la energía y la energía media se obtiene el número de neutrinos y su fluencia; con la sección eficaz y los protones del detector, los sucesos; el retraso por masa se calcula con una forma algebraica estable.
- Con `2,5 × 10⁴⁶ J` en neutrinos de `10 MeV` en promedio (ilustrativos) a `10 kpc`, la fluencia por sabor es `2,17 × 10¹¹ cm⁻²` y un kilotón de agua daría `145,4` sucesos con una sección eficaz de `10⁻⁴¹ cm²` (ilustrativa).
- 🎯 **Por qué importa:** Los neutrinos de una supernova galáctica serían una señal de cientos de sucesos en unos segundos, mensajera del interior de la estrella. La decisión central: ¿cuántos neutrinos llegan, qué retraso produce su masa y cómo se calcula sin perder precisión?

📘 **Dónde se aprende:** [B27-C18 · Neutrinos de supernova](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md); [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md); [B58-C12 · Radar planetario](../programa/clases/B58/B58-C12-radar-planetario/CLASE.md); [B60-C01 · Colisiones moleculares y secciones eficaces en gas interestelar](../programa/clases/B60/B60-C01-colisiones-moleculares-y-secciones-eficaces-en-gas-interestelar/CLASE.md); [B88-C03 · Procesadores tolerantes a radiación](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md) y 2 más.

### Segundo de arco

*Aparece en 6 clases.*

- Un segundo de arco es 1/3 600 de grado.
- El grado (°) es `π/180` rad; el minuto de arco (′) es `1/60` de grado y el segundo de arco (″) es `1/60` de minuto de arco, es decir, `π/648 000` rad (S2).
- Un segundo de arco es `1/3600` de grado: `1″ = π/648 000 rad = 4,848 × 10⁻⁶ rad` (S3).
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C10](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md):**
- Para una estrella a `d` parsecs, el paralaje en segundos de arco es `p = 1/d`.
- Ejercicio 4. Convierte 2′ en segundos de arco y en grados.
- 🎯 **Por qué importa:** La pregunta «¿se mueve la Tierra o el cielo?» se puede responder hoy en una línea, pero en 1500 una persona razonable podía defender cualquiera de las dos. La pregunta motivadora es: ¿con qué criterios se elige entre dos modelos que predicen casi lo mismo?

📘 **Dónde se aprende:** [B02-C10 · Geocentrismo y heliocentrismo](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md); [B03-C08 · Tiempo y conversiones astronómicas](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md); [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md); [B04-C01 · Polinomios y factorización](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md); [B04-C06 · Identidades trigonométricas](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md); [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md).

### Semieje mayor

*Aparece en 9 clases.*

- El semieje mayor `a` es la mitad del eje largo de una órbita elíptica; si la órbita es casi circular, es casi su radio.
- El semieje mayor `a` es la mitad del diámetro mayor de la elipse.
- El semieje mayor `a` es la mitad de la dimensión mayor; el semieje menor `b`, la mitad de la menor.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C13](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md):**
- La ficha no rotula esa fila como semieje mayor, así que no sabemos si es el mismo número; el ejemplo enseña a comprobar qué magnitud mide una tabla antes de usarla.
- Límite: las cifras de la ficha tienen tres o cuatro cifras, y la distancia que tabula no se rotula como semieje mayor; eso importa en la sección 8.4.
- 🎯 **Por qué importa:** Se dice que el sistema solar «está vacío», y es verdad en un sentido preciso: si el Sol midiera 9 mm, la Tierra sería un grano de 0,085 mm a un metro de distancia, y la estrella más cercana quedaría a más de 260 km. Pero esa imagen solo se entiende si la construyes tú con números.

📘 **Dónde se aprende:** [B01-C13 · Sistema solar como sistema físico](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md); [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B05-C20 · Problema físico integrado de satélite ideal](../programa/clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md); [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md) y 3 más.

### Semilado recto

*Aparece en 6 clases.*

- El semilado recto `p = a(1 − e²)` es la distancia al foco medida en perpendicular al eje mayor.
- El semilado recto `p = a(1 − e²)` es el valor de `r` en `θ = 90°`.
- La ecuación polar común con el foco en el origen y `θ` desde el punto más cercano (periastro) es `r = p/(1 + e cos θ)`, con `p` el semilado recto; la distancia mínima es `q = p/(1 + e)`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C10](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md):**
- Paso 1 · Semilado recto. `p = a(1 − e²) = 17,9286 × 0,063093 = 1,1312 au`.
- 🎯 **Por qué importa:** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.

📘 **Dónde se aprende:** [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md); [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B27-C09 · Órbitas en campos fuertes](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md); [B71-C06 · Momento angular específico](../programa/clases/B71/B71-C06-momento-angular-especifico/CLASE.md); [B71-C08 · Órbitas elípticas](../programa/clases/B71/B71-C08-orbitas-elipticas/CLASE.md).

### Sensibilidad

*Aparece en 42 clases.*

- La sensibilidad es la luz mínima que detecta.
- La sensibilidad mide cuánto cambia el objetivo al desviarse del óptimo.
- La sensibilidad describe cuánto se amplifica una diferencia inicial.
- *(y 38 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C07](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md):**
- D --> E["Comprobar el resultado<br/>y su sensibilidad"]
- Evaluar la sensibilidad de un diseño a desviarse del óptimo.
- ⚠️ **Error frecuente:** Exagerar la precisión del óptimo. Se corrige con la sensibilidad (sección 8.5) y el ejercicio 7.
- 🎯 **Por qué importa:** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.

📘 **Dónde se aprende:** [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md); [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md); [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md); [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md); [B16-C07 · Realimentación y estabilidad](../programa/clases/B16/B16-C07-realimentacion-y-estabilidad/CLASE.md); [B27-C19 · Observatorios de rayos X y gamma](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md) y 36 más.

### Sesgo

*Aparece en 21 clases.*

- El sesgo es un error constante de un instrumento.
- El sesgo (*bias*) de un giróscopo es un error sistemático constante en `ω`.
- El sesgo de una medida es `E[error]`; el error cuadrático medio es `E[error²] = Var + sesgo²`.
- *(y 15 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C08](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md):**
- En navegación real se combinan con otras medidas para acotar el sesgo.
- Un pequeño sesgo (error constante) crece: con un sesgo de `10⁻³ m/s²` durante 100 s la velocidad se desvía `0,100 m/s` y la posición, `5,00 m`.
- 🎯 **Por qué importa:** Un acelerómetro mide aceleración; lo que se necesita es velocidad y posición. Una gravedad `g(r)` se conoce; lo que decide si una sonda escapa es la energía, que sale de «deshacer» esa derivada.

📘 **Dónde se aprende:** [B09-C08 · Integrales indefinidas](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md); [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md); [B12-C04 · Esperanza y varianza](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md); [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md); [B13-C03 · Exactitud frente a precisión](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md); [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md) y 15 más.

### SHA-256

*Aparece en 6 clases.*

- Una huella (*hash*) es un número de longitud fija calculado a partir del contenido de un archivo; si el contenido cambia, la huella cambia. SHA-256 es una función de huella de 256 bits.
- Un hash (huella) es una función que resume un contenido; SHA-256 produce 256 bits, que se escriben como 64 caracteres hexadecimales.
- Un manifiesto lista cada archivo con su huella. SHA-256 es una función hash de 256 bits.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Por ejemplo: `"""Devuelve la huella SHA-256 (hexadecimal) del contenido de un archivo."""`.
- D["datos<br/>+ huella SHA-256"] --> E["ejecución"]
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.

📘 **Dónde se aprende:** [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md); [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B48-C17 · Gestión de archivos observacionales](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md); [B90-C18 · Trazabilidad de evidencias](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md); [B96-C22 · Transferencia de datos entre estación y centro de datos](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md); [B130-C06 · Publicación de un proyecto educativo](../programa/clases/B130/B130-C06-publicacion-de-un-proyecto-educativo/CLASE.md).

### Sobreimpulso

*Aparece en 8 clases.*

- El sobreimpulso `Mp` es cuánto excede la respuesta a su valor final (en fracción), el tiempo de pico `tp` es cuándo ocurre, el tiempo de subida `tr` es el que tarda entre 10 % y 90 % del valor final y el tiempo de asentamiento `ts` es el que tarda en quedar dentro de ±2 % para siempre.
- El sobreimpulso es `exp(−πζ/√(1−ζ²))`.
- El sobreimpulso es el máximo exceso sobre la consigna.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C04](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md):**
- No hay sobreimpulso: la curva se acerca sin pasarse.
- Derivando `y(t)` y buscando el primer máximo se obtiene el tiempo de pico `tp = π/ωd` y el sobreimpulso `Mp = exp(−π ζ/√(1 − ζ²))`; solo dependen de `ζ`.
- 🎯 **Por qué importa:** Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación.

📘 **Dónde se aprende:** [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B43-C15 · Motores paso a paso y servomotores](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md); [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md); [B85-C10 · Control térmico activo](../programa/clases/B85/B85-C10-control-termico-activo/CLASE.md); [B88-C19 · Simulación hardware-in-the-loop](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md); [B97-C24 · Modelos de actuadores virtuales e integración en simulación](../programa/clases/B97/B97-C24-modelos-de-actuadores-virtuales-e-integracion-en-simulacion/CLASE.md) y 2 más.

### Supresión

*Aparece en 6 clases.*

- La supresión es el cociente entre `D(1)` en ΛCDM y `a` (en EdS vale 1).
- La supresión descarta el evento y cuenta cuántos.
- Una alarma dependiente se deriva de una causa raíz ya activa; la supresión la oculta para no saturar.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- Calcular la supresión del crecimiento por la constante cosmológica.
- Ejercicio 12 · integrador. Elabora tu *curva de crecimiento*: resuelve el crecimiento por ODE e integral para dos `Ω_m`, la supresión, el `D_C` y el ángulo de la regla BAO a `z = 0,35` en dos modelos.
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.

📘 **Dónde se aprende:** [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md); [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md); [B88-C10 · Gestión de eventos](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md); [B98-C04 · Interfaces humano-robot para operación remota](../programa/clases/B98/B98-C04-interfaces-humano-robot-para-operacion-remota/CLASE.md); [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md); [B129-C05 · Consentimiento y privacidad de participantes](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md).

### Tasa

*Aparece en 9 clases.*

- Una tasa es un cociente de magnitudes de clases distintas (km/s).
- Una falsa alarma es una detección que no corresponde a ninguna fuente; su tasa es la fracción de píxeles (o el número por imagen) que superan el umbral solo por ruido.
- La tasa `R` es el número de fusiones por volumen y año.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C02](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md):**
- Distinguir una razón (adimensional) de una tasa (con unidades, como km/s).
- 🎯 **Por qué importa:** Una cifra aislada como «69 911 km» no dice si Júpiter es grande o pequeño. Una razón sí: Júpiter tiene un radio unas 11 veces el terrestre.

📘 **Dónde se aprende:** [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md); [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md); [B28-C11 · Coincidencias entre observatorios](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md); [B51-C11 · Búsqueda de franjas VLBI: ajuste de retardo y tasa](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md); [B105-C10 · Respuesta inmune](../programa/clases/B105/B105-C10-respuesta-inmune/CLASE.md) y 3 más.

### Temperatura de equilibrio

*Aparece en 11 clases.*

- La temperatura de equilibrio es la que iguala potencia absorbida y emitida.
- La temperatura de equilibrio es aquella en que la potencia absorbida iguala a la radiada.
- La temperatura de equilibrio `T = [L(1−A)/(16πσd²)]^(1/4)` es la de un cuerpo esférico de rotación rápida.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C13](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md):**
- *Descripción textual:* la luz solar de potencia `S × área` es absorbida y aumenta la energía térmica; el cuerpo emite `σ A T⁴`; en el equilibrio, entrada y salida se igualan y eso fija la temperatura.
- Balance de energía da la temperatura de equilibrio con muy pocos datos.
- ⚠️ **Error frecuente:** Creer que más masa implica otra temperatura de equilibrio. Sección 13.
- 🎯 **Por qué importa:** Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: ¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?

📘 **Dónde se aprende:** [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md); [B13-C16 · Calibración térmica](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md); [B29-C13 · Zonas de habitabilidad](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md); [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md); [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md); [B52-C15 · Cinturón de Kuiper](../programa/clases/B52/B52-C15-cinturon-de-kuiper/CLASE.md) y 5 más.

### Tiempo de respuesta

*Aparece en 6 clases.*

- El tiempo de respuesta es `fin − llegada`.
- El tiempo de respuesta `R_i = C_i + Σ_j ⌈R_i/T_j⌉ C_j` (j de mayor prioridad) es exacto.
- El tiempo de respuesta es el que se tarda en detectar, decidir y actuar.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B88-C05](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md):**
- Con paso de 1 ms sobre 3 hiperperiodos (468 ms), el tiempo de respuesta máximo observado es 1, 3 y 10 ms: igual al analítico, con 0 plazos incumplidos.
- *Descripción textual:* de las tareas y sus prioridades sale el tiempo de respuesta por iteración; la simulación lo comprueba; ambos alimentan el veredicto.
- 🎯 **Por qué importa:** En una nave, una tarea de control que llega tarde puede ser tan mala como una que da un resultado incorrecto. La decisión central: ¿cada tarea termina siempre antes de su plazo, aun cuando las de mayor prioridad la interrumpen?

📘 **Dónde se aprende:** [B88-C05 · Sistemas de tiempo real](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md); [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md); [B96-C15 · Operaciones de emergencia](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md); [B96-C25 · Seguridad física y control de acceso de estaciones terrestres](../programa/clases/B96/B96-C25-seguridad-fisica-y-control-de-acceso-de-estaciones-terrestres/CLASE.md); [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md); [B104-C13 · Procedimientos de emergencia](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md).

### Tolerancia

*Aparece en 6 clases.*

- La tolerancia combina una parte relativa `rtol` y una absoluta `atol`: la escala de cada componente es `sc_i = atol + rtol |s_i|`.
- La tolerancia es la diferencia máxima que aceptas entre lo obtenido y lo esperado; se compone de una parte relativa `rtol` y una absoluta `atol`.
- La tolerancia `w` es el semiancho aceptado en frecuencia.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C08](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md):**
- La tolerancia controla el error local de cada paso.
- Para un error global dado hay que reducir la tolerancia y verificar con una referencia (C19).
- ⚠️ **Error frecuente:** Confundir tolerancia local con error global. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.

📘 **Dónde se aprende:** [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md); [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md); [B55-C10 · Identificación de moléculas orgánicas](../programa/clases/B55/B55-C10-identificacion-de-moleculas-organicas/CLASE.md); [B62-C08 · Mezclas moleculares y confusión de líneas](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md); [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md); [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### Transición

*Aparece en 6 clases.*

- Una transición es el salto de un electrón entre dos niveles.
- La transición es el paso de laminar a turbulento, convencionalmente en `Re_x ≈ 5 × 10⁵` en placa y `Re ≈ 2300` en tubo.
- Una transición es un cambio de modo.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Con `h c = 1239,84 eV·nm` (que sale de las constantes exactas del SI, S1), una transición de 1,89 eV corresponde a `λ = 1239,84/1,89 ≈ 656 nm`, justamente la línea H-alfa.
- Dato de partida: la transición 3→2 del hidrógeno, con constantes CODATA 2022 (S1).
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.

📘 **Dónde se aprende:** [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B46-C12 · Emisiones moleculares](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md); [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md); [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md); [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md); [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md).

### Traza

*Aparece en 9 clases.*

- Una traza es una tabla que anota el valor de las variables después de cada paso.
- La traza es la suma de la diagonal.
- La traza es la contracción `Tᵢᵢ` (S1: suma de la diagonal, §1.2(vi), ec. 1.2.62).
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C01](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md):**
- La traza para los datos de la sección 5 empieza con «mejor = Mercurio, 87,969».
- Una traza te permite descubrir errores de lógica sin que el computador intervenga.
- 🎯 **Por qué importa:** En astronomía casi todo resultado pasa por un procedimiento repetible: reducir imágenes, ajustar una órbita, buscar el máximo de una curva de luz. Si no puedes describir el procedimiento con precisión, no puedes ejecutarlo en un computador ni dárselo a otra persona para que lo repita.

📘 **Dónde se aprende:** [B07-C01 · Pensamiento algorítmico](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md); [B07-C12 · Manejo de errores y excepciones](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md); [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md); [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md); [B106-C21 · Depuración de trazas gaseosas de la atmósfera de cabina](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md) y 3 más.

### Trazabilidad

*Aparece en 10 clases.*

- La trazabilidad es la capacidad de seguir una afirmación hasta su origen.
- La trazabilidad es poder seguir cada requisito hasta su comprobación.
- La trazabilidad es la capacidad de reconstruir, para una cifra, los datos, el código, los parámetros y el entorno que la produjeron.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C19](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md):**
- Lo que decide es la trazabilidad, no el peldaño.
- 🎯 **Por qué importa:** Un titular dice: «Neutrinos superan la velocidad de la luz: Einstein estaba equivocado». Es una afirmación fuerte.

📘 **Dónde se aprende:** [B01-C19 · Fuentes confiables y desinformación espacial](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md); [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md); [B90-C18 · Trazabilidad de evidencias](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md); [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md) y 4 más.
