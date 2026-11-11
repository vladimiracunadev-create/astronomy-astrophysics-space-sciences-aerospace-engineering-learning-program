# Términos · V (parte 2 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · **V** · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-v.md) · **2**

### Voz activa

- La voz activa nombra a quien actúa.

💡 **Cómo se explica en la clase [B128-C08](../programa/clases/B128/B128-C08-lenguaje-claro-y-redaccion-accesible/CLASE.md):**
- La guía de digital.gov recomienda voz activa (nombrar al actor), tiempo presente, quitar verbos escondidos, secciones cortas con títulos, listas para elementos paralelos, hablar al lector («usted/tú») y términos familiares.
- O --> R["reescribir: voz activa, frases cortas, verbos"]
- 🎯 **Por qué importa:** El lenguaje claro ayuda a personas con dificultades de lectura, a quienes leen en una segunda lengua, a quien lee con prisa y a quien usa un lector de pantalla. La decisión central: ¿qué cambios hacen el texto más claro sin perder ninguna cifra ni ningún aviso de seguridad?
- 🔗 **Se estudia junto con:** lenguaje claro, verbo escondido, jerga, métrica de superficie.

📘 **Dónde se aprende** (1 clase): [B128-C08 · Lenguaje claro y redacción accesible](../programa/clases/B128/B128-C08-lenguaje-claro-y-redaccion-accesible/CLASE.md).

### VPN

- El VPN es la suma de los flujos descontados.
- La sensibilidad, la especificidad, el VPP y el VPN miden un umbral.

💡 **Cómo se explica en la clase [B105-C24](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md):**
- Calcular sensibilidad, especificidad, VPP y VPN de un umbral con una prevalencia dada.
- umbral sensibilidad especificidad VPP (prevalencia 2 %) VPN
- 🎯 **Por qué importa:** Con tripulaciones pequeñas, el intervalo de la población general es poco sensible a los cambios personales, y un umbral con baja prevalencia da más falsas alarmas que aciertos. La decisión central: ¿cuándo un cambio de un indicador es real y qué umbral equilibra sensibilidad y valor predictivo?
- 🔗 **Se estudia junto con:** intervalo de referencia, índice de individualidad, RCV, sensibilidad.

📘 **Dónde se aprende** (2 clases): [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md); [B126-C05 · Evaluación de viabilidad económica de un negocio espacial](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md).

### VPP

- La sensibilidad, la especificidad, el VPP y el VPN miden un umbral.

💡 **Cómo se explica en la clase [B105-C24](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md):**
- Subir el umbral sube la especificidad y el VPP y baja la sensibilidad.
- T["umbral"] --> S["sensibilidad, especificidad,<br/>VPP segun prevalencia"]
- ⚠️ **Error frecuente:** Ignorar la prevalencia al evaluar un umbral. El VPP depende de ella (8.3).
- 🎯 **Por qué importa:** Con tripulaciones pequeñas, el intervalo de la población general es poco sensible a los cambios personales, y un umbral con baja prevalencia da más falsas alarmas que aciertos. La decisión central: ¿cuándo un cambio de un indicador es real y qué umbral equilibra sensibilidad y valor predictivo?
- 🔗 **Se estudia junto con:** intervalo de referencia, índice de individualidad, RCV, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md).

### Vuelco

- Un vuelco (*flip*) es una solución de pose con la inclinación invertida, casi tan compatible con los datos como la verdadera.

💡 **Cómo se explica en la clase [B103-C07](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md):**
- Pero la cola es mala: la proporción de vuelcos (más de 30°) es 0 % con 5°, 22,5 % con 20° y 11,5 % con 45° a 2 m, y a 8 m casi la mitad.
- Descripción larga: el error de profundidad crece con `Z²` y la rotación se degrada rápidamente; desde 2 m aparece una fracción creciente de vuelcos.
- ⚠️ **Error frecuente:** Confiar en la rotación con poca perspectiva. Revisa la inclinación y los vuelcos (8.5).
- 🎯 **Por qué importa:** A 8 m un marcador de 10 cm mide 10 px y su pose es casi indeterminada; a 1 m, el error de profundidad es de unos 3 mm. La decisión central: ¿hasta qué distancia es fiable la pose estimada con un objeto de cierto tamaño, y cuándo hay que dudar de ella?
- 🔗 **Se estudia junto con:** pose, PnP, PnP plano, radio cuadrático medio.

📘 **Dónde se aprende** (1 clase): [B103-C07 · Estimación de pose de objetos y objetivos por visión](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md).

### Vuelta

- La vuelta es un periodo orbital `T`.

💡 **Cómo se explica en la clase [B11-C10](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md):**
- Se integra una órbita y, al final de cada vuelta, se evalúa `ε = (v_x² + v_y²)/2 − GM/r` y `h = x v_y − y v_x`.
- Con 200 pasos por vuelta, la energía de Euler sube `+23 %` tras una vuelta (`r/a = 1,37`) y `+48 %` tras cinco (`r/a = 2,06`).
- 🎯 **Por qué importa:** Un análisis de misión puede necesitar propagar un satélite durante años, es decir, decenas de miles de vueltas. Si cada vuelta añade o quita un poco de energía, la altura de la órbita cambia solo por culpa del programa.
- 🔗 **Se estudia junto con:** cantidad conservada, deriva, secular, acotada u oscilante.

📘 **Dónde se aprende** (1 clase): [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md).

### Vulcanismo evolucionado

- El vulcanismo evolucionado es el de magmas diferenciados (más sílice, más viscosos).

💡 **Cómo se explica en la clase [B70-C02](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md):**
- python programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/domos.py
- 🎯 **Por qué importa:** Una colina empinada de lava puede tener una altura que solo depende del material y de `g`. La decisión central: ¿qué altura puede alcanzar un domo de resistencia dada y qué cambiaría en otro mundo?
- 🔗 **Se estudia junto con:** domo, resistencia a la fluencia, plástico perfecto.

📘 **Dónde se aprende** (1 clase): [B70-C02 · Domos volcánicos y vulcanismo evolucionado](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md).

### Vulnerabilidad

- La amenaza es la probabilidad e intensidad del fenómeno; la exposición es lo que está en su camino; la vulnerabilidad es cuán dañable es.

💡 **Cómo se explica en la clase [B57-C19](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md):**
- Tres capas de `60 × 60` celdas sintéticas: la amenaza se concentra en el noroeste, la exposición en el centro y la vulnerabilidad crece hacia el este.
- Definir riesgo como amenaza × exposición × vulnerabilidad y como suma ponderada.
- 🎯 **Por qué importa:** Los mapas de riesgo orientan decisiones y presupuestos, pero dependen de supuestos de ponderación que suelen quedar ocultos. La decisión central: ¿cómo combino capas y cuánto cambian las zonas prioritarias si cambio los pesos?
- 🔗 **Se estudia junto con:** amenaza, exposición, proceso analítico jerárquico (AHP), razón de consistencia.

📘 **Dónde se aprende** (1 clase): [B57-C19 · SIG y análisis de riesgo](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md).
