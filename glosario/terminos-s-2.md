# Términos · S (parte 2 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · **S** · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-s.md) · **2**

### Subida

- Cada orden viaja por subida y su respuesta por bajada; cada trayecto se pierde con probabilidad `p`.

💡 **Cómo se explica en la clase [B98-C06](../programa/clases/B98/B98-C06-simulacion-de-teleoperacion-con-retardo/CLASE.md):**
- *Descripción textual:* cada orden se reenvía hasta que subida y bajada llegan; los intentos fallidos cuestan el temporizador y el éxito cuesta ejecución y decisión.
- 🎯 **Por qué importa:** Un promedio oculta la cola: una campaña que «normalmente» dura 8,7 h puede tardar 10,2 h una de cada veinte veces. La decisión central: ¿qué duración debe prometerse a la misión, la media o un percentil, y cómo se comprueba que la simulación es correcta?

📘 **Dónde se aprende** (1 clase): [B98-C06 · Simulación de teleoperación con retardo](../programa/clases/B98/B98-C06-simulacion-de-teleoperacion-con-retardo/CLASE.md).

### Subida rápida y caída exponencial

- La subida rápida y caída exponencial es su plantilla mínima.

🎯 **Por qué importa (clase B29-C15):** La distribución de energías de las llamaradas determina cuánta energía total reciben los planetas cercanos. Estimar su índice con poco sesgo exige usar el estimador correcto.

📘 **Dónde se aprende** (1 clase): [B29-C15 · Eventos eruptivos estelares](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md).

### Sublimación

- La sublimación es el paso de sólido a gas.
- La sublimación es el paso de sólido a vapor.
- Las curvas de equilibrio separan regiones: fusión (sólido–líquido), vaporización (líquido–gas) y sublimación (sólido–gas).

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- Con el CO₂, sublimación a 1 atm, y `ΔH_sub = 26,1 kJ/mol`, resulta `194,7 K`; con los extremos publicados (25,2 y 27,2 kJ/mol), `194,0` y `195,5 K`: la incertidumbre de `ΔH` mueve el resultado en 1,5 K (S5).
- B -->|"Sí"| C{"¿T < T de sublimación a esa P?"}
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.

📘 **Dónde se aprende** (3 clases): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md); [B58-C04 · Núcleos y colas cometarias](../programa/clases/B58/B58-C04-nucleos-y-colas-cometarias/CLASE.md); [B59-C06 · Extracción y procesamiento de volátiles](../programa/clases/B59/B59-C06-extraccion-y-procesamiento-de-volatiles/CLASE.md).

### Submuestrear

- La cadencia es el intervalo entre observaciones; submuestrear es quedarse con un registro por ventana de tiempo.

🎯 **Por qué importa (clase B14-C22):** Quieres estudiar una región activa del Sol durante un día usando imágenes ultravioleta. Hay cientos de miles de archivos repartidos en varios proveedores.

📘 **Dónde se aprende** (1 clase): [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md).

### Subnormal

- Un desbordamiento es un resultado mayor que el máximo representable (`1,8 × 10³⁰⁸`), que da `inf`; un subdesbordamiento va hacia cero o a un número subnormal.

💡 **Cómo se explica en la clase [B11-C25](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md):**
- Los límites son `1,8 × 10³⁰⁸` (máximo), `2,2 × 10⁻³⁰⁸` (mínimo normal) y `4,9 × 10⁻³²⁴` (mínimo subnormal);
- 🎯 **Por qué importa:** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.

📘 **Dónde se aprende** (1 clase): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md).

### Subnotificación

- Una cultura justa protege el reporte honesto. Subnotificación es informar menos de lo ocurrido.

💡 **Cómo se explica en la clase [B119-C21](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md):**
- ⚠️ **Error frecuente:** Ignorar la subnotificación. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** B88-C16 cubre la seguridad funcional técnica; ninguna clase trata la dimensión cultural, y los indicadores de reportes se malinterpretan con facilidad. La decisión central: ¿qué indicador permite saber si una organización aprende cuando los reportes dependen de la confianza para informar?

📘 **Dónde se aprende** (1 clase): [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md).

### Subpresión

- La subpresión `ΔP` es la caída de presión de la cámara respecto de la litostática.

💡 **Cómo se explica en la clase [B70-C03](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md):**
- Un techo ancho y delgado colapsa con menos subpresión.
- D["volumen evacuado"] --> P["subpresión ΔP = K ΔV/Vc"]
- ⚠️ **Error frecuente:** Confundir subpresión con presión. Se corrige en la sección 6.
- 🎯 **Por qué importa:** Evacuar magma no siempre hunde el techo. La decisión central: ¿cuánta subpresión resiste un techo y cuánto magma hay que sacar para vencerla?

📘 **Dónde se aprende** (1 clase): [B70-C03 · Calderas planetarias: formación y colapso](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md).

### Subproducto

- El subproducto aquí es el monóxido de carbono.
- Un subproducto es un material que sale junto al producto.

💡 **Cómo se explica en la clase [B59-C23](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md):**
- El balance dice cuánto; no dice si el subproducto tiene uso.
- 🎯 **Por qué importa:** Producir un kilogramo de oxígeno genera toneladas de otras cosas. La decisión central: ¿qué masa de residuo o de subproducto aparece por cada kilogramo de producto?

📘 **Dónde se aprende** (2 clases): [B59-C08 · Producción de oxígeno](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md); [B59-C23 · Subproductos y flujos residuales de procesos ISRU](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md).

### Subsidencia

- La subsidencia es el hundimiento del terreno.

🎯 **Por qué importa (clase B69-C06):** Un solo interferograma no dice si el suelo bajó o se movió al este. La decisión central: ¿qué parte del movimiento real mide la línea de visión, hasta qué gradiente se puede desenvolver y qué se puede concluir?

📘 **Dónde se aprende** (1 clase): [B69-C06 · Deslizamientos y subsidencia medidos con InSAR](../programa/clases/B69/B69-C06-deslizamientos-y-subsidencia-medidos-con-insar/CLASE.md).

### Subtítulos

- Los subtítulos (captions) son texto sincronizado con el habla y con los sonidos no hablados relevantes.

💡 **Cómo se explica en la clase [B128-C05](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md):**
- W3C WAI distingue: los *captions* son el texto del habla y de los sonidos no hablados necesarios, sincronizados y normalmente activables; los *subtítulos* suelen ser traducciones a otro idioma; las transcripciones tienen el mismo texto que los captions; la audiodescripción describe lo visual.
- ⚠️ **Error frecuente:** Confundir subtítulos y transcripción. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un subtítulo mal sincronizado o demasiado rápido no se alcanza a leer, y una transcripción automática sin revisar puede decir lo contrario de lo dicho. La decisión central: ¿cómo compruebo que los subtítulos se pueden leer y que no cambian el sentido?

📘 **Dónde se aprende** (1 clase): [B128-C05 · Subtítulos y transcripciones](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md).

### Sub-triage

- La categoría (baja, media, alta) agrupa el total. Sub-triage: caso asignado a una categoría menos urgente que la verdadera;

💡 **Cómo se explica en la clase [B116-C04](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md):**
- Sensibilidad `(1132 + 1240 + 1013)/3978 = 0,851`; especificidad `15822/16022 = 0,988`; sub-triage `593/20000 = 2,96 %`.
- El ruido del sensor produce sobre-triage de personas estables, con el coste de alertas y consultas, más que sub-triage.
- 🎯 **Por qué importa:** Un puntaje simple ayuda a decidir rápido y de forma homogénea, pero un fallo por defecto (sub-triage) deja sin atender a quien lo necesita y uno por exceso (sobre-triage) agota recursos y atención. Y si la respuesta de tierra tarda decenas de minutos, no se puede esperar a tierra para lo que no admite espera.

📘 **Dónde se aprende** (1 clase): [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Sucesión de Sturm

- La sucesión de Sturm cuenta autovalores menores que un valor.

🎯 **Por qué importa (clase B31-C02):** Los espectros de los átomos y los niveles de los núcleos salen de esta ecuación. La decisión central: ¿cómo se obtiene la energía de un estado ligado y cuánto atraviesa una barrera?

📘 **Dónde se aprende** (1 clase): [B31-C02 · Ecuación de Schrödinger](../programa/clases/B31/B31-C02-ecuacion-de-schrodinger/CLASE.md).

### Suceso raro

- Un suceso raro tiene probabilidad muy pequeña.

💡 **Cómo se explica en la clase [B12-C15](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md):**
- A["Objetivo p(x)<br/>(suceso raro en la cola)"] --> B["Elegir propuesta q(x)<br/>con masa en la cola"]
- 🎯 **Por qué importa:** Los sucesos que más interesan en seguridad espacial —un error de aproximación fuera de límites, una falla simultánea, una colisión— son raros por diseño. Un Monte Carlo simple puede pasar millones de ensayos sin ver un solo acierto y reportar «cero», que no es una estimación útil.

📘 **Dónde se aprende** (1 clase): [B12-C15 · Muestreo de importancia](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md).

### Suelo de fondo

- El suelo de fondo es el suelo visible bajo y entre las plantas.

💡 **Cómo se explica en la clase [B57-C06](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar el suelo de fondo. Se mide en 8.2.
- 🎯 **Por qué importa:** Un índice facilita comparar fechas y lugares, pero también esconde supuestos. La decisión central: ¿cuándo el NDVI mide de verdad la cantidad de vegetación y cuándo lo engañan la saturación o el suelo?

📘 **Dónde se aprende** (1 clase): [B57-C06 · Índices de vegetación](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md).

### Suelo de ruido

- El suelo de ruido es el límite de precisión de la posición de una fuente que no baja aunque se observe más (S1;
- El suelo de ruido es `k T B` más la cifra de ruido.
- El suelo de ruido limita lo que se ve de los lóbulos.

💡 **Cómo se explica en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
- ICRF2 (2009; fundamental desde el 1 de enero de 2010): `295` definidoras, `3414` fuentes en total, suelo de ruido `≈ 0,04 mas` y ejes estables dentro de `0,01 mas` (S1, 2.2).
- ICRF3 (adoptado por la IAU en 2018, vigente desde el 1 de enero de 2019): `4588` fuentes, `303` definidoras, mediana `0,1 mas`/`0,2 mas`, suelo de ruido `0,03 mas`, con medidas en `8,4`, `24` y `32 GHz` (S2, resumen).
- 🎯 **Por qué importa:** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.

📘 **Dónde se aprende** (3 clases): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md); [B49-C05 · Medición y calibración de patrones de antena](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md); [B49-C09 · Linealidad, compresión e intermodulación de receptores de RF](../programa/clases/B49/B49-C09-linealidad-compresion-e-intermodulacion-de-receptores-de-rf/CLASE.md).

### Suficiente

- El teorema de la ganancia pequeña dice que, si el lazo nominal es estable y `|Δ|·‖T‖∞ < 1` (para `Δ` constante o con `|Δ(jω)| ≤ δ`), el lazo con incertidumbre multiplicativa sigue estable: es una condición suficiente.
- La cota de Liu–Layland `n(2^(1/n) − 1)` es una condición suficiente de planificabilidad con prioridades por tasa.
- Un criterio necesario debe cumplirse siempre; uno suficiente basta por sí solo.

💡 **Cómo se explica en la clase [B16-C16](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md):**
- La cota es suficiente pero no necesaria.
- 🎯 **Por qué importa:** La inercia de un satélite cambia al desplegar paneles, consumir propergol o capturar una carga; el actuador envejece; el sensor tiene un retardo que no se conocía. El lazo diseñado con la inercia nominal debe seguir funcionando.

📘 **Dónde se aprende** (3 clases): [B16-C16 · Control robusto inicial](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md); [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md); [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md).

### Suitport

- Un suitport acopla el traje a la pared del hábitat para entrar sin llevar el polvo adentro.

💡 **Cómo se explica en la clase [B109-C04](../programa/clases/B109/B109-C04-mitigacion-de-polvo-lunar-en-accesos-y-habitats/CLASE.md):**
- (2023) comparan esclusa, *suitlock* y suitport-esclusa y concluyen, de forma cualitativa, que los dos últimos reducen la entrada de polvo porque evitan abrir la escotilla interior con trajes sucios.
- Con cepillado más suitport (`3 %` cruza, ilustrativo) bajan a `1,20 g` por traje y `0,250 kg/año`.
- 🎯 **Por qué importa:** Cada salida y cada regreso trae polvo a un lugar donde la tripulación respira, duerme y repara equipos. La decisión central: ¿cuántas barreras en serie hacen falta y qué arquitectura de acceso reduce más la entrada?

📘 **Dónde se aprende** (1 clase): [B109-C04 · Mitigación de polvo lunar en accesos y hábitats](../programa/clases/B109/B109-C04-mitigacion-de-polvo-lunar-en-accesos-y-habitats/CLASE.md).

### Sujeción

- Par `τ`: fuerza por brazo. Sujeción: apoyo que reacciona.

💡 **Cómo se explica en la clase [B106-C16](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md):**
- *Descripción textual:* la fuerza que se aplica a una carga produce una reacción sobre el cuerpo; una sujeción absorbe esa reacción y mantiene la tarea en su sitio.
- Paso 4. Par de 10 N·m sin sujeción: `α = 10/1,5 = 6,67 rad/s²`;
- 🎯 **Por qué importa:** Sin peso ni fricción, toda fuerza tiene una reacción que mueve al operario o a la carga; un diseño de herramientas y de superficies que lo ignore produce maniobras inseguras. La decisión central: ¿qué sujeciones y qué límites de par o de empuje evitan que la reacción mueva al astronauta fuera de la tarea?

📘 **Dónde se aprende** (1 clase): [B106-C16 · Ergonomía en microgravedad](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md).

### Suma

- La suma de vectores se hace componente a componente.

💡 **Cómo se explica en la clase [B04-C12](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md):**
- Para sumar dos, pon el inicio de la segunda en la punta de la primera: la suma es la flecha que va del inicio de la primera a la punta de la segunda.
- A["v_Tierra = (0; 29,79) km/s"] --> S["Suma componente a componente"]
- 🎯 **Por qué importa:** Una sonda que sale de la Tierra tiene una velocidad respecto de la Tierra y la Tierra tiene una velocidad respecto del Sol. ¿Cuál es la velocidad de la sonda respecto del Sol?

📘 **Dónde se aprende** (1 clase): [B04-C12 · Vectores y componentes](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md).

### Suma compensada

- La suma compensada (de Kahan) lleva una corrección con lo que se pierde en cada suma.

🎯 **Por qué importa (clase B11-C25):** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.

📘 **Dónde se aprende** (1 clase): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md).

### Suma cuadrática

- La suma cuadrática combina aportes independientes.
- La suma cuadrática combina términos independientes.

💡 **Cómo se explica en la clase [B50-C15](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md):**
- Con 20 000 sistemas la media de `W²` es `2812,6 ± 8,9 nm²` y la suma cuadrática da `2825,0 nm²`.
- 🎯 **Por qué importa:** El requisito de un instrumento se cumple o no según cómo se reparta el error entre diseño, fabricación y alineación. La decisión central: ¿cuánto frente de onda se puede gastar en cada etapa sin superar el requisito?

📘 **Dónde se aprende** (2 clases): [B50-C09 · Asignación y balance de tolerancias ópticas](../programa/clases/B50/B50-C09-asignacion-y-balance-de-tolerancias-opticas/CLASE.md); [B50-C15 · Presupuesto de error de frente de onda de un instrumento](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md).

### Suma de apertura

- La suma de apertura suma los píxeles y corrige la fracción.

🎯 **Por qué importa (clase B45-C18):** Una extracción ingenua pierde señal a ruido y es sensible a defectos. La decisión central: ¿qué pesos dan la menor varianza y cómo se protege la extracción de valores atípicos?

📘 **Dónde se aprende** (1 clase): [B45-C18 · Extracción de espectros](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md).

### Suma de cuantilas

- La suma de cuantilas es conservadora; la raíz de la suma de cuadrados (RSS) es optimista para sumar magnitudes.

💡 **Cómo se explica en la clase [B81-C14](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md):**
- La cuantila de la suma queda entre el RSS y la suma de cuantilas.
- Cinco correcciones independientes necesitan `8,19 m/s` (la suma de cuantilas sería `13,20`).
- 🎯 **Por qué importa:** Un presupuesto muy bajo deja a la nave sin propelente; uno muy alto la lastra. La decisión central: ¿qué cuantila de `Δv` reservar para una o varias correcciones, y cómo se combinan?

📘 **Dónde se aprende** (1 clase): [B81-C14 · Presupuestos de maniobras de corrección](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md).

### Suma de flujos

- Brillo del cielo: mag por arcsec². Suma de flujos: los brillos se suman como flujos.

💡 **Cómo se explica en la clase [B48-C18](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md):**
- M["m_nat, m_art"] --> S["Suma de flujos"]
- 🎯 **Por qué importa:** Cada fracción de magnitud perdida se paga en tiempo de telescopio. La decisión central: ¿cuánto cuesta en exposición una contaminación luminosa dada?

📘 **Dónde se aprende** (1 clase): [B48-C18 · Protección del cielo oscuro](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md).

### Suma de fracciones de vida consumidas

- Daño acumulado: suma de fracciones de vida consumidas. Paquete de datos: conjunto de evidencias de aceptación.

🎯 **Por qué importa (clase B90-C19):** Un ensayo de aceptación demasiado severo gasta vida útil; uno demasiado suave deja pasar defectos. La decisión central: ¿qué nivel y duración demuestran la mano de obra sin dañar la unidad, y con qué evidencia se acepta?

📘 **Dónde se aprende** (1 clase): [B90-C19 · Aceptación de unidades de vuelo](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md).

### Suma de Petzval

- La superficie de Petzval es la superficie de enfoque sin astigmatismo; su curvatura es la suma de Petzval `Σ φᵢ/nᵢ` (con `n = −1` en un espejo).

💡 **Cómo se explica en la clase [B50-C07](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md):**
- *Descripción textual:* las superficies de enfoque se obtienen de trazar haces estrechos, y el aplanador anula la suma de Petzval.
- 🎯 **Por qué importa:** Un detector plano mal enfocado en el borde pierde resolución: hay que decidir si se acepta, se curva el detector o se agrega un aplanador. La decisión central: ¿cuánto se hunde el foco en el borde y qué lo corrige?

📘 **Dónde se aprende** (1 clase): [B50-C07 · Curvatura de campo y aplanadores](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md).

### Suma de verificación

- Una suma de verificación (*checksum*) es un número calculado a partir de los bytes de un archivo.
- Suma de verificación: resumen corto de un archivo.

🎯 **Por qué importa (clase B14-C11):** Un análisis usó «la tabla de catálogo de octubre». En noviembre alguien reemplazó el archivo por otro con el mismo nombre.

📘 **Dónde se aprende** (2 clases): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md); [B48-C17 · Gestión de archivos observacionales](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md).

### Suma directa

- La suma directa suma `−G m_i/d_i` sobre todas las masas.
- La suma directa calcula la fuerza sobre cada cuerpo como suma de las de los demás: `a_i = Σ_{j≠i} GM_j (r_j − r_i)/|r_j − r_i|³`.

💡 **Cómo se explica en la clase [B53-C03](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md):**
- A `r = 3a` la serie con `J2` difiere de la suma directa en `3,69 × 10⁻⁵` en relación; a `r = 10a`, en `2,78 × 10⁻⁷`.
- 🎯 **Por qué importa:** Las trayectorias de una sonda dependen del campo. La decisión central: ¿hasta qué término de la serie hay que llegar a una distancia dada?

📘 **Dónde se aprende** (2 clases): [B53-C03 · Campo gravitatorio planetario](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md); [B73-C08 · Sistemas de N cuerpos](../programa/clases/B73/B73-C08-sistemas-de-n-cuerpos/CLASE.md).

### Suma en cuadratura (RSS)

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C20):** Un diseño es un conjunto de compromisos. La decisión central: ¿qué apertura y qué focal cumplen el objetivo y qué defecto domina?

📘 **Dónde se aprende** (2 clases): [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md); [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md).

### Suma incoherente

- Incertidumbre `U`: dispersión de la medida. Suma incoherente: suma de potencias.

🎯 **Por qué importa (clase B90-C13):** Un convertidor de potencia emite armónicos que viajan por el arnés y pueden perturbar a otro equipo. El margen de 2 dB que pasa hoy puede ser negativo mañana si cambia la incertidumbre.

📘 **Dónde se aprende** (1 clase): [B90-C13 · Compatibilidad electromagnética EMC](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md).

### Suma lineal

- La suma lineal es la cota del peor caso.

💡 **Cómo se explica en la clase [B87-C22](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md):**
- Suma lineal: peor caso o errores correlacionados.
- 🎯 **Por qué importa:** Un requisito de apuntamiento solo se cumple si el diseño lo respalda con números. La decisión central: ¿qué contribuyentes dominan, cómo se combinan (suma lineal o cuadrática), con qué margen se cumple el requisito y qué ocurre con dos ejes?

📘 **Dónde se aprende** (1 clase): [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md).

### Suma ponderada

- La suma ponderada puntúa cada candidato como `Σ wⱼ vⱼ`, con `vⱼ` normalizado y con signo según se maximice o minimice.
- La suma ponderada combina puntajes.

💡 **Cómo se explica en la clase [B91-C06](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md):**
- Límite: la suma ponderada con normalización min–max depende del conjunto de candidatos; añadir uno cambia la escala.
- 🎯 **Por qué importa:** Ninguna antena gana en todo: más ganancia suele costar masa, apertura o dinero. La decisión central: ¿qué antena cumple los requisitos y cuál conviene según cómo se pesen la masa, el costo y el riesgo, y cuánto cambia la respuesta si los pesos cambian?

📘 **Dónde se aprende** (2 clases): [B91-C06 · Selección y compromiso de diseño de antenas](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md); [B119-C18 · Ética y derechos en actividades espaciales](../programa/clases/B119/B119-C18-etica-y-derechos-en-actividades-espaciales/CLASE.md).

### Sumador

- Un sumador (círculo) combina señales con signo.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- Se puede trasladar un sumador o una bifurcación a través de un bloque si se compensa con ese mismo bloque.
- Recorre una señal: sale del sumador como error, pasa por el controlador, el cuerpo, llega a la salida, vuelve por el sensor al sumador.
- ⚠️ **Error frecuente:** Confundir el signo del sumador. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.

📘 **Dónde se aprende** (1 clase): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md).

### Sumas de Riemann

- La integral definida `∫_a^b f(x) dx` es el límite de las sumas de Riemann `Σ f(x_i*) Δx` cuando `Δx → 0` (S1, §1.4(v)).

🎯 **Por qué importa (clase B09-C11):** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.

📘 **Dónde se aprende** (1 clase): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md).

### Sumidero

- Alcanzabilidad: estados a los que se llega desde otro. Sumidero: estado terminal.

💡 **Cómo se explica en la clase [B96-C08](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md):**
- (2) FIN es sumidero y solo lo alcanza DESORBITANDO.
- Paso 4 · Sumidero. FIN solo desde DESORBITANDO.
- 🎯 **Por qué importa:** Un comando válido en un estado puede ser peligroso en otro; y un modo seguro al que no se puede volver es una trampa. La decisión central: ¿qué transiciones existen y se puede siempre llegar al estado seguro?

📘 **Dónde se aprende** (1 clase): [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md).

### Sumidero efectivo

- Radiador: superficie que emite al espacio. Sumidero efectivo: temperatura radiativa del entorno visto.

🎯 **Por qué importa (clase B106-C08):** En el vacío el calor solo sale por radiación; el área del radiador depende de la temperatura y de lo que «ve». La decisión central: ¿cuánta área y qué caudal de refrigerante para evacuar la carga, y cuánto tiempo hay si el enfriamiento falla?

📘 **Dónde se aprende** (1 clase): [B106-C08 · Control térmico interior](../programa/clases/B106/B106-C08-control-termico-interior/CLASE.md).

### Sumidero equivalente

- El sumidero equivalente `T_s` agrupa en una temperatura lo que el radiador ve.

💡 **Cómo se explica en la clase [B86-C12](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md):**
- Con `Q = 20,124 W`, `ε = 0,85`, `T = 300 K` y un sumidero equivalente de `220 K`: `A = Q/(ε σ (T⁴ − T_s⁴)) = 0,0725 m²` (`q = 277,5 W/m²`).
- Límite: el sumidero equivalente no es un balance térmico: ignora la Tierra, el Sol y los intercambios radiativos entre superficies.
- 🎯 **Por qué importa:** Una eficiencia de `92 %` parece alta hasta que se multiplica por las demás etapas y se ve el calor que queda. Cada vatio perdido debe radiarse: el calor decide el tamaño del radiador y la potencia del ala.

📘 **Dónde se aprende** (1 clase): [B86-C12 · Eficiencia y disipación](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md).

### SumThreshold

- El umbral `χ σ`. SumThreshold: umbrales sobre la media de `M` muestras consecutivas.

💡 **Cómo se explica en la clase [B51-C13](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md):**
- Umbrales de SumThreshold con `χ₁ = 4` y `ρ = 1,5`: 1 muestras: 4,00 σ, 2 muestras: 2,67 σ, 4 muestras: 1,78 σ, 8 muestras: 1,19 σ, 16 muestras: 0,79 σ.
- M --> S["SumThreshold: M = 1, 2, 4, 8, 16"]
- ⚠️ **Error frecuente:** Creer que SumThreshold es gratis. Se corrige con la tabla de 8.2.
- 🎯 **Por qué importa:** Dejar RFI en los datos degrada la imagen; marcar demasiado pierde señal. La decisión central: ¿qué umbral marca la interferencia sin marcar el ruido, y cómo se detecta la interferencia débil y extendida?

📘 **Dónde se aprende** (1 clase): [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md).

### Supercúmulo

- Un supercúmulo es una estructura mayor que reúne grupos y cúmulos;

💡 **Cómo se explica en la clase [B01-C15](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md):**
- CL --> SC["Supercúmulo: Laniakea (flujos convergentes)"]
- *Descripción textual:* una jerarquía de cinco niveles ligados por la gravedad: estrellas, galaxia, grupo, cúmulo y supercúmulo; más allá, la expansión domina y lo no ligado se aleja.
- 🎯 **Por qué importa:** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Superficial r_s

- La resistencia aerodinámica `r_a` y la superficial `r_s` controlan el paso del vapor.

🎯 **Por qué importa (clase B115-C06):** El cultivo es el mayor flujo de agua de un hábitat con plantas. La decisión central: ¿cuánta agua transpira el cultivo, cuánta se recupera y cuánta hay que reponer, y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B115-C06 · Balance de agua y evapotranspiración en cultivos](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md).

### Superficie

- La superficie es la capa química activa en contacto con el gas (aquí, una monocapa); el manto es el hielo enterrado bajo ella.
- El tránsito es el viaje entre destinos; la superficie, la estancia sobre un cuerpo planetario.

💡 **Cómo se explica en la clase [B60-C04](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md):**
- El enterramiento es `F_ent = F_acc (s/ML)⁴`, de modo que la superficie se llena hasta 1 ML y el exceso se entierra.
- Un modelo de dos fases mantiene 79 monocapas como «superficie activa»; el de tres fases, una.
- ⚠️ **Error frecuente:** Tratar todo el hielo como superficie. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un modelo de dos fases trata todo el hielo como si estuviera expuesto en la superficie; en la realidad la mayor parte queda enterrada bajo capas posteriores. La decisión central: ¿qué cambia en la predicción de cuánto hielo se libera al calentar si se distingue la superficie del manto?

📘 **Dónde se aprende** (2 clases): [B60-C04 · Balance químico gas-grano: modelos de tres fases](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md); [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Superficie de Petzval

- La superficie de Petzval es la superficie de enfoque sin astigmatismo; su curvatura es la suma de Petzval `Σ φᵢ/nᵢ` (con `n = −1` en un espejo).

🎯 **Por qué importa (clase B50-C07):** Un detector plano mal enfocado en el borde pierde resolución: hay que decidir si se acepta, se curva el detector o se agrega un aplanador. La decisión central: ¿cuánto se hunde el foco en el borde y qué lo corrige?

📘 **Dónde se aprende** (1 clase): [B50-C07 · Curvatura de campo y aplanadores](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md).

### Superficie específica

- La superficie específica es el área por unidad de masa.

🎯 **Por qué importa (clase B59-C04):** Un tamiz, una tolva o un horno de sinterización se diseñan para una distribución de tamaños, no para un grano. La decisión central: ¿qué fracción de la masa es fina (menor de 20 µm) y cuánto cambia si hablo de número o de masa?

📘 **Dónde se aprende** (1 clase): [B59-C04 · Caracterización de regolito lunar](../programa/clases/B59/B59-C04-caracterizacion-de-regolito-lunar/CLASE.md).

### Superficie numérica

- La superficie numérica es el punto donde `ρ` baja de un umbral (aquí `10³ kg/m³`).

🎯 **Por qué importa (clase B27-C02):** Las enanas blancas son el destino de la mayoría de las estrellas, sirven de relojes cosmológicos y, al acercarse a su masa límite, pueden explotar. Una relación masa–radio correcta separa masas y radios que la fotometría sola confunde.

📘 **Dónde se aprende** (1 clase): [B27-C02 · Enanas blancas y límite de Chandrasekhar](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md).

### Supernova

- Una supernova es la explosión de una estrella que brilla durante semanas.
- Una supernova es la explosión final de una estrella masiva o de una enana blanca que acreta.
- Una supernova es la explosión final de una estrella masiva; aquí se toma una energía convencional de `10⁵¹ erg = 10⁴⁴ J` por explosión (valor ilustrativo).

💡 **Cómo se explica en la clase [B02-C12](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md):**
- Las observaciones de S1 para la supernova de 1572 y el cometa de 1577 no mostraron un paralaje apreciable con la precisión de Tycho, por lo que los objetos estaban más allá de la Luna.
- S1 indica que la supernova y el cometa socavaban la división aristotélica entre lo terrestre y lo celeste, y que el movimiento del cometa mostraba que no podían existir esferas sólidas, idea que fue desapareciendo entre 1575 y 1625.
- 🎯 **Por qué importa:** Una teoría solo es tan buena como los datos con que se contrasta. La pregunta motivadora es: ¿qué diferencia hay entre «mirar el cielo» y «observar sistemáticamente», y por qué esa diferencia cambió la astronomía?

📖 **Explicado a fondo:** [Supernova](esencial/esencial-m-z.md#supernova) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B02-C12 · Tycho Brahe y observaciones sistemáticas](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md); [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md); [B25-C16 · Retroalimentación estelar](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md).

### Supernovas Ia

- Las supernovas Ia son velas estándar tras la calibración.

💡 **Cómo se explica en la clase [B26-C19](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md):**
- Riess y colaboradores midieron 10 supernovas Ia a `0,16 < z < 0,62` y las combinaron con otras 40: las distantes aparecían, en promedio, un `10` a `15 %` más lejos de lo esperado en un universo de baja densidad sin constante cosmológica, lo que favorecía una constante cosmológica positiva (S3, resumen).
- 🎯 **Por qué importa:** La aceleración cósmica se descubrió porque las supernovas Ia lejanas aparecían más débiles de lo esperado. Para reproducir ese razonamiento hay que saber calcular la distancia de luminosidad y ver cuánto cambia con el contenido del universo.

📘 **Dónde se aprende** (1 clase): [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md).

### Superposición

- Un sistema es lineal si cumple aditividad (la respuesta a `u₁ + u₂` es la suma de respuestas) y homogeneidad (la respuesta a `a u` es `a` por la respuesta a `u`); juntas, superposición.
- La superposición dice que dos ondas se suman.
- La superposición trata un núcleo como `A` protones.

💡 **Cómo se explica en la clase [B16-C03](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md):**
- Superposición: si `u₁ → y₁` y `u₂ → y₂`, entonces `a u₁ + b u₂ → a y₁ + b y₂`.
- ⚠️ **Error frecuente:** Olvidar las condiciones iniciales. Superposición exige reposo o separar la respuesta libre.
- 🎯 **Por qué importa:** Un ingeniero de control no puede ensayar todos los pares posibles en un telescopio de miles de millones de euros. La esperanza es que, con unas pocas pruebas, se pueda predecir la respuesta a cualquier par.

📘 **Dónde se aprende** (3 clases): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B31-C13 · Rayos cósmicos y cascadas](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md).

### Superposición modal

- La superposición modal es `H_ij = Σ φ_ir φ_jr/(ω_r² − ω² + 2iζ_r ω_r ω)`.

🎯 **Por qué importa (clase B84-C33):** La función de transferencia dice cuánto se amplifica cada frecuencia entre el punto donde se excita y el punto donde se mide; es la herramienta que usan el análisis y el ensayo de barrido sinusoidal. La decisión central: ¿cuánto se amplifica la respuesta en cada frecuencia y cuánto amortiguamiento tiene cada modo?

📘 **Dónde se aprende** (1 clase): [B84-C33 · Respuesta armónica y funciones de transferencia estructural](../programa/clases/B84/B84-C33-respuesta-armonica-y-funciones-de-transferencia-estructural/CLASE.md).

### Supervisión continua

- La supervisión continua es el control durante toda la vida de la actividad.
- La supervisión continua es la vigilancia del Estado tras otorgar la licencia.

💡 **Cómo se explica en la clase [B119-C08](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md):**
- VI: los Estados responden internacionalmente por sus actividades nacionales, públicas o privadas; las privadas requieren autorización y supervisión continua.
- 🎯 **Por qué importa:** C01 enuncia el art. VI como regla; esta clase lo convierte en un proceso con tiempos y cobertura, lo que ninguna clase del bloque hace.

📘 **Dónde se aprende** (2 clases): [B119-C08 · Autorización y supervisión de operadores](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md); [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md).

### Supervivencia

- La supervivencia `S` es la fracción que queda tras recorrer una distancia.
- La supervivencia `S(D)` es la fracción de células que lo logra.
- La supervivencia es la fracción de la masa o de los fragmentos que llega al suelo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B26-C03](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md):**
- La supervivencia de `1/2` tras `15 km` exige `d/(γβcτ) = ln 2`: `γ = 32,87`, `β = 0,999 537`.
- *Descripción textual:* en ambos marcos el tiempo propio del recorrido es `d/(γβc)`, y la supervivencia es la exponencial de ese tiempo entre la vida media.
- 🎯 **Por qué importa:** Los muones se producen en la alta atmósfera por rayos cósmicos, viven microsegundos y, sin embargo, llegan al suelo en cantidad. Los relojes de satélites de navegación se ajustan por el mismo efecto.

📘 **Dónde se aprende** (4 clases): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md); [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md); [B118-C14 · Reentrada y riesgos en superficie](../programa/clases/B118/B118-C14-reentrada-y-riesgos-en-superficie/CLASE.md); [B127-C02 · Seguros en órbita](../programa/clases/B127/B127-C02-seguros-en-orbita/CLASE.md).

### Superviviente

- Un superviviente es una estrella que aún está en la secuencia principal.

🎯 **Por qué importa (clase B24-C19):** La edad de una estrella aislada es difícil de medir; la de un cúmulo se puede leer en su diagrama HR, porque las estrellas más masivas ya han salido de la secuencia principal y el «punto de desvío» marca la edad. Esas edades fijan la cronología de la Galaxia y calibran los modelos.

📘 **Dónde se aprende** (1 clase): [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Supresión

- La supresión es el cociente entre `D(1)` en ΛCDM y `a` (en EdS vale 1).
- La supresión descarta el evento y cuenta cuántos.
- Una alarma dependiente se deriva de una causa raíz ya activa; la supresión la oculta para no saturar.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B47-C07](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md):**
- B["brillo corona 1e-6"] --> S["supresión 1e-7"]
- Ver una corona de brillo `10⁻⁶` con `S/N = 10` exige una supresión de `1,0 × 10⁻⁷`.
- 🎯 **Por qué importa:** La luz difractada del disco es mayor que la señal buscada. La decisión central: ¿cuánta supresión de luz difractada se necesita y con qué geometría de ocultador?

📘 **Dónde se aprende** (6 clases): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md); [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md); [B88-C10 · Gestión de eventos](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md); [B98-C04 · Interfaces humano-robot para operación remota](../programa/clases/B98/B98-C04-interfaces-humano-robot-para-operacion-remota/CLASE.md); [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md); [B129-C05 · Consentimiento y privacidad de participantes](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md).

### Supresión (dBc)

- Armónico: componente a múltiplo de la frecuencia del transmisor. Supresión (dBc): nivel relativo a la portadora.

🎯 **Por qué importa (clase B90-C14):** Un transmisor de 1 W deja un armónico de −30 dBm; el piso de ruido de un receptor estrecho está cerca de −132 dBm. La diferencia de más de 100 dB se pierde con facilidad en un chasis de 10 cm.

📘 **Dónde se aprende** (1 clase): [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md).

### Supuesto

- Un supuesto es una condición que se acepta sin comprobarla en ese momento.
- Un supuesto es una condición aceptada (órbitas circulares, masa del planeta despreciable).
- Para un gas diatómico rígido, `κ = 2/7` y `c_p = 7R/(2M)`; es un supuesto de la clase.

💡 **Cómo se explica en la clase [B01-C05](../programa/clases/B01/B01-C05-observacion-frente-a-interpretacion/CLASE.md):**
- Convertir `z` en velocidad con `v ≈ c·z` agrega un supuesto: que `z` es pequeño y que el corrimiento se interpreta como movimiento aparente.
- El primer peldaño es lo que el instrumento registró; cada peldaño siguiente agrega un supuesto, y cuanto más arriba, más cosas hay que creer para sostener la frase.
- 🎯 **Por qué importa:** En septiembre de 2011 la colaboración OPERA publicó que neutrinos enviados desde el CERN habían llegado a su detector, a unos 730 km, 60,7 ns antes de lo que tardaría la luz (S1, versión 1). Una cifra medida pasó rápidamente a titulares que decían otra cosa.

📘 **Dónde se aprende** (3 clases): [B01-C05 · Observación frente a interpretación](../programa/clases/B01/B01-C05-observacion-frente-a-interpretacion/CLASE.md); [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B54-C15 · Atmósferas de gigantes gaseosos](../programa/clases/B54/B54-C15-atmosferas-de-gigantes-gaseosos/CLASE.md).

### Suscripción

- La suscripción es acceso por un plazo a un precio fijo.

💡 **Cómo se explica en la clase [B125-C02](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md):**
- El ejemplo conductor es sintético: una suscripción anual de `120 000` u.m. pagada por adelantado se reconoce a `10 000` u.m. por mes; un cliente con `ARPU = 1 000`, margen `70 %` y abandono `2 %` mensual vale `35 000` u.m.
- Descripción larga: la suscripción reparte el ingreso en 12 partes iguales aunque se cobre al inicio; el servicio concentra el ingreso en cuatro hitos; el valor de vida cae a la mitad cuando el abandono se duplica.
- 🎯 **Por qué importa:** El modelo de ingresos define cuándo entra el dinero y cuánto vale un cliente; ninguna clase anterior lo trata. La decisión central: ¿cuánto vale un cliente de suscripción, cuándo se reconoce su ingreso y cuánto abandono puede tolerar el negocio?

📘 **Dónde se aprende** (1 clase): [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md).

### Sustentación

- El coeficiente de arrastre es `Cd = D/(q·A)` y el de sustentación `CL = L/(q·A)`.
- La fuerza aerodinámica se descompone en arrastre `D = Cd·q·A` y sustentación `L = CL·q·A`.

💡 **Cómo se explica en la clase [B77-C03](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md):**
- Una sustentación pequeña ya carga la estructura de forma lateral.
- *Descripción textual:* el tiempo da altitud y velocidad; de ahí sale la presión dinámica, con la que se calculan arrastre, sustentación y el máximo de `q`.
- 🎯 **Por qué importa:** El momento de mayor carga aerodinámica no es el de mayor velocidad ni el de menor altitud. La decisión central: ¿cuándo ocurre el máximo de la presión dinámica y qué fuerzas produce?

📘 **Dónde se aprende** (2 clases): [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md); [B77-C04 · Coeficientes de arrastre y sustentación](../programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/CLASE.md).

### Sustentación arriba/abajo

- La sustentación arriba/abajo idealiza el balanceo del vector de sustentación.

🎯 **Por qué importa (clase B77-C25):** El corredor es la tolerancia que se le deja a la navegación y a la guía antes de entrar. La decisión central: ¿entre qué ángulos puede entrar el vehículo, cuánto ensancha el corredor la sustentación y cuándo falla la estimación de Allen–Eggers?

📘 **Dónde se aprende** (1 clase): [B77-C25 · Corredores de entrada y límites de trayectoria](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md).

### Sustitución

- La sustitución (o cambio de variable) reemplaza una expresión `u = g(x)` por una nueva variable; su justificación es la regla de la cadena: `∫ f(g(x)) g′(x) dx = ∫ f(u) du` (S1, §1.4(v), ec. 1.4.28 en forma definida).
- La sustitución despeja una incógnita y la reemplaza en las demás.

💡 **Cómo se explica en la clase [B04-C03](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md):**
- La sustitución es clara en 2×2 y cuando una incógnita queda despejada.
- 🎯 **Por qué importa:** Un detector no entrega «brillo»: entrega cuentas. Para convertir cuentas en flujo hay que descubrir dos números, una pendiente y un desfase, y para ello se miden dos fuentes de referencia.

📘 **Dónde se aprende** (2 clases): [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md); [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md).

### Sustitución hacia atrás

- La sustitución hacia atrás despeja desde la última ecuación.

🎯 **Por qué importa (clase B10-C05):** Para fijar la posición de un objeto a partir de las distancias a tres estaciones se plantean tres ecuaciones con dos incógnitas (plano). Los sistemas reales tienen decenas o miles de incógnitas: parámetros orbitales, sesgos de relojes, coeficientes de calibración.

📘 **Dónde se aprende** (1 clase): [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md).

### Sustituto gratuito

- El sustituto gratuito es un producto sin precio que cubre parte del valor.

💡 **Cómo se explica en la clase [B125-C01](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md):**
- Ninguna de las dos fuentes da precios ni cuotas de mercado: son el contexto de que existe un sustituto gratuito.
- 🎯 **Por qué importa:** [B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) trata los segmentos de la industria en general; ninguna clase explica por qué un dato crudo puede valer cero y aun así sostener empresas.

📘 **Dónde se aprende** (1 clase): [B125-C01 · Mercado de datos espaciales](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md).

### Sustracción del continuo

- La sustracción del continuo con un polinomio de orden `p`.

🎯 **Por qué importa (clase B51-C14):** Una línea débil sobre un continuo brillante solo se ve si la banda está calibrada mejor que la razón línea/continuo. La decisión central: ¿cuánto ruido inyecta la solución de banda y por qué no basta con restar un polinomio?

📘 **Dónde se aprende** (1 clase): [B51-C14 · Calibración de banda en la reducción de datos de síntesis](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md).

### Sustrato

- El sustrato retiene agua según su profundidad y porosidad.

💡 **Cómo se explica en la clase [B59-C14](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md):**
- Un sustrato de 0,20 m y porosidad 0,5 almacena `100 kg/m²`: se seca en `33,3 días` sin riego.
- 🎯 **Por qué importa:** Cultivar exige luz, y la luz eléctrica cuesta potencia. La decisión central: ¿cuántos metros cuadrados y cuántos kilovatios necesita un cultivo para producir el oxígeno de una persona?

📘 **Dónde se aprende** (1 clase): [B59-C14 · Agricultura y sustratos artificiales](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md).

### SVD

- La SVD de una matriz real `A` de `m × n` es `A = U Σ Vᵀ`, con `U` (`m × m`, o `m × r` en la versión «económica») y `V` (`n × n`) de columnas ortonormales, y `Σ` diagonal con los valores singulares `σ₁ ≥ σ₂ ≥ … ≥ 0`.
- La solución por SVD usa `B = Σ bᵢ rᵢᵀ = U S Vᵀ` y `A = U diag(1,1,det) Vᵀ`.

💡 **Cómo se explica en la clase [B10-C11](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md):**
- La SVD nunca engaña, pero hay que elegir el umbral.
- Ninguno es dato real; sirven para ver qué dice la SVD.
- 🎯 **Por qué importa:** Un instrumento entrega una imagen de miles de píxeles; la mayor parte de su estructura se puede describir con muy pocos patrones. Una matriz de medidas puede tener columnas casi redundantes, de modo que un cálculo «técnicamente posible» sea inútil.

📘 **Dónde se aprende** (2 clases): [B10-C11 · Valores singulares y SVD](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md); [B74-C14 · Navegación con cámaras estelares](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md).

### SVD de Wahba

- El SVD de Wahba factoriza `B = Σ w_i b_i r_iᵀ = U S Vᵀ` y toma `A = U diag(1, 1, det U det V) Vᵀ`.

🎯 **Por qué importa (clase B87-C09):** Cada sensor de vector da solo dos grados de libertad; la actitud completa exige combinarlos. La decisión central: ¿qué método usar, cómo ponderar el sensor mejor y cuánto importa el ángulo entre los vectores?

📘 **Dónde se aprende** (1 clase): [B87-C09 · Estimación de actitud](../programa/clases/B87/B87-C09-estimacion-de-actitud/CLASE.md).

### SWEG

- SMAC: concentración máxima permitida en nave. SWEG: guía de agua potable.

💡 **Cómo se explica en la clase [B106-C24](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md):**
- La página consultada dice qué son los SMAC y quién los fija; no da valores (los oficiales están en JSC 20584 y los de agua, SWEG, en JSC 63414).
- 🎯 **Por qué importa:** Evaluar el aire exige límites y una regla para combinar contaminantes; ninguno basta por sí solo. La decisión central: ¿cumple una mezcla de contaminantes su límite combinado y qué compuesto la domina?

📘 **Dónde se aprende** (1 clase): [B106-C24 · Calidad del aire y límites de exposición en cabina](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md).
