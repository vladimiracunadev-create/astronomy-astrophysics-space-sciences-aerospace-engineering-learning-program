# Términos · P (parte 3 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · **P** · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-p.md) · [2](terminos-p-2.md) · **3**

### Productividad

- La productividad es masa por hora.
- La productividad es la masa entregada por hora.

💡 **Cómo se explica en la clase [B97-C25](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md):**
- La productividad es `293,21` kg/h: mover una tonelada requiere `33` ciclos.
- *Descripción textual:* la fuerza de corte del suelo y la reacción máxima de la máquina se igualan para dar la profundidad máxima, que fija el volumen y la productividad.
- 🎯 **Por qué importa:** Una excavadora diseñada y probada en la Tierra puede ser incapaz de cortar en la Luna por falta de reacción, no por falta de potencia. Es un error de diseño caro que un cálculo de pocos renglones evita.

📘 **Dónde se aprende** (2 clases): [B97-C25 · Excavación y manejo de regolito con robots](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md); [B97-C27 · Simulación de productividad de flotas de maquinaria](../programa/clases/B97/B97-C27-simulacion-de-productividad-de-flotas-de-maquinaria/CLASE.md).

### Producto

- Un producto es el conjunto archivo de datos más descripción (en el sentido de esta clase).

💡 **Cómo se explica en la clase [B14-C21](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md):**
- Es la versión de C06 (archivo FITS cuyo tamaño no es múltiplo de 2880) para este producto.
- No leí el documento de conceptos ni el *Standards Reference*, de modo que no describo la estructura de un producto, un lote (*bundle*) ni los identificadores lógicos de PDS4 y no afirmo que este laboratorio refleje esos detalles.
- 🎯 **Por qué importa:** Un archivo binario de una sonda planetaria son bytes sin significado: ¿cuántas filas?, ¿enteros o reales?, ¿qué orden de bytes?, ¿qué número indica «no hay dato»?, ¿qué unidad? Y para interpretarlo, hace falta saber dónde estaba la nave y hacia dónde apuntaba.

📘 **Dónde se aprende** (1 clase): [B14-C21 · Datos de misiones planetarias: PDS4, etiquetas y SPICE](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md).

### Producto bruto

- El producto bruto `x` es lo que produce cada etapa.

💡 **Cómo se explica en la clase [B124-C01](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md):**
- El producto bruto cumple `x = A x + f`, es decir `x = (I − A)⁻¹ f`.
- Con los datos sintéticos, el producto bruto total es `286,150` um para una demanda final de `200,0` um.
- ⚠️ **Error frecuente:** Confundir producto bruto con valor agregado. Se corrige con 8.1: el producto bruto cuenta varias veces lo que se compra a otras etapas.
- 🎯 **Por qué importa:** El bloque necesita un mapa común antes de hablar de costos, financiamiento o contratos: ¿quién le compra a quién y dónde queda el valor? Ninguna clase anterior del programa trata la estructura económica de la industria espacial.

📘 **Dónde se aprende** (1 clase): [B124-C01 · Cadena de valor de industria espacial](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md).

### Producto de cuaterniones

- El producto de cuaterniones `a ⊗ b` compone rotaciones.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- Un error de implementación (un signo, el orden del producto de cuaterniones, una convención) o un paso de integración demasiado grande, pues con 0,02 rad la diferencia entre lineal y no lineal debe ser del orden del cuadrado (4×10⁻⁴ relativo), muy por debajo de 10⁻².
- El producto de cuaterniones, el cuaternión identidad, el cálculo del ángulo y la matriz de rotación.
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### Producto de Hamilton

- El producto de Hamilton `p ⊗ q` es la multiplicación que respeta esas reglas (sección 8.2).

🎯 **Por qué importa (clase B10-C15):** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.

📘 **Dónde se aprende** (1 clase): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md).

### Producto escalar

- El producto escalar de `u = (uₓ; u_y; u_z)` y `v = (vₓ; v_y; v_z)` es el número `u · v = uₓvₓ + u_yv_y + u_zv_z`.

💡 **Cómo se explica en la clase [B04-C13](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md):**
- El producto escalar mide cuánto «avanza» uno en la dirección del otro: si apuntan igual, es máximo; si son perpendiculares, cero; si se oponen, negativo.
- *Descripción textual:* de dos vectores unitarios se obtiene su producto escalar, que es el coseno del ángulo entre ellos; si el ángulo no es pequeño se usa arccos, y si es muy pequeño se usa la fórmula por cuerda, que no pierde cifras; el resultado debe quedar entre 0° y 180°.
- 🎯 **Por qué importa:** Antes de apuntar un telescopio de una estrella a otra, antes de saber si dos objetos caben en el mismo campo de visión, antes de decidir si un planeta está demasiado cerca del Sol para observarlo, hay que saber cuántos grados los separan en el cielo.

📘 **Dónde se aprende** (1 clase): [B04-C13 · Producto escalar y ángulo entre vectores](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md).

### Producto interno

- El producto interno (escalar) de `u, v ∈ ℝⁿ` es `⟨u, v⟩ = Σ uᵢ vᵢ`; es simétrico, lineal en cada argumento y `⟨u, u⟩ > 0` si `u ≠ 0` (S1, §1.2(v), ecs. 1.2.40–1.2.43).

💡 **Cómo se explica en la clase [B10-C06](../programa/clases/B10/B10-C06-producto-interno-y-ortogonalidad/CLASE.md):**
- El producto interno mide cuánto de un vector «cabe» en la dirección de otro.
- *Descripción textual:* el signo del producto interno da el tipo de ángulo; cero significa perpendicular; el valor dividido por las normas es el coseno.
- 🎯 **Por qué importa:** La potencia que recibe un panel solar depende del ángulo entre su normal y la dirección al Sol: más inclinado, menos luz. El control de actitud, la orientación de antenas y de instrumentos usan el mismo cálculo.

📘 **Dónde se aprende** (1 clase): [B10-C06 · Producto interno y ortogonalidad](../programa/clases/B10/B10-C06-producto-interno-y-ortogonalidad/CLASE.md).

### Producto iónico del agua

- El producto iónico del agua `K_w = [H⁺][OH⁻]` vale, a 25 °C, `1,0 × 10⁻¹⁴` (valor de trabajo de la clase), por lo que `pH + pOH = 14`.

🎯 **Por qué importa (clase B06-C15):** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Producto iónico (IP)

- Orina pretratada: orina con aditivos que estabilizan. Producto iónico (IP): `[Ca][SO₄]`.

💡 **Cómo se explica en la clase [B106-C27](../programa/clases/B106/B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md):**
- Si la fracción recuperada es `r`, el residuo se concentra `CF = 1/(1 − r)` veces y el producto iónico crece `CF²`.
- *Descripción textual:* la destilación recupera agua y concentra la salmuera; si el producto iónico supera el de solubilidad, la sal precipita y obstruye; una segunda etapa trata la salmuera.
- 🎯 **Por qué importa:** Evaporar la orina concentra sales hasta que precipitan y obstruyen el equipo; el límite lo fija la química, no la termodinámica del agua. La decisión central: ¿hasta qué fracción se puede recuperar el agua antes de precipitar y cómo se supera ese límite?

📘 **Dónde se aprende** (1 clase): [B106-C27 · Tratamiento de orina y recuperación de agua](../programa/clases/B106/B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md).

### Producto matricial

- El producto matricial `AB` aplica primero `B` y luego `A`.

🎯 **Por qué importa (clase B10-C03):** Una estación terrestre está fija respecto de la Tierra, pero la Tierra gira respecto del espacio inercial. Para saber dónde está la estación en el sistema inercial a cada instante hay que aplicar una transformación que depende del tiempo.

📘 **Dónde se aprende** (1 clase): [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md).

### Producto tensorial

- El producto tensorial (o externo) de `a` y `b` es el tensor de rango 2 `(a ⊗ b)ᵢⱼ = aᵢ bⱼ` (una matriz `a bᵀ`).

💡 **Cómo se explica en la clase [B10-C18](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md):**
- El script [tensor_de_marea.py](tensor_de_marea.py) comprueba producto tensorial y contracción, forma el tensor de marea, verifica su traza y autovalores, lo contrasta con diferencias finitas y comprueba su transformación bajo una rotación.
- python programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/tensor_de_marea.py
- 🎯 **Por qué importa:** La gravedad no es uniforme a lo largo de un satélite: lo que está más cerca de la Tierra se acelera más que lo que está lejos, y lo que está a los lados se comprime. Con una sola derivada `dg/dr` solo describes la dirección radial; el tensor de marea describe las tres direcciones a la vez.

📘 **Dónde se aprende** (1 clase): [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md).

### Producto tiempo–ancho de banda

- El producto tiempo–ancho de banda `Bτ` es la ganancia de compresión.

💡 **Cómo se explica en la clase [B57-C07](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md):**
- Longitud de onda = 5.547 cm ; producto tiempo-ancho de banda = 1000
- 🎯 **Por qué importa:** La luz visible no atraviesa nubes ni sirve de noche; las microondas sí. Pero un radar no «fotografía»: mide distancia y fase de ecos.

📘 **Dónde se aprende** (1 clase): [B57-C07 · Sistemas radar SAR](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md).

### Producto vectorial

- El producto vectorial `u × v` es el vector perpendicular a `u` y a `v` con módulo `|u||v| sen γ` y sentido dado por la regla de la mano derecha: si los dedos van de `u` hacia `v` por el ángulo menor, el pulgar apunta a `u × v`.

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- Comprobar numéricamente las propiedades del producto vectorial.
- python programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/orientacion_orbital.py
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?

📘 **Dónde se aprende** (1 clase): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md).

### Productos

- Los reactivos están a la izquierda y los productos a la derecha de una ecuación química.

💡 **Cómo se explica en la clase [B06-C08](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md):**
- Se escriben las fórmulas de los reactivos, una flecha y las de los productos: `CH₄ + O₂ → CO₂ + H₂O`.
- R["Reactivos: CH4 + O2"] -->|"átomos se reordenan"| P["Productos: CO2 + H2O"]
- ⚠️ **Error frecuente:** No contar el hidrógeno de ambos productos. Se corrige con el ejercicio 2 y el 11.
- 🎯 **Por qué importa:** Una vela y el Sol liberan energía, pero lo hacen de maneras radicalmente distintas. En la vela, los átomos de carbono e hidrógeno se reordenan con el oxígeno y todos siguen ahí al terminar.

📘 **Dónde se aprende** (1 clase): [B06-C08 · Reacciones y conservación de masa](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md).

### Proficiencia

- La proficiencia `p` es la probabilidad de entender bien un elemento crítico y `d` la de detectar el error mediante repetición de lectura.

💡 **Cómo se explica en la clase [B111-C02](../programa/clases/B111/B111-C02-gestion-intercultural-en-tripulaciones-multinacionales/CLASE.md):**
- La repetición de lectura reduce el riesgo en un factor de 4 a 5 en estos casos, para cualquier proficiencia: es un procedimiento, no un juicio sobre las personas.
- Un mensaje de 5 elementos críticos a un miembro con proficiencia `0,90` tiene `40,95 %` de probabilidad de un malentendido no detectado sin repetición de lectura y `9,61 %` con ella (detección `0,8`).
- 🎯 **Por qué importa:** Ninguna clase del programa trataba las diferencias culturales y de idioma en equipos internacionales. La decisión central: ¿cómo se vuelve un riesgo de comunicación cuantificable y cómo se mitiga con procedimientos y no con estereotipos?

📘 **Dónde se aprende** (1 clase): [B111-C02 · Gestión intercultural en tripulaciones multinacionales](../programa/clases/B111/B111-C02-gestion-intercultural-en-tripulaciones-multinacionales/CLASE.md).

### Profundidad

- El tránsito es la disminución de brillo cuando un cuerpo pasa por delante de su estrella; su profundidad es la fracción de flujo que se pierde.
- La profundidad es la caída relativa de flujo.
- La profundidad es `1 − F_en/F_fuera`.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C07](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md):**
- Estima la profundidad: `0,01006` frente a la verdadera 0,01.
- Paso final · incertidumbre. La profundidad estimada concuerda con la verdadera dentro de 6 × 10⁻⁵, pero una sola realización del ruido no dice cuánto varía esa estimación; para eso habría que repetir con varias semillas (B12).
- 🎯 **Por qué importa:** Una simulación o un instrumento moderno produce series de millones de muestras con sus metadatos. Guardarlas en texto es lento y pesado; cargarlas enteras en memoria para leer un fragmento es inviable.

📘 **Dónde se aprende** (10 clases): [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md); [B28-C15 · Búsqueda de contrapartidas ópticas](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md); [B29-C01 · Tránsitos planetarios](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md); [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md); [B53-C17 · Mineralogía espectral](../programa/clases/B53/B53-C17-mineralogia-espectral/CLASE.md); [B53-C24 · Sondeo radar de penetración de hielo](../programa/clases/B53/B53-C24-sondeo-radar-de-penetracion-de-hielo/CLASE.md) y 4 más.

### Profundidad atmosférica

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B33-C08):** La altitud y la profundidad atmosférica determinan cuánta radiación llega. La decisión central: ¿cuánto menos atmósfera hay a la altitud de vuelo?

📘 **Dónde se aprende** (1 clase): [B33-C08 · Dosis de radiación en aviación](../programa/clases/B33/B33-C08-dosis-de-radiacion-en-aviacion/CLASE.md).

### Profundidad de bloqueo

- La profundidad de bloqueo es la profundidad sobre la cual la falla está trabada.

💡 **Cómo se explica en la clase [B57-C17](../programa/clases/B57/B57-C17-terremotos-y-deformacion/CLASE.md):**
- Aquí lo modelas con una falla ilustrativa de `500 × 100 km` y rigidez `30 GPa`, y comparas con una falla de tornillo de deslizamiento `4 m` y profundidad de bloqueo `15 km`.
- 🎯 **Por qué importa:** Medir la deformación permite saber cuánto deslizó la falla y cuánta tensión queda. La decisión central: ¿cómo se pasa de un número de magnitud al deslizamiento y a la deformación que verá un satélite?

📘 **Dónde se aprende** (1 clase): [B57-C17 · Terremotos y deformación](../programa/clases/B57/B57-C17-terremotos-y-deformacion/CLASE.md).

### Profundidad de compresión

- La profundidad de compresión `d` es cuánto se hunde el esternón del maniquí, en mm.

💡 **Cómo se explica en la clase [B117-C01](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md):**
- Un estudio en maniquí en vuelos parabólicos (comunicado del 2025-08-27) midió profundidades de compresión medianas de 34,5 mm con el método manual «handstand», 53,0 mm con un pistón mecánico estándar y 29 mm con otros dos dispositivos, con unos 22 s de microgravedad por parábola.
- Modelar la profundidad de compresión con una curva de fatiga `d(t)`.
- 🎯 **Por qué importa:** Ninguna clase anterior trata primeros auxilios en microgravedad. La decisión central: ¿cuánto tiempo puede sostener un reanimador una compresión de calidad y cuándo hay que relevarlo?

📘 **Dónde se aprende** (1 clase): [B117-C01 · Primeros auxilios y procedimientos básicos en entorno espacial](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md).

### Profundidad de Curie

- La profundidad de Curie es la profundidad donde la temperatura alcanza la de Curie.

💡 **Cómo se explica en la clase [B65-C03](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md):**
- La profundidad de Curie ilustrativa, con `T_C = 853 K`, `T_s = 210 K` y un gradiente de `15 K/km`, es `(853 − 210)/15 = 42,9 km`.
- Ejercicio 8. Profundidad de Curie con un gradiente de `30 K/km`.
- 🎯 **Por qué importa:** La corteza magnetizada permite reconstruir campos de cuerpos que hoy no tienen dinamo. La decisión central: ¿qué parte de un mapa de anomalías es información sobre la magnetización y qué parte es ambigüedad geométrica?

📘 **Dónde se aprende** (1 clase): [B65-C03 · Magnetismo cortical remanente y anomalías magnéticas](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md).

### Profundidad de descarga

- La profundidad de descarga (DoD) es la energía extraída entre la capacidad.
- Autonomía: tiempo que el respaldo sostiene la carga. Profundidad de descarga (DoD): fracción usable de la batería.
- Espesor másico: densidad por espesor (g/cm²). Profundidad de descarga: fracción usada de una batería.

💡 **Cómo se explica en la clase [B47-C25](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md):**
- Calcular el balance de potencia y la profundidad de descarga.
- energia en eclipse = 2.264 Wh ; profundidad de descarga = 11.32 %
- 🎯 **Por qué importa:** Muchos CubeSat universitarios fracasan por requisitos sin cifra o sin evidencia. La decisión central: ¿qué requisitos medibles se fijan, cómo se verifican y cuáles cumple un diseño preliminar?

📘 **Dónde se aprende** (4 clases): [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md); [B48-C07 · Seguridad en instalaciones remotas](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md); [B83-C10 · Presupuestos de energía](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md); [B106-C19 · Arquitectura de asentamiento lunar conceptual](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md).

### Profundidad de enfoque

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C15](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md):**
- Con profundidad de enfoque `4λN² = 0,220 mm` (N = 10): el singlete desenfoca `48,56` profundidades entre 486 y 656 nm, el doblete `2,57` y el triplete `0,15`; entre 400 y 800 nm: `26,467; 4,532; 0,303 mm`.
- Ejercicio 7. Profundidades de enfoque del doblete.
- 🎯 **Por qué importa:** Un refractor sin color necesita combinar vidrios. La decisión central: ¿cuánto color queda con dos o tres vidrios?

📘 **Dónde se aprende** (1 clase): [B41-C15 · Refractores acromáticos y apocromáticos](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md).

### Profundidad de excavación

- La profundidad de excavación es la que alcanza la cavidad transitoria.

💡 **Cómo se explica en la clase [B61-C07](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md):**
- Con profundidad de excavación ilustrativa 0,1 D y corteza de 40 km: 300 km → 30 km (corteza); 600 km → 60 km (manto); 1000 km → 100 km (manto).
- Comparar una profundidad de excavación ilustrativa con el espesor de la corteza.
- 🎯 **Por qué importa:** Las cuencas dejan huella en la corteza entera. La decisión central: ¿cómo se espacian los anillos, qué proyectil implica una cuenca y cuándo excava hasta el manto?

📘 **Dónde se aprende** (1 clase): [B61-C07 · Cuencas multianillo y grandes impactos](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md).

### Profundidad de foco

- La profundidad de foco es `±2λN²`.
- La profundidad de foco (`±2 λ N²`).

💡 **Cómo se explica en la clase [B50-C07](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md):**
- Calcular el hundimiento `fθ²/2` y compararlo con la profundidad de foco.
- 🎯 **Por qué importa:** Un detector plano mal enfocado en el borde pierde resolución: hay que decidir si se acepta, se curva el detector o se agrega un aplanador. La decisión central: ¿cuánto se hunde el foco en el borde y qué lo corrige?

📘 **Dónde se aprende** (3 clases): [B41-C19 · Colimación y prueba de enfoque](../programa/clases/B41/B41-C19-colimacion-y-prueba-de-enfoque/CLASE.md); [B50-C07 · Curvatura de campo y aplanadores](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md); [B50-C12 · Sensibilidad térmica del desempeño óptico y atermalización](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md).

### Profundidad de Nye

- La profundidad de Nye es `d = (2/(ρ g)) (ε̇/A)^(1/n)`.

💡 **Cómo se explica en la clase [B53-C23](../programa/clases/B53/B53-C23-mecanica-de-hielo-reologia-fracturas-y-deformacion/CLASE.md):**
- *Descripción textual:* La temperatura fija el coeficiente `A`; con el esfuerzo da la tasa de deformación; esta se integra en la velocidad de la lámina y fija la profundidad de las grietas.
- La profundidad de una grieta de Nye con `ε̇ = 10⁻¹⁰ s⁻¹` es `8,5 m`.
- 🎯 **Por qué importa:** El hielo de una luna fría se comporta como un sólido casi rígido y el de un glaciar templado fluye. La decisión central: ¿cuánto cambia la velocidad de deformación con la temperatura, el espesor y la gravedad?

📘 **Dónde se aprende** (1 clase): [B53-C23 · Mecánica de hielo: reología, fracturas y deformación](../programa/clases/B53/B53-C23-mecanica-de-hielo-reologia-fracturas-y-deformacion/CLASE.md).

### Profundidad de penetración

- La profundidad de penetración es `δ = √(2κ/ω)`.
- La profundidad de penetración `λ/(4πk)`.

💡 **Cómo se explica en la clase [B43-C07](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md):**
- Ejercicio 2 · con una pista. Profundidad de penetración `λ/(4πk)`.
- 🎯 **Por qué importa:** Una película delgada deja pasar luz; una gruesa refleja pero no se adhiere ni es uniforme. La decisión central: ¿qué espesor es opaco, qué reflectancia da y cuánto varía de centro a borde por la geometría del evaporador?

📘 **Dónde se aprende** (2 clases): [B43-C07 · Aluminizado y recubrimientos](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md); [B67-C06 · Pérdida de volátiles por sublimación y migración térmica](../programa/clases/B67/B67-C06-perdida-de-volatiles-por-sublimacion-y-migracion-termica/CLASE.md).

### Profundidad de piel

- La profundidad de piel es `δ = √(2/(μ₀ σ ω))`.

💡 **Cómo se explica en la clase [B53-C27](../programa/clases/B53/B53-C27-deteccion-remota-de-oceanos-subsuperficiales-induccion-magnetica-libracion-y-radar/CLASE.md):**
- *Descripción textual:* El período de excitación y la conductividad dan la profundidad de piel y la atenuación; la inercia de la capa da la amplificación de la libración; ambas son evidencia independiente.
- Con un período sinódico de `11,23 h` (de períodos de rotación y orbital de uso común, no consultados) y `σ = 2,5 S/m` (ilustrativa), la profundidad de piel es `64,0 km`.
- 🎯 **Por qué importa:** Cada método ve algo distinto y ninguno basta solo. La decisión central: ¿qué señal esperaría un océano de cierta conductividad y espesor y cuánto se distingue de un cuerpo sólido?

📘 **Dónde se aprende** (1 clase): [B53-C27 · Detección remota de océanos subsuperficiales: inducción magnética, libración y radar](../programa/clases/B53/B53-C27-deteccion-remota-de-oceanos-subsuperficiales-induccion-magnetica-libracion-y-radar/CLASE.md).

### Profundidad de pulverización

- La profundidad de pulverización `Nd` es la columna de hielo desde la que se expulsan moléculas.

💡 **Cómo se explica en la clase [B68-C03](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md):**
- S --> N["Nd(Se): profundidad de pulverizacion"]
- No: con `Se` alto 1 ML rinde solo ~7 % del grueso (CO, `Se = 100`); la profundidad de pulverización es de decenas de ML (8.3).
- 🎯 **Por qué importa:** Un hielo en una nube densa recibe poca luz ultravioleta externa, pero sigue recibiendo partículas energéticas y fotones secundarios. Esas dosis lentas transforman la composición del hielo durante millones de años.

📘 **Dónde se aprende** (1 clase): [B68-C03 · Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md).

### Profundidad del máximo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B31-C13):** La energía y la composición de un rayo cósmico se infieren de la forma de su cascada, y el fondo de microondas limita la energía que llega. La decisión central: ¿qué profundidad y tamaño tiene una cascada y a qué energía aparece un corte?

📘 **Dónde se aprende** (1 clase): [B31-C13 · Rayos cósmicos y cascadas](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md).

### Profundidad del océano

- La profundidad del océano `d_o` es la del agua.

💡 **Cómo se explica en la clase [B56-C09](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md):**
- Con `d_h = 5, 15, 30 km`, la profundidad del océano sale `93,2; 94,6; 96,6 km` y la presión `131,8; 145,7; 166,5 MPa`.
- Descripción larga: la profundidad del océano casi no depende del espesor del hielo; la presión sí, porque suma la columna de hielo.
- 🎯 **Por qué importa:** Un océano global bajo el hielo es un candidato a hábitat, protegido de la radiación y del vacío. Saber cuán profundo es y qué presión soporta fija qué sondas podrían llegar y qué ambientes existen.

📘 **Dónde se aprende** (1 clase): [B56-C09 · Océanos de Europa](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md).

### Profundidad máxima

- La profundidad máxima es la que iguala ambas.

💡 **Cómo se explica en la clase [B97-C25](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md):**
- *Descripción textual:* la fuerza de corte del suelo y la reacción máxima de la máquina se igualan para dar la profundidad máxima, que fija el volumen y la productividad.
- La profundidad máxima de corte es `0,1190`, `0,0630` y `0,0297` m.
- 🎯 **Por qué importa:** Una excavadora diseñada y probada en la Tierra puede ser incapaz de cortar en la Luna por falta de reacción, no por falta de potencia. Es un error de diseño caro que un cálculo de pocos renglones evita.

📘 **Dónde se aprende** (1 clase): [B97-C25 · Excavación y manejo de regolito con robots](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md).

### Profundidad óptica

- La extinción es la pérdida de luz por absorción y dispersión en el camino; si es exponencial, `I = I₀ e^(−τ)` con `τ` la profundidad óptica.
- La profundidad óptica `τ` mide cuánta opacidad se atraviesa desde fuera: `τ = ∫ κ ρ dr`; con `τ = 1` la intensidad cae un factor `e`.
- La profundidad óptica `τ` es el exponente de atenuación `F = F₀ e^{−τ}`.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C09](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md):**
- *Descripción textual:* la temperatura crece con la profundidad óptica; la luz que llega al observador proviene sobre todo de `τ ≈ 2/3`, donde `T = T_ef`.
- En el modelo gris, la luz que vemos sale de la capa de profundidad óptica `τ ≈ 2/3`, a `5772 K`; la capa más externa (`τ = 0`) está a `4854 K`, y a `τ = 10` la temperatura es `9707 K`.
- 🎯 **Por qué importa:** Toda temperatura o composición que atribuimos a una estrella se infiere de una capa delgada. Saber de qué profundidad viene la luz, cuánto vale la opacidad y cuánto puede brillar una estrella sin expulsar su atmósfera es lo que permite interpretar espectros (C10) y entender los vientos (C17).

📘 **Dónde se aprende** (13 clases): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B24-C09 · Atmósferas y opacidades](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md); [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md); [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B32-C01 · Ecuación de transferencia radiativa en atmósferas estelares](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md); [B32-C05 · Relación T-τ y estructura térmica de la fotosfera](../programa/clases/B32/B32-C05-relacion-t-y-estructura-termica-de-la-fotosfera/CLASE.md) y 7 más.

### Profundidad óptica central

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B32-C09):** Medir una abundancia exige saber en qué régimen está la línea. La decisión central: ¿cómo depende el ancho equivalente de la columna de absorbedores?

📘 **Dónde se aprende** (1 clase): [B32-C09 · Medición de perfiles de línea: ancho equivalente y ajuste](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md).

### Profundidad óptica infrarroja

- La profundidad óptica infrarroja `τ` mide cuán opaca es, de arriba abajo.

🎯 **Por qué importa (clase B54-C09):** La diferencia entre la temperatura de equilibrio (B54-C03) y la observada necesita una causa. La pregunta motivadora: ¿qué opacidad infrarroja hace falta para explicar la temperatura de superficie de cada mundo?

📘 **Dónde se aprende** (1 clase): [B54-C09 · Efecto invernadero](../programa/clases/B54/B54-C09-efecto-invernadero/CLASE.md).

### Profundidad solar

- La profundidad solar `δ` es el ángulo del Sol bajo el horizonte.

💡 **Cómo se explica en la clase [B118-C16](../programa/clases/B118/B118-C16-contaminacion-luminica/CLASE.md):**
- La profundidad solar máxima a la que un satélite de 550 km sigue iluminado es 23,00° (a 1200 km, 32,70°); a 15°/h en el ecuador son unos 92 min (aproximación).
- Descripción larga: la ventana de iluminación llega hasta unos 23° de profundidad solar; el satélite del ejemplo es de magnitud ≈ 5, al borde de lo visible a simple vista; en una exposición de 30 s la probabilidad de una traza en un campo de 3° es del orden de 7 %.
- 🎯 **Por qué importa:** El brillo y el número de satélites visibles dependen de la altitud y de la profundidad del Sol bajo el horizonte; para un telescopio, una traza arruina la zona que cruza. La decisión central: ¿cuánto dura la ventana de iluminación, qué tan brillante es el satélite y cuántas trazas esperar en una exposición?

📘 **Dónde se aprende** (1 clase): [B118-C16 · Contaminación lumínica](../programa/clases/B118/B118-C16-contaminacion-luminica/CLASE.md).

### Prógrada

- Una órbita es prógrada si el disco gira en el mismo sentido que el encuentro.
- El vector nodo `n = ẑ × h` apunta al nodo ascendente. Prógrada es `i < 90°`;
- Una transferencia es prógrada si `n` apunta hacia el eje de referencia `+z` (`h_z > 0`) y retrógrada si apunta hacia `−z`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B52-C11](../programa/clases/B52/B52-C11-formacion-de-satelites-naturales/CLASE.md):**
- En la simulación, las órbitas prógradas circulares sobreviven hasta `0.475 R_H` y las retrógradas hasta `0.975 R_H`.
- Integrar órbitas circulares prógradas y retrógradas con RK4.
- 🎯 **Por qué importa:** Los satélites regulares ocupan una pequeña fracción de la esfera de Hill, y el límite exterior de órbitas estables restringe dónde pudo existir el disco circumplanetario. La decisión central: ¿hasta qué fracción del radio de Hill puede haber satélites y dónde están los reales?

📘 **Dónde se aprende** (5 clases): [B25-C12 · Interacciones y fusiones galácticas](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md); [B52-C11 · Formación de satélites naturales](../programa/clases/B52/B52-C11-formacion-de-satelites-naturales/CLASE.md); [B71-C11 · Inclinación y nodo ascendente](../programa/clases/B71/B71-C11-inclinacion-y-nodo-ascendente/CLASE.md); [B76-C03 · Órbitas alrededor de la Luna](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md); [B82-C02 · Lambert de arco largo](../programa/clases/B82/B82-C02-lambert-de-arco-largo/CLASE.md).

### Progradación

- La progradación es el avance de un delta hacia la cuenca.

🎯 **Por qué importa (clase B66-C05):** Los deltas marcianos se interpretan como archivo de ambientes pasados, pero un grano cae más despacio con menos gravedad y el mismo flujo puede dejar otra facies. La decisión central: ¿cómo cambia la facies que deja un flujo cuando cambia la gravedad?

📘 **Dónde se aprende** (1 clase): [B66-C05 · Depósitos sedimentarios y sedimentología planetaria](../programa/clases/B66/B66-C05-depositos-sedimentarios-y-sedimentologia-planetaria/CLASE.md).

### Programa

- Un programa es un algoritmo escrito en un lenguaje que una máquina puede ejecutar.

💡 **Cómo se explica en la clase [B07-C01](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md):**
- Un archivo `.py` es un texto con instrucciones que el intérprete (el programa `python`) ejecuta de arriba abajo.
- Una prueba automática usa `assert condición`, que detiene el programa con un error si la condición es falsa.
- 🎯 **Por qué importa:** En astronomía casi todo resultado pasa por un procedimiento repetible: reducir imágenes, ajustar una órbita, buscar el máximo de una curva de luz. Si no puedes describir el procedimiento con precisión, no puedes ejecutarlo en un computador ni dárselo a otra persona para que lo repita.

📘 **Dónde se aprende** (1 clase): [B07-C01 · Pensamiento algorítmico](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md).

### Programa de cabeceo

- El programa de cabeceo es la ley `γ(t)` con que se inclina la trayectoria.

💡 **Cómo se explica en la clase [B77-C08](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md):**
- *Descripción textual:* el empuje inicial fija el tiempo de combustión; con el programa de cabeceo se integra la pérdida gravitacional, que se resta del `Δv` ideal para dar el `Δv` neto.
- Integrarla con la regla de Simpson para un programa de cabeceo lineal.
- 🎯 **Por qué importa:** Un `Δv` ideal alto no garantiza velocidad alta al final. La decisión central: ¿cuánto del `Δv` se pierde por gravedad y cómo se reduce con más empuje o con una trayectoria más inclinada?

📘 **Dónde se aprende** (1 clase): [B77-C08 · Pérdidas gravitacionales](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md).

### Programación dinámica

- Voraz: elección paso a paso. Programación dinámica: solución exacta por subproblemas.
- La programación dinámica lo resuelve exactamente.
- La programación dinámica resuelve el problema por etapas.

💡 **Cómo se explica en la clase [B47-C17](../programa/clases/B47/B47-C17-planificacion-de-observaciones/CLASE.md):**
- Con presupuesto de 150 min: voraz `47` (usa `145 min`), programación dinámica `47` y enumeración de los 4096 subconjuntos `47`.
- Blancos (10, 60), (20, 100), (30, 120) con presupuesto 50: voraz `160`; óptimo `220` (programación dinámica) y `220` (enumeración).
- 🎯 **Por qué importa:** Sin planificación se desperdicia tiempo de observación. La decisión central: ¿qué blancos observar con un presupuesto de tiempo limitado y cuánto tiempo hay de visibilidad?

📘 **Dónde se aprende** (4 clases): [B47-C17 · Planificación de observaciones](../programa/clases/B47/B47-C17-planificacion-de-observaciones/CLASE.md); [B96-C10 · Planificación de cargas útiles](../programa/clases/B96/B96-C10-planificacion-de-cargas-utiles/CLASE.md); [B104-C23 · Ejecución de experimentos a bordo: procedimientos y registro](../programa/clases/B104/B104-C23-ejecucion-de-experimentos-a-bordo-procedimientos-y-registro/CLASE.md); [B117-C05 · Inventario y gestión del equipo médico a bordo](../programa/clases/B117/B117-C05-inventario-y-gestion-del-equipo-medico-a-bordo/CLASE.md).

### Progresión

- Una progresión es la serie de bandas con `v'` creciente.

💡 **Cómo se explica en la clase [B62-C03](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md):**
- Las intensidades relativas de la progresión del caso A (v' = 0…5) son 0,484; 0,983; 1,000; 0,678; 0,345; 0,140.
- *Descripción textual:* dos funciones de onda en pozos desplazados dan un solapamiento; su cuadrado es el FC, la progresión es la lista de FC y todos suman 1.
- ⚠️ **Error frecuente:** Confundir FC con intensidad absoluta. Se corrige con 8.1: es una intensidad relativa dentro de la progresión.
- 🎯 **Por qué importa:** Las bandas electrónicas aparecen en el ultravioleta y el visible; su forma, una serie de picos, revela cuánto cambia la geometría de la molécula. La decisión central: ¿qué picos de la progresión serán intensos?

📘 **Dónde se aprende** (1 clase): [B62-C03 · Transiciones electrónicas moleculares](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md).

### Prolongación

- Restricción es pasar un campo a la malla gruesa; prolongación, a la fina.
- La restricción promedia datos finos en una celda gruesa; la prolongación reparte datos de una celda gruesa en sus hijas.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- Prolongación: llevar `e` a la malla fina por interpolación bilineal y sumar `u ← u + e`.
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;

📘 **Dónde se aprende** (2 clases): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md); [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Promediado

- El promediado de `M` espectros reduce la dispersión como `1/√M`.

💡 **Cómo se explica en la clase [B46-C10](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha del espectrómetro SDR*: resolución, ENBW y tabla del promediado.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha del espectrómetro SDR*: resolución, ENBW y tabla del promediado.
- 🎯 **Por qué importa:** Promediar espectros es la forma práctica de aplicar la ecuación del radiómetro con un instrumento barato, pero la ventana cambia el ancho de banda efectivo. La decisión central: ¿cuántos espectros promediar para detectar una línea débil?

📘 **Dónde se aprende** (1 clase): [B46-C10 · Radioastronomía mediante SDR](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md).

### Promediando

- El moteado hace que cada pulso sea ruidoso; se reduce promediando pulsos.

💡 **Cómo se explica en la clase [B57-C09](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md):**
- El eco real es borroso; ajustas su inicio promediando muchas veces.
- 🎯 **Por qué importa:** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Promedio

- El promedio `ȳᵢ(τ)` es el promedio de `y` en un intervalo `τ = m τ₀`.

💡 **Cómo se explica en la clase [B13-C07](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md):**
- La serie `y_k` es el promedio de `y` en cada intervalo de `τ₀`.
- Una ventaja de usar `y` es que un sesgo constante de frecuencia no cambia las diferencias entre promedios contiguos: la desviación de Allan no ve la desviación media, solo su variabilidad.
- 🎯 **Por qué importa:** Dos relojes pueden tener la misma desviación de frecuencia media y comportarse de forma muy distinta: uno oscila alrededor de su valor y otro se aleja de él con el tiempo. La desviación típica ordinaria no sirve para describirlo, porque en un reloj con deriva no converge.

📘 **Dónde se aprende** (1 clase): [B13-C07 · Relojes atómicos y frecuencia](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md).

### Promedio de celda

- Una celda es un tramo de longitud `Δx` del dominio; el promedio de celda `q_i` es el valor medio de `q` en ella.

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- Si el promedio de celda es `q_i^n` en el instante `t_n`, la actualización de volúmenes finitos es
- A["Promedios de celda<br/>q_i en el tiempo n"] --> B["Estados a izquierda y derecha<br/>de cada interfaz"]
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.

📘 **Dónde se aprende** (1 clase): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md).

### Promedio de Gauss

- El promedio de Gauss es la media sobre la anomalía media de `dΩ/dt = r sin(ω+ν) W/(h sin i)`, con `W` la aceleración fuera del plano y `h = √(μp)`.
- El promedio de Gauss es la media sobre la anomalía media de las ecuaciones de variación con las aceleraciones J2 y J3.

💡 **Cómo se explica en la clase [B72-C04](../programa/clases/B72/B72-C04-precesion-del-nodo-orbital/CLASE.md):**
- G["promedio de Gauss"] --> V["verificar"]
- *Descripción textual:* la tasa depende de J2, del movimiento medio y de `cos i`; se tabula para el diseño y se verifica con el promedio numérico de Gauss.
- 🎯 **Por qué importa:** El nodo decide a qué hora local pasa un satélite sobre un lugar y cuándo su plano apunta al Sol. La decisión central: ¿qué altitud e inclinación hacen que el nodo avance o retroceda lo que necesita la misión?

📘 **Dónde se aprende** (2 clases): [B72-C04 · Precesión del nodo orbital](../programa/clases/B72/B72-C04-precesion-del-nodo-orbital/CLASE.md); [B72-C14 · Órbitas congeladas](../programa/clases/B72/B72-C14-orbitas-congeladas/CLASE.md).

### Promedio en energía

- El promedio en energía lleva `P` a `sen²2θ/2`.

💡 **Cómo se explica en la clase [B31-C11](../programa/clases/B31/B31-C11-neutrinos-y-oscilaciones/CLASE.md):**
- A 5000 km con energía uniforme entre 0,5 y 2 GeV, el promedio es `0,4985`, cerca del límite `sen²2θ/2 = 0,5`.
- *Descripción textual:* las constantes dan el coeficiente, la fase y la probabilidad, de la que salen la longitud de oscilación, las detecciones y el promedio en energía.
- 🎯 **Por qué importa:** Detectar neutrinos del Sol, la atmósfera y aceleradores exige saber cuánto oscilan. La decisión central: ¿cuál es la probabilidad de oscilación a cierta distancia y energía?

📘 **Dónde se aprende** (1 clase): [B31-C11 · Neutrinos y oscilaciones](../programa/clases/B31/B31-C11-neutrinos-y-oscilaciones/CLASE.md).

### Promedio global de visibles

- El promedio global de visibles es `T(1 − cos λ)/2` si los satélites se distribuyen uniformemente.

💡 **Cómo se explica en la clase [B89-C17](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md):**
- Comprobar el promedio global de visibles con `T(1 − cos λ)/2`.
- 🎯 **Por qué importa:** El número de satélites, su altitud y la inclinación fijan cuánta gente o cuántos usuarios ven al menos uno (o cuatro, para navegar) y cuánto cuesta lograrlo. La decisión central: ¿cuántos satélites y qué geometría dan la cobertura necesaria?

📘 **Dónde se aprende** (1 clase): [B89-C17 · Constelaciones y cobertura](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md).

### Promedio orbital

- El promedio orbital integra la tasa a lo largo de un día.

🎯 **Por qué importa (clase B85-C22):** La dosis anual decide el blindaje y la vida de la electrónica y los materiales. La decisión central: ¿cuánta dosis acumula una órbita al año y cuánto la reduce un milímetro más de blindaje?

📘 **Dónde se aprende** (1 clase): [B85-C22 · Modelos de exposición a radiación en órbita](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md).

### Prominencia

- El filamento o la prominencia.

💡 **Cómo se explica en la clase [B34-C08](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md):**
- Una prominencia de `10¹² kg` a `30 Mm` tiene `8,2 × 10²¹ J` de energía potencial; a `100 km/s`, `5,0 × 10²¹ J` de cinética.
- python programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/filamento.py
- 🎯 **Por qué importa:** Saber a qué altura el campo ya no sostiene al filamento sirve para anticipar erupciones. La decisión central: ¿a qué altura el decaimiento del campo supera el umbral?

📘 **Dónde se aprende** (1 clase): [B34-C08 · Erupciones de filamentos y prominencias](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md).

### Pronóstico

- Un pronóstico daría una probabilidad con fecha; esta clase no lo hace.

💡 **Cómo se explica en la clase [B57-C20](../programa/clases/B57/B57-C20-caso-de-estudio-climatico-o-geologico-de-chile/CLASE.md):**
- Explicar por qué la cuenta no es un pronóstico.
- Límites: acumulación uniforme y sin deslizamiento asísmico; no es un pronóstico.
- ⚠️ **Error frecuente:** Leer el tiempo de reposición como pronóstico. Es una escala (8.4).
- 🎯 **Por qué importa:** Chile vive sobre una zona de subducción activa y las instituciones deben comprender cuánta deformación se acumula y se libera. La decisión central: ¿qué puede decir una cuenta de balance de deslizamiento y qué no puede decir sobre cuándo ocurrirá el próximo terremoto?

📘 **Dónde se aprende** (1 clase): [B57-C20 · Caso de estudio climático o geológico de Chile](../programa/clases/B57/B57-C20-caso-de-estudio-climatico-o-geologico-de-chile/CLASE.md).

### Propagación

- La propagación es la transmisión de los errores de los datos al resultado.
- La propagación es el recálculo de lo que depende de un cambio.
- La propagación suma las varianzas.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C19](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md):**
- Ejercicio 8. Un compañero propaga una suma `x + y` sumando los errores relativos.
- python programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/laboratorio_propagacion.py
- 🎯 **Por qué importa:** Con los datos de la Tierra redondeados a tres cifras (semieje `1,50 × 10⁸ km` y período `365 d`), la rapidez orbital sale `29,89 km/s`. La NASA publica 29,78 km/s.

📘 **Dónde se aprende** (5 clases): [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B44-C12 · Calibración con bias](../programa/clases/B44/B44-C12-calibracion-con-bias/CLASE.md); [B83-C12 · Model-Based Systems Engineering](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md); [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md); [B131-C01 · Actividades de medición astronómica para el aula](../programa/clases/B131/B131-C01-actividades-de-medicion-astronomica-para-el-aula/CLASE.md).

### Propagación de errores

- La propagación de errores calcula cómo `σθ` se transmite a `h` (a primer orden, con derivadas).
- La propagación de errores suma las varianzas relativas.
- La propagación de errores traslada la incertidumbre de las entradas a la salida.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

🎯 **Por qué importa (clase B04-C20):** Las distancias a las estrellas más cercanas se obtienen con un triángulo (el paralaje de C07): la base es la órbita de la Tierra y el ángulo es lo que cambia la dirección de la estrella.

📘 **Dónde se aprende** (5 clases): [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md); [B34-C04 · Ondas y oscilaciones coronales como sismología solar](../programa/clases/B34/B34-C04-ondas-y-oscilaciones-coronales-como-sismologia-solar/CLASE.md); [B45-C09 · Calibración de respuesta instrumental](../programa/clases/B45/B45-C09-calibracion-de-respuesta-instrumental/CLASE.md); [B58-C03 · Composición de asteroides](../programa/clases/B58/B58-C03-composicion-de-asteroides/CLASE.md); [B97-C04 · Visión estereoscópica](../programa/clases/B97/B97-C04-vision-estereoscopica/CLASE.md).

### Propagación de incertidumbre

- La propagación de incertidumbre estima la incertidumbre de una función a partir de las de sus variables.
- La propagación de incertidumbre traslada la de los datos a la del modelo.

💡 **Cómo se explica en la clase [B09-C16](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md):**
- La evidencia es la tabla de sensibilidades con propagación de incertidumbre del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *tabla de sensibilidades con propagación de incertidumbre*: parciales de `L`, derivada mixta, propagación lineal y Monte Carlo para dos pares de incertidumbres (sintéticas), y el hessiano del potencial Tierra–Luna en `x*`.
- 🎯 **Por qué importa:** La luminosidad de una estrella calculada con su radio y su temperatura tiene una incertidumbre que viene de las dos. ¿Cuál pesa más?

📘 **Dónde se aprende** (2 clases): [B09-C16 · Derivadas parciales](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md); [B65-C05 · Inversión geofísica conjunta: validación de modelos interiores](../programa/clases/B65/B65-C05-inversion-geofisica-conjunta-validacion-de-modelos-interiores/CLASE.md).

### Propagación de primer orden

- La propagación de primer orden (método delta) aproxima la dispersión de una función con su derivada.

💡 **Cómo se explica en la clase [B59-C02](../programa/clases/B59/B59-C02-prospeccion-de-hielo-lunar/CLASE.md):**
- El script [prospeccion.py](prospeccion.py) calcula la masa proyectada, propaga la incertidumbre a primer orden y por Monte Carlo (comprueba que el primer orden subestima y que la mediana queda a menos de 5 % del cociente central) y evalúa un depósito hipotético.
- 🎯 **Por qué importa:** Un recurso no se planifica con un valor central sino con un rango. La decisión central: ¿cuánto regolito hay que procesar si la abundancia es 2,7 % en vez de 5,6 %?

📘 **Dónde se aprende** (1 clase): [B59-C02 · Prospección de hielo lunar](../programa/clases/B59/B59-C02-prospeccion-de-hielo-lunar/CLASE.md).

### Propagación de ruido

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C22](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md):**
- El zonal reproduce el frente casi sin error pero propaga 1,75 veces más ruido; el modal propaga menos ruido pero deja `10,5 %` de truncado.
- *Descripción textual:* ambos reconstructores invierten el mismo operador de pendientes; el modal restringe la solución y propaga menos ruido pero trunca.
- 🎯 **Por qué importa:** El reconstructor decide qué parte del frente se recupera y cuánto ruido se propaga. La decisión central: ¿zonal o modal, y con cuántos modos?

📘 **Dónde se aprende** (1 clase): [B42-C22 · Reconstructores de frente de onda: zonal y modal](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md).

### Propagación lineal

- La propagación lineal es `σ_f = |f'| σ_x`.
- La propagación lineal usa derivadas parciales.
- La propagación lineal usa derivadas.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B29-C10](../programa/clases/B29/B29-C10-masas-y-radios-planetarios/CLASE.md):**
- Con `M = 5 ± 1 M_⊕` y `R = 1,5 ± 0,1 R_⊕`: `ρ = 8,141 g/cc`; propagación lineal `σ_ρ = 2,303 g/cc` (28,3 %);
- *Descripción textual:* la masa y el radio con sus errores dan la densidad; la propagación lineal y el Monte Carlo se comparan y coinciden solo si los errores son pequeños.
- ⚠️ **Error frecuente:** Aplicar la propagación lineal con errores grandes. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una densidad con 28 % de incertidumbre no distingue una roca de un mundo con agua. Saber de qué medida depende el error orienta la inversión de observación.

📘 **Dónde se aprende** (5 clases): [B29-C10 · Masas y radios planetarios](../programa/clases/B29/B29-C10-masas-y-radios-planetarios/CLASE.md); [B33-C02 · Modelos de propagación de CME](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md); [B53-C19 · Incertidumbre en mapas planetarios](../programa/clases/B53/B53-C19-incertidumbre-en-mapas-planetarios/CLASE.md); [B58-C08 · Propagación de incertidumbre orbital](../programa/clases/B58/B58-C08-propagacion-de-incertidumbre-orbital/CLASE.md); [B77-C13 · Inyección y dispersión orbital](../programa/clases/B77/B77-C13-inyeccion-y-dispersion-orbital/CLASE.md).

### Propagación lineal de covarianza

- La propagación lineal de covarianza es `C_x = J C_p Jᵀ` (C10 introdujo la covarianza).

🎯 **Por qué importa (clase B10-C19):** Una estación mide la distancia, el azimut y la elevación de un objeto con incertidumbres. Para decir dónde está en coordenadas cartesianas y cuánta incertidumbre tiene esa posición, hay que transformar los números y sus errores.

📘 **Dónde se aprende** (1 clase): [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md).

### Propagación lineal de la covarianza

- La propagación lineal de la covarianza es `P(t) = Φ P₀ Φᵀ`.

💡 **Cómo se explica en la clase [B74-C12](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md):**
- *Descripción textual:* la misma covarianza inicial se propaga de tres maneras y se comparan las desviaciones y la fracción de muestras que queda dentro del elipsoide lineal.
- Ejercicio 9 · transferencia. Transferencia. Una agencia reporta un riesgo de conjunción con una covarianza lineal tras 30 días de propagación.
- 🎯 **Por qué importa:** Una predicción de dónde estará un satélite dentro de semanas necesita su incertidumbre, y esa incertidumbre se vuelve curva. La decisión central: ¿cuándo basta la covarianza lineal y cuándo hay que propagar la distribución completa?

📘 **Dónde se aprende** (1 clase): [B74-C12 · Propagación de incertidumbre — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Propagador

- Un propagador calcula el estado en un instante.

💡 **Cómo se explica en la clase [B71-C20](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md):**
- El error de T5 está dominado por el RK4, no por el propagador analítico.
- Con 30 órbitas sintéticas (semilla 20, `e ≤ 0,7`, `t` entre `−1,2 T` y `1,2 T`), el propagador reproduce el estado inicial con `0e+00 m`, vuelve tras un período con `8.2e-08 m`, conserva `h` y `ε` con `3e-15` e ida y vuelta con `3.4e-08 m`, y difiere de un RK4 independiente en `2.0e-05 m` y `2.7e-09 m/s`.
- 🎯 **Por qué importa:** Un propagador que «parece funcionar» puede tener un error de tiempo que ningún invariante detecta. La decisión central: ¿qué pruebas, con qué tolerancias y contra qué referencia independiente demuestran que el propagador es correcto?

📘 **Dónde se aprende** (1 clase): [B71-C20 · Propagador kepleriano verificable](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md).

### Propagador secular

- El propagador secular avanza elementos medios con tasas de variación lineal.

💡 **Cómo se explica en la clase [B72-C20](../programa/clases/B72/B72-C20-comparacion-de-propagadores-de-fidelidad-distinta/CLASE.md):**
- Un propagador secular exige elementos medios.
- Explicar por qué un propagador secular alimentado con elementos osculadores puede ser peor de lo esperado.
- ⚠️ **Error frecuente:** Creer que un propagador secular alimentado con osculadores es fiel. Se corrige con 8.3.
- 🎯 **Por qué importa:** La fidelidad cuesta cálculo y datos: un propagador analítico es instantáneo pero erra por miles de kilómetros en días; uno numérico con muchas fuerzas es lento. La decisión central: ¿qué propagador basta para una tarea, según el horizonte de predicción y el error aceptable?

📘 **Dónde se aprende** (1 clase): [B72-C20 · Comparación de propagadores de fidelidad distinta](../programa/clases/B72/B72-C20-comparacion-de-propagadores-de-fidelidad-distinta/CLASE.md).

### Propagar

- El conjunto ponderado aproxima la distribución del estado. Propagar es avanzar cada partícula con el modelo, incluida su aleatoriedad.
- La región en banana es la forma curva que adopta la incertidumbre en coordenadas cartesianas cuando es grande. Propagar es llevar las muestras o la covarianza a un instante posterior.

💡 **Cómo se explica en la clase [B15-C18](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md):**
- P["Partículas {xᵢ, wᵢ}"] --> A["Propagar:<br/>x = F x + ruido"]
- Paso 1 · Datos (sintéticos). Posiciones de cuatro partículas tras propagar: `98; 100; 103; 106` m, pesos `0,25` cada una.
- 🎯 **Por qué importa:** Un sensor mide la distancia oblicua a un objeto que pasa junto a él. Cuando el objeto está justo frente al sensor, un pequeño cambio de posición casi no cambia la distancia: la medida no distingue bien un lado del otro, y la incertidumbre de la posición deja de ser una campana.

📘 **Dónde se aprende** (2 clases): [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md); [B118-C08 · Propagación de incertidumbre en conjunciones](../programa/clases/B118/B118-C08-propagacion-de-incertidumbre-en-conjunciones/CLASE.md).

### Propelente

- El propelente es la masa que se expulsa para impulsar.

💡 **Cómo se explica en la clase [B59-C01](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md):**
- Con `v_e = Isp·g₀` (`g₀ = 9,806 65 m/s²`, exacta, S1) la masa de propelente es `m_p = m_f (e^{Δv/v_e} − 1)`.
- El propelente es muy sensible al impulso específico: con `Isp × 0,9` crece `+20,1 %` y con `Isp × 1,1` baja `−14,6 %`.
- ⚠️ **Error frecuente:** Confundir masa seca con masa final con carga. Se corrige con la sección 8.1: `m_f` incluye todo lo que no es propelente.
- 🎯 **Por qué importa:** Cada kilogramo que se lanza arrastra consigo más propelente para lanzarlo. La decisión central: ¿cuánta masa de planta de producción compensa el oxidante que dejas de llevar?

📘 **Dónde se aprende** (1 clase): [B59-C01 · Concepto de utilización de recursos in situ](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md).

### Propergol

- Un propergol es combustible más oxidante.
- El propergol es combustible más oxidante.

💡 **Cómo se explica en la clase [B119-C25](../programa/clases/B119/B119-C25-derecho-y-marcos-de-recursos-espaciales/CLASE.md):**
- Con estructura del 10 % del propergol, el propergol es `1582 kg` y la masa inicial `2740 kg`.
- Si el propergol se obtiene en el espacio, el ahorro es `3.95 M u.m.`, es decir `2500 u.m./kg` de propergol: es el precio máximo del propergol en el depósito.
- 🎯 **Por qué importa:** B119 trata los tratados en general (C01, C05) y ninguna clase enseña los marcos de recursos ni el razonamiento económico que los motiva. La gobernanza se desarrolla en C36 y los aspectos técnicos en B59.

📘 **Dónde se aprende** (2 clases): [B119-C23 · Protección ambiental de las actividades de lanzamiento](../programa/clases/B119/B119-C23-proteccion-ambiental-de-las-actividades-de-lanzamiento/CLASE.md); [B119-C25 · Derecho y marcos de recursos espaciales](../programa/clases/B119/B119-C25-derecho-y-marcos-de-recursos-espaciales/CLASE.md).

### Propia

- Es propia si el grado del numerador no supera al del denominador.

🎯 **Por qué importa (clase B16-C05):** Un ingeniero que diseña el control de actitud de un telescopio revisa decenas de variantes de ganancias.

📘 **Dónde se aprende** (1 clase): [B16-C05 · Funciones de transferencia](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md).

### Propiedad

- Una propiedad es una relación que debe cumplirse siempre (por ejemplo, duplicar el radio multiplica el volumen por 8).
- Una propiedad es una ley que se verifica con muchas entradas.
- Interfaz: conjunto de operaciones por tipo de dispositivo. Propiedad: valor expuesto por un driver.

💡 **Cómo se explica en la clase [B07-C17](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md):**
- Para el volumen: caso analítico (radio 1), borde (radio 0 da 0) y propiedad de escala (duplicar el radio multiplica el volumen por 8), parametrizada con cuatro radios (0,5; 1; 6371; 0,001).
- Solo las pruebas de escala detectan el error: al introducirlo a propósito, 14 pruebas pasan y 4 fallan (las cuatro de la propiedad de escala).
- 🎯 **Por qué importa:** Una función matemática puede dar el resultado correcto en el único caso que probaste y estar mal en los demás. Y es fácil escribir una prueba que no puede fallar: la que compara la función contra sí misma o contra un caso donde el error se esconde.

📘 **Dónde se aprende** (3 clases): [B07-C17 · Pruebas de funciones matemáticas](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md); [B48-C21 · Protocolos estándar de control instrumental (ASCOM e INDI)](../programa/clases/B48/B48-C21-protocolos-estandar-de-control-instrumental-ascom-e-indi/CLASE.md); [B88-C36 · Codificación defensiva y estándares de código seguro](../programa/clases/B88/B88-C36-codificacion-defensiva-y-estandares-de-codigo-seguro/CLASE.md).

### Propiedad ciega

- Una propiedad ciega a un defecto es una propiedad que el programa defectuoso sigue cumpliendo.

💡 **Cómo se explica en la clase [B23-C02](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md):**
- La lección: las propiedades detectan errores estructurales y son ciegas a errores de valor (constantes, exponentes pequeños).
- Construir una tabla «defecto × propiedad» e identificar defectos a los que las propiedades son ciegas.

📘 **Dónde se aprende** (1 clase): [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md).

### Propiedad de seguridad

- Sumidero: estado terminal. Propiedad de seguridad: condición que siempre debe cumplirse.
- Cancelación manual: orden del operador que detiene la pasada. Propiedad de seguridad: condición que siempre debe cumplirse.

💡 **Cómo se explica en la clase [B96-C08](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md):**
- Analogía: los estados son como las habitaciones de una casa con puertas de sentido único: la propiedad de seguridad dice que desde cualquier habitación se llega al refugio.
- Verificar la propiedad de seguridad de retorno a SEGURO.
- ⚠️ **Error frecuente:** Olvidar una transición de retorno. Verifica la propiedad de seguridad (8.3)
- 🎯 **Por qué importa:** Un comando válido en un estado puede ser peligroso en otro; y un modo seguro al que no se puede volver es una trampa. La decisión central: ¿qué transiciones existen y se puede siempre llegar al estado seguro?

📘 **Dónde se aprende** (2 clases): [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md); [B96-C24 · Operación remota y automatizada de estaciones](../programa/clases/B96/B96-C24-operacion-remota-y-automatizada-de-estaciones/CLASE.md).

### Propiedad distributiva

- La propiedad distributiva dice `a(b + c) = ab + ac`.

💡 **Cómo se explica en la clase [B03-C13](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md):**
- Reducir términos semejantes y aplicar la propiedad distributiva.
- 🎯 **Por qué importa:** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.

📘 **Dónde se aprende** (1 clase): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md).

### Propiedad foco–directriz

- Todas cumplen la propiedad foco–directriz: hay un punto (el foco) y una recta (la directriz) tales que la distancia de cada punto de la curva al foco es `e` veces su distancia a la directriz;

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- Comprobar la propiedad foco–directriz `|PF| = e·d(P, directriz)`.
- Ejercicio 3 · casi autónomo. Verifica la propiedad foco–directriz para `e = 0,5`, `p = 1,5` y `θ = 60°`.
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.

📘 **Dónde se aprende** (1 clase): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md).

### Propio

- El tiempo acumulado incluye las funciones llamadas; el propio (*tottime*) no.

🎯 **Por qué importa (clase B14-C14):** Una función que calcula la distancia de 200 000 posiciones tarda medio minuto en tu cuaderno, y alguien propone «comprar un servidor». La pregunta motivadora es: ¿es el cálculo lento por su matemática o por cómo lo escribí, y cuánto puedo ganar sin cambiar el resultado?

📘 **Dónde se aprende** (1 clase): [B14-C14 · Vectorización y rendimiento](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md).

### Proporción

- Una proporción es la igualdad de dos razones.

💡 **Cómo se explica en la clase [B03-C02](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md):**
- Resolver una proporción (`a/b = c/d`) para hallar un dato desconocido.
- 🎯 **Por qué importa:** Una cifra aislada como «69 911 km» no dice si Júpiter es grande o pequeño. Una razón sí: Júpiter tiene un radio unas 11 veces el terrestre.

📘 **Dónde se aprende** (1 clase): [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md).

### Propuesta

- El muestreo de importancia estima `E_p[h(X)]` sorteando de otra densidad `q` (la propuesta) y ponderando cada muestra por el peso `w(x) = p(x)/q(x)`: `E_p[h] = ∫ h p dx = ∫ h (p/q) q dx = E_q[h w]`.

💡 **Cómo se explica en la clase [B12-C15](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md):**
- Una buena propuesta tiene masa justo donde está la integranda `h p`; centrarla en el umbral es un punto de partida razonable para colas gaussianas.
- Se comparan dos propuestas distintas: si ambas coinciden dentro de sus errores típicos (como `N(4,1)` y `N(3,1)` aquí: `3,15` y `3,22 × 10⁻⁵`, diferencia `0,07 × 10⁻⁵` frente a errores de `0,02` y `0,03 × 10⁻⁵`, que son consistentes a ~2 errores típicos), la estimación es creíble; si discrepan, algo falla.
- ⚠️ **Error frecuente:** Propuesta con colas livianas. Se corrige con 8.4 y el ejercicio 11.
- 🎯 **Por qué importa:** Los sucesos que más interesan en seguridad espacial —un error de aproximación fuera de límites, una falla simultánea, una colisión— son raros por diseño. Un Monte Carlo simple puede pasar millones de ensayos sin ver un solo acierto y reportar «cero», que no es una estimación útil.

📘 **Dónde se aprende** (1 clase): [B12-C15 · Muestreo de importancia](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md).

### Propulsión de bajo empuje

- La propulsión de bajo empuje acelera poco y mucho tiempo.

💡 **Cómo se explica en la clase [B75-C11](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md):**
- python programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/espiral.py
- 🎯 **Por qué importa:** Un motor de alta `I_sp` ahorra propulsante pero tarda mucho. La decisión central: ¿cuánto delta-v y cuánto tiempo cuesta una espiral y cuándo es válida la fórmula de Edelbaum?

📘 **Dónde se aprende** (1 clase): [B75-C11 · Propulsión de bajo empuje](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md).

### Propulsión nuclear-eléctrica

- La propulsión nuclear-eléctrica usa un reactor como fuente de potencia (concepto).

💡 **Cómo se explica en la clase [B78-C15](../programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/CLASE.md):**
- python programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/nep.py
- 🎯 **Por qué importa:** Subir la velocidad de escape reduce el propelente pero obliga a más potencia, y por tanto a más planta, para el mismo tiempo de empuje. La decisión central: ¿existe un `Isp` que maximice la carga útil y cómo cambia con el Δv y con la masa específica de la planta?

📘 **Dónde se aprende** (1 clase): [B78-C15 · Propulsión nuclear eléctrica conceptual](../programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/CLASE.md).

### Propulsor

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C19](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md):**
- Propulsor: `0,6937 kg/año` para `10 m/s` sobre 150 kg con `Isp = 220 s`; los 12 kg duran `17,30 años`.
- Con tasas ilustrativas, la confiabilidad del sistema a 5 años es `0,6469` (Monte Carlo `0,6472`), baja a `0,8` en `3,24 años`; el propulsor dura `17,3 años` y la potencia llega al 70 % en `14,1 años`.
- 🎯 **Por qué importa:** No sirve duplicar un equipo si otro componente falla antes. La decisión central: ¿qué recurso limita la vida de la misión y qué redundancia vale la pena?

📘 **Dónde se aprende** (1 clase): [B47-C19 · Mantenimiento y vida útil](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md).

### Propulsor solar térmico

- El propulsor solar térmico expande el gas calentado.

💡 **Cómo se explica en la clase [B78-C13](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md):**
- La evidencia es la ficha de un propulsor solar térmico del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de un propulsor solar térmico*: potencia, caudal, escape, empuje, efecto de la temperatura, contraste con un eléctrico y qué es consultado e ilustrativo.
- 🎯 **Por qué importa:** La energía llega por la óptica y el propelente solo la transporta; el escape depende de la temperatura que resistan los materiales y de la masa molar. La decisión central: ¿qué empuje e `Isp` da un colector de área dada y cómo se compara con un propulsor eléctrico alimentado con la misma potencia?

📘 **Dónde se aprende** (1 clase): [B78-C13 · Propulsión solar térmica](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md).

### Protección, detección y recuperación

- Las tres capacidades de resiliencia de NIST SP 800-193 son protección, detección y recuperación.

💡 **Cómo se explica en la clase [B88-C13](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md):**
- Relacionar el diseño con protección, detección y recuperación.
- 🎯 **Por qué importa:** Una actualización fallida en órbita no se arregla con un cable. La decisión central: ¿qué comprobaciones aceptan solo la imagen correcta y qué mecanismo vuelve a una versión conocida si la nueva no arranca?

📘 **Dónde se aprende** (1 clase): [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md).

### Protección planetaria

- La protección planetaria son las normas para evitar contaminar otros mundos (COSPAR, S1).
- Biocarga: número de microorganismos viables sobre un objeto. Protección planetaria: control de la contaminación hacia adelante (de la Tierra a otro cuerpo) y hacia atrás.

💡 **Cómo se explica en la clase [B59-C17](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md):**
- Situar el análisis en el contexto de la protección planetaria.
- 🎯 **Por qué importa:** Sin atmósfera, la eyecta viaja lejos y sin frenar. La decisión central: ¿a qué distancia de una zona sensible, como una sombra permanente, hay que operar para que la eyecta no la alcance?

📘 **Dónde se aprende** (2 clases): [B59-C17 · Impacto ambiental extraterrestre](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md); [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md).

### Protocolo

- Un protocolo es la descripción previa de cómo se medirá: qué, cuándo, con qué instrumento, cuántas veces y qué se descarta.
- El protocolo es la regla comunitaria sobre cuándo, cómo y quién transmite o cuenta algo.
- El protocolo es la regla comunitaria sobre compartir un saber.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C20](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md):**
- El protocolo dice cuántas lecturas (al menos 5 a 10), cada cuánto, con qué instrumento, qué incertidumbre tipo B asignas (regla, vertical, tiempo) y cuándo se descarta una lectura.
- H --> K["Criterio de refutación y protocolo (C07, C18)"]
- 🎯 **Por qué importa:** Entender el método no es lo mismo que aplicarlo. Cuando mides de verdad, aparecen problemas que los ejercicios no tienen: el cielo se nubla, el palo no está del todo vertical, la regla se mueve, los datos no coinciden con lo que predijiste.

📘 **Dónde se aprende** (5 clases): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md); [B48-C21 · Protocolos estándar de control instrumental (ASCOM e INDI)](../programa/clases/B48/B48-C21-protocolos-estandar-de-control-instrumental-ascom-e-indi/CLASE.md); [B133-C02 · Narrativas orales y transmisión del saber del cielo](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md); [B133-C03 · Colaboración con comunidades en investigación y educación](../programa/clases/B133/B133-C03-colaboracion-con-comunidades-en-investigacion-y-educacion/CLASE.md); [B133-C04 · Riesgos de apropiación cultural en la divulgación](../programa/clases/B133/B133-C04-riesgos-de-apropiacion-cultural-en-la-divulgacion/CLASE.md).

### Protocolo de búsqueda

- Un protocolo de búsqueda es el documento que reúne pregunta, fuentes, consultas, criterios y fechas.

💡 **Cómo se explica en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- La evidencia es la hoja de protocolo de búsqueda del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora la *hoja de protocolo de búsqueda* (sección 20) para una pregunta tuya de astronomía: pregunta, términos con sinónimos, fuentes, consultas con fecha, criterios operativos, flujo con conteos que cuadren, motivos de exclusión y tres referencias completas.
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.

📘 **Dónde se aprende** (1 clase): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md).

### Protocolo de etiquetado

- Un protocolo de etiquetado es el documento que define cada clase, con ejemplos y reglas para los casos ambiguos.

💡 **Cómo se explica en la clase [B17-C10](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md):**
- A["Objetos<br/>con identificador único"] --> B["Protocolo de etiquetado<br/>(clases, ambiguos)"]
- Redactar un protocolo de etiquetado con clases definidas, casos ambiguos y una categoría «incierto».
- 🎯 **Por qué importa:** Se quiere entrenar un modelo que distinga galaxias espirales de elípticas. Hay un millón de imágenes y nadie las ha etiquetado.

📘 **Dónde se aprende** (1 clase): [B17-C10 · Conjuntos de datos etiquetados para aprendizaje supervisado](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md).

### Protocolo de seguridad de enlace de datos (SDLS)

- El protocolo de seguridad de enlace de datos (SDLS) de la CCSDS protege tramas con autenticación y/o cifrado.

💡 **Cómo se explica en la clase [B89-C25](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md):**
- Explicar qué servicios da el protocolo de seguridad de enlace de datos según la CCSDS 355.0-B-2.
- 🎯 **Por qué importa:** Los comandos son la superficie más sensible de una misión; sin autenticación y sin protección contra repetición, una trama capturada podría reutilizarse, y un CRC solo detecta errores, no ataques (C12). La decisión central: ¿cómo garantizar que una trama es auténtica, íntegra y no repetida, y cuánto cuesta en sobrecarga?

📘 **Dónde se aprende** (1 clase): [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md).

### Protocolo preregistrado

- Un protocolo preregistrado es el plan de análisis fechado y fijado antes de ver los datos.

💡 **Cómo se explica en la clase [B14-C23](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md):**
- La evidencia es el protocolo preregistrado con criterios de decisión del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Entrega un protocolo preregistrado con criterios de decisión para un análisis sintético propio: hipótesis, prueba, umbral, exclusiones, versión de los datos, huella del protocolo, simulación de la tasa de falsos positivos con tu diseño, detección de desviaciones y declaración de lo que el preregistro no cubre.
- 🎯 **Por qué importa:** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.

📘 **Dónde se aprende** (1 clase): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md).

### Protocuenca

- Una protocuenca tiene un pico más un anillo interno y otro intervalo.

🎯 **Por qué importa (clase B61-C07):** Las cuencas dejan huella en la corteza entera. La decisión central: ¿cómo se espacian los anillos, qué proyectil implica una cuenca y cuándo excava hasta el manto?

📘 **Dónde se aprende** (1 clase): [B61-C07 · Cuencas multianillo y grandes impactos](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md).

### Protoestrella

- Una protoestrella es un objeto central del colapso que aún no obtiene su energía de la fusión de hidrógeno y brilla por contracción y acreción.

💡 **Cómo se explica en la clase [B24-C02](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md):**
- Es lo que dura una estrella que solo se contrae, mucho más que `t_ff` (C01): la protoestrella se queda mucho tiempo en la fase de contracción.
- Paso 4 · Sentido. Por acreción la protoestrella puede ser casi ocho veces más luminosa que el Sol aunque no fusione nada.
- 🎯 **Por qué importa:** Una protoestrella brilla, pero no por el motor que alimenta al Sol. Para saber de dónde sale su energía, cuánto tiempo puede brillar así y cómo distinguirla de una estrella ya estable hay que seguir la energía gravitatoria.

📘 **Dónde se aprende** (1 clase): [B24-C02 · Formación de protoestrellas](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md).

### Protón

- Un protón es el núcleo del hidrógeno (`p`); una partícula alfa es el núcleo de helio-4.

💡 **Cómo se explica en la clase [B24-C06](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md):**
- En términos de masas: `Q = [4 m_p + 4 m_e − (m_α + 2 m_e)] c²`, con `m_p` la masa del protón, `m_α` la de la partícula alfa y `m_e` la del electrón (S1).
- Cuatro protones pesan algo más que un núcleo de helio con sus dos electrones asociados; la diferencia (0,7 %) desaparece como energía.
- ⚠️ **Error frecuente:** Confundir masa de protones con masa de átomos. Se corrige con 8.1 y el ejercicio 1.
- 🎯 **Por qué importa:** Una estrella como el Sol brilla desde hace miles de millones de años; ninguna fuente química ni gravitatoria alcanza (C02). La fusión nuclear sí.

📘 **Dónde se aprende** (1 clase): [B24-C06 · Fusión de hidrógeno](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md).

### Protones

- Tiene un núcleo, minúsculo y denso, formado por protones (carga positiva) y neutrones (sin carga), y a su alrededor electrones (carga negativa).

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Un átomo de hidrógeno ordinario tiene un protón y un electrón; el helio, dos protones (`Z = 2`); el carbono, seis.
- La masa está casi toda en el núcleo: un protón pesa unas 1836 veces más que un electrón (S1).
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.

📘 **Dónde se aprende** (1 clase): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md).

### Protones libres

- Los protones libres son el blanco principal en agua.

💡 **Cómo se explica en la clase [B27-C18](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md):**
- Un kilotón de agua tiene `6,6913 × 10³¹` protones libres.
- protones libres en 1 kt de agua = 6.6913e+31 ; sucesos esperados = 145.4 (sigma = 1e-41 cm2 ilustrativa)
- 🎯 **Por qué importa:** Los neutrinos de una supernova galáctica serían una señal de cientos de sucesos en unos segundos, mensajera del interior de la estrella. La decisión central: ¿cuántos neutrinos llegan, qué retraso produce su masa y cómo se calcula sin perder precisión?

📘 **Dónde se aprende** (1 clase): [B27-C18 · Neutrinos de supernova](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md).

### Prototipo

- Prototipo: versión temprana para explorar el diseño.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- Por propósito: exploración (prototipo), diseño (EM), calificación (QM), vuelo (FM).
- Distinguir prototipo, modelo de ingeniería, modelo de calificación, protovuelo y unidad de vuelo.
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?

📘 **Dónde se aprende** (1 clase): [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### Prototipo pasabajos

- El prototipo pasabajos `g_k = 2 sin((2k−1)π/2n)`.

🎯 **Por qué importa (clase B49-C10):** Más orden rechaza más, pero también pierde más señal. La decisión central: ¿qué orden y qué ancho de banda dan el rechazo de imagen necesario con una pérdida aceptable?

📘 **Dónde se aprende** (1 clase): [B49-C10 · Filtros de radiofrecuencia pasabanda y rechazo de banda imagen](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md).

### Protovuelo

- Calificación: demostración del diseño en niveles extremos con una unidad. Protovuelo: calificación aplicada a la unidad de vuelo.
- Modelo de calificación (QM): unidad idéntica a la de vuelo para calificar. Protovuelo: calificación aplicada a la unidad de vuelo.

💡 **Cómo se explica en la clase [B90-C19](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md):**
- P["Protovuelo<br/>ambas preguntas<br/>en la unidad de vuelo"] --> A
- *Descripción textual:* la calificación responde si el diseño resiste, con una unidad de calificación; la aceptación responde si cada unidad de vuelo está bien hecha, con niveles menores; el protovuelo combina ambas en la unidad de vuelo; todos terminan en un paquete de datos y una decisión.
- 🎯 **Por qué importa:** Un ensayo de aceptación demasiado severo gasta vida útil; uno demasiado suave deja pasar defectos. La decisión central: ¿qué nivel y duración demuestran la mano de obra sin dañar la unidad, y con qué evidencia se acepta?

📘 **Dónde se aprende** (2 clases): [B90-C19 · Aceptación de unidades de vuelo](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md); [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### Proveedor y consumidor

- ICD: documento de control de interfaces. Proveedor y consumidor: quien entrega y quien recibe en la interfaz.

💡 **Cómo se explica en la clase [B90-C05](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md):**
- *Descripción textual:* el proveedor declara su rango de salida, el consumidor su rango de entrada y su corriente; el ICD los cruza y la verificación produce hallazgos cuando el rango no cabe o el margen es insuficiente.
- Paso 1 · Rangos. Proveedor 4,80–5,20 V; consumidor 4,90–5,50 V.
- 🎯 **Por qué importa:** La mayoría de los problemas de integración nacen en interfaces mal definidas: un equipo entrega 4,8 V y el otro necesita 4,9 V; un agujero admite 0,25 mm de desalineación y la pila de tolerancias llega a 0,40 mm. La decisión central: ¿las interfaces del ICD son compatibles antes de unir el hardware?

📘 **Dónde se aprende** (1 clase): [B90-C05 · Documentación de interfaces](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md).

### Provincia

- La provincia es una región volcánica con origen común.

💡 **Cómo se explica en la clase [B70-C04](../programa/clases/B70/B70-C04-vulcanismo-marciano-provincias-edades-y-evolucion/CLASE.md):**
- El ejemplo conductor son tres provincias sintéticas: A (`40 000 km²`, edad verdadera `3,6 Gyr`, `N = 63` cráteres ≥ 1 km), B (`25 000 km²`, `1,5 Gyr`, `N = 20`) y C (`10 000 km²`, `0,3 Gyr`, `N = 1`).
- La evidencia es la ficha de la edad de una provincia del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un conteo de cráteres es un número entero y ruidoso. La decisión central: ¿qué edad y qué incertidumbre le corresponden a una provincia dada su área y su conteo?

📘 **Dónde se aprende** (1 clase): [B70-C04 · Vulcanismo marciano: provincias, edades y evolución](../programa/clases/B70/B70-C04-vulcanismo-marciano-provincias-edades-y-evolucion/CLASE.md).

### Proxy

- Un proxy es una magnitud medible que sustituye a otra que no se puede medir (el diámetro en píxeles como sustituto del diámetro angular).

💡 **Cómo se explica en la clase [B01-C06](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md):**
- Medible: existe una magnitud con unidad que responde la pregunta, o un proxy justificado.
- Medible: con un proxy (fotos con ajustes fijos).
- 🎯 **Por qué importa:** «¿Hay vida en otros planetas?» es una pregunta legítima y apasionante, pero nadie puede responderla con un cuaderno y una cámara de teléfono. «¿Cambia el tamaño aparente de la Luna a lo largo de un mes?» sí puede responderse con una cámara y un trípode, y su respuesta enseña algo real sobre la órbita lunar.

📘 **Dónde se aprende** (1 clase): [B01-C06 · Preguntas investigables en astronomía](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md).

### Proxy de Dst

- El proxy de Dst promedia la perturbación de estaciones de latitud baja corregida por `cos λ`.

💡 **Cómo se explica en la clase [B30-C23](../programa/clases/B30/B30-C23-indices-geomagneticos-kp-y-dst/CLASE.md):**
- El proxy no tiene sesgo y su incertidumbre (≈1,6 nT) no depende del nivel de la perturbación; con más estaciones bajaría como `1/√N`.
- *Descripción textual:* trece valores `K` promediados dan el Kp y su etiqueta; cuatro perturbaciones corregidas por latitud dan el proxy de Dst y su incertidumbre.
- 🎯 **Por qué importa:** Kp y Dst son los índices con que se habla de tormentas. Saber cómo se construyen y con qué incertidumbre ayuda a leer un registro.

📘 **Dónde se aprende** (1 clase): [B30-C23 · Índices geomagnéticos Kp y Dst](../programa/clases/B30/B30-C23-indices-geomagneticos-kp-y-dst/CLASE.md).

### Proyección

- La proyección de `w` sobre una dirección unitaria `ê` es el número `w · ê`.
- Una proyección es la integral a lo largo de una línea.
- Una proyección deja un vector sobre un subespacio.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C13](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md):**
- Si `w = (3; 4; 0)` y `ê = (1; 0; 0)`, la proyección es 3: el vector avanza 3 unidades en esa dirección.
- Calcular la proyección de un vector sobre una dirección.
- 🎯 **Por qué importa:** Antes de apuntar un telescopio de una estrella a otra, antes de saber si dos objetos caben en el mismo campo de visión, antes de decidir si un planeta está demasiado cerca del Sol para observarlo, hay que saber cuántos grados los separan en el cielo.

📘 **Dónde se aprende** (5 clases): [B04-C13 · Producto escalar y ángulo entre vectores](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md); [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md); [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md); [B34-C06 · Tomografía coronal](../programa/clases/B34/B34-C06-tomografia-coronal/CLASE.md); [B111-C04 · Conciencia situacional en operaciones de vuelo](../programa/clases/B111/B111-C04-conciencia-situacional-en-operaciones-de-vuelo/CLASE.md).

### Proyección cartográfica

- Una proyección cartográfica es una regla que asigna a cada punto `(φ, λ)` de la esfera un punto `(x, y)` del plano.

💡 **Cómo se explica en la clase [B04-C17](../programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/CLASE.md):**
- python programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/proyecciones.py
- 🎯 **Por qué importa:** Casi todo lo que ves del espacio, de la Tierra o de otro cuerpo, llega en forma de mapa: la superficie de un planeta, el cielo entero, la huella de un satélite. Y un mapa es una proyección.

📘 **Dónde se aprende** (1 clase): [B04-C17 · Proyecciones cartográficas elementales](../programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/CLASE.md).

### Proyección con orificio

- La proyección con orificio forma una imagen del Sol sobre una pantalla sin mirar el Sol (S1).

💡 **Cómo se explica en la clase [B08-C16](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md):**
- Por esta razón esta clase no te pide usar el Sol con telescopio ni binoculares salvo bajo la supervisión de una persona con experiencia; la actividad central es la proyección con orificio.
- B -->|"Sin equipo"| C["Proyección con orificio<br/>(de espaldas al Sol)"]
- 🎯 **Por qué importa:** Una persona que mira un eclipse parcial con gafas falsas, o enfoca el Sol con un telescopio sin filtro frontal, puede quedar con una lesión permanente. La pregunta motivadora: ¿cómo observo el Sol sin dañarme y sin dañar a otros?

📘 **Dónde se aprende** (1 clase): [B08-C16 · Observación solar con filtros certificados](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md).

### Proyección del centro de masas

- La proyección del centro de masas es el punto en que la vertical local, desde el centro de masas, corta el plano de apoyo.

💡 **Cómo se explica en la clase [B102-C05](../programa/clases/B102/B102-C05-distribucion-de-cargas-y-estabilidad-ante-vuelco/CLASE.md):**
- Con el cuerpo inclinado `θ` y `φ`, la proyección del centro de masas cae en `p_x = x_c − h tan θ/cos φ` y `p_y = −h tan φ`.
- *Descripción textual:* la inclinación y la geometría fijan dónde cae la proyección del centro de masas; la distancia al borde es el margen y el vuelco ocurre cuando es nulo; además la inclinación reparte las cargas entre ejes y lados.
- 🎯 **Por qué importa:** Las leyes de operación de un rover fijan un máximo de inclinación. La decisión central: ¿cuánto margen queda frente al vuelco en una pendiente dada, y qué parte de ese margen depende de la gravedad?

📘 **Dónde se aprende** (1 clase): [B102-C05 · Distribución de cargas y estabilidad ante vuelco](../programa/clases/B102/B102-C05-distribucion-de-cargas-y-estabilidad-ante-vuelco/CLASE.md).

### Proyección estereográfica

- La proyección estereográfica es conforme: conserva ángulos y cambia la escala con la latitud.

💡 **Cómo se explica en la clase [B53-C05](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md):**
- En la proyección estereográfica polar sur `ρ = 2R tan((90° − |φ|)/2)` y la escala radial es `k = 2/(1 + sin|φ|)`.
- Ejercicio 7 · autónomo. ¿Por qué la proyección estereográfica no conserva áreas?
- 🎯 **Por qué importa:** Dos productos en marcos distintos no se superponen sin corregir. La decisión central: ¿en qué marco, con qué figura y con qué convención está cada coordenada, y cuánto se desplaza un punto al cambiar de marco?

📘 **Dónde se aprende** (1 clase): [B53-C05 · Sistemas de coordenadas lunares](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md).

### Proyección gnomónica

- La proyección gnomónica (tangente) lleva el cielo a un plano tangente en un punto.

💡 **Cómo se explica en la clase [B58-C06](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md):**
- Aplicar y invertir la proyección gnomónica.
- 🎯 **Por qué importa:** Una órbita no puede ser mejor que sus posiciones: un error de décimas de segundo de arco se amplifica al propagar. La decisión central: ¿con qué exactitud puedo asignar coordenadas a un objeto en una imagen y qué la limita?

📘 **Dónde se aprende** (1 clase): [B58-C06 · Astrometría de objetos menores](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md).

### Proyección ortogonal

- La proyección ortogonal de `v` sobre un subespacio `W` es el vector de `W` más cercano a `v`; la diferencia `v − P v` es ortogonal a `W`.

💡 **Cómo se explica en la clase [B10-C07](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md):**
- El script [minimos_cuadrados.py](minimos_cuadrados.py) genera los datos sintéticos, ajusta por tres métodos, verifica que el residuo es ortogonal, calcula incertidumbres y proyección, y compara normales con QR en un caso mal condicionado.
- 🎯 **Por qué importa:** Una estación mide la distancia a un satélite cada segundo durante diez segundos. Hay once medidas y solo tres parámetros que describir (posición, velocidad y aceleración radiales).

📘 **Dónde se aprende** (1 clase): [B10-C07 · Proyecciones y mínimos cuadrados](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md).

### Proyecto

- Un proyecto es un directorio con un `pyproject.toml`.

💡 **Cómo se explica en la clase [B14-C12](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md):**
- El proyecto del laboratorio declara en `pyproject.toml`: nombre, versión, `requires-python = ">=3.12"` y `dependencies = ["numpy==2.5.4"]`.
- Para un proyecto científico, el bloqueo es el mínimo; el contenedor, cuando el sistema importa.
- 🎯 **Por qué importa:** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.

📘 **Dónde se aprende** (1 clase): [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Prueba

- Una prueba es una comprobación automática de que el programa da la salida esperada para una entrada conocida.
- Una prueba (*test*) es una función que ejecuta código y comprueba el resultado con `assert`. pytest descubre archivos `test_*.py` y funciones `test_*` (S2).
- Una prueba es un código que llama al núcleo con un caso cuya respuesta conoces y falla si no la obtiene.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C01](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md):**
- Una prueba automática usa `assert condición`, que detiene el programa con un error si la condición es falsa.
- Escribir pruebas que cubran el caso típico y los casos borde (lista de un elemento, lista vacía).
- 🎯 **Por qué importa:** En astronomía casi todo resultado pasa por un procedimiento repetible: reducir imágenes, ajustar una órbita, buscar el máximo de una curva de luz. Si no puedes describir el procedimiento con precisión, no puedes ejecutarlo en un computador ni dárselo a otra persona para que lo repita.

📘 **Dónde se aprende** (5 clases): [B07-C01 · Pensamiento algorítmico](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md); [B07-C17 · Pruebas de funciones matemáticas](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md); [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md); [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md); [B90-C01 · Plan de ensamblaje e integración](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md).

### Prueba A/B

- La prueba A/B compara dos mensajes.

💡 **Cómo se explica en la clase [B124-C18](../programa/clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md):**
- *Descripción textual:* las impresiones se reducen etapa a etapa hasta los seguidores; por separado, dos mensajes se comparan con una prueba cuyo tamaño de muestra se verifica por simulación.
- Paso 2 · Prueba. `p_A = 0,10`, `p_B = 0,12`, `n = 3 000` por brazo.
- ⚠️ **Error frecuente:** Detener la prueba al primer p-valor favorable. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Sin medir, la divulgación se evalúa por impresión. La decisión central: ¿cuántas personas hay que observar para saber si un mensaje funciona mejor que otro, y cuánto alcance real tiene una campaña?

📘 **Dónde se aprende** (1 clase): [B124-C18 · Comunicación y divulgación](../programa/clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md).

### Prueba binomial

- La prueba binomial cuenta cuántos ejes caen en una ventana de ancho `2w`; bajo azar la probabilidad de caer en ella es `p0 = 2w/180°`.

💡 **Cómo se explica en la clase [B132-C04](../programa/clases/B132/B132-C04-estadistica-de-orientaciones-en-arqueoastronomia/CLASE.md):**
- *Descripción textual:* los ejes se duplican para la prueba de Rayleigh y se cuentan en una ventana fijada antes para la binomial; ambos resultados se corrigen según cuántas hipótesis se probaron y se reúnen en el informe.
- Aplicar una prueba binomial exacta a una ventana fijada antes de ver los datos.
- 🎯 **Por qué importa:** Si se mira un conjunto de ejes y se busca «algo», casi siempre se encuentra. La decisión central: ¿la agrupación observada supera lo esperable por azar, una vez descontado que se probaron varias hipótesis?

📘 **Dónde se aprende** (1 clase): [B132-C04 · Estadística de orientaciones en arqueoastronomía](../programa/clases/B132/B132-C04-estadistica-de-orientaciones-en-arqueoastronomia/CLASE.md).

### Prueba contrafactual

- La prueba contrafactual pregunta si, sin el hecho, el daño habría ocurrido.

💡 **Cómo se explica en la clase [B123-C02](../programa/clases/B123/B123-C02-causalidad-y-atribucion-juridica-del-dano/CLASE.md):**
- *Descripción textual:* del daño probado se pasa al objeto candidato, se somete a la prueba contrafactual y a la evidencia, y según el lugar se aplica el régimen absoluto o por culpa; con varios Estados implicados se reparte según el artículo IV.
- Aplicar la prueba contrafactual «sin el objeto, ¿habría daño?».
- 🎯 **Por qué importa:** Un daño probado no tiene responsable hasta que se establece qué objeto lo causó y bajo qué régimen. La decisión central: ¿qué objeto, de qué Estado, con qué régimen y con qué reparto?

📘 **Dónde se aprende** (1 clase): [B123-C02 · Causalidad y atribución jurídica del daño](../programa/clases/B123/B123-C02-causalidad-y-atribucion-juridica-del-dano/CLASE.md).

### Prueba de aceptación

- Una prueba de aceptación fija una tolerancia antes de ejecutar.
- Tipo con unidad: valor que lleva su unidad. Prueba de aceptación: verificación de lo entregado frente a lo esperado.

💡 **Cómo se explica en la clase [B71-C20](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md):**
- *Descripción textual:* los elementos se propagan con Kepler; seis pruebas con tolerancias fijadas de antemano decidieron si se acepta; la mutación demuestra que la comparación con un integrador independiente detecta lo que los invariantes no.
- 🎯 **Por qué importa:** Un propagador que «parece funcionar» puede tener un error de tiempo que ningún invariante detecta. La decisión central: ¿qué pruebas, con qué tolerancias y contra qué referencia independiente demuestran que el propagador es correcto?

📘 **Dónde se aprende** (2 clases): [B71-C20 · Propagador kepleriano verificable](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md); [B96-C19 · Lecciones aprendidas operativas](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md).

### Prueba de discriminación

- Una prueba de discriminación comprueba que el instrumento puede distinguir entre las predicciones de la hipótesis y de su alternativa.

💡 **Cómo se explica en la clase [B01-C07](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md):**
- Es la prueba de discriminación de la sección 8.4 a gran escala.
- Ejercicio 12 · integrador. Elabora tu ficha de hipótesis: hipótesis con alcance, hipótesis alternativa, predicción numérica con unidades y fuente de los datos, criterio de refutación, prueba de discriminación con el instrumento que tendrás, y fecha de registro anterior a la medida.
- 🎯 **Por qué importa:** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.

📘 **Dónde se aprende** (1 clase): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md).

### Prueba de extremo a extremo

- Una prueba de extremo a extremo evalúa la cadena completa.
- Prueba de extremo a extremo: prueba de un hilo operativo completo entre elementos e interfaces externas.

💡 **Cómo se explica en la clase [B15-C20](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md):**
- Verificar cada etapa con una cifra y la cadena con una prueba de extremo a extremo.
- 🎯 **Por qué importa:** Detectar y seguir un objeto móvil —un asteroide, un fragmento de basura espacial, un satélite— combina varios problemas: la cámara no apunta exactamente igual en cada imagen, las estrellas fijas saturan la escena, el objeto es débil y la medida es ruidosa.

📘 **Dónde se aprende** (2 clases): [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md); [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### Prueba de Foucault

- La prueba de Foucault coloca una cuchilla en el foco.

💡 **Cómo se explica en la clase [B41-C19](../programa/clases/B41/B41-C19-colimacion-y-prueba-de-enfoque/CLASE.md):**
- Trazar la prueba de Foucault en el centro de curvatura.
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué la prueba de Foucault detecta zonas?
- 🎯 **Por qué importa:** Un buen espejo mal colimado rinde mal. La decisión central: ¿cuánta descolimación y cuánto desenfoque se toleran?

📘 **Dónde se aprende** (2 clases): [B41-C19 · Colimación y prueba de enfoque](../programa/clases/B41/B41-C19-colimacion-y-prueba-de-enfoque/CLASE.md); [B43-C06 · Pruebas de Ronchi y Foucault](../programa/clases/B43/B43-C06-pruebas-de-ronchi-y-foucault/CLASE.md).

### Prueba de frontera

- Una prueba de frontera usa el valor límite.

💡 **Cómo se explica en la clase [B88-C14](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md):**
- Las pruebas de frontera valen su peso en esos dos mutantes.
- De los 9 mutantes de operadores, las 6 pruebas matan los 9 (`100 %`); sin las dos de frontera, la puntuación baja a `77,8 %`.
- 🎯 **Por qué importa:** Una prueba que pasa no prueba nada si pasaría también con el código roto. La decisión central: ¿las pruebas detectan los cambios de comportamiento o solo recorren el código?

📘 **Dónde se aprende** (1 clase): [B88-C14 · Pruebas de software embarcado](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md).

### Prueba de Kalman

- Según la prueba de Kalman, el sistema es controlable si `rango 𝒞 = n` y observable si `rango 𝒪 = n`.

💡 **Cómo se explica en la clase [B16-C13](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md):**
- Aplicar las pruebas de rango de Kalman y la prueba PBH.
- 🎯 **Por qué importa:** Un satélite puede perder actuadores o sensores en vuelo. Antes de diseñar una ley de control conviene saber si el problema tiene solución: ninguna ley, por ingeniosa que sea, mueve un estado que ningún actuador alcanza, ni estima uno que ningún sensor ve.

📘 **Dónde se aprende** (1 clase): [B16-C13 · Observabilidad y controlabilidad](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md).

### Prueba de Kolmogorov–Smirnov (KS)

- La prueba de Kolmogorov–Smirnov (KS) de dos muestras mide `D = máx |F₁(x) − F₂(x)|`, la mayor diferencia entre las distribuciones acumuladas empíricas.

🎯 **Por qué importa (clase B17-C07):** Un modelo se entrena con un catálogo y se despliega sobre otro: otro telescopio, otra época, otro brillo límite. Su exactitud medida en validación cruzada deja de valer, y el modelo no avisa: responde con la misma seguridad.

📘 **Dónde se aprende** (1 clase): [B17-C07 · Validación fuera de distribución](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md).

### Prueba de la relatividad

- Una prueba de la relatividad compara la predicción con la medida y acota la desviación.

💡 **Cómo se explica en la clase [B26-C06](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md):**
- Una prueba con dos satélites Galileo en órbitas excéntricas midió la desviación del corrimiento respecto de la predicción de la relatividad general: `(+0,19 ± 2,48) × 10⁻⁵`, con `1008` días de datos (S3, resumen).
- 🎯 **Por qué importa:** Los relojes de los satélites de navegación van a un ritmo ligeramente distinto de los terrestres, y un maser en una torre ve su frecuencia cambiar con la altura. Todo eso se deduce de la equivalencia entre aceleración y gravedad.

📘 **Dónde se aprende** (1 clase): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md).

### Prueba de la segunda derivada

- La prueba de la segunda derivada: si `f′(x₀) = 0` y `f″(x₀) > 0`, hay mínimo local; si `f″(x₀) < 0`, máximo (S1, §1.4(iii)).

🎯 **Por qué importa (clase B09-C07):** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.

📘 **Dónde se aprende** (1 clase): [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md).

### Prueba de mutación

- La prueba de mutación introduce omisiones para medir si el verificador las detecta.

💡 **Cómo se explica en la clase [B120-C04](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md):**
- *Descripción textual:* el expediente se compara con el esquema (completitud) y consigo mismo (coherencia); la mutación prueba al verificador.
- Probar un verificador con una prueba de mutación.
- 🎯 **Por qué importa:** El expediente regulatorio es un entregable del rol; B90-C05 documenta interfaces, no trámites regulatorios.

📘 **Dónde se aprende** (1 clase): [B120-C04 · Documentación regulatoria de un sistema satelital](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md).

### Prueba de permutaciones

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B34-C07):** Una buena correlación puede ocultar un error de escala. La decisión central: ¿qué métrica detecta cada tipo de discrepancia?

📘 **Dónde se aprende** (1 clase): [B34-C07 · Comparación de modelos coronales con observaciones](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md).

### Prueba de regresión

- Una prueba de regresión vuelve a ejecutar un caso conocido y exige el mismo resultado.
- Una prueba de regresión compara el resultado actual con uno guardado de una versión anterior; detecta cambios, no demuestra corrección.

💡 **Cómo se explica en la clase [B14-C10](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md):**
- Si la referencia estaba mal, la prueba de regresión la defiende.
- Distinguir una prueba de regresión de una prueba de corrección.
- 🎯 **Por qué importa:** Cambias una línea de un propagador orbital «solo para ordenarlo» y el período de una órbita pasa de 5553,624562 s a 5553,627342 s (situación ilustrativa con cifras de esta clase). ¿Es un error o ruido?

📘 **Dónde se aprende** (2 clases): [B11-C20 · Propagador reproducible de trayectoria](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md); [B14-C10 · Pruebas de regresión numérica](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md).

### Prueba de Ronchi

- La prueba de Ronchi coloca una rejilla y se cuentan las bandas.

💡 **Cómo se explica en la clase [B43-C06](../programa/clases/B43/B43-C06-pruebas-de-ronchi-y-foucault/CLASE.md):**
- La evidencia es la ficha de pruebas de Foucault y Ronchi del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de pruebas de Foucault y Ronchi*: lecturas y bandas.
- 🎯 **Por qué importa:** La prueba convierte una desviación de nanómetros en un desplazamiento de milímetros de la cuchilla. La decisión central: ¿en cuánto debe desplazarse la cuchilla para cada zona del paraboloide y cuántas bandas de Ronchi se esperan?

📘 **Dónde se aprende** (1 clase): [B43-C06 · Pruebas de Ronchi y Foucault](../programa/clases/B43/B43-C06-pruebas-de-ronchi-y-foucault/CLASE.md).

### Prueba del parche

- La prueba del parche exige que una malla irregular reproduzca exactamente una solución lineal.

💡 **Cómo se explica en la clase [B84-C12](../programa/clases/B84/B84-C12-analisis-de-elementos-finitos/CLASE.md):**
- La prueba del parche con una malla irregular y área constante da un error nodal máximo `2,2 × 10⁻¹⁹ m`.
- El script [mef_barra.py](mef_barra.py) ensambla y resuelve el modelo con 1 a 32 elementos y ejecuta la prueba del parche (comprueba reacción `= −P`, energía `= ½ P u`, orden entre 1,9 y 2,1 y parche < 1e-12).
- 🎯 **Por qué importa:** Un modelo que da un resultado no es un modelo correcto: la verificación contra una solución conocida es lo que lo convierte en una herramienta. La decisión central: ¿cómo demuestras que un modelo de elementos finitos resuelve bien las ecuaciones que dice resolver?

📘 **Dónde se aprende** (1 clase): [B84-C12 · Análisis de elementos finitos](../programa/clases/B84/B84-C12-analisis-de-elementos-finitos/CLASE.md).

### Prueba KS

- La prueba KS compara dos distribuciones acumuladas con `D = max|F₁ − F₂|`.

💡 **Cómo se explica en la clase [B38-C09](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md):**
- La prueba KS da `D = 0,1140` y `p ≈ 1,1 × 10⁻¹¹³`: se rechaza.
- Una muestra de 20 000 galaxias con los parámetros ajustados frente a la mitad de prueba da `D = 0,0119` y `p = 0,300`.
- 🎯 **Por qué importa:** Una simulación calibrada para coincidir con los datos no queda validada por coincidir con ellos. La decisión central: ¿qué parte del acuerdo es una predicción y qué parte es un ajuste?

📘 **Dónde se aprende** (1 clase): [B38-C09 · Validación de galaxias simuladas frente a observaciones](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md).

### Prueba pareada

- Una prueba pareada compara dos condiciones en las mismas personas.

🎯 **Por qué importa (clase B109-C12):** Sin medir, «esta distribución es mejor» es una opinión. La decisión central: ¿la diferencia entre dos maquetas es mayor que lo que daría el azar, y las personas que la evalúan coinciden entre sí?

📘 **Dónde se aprende** (1 clase): [B109-C12 · Evaluación de factores humanos de maquetas y distribuciones](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md).

### Prueba par–impar

- La prueba par–impar compara eclipses alternos.

💡 **Cómo se explica en la clase [B29-C08](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md):**
- La evidencia es la ficha de una prueba par–impar del ejercicio 12 (sección 20).
- Ejercicio 9 · transferencia. Un compañero dice que si la prueba par–impar no detecta nada, no es una binaria.
- 🎯 **Por qué importa:** Una pequeña fracción de falsos positivos contamina cualquier muestra de planetas. Conocer qué pruebas los detectan, con qué potencia y con qué falsas alarmas, permite diseñar cribados honestos.

📘 **Dónde se aprende** (1 clase): [B29-C08 · Falsos positivos de tránsito](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md).

### Prueba PBH

- La prueba PBH (Popov–Belevitch–Hautus) dice: es controlable si `rango [λI − A, B] = n` para todo autovalor `λ`.

💡 **Cómo se explica en la clase [B16-C13](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md):**
- La prueba PBH localiza el problema: en el autovalor `λ = 0` el rango de `[λI − A, B]` cae por debajo de 6, que corresponde al modo del eje sin actuador.
- El sistema no lineal real, con momento almacenado, puede ser controlable de otras maneras (por ejemplo, usando el acoplamiento giroscópico); la prueba lineal no lo afirma ni lo descarta.
- ⚠️ **Error frecuente:** Concluir sobre el sistema no lineal a partir de la prueba lineal. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Un satélite puede perder actuadores o sensores en vuelo. Antes de diseñar una ley de control conviene saber si el problema tiene solución: ninguna ley, por ingeniosa que sea, mueve un estado que ningún actuador alcanza, ni estima uno que ningún sensor ve.

📘 **Dónde se aprende** (1 clase): [B16-C13 · Observabilidad y controlabilidad](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md).

### Prueba sintética

- Una prueba sintética genera datos desde una verdad conocida, los invierte y compara.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Diseñar una prueba sintética con verdad, modelo generador, ruido y métrica declarados.
- Redactar una declaración de límites de una prueba sintética.
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Prueba z de dos proporciones

- La prueba z de dos proporciones compara `p_A` y `p_B` con una varianza agrupada.

💡 **Cómo se explica en la clase [B124-C18](../programa/clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md):**
- Calcular el tamaño de muestra de una prueba de dos proporciones.
- El script [embudo_y_prueba_ab.py](embudo_y_prueba_ab.py) calcula un embudo, los cuantiles normales por bisección, el tamaño de muestra de una prueba de dos proporciones y verifica potencia y nivel con 4 000 experimentos (comprueba cuantiles a 1e-5, potencia a 0,03 y nivel a 0,015).
- 🎯 **Por qué importa:** Sin medir, la divulgación se evalúa por impresión. La decisión central: ¿cuántas personas hay que observar para saber si un mensaje funciona mejor que otro, y cuánto alcance real tiene una campaña?

📘 **Dónde se aprende** (1 clase): [B124-C18 · Comunicación y divulgación](../programa/clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md).

### Pruebas múltiples

- En pruebas múltiples, la probabilidad de al menos un falso positivo crece con el número de pruebas.

💡 **Cómo se explica en la clase [B12-C09](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md):**
- Reconocer y corregir el problema de pruebas múltiples.
- ⚠️ **Error frecuente:** Ignorar las pruebas múltiples. Se corrige con 8.6 y el ejercicio 11.
- 🎯 **Por qué importa:** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.

📘 **Dónde se aprende** (1 clase): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md).

### PSD

- La PSD `S(f)`;
- PSD: densidad espectral de potencia, g²/Hz.

💡 **Cómo se explica en la clase [B43-C23](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md):**
- PS["PSD A/f²"] --> P["perfil con fases aleatorias"]
- *Descripción textual:* una PSD fija la rugosidad en una banda; la TIS la convierte en luz dispersa por la fórmula escalar.
- ⚠️ **Error frecuente:** Confundir PSD con la amplitud de un modo. Se corrige con 8.1.
- 🎯 **Por qué importa:** La luz dispersa reduce el contraste y la reflectancia especular. La decisión central: ¿qué rugosidad RMS, en qué banda de frecuencias espaciales, deja la luz dispersa por debajo del presupuesto?

📘 **Dónde se aprende** (2 clases): [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md); [B90-C09 · Ensayos de vibración](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md).

### Pseudocódigo

- El pseudocódigo es un algoritmo escrito en frases ordenadas, sin la sintaxis de un lenguaje.

💡 **Cómo se explica en la clase [B07-C01](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md):**
- Con eso, el algoritmo se lee casi igual que el pseudocódigo:
- Descomponer un problema pequeño en pasos no ambiguos y escribirlos como pseudocódigo.
- 🎯 **Por qué importa:** En astronomía casi todo resultado pasa por un procedimiento repetible: reducir imágenes, ajustar una órbita, buscar el máximo de una curva de luz. Si no puedes describir el procedimiento con precisión, no puedes ejecutarlo en un computador ni dárselo a otra persona para que lo repita.

📘 **Dónde se aprende** (1 clase): [B07-C01 · Pensamiento algorítmico](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md).

### Pseudodistancia

- La pseudodistancia es la distancia aparente medida con el tiempo de viaje de la señal, con el sesgo del reloj del receptor.
- La pseudodistancia es `ρᵢ = |sᵢ − x| + c δt`.

💡 **Cómo se explica en la clase [B57-C10](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md):**
- Un sesgo de reloj de `0,3 ms` equivale a `89,9 km` de pseudodistancia y se recupera con error de `1,6e-17 s`.
- S["satelites en r_i"] --> P["pseudodistancias P_i"]
- 🎯 **Por qué importa:** La geodesia con GNSS mide posiciones de estaciones con precisión de milímetros a centímetros y sirve para ver cómo se mueve la corteza. Pero la precisión depende de la geometría de los satélites.

📘 **Dónde se aprende** (2 clases): [B57-C10 · Geodesia mediante GNSS](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md); [B89-C16 · GNSS como navegación de satélites](../programa/clases/B89/B89-C16-gnss-como-navegacion-de-satelites/CLASE.md).

### Pseudoinversa amortiguada

- Espacio nulo: movimientos articulares que no mueven el extremo. Pseudoinversa amortiguada: `Jᵀ(JJᵀ + λ²I)⁻¹`.

💡 **Cómo se explica en la clase [B101-C02](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md):**
- Aplicar el método de Newton con pseudoinversa amortiguada a una pose de seis dimensiones.
- 🎯 **Por qué importa:** El operador pide «lleva la herramienta allí» y el brazo debe decidir cuántos grados gira cada articulación. Hay ninguna, una, varias o infinitas soluciones.

📘 **Dónde se aprende** (1 clase): [B101-C02 · Cinemática inversa y redundancia de manipuladores](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md).

### PSF

- La PSF (*point spread function*) es la imagen que el sistema da de una fuente puntual; en el modelo, la respuesta impulsional bidimensional de C08.
- La PSF es la respuesta del instrumento a una fuente puntual.
- La PSF es la respuesta a una fuente puntual.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- Con PSF gaussiana: `FWHM = 2,355 σ` y pico normalizado `1/(2πσ²)`.
- donde `⋆` es la correlación con la PSF (convolución con la PSF volteada).
- ⚠️ **Error frecuente:** Usar una PSF que no corresponde al instrumento y al campo. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.

📘 **Dónde se aprende** (6 clases): [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md); [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md); [B45-C24 · Fotometría por ajuste de PSF](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md); [B74-C02 · Observación angular y astrometría](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md); [B74-C25 · Detección de limbo y bordes planetarios en imágenes de navegación](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md).

### PSF conocida

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C19](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md):**
- Límites: PSF conocida; ruido gaussiano aproximado.
- 🎯 **Por qué importa:** Deconvolucionar recupera detalle bajo el límite de difracción pero amplifica el ruido. La decisión central: ¿qué método usar y qué se gana y se pierde con cada uno?

📘 **Dónde se aprende** (1 clase): [B42-C19 · Reconstrucción de imágenes](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md).

### Psia

- Diluyente: gas inerte de la mezcla (al menos 30 %). Psia: libras por pulgada cuadrada absolutas.

💡 **Cómo se explica en la clase [B106-C03](../programa/clases/B106/B106-C03-composicion-atmosferica-respirable/CLASE.md):**
- Con un máximo de 70 % de O₂, `P = 47 + 149/0,7 = 259,9 mmHg = 34,64 kPa = 5,02 psia`.
- El resumen consultado da 5,0 psia como presión más baja alcanzable.
- 🎯 **Por qué importa:** El cuerpo no responde a la fracción de oxígeno sino a su presión parcial; bajar la presión total exige subir la fracción, y eso trae riesgo de incendio (C17). La decisión central: ¿qué par presión–composición da normoxia dentro de los límites consultados?

📘 **Dónde se aprende** (1 clase): [B106-C03 · Composición atmosférica respirable](../programa/clases/B106/B106-C03-composicion-atmosferica-respirable/CLASE.md).

### Psicrófilo

- Un psicrófilo crece mejor a temperaturas bajas; la clasificación exacta por intervalo varía y aquí no se fija.

💡 **Cómo se explica en la clase [B64-C03](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. Un artículo de divulgación dice «los psicrófilos viven a −40 °C como si nada».
- El script [psicrofilos.py](psicrofilos.py) calcula factores y Q10, recupera `Eₐ` de datos con ruido y compara el factor directo con el producto por tramos (comprueba 2 %, 1e-12 y 1e-9).
- 🎯 **Por qué importa:** El frío no detiene la vida de golpe: la ralentiza. La pregunta motivadora: ¿cuánto más lento es el metabolismo a −40 °C que a 25 °C, y qué significa «vivir» a esa velocidad?

📘 **Dónde se aprende** (1 clase): [B64-C03 · Psicrófilos y vida en frío](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md).

### PSLR

- El PSLR es la razón entre el mayor lóbulo lateral y el pico principal.

💡 **Cómo se explica en la clase [B69-C02](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md):**
- Medir anchuras a −3 dB y el nivel del lóbulo lateral (PSLR).
- Ejercicio 8 · autónomo. ¿A qué amplitud corresponde un PSLR de −13,26 dB?
- 🎯 **Por qué importa:** Sin procesamiento, un eco crudo parece ruido. La decisión central: ¿qué operaciones convierten el eco crudo en una imagen con la resolución teórica, y cuándo fallan?

📘 **Dónde se aprende** (1 clase): [B69-C02 · Formación de imágenes SAR](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md).

### Publicación anticipada

- La publicación anticipada (API) es la descripción general de la red que se publica en la circular de información de la Oficina de Radiocomunicaciones (BR IFIC).

💡 **Cómo se explica en la clase [B120-C01](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md):**
- Según el documento consultado, antes de actuar bajo el Artículo 11 la administración envía la publicación anticipada «no antes de siete años y preferentemente no después de dos años» antes de la puesta en servicio planeada.
- *Descripción textual:* la fecha de la publicación anticipada abre una ventana; la coordinación, la notificación y la puesta en servicio deben caer dentro de ventanas derivadas de ella.
- 🎯 **Por qué importa:** B119-C09 presenta las normas sin el procedimiento. La decisión central: dada la fecha de recepción de la publicación anticipada, ¿entre qué fechas deben ocurrir la coordinación, la notificación y la puesta en servicio, y qué se pierde si no ocurren?

📘 **Dónde se aprende** (1 clase): [B120-C01 · Licencias satelitales y procedimiento de notificación](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md).

### Pueblo originario

- Un pueblo originario es un pueblo con historia anterior a la formación del Estado actual.

💡 **Cómo se explica en la clase [B02-C06](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md):**
- Con lo consultado no podemos describir constelaciones concretas mapuche, ni su cuenta de los días, ni el conocimiento de otros pueblos originarios de Chile (lickanantay, aymara, rapanui, kawésqar, yagán y otros).
- Ejercicio 12 · integrador. Elabora la *ficha de fuente y consentimiento* (sección 20) para un saber celeste de un pueblo originario de Chile: pueblo, fuente, quién habla, qué dice, qué falta y qué consentimiento necesitarías.
- 🎯 **Por qué importa:** Chile alberga algunos de los cielos más oscuros del mundo y los más grandes observatorios, y también pueblos que miraron esos cielos durante milenios. La pregunta motivadora es: ¿cómo hablar de saberes celestes de pueblos vivos sin generalizar, sin apropiarse y sin presentar como establecido lo que no hemos podido verificar?

📘 **Dónde se aprende** (1 clase): [B02-C06 · Astronomía de pueblos originarios de Chile](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md).

### Puente

- Un puente es un enlace sin alternativa.

💡 **Cómo se explica en la clase [B88-C31](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md):**
- En la estrella y el árbol todo enlace es puente: una falla aísla un nodo.
- 🎯 **Por qué importa:** Una red con un enlace crítico único pierde un subsistema entero con una sola falla. La decisión central: ¿qué topología da la tolerancia y la latencia necesarias con el menor número de enlaces?

📘 **Dónde se aprende** (1 clase): [B88-C31 · Topologías de red de datos a bordo](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md).

### Puente browniano

- La marcha aleatoria de fase y el puente browniano.

🎯 **Por qué importa (clase B46-C17):** Sin calibrar, la fase de la visibilidad no contiene el cielo. La decisión central: ¿cada cuánto hay que observar el calibrador para que el residuo no destruya la coherencia?

📘 **Dónde se aprende** (1 clase): [B46-C17 · Calibración de fase](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md).

### Puerta

- Una puerta es el umbral de distancia estadística bajo el cual se acepta una asociación.

💡 **Cómo se explica en la clase [B118-C02](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md):**
- De las 43, 40 son los objetos no catalogados y 3 son pistas conocidas rechazadas por la puerta (esperado `1 % × 360 = 3,6`).
- *Descripción textual:* cada pista se compara con todos los objetos del catálogo mediante una distancia normalizada por la incertidumbre; si la menor distancia cabe en la puerta se asocia, si no queda sin pareja.
- ⚠️ **Error frecuente:** Fijar una puerta sin conocer la incertidumbre. Se corrige con 8.3: la puerta depende de `σ`.
- 🎯 **Por qué importa:** Sin un catálogo no hay conjunciones: cada alerta empieza identificando de qué objeto habla. Los formatos antiguos tienen límites de tamaño y la asociación de observaciones puede equivocarse.

📘 **Dónde se aprende** (1 clase): [B118-C02 · Catálogos de objetos espaciales](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md).

### Puerto

- Un puerto es un amplificador de salida independiente.

💡 **Cómo se explica en la clase [B44-C18](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md):**
- N["pixeles"] --> T["pixeles entre puertos por frecuencia"]
- *Descripción textual:* el número de píxeles, los puertos y la frecuencia fijan el tiempo de lectura; este y la exposición dan el tiempo muerto.
- 🎯 **Por qué importa:** Leer lento reduce ruido pero desperdicia tiempo de observación. La decisión central: ¿qué modo de lectura equilibra ruido y tiempo muerto?

📘 **Dónde se aprende** (1 clase): [B44-C18 · Control electrónico de cámaras](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md).

### Puerto oscuro

- El puerto oscuro es la salida donde, sin onda, no llega luz.

💡 **Cómo se explica en la clase [B28-C06](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md):**
- Si uno se alarga por la onda, los fotones tardan más y llegan desfasados; la fase se lee en la intensidad del puerto oscuro.
- Escribir la potencia del puerto oscuro `P₀ sin²(Δφ/2)`.
- 🎯 **Por qué importa:** Un detector que mide `10⁻¹⁹ m` necesita muchos fotones y cavidades que multipliquen el efecto. La decisión central: ¿qué fase produce una onda, qué fase mínima permite el ruido de disparo y cómo se mejora la sensibilidad?

📘 **Dónde se aprende** (1 clase): [B28-C06 · Interferómetros gravitacionales](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md).

### Puesta en servicio

- La puesta en servicio (BIU, *bringing into use*) es el inicio efectivo del uso de la asignación.

💡 **Cómo se explica en la clase [B120-C01](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md):**
- Según el documento consultado, antes de actuar bajo el Artículo 11 la administración envía la publicación anticipada «no antes de siete años y preferentemente no después de dos años» antes de la puesta en servicio planeada.
- Una asignación a una estación espacial geoestacionaria se considera puesta en servicio cuando una estación con capacidad de transmitir o recibir esa frecuencia ha estado desplegada y mantenida en la posición notificada 90 días continuos; la administración informa a la Oficina en los 30 días siguientes (No. 11.44B).
- 🎯 **Por qué importa:** B119-C09 presenta las normas sin el procedimiento. La decisión central: dada la fecha de recepción de la publicación anticipada, ¿entre qué fechas deben ocurrir la coordinación, la notificación y la puesta en servicio, y qué se pierde si no ocurren?

📘 **Dónde se aprende** (1 clase): [B120-C01 · Licencias satelitales y procedimiento de notificación](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md).

### Púlsar

- Un púlsar es una estrella de neutrones que emite pulsos periódicos.

💡 **Cómo se explica en la clase [B27-C05](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md):**
- En un púlsar de milisegundos, el retardo de Shapiro mide la masa (`2,14 M☉` para J0740+6620, S5, resumen).
- *Descripción textual:* del periodo y su derivada salen la pérdida de energía rotacional, el campo y la edad; en una binaria, el semieje y el periodo orbital dan la función de masa y, con la masa del púlsar, la de la compañera.
- 🎯 **Por qué importa:** Un púlsar da, a la vez, un reloj de precisión, la medida de su campo magnético y, en una binaria, la masa de las estrellas y una prueba de la relatividad general. La decisión central: dados el periodo y su derivada, ¿qué campo, edad y potencia de frenado tiene el púlsar y qué se aprende de su binaria?

📖 **Explicado a fondo:** [Estrella de neutrones y púlsar](esencial/esencial-d-l.md#estrella-de-neutrones-y-púlsar) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md).

### Pulso semisenoidal

- SRS: espectro de respuesta al choque, pico del oscilador según su frecuencia. Pulso semisenoidal: medio ciclo de seno de amplitud `A` y duración `T`.

💡 **Cómo se explica en la clase [B90-C10](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md):**
- Un pulso semisenoidal `a(t) = A sen(πt/T)` con `A = 200 g` y `T = 1 ms` cambia la velocidad en `ΔV = 2AT/π = 1,2486 m/s`.
- Calcular el cambio de velocidad de un pulso semisenoidal.
- 🎯 **Por qué importa:** Dos pulsos con distinta forma pueden dañar lo mismo si sus SRS coinciden, y un pulso con gran aceleración pico puede ser inofensivo para un equipo de baja frecuencia. La decisión central: ¿qué frecuencias de mi equipo están amenazadas por este choque y con qué nivel?

📘 **Dónde se aprende** (1 clase): [B90-C10 · Ensayos de choque](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md).

### Pulso térmico

- Un pulso térmico es un episodio recurrente de ignición de la capa de helio.

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- En la fase AGB, dos capas de fusión (hidrógeno y helio) rodean el núcleo y la capa de helio se enciende de forma recurrente: son los pulsos térmicos.
- A["Pulso térmico<br/>(capa de He)"] --> B["Fuente de neutrones<br/>en la zona intermedia"]
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.

📘 **Dónde se aprende** (1 clase): [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### Pulverización

- La pulverización es la expulsión de moléculas por el paso de un ion.
- La pulverización es el arranque de átomos por impacto iónico.

💡 **Cómo se explica en la clase [B68-C03](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md):**
- Consecuencia: una capa fina de hielo, como la del inicio de la formación de manto, se pulveriza menos que una gruesa.
- El rendimiento de pulverización crece con el cuadrado de `Se` y depende del espesor; la química depende de la dosis y de los valores G de cada paso.
- 🎯 **Por qué importa:** Un hielo en una nube densa recibe poca luz ultravioleta externa, pero sigue recibiendo partículas energéticas y fotones secundarios. Esas dosis lentas transforman la composición del hielo durante millones de años.

📘 **Dónde se aprende** (2 clases): [B68-C03 · Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md); [B78-C21 · Erosión y vida útil de propulsores eléctricos](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md).

### Puntaje

- El puntaje `S` es la suma ponderada de los criterios.
- El puntaje `L×C` se clasifica (en el ejemplo: alto ≥ 15, medio 8–14, bajo < 8).
- El puntaje `s = θ + ε` suma un ruido `ε`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B83-C16](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md):**
- R["Riesgos: L, C, impacto"] --> P["Puntaje L x C"]
- *Descripción textual:* cada riesgo da un puntaje y una exposición; sumados definen el retraso total, que se estudia por Monte Carlo y por enumeración exacta; la probabilidad de caber en la reserva se mejora mitigando los mayores puntajes.
- 🎯 **Por qué importa:** Una lista de riesgos sin números no dice cuánta reserva hace falta ni qué mitigar primero. La decisión central: ¿qué riesgos mitigar primero y alcanza la reserva de calendario para los que no se mitiguen?

📘 **Dónde se aprende** (5 clases): [B83-C16 · Gestión de riesgos técnicos](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md); [B104-C03 · Selección y aptitud](../programa/clases/B104/B104-C03-seleccion-y-aptitud/CLASE.md); [B122-C07 · Clasificación de severidad e impacto de incidentes espaciales](../programa/clases/B122/B122-C07-clasificacion-de-severidad-e-impacto-de-incidentes-espaciales/CLASE.md); [B124-C04 · Diseño de propuesta de valor](../programa/clases/B124/B124-C04-diseno-de-propuesta-de-valor/CLASE.md); [B124-C20 · Proyecto integrador y portafolio profesional](../programa/clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md).

### Puntaje de alerta temprana

- Un puntaje de alerta temprana suma puntos por parámetros fisiológicos.

🎯 **Por qué importa (clase B116-C04):** Un puntaje simple ayuda a decidir rápido y de forma homogénea, pero un fallo por defecto (sub-triage) deja sin atender a quien lo necesita y uno por exceso (sobre-triage) agota recursos y atención. Y si la respuesta de tierra tarda decenas de minutos, no se puede esperar a tierra para lo que no admite espera.

📘 **Dónde se aprende** (1 clase): [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Puntaje de Brier

- El puntaje de Brier `BS = (1/N) Σ (fᵢ − oᵢ)²` mide el error cuadrático medio de las probabilidades pronosticadas `fᵢ ∈ [0,1]` frente a los resultados `oᵢ ∈ {0,1}`; 0 es perfecto.

💡 **Cómo se explica en la clase [B12-C24](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md):**
- Frente a la persistencia (pronosticar para hoy lo que ocurrió ayer, con puntaje de Brier ≈ `2ō(1−ō)` por ser 0/1), el mismo pronóstico obtiene `BSS = 0,510`.
- *Descripción textual:* de los pronósticos y eventos se calcula el puntaje de Brier y, con una referencia, el BSS; con un umbral se arma la tabla de contingencia y de ella POD, POFD, TSS y HSS; un bootstrap da la incertidumbre de las métricas; el informe declara referencia, umbral, muestra y límites.
- 🎯 **Por qué importa:** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.

📘 **Dónde se aprende** (1 clase): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md).

### Puntaje de habilidad de Brier

- El puntaje de habilidad de Brier es `BSS = 1 − BS/BS_ref`: 1 es perfecto, 0 iguala a la referencia, negativo es peor.

🎯 **Por qué importa (clase B12-C24):** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.

📘 **Dónde se aprende** (1 clase): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md).

### Puntaje de habilidad de Heidke

- El puntaje de habilidad de Heidke `HSS = 2(ad − bc)/[(a+c)(c+d) + (a+b)(b+d)]` compara los aciertos con los esperados por azar y sí depende de la tasa base.

🎯 **Por qué importa (clase B12-C24):** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.

📘 **Dónde se aprende** (1 clase): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md).

### Puntaje ponderado

- El puntaje ponderado es la suma de los criterios normalizados por sus pesos, que suman 1.
- El puntaje ponderado es `Σ w_j x_j`.
- El puntaje ponderado es `Σ w_k s_ik`.

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- Calcular un puntaje ponderado y ordenar los sitios.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?

📘 **Dónde se aprende** (3 clases): [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B95-C03 · Selección y comparación de plataformas](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md); [B124-C04 · Diseño de propuesta de valor](../programa/clases/B124/B124-C04-diseno-de-propuesta-de-valor/CLASE.md).

### Puntaje z modificado

- El puntaje z modificado es `Mᵢ = 0,6745 (xᵢ − mediana)/MAD`; se marca `|Mᵢ| > 3,5` (umbral convencional).

💡 **Cómo se explica en la clase [B12-C19](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md):**
- El puntaje z modificado con la MAD marca exactamente los dos.
- Paso 1 · Criterio. Grubbs al 5 % bilateral; puntaje z modificado como contraste.
- 🎯 **Por qué importa:** Un dato aberrante puede ser un error del instrumento, una pérdida de sincronía o el primer indicio de un fenómeno real. Eliminarlo sin criterio esconde información; conservarlo sin revisar contamina el resultado.

📘 **Dónde se aprende** (1 clase): [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md).

### Puntero de primera cabecera

- El puntero de primera cabecera (FHP) da el desplazamiento del primer paquete que comienza en la trama: `11111111111` si ninguno empieza y `11111111110` si el campo es de relleno.

💡 **Cómo se explica en la clase [B94-C03](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md):**
- Resincronizar paquetes con el puntero de primera cabecera.
- 🎯 **Por qué importa:** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?

📘 **Dónde se aprende** (1 clase): [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### Punto a punto

- Un mensaje punto a punto va de un proceso a otro; una operación colectiva involucra a todo el comunicador.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Con la regla del punto medio, `π ≈ h Σ_{i=0}^{n-1} 4/(1+x_i²)`, `x_i = (i+½)h`, `h = 1/n`.
- Lectura. Ambos cumplen la tolerancia con holgura (el error teórico de la regla del punto medio con `n = 10⁶` es del orden de 10⁻¹³ o menor).
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.

📘 **Dónde se aprende** (1 clase): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md).

### Punto cero

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C21](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md):**
- Con un punto cero de `10¹⁰ fotones/s/m²`, eficiencia `0,30`, subapertura de `0,2 m` y trama de `2 ms` (ilustrativos) la magnitud límite es `9,555` con `36,2` fotones por subapertura, y con una densidad ilustrativa de `0,0116 estrellas/arcmin²` la cobertura de un disco de 30 arcsec es `0,0091`.
- 🎯 **Por qué importa:** La mayoría del cielo no tiene una estrella brillante cerca: la cobertura limita a la óptica adaptativa natural. La decisión central: ¿hasta qué magnitud corrige el lazo y qué fracción del cielo queda cubierta?

📘 **Dónde se aprende** (3 clases): [B42-C21 · Estrellas guía naturales y cobertura de cielo](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B45-C21 · Estándares fotométricos y sistemas de referencia](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md).

### Punto ciego

- Oclusión: interposición de un objeto. Punto ciego: punto que ninguna cámara ve.

💡 **Cómo se explica en la clase [B101-C09](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md):**
- Quedan 42 puntos ciegos (0,9 %) con las tres cámaras, en `x` de −0,1 a 0,4 m y `z` de −0,5 a 0,4 m, es decir, tras la carga. 4 421 puntos (96,2 %) los ven al menos dos cámaras.
- Descripción larga: la segunda cámara aporta 8,8 puntos porcentuales y la tercera solo 0,6; los puntos ciegos se concentran detrás de la carga.
- 🎯 **Por qué importa:** Si el operador no ve el punto de contacto, depende de la imaginación. La decisión central: ¿qué cámaras necesito y dónde para que la zona de trabajo se vea, con qué resolución y sin puntos ciegos críticos?

📘 **Dónde se aprende** (1 clase): [B101-C09 · Coordinación visual y cámaras en operaciones con manipulador](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md).

### Punto crítico

- El punto crítico `(T_c, P_c)` es el extremo de la curva de vaporización: por encima de ambos, la sustancia es un fluido supercrítico, sin diferencia nítida entre líquido y gas.
- Un punto crítico es un `x` donde `f′(x) = 0` o `f′` no existe.
- Un punto crítico es donde `∇f = 0`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- En el diagrama del agua, el punto triple es `(273,16 K; 0,0061 bar)` y el punto crítico, `(647 K; 220,64 bar)` (S4).
- Su punto crítico es `(304,18 K; 73,80 bar)`.
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.

📘 **Dónde se aprende** (4 clases): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md); [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md); [B09-C17 · Gradiente y derivada direccional](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md); [B30-C10 · Viento solar y heliosfera](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md).

### Punto de atracción igual

- El punto de atracción igual es donde la fuerza neta de dos cuerpos se anula.

💡 **Cómo se explica en la clase [B09-C07](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md):**
- Sobre la línea que une la Tierra y la Luna existe un punto donde las dos atracciones son iguales y opuestas.
- Hallar el punto de atracción igual entre dos cuerpos y distinguir máximo de mínimo del potencial.
- 🎯 **Por qué importa:** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.

📘 **Dónde se aprende** (1 clase): [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md).

### Punto de bifurcación

- Un punto de bifurcación reparte una señal sin modificarla.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- Dibujar e interpretar un diagrama de bloques con sumadores, bloques y puntos de bifurcación.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.

📘 **Dónde se aprende** (1 clase): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md).

### Punto de compresión de 1 dB

- El punto de compresión de 1 dB es la entrada en que la ganancia cae 1 dB.

🎯 **Por qué importa (clase B49-C09):** Un receptor que satura con una señal fuerte arruina la observación de una señal débil cercana. La decisión central: ¿qué potencia máxima admite el receptor y qué productos de intermodulación genera?

📘 **Dónde se aprende** (1 clase): [B49-C09 · Linealidad, compresión e intermodulación de receptores de RF](../programa/clases/B49/B49-C09-linealidad-compresion-e-intermodulacion-de-receptores-de-rf/CLASE.md).

### Punto de control

- Un punto de control es una altura de referencia de mayor exactitud.
- El punto de control es un paso donde se mide o se actúa.

💡 **Cómo se explica en la clase [B57-C31](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md):**
- *Descripción textual:* los errores frente a puntos de control se resumen con varias métricas, algunas sensibles y otras robustas a atípicos, y se comparan con la exactitud especificada, con intervalos de confianza.
- Un MDE se compara con `400` puntos de control: errores gaussianos con sesgo `0,5 m` y desviación `2,0 m`, y una variante con `3 %` de valores atípicos de `±20 m` (sintéticos).
- 🎯 **Por qué importa:** Decir «el MDE tiene 4 m de error» sin definir la métrica ni los puntos de control no significa nada. La decisión central: ¿qué métrica y qué intervalo de confianza reporto para que mi validación sea comparable y honesta?

📘 **Dónde se aprende** (2 clases): [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md); [B115-C07 · Bioseguridad e inocuidad alimentaria en hábitats](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md).

### Punto de desvío

- El punto de desvío (*turn-off*) es la masa de las estrellas que acaban de dejar la secuencia principal.

💡 **Cómo se explica en la clase [B24-C19](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md):**
- Para una edad dada, la masa del punto de desvío se obtiene por bisección.
- A `0,5 Gyr` el punto de desvío es `2,56 M☉` y la fracción esperada de supervivientes es `98,6 %` (`2958 ± 6`); el laboratorio encuentra `2957`, dentro de `3σ`.
- 🎯 **Por qué importa:** La edad de una estrella aislada es difícil de medir; la de un cúmulo se puede leer en su diagrama HR, porque las estrellas más masivas ya han salido de la secuencia principal y el «punto de desvío» marca la edad. Esas edades fijan la cronología de la Galaxia y calibran los modelos.

📘 **Dónde se aprende** (1 clase): [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Punto de equilibrio

- El punto de equilibrio es el tamaño o la intensidad a partir de la cual compensa.
- El punto de equilibrio es `N* = M_planta/M_pieza`.
- El punto de equilibrio es `t_eq = M_eq/(D η − repuestos)`.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- Paso final · incertidumbre. Los parámetros del modelo son inventados: con valores reales, el equilibrio será otro; la ganancia y el punto de equilibrio dependen del hardware, de los costes de lanzamiento y de la memoria.
- Plantear un modelo de tiempo con transferencia y calcular el punto de equilibrio.
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?

📘 **Dónde se aprende** (8 clases): [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md); [B84-C38 · Producción de piezas y repuestos con materia prima in situ](../programa/clases/B84/B84-C38-produccion-de-piezas-y-repuestos-con-materia-prima-in-situ/CLASE.md); [B100-C07 · Dependencia de suministros terrestres y cierre de lazos logísticos](../programa/clases/B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md); [B106-C06 · Reciclaje de agua](../programa/clases/B106/B106-C06-reciclaje-de-agua/CLASE.md); [B124-C02 · Agencias científicas y empresas](../programa/clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md); [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md) y 2 más.

### Punto de espejo

- El punto de espejo es donde `v_∥ = 0`.

🎯 **Por qué importa (clase B30-C16):** Las partículas con ángulo de paso pequeño se pierden en la atmósfera; las demás quedan atrapadas y dañan satélites. La decisión central: ¿qué partículas quedan atrapadas y con qué periodo rebotan?

📘 **Dónde se aprende** (1 clase): [B30-C16 · Cinturones de Van Allen](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md).

### Punto de inflexión

- Un punto de inflexión es donde cambia la concavidad.

💡 **Cómo se explica en la clase [B09-C07](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md):**
- Si `f″ = 0` la prueba no decide: en `x³`, `x = 0` es un punto de inflexión.
- Su límite: la bola puede detenerse también en una meseta o en un punto de inflexión como `x³` en 0, que no es ni máximo ni mínimo.
- 🎯 **Por qué importa:** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.

📘 **Dónde se aprende** (1 clase): [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md).

### Punto de intercepción de tercer orden

- El punto de intercepción de tercer orden (IIP3) es la entrada ficticia en que los productos igualarían a la fundamental.

🎯 **Por qué importa (clase B49-C09):** Un receptor que satura con una señal fuerte arruina la observación de una señal débil cercana. La decisión central: ¿qué potencia máxima admite el receptor y qué productos de intermodulación genera?

📘 **Dónde se aprende** (1 clase): [B49-C09 · Linealidad, compresión e intermodulación de receptores de RF](../programa/clases/B49/B49-C09-linealidad-compresion-e-intermodulacion-de-receptores-de-rf/CLASE.md).

### Punto de Lagrange

- Un punto de Lagrange es un equilibrio del potencial efectivo `Ω`: `∇Ω = 0`.

💡 **Cómo se explica en la clase [B73-C03](../programa/clases/B73/B73-C03-puntos-de-equilibrio-de-lagrange/CLASE.md):**
- python programa/clases/B73/B73-C03-puntos-de-equilibrio-de-lagrange/puntos_lagrange.py
- 🎯 **Por qué importa:** Los puntos de Lagrange son donde se estacionan observatorios y donde se acumulan asteroides troyanos. Un error de signo en la ecuación mueve L2 al otro lado.

📘 **Dónde se aprende** (1 clase): [B73-C03 · Puntos de equilibrio de Lagrange](../programa/clases/B73/B73-C03-puntos-de-equilibrio-de-lagrange/CLASE.md).

### Punto de Lagrange L1

- El punto de Lagrange L1 es el punto entre las dos estrellas donde las fuerzas sobre el gas se anulan.

💡 **Cómo se explica en la clase [B24-C22](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md):**
- Definir potencial de Roche, punto de Lagrange L1 y lóbulo de Roche.
- 🎯 **Por qué importa:** Una estrella que se expande (C16) o se hincha en una binaria puede llenar la región donde su gravedad domina y verter gas sobre su compañera. Esa transferencia cambia las masas, la órbita y el destino de ambas, y es el camino hacia muchos objetos exóticos.

📘 **Dónde se aprende** (2 clases): [B24-C22 · Evolución binaria: lóbulo de Roche y transferencia de masa](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md); [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md).

### Punto de máxima potencia

- El punto de máxima potencia (MPP) es el máximo de `P = V I`.

💡 **Cómo se explica en la clase [B86-C02](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md):**
- *Descripción textual:* la luz fija `I_ph`; el diodo y la resistencia en serie dan la curva `I(V)`; de ella salen los extremos, el punto de máxima potencia, el factor de llenado y la eficiencia; la temperatura modifica el diodo.
- Analogía: una manguera con presión fija y una válvula; con la válvula cerrada hay presión y no hay caudal, con la válvula abierta hay caudal y no hay presión, y la potencia máxima está en un punto intermedio.
- 🎯 **Por qué importa:** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Punto de Poisson

- El punto de Poisson: máximo en el centro de la sombra.

💡 **Cómo se explica en la clase [B47-C07](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md):**
- Un disco de `0,05 m` a `1000 m` (número de Fresnel `4,545`) deja una intensidad axial de `1,000000`, el punto de Poisson.
- Reconocer el punto de Poisson en el eje.
- 🎯 **Por qué importa:** La luz difractada del disco es mayor que la señal buscada. La decisión central: ¿cuánta supresión de luz difractada se necesita y con qué geometría de ocultador?

📘 **Dónde se aprende** (1 clase): [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md).

### Punto de reorden

- El punto de reorden `s` es la existencia a la que se pide.

💡 **Cómo se explica en la clase [B104-C21](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md):**
- *Descripción textual:* el consumo y el plazo definen la demanda durante la espera y con ella el punto de reorden; la simulación mide los faltantes; aparte, los objetos se empaquetan en bolsas y se compara con la cota inferior.
- Paso 4 · Punto de reorden. `168 + 18,5 = 186,5 kg`.
- 🎯 **Por qué importa:** Quedarse sin un consumible a bordo no se arregla enviando a alguien a comprarlo. La decisión central: ¿con qué punto de reorden se pide para que el faltante sea raro, y cuánto volumen cuesta guardar lo pedido?

📘 **Dónde se aprende** (1 clase): [B104-C21 · Inventario, logística y estiba a bordo](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md).

### Punto de rocío

- Punto de rocío: temperatura a la que el vapor satura.
- Humedad relativa: `p_v/e_s`. Punto de rocío: `T` con `e_s(T_d) = p_v`.

💡 **Cómo se explica en la clase [B48-C06](../programa/clases/B48/B48-C06-meteorologia-de-observatorios/CLASE.md):**
- T["T y HR"] --> D["Punto de rocío (Magnus)"]
- *Descripción textual:* el viento simulado alimenta una regla con dos umbrales y tiempos de espera; la temperatura y la humedad dan el punto de rocío como margen contra la condensación.
- ⚠️ **Error frecuente:** Confundir punto de rocío con temperatura. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un cierre que oscila abre y cierra la cúpula cientos de veces y desgasta el equipo. La decisión central: ¿qué regla de cierre evita el parpadeo sin perder tiempo útil?

📘 **Dónde se aprende** (2 clases): [B48-C06 · Meteorología de observatorios](../programa/clases/B48/B48-C06-meteorologia-de-observatorios/CLASE.md); [B106-C07 · Gestión de humedad](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md).

### Punto de ruptura

- El punto de ruptura de un estimador es la fracción máxima de datos que pueden ser arbitrariamente malos sin que el estimador se vaya al infinito: 0 para la media, 50 % para la mediana.
- Un punto de ruptura es donde dos ramas reales se juntan y salen al plano complejo.

💡 **Cómo se explica en la clase [B12-C11](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md):**
- Por eso el punto de ruptura de la media es 0 y el de la mediana, 50 %.
- Mediana/Theil–Sen tienen alto punto de ruptura pero pierden eficiencia y Theil–Sen es costoso para `n` grande.
- 🎯 **Por qué importa:** Los datos reales traen errores de transmisión, rayos cósmicos en un detector, una lectura perdida o un salto del sensor. Un solo punto muy alejado puede torcer la recta de mínimos cuadrados y producir parámetros y predicciones erróneos con errores típicos pequeños y engañosos.

📘 **Dónde se aprende** (2 clases): [B12-C11 · Regresión robusta](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md); [B16-C09 · Lugar de las raíces](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md).

### Punto de silla

- Un punto de silla es máximo en una dirección y mínimo en otra.

💡 **Cómo se explica en la clase [B09-C15](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md):**
- Una sonda que pasa por ahí «cae» fuera del eje por los lados: punto de silla.
- F --> G["Máximo, mínimo<br/>o punto de silla"]
- ⚠️ **Error frecuente:** Confundir un punto de silla con un máximo o un mínimo. Se corrige con el ejercicio 2.
- 🎯 **Por qué importa:** Una sonda que viaja de la Tierra a la Luna se mueve en un campo de potencial que depende de dos coordenadas del plano. Dónde están los puntos de equilibrio y qué forma tiene el campo alrededor de ellos se lee en un mapa de curvas de nivel.

📘 **Dónde se aprende** (1 clase): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md).

### Punto de trabajo

- El punto de trabajo es la fase donde se mide la pendiente máxima.

💡 **Cómo se explica en la clase [B28-C06](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md):**
- Con `4 × 10⁴` fotones esperados en el puerto en el punto de trabajo (`φ₀ = π/2`) y una fase inyectada de `2,0 × 10⁻³ rad`, 2000 realizaciones con semilla fija dan una fase media `1,8476 × 10⁻³` y una desviación `4,9942 × 10⁻³`, frente a `5,0000 × 10⁻³` esperada (`√P/(dP/dφ)`).
- 🎯 **Por qué importa:** Un detector que mide `10⁻¹⁹ m` necesita muchos fotones y cavidades que multipliquen el efecto. La decisión central: ¿qué fase produce una onda, qué fase mínima permite el ruido de disparo y cómo se mejora la sensibilidad?

📘 **Dónde se aprende** (1 clase): [B28-C06 · Interferómetros gravitacionales](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md).

### Punto del limbo

- Un punto del limbo es una dirección `h_k` con `h_k·n = cos ρ`.

💡 **Cómo se explica en la clase [B87-C04](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md):**
- Cada punto del limbo cumple `h_k·n = cos ρ`.
- *Descripción textual:* la altitud fija el radio angular; los puntos del limbo están a ese ángulo del nadir, y un ajuste lineal por mínimos cuadrados devuelve el nadir y su error.
- 🎯 **Por qué importa:** Para apuntar una antena o una cámara hacia la Tierra hace falta el nadir. La decisión central: ¿cuántos puntos del limbo y qué precisión se necesitan, y cuánto cambia el resultado con la altitud y con un error en el radio angular supuesto?

📘 **Dónde se aprende** (1 clase): [B87-C04 · Sensores terrestres](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md).

### Punto fijo

- El punto fijo itera `E ← M + e sin E`.

💡 **Cómo se explica en la clase [B71-C14](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md):**
- Punto fijo: `39.1` iteraciones de media, máximo `500` y `13` casos sin converger en 500.
- En el caso `M = 0,1 rad` el laboratorio muestra (iteraciones con `E₀ = π`, con `E₀ = M` y punto fijo): `e = 0,0935`: 5, 3, 11;
- 🎯 **Por qué importa:** Propagar una órbita kepleriana exige resolver esta ecuación miles de veces; un método que no converge en `e` alto rompe todo el cálculo. La decisión central: ¿qué solucionador y qué valor inicial usas para que converja siempre y con cuántas iteraciones?

📘 **Dónde se aprende** (1 clase): [B71-C14 · Ecuación de Kepler](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md).

### Punto L1

- El punto L1 es el equilibrio entre la estrella y el cúmulo.

💡 **Cómo se explica en la clase [B52-C04](../programa/clases/B52/B52-C04-formacion-de-planetesimales/CLASE.md):**
- El punto L1 del problema restringido circular (estrella `M`, cúmulo `m`, `ω² = G(M+m)/D³`) se halla por bisección de `GM/x² − Gm/(D−x)² − ω²(x − x_cm) = 0`.
- Hallar numéricamente el punto L1 y compararlo con el radio de Hill.
- 🎯 **Por qué importa:** Si la autogravedad solo gana contra las mareas por encima de cierta densidad, esa densidad fija cuánto debe concentrarse el polvo. La decisión central: ¿qué densidad necesita un cúmulo de partículas para colapsar a una distancia dada?

📘 **Dónde se aprende** (1 clase): [B52-C04 · Formación de planetesimales](../programa/clases/B52/B52-C04-formacion-de-planetesimales/CLASE.md).

### Punto medio

- El punto medio es `t_k + h/2`.

💡 **Cómo se explica en la clase [B11-C07](../programa/clases/B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md):**
- RK4 sondea la pendiente en el inicio, dos veces en el medio (con dos estimaciones distintas del estado medio) y en el final, y luego pondera: los puntos medios pesan el doble.
- 🎯 **Por qué importa:** La mayoría de los programas de simulación científica usa, de forma directa o como base, un método de la familia Runge–Kutta. Entender RK4 permite leer cualquier código de propagación, estimar cuántos pasos necesita una órbita y saber en qué punto empieza a ser conveniente algo más sofisticado.

📘 **Dónde se aprende** (1 clase): [B11-C07 · Runge-Kutta de cuarto orden](../programa/clases/B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md).

### Punto medio modificado

- El punto medio modificado con `n` subpasos de tamaño `h = H/n` es: `z₁ = z₀ + h f(z₀)`, `z_{m+1} = z_{m−1} + 2h f(z_m)` y `y(H) ≈ ½[z_n + z_{n−1} + h f(z_n)]`; su error es un desarrollo en potencias pares de `h`.

💡 **Cómo se explica en la clase [B11-C21](../programa/clases/B11/B11-C21-integracion-numerica-de-alta-precision/CLASE.md):**
- Aplicar el punto medio modificado y extrapolar con Richardson en `h²`.
- Ejercicio 1 · con los pasos indicados. Calcula el punto medio modificado con `n = 2` para `y′ = y`, `H = 1`.
- 🎯 **Por qué importa:** Una trayectoria de millones de vueltas, un encuentro cercano que exige metros de precisión o una comprobación contra otro código piden errores de truncamiento muy por debajo del que da RK4 a costo razonable. A orden alto el costo por precisión baja mucho, pero el error de redondeo pasa a ser el límite.

📘 **Dónde se aprende** (1 clase): [B11-C21 · Integración numérica de alta precisión](../programa/clases/B11/B11-C21-integracion-numerica-de-alta-precision/CLASE.md).

### Punto porcentual

- Un punto porcentual es la diferencia entre dos porcentajes: pasar de 20 % a 25 % es un aumento de 5 puntos porcentuales, que es un cambio relativo de 25 %.

💡 **Cómo se explica en la clase [B03-C03](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md):**
- Si una proporción pasa de 20 % a 25 %, subió 5 puntos porcentuales (diferencia de porcentajes) y subió 25 % en términos relativos (`5/20`).
- Distinguir porcentaje de punto porcentual.
- ⚠️ **Error frecuente:** Confundir punto porcentual con porcentaje. Ejercicio 6.
- 🎯 **Por qué importa:** La Tierra no gira en un círculo: su distancia al Sol varía a lo largo del año. ¿Mucho o poco?

📘 **Dónde se aprende** (1 clase): [B03-C03 · Porcentajes y escalas comparativas](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md).

### Punto tangente

- El punto tangente es donde la línea de visión es tangente a un círculo.

💡 **Cómo se explica en la clase [B46-C11](../programa/clases/B46/B46-C11-observacion-de-hidrogeno-a-21-centimetros/CLASE.md):**
- Hallar el punto tangente y la velocidad terminal.
- Ejercicio 7. ¿Por qué el máximo está en el punto tangente?
- 🎯 **Por qué importa:** La velocidad de cada componente del perfil indica dónde está el gas, y su integral cuánto hay. La decisión central: ¿qué velocidad de la línea corresponde a cada distancia y qué columna implica una intensidad?

📘 **Dónde se aprende** (1 clase): [B46-C11 · Observación de hidrógeno a 21 centímetros](../programa/clases/B46/B46-C11-observacion-de-hidrogeno-a-21-centimetros/CLASE.md).

### Punto triple

- El punto triple es el único par (P, T) donde coexisten las tres fases.
- El punto triple es el par (T, P) donde coexisten hielo, líquido y vapor.

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- En el diagrama del agua, el punto triple es `(273,16 K; 0,0061 bar)` y el punto crítico, `(647 K; 220,64 bar)` (S4).
- Para el CO₂, el punto triple está en `5,185 bar`, es decir, a una presión más de cinco veces la atmosférica: por eso el CO₂ sólido a presión ambiental no se funde, sublima (S5).
- ⚠️ **Error frecuente:** Extrapolar el modelo lejos del punto triple sin advertirlo. Se corrige con la sección 8.3 y el ejercicio 5.
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.

📘 **Dónde se aprende** (2 clases): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md); [B56-C06 · Agua líquida y solventes alternativos](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md).

### Punto triple del agua

- El kelvin se define fijando el valor de la constante de Boltzmann, `k = 1,380 649 × 10⁻²³ J/K` (S1, S2); el punto triple del agua, `273,16 K`, ya no define el kelvin pero sigue siendo una referencia práctica de calibración (S2).

💡 **Cómo se explica en la clase [B13-C16](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md):**
- El punto triple del agua, `273,16 K`, deja de definir la unidad, pero una celda de punto triple evacuada a `611,657 Pa` sigue siendo una referencia práctica, con celdas de laboratorio que concuerdan con `273,16 K` a unos `50 µK` (S2).
- Su sensor es una resistencia lineal sintética, `R(T) = 100,000 + 0,3850 (T − 273,16) Ω`, calibrada con el punto triple del agua (`273,16 K`) y un baño de referencia a `323,15 K` (sintético).
- 🎯 **Por qué importa:** Un sensor de temperatura pegado a un panel de una nave devuelve una resistencia. Convertirla en kelvin exige calibrarlo contra referencias conocidas, y comprobar que la temperatura medida concuerda con un balance térmico previsto.

📘 **Dónde se aprende** (1 clase): [B13-C16 · Calibración térmica](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md).

### Punto único de falla

- Un punto único de falla es un elemento cuya caída detiene el servicio.

🎯 **Por qué importa (clase B122-C01):** B119-C16 solo introduce la infraestructura crítica y no analiza de quién depende. La decisión central: ¿qué proveedor, si cae, daña más servicios, y cuánto baja el riesgo si hay una segunda fuente?

📘 **Dónde se aprende** (1 clase): [B122-C01 · Dependencias de proveedores y cadena de suministro de infraestructura espacial](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md).

### Punto vernal

- La ascensión recta (AR, `α`) es el ángulo, medido hacia el este sobre el ecuador celeste, entre el punto vernal (un punto del ecuador que sirve de origen) y el círculo que une los polos con el astro; se expresa en horas (24 h = 360°).

💡 **Cómo se explica en la clase [B08-C03](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md):**
- La ascensión recta es como la longitud: da la vuelta completa, pero se mide hacia el este desde el punto vernal en lugar de desde Greenwich.
- C["Punto vernal"] --> D["AR: ángulo hacia el este (0 h a 24 h)"]
- 🎯 **Por qué importa:** Un catálogo no puede decir «a la izquierda de la Luna», porque eso cambia a cada minuto. Necesita direcciones fijas.

📘 **Dónde se aprende** (1 clase): [B08-C03 · Ascensión recta y declinación](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md).

### Puntos de colocación

- Los puntos de colocación son los instantes donde se exige que el residuo sea pequeño.

💡 **Cómo se explica en la clase [B17-C03](../programa/clases/B17/B17-C03-redes-neuronales-informadas-por-la-fisica-pinn/CLASE.md):**
- Se eligen puntos de colocación `tⱼ` (aquí 60, repartidos uniformemente en [0, 3]) y se arma
- B --> C["Residuo de la EDO<br/>en puntos de colocación"]
- ⚠️ **Error frecuente:** Medir el error solo donde hay colocación. Evalúa en puntos distintos (301 en el laboratorio).
- 🎯 **Por qué importa:** Un modelo ajustado solo a datos puede reproducir muy bien lo medido y decir disparates fuera de ese rango: no sabe que una cantidad decae, ni que una oscilación conserva su amplitud. Si ya conoces la ecuación que gobierna el fenómeno, dejarla fuera es desperdiciar información.

📘 **Dónde se aprende** (1 clase): [B17-C03 · Redes neuronales informadas por la física (PINN)](../programa/clases/B17/B17-C03-redes-neuronales-informadas-por-la-fisica-pinn/CLASE.md).

### Puntos de Lagrange colineales

- Los puntos de Lagrange colineales `L1`, `L2`, `L3` están sobre la línea Tierra-Luna y son puntos de equilibrio en el marco sinódico.

💡 **Cómo se explica en la clase [B76-C01](../programa/clases/B76/B76-C01-sistema-tierra-luna/CLASE.md):**
- Resolver por bisección los puntos de Lagrange colineales `L1`, `L2` y `L3`.
- 🎯 **Por qué importa:** Una nave que sale de la Tierra hacia la Luna siente dos atracciones comparables en una región pequeña. La decisión central: ¿en qué punto del sistema deja de bastar el modelo de dos cuerpos y qué escalas gobiernan el problema?

📘 **Dónde se aprende** (1 clase): [B76-C01 · Sistema Tierra-Luna](../programa/clases/B76/B76-C01-sistema-tierra-luna/CLASE.md).

### Puntos homólogos

- Los puntos homólogos son posiciones del mismo objeto en las dos imágenes.

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- Puntos homólogos: exige emparejar puntos (por ejemplo, detectados como en C12) pero admite rotación, escala y ajuste con incertidumbre.
- Con puntos homólogos, en cambio, hallas la rotación y la traslación que mejor los hacen coincidir.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».

📘 **Dónde se aprende** (1 clase): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md).

### Puntos por longitud de onda

- El número de Courant `ν = cΔt/Δx` compara cuánto avanza la onda en un paso con el ancho de celda. Puntos por longitud de onda es `λ/Δx`.

💡 **Cómo se explica en la clase [B21-C02](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md):**
- Para `kΔx` pequeño (muchos puntos por longitud de onda) se obtiene `c_num/c ≈ 1 − (kΔx)²(1 − ν²)/24`.
- Con `ν = 0,5` y 10 puntos por longitud de onda (`kΔx = 0,628`) la aproximación da `−1,23 %` y la fórmula exacta `−1,24 %`.
- 🎯 **Por qué importa:** Casi toda señal que viaja en el espacio —ondas de radio, ondas de Alfvén en la corona solar, ondas sísmicas en una luna, vibraciones de una estructura— obedece alguna forma de la ecuación de onda.

📘 **Dónde se aprende** (1 clase): [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md).

### Puntos sigma

- La transformada unscented aproxima la distribución con `2n+1` puntos sigma y los pesos `w_m`, `w_c`.

💡 **Cómo se explica en la clase [B74-C10](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md):**
- P["previa (m, P)"] --> S["puntos sigma"]
- Paso 4 · Lectura. En el laboratorio el azimut se envuelve a `[−π, π]` en la innovación y en el promedio ponderado de los puntos sigma.
- 🎯 **Por qué importa:** Un filtro puede dar una estimación aceptable y una covarianza falsa. La decisión central: ¿cuándo basta el EKF y cuándo la covarianza obliga a usar un filtro no lineal, y cómo lo verifico con una referencia?

📘 **Dónde se aprende** (1 clase): [B74-C10 · Filtro de Kalman no lineal](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md).

### Puntuación de Brier

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B33-C05):** La mejor comunicación de riesgo da probabilidades calibradas y deja decidir al usuario. La decisión central: ¿cuándo conviene proteger y cuán fiables son las probabilidades?

📘 **Dónde se aprende** (1 clase): [B33-C05 · Comunicación de riesgo y alertas de clima espacial](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md).

### Puntuación de Heidke

- La puntuación de Heidke mide la mejora sobre el azar.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- Aunque el 91,8 % de los días se pronostican bien, la regla «nunca alertar» acierta el 95,1 % (`346/364`) con habilidad nula (Heidke 0): la tasa de aciertos no sirve cuando el evento es raro, y la puntuación de Heidke sí.
- Calcular POD, FAR, CSI y la puntuación de Heidke por dos fórmulas.
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?

📘 **Dónde se aprende** (1 clase): [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md).

### Puntuación de mutación

- La puntuación de mutación `= muertos/total`.

💡 **Cómo se explica en la clase [B88-C14](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md):**
- La evidencia es la informe de pruebas con puntuación de mutación del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *informe de pruebas con puntuación de mutación*: pruebas, cobertura, mutantes, vivos y lista de qué es sintético.
- 🎯 **Por qué importa:** Una prueba que pasa no prueba nada si pasaría también con el código roto. La decisión central: ¿las pruebas detectan los cambios de comportamiento o solo recorren el código?

📘 **Dónde se aprende** (1 clase): [B88-C14 · Pruebas de software embarcado](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md).

### Puntuación de mutantes

- La puntuación de mutantes es la fracción de muertos.

💡 **Cómo se explica en la clase [B94-C06](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md):**
- La evidencia es la matriz de trazabilidad requisito–prueba con puntuación de mutantes del ejercicio 12 (sección 20).
- Ejercicio 10 · transferencia. Transferencia. ¿Basta una puntuación de mutantes del 100 % para declarar conformidad?
- 🎯 **Por qué importa:** Una implementación que «funciona con la mía» puede fallar con otra. La decisión central: ¿qué pruebas demuestran que cada requisito se cumple y cómo sabes que tu suite detectaría un defecto?

📘 **Dónde se aprende** (1 clase): [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Puntuación robusta

- Límite fijo: umbral de 3σ. Puntuación robusta: desvío en unidades de MAD.

💡 **Cómo se explica en la clase [B96-C13](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md):**
- La puntuación robusta se adapta a la deriva porque la ventana la absorbe: ve picos, no cambios lentos.
- La puntuación robusta no ve la deriva (la ventana se adapta) y CUSUM la ve en 7 muestras, con 5 falsas alarmas.
- 🎯 **Por qué importa:** Un detector que no ve una deriva lenta avisa cuando ya es tarde, y uno que alarma por todo se ignora. La decisión central: ¿qué detector ve cada tipo de anomalía, con qué retraso y a qué costo en falsas alarmas?

📘 **Dónde se aprende** (1 clase): [B96-C13 · Detección de anomalías](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md).

### Puntuación tipo SAGAT

- Una puntuación tipo SAGAT congela una simulación y pregunta por cada nivel; aquí se simula, no se mide.

🎯 **Por qué importa (clase B111-C04):** Falta la clase que trate la conciencia situacional de la tripulación. La decisión central: ¿cómo se cuantifica lo que el equipo sabe y cada cuánto debe verificarlo para que no se quede desactualizado?

📘 **Dónde se aprende** (1 clase): [B111-C04 · Conciencia situacional en operaciones de vuelo](../programa/clases/B111/B111-C04-conciencia-situacional-en-operaciones-de-vuelo/CLASE.md).

### Puntuación z

- La puntuación z estandariza la serie.

🎯 **Por qué importa (clase B105-C09):** Un umbral bajo detecta pronto pero alarma de más; uno alto alarma poco pero tarda. Con una tripulación pequeña, las falsas alarmas se acumulan.

📘 **Dónde se aprende** (1 clase): [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md).

### Pupila

- La pupila `P(x)`.

💡 **Cómo se explica en la clase [B42-C06](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md):**
- La pupila tiene `812` píxeles (disco ideal `804,2`); el pico sin aberración vale `659 344 = 812²`.
- Una inclinación de 5 ciclos por pupila mueve el pico de la columna 0 a la 5 sin cambiar su valor (`1,000000`).
- 🎯 **Por qué importa:** Toda imagen es la escena convolucionada con la PSF; si la PSF se degrada, se pierde resolución y contraste. La decisión central: ¿cómo se calcula la PSF de una pupila con aberraciones y cuándo basta el pico?

📘 **Dónde se aprende** (1 clase): [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md).

### Pupila de entrada

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C09):** La pupila limita la luz y el viñeteo oscurece los bordes. La decisión central: ¿qué diafragma manda y cuánta luz se pierde fuera del eje?

📘 **Dónde se aprende** (1 clase): [B41-C09 · Pupilas y diafragmas ópticos](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md).

### Pupila de salida

- La pupila de salida es el círculo de luz que sale del ocular, de diámetro `D/M`.
- La pupila de salida es `D/M`.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- Con estos números se calcula: 7×50 → pupila de salida `50/7 = 7,14 mm`; 10×50 → `5,0 mm`; 7×35 → `5,0 mm`.
- Pausa. ¿Qué binoculares tienen mayor pupila de salida: 8×42 o 10×50? <details><summary>Respuesta</summary>8×42: `42/8 = 5,25 mm`; 10×50: `5,0 mm`.</details>
- ⚠️ **Error frecuente:** Ignorar la pupila de salida. Ejercicio 4.
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?

📘 **Dónde se aprende** (4 clases): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md); [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md); [B41-C07 · Aumentos y sistemas afocales](../programa/clases/B41/B41-C07-aumentos-y-sistemas-afocales/CLASE.md); [B41-C09 · Pupilas y diafragmas ópticos](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md).

### Pureza

- La pureza compara los grupos con clases conocidas (solo existe con datos sintéticos o ya etiquetados).

💡 **Cómo se explica en la clase [B17-C06](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md):**
- Paso 5 · incertidumbre. Como los datos son sintéticos, se puede medir la pureza (0,997: 3 de 900 mal asignados).
- Ejercicio 7. La pureza fue 0,997 con 900 objetos.
- 🎯 **Por qué importa:** Un catálogo trae miles de objetos medidos en varias bandas y nadie los ha clasificado. ¿Hay poblaciones distintas?

📘 **Dónde se aprende** (1 clase): [B17-C06 · Aprendizaje no supervisado](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md).

### Push-to

- Una montura motorizada o con GoTo apunta y sigue con motores; push-to guía sin motores.

🎯 **Por qué importa (clase B08-C15):** A 120 aumentos, un planeta cruza el ocular en menos de dos minutos y tienes que empujar el tubo constantemente. La pregunta motivadora: ¿qué montura necesito y qué error puedo tolerar al seguir un objeto?

📘 **Dónde se aprende** (1 clase): [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md).

### PV

- El PV es el valor del trabajo planificado a la fecha; el EV, el valor del trabajo logrado; el AC, el costo real.
- El PV y el RMS del resto.

💡 **Cómo se explica en la clase [B43-C22](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md):**
- La superficie tiene `14,84` franjas (PV total/(λ/2)); el resto, `0,308`.
- La superficie tiene `14,8` franjas en total; tras ajustar piston, inclinaciones y desenfoque queda un resto de `97,3 nm` PV y `19,90 nm` RMS (`0,0314 λ`).
- 🎯 **Por qué importa:** El mapa de error de forma es la prueba de aceptación de un espejo. La decisión central: ¿cómo se recupera la fase, qué se descuenta y qué PV y RMS quedan?

📘 **Dónde se aprende** (2 clases): [B43-C22 · Interferometría de superficie y mapas de error de forma](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md); [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### P-valor bilateral

- El p-valor bilateral es `erfc(n_σ/√2)`.

💡 **Cómo se explica en la clase [B26-C23](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md):**
- Ejercicio 4. p-valor bilateral de `4,40σ`.
- 🎯 **Por qué importa:** Decir «hay una tensión» solo tiene sentido con un número: ¿cuántas sigmas?, ¿qué probabilidad de ocurrir por azar?, ¿qué se asume? Sin ese rigor, una discrepancia se exagera o se descarta.

📘 **Dónde se aprende** (1 clase): [B26-C23 · Tensiones observacionales: constante de Hubble y S8](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md).

### Pwo

- Un pwo es un navegante maestro en la tradición de las islas Carolinas (S3).

💡 **Cómo se explica en la clase [B02-C07](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md):**
- Una valora que Mau compartiera el conocimiento por responsabilidad de preservarlo; otra, de personas micronesias, critica apropiación y objeta que la Sociedad nombre navegantes *pwo* (S3).
- 🎯 **Por qué importa:** Se discutió durante décadas si los pueblos del Pacífico llegaron a las islas por azar o por navegación deliberada. La pregunta motivadora es: ¿cómo se orienta quien no puede ver tierra, y qué dice su método sobre el valor del conocimiento oral?

📘 **Dónde se aprende** (1 clase): [B02-C07 · Observaciones de Polinesia y navegación oceánica](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md).

### Pyproject.toml

- Las dependencias de ejecución se instalan siempre; las de desarrollo (por ejemplo, la herramienta de pruebas) solo para quien trabaja en el proyecto (S2). `pyproject.toml` es el archivo del proyecto que declara su nombre, versión de Python requerida y dependencias (S3).

💡 **Cómo se explica en la clase [B07-C13](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md):**
- En una carpeta vacía, `uv init --no-package --python 3.12 orbita` crea `.python-version`, `README.md`, `main.py` y `pyproject.toml` con `dependencies = []`; sin `--no-package`, el proyecto se crea como aplicación con paquete en `src/` (S5).
- Luego `uv add "numpy==2.4.4"` crea `.venv`, resuelve las versiones, descarga e instala y escribe en `pyproject.toml`: `dependencies = ["numpy==2.4.4"]`.
- 🎯 **Por qué importa:** «En mi computador funciona» es la frase más cara de la informática científica: el programa depende, sin decirlo, de la versión de Python y de cada biblioteca instalada. Si cambian, los resultados pueden cambiar o el programa fallar con un `ModuleNotFoundError`.

📘 **Dónde se aprende** (1 clase): [B07-C13 · Entornos y dependencias con uv](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md).
