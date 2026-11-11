# Términos · K

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · **K** · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### K de n

- La arquitectura k de n funciona si al menos `k` de `n` unidades funcionan.

🎯 **Por qué importa (clase B86-C11):** Duplicar un equipo no duplica la confiabilidad ni resuelve todas las fallas: depende de cómo se conmuta, de si las unidades comparten una causa común y de cuánto cuesta en masa y en potencia. La decisión central: ¿qué arquitectura redundante da la confiabilidad necesaria sin pagar más masa y potencia de las debidas?

📘 **Dónde se aprende** (1 clase): [B86-C11 · Redundancia eléctrica](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md).

### Ka

- Las bandas VHF (~145 MHz), UHF (~401 MHz), S (~2,2 GHz), X (~8,4 GHz) y Ka (~32 GHz) se tratan aquí con frecuencias centrales ilustrativas.

💡 **Cómo se explica en la clase [B89-C03](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md):**
- La ganancia es `1,4` dBi en VHF, `10,3` en UHF, `25,0` en S, `36,7` en X y `48,3` en Ka; el haz pasa de `144,7°` a `0,66°`.
- Para una ganancia de 30 dBi hace falta una parábola de `9,72 m` en UHF, de `0,464 m` en X y de `0,122 m` en Ka.
- ⚠️ **Error frecuente:** Olvidar el apuntamiento al elegir Ka. Se corrige con 8.3.
- 🎯 **Por qué importa:** Elegir la banda es la primera decisión de diseño de un enlace y determina el tamaño de la antena y la tasa alcanzable. La decisión central: ¿qué banda usar para una ganancia de antena dada y qué se paga en apuntamiento por usarla?

📘 **Dónde se aprende** (1 clase): [B89-C03 · Bandas VHF UHF S X Ka](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md).

### Kabsch

- El registro alinea dos conjuntos de puntos. Kabsch es la solución de mínimos cuadrados para la rotación entre conjuntos de puntos centrados.

💡 **Cómo se explica en la clase [B103-C02](../programa/clases/B103/B103-C02-calibracion-extrinseca-y-registro-multisensor/CLASE.md):**
- Kabsch devuelve una rotación con 0,0220° de error y una traslación con 0,72 mm de error; el residuo RMS es de 3,08 mm (el ruido por tres ejes es `2 mm·√3 = 3,46 mm`).
- Estimar `R` y `t` con Kabsch (centrado, SVD y corrección de reflexión).
- 🎯 **Por qué importa:** Un error de 0,02° en la rotación entre una cámara y el brazo de un robot parece nada, pero a 10 m son 3,5 mm de error de posición, y a más distancia crece sin límite. La decisión central: ¿cuántas correspondencias y con qué geometría hacen falta para que la pose entre sensores cumpla un presupuesto de error dado?

📘 **Dónde se aprende** (1 clase): [B103-C02 · Calibración extrínseca y registro multisensor](../programa/clases/B103/B103-C02-calibracion-extrinseca-y-registro-multisensor/CLASE.md).

### K-anonimato

- El k-anonimato es el tamaño mínimo de grupo.
- El `k`-anonimato es el tamaño mínimo de los grupos de personas con los mismos cuasi-identificadores.
- El k-anonimato exige que cada combinación de cuasi-identificadores aparezca al menos `k` veces.

💡 **Cómo se explica en la clase [B105-C19](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md):**
- Calcular el k-anonimato y la fracción de registros únicos de una tabla.
- El script [privacidad.py](privacidad.py) mide el k-anonimato y la unicidad de cohortes sintéticas de 6 con cinco esquemas de cuasi-identificadores y calcula el error del ruido de Laplace por `ε` (comprueba que más cuasi-identificadores no reduce la unicidad y que el error del ruido iguala la escala de Laplace).
- 🎯 **Por qué importa:** No basta con quitar el nombre: con edad, sexo, profesión y misión, una persona de una cohorte de 6 suele ser única. La decisión central: ¿qué se puede publicar de una cohorte pequeña sin identificar a nadie y cuánta utilidad se pierde al protegerla?

📘 **Dónde se aprende** (3 clases): [B105-C19 · Bioética en investigación tripulada](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md); [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md); [B129-C05 · Consentimiento y privacidad de participantes](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md).

### Kaplan–Meier

- La censura es no haber alcanzado el criterio al terminar. Kaplan–Meier estima `S(t)` con censura.

💡 **Cómo se explica en la clase [B107-C10](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md):**
- T["tiempo al criterio, con censura"] --> K["Kaplan-Meier S(t)"]
- *Descripción textual:* las medidas dan el porcentaje de recuperación y la pendiente semanal; los tiempos con censura dan la curva de Kaplan–Meier y el CUSUM de la pendiente emite una alerta de estancamiento.
- 🎯 **Por qué importa:** Los fragmentos consultados describen el entrenamiento en la ISS (Loehr et al., 2015) y baterías funcionales con medidas fisiológicas (Mulavara et al., 2018), pero un seguimiento necesita indicadores bien definidos y bien calculados.

📘 **Dónde se aprende** (1 clase): [B107-C10 · Indicadores de rehabilitación y seguimiento](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md).

### Kappa

- El acuerdo exacto es la fracción de pares con el mismo nivel; el adyacente, con diferencia de a lo sumo un nivel. Kappa de Cohen corrige el acuerdo exacto por el azar: `κ = (po − pe)/(1 − pe)`.
- El kappa `κ = (p_o − p_e)/(1 − p_e)` corrige el azar.

💡 **Cómo se explica en la clase [B119-C26](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md):**
- El kappa no dice qué declara un Estado ni si lo cumple; solo cuán fiable es un procedimiento de lectura.
- *Descripción textual:* dos codificadores leen los mismos textos; sus asignaciones forman una matriz; de ella salen el acuerdo, el kappa y su incertidumbre.
- 🎯 **Por qué importa:** C11 y C12 tratan los límites militares y la historia; ninguna clase enseña a leer doctrinas públicas con rigor. La lectura real de documentos oficiales exige fuentes que no se consultaron aquí.

📘 **Dónde se aprende** (2 clases): [B119-C26 · Doctrinas y políticas espaciales declaradas públicamente](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md); [B131-C09 · Rúbricas de evaluación](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md).

### Kappa de Cohen

- El acuerdo esperado por azar `pₑ` se calcula con las proporciones de cada anotador; el kappa de Cohen es `κ = (pₒ − pₑ)/(1 − pₑ)`, mide el acuerdo más allá del azar y compara a dos anotadores entre sí, no a un modelo con la verdad (S2).
- El acuerdo entre dos definiciones es la fracción de casos con el mismo veredicto; el kappa de Cohen descuenta el acuerdo esperado por azar: `κ = (p_o − p_e)/(1 − p_e)`.
- El kappa de Cohen mide el acuerdo entre dos evaluadores corrigiendo el azar.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B17-C10](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md):**
- Calcular el acuerdo observado y el coeficiente kappa de Cohen entre dos anotadores.
- 🎯 **Por qué importa:** Se quiere entrenar un modelo que distinga galaxias espirales de elípticas. Hay un millón de imágenes y nadie las ha etiquetado.

📘 **Dónde se aprende** (4 clases): [B17-C10 · Conjuntos de datos etiquetados para aprendizaje supervisado](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md); [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md); [B109-C12 · Evaluación de factores humanos de maquetas y distribuciones](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md); [B124-C20 · Proyecto integrador y portafolio profesional](../programa/clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md).

### Kappa ponderado

- El kappa ponderado penaliza más los desacuerdos grandes.

🎯 **Por qué importa (clase B124-C20):** Un portafolio con una nota promedio alta puede ocultar una falta grave, como presentar datos inventados como reales. La decisión central: ¿qué hace falta para declarar logrado un portafolio y cómo se sabe que dos revisores miden lo mismo?

📘 **Dónde se aprende** (1 clase): [B124-C20 · Proyecto integrador y portafolio profesional](../programa/clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md).

### Kappa ponderado cuadrático

- El kappa ponderado cuadrático penaliza más las discrepancias grandes.

💡 **Cómo se explica en la clase [B131-C09](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md):**
- Calcular kappa de Cohen y kappa ponderado cuadrático.
- 🎯 **Por qué importa:** Una rúbrica sin acuerdo entre evaluadores asigna notas que dependen de quién corrige. La decisión central: ¿dos personas distintas darían el mismo nivel a este trabajo, y cómo lo sabes?

📘 **Dónde se aprende** (1 clase): [B131-C09 · Rúbricas de evaluación](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md).

### K_CMB

- Las unidades `K_CMB` y `K_RJ`.

💡 **Cómo se explica en la clase [B40-C10](../programa/clases/B40/B40-C10-emisiones-de-primer-plano-galacticas-y-su-separacion/CLASE.md):**
- Convertir temperaturas RJ y brillo a `K_CMB`.
- ⚠️ **Error frecuente:** Mezclar unidades `K_RJ` y `K_CMB`. Se corrige con la sección 9.
- 🎯 **Por qué importa:** Sin separar los primeros planos no se mide el fondo. La decisión central: ¿qué pesos por frecuencia minimizan la contaminación sin tocar la señal del CMB?

📘 **Dónde se aprende** (1 clase): [B40-C10 · Emisiones de primer plano galácticas y su separación](../programa/clases/B40/B40-C10-emisiones-de-primer-plano-galacticas-y-su-separacion/CLASE.md).

### Kelvin

- El kelvin se define fijando el valor de la constante de Boltzmann, `k = 1,380 649 × 10⁻²³ J/K` (S1, S2); el punto triple del agua, `273,16 K`, ya no define el kelvin pero sigue siendo una referencia práctica de calibración (S2).

💡 **Cómo se explica en la clase [B13-C16](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md):**
- Desde 2019 el kelvin se define fijando `k = 1,380 649 × 10⁻²³ J/K`: un kelvin es el cambio de temperatura termodinámica que cambia la energía térmica `kT` en esa cantidad.
- Explicar cómo el kelvin se define con la constante de Boltzmann y qué papel conserva el punto triple del agua.
- ⚠️ **Error frecuente:** Usar grados Celsius en la ley de Stefan–Boltzmann. Se corrige en el ejercicio 4 (usa kelvin).
- 🎯 **Por qué importa:** Un sensor de temperatura pegado a un panel de una nave devuelve una resistencia. Convertirla en kelvin exige calibrarlo contra referencias conocidas, y comprobar que la temperatura medida concuerda con un balance térmico previsto.

📘 **Dónde se aprende** (1 clase): [B13-C16 · Calibración térmica](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md).

### Kelvin–Helmholtz

- Los dos haces son dos poblaciones que se cruzan. Kelvin–Helmholtz nace de la cizalladura de velocidad.

💡 **Cómo se explica en la clase [B35-C03](../programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/CLASE.md):**
- Las dos vías coinciden a `10⁻⁹` en los haces y a `10⁻⁶` en Kelvin–Helmholtz.
- En Kelvin–Helmholtz con campo paralelo la perturbación crece solo si el salto de velocidad supera `2 v_A`: para `U = 3 v_A` la tasa es `1,118 k v_A`.
- ⚠️ **Error frecuente:** Olvidar el campo en Kelvin–Helmholtz. Se corrige con 8.2.
- 🎯 **Por qué importa:** Las inestabilidades limitan los equilibrios y convierten energía libre en turbulencia. La decisión central: ¿para qué número de onda y para qué cizalladura crece la perturbación y cuánto?

📘 **Dónde se aprende** (1 clase): [B35-C03 · Inestabilidades de plasma: cinéticas y de fluido](../programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/CLASE.md).

### Kepleriano

- El período nodal es el tiempo entre dos pasos consecutivos por el nodo ascendente; el kepleriano ignora las perturbaciones.

💡 **Cómo se explica en la clase [B119-C04](../programa/clases/B119/B119-C04-convenio-de-registro/CLASE.md):**
- Calcular el período kepleriano desde apogeo y perigeo con `T = 2π √(a³/GM)`.
- Distinguir el período kepleriano del nodal y nombrar el efecto que se ignora (J2).
- ⚠️ **Error frecuente:** Confundir período kepleriano y nodal. Se corrige con 8.4.
- 🎯 **Por qué importa:** El art. VIII del tratado de 1967 vincula la jurisdicción al registro, y el convenio de 1974 define qué se registra; ninguna clase anterior lo calcula ni lo valida.

📘 **Dónde se aprende** (1 clase): [B119-C04 · Convenio de Registro](../programa/clases/B119/B119-C04-convenio-de-registro/CLASE.md).

### Kernel

- Un kernel es el proceso que ejecuta el código y conserva sus variables entre celdas.
- Un kernel es un archivo de datos de SPICE.

💡 **Cómo se explica en la clase [B14-C09](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md):**
- El laboratorio simula ese criterio sin kernel: ejecuta las celdas de código con `exec`, en orden, en un espacio de nombres nuevo.
- (Es una simulación: un kernel real tiene más estado, como importaciones y configuración de gráficos.)
- 🎯 **Por qué importa:** Alguien te manda un cuaderno con un gráfico que apoya una conclusión. Lo abres, ejecutas las celdas y el gráfico sale distinto.

📘 **Dónde se aprende** (3 clases): [B14-C09 · Jupyter y experimentos reproducibles](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md); [B14-C21 · Datos de misiones planetarias: PDS4, etiquetas y SPICE](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md); [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### Kernel rotacional

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C11](../programa/clases/B32/B32-C11-ensanchamiento-rotacional-y-v-sin-i/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha del ensanchamiento rotacional*: kernel, FWHM y recuperación.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha del ensanchamiento rotacional*: kernel, FWHM y recuperación.
- 🎯 **Por qué importa:** `v sin i` es la rotación proyectada y da pistas de edad y actividad. La decisión central: ¿cómo se mide `v sin i` de un perfil?

📘 **Dónde se aprende** (1 clase): [B32-C11 · Ensanchamiento rotacional y v sin i](../programa/clases/B32/B32-C11-ensanchamiento-rotacional-y-v-sin-i/CLASE.md).

### Kilonova

- La kilonova es el transitorio térmico tras una fusión de estrellas de neutrones.

💡 **Cómo se explica en la clase [B28-C18](../programa/clases/B28/B28-C18-interpretacion-de-kilonovas/CLASE.md):**
- Metzger describe las kilonovas como transitorios térmicos casi isótropos alimentados por la desintegración radiactiva de núcleos inestables formados en la fusión (S3, resumen).
- La evidencia es la ficha de una kilonova del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** La escala de tiempo y el brillo de una kilonova dependen de la masa eyectada y de su velocidad. Entender esa relación permite estimar ambos a partir de la curva de luz.

📘 **Dónde se aprende** (1 clase): [B28-C18 · Interpretación de kilonovas](../programa/clases/B28/B28-C18-interpretacion-de-kilonovas/CLASE.md).

### KKT

- Con desigualdad `T(x) ≤ T_max` aparecen las condiciones KKT: estacionariedad `∇Dv + μ ∇T = 0`; factibilidad `T ≤ T_max`;

💡 **Cómo se explica en la clase [B11-C23](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md):**
- KKT: `Δv′ + μ T′ = 0` ⇒ `μ = 7,67 × 10⁻⁵/25,47 = 3,01 × 10⁻⁶ > 0`.
- Tres pruebas: la restricción se cumple a la tolerancia; el gradiente del Lagrangiano se anula (residuo KKT `0` en el laboratorio); y un barrido independiente de la región factible no encuentra nada mejor.
- ⚠️ **Error frecuente:** Aceptar KKT sin barrido de comprobación. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Casi todo problema de diseño de trayectorias tiene límites: tiempo máximo, combustible disponible, distancia mínima a un cuerpo. Un optimizador que ignora las restricciones devuelve un resultado imposible; uno que las trata mal da un resultado que parece factible y no es óptimo.

📘 **Dónde se aprende** (1 clase): [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md).

### K-medias

- El agrupamiento (*clustering*) divide los datos en grupos de elementos similares. k-medias busca `k` centroides que minimicen la inercia `Σ ‖x_i − c_{g(i)}‖²`.
- El agrupamiento (*clustering*) asigna cada objeto a un grupo. K-medias repite dos pasos (algoritmo de Lloyd): asignar cada punto al centro más cercano y recalcular cada centro como la media de sus puntos.

💡 **Cómo se explica en la clase [B15-C23](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md):**
- (2) `c_j = media{x_i : g(i) = j}`; se repite hasta que los centroides no cambian.
- Cada paso no aumenta la inercia: asignar al más cercano la disminuye o la mantiene; recalcular la media también (la media minimiza la suma de cuadrados).
- 🎯 **Por qué importa:** Un satélite fotografía una región que nadie ha cartografiado. Sin muestras, no se puede entrenar un clasificador, pero sí se puede preguntar cuántos «tipos» de superficie distintos hay en las bandas.

📘 **Dónde se aprende** (2 clases): [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md); [B17-C06 · Aprendizaje no supervisado](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md).

### Kolmogorov

- Seeing: ancho a media altura, `0,98 λ/r₀`. Kolmogorov: modelo de turbulencia.

💡 **Cómo se explica en la clase [B48-C12](../programa/clases/B48/B48-C12-monitorizacion-de-seeing/CLASE.md):**
- Límite: turbulencia de Kolmogorov, exposición corta y sin ruido de centroide.
- 🎯 **Por qué importa:** Sin medir el seeing, no se sabe si una noche sirve para un programa. La decisión central: ¿cuántas medidas hacen falta para que `r₀` tenga una incertidumbre aceptable?

📘 **Dónde se aprende** (1 clase): [B48-C12 · Monitorización de seeing](../programa/clases/B48/B48-C12-monitorizacion-de-seeing/CLASE.md).

### Kp

- El Kp es un índice trihorario planetario.

💡 **Cómo se explica en la clase [B30-C23](../programa/clases/B30/B30-C23-indices-geomagneticos-kp-y-dst/CLASE.md):**
- Trece estaciones ilustrativas dan `K = [3, 4, 4, 4, 4, 5, 6, 6, 2, 4, 4, 2, 5]`, promedio `4,077` y Kp `4o` (12 tercios).
- El Kp redondeado al tercio pierde información: dos conjuntos de `K` distintos pueden dar la misma etiqueta.
- ⚠️ **Error frecuente:** Pensar que el Kp es lineal. Se corrige con 8.2.
- 🎯 **Por qué importa:** Kp y Dst son los índices con que se habla de tormentas. Saber cómo se construyen y con qué incertidumbre ayuda a leer un registro.

📘 **Dónde se aprende** (1 clase): [B30-C23 · Índices geomagnéticos Kp y Dst](../programa/clases/B30/B30-C23-indices-geomagneticos-kp-y-dst/CLASE.md).

### KR-20

- La discriminación es la correlación entre acertar el ítem y el puntaje en los demás. KR-20 y el alfa de Cronbach miden la consistencia interna; para ítems dicotómicos coinciden.
- La discriminación `r` mide si quienes aciertan el ítem puntúan mejor en el resto. KR-20 estima la consistencia interna de una prueba de ítems dicotómicos.

💡 **Cómo se explica en la clase [B130-C05](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md):**
- KR-20 y el alfa de Cronbach dan ambos `0,7295` con diferencia `0` (menor que `1e-12`): son la misma cantidad calculada por dos vías.
- La fórmula de KR-20 no se consultó en una fuente concreta; la comprobación cruzada valida el código, no la fórmula.
- 🎯 **Por qué importa:** Saber si la divulgación funcionó exige medir la comprensión; ninguna otra clase lo trata. La decisión central: ¿qué número resume la mejora del público, y cuánto se puede confiar en que no sea azar?

📘 **Dónde se aprende** (2 clases): [B130-C05 · Evaluación de la comprensión del público](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md); [B131-C08 · Evaluación formativa en el aula de astronomía](../programa/clases/B131/B131-C08-evaluacion-formativa-en-el-aula-de-astronomia/CLASE.md).

### Kriging ordinario

- El kriging ordinario es el mejor estimador lineal insesgado con media constante desconocida.

💡 **Cómo se explica en la clase [B67-C05](../programa/clases/B67/B67-C05-modelos-geoestadisticos-de-distribucion-de-volatiles/CLASE.md):**
- Plantear y resolver el sistema de kriging ordinario con la restricción de suma de pesos igual a 1.
- Ejercicio 3 · casi autónomo. ¿Por qué los pesos de kriging ordinario deben sumar 1?
- 🎯 **Por qué importa:** Promediar muestras ignora que dos puntos cercanos se parecen más que dos lejanos, y una interpolación sin varianza no dice dónde se sabe poco. La decisión central: ¿qué valor y qué incertidumbre se asigna a un punto sin muestra, y dónde conviene muestrear más?

📘 **Dónde se aprende** (1 clase): [B67-C05 · Modelos geoestadísticos de distribución de volátiles](../programa/clases/B67/B67-C05-modelos-geoestadisticos-de-distribucion-de-volatiles/CLASE.md).

### K_RJ

- Las unidades `K_CMB` y `K_RJ`.

💡 **Cómo se explica en la clase [B40-C10](../programa/clases/B40/B40-C10-emisiones-de-primer-plano-galacticas-y-su-separacion/CLASE.md):**
- ⚠️ **Error frecuente:** Mezclar unidades `K_RJ` y `K_CMB`. Se corrige con la sección 9.
- 🎯 **Por qué importa:** Sin separar los primeros planos no se mide el fondo. La decisión central: ¿qué pesos por frecuencia minimizan la contaminación sin tocar la señal del CMB?

📘 **Dónde se aprende** (1 clase): [B40-C10 · Emisiones de primer plano galácticas y su separación](../programa/clases/B40/B40-C10-emisiones-de-primer-plano-galacticas-y-su-separacion/CLASE.md).

### K_sp

- Producto iónico (IP): `[Ca][SO₄]`. `K_sp`: producto de solubilidad.

💡 **Cómo se explica en la clase [B106-C27](../programa/clases/B106/B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md):**
- Precipita cuando `IP₀ CF² > K_sp`, es decir `r > r_max = 1 − √(IP₀/K_sp)`.
- Con `IP₀ = 6·10⁻⁶`, `r_max = 0,560`; a `r = 0,9` el cociente `IP/K_sp` sería 19,35.
- 🎯 **Por qué importa:** Evaporar la orina concentra sales hasta que precipitan y obstruyen el equipo; el límite lo fija la química, no la termodinámica del agua. La decisión central: ¿hasta qué fracción se puede recuperar el agua antes de precipitar y cómo se supera ese límite?

📘 **Dónde se aprende** (1 clase): [B106-C27 · Tratamiento de orina y recuperación de agua](../programa/clases/B106/B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md).

### KSZ

- El kSZ es `−τ v_r/c`.

💡 **Cómo se explica en la clase [B40-C11](../programa/clases/B40/B40-C11-efecto-sunyaev-zeldovich-termico-y-cinematico/CLASE.md):**
- El tSZ es un déficit por debajo de 217,5 GHz y un exceso por encima; el kSZ conserva la forma del cuerpo negro y no se anula.
- Ejercicio 6. Cociente tSZ/kSZ a 143 GHz.
- ⚠️ **Error frecuente:** Confundir tSZ y kSZ. Se corrige con 8.4.
- 🎯 **Por qué importa:** El tSZ no depende del corrimiento al rojo y permite detectar cúmulos lejanos. La decisión central: ¿cuánto vale la distorsión a cada frecuencia y dónde se anula?

📘 **Dónde se aprende** (1 clase): [B40-C11 · Efecto Sunyaev-Zeldovich térmico y cinemático](../programa/clases/B40/B40-C11-efecto-sunyaev-zeldovich-termico-y-cinematico/CLASE.md).
