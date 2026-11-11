# Términos · Z

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · **Z** · [0-9](terminos-0-9.md)

### Z

- En astronomía, X es la fracción en masa del hidrógeno, Y la del helio y Z la de todo lo demás, llamado en bloque «metales» aunque incluya carbono, nitrógeno y oxígeno (S1).

🎯 **Por qué importa (clase B06-C02):** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?

📘 **Dónde se aprende** (1 clase): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md).

### ZHR

- La ZHR (*zenithal hourly rate*) es el número de meteoros de la lluvia por hora que vería un observador con magnitud límite 6,5 y el radiante en el cenit (S3).
- La ZHR es la tasa horaria cenital: recuentos por hora bajo cielo ideal (`lm = 6,5`) y con el radiante en el cenit.

💡 **Cómo se explica en la clase [B08-C18](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md):**
- La página consultada no da radiantes ni ZHR, y tiene una incoherencia interna en el período de las Alfa Capricórnidas, por lo que su detalle no se reproduce aquí.
- De la definición de ZHR (S3) se deduce, bajo supuestos declarados, que `ZHR = N · r^(6,5 − lm) / (T · sen h · (1 − c))`, donde `N` es el número de meteoros de la lluvia en `T` horas, `lm` la magnitud límite, `r` el índice de población (aquí 2,5, valor de ejemplo), `h` la altura del radiante y `c` la fracción de cielo cubierta por nubes.
- 🎯 **Por qué importa:** Cada año, titulares prometen «cientos de estrellas fugaces por hora». Con un cielo contaminado o con el radiante bajo el horizonte, verás muy pocas.

📘 **Dónde se aprende** (2 clases): [B08-C18 · Introducción a meteoros y lluvias](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md); [B129-C03 · Seguimiento ciudadano de meteoros](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md).

### Zij

- Un zij es una tabla astronómica de la tradición islámica.

💡 **Cómo se explica en la clase [B02-C04](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md):**
- El *Zij-i Ilkhani*, escrito primero en persa y luego traducido al árabe, se basó en unos 12 años de observaciones y contiene tablas para calcular posiciones planetarias y un catálogo de estrellas (S5).
- T["Texto de método: zij,<br/>calendarios"] --> W["Uso actual:<br/>historia de modelos"]
- 🎯 **Por qué importa:** Contar la historia de la astronomía como una línea recta de Grecia a Europa deja fuera lo que otras sociedades observaron, calcularon y construyeron. La pregunta motivadora es: ¿qué sabemos con precisión de estas tradiciones, qué falta y cómo evitar contar la historia desde un solo lado?

📘 **Dónde se aprende** (1 clase): [B02-C04 · Astronomía de India, China y mundo islámico](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md).

### ZNCC

- SSD: suma de diferencias al cuadrado. ZNCC: correlación normalizada de media cero.

💡 **Cómo se explica en la clase [B99-C07](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md):**
- Con cambio de ganancia `g` y sesgo `b` (`I → gI + b`) la ZNCC no cambia, y la SSD sí.
- En el laboratorio (100 parches de `11×11`, ruido de 4 niveles): a contraste 40 y sin cambio ambos aciertan 100 %; con `g = 1,5` y `b = 25` la SSD baja a 80 % y a 4 % con contraste 10, mientras la ZNCC mantiene 100 %.
- ⚠️ **Error frecuente:** Confiar en ZNCC cuando el contraste es menor que el ruido. A contraste 1 el acierto cae a 55 % (8.4).
- 🎯 **Por qué importa:** Un estimador que funciona en el laboratorio puede fallar sin avisar cuando el entorno empeora. La decisión central: ¿qué estimador usar, cómo detectar que el entorno no determina el movimiento y cuándo dejar de confiar en el mapa?

📘 **Dónde se aprende** (1 clase): [B99-C07 · Robustez del mapeo ante entornos degradados](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md).

### Zona

- Una zona agrupa funciones que comparten espacio.

💡 **Cómo se explica en la clase [B109-C02](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md):**
- Por área: m² por zona frente al mínimo recomendado.
- 🎯 **Por qué importa:** Un buen plano ahorra pasos, separa lo sucio de lo limpio y deja las zonas tranquilas lejos de las ruidosas. La decisión central: ¿dónde pongo cada zona para que los recorridos frecuentes sean cortos y las zonas incompatibles estén lejos?

📘 **Dónde se aprende** (1 clase): [B109-C02 · Zonificación y distribución funcional de módulos de un hábitat](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md).

### Zona ciega

- La zona ciega del cenit es donde la velocidad de acimut supera el máximo del motor.

💡 **Cómo se explica en la clase [B43-C13](../programa/clases/B43/B43-C13-montura-altacimutal/CLASE.md):**
- Con un máximo de `1°/s` en acimut, la zona ciega del cenit tiene radio `0,207°`.
- 🎯 **Por qué importa:** La altacimutal reemplaza un giro uniforme por dos giros variables y un ángulo de campo que cambia. La decisión central: ¿qué velocidades exigen los motores, cuánto rota el campo y qué región del cielo no se puede seguir?

📘 **Dónde se aprende** (1 clase): [B43-C13 · Montura altacimutal](../programa/clases/B43/B43-C13-montura-altacimutal/CLASE.md).

### Zona de alimentación

- La zona de alimentación es la franja del disco de la que un embrión toma material, de ancho `b` en radios de Hill.

🎯 **Por qué importa (clase B52-C05):** El tiempo de crecimiento decide si un núcleo existe antes de que el gas se disipe. La decisión central: ¿cómo cambia la tasa de acreción con la masa y cuándo se detiene?

📘 **Dónde se aprende** (1 clase): [B52-C05 · Crecimiento de embriones planetarios](../programa/clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md).

### Zona de coordinación

- La zona de coordinación es el área dentro de la cual hay que coordinar.

🎯 **Por qué importa (clase B120-C02):** Coordinar con otros servicios define dónde y cómo se puede operar y ninguna clase lo trata. La decisión central: ¿con qué administraciones hay que coordinar una estación terrena y en cuánto tiempo deben responder?

📘 **Dónde se aprende** (1 clase): [B120-C02 · Zonas de coordinación entre servicios radioeléctricos](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md).

### Zona de desempeño

- Zona de salud: intervalo de temperatura y humedad que protege la salud; zona de desempeño: el más estrecho en el que el trabajo rutinario no se degrada por estrés térmico.

🎯 **Por qué importa (clase B106-C01):** Un hábitat se diseña de adentro hacia afuera: primero lo que consume y emite la tripulación, después la máquina que lo repone. Si el balance humano está mal, todo el ECLSS queda mal dimensionado.

📘 **Dónde se aprende** (1 clase): [B106-C01 · Requisitos de habitabilidad](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md).

### Zona de dispersión

- La zona de dispersión es el área de caída posible.

🎯 **Por qué importa (clase B118-C14):** El riesgo en superficie se controla antes de lanzar: limitando los fragmentos que sobreviven o confinando la reentrada a zonas despobladas. La decisión central: ¿cuánta área de víctima se puede aceptar para respetar 10⁻⁴ y cómo influye dónde cae?

📘 **Dónde se aprende** (1 clase): [B118-C14 · Reentrada y riesgos en superficie](../programa/clases/B118/B118-C14-reentrada-y-riesgos-en-superficie/CLASE.md).

### Zona de exclusión

- La zona de exclusión es el área cerrada a terceros durante el lanzamiento.
- La zona de exclusión es una distancia que no se cruza sin coordinación.

💡 **Cómo se explica en la clase [B119-C28](../programa/clases/B119/B119-C28-normas-de-comportamiento-responsable-en-el-espacio/CLASE.md):**
- Una geometría sin deriva es previsible, pero cruzar una zona de exclusión sin avisar puede percibirse como amenaza; por eso el deber de consulta del art.
- *Descripción textual:* la órbita de referencia y las condiciones iniciales determinan la distancia relativa en el tiempo; se compara con una zona de exclusión para decidir si hace falta coordinar.
- 🎯 **Por qué importa:** B119-C11 trata límites militares; las normas voluntarias de conducta responsable no tienen clase y se apoyan en conceptos físicos (distancia relativa, deriva, previsibilidad) que esta clase muestra. La decisión central: ¿qué condiciones iniciales mantienen al vecino a distancia constante y cuáles lo hacen derivar o acercarse?

📘 **Dónde se aprende** (2 clases): [B119-C22 · Seguridad de instalaciones y operaciones de sitio de lanzamiento](../programa/clases/B119/B119-C22-seguridad-de-instalaciones-y-operaciones-de-sitio-de-lanzamiento/CLASE.md); [B119-C28 · Normas de comportamiento responsable en el espacio](../programa/clases/B119/B119-C28-normas-de-comportamiento-responsable-en-el-espacio/CLASE.md).

### Zona de impacto

- La zona de impacto es la distribución de dónde caen los escombros.
- La zona de impacto es un área donde pueden caer fragmentos.

🎯 **Por qué importa (clase B77-C19):** Mover el sitio de impacto un par de decenas de kilómetros cambia el riesgo en un factor de varios. La decisión central: ¿cómo se calculan las víctimas esperadas y cuánto depende de dónde cae lo que cae?

📘 **Dónde se aprende** (2 clases): [B77-C19 · Seguridad de rango a nivel conceptual](../programa/clases/B77/B77-C19-seguridad-de-rango-a-nivel-conceptual/CLASE.md); [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md).

### Zona de salud

- Normoxia: oxígeno suficiente sin exceso. Zona de salud: intervalo de temperatura y humedad que protege la salud;

🎯 **Por qué importa (clase B106-C01):** Un hábitat se diseña de adentro hacia afuera: primero lo que consume y emite la tripulación, después la máquina que lo repone. Si el balance humano está mal, todo el ECLSS queda mal dimensionado.

📘 **Dónde se aprende** (1 clase): [B106-C01 · Requisitos de habitabilidad](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md).

### Zona de seguridad

- La zona de seguridad es el área alrededor de una instalación.

💡 **Cómo se explica en la clase [B119-C05](../programa/clases/B119/B119-C05-acuerdo-sobre-la-luna-y-alcance/CLASE.md):**
- El ejemplo conductor: 12 instalaciones sintéticas con zona de seguridad de 5 km y cinco Estados genéricos con contribuciones 0,40; 0,25; 0,15; 0,12 y 0,08.
- 🎯 **Por qué importa:** La clase C01 establece la no apropiación; este acuerdo la aplica a los recursos y es la base de los debates de C25 y C36. La decisión central: ¿cómo se compara lo que ocupan las instalaciones con la superficie total y qué regla de reparto da un resultado más equitativo?

📘 **Dónde se aprende** (1 clase): [B119-C05 · Acuerdo sobre la Luna y alcance](../programa/clases/B119/B119-C05-acuerdo-sobre-la-luna-y-alcance/CLASE.md).

### Zona habitable

- La zona habitable es la región con agua líquida posible.
- La zona habitable es un intervalo de distancias o instalaciones.
- La zona habitable es un intervalo que depende del modelo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B29-C13](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md):**
- Una `T_eq` entre `273` y `373 K` no define la zona habitable porque ignora el invernadero y el ciclo del carbono: en el Sol da `0,47–0,87 au`, bastante más cerca de lo que dan los modelos climáticos.
- 🎯 **Por qué importa:** La temperatura de equilibrio es la primera estimación de si un mundo es cálido o helado, pero no es la temperatura de la superficie: depende del albedo y del efecto invernadero. La decisión central: ¿a qué distancias una estrella da una temperatura de equilibrio dada y cuánto cambia con el albedo?

📖 **Explicado a fondo:** [Habitabilidad y zona habitable](esencial/esencial-d-l.md#habitabilidad-y-zona-habitable) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B29-C13 · Zonas de habitabilidad](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md); [B54-C17 · Clima exoplanetario](../programa/clases/B54/B54-C17-clima-exoplanetario/CLASE.md); [B54-C20 · Comparación de habitabilidad climática](../programa/clases/B54/B54-C20-comparacion-de-habitabilidad-climatica/CLASE.md); [B56-C12 · Exoplanetas potencialmente habitables](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md).

### Zona libre de campo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C08](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md):**
- Límite: campo uniforme, zona libre de campo.
- 🎯 **Por qué importa:** La resolución de masa decide qué especies se separan. La decisión central: ¿qué tiempo de vuelo, qué dispersión y qué resolución permiten distinguir dos iones casi isobáricos?

📘 **Dónde se aprende** (1 clase): [B47-C08 · Espectrómetros de masas orbitales](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md).

### Zona muerta

- La zona muerta anula el par pequeño (aquí representa la holgura).

💡 **Cómo se explica en la clase [B97-C24](../programa/clases/B97/B97-C24-modelos-de-actuadores-virtuales-e-integracion-en-simulacion/CLASE.md):**
- Con zona muerta de `±1 N·m`, el sobreimpulso es `0,3971` y queda un error final de `0,00616` rad (por debajo de la cota `zona/Kp = 0,020` rad).
- *Descripción textual:* el controlador envía un par que pasa por retardo, saturación y zona muerta antes de llegar a la planta; la salida se mide en sobreimpulso, establecimiento y error final.
- ⚠️ **Error frecuente:** Llamar «juego» a la zona muerta. Es una simplificación (ver los límites)
- 🎯 **Por qué importa:** Un controlador que funciona en simulación con un actuador ideal puede oscilar o no llegar al objetivo con uno real. Conocer qué efecto causa cada fenómeno evita sorpresas al integrar el control con el hardware.

📘 **Dónde se aprende** (1 clase): [B97-C24 · Modelos de actuadores virtuales e integración en simulación](../programa/clases/B97/B97-C24-modelos-de-actuadores-virtuales-e-integracion-en-simulacion/CLASE.md).

### Zona protegida contra ESD

- Falla latente: daño que no se manifiesta hasta después. Zona protegida contra ESD: área con control de carga (superficies disipativas, puesta a tierra, ropa).

🎯 **Por qué importa (clase B90-C03):** Un componente electrónico puede quedar con una falla latente tras una descarga que nadie sintió: una persona percibe una chispa solo por encima de unos miles de voltios (orden de magnitud no consultado), por encima de lo que puede dañar a un componente sensible.

📘 **Dónde se aprende** (1 clase): [B90-C03 · Protección frente a ESD](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md).

### Zonas de sombra permanente

- Las zonas de sombra permanente son regiones polares que no reciben luz solar directa;

🎯 **Por qué importa (clase B59-C02):** Un recurso no se planifica con un valor central sino con un rango. La decisión central: ¿cuánto regolito hay que procesar si la abundancia es 2,7 % en vez de 5,6 %?

📘 **Dónde se aprende** (1 clase): [B59-C02 · Prospección de hielo lunar](../programa/clases/B59/B59-C02-prospeccion-de-hielo-lunar/CLASE.md).
