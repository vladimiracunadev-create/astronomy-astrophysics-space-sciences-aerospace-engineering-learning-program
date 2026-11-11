# Términos · A (parte 2 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

**A** · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-a.md) · **2** · [3](terminos-a-3.md)

### Anchura del pulso

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C08](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md):**
- **Idea central (modelo mental):** Es una carrera en que todos reciben el mismo empujón: los livianos llegan primero. Si la salida es desordenada, dos corredores casi iguales llegan juntos.
- 🎯 **Por qué importa:** La resolución de masa decide qué especies se separan. La decisión central: ¿qué tiempo de vuelo, qué dispersión y qué resolución permiten distinguir dos iones casi isobáricos?
- 🔗 **Se estudia junto con:** tiempo de vuelo, resolución de masa, dispersión de energía inicial, iones isobáricos.

📘 **Dónde se aprende** (1 clase): [B47-C08 · Espectrómetros de masas orbitales](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md).

### Ancla

- Gauss–Newton: iteración que linealiza y resuelve `H Δx = −b`. Ancla: pose fija que elimina la libertad de colocar el grafo en cualquier lugar.

💡 **Cómo se explica en la clase [B99-C03](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md):**
- Se fija la primera pose (ancla); sin ella `H` es singular, porque el coste no cambia al mover todo el grafo rígidamente.
- El coste no cambia al mover o girar todo el grafo; sin ancla `H` es singular y la solución no es única.
- ⚠️ **Error frecuente:** Olvidar fijar una pose. Sin ancla `H` es singular (8.3).
- 🎯 **Por qué importa:** Sumar movimientos da una trayectoria que no cierra el lazo; una medida de cierre de bucle dice que la pose final es la inicial. La decisión central: ¿cómo repartir el desacuerdo entre cientos de poses de modo coherente con la incertidumbre de cada medida?
- 🔗 **Se estudia junto con:** Grafo de poses, Medida z_ij, Información Ω_ij, Error de arista e_ij.

📘 **Dónde se aprende** (1 clase): [B99-C03 · SLAM basado en grafos de poses](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md).

### Anclaje

- Un anclaje es la distancia geométrica a la primera galaxia de la cadena.
- El cordón de seguridad ata a la persona a un anclaje; limita la distancia al anclaje.

💡 **Cómo se explica en la clase [B26-C12](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md):**
- A["Anclaje: LMC<br/>σ = 1,2 %"] --> B["Peldaño 2<br/>σ_μ = 0,03 mag → 1,38 %"]
- La distancia a la LMC se conoce con `1,2 %` por binarias eclipsantes; la incertidumbre total de la escalera pasó de `2,5 %` a `1,3 %`, y `H₀ = 74,22 ± 1,82 km/s/Mpc` con solo ese anclaje (S1, resumen), una precisión de `2,45 %`.
- 🎯 **Por qué importa:** Una distancia con un error de `2,6 %` produce un `H₀` con un error similar, y la discusión actual sobre `H₀` gira alrededor de esas décimas de punto porcentual. Entender cómo se acumulan los errores en una cadena de pasos evita confiar en una cifra más de lo debido.
- 🔗 **Se estudia junto con:** escalera de distancias, peldaño, error fraccional, error de módulo.

📘 **Dónde se aprende** (2 clases): [B26-C12 · Escalas de distancia cosmológicas](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md); [B108-C02 · Planificación de desplazamientos y rutas de EVA](../programa/clases/B108/B108-C02-planificacion-de-desplazamientos-y-rutas-de-eva/CLASE.md).

### Anexado solo

- Cadena de hashes: cada entrada incluye el hash de la anterior. Anexado solo: no se editan entradas previas.

💡 **Contexto en la clase [B96-C30](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md):**
- 🎯 **Por qué importa:** Sin registro verificable no se puede reconstruir un incidente ni demostrar quién aprobó un comando. La decisión central: ¿cómo se registra para que una alteración se detecte y cuánto hay que revisar en una auditoría?
- 🔗 **Se estudia junto con:** Bitácora, Cadena de hashes, Hash anclado, Muestra de auditoría.

📘 **Dónde se aprende** (1 clase): [B96-C30 · Registro y auditoría de operaciones](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md).

### Angular

- Con pares solitarios aparecen la forma angular (como el agua) y la piramidal (como el amoníaco).

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- Con 4, la geometría electrónica es tetraédrica; si todos son enlaces, la forma también lo es (109,47°); si hay un par solitario, la forma es piramidal; si hay dos, angular.
- En el agua angular con 104,48°, la suma tiene módulo `2 cos(52,24°) = 1,2247` (en unidades del dipolo de enlace): molécula polar.
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).
- 🔗 **Se estudia junto con:** dominio de electrones, modelo de repulsión de pares de valencia, geometría electrónica, forma molecular.

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Ángulo

- Un ángulo es adimensional en el SI; el radián es la unidad coherente.
- El ángulo `ψ` es el que forma con la dirección radial.
- El ángulo entre vectores no nulos cumple `cos θ = ⟨u, v⟩/(‖u‖‖v‖)`.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B10-C06](../programa/clases/B10/B10-C06-producto-interno-y-ortogonalidad/CLASE.md):**
- Gracias a ella el coseno de la fórmula del ángulo nunca sale de `[−1, 1]`.
- C -->|"> 0"| D["ángulo agudo:<br/>apuntan hacia el mismo lado"]
- 🎯 **Por qué importa:** La potencia que recibe un panel solar depende del ángulo entre su normal y la dirección al Sol: más inclinado, menos luz. El control de actitud, la orientación de antenas y de instrumentos usan el mismo cálculo.
- 🔗 **Se estudia junto con:** producto interno, norma, ortogonales, vector unitario.

📘 **Dónde se aprende** (7 clases): [B10-C06 · Producto interno y ortogonalidad](../programa/clases/B10/B10-C06-producto-interno-y-ortogonalidad/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md); [B30-C10 · Viento solar y heliosfera](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md); [B32-C01 · Ecuación de transferencia radiativa en atmósferas estelares](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md); [B40-C08 · Polarización E y B del fondo cósmico](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md); [B45-C15 · Polarización lineal y circular](../programa/clases/B45/B45-C15-polarizacion-lineal-y-circular/CLASE.md) y 1 más.

### Ángulo azimutal

- En matemáticas y física se usan el ángulo polar `θ` (desde el eje `z`, de 0° a 180°) y el ángulo azimutal `φ` (en el plano `xy` desde el eje `x`, de 0° a 360°).

💡 **Contexto en la clase [B04-C11](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md):**
- **Idea central (modelo mental):** Imagina una esfera enorme centrada en el observador con las estrellas pegadas en su superficie. La declinación es como la latitud terrestre y la ascensión recta como la longitud: dos ángulos bastan para fijar un punto en la esfera. Con una distancia `r` se completa la posición en el espacio.
- 🎯 **Por qué importa:** Un catálogo de estrellas da para cada una dos números: dónde está en el cielo. Pero un programa que cruza catálogos, calcula separaciones o apunta un telescopio no trabaja con horas y grados: trabaja con vectores.
- 🔗 **Se estudia junto con:** coordenadas esféricas, ángulo polar, ascensión recta, declinación.

📘 **Dónde se aprende** (1 clase): [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md).

### Ángulo beta

- El ángulo beta (β) fija su duración: `fracción = arccos(√(h²+2Rh)/((R+h)cos β))/π`, y es cero si el argumento es 1 o mayor.
- El ángulo beta `β` es el ángulo entre el Sol y el plano orbital.
- El ángulo beta del blanco respecto del plano.

💡 **Cómo se explica en la clase [B83-C10](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md):**
- Calcular la fracción de eclipse de una órbita circular en función del ángulo beta.
- 🎯 **Por qué importa:** Un satélite sin energía suficiente en el peor eclipse se apaga y no vuelve. La decisión central: ¿el panel y la batería cierran el balance en el caso más desfavorable, con margen y con una descarga que la batería soporte?
- 🔗 **Se estudia junto con:** eclipse, potencia del panel, energía requerida, profundidad de descarga.

📘 **Dónde se aprende** (3 clases): [B47-C17 · Planificación de observaciones](../programa/clases/B47/B47-C17-planificacion-de-observaciones/CLASE.md); [B83-C10 · Presupuestos de energía](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md); [B86-C04 · Orientación solar y eclipses](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md).

### Ángulo causal

- El ángulo causal `η/χ`.

💡 **Cómo se explica en la clase [B40-C04](../programa/clases/B40/B40-C04-problemas-del-horizonte-y-de-la-planitud/CLASE.md):**
- Con `H₀ = 67,4` y `Ω_m = 0,315` (Planck 2018 VI, resumen), el horizonte comóvil en `z* = 1090` es `280,11 Mpc` y la distancia es `13 864,3 Mpc`: el ángulo causal es `1,158°`, unos `2450` parches desconectados.
- Obtener el ángulo causal en `z* = 1090`.
- 🎯 **Por qué importa:** Regiones del fondo separadas más de un grado nunca se comunicaron en el modelo sin inflación, y la curvatura tendría que ser fantásticamente pequeña al principio. La decisión central: ¿qué tan grande es el problema, en números?
- 🔗 **Se estudia junto con:** horizonte de partículas, distancia comóvil, problema de la planitud.

📘 **Dónde se aprende** (1 clase): [B40-C04 · Problemas del horizonte y de la planitud](../programa/clases/B40/B40-C04-problemas-del-horizonte-y-de-la-planitud/CLASE.md).

### Ángulo cenital

- El ángulo cenital `χ` es el ángulo del Sol con la vertical.
- El ángulo cenital `θ` es el que forma el Sol con la vertical: `tan θ = S/H`.

💡 **Cómo se explica en la clase [B30-C17](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md):**
- *Descripción textual:* la altura y el ángulo cenital dan la capa de Chapman; la energía de los electrones da los pares; la longitud de onda da la energía de los fotones; las conductancias dan la corriente y el calentamiento.
- 🎯 **Por qué importa:** La aurora y las corrientes ionosféricas son la parte visible y eléctrica del acoplamiento entre la magnetosfera y la atmósfera. La decisión central: ¿dónde se produce la ionización y cuánta energía se disipa por efecto Joule?
- 🔗 **Se estudia junto con:** capa de Chapman, altura de escala, conductancia de Pedersen, de Hall.

📘 **Dónde se aprende** (3 clases): [B30-C17 · Auroras y corrientes ionosféricas](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md); [B54-C10 · Fotoquímica atmosférica](../programa/clases/B54/B54-C10-fotoquimica-atmosferica/CLASE.md); [B131-C01 · Actividades de medición astronómica para el aula](../programa/clases/B131/B131-C01-actividades-de-medicion-astronomica-para-el-aula/CLASE.md).

### Ángulo central

- El ángulo central `λ` es el ángulo en el centro de la Tierra entre el sensor y el límite de visibilidad.
- El ángulo central `λ` entre la estación y el nadir del satélite cumple `tan ε = (cos λ − R/(R+h))/sin λ`.

💡 **Cómo se explica en la clase [B119-C13](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md):**
- A 550 km: período `95.65 min`, ángulo central `14.96°`, paso máximo `477 s` (`7.95 min`).
- Calcular el ángulo central de visibilidad y la duración máxima de un paso.
- 🎯 **Por qué importa:** El art. VI del Convenio de Registro prevé ayuda en la identificación mediante medios de rastreo; ninguna clase anterior muestra qué cubre un sensor ni cómo se criba un catálogo.
- 🔗 **Se estudia junto con:** conciencia situacional espacial, paso, cribado, fuerza bruta.

📘 **Dónde se aprende** (2 clases): [B89-C14 · Estaciones terrestres](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md); [B119-C13 · Vigilancia y conciencia situacional espacial](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md).

### Ángulo coorbital

- El ángulo coorbital `θ = λ_part − λ_Tierra` (sin envolver) distingue: tadpole (`θ` oscila alrededor de `±60°` sin cruzar `0` ni `π`), herradura (`θ` cubre `π` sin cruzar `0` ni `2π`) y cuasi-satélite (`θ` oscila alrededor de `0` con una amplitud pequeña y la partícula se mantiene a unos pocos `R_H`).

💡 **Cómo se explica en la clase [B73-C22](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md):**
- Descripción larga: tres comportamientos del ángulo coorbital en 200 años, con la constante de Jacobi intacta y una captura temporal que dura menos de un año con velocidad alta.
- Definir el ángulo coorbital `θ` sin envolver respecto de la Tierra.
- 🎯 **Por qué importa:** Un asteroide puede acompañar a la Tierra durante siglos sin orbitarla: dando vueltas alrededor de L4 (tadpole), de L3–L4–L5 (herradura) o de la propia Tierra (cuasi-satélite); y puede ser capturado temporalmente dentro de su esfera de Hill. Distinguirlos requiere una clasificación operativa y una advertencia: no son satélites.
- 🔗 **Se estudia junto con:** tadpole, herradura, cuasi-satélite, captura temporal.

📘 **Dónde se aprende** (1 clase): [B73-C22 · Capturas temporales y cuasi-satélites](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md).

### Ángulo crítico

- El ángulo crítico es la pendiente máxima estable.
- La reflexión total ocurre al pasar a un medio de menor índice con un ángulo mayor que el ángulo crítico `arcsen(n₂/n₁)`.
- El ángulo crítico `asin(n₂/n₁)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C19](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md):**
- Al pasar del vidrio al aire, el ángulo crítico es `arcsen(1/1,5) = 41,81°`.
- Para un medio de `n = 1,33` (sintético) el ángulo crítico es `48,75°`.
- 🎯 **Por qué importa:** Un telescopio espacial o una cámara en órbita baja distinguen detalles hasta cierto límite que no depende de la calidad de la electrónica, y la luz de un objeto lejano llega con retraso. La pregunta motivadora es: ¿qué determina cuán pequeño es el detalle que un instrumento óptico puede resolver y cuánto tarda la luz en llegar?
- 🔗 **Se estudia junto con:** velocidad de la luz en el vacío, índice de refracción, reflexión, refracción.

📘 **Dónde se aprende** (4 clases): [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md); [B41-C02 · Índice de refracción y ley de Snell](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md); [B47-C05 · Instrumentos de rayos X](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md); [B61-C03 · Cráteres complejos: colapso, picos centrales y terrazas](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md).

### Ángulo de anticipación

- El ángulo de anticipación (*point-ahead*) `α = v_⊥/c` es la diferencia entre la dirección a la posición actual del receptor y a la que tendrá cuando llegue la luz.

💡 **Cómo se explica en la clase [B92-C07](../programa/clases/B92/B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md):**
- *Descripción textual:* la distancia fija el tiempo de luz y la caída de la tasa; la velocidad transversal fija el ángulo de anticipación, que comparado con la divergencia decide la pérdida si no se aplica; las aperturas escalan la tasa.
- Descripción larga: la tasa cae con el cuadrado de la distancia y el tiempo de luz crece con ella; el ángulo de anticipación crece con la velocidad transversal y supera al ancho del haz por encima de unos 10 km/s.
- 🎯 **Por qué importa:** El espacio profundo exige otra forma de pensar: pocos fotones, latencia de minutos y apuntamiento predictivo. La decisión central: ¿cómo cambia la tasa con la distancia y qué hay que prever para que el haz llegue al receptor?
- 🔗 **Se estudia junto con:** tiempo de luz, escalado de tasa, ganancia de transmisión, latencia.

📘 **Dónde se aprende** (1 clase): [B92-C07 · Enlaces ópticos de espacio profundo](../programa/clases/B92/B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md).

### Ángulo de ataque

- El ángulo de ataque `α` es el que forman el eje del vehículo y la velocidad relativa al aire.

💡 **Contexto en la clase [B77-C03](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR T["t"] --> HV["h(t), v(t)"] HV --> Q["q = 0,5 rho(h) v^2"] Q --> D["D = Cd q A"] Q --> L["L = CLalfa alfa q A"] Q --> M["max-q: dq/dt = 0"] ``` *Descripción textual:* el tiempo da altitud y velocidad; de ahí sale la presión dinámica, con la que se calculan arrastre, sustentación y el máximo de `q`.
- 🎯 **Por qué importa:** El momento de mayor carga aerodinámica no es el de mayor velocidad ni el de menor altitud. La decisión central: ¿cuándo ocurre el máximo de la presión dinámica y qué fuerzas produce?
- 🔗 **Se estudia junto con:** presión dinámica, fuerza aerodinámica, arrastre, sustentación.

📘 **Dónde se aprende** (1 clase): [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md).

### Ángulo de avance

- El ángulo de avance `λ = atan(L/(π d))`.

💡 **Cómo se explica en la clase [B43-C14](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md):**
- *Descripción textual:* el ángulo de avance y la fricción fijan el rendimiento y el autobloqueo; la relación y la rigidez fijan la resolución y la resonancia.
- El ángulo de avance es `2,734°` frente a `φ = 5,711°` (`μ = 0,1`): hay autobloqueo y el rendimiento es `0,3216`.
- 🎯 **Por qué importa:** El reductor fija la resolución, la fuerza disponible y el comportamiento dinámico. La decisión central: ¿qué relación, qué rendimiento y qué rigidez permiten apuntar con la resolución pedida sin resonancias?
- 🔗 **Se estudia junto con:** ángulo de fricción, autobloqueo, rendimiento, holgura.

📘 **Dónde se aprende** (1 clase): [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md).

### Ángulo de Brewster

- El ángulo de Brewster `atan(n₂/n₁)`.

💡 **Cómo se explica en la clase [B41-C02](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md):**
- El ángulo de Brewster es `56,5994°` con `Rp = 4 × 10⁻³³` y `Rs = 0,15518`.
- Para aire (`1,0003`) a vidrio (`1,517`), la reflectancia en incidencia normal es `0,042132`, el ángulo de Brewster es `56,5994°` (donde `Rp = 0`) y de vidrio a aire el ángulo crítico es `41,2536°`.
- 🎯 **Por qué importa:** Un telescopio refractor y los recubrimientos dependen de cuánta luz se refleja y a qué ángulo se dobla. La decisión central: ¿qué fracción de luz se pierde por reflexión y cuándo hay reflexión total?
- 🔗 **Se estudia junto con:** ley de Snell, ángulo crítico, reflectancia, transmitancia.

📘 **Dónde se aprende** (1 clase): [B41-C02 · Índice de refracción y ley de Snell](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md).

### Ángulo de Cherenkov

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B31-C14](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md):**
- angulo de Cherenkov para beta -> 1: 41.247 grados
- 🎯 **Por qué importa:** Interpretar una señal exige saber qué partículas la producen y con qué precisión se mide su energía. La decisión central: ¿qué umbral y qué resolución tiene un detector?
- 🔗 **Se estudia junto con:** radiación de Cherenkov, rendimiento, calorímetro, resolución.

📘 **Dónde se aprende** (1 clase): [B31-C14 · Detectores de partículas](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md).

### Ángulo de contacto

- El ángulo de contacto `θ₀ = arccos(1 − z₀/R)` fija el arco en que la rueda toca el suelo.

💡 **Contexto en la clase [B102-C02](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md):**
- 🎯 **Por qué importa:** La tracción de un rover en regolito no sale de un coeficiente de rozamiento único. La decisión central: ¿cuánta fuerza neta de empuje queda para tirar del vehículo, una vez descontada la resistencia que crea el propio hundimiento, y cómo depende del patinaje y de la gravedad?
- 🔗 **Se estudia junto con:** ley de presión-hundimiento, resistencia de cizalla, empuje, resistencia por compactación.

📘 **Dónde se aprende** (1 clase): [B102-C02 · Terramecánica: tracción y hundimiento en suelos sueltos](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md).

### Ángulo de desviación

- El ángulo de desviación de un rayo que pasa a distancia `b` de una masa puntual `M` es, en campo débil, `4GM/(c²b)` (dato de la relatividad general, B26).

💡 **Cómo se explica en la clase [B25-C14](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md):**
- Definir lente, fuente, ángulo de desviación, radio de Einstein, imagen y magnificación.
- 🎯 **Por qué importa:** La luz de una galaxia lejana se curva al pasar cerca de una masa, y la masa interior se deduce del tamaño de la distorsión sin importar si es luminosa u oscura ni si está en equilibrio. Por eso las lentes son una prueba directa de la distribución de masa.
- 🔗 **Se estudia junto con:** lente gravitacional, ecuación de la lente, radio de Einstein, esfera isoterma singular (SIS).

📘 **Dónde se aprende** (1 clase): [B25-C14 · Lentes gravitacionales galácticas](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md).

### Ángulo de entrada

- El ángulo de entrada `γ_E` se mide bajo el horizonte.

💡 **Cómo se explica en la clase [B77-C14](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md):**
- *Descripción textual:* la entrada, el ángulo y el coeficiente balístico dan la ecuación de movimiento; su solución cerrada da la desaceleración máxima y la altitud del pico, que se contrastan con una integración numérica.
- Con ángulo de entrada de `5°` la desaceleración máxima es `11,70 g` tanto con `β = 100` como con `1000 kg/m²` (la integración da `11,71` y `11,70 g`), pero el pico ocurre a `60,2 km` en el primero y a `40,6 km` en el segundo.
- 🎯 **Por qué importa:** La desaceleración máxima fija la carga sobre la carga útil y sobre la tripulación. La decisión central: ¿qué ángulo de entrada limita la desaceleración y de qué propiedades del vehículo no depende?
- 🔗 **Se estudia junto con:** entrada balística, coeficiente balístico, desaceleración máxima, altitud del pico.

📘 **Dónde se aprende** (1 clase): [B77-C14 · Dinámica de reentrada](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md).

### Ángulo de equilibrio

- El ángulo de equilibrio (trim) es donde `Cm = 0`.

💡 **Cómo se explica en la clase [B77-C17](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md):**
- *Descripción textual:* el momento de cabeceo da el ángulo de equilibrio y la frecuencia natural;
- `Cm_q` da el amortiguamiento; si `Cm_α` cambia de signo, el equilibrio se vuelve inestable y el ángulo diverge.
- 🎯 **Por qué importa:** Una cápsula inestable no entra con el escudo hacia delante. La decisión central: ¿qué pendiente de momento da una oscilación acotada y cuánto tarda en divergir una inestable?
- 🔗 **Se estudia junto con:** estabilidad estática, frecuencia natural, amortiguamiento, divergencia.

📘 **Dónde se aprende** (1 clase): [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md).

### Ángulo de fase

- El ángulo de fase `i` es el ángulo Sol–Luna–Tierra visto desde la Luna.
- El ángulo de fase es el que debe separar a los cuerpos al salir.
- El ángulo de fase `φ` es la posición angular del objetivo menos la del perseguidor.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C08](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md):**
- La diferencia se debe a que el Sol está a una distancia finita: el ángulo de fase exacto es `tan i = R sen ψ / (d − R cos ψ)`, con `R` la distancia al Sol y `d` la de la Luna.
- 🎯 **Por qué importa:** La Luna es el primer blanco de cualquier observación y el principal enemigo de las observaciones de objetos débiles (C12). Saber su fase y cuándo está en el cielo es parte de toda planificación.
- 🔗 **Se estudia junto con:** fase, elongación, Creciente, menguante.

📘 **Dónde se aprende** (5 clases): [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md); [B71-C18 · Maniobra de Hohmann](../programa/clases/B71/B71-C18-maniobra-de-hohmann/CLASE.md); [B76-C10 · Encuentro orbital](../programa/clases/B76/B76-C10-encuentro-orbital/CLASE.md); [B118-C03 · Detección y seguimiento óptico](../programa/clases/B118/B118-C03-deteccion-y-seguimiento-optico/CLASE.md); [B131-C05 · Demostraciones visuales y modelos para el aula](../programa/clases/B131/B131-C05-demostraciones-visuales-y-modelos-para-el-aula/CLASE.md).

### Ángulo de fase de salida

- El ángulo de fase de salida `φ` es la diferencia de longitud heliocéntrica destino − Tierra al partir.

💡 **Cómo se explica en la clase [B75-C02](../programa/clases/B75/B75-C02-angulos-de-fase-planetaria/CLASE.md):**
- Definir el ángulo de fase de salida y su signo.
- 🎯 **Por qué importa:** Una nave que llega al afelio de su elipse debe encontrar allí al planeta. Como el planeta se mueve mientras la nave vuela, hay que salir cuando el destino va por delante (o por detrás) un ángulo preciso.
- 🔗 **Se estudia junto con:** periodo sinódico, movimiento medio, exterior, interior.

📘 **Dónde se aprende** (1 clase): [B75-C02 · Ángulos de fase planetaria](../programa/clases/B75/B75-C02-angulos-de-fase-planetaria/CLASE.md).

### Ángulo de fricción

- La cohesión `c` es la resistencia al corte sin carga y `φ` el ángulo de fricción.
- El ángulo de fricción `φ = atan μ`.

💡 **Cómo se explica en la clase [B43-C14](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md):**
- *Descripción textual:* el ángulo de avance y la fricción fijan el rendimiento y el autobloqueo; la relación y la rigidez fijan la resolución y la resonancia.
- 🎯 **Por qué importa:** El reductor fija la resolución, la fuerza disponible y el comportamiento dinámico. La decisión central: ¿qué relación, qué rendimiento y qué rigidez permiten apuntar con la resolución pedida sin resonancias?
- 🔗 **Se estudia junto con:** ángulo de avance, autobloqueo, rendimiento, holgura.

📘 **Dónde se aprende** (2 clases): [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md); [B97-C06 · Control de movilidad sobre regolito](../programa/clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md).

### Ángulo de giro

- El ángulo de giro `δ` es la desviación entre las direcciones de llegada y salida.
- El ángulo de giro `δ` es lo que se desvía `v∞`.

💡 **Cómo se explica en la clase [B71-C09](../programa/clases/B71/B71-C09-orbitas-parabolicas-e-hiperbolicas/CLASE.md):**
- El ángulo asintótico es `ν∞ = arccos(−1/e)` y el giro `δ = 2 arcsin(1/e)`.
- Calcular el ángulo asintótico `ν∞`, el giro `δ = 2 arcsin(1/e)` y el parámetro de impacto `b`.
- 🎯 **Por qué importa:** Las trayectorias de escape y de sobrevuelo son hipérbolas respecto del cuerpo local. La decisión central: ¿qué velocidad en el periapsis produce un exceso `v∞` dado y cuánto se desvía la trayectoria?
- 🔗 **Se estudia junto con:** exceso de velocidad hiperbólica, energía característica, excentricidad, parámetro de impacto.

📘 **Dónde se aprende** (2 clases): [B71-C09 · Órbitas parabólicas e hiperbólicas](../programa/clases/B71/B71-C09-orbitas-parabolicas-e-hiperbolicas/CLASE.md); [B75-C06 · Asistencias gravitacionales](../programa/clases/B75/B75-C06-asistencias-gravitacionales/CLASE.md).

### Ángulo de incidencia

- El ángulo de incidencia `α` entre la normal y el Sol reduce la fuerza como `cos²α` para una vela ideal.

💡 **Contexto en la clase [B78-C12](../programa/clases/B78/B78-C12-velas-solares/CLASE.md):**
- 🎯 **Por qué importa:** La vela no gasta propelente, pero su empuje es del orden de los micronewton por metro cuadrado y cae con el cuadrado de la distancia al Sol. La decisión central: ¿cuánta aceleración da una vela real y cómo depende de su orientación y de su distancia?
- 🔗 **Se estudia junto con:** irradiancia, presión de radiación, reflectividad, vela.

📘 **Dónde se aprende** (1 clase): [B78-C12 · Velas solares](../programa/clases/B78/B78-C12-velas-solares/CLASE.md).

### Ángulo de inclinación

- El ángulo de inclinación es el del eje mayor respecto del eje de referencia.

💡 **Contexto en la clase [B91-C02](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md):**
- 🎯 **Por qué importa:** Un enlace pierde potencia si las polarizaciones no coinciden, y puede perderla toda si son ortogonales. La decisión central: ¿qué polarización y qué razón axial exigir a las dos antenas para que la desadaptación quede por debajo del margen del enlace?
- 🔗 **Se estudia junto con:** vector de Jones, razón axial, factor de pérdida de polarización, aislamiento de polarización cruzada.

📘 **Dónde se aprende** (1 clase): [B91-C02 · Polarización de antenas y pérdidas por desadaptación](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md).

### Ángulo de la regla

- El ángulo de la regla es `θ = r_BAO/D_C`.

💡 **Cómo se explica en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- *Descripción textual:* las fluctuaciones crecen como `a` mientras la materia domina y más despacio después; por separado, la regla BAO se convierte en ángulo dividiéndola por la distancia comóvil.
- Ejercicio 12 · integrador. Elabora tu *curva de crecimiento*: resuelve el crecimiento por ODE e integral para dos `Ω_m`, la supresión, el `D_C` y el ángulo de la regla BAO a `z = 0,35` en dos modelos.
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.
- 🔗 **Se estudia junto con:** perturbación de densidad, crecimiento lineal, ecuación de crecimiento, supresión.

📘 **Dónde se aprende** (1 clase): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md).

### Ángulo de la trayectoria

- El ángulo de la trayectoria `γ` se mide sobre el horizonte local.

💡 **Contexto en la clase [B77-C12](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md):**
- 🎯 **Por qué importa:** La trayectoria de ascenso decide a la vez las pérdidas, las cargas y la órbita alcanzada. La decisión central: ¿qué perfil de inclinación lleva al vehículo a una órbita casi circular y qué cuesta?
- 🔗 **Se estudia junto con:** giro de gravedad, fase vertical, agotamiento, ecuación vis-viva.

📘 **Dónde se aprende** (1 clase): [B77-C12 · Perfil de ascenso orbital](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md).

### Ángulo de Mach

- El ángulo de Mach es `μ = arcsin(1/M)`.

💡 **Cómo se explica en la clase [B79-C06](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md):**
- *Descripción textual:* el Mach supersónico determina la relación de áreas, el ángulo de Mach y la función de Prandtl–Meyer; las dos relaciones se verifican con integrales numéricas.
- Una tobera con `A/A* = 5` produce `M = 3,17478` con ángulo de Mach `18,36°`.
- 🎯 **Por qué importa:** El comportamiento de un flujo a `M > 1` en toberas y vehículos no lo trata ninguna clase del tronco. Sin él no se entiende por qué una tobera necesita una parte divergente.
- 🔗 **Se estudia junto con:** relación área–Mach, función de Prandtl–Meyer, expansión de Prandtl–Meyer.

📘 **Dónde se aprende** (1 clase): [B79-C06 · Flujos supersónicos](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md).

### Ángulo de mezcla

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B31-C11](../programa/clases/B31/B31-C11-neutrinos-y-oscilaciones/CLASE.md):**
- **Idea central (modelo mental):** Como una luz que cambia de color con el tiempo según la distancia recorrida: a cierta distancia vuelve al color inicial.
- 🎯 **Por qué importa:** Detectar neutrinos del Sol, la atmósfera y aceleradores exige saber cuánto oscilan. La decisión central: ¿cuál es la probabilidad de oscilación a cierta distancia y energía?
- 🔗 **Se estudia junto con:** probabilidad de oscilación, diferencia de masas, longitud de oscilación, promedio en energía.

📘 **Dónde se aprende** (1 clase): [B31-C11 · Neutrinos y oscilaciones](../programa/clases/B31/B31-C11-neutrinos-y-oscilaciones/CLASE.md).

### Ángulo de paso

- El ángulo de paso `ψ` es el ángulo entre la tangente al brazo y la tangente al círculo que pasa por ese punto: `ψ = 0` es un círculo y `ψ = 90°` un rayo.

💡 **Cómo se explica en la clase [B25-C02](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md):**
- Si `R = R_k e^{−(β−β_k) tan ψ}`, entonces `dR/dβ = −R tan ψ`: la razón entre el avance radial y el avance a lo largo del círculo vale `tan ψ` en todos los puntos, lo que fija un ángulo de paso constante.
- Reid y colaboradores señalan que una galaxia de dos brazos tendría que enrollarse dos veces para pasar por las paralajes medidas, con ángulos de paso cercanos a `5°`; el promedio de los cuatro brazos mayores ponderado por longitud es de unos `10°` (S2).
- 🎯 **Por qué importa:** Los brazos espirales son lo más llamativo de una galaxia de disco, pero la rotación diferencial debería enrollarlos hasta borrarlos en unas pocas vueltas. Entender esa paradoja es entender qué es un brazo: no un montón fijo de materia, sino un patrón.
- 🔗 **Se estudia junto con:** espiral logarítmica, nudo, barra, rotación diferencial.

📘 **Dónde se aprende** (1 clase): [B25-C02 · Brazos espirales y barra galáctica](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md).

### Ángulo de paso ecuatorial

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B30-C16](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md):**
- **Idea central (modelo mental):** Una partícula atrapada es como una canica en un cuenco: rebota entre las paredes; si va casi recta hacia abajo (ángulo de paso pequeño) se sale por el fondo.
- 🎯 **Por qué importa:** Las partículas con ángulo de paso pequeño se pierden en la atmósfera; las demás quedan atrapadas y dañan satélites. La decisión central: ¿qué partículas quedan atrapadas y con qué periodo rebotan?
- 🔗 **Se estudia junto con:** punto de espejo, cono de pérdida, periodo de rebote, cinturones de Van Allen.

📘 **Dónde se aprende** (1 clase): [B30-C16 · Cinturones de Van Allen](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md).

### Ángulo de rotación

- El ángulo de rotación `θ` es positivo en sentido antihorario visto desde el extremo positivo del eje (regla de la mano derecha).

💡 **Cómo se explica en la clase [B10-C12](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md):**
- *Descripción textual:* para un mismo ángulo, la rotación activa aplica `R(θ)` y la pasiva aplica su transpuesta; los números se parecen pero los signos difieren, y confundirlas es el error más común.
- 🎯 **Por qué importa:** La Tierra gira una vuelta cada 23,93 horas: una estación de seguimiento ve pasar los satélites porque sus ejes locales rotan respecto del espacio inercial. Un satélite recibe órdenes expresadas en ejes terrestres y debe saber dónde están en ejes inerciales.
- 🔗 **Se estudia junto con:** rotación, activa, pasiva, eje de rotación.

📘 **Dónde se aprende** (1 clase): [B10-C12 · Rotaciones en el plano y espacio](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md).

### Ángulo de rotación terrestre

- El ángulo de rotación terrestre (ERA) es el ángulo de `R`, y se define por `ERA(Tu) = 2π(0,7790572732640 + 1,00273781191135448 Tu)` con `Tu = (fecha juliana UT1 − 2451545,0)` (S1, ec. 5.14).

💡 **Cómo se explica en la clase [B10-C16](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md):**
- Calcular el ángulo de rotación terrestre `ERA` para una fecha UT1.
- 🎯 **Por qué importa:** Una estación terrestre tiene coordenadas fijas en la Tierra. Un satélite se propaga en un sistema inercial, donde las leyes de Newton valen.
- 🔗 **Se estudia junto con:** marco de referencia, inercial, GCRS, ITRS.

📘 **Dónde se aprende** (1 clase): [B10-C16 · Transformación de marcos de referencia](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md).

### Ángulo de rotación terrestre (ERA)

- El ángulo de rotación terrestre (ERA) es el ángulo entre un origen celeste de referencia y un origen terrestre, que describe la rotación de la Tierra en torno a su eje; la convención IERS lo define como una función lineal de `UT1` (S1, ec. 5.14).

💡 **Cómo se explica en la clase [B13-C10](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md):**
- Definir el ángulo de rotación terrestre (ERA) y su fórmula convencional.
- 🎯 **Por qué importa:** Un telescopio en el desierto debe saber cuándo un objeto pasa por su meridiano, que es cuando está más alto y se observa mejor. Esa hora no es la del reloj civil: el cielo se adelanta casi cuatro minutos cada día.
- 🔗 **Se estudia junto con:** UT1, día sidéreo, longitud este, ángulo horario.

📘 **Dónde se aprende** (1 clase): [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md).

### Ángulo de salida

- El ángulo de salida `θ` es la posición de partida en la órbita baja.

💡 **Contexto en la clase [B76-C08](../programa/clases/B76/B76-C08-transferencias-de-baja-energia/CLASE.md):**
- 🎯 **Por qué importa:** Una transferencia de baja energía promete ahorrar propergol a cambio de tiempo, pero ¿qué ahorra y qué no? La decisión central: ¿qué energía hace falta para que una trayectoria pueda pasar por los cuellos de `L1` y `L2`, y qué no explica un modelo sin el Sol?
- 🔗 **Se estudia junto con:** constante de Jacobi, cuello, umbral, transferencia de baja energía.

📘 **Dónde se aprende** (1 clase): [B76-C08 · Transferencias de baja energía](../programa/clases/B76/B76-C08-transferencias-de-baja-energia/CLASE.md).

### Ángulo de transferencia

- El ángulo de transferencia `Δθ` es el que forman `r₁` y `r₂`.

💡 **Cómo se explica en la clase [B75-C04](../programa/clases/B75/B75-C04-ecuacion-de-lambert/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *ficha de un arco de Lambert verificado* para un ángulo de transferencia de tu elección: geometría (`c`, `s`, `a_min`), tabla de `v∞` frente a `Δt`, y las cuatro verificaciones.
- 🎯 **Por qué importa:** Con ventanas fijas solo se calcula el caso ideal. Para cualquier fecha de salida y llegada hace falta resolver la geometría entre dos posiciones.
- 🔗 **Se estudia junto con:** problema de Lambert, cuerda, semiperímetro, variable universal.

📘 **Dónde se aprende** (1 clase): [B75-C04 · Ecuación de Lambert](../programa/clases/B75/B75-C04-ecuacion-de-lambert/CLASE.md).

### Ángulo de trayectoria

- El ángulo de trayectoria `γ` es la inclinación de la entrada.
- El ángulo de trayectoria `γ` es el ángulo bajo el horizonte local.

💡 **Cómo se explica en la clase [B104-C19](../programa/clases/B104/B104-C19-operaciones-de-retorno-y-reintegracion/CLASE.md):**
- Límites: Tierra plana, trayectoria recta, sin calentamiento, sin sustentación, ángulo constante y atmósfera exponencial única.
- 🎯 **Por qué importa:** Un ángulo de entrada más empinado reduce el calentamiento total pero aumenta la desaceleración. La decisión central: ¿cuántos g máximos soporta la tripulación según el ángulo de entrada, y por qué ese máximo no depende de la masa de la nave?
- 🔗 **Se estudia junto con:** reingreso, Allen–Eggers, reintegración.

📘 **Dónde se aprende** (2 clases): [B104-C19 · Operaciones de retorno y reintegración](../programa/clases/B104/B104-C19-operaciones-de-retorno-y-reintegracion/CLASE.md); [B118-C13 · Desorbitación controlada](../programa/clases/B118/B118-C13-desorbitacion-controlada/CLASE.md).

### Ángulo de triangulación

- Tamaño de pixel en el objeto (GSD): `2 d tan(θ)/N`. Ángulo de triangulación: ángulo entre las líneas de vista de dos cámaras.

💡 **Cómo se explica en la clase [B101-C09](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md):**
- Calcular el tamaño de pixel en el objeto y el ángulo de triangulación entre cámaras.
- Ejercicio 4 · autónomo. Ángulo de triangulación entre dos cámaras con líneas de vista `(1, 0, 0)` y `(0, 1, 0)`.
- 🎯 **Por qué importa:** Si el operador no ve el punto de contacto, depende de la imaginación. La decisión central: ¿qué cámaras necesito y dónde para que la zona de trabajo se vea, con qué resolución y sin puntos ciegos críticos?
- 🔗 **Se estudia junto con:** Campo de visión (FOV), Eje óptico, Oclusión, Punto ciego.

📘 **Dónde se aprende** (1 clase): [B101-C09 · Coordinación visual y cámaras en operaciones con manipulador](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md).

### Ángulo de visión

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B28-C12](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md):**
- Esta clase no ajusta ninguna observación: con `Γ = 100`, `θ_c = 0,1 rad` y exponente Doppler `3` (ilustrativos) calcula cómo cae el brillo con el ángulo de visión.
- Para aislar el efecto del ángulo de visión del valor absoluto de la energía.
- 🎯 **Por qué importa:** Un destello gamma débil puede ser un evento normal visto de lado. Un modelo de emisión conjunta permite relacionar qué se ve en cada mensajero con el ángulo de visión.
- 🔗 **Se estudia junto con:** chorro estructurado, núcleo, exponente Doppler, brillo relativo.

📘 **Dónde se aprende** (1 clase): [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md).

### Ángulo entre planos

- El ángulo entre planos al cambiar `Ω` es `θ` con `cos θ = cos² i + sin² i cos ΔΩ`.

💡 **Cómo se explica en la clase [B71-C19](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md):**
- Con `i = 51,6°` (ilustrativa) y `ΔΩ = 10°`, el ángulo entre planos es `θ = 7.8331°`, a pesar de que `ΔΩ = 10°`.
- Calcular el ángulo entre planos al cambiar la RAAN y su costo.
- 🎯 **Por qué importa:** Un cambio de plano mal ubicado puede costar más que todo el resto de la misión orbital. La decisión central: ¿dónde y cómo conviene cambiar el plano para gastar el mínimo `Δv`?
- 🔗 **Se estudia junto con:** cambio de plano puro, impulso combinado, línea de nodos, reparto óptimo.

📘 **Dónde se aprende** (1 clase): [B71-C19 · Cambios de plano simples](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md).

### Ángulo entre vectores

- Geométricamente `u · v = |u||v| cos γ`, donde `γ` es el ángulo entre vectores (entre 0° y 180°).

💡 **Cómo se explica en la clase [B04-C13](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md):**
- *Descripción textual:* de dos vectores unitarios se obtiene su producto escalar, que es el coseno del ángulo entre ellos; si el ángulo no es pequeño se usa arccos, y si es muy pequeño se usa la fórmula por cuerda, que no pierde cifras; el resultado debe quedar entre 0° y 180°.
- Obtener el ángulo entre dos vectores con `arccos` y comprobar su dominio.
- 🎯 **Por qué importa:** Antes de apuntar un telescopio de una estrella a otra, antes de saber si dos objetos caben en el mismo campo de visión, antes de decidir si un planeta está demasiado cerca del Sol para observarlo, hay que saber cuántos grados los separan en el cielo.
- 🔗 **Se estudia junto con:** producto escalar, perpendiculares, proyección, separación angular.

📘 **Dónde se aprende** (1 clase): [B04-C13 · Producto escalar y ángulo entre vectores](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md).

### Ángulo espectral

- El ángulo espectral (SAM) es el ángulo entre dos espectros vistos como vectores; no cambia si un espectro se multiplica por un factor.

💡 **Cómo se explica en la clase [B57-C22](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md):**
- El ángulo espectral entre arcilla y hematita es `9,78°`, entre arcilla y vegetación `19,92°` y entre hematita y vegetación `14,52°`.
- Calcular el ángulo espectral entre dos espectros y su invariancia al brillo.
- 🎯 **Por qué importa:** Dos materiales distintos pueden parecer iguales en cuatro bandas anchas y diferenciarse en cientos de bandas estrechas. La decisión central: ¿cuándo vale la pena el costo en datos de un sensor hiperespectral y cómo se separa una mezcla de materiales?
- 🔗 **Se estudia junto con:** cubo hiperespectral, miembro extremo, desmezclado lineal, abundancias.

📘 **Dónde se aprende** (1 clase): [B57-C22 · Espectrómetros de imagen e hiperespectrales](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md).

### Ángulo espectral (SAM)

- El ángulo espectral (SAM) es `arccos(u·v/(|u||v|))`.

💡 **Cómo se explica en la clase [B53-C29](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md):**
- Los ángulos espectrales entre miembros son `11,3°`, `13,6°` y `9,3°`.
- Calcular el ángulo espectral entre miembros extremos.
- 🎯 **Por qué importa:** Un píxel gris puede ser una mezcla de tres minerales. La decisión central: ¿qué abundancias explican el espectro de un píxel y con qué error, dado el ruido y la similitud entre miembros extremos?
- 🔗 **Se estudia junto con:** miembro extremo, abundancia, mezcla lineal.

📘 **Dónde se aprende** (1 clase): [B53-C29 · Imágenes hiperespectrales de superficies planetarias](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md).

### Ángulo heliocéntrico

- El ángulo heliocéntrico es el ángulo entre las direcciones al Sol de dos planetas medido desde el Sol.

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- Si dibujas las órbitas como circunferencias con el Sol en el centro, la Tierra y Marte son dos puntos y el Sol el tercero: un triángulo con dos lados conocidos (149,6 y 228,0) y el ángulo entre ellos (el ángulo heliocéntrico `φ`).
- Calcular la distancia entre dos planetas en órbitas circulares coplanares según su ángulo heliocéntrico.
- ⚠️ **Error frecuente:** Confundir la elongación con el ángulo heliocéntrico. Se corrige con el ejercicio 3 y la sección 6.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.
- 🔗 **Se estudia junto con:** ley de cosenos, ley de senos, resuelve, LAL.

📘 **Dónde se aprende** (1 clase): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### Ángulo horario

- El ángulo horario `H` es el ángulo, medido hacia el oeste, entre el meridiano y el círculo que pasa por el astro y los polos; vale cero cuando el astro cruza el meridiano (tránsito o culminación, S2).
- La declinación `δ` de un astro es su latitud celeste; el ángulo horario `H` crece con la rotación de la Tierra.
- El ángulo horario `H` de una dirección es el ángulo local menos su ascensión recta: `H = 0` en la culminación.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C04](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md):**
- El intervalo salida–tránsito (5,5 h) supera las 5,3 h porque la Luna avanza hacia el este entre las estrellas (≈ 0,6° por hora) y su ángulo horario crece algo más despacio que el del cielo.
- El ángulo horario es el puente: `H = TSL − α`.
- ⚠️ **Error frecuente:** Confundir el ángulo horario con la AR. Ejercicio 2.
- 🎯 **Por qué importa:** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».
- 🔗 **Se estudia junto con:** altura, distancia cenital, acimut, tránsito.

📘 **Dónde se aprende** (7 clases): [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md); [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B46-C14 · Líneas de base interferométricas](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md); [B48-C04 · Planificación por visibilidad](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md) y 1 más.

### Ángulo isoplanático

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B42-C18](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md):**
- **Idea central (modelo mental):** Como iluminar un escenario con varios focos: cada uno cubre una zona; donde ninguno llega, queda en sombra.
- 🎯 **Por qué importa:** Una sola corrección solo vale dentro del ángulo isoplanático (unos segundos de arco). La decisión central: ¿cómo se amplía el campo y qué parte de la turbulencia queda sin restricción?
- 🔗 **Se estudia junto con:** anisoplanatismo, altura efectiva, MCAO, huella.

📘 **Dónde se aprende** (1 clase): [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### Ángulo paralactico

- La rotación de campo es el giro de la imagen respecto del horizonte; es el ángulo paraláctico `q`.

💡 **Cómo se explica en la clase [B41-C18](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md):**
- Paso 3 · Comprobación. La derivada numérica del ángulo paralactico da `24,4448 "/s` (módulo).
- El script [monturas.py](monturas.py) compara la fórmula de rotación con la derivada numérica del ángulo paralactico y simula el error periódico (comprueba el módulo a `10⁻⁴` y la deriva a 1 %).
- 🎯 **Por qué importa:** La montura decide cuánto tiempo se puede exponer. La decisión central: ¿altazimutal o ecuatorial y qué exposición máxima sin guiado?
- 🔗 **Se estudia junto con:** montura ecuatorial, montura altazimutal, rotación de campo, error periódico.

📘 **Dónde se aprende** (2 clases): [B41-C18 · Monturas y mecanismos de seguimiento](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md); [B43-C13 · Montura altacimutal](../programa/clases/B43/B43-C13-montura-altacimutal/CLASE.md).

### Ángulo polar

- En matemáticas y física se usan el ángulo polar `θ` (desde el eje `z`, de 0° a 180°) y el ángulo azimutal `φ` (en el plano `xy` desde el eje `x`, de 0° a 360°).

💡 **Cómo se explica en la clase [B04-C11](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md):**
- Ángulo polar y azimut: convención matemática; exige no confundir `θ` con `δ`.
- Ejercicio 7. ¿Cuál es el ángulo polar `θ` de Próxima?
- 🎯 **Por qué importa:** Un catálogo de estrellas da para cada una dos números: dónde está en el cielo. Pero un programa que cruza catálogos, calcula separaciones o apunta un telescopio no trabaja con horas y grados: trabaja con vectores.
- 🔗 **Se estudia junto con:** coordenadas esféricas, ángulo azimutal, ascensión recta, declinación.

📘 **Dónde se aprende** (1 clase): [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md).

### Ángulo resonante

- El ángulo resonante `φ` libra alrededor de un valor en la resonancia.

💡 **Cómo se explica en la clase [B72-C11](../programa/clases/B72/B72-C11-resonancias-orbitales-perturbaciones-y-evolucion-de-orbitas/CLASE.md):**
- Para mostrarlo en un sistema real hay que calcular el ángulo resonante con elementos medidos; el laboratorio solo prueba la combinación de movimientos medios.
- Límite: el péndulo es un modelo de una sola resonancia aislada; las resonancias reales se solapan y su ángulo resonante exige elementos que no se calculan aquí.
- 🎯 **Por qué importa:** Una resonancia mantiene a los satélites de Júpiter en equilibrio dinámico y obliga a gestionar un satélite geoestacionario, que se desplaza hacia dos puntos de equilibrio por el campo no esférico.
- 🔗 **Se estudia junto con:** resonancia de movimiento medio, relación de Laplace, péndulo de resonancia, separatriz.

📘 **Dónde se aprende** (1 clase): [B72-C11 · Resonancias orbitales — Perturbaciones y evolución de órbitas](../programa/clases/B72/B72-C11-resonancias-orbitales-perturbaciones-y-evolucion-de-orbitas/CLASE.md).

### Ángulo sólido

- El ángulo sólido mide la extensión de cielo.
- El ángulo sólido del cono.

💡 **Cómo se explica en la clase [B41-C10](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md):**
- Verificar con una integral del ángulo sólido.
- 🎯 **Por qué importa:** La relación focal decide si un telescopio es «rápido» o «lento». La decisión central: ¿qué importa más, el diámetro o la relación focal?
- 🔗 **Se estudia junto con:** relación focal, área colectora, magnitud límite, brillo superficial.

📘 **Dónde se aprende** (2 clases): [B41-C10 · Apertura y relación focal](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md); [B118-C16 · Contaminación lumínica](../programa/clases/B118/B118-C16-contaminacion-luminica/CLASE.md).

### Ángulo sólido del haz

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B46-C05](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md):**
- **Idea central (modelo mental):** Si la linterna ilumina solo parte del cuadro, la lectura promedia la zona luminosa con la oscura; la dilución es esa fracción.
- 🎯 **Por qué importa:** Para saber cuánto flujo hay en una fuente hay que conocer cuánta fracción del haz llena. La decisión central: ¿cuánto vale la temperatura de antena de una fuente extensa en un haz dado?
- 🔗 **Se estudia junto con:** temperatura de antena, área efectiva, sensibilidad, dilución del haz.

📘 **Dónde se aprende** (1 clase): [B46-C05 · Ganancia y temperatura de antena](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md).

### Ángulos de Euler

- Los ángulos de Euler son tres rotaciones sucesivas alrededor de ejes del cuerpo (o fijos) que componen una orientación.

💡 **Cómo se explica en la clase [B10-C14](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md):**
- Paso 5 · Sentido. La singularidad está en la representación, no en el satélite: el movimiento es suave, pero los ángulos de Euler no pueden seguirlo.
- Ángulos de Euler: intuitivos, singulares.
- 🎯 **Por qué importa:** Un satélite que apunta una antena al cenit tiene el cabeceo cerca de `90°`; si la actitud se guarda con ángulos de Euler, justo ahí el cálculo se vuelve inestable: ángulos que cambian muy rápido para movimientos pequeños, o dos conjuntos de ángulos distintos para la misma orientación.
- 🔗 **Se estudia junto con:** tipo Tait–Bryan, Euler propio, guiñada, cabeceo.

📘 **Dónde se aprende** (1 clase): [B10-C14 · Ángulos de Euler y singularidades](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md).

### Ángulos de Euler 3-2-1

- Los ángulos de Euler 3-2-1 son *yaw* (eje z), *pitch* (eje y) y *roll* (eje x): `A = Rx(roll) Ry(pitch) Rz(yaw)`.

💡 **Cómo se explica en la clase [B87-C02](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md):**
- *Descripción textual:* la rotación es una sola; la matriz y el cuaternión se convierten sin pérdida, el eje-ángulo es una lectura geométrica del cuaternión y Euler es la forma legible pero singular; el producto de cuaterniones compone rotaciones.
- Analogía: una misma dirección puede darse como «40° al noreste» (Euler), como un vector (matriz) o como una brújula con un giro (eje-ángulo); cada forma es buena para algo.
- 🎯 **Por qué importa:** Casi todos los errores de actitud en software vienen de convenciones mezcladas: orden de ejes, sentido de la rotación, posición de la parte escalar. La decisión central: ¿qué representación uso para integrar, cuál para filtrar y cuál para mostrar?
- 🔗 **Se estudia junto con:** matriz de actitud, cuaternión, eje-ángulo, doble cobertura.

📘 **Dónde se aprende** (1 clase): [B87-C02 · Representaciones de orientación](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md).

### Anidamiento

- El anidamiento deja que una prioridad mayor interrumpa a una menor.

💡 **Cómo se explica en la clase [B88-C22](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md):**
- Con un marco por nivel (32 + 48 + 40 = 120 B), cualquier combinación de anidamientos cabe: observado `80 ≤ 120 B`.
- Q -->|si| P{"Prioridad mayor y anidamiento?"}
- 🎯 **Por qué importa:** Las interrupciones fijan cuánto tarda el sistema en reaccionar y cuánta pila usa. La decisión central: ¿se permite que una interrupción de mayor prioridad interrumpa a otra, y qué cuesta eso en latencia y pila?
- 🔗 **Se estudia junto con:** latencia, tiempo de respuesta, pila máxima, cota de pila.

📘 **Dónde se aprende** (1 clase): [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md).

### Anillo

- El anillo es el conjunto de direcciones con la misma diferencia de tiempo.
- Un anillo es un disco delgado de partículas.
- La malla completa tiene `n(n−1)/2` enlaces; el anillo, `n`; la estrella, `n − 1`.

💡 **Cómo se explica en la clase [B28-C10](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md):**
- Con dos detectores la fuente está sobre un anillo ancho; un tercero añade otro anillo y la intersección reduce el área a dos manchas simétricas respecto del plano de los detectores.
- 🎯 **Por qué importa:** El área de localización decide cuántas fotos hacen falta para encontrar la contrapartida. Un mapa mal calibrado engaña.
- 🔗 **Se estudia junto con:** tiempo de llegada, línea de base, rejilla de Fibonacci, región creíble.

📘 **Dónde se aprende** (3 clases): [B28-C10 · Localización probabilística de eventos](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md); [B52-C12 · Anillos planetarios](../programa/clases/B52/B52-C12-anillos-planetarios/CLASE.md); [B88-C31 · Topologías de red de datos a bordo](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md).

### Anillo atmosférico

- El anillo atmosférico tiene espesor `NH`.

💡 **Contexto en la clase [B29-C11](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md):**
- **Idea central (modelo mental):** Una moneda con un halo borroso tapa un poco más que la moneda sola. El ancho del halo es el espesor de la atmósfera efectiva, de unas cuantas alturas de escala.
- 🎯 **Por qué importa:** Los planetas inflados y calientes tienen señales de cientos de ppm; las Tierras alrededor de estrellas como el Sol, de ~1 ppm, que no se alcanzan. La decisión central: ¿qué señal produce una atmósfera dada y cuántos tránsitos hacen falta para verla?
- 🔗 **Se estudia junto con:** altura de escala, masa molecular media, señal de transmisión, detección a 5σ.

📘 **Dónde se aprende** (1 clase): [B29-C11 · Atmósferas exoplanetarias](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md).

### Anillo de apoyo

- El anillo de apoyo de radio `b`.

💡 **Cómo se explica en la clase [B43-C08](../programa/clases/B43/B43-C08-montaje-de-espejo-primario/CLASE.md):**
- *Descripción textual:* el apoyo fija el desplazamiento; al quitar piston y desenfoque el residuo depende del radio del anillo.
- 🎯 **Por qué importa:** Un apoyo mal elegido deja un error de forma que ninguna pieza posterior corrige. La decisión central: ¿en qué radio conviene apoyar el espejo para que, tras quitar piston y desenfoque, quede el menor error?
- 🔗 **Se estudia junto con:** energía de Kirchhoff, base polinómica, sistema KKT, error residual.

📘 **Dónde se aprende** (1 clase): [B43-C08 · Montaje de espejo primario](../programa/clases/B43/B43-C08-montaje-de-espejo-primario/CLASE.md).

### Anillo de cielo

- El anillo de cielo da el fondo.

💡 **Cómo se explica en la clase [B45-C23](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md):**
- El anillo de cielo (12 a 19 píxeles) tiene 692 píxeles.
- Un anillo de 3 a 6 píxeles, cerca de la estrella, sobreestima el cielo en `32,64 e⁻/píxel`, lo que quita el `61,0 %` del flujo en una apertura de 1,5 FWHM.
- 🎯 **Por qué importa:** Una apertura pequeña pierde flujo y una grande añade ruido de cielo. La decisión central: ¿qué radio da el mejor S/N y cómo se mide el cielo?
- 🔗 **Se estudia junto con:** apertura, fracción encerrada, mediana, contaminación.

📘 **Dónde se aprende** (1 clase): [B45-C23 · Fotometría de apertura y estimación del cielo](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md).

### Anillo de eventos

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C06](../programa/clases/B47/B47-C06-instrumentos-de-rayos-gamma/CLASE.md):**
- **Idea central (modelo mental):** Un fotón Compton es una bola de billar que golpea otra en reposo: la energía que pierde fija el ángulo del choque, y al medir las dos energías se despeja de dónde venía.
- 🎯 **Por qué importa:** Cada proceso (Compton, pares) domina a una energía distinta y fija el tipo de instrumento. La decisión central: ¿qué proceso usa el detector y con qué incertidumbre angular reconstruye la dirección?
- 🔗 **Se estudia junto con:** dispersión Compton, sección eficaz de Klein-Nishina, sección eficaz de Thomson, producción de pares.

📘 **Dónde se aprende** (1 clase): [B47-C06 · Instrumentos de rayos gamma](../programa/clases/B47/B47-C06-instrumentos-de-rayos-gamma/CLASE.md).

### Anillo de fondo

- Una apertura es el conjunto de píxeles que se suman para medir una estrella y un anillo de fondo el conjunto alrededor que estima el cielo.

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- Se suman los píxeles de una apertura de radio 5 px (81 píxeles) y se resta el fondo estimado como la mediana de un anillo (de 8 a 12 píxeles de radio): `F = Σ_ap (I − fondo)`.
- Medir el flujo de una estrella con una apertura y un anillo de fondo.
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.
- 🔗 **Se estudia junto con:** imagen digital, píxel, ADU, ganancia.

📘 **Dónde se aprende** (1 clase): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md).

### Anillo E

- El anillo E es el anillo de Saturno formado por material del penacho.

💡 **Cómo se explica en la clase [B56-C10](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md):**
- C -- "no" --> E["Escapa:<br/>alimenta el anillo E"]
- Modelo con gas, rotación y Saturno: necesario para predecir el anillo E.
- 🎯 **Por qué importa:** El penacho permite muestrear un océano sin aterrizar. Para diseñar un sobrevuelo hace falta saber hasta dónde llegan los granos y cuáles escapan al anillo E.
- 🔗 **Se estudia junto con:** penacho, velocidad de escape, apogeo, balística radial.

📘 **Dónde se aprende** (1 clase): [B56-C10 · Océanos de Encélado](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md).

### Anión

- Un ion es un átomo o grupo con carga neta: un catión (positivo) pierde electrones; un anión (negativo) los gana.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- Pregunta: un par catión +1 / anión −1 a 0,30 nm (distancia sintética), ¿resiste la agitación térmica a 176 K, la temperatura del eutéctico NH₃–H₂O (S1)?
- En una sal, el NH₄⁺ está unido electrostáticamente a un anión (por ejemplo formiato) en un sólido; para escapar tendría que romper una atracción de varios eV.
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).
- 🔗 **Se estudia junto con:** electrones de valencia, regla del octeto, ion, catión.

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Aniquilación

- La aniquilación electrón–positrón convierte sus masas en fotones.
- La aniquilación convierte materia y antimateria en radiación.
- La aniquilación `e⁺e⁻ → γγ`.

💡 **Cómo se explica en la clase [B26-C05](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md):**
- Calcular la energía de un balance de masas (aniquilación, fusión, fusión de agujeros negros).
- Ejercicio 6. ¿Qué energía lleva cada fotón en la aniquilación en reposo de `e⁺e⁻`?
- 🎯 **Por qué importa:** El Sol, un acelerador de partículas y la fusión de dos agujeros negros son balances de masa y energía. Para calcularlos hay que saber cuánta energía tiene una partícula en reposo y en movimiento, y por qué no puede acelerarse hasta `c`.
- 🔗 **Se estudia junto con:** energía de reposo, energía total, momento relativista, energía cinética.

📘 **Dónde se aprende** (3 clases): [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md); [B31-C12 · Antimateria y aniquilación](../programa/clases/B31/B31-C12-antimateria-y-aniquilacion/CLASE.md); [B40-C03 · Desacoplamiento de neutrinos y fondo cósmico de neutrinos](../programa/clases/B40/B40-C03-desacoplamiento-de-neutrinos-y-fondo-cosmico-de-neutrinos/CLASE.md).

### Anisoplanatismo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C18](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md):**
- *Descripción textual:* el anisoplanatismo crece como `(θ/θ₀)^{5/3}`; la MCAO lo reduce hasta que la huella queda fuera de las guías.
- 🎯 **Por qué importa:** Una sola corrección solo vale dentro del ángulo isoplanático (unos segundos de arco). La decisión central: ¿cómo se amplía el campo y qué parte de la turbulencia queda sin restricción?
- 🔗 **Se estudia junto con:** ángulo isoplanático, altura efectiva, MCAO, huella.

📘 **Dónde se aprende** (1 clase): [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### Anisotropía

- La anisotropía es su pequeña variación de temperatura, del orden de `10⁻⁵`.

💡 **Cómo se explica en la clase [B26-C15](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md):**
- Límites: cuerpo negro perfecto, sin anisotropías ni distorsiones.
- 🎯 **Por qué importa:** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.
- 🔗 **Se estudia junto con:** función de Planck, densidad numérica de fotones, frecuencia del máximo, energía media.

📘 **Dónde se aprende** (1 clase): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### Anodizado

- El anodizado genera óxido: `espesor = η j t M_ox/(3Fρ_ox)`.

💡 **Cómo se explica en la clase [B84-C34](../programa/clases/B84/B84-C34-tratamientos-y-recubrimientos-superficiales-de-componentes-espaciales/CLASE.md):**
- *Descripción textual:* `α`, `ε` y `S` dan la temperatura de equilibrio, comprobada con el balance; la degradación la desplaza; el anodizado se calcula aparte con Faraday.
- Una placa con la cara al Sol (`S = 1361 W/m²`, ilustrativo) alcanza `14,2 °C` con pintura blanca (`α/ε = 0,284`), `125,8 °C` con pintura negra, `283,5 °C` con aluminio pulido, `47,0 °C` con aluminio anodizado, `426,8 °C` con oro y `−51,8 °C` con un reflector solar óptico.
- 🎯 **Por qué importa:** Cambiar el recubrimiento de una placa de aluminio cambia su temperatura de equilibrio en 400 K; la degradación en órbita lo desplaza decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la temperatura de una superficie en su rango y qué espesor de anodizado se necesita?
- 🔗 **Se estudia junto con:** temperatura de equilibrio, razón, OSR.

📘 **Dónde se aprende** (1 clase): [B84-C34 · Tratamientos y recubrimientos superficiales de componentes espaciales](../programa/clases/B84/B84-C34-tratamientos-y-recubrimientos-superficiales-de-componentes-espaciales/CLASE.md).

### Anomalía

- Una anomalía es una observación que no se parece a lo esperado según un modelo de lo normal.
- Anomalía: desvío de lo esperado.
- Una anomalía pierde el día.

💡 **Cómo se explica en la clase [B17-C05](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md):**
- El parámetro de contaminación (fracción esperada de anomalías) fija el umbral por percentil: con contaminación 0,01 y 5000 puntos marcaría 50.
- La documentación de scikit-learn distingue dos tareas: la detección de valores atípicos, donde los datos de entrenamiento ya contienen anomalías y el método ajusta las zonas densas, y la detección de novedades, donde el entrenamiento es limpio y se busca marcar observaciones nuevas que se desvían (S1).
- ⚠️ **Error frecuente:** Entrenar con anomalías y llamarlo novedades. Ejercicio 8.
- 🎯 **Por qué importa:** El subsistema térmico de un satélite entrega temperatura y corriente. Cada una, por separado, puede estar dentro de su rango normal y sin embargo la pareja ser imposible: la corriente alta con temperatura baja no ocurre nunca en operación sana.
- 🔗 **Se estudia junto con:** distancia de Mahalanobis, distribución chi-cuadrado, bosque de aislamiento, falsa alarma.

📖 **Explicado a fondo:** [Anomalía y ecuación de Kepler](esencial/tercera-a-e.md#anomalía-y-ecuación-de-kepler) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md); [B96-C13 · Detección de anomalías](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md); [B97-C20 · Misión robótica integrada simulada](../programa/clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md).

### Anomalía de altura

- La anomalía de altura `η` es la altura respecto de una referencia.

💡 **Contexto en la clase [B57-C12](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md):**
- **Idea central (modelo mental):** Una loma de agua debería deslizarse, pero la rotación terrestre desvía el flujo y lo hace circular alrededor de la loma: la pendiente da la velocidad.
- 🎯 **Por qué importa:** El océano se mueve lento y se eleva más lento aún. La decisión central: ¿qué pendiente de la superficie equivale a una corriente y cuántos años de datos se necesitan para ver una tendencia de pocos milímetros por año entre un ruido de centímetros?
- 🔗 **Se estudia junto con:** balance geostrófico, número de Rossby, tendencia, ciclo anual.

📘 **Dónde se aprende** (1 clase): [B57-C12 · Oceanografía desde órbita](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md).

### Anomalía estandarizada

- La anomalía estandarizada `z = (x − μ)/σ` mide cuántas desviaciones se aleja un valor del promedio.

💡 **Cómo se explica en la clase [B57-C15](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md):**
- La anomalía estandarizada supone distribución normal, que no vale para lluvias muy sesgadas.
- 🎯 **Por qué importa:** Las agencias necesitan mapas de inundación en horas y alertas de sequía en meses. La decisión central: ¿cómo se fija el umbral entre agua y tierra sin fijarlo a ojo, y cómo se declara que un año es seco?
- 🔗 **Se estudia junto con:** índice de agua, umbral de Otsu, máscara, sequía.

📘 **Dónde se aprende** (1 clase): [B57-C15 · Sequías e inundaciones](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md).

### Anomalía excéntrica

- La anomalía excéntrica `E` es un ángulo auxiliar que cumple la ecuación de Kepler, `M = E − e sen E`.
- La anomalía excéntrica `E` es un ángulo auxiliar que sitúa al planeta en la elipse.
- La anomalía excéntrica `E` y la media `M = E − e sin E`.

💡 **Cómo se explica en la clase [B02-C14](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md):**
- *Descripción textual:* con `a`, `e` y `T` se calcula la anomalía media en cada instante; se resuelve la ecuación de Kepler para hallar la anomalía excéntrica; de ella salen las coordenadas; y se comprueban las leyes de las áreas y del período.
- 🎯 **Por qué importa:** Para Kepler, como para todos antes, el círculo era la figura natural del cielo. Los datos de Tycho no se dejaban describir con círculos.
- 🔗 **Se estudia junto con:** semieje mayor, excentricidad, perihelio, afelio.

📘 **Dónde se aprende** (3 clases): [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B71-C14 · Ecuación de Kepler](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md).

### Anomalía magnética

- Una anomalía magnética es la diferencia entre el campo observado y el campo de referencia.

💡 **Cómo se explica en la clase [B65-C03](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md):**
- La evidencia es la ficha de la anomalía magnética del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de la anomalía magnética*: `m`, pico, ajuste con error, caída con la altura y profundidad de Curie.
- 🎯 **Por qué importa:** La corteza magnetizada permite reconstruir campos de cuerpos que hoy no tienen dinamo. La decisión central: ¿qué parte de un mapa de anomalías es información sobre la magnetización y qué parte es ambigüedad geométrica?
- 🔗 **Se estudia junto con:** magnetización remanente, temperatura de Curie, momento magnético, profundidad de Curie.

📘 **Dónde se aprende** (1 clase): [B65-C03 · Magnetismo cortical remanente y anomalías magnéticas](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md).

### Anomalía media

- La anomalía media `M = 2π t/T` crece de manera uniforme con el tiempo.
- La anomalía media `M` crece uniformemente con el tiempo, `M = n t`, con `n` el movimiento medio.
- La anomalía media `M = 2π(t − t₀)/P`.

💡 **Cómo se explica en la clase [B02-C14](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md):**
- La anomalía media crece de manera uniforme: `M = 2π t/T`.
- A["Parámetros:<br/>a, e, T"] --> B["Tiempo t → anomalía media<br/>M = 2π t / T"]
- 🎯 **Por qué importa:** Para Kepler, como para todos antes, el círculo era la figura natural del cielo. Los datos de Tycho no se dejaban describir con círculos.
- 🔗 **Se estudia junto con:** semieje mayor, excentricidad, perihelio, afelio.

📘 **Dónde se aprende** (3 clases): [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B29-C03 · Velocidad radial estelar](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md).

### Anomalía verdadera

- La anomalía verdadera es el ángulo `θ` de un cuerpo en órbita medido desde el perihelio, con el Sol en el origen.
- La anomalía verdadera `ν` es el ángulo real desde el periapsis.

💡 **Contexto en la clase [B04-C10](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md):**
- **Idea central (modelo mental):** Las cartesianas piden «cuánto a la derecha y cuánto arriba». Las polares piden «cuánto lejos y en qué dirección». El mismo punto tiene los dos pares de valores.
- 🎯 **Por qué importa:** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.
- 🔗 **Se estudia junto con:** coordenadas cartesianas, coordenadas polares, polo, eje polar.

📘 **Dónde se aprende** (2 clases): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md); [B71-C13 · Anomalías orbitales](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md).

### Anomalía/discrepancia

- Anomalía/discrepancia: variación frente a lo esperado.

💡 **Contexto en la clase [B90-C17](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md):**
- 🎯 **Por qué importa:** Una falla única en 500 horas de ensayo no demuestra que el equipo sea confiable: solo acota la tasa de fallas. Y una anomalía mal registrada se pierde.
- 🔗 **Se estudia junto con:** No conformidad, Disposición, Severidad, Causa raíz.

📘 **Dónde se aprende** (1 clase): [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md).

### Anotador

- Un anotador es quien etiqueta.

💡 **Cómo se explica en la clase [B17-C10](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md):**
- Sin protocolo, las diferencias entre anotadores serán más diferencias de interpretación que de atención.
- Con dos anotadores que aciertan cada uno con probabilidad `p = 0,8` e independientes, ambos coinciden si los dos aciertan o los dos fallan (en el caso binario eso lleva a la misma etiqueta): `pₒ = p² + (1 − p)² = 0,64 + 0,04 = 0,68`.
- 🎯 **Por qué importa:** Se quiere entrenar un modelo que distinga galaxias espirales de elípticas. Hay un millón de imágenes y nadie las ha etiquetado.
- 🔗 **Se estudia junto con:** protocolo de etiquetado, acuerdo observado, acuerdo esperado por azar, kappa de Cohen.

📘 **Dónde se aprende** (1 clase): [B17-C10 · Conjuntos de datos etiquetados para aprendizaje supervisado](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md).

### Antena de referencia

- La antena de referencia (fase 0).

💡 **Cómo se explica en la clase [B51-C03](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md):**
- Resolver amplitud y fase por separado con ajuste logarítmico y antena de referencia.
- 🎯 **Por qué importa:** Sin ganancias el conjunto de datos no sirve para formar imágenes. La decisión central: ¿cómo se estiman las ganancias a partir de un modelo de cielo conocido y qué precisión se alcanza?
- 🔗 **Se estudia junto con:** ecuación de medida, ganancia compleja, mínimos cuadrados alternados, modelo de cielo.

📘 **Dónde se aprende** (1 clase): [B51-C03 · Ganancias complejas por antena y soluciones de calibración](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md).

### Antes

- El de ventana también reinicia si la patada llega antes de `t_min`.

💡 **Cómo se explica en la clase [B88-C11](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md):**
- Analogía: un watchdog de ventana es como un guardia que exige que lo saludes cada hora, ni antes de los 40 minutos ni después de los 80.
- Una patada adelantada por un lazo desbocado (antes de `t_min`).
- 🎯 **Por qué importa:** Un watchdog mal ajustado reinicia sin necesidad o no reinicia cuando hace falta. La decisión central: ¿qué ventana y qué escalera de acciones recuperan un software colgado sin reinicios falsos?
- 🔗 **Se estudia junto con:** watchdog simple, de ventana, reinicio falso, escalera de recuperación.

📘 **Dónde se aprende** (1 clase): [B88-C11 · Watchdogs y recuperación](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md).

### Anticonmutativo

- Es anticonmutativo: `v × u = −(u × v)`.

💡 **Contexto en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- **Idea central (modelo mental):** Un cuerpo que gira en un plano define un eje perpendicular a él. La regla de la mano derecha dice hacia qué lado apunta ese eje: si los dedos siguen el giro, el pulgar marca la normal. Cambiar el sentido del giro invierte la normal.
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?
- 🔗 **Se estudia junto con:** producto vectorial, regla de la mano derecha, normal a un plano, normal unitaria.

📘 **Dónde se aprende** (1 clase): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md).

### Antiderivada

- Una antiderivada de `f` es una función `F` tal que `F′ = f`.

💡 **Cómo se explica en la clase [B09-C08](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md):**
- Si `F` es antiderivada, también lo es `F + C`.
- Con `f = 2 sin x cos x`, tanto `sin² x` como `−cos² x` son antiderivadas, y difieren en la constante `1`, porque `sin² + cos² = 1`.
- 🎯 **Por qué importa:** Un acelerómetro mide aceleración; lo que se necesita es velocidad y posición. Una gravedad `g(r)` se conoce; lo que decide si una sonda escapa es la energía, que sale de «deshacer» esa derivada.
- 🔗 **Se estudia junto con:** integral indefinida, constante de integración, condición inicial, potencial gravitatorio.

📘 **Dónde se aprende** (1 clase): [B09-C08 · Integrales indefinidas](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md).

### Antidisipativo

- Un método es disipativo si reduce la energía y antidisipativo si la aumenta.

💡 **Cómo se explica en la clase [B11-C10](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md):**
- Es antidisipativo y no sirve para ninguna propagación seria.
- 🎯 **Por qué importa:** Un análisis de misión puede necesitar propagar un satélite durante años, es decir, decenas de miles de vueltas. Si cada vuelta añade o quita un poco de energía, la altura de la órbita cambia solo por culpa del programa.
- 🔗 **Se estudia junto con:** cantidad conservada, deriva, secular, acotada u oscilante.

📘 **Dónde se aprende** (1 clase): [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md).

### Antigüedad

- La antigüedad es `ahora − instante efectivo`.

💡 **Cómo se explica en la clase [B116-C07](../programa/clases/B116/B116-C07-diseno-de-paneles-de-monitoreo-de-salud/CLASE.md):**
- La antigüedad es `ahora − efectivo`; el retardo de comunicaciones ya está en ese desfase.
- El campo `effective` de una observación FHIR es el instante clínicamente relevante; la antigüedad se calcula contra ese instante y no contra el de recepción.
- ⚠️ **Error frecuente:** Mostrar el último valor sin su edad. Calcula y muestra la antigüedad (8.3).
- 🎯 **Por qué importa:** Un panel que muestra «FC 72» sin decir de cuándo es, o que usa un gris que no se lee, puede ser peor que no tener panel. La decisión central: ¿qué debe mostrar un panel de salud para que quien lo mira sepa qué está pasando, cuán fresco es el dato y a quién atender primero?
- 🔗 **Se estudia junto con:** panel, razón de contraste, luminancia relativa, Obsoleto.

📘 **Dónde se aprende** (1 clase): [B116-C07 · Diseño de paneles de monitoreo de salud](../programa/clases/B116/B116-C07-diseno-de-paneles-de-monitoreo-de-salud/CLASE.md).

### Antisimétrica

- Una matriz antisimétrica cumple `Kᵀ = −K`; la del eje unitario `u` es `K = [[0, −u₃, u₂], [u₃, 0, −u₁], [−u₂, u₁, 0]]` y cumple `K v = u × v`.

💡 **Contexto en la clase [B10-C13](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md):**
- **Idea central (modelo mental):** Una matriz de rotación dice dónde caen los tres ejes del cuerpo: su primera columna es el eje `x` del cuerpo en el sistema inercial, la segunda el `y`, la tercera el `z`.
- 🎯 **Por qué importa:** La actitud de un satélite (hacia dónde apuntan sus ejes) se guarda como una matriz de rotación: sus columnas son los ejes del cuerpo expresados en el sistema inercial. Con ella, un seguidor estelar, un panel o una antena se orientan sin ambigüedad.
- 🔗 **Se estudia junto con:** rotaciones elementales, grupo SO(3), fórmula de Rodrigues, matriz de transformación de marco.

📘 **Dónde se aprende** (1 clase): [B10-C13 · Matrices de rotación tridimensional](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md).

### Anti-windup

- El anti-windup es cualquier mecanismo que lo evita.
- El antiwindup detiene la integral cuando el actuador satura.

💡 **Cómo se explica en la clase [B16-C18](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md):**
- Sin anti-windup, `ξ̇ = e` todo el tiempo, también durante la saturación.
- Resultado: la integral máxima es 0,099 rad·s (frente a 5,29), el sobreimpulso baja a 0,8 % y el asentamiento (2 %) a 40,9 s (frente a 61,9 s sin anti-windup).
- ⚠️ **Error frecuente:** Medir el anti-windup solo en el caso saturado. Se corrige con el ejercicio 6 y la sección 8.4.
- 🎯 **Por qué importa:** Una rueda de reacción entrega un par máximo y almacena un momento angular máximo (el Hubble usa ruedas de hasta unas 3000 rpm, y magnetopares para gestionar su velocidad, S1). Cuando el controlador pide más de lo que el actuador puede dar, el lazo deja de comportarse como se diseñó.
- 🔗 **Se estudia junto con:** saturación, windup, recálculo hacia atrás, integración condicional.

📘 **Dónde se aprende** (2 clases): [B16-C18 · Saturación y anti-windup](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md); [B85-C10 · Control térmico activo](../programa/clases/B85/B85-C10-control-termico-activo/CLASE.md).

### Antropometría

- La antropometría mide las dimensiones del cuerpo.

💡 **Cómo se explica en la clase [B109-C06](../programa/clases/B109/B109-C06-antropometria-y-dimensionamiento-para-tripulacion/CLASE.md):**
- Con `g = 1,62 m/s²` (NASA/NSSDC) la gravedad parcial permite posturas verticales y movimientos que en microgravedad no existen, y por eso la antropometría de microgravedad no se traslada sin revisión.
- El concepto de hábitat lunar de NASA (Burke et al., 2022) define sus volúmenes funcionales con la antropometría del percentil 99 de hombres y mujeres y una altura estándar de `2,4 m`; el volumen de sueño es de `1 m` de altura y la longitud del cuerpo manda sobre la litera.
- 🎯 **Por qué importa:** Si se dimensiona para la media, la mitad de las personas no cabe o no alcanza. La decisión central: ¿qué percentil de qué población usar para cada dimensión?
- 🔗 **Se estudia junto con:** percentil, holgura, alcance, intervalo de diseño.

📘 **Dónde se aprende** (1 clase): [B109-C06 · Antropometría y dimensionamiento para tripulación](../programa/clases/B109/B109-C06-antropometria-y-dimensionamiento-para-tripulacion/CLASE.md).

### Anular

- Un eclipse solar es total si la Luna cubre por completo el Sol; anular si la Luna parece más pequeña que el Sol y deja un anillo brillante;

💡 **Cómo se explica en la clase [B08-C09](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md):**
- En 2025 la distancia varió entre 356 830 y 406 690 km (S2): cerca del perigeo un eclipse central sería total, cerca del apogeo, anular.
- Pausa. El 21 de septiembre de 2025 la Luna estaba a 396 872 km; si el eclipse hubiese sido central, ¿habría sido total o anular? <details><summary>Respuesta</summary>`396 872 > 380 909 km`: el vértice no llega: anular.</details>
- ⚠️ **Error frecuente:** Creer que un eclipse anular es seguro a simple vista. Ejercicio 10.
- 🎯 **Por qué importa:** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?
- 🔗 **Se estudia junto con:** umbra, penumbra, solar, lunar.

📘 **Dónde se aprende** (1 clase): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md).

### Año juliano

- El año juliano es, por convención del programa, 365,25 d.

💡 **Cómo se explica en la clase [B03-C08](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md):**
- Ejercicio 4. Convierte el período de Mercurio, 87,969 d, a segundos y a años julianos.
- Predice antes de ejecutar: ¿cuántos años julianos dura una vuelta de Neptuno?
- 🎯 **Por qué importa:** El período de Neptuno en las fichas de la NASA es 60 189,018 días. Nadie piensa en 60 mil días; se piensa en años.
- 🔗 **Se estudia junto con:** segundo, minuto, hora, día.

📘 **Dónde se aprende** (1 clase): [B03-C08 · Tiempo y conversiones astronómicas](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md).

### Año luz

- El año luz (ly) es la distancia que la luz recorre en un año juliano.

💡 **Cómo se explica en la clase [B01-C02](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md):**
- El script [escalera_de_escalas.py](escalera_de_escalas.py) imprime la tabla de la sección 12 a partir de valores publicados y comprueba antes las constantes con pruebas: que el parsec valga `648 000/π` au, que un año luz mida lo que debe, que la luz del Sol tarde 499,0 s y que el cociente Sol/Tierra sea 109.
- 🎯 **Por qué importa:** Cuando alguien dice que Próxima Centauri está «a cuatro años luz» y que Andrómeda está «a dos millones y medio», es fácil oír solo «lejos» y «más lejos». Pero entre una y otra hay un factor de casi seis cien mil.
- 🔗 **Se estudia junto con:** orden de magnitud, notación científica, logaritmo decimal, cociente.

📘 **Dónde se aprende** (1 clase): [B01-C02 · Escalas desde la Tierra al cosmos observable](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md).

### Año luz (ly)

- El año luz (ly) es la distancia que recorre la luz en el vacío en un año juliano de 365,25 días.

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- El año luz es `c × 1 año juliano = 299 792 458 m/s × 31 557 600 s = 9 460 730 472 580 800 m`, es decir, `9,4607 × 10¹⁵ m = 63 241,1 au`.
- AU -->|"× 1 ly / 63 241,1 au"| LY["año luz (ly)"]
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.
- 🔗 **Se estudia junto con:** Sistema Internacional (SI), unidades base, unidad derivada, unidad no SI aceptada.

📘 **Dónde se aprende** (1 clase): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md).

### Año sidéreo

- El año sidéreo es el período orbital de la Tierra respecto de las estrellas (365,256 días), mientras que el año trópico (365,242 días) se mide respecto de las estaciones (S2).

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- El día solar dura 24,0000 h porque lo medimos de mediodía a mediodía; el día sidéreo dura 23,9345 h, porque lo medimos respecto de las estrellas (S2).
- Eso significa que en un año sidéreo la Tierra da una vuelta más sobre su eje respecto de las estrellas que días solares ha contado: `365,256 × 24/23,9345 = 366,26` días sidéreos frente a 365,256 días solares.
- ⚠️ **Error frecuente:** Mezclar día solar y sidéreo. Se piensa que las estrellas salen a la misma hora cada noche.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).
- 🔗 **Se estudia junto con:** ciclo, período, día solar medio, día sidéreo.

📖 **Explicado a fondo:** [Año tropical y año sidéreo](esencial/cuarta-fundamentos.md#año-tropical-y-año-sidéreo) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md).

### Año trópico

- El año sidéreo es el período orbital de la Tierra respecto de las estrellas (365,256 días), mientras que el año trópico (365,242 días) se mide respecto de las estaciones (S2).
- Un año trópico es el ciclo de las estaciones (365,242 días, S2); un mes sinódico es el ciclo de las fases de la Luna (29,53 días, S3).

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- El ciclo natural (día, mes, año) es fácil de observar pero cambia según el modo de medirlo: día solar o sidéreo, año sidéreo o trópico.
- Ejercicio 6. El año juliano son 365,25 d; el trópico, 365,242 d.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).
- 🔗 **Se estudia junto con:** ciclo, período, día solar medio, día sidéreo.

📘 **Dónde se aprende** (2 clases): [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B02-C01 · Calendarios astronómicos en civilizaciones antiguas](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md).

### AoS

- Un paso (*stride*) es el salto en bytes entre elementos consecutivos de un eje. AoS (arreglo de estructuras) guarda registros completos uno tras otro;

💡 **Cómo se explica en la clase [B18-C03](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md):**
- Sumar solo `x` en AoS salta 32 B entre valores: cada línea de 64 B trae 2 valores de `x` y 6 de otros campos que no se usan.
- AoS cuando se usan todos los campos del mismo registro juntos.
- 🎯 **Por qué importa:** Un catálogo con millones de estrellas o una rejilla de simulación pasan cada dato por la CPU una o pocas veces. Cuando las operaciones por dato son pocas, el tiempo no lo fija la CPU sino el viaje de los datos.
- 🔗 **Se estudia junto con:** jerarquía de memoria, caché, línea de caché, localidad espacial.

📘 **Dónde se aprende** (1 clase): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md).

### AOS/LOS

- Holgura: `LS − ES`. AOS/LOS: inicio y fin del contacto.

💡 **Contexto en la clase [B96-C09](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md):**
- 🎯 **Por qué importa:** Una secuencia que no cabe en la ventana deja comandos sin ejecutar o telemetría sin confirmar. La decisión central: ¿qué actividades fijan la duración mínima y cuánta holgura queda?
- 🔗 **Se estudia junto con:** Secuencia, Camino crítico, ES/EF, LS/LF.

📘 **Dónde se aprende** (1 clase): [B96-C09 · Secuencias de misión](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md).

### AP

- El AP es el área bajo la curva precisión-exhaustividad con la precisión interpolada.

💡 **Cómo se explica en la clase [B103-C08](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md):**
- Control: un detector perfecto da `AP = 1,000`.
- El AP es el área bajo la curva con precisión interpolada: `AP50 = 0,581`.
- 🎯 **Por qué importa:** Un segmentador que acierta el 99 % de los píxeles puede no encontrar nunca la clase que importa, y dos detectores con AP de 0,58 y 0,60 pueden ser indistinguibles con 100 imágenes. La decisión central: ¿qué métricas y qué intervalo hacen falta para afirmar que un algoritmo de percepción es suficiente para una tarea?
- 🔗 **Se estudia junto con:** IoU, precisión, exhaustividad, MAE.

📘 **Dónde se aprende** (1 clase): [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md).

### Apagado

- El apagado ocurre cuando `P < P_min`.

💡 **Cómo se explica en la clase [B81-C05](../programa/clases/B81/B81-C05-limitaciones-de-potencia-en-propulsion-electrica/CLASE.md):**
- Con `P₁ = 10 kW`, `P_max = 4,5 kW` y `P_min = 0,5 kW`: el radio de saturación es `√(10/4,5) = 1,4907 UA` y el de apagado `√(10/0,5) = 4,4721 UA`.
- Incluir la saturación del propulsor y el apagado por potencia mínima.
- ⚠️ **Error frecuente:** Olvidar el apagado por potencia mínima. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un diseño de trayectoria que ignore la potencia sobreestima el empuje lejos del Sol. La decisión central: ¿hasta qué distancia mantiene una nave eléctrica su empuje máximo y a partir de dónde pierde capacidad?
- 🔗 **Se estudia junto con:** irradiancia, potencia disponible, empuje, saturación.

📘 **Dónde se aprende** (1 clase): [B81-C05 · Limitaciones de potencia en propulsión eléctrica](../programa/clases/B81/B81-C05-limitaciones-de-potencia-en-propulsion-electrica/CLASE.md).

### Apalancamiento

- El apalancamiento (*leverage*) es la influencia potencial de un punto por estar lejos del centro de las `t`.
- El apalancamiento y el residuo son lo relevante en regresión (C11).
- El apalancamiento (*gear ratio*) es cuántos kilogramos hay que lanzar desde la Tierra por cada kilogramo que llega a la superficie del destino.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C11](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md):**
- Los atípicos en los extremos de `t` tienen apalancamiento alto, por eso OLS se tuerce tanto.
- Huber equilibra: casi tan eficiente como OLS en datos limpios y resistente a atípicos moderados, pero su resistencia a atípicos con alto apalancamiento es menor.
- ⚠️ **Error frecuente:** Ignorar el apalancamiento. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Los datos reales traen errores de transmisión, rayos cósmicos en un detector, una lectura perdida o un salto del sensor. Un solo punto muy alejado puede torcer la recta de mínimos cuadrados y producir parámetros y predicciones erróneos con errores típicos pequeños y engañosos.
- 🔗 **Se estudia junto con:** valor atípico, punto de ruptura, MAD, pendiente de Theil–Sen.

📘 **Dónde se aprende** (4 clases): [B12-C11 · Regresión robusta](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md); [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md); [B59-C01 · Concepto de utilización de recursos in situ](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md); [B59-C19 · Evaluación logística de una instalación](../programa/clases/B59/B59-C19-evaluacion-logistica-de-una-instalacion/CLASE.md).

### Apantallamiento

- El apantallamiento es la cancelación del campo de una carga por las demás.
- El apantallamiento (autoabsorción) reduce la tasa dentro de la nube.

💡 **Cómo se explica en la clase [B30-C07](../programa/clases/B30/B30-C07-longitud-de-debye-y-plasma/CLASE.md):**
- Comprobar la carga de apantallamiento `−q`.
- Ejercicio 11 · transferencia. Transferencia. ¿Qué pasa con el apantallamiento a escalas menores que `λ_D`?
- ⚠️ **Error frecuente:** Creer que a escalas menores hay apantallamiento. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Sin apantallamiento no hay plasma, y sin muchas partículas en la esfera de Debye no hay comportamiento colectivo. La decisión central: ¿cuándo un gas ionizado es un plasma?
- 🔗 **Se estudia junto con:** longitud de Debye, parámetro de plasma, cuasineutralidad.

📘 **Dónde se aprende** (2 clases): [B30-C07 · Longitud de Debye y plasma](../programa/clases/B30/B30-C07-longitud-de-debye-y-plasma/CLASE.md); [B55-C08 · Fotoquímica cósmica](../programa/clases/B55/B55-C08-fotoquimica-cosmica/CLASE.md).

### Aperiódica

- Una cadena irreducible puede llegar de cualquier estado a cualquier otro; aperiódica no queda atrapada en ciclos; si es ambas, converge a su única `π` desde cualquier inicio.

💡 **Contexto en la clase [B12-C13](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md):**
- **Idea central (modelo mental):** Imagina un paseante en un paisaje cuya altura es la densidad objetivo. Prueba un paso al azar: si sube, siempre lo da; si baja, lo da con una probabilidad proporcional a cuánto baja. A largo plazo pasa más tiempo en las zonas altas, exactamente en proporción a la altura.
- 🎯 **Por qué importa:** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.
- 🔗 **Se estudia junto con:** cadena de Markov, matriz de transición, distribución estacionaria, irreducible.

📘 **Dónde se aprende** (1 clase): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md).

### Apertura

- La apertura `D` es el diámetro de la abertura que recoge la luz (pupila o espejo).
- La apertura `D` es el diámetro del objetivo o espejo; la distancia focal `F`, la longitud del camino óptico; la razón focal `N = F/D`.
- La exposición es el tiempo con el obturador abierto; el ISO es la amplificación de la señal; la apertura relativa del objetivo (f/) controla la luz.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C10](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md):**
- La luz del objeto pasa por el rango espectral del detector, por la apertura que fija cuánta luz entra, por la resolución que decide qué detalle se separa y por la percepción que interpreta; al final hay un registro o una impresión.
- Límite: los cuellos no son independientes; por ejemplo, ampliar la apertura mejora a la vez la luz captada y la resolución.
- 🎯 **Por qué importa:** Si el ojo bastara, no habría observatorios. La luz visible es una franja pequeña del espectro electromagnético (S1, S2); además, tu pupila recoge poca luz, separa detalles hasta cierto tamaño y puede engañarte.
- 🔗 **Se estudia junto con:** rango espectral, sensibilidad, resolución angular, difracción.

📘 **Dónde se aprende** (8 clases): [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md); [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md); [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md); [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md); [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B42-C02 · Principio de Huygens-Fresnel](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md) y 2 más.

### Apertura limitante

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C09](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md):**
- A["apertura limitante"] --> P["pupila de salida: imagen"]
- *Descripción textual:* la apertura limitante fija la luz; su imagen es la pupila de salida y el solape de aperturas, el viñeteo.
- 🎯 **Por qué importa:** La pupila limita la luz y el viñeteo oscurece los bordes. La decisión central: ¿qué diafragma manda y cuánta luz se pierde fuera del eje?
- 🔗 **Se estudia junto con:** pupila de entrada, pupila de salida, relieve ocular, obstrucción central.

📘 **Dónde se aprende** (1 clase): [B41-C09 · Pupilas y diafragmas ópticos](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md).

### Apertura óptima

- La apertura óptima maximiza la SNR.

💡 **Cómo se explica en la clase [B29-C02](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md):**
- Con `20 000` realizaciones en la apertura óptima: flujo medio `48 643,0` (esperado `48 644,6`) y desviación `233,97` (esperada `234,02`).
- *Descripción textual:* la PSF da la fracción de estrella dentro de la apertura; el número de pixeles da el ruido del fondo; ambos fijan la SNR, cuyo máximo da la apertura óptima y el error en magnitud.
- 🎯 **Por qué importa:** Una apertura pequeña pierde estrella; una grande suma cielo y ruido de lectura. La decisión central: ¿qué apertura maximiza la relación señal-ruido y qué error en magnitud implica?
- 🔗 **Se estudia junto con:** fotometría de apertura, ruido de disparo, ruido de lectura, error en magnitud.

📘 **Dónde se aprende** (1 clase): [B29-C02 · Curvas de luz fotométricas](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md).

### Apertura sintética

- La apertura sintética es el tramo de órbita en que un blanco está iluminado.
- La apertura sintética es el tramo de órbita, de longitud `vT`, durante el cual el blanco está iluminado.

💡 **Cómo se explica en la clase [B57-C07](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md):**
- Con `R = 846,0 km`, la apertura sintética tiene `λR/L = 3,91 km`.
- M["movimiento del satelite"] --> S["apertura sintetica lambda R/L"]
- 🎯 **Por qué importa:** La luz visible no atraviesa nubes ni sirve de noche; las microondas sí. Pero un radar no «fotografía»: mide distancia y fase de ecos.
- 🔗 **Se estudia junto con:** chirp, filtro adaptado, producto tiempo–ancho de banda, rango oblicuo.

📘 **Dónde se aprende** (2 clases): [B57-C07 · Sistemas radar SAR](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md); [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md).

### API

- Una API (interfaz de programación) es el contrato por el que un programa pide datos a otro.

💡 **Cómo se explica en la clase [B14-C31](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md):**
- La paginación por desplazamiento es sensible a inserciones durante el recorrido (un elemento nuevo desplaza los siguientes); en una API con datos cambiantes se prefiere un cursor, que no se trata aquí.
- La API paginada entrega por partes y permite filtros.
- 🎯 **Por qué importa:** Tu catálogo de escenas tiene 250 000 ítems y un programa ajeno quiere recorrerlos. Si le entregas una lista de golpe, se cae; si cada petición repite lo que ya tiene, desperdicias ancho de banda; si cambia un parámetro y falla sin explicación, nadie sabe qué hizo mal.
- 🔗 **Se estudia junto con:** recurso, ruta, Paginar, código de estado.

📘 **Dónde se aprende** (1 clase): [B14-C31 · APIs de servicios de datos](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md).

### API SBDB

- La API SBDB del JPL entrega datos de un cuerpo en formato legible por máquina; sus campos incluyen `a`, `e`, `i`, `q`, `ad`, `moid` y, en la parte física, `H` [S5].

💡 **Contexto en la clase [B58-C20](../programa/clases/B58/B58-C20-simulador-de-riesgo-de-impacto-basado-en-datos/CLASE.md):**
- 🎯 **Por qué importa:** Un simulador convierte reglas sueltas en un flujo reproducible: leer datos, filtrar, calcular y ordenar. La decisión central: ¿qué objetos del catálogo merecen atención primero y qué número de impactos de fondo es coherente con la ley de frecuencias?
- 🔗 **Se estudia junto con:** proceso de Poisson, frecuencia de fondo, simulador basado en datos.

📘 **Dónde se aprende** (1 clase): [B58-C20 · Simulador de riesgo de impacto basado en datos](../programa/clases/B58/B58-C20-simulador-de-riesgo-de-impacto-basado-en-datos/CLASE.md).

### Apilamiento

- El apilamiento es el efecto de pagar varias regalías por un mismo producto.

💡 **Cómo se explica en la clase [B124-C09](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de valoración de una licencia sintética*: flujo de regalías, valor actual con su verificación, apilamiento, comparación exclusiva/no exclusiva y lista de qué es sintético, con el aviso de que no es asesoría legal.
- El script [valor_de_licencia.py](valor_de_licencia.py) valora regalías por bucle y forma cerrada, evalúa el apilamiento y compara licencia exclusiva con no exclusiva (comprueba diferencia menor que 1e-9 y el factor de equilibrio por sustitución).
- 🎯 **Por qué importa:** La propiedad intelectual es un activo, pero su valor depende de cuánto se vende con ella y de cuánto del margen se queda el que la usa. La decisión central: ¿qué licencia conviene ofrecer y cuántas regalías soporta el licenciatario?
- 🔗 **Se estudia junto con:** licencia, cuota inicial, regalía, valor actual.

📘 **Dónde se aprende** (1 clase): [B124-C09 · Propiedad intelectual y licencias](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md).

### Aplanado

- El aplanado (*flat-fielding*, aquí del fondo) divide la imagen por un perfil de fondo.

💡 **Cómo se explica en la clase [B15-C13](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md):**
- Umbral local o con fondo aplanado: se adapta a fondos variables.
- Ejercicio 12 · integrador. Elabora tu *máscara segmentada con métricas*: genera tu disco con oscurecimiento al borde y tres manchas, segmenta con Otsu global y con el método aplanado, calcula píxeles marcados, IoU, Dice, número de regiones y área como fracción del disco, y comenta por qué difieren.
- 🎯 **Por qué importa:** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.
- 🔗 **Se estudia junto con:** segmentación, umbralización, método de Otsu, varianza entre clases.

📘 **Dónde se aprende** (1 clase): [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md).

### Aplanador

- El aplanador es un elemento cercano al foco que anula esa suma.

💡 **Cómo se explica en la clase [B50-C07](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md):**
- *Descripción textual:* las superficies de enfoque se obtienen de trazar haces estrechos, y el aplanador anula la suma de Petzval.
- Un aplanador de focal `-1863 mm` anula el hundimiento.
- 🎯 **Por qué importa:** Un detector plano mal enfocado en el borde pierde resolución: hay que decidir si se acepta, se curva el detector o se agrega un aplanador. La decisión central: ¿cuánto se hunde el foco en el borde y qué lo corrige?
- 🔗 **Se estudia junto con:** tangencial, sagital, superficie de Petzval, suma de Petzval.

📘 **Dónde se aprende** (1 clase): [B50-C07 · Curvatura de campo y aplanadores](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md).

### Aplicación de planetario

- Una aplicación de planetario es un programa que calcula posiciones y las dibuja para tu lugar y hora;

💡 **Contexto en la clase [B08-C07](../programa/clases/B08/B08-C07-planisferios-y-aplicaciones-celestes/CLASE.md):**
- **Idea central (modelo mental):** El disco del mapa representa la esfera celeste en AR y Dec (C03); la máscara representa tu horizonte, que depende de tu latitud (C02). Girar el disco es lo mismo que cambiar el tiempo sidéreo: la ascensión recta que queda en el meridiano es el TSL.
- 🎯 **Por qué importa:** Una herramienta que no entiendes es una caja negra: si la aplicación se equivoca de ubicación o de hora, no lo notarás. La pregunta motivadora: ¿puedo confiar en lo que me muestra la herramienta, y qué hago si no hay batería?
- 🔗 **Se estudia junto con:** planisferio, Stellarium, modo nocturno rojo, hora oficial.

📘 **Dónde se aprende** (1 clase): [B08-C07 · Planisferios y aplicaciones celestes](../programa/clases/B08/B08-C07-planisferios-y-aplicaciones-celestes/CLASE.md).

### Apoápside

- Periápside y apoápside son los puntos más cercano y más lejano al cuerpo central; en torno al Sol se llaman perihelio y afelio.
- El periápside `r_p = a(1 − e)` y el apoápside `r_a = a(1 + e)`.

💡 **Cómo se explica en la clase [B71-C01](../programa/clases/B71/B71-C01-leyes-de-kepler/CLASE.md):**
- *Pista:* en el periápside y el apoápside la velocidad es perpendicular al radio.
- 🎯 **Por qué importa:** Kepler obtuvo sus leyes ajustando observaciones; Newton mostró después que son consecuencia de una fuerza central inversa al cuadrado.
- 🔗 **Se estudia junto con:** semieje mayor, excentricidad, período, velocidad areolar.

📘 **Dónde se aprende** (2 clases): [B71-C01 · Leyes de Kepler](../programa/clases/B71/B71-C01-leyes-de-kepler/CLASE.md); [B71-C08 · Órbitas elípticas](../programa/clases/B71/B71-C08-orbitas-elipticas/CLASE.md).

### Apoapsis alcanzado

- El apoapsis alcanzado es `a(1 + e)`.

💡 **Cómo se explica en la clase [B75-C22](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md):**
- El apoapsis alcanzado baja respecto del tangencial (barrido de `φ`), por lo que cuesta más llegar al mismo radio.
- 🎯 **Por qué importa:** Antes de optimizar toda la misión conviene entender el primer impulso. La decisión central: ¿qué módulo y qué dirección del primer impulso alcanzan un radio dado con el menor delta-v y en cuánto tiempo?
- 🔗 **Se estudia junto con:** primer impulso, dirección, familia tangencial, tiempo hasta el apoapsis.

📘 **Dónde se aprende** (1 clase): [B75-C22 · Modelos de primer impulso](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md).

### Apodización

- La apodización suaviza el borde de la máscara.

💡 **Contexto en la clase [B40-C08](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md):**
- **Idea central (modelo mental):** Como separar el campo eléctrico de un campo que gira: solo se distinguen si se ve el mapa completo; con un hueco aparecen mezclas.
- 🎯 **Por qué importa:** Un modo B primordial sería una huella de ondas gravitacionales, pero las máscaras filtran E hacia B. La decisión central: ¿cómo se separan E y B y cuánto contamina una máscara?
- 🔗 **Se estudia junto con:** modo E, modo B, parámetros de Stokes, ángulo.

📘 **Dónde se aprende** (1 clase): [B40-C08 · Polarización E y B del fondo cósmico](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md).

### Apogeo

- El apogeo es el punto más alto de una trayectoria.
- El apogeo y el perigeo son las alturas máxima y mínima.
- El apogeo es la altura máxima.

💡 **Cómo se explica en la clase [B56-C10](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md):**
- Integrando `r'' = −GM/r²` desde la superficie, el apogeo coincide con el de la energía a menos de `10⁻⁶` en los tres casos.
- C -- "sí" --> D["Apogeo finito:<br/>cae como nieve"]
- 🎯 **Por qué importa:** El penacho permite muestrear un océano sin aterrizar. Para diseñar un sobrevuelo hace falta saber hasta dónde llegan los granos y cuáles escapan al anillo E.
- 🔗 **Se estudia junto con:** penacho, velocidad de escape, balística radial, anillo E.

📘 **Dónde se aprende** (3 clases): [B56-C10 · Océanos de Encélado](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md); [B119-C04 · Convenio de Registro](../programa/clases/B119/B119-C04-convenio-de-registro/CLASE.md); [B119-C24 · Límites legales y de seguridad de la experimentación educativa](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md).

### Apolune

- El perilune y el apolune son los radios mínimo y máximo respecto de la Luna.

💡 **Cómo se explica en la clase [B76-C05](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md):**
- Se parte del apolune: `(x0, 0, z0, 0, vy0, 0)`.
- Periodo `6,5375 d`; resonancia `2 P_sin/T = 9,034`; perilune `3184 km` (`1447 km` de altitud); apolune `71.078 km`;
- 🎯 **Por qué importa:** La NRHO es la órbita de referencia publicada para la estación Gateway. La decisión central: ¿cómo se calcula una órbita periódica inestable y qué tan cerca queda un modelo simple de la referencia en un modelo de efemérides?
- 🔗 **Se estudia junto con:** NRHO, perilune, corrección diferencial, monodromia.

📘 **Dónde se aprende** (1 clase): [B76-C05 · Órbitas NRHO](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md).

### Aporte

- Posterior: probabilidad tras la evidencia. Aporte: `log₁₀` de la razón de verosimilitud de un síntoma.

💡 **Cómo se explica en la clase [B96-C21](../programa/clases/B96/B96-C21-diagnostico-explicable-de-anomalias/CLASE.md):**
- Quitar el síntoma de mayor aporte (generación baja) cambia el diagnóstico a «nominal» (0,5429): la conclusión depende de esa evidencia.
- Q --> E["Explicacion: prior + aporte por sintoma"]
- ⚠️ **Error frecuente:** Dar el diagnóstico sin explicación. Muestra el aporte de cada síntoma (8.3)
- 🎯 **Por qué importa:** C13 detecta que algo anda mal; esta clase responde por qué la máquina cree lo que cree. La decisión central: ¿qué hipótesis es la más probable y qué evidencia la sostiene, de modo que un operador pueda aceptarla o refutarla?
- 🔗 **Se estudia junto con:** Hipótesis, Síntoma, Prior, Posterior.

📘 **Dónde se aprende** (1 clase): [B96-C21 · Diagnóstico explicable de anomalías](../programa/clases/B96/B96-C21-diagnostico-explicable-de-anomalias/CLASE.md).

### Aporte del cortante

- El aporte del cortante es `3EI/(κGAL²)` en un voladizo.

💡 **Cómo se explica en la clase [B84-C27](../programa/clases/B84/B84-C27-tipos-de-elementos-finitos-viga-placa-y-solido/CLASE.md):**
- El aporte del cortante `3EI/(κGAL²)` cae con `(h/L)²`; con el criterio ilustrativo de 5 %, Euler es aceptable desde `L/h ≥ 4` en sección rectangular.
- Ejercicio 2 · con los pasos indicados ¿Qué aporte del cortante tiene `L/h = 10`?
- 🎯 **Por qué importa:** Una viga corta modelada con Euler subestima la flecha en 17 %; no es un error de malla sino de hipótesis. La decisión central: ¿para qué esbeltez es válido el elemento de Euler y cuándo hace falta cortante?
- 🔗 **Se estudia junto con:** viga de Euler–Bernoulli, Timoshenko, integración reducida.

📘 **Dónde se aprende** (1 clase): [B84-C27 · Tipos de elementos finitos: viga, placa y sólido](../programa/clases/B84/B84-C27-tipos-de-elementos-finitos-viga-placa-y-solido/CLASE.md).

### Apoyo a la decisión

- Sensibilidad `TP/(TP+FN)` y especificidad `TN/(TN+FP)`. Apoyo a la decisión: herramienta que sugiere, no decide.

💡 **Contexto en la clase [B116-C04](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md):**
- 🎯 **Por qué importa:** Un puntaje simple ayuda a decidir rápido y de forma homogénea, pero un fallo por defecto (sub-triage) deja sin atender a quien lo necesita y uno por exceso (sobre-triage) agota recursos y atención. Y si la respuesta de tierra tarda decenas de minutos, no se puede esperar a tierra para lo que no admite espera.
- 🔗 **Se estudia junto con:** Triage, puntaje de alerta temprana, categoría, Sub-triage.

📘 **Dónde se aprende** (1 clase): [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Aprendizaje no supervisado

- El aprendizaje no supervisado busca estructura en datos sin etiquetas.

💡 **Cómo se explica en la clase [B17-C06](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md):**
- python programa/clases/B17/B17-C06-aprendizaje-no-supervisado/agrupamiento.py
- 🎯 **Por qué importa:** Un catálogo trae miles de objetos medidos en varias bandas y nadie los ha clasificado. ¿Hay poblaciones distintas?
- 🔗 **Se estudia junto con:** componente principal, varianza explicada, agrupamiento, K-medias.

📘 **Dónde se aprende** (1 clase): [B17-C06 · Aprendizaje no supervisado](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md).

### Aprendizaje supervisado

- El aprendizaje supervisado ajusta un modelo a pares (entrada, respuesta): las respuestas se llaman etiquetas.

💡 **Cómo se explica en la clase [B17-C02](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md):**
- python programa/clases/B17/B17-C02-aprendizaje-supervisado/validacion_cruzada.py
- 🎯 **Por qué importa:** Un modelo que clasifica señales como «candidata» o «no candidata» puede acertar el 100 % de los ejemplos con los que se entrenó y fallar la cuarta parte de los nuevos: memorizó. Lo que importa a un equipo científico es el desempeño en datos que el modelo no vio.
- 🔗 **Se estudia junto con:** etiquetas, clasificación, regresión, conjunto de entrenamiento.

📘 **Dónde se aprende** (1 clase): [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md).

### Aprobación

- Rol: nivel de autoridad. Aprobación: visto bueno de otra persona.

💡 **Cómo se explica en la clase [B96-C07](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md):**
- Se evalúan `3 × 4 × 5 × 2 = 120` combinaciones (rol, criticidad, cinco listas de aprobaciones, armado sí/no) con la política y con una referencia independiente basada en tablas de mínimos.
- (2) Ningún comando crítico se permite sin aprobación.
- ⚠️ **Error frecuente:** Dejar que el solicitante se apruebe. La aprobación viene de otra persona (8.2)
- 🎯 **Por qué importa:** Un comando enviado por la persona equivocada o sin segunda revisión puede perder la misión. La decisión central: ¿qué rol, qué aprobaciones y qué armado exige cada nivel de criticidad y cómo se prueba que la política no tiene huecos?
- 🔗 **Se estudia junto con:** Criticidad, Rol, Armado, Referencia independiente.

📘 **Dónde se aprende** (1 clase): [B96-C07 · Telecomandos y autorizaciones](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md).

### Aprobador

- Un aprobador autoriza el mensaje.

💡 **Cómo se explica en la clase [B122-C08](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md):**
- K --> M["matriz: audiencia, canal, aprobador"]
- Construir una matriz de audiencias, canales y aprobadores.
- 🎯 **Por qué importa:** B124-C18 trata divulgación; la comunicación de crisis con mensajes oportunos no está cubierta. La decisión central: ¿qué hay que comunicar, a quién y antes de qué plazo?
- 🔗 **Se estudia junto con:** alerta temprana, notificación, informe final, audiencia.

📘 **Dónde se aprende** (1 clase): [B122-C08 · Comunicación de crisis con operadores, autoridades y público](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md).

### Apropiación cultural

- La apropiación cultural es, en esta clase, usar un saber, relato o símbolo de un pueblo sin su autorización o sin beneficio para él, descontextualizándolo.

💡 **Cómo se explica en la clase [B133-C04](../programa/clases/B133/B133-C04-riesgos-de-apropiacion-cultural-en-la-divulgacion/CLASE.md):**
- python programa/clases/B133/B133-C04-riesgos-de-apropiacion-cultural-en-la-divulgacion/auditoria_guion.py
- 🎯 **Por qué importa:** La divulgación llega a mucha gente y la apropiación suele ocurrir sin mala intención, por falta de método. La decisión central: ¿qué revisas antes de difundir un contenido sobre un saber que no es tuyo, y quién decide si se difunde?
- 🔗 **Se estudia junto con:** atribución, generalización, borrado temporal, protocolo.

📘 **Dónde se aprende** (1 clase): [B133-C04 · Riesgos de apropiación cultural en la divulgación](../programa/clases/B133/B133-C04-riesgos-de-apropiacion-cultural-en-la-divulgacion/CLASE.md).

### Apropiación nacional

- VIII). Apropiación nacional es reclamar soberanía u ocupar de manera exclusiva (art.

💡 **Contexto en la clase [B119-C01](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md):**
- 🎯 **Por qué importa:** Casi todo el derecho espacial posterior (salvamento, responsabilidad, registro, Luna) desarrolla principios de este tratado, y ninguna otra clase del programa lo estudia como instrumento jurídico. La decisión central: ¿qué obligación del tratado se infringe en una misión dada y qué cambio mínimo la devuelve a la conformidad?
- 🔗 **Se estudia junto con:** Estado parte, autorización y supervisión continua, Jurisdicción y control, regla comprobable.

📘 **Dónde se aprende** (1 clase): [B119-C01 · Tratado del Espacio Ultraterrestre](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md).

### Aproximación

- Una aproximación sustituye una expresión por otra más sencilla con un error acotado.

💡 **Cómo se explica en la clase [B04-C06](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md):**
- *Descripción textual:* a partir del ángulo se obtiene el punto del círculo unidad; de él salen la identidad de Pitágoras y, girando dos veces, la suma de ángulos y el ángulo doble; si el ángulo es pequeño se aproxima `sen` y `tan` por el ángulo; si no, se usa la función exacta.
- Paso 2 · Aproximación. `δ ≈ 2R/d = 9,0395 × 10⁻³ rad`.
- 🎯 **Por qué importa:** Casi toda medición astronómica es un ángulo: la posición de una estrella respecto de otra, el tamaño aparente de la Luna, el desplazamiento por paralaje. Y casi todos esos ángulos son diminutos, de segundos de arco.
- 🔗 **Se estudia junto con:** círculo unidad, tangente, radián, segundo de arco.

📘 **Dónde se aprende** (1 clase): [B04-C06 · Identidades trigonométricas](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md).

### Aproximación cuadrupolar

- La aproximación cuadrupolar es `2 μ_s r/d³` sobre la línea Sol-Tierra.

💡 **Cómo se explica en la clase [B72-C09](../programa/clases/B72/B72-C09-perturbaciones-solares/CLASE.md):**
- Ejercicio 3 · casi autónomo. ¿Por qué la aproximación cuadrupolar es tan buena?
- 🎯 **Por qué importa:** En órbitas altas el Sol y la Luna compiten con J2 y gobiernan la evolución de la inclinación y del nodo. La decisión central: ¿cuánto gira el plano de una órbita por la marea solar y qué fórmula sirve para predecirlo?
- 🔗 **Se estudia junto con:** marea solar, polo orbital, precesión luni-solar.

📘 **Dónde se aprende** (1 clase): [B72-C09 · Perturbaciones solares](../programa/clases/B72/B72-C09-perturbaciones-solares/CLASE.md).

### Aproximación de ángulo pequeño

- La aproximación de ángulo pequeño dice `tan θ ≈ θ` (en radianes) si `θ` es pequeño.

💡 **Cómo se explica en la clase [B03-C18](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md):**
- La aproximación de ángulo pequeño sirve.
- Usar la aproximación de ángulo pequeño y reconocer su rango de validez.
- 🎯 **Por qué importa:** El Sol y la Luna se ven en el cielo con tamaños angulares muy parecidos, de alrededor de medio grado. ¿Es casualidad que midan lo mismo en el cielo siendo tan distintos?
- 🔗 **Se estudia junto con:** triángulo rectángulo, cateto opuesto, cateto adyacente, hipotenusa.

📘 **Dónde se aprende** (1 clase): [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md).

### Aproximación de campo débil

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B32-C12](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md):**
- **Idea central (modelo mental):** Un campo magnético hace que la cuerda del átomo vibre con dos tonos ligeramente distintos según la polarización; la diferencia entre ambos tonos es el signo del campo.
- 🎯 **Por qué importa:** Medir campos estelares exige saber cuándo el desdoblamiento se resuelve y cuándo basta la polarización. La decisión central: ¿qué campo produce un desdoblamiento comparable al ancho de la línea?
- 🔗 **Se estudia junto con:** efecto Zeeman, factor de Landé efectivo, desdoblamiento, polarización circular.

📘 **Dónde se aprende** (2 clases): [B32-C12 · Efecto Zeeman y diagnóstico de campos magnéticos estelares](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md); [B47-C21 · Magnetógrafos y medición de campos solares](../programa/clases/B47/B47-C21-magnetografos-y-medicion-de-campos-solares/CLASE.md).

### Aproximación de cáscara fina

- Una aproximación de cáscara fina supone `d_o ≪ R` y vale `V ≈ 4πr²d_o`.

💡 **Cómo se explica en la clase [B56-C09](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md):**
- Comparar con la aproximación de cáscara fina.
- 🎯 **Por qué importa:** Un océano global bajo el hielo es un candidato a hábitat, protegido de la radiación y del vacío. Saber cuán profundo es y qué presión soporta fija qué sondas podrían llegar y qué ambientes existen.
- 🔗 **Se estudia junto con:** océano subsuperficial, cascarón esférico, espesor del hielo, profundidad del océano.

📘 **Dónde se aprende** (1 clase): [B56-C09 · Océanos de Europa](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md).

### Aproximación de Condon

- La aproximación de Condon supone que el momento de transición electrónico es constante.

💡 **Cómo se explica en la clase [B62-C03](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md):**
- Enunciar el principio de Franck-Condon y la aproximación de Condon.
- Ejercicio 10 · transferencia. Transferencia. ¿Qué debes verificar antes de usar la aproximación de Condon?
- 🎯 **Por qué importa:** Las bandas electrónicas aparecen en el ultravioleta y el visible; su forma, una serie de picos, revela cuánto cambia la geometría de la molécula. La decisión central: ¿qué picos de la progresión serán intensos?
- 🔗 **Se estudia junto con:** principio de Franck-Condon, factor de Franck-Condon, factor de Huang-Rhys, progresión.

📘 **Dónde se aprende** (1 clase): [B62-C03 · Transiciones electrónicas moleculares](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md).

### Aproximación de evento raro

- La aproximación de evento raro suma las probabilidades de los cortes; la cota de cortes mínimos es `1 − Π(1 − P(cᵢ))`.

💡 **Cómo se explica en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- La enumeración exacta de los 128 estados da 0,016132; la inclusión–exclusión, 0,016132; la aproximación de evento raro, 0,016200 (un 0,42 % de más); la cota de cortes mínimos, 0,016132 (aquí coincide porque los cortes mínimos no comparten eventos);
- Comparar la aproximación de evento raro y la cota de cortes mínimos con el valor exacto.
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?
- 🔗 **Se estudia junto con:** árbol de fallos, eventos básicos, conjunto de corte, mínimo.

📘 **Dónde se aprende** (1 clase): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Aproximación de Hill

- La aproximación de Hill da la distancia de L1 y L2 al primario menor como `(μ/3)^(1/3)` unidades cuando `μ` es pequeño.

💡 **Cómo se explica en la clase [B47-C22](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md):**
- L1: distancia a la Tierra = 1.49155 millones de km ; aproximacion de Hill = 1.49656 ; diferencia = 0.336 %
- 🎯 **Por qué importa:** Cada órbita compra una ventaja y una dificultad. La decisión central: ¿qué punto o qué órbita da la vista del Sol que necesita el instrumento a un costo térmico y de enlace aceptable?
- 🔗 **Se estudia junto con:** punto de Lagrange L1, órbita geosíncrona, perihelio, afelio.

📘 **Dónde se aprende** (2 clases): [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md); [B73-C03 · Puntos de equilibrio de Lagrange](../programa/clases/B73/B73-C03-puntos-de-equilibrio-de-lagrange/CLASE.md).

### Aproximación de Maréchal

- La aproximación de Maréchal es `S ≈ e^(−(2πσ)²)` con `σ` en ondas.
- La aproximación de Maréchal `exp(−σ²)`.

💡 **Cómo se explica en la clase [B50-C14](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md):**
- Comparar con la aproximación de Maréchal.
- Esferica de Zernike Z(4,0): Strehl exacto (intensidad central) frente a la aproximacion de Marechal
- 🎯 **Por qué importa:** Una especificación solo sirve si se puede verificar con una medida que tiene incertidumbre. La decisión central: ¿cuánto margen se deja para que una medida incierta no acepte una unidad mala?
- 🔗 **Se estudia junto con:** razón de Strehl, criterio de Rayleigh, banda de guarda, riesgo del consumidor.

📘 **Dónde se aprende** (2 clases): [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md); [B50-C14 · Criterios de aceptación: Strehl, error de frente de onda y especificaciones](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md).

### Aproximación de primer orden

- La aproximación de primer orden es `π HBR² × densidad(0)`.

💡 **Cómo se explica en la clase [B76-C14](../programa/clases/B76/B76-C14-evasion-de-colision/CLASE.md):**
- Calcularla por cuadratura polar y por la aproximación de primer orden.
- Pc cuadratura polar = 5.0457e-03 ; aproximacion de primer orden = 5.0727e-03 ;
- 🎯 **Por qué importa:** Una distancia de fallo pequeña no basta para decidir: importa cuánto vale frente a la incertidumbre. La decisión central: ¿cuál es la probabilidad de colisión y cuánto impulso cuesta bajarla de un umbral?
- 🔗 **Se estudia junto con:** probabilidad de colisión, fallo, umbral.

📘 **Dónde se aprende** (1 clase): [B76-C14 · Evasión de colisión](../programa/clases/B76/B76-C14-evasion-de-colision/CLASE.md).

### Aproximación de rango k

- La aproximación de rango `k` es `A_k = Σ_{i≤k} σᵢ uᵢ vᵢᵀ`.

💡 **Cómo se explica en la clase [B10-C11](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md):**
- El teorema de Eckart–Young (resultado estándar sin cita específica aquí) dice que la mejor aproximación de rango `k` en norma 2 tiene error exactamente `σ_{k+1}`, y en norma de Frobenius `√(Σ_{i>k} σᵢ²)`.
- Estimar el almacenamiento y el error de una aproximación de bajo rango.
- 🎯 **Por qué importa:** Un instrumento entrega una imagen de miles de píxeles; la mayor parte de su estructura se puede describir con muy pocos patrones. Una matriz de medidas puede tener columnas casi redundantes, de modo que un cálculo «técnicamente posible» sea inútil.
- 🔗 **Se estudia junto con:** SVD, valores singulares, vectores singulares izquierdos, derechos.

📘 **Dónde se aprende** (1 clase): [B10-C11 · Valores singulares y SVD](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md).

### Aproximación de Zel'dovich

- La aproximación de Zel'dovich `x = q + D s(q)`.

💡 **Contexto en la clase [B36-C05](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md):**
- **Idea central (modelo mental):** Es como una fila de fichas empujadas hacia un punto: antes de que se toquen, su posición es una fórmula simple; después, hay que seguirlas una a una.
- 🎯 **Por qué importa:** Una simulación sin comprobar contra un caso exacto no es una prueba. La decisión central: ¿converge el integrador al resultado analítico y qué pasa cuando las láminas se cruzan?
- 🔗 **Se estudia junto con:** lámina, posición lagrangiana, caja periódica, salto de rana.

📘 **Dónde se aprende** (1 clase): [B36-C05 · Simulaciones cosmológicas de N cuerpos: condiciones iniciales y caja periódica](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md).

### Aproximación impulsiva

- La aproximación impulsiva reemplaza el encuentro por un cambio instantáneo de velocidad.

💡 **Contexto en la clase [B52-C16](../programa/clases/B52/B52-C16-nube-de-oort/CLASE.md):**
- **Idea central (modelo mental):** Como un empujón a un niño en un columpio casi detenido en lo más alto: un empujón pequeño cambia mucho su trayectoria porque su velocidad es mínima. Límite: estrella en línea recta, cometa de prueba, sin marea galáctica.
- 🎯 **Por qué importa:** Las perturbaciones estelares explican cómo cometas casi circulares en la nube pasan a órbitas que cruzan el Sistema Solar interior. La decisión central: ¿cuánto cambia la velocidad de un cometa de la nube con el paso de una estrella y qué efecto tiene en su perihelio?
- 🔗 **Se estudia junto con:** nube de Oort, término indirecto, perihelio.

📘 **Dónde se aprende** (1 clase): [B52-C16 · Nube de Oort](../programa/clases/B52/B52-C16-nube-de-oort/CLASE.md).

### Aproximación lineal

- Una aproximación lineal es el orden 1.
- La aproximación lineal (o linealización) en `p₀` es `f(p₀ + δ) ≈ f(p₀) + J(p₀) δ`.
- La aproximación lineal `m_p ≈ m₀ Δv/Vₑ` vale si `Δv ≪ Vₑ`.

💡 **Cómo se explica en la clase [B09-C14](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md):**
- La aproximación lineal (C03–C04) es el caso `n = 1`.
- 🎯 **Por qué importa:** Un cálculo orbital rápido usa `g(h) = g₀(1 − 2h/R)` para una altitud baja; uno más exigente necesita el siguiente término. Sin una cota del error no se sabe cuál usar.
- 🔗 **Se estudia junto con:** polinomio de Taylor, serie de Maclaurin, resto, Lagrange.

📘 **Dónde se aprende** (3 clases): [B09-C14 · Series y aproximaciones](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md); [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md); [B78-C11 · Micropropulsión para CubeSat](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md).

### Aproximación paraxial

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C08](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md):**
- **Idea central (modelo mental):** Como disparar con una mira exacta y otra aproximada: con tiros cerca del eje coinciden; con tiros desviados la aproximación falla, y el error crece con el cuadrado de la desviación.
- 🎯 **Por qué importa:** Los programas de diseño óptico trazan rayos exactos. La decisión central: ¿cuándo se separa el rayo real del paraxial y cómo crece esa diferencia?
- 🔗 **Se estudia junto con:** trazado exacto, distancia focal posterior (BFD), aberración esférica longitudinal, altura del rayo.

📘 **Dónde se aprende** (1 clase): [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md).

### Aproximación R-bar

- La aproximación R-bar va por la vertical.

💡 **Cómo se explica en la clase [B76-C11](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md):**
- La aproximación por R-bar tiene la ventaja de que la gravedad ayuda a frenar si falla un impulso.
- Planificar una aproximación R-bar con velocidad final nula.
- 🎯 **Por qué importa:** Una aproximación a baja velocidad no puede depender de que todos los impulsos se ejecuten. La decisión central: ¿cuántos tramos usar, cuánto cuestan y qué ocurre si el segundo impulso de un tramo falla?
- 🔗 **Se estudia junto con:** salto V-bar, seguridad pasiva, esfera de exclusión, costo por metro.

📘 **Dónde se aprende** (1 clase): [B76-C11 · Operaciones de aproximación](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md).

### Aproximación variacional

- La aproximación variacional `q*` es el miembro de la familia que minimiza `KL(q ‖ p(θ | y))`.

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- Un indicio práctico: si los intervalos variacionales cubren menos de lo nominal, la aproximación es demasiado confiada.
- Blei, Kucukelbir y McAuliffe (fuente S1) presentan la inferencia variacional como un método de aprendizaje automático que aproxima densidades difíciles, como las posteriores bayesianas, mediante optimización: se escoge una familia de densidades y se busca el miembro más cercano al objetivo en divergencia de Kullback–Leibler.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.
- 🔗 **Se estudia junto con:** divergencia de Kullback–Leibler, familia variacional, ELBO, campo medio.

📘 **Dónde se aprende** (1 clase): [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### Aproximación WKB

- La aproximación WKB supone longitudes de onda cortas frente a la escala del medio.

💡 **Contexto en la clase [B30-C09](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md):**
- **Idea central (modelo mental):** Las líneas de campo son como cuerdas tensas con masa: una sacudida transversal viaja a una velocidad que sube con la tensión (`B²/μ₀`) y baja con la densidad.
- 🎯 **Por qué importa:** La velocidad de Alfvén fija cuánto tarda una perturbación en recorrer un lazo coronal o una línea de campo del viento solar. La decisión central: ¿con qué velocidad viaja una perturbación magnética y cómo cambia el tiempo de viaje en un medio estratificado?
- 🔗 **Se estudia junto con:** MHD ideal, onda de Alfvén, esquema de salto de rana, condición CFL.

📘 **Dónde se aprende** (1 clase): [B30-C09 · Magnetohidrodinámica](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md).

### Aptitud

- La aptitud es `k₁ Σ w e^(−(t−s)/τ₁)` y la fatiga `k₂ Σ w e^(−(t−s)/τ₂)`.
- La aptitud es el componente que sube despacio y decae despacio (`τ1`).

💡 **Cómo se explica en la clase [B104-C04](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md):**
- Cada sesión suma una exponencial lenta de aptitud y una rápida de fatiga.
- W["carga diaria w(t)"] --> A["aptitud<br/>τ₁ = 42 d, k₁"]
- 🎯 **Por qué importa:** Entrenar más no siempre significa rendir más el día que importa. La decisión central: ¿cómo distribuir una misma carga total para llegar con la mejor combinación de aptitud y fatiga?
- 🔗 **Se estudia junto con:** carga, fatiga, rendimiento, TRIMP.

📘 **Dónde se aprende** (2 clases): [B104-C04 · Acondicionamiento físico general](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md); [B107-C01 · Entrenamiento cardiorrespiratorio y de resistencia de astronautas](../programa/clases/B107/B107-C01-entrenamiento-cardiorrespiratorio-y-de-resistencia-de-astronautas/CLASE.md).

### Aptitud latente

- La aptitud latente `θ` es la cualidad que se quiere medir, no observable.

💡 **Cómo se explica en la clase [B104-C03](../programa/clases/B104/B104-C03-seleccion-y-aptitud/CLASE.md):**
- T["aptitud latente θ"] --> S["puntaje s = θ + ruido"]
- *Descripción textual:* la aptitud latente genera un puntaje ruidoso; el corte y la elección de los diez mejores producen precisión, exhaustividad y la fracción de aptos entre los elegidos.
- 🎯 **Por qué importa:** Si una prueba tiene ruido, ¿cuántos de los elegidos serán de verdad aptos? La decisión central: ¿cuánto ruido tolera un embudo antes de que la elección se parezca a un sorteo?
- 🔗 **Se estudia junto con:** puntaje, umbral de corte, precisión, exhaustividad.

📘 **Dónde se aprende** (1 clase): [B104-C03 · Selección y aptitud](../programa/clases/B104/B104-C03-seleccion-y-aptitud/CLASE.md).

### Apuntamiento

- El apuntamiento resuelve `J Δv = r_ref − r(T)`, con `J` la jacobiana de la posición final respecto de la velocidad.

💡 **Cómo se explica en la clase [B76-C19](../programa/clases/B76/B76-C19-orbitas-de-mantenimiento/CLASE.md):**
- Por estrategia: apuntamiento a posición.
- 🎯 **Por qué importa:** Una órbita periódica inestable no se mantiene sola. La decisión central: ¿con qué frecuencia y qué impulso hay que corregir para que el error no crezca?
- 🔗 **Se estudia junto con:** mantenimiento, error de ejecución, cociente de desviaciones.

📘 **Dónde se aprende** (1 clase): [B76-C19 · Órbitas de mantenimiento](../programa/clases/B76/B76-C19-orbitas-de-mantenimiento/CLASE.md).

### AR(1)

- Un proceso AR(1) (*autorregresivo de orden 1*) cumple `x[n] = φ x[n−1] + w[n]` con `|φ| < 1`: cada dato hereda una fracción `φ` del anterior.

💡 **Cómo se explica en la clase [B15-C03](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md):**
- Para `N` grande, la varianza de la media de un AR(1) es aproximadamente `σ_x² (1 + φ)/[(1 − φ) N]`.
- La de un AR(1) es plana por debajo de una frecuencia de corte y cae después, así que su pendiente depende de la ventana que mires: en el laboratorio, entre `0,001` y `0,2` ciclos por muestra, da −1,40.
- ⚠️ **Error frecuente:** Leer la pendiente del AR(1) como constante. Depende de la ventana; sección 8.6.
- 🎯 **Por qué importa:** Una regla heredada de la física del laboratorio dice que, al promediar `N` mediciones, el error baja como `1/√N`. Esa regla solo vale si los errores de cada medición son independientes.
- 🔗 **Se estudia junto con:** ruido blanco, paseo aleatorio, ruido coloreado, ruido rojo.

📘 **Dónde se aprende** (1 clase): [B15-C03 · Ruido blanco y coloreado](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md).

### Árbitro

- El autor responde por el trabajo; el árbitro (*referee*, *reviewer*) lo evalúa y emite un informe; el editor decide, con base en los informes y en su criterio (S1).

💡 **Cómo se explica en la clase [B20-C03](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md):**
- El editor es responsable del contenido y toma la decisión; no está obligado a seguir la recomendación de cada árbitro, y puede rechazar en cualquier momento antes de la publicación si surgen problemas de integridad (S1).
- Para ti, como autor, implica que tienes derecho a críticas fundamentadas y no ofensivas, y para ti como futuro árbitro, un código de conducta.
- 🎯 **Por qué importa:** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.
- 🔗 **Se estudia junto con:** revisión por pares, autor, editor, informe de árbitro.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Árbol de ataque

- Un árbol de ataque descompone un evento en hojas.

💡 **Cómo se explica en la clase [B119-C14](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md):**
- La evidencia es la árbol de ataque defensivo con controles del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *árbol de ataque defensivo con controles*: árbol, riesgo base, efecto de cada control, combinación y aviso de que es educativo.
- 🎯 **Por qué importa:** La amenaza cibernética conecta el derecho con la seguridad operativa; el modelo defensivo de infraestructura espacial (B122-C03) lo desarrolla, y esta clase fija el razonamiento de riesgo. La decisión central: ¿qué control reduce más el riesgo residual y cuánto se gana al combinarlos?
- 🔗 **Se estudia junto con:** hoja, control, riesgo residual, defensa en profundidad.

📘 **Dónde se aprende** (1 clase): [B119-C14 · Amenazas cibernéticas a satélites](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md).

### Árbol de comportamiento

- Un árbol de comportamiento combina nodos *Secuencia* (todos deben tener éxito), *Fallback* (basta uno), condiciones y acciones.

💡 **Cómo se explica en la clase [B98-C02](../programa/clases/B98/B98-C02-sistemas-de-decision-autonomos-y-maquinas-de-estados-de-comportamiento/CLASE.md):**
- Expresar la misma decisión como un árbol de comportamiento y contrastarlo con la tabla.
- Ejercicio 10 · transferencia. Transferencia. ¿Cuándo preferirías un árbol de comportamiento a una tabla de estados?
- 🎯 **Por qué importa:** Una cadena de `if` crece sin control y nadie puede decir si un estado inseguro es alcanzable. La decisión central: ¿cómo se estructura la decisión para que se pueda comprobar que nunca se conduce sin energía ni se sale del modo seguro sin orden de Tierra?
- 🔗 **Se estudia junto con:** máquina de estados, guarda, modo seguro, invariante.

📘 **Dónde se aprende** (1 clase): [B98-C02 · Sistemas de decisión autónomos y máquinas de estados de comportamiento](../programa/clases/B98/B98-C02-sistemas-de-decision-autonomos-y-maquinas-de-estados-de-comportamiento/CLASE.md).

### Árbol de fallos

- Un árbol de fallos descompone un evento superior con compuertas Y y O hasta eventos básicos.

💡 **Cómo se explica en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- La evidencia es la árbol de fallos con cortes mínimos e importancia del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *árbol de fallos con cortes mínimos e importancia*: estructura, cortes, probabilidad por tres vías, importancia y acciones, con lista de qué es sintético y no consultado.
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?
- 🔗 **Se estudia junto con:** eventos básicos, conjunto de corte, mínimo, MOCUS.

📘 **Dónde se aprende** (1 clase): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Árbol de trabajo

- El árbol de trabajo es lo que ves y editas; el área de preparación es la lista de lo que irá en el próximo commit; el historial es la cadena de commits.

💡 **Cómo se explica en la clase [B07-C14](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md):**
- T["árbol de trabajo<br/>lo que editas"] -->|"git add"| A["área de preparación<br/>lo que irá en el commit"]
- Los cambios del árbol de trabajo pasan al área de preparación con `git add`, y de ahí al historial con `git commit`.
- 🎯 **Por qué importa:** Sin control de versiones, un proyecto científico acumula archivos como `analisis_final.py`, `analisis_final2.py` y `analisis_final_ahora_si.py`, y nadie sabe cuál produjo la figura del artículo. Con Git, cada estado importante queda guardado con un mensaje, una fecha y un autor, y puedes comparar o recuperar cualquier versión.
- 🔗 **Se estudia junto con:** repositorio, commit, modificado, preparado.

📘 **Dónde se aprende** (1 clase): [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md).

### Archivo de bloqueo

- Un archivo de bloqueo (`uv.lock`) registra las versiones exactas resueltas de todas las dependencias, incluidas las indirectas, y es multiplataforma (S3).
- Un archivo de bloqueo (*lockfile*) registra el resultado de esa resolución.

💡 **Cómo se explica en la clase [B07-C13](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md):**
- Límite de la analogía: una receta de cocina («2 huevos») no cambia de un día para otro; un paquete publicado sí puede desaparecer o cambiar de comportamiento si no fijas la versión, y el archivo de bloqueo no protege de cambios en el sistema operativo ni en el hardware.
- PyYAML 6.0.3; pytest 9.2.0) y trae su archivo de bloqueo `uv.lock`.
- 🎯 **Por qué importa:** «En mi computador funciona» es la frase más cara de la informática científica: el programa depende, sin decirlo, de la versión de Python y de cada biblioteca instalada. Si cambian, los resultados pueden cambiar o el programa fallar con un `ModuleNotFoundError`.
- 🔗 **Se estudia junto con:** entorno virtual, dependencia, dependencias de ejecución, desarrollo.

📘 **Dónde se aprende** (2 clases): [B07-C13 · Entornos y dependencias con uv](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md); [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Arco

- El arco es el intervalo de tiempo observado.
- El arco es el tiempo cubierto.

💡 **Cómo se explica en la clase [B58-C07](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md):**
- Con el mismo ruido, `σ(a)` baja al crecer el arco: 10 obs.
- El factor entre el arco corto y el largo es 180.
- ⚠️ **Error frecuente:** Ignorar el efecto del arco. Se corrige con 8.4.
- 🎯 **Por qué importa:** Una órbita ajustada es el producto central de la defensa planetaria: de ella salen las predicciones y las probabilidades. La decisión central: ¿cuántas observaciones y qué arco hacen falta para que la órbita sea fiable, y cómo se sabe que el ajuste es bueno?
- 🔗 **Se estudia junto con:** determinación de órbitas, Levenberg–Marquardt, residuos, covarianza formal.

📘 **Dónde se aprende** (2 clases): [B58-C07 · Determinación de órbitas](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md); [B58-C11 · Observaciones de seguimiento](../programa/clases/B58/B58-C11-observaciones-de-seguimiento/CLASE.md).

### Arco de ajuste

- El arco de ajuste es donde hay datos; la predicción es fuera de él.

💡 **Cómo se explica en la clase [B74-C20](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md):**
- *Descripción textual:* la referencia y la solución se comparan en el marco RTN dentro y fuera del arco de ajuste; la componente dominante apunta al modelo que falta.
- Descripción larga: la diferencia crece con el tiempo fuera del arco de ajuste y se concentra en la componente normal, señal de que falta la precesión nodal por J2.
- ⚠️ **Error frecuente:** Validar solo en el arco de ajuste. Compara también en predicción; ver 8.3.
- 🎯 **Por qué importa:** Una solución que ajusta bien sus datos puede predecir pésimamente. La decisión central: ¿dentro de qué tolerancia coincide mi solución con la referencia, en qué componente falla y qué modelo falta?
- 🔗 **Se estudia junto con:** efeméride de referencia, diferencia RTN, predicción, J2.

📘 **Dónde se aprende** (1 clase): [B74-C20 · Validación frente a efemérides de referencia](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md).

### Arco singular

- Un arco singular es el de 180°.

💡 **Cómo se explica en la clase [B75-C29](../programa/clases/B75/B75-C29-analisis-de-calendario-con-graficos-pork-chop/CLASE.md):**
- Al excluir los arcos a menos de `0,05°` de 180° (Lambert singular), el mínimo no queda sesgado por ruido numérico: sin la exclusión, el refinamiento llegó a un valor espurio de `8,618`.
- Un arco de `180°` es singular; se excluyen los puntos a menos de `0,05°`.
- 🎯 **Por qué importa:** El diseño de una misión necesita ver el espacio de soluciones, no un solo punto. La decisión central: ¿qué combinaciones de fecha de salida y tiempo de vuelo dan un `C3` aceptable y cuán ancha es la ventana?
- 🔗 **Se estudia junto con:** gráfico pork-chop, banda, ventana, día 0.

📘 **Dónde se aprende** (1 clase): [B75-C29 · Análisis de calendario con gráficos pork-chop](../programa/clases/B75/B75-C29-analisis-de-calendario-con-graficos-pork-chop/CLASE.md).

### Área

- El perímetro de un círculo de radio `r` es `2πr`; su área, `πr²`.

💡 **Cómo se explica en la clase [B03-C17](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md):**
- Para la Tierra, `r = 6 371 km`: perímetro `40 030 km`, área `1,2751 × 10⁸ km²`.
- Para la Tierra con radio medio, el área superficial es `5,1006 × 10⁸ km²`; el volumen, `1,0832 × 10¹² km³`.
- 🎯 **Por qué importa:** La NASA publica que la densidad media del Sol es 1408 kg/m³ (S1), cerca de una vez y media la del agua. ¿Cómo se obtiene?
- 🔗 **Se estudia junto con:** perímetro, esfera, área superficial, volumen.

📘 **Dónde se aprende** (1 clase): [B03-C17 · Áreas y volúmenes elementales](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md).

### Área (AUC)

- La curva ROC grafica la fracción de anomalías detectadas contra la de falsas alarmas al variar el umbral; su área (AUC) vale 1 si el método separa perfectamente y 0,5 si no distingue (S2).

💡 **Cómo se explica en la clase [B17-C05](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md):**
- Comparar métodos con el área bajo la curva ROC.
- 🎯 **Por qué importa:** El subsistema térmico de un satélite entrega temperatura y corriente. Cada una, por separado, puede estar dentro de su rango normal y sin embargo la pareja ser imposible: la corriente alta con temperatura baja no ocurre nunca en operación sana.
- 🔗 **Se estudia junto con:** anomalía, distancia de Mahalanobis, distribución chi-cuadrado, bosque de aislamiento.

📘 **Dónde se aprende** (1 clase): [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md).

### Área colectora

- La área colectora de un telescopio es la superficie con que recoge luz o ondas.

💡 **Cómo se explica en la clase [B02-C18](../programa/clases/B02/B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md):**
- Calcular intervalos y áreas colectoras a partir de datos publicados.
- En una hoja de cálculo arma la línea de tiempo de la sección 12 con una columna de fuente y estado, y calcula las áreas colectoras de los ejercicios 1 a 5.
- 🎯 **Por qué importa:** Chile alberga observatorios de primer nivel porque combina cielos oscuros, aire seco y altitud. Pero un observatorio también es una historia de decisiones, instituciones y territorios.
- 🔗 **Se estudia junto con:** paralaje solar, observatorio nacional, observatorio internacional, sitio astronómico.

📘 **Dónde se aprende** (2 clases): [B02-C18 · Expansión de la astronomía en Chile](../programa/clases/B02/B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md); [B41-C10 · Apertura y relación focal](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md).

### Área con signo

- El área con signo de un paralelogramo es el determinante de la matriz formada por sus lados.

💡 **Cómo se explica en la clase [B10-C04](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md):**
- El determinante es el factor por el que el operador multiplica áreas (en 2D) o volúmenes (en 3D); su signo dice si invierte la orientación.
- Interpretarlos como área o volumen con signo.
- 🎯 **Por qué importa:** Dos estaciones terrestres miden la dirección hacia un mismo objeto y quieren fijar su posición cruzando las visuales. Si el objeto está cerca y las visuales forman un buen ángulo, el cruce es nítido.
- 🔗 **Se estudia junto con:** determinante, expansión por cofactores, menor, singular.

📘 **Dónde se aprende** (1 clase): [B10-C04 · Determinantes y soluciones](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md).

### Área de baja

- El área de baja `A_cas` es el área en la que un fragmento causa una baja.
- El área de baja `A_cas` es el área en que un fragmento causa una baja.

💡 **Contexto en la clase [B121-C01](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md):**
- 🎯 **Por qué importa:** La autorización de un lanzamiento no es un trámite abstracto: incluye criterios numéricos de riesgo. La decisión central: ¿una trayectoria cumple el criterio de riesgo colectivo e individual que exige la licencia y con qué margen?
- 🔗 **Se estudia junto con:** licencia, riesgo colectivo, riesgo individual, zona de impacto.

📘 **Dónde se aprende** (2 clases): [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md); [B121-C03 · Protección ambiental en la legislación espacial](../programa/clases/B121/B121-C03-proteccion-ambiental-en-la-legislacion-espacial/CLASE.md).

### Área de garganta

- El área de garganta `A*` fija el caudal.

💡 **Cómo se explica en la clase [B78-C10](../programa/clases/B78/B78-C10-propulsion-de-gas-frio/CLASE.md):**
- *Descripción textual:* el gas y la temperatura dan el escape por energía y, por otra vía, por el número de Mach; el escape fija el caudal para un empuje, el área de garganta y la masa de gas para un impulso total.
- Calcular el caudal y el área de garganta para un empuje dado.
- 🎯 **Por qué importa:** Con la misma temperatura, el gas más liviano escapa más rápido, pero ocupa más volumen almacenado. La decisión central: ¿qué gas da más impulso por kilo y qué cuesta en volumen y en límites físicos de la expansión?
- 🔗 **Se estudia junto con:** gas frío, flujo estrangulado, número de Mach de salida, impulso total.

📘 **Dónde se aprende** (1 clase): [B78-C10 · Propulsión de gas frío](../programa/clases/B78/B78-C10-propulsion-de-gas-frio/CLASE.md).

### Área de intersección

- El área de intersección es la superficie común de los discos.
- El área de intersección de dos círculos da la fracción libre.

💡 **Cómo se explica en la clase [B29-C01](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md):**
- Calcular el área de intersección de dos discos y comprobarla por integración.
- Ejercicio 7. Área de intersección con `d = 0,5`, radios `1` y `0,3`.
- 🎯 **Por qué importa:** El tránsito es el método con más planetas descubiertos. Su profundidad da el radio del planeta y su duración informa del semieje y el parámetro de impacto.
- 🔗 **Se estudia junto con:** profundidad, duración, parámetro de impacto, oscurecimiento al limbo.

📘 **Dónde se aprende** (2 clases): [B29-C01 · Tránsitos planetarios](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md); [B50-C04 · Telecentricidad, viñeteo y diseño del campo](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md).

### Área de la separatriz

- El área de la separatriz es `A_s = 16 √ε`.

💡 **Cómo se explica en la clase [B73-C12](../programa/clases/B73/B73-C12-captura-y-escape-resonante/CLASE.md):**
- La separatriz encoge hasta igualar ese área cuando `16√ε = J`, es decir `ε* = (J/16)² = 0,01575`.
- P["pendulo: q, phi, eps(t)"] --> S["separatriz: area 16 sqrt(eps)"]
- 🎯 **Por qué importa:** Muchas resonancias observadas (satélites, planetas migrantes, asteroides) no son primordiales: los cuerpos entraron en ellas. Saber cuándo una captura es segura y cuándo es improbable, y cuándo un cuerpo atrapado debe escapar, evita explicaciones erróneas.
- 🔗 **Se estudia junto con:** modelo del péndulo, separatriz, invariante adiabático, captura.

📘 **Dónde se aprende** (1 clase): [B73-C12 · Captura y escape resonante](../programa/clases/B73/B73-C12-captura-y-escape-resonante/CLASE.md).

### Área de preparación

- El árbol de trabajo es lo que ves y editas; el área de preparación es la lista de lo que irá en el próximo commit; el historial es la cadena de commits.

💡 **Cómo se explica en la clase [B07-C14](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md):**
- T["árbol de trabajo<br/>lo que editas"] -->|"git add"| A["área de preparación<br/>lo que irá en el commit"]
- Los cambios del árbol de trabajo pasan al área de preparación con `git add`, y de ahí al historial con `git commit`.
- 🎯 **Por qué importa:** Sin control de versiones, un proyecto científico acumula archivos como `analisis_final.py`, `analisis_final2.py` y `analisis_final_ahora_si.py`, y nadie sabe cuál produjo la figura del artículo. Con Git, cada estado importante queda guardado con un mensaje, una fecha y un autor, y puedes comparar o recuperar cualquier versión.
- 🔗 **Se estudia junto con:** repositorio, commit, modificado, preparado.

📘 **Dónde se aprende** (1 clase): [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md).

### Área de referencia

- El área de referencia `A` es la superficie con la que se normaliza.
- El área de referencia `A` debe indicarse siempre con el coeficiente.

💡 **Cómo se explica en la clase [B77-C03](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md):**
- Calcular arrastre y sustentación con coeficientes y área de referencia.
- El área de referencia: sin ella `Cd` no permite calcular la fuerza.
- ⚠️ **Error frecuente:** Dar `Cd` sin su área de referencia. Se corrige con el vocabulario (sección 6).
- 🎯 **Por qué importa:** El momento de mayor carga aerodinámica no es el de mayor velocidad ni el de menor altitud. La decisión central: ¿cuándo ocurre el máximo de la presión dinámica y qué fuerzas produce?
- 🔗 **Se estudia junto con:** presión dinámica, fuerza aerodinámica, arrastre, sustentación.

📘 **Dónde se aprende** (2 clases): [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md); [B77-C04 · Coeficientes de arrastre y sustentación](../programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/CLASE.md).

### Área de una superficie de revolución

- La longitud de arco de `y = f(x)` es `∫ √(1 + f′²) dx`; el área de una superficie de revolución es `∫ 2π r ds`, con `ds = √(1 + z′²) dr`.

💡 **Cómo se explica en la clase [B09-C13](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md):**
- Calcular el área de una superficie de revolución con la longitud de arco.
- 🎯 **Por qué importa:** Un telescopio necesita un espejo con forma de paraboloide. Cuánto vidrio hay que retirar de un disco plano para darle forma, cuánto pesa, y cuánta superficie hay que aluminizar son preguntas de volumen y área.
- 🔗 **Se estudia junto con:** área entre curvas, sólido de revolución, método de los discos, método de los cascarones.

📘 **Dónde se aprende** (1 clase): [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md).

### Área de víctima

- El área de víctima es el área efectiva por fragmento.
- El área de víctima `A_c` es el área efectiva donde una persona sería alcanzada.

💡 **Cómo se explica en la clase [B77-C19](../programa/clases/B77/B77-C19-seguridad-de-rango-a-nivel-conceptual/CLASE.md):**
- *Descripción textual:* la probabilidad de falla, la distribución de impactos, la población y el área de víctima se combinan en las víctimas esperadas y en el riesgo individual, que se comparan con los umbrales.
- 🎯 **Por qué importa:** Mover el sitio de impacto un par de decenas de kilómetros cambia el riesgo en un factor de varios. La decisión central: ¿cómo se calculan las víctimas esperadas y cuánto depende de dónde cae lo que cae?
- 🔗 **Se estudia junto con:** víctimas esperadas, riesgo individual, zona de impacto, cuadratura.

📘 **Dónde se aprende** (2 clases): [B77-C19 · Seguridad de rango a nivel conceptual](../programa/clases/B77/B77-C19-seguridad-de-rango-a-nivel-conceptual/CLASE.md); [B118-C14 · Reentrada y riesgos en superficie](../programa/clases/B118/B118-C14-reentrada-y-riesgos-en-superficie/CLASE.md).

### Área efectiva

- El área efectiva `A_e = η A`.

💡 **Cómo se explica en la clase [B46-C03](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md):**
- Calcular el área efectiva y la ganancia en dBi.
- 🎯 **Por qué importa:** El tamaño de la antena fija a la vez la resolución y la sensibilidad. La decisión central: ¿qué diámetro y qué razón focal dan el haz y la ganancia requeridos?
- 🔗 **Se estudia junto con:** paraboloide, razón focal, patrón de Airy, ancho a media potencia.

📘 **Dónde se aprende** (4 clases): [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md); [B46-C03 · Antenas parabólicas](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md); [B46-C05 · Ganancia y temperatura de antena](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md); [B47-C05 · Instrumentos de rayos X](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md).

### Área entre curvas

- El área entre curvas es `∫_a^b [f(x) − g(x)] dx` con `f ≥ g` (S1, §1.4(v)).

💡 **Contexto en la clase [B09-C13](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md):**
- **Idea central (modelo mental):** Cualquier cantidad geométrica se obtiene rebanando el objeto en piezas de forma conocida (discos, cilindros huecos, tiras) y sumando con una integral. Lo esencial es elegir las rebanadas de modo que su aporte sea una fórmula sencilla de la variable de integración.
- 🎯 **Por qué importa:** Un telescopio necesita un espejo con forma de paraboloide. Cuánto vidrio hay que retirar de un disco plano para darle forma, cuánto pesa, y cuánta superficie hay que aluminizar son preguntas de volumen y área.
- 🔗 **Se estudia junto con:** sólido de revolución, método de los discos, método de los cascarones, longitud de arco.

📘 **Dónde se aprende** (1 clase): [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md).

### Área expuesta

- El área expuesta `A_c` es la superficie efectiva de una persona.

💡 **Cómo se explica en la clase [B119-C22](../programa/clases/B119/B119-C22-seguridad-de-instalaciones-y-operaciones-de-sitio-de-lanzamiento/CLASE.md):**
- El ejemplo conductor: 200 fragmentos con velocidad lognormal (mediana 70 m/s, `σ = 0,4`), 0,5 m² de área expuesta por persona y 100 personas por km² fuera de la zona.
- 🎯 **Por qué importa:** B77-C19 solo ve seguridad de rango de forma conceptual; esta clase cuantifica el razonamiento y lo liga a la responsabilidad del Estado por actividades privadas (art. VI) y al régimen de daños (C03).
- 🔗 **Se estudia junto con:** zona de exclusión, alcance, esperanza de bajas, densidad.

📘 **Dónde se aprende** (1 clase): [B119-C22 · Seguridad de instalaciones y operaciones de sitio de lanzamiento](../programa/clases/B119/B119-C22-seguridad-de-instalaciones-y-operaciones-de-sitio-de-lanzamiento/CLASE.md).

### Área requerida

- El área requerida es `A = Q/flujo_neto`.

💡 **Cómo se explica en la clase [B85-C07](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md):**
- El absorbido aumenta y el área requerida crece; hay que reducir el factor de forma con la actitud o la orientación.
- 🎯 **Por qué importa:** El área del radiador manda en masa, volumen y costo. La decisión central: ¿cuánta área necesita un radiador en el caso caliente de fin de vida y qué la reduce?
- 🔗 **Se estudia junto con:** flujo neto, aleta radiante, eficiencia, espacio profundo.

📘 **Dónde se aprende** (1 clase): [B85-C07 · Radiadores espaciales](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md).

### Área superficial

- La sección eficaz geométrica es `π a²`; el área superficial es `4π a²`.
- Una esfera de radio `r` tiene área superficial `4πr²` y volumen `(4/3)πr³`.

💡 **Cómo se explica en la clase [B03-C17](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md):**
- Para la Tierra con radio medio, el área superficial es `5,1006 × 10⁸ km²`; el volumen, `1,0832 × 10¹² km³`.
- Ejercicio 3 · casi autónomo. Calcula el área superficial de la Tierra (esfera de radio 6 371 km).
- 🎯 **Por qué importa:** La NASA publica que la densidad media del Sol es 1408 kg/m³ (S1), cerca de una vez y media la del agua. ¿Cómo se obtiene?
- 🔗 **Se estudia junto con:** perímetro, área, esfera, volumen.

📘 **Dónde se aprende** (2 clases): [B03-C17 · Áreas y volúmenes elementales](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md); [B55-C05 · Granos de polvo interestelar](../programa/clases/B55/B55-C05-granos-de-polvo-interestelar/CLASE.md).

### Areoide

- Un areoide es el geoide de Marte.

💡 **Cómo se explica en la clase [B53-C06](../programa/clases/B53/B53-C06-geodesia-de-marte/CLASE.md):**
- Ejercicio 11 · transferencia. ¿Qué altura da el altímetro: elipsoidal o sobre areoide?
- Límites: elipsoide de revolución sin topografía ni areoide.
- ⚠️ **Error frecuente:** Confundir altura elipsoidal con sobre el areoide. se corrige con la sección 6
- 🎯 **Por qué importa:** Una altura de 1 km no significa lo mismo sobre una esfera que sobre un elipsoide. La decisión central: ¿qué latitud y qué referencia usa cada producto, y cuánto difieren?
- 🔗 **Se estudia junto con:** latitud planetográfica, planetocéntrica, altura elipsoidal.

📘 **Dónde se aprende** (1 clase): [B53-C06 · Geodesia de Marte](../programa/clases/B53/B53-C06-geodesia-de-marte/CLASE.md).

### ARF

- La ARF es el área efectiva en función de la energía.

💡 **Cómo se explica en la clase [B27-C22](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md):**
- M["modelo K(E/3)^−Γ"] --> A["× ARF × exposición × ΔE"]
- El manual de XSPEC describe el ajuste de modelos a datos con respuesta (S2, página consultada sin las definiciones de `χ²`, C-stat, RMF ni ARF); el telescopio Fermi-LAT cubre de menos de `20 MeV` a más de `300 GeV` (S3, resumen).
- 🎯 **Por qué importa:** Ajustar un espectro «de fotones» directamente a las cuentas da resultados engañosos; hay que plegar el modelo con la respuesta y usar la estadística correcta para conteos pequeños. La decisión central: ¿qué parámetros recupera cada estadística y con qué sesgo cuando las cuentas son pocas?
- 🔗 **Se estudia junto con:** RMF, plegado, estadística de Cash, χ² con varianza igual a las cuentas.

📘 **Dónde se aprende** (1 clase): [B27-C22 · Análisis espectral de rayos X y gamma: ajuste con respuesta instrumental](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md).

### Argumento

- Un parámetro es el nombre que la función da a un dato de entrada; un argumento es el valor concreto que le pasas al llamarla.

💡 **Cómo se explica en la clase [B07-C06](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md):**
- Los argumentos se asignan por posición o por nombre: `periodo_predicho(4.0, exponente=2)` pasa `2` al parámetro `exponente`.
- A["argumentos<br/>a_rel, t_anios"] --> F["función razon_kepler<br/>variables locales"]
- 🎯 **Por qué importa:** Copiar y pegar el mismo cálculo en cinco sitios es la forma más rápida de tener cinco versiones distintas y un error corregido solo en una. Una función concentra la lógica en un lugar, le da un nombre que expresa su intención y permite probarla aislada.
- 🔗 **Se estudia junto con:** función, parámetro, valor devuelto, efecto secundario.

📘 **Dónde se aprende** (1 clase): [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md).

### Argumento de latitud

- El argumento de latitud `u = ω + ν` va del nodo al satélite.

💡 **Cómo se explica en la clase [B71-C12](../programa/clases/B71/B71-C12-argumento-del-periapsis/CLASE.md):**
- Calcular el argumento de latitud `u = ω + ν` por dos vías.
- 🎯 **Por qué importa:** Un elemento mal condicionado puede dar un valor sin sentido aunque el estado sea exacto. La decisión central: ¿cuándo puedes fiarte de `ω` y qué ángulo usas cuando no?
- 🔗 **Se estudia junto con:** argumento del periapsis, mal condicionamiento, inclinación crítica, elemento indefinido.

📘 **Dónde se aprende** (1 clase): [B71-C12 · Argumento del periapsis](../programa/clases/B71/B71-C12-argumento-del-periapsis/CLASE.md).

### Argumento del periapsis

- El argumento del periapsis `ω` va del nodo ascendente al periapsis, en el plano orbital.

💡 **Cómo se explica en la clase [B71-C12](../programa/clases/B71/B71-C12-argumento-del-periapsis/CLASE.md):**
- python programa/clases/B71/B71-C12-argumento-del-periapsis/argumento_periapsis.py
- 🎯 **Por qué importa:** Un elemento mal condicionado puede dar un valor sin sentido aunque el estado sea exacto. La decisión central: ¿cuándo puedes fiarte de `ω` y qué ángulo usas cuando no?
- 🔗 **Se estudia junto con:** argumento de latitud, mal condicionamiento, inclinación crítica, elemento indefinido.

📘 **Dónde se aprende** (1 clase): [B71-C12 · Argumento del periapsis](../programa/clases/B71/B71-C12-argumento-del-periapsis/CLASE.md).

### Argumento del periastro

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B29-C03](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md):**
- **Idea central (modelo mental):** Un bailarín pesado (la estrella) y uno ligero (el planeta) giran alrededor del centro de masas: el pesado traza un círculo pequeño; si miramos desde el borde del escenario vemos que se acerca y se aleja con una velocidad `K`.
- 🎯 **Por qué importa:** La velocidad radial da la masa mínima del planeta, que el tránsito no da. Combinados, dan la densidad.
- 🔗 **Se estudia junto con:** semiamplitud, anomalía media, ecuación de Kepler, masa mínima.

📘 **Dónde se aprende** (1 clase): [B29-C03 · Velocidad radial estelar](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md).

### Argumento resonante

- El argumento resonante es el ángulo `φ = pλ₂ − qλ₁ − …` y libra si oscila alrededor de un valor.

💡 **Cómo se explica en la clase [B73-C10](../programa/clases/B73/B73-C10-resonancias-de-movimiento-medio/CLASE.md):**
- Una razón cercana a un racional es un indicio, no una demostración: la resonancia exige que el argumento resonante libre (no circule), lo que requiere longitudes y no solo periodos.
- Paso 4 · Lectura. La línea de conjunción da una vuelta en `≈ 1,3 años`: esa es la escala del argumento resonante.
- 🎯 **Por qué importa:** Una razón de periodos cercana a un número racional es el primer indicio de una resonancia, pero puede engañar si la fuente usa periodos instantáneos en lugar de medios. La decisión central: ¿qué periodos puedo usar para afirmar que hay una resonancia y qué puedo y no puedo concluir?
- 🔗 **Se estudia junto con:** resonancia de movimiento medio, libra, circulación, relación de Laplace.

📘 **Dónde se aprende** (1 clase): [B73-C10 · Resonancias de movimiento medio](../programa/clases/B73/B73-C10-resonancias-de-movimiento-medio/CLASE.md).

### Aritmética extendida

- La aritmética extendida usa más dígitos que la doble precisión (aquí el módulo `decimal` con 40 dígitos, S2).

💡 **Contexto en la clase [B11-C21](../programa/clases/B11/B11-C21-integracion-numerica-de-alta-precision/CLASE.md):**
- **Idea central (modelo mental):** Mirar el mismo tramo con 2, 4, 6… subpasos da respuestas cada vez mejores, y los errores siguen un patrón predecible; con ese patrón se «adivina» el límite a paso cero.
- 🎯 **Por qué importa:** Una trayectoria de millones de vueltas, un encuentro cercano que exige metros de precisión o una comprobación contra otro código piden errores de truncamiento muy por debajo del que da RK4 a costo razonable. A orden alto el costo por precisión baja mucho, pero el error de redondeo pasa a ser el límite.
- 🔗 **Se estudia junto con:** punto medio modificado, extrapolación de Richardson, Gragg–Bulirsch–Stoer, macro-paso.

📘 **Dónde se aprende** (1 clase): [B11-C21 · Integración numérica de alta precisión](../programa/clases/B11/B11-C21-integracion-numerica-de-alta-precision/CLASE.md).

### ARL

- El ARL es la longitud media de racha: `ARL₀` en control (falsas alarmas) y `ARL₁` bajo desplazamiento.
- El ARL₀ es la longitud media hasta una falsa alarma.

💡 **Cómo se explica en la clase [B84-C35](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md):**
- *Descripción textual:* los subgrupos alimentan las dos cartas; la simulación da los ARL, que se contrastan con la teoría;
- ARL en control: `369,7` (teórica `370,4`); con `+1σ`, Shewhart `4,50` y EWMA `2,31`.
- 🎯 **Por qué importa:** Un proceso con `Cpk` de 1,33 puede desplazarse 1σ sin dejar piezas fuera de tolerancia durante semanas si solo se inspecciona el producto; la carta lo detecta en pocos subgrupos. La decisión central: ¿qué carta detecta antes un desplazamiento del proceso y qué capacidad tiene el proceso antes y después?
- 🔗 **Se estudia junto con:** carta X-barra, EWMA.

📘 **Dónde se aprende** (2 clases): [B84-C35 · Control de procesos de fabricación y calidad](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md); [B97-C22 · Detección autónoma de eventos científicos](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md).

### Armado

- Aprobación: visto bueno de otra persona. Armado: habilitación explícita previa.

💡 **Cómo se explica en la clase [B96-C07](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md):**
- Se evalúan `3 × 4 × 5 × 2 = 120` combinaciones (rol, criticidad, cinco listas de aprobaciones, armado sí/no) con la política y con una referencia independiente basada en tablas de mínimos.
- (1) Ningún comando peligroso se permite sin armado.
- 🎯 **Por qué importa:** Un comando enviado por la persona equivocada o sin segunda revisión puede perder la misión. La decisión central: ¿qué rol, qué aprobaciones y qué armado exige cada nivel de criticidad y cómo se prueba que la política no tiene huecos?
- 🔗 **Se estudia junto con:** Criticidad, Rol, Aprobación, Referencia independiente.

📘 **Dónde se aprende** (1 clase): [B96-C07 · Telecomandos y autorizaciones](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md).

### Armónico

- Un armónico es una frecuencia múltiplo de la fundamental.
- La emisión fundamental está en `f_p`, el armónico en `2f_p`.
- Aislamiento: atenuación entre fuente y víctima. Armónico: componente a múltiplo de la frecuencia del transmisor.

💡 **Cómo se explica en la clase [B29-C14](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md):**
- Con el periodo verdadero `5,3 d`: ajuste de un armónico `5,29808 d`; tres armónicos `5,29909 d`;
- Para una sinusoide pura de amplitud `0,316 mag` (la fundamental de los armónicos dados) en 60 realizaciones: periodo `5,29991 ± 0,00196 d`, frente a la `σ_P` teórica `0,00190 d` (diferencia del `3 %`).
- 🎯 **Por qué importa:** El periodo es la propiedad básica de una variable periódica; de él y de la forma de la curva se deducen la masa, la edad o la distancia en muchos casos. La decisión central: ¿qué periodo y qué incertidumbre da la serie y qué métodos coinciden?
- 🔗 **Se estudia junto con:** curva de fase, dispersión de fase, rejilla de frecuencias, amplitud.

📘 **Dónde se aprende** (4 clases): [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md); [B30-C21 · Radioemisión solar: estallidos de radio y su observación](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md); [B58-C13 · Caracterización de rotación](../programa/clases/B58/B58-C13-caracterizacion-de-rotacion/CLASE.md); [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md).

### Armónico esférico

- El armónico esférico `Y_l^m` tiene grado `l` y orden azimutal `m`.

💡 **Contexto en la clase [B37-C08](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md):**
- **Idea central (modelo mental):** Es como un tambor (la tensión restaura: p) y un péndulo (el peso restaura: g). El tambor suena agudo y el péndulo lento; una estrella tiene ambos.
- 🎯 **Por qué importa:** Los modos p y g sondean regiones distintas. La decisión central: ¿en qué cavidad se propaga un modo de frecuencia y grado dados?
- 🔗 **Se estudia junto con:** modo p, g, frecuencia de Lamb, frecuencia de Brunt–Väisälä.

📘 **Dónde se aprende** (1 clase): [B37-C08 · Oscilaciones no radiales: modos p, g y mixtos](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md).

### Armónico zonal

- Un armónico zonal `J_n` es el coeficiente de un término que solo depende de la latitud.

💡 **Cómo se explica en la clase [B72-C02](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md):**
- La evidencia es la tabla de armónicos zonales del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *tabla de armónicos zonales*: J2, J3 y J4 relativos a `μ/r²` a 400 km en cuatro latitudes, con la verificación del gradiente y la lista de lo consultado, lo ilustrativo y lo no consultado.
- 🎯 **Por qué importa:** Sin un potencial no hay perturbación gravitatoria que calcular, y los números de la bibliografía (J2, J3, J4) dependen de un convenio de signos y de un radio de referencia. La decisión central: ¿qué términos del potencial incluir y con qué radio y convenio, para que J2 signifique lo mismo en tu código y en la fuente?
- 🔗 **Se estudia junto con:** J2, polinomio de Legendre, convenio de signos, gradiente.

📘 **Dónde se aprende** (1 clase): [B72-C02 · Potencial gravitatorio no esférico](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md).

### Armónicos esféricos

- Los armónicos esféricos descomponen el campo; el grado `l` fija la resolución `πR/l`.

💡 **Cómo se explica en la clase [B57-C14](../programa/clases/B57/B57-C14-glaciares-y-criosfera/CLASE.md):**
- Relacionar el grado de los armónicos esféricos con la resolución espacial.
- 🎯 **Por qué importa:** Un glaciar que baja medio metro puede haber perdido mucha o poca masa según lo que se pierda sea hielo o nieve. La decisión central: ¿qué densidad uso para convertir cambios de altura en masa y cuánto cambia el resultado?
- 🔗 **Se estudia junto con:** equivalente en nivel del mar, gravimetría, grado, firn.

📘 **Dónde se aprende** (1 clase): [B57-C14 · Glaciares y criósfera](../programa/clases/B57/B57-C14-glaciares-y-criosfera/CLASE.md).

### Arnés

- El arnés es el conjunto de cables.
- Bus de potencia: red que distribuye la energía. Arnés: conjunto de cables y conectores.

💡 **Cómo se explica en la clase [B86-C07](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md):**
- Paso 4 · Pérdida. `R I²`; en el bus de `28 V` el total del arnés es `1,039 W`.
- Resolver la corriente de una carga de potencia constante con caída en el arnés.
- ⚠️ **Error frecuente:** Presentar el arnés sintético como real. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Un cable largo y fino desperdicia potencia y baja la tensión que ve el equipo; uno grueso pesa. La tensión del bus cambia la corriente, y por tanto las pérdidas, con el cuadrado.
- 🔗 **Se estudia junto con:** caída de tensión, carga de potencia constante, colapso de tensión, bus regulado.

📘 **Dónde se aprende** (2 clases): [B86-C07 · Distribución de potencia](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md); [B90-C07 · Integración eléctrica de buses](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md).

### Aromático

- Un hidrocarburo contiene sólo carbono e hidrógeno: alcano (enlaces simples, `CₙH₂ₙ₊₂`, como el metano `CH₄`), alqueno (un doble enlace, `CₙH₂ₙ`, como el eteno `C₂H₄`), alquino (un triple enlace) y aromático (anillos con enlaces alternados, como el benceno `C₆H₆`).

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- H --> A3["Aromático: C6H6, insaturación 4"]
- La primera son los hidrocarburos: alcanos (insaturación 0), alquenos (1) y aromáticos como el benceno (4).
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).
- 🔗 **Se estudia junto con:** química orgánica, hidrocarburo, alcano, alqueno.

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### ARPA

- El ARPA es el ingreso medio por cliente y mes.

💡 **Cómo se explica en la clase [B126-C04](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md):**
- El ejemplo conductor es un servicio sintético de datos de observación de la Tierra por suscripción: gasto de captación de 240 000 USD por trimestre con 60 clientes nuevos, ingreso mensual por cliente (ARPA) de 900 USD, margen bruto de 70 % y abandono mensual de 2 %.
- 🎯 **Por qué importa:** Un negocio espacial debe medir cuánto cuesta ganar un cliente; el catálogo no lo trata. La decisión central: ¿vale la pena el gasto de captación, dado cuánto tiempo se queda el cliente y cuánto margen deja?
- 🔗 **Se estudia junto con:** CAC, margen bruto, abandono, LTV.

📘 **Dónde se aprende** (1 clase): [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### ARPU

- El ARPU es el ingreso por suscriptor y mes.
- El ARPU es el ingreso mensual medio por cliente.

💡 **Cómo se explica en la clase [B124-C11](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md):**
- Si la vida útil baja a 3,5 años el equilibrio sube a `78333` (`1,21` veces); si sube a 7, baja a `55833`; si el ARPU cae a 40 um/mes, sube a `81042`.
- *Descripción textual:* la flota y su vida dan la tasa de reposición, que se verifica por simulación; esta, más el costo operativo, da el costo anual y, con el ARPU, el equilibrio en suscriptores.
- 🎯 **Por qué importa:** Una constelación puede ser técnicamente exitosa y económicamente inviable si la reposición se come el margen. La decisión central: ¿cuántos suscriptores se necesitan para cubrir la reposición y la operación, y qué tan sensible es eso a la vida útil?
- 🔗 **Se estudia junto con:** reposición, tasa de renovación, reserva de desorbitación, punto de equilibrio.

📘 **Dónde se aprende** (2 clases): [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md); [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md).

### ARQ

- Ráfaga: error en bits consecutivos. ARQ: retransmisión automática.

💡 **Contexto en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?
- 🔗 **Se estudia junto con:** Prueba de extremo a extremo, CRC, BER, FER.

📘 **Dónde se aprende** (1 clase): [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### Arqueoastronomía

- La arqueoastronomía estudia las prácticas astronómicas de culturas antiguas, incluidas las orientaciones de sitios y estructuras; la astronomía cultural es el término más amplio, que incluye también tradiciones vivas (S2).

💡 **Cómo se explica en la clase [B02-C08](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md):**
- Definir arqueoastronomía y astronomía cultural como campos interdisciplinarios.
- python programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/azimut_a_declinacion.py
- 🎯 **Por qué importa:** Decir «esta puerta mira al solsticio» es fácil; demostrarlo es difícil. Hay que medir bien, conocer el horizonte, descartar el azar y entender el contexto cultural.
- 🔗 **Se estudia junto con:** astronomía cultural, orientación, azimut, altura del horizonte.

📘 **Dónde se aprende** (1 clase): [B02-C08 · Arqueoastronomía y sus métodos](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md).

### Arquitectura

- La arquitectura es el conjunto de semiejes, masas y excentricidades de un sistema.
- ECLSS: sistema de control ambiental y soporte vital. Arquitectura: combinación de subsistemas.

💡 **Cómo se explica en la clase [B52-C10](../programa/clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md):**
- La evidencia es la ficha de la arquitectura de un sistema del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Integrador. Elabora tu *ficha de la arquitectura de un sistema*: tablas 8.1 y 8.2, sistema sintético y límites.
- 🎯 **Por qué importa:** El espaciado mide cuán «apretado» está un sistema y cuán cerca está de la inestabilidad. La decisión central: ¿cómo se expresa el espaciado entre planetas independientemente de su escala?
- 🔗 **Se estudia junto con:** radio de Hill mutuo, espaciado, razón de periodos.

📘 **Dónde se aprende** (2 clases): [B52-C10 · Arquitecturas de sistemas exoplanetarios](../programa/clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md); [B106-C09 · Sistemas ECLSS](../programa/clases/B106/B106-C09-sistemas-eclss/CLASE.md).

### Arquitectura candidata

- Una arquitectura candidata es una organización posible del sistema.

💡 **Contexto en la clase [B83-C07](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md):**
- 🎯 **Por qué importa:** Elegir una arquitectura «porque sí» es una decisión sin rastro. La decisión central: ¿qué arquitectura conviene, con qué criterios y qué tan firme es la elección?
- 🔗 **Se estudia junto con:** estudio de compromiso, AHP, razón de consistencia, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B83-C07 · Arquitecturas de sistemas](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md).

### Arranque en caliente

- El arranque en caliente reutiliza la solución anterior desplazada.

💡 **Cómo se explica en la clase [B87-C21](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md):**
- FISTA con 1500 iteraciones por paso (arranque en caliente) converge: la diferencia máxima entre la solución a 1500 y a 15 000 iteraciones es `0,623 %` del límite y el residuo del gradiente proyectado `7,11e-01`.
- Aplicar el horizonte deslizante con arranque en caliente.
- 🎯 **Por qué importa:** Un PD satura el par y no sabe de límites de velocidad: puede superar el máximo de la rueda o de la carga útil. La decisión central: ¿cómo formular un problema que respete par y velocidad, cuánto cuesta calcularlo y qué se gana?
- 🔗 **Se estudia junto con:** MPC, horizonte, QP condensado, restricción dura.

📘 **Dónde se aprende** (1 clase): [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md).

### Arranque en frío

- El arranque en frío es el periodo en que aún no vuelve material.

💡 **Cómo se explica en la clase [B59-C15](../programa/clases/B59/B59-C15-ciclo-cerrado-de-materiales/CLASE.md):**
- En 500 días, con arranque en frío y retardo de 3 días, la reposición es `1 650,7 kg` frente a `12 500 kg` sin lazo (ahorro `86,8 %`).
- Distinguir el arranque en frío del régimen.
- ⚠️ **Error frecuente:** Olvidar el arranque en frío. Se corrige con 8.2.
- 🎯 **Por qué importa:** Cerrar el 87 % de un lazo no deja una reposición del 13 % sino una dependencia permanente del 13 %. La decisión central: ¿qué etapa del lazo conviene mejorar para reducir más la reposición?
- 🔗 **Se estudia junto con:** recuperación global, reposición, retardo, ciclos por kg de reposición.

📘 **Dónde se aprende** (1 clase): [B59-C15 · Ciclo cerrado de materiales](../programa/clases/B59/B59-C15-ciclo-cerrado-de-materiales/CLASE.md).

### Arranque múltiple

- El arranque múltiple ejecuta un método local (L-BFGS-B) desde varios puntos.

💡 **Cómo se explica en la clase [B81-C13](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md):**
- Sobre la función de Rastrigin en dos variables (mínimo global `f = 0` en el origen y mínimos locales en los enteros), con 30 repeticiones: el enjambre acierta 30 de 30 con 2430 evaluaciones; el genético 24 de 30 con 2440; el arranque múltiple de 20 inicios locales solo 5 de 30 con 792; un solo arranque local, 0 de 30.
- Descripción larga: con presupuestos de evaluaciones parecidos, los heurísticos superan al arranque múltiple local en esta función multimodal.
- 🎯 **Por qué importa:** Un método heurístico no garantiza el óptimo, pero puede evitar los mínimos locales. La decisión central: ¿qué método global elegir y cuántas evaluaciones se gastan para una tasa de éxito dada?
- 🔗 **Se estudia junto con:** algoritmo genético, enjambre de partículas, éxito.

📘 **Dónde se aprende** (1 clase): [B81-C13 · Optimización heurística (algoritmos genéticos y enjambres)](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md).

### Arrastre

- El arrastre es la traza que deja un objeto que se mueve durante la exposición.
- El arrastre `φ` es la fracción de la concentración de la salmuera que pasa al vapor.
- El arrastre es `D = Cd·(ρV²/2)·A`.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B54-C07](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md):**
- Límite: el globo es un objeto cerrado; la parcela se mezcla y pierde energía por arrastre y por el peso de las gotas.
- Por balance de momento con arrastre: incluye mezcla (no se desarrolla aquí).
- 🎯 **Por qué importa:** La energía convectiva disponible decide si una tormenta tiene vigor o no. La pregunta motivadora: ¿cuánta velocidad puede alcanzar el aire que sube si toda la flotabilidad se convierte en movimiento?
- 🔗 **Se estudia junto con:** CAPE, flotabilidad, parcela.

📘 **Dónde se aprende** (9 clases): [B54-C07 · Dinámica de tormentas](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md); [B58-C06 · Astrometría de objetos menores](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md); [B59-C07 · Purificación de agua](../programa/clases/B59/B59-C07-purificacion-de-agua/CLASE.md); [B77-C02 · Movimiento en atmósfera](../programa/clases/B77/B77-C02-movimiento-en-atmosfera/CLASE.md); [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md); [B77-C09 · Pérdidas aerodinámicas](../programa/clases/B77/B77-C09-perdidas-aerodinamicas/CLASE.md) y 3 más.

### Arreglo

- NumPy es una biblioteca para cálculo numérico; su estructura central es el arreglo (`ndarray`): una rejilla de elementos del mismo tipo con tamaño fijo (S2).
- Un arreglo (`ndarray`) es una tabla de valores del mismo tipo.

💡 **Cómo se explica en la clase [B07-C09](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md):**
- Un arreglo es una columna de una hoja de cálculo; una operación vectorizada es escribir una fórmula en la primera celda y arrastrarla hacia abajo, pero hecha de una sola vez y sin errores de arrastre.
- Límite de la analogía: una hoja de cálculo mezcla tipos libremente; un arreglo de NumPy tiene un solo `dtype`, y eso lo hace rápido pero obliga a que todos los elementos sean del mismo tipo.
- ⚠️ **Error frecuente:** Mezclar listas con arreglos. `lista * 2` repite;
- 🎯 **Por qué importa:** Calcular la densidad de ocho planetas con un `for` funciona, pero a escala de millones de datos es lento y verboso. NumPy opera sobre arreglos completos con una sola expresión y es la base de casi toda la ciencia con Python.
- 🔗 **Se estudia junto con:** NumPy, vectorizada, difusión, densidad media.

📘 **Dónde se aprende** (2 clases): [B07-C09 · Cálculos científicos básicos con Python](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md); [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md).

### Arreglo de antenas

- El arreglo de antenas (*arraying*) combina señales de varias antenas.

💡 **Cómo se explica en la clase [B91-C08](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md):**
- Comparar una antena de 70 m con una de 34 m escalada y con un arreglo de cuatro antenas.
- 🎯 **Por qué importa:** Un enlace a distancias de unidades astronómicas pierde unos 280 dB: solo se cierra con una estación enorme y de ruido muy bajo. La decisión central: ¿qué antena de estación (una de 70 m, una de 34 m o un arreglo de varias) permite la velocidad de datos pedida, y cuánto cuesta un error de apuntamiento?
- 🔗 **Se estudia junto con:** EIRP, figura de mérito G/T, pérdida por apuntamiento, pérdida de espacio libre.

📘 **Dónde se aprende** (1 clase): [B91-C08 · Antenas de gran apertura y estaciones de espacio profundo](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md).

### Arreglo de Routh

- El arreglo de Routh es una tabla construida con los coeficientes; el criterio de Routh–Hurwitz dice que el número de cambios de signo en su primera columna es el número de raíces con parte real positiva.

💡 **Cómo se explica en la clase [B16-C08](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md):**
- A["Coeficientes del polinomio"] --> B["Arreglo de Routh<br/>filas s^n, s^n-1, ..."]
- *Descripción textual:* de los coeficientes se construye el arreglo de Routh por filas; se lee su primera columna; el número de cambios de signo es el número de raíces inestables.
- 🎯 **Por qué importa:** Al diseñar un lazo, la ganancia `K` es una incógnita que quieres elegir. Calcular las raíces para cada `K` es posible con un computador, pero no da la frontera: el valor exacto de `K` por encima del cual el sistema se desestabiliza.
- 🔗 **Se estudia junto con:** polinomio característico, Hurwitz, criterio de Routh–Hurwitz, ganancia crítica.

📘 **Dónde se aprende** (1 clase): [B16-C08 · Criterio de Routh-Hurwitz](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md).

### Artefacto

- Un artefacto es una estructura generada por el procesado, no presente en el objeto.

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- No garantiza el flujo local (el pico de 505 solo llegó a 131,8), ni evita artefactos (anillos, picos).
- La evidencia es la deconvolución con medida de mejora y de artefactos del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.
- 🔗 **Se estudia junto con:** PSF, gaussiana, FWHM, desenfoque.

📘 **Dónde se aprende** (1 clase): [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md).

### Artefacto de movimiento

- El artefacto de movimiento es la parte de la señal causada por el movimiento y no por el pulso.

💡 **Cómo se explica en la clase [B116-C01](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md):**
- Descripción larga: el error es nulo hasta que el movimiento iguala al pulso y de ahí salta; la ventana mejora la resolución pero no arregla un artefacto dominante.
- Identificar cuándo el artefacto de movimiento domina y el estimador se engancha a la cadencia.
- 🎯 **Por qué importa:** Una pulsera que da «72 lpm» no dice «72 ± 0,1». Con movimiento puede dar 120 cuando el pulso real es 70.
- 🔗 **Se estudia junto con:** fotopletismografía (PPG), frecuencia cardiaca, resolución espectral, Bland–Altman.

📘 **Dónde se aprende** (1 clase): [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Artículo arbitrado

- Un artículo arbitrado es el que pasó por revisión de especialistas (se verá en C03).

💡 **Contexto en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- **Idea central (modelo mental):** Piensa en un embudo de cuatro etapas. Arriba entran todos los resultados que devuelven las consultas; cada etapa descarta algo por una razón que se escribe; abajo queda el conjunto que se leerá.
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.
- 🔗 **Se estudia junto con:** pregunta de revisión, cadena de consulta, operador lógico, criterios de inclusión y exclusión.

📘 **Dónde se aprende** (1 clase): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md).

### Artículo de investigación original

- Un artículo de investigación original es el que presenta datos y análisis nuevos.

💡 **Contexto en la clase [B20-C04](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md):**
- **Idea central (modelo mental):** Un artículo es una cadena de afirmaciones, cada una apoyada por evidencia y acotada por un límite. La introducción dice qué se sabía y qué faltaba; los métodos, qué se hizo, con qué datos y qué reglas se fijaron antes; los resultados, qué salió, con su incertidumbre; la discusión, qué significa y qué no puede concluirse.
- 🎯 **Por qué importa:** Un resultado correcto mal comunicado se pierde: nadie sabe qué se midió, con qué incertidumbre ni qué supuestos hay detrás, y no puede reproducirse ni usarse.
- 🔗 **Se estudia junto con:** IMRaD, resumen, afirmación, evidencia.

📘 **Dónde se aprende** (1 clase): [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### ARW

- El ARW (*angle random walk*) `N` es el ruido blanco de la tasa, en `rad/√s`.

💡 **Cómo se explica en la clase [B87-C06](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md):**
- G["tasa medida = verdad + ARW + sesgo RRW"] --> P["promedios de duracion tau"]
- Analogía: un reloj que se adelanta con un tic aleatorio (ARW) y que además cambia de ritmo a lo largo del día (RRW): para periodos cortos domina el tic y para largos domina el cambio de ritmo.
- 🎯 **Por qué importa:** Entre dos medidas de un sensor de vector, la actitud se propaga integrando el giroscopio, y esa integración se desvía. La decisión central: ¿cada cuánto hay que corregir con otro sensor, y qué parte de la deriva es ruido blanco y cuál sesgo?
- 🔗 **Se estudia junto con:** RRW, varianza de Allan, inestabilidad de sesgo, tasa de muestreo.

📘 **Dónde se aprende** (1 clase): [B87-C06 · Giroscopios MEMS](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md).

### Ascendente

- El muestreo descendente reduce la resolución (p. ej., agrupando 2 × 2) para captar contexto; el ascendente la restituye.

💡 **Contexto en la clase [B17-C11](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md):**
- 🎯 **Por qué importa:** Delimitar una mancha solar, una nube o un cráter a mano en miles de imágenes no escala. Un umbral por píxel falla cuando el ruido es comparable al contraste.
- 🔗 **Se estudia junto con:** segmentación semántica, máscara, convolución, válido.

📘 **Dónde se aprende** (1 clase): [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md).

### Ascendente/descendente

- Una franja es un ciclo de 2π. Ascendente/descendente son las dos geometrías de órbita.

💡 **Cómo se explica en la clase [B69-C06](../programa/clases/B69/B69-C06-deslizamientos-y-subsidencia-medidos-con-insar/CLASE.md):**
- Un deslizamiento sintético de 12 mm/año al este y −5 mm/año vertical se ve como −10,75 mm/año desde la órbita ascendente y +2,46 mm/año desde la descendente.
- Ejercicio 12 · integrador. Elabora tu *ficha de la deformación*: el perfil de subsidencia, la reconstrucción con error, el límite del gradiente y la descomposición ascendente–descendente.
- ⚠️ **Error frecuente:** Olvidar la geometría ascendente/descendente. Se corrige con 8.5.
- 🎯 **Por qué importa:** Un solo interferograma no dice si el suelo bajó o se movió al este. La decisión central: ¿qué parte del movimiento real mide la línea de visión, hasta qué gradiente se puede desenvolver y qué se puede concluir?
- 🔗 **Se estudia junto con:** desplazamiento en la línea de visión, Desenvolver, franja, subsidencia.

📘 **Dónde se aprende** (1 clase): [B69-C06 · Deslizamientos y subsidencia medidos con InSAR](../programa/clases/B69/B69-C06-deslizamientos-y-subsidencia-medidos-con-insar/CLASE.md).

### Ascensión recta

- La ascensión recta es una coordenada celeste que se expresa en horas, minutos y segundos de tiempo (se desarrolla en B08).
- En astronomía se usan la ascensión recta `α` (equivalente a `φ`) y la declinación `δ` (que se mide desde el ecuador: `δ = 90° − θ`, de −90° a +90°).
- La ascensión recta (AR, `α`) es el ángulo, medido hacia el este sobre el ecuador celeste, entre el punto vernal (un punto del ecuador que sirve de origen) y el círculo que une los polos con el astro; se expresa en horas (24 h = 360°).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C08](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md):**
- Esto relaciona la ascensión recta en horas con grados: `6 h = 90°`.
- Relacionar horas de ascensión recta con grados (15° por hora).
- 🎯 **Por qué importa:** El período de Neptuno en las fichas de la NASA es 60 189,018 días. Nadie piensa en 60 mil días; se piensa en años.
- 🔗 **Se estudia junto con:** segundo, minuto, hora, día.

📖 **Explicado a fondo:** [Ascensión recta y declinación](esencial/esencial-a-c.md#ascensión-recta-y-declinación) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B03-C08 · Tiempo y conversiones astronómicas](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md); [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md); [B08-C03 · Ascensión recta y declinación](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md); [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md).

### Ascensión recta del nodo ascendente

- El nodo ascendente es el punto donde la órbita cruza el ecuador hacia el norte; su longitud es la ascensión recta del nodo ascendente (`Ω` o RAAN).

💡 **Contexto en la clase [B71-C11](../programa/clases/B71/B71-C11-inclinacion-y-nodo-ascendente/CLASE.md):**
- 🎯 **Por qué importa:** Un error de cuadrante en `Ω` coloca el plano a 180° de su sitio. La decisión central: ¿cómo obtienes `i` y `Ω` sin ambigüedad y qué latitudes puede alcanzar una órbita con esa inclinación?
- 🔗 **Se estudia junto con:** inclinación, línea de nodos, nodo ascendente, vector nodo.

📘 **Dónde se aprende** (1 clase): [B71-C11 · Inclinación y nodo ascendente](../programa/clases/B71/B71-C11-inclinacion-y-nodo-ascendente/CLASE.md).

### ASD

- La ASD (*acceleration spectral density*) es `G(f)` en g²/Hz.

💡 **Cómo se explica en la clase [B84-C01](../programa/clases/B84/B84-C01-entorno-mecanico-de-lanzamiento/CLASE.md):**
- La aceptación es la mitad de la ASD (−3 dB) y su `g` rms es `14,14/√2 ≈ 10,0`.
- A["ASD por tramos<br/>f, G"] --> B["exponente m<br/>por tramo"]
- 🎯 **Por qué importa:** Un satélite no falla en órbita por el empuje del motor sino por la sacudida de la subida; esa sacudida se especifica con un espectro, no con un número. Un espectro con 0,16 g²/Hz de meseta no dice nada hasta que se integra.
- 🔗 **Se estudia junto con:** valor eficaz, Calificación, aceptación, mano de obra mínima.

📘 **Dónde se aprende** (1 clase): [B84-C01 · Entorno mecánico de lanzamiento](../programa/clases/B84/B84-C01-entorno-mecanico-de-lanzamiento/CLASE.md).

### ASET

- El ASET (*available safe egress time*) es el tiempo disponible antes de que el peligro impida la salida; aquí se toma igual a `T_Res`.

💡 **Cómo se explica en la clase [B110-C03](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md):**
- Paso 1 · ASET. `58,19 × (10/20)² = 14,55 min`.
- Una cabina de 100 m³ con un orificio de 20 mm da un ASET de `14,55 min`.
- 🎯 **Por qué importa:** Ninguna clase anterior trata evacuación, refugio y vehículos de escape. La decisión central: ¿alcanza el margen entre ASET y RSET, y cuánto de ese margen depende de supuestos que no se conocen?
- 🔗 **Se estudia junto con:** RSET, margen, refugio, cuello de botella.

📘 **Dónde se aprende** (1 clase): [B110-C03 · Evacuación y refugio de emergencia](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md).

### Asidero

- Un asidero es un punto de agarre fijo en la estructura.
- Sujeción: apoyo que reacciona. Asidero: punto de agarre.

💡 **Cómo se explica en la clase [B106-C16](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md):**
- Cruzar 5 m a 0,3 m/s toma 16,7 s; frenar `75·0,3 = 22,5 N·s` en 0,3 s exige 75 N sobre un asidero.
- Los asideros deben soportar esa fuerza y estar al alcance del brazo.
- 🎯 **Por qué importa:** Sin peso ni fricción, toda fuerza tiene una reacción que mueve al operario o a la carga; un diseño de herramientas y de superficies que lo ignore produce maniobras inseguras. La decisión central: ¿qué sujeciones y qué límites de par o de empuje evitan que la reacción mueva al astronauta fuera de la tarea?
- 🔗 **Se estudia junto con:** Impulso, Conservación del momento, Momento de inercia I, Par τ.

📘 **Dónde se aprende** (2 clases): [B106-C16 · Ergonomía en microgravedad](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md); [B108-C02 · Planificación de desplazamientos y rutas de EVA](../programa/clases/B108/B108-C02-planificacion-de-desplazamientos-y-rutas-de-eva/CLASE.md).

### Asignación

- Una asignación liga una línea observada con una transición del catálogo.
- La asignación reparte funciones a subsistemas.
- Estación: antena que atiende una pasada a la vez. Asignación: estación (o ninguna) por pasada.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B55-C10](../programa/clases/B55/B55-C10-identificacion-de-moleculas-organicas/CLASE.md):**
- La primera ventana de ±8 km/s da `v` por mediana de las velocidades por línea; la segunda ventana de ±0,6 MHz asigna 14 de 17 y el ajuste de mínimos cuadrados da `v = 4,944 km/s` (inyectada 5,0; el ruido de 0,15 MHz explica la diferencia).
- *Descripción textual:* una primera ventana en velocidad fija un valor robusto, una segunda ventana en frecuencia asigna líneas y se afina `v`; la densidad del catálogo da la probabilidad de coincidencias casuales.
- 🎯 **Por qué importa:** Casi todas las detecciones de moléculas se basan en coincidencias de frecuencia, y hay catálogos con decenas de miles de líneas: una coincidencia aislada puede ser casualidad. La decisión central: ¿cuántas líneas asignadas, con qué velocidad común y con qué probabilidad de falso positivo se justifica afirmar una especie?
- 🔗 **Se estudia junto con:** tolerancia, densidad de líneas, probabilidad de coincidencia casual, líneas intrusas.

📘 **Dónde se aprende** (4 clases): [B55-C10 · Identificación de moléculas orgánicas](../programa/clases/B55/B55-C10-identificacion-de-moleculas-organicas/CLASE.md); [B83-C06 · Descomposición funcional](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md); [B96-C17 · Coordinación de múltiples estaciones](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md); [B97-C09 · Robótica colaborativa](../programa/clases/B97/B97-C09-robotica-colaborativa/CLASE.md).

### Asignación de redundancia

- La asignación de redundancia escoge qué duplicar bajo un presupuesto.

💡 **Cómo se explica en la clase [B83-C23](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *estudio de redundancia con confiabilidad de misión*: cuatro esquemas, verificación por Monte Carlo, asignación bajo masa y lista de supuestos y de qué es sintético.
- 🎯 **Por qué importa:** Duplicar todo es imposible por masa y a veces contraproducente; no duplicar nada deja una misión frágil. La decisión central: ¿qué unidades duplicar, con qué esquema y cuánta confiabilidad compra cada kilogramo?
- 🔗 **Se estudia junto con:** confiabilidad, Paralelo activo, Redundancia fría, 2-de-3.

📘 **Dónde se aprende** (1 clase): [B83-C23 · Redundancia y tolerancia a fallos de misión](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md).

### Asignación global

- La asignación global minimiza la suma de costos `d²` de todas las pistas a la vez.

💡 **Cómo se explica en la clase [B74-C30](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md):**
- Incluso con asignación global, a `1,5σ` casi la mitad de las escenas falla: no hay algoritmo que arregle observaciones ambiguas.
- *Descripción textual:* las pistas y las observaciones pasan por la compuerta y generan una matriz de costos; se asigna con vecino más cercano o con asignación global y se evalúa la fracción de aciertos.
- ⚠️ **Error frecuente:** Asignar voraz en un orden arbitrario. Es peor que la asignación global; ver 8.2–8.3.
- 🎯 **Por qué importa:** Una asociación incorrecta no se ve en el filtro: el estado sigue convergiendo, pero hacia el objeto equivocado. La decisión central: ¿qué compuerta y qué regla de asignación equilibran el riesgo de perder una observación verdadera y el de aceptar una falsa o la de otro objeto?
- 🔗 **Se estudia junto con:** compuerta, asociación de vecino más cercano, clutter, pista.

📘 **Dónde se aprende** (1 clase): [B74-C30 · Asociación de observaciones y correlación de pistas](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md).

### Asimetría

- La asimetría mide qué tan desbalanceada está la distribución (cero en una simétrica).
- Retardo: tiempo de ida y vuelta menos el procesamiento. Asimetría: ida y vuelta distintas.
- La asimetría y la curtosis en exceso: momentos de la forma de `z`.

💡 **Cómo se explica en la clase [B12-C06](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md):**
- La asimetría de los promedios simulados está en torno de `0,000 ± 0,008`: una uniforme es simétrica y así permanece.
- Para una distribución asimétrica, la asimetría del promedio decrece como `1/√n`: más lenta que la dispersión.
- 🎯 **Por qué importa:** Ningún instrumento tiene ruido exactamente normal, y sin embargo casi todas las incertidumbres se expresan con campanas. La razón es que se reportan promedios y sumas de muchas contribuciones pequeñas.
- 🔗 **Se estudia junto con:** teorema central del límite, Estandarizar, distancia de Kolmogorov–Smirnov, colas pesadas.

📘 **Dónde se aprende** (3 clases): [B12-C06 · Teorema central del límite](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md); [B48-C10 · Redes de instrumentos](../programa/clases/B48/B48-C10-redes-de-instrumentos/CLASE.md); [B51-C07 · Evaluación de residuos y diagnóstico de calidad de calibración](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md).

### Asimetría relativa

- La asimetría relativa es `‖P − Pᵀ‖/‖P‖`.

💡 **Cómo se explica en la clase [B74-C18](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md):**
- Ejercicio 2 · guiado. ¿Qué mide la asimetría relativa de `P`?
- variante menor autovalor de P [m^2] asimetria relativa rms error pos. ultimos 50 pasos [m]
- 🎯 **Por qué importa:** Una covarianza con un autovalor negativo no es una covarianza: el filtro deja de ser fiable sin avisar. La decisión central: ¿qué formulación numérica y qué coste permite el procesador de a bordo sin perder consistencia?
- 🔗 **Se estudia junto con:** forma de Joseph, rango dinámico, coste, precisión simple.

📘 **Dónde se aprende** (1 clase): [B74-C18 · Estimación autónoma a bordo](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md).

### Asincrónico

- El mensaje asincrónico se envía y se responde cuando se pueda.

💡 **Cómo se explica en la clase [B113-C03](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md):**
- Con retardo máximo, el primer mensaje asincrónico tiene respuesta posible tras `46,63 min`.
- Distinguir conversación en tiempo real de mensajes asincrónicos.
- 🎯 **Por qué importa:** Ninguna clase trata el efecto del retardo en el apoyo psicológico. La decisión central: ¿qué formatos de apoyo siguen siendo posibles cuando una respuesta tarda decenas de minutos?
- 🔗 **Se estudia junto con:** retardo de ida, intercambio, conversación en tiempo real, distancia Tierra–Marte.

📘 **Dónde se aprende** (1 clase): [B113-C03 · Comunicación diferida y soporte psicológico a distancia](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md).

### Asíncrono

- Un canal síncrono permite conversar; uno asíncrono, solo mensajes.

💡 **Cómo se explica en la clase [B104-C08](../programa/clases/B104/B104-C08-comunicacion-de-tripulacion/CLASE.md):**
- Distinguir un canal síncrono de uno asíncrono.
- 🎯 **Por qué importa:** A 1,28 s de la Luna aún se conversa; a más de 3 minutos de Marte ya no. La decisión central: ¿qué protocolo de mensajes usar cuando cada ida y vuelta cuesta minutos y un error cuesta caro?
- 🔗 **Se estudia junto con:** retardo de luz, síncrono, repetición de lectura, error residual.

📘 **Dónde se aprende** (1 clase): [B104-C08 · Comunicación de tripulación](../programa/clases/B104/B104-C08-comunicacion-de-tripulacion/CLASE.md).

### Asinh

- El estiramiento asinh `f(t) = asinh(t/b)/asinh(1/b)` se comporta como una recta cerca de 0 y como un logaritmo para valores grandes; fue propuesto en astronomía por Lupton y colaboradores (S2).

💡 **Cómo se explica en la clase [B15-C10](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md):**
- Con `b = 0,02`, la pendiente inicial es `1/(b asinh(1/b)) = 10,86`: los valores cercanos a 0 se multiplican por casi 11, y para `t ≫ b` se parece a un logaritmo (el laboratorio: `f(0,5) = 0,8496`, aproximación logarítmica `0,8495`).
- Sumadas tras normalizar a [0, 1] y estirar, el laboratorio da: lineal `2,000`; raíz `1,414`; asinh `1,839`.
- 🎯 **Por qué importa:** Tienes una imagen con un cielo de 50 ADU, una estructura difusa tenue 15 ADU por encima y una estrella de 9000 ADU. Si la muestras con una escala lineal entre mínimo y máximo, el cielo y la estructura quedan en los niveles de gris 1 y 2 de 255: parece una pantalla negra con un punto.
- 🔗 **Se estudia junto con:** histograma, normalización, estiramiento, intervalo.

📘 **Dónde se aprende** (1 clase): [B15-C10 · Histogramas y normalización](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md).

### Asíntota

- En la hipérbola, `1 + e cos θ` se anula en el ángulo `θ∞ = arccos(−1/e)`: allí `r → ∞` y la dirección se llama asíntota.
- La asíntota es el valor al que tiende la recuperación (100 en este modelo; puede ser menor).

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- Las asíntotas están en `θ∞ = arccos(−1/e) = arccos(−0,83255) = 146,36°`.
- *Descripción textual:* una sola ecuación da cuatro curvas según la excentricidad: circunferencia (0), elipse (entre 0 y 1, con semieje positivo), parábola (1, semieje infinito) e hipérbola (mayor que 1, semieje negativo, con asíntotas a `arccos(−1/e)`); las dos primeras son ligadas y las otras dos no.
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.
- 🔗 **Se estudia junto con:** cónica, propiedad foco–directriz, foco, directriz.

📘 **Dónde se aprende** (2 clases): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B105-C17 · Rehabilitación posterior al vuelo](../programa/clases/B105/B105-C17-rehabilitacion-posterior-al-vuelo/CLASE.md).

### Asíntotas

- Las ramas parten de los polos de `P` (con `K=0`) y terminan en los ceros de `P` o van al infinito siguiendo asíntotas.

💡 **Cómo se explica en la clase [B16-C09](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md):**
- Calcular asíntotas, punto de ruptura y cruce del eje imaginario de un lazo sencillo.
- Ejercicio 2 · con pista. Para `P = 1/(s(s+1)(s+2))` calcula el centroide y los ángulos de asíntota.
- 🎯 **Por qué importa:** Subir la ganancia de un lazo hace que responda más rápido, pero también más oscilante, hasta que se desestabiliza. Para decidir cuánta ganancia usar necesitas ver el compromiso de un vistazo.
- 🔗 **Se estudia junto con:** lugar de las raíces, parten, terminan, punto de ruptura.

📘 **Dónde se aprende** (1 clase): [B16-C09 · Lugar de las raíces](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md).

### Asintótica

- La asintótica `ν_{n,l} = Δν(n + l/2 + ε) − l(l+1)D₀`.

💡 **Contexto en la clase [B37-C09](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md):**
- **Idea central (modelo mental):** Es como los trastes de una guitarra: su separación depende del tamaño del instrumento. Medir la separación de las frecuencias da el tamaño y la masa de la estrella, igual que un luthier mide el diapasón.
- 🎯 **Por qué importa:** Sin Δν y νmax habría que ajustar modelos para saber masa y radio. La decisión central: ¿qué precisión en masa y radio se obtiene con estos observables y qué supuestos exige?
- 🔗 **Se estudia junto con:** separación grande, frecuencia ν_max, relación de escala, espaciado de períodos.

📘 **Dónde se aprende** (1 clase): [B37-C09 · Frecuencias características: Δν, νmax y espaciado de períodos](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md).

### Asintóticamente estable

- Un sistema `y′ = A y` es asintóticamente estable si todos los autovalores tienen parte real negativa, marginalmente estable si alguno tiene parte real cero y ninguno positiva (con autovectores completos), e inestable si alguno tiene parte real positiva.
- Un sistema LTI es asintóticamente estable si, ante cualquier condición inicial y sin entrada, su estado tiende a cero; esto ocurre si y solo si todos los polos (autovalores de `A`) tienen parte real negativa.

💡 **Cómo se explica en la clase [B10-C09](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md):**
- Paso 3 · Estabilidad. Parte real `−0,0628 < 0`: asintóticamente estable.
- 🎯 **Por qué importa:** Un panel solar largo y delgado vibra después de una maniobra. Si la vibración se amortigua, el panel es estable; si crece, hay un problema serio.
- 🔗 **Se estudia junto con:** diagonalizable, semejantes, exponencial matricial, marginalmente estable.

📘 **Dónde se aprende** (2 clases): [B10-C09 · Diagonalización y estabilidad](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md); [B16-C07 · Realimentación y estabilidad](../programa/clases/B16/B16-C07-realimentacion-y-estabilidad/CLASE.md).

### ASM (attached sync marker)

- El ASM (attached sync marker) `1ACFFC1D` (32 bits) precede a cada bloque codificado con RS, concatenado o LDPC de tasa 7/8.

💡 **Cómo se explica en la clase [B89-C11](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md):**
- El laboratorio lista `I = 1, 2, 3, 4, 5, 8`: `I = 5` da `n = 1275` octetos de bloque y `1279` con el ASM.
- *Descripción textual:* los datos forman una trama que se codifica con RS, se precede del ASM y se envía; el receptor correla el ASM con tolerancia `t` para recuperar la sincronía.
- ⚠️ **Error frecuente:** Olvidar el ASM en la longitud de canal. Se corrige con 8.2.
- 🎯 **Por qué importa:** El receptor solo puede decodificar si encuentra el comienzo de cada bloque; la elección del marcador, su tolerancia y la profundidad de entrelazado deciden la latencia, el rendimiento y la pérdida de tramas.
- 🔗 **Se estudia junto con:** bloque de información, bloque de canal, eficiencia de datos, sincronía de trama.

📘 **Dónde se aprende** (1 clase): [B89-C11 · Telemetría CCSDS](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md).

### Asociación

- La asociación relaciona detecciones con la pista (aquí por distancia a la verdad, solo en la simulación).

💡 **Cómo se explica en la clase [B15-C20](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md):**
- Tampoco prueba la asociación de varios objetos, que en la simulación se hace con la verdad.
- Detección en cada imagen + asociación: la elegida.
- 🎯 **Por qué importa:** Detectar y seguir un objeto móvil —un asteroide, un fragmento de basura espacial, un satélite— combina varios problemas: la cámara no apunta exactamente igual en cada imagen, las estrellas fijas saturan la escena, el objeto es débil y la medida es ruidosa.
- 🔗 **Se estudia junto con:** requisito, prueba de extremo a extremo, mediana temporal, imagen de diferencia.

📘 **Dónde se aprende** (1 clase): [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md).

### Asociación de seguridad (SA)

- Una asociación de seguridad (SA) fija algoritmo, clave, tamaño de etiqueta y ventana.

💡 **Cómo se explica en la clase [B89-C25](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md):**
- Los parámetros de la asociación de seguridad incluyen algoritmo, clave, máscara de autenticación y ventana de secuencia.
- SA["asociacion de seguridad: SPI, clave, ventana"] --> TX["emisor: etiqueta = MAC(clave, SPI, ASN, carga)"]
- 🎯 **Por qué importa:** Los comandos son la superficie más sensible de una misión; sin autenticación y sin protección contra repetición, una trama capturada podría reutilizarse, y un CRC solo detecta errores, no ataques (C12). La decisión central: ¿cómo garantizar que una trama es auténtica, íntegra y no repetida, y cuánto cuesta en sobrecarga?
- 🔗 **Se estudia junto con:** protocolo de seguridad de enlace de datos (SDLS), cifrado autenticado AES en modo Galois/Counter (GCM), SPI, ventana anti-repetición.

📘 **Dónde se aprende** (1 clase): [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md).

### Asociación de vecino más cercano

- La asociación de vecino más cercano toma para cada pista la observación más próxima disponible.

💡 **Contexto en la clase [B74-C30](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md):**
- 🎯 **Por qué importa:** Una asociación incorrecta no se ve en el filtro: el estado sigue convergiendo, pero hacia el objeto equivocado. La decisión central: ¿qué compuerta y qué regla de asignación equilibran el riesgo de perder una observación verdadera y el de aceptar una falsa o la de otro objeto?
- 🔗 **Se estudia junto con:** compuerta, asignación global, clutter, pista.

📘 **Dónde se aprende** (1 clase): [B74-C30 · Asociación de observaciones y correlación de pistas](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md).

### Asociatividad

- La precedencia es el orden en que se evalúan los operadores; la asociatividad dice hacia qué lado se agrupan los de igual precedencia.

💡 **Contexto en la clase [B07-C03](../programa/clases/B07/B07-C03-operadores-y-expresiones/CLASE.md):**
- **Idea central (modelo mental):** Una expresión se evalúa como un árbol: las operaciones de mayor precedencia son ramas bajas que se resuelven primero y alimentan a las de arriba. Los paréntesis fuerzan una rama. ```mermaid flowchart BT n2["2"] --> mas["+"] n3["3"] --> por["*"] n4["4"] --> por por --> mas mas --> r["14"] ``` *Descripción textual:* el árbol de `2 + 3 * 4`.
- 🎯 **Por qué importa:** Casi cualquier resultado científico es una expresión: una masa dividida por un volumen, un cociente de períodos. Si no sabes en qué orden Python evalúa `a / b  3`, escribirás una fórmula distinta de la que piensas y no recibirás ningún aviso: el programa funcionará y dará un número equivocado.
- 🔗 **Se estudia junto con:** operador, operando, expresión, evalúa.

📘 **Dónde se aprende** (1 clase): [B07-C03 · Operadores y expresiones](../programa/clases/B07/B07-C03-operadores-y-expresiones/CLASE.md).

### Asterismo

- Un asterismo es una figura reconocible de estrellas que no es una de las 88 (puede cruzar constelaciones o ser parte de una).

💡 **Cómo se explica en la clase [B08-C06](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md):**
- Explicar qué es una constelación en el sentido de la IAU y distinguirla de un asterismo.
- 🎯 **Por qué importa:** Dos personas dicen «la estrella roja de la Cruz del Sur» y creen hablar de lo mismo; un programa de telescopio pide «HIP 12345». Sin un lenguaje común no puedes repetir una observación ni compartirla.
- 🔗 **Se estudia junto con:** constelación, catálogo, identificador, magnitud límite.

📖 **Explicado a fondo:** [Constelación y asterismo](esencial/cuarta-fundamentos.md#constelación-y-asterismo) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B08-C06 · Constelaciones y catálogos estelares](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md).

### Astigmatismo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C14](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md):**
- *Descripción textual:* la dispersión del vidrio fija la separación focal y el campo fuera de eje la del astigmatismo.
- La evidencia es la ficha de aberración cromática y astigmatismo del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** El color y el astigmatismo degradan el campo de refractores y espejos. La decisión central: ¿cuánto se separan los focos por color y por plano?
- 🔗 **Se estudia junto con:** dispersión, número de Abbe, aberración cromática longitudinal, F, d, C.

📘 **Dónde se aprende** (1 clase): [B41-C14 · Aberración cromática y astigmatismo](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md).

### Astrofotografía

- La astrofotografía es el registro fotográfico de objetos celestes.

💡 **Cómo se explica en la clase [B02-C17](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md):**
- Ordenar cronológicamente cinco hitos de la astrofotografía temprana.
- 🎯 **Por qué importa:** Un dibujo depende de quien lo hace; una placa registra lo que llegó. La pregunta motivadora es: ¿qué cambia cuando la observación puede guardarse, compararse años después y medirse?
- 🔗 **Se estudia junto con:** daguerrotipo, placa seca de gelatina, exposición, seguimiento.

📘 **Dónde se aprende** (1 clase): [B02-C17 · Nacimiento de la astrofotografía](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md).

### Astrometría

- La astrometría es la medición de posiciones.

💡 **Cómo se explica en la clase [B58-C06](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md):**
- La evidencia es la ficha de astrometría del ejercicio 12 (sección 20).
- Ejercicio 9 · transferencia. Transferencia. ¿Por qué la astrometría de un campo grande necesita más constantes?
- 🎯 **Por qué importa:** Una órbita no puede ser mejor que sus posiciones: un error de décimas de segundo de arco se amplifica al propagar. La decisión central: ¿con qué exactitud puedo asignar coordenadas a un objeto en una imagen y qué la limita?
- 🔗 **Se estudia junto con:** proyección gnomónica, coordenadas estándar, constantes de placa, arrastre.

📖 **Explicado a fondo:** [Astrometría](esencial/esencial-a-c.md#astrometría) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B58-C06 · Astrometría de objetos menores](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md).

### Astronomía cultural

- La arqueoastronomía estudia las prácticas astronómicas de culturas antiguas, incluidas las orientaciones de sitios y estructuras; la astronomía cultural es el término más amplio, que incluye también tradiciones vivas (S2).

💡 **Cómo se explica en la clase [B02-C08](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md):**
- Definir arqueoastronomía y astronomía cultural como campos interdisciplinarios.
- 🎯 **Por qué importa:** Decir «esta puerta mira al solsticio» es fácil; demostrarlo es difícil. Hay que medir bien, conocer el horizonte, descartar el azar y entender el contexto cultural.
- 🔗 **Se estudia junto con:** arqueoastronomía, orientación, azimut, altura del horizonte.

📘 **Dónde se aprende** (1 clase): [B02-C08 · Arqueoastronomía y sus métodos](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md).

### Atasco

- El atasco repite el último valor.

💡 **Cómo se explica en la clase [B88-C42](../programa/clases/B88/B88-C42-simuladores-y-mocks-de-sensores-para-pruebas/CLASE.md):**
- El detector (5 lecturas idénticas) detecta el atasco en 200 de 200 corridas, con 0 falsas alarmas y latencia media `2,99` muestras.
- Modelar sesgo, ruido, cuantización, atasco y pérdida de dato.
- 🎯 **Por qué importa:** Para probar el FDIR hace falta provocar fallos que el sensor real no da a pedido. La decisión central: ¿qué características del sensor debe reproducir el doble para que la prueba sea válida?
- 🔗 **Se estudia junto con:** doble, pérdida de dato, desviación de Allan.

📘 **Dónde se aprende** (1 clase): [B88-C42 · Simuladores y mocks de sensores para pruebas](../programa/clases/B88/B88-C42-simuladores-y-mocks-de-sensores-para-pruebas/CLASE.md).

### ATE

- Ancla: pose fija que elimina la libertad de colocar el grafo en cualquier lugar. ATE: error absoluto de trayectoria (C06).
- ATE: RMSE de la traslación tras alinear la estimación con la verdad por cuerpo rígido (F2).

💡 **Cómo se explica en la clase [B99-C03](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md):**
- La odometría sola termina a 1,741 m del origen (ATE 0,576 m); tras optimizar, a 0,028 m (ATE 0,172 m), con el `χ²` cayendo de 7 603,3 a 4,2 en dos iteraciones.
- Descripción larga: el cierre de bucle reduce el error de la pose final en un factor 60, pero el ATE solo baja a 0,17 m, porque el error se reparte a lo largo de toda la trayectoria.
- 🎯 **Por qué importa:** Sumar movimientos da una trayectoria que no cierra el lazo; una medida de cierre de bucle dice que la pose final es la inicial. La decisión central: ¿cómo repartir el desacuerdo entre cientos de poses de modo coherente con la incertidumbre de cada medida?
- 🔗 **Se estudia junto con:** Grafo de poses, Medida z_ij, Información Ω_ij, Error de arista e_ij.

📘 **Dónde se aprende** (2 clases): [B99-C03 · SLAM basado en grafos de poses](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md); [B99-C06 · Evaluación de deriva y error de trayectoria](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md).

### Atenuación

- La atenuación de una onda plana en un espesor `t` es `e^(−t/δ)`.
- La atenuación es la caída de la presión con la distancia.
- La atenuación es la pérdida de señal con la distancia y crece con la frecuencia.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B53-C27](../programa/clases/B53/B53-C27-deteccion-remota-de-oceanos-subsuperficiales-induccion-magnetica-libracion-y-radar/CLASE.md):**
- *Descripción textual:* El período de excitación y la conductividad dan la profundidad de piel y la atenuación; la inercia de la capa da la amplificación de la libración; ambas son evidencia independiente.
- Paso 3. Atenuación: `e^(−100/δ) = 0,210`.
- ⚠️ **Error frecuente:** Confundir atenuación con profundidad del océano. se corrige con 8,2
- 🎯 **Por qué importa:** Cada método ve algo distinto y ninguno basta solo. La decisión central: ¿qué señal esperaría un océano de cierta conductividad y espesor y cuánto se distingue de un cuerpo sólido?
- 🔗 **Se estudia junto con:** profundidad de piel, amplificación de libración, período sinódico.

📘 **Dónde se aprende** (4 clases): [B53-C27 · Detección remota de océanos subsuperficiales: inducción magnética, libración y radar](../programa/clases/B53/B53-C27-deteccion-remota-de-oceanos-subsuperficiales-induccion-magnetica-libracion-y-radar/CLASE.md); [B61-C05 · Fusión por impacto y metamorfismo de choque](../programa/clases/B61/B61-C05-fusion-por-impacto-y-metamorfismo-de-choque/CLASE.md); [B85-C28 · Protección pasiva frente al ambiente espacial](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md); [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### Atenuación A_p

- La atenuación `A_p` es la excedida el `p %` del año.

💡 **Cómo se explica en la clase [B91-C07](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md):**
- (Los porcentajes `A₁%`, `A₀,₁%` y `A₀,₀₀₁%` están en las columnas `p = 1 %`, `0,1 %` y `0,001 %`.) La atenuación crece de forma muy rápida con la frecuencia y con la exigencia de disponibilidad.
- Una antena con ruido muy bajo es muy sensible al ruido de la lluvia: `0,5 dB` de atenuación cuestan casi `5 dB` de `C/N₀`.
- ⚠️ **Error frecuente:** Sumar la atenuación específica por todo el trayecto sin factores de reducción. Ver 8.2.
- 🎯 **Por qué importa:** En bandas altas la lluvia puede quitar decenas de dB durante una fracción pequeña del año. La decisión central: ¿qué margen reservar para una disponibilidad dada, y a partir de qué frecuencia deja de ser razonable un enlace sin reserva ni diversidad?
- 🔗 **Se estudia junto con:** atenuación específica, longitud efectiva, temperatura de ruido de cielo, disponibilidad.

📘 **Dónde se aprende** (1 clase): [B91-C07 · Atenuación atmosférica y efectos de la lluvia en enlaces](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md).

### Atenuación atmosférica

- La atenuación atmosférica es la pérdida por gases y lluvia, que crece con la frecuencia.

💡 **Cómo se explica en la clase [B89-C04](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md):**
- Con una atenuación atmosférica sintética de 1,5 dB en Ka, el total a la Luna es `235,75 dB`.
- Añadir una atenuación atmosférica sintética y distinguirla de la de espacio libre.
- 🎯 **Por qué importa:** La pérdida de espacio libre domina cualquier presupuesto de enlace de espacio profundo y fija la potencia, la ganancia y el tiempo de ida y vuelta que tendrá una misión. La decisión central: ¿cuántos decibelios se pierden entre transmisor y receptor y cuánto tarda la señal en llegar?
- 🔗 **Se estudia junto con:** pérdida de espacio libre, retardo de luz, UA, tiempo de ida y vuelta.

📘 **Dónde se aprende** (1 clase): [B89-C04 · Propagación y pérdidas de espacio libre](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md).

### Atenuación específica

- La atenuación específica `γ_R = k R^α` (dB/km) viene de la tasa de lluvia `R` (mm/h) y de coeficientes `k`, `α` que dependen de la frecuencia y la polarización.

💡 **Cómo se explica en la clase [B91-C07](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md):**
- La atenuación específica por lluvia no depende de la antena, pero el ruido que aporta sí pesa más cuanto menor es el `T_op`.
- *Descripción textual:* la tasa de lluvia y la frecuencia dan la atenuación específica; la geometría del trayecto da la longitud lluviosa y los factores de reducción dan la longitud efectiva; el producto es la atenuación del `0,01 %`, que se escala a otros porcentajes y se convierte en ruido de cielo.
- ⚠️ **Error frecuente:** Sumar la atenuación específica por todo el trayecto sin factores de reducción. Ver 8.2.
- 🎯 **Por qué importa:** En bandas altas la lluvia puede quitar decenas de dB durante una fracción pequeña del año. La decisión central: ¿qué margen reservar para una disponibilidad dada, y a partir de qué frecuencia deja de ser razonable un enlace sin reserva ni diversidad?
- 🔗 **Se estudia junto con:** longitud efectiva, atenuación A_p, temperatura de ruido de cielo, disponibilidad.

📘 **Dónde se aprende** (1 clase): [B91-C07 · Atenuación atmosférica y efectos de la lluvia en enlaces](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md).

### Aterrizador reutilizable

- Un aterrizador reutilizable baja y sube entre dos nodos con propelente del depósito.

💡 **Cómo se explica en la clase [B100-C06](../programa/clases/B100/B100-C06-logistica-cislunar-nodos-depositos-y-rutas-de-reabastecimiento/CLASE.md):**
- *Descripción textual:* tres nodos con tramos de Δv ilustrativo: de órbita baja a NRHO, de NRHO a la superficie y de vuelta; la ruta directa A usa etapas desechables, la B un aterrizador reutilizable abastecido desde el depósito.
- Con un aterrizador reutilizable de 500 kg secos desde un depósito en NRHO hacen falta `2043,6 kg` de propelente por viaje; si la carga y el propelente suben desde órbita baja con etapas químicas, la razón empeora a `7,779`; con un remolcador eléctrico ilustrativo baja a `4,729` con 10 viajes y supera a la ruta directa desde el viaje 2.
- 🎯 **Por qué importa:** Un depósito en órbita lunar parece una ventaja obvia, pero solo lo es si el propelente llega al depósito de una forma más barata que llevarlo directamente. La decisión central: ¿con qué transporte y con cuántos viajes del aterrizador reutilizable un depósito reduce la masa que hay que lanzar desde órbita baja?
- 🔗 **Se estudia junto con:** nodo, tramo, depósito, remolcador eléctrico.

📘 **Dónde se aprende** (1 clase): [B100-C06 · Logística cislunar: nodos, depósitos y rutas de reabastecimiento](../programa/clases/B100/B100-C06-logistica-cislunar-nodos-depositos-y-rutas-de-reabastecimiento/CLASE.md).

### Aterrizaje balístico

- Un aterrizaje balístico es uno sin sustentación, con mayor dispersión.

💡 **Cómo se explica en la clase [B104-C14](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md):**
- En un resultado de búsqueda, no consultado en la página original, aparecen un aterrizaje balístico de Soyuz corto del objetivo (Expedición 6) y la posterior incorporación de un sistema de localización; esos detalles no se citan como hechos de la clase.
- Aun así, un aterrizaje balístico alarga la mediana en más de una hora.
- 🎯 **Por qué importa:** Si el rescate no llega antes de que se agoten el refugio y las provisiones, la situación se vuelve crítica. La decisión central: ¿cuánto reducen la baliza y la ubicación del rescate la probabilidad de una espera mayor que la autonomía?
- 🔗 **Se estudia junto con:** dispersión de aterrizaje, baliza, autonomía, tiempo de rescate.

📘 **Dónde se aprende** (1 clase): [B104-C14 · Supervivencia en entorno terrestre](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md).

### Atípico

- Un atípico (*outlier*) es un valor muy distinto del resto; puede ser un error o un fenómeno real.
- Atípico: dato que no sigue el modelo.

💡 **Cómo se explica en la clase [B14-C08](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md):**
- La media y la desviación típica se dejan arrastrar por los propios atípicos.
- Se marca como atípico `|x − mediana| > 5 × 1,4826 × MAD`.
- ⚠️ **Error frecuente:** Borrar atípicos que podrían ser reales. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Una bitácora de observación real tiene errores: alguien escribió `-99` donde faltaba un dato, el mismo objeto aparece con tres grafías, una fila se copió dos veces, un valor tiene un dígito de más. Si calculas una media sin limpiar, el resultado es otro número.
- 🔗 **Se estudia junto con:** magnitud, centinela, valor ausente, duplicado exacto.

📘 **Dónde se aprende** (2 clases): [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md); [B99-C07 · Robustez del mapeo ante entornos degradados](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md).

### Atlas

- Un atlas de brillo artificial es un mapa calculado con modelos de propagación a partir de datos de satélite y de mediciones en tierra (S2).

💡 **Cómo se explica en la clase [B08-C12](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md):**
- Falchi y colaboradores (S2) calcularon un atlas mundial del brillo artificial del cielo con datos de satélite de alta resolución y nuevas mediciones.
- Son resultados de un modelo y no mediciones directas en cada sitio: el atlas es una guía, no una medida de tu patio.
- ⚠️ **Error frecuente:** Extrapolar el atlas a tu patio. Ejercicio 8.
- 🎯 **Por qué importa:** La mayoría de las personas ya no ve la Vía Láctea desde su casa. La pregunta motivadora: ¿qué tan oscuro es mi cielo, cuánto de eso es culpa de la Luna y cuánto de las luces, y qué puedo hacer?
- 🔗 **Se estudia junto con:** contaminación lumínica, brillo del cielo, magnitud límite, noche astronómica.

📘 **Dónde se aprende** (1 clase): [B08-C12 · Limitación por contaminación lumínica](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md).

### Atmósfera exponencial

- La atmósfera exponencial es `ρ(h) = ρ₀ e^(−h/H)`.

💡 **Cómo se explica en la clase [B77-C02](../programa/clases/B77/B77-C02-movimiento-en-atmosfera/CLASE.md):**
- Con la atmósfera exponencial el apogeo baja a `3444,3 m` (un `24,9 %` menos) y se alcanza a los `25,43 s`.
- La atmósfera exponencial es una aproximación local; las tablas estándar (U.S.
- 🎯 **Por qué importa:** El aire frena un cuerpo de forma distinta a cada altitud porque la densidad cambia. La decisión central: ¿qué modelo de atmósfera y de integración basta para predecir el movimiento, y cómo se comprueba?
- 🔗 **Se estudia junto con:** arrastre, coeficiente balístico, altura de escala, velocidad terminal.

📘 **Dónde se aprende** (1 clase): [B77-C02 · Movimiento en atmósfera](../programa/clases/B77/B77-C02-movimiento-en-atmosfera/CLASE.md).

### Atmósfera gris

- Una atmósfera gris tiene una opacidad independiente de la longitud de onda.
- La atmósfera gris tiene opacidad constante.
- Una atmósfera gris tiene la misma opacidad infrarroja a todas las longitudes de onda.

💡 **Cómo se explica en la clase [B24-C09](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md):**
- En una atmósfera gris plano–paralela en equilibrio radiativo, en la aproximación de Eddington, `T⁴ = (3/4) T_ef⁴ (τ + 2/3)`.
- Límite: la opacidad real depende de la longitud de onda; una atmósfera gris la simplifica.
- 🎯 **Por qué importa:** Toda temperatura o composición que atribuimos a una estrella se infiere de una capa delgada. Saber de qué profundidad viene la luz, cuánto vale la opacidad y cuánto puede brillar una estrella sin expulsar su atmósfera es lo que permite interpretar espectros (C10) y entender los vientos (C17).
- 🔗 **Se estudia junto con:** opacidad, profundidad óptica, fotosfera, oscurecimiento al limbo.

📘 **Dónde se aprende** (4 clases): [B24-C09 · Atmósferas y opacidades](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md); [B32-C01 · Ecuación de transferencia radiativa en atmósferas estelares](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md); [B32-C05 · Relación T-τ y estructura térmica de la fotosfera](../programa/clases/B32/B32-C05-relacion-t-y-estructura-termica-de-la-fotosfera/CLASE.md); [B54-C09 · Efecto invernadero](../programa/clases/B54/B54-C09-efecto-invernadero/CLASE.md).

### Atmósfera gris de Eddington

- La atmósfera gris de Eddington `T⁴ = (3/4) T_ef⁴ (τ + 2/3)`.

💡 **Contexto en la clase [B37-C04](../programa/clases/B37/B37-C04-condiciones-de-frontera-centrales-y-superficiales-en-modelos-estelares/CLASE.md):**
- **Idea central (modelo mental):** Es como una cuerda fijada en dos extremos: la forma depende de lo que fijes en el techo (el centro) y en el piso (la superficie); si te equivocas en un extremo, toda la curva se desplaza.
- 🎯 **Por qué importa:** Sin condiciones de frontera no hay solución única. La decisión central: ¿qué valores fijan el centro y la superficie, y cuánto cuestan los errores de una frontera?
- 🔗 **Se estudia junto con:** ecuación de Lane–Emden, serie central, profundidad óptica, fotosfera.

📘 **Dónde se aprende** (1 clase): [B37-C04 · Condiciones de frontera centrales y superficiales en modelos estelares](../programa/clases/B37/B37-C04-condiciones-de-frontera-centrales-y-superficiales-en-modelos-estelares/CLASE.md).

### Atómico

- Un requisito atómico tiene una sola obligación.

💡 **Cómo se explica en la clase [B83-C04](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md):**
- Seis cumplen todas las reglas; los otros 14 defectos se reparten así: R1 (sin «deberá») 1, R2 (ambigüedad) 5, R3 (no atómico) 1, R4 (sin valor medible) 5 y R5 (sin método de verificación) 2.
- Ejercicio 4 · autónomo. Divide «El sistema deberá comandarse y deberá almacenar 8 Gbit» en dos requisitos atómicos.
- 🎯 **Por qué importa:** Un requisito vago («resolución adecuada») no puede aprobarse ni suspenderse: bloquea el diseño y siembra disputas. La decisión central: ¿este enunciado se puede comprobar con un método y un criterio de aceptación?
- 🔗 **Se estudia junto con:** requisito, Verificable, modal, palabra ambigua.

📘 **Dónde se aprende** (1 clase): [B83-C04 · Requisitos verificables](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md).

### Átomo

- El átomo es la unidad más pequeña de un elemento que conserva sus propiedades químicas.

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Un átomo de hidrógeno ordinario tiene un protón y un electrón; el helio, dos protones (`Z = 2`); el carbono, seis.
- N2 -.->|"absorbe 3,40 eV o más"| L["n = infinito: 0 eV (átomo ionizado)"]
- ⚠️ **Error frecuente:** Usar la fórmula de Bohr para cualquier átomo. Se corrige con los ejercicios 10 y 11.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.
- 🔗 **Se estudia junto con:** núcleo, protones, neutrones, electrones.

📘 **Dónde se aprende** (1 clase): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md).

### Atrapamiento

- El atrapamiento de un ácido débil es la acumulación de su forma disociada donde el pH es mayor.

💡 **Cómo se explica en la clase [B64-C05](../programa/clases/B64/B64-C05-acidofilos-y-alcalofilos/CLASE.md):**
- Por simulación: la razón de atrapamiento sale de la permeación.
- Calcular la razón de atrapamiento de un ácido débil.
- 🎯 **Por qué importa:** Un acidófilo vive en un medio miles de veces más ácido que su citoplasma. La pregunta motivadora: ¿cómo mantiene una célula un interior casi neutro y qué le cuesta?
- 🔗 **Se estudia junto con:** fuerza protonmotriz, acidófilo, alcalófilo.

📘 **Dónde se aprende** (1 clase): [B64-C05 · Acidófilos y alcalófilos](../programa/clases/B64/B64-C05-acidofilos-y-alcalofilos/CLASE.md).

### Atraso

- El atraso (o *backlog*) es lo que se necesitó y no se pudo pagar.

💡 **Cómo se explica en la clase [B124-C06](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md):**
- Con tope `14` uc/año, cada año el gasto es `min(tope, atraso + demanda)`.
- El atraso máximo es `12,750` uc y el proyecto termina en el año `9`, es decir `1` año(s) tarde.
- 🎯 **Por qué importa:** Un proyecto puede estar bien estimado y aun así fallar porque el dinero no llega al ritmo que necesita. La decisión central: ¿qué tope anual evita el atraso y cuánto cuesta cada año de espera?
- 🔗 **Se estudia junto con:** demanda acumulada, tope, costo de espera, comprometido.

📘 **Dónde se aprende** (1 clase): [B124-C06 · Financiamiento público](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md).

### Atribución

- Atribución es asignar un hecho a un autor.
- La atribución nombra a la comunidad y a la fuente.

💡 **Cómo se explica en la clase [B119-C30](../programa/clases/B119/B119-C30-atribucion-de-incidentes-y-desinformacion-en-el-dominio-espacial/CLASE.md):**
- Una sola fuente dudosa puede mover la conclusión; la confianza debe declararse con su fundamento, y la atribución jurídica o política exige más que un número.
- No se consultó ningún método oficial de atribución ni caso real. El ejemplo conductor: tres hipótesis sintéticas (falla técnica, actor A, actor B) con a priori 0,50; 0,25; 0,25, y cuatro evidencias con verosimilitudes inventadas.
- 🎯 **Por qué importa:** B01-C19 trata la desinformación en general; la atribución técnica y política de incidentes espaciales no está cubierta. El art.
- 🔗 **Se estudia junto con:** posterior, razón de verosimilitud, fiabilidad, desinformación.

📘 **Dónde se aprende** (2 clases): [B119-C30 · Atribución de incidentes y desinformación en el dominio espacial](../programa/clases/B119/B119-C30-atribucion-de-incidentes-y-desinformacion-en-el-dominio-espacial/CLASE.md); [B133-C04 · Riesgos de apropiación cultural en la divulgación](../programa/clases/B133/B133-C04-riesgos-de-apropiacion-cultural-en-la-divulgacion/CLASE.md).

### Atributo

- Un atributo es un metadato pequeño con nombre.
- Un atributo es un dato no espacial (el nombre de la escena).

💡 **Cómo se explica en la clase [B14-C07](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md):**
- Los atributos se asignan con `dset.attrs["unidad"] = ...`.
- Un archivo sin atributos obliga a quien lo recibe a adivinar.
- ⚠️ **Error frecuente:** Olvidar los atributos. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Una simulación o un instrumento moderno produce series de millones de muestras con sus metadatos. Guardarlas en texto es lento y pesado; cargarlas enteras en memoria para leer un fragmento es inviable.
- 🔗 **Se estudia junto con:** grupo, dataset, fragmento, compresión sin pérdida.

📘 **Dónde se aprende** (2 clases): [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md); [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md).

### Atrofia

- La atrofia es la pérdida de masa o de sección de un músculo.

💡 **Cómo se explica en la clase [B105-C03](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md):**
- La evidencia es la ficha de atrofia con balance proteico del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de atrofia con balance proteico*: modelo, `δ` con su origen, área y fuerza a 30, 90 y 180 días, comparación con contramedida simulada, dispersión y lista de qué es sintético.
- 🎯 **Por qué importa:** Sin carga y sin aporte adecuado, el músculo se pierde más rápido que en la Tierra. La decisión central: ¿cuánta área y cuánta fuerza quedan tras 30, 90 y 180 días, y cuánto cambia una contramedida?
- 🔗 **Se estudia junto con:** balance proteico, tensión específica, fuerza máxima, contramedida.

📘 **Dónde se aprende** (1 clase): [B105-C03 · Atrofia muscular](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md).

### AUC

- El AUC es el área bajo ella.
- El AUC es `F D/CL`.
- El AUC es la probabilidad de que un afectado supere a un sano.

💡 **Cómo se explica en la clase [B33-C14](../programa/clases/B33/B33-C14-verificacion-de-alertas-con-tablas-de-contingencia/CLASE.md):**
- El AUC resume la discriminación sin depender del umbral.
- Paso 4 · AUC. `U/(n_pos n_neg) = 0,8047`.
- ⚠️ **Error frecuente:** Tomar el AUC por real. Se corrige con la sección 10.
- 🎯 **Por qué importa:** La verificación decide si una alerta merece confianza. La decisión central: ¿cómo resumir la capacidad de discriminar de un pronóstico?
- 🔗 **Se estudia junto con:** curva ROC, estadístico de Mann–Whitney, sesgo de frecuencia.

📘 **Dónde se aprende** (3 clases): [B33-C14 · Verificación de alertas con tablas de contingencia](../programa/clases/B33/B33-C14-verificacion-de-alertas-con-tablas-de-contingencia/CLASE.md); [B105-C13 · Farmacología y microgravedad](../programa/clases/B105/B105-C13-farmacologia-y-microgravedad/CLASE.md); [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md).

### AUC diario

- El AUC diario es el área bajo `C` en 24 h.

💡 **Cómo se explica en la clase [B105-C22](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md):**
- Calibrar la escala `a` para que el promedio diario sea 1.
- 🎯 **Por qué importa:** Una medición de cortisol sin hora del día no se interpreta: el ritmo diario domina. Y un estresor crónico cambia el nivel medio de una forma distinta que uno agudo.
- 🔗 **Se estudia junto con:** cortisol relativo, entrada, ganancia de retroalimentación, semivida.

📘 **Dónde se aprende** (1 clase): [B105-C22 · Sistema neuroendocrino y respuesta al estrés en vuelo](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md).

### Audiencia

- Una audiencia es el grupo al que se dirige un mensaje.

💡 **Cómo se explica en la clase [B122-C08](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md):**
- K --> M["matriz: audiencia, canal, aprobador"]
- *Descripción textual:* desde el conocimiento corren los plazos de alerta, notificación e informe final, y en paralelo se preparan los mensajes por audiencia.
- 🎯 **Por qué importa:** B124-C18 trata divulgación; la comunicación de crisis con mensajes oportunos no está cubierta. La decisión central: ¿qué hay que comunicar, a quién y antes de qué plazo?
- 🔗 **Se estudia junto con:** alerta temprana, notificación, informe final, canal.

📘 **Dónde se aprende** (1 clase): [B122-C08 · Comunicación de crisis con operadores, autoridades y público](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md).

### Audiodescripción

- La audiodescripción narra lo visual.

💡 **Cómo se explica en la clase [B128-C05](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md):**
- W3C WAI distingue: los *captions* son el texto del habla y de los sonidos no hablados necesarios, sincronizados y normalmente activables; los *subtítulos* suelen ser traducciones a otro idioma; las transcripciones tienen el mismo texto que los captions; la audiodescripción describe lo visual.
- Distinguir subtítulos, captions, transcripción y audiodescripción.
- 🎯 **Por qué importa:** Un subtítulo mal sincronizado o demasiado rápido no se alcanza a leer, y una transcripción automática sin revisar puede decir lo contrario de lo dicho. La decisión central: ¿cómo compruebo que los subtítulos se pueden leer y que no cambian el sentido?
- 🔗 **Se estudia junto con:** subtítulos, transcripción, WebVTT, WER.

📘 **Dónde se aprende** (1 clase): [B128-C05 · Subtítulos y transcripciones](../programa/clases/B128/B128-C05-subtitulos-y-transcripciones/CLASE.md).

### Auditoría

- Una auditoría es una revisión sistemática contra criterios.
- La auditoría es aquí una revisión por reglas de texto.

💡 **Cómo se explica en la clase [B128-C11](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md):**
- Declarar lo que la auditoría no pudo evaluar y que falta la prueba con personas.
- La evidencia es el informe de auditoría priorizado del ejercicio 12 (sección 20).
- ⚠️ **Error frecuente:** Presentar la auditoría como certificación. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Un puntaje alto puede esconder una barrera grave: un video sin subtítulos con todo lo demás perfecto sigue siendo inaccesible para quien no oye. La decisión central: ¿cómo reporto el estado de un recurso sin que el promedio oculte un bloqueo y sin dar por cumplido lo que no se evaluó?
- 🔗 **Se estudia junto con:** criterio, peso, crítico, No evaluado.

📘 **Dónde se aprende** (2 clases): [B128-C11 · Auditoría de accesibilidad de un recurso educativo](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md); [B133-C04 · Riesgos de apropiación cultural en la divulgación](../programa/clases/B133/B133-C04-riesgos-de-apropiacion-cultural-en-la-divulgacion/CLASE.md).

### Auditoría de accesos

- Una auditoría de accesos compara lo asignado con lo permitido.

💡 **Cómo se explica en la clase [B122-C05](../programa/clases/B122/B122-C05-control-de-accesos-y-gestion-de-identidades-en-operaciones/CLASE.md):**
- La evidencia es la informe de auditoría de accesos sintético del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *informe de auditoría de accesos sintético*: matriz, hallazgos (excesos y conflictos), correcciones propuestas, efecto en la superficie y lo consultado o sintético, con el aviso de que no es asesoría.
- 🎯 **Por qué importa:** B96-C07 trata solo la autorización de telecomandos. La decisión central: ¿qué permisos sobran, cuáles se contradicen y quién puede aprobar a quién?
- 🔗 **Se estudia junto con:** privilegio mínimo, segregación de funciones, regla de dos personas, identidad.

📘 **Dónde se aprende** (1 clase): [B122-C05 · Control de accesos y gestión de identidades en operaciones](../programa/clases/B122/B122-C05-control-de-accesos-y-gestion-de-identidades-en-operaciones/CLASE.md).

### Aumento

- En «M×D» (por ejemplo 7×35), `M` es el aumento y `D` el diámetro del objetivo en milímetros (S2).
- El ocular (distancia focal `f_o`) amplía la imagen; el aumento es `M = F/f_o`.
- El aumento `m` del secundario multiplica la distancia focal.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- NASA recomienda, para empezar, entre 7×35 y 10×50: con más aumento el campo es más estrecho, pesan más y se sacuden, salvo con estabilización o trípode (S2, S3).
- Apoya los codos, o el cuerpo en un muro; a mayor aumento, el temblor se nota más, y NASA sugiere trípode para 10× o 15× en la Luna (S4).
- ⚠️ **Error frecuente:** Pensar que más aumento es mejor. Ejercicio 6.
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?
- 🔗 **Se estudia junto con:** objetivo, pupila de salida, campo de visión, campo aparente.

📘 **Dónde se aprende** (3 clases): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md); [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md); [B43-C02 · Selección de geometría instrumental](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md).

### Aumento angular

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C07](../programa/clases/B41/B41-C07-aumentos-y-sistemas-afocales/CLASE.md):**
- *Descripción textual:* dos lentes separadas por la suma de focales dan aumento angular y comprimen el haz.
- ⚠️ **Error frecuente:** Confundir aumento con tamaño de imagen. El aumento es angular.
- 🎯 **Por qué importa:** El aumento decide qué se ve. La decisión central: ¿qué ocular da el aumento y la pupila de salida adecuados?
- 🔗 **Se estudia junto con:** sistema afocal, pupila de salida, telescopio de Kepler, Galileo.

📘 **Dónde se aprende** (1 clase): [B41-C07 · Aumentos y sistemas afocales](../programa/clases/B41/B41-C07-aumentos-y-sistemas-afocales/CLASE.md).

### Aumento de datos

- Un aumento de datos crea ejemplos nuevos transformando los existentes.

💡 **Cómo se explica en la clase [B17-C11](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md):**
- El trabajo que introdujo la U-Net presenta una red y una estrategia de entrenamiento para segmentar imágenes biomédicas aprovechando muy pocas imágenes anotadas gracias a un uso intensivo de aumentos de datos.
- Planificar aumentos de datos que transformen imagen y máscara a la vez.
- 🎯 **Por qué importa:** Delimitar una mancha solar, una nube o un cráter a mano en miles de imágenes no escala. Un umbral por píxel falla cuando el ruido es comparable al contraste.
- 🔗 **Se estudia junto con:** segmentación semántica, máscara, convolución, válido.

📘 **Dónde se aprende** (1 clase): [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md).

### Aumento del secundario

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C17](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md):**
- **Idea central (modelo mental):** Como un periscopio que pliega la luz en dos: el secundario convexo la devuelve al primario y la focal efectiva es `m` veces la del primario en un tubo corto.
- 🎯 **Por qué importa:** Dos espejos permiten un tubo corto y focal larga, y distintos diseños eligen qué aberración corregir. La decisión central: ¿qué diseño corrige la coma y a qué costo?
- 🔗 **Se estudia junto con:** Cassegrain clásico, Dall-Kirkham, Ritchey-Chrétien, focal efectiva.

📘 **Dónde se aprende** (1 clase): [B41-C17 · Telescopios Cassegrain y derivados](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md).

### Aumento lateral

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C06](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md):**
- Calcular el aumento lateral `m = −s'/s`.
- 🎯 **Por qué importa:** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?
- 🔗 **Se estudia junto con:** distancia objeto, distancia imagen, imagen real, virtual.

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Aumento mínimo

- El aumento mínimo y el máximo.

💡 **Cómo se explica en la clase [B41-C20](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md):**
- Aumento mínimo (pupila de 7 mm) `35,7`; máximo orientativo `500`.
- aumento minimo (pupila 7 mm) = 35.7 ; maximo orientativo 2 D[mm] = 500
- 🎯 **Por qué importa:** Un diseño es un conjunto de compromisos. La decisión central: ¿qué apertura y qué focal cumplen el objetivo y qué defecto domina?
- 🔗 **Se estudia junto con:** presupuesto de diseño, corrector de coma, Strehl de Maréchal, suma en cuadratura (RSS).

📘 **Dónde se aprende** (1 clase): [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md).

### Aumento útil

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C07](../programa/clases/B41/B41-C07-aumentos-y-sistemas-afocales/CLASE.md):**
- Fijar el aumento mínimo y el máximo útil.
- 🎯 **Por qué importa:** El aumento decide qué se ve. La decisión central: ¿qué ocular da el aumento y la pupila de salida adecuados?
- 🔗 **Se estudia junto con:** sistema afocal, aumento angular, pupila de salida, telescopio de Kepler.

📘 **Dónde se aprende** (1 clase): [B41-C07 · Aumentos y sistemas afocales](../programa/clases/B41/B41-C07-aumentos-y-sistemas-afocales/CLASE.md).

### Ausencia de memoria

- La ausencia de memoria es la propiedad `P(T > s+t | T > s) = P(T > t)`.

💡 **Cómo se explica en la clase [B12-C03](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md):**
- El script [distribuciones_basicas.py](distribuciones_basicas.py) suma la pmf de Poisson, comprueba que su media y varianza valen `λ`, compara binomial y Poisson, verifica la ausencia de memoria y las fracciones `erf`, y contrasta con simulaciones; falla si una igualdad no se cumple.
- 🎯 **Por qué importa:** Cada vez que un detector cuenta fotones, una nave registra impactos o un instrumento mide con ruido, el patrón de la incertidumbre se parece a uno de unos pocos moldes. Reconocer el molde permite calcular probabilidades sin construir todo desde cero y entender qué supuesto físico lo respalda.
- 🔗 **Se estudia junto con:** distribución, parámetro, distribución binomial, distribución de Poisson.

📘 **Dónde se aprende** (1 clase): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md).

### Autobloqueo

- El autobloqueo ocurre si `λ < φ`.

💡 **Cómo se explica en la clase [B43-C14](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md):**
- *Descripción textual:* el ángulo de avance y la fricción fijan el rendimiento y el autobloqueo; la relación y la rigidez fijan la resolución y la resonancia.
- El ángulo de avance es `2,734°` frente a `φ = 5,711°` (`μ = 0,1`): hay autobloqueo y el rendimiento es `0,3216`.
- 🎯 **Por qué importa:** El reductor fija la resolución, la fuerza disponible y el comportamiento dinámico. La decisión central: ¿qué relación, qué rendimiento y qué rigidez permiten apuntar con la resolución pedida sin resonancias?
- 🔗 **Se estudia junto con:** ángulo de avance, ángulo de fricción, rendimiento, holgura.

📘 **Dónde se aprende** (1 clase): [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md).

### Autocalentamiento

- El autocalentamiento `ΔT = P/δ` con `δ` la constante de disipación.

💡 **Cómo se explica en la clase [B85-C25](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md):**
- Cuantización `0,0111 K`, autocalentamiento `0,1812 K`, tolerancia de `β` (1 %) `0,0186 K` y referencia (`0,1 %`) `0,150 K`: RSS `0,2362 K`.
- Domina el autocalentamiento; se reduce bajando la tensión de excitación o usando un pulso de medida.
- ⚠️ **Error frecuente:** Medir con corriente alta. el autocalentamiento domina (8.2)
- 🎯 **Por qué importa:** Una temperatura mal medida lleva a una decisión errónea de control o de margen. La decisión central: ¿qué error total tiene la cadena de medida a una temperatura dada y qué término lo domina?
- 🔗 **Se estudia junto con:** ecuación β, divisor, cuantización, Callendar–Van Dusen.

📘 **Dónde se aprende** (1 clase): [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md).

### Autocalibración

- La autocalibración (*self-cal*).

💡 **Cómo se explica en la clase [B51-C06](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md):**
- La evidencia es la ficha de la autocalibración del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de la autocalibración*: ciclo, tabla de convergencia, controles y límites.
- 🎯 **Por qué importa:** Sin autocalibración, los errores de ganancia de la atmósfera limitan el rango dinámico. La decisión central: ¿converge el ciclo modelo–ganancias, a qué valor y con qué sesgo?
- 🔗 **Se estudia junto con:** modelo de cielo, imagen sucia, haz sucio, CLEAN.

📘 **Dónde se aprende** (1 clase): [B51-C06 · Autocalibración iterativa con modelo de cielo](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md).

### Autocolisión

- Holgura: distancia entre cápsulas menos la suma de radios. Autocolisión: holgura negativa entre eslabones no adyacentes.

💡 **Cómo se explica en la clase [B101-C04](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md):**
- Evaluar la holgura de autocolisión entre cápsulas.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de espacio de trabajo*: alcance, celdas por límite, tasa y peor caso de autocolisión, evitación de topes y qué es consultado, no consultado y sintético.
- 🎯 **Por qué importa:** Una solución de cinemática inversa que exceda un tope o atraviese el propio brazo no sirve. La decisión central: ¿esta configuración es admisible: respeta los topes y deja holgura entre eslabones?
- 🔗 **Se estudia junto con:** Espacio de trabajo, Tope articular, Cápsula, Holgura.

📘 **Dónde se aprende** (1 clase): [B101-C04 · Límites articulares, espacio de trabajo y evitación de colisiones](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md).

### Autoconvergencia

- La autoconvergencia estima el orden con tres resoluciones: `p ≈ log₂(|y_h − y_{h/2}|/|y_{h/2} − y_{h/4}|)`.

💡 **Cómo se explica en la clase [B11-C19](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md):**
- Con autoconvergencia se verifica el orden y se confirma que el código está en régimen asintótico.
- Medir el orden por autoconvergencia sin solución exacta.
- ⚠️ **Error frecuente:** Confundir autoconvergencia con exactitud. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un resultado numérico sin cota de error es una cifra sin sentido. Y gastar horas de cálculo para reducir un error de método que ya es menor que la incertidumbre de los datos es un desperdicio.
- 🔗 **Se estudia junto con:** error de truncamiento, error de redondeo, error de modelo, error de datos.

📘 **Dónde se aprende** (1 clase): [B11-C19 · Estimación de error y convergencia](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md).

### Autocorrelación

- La autocorrelación `r_k` mide cuánto se parece la serie a sí misma desplazada `k` muestras; el número `k` es el retardo (en inglés *lag*).
- La autocorrelación es la semejanza entre observaciones cercanas en el tiempo.
- La autocorrelación mide la repetición.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C01](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md):**
- Con la media `x̄`, la autocorrelación muestral al retardo `k` es
- C --> E["Memoria:<br/>autocorrelación r_k"]
- 🎯 **Por qué importa:** Un telescopio espacial mide el brillo de una estrella cada dos minutos durante semanas. Lo que llega a tierra no es una curva continua, sino una tabla de números.
- 🔗 **Se estudia junto con:** serie temporal discreta, cadencia, frecuencia de muestreo, media.

📘 **Dónde se aprende** (6 clases): [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B17-C09 · Prevención de fuga de datos](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md); [B30-C03 · Ciclo de actividad solar](../programa/clases/B30/B30-C03-ciclo-de-actividad-solar/CLASE.md); [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md); [B48-C06 · Meteorología de observatorios](../programa/clases/B48/B48-C06-meteorologia-de-observatorios/CLASE.md); [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md).

### Autoestado de masa

- El autoestado de masa tiene masa definida.

💡 **Cómo se explica en la clase [B28-C03](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md):**
- Cada autoestado de masa avanza con una fase distinta.
- 🎯 **Por qué importa:** Un detector que ve neutrinos muónicos de una fuente lejana no ve lo que salió de ella. Para interpretar la razón de sabores hay que conocer la mezcla.
- 🔗 **Se estudia junto con:** sabor, matriz de mezcla, fase de oscilación, probabilidad promediada.

📘 **Dónde se aprende** (1 clase): [B28-C03 · Neutrinos astrofísicos](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md).

### Autónoma

- Es autónoma si `t` no aparece explícitamente.

💡 **Cómo se explica en la clase [B11-C01](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md):**
- Es de segundo orden, no lineal (porque `|r|` depende de las componentes) y autónoma.
- Segundo orden, lineal, homogénea, autónoma.
- 🎯 **Por qué importa:** Casi ninguna ley de la mecánica espacial nos dice *dónde está* un satélite; nos dice *cómo cambia* su movimiento: la aceleración depende de la posición. Eso es una ecuación diferencial.
- 🔗 **Se estudia junto con:** ecuación diferencial, ordinaria, orden, lineal.

📘 **Dónde se aprende** (1 clase): [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md).

### Autonomía

- La autonomía es la capacidad de ejecutar un evento sin comando en tiempo real.
- La autonomía es el tiempo que alcanzan las provisiones y el refugio.
- La autonomía es la capacidad de decidir cómo y cuándo hacer el trabajo.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B48-C07](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md):**
- En cerca de dos de cada tres años habrá un corte que supere la autonomía de 3,6 h: el respaldo solo compra tiempo para un apagado ordenado, no para seguir observando.
- *Descripción textual:* la energía útil entre la carga da la autonomía; la exponencial da la probabilidad de superarla y Poisson da cuántos cortes largos ocurren por año.
- 🎯 **Por qué importa:** Un respaldo mal dimensionado deja la cúpula abierta con lluvia. La decisión central: ¿qué autonomía cubre la mayoría de los cortes?
- 🔗 **Se estudia junto con:** Profundidad de descarga, Distribución exponencial, Proceso de Poisson, Carga crítica.

📘 **Dónde se aprende** (5 clases): [B48-C07 · Seguridad en instalaciones remotas](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md); [B75-C19 · Restricciones de navegación autónoma](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md); [B104-C14 · Supervivencia en entorno terrestre](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md); [B113-C04 · Autonomía personal y gestión del tiempo en aislamiento](../programa/clases/B113/B113-C04-autonomia-personal-y-gestion-del-tiempo-en-aislamiento/CLASE.md); [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Autonomía compartida

- La autonomía compartida reparte funciones entre ambos; una clasificación consultada distingue cuatro clases de función (adquisición y análisis de información, selección de decisión y ejecución de acción) con un continuo de niveles de automatización desde manual hasta autónomo.

💡 **Cómo se explica en la clase [B98-C03](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md):**
- python programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/supervisado.py
- 🎯 **Por qué importa:** Ni siempre conviene más autonomía ni siempre más control manual: sin retardo, el manual puede ser más rápido. La decisión central: ¿a partir de qué retardo compensa pasar de órdenes cortas a metas supervisadas, y qué se pierde al hacerlo?
- 🔗 **Se estudia junto con:** tiempo de luz de una vía, mover y esperar, control supervisado.

📘 **Dónde se aprende** (1 clase): [B98-C03 · Control supervisado y autonomía compartida](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md).

### Autonomía supervisada

- La autonomía supervisada es dar un objetivo de alto nivel que el robot ejecuta solo.
- La autonomía supervisada agrupa `k` pasos por orden.

💡 **Cómo se explica en la clase [B104-C12](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md):**
- Con retardo de ida de 0 s tarda 189,0 s en modo mover y esperar y 75,0 s con autonomía supervisada (3 objetivos de 25 s); con la Luna (1,28 s), 221,3 s y 82,7 s; con Marte cercano (182,1 s), 4 778,6 s y 1 167,8 s; con Marte lejano (1 337,6 s), 33 896,3 s y 8 100,6 s.
- Calcular el tiempo con autonomía supervisada por objetivos.
- 🎯 **Por qué importa:** Con 0 s de retardo se opera en tiempo real; con 3 minutos cada movimiento tarda mucho más. La decisión central: ¿hasta qué retardo conviene teleoperar paso a paso y a partir de cuándo hay que delegar autonomía supervisada?
- 🔗 **Se estudia junto con:** Mover y esperar, retardo de ida, corrección, teleoperación.

📘 **Dónde se aprende** (2 clases): [B97-C07 · Teleoperación con latencia](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md); [B104-C12 · Robótica tripulada](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md).

### Autor

- El autor responde por el trabajo; el árbitro (*referee*, *reviewer*) lo evalúa y emite un informe; el editor decide, con base en los informes y en su criterio (S1).

💡 **Cómo se explica en la clase [B20-C03](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md):**
- Los autores preparan el manuscrito y responden a las críticas.
- Para ti, como autor, implica que tienes derecho a críticas fundamentadas y no ofensivas, y para ti como futuro árbitro, un código de conducta.
- 🎯 **Por qué importa:** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.
- 🔗 **Se estudia junto con:** revisión por pares, árbitro, editor, informe de árbitro.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Autoridad de lanzamiento

- La autoridad de lanzamiento es el Estado u organización responsable del lanzamiento.

💡 **Cómo se explica en la clase [B119-C02](../programa/clases/B119/B119-C02-acuerdo-de-salvamento/CLASE.md):**
- Por actor: autoridad de lanzamiento y Estado de aterrizaje.
- El texto del Acuerdo de Salvamento no se pudo consultar (la página devolvió 404): lo que se dice de sus obligaciones (notificar, auxiliar, devolver personal y objetos, con gastos a cargo de la autoridad de lanzamiento) es «no consultado» y debe verificarse en la fuente oficial.
- 🎯 **Por qué importa:** El tratado de 1967 (C01) menciona la asistencia a los astronautas (art. V, no discutido en la fuente consultada); el Acuerdo de Salvamento la desarrolla, y ninguna otra clase la cubre.
- 🔗 **Se estudia junto con:** devolución, notificación, banda alcanzable.

📘 **Dónde se aprende** (1 clase): [B119-C02 · Acuerdo de Salvamento](../programa/clases/B119/B119-C02-acuerdo-de-salvamento/CLASE.md).

### Autorización

- La autorización es el permiso previo.

💡 **Cómo se explica en la clase [B119-C08](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md):**
- *Descripción textual:* la solicitud espera, se evalúa y se autoriza; después el operador queda bajo inspección continua, y el Estado responde de todo el proceso.
- Límite: una autorización real tiene varias etapas y servidores.
- 🎯 **Por qué importa:** C01 enuncia el art. VI como regla; esta clase lo convierte en un proceso con tiempos y cobertura, lo que ninguna clase del bloque hace.
- 🔗 **Se estudia junto con:** supervisión continua, tasa de llegada, de servicio, tiempo en el sistema.

📘 **Dónde se aprende** (1 clase): [B119-C08 · Autorización y supervisión de operadores](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md).

### Autorización y supervisión continua

- La autorización y supervisión continua es el control que el Estado debe ejercer sobre sus actores privados (art.

💡 **Cómo se explica en la clase [B119-C01](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md):**
- IV); los Estados responden internacionalmente por sus actividades, también las privadas, que requieren autorización y supervisión continua (art.
- 🎯 **Por qué importa:** Casi todo el derecho espacial posterior (salvamento, responsabilidad, registro, Luna) desarrolla principios de este tratado, y ninguna otra clase del programa lo estudia como instrumento jurídico. La decisión central: ¿qué obligación del tratado se infringe en una misión dada y qué cambio mínimo la devuelve a la conformidad?
- 🔗 **Se estudia junto con:** Estado parte, Jurisdicción y control, Apropiación nacional, regla comprobable.

📘 **Dónde se aprende** (1 clase): [B119-C01 · Tratado del Espacio Ultraterrestre](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md).

### Autoseguro

- El autoseguro es no contratar y asumir la pérdida.

💡 **Contexto en la clase [B127-C08](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md):**
- 🎯 **Por qué importa:** Integrar los seguros de una misión en un caso permite practicar la decisión; no existía tal caso. La decisión central: ¿cuánto se paga de más por reducir el riesgo y qué riesgo se está dispuesto a retener?
- 🔗 **Se estudia junto con:** estrategia, costo del operador, pérdida retenida, riesgo retenido.

📘 **Dónde se aprende** (1 clase): [B127-C08 · Simulación de cobertura de seguros para una misión](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md).

### Autovalor

- Un autovector de una matriz cuadrada `A` es un vector no nulo `v` tal que `A v = λ v`; el número `λ` es su autovalor (S1, §1.2(vi), ec. 1.2.70).
- Un autovalor es una energía permitida.

💡 **Cómo se explica en la clase [B10-C08](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md):**
- Para `diag(2, 3)`, `e₁` y `e₂` son autovectores con autovalores `2` y `3`.
- En general, una matriz real simétrica tiene autovalores reales y un conjunto de autovectores ortonormales (S2, §1.3, sobre operadores autoadjuntos).
- ⚠️ **Error frecuente:** Creer que toda matriz real tiene autovalores reales. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** Un satélite que rota libremente no gira igual alrededor de cualquier eje: tiene tres ejes especiales —los ejes principales de inercia— en los que la rotación es simple. Conocerlos permite diseñar su estabilización, decidir dónde colocar instrumentos sensibles al giro y entender por qué ciertos giros se desestabilizan.
- 🔗 **Se estudia junto con:** autovector, ecuación característica, polinomio característico, espectro.

📘 **Dónde se aprende** (2 clases): [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B31-C02 · Ecuación de Schrödinger](../programa/clases/B31/B31-C02-ecuacion-de-schrodinger/CLASE.md).

### Autovalores

- Los autovalores son las varianzas en los ejes principales del elipsoide de error.

💡 **Cómo se explica en la clase [B74-C11](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md):**
- La covarianza inercial `P_I = Q P Qᵀ` tiene los mismos autovalores (`471,18`, `10000,00`, `252028,82 m²`), la misma traza (`262500,0 m²`) y el mismo determinante que la RTN.
- *Descripción textual:* la covarianza se rota entre marcos, sus autovalores dan los semiejes del elipsoide, las correlaciones muestran la forma y `k²` convierte el elipsoide en una probabilidad.
- ⚠️ **Error frecuente:** Leer solo la diagonal. Mira correlaciones y autovalores.
- 🎯 **Por qué importa:** Los números de la diagonal engañan: dos errores muy correlacionados pueden ser individualmente grandes y conjuntamente pequeños. La decisión central: ¿qué dicen realmente los autovalores, las correlaciones y el elipsoide, y qué probabilidad encierra cada «k sigma» en tres dimensiones?
- 🔗 **Se estudia junto con:** matriz de covarianza, elipsoide de error, correlación, varianza condicional.

📘 **Dónde se aprende** (1 clase): [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Autovector

- Un autovector de una matriz cuadrada `A` es un vector no nulo `v` tal que `A v = λ v`; el número `λ` es su autovalor (S1, §1.2(vi), ec. 1.2.70).

💡 **Cómo se explica en la clase [B10-C08](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md):**
- Para `diag(2, 3)`, `e₁` y `e₂` son autovectores con autovalores `2` y `3`.
- Para `[[2, 1], [1, 2]]`: `λ² − 4λ + 3 = 0`, `λ = 3` y `λ = 1`, con autovectores `(1, 1)` y `(1, −1)`, perpendiculares entre sí.
- ⚠️ **Error frecuente:** Aceptar el vector cero como autovector. Se corrige en el vocabulario y el ejercicio 11.
- 🎯 **Por qué importa:** Un satélite que rota libremente no gira igual alrededor de cualquier eje: tiene tres ejes especiales —los ejes principales de inercia— en los que la rotación es simple. Conocerlos permite diseñar su estabilización, decidir dónde colocar instrumentos sensibles al giro y entender por qué ciertos giros se desestabilizan.
- 🔗 **Se estudia junto con:** autovalor, ecuación característica, polinomio característico, espectro.

📘 **Dónde se aprende** (1 clase): [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md).

### Avance ciego

- El avance ciego es la distancia que recorre el robot mientras no recibe nueva orden.

💡 **Cómo se explica en la clase [B97-C07](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md):**
- *Descripción textual:* de la distancia sale el retardo y el ciclo; agrupar pasos reparte el retardo entre más pasos; el avance ciego mide el riesgo.
- Ejercicio 3 · casi autónomo. ¿Cuánto es el avance ciego del rover durante el ida y vuelta mínimo a Marte?
- ⚠️ **Error frecuente:** Elegir `k` solo por el tiempo. El avance ciego crece con `k` (8.4)
- 🎯 **Por qué importa:** Con un retardo de unos segundos se puede teleoperar casi en vivo; con minutos, no. La diferencia se traduce en horas o días de tarea y en la necesidad de dar autonomía al robot.
- 🔗 **Se estudia junto con:** retardo de ida, ciclo mover y esperar, autonomía supervisada.

📘 **Dónde se aprende** (1 clase): [B97-C07 · Teleoperación con latencia](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md).

### Avance relativista del periapsis

- El avance relativista del periapsis es `Δω` por órbita.

💡 **Contexto en la clase [B72-C17](../programa/clases/B72/B72-C17-efectos-relativistas-orbitales/CLASE.md):**
- 🎯 **Por qué importa:** La corrección relativista es un test histórico de la teoría y, en navegación por satélite, un término que los modelos de precisión no pueden ignorar. La decisión central: ¿cuánto vale el avance relativista del periapsis, cuándo es relevante y qué parte de la relatividad queda fuera de este cálculo?
- 🔗 **Se estudia junto con:** aceleración de Schwarzschild post-newtoniana, precesión de Lense–Thirring, precesión geodésica, mas.

📘 **Dónde se aprende** (1 clase): [B72-C17 · Efectos relativistas orbitales](../programa/clases/B72/B72-C17-efectos-relativistas-orbitales/CLASE.md).

### Aviso

- El aviso es la notificación del siniestro.

💡 **Cómo se explica en la clase [B127-C06](../programa/clases/B127/B127-C06-gestion-de-siniestros-espaciales/CLASE.md):**
- A["aviso del siniestro"] --> I["investigación y peritaje"]
- *Descripción textual:* tras el aviso y el peritaje, la capacidad perdida se compara con el umbral: si lo alcanza se paga como pérdida total menos salvamento y deducible; si no, la fracción perdida menos el deducible.
- 🎯 **Por qué importa:** Tras una pérdida hay un proceso de reclamación y peritaje que ninguna clase describía. La decisión central: ¿cuándo se considera total una pérdida parcial y cuánto cambia el pago por cruzar ese umbral?
- 🔗 **Se estudia junto con:** peritaje, pérdida total constructiva, pérdida parcial, salvamento.

📘 **Dónde se aprende** (1 clase): [B127-C06 · Gestión de siniestros espaciales](../programa/clases/B127/B127-C06-gestion-de-siniestros-espaciales/CLASE.md).

### AW

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?
- 🔗 **Se estudia junto con:** términos, IA, IE, CA.

📘 **Dónde se aprende** (1 clase): [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).
