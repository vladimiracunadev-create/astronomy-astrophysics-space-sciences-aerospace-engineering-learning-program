# Anexo J · Estudios de caso a fondo

[⬅️ Anexo I](ANEXO-I-escalas-formulas-y-calculadora.md) · [Índice de anexos](README.md)

Las fichas de los anexos anteriores cuentan *qué pasó*. Estos diez casos explican *cómo y por qué*: el problema de ingeniería o de ciencia, los números que lo gobiernan, lo que falló o estuvo a punto de fallar y lo que cambió después. Cada caso termina con un **ejercicio con solución**, que puedes repetir con la [calculadora científica](../herramientas/calculadora_cientifica.py).

> **Estado del texto.** Síntesis propia con cifras redondeadas, pendiente de revisión disciplinar y de contraste con informes oficiales (nivel E0). Los ejercicios usan datos aproximados con fines didácticos.

**Cómo usar un caso:** lee el contexto, intenta predecir el problema antes de leerlo, haz el ejercicio y compara con la solución, y discute las preguntas de reflexión.

---

## Caso 1 · Apollo 11: los últimos minutos del descenso (1969)

**Contexto.** El 20 de julio de 1969 el módulo lunar *Eagle* se separó del módulo de mando y comenzó su descenso desde una órbita de ≈ 110 km de altura. Neil Armstrong y Buzz Aldrin llevaban un computador de guiado con una memoria de unas 36 000 palabras.

**El problema.** Quitar a una nave toda su velocidad orbital (≈ 1,63 km/s) y posarla con menos de un par de metros por segundo, con un solo motor de descenso regulable, sin poder abortar sin riesgo durante buena parte del trayecto. Además, el combustible se consume a ritmo propio: cada segundo de indecisión cuesta Δv.

**Lo que ocurrió.** Durante el descenso el computador emitió alarmas (códigos 1201 y 1202) porque el radar de encuentro —conectado en una configuración que no estaba prevista para esa fase— le saturaba de tareas. El software estaba diseñado para **descartar las tareas de menor prioridad y reiniciar**, de modo que el guiado esencial siguió funcionando. El control de misión (con un joven ingeniero, Steve Bales, y el técnico Jack Garman) decidió continuar. Cerca del suelo, Armstrong vio que el punto previsto estaba lleno de rocas, tomó el control manual y voló unos segundos más para encontrar un lugar liso. Se posaron con muy poco propelente en los tanques.

**Lo que enseña.**
- **Prioridades en software crítico:** un sistema bien diseñado falla *hacia lo seguro*, no hacia lo inútil.
- **Ingeniería de factores humanos:** el piloto necesitaba datos claros y tiempo para decidir; las alarmas eran la medida de la carga de trabajo.
- **Margen:** la reserva de combustible no es un lujo; es el espacio de decisión.

**Ejercicio.** ¿Cuál era la velocidad orbital circular a 110 km sobre la Luna? *Solución:* r = 1 737,4 + 110 = 1 847,4 km; v = √(GM/r) con GM_Luna = 4,9028 × 10¹² m³/s² → v ≈ **1,63 km/s**. Comprobación: `calc "sqrt(GM_luna/(R_luna+110e3))"`.

**Preguntas.** ¿Por qué no se puede "frenar" simplemente con paracaídas en la Luna? ¿Qué decisión de diseño evitó que el reinicio del computador perdiera el rumbo?

📘 [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B88](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md "Aviónica y software crítico espacial"), [B96](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md "Control y operación de misiones espaciales").

---

## Caso 2 · Voyager 2 y la alineación de los planetas exteriores (1977–1989)

**Contexto.** A finales de los años 60 se calculó que, hacia 1977, Júpiter, Saturno, Urano y Neptuno estarían alineados de forma que una sola nave podría visitarlos aprovechando la **asistencia gravitatoria** de cada uno. Una alineación así ocurre cada ≈ 175 años. Voyager 2 se lanzó el 20 de agosto de 1977 y llegó a Júpiter (1979), Saturno (1981), Urano (enero de 1986) y Neptuno (agosto de 1989).

**El problema.** Llegar al sistema solar exterior con la energía de un cohete que habría necesitado décadas sin las asistencias; y comunicar desde miles de millones de kilómetros con un transmisor de unos 23 W (menos que una bombilla pequeña).

**Cómo se resolvió.**
- **Energía:** generadores termoeléctricos de radioisótopos (RTG) que convierten el calor del plutonio-238 en electricidad; su potencia decae con el tiempo (vida media del Pu-238 ≈ 87,7 años, más degradación de los termopares), por lo que los instrumentos se van apagando en un orden planificado.
- **Comunicación:** antena de alta ganancia de 3,7 m y receptores de la Red de Espacio Profundo; la tasa de datos bajó de decenas de kbit/s en Júpiter a cientos de bit/s hoy.
- **Longevidad:** una misión planeada para 4–5 años lleva casi medio siglo operando, con reparaciones de software enviadas por radio.

**Lo que enseña.** Que la **geometría orbital** (la alineación) vale más que el tamaño del cohete; que la energía y el enlace de comunicaciones son los límites de una misión lejana; y que diseñar para la longevidad paga.

**Ejercicio.** Voyager 1 está a ≈ 165 UA. ¿Cuánto tarda una señal en llegar? *Solución:* 165 × 499 s ≈ 82 300 s ≈ **22,9 horas**. Comprobación: `calc "165*UA/c/3600"`.

**Preguntas.** Si la potencia del transmisor es fija y la distancia se duplica, ¿cómo cambia la señal recibida? (*Respuesta:* cae a la cuarta parte, ley del inverso del cuadrado.)

📘 [B75](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias"), [B86](../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md "Sistemas de potencia y energía espacial"), [B89](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital").

---

## Caso 3 · Hubble: el espejo equivocado (1990–1993)

**Contexto.** El Telescopio Espacial Hubble se lanzó en abril de 1990 con un espejo primario de 2,4 m. Las primeras imágenes de estrellas mostraban un halo borroso: la luz no se concentraba en un punto.

**El problema.** El espejo estaba pulido con una forma incorrecta: demasiado plano en el borde por ≈ 2 µm (unas treinta veces menos que el grosor de un cabello). La causa fue un instrumento de verificación (un corrector nulo) armado con una lente mal colocada por ≈ 1,3 mm. El espejo se había pulido con gran perfección... según una regla equivocada. Lo que se pulió estaba bien medido, pero medido con un patrón erróneo.

**Cómo se resolvió.** Como el error era conocido y preciso, se diseñó óptica correctora que lo cancelara, como unas "gafas": la instalaron astronautas en la misión STS-61 (diciembre de 1993) con el sistema COSTAR para los instrumentos antiguos, y las cámaras posteriores incorporaron la corrección en su diseño.

**Lo que enseña.** Verificación independiente: una prueba de punta a punta con un segundo método habría detectado el error en tierra. También mostró el valor de diseñar para el **servicio en órbita**.

**Ejercicio.** ¿Cuál es el límite de difracción de Hubble a 550 nm? *Solución:* θ = 1,22 · 550 × 10⁻⁹ / 2,4 ≈ 2,8 × 10⁻⁷ rad ≈ **0,058″**. Comprobación: `calc "1.22*550e-9/2.4/(pi/648000)"`.

**Preguntas.** ¿Por qué era mejor corregir en lugar de rehacer el espejo? ¿Qué prueba independiente propondrías?

📘 [B41](../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md "Óptica geométrica y diseño de telescopios"), [B47](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md "Instrumentación y observatorios espaciales"), [B90](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md "Integración, ensayos y calificación espacial"), [B23](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md "Verificación y validación de software científico").

---

## Caso 4 · Rosetta y Philae: una cita con un cometa (2004–2016)

**Contexto.** La sonda europea Rosetta se lanzó el 2 de marzo de 2004 hacia el cometa 67P/Churiumov–Guerasimenko. Necesitó **cuatro asistencias gravitatorias** (Tierra 2005, Marte 2007, Tierra 2007 y 2009) y un viaje de diez años para igualar la velocidad del cometa.

**El problema.** Encontrarse con un cuerpo de ≈ 4 km que gira cada 12,4 horas, con gravedad casi nula, y posar un módulo (Philae). La velocidad de escape del cometa es de unos 0,8 m/s: un salto a paso rápido bastaría para escapar.

**Lo que ocurrió.**
- Entre 2011 y 2014 la nave estuvo en hibernación profunda para ahorrar energía (muy lejos del Sol, con paneles insuficientes), y despertó puntualmente en enero de 2014.
- Llegó en agosto de 2014 y cartografió el cometa. Philae se separó el 12 de noviembre de 2014.
- Los arpones que debían anclarlo **no se dispararon**; Philae rebotó, volvió a tocar y se detuvo en un lugar con sombra, con poca luz para sus paneles. Aun así transmitió datos durante unos días y reapareció brevemente en 2015.
- En septiembre de 2016 Rosetta terminó su misión descendiendo sobre el cometa.

**Lo que enseña.** Navegación interplanetaria con asistencias; operar a *velocidades de paseo* con gravedad casi nula; y que un fallo parcial (un módulo en sombra) no invalida el éxito científico de la misión.

**Ejercicio.** Estima la velocidad de escape de 67P con M ≈ 1,0 × 10¹³ kg y R ≈ 2 km. *Solución:* v = √(2GM/R) = √(2 · 6,674 × 10⁻¹¹ · 10¹³ / 2 000) ≈ **0,82 m/s**. Comprobación: `calc "sqrt(2*G*1e13/2000)"`.

**Preguntas.** ¿Por qué el anclaje por arpón era crítico? ¿Qué compromisos se hacen al elegir un lugar de aterrizaje?

📘 [B58](../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md "Asteroides, cometas y defensa planetaria"), [B75](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias"), [B76](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md "Dinámica cislunar y operaciones de proximidad").

---

## Caso 5 · James Webb: doblar un telescopio (2021)

**Contexto.** El Telescopio Espacial James Webb (6,5 m, infrarrojo) debía caber en la cofia de un Ariane 5, de modo que se **plegó** y se desplegó tras el lanzamiento (25 de diciembre de 2021). Opera en el punto L2 Sol–Tierra, a ≈ 1,5 millones de km.

**El problema.** Un telescopio infrarrojo debe estar *muy frío* (por debajo de ≈ 50 K el instrumental) para que su propio calor no tape el cielo. Hace falta un parasol del tamaño de una cancha de tenis, plegado en un cohete y desplegado sin ninguna reparación posible: estaba demasiado lejos para una misión de servicio.

**Cómo se resolvió.**
- **Parasol de cinco capas** de película aislante que reduce unos 300 °C de diferencia entre el lado caliente (≈ +85 °C) y el frío (≈ −233 °C).
- **Espejo segmentado** de 18 hexágonos de berilio recubiertos de oro, que se alinean con actuadores con una precisión de nanómetros.
- **Despliegue paso a paso** durante dos semanas, con cientos de mecanismos que tenían que funcionar sin repetición, y un periodo de puesta en marcha de unos seis meses.

**Lo que enseña.** Gestión de riesgo con "puntos únicos de fallo", pruebas en cámaras de vacío y de enfriamiento, y la planificación de operaciones de despliegue.

**Ejercicio.** Límite de difracción de Webb a 2 µm. *Solución:* θ = 1,22 · 2 × 10⁻⁶ / 6,5 ≈ 3,8 × 10⁻⁷ rad ≈ **0,077″**; y la luz tarda 1,5 × 10⁹ / c ≈ **5 s** en llegar desde L2. Comprobación: `calc "1.22*2e-6/6.5/(pi/648000)"`.

**Preguntas.** ¿Por qué un telescopio infrarrojo debe estar frío? ¿Por qué L2 y no una órbita baja?

📘 [B47](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md "Instrumentación y observatorios espaciales"), [B85](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md "Gestión térmica y entorno espacial"), [B42](../programa/tronco-comun/B42-optica-fisica-y-optica-adaptativa.md "Óptica física y óptica adaptativa"), [B73](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md "Mecánica celeste, resonancias y caos").

---

## Caso 6 · DART: mover un asteroide (2022)

**Contexto.** El 26 de septiembre de 2022 la nave DART impactó a ≈ 6,1 km/s contra Dimorphos (≈ 160 m), la luna del asteroide Didymos, para probar la **desviación cinética**. La luna orbitaba a Didymos en 11 h 55 min.

**El problema.** Medir cuánto cambia la órbita tras el impacto. Un cambio de velocidad de milímetros por segundo se traduce, tras muchas vueltas, en minutos de diferencia del período.

**Resultado.** El período bajó a 11 h 23 min, es decir, unos **32 minutos** menos, mucho más de lo mínimo exigido (73 s). Esto implica que el **retroceso del material expulsado** (eyecta) multiplicó el empuje de la nave por un factor β de entre ≈ 2 y 4.

**Lo que enseña.** El impacto de una nave es una fracción del efecto: la eyecta lo amplifica. El resultado depende de la estructura del asteroide (una pila de escombros, no un bloque sólido). Confirma que la defensa planetaria es posible con aviso de años.

**Ejercicio.** Estima Δv de Dimorphos con m = 570 kg, v = 6,1 km/s, β = 3,6 y M_Dimorphos ≈ 4,3 × 10⁹ kg. *Solución:* Δp = β m v = 3,6 · 570 · 6 100 ≈ 1,25 × 10⁷ kg·m/s; Δv = Δp / M ≈ **2,9 mm/s**. Comprobación: `calc "3.6*570*6100/4.3e9"`.

**Preguntas.** ¿Por qué un cambio de milímetros por segundo es suficiente si se aplica con años de antelación? ¿Qué mide una misión de seguimiento (Hera)?

📘 [B58](../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md "Asteroides, cometas y defensa planetaria"), [B75](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias"), [B76](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md "Dinámica cislunar y operaciones de proximidad").

---

## Caso 7 · Challenger: la decisión de lanzar (1986)

**Contexto.** El 28 de enero de 1986 el transbordador *Challenger* se desintegró 73 segundos después del despegue, con siete tripulantes. La mañana fue excepcionalmente fría para Florida, con temperaturas alrededor de 0 °C o menos en la plataforma, muy inferiores a las de lanzamientos anteriores.

**El problema técnico.** Un sello de goma (junta tórica, *O-ring*) en una unión del propulsor sólido se endurece con el frío y no sella a tiempo cuando se presuriza; los gases calientes escaparon, erosionaron la estructura y provocaron el fallo.

**El problema humano.** Ingenieros del fabricante del propulsor habían advertido, la víspera, de que el frío ponía en riesgo los sellos. La decisión de continuar se tomó bajo presión de calendario. La Comisión Rogers (con el físico Richard Feynman, que demostró en una audiencia el endurecimiento de la goma en agua helada) concluyó que había un problema de *cultura de seguridad*: se había "normalizado" una anomalía que ya aparecía en vuelos anteriores, porque no había causado una pérdida.

**Lo que enseña.**
- **Normalización de la desviación:** aceptar un riesgo repetido como si fuera normal.
- **Comunicación del riesgo:** la información técnica debe llegar a quien decide, sin filtros.
- **Autoridad para detener:** una cultura donde cualquiera pueda decir "no" a un lanzamiento.

**Ejercicio de análisis.** Reconstruye la cadena de decisiones: ¿qué dato faltó, quién lo tenía y cuál es el criterio explícito para detener un lanzamiento?

**Preguntas.** ¿Cómo distinguir una anomalía tolerable de una que es una advertencia? ¿Qué pasa con la responsabilidad cuando se descubre el error años después?

📘 [B110](../programa/tronco-comun/B110-emergencias-y-seguridad-de-tripulacion.md "Emergencias y seguridad de tripulación"), [B96](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md "Control y operación de misiones espaciales"), [B111](../programa/tronco-comun/B111-factores-humanos-y-liderazgo-de-tripulacion.md "Factores humanos y liderazgo de tripulación").

---

## Caso 8 · GPS y la relatividad (desde 1978)

**Contexto.** Cada satélite GPS lleva relojes atómicos. El receptor mide la diferencia entre la hora de emisión y la de llegada de la señal; multiplicada por *c* da la distancia. Un error de un nanosegundo equivale a ≈ 0,3 m.

**El problema.** Los relojes satelitales están en un entorno distinto del de los de tierra: se mueven rápido (v ≈ 3,87 km/s) y están en un campo gravitatorio más débil (r ≈ 26 560 km). Según la relatividad, ambos efectos cambian el ritmo del reloj.

**Los números.**
- **Efecto de velocidad (relatividad especial):** el reloj en movimiento va más lento: −v²/(2c²) · 86 400 s ≈ **−7,2 µs/día**.
- **Efecto gravitacional (relatividad general):** el reloj más alto va más rápido: (GM/c²)(1/R_T − 1/r) · 86 400 s ≈ **+45,7 µs/día**.
- **Neto:** ≈ **+38,5 µs/día**. Sin corregirlo, el error de distancia crecería ≈ 11,5 km por día. Por eso los relojes se ajustan antes del lanzamiento.

**Lo que enseña.** La relatividad no es una curiosidad: sin ella la navegación por satélite falla. También ilustra el uso de **órdenes de magnitud** y de unidades (µs, ns, km) para decidir qué efecto importa.

**Ejercicio.** Calcula el efecto de velocidad. *Solución:* (3 870)² / (2 · (299 792 458)²) · 86 400 ≈ 7,2 × 10⁻⁶ s. Comprobación: `calc "3870**2/(2*c**2)*86400*1e6"`.

**Preguntas.** ¿Qué pasaría con un reloj en la Luna? ¿Qué otros sistemas (telecomunicaciones, finanzas) dependen de la sincronización por GPS?

📘 [B13](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas"), [B39](../programa/tronco-comun/B39-relatividad-general-avanzada.md "Relatividad general avanzada"), [B74](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md "Estimación de órbitas y navegación espacial"), [B89](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital").

---

## Caso 9 · Mars Climate Orbiter: un error de unidades (1999)

**Contexto.** La sonda de NASA Mars Climate Orbiter debía entrar en órbita de Marte el 23 de septiembre de 1999. Se perdió: pasó mucho más cerca del planeta de lo previsto y se destruyó en la atmósfera.

**La causa.** Un programa en tierra entregaba el impulso de los propulsores en **libras-fuerza por segundo** (unidades inglesas), mientras que el software de navegación esperaba **newton por segundo** (SI). La diferencia es un factor de ≈ **4,45**. Las pequeñas correcciones del rumbo, acumuladas durante meses, llevaron la nave a ≈ 57 km de altura sobre Marte, en lugar de los ≈ 226 km previstos; por debajo de ≈ 80 km, la nave no podía sobrevivir.

**Lo que enseña.** Esta es la lección central del [Anexo I](ANEXO-I-escalas-formulas-y-calculadora.md): **las unidades son parte del dato**. Fallaron también las revisiones: hubo señales de discrepancia en la navegación que no se investigaron a fondo.

**Ejercicio.** Convierte 1 lbf·s a N·s. *Solución:* 1 lbf = 4,448 N, así que 1 lbf·s = **4,448 N·s**. Si 100 lbf·s se interpretan como 100 N·s, el impulso es **4,45 veces menor** que el real.

**Preguntas.** ¿Qué controles automáticos habrías puesto en la interfaz entre los dos programas? ¿Por qué estos errores se detectan mejor con unidades explícitas en cada variable?

📘 [B13](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas"), [B23](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md "Verificación y validación de software científico"), [B83](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md "Ingeniería de sistemas y diseño de misiones").

---

## Caso 10 · Ariane 5, vuelo 501: 37 segundos (1996)

**Contexto.** El 4 de junio de 1996 el primer Ariane 5 se desvió de su trayectoria y se autodestruyó a los 37 segundos de vuelo. Llevaba cuatro satélites científicos (Cluster). La pérdida se estimó en cientos de millones de dólares.

**La causa.** El software de navegación inercial se reutilizó del Ariane 4. En el Ariane 5, más potente, un valor relacionado con la velocidad horizontal excedió el rango de un entero de 16 bits en una conversión desde un número de punto flotante de 64 bits. Se produjo una excepción no controlada; el computador principal y el de respaldo (idéntico) fallaron del mismo modo. Esa función ni siquiera era necesaria después del despegue.

**Lo que enseña.**
- **Reutilizar no es verificar:** el código era correcto en un contexto distinto.
- **Redundancia idéntica no protege contra fallos de diseño**; hace falta diversidad.
- **Pruebas con datos realistas** y revisión de las hipótesis de entorno.

**Ejercicio.** ¿Cuál es el mayor entero con signo de 16 bits? *Solución:* 2¹⁵ − 1 = **32 767**. Un valor de 40 000 en esa conversión desborda. Comprobación: `calc "2**15-1"`.

**Preguntas.** ¿Cómo se prueba un software heredado en un contexto nuevo? ¿Qué diferencia hay entre redundancia de hardware y de diseño?

📘 [B88](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md "Aviónica y software crítico espacial"), [B23](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md "Verificación y validación de software científico"), [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada").

---

## Cómo analizar un caso por tu cuenta

1. **Resume en tres frases** el contexto, el problema y el desenlace.
2. **Identifica la restricción física** que lo gobierna (energía, tiempo, distancia, temperatura, información).
3. **Calcula un orden de magnitud** con las fórmulas del [Anexo I](ANEXO-I-escalas-formulas-y-calculadora.md).
4. **Busca la causa raíz** (técnica, de proceso o de cultura) y distingue entre síntoma y causa.
5. **Escribe una lección transferible** a otro proyecto.

[⬅️ Anexo I](ANEXO-I-escalas-formulas-y-calculadora.md) · [Índice de anexos](README.md)
