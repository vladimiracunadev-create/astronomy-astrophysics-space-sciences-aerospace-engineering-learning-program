# Términos · W

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · **W** · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### WAIC

- LOO: `elpd_loo = Σ_i log p(y_i | y_{−i})`. WAIC: `elpd_waic = lppd − p_waic`, con `lppd = Σ_i log E_post[p(y_i | θ)]` y `p_waic = Σ_i Var_post[log p(y_i | θ)]`, la penalización por complejidad efectiva.

💡 **Cómo se explica en la clase [B19-C07](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md):**
- LOO/WAIC responden «¿qué modelo predecirá mejor datos nuevos?»; son menos sensibles al prior y adecuadas para elegir con fines predictivos (S2).
- LOO y WAIC miran hacia adelante: «con lo aprendido de estos datos, ¿cómo predice un dato nuevo?».
- 🎯 **Por qué importa:** Miras 10 mediciones de la amplitud de una señal y el promedio es 0,57 con ruido conocido 1. ¿Hay señal (`μ ≠ 0`) o solo ruido (`μ = 0`)?

📘 **Dónde se aprende** (1 clase): [B19-C07 · Comparación de modelos bayesianos](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md).

### Walker-delta

- Una Walker-delta reparte los satélites en planos igualmente espaciados en la ascensión recta.

💡 **Cómo se explica en la clase [B118-C15](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md):**
- Generar una constelación Walker-delta `P/S/F` y propagarla con Kepler.
- Constelacion SINTETICA Walker-delta 24 x 22 (528 satelites), inclinacion 53 deg, 550 km; fases con error de +-3 deg (semilla 118).
- 🎯 **Por qué importa:** La sección 5.5 de la IADC Rev. 4 pide planificar y operar las constelaciones para minimizar la probabilidad de colisión entre sus miembros, en los cruces de planos y con otras constelaciones, y minimizar el riesgo acumulado de reentradas.

📘 **Dónde se aprende** (1 clase): [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md).

### Watchdog simple

- El watchdog simple reinicia si pasa demasiado tiempo sin patada.

🎯 **Por qué importa (clase B88-C11):** Un watchdog mal ajustado reinicia sin necesidad o no reinicia cuando hace falta. La decisión central: ¿qué ventana y qué escalera de acciones recuperan un software colgado sin reinicios falsos?

📘 **Dónde se aprende** (1 clase): [B88-C11 · Watchdogs y recuperación](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md).

### WCET

- El WCET es la cota superior.

💡 **Cómo se explica en la clase [B88-C30](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md):**
- Analogía: el WCET es como el tiempo del viaje más lento posible con todos los semáforos en rojo: puede no ocurrir nunca, pero el horario se arma con él.
- Calcular el WCET como camino más largo con cotas de bucle.
- ⚠️ **Error frecuente:** Medir y llamar WCET al máximo. Una cota se calcula (8.1)
- 🎯 **Por qué importa:** El análisis de planificación (C05) necesita `C` de cada tarea, y medir no basta porque el peor camino puede no ejercitarse. La decisión central: ¿cuál es una cota segura del tiempo de ejecución y cuánto pesimismo trae?

📘 **Dónde se aprende** (1 clase): [B88-C30 · Análisis de peor caso de tiempo de ejecución (WCET)](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md).

### WCS

- Una WCS (*World Coordinate System*) asocia píxeles con coordenadas del cielo mediante palabras clave como `CRPIX`, `CRVAL`, `CDELT` y `CTYPE`.

💡 **Cómo se explica en la clase [B14-C06](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md):**
- Para el campo pequeño del ejemplo, la WCS es: `CRPIX = (33, 25)` (píxel de referencia, numerado desde 1), `CRVAL = (150°, 2°)` (coordenadas del cielo de ese píxel), `CDELT = (−1″, +1″)` expresadas en grados, `CTYPE = RA---TAN, DEC--TAN`.
- (No consulté el estándar de WCS: lo uso como convención y verifico su resultado, ver sección 11.)
- 🎯 **Por qué importa:** Una imagen astronómica es una matriz de números, pero esos números no significan nada sin su encabezado: ¿qué unidad tienen?, ¿cuánto duró la exposición?, ¿a qué punto del cielo apunta el píxel central? Si el encabezado miente o se pierde, la imagen no sirve.

📘 **Dónde se aprende** (1 clase): [B14-C06 · Formato FITS y encabezados](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md).

### WebVTT

- La audiodescripción narra lo visual. WebVTT es el formato web común de subtítulos.

💡 **Cómo se explica en la clase [B128-C05](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md):**
- Leer un archivo WebVTT y calcular la velocidad de lectura de cada bloque.
- El script [subtitulos.py](subtitulos.py) analiza un WebVTT sintético y calcula el WER por programación dinámica (comprueba contra una recursión con memoria y una hipótesis idéntica).
- 🎯 **Por qué importa:** Un subtítulo mal sincronizado o demasiado rápido no se alcanza a leer, y una transcripción automática sin revisar puede decir lo contrario de lo dicho. La decisión central: ¿cómo compruebo que los subtítulos se pueden leer y que no cambian el sentido?

📘 **Dónde se aprende** (1 clase): [B128-C05 · Subtítulos y transcripciones](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md).

### Weibull

- La tasa de fallo es la probabilidad de fallar por unidad de tiempo. Weibull es una familia de distribuciones con forma `β` y escala `η`.
- Confiabilidad `R(t)`: probabilidad de sobrevivir hasta `t`. Weibull: distribución de vida con forma `β` y escala `η`.
- La curva de Weibull `σ(L) = σ_sat(1 − exp(−((L − L₀)/W)^s))`.

💡 **Cómo se explica en la clase [B48-C14](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md):**
- Con vida Weibull de forma 2,5 y escala 1000 h, costo preventivo 1 y costo por falla 10, el reemplazo óptimo está en 354,6 h con costo 0,004751 por hora, frente a 0,011271 sin prevención: ahorro de 57,9 %.
- 🎯 **Por qué importa:** Reemplazar muy pronto desperdicia vida útil; muy tarde, produce fallas caras. La decisión central: ¿cada cuántas horas conviene reemplazar?

📘 **Dónde se aprende** (3 clases): [B48-C14 · Mantenimiento preventivo](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md); [B88-C03 · Procesadores tolerantes a radiación](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md); [B127-C02 · Seguros en órbita](../programa/clases/B127/B127-C02-seguros-en-orbita/CLASE.md).

### WER

- El WER es `(S + D + I)/N`: sustituciones, borrados e inserciones sobre las palabras de referencia.

💡 **Cómo se explica en la clase [B128-C05](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md):**
- Con referencia de 12 palabras y una hipótesis sin «no»: `D = 1`, `WER = 1/12 = 8,3 %`.
- Un WER pequeño puede ocultar un error que invierte el sentido.
- 🎯 **Por qué importa:** Un subtítulo mal sincronizado o demasiado rápido no se alcanza a leer, y una transcripción automática sin revisar puede decir lo contrario de lo dicho. La decisión central: ¿cómo compruebo que los subtítulos se pueden leer y que no cambian el sentido?

📘 **Dónde se aprende** (1 clase): [B128-C05 · Subtítulos y transcripciones](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md).

### Windup

- El windup es el crecimiento excesivo del estado integral cuando el actuador está saturado, porque la integral sigue acumulando error.

💡 **Cómo se explica en la clase [B16-C18](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md):**
- Sin anti-windup, `ξ̇ = e` todo el tiempo, también durante la saturación.
- Resultado: la integral máxima es 0,099 rad·s (frente a 5,29), el sobreimpulso baja a 0,8 % y el asentamiento (2 %) a 40,9 s (frente a 61,9 s sin anti-windup).
- ⚠️ **Error frecuente:** Medir el anti-windup solo en el caso saturado. Se corrige con el ejercicio 6 y la sección 8.4.
- 🎯 **Por qué importa:** Una rueda de reacción entrega un par máximo y almacena un momento angular máximo (el Hubble usa ruedas de hasta unas 3000 rpm, y magnetopares para gestionar su velocidad, S1). Cuando el controlador pide más de lo que el actuador puede dar, el lazo deja de comportarse como se diseñó.

📘 **Dónde se aprende** (1 clase): [B16-C18 · Saturación y anti-windup](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md).

### WRT

- El RTO es el tiempo objetivo para restablecer el servicio; el WRT es el tiempo adicional para recuperar el trabajo; el MTD es el tiempo máximo tolerable de interrupción.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- *Descripción textual:* desde el fallo corren el RTO y el WRT, cuya suma no debe pasar del MTD, mientras el costo crece; el RPO limita el intervalo entre copias.
- Analogía: un grifo roto que inunda más cada minuto: arreglarlo (RTO) y secar (WRT) debe caber antes del daño inaceptable (MTD).
- ⚠️ **Error frecuente:** Olvidar el WRT. Se corrige con 8.2.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?

📘 **Dónde se aprende** (1 clase): [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### WVR

- TML (*total mass loss*) es la pérdida total de masa; WVR, el vapor de agua recuperado;

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- A["pesadas mi, mf, mh, dc"] --> B["TML, WVR, RML, CVCM"]
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?

📘 **Dónde se aprende** (1 clase): [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md).
