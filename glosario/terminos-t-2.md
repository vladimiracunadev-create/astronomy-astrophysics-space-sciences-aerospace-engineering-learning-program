# Términos · T (parte 2 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · **T** · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-t.md) · **2**

### Tiempo hasta el apoapsis

- El tiempo hasta el apoapsis es medio periodo.

💡 **Cómo se explica en la clase [B75-C22](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md):**
- *Descripción textual:* El impulso y su dirección dan el vector velocidad; de él salen la energía y el momento, los elementos y el apoapsis; el semieje da el tiempo hasta el apoapsis.
- Familia tangencial: dv, apoapsis y tiempo hasta el apoapsis
- 🎯 **Por qué importa:** Antes de optimizar toda la misión conviene entender el primer impulso. La decisión central: ¿qué módulo y qué dirección del primer impulso alcanzan un radio dado con el menor delta-v y en cuánto tiempo?
- 🔗 **Se estudia junto con:** primer impulso, dirección, familia tangencial, apoapsis alcanzado.

📘 **Dónde se aprende** (1 clase): [B75-C22 · Modelos de primer impulso](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md).

### Tiempo hasta el criterio

- El tiempo hasta el criterio es el tiempo en alcanzar un umbral.

💡 **Cómo se explica en la clase [B107-C10](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md):**
- Una cohorte inventada de 40 personas con tiempo hasta el criterio exponencial de media 30 d y seguimiento de 45 d: 30 alcanzan el criterio y 10 quedan censuradas.
- Estimar la curva de supervivencia (tiempo hasta el criterio) con Kaplan–Meier con datos censurados.
- 🎯 **Por qué importa:** Los fragmentos consultados describen el entrenamiento en la ISS (Loehr et al., 2015) y baterías funcionales con medidas fisiológicas (Mulavara et al., 2018), pero un seguimiento necesita indicadores bien definidos y bien calculados.
- 🔗 **Se estudia junto con:** % de recuperación, censura, Kaplan–Meier, CUSUM.

📘 **Dónde se aprende** (1 clase): [B107-C10 · Indicadores de rehabilitación y seguimiento](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md).

### Tiempo hasta lo crítico

- Emergencia: situación que exige acción inmediata. Tiempo hasta lo crítico: `ΔE/(P_carga − P_gen)`.

💡 **Cómo se explica en la clase [B96-C15](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md):**
- S["SOC 80 %, limite 20 %"] --> T["Tiempo hasta lo critico"]
- *Descripción textual:* el tiempo hasta lo crítico se calcula con la energía disponible y la descarga neta; se compara con el tiempo de respuesta; el margen indica si hay tiempo y la generación mínima indica cuánto falta.
- 🎯 **Por qué importa:** Cuando falta el contacto, esperar tiene un costo medible. La decisión central: ¿alcanza el tiempo de respuesta antes del límite crítico y qué se puede hacer para ganar margen?
- 🔗 **Se estudia junto con:** Emergencia, Tiempo de respuesta, Margen, Descarga neta.

📘 **Dónde se aprende** (1 clase): [B96-C15 · Operaciones de emergencia](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md).

### Tiempo hasta resolver

- Prioridad no expropiativa: no interrumpe al que se atiende. Tiempo hasta resolver: espera más servicio.

💡 **Cómo se explica en la clase [B96-C26](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md):**
- Tiempo medio hasta resolver: 102,4 min (alta) y 165,9 min (baja).
- El tiempo medio hasta resolver es 102,4 min (alta) y 165,9 min (baja).
- 🎯 **Por qué importa:** Sin un procedimiento de priorización, un incidente leve puede retrasar a uno grave. La decisión central: ¿cuánto esperan los incidentes de alta y de baja prioridad y cuánto mejora la priorización al grave sin colapsar al leve?
- 🔗 **Se estudia junto con:** Incidente, M/M/1, Utilización, Espera Wq.

📘 **Dónde se aprende** (1 clase): [B96-C26 · Gestión de incidentes en la operación de estaciones](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md).

### Tiempo integral

- El tiempo integral es `Ti = Kp/Ki` (s) y el derivativo `Td = Kd/Kp` (s).

💡 **Contexto en la clase [B16-C11](../programa/clases/B16/B16-C11-control-proporcional-integral-derivativo/CLASE.md):**
- **Idea central (modelo mental):** La acción proporcional mira el presente (cuánto error hay). La integral mira el pasado (cuánto error se acumuló). La derivada mira el futuro (hacia dónde va el error).
- 🎯 **Por qué importa:** En el espacio actúan pares pequeños pero persistentes: presión de radiación solar, gradiente de gravedad, fugas de un propulsor. Un lazo PD termina con un error constante `d/Kp` (C04).
- 🔗 **Se estudia junto con:** PID, derivada sobre la medida, tipo, derivativo.

📘 **Dónde se aprende** (1 clase): [B16-C11 · Control proporcional integral derivativo](../programa/clases/B16/B16-C11-control-proporcional-integral-derivativo/CLASE.md).

### Tiempo límite

- El tiempo límite evita esperas infinitas.
- Ejecutor: programa que corre una secuencia. Tiempo límite: plazo de un paso.

💡 **Cómo se explica en la clase [B88-C24](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md):**
- Límite: un enchufe no evita que la central falle; por eso el tiempo límite.
- Tratar un dispositivo colgado con tiempo límite.
- ⚠️ **Error frecuente:** Esperar sin límite. Define un tiempo límite (8.4)
- 🎯 **Por qué importa:** Si la aplicación toca registros, no se puede probar sin el hardware y cada cambio de componente la rompe. La decisión central: ¿qué interfaz mínima expone el dispositivo para que la aplicación no dependa de él?
- 🔗 **Se estudia junto con:** HAL, controlador, mock, reintento.

📘 **Dónde se aprende** (2 clases): [B88-C24 · Capa de abstracción de hardware (HAL) y controladores](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md); [B96-C24 · Operación remota y automatizada de estaciones](../programa/clases/B96/B96-C24-operacion-remota-y-automatizada-de-estaciones/CLASE.md).

### Tiempo luz

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C22](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md):**
- Tiempo luz de 1 au: `499,00 s`; de 0,72 au: `359,28 s`.
- *Descripción textual:* la gravedad de dos cuerpos fija los puntos y las órbitas útiles, y el flujo y el tiempo luz fijan las condiciones de la nave.
- 🎯 **Por qué importa:** Cada órbita compra una ventaja y una dificultad. La decisión central: ¿qué punto o qué órbita da la vista del Sol que necesita el instrumento a un costo térmico y de enlace aceptable?
- 🔗 **Se estudia junto con:** punto de Lagrange L1, aproximación de Hill, órbita geosíncrona, perihelio.

📘 **Dónde se aprende** (1 clase): [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md).

### Tiempo medio

- El tiempo medio `T½` es el que tarda un compartimento en eliminar la mitad de su exceso.

💡 **Cómo se explica en la clase [B104-C11](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md):**
- Las razones críticas y los tiempos medios son inventados: no usar para ninguna decisión sobre descompresión ni respiración.
- Descripción larga: el tiempo crece con el tiempo medio y disminuye al aflojar la razón o la presión de cabina.
- 🎯 **Por qué importa:** Un traje presurizado a una fracción de la presión de la cabina deja al nitrógeno disuelto en sobresaturación si no se elimina antes. La decisión conceptual: ¿cómo depende el tiempo de eliminación del nitrógeno del compartimento, de la razón crítica y de la presión de la cabina?
- 🔗 **Se estudia junto con:** razón crítica, preoxigenación, compartimento.

📘 **Dónde se aprende** (1 clase): [B104-C11 · Trajes espaciales](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md).

### Tiempo mínimo

- El tiempo mínimo con cota `U` para recorrer `d` en reposo es `T_min = 2√(d/U)`.
- El tiempo mínimo `T_min(M)` es el mínimo de esa curva, en `x = x_min`.

💡 **Cómo se explica en la clase [B81-C12](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md):**
- Hallar la cota mínima factible con el tiempo mínimo bang-bang.
- Tiempo minimo T_min = 2 sqrt(d/U): U = 4 -> 1.0000 ;
- 🎯 **Por qué importa:** Ignorar una cota produce un control irrealizable; imponerla mal produce un problema sin solución. La decisión central: ¿cuánto cuesta una cota de control y cuál es el mínimo valor para el que el problema aún tiene solución?
- 🔗 **Se estudia junto con:** cota, conjunto activo.

📘 **Dónde se aprende** (2 clases): [B81-C12 · Restricciones dinámicas en optimización](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md); [B82-C04 · Lambert multirrevolución](../programa/clases/B82/B82-C04-lambert-multirrevolucion/CLASE.md).

### Tiempo mínimo de retorno

- El tiempo mínimo de retorno `t_min` es el del residuo más ligado.

💡 **Cómo se explica en la clase [B27-C16](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md):**
- Calcular la dispersión de energía y el tiempo mínimo de retorno.
- 🎯 **Por qué importa:** Estos eventos iluminan agujeros negros inactivos y permiten estimar su masa. Gezari revisa 56 de ellos (S3, resumen).
- 🔗 **Se estudia junto con:** radio de marea, masa de Hills, dispersión de energía, tasa de retorno.

📘 **Dónde se aprende** (1 clase): [B27-C16 · Eventos de disrupción por marea](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md).

### Tiempo muerto

- El tiempo muerto es el intervalo tras un evento durante el cual el detector no registra otro.
- El tiempo muerto es el que no se expone.
- El tiempo muerto `τ` es el intervalo ciego tras un conteo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C10](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md):**
- Ejercicio 9 · transferencia. Si el detector tiene un tiempo muerto de 1 ms, ¿qué fracción de los intervalos entre fotones (con `λ = 100 s⁻¹`, sintética) son más cortos que 1 ms?
- Límites: llegadas independientes; sin tiempo muerto ni ruido; datos simulados; no es análisis de un detector real.
- 🎯 **Por qué importa:** Un detector cuenta fotones que llegan al azar. Cuánto hay que esperar, en promedio, entre uno y el siguiente, y cuánto varía esa espera, decide el tiempo de exposición, el tiempo muerto aceptable y el ruido.
- 🔗 **Se estudia junto con:** integración por partes, tasa de conteo, tiempo de espera, media.

📘 **Dónde se aprende** (4 clases): [B09-C10 · Integración por partes](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md); [B44-C18 · Control electrónico de cámaras](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md); [B86-C09 · Electrónica de potencia](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md); [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Tiempo muerto no paralizable

- El tiempo muerto no paralizable `m = n/(1 + nτ)` se corrige con `n = m/(1 − mτ)`.

💡 **Cómo se explica en la clase [B85-C23](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md):**
- Límites: respuesta de potencia, sin dependencia de tasa de dosis ni temperatura, tiempo muerto no paralizable.
- 🎯 **Por qué importa:** Un monitor mal calibrado no distingue una dosis real del ruido. La decisión central: ¿cuál es la relación señal–dosis, desde qué dosis es fiable y hasta qué tasa de cuentas se puede corregir el tiempo muerto?
- 🔗 **Se estudia junto con:** calibración, ajuste log-log, ajuste directo, límite de detección.

📘 **Dónde se aprende** (1 clase): [B85-C23 · Dosímetros y monitores de radiación a bordo](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md).

### Tiempo nuclear

- El tiempo nuclear es lo que dura el combustible a la luminosidad actual.
- El tiempo nuclear `t_MS = f X M ε c²/L` es la vida en la secuencia principal, con `f` la fracción de masa que llega a quemarse y `X` la fracción de hidrógeno.

💡 **Cómo se explica en la clase [B24-C06](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md):**
- El tiempo nuclear es `t = f X M ε c² / L`: `7,4 Gyr` con `X = 0,7` y `10,5 Gyr` con `X = 1`.
- Estimar el tiempo nuclear de una estrella.
- 🎯 **Por qué importa:** Una estrella como el Sol brilla desde hace miles de millones de años; ninguna fuente química ni gravitatoria alcanza (C02). La fusión nuclear sí.
- 🔗 **Se estudia junto con:** fusión nuclear, defecto de masa, protón, partícula alfa.

📘 **Dónde se aprende** (2 clases): [B24-C06 · Fusión de hidrógeno](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md); [B24-C15 · Estrellas de baja masa](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md).

### Tiempo parabólico

- El tiempo parabólico `t_p = (√2/3)(s^(3/2) − (s−c)^(3/2))` separa elipses de hipérbolas para `θ < 180°`.
- El tiempo parabólico (`x = 1`) se calcula aparte: `T(1) = (2/3)(1 − λ³)`.

💡 **Cómo se explica en la clase [B82-C01](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md):**
- Con `μ = 1` y la unidad de tiempo `TU = 58,13244 d`, el tiempo de mínima energía vale `212,709 d` y el parabólico `88,000 d`.
- Calcular el tiempo de mínima energía y el tiempo parabólico (Euler) de una transferencia.
- 🎯 **Por qué importa:** Un diseñador de trayectorias conoce dónde está la nave y dónde debe estar, y cuánto tiempo tiene; no conoce la velocidad con que debe salir. La decisión central: ¿qué semieje y qué velocidad inicial hacen que la nave pase por `r2` exactamente a los `t` días?
- 🔗 **Se estudia junto con:** cuerda, semiperímetro, teorema de Lambert, tiempo de mínima energía.

📘 **Dónde se aprende** (2 clases): [B82-C01 · Lambert de arco corto](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md); [B82-C05 · Singularidades del problema de Lambert](../programa/clases/B82/B82-C05-singularidades-del-problema-de-lambert/CLASE.md).

### Tiempo por llamada

- El tiempo por llamada se mide con `perf_counter` y depende del equipo.

💡 **Cómo se explica en la clase [B82-C07](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md):**
- Los tiempos por llamada fueron de 3378, 2833, 2458, 1964 y 2082 µs en este equipo, con otros procesos en ejecución: varían entre ejecuciones y no son una medida absoluta.
- Paso 4. El tiempo por llamada (1964 µs) se anota como dependiente del equipo.
- 🎯 **Por qué importa:** Elegir un solucionador sin medirlo es adivinar. La decisión central: ¿qué solucionador conviene para un banco de transferencias, y qué cifras sustentan esa elección?
- 🔗 **Se estudia junto con:** banco de casos, éxito, fallo, iteraciones.

📘 **Dónde se aprende** (1 clase): [B82-C07 · Benchmark entre solucionadores de Lambert](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md).

### Tiempo propio

- El tiempo propio `τ` es el medido por un reloj que viaja con el objeto.
- El tiempo propio a lo largo de una línea de universo es `τ = ∫ √(1 − v²/c²) dt`.
- El tiempo propio `τ` lo mide el reloj del cuerpo que cae.

💡 **Cómo se explica en la clase [B26-C03](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md):**
- En el marco del muón: tiempo propio `2116/(0,99c) = 7,13 μs`; en unidades de `τ`: `3,245`; el mismo `S`.
- *Descripción textual:* en ambos marcos el tiempo propio del recorrido es `d/(γβc)`, y la supervivencia es la exponencial de ese tiempo entre la vida media.
- 🎯 **Por qué importa:** Los muones se producen en la alta atmósfera por rayos cósmicos, viven microsegundos y, sin embargo, llegan al suelo en cantidad. Los relojes de satélites de navegación se ajustan por el mismo efecto.
- 🔗 **Se estudia junto con:** tiempo coordenado, dilatación temporal, longitud propia, contracción de longitudes.

📘 **Dónde se aprende** (3 clases): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md); [B26-C04 · Espacio-tiempo de Minkowski](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md); [B27-C08 · Horizonte de sucesos](../programa/clases/B27/B27-C08-horizonte-de-sucesos/CLASE.md).

### Tiempo real

- El tiempo real (RTT menor que 1 s, umbral ilustrativo) permite conversación.

💡 **Contexto en la clase [B105-C15](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md):**
- 🎯 **Por qué importa:** Una conversación en tiempo real es posible a la Luna (2,6 s de ida y vuelta) y deja de serlo a Marte (hasta 42 min). La decisión central: ¿cuánto dura una consulta según el destino y el diseño del intercambio (varios turnos o un paquete completo)?
- 🔗 **Se estudia junto con:** retardo de ida, ida y vuelta, tiempo de transferencia, modelo circular.

📘 **Dónde se aprende** (1 clase): [B105-C15 · Telemedicina espacial](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md).

### Tiempo sideral local

- El tiempo sideral local `θ` es el ángulo entre el equinoccio y el meridiano del sitio.

💡 **Cómo se explica en la clase [B77-C11](../programa/clases/B77/B77-C11-ventanas-de-lanzamiento-dinamica-de-lanzamiento-y-reentrada/CLASE.md):**
- Para un sitio sintético a `28,5°` de latitud y un plano de `i = 51,6°` y `RAAN = 120°`, la ventana ascendente se abre cuando el tiempo sideral local es `145,489°` con acimut `44,975°`; la descendente a `274,511°` con acimut `135,025°`.
- Hallar el tiempo sideral local de las dos ventanas diarias.
- 🎯 **Por qué importa:** Si el vehículo despega fuera de la ventana, el plano que alcanza no es el deseado y corregirlo cuesta `Δv`. La decisión central: ¿a qué hora sideral y con qué acimut se lanza para entrar en un plano dado, y cuánto error produce un retraso?
- 🔗 **Se estudia junto con:** ventana de lanzamiento, acimut de lanzamiento, vector normal, lanzamiento ascendente.

📘 **Dónde se aprende** (1 clase): [B77-C11 · Ventanas de lanzamiento — Dinámica de lanzamiento y reentrada](../programa/clases/B77/B77-C11-ventanas-de-lanzamiento-dinamica-de-lanzamiento-y-reentrada/CLASE.md).

### Tiempo sidéreo de Greenwich (GMST)

- El tiempo sidéreo de Greenwich (GMST) es el TSL en longitud 0°;

💡 **Contexto en la clase [B08-C05](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md):**
- **Idea central (modelo mental):** La Tierra gira 360° respecto de las estrellas en un día sidéreo. Pero también avanza por su órbita, y para que el Sol vuelva al meridiano debe girar un poco más: casi 1° más. Ese 1° de giro extra toma unos 4 min.
- 🎯 **Por qué importa:** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.
- 🔗 **Se estudia junto con:** día solar, día solar medio, día sidéreo, tiempo sidéreo local (TSL).

📘 **Dónde se aprende** (1 clase): [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md).

### Tiempo sidéreo local

- El tiempo sidéreo local (TSL) es el ángulo horario del punto vernal en tu lugar; se verá en C05.

💡 **Cómo se explica en la clase [B08-C04](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md):**
- *Descripción textual:* se combinan la ascensión recta del astro con el tiempo sidéreo local para obtener el ángulo horario, y con él, la latitud y la declinación se calculan altura y acimut.
- 🎯 **Por qué importa:** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».
- 🔗 **Se estudia junto con:** altura, distancia cenital, acimut, ángulo horario.

📘 **Dónde se aprende** (1 clase): [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md).

### Tiempo sidéreo local (TSL)

- El tiempo sidéreo local (TSL) es el ángulo horario del punto vernal en tu lugar, expresado en horas; en el meridiano, el TSL es igual a la AR del astro que culmina.

💡 **Cómo se explica en la clase [B08-C05](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md):**
- A las 00:00 UT del 5 de noviembre, el tiempo sidéreo local fue `22,25 h` (laboratorio, simulado).
- Calcular el tiempo sidéreo local a una hora UT y usarlo para ubicar el tránsito de un objeto.
- 🎯 **Por qué importa:** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.
- 🔗 **Se estudia junto con:** día solar, día solar medio, día sidéreo, tiempo sidéreo de Greenwich (GMST).

📘 **Dónde se aprende** (1 clase): [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md).

### Tiempo Terrestre (TT)

- El Tiempo Terrestre (TT) avanza al mismo ritmo que TAI con un desfase fijo `TT = TAI + 32,184 s` (S2, S3).

💡 **Contexto en la clase [B13-C08](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md):**
- **Idea central (modelo mental):** TAI es el reloj continuo. UTC es TAI menos un entero de segundos (con saltos). TT es TAI más una constante.
- 🎯 **Por qué importa:** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.
- 🔗 **Se estudia junto con:** Tiempo Universal Coordinado (UTC), Tiempo Atómico Internacional (TAI), Tiempo Dinámico Baricéntrico (TDB), segundo intercalar.

📘 **Dónde se aprende** (1 clase): [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### Tiempo total

- El tiempo total es la suma de etapas secuenciales.

💡 **Cómo se explica en la clase [B119-C20](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md):**
- Descripción larga: paralelizar una etapa independiente reduce la media y la cola del tiempo total.
- 🎯 **Por qué importa:** Las clases anteriores estudian reglas; esta pone a prueba si una cadena de respuesta es suficientemente rápida. Es la clase integradora del bloque junto con la matriz de obligaciones (C33).
- 🔗 **Se estudia junto con:** etapa, Paralelizar, percentil 95, cuello de botella.

📘 **Dónde se aprende** (1 clase): [B119-C20 · Simulación de respuesta institucional a incidentes](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md).

### Tiempo Universal Coordinado (UTC)

- El Tiempo Universal Coordinado (UTC) es una forma de nombrar instantes con fecha y hora civil que sigue a TAI con saltos de un segundo para mantenerse a menos de `0,9 s` de UT1 (S3); no es una escala continua.

💡 **Contexto en la clase [B13-C08](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md):**
- **Idea central (modelo mental):** TAI es el reloj continuo. UTC es TAI menos un entero de segundos (con saltos). TT es TAI más una constante.
- 🎯 **Por qué importa:** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.
- 🔗 **Se estudia junto con:** Tiempo Atómico Internacional (TAI), Tiempo Terrestre (TT), Tiempo Dinámico Baricéntrico (TDB), segundo intercalar.

📘 **Dónde se aprende** (1 clase): [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### Tiempo visible

- El tiempo visible `T_vis` es el que pasa sobre el límite.

💡 **Cómo se explica en la clase [B28-C08](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md):**
- Cada magnitud más profunda alarga el tiempo visible en un factor `10^{0,4/α} = 2,03`.
- La cadencia debe ser menor que el tiempo visible para garantizar la detección: `17 d` o menos en este ejemplo.
- 🎯 **Por qué importa:** Un transitorio que dura menos que el intervalo entre visitas se pierde. El índice de caída decide cuánto dura un evento sobre el límite de detección.
- 🔗 **Se estudia junto con:** transitorio, curva de luz, índice de caída, límite de detección.

📘 **Dónde se aprende** (1 clase): [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md).

### Tierra esférica

- La Tierra esférica es un modelo sin achatamiento ni atmósfera.

💡 **Cómo se explica en la clase [B87-C04](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md):**
- B87-C04 sensor de horizonte | Tierra esferica; limbo medido con sigma = 0.05 deg por eje (SINTETICO, semilla 20260514)
- Límites: Tierra esférica, limbo puntual, sin atmósfera, achatamiento ni ruido de escala; el eje de giro alrededor del nadir no se observa.
- 🎯 **Por qué importa:** Para apuntar una antena o una cámara hacia la Tierra hace falta el nadir. La decisión central: ¿cuántos puntos del limbo y qué precisión se necesitan, y cuánto cambia el resultado con la altitud y con un error en el radio angular supuesto?
- 🔗 **Se estudia junto con:** radio angular, punto del limbo, nadir, ajuste.

📘 **Dónde se aprende** (1 clase): [B87-C04 · Sensores terrestres](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md).

### Tierra plana

- La Tierra plana supone `g` constante y horizonte fijo.

💡 **Cómo se explica en la clase [B77-C08](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md):**
- Límites: Tierra plana, `g` constante, sin aire; el cabeceo y la aceleración a lo largo de la velocidad son simplificaciones.
- 🎯 **Por qué importa:** Un `Δv` ideal alto no garantiza velocidad alta al final. La decisión central: ¿cuánto del `Δv` se pierde por gravedad y cómo se reduce con más empuje o con una trayectoria más inclinada?
- 🔗 **Se estudia junto con:** pérdida gravitacional, programa de cabeceo, tiempo de combustión, Δv neto.

📘 **Dónde se aprende** (1 clase): [B77-C08 · Pérdidas gravitacionales](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md).

### Timoshenko

- La de Timoshenko añade el giro de la sección independiente, con cortante `κ G A`.

💡 **Cómo se explica en la clase [B84-C27](../programa/clases/B84/B84-C27-tipos-de-elementos-finitos-viga-placa-y-solido/CLASE.md):**
- El Timoshenko FE (8 elementos, error < 2 % en todos los casos) sigue a Timoshenko.
- Un voladizo de `0,50 m` con `b = 20 mm` y `P = 100 N` con `L/h = 5` tiene flecha de Euler `0,0362 mm` y de Timoshenko `0,0374 mm`: el cortante aporta `3,19 %`; con `L/h = 2` la flecha de Euler `0,0023 mm` queda `16,6 %` por debajo de la de Timoshenko `0,0028`.
- 🎯 **Por qué importa:** Una viga corta modelada con Euler subestima la flecha en 17 %; no es un error de malla sino de hipótesis. La decisión central: ¿para qué esbeltez es válido el elemento de Euler y cuándo hace falta cortante?
- 🔗 **Se estudia junto con:** viga de Euler–Bernoulli, integración reducida, aporte del cortante.

📘 **Dónde se aprende** (1 clase): [B84-C27 · Tipos de elementos finitos: viga, placa y sólido](../programa/clases/B84/B84-C27-tipos-de-elementos-finitos-viga-placa-y-solido/CLASE.md).

### Tipo

- Un tipo es la clase de valor, que fija qué operaciones valen.
- El tipo de un lazo es el número de integradores en `L`; el tipo determina el error ante escalón y rampa.
- Su tipo (`dtype`) fija cómo se guarda cada valor (`float64`, `float32`, `int64`).

💡 **Cómo se explica en la clase [B07-C02](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md):**
- Cinco tipos distintos en una sola ficha, más la ausencia de un dato.
- La forma accesible es la tabla de la sección 9 y la salida impresa del laboratorio, que lista cada variable con su valor y su tipo.
- 🎯 **Por qué importa:** Un dato sin tipo es ambiguo: «12756» puede ser un número con el que calculas o un texto que lees de un archivo. Si el programa los confunde, falla o, peor, da un resultado plausible pero erróneo.
- 🔗 **Se estudia junto con:** variable, conversión, notación científica, palabra reservada.

📘 **Dónde se aprende** (3 clases): [B07-C02 · Tipos de datos y variables](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md); [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md); [B16-C11 · Control proporcional integral derivativo](../programa/clases/B16/B16-C11-control-proporcional-integral-derivativo/CLASE.md).

### Tipo A

- La evaluación de tipo A de una incertidumbre típica se obtiene del análisis estadístico de observaciones repetidas; la de tipo B, por otros medios: datos previos, especificaciones, certificados, juicio científico (S1, 4.2–4.3).

💡 **Cómo se explica en la clase [B12-C20](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md):**
- Componentes: altitud (tipo A, 9 lecturas, `s = 300 m`), radio de referencia (tipo B, rectangular ±500 m), `GM` (tipo B, `10⁻⁹` relativa, hipotético).
- Clasificar componentes en tipo A (estadísticos) y tipo B (otros) y evaluar cada uno.
- 🎯 **Por qué importa:** Una cifra sin incertidumbre es una opinión; una incertidumbre sin presupuesto es una cifra sin respaldo. Quien revise la misión —otro ingeniero, un cliente o uno mismo dentro de un año— debe poder ver qué componentes se consideraron, cómo se evaluó cada uno, cuál domina y si el requisito se cumple.
- 🔗 **Se estudia junto con:** mensurando, modelo de medida, tipo B, incertidumbre típica combinada.

📘 **Dónde se aprende** (1 clase): [B12-C20 · Informe de incertidumbre de una misión](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md).

### Tipo B

- La evaluación tipo A estima `u` de una serie de lecturas (S1, 2.3.2); la tipo B, de información como certificados, hojas técnicas o juicio (S1, 2.3.3).
- La evaluación de tipo A de una incertidumbre típica se obtiene del análisis estadístico de observaciones repetidas; la de tipo B, por otros medios: datos previos, especificaciones, certificados, juicio científico (S1, 4.2–4.3).
- La incertidumbre tipo A viene del ruido y del ajuste; la tipo B de la fuerza de referencia (masas y gravedad local).

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- Si el espectrógrafo tiene una calibración que desplaza todas las longitudes 0,05 nm, la media no lo detecta: hay que tener información externa (la incertidumbre de calibración, de tipo B).
- Por eso un reporte serio declara ambos: la repetibilidad (tipo A) y la calibración (tipo B).
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.
- 🔗 **Se estudia junto con:** error, incertidumbre, incertidumbre estándar, evaluación tipo A.

📘 **Dónde se aprende** (3 clases): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B12-C20 · Informe de incertidumbre de una misión](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md); [B102-C06 · Dinamometría y medición de fuerzas de tracción](../programa/clases/B102/B102-C06-dinamometria-y-medicion-de-fuerzas-de-traccion/CLASE.md).

### Tipo con unidad

- Interfaz: frontera entre dos sistemas que intercambian datos. Tipo con unidad: valor que lleva su unidad.

💡 **Cómo se explica en la clase [B96-C19](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md):**
- Ejercicio 8 · autónomo. ¿Qué rechaza el tipo con unidad?
- Límites: deriva lineal, sin geometría de trayectoria; un solo tipo de unidad de impulso.
- 🎯 **Por qué importa:** Un número sin unidad es una trampa: el programa corre, el valor parece razonable y la nave se pierde. La decisión central: ¿cómo se evita que una conversión de unidades pase inadvertida entre el software de tierra y el de vuelo?
- 🔗 **Se estudia junto con:** Lección aprendida, lbf·s, N·s, Interfaz.

📘 **Dónde se aprende** (1 clase): [B96-C19 · Lecciones aprendidas operativas](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md).

### Tipo espectral

- El tipo espectral (O, B, A, F, G, K, M, de caliente a frío) es una clasificación por las líneas.

💡 **Cómo se explica en la clase [B24-C10](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md):**
- Por las líneas (tipo espectral): casi independiente del enrojecimiento.
- 🎯 **Por qué importa:** La intensidad de una línea espectral no crece simplemente con la temperatura: depende de cuántos átomos están en el nivel adecuado y de cuántos están ionizados. Por eso un mismo elemento domina en estrellas de temperaturas muy distintas.
- 🔗 **Se estudia junto con:** ley de Wien, ecuación de Boltzmann, ecuación de Saha, serie de Balmer.

📘 **Dónde se aprende** (1 clase): [B24-C10 · Espectros y clasificación estelar](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md).

### Tipo I

- El nivel de significación `α` es la tasa de falsos rechazos que se acepta (error tipo I); el error tipo II (probabilidad `β`) es no rechazar una `H₀` falsa; la potencia `1 − β` es la probabilidad de detectar un efecto real de un tamaño dado.

💡 **Cómo se explica en la clase [B12-C09](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md):**
- Distinguir error tipo I, error tipo II y potencia, y calcular la potencia en un caso.
- Debe incluir: hipótesis y supuestos; estadístico y `p` comprobado por dos caminos; simulación del error tipo I; potencia y `n` necesario; sensibilidad (correlación, colas); conclusión acotada; datos rotulados como observados/estimados/sintéticos y fuentes con fecha.
- 🎯 **Por qué importa:** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.
- 🔗 **Se estudia junto con:** hipótesis nula, alternativa, estadístico de prueba, valor p.

📘 **Dónde se aprende** (1 clase): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md).

### Tipo Tait–Bryan

- Una secuencia de tipo Tait–Bryan usa tres ejes distintos (3‑2‑1: `z`, `y`, `x`); una de Euler propio repite el primero y el tercero (3‑1‑3: `z`, `x`, `z`).

💡 **Contexto en la clase [B10-C14](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md):**
- **Idea central (modelo mental):** En un giroscopio de tres anillos, cuando el anillo intermedio gira `90°` los anillos exterior e interior quedan alineados: dos movimientos distintos producen el mismo efecto y se pierde un grado de libertad.
- 🎯 **Por qué importa:** Un satélite que apunta una antena al cenit tiene el cabeceo cerca de `90°`; si la actitud se guarda con ángulos de Euler, justo ahí el cálculo se vuelve inestable: ángulos que cambian muy rápido para movimientos pequeños, o dos conjuntos de ángulos distintos para la misma orientación.
- 🔗 **Se estudia junto con:** ángulos de Euler, Euler propio, guiñada, cabeceo.

📘 **Dónde se aprende** (1 clase): [B10-C14 · Ángulos de Euler y singularidades](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md).

### TIR

- La TIR es la `r` con VAN igual a cero.
- La TIR es la tasa que hace el VPN igual a cero.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- La TIR por bisección es `23,8799` %; por Newton, `23,8799` %; el error de `VAN(TIR)` es `8,2e-14`.
- Este flujo cambia de signo una sola vez, así que la TIR es única; con varios cambios de signo puede haber varias.
- ⚠️ **Error frecuente:** Reportar la TIR sin el flujo. Se corrige con 8.1.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?
- 🔗 **Se estudia junto con:** VAN, MOIC, pre-money, post-money.

📘 **Dónde se aprende** (2 clases): [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md); [B126-C05 · Evaluación de viabilidad económica de un negocio espacial](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md).

### Tirante

- El índice de panel es `E^(1/3)/ρ`; el de tirante, `σ_y/ρ`; el de columna, `E^(1/2)/ρ`.

💡 **Cómo se explica en la clase [B84-C05](../programa/clases/B84/B84-C05-seleccion-de-materiales/CLASE.md):**
- Derivar índices de mérito para panel, tirante y columna.
- 🎯 **Por qué importa:** Un ganador que cambia con pequeñas variaciones de pesos no es una decisión: es una opinión. La sensibilidad dice si la elección es robusta.
- 🔗 **Se estudia junto con:** índice de panel, columna, matriz de decisión, pesos.

📘 **Dónde se aprende** (1 clase): [B84-C05 · Selección de materiales](../programa/clases/B84/B84-C05-seleccion-de-materiales/CLASE.md).

### Tiro

- El tiro (*shooting*) convierte el BVP en un IVP: se adivina la condición inicial que falta, se integra y se corrige hasta cumplir la condición del otro extremo.

💡 **Cómo se explica en la clase [B11-C12](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md):**
- Tiro: simple de programar sobre un integrador ya validado; puede ser muy sensible si el problema es inestable (pequeños cambios en `v₀` producen grandes cambios en el extremo).
- B -->|"Tiro"| E["Adivinar la condición<br/>inicial que falta"]
- ⚠️ **Error frecuente:** Aceptar el tiro sin verificar con otro paso. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.
- 🔗 **Se estudia junto con:** problema de frontera, Dirichlet, Neumann, mixtas.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Tiro de barra

- El empuje `H` es la integral de `τ` en el arco; la resistencia por compactación `Rc = b k z₀^(n+1)/(n+1)` es el trabajo de hundir la rueda; el tiro de barra es `DP = H − Rc`.

💡 **Cómo se explica en la clase [B102-C02](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md):**
- *Descripción textual:* la carga fija el hundimiento y este el arco de contacto; con el patinaje se obtiene el empuje; restando la resistencia por compactación queda el tiro de barra.
- Paso 4 · Tiro de barra. `DP = 223,958 − 108,961 = 114,997 N`, `DP/W = 0,185`.
- 🎯 **Por qué importa:** La tracción de un rover en regolito no sale de un coeficiente de rozamiento único. La decisión central: ¿cuánta fuerza neta de empuje queda para tirar del vehículo, una vez descontada la resistencia que crea el propio hundimiento, y cómo depende del patinaje y de la gravedad?
- 🔗 **Se estudia junto con:** ley de presión-hundimiento, ángulo de contacto, resistencia de cizalla, empuje.

📘 **Dónde se aprende** (1 clase): [B102-C02 · Terramecánica: tracción y hundimiento en suelos sueltos](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md).

### TIS

- La TIS `(4πσ cos θ/λ)²`.

💡 **Cómo se explica en la clase [B43-C23](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md):**
- A igual `σ`, la TIS cambia por `(λ₂/λ₁)² = 4,0` entre 400 y 800 nm.
- *Descripción textual:* una PSD fija la rugosidad en una banda; la TIS la convierte en luz dispersa por la fórmula escalar.
- 🎯 **Por qué importa:** La luz dispersa reduce el contraste y la reflectancia especular. La decisión central: ¿qué rugosidad RMS, en qué banda de frecuencias espaciales, deja la luz dispersa por debajo del presupuesto?
- 🔗 **Se estudia junto con:** rugosidad RMS, PSD, banda, reflectancia especular.

📘 **Dónde se aprende** (1 clase): [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md).

### Tisserand

- El Tisserand respecto a una luna se conserva en cada sobrevuelo de esa luna.

💡 **Cómo se explica en la clase [B75-C26](../programa/clases/B75/B75-C26-sobrevuelos-de-lunas-y-tours-de-sistemas-planetarios/CLASE.md):**
- (3) El `v∞` calculado en el cruce con Ganimedes para la familia de Tisserand coincide con el pedido con error menor que `10⁻⁶ km/s`.
- La evidencia es tu esbozo de tour por Tisserand del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Cada luna es un peldaño de energía en torno a Júpiter. La decisión central: ¿qué órbitas jovianas puede alcanzar una nave con un sobrevuelo de Ganimedes de `v∞` dado y cuánto cambia la energía en un solo paso?
- 🔗 **Se estudia junto con:** tour, identidad de la energía, giro máximo, delta-v apalancado.

📘 **Dónde se aprende** (1 clase): [B75-C26 · Sobrevuelos de lunas y tours de sistemas planetarios](../programa/clases/B75/B75-C26-sobrevuelos-de-lunas-y-tours-de-sistemas-planetarios/CLASE.md).

### TLE

- El TLE son dos líneas de 69 columnas con elementos medios para el modelo SGP4.
- Una TLE (*two-line element set*) es un formato de dos líneas con elementos medios.

💡 **Cómo se explica en la clase [B74-C29](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md):**
- El TLE sintético da `5` (línea 1) y `1` (línea 2).
- EL["elementos"] --> TLE["TLE: 2 lineas de 69 columnas"]
- ⚠️ **Error frecuente:** Leer un TLE como elementos osculadores. Son medios para SGP4; ver 8.4.
- 🎯 **Por qué importa:** Un TLE mal copiado o mal leído da una órbita equivocada sin avisar. La decisión central: ¿qué errores detecta la suma de verificación, qué resolución tiene cada campo y qué significan realmente esos «elementos medios»?
- 🔗 **Se estudia junto con:** checksum, movimiento medio, OMM, teoría de elementos medios.

📘 **Dónde se aprende** (2 clases): [B74-C29 · Formatos TLE y OMM de elementos orbitales](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md); [B118-C02 · Catálogos de objetos espaciales](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md).

### TML

- TML (*total mass loss*) es la pérdida total de masa;
- Desgasificación: liberación de gases de un material en vacío. TML: pérdida total de masa, `100 (mᵢ − m_f)/mᵢ`.

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- La silicona B pasa en `TML` y falla en `CVCM`: por eso se exigen ambos criterios.
- ⚠️ **Error frecuente:** Usar solo TML. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?
- 🔗 **Se estudia junto con:** WVR, RML, CVCM, bakeout.

📘 **Dónde se aprende** (2 clases): [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md); [B90-C04 · Control de contaminación](../programa/clases/B90/B90-C04-control-de-contaminacion/CLASE.md).

### Tobera adaptada

- La tobera adaptada es la que expande hasta la presión ambiente.
- La tobera adaptada tiene `p_e = p_a`;

💡 **Cómo se explica en la clase [B78-C03](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md):**
- Ejercicio 10 · transferencia. ¿Por qué una tobera adaptada elimina el término de presión del empuje?
- Límites: gas ideal, `γ` y `M` constantes, sin disociación, sin pérdidas, tobera adaptada.
- 🎯 **Por qué importa:** El mismo calor produce chorros distintos según el gas. La decisión central: ¿qué parámetro de cámara gana más escape, subir la temperatura o bajar la masa molar, y hasta dónde se puede expandir el gas?
- 🔗 **Se estudia junto con:** temperatura de cámara, razón de presiones, masa molar, velocidad característica.

📘 **Dónde se aprende** (2 clases): [B78-C03 · Termodinámica de cámaras](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md); [B79-C08 · Flujo en toberas convergente-divergentes](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md).

### Tobera magnética

- La tobera magnética guía y expande el plasma con un campo divergente.

💡 **Cómo se explica en la clase [B78-C09](../programa/clases/B78/B78-C09-propulsion-por-plasma/CLASE.md):**
- CS --> TOB["tobera magnetica: v^2 = cs^2 (1 + 2 ln(n0/n))"]
- Calcular la velocidad de Bohm y la expansión isoterma en una tobera magnética.
- 🎯 **Por qué importa:** Un plasma solo es un plasma si es mucho mayor que su longitud de Debye. La decisión central: ¿cuándo un gas ionizado se comporta como plasma y cuánta velocidad de escape puede ganar al expandirse en una tobera magnética?
- 🔗 **Se estudia junto con:** longitud de Debye, frecuencia de plasma, velocidad de Bohm, isoterma.

📘 **Dónde se aprende** (1 clase): [B78-C09 · Propulsión por plasma](../programa/clases/B78/B78-C09-propulsion-por-plasma/CLASE.md).

### Tolerancia

- La tolerancia combina una parte relativa `rtol` y una absoluta `atol`: la escala de cada componente es `sc_i = atol + rtol |s_i|`.
- La tolerancia es la diferencia máxima que aceptas entre lo obtenido y lo esperado; se compone de una parte relativa `rtol` y una absoluta `atol`.
- La tolerancia `w` es el semiancho aceptado en frecuencia.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C08](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md):**
- La tolerancia controla el error local de cada paso.
- Para un error global dado hay que reducir la tolerancia y verificar con una referencia (C19).
- ⚠️ **Error frecuente:** Confundir tolerancia local con error global. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.
- 🔗 **Se estudia junto con:** error local estimado, duplicación de paso, error normalizado, acepta.

📘 **Dónde se aprende** (6 clases): [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md); [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md); [B55-C10 · Identificación de moléculas orgánicas](../programa/clases/B55/B55-C10-identificacion-de-moleculas-organicas/CLASE.md); [B62-C08 · Mezclas moleculares y confusión de líneas](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md); [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md); [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### Tolerancia relativa

- La tolerancia relativa `rtol` escala con el tamaño de la referencia; la absoluta `atol` es un piso fijo.
- La tolerancia relativa `rtol` y la absoluta `atol` fijan el error permitido por paso.

💡 **Cómo se explica en la clase [B14-C10](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md):**
- Cierre. Se compara con `atol = 10⁻³ m`; una tolerancia solo relativa sobre `10⁻⁵ m` sería injusta.
- S1 destaca además que la comparación es asimétrica: la tolerancia relativa se escala con `|desired|` (la referencia), no con `actual`, de modo que intercambiar los argumentos puede cambiar el resultado cerca del límite.
- 🎯 **Por qué importa:** Cambias una línea de un propagador orbital «solo para ordenarlo» y el período de una órbita pasa de 5553,624562 s a 5553,627342 s (situación ilustrativa con cifras de esta clase). ¿Es un error o ruido?
- 🔗 **Se estudia junto con:** prueba de regresión, valor de referencia, absoluta, falso positivo.

📘 **Dónde se aprende** (2 clases): [B14-C03 · Análisis numérico con SciPy](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md); [B14-C10 · Pruebas de regresión numérica](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md).

### Tolerancia uniforme

- Una tolerancia uniforme `±δ` tiene desviación `δ/√3`.

💡 **Cómo se explica en la clase [B50-C09](../programa/clases/B50/B50-C09-asignacion-y-balance-de-tolerancias-opticas/CLASE.md):**
- Ejercicio 1 · con los pasos indicados. RMS de una tolerancia uniforme de `±0,03`.
- 🎯 **Por qué importa:** Repartir la tolerancia por igual es simple pero caro: pide más precisión justo donde cuesta más. La decisión central: ¿cuánta tolerancia le toca a cada parámetro para el menor costo con el mismo desempeño?
- 🔗 **Se estudia junto con:** sensibilidad, suma cuadrática, multiplicador de Lagrange, óptimo.

📘 **Dónde se aprende** (1 clase): [B50-C09 · Asignación y balance de tolerancias ópticas](../programa/clases/B50/B50-C09-asignacion-y-balance-de-tolerancias-opticas/CLASE.md).

### Tomografía

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B34-C06](../programa/clases/B34/B34-C06-tomografia-coronal/CLASE.md):**
- La evidencia es la ficha de la tomografía coronal del ejercicio 12 (sección 20).
- Ejercicio 11 · transferencia. Transferencia. ¿Qué limita la tomografía solar?
- 🎯 **Por qué importa:** Más ángulos dan mejores imágenes, pero las vistas disponibles son pocas. La decisión central: ¿cuánto mejora la reconstrucción con más direcciones de vista?
- 🔗 **Se estudia junto con:** proyección, método ART/Kaczmarz, positividad, no unicidad.

📘 **Dónde se aprende** (2 clases): [B34-C06 · Tomografía coronal](../programa/clases/B34/B34-C06-tomografia-coronal/CLASE.md); [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### Tope

- El tope es el máximo de pasos permitido.
- El tope es el máximo que se puede gastar por año.
- El tope (*latch*) detiene el movimiento en `θ = π/2`.

💡 **Cómo se explica en la clase [B84-C13](../programa/clases/B84/B84-C13-mecanismos-desplegables/CLASE.md):**
- La energía cinética final es lo que absorbe el tope (impacto).
- El par que queda en el tope es `0,0858 N·m`, 4,3 veces la fricción: hay un pequeño par de retención.
- ⚠️ **Error frecuente:** Ignorar el impacto en el tope. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un mecanismo que se despliega bien en el banco puede quedarse trabado en órbita si la fricción sube o la precarga baja; el margen de par lo cuantifica. La decisión central: ¿qué razón de par tiene el despliegue y qué precarga hace falta para cumplir el requisito?
- 🔗 **Se estudia junto con:** razón de par, precarga, balance de energía.

📘 **Dónde se aprende** (3 clases): [B84-C13 · Mecanismos desplegables](../programa/clases/B84/B84-C13-mecanismos-desplegables/CLASE.md); [B97-C16 · Autonomía de exploración](../programa/clases/B97/B97-C16-autonomia-de-exploracion/CLASE.md); [B124-C06 · Financiamiento público](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md).

### Tope articular

- Espacio de trabajo: conjunto de posiciones que alcanza el extremo. Tope articular: límite de ángulo.

💡 **Contexto en la clase [B101-C04](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR Q["Configuracion q"] --> L{"Topes:<br/>|q_i| menor que limite?"} L -->|no| X["Rechazada"] L -->|si| C{"Holgura entre<br/>capsulas > 0?"} C -->|no| X C -->|si| A["Admisible"] ``` *Descripción textual:* una configuración se acepta solo si respeta los topes y deja holgura positiva entre los pares de eslabones no adyacentes.
- 🎯 **Por qué importa:** Una solución de cinemática inversa que exceda un tope o atraviese el propio brazo no sirve. La decisión central: ¿esta configuración es admisible: respeta los topes y deja holgura entre eslabones?
- 🔗 **Se estudia junto con:** Espacio de trabajo, Cápsula, Holgura, Autocolisión.

📘 **Dónde se aprende** (1 clase): [B101-C04 · Límites articulares, espacio de trabajo y evitación de colisiones](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md).

### Tope de la atmósfera

- El tope de la atmósfera (TOA) es el nivel de referencia donde el modelo evalúa la radiancia.

💡 **Contexto en la clase [B57-C01](../programa/clases/B57/B57-C01-fundamentos-de-teledeteccion/CLASE.md):**
- **Idea central (modelo mental):** El sensor recibe la suma de lo que el píxel refleja del Sol y de lo que emite por su calor. Según la longitud de onda manda una u otra.
- 🎯 **Por qué importa:** Casi todas las técnicas del bloque eligen una región del espectro: óptica y de infrarrojo cercano para reflectancia, infrarrojo térmico para temperatura, microondas para radar. Esa elección nace de una pregunta física: ¿en qué longitudes de onda domina la luz solar reflejada y en cuáles domina la emisión propia?
- 🔗 **Se estudia junto con:** radiancia, irradiancia, reflectancia, lambertiana.

📘 **Dónde se aprende** (1 clase): [B57-C01 · Fundamentos de teledetección](../programa/clases/B57/B57-C01-fundamentos-de-teledeteccion/CLASE.md).

### Tope de potencia

- El tope de potencia limita el empuje eléctrico.

💡 **Cómo se explica en la clase [B78-C20](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md):**
- P["potencia"] --> TOPE["F <= min(75 mN/kW x P, 2 eta P / Ve)"]
- Aplicar el tope de empuje por potencia a las opciones eléctricas.
- ⚠️ **Error frecuente:** Ignorar el tope de potencia. Se corrige con 8.3.
- 🎯 **Por qué importa:** Cada arquitectura gana en una dimensión y pierde en otra. La decisión central: ¿qué opciones no están dominadas por otra en propelente y en tiempo, y cómo cambia el resultado con la potencia disponible?
- 🔗 **Se estudia junto con:** comparación no operativa, valor representativo, dominancia, frente de Pareto.

📘 **Dónde se aprende** (1 clase): [B78-C20 · Comparación no operativa de arquitecturas de propulsión](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md).

### Tope de valoración

- El tope de valoración (`CAP`) fija el precio máximo de conversión.

💡 **Cómo se explica en la clase [B126-C01](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md):**
- Con valoraciones bajas gana el descuento; con altas, el tope.
- El ejemplo conductor es una empresa sintética de 9 000 000 acciones previas (8 000 000 de fundadores y 1 000 000 de fondo de opciones) que firma un SAFE de 500 000 USD con tope post-money de 5 000 000 USD y 20 % de descuento, y luego levanta 3 000 000 USD en una ronda a tres valoraciones posibles.
- 🎯 **Por qué importa:** El catálogo trata el financiamiento privado en general (B124-C07, «Financiamiento privado», en la [guía del bloque B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md)), no la mecánica de las etapas iniciales.
- 🔗 **Se estudia junto con:** SAFE, descuento, ronda con precio, tabla de capitalización.

📘 **Dónde se aprende** (1 clase): [B126-C01 · Capital semilla y financiamiento inicial](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md).

### Tope por potencia

- El tope por potencia es el empuje máximo por kilovatio.

💡 **Cómo se explica en la clase [B78-C11](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md):**
- Aplicar el tope de empuje por potencia de la NASA a un CubeSat.
- El script [cubesat.py](cubesat.py) calcula propelente, tiempo de empuje y cumplimiento del tope de potencia para cinco tecnologías, el Δv de los impulsos totales consultados y el tiempo con potencia limitada (comprueba la aproximación lineal contra Tsiolkovsky y que los eléctricos no superan el tope).
- 🎯 **Por qué importa:** Un propulsor de alto `Isp` ahorra propelente pero empuja poco y tarda semanas; uno de empuje alto gasta más volumen de propelente. La decisión central: ¿qué tecnología cumple un Δv dado con una masa, un volumen y una potencia que un CubeSat sí puede dar?
- 🔗 **Se estudia junto con:** micropropulsión, impulso total, aproximación lineal, tiempo de empuje.

📘 **Dónde se aprende** (1 clase): [B78-C11 · Micropropulsión para CubeSat](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md).

### Tope que fija el panel desplegado

- Traba (*latch*): tope que fija el panel desplegado. Inhibidor independiente: dispositivo físico entre una fuente de energía y un peligro.

💡 **Contexto en la clase [B90-C15](../programa/clases/B90/B90-C15-pruebas-de-despliegue/CLASE.md):**
- 🎯 **Por qué importa:** Un mecanismo que despliega en el laboratorio con un margen justo puede quedarse a medio camino con lubricación degradada o arrastre de un arnés. La decisión central: ¿cuánto par sobra frente al arrastre y con qué velocidad llega a la traba?
- 🔗 **Se estudia junto con:** Despliegue, Par de resorte, Arrastre, Margen de par.

📘 **Dónde se aprende** (1 clase): [B90-C15 · Pruebas de despliegue](../programa/clases/B90/B90-C15-pruebas-de-despliegue/CLASE.md).

### Topología

- La topología es el patrón de conexiones.
- La topología exige sin huecos ni solapes entre unidades.

💡 **Cómo se explica en la clase [B53-C18](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *ficha del mapa geológico digital*: proyección, áreas, errores y topología.
- topologia: contiguas -> huecos 0, solapes 0 ; con hueco -> huecos 100, solapes 0 ; con solape -> huecos 0, solapes 100
- ⚠️ **Error frecuente:** Ignorar la topología. se corrige con 8,2
- 🎯 **Por qué importa:** Un área medida en una proyección inadecuada es un área falsa. La decisión central: ¿qué proyección conserva las áreas y qué errores topológicos tiene el mapa?
- 🔗 **Se estudia junto con:** equivalente, sinusoidal, azimutal equivalente de Lambert.

📘 **Dónde se aprende** (2 clases): [B53-C18 · Cartografía geológica digital](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md); [B88-C31 · Topologías de red de datos a bordo](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md).

### Tormenta de partículas solares

- La tormenta de partículas solares es un aumento de protones energéticos de origen solar.

💡 **Contexto en la clase [B114-C04](../programa/clases/B114/B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md):**
- 🎯 **Por qué importa:** Una tormenta solar no se puede evitar, pero se puede limitar la dosis si la tripulación llega a tiempo a un lugar bien blindado. La decisión central: ¿cuánto blindaje y cuánto tiempo de reacción hacen falta para quedar bajo un objetivo de dosis?
- 🔗 **Se estudia junto con:** dosis equivalente, densidad areal, longitud de atenuación, refugio.

📘 **Dónde se aprende** (1 clase): [B114-C04 · Refugio contra tormentas solares y compartimentos de protección](../programa/clases/B114/B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md).

### Tormenta de tipo Carrington

- Una tormenta de tipo Carrington es una extrema.

💡 **Cómo se explica en la clase [B30-C18](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md):**
- Los estudios de la tormenta de Carrington del 2 de septiembre de 1859 (S2) y de una tormenta de tipo Carrington del 29 de octubre de 2003 observada en Tihany (S3) son el contexto, solo resumen.
- Ejercicio 11 · transferencia. Transferencia. ¿Qué limita extrapolar a tormentas de tipo Carrington?
- 🎯 **Por qué importa:** Prever la profundidad y la duración de una tormenta orienta la protección de redes y satélites. La decisión central: ¿qué mínimo alcanza `Dst*` y cuánto tarda en recuperarse?
- 🔗 **Se estudia junto con:** fase principal, fase de recuperación, tiempo de decaimiento, mínimo.

📘 **Dónde se aprende** (1 clase): [B30-C18 · Tormentas geomagnéticas](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md).

### Tornillo sin fin

- El tornillo sin fin mueve la corona; su periodo es el día sidéreo dividido por los dientes.

💡 **Cómo se explica en la clase [B43-C12](../programa/clases/B43/B43-C12-montura-ecuatorial/CLASE.md):**
- *Descripción textual:* el eje horario gira a la velocidad sidérea; el tornillo añade un error periódico cuya deriva depende de la exposición.
- En palabras: el eje sigue a velocidad constante y el tornillo añade una oscilación.
- 🎯 **Por qué importa:** Una exposición larga solo es nítida si el error de seguimiento es menor que un píxel. La decisión central: ¿a qué velocidad hay que girar el eje horario y cuánto puede derivar la imagen durante la exposición?
- 🔗 **Se estudia junto con:** velocidad sidérea, eje horario, periodo, error periódico.

📘 **Dónde se aprende** (1 clase): [B43-C12 · Montura ecuatorial](../programa/clases/B43/B43-C12-montura-ecuatorial/CLASE.md).

### Torque

- El torque (o momento de una fuerza) respecto de `O` es `τ = r × F`; en 2D, `τ = x F_y − y F_x`, en `N·m`.

💡 **Cómo se explica en la clase [B05-C09](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md):**
- El momento angular es al giro lo que el momento lineal a la traslación; el torque es a `L` lo que la fuerza es a `p`: `τ = dL/dt`.
- A["Fuerza F aplicada en la posición r"] --> B["Torque τ = r × F"]
- ⚠️ **Error frecuente:** Confundir torque con fuerza. Ejercicio 2.
- 🎯 **Por qué importa:** Un satélite en órbita elíptica va más rápido cerca de la Tierra que lejos; un patinador gira más rápido al recoger los brazos. La pregunta motivadora es: ¿qué cantidad se mantiene constante cuando algo gira bajo una fuerza central, y qué hace falta para cambiar un giro?
- 🔗 **Se estudia junto con:** momento angular, momento angular específico, momento de inercia, aceleración angular.

📖 **Explicado a fondo:** [Torque (momento de una fuerza)](esencial/ampliacion-n-z.md#torque-momento-de-una-fuerza) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B05-C09 · Momento angular y torque](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md).

### Total

- Un eclipse solar es total si la Luna cubre por completo el Sol;

💡 **Cómo se explica en la clase [B08-C09](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md):**
- En 2025 la distancia varió entre 356 830 y 406 690 km (S2): cerca del perigeo un eclipse central sería total, cerca del apogeo, anular.
- Pausa. El 21 de septiembre de 2025 la Luna estaba a 396 872 km; si el eclipse hubiese sido central, ¿habría sido total o anular? <details><summary>Respuesta</summary>`396 872 > 380 909 km`: el vértice no llega: anular.</details>
- 🎯 **Por qué importa:** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?
- 🔗 **Se estudia junto con:** umbra, penumbra, solar, lunar.

📘 **Dónde se aprende** (1 clase): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md).

### Tour

- El tour es la fase entre la captura joviana y la luna.
- Un tour es una secuencia de sobrevuelos de lunas.

💡 **Cómo se explica en la clase [B75-C20](../programa/clases/B75/B75-C20-diseno-de-una-mision-a-luna-helada/CLASE.md):**
- J --> U["Tour de lunas (sintetico 0.30 km/s)"]
- Límite: la escalera real tiene más peldaños (asistencias gravitacionales) y el tour no se calcula aquí.
- ⚠️ **Error frecuente:** Olvidar que el tour no se calculó. Se corrige con la sección 11.
- 🎯 **Por qué importa:** Antes de diseñar una misión hay que saber si es viable y qué la hace cara. La decisión central: ¿cuánto delta-v y cuánta masa cuesta ir de la Tierra a una luna de Júpiter, y cuánto se ahorra con una misión de sobrevuelos en lugar de un orbitador?
- 🔗 **Se estudia junto con:** orbitador, misión de sobrevuelos, esbozo preliminar, razón de masa.

📘 **Dónde se aprende** (2 clases): [B75-C20 · Diseño de una misión a luna helada](../programa/clases/B75/B75-C20-diseno-de-una-mision-a-luna-helada/CLASE.md); [B75-C26 · Sobrevuelos de lunas y tours de sistemas planetarios](../programa/clases/B75/B75-C26-sobrevuelos-de-lunas-y-tours-de-sistemas-planetarios/CLASE.md).

### TPD

- La TPD (desorción programada por temperatura) calienta con rampa lineal `T = T₀ + βt` y mide la tasa de salida.
- La TPD es la desorción programada por temperatura (B68-C01).

💡 **Cómo se explica en la clase [B68-C01](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md):**
- El máximo de la TPD cumple, con buena aproximación, `E = T_p [ln(ν₁ T_p/β) − 3,46]` (aproximación de Redhead, relación estándar que no se consultó y que el laboratorio verifica).
- Con una TPD sintética de `E = 1040 K` y `ν₁ = 10¹³ s⁻¹` (sintéticos), el pico sale a `32,927 K` y la fórmula devuelve `1039,7 K`: error `0,02 %`.
- 🎯 **Por qué importa:** Un hielo de CO que dura mil millones de años a 15 K desaparece en un segundo a 30 K. Esa sensibilidad exponencial decide dónde está la «línea de nieve» de cada molécula y qué hay en el gas.
- 🔗 **Se estudia junto con:** desorción, energía de enlace, factor preexponencial, orden cero.

📘 **Dónde se aprende** (2 clases): [B68-C01 · Desorción térmica de hielos interestelares](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md); [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### Trabajador

- Un trabajador es un proceso del `Pool`.

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Con cuatro procesos no hubo ganancia. No es un fallo: en Windows el método de arranque es `spawn` (S1), cada trabajador es un intérprete nuevo que debe importar NumPy, y ese arranque cuesta una fracción de segundo por proceso, del orden del trabajo útil de cada trozo.
- `Pool.map` reparte las entradas de una función entre procesos trabajadores.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.
- 🔗 **Se estudia junto con:** proceso, hilo, GIL, aceleración.

📘 **Dónde se aprende** (1 clase): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md).

### Trabajo

- El trabajo `W` de una fuerza constante es `F d cos θ`, donde `d` es el desplazamiento y `θ` el ángulo entre la fuerza y el desplazamiento.
- El trabajo por unidad de masa es la integral de la aceleración sobre la distancia.
- El trabajo aquí es el número de evaluaciones de la fuerza.

💡 **Cómo se explica en la clase [B05-C06](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md):**
- Si `θ > 90°`, el trabajo es negativo: la fuerza frena.
- Con `ΣF = m a` y `v² = v₀² + 2 a d` (C03) se obtiene `ΣF d = ½ m v² − ½ m v₀²`; es decir, el trabajo de la fuerza neta es el cambio de energía cinética: `W_neto = ΔE_c`.
- ⚠️ **Error frecuente:** Creer que toda fuerza hace trabajo. Ejercicio 6.
- 🎯 **Por qué importa:** Poner 1000 kg en órbita cuesta mucho más que subirlos 400 km. La pregunta motivadora es: ¿cuánta energía hay que entregar para cambiar el estado de un cuerpo, y en qué se convierte?
- 🔗 **Se estudia junto con:** energía cinética, energía potencial gravitatoria, energía mecánica, potencia.

📘 **Dónde se aprende** (3 clases): [B05-C06 · Trabajo y energía](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md); [B09-C12 · Teorema fundamental del cálculo](../programa/clases/B09/B09-C12-teorema-fundamental-del-calculo/CLASE.md); [B11-C26 · Benchmark de algoritmos numéricos](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md).

### Trabajo de compresión

- El trabajo de compresión por kg es `w = (p₂ v₂ − p₁ v₁)/(n−1)`.

💡 **Cómo se explica en la clase [B79-C12](../programa/clases/B79/B79-C12-procesos-adiabaticos-e-isentropicos/CLASE.md):**
- Calcular estado final y trabajo de una compresión isentrópica.
- El script [isentropico.py](isentropico.py) calcula tres compresiones de un cilindro, verifica el trabajo con la integral `∫ p dv` y la temperatura isentrópica con RK4 (comprueba diferencia < 1e-9 y trabajo < 1e-8).
- 🎯 **Por qué importa:** Las relaciones isentrópicas son el núcleo del análisis de toberas, compresores y turbinas; el tronco no las trata. Aquí se obtienen desde primeros principios y se ve cuándo valen.
- 🔗 **Se estudia junto con:** isentrópico, politrópico, relación de volúmenes.

📘 **Dónde se aprende** (1 clase): [B79-C12 · Procesos adiabáticos e isentrópicos](../programa/clases/B79/B79-C12-procesos-adiabaticos-e-isentropicos/CLASE.md).

### Trabajo del empuje

- El trabajo del empuje por unidad de masa es `a·v`; su integral es `ΔE`.

💡 **Cómo se explica en la clase [B81-C08](../programa/clases/B81/B81-C08-validacion-de-trayectorias-de-empuje-continuo/CLASE.md):**
- El trabajo del empuje es cero en eclipse; la integral debe reflejarlo (aceleración nula en esos tramos).
- 🎯 **Por qué importa:** Un resultado que solo se ha verificado con el mismo código no está validado. La decisión central: ¿qué chequeos independientes demuestran que una trayectoria de empuje continuo es correcta y que es un óptimo local?
- 🔗 **Se estudia junto con:** orden, primera variación, admisible.

📘 **Dónde se aprende** (1 clase): [B81-C08 · Validación de trayectorias de empuje continuo](../programa/clases/B81/B81-C08-validacion-de-trayectorias-de-empuje-continuo/CLASE.md).

### Trabajo neto

- El trabajo neto es `w = c_p T₁ [τ (1 − r^(−k)) − (r^k − 1)]` con `k = (γ−1)/γ` y `τ = T_max/T₁`.

💡 **Cómo se explica en la clase [B79-C15](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md):**
- Cada rendimiento isentrópico afecta al trabajo neto, que es una diferencia de dos grandes.
- *Descripción textual:* cuatro estaciones unidas por compresión, combustión a presión constante, expansión y descarga; el trabajo neto es el de la turbina menos el del compresor.
- 🎯 **Por qué importa:** B85-C11 trata ciclos térmicos de ensayo, no termodinámicos. Para entender el rendimiento de una turbina de gas hay que ver el ciclo que lo origina.
- 🔗 **Se estudia junto con:** ciclo de Brayton, rendimiento ideal, relación de presiones de trabajo máximo.

📘 **Dónde se aprende** (1 clase): [B79-C15 · Ciclos termodinámicos de propulsión](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md).

### Trabajo perdido

- El trabajo perdido (Gouy–Stodola) es `T₀ s_gen` con `T₀` la temperatura del ambiente.

💡 **Cómo se explica en la clase [B79-C11](../programa/clases/B79/B79-C11-segunda-ley-y-entropia/CLASE.md):**
- *Descripción textual:* el cambio de entropía entre estados da la entropía generada, que se traduce en trabajo perdido; una integral numérica comprueba la fórmula.
- Convertir la entropía generada en trabajo perdido.
- ⚠️ **Error frecuente:** Confundir trabajo perdido con la diferencia respecto al isentrópico. Se corrige con 8.2.
- 🎯 **Por qué importa:** Ninguna clase del tronco trata entropía ni irreversibilidad, necesarias para entender por qué un compresor real consume más que uno ideal y por qué un choque pierde presión total. La decisión central: ¿cuánta capacidad de trabajo pierde cada componente y por qué mecanismo?
- 🔗 **Se estudia junto con:** segunda ley, isentrópico, fuente de irreversibilidad.

📘 **Dónde se aprende** (1 clase): [B79-C11 · Segunda ley y entropía](../programa/clases/B79/B79-C11-segunda-ley-y-entropia/CLASE.md).

### Tracción

- La tracción `μ (1 − e^(−s/s₀))` es la fuerza de empuje por unidad de carga normal.

💡 **Cómo se explica en la clase [B102-C07](../programa/clases/B102/B102-C07-simulacion-de-movilidad-sobre-pendientes-y-terreno/CLASE.md):**
- *Descripción textual:* la pendiente, la tracción y la resistencia entran en un balance de fuerzas del que sale el patinaje de equilibrio; con él se obtiene la velocidad y el tiempo de ruta.
- Por fuerzas: tracción, resistencia y peso.
- 🎯 **Por qué importa:** Un rover no sube cualquier pendiente aunque no vuelque. La decisión central: ¿a qué pendiente se agota la tracción, cuánto patina antes y cuánto tarda una ruta con tramos de distinta inclinación?
- 🔗 **Se estudia junto con:** resistencia a la rodadura, patinaje de equilibrio, pendiente máxima, transitoria.

📘 **Dónde se aprende** (1 clase): [B102-C07 · Simulación de movilidad sobre pendientes y terreno](../programa/clases/B102/B102-C07-simulacion-de-movilidad-sobre-pendientes-y-terreno/CLASE.md).

### Tracción neta

- La tracción neta `DP` es el empuje menos la resistencia a la rodadura.

💡 **Cómo se explica en la clase [B97-C06](../programa/clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md):**
- *Descripción textual:* el peso y los parámetros del suelo dan el empuje; restando la rodadura se tiene la tracción neta y la pendiente máxima; el empuje se verifica integrando numéricamente.
- Calcular la tracción neta y la pendiente máxima aproximada.
- 🎯 **Por qué importa:** Un rover que se atasca puede perder la misión. Estimar cuánta tracción hay disponible en cada gravedad, y cómo varía con el deslizamiento, permite limitar pendientes y planear rutas.
- 🔗 **Se estudia junto con:** empuje, deslizamiento, cohesión, ángulo de fricción.

📘 **Dónde se aprende** (1 clase): [B97-C06 · Control de movilidad sobre regolito](../programa/clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md).

### Trade-off

- El trade-off (compromiso) es que cambios en profundidad y en volumen producen deformaciones parecidas.

💡 **Contexto en la clase [B57-C18](../programa/clases/B57/B57-C18-volcanismo-y-monitoreo/CLASE.md):**
- **Idea central (modelo mental):** Si empujas desde dentro una esponja tapada con un paño, el paño se levanta en forma de campana: más profundo, más ancha y baja; más superficial, más angosta y alta.
- 🎯 **Por qué importa:** Medir la deformación de un volcán permite inferir qué ocurre bajo tierra, pero la inversión no tiene respuesta única. La decisión central: ¿qué profundidad y qué volumen explican la deformación y con qué incertidumbre conjunta?
- 🔗 **Se estudia junto con:** fuente de Mogi, inversión.

📘 **Dónde se aprende** (1 clase): [B57-C18 · Volcanismo y monitoreo](../programa/clases/B57/B57-C18-volcanismo-y-monitoreo/CLASE.md).

### Tradición oral

- La tradición oral es el conjunto de saberes y expresiones transmitidos de forma hablada, cantada o practicada; la Convención de 2003 de la UNESCO la incluye entre los dominios del patrimonio inmaterial.

💡 **Cómo se explica en la clase [B133-C02](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. Un libro dice que «la tradición oral conserva el cielo de hace diez mil años».
- 🎯 **Por qué importa:** La transmisión oral se trata a menudo como una cadena frágil («se pierde») o como un archivo infalible («se conservó intacto»). Ninguna de las dos cosas está probada en general.
- 🔗 **Se estudia junto con:** canal, retención, corrupción, protocolo.

📘 **Dónde se aprende** (1 clase): [B133-C02 · Narrativas orales y transmisión del saber del cielo](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md).

### Traducción no oficial

- La traducción no oficial no tiene valor legal.

💡 **Cómo se explica en la clase [B121-C04](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md):**
- El Decreto Supremo 338 (firmado el 2001-07-17 y publicado en el Diario Oficial el 2001-08-17) creó un Comité Asesor Presidencial denominado Agencia Espacial de Chile, que asesora, coordina, propone una política y debe redactar un proyecto de ley para un marco institucional permanente (traducción no oficial de UNOOSA, leída).
- Ejercicio 10 · transferencia. Transferencia. Una traducción no oficial de un decreto, ¿sirve para cumplir la norma?
- ⚠️ **Error frecuente:** Citar una traducción no oficial como texto legal. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un marco nacional se conoce por sus instrumentos, y cada instrumento debe leerse en su texto vigente. La decisión central: ¿qué funciones regulatorias tienen un instrumento chileno identificado y con qué nivel de evidencia?
- 🔗 **Se estudia junto con:** nivel de evidencia, función regulatoria, instrumento, concesión.

📘 **Dónde se aprende** (1 clase): [B121-C04 · Marco legal espacial en Chile](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md).

### Trama CAN 2.0A

- La trama CAN 2.0A tiene `34 + 8n` bits de cabecera y datos (SOF…CRC), más 13 bits de cola (delimitador, ACK, EOF e IFS).

💡 **Cómo se explica en la clase [B88-C07](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md):**
- Una trama de `n = 8` tiene `34 + 64 = 98` bits entre SOF y CRC, más 13 de cola: `111`.
- En 5000 tramas aleatorias el máximo de rellenos fue 10 (media `3,30`); una trama de ceros añadió 16.
- 🎯 **Por qué importa:** El bus fija cuánta telemetría y cuántos comandos caben y con qué retardo. La decisión central: ¿cuál es el caudal útil y el peor tiempo de trama de cada bus para mi carga?
- 🔗 **Se estudia junto con:** relleno de bits, CRC-15, carácter de datos.

📘 **Dónde se aprende** (1 clase): [B88-C07 · Buses I2C SPI CAN y SpaceWire](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md).

### Trama de transferencia de telemetría

- La trama de transferencia de telemetría tiene una cabecera primaria de 6 octetos, un campo de datos, un campo de control operacional (OCF, opcional) y un campo de control de errores de trama (FECF, opcional, 2 octetos).

💡 **Cómo se explica en la clase [B94-C03](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md):**
- python programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/trama_tm.py
- 🎯 **Por qué importa:** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?
- 🔗 **Se estudia junto con:** SCID, VCID, contador de canal maestro, canal virtual.

📘 **Dónde se aprende** (1 clase): [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### Trámite

- Un trámite tiene una etapa de preparación y otra de evaluación.

💡 **Cómo se explica en la clase [B121-C05](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md):**
- T["Plazos de trámite"] --> C["Serie vs paralelo"]
- *Descripción textual:* los requisitos y el diseño forman la matriz; de ella salen los incumplimientos y la envolvente, y los plazos de trámite dan el camino crítico.
- 🎯 **Por qué importa:** Ninguna clase trata el análisis de cumplimiento. La decisión central: ¿cuál es el requisito más estricto de cada tipo, qué incumple el diseño y cuánto tardan los trámites?
- 🔗 **Se estudia junto con:** matriz de cumplimiento, envolvente, jurisdicción, camino crítico.

📘 **Dónde se aprende** (1 clase): [B121-C05 · Cumplimiento regulatorio en varias jurisdicciones](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md).

### Tramo

- Un tramo es un arco entre nodos con un Δv.
- El tramo es un intervalo de resolución al que una norma podría asociar condiciones.

💡 **Cómo se explica en la clase [B100-C06](../programa/clases/B100/B100-C06-logistica-cislunar-nodos-depositos-y-rutas-de-reabastecimiento/CLASE.md):**
- Segunda vía: con `ε = 0`, `exp(3,5/4,413) × exp(2,7/4,413) = 4,075292`, igual al tramo único de 6,2 km/s.
- *Descripción textual:* tres nodos con tramos de Δv ilustrativo: de órbita baja a NRHO, de NRHO a la superficie y de vuelta; la ruta directa A usa etapas desechables, la B un aterrizador reutilizable abastecido desde el depósito.
- 🎯 **Por qué importa:** Un depósito en órbita lunar parece una ventaja obvia, pero solo lo es si el propelente llega al depósito de una forma más barata que llevarlo directamente. La decisión central: ¿con qué transporte y con cuántos viajes del aterrizador reutilizable un depósito reduce la masa que hay que lanzar desde órbita baja?
- 🔗 **Se estudia junto con:** nodo, depósito, aterrizador reutilizable, remolcador eléctrico.

📘 **Dónde se aprende** (2 clases): [B100-C06 · Logística cislunar: nodos, depósitos y rutas de reabastecimiento](../programa/clases/B100/B100-C06-logistica-cislunar-nodos-depositos-y-rutas-de-reabastecimiento/CLASE.md); [B121-C02 · Licenciamiento de actividades de teledetección](../programa/clases/B121/B121-C02-licenciamiento-de-actividades-de-teledeteccion/CLASE.md).

### Trampa fría

- La trampa fría es un lugar con `T` tan baja que `J` es despreciable.

💡 **Cómo se explica en la clase [B53-C13](../programa/clases/B53/B53-C13-geomorfologia-de-hielos/CLASE.md):**
- Comparar una trampa fría con una superficie templada.
- Ejercicio 7 · autónomo. ¿Por qué una trampa fría conserva hielo?
- 🎯 **Por qué importa:** Una forma de hielo (un depósito, un glaciar, un cráter sombreado) persiste o desaparece según su temperatura. La decisión central: ¿a qué temperatura el hielo expuesto sobrevive miles de millones de años y a cuál se pierde en días?
- 🔗 **Se estudia junto con:** Clausius–Clapeyron, flujo de Hertz–Knudsen.

📘 **Dónde se aprende** (1 clase): [B53-C13 · Geomorfología de hielos](../programa/clases/B53/B53-C13-geomorfologia-de-hielos/CLASE.md).

### Transcripción

- La transcripción es el texto completo, sin sincronía.

💡 **Cómo se explica en la clase [B128-C05](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md):**
- W3C WAI distingue: los *captions* son el texto del habla y de los sonidos no hablados necesarios, sincronizados y normalmente activables; los *subtítulos* suelen ser traducciones a otro idioma; las transcripciones tienen el mismo texto que los captions; la audiodescripción describe lo visual.
- V["video con audio"] --> G["guion o transcripcion"]
- ⚠️ **Error frecuente:** Confundir subtítulos y transcripción. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un subtítulo mal sincronizado o demasiado rápido no se alcanza a leer, y una transcripción automática sin revisar puede decir lo contrario de lo dicho. La decisión central: ¿cómo compruebo que los subtítulos se pueden leer y que no cambian el sentido?
- 🔗 **Se estudia junto con:** subtítulos, audiodescripción, WebVTT, WER.

📘 **Dónde se aprende** (1 clase): [B128-C05 · Subtítulos y transcripciones](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md).

### Transferencia

- Una transferencia es copiar datos entre la memoria del equipo y la de la GPU.
- La transferencia es un paso de carga entre píxeles vecinos.
- Transferencia es usar lo aprendido en una situación distinta de la de aprendizaje.

💡 **Cómo se explica en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- A["Datos en memoria<br/>del equipo"] -->|"transferencia<br/>(ancho de banda)"| B["Memoria de la GPU"]
- C -->|"transferencia de vuelta"| D["Resultado en el equipo"]
- ⚠️ **Error frecuente:** Suponer aceleración sin contar la transferencia. Se corrige con la sección 8.2.
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?
- 🔗 **Se estudia junto con:** GPU, intensidad aritmética, reducción, reducción en árbol.

📖 **Explicado a fondo:** [Hohmann (transferencia)](esencial/esencial-d-l.md#hohmann-transferencia) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md); [B44-C02 · Sensores CCD](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md); [B131-C07 · Ejercicios de transferencia](../programa/clases/B131/B131-C07-ejercicios-de-transferencia/CLASE.md).

### Transferencia a operaciones

- La transferencia a operaciones entrega el sistema, sus procedimientos y su personal.

💡 **Cómo se explica en la clase [B83-C19](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md):**
- python programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/base_de_telemetria.py
- 🎯 **Por qué importa:** Un satélite entregado con una base de datos errónea muestra valores falsos o alarmas inútiles; operadores sin entrenamiento no saben responder. La decisión central: ¿la base de datos, los comandos y las personas están listos, de modo que operaciones pueda recibir el sistema?
- 🔗 **Se estudia junto con:** base de datos de telemetría y comandos, calibración polinómica, fuera de límites, aceptación.

📘 **Dónde se aprende** (1 clase): [B83-C19 · Aceptación y transferencia a operaciones](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md).

### Transferencia bi-elíptica

- La transferencia bi-elíptica tiene tres impulsos: el primero sube a una elipse con apoapsis `rb > r₂`; el segundo, en `rb`, cambia el periapsis a `r₂`; el tercero circulariza.

💡 **Cómo se explica en la clase [B75-C05](../programa/clases/B75/B75-C05-transferencias-bi-elipticas/CLASE.md):**
- Ejercicio 11 · transferencia. Un colega afirma que la bi-elíptica siempre gasta menos combustible.
- python programa/clases/B75/B75-C05-transferencias-bi-elipticas/bielipticas.py
- 🎯 **Por qué importa:** El delta-v es lo caro. A veces conviene gastar tiempo para ahorrarlo.
- 🔗 **Se estudia junto con:** es el cociente por encima del cual.

📘 **Dónde se aprende** (1 clase): [B75-C05 · Transferencias bi-elípticas](../programa/clases/B75/B75-C05-transferencias-bi-elipticas/CLASE.md).

### Transferencia conservativa

- La transferencia conservativa conserva masa total y momento angular orbital.

💡 **Cómo se explica en la clase [B24-C22](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md):**
- Calcular el nuevo semieje tras una transferencia conservativa de masa y momento angular.
- transferencia conservativa (donante 1.5, acretor 1.0, a_i = 10 R_sol):
- 🎯 **Por qué importa:** Una estrella que se expande (C16) o se hincha en una binaria puede llenar la región donde su gravedad domina y verter gas sobre su compañera. Esa transferencia cambia las masas, la órbita y el destino de ambas, y es el camino hacia muchos objetos exóticos.
- 🔗 **Se estudia junto con:** potencial de Roche, punto de Lagrange L1, lóbulo de Roche, radio del lóbulo.

📘 **Dónde se aprende** (1 clase): [B24-C22 · Evolución binaria: lóbulo de Roche y transferencia de masa](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md).

### Transferencia de baja energía

- Una transferencia de baja energía aprovecha además la perturbación del Sol, que este modelo no incluye.

💡 **Cómo se explica en la clase [B76-C08](../programa/clases/B76/B76-C08-transferencias-de-baja-energia/CLASE.md):**
- python programa/clases/B76/B76-C08-transferencias-de-baja-energia/jacobi.py
- 🎯 **Por qué importa:** Una transferencia de baja energía promete ahorrar propergol a cambio de tiempo, pero ¿qué ahorra y qué no? La decisión central: ¿qué energía hace falta para que una trayectoria pueda pasar por los cuellos de `L1` y `L2`, y qué no explica un modelo sin el Sol?
- 🔗 **Se estudia junto con:** constante de Jacobi, cuello, umbral, ángulo de salida.

📘 **Dónde se aprende** (1 clase): [B76-C08 · Transferencias de baja energía](../programa/clases/B76/B76-C08-transferencias-de-baja-energia/CLASE.md).

### Transferencia de carga

- La transferencia de carga es la diferencia de carga entre lados o ejes producida por la pendiente.

💡 **Cómo se explica en la clase [B102-C05](../programa/clases/B102/B102-C05-distribucion-de-cargas-y-estabilidad-ante-vuelco/CLASE.md):**
- Los ángulos de vuelco y las razones de transferencia de carga no dependen de `g`; las cargas, las aceleraciones críticas y las velocidades críticas en un giro sí.
- Calcular la carga de los ejes y la transferencia lateral en pendiente.
- 🎯 **Por qué importa:** Las leyes de operación de un rover fijan un máximo de inclinación. La decisión central: ¿cuánto margen queda frente al vuelco en una pendiente dada, y qué parte de ese margen depende de la gravedad?
- 🔗 **Se estudia junto con:** proyección del centro de masas, margen de vuelco, cabeceo, balanceo.

📘 **Dónde se aprende** (1 clase): [B102-C05 · Distribución de cargas y estabilidad ante vuelco](../programa/clases/B102/B102-C05-distribucion-de-cargas-y-estabilidad-ante-vuelco/CLASE.md).

### Transferencia de custodia

- La transferencia de custodia traslada la responsabilidad de entrega a un nodo.

💡 **Cómo se explica en la clase [B94-C04](../programa/clases/B94/B94-C04-redes-con-retardo-y-desconexion-enrutamiento-y-almacenamiento/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué papel tendría la transferencia de custodia en esta red?
- 🎯 **Por qué importa:** Un protocolo como TCP necesita confirmaciones en tiempo real; con 25 min de ida y vuelta o sin enlace durante horas, se hunde. La decisión central: ¿cuándo llega un paquete, cuánto almacenamiento exige y cuándo hay que descartarlo?
- 🔗 **Se estudia junto con:** contacto, plan de contactos, almacenamiento y reenvío, paquete.

📘 **Dónde se aprende** (1 clase): [B94-C04 · Redes con retardo y desconexión: enrutamiento y almacenamiento](../programa/clases/B94/B94-C04-redes-con-retardo-y-desconexion-enrutamiento-y-almacenamiento/CLASE.md).

### Transferencia de ganancia

- El método de transferencia de ganancia compara la potencia recibida con la AUT y con una antena de referencia: `G_AUT = G_ref + (P_AUT − P_ref)`.

💡 **Cómo se explica en la clase [B91-C05](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md):**
- Aplicar el método de transferencia de ganancia (sustitución) con una antena de referencia.
- Transferencia de ganancia (sustitucion), datos SINTETICOS con ruido gaussiano de 0.05 dB (semilla 91, 30 repeticiones):
- 🎯 **Por qué importa:** Una antena se acepta si su ganancia y su patrón medidos cumplen la especificación dentro de una incertidumbre conocida. La decisión central: ¿a qué distancia medir y con qué incertidumbre, para poder afirmar que la antena cumple?
- 🔗 **Se estudia junto con:** distancia de campo lejano, error de fase en el borde, incertidumbre combinada, expandida.

📘 **Dónde se aprende** (1 clase): [B91-C05 · Medición y calibración de antenas](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md).

### Transferencia de Hohmann

- La transferencia de Hohmann es la de menor Δv entre dos órbitas circulares coplanares.
- La transferencia de Hohmann es la elipse tangente a las dos circulares.

💡 **Cómo se explica en la clase [B56-C20](../programa/clases/B56/B56-C20-diseno-de-mision-astrobiologica-conceptual/CLASE.md):**
- Calcular los Δv y el tiempo de vuelo de una transferencia de Hohmann entre órbitas circulares.
- 🎯 **Por qué importa:** Una misión que busca vida combina ciencia, ingeniería y protección planetaria. Para decidir si es viable hay que traducir la pregunta científica en requisitos y comprobar que el presupuesto cierra.
- 🔗 **Se estudia junto con:** requisito, verificación, Δv, ecuación del cohete.

📘 **Dónde se aprende** (2 clases): [B56-C20 · Diseño de misión astrobiológica conceptual](../programa/clases/B56/B56-C20-diseno-de-mision-astrobiologica-conceptual/CLASE.md); [B71-C18 · Maniobra de Hohmann](../programa/clases/B71/B71-C18-maniobra-de-hohmann/CLASE.md).

### Transferencia de tiempo de dos sentidos

- La transferencia de tiempo de dos sentidos estima el desfase suponiendo trayectos simétricos.

💡 **Cómo se explica en la clase [B74-C16](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md):**
- En una transferencia de tiempo de dos sentidos, una asimetría de 20 ns genera `10,0 ns` de error de desfase.
- Explicar el error de una transferencia de tiempo de dos sentidos por la asimetría del trayecto.
- 🎯 **Por qué importa:** Un microsegundo son 150 m de alcance de ida y vuelta, y un reloj no estable sobre una hora ya acumula decenas de nanosegundos de error de predicción. La decisión central: ¿qué parte del error de tiempo se calibra, cuál se estima y cuál queda como ruido?
- 🔗 **Se estudia junto con:** desfase, frecuencia fraccional, desviación de Allan, ruido blanco de frecuencia.

📘 **Dónde se aprende** (1 clase): [B74-C16 · Sincronización temporal](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md).

### Transferencia intangible

- La transferencia intangible es la de software o conocimiento por medios electrónicos u orales.

💡 **Cómo se explica en la clase [B125-C05](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md):**
- Para una empresa que comparte planos con un socio, la transferencia intangible es la ruta más fácil de pasar por alto.
- «Licencia probable (incluye transferencia intangible)».
- 🎯 **Por qué importa:** La tecnología espacial está sujeta a controles de exportación que condicionan el negocio, y las alianzas de la clase anterior chocan con ellos; ninguna clase los trata. La decisión central: ¿qué ruta de exportación debe esperar un producto o una transferencia de tecnología y cuánto cuesta, en promedio, esperar la licencia?
- 🔗 **Se estudia junto con:** exportación, doble uso, licencia, denegación.

📘 **Dónde se aprende** (1 clase): [B125-C05 · Control de exportaciones y transferencia de tecnología](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md).

### Transferencia negativa

- La transferencia negativa es entrenar algo que perjudica en el sistema real.

💡 **Cómo se explica en la clase [B104-C09](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md):**
- Un único criterio, una curva exponencial inventada, costos ilustrativos, sin transferencia negativa y sin diferencias de fidelidad.
- Puede ser negativa (transferencia negativa): hay que medir con tareas del sistema real.
- 🎯 **Por qué importa:** El simulador es más barato que el vuelo, pero más horas no siempre ahorran más: hay saturación. La decisión central: ¿cuántas horas de simulador conviene programar y cómo se sabe que transfieren al sistema real?
- 🔗 **Se estudia junto con:** razón de efectividad de transferencia, fidelidad, saturación, criterio.

📘 **Dónde se aprende** (1 clase): [B104-C09 · Entrenamiento en simuladores](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md).

### Transformación de semejanza

- Una transformación de semejanza es el cambio de base `x = P z`.

💡 **Contexto en la clase [B16-C02](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md):**
- **Idea central (modelo mental):** `A` es el carácter propio del sistema: qué haría si lo soltaras. `B` es la palanca que tú tienes. `C` es la ventana por la que miras.
- 🎯 **Por qué importa:** El computador de a bordo de un satélite no maneja ecuaciones sueltas: maneja vectores y matrices, y una sola rutina sirve para cualquier eje, rueda o sensor que se le añada.
- 🔗 **Se estudia junto con:** representación en espacio de estados, exponencial matricial, matriz de transición, retenedor de orden cero.

📘 **Dónde se aprende** (1 clase): [B16-C02 · Representaciones en espacio de estados](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md).

### Transformación homogénea

- Transformación homogénea: matriz `T = [R p; 0 1]` de 4×4.

💡 **Cómo se explica en la clase [B101-C01](../programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/CLASE.md):**
- Construir una matriz homogénea de 4×4 y componer transformaciones en el orden correcto.
- Invertir una transformación homogénea con `[Rᵀ, −Rᵀp]`.
- 🎯 **Por qué importa:** Para mover un brazo hay que saber dónde está su extremo. Si el marco de cada eslabón está mal puesto, todo lo que sigue (cinemática inversa, singularidades, calibración) hereda el error.
- 🔗 **Se estudia junto con:** Marco {0}, Marco {E}, Parámetros D-H, Cinemática directa.

📘 **Dónde se aprende** (1 clase): [B101-C01 · Transformaciones homogéneas y parametrización de eslabones (Denavit-Hartenberg)](../programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/CLASE.md).

### Transformación inversa

- La transformación inversa corresponde a `−β`.

💡 **Cómo se explica en la clase [B26-C02](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *hoja de transformaciones verificadas*: transforma un evento a tres marcos, comprueba `s²`, compón dos *boosts*, verifica la inversa y demuestra que un rayo de luz se conserva.
- 🎯 **Por qué importa:** Para comparar la hora de un reloj en órbita con la de uno en tierra, o la dirección de una señal vista desde dos naves, hace falta una fórmula que traduzca coordenadas entre marcos. Esa fórmula debe respetar los postulados de C01.
- 🔗 **Se estudia junto con:** boost de Lorentz, intervalo, matriz de Lorentz, composición.

📘 **Dónde se aprende** (1 clase): [B26-C02 · Transformaciones de Lorentz](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md).

### Transformación rígida

- Un desplazamiento `(dy, dx)` es una traslación; una transformación rígida añade rotación; una afín añade escala y cizalla.

💡 **Contexto en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- **Idea central (modelo mental):** Dos transparencias con las mismas estrellas: deslizas una sobre la otra hasta que coinciden. La correlación de fase hace ese deslizamiento con la FFT, de una sola vez. Con puntos homólogos, en cambio, hallas la rotación y la traslación que mejor los hacen coincidir.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».
- 🔗 **Se estudia junto con:** registro, desplazamiento, afín, correlación cruzada.

📘 **Dónde se aprende** (1 clase): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md).

### Transformada de Fourier continua

- La transformada de Fourier continua de una función `f(t)` es, con la convención de S1 (DLMF §1.14), `F(x) = (1/√(2π)) ∫ f(t) e^{ixt} dt`; otras referencias usan el signo contrario en el exponente.

💡 **Contexto en la clase [B15-C04](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md):**
- **Idea central (modelo mental):** Un prisma separa la luz blanca en colores; la DFT separa una serie en frecuencias. Cada `X[k]` es un número complejo: su módulo dice cuánto de la frecuencia `k` hay; su ángulo (la fase) dice cuándo está el máximo de esa oscilación. Analogía: el prisma.
- 🎯 **Por qué importa:** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.
- 🔗 **Se estudia junto con:** número complejo, módulo, fórmula de Euler, transformada discreta de Fourier (DFT).

📘 **Dónde se aprende** (1 clase): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md).

### Transformada de Laplace

- La transformada de Laplace de una función `f(t)` definida para `t ≥ 0` es `F(s) = ∫₀^∞ e^(−st) f(t) dt` (S1, ec. 1.14.17), con `s` un número complejo cuya parte real es suficientemente grande para que la integral converja; sus unidades son s⁻¹.

💡 **Cómo se explica en la clase [B16-C05](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md):**
- El límite de la analogía: la transformada de Laplace es una herramienta para sistemas LTI con condiciones iniciales nulas; una saturación o una condición inicial no nula no se resumen con un solo cociente.
- 🎯 **Por qué importa:** Un ingeniero que diseña el control de actitud de un telescopio revisa decenas de variantes de ganancias.
- 🔗 **Se estudia junto con:** función de transferencia, polos, ceros, orden.

📘 **Dónde se aprende** (1 clase): [B16-C05 · Funciones de transferencia](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md).

### Transformada discreta

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B33-C06](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md):**
- Calcular `E(t)` por transformada discreta.
- 🎯 **Por qué importa:** El campo eléctrico depende de la conductividad y de la frecuencia. La decisión central: ¿cuánto vale el campo geoeléctrico y la corriente en una línea para un campo magnético dado?
- 🔗 **Se estudia junto con:** semiespacio uniforme, impedancia de superficie, campo geoeléctrico, corriente inducida.

📘 **Dónde se aprende** (1 clase): [B33-C06 · Corrientes geomagnéticas inducidas (GIC)](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md).

### Transformada discreta de Fourier

- La transformada discreta de Fourier (DFT) da los coeficientes `f̂_k`; la transformada rápida (FFT) la calcula con `O(N log N)` operaciones.

💡 **Contexto en la clase [B11-C16](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md):**
- **Idea central (modelo mental):** En lugar de describir la señal punto a punto, se descompone en sus armónicos. Derivar es multiplicar cada armónico por su frecuencia. Si la señal es suave, los armónicos altos son diminutos y bastan pocos.
- 🎯 **Por qué importa:** Cuando la solución es suave y periódica —una señal a lo largo de una órbita, un perfil de temperatura alrededor de un vehículo que gira, el campo en una caja periódica—, un método espectral logra con 24 puntos lo que unas diferencias finitas lograrían con millones.
- 🔗 **Se estudia junto con:** transformada rápida, derivada espectral, convergencia espectral, aliasing.

📘 **Dónde se aprende** (1 clase): [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md).

### Transformada discreta de Fourier (DFT)

- La transformada discreta de Fourier (DFT) de `N` muestras es `X[k] = Σ_{n=0}^{N−1} x[n] e^{−2π i k n/N}`, para `k = 0, …, N − 1`; es la convención usada en NumPy y en esta clase.

💡 **Cómo se explica en la clase [B15-C04](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md):**
- Definir la transformada discreta de Fourier (DFT) y calcular una de 4 muestras a mano.
- 🎯 **Por qué importa:** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.
- 🔗 **Se estudia junto con:** número complejo, módulo, fórmula de Euler, transformada de Fourier continua.

📘 **Dónde se aprende** (1 clase): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md).

### Transformada inversa

- La transformada inversa genera una muestra aplicando la inversa de la acumulada a números uniformes.

💡 **Cómo se explica en la clase [B52-C13](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md):**
- Muestrearla por transformada inversa con semilla fija.
- El script [tamanos.py](tamanos.py) genera la muestra sintética por transformada inversa, estima `q` por máxima verosimilitud y compara fracciones de número y de masa con las analíticas (comprueba 3 errores estándar y `0,15`).
- 🎯 **Por qué importa:** Cómo se reparte la masa entre tamaños indica qué cuerpos dominan una población y qué mide un censo incompleto. La decisión central: ¿cómo se estima el exponente de una ley de potencias y qué tan fiable es la masa que implica?
- 🔗 **Se estudia junto con:** ley de potencias, estimador de máxima verosimilitud, fracción de masa, truncada.

📘 **Dónde se aprende** (1 clase): [B52-C13 · Pequeños cuerpos remanentes](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md).

### Transformada rápida

- La transformada discreta de Fourier (DFT) da los coeficientes `f̂_k`; la transformada rápida (FFT) la calcula con `O(N log N)` operaciones.

💡 **Contexto en la clase [B11-C16](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md):**
- **Idea central (modelo mental):** En lugar de describir la señal punto a punto, se descompone en sus armónicos. Derivar es multiplicar cada armónico por su frecuencia. Si la señal es suave, los armónicos altos son diminutos y bastan pocos.
- 🎯 **Por qué importa:** Cuando la solución es suave y periódica —una señal a lo largo de una órbita, un perfil de temperatura alrededor de un vehículo que gira, el campo en una caja periódica—, un método espectral logra con 24 puntos lo que unas diferencias finitas lograrían con millones.
- 🔗 **Se estudia junto con:** transformada discreta de Fourier, derivada espectral, convergencia espectral, aliasing.

📘 **Dónde se aprende** (1 clase): [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md).

### Transformada unscented

- La transformada unscented aproxima la distribución con `2n+1` puntos sigma y los pesos `w_m`, `w_c`.
- La transformada unscented propaga `2n+1` puntos.

💡 **Cómo se explica en la clase [B74-C10](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md):**
- Describir la transformada unscented: puntos sigma, pesos y recomposición.
- 🎯 **Por qué importa:** Un filtro puede dar una estimación aceptable y una covarianza falsa. La decisión central: ¿cuándo basta el EKF y cuándo la covarianza obliga a usar un filtro no lineal, y cómo lo verifico con una referencia?
- 🔗 **Se estudia junto con:** puntos sigma, UKF, muestreo de importancia, ECM.

📘 **Dónde se aprende** (2 clases): [B74-C10 · Filtro de Kalman no lineal](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md); [B74-C12 · Propagación de incertidumbre — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Transición

- Una transición es el salto de un electrón entre dos niveles.
- La transición es el paso de laminar a turbulento, convencionalmente en `Re_x ≈ 5 × 10⁵` en placa y `Re ≈ 2300` en tubo.
- Una transición es un cambio de modo.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Con `h c = 1239,84 eV·nm` (que sale de las constantes exactas del SI, S1), una transición de 1,89 eV corresponde a `λ = 1239,84/1,89 ≈ 656 nm`, justamente la línea H-alfa.
- Dato de partida: la transición 3→2 del hidrógeno, con constantes CODATA 2022 (S1).
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.
- 🔗 **Se estudia junto con:** átomo, núcleo, protones, neutrones.

📘 **Dónde se aprende** (6 clases): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B46-C12 · Emisiones moleculares](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md); [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md); [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md); [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md); [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md).

### Transición simple–compleja

- La transición simple–compleja es el diámetro `D_sc` en que cambia la forma.

💡 **Cómo se explica en la clase [B61-C03](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md):**
- La evidencia es la ficha de la transición simple–compleja del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de la transición simple–compleja*: el modelo de umbral por gravedad, su calibración con la Luna, el contraste con Marte, el exponente libre y el resultado de la relajación de pendientes, con rótulos.
- 🎯 **Por qué importa:** Sin la transición simple–compleja no se puede interpretar la forma de un cráter grande ni comparar cuerpos. La decisión central: ¿a qué diámetro cambia la morfología y cómo depende de la gravedad?
- 🔗 **Se estudia junto con:** pico central, terrazas, resistencia efectiva, ángulo crítico.

📘 **Dónde se aprende** (1 clase): [B61-C03 · Cráteres complejos: colapso, picos centrales y terrazas](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md).

### Tránsito

- El ángulo horario `H` es el ángulo, medido hacia el oeste, entre el meridiano y el círculo que pasa por el astro y los polos; vale cero cuando el astro cruza el meridiano (tránsito o culminación, S2).
- El tránsito es la disminución de brillo cuando un cuerpo pasa por delante de su estrella; su profundidad es la fracción de flujo que se pierde.
- El tránsito es el paso de un planeta frente a su estrella.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C04](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md):**
- Un barrido minuto a minuto del programa (interpolando linealmente la tabla S1 entre filas de 2 h; ±5 min) da: salida a las 22:26 UT, tránsito a las 03:57 UT y puesta a las 09:26 UT.
- El intervalo salida–tránsito (5,5 h) supera las 5,3 h porque la Luna avanza hacia el este entre las estrellas (≈ 0,6° por hora) y su ángulo horario crece algo más despacio que el del cielo.
- 🎯 **Por qué importa:** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».
- 🔗 **Se estudia junto con:** altura, distancia cenital, acimut, ángulo horario.

📖 **Explicado a fondo:** [Tránsito](esencial/esencial-m-z.md#tránsito) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md); [B48-C04 · Planificación por visibilidad](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md); [B56-C14 · Biofirmas espectrales](../programa/clases/B56/B56-C14-biofirmas-espectrales/CLASE.md); [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Transitoria

- La transitoria es el tiempo que tarda la velocidad en llegar al equilibrio.

💡 **Cómo se explica en la clase [B102-C07](../programa/clases/B102/B102-C07-simulacion-de-movilidad-sobre-pendientes-y-terreno/CLASE.md):**
- Descripción larga: el patinaje crece rápido cerca de la pendiente máxima, que no depende de `g`; la gravedad solo cambia la rapidez de la transitoria.
- Ejercicio 8 · autónomo. ¿Cuántas veces es más lenta la transitoria en la Luna que en la Tierra?
- 🎯 **Por qué importa:** Un rover no sube cualquier pendiente aunque no vuelque. La decisión central: ¿a qué pendiente se agota la tracción, cuánto patina antes y cuánto tarda una ruta con tramos de distinta inclinación?
- 🔗 **Se estudia junto con:** tracción, resistencia a la rodadura, patinaje de equilibrio, pendiente máxima.

📘 **Dónde se aprende** (1 clase): [B102-C07 · Simulación de movilidad sobre pendientes y terreno](../programa/clases/B102/B102-C07-simulacion-de-movilidad-sobre-pendientes-y-terreno/CLASE.md).

### Transitorio

- Un transitorio es una fuente de brillo variable en escala corta.

💡 **Cómo se explica en la clase [B28-C08](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md):**
- La evidencia es la ficha de un transitorio y su cadencia del ejercicio 12 (sección 20).
- Ejercicio 10 · transferencia. ¿Por qué un transitorio que cae más rápido es más difícil de detectar?
- 🎯 **Por qué importa:** Un transitorio que dura menos que el intervalo entre visitas se pierde. El índice de caída decide cuánto dura un evento sobre el límite de detección.
- 🔗 **Se estudia junto con:** curva de luz, índice de caída, límite de detección, cadencia.

📘 **Dónde se aprende** (1 clase): [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md).

### Transmisibilidad

- La transmisibilidad es `T = √((1 + (2ζr)²)/((1 − r²)² + (2ζr)²))` con `r = f/f_n`.
- Factor `Q`: amplificación en resonancia. Transmisibilidad: cociente respuesta/entrada en función de la frecuencia.

💡 **Cómo se explica en la clase [B47-C11](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md):**
- Con una frecuencia natural de `10 Hz` (ilustrativa) y `ζ = 0,05`, la transmisibilidad es `10,05` en la resonancia, `1` en `r = √2` y `0,0143` en `r = 10`; con `ζ = 0,5` esas cifras son `1,414`, `1` y `0,1010`.
- 🎯 **Por qué importa:** Un aislador mal sintonizado amplifica en vez de atenuar. La decisión central: ¿qué frecuencia natural y qué amortiguamiento aíslan sin amplificar demasiado en la resonancia?
- 🔗 **Se estudia junto con:** frecuencia natural, razón de frecuencias, amortiguamiento, resonancia.

📘 **Dónde se aprende** (3 clases): [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B84-C11 · Vibraciones y resonancias](../programa/clases/B84/B84-C11-vibraciones-y-resonancias/CLASE.md); [B90-C09 · Ensayos de vibración](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md).

### Transmisión

- La transmisión `T = e^{−τ/μ}` con `μ = cos χ` es la fracción que atraviesa.
- La transmisión `T(λ)`.
- La transmisión `e^(−τ)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B45-C03](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md):**
- Una transmisión residual de `10⁻³` sobre 700 nm aumenta el flujo medido un `0,794 %` para 3000 K y un `0,1123 %` para 10 000 K.
- La evidencia es la ficha de la curva de transmisión del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Una banda se describe por su curva completa, no por dos números. La decisión central: ¿cómo se combinan las curvas y qué longitud de onda se asigna a una banda?
- 🔗 **Se estudia junto con:** ancho equivalente, longitud de onda efectiva, longitud de onda de pivote, fuga.

📘 **Dónde se aprende** (4 clases): [B45-C03 · Curvas de transmisión](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md); [B45-C11 · Líneas de absorción](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md); [B47-C01 · Ventajas de observación fuera de atmósfera](../programa/clases/B47/B47-C01-ventajas-de-observacion-fuera-de-atmosfera/CLASE.md); [B54-C12 · Interacción con radiación solar](../programa/clases/B54/B54-C12-interaccion-con-radiacion-solar/CLASE.md).

### Transmisión de poro

- La transmisión de poro `W = 1/(1 + 3d/(8 r_p))` es la fracción de moléculas que, saliendo del hielo, atraviesan una capa de espesor `d` con poros de radio `r_p`.

💡 **Cómo se explica en la clase [B67-C06](../programa/clases/B67/B67-C06-perdida-de-volatiles-por-sublimacion-y-migracion-termica/CLASE.md):**
- Límite: se ignora el calor latente de la sublimación, la dependencia de `κ` con la temperatura, la radiación en los poros y el transporte del vapor por otros caminos; la transmisión es una relación de ingeniería que no se consultó.
- Estimar el flujo de vapor del hielo enterrado con una transmisión de poro.
- 🎯 **Por qué importa:** Una oscilación de temperatura de pocos kelvin cambia la pérdida en órdenes de magnitud, y esa oscilación decae con la profundidad. La decisión central: ¿a qué profundidad el hielo es estable, y cuánto engaña usar la temperatura media?
- 🔗 **Se estudia junto con:** onda térmica, profundidad de penetración, desigualdad de Jensen.

📘 **Dónde se aprende** (1 clase): [B67-C06 · Pérdida de volátiles por sublimación y migración térmica](../programa/clases/B67/B67-C06-perdida-de-volatiles-por-sublimacion-y-migracion-termica/CLASE.md).

### Transmitancia

- La reflectancia `R` y la transmitancia `T`.
- La transmitancia `t(x)`.

💡 **Contexto en la clase [B41-C02](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md):**
- **Idea central (modelo mental):** Como un coche que entra de lado en un barrizal: la rueda que entra primero se frena y el coche gira hacia la normal; si el barro frena mucho y se entra muy tangente, la trayectoria no entra (reflexión total).
- 🎯 **Por qué importa:** Un telescopio refractor y los recubrimientos dependen de cuánta luz se refleja y a qué ángulo se dobla. La decisión central: ¿qué fracción de luz se pierde por reflexión y cuándo hay reflexión total?
- 🔗 **Se estudia junto con:** ley de Snell, ángulo crítico, ángulo de Brewster, reflectancia.

📘 **Dónde se aprende** (2 clases): [B41-C02 · Índice de refracción y ley de Snell](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md); [B42-C04 · Difracción de aperturas](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md).

### Transmitancia total

- La transmitancia total `T_d T_u` es la fracción que baja y sube.

💡 **Cómo se explica en la clase [B57-C26](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md):**
- La transmitancia total del rojo es `T_d T_u = 0,4704` y la reflectancia de trayectoria `0,01920`: la neblina atmosférica aporta casi la mitad de la señal de una superficie oscura.
- 🎯 **Por qué importa:** Comparar imágenes de fechas distintas con atmósferas distintas confunde atmósfera con cambio. La decisión central: ¿cuánto sesga la atmósfera y cómo se estima y descuenta con la información disponible?
- 🔗 **Se estudia junto con:** reflectancia de trayectoria, albedo esférico, corrección atmosférica, objeto oscuro.

📘 **Dónde se aprende** (1 clase): [B57-C26 · Corrección atmosférica de imágenes](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md).

### Transparencia

- La transparencia es la fracción de luz que llega.
- La transparencia es informar con apertura y a tiempo.
- La transparencia es la apertura de información.

💡 **Cómo se explica en la clase [B45-C17](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md):**
- La variación de la transparencia fuera de tránsito es `3,410 %` RMS.
- Límite: transparencia igual para todas las estrellas.
- 🎯 **Por qué importa:** La atmósfera varía más que la señal; sin una referencia, la curva de luz no sirve. La decisión central: ¿qué comparaciones y qué precisión se necesitan para una profundidad dada?
- 🔗 **Se estudia junto con:** curva diferencial, conjunto, ruido de fotones, profundidad.

📘 **Dónde se aprende** (3 clases): [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md); [B56-C19 · Ética del descubrimiento de vida](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md); [B119-C18 · Ética y derechos en actividades espaciales](../programa/clases/B119/B119-C18-etica-y-derechos-en-actividades-espaciales/CLASE.md).

### Transpuesta

- La transpuesta `Aᵀ` intercambia filas y columnas.

💡 **Contexto en la clase [B10-C03](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md):**
- **Idea central (modelo mental):** Una matriz dice qué hace el operador con cada vector de la base; todo lo demás sale por linealidad.
- 🎯 **Por qué importa:** Una estación terrestre está fija respecto de la Tierra, pero la Tierra gira respecto del espacio inercial. Para saber dónde está la estación en el sistema inercial a cada instante hay que aplicar una transformación que depende del tiempo.
- 🔗 **Se estudia junto con:** operador lineal, matriz, matriz de T en una base, producto matricial.

📘 **Dónde se aprende** (1 clase): [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md).

### Transversal

- La velocidad radial es `μ e sin ν/h` y la transversal `h/r`.
- La componente de línea de visión y la transversal son las incertidumbres a lo largo de la dirección de la nave y perpendicular a ella.
- En una onda transversal, el medio se mueve perpendicular a la propagación (cuerda); en una longitudinal, paralelo (sonido).

💡 **Cómo se explica en la clase [B05-C12](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md):**
- Distinguir ondas transversales y longitudinales y explicar que necesitan un medio.
- 🎯 **Por qué importa:** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.
- 🔗 **Se estudia junto con:** onda mecánica, longitudinal, longitud de onda, frecuencia.

📘 **Dónde se aprende** (3 clases): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B71-C17 · Movimientos en planos orbitales](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md); [B74-C15 · Geometría de la red de seguimiento](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md).

### Trapezoidal

- BDF2 (fórmula de diferenciación hacia atrás de orden 2): `y_{n+1} = (4 y_n − y_{n−1})/3 + (2h/3) f(t_{n+1}, y_{n+1})`. Trapezoidal: `y_{n+1} = y_n + (h/2)[f(t_n, y_n) + f(t_{n+1}, y_{n+1})]`.
- El perfil triangular acelera y frena sin crucero; el trapezoidal incluye un tramo a velocidad máxima.

💡 **Cómo se explica en la clase [B11-C22](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md):**
- BDF2 `1,6 × 10⁻⁸ … 2,5 × 10⁻¹⁰`, órdenes `2,00`; trapezoidal `4,0 × 10⁻⁹ … 6,3 × 10⁻¹¹`, órdenes `2,00`.
- Euler implícito (`2,7 × 10⁻⁷` en `t = 2`), igual; el trapezoidal conserva una oscilación de `0,157` que no se apaga, porque su factor de amplificación tiende a `−1`, no a 0 (por ejemplo, con `z = −100`, `(1 − 50)/(1 + 50) = −0,96`).
- ⚠️ **Error frecuente:** Elegir el trapezoidal con transitorios. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Los modelos térmicos, de combustión, de propulsión y de química atmosférica mezclan escalas de microsegundos con horas. Un integrador explícito pagaría el paso del más rápido durante toda la simulación.
- 🔗 **Se estudia junto con:** implícito, Euler implícito, BDF2, Newton.

📘 **Dónde se aprende** (2 clases): [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md); [B87-C11 · Ruedas de reacción](../programa/clases/B87/B87-C11-ruedas-de-reaccion/CLASE.md).

### Traspuesta

- La inversa de una rotación es su traspuesta: `R⁻¹ = Rᵀ`.

💡 **Cómo se explica en la clase [B04-C15](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md):**
- Girar los ejes `+0,5 rad` alrededor de `x` equivale a girar el punto `−0,5 rad`; la matriz de la segunda es la traspuesta de la primera.
- *Descripción textual:* de las componentes ecuatoriales se pasa a las eclípticas con la rotación pasiva `R_x(ε)`; la traspuesta devuelve las ecuatoriales; de las eclípticas salen longitud y latitud con `atan2` y `arcsen`; y la matriz se comprueba con ortogonalidad y determinante 1.
- 🎯 **Por qué importa:** El ecuador de la Tierra y el plano de su órbita (la eclíptica) forman un ángulo de unos 23,4°. Los catálogos de estrellas se dan en coordenadas ecuatoriales; el movimiento del Sol, la Luna y los planetas es más simple en coordenadas eclípticas.
- 🔗 **Se estudia junto con:** matriz de rotación, ortogonal, determinante, inversa.

📘 **Dónde se aprende** (1 clase): [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md).

### Tratado del Espacio Ultraterrestre

- El Tratado del Espacio Ultraterrestre (1967) establece principios para la actividad de los estados en el espacio (S5).

💡 **Cómo se explica en la clase [B02-C19](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md):**
- B --> F["1967: Tratado del Espacio<br/>Ultraterrestre"]
- Enunciar tres principios del Tratado del Espacio Ultraterrestre.
- 🎯 **Por qué importa:** La exploración espacial es una historia científica y también política. La pregunta motivadora es: ¿qué cambió, para la astronomía y para la sociedad, cuando los instrumentos y las personas empezaron a salir de la atmósfera, y qué reglas se acordaron?
- 🔗 **Se estudia junto con:** satélite artificial, órbita baja, duración del vuelo, período orbital.

📘 **Dónde se aprende** (1 clase): [B02-C19 · Historia de la exploración espacial](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md).

### Traversabilidad

- La traversabilidad es la capacidad de un vehículo de cruzar una celda.

💡 **Cómo se explica en la clase [B103-C04](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md):**
- La evidencia es la mapa de traversabilidad con matriz de confusión del ejercicio 12 (sección 20).
- El hundimiento y el deslizamiento de las ruedas: la traversabilidad real también depende de las propiedades del suelo, que este mapa no incluye.
- 🎯 **Por qué importa:** El ruido del MDE crece con el cuadrado del rango y, a partir de cierta distancia, la señal de un obstáculo queda por debajo del ruido. La decisión central: ¿hasta qué rango se puede clasificar el terreno de forma útil, y qué política (conservadora o corregida) elegir más allá?
- 🔗 **Se estudia junto con:** pendiente, escalón, rugosidad, falso «seguro».

📘 **Dónde se aprende** (1 clase): [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Traversable

- Rugosidad: dispersión de la altura respecto de un plano local. Traversable: celda que cumple los umbrales de pendiente y rugosidad.

💡 **Cómo se explica en la clase [B99-C05](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md):**
- Con umbrales de 15° y 5 cm (sintéticos) se declara traversable 96 % del interior; la roca (pendiente máxima 22,9°) queda no traversable en 8 de sus 12 celdas, por pendiente y no por rugosidad (rugosidad máxima 4,9 cm).
- 🎯 **Por qué importa:** Un mapa útil para navegar distingue lo ocupado, lo libre y lo que no se sabe, y dice si el terreno es pisable. La decisión central: ¿cómo fusionar medidas ruidosas en cada celda y qué umbrales de pendiente y rugosidad declaran un terreno traversable?
- 🔗 **Se estudia junto con:** Rejilla de ocupación, Log-odds, Recorte (clamping), Rejilla de elevación (2.5D).

📘 **Dónde se aprende** (1 clase): [B99-C05 · Mapas de ocupación y rejillas de elevación](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md).

### Trayectorias vecinas

- Con trayectorias vecinas, se mide `d_n/d_0` y se renormaliza la separación.

💡 **Cómo se explica en la clase [B73-C14](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md):**
- Para `K = 5` el exponente medio es `0,9741` por iteración con el vector tangente y `0,9741` con trayectorias vecinas (`0,00%` de diferencia); la estimación `ln(K/2)` da `0,9163`.
- Calcularlo con dos trayectorias vecinas y compararlos.
- 🎯 **Por qué importa:** El exponente de Lyapunov es el número que cuantifica el caos: fija el horizonte de predicción y distingue una trayectoria regular de una caótica. En un espacio de fases mixto, un solo exponente no basta.
- 🔗 **Se estudia junto con:** exponente de Lyapunov máximo, vector tangente, tiempo de Lyapunov, espacio de fases mixto.

📘 **Dónde se aprende** (1 clase): [B73-C14 · Exponentes de Lyapunov](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md).

### Traza

- Una traza es una tabla que anota el valor de las variables después de cada paso.
- La traza es la suma de la diagonal.
- La traza es la contracción `Tᵢᵢ` (S1: suma de la diagonal, §1.2(vi), ec. 1.2.62).
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C01](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md):**
- La traza para los datos de la sección 5 empieza con «mejor = Mercurio, 87,969».
- Una traza te permite descubrir errores de lógica sin que el computador intervenga.
- 🎯 **Por qué importa:** En astronomía casi todo resultado pasa por un procedimiento repetible: reducir imágenes, ajustar una órbita, buscar el máximo de una curva de luz. Si no puedes describir el procedimiento con precisión, no puedes ejecutarlo en un computador ni dárselo a otra persona para que lo repita.
- 🔗 **Se estudia junto con:** algoritmo, entrada, salida, pseudocódigo.

📘 **Dónde se aprende** (9 clases): [B07-C01 · Pensamiento algorítmico](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md); [B07-C12 · Manejo de errores y excepciones](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md); [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md); [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md); [B106-C21 · Depuración de trazas gaseosas de la atmósfera de cabina](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md) y 3 más.

### Traza al suelo

- La traza al suelo es el recorrido de la proyección de la nave sobre la superficie.

💡 **Cómo se explica en la clase [B75-C17](../programa/clases/B75/B75-C17-oportunidades-cientificas-de-sobrevuelo/CLASE.md):**
- Calcular la traza al suelo y la velocidad sobre el suelo.
- h_ca [km] e giro [grados] v_p [km/s] v suelo en h_ca [km/s] t en ventana [min] traza [km] resol. en h_ca [m] resol. a 1000 km [m] datos [Gbit]
- 🎯 **Por qué importa:** Cada metro de altitud cuesta resolución, y cada segundo de ventana cuesta datos. La decisión central: ¿qué altitud de máxima aproximación equilibra resolución, cobertura y volumen de datos en un sobrevuelo?
- 🔗 **Se estudia junto con:** ventana de observación, velocidad sobre el suelo, resolución lineal, volumen de datos.

📘 **Dónde se aprende** (1 clase): [B75-C17 · Oportunidades científicas de sobrevuelo](../programa/clases/B75/B75-C17-oportunidades-cientificas-de-sobrevuelo/CLASE.md).

### Traza repetida

- La traza repetida `N/D` significa `N` órbitas en `D` días.

💡 **Cómo se explica en la clase [B57-C23](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md):**
- Si Landsat 8 repitiera 233 órbitas en 16 días (esta cifra no se consultó; es una hipótesis de la clase), la altitud de traza repetida sería `699,6 km` y el espaciado `172,0 km`, menor que el barrido de 185 km.
- Hallar la altitud de una traza repetida `N/D` por bisección.
- 🎯 **Por qué importa:** Si la órbita no repite sus trazas o el barrido no cubre el espacio entre ellas, quedan huecos. La decisión central: ¿qué altitud e inclinación dan un ciclo de repetición que cubre todo con el barrido disponible?
- 🔗 **Se estudia junto con:** órbita heliosíncrona, periodo nodal, espaciado entre trazas, revisita.

📘 **Dónde se aprende** (1 clase): [B57-C23 · Diseño de órbita y revisita para observación terrestre](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md).

### Trazabilidad

- La trazabilidad es la capacidad de seguir una afirmación hasta su origen.
- La trazabilidad es poder seguir cada requisito hasta su comprobación.
- La trazabilidad es la capacidad de reconstruir, para una cifra, los datos, el código, los parámetros y el entorno que la produjeron.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C19](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md):**
- Lo que decide es la trazabilidad, no el peldaño.
- 🎯 **Por qué importa:** Un titular dice: «Neutrinos superan la velocidad de la luz: Einstein estaba equivocado». Es una afirmación fuerte.
- 🔗 **Se estudia junto con:** fuente primaria, fuente oficial, fuente secundaria, preprint.

📘 **Dónde se aprende** (10 clases): [B01-C19 · Fuentes confiables y desinformación espacial](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md); [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md); [B90-C18 · Trazabilidad de evidencias](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md); [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md) y 4 más.

### Trazabilidad documentada

- La trazabilidad documentada exige que cada calibración deje constancia (S2, 2.41).

💡 **Contexto en la clase [B13-C19](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md):**
- **Idea central (modelo mental):** Imagina una ficha de laboratorio con un sello de cera. La ficha dice quién calibró, con qué, cuándo y cuánto vale la incertidumbre; el sello (el hash) se rompe si alguien cambia algo. Un revisor automático comprueba que la ficha está completa, vigente y con el sello intacto.
- 🎯 **Por qué importa:** Dentro de un año alguien usará los datos de un fotodiodo calibrado hoy. Necesitará saber con qué patrones, a qué temperatura, con qué incertidumbre y hasta cuándo es válida la calibración.
- 🔗 **Se estudia junto con:** metadato, registro de calibración, vigencia, hash SHA-256.

📘 **Dónde se aprende** (1 clase): [B13-C19 · Metadatos y registros de calibración](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md).

### Trazabilidad metrológica

- La trazabilidad metrológica es la propiedad de un resultado de medida por la cual puede relacionarse con una referencia mediante una cadena ininterrumpida y documentada de calibraciones, cada una de las cuales contribuye a la incertidumbre (S2, 2.41).

💡 **Cómo se explica en la clase [B13-C02](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md):**
- Definir trazabilidad metrológica con sus tres requisitos.
- 🎯 **Por qué importa:** Un satélite recibe un comando con un tiempo de encendido de motor; el ingeniero de tierra usó una fórmula del periodo orbital copiada de una hoja de cálculo. Si la fórmula está mal dimensionada, el resultado sale en «segundos al cuadrado» o en «metros por segundo» sin que nadie lo note.
- 🔗 **Se estudia junto con:** dimensión, M, L, T.

📘 **Dónde se aprende** (1 clase): [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md).

### Trazable

- Una cifra trazable puede rastrearse hasta sus entradas.

💡 **Contexto en la clase [B126-C06](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md):**
- 🎯 **Por qué importa:** [B124-C19](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) redacta propuestas de misión, no financieras. La decisión central: ¿qué cifra se muestra, con qué rótulo y con qué rango, de modo que un tercero pueda comprobarla?
- 🔗 **Se estudia junto con:** matriz de evidencia, rótulo, rango de incertidumbre, solicitación general.

📘 **Dónde se aprende** (1 clase): [B126-C06 · Presentación financiera ante inversionistas con evidencia](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md).

### Trazado exacto

- El trazado exacto resuelve la intersección rayo–superficie sin aproximar.

💡 **Cómo se explica en la clase [B41-C08](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué el trazado exacto exige elegir la raíz de intersección correcta?
- El script [trazado.py](trazado.py) traza rayos exactos por dos esferas y mide la focal por altura (comprueba `h → 0` contra la matriz a `10⁻⁴ mm` y el exponente en `2 ± 0,2`).
- 🎯 **Por qué importa:** Los programas de diseño óptico trazan rayos exactos. La decisión central: ¿cuándo se separa el rayo real del paraxial y cómo crece esa diferencia?
- 🔗 **Se estudia junto con:** aproximación paraxial, distancia focal posterior (BFD), aberración esférica longitudinal, altura del rayo.

📘 **Dónde se aprende** (2 clases): [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md); [B50-C01 · Trazado exacto de rayos y aberraciones de orden superior](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md).

### Trazado óptimo

- Un trazado óptimo es el de menor coste.

💡 **Cómo se explica en la clase [B109-C02](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md):**
- Hay `4` trazados óptimos, un múltiplo de `4` como exige el grupo de simetrías de la cuadrícula (identidad, dos reflejos y un giro de 180°).
- El trazado óptimo deja Dormitorios junto a Higiene y Cocina-mesa, y la Esclusa en la esquina opuesta.
- 🎯 **Por qué importa:** Un buen plano ahorra pasos, separa lo sucio de lo limpio y deja las zonas tranquilas lejos de las ruidosas. La decisión central: ¿dónde pongo cada zona para que los recorridos frecuentes sean cortos y las zonas incompatibles estén lejos?
- 🔗 **Se estudia junto con:** zona, flujo, adyacencia, incompatibilidad.

📘 **Dónde se aprende** (1 clase): [B109-C02 · Zonificación y distribución funcional de módulos de un hábitat](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md).

### Trazador

- Un trazador es una especie fácil de observar que sirve para inferir otra difícil de ver.

💡 **Cómo se explica en la clase [B25-C04](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md):**
- El `H₂` carece de emisión útil a 10 K, y el `CO` es el trazador más usado.
- Piensa en una nube de humo en una habitación: no ves el gas, ves cómo oscurece una lámpara detrás (sombra) o cómo brilla un trazador que añadiste (CO).
- 🎯 **Por qué importa:** El hidrógeno molecular `H₂`, el componente principal de las nubes donde nacen las estrellas, casi no emite en el gas frío. Por eso la masa de una nube se estima con un trazador indirecto, el monóxido de carbono `CO`, y con el polvo que apaga la luz de fondo.
- 🔗 **Se estudia junto con:** nube molecular, intensidad integrada, factor de conversión, masa con helio.

📘 **Dónde se aprende** (1 clase): [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md).

### TRIAD

- El problema de Wahba minimiza `Σ wᵢ |bᵢ − A rᵢ|²` sobre matrices de rotación `A`. TRIAD construye dos ternas ortonormales con dos estrellas.
- El método q halla el autovector de mayor autovalor de la matriz `K` de Davenport. TRIAD construye ternas ortonormales con dos vectores.

💡 **Cómo se explica en la clase [B74-C14](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md):**
- Con dos vectores medidos `b₁, b₂` y sus catálogos `r₁, r₂`, TRIAD toma `b₁` como eje principal y construye la terna con `b₁ × b₂`.
- Con solo dos estrellas, las desviaciones son de `10,1″` (TRIAD) y `12,0″` (SVD), dominadas por pares casi colineales (colas pesadas).
- 🎯 **Por qué importa:** Un error de actitud de unos segundos de arco desplaza a un objeto a un millón de kilómetros por decenas de metros, y un error de giro mayor en el eje óptico es normal. La decisión central: ¿cuántas estrellas y qué campo de visión hacen falta para cada eje de la actitud?
- 🔗 **Se estudia junto con:** problema de Wahba, SVD, giro, campo de visión.

📘 **Dónde se aprende** (2 clases): [B74-C14 · Navegación con cámaras estelares](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md); [B87-C09 · Estimación de actitud](../programa/clases/B87/B87-C09-estimacion-de-actitud/CLASE.md).

### Triage

- Triage es la clasificación de casos por urgencia para decidir el orden y el tipo de atención.

💡 **Cómo se explica en la clase [B116-C04](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md):**
- Sensibilidad `(1132 + 1240 + 1013)/3978 = 0,851`; especificidad `15822/16022 = 0,988`; sub-triage `593/20000 = 2,96 %`.
- El ruido del sensor produce sobre-triage de personas estables, con el coste de alertas y consultas, más que sub-triage.
- 🎯 **Por qué importa:** Un puntaje simple ayuda a decidir rápido y de forma homogénea, pero un fallo por defecto (sub-triage) deja sin atender a quien lo necesita y uno por exceso (sobre-triage) agota recursos y atención. Y si la respuesta de tierra tarda decenas de minutos, no se puede esperar a tierra para lo que no admite espera.
- 🔗 **Se estudia junto con:** puntaje de alerta temprana, categoría, Sub-triage, sobre-triage.

📘 **Dónde se aprende** (1 clase): [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Trial

- El trial es un valor de prueba de DM.

💡 **Contexto en la clase [B29-C17](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md):**
- **Idea central (modelo mental):** Todos los corredores salen a la vez, pero los lentos (baja frecuencia) llegan después. Para ver la salida simultánea hay que adelantar a cada corredor lo que se retrasó: eso es desdispersar.
- 🎯 **Por qué importa:** La medida de dispersión informa de la distancia a la fuente y de la materia que atravesó. Sin desdispersión, un pulso breve se pierde entre canales.
- 🔗 **Se estudia junto con:** dispersión, medida de dispersión, desdispersión, ensanchamiento intra-canal.

📘 **Dónde se aprende** (1 clase): [B29-C17 · Fenómenos transitorios rápidos](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md).

### Triangulación

- La triangulación es la medición de la distancia a un objeto a partir de una base conocida y de los ángulos que forman con ella las visuales desde sus extremos.

💡 **Cómo se explica en la clase [B04-C20](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md):**
- Un plan de triangulación fija: el objeto y su distancia esperada, la base disponible, la precisión angular del instrumento, el error relativo exigido, la base necesaria, la comprobación (simulación o caso conocido), los supuestos (plano, sin error de base, ruido gaussiano) y las fuentes de cada cifra.
- Paso 2 · Comprobar la triangulación. `h = B/(cot A + cot B') = 6000/(2 × 0,007805) = 384 400 km` ✓ (`cot 89,553° = 0,007805`).
- 🎯 **Por qué importa:** Las distancias a las estrellas más cercanas se obtienen con un triángulo (el paralaje de C07): la base es la órbita de la Tierra y el ángulo es lo que cambia la dirección de la estrella.
- 🔗 **Se estudia junto con:** base, altura, incertidumbre angular, propagación de errores.

📘 **Dónde se aprende** (1 clase): [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md).

### Triangular

- Una duración triangular tiene mínimo, moda y máximo.

💡 **Cómo se explica en la clase [B124-C16](../programa/clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md):**
- Con duraciones triangulares (mínimo 0,8 d, moda d, máximo 1,6 d) y 20 000 simulaciones, el plazo medio es `35,43` semanas;
- Simular duraciones triangulares y obtener percentiles del plazo.
- 🎯 **Por qué importa:** Un plazo prometido sin ruta crítica ni incertidumbre es una apuesta. La decisión central: ¿qué actividades controlan el plazo y con qué probabilidad se cumple?
- 🔗 **Se estudia junto con:** ruta crítica, tempranas, tardías, holgura.

📘 **Dónde se aprende** (1 clase): [B124-C16 · Planificación de cronograma y entregables](../programa/clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md).

### Triangulares

- Los colineales L1, L2, L3 están sobre el eje que une los primarios; los triangulares L4 y L5 forman con ellos un triángulo equilátero.

💡 **Contexto en la clase [B73-C03](../programa/clases/B73/B73-C03-puntos-de-equilibrio-de-lagrange/CLASE.md):**
- 🎯 **Por qué importa:** Los puntos de Lagrange son donde se estacionan observatorios y donde se acumulan asteroides troyanos. Un error de signo en la ecuación mueve L2 al otro lado.
- 🔗 **Se estudia junto con:** punto de Lagrange, colineales, aproximación de Hill.

📘 **Dónde se aprende** (1 clase): [B73-C03 · Puntos de equilibrio de Lagrange](../programa/clases/B73/B73-C03-puntos-de-equilibrio-de-lagrange/CLASE.md).

### Triángulo esférico

- Un triángulo esférico está formado por tres arcos de círculo máximo.

💡 **Contexto en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- **Idea central (modelo mental):** Si cortas una naranja por un plano que pasa por su centro, el borde del corte es un círculo máximo; es el más grande que cabe en ella. Entre dos puntos de la cáscara, el camino más corto sobre ella es el arco de ese círculo.
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.
- 🔗 **Se estudia junto con:** esfera, círculo máximo, círculo menor, distancia angular.

📘 **Dónde se aprende** (1 clase): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md).

### Triángulo rectángulo

- En un triángulo rectángulo, el cateto opuesto a un ángulo `θ` es el lado frente a él, el cateto adyacente es el lado que lo forma junto con la hipotenusa, y la hipotenusa es el lado mayor, frente al ángulo recto.
- Un triángulo rectángulo tiene un ángulo de 90°; el lado opuesto a él es la hipotenusa y los otros dos son los catetos.

💡 **Cómo se explica en la clase [B03-C18](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md):**
- Visto desde una distancia `d`, el radio `r` forma un triángulo rectángulo con la visual tangente: `tan(θ/2) = r/d`, luego `θ = 2·atan(r/d)`.
- Definir seno, coseno y tangente como razones de lados en un triángulo rectángulo.
- 🎯 **Por qué importa:** El Sol y la Luna se ven en el cielo con tamaños angulares muy parecidos, de alrededor de medio grado. ¿Es casualidad que midan lo mismo en el cielo siendo tan distintos?
- 🔗 **Se estudia junto con:** cateto opuesto, cateto adyacente, hipotenusa, razones trigonométricas.

📘 **Dónde se aprende** (2 clases): [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md); [B04-C07 · Triángulos y distancias angulares](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md).

### Tridiagonal

- Un sistema tridiagonal solo tiene tres diagonales distintas de cero y se resuelve con el algoritmo de Thomas (eliminación sin pivoteo, `O(N)`).

💡 **Cómo se explica en la clase [B11-C12](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md):**
- C --> D["Sistema tridiagonal<br/>(Thomas)"]
- *Descripción textual:* un BVP se resuelve de dos maneras: con diferencias finitas se plantea una ecuación en cada nodo y se resuelve un sistema tridiagonal; con tiro se prueba una condición inicial, se integra y se corrige según el desvío en el extremo hasta que se anule.
- 🎯 **Por qué importa:** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.
- 🔗 **Se estudia junto con:** problema de frontera, Dirichlet, Neumann, mixtas.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Trigonal plana

- Las formas básicas son lineal (2 dominios, 180°), trigonal plana (3, 120°) y tetraédrica (4, 109,47°).

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- Con 3 sin pares solitarios, trigonal plana (120°).
- D2["2 dominios: lineal, 180°"] --> D3["3 dominios: trigonal plana, 120°"]
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).
- 🔗 **Se estudia junto con:** dominio de electrones, modelo de repulsión de pares de valencia, geometría electrónica, forma molecular.

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### TRIMP

- El rendimiento es aptitud menos fatiga. TRIMP es una carga basada en frecuencia cardiaca.

💡 **Cómo se explica en la clase [B104-C04](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md):**
- Calcular la fracción de reserva de frecuencia cardiaca (Karvonen) y una carga tipo TRIMP.
- Ejercicio 2 · con una pista. Calcula el TRIMP de 30 min a 110 lpm.
- 🎯 **Por qué importa:** Entrenar más no siempre significa rendir más el día que importa. La decisión central: ¿cómo distribuir una misma carga total para llegar con la mejor combinación de aptitud y fatiga?
- 🔗 **Se estudia junto con:** carga, aptitud, fatiga, rendimiento.

📘 **Dónde se aprende** (1 clase): [B104-C04 · Acondicionamiento físico general](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md).

### Triple alfa

- El triple alfa es la fusión `3 ⁴He → ¹²C`, con ayuda del berilio-8 inestable como paso intermedio.

💡 **Cómo se explica en la clase [B24-C08](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md):**
- La energía por kilogramo del triple alfa es `ε c² = 5,85 × 10¹³ J/kg`, frente a `6,40 × 10¹⁴` del hidrógeno.
- Cinética con una ecuación (triple alfa): da la forma de la caída de abundancia.
- ⚠️ **Error frecuente:** Olvidar que el triple alfa es de tres cuerpos. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** El carbono de tu cuerpo, el oxígeno que respiras y el hierro de tus huesos se forjaron en estrellas. Entender cómo, y cuánta energía rinde cada etapa, explica por qué la vida de una estrella se acorta con cada combustible y por qué el hierro es el final de la cadena.
- 🔗 **Se estudia junto con:** nucleosíntesis estelar, partícula alfa, secuencia de quemado, grupo del hierro.

📘 **Dónde se aprende** (1 clase): [B24-C08 · Nucleosíntesis estelar](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md).

### Triplete

- El triplete (`s = 1`) y el singlete (`s = 0`).

💡 **Cómo se explica en la clase [B31-C05](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md):**
- S2["S = S₁ + S₂"] --> T["triplete s=1, singlete s=0"]
- *Descripción textual:* el ángulo da la probabilidad en un analizador; la suma de espines da triplete y singlete; el campo da el desdoblamiento Zeeman y su frecuencia.
- 🎯 **Por qué importa:** El espín explica los desdoblamientos de líneas espectrales y la estructura de la materia. La decisión central: ¿qué probabilidades y qué energías resultan de un espín en un campo?
- 🔗 **Se estudia junto con:** espín, analizador de Stern–Gerlach, singlete, degeneración.

📘 **Dónde se aprende** (1 clase): [B31-C05 · Espín y momento angular](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md).

### Triplete apocromático

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C15](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md):**
- **Idea central (modelo mental):** Como equilibrar una balanza con dos pesas: el crown converge y el flint diverge, los colores extremos se igualan pero queda un resto en el medio; una tercera pesa lo reduce.
- 🎯 **Por qué importa:** Un refractor sin color necesita combinar vidrios. La decisión central: ¿cuánto color queda con dos o tres vidrios?
- 🔗 **Se estudia junto con:** doblete acromático, espectro secundario, potencia, factor de forma.

📘 **Dónde se aprende** (1 clase): [B41-C15 · Refractores acromáticos y apocromáticos](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md).

### Trípode

- La estabilización de imagen o un trípode reducen el temblor.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- NASA recomienda, para empezar, entre 7×35 y 10×50: con más aumento el campo es más estrecho, pesan más y se sacuden, salvo con estabilización o trípode (S2, S3).
- Apoya los codos, o el cuerpo en un muro; a mayor aumento, el temblor se nota más, y NASA sugiere trípode para 10× o 15× en la Luna (S4).
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?
- 🔗 **Se estudia junto con:** aumento, objetivo, pupila de salida, campo de visión.

📘 **Dónde se aprende** (1 clase): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md).

### TRL

- El TRL es el nivel de 1 a 9 de madurez.
- Los TRL (S6): 1 principios básicos; 2 concepto; 3 prueba de concepto; 4 componentes probados; 5 maqueta en entorno relevante; 6 prototipo representativo; 7 prototipo en el espacio; 8 calificado para vuelo; 9 probado en misión.

💡 **Cómo se explica en la clase [B78-C19](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md):**
- El TRL es la longitud de la cadena contigua de hitos desde el 1.
- Un sistema formado por A, B y C tiene componentes `[9, 7, 3]` y TRL `min = 3`; la media daría `6,33`.
- ⚠️ **Error frecuente:** Dar el TRL por el máximo con evidencia. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una tecnología con un buen desempeño en papel puede estar lejos de volar. La decisión central: ¿en qué nivel está una tecnología según la evidencia que tiene, y qué nivel tiene un sistema formado por componentes de madureces distintas?
- 🔗 **Se estudia junto con:** hito de evidencia, cadena contigua, eslabón más débil, entorno relevante.

📘 **Dónde se aprende** (2 clases): [B78-C19 · Madurez tecnológica TRL](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md); [B83-C18 · Niveles de madurez tecnológica](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md).

### TRL del sistema

- El TRL del sistema es el mínimo de sus elementos (S5).

💡 **Cómo se explica en la clase [B83-C18](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md):**
- *Descripción textual:* el TRL declarado pasa por las reglas de herencia e integración y da el TRL efectivo; su mínimo es el del sistema; la brecha frente a PDR/CDR y la dificultad de avance dan el esfuerzo y el plan.
- El TRL del sistema es 4 (el del detector).
- 🎯 **Por qué importa:** Un elemento «con herencia de vuelo» que se usa en otro entorno no es TRL 9. La decisión central: ¿cuál es el TRL real del sistema, qué elementos lo frenan y cuánto cuesta llevarlos al nivel que pide la revisión?
- 🔗 **Se estudia junto con:** TRL, herencia, AD2, evaluación de madurez.

📘 **Dónde se aprende** (1 clase): [B83-C18 · Niveles de madurez tecnológica](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md).

### Tropopausa

- La tropopausa es el techo de la capa donde `T` desciende con la altura.

💡 **Cómo se explica en la clase [B54-C01](../programa/clases/B54/B54-C01-estructura-vertical-de-atmosferas/CLASE.md):**
- La temperatura baja hasta `216,65 K` a 11 km (la tropopausa del modelo), sube con el gradiente positivo de las capas superiores hasta `270,65 K` a 47 km y vuelve a bajar.
- Identificar la tropopausa y el máximo y mínimo de temperatura de un perfil por capas.
- 🎯 **Por qué importa:** Todo lo que sigue en el bloque (balance de energía, convección, nubes, escape) ocurre en una columna de gas con una presión y una temperatura que dependen de la altura. La pregunta motivadora: ¿cómo cae la presión con la altura cuando la temperatura también cambia?
- 🔗 **Se estudia junto con:** equilibrio hidrostático, altura de escala, gradiente de temperatura, capa isoterma.

📘 **Dónde se aprende** (1 clase): [B54-C01 · Estructura vertical de atmósferas](../programa/clases/B54/B54-C01-estructura-vertical-de-atmosferas/CLASE.md).

### Trozo

- Un trozo (*chunk*) es una porción independiente de trabajo.
- SHA-256: hash de 256 bits. Trozo: unidad de transferencia.

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Con cuatro procesos no hubo ganancia. No es un fallo: en Windows el método de arranque es `spawn` (S1), cada trabajador es un intérprete nuevo que debe importar NumPy, y ese arranque cuesta una fracción de segundo por proceso, del orden del trabajo útil de cada trozo.
- Con trozos de 50 000 puntos, la versión serie tardó 25,2 ms y la de dos procesos 1682 ms: aceleración de 0,015 (la paralela fue 67 veces más lenta).
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.
- 🔗 **Se estudia junto con:** proceso, hilo, GIL, trabajador.

📘 **Dónde se aprende** (2 clases): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md); [B96-C22 · Transferencia de datos entre estación y centro de datos](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md).

### TRR

- La TRR revisa la preparación de cada ensayo.

💡 **Cómo se explica en la clase [B83-C14](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md):**
- La TRR de los ensayos requeridos no está lista hasta resolver E3 y E4.
- *Descripción textual:* cada requisito recibe un método; los de ensayo se asocian a un ensayo con su lista de preparación y su veredicto de TRR; si es de vibración, el perfil se integra para dar los niveles de carga.
- ⚠️ **Error frecuente:** Convocar la TRR sin la lista. Verifica las cinco condiciones
- 🎯 **Por qué importa:** Un ensayo mal preparado destruye hardware o no demuestra nada. La decisión central: ¿cada requisito tiene un método asignado, y cada ensayo está listo (procedimiento, equipo, configuración, personal e instalación) y con un nivel de carga definido?
- 🔗 **Se estudia junto con:** matriz de verificación, CDR, vibración aleatoria, Grms.

📘 **Dónde se aprende** (1 clase): [B83-C14 · Revisiones CDR y TRR](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md).

### Truncada

- Una distribución es truncada si tiene tamaños mínimo y máximo.

💡 **Cómo se explica en la clase [B52-C13](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md):**
- Definir una distribución acumulada de ley de potencias truncada.
- 🎯 **Por qué importa:** Cómo se reparte la masa entre tamaños indica qué cuerpos dominan una población y qué mide un censo incompleto. La decisión central: ¿cómo se estima el exponente de una ley de potencias y qué tan fiable es la masa que implica?
- 🔗 **Se estudia junto con:** ley de potencias, transformada inversa, estimador de máxima verosimilitud, fracción de masa.

📘 **Dónde se aprende** (1 clase): [B52-C13 · Pequeños cuerpos remanentes](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md).

### Tubo

- El tubo sostiene el detector respecto del espejo.

💡 **Cómo se explica en la clase [B50-C12](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md):**
- Un espejo y un tubo del mismo material (homólogo) no se desenfocan.
- E["espejo α_m y tubo α_t"] --> D2["defocus = f ΔT (α_m − α_t)"]
- 🎯 **Por qué importa:** Un telescopio que se enfría de noche se desenfoca si sus materiales se dilatan distinto. La decisión central: ¿qué dilatación debe tener la estructura para que el foco no se mueva?
- 🔗 **Se estudia junto con:** coeficiente térmico de la focal, carcasa atérmica, defocus, profundidad de foco.

📘 **Dónde se aprende** (1 clase): [B50-C12 · Sensibilidad térmica del desempeño óptico y atermalización](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md).

### Tubo de flujo

- Un tubo de flujo es un haz de líneas de campo.

💡 **Contexto en la clase [B30-C05](../programa/clases/B30/B30-C05-campos-magneticos-solares/CLASE.md):**
- **Idea central (modelo mental):** Las líneas de campo son bandas elásticas: en un fluido denso (β grande) el gas las arrastra; en un gas muy tenue (β pequeño) las bandas mandan y el gas sigue su forma.
- 🎯 **Por qué importa:** Que el gas domine al campo en la fotosfera y el campo al gas en la corona explica por qué la corona se estructura en lazos y por qué las erupciones liberan energía magnética. La decisión central: ¿en qué capa manda el campo y cuánta energía guarda?
- 🔗 **Se estudia junto con:** beta del plasma, velocidad de Alfvén, conservación del flujo, densidad de energía magnética.

📘 **Dónde se aprende** (2 clases): [B30-C05 · Campos magnéticos solares](../programa/clases/B30/B30-C05-campos-magneticos-solares/CLASE.md); [B34-C03 · Bucles magnéticos coronales](../programa/clases/B34/B34-C03-bucles-magneticos-coronales/CLASE.md).

### Tubo delgado

- El tubo delgado `I = π r³ t`.

💡 **Cómo se explica en la clase [B43-C10](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md):**
- Calcular el momento de inercia de un tubo delgado `π r³ t`.
- 🎯 **Por qué importa:** Lo que decolima no es la flexión sino la flexión diferencial entre primario y secundario. La decisión central: ¿qué rigideces hacen que los dos extremos se muevan lo mismo, de modo que el eje óptico solo se desplace en paralelo?
- 🔗 **Se estudia junto con:** cercha Serrurier, rigidez a flexión, flecha de voladizo, descentrado diferencial.

📘 **Dónde se aprende** (1 clase): [B43-C10 · Estructura de tubo óptico](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md).

### Tubo testigo

- Un tubo testigo (*witness tube*) es un tubo que registra contaminación de la propia nave.

💡 **Cómo se explica en la clase [B63-C02](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md):**
- Como contexto real, NASA describe (S4) que Perseverance perfora un testigo con una broca, que un brazo interior lo mueve a estaciones de inspección y sellado, que lo guarda sellado y que puede dejarlo en un depósito de muestras en superficie; también lleva tubos «testigo» (*witness tubes*) que capturan contaminantes terrestres.
- La fuente da 43 tubos y 5 tubos testigo, aunque un pie de foto menciona 39; por esa inconsistencia no se usa ninguna cifra para el cálculo.
- 🎯 **Por qué importa:** Un rover tiene un número limitado de tubos. La decisión central: ¿cuántas muestras hacen falta para no perderse una litología rara con una confianza dada?
- 🔗 **Se estudia junto con:** testigo, litología, fracción de área, confianza.

📘 **Dónde se aprende** (1 clase): [B63-C02 · Muestreo superficial y estrategias de recolección](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md).

### Tupla

- Una tupla es una secuencia ordenada e inmutable, entre paréntesis (S3).

💡 **Cómo se explica en la clase [B07-C07](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md):**
- Una tupla `(nombre, valor)` no se puede modificar.
- Una tupla de un elemento necesita coma final: `(5,)` es tupla, `(5)` es el entero 5.
- 🎯 **Por qué importa:** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.
- 🔗 **Se estudia junto con:** lista, inmutable, diccionario, conjunto.

📘 **Dónde se aprende** (1 clase): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md).

### Turbulento

- El flujo es laminar si las capas no se mezclan y turbulento si hay mezcla caótica.

💡 **Cómo se explica en la clase [B79-C04](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md):**
- Con `Re_L = 2 × 10⁶` el `C_f` turbulento es `4,33` veces el laminar.
- El régimen turbulento tiene más fricción (en placa, `C_f` mayor y decae más despacio con `Re`) pero también retrasa el desprendimiento.
- ⚠️ **Error frecuente:** Usar `f = 64/Re` en régimen turbulento. Se corrige con 8.1.
- 🎯 **Por qué importa:** El régimen cambia el arrastre y la transferencia de calor por factores de varios; no distinguirlo lleva a subestimar el calentamiento de una pared o la pérdida de presión de un conducto. El tronco no lo trata.
- 🔗 **Se estudia junto con:** número de Reynolds, laminar, factor de fricción de Darcy, coeficiente de arrastre.

📘 **Dónde se aprende** (1 clase): [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md).

### Turno

- Horas efectivas: jornada menos ausencias. Turno: bloque de 8 h.

💡 **Cómo se explica en la clase [B96-C03](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md):**
- Con 21 turnos semanales y 6 personas se asignan por turno y en rotación.
- Cada hora de la semana (168) se cubre exactamente una vez; ninguna persona tiene dos turnos contiguos y el máximo es de 4 turnos (32 h), dentro de las 40 h.
- 🎯 **Por qué importa:** Un rol vacío durante un contacto es un contacto perdido. La decisión central: ¿cuánto personal exige cubrir una posición 24/7 y cómo se comprueba que el cronograma no deja huecos?
- 🔗 **Se estudia junto con:** Posición, Cobertura 24/7, Horas efectivas, Equivalente a tiempo completo (ETC).

📘 **Dónde se aprende** (1 clase): [B96-C03 · Roles de control de misión](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md).
