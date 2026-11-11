# Términos · P (parte 4 de 4)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · **P** · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-p.md) · [2](terminos-p-2.md) · [3](terminos-p-3.md) · **4**

### Puntuación de mutantes

- La puntuación de mutantes es la fracción de muertos.

💡 **Cómo se explica en la clase [B94-C06](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md):**
- La evidencia es la matriz de trazabilidad requisito–prueba con puntuación de mutantes del ejercicio 12 (sección 20).
- Ejercicio 10 · transferencia. Transferencia. ¿Basta una puntuación de mutantes del 100 % para declarar conformidad?
- 🎯 **Por qué importa:** Una implementación que «funciona con la mía» puede fallar con otra. La decisión central: ¿qué pruebas demuestran que cada requisito se cumple y cómo sabes que tu suite detectaría un defecto?
- 🔗 **Se estudia junto con:** conformidad, implementación bajo prueba, vector de prueba, oráculo.

📘 **Dónde se aprende** (1 clase): [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Puntuación robusta

- Límite fijo: umbral de 3σ. Puntuación robusta: desvío en unidades de MAD.

💡 **Cómo se explica en la clase [B96-C13](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md):**
- La puntuación robusta se adapta a la deriva porque la ventana la absorbe: ve picos, no cambios lentos.
- La puntuación robusta no ve la deriva (la ventana se adapta) y CUSUM la ve en 7 muestras, con 5 falsas alarmas.
- 🎯 **Por qué importa:** Un detector que no ve una deriva lenta avisa cuando ya es tarde, y uno que alarma por todo se ignora. La decisión central: ¿qué detector ve cada tipo de anomalía, con qué retraso y a qué costo en falsas alarmas?
- 🔗 **Se estudia junto con:** Anomalía, Límite fijo, CUSUM, Falsa alarma.

📘 **Dónde se aprende** (1 clase): [B96-C13 · Detección de anomalías](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md).

### Puntuación tipo SAGAT

- Una puntuación tipo SAGAT congela una simulación y pregunta por cada nivel; aquí se simula, no se mide.

💡 **Contexto en la clase [B111-C04](../programa/clases/B111/B111-C04-conciencia-situacional-en-operaciones-de-vuelo/CLASE.md):**
- 🎯 **Por qué importa:** Falta la clase que trate la conciencia situacional de la tripulación. La decisión central: ¿cómo se cuantifica lo que el equipo sabe y cada cuánto debe verificarlo para que no se quede desactualizado?
- 🔗 **Se estudia junto con:** conciencia situacional, percepción, comprensión, proyección.

📘 **Dónde se aprende** (1 clase): [B111-C04 · Conciencia situacional en operaciones de vuelo](../programa/clases/B111/B111-C04-conciencia-situacional-en-operaciones-de-vuelo/CLASE.md).

### Puntuación z

- La puntuación z estandariza la serie.

💡 **Contexto en la clase [B105-C09](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md):**
- 🎯 **Por qué importa:** Un umbral bajo detecta pronto pero alarma de más; uno alto alarma poco pero tarda. Con una tripulación pequeña, las falsas alarmas se acumulan.
- 🔗 **Se estudia junto con:** línea base personal, CUSUM, tasa de falsas alarmas, retraso.

📘 **Dónde se aprende** (1 clase): [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md).

### Pupila

- La pupila `P(x)`.

💡 **Cómo se explica en la clase [B42-C06](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md):**
- La pupila tiene `812` píxeles (disco ideal `804,2`); el pico sin aberración vale `659 344 = 812²`.
- Una inclinación de 5 ciclos por pupila mueve el pico de la columna 0 a la 5 sin cambiar su valor (`1,000000`).
- 🎯 **Por qué importa:** Toda imagen es la escena convolucionada con la PSF; si la PSF se degrada, se pierde resolución y contraste. La decisión central: ¿cómo se calcula la PSF de una pupila con aberraciones y cuándo basta el pico?
- 🔗 **Se estudia junto con:** PSF, fase, cociente de Strehl, muestreo.

📘 **Dónde se aprende** (1 clase): [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md).

### Pupila de entrada

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C09](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md):**
- **Idea central (modelo mental):** Como mirar por dos tubos de cartón alineados: de frente se ve todo el círculo, de lado el solape se estrecha hasta anularse; el solape es el área de dos círculos.
- 🎯 **Por qué importa:** La pupila limita la luz y el viñeteo oscurece los bordes. La decisión central: ¿qué diafragma manda y cuánta luz se pierde fuera del eje?
- 🔗 **Se estudia junto con:** apertura limitante, pupila de salida, relieve ocular, obstrucción central.

📘 **Dónde se aprende** (1 clase): [B41-C09 · Pupilas y diafragmas ópticos](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md).

### Pupila de salida

- La pupila de salida es el círculo de luz que sale del ocular, de diámetro `D/M`.
- La pupila de salida es `D/M`.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- Con estos números se calcula: 7×50 → pupila de salida `50/7 = 7,14 mm`; 10×50 → `5,0 mm`; 7×35 → `5,0 mm`.
- Pausa. ¿Qué binoculares tienen mayor pupila de salida: 8×42 o 10×50? <details><summary>Respuesta</summary>8×42: `42/8 = 5,25 mm`; 10×50: `5,0 mm`.</details>
- ⚠️ **Error frecuente:** Ignorar la pupila de salida. Ejercicio 4.
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?
- 🔗 **Se estudia junto con:** aumento, objetivo, campo de visión, campo aparente.

📘 **Dónde se aprende** (4 clases): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md); [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md); [B41-C07 · Aumentos y sistemas afocales](../programa/clases/B41/B41-C07-aumentos-y-sistemas-afocales/CLASE.md); [B41-C09 · Pupilas y diafragmas ópticos](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md).

### Pureza

- La pureza compara los grupos con clases conocidas (solo existe con datos sintéticos o ya etiquetados).

💡 **Cómo se explica en la clase [B17-C06](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md):**
- Paso 5 · incertidumbre. Como los datos son sintéticos, se puede medir la pureza (0,997: 3 de 900 mal asignados).
- Ejercicio 7. La pureza fue 0,997 con 900 objetos.
- 🎯 **Por qué importa:** Un catálogo trae miles de objetos medidos en varias bandas y nadie los ha clasificado. ¿Hay poblaciones distintas?
- 🔗 **Se estudia junto con:** aprendizaje no supervisado, componente principal, varianza explicada, agrupamiento.

📘 **Dónde se aprende** (1 clase): [B17-C06 · Aprendizaje no supervisado](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md).

### Push-to

- Una montura motorizada o con GoTo apunta y sigue con motores; push-to guía sin motores.

💡 **Contexto en la clase [B08-C15](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md):**
- **Idea central (modelo mental):** El cielo gira alrededor del polo. Una montura ecuatorial gira sobre un eje paralelo al de la Tierra: con un solo movimiento uniforme sigue cualquier objeto. Una altacimutal debe mover dos ejes a velocidades que cambian con la posición del objeto.
- 🎯 **Por qué importa:** A 120 aumentos, un planeta cruza el ocular en menos de dos minutos y tienes que empujar el tubo constantemente. La pregunta motivadora: ¿qué montura necesito y qué error puedo tolerar al seguir un objeto?
- 🔗 **Se estudia junto con:** montura, altacimutal, ecuatorial, ascensión recta.

📘 **Dónde se aprende** (1 clase): [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md).

### PV

- El PV es el valor del trabajo planificado a la fecha; el EV, el valor del trabajo logrado; el AC, el costo real.
- El PV y el RMS del resto.

💡 **Cómo se explica en la clase [B43-C22](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md):**
- La superficie tiene `14,84` franjas (PV total/(λ/2)); el resto, `0,308`.
- La superficie tiene `14,8` franjas en total; tras ajustar piston, inclinaciones y desenfoque queda un resto de `97,3 nm` PV y `19,90 nm` RMS (`0,0314 λ`).
- 🎯 **Por qué importa:** El mapa de error de forma es la prueba de aceptación de un espejo. La decisión central: ¿cómo se recupera la fase, qué se descuenta y qué PV y RMS quedan?
- 🔗 **Se estudia junto con:** desplazamiento de fase, fase, desenvolvimiento, ajuste de modos.

📘 **Dónde se aprende** (2 clases): [B43-C22 · Interferometría de superficie y mapas de error de forma](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md); [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### P-valor bilateral

- El p-valor bilateral es `erfc(n_σ/√2)`.

💡 **Cómo se explica en la clase [B26-C23](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md):**
- Ejercicio 4. p-valor bilateral de `4,40σ`.
- 🎯 **Por qué importa:** Decir «hay una tensión» solo tiene sentido con un número: ¿cuántas sigmas?, ¿qué probabilidad de ocurrir por azar?, ¿qué se asume? Sin ese rigor, una discrepancia se exagera o se descarta.
- 🔗 **Se estudia junto con:** significancia, tensión de Hubble, solución, dependencia del modelo.

📘 **Dónde se aprende** (1 clase): [B26-C23 · Tensiones observacionales: constante de Hubble y S8](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md).

### Pwo

- Un pwo es un navegante maestro en la tradición de las islas Carolinas (S3).

💡 **Cómo se explica en la clase [B02-C07](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md):**
- Una valora que Mau compartiera el conocimiento por responsabilidad de preservarlo; otra, de personas micronesias, critica apropiación y objeta que la Sociedad nombre navegantes *pwo* (S3).
- 🎯 **Por qué importa:** Se discutió durante décadas si los pueblos del Pacífico llegaron a las islas por azar o por navegación deliberada. La pregunta motivadora es: ¿cómo se orienta quien no puede ver tierra, y qué dice su método sobre el valor del conocimiento oral?
- 🔗 **Se estudia junto con:** navegación sin instrumentos, compás estelar, azimut, declinación.

📘 **Dónde se aprende** (1 clase): [B02-C07 · Observaciones de Polinesia y navegación oceánica](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md).

### Pyproject.toml

- Las dependencias de ejecución se instalan siempre; las de desarrollo (por ejemplo, la herramienta de pruebas) solo para quien trabaja en el proyecto (S2). `pyproject.toml` es el archivo del proyecto que declara su nombre, versión de Python requerida y dependencias (S3).

💡 **Cómo se explica en la clase [B07-C13](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md):**
- En una carpeta vacía, `uv init --no-package --python 3.12 orbita` crea `.python-version`, `README.md`, `main.py` y `pyproject.toml` con `dependencies = []`; sin `--no-package`, el proyecto se crea como aplicación con paquete en `src/` (S5).
- Luego `uv add "numpy==2.4.4"` crea `.venv`, resuelve las versiones, descarga e instala y escribe en `pyproject.toml`: `dependencies = ["numpy==2.4.4"]`.
- 🎯 **Por qué importa:** «En mi computador funciona» es la frase más cara de la informática científica: el programa depende, sin decirlo, de la versión de Python y de cada biblioteca instalada. Si cambian, los resultados pueden cambiar o el programa fallar con un `ModuleNotFoundError`.
- 🔗 **Se estudia junto con:** entorno virtual, dependencia, dependencias de ejecución, desarrollo.

📘 **Dónde se aprende** (1 clase): [B07-C13 · Entornos y dependencias con uv](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md).
