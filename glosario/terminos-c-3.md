# Términos · C (parte 3 de 4)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · **C** · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-c.md) · [2](terminos-c-2.md) · **3** · [4](terminos-c-4.md)

### Conjunto de referencia

- Un conjunto de referencia (o *dataset* oficial) es un dato publicado con procedencia, versión y marco que se toma como patrón.

🎯 **Por qué importa (clase B23-C05):** Un modelo kepleriano de la Tierra pasó todas las pruebas de C01–C04, pero eso no dice nada sobre si la Tierra se mueve como una elipse perfecta. La pregunta motivadora es: ¿contra qué contrasto mi modelo, y qué diferencia estoy dispuesto a aceptar?

📘 **Dónde se aprende** (1 clase): [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md).

### Conjunto mínimo de corte

- Un conjunto mínimo de corte no tiene subconjunto que también cause el tope.

💡 **Cómo se explica en la clase [B88-C16](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md):**
- Los conjuntos mínimos de corte son `{C}`, `{A, B}` y `{D, E}`.
- Conjuntos minimos de corte: [['C'], ['A', 'B'], ['D', 'E']]
- 🎯 **Por qué importa:** Una nave tolera fallos si ninguno solo provoca la pérdida y las combinaciones peligrosas son improbables. La decisión central: ¿qué combinaciones mínimas de fallos causan la pérdida y cuál elemento merece más protección?

📘 **Dónde se aprende** (1 clase): [B88-C16 · Ingeniería de seguridad funcional](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md).

### Conjunto ponderado

- El conjunto ponderado aproxima la distribución del estado.

🎯 **Por qué importa (clase B15-C18):** Un sensor mide la distancia oblicua a un objeto que pasa junto a él. Cuando el objeto está justo frente al sensor, un pequeño cambio de posición casi no cambia la distancia: la medida no distingue bien un lado del otro, y la incertidumbre de la posición deja de ser una campana.

📘 **Dónde se aprende** (1 clase): [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md).

### Conmutación

- Las pérdidas de conducción son `R I²`; las de conmutación son `½ V I (t_r + t_f) f`.

💡 **Cómo se explica en la clase [B86-C08](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md):**
- Por pérdidas: conducción, diodo, conmutación.
- Simular la conmutación y comparar el rizado y la tensión media con las fórmulas.
- 🎯 **Por qué importa:** Un convertidor que reduce la tensión con un interruptor y una bobina puede ser mucho más eficiente que un regulador lineal, pero introduce rizado, ruido y pérdidas de conmutación que hay que dimensionar. La decisión central: ¿qué ciclo de trabajo, bobina y condensador dan `5 V` desde `28 V` con rizado y eficiencia aceptables?

📘 **Dónde se aprende** (1 clase): [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### Conmutación de Dicke

- La conmutación de Dicke alterna fuente y referencia.

💡 **Cómo se explica en la clase [B46-C06](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md):**
- Explicar la penalización de la conmutación de Dicke.
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué se conmuta con Dicke?
- 🎯 **Por qué importa:** La señal de una fuente astronómica es mucho menor que el ruido, y solo el promedio la hace visible. La decisión central: ¿cuánto tiempo y ancho de banda se necesitan para alcanzar una sensibilidad dada?

📘 **Dónde se aprende** (1 clase): [B46-C06 · Ruido de sistema y radiometría](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md).

### Conmutación en posición

- La conmutación en posición ON/OFF.

🎯 **Por qué importa (clase B46-C20):** Un proyecto viable cuadra objetivo, sensibilidad, tiempo y datos. La decisión central: ¿cuánto tiempo de observación pide el objetivo y con qué margen?

📘 **Dónde se aprende** (1 clase): [B46-C20 · Proyecto de observación radioastronómica](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md).

### Conmutación tipo Dicke

- La conmutación tipo Dicke alterna cielo y referencia.

🎯 **Por qué importa (clase B49-C08):** Integrar más tiempo no siempre mejora la medida: la deriva lo impide. La decisión central: ¿hasta qué tiempo de integración vale la pena, y cuándo hay que conmutar?

📘 **Dónde se aprende** (1 clase): [B49-C08 · Estabilidad de ganancia de receptores y variaciones de ganancia](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md).

### Cono de emisión

- El cono de emisión tiene semiángulo `1/γ`.

💡 **Cómo se explica en la clase [B27-C11](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md):**
- Ejercicio 6. Semiángulo del cono de emisión para `γ = 30`.
- 🎯 **Por qué importa:** Un chorro que se acerca puede parecer más rápido que la luz sin violar nada, y su brillo cambia en órdenes de magnitud según el ángulo. Sin estos efectos no se pueden comparar chorros ni inferir su velocidad.

📘 **Dónde se aprende** (1 clase): [B27-C11 · Chorros relativistas](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md).

### Cono de luz

- El cono de luz de un evento es el conjunto de eventos a intervalo nulo; separa el futuro, el pasado y el «en otra parte».

💡 **Cómo se explica en la clase [B26-C04](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md):**
- Un evento puede influir en otro solo si el segundo está en su cono futuro (o sobre él).
- Cada punto del mapa tiene un cono de luz dibujado: dentro del cono hacia arriba está su futuro, dentro hacia abajo su pasado; fuera, sus eventos inalcanzables.
- 🎯 **Por qué importa:** Comunicar con una sonda, sincronizar relojes de dos estaciones o decidir si un evento puede haber causado otro exige saber cuándo dos sucesos están conectados por una señal. El intervalo lo decide para todos los observadores.

📘 **Dónde se aprende** (1 clase): [B26-C04 · Espacio-tiempo de Minkowski](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md).

### Cono de orientación

- El cono de orientación limita `|δ|`.

💡 **Cómo se explica en la clase [B81-C06](../programa/clases/B81/B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md):**
- Aplicar un cono de orientación `|δ| ≤ δ_max`.
- El script [orientacion.py](orientacion.py) calcula `E(ψ, δ)`, el óptimo analítico y por rejilla, el efecto de un cono de orientación y el tiempo de misión (comprueba que la rejilla coincida con el analítico a 1e-6 y `E(30°, 0) = 0,5`).
- 🎯 **Por qué importa:** Una trayectoria óptima en el vacío no es necesariamente volable: el guiado debe respetar la orientación de los paneles. La decisión central: ¿cuánto conviene desviar el empuje de la dirección óptima para recuperar potencia, y dentro de qué cono?

📘 **Dónde se aprende** (1 clase): [B81-C06 · Restricciones de orientación del empuje](../programa/clases/B81/B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md).

### Cono de pérdida

- El cono de pérdida es el rango de `α_eq` con espejo bajo la atmósfera.

💡 **Cómo se explica en la clase [B30-C16](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md):**
- En `L = 4` la línea toca la atmósfera (100 km) en `λ = 59,74°`, donde `B = 53 585 nT`; el cono de pérdida es `α_LC = 5,47°`.
- A --> LC["cono de pérdida en la atmósfera"]
- 🎯 **Por qué importa:** Las partículas con ángulo de paso pequeño se pierden en la atmósfera; las demás quedan atrapadas y dañan satélites. La decisión central: ¿qué partículas quedan atrapadas y con qué periodo rebotan?

📘 **Dónde se aprende** (1 clase): [B30-C16 · Cinturones de Van Allen](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md).

### Conocimiento tradicional

- El conocimiento tradicional es el saber transmitido por una comunidad.

💡 **Cómo se explica en la clase [B02-C20](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md):**
- La iniciativa UNESCO–IAU, lanzada en 2003 como actividad de prueba inicial, vincula ciencia y cultura para reconocer sitios relacionados con la astronomía, incluido el «conocimiento comunitario tradicional»; la IAU participa desde un acuerdo con la UNESCO en 2008.
- 🎯 **Por qué importa:** Los sitios, instrumentos, archivos, saberes y hasta la oscuridad del cielo son patrimonio, y los telescopios, el turismo y las constelaciones de satélites pueden dañarlo. La pregunta motivadora es: ¿qué debo preguntar, a quién y antes de qué, cuando mi trabajo toca un cielo o un lugar que importa a otras personas?

📘 **Dónde se aprende** (1 clase): [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md).

### CONOPS

- Un CONOPS describe fases, modos, actores y escenarios de operación.
- ConOps: descripción de cómo se opera la misión.

💡 **Cómo se explica en la clase [B83-C03](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md):**
- El CONOPS de ejemplo tiene cuatro fases: lanzamiento y primeras órbitas (7 d), puesta en servicio (30 d), operaciones nominales (3 años) y fin de vida (90 d).
- *Descripción textual:* las fases y modos del CONOPS definen la órbita y la estación; la simulación de visibilidad da pases, duraciones y huecos, de los que sale el tiempo de enlace diario; la cota analítica del pase cenital sirve de comprobación.
- ⚠️ **Error frecuente:** Escribir un CONOPS sin números. Añade pases, huecos y latencias
- 🎯 **Por qué importa:** Los requisitos de datos, energía y operaciones dependen de cuántas veces al día se puede hablar con el satélite y por cuánto tiempo. La decisión central: ¿cuánto contacto real ofrece la órbita y cómo se reparte en las fases de la misión?

📘 **Dónde se aprende** (2 clases): [B83-C03 · Concepto de operaciones CONOPS](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md); [B96-C02 · Concepto de operaciones de misión](../programa/clases/B96/B96-C02-concepto-de-operaciones-de-mision/CLASE.md).

### Consejo

- El consejo es el órgano que dirige la empresa.

💡 **Cómo se explica en la clase [B125-C03](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md):**
- Consejo sintético con pesos `[3, 2, 1, 1, 1, 1, 1]` y cuota `6` de `10`.
- Descripción larga: con 20 votos por acción, menos del 5 % de las acciones da la mitad del voto; en un consejo ponderado el poder real se aparta del peso nominal, y un peso dominante lo concentra todo.
- 🎯 **Por qué importa:** Las decisiones de una empresa se estructuran en su gobierno y, en el espacio, el capital intensivo hace que quien controla la votación controle el rumbo de misiones de años; ninguna clase lo trata.

📘 **Dónde se aprende** (1 clase): [B125-C03 · Gobierno corporativo de una empresa espacial](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md).

### Consenso

- El consenso exige que nadie bloquee.

💡 **Cómo se explica en la clase [B119-C06](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md):**
- El detalle del reglamento y las decisiones por consenso no se consultaron.
- Para consenso con probabilidad al menos 0,5: `p ≤ 0.03778` con 18 miembros y `p ≤ 0.00691` con 100.
- ⚠️ **Error frecuente:** Creer que consenso es unanimidad de votos. Se corrige con el vocabulario.
- 🎯 **Por qué importa:** Quien estudia el derecho espacial necesita saber dónde se negocia y cómo se decide; ninguna clase anterior trata los organismos. La decisión central: ¿cómo cambia la probabilidad de bloqueo cuando crece el número de miembros que deben consentir?

📘 **Dónde se aprende** (1 clase): [B119-C06 · Organismos UNOOSA y COPUOS](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md).

### Consentimiento libre, previo e informado

- El consentimiento libre, previo e informado es el derecho de un pueblo a decidir, antes de un proyecto y con información suficiente, si acepta que afecte su territorio o su conocimiento (S3).
- El consentimiento libre, previo e informado es la aceptación sin coacción, antes de empezar y con información suficiente.
- El consentimiento libre, previo e informado (CLPI) exige obtener el acuerdo de un pueblo antes de un proyecto que afecte sus tierras o territorios, sin coerción y con información suficiente (S2).

💡 **Cómo se explica en la clase [B02-C06](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md):**
- Reconocer las preguntas de consentimiento libre, previo e informado.
- 🎯 **Por qué importa:** Chile alberga algunos de los cielos más oscuros del mundo y los más grandes observatorios, y también pueblos que miraron esos cielos durante milenios. La pregunta motivadora es: ¿cómo hablar de saberes celestes de pueblos vivos sin generalizar, sin apropiarse y sin presentar como establecido lo que no hemos podido verificar?

📘 **Dónde se aprende** (3 clases): [B02-C06 · Astronomía de pueblos originarios de Chile](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md); [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md); [B133-C03 · Colaboración con comunidades en investigación y educación](../programa/clases/B133/B133-C03-colaboracion-con-comunidades-en-investigacion-y-educacion/CLASE.md).

### Conserva

- La energía mecánica `E = E_c + E_p` se conserva si solo actúan fuerzas conservativas, o si las demás no hacen trabajo.
- Un sobrevuelo lo conserva (en el límite de cónicas empalmadas con planeta en órbita circular).

💡 **Cómo se explica en la clase [B05-C07](../programa/clases/B05/B05-C07-conservacion-de-energia-mecanica/CLASE.md):**
- Paso 4 · Sentido físico. Con `g` constante saldrían 1275 km: la conservación con `E_p = −GM/r` es más fiel.
- En esta clase calcularás ambos valores con conservación de energía y los compararás con los publicados.
- ⚠️ **Error frecuente:** Aplicar conservación con fuerzas no conservativas. Ejercicios 8 y 11.
- 🎯 **Por qué importa:** Si lanzas algo hacia arriba, ¿hasta dónde sube? ¿Con qué rapidez hay que lanzarlo para que no vuelva?

📘 **Dónde se aprende** (2 clases): [B05-C07 · Conservación de energía mecánica](../programa/clases/B05/B05-C07-conservacion-de-energia-mecanica/CLASE.md); [B75-C08 · Secuencias múltiples de sobrevuelos](../programa/clases/B75/B75-C08-secuencias-multiples-de-sobrevuelos/CLASE.md).

### Conserva el volumen

- Es reversible y conserva el volumen, pero no exactamente la energía: su error de energía `ΔH` escala como `ε²`.

🎯 **Por qué importa (clase B19-C03):** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.

📘 **Dónde se aprende** (1 clase): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md).

### Conservación

- La conservación es `∇_a T^ab = 0`.
- La conservación de la corriente.
- La conservación exige que cada columna de `M` sume cero.

💡 **Cómo se explica en la clase [B33-C07](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de la red eléctrica*: matriz, corrientes y conservación.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de la red eléctrica*: matriz, corrientes y conservación.
- ⚠️ **Error frecuente:** Ignorar la conservación. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una subestación con una corriente de tierra alta puede saturar un transformador. La decisión central: ¿cómo se reparte la corriente inducida entre las subestaciones?

📘 **Dónde se aprende** (3 clases): [B33-C07 · Impactos del clima espacial en redes eléctricas](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md); [B39-C04 · Tensor de energía-momento y fuentes de curvatura](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md); [B55-C20 · Modelo simplificado de red astroquímica](../programa/clases/B55/B55-C20-modelo-simplificado-de-red-astroquimica/CLASE.md).

### Conservación de la masa

- La conservación de la masa limita el modelo.

🎯 **Por qué importa (clase B118-C09):** La directriz 5 de la COPUOS dice que la mayor parte de los desechos catalogados proviene de fragmentaciones; entender cuántos fragmentos produce un evento y de qué tamaño es la base de los escenarios futuros. La decisión central: ¿cuántos fragmentos relevantes genera un evento y cuándo es «catastrófico»?

📘 **Dónde se aprende** (1 clase): [B118-C09 · Generación de desechos](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md).

### Conservación de los átomos

- La conservación de los átomos y de la carga son las condiciones que exigimos a una ecuación balanceada.

💡 **Cómo se explica en la clase [B06-C08](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md):**
- La analogía de las piezas muestra que se conserva el número de átomos; su límite es que no explica la energía: en una reacción química se libera o absorbe, aunque la masa casi no cambie.
- 🎯 **Por qué importa:** Una vela y el Sol liberan energía, pero lo hacen de maneras radicalmente distintas. En la vela, los átomos de carbono e hidrógeno se reordenan con el oxígeno y todos siguen ahí al terminar.

📘 **Dónde se aprende** (1 clase): [B06-C08 · Reacciones y conservación de masa](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md).

### Conservación del flujo

- La conservación del flujo relaciona campo y sección.

💡 **Cómo se explica en la clase [B30-C05](../programa/clases/B30/B30-C05-campos-magneticos-solares/CLASE.md):**
- *Descripción textual:* la densidad, la temperatura y el campo dan las presiones y el beta; el campo y la densidad dan la velocidad de Alfvén; el campo se rige además por la conservación del flujo.
- Aplicar la conservación del flujo `B₁A₁ = B₂A₂`.
- 🎯 **Por qué importa:** Que el gas domine al campo en la fotosfera y el campo al gas en la corona explica por qué la corona se estructura en lazos y por qué las erupciones liberan energía magnética. La decisión central: ¿en qué capa manda el campo y cuánta energía guarda?

📘 **Dónde se aprende** (2 clases): [B30-C05 · Campos magnéticos solares](../programa/clases/B30/B30-C05-campos-magneticos-solares/CLASE.md); [B34-C03 · Bucles magnéticos coronales](../programa/clases/B34/B34-C03-bucles-magneticos-coronales/CLASE.md).

### Conservación del momento

- Impulso: `F·t`. Conservación del momento: la suma `Σ m v` no cambia sin fuerzas externas.

💡 **Cómo se explica en la clase [B106-C16](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md):**
- Aplicar la conservación del momento lineal a un empujón entre astronauta y carga.
- Comprobar la conservación del momento total.
- 🎯 **Por qué importa:** Sin peso ni fricción, toda fuerza tiene una reacción que mueve al operario o a la carga; un diseño de herramientas y de superficies que lo ignore produce maniobras inseguras. La decisión central: ¿qué sujeciones y qué límites de par o de empuje evitan que la reacción mueva al astronauta fuera de la tarea?

📘 **Dónde se aprende** (1 clase): [B106-C16 · Ergonomía en microgravedad](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md).

### Conservador

- Optimista significa covarianza menor que el error real; conservador, mayor.

💡 **Cómo se explica en la clase [B74-C23](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md):**
- El conservador (`q` diez veces mayor) tiene NEES `1,132`, por debajo del límite inferior, y NIS `0,865`.
- L --> V["consistente / optimista / conservador"]
- 🎯 **Por qué importa:** Un filtro optimista presenta covarianzas pequeñas y errores grandes, y no avisa. La decisión central: ¿cómo sé, con una prueba estadística, si mi filtro es consistente y qué estadístico me avisa de qué fallo?

📘 **Dónde se aprende** (1 clase): [B74-C23 · Consistencia de filtros: innovaciones y pruebas NEES/NIS](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md).

### Conservan

- La energía específica (por unidad de masa) es `E = v²/2 − GM/r` y el momento angular específico, `L = x·vy − y·vx`; ambos se conservan en un campo central.

💡 **Cómo se explica en la clase [B07-C20](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md):**
- (3) Runge-Kutta de orden 4 y los métodos con paso adaptativo: más precisión por paso, pero tampoco conservan la energía exactamente; se estudian en B11 y no se consultaron.
- Ejercicio 8. ¿Qué dos cantidades se conservan en un campo central y cómo se comprueba con el simulador?
- 🎯 **Por qué importa:** Un simulador es la forma de explorar un fenómeno cuya solución no tienes a mano, y de comprobar que entiendes uno cuya solución sí conoces. Aquí conoces la respuesta (una órbita circular se repite con un período dado por una fórmula), así que puedes verificar el simulador antes de confiar en él para casos que no conoces.

📘 **Dónde se aprende** (1 clase): [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md).

### Conservativa

- Una fuerza conservativa es aquella cuyo trabajo no depende del camino, solo de los extremos (la gravedad lo es).

🎯 **Por qué importa (clase B05-C06):** Poner 1000 kg en órbita cuesta mucho más que subirlos 400 km. La pregunta motivadora es: ¿cuánta energía hay que entregar para cambiar el estado de un cuerpo, y en qué se convierte?

📘 **Dónde se aprende** (1 clase): [B05-C06 · Trabajo y energía](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md).

### Conservativo

- Un campo es conservativo si `F = ∇f`; entonces `∫_C F·dr = f(B) − f(A)` (ec. 1.6.42) y `∇×F = 0`.

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- Para la gravedad, el rotacional es cero (laboratorio: `< 10⁻¹⁵ s⁻²`): el campo es conservativo.
- Por potencial cuando el campo es conservativo: basta evaluar en los extremos.
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.

📘 **Dónde se aprende** (1 clase): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md).

### Consistencia

- La consistencia es que el error de truncamiento tienda a cero; la estabilidad, que los errores no crezcan.
- La consistencia significa que `P_declarada − P_real` es semidefinida positiva.
- La consistencia (protocolo de Wald) exige que, al degradar la imagen fusionada a la resolución original, se recupere la multiespectral.

💡 **Cómo se explica en la clase [B15-C24](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md):**
- La consistencia garantiza que la fusión no altera los colores promediados a la resolución original;
- Para el NIR, cuyo detalle es independiente de la pancromática, la fusión empeora el error de 0,0249 a 0,0341: el detalle inyectado es falso, aunque la consistencia sea perfecta.
- ⚠️ **Error frecuente:** Creer que la consistencia garantiza que el detalle es correcto. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Un mapa de cobertura exige distinguir objetos pequeños (caminos, parcelas) y también su firma espectral (si son vegetación o suelo). Ninguna imagen entrega ambas cosas a la vez.

📘 **Dónde se aprende** (3 clases): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md); [B15-C24 · Fusión de imágenes de distintos sensores](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md); [B80-C08 · Filtrado distribuido y descentralizado](../programa/clases/B80/B80-C08-filtrado-distribuido-y-descentralizado/CLASE.md).

### Consistencia física

- La consistencia física de un modelo es que sus dependencias respeten leyes o restricciones conocidas (exponentes, monotonía, signos, unidades).

💡 **Cómo se explica en la clase [B17-C08](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md):**
- *Descripción textual:* un modelo entrenado se somete a dos revisiones paralelas: la importancia por permutación (de qué depende, con atención a variables espurias y duplicadas) y la consistencia física (exponentes, monotonía y extrapolación).
- Las pruebas de consistencia física (exponentes, signos, monotonía, extrapolación) son las más cercanas a lo que un especialista exige, y se escriben como tests automáticos.
- 🎯 **Por qué importa:** Dos modelos pueden tener el mismo error en validación y haber aprendido cosas muy distintas: uno la ley física, otro un atajo que funciona en el rango visto. Si solo miras la métrica, no los distingues, y el atajo falla al primer dato fuera de rango.

📘 **Dónde se aprende** (1 clase): [B17-C08 · Interpretabilidad con consistencia física](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md).

### Consistente

- Un estimador es consistente si converge al valor verdadero al crecer `n`.
- Un filtro es consistente si su promedio está dentro de los límites de la `χ²`.

💡 **Cómo se explica en la clase [B74-C23](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md):**
- L --> V["consistente / optimista / conservador"]
- *Descripción textual:* el filtro produce errores con covarianza e innovaciones con su covarianza; los promedios de NEES y NIS sobre las simulaciones se comparan con los límites de la χ² para decidir si el filtro es consistente.
- 🎯 **Por qué importa:** Un filtro optimista presenta covarianzas pequeñas y errores grandes, y no avisa. La decisión central: ¿cómo sé, con una prueba estadística, si mi filtro es consistente y qué estadístico me avisa de qué fallo?

📘 **Dónde se aprende** (2 clases): [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md); [B74-C23 · Consistencia de filtros: innovaciones y pruebas NEES/NIS](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md).

### Constante

- Una constante es un valor que no cambia: exacta por definición (como `c = 299 792 458 m/s` en el SI, S4), medida (como `G`, con incertidumbre) o nominal (valor de conversión fijado por acuerdo, como el `(GM)☉` de la IAU).
- Una constante de `astropy.constants` es una cantidad con unidad, incertidumbre y referencia (S3).
- Para `ω` constante, la solución exacta es `q(t) = (cos(|ω| t/2), sin(|ω| t/2) ω/|ω|)` partiendo de la identidad.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C12](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md):**
- La constante de gravitación `G` no está fijada por el SI; se mide en laboratorio.
- Un símbolo se pregunta si cambia en el problema (variable); si no, si es propio del caso (parámetro) o universal (constante); y la constante universal se clasifica en exacta, medida o nominal.
- ⚠️ **Error frecuente:** Dar incertidumbre a una constante exacta. Ejercicio 7.
- 🎯 **Por qué importa:** La masa del Sol se conoce con unas cinco cifras. Sin embargo, el producto `GM` del Sol se conoce con diez, y la constante `G` por sí sola con apenas cinco.

📘 **Dónde se aprende** (4 clases): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B07-C11 · Gestión de unidades en programas](../programa/clases/B07/B07-C11-gestion-de-unidades-en-programas/CLASE.md); [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md); [B45-C13 · Temperatura y espectro de cuerpo negro](../programa/clases/B45/B45-C13-temperatura-y-espectro-de-cuerpo-negro/CLASE.md).

### Constante cónica

- La constante cónica `k` (0 esfera, −1 paraboloide).

🎯 **Por qué importa (clase B41-C04):** El espejo primario de un telescopio reflector es una superficie cónica. La decisión central: ¿por qué se usa un paraboloide y no una esfera?

📘 **Dónde se aprende** (2 clases): [B41-C04 · Espejos esféricos y parabólicos](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md); [B41-C17 · Telescopios Cassegrain y derivados](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md).

### Constante cosmológica

- La constante cosmológica `Λ` es una densidad de energía constante.

💡 **Cómo se explica en la clase [B26-C13](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md):**
- La materia frena la expansión como la gravedad frena una pelota; la constante cosmológica añade un empuje que no se diluye.
- *Descripción textual:* la tasa de expansión suma la materia, que decae como `a⁻³`, y la constante cosmológica; integrando `1/(aH)` se obtiene la edad, y el signo de `ä` marca el paso de frenar a acelerar.
- 🎯 **Por qué importa:** La edad del universo, la distancia a una galaxia y el calendario de su historia salen de la ecuación de Friedmann. Con ella se interpreta cualquier parámetro cosmológico.

📘 **Dónde se aprende** (1 clase): [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md).

### Constante de Avogadro

- Su unidad es el mol: un mol contiene exactamente 6,022 140 76 × 10²³ entidades elementales, número que es el valor fijado de la constante de Avogadro `N_A` (en mol⁻¹), según la definición vigente del SI (S2).

💡 **Cómo se explica en la clase [B06-C06](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md):**
- De masa a cantidad se divide entre la masa molar; de cantidad a número de partículas se multiplica por la constante de Avogadro; las flechas inversas deshacen cada paso.
- Enunciar la definición del mol y el valor de la constante de Avogadro.
- 🎯 **Por qué importa:** La misión OSIRIS-REx trajo a la Tierra 121,6 g de material del asteroide Bennu. Los análisis de laboratorio de una parte de esa muestra encontraron entre 4,5 y 4,7 % de carbono y entre 0,23 y 0,25 % de nitrógeno en masa (S1).

📘 **Dónde se aprende** (1 clase): [B06-C06 · Cantidad de sustancia y mol](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md).

### Constante de Boltzmann

- El SI fija la constante de Boltzmann `k_B = 1,380 649 × 10⁻²³ J/K` (S3), que define el kelvin.

🎯 **Por qué importa (clase B05-C13):** Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: ¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?

📘 **Dónde se aprende** (1 clase): [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md).

### Constante de consumo

- La constante de consumo `k` es la tasa de consumo de primer orden.

🎯 **Por qué importa (clase B64-C06):** Una película de células y matriz crea su propio microambiente. La pregunta motivadora: ¿hasta qué profundidad llega un nutriente en un biofilm y qué sucede con las células que quedan más adentro?

📘 **Dónde se aprende** (1 clase): [B64-C06 · Biofilms en ambientes extremos](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md).

### Constante de decaimiento

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B31-C08):** Fechar rocas, medir la edad de objetos y modelar la nucleosíntesis usan estas leyes. La decisión central: ¿cómo se estima una constante de decaimiento y cómo evoluciona una cadena?

📘 **Dónde se aprende** (1 clase): [B31-C08 · Decaimiento radiactivo](../programa/clases/B31/B31-C08-decaimiento-radiactivo/CLASE.md).

### Constante de degradación

- La constante de degradación `k` (1/d) fija la velocidad de pérdida.

💡 **Cómo se explica en la clase [B100-C04](../programa/clases/B100/B100-C04-almacenamiento-remoto-y-depositos-de-suministros/CLASE.md):**
- *Descripción textual:* la temperatura fija la constante de degradación y esta la vida útil; la fuga térmica fija la evaporación; ambas determinan cuánto hay que sobredimensionar.
- Límite: se supone un único mecanismo de degradación con una `Ea` constante; los materiales reales tienen varios y distintos.
- 🎯 **Por qué importa:** Guardar más cantidad para cubrir una ventana larga solo sirve si lo guardado sigue siendo útil al final. La decisión central: ¿cuánto sobredimensionar un depósito para que, tras la espera, quede la cantidad útil necesaria, y qué temperatura de almacenamiento reduce esa pérdida?

📘 **Dónde se aprende** (1 clase): [B100-C04 · Almacenamiento remoto y depósitos de suministros](../programa/clases/B100/B100-C04-almacenamiento-remoto-y-depositos-de-suministros/CLASE.md).

### Constante de desintegración

- La constante de desintegración `λ = 1/τ`.

🎯 **Por qué importa (clase B27-C14):** La luminosidad tardía de estas supernovas sigue la semivida del cobalto-56, y por eso se usan para medir distancias. La decisión central: ¿cuántos núcleos de cada especie quedan en cada instante y qué luminosidad producen?

📘 **Dónde se aprende** (1 clase): [B27-C14 · Supernovas termonucleares](../programa/clases/B27/B27-C14-supernovas-termonucleares/CLASE.md).

### Constante de despresurización

- La constante de despresurización `τ = V/(C_d A √(γRT) · 0,5787)`.

🎯 **Por qué importa (clase B104-C13):** Un procedimiento sirve si se puede ejecutar dentro del tiempo disponible. La decisión central: ¿para qué tamaños de orificio alcanza un tiempo de respuesta de 15 minutos y a partir de cuál ya no?

📘 **Dónde se aprende** (1 clase): [B104-C13 · Procedimientos de emergencia](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md).

### Constante de equilibrio

- La constante de equilibrio `K` es el cociente entre productos y reactivos elevados a sus coeficientes, medido en el equilibrio.
- La constante de equilibrio `K = exp(−ΔG°/RT)`.

💡 **Cómo se explica en la clase [B06-C13](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md):**
- Abajo, una decisión: si el cociente de reacción es menor que la constante, el sistema avanza hacia productos; si es mayor, hacia reactivos; si es igual, está en equilibrio.
- Escribir la constante de equilibrio de una reacción, incluyendo sólidos y gases.
- 🎯 **Por qué importa:** Según el cálculo de esta clase, el CO₂ de Marte puede condensarse como hielo o volver al gas según la temperatura. Es un equilibrio entre CO₂ sólido y gas: `CO₂(s) ⇌ CO₂(g)`.

📘 **Dónde se aprende** (2 clases): [B06-C13 · Equilibrio químico](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md); [B56-C07 · Energía química para la vida](../programa/clases/B56/B56-C07-energia-quimica-para-la-vida/CLASE.md).

### Constante de estructura

- La constante de estructura `Cn²` mide la intensidad de la turbulencia, en m^(−2/3).

🎯 **Por qué importa (clase B92-C04):** Un enlace espacial es perfecto hasta que llega a las últimas decenas de kilómetros. La decisión central: ¿cuánto margen exige la turbulencia y cuántas estaciones exige la nubosidad para cumplir una disponibilidad?

📘 **Dónde se aprende** (1 clase): [B92-C04 · Atmósfera y nubes en enlaces ópticos con la Tierra](../programa/clases/B92/B92-C04-atmosfera-y-nubes-en-enlaces-opticos-con-la-tierra/CLASE.md).

### Constante de estructura fina

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B31-C09](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md):**
- La constante de estructura fina calculada es `7,2973525643 × 10⁻³` (`1/α = 137,036`), igual a la de NIST (S1).
- 🎯 **Por qué importa:** Saber qué interacción domina en cada escala explica por qué los núcleos, los átomos y las estrellas son como son. La decisión central: ¿cuánto más fuerte es la fuerza eléctrica que la gravitatoria y qué fija el alcance de una fuerza?

📘 **Dónde se aprende** (1 clase): [B31-C09 · Interacciones fundamentales](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md).

### Constante de fuga

- La constante de fuga `τ` hace `p = p₀ e^(−t/τ)`.

💡 **Cómo se explica en la clase [B104-C05](../programa/clases/B104/B104-C05-sistemas-de-vehiculos-tripulados/CLASE.md):**
- Con una fuga de constante de tiempo de 72 h, la presión baja de 101,3 a 70 kPa en 26,6 h.
- Modelar una fuga lineal con una constante de tiempo y calcular el tiempo hasta un umbral.
- 🎯 **Por qué importa:** Lo que importa para respirar no es la presión total sino la presión parcial de cada gas. La decisión central: ¿cuánto tiempo hay para actuar si la cabina pierde presión o si se acumula CO₂?

📘 **Dónde se aprende** (1 clase): [B104-C05 · Sistemas de vehículos tripulados](../programa/clases/B104/B104-C05-sistemas-de-vehiculos-tripulados/CLASE.md).

### Constante de gravitación

- La constante de gravitación `G` tiene un valor medido (con incertidumbre) y unidades `m³ kg⁻¹ s⁻²`.

💡 **Cómo se explica en la clase [B05-C10](../programa/clases/B05/B05-C10-gravitacion-universal/CLASE.md):**
- Enunciar la ley de gravitación `F = G M m / r²` con su constante y unidades.
- 🎯 **Por qué importa:** La misma fuerza que hace caer una manzana mantiene a la Luna en órbita: esa idea unificó el cielo y la Tierra. La pregunta motivadora es: ¿cómo comprobar con números que la gravedad de la superficie y la órbita de la Luna son la misma fuerza?

📖 **Explicado a fondo:** [Constante de gravitación (G) y parámetro gravitacional (GM)](esencial/esencial-a-c.md#constante-de-gravitación-g-y-parámetro-gravitacional-gm) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B05-C10 · Gravitación universal](../programa/clases/B05/B05-C10-gravitacion-universal/CLASE.md); [B71-C02 · Ley de gravitación universal](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md).

### Constante de Hubble

- La constante de Hubble `H₀` es la razón entre la velocidad de recesión aparente y la distancia, hoy.
- La constante de Hubble `H₀` se da en `km s⁻¹ Mpc⁻¹`.

🎯 **Por qué importa (clase B01-C16):** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).

📘 **Dónde se aprende** (2 clases): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md); [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md).

### Constante de integración

- La constante de integración `C` es un número arbitrario: derivar lo elimina.

💡 **Cómo se explica en la clase [B09-C08](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md):**
- En física, cada integración sucesiva trae su constante: la velocidad inicial y la posición inicial.
- El script [antiderivadas_y_potencial.py](antiderivadas_y_potencial.py) calcula antiderivadas de polinomios generalizados por la regla de la potencia, las comprueba derivando, integra el perfil de aceleración, muestra que dos antiderivadas difieren en una constante y evalúa el potencial terrestre y el sesgo del acelerómetro.
- ⚠️ **Error frecuente:** Olvidar la constante de integración. Se corrige con los ejercicios 1 y 7.
- 🎯 **Por qué importa:** Un acelerómetro mide aceleración; lo que se necesita es velocidad y posición. Una gravedad `g(r)` se conoce; lo que decide si una sonda escapa es la energía, que sale de «deshacer» esa derivada.

📘 **Dónde se aprende** (1 clase): [B09-C08 · Integrales indefinidas](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md).

### Constante de Jacobi

- La constante de Jacobi es `C = 2Ω − v²` con `Ω = (x²+y²)/2 + (1−μ)/r₁ + μ/r₂`.
- La constante de Jacobi es `C = 2Ω − v²`, con `2Ω = x² + y² + 2(1−μ)/r₁ + 2μ/r₂`.
- La constante de Jacobi `C = 2Ω − v²` en el marco sinódico.

💡 **Cómo se explica en la clase [B73-C01](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md):**
- Una masa de prueba que parte de `(0,85, 0)` con velocidad `(0, −0,40)` en el marco sinódico tiene constante de Jacobi `C = 3,030382` y tras `20` unidades de tiempo (`86,97` d) está a `108018` km de la Luna, con una deriva de `C` de `6,94e-09`.
- Calcular la constante de Jacobi y medir su deriva.
- 🎯 **Por qué importa:** Con tres cuerpos no hay solución cerrada, pero sí una cantidad conservada que organiza todo lo demás: puntos de equilibrio, regiones prohibidas y transferencias de bajo costo. La decisión central: ¿cuándo basta el modelo de tres cuerpos restringido, y cómo sé que mi integración no inventa dinámica?

📘 **Dónde se aprende** (3 clases): [B73-C01 · Problema restringido de tres cuerpos](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md); [B73-C07 · Constante de Jacobi](../programa/clases/B73/B73-C07-constante-de-jacobi/CLASE.md); [B76-C08 · Transferencias de baja energía](../programa/clases/B76/B76-C08-transferencias-de-baja-energia/CLASE.md).

### Constante de Lipschitz

- La constante de Lipschitz `L` mide cuánto puede cambiar `f` cuando cambia `y`: `|f(t, y₁) − f(t, y₂)| ≤ L |y₁ − y₂|`.

💡 **Cómo se explica en la clase [B11-C02](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md):**
- En general, si `f` tiene constante de Lipschitz `L`, la diferencia crece como mucho como `δ e^{L t}`.
- Ejercicio 10 · transferencia. Para `f(y) = y²` en `|y| ≤ M`, ¿cuál es una constante de Lipschitz?
- 🎯 **Por qué importa:** Una nave no sigue «la» solución de las ecuaciones del movimiento: sigue la que corresponde a *su* posición y velocidad en el instante en que se midieron. Saber cuántos datos exige la ecuación, cuándo garantizan una única trayectoria y cuánto se amplifica su error es la base de toda predicción de trayectoria.

📘 **Dónde se aprende** (1 clase): [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md).

### Constante de proporcionalidad

- La constante de proporcionalidad `k` es ese valor fijo.

🎯 **Por qué importa (clase B03-C10):** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?

📘 **Dónde se aprende** (1 clase): [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md).

### Constante de radiación

- La constante de radiación es `a = 4σ/c`.

🎯 **Por qué importa (clase B26-C14):** Casi todo lo observable del universo temprano (radiación de fondo, abundancia de helio) depende de su temperatura y de qué componente dominaba la densidad en cada época.

📘 **Dónde se aprende** (1 clase): [B26-C14 · Evolución térmica del universo](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md).

### Constante de recuperación

- `τ` es la constante de recuperación dentro de una exposición.

🎯 **Por qué importa (clase B113-C02):** Ninguna clase previa trata la respuesta emocional ante simulaciones de riesgo. La decisión central: ¿cuántas repeticiones de un escenario hacen falta para que el pico baje a un nivel de trabajo, y cuándo la repetición deja de ayudar?

📘 **Dónde se aprende** (1 clase): [B113-C02 · Ansiedad y respuesta emocional en escenarios simulados](../programa/clases/B113/B113-C02-ansiedad-y-respuesta-emocional-en-escenarios-simulados/CLASE.md).

### Constante de Rydberg

- La constante de Rydberg `R` fija las longitudes de onda de las líneas del hidrógeno.

💡 **Cómo se explica en la clase [B02-C16](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md):**
- La constante de Rydberg para núcleo infinitamente pesado es `R∞ = 10 973 731,568 157 m⁻¹` (NIST, CODATA 2022, S2); para el hidrógeno se corrige por la masa del protón: `R_H = R∞/(1 + mₑ/mₚ)`, con `mₚ/mₑ = 1 836,152 673 426` (S3).
- 🎯 **Por qué importa:** Hasta 1859 se pensaba, con razones, que nunca sabríamos de qué están hechas las estrellas: estaban demasiado lejos para tocarlas. La pregunta motivadora es: ¿cómo se puede conocer la composición de un objeto que solo se ve como luz?

📘 **Dónde se aprende** (3 clases): [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md); [B45-C10 · Líneas de emisión](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md); [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md).

### Constante de Stefan–Boltzmann

- La constante de Stefan–Boltzmann `σ` liga la energía emitida por unidad de superficie con `T⁴`.
- La constante de Stefan–Boltzmann `σ` liga la emisión de un cuerpo negro con `T⁴`.

🎯 **Por qué importa (clase B01-C14):** Dos estrellas pueden verse igual de brillantes y ser totalmente distintas: una pequeña y cercana, otra enorme y lejana (C09). Para saber cómo es una estrella necesitas separar lo que ves (flujo) de lo que ella es (luminosidad, temperatura, radio) y de dónde está (distancia).

📘 **Dónde se aprende** (2 clases): [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B24-C03 · Diagrama de Hertzsprung-Russell](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md).

### Constante de tiempo

- La constante de tiempo `τ` es el tiempo en que la diferencia con el equilibrio se reduce a `1/e ≈ 36,8 %`.
- La constante de tiempo `τ` de un sensor de primer orden es el tiempo en que recorre el 63,2 % de un cambio brusco (`1 − e^{−1}`).
- La constante de tiempo `τ_c` de un sistema de primer orden es el tiempo en el que la respuesta a un escalón alcanza el 63,2 % de su valor final.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C03](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md):**
- La velocidad terminal es `g m/c = 196,1 m/s`, se alcanza con una constante de tiempo `m/c = 20 s`, y a los 30 s la velocidad es `152,4 m/s`.
- Interpretar la constante de tiempo y el equilibrio.
- ⚠️ **Error frecuente:** Mezclar la constante de tiempo con la velocidad. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Muchos procesos espaciales relajan hacia un equilibrio: una cápsula que cae frena hasta una velocidad terminal, un instrumento se enfría hacia la temperatura de su entorno, una población de partículas decae.

📘 **Dónde se aprende** (11 clases): [B11-C03 · Ecuaciones de primer orden](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md); [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B43-C11 · Dilatación térmica y estabilidad](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md); [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md); [B85-C11 · Ciclos térmicos](../programa/clases/B85/B85-C11-ciclos-termicos/CLASE.md) y 5 más.

### Constante de tiempo τ

- Nodo concentrado: modelo de una sola temperatura. Constante de tiempo `τ`: `m c/G`.
- Coeficiente de descarga `Cd`: corrección entre el área geométrica y la efectiva. Constante de tiempo `τ`: escala del vaciado exponencial.

💡 **Cómo se explica en la clase [B90-C11](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md):**
- Paso 1 · Constante de tiempo. `τ = m c/G = 1 800/2 = 900 s`.
- Plantear la ecuación de un nodo térmico concentrado y calcular su constante de tiempo.
- 🎯 **Por qué importa:** Una prueba funcional hecha antes de que la unidad se estabilice no demuestra nada sobre la temperatura extrema; una espera excesiva consume cámara y calendario. La decisión central: ¿cuánto debe esperar el ensayo para que la temperatura de la unidad sea la de la prueba?

📘 **Dónde se aprende** (2 clases): [B90-C11 · Ensayos térmicos](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md); [B106-C02 · Presurización de módulos](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md).

### Constante de velocidad

- La constante de velocidad `k(T)` es el promedio térmico `⟨σ v⟩`.
- Una reacción de primer orden `A → productos` tiene velocidad `v = −d[A]/dt = k[A]`, con `k` la constante de velocidad (en 1/s).

💡 **Cómo se explica en la clase [B06-C14](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md):**
- Una reacción real puede tener varios pasos, orden distinto de 1 y una constante de velocidad que no se comporta como Arrhenius a baja temperatura.
- *Descripción textual:* arriba, dos valles separados por una barrera de altura `E_a`; abajo, la cadena: la temperatura fija la fracción de moléculas con energía suficiente, esa fracción da la constante de velocidad por Arrhenius, y la constante da la velocidad y la vida media.
- 🎯 **Por qué importa:** Que una reacción sea posible (energía favorable, `K` grande) no significa que ocurra: puede ser tan lenta que no ocurra nunca en la edad del universo. En una nube molecular a 10 K, la energía térmica es de apenas 0,86 meV (C10).

📘 **Dónde se aprende** (2 clases): [B06-C14 · Cinética química inicial](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md); [B60-C01 · Colisiones moleculares y secciones eficaces en gas interestelar](../programa/clases/B60/B60-C01-colisiones-moleculares-y-secciones-eficaces-en-gas-interestelar/CLASE.md).

### Constante definitoria

- Una constante definitoria del SI es una de las siete cuyo valor numérico se fija exactamente (S4).
- Una constante definitoria es una constante física a la que el SI asigna un valor numérico exacto; las unidades se definen fijándola (S2).

💡 **Cómo se explica en la clase [B13-C01](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir constante definitoria con constante medida. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Una señal de radio o de láser viaja a la Luna y regresa. Para decir «la Luna está a 384 400 km» hay que haber acordado qué es un kilómetro, qué es un segundo y a qué velocidad viaja la señal.

📘 **Dónde se aprende** (2 clases): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md).

### Constante espectroscópica

- Una constante espectroscópica es un parámetro del Hamiltoniano efectivo (`B`, `D`, `H`…).

🎯 **Por qué importa (clase B62-C05):** Una constante sin incertidumbre no se puede usar para predecir una línea en otro rango, ni para decidir si una línea observada es de esa molécula. La decisión central: ¿cuántos parámetros justifica el conjunto de datos?

📘 **Dónde se aprende** (1 clase): [B62-C05 · Constantes espectroscópicas y ajuste de espectros](../programa/clases/B62/B62-C05-constantes-espectroscopicas-y-ajuste-de-espectros/CLASE.md).

### Constante física

- Una constante física es un valor con unidad, incertidumbre y referencia.

🎯 **Por qué importa (clase B14-C04):** En 1999 la sonda Mars Climate Orbiter se perdió al llegar a Marte. NASA atribuye la pérdida a un error de navegación causado por no traducir unidades inglesas a métricas: el software en tierra usaba unidades inglesas y el de a bordo, métricas (S1).

📘 **Dónde se aprende** (1 clase): [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### Constante molar de los gases

- La ley de los gases ideales relaciona la presión `P`, el volumen `V`, la cantidad de sustancia `n` y la temperatura absoluta `T`: `PV = nRT`, con `R` la constante molar de los gases.

🎯 **Por qué importa (clase B06-C09):** La NASA publica para Marte, Venus y la Tierra la presión y la temperatura medias en la superficie, la gravedad, el peso molecular de la atmósfera y su densidad (S1, S2, S3). ¿Puedes reproducir esa densidad con sólo lo anterior?

📘 **Dónde se aprende** (1 clase): [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md).

### Constante psicrométrica γ

- La pendiente `Δ` de la curva de saturación y la constante psicrométrica `γ` acoplan temperatura y vapor.

🎯 **Por qué importa (clase B115-C06):** El cultivo es el mayor flujo de agua de un hábitat con plantas. La decisión central: ¿cuánta agua transpira el cultivo, cuánta se recupera y cuánta hay que reponer, y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B115-C06 · Balance de agua y evapotranspiración en cultivos](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md).

### Constante rotacional

- La constante rotacional `B` es la energía por unidad de `J(J+1)` expresada en cm⁻¹.
- La constante rotacional `B` (MHz) depende del momento de inercia.

💡 **Cómo se explica en la clase [B62-C01](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md):**
- Calcular la constante rotacional `B` desde la masa reducida y la longitud de enlace.
- 🎯 **Por qué importa:** Una línea de CO a 115,27 GHz no es un dato aislado: es la consecuencia de un momento de inercia. Si entiendes de dónde sale, puedes predecir líneas que nadie ha medido y reconocer cuándo una línea observada no es del CO.

📘 **Dónde se aprende** (2 clases): [B55-C09 · Espectros moleculares de radio](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md); [B62-C01 · Espectros rotacionales de moléculas: niveles y reglas de selección](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md).

### Constante rotacional del nivel

- La constante rotacional del nivel `B_v = Be − αe(v+½)` decrece al vibrar.

🎯 **Por qué importa (clase B62-C02):** Las bandas del CO a 4,67 µm se observan en el infrarrojo, no en milimétricas. Para interpretarlas necesitas saber de dónde sale el origen de banda, por qué las ramas P y R se separan en dos grupos y qué cambia al pasar a un isotopólogo.

📘 **Dónde se aprende** (1 clase): [B62-C02 · Espectros vibracionales de moléculas](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md).

### Constantes de Oort

- Las constantes de Oort `A` y `B` miden la rotación y la cizalla locales.

💡 **Cómo se explica en la clase [B25-C07](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md):**
- A["Curva de rotación<br/>Theta(R)"] --> B["Constantes de Oort<br/>A, B"]
- Bland-Hawthorn y Gerhard (S1) adoptan `R₀ = 8,2 kpc` y `Θ₀ = 238 km/s`, y definen las constantes de Oort por `A − B = Θ₀/R₀` y `A + B = −(∂Θ/∂R)_{R₀}`; recogen valores medidos de `A − B` entre `27` y `32 km s⁻¹ kpc⁻¹`, y describen una curva de rotación casi plana entre `5` y `13 kpc`.
- 🎯 **Por qué importa:** Las estrellas de una galaxia no giran en círculos perfectos: oscilan alrededor de una órbita circular, y su agitación revela la edad y la historia de la población. Además, no nacen todas con la misma masa: la función de masa inicial fija cuántas hay de cada tipo y cuánta luz y metales producirán.

📘 **Dónde se aprende** (1 clase): [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### Constantes de placa

- Las constantes de placa son los seis coeficientes de la relación lineal entre píxel y `(ξ, η)`.

💡 **Cómo se explica en la clase [B58-C06](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md):**
- Plantear el modelo lineal de seis constantes de placa.
- El script [astrometria.py](astrometria.py) proyecta, ajusta seis constantes de placa con 40 estrellas sintéticas y mide el error de un asteroide (comprueba ida y vuelta de 10⁻⁹, escala y rotación sin ruido con 10⁻⁹ y RMS entre 0,7 y 1,2 veces el esperado).
- 🎯 **Por qué importa:** Una órbita no puede ser mejor que sus posiciones: un error de décimas de segundo de arco se amplifica al propagar. La decisión central: ¿con qué exactitud puedo asignar coordenadas a un objeto en una imagen y qué la limita?

📘 **Dónde se aprende** (1 clase): [B58-C06 · Astrometría de objetos menores](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md).

### Constantes definitorias

- El SI (Sistema Internacional de Unidades) es el sistema acordado internacionalmente; sus siete unidades base son el segundo (s), el metro (m), el kilogramo (kg), el amperio (A), el kelvin (K), el mol (mol) y la candela (cd), definidas a partir de siete constantes definitorias de valor exacto (S2).

🎯 **Por qué importa (clase B03-C06):** El 23 de septiembre de 1999 la NASA perdió contacto con la sonda Mars Climate Orbiter. Según la agencia, un error de navegación se debió a no traducir unidades inglesas a métricas: el programa en tierra usaba unas y el de la nave otras, y la sonda pasó demasiado cerca de Marte y se quemó en su atmósfera (S1).

📘 **Dónde se aprende** (1 clase): [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md).

### Constelación

- Una constelación es, para la IAU, una de las 88 regiones en que se divide toda la esfera celeste, con límites definidos por líneas de ascensión recta y declinación (S1).
- Una constelación es un conjunto de satélites que operan coordinados.

💡 **Cómo se explica en la clase [B08-C06](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md):**
- Eugène Delporte, del Observatorio Real de Bruselas, trazó sus límites con líneas de ascensión recta y declinación; la asamblea de 1928 en Leiden los aprobó y se publicaron en 1930; hoy se distribuyen en coordenadas J2000, y las estrellas variables conocidas se mantuvieron en la constelación en que ya estaban (S1).
- Dos consecuencias: toda posición del cielo cae en una, y solo una, constelación; y el nombre de una constelación sirve para *localizar* («está en…»), no para describir lo que es.
- ⚠️ **Error frecuente:** Creer que una constelación es una agrupación física. Ejercicio 6.
- 🎯 **Por qué importa:** Dos personas dicen «la estrella roja de la Cruz del Sur» y creen hablar de lo mismo; un programa de telescopio pide «HIP 12345». Sin un lenguaje común no puedes repetir una observación ni compartirla.

📘 **Dónde se aprende** (2 clases): [B08-C06 · Constelaciones y catálogos estelares](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md); [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md).

### Constelación grande

- Una constelación grande son muchos satélites con un mismo diseño.

💡 **Cómo se explica en la clase [B121-C03](../programa/clases/B121/B121-C03-proteccion-ambiental-en-la-legislacion-espacial/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué `p ≥ 0,9` no basta para una constelación grande?
- 🎯 **Por qué importa:** El catálogo no trata la mitigación de desechos como requisito normativo. La decisión central: ¿un diseño cumple el plazo de desorbitación, la probabilidad de éxito y el riesgo de reentrada que exige la norma?

📘 **Dónde se aprende** (1 clase): [B121-C03 · Protección ambiental en la legislación espacial](../programa/clases/B121/B121-C03-proteccion-ambiental-en-la-legislacion-espacial/CLASE.md).

### Constelación oscura

- Una constelación oscura es una figura reconocida no en las estrellas sino en las zonas oscuras de la Vía Láctea, que corresponden a nubes de polvo (S1).

💡 **Cómo se explica en la clase [B02-C05](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md):**
- Describir ejemplos de alineaciones solares y de constelaciones oscuras en la literatura.
- 🎯 **Por qué importa:** Hablar de «astronomía andina» en singular es un error: los Andes reúnen sociedades de épocas y regiones muy distintas. La pregunta motivadora es: ¿cómo se estudia respetuosamente un cielo que otra cultura leyó de otra manera, sin imponerle nuestras categorías y sin inventar lo que las fuentes no dicen?

📘 **Dónde se aprende** (1 clase): [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md).

### Constelación Walker delta

- Una constelación Walker delta `i:T/P/F` tiene `T` satélites en `P` planos con inclinación `i`;

💡 **Cómo se explica en la clase [B89-C17](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md):**
- Generar una constelación Walker delta `i:T/P/F`.
- 🎯 **Por qué importa:** El número de satélites, su altitud y la inclinación fijan cuánta gente o cuántos usuarios ven al menos uno (o cuatro, para navegar) y cuánto cuesta lograrlo. La decisión central: ¿cuántos satélites y qué geometría dan la cobertura necesaria?

📘 **Dónde se aprende** (1 clase): [B89-C17 · Constelaciones y cobertura](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md).

### Consulta

- Una consulta selecciona filas y columnas con criterios.

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- La consulta (`paralaje > 2 mas` y `mag < 15`) devuelve 1594 filas, con distancia mediana 290,12 pc.
- No hay red, autenticación, reintentos, paginación ni descargas parciales; el servidor es local y la consulta ADQL no se envió, de modo que no sé qué respondería un servicio real.
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.

📘 **Dónde se aprende** (1 clase): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md).

### Consulta de solapamiento

- Una consulta de solapamiento devuelve las cajas que se cruzan con la de consulta.

💡 **Cómo se explica en la clase [B14-C28](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md):**
- Q["Consulta<br/>caja o punto"] --> I["Índice R-tree<br/>candidatos por solapamiento"]
- *Descripción textual:* la consulta (caja o punto) va primero al índice, que devuelve candidatos por solapamiento; se refinan con una prueba exacta de geometría, se unen con los atributos por identificador y se obtiene el resultado.
- 🎯 **Por qué importa:** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.

📘 **Dónde se aprende** (1 clase): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md).

### Consulta puntual

- Una consulta puntual devuelve las cajas que contienen un punto.

🎯 **Por qué importa (clase B14-C28):** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.

📘 **Dónde se aprende** (1 clase): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md).

### Consume

- Una falla se consume si se termina después de su plazo.

💡 **Cómo se explica en la clase [B110-C04](../programa/clases/B110/B110-C04-priorizacion-y-decisiones-bajo-emergencia/CLASE.md):**
- Para el orden `(F2, F4, F5, F1, F3, F6)` se acumulan los esfuerzos y se compara con el plazo: F2 termina a `10 ≤ 15`, F4 a `30 ≤ 55`, F5 a `65 ≤ 120`, F1 a `95 > 90` (se consume una de vehículo), F3 a `120`, F6 a `135`.
- Términos `10, 30, 65, 95, 120, 135`; solo F1 (95 > 90) se consume: `(0, 1, 0)`.
- 🎯 **Por qué importa:** B104 enseña los procedimientos; falta cómo se ordenan cuando coinciden. La decisión central: ¿qué se atiende primero y cuánto cuesta equivocarse de orden?

📘 **Dónde se aprende** (1 clase): [B110-C04 · Priorización y decisiones bajo emergencia](../programa/clases/B110/B110-C04-priorizacion-y-decisiones-bajo-emergencia/CLASE.md).

### Consumo

- El consumo es `m = J_total/(Isp g₀)`.
- El consumo es la masa esperada de repuestos usados.

💡 **Cómo se explica en la clase [B87-C13](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md):**
- Estimar el consumo por hora de un ciclo límite.
- La evidencia es la ficha de consumo y ciclo límite de una maniobra con propulsores del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Los propulsores son el actuador de más par y de respuesta rápida, y el único que cambia el momento total del satélite, pero cada pulso gasta masa que no vuelve. La decisión central: ¿cuánto propergol cuesta una maniobra o un año de mantenimiento de actitud, y qué precisión permite el impulso mínimo?

📘 **Dónde se aprende** (2 clases): [B87-C13 · Propulsores de control de actitud](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md); [B97-C19 · Logística de piezas y reparaciones](../programa/clases/B97/B97-C19-logistica-de-piezas-y-reparaciones/CLASE.md).

### Consumo específico

- El consumo específico `TSFC = f/(F/ṁ)`.

💡 **Cómo se explica en la clase [B79-C16](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md):**
- El empuje específico máximo (`838,4 N·s/kg`) está en `r = 15,80`, mientras que el consumo mínimo del barrido (`28,60`) está en el borde (`r = 40`): subir `r` ahorra combustible pero a costa de empuje por kg de aire, es decir, de tamaño del motor.
- Calcular el flujo de combustible, el empuje específico y el consumo específico.
- 🎯 **Por qué importa:** Ninguna clase cubre cómo se cuantifica la conversión de energía en propulsión. Sin eficiencias separadas, un cambio de diseño se evalúa a ciegas: no se sabe si mejora el ciclo o el aprovechamiento del chorro.

📘 **Dónde se aprende** (1 clase): [B79-C16 · Eficiencias termodinámicas de motores](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md).

### Consumo específico de oxígeno

- Consumo específico de oxígeno: O₂ por kilogramo y minuto.

💡 **Cómo se explica en la clase [B106-C01](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md):**
- Calcular el oxígeno que consume una persona en reposo a partir de su consumo específico y compararlo con el valor consultado.
- 🎯 **Por qué importa:** Un hábitat se diseña de adentro hacia afuera: primero lo que consume y emite la tripulación, después la máquina que lo repone. Si el balance humano está mal, todo el ECLSS queda mal dimensionado.

📘 **Dónde se aprende** (1 clase): [B106-C01 · Requisitos de habitabilidad](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md).

### Contacto

- Un contacto es una ventana `(origen, destino, inicio, fin, tasa, retardo)`.
- Un contacto `(de, a, inicio, fin, tasa, retardo)` es una oportunidad de transmisión.
- El contacto activa un segundo resorte cuando `u > g`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B84-C25](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md):**
- *Descripción textual:* en cada paso se hace una prueba elástica y, si excede el límite, se retorna; el contacto se resuelve con Newton cambiando la tangente al cerrar la holgura.
- Paso 1 · Con contacto. `u > g` si `P > k₁ g = 1000 N`.
- 🎯 **Por qué importa:** Un modelo lineal da tensiones de 400 MPa en un material que cedió a 275: el resultado correcto es una deformación permanente y una tensión residual que solo el análisis no lineal muestra. La decisión central: ¿qué deformación permanente y tensión residual deja una carga que excede el límite elástico, y cuándo actúa un contacto?

📘 **Dónde se aprende** (4 clases): [B84-C25 · Comportamiento estructural no lineal: plasticidad y contacto](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md); [B89-C13 · Protocolos para espacio profundo](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md); [B94-C04 · Redes con retardo y desconexión: enrutamiento y almacenamiento](../programa/clases/B94/B94-C04-redes-con-retardo-y-desconexion-enrutamiento-y-almacenamiento/CLASE.md); [B96-C02 · Concepto de operaciones de misión](../programa/clases/B96/B96-C02-concepto-de-operaciones-de-mision/CLASE.md).

### Contacto de Hertz

- El contacto de Hertz esfera-plano: `a = (3FR/(4E*))^(1/3)`.
- El contacto de Hertz da el radio de contacto `a = (3 Q R′/(4E*))^(1/3)` y la presión máxima `p₀ = 3Q/(2πa²)`.

💡 **Cómo se explica en la clase [B43-C25](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md):**
- Calcular `a`, `δ` y `p₀` de un contacto de Hertz.
- 🎯 **Por qué importa:** La rigidez del contacto determina cuánto se mueve el eje bajo carga y la frecuencia de resonancia. La decisión central: ¿cuánto se deforma el contacto, cuánta rigidez aporta y qué fracción de la carga soporta la bola más cargada?

📘 **Dónde se aprende** (2 clases): [B43-C25 · Rodamientos y apoyos de precisión en telescopios](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md); [B84-C14 · Rodamientos y lubricación espacial](../programa/clases/B84/B84-C14-rodamientos-y-lubricacion-espacial/CLASE.md).

### Contacto de penalización

- Un contacto de penalización reacciona con una fuerza `k·penetración + c·velocidad` cuando hay interpenetración.

💡 **Cómo se explica en la clase [B102-C01](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md):**
- Una masa de 5 kg sobre un contacto de penalización `k = 2,0 × 10⁴ N/m` termina en reposo con una penetración `m g/k`: `2,4517 mm` en la Tierra, `0,9325 mm` en Marte y `0,4050 mm` en la Luna.
- Modelar un contacto unilateral con penalización y comparar la penetración estática con `m g/k`.
- 🎯 **Por qué importa:** Un manipulador de un rover se diseña y se ensaya en la Tierra, pero trabaja en Marte o en la Luna. La decisión central: ¿qué par necesita cada articulación en otro cuerpo, y qué cambia además del par?

📘 **Dónde se aprende** (1 clase): [B102-C01 · Dinámica multicuerpo de rovers y manipuladores](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md).

### Contactos

- Los contactos son los instantes en que los discos se tocan.

💡 **Cómo se explica en la clase [B29-C01](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md):**
- T --> NUM["contactos numéricos z = 1 + k"]
- Verificar `T₁₄` buscando numéricamente los contactos.
- 🎯 **Por qué importa:** El tránsito es el método con más planetas descubiertos. Su profundidad da el radio del planeta y su duración informa del semieje y el parámetro de impacto.

📘 **Dónde se aprende** (1 clase): [B29-C01 · Tránsitos planetarios](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md).

### Contador de canal maestro

- El contador de canal maestro (MCFC) cuenta todas las tramas; el de canal virtual (VCFC), las del canal.

🎯 **Por qué importa (clase B94-C03):** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?

📘 **Dónde se aprende** (1 clase): [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### Contador de secuencia

- El contador de secuencia debe valer el anterior más uno.

💡 **Cómo se explica en la clase [B88-C09](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md):**
- El último caso muestra que, tras un `TO_SAFE` con secuencia fuera de orden, el contador queda en 200 y hay que resincronizarlo con un procedimiento definido.
- 🎯 **Por qué importa:** Un telecomando aceptado en el estado equivocado puede dañar la nave; uno rechazado en el estado correcto puede perderla. La decisión central: ¿qué comando es válido en cada modo y qué comprobaciones lo protegen?

📘 **Dónde se aprende** (1 clase): [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md).

### Contaminación

- La contaminación es el material terrestre que altera la muestra; un blanco de procedimiento es una muestra de control que sigue el mismo tratamiento sin la muestra para detectarla.
- El recall es la fracción del suelo verdadero recuperada; la contaminación es la fracción de lo clasificado como suelo que no lo es.
- La estimación se complica por la contaminación: las alas de las fuentes elevan el fondo medido.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C20](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md):**
- Las muestras de Bennu, devueltas a la Tierra en condiciones controladas para limitar la contaminación, tienen más carbono, nitrógeno y amoníaco que las de Ryugu y que la mayoría de los meteoritos, con C = 4,5–4,7 % y N = 0,23–0,25 % en masa (S2).
- (2) Controlar la contaminación y usar blancos de procedimiento: los autores de S2 subrayan que la devolución en condiciones controladas permitió estudiar material sin exposición incontrolada a la biosfera terrestre.
- 🎯 **Por qué importa:** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.

📘 **Dónde se aprende** (5 clases): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md); [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B45-C23 · Fotometría de apertura y estimación del cielo](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md); [B57-C30 · Nubes de puntos tridimensionales](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md); [B86-C14 · Envejecimiento de paneles](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md).

### Contaminación cruzada

- La contaminación cruzada es la transferencia desde otra muestra o del ambiente.

🎯 **Por qué importa (clase B55-C18):** En muestras extraterrestres la cantidad buscada puede ser del orden de la contaminación que entra al manipularlas. La decisión central: ¿la señal neta supera el límite de detección y con qué incertidumbre, una vez restado el blanco?

📘 **Dónde se aprende** (1 clase): [B55-C18 · Contaminación de muestras](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md).

### Contaminación lumínica

- La contaminación lumínica es el exceso de luz artificial que borra la visibilidad del cielo nocturno.
- La contaminación lumínica es la luz artificial que degrada el cielo nocturno.
- La contaminación lumínica es el brillo del cielo nocturno por luz artificial emitida o reflejada hacia arriba, y su efecto sobre la observación y los ecosistemas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C06](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md):**
- Ejercicio 10 · transferencia. El autor de S3 propone considerar la contaminación lumínica como pérdida cultural.
- 🎯 **Por qué importa:** Chile alberga algunos de los cielos más oscuros del mundo y los más grandes observatorios, y también pueblos que miraron esos cielos durante milenios. La pregunta motivadora es: ¿cómo hablar de saberes celestes de pueblos vivos sin generalizar, sin apropiarse y sin presentar como establecido lo que no hemos podido verificar?

📖 **Explicado a fondo:** [Contaminación lumínica](esencial/ampliacion-a-m.md#contaminación-lumínica) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B02-C06 · Astronomía de pueblos originarios de Chile](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md); [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md); [B08-C12 · Limitación por contaminación lumínica](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md); [B48-C18 · Protección del cielo oscuro](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md).

### Contaminación molecular

- La contaminación molecular es una película condensada; su espesor sale de `m/ρ`.

💡 **Cómo se explica en la clase [B85-C16](../programa/clases/B85/B85-C16-polvo-lunar-y-contaminacion/CLASE.md):**
- Contaminacion molecular ILUSTRATIVA: 0.10 g condensables llegan al radiador -> espesor 0.100 um ; delta alfa = 0.0500 ;
- 🎯 **Por qué importa:** Un radiador que se ensucia rechaza menos calor y se calienta; en la Luna la limpieza no es sencilla. La decisión central: ¿qué cobertura de polvo o espesor de película hace subir la temperatura de un radiador por encima de su límite?

📘 **Dónde se aprende** (1 clase): [B85-C16 · Polvo lunar y contaminación](../programa/clases/B85/B85-C16-polvo-lunar-y-contaminacion/CLASE.md).

### Contención

- La contención es el aislamiento de una muestra.
- La contención es el conjunto de medidas que impiden que el material salga o entre.
- La contención es mantener el contaminante en un volumen acotado.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B56-C19](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md):**
- La política de COSPAR exige contención ante una posible entidad replicante, sea cual sea la probabilidad; el cálculo de esta clase no la reemplaza.
- La cifra es sintética y depende de supuestos; el anuncio debe describir la evidencia y sus límites, y la política exige contención de muestras mientras se verifica (sección 5).
- ⚠️ **Error frecuente:** Olvidar la contención. Se corrige con la sección 5.
- 🎯 **Por qué importa:** Anunciar demasiado pronto un hallazgo puede dañar la ciencia y la confianza pública; ocultarlo puede dañar la transparencia. Hace falta una forma explícita de saber cuánta evidencia hay.

📘 **Dónde se aprende** (5 clases): [B56-C19 · Ética del descubrimiento de vida](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md); [B63-C05 · Contención de muestras extraterrestres: instalaciones y principios](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md); [B106-C10 · Gestión de residuos humanos](../programa/clases/B106/B106-C10-gestion-de-residuos-humanos/CLASE.md); [B117-C02 · Contención de riesgos biológicos y químicos en cabina](../programa/clases/B117/B117-C02-contencion-de-riesgos-biologicos-y-quimicos-en-cabina/CLASE.md); [B122-C06 · Respuesta a incidentes cibernéticos en operaciones de misión](../programa/clases/B122/B122-C06-respuesta-a-incidentes-ciberneticos-en-operaciones-de-mision/CLASE.md).

### Contenedor

- Una imagen es el paquete inmutable; un contenedor es una instancia en ejecución de una imagen.

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- Según S1, un contenedor es autocontenido y aislado, y comparte el núcleo del anfitrión.
- Por eso dos contenedores idénticos en máquinas distintas pueden diferir en el último dígito de un cálculo (C10) si el procesador es distinto.
- ⚠️ **Error frecuente:** Creer que el contenedor lo reproduce todo. Se corrige con los ejercicios 3 y 8.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende** (1 clase): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md).

### Contenido

- El contenido del elipsoide `k²` es la probabilidad de que el error caiga dentro.

💡 **Cómo se explica en la clase [B74-C11](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md):**
- En 3D el contenido de un elipsoide `1σ` es solo `0,1987`.
- Descripción larga: rotar no cambia la incertidumbre total; la correlación aplana el elipsoide; el contenido de un elipsoide de k sigma en 3D es mucho menor que el intervalo 1D.
- 🎯 **Por qué importa:** Los números de la diagonal engañan: dos errores muy correlacionados pueden ser individualmente grandes y conjuntamente pequeños. La decisión central: ¿qué dicen realmente los autovalores, las correlaciones y el elipsoide, y qué probabilidad encierra cada «k sigma» en tres dimensiones?

📘 **Dónde se aprende** (1 clase): [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Contenido canónico

- El contenido canónico es una forma de escribir el registro con claves ordenadas y sin espacios, para que el hash sea reproducible.

💡 **Cómo se explica en la clase [B13-C19](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md):**
- El contenido canónico (claves ordenadas, sin espacios) del registro, sin el campo `sha256`, se codifica en UTF-8 y se procesa con SHA-256; el resultado se guarda en el propio registro.
- R --> H["Hash SHA-256<br/>del contenido canónico"]
- 🎯 **Por qué importa:** Dentro de un año alguien usará los datos de un fotodiodo calibrado hoy. Necesitará saber con qué patrones, a qué temperatura, con qué incertidumbre y hasta cuándo es válida la calibración.

📘 **Dónde se aprende** (1 clase): [B13-C19 · Metadatos y registros de calibración](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md).

### Contenido electrónico total

- El contenido electrónico total (TEC), en TECU (`1 TECU = 10¹⁶ m⁻²`).

🎯 **Por qué importa (clase B51-C05):** A frecuencias bajas la ionosfera domina el error de fase y de polarización. La decisión central: ¿cómo se mide y se quita el efecto con las propias frecuencias de la observación?

📘 **Dónde se aprende** (1 clase): [B51-C05 · Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md).

### Conteo

- El conteo `N ~ Poisson(sH + B)`.

💡 **Cómo se explica en la clase [B105-C07](../programa/clases/B105/B105-C07-dosimetria-personal/CLASE.md):**
- En 20.000 repeticiones por dosis, el intervalo `Ĥ ± 1,96 σ_H` cubre el valor verdadero entre 0,949 y 0,950 de los casos: la aproximación gaussiana funciona con estos conteos.
- Con seis dosis de referencia (1, 2, 5, 10, 20 y 50 mSv) y conteos sintéticos, `ŝ = Σ H y/Σ H² = 197,04` cuentas/mSv (verdad 200).
- 🎯 **Por qué importa:** Un número de dosis sin su incertidumbre no es utilizable: cerca del fondo, el dosímetro no distingue una dosis pequeña de cero. La decisión central: ¿desde qué dosis se puede afirmar que el dosímetro vio algo y con qué incertidumbre se informa?

📘 **Dónde se aprende** (1 clase): [B105-C07 · Dosimetría personal](../programa/clases/B105/B105-C07-dosimetria-personal/CLASE.md).

### Conteo acumulado

- El conteo acumulado `N(>d)` es el número de objetos mayores que `d`.

💡 **Cómo se explica en la clase [B118-C01](../programa/clases/B118/B118-C01-poblacion-de-objetos-orbitales/CLASE.md):**
- *Descripción textual:* de dos conteos acumulados se obtiene la pendiente de la distribución de tamaños; de la población sintética se obtiene el conteo por capa y, dividido por el volumen, la densidad espacial.
- 🎯 **Por qué importa:** Los catálogos solo contienen los objetos que los sensores pueden seguir; el resto se conoce por modelos y por mediciones in situ. Esta clase fija el vocabulario cuantitativo (conteos acumulados, pendiente, densidad) que usan todas las demás.

📘 **Dónde se aprende** (1 clase): [B118-C01 · Población de objetos orbitales](../programa/clases/B118/B118-C01-poblacion-de-objetos-orbitales/CLASE.md).

### Conteo cíclico

- Un conteo cíclico cuenta una parte del inventario cada vez.

💡 **Cómo se explica en la clase [B100-C01](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md):**
- *Descripción textual:* los lotes entran al almacén; salen por emisión (que queda registrada) o por caducidad; el conteo cíclico compara el registro con lo físico.
- Calcular la exactitud del registro con un conteo cíclico.
- 🎯 **Por qué importa:** Un inventario que solo sabe «cuántas unidades hay» no puede decir de qué lote vienen, cuándo caducan ni dónde se usaron. La decisión central: ¿qué registro mínimo hace falta para emitir primero lo que caduca antes y para encontrar, si un lote resulta defectuoso, adónde fue?

📘 **Dónde se aprende** (1 clase): [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Conteo de fotones

- El conteo de fotones registra eventos individuales en vez de energía.
- El conteo de fotones registra eventos individuales.

💡 **Cómo se explica en la clase [B92-C05](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md):**
- *Descripción textual:* la ranura con pulso recibe señal y fondo, las otras solo fondo; el receptor elige la ranura de mayor conteo, de ahí sale el error de símbolo y los fotones necesarios; el tiempo muerto limita la tasa medible.
- Como contexto publicado, el receptor de DSOC en Palomar es un receptor de conteo de fotones de nanohilos superconductores (NASA/JPL), sin más especificaciones en la página consultada.
- 🎯 **Por qué importa:** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?

📘 **Dónde se aprende** (2 clases): [B57-C11 · LiDAR satelital](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md); [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Conteo de Poisson

- El conteo de Poisson tiene varianza igual a su media.

💡 **Cómo se explica en la clase [B67-C07](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md):**
- *Descripción textual:* un parámetro físico (la abundancia) produce una señal media; el azar de Poisson la convierte en un conteo; el cálculo inverso devuelve la abundancia con su incertidumbre, y lo mismo con el espectro de masas.
- Invertir un conteo de Poisson y propagar su incertidumbre.
- 🎯 **Por qué importa:** Un sensor no mide «agua»: mide cuentas, y de ellas se infiere la abundancia con un modelo. La decisión central: ¿cuánto tiempo de medición y qué canales hacen falta para detectar y separar un volátil con la incertidumbre requerida?

📘 **Dónde se aprende** (1 clase): [B67-C07 · Sensores para volátiles: espectrometría de neutrones y de masas](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md).

### Conteo independiente

- El conteo independiente es un recuento por un método distinto del que se verifica.
- Un conteo independiente usa otro método (C18).

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- Un conteo independiente, con arreglos de NumPy y sin pandas, da 1594: coincide.
- Comprueba con un conteo independiente: 1594.
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.

📘 **Dónde se aprende** (2 clases): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md); [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md).

### Conteos esperados

- Los conteos esperados son `N [P(X>u_k) − P(X>u_{k+1})]`.

💡 **Cómo se explica en la clase [B33-C04](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md):**
- *Descripción textual:* los umbrales definen niveles; la cola de potencias da conteos esperados que el Monte Carlo verifica.
- Calcular conteos esperados de una cola de potencias.
- 🎯 **Por qué importa:** Comparar severidades exige conocer cómo se definió cada nivel. La decisión central: ¿cuántos eventos caen en cada nivel y por qué no son comparables entre escalas?

📘 **Dónde se aprende** (1 clase): [B33-C04 · Escalas de severidad de clima espacial](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md).

### Conteos «off»

- Los conteos «off» `N_off` son los de una región de fondo.

💡 **Cómo se explica en la clase [B27-C19](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md):**
- *Descripción textual:* los conteos alimentan dos fórmulas de significancia; el Monte Carlo bajo la hipótesis nula compara sus tasas de falsos positivos; la razón de verosimilitudes sirve para hallar la señal mínima.
- Aquí no se usa ninguna cifra de su rendimiento: los conteos son sintéticos.
- 🎯 **Por qué importa:** Decir «detectamos la fuente a 5σ» exige saber qué fórmula se usó y cuántos falsos positivos produce. La decisión central: ¿qué significancia tiene un par de conteos y qué señal mínima se necesita para una detección?

📘 **Dónde se aprende** (1 clase): [B27-C19 · Observatorios de rayos X y gamma](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md).

### Conteos «on»

- Los conteos «on» `N_on` son los de la región de la fuente.

💡 **Cómo se explica en la clase [B27-C19](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md):**
- *Descripción textual:* los conteos alimentan dos fórmulas de significancia; el Monte Carlo bajo la hipótesis nula compara sus tasas de falsos positivos; la razón de verosimilitudes sirve para hallar la señal mínima.
- Aquí no se usa ninguna cifra de su rendimiento: los conteos son sintéticos.
- 🎯 **Por qué importa:** Decir «detectamos la fuente a 5σ» exige saber qué fórmula se usó y cuántos falsos positivos produce. La decisión central: ¿qué significancia tiene un par de conteos y qué señal mínima se necesita para una detección?

📘 **Dónde se aprende** (1 clase): [B27-C19 · Observatorios de rayos X y gamma](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md).

### Conteos oscuros

- Los conteos oscuros y el fondo son eventos sin señal.

🎯 **Por qué importa (clase B92-C05):** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?

📘 **Dónde se aprende** (1 clase): [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Contexto

- El contexto y el objeto y fin son fuentes que restringen la lectura.
- El contexto (`info`) distingue propósito y época.

💡 **Cómo se explica en la clase [B88-C38](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md):**
- Se extrae con una sal y se expande con el contexto `propósito|época=n`.
- Paso 2 · Derivar. `expand(PRK, contexto, 32)`.
- 🎯 **Por qué importa:** Una clave filtrada o reutilizada anula toda la autenticación. La decisión central: ¿cómo se separan las claves por función y época para que el compromiso de una no arrastre a las demás?

📘 **Dónde se aprende** (2 clases): [B88-C38 · Gestión de claves y secretos en aviónica](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md); [B119-C32 · Interpretación de tratados internacionales](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md).

### Contexto ritual y social

- El contexto ritual y social es el conjunto de prácticas, calendarios, jerarquías y creencias en que se inscribe una observación del cielo.

💡 **Cómo se explica en la clase [B132-C05](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md):**
- python programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/contexto.py
- 🎯 **Por qué importa:** El catálogo trata alineaciones sin ese contexto. La decisión central: ¿cuánto apoyo da cada línea de evidencia a la intención de una alineación, y qué parte de la conclusión depende de lo que se supone de antemano?

📘 **Dónde se aprende** (1 clase): [B132-C05 · Contexto ritual y social de la observación del cielo](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md).

### Contingencia

- DITL: prueba de «día en la vida». Contingencia: tiempo reservado para fallas.

💡 **Cómo se explica en la clase [B90-C20](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md):**
- Para una confianza de 90 % hay que reservar `25 − 15 = 10 d` de contingencia sobre los 15 d sin fallas.
- Por calendario: duración y contingencia (esta clase).
- ⚠️ **Error frecuente:** Planificar con la duración sin fallas. Reserva contingencia (8.4)
- 🎯 **Por qué importa:** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### Continua

- Es discreta si toma valores aislados y continua si toma cualquier valor de un intervalo (S1, C.2.2, nota 1).

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- Su límite: en una variable continua no hay pilas contables; la «pila» de un valor exacto pesa cero y sólo pesan los intervalos.
- Paso 1 · Variables. `X` discreta (pmf de 8.1), `Y` continua (8.3); se supone que `X` e `Y` son independientes (el telémetro no depende de los computadores en este modelo).
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.

📘 **Dónde se aprende** (1 clase): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md).

### Continua en a

- Una función `f` es continua en `a` si existen `f(a)` y `lim_{x→a} f(x)` y son iguales (S1, §1.4(ii)).

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- Para comprobar que `f(x) = x² + 1` es continua en 2: `f(2) = 5`, el límite es 5, coinciden.
- Para polinomios, exponenciales, senos y cosenos basta evaluar; sumas, productos y composiciones de funciones continuas son continuas (S1).
- ⚠️ **Error frecuente:** Creer que «definida» implica «continua». Se corrige con el ejercicio 1.
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Continua por tramos

- Una función es continua por tramos si lo es salvo en un número finito de saltos.

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- Calcular el valor que hace continua una función definida por tramos.
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Continuación

- La continuación sigue la familia en `A`.

💡 **Cómo se explica en la clase [B76-C06](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md):**
- Una búsqueda directa a `70.000 km` puede caer en otra solución; la continuación evita ese riesgo.
- Seguir la familia por continuación en la amplitud.
- ⚠️ **Error frecuente:** Buscar la DRO sin continuación. Se corrige con 8.2.
- 🎯 **Por qué importa:** La NRHO es inestable y exige mantenimiento; la DRO es estable. La decisión central: ¿qué se gana y qué se paga al elegir una órbita estable y lejana frente a una NRHO cercana?

📘 **Dónde se aprende** (1 clase): [B76-C06 · Órbitas DRO — Dinámica cislunar y operaciones de proximidad](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md).

### Continuidad

- La continuidad estacionaria dice que `ṁ` es el mismo en todas las secciones.
- La continuidad exige que `P` y `e` coincidan en la unión.

💡 **Cómo se explica en la clase [B27-C04](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md):**
- Para `ρ < ρ_t`, `P = K₁ρ^{Γ₁}`; para `ρ ≥ ρ_t`, `P = K₂ρ^{Γ₂}` con `K₂ = K₁ρ_t^{Γ₁−Γ₂}` (continuidad de `P`).
- El laboratorio comprueba ambas continuidades a `10⁻¹²`.
- 🎯 **Por qué importa:** Las estrellas de neutrones son el único laboratorio de materia más allá de la densidad nuclear. Su EOS no se conoce con precisión; las medidas de masa máxima y de radio la acotan.

📘 **Dónde se aprende** (2 clases): [B27-C04 · Ecuación de estado nuclear](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md); [B79-C01 · Conservación de masa en fluidos](../programa/clases/B79/B79-C01-conservacion-de-masa-en-fluidos/CLASE.md).

### Continuo

- Un modelo es lineal si cumple superposición (lo precisa C03), invariante si sus parámetros no cambian con el tiempo, continuo si el tiempo es una variable real `t` y discreto si solo existe en instantes `kT`.
- El continuo es la opacidad de fondo.
- El continuo es la línea base sin la banda.

💡 **Cómo se explica en la clase [B16-C01](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md):**
- El modelo de la sección 8.2 es lineal (el estado aparece solo multiplicado por constantes), invariante (`J` no cambia), continuo y de orden 2.
- Un modelo continuo describe el fenómeno; uno discreto describe lo que ve el computador de a bordo, que mide y actúa cada `T` segundos (C02).
- 🎯 **Por qué importa:** Un telescopio espacial tiene que apuntar a una estrella y mantenerse allí. El telescopio Hubble lo hace con una desviación de no más de 0,007 segundos de arco durante al menos 24 horas (fuente S2).

📘 **Dónde se aprende** (4 clases): [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md); [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B32-C10 · Normalización y modelado del continuo espectral](../programa/clases/B32/B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md); [B53-C17 · Mineralogía espectral](../programa/clases/B53/B53-C17-mineralogia-espectral/CLASE.md).

### Contracción

- La contracción (*shrinkage*) acerca cada `y_j` a la media del conjunto con peso `B_j = σ_j²/(σ_j² + τ²)`: la media posterior condicionada a `τ` es `(1 − B_j) y_j + B_j μ̂`.
- La contracción de un par de índices los iguala y suma: `Tᵢᵢ` (traza), `Tᵢⱼ bⱼ` (producto por un vector), `aᵢ bᵢ` (producto escalar).

💡 **Cómo se explica en la clase [B10-C18](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md):**
- La contracción de sus dos índices da `4 + 10 + 18 = 32 = a · b`, y la contracción de un índice con `b` da `(a ⊗ b) b = a (b · b)`.
- Paso 3 · Contracción. `δa = T δx = (2,3242 × 10⁻⁵; 0; 0) m/s²`.
- 🎯 **Por qué importa:** La gravedad no es uniforme a lo largo de un satélite: lo que está más cerca de la Tierra se acelera más que lo que está lejos, y lo que está a los lados se comprime. Con una sola derivada `dg/dr` solo describes la dirección radial; el tensor de marea describe las tres direcciones a la vez.

📘 **Dónde se aprende** (2 clases): [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md); [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md).

### Contracción de longitudes

- La contracción de longitudes dice que, en un marco donde el objeto se mueve, su longitud a lo largo del movimiento es `L = L₀/γ`.

🎯 **Por qué importa (clase B26-C03):** Los muones se producen en la alta atmósfera por rayos cósmicos, viven microsegundos y, sin embargo, llegan al suelo en cantidad. Los relojes de satélites de navegación se ajustan por el mismo efecto.

📘 **Dónde se aprende** (1 clase): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md).

### Contracción global

- La contracción global reduce el radio `ΔR/R = ε/2`, con `ε` la deformación areal.

🎯 **Por qué importa (clase B53-C12):** La flexión revela el espesor elástico de la litosfera y la contracción, el balance térmico global. La decisión central: ¿qué espesor elástico y qué acortamiento explican la deformación observada?

📘 **Dónde se aprende** (1 clase): [B53-C12 · Tectónica planetaria](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md).

### Contrachorro

- El contrachorro es el que se aleja.

💡 **Cómo se explica en la clase [B27-C11](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md):**
- Por cociente chorro/contrachorro: observacional.
- Estimar la razón de brillos entre el chorro y el contrachorro.
- ⚠️ **Error frecuente:** Olvidar el contrachorro. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un chorro que se acerca puede parecer más rápido que la luz sin violar nada, y su brillo cambia en órdenes de magnitud según el ángulo. Sin estos efectos no se pueden comparar chorros ni inferir su velocidad.

📘 **Dónde se aprende** (1 clase): [B27-C11 · Chorros relativistas](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md).

### Contracorriente

- El esquema contracorriente (*upwind*) para `u_t + c u_x = 0` con `c > 0` usa el nodo de aguas arriba: `u_i^{n+1} = u_i^n − ν (u_i^n − u_{i−1}^n)`.

💡 **Cómo se explica en la clase [B11-C14](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md):**
- Para `u_t + c u_x = 0`, el esquema contracorriente es estable si `ν = c Δt/Δx ≤ 1`: la información no puede cruzar más de una celda por paso.
- Contracorriente: para advección, orden 1, estable con `ν ≤ 1` y que difunde el pulso (suaviza la forma).
- 🎯 **Por qué importa:** Casi todo código de simulación de calor, fluidos o plasma en una malla regular usa diferencias finitas. Elegir el paso de tiempo equivocado no da un resultado ligeramente malo: da un resultado que explota.

📘 **Dónde se aprende** (1 clase): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md).

### Contraejemplo

- Un contraejemplo es un caso concreto que hace falsa una afirmación.

💡 **Cómo se explica en la clase [B10-C01](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md):**
- Contraejemplo. `W = {(x, y, 1)}`, el plano `z = 1`: `(0, 0, 0)` no está, y `(1, 0, 1) + (0, 1, 1) = (1, 1, 2)` no está.
- Contraejemplo numérico: basta uno para refutar.
- 🎯 **Por qué importa:** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Contraluz

- El contraluz es una fase mayor que `120°` (hipótesis).

💡 **Cómo se explica en la clase [B76-C18](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md):**
- Con `β = 0` solo el `30,5 %` de la órbita está al sol con buena fase; con `β` alto hay más sol pero el contraluz deja de ser el límite y la fase se limita por `β`.
- 🎯 **Por qué importa:** Una aproximación planificada de noche, o con el Sol detrás del objetivo, puede dejar ciego al sensor. La decisión central: ¿qué fracción de la órbita está al sol y con buena fase, según el ángulo `β`?

📘 **Dónde se aprende** (1 clase): [B76-C18 · Restricciones de iluminación](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md).

### Contramedida

- La contramedida es una intervención que reduce la pérdida (aquí, `δ/2`, ilustrativa).
- La contramedida es una medida para prevenir o mitigar un riesgo.

💡 **Cómo se explica en la clase [B105-C03](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md):**
- La contramedida es una suposición del modelo, no una prescripción.
- Con la mitad de `δ` (contramedida simulada) la fuerza a 180 días es 1.335,9 N.
- ⚠️ **Error frecuente:** Tomar la contramedida simulada como recomendación. Es una hipótesis del modelo (8.3).
- 🎯 **Por qué importa:** Sin carga y sin aporte adecuado, el músculo se pierde más rápido que en la Tierra. La decisión central: ¿cuánta área y cuánta fuerza quedan tras 30, 90 y 180 días, y cuánto cambia una contramedida?

📘 **Dónde se aprende** (2 clases): [B105-C03 · Atrofia muscular](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md); [B113-C05 · Intervenciones de apoyo y contramedidas conductuales](../programa/clases/B113/B113-C05-intervenciones-de-apoyo-y-contramedidas-conductuales/CLASE.md).

### Contrapeso

- El contrapeso `m_c r_c = m_t r_t`.

💡 **Cómo se explica en la clase [B43-C19](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md):**
- Un tubo de 7 kg con el centro a 0,20 m y un contrapeso de 4 kg a 0,35 m dejan un desbalance de `2,2 × 10⁻¹⁶ kg m`; el contrapeso necesario es `4,000 kg`.
- Equilibrar una montura con un contrapeso.
- 🎯 **Por qué importa:** La seguridad empieza por saber cuán grande es el riesgo. La decisión central: ¿cuánta potencia y qué temperatura aparecen en el foco, cómo se balancea la montura y cuánto polvo es aceptable?

📘 **Dónde se aprende** (1 clase): [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md).

### Contraste

- El contraste `c = (T_m/T_ef)⁴` es el cociente entre el flujo por unidad de área de la mancha y el del entorno.
- El contraste es el cociente de flujos planeta/estrella.
- El contraste WCAG es `(L₁ + 0,05)/(L₂ + 0,05)` con `L` la luminancia relativa.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C12](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md):**
- A["Mancha: radio ρ,<br/>contraste c"] --> B["Área proyectada<br/>A cos γ(t)"]
- Definir mancha, contraste y modulación rotacional.
- 🎯 **Por qué importa:** La modulación del brillo por manchas permite medir el periodo de rotación de miles de estrellas sin necesitar espectros, pero también contamina la búsqueda de exoplanetas y limita la precisión de las velocidades radiales.

📘 **Dónde se aprende** (8 clases): [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md); [B29-C06 · Imagen directa de exoplanetas](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md); [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md); [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md); [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md); [B53-C26 · Publicación de mapas geológicos planetarios: estándares y leyendas](../programa/clases/B53/B53-C26-publicacion-de-mapas-geologicos-planetarios-estandares-y-leyendas/CLASE.md) y 2 más.

### Contribución

- La contribución de `xᵢ` a la varianza combinada es `(cᵢ u(xᵢ))²` (S1, 5.1.2–5.1.3).
- Una contribución es el término `|c_i| u(x_i)`, en unidades del mensurando.
- La contribución de cada dimensión es `tᵢ²/Σt²`.

💡 **Cómo se explica en la clase [B12-C17](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md):**
- Con `u(v_e) = 60 m/s`, `u(m₀) = 5 kg`, `u(m_f) = 3 kg`: contribuciones `(0,51083·60)² = 939,3`, `(3·5)² = 225` y `(5·3)² = 225` m²/s².
- Si `v_e` se mide con 1 % (30 m/s) en vez de 2 %: contribuciones `234,9; 225; 225`, total `684,9`, `u = 26,17 m/s`, es decir, 29,8 % menos.
- 🎯 **Por qué importa:** Mejorar una medida cuesta dinero, masa o tiempo. Si el presupuesto de una misión ofrece mejorar la masa seca o el empuje específico, hay que saber cuál de las dos reduce más la incertidumbre del resultado.

📘 **Dónde se aprende** (3 clases): [B12-C17 · Análisis de sensibilidad](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md); [B13-C13 · Presupuestos de incertidumbre](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md); [B84-C16 · Tolerancias de fabricación](../programa/clases/B84/B84-C16-tolerancias-de-fabricacion/CLASE.md).

### Contribución a la varianza

- La contribución a la varianza de un factor es su `σ²` entre la suma de las `σ²` en la escala logarítmica.
- La contribución a la varianza de cada parámetro.

💡 **Cómo se explica en la clase [B33-C02](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md):**
- parametro dT/dp (h por unidad) contribucion a la varianza [h^2]
- 🎯 **Por qué importa:** Un pronóstico de llegada sin incertidumbre es engañoso. La decisión central: ¿qué parámetro domina la incertidumbre del tiempo de llegada?

📘 **Dónde se aprende** (2 clases): [B33-C02 · Modelos de propagación de CME](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md); [B67-C08 · Informe de disponibilidad de volátiles con incertidumbre](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md).

### Contribuyente

- Un contribuyente es una fuente de error con su `σ` (1σ).

💡 **Cómo se explica en la clase [B87-C22](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md):**
- Sin el mayor contribuyente (el alineamiento), el RSS bajaría a `6,12″`: el alineamiento aporta el 40 % de la varianza y es donde conviene invertir.
- *Descripción textual:* cada contribuyente se describe por su desviación; la suma cuadrática da el error total, el Monte Carlo la confirma y la comparación con el requisito da el margen; con dos ejes aparece el error radial.
- 🎯 **Por qué importa:** Un requisito de apuntamiento solo se cumple si el diseño lo respalda con números. La decisión central: ¿qué contribuyentes dominan, cómo se combinan (suma lineal o cuadrática), con qué margen se cumple el requisito y qué ocurre con dos ejes?

📘 **Dónde se aprende** (1 clase): [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md).

### Control

- Un control es una medida defensiva.
- Un control reduce la probabilidad de una hoja.

💡 **Cómo se explica en la clase [B119-C14](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md):**
- Cada control reduce a la mitad una hoja.
- Con los cuatro controles el riesgo baja a `0.04719` (`56.1 %` menos).
- 🎯 **Por qué importa:** La amenaza cibernética conecta el derecho con la seguridad operativa; el modelo defensivo de infraestructura espacial (B122-C03) lo desarrolla, y esta clase fija el razonamiento de riesgo. La decisión central: ¿qué control reduce más el riesgo residual y cuánto se gana al combinarlos?

📘 **Dónde se aprende** (2 clases): [B119-C14 · Amenazas cibernéticas a satélites](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md); [B122-C03 · Modelo defensivo de riesgos de infraestructura espacial](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md).

### Control de actitud fija

- El control de actitud fija mantiene `θ = 0`; la carga ante racha es `q·α`.

🎯 **Por qué importa (clase B77-C23):** Un vehículo inestable es controlable si el control es más rápido que la divergencia, pero el control a su vez fija las cargas ante rachas. La decisión central: ¿cuánto control hace falta para estabilizar un lanzador y qué ángulo de ataque deja una racha según la ganancia?

📘 **Dónde se aprende** (1 clase): [B77-C23 · Estabilidad de vuelo de lanzadores en ascenso](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md).

### Control de calidad

- El control de calidad (QC) acepta o rechaza el lote con criterios declarados.

💡 **Cómo se explica en la clase [B14-C30](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md):**
- Cada etapa recibe un dato con su huella, calcula la clave del resultado, y si ya existe lo reutiliza; si no, lo calcula, y si falla lo reintenta; si el control de calidad lo rechaza, detiene el lote.
- I["Ingestar"] --> V["Validar<br/>control de calidad"]
- ⚠️ **Error frecuente:** Dejar pasar un lote sin control de calidad. Se corrige con la sección 8.3 y el ejercicio 7.
- 🎯 **Por qué importa:** Cada madrugada llegan datos nuevos. Si un humano debe lanzar cada paso, tarde o temprano se olvida uno; si un lote corrupto atraviesa la cadena, contamina el producto final; si un fallo de red detiene todo y al reiniciar se repite desde cero, se pierde tiempo.

📘 **Dónde se aprende** (1 clase): [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md).

### Control PD

- El control PD usa el error y su derivada: `δ = Kp(θ_c − θ) − Kd θ̇`.

💡 **Cómo se explica en la clase [B77-C24](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md):**
- La ganancia estática es `μ_c Kp/(μ_c Kp − μ_α) = 1,4123`: el vehículo termina a `1,412` veces el comando, porque el control proporcional debe vencer además la rigidez aerodinámica negativa.
- Un control real añade integrador o realimentación de la dirección de vuelo.
- 🎯 **Por qué importa:** El control de un lanzador inestable debe ser lo bastante rápido para estabilizarlo y lo bastante suave para no saturar la tobera. La decisión central: ¿qué ganancias cumplen una especificación dada y qué ocurre cuando la demanda supera los límites del actuador?

📘 **Dónde se aprende** (1 clase): [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md).

### Control supervisado

- En control supervisado el operador da una meta de mayor alcance y el vehículo la ejecuta con autonomía.

💡 **Cómo se explica en la clase [B98-C03](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md):**
- Sin retardo, «mover y esperar» (pasos de 1 m, `v = 0,04 m/s`, 30 s de decisión por orden) tarda 1,53 h y el control supervisado (metas de 10 m, `v = 0,02 m/s`, 120 s por meta) 1,72 h: gana el manual.
- python programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/supervisado.py
- 🎯 **Por qué importa:** Ni siempre conviene más autonomía ni siempre más control manual: sin retardo, el manual puede ser más rápido. La decisión central: ¿a partir de qué retardo compensa pasar de órdenes cortas a metas supervisadas, y qué se pierde al hacerlo?

📘 **Dónde se aprende** (1 clase): [B98-C03 · Control supervisado y autonomía compartida](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md).

### Controlable

- El sistema `ẋ = A x + B u` (con `n` estados) es controlable si, desde cualquier estado inicial, existe una entrada que lo lleva a cualquier otro estado en un tiempo finito.

💡 **Cómo se explica en la clase [B16-C13](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md):**
- Con `A = [[0,1],[0,0]]`, `B = [0, 1/J]ᵀ`: `AB = [1/J, 0]ᵀ`, luego `𝒞 = [[0, 1/J],[1/J, 0]]` de rango 2: controlable.
- El sistema no lineal real, con momento almacenado, puede ser controlable de otras maneras (por ejemplo, usando el acoplamiento giroscópico); la prueba lineal no lo afirma ni lo descarta.
- ⚠️ **Error frecuente:** Confundir «controlable» con «barato». Se corrige con los ejercicios 5 y 11.
- 🎯 **Por qué importa:** Un satélite puede perder actuadores o sensores en vuelo. Antes de diseñar una ley de control conviene saber si el problema tiene solución: ninguna ley, por ingeniosa que sea, mueve un estado que ningún actuador alcanza, ni estima uno que ningún sensor ve.

📘 **Dónde se aprende** (1 clase): [B16-C13 · Observabilidad y controlabilidad](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md).

### Controlador

- Un controlador implementa la HAL para un dispositivo.
- Balance ambiental: suma de generaciones, retiros y acumulación de cada magnitud. Controlador: lazo que enciende o apaga un equipo.

💡 **Cómo se explica en la clase [B88-C24](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md):**
- HAL --> R["Controlador de registros (FIFO 4)"]
- El laboratorio ejecuta la misma aplicación en ambos controladores.
- 🎯 **Por qué importa:** Si la aplicación toca registros, no se puede probar sin el hardware y cada cambio de componente la rompe. La decisión central: ¿qué interfaz mínima expone el dispositivo para que la aplicación no dependa de él?

📘 **Dónde se aprende** (2 clases): [B88-C24 · Capa de abstracción de hardware (HAL) y controladores](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md); [B106-C20 · Proyecto de balance ambiental de hábitat](../programa/clases/B106/B106-C20-proyecto-de-balance-ambiental-de-habitat/CLASE.md).

### Controlador PD

- El controlador PD `τ = K_p e − K_d θ'`.

🎯 **Por qué importa (clase B43-C15):** El motor fija la resolución, la fuerza útil y la estabilidad del lazo. La decisión central: ¿cuánto se desvía un motor paso a paso bajo carga y qué ganancias dan una respuesta de servo sin sobreimpulso excesivo?

📘 **Dónde se aprende** (1 clase): [B43-C15 · Motores paso a paso y servomotores](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md).

### Convección

- La convección es el transporte por movimiento macroscópico del gas.

💡 **Cómo se explica en la clase [B24-C05](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md):**
- Si `∇_rad > ∇_ad`, una burbuja desplazada hacia arriba sigue siendo más caliente que su entorno, sigue subiendo y aparece convección.
- Una opacidad alta (capas externas frías) o una luminosidad alta por unidad de masa (núcleos de estrellas masivas) empujan a la convección.
- 🎯 **Por qué importa:** La energía generada en el núcleo tarda milenios en salir y el modo de transporte decide la estructura: si el interior de una estrella es convectivo, su composición se mezcla; si es radiativo, no. De ello depende cuánto combustible alcanza el núcleo, y por tanto la vida de la estrella.

📘 **Dónde se aprende** (1 clase): [B24-C05 · Transporte radiativo y convectivo](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md).

### Convección natural

- La convección natural se apaga si `Ra` es menor que el valor crítico, aquí `1708`.
- La convección natural depende de la flotabilidad; en microgravedad `h_c ≈ 0` sin ventilación.

💡 **Cómo se explica en la clase [B85-C03](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md):**
- Descripción larga: la convección natural a 1 atm equivale a la radiación; con la presión a la décima parte, `Ra` cae cien veces, y con microgravedad desaparece aunque haya aire.
- Hallar la presión a la que la convección natural se apaga (`Ra = 1708`).
- 🎯 **Por qué importa:** Un equipo que se enfría bien sobre la mesa puede sobrecalentarse en vacío y en microgravedad. La decisión central: ¿cuánto del enfriamiento de un equipo se pierde al quitar la convección y qué queda para sustituirla?

📘 **Dónde se aprende** (2 clases): [B85-C03 · Convección y ausencia de convección exterior](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md); [B105-C23 · Termorregulación humana en vuelo](../programa/clases/B105/B105-C23-termorregulacion-humana-en-vuelo/CLASE.md).

### Convención

- Una convención es un acuerdo que no se deduce de la naturaleza: el umbral de 20 000 km lo es.

💡 **Cómo se explica en la clase [B07-C04](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md):**
- Se acepta cualquier umbral declarado como convención.
- 🎯 **Por qué importa:** Toda clasificación astronómica es una decisión sobre un dato: ¿esta señal supera el ruido?, ¿esta estrella es más brillante que el umbral?, ¿esta imagen está saturada? Una decisión mal escrita no falla ruidosamente: clasifica mal en silencio, justo en los casos frontera, que son los que importan.

📘 **Dónde se aprende** (1 clase): [B07-C04 · Condicionales y decisiones](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md).

### Convención de signo

- Una convención de signo es el acuerdo sobre qué sentido es positivo.

💡 **Cómo se explica en la clase [B03-C09](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md):**
- Para magnitudes que no pueden ser negativas (masa, distancia) un signo menos indica un error de datos, no una convención.
- La evidencia es el registro de signos y convenciones del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Cuando observas una llamarada solar a las 12:00:00, el evento ocurrió antes: su tiempo es el observado menos 499 s. Si sumas en vez de restar, afirmas que la llamarada ocurre en el futuro.

📘 **Dónde se aprende** (1 clase): [B03-C09 · Operaciones con números negativos](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md).

### Convención de suma de Einstein

- La convención de suma de Einstein dice que un índice repetido en un término se suma de 1 a 3: `aᵢ bᵢ = Σ aᵢ bᵢ`.

🎯 **Por qué importa (clase B10-C17):** La inercia de un satélite frente a un giro depende de la dirección: se necesita nueve números ordenados en una matriz, y esos nueve números cambian si cambias los ejes del cuerpo, pero de forma que la física no cambie.

📘 **Dónde se aprende** (1 clase): [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md).

### Convenio de signos

- El convenio de signos aquí es el de `U` positivo, con `J_n` positivo para un achatamiento ecuatorial.

💡 **Cómo se explica en la clase [B72-C02](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md):**
- Dos códigos que usen radios o convenios de signo distintos para `J2` no son comparables.
- ⚠️ **Error frecuente:** Mezclar el convenio de signos del potencial. Se corrige con la sección 10: aquí `U` es positivo.
- 🎯 **Por qué importa:** Sin un potencial no hay perturbación gravitatoria que calcular, y los números de la bibliografía (J2, J3, J4) dependen de un convenio de signos y de un radio de referencia. La decisión central: ¿qué términos del potencial incluir y con qué radio y convenio, para que J2 signifique lo mismo en tu código y en la fuente?

📘 **Dónde se aprende** (1 clase): [B72-C02 · Potencial gravitatorio no esférico](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md).

### Convergencia

- La convergencia de un integrador es la reducción del error al disminuir el paso; su orden `p` cumple `error ∝ h^p`.
- Un calentamiento (*warm-up*) son las primeras iteraciones, que se descartan. Convergencia significa que las cadenas muestrean la misma distribución estacionaria, la posterior; no es una propiedad que se demuestre, solo que se detecta su ausencia.
- La convergencia es la reducción del error al refinar la malla.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C19](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md):**
- (c) el orden de convergencia: el error a `t = 20 s` es 4,1×10⁻⁹ con `h = 0,4`, 1,4×10⁻¹⁰ con 0,2 y 5,3×10⁻¹² con 0,1; los órdenes son 4,89 y 4,71, es decir, al menos 4, como corresponde a RK4.
- Verificar el integrador: coincidencia con una fórmula y orden de convergencia.
- 🎯 **Por qué importa:** Un lazo que «se ve bien» en una simulación puede estar mal por tres razones: el diseño no cumple un requisito en parte del rango de parámetros, la discretización en el computador de vuelo cambia el comportamiento, o el simulador tiene un error numérico.

📘 **Dónde se aprende** (5 clases): [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md); [B39-C06 · Introducción a la relatividad numérica: formalismo 3+1](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md); [B73-C20 · Proyecto de integración celeste de precisión](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md); [B116-C03 · Historia clínica remota y registros médicos de misión](../programa/clases/B116/B116-C03-historia-clinica-remota-y-registros-medicos-de-mision/CLASE.md).

### Convergencia en el paso

- La convergencia en el paso es la estabilización del resultado al reducir `Δt`.

💡 **Cómo se explica en la clase [B77-C20](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md):**
- Comprobar la convergencia al reducir el paso (RK4).
- El script [simulacion.py](simulacion.py) integra el ascenso con `Cd(M)`, registra eventos, cierra el presupuesto de pérdidas y estudia la convergencia con tres pasos (comprueba residuo < 1e-6, cambios decrecientes y conservación < 1e-8).
- 🎯 **Por qué importa:** Una simulación solo vale si se sabe cuánto error numérico tiene y a dónde va cada metro por segundo. La decisión central: ¿cómo se verifica que una simulación de vuelo es numéricamente fiable y cómo se lee su presupuesto de pérdidas?

📘 **Dónde se aprende** (1 clase): [B77-C20 · Simulación académica de una trayectoria de vuelo](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md).

### Convergencia espectral

- La convergencia espectral (o exponencial) es un error que decae como `e^{−c N}`.

💡 **Cómo se explica en la clase [B11-C16](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md):**
- Espectral: convergencia exponencial en dominios simples con soluciones suaves; delicado con saltos y con condiciones de borde no periódicas.
- 🎯 **Por qué importa:** Cuando la solución es suave y periódica —una señal a lo largo de una órbita, un perfil de temperatura alrededor de un vehículo que gira, el campo en una caja periódica—, un método espectral logra con 24 puntos lo que unas diferencias finitas lograrían con millones.

📘 **Dónde se aprende** (1 clase): [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md).

### Convergencia exponencial

- La convergencia exponencial es un error `~ e^{−c N}` si la solución es analítica.

💡 **Cómo se explica en la clase [B11-C24](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md):**
- Medir la convergencia exponencial frente a diferencias finitas.
- Chebyshev agrupa nodos en los bordes y ayuda, pero la capa muy delgada exige muchos nodos o un cambio de variable; la convergencia exponencial solo aparece cuando `N` resuelve la capa.
- ⚠️ **Error frecuente:** Esperar convergencia exponencial con funciones no analíticas. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Cuando la solución es suave, un método espectral reduce un problema que necesita miles de puntos con diferencias a una docena con Chebyshev. Pero tiene un costo: el paso máximo estable de un esquema explícito baja como `1/N⁴`, y funciona mal si la solución no es suave.

📘 **Dónde se aprende** (1 clase): [B11-C24 · Métodos espectrales avanzados (Chebyshev y Fourier)](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md).

### Conversación en tiempo real

- La conversación en tiempo real exige retardos pequeños.

💡 **Cómo se explica en la clase [B113-C03](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md):**
- Distinguir conversación en tiempo real de mensajes asincrónicos.
- 🎯 **Por qué importa:** Ninguna clase trata el efecto del retardo en el apoyo psicológico. La decisión central: ¿qué formatos de apoyo siguen siendo posibles cuando una respuesta tarda decenas de minutos?

📘 **Dónde se aprende** (1 clase): [B113-C03 · Comunicación diferida y soporte psicológico a distancia](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md).

### Conversión

- Una conversión (o *cast*) transforma un valor de un tipo a otro.
- Una conversión cambia la unidad sin cambiar la cantidad física.

💡 **Cómo se explica en la clase [B07-C02](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md):**
- Imprime cada variable con su tipo y añade al menos tres `assert` que comprueben los tipos y una conversión.
- Antes de imprimir ejecuta pruebas: tipos esperados, `0.1 + 0.2 != 0.3` y `isclose`, división real/entera/resto, conversiones de texto, `True + True == 2` y consistencia de la masa en notación científica y diámetro = 2 × radio.
- 🎯 **Por qué importa:** Un dato sin tipo es ambiguo: «12756» puede ser un número con el que calculas o un texto que lees de un archivo. Si el programa los confunde, falla o, peor, da un resultado plausible pero erróneo.

📘 **Dónde se aprende** (2 clases): [B07-C02 · Tipos de datos y variables](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### Conversión AB

- La conversión AB es `m_AB = −2,5 log₁₀(f/3631 Jy)`.

💡 **Cómo se explica en la clase [B45-C21](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md):**
- Conversión AB: 3631,0 Jy → -0,000, 363,1 Jy → 2,500, 1,0 Jy → 8,900, 0,001 Jy → 16,400.
- 🎯 **Por qué importa:** Sin estándares la escala de un cielo concreto es arbitraria. La decisión central: ¿qué ecuación de transformación se ajusta y con qué error en la magnitud final?

📘 **Dónde se aprende** (1 clase): [B45-C21 · Estándares fotométricos y sistemas de referencia](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md).

### Conversión ida y vuelta

- La conversión ida y vuelta es la prueba `estado → elementos → estado`.

💡 **Cómo se explica en la clase [B72-C12](../programa/clases/B72/B72-C12-variaciones-de-elementos-osculadores/CLASE.md):**
- Comprobar la conversión con un error de ida y vuelta de `10⁻¹⁵`.
- 🎯 **Por qué importa:** Un catálogo publica elementos de un instante; usarlos como si fueran constantes introduce errores de kilómetros. La decisión central: ¿cuánto difiere un elemento osculador del medio y qué error de fase o de periodo produce usar el equivocado?

📘 **Dónde se aprende** (1 clase): [B72-C12 · Variaciones de elementos osculadores](../programa/clases/B72/B72-C12-variaciones-de-elementos-osculadores/CLASE.md).

### Conversión superficie–frente de onda

- La conversión superficie–frente de onda es `2 cos θ` en un espejo y `(n − 1)` en una cara refractiva con aire.

🎯 **Por qué importa (clase B50-C15):** El requisito de un instrumento se cumple o no según cómo se reparta el error entre diseño, fabricación y alineación. La decisión central: ¿cuánto frente de onda se puede gastar en cada etapa sin superar el requisito?

📘 **Dónde se aprende** (1 clase): [B50-C15 · Presupuesto de error de frente de onda de un instrumento](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md).

### Convolución

- La convolución de `x` y `h` es `(x ∗ h)[n] = Σ_m x[m] h[n − m]` (la definición de NumPy en S2 es la misma con otro orden de nombres: se voltea una secuencia y se desliza sobre la otra).
- La convolución de `h` y `u` es `(h∗u)(t) = ∫₀ᵗ h(t−s) u(s) ds` (fuente S2).
- La convolución (en redes, una correlación cruzada: producto punto de un núcleo con cada ventana de la imagen, sin invertir el núcleo) produce un mapa de respuestas; en modo válido la salida mide `N − k + 1` por lado.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- Resulta `y[n] = Σ_m x[m] h[n − m]`: la convolución.
- La media móvil de C07 es la convolución con `h[m] = 1/M`.
- ⚠️ **Error frecuente:** Multiplicar DFT sin rellenar y creer que se obtiene la convolución lineal. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.

📘 **Dónde se aprende** (7 clases): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md); [B32-C06 · Micro y macroturbulencia y granulación estelar](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md); [B32-C11 · Ensanchamiento rotacional y v sin i](../programa/clases/B32/B32-C11-ensanchamiento-rotacional-y-v-sin-i/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md) y 1 más.

### Convolución circular

- La convolución circular es la que implícitamente calcula el producto de DFT: supone que las series se repiten.

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- El teorema de convolución (S1, §1.14, la propiedad de convolución: la transformada de `f ∗ g` es el producto de las transformadas, con la normalización de S1) tiene una versión discreta: la DFT de la convolución circular es el producto de las DFT.
- No: obtiene la convolución circular; el laboratorio da una desviación máxima de `2,75` respecto a la lineal.
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.

📘 **Dónde se aprende** (1 clase): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md).

### Coordenada

- La coordenada `r` se define de modo que una circunferencia mide `2πr`.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- Entre `R☉` y `2R☉`, `s = 6,957 010 × 10⁸ m`, `1023,52 m` más que la diferencia de coordenadas `6,957 × 10⁸ m`.
- *Descripción textual:* la masa fija `r_s`; el factor `1 − r_s/r` aparece en la métrica; la distancia propia radial integra su raíz inversa y resulta mayor que la diferencia de coordenadas.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### Coordenadas

- Las coordenadas de `v` en la base `{b₁, …, b_n}` son los números `c_k` tales que `v = Σ c_k b_k`.

💡 **Cómo se explica en la clase [B10-C02](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md):**
- En `ℝ³` la base canónica es `{(1,0,0), (0,1,0), (0,0,1)}` y las coordenadas son las componentes habituales.
- Una base ortonormal es cómoda (coordenadas por producto escalar) y numéricamente estable.
- ⚠️ **Error frecuente:** Pensar que las coordenadas son el vector. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Un vector es una entidad geométrica; sus «componentes» dependen de los ejes que elijas. Un operador de estación terrestre describe un satélite con ejes ligados al ecuador; el satélite mismo, con ejes ligados a su órbita; un instrumento, con ejes del instrumento.

📘 **Dónde se aprende** (1 clase): [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md).

### Coordenadas cartesianas

- Las coordenadas cartesianas `(x, y)` dan la posición por las distancias a dos ejes perpendiculares.

💡 **Cómo se explica en la clase [B04-C10](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md):**
- python programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/polares_y_orbita.py
- 🎯 **Por qué importa:** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.

📘 **Dónde se aprende** (1 clase): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md).

### Coordenadas esféricas

- Las coordenadas esféricas dan un punto del espacio por su distancia `r` al origen y dos ángulos.

💡 **Cómo se explica en la clase [B04-C11](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md):**
- Definir coordenadas esféricas `(r, θ, φ)` y su convención de ángulos.
- python programa/clases/B04/B04-C11-coordenadas-esfericas/direcciones_esfericas.py
- 🎯 **Por qué importa:** Un catálogo de estrellas da para cada una dos números: dónde está en el cielo. Pero un programa que cruza catálogos, calcula separaciones o apunta un telescopio no trabaja con horas y grados: trabaja con vectores.

📘 **Dónde se aprende** (1 clase): [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md).

### Coordenadas estándar

- Las coordenadas estándar `(ξ, η)` son las del plano.

💡 **Cómo se explica en la clase [B58-C06](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md):**
- *Descripción textual:* las estrellas de referencia fijan por mínimos cuadrados las constantes que llevan los píxeles a coordenadas estándar; la proyección inversa da la ascensión recta y la declinación.
- 🎯 **Por qué importa:** Una órbita no puede ser mejor que sus posiciones: un error de décimas de segundo de arco se amplifica al propagar. La decisión central: ¿con qué exactitud puedo asignar coordenadas a un objeto en una imagen y qué la limita?

📘 **Dónde se aprende** (1 clase): [B58-C06 · Astrometría de objetos menores](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md).

### Coordenadas generalizadas

- Las coordenadas generalizadas `q = (q₁, q₂)` son los ángulos de las articulaciones, medidos desde la horizontal.

🎯 **Por qué importa (clase B102-C01):** Un manipulador de un rover se diseña y se ensaya en la Tierra, pero trabaja en Marte o en la Luna. La decisión central: ¿qué par necesita cada articulación en otro cuerpo, y qué cambia además del par?

📘 **Dónde se aprende** (1 clase): [B102-C01 · Dinámica multicuerpo de rovers y manipuladores](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md).

### Coordenadas ICRS

- Las coordenadas ICRS `(α, δ)` son ascensión recta y declinación respecto de esos ejes.

🎯 **Por qué importa (clase B13-C21):** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.

📘 **Dónde se aprende** (1 clase): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### Coordenadas polares

- Las coordenadas polares `(r, θ)` la dan por la distancia `r` a un origen (el polo) y el ángulo `θ` medido desde un eje polar.

💡 **Cómo se explica en la clase [B04-C10](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md):**
- python programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/polares_y_orbita.py
- 🎯 **Por qué importa:** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.

📘 **Dónde se aprende** (1 clase): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md).

### Coordenadas (u, v, w)

- Las coordenadas `(u, v, w)` están en longitudes de onda y miran a la fuente (`w` hacia ella).

🎯 **Por qué importa (clase B46-C14):** La línea de base fija la escala angular que se ve y el retardo que hay que compensar. La decisión central: ¿qué punto del plano `uv` y qué retardo corresponden a una línea de base y a una dirección?

📘 **Dónde se aprende** (1 clase): [B46-C14 · Líneas de base interferométricas](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md).

### Coordinación

- La coordinación es la negociación con administraciones cuyos servicios pueden verse afectados.
- La coordinación busca evitar interferencia entre sistemas.

💡 **Cómo se explica en la clase [B119-C09](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md):**
- La UIT-R examina, coordina, inscribe y ayuda con las interferencias; los criterios numéricos quedan como «no consultados».
- N["Notificación a la UIT"] --> C["Coordinación"]
- 🎯 **Por qué importa:** Ninguna clase anterior vincula el derecho de telecomunicaciones con el cálculo de interferencia; B120 trata licencias y espectro en detalle y esta clase fija el marco.

📘 **Dónde se aprende** (2 clases): [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md); [B120-C01 · Licencias satelitales y procedimiento de notificación](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md).

### Copa de Faraday

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C24):** La energía por carga elegida por el analizador determina qué se mide; la resolución de los canales limita la temperatura que se recupera. La decisión central: ¿cuántos canales y qué corrección dan la velocidad y la temperatura del plasma con error aceptable?

📘 **Dónde se aprende** (1 clase): [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md).

### Copia

- Una vista es un arreglo que mira los mismos datos que otro sin copiarlos; una copia tiene datos propios.

💡 **Cómo se explica en la clase [B14-C02](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md):**
- Indexar con una lista de posiciones `est[[0, 1]]` crea una copia.
- Distinguir si una operación devuelve una vista o una copia, y por qué importa.
- ⚠️ **Error frecuente:** Confundir vista y copia. Se corrige con los ejercicios 5 y 11.
- 🎯 **Por qué importa:** Una constelación de seis satélites y cinco estaciones en tierra producen treinta distancias. Un catálogo de estrellas produce millones.

📘 **Dónde se aprende** (1 clase): [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md).

### COPUOS

- COPUOS es la Comisión sobre la Utilización del Espacio Ultraterrestre con Fines Pacíficos.

💡 **Cómo se explica en la clase [B119-C06](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md):**
- *Descripción textual:* la Asamblea crea COPUOS; este tiene dos subcomités y una secretaría; decide por consenso, lo que da poder de bloqueo a cada miembro.
- Según el resumen de búsqueda de las páginas de UNOOSA (2026-11-11), la Asamblea General creó COPUOS como órgano ad hoc con 18 miembros por la res. 1348 (XIII) del 13-12-1958 y lo hizo permanente por la res. 1472 (XIV) del 12-12-1959; tiene un Subcomité Científico y Técnico y un Subcomité Jurídico, y UNOOSA es su secretaría.
- ⚠️ **Error frecuente:** Atribuir la decisión a UNOOSA y no a COPUOS. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** Quien estudia el derecho espacial necesita saber dónde se negocia y cómo se decide; ninguna clase anterior trata los organismos. La decisión central: ¿cómo cambia la probabilidad de bloqueo cuando crece el número de miembros que deben consentir?

📘 **Dónde se aprende** (1 clase): [B119-C06 · Organismos UNOOSA y COPUOS](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md).

### Cordón

- El cordón es el material depositado; su ancho es `w`.

💡 **Cómo se explica en la clase [B59-C13](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md):**
- Una cúpula hemisférica de 3,0 m de radio exterior y 0,30 m de pared, con cordón de 5 cm y velocidad 0,10 m/s (todo ilustrativo).
- 🎯 **Por qué importa:** Una capa más fina da mejor forma pero más tiempo; y una cúpula tiene una zona alta que no se puede imprimir sin apoyo. La decisión central: ¿qué grosor de capa y qué perfil de cúpula hacen viable la impresión?

📘 **Dónde se aprende** (1 clase): [B59-C13 · Impresión 3D extraterrestre](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md).

### Cordón de seguridad

- El cordón de seguridad ata a la persona a un anclaje; limita la distancia al anclaje.

🎯 **Por qué importa (clase B108-C02):** Ninguna clase planifica rutas y accesibilidad de una EVA en una estructura. La decisión central: ¿por qué asideros pasa la persona, cuánto tarda y qué restricciones (alcance, cordón) pueden dejar un puesto inaccesible?

📘 **Dónde se aprende** (1 clase): [B108-C02 · Planificación de desplazamientos y rutas de EVA](../programa/clases/B108/B108-C02-planificacion-de-desplazamientos-y-rutas-de-eva/CLASE.md).

### Coriolis y centrífugo

- El término de Coriolis y centrífugo `C(q, q̇) q̇` aparece al girar varias articulaciones a la vez.

🎯 **Por qué importa (clase B102-C01):** Un manipulador de un rover se diseña y se ensaya en la Tierra, pero trabaja en Marte o en la Luna. La decisión central: ¿qué par necesita cada articulación en otro cuerpo, y qué cambia además del par?

📘 **Dónde se aprende** (1 clase): [B102-C01 · Dinámica multicuerpo de rovers y manipuladores](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md).

### Corona

- La fotosfera es la capa que emite la luz visible; la cromosfera y la corona están encima.
- Una corona es una estructura circular asociada a procesos del manto (concepto; no se calcula aquí).

💡 **Cómo se explica en la clase [B30-C02](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md):**
- Para la corona de `1,5 × 10⁶ K` el exponente en el infinito es `GMμu/(kTR) = 9,18`.
- La corona, 260 veces más caliente que la fotosfera, es un gas que se extiende tanto que su presión a gran distancia no desaparece.
- 🎯 **Por qué importa:** La corona caliente es el origen del viento solar y de gran parte de la actividad. Entender por qué no puede estar en reposo conecta el Sol con el medio interplanetario.

📘 **Dónde se aprende** (2 clases): [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md); [B70-C05 · Actividad volcánica venusina: llanuras, coronas e indicios de actividad reciente](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md).

### Coronógrafo

- El coronógrafo bloquea el disco solar para ver la corona.

💡 **Cómo se explica en la clase [B30-C13](../programa/clases/B30/B30-C13-eyecciones-de-masa-coronal/CLASE.md):**
- Las eyecciones de masa se observan con coronógrafos; un estudio de 909 CME de tipo *streamer-blowout* con LASCO/C2 forma parte del contexto (S3, solo resumen).
- 🎯 **Por qué importa:** Saber cuándo llegará una CME determina el margen de alerta. La decisión central: ¿cuánto tarda en llegar y cuánto depende ese tiempo del arrastre?

📘 **Dónde se aprende** (1 clase): [B30-C13 · Eyecciones de masa coronal](../programa/clases/B30/B30-C13-eyecciones-de-masa-coronal/CLASE.md).

### Corpus

- El corpus guarda entradas que descubren ramas nuevas.

💡 **Cómo se explica en la clase [B88-C37](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md):**
- C["Corpus de semillas"] --> M["Mutar una entrada"]
- *Descripción textual:* se muta una entrada del corpus y se ejecuta el objetivo; las excepciones se registran y las entradas que abren ramas nuevas pasan al corpus.
- 🎯 **Por qué importa:** Las pruebas diseñadas por una persona no prevén todas las combinaciones. La decisión central: ¿qué estrategia de entradas encuentra más fallos con menos ejecuciones en un banco autorizado?

📘 **Dónde se aprende** (1 clase): [B88-C37 · Fuzzing autorizado de software embarcado en banco de pruebas](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md).

### Corrección

- La corrección es el valor que se suma para compensar un sesgo conocido.
- La corrección en el instante `t` es `dv(t) = −Φ_rv(T,t)⁻¹ [Φ_rr(T,t) δr(t) + Φ_rv(T,t) δv(t)]`.
- La detección es que el error se advierta; la corrección, que se acepte y se repare.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C04](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md):**
- La corrección resultante hereda esa incertidumbre;
- *Descripción textual:* una lectura se descompone en verdad, sesgo y ruido; el promedio solo reduce el ruido; el sesgo se elimina con una corrección obtenida de un patrón.
- 🎯 **Por qué importa:** Una estación mide el instante de llegada de un pulso de una baliza. Cada lectura fluctúa por ruido electrónico, y además hay un retardo constante del cable que nadie incluyó.

📘 **Dónde se aprende** (6 clases): [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B74-C08 · Filtrado recursivo de estados](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md); [B81-C15 · Robustez de trayectoria ante fallas](../programa/clases/B81/B81-C15-robustez-de-trayectoria-ante-fallas/CLASE.md); [B104-C07 · Factores de liderazgo](../programa/clases/B104/B104-C07-factores-de-liderazgo/CLASE.md); [B104-C12 · Robótica tripulada](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md).

### Corrección atmosférica

- La corrección atmosférica convierte `ρ_TOA` en `ρ_s`.

💡 **Cómo se explica en la clase [B57-C26](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md):**
- La evidencia es la ficha de corrección atmosférica del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de corrección atmosférica*: la tabla de reflectancias del suelo, el TOA y la corregida, el sesgo del NDVI y el error del objeto oscuro y de un `τ` mal estimado.
- 🎯 **Por qué importa:** Comparar imágenes de fechas distintas con atmósferas distintas confunde atmósfera con cambio. La decisión central: ¿cuánto sesga la atmósfera y cómo se estima y descuenta con la información disponible?

📘 **Dónde se aprende** (1 clase): [B57-C26 · Corrección atmosférica de imágenes](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md).

### Corrección baricéntrica

- La corrección baricéntrica quita el movimiento de la Tierra.

💡 **Cómo se explica en la clase [B45-C12](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Qué es la corrección baricéntrica?
- ⚠️ **Error frecuente:** Olvidar la corrección baricéntrica. Se corrige con 8.3.
- 🎯 **Por qué importa:** Las velocidades radiales descubren planetas, binarias y la expansión del universo. La decisión central: ¿cómo se pasa de un corrimiento a una velocidad y con qué precisión?

📘 **Dónde se aprende** (1 clase): [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md).

### Corrección de Bonferroni

- La corrección de Bonferroni usa `α/k` por prueba.
- La corrección de Bonferroni divide `α` entre el número de pruebas.
- Las comparaciones múltiples inflan `α`; la corrección de Bonferroni usa `α/m`.

💡 **Cómo se explica en la clase [B14-C23](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md):**
- Aplicar la corrección de Bonferroni y explicar su coste.
- 🎯 **Por qué importa:** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.

📘 **Dónde se aprende** (3 clases): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md); [B105-C20 · Diseño de protocolo médico simulado](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md).

### Corrección de flujo

- La corrección de flujo (*refluxing*) reemplaza el flujo grueso en una interfaz por el flujo fino.

💡 **Cómo se explica en la clase [B21-C05](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md):**
- Paso 4 · Corrección de flujo. Sea la advección con `a = 1`, `ν = 0,8` y una celda gruesa a la izquierda del parche con `u_viejo = 1,0`.
- Explicar el subciclado y la corrección de flujo en las interfaces grueso–fino.
- 🎯 **Por qué importa:** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Corrección de primer orden

- La corrección de primer orden por sesgo usa el jacobiano `J = ∂Δ/∂b` evaluado en el sesgo de linealización.

🎯 **Por qué importa (clase B80-C09):** B87-C06 trata los giroscopios; falta la integración conjunta de acelerómetros y giroscopios para estimar el movimiento de un robot y su deriva. La decisión central: ¿cómo se reutiliza una integración inercial cuando cambian el estado inicial y los sesgos estimados?

📘 **Dónde se aprende** (1 clase): [B80-C09 · Odometría inercial y preintegración de IMU](../programa/clases/B80/B80-C09-odometria-inercial-y-preintegracion-de-imu/CLASE.md).

### Corrección de sesgo

- La corrección de sesgo resta el aporte esperado del ruido.

💡 **Cómo se explica en la clase [B103-C04](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md):**
- Con el ruido ilustrativo `σ_h = 0,0005 r²` (5 cm a 10 m), el clasificador bruto deja pasar solo 27 peligros de 22 144, pero da un 99,4 % de falsas alarmas entre 10 y 15 m; con corrección de sesgo, las falsas alarmas bajan a 0,6 % pero se pierde el 72,9 % de los peligros en esa banda.
- El script [traversabilidad.py](traversabilidad.py) genera un MDE con rocas, calcula pendiente, escalón y rugosidad en ventanas, clasifica con y sin corrección de sesgo y muestra la matriz de confusión por rango (comprueba 0 errores sin ruido y el compromiso entre falsos «seguro» y falsas alarmas).
- 🎯 **Por qué importa:** El ruido del MDE crece con el cuadrado del rango y, a partir de cierta distancia, la señal de un obstáculo queda por debajo del ruido. La decisión central: ¿hasta qué rango se puede clasificar el terreno de forma útil, y qué política (conservadora o corregida) elegir más allá?

📘 **Dónde se aprende** (1 clase): [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Corrección de Van Vleck

- La corrección de Van Vleck: `ρ = sin(π ρ_q/2)` para 1 bit.

💡 **Cómo se explica en la clase [B51-C12](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md):**
- Aplicar la corrección de Van Vleck para 1 bit.
- El script [formatos_de_datos.py](formatos_de_datos.py) cuantiza, corrige, empaqueta y arma una cabecera (comprueba `η` a 0,01, la corrección de Van Vleck a tres errores estándar y la ida y vuelta exacta).
- 🎯 **Por qué importa:** La elección de bits y de formato fija cuánta sensibilidad se pierde y cuánto disco y red se necesitan. La decisión central: ¿cuántos bits por muestra, qué eficiencia se obtiene y cómo se empaqueta sin perder información?

📘 **Dónde se aprende** (1 clase): [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md).

### Corrección determinista

- La corrección determinista busca `g * t ≈ error`.

🎯 **Por qué importa (clase B43-C05):** Pulir es controlar un retiro de décimas de micrón: sin un modelo se oscila entre sobrecorregir y subcorregir. La decisión central: ¿cuánto hay que retirar de la mejor esfera para obtener un paraboloide y cuánto tiempo debe permanecer la herramienta en cada zona?

📘 **Dónde se aprende** (1 clase): [B43-C05 · Pulido óptico](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md).

### Corrección diferencial

- La corrección diferencial ajusta `v_y0` hasta anular `vx` en el cruce.
- La corrección diferencial ajusta el estado inicial hasta que la órbita se cierre.

💡 **Cómo se explica en la clase [B76-C05](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md):**
- Aplicar la corrección diferencial de Newton sobre `x0` y `vy0`.
- 🎯 **Por qué importa:** La NRHO es la órbita de referencia publicada para la estación Gateway. La decisión central: ¿cómo se calcula una órbita periódica inestable y qué tan cerca queda un modelo simple de la referencia en un modelo de efemérides?

📘 **Dónde se aprende** (2 clases): [B73-C05 · Órbitas periódicas](../programa/clases/B73/B73-C05-orbitas-periodicas/CLASE.md); [B76-C05 · Órbitas NRHO](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md).

### Corrección norte-sur

- La corrección norte-sur es la maniobra que devuelve la inclinación a cero.

🎯 **Por qué importa (clase B72-C10):** Un satélite geoestacionario sin maniobras de inclinación deriva de su plano ecuatorial algo menos de un grado por año, y el combustible de ese mantenimiento fija su vida útil. La decisión central: ¿cuánto contribuye cada cuerpo a la deriva de la inclinación y cuánto de ese resultado depende de simplificar la órbita lunar?

📘 **Dónde se aprende** (1 clase): [B72-C10 · Perturbaciones lunares](../programa/clases/B72/B72-C10-perturbaciones-lunares/CLASE.md).

### Correcto pero insuficiente

- Un requisito puede ser correcto pero insuficiente si no cubre un escenario de uso.

🎯 **Por qué importa (clase B83-C17):** Un proyecto puede pasar todas las pruebas de requisitos y fracasar en el uso. La decisión central: ¿además de cumplir los requisitos, el sistema satisface la necesidad en las condiciones reales de uso?

📘 **Dónde se aprende** (1 clase): [B83-C17 · Verificación frente a validación](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md).

### Corrector

- `s_{k+1} = s_k + (h/2)(k₁ + k₂)` (corrector).

💡 **Cómo se explica en la clase [B11-C06](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md):**
- Aplicar a mano el método de Heun (predictor y corrector).
- Heun existe precisamente por el corrector.
- 🎯 **Por qué importa:** Una evaluación de `F` en un cálculo de trayectorias es cara cuando incluye gravedad de varios cuerpos o un modelo de atmósfera. La pregunta práctica es siempre cuánta precisión compra cada evaluación.

📘 **Dónde se aprende** (1 clase): [B11-C06 · Método de Heun](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md).

### Corrector de coma

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C20](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md):**
- El cálculo muestra que el espejo y el plano cumplen, pero que el instrumento no cubre el sensor completo sin un corrector de coma: la conclusión del diseño no es «todo cumple» sino qué hay que añadir.
- La conclusión importante: la coma en el borde del sensor es `100,57 µm`, unas `30` veces el radio de Airy: se necesita un corrector.
- 🎯 **Por qué importa:** Un diseño es un conjunto de compromisos. La decisión central: ¿qué apertura y qué focal cumplen el objetivo y qué defecto domina?

📘 **Dónde se aprende** (1 clase): [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md).

### Corredor de aerofrenado

- El corredor de aerofrenado es el rango de altitudes de periapsis útiles.

🎯 **Por qué importa (clase B75-C15):** Cada pasada baja el apoapsis un poco, y hace falta algún margen de seguridad con la densidad. La decisión central: ¿cuántas pasadas y cuánto tiempo hacen falta para bajar el apoapsis, y qué delta-v propulsivo se ahorra?

📘 **Dónde se aprende** (1 clase): [B75-C15 · Aerofrenado conceptual](../programa/clases/B75/B75-C15-aerofrenado-conceptual/CLASE.md).

### Corredor de entrada

- El corredor de entrada es el intervalo de ángulos de entrada aceptables.

💡 **Cómo se explica en la clase [B77-C25](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md):**
- *Descripción textual:* para cada ángulo de entrada se simula el paso por la atmósfera; el máximo de desaceleración da el límite empinado y el apogeo de salida da el somero; su diferencia es el corredor, que la sustentación ensancha.
- La evidencia es la ficha de corredor de entrada del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** El corredor es la tolerancia que se le deja a la navegación y a la guía antes de entrar. La decisión central: ¿entre qué ángulos puede entrar el vehículo, cuánto ensancha el corredor la sustentación y cuándo falla la estimación de Allen–Eggers?

📘 **Dónde se aprende** (1 clase): [B77-C25 · Corredores de entrada y límites de trayectoria](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md).

### Correlación

- La correlación `ρ` entre dos medidas cambia la incertidumbre combinada: `σ² = 1/(1ᵀC⁻¹1)`.
- La correlación de Pearson.
- Ruido: error independiente de cada revisor. Correlación: acuerdo lineal entre nota y mérito.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B26-C21](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md):**
- Con dos medidas de `σ = 0,018` y `0,015` y correlación `ρ`, la incertidumbre combinada es `0,01152` si `ρ = 0`, `0,01400` si `ρ = 0,5` y `0,01483` si `ρ = 0,9`: la correlación quita información.
- Incluir una correlación entre dos medidas.
- 🎯 **Por qué importa:** Ninguna sonda fija sola todos los parámetros; combinarlas reduce la incertidumbre, pero solo si son compatibles entre sí y si se tratan bien sus correlaciones. La decisión central: dadas tres restricciones sobre `Ω_m`, ¿cuál es el valor combinado, qué incertidumbre tiene y son consistentes entre sí?

📘 **Dónde se aprende** (7 clases): [B26-C21 · Verosimilitud cosmológica con datos combinados](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md); [B33-C01 · Validación de modelos MHD con eventos solares documentados](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md); [B34-C07 · Comparación de modelos coronales con observaciones](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md); [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md); [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md) y 1 más.

### Correlación cruzada

- La correlación cruzada mide cuánto se parecen dos imágenes al desplazarlas.
- La correlación cruzada compara una curva con otra desplazada.
- La correlación cruzada compara el espectro con una plantilla desplazada.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- Correlación cruzada normalizada: más robusta al ruido, algo más lenta.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».

📘 **Dónde se aprende** (5 clases): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md); [B27-C20 · Análisis multibanda de un evento extremo](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md); [B34-C09 · Integración multiinstrumento de datos heliofísicos](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md); [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md); [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Correlación de fase

- La correlación de fase usa solo la fase del espectro cruzado: `R = conj(F₁) F₂ / |conj(F₁) F₂|`, y su transformada inversa tiene un pico en el desplazamiento.

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- Correlación de fase: no necesita identificar estrellas, es rápida (FFT), pero solo traslaciones (con extensiones para giros) y sufre con ruido.
- La correlación de fase hace ese deslizamiento con la FFT, de una sola vez.
- ⚠️ **Error frecuente:** Usar correlación de fase con mucho ruido. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».

📘 **Dónde se aprende** (1 clase): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md).

### Correlación ítem–total corregida

- La correlación ítem–total corregida correlaciona un ítem con la suma de los demás.

💡 **Cómo se explica en la clase [B105-C27](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md):**
- Correlaciones ítem–total corregidas: 0,716; 0,623; 0,649; 0,715; 0,624; 0,669; 0,594; 0,689 (ítems 1–8) y 0,283 y 0,145 (9 y 10).
- Calcular la correlación ítem–total corregida y el alfa si se elimina cada ítem.
- 🎯 **Por qué importa:** Un cuestionario con ítems que no miden lo mismo produce una puntuación poco fiable, y con pocos participantes su fiabilidad ni siquiera se puede estimar. La decisión central: ¿qué ítems sobran, cuántos ítems hacen falta y cuántos participantes se necesitan para estimar el alfa con una incertidumbre aceptable?

📘 **Dónde se aprende** (1 clase): [B105-C27 · Instrumentos validados y psicometría en investigación](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md).

### Correlación positiva

- Independientes (S1, C.3.7) es más fuerte: la distribución de una no cambia al conocer la otra; independientes ⇒ `Cov = 0`, pero no al revés. Correlación positiva significa que tienden a subir juntas;

🎯 **Por qué importa (clase B12-C05):** En navegación espacial, la posición y la velocidad estimadas por un filtro no tienen errores independientes: un error de posición hacia delante suele ir acompañado de uno de velocidad. Ignorar esa relación da incertidumbres falsas, a veces demasiado optimistas y a veces demasiado pesimistas.

📘 **Dónde se aprende** (1 clase): [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md).

### Correspondencia

- Odometría visual: estimación del movimiento propio a partir de imágenes (F6). Correspondencia: par de observaciones del mismo punto en dos instantes.

💡 **Cómo se explica en la clase [B99-C01](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md):**
- Se eligen 2 correspondencias al azar (basta para fijar un movimiento 2D rígido), se ajusta `(R, t)`, se cuentan los inliers (error `< 0,10 m`) y tras 60 hipótesis se reajusta con los inliers de la mejor.
- A["Observaciones<br/>instante k y k+1"] --> B["Correspondencias<br/>mismo punto"]
- 🎯 **Por qué importa:** Una trayectoria se obtiene sumando movimientos pequeños, y cada uno trae un error; esos errores no se corrigen solos. La decisión central: ¿con qué calidad de correspondencias y de medida puedo confiar en la odometría, y cuándo necesito corregirla con cierres de bucle (C04)?

📘 **Dónde se aprende** (1 clase): [B99-C01 · Odometría visual](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md).

### Correspondencia por bloques

- La correspondencia por bloques busca, para cada ventana de la imagen izquierda, la ventana de la derecha con menor coste (aquí, la suma de diferencias absolutas, SAD).

🎯 **Por qué importa (clase B103-C03):** La profundidad estéreo es barata y densa, pero su error crece con el cuadrado de la distancia: a 20 m una incertidumbre de 0,3 px en la disparidad son 71 cm. La decisión central: ¿hasta qué distancia se puede confiar en el mapa de profundidad para decidir si un camino es seguro, y qué línea de base lo permite?

📘 **Dónde se aprende** (1 clase): [B103-C03 · Mapas de profundidad y correspondencia estéreo](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md).

### Corriente a la pared

- La corriente a la pared `j` es la densidad de iones que la golpean.

💡 **Cómo se explica en la clase [B78-C21](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md):**
- *Descripción textual:* la tensión fija la energía de impacto y el rendimiento; con la corriente a la pared da la velocidad de recesión; como la energía baja al retirarse la pared resulta una ecuación lineal con solución cerrada, contrastada con una integración numérica.
- 🎯 **Por qué importa:** El impulso total que un propulsor eléctrico puede entregar no lo limita el propelente sino su desgaste. La decisión central: ¿cómo depende la vida útil de la tensión de descarga y qué fracción del empuje máximo posible con el propelente alcanza a entregar?

📘 **Dónde se aprende** (1 clase): [B78-C21 · Erosión y vida útil de propulsores eléctricos](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md).

### Corriente admisible

- La corriente admisible de una pista depende de su sección y del aumento de temperatura `ΔT` aceptado.

💡 **Cómo se explica en la clase [B93-C01](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md):**
- Por margen: corriente admisible menos corriente real.
- Ejercicio 5 · autónomo. Si el cobre fuera de 70 µm con el mismo ancho, ¿cómo cambia la corriente admisible?
- 🎯 **Por qué importa:** El tronco no trataba el diseño de placas: B90 integra y B86 trata potencia, pero nadie calculaba una pista. La decisión central: ¿qué ancho de cobre y qué geometría de microtira necesita una placa para llevar una corriente y una señal dadas, y qué margen queda?

📘 **Dónde se aprende** (1 clase): [B93-C01 · Diseño de PCB espacial (conceptual)](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md).

### Corriente anular

- La corriente anular es la corriente equivalente de un anillo de radio `a`.

🎯 **Por qué importa (clase B30-C22):** El índice Dst (B30-C23) es un indicador de la energía del anillo de corriente. La decisión central: ¿qué energía y qué corriente corresponden a una disminución dada del campo?

📘 **Dónde se aprende** (1 clase): [B30-C22 · Anillo de corriente y corrientes magnetosféricas](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md).

### Corriente de alimentación

- La corriente de alimentación es la del punto de entrada.

💡 **Cómo se explica en la clase [B49-C01](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md):**
- La resistencia de entrada es `R/sin²(kh)`, porque la corriente de alimentación es `I₀ sin(kh)`.
- A `L = λ` la corriente de alimentación es nula y la resistencia de entrada del modelo diverge.
- 🎯 **Por qué importa:** Sin la resistencia de radiación no se sabe qué carga ve la línea ni cuánta potencia se irradia. La decisión central: ¿de qué longitud hacer el hilo y qué impedancia presentará a la línea?

📘 **Dónde se aprende** (1 clase): [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md).

### Corriente de corte

- La corriente de corte (`C/20`) termina la carga.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- La fase CV termina en la corriente de corte y repone `1,314 Ah` de los `1,399 Ah` (quedan `0,084 Ah`, que se recuperan en la órbita siguiente o con un corte más bajo).
- *Descripción textual:* la carga empieza a corriente constante hasta alcanzar la tensión máxima; luego sigue a tensión constante con corriente decreciente hasta la corriente de corte; la integral de la corriente da la carga repuesta.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Corriente de fusión

- La corriente de fusión `I_f` es la mínima que lo funde.

💡 **Cómo se explica en la clase [B86-C10](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md):**
- *Descripción textual:* el bus da la corriente de falla; de ella salen los tiempos y las integrales `I²t` de cada fusible; si la de despeje del fusible de la rama es menor que la de fusión del de aguas arriba, es selectivo.
- Paso 4 · Lectura. Con `10 A`, más de tres veces la corriente de fusión, el fusible abre en unas décimas de segundo.
- 🎯 **Por qué importa:** Si el fusible aguas arriba se funde antes que el de la rama averiada, un fallo local deja sin energía a toda la nave. Una protección bien coordinada aísla la rama y conserva el resto.

📘 **Dónde se aprende** (1 clase): [B86-C10 · Protección contra sobrecorriente](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md).

### Corriente de oscuridad

- La corriente de oscuridad es la señal que se acumula sin luz y crece con la exposición (S1).

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- Dividir por el plano antes de restar el oscuro, o restar un oscuro de otra duración sin escalar la corriente de oscuridad, produce errores sistemáticos.
- La guía de reducción de datos CCD de Astropy (S1) describe el modelo estándar: la imagen cruda es bias, corriente de oscuridad, ruido y un «plano» que multiplica al cielo y a las estrellas; resolver ese modelo da las cuentas de las estrellas.
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.

📘 **Dónde se aprende** (2 clases): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Corriente de oscuridad D

- La corriente de oscuridad `D` es la carga generada térmicamente, en `e⁻/s/píxel`.

💡 **Cómo se explica en la clase [B13-C15](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md):**
- Con estos órdenes de magnitud (`R = 3,0 e⁻`, `1,6 e⁻/DN`) y un cielo, una corriente de oscuridad y una apertura sintéticos, se analiza una fuente débil.
- 🎯 **Por qué importa:** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.

📘 **Dónde se aprende** (1 clase): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md).

### Corriente de saturación

- La corriente de saturación `I_0` fija la tensión de circuito abierto.

🎯 **Por qué importa (clase B86-C02):** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Corriente de tierra

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B33-C07](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md):**
- La subestación de menor resistencia a tierra (nodo 2) recibe la mayor corriente.
- 🎯 **Por qué importa:** Una subestación con una corriente de tierra alta puede saturar un transformador. La decisión central: ¿cómo se reparte la corriente inducida entre las subestaciones?

📘 **Dónde se aprende** (1 clase): [B33-C07 · Impactos del clima espacial en redes eléctricas](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md).

### Corriente eléctrica

- La corriente eléctrica `I` es la carga que atraviesa una sección por unidad de tiempo, `I = ΔQ/Δt`; se mide en amperios (`1 A = 1 C/s`).

🎯 **Por qué importa (clase B05-C16):** Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: ¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?

📘 **Dónde se aprende** (1 clase): [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md).

### Corriente fotogenerada

- La corriente fotogenerada `I_ph` es proporcional a la irradiancia.

🎯 **Por qué importa (clase B86-C02):** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Corriente galvánica

- La corriente galvánica `I = ΔV/(Rp_a/A_a + Rp_c/A_c)` es la de la pila.

💡 **Cómo se explica en la clase [B84-C21](../programa/clases/B84/B84-C21-compatibilidad-quimica-y-galvanica-de-materiales/CLASE.md):**
- Calcular la corriente galvánica con un modelo de resistencias.
- El script [galvanica.py](galvanica.py) calcula `ΔV`, la corriente galvánica y la velocidad de corrosión según la relación de áreas (comprueba coincidencia entre la masa de Faraday y `ρ × espesor × área` (< 1e-12)).
- 🎯 **Por qué importa:** Un tornillo de acero inoxidable en un panel de aluminio puede corroerlo 90 veces más rápido que otro de aluminio, y la corrosión ocurre en tierra, antes del lanzamiento. La decisión central: ¿qué pares de materiales pueden ir en contacto y cómo debe ser la relación de áreas?

📘 **Dónde se aprende** (1 clase): [B84-C21 · Compatibilidad química y galvánica de materiales](../programa/clases/B84/B84-C21-compatibilidad-quimica-y-galvanica-de-materiales/CLASE.md).

### Corriente inducida

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B33-C06](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de las corrientes inducidas*: campo, serie temporal y corriente.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de las corrientes inducidas*: campo, serie temporal y corriente.
- 🎯 **Por qué importa:** El campo eléctrico depende de la conductividad y de la frecuencia. La decisión central: ¿cuánto vale el campo geoeléctrico y la corriente en una línea para un campo magnético dado?

📘 **Dónde se aprende** (1 clase): [B33-C06 · Corrientes geomagnéticas inducidas (GIC)](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md).

### Corriente oscura

- La corriente oscura `D(T)` es la tasa de electrones térmicos por píxel.

💡 **Cómo se explica en la clase [B44-C07](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md):**
- Paso 3 · Resultado. La corriente oscura baja `6,34` veces.
- Evaluar una ley térmica de la corriente oscura.
- 🎯 **Por qué importa:** La oscuridad añade señal y ruido; saber cómo escala permite elegir temperatura y exposición. La decisión central: ¿cuánto hay que enfriar para que la corriente oscura deje de importar?

📘 **Dónde se aprende** (1 clase): [B44-C07 · Corriente oscura](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md).

### Corrimiento

- El corrimiento `z = Δλ/λ`.

💡 **Cómo se explica en la clase [B45-C12](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md):**
- Como la sirena de una ambulancia: el tono sube al acercarse y baja al alejarse; el corrimiento de las líneas es proporcional a la velocidad.
- Medir un corrimiento por correlación cruzada.
- 🎯 **Por qué importa:** Las velocidades radiales descubren planetas, binarias y la expansión del universo. La decisión central: ¿cómo se pasa de un corrimiento a una velocidad y con qué precisión?

📘 **Dónde se aprende** (1 clase): [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md).

### Corrimiento al rojo

- El corrimiento al rojo es ```text z = λ_obs / λ_reposo − 1 ``` y, para `z ≪ 1`, la velocidad radial aproximada es `v = c z`.

🎯 **Por qué importa (clase B06-C17):** En B01-C01 estimaste la velocidad de una galaxia con una sola línea, H-alfa en 662,9 nm. Pero ¿cómo se sabe que esa línea es H-alfa y no otra?

📖 **Explicado a fondo:** [Corrimiento al rojo (redshift)](esencial/esencial-a-c.md#corrimiento-al-rojo-redshift) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Corrimiento al rojo cosmológico

- El corrimiento al rojo cosmológico `z` es el cambio fraccional de longitud de onda por la expansión.

🎯 **Por qué importa (clase B26-C11):** `H₀` fija la escala de distancias del universo y su edad aproximada, y hoy su valor depende de cómo se mida (C23). Para entender esa discusión hay que saber ajustar la ley a datos con dispersión, cuándo vale `v = cz` y qué incertidumbre se arrastra.

📘 **Dónde se aprende** (1 clase): [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md).

### Corrimiento de transición

- El corrimiento de transición `z_t` es aquel en que `ä = 0`.

💡 **Cómo se explica en la clase [B26-C13](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md):**
- Calcular el parámetro de deceleración y el corrimiento de transición.
- 🎯 **Por qué importa:** La edad del universo, la distancia a una galaxia y el calendario de su historia salen de la ecuación de Friedmann. Con ella se interpreta cualquier parámetro cosmológico.

📘 **Dónde se aprende** (1 clase): [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md).

### Corrimiento exacto

- El corrimiento exacto (Schwarzschild) es `1 + z = 1/√(1 − r_s/R)`.

💡 **Cómo se explica en la clase [B26-C10](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md):**
- Ejercicio 5. Corrimiento exacto de la estrella de neutrones.
- Ejercicio 12 · integrador. Elabora tu *tabla de corrimientos*: calcula `z` exacto y débil para cuatro cuerpos, el error de la serie, la velocidad equivalente y la razón suelo–órbita; interpreta la prueba Galileo.
- 🎯 **Por qué importa:** El corrimiento gravitacional ajusta los relojes de los satélites de navegación, contamina la medida de velocidades en enanas blancas y revela la compacidad de las estrellas de neutrones. La decisión central: dada la compacidad de un cuerpo, ¿cuánto vale el corrimiento de su luz y cuándo falla la aproximación de campo débil?

📘 **Dónde se aprende** (1 clase): [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md).

### Corrimiento gravitacional al rojo

- El corrimiento gravitacional al rojo es el cambio de frecuencia de la luz al subir en un campo.
- El corrimiento gravitacional al rojo es el aumento de longitud de onda de la luz al salir de un pozo de potencial.

💡 **Cómo se explica en la clase [B26-C10](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md):**
- python programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/corrimientos.py
- 🎯 **Por qué importa:** El corrimiento gravitacional ajusta los relojes de los satélites de navegación, contamina la medida de velocidades en enanas blancas y revela la compacidad de las estrellas de neutrones. La decisión central: dada la compacidad de un cuerpo, ¿cuánto vale el corrimiento de su luz y cuándo falla la aproximación de campo débil?

📘 **Dónde se aprende** (2 clases): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md); [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md).

### Corrupción

- La corrupción es una alteración involuntaria de los bytes.
- La corrupción es el cambio de un elemento a una versión errónea.

💡 **Cómo se explica en la clase [B14-C11](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md):**
- Detectar la corrupción de un solo bit y la modificación de un único valor.
- El script [versiones_de_datos.py](versiones_de_datos.py) implementa un almacén direccionado por contenido con SHA-256, comprueba el vector de prueba del NIST, inserta dos versiones y un duplicado, usa manifiestos como versiones, localiza el cambio, detecta la corrupción de un bit y mide el efecto avalancha.
- 🎯 **Por qué importa:** Un análisis usó «la tabla de catálogo de octubre». En noviembre alguien reemplazó el archivo por otro con el mismo nombre.

📘 **Dónde se aprende** (2 clases): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md); [B133-C02 · Narrativas orales y transmisión del saber del cielo](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md).

### Corte

- Un corte es la masa donde cambia el índice.
- Un corte (sección) fija una variable y deja la otra libre.
- Acuerdo entre revisores: cuánto coinciden entre sí. Corte: fracción que se financia.

💡 **Cómo se explica en la clase [B09-C15](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md):**
- B --> D["Cada corte es una<br/>función de una variable"]
- Paso 3 · Corte a lo largo de `x`. A `±5000 km`: `−1,2818` y `−1,2824`, ambos menores.
- 🎯 **Por qué importa:** Una sonda que viaja de la Tierra a la Luna se mueve en un campo de potencial que depende de dos coordenadas del plano. Dónde están los puntos de equilibrio y qué forma tiene el campo alrededor de ellos se lee en un mapa de curvas de nivel.

📘 **Dónde se aprende** (3 clases): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md); [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md).

### Corte de energía

- Un corte de energía interrumpe la escritura en un byte.

💡 **Cómo se explica en la clase [B88-C35](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md):**
- La evidencia es la prueba exhaustiva de corte de energía del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *prueba exhaustiva de corte de energía*: registro, esquema, cortes, resultados y lista de qué es sintético.
- 🎯 **Por qué importa:** Un corte durante una escritura deja un registro a medias. La decisión central: ¿qué esquema garantiza que, cortes donde cortes, siempre haya un estado válido recuperable?

📘 **Dónde se aprende** (1 clase): [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md).

### Corte GZK

- El corte GZK es el límite por interacción con el fondo.

🎯 **Por qué importa (clase B31-C13):** La energía y la composición de un rayo cósmico se infieren de la forma de su cascada, y el fondo de microondas limita la energía que llega. La decisión central: ¿qué profundidad y tamaño tiene una cascada y a qué energía aparece un corte?

📘 **Dónde se aprende** (1 clase): [B31-C13 · Rayos cósmicos y cascadas](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md).

### Corteza

- La corteza es la capa superior de un cuerpo diferenciado.

💡 **Cómo se explica en la clase [B61-C07](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md):**
- Con profundidad de excavación ilustrativa 0,1 D y corteza de 40 km: 300 km → 30 km (corteza); 600 km → 60 km (manto); 1000 km → 100 km (manto).
- Comparar una profundidad de excavación ilustrativa con el espesor de la corteza.
- 🎯 **Por qué importa:** Las cuencas dejan huella en la corteza entera. La decisión central: ¿cómo se espacian los anillos, qué proyectil implica una cuenca y cuándo excava hasta el manto?

📘 **Dónde se aprende** (1 clase): [B61-C07 · Cuencas multianillo y grandes impactos](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md).

### Cortisol relativo

- El cortisol relativo `C` es adimensional.

🎯 **Por qué importa (clase B105-C22):** Una medición de cortisol sin hora del día no se interpreta: el ritmo diario domina. Y un estresor crónico cambia el nivel medio de una forma distinta que uno agudo.

📘 **Dónde se aprende** (1 clase): [B105-C22 · Sistema neuroendocrino y respuesta al estrés en vuelo](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md).

### Cosmovisión

- Una cosmovisión es la manera en que una sociedad entiende el mundo y su lugar en él, y la astronomía es una de las formas en que se expresa.

💡 **Cómo se explica en la clase [B02-C05](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md):**
- Esta relación entre cielo y ciclo biológico es un ejemplo de lo que significa una cosmovisión: el cielo y la vida están conectados en una misma explicación.
- Para Machu Picchu, un artículo propone reinterpretarlo como centro de peregrinación ligado a la cosmovisión inca, en lugar de residencia real de Pachacuti, analizando el entorno y los ciclos celestes (S4).
- 🎯 **Por qué importa:** Hablar de «astronomía andina» en singular es un error: los Andes reúnen sociedades de épocas y regiones muy distintas. La pregunta motivadora es: ¿cómo se estudia respetuosamente un cielo que otra cultura leyó de otra manera, sin imponerle nuestras categorías y sin inventar lo que las fuentes no dicen?

📘 **Dónde se aprende** (1 clase): [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md).

### Coste

- El coste es el número de evaluaciones de la fuerza: leapfrog `1` por paso, Yoshida `3`.
- Un criterio de beneficio es mejor cuanto mayor; uno de coste es mejor cuanto menor.
- El coste se cuenta en operaciones de punto flotante por paso.

💡 **Cómo se explica en la clase [B73-C20](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md):**
- *Descripción textual:* los requisitos fijan un presupuesto frente al error de modelo; la convergencia da el paso requerido de cada integrador; el coste decide cuál usar.
- Por coste: evaluaciones para el presupuesto.
- 🎯 **Por qué importa:** Una integración «de precisión» no es la que usa el paso más pequeño sino la que mantiene el error numérico por debajo de la incertidumbre del modelo, con el menor coste. Sin ese presupuesto se gasta cómputo sin ganar exactitud o se afirma una exactitud que no existe.

📘 **Dónde se aprende** (3 clases): [B73-C20 · Proyecto de integración celeste de precisión](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md); [B74-C18 · Estimación autónoma a bordo](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md); [B95-C03 · Selección y comparación de plataformas](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md).

### Coste asimétrico

- El coste asimétrico pondera más un error que el otro.

🎯 **Por qué importa (clase B119-C17):** C11 trata los límites militares del tratado; esta clase aborda cómo razonar la distinción bajo incertidumbre, un tema que ninguna clase del bloque cubre y que exige cautela jurídica. La decisión central: ¿cómo cambia el umbral de decisión cuando equivocarse en un sentido es mucho más grave que en el otro?

📘 **Dónde se aprende** (1 clase): [B119-C17 · Conflictos y normas humanitarias aplicables](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md).

### Coste de arranque

- El coste de arranque es el tiempo de crear procesos y copiar datos.

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Decisión. Para esta tarea de poco más de un segundo, no compensa; sí compensaría con trozos cien veces más largos, donde el coste de arranque es una fracción pequeña.
- Límites: los tiempos cambian en cada ejecución y en cada máquina; en Linux, con `fork`, el coste de arranque sería menor; no se probaron hilos; el ajuste de `s` usa tres puntos.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.

📘 **Dónde se aprende** (1 clase): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md).

### Coste de celda

- El coste de celda es `1 + w_s (pendiente/límite)² + w_r (rugosidad/límite)` y es infinito si se supera algún umbral.

💡 **Cómo se explica en la clase [B102-C08](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md):**
- Dijkstra con 8 vecinos y paso `Δx √2` o `Δx` por la media de los costes de las dos celdas encuentra una ruta de `56` celdas, `122,4 m` y coste `257,1`, frente a `99,0 m` en línea recta (`23,6 %` más larga).
- Endurecer el límite de `30°` a `20°` triplica las celdas prohibidas y sube el coste de la ruta un `18,5 %`, aunque la geometría de la ruta no cambia.
- 🎯 **Por qué importa:** Elegir la ruta es elegir qué riesgo se acepta. La decisión central: ¿qué celdas son intransitables, cuánto cuesta cruzar las demás y cuánto se alarga la ruta de mínimo riesgo respecto de la recta?

📘 **Dónde se aprende** (1 clase): [B102-C08 · Traversabilidad y evaluación de riesgo de terreno](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md).

### Coste de trazado

- El coste de trazado es `Σ f·d`.

💡 **Cómo se explica en la clase [B109-C02](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md):**
- *Descripción textual:* las zonas y sus flujos definen un coste; una cuadrícula fija las posiciones posibles; la enumeración de todas las permutaciones da el mejor trazado, que se compara con los trazados al azar.
- Calcular el coste de un trazado como suma de flujo por distancia.
- 🎯 **Por qué importa:** Un buen plano ahorra pasos, separa lo sucio de lo limpio y deja las zonas tranquilas lejos de las ruidosas. La decisión central: ¿dónde pongo cada zona para que los recorridos frecuentes sean cortos y las zonas incompatibles estén lejos?

📘 **Dónde se aprende** (1 clase): [B109-C02 · Zonificación y distribución funcional de módulos de un hábitat](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md).

### Costo

- El costo se mide aquí como número de comparaciones.
- El costo es `C(φ, T) = v∞,sal + v∞,lleg` en km/s.
- El costo de un par es tiempo de viaje más trabajo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- Casos: lista vacía, un elemento, repetidos, ya ordenada (mínimo costo de inserción), inversa (máximo), y listas aleatorias contrastadas con `sorted`.
- Contar comparaciones para medir el costo sin depender de la velocidad del equipo.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.

📘 **Dónde se aprende** (4 clases): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md); [B33-C05 · Comunicación de riesgo y alertas de clima espacial](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md); [B75-C12 · Optimización de trayectoria](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md); [B97-C09 · Robótica colaborativa](../programa/clases/B97/B97-C09-robotica-colaborativa/CLASE.md).

### Costo cuadrático

- El costo cuadrático es `C = ∫₀^∞ (xᵀ Q x + uᵀ R u) dt` con `Q` simétrica semidefinida positiva y `R` simétrica definida positiva.

💡 **Cómo se explica en la clase [B16-C15](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md):**
- Es el amortiguamiento del filtro de Butterworth de segundo orden; el costo cuadrático con `Q = diag(q, 0)` lleva a él.
- Límite: el costo cuadrático penaliza mucho los picos y poco los ruidos pequeños; puede no reflejar un límite físico estricto.
- 🎯 **Por qué importa:** Con un PD hay dos perillas, `Kp` y `Kd`, y no es obvio cuánto esfuerzo gasta cada combinación. En un satélite el esfuerzo tiene un costo real: energía de las ruedas, momento almacenado, desgaste.

📘 **Dónde se aprende** (1 clase): [B16-C15 · Control óptimo LQR](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md).

### Costo de espera

- El costo de espera es el gasto adicional por cada año extra.

💡 **Cómo se explica en la clase [B124-C06](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md):**
- Si cada año extra cuesta 6 % del total, el costo de espera es `6,0` uc (`6,0` % del total), un supuesto sintético.
- *Descripción textual:* cada año se gasta lo menor entre el tope y lo pendiente; lo que no se paga queda como atraso, que define el año de término y el costo de espera, y todo se comprueba con una fórmula del mínimo.
- 🎯 **Por qué importa:** Un proyecto puede estar bien estimado y aun así fallar porque el dinero no llega al ritmo que necesita. La decisión central: ¿qué tope anual evita el atraso y cuánto cuesta cada año de espera?

📘 **Dónde se aprende** (1 clase): [B124-C06 · Financiamiento público](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md).

### Costo del operador

- El costo del operador es las primas más las pérdidas que él retiene.

💡 **Cómo se explica en la clase [B127-C08](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md):**
- *Descripción textual:* el mismo conjunto de eventos aleatorios se aplica a cuatro estrategias que añaden coberturas de a una; para cada una se simula el costo del operador y se resumen su media, su desviación, su cuantil 99 % y la probabilidad de superar `60 MUSD`.
- Límite: aquí el operador es neutral al costo de capital y no hay efectos de segundo orden, como la caída del negocio tras una pérdida.
- 🎯 **Por qué importa:** Integrar los seguros de una misión en un caso permite practicar la decisión; no existía tal caso. La decisión central: ¿cuánto se paga de más por reducir el riesgo y qué riesgo se está dispuesto a retener?

📘 **Dónde se aprende** (1 clase): [B127-C08 · Simulación de cobertura de seguros para una misión](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md).

### Costo esperado

- Un costo esperado pondera cada tipo de error por su costo.

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Costo esperado: el que lleva a una decisión; exige conocer costos.
- Elegir un umbral minimizando un costo esperado.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Costo fijo

- El costo fijo `F` se paga siempre; el variable `v`, por producto; el escalonado `S` se suma por cada tramo de capacidad `cap`.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- F["costo fijo F"] --> C["C(Q) = F + vQ + S ⌈Q/cap⌉"]
- *Descripción textual:* los costos fijo, variable y escalonado forman el costo total, del que salen el costo medio, el precio con margen y el equilibrio; la incertidumbre de la demanda se evalúa con dos métodos.
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Costo más incentivo (CPIF)

- Precio fijo (FFP): el pago no depende del costo real. Costo más incentivo (CPIF): se paga el costo real más un honorario que baja cuando el costo supera el objetivo.

💡 **Cómo se explica en la clase [B124-C10](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md):**
- Ninguno es mejor en sí: depende de qué tan bien se conoce el costo, y el modelo no incluye incentivos a ocultar costos ni renegociaciones.
- Describir un contrato de precio fijo y uno de costo más honorario con incentivo.
- 🎯 **Por qué importa:** El tipo de contrato reparte el riesgo de sobrecosto entre quien compra y quien vende. La decisión central: ¿cuánto riesgo asume cada parte con cada tipo de contrato y cuánto cuesta ese reparto en promedio?

📘 **Dónde se aprende** (1 clase): [B124-C10 · Contratos y compras espaciales](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md).

### Costo medio

- El costo medio es `C(Q)/Q`.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- Con margen sobre precio de 25 %, `p = costo medio/0,75`: `78,67` um a 1 000, `37,60` a 2 500 y `23,20` a 5 000 productos.
- *Descripción textual:* los costos fijo, variable y escalonado forman el costo total, del que salen el costo medio, el precio con margen y el equilibrio; la incertidumbre de la demanda se evalúa con dos métodos.
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Costo neto

- El costo neto es pérdida retenida más prima de reaseguro.

💡 **Cómo se explica en la clase [B127-C07](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md):**
- Costo neto medio: `0,70 × 67,745 + 18,00 = 65,42`.
- Costo neto medio `74,58`: cuesta `6,8 MUSD` más que no reasegurar, a cambio de desviación `76,9` y cuantil 99 % `336,8`.
- 🎯 **Por qué importa:** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Costo nivelado (LCOP)

- El costo nivelado (LCOP) es `(CapEx·CRF + OpEx)/Q`.

💡 **Cómo se explica en la clase [B124-C24](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md):**
- *Descripción textual:* el equipo y su transporte forman el CapEx, que se convierte en anualidad y se suma al OpEx para dar el costo anual y el costo nivelado, que se verifica con valor actual y se compara con traer el producto.
- Descripción larga: el transporte domina el capital y la operación, y el costo nivelado es una pequeña fracción del de traer el producto, siempre que la producción llegue a lo planificado.
- 🎯 **Por qué importa:** B124 estima costos de misión, pero una instalación que opera años necesita separar el capital de la operación y ponerlos en una misma unidad. La decisión central: ¿a qué costo por kilogramo produce la instalación y desde qué producción conviene frente a traer el producto?

📘 **Dónde se aprende** (1 clase): [B124-C24 · CapEx y OpEx de una instalación extraterrestre](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md).

### Costo por kilogramo

- El costo por kilogramo es el precio dividido por la carga útil.

💡 **Cómo se explica en la clase [B124-C23](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md):**
- El costo por kilogramo es el precio dividido por una fracción pequeña: cualquier mejora de la fracción mejora el costo en la misma proporción.
- El descenso desde órbita baja (`Δv = 6 000 m/s`, `Isp` 340 s, `e = 0,12`) deja una fracción de `0,05157`, así que cada kilogramo en superficie exige `1/0,05157` kg en órbita: el costo sube a `87176` um/kg (`19,4` veces); con reutilización, `61024`.
- ⚠️ **Error frecuente:** Tomar un costo por kilogramo como un dato universal. Se corrige con la sección 10 y el ejercicio 11.
- 🎯 **Por qué importa:** El costo por kilogramo a superficie no se puede leer en una lista de precios: depende de una cadena de fracciones de masa que se multiplican. La decisión central: ¿cuánto cuesta llevar un kilogramo a la superficie, de qué depende ese costo y qué lo hace más sensible?

📘 **Dónde se aprende** (1 clase): [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Costo por metro

- El costo por metro es el `Δv` entre el cambio de posición.

💡 **Cómo se explica en la clase [B76-C11](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md):**
- Comparar el costo por metro de tramos de distinta duración.
- Ejercicio 2 · con una pista. Calcula el costo por metro del tramo 1.
- 🎯 **Por qué importa:** Una aproximación a baja velocidad no puede depender de que todos los impulsos se ejecuten. La decisión central: ¿cuántos tramos usar, cuánto cuestan y qué ocurre si el segundo impulso de un tramo falla?

📘 **Dónde se aprende** (1 clase): [B76-C11 · Operaciones de aproximación](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md).

### Costo por suscriptor-mes

- El costo por suscriptor-mes es el costo anual repartido en suscriptores y meses.

💡 **Cómo se explica en la clase [B124-C11](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md):**
- Con 100 000 suscriptores el ingreso es `60,0` Mum/año, el margen `21,100` Mum/año y el costo por suscriptor-mes `32,42` um; el despliegue se recupera en `4,27` años (sin descuento).
- *Descripción textual:* la flota y su vida dan la tasa de reposición, que se verifica por simulación; esta, más el costo operativo, da el costo anual y, con el ARPU, el equilibrio en suscriptores.
- 🎯 **Por qué importa:** Una constelación puede ser técnicamente exitosa y económicamente inviable si la reposición se come el margen. La decisión central: ¿cuántos suscriptores se necesitan para cubrir la reposición y la operación, y qué tan sensible es eso a la vida útil?

📘 **Dónde se aprende** (1 clase): [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md).

### Costo total

- El costo total es `J = m₀ + c_t·TOF`, con `m₀` en toneladas y `c_t` en unidades por día.

💡 **Cómo se explica en la clase [B75-C27](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md):**
- Por costo total: con `c_t` el óptimo se desplaza.
- Con un costo temporal ilustrativo de `0,02 u/d`, el costo total mínimo (masa en toneladas + tiempo) cae en `220 d`: se paga más masa (`4,512 t` en vez de `4,189 t`) para ahorrar 40 días.
- ⚠️ **Error frecuente:** Confundir el óptimo en delta-v con el óptimo en costo total. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un viaje más corto gasta más combustible y uno más largo gasta más tiempo. La decisión central: ¿qué tiempo de vuelo minimiza el costo total cuando se pesan la masa lanzada y la duración?

📘 **Dónde se aprende** (1 clase): [B75-C27 · Duración de misión y tiempo de vuelo como restricción](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md).

### Costos

- Los costos se reparten por igual salvo decisión distinta (art.

💡 **Cómo se explica en la clase [B123-C03](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md):**
- Ejercicio 5 · autónomo. ¿Quién paga los costos de la comisión?
- 🎯 **Por qué importa:** Un derecho a reclamar se pierde o se debilita si no se ejerce por la vía y en el plazo previstos. La decisión central: ¿cuándo y cómo se presenta la reclamación, cuándo se puede pedir una comisión y qué valor tiene su decisión?

📘 **Dónde se aprende** (1 clase): [B123-C03 · Mecanismos de reclamación entre Estados](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md).

### Costura

- Una costura es la línea de unión entre dos teselas.

💡 **Cómo se explica en la clase [B14-C27](../programa/clases/B14/B14-C27-procesamiento-por-teselas-de-grandes-volumenes-de-imagenes/CLASE.md):**
- Un píxel junto a la costura necesita hasta 2 píxeles de la tesela vecina.
- El laboratorio comprueba que todos esos píxeles están a 2 o menos píxeles de una costura interior: el error vive en las franjas de ancho `2R` alrededor de las costuras, no en el interior de las teselas.
- ⚠️ **Error frecuente:** Culpar al redondeo de un error de costuras. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Una cobertura global de imágenes ocupa terabytes y ningún equipo la carga entera. Para suavizarla, calcular un índice o detectar cambios hay que procesarla por pedazos.

📘 **Dónde se aprende** (1 clase): [B14-C27 · Procesamiento por teselas de grandes volúmenes de imágenes](../programa/clases/B14/B14-C27-procesamiento-por-teselas-de-grandes-volumenes-de-imagenes/CLASE.md).

### Cota

- Una cota es un valor que el resultado no debería superar (superior) o no debería bajar de él (inferior).
- Un error de redondeo es la diferencia entre el valor y su redondeo; su cota es el máximo posible: ±media unidad de la última cifra conservada (`365` → ±0,5).
- La cota es un límite superior, no una medición del valor.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C11](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md):**
- D --> E["Reportar con unidad, cifras y cota"]
- Primero se estima con una cifra; luego se calcula sin redondear; se compara con la estimación; se redondea al final según la calidad de los datos; y se reporta con unidad, cifras y cota.
- 🎯 **Por qué importa:** Si te piden el tiempo que tarda la luz del Sol en llegar a la Tierra y respondes «499,004783836 s», parece muy preciso, pero tus datos (1 au y `c`) son exactos; en cambio, si respondes lo mismo para la distancia a la Luna, que varía entre unos 357 000 y 407 000 km, esas cifras serían falsas.

📘 **Dónde se aprende** (7 clases): [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md); [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md); [B53-C05 · Sistemas de coordenadas lunares](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md); [B81-C12 · Restricciones dinámicas en optimización](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md) y 1 más.

### Cota aproximada

- La cota aproximada supone `k × (celdas medias por campo)` celdas.

💡 **Cómo se explica en la clase [B28-C15](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md):**
- Comparar la cobertura con una cota aproximada y con la garantía `1 − 1/e`.
- Ejercicio 11 · transferencia. ¿Qué valida la comparación con la cota aproximada?
- 🎯 **Por qué importa:** Observar más campos cubre más probabilidad, pero cada campo recibe menos tiempo y es menos profundo. Si la fuente es débil, el exceso de campos hace que no se vea.

📘 **Dónde se aprende** (1 clase): [B28-C15 · Búsqueda de contrapartidas ópticas](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md).

### Cota de cortes mínimos

- La aproximación de evento raro suma las probabilidades de los cortes; la cota de cortes mínimos es `1 − Π(1 − P(cᵢ))`.

💡 **Cómo se explica en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- La enumeración exacta de los 128 estados da 0,016132; la inclusión–exclusión, 0,016132; la aproximación de evento raro, 0,016200 (un 0,42 % de más); la cota de cortes mínimos, 0,016132 (aquí coincide porque los cortes mínimos no comparten eventos);
- Comparar la aproximación de evento raro y la cota de cortes mínimos con el valor exacto.
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?

📘 **Dónde se aprende** (1 clase): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Cota de Cramér–Rao

- La matriz de información de Fisher es `F = Jᵀ J / σ²` (ruido gaussiano independiente); la cota de Cramér–Rao dice que la covarianza de cualquier estimador insesgado es al menos `F⁻¹`.
- La cota de Cramér–Rao es el límite de precisión.
- La cota de Cramér–Rao (CRB) dice que cualquier estimador sin sesgo cumple `Var(θ̂) ≥ 1/I(θ)`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C15](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md):**
- *Descripción textual:* los datos con ruido alimentan un estimador; de su sesgo y su varianza sale el error cuadrático medio; la varianza de un estimador sin sesgo se compara con la cota de Cramér–Rao.
- Calcular la información de Fisher y la cota de Cramér–Rao.
- 🎯 **Por qué importa:** Un telescopio recoge 100 fotones de una estrella y quieres su posición con la mayor exactitud posible. ¿Basta con promediar las posiciones?

📘 **Dónde se aprende** (6 clases): [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md); [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md); [B46-C18 · VLBI y geodesia](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md); [B74-C03 · Medición de alcance por radio](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md); [B74-C27 · Navegación por púlsares de rayos X como técnica de investigación](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md).

### Cota de escape

- La cota de escape es `√(2 f ε)`.
- La cota de escape `Vₑ_max = √(2ηε)` es el escape máximo con una fuente de energía específica `ε`.

💡 **Cómo se explica en la clase [B78-C16](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md):**
- *Descripción textual:* la energía por reacción y la masa de los reactivos dan la energía específica; ésta da la fracción de masa convertida y, con la fracción dirigida, la cota de escape, que se contrasta con la relativista; con una potencia dada se calcula el consumo.
- Descripción larga: la energía por kilo de la fusión supera a la química en siete órdenes de magnitud; la cota de escape sigue siendo una fracción de la velocidad de la luz.
- 🎯 **Por qué importa:** Si la energía por kilo es millones de veces mayor, el escape posible es enorme; pero eso es una cota, no un propulsor. La decisión central: ¿cuánta energía por kilo libera cada reacción y cuánto escape acotaría, según la fracción que se logre dirigir?

📘 **Dónde se aprende** (2 clases): [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md); [B78-C18 · Energía específica y limitaciones](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md).

### Cota de Liu y Layland

- La cota de Liu y Layland `U ≤ n(2^(1/n) − 1)` es suficiente para RM con plazos iguales a los períodos y tiende a `ln 2 = 0,6931`.

🎯 **Por qué importa (clase B88-C06):** Elegir la política determina cuánta CPU se puede usar con garantías. La decisión central: ¿RM basta, o se necesita EDF para el conjunto de tareas?

📘 **Dónde se aprende** (1 clase): [B88-C06 · Planificación de tareas RTOS](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md).

### Cota de Liu–Layland

- La cota de Liu–Layland `n(2^(1/n) − 1)` es una condición suficiente de planificabilidad con prioridades por tasa.

💡 **Cómo se explica en la clase [B98-C07](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md):**
- Calcular la utilización de un conjunto de tareas periódicas y compararla con la cota de Liu–Layland.
- El script [tres_capas.py](tres_capas.py) calcula la utilización, la cota de Liu–Layland, el tiempo de respuesta de cada tarea por punto fijo y la probabilidad de plan tardío por Monte Carlo y por fórmula (comprueba `R ≤ T`, `U ≤` cota, latencia reflejo ≤ 0,5 s y concordancia Monte Carlo–fórmula < 0,005).
- 🎯 **Por qué importa:** Una arquitectura sin presupuesto de tiempos puede parecer correcta hasta que una tarea lenta retrasa un reflejo. La decisión central: ¿cada capa cumple sus plazos aunque las demás consuman su peor caso, y qué pasa cuando el planificador tarda más de lo previsto?

📘 **Dónde se aprende** (1 clase): [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md).

### Cota de peor caso

- La cota de peor caso supone que todos los errores actúan en la dirección más desfavorable.
- La cota de peor caso suma los máximos: `2 + 15 + 8 = 25 µs`.

💡 **Cómo se explica en la clase [B03-C19](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md):**
- La cota de peor caso, que considera todos los redondeos en la dirección peor, es `[29,745; 30,027] km/s`; la incertidumbre en cuadratura es `0,062 km/s`.
- Distinguir la cota de peor caso de la incertidumbre estándar en cuadratura, y usar `a/√3` para una distribución uniforme.
- ⚠️ **Error frecuente:** Confundir cota de peor caso con incertidumbre estándar. Ejercicio 11.
- 🎯 **Por qué importa:** Con los datos de la Tierra redondeados a tres cifras (semieje `1,50 × 10⁸ km` y período `365 d`), la rapidez orbital sale `29,89 km/s`. La NASA publica 29,78 km/s.

📘 **Dónde se aprende** (2 clases): [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B88-C26 · Latencia de interrupciones y jitter](../programa/clases/B88/B88-C26-latencia-de-interrupciones-y-jitter/CLASE.md).

### Cota de pila

- La cota de pila suma un marco por nivel de prioridad.

💡 **Cómo se explica en la clase [B88-C22](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md):**
- Ejercicio 4 · autónomo. Calcula la cota de pila.
- Cota de pila (un marco por nivel) = 120 B ; observada con anidamiento = 80 B
- 🎯 **Por qué importa:** Las interrupciones fijan cuánto tarda el sistema en reaccionar y cuánta pila usa. La decisión central: ¿se permite que una interrupción de mayor prioridad interrumpa a otra, y qué cuesta eso en latencia y pila?

📘 **Dónde se aprende** (1 clase): [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md).

### Cota de sección eficaz

- La cota de sección eficaz `σ < s_up/(εΦ)`.

💡 **Cómo se explica en la clase [B31-C18](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md):**
- *Descripción textual:* las observaciones y el fondo dan el límite por cada método; el límite se convierte en cota de sección eficaz y la cobertura se verifica por Monte Carlo.
- 🎯 **Por qué importa:** Un límite mal calculado puede excluir una teoría que no estaba excluida. La decisión central: ¿qué señal máxima es compatible con lo observado y cuán fiable es el método?

📘 **Dónde se aprende** (1 clase): [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md).

### Cota de Sellke–Bayarri–Berger

- La cota de Sellke–Bayarri–Berger acota el `BF` a favor de la alternativa con `BF ≤ 1/(−e p ln p)` para `p < 1/e`.

🎯 **Por qué importa (clase B132-C05):** El catálogo trata alineaciones sin ese contexto. La decisión central: ¿cuánto apoyo da cada línea de evidencia a la intención de una alineación, y qué parte de la conclusión depende de lo que se supone de antemano?

📘 **Dónde se aprende** (1 clase): [B132-C05 · Contexto ritual y social de la observación del cielo](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md).

### Cota de unión

- Matriz de confusión: frecuencia de cada clasificación por causa verdadera. Cota de unión: `1 − Σ Q(dᵢⱼ/2)`.

💡 **Cómo se explica en la clase [B96-C29](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md):**
- La cota de unión `1 − Σ Q(d/2)` queda por debajo de cada acierto simulado (por ejemplo, 0,8191 frente a 0,8159 en apuntamiento, dentro de 0,01).
- Comparar el acierto con una cota inferior de unión.
- 🎯 **Por qué importa:** Perder tiempo de contacto buscando la causa equivocada es caro. La decisión central: ¿qué medidas distinguen las causas y cuáles se confunden entre sí?

📘 **Dónde se aprende** (1 clase): [B96-C29 · Diagnóstico de fallas de enlace](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md).

### Cota de Δv

- La cota de Δv es el valor al que tiende la etapa con propelente infinito.

💡 **Cómo se explica en la clase [B78-C02](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md):**
- Descripción larga: el Δv crece con el logaritmo de la razón de masas y tiene una cota que depende solo de la fracción de tanques y del `Isp`.
- Calcular la cota de Δv que impone la fracción de tanques.
- 🎯 **Por qué importa:** Más propelente da más Δv, pero cada kilo de propelente exige tanques, y esos tanques también se aceleran. La decisión central: ¿cuánto propelente hace falta para un Δv dado y existe un máximo de Δv que ninguna cantidad de propelente supera?

📘 **Dónde se aprende** (1 clase): [B78-C02 · Propulsión química como sistema físico](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md).

### Cota superior

- Eficiencia de recuperación: fracción recuperada por el hisopo. Cota superior: valor que, con confianza `CL`, no es menor que la densidad verdadera.
- Una cota superior acota por arriba.

💡 **Cómo se explica en la clase [B90-C21](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md):**
- *Descripción textual:* los hisopos recogen colonias; la densidad estimada es `C/(eA)` y la cota superior usa el límite de Poisson de `C`; se compara la cota con el límite.
- La densidad observada es 40 /m² y la corregida 266,7 esporas/m², bajo el límite de ejemplo de 300; pero la cota superior al 95 % es 481,2 /m²: no cumple con esa confianza.
- 🎯 **Por qué importa:** Un hisopo recoge solo una fracción de las esporas de una superficie y se cuentan pocas colonias; el resultado es una estimación con incertidumbre. La decisión central: ¿la biocarga cumple el límite con la confianza exigida o hace falta muestrear más o reducir?

📘 **Dónde se aprende** (2 clases): [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md); [B119-C23 · Protección ambiental de las actividades de lanzamiento](../programa/clases/B119/B119-C23-proteccion-ambiental-de-las-actividades-de-lanzamiento/CLASE.md).

### Cota superior de confianza

- Causa raíz: origen de la falla. Cota superior de confianza: valor que, con probabilidad `CL`, no es inferior a la tasa verdadera.

💡 **Cómo se explica en la clase [B90-C17](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md):**
- Calcular la cota superior de Poisson de la tasa de fallas con una confianza dada.
- 🎯 **Por qué importa:** Una falla única en 500 horas de ensayo no demuestra que el equipo sea confiable: solo acota la tasa de fallas. Y una anomalía mal registrada se pierde.

📘 **Dónde se aprende** (1 clase): [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md).

### Cotas de Voigt y Reuss

- Las cotas de Voigt y Reuss son `E_V = V_f E_f + (1 − V_f)E_m` y `E_R = 1/(V_f/E_f + (1 − V_f)/E_m)`.

💡 **Cómo se explica en la clase [B84-C37](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md):**
- Calcular las cotas de rigidez de Voigt y Reuss.
- 🎯 **Por qué importa:** La resistencia de un compuesto cae exponencialmente con la porosidad: pasar de 10 a 25 % de huecos divide la resistencia por 2,4. La decisión central: ¿qué porosidad máxima permite cumplir una resistencia mínima y cuánto ligante hay que transportar?

📘 **Dónde se aprende** (1 clase): [B84-C37 · Compuestos y aglomerantes a base de regolito](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md).

### COTS

- El COTS (*commercial off-the-shelf*) es un componente comercial no diseñado para el espacio.

🎯 **Por qué importa (clase B95-C02):** Un componente comercial puede funcionar bien en tierra y degradarse o fallar en órbita. La decisión central: ¿qué componente comercial se puede usar en esta misión, con qué margen de radiación y con qué fiabilidad del conjunto?

📘 **Dónde se aprende** (1 clase): [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### Couette

- El flujo de Couette lo arrastra una placa; el de Poiseuille lo impulsa un gradiente de presión.

💡 **Cómo se explica en la clase [B79-C03](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md):**
- Paso 1 · Término de Couette. `0,5 × 0,2 = 0,10 m/s`.
- Obtener el perfil de Couette–Poiseuille analítico.
- 🎯 **Por qué importa:** Casi todo flujo de ingeniería tiene paredes, y en ellas la viscosidad impone velocidad cero. Sin Navier–Stokes no hay arrastre ni fricción ni calentamiento por pared.

📘 **Dónde se aprende** (1 clase): [B79-C03 · Ecuaciones de Navier-Stokes](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md).

### Covalente polar

- Si los electrones se reparten de forma desigual, el enlace es covalente polar.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- E -->|"Sí"| F["Covalente polar (cargas parciales)"]
- Si ambos atraen electrones, los comparten (covalente); si el reparto es desigual, el enlace es polar.
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Covarianza

- La covarianza estimada de los parámetros es `σ̂² (JᵀJ)⁻¹`.
- La covarianza `Cov(X,Y) = E[(X − E[X])(Y − E[Y])] = E[XY] − E[X]E[Y]` mide la variación conjunta; su unidad es el producto de las unidades; el GUM la define y tabula su papel en la propagación (S1, C.3.4; 5.2.2).
- Su inversa es la covarianza (cota de Cramér–Rao).
- *(y 10 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C05](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md):**
- Con 1 000 000 de pares normales con `ρ = 0,8`, la correlación simulada es `0,8002` y la covarianza `9,609` (exacta `9,600`).
- La covarianza es la mitad «sin escala» de esa inclinación, y `r` la normaliza.
- ⚠️ **Error frecuente:** Sumar varianzas ignorando la covarianza. Se corrige con 8.3 y el ejercicio 2.
- 🎯 **Por qué importa:** En navegación espacial, la posición y la velocidad estimadas por un filtro no tienen errores independientes: un error de posición hacia delante suele ir acompañado de uno de velocidad. Ignorar esa relación da incertidumbres falsas, a veces demasiado optimistas y a veces demasiado pesimistas.

📘 **Dónde se aprende** (13 clases): [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md); [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md); [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md); [B29-C04 · Astrometría de exoplanetas](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md); [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md) y 7 más.

### Covarianza cruzada

- La covarianza cruzada entre el estado actual y el ruido de proceso del intervalo es lo que las aproximaciones deben tratar.

💡 **Cómo se explica en la clase [B74-C24](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md):**
- Descripción larga: reprocesar en orden es el mejor; usar la medida como actual es el peor; una retrodicción sin correlación cruzada es peor que descartar y deja una covarianza inválida.
- 🎯 **Por qué importa:** Una medida tardía contiene información valiosa pero tratarla mal puede dañar más que descartarla. La decisión central: ¿qué tratamiento de una medida tardía mejora el estimado sin romper la consistencia, y a qué coste?

📘 **Dónde se aprende** (1 clase): [B74-C24 · Medidas retardadas y fuera de secuencia en filtros de estimación](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md).

### Covarianza de los parámetros

- La covarianza de los parámetros es `s²(XᵀX)⁻¹` (S1).

💡 **Cómo se explica en la clase [B12-C10](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md):**
- *Descripción textual:* de los datos y un modelo se minimizan los cuadrados de los residuos; se obtienen los parámetros y la varianza del ruido; con ellos, la covarianza de los parámetros; los residuos se examinan por si muestran patrón; con la covarianza se da una predicción con su incertidumbre.
- Ejercicio 12 · integrador. Elabora tu *informe de ajuste*: elige datos sintéticos que sigan una recta y otros una exponencial; ajusta cada uno, tabula parámetros con errores típicos, verifica la covarianza por simulación, examina los residuos y da una predicción fuera del rango con su incertidumbre y su advertencia.
- 🎯 **Por qué importa:** Casi todo en ciencias espaciales es un ajuste: la deriva de un oscilador, la curva de luz de un tránsito, la degradación de una celda solar, la relación período–luminosidad. Un ajuste sin incertidumbre de parámetros ni diagnóstico de residuos es sólo una línea dibujada.

📘 **Dónde se aprende** (1 clase): [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md).

### Covarianza de medida

- La covarianza de medida es `R` (ruido) o `H P Hᵀ` (efecto de la incertidumbre del estado).

💡 **Cómo se explica en la clase [B74-C01](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md):**
- Propagar una covarianza de posición a covarianza de medida con `H P Hᵀ`.
- Ejercicio 8 · autónomo. Para `σ_ρ = 5 m` y `σ_r = 100 m`, ¿qué domina la covarianza de la medida esperada?
- 🎯 **Por qué importa:** Todo método de B74 (mínimos cuadrados, filtros, validación) deriva del par `h` y `H = ∂h/∂x`. La decisión central: ¿qué función y qué derivadas describen la medida, y cómo sé que están bien escritas antes de dárselas a un estimador?

📘 **Dónde se aprende** (1 clase): [B74-C01 · Modelos de observación](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md).

### Covarianza del ruido de medida

- `Q` es la covarianza del ruido de proceso (cuánto se aparta el movimiento real del modelo) y `R` la covarianza del ruido de medida (S1).

🎯 **Por qué importa (clase B15-C17):** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.

📘 **Dónde se aprende** (1 clase): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md).

### Covarianza del ruido de proceso

- `Q` es la covarianza del ruido de proceso (cuánto se aparta el movimiento real del modelo) y `R` la covarianza del ruido de medida (S1).

🎯 **Por qué importa (clase B15-C17):** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.

📘 **Dónde se aprende** (1 clase): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md).

### Covarianza formal

- La covarianza formal `(JᵀWJ)⁻¹` mide la incertidumbre bajo el modelo lineal.
- La covarianza formal `P = (HᵀWH)⁻¹` supone modelo lineal y ruido bien descrito.

💡 **Cómo se explica en la clase [B58-C07](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md):**
- Límites: dos cuerpos, Tierra circular, sin aberración ni retardo de luz; covarianza formal lineal.
- 🎯 **Por qué importa:** Una órbita ajustada es el producto central de la defensa planetaria: de ella salen las predicciones y las probabilidades. La decisión central: ¿cuántas observaciones y qué arco hacen falta para que la órbita sea fiable, y cómo se sabe que el ajuste es bueno?

📘 **Dónde se aprende** (2 clases): [B58-C07 · Determinación de órbitas](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md); [B74-C07 · Ajuste por mínimos cuadrados](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md).

### CPI

- El CPI es `EV/AC`; el SPI, `EV/PV`.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- `CPI = 0,7950` (se gasta más de lo que se gana) y `SPI = 0,8368` (hay atraso).
- Si el rendimiento de costo se mantiene, `EAC = BAC/CPI = 100,63` Mum (ETC `40,63`, VAC `-20,63`), idéntico a `AC + (BAC − EV)/CPI` (error `0,0e+00`).
- ⚠️ **Error frecuente:** Confundir gastar con avanzar. Se corrige con 8.2: el CPI compara lo ganado con lo gastado.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?

📘 **Dónde se aprende** (1 clase): [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### CR3BP

- El CR3BP estudia una masa despreciable bajo la gravedad de dos cuerpos masivos en órbita circular mutua.

💡 **Cómo se explica en la clase [B73-C01](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md):**
- Escribir las ecuaciones del CR3BP adimensional con el parámetro de masa `μ`.
- La evidencia es la ficha del CR3BP Tierra–Luna con control de conservación del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Con tres cuerpos no hay solución cerrada, pero sí una cantidad conservada que organiza todo lo demás: puntos de equilibrio, regiones prohibidas y transferencias de bajo costo. La decisión central: ¿cuándo basta el modelo de tres cuerpos restringido, y cómo sé que mi integración no inventa dinámica?

📘 **Dónde se aprende** (1 clase): [B73-C01 · Problema restringido de tres cuerpos](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md).

### Crank–Nicolson

- La fotoevaporación es la pérdida de gas calentado por radiación. Crank–Nicolson es un esquema implícito de segundo orden.
- La fracción termalizada `η` es la parte que se convierte en calor. Crank–Nicolson es un esquema implícito de segundo orden.
- El esquema Crank–Nicolson avanza en el tiempo promediando la derivada al inicio y al final del paso (orden 2).

💡 **Cómo se explica en la clase [B23-C04](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md):**
- El error total tiene una parte espacial (`∝ Δz²`) y otra temporal (`∝ Δt²` en Crank–Nicolson).
- La diferencia con Crank–Nicolson (2000 pasos) es `5,8 × 10⁻⁷ K`: es el error temporal de Crank–Nicolson.
- 🎯 **Por qué importa:** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.

📘 **Dónde se aprende** (3 clases): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md); [B52-C09 · Dispersión de discos de gas](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md); [B52-C17 · Colisiones y evolución térmica](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md).

### Cráter aparente

- Un cráter aparente es el visible hoy.

💡 **Cómo se explica en la clase [B61-C02](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md):**
- Con `d/D` = 0,2, un cráter aparente de 1000 m tiene 200 m de profundidad y un volumen de 8,27×10⁷ m³; su radio de curvatura vale 1,45 `R`.
- Distinguir el cráter transitorio del aparente y usar el factor de ensanchamiento.
- ⚠️ **Error frecuente:** Confundir cráter transitorio y aparente. Se corrige con 8.2.
- 🎯 **Por qué importa:** Medir un cráter es medir un bol, pero lo que se ve es el bol después de colapsar y rellenarse. La decisión central: ¿cuánto volumen tenía la cavidad original y cuánto se perdió en el relleno de brecha?

📘 **Dónde se aprende** (1 clase): [B61-C02 · Cráteres simples: morfología y formación](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md).

### Cráter simple

- El cráter simple conserva forma de cuenco.

💡 **Cómo se explica en la clase [B58-C15](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md):**
- El escalamiento recordado da un cráter transitorio de `6.01 km` y uno final simple de `7.51 km`.
- Crater transitorio D_tc = 6.010 km ; crater simple final = 7.512 km
- 🎯 **Por qué importa:** Para decidir si una desviación es necesaria hay que saber qué haría el impacto. La decisión central: ¿cómo escalan la energía y el cráter con el tamaño, la velocidad y el ángulo?

📘 **Dónde se aprende** (1 clase): [B58-C15 · Modelos de impacto planetario](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md).

### Cráter transitorio

- El cráter transitorio es la cavidad máxima antes del colapso.

💡 **Cómo se explica en la clase [B58-C15](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md):**
- Con `v = 30 km/s` y la misma energía (`6756 Mt`), el cuerpo mediría `359 m` y el cráter transitorio sería `5.82 km`: la energía no basta, importan el tamaño y la velocidad por separado.
- El escalamiento recordado da un cráter transitorio de `6.01 km` y uno final simple de `7.51 km`.
- 🎯 **Por qué importa:** Para decidir si una desviación es necesaria hay que saber qué haría el impacto. La decisión central: ¿cómo escalan la energía y el cráter con el tamaño, la velocidad y el ángulo?

📘 **Dónde se aprende** (2 clases): [B58-C15 · Modelos de impacto planetario](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md); [B61-C01 · Dinámica de eyección y escalado de cráteres](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md).

### CRC

- Prueba de extremo a extremo: prueba de un hilo operativo completo entre elementos e interfaces externas. CRC: código de redundancia cíclica.

💡 **Cómo se explica en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- CCSDS publica protocolos de datos espaciales, pero sus recomendaciones no se consultaron; el CRC-16/CCITT-FALSE (polinomio 0x1021, valor inicial 0xFFFF) y su valor de comprobación 0x29B1 son datos de uso general no consultados en una fuente concreta.
- El laboratorio calcula `CRC("123456789") = 0x29B1`, igual al valor de comprobación.
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?

📘 **Dónde se aprende** (1 clase): [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### CRC-15

- El CRC-15 usa el polinomio `0x4599`.

💡 **Cómo se explica en la clase [B88-C07](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md):**
- Implementar el CRC-15 del CAN y el relleno.
- Ejercicio 10 · transferencia. Transferencia. ¿Qué cambia si el CRC-15 se calcula con un polinomio distinto?
- 🎯 **Por qué importa:** El bus fija cuánta telemetría y cuántos comandos caben y con qué retardo. La decisión central: ¿cuál es el caudal útil y el peor tiempo de trama de cada bus para mi carga?

📘 **Dónde se aprende** (1 clase): [B88-C07 · Buses I2C SPI CAN y SpaceWire](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md).

### CRC-16

- El CRC-16 con polinomio `0x1021` e inicio `0xFFFF` da `0x29B1` para la cadena `123456789`.
- El CRC-16 valida el registro.
- El CRC-16 usa el polinomio `x¹⁶ + x¹² + x⁵ + 1` (0x1021).

💡 **Cómo se explica en la clase [B88-C08](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md):**
- El CRC-16 de `123456789` es `0x29B1` (valor de comprobación del propio laboratorio).
- Con CRC-16, un error de un byte (ráfaga ≤ 16 bits) siempre se detecta; esto lo comprueba el laboratorio, no una norma.
- 🎯 **Por qué importa:** Sin telemetría no se ve la salud de la nave; con demasiada, se satura el enlace. La decisión central: ¿qué parámetros, a qué frecuencia y con qué protección caben en el enlace sin perder los críticos?

📘 **Dónde se aprende** (3 clases): [B88-C08 · Telemetría interna](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md); [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md); [B89-C12 · Telecomandos CCSDS](../programa/clases/B89/B89-C12-telecomandos-ccsds/CLASE.md).

### CRC-32

- SHA-256: hash criptográfico de 256 bits. CRC-32: código cíclico de 32 bits.

💡 **Cómo se explica en la clase [B48-C17](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md):**
- El CRC-32 detecta con seguridad cualquier cambio de un bit, pero no protege de una alteración deliberada; para eso se usa SHA-256.
- El SHA-256 de «abc» es ba7816bf8f01cfea…, y el CRC-32 de «123456789» es 0xcbf43926.
- 🎯 **Por qué importa:** Un archivo que se corrompe en silencio contamina todos los análisis posteriores. La decisión central: ¿qué suma de verificación y con cuántos bits detecta la corrupción?

📘 **Dónde se aprende** (1 clase): [B48-C17 · Gestión de archivos observacionales](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md).

### CRC-8

- El CRC-8 con polinomio `0x07` da `0xF4` para `123456789`.

💡 **Cómo se explica en la clase [B88-C09](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md):**
- Ejercicio 6 · autónomo. Calcula el CRC-8 de un solo byte `0x00` con polinomio `0x07`.
- El script [telecomandos_modos.py](telecomandos_modos.py) imprime la matriz estado–comando, ejecuta un guion de nueve telecomandos con CRC y secuencia y comprueba 11 celdas aceptadas, el modo final `SAFE` y el CRC-8 de prueba `0xF4`.
- 🎯 **Por qué importa:** Un telecomando aceptado en el estado equivocado puede dañar la nave; uno rechazado en el estado correcto puede perderla. La decisión central: ¿qué comando es válido en cada modo y qué comprobaciones lo protegen?

📘 **Dónde se aprende** (1 clase): [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md).

### Creciente

- Una función es creciente si, al aumentar `x`, `f(x)` no disminuye.
- El ángulo de fase `i` es el ángulo Sol–Luna–Tierra visto desde la Luna. Creciente es el tramo de Luna nueva a llena;

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Comprueba: la función creciente da `P(292) ≈ 996 d`, coherente con redondeo.
- Componer funciones y hallar la inversa de una función creciente.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.

📘 **Dónde se aprende** (2 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md).

### Crecimiento aditivo

- El crecimiento aditivo añade módulos sin retirar los existentes.

🎯 **Por qué importa (clase B109-C05):** Si el primer módulo no admite ampliación, crecer obliga a desechar lo construido. La decisión central: ¿qué funciones se duplican con la tripulación, cuáles no, y cómo se añaden módulos sin rediseñar?

📘 **Dónde se aprende** (1 clase): [B109-C05 · Crecimiento modular y escalabilidad de asentamientos](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md).

### Crecimiento del núcleo

- El crecimiento del núcleo es `dM_c/dt = L/(X ε c²)` si toda la luminosidad viene de la capa.

💡 **Cómo se explica en la clase [B24-C16](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md):**
- Estimar el crecimiento del núcleo por quemado de hidrógeno en capa.
- Ejercicio 12 · integrador. Elabora tu *ficha de una gigante roja*: elige `M`, `L` y `T_ef` (ilustrativos), calcula `R`, `g`, `ρ̄`, `t_dyn`, `Δν` por escala, el ritmo de crecimiento del núcleo y nombra dos fenómenos omitidos.
- 🎯 **Por qué importa:** Una gigante roja es mucho mayor y más luminosa que su estrella original y tiene una densidad media ínfima. Entender su tamaño, su gravedad y cómo crece su núcleo permite interpretar las gigantes observadas, usarlas como sondas asterosísmicas y anticipar el destino del Sol.

📘 **Dónde se aprende** (1 clase): [B24-C16 · Gigantes rojas](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md).

### Crecimiento descontrolado

- El crecimiento descontrolado (*runaway*) es el régimen en que el cuerpo más masivo crece más rápido en términos relativos.

🎯 **Por qué importa (clase B52-C05):** El tiempo de crecimiento decide si un núcleo existe antes de que el gas se disipe. La decisión central: ¿cómo cambia la tasa de acreción con la masa y cuándo se detiene?

📘 **Dónde se aprende** (1 clase): [B52-C05 · Crecimiento de embriones planetarios](../programa/clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md).

### Crecimiento lineal

- El crecimiento lineal `D(a)` describe cómo `δ` crece mientras `δ ≪ 1`.

💡 **Cómo se explica en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- Escribir la ecuación de crecimiento lineal.
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.

📘 **Dónde se aprende** (1 clase): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md).

### Crecimiento logístico

- Confianza: probabilidad de detectar. Crecimiento logístico: curva en S.

💡 **Cómo se explica en la clase [B106-C28](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md):**
- G["crecimiento logistico"] --> T["t hasta el umbral"]
- Calcular el crecimiento logístico y el tiempo hasta el umbral de acción.
- 🎯 **Por qué importa:** Una muestra pequeña puede no contener ningún organismo de una contaminación real, y un muestreo espaciado deja crecer la población. La decisión central: ¿qué volumen y qué intervalo de muestreo dan una confianza dada de detectar una contaminación antes de que supere el umbral de acción?

📘 **Dónde se aprende** (1 clase): [B106-C28 · Monitoreo microbiológico de agua y superficies del hábitat](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md).

### Crecimiento, mantenimiento y supervivencia

- Un tiempo de renovación es lo que tarda en renovarse una unidad de carbono celular. Crecimiento, mantenimiento y supervivencia son tres regímenes de actividad.

💡 **Cómo se explica en la clase [B64-C03](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md):**
- Si a 25 °C una unidad de carbono se renovara en 1 h (supuesto sintético), el régimen de crecimiento a −40 °C tardaría 26,9 años, el de mantenimiento 2,69·10⁴ años y el de supervivencia 2,69·10⁷ años.
- Price y Sowers [S1] compararon tasas metabólicas de microbios en muchos ambientes fríos y no hallaron una temperatura mínima de metabolismo; según su resumen, crecimiento, mantenimiento y supervivencia siguen una misma energía de activación de unos 110 kJ y se escalan aproximadamente como 10⁶ : 10³ : 1.
- 🎯 **Por qué importa:** El frío no detiene la vida de golpe: la ralentiza. La pregunta motivadora: ¿cuánto más lento es el metabolismo a −40 °C que a 25 °C, y qué significa «vivir» a esa velocidad?

📘 **Dónde se aprende** (1 clase): [B64-C03 · Psicrófilos y vida en frío](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md).

### Crecimiento por madurez

- El crecimiento por madurez es la reserva de cada equipo según lo conocido que sea (comercial, modificado, nuevo).

💡 **Cómo se explica en la clase [B86-C19](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md):**
- S["subsistemas y modos"] --> M["crecimiento por madurez"]
- *Descripción textual:* los subsistemas, con su crecimiento por madurez y la reserva de sistema, dan la demanda por fase y la potencia de ala requerida; con la generación de cada fase resultan los márgenes y la fase crítica; un Monte Carlo del crecimiento estima la probabilidad de exceso.
- 🎯 **Por qué importa:** Un presupuesto es un compromiso de ingeniería: cada subsistema promete una potencia que todavía puede crecer. Las reservas por madurez evitan que el ala quede corta cuando una carga nueva consume más de lo previsto.

📘 **Dónde se aprende** (1 clase): [B86-C19 · Presupuesto de potencia de misión](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md).

### Crecimiento secular

- El crecimiento secular es el que aumenta con `t`.

🎯 **Por qué importa (clase B72-C19):** Las incertidumbres de la órbita inicial y de los parámetros determinan cuánto tiempo vale una predicción. La decisión central: ¿cómo crece con el tiempo el error de posición por cada fuente de incertidumbre y cuál de ellas manda?

📘 **Dónde se aprende** (1 clase): [B72-C19 · Análisis de sensibilidad orbital](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md).

### Crédito

- Un crédito nombra al autor, enlaza la fuente y la licencia, e indica si hubo cambios.

💡 **Cómo se explica en la clase [B130-C01](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md):**
- ESO publica sus imágenes bajo CC BY 4.0 y pide un crédito completo y visible, con enlace en línea, e indicar si se modificó el material, también si se usó IA.
- *Descripción textual:* cada dato pasa por una ficha; si la auditoría la encuentra completa se dibuja con una escala honesta y su crédito; si no, se corrige o se rotula como ilustrativo.
- 🎯 **Por qué importa:** Comunicar con imágenes exige mantener la fuente y la incertidumbre; la clase de comunicación general no entra en cómo se audita una pieza visual. La decisión central: ¿qué debe llevar cada cifra de una infografía para que otra persona pueda verificarla, y qué diseño la deforma?

📘 **Dónde se aprende** (1 clase): [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md).

### Crédito de servicio

- El crédito de servicio compensa al cliente.

💡 **Cómo se explica en la clase [B124-C21](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de acuerdo de nivel de servicio de un producto de datos*: componentes con MTBF y MTTR, disponibilidad en serie y con redundancia, presupuesto de error, simulación, plazo, créditos esperados y lista de qué es sintético, con el aviso de que no es un contrato.
- 🎯 **Por qué importa:** B124 trata propuestas de valor, pero un servicio de observación se compromete con plazos y calidad, y esos compromisos tienen una aritmética precisa. La decisión central: ¿qué disponibilidad y qué plazo puede prometer un servicio sin incumplir seguido y cuánto cuesta cada incumplimiento?

📘 **Dónde se aprende** (1 clase): [B124-C21 · Acuerdos de nivel de servicio para productos de datos](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md).

### Cribado

- El cribado es la aplicación de esos criterios, primero al título y resumen y luego al texto completo.
- El cribado es el filtro rápido previo al cálculo fino.
- El cribado descarta pares.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- Cuenta en cada etapa: identificados; duplicados eliminados; cribados; excluidos por cada motivo; incluidos.
- Debe cumplirse una conservación sencilla: `identificados − duplicados = cribados = incluidos + excluidos`.
- ⚠️ **Error frecuente:** Contar mal el flujo. Restar dos veces o mezclar cribados con identificados.
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.

📘 **Dónde se aprende** (4 clases): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md); [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md); [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md); [B119-C13 · Vigilancia y conciencia situacional espacial](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md).

### Crimen inverso

- Si son el mismo, hay crimen inverso.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Wirgin define el crimen inverso como usar los mismos componentes teóricos, o casi los mismos, para generar los datos y para invertirlos en un problema inverso, y recuerda que Colton y Kress lo consideran una práctica trivial que debe evitarse (S3).
- Definir el crimen inverso y reconocerlo en un experimento.
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Criógeno

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C13](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md):**
- *Descripción textual:* la radiación entre escudos y la conducción por soportes suman una carga que consume el criógeno.
- Con emisividad `0,02`, área `0,2 m²`, 4 soportes y 50 kg de criógeno (ilustrativos), la carga parásita baja de `818,2 mW` sin escudos a `28,0 mW` con 40 escudos, y la vida pasa de `0,040` a `1,182 años`.
- 🎯 **Por qué importa:** Cada vatio parásito acorta la vida de un criógeno. La decisión central: ¿cuántos escudos y qué soportes bastan para una vida útil dada?

📘 **Dónde se aprende** (1 clase): [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md).

### Criomagma

- El criomagma es el material líquido o semilíquido que sube.

🎯 **Por qué importa (clase B70-C06):** El agua líquida es más densa que el hielo, así que no sube sola. La decisión central: ¿qué presión extra y qué mecanismo hacen falta para que el agua llegue a la superficie?

📘 **Dónde se aprende** (1 clase): [B70-C06 · Criovulcanismo: lavas heladas y emisión de volátiles](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md).

### Criovulcanismo

- El criovulcanismo es la erupción de volátiles helados o agua en lugar de silicatos.

💡 **Cómo se explica en la clase [B70-C06](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md):**
- La evidencia es la ficha del criovulcanismo del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha del criovulcanismo*: gravedad, escape, sobrepresión, chorro y límites.
- 🎯 **Por qué importa:** El agua líquida es más densa que el hielo, así que no sube sola. La decisión central: ¿qué presión extra y qué mecanismo hacen falta para que el agua llegue a la superficie?

📘 **Dónde se aprende** (1 clase): [B70-C06 · Criovulcanismo: lavas heladas y emisión de volátiles](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md).

### Criterio

- Un criterio es una propiedad que se compara (reserva, pendiente, iluminación, riesgo).
- El criterio es el nivel de desempeño exigido.
- Un criterio es un aspecto de comparación.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- Para un criterio donde más es mejor, `z = (x − mín)/(máx − mín)`; donde menos es mejor, `z = 1 − (x − mín)/(máx − mín)`.
- S7 (90 kt, 7°, 35 %, riesgo 5) está dominado por S4 (95 kt, 6°, 40 %, riesgo 4): S4 es mejor en los cuatro criterios.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?

📘 **Dónde se aprende** (6 clases): [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md); [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md); [B104-C09 · Entrenamiento en simuladores](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md); [B124-C04 · Diseño de propuesta de valor](../programa/clases/B124/B124-C04-diseno-de-propuesta-de-valor/CLASE.md); [B128-C11 · Auditoría de accesibilidad de un recurso educativo](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md).

### Criterio de aceptación

- El criterio de aceptación es la regla de decisión fijada de antemano: aquí, `z ≤ 2` en todos los blancos.
- El criterio de aceptación es una condición medible (p. ej. «error ≤ 10⁻³ au a 91 d») fijada antes de comparar.
- Un criterio de aceptación es una condición medible con umbral.

💡 **Cómo se explica en la clase [B13-C20](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md):**
- Definir un criterio de aceptación `z ≤ 2` por blanco.
- 🎯 **Por qué importa:** Un telémetro calibrado, con presupuesto y registro, puede seguir fallando: un error de escala oculto que la calibración en una sola distancia no ve.

📘 **Dónde se aprende** (3 clases): [B13-C20 · Validación de una cadena de medida](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md); [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md); [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Criterio de beneficio

- Un criterio de beneficio es mejor cuanto mayor; uno de coste es mejor cuanto menor.

💡 **Cómo se explica en la clase [B95-C03](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md):**
- Normalizar criterios de beneficio y de coste a `[0, 1]`.
- 🎯 **Por qué importa:** Elegir una plataforma «porque la conocemos» no se puede defender. La decisión central: ¿qué plataforma cumple lo imprescindible, cuál puntúa mejor y cuánto depende ese resultado de los pesos que elegimos?

📘 **Dónde se aprende** (1 clase): [B95-C03 · Selección y comparación de plataformas](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md).

### Criterio de comparación

- Un criterio de comparación es la regla que decide qué modelo describe mejor los datos.

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- Ese es el criterio de comparación: el que deje menor residuo en escala logarítmica, declarado antes de calcular.
- Ejercicio 8. ¿Por qué el criterio de comparación se escribe antes de calcular?
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?

📘 **Dónde se aprende** (1 clase): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md).

### Criterio de comprobación

- Un criterio de comprobación es una prueba objetiva que dice si el requisito se cumple.
- Un requisito es una condición que la campaña debe cumplir; debe ser verificable: tener un criterio de comprobación (un número o un sí/no) y un método de comprobación.

💡 **Cómo se explica en la clase [B08-C20](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md):**
- Cada uno tiene criterio, método de comprobación y fuente: R1, seguridad solar (nadie mira el Sol sin protección certificada verificada; revisión por una segunda persona;
- Escribir requisitos de una campaña con su criterio y método de comprobación.
- 🎯 **Por qué importa:** Una salida sin plan termina en una noche perdida o en un accidente. La pregunta motivadora: ¿cómo preparo una salida de observación para que sea segura, útil, accesible y reproducible?

📘 **Dónde se aprende** (2 clases): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md).

### Criterio de correlación

- El criterio de correlación (aquí `|ΔT| ≤ 3 K`, ilustrativo) acepta o rechaza el modelo.

💡 **Cómo se explica en la clase [B85-C27](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. Un criterio de correlación de `±3 K` ¿es universal?
- Ejercicio 12 · integrador. Integrador. Elabora tu *informe de correlación y margen térmico*: residuos, ajuste, criterio, Monte Carlo, margen y lista de lo sintético.
- 🎯 **Por qué importa:** Un modelo sin correlación no sirve para predecir y un margen sin incertidumbre es una apuesta. La decisión central: ¿el modelo reproduce el ensayo dentro del criterio y cuánto margen queda tras la incertidumbre?

📘 **Dónde se aprende** (1 clase): [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md).

### Criterio de daño

- El criterio de daño compara la interferencia con el ruido.

🎯 **Por qué importa (clase B118-C17):** La radioastronomía opera en bandas donde la ITU asigna protección, pero las constelaciones numerosas y sus emisiones no deseadas pueden degradar la sensibilidad. La decisión central: ¿cuánto debe bajar una emisión para quedar por debajo del umbral de daño y de qué depende ese umbral?

📘 **Dónde se aprende** (1 clase): [B118-C17 · Interferencia radioastronómica](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md).

### Criterio de detección

- El objetivo científico y el criterio de detección (5σ).

🎯 **Por qué importa (clase B46-C20):** Un proyecto viable cuadra objetivo, sensibilidad, tiempo y datos. La decisión central: ¿cuánto tiempo de observación pide el objetivo y con qué margen?

📘 **Dónde se aprende** (1 clase): [B46-C20 · Proyecto de observación radioastronómica](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md).

### Criterio de éxito

- El criterio de éxito combina condiciones (agua y ciencia).

💡 **Cómo se explica en la clase [B104-C20](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md):**
- Fallas independientes y del mismo tamaño, sin cascadas, sin consumos que cambien por fatiga o estrés, sin reabastecimiento ni abortos, y criterios de éxito inventados.
- *Descripción textual:* la tasa de fallas determina cuántas ocurren; cada una consume horas y agua; junto con el consumo variable, determinan si se cumple el criterio de éxito.
- 🎯 **Por qué importa:** Cada margen parece suficiente por separado, pero las fallas consumen a la vez agua y tiempo. La decisión central: ¿hasta qué tasa de fallas mantiene la misión una probabilidad de éxito alta, y cuál recurso se agota primero?

📘 **Dónde se aprende** (1 clase): [B104-C20 · Misión tripulada simulada](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md).

### Criterio de Gladman

- El criterio de Gladman para dos planetas en órbitas circulares es `Δ > 2√3 ≈ 3,46`.

💡 **Cómo se explica en la clase [B73-C17](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md):**
- El criterio de Gladman no se consultó en su fuente y solo se contrasta numéricamente.
- Ejercicio 10 · transferencia. Transferencia. Un colega usa el criterio de Gladman para tres planetas.
- 🎯 **Por qué importa:** Muchos sistemas exoplanetarios son compactos y su existencia depende de no haberse desestabilizado. Un criterio simple de separación permite descartar configuraciones inviables antes de integrar.

📘 **Dónde se aprende** (1 clase): [B73-C17 · Estabilidad de sistemas exoplanetarios](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md).

### Criterio de Hill

- El criterio de Hill pide que el radio de la partícula iguale su esfera de Hill: `1,442 R (ρ_M/ρ_m)^{1/3}`.

💡 **Cómo se explica en la clase [B73-C16](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md):**
- El criterio de Hill cae entre los dos límites, como debe.
- Calcular los límites de Roche rígido y fluido y el criterio de Hill.
- 🎯 **Por qué importa:** Un anillo existe donde las mareas impiden que las partículas se junten, se ensancha por viscosidad y se estructura por resonancias con las lunas. La decisión central: ¿qué escalas fijan dónde hay un anillo, cuánto dura y dónde lo moldean las lunas?

📘 **Dónde se aprende** (1 clase): [B73-C16 · Dinámica de anillos](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md).

### Criterio de Hillas

- El criterio de Hillas limita `E_max` por el tamaño y el campo de la fuente.
- El criterio de Hillas limita la energía por el tamaño y el campo.

🎯 **Por qué importa (clase B28-C04):** El origen de los rayos cósmicos de mayor energía sigue abierto; el criterio de Hillas descarta fuentes y la anisotropía apunta a regiones. La decisión central: ¿qué fuentes pueden alcanzar una energía dada y qué anisotropía se puede detectar con un número dado de eventos?

📘 **Dónde se aprende** (2 clases): [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md); [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md).

### Criterio de información de Akaike

- El criterio de información de Akaike es `AIC = 2k − 2 ln L_max`, con `k` parámetros; el bayesiano es `BIC = k ln n − 2 ln L_max`, con `n` datos.
- El criterio de información de Akaike (AIC) penaliza los parámetros: `n ln(RSS/n) + 2k`.

🎯 **Por qué importa (clase B12-C22):** Un modelo más flexible siempre ajusta mejor los datos que uno más sencillo, así que el ajuste solo no sirve para elegir. Hace falta penalizar la complejidad: ¿vale la pena el parámetro extra?

📘 **Dónde se aprende** (2 clases): [B12-C22 · Comparación de modelos: evidencia bayesiana y criterios de información](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md); [B15-C21 · Series temporales multivariadas y regresión dinámica](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md).

### Criterio de ligada

- El criterio de ligada de este laboratorio: la distancia a la Luna no supera `R_H` en 30 d.

💡 **Cómo se explica en la clase [B76-C03](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md):**
- Límites: CR3BP plano, 30 d, un solo criterio de ligada; sin Sol ni campo no esférico.
- 🎯 **Por qué importa:** Un orbitador lunar bajo y un satélite de relevo alto obedecen leyes distintas. La decisión central: ¿hasta qué distancia de la Luna puede mantenerse una órbita casi circular y qué sentido de giro resiste mejor la perturbación terrestre?

📘 **Dónde se aprende** (1 clase): [B76-C03 · Órbitas alrededor de la Luna](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md).

### Criterio de muestreo

- El criterio de muestreo usado aquí (supuesto del ejemplo) pide al menos dos píxeles por rasgo: `GSD ≤ rasgo/2`.

💡 **Cómo se explica en la clase [B83-C01](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md):**
- Derivar la resolución en tierra (GSD) a partir del tamaño del rasgo con un criterio de muestreo explícito.
- Límites: difracción sin aberraciones ni ruido; criterio de muestreo de ejemplo; puntajes inventados; no hay una misión real detrás.
- 🎯 **Por qué importa:** Un equipo sabe que quiere «mirar la costa» pero no cuánto debe resolver ni qué objetivo merece el presupuesto. La decisión central: ¿qué requisito de medición se deduce de la pregunta científica y qué objetivo conviene perseguir primero?

📘 **Dónde se aprende** (1 clase): [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md).

### Criterio de Rayleigh

- El criterio de Rayleigh es un PV de λ/4.
- El ruido de fotones (o de disparo) es de tamaño `√N`; el criterio de Rayleigh da el límite de difracción `1,22 λ/D`.
- El criterio de Rayleigh: separación igual al primer cero.

💡 **Cómo se explica en la clase [B41-C12](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué criterio da el menor ángulo, Rayleigh, Sparrow o Dawes?
- ⚠️ **Error frecuente:** Usar Rayleigh como límite absoluto. Es un criterio, no un muro.
- 🎯 **Por qué importa:** La difracción fija el mejor detalle posible. La decisión central: ¿cuándo se resuelven dos estrellas y qué cuesta una obstrucción?

📘 **Dónde se aprende** (4 clases): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md); [B50-C14 · Criterios de aceptación: Strehl, error de frente de onda y especificaciones](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md); [B57-C04 · Satélites ópticos de observación](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md).

### Criterio de rechazo de datos

- Un criterio de rechazo de datos es la regla, escrita antes, para descartar una lectura.

🎯 **Por qué importa (clase B01-C20):** Entender el método no es lo mismo que aplicarlo. Cuando mides de verdad, aparecen problemas que los ejercicios no tienen: el cielo se nubla, el palo no está del todo vertical, la regla se mueve, los datos no coinciden con lo que predijiste.

📘 **Dónde se aprende** (1 clase): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md).

### Criterio de refinamiento

- Un criterio de refinamiento decide qué celdas se dividen.

💡 **Cómo se explica en la clase [B21-C05](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md):**
- Por eso el criterio equivale a fijar una tolerancia de error `≈ C/2`, y hay refinamiento solo mientras no se alcance.
- 🎯 **Por qué importa:** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Criterio de refutación

- Un criterio de refutación es el resultado que, de ocurrir, te hace rechazar la hipótesis.

💡 **Cómo se explica en la clase [B01-C07](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md):**
- Paso 4 · Criterio de refutación. Se rechaza si `|R − 1| ≤ 2σ_R`; se mantiene si `|R − 1,116| ≤ 2σ_R` y no es compatible con 1.
- Distinguir hipótesis, predicción y criterio de refutación.
- 🎯 **Por qué importa:** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.

📘 **Dónde se aprende** (1 clase): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md).

### Criterio de Routh–Hurwitz

- El arreglo de Routh es una tabla construida con los coeficientes; el criterio de Routh–Hurwitz dice que el número de cambios de signo en su primera columna es el número de raíces con parte real positiva.

💡 **Cómo se explica en la clase [B16-C08](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md):**
- python programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/arreglo_de_routh.py
- 🎯 **Por qué importa:** Al diseñar un lazo, la ganancia `K` es una incógnita que quieres elegir. Calcular las raíces para cada `K` es posible con un computador, pero no da la frontera: el valor exacto de `K` por encima del cual el sistema se desestabiliza.

📘 **Dónde se aprende** (1 clase): [B16-C08 · Criterio de Routh-Hurwitz](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md).

### Criterio de Schwarzschild

- El criterio de Schwarzschild dice que una capa es inestable si su gradiente real `−dT/dz` supera `Γ`.
- El criterio de Schwarzschild dice que hay convección si `∇_rad > ∇_ad`.

💡 **Cómo se explica en la clase [B24-C05](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md):**
- El criterio de Schwarzschild se cumple en las capas externas, donde `κ` es alta y `T` baja, aunque en el interior profundo sea radiativo.
- 🎯 **Por qué importa:** La energía generada en el núcleo tarda milenios en salir y el modo de transporte decide la estructura: si el interior de una estrella es convectivo, su composición se mezcla; si es radiativo, no. De ello depende cuánto combustible alcanza el núcleo, y por tanto la vida de la estrella.

📘 **Dónde se aprende** (2 clases): [B24-C05 · Transporte radiativo y convectivo](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md); [B54-C05 · Transporte convectivo](../programa/clases/B54/B54-C05-transporte-convectivo/CLASE.md).

### Criterio de Sparrow

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C12](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué criterio da el menor ángulo, Rayleigh, Sparrow o Dawes?
- 🎯 **Por qué importa:** La difracción fija el mejor detalle posible. La decisión central: ¿cuándo se resuelven dos estrellas y qué cuesta una obstrucción?

📘 **Dónde se aprende** (1 clase): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md).

### Criterio de tolerancia

- El criterio de tolerancia pide coma menor que el radio de Airy.

🎯 **Por qué importa (clase B43-C18):** Colimar es ajustar tornillos hasta que el coma deje de verse; el modelo dice cuánto es «suficiente». La decisión central: ¿qué inclinación del primario produce un coma igual al radio de Airy y cuánto desvía un plano inclinado?

📘 **Dónde se aprende** (1 clase): [B43-C18 · Colimación instrumental](../programa/clases/B43/B43-C18-colimacion-instrumental/CLASE.md).

### Criterio necesario

- Un criterio necesario debe cumplirse siempre; uno suficiente basta por sí solo.

💡 **Cómo se explica en la clase [B56-C01](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md):**
- Definir definición operativa, criterio necesario y suficiente, caso límite y coincidencia entre definiciones.
- 🎯 **Por qué importa:** Una misión que busca vida necesita saber qué buscar y qué contará como hallazgo. Si el criterio es vago, cualquier resultado se puede discutir; si es demasiado estrecho, se pasa por alto lo que no se parece a la vida terrestre.

📘 **Dónde se aprende** (1 clase): [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md).

### Criterios de aceptación

- Los criterios de aceptación del ejemplo son: base sin defectos, 100 % de comandos probados y todos los operadores con al menos 32 h.

💡 **Cómo se explica en la clase [B83-C19](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md):**
- Con los tres criterios fallidos la transferencia no se acepta; las acciones son corregir la base, probar los dos comandos con un simulador y completar 8 h al operador con 24 h.
- T["Comandos probados"] --> A["Criterios de aceptacion"]
- ⚠️ **Error frecuente:** Aceptar por calendario. Acepta por criterios cumplidos
- 🎯 **Por qué importa:** Un satélite entregado con una base de datos errónea muestra valores falsos o alarmas inútiles; operadores sin entrenamiento no saben responder. La decisión central: ¿la base de datos, los comandos y las personas están listos, de modo que operaciones pueda recibir el sistema?

📘 **Dónde se aprende** (1 clase): [B83-C19 · Aceptación y transferencia a operaciones](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md).

### Criterios de inclusión y exclusión

- Los criterios de inclusión y exclusión son reglas escritas antes de ver los resultados que deciden qué obra entra al análisis.

💡 **Cómo se explica en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- Redactar criterios de inclusión y exclusión operativos, fijados antes de ver los resultados.
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.

📘 **Dónde se aprende** (1 clase): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md).

### Crítica de fuentes

- La crítica de fuentes es el examen de origen, fecha, propósito y dependencia de un testimonio.

💡 **Cómo se explica en la clase [B132-C01](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md):**
- La evidencia es la matriz de crítica de fuentes con sensibilidad del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *matriz de crítica de fuentes con sensibilidad* para un hecho ficticio con 5 fuentes: tipo, distancia, grupo, sesgo, peso, soporte ingenuo y por grupos, y un barrido de al menos un parámetro.
- 🎯 **Por qué importa:** Un relato histórico es tan fiable como las fuentes que lo sostienen, y tres copias de una misma fuente no son tres fuentes. La decisión central: ¿cuánto apoyo da realmente un conjunto de fuentes a una afirmación y cuánto de ese apoyo es robusto ante cambios razonables de criterio?

📘 **Dónde se aprende** (1 clase): [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Criticidad

- La criticidad mide cuántos nodos caen por una falla.
- Criticidad: consecuencia de un comando.

💡 **Cómo se explica en la clase [B96-C07](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md):**
- Se evalúan `3 × 4 × 5 × 2 = 120` combinaciones (rol, criticidad, cinco listas de aprobaciones, armado sí/no) con la política y con una referencia independiente basada en tablas de mínimos.
- C["Comando y criticidad"] --> R{"Rol minimo?"}
- 🎯 **Por qué importa:** Un comando enviado por la persona equivocada o sin segunda revisión puede perder la misión. La decisión central: ¿qué rol, qué aprobaciones y qué armado exige cada nivel de criticidad y cómo se prueba que la política no tiene huecos?

📘 **Dónde se aprende** (2 clases): [B96-C07 · Telecomandos y autorizaciones](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md); [B119-C16 · Protección de infraestructura crítica](../programa/clases/B119/B119-C16-proteccion-de-infraestructura-critica/CLASE.md).

### Crítico

- Es crítico si su fallo impide la revisión.
- Un criterio crítico bloquea el veredicto si no se cumple.

💡 **Cómo se explica en la clase [B83-C13](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md):**
- SRR: requisitos verificables (≥ 95 %), necesidades con requisito (100 %), requisitos con origen (100 %), CONOPS documentado y estabilidad del orden de necesidades (≥ 70 %, no crítico).
- *Descripción textual:* el estado del proyecto y los umbrales dan criterios evaluados; los críticos fallidos determinan si la revisión está lista y generan acciones, cuyo cierre se estima en semanas.
- ⚠️ **Error frecuente:** Promediar criterios críticos. Un crítico fallido impide la revisión
- 🎯 **Por qué importa:** Una revisión aprobada sin criterios es un trámite; una revisión con criterios medibles es una decisión. La decisión central: ¿el proyecto cumple los criterios de entrada de la SRR y de la PDR y qué falta para llegar?

📘 **Dónde se aprende** (2 clases): [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md); [B128-C11 · Auditoría de accesibilidad de un recurso educativo](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md).

### Críticos

- Los eventos críticos nunca pasan por el limitador.

💡 **Cómo se explica en la clase [B88-C10](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md):**
- Con limitador: registrados `48`, suprimidos `978` (todos del identificador 5) y críticos registrados `2` de `2`.
- E["Evento con id y severidad"] --> Q{"Critico?"}
- ⚠️ **Error frecuente:** Limitar también los críticos. Exímelos del limitador (8.2)
- 🎯 **Por qué importa:** Un sensor que parpadea puede generar miles de eventos y saturar el registro y el enlace, ocultando el único evento importante. La decisión central: ¿cómo se limita el ruido sin perder lo crítico?

📘 **Dónde se aprende** (1 clase): [B88-C10 · Gestión de eventos](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md).

### Cromosfera

- La fotosfera es la capa que emite la luz visible; la cromosfera y la corona están encima.

💡 **Cómo se explica en la clase [B30-C02](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md):**
- Las temperaturas (5772 K nominal de la fotosfera; 10⁴ K y 1,5 × 10⁶ K ilustrativas para cromosfera y corona) y las masas moleculares medias (1,3; 1,2; 0,6) son ilustrativas.
- `T` y `μ` de cromosfera y corona ilustrativos.
- 🎯 **Por qué importa:** La corona caliente es el origen del viento solar y de gran parte de la actividad. Entender por qué no puede estar en reposo conecta el Sol con el medio interplanetario.

📘 **Dónde se aprende** (1 clase): [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md).

### Crónica

- Una crónica es un relato histórico escrito, aquí por cronistas del siglo XVI.
- La carga aguda es el promedio de los últimos 7 días; la crónica, el de 28.

💡 **Cómo se explica en la clase [B02-C05](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md):**
- B["Texto: crónicas del siglo XVI<br/>(escritas por terceros)"] --> D
- El límite: en los Andes, el «diario» de las crónicas fue escrito por quienes ocupaban el territorio, con sus propios sesgos.
- ⚠️ **Error frecuente:** Tomar crónicas como voz indígena. Ejercicio 8.
- 🎯 **Por qué importa:** Hablar de «astronomía andina» en singular es un error: los Andes reúnen sociedades de épocas y regiones muy distintas. La pregunta motivadora es: ¿cómo se estudia respetuosamente un cielo que otra cultura leyó de otra manera, sin imponerle nuestras categorías y sin inventar lo que las fuentes no dicen?

📘 **Dónde se aprende** (2 clases): [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md); [B107-C05 · Prevención de lesiones en entrenamiento y trabajo operativo](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md).

### Crónico

- El estresor agudo `S(t) = 1` durante 2 h y el crónico `S = 0,5` durante 7 días.

💡 **Cómo se explica en la clase [B105-C22](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md):**
- Con `S = 0,5` durante 7 días (`g = 1`), la media diaria sube de 1,000 a 1,341 (+34,1 %) y la amplitud pico-valle baja de 1,156 a 0,926: el estrés crónico eleva el nivel y aplana el ritmo en el modelo.
- Con `g = 1`, el aumento cae al 10 % en 2,74 h; un estresor crónico (+0,5 durante 7 días) sube la media diaria de 1,000 a 1,341 (+34,1 %).
- ⚠️ **Error frecuente:** Confundir estrés agudo y crónico. Efectos distintos en nivel y ritmo.
- 🎯 **Por qué importa:** Una medición de cortisol sin hora del día no se interpreta: el ritmo diario domina. Y un estresor crónico cambia el nivel medio de una forma distinta que uno agudo.

📘 **Dónde se aprende** (1 clase): [B105-C22 · Sistema neuroendocrino y respuesta al estrés en vuelo](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md).

### Cronología

- Una cronología es una lista ordenada de hitos con fecha.
- La cronología `N₁(T)` convierte edad `T` en densidad.

💡 **Cómo se explica en la clase [B70-C04](../programa/clases/B70/B70-C04-vulcanismo-marciano-provincias-edades-y-evolucion/CLASE.md):**
- Las edades reales requieren la cronología publicada y la verificación de la saturación;
- *Descripción textual:* el conteo da una densidad; la cronología la convierte en edad y la fluctuación de Poisson da el intervalo.
- ⚠️ **Error frecuente:** Creer que la cronología es la publicada. Se corrige en la sección 5.
- 🎯 **Por qué importa:** Un conteo de cráteres es un número entero y ruidoso. La decisión central: ¿qué edad y qué incertidumbre le corresponden a una provincia dada su área y su conteo?

📘 **Dónde se aprende** (2 clases): [B70-C04 · Vulcanismo marciano: provincias, edades y evolución](../programa/clases/B70/B70-C04-vulcanismo-marciano-provincias-edades-y-evolucion/CLASE.md); [B104-C01 · Historia de vuelos tripulados](../programa/clases/B104/B104-C01-historia-de-vuelos-tripulados/CLASE.md).

### Cruce

- Un cruce es el punto donde dos pasadas se intersecan.
- El cruce es la potencia a partir de la cual otra fuente pesa menos.
- El cruce es la `c` donde ambas valen lo mismo.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C17](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md):**
- REG --> CRU["cruce: |Δt| ≤ ventana y separación ≤ radio"]
- *Descripción textual:* cada registro se serializa de forma canónica y se firma con SHA-256; el validador revisa esquema, rangos, formato de tiempo, versión y huella; el cruce busca pares de mensajeros distintos.
- 🎯 **Por qué importa:** Un catálogo sin identificadores estables, versiones ni huellas no se puede citar ni auditar. La decisión central: ¿cómo se guarda un evento para que se pueda verificar, actualizar y cruzar con otros?

📘 **Dónde se aprende** (6 clases): [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md); [B53-C07 · Topografía por altimetría](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md); [B86-C22 · Suministro de energía durante la noche lunar](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md); [B88-C32 · Redundancia fría y caliente: estrategias y conmutación](../programa/clases/B88/B88-C32-redundancia-fria-y-caliente-estrategias-y-conmutacion/CLASE.md); [B88-C33 · Votación y redundancia modular triple (TMR)](../programa/clases/B88/B88-C33-votacion-y-redundancia-modular-triple-tmr/CLASE.md); [B88-C44 · Mantenimiento predictivo y pronóstico de salud de sistemas](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md).

### Cruce de fase

- El cruce de ganancia `ω_gc` es donde `|L| = 1` (0 dB); el cruce de fase `ω_pc` es donde la fase es −180°.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- El cruce de fase ocurre en `ω_pc = √2 = 1,414 rad/s`, donde `|L| = K/(√2·√3·√6) = K/6`.
- Obtener las frecuencias de cruce y los márgenes de ganancia y de fase.
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.

📘 **Dónde se aprende** (1 clase): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).

### Cruce de ganancia

- El cruce de ganancia `ω_gc` es donde `|L| = 1` (0 dB); el cruce de fase `ω_pc` es donde la fase es −180°.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- Paso 1 · cruce de ganancia. Se resuelve `|L(jω)| = 1` con `K = 2`: `ω_gc = 0,749 rad/s`.
- Obtener las frecuencias de cruce y los márgenes de ganancia y de fase.
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.

📘 **Dónde se aprende** (1 clase): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).
