# Términos · S (parte 2 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · **S** · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-s.md) · **2**

### Sobreexpandida

- La tobera adaptada tiene `p_e = p_a`; sobreexpandida, `p_e < p_a`;

💡 **Cómo se explica en la clase [B79-C08](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md):**
- `729272 Pa` es la contrapresión con el choque justo en la salida; entre ese valor y `62686 Pa` hay choques oblicuos fuera (sobreexpandida); y `62686 Pa` es la presión de diseño.
- A nivel del mar (`pa/pe = 1,62`) la tobera de `ε = 10` está sobreexpandida y la de `ε = 25` mucho más; la separación de la capa límite (no modelada) limita la sobreexpansión.
- 🎯 **Por qué importa:** B78-C03 trata la cámara pero no el flujo por la tobera. La teoría de expansión es lo que une la presión de cámara con el empuje.
- 🔗 **Se estudia junto con:** bloqueada, relación de expansión, empuje, coeficiente de empuje.

📘 **Dónde se aprende** (1 clase): [B79-C08 · Flujo en toberas convergente-divergentes](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md).

### Sobreimpulso

- El sobreimpulso `Mp` es cuánto excede la respuesta a su valor final (en fracción), el tiempo de pico `tp` es cuándo ocurre, el tiempo de subida `tr` es el que tarda entre 10 % y 90 % del valor final y el tiempo de asentamiento `ts` es el que tarda en quedar dentro de ±2 % para siempre.
- El sobreimpulso es `exp(−πζ/√(1−ζ²))`.
- El sobreimpulso es el máximo exceso sobre la consigna.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C04](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md):**
- No hay sobreimpulso: la curva se acerca sin pasarse.
- Derivando `y(t)` y buscando el primer máximo se obtiene el tiempo de pico `tp = π/ωd` y el sobreimpulso `Mp = exp(−π ζ/√(1 − ζ²))`; solo dependen de `ζ`.
- 🎯 **Por qué importa:** Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación.
- 🔗 **Se estudia junto con:** respuesta transitoria, estacionaria, constante de tiempo, frecuencia natural.

📘 **Dónde se aprende** (8 clases): [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B43-C15 · Motores paso a paso y servomotores](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md); [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md); [B85-C10 · Control térmico activo](../programa/clases/B85/B85-C10-control-termico-activo/CLASE.md); [B88-C19 · Simulación hardware-in-the-loop](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md); [B97-C24 · Modelos de actuadores virtuales e integración en simulación](../programa/clases/B97/B97-C24-modelos-de-actuadores-virtuales-e-integracion-en-simulacion/CLASE.md) y 2 más.

### Sobremuestreo

- El sobremuestreo reparte cada píxel grueso en varios finos.

💡 **Cómo se explica en la clase [B57-C05](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md):**
- M["multiespectral gruesa"] --> U["sobremuestreo"]
- 🎯 **Por qué importa:** Con una sola banda el agua oscura, la sombra y el asfalto se confunden; con varias, cada cubierta deja una firma distinta. La decisión central: ¿qué combinación de bandas separa las cubiertas que me interesan y cómo recupero detalle espacial sin falsear los colores?
- 🔗 **Se estudia junto con:** banda, composición, falso color, razón de bandas.

📘 **Dónde se aprende** (1 clase): [B57-C05 · Imágenes multiespectrales](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md).

### Sobreparametrización

- La sobreparametrización es usar más parámetros de los que los datos sostienen.
- La sobreparametrización usa más parámetros de los que los datos sostienen (C16).

💡 **Cómo se explica en la clase [B15-C16](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md):**
- Hay que comparar modelos alternativos, vigilar la sobreparametrización y declarar los supuestos del ruido.
- 🎯 **Por qué importa:** En C01 una recta ajustada a 2,8 periodos de una oscilación dio una pendiente de −2,24 × 10⁻⁴ por día cuando la real era −1,00 × 10⁻⁴: el modelo estaba mal planteado.
- 🔗 **Se estudia junto con:** modelo, parámetros, residuo, Mínimos cuadrados.

📘 **Dónde se aprende** (2 clases): [B15-C16 · Ajuste de curvas](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md); [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md).

### Sobrepresión

- La sobrepresión es la presión por encima de la hidrostática del hielo.

💡 **Cómo se explica en la clase [B70-C06](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md):**
- *Descripción textual:* la masa y el radio fijan la gravedad; esta da la sobrepresión; la temperatura del gas da la velocidad del chorro, que se compara con la de escape.
- Obtener la sobrepresión `(ρ_w − ρ_i) g h`.
- 🎯 **Por qué importa:** El agua líquida es más densa que el hielo, así que no sube sola. La decisión central: ¿qué presión extra y qué mecanismo hacen falta para que el agua llegue a la superficie?
- 🔗 **Se estudia junto con:** criovulcanismo, criomagma, flujo estrangulado, velocidad de escape.

📘 **Dónde se aprende** (1 clase): [B70-C06 · Criovulcanismo: lavas heladas y emisión de volátiles](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md).

### Sobresuscripción

- Cuota: fracción pactada. Sobresuscripción: horas pedidas entre horas disponibles.

💡 **Cómo se explica en la clase [B48-C02](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md):**
- Calcular la presión de sobresuscripción.
- 🎯 **Por qué importa:** Un reparto sin regla clara genera conflicto, y uno sin clima genera promesas incumplibles. La decisión central: ¿cuántas horas se asignan y cuántas se esperan efectivas?
- 🔗 **Se estudia junto con:** Cuota, Método de Hamilton, Método de D'Hondt, Horas efectivas.

📘 **Dónde se aprende** (1 clase): [B48-C02 · Concesión de tiempo de observación](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md).

### Sobre-triage

- Sub-triage: caso asignado a una categoría menos urgente que la verdadera; sobre-triage: a una más urgente.

💡 **Cómo se explica en la clase [B116-C04](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md):**
- El ruido del sensor produce sobre-triage de personas estables, con el coste de alertas y consultas, más que sub-triage.
- Por errores: matriz, sub y sobre-triage.
- 🎯 **Por qué importa:** Un puntaje simple ayuda a decidir rápido y de forma homogénea, pero un fallo por defecto (sub-triage) deja sin atender a quien lo necesita y uno por exceso (sobre-triage) agota recursos y atención. Y si la respuesta de tierra tarda decenas de minutos, no se puede esperar a tierra para lo que no admite espera.
- 🔗 **Se estudia junto con:** Triage, puntaje de alerta temprana, categoría, Sub-triage.

📘 **Dónde se aprende** (1 clase): [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Sobrevive

- Un mutante es una copia de la IUT con un defecto inyectado; está muerto si alguna prueba falla y sobrevive si todas pasan.

💡 **Cómo se explica en la clase [B94-C06](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md):**
- Uno que no cambia el comportamiento observable, por ejemplo reordenar dos instrucciones independientes: sobrevive sin ser un hueco de la suite.
- pad_ff relleno con 0xFF en vez de 0x00 -> SOBREVIVE
- 🎯 **Por qué importa:** Una implementación que «funciona con la mía» puede fallar con otra. La decisión central: ¿qué pruebas demuestran que cada requisito se cumple y cómo sabes que tu suite detectaría un defecto?
- 🔗 **Se estudia junto con:** conformidad, implementación bajo prueba, vector de prueba, oráculo.

📘 **Dónde se aprende** (1 clase): [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Sobrevivir

- Un límite de replicación es el valor de una variable por debajo (o encima) del cual no hay división celular. Sobrevivir es conservar la viabilidad sin dividirse;

💡 **Cómo se explica en la clase [B56-C05](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md):**
- Distinguir sobrevivir, metabolizar y replicarse.
- Ejercicio 6. ¿Qué diferencia hay entre sobrevivir y replicarse en un ambiente a −40 °C?
- ⚠️ **Error frecuente:** Confundir sobrevivir con replicarse. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Decidir si un ambiente es habitable, o si una nave puede contaminarlo, exige umbrales de temperatura y de agua disponible. La decisión central: dada la temperatura y la actividad del agua de un ambiente, ¿está dentro de los límites en que la vida terrestre puede replicarse?
- 🔗 **Se estudia junto con:** extremófilo, actividad del agua, temperatura cardinal, límite de replicación.

📘 **Dónde se aprende** (1 clase): [B56-C05 · Extremófilos y límites ambientales](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md).

### Sobrevuelo

- Un sobrevuelo (o asistencia gravitacional) es el paso de una nave cerca de un planeta.
- Un sobrevuelo termina cuando la nave sale de ella.

💡 **Cómo se explica en la clase [B75-C06](../programa/clases/B75/B75-C06-asistencias-gravitacionales/CLASE.md):**
- (3) RK4 y Kepler coinciden tras 20 d de sobrevuelo (menos de 10 km).
- Por RK4: integra el sobrevuelo directamente.
- 🎯 **Por qué importa:** Un cohete que sale de la Tierra no puede llevar combustible para ir a Júpiter con una trayectoria directa de baja energía y además frenar. La decisión central: ¿cuánta velocidad heliocéntrica puede ganar o perder una nave pasando cerca de un planeta, y de qué depende?
- 🔗 **Se estudia junto con:** ángulo de giro, periapsis, acelerador, frenador.

📘 **Dónde se aprende** (2 clases): [B75-C06 · Asistencias gravitacionales](../programa/clases/B75/B75-C06-asistencias-gravitacionales/CLASE.md); [B75-C07 · Sobrevuelos planetarios](../programa/clases/B75/B75-C07-sobrevuelos-planetarios/CLASE.md).

### SOC

- SOC: estado de carga.

💡 **Cómo se explica en la clase [B96-C12](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md):**
- Por simulación: SOC a lo largo del tiempo (esta clase).
- El script [balance_de_energia.py](balance_de_energia.py) simula el SOC de la batería durante 30 órbitas con cuatro planes de operación, calcula la DoD máxima y la contrasta con la fórmula analítica;
- 🎯 **Por qué importa:** Una batería descargada en exceso se degrada y una nave sin energía deja de ser comandable. La decisión central: ¿qué plan de operación mantiene la batería dentro de su criterio de descarga y recupera la carga en cada órbita?
- 🔗 **Se estudia junto con:** DoD, Carga base, Balance neto, Eficiencia de carga.

📘 **Dónde se aprende** (1 clase): [B96-C12 · Gestión de energía en operaciones](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md).

### SOC mínimo

- El SOC mínimo es el menor estado de carga del periodo simulado.

💡 **Cómo se explica en la clase [B86-C20](../programa/clases/B86/B86-C20-simulacion-de-ciclo-energetico-orbital/CLASE.md):**
- El SOC mínimo ocurre en el caso B en la órbita `447`: donde la combinación de `β`, degradación y carga extra es menos favorable.
- *Descripción textual:* `β` fija el eclipse y el coseno del ala; con la degradación da la generación; en cada paso el balance con las cargas determina la batería, la energía descartada y las pérdidas; de ahí salen el SOC mínimo y el cierre del balance.
- 🎯 **Por qué importa:** Los cálculos por órbita aislada no ven que `β` cambia día a día ni que la degradación se acumula. Una simulación larga revela el peor día y comprueba que la energía se conserva en todo el recorrido.
- 🔗 **Se estudia junto con:** simulación acoplada, paso de tiempo, generación descartada, cierre del balance.

📘 **Dónde se aprende** (1 clase): [B86-C20 · Simulación de ciclo energético orbital](../programa/clases/B86/B86-C20-simulacion-de-ciclo-energetico-orbital/CLASE.md).

### Sociedad de beneficio público

- Una sociedad de beneficio público debe equilibrar el interés de sus accionistas con un beneficio público declarado.

💡 **Cómo se explica en la clase [B125-C03](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Qué tensión introduce una sociedad de beneficio público en las decisiones de un consejo?
- 🎯 **Por qué importa:** Las decisiones de una empresa se estructuran en su gobierno y, en el espacio, el capital intensivo hace que quien controla la votación controle el rumbo de misiones de años; ninguna clase lo trata.
- 🔗 **Se estudia junto con:** clase de acciones, poder de voto, consejo, cuota.

📘 **Dónde se aprende** (1 clase): [B125-C03 · Gobierno corporativo de una empresa espacial](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md).

### Sodio

- La capa de sodio y la retrodispersión Rayleigh.

💡 **Cómo se explica en la clase [B42-C17](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md):**
- El cociente Rayleigh/sodio es `37,87` (límite `9^{5/3} = 38,9`; menor porque parte de la turbulencia está sobre 10 km y se trunca).
- Con apertura de 8 m y el perfil de la clase C12 (ilustrativo), el error de cono sin quitar piston ni inclinación es `77,34 rad²` para una Rayleigh a 10 km y `2,04 rad²` para sodio a 90 km; una subapertura a 8 m del lanzador ve la mancha alargada `2,04 arcsec`.
- 🎯 **Por qué importa:** Sin estrella guía no hay corrección en casi todo el cielo. La decisión central: ¿a qué altitud conviene crear la estrella y qué error de cono y qué elongación trae?
- 🔗 **Se estudia junto con:** estrella guía láser, efecto cono, altitud, retrodispersión Rayleigh.

📘 **Dónde se aprende** (1 clase): [B42-C17 · Estrellas guía artificiales](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md).

### Sol

- El Sol sirve de referencia: `Z☉ = 0,0134` (fotosfera, S1).

💡 **Cómo se explica en la clase [B25-C17](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md):**
- En el Sol: `X + Y + Z = 0,7381 + 0,2485 + 0,0134 = 1,0000`, y `Z/X = 0,0181`.
- En dex, una galaxia con `Z = 0,0069` está a `−0,29 dex` del Sol.
- 🎯 **Por qué importa:** Cada generación de estrellas fabrica elementos pesados y los devuelve al gas; la proporción de metales de una galaxia cuenta cuánto se ha procesado su gas. En astronomía, «metales» son todos los elementos más pesados que el helio.
- 🔗 **Se estudia junto con:** metalicidad, logarítmica, fracción de gas, rendimiento.

📘 **Dónde se aprende** (1 clase): [B25-C17 · Metalicidad y evolución química](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md).

### Sol marciano

- Arrastre: sincronización con la luz. Sol marciano: día solar de Marte.

💡 **Cómo se explica en la clase [B106-C13](../programa/clases/B106/B106-C13-iluminacion-y-ciclos-circadianos/CLASE.md):**
- Paso 4. Retraso de un sol marciano sin ajuste: `0,66 h/día`; en 30 días, `19,8 h`.
- El sol marciano mide 24,6597 h y acumula 19,8 h de retraso en 30 días si no hay ajuste.
- ⚠️ **Error frecuente:** Ignorar el retraso del sol marciano. Ver 8.5.
- 🎯 **Por qué importa:** El reloj interno no mide exactamente 24 h; la luz lo corrige. Un hábitat con otra duración de día pide programar la luz.
- 🔗 **Se estudia junto con:** Ritmo circadiano, Periodo intrínseco, Arrastre, Ecuación de Adler.

📘 **Dónde se aprende** (1 clase): [B106-C13 · Iluminación y ciclos circadianos](../programa/clases/B106/B106-C13-iluminacion-y-ciclos-circadianos/CLASE.md).

### Solapamiento

- Un solapamiento es un intervalo en el que dos comandan.

💡 **Cómo se explica en la clase [B42-C07](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md):**
- Con una pupila de 32 píxeles en malla de 128 (ilustrativos) la MTF a `v = 0,5` es `0,39409` (FFT y autocorrelación) frente a `0,39100` analítica, y al submuestrear la PSF a 1 píxel por `λ/D` la OTF medida a `v = 0,5` sube a `0,78818` por el solapamiento.
- Predecir el solapamiento por submuestreo.
- 🎯 **Por qué importa:** La OTF dice qué detalles (frecuencias espaciales) pasan por el sistema y cuáles se pierden; fija el muestreo necesario del detector. La decisión central: ¿hasta qué frecuencia transmite el telescopio y qué muestreo exige?
- 🔗 **Se estudia junto con:** OTF, MTF, frecuencia de corte, autocorrelación.

📘 **Dónde se aprende** (2 clases): [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md); [B98-C08 · Protocolos de relevo de control entre operadores](../programa/clases/B98/B98-C08-protocolos-de-relevo-de-control-entre-operadores/CLASE.md).

### Solape

- El solape es la fracción de celdas prioritarias comunes a dos mapas.

💡 **Cómo se explica en la clase [B57-C19](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md):**
- Perturbando cada peso hasta ±20 %, el solape con el mapa base del 10 % prioritario tiene mínimo `94,4%` y media `97,8%`.
- Medir el solape entre dos métodos de combinación.
- 🎯 **Por qué importa:** Los mapas de riesgo orientan decisiones y presupuestos, pero dependen de supuestos de ponderación que suelen quedar ocultos. La decisión central: ¿cómo combino capas y cuánto cambian las zonas prioritarias si cambio los pesos?
- 🔗 **Se estudia junto con:** amenaza, exposición, vulnerabilidad, proceso analítico jerárquico (AHP).

📘 **Dónde se aprende** (1 clase): [B57-C19 · SIG y análisis de riesgo](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md).

### Solar

- Un eclipse solar ocurre cuando la Luna se interpone entre el Sol y la Tierra (Luna nueva); uno lunar, cuando la Tierra se interpone entre el Sol y la Luna (Luna llena).

💡 **Cómo se explica en la clase [B08-C09](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md):**
- El modelo del laboratorio usa un criterio geométrico: habrá algún eclipse solar, al menos parcial en algún lugar, si la separación Luna–Sol en la luna nueva es menor que la suma de sus radios angulares más la paralaje de la Luna (≈ 0,95°), es decir, unos 1,4°–1,6° según la distancia.
- La tabla de la NASA para 2021–2030 (S1) marca como visibles desde el sur de Sudamérica los siguientes eclipses solares: parcial del 30 de abril de 2022 (sudeste del Pacífico y sur de Sudamérica); anular del 14 de octubre de 2023 (Norteamérica, Centroamérica y Sudamérica, con la trayectoria central por Colombia y Brasil);
- 🎯 **Por qué importa:** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?
- 🔗 **Se estudia junto con:** umbra, penumbra, lunar, total.

📖 **Explicado a fondo:** [Tiempo sidéreo y solar](esencial/esencial-m-z.md#tiempo-sidéreo-y-solar) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md).

### Solicitación general

- La solicitación general es ofrecer valores al público; la regulan normas que esta clase no desarrolla.

💡 **Cómo se explica en la clase [B126-C06](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md):**
- Consultar a un abogado: la página de la SEC distingue ofertas con y sin solicitación general y esta clase no basta para decidirlo.
- 🎯 **Por qué importa:** [B124-C19](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) redacta propuestas de misión, no financieras. La decisión central: ¿qué cifra se muestra, con qué rótulo y con qué rango, de modo que un tercero pueda comprobarla?
- 🔗 **Se estudia junto con:** matriz de evidencia, rótulo, trazable, rango de incertidumbre.

📘 **Dónde se aprende** (1 clase): [B126-C06 · Presentación financiera ante inversionistas con evidencia](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md).

### Solicitud de cambio

- Una solicitud de cambio (CR) propone un cambio; la CCB la decide tras un análisis de impacto.

💡 **Cómo se explica en la clase [B83-C15](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md):**
- R["Solicitud de cambio"] --> I["Impacto aguas abajo"]
- *Descripción textual:* los elementos se resumen con huellas y forman la línea base; la comparación con el estado actual detecta deriva; una solicitud de cambio genera un impacto y una clase que la CCB decide.
- 🎯 **Por qué importa:** Si nadie sabe qué versión de qué documento se ensayó, no se puede demostrar nada. La decisión central: ¿la configuración actual es la aprobada, y qué se afecta si apruebo este cambio?
- 🔗 **Se estudia junto con:** elemento de configuración, línea base, huella, deriva.

📘 **Dónde se aprende** (1 clase): [B83-C15 · Gestión de configuración](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md).

### Solidaridad

- La solidaridad permite cobrar el total a cualquiera.

💡 **Cómo se explica en la clase [B119-C03](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md):**
- III cubre los daños en el espacio con responsabilidad por culpa, con solidaridad cuando dos objetos de distintos Estados dañan a un tercero.
- Calcular el pago de cada Estado frente a la víctima bajo solidaridad, también con un Estado insolvente.
- 🎯 **Por qué importa:** El art. VII del tratado de 1967 (no discutido en la fuente de C01) fundamenta la responsabilidad; el convenio de 1972 la desarrolla, y la cuantificación del daño se trata en el bloque de reclamaciones (B123); esta clase fija la regla de reparto.
- 🔗 **Se estudia junto con:** responsabilidad absoluta, responsabilidad por culpa, cuota interna, regreso.

📘 **Dónde se aprende** (2 clases): [B119-C03 · Convenio de Responsabilidad](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md); [B123-C02 · Causalidad y atribución jurídica del daño](../programa/clases/B123/B123-C02-causalidad-y-atribucion-juridica-del-dano/CLASE.md).

### Sólido

- En un sólido las partículas ocupan posiciones casi fijas; en un líquido están juntas pero se deslizan; en un gas están lejos y se mueven libres; en un plasma el gas está parcialmente o totalmente ionizado, es decir, hay electrones libres e iones.

💡 **Cómo se explica en la clase [B06-C10](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md):**
- Sólido, líquido y gas se distinguen por el orden y la distancia entre partículas.
- A["ε / kT muy grande (≫ 14)"] --> S["Sólido: partículas casi fijas"]
- 🎯 **Por qué importa:** En Marte, la temperatura media es 214 K y la presión media en superficie 6,36 mb (S1). Ese valor está casi en el punto triple del agua, la presión mínima a la que puede existir agua líquida (S2).
- 🔗 **Se estudia junto con:** materia, estados, líquido, gas.

📘 **Dónde se aprende** (1 clase): [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md).

### Sólido de revolución

- Un sólido de revolución se genera al girar una curva en torno a un eje.

💡 **Cómo se explica en la clase [B09-C13](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md):**
- Calcular el volumen de un sólido de revolución por discos y por cascarones.
- 🎯 **Por qué importa:** Un telescopio necesita un espejo con forma de paraboloide. Cuánto vidrio hay que retirar de un disco plano para darle forma, cuánto pesa, y cuánta superficie hay que aluminizar son preguntas de volumen y área.
- 🔗 **Se estudia junto con:** área entre curvas, método de los discos, método de los cascarones, longitud de arco.

📘 **Dónde se aprende** (1 clase): [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md).

### Sólidos y líquidos puros

- Para gases se usan presiones parciales divididas entre una presión estándar `p° = 1 bar`; para disoluciones, concentraciones divididas entre 1 mol/L; los sólidos y líquidos puros no aparecen (su actividad vale 1).

💡 **Contexto en la clase [B06-C13](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md):**
- **Idea central (modelo mental):** Imagina un río con dos canales que se cruzan: uno lleva agua de A hacia B y otro de B hacia A. Si A tiene más agua, fluye más hacia B hasta que los dos flujos se igualan. Entonces los niveles dejan de cambiar, aunque el agua siga circulando.
- 🎯 **Por qué importa:** Según el cálculo de esta clase, el CO₂ de Marte puede condensarse como hielo o volver al gas según la temperatura. Es un equilibrio entre CO₂ sólido y gas: `CO₂(s) ⇌ CO₂(g)`.
- 🔗 **Se estudia junto con:** equilibrio químico, constante de equilibrio, cociente de reacción, actuales.

📘 **Dónde se aprende** (1 clase): [B06-C13 · Equilibrio químico](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md).

### Solo de adición

- Una cadena de huellas hace que cada entrada incluya la huella de la anterior. Solo de adición significa que no se modifica ni borra lo escrito.

💡 **Contexto en la clase [B14-C24](../programa/clases/B14/B14-C24-documentacion-de-hipotesis-y-decisiones-de-analisis/CLASE.md):**
- **Idea central (modelo mental):** Cada entrada contiene la huella de la anterior en su propio contenido. Cambiar una entrada vieja cambia su huella y, con ella, la que la siguiente tenía anotada: el vínculo se rompe desde ahí.
- 🎯 **Por qué importa:** Seis meses después de un análisis, nadie recuerda por qué se excluyeron tres puntos ni cuándo se cambió el modelo. Y un revisor pregunta si la exclusión estaba prevista.
- 🔗 **Se estudia junto con:** hipótesis, decisión, desviación, bitácora.

📘 **Dónde se aprende** (1 clase): [B14-C24 · Documentación de hipótesis y decisiones de análisis](../programa/clases/B14/B14-C24-documentacion-de-hipotesis-y-decisiones-de-analisis/CLASE.md).

### Solo empujan

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B43-C09](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md):**
- **Idea central (modelo mental):** Como una balanza de mercado de tres platos: si el punto de apoyo no está en el centro, un plato carga más que los otros, en proporción directa al desplazamiento.
- 🎯 **Por qué importa:** Una celda que no reparte la carga como se diseñó deforma el espejo. La decisión central: ¿cómo se reparte el peso entre los puntos de apoyo y cuánto cambia si el pivote se desplaza unos milímetros?
- 🔗 **Se estudia junto con:** balanza triangular, pivote, desbalance, soporte lateral.

📘 **Dónde se aprende** (1 clase): [B43-C09 · Celdas y soporte de espejos](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md).

### Solsticio

- El solsticio es el día de mayor o menor altura del Sol; el equinoccio, el día en que `δ = 0`.
- Un solsticio es el momento de máximo alejamiento del Sol respecto del ecuador celeste.

💡 **Cómo se explica en la clase [B01-C11](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md):**
- Por estar inclinado 23,44°, `δ_Sol` oscila entre `−23,44°` en el solsticio de diciembre y `+23,44°` en el de junio.
- Para `φ = −33,45°`: en el solsticio de diciembre, `δ = −23,44°` y `h = 90° − 10,01° = 79,99°`; en el equinoccio, `h = 56,55°`; en el de junio, `h = 33,11°`.
- 🎯 **Por qué importa:** Antes de cualquier telescopio, la humanidad dedujo mucho del cielo a simple vista. Que el Sol «salga» y «se ponga» es una observación; que la Tierra gire es una interpretación (C05) que explica además el movimiento de todas las estrellas.
- 🔗 **Se estudia junto con:** horizonte, cénit, meridiano, altura.

📖 **Explicado a fondo:** [Equinoccio y solsticio](esencial/esencial-d-l.md#equinoccio-y-solsticio) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md).

### Solución

- Una solución es el valor que hace cierta la igualdad.
- Su solución es el conjunto de valores que cumple todas las ecuaciones.
- Una solución es una función que, sustituida, hace cierta la ecuación en todo un intervalo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C14](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md):**
- Todo despeje se comprueba de tres maneras: (1) sustituir la solución en la ecuación original;
- El límite: una balanza no distingue entre pesos negativos; en una ecuación hay operaciones que no se pueden aplicar siempre (dividir entre cero, elevar al cuadrado puede introducir soluciones espurias).
- 🎯 **Por qué importa:** La fórmula de la velocidad de escape, `v = √(2GM/R)`, aparece en las fichas de la NASA como un número (11,186 km/s). Pero un ingeniero puede necesitar lo contrario: dado `v`, ¿cuál es el radio?
- 🔗 **Se estudia junto con:** ecuación, incógnitas, Resolver, despejar.

📘 **Dónde se aprende** (4 clases): [B03-C14 · Despeje de ecuaciones elementales](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md); [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md); [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md); [B26-C23 · Tensiones observacionales: constante de Hubble y S8](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md).

### Solución a validar

- La solución a validar es el producto cuya calidad se mide.

💡 **Contexto en la clase [B74-C20](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md):**
- 🎯 **Por qué importa:** Una solución que ajusta bien sus datos puede predecir pésimamente. La decisión central: ¿dentro de qué tolerancia coincide mi solución con la referencia, en qué componente falla y qué modelo falta?
- 🔗 **Se estudia junto con:** efeméride de referencia, diferencia RTN, arco de ajuste, predicción.

📘 **Dónde se aprende** (1 clase): [B74-C20 · Validación frente a efemérides de referencia](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md).

### Solución analítica

- Una solución analítica (o *exacta*) es una expresión cerrada que satisface las ecuaciones del modelo.

💡 **Cómo se explica en la clase [B23-C03](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md):**
- Una solución analítica es la herramienta natural para ese registro: define en qué parámetros el código se ha comparado con la verdad.
- ¿Qué solución analítica usas y qué orden esperas de un integrador de Euler?
- 🎯 **Por qué importa:** Un integrador de órbitas puede conservar la energía, ser reversible e invariante ante rotaciones y aun así describir un Sol con otra masa o una ley de fuerza distinta. Para detectarlo necesitas una referencia con valores: «tras exactamente un período, el planeta vuelve a su punto de partida».
- 🔗 **Se estudia junto con:** error global, orden nominal, orden observado, régimen asintótico.

📘 **Dónde se aprende** (1 clase): [B23-C03 · Casos analíticos de validación](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md).

### Solución de banda

- La solución de banda (*bandpass solution*).

💡 **Cómo se explica en la clase [B51-C14](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md):**
- Con un calibrador de 5,0 Jy, 20 muestras por solución y ruido de 0,05 Jy (sintéticos), la banda inyecta 1,38 mJy de ruido en el blanco (fórmula 1,38 mJy).
- La solución promediada deja un error residual por cada intervalo; hay que resolver la banda más seguido.
- 🎯 **Por qué importa:** Una línea débil sobre un continuo brillante solo se ve si la banda está calibrada mejor que la razón línea/continuo. La decisión central: ¿cuánto ruido inyecta la solución de banda y por qué no basta con restar un polinomio?
- 🔗 **Se estudia junto con:** calibrador de banda, sustracción del continuo, canales libres de línea, ruido inyectado.

📘 **Dónde se aprende** (1 clase): [B51-C14 · Calibración de banda en la reducción de datos de síntesis](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md).

### Solución de dispersión

- La solución de dispersión `λ(x)`.

💡 **Contexto en la clase [B45-C08](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md):**
- **Idea central (modelo mental):** Como graduar una regla con unas pocas marcas conocidas: entre marcas es fiable; fuera de ellas, la curva se desmanda.
- 🎯 **Por qué importa:** Un error de calibración es un error de velocidad o de identificación de líneas. La decisión central: ¿qué grado del polinomio es adecuado y cuánto se puede fiar el ajuste fuera de las líneas?
- 🔗 **Se estudia junto con:** línea de lámpara, centroide, RMS, validación cruzada.

📘 **Dónde se aprende** (1 clase): [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md).

### Solución de energía mínima

- La solución de energía mínima tiene `a = s/2`.

💡 **Contexto en la clase [B75-C04](../programa/clases/B75/B75-C04-ecuacion-de-lambert/CLASE.md):**
- 🎯 **Por qué importa:** Con ventanas fijas solo se calcula el caso ideal. Para cualquier fecha de salida y llegada hace falta resolver la geometría entre dos posiciones.
- 🔗 **Se estudia junto con:** problema de Lambert, cuerda, semiperímetro, ángulo de transferencia.

📘 **Dónde se aprende** (1 clase): [B75-C04 · Ecuación de Lambert](../programa/clases/B75/B75-C04-ecuacion-de-lambert/CLASE.md).

### Solución de fase sola

- La solución de fase sola frente a amplitud y fase.

💡 **Contexto en la clase [B51-C06](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md):**
- **Idea central (modelo mental):** Como afinar un piano escuchando una melodía que no conoces del todo: primero ajustas lo grueso con lo que sí reconoces, escribes mejor la melodía y vuelves a afinar; cada vuelta mejora ambas cosas.
- 🎯 **Por qué importa:** Sin autocalibración, los errores de ganancia de la atmósfera limitan el rango dinámico. La decisión central: ¿converge el ciclo modelo–ganancias, a qué valor y con qué sesgo?
- 🔗 **Se estudia junto con:** autocalibración, modelo de cielo, imagen sucia, haz sucio.

📘 **Dónde se aprende** (1 clase): [B51-C06 · Autocalibración iterativa con modelo de cielo](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md).

### Solución de ganancias

- La solución de ganancias estima `g_i` de un calibrador.

💡 **Contexto en la clase [B46-C17](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md):**
- **Idea central (modelo mental):** Cada músico desafina un poco; afinando con una nota de referencia cada cierto tiempo, el desajuste queda acotado por cuánto se desafina entre afinaciones.
- 🎯 **Por qué importa:** Sin calibrar, la fase de la visibilidad no contiene el cielo. La decisión central: ¿cada cuánto hay que observar el calibrador para que el residuo no destruya la coherencia?
- 🔗 **Se estudia junto con:** ganancia compleja, fase de cierre, referencia de fase, marcha aleatoria.

📘 **Dónde se aprende** (1 clase): [B46-C17 · Calibración de fase](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md).

### Solución de Kirsch

- La solución de Kirsch da `σ_θθ = σ/2[(1 + a²/r²) − (1 + 3a⁴/r⁴) cos 2θ]`.

💡 **Contexto en la clase [B84-C29](../programa/clases/B84/B84-C29-concentraciones-de-tension-y-entallas/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR A["sigma, a"] --> B["Kirsch sigma_tt(r, theta)"] B --> C["Kt = 3 en 90 grados"] B --> D["equilibrio por integral"] C --> E["q, Kf"] E --> F["S_a local, N Basquin"] ``` *Descripción textual:* Kirsch da el campo y el factor teórico; la integral verifica el equilibrio; con la sensibilidad se pasa a `K_f` y a la vida.
- 🎯 **Por qué importa:** Una tensión remota de 100 MPa se triplica a 300 MPa en el borde de un agujero; con `K_f = 2,8` la vida baja de 10¹¹ a 10⁷ ciclos. La decisión central: ¿qué tensión local y qué vida resultan de un agujero en una placa cargada?
- 🔗 **Se estudia junto con:** factor teórico, sensibilidad, factor de fatiga.

📘 **Dónde se aprende** (1 clase): [B84-C29 · Concentraciones de tensión y entallas](../programa/clases/B84/B84-C29-concentraciones-de-tension-y-entallas/CLASE.md).

### Solución de mínimos cuadrados

- La solución de mínimos cuadrados minimiza la suma de los residuos ponderados por `1/σ²`.

💡 **Cómo se explica en la clase [B97-C05](../programa/clases/B97/B97-C05-localizacion-y-mapeo-slam/CLASE.md):**
- El script [deriva_cierre_bucle.py](deriva_cierre_bucle.py) genera una trayectoria con deriva, resuelve el grafo de poses por mínimos cuadrados y compara con la solución analítica (comprueba diferencia < 1e-9 y error de cierre menor que sin corregir).
- 🎯 **Por qué importa:** Sin una corrección, el error de la odometría crece con el recorrido y el mapa se deforma. El cierre de bucle reparte ese error por toda la trayectoria; entender cuánto y cómo evita fiarse de un mapa que se «cierra» solo en apariencia.
- 🔗 **Se estudia junto con:** deriva, grafo de poses, cierre de bucle.

📘 **Dónde se aprende** (1 clase): [B97-C05 · Localización y mapeo SLAM](../programa/clases/B97/B97-C05-localizacion-y-mapeo-slam/CLASE.md).

### Solución de Nash

- La solución de Nash maximiza el producto de las ganancias sobre el desacuerdo.

💡 **Cómo se explica en la clase [B119-C27](../programa/clases/B119/B119-C27-diplomacia-y-comunicacion-entre-estados-ante-incidentes-espaciales/CLASE.md):**
- D["Puntos de desacuerdo d1, d2"] --> N["Solución de Nash"]
- *Descripción textual:* los puntos de desacuerdo dan la solución de Nash; los descuentos dan la solución de Rubinstein; ambas producen un reparto y se analiza su sensibilidad.
- 🎯 **Por qué importa:** C20 simula la respuesta institucional interna; la diplomacia entre Estados no está cubierta. Esta clase aporta el razonamiento básico de negociación sin pretender describir ninguna práctica.
- 🔗 **Se estudia junto con:** ofertas alternadas, factor de descuento, inducción hacia atrás.

📘 **Dónde se aprende** (1 clase): [B119-C27 · Diplomacia y comunicación entre Estados ante incidentes espaciales](../programa/clases/B119/B119-C27-diplomacia-y-comunicacion-entre-estados-ante-incidentes-espaciales/CLASE.md).

### Solución de Sedov–Taylor

- La solución de Sedov–Taylor describe la expansión autosemejante de una explosión intensa.

💡 **Contexto en la clase [B58-C16](../programa/clases/B58/B58-C16-consecuencias-geofisicas-de-impactos/CLASE.md):**
- 🎯 **Por qué importa:** Las consecuencias se miden por zonas: sismo, onda de choque, calor. Las escalas con la energía son lo que permite comparar casos.
- 🔗 **Se estudia junto con:** magnitud sísmica equivalente, Mach, relaciones de Rankine–Hugoniot, radio de Mach 2.

📘 **Dónde se aprende** (1 clase): [B58-C16 · Consecuencias geofísicas de impactos](../programa/clases/B58/B58-C16-consecuencias-geofisicas-de-impactos/CLASE.md).

### Solución de semejanza

- Una solución de semejanza conserva su forma al reescalar.

💡 **Cómo se explica en la clase [B52-C09](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md):**
- Descripción larga: el esquema reproduce la solución de semejanza con error de millonésimas y la acreción viscosa cae al nivel de la fotoevaporación en unos pocos millones de años del modelo.
- Contrastar con la solución de semejanza y con el cambio de paso.
- 🎯 **Por qué importa:** La vida del gas fija cuánto tiempo hay para formar núcleos, gigantes y migración. La decisión central: ¿cuánto tarda un disco en perder su gas y cómo se comprueba un esquema numérico de difusión?
- 🔗 **Se estudia junto con:** viscosidad, escala viscosa, fotoevaporación, Crank–Nicolson.

📘 **Dónde se aprende** (1 clase): [B52-C09 · Dispersión de discos de gas](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md).

### Solución fabricada

- Una solución fabricada es una función elegida arbitrariamente (pero suave y con derivadas conocidas) que se declara solución.

💡 **Cómo se explica en la clase [B23-C04](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md):**
- Las fronteras no son triviales (varían en el tiempo y no son cero); una solución fabricada con fronteras cero esconde errores de fronteras.
- El error respecto de la solución fabricada es `3,0 × 10⁻³ K`: es el error espacial, mucho mayor, idéntico en ambos códigos porque comparten la discretización.
- 🎯 **Por qué importa:** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.
- 🔗 **Se estudia junto con:** término fuente, condiciones de frontera, estudio de refinamiento, nodo fantasma.

📘 **Dónde se aprende** (1 clase): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md).

### Solución general

- La solución general contiene constantes libres; una solución particular fija esas constantes.

💡 **Cómo se explica en la clase [B11-C01](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md):**
- Esta es una solución *particular*: la general incluye elipses y otras posiciones iniciales (C02, C04).
- Por ser de segundo orden, su solución general tiene dos constantes libres (8.2).
- 🎯 **Por qué importa:** Casi ninguna ley de la mecánica espacial nos dice *dónde está* un satélite; nos dice *cómo cambia* su movimiento: la aceleración depende de la posición. Eso es una ecuación diferencial.
- 🔗 **Se estudia junto con:** ecuación diferencial, ordinaria, orden, lineal.

📘 **Dónde se aprende** (1 clase): [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md).

### Solución madre

- La solución madre es una solución concentrada que se diluye al preparar.

💡 **Cómo se explica en la clase [B115-C03](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md):**
- S["soluciones madre<br/>1 M"] --> R["depósito 40 L<br/>solución objetivo"]
- *Descripción textual:* las soluciones madre y el agua llenan el depósito; las plantas absorben cada ion a su ritmo; un sensor mide y una regla decide cuánta solución madre añadir.
- 🎯 **Por qué importa:** Una solución nutritiva que se repone «por conductividad» puede parecer estable y estar desequilibrada. La decisión central: ¿qué se mide, cada cuánto y qué se repone para que cada ion se mantenga cerca de su objetivo, y cuándo conviene renovar la solución?
- 🔗 **Se estudia junto con:** solución nutritiva, macronutrientes, micronutrientes, conductividad eléctrica (EC).

📘 **Dónde se aprende** (1 clase): [B115-C03 · Control de nutrientes y solución nutritiva](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md).

### Solución manufacturada

- Una solución manufacturada es una analítica contra la que se compara.

💡 **Contexto en la clase [B37-C05](../programa/clases/B37/B37-C05-codigos-de-evolucion-estelar-configuracion-verificacion-y-limites/CLASE.md):**
- **Idea central (modelo mental):** Es como medir una curva con reglas cada vez más cortas: si al partir la regla por la mitad el error se divide por 2, 4 o 16, sabes qué tipo de regla tienes.
- 🎯 **Por qué importa:** Un código sin verificación puede dar resultados bonitos y falsos. La decisión central: ¿converge el error con el orden teórico al refinar la malla y el paso de tiempo?
- 🔗 **Se estudia junto con:** Verificar, validar, orden de convergencia, error global.

📘 **Dónde se aprende** (1 clase): [B37-C05 · Códigos de evolución estelar: configuración, verificación y límites](../programa/clases/B37/B37-C05-codigos-de-evolucion-estelar-configuracion-verificacion-y-limites/CLASE.md).

### Solución nutritiva

- La solución nutritiva es agua con los elementos esenciales disueltos.

💡 **Cómo se explica en la clase [B115-C03](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md):**
- La evidencia es la ficha de solución nutritiva con regla de reposición del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de solución nutritiva con regla de reposición*: receta (mM, mg/L, gramos), comprobaciones, EC estimada y su incertidumbre, agotamiento sin control, comparación de las reglas A y B, regla de renovación y lista de qué es consultado, sintético e ilustrativo.
- 🎯 **Por qué importa:** Una solución nutritiva que se repone «por conductividad» puede parecer estable y estar desequilibrada. La decisión central: ¿qué se mide, cada cuánto y qué se repone para que cada ion se mantenga cerca de su objetivo, y cuándo conviene renovar la solución?
- 🔗 **Se estudia junto con:** macronutrientes, micronutrientes, solución madre, conductividad eléctrica (EC).

📘 **Dónde se aprende** (1 clase): [B115-C03 · Control de nutrientes y solución nutritiva](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md).

### Solución particular

- La solución general contiene constantes libres; una solución particular fija esas constantes.

💡 **Cómo se explica en la clase [B11-C01](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md):**
- Esta es una solución *particular*: la general incluye elipses y otras posiciones iniciales (C02, C04).
- Una constante libre; con `C = 5` es una solución particular (sección 6).
- 🎯 **Por qué importa:** Casi ninguna ley de la mecánica espacial nos dice *dónde está* un satélite; nos dice *cómo cambia* su movimiento: la aceleración depende de la posición. Eso es una ecuación diferencial.
- 🔗 **Se estudia junto con:** ecuación diferencial, ordinaria, orden, lineal.

📘 **Dónde se aprende** (1 clase): [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md).

### Solución periódica

- La solución periódica de un nodo lineal por tramos iguala `T` al final de un ciclo con `T` al inicio.

💡 **Cómo se explica en la clase [B85-C11](../programa/clases/B85/B85-C11-ciclos-termicos/CLASE.md):**
- El script [ciclos_termicos.py](ciclos_termicos.py) calcula la solución periódica, la contrasta con la integración numérica y estima `N`, la vida y el daño (comprueba numérica frente a analítica a 0,05 K y `ΔT` decreciente con la inercia).
- 🎯 **Por qué importa:** La amplitud térmica de cada ciclo decide la vida por fatiga de soldaduras y uniones, y se reduce con inercia térmica o con calentadores. La decisión central: ¿qué amplitud de ciclo y cuántos ciclos acumula una unión en la misión, y cuánto la reduce la inercia térmica?
- 🔗 **Se estudia junto con:** constante de tiempo, amplitud, ley de Coffin–Manson, regla de Miner.

📘 **Dónde se aprende** (1 clase): [B85-C11 · Ciclos térmicos](../programa/clases/B85/B85-C11-ciclos-termicos/CLASE.md).

### Solución regularizada

- La solución regularizada `x_λ` es el vector que minimiza una suma de dos costes: el desajuste `‖A x − b‖²` (qué tan lejos queda `A x` de los datos) y la penalización `λ² ‖x‖²` (qué tan grande es la solución).

💡 **Cómo se explica en la clase [B22-C02](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md):**
- Cada componente regularizada difiere de la ingenua por el factor `fᵢ < 1`: la solución regularizada está sesgada hacia cero en todas las direcciones.
- Paso 3 · solución regularizada. `x_λ = f · x = 0,7353 × 4 = 2,941`.
- 🎯 **Por qué importa:** Si no puedes confiar en `x = A⁻¹ b` y no puedes bajar el ruido a voluntad, necesitas una regla que ignore lo que los datos no pueden decir. Esa regla debe tener una perilla: cuánto ignorar.
- 🔗 **Se estudia junto con:** desajuste, penalización, parámetro de regularización, forma estándar.

📘 **Dónde se aprende** (1 clase): [B22-C02 · Regularización de Tikhonov](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md).

### Solucionador de Riemann

- Un solucionador de Riemann calcula (exacta o aproximadamente) la solución de ese problema para obtener el flujo.

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- Resolver el problema de Riemann exacto en cada interfaz y en cada paso es caro; por eso se usan solucionadores aproximados.
- B --> C["Solucionador de Riemann<br/>flujo F_{i+½}"]
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.
- 🔗 **Se estudia junto con:** ley de conservación, vector de estado conservado, flujo, celda.

📘 **Dónde se aprende** (1 clase): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md).

### Soluto

- Una disolución es una mezcla homogénea de un soluto en un disolvente; en esta clase, el disolvente es el agua.

💡 **Contexto en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- **Idea central (modelo mental):** Un ácido es quien presta un protón y una base, quien lo recibe. El préstamo no es todo o nada: en un ácido fuerte casi todos los protones se prestan; en uno débil, sólo una fracción, y el equilibrio fija cuántos.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.
- 🔗 **Se estudia junto con:** disolución, disolvente, concentración, molaridad.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Solutos compatibles

- La estrategia «salt-in» equilibra con KCl interno; los solutos compatibles son moléculas orgánicas que no perturban las proteínas.

💡 **Cómo se explica en la clase [B64-C04](../programa/clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md):**
- E --> S["KCl interno (salt-in) o solutos compatibles"]
- *Descripción textual:* la sal y su coeficiente osmótico fijan la actividad del agua; de ella salen la presión osmótica y la condición de equilibrio que la célula cumple con KCl o con solutos compatibles.
- 🎯 **Por qué importa:** En una salmuera concentrada el agua existe pero «no está disponible» del mismo modo. La pregunta motivadora: ¿cuánta sal puede haber en el exterior antes de que el agua deje de bastar para la célula?
- 🔗 **Se estudia junto con:** actividad del agua, molalidad, coeficiente osmótico, presión osmótica.

📘 **Dónde se aprende** (1 clase): [B64-C04 · Halófilos y vida en salmueras](../programa/clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md).

### Solvente

- Un solvente es el medio líquido en que se disuelven y reaccionan las moléculas.

💡 **Cómo se explica en la clase [B56-C06](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md):**
- Que un solvente sea líquido no implica que sustente una química comparable; eso es hipótesis.
- Aplicar el mismo método a un solvente alternativo, el metano.
- ⚠️ **Error frecuente:** Tomar un solvente líquido como habitable. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** «Sigue el agua» es una consigna de la exploración, pero tener hielo o vapor no es tener un líquido. La presión y la temperatura mandan.
- 🔗 **Se estudia junto con:** punto triple, presión de vapor, temperatura de ebullición, calor latente de vaporización.

📘 **Dónde se aprende** (1 clase): [B56-C06 · Agua líquida y solventes alternativos](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md).

### Sombra

- La sombra es la región oscura que el horizonte y la captura de la luz dejan sobre un fondo brillante.
- La sombra es la región oscura del anillo.
- La sombra de una roca de altura `h` bajo el Sol a elevación `e` mide `L = h/tan e`.

💡 **Cómo se explica en la clase [B25-C11](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md):**
- El diámetro de la sombra es `2b_c GM/c² = 6√3 GM/c² = 10,39 GM/c² = 5,196 R_s`, con `R_s = 2GM/c²`.
- Con el anillo de `42 μas` de S1, la distancia implícita es `15,9 Mpc`: es un cálculo propio con el diámetro de la sombra, y no la distancia medida por S1; la incertidumbre relativa combinada es de ~`13 %` (`11 %` de la masa y `7 %` del anillo).
- ⚠️ **Error frecuente:** Equiparar la sombra con el horizonte. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Algunas galaxias tienen en el centro una fuente que supera a todas sus estrellas, y casi todas las galaxias grandes albergan un agujero negro supermasivo. Entender el AGN une el centro de la galaxia, su gas y su evolución.
- 🔗 **Se estudia junto con:** núcleo activo de galaxia (AGN), acreción, eficiencia radiativa, luminosidad de Eddington.

📘 **Dónde se aprende** (3 clases): [B25-C11 · Núcleos activos de galaxias](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md); [B27-C09 · Órbitas en campos fuertes](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md); [B103-C06 · Detección y catalogación de rocas en imágenes de superficie](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md).

### Sombra cilíndrica

- La sombra cilíndrica es el modelo de eclipse más simple.
- La sombra cilíndrica supone rayos paralelos.
- Beta crítico: `asen(R/a)`: sobre él no hay eclipse. Sombra cilíndrica: modelo de sombra sin penumbra.

💡 **Cómo se explica en la clase [B72-C08](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué el modelo de sombra cilíndrica subestima el tiempo en eclipse?
- El script [presion_radiacion.py](presion_radiacion.py) deriva la irradiancia, calcula la aceleración por presión de radiación, mide la sombra cilíndrica con un conteo numérico e integra una órbita geoestacionaria para verificar `e(t)` (comprueba que `e` numérica y teórica difieren menos de `3 %`).
- 🎯 **Por qué importa:** En órbita geoestacionaria no hay arrastre, y el empuje solar domina las maniobras de mantenimiento de un satélite con paneles grandes; en una vela solar es el propulsor. La decisión central: ¿cuánto vale la aceleración por presión de radiación y cuánto deforma una órbita alta en semanas?
- 🔗 **Se estudia junto con:** irradiancia, presión de radiación, coeficiente de reflectividad, excentricidad forzada.

📘 **Dónde se aprende** (3 clases): [B72-C08 · Presión de radiación solar](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md); [B86-C04 · Orientación solar y eclipses](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md); [B96-C11 · Operación durante eclipse](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md).

### Sombra de la Tierra

- La sombra de la Tierra es la región sin luz solar.

💡 **Contexto en la clase [B118-C16](../programa/clases/B118/B118-C16-contaminacion-luminica/CLASE.md):**
- 🎯 **Por qué importa:** El brillo y el número de satélites visibles dependen de la altitud y de la profundidad del Sol bajo el horizonte; para un telescopio, una traza arruina la zona que cruza. La decisión central: ¿cuánto dura la ventana de iluminación, qué tan brillante es el satélite y cuántas trazas esperar en una exposición?
- 🔗 **Se estudia junto con:** profundidad solar, ventana de iluminación, magnitud, traza.

📘 **Dónde se aprende** (1 clase): [B118-C16 · Contaminación lumínica](../programa/clases/B118/B118-C16-contaminacion-luminica/CLASE.md).

### Sombreado

- El sombreado es `cos z cos s + sin z sin s cos(a − o)`.

💡 **Cómo se explica en la clase [B53-C20](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md):**
- *Descripción textual:* El MDE da pendiente y sombreado; la pendiente produce la máscara; la búsqueda da el camino.
- sombreado en el plano inclinado = 0.4877
- 🎯 **Por qué importa:** Un derivado sin verificar propaga errores a la decisión. La decisión central: ¿qué parte del terreno cumple un criterio de pendiente y existe un camino que lo respete?
- 🔗 **Se estudia junto con:** esquema de Horn, máscara de transitabilidad, búsqueda en anchura.

📘 **Dónde se aprende** (1 clase): [B53-C20 · Proyecto SIG de terreno extraterrestre](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md).

### Son láminas reflectantes que reducen la radiación. Un

- El aislamiento multicapa son láminas reflectantes que reducen la radiación. Un refrigerador de cero evaporación extrae el calor que entra.

💡 **Contexto en la clase [B59-C21](../programa/clases/B59/B59-C21-almacenamiento-criogenico-y-aislado-de-volatiles-extraidos/CLASE.md):**
- **Idea central (modelo mental):** Como un termo que deja pasar un poco de calor y pierde hielo: un refrigerador sería una nevera enchufada que lo repone. Límite: el termo no tiene que rechazar el calor a 250 K.
- 🎯 **Por qué importa:** Lo extraído sirve si se conserva. La decisión central: ¿se acepta la evaporación o se paga la potencia de un refrigerador de cero evaporación?
- 🔗 **Se estudia junto con:** es el líquido que se vaporiza por el calor que entra. El, extrae el calor que entra. El, es T_c/(T_h − T_c). La.

📘 **Dónde se aprende** (1 clase): [B59-C21 · Almacenamiento criogénico y aislado de volátiles extraídos](../programa/clases/B59/B59-C21-almacenamiento-criogenico-y-aislado-de-volatiles-extraidos/CLASE.md).

### Sonda

- Una sonda es una nave no tripulada que se aleja de la Tierra.

💡 **Cómo se explica en la clase [B02-C19](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md):**
- C --> D["1977: sondas hacia fuera<br/>(Voyager)"]
- *Descripción textual:* una cadena de hitos técnicos (un objeto, una persona, personas en la Luna, sondas hacia fuera) y dos ramas institucionales: la creación de la NASA en 1958 y el tratado de 1967.
- 🎯 **Por qué importa:** La exploración espacial es una historia científica y también política. La pregunta motivadora es: ¿qué cambió, para la astronomía y para la sociedad, cuando los instrumentos y las personas empezaron a salir de la atmósfera, y qué reglas se acordaron?
- 🔗 **Se estudia junto con:** satélite artificial, órbita baja, duración del vuelo, período orbital.

📘 **Dónde se aprende** (1 clase): [B02-C19 · Historia de la exploración espacial](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md).

### Sondeo

- Adaptador: capa que traduce a una operación común. Sondeo (*polling*): consulta periódica.

💡 **Cómo se explica en la clase [B48-C21](../programa/clases/B48/B48-C21-protocolos-estandar-de-control-instrumental-ascom-e-indi/CLASE.md):**
- El sondeo añade una latencia media de la mitad del periodo; una notificación por eventos la evita.
- Un sondeo cada 1 s detecta un evento con latencia media 0,4997 s (teórica 0,5000).
- ⚠️ **Error frecuente:** Olvidar la latencia del sondeo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Sin una capa común, el software de la noche depende de cada fabricante. La decisión central: ¿cómo se aísla el programa de observación del estilo de cada protocolo?
- 🔗 **Se estudia junto con:** Protocolo, Interfaz, Propiedad, Adaptador.

📘 **Dónde se aprende** (1 clase): [B48-C21 · Protocolos estándar de control instrumental (ASCOM e INDI)](../programa/clases/B48/B48-C21-protocolos-estandar-de-control-instrumental-ascom-e-indi/CLASE.md).

### Sonificación

- La sonificación representa datos con sonido.

💡 **Cómo se explica en la clase [B128-C07](../programa/clases/B128/B128-C07-modelos-tactiles-y-sonificacion/CLASE.md):**
- El script [sonificacion.py](sonificacion.py) genera la curva, las frecuencias, el relieve y un audio WAV en memoria (comprueba la monotonía, la razón de 4, el número de muestras y un hash estable).
- python programa/clases/B128/B128-C07-modelos-tactiles-y-sonificacion/sonificacion.py
- 🎯 **Por qué importa:** Un mapeo sin reglas explícitas engaña: si la escala de tono se estira para que se oiga una caída de 1 %, el oyente puede creer que la caída fue enorme. La decisión central: ¿qué se mapea a qué, con qué escala, y cómo se avisa de la amplificación?
- 🔗 **Se estudia junto con:** mapeo, semitono, relieve, cuantización.

📘 **Dónde se aprende** (1 clase): [B128-C07 · Modelos táctiles y sonificación](../programa/clases/B128/B128-C07-modelos-tactiles-y-sonificacion/CLASE.md).

### Soporte lateral

- El soporte lateral sostiene la componente del peso perpendicular al eje.

💡 **Cómo se explica en la clase [B43-C09](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de celda y soporte*: balanza, desplazamiento y soporte lateral.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de celda y soporte*: balanza, desplazamiento y soporte lateral.
- 🎯 **Por qué importa:** Una celda que no reparte la carga como se diseñó deforma el espejo. La decisión central: ¿cómo se reparte el peso entre los puntos de apoyo y cuánto cambia si el pivote se desplaza unos milímetros?
- 🔗 **Se estudia junto con:** balanza triangular, pivote, desbalance, distribución de coseno.

📘 **Dónde se aprende** (1 clase): [B43-C09 · Celdas y soporte de espejos](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md).

### Sostenibilidad a largo plazo

- La sostenibilidad a largo plazo busca mantener el uso del espacio.

💡 **Cómo se explica en la clase [B118-C19](../programa/clases/B118/B118-C19-sostenibilidad-y-gobernanza-orbital/CLASE.md):**
- Las Directrices de Sostenibilidad a Largo Plazo (2019) solo se conocen por un resumen de búsqueda.
- 🎯 **Por qué importa:** Una norma voluntaria vale lo que se cumple; medir el cumplimiento exige muestras y declarar la incertidumbre. La decisión central: ¿qué se puede afirmar del cumplimiento de un grupo de operadores con una muestra pequeña y qué no?
- 🔗 **Se estudia junto con:** directriz, mitigación, tasa de cumplimiento, bootstrap.

📘 **Dónde se aprende** (1 clase): [B118-C19 · Sostenibilidad y gobernanza orbital](../programa/clases/B118/B118-C19-sostenibilidad-y-gobernanza-orbital/CLASE.md).

### Span

- El span es la potencia total.

💡 **Cómo se explica en la clase [B69-C04](../programa/clases/B69/B69-C04-polarimetria-sar/CLASE.md):**
- Con `k = (Shh + Svv, Shh − Svv, 2Shv)/√2`, los blancos canónicos dan: plano/esfera, `(2, 0, 0)`; diedro a 0°, `(0, 2, 0)`; dipolo horizontal, `(0,5, 0,5, 0)` (span 1).
- El span se conserva: `|k|² = |Shh|² + 2|Shv|² + |Svv|²`.
- 🎯 **Por qué importa:** Con un solo canal no se distingue un suelo desnudo de un edificio. La decisión central: ¿qué mecanismo de dispersión domina en un pixel y qué conclusiones se pueden sacar con seguridad de las potencias de los canales?
- 🔗 **Se estudia junto con:** matriz de dispersión, vector de Pauli, matriz de coherencia, entropía.

📘 **Dónde se aprende** (1 clase): [B69-C04 · Polarimetría SAR](../programa/clases/B69/B69-C04-polarimetria-sar/CLASE.md).

### Spearman–Brown

- La correlación ítem–total corregida correlaciona un ítem con la suma de los demás. Spearman–Brown: `ρ_k = k r̄/(1 + (k − 1) r̄)` con `r̄` la correlación media entre ítems.

💡 **Cómo se explica en la clase [B105-C27](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md):**
- S --> SB["Spearman-Brown:<br/>longitud"]
- *Descripción textual:* las respuestas permiten calcular el alfa, las correlaciones ítem–total y los valores propios; se eliminan los ítems defectuosos, se acompaña el alfa de un intervalo y se usa Spearman–Brown para decidir la longitud.
- 🎯 **Por qué importa:** Un cuestionario con ítems que no miden lo mismo produce una puntuación poco fiable, y con pocos participantes su fiabilidad ni siquiera se puede estimar. La decisión central: ¿qué ítems sobran, cuántos ítems hacen falta y cuántos participantes se necesitan para estimar el alfa con una incertidumbre aceptable?
- 🔗 **Se estudia junto con:** alfa de Cronbach, correlación ítem–total corregida, unidimensionalidad, validez.

📘 **Dónde se aprende** (1 clase): [B105-C27 · Instrumentos validados y psicometría en investigación](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md).

### Speckle

- El speckle es el granulado de interferencia.

💡 **Cómo se explica en la clase [B69-C03](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md):**
- En cada pixel: `x̂ = m + k (I − m)`, con `m` la media local en 7 × 7 y `k = 1 − Cu²/Ci²` acotado a [0, 1], con `Cu = 1/√L` el contraste del speckle y `Ci` el local.
- Las cifras son sintéticas, con speckle totalmente desarrollado e independiente entre pixeles; una imagen real tiene correlación espacial por el sobremuestreo y blancos brillantes que violan el modelo.
- ⚠️ **Error frecuente:** Creer que el speckle es ruido térmico. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un valor de píxel aislado de una imagen SAR no mide la reflectividad de la superficie: es una muestra de una distribución muy ancha. La decisión central: ¿cuánto hay que promediar o filtrar para estimar la reflectividad con una incertidumbre dada, y a qué precio en resolución?
- 🔗 **Se estudia junto con:** intensidad, contraste, ENL, multivista.

📘 **Dónde se aprende** (1 clase): [B69-C03 · Ruido speckle y filtrado en imágenes SAR](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md).

### SPH

- La onda de rarefacción, la discontinuidad de contacto y el choque son las tres ondas del tubo de Sod. SPH es un método de partículas con kernel de suavizado `W` y longitud `h`.

💡 **Cómo se explica en la clase [B38-C06](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md):**
- El error L1 del SPH se pondera por el volumen de cada partícula y se mide en `|x| < 0,45`.
- El SPH conserva la masa por construcción y la energía a 0,2 %.
- 🎯 **Por qué importa:** Cada método tiene errores distintos en choques y discontinuidades de contacto. La decisión central: ¿qué error comete cada método frente a una solución exacta y cómo cambia con la resolución?
- 🔗 **Se estudia junto con:** problema de Riemann, onda de rarefacción, discontinuidad de contacto, choque.

📘 **Dónde se aprende** (1 clase): [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md).

### SPI

- El CPI es `EV/AC`; el SPI, `EV/PV`.
- El SPI identifica la SA.

💡 **Cómo se explica en la clase [B89-C25](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md):**
- Con campos ilustrativos (SPI 2, IV 12, etiqueta 16 octetos = `30`), un bloque de `1115` octetos con cabecera de 8 deja `1077` octetos de datos: la eficiencia baja de `0,9928` a `0,9659`.
- SA["asociacion de seguridad: SPI, clave, ventana"] --> TX["emisor: etiqueta = MAC(clave, SPI, ASN, carga)"]
- 🎯 **Por qué importa:** Los comandos son la superficie más sensible de una misión; sin autenticación y sin protección contra repetición, una trama capturada podría reutilizarse, y un CRC solo detecta errores, no ataques (C12). La decisión central: ¿cómo garantizar que una trama es auténtica, íntegra y no repetida, y cuánto cuesta en sobrecarga?
- 🔗 **Se estudia junto con:** protocolo de seguridad de enlace de datos (SDLS), cifrado autenticado AES en modo Galois/Counter (GCM), asociación de seguridad (SA), ventana anti-repetición.

📘 **Dónde se aprende** (2 clases): [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md); [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### SPK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- En el laboratorio se resuelven 6 archivos; todos existen y LSK y SCLK están antes que los SPK (las dos comprobaciones valen 1 = sí: `1` y `1`).
- Con dos SPK de «NAVE» solapados, en `t = 500 s` los datos vienen de `spk_nave_v2_sint,bsp`.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, CK, PCK, IK.

📘 **Dónde se aprende** (1 clase): [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### SPMD

- El tamaño es cuántos procesos hay y el rango (*rank*) es el número de cada uno, de 0 a tamaño−1. SPMD (un programa, muchos datos) significa que todos ejecutan el mismo código y se comportan distinto según su rango.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Explicar el modelo SPMD, el rango y el tamaño de un comunicador.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.
- 🔗 **Se estudia junto con:** comunicador, tamaño, rango, punto a punto.

📘 **Dónde se aprende** (1 clase): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md).

### SQNR

- La SQNR es el cociente entre la potencia de la señal y la del error de cuantización.

💡 **Cómo se explica en la clase [B57-C03](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md):**
- Para una sinusoide a plena escala, la SQNR teórica es `6,02 N + 1,76 dB`.
- Ejercicio 2 · con una pista. Calcula la SQNR teórica de 10 bits.
- 🎯 **Por qué importa:** Dos sensores con el mismo píxel pueden dar información muy distinta si uno distingue 256 niveles y otro 65.536, o si una banda es ancha y otra estrecha. La decisión central: ¿cuántos bits y qué ancho de banda hacen falta para ver el cambio que me interesa?
- 🔗 **Se estudia junto con:** cuantización, paso de cuantización, banda espectral, respuesta espectral.

📘 **Dónde se aprende** (1 clase): [B57-C03 · Resolución radiométrica y espectral](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md).

### SQP

- El multiplicador mide la sensibilidad: `dDv*/dT_max = −μ`. SQP (programación cuadrática secuencial) resuelve la secuencia de problemas cuadráticos que salen de aplicar Newton al sistema KKT; con solo igualdades es Newton sobre `[∇f + λ∇g; g] = 0`.

💡 **Cómo se explica en la clase [B11-C23](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md):**
- D --> G["Resolver con SQP/Newton<br/>sobre las condiciones KKT"]
- SQP converge más rápido pero necesita derivadas y un buen punto de partida.
- 🎯 **Por qué importa:** Casi todo problema de diseño de trayectorias tiene límites: tiempo máximo, combustible disponible, distancia mínima a un cuerpo. Un optimizador que ignora las restricciones devuelve un resultado imposible; uno que las trata mal da un resultado que parece factible y no es óptimo.
- 🔗 **Se estudia junto con:** con restricción de igualdad, Lagrangiano, multiplicador de Lagrange, desigualdad.

📘 **Dónde se aprende** (1 clase): [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md).

### SRGB

- Texto grande es de al menos 18 pt, o 14 pt en negrita. sRGB es el espacio de color de las pantallas.

💡 **Cómo se explica en la clase [B128-C06](../programa/clases/B128/B128-C06-contraste-y-color-accesibles/CLASE.md):**
- Calcular la luminancia relativa de un color sRGB.
- 🎯 **Por qué importa:** Un texto gris claro sobre blanco, un azul puro sobre negro o una leyenda donde solo cambia el tono se pierden para quien tiene baja visión, daltonismo o una pantalla poco luminosa. La decisión central: ¿cómo compruebo con números que un par de colores se lee, y cuándo el color no basta?
- 🔗 **Se estudia junto con:** luminancia relativa, razón de contraste, Texto grande, uso del color.

📘 **Dónde se aprende** (1 clase): [B128-C06 · Contraste y color accesibles](../programa/clases/B128/B128-C06-contraste-y-color-accesibles/CLASE.md).

### SRR

- La SRR revisa requisitos y concepto de operaciones.

💡 **Cómo se explica en la clase [B83-C13](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md):**
- SRR: requisitos verificables (≥ 95 %), necesidades con requisito (100 %), requisitos con origen (100 %), CONOPS documentado y estabilidad del orden de necesidades (≥ 70 %, no crítico).
- Resultado: SRR 2/5 y PDR 2/7; ninguna lista.
- 🎯 **Por qué importa:** Una revisión aprobada sin criterios es un trámite; una revisión con criterios medibles es una decisión. La decisión central: ¿el proyecto cumple los criterios de entrada de la SRR y de la PDR y qué falta para llegar?
- 🔗 **Se estudia junto con:** PDR, criterio, crítico, RID.

📘 **Dónde se aprende** (1 clase): [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md).

### SRS

- Choque: excitación transitoria breve. SRS: espectro de respuesta al choque, pico del oscilador según su frecuencia.

💡 **Cómo se explica en la clase [B90-C10](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md):**
- Con `z'' + 2ζω z' + ω² z = −a(t)`, `ζ = 1/(2Q) = 0,05` y aceleración absoluta `a_abs = 2ζω z' + ω² z`, el SRS de frecuencia `fn = ω/2π` es `máx |a_abs|`.
- A 10 Hz: SRS `= 7,45 g`; respuesta analítica del impulso `= 7,45 g` (diferencia 0,01 %); el SRS queda 6,9 % por debajo de la cota sin amortiguamiento `ω ΔV = 8,00 g`.
- ⚠️ **Error frecuente:** Confundir la aceleración pico con la amenaza. Calcula el SRS (8.4)
- 🎯 **Por qué importa:** Dos pulsos con distinta forma pueden dañar lo mismo si sus SRS coinciden, y un pulso con gran aceleración pico puede ser inofensivo para un equipo de baja frecuencia. La decisión central: ¿qué frecuencias de mi equipo están amenazadas por este choque y con qué nivel?
- 🔗 **Se estudia junto con:** Choque, Pulso semisenoidal, Cambio de velocidad ΔV, Q.

📘 **Dónde se aprende** (1 clase): [B90-C10 · Ensayos de choque](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md).

### SSD

- Información `JᵀJ`: matriz cuyos autovalores miden la certeza por dirección. SSD: suma de diferencias al cuadrado.

💡 **Cómo se explica en la clase [B99-C07](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md):**
- Con cambio de ganancia `g` y sesgo `b` (`I → gI + b`) la ZNCC no cambia, y la SSD sí.
- En el laboratorio (100 parches de `11×11`, ruido de 4 niveles): a contraste 40 y sin cambio ambos aciertan 100 %; con `g = 1,5` y `b = 25` la SSD baja a 80 % y a 4 % con contraste 10, mientras la ZNCC mantiene 100 %.
- 🎯 **Por qué importa:** Un estimador que funciona en el laboratorio puede fallar sin avisar cuando el entorno empeora. La decisión central: ¿qué estimador usar, cómo detectar que el entorno no determina el movimiento y cuándo dejar de confiar en el mapa?
- 🔗 **Se estudia junto con:** Atípico, Huber / IRLS, RANSAC, Degeneración.

📘 **Dónde se aprende** (1 clase): [B99-C07 · Robustez del mapeo ante entornos degradados](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md).

### Stellarium

- Una aplicación de planetario es un programa que calcula posiciones y las dibuja para tu lugar y hora; Stellarium, por ejemplo, es un planetario libre que muestra el cielo como se vería a ojo, con binoculares o con telescopio, con varias bases de estrellas y constelaciones de más de 40 culturas (S2).

💡 **Cómo se explica en la clase [B08-C07](../programa/clases/B08/B08-C07-planisferios-y-aplicaciones-celestes/CLASE.md):**
- Una aplicación como Stellarium (S2) calcula con tu ubicación y hora y dibuja el cielo, con catálogo base de más de 600 000 estrellas y catálogos adicionales de más de 220 millones (S2).
- 🎯 **Por qué importa:** Una herramienta que no entiendes es una caja negra: si la aplicación se equivoca de ubicación o de hora, no lo notarás. La pregunta motivadora: ¿puedo confiar en lo que me muestra la herramienta, y qué hago si no hay batería?
- 🔗 **Se estudia junto con:** planisferio, aplicación de planetario, modo nocturno rojo, hora oficial.

📘 **Dónde se aprende** (1 clase): [B08-C07 · Planisferios y aplicaciones celestes](../programa/clases/B08/B08-C07-planisferios-y-aplicaciones-celestes/CLASE.md).

### Stock inicial

- El stock inicial es la cantidad de repuestos al comienzo de cada intervalo.

💡 **Cómo se explica en la clase [B97-C19](../programa/clases/B97/B97-C19-logistica-de-piezas-y-reparaciones/CLASE.md):**
- Ejercicio 2 · con una pista. Predice si el stock inicial crece o baja con `τ`.
- 🎯 **Por qué importa:** Un stock grande cuesta masa inicial; reabastecer a menudo cuesta vuelos. El mínimo está en un punto intermedio que solo aparece al calcular ambos efectos con la misma confianza de misión.
- 🔗 **Se estudia junto con:** intervalo de reabastecimiento, confianza de misión, consumo.

📘 **Dónde se aprende** (1 clase): [B97-C19 · Logística de piezas y reparaciones](../programa/clases/B97/B97-C19-logistica-de-piezas-y-reparaciones/CLASE.md).

### Strehl

- El Strehl `S` es el cociente entre la intensidad central real y la ideal.
- El Strehl escala con `λ⁻²`.

💡 **Cómo se explica en la clase [B43-C01](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md):**
- *Descripción textual:* la apertura y la razón focal fijan la escala y el muestreo; los errores por pieza se suman en cuadratura y fijan el Strehl.
- Con un frente de onda de `λ/14` RMS el Strehl de Maréchal es `0,8176`; el presupuesto de cinco errores suma `30,55 nm` RMS.
- 🎯 **Por qué importa:** Sin requisitos escritos, cada pieza del telescopio se fabrica «lo mejor posible» y no se sabe cuándo basta. La decisión central: ¿qué error de frente de onda, qué escala de imagen y qué tolerancia mecánica hay que pedir, y cómo se reparte el error entre las piezas?
- 🔗 **Se estudia junto con:** apertura, razón focal, escala de placa, muestreo de Nyquist.

📘 **Dónde se aprende** (2 clases): [B43-C01 · Requisitos ópticos y mecánicos](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md); [B50-C15 · Presupuesto de error de frente de onda de un instrumento](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md).

### Strehl de Maréchal

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C20](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md):**
- Strehl de Maréchal `0,875`; la pantalla de fase blanca de 40 000 puntos da `0,873`.
- 🎯 **Por qué importa:** Un diseño es un conjunto de compromisos. La decisión central: ¿qué apertura y qué focal cumplen el objetivo y qué defecto domina?
- 🔗 **Se estudia junto con:** presupuesto de diseño, corrector de coma, suma en cuadratura (RSS), aumento mínimo.

📘 **Dónde se aprende** (1 clase): [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md).

### Strehl instantáneo

- El Strehl instantáneo y el de larga exposición.

💡 **Cómo se explica en la clase [B42-C20](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md):**
- El pico de larga exposición dividido por el Strehl instantáneo medio es `2,63` en lazo abierto (la imagen se mueve: el pico no cae siempre en el origen) y `1,00` con el lazo cerrado.
- Medir el Strehl instantáneo por la identidad `|⟨e^{iφ}⟩|²`.
- ⚠️ **Error frecuente:** Confundir pico con Strehl instantáneo. En lazo abierto difieren.
- 🎯 **Por qué importa:** El producto es un informe con evidencia numérica de cuánto corrige un lazo dado, con sus límites. La decisión central: ¿qué ganancia y qué ruido dan el Strehl más alto y cómo se comprueba?
- 🔗 **Se estudia junto con:** lazo cerrado, flujo congelado, sensor ideal, larga exposición.

📘 **Dónde se aprende** (1 clase): [B42-C20 · Laboratorio de corrección óptica simulada](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md).

### STRIDE

- La probabilidad de acierto al azar es `2^−b`. STRIDE son seis categorías de amenaza.

💡 **Cómo se explica en la clase [B88-C17](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md):**
- Escribir un modelo de amenazas STRIDE con mitigaciones.
- Ejercicio 11 · transferencia. Transferencia. ¿Qué amenaza de STRIDE no cubre el HMAC?
- 🎯 **Por qué importa:** Una orden falsa o repetida puede apagar un subsistema o poner la nave en riesgo. La decisión central: ¿qué comprobaciones aseguran que cada comando viene de quien tiene la clave y no es una repetición?
- 🔗 **Se estudia junto con:** etiqueta, ventana, probabilidad de acierto al azar, comando de resincronización.

📘 **Dónde se aprende** (1 clase): [B88-C17 · Ciberseguridad de aviónica](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md).

### Suavizado

- El suavizado es la propiedad de la relajación de eliminar rápido los errores oscilantes.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- Esa asimetría es la propiedad de suavizado, y es la clave del multigrid.
- Explicar la propiedad de suavizado y escribir un ciclo V de multigrid.
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;
- 🔗 **Se estudia junto con:** ecuación de Poisson, elíptico, de Dirichlet, estencil de cinco puntos.

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Suavizado de malla

- El suavizado de malla marca también las vecinas de una celda marcada.

💡 **Cómo se explica en la clase [B21-C05](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md):**
- RAMSES añade una regla estricta para que las transiciones sean suaves: toda celda refinada debe estar rodeada de celdas padre vecinas, y también un «suavizado de malla» que marca las vecinas de las marcadas, para que el mapa de refinamiento no sea ruidoso (S1).
- 🎯 **Por qué importa:** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.
- 🔗 **Se estudia junto con:** malla adaptativa, nivel, criterio de refinamiento, restricción.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Subapertura

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C14](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md):**
- S["subapertura"] --> M["mancha desplazada"]
- Con mancha gaussiana de `σ = 0,85 px`, ventana de 8 × 8 y lectura de 3 e⁻ (ilustrativos) 400 fotones dan un centroide con `0,1461 px` (previsto `0,1446`); un centroide de `0,05 px` es `24,24 nm` de camino óptico en una subapertura de `0,2 m`.
- 🎯 **Por qué importa:** El Shack-Hartmann es el sensor más usado en óptica adaptativa. La decisión central: ¿cuántos fotones hacen falta por subapertura para que el centroide sea preciso?
- 🔗 **Se estudia junto con:** centroide, ruido de fotones, de lectura, ventana.

📘 **Dónde se aprende** (1 clase): [B42-C14 · Sensores Shack-Hartmann](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md).

### Subarmónicos

- Los subarmónicos: frecuencias bajas añadidas.

💡 **Cómo se explica en la clase [B42-C11](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md):**
- El déficit frente a la teoría infinita (15 % a 23 %) no es un error de código: la malla pierde potencia por encima de Nyquist y, para `r = 0,64 m` (`L/4`), la integral espectral da `55,157` frente a `77,221` (déficit `28,6 %`) por las frecuencias bajas que faltan aun con subarmónicos.
- Sin subarmónicos el déficit a 0,08 m era de 35 %.
- ⚠️ **Error frecuente:** Olvidar los pares sin envolver. Los subarmónicos no son periódicos.
- 🎯 **Por qué importa:** La atmósfera fija el límite de resolución de los telescopios terrestres y es la perturbación que corrige la óptica adaptativa. La decisión central: ¿cómo se simula una pantalla de fase con la estadística correcta y qué errores introduce la malla?
- 🔗 **Se estudia junto con:** pantalla de fase, espectro de potencia, función de estructura, parámetro.

📘 **Dónde se aprende** (1 clase): [B42-C11 · Turbulencia atmosférica](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md).

### Subciclado

- El subciclado da varios pasos de tiempo pequeños en el nivel fino por cada paso del grueso.

💡 **Cómo se explica en la clase [B21-C05](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md):**
- Explicar el subciclado y la corrección de flujo en las interfaces grueso–fino.
- Ejercicio 6. Con tres niveles (razón 2 entre ellos) y subciclado, ¿cuántos pasos da el nivel más fino por cada paso grueso?
- 🎯 **Por qué importa:** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.
- 🔗 **Se estudia junto con:** malla adaptativa, nivel, criterio de refinamiento, suavizado de malla.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Subdesbordamiento

- Un desbordamiento es un resultado mayor que el máximo representable (`1,8 × 10³⁰⁸`), que da `inf`; un subdesbordamiento va hacia cero o a un número subnormal.

💡 **Contexto en la clase [B11-C25](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md):**
- **Idea central (modelo mental):** Los números representables son marcas en una regla; entre dos marcas no hay nada. Las marcas están más separadas cuanto mayor es el número, así que el error absoluto crece con la magnitud, y el relativo se mantiene en `ε`.
- 🎯 **Por qué importa:** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.
- 🔗 **Se estudia junto con:** doble precisión, épsilon de máquina, ulp, redondeo al más cercano.

📘 **Dónde se aprende** (1 clase): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md).

### Subespacio

- Un subespacio es un subconjunto de `V` que, con las mismas operaciones, es en sí un espacio vectorial; basta comprobar tres cosas (sección 8.3).

💡 **Cómo se explica en la clase [B10-C01](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md):**
- Sus soluciones forman un subespacio: si `u` y `v` la cumplen, `a(u + v) = a u + a v = 0`, y `a(k u) = k·0 = 0`.
- Con lado derecho distinto de cero no hay subespacio (el origen no es solución).
- ⚠️ **Error frecuente:** Creer que todo plano es subespacio. Se corrige con el ejercicio 3 y la sección 8.4.
- 🎯 **Por qué importa:** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.
- 🔗 **Se estudia junto con:** espacio vectorial real, cero, opuesto, escalar.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Subexpandida

- sobreexpandida, `p_e < p_a`; subexpandida, `p_e > p_a`.

💡 **Cómo se explica en la clase [B79-C08](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md):**
- No: en vacío `p_a = 0`, está subexpandida.
- 🎯 **Por qué importa:** B78-C03 trata la cámara pero no el flujo por la tobera. La teoría de expansión es lo que une la presión de cámara con el empuje.
- 🔗 **Se estudia junto con:** bloqueada, relación de expansión, empuje, coeficiente de empuje.

📘 **Dónde se aprende** (1 clase): [B79-C08 · Flujo en toberas convergente-divergentes](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md).

### Subida

- Cada orden viaja por subida y su respuesta por bajada; cada trayecto se pierde con probabilidad `p`.

💡 **Cómo se explica en la clase [B98-C06](../programa/clases/B98/B98-C06-simulacion-de-teleoperacion-con-retardo/CLASE.md):**
- *Descripción textual:* cada orden se reenvía hasta que subida y bajada llegan; los intentos fallidos cuestan el temporizador y el éxito cuesta ejecución y decisión.
- Modelar una orden con subida, bajada, temporizador y retransmisión.
- 🎯 **Por qué importa:** Un promedio oculta la cola: una campaña que «normalmente» dura 8,7 h puede tardar 10,2 h una de cada veinte veces. La decisión central: ¿qué duración debe prometerse a la misión, la media o un percentil, y cómo se comprueba que la simulación es correcta?
- 🔗 **Se estudia junto con:** bajada, esperanza, percentil 95.

📘 **Dónde se aprende** (1 clase): [B98-C06 · Simulación de teleoperación con retardo](../programa/clases/B98/B98-C06-simulacion-de-teleoperacion-con-retardo/CLASE.md).

### Subida rápida y caída exponencial

- La subida rápida y caída exponencial es su plantilla mínima.

💡 **Contexto en la clase [B29-C15](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md):**
- **Idea central (modelo mental):** Cada petardo (llamarada) tiene una energía; en un registro largo hay muchos pequeños y pocos grandes. El índice dice cuán rápido disminuyen.
- 🎯 **Por qué importa:** La distribución de energías de las llamaradas determina cuánta energía total reciben los planetas cercanos. Estimar su índice con poco sesgo exige usar el estimador correcto.
- 🔗 **Se estudia junto con:** llamarada, energía, índice, máxima verosimilitud.

📘 **Dónde se aprende** (1 clase): [B29-C15 · Eventos eruptivos estelares](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md).

### Sublimación

- La sublimación es el paso de sólido a gas.
- La sublimación es el paso de sólido a vapor.
- Las curvas de equilibrio separan regiones: fusión (sólido–líquido), vaporización (líquido–gas) y sublimación (sólido–gas).

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- Para el CO₂, el punto triple está en `5,185 bar`, es decir, a una presión más de cinco veces la atmosférica: por eso el CO₂ sólido a presión ambiental no se funde, sublima (S5).
- Con el CO₂, sublimación a 1 atm, y `ΔH_sub = 26,1 kJ/mol`, resulta `194,7 K`; con los extremos publicados (25,2 y 27,2 kJ/mol), `194,0` y `195,5 K`: la incertidumbre de `ΔH` mueve el resultado en 1,5 K (S5).
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.
- 🔗 **Se estudia junto con:** diagrama de fases, curvas de equilibrio, fusión, vaporización.

📘 **Dónde se aprende** (3 clases): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md); [B58-C04 · Núcleos y colas cometarias](../programa/clases/B58/B58-C04-nucleos-y-colas-cometarias/CLASE.md); [B59-C06 · Extracción y procesamiento de volátiles](../programa/clases/B59/B59-C06-extraccion-y-procesamiento-de-volatiles/CLASE.md).

### Submuestrear

- La cadencia es el intervalo entre observaciones; submuestrear es quedarse con un registro por ventana de tiempo.

💡 **Cómo se explica en la clase [B14-C22](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md):**
- Submuestrear por cadencia con una regla clara y verificar el conteo.
- 🎯 **Por qué importa:** Quieres estudiar una región activa del Sol durante un día usando imágenes ultravioleta. Hay cientos de miles de archivos repartidos en varios proveedores.
- 🔗 **Se estudia junto con:** cliente, búsqueda, registro, cadencia.

📘 **Dónde se aprende** (1 clase): [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md).

### Subnormal

- Un desbordamiento es un resultado mayor que el máximo representable (`1,8 × 10³⁰⁸`), que da `inf`; un subdesbordamiento va hacia cero o a un número subnormal.

💡 **Cómo se explica en la clase [B11-C25](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md):**
- Los límites son `1,8 × 10³⁰⁸` (máximo), `2,2 × 10⁻³⁰⁸` (mínimo normal) y `4,9 × 10⁻³²⁴` (mínimo subnormal);
- límites: máximo 1.798e+308; mínimo normal 2.225e-308; mínimo subnormal 4.941e-324; 1e308*10 = inf
- 🎯 **Por qué importa:** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.
- 🔗 **Se estudia junto con:** doble precisión, épsilon de máquina, ulp, redondeo al más cercano.

📘 **Dónde se aprende** (1 clase): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md).

### Subnotificación

- Una cultura justa protege el reporte honesto. Subnotificación es informar menos de lo ocurrido.

💡 **Cómo se explica en la clase [B119-C21](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md):**
- ⚠️ **Error frecuente:** Ignorar la subnotificación. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** B88-C16 cubre la seguridad funcional técnica; ninguna clase trata la dimensión cultural, y los indicadores de reportes se malinterpretan con facilidad. La decisión central: ¿qué indicador permite saber si una organización aprende cuando los reportes dependen de la confianza para informar?
- 🔗 **Se estudia junto con:** cultura de seguridad, fracción reportada, curva de aprendizaje, cultura justa.

📘 **Dónde se aprende** (1 clase): [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md).

### Subpresión

- La subpresión `ΔP` es la caída de presión de la cámara respecto de la litostática.

💡 **Cómo se explica en la clase [B70-C03](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md):**
- Un techo ancho y delgado colapsa con menos subpresión.
- D["volumen evacuado"] --> P["subpresión ΔP = K ΔV/Vc"]
- ⚠️ **Error frecuente:** Confundir subpresión con presión. Se corrige en la sección 6.
- 🎯 **Por qué importa:** Evacuar magma no siempre hunde el techo. La decisión central: ¿cuánta subpresión resiste un techo y cuánto magma hay que sacar para vencerla?
- 🔗 **Se estudia junto con:** pistón, falla anular, balance de volumen.

📘 **Dónde se aprende** (1 clase): [B70-C03 · Calderas planetarias: formación y colapso](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md).

### Subproducto

- El subproducto aquí es el monóxido de carbono.
- Un subproducto es un material que sale junto al producto.

💡 **Cómo se explica en la clase [B59-C08](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md):**
- Es un subproducto que se gestiona o aprovecha (C23).
- 🎯 **Por qué importa:** Un oxidante producido en destino se mide en gramos por hora, pero el diseñador piensa en amperios y vatios. La decisión central: ¿qué corriente y qué potencia exige una tasa de oxígeno dada?
- 🔗 **Se estudia junto con:** electrólisis de óxido sólido, electrones por O₂, ley de Faraday, celda en serie.

📘 **Dónde se aprende** (2 clases): [B59-C08 · Producción de oxígeno](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md); [B59-C23 · Subproductos y flujos residuales de procesos ISRU](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md).

### Subsidencia

- La subsidencia es el hundimiento del terreno.

💡 **Cómo se explica en la clase [B69-C06](../programa/clases/B69/B69-C06-deslizamientos-y-subsidencia-medidos-con-insar/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *ficha de la deformación*: el perfil de subsidencia, la reconstrucción con error, el límite del gradiente y la descomposición ascendente–descendente.
- El script [deformacion_insar.py](deformacion_insar.py) genera la fase de un cuenco de subsidencia y de un deslizamiento sintéticos, desenvuelve con ruido y descompone con dos geometrías (comprueba el hundimiento a 2 mm, el fallo con gradiente fuerte y la descomposición exacta a 10⁻⁹).
- 🎯 **Por qué importa:** Un solo interferograma no dice si el suelo bajó o se movió al este. La decisión central: ¿qué parte del movimiento real mide la línea de visión, hasta qué gradiente se puede desenvolver y qué se puede concluir?
- 🔗 **Se estudia junto con:** desplazamiento en la línea de visión, Desenvolver, franja, Ascendente/descendente.

📘 **Dónde se aprende** (1 clase): [B69-C06 · Deslizamientos y subsidencia medidos con InSAR](../programa/clases/B69/B69-C06-deslizamientos-y-subsidencia-medidos-con-insar/CLASE.md).

### Subtítulos

- Los subtítulos (captions) son texto sincronizado con el habla y con los sonidos no hablados relevantes.

💡 **Cómo se explica en la clase [B128-C05](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md):**
- W3C WAI distingue: los *captions* son el texto del habla y de los sonidos no hablados necesarios, sincronizados y normalmente activables; los *subtítulos* suelen ser traducciones a otro idioma; las transcripciones tienen el mismo texto que los captions; la audiodescripción describe lo visual.
- Distinguir subtítulos, captions, transcripción y audiodescripción.
- ⚠️ **Error frecuente:** Confundir subtítulos y transcripción. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un subtítulo mal sincronizado o demasiado rápido no se alcanza a leer, y una transcripción automática sin revisar puede decir lo contrario de lo dicho. La decisión central: ¿cómo compruebo que los subtítulos se pueden leer y que no cambian el sentido?
- 🔗 **Se estudia junto con:** transcripción, audiodescripción, WebVTT, WER.

📘 **Dónde se aprende** (1 clase): [B128-C05 · Subtítulos y transcripciones](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md).

### Sub-triage

- La categoría (baja, media, alta) agrupa el total. Sub-triage: caso asignado a una categoría menos urgente que la verdadera;

💡 **Cómo se explica en la clase [B116-C04](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md):**
- Sensibilidad `(1132 + 1240 + 1013)/3978 = 0,851`; especificidad `15822/16022 = 0,988`; sub-triage `593/20000 = 2,96 %`.
- El ruido del sensor produce sobre-triage de personas estables, con el coste de alertas y consultas, más que sub-triage.
- 🎯 **Por qué importa:** Un puntaje simple ayuda a decidir rápido y de forma homogénea, pero un fallo por defecto (sub-triage) deja sin atender a quien lo necesita y uno por exceso (sobre-triage) agota recursos y atención. Y si la respuesta de tierra tarda decenas de minutos, no se puede esperar a tierra para lo que no admite espera.
- 🔗 **Se estudia junto con:** Triage, puntaje de alerta temprana, categoría, sobre-triage.

📘 **Dónde se aprende** (1 clase): [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Sucesión de Sturm

- La sucesión de Sturm cuenta autovalores menores que un valor.

💡 **Contexto en la clase [B31-C02](../programa/clases/B31/B31-C02-ecuacion-de-schrodinger/CLASE.md):**
- **Idea central (modelo mental):** Como una cuerda de guitarra fija en sus extremos, solo ciertas ondas caben y cada una tiene su energía; la barrera es una zona donde la onda decae, pero no se anula.
- 🎯 **Por qué importa:** Los espectros de los átomos y los niveles de los núcleos salen de esta ecuación. La decisión central: ¿cómo se obtiene la energía de un estado ligado y cuánto atraviesa una barrera?
- 🔗 **Se estudia junto con:** hamiltoniano, autovalor, pozo infinito, oscilador armónico.

📘 **Dónde se aprende** (1 clase): [B31-C02 · Ecuación de Schrödinger](../programa/clases/B31/B31-C02-ecuacion-de-schrodinger/CLASE.md).

### Suceso raro

- Un suceso raro tiene probabilidad muy pequeña.

💡 **Cómo se explica en la clase [B12-C15](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md):**
- A["Objetivo p(x)<br/>(suceso raro en la cola)"] --> B["Elegir propuesta q(x)<br/>con masa en la cola"]
- Monte Carlo simple: sin diseño, pero inviable para sucesos raros.
- 🎯 **Por qué importa:** Los sucesos que más interesan en seguridad espacial —un error de aproximación fuera de límites, una falla simultánea, una colisión— son raros por diseño. Un Monte Carlo simple puede pasar millones de ensayos sin ver un solo acierto y reportar «cero», que no es una estimación útil.
- 🔗 **Se estudia junto con:** muestreo de importancia, propuesta, peso, insesgado.

📘 **Dónde se aprende** (1 clase): [B12-C15 · Muestreo de importancia](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md).

### Suelo de fondo

- El suelo de fondo es el suelo visible bajo y entre las plantas.

💡 **Cómo se explica en la clase [B57-C06](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md):**
- Medir cuánto cambia el NDVI y el SAVI con el suelo de fondo.
- Ejercicio 7. ¿Qué pasa con el NDVI si aumenta la reflectancia del suelo de fondo (LAI = 1)?
- ⚠️ **Error frecuente:** Olvidar el suelo de fondo. Se mide en 8.2.
- 🎯 **Por qué importa:** Un índice facilita comparar fechas y lugares, pero también esconde supuestos. La decisión central: ¿cuándo el NDVI mide de verdad la cantidad de vegetación y cuándo lo engañan la saturación o el suelo?
- 🔗 **Se estudia junto con:** NDVI, SAVI, LAI, saturación.

📘 **Dónde se aprende** (1 clase): [B57-C06 · Índices de vegetación](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md).

### Suelo de ruido

- El suelo de ruido es el límite de precisión de la posición de una fuente que no baja aunque se observe más (S1;
- El suelo de ruido es `k T B` más la cifra de ruido.
- El suelo de ruido limita lo que se ve de los lóbulos.

💡 **Cómo se explica en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
- ICRF2 (2009; fundamental desde el 1 de enero de 2010): `295` definidoras, `3414` fuentes en total, suelo de ruido `≈ 0,04 mas` y ejes estables dentro de `0,01 mas` (S1, 2.2).
- ICRF3 (adoptado por la IAU en 2018, vigente desde el 1 de enero de 2019): `4588` fuentes, `303` definidoras, mediana `0,1 mas`/`0,2 mas`, suelo de ruido `0,03 mas`, con medidas en `8,4`, `24` y `32 GHz` (S2, resumen).
- 🎯 **Por qué importa:** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.
- 🔗 **Se estudia junto con:** Sistema Celeste de Referencia Internacional (ICRS), Marco Celeste de Referencia Internacional (ICRF), fuente definidora, cuásar.

📘 **Dónde se aprende** (3 clases): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md); [B49-C05 · Medición y calibración de patrones de antena](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md); [B49-C09 · Linealidad, compresión e intermodulación de receptores de RF](../programa/clases/B49/B49-C09-linealidad-compresion-e-intermodulacion-de-receptores-de-rf/CLASE.md).

### Suficiente

- El teorema de la ganancia pequeña dice que, si el lazo nominal es estable y `|Δ|·‖T‖∞ < 1` (para `Δ` constante o con `|Δ(jω)| ≤ δ`), el lazo con incertidumbre multiplicativa sigue estable: es una condición suficiente.
- La cota de Liu–Layland `n(2^(1/n) − 1)` es una condición suficiente de planificabilidad con prioridades por tasa.
- Un criterio necesario debe cumplirse siempre; uno suficiente basta por sí solo.

💡 **Cómo se explica en la clase [B16-C16](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md):**
- La cota es suficiente pero no necesaria.
- Aplicar el teorema de la ganancia pequeña y reconocer que es suficiente, no necesario.
- 🎯 **Por qué importa:** La inercia de un satélite cambia al desplegar paneles, consumir propergol o capturar una carga; el actuador envejece; el sensor tiene un retardo que no se conocía. El lazo diseñado con la inercia nominal debe seguir funcionando.
- 🔗 **Se estudia junto con:** incertidumbre paramétrica, incertidumbre multiplicativa, norma H∞, teorema de la ganancia pequeña.

📘 **Dónde se aprende** (3 clases): [B16-C16 · Control robusto inicial](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md); [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md); [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md).

### Suitport

- Un suitport acopla el traje a la pared del hábitat para entrar sin llevar el polvo adentro.

💡 **Cómo se explica en la clase [B109-C04](../programa/clases/B109/B109-C04-mitigacion-de-polvo-lunar-en-accesos-y-habitats/CLASE.md):**
- (2023) comparan esclusa, *suitlock* y suitport-esclusa y concluyen, de forma cualitativa, que los dos últimos reducen la entrada de polvo porque evitan abrir la escotilla interior con trajes sucios.
- Con cepillado más suitport (`3 %` cruza, ilustrativo) bajan a `1,20 g` por traje y `0,250 kg/año`.
- 🎯 **Por qué importa:** Cada salida y cada regreso trae polvo a un lugar donde la tripulación respira, duerme y repara equipos. La decisión central: ¿cuántas barreras en serie hacen falta y qué arquitectura de acceso reduce más la entrada?
- 🔗 **Se estudia junto con:** regolito, polvo, barrera, cadena de barreras.

📘 **Dónde se aprende** (1 clase): [B109-C04 · Mitigación de polvo lunar en accesos y hábitats](../programa/clases/B109/B109-C04-mitigacion-de-polvo-lunar-en-accesos-y-habitats/CLASE.md).

### Sujeción

- Par `τ`: fuerza por brazo. Sujeción: apoyo que reacciona.

💡 **Cómo se explica en la clase [B106-C16](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md):**
- *Descripción textual:* la fuerza que se aplica a una carga produce una reacción sobre el cuerpo; una sujeción absorbe esa reacción y mantiene la tarea en su sitio.
- Paso 4. Par de 10 N·m sin sujeción: `α = 10/1,5 = 6,67 rad/s²`;
- 🎯 **Por qué importa:** Sin peso ni fricción, toda fuerza tiene una reacción que mueve al operario o a la carga; un diseño de herramientas y de superficies que lo ignore produce maniobras inseguras. La decisión central: ¿qué sujeciones y qué límites de par o de empuje evitan que la reacción mueva al astronauta fuera de la tarea?
- 🔗 **Se estudia junto con:** Impulso, Conservación del momento, Momento de inercia I, Par τ.

📘 **Dónde se aprende** (1 clase): [B106-C16 · Ergonomía en microgravedad](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md).

### Suma

- La suma de vectores se hace componente a componente.

💡 **Cómo se explica en la clase [B04-C12](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md):**
- Para sumar dos, pon el inicio de la segunda en la punta de la primera: la suma es la flecha que va del inicio de la primera a la punta de la segunda.
- A["v_Tierra = (0; 29,79) km/s"] --> S["Suma componente a componente"]
- 🎯 **Por qué importa:** Una sonda que sale de la Tierra tiene una velocidad respecto de la Tierra y la Tierra tiene una velocidad respecto del Sol. ¿Cuál es la velocidad de la sonda respecto del Sol?
- 🔗 **Se estudia junto con:** escalar, vector, componentes, módulo.

📘 **Dónde se aprende** (1 clase): [B04-C12 · Vectores y componentes](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md).

### Suma compensada

- La suma compensada (de Kahan) lleva una corrección con lo que se pierde en cada suma.

💡 **Cómo se explica en la clase [B11-C25](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md):**
- El error de acumulación (`1,3 × 10⁻¹¹` relativo) hace que la igualdad falle; se calcula `t = n · h` en cada paso o se usa suma compensada, y se compara con tolerancia.
- 🎯 **Por qué importa:** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.
- 🔗 **Se estudia junto con:** doble precisión, épsilon de máquina, ulp, redondeo al más cercano.

📘 **Dónde se aprende** (1 clase): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md).

### Suma cuadrática

- La suma cuadrática combina aportes independientes.
- La suma cuadrática combina términos independientes.

💡 **Cómo se explica en la clase [B50-C09](../programa/clases/B50/B50-C09-asignacion-y-balance-de-tolerancias-opticas/CLASE.md):**
- Objetivo: 0.05 ondas RMS (suma cuadratica); costo C = suma de a_i / delta_i
- 🎯 **Por qué importa:** Repartir la tolerancia por igual es simple pero caro: pide más precisión justo donde cuesta más. La decisión central: ¿cuánta tolerancia le toca a cada parámetro para el menor costo con el mismo desempeño?
- 🔗 **Se estudia junto con:** sensibilidad, tolerancia uniforme, multiplicador de Lagrange, óptimo.

📘 **Dónde se aprende** (2 clases): [B50-C09 · Asignación y balance de tolerancias ópticas](../programa/clases/B50/B50-C09-asignacion-y-balance-de-tolerancias-opticas/CLASE.md); [B50-C15 · Presupuesto de error de frente de onda de un instrumento](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md).

### Suma de apertura

- La suma de apertura suma los píxeles y corrige la fracción.

💡 **Contexto en la clase [B45-C18](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md):**
- **Idea central (modelo mental):** Como una votación donde los votos más fiables (píxeles de mayor señal) pesan más y los dudosos casi nada.
- 🎯 **Por qué importa:** Una extracción ingenua pierde señal a ruido y es sensible a defectos. La decisión central: ¿qué pesos dan la menor varianza y cómo se protege la extracción de valores atípicos?
- 🔗 **Se estudia junto con:** perfil espacial, extracción óptima, varianza, rayo cósmico.

📘 **Dónde se aprende** (1 clase): [B45-C18 · Extracción de espectros](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md).

### Suma de cuantilas

- La suma de cuantilas es conservadora; la raíz de la suma de cuadrados (RSS) es optimista para sumar magnitudes.

💡 **Cómo se explica en la clase [B81-C14](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md):**
- La cuantila de la suma queda entre el RSS y la suma de cuantilas.
- Cinco correcciones independientes necesitan `8,19 m/s` (la suma de cuantilas sería `13,20`).
- ⚠️ **Error frecuente:** Sumar cuantilas como si fueran de la suma. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un presupuesto muy bajo deja a la nave sin propelente; uno muy alto la lastra. La decisión central: ¿qué cuantila de `Δv` reservar para una o varias correcciones, y cómo se combinan?
- 🔗 **Se estudia junto con:** Δv de corrección, magnitud, presupuesto al 99 %, raíz de la suma de cuadrados.

📘 **Dónde se aprende** (1 clase): [B81-C14 · Presupuestos de maniobras de corrección](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md).

### Suma de flujos

- Brillo del cielo: mag por arcsec². Suma de flujos: los brillos se suman como flujos.

💡 **Cómo se explica en la clase [B48-C18](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md):**
- M["m_nat, m_art"] --> S["Suma de flujos"]
- *Descripción textual:* los flujos de las fuentes de brillo se suman, de la suma sale el cielo en electrones por segundo y de él el tiempo necesario para una relación señal-ruido.
- 🎯 **Por qué importa:** Cada fracción de magnitud perdida se paga en tiempo de telescopio. La decisión central: ¿cuánto cuesta en exposición una contaminación luminosa dada?
- 🔗 **Se estudia junto con:** Brillo del cielo, Limitado por el cielo, Relación señal-ruido, Contaminación lumínica.

📘 **Dónde se aprende** (1 clase): [B48-C18 · Protección del cielo oscuro](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md).

### Suma de fracciones de vida consumidas

- Daño acumulado: suma de fracciones de vida consumidas. Paquete de datos: conjunto de evidencias de aceptación.

💡 **Contexto en la clase [B90-C19](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md):**
- 🎯 **Por qué importa:** Un ensayo de aceptación demasiado severo gasta vida útil; uno demasiado suave deja pasar defectos. La decisión central: ¿qué nivel y duración demuestran la mano de obra sin dañar la unidad, y con qué evidencia se acepta?
- 🔗 **Se estudia junto con:** Calificación, Protovuelo, Aceptación, calidad de fabricación.

📘 **Dónde se aprende** (1 clase): [B90-C19 · Aceptación de unidades de vuelo](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md).

### Suma de Petzval

- La superficie de Petzval es la superficie de enfoque sin astigmatismo; su curvatura es la suma de Petzval `Σ φᵢ/nᵢ` (con `n = −1` en un espejo).

💡 **Cómo se explica en la clase [B50-C07](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md):**
- *Descripción textual:* las superficies de enfoque se obtienen de trazar haces estrechos, y el aplanador anula la suma de Petzval.
- Comparar el óptimo con la suma de Petzval.
- 🎯 **Por qué importa:** Un detector plano mal enfocado en el borde pierde resolución: hay que decidir si se acepta, se curva el detector o se agrega un aplanador. La decisión central: ¿cuánto se hunde el foco en el borde y qué lo corrige?
- 🔗 **Se estudia junto con:** tangencial, sagital, superficie de Petzval, aplanador.

📘 **Dónde se aprende** (1 clase): [B50-C07 · Curvatura de campo y aplanadores](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md).

### Suma de verificación

- Una suma de verificación (*checksum*) es un número calculado a partir de los bytes de un archivo.
- Suma de verificación: resumen corto de un archivo.

💡 **Cómo se explica en la clase [B14-C11](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md):**
- Calcular y comprobar la suma de verificación SHA-256 de un archivo contra un vector de prueba oficial.
- 🎯 **Por qué importa:** Un análisis usó «la tabla de catálogo de octubre». En noviembre alguien reemplazó el archivo por otro con el mismo nombre.
- 🔗 **Se estudia junto con:** función de hash criptográfica, direccionamiento por contenido, deduplicación, manifiesto.

📘 **Dónde se aprende** (2 clases): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md); [B48-C17 · Gestión de archivos observacionales](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md).

### Suma directa

- La suma directa suma `−G m_i/d_i` sobre todas las masas.
- La suma directa calcula la fuerza sobre cada cuerpo como suma de las de los demás: `a_i = Σ_{j≠i} GM_j (r_j − r_i)/|r_j − r_i|³`.

💡 **Cómo se explica en la clase [B53-C03](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md):**
- A `r = 3a` la serie con `J2` difiere de la suma directa en `3,69 × 10⁻⁵` en relación; a `r = 10a`, en `2,78 × 10⁻⁷`.
- Calcular el potencial exacto por suma directa.
- 🎯 **Por qué importa:** Las trayectorias de una sonda dependen del campo. La decisión central: ¿hasta qué término de la serie hay que llegar a una distancia dada?
- 🔗 **Se estudia junto con:** monopolo, multipolo.

📘 **Dónde se aprende** (2 clases): [B53-C03 · Campo gravitatorio planetario](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md); [B73-C08 · Sistemas de N cuerpos](../programa/clases/B73/B73-C08-sistemas-de-n-cuerpos/CLASE.md).

### Suma en cuadratura (RSS)

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C20](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md):**
- **Idea central (modelo mental):** Como un presupuesto familiar: cada partida (espejo, plano, enfoque) gasta una parte del error total, y se suman en cuadratura; se mira cuál gasta más.
- 🎯 **Por qué importa:** Un diseño es un conjunto de compromisos. La decisión central: ¿qué apertura y qué focal cumplen el objetivo y qué defecto domina?
- 🔗 **Se estudia junto con:** presupuesto de diseño, corrector de coma, Strehl de Maréchal, aumento mínimo.

📘 **Dónde se aprende** (2 clases): [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md); [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md).

### Suma incoherente

- Incertidumbre `U`: dispersión de la medida. Suma incoherente: suma de potencias.

💡 **Cómo se explica en la clase [B90-C13](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md):**
- Verificar la suma incoherente con Monte Carlo de fases.
- Dos fuentes de 70 dBuV: suma incoherente = 73.010 dBuV (+3.01 dB) ; suma coherente = 76.021 dBuV (+6.02 dB)
- 🎯 **Por qué importa:** Un convertidor de potencia emite armónicos que viajan por el arnés y pueden perturbar a otro equipo. El margen de 2 dB que pasa hoy puede ser negativo mañana si cambia la incertidumbre.
- 🔗 **Se estudia junto con:** EMC, Emisión conducida, dBµV, Límite.

📘 **Dónde se aprende** (1 clase): [B90-C13 · Compatibilidad electromagnética EMC](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md).

### Suma lineal

- La suma lineal es la cota del peor caso.

💡 **Cómo se explica en la clase [B87-C22](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md):**
- Suma lineal: peor caso o errores correlacionados.
- Con seis contribuyentes (`3; 5; 4; 2,5; 1,5; 2″` 1σ), la suma cuadrática es `7,91″` y la lineal `18,0″`.
- 🎯 **Por qué importa:** Un requisito de apuntamiento solo se cumple si el diseño lo respalda con números. La decisión central: ¿qué contribuyentes dominan, cómo se combinan (suma lineal o cuadrática), con qué margen se cumple el requisito y qué ocurre con dos ejes?
- 🔗 **Se estudia junto con:** contribuyente, RSS, término acotado uniforme, margen.

📘 **Dónde se aprende** (1 clase): [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md).

### Suma ponderada

- La suma ponderada puntúa cada candidato como `Σ wⱼ vⱼ`, con `vⱼ` normalizado y con signo según se maximice o minimice.
- La suma ponderada combina puntajes.

💡 **Cómo se explica en la clase [B91-C06](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md):**
- Límite: la suma ponderada con normalización min–max depende del conjunto de candidatos; añadir uno cambia la escala.
- Aplicar una suma ponderada con normalización min–max.
- 🎯 **Por qué importa:** Ninguna antena gana en todo: más ganancia suele costar masa, apertura o dinero. La decisión central: ¿qué antena cumple los requisitos y cuál conviene según cómo se pesen la masa, el costo y el riesgo, y cuánto cambia la respuesta si los pesos cambian?
- 🔗 **Se estudia junto con:** requisito, domina, frente de Pareto, sensibilidad.

📘 **Dónde se aprende** (2 clases): [B91-C06 · Selección y compromiso de diseño de antenas](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md); [B119-C18 · Ética y derechos en actividades espaciales](../programa/clases/B119/B119-C18-etica-y-derechos-en-actividades-espaciales/CLASE.md).

### Sumador

- Un sumador (círculo) combina señales con signo.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- Se puede trasladar un sumador o una bifurcación a través de un bloque si se compensa con ese mismo bloque.
- Recorre una señal: sale del sumador como error, pasa por el controlador, el cuerpo, llega a la salida, vuelve por el sensor al sumador.
- ⚠️ **Error frecuente:** Confundir el signo del sumador. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.
- 🔗 **Se estudia junto con:** diagrama de bloques, punto de bifurcación, lazo cerrado, referencia.

📘 **Dónde se aprende** (1 clase): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md).

### Sumas de Riemann

- La integral definida `∫_a^b f(x) dx` es el límite de las sumas de Riemann `Σ f(x_i*) Δx` cuando `Δx → 0` (S1, §1.4(v)).

💡 **Cómo se explica en la clase [B09-C11](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md):**
- Definir la integral definida como límite de sumas de Riemann.
- 🎯 **Por qué importa:** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.
- 🔗 **Se estudia junto con:** integral definida, partición, regla del punto izquierdo (derecho), regla del punto medio.

📘 **Dónde se aprende** (1 clase): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md).

### Sumidero

- Alcanzabilidad: estados a los que se llega desde otro. Sumidero: estado terminal.

💡 **Cómo se explica en la clase [B96-C08](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md):**
- (2) FIN es sumidero y solo lo alcanza DESORBITANDO.
- Paso 4 · Sumidero. FIN solo desde DESORBITANDO.
- 🎯 **Por qué importa:** Un comando válido en un estado puede ser peligroso en otro; y un modo seguro al que no se puede volver es una trampa. La decisión central: ¿qué transiciones existen y se puede siempre llegar al estado seguro?
- 🔗 **Se estudia junto con:** Estado/modo, Transición, Alcanzabilidad, Propiedad de seguridad.

📘 **Dónde se aprende** (1 clase): [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md).

### Sumidero efectivo

- Radiador: superficie que emite al espacio. Sumidero efectivo: temperatura radiativa del entorno visto.

💡 **Cómo se explica en la clase [B106-C08](../programa/clases/B106/B106-C08-control-termico-interior/CLASE.md):**
- Calcular el área de un radiador con la ley de Stefan–Boltzmann y un sumidero efectivo.
- Ejercicio 9 · transferencia. En la superficie lunar con día caliente un sumidero efectivo puede estar sobre 300 K.
- 🎯 **Por qué importa:** En el vacío el calor solo sale por radiación; el área del radiador depende de la temperatura y de lo que «ve». La decisión central: ¿cuánta área y qué caudal de refrigerante para evacuar la carga, y cuánto tiempo hay si el enfriamiento falla?
- 🔗 **Se estudia junto con:** Carga térmica, Radiador, Salto de temperatura ΔT, Absortividad solar.

📘 **Dónde se aprende** (1 clase): [B106-C08 · Control térmico interior](../programa/clases/B106/B106-C08-control-termico-interior/CLASE.md).

### Sumidero equivalente

- El sumidero equivalente `T_s` agrupa en una temperatura lo que el radiador ve.

💡 **Cómo se explica en la clase [B86-C12](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md):**
- Con `Q = 20,124 W`, `ε = 0,85`, `T = 300 K` y un sumidero equivalente de `220 K`: `A = Q/(ε σ (T⁴ − T_s⁴)) = 0,0725 m²` (`q = 277,5 W/m²`).
- Límite: el sumidero equivalente no es un balance térmico: ignora la Tierra, el Sol y los intercambios radiativos entre superficies.
- 🎯 **Por qué importa:** Una eficiencia de `92 %` parece alta hasta que se multiplica por las demás etapas y se ve el calor que queda. Cada vatio perdido debe radiarse: el calor decide el tamaño del radiador y la potencia del ala.
- 🔗 **Se estudia junto con:** eficiencia de cadena, disipación, emisividad, flujo.

📘 **Dónde se aprende** (1 clase): [B86-C12 · Eficiencia y disipación](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md).

### SumThreshold

- El umbral `χ σ`. SumThreshold: umbrales sobre la media de `M` muestras consecutivas.

💡 **Cómo se explica en la clase [B51-C13](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md):**
- Umbrales de SumThreshold con `χ₁ = 4` y `ρ = 1,5`: 1 muestras: 4,00 σ, 2 muestras: 2,67 σ, 4 muestras: 1,78 σ, 8 muestras: 1,19 σ, 16 muestras: 0,79 σ.
- M --> S["SumThreshold: M = 1, 2, 4, 8, 16"]
- ⚠️ **Error frecuente:** Creer que SumThreshold es gratis. Se corrige con la tabla de 8.2.
- 🎯 **Por qué importa:** Dejar RFI en los datos degrada la imagen; marcar demasiado pierde señal. La decisión central: ¿qué umbral marca la interferencia sin marcar el ruido, y cómo se detecta la interferencia débil y extendida?
- 🔗 **Se estudia junto con:** interferencia, mediana, MAD, σ robusta.

📘 **Dónde se aprende** (1 clase): [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md).

### Supercúmulo

- Un supercúmulo es una estructura mayor que reúne grupos y cúmulos;

💡 **Cómo se explica en la clase [B01-C15](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md):**
- CL --> SC["Supercúmulo: Laniakea (flujos convergentes)"]
- *Descripción textual:* una jerarquía de cinco niveles ligados por la gravedad: estrellas, galaxia, grupo, cúmulo y supercúmulo; más allá, la expansión domina y lo no ligado se aleja.
- 🎯 **Por qué importa:** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?
- 🔗 **Se estudia junto con:** galaxia, espiral, elíptica, irregular.

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Superficial r_s

- La resistencia aerodinámica `r_a` y la superficial `r_s` controlan el paso del vapor.

💡 **Cómo se explica en la clase [B115-C06](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md):**
- La resistencia superficial pesa menos: con `r_s` de 30, 70 y 120 s/m, `ETc` vale 1,179, 1,149 y 1,112 mm/día.
- Casos de referencia consultados: el capítulo 2 de FAO-56 define la evapotranspiración de referencia (ETo en mm/día), el coeficiente de cultivo `Kc = ETc/ETo` y un cultivo hipotético de 0,12 m de altura, 70 s/m de resistencia superficial y albedo de 0,23.
- 🎯 **Por qué importa:** El cultivo es el mayor flujo de agua de un hábitat con plantas. La decisión central: ¿cuánta agua transpira el cultivo, cuánta se recupera y cuánta hay que reponer, y con qué incertidumbre?
- 🔗 **Se estudia junto con:** evapotranspiración de referencia (ETo), del cultivo (ETc), radiación neta (Rn), déficit de presión de vapor.

📘 **Dónde se aprende** (1 clase): [B115-C06 · Balance de agua y evapotranspiración en cultivos](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md).

### Superficie

- La superficie es la capa química activa en contacto con el gas (aquí, una monocapa); el manto es el hielo enterrado bajo ella.
- El tránsito es el viaje entre destinos; la superficie, la estancia sobre un cuerpo planetario.

💡 **Cómo se explica en la clase [B60-C04](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md):**
- El enterramiento es `F_ent = F_acc (s/ML)⁴`, de modo que la superficie se llena hasta 1 ML y el exceso se entierra.
- Un modelo de dos fases mantiene 79 monocapas como «superficie activa»; el de tres fases, una.
- ⚠️ **Error frecuente:** Tratar todo el hielo como superficie. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un modelo de dos fases trata todo el hielo como si estuviera expuesto en la superficie; en la realidad la mayor parte queda enterrada bajo capas posteriores. La decisión central: ¿qué cambia en la predicción de cuánto hielo se libera al calentar si se distingue la superficie del manto?
- 🔗 **Se estudia junto con:** acreción, desorción térmica, manto, modelo de tres fases.

📘 **Dónde se aprende** (2 clases): [B60-C04 · Balance químico gas-grano: modelos de tres fases](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md); [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Superficie de Petzval

- La superficie de Petzval es la superficie de enfoque sin astigmatismo; su curvatura es la suma de Petzval `Σ φᵢ/nᵢ` (con `n = −1` en un espejo).

💡 **Contexto en la clase [B50-C07](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md):**
- **Idea central (modelo mental):** Como una pantalla de cine curva: las butacas del centro y del borde ven nítido solo si la pantalla sigue la superficie de enfoque.
- 🎯 **Por qué importa:** Un detector plano mal enfocado en el borde pierde resolución: hay que decidir si se acepta, se curva el detector o se agrega un aplanador. La decisión central: ¿cuánto se hunde el foco en el borde y qué lo corrige?
- 🔗 **Se estudia junto con:** tangencial, sagital, suma de Petzval, aplanador.

📘 **Dónde se aprende** (1 clase): [B50-C07 · Curvatura de campo y aplanadores](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md).

### Superficie específica

- La superficie específica es el área por unidad de masa.

💡 **Cómo se explica en la clase [B59-C04](../programa/clases/B59/B59-C04-caracterizacion-de-regolito-lunar/CLASE.md):**
- Obtener el diámetro de Sauter y la superficie específica.
- Ejercicio 7. Calcula la superficie específica de esferas (8.4).
- 🎯 **Por qué importa:** Un tamiz, una tolva o un horno de sinterización se diseñan para una distribución de tamaños, no para un grano. La decisión central: ¿qué fracción de la masa es fina (menor de 20 µm) y cuánto cambia si hablo de número o de masa?
- 🔗 **Se estudia junto con:** desviación geométrica, coeficiente de uniformidad, diámetro de Sauter.

📘 **Dónde se aprende** (1 clase): [B59-C04 · Caracterización de regolito lunar](../programa/clases/B59/B59-C04-caracterizacion-de-regolito-lunar/CLASE.md).

### Superficie numérica

- La superficie numérica es el punto donde `ρ` baja de un umbral (aquí `10³ kg/m³`).

💡 **Contexto en la clase [B27-C02](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md):**
- **Idea central (modelo mental):** Al añadir masa, la presión debe subir; en el régimen no relativista eso exige que la estrella se comprima, y la degeneración responde con poco aumento de presión (exponente `5/3`), así que se encoge más y más. En el régimen ultrarrelativista el exponente `4/3` no alcanza y la estrella no puede sostener más masa.
- 🎯 **Por qué importa:** Las enanas blancas son el destino de la mayoría de las estrellas, sirven de relojes cosmológicos y, al acercarse a su masa límite, pueden explotar. Una relación masa–radio correcta separa masas y radios que la fotometría sola confunde.
- 🔗 **Se estudia junto con:** enana blanca, relación masa–radio, masa de Chandrasekhar, densidad central.

📘 **Dónde se aprende** (1 clase): [B27-C02 · Enanas blancas y límite de Chandrasekhar](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md).

### Supernova

- Una supernova es la explosión de una estrella que brilla durante semanas.
- Una supernova es la explosión final de una estrella masiva o de una enana blanca que acreta.
- Una supernova es la explosión final de una estrella masiva; aquí se toma una energía convencional de `10⁵¹ erg = 10⁴⁴ J` por explosión (valor ilustrativo).

💡 **Cómo se explica en la clase [B02-C12](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md):**
- Las observaciones de S1 para la supernova de 1572 y el cometa de 1577 no mostraron un paralaje apreciable con la precisión de Tycho, por lo que los objetos estaban más allá de la Luna.
- S1 indica que la supernova y el cometa socavaban la división aristotélica entre lo terrestre y lo celeste, y que el movimiento del cometa mostraba que no podían existir esferas sólidas, idea que fue desapareciendo entre 1575 y 1625.
- 🎯 **Por qué importa:** Una teoría solo es tan buena como los datos con que se contrasta. La pregunta motivadora es: ¿qué diferencia hay entre «mirar el cielo» y «observar sistemáticamente», y por qué esa diferencia cambió la astronomía?
- 🔗 **Se estudia junto con:** observación sistemática, precisión angular, minuto de arco, refracción atmosférica.

📖 **Explicado a fondo:** [Supernova](esencial/esencial-m-z.md#supernova) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B02-C12 · Tycho Brahe y observaciones sistemáticas](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md); [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md); [B25-C16 · Retroalimentación estelar](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md).

### Supernovas Ia

- Las supernovas Ia son velas estándar tras la calibración.

💡 **Cómo se explica en la clase [B26-C19](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md):**
- La supernova a `z = 0,5` está un `9,9 %` más lejos en ΛCDM que en el modelo abierto sin Λ, que son `+0,204 mag`; a `z = 1`, `+11,5 %` y `+0,237 mag`.
- Con Pantheon+ (1550 supernovas), `Ω_m = 0,334 ± 0,018` en ΛCDM plano y `w₀ = −0,90 ± 0,14` con supernovas solas, compatible con una constante cosmológica (`w = −1`); combinado con CMB y BAO, `w₀ = −0,978 (+0,024/−0,031)` (S5, resumen).
- 🎯 **Por qué importa:** La aceleración cósmica se descubrió porque las supernovas Ia lejanas aparecían más débiles de lo esperado. Para reproducir ese razonamiento hay que saber calcular la distancia de luminosidad y ver cuánto cambia con el contenido del universo.
- 🔗 **Se estudia junto con:** distancia de luminosidad, distancia comóvil, distancia transversal, módulo de distancia.

📘 **Dónde se aprende** (1 clase): [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md).

### Superposición

- Un sistema es lineal si cumple aditividad (la respuesta a `u₁ + u₂` es la suma de respuestas) y homogeneidad (la respuesta a `a u` es `a` por la respuesta a `u`); juntas, superposición.
- La superposición dice que dos ondas se suman.
- La superposición trata un núcleo como `A` protones.

💡 **Cómo se explica en la clase [B05-C12](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md):**
- Interpretar superposición, ondas estacionarias y batidos.
- 🎯 **Por qué importa:** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.
- 🔗 **Se estudia junto con:** onda mecánica, transversal, longitudinal, longitud de onda.

📘 **Dónde se aprende** (3 clases): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B31-C13 · Rayos cósmicos y cascadas](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md).

### Superposición modal

- La superposición modal es `H_ij = Σ φ_ir φ_jr/(ω_r² − ω² + 2iζ_r ω_r ω)`.

💡 **Cómo se explica en la clase [B84-C33](../programa/clases/B84/B84-C33-respuesta-armonica-y-funciones-de-transferencia-estructural/CLASE.md):**
- El script [armonica.py](armonica.py) calcula `H₂₁` por inversión directa y superposición modal y estima `ζ` (comprueba directa frente a modal (< 1e-9) y `ζ` dentro del 5 %).
- Diferencia relativa maxima entre inversion directa y superposicion modal en 6 frecuencias = 1.6e-15
- 🎯 **Por qué importa:** La función de transferencia dice cuánto se amplifica cada frecuencia entre el punto donde se excita y el punto donde se mide; es la herramienta que usan el análisis y el ensayo de barrido sinusoidal. La decisión central: ¿cuánto se amplifica la respuesta en cada frecuencia y cuánto amortiguamiento tiene cada modo?
- 🔗 **Se estudia junto con:** receptancia, método de potencia mitad, fase.

📘 **Dónde se aprende** (1 clase): [B84-C33 · Respuesta armónica y funciones de transferencia estructural](../programa/clases/B84/B84-C33-respuesta-armonica-y-funciones-de-transferencia-estructural/CLASE.md).

### Supervisión continua

- La supervisión continua es el control durante toda la vida de la actividad.
- La supervisión continua es la vigilancia del Estado tras otorgar la licencia.

💡 **Cómo se explica en la clase [B119-C08](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md):**
- VI: los Estados responden internacionalmente por sus actividades nacionales, públicas o privadas; las privadas requieren autorización y supervisión continua.
- Enunciar el requisito de autorización y supervisión continua del art.
- 🎯 **Por qué importa:** C01 enuncia el art. VI como regla; esta clase lo convierte en un proceso con tiempos y cobertura, lo que ninguna clase del bloque hace.
- 🔗 **Se estudia junto con:** autorización, tasa de llegada, de servicio, tiempo en el sistema.

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
- 🔗 **Se estudia junto con:** tiempo propio, tiempo coordenado, dilatación temporal, longitud propia.

📘 **Dónde se aprende** (4 clases): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md); [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md); [B118-C14 · Reentrada y riesgos en superficie](../programa/clases/B118/B118-C14-reentrada-y-riesgos-en-superficie/CLASE.md); [B127-C02 · Seguros en órbita](../programa/clases/B127/B127-C02-seguros-en-orbita/CLASE.md).

### Superviviente

- Un superviviente es una estrella que aún está en la secuencia principal.

💡 **Contexto en la clase [B24-C19](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md):**
- **Idea central (modelo mental):** Todas nacen juntas; las más masivas viven menos y salen primero. Con el paso del tiempo, el «corte» de masa que ya salió sube hacia las estrellas menos masivas.
- 🎯 **Por qué importa:** La edad de una estrella aislada es difícil de medir; la de un cúmulo se puede leer en su diagrama HR, porque las estrellas más masivas ya han salido de la secuencia principal y el «punto de desvío» marca la edad. Esas edades fijan la cronología de la Galaxia y calibran los modelos.
- 🔗 **Se estudia junto con:** cúmulo estelar, punto de desvío, isócrona, función inicial de masa.

📘 **Dónde se aprende** (1 clase): [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Supresión

- La supresión es el cociente entre `D(1)` en ΛCDM y `a` (en EdS vale 1).
- La supresión descarta el evento y cuenta cuántos.
- Una alarma dependiente se deriva de una causa raíz ya activa; la supresión la oculta para no saturar.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- Calcular la supresión del crecimiento por la constante cosmológica.
- Ejercicio 12 · integrador. Elabora tu *curva de crecimiento*: resuelve el crecimiento por ODE e integral para dos `Ω_m`, la supresión, el `D_C` y el ángulo de la regla BAO a `z = 0,35` en dos modelos.
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.
- 🔗 **Se estudia junto con:** perturbación de densidad, crecimiento lineal, ecuación de crecimiento, oscilaciones acústicas de bariones (BAO).

📘 **Dónde se aprende** (6 clases): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md); [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md); [B88-C10 · Gestión de eventos](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md); [B98-C04 · Interfaces humano-robot para operación remota](../programa/clases/B98/B98-C04-interfaces-humano-robot-para-operacion-remota/CLASE.md); [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md); [B129-C05 · Consentimiento y privacidad de participantes](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md).

### Supresión (dBc)

- Armónico: componente a múltiplo de la frecuencia del transmisor. Supresión (dBc): nivel relativo a la portadora.

💡 **Contexto en la clase [B90-C14](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md):**
- 🎯 **Por qué importa:** Un transmisor de 1 W deja un armónico de −30 dBm; el piso de ruido de un receptor estrecho está cerca de −132 dBm. La diferencia de más de 100 dB se pierde con facilidad en un chasis de 10 cm.
- 🔗 **Se estudia junto con:** EMI, Fuente y víctima, Piso de ruido, I/N.

📘 **Dónde se aprende** (1 clase): [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md).

### Supuesto

- Un supuesto es una condición que se acepta sin comprobarla en ese momento.
- Un supuesto es una condición aceptada (órbitas circulares, masa del planeta despreciable).
- Para un gas diatómico rígido, `κ = 2/7` y `c_p = 7R/(2M)`; es un supuesto de la clase.

💡 **Cómo se explica en la clase [B01-C05](../programa/clases/B01/B01-C05-observacion-frente-a-interpretacion/CLASE.md):**
- Convertir `z` en velocidad con `v ≈ c·z` agrega un supuesto: que `z` es pequeño y que el corrimiento se interpreta como movimiento aparente.
- (2) ¿Se obtiene de datos mediante razonamiento o cálculo que cualquiera puede repetir con los mismos supuestos?
- 🎯 **Por qué importa:** En septiembre de 2011 la colaboración OPERA publicó que neutrinos enviados desde el CERN habían llegado a su detector, a unos 730 km, 60,7 ns antes de lo que tardaría la luz (S1, versión 1). Una cifra medida pasó rápidamente a titulares que decían otra cosa.
- 🔗 **Se estudia junto con:** observación, dato, inferencia, modelo.

📘 **Dónde se aprende** (3 clases): [B01-C05 · Observación frente a interpretación](../programa/clases/B01/B01-C05-observacion-frente-a-interpretacion/CLASE.md); [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B54-C15 · Atmósferas de gigantes gaseosos](../programa/clases/B54/B54-C15-atmosferas-de-gigantes-gaseosos/CLASE.md).

### Suscripción

- La suscripción es acceso por un plazo a un precio fijo.

💡 **Cómo se explica en la clase [B125-C02](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md):**
- El ejemplo conductor es sintético: una suscripción anual de `120 000` u.m. pagada por adelantado se reconoce a `10 000` u.m. por mes; un cliente con `ARPU = 1 000`, margen `70 %` y abandono `2 %` mensual vale `35 000` u.m.
- Descripción larga: la suscripción reparte el ingreso en 12 partes iguales aunque se cobre al inicio; el servicio concentra el ingreso en cuatro hitos; el valor de vida cae a la mitad cuando el abandono se duplica.
- 🎯 **Por qué importa:** El modelo de ingresos define cuándo entra el dinero y cuánto vale un cliente; ninguna clase anterior lo trata. La decisión central: ¿cuánto vale un cliente de suscripción, cuándo se reconoce su ingreso y cuánto abandono puede tolerar el negocio?
- 🔗 **Se estudia junto con:** ingreso diferido, reconocimiento ratable, hito, ARPU.

📘 **Dónde se aprende** (1 clase): [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md).

### Sustentación

- El coeficiente de arrastre es `Cd = D/(q·A)` y el de sustentación `CL = L/(q·A)`.
- La fuerza aerodinámica se descompone en arrastre `D = Cd·q·A` y sustentación `L = CL·q·A`.

💡 **Cómo se explica en la clase [B77-C03](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md):**
- Una sustentación pequeña ya carga la estructura de forma lateral.
- *Descripción textual:* el tiempo da altitud y velocidad; de ahí sale la presión dinámica, con la que se calculan arrastre, sustentación y el máximo de `q`.
- 🎯 **Por qué importa:** El momento de mayor carga aerodinámica no es el de mayor velocidad ni el de menor altitud. La decisión central: ¿cuándo ocurre el máximo de la presión dinámica y qué fuerzas produce?
- 🔗 **Se estudia junto con:** presión dinámica, fuerza aerodinámica, arrastre, Max-q.

📘 **Dónde se aprende** (2 clases): [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md); [B77-C04 · Coeficientes de arrastre y sustentación](../programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/CLASE.md).

### Sustentación arriba/abajo

- La sustentación arriba/abajo idealiza el balanceo del vector de sustentación.

💡 **Contexto en la clase [B77-C25](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md):**
- 🎯 **Por qué importa:** El corredor es la tolerancia que se le deja a la navegación y a la guía antes de entrar. La decisión central: ¿entre qué ángulos puede entrar el vehículo, cuánto ensancha el corredor la sustentación y cuándo falla la estimación de Allen–Eggers?
- 🔗 **Se estudia junto con:** corredor de entrada, límite empinado, límite somero, perigeo kepleriano.

📘 **Dónde se aprende** (1 clase): [B77-C25 · Corredores de entrada y límites de trayectoria](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md).

### Sustitución

- La sustitución (o cambio de variable) reemplaza una expresión `u = g(x)` por una nueva variable; su justificación es la regla de la cadena: `∫ f(g(x)) g′(x) dx = ∫ f(u) du` (S1, §1.4(v), ec. 1.4.28 en forma definida).
- La sustitución despeja una incógnita y la reemplaza en las demás.

💡 **Cómo se explica en la clase [B04-C03](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md):**
- La sustitución es clara en 2×2 y cuando una incógnita queda despejada.
- Resolver sistemas 2×2 por sustitución y por eliminación.
- 🎯 **Por qué importa:** Un detector no entrega «brillo»: entrega cuentas. Para convertir cuentas en flujo hay que descubrir dos números, una pendiente y un desfase, y para ello se miden dos fuentes de referencia.
- 🔗 **Se estudia junto con:** sistema de ecuaciones, lineal, solución, compatible determinado.

📘 **Dónde se aprende** (2 clases): [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md); [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md).

### Sustitución hacia atrás

- La sustitución hacia atrás despeja desde la última ecuación.

💡 **Cómo se explica en la clase [B10-C05](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md):**
- Resolver un sistema pequeño por eliminación gaussiana y sustitución hacia atrás.
- Ejercicio 7. Resuelve por sustitución hacia atrás `[[2,1,1],[0,3,2],[0,0,4]] x = (7, 8, 4)`.
- 🎯 **Por qué importa:** Para fijar la posición de un objeto a partir de las distancias a tres estaciones se plantean tres ecuaciones con dos incógnitas (plano). Los sistemas reales tienen decenas o miles de incógnitas: parámetros orbitales, sesgos de relojes, coeficientes de calibración.
- 🔗 **Se estudia junto con:** sistema lineal, matriz ampliada, operación elemental de fila, eliminación gaussiana.

📘 **Dónde se aprende** (1 clase): [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md).

### Sustituto gratuito

- El sustituto gratuito es un producto sin precio que cubre parte del valor.

💡 **Cómo se explica en la clase [B125-C01](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md):**
- Ninguna de las dos fuentes da precios ni cuotas de mercado: son el contexto de que existe un sustituto gratuito.
- Incorporar un sustituto gratuito que cubre una fracción `s` del valor y deducir `P* = (1 − s) W / 2`.
- 🎯 **Por qué importa:** [B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) trata los segmentos de la industria en general; ninguna clase explica por qué un dato crudo puede valer cero y aun así sostener empresas.
- 🔗 **Se estudia junto con:** disposición a pagar, ingreso por cliente, cadena de valor, dato abierto.

📘 **Dónde se aprende** (1 clase): [B125-C01 · Mercado de datos espaciales](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md).

### Sustracción del continuo

- La sustracción del continuo con un polinomio de orden `p`.

💡 **Cómo se explica en la clase [B51-C14](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de la calibración de banda en síntesis*: solución, ruido inyectado, sustracción del continuo y límites.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de la calibración de banda en síntesis*: solución, ruido inyectado, sustracción del continuo y límites.
- 🎯 **Por qué importa:** Una línea débil sobre un continuo brillante solo se ve si la banda está calibrada mejor que la razón línea/continuo. La decisión central: ¿cuánto ruido inyecta la solución de banda y por qué no basta con restar un polinomio?
- 🔗 **Se estudia junto con:** solución de banda, calibrador de banda, canales libres de línea, ruido inyectado.

📘 **Dónde se aprende** (1 clase): [B51-C14 · Calibración de banda en la reducción de datos de síntesis](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md).

### Sustrato

- El sustrato retiene agua según su profundidad y porosidad.

💡 **Cómo se explica en la clase [B59-C14](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md):**
- Un sustrato de 0,20 m y porosidad 0,5 almacena `100 kg/m²`: se seca en `33,3 días` sin riego.
- Ejercicio 11 · transferencia. ¿Cuántos días tarda en secarse el sustrato sin riego?
- 🎯 **Por qué importa:** Cultivar exige luz, y la luz eléctrica cuesta potencia. La decisión central: ¿cuántos metros cuadrados y cuántos kilovatios necesita un cultivo para producir el oxígeno de una persona?
- 🔗 **Se estudia junto con:** PPFD, fotones por O₂, eficacia, evapotranspiración.

📘 **Dónde se aprende** (1 clase): [B59-C14 · Agricultura y sustratos artificiales](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md).

### SVD

- La SVD de una matriz real `A` de `m × n` es `A = U Σ Vᵀ`, con `U` (`m × m`, o `m × r` en la versión «económica») y `V` (`n × n`) de columnas ortonormales, y `Σ` diagonal con los valores singulares `σ₁ ≥ σ₂ ≥ … ≥ 0`.
- La solución por SVD usa `B = Σ bᵢ rᵢᵀ = U S Vᵀ` y `A = U diag(1,1,det) Vᵀ`.

💡 **Cómo se explica en la clase [B10-C11](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md):**
- La SVD nunca engaña, pero hay que elegir el umbral.
- Ninguno es dato real; sirven para ver qué dice la SVD.
- 🎯 **Por qué importa:** Un instrumento entrega una imagen de miles de píxeles; la mayor parte de su estructura se puede describir con muy pocos patrones. Una matriz de medidas puede tener columnas casi redundantes, de modo que un cálculo «técnicamente posible» sea inútil.
- 🔗 **Se estudia junto con:** valores singulares, vectores singulares izquierdos, derechos, rango efectivo.

📘 **Dónde se aprende** (2 clases): [B10-C11 · Valores singulares y SVD](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md); [B74-C14 · Navegación con cámaras estelares](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md).

### SVD de Wahba

- El SVD de Wahba factoriza `B = Σ w_i b_i r_iᵀ = U S Vᵀ` y toma `A = U diag(1, 1, det U det V) Vᵀ`.

💡 **Cómo se explica en la clase [B87-C09](../programa/clases/B87/B87-C09-estimacion-de-actitud/CLASE.md):**
- Plantear la función de pérdida de Wahba `L(A) = ½ Σ w_i |b_i − A r_i|²`.
- La evidencia es la comparación de métodos de estimación de actitud con la pérdida de Wahba del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Cada sensor de vector da solo dos grados de libertad; la actitud completa exige combinarlos. La decisión central: ¿qué método usar, cómo ponderar el sensor mejor y cuánto importa el ángulo entre los vectores?
- 🔗 **Se estudia junto con:** pérdida de Wahba, método q, TRIAD, vector primario.

📘 **Dónde se aprende** (1 clase): [B87-C09 · Estimación de actitud](../programa/clases/B87/B87-C09-estimacion-de-actitud/CLASE.md).

### SWEG

- SMAC: concentración máxima permitida en nave. SWEG: guía de agua potable.

💡 **Cómo se explica en la clase [B106-C24](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md):**
- La página consultada dice qué son los SMAC y quién los fija; no da valores (los oficiales están en JSC 20584 y los de agua, SWEG, en JSC 63414).
- 🎯 **Por qué importa:** Evaluar el aire exige límites y una regla para combinar contaminantes; ninguno basta por sí solo. La decisión central: ¿cumple una mezcla de contaminantes su límite combinado y qué compuesto la domina?
- 🔗 **Se estudia junto con:** SMAC, Índice de riesgo aditivo, ppm, mg/m³.

📘 **Dónde se aprende** (1 clase): [B106-C24 · Calidad del aire y límites de exposición en cabina](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md).
