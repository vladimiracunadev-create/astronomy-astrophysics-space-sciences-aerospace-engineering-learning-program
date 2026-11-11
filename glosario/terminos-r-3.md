# Términos · R (parte 3 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · **R** · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-r.md) · [2](terminos-r-2.md) · **3**

### Retardo geométrico

- El retardo geométrico `τ = B·ŝ/c`.

💡 **Cómo se explica en la clase [B51-C09](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md):**
- Con `B = 1000` m, `δ = 30°` y `ν = 1,4` GHz, el retardo geométrico máximo es 2,8887 µs y la tasa de franjas en `H = 0` es -0,294911 Hz.
- B = 1000 m ; dec = 30 grados ; nu = 1.4 GHz ; retardo geometrico maximo = 2.8887 us
- 🎯 **Por qué importa:** Si se promedia sin detener las franjas, la señal se anula. La decisión central: ¿qué tasa de franjas tiene una fuente, cuánto se pierde al promediar y qué precisión pide el modelo?
- 🔗 **Se estudia junto con:** ángulo horario, tasa de franjas, fringe stopping, función seno cardinal.

📘 **Dónde se aprende** (2 clases): [B46-C14 · Líneas de base interferométricas](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md); [B51-C09 · Fringe stopping y rotación de fase por retardo geométrico](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md).

### Retardo instrumental

- El retardo instrumental es el tiempo que la señal tarda en los equipos.

💡 **Cómo se explica en la clase [B74-C03](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md):**
- Paso 4 · Lectura. El ruido del receptor es solo una parte del error: el retardo instrumental y la troposfera suelen dominar (clase C05).
- 🎯 **Por qué importa:** Un nanosegundo son quince centímetros de alcance, y un pulso ancho en ruido se mide con nanosegundos de incertidumbre. La decisión central: ¿cuánta precisión de alcance permite el ancho de banda y la relación señal/ruido, y qué hay que corregir además del retardo?
- 🔗 **Se estudia junto con:** tiempo de ida y vuelta, alcance, cota de Cramér–Rao, ancho de banda efectivo.

📘 **Dónde se aprende** (1 clase): [B74-C03 · Medición de alcance por radio](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md).

### Retardo ionosférico

- El retardo ionosférico es proporcional al TEC y a `1/f²`.
- El retardo ionosférico `K TEC/(c ν²)`.

💡 **Cómo se explica en la clase [B51-C10](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md):**
- *Descripción textual:* el retardo troposférico se mapea con la elevación y el ionosférico se elimina con dos frecuencias.
- Calcular el retardo ionosférico con la `K` derivada de NIST.
- 🎯 **Por qué importa:** Un error atmosférico de centímetros es un error de posición en geodesia y un error de fase en imagen. La decisión central: ¿cómo se mapea el retardo con la elevación y cómo se separa lo dispersivo de lo no dispersivo?
- 🔗 **Se estudia junto con:** retardo cenital, función de mapeo, elevación, capa delgada.

📘 **Dónde se aprende** (2 clases): [B51-C10 · Retardo troposférico e ionosférico en VLBI y su modelado](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md); [B57-C29 · Correcciones atmosféricas en altimetría](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md).

### Retardo ionosférico de grupo

- El retardo ionosférico de grupo de primer orden es `Δ = 40,3·TEC/f²` (m, con TEC en el/m² y `f` en Hz).

💡 **Cómo se explica en la clase [B89-C21](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md):**
- ⚠️ **Error frecuente:** Aplicar el retardo ionosférico como de fase en vez de grupo. Se corrige con el vocabulario: aquí es de grupo (el de fase tiene signo opuesto).
- 🎯 **Por qué importa:** La ionosfera es el mayor error de un receptor GNSS de una sola frecuencia y el origen de pérdidas de señal en regiones ecuatoriales y polares; sin entenderla no se puede interpretar un error de posición. La decisión central: ¿cuánto error añade la ionosfera, cómo se elimina y cuándo el centelleo hace perder la señal?
- 🔗 **Se estudia junto con:** factor de oblicuidad, combinación libre de ionosfera, índice S4.

📘 **Dónde se aprende** (1 clase): [B89-C21 · Efectos ionosféricos y centelleo en señales GNSS](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md).

### Retardo residual

- El retardo residual `τ₀`: pendiente de fase.

💡 **Cómo se explica en la clase [B51-C04](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md):**
- Con 256 canales sobre 128 MHz, un retardo residual inyectado de 3,0 ns y una reflexión de amplitud 0,05 a 40 ns (todo sintético), el ajuste da 3,0213 ns sin ruido y la ondulación aparece con periodo de 25,0 MHz.
- 🎯 **Por qué importa:** Un error de banda aparece en las líneas espectrales como una falsa estructura y limita el rango dinámico del continuo. La decisión central: ¿qué parte del error de banda es un retardo, qué parte una ondulación, y con qué precisión se miden?
- 🔗 **Se estudia junto con:** respuesta de banda, ondulación, ancho de banda, desviación típica de las frecuencias.

📘 **Dónde se aprende** (1 clase): [B51-C04 · Respuesta de banda y errores dependientes de la frecuencia](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md).

### Retardo S−P

- El retardo S−P es la diferencia entre las llegadas de la onda S y la onda P.

💡 **Cómo se explica en la clase [B63-C01](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md):**
- Las ondas P y S salen juntas del foco y llegan con un retardo `Δt = d/vs − d/vp`.
- Con `vp = 5,0` y `vs = 2,9 km/s`, el factor vale `6,905 km/s`: un retardo de `30 s` da `207,14 km`.
- ⚠️ **Error frecuente:** Usar el retardo como distancia. La distancia es retardo por un factor de velocidades.
- 🎯 **Por qué importa:** Un rover no puede volver a medir lo que midió mal. Antes de elegir qué observar hay que saber qué puede resolver cada instrumento.
- 🔗 **Se estudia junto con:** GSD, focal, paso de píxel, relación señal/ruido.

📘 **Dónde se aprende** (1 clase): [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md).

### Retardo total τ

- Retardo total `τ`: reacción más comunicación.

💡 **Cómo se explica en la clase [B101-C10](../programa/clases/B101/B101-C10-simulacion-de-una-tarea-tripulada-con-manipulador/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. El retardo total son la reacción y la comunicación.
- 🎯 **Por qué importa:** Cuanto más tarda en llegar la imagen y la orden, más difícil es corregir. La decisión central: ¿con qué retardo total y qué ganancia el operador puede capturar con éxito y cuándo conviene pasar a «mover y esperar»?
- 🔗 **Se estudia junto con:** Ganancia K, Mover y esperar, Inversión de orden, Captura exitosa.

📘 **Dónde se aprende** (1 clase): [B101-C10 · Simulación de una tarea tripulada con manipulador](../programa/clases/B101/B101-C10-simulacion-de-una-tarea-tripulada-con-manipulador/CLASE.md).

### Retardo troposférico seco (hidrostático)

- El retardo troposférico seco (hidrostático) es casi proporcional a la presión de superficie.

💡 **Contexto en la clase [B57-C29](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md):**
- **Idea central (modelo mental):** La atmósfera estira la cinta métrica del radar. La ionosfera la estira distinto en cada frecuencia, y esa diferencia permite saber cuánto se estiró.
- 🎯 **Por qué importa:** Un error de decímetros en la distancia equivale a decímetros de error en la altura del mar, mayor que las señales que se buscan. La decisión central: ¿qué corrección aplicar a cada retardo y cuánto ruido agrega?
- 🔗 **Se estudia junto con:** retardo ionosférico, combinación libre de ionosfera, barometría inversa, TECU.

📘 **Dónde se aprende** (1 clase): [B57-C29 · Correcciones atmosféricas en altimetría](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md).

### Retardo unidireccional

- El retardo unidireccional es `d/c`.

💡 **Cómo se explica en la clase [B75-C19](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md):**
- En el modelo, la distancia Tierra–Marte va de `78,36` a `377,55×10⁶ km`; el retardo unidireccional de `4,36` a `20,99 min` (medio `14,08 min`) y el de ida y vuelta de `8,71` a `41,98 min`.
- Predice antes de ejecutar: ¿Cuál es el retardo unidireccional medio?
- ⚠️ **Error frecuente:** Confundir retardo unidireccional con RTLT. Se corrige con la sección 6.
- 🎯 **Por qué importa:** No se puede dirigir desde la Tierra lo que sucede en minutos. La decisión central: ¿qué eventos duran menos que el tiempo mínimo de reacción desde tierra y por tanto deben ser autónomos?
- 🔗 **Se estudia junto con:** RTLT, tiempo de reacción, autonomía, conjunción solar.

📘 **Dónde se aprende** (1 clase): [B75-C19 · Restricciones de navegación autónoma](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md).

### Retención

- La retención («hold and review») es mantener la muestra contenida mientras se revisa.
- La retención `r` es la probabilidad de que un elemento sobreviva correcto una generación.
- La retención `A` (< 1 olvida) y la sensibilidad al error `B` fijan la tasa `λ = A − B` y el estado estacionario `x* = B p/(1 − A + B)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B105-C25](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md):**
- *Descripción textual:* el error entre la perturbación y el estado actualiza el estado con una retención y una sensibilidad; el estado converge a un estado estacionario y deja un postefecto al retirar la perturbación.
- Un modelo con `A = 0,95` (retención) y `B = 0,20` (sensibilidad al error) enfrenta una perturbación de 30° durante 40 ensayos y luego 40 ensayos de lavado.
- 🎯 **Por qué importa:** Quien se adapta a un entorno nuevo comete errores al volver al anterior. Entender el ritmo de adaptación y el postefecto permite diseñar el entrenamiento y anticipar las torpezas.
- 🔗 **Se estudia junto con:** estado, error, sensibilidad al error, postefecto.

📘 **Dónde se aprende** (4 clases): [B63-C06 · Evaluación de riesgos biológicos de muestras: marcos de decisión](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md); [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md); [B106-C11 · Almacenamiento de alimentos](../programa/clases/B106/B106-C11-almacenamiento-de-alimentos/CLASE.md); [B133-C02 · Narrativas orales y transmisión del saber del cielo](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md).

### Retenedor de orden cero

- Un retenedor de orden cero (ZOH) mantiene la entrada constante entre dos muestras.

💡 **Cómo se explica en la clase [B16-C02](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md):**
- Discretizar un modelo continuo con retenedor de orden cero y justificar el paso `T`.
- 🎯 **Por qué importa:** El computador de a bordo de un satélite no maneja ecuaciones sueltas: maneja vectores y matrices, y una sola rutina sirve para cualquier eje, rueda o sensor que se le añada.
- 🔗 **Se estudia junto con:** representación en espacio de estados, exponencial matricial, matriz de transición, transformación de semejanza.

📘 **Dónde se aprende** (1 clase): [B16-C02 · Representaciones en espacio de estados](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md).

### Reticulado

- El reticulado es el conjunto de combinaciones de niveles de generalización.

💡 **Cómo se explica en la clase [B124-C13](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md):**
- El ejemplo conductor es un conjunto sintético de 300 participantes: sin generalizar, `300` registros (`100,0%`) son únicos y por tanto reidentificables; el mejor nodo del reticulado logra `k = 5` con `11` supresiones.
- Explorar un reticulado de generalizaciones de forma exhaustiva.
- 🎯 **Por qué importa:** Abrir datos sin proteger a las personas es un daño, y proteger sin medir es una promesa vacía. La decisión central: ¿cuánto generalizar los datos para que ninguna persona sea identificable y cuánta información se pierde?
- 🔗 **Se estudia junto con:** k-anonimato, generalización, supresión, discernibilidad (DM).

📘 **Dónde se aprende** (1 clase): [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md).

### Retirada

- La retirada del consentimiento detiene el uso posterior de los datos de esa persona.

💡 **Cómo se explica en la clase [B129-C05](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md):**
- Llevar un registro de consentimiento con estado por defecto «sin consentimiento» y retirada efectiva.
- 🎯 **Por qué importa:** Cuando un conjunto de datos se publica o se comparte, los datos de las personas pueden permitir reconocerlas aunque se quite el nombre. La decisión central: ¿qué recoger, con qué precisión publicarlo y cómo respetar que alguien retire su consentimiento?
- 🔗 **Se estudia junto con:** minimización, generalización, k-anonimato, registro único.

📘 **Dónde se aprende** (1 clase): [B129-C05 · Consentimiento y privacidad de participantes](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md).

### Retorno

- El retorno ocurre cuando la nave y la Tierra coinciden de nuevo.

💡 **Cómo se explica en la clase [B75-C25](../programa/clases/B75/B75-C25-resonancias-para-sobrevuelos/CLASE.md):**
- La ficha de la ESA indica que Juice usa asistencias de la Luna–Tierra, Venus y la Tierra [S2]; si usa retornos resonantes no se consultó.
- La evidencia es tu tabla de resonancias de retorno del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Para volver a un planeta hay que llegar a la misma posición un número entero de años después. La decisión central: ¿qué resonancias `k:m` son alcanzables con un `v∞` dado y cuánto `v∞` hace falta para las demás?
- 🔗 **Se estudia junto con:** resonancia k:m, viabilidad, v∞ mínimo.

📘 **Dónde se aprende** (1 clase): [B75-C25 · Resonancias para sobrevuelos](../programa/clases/B75/B75-C25-resonancias-para-sobrevuelos/CLASE.md).

### Retorno científico

- El retorno científico es el tiempo en modo nominal.

💡 **Contexto en la clase [B86-C21](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md):**
- 🎯 **Por qué importa:** Cuando la energía escasea, apagar la carga útil a tiempo mantiene viva la nave. Un umbral único hace oscilar al sistema entre modos; la histéresis lo evita.
- 🔗 **Se estudia junto con:** modo de operación, modo seguro, política de modos, histéresis.

📘 **Dónde se aprende** (1 clase): [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md).

### Retorno radial

- El retorno radial corrige la tensión de prueba elástica al límite de fluencia actual.

💡 **Cómo se explica en la clase [B84-C25](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md):**
- El script [nolineal.py](nolineal.py) integra un ciclo elastoplástico con retorno radial y resuelve un contacto con Newton (comprueba `σ` monotónica frente a analítica (< 1e-9) y `u` de contacto exacta).
- 🎯 **Por qué importa:** Un modelo lineal da tensiones de 400 MPa en un material que cedió a 275: el resultado correcto es una deformación permanente y una tensión residual que solo el análisis no lineal muestra. La decisión central: ¿qué deformación permanente y tensión residual deja una carga que excede el límite elástico, y cuándo actúa un contacto?
- 🔗 **Se estudia junto con:** endurecimiento isótropo, carga monotónica, contacto.

📘 **Dónde se aprende** (1 clase): [B84-C25 · Comportamiento estructural no lineal: plasticidad y contacto](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md).

### Retorno restringido

- La Categoría V agrupa las misiones de retorno a la Tierra. «Retorno restringido» es la subcategoría de mayor preocupación.

💡 **Cómo se explica en la clase [B63-C04](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md):**
- Según S1, para el retorno restringido: (1) se prohíbe de forma absoluta el impacto destructivo al regresar;
- Enumerar las exigencias de contención y las revisiones de un retorno restringido.
- 🎯 **Por qué importa:** Traer material de otro cuerpo exige proteger a la Tierra y a la muestra. La decisión central: ¿cuántas barreras independientes hacen falta, y qué pasa si dejan de ser independientes?
- 🔗 **Se estudia junto con:** Categoría V, Romper la cadena de contacto, barrera, probabilidad de fallo.

📘 **Dónde se aprende** (1 clase): [B63-C04 · Misiones de retorno de muestras: salvaguardas históricas y regulatorias](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md).

### Retrabajo

- Pasada hacia atrás: calcula fin (`LF`) e inicio (`LS`) más tardíos. Retrabajo: corregir un producto no conforme.

💡 **Cómo se explica en la clase [B90-C01](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md):**
- Si la prueba funcional H falla, hay que añadir retrabajo (3 d) y repetirla (2 d).
- Límite: una receta no tiene fallas que obliguen a repetir un paso; el plan sí debe prever retrabajo.
- ⚠️ **Error frecuente:** Planificar sin retrabajo. Reserva contingencia (8.4)
- 🎯 **Por qué importa:** La integración es la fase donde los errores de diseño se vuelven visibles y caros. Un plan que no distingue las tareas críticas de las que tienen holgura gasta esfuerzo en el lugar equivocado.
- 🔗 **Se estudia junto con:** Ensamblaje, Integración, Prueba, Ruta crítica.

📘 **Dónde se aprende** (1 clase): [B90-C01 · Plan de ensamblaje e integración](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md).

### Retransmisión

- Completitud: fracción recibida. Retransmisión: reenvío de faltantes.

💡 **Cómo se explica en la clase [B96-C16](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md):**
- Descripción larga: cada retransmisión multiplica los faltantes por `p = 0,03`; en tres pasadas el conjunto queda completo.
- Simular la retransmisión de faltantes en pasadas sucesivas.
- 🎯 **Por qué importa:** Un conjunto de datos con huecos no declarados da conclusiones erróneas, y una retransmisión sin plan agota los contactos. La decisión central: ¿qué falta, cuántas pasadas hacen falta para completarlo y qué producto se entrega en cada nivel?
- 🔗 **Se estudia junto con:** Paquete, Hueco, Completitud, Nivel de procesamiento.

📘 **Dónde se aprende** (1 clase): [B96-C16 · Gestión de datos científicos](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md).

### Retraso

- El retraso es el tiempo hasta la primera alarma tras el cambio.

💡 **Cómo se explica en la clase [B105-C09](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md):**
- Subir `h` baja las falsas alarmas y alarga el retraso.
- A --> M["falsas alarmas,<br/>deteccion, retraso"]
- 🎯 **Por qué importa:** Un umbral bajo detecta pronto pero alarma de más; uno alto alarma poco pero tarda. Con una tripulación pequeña, las falsas alarmas se acumulan.
- 🔗 **Se estudia junto con:** línea base personal, puntuación z, CUSUM, tasa de falsas alarmas.

📘 **Dónde se aprende** (1 clase): [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md).

### Retraso de detección

- El retraso de detección es el tiempo entre el inicio del evento (dos anchos antes del centro) y la alarma; una alarma anterior al inicio es una falsa alarma.

💡 **Cómo se explica en la clase [B97-C22](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md):**
- Calcular la probabilidad y el retraso de detección de un evento pequeño y uno grande.
- 🎯 **Por qué importa:** Un detector sensible produce falsas alarmas que consumen enlace y energía; uno estricto pierde eventos. La clave es medir ambos efectos con una referencia (ARL₀) y comparar métodos con el mismo costo de falsas alarmas.
- 🔗 **Se estudia junto con:** CUSUM, margen, umbral de decisión, ARL₀.

📘 **Dónde se aprende** (1 clase): [B97-C22 · Detección autónoma de eventos científicos](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md).

### Retraso geométrico

- El retraso geométrico es `Δt = n·Δr/c` para un desplazamiento `Δr` respecto de la referencia.

💡 **Contexto en la clase [B74-C27](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md):**
- 🎯 **Por qué importa:** La idea atrae porque sería autónoma, sin estaciones; la pregunta honesta es cuánta precisión da con una cantidad realista de fotones. La decisión central: ¿cuánto tiempo de observación y cuántos púlsares hacen falta para una cierta precisión, y qué parte de la técnica sigue sin demostrarse en esta clase?
- 🔗 **Se estudia junto con:** tiempo de llegada, perfil plegado, cota de Cramér–Rao, dilución.

📘 **Dónde se aprende** (1 clase): [B74-C27 · Navegación por púlsares de rayos X como técnica de investigación](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md).

### Retraso por masa

- El retraso por masa `Δt = (d/c)(1 − β)/β`.
- El retraso por masa afecta a partículas con masa en reposo.

💡 **Cómo se explica en la clase [B27-C18](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md):**
- *Descripción textual:* de la energía y la energía media se obtiene el número de neutrinos y su fluencia; con la sección eficaz y los protones del detector, los sucesos; el retraso por masa se calcula con una forma algebraica estable.
- Calcular el retraso por masa de forma estable.
- 🎯 **Por qué importa:** Los neutrinos de una supernova galáctica serían una señal de cientos de sucesos en unos segundos, mensajera del interior de la estrella. La decisión central: ¿cuántos neutrinos llegan, qué retraso produce su masa y cómo se calcula sin perder precisión?
- 🔗 **Se estudia junto con:** neutrino, fluencia, sección eficaz, protones libres.

📘 **Dónde se aprende** (2 clases): [B27-C18 · Neutrinos de supernova](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md); [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md).

### Retraso S−P

- El retraso S−P es `t_S − t_P`.

💡 **Cómo se explica en la clase [B53-C02](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md):**
- Analogía: el trueno y el relámpago: la luz llega antes que el sonido, y el retraso dice a qué distancia cayó el rayo.
- T --> D["distancia = retraso / (1/vs - 1/vp)"]
- 🎯 **Por qué importa:** Un solo sismómetro no da la posición completa de un evento. La decisión central: ¿cuánto vale la distancia al evento y con qué incertidumbre, si solo se leen los tiempos de llegada P y S?
- 🔗 **Se estudia junto con:** parámetro de rayo, distancia epicentral, fase.

📘 **Dónde se aprende** (1 clase): [B53-C02 · Sismología planetaria](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md).

### Retroalimentación estelar

- La retroalimentación estelar es el efecto de las estrellas sobre el gas que las rodea: calentamiento, empuje y enriquecimiento.

💡 **Cómo se explica en la clase [B25-C16](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md):**
- Ejercicio 12 · integrador. Elabora la *ficha de presupuesto de retroalimentación*: elige una galaxia (sintética) con `σ` y gas; calcula supernovas por `M☉`, `E_b`, supernovas necesarias, masa estelar, fracción del gas y la sensibilidad a `ε`; indica qué parámetros son convencionales.
- El script [retroalimentacion.py](retroalimentacion.py) calcula las supernovas por masa, la energía de ligadura, la masa estelar necesaria y la burbuja.
- 🎯 **Por qué importa:** Sin retroalimentación, el gas de una galaxia se convertiría en estrellas mucho más deprisa de lo observado. Las supernovas, los vientos y la radiación de las estrellas masivas calientan y expulsan gas, y lo enriquecen con metales (C17).
- 🔗 **Se estudia junto con:** supernova, umbral, eficiencia de acoplamiento, energía de ligadura del gas.

📘 **Dónde se aprende** (1 clase): [B25-C16 · Retroalimentación estelar](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md).

### Retroceso

- El retroceso propaga con `−t`.

💡 **Contexto en la clase [B71-C20](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md):**
- 🎯 **Por qué importa:** Un propagador que «parece funcionar» puede tener un error de tiempo que ningún invariante detecta. La decisión central: ¿qué pruebas, con qué tolerancias y contra qué referencia independiente demuestran que el propagador es correcto?
- 🔗 **Se estudia junto con:** propagador, prueba de aceptación, integrador independiente, mutación.

📘 **Dónde se aprende** (1 clase): [B71-C20 · Propagador kepleriano verificable](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md).

### Retroceso nuclear

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B36-C10](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md):**
- **Idea central (modelo mental):** Es como lanzar bolas de billar contra una pared de bolas más pesadas: la energía que reciben depende de la velocidad, de las masas y del ángulo.
- 🎯 **Por qué importa:** Un límite de sección eficaz depende de la cinemática, de la exposición y de las cuentas. La decisión central: ¿qué sección eficaz excluye una exposición sin sucesos?
- 🔗 **Se estudia junto con:** masa reducida, cinemática, espectro, modulación anual.

📘 **Dónde se aprende** (1 clase): [B36-C10 · Búsqueda directa de materia oscura en laboratorio](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md).

### Retrodicción

- La retrodicción propaga el estado hacia atrás: `x_m = F⁻ˡ x_k`.

💡 **Cómo se explica en la clase [B74-C24](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md):**
- *Descripción textual:* una medida con sello anterior al estado actual puede descartarse, usarse como actual, tratarse con retrodicción aproximada o reprocesarse; cada tratamiento se evalúa con rms, NEES y validez de la covarianza.
- Paso 3 · Retrodicción. `x_m = F⁻⁵ x_k`; con la matriz de movimiento uniforme, la posición retrocede `5 v`.
- 🎯 **Por qué importa:** Una medida tardía contiene información valiosa pero tratarla mal puede dañar más que descartarla. La decisión central: ¿qué tratamiento de una medida tardía mejora el estimado sin romper la consistencia, y a qué coste?
- 🔗 **Se estudia junto con:** OOSM, retardo, reprocesado, covarianza cruzada.

📘 **Dónde se aprende** (1 clase): [B74-C24 · Medidas retardadas y fuera de secuencia en filtros de estimación](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md).

### Retrodispersión Rayleigh

- La capa de sodio y la retrodispersión Rayleigh.

💡 **Cómo se explica en la clase [B42-C17](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md):**
- La retrodispersión Rayleigh a 10 km tiene densidad relativa `0,2865` (altura de escala 8 km, ilustrativa) y el ultravioleta (355 nm) dispersa `5,04` veces más que 532 nm (`λ⁻⁴`).
- 🎯 **Por qué importa:** Sin estrella guía no hay corrección en casi todo el cielo. La decisión central: ¿a qué altitud conviene crear la estrella y qué error de cono y qué elongación trae?
- 🔗 **Se estudia junto con:** estrella guía láser, efecto cono, altitud, sodio.

📘 **Dónde se aprende** (1 clase): [B42-C17 · Estrellas guía artificiales](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md).

### Retrógrada

- Una órbita es directa si `i < 90°` y retrógrada si `i > 90°`.
- Prógrada es `i < 90°`; retrógrada, `i > 90°`.
- Una transferencia es prógrada si `n` apunta hacia el eje de referencia `+z` (`h_z > 0`) y retrógrada si apunta hacia `−z`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- La componente `z` es `cos i`: positiva si `i < 90°` (directa) y negativa si `i > 90°` (retrógrada).
- E -->|"< 0"| G["Órbita retrógrada (i > 90°)"]
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?
- 🔗 **Se estudia junto con:** producto vectorial, regla de la mano derecha, anticonmutativo, normal a un plano.

📘 **Dónde se aprende** (6 clases): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md); [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md); [B52-C11 · Formación de satélites naturales](../programa/clases/B52/B52-C11-formacion-de-satelites-naturales/CLASE.md); [B71-C11 · Inclinación y nodo ascendente](../programa/clases/B71/B71-C11-inclinacion-y-nodo-ascendente/CLASE.md); [B76-C03 · Órbitas alrededor de la Luna](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md); [B82-C02 · Lambert de arco largo](../programa/clases/B82/B82-C02-lambert-de-arco-largo/CLASE.md).

### Reunión

- La difusión (*broadcast*) copia un dato del proceso raíz a todos; el reparto (*scatter*) divide una colección de la raíz entre los procesos; la reunión (*gather*) hace lo contrario; la reducción (*reduce*) combina valores de todos con una operación (suma, máximo…) y la deja en la raíz, y `allreduce` la deja en todos.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Elegir entre difusión, reparto, reunión y reducción para un patrón dado.
- El script [mensajes_mpi.py](mensajes_mpi.py) ejecuta, con cualquier número de procesos: un anillo con `sendrecv`, una difusión de parámetros, el cálculo de π con `reduce` y `allreduce`, el reparto y reunión de 4 órbitas por proceso, y un eco de 16 MB con objetos y con *buffers*.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.
- 🔗 **Se estudia junto con:** comunicador, tamaño, rango, SPMD.

📘 **Dónde se aprende** (1 clase): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md).

### Reunión de revisión

- La reunión de revisión es una conversación programada.

💡 **Contexto en la clase [B104-C16](../programa/clases/B104/B104-C16-manejo-de-conflictos/CLASE.md):**
- 🎯 **Por qué importa:** Un conflicto abierto cuesta tiempo, errores y confianza; prevenirlo cuesta pequeñas conversaciones continuas. La decisión central: ¿cuánto reduce una intervención temprana la probabilidad de que la tensión llegue al conflicto abierto, frente a no hacer nada o reunirse una vez por semana?
- 🔗 **Se estudia junto con:** tensión, persistencia, conflicto abierto, mediación temprana.

📘 **Dónde se aprende** (1 clase): [B104-C16 · Manejo de conflictos](../programa/clases/B104/B104-C16-manejo-de-conflictos/CLASE.md).

### Reutilizable

- La lista de comprobación es un conjunto de reglas que se aplican al paquete. Reutilizable significa que otra persona puede usarlo legal y técnicamente.

💡 **Contexto en la clase [B14-C19](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md):**
- **Idea central (modelo mental):** Un paquete bien hecho responde, sin que su autor esté presente, cinco preguntas: qué es (README, descripción), qué puedo hacer con ello (licencia), cómo lo cito (CITATION.cff), qué significan los datos (unidades, procedencia) y si es el archivo correcto (huellas).
- 🎯 **Por qué importa:** Subes tu código a un repositorio y tus datos a una carpeta compartida. Un año después, alguien quiere usarlos y no sabe si puede, cómo citarte, qué significan las columnas ni si el archivo es el que tú usaste.
- 🔗 **Se estudia junto con:** identificador persistente, licencia, identificador SPDX, metadatos.

📘 **Dónde se aprende** (1 clase): [B14-C19 · Publicación de código y datos](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md).

### Reutilización

- La reutilización reduce el precio efectivo.

💡 **Cómo se explica en la clase [B124-C23](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md):**
- Con 550 000 kg de masa inicial, la carga útil es `13346` kg; a 60 Mum el costo es `4496` um/kg, y si la reutilización ahorra el 30 % del precio, `3147` um/kg.
- El descenso desde órbita baja (`Δv = 6 000 m/s`, `Isp` 340 s, `e = 0,12`) deja una fracción de `0,05157`, así que cada kilogramo en superficie exige `1/0,05157` kg en órbita: el costo sube a `87176` um/kg (`19,4` veces); con reutilización, `61024`.
- ⚠️ **Error frecuente:** Creer que la reutilización resuelve todo el costo. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** El costo por kilogramo a superficie no se puede leer en una lista de precios: depende de una cadena de fracciones de masa que se multiplican. La decisión central: ¿cuánto cuesta llevar un kilogramo a la superficie, de qué depende ese costo y qué lo hace más sensible?
- 🔗 **Se estudia junto con:** ecuación del cohete, razón de masas, coeficiente estructural, fracción de carga útil.

📘 **Dónde se aprende** (1 clase): [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Reverberante

- El campo directo viene de la fuente; el reverberante, de los rebotes.

💡 **Cómo se explica en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- El nivel total es `59,2 dBA` a `1 m`, `56,6` a `2 m`, `55,9` a `3 m` y `55,5` a `5 m`; el campo reverberante da `55,2`.
- *Descripción textual:* las fuentes se suman en energía; el recinto aporta absorción y constante; el nivel en un punto mezcla campo directo y reverberante y se compara con el límite y el objetivo para decidir qué fuente bajar.
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?
- 🔗 **Se estudia junto con:** nivel de potencia sonora, nivel de presión, campo directo, absorción.

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Reversibilidad

- La reversibilidad es que el trazado de vuelta recupere el rayo de entrada.
- La reversibilidad de un método es `Φ_{−h} ∘ Φ_h = id`.
- La reversibilidad es poder volver al inicio con el mapa inverso.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B50-C06](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md):**
- Comprobar la reversibilidad del trazado.
- Ejercicio 6. ¿Cuál es la desviación de la reversibilidad?
- 🎯 **Por qué importa:** Los programas de diseño óptico son cajas con muchas opciones: lo que hace reproducible un diseño es el archivo, sus unidades, su versión y sus pruebas. La decisión central: ¿cómo se demuestra que un modelo sigue siendo el mismo y sigue dando lo mismo?
- 🔗 **Se estudia junto con:** modelo reproducible, huella, forma canónica, regresión.

📘 **Dónde se aprende** (5 clases): [B50-C06 · Software de diseño óptico: modelos reproducibles y verificación](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md); [B73-C06 · Variedades invariantes](../programa/clases/B73/B73-C06-variedades-invariantes/CLASE.md); [B73-C09 · Integración de largo plazo](../programa/clases/B73/B73-C09-integracion-de-largo-plazo/CLASE.md); [B73-C13 · Caos determinista](../programa/clases/B73/B73-C13-caos-determinista/CLASE.md); [B75-C30 · Validación de maniobras por reintegración](../programa/clases/B75/B75-C30-validacion-de-maniobras-por-reintegracion/CLASE.md).

### Reversibilidad temporal

- Una reversibilidad temporal significa que avanzar y luego invertir la velocidad y avanzar vuelve al inicio.

💡 **Contexto en la clase [B11-C11](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md):**
- **Idea central (modelo mental):** Un método simpléctico no recorre la órbita verdadera sino otra, muy cercana, que conserva *exactamente* su propia energía. El error de energía respecto de la órbita verdadera oscila, pero no crece; lo que sí crece es el desfase con que se recorre.
- 🎯 **Por qué importa:** Para el sistema solar, anillos planetarios o constelaciones se necesitan integraciones de millones de vueltas. Un método que añade o quita un poco de energía en cada vuelta termina destruyendo la órbita.
- 🔗 **Se estudia junto con:** hamiltoniano, simpléctico, leapfrog, hamiltoniano modificado.

📘 **Dónde se aprende** (1 clase): [B11-C11 · Métodos simplécticos](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md).

### Reversible

- Es reversible y conserva el volumen, pero no exactamente la energía: su error de energía `ΔH` escala como `ε²`.

💡 **Cómo se explica en la clase [B19-C03](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md):**
- Es *reversible*: si al final inviertes el signo del momento y repites `L` pasos, vuelves al punto inicial (el laboratorio lo comprueba a 10⁻¹⁰).
- 🎯 **Por qué importa:** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.
- 🔗 **Se estudia junto con:** posición, momento, energía potencial, cinética.

📘 **Dónde se aprende** (1 clase): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md).

### Reversible en el tiempo

- Un método es reversible en el tiempo si, tras avanzar `N` pasos, invertir la velocidad y avanzar otros `N` pasos devuelve el estado inicial.

💡 **Cómo se explica en la clase [B23-C02](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md):**
- RK4 (orden 4) da errores de energía mucho menores a corto plazo (`2,7 × 10⁻⁹` frente a `5,0 × 10⁻⁶` con `h = 1 d` en 10 años) pero no es reversible ni conserva `L` exactamente, y su error de energía crece con el tiempo.
- 🔗 **Se estudia junto con:** magnitud conservada, energía específica, momento angular específico, simetría.

📘 **Dónde se aprende** (1 clase): [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md).

### Reversión

- Una reversión (*rollback*) restaura la anterior.

💡 **Cómo se explica en la clase [B88-C13](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md):**
- (4) imagen buena que no arranca → 3 arranques fallidos y reversión a A.
- Ejercicio 5 · autónomo. ¿Cuántos arranques fallidos provocan la reversión del caso 4?
- 🎯 **Por qué importa:** Una actualización fallida en órbita no se arregla con un cable. La decisión central: ¿qué comprobaciones aceptan solo la imagen correcta y qué mecanismo vuelve a una versión conocida si la nueva no arranca?
- 🔗 **Se estudia junto con:** hash, HMAC-SHA256, ranuras A/B, cuenta de arranques.

📘 **Dónde se aprende** (1 clase): [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md).

### Revisión por pares

- La revisión por pares (o arbitraje) es la evaluación de un manuscrito por especialistas independientes antes de su publicación.

💡 **Cómo se explica en la clase [B20-C03](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md):**
- La lección: la revisión por pares tiene reglas de conducta para las tres partes.
- Describir las funciones de autor, árbitro y editor en la revisión por pares y sus deberes de confidencialidad y de declaración de conflictos.
- 🎯 **Por qué importa:** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.
- 🔗 **Se estudia junto con:** autor, árbitro, editor, informe de árbitro.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Revisita

- La revisita es el intervalo entre observaciones de un punto, que puede ser menor que el ciclo si los barridos se solapan o hay varios satélites.

💡 **Cómo se explica en la clase [B57-C23](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md):**
- La revisita real es menor que el ciclo si los barridos de trazas vecinas se solapan en latitudes altas o si hay varios satélites.
- Por constelación: menor revisita con más satélites.
- ⚠️ **Error frecuente:** Confundir ciclo con revisita. Pueden diferir (8.4).
- 🎯 **Por qué importa:** Si la órbita no repite sus trazas o el barrido no cubre el espacio entre ellas, quedan huecos. La decisión central: ¿qué altitud e inclinación dan un ciclo de repetición que cubre todo con el barrido disponible?
- 🔗 **Se estudia junto con:** órbita heliosíncrona, periodo nodal, traza repetida, espaciado entre trazas.

📘 **Dónde se aprende** (1 clase): [B57-C23 · Diseño de órbita y revisita para observación terrestre](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md).

### Rezago normativo

- El rezago normativo es el tiempo entre una tecnología y su regulación.

💡 **Contexto en la clase [B119-C12](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md):**
- 🎯 **Por qué importa:** Para leer el derecho vigente conviene saber qué contexto lo produjo; ninguna clase anterior da la cronología comparada entre la tecnología y los instrumentos jurídicos. La decisión central: ¿cuánto tardó el derecho en seguir a la tecnología y por qué importa distinguir fechas verificadas de fechas recordadas?
- 🔗 **Se estudia junto con:** hito, día juliano, Competencia estratégica, fuente primaria.

📘 **Dónde se aprende** (1 clase): [B119-C12 · Historia de competencia estratégica espacial](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md).

### Rica

- Una mezcla rica tiene exceso de combustible; una pobre, de oxidante.

💡 **Cómo se explica en la clase [B78-C05](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md):**
- Con disociación, la temperatura se achata cerca del estequiométrico y la menor masa molar de una mezcla rica pasa a ganar; por eso los motores de H₂/O₂ operan ricos.
- La disociación, que desplaza el óptimo hacia mezclas ricas.
- 🎯 **Por qué importa:** Un motor puede quemar mezclas con exceso de combustible o de oxidante. La decisión central: ¿qué `O/F` maximiza el escape en un modelo sin disociación y por qué los motores reales operan en otro punto?
- 🔗 **Se estudia junto con:** bipropelente, relación O/F, estequiométrica, pobre.

📘 **Dónde se aprende** (1 clase): [B78-C05 · Propulsión bipropelente conceptual](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md).

### Rica en combustible

- La razón O/F de 3,5 es rica en combustible frente a la estequiométrica (3,99).

💡 **Contexto en la clase [B59-C09](../programa/clases/B59/B59-C09-fabricacion-de-combustibles-conceptuales/CLASE.md):**
- **Idea central (modelo mental):** Como una receta que devuelve la mitad de un ingrediente al cocinar: hay que reponer la otra mitad. Límite: la conversión real del reactor no es total.
- 🎯 **Por qué importa:** Un combustible fabricado en destino depende de qué parte del hidrógeno se recicla. La decisión central: ¿cuánto hidrógeno hay que importar para fabricar 1 000 kg de propelente O₂/CH₄?
- 🔗 **Se estudia junto con:** reacción de Sabatier, lazo del agua, razón O/F, hidrógeno importado.

📘 **Dónde se aprende** (1 clase): [B59-C09 · Fabricación de combustibles conceptuales](../programa/clases/B59/B59-C09-fabricacion-de-combustibles-conceptuales/CLASE.md).

### Richardson

- El orden observado es `p = ln((f₂ − f₁)/(f₃ − f₂))/ln r` con tres mallas. Richardson: `f_ext = f₃ + (f₃ − f₂)/(r^p − 1)`.

💡 **Cómo se explica en la clase [B84-C26](../programa/clases/B84/B84-C26-generacion-de-mallas-y-convergencia-en-elementos-finitos/CLASE.md):**
- `p = 0,935`, Richardson `25,0367 MPa` (dif `1,5 × 10⁻³`) y GCI `3,14 %`.
- Extrapolar con Richardson al límite de malla infinitamente fina.
- 🎯 **Por qué importa:** Una malla más gruesa puede errar 30 % en tensión sin que el resultado «parezca» mal; la convergencia dice cuánto y cuánto refinar. La decisión central: ¿cuántos elementos hacen falta para que la magnitud de interés cambie menos que una tolerancia dada?
- 🔗 **Se estudia junto con:** orden observado, GCI, malla fina.

📘 **Dónde se aprende** (1 clase): [B84-C26 · Generación de mallas y convergencia en elementos finitos](../programa/clases/B84/B84-C26-generacion-de-mallas-y-convergencia-en-elementos-finitos/CLASE.md).

### Richardson–Lucy

- El método de Richardson–Lucy (RL) es iterativo, conserva la positividad y es el que implementan bibliotecas como scikit-image (S2).
- La inversión es hallar `ψ` a partir de los conteos. Richardson–Lucy es una iteración multiplicativa de máxima verosimilitud de Poisson.
- El filtro de Wiener. Richardson-Lucy: iteración que conserva flujo y positividad.

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- I -->|"Richardson–Lucy<br/>y parar a tiempo"| F["Estimación x̂:<br/>más nítida"]
- *Descripción textual:* el objeto se convoluciona con la PSF y se le añade ruido; invertir con el filtro inverso amplifica el ruido hasta inutilizar la imagen, mientras que el método iterativo de Richardson–Lucy, detenido a tiempo, produce una estimación más nítida.
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.
- 🔗 **Se estudia junto con:** PSF, gaussiana, FWHM, desenfoque.

📘 **Dónde se aprende** (3 clases): [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B38-C04 · Historia de formación estelar a partir de poblaciones resueltas](../programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/CLASE.md); [B42-C19 · Reconstrucción de imágenes](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md).

### RID

- Un RID (*review item discrepancy*) es un hallazgo que debe cerrarse. «Lista» significa que pasan todos los criterios críticos; los no críticos se registran.

💡 **Cómo se explica en la clase [B83-C13](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md):**
- Estimar el tiempo para cerrar las acciones de revisión (RID).
- Acciones (RID): 10 en total, 3 criticas, capacidad 2 por semana -> 5 semanas para cerrar todas, 2 para las criticas
- ⚠️ **Error frecuente:** Cerrar RID sin evidencia. Registra la evidencia del cierre
- 🎯 **Por qué importa:** Una revisión aprobada sin criterios es un trámite; una revisión con criterios medibles es una decisión. La decisión central: ¿el proyecto cumple los criterios de entrada de la SRR y de la PDR y qué falta para llegar?
- 🔗 **Se estudia junto con:** SRR, PDR, criterio, crítico.

📘 **Dónde se aprende** (1 clase): [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md).

### Riesgo

- Un riesgo es un evento posible con consecuencia; se acompaña de una mitigación.
- Un riesgo es un escenario con verosimilitud (L, 1–5) y consecuencia (C, 1–5).
- Un peligro es una fuente de daño; el riesgo combina severidad y verosimilitud.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C20](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md):**
- Riesgos: sol y calor de día, frío y oscuridad de noche, caídas en terreno, vehículos, equipo volcado, fatiga al regresar, pérdida de adaptación a la oscuridad por luces; cada uno con su mitigación.
- 🎯 **Por qué importa:** Una salida sin plan termina en una noche perdida o en un accidente. La pregunta motivadora: ¿cómo preparo una salida de observación para que sea segura, útil, accesible y reproducible?
- 🔗 **Se estudia junto con:** requisito, verificable, criterio de comprobación, método de comprobación.

📘 **Dónde se aprende** (7 clases): [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B83-C16 · Gestión de riesgos técnicos](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md); [B83-C21 · Identificación de peligros en sistemas de lanzamiento (HAZID)](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md); [B110-C02 · Protocolos operativos de aislamiento de un tripulante enfermo o contaminado](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md); [B114-C06 · Matriz de riesgo ambiental de un hábitat](../programa/clases/B114/B114-C06-matriz-de-riesgo-ambiental-de-un-habitat/CLASE.md); [B120-C05 · Riesgos de incumplimiento regulatorio](../programa/clases/B120/B120-C05-riesgos-de-incumplimiento-regulatorio/CLASE.md) y 1 más.

### Riesgo colectivo

- El riesgo colectivo `Ec` es el número esperado de bajas.

💡 **Cómo se explica en la clase [B121-C01](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md):**
- Un riesgo individual bajo no garantiza un riesgo colectivo bajo: `Ec` suma sobre mucha gente.
- ⚠️ **Error frecuente:** Creer que cumplir el riesgo individual implica cumplir el colectivo. Se corrige con 8.2 y 8.3.
- 🎯 **Por qué importa:** La autorización de un lanzamiento no es un trámite abstracto: incluye criterios numéricos de riesgo. La decisión central: ¿una trayectoria cumple el criterio de riesgo colectivo e individual que exige la licencia y con qué margen?
- 🔗 **Se estudia junto con:** licencia, riesgo individual, zona de impacto, área de baja.

📘 **Dónde se aprende** (1 clase): [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md).

### Riesgo de exceso

- El riesgo de exceso es la probabilidad adicional atribuible a la exposición.

💡 **Cómo se explica en la clase [B112-C04](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md):**
- El riesgo de exceso nominal es `r·E` con `r = 0,05 Sv⁻¹`: 0,050 % a 10 mSv, 0,500 % a 100, 1,250 % a 250, 3,000 % a 600 y 5,000 % a 1000 mSv.
- E["dosis efectiva E [Sv]"] --> R["riesgo de exceso<br/>r · E"]
- 🎯 **Por qué importa:** Ninguna clase cubre riesgo de cáncer y efectos tardíos. Los límites de carrera de una misión se expresan como riesgo, no como umbral, y sin entender cómo se estima y cuán incierta es esa estimación, un límite en mSv parece más preciso de lo que es.
- 🔗 **Se estudia junto con:** modelo lineal sin umbral, DDREF, detrimento, efecto estocástico.

📘 **Dónde se aprende** (1 clase): [B112-C04 · Efectos crónicos y carcinogénesis por radiación](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md).

### Riesgo de exceso de muerte inducida por exposición

- El riesgo de exceso de muerte inducida por exposición (REID) es la probabilidad de que una persona muera de cáncer a causa de la exposición, en función de la dosis efectiva, la edad y el sexo (NASA THREE).

💡 **Contexto en la clase [B112-C06](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md):**
- 🎯 **Por qué importa:** Falta la clase de estimación de riesgo por misión. Es la que usa un planificador: suma dosis de cada tramo, la convierte en riesgo y decide si cabe dentro de un límite.
- 🔗 **Se estudia junto con:** límite de carrera, nivel del 95 % de confianza, límite administrativo, ALARA.

📘 **Dónde se aprende** (1 clase): [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Riesgo del consumidor

- El riesgo del consumidor es aceptar una unidad mala; el del productor, rechazar una buena.

💡 **Cómo se explica en la clase [B50-C14](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md):**
- G --> R["riesgos consumidor y productor"]
- Con límite de 0,05 ondas e incertidumbre de medida 0,005, una banda de guarda de 1,645 baja el riesgo del consumidor de `3,51 %` a `0,22 %`.
- 🎯 **Por qué importa:** Una especificación solo sirve si se puede verificar con una medida que tiene incertidumbre. La decisión central: ¿cuánto margen se deja para que una medida incierta no acepte una unidad mala?
- 🔗 **Se estudia junto con:** razón de Strehl, aproximación de Maréchal, criterio de Rayleigh, banda de guarda.

📘 **Dónde se aprende** (1 clase): [B50-C14 · Criterios de aceptación: Strehl, error de frente de onda y especificaciones](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md).

### Riesgo individual

- El riesgo individual `P_c` es la probabilidad de que una persona resulte víctima.
- El riesgo individual `Pc` es la probabilidad de baja de una persona.

💡 **Cómo se explica en la clase [B77-C19](../programa/clases/B77/B77-C19-seguridad-de-rango-a-nivel-conceptual/CLASE.md):**
- *Descripción textual:* la probabilidad de falla, la distribución de impactos, la población y el área de víctima se combinan en las víctimas esperadas y en el riesgo individual, que se comparan con los umbrales.
- Descripción larga: el riesgo colectivo sube de forma marcada al acercar una zona poblada al eje de la trayectoria; el riesgo individual en un punto es mucho más pequeño que el colectivo.
- ⚠️ **Error frecuente:** Confundir riesgo colectivo con individual. Se corrige con 8.3.
- 🎯 **Por qué importa:** Mover el sitio de impacto un par de decenas de kilómetros cambia el riesgo en un factor de varios. La decisión central: ¿cómo se calculan las víctimas esperadas y cuánto depende de dónde cae lo que cae?
- 🔗 **Se estudia junto con:** víctimas esperadas, zona de impacto, área de víctima, cuadratura.

📘 **Dónde se aprende** (2 clases): [B77-C19 · Seguridad de rango a nivel conceptual](../programa/clases/B77/B77-C19-seguridad-de-rango-a-nivel-conceptual/CLASE.md); [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md).

### Riesgo inherente

- El riesgo inherente es `P × I` sin controles; el residual, con controles.

💡 **Cómo se explica en la clase [B122-C03](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md):**
- *Descripción textual:* activo y amenaza definen un riesgo inherente; los controles reducen la probabilidad y dejan el riesgo residual, que se clasifica.
- Calcular el riesgo inherente y el residual.
- 🎯 **Por qué importa:** B83-C16 trata riesgos técnicos y B119-C14 amenazas sin modelo. La decisión central: ¿qué riesgo residual domina y qué activo carece de controles?
- 🔗 **Se estudia junto con:** activo, amenaza, control, residual.

📘 **Dónde se aprende** (1 clase): [B122-C03 · Modelo defensivo de riesgos de infraestructura espacial](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md).

### Riesgo residual

- El riesgo residual es el `R` tras aplicar las medidas.
- El riesgo residual es el que queda.
- Filosofía de modelos: conjunto de modelos que se construye y prueba. Riesgo residual: probabilidad de que un defecto llegue a órbita.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- La mejor filosofía es C porque las correcciones tempranas son baratas y el riesgo residual es 5 veces menor que el de A.
- Descripción larga: el costo esperado de A crece con la pérdida más rápido que el de C porque el riesgo residual de A es mayor.
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?
- 🔗 **Se estudia junto con:** Prototipo, Modelo de ingeniería (EM), Modelo de calificación (QM), Protovuelo.

📘 **Dónde se aprende** (3 clases): [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md); [B114-C06 · Matriz de riesgo ambiental de un hábitat](../programa/clases/B114/B114-C06-matriz-de-riesgo-ambiental-de-un-habitat/CLASE.md); [B119-C14 · Amenazas cibernéticas a satélites](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md).

### Riesgo retenido

- El riesgo retenido se mide por la desviación y los cuantiles del costo.

💡 **Cómo se explica en la clase [B127-C08](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md):**
- El tercero pasaría a dominar el riesgo retenido en A–C y su prima subiría unas diez veces;
- 🎯 **Por qué importa:** Integrar los seguros de una misión en un caso permite practicar la decisión; no existía tal caso. La decisión central: ¿cuánto se paga de más por reducir el riesgo y qué riesgo se está dispuesto a retener?
- 🔗 **Se estudia junto con:** estrategia, costo del operador, pérdida retenida, autoseguro.

📘 **Dónde se aprende** (1 clase): [B127-C08 · Simulación de cobertura de seguros para una misión](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md).

### Rigidez

- La fuerza restauradora apunta al equilibrio y es proporcional al desplazamiento: `F = −k x` (ley de Hooke), con `k` la rigidez (N/m).
- La rigidez de una EOS es cuánto crece `P` con `ρ`.
- La rigidez es el par por grado.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- No se consultó un dato de vibración de ninguna misión, así que el caso de esta clase es sintético: un mástil de enseñanza de 50 kg de masa efectiva y rigidez de 2,0 × 10⁵ N/m.
- Ejercicio 12 · integrador. Elabora una *ficha de oscilador* (sección 20): para un sistema sintético (masa y rigidez a tu elección), calcula `ω₀`, `f`, `T`, energía, amplificación en resonancia con dos `ζ`, y compáralo con una integración numérica.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?
- 🔗 **Se estudia junto con:** movimiento armónico simple (MAS), amplitud, frecuencia angular, fase.

📘 **Dónde se aprende** (5 clases): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B27-C04 · Ecuación de estado nuclear](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md); [B43-C25 · Rodamientos y apoyos de precisión en telescopios](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md); [B107-C02 · Movilidad articular, flexibilidad y postura](../programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/CLASE.md); [B107-C07 · Rehabilitación vestibular y del equilibrio posterior al vuelo](../programa/clases/B107/B107-C07-rehabilitacion-vestibular-y-del-equilibrio-posterior-al-vuelo/CLASE.md).

### Rigidez a flexión

- La rigidez a flexión `E I`.

💡 **Contexto en la clase [B43-C10](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md):**
- **Idea central (modelo mental):** Como dos niños en un balancín que bajan lo mismo aunque pesen distinto porque el brazo del liviano es más flexible: ambos bajan juntos y el eje se mantiene paralelo.
- 🎯 **Por qué importa:** Lo que decolima no es la flexión sino la flexión diferencial entre primario y secundario. La decisión central: ¿qué rigideces hacen que los dos extremos se muevan lo mismo, de modo que el eje óptico solo se desplace en paralelo?
- 🔗 **Se estudia junto con:** cercha Serrurier, flecha de voladizo, descentrado diferencial, tubo delgado.

📘 **Dónde se aprende** (1 clase): [B43-C10 · Estructura de tubo óptico](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md).

### Rigidez de elemento

- La rigidez de elemento es `k = EA/l [[1,−1],[−1,1]]`.

💡 **Cómo se explica en la clase [B84-C12](../programa/clases/B84/B84-C12-analisis-de-elementos-finitos/CLASE.md):**
- *Descripción textual:* se calcula la rigidez de cada elemento, se ensambla `K`, se restringe el empotramiento, se resuelve y se verifican reacción, energía y error.
- Analogía: una barra afilada es una cadena de resortes de rigidez decreciente: cada elemento aporta un resorte con el área en su punto medio.
- 🎯 **Por qué importa:** Un modelo que da un resultado no es un modelo correcto: la verificación contra una solución conocida es lo que lo convierte en una herramienta. La decisión central: ¿cómo demuestras que un modelo de elementos finitos resuelve bien las ecuaciones que dice resolver?
- 🔗 **Se estudia junto con:** ensamblaje, condiciones de contorno, prueba del parche, orden de convergencia.

📘 **Dónde se aprende** (1 clase): [B84-C12 · Análisis de elementos finitos](../programa/clases/B84/B84-C12-analisis-de-elementos-finitos/CLASE.md).

### Rigidez del sándwich

- La rigidez del sándwich es `D = E t_f d²/(2(1 − ν²))` con `d = h + t_f`.

💡 **Cómo se explica en la clase [B84-C20](../programa/clases/B84/B84-C20-diseno-estructural-de-plataforma-satelital/CLASE.md):**
- Calcular la rigidez y la frecuencia de un panel sándwich.
- 🎯 **Por qué importa:** Un diseño estructural se justifica con requisitos, un modelo, márgenes y un balance de masa; sin cualquiera de ellos no se puede revisar. La decisión central: ¿cumple esta estructura preliminar los requisitos de frecuencia y de resistencia con la masa disponible?
- 🔗 **Se estudia junto con:** frecuencia, margen, balance de masa.

📘 **Dónde se aprende** (1 clase): [B84-C20 · Diseño estructural de plataforma satelital](../programa/clases/B84/B84-C20-diseno-estructural-de-plataforma-satelital/CLASE.md).

### Rigidez deseada K_d

- Impedancia: relación entre el movimiento y la fuerza. Rigidez deseada `K_d`: N/m.

💡 **Cómo se explica en la clase [B101-C07](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md):**
- Menor rigidez deseada, menor fuerza: con `K_d = 200` N/m la fuerza es 13 veces menor que con 5 000 N/m para la misma posición ordenada.
- 🎯 **Por qué importa:** Si un brazo muy rígido empuja una pieza que está 5 mm más lejos de lo que cree, aplica una fuerza grande. La decisión central: ¿qué rigidez y qué amortiguamiento le doy al extremo para que el contacto sea suave y la fuerza predecible?
- 🔗 **Se estudia junto con:** Impedancia, Amortiguamiento B_d, Inercia deseada M_d, Fuerza externa F_ext.

📘 **Dónde se aprende** (1 clase): [B101-C07 · Control de fuerza e impedancia en manipulación](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md).

### Rigidez específica

- La rigidez específica es `E/ρ`; la resistencia específica, `σ₀,₂/ρ`; la resiliencia, `σ₀,₂²/(2E)`.
- La rigidez específica `E/ρ` compara materiales de igual masa.

💡 **Cómo se explica en la clase [B43-C03](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md):**
- Calcular la rigidez específica `E/ρ` y la figura de mérito térmica `k/α`.
- 🎯 **Por qué importa:** Un buen material no es el más duro ni el más estable: es el que deja el menor error de forma para una masa y un presupuesto. La decisión central: ¿qué material y qué espesor mantienen la flexión y la deriva térmica por debajo de la tolerancia?
- 🔗 **Se estudia junto con:** módulo de Young, figura de mérito térmica, placa de Kirchhoff, ecuación biarmónica.

📘 **Dónde se aprende** (2 clases): [B43-C03 · Materiales para espejos](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md); [B84-C02 · Propiedades de aleaciones](../programa/clases/B84/B84-C02-propiedades-de-aleaciones/CLASE.md).

### Rigidez flexural

- La rigidez flexural es `D = E T³/(12(1 − ν²))`.

💡 **Cómo se explica en la clase [B53-C12](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md):**
- *Descripción textual:* El espesor elástico fija la rigidez y el parámetro flexural, que con la carga dan la deflexión y su abombamiento; aparte, los escarpes dan la contracción.
- 🎯 **Por qué importa:** La flexión revela el espesor elástico de la litosfera y la contracción, el balance térmico global. La decisión central: ¿qué espesor elástico y qué acortamiento explican la deformación observada?
- 🔗 **Se estudia junto con:** parámetro flexural, abombamiento periférico, contracción global.

📘 **Dónde se aprende** (1 clase): [B53-C12 · Tectónica planetaria](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md).

### Rigidez magnética

- La rigidez magnética `Bρ = p/e`.

💡 **Contexto en la clase [B31-C15](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md):**
- **Idea central (modelo mental):** Como una honda: cuanto más rápido gira la piedra, más tensión necesita el cordón (el campo), y si la piedra es muy ligera pierde energía radiando.
- 🎯 **Por qué importa:** El diseño de un acelerador depende de cuánta energía se pierde por radiación y de cuánta energía útil se obtiene. La decisión central: ¿qué campo y qué radio se necesitan y por qué los electrones pierden tanto?
- 🔗 **Se estudia junto con:** pérdida por vuelta, ciclotrón, colisionador, blanco fijo.

📘 **Dónde se aprende** (1 clase): [B31-C15 · Física de aceleradores](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md).

### Rígido

- Un problema es rígido cuando contiene escalas de tiempo muy distintas y la más rápida obliga a un paso pequeño sin interés por sí misma.
- Un sistema es rígido si tiene componentes que evolucionan en escalas de tiempo muy distintas.

💡 **Cómo se explica en la clase [B11-C09](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md):**
- Implícitos (Euler implícito, y sus relativos de orden alto): resuelven una ecuación por paso, estables en problemas rígidos.
- Un control adaptativo (C08) *reduce* `h` si el error crece, y por tanto también detecta la inestabilidad, pero a un costo enorme en problemas rígidos: el paso baja a `2/k` aunque la solución sea lisa.
- ⚠️ **Error frecuente:** Usar un método explícito para un problema rígido y culpar al código. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.
- 🔗 **Se estudia junto con:** ecuación de prueba, factor de amplificación, estable, región de estabilidad.

📘 **Dónde se aprende** (2 clases): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B60-C03 · Integración numérica de redes químicas rígidas](../programa/clases/B60/B60-C03-integracion-numerica-de-redes-quimicas-rigidas/CLASE.md).

### Ripples

- Las ripples y dunas son formas que el transporte genera en el lecho.

💡 **Cómo se explica en la clase [B66-C03](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md):**
- python programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/eolico.py
- 🎯 **Por qué importa:** Marte tiene dunas y una atmósfera cien veces menos densa que la terrestre; Venus, una atmósfera enorme y casi sin viento.
- 🔗 **Se estudia junto con:** velocidad umbral de fricción, parámetro de Shields, saltación, longitud de saltación.

📘 **Dónde se aprende** (1 clase): [B66-C03 · Procesos eólicos: dunas, ripples y erosión planetaria](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md).

### Riqueza

- La riqueza cuenta taxones.

💡 **Cómo se explica en la clase [B105-C11](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md):**
- Con pocas lecturas, la riqueza y Shannon se subestiman.
- Equivalente textual: más profundidad, más riqueza observada; más mezcla, menor disimilitud; más dominancia, menos diversidad.
- 🎯 **Por qué importa:** Un índice de diversidad depende de la comunidad y de cuántas lecturas se obtuvieron. La decisión central: ¿qué profundidad de muestreo hace fiable un índice y cómo se cuantifica el parecido entre la piel de la tripulación y las superficies?
- 🔗 **Se estudia junto con:** índice de Shannon, Simpson, disimilitud de Bray–Curtis, profundidad.

📘 **Dónde se aprende** (1 clase): [B105-C11 · Microbioma en ambientes cerrados](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md).

### Ritchey-Chrétien

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C17](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md):**
- Con `m = 5` y foco `100 mm` tras el primario: `d = 316,667 mm`, `R₂ = 208,333 mm` y `k₂ = −2,25`; el clásico da coma `10,955 µm` a 10', el Dall-Kirkham `135,089 µm` y el Ritchey-Chrétien `0` (`k₁ = −1,02130`, `k₂ = −2,44971`).
- Resolver Ritchey-Chrétien por Newton 2D.
- 🎯 **Por qué importa:** Dos espejos permiten un tubo corto y focal larga, y distintos diseños eligen qué aberración corregir. La decisión central: ¿qué diseño corrige la coma y a qué costo?
- 🔗 **Se estudia junto con:** Cassegrain clásico, Dall-Kirkham, aumento del secundario, focal efectiva.

📘 **Dónde se aprende** (1 clase): [B41-C17 · Telescopios Cassegrain y derivados](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md).

### Ritchey-Chrétien (RC)

- El Ritchey-Chrétien (RC) usa dos hiperboloides.

💡 **Cómo se explica en la clase [B43-C02](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md):**
- Obtener las conicidades de un Ritchey-Chrétien resolviendo dos condiciones.
- 🎯 **Por qué importa:** La geometría decide qué aberraciones quedan y cuánto mide el tubo. La decisión central: ¿qué conicidades de primario y secundario anulan la aberración esférica y el coma, y qué se paga en largo y obstrucción?
- 🔗 **Se estudia junto con:** cónica, Cassegrain clásico, aumento, coma.

📘 **Dónde se aprende** (1 clase): [B43-C02 · Selección de geometría instrumental](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md).

### Ritmo circadiano

- El ritmo circadiano `C` es una oscilación de 24 h.
- Ritmo circadiano: oscilación de unas 24 h de procesos fisiológicos.

💡 **Cómo se explica en la clase [B104-C17](../programa/clases/B104/B104-C17-gestion-de-fatiga/CLASE.md):**
- *Descripción textual:* la presión de sueño sube despierto y baja dormido; el ritmo circadiano la compensa o la agrava; la alerta es su diferencia.
- 🎯 **Por qué importa:** NASA reconoce la pérdida de sueño, la desincronización circadiana y la sobrecarga como un riesgo del vuelo. La decisión conceptual: ¿cuánta alerta se pierde en el trabajo diurno al acortar el sueño unas horas, y por qué el modelo no sustituye a la medición?
- 🔗 **Se estudia junto con:** presión de sueño, alerta, deuda de sueño, desincronización circadiana.

📘 **Dónde se aprende** (2 clases): [B104-C17 · Gestión de fatiga](../programa/clases/B104/B104-C17-gestion-de-fatiga/CLASE.md); [B106-C13 · Iluminación y ciclos circadianos](../programa/clases/B106/B106-C13-iluminacion-y-ciclos-circadianos/CLASE.md).

### Ritmo libre

- El ritmo libre es el periodo del ciclo sueño–vigilia sin señales externas.

💡 **Cómo se explica en la clase [B113-C04](../programa/clases/B113/B113-C04-autonomia-personal-y-gestion-del-tiempo-en-aislamiento/CLASE.md):**
- Un ritmo libre de `25,0 h` (valor ilustrativo, cercano al del tripulante b de Basner et al.) desplaza el sueño `1 h` por día respecto de un reloj de 24 h: `10 h` tras `10` días y una vuelta completa en `24` días.
- Relacionar el ritmo libre cercano a 25 h con la pérdida de sincronía.
- 🎯 **Por qué importa:** Falta la clase sobre autonomía y rutinas. La decisión central: ¿qué holgura reservar en una jornada y qué reloj seguir cuando el día local no dura 24 horas?
- 🔗 **Se estudia junto con:** día solar, deriva, holgura, autonomía.

📘 **Dónde se aprende** (1 clase): [B113-C04 · Autonomía personal y gestión del tiempo en aislamiento](../programa/clases/B113/B113-C04-autonomia-personal-y-gestion-del-tiempo-en-aislamiento/CLASE.md).

### Ritmo máximo

- La dirección de máximo crecimiento es `∇f/|∇f|` y el ritmo máximo es `|∇f|`.

💡 **Cómo se explica en la clase [B09-C17](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md):**
- B --> C["Dirección ∇f/|∇f|:<br/>máximo crecimiento, ritmo |∇f|"]
- Ejercicio 3 · casi autónomo. Halla la dirección, el ritmo máximo y una dirección de cambio nulo para la misma función.
- 🎯 **Por qué importa:** La gravedad no es un número: es un vector que apunta a un lado y tiene una magnitud. En un campo con dos cuerpos, como Tierra–Luna, esa dirección cambia de punto a punto.
- 🔗 **Se estudia junto con:** gradiente, derivada direccional, vector unitario, curva de nivel.

📘 **Dónde se aprende** (1 clase): [B09-C17 · Gradiente y derivada direccional](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md).

### Rizado

- El rizado es la variación pico a pico en un periodo.

💡 **Cómo se explica en la clase [B86-C08](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md):**
- *Descripción textual:* el interruptor conecta la entrada a la bobina con ciclo `D`; el diodo conduce en el resto del periodo; la bobina y el condensador filtran y alimentan la carga; de ahí salen el rizado y las pérdidas.
- Paso 4 · Rizado. `ΔI = 23 × 0,965 µs/22 µH = 1,0085 A`.
- ⚠️ **Error frecuente:** Confundir rizado con valor medio. Se corrige con 8.2 y 8.3.
- 🎯 **Por qué importa:** Un convertidor que reduce la tensión con un interruptor y una bobina puede ser mucho más eficiente que un regulador lineal, pero introduce rizado, ruido y pérdidas de conmutación que hay que dimensionar. La decisión central: ¿qué ciclo de trabajo, bobina y condensador dan `5 V` desde `28 V` con rizado y eficiencia aceptables?
- 🔗 **Se estudia junto con:** ciclo de trabajo, CCM, DCM, inductancia crítica.

📘 **Dónde se aprende** (1 clase): [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### RK4

- La temperatura límite es `T_a − Q/G`. RK4 es un integrador de cuarto orden.
- El baricentro es el centro de masas del par. RK4 es el método de Runge–Kutta de cuarto orden.
- Euler explícito es de orden 1. RK4 es de orden 4.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B44-C08](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md):**
- Con paso de `0,5 s`, el error máximo de Euler es `0,01380 K` y el de RK4 `4,8 × 10⁻¹³ K`.
- Ejercicio 7. Error de Euler frente a RK4.
- 🎯 **Por qué importa:** La cámara no está fría al encenderla. La decisión central: ¿cuánto hay que esperar antes de calibrar y qué temperatura final se alcanza?
- 🔗 **Se estudia junto con:** capacidad térmica, conductancia, potencia de enfriamiento, constante de tiempo.

📘 **Dónde se aprende** (6 clases): [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md); [B71-C03 · Ecuación de movimiento de dos cuerpos](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md); [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md); [B85-C26 · Análisis térmico transitorio y casos extremos](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md); [B97-C23 · Diseño de simulador de misión robótica](../programa/clases/B97/B97-C23-diseno-de-simulador-de-mision-robotica/CLASE.md); [B101-C06 · Simulación de un brazo robótico espacial](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md).

### RMF

- La RMF es la matriz de redistribución de energía a canal.

💡 **Cómo se explica en la clase [B27-C22](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md):**
- RMF gaussiana con `σ = 0,1E`, normalizada de modo que cada columna suma 1.
- Con respuesta identidad, el plegado coincide con el cálculo directo a `10⁻⁹`; las columnas de la RMF suman 1;
- 🎯 **Por qué importa:** Ajustar un espectro «de fotones» directamente a las cuentas da resultados engañosos; hay que plegar el modelo con la respuesta y usar la estadística correcta para conteos pequeños. La decisión central: ¿qué parámetros recupera cada estadística y con qué sesgo cuando las cuentas son pocas?
- 🔗 **Se estudia junto con:** ARF, plegado, estadística de Cash, χ² con varianza igual a las cuentas.

📘 **Dónde se aprende** (1 clase): [B27-C22 · Análisis espectral de rayos X y gamma: ajuste con respuesta instrumental](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md).

### RML

- WVR, el vapor de agua recuperado; RML `= TML − WVR`;

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- A["pesadas mi, mf, mh, dc"] --> B["TML, WVR, RML, CVCM"]
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?
- 🔗 **Se estudia junto con:** TML, WVR, CVCM, bakeout.

📘 **Dónde se aprende** (1 clase): [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md).

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

📘 **Dónde se aprende** (6 clases): [B43-C22 · Interferometría de superficie y mapas de error de forma](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md); [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md); [B47-C10 · Estabilidad de apuntamiento](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md); [B85-C14 · Degradación ultravioleta](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md); [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md); [B97-C26 · Monitoreo de condición de maquinaria extraterrestre](../programa/clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md).

### RMS 3D

- El RMS 3D es `√(Σσ²)`.

💡 **Cómo se explica en la clase [B74-C19](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md):**
- Con `σ = (3; 1,2; 2) m`: RMS 3D `3,8000 m` (muestral `3,8012 m`), percentil 95 de la norma 3D `6,493 m`, SEP (50 %) `3,190 m`, CEP (50 %, horizontal) `2,425 m`.
- Con `N = 50`, el RMS 3D es `3,816 ± 0,245 m`, el percentil 95 `6,316 ± 0,634 m` y el CEP `2,457 ± 0,264 m`.
- 🎯 **Por qué importa:** Dos informes pueden decir «3 m» y referirse a cosas distintas (RMS, 50 %, 95 %). La decisión central: ¿qué métrica comunica el riesgo que importa, con qué probabilidad y con qué incertidumbre muestral?
- 🔗 **Se estudia junto con:** CEP, SEP, 2DRMS, percentil.

📘 **Dónde se aprende** (1 clase): [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md).

### RMS del frente de onda

- El RMS del frente de onda se calcula quitando pistón, inclinación y enfoque.

💡 **Cómo se explica en la clase [B50-C10](../programa/clases/B50/B50-C10-errores-de-centrado-y-su-efecto-en-el-desempeno/CLASE.md):**
- Medir el RMS del frente de onda con el secundario desplazado.
- El script [descentramiento.py](descentramiento.py) desplaza el secundario y mide el RMS del frente de onda (comprueba linealidad a 2 %, simetría a 1e-9 e invariancia a 1e-6 ondas).
- 🎯 **Por qué importa:** El descentramiento es una de las tolerancias de montaje que más pesan en un telescopio. La decisión central: ¿cuánto puede desplazarse el secundario antes de degradar la imagen?
- 🔗 **Se estudia junto con:** descentramiento, coma, respuesta lineal, campo equivalente.

📘 **Dónde se aprende** (1 clase): [B50-C10 · Errores de centrado y su efecto en el desempeño](../programa/clases/B50/B50-C10-errores-de-centrado-y-su-efecto-en-el-desempeno/CLASE.md).

### RMS sin enfoque

- El RMS sin enfoque quita el pistón, la inclinación y el desenfoque.

💡 **Cómo se explica en la clase [B50-C03](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md):**
- Con enfoque libre (`a = 6,138 × 10⁻¹¹`, `b = 4,483 × 10⁻⁹`) queda en `0,00311` ondas.
- Un espejo esférico `R = 2000 mm`, `f/5`, tiene un RMS sin enfoque de `0,427` ondas en el eje.
- 🎯 **Por qué importa:** Combinar espejos y elementos refractivos permite campos amplios con superficies fáciles de fabricar. La decisión central: ¿dónde va el diafragma y qué corrige el elemento refractivo?
- 🔗 **Se estudia junto con:** centro de curvatura, diafragma, placa de Schmidt, menisco.

📘 **Dónde se aprende** (1 clase): [B50-C03 · Sistemas catadióptricos: Schmidt y Maksutov](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md).

### RMSE

- El RMSE es la raíz del error cuadrático medio.
- MAE es el error absoluto medio, RMSE el cuadrático medio, AbsRel la media de `|ẑ − z|/z` y delta1 la fracción de puntos con `máx(z/ẑ, ẑ/z) < 1,25`.

💡 **Cómo se explica en la clase [B33-C01](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md):**
- Sesgo `−5,22 km/s`, RMSE `39,39 km/s`, correlación `0,8059`, `MSSS` frente a la climatología `0,5907` y frente a la persistencia de 24 h `0,3341`.
- El RMSE por remuestreo tiene mediana `39,48` e intervalo del 5–95 % `[37,73; 41,67] km/s`; el valor observado cae dentro.
- 🎯 **Por qué importa:** Un modelo sin validación no sirve para pronosticar. La decisión central: ¿cuán bien reproduce el modelo la serie y con qué desfase?
- 🔗 **Se estudia junto con:** sesgo, correlación, destreza, persistencia.

📘 **Dónde se aprende** (4 clases): [B33-C01 · Validación de modelos MHD con eventos solares documentados](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md); [B33-C12 · Pronóstico de llegada y severidad de CME](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md); [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md).

### RMSF

- La RMSF es su respuesta a una fuente puntual.

💡 **Cómo se explica en la clase [B46-C13](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md):**
- Con una fuente sintética de `RM = 60 rad/m²` y `p = 0,3`, la síntesis da el pico en `59,5 rad/m²` (amplitud `0,297`) y el ajuste `59,54 rad/m²`; la RMSF mide `61,3 rad/m²`.
- Ejercicio 6. ¿Cuánto vale la RMSF para `Δλ² = 0,113 m²`?
- 🎯 **Por qué importa:** El ángulo de polarización gira con `λ²`, y hay que medirlo en varias frecuencias para saber cuánto. La decisión central: ¿cómo se obtiene la medida de rotación sin ambigüedad de `nπ`?
- 🔗 **Se estudia junto con:** parámetros de Stokes, polarización lineal, rotación de Faraday, síntesis de RM.

📘 **Dónde se aprende** (1 clase): [B46-C13 · Polarimetría de radio](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md).

### Robustez

- La robustez es la fracción de pesos aleatorios con que un sitio sigue siendo el primero.

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *ficha de selección multicriterio*: tabla de datos, normalización, puntaje, frente de Pareto, robustez y umbral de cambio.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?
- 🔗 **Se estudia junto con:** criterio, normalización min-max, puntaje ponderado, domina.

📘 **Dónde se aprende** (1 clase): [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md).

### Roca

- Una roca es una mezcla de minerales.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Una roca solamente de olivino y piroxeno tiene Mg/Si entre 1 y 2.
- Imagina un grano de roca (un silicato) en una nube fría, cubierto por capas de hielo: primero agua, luego CO₂ y otras moléculas, según las temperaturas de condensación.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).
- 🔗 **Se estudia junto con:** hielo, mineral, olivino, forsterita.

📘 **Dónde se aprende** (1 clase): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md).

### Rodadura lenta

- La rodadura lenta: `φ̈` despreciable.

💡 **Cómo se explica en la clase [B40-C01](../programa/clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md):**
- La condición `ε = 1` se alcanza en `φ = 1,0062 M_pl` y `t = 18,630/m`, con `N = 64,563` frente a `63,500` de la rodadura lenta (diferencia `+1,063`).
- La rodadura lenta pierde exactitud al final, como muestra la fila `N = 60`.
- ⚠️ **Error frecuente:** Usar rodadura lenta hasta el final. Se corrige con 8.1.
- 🎯 **Por qué importa:** Sin un mecanismo para las condiciones iniciales, el modelo FLRW deja sin explicar la planitud y la homogeneidad. La decisión central: ¿cuántos e-pliegues produce un campo que rueda lentamente y cuándo termina la inflación?
- 🔗 **Se estudia junto con:** campo escalar, potencial, parámetro de Hubble, e-pliegue.

📘 **Dónde se aprende** (1 clase): [B40-C01 · Inflación cósmica: motivación y dinámica básica](../programa/clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md).

### Rodilla

- La rodilla es el cambio de pendiente del espectro.
- La rodilla es el punto del frente más alejado, hacia el óptimo, de la recta que une los extremos (objetivos normalizados).

💡 **Cómo se explica en la clase [B28-C04](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md):**
- Con `γ₁ = 2,7`, `γ₂ = 3,1` y rodilla en `10¹⁵ eV`, el flujo integral analítico y el numérico (Simpson en `ln E`) coinciden a `10⁻⁶`: `1,173684 × 10⁻¹⁹` por encima de `10¹¹ eV` y `4,672165 × 10⁻²³` por encima de `10¹³ eV` (unidades arbitrarias).
- Por encima de la rodilla, `flujo(>10¹⁶)/flujo(>10¹⁵) = 0,0079 = 10^{−(γ₂−1)}`.
- 🎯 **Por qué importa:** El origen de los rayos cósmicos de mayor energía sigue abierto; el criterio de Hillas descarta fuentes y la anisotropía apunta a regiones. La decisión central: ¿qué fuentes pueden alcanzar una energía dada y qué anisotropía se puede detectar con un número dado de eventos?
- 🔗 **Se estudia junto con:** criterio de Hillas, flujo integral, dipolo, estimador.

📘 **Dónde se aprende** (2 clases): [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md); [B81-C11 · Optimización multicriterio y frentes de Pareto](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md).

### ROE

- La ROE (razón de onda estacionaria) `(1 + |Γ|)/(1 − |Γ|)`.

💡 **Cómo se explica en la clase [B49-C02](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md):**
- El patrón de ondas estacionarias de esa carga da ROE muestreada `1,64872`, igual a la analítica (`|Γ| = 0,24492`).
- Una ROE de 1,46 pierde solo 0,155 dB; una de 5 pierde 2,55 dB.
- ⚠️ **Error frecuente:** Confundir ROE y pérdida de retorno. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una antena desadaptada devuelve potencia y empeora la sensibilidad. La decisión central: ¿cuánta potencia se refleja y cómo se adapta con un tramo de línea?
- 🔗 **Se estudia junto con:** coeficiente de reflexión, pérdida de retorno, carta de Smith, longitud eléctrica.

📘 **Dónde se aprende** (1 clase): [B49-C02 · Adaptación de impedancias y líneas de transmisión en antenas](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md).

### Rol

- Un rol es una responsabilidad asignada a una persona.
- Criticidad: consecuencia de un comando. Rol: nivel de autoridad.

💡 **Cómo se explica en la clase [B96-C07](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md):**
- Se evalúan `3 × 4 × 5 × 2 = 120` combinaciones (rol, criticidad, cinco listas de aprobaciones, armado sí/no) con la política y con una referencia independiente basada en tablas de mínimos.
- (3) Monotonía: si un rol menor está autorizado, el siguiente también lo está.
- 🎯 **Por qué importa:** Un comando enviado por la persona equivocada o sin segunda revisión puede perder la misión. La decisión central: ¿qué rol, qué aprobaciones y qué armado exige cada nivel de criticidad y cómo se prueba que la política no tiene huecos?
- 🔗 **Se estudia junto con:** Criticidad, Aprobación, Armado, Referencia independiente.

📘 **Dónde se aprende** (2 clases): [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B96-C07 · Telecomandos y autorizaciones](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md).

### Roll-off

- El roll-off `α` es el exceso de banda del filtro de coseno alzado; el ancho ocupado es `Rs(1+α)`.

💡 **Cómo se explica en la clase [B89-C02](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md):**
- *Descripción textual:* la tasa de bits, el código y la modulación dan la tasa de símbolos; con el roll-off, el ancho ocupado; este decide cuántos canales caben y la capacidad de Shannon; el Doppler se suma por separado.
- ILUSTRATIVO: Rb = 2 Mbit/s, codigo 1/2, QPSK, roll-off 0.35, guarda 0.3 MHz, banda 50 MHz
- ⚠️ **Error frecuente:** Olvidar el roll-off al calcular el ancho. Se corrige con 8.1.
- 🎯 **Por qué importa:** Sin una idea cuantitativa del ancho de banda no se puede decidir cuántos enlaces caben en una banda ni cuánta tasa de datos es posible. La regulación (C19) trabaja con exactamente estas magnitudes.
- 🔗 **Se estudia junto con:** tasa de símbolos, ancho ocupado, eficiencia espectral, banda de guarda.

📘 **Dónde se aprende** (1 clase): [B89-C02 · Frecuencia y espectro espacial](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md).

### Romper la cadena de contacto

- La Categoría V agrupa las misiones de retorno a la Tierra. «Retorno restringido» es la subcategoría de mayor preocupación. Romper la cadena de contacto es evitar que hardware que tocó el cuerpo regrese sin contención.

💡 **Cómo se explica en la clase [B63-C04](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md):**
- Explicar qué significa «romper la cadena de contacto».
- Ejercicio 9 · transferencia. Transferencia. ¿Qué quiere decir «romper la cadena de contacto»?
- 🎯 **Por qué importa:** Traer material de otro cuerpo exige proteger a la Tierra y a la muestra. La decisión central: ¿cuántas barreras independientes hacen falta, y qué pasa si dejan de ser independientes?
- 🔗 **Se estudia junto con:** Categoría V, Retorno restringido, barrera, probabilidad de fallo.

📘 **Dónde se aprende** (1 clase): [B63-C04 · Misiones de retorno de muestras: salvaguardas históricas y regulatorias](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md).

### Ronda con precio

- La ronda con precio vende acciones preferentes a un precio por acción.

💡 **Cómo se explica en la clase [B126-C01](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md):**
- Si el precio de la ronda es `P = V/(C+s)` y el SAFE paga `(1 − d)P`, entonces `s = INV/((1 − d)P)`.
- *Descripción textual:* el SAFE se convierte por dos caminos (tope o descuento) y recibe el que da más acciones; con eso se obtiene el precio de la ronda y la tabla de capitalización, y se verifica con una iteración de punto fijo.
- 🎯 **Por qué importa:** El catálogo trata el financiamiento privado en general (B124-C07, «Financiamiento privado», en la [guía del bloque B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md)), no la mecánica de las etapas iniciales.
- 🔗 **Se estudia junto con:** SAFE, tope de valoración, descuento, tabla de capitalización.

📘 **Dónde se aprende** (1 clase): [B126-C01 · Capital semilla y financiamiento inicial](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md).

### Root

- Un resumen (*digest*) identifica una imagen por su contenido. Root es el usuario con todos los privilegios.

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- ⚠️ **Error frecuente:** Ejecutar como root. Se corrige con la regla `USER` de la sección 8.2.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?
- 🔗 **Se estudia junto con:** imagen, contenedor, Dockerfile, capa.

📘 **Dónde se aprende** (1 clase): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md).

### Rotación

- Una rotación es una transformación lineal que conserva longitudes y ángulos y no invierte la orientación: su matriz `R` cumple `RᵀR = I` y `det R = +1` (una matriz ortogonal, con el determinante de C04).
- La rotación cambia de época.

💡 **Cómo se explica en la clase [B10-C12](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md):**
- En SPICE, la matriz `[w]ᵢ` «rota el sistema de coordenadas `w` radianes alrededor del eje `i` y rota los vectores `−w`» (S1): su matriz es la transpuesta de la activa.
- *Descripción textual:* para un mismo ángulo, la rotación activa aplica `R(θ)` y la pasiva aplica su transpuesta; los números se parecen pero los signos difieren, y confundirlas es el error más común.
- ⚠️ **Error frecuente:** Confundir rotación activa y pasiva (signo). Se corrige con los ejercicios 2 y 11.
- 🎯 **Por qué importa:** La Tierra gira una vuelta cada 23,93 horas: una estación de seguimiento ve pasar los satélites porque sus ejes locales rotan respecto del espacio inercial. Un satélite recibe órdenes expresadas en ejes terrestres y debe saber dónde están en ejes inerciales.
- 🔗 **Se estudia junto con:** activa, pasiva, eje de rotación, ángulo de rotación.

📘 **Dónde se aprende** (2 clases): [B10-C12 · Rotaciones en el plano y espacio](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md); [B88-C38 · Gestión de claves y secretos en aviónica](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md).

### Rotación 3‑1‑3

- La rotación 3‑1‑3 es `R_z(Ω) R_x(i) R_z(ω)`.

💡 **Cómo se explica en la clase [B71-C17](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md):**
- En 500 estados sintéticos (semilla 17) cumple `max|M Mᵀ − I| = 4.4e-16` y `|det M − 1| = 4.4e-16`: es una rotación propia.
- *Descripción textual:* las coordenadas perifocales se rotan al marco inercial; los invariantes (`h`, energía, componentes) y una integración inercial comprueban que la rotación es correcta.
- 🎯 **Por qué importa:** Casi todo error de signo o de orden en una rotación aparece como un plano equivocado. La decisión central: ¿cómo pasas del plano orbital al marco inercial y cómo compruebas que la transformación es correcta?
- 🔗 **Se estudia junto con:** sistema perifocal, matriz ortogonal, velocidad radial, transversal.

📘 **Dónde se aprende** (1 clase): [B71-C17 · Movimientos en planos orbitales](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md).

### Rotación activa

- Una rotación activa gira el punto manteniendo los ejes; una rotación pasiva gira los ejes y deja el punto, de modo que sus componentes cambian.

💡 **Cómo se explica en la clase [B04-C15](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md):**
- Distinguir rotación activa (de puntos) y pasiva (de ejes) y sus signos.
- Ejercicio 7. Gira el vector `(1; 1; 0)` +0,5 rad de forma activa alrededor de `x` y comprueba que es igual a la rotación pasiva de −0,5 rad.
- 🎯 **Por qué importa:** El ecuador de la Tierra y el plano de su órbita (la eclíptica) forman un ángulo de unos 23,4°. Los catálogos de estrellas se dan en coordenadas ecuatoriales; el movimiento del Sol, la Luna y los planetas es más simple en coordenadas eclípticas.
- 🔗 **Se estudia junto con:** matriz de rotación, ortogonal, determinante, inversa.

📘 **Dónde se aprende** (1 clase): [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md).

### Rotación de campo

- La rotación de campo es el giro de la imagen que sufre una montura altacimutal al seguir un objeto.
- La rotación de campo es el giro de la imagen respecto del horizonte; es el ángulo paraláctico `q`.

💡 **Cómo se explica en la clase [B08-C15](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md):**
- Además, la imagen gira (rotación de campo), irrelevante a ojo pero grave para fotografiar (C19).
- C --> E["Dos movimientos variables<br/>y rotación de campo"]
- 🎯 **Por qué importa:** A 120 aumentos, un planeta cruza el ocular en menos de dos minutos y tienes que empujar el tubo constantemente. La pregunta motivadora: ¿qué montura necesito y qué error puedo tolerar al seguir un objeto?
- 🔗 **Se estudia junto con:** montura, altacimutal, ecuatorial, ascensión recta.

📘 **Dónde se aprende** (3 clases): [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md); [B41-C18 · Monturas y mecanismos de seguimiento](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md); [B43-C13 · Montura altacimutal](../programa/clases/B43/B43-C13-montura-altacimutal/CLASE.md).

### Rotación de Faraday

- La rotación de Faraday `χ = χ₀ + RM λ²`.
- La rotación de Faraday: `χ = RM λ²`.

💡 **Cómo se explica en la clase [B51-C05](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md):**
- python programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/ionosfera.py
- 🎯 **Por qué importa:** A frecuencias bajas la ionosfera domina el error de fase y de polarización. La decisión central: ¿cómo se mide y se quita el efecto con las propias frecuencias de la observación?
- 🔗 **Se estudia junto con:** contenido electrónico total, retardo dispersivo, medida de rotación, ambigüedad nπ.

📘 **Dónde se aprende** (2 clases): [B46-C13 · Polarimetría de radio](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md); [B51-C05 · Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md).

### Rotación de Rodrigues

- La rotación de Rodrigues `v cos θ + (k×v) sen θ + k (k·v)(1−cos θ)`.

💡 **Cómo se explica en la clase [B43-C17](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md):**
- Calcular la deriva con rotaciones de Rodrigues exactas.
- El script [alineacion_polar.py](alineacion_polar.py) simula la deriva con rotaciones de Rodrigues, la compara con la predicción lineal e invierte para estimar el error (comprueba `1 %`).
- 🎯 **Por qué importa:** La alineación polar se corrige midiendo la deriva de una estrella. La decisión central: ¿qué deriva produce un error de acimut o de altura y cómo se invierte para corregirlo?
- 🔗 **Se estudia junto con:** error de acimut, error de altura, método de la deriva, predicción lineal.

📘 **Dónde se aprende** (1 clase): [B43-C17 · Alineación polar](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md).

### Rotación diferencial

- La rotación diferencial es girar a distinto ritmo según la latitud.
- La rotación diferencial es que la velocidad angular depende del radio.
- La rotación diferencial es que las zonas giran distinto.

💡 **Cómo se explica en la clase [B24-C11](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md):**
- Nombrar qué limita el modelo (rotación diferencial, pérdida de momento angular).
- 🎯 **Por qué importa:** La rotación y el campo explican por qué las estrellas jóvenes son más activas, por qué las enanas blancas y las estrellas de neutrones giran y se magnetizan tanto, y por qué no pueden girar a cualquier velocidad.
- 🔗 **Se estudia junto con:** velocidad de rotación, velocidad crítica, momento de inercia, momento angular.

📘 **Dónde se aprende** (3 clases): [B24-C11 · Rotación y campos magnéticos](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md); [B25-C02 · Brazos espirales y barra galáctica](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md); [B37-C11 · Rotación interna a partir del desdoblamiento de frecuencias](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md).

### Rotación pasiva

- Una rotación activa gira el punto manteniendo los ejes; una rotación pasiva gira los ejes y deja el punto, de modo que sus componentes cambian.

💡 **Cómo se explica en la clase [B04-C15](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md):**
- A["Componentes ecuatoriales<br/>(x, y, z)"] -->|"R_x(ε): rotación pasiva de ejes"| B["Componentes eclípticas"]
- *Descripción textual:* de las componentes ecuatoriales se pasa a las eclípticas con la rotación pasiva `R_x(ε)`; la traspuesta devuelve las ecuatoriales; de las eclípticas salen longitud y latitud con `atan2` y `arcsen`; y la matriz se comprueba con ortogonalidad y determinante 1.
- 🎯 **Por qué importa:** El ecuador de la Tierra y el plano de su órbita (la eclíptica) forman un ángulo de unos 23,4°. Los catálogos de estrellas se dan en coordenadas ecuatoriales; el movimiento del Sol, la Luna y los planetas es más simple en coordenadas eclípticas.
- 🔗 **Se estudia junto con:** matriz de rotación, ortogonal, determinante, inversa.

📘 **Dónde se aprende** (1 clase): [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md).

### Rotación sincrónica

- La rotación sincrónica es que la Luna gira sobre su eje una vez por cada vuelta alrededor de la Tierra, por lo que muestra siempre la misma cara; la libración son pequeños balanceos que dejan ver algo más de la mitad (S3).

💡 **Cómo se explica en la clase [B08-C08](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md):**
- Como la rotación es sincrónica, ves siempre la misma cara, pero las tablas de la NASA muestran el punto de la Luna que mira a la Tierra (el «punto subterrestre») moviéndose: en 2025 su longitud selenográfica varió entre −7,7° y +8,0°, y su latitud entre −6,8° y +6,9°.
- Explicar la rotación sincrónica y la libración, con sus magnitudes de 2025.
- 🎯 **Por qué importa:** La Luna es el primer blanco de cualquier observación y el principal enemigo de las observaciones de objetos débiles (C12). Saber su fase y cuándo está en el cielo es parte de toda planificación.
- 🔗 **Se estudia junto con:** fase, elongación, ángulo de fase, Creciente.

📘 **Dónde se aprende** (1 clase): [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md).

### Rotacional

- El rotacional `∇×F` mide cuánto «gira» (ec. 1.6.22).

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- Para la gravedad, el rotacional es cero (laboratorio: `< 10⁻¹⁵ s⁻²`): el campo es conservativo.
- Rotacional cero no significa «sin movimiento».
- ⚠️ **Error frecuente:** Confundir divergencia (escalar) con rotacional (vector). Se corrige con los ejercicios 1 y 2.
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.
- 🔗 **Se estudia junto con:** campo vectorial, divergencia, integral de línea, conservativo.

📘 **Dónde se aprende** (1 clase): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md).

### Rotaciones elementales

- Las rotaciones elementales (activas, regla de la mano derecha) son `Rₓ(a) = [[1, 0, 0], [0, cos a, −sin a], [0, sin a, cos a]]`, `R_y(a) = [[cos a, 0, sin a], [0, 1, 0], [−sin a, 0, cos a]]`, `R_z(a) = [[cos a, −sin a, 0], [sin a, cos a, 0], [0, 0, 1]]`.

💡 **Cómo se explica en la clase [B10-C13](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu cuaderno de matrices de rotación: tres matrices elementales con su verificación, una composición de dos giros en ambos órdenes con el efecto sobre un vector, el eje y el ángulo de la composición, la matriz de marco de SPICE y la prueba de deriva.
- 🎯 **Por qué importa:** La actitud de un satélite (hacia dónde apuntan sus ejes) se guarda como una matriz de rotación: sus columnas son los ejes del cuerpo expresados en el sistema inercial. Con ella, un seguidor estelar, un panel o una antena se orientan sin ambigüedad.
- 🔗 **Se estudia junto con:** grupo SO(3), antisimétrica, fórmula de Rodrigues, matriz de transformación de marco.

📘 **Dónde se aprende** (1 clase): [B10-C13 · Matrices de rotación tridimensional](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md).

### Rotador rápido

- Un rotador rápido tiene rotación ordenada comparable a su dispersión; uno lento, poca rotación (S2).

💡 **Cómo se explica en la clase [B25-C09](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md):**
- Cappellari (S2), con espectroscopía de campo integral, separa las galaxias de tipo temprano en rotadores rápidos y lentos: los lentos son débilmente triaxiales y dominan por encima de una masa crítica de unos `2 × 10¹¹ M☉`; los rápidos, por debajo, se parecen a las espirales.
- Describir qué distingue rotadores rápidos y lentos entre las galaxias de tipo temprano.
- 🎯 **Por qué importa:** Las galaxias parecen muy distintas: discos con brazos y gas, o bolas suaves de estrellas viejas. Esa diferencia guarda su historia (formación estelar, fusiones) y exige un lenguaje común para compararlas.
- 🔗 **Se estudia junto con:** galaxia espiral, elíptica, lenticular, bulbo.

📘 **Dónde se aprende** (1 clase): [B25-C09 · Galaxias elípticas y espirales](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md).

### Rotor rígido

- El rotor rígido es una molécula lineal que gira sin deformarse; sus niveles son `E_J = h B J(J+1)` y las transiciones `J → J−1` caen en `ν = 2 B J`.
- Un rotor rígido es una molécula cuyos núcleos giran a distancia fija.
- El rotor rígido: `E_J = hB J(J+1)`.

💡 **Cómo se explica en la clase [B46-C12](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md):**
- Límite: rotor rígido, ETL y sin profundidad óptica.
- Límites: rotor rígido, ETL, sin opacidad.
- 🎯 **Por qué importa:** Qué transición observar depende de la temperatura del gas, porque la población de cada nivel cambia. La decisión central: ¿qué línea es la más intensa a una temperatura dada?
- 🔗 **Se estudia junto con:** transición, ETL, función de partición, temperatura de excitación.

📘 **Dónde se aprende** (3 clases): [B46-C12 · Emisiones moleculares](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md); [B55-C09 · Espectros moleculares de radio](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md); [B62-C01 · Espectros rotacionales de moléculas: niveles y reglas de selección](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md).

### Rótulo

- Un rótulo es consultada, sintética o calculada.
- Un rótulo nombra la magnitud y su unidad.

💡 **Cómo se explica en la clase [B126-C06](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md):**
- Una cifra en una presentación debe llevar: valor, unidad, año, rótulo y fuente (o su fórmula y entradas).
- *Descripción textual:* las entradas rotuladas permiten recalcular cada cifra de la presentación y compararla con lo mostrado; el resultado marca errores o cifras sin rótulo; con la simulación se agrega el rango, y todo va al anexo.
- 🎯 **Por qué importa:** [B124-C19](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) redacta propuestas de misión, no financieras. La decisión central: ¿qué cifra se muestra, con qué rótulo y con qué rango, de modo que un tercero pueda comprobarla?
- 🔗 **Se estudia junto con:** matriz de evidencia, trazable, rango de incertidumbre, solicitación general.

📘 **Dónde se aprende** (2 clases): [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md); [B126-C06 · Presentación financiera ante inversionistas con evidencia](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md).

### Rotura de doble cadena (DSB)

- Una rotura de doble cadena (DSB) corta las dos hebras del ADN.

💡 **Contexto en la clase [B64-C01](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md):**
- **Idea central (modelo mental):** El modelo trata cada genoma irradiado como una urna: la dosis decide cuántos cortes caen, y la reparación decide cuántos puede asumir.
- 🎯 **Por qué importa:** La radiación ionizante rompe el ADN, y una célula muere cuando el daño supera su capacidad de reparación. La pregunta motivadora: ¿por qué dos organismos con el mismo daño inicial por gray sobreviven a dosis tan distintas?
- 🔗 **Se estudia junto con:** dosis absorbida, rendimiento, capacidad de reparación, supervivencia.

📘 **Dónde se aprende** (1 clase): [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md).

### Rotura doble

- Una rotura doble (DSB) rompe las dos hebras del ADN; es el daño más peligroso.

💡 **Contexto en la clase [B112-C05](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md):**
- 🎯 **Por qué importa:** Falta la clase de mecanismos moleculares de daño y reparación. Sin ella, la diferencia de eficacia biológica entre fotones e iones pesados (B112-C01, C02) y la incertidumbre del riesgo (C04) parecen cifras arbitrarias.
- 🔗 **Se estudia junto con:** daño agrupado o complejo, reparación, unión de extremos no homólogos, error de reunión.

📘 **Dónde se aprende** (1 clase): [B112-C05 · Daño y reparación del ADN por radiación espacial](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md).

### Rover

- Un rover es un robot móvil de superficie; un orbitador es una nave robótica en órbita.

💡 **Cómo se explica en la clase [B97-C01](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md):**
- Analogía: el orbitador es un dron que barre un campo desde arriba y el rover es una persona que camina entre los surcos.
- Un orbitador ilustrativo a `300 km` con una franja de `12 km` la cubre con 4,44 min de imagen continua; un rover que debe recorrer `5 km` con un factor de uso `0,5` tarda 16,45 días de operación.
- 🎯 **Por qué importa:** Elegir entre «ir con un rover» y «mirar desde órbita» es la primera decisión de una misión robótica, y se toma con órdenes de magnitud. Sin ellos, se prometen traslados que tardan meses o coberturas que una órbita no entrega.
- 🔗 **Se estudia junto con:** orbitador, velocidad sobre el suelo, franja, tasa de cobertura.

📖 **Explicado a fondo:** [Rover y movilidad planetaria](esencial/ampliacion-n-z.md#rover-y-movilidad-planetaria) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B97-C01 · Robots rover y orbitadores](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md).

### Rozamiento

- El rozamiento es la fuerza de contacto paralela a la superficie que se opone al deslizamiento.

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- En un plano inclinado, un eje a lo largo de la rampa y otro perpendicular evita descomponer la normal y el rozamiento.
- Ejercicio 6. Un bloque de 20 kg en una rampa de 30° sin rozamiento: ¿qué componente del peso va a lo largo de la rampa?
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?
- 🔗 **Se estudia junto con:** diagrama de cuerpo libre (DCL), peso, normal, tensión.

📘 **Dónde se aprende** (1 clase): [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md).

### RPE

- ATE: RMSE de la traslación tras alinear la estimación con la verdad por cuerpo rígido (F2). RPE: error del movimiento relativo entre pares de poses separados por una ventana (F2).

💡 **Cómo se explica en la clase [B99-C06](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md):**
- Para el RPE se mide el error del movimiento relativo entre pares de poses, y la opción de ventana fija permite comparar cada pose con otra posterior a una separación dada (en segundos, metros, radianes o cuadros), útil para estimar la deriva.
- La página no escribe las fórmulas del RMSE ni del RPE; las que siguen son las del laboratorio.
- ⚠️ **Error frecuente:** Creer que ATE bajo implica RPE bajo. El grafo bajó el ATE sin cambiar el RPE (8.5).
- 🎯 **Por qué importa:** «Mi robot deriva poco» no es una afirmación comprobable. La decisión central: ¿qué métrica, con qué alineación y con qué ventana, describe el error que importa para la tarea?
- 🔗 **Se estudia junto con:** ATE, Alineación, Ventana (delta), Deriva.

📘 **Dónde se aprende** (1 clase): [B99-C06 · Evaluación de deriva y error de trayectoria](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md).

### RPN

- El RPN es `S×O×D`.

💡 **Cómo se explica en la clase [B83-C22](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md):**
- Ejemplo: rueda de reacción, modo «fricción creciente», efecto «apuntamiento degradado», `S = 6`, `O = 5`, `D = 5`: `RPN = 150`, el mayor.
- La batería (cortocircuito de celda, `S = 9`) tiene RPN 135 y `p = 1,56 %`.
- ⚠️ **Error frecuente:** Multiplicar escalas ordinales como si fueran números exactos. Usa el RPN para priorizar, no como medida absoluta
- 🎯 **Por qué importa:** Los fallos que no se anticipan se descubren en órbita. La decisión central: ¿qué modos de fallo hay que atacar primero, cuánta probabilidad tienen en la vida de la misión y qué cambia si mejoro su detección?
- 🔗 **Se estudia junto con:** modo de fallo, efecto, S, O.

📘 **Dónde se aprende** (1 clase): [B83-C22 · Análisis de modos y efectos de fallo (FMEA) en sistemas espaciales](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md).

### RPO

- El RPO es la pérdida máxima de datos aceptable, medida en tiempo.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- Con RPO de 4 h, una copia cada 1 h cumple (pérdida máxima 1 h) y cada 6 h o 24 h no.
- D["copias cada T"] --> P["perdida maxima = T vs RPO"]
- ⚠️ **Error frecuente:** Confundir RPO con RTO. El RPO es de datos y el RTO de servicio; ver sección 6.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?
- 🔗 **Se estudia junto con:** disponibilidad, MTBF, MTTR, RTO.

📘 **Dónde se aprende** (1 clase): [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### RRW

- El RRW (*rate random walk*) `K` es la deriva aleatoria del sesgo, en `rad/s/√s`.

💡 **Cómo se explica en la clase [B87-C06](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md):**
- G["tasa medida = verdad + ARW + sesgo RRW"] --> P["promedios de duracion tau"]
- Analogía: un reloj que se adelanta con un tic aleatorio (ARW) y que además cambia de ritmo a lo largo del día (RRW): para periodos cortos domina el tic y para largos domina el cambio de ritmo.
- 🎯 **Por qué importa:** Entre dos medidas de un sensor de vector, la actitud se propaga integrando el giroscopio, y esa integración se desvía. La decisión central: ¿cada cuánto hay que corregir con otro sensor, y qué parte de la deriva es ruido blanco y cuál sesgo?
- 🔗 **Se estudia junto con:** ARW, varianza de Allan, inestabilidad de sesgo, tasa de muestreo.

📘 **Dónde se aprende** (1 clase): [B87-C06 · Giroscopios MEMS](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md).

### RSET

- El RSET (*required safe egress time*) es el tiempo necesario: detección, reunión, traslado, paso por escotilla y verificación.

💡 **Cómo se explica en la clase [B110-C03](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md):**
- Con `N = 4` y sin varianza, `RSET = 20 + 60 + 90 + 4 × 20 + 120 = 370 s`; el laboratorio lo reproduce de forma exacta.
- Pasar de 2 a 6 personas añade `1,78 min` al RSET mediano por el cuello de botella de la escotilla y por el máximo de las reuniones.
- ⚠️ **Error frecuente:** Tomar el RSET como un número único. Es una distribución con cola larga (8.2 y 8.3).
- 🎯 **Por qué importa:** Ninguna clase anterior trata evacuación, refugio y vehículos de escape. La decisión central: ¿alcanza el margen entre ASET y RSET, y cuánto de ese margen depende de supuestos que no se conocen?
- 🔗 **Se estudia junto con:** ASET, margen, refugio, cuello de botella.

📘 **Dónde se aprende** (1 clase): [B110-C03 · Evacuación y refugio de emergencia](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md).

### RSS

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

📘 **Dónde se aprende** (4 clases): [B84-C16 · Tolerancias de fabricación](../programa/clases/B84/B84-C16-tolerancias-de-fabricacion/CLASE.md); [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md); [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md); [B90-C05 · Documentación de interfaces](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md).

### RTG

- Un RTG (*radioisotope thermoelectric generator*) convierte el calor del decaimiento en electricidad sin partes móviles.

💡 **Contexto en la clase [B86-C16](../programa/clases/B86/B86-C16-generadores-radioisotopicos/CLASE.md):**
- 🎯 **Por qué importa:** Un generador radioisotópico no depende de la distancia al Sol ni del eclipse, pero su potencia decae con el combustible y con los termopares y su eficiencia es baja. Entender esa curva decide qué misiones lo usan.
- 🔗 **Se estudia junto con:** GPHS, vida media, degradación del termopar, eficiencia de sistema.

📘 **Dónde se aprende** (1 clase): [B86-C16 · Generadores radioisotópicos](../programa/clases/B86/B86-C16-generadores-radioisotopicos/CLASE.md).

### RTLT

- El RTLT es el tiempo de ida y vuelta de la luz.

💡 **Cómo se explica en la clase [B75-C19](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md):**
- `50,6 %` por muestreo) tiene un RTLT mayor que 30 min.
- Reacción = `RTLT + 1800 s` (sintético): `2323 s` en el mínimo, `3489 s` en el medio y `4319 s` en el máximo.
- ⚠️ **Error frecuente:** Confundir retardo unidireccional con RTLT. Se corrige con la sección 6.
- 🎯 **Por qué importa:** No se puede dirigir desde la Tierra lo que sucede en minutos. La decisión central: ¿qué eventos duran menos que el tiempo mínimo de reacción desde tierra y por tanto deben ser autónomos?
- 🔗 **Se estudia junto con:** retardo unidireccional, tiempo de reacción, autonomía, conjunción solar.

📘 **Dónde se aprende** (1 clase): [B75-C19 · Restricciones de navegación autónoma](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md).

### RTO

- El RTO es el tiempo objetivo para restablecer el servicio; el WRT es el tiempo adicional para recuperar el trabajo; el MTD es el tiempo máximo tolerable de interrupción.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- F["fallo"] --> R["recuperar el servicio: RTO"]
- *Descripción textual:* desde el fallo corren el RTO y el WRT, cuya suma no debe pasar del MTD, mientras el costo crece; el RPO limita el intervalo entre copias.
- ⚠️ **Error frecuente:** Confundir RTO con MTTR. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?
- 🔗 **Se estudia junto con:** disponibilidad, MTBF, MTTR, WRT.

📘 **Dónde se aprende** (1 clase): [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### R-tree

- Un R-tree es un índice jerárquico de cajas.

💡 **Cómo se explica en la clase [B14-C28](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md):**
- Resultado: el R-tree devuelve 101 escenas.
- Una sola medición dio 0,27 ms con el R-tree y 0,77 ms con NumPy sobre todas las cajas.
- 🎯 **Por qué importa:** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.
- 🔗 **Se estudia junto con:** índice espacial, tabla virtual, consulta de solapamiento, consulta puntual.

📘 **Dónde se aprende** (1 clase): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md).

### Rúbrica

- La rúbrica define niveles 1 a 4 por criterio.

💡 **Cómo se explica en la clase [B124-C20](../programa/clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md):**
- Un kappa de ese orden es bajo e indica que la rúbrica o su entrenamiento necesitan afinarse; no hay umbral universal.
- Calcular un puntaje ponderado de rúbrica en escala 0–100.
- 🎯 **Por qué importa:** Un portafolio con una nota promedio alta puede ocultar una falta grave, como presentar datos inventados como reales. La decisión central: ¿qué hace falta para declarar logrado un portafolio y cómo se sabe que dos revisores miden lo mismo?
- 🔗 **Se estudia junto con:** puntaje, condiciones críticas, kappa de Cohen, kappa ponderado.

📘 **Dónde se aprende** (1 clase): [B124-C20 · Proyecto integrador y portafolio profesional](../programa/clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md).

### Rúbrica analítica

- Una rúbrica analítica puntúa cada criterio por separado; una holística, el trabajo en conjunto.

💡 **Cómo se explica en la clase [B131-C09](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md):**
- Redactar una rúbrica analítica con criterios y niveles descritos en términos observables.
- 🎯 **Por qué importa:** Una rúbrica sin acuerdo entre evaluadores asigna notas que dependen de quién corrige. La decisión central: ¿dos personas distintas darían el mismo nivel a este trabajo, y cómo lo sabes?
- 🔗 **Se estudia junto con:** holística, acuerdo exacto, adyacente, Kappa.

📘 **Dónde se aprende** (1 clase): [B131-C09 · Rúbricas de evaluación](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md).

### Rueda

- Una rueda (*wheel*) es un paquete ya compilado para una plataforma; una distribución fuente (*sdist*) es el código sin compilar.

💡 **Cómo se explica en la clase [B14-C12](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md):**
- Hay una por cada archivo descargable: la distribución fuente y una rueda por plataforma, versión de Python y arquitectura.
- sumas SHA-256 en el bloqueo: 66 (sdist + ruedas de cada plataforma)
- 🎯 **Por qué importa:** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.
- 🔗 **Se estudia junto con:** proyecto, resolutor, archivo de bloqueo, bloqueo universal.

📘 **Dónde se aprende** (1 clase): [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Rueda de reacción

- La rueda de reacción intercambia momento con el cuerpo.

💡 **Cómo se explica en la clase [B87-C11](../programa/clases/B87/B87-C11-ruedas-de-reaccion/CLASE.md):**
- La evidencia es la maniobra de un eje con el histórico de la rueda de reacción del ejercicio 12 (sección 20).
- B87-C11 rueda de reaccion | SINTETICO: I = diag(0.35, 0.40, 0.30) kg m^2; par max 0.01 N m, momento max 0.05 N m s, I_rueda = 5e-5 kg m^2
- 🎯 **Por qué importa:** La rueda es el actuador estándar del control fino de tres ejes. La decisión central: ¿cuánto tarda una maniobra con límites de par y de momento, y qué velocidad alcanza la rueda?
- 🔗 **Se estudia junto con:** par de rueda, momento almacenado, saturación de momento, perfil triangular.

📘 **Dónde se aprende** (2 clases): [B47-C10 · Estabilidad de apuntamiento](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md); [B87-C11 · Ruedas de reacción](../programa/clases/B87/B87-C11-ruedas-de-reaccion/CLASE.md).

### Rugosidad

- La rugosidad es la desviación típica de los residuos de ese plano.
- La rugosidad es la desviación típica del residuo respecto del plano.
- Rejilla de elevación (2.5D): un valor de altura por celda (F5). Rugosidad: dispersión de la altura respecto de un plano local.

💡 **Cómo se explica en la clase [B99-C05](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md):**
- La rugosidad es la desviación típica del residuo de las medias de una ventana `3×3` respecto de su plano ajustado.
- Con umbrales de 15° y 5 cm (sintéticos) se declara traversable 96 % del interior; la roca (pendiente máxima 22,9°) queda no traversable en 8 de sus 12 celdas, por pendiente y no por rugosidad (rugosidad máxima 4,9 cm).
- 🎯 **Por qué importa:** Un mapa útil para navegar distingue lo ocupado, lo libre y lo que no se sabe, y dice si el terreno es pisable. La decisión central: ¿cómo fusionar medidas ruidosas en cada celda y qué umbrales de pendiente y rugosidad declaran un terreno traversable?
- 🔗 **Se estudia junto con:** Rejilla de ocupación, Log-odds, Recorte (clamping), Rejilla de elevación (2.5D).

📘 **Dónde se aprende** (3 clases): [B99-C05 · Mapas de ocupación y rejillas de elevación](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md); [B102-C08 · Traversabilidad y evaluación de riesgo de terreno](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md); [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Rugosidad RMS

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B43-C23](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md):**
- Como una pared con polvo fino: la rugosidad no se ve, pero cada grano esparce un poco de luz; cuanto más corta la longitud de onda, más se nota.
- *Descripción textual:* una PSD fija la rugosidad en una banda; la TIS la convierte en luz dispersa por la fórmula escalar.
- 🎯 **Por qué importa:** La luz dispersa reduce el contraste y la reflectancia especular. La decisión central: ¿qué rugosidad RMS, en qué banda de frecuencias espaciales, deja la luz dispersa por debajo del presupuesto?
- 🔗 **Se estudia junto con:** PSD, TIS, banda, reflectancia especular.

📘 **Dónde se aprende** (1 clase): [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md).

### Ruido

- El ruido es una perturbación aleatoria de las muestras.
- El ruido es la parte de la serie que no se explica con el modelo.
- El fondo (*background*) es el nivel del cielo sin fuentes; el ruido `σ` su desviación.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C11](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md):**
- Si cada muestra tiene ruido independiente de desviación `σ` y paso `Δt`, el error en la integral crece como `σ Δt √N` (no como `N`).
- La elección del método importa más que añadir ruido o decimales.
- ⚠️ **Error frecuente:** Esperar que más puntos eliminen el ruido. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.
- 🔗 **Se estudia junto con:** integral definida, sumas de Riemann, partición, regla del punto izquierdo (derecho).

📘 **Dónde se aprende** (9 clases): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B22-C01 · Problemas directos e inversos y mal condicionamiento](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md); [B42-C16 · Lazo de control de óptica adaptativa](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md) y 3 más.

### Ruido 1/f

- El ruido 1/f tiene más potencia a baja frecuencia.

💡 **Cómo se explica en la clase [B49-C08](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md):**
- El ruido blanco sigue `τ^(−1/2)` (la estimación de Allan con pocos intervalos tiene una incertidumbre del orden de `1/√(2n)`, hasta 12 % en `τ` largos).
- Como pesar con una balanza que se descalibra: pesar mucho rato promedia el ruido, pero la descalibración crece; hay que tarar a menudo.
- 🎯 **Por qué importa:** Integrar más tiempo no siempre mejora la medida: la deriva lo impide. La decisión central: ¿hasta qué tiempo de integración vale la pena, y cuándo hay que conmutar?
- 🔗 **Se estudia junto con:** ecuación del radiómetro, deriva de ganancia, desviación de Allan, conmutación tipo Dicke.

📘 **Dónde se aprende** (1 clase): [B49-C08 · Estabilidad de ganancia de receptores y variaciones de ganancia](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md).

### Ruido angular

- El centroide tiene ruido `σ_px`; el ruido angular por estrella es `σ_a = atan(σ_px/f)`.

💡 **Cómo se explica en la clase [B87-C07](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md):**
- Paso 1 · Ruido angular. `σ_a = atan(0,1/3889) = 5,30″`.
- Pasar el ruido de centroide en píxeles a ruido angular por estrella.
- 🎯 **Por qué importa:** Para apuntar un telescopio o una antena con precisión de segundos de arco, un sensor solar o un magnetómetro no bastan. La decisión central: ¿cuántas estrellas hacen falta y por qué el giro alrededor del eje óptico (balanceo) es mucho peor que el apuntamiento?
- 🔗 **Se estudia junto con:** modelo estenopeico, IFOV, centroide, error transversal.

📘 **Dónde se aprende** (1 clase): [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md).

### Ruido blanco

- El ruido blanco `w[n]` es una sucesión de variables independientes, de media 0 y varianza `σ²`: no tiene memoria y su espectro es plano (el nombre viene de la luz blanca, que mezcla todas las frecuencias por igual).
- El ruido blanco `N` produce un paseo aleatorio de velocidad (VRW) con densidad `N` en `m/s/√s`.

💡 **Cómo se explica en la clase [B15-C03](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md):**
- El ruido blanco es el ruido de la lluvia sobre un techo: cada gota es independiente de la anterior.
- W["Ruido blanco<br/>w[n]"] --> A["AR(1):<br/>x = φx₋₁ + w"]
- ⚠️ **Error frecuente:** Creer que un histograma gaussiano implica ruido blanco. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una regla heredada de la física del laboratorio dice que, al promediar `N` mediciones, el error baja como `1/√N`. Esa regla solo vale si los errores de cada medición son independientes.
- 🔗 **Se estudia junto con:** AR(1), paseo aleatorio, ruido coloreado, ruido rojo.

📘 **Dónde se aprende** (3 clases): [B15-C03 · Ruido blanco y coloreado](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md); [B80-C02 · Modelo de error de acelerómetros](../programa/clases/B80/B80-C02-modelo-de-error-de-acelerometros/CLASE.md).

### Ruido blanco de frecuencia

- El ruido blanco de frecuencia tiene muestras independientes de `y`.
- El ruido blanco de frecuencia (pendiente −1/2).
- El ruido blanco de frecuencia domina a corto plazo y el paseo aleatorio de frecuencia a largo plazo.

💡 **Cómo se explica en la clase [B13-C07](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md):**
- Tres relojes simulados tienen un ruido blanco de frecuencia (`σ = 10⁻¹²`), un paseo aleatorio de frecuencia y una deriva lineal.
- Reconocer la pendiente de la curva para ruido blanco de frecuencia (`−1/2`), paseo aleatorio (`+1/2`) y deriva lineal (`+1`).
- 🎯 **Por qué importa:** Dos relojes pueden tener la misma desviación de frecuencia media y comportarse de forma muy distinta: uno oscila alrededor de su valor y otro se aleja de él con el tiempo. La desviación típica ordinaria no sirve para describirlo, porque en un reloj con deriva no converge.
- 🔗 **Se estudia junto con:** estabilidad de frecuencia, promedio, varianza de Allan, desviación de Allan.

📘 **Dónde se aprende** (3 clases): [B13-C07 · Relojes atómicos y frecuencia](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md); [B46-C08 · Osciladores y estabilidad](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md); [B74-C16 · Sincronización temporal](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md).

### Ruido coloreado

- El ruido coloreado es cualquier ruido con memoria; el ruido rojo concentra su potencia en las frecuencias bajas.

💡 **Cómo se explica en la clase [B15-C03](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md):**
- Los dos primeros se parecen al ruido blanco; las variaciones lentas son ruido coloreado.
- python programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/ruido.py
- 🎯 **Por qué importa:** Una regla heredada de la física del laboratorio dice que, al promediar `N` mediciones, el error baja como `1/√N`. Esa regla solo vale si los errores de cada medición son independientes.
- 🔗 **Se estudia junto con:** ruido blanco, AR(1), paseo aleatorio, ruido rojo.

📘 **Dónde se aprende** (1 clase): [B15-C03 · Ruido blanco y coloreado](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md).

### Ruido de correlación

- El ruido de correlación: por parte `(S+N)/√(2M)`.

💡 **Cómo se explica en la clase [B46-C15](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md):**
- *Descripción textual:* la correlación cruzada de dos flujos con una señal común da la visibilidad, con un ruido que baja con el número de muestras.
- El script [correlador.py](correlador.py) simula la correlación, estima la visibilidad y compara FX con XF (comprueba el ruido y la coincidencia).
- 🎯 **Por qué importa:** La visibilidad es el dato básico de la imagen, y su ruido determina la sensibilidad. La decisión central: ¿cuántas muestras hay que correlacionar para fijar amplitud y fase con la precisión requerida?
- 🔗 **Se estudia junto con:** visibilidad, XF, FX, lag.

📘 **Dónde se aprende** (1 clase): [B46-C15 · Correladores y visibilidades](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md).

### Ruido de disparo

- El ruido de disparo es la incertidumbre por conteo de fotones.
- El ruido de disparo es la fluctuación de Poisson.
- El ruido de disparo es la fluctuación de Poisson del número de fotones: varianza igual a la media.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C15](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md):**
- *Descripción textual:* la varianza total suma el ruido de disparo de la señal (`N`), el del cielo, el de la oscuridad y el de lectura; la SNR es la señal dividida por la raíz de esa suma.
- Su límite: la ecuación supone ruido de disparo de Poisson y lectura gaussiana, sin ruido de patrón fijo ni errores de aplanado.
- ⚠️ **Error frecuente:** Olvidar el ruido de disparo de la propia señal. Se corrige con los ejercicios 1 y 3.
- 🎯 **Por qué importa:** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.
- 🔗 **Se estudia junto con:** fondo de cielo B, corriente de oscuridad D, ruido de lectura R, ganancia.

📘 **Dónde se aprende** (5 clases): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md); [B28-C06 · Interferómetros gravitacionales](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md); [B29-C02 · Curvas de luz fotométricas](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md); [B44-C01 · Principios fotoeléctricos](../programa/clases/B44/B44-C01-principios-fotoelectricos/CLASE.md); [B48-C13 · Calibraciones nocturnas](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md).

### Ruido de etiquetas

- El ruido de etiquetas es la fracción de etiquetas incorrectas.

💡 **Cómo se explica en la clase [B17-C10](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md):**
- En el laboratorio, un modelo entrenado con etiquetas con 20 % de ruido simétrico, y evaluado con etiquetas limpias, dio 0,843, igual que uno entrenado con etiquetas limpias (0,843): el ruido simétrico apenas afectó el entrenamiento en este caso (muchos datos, un modelo simple).
- Pero la evaluación sí cambia: si se mide el modelo contra las etiquetas ruidosas, la exactitud aparente es `A(1 − η) + (1 − A)η`, con `A` la exactitud real y `η` el ruido.
- 🎯 **Por qué importa:** Se quiere entrenar un modelo que distinga galaxias espirales de elípticas. Hay un millón de imágenes y nadie las ha etiquetado.
- 🔗 **Se estudia junto con:** protocolo de etiquetado, anotador, acuerdo observado, acuerdo esperado por azar.

📘 **Dónde se aprende** (1 clase): [B17-C10 · Conjuntos de datos etiquetados para aprendizaje supervisado](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md).

### Ruido de fondo

- El ruido de fondo es el nivel del recinto receptor.

💡 **Cómo se explica en la clase [B109-C09](../programa/clases/B109/B109-C09-privacidad-y-espacios-personales/CLASE.md):**
- Más ruido de fondo da más privacidad (a costa de otros criterios, ver [B109-C10](../B109-C10-acustica-y-control-de-ruido-interior/CLASE.md)).
- Comparar con el ruido de fondo según un criterio de privacidad.
- 🎯 **Por qué importa:** Una división que no se ve a través pero que deja pasar cada palabra no da privacidad. La decisión central: ¿qué masa debe tener una división para que lo que se dice al otro lado quede por debajo del ruido de fondo?
- 🔗 **Se estudia junto con:** privacidad acústica, nivel de presión sonora, pérdida de transmisión, ley de masa.

📘 **Dónde se aprende** (1 clase): [B109-C09 · Privacidad y espacios personales](../programa/clases/B109/B109-C09-privacidad-y-espacios-personales/CLASE.md).

### Ruido de fotones

- El ruido de fotones relativo es `1/√N`.
- El ruido de fotones (o de disparo) es de tamaño `√N`; el criterio de Rayleigh da el límite de difracción `1,22 λ/D`.
- El ruido de fotones sigue una ley de Poisson: su varianza es igual a la señal.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B42-C14](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md):**
- A 400 fotones el ruido de lectura (`0,1375 px`) domina sobre el de fotones (`0,0449 px`).
- Ejercicio 10 · transferencia. Transferencia. Un compañero dice que más fotones siempre reducen el ruido como `1/√N`.
- 🎯 **Por qué importa:** El Shack-Hartmann es el sensor más usado en óptica adaptativa. La decisión central: ¿cuántos fotones hacen falta por subapertura para que el centroide sea preciso?
- 🔗 **Se estudia junto con:** subapertura, centroide, de lectura, ventana.

📘 **Dónde se aprende** (4 clases): [B42-C14 · Sensores Shack-Hartmann](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md); [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md); [B57-C04 · Satélites ópticos de observación](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md).

### Ruido de Johnson

- El ruido de Johnson es el ruido térmico de una resistencia.

💡 **Contexto en la clase [B49-C07](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md):**
- **Idea central (modelo mental):** Como un termo: lo que importa es cuánto calor se cuela por conducción y radiación, no solo cuán frío esté el líquido.
- 🎯 **Por qué importa:** Cada kelvin ahorrado exige vatios en la cabeza fría, y cada vatio de carga reduce el margen. La decisión central: ¿a qué temperatura enfriar y cuánta carga admite el criostato?
- 🔗 **Se estudia junto con:** potencia disponible, cabeza fría, carga térmica, aislamiento multicapa.

📘 **Dónde se aprende** (1 clase): [B49-C07 · Criogenia y refrigeración de receptores de radio](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md).

### Ruido de lectura

- El ruido de lectura viene de la electrónica; el ruido de Poisson (de fotones), de la naturaleza discreta de la luz: su varianza es igual a la señal en electrones.
- El ruido de lectura es constante por pixel.
- El ruido de lectura es la parte aleatoria de cada lectura.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- La varianza de un píxel de cielo es: lectura `σ_L²` + fotones (`cielo + oscuro`) + el ruido del oscuro maestro, que vale `(σ_L² + oscuro)/K` si se promedian `K` oscuros.
- Ejercicio 4. En un píxel de cielo de 50 e⁻ con lectura 5 ADU, ¿domina el ruido de lectura o el de fotones?
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.
- 🔗 **Se estudia junto con:** imagen digital, píxel, ADU, ganancia.

📘 **Dónde se aprende** (6 clases): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B29-C02 · Curvas de luz fotométricas](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md); [B44-C06 · Ruido de lectura](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md); [B47-C15 · Calibración a bordo](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md); [B48-C13 · Calibraciones nocturnas](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md).

### Ruido de lectura R

- El ruido de lectura `R` es el ruido del electrónico al leer cada píxel, en `e⁻` rms, independiente del tiempo.

💡 **Cómo se explica en la clase [B13-C15](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md):**
- Para verificar la fórmula, se simulan `2 × 10⁵` medidas con Poisson (señal y fondo) y ruido de lectura gaussiano: `SNR = 10,674` frente a `10,687` de la ecuación (`0,1 %` de diferencia).
- La señal llena una cubeta (el pozo); el fondo, la oscuridad y el ruido de lectura son cuatro «grifos» que añaden incertidumbre.
- ⚠️ **Error frecuente:** Pensar que muchas lecturas cortas eliminan el ruido de lectura. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.
- 🔗 **Se estudia junto con:** ruido de disparo, fondo de cielo B, corriente de oscuridad D, ganancia.

📘 **Dónde se aprende** (1 clase): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md).

### Ruido de medición

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B42-C20](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md):**
- **Idea central (modelo mental):** Como un conductor que corrige el volante mirando la carretera con un poco de retraso: reduce el error pero no lo elimina.
- 🎯 **Por qué importa:** El producto es un informe con evidencia numérica de cuánto corrige un lazo dado, con sus límites. La decisión central: ¿qué ganancia y qué ruido dan el Strehl más alto y cómo se comprueba?
- 🔗 **Se estudia junto con:** lazo cerrado, flujo congelado, sensor ideal, Strehl instantáneo.

📘 **Dónde se aprende** (1 clase): [B42-C20 · Laboratorio de corrección óptica simulada](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md).

### Ruido de medida

- En un lazo cerrado, la referencia `r` es lo que se desea, la salida `y` lo que se tiene, el error `e = r − H y` su diferencia, `d` una perturbación y `n` el ruido de medida.
- El ruido de medida es la variación aleatoria del sensor.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- El ruido de medida `n` llega a `θ` con la misma `T` que la referencia pero con signo contrario: el lazo sigue fielmente tanto la referencia como el ruido, por eso se filtra (C14).
- *Descripción textual:* la referencia `r` entra a un sumador que resta la medida; el error `e` alimenta al controlador `C`; su salida se suma con la perturbación `d` y entra al cuerpo `G`; la salida `y` se mide, se le suma el ruido `n` y vuelve al primer sumador.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.
- 🔗 **Se estudia junto con:** diagrama de bloques, sumador, punto de bifurcación, lazo cerrado.

📘 **Dónde se aprende** (2 clases): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md); [B116-C02 · Signos vitales: medición, interpretación y límites](../programa/clases/B116/B116-C02-signos-vitales-medicion-interpretacion-y-limites/CLASE.md).

### Ruido de partículas

- El ruido de partículas es la fluctuación estadística.

💡 **Cómo se explica en la clase [B35-C05](../programa/clases/B35/B35-C05-simulacion-de-plasmas-por-particulas-pic/CLASE.md):**
- Con pocas partículas el ruido sube y la deriva de energía crece; el método no sustituye a los códigos de investigación.
- 🎯 **Por qué importa:** Un código sin validar produce figuras bonitas y físicas falsas. La decisión central: ¿reproduce el código la frecuencia y la tasa de crecimiento conocidas?
- 🔗 **Se estudia junto con:** macropartícula, ponderación CIC, salto de rana, deriva de energía.

📘 **Dónde se aprende** (1 clase): [B35-C05 · Simulación de plasmas por partículas (PIC)](../programa/clases/B35/B35-C05-simulacion-de-plasmas-por-particulas-pic/CLASE.md).

### Ruido de Poisson

- El ruido de lectura viene de la electrónica; el ruido de Poisson (de fotones), de la naturaleza discreta de la luz: su varianza es igual a la señal en electrones.
- El ruido de Poisson es la fluctuación de contar `n` objetos.
- El ruido de Poisson crece como la raíz de las cuentas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B35-C06](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md):**
- El ruido de Poisson se controla con más cuentas (`σ_V ∝ 1/√N`).
- El script [momentos.py](momentos.py) genera cuentas de Poisson y calcula momentos, ruido y sesgos (comprueba el ruido frente a `σ/√N` y el sesgo frente a la gaussiana truncada).
- ⚠️ **Error frecuente:** Ignorar el ruido de Poisson. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un momento sin su incertidumbre ni sus sesgos no es una medición. La decisión central: ¿cuántas cuentas hacen falta y qué sesgos introduce el instrumento?
- 🔗 **Se estudia junto con:** cuentas, momento, ventana, potencial de la nave.

📘 **Dónde se aprende** (4 clases): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B35-C06 · Mediciones in situ de plasmas espaciales](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md); [B36-C04 · Espectro de potencia de materia](../programa/clases/B36/B36-C04-espectro-de-potencia-de-materia/CLASE.md); [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md).

### Ruido de proceso

- El ruido de proceso `Q` modela lo que el modelo no sabe.
- El ruido de proceso viene de ARW y RRW (C06).

💡 **Cómo se explica en la clase [B74-C08](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md):**
- Con previa difusa y sin ruido de proceso, mínimos cuadrados recursivos y el ajuste por lotes coinciden con diferencia máxima `1,78e-10`.
- Distinguir ruido de medida `R` de ruido de proceso `Q`.
- 🎯 **Por qué importa:** Una nave en vuelo recibe medidas continuamente y necesita su estado ahora. La decisión central: ¿cuándo es el filtro equivalente al ajuste por lotes, qué añade el ruido de proceso y cómo evito que una previa errónea domine?
- 🔗 **Se estudia junto con:** predicción, corrección, ganancia de Kalman, innovación.

📘 **Dónde se aprende** (2 clases): [B74-C08 · Filtrado recursivo de estados](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md); [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md).

### Ruido del integrador

- El ruido del integrador es la diferencia entre dos ejecuciones con tolerancias muy distintas.

💡 **Cómo se explica en la clase [B23-C06](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md):**
- Esa diferencia es el ruido del integrador.
- Fijar la tolerancia de cada relación desde el ruido del integrador.
- 🎯 **Por qué importa:** El movimiento de un satélite con achatamiento terrestre (J2) no tiene solución cerrada, y tu código no tiene un valor correcto con el que compararse.
- 🔗 **Se estudia junto con:** relación metamórfica, entrada seguida, entrada base, simetría.

📘 **Dónde se aprende** (1 clase): [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md).

### Ruido inyectado

- El ruido inyectado por la banda.

💡 **Cómo se explica en la clase [B51-C14](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md):**
- Predecir el ruido inyectado `S_obj σ rms(1/B)/(S_cal √n)`.
- Ejercicio 2 · con una pista. Ruido inyectado con `B = 1`, `S_obj = 0,5`.
- 🎯 **Por qué importa:** Una línea débil sobre un continuo brillante solo se ve si la banda está calibrada mejor que la razón línea/continuo. La decisión central: ¿cuánto ruido inyecta la solución de banda y por qué no basta con restar un polinomio?
- 🔗 **Se estudia junto con:** solución de banda, calibrador de banda, sustracción del continuo, canales libres de línea.

📘 **Dónde se aprende** (1 clase): [B51-C14 · Calibración de banda en la reducción de datos de síntesis](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md).

### Ruido kTC

- El ruido kTC es el ruido térmico de la carga al reiniciar un condensador, `√(k_B T C)/e`.

💡 **Cómo se explica en la clase [B44-C03](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md):**
- Sin CDS el ruido es `40,24 e⁻` (esperado `40,22`); con CDS, `2,85 e⁻` (esperado `√2 × 2 = 2,83`).
- R["reinicio con ruido kTC"] --> L1["lectura de reinicio"]
- ⚠️ **Error frecuente:** Pensar que el CDS elimina todo el ruido. Se corrige con 8.2.
- 🎯 **Por qué importa:** El diseño CMOS cambia el ruido y la geometría de la lectura. La decisión central: ¿qué ruido elimina el CDS y qué artefacto introduce el obturador rodante?
- 🔗 **Se estudia junto con:** CDS, obturador rodante, lectura por columna.

📘 **Dónde se aprende** (1 clase): [B44-C03 · Sensores CMOS](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md).

### Ruido rms

- El ruido rms `ΔT_rms` es la fluctuación de la medida tras integrar.

💡 **Cómo se explica en la clase [B118-C17](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md):**
- `pfd = EIRP/(4π d²) = 7,958 × 10⁻²¹ W m⁻² Hz⁻¹ = 7,958 × 10⁵ Jy` a 1000 km: unos 10⁸ veces el ruido.
- Paso 1 · Ruido. `25/√(10⁶ × 3600) = 0,417 mK`.
- ⚠️ **Error frecuente:** Esperar que más integración elimine una interferencia constante. Se corrige con 8.1: reduce el ruido, no la señal de interferencia.
- 🎯 **Por qué importa:** La radioastronomía opera en bandas donde la ITU asigna protección, pero las constelaciones numerosas y sus emisiones no deseadas pueden degradar la sensibilidad. La decisión central: ¿cuánto debe bajar una emisión para quedar por debajo del umbral de daño y de qué depende ese umbral?
- 🔗 **Se estudia junto con:** densidad de flujo, densidad de flujo de potencia, EIRP espectral, lóbulo lateral.

📘 **Dónde se aprende** (1 clase): [B118-C17 · Interferencia radioastronómica](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md).

### Ruido rojo

- El ruido coloreado es cualquier ruido con memoria; el ruido rojo concentra su potencia en las frecuencias bajas.

💡 **Cómo se explica en la clase [B15-C03](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md):**
- El ruido rojo es el vaivén de un tren sobre una vía irregular: cada movimiento depende del anterior.
- Paso 6 · Lectura. El mismo promedio es 9 a 10 veces menos preciso con ruido rojo.
- 🎯 **Por qué importa:** Una regla heredada de la física del laboratorio dice que, al promediar `N` mediciones, el error baja como `1/√N`. Esa regla solo vale si los errores de cada medición son independientes.
- 🔗 **Se estudia junto con:** ruido blanco, AR(1), paseo aleatorio, ruido coloreado.

📘 **Dónde se aprende** (1 clase): [B15-C03 · Ruido blanco y coloreado](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md).

### Ruina

- La ruina es una pérdida mayor que primas más capital.

💡 **Cómo se explica en la clase [B124-C08](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md):**
- *Descripción textual:* la probabilidad de falla da la pérdida esperada y la prima; la cola de pérdidas, agravada por las fallas en grupo, da la probabilidad de ruina, que se comprueba con una simulación.
- El ejemplo conductor es una cartera sintética de 20 satélites con prima total de `324,0` um y una probabilidad de ruina de `0,0439`; si los satélites vuelan de a 4 por cohete, esa probabilidad es `0,1846`.
- 🎯 **Por qué importa:** El seguro no elimina el riesgo: lo traslada a quien puede juntarlo. La decisión central: ¿cuánto cobrar por cubrir un riesgo y con qué probabilidad el asegurador se queda sin capital?
- 🔗 **Se estudia junto con:** prima, pérdida esperada, recargo, capital.

📘 **Dónde se aprende** (1 clase): [B124-C08 · Seguros y riesgo espacial](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md).

### RUL

- La RUL `= t_cruce − t_actual`.

💡 **Cómo se explica en la clase [B88-C44](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md):**
- *Descripción textual:* la serie se ajusta con un modelo exponencial; el cruce del umbral da la RUL; el remuestreo da su intervalo y la política decide si alertar.
- El ajuste da `a = 1,9958`, `b = 0,000601 /h`; la RUL estimada es `88,1` días (real `88,2`); el intervalo de remuestreo 95 % es `[86,5; 89,6]` días.
- 🎯 **Por qué importa:** Detectar una falla (C12) llega tarde para planificar; anticiparla da tiempo para actuar. La decisión central: ¿cuándo cruzará el umbral y con qué incertidumbre, para decidir si alertar?
- 🔗 **Se estudia junto con:** ajuste, cruce, remuestreo, política de alerta.

📘 **Dónde se aprende** (1 clase): [B88-C44 · Mantenimiento predictivo y pronóstico de salud de sistemas](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md).

### Runge–Kutta de cuarto orden (RK4)

- Euler explícito: `q + h q̇`. Runge–Kutta de cuarto orden (RK4): combina cuatro evaluaciones de `q̇` por paso.

💡 **Contexto en la clase [B10-C20](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md):**
- **Idea central (modelo mental):** Integrar es componer miles de rotaciones pequeñas: en cada paso, el cuaternión se multiplica por el de un giro de ángulo `|ω| h` alrededor de `ω`.
- 🎯 **Por qué importa:** Los giróscopos de un satélite miden la velocidad angular en ejes del cuerpo. Para saber hacia dónde apunta una cámara, hay que integrar esa velocidad en el tiempo, miles de veces.
- 🔗 **Se estudia junto con:** ecuación cinemática del cuaternión, constante, método de un paso, Euler explícito.

📘 **Dónde se aprende** (1 clase): [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md).

### Ruptura

- Adsorción: retención en la superficie de un sólido. Ruptura: momento en que el lecho deja pasar el contaminante.

💡 **Cómo se explica en la clase [B106-C21](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md):**
- Usar el modelo de Yoon–Nelson para el tiempo al 10 % y 90 % de ruptura.
- La concentración a la salida (ruptura) y la caída de presión; en el modelo, el 10 % de `C₀`.
- 🎯 **Por qué importa:** Una cabina cerrada acumula trazas que no son CO₂ ni agua; hay que retirarlas con lechos y catalizadores que se saturan o dependen de la temperatura. La decisión central: ¿cuánto dura un lecho, a qué temperatura debe operar el catalizador y qué concentración queda en la cabina?
- 🔗 **Se estudia junto con:** Traza, Adsorción, Yoon–Nelson, Oxidador catalítico.

📘 **Dónde se aprende** (1 clase): [B106-C21 · Depuración de trazas gaseosas de la atmósfera de cabina](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md).

### Ruta

- Una ruta (*path*) es la dirección de un archivo o carpeta.
- Una ruta es su dirección.

💡 **Cómo se explica en la clase [B07-C15](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md):**
- Ejemplo real de esta clase, en la carpeta C15 de un equipo Windows: bash mostró una ruta con barras `/c/dev/.../B07-C15-terminal-y-rutas-de-archivos` y PowerShell, la misma carpeta como `C:\dev\...\B07-C15-terminal-y-rutas-de-archivos`.
- Las comillas protegen espacios en rutas: `cd "Mis datos"`.
- ⚠️ **Error frecuente:** Ruta absoluta fija. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Una causa muy común de «el programa no encuentra el archivo» es que la ruta funciona en el computador del autor y no en otro: se escribió con `C:\Usuarios\ana\datos\...`, o se asumió que el programa se ejecuta desde cierta carpeta.
- 🔗 **Se estudia junto con:** terminal, intérprete de comandos, directorio de trabajo, absoluta.

📘 **Dónde se aprende** (2 clases): [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md); [B14-C31 · APIs de servicios de datos](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md).

### Ruta alternativa

- La ruta alternativa es otra que no comparte pasillos con la principal.

💡 **Cómo se explica en la clase [B114-C01](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md):**
- Comprobar la existencia de una ruta alternativa que no comparte pasillos.
- No tiene ruta alternativa: es un punto único de fallo que debe señalarse en el análisis.
- ⚠️ **Error frecuente:** Suponer que una salida basta sin ruta alternativa. Se corrige con 8.3.
- 🎯 **Por qué importa:** Una salida existe en el plano, pero la evacuación depende de cuánto se tarda en llegar a ella y de qué pasa si el camino principal queda bloqueado. La decisión central: ¿cuánto tarda en salir toda la tripulación y qué ruta queda si falla la principal?
- 🔗 **Se estudia junto con:** ruta de evacuación, camino mínimo, flujo de puerta, cuello de botella.

📘 **Dónde se aprende** (1 clase): [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md).

### Ruta crítica

- La ruta crítica es el camino de mayor duración; la holgura es el margen de una actividad fuera de ella.
- La ruta crítica es el camino de mayor duración.
- La ruta crítica es la cadena de pasos que fija la fecha más temprana posible.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B83-C06](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md):**
- *Descripción textual:* la función de misión se divide en hijas; sus dependencias dan la ruta crítica y las holguras, y su asignación a subsistemas da los flujos cruzados, que se convertirán en interfaces.
- La secuencia de una toma dura 655 s por la ruta crítica; las funciones de comando (F1) y calentamiento del detector (F4) tienen 88 s de holgura.
- 🎯 **Por qué importa:** Si se salta a las piezas demasiado pronto, se diseñan cosas que nadie sabe para qué sirven; si se descompone bien, se ve qué función domina el tiempo y dónde se acoplan los subsistemas. La decisión central: ¿qué funciones son críticas para el tiempo y qué subsistemas quedan más acoplados?
- 🔗 **Se estudia junto con:** función, descomposición funcional, diagrama de flujo funcional, holgura.

📘 **Dónde se aprende** (5 clases): [B83-C06 · Descomposición funcional](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md); [B90-C01 · Plan de ensamblaje e integración](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md); [B97-C13 · Ensamblaje de estructuras en órbita](../programa/clases/B97/B97-C13-ensamblaje-de-estructuras-en-orbita/CLASE.md); [B120-C06 · Caso de planificación regulatoria de un sistema satelital](../programa/clases/B120/B120-C06-caso-de-planificacion-regulatoria-de-un-sistema-satelital/CLASE.md); [B124-C16 · Planificación de cronograma y entregables](../programa/clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md).

### Ruta de evacuación

- La ruta de evacuación es el camino desde un módulo hasta una salida.

💡 **Cómo se explica en la clase [B114-C01](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *plano de evacuación sintético con tiempos*: grafo, tabla de tiempos por módulo, rutas alternativas, tiempo de cola y lista de qué es sintético y qué no se consultó.
- El script [evacuacion.py](evacuacion.py) calcula el camino mínimo con Dijkstra, lo verifica por enumeración, busca rutas alternativas y estima la cola (comprueba diferencia < 1e-9 m y que repartir en dos salidas reduce la cola).
- 🎯 **Por qué importa:** Una salida existe en el plano, pero la evacuación depende de cuánto se tarda en llegar a ella y de qué pasa si el camino principal queda bloqueado. La decisión central: ¿cuánto tarda en salir toda la tripulación y qué ruta queda si falla la principal?
- 🔗 **Se estudia junto con:** ruta alternativa, camino mínimo, flujo de puerta, cuello de botella.

📘 **Dónde se aprende** (1 clase): [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md).

### Ruta de mínima energía

- La ruta de mínima energía minimiza la suma de energías de las aristas, no la distancia.

💡 **Cómo se explica en la clase [B100-C05](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md):**
- Luna: la ruta de mínima energía cuesta `0,3597 kWh`; la de mínima distancia (`2162,6 m`) cuesta `0,3679 kWh`, un `2,28 %` más.
- *Descripción textual:* la gravedad, la masa y la pendiente de cada arista dan su fuerza y su energía; con esos costos, Dijkstra y Bellman–Ford encuentran la ruta de mínima energía y se comparan entre sí.
- 🎯 **Por qué importa:** Mover una tonelada un kilómetro cuesta energía, y esa energía depende de la gravedad, del suelo y de la pendiente. La decisión central: ¿cuánta carga y qué ruta permiten llegar con la batería disponible, y cuánto cambia el costo entre la Luna y Marte?
- 🔗 **Se estudia junto con:** resistencia a la rodadura, fuerza de pendiente, fuerza de avance, energía.

📘 **Dónde se aprende** (1 clase): [B100-C05 · Transporte de carga sobre superficie planetaria](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md).

### Ruta de mínimo coste

- La ruta de mínimo coste se obtiene con el algoritmo de Dijkstra.

💡 **Cómo se explica en la clase [B102-C08](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md):**
- *Descripción textual:* las elevaciones dan la pendiente y, con el plano local, la altura de obstáculo y la rugosidad; los tres forman el coste de celda y Dijkstra obtiene la ruta de mínimo coste.
- La ruta de mínimo coste entre dos puntos a `99,0 m` mide `122,4 m`, con una pendiente máxima de `18,83°`.
- 🎯 **Por qué importa:** Elegir la ruta es elegir qué riesgo se acepta. La decisión central: ¿qué celdas son intransitables, cuánto cuesta cruzar las demás y cuánto se alarga la ruta de mínimo riesgo respecto de la recta?
- 🔗 **Se estudia junto con:** pendiente, altura de obstáculo, rugosidad, coste de celda.

📘 **Dónde se aprende** (1 clase): [B102-C08 · Traversabilidad y evaluación de riesgo de terreno](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md).

### Ruze

- La ganancia es `G = η e^{−(4πσ/λ)²} (πD/λ)²`. Ruze es el factor `e^{−(4πσ/λ)²}` de pérdida por error de superficie rms `σ`.

💡 **Cómo se explica en la clase [B89-C06](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md):**
- S["sigma rms"] --> RZ["Ruze = exp(-(4 pi sigma / lambda)^2)"]
- *Descripción textual:* la ganancia ideal se corrige con Ruze y con la pérdida por apuntamiento, que depende del ancho de haz.
- 🎯 **Por qué importa:** Una antena mal apuntada o con la superficie deformada pierde decibelios que ningún amplificador recupera, y esas pérdidas crecen con la frecuencia. La decisión central: ¿qué ganancia efectiva da una antena y a qué frecuencia deja de compensar subir la frecuencia?
- 🔗 **Se estudia junto con:** ganancia, ancho de haz, pérdida por apuntamiento, frecuencia óptima.

📘 **Dónde se aprende** (1 clase): [B89-C06 · Ganancias y pérdidas de antena](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md).
