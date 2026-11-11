# Términos · M (parte 3 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · **M** · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-m.md) · [2](terminos-m-2.md) · **3**

### Muerto

- Un mutante es una copia de la IUT con un defecto inyectado; está muerto si alguna prueba falla y sobrevive si todas pasan.
- El píxel caliente da más señal que el vecino; el muerto, menos o ninguna.
- Un mutante muerto hace fallar alguna prueba; uno vivo, no.

💡 **Cómo se explica en la clase [B44-C15](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md):**
- En un cuadro de `64 × 64` con `30` calientes (+300 ADU) y `20` muertos (valor 0), la sigma robusta es `10,10 ADU` (verdadera `10`) frente a una desviación habitual de `75,07`.
- El script [defectuosos.py](defectuosos.py) detecta calientes y muertos con la MAD y los repara con la mediana de los vecinos (comprueba que se detectan los 50 y que hay menos de 3 falsos positivos).
- 🎯 **Por qué importa:** La media y la desviación habituales se distorsionan con los defectos. La decisión central: ¿qué umbral detecta todos los defectos sin falsos positivos?
- 🔗 **Se estudia junto con:** píxel caliente, MAD, máscara, interpolación.

📘 **Dónde se aprende** (3 clases): [B44-C15 · Píxeles defectuosos](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md); [B88-C14 · Pruebas de software embarcado](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md); [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Muestra de auditoría

- Hash anclado: hash final guardado aparte. Muestra de auditoría: entradas revisadas.

💡 **Cómo se explica en la clase [B96-C30](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md):**
- Consultar la bitácora y calcular una muestra de auditoría.
- Ejercicio 12 · integrador. Integrador. Elabora tu *bitácora verificable con prueba de manipulación*: entrada, cadena, manipulaciones probadas, límite del truncamiento, muestra de auditoría y lista de lo consultado, sintético y no consultado.
- 🎯 **Por qué importa:** Sin registro verificable no se puede reconstruir un incidente ni demostrar quién aprobó un comando. La decisión central: ¿cómo se registra para que una alteración se detecte y cuánto hay que revisar en una auditoría?
- 🔗 **Se estudia junto con:** Bitácora, Cadena de hashes, Anexado solo, Hash anclado.

📘 **Dónde se aprende** (1 clase): [B96-C30 · Registro y auditoría de operaciones](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md).

### Muestra limitada por flujo

- La muestra limitada por flujo detecta lo más brillante que `m_lim`.

💡 **Contexto en la clase [B28-C19](../programa/clases/B28/B28-C19-limitaciones-y-sesgos-de-deteccion/CLASE.md):**
- **Idea central (modelo mental):** La red solo retiene peces mayores que cierto tamaño; cuanto más lejos, más grande hay que ser. Al medir lo que cae en la red se sobrestima el tamaño medio del lago.
- 🎯 **Por qué importa:** Si se promedia la luminosidad de los eventos detectados sin corregir, se sobrestima la luminosidad típica de la población. El mismo razonamiento vale para las masas de fusiones de ondas gravitacionales detectadas.
- 🔗 **Se estudia junto con:** sesgo de Malmquist, función de selección, normal truncada, módulo de distancia.

📘 **Dónde se aprende** (1 clase): [B28-C19 · Limitaciones y sesgos de detección](../programa/clases/B28/B28-C19-limitaciones-y-sesgos-de-deteccion/CLASE.md).

### Muestra sintética

- La muestra sintética es un conjunto de datos simulados.

💡 **Cómo se explica en la clase [B26-C20](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md):**
- En esta clase se ajusta una muestra sintética de `100` supernovas con `Ω_m = 0,315` verdadero y ruido de `0,15 mag`.
- Datos: ninguno observado; muestra sintética;
- 🎯 **Por qué importa:** Una cifra cosmológica sin incertidumbre no significa nada. Para decidir si dos resultados concuerdan, o si un modelo queda excluido, hay que saber construir y leer un intervalo de confianza.
- 🔗 **Se estudia junto con:** χ², grados de libertad, mejor ajuste, intervalo de 68 %.

📘 **Dónde se aprende** (1 clase): [B26-C20 · Límites observacionales de modelos cosmológicos](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md).

### Muestras de entrenamiento

- Las muestras de entrenamiento son píxeles con clase conocida usados para estimar el clasificador; las muestras de prueba son píxeles independientes con clase conocida para evaluarlo.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- Con 30 muestras de entrenamiento por clase y 5000 de prueba por clase, el laboratorio da:
- Su límite: en el gráfico ves los grupos; en una imagen real, las clases no son gaussianas ni están bien definidas, y las muestras de entrenamiento pueden estar sesgadas.
- ⚠️ **Error frecuente:** Muestras de prueba correlacionadas con las de entrenamiento. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, NDVI, clase, muestras de prueba.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Muestras de prueba

- Las muestras de entrenamiento son píxeles con clase conocida usados para estimar el clasificador; las muestras de prueba son píxeles independientes con clase conocida para evaluarlo.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- Con 30 muestras de entrenamiento por clase y 5000 de prueba por clase, el laboratorio da:
- La evaluación honesta exige muestras de prueba separadas (o validación cruzada).
- ⚠️ **Error frecuente:** Muestras de prueba correlacionadas con las de entrenamiento. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, NDVI, clase, muestras de entrenamiento.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Muestreo

- El muestreo es tomar valores de una señal continua a intervalos regulares `Δt`.
- El muestreo: píxeles por `λ/D`.

💡 **Cómo se explica en la clase [B15-C02](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md):**
- A["Señal continua<br/>frecuencia f"] --> B["Muestreo<br/>f_s = 1/Δt"]
- Paso 2 · Muestreo. `f_s = 86 400/120 = 720 c/d`;
- 🎯 **Por qué importa:** Un detector que mide una estrella cada 2 minutos no puede ver directamente algo que oscila cada 3 minutos con precisión, pero tampoco lo ignora: ese movimiento rápido queda registrado como una oscilación lenta y falsa. Si no sabes que eso ocurre, publicarías un periodo que no existe.
- 🔗 **Se estudia junto con:** frecuencia de muestreo, frecuencia de Nyquist, aliasing, filtro antialias.

📘 **Dónde se aprende** (2 clases): [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md); [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md).

### Muestreo de importancia

- El muestreo de importancia estima `E_p[h(X)]` sorteando de otra densidad `q` (la propuesta) y ponderando cada muestra por el peso `w(x) = p(x)/q(x)`: `E_p[h] = ∫ h p dx = ∫ h (p/q) q dx = E_q[h w]`.
- El muestreo de importancia pondera muestras de la previa con la verosimilitud para aproximar la posterior de Bayes.

💡 **Cómo se explica en la clase [B12-C15](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md):**
- Muestreo de importancia: gran ahorro si la propuesta es buena, riesgo de varianza infinita si no.
- Estimar un suceso raro y su error típico con muestreo de importancia.
- 🎯 **Por qué importa:** Los sucesos que más interesan en seguridad espacial —un error de aproximación fuera de límites, una falla simultánea, una colisión— son raros por diseño. Un Monte Carlo simple puede pasar millones de ensayos sin ver un solo acierto y reportar «cero», que no es una estimación útil.
- 🔗 **Se estudia junto con:** propuesta, peso, insesgado, varianza.

📘 **Dónde se aprende** (2 clases): [B12-C15 · Muestreo de importancia](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md); [B74-C10 · Filtro de Kalman no lineal](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md).

### Muestreo de Nyquist

- El muestreo de Nyquist: al menos 2 píxeles por `λ/D`.
- El muestreo de Nyquist pide al menos dos píxeles por elemento resoluble.
- El muestreo de Nyquist pide al menos `2` píxeles por FWHM.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C01](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md):**
- Decidir el tamaño de píxel por muestreo de Nyquist.
- 🎯 **Por qué importa:** Sin requisitos escritos, cada pieza del telescopio se fabrica «lo mejor posible» y no se sabe cuándo basta. La decisión central: ¿qué error de frente de onda, qué escala de imagen y qué tolerancia mecánica hay que pedir, y cómo se reparte el error entre las piezas?
- 🔗 **Se estudia junto con:** apertura, razón focal, escala de placa, error de frente de onda.

📘 **Dónde se aprende** (6 clases): [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md); [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md); [B43-C01 · Requisitos ópticos y mecánicos](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md); [B44-C17 · Escala de imagen y muestreo](../programa/clases/B44/B44-C17-escala-de-imagen-y-muestreo/CLASE.md); [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md); [B46-C09 · Conversión analógica digital](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md).

### Muestreo descendente

- El muestreo descendente reduce la resolución (p. ej., agrupando 2 × 2) para captar contexto; el ascendente la restituye.

💡 **Contexto en la clase [B17-C11](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md):**
- 🎯 **Por qué importa:** Delimitar una mancha solar, una nube o un cráter a mano en miles de imágenes no escala. Un umbral por píxel falla cuando el ruido es comparable al contraste.
- 🔗 **Se estudia junto con:** segmentación semántica, máscara, convolución, válido.

📘 **Dónde se aprende** (1 clase): [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md).

### Muestreo estroboscópico

- El muestreo estroboscópico toma una medida por vuelta en la misma fase.

💡 **Contexto en la clase [B72-C15](../programa/clases/B72/B72-C15-aproximaciones-perturbativas/CLASE.md):**
- 🎯 **Por qué importa:** Una fórmula de primer orden se usa mucho tiempo sin preguntar cuándo deja de valer. La decisión central: ¿cómo saber cuándo basta un desarrollo de primer orden y cómo se estima su error?
- 🔗 **Se estudia junto con:** desarrollo perturbativo, método de Lindstedt–Poincaré, orden, error de truncamiento.

📘 **Dónde se aprende** (1 clase): [B72-C15 · Aproximaciones perturbativas](../programa/clases/B72/B72-C15-aproximaciones-perturbativas/CLASE.md).

### MUF

- La MUF (frecuencia máxima utilizable) para un salto de distancia `D` es `foF2/cos φ`, con `φ` el ángulo de incidencia en la capa.

💡 **Cómo se explica en la clase [B89-C22](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md):**
- Con la densidad en `4×10¹¹` la MUF baja a `63 %` de la diurna (misma razón en todas las distancias, `√(N₂/N₁)`): a 2000 km, de `25,3` a `16,0 MHz`.
- *Descripción textual:* la densidad da la frecuencia crítica; la distancia y la altura dan el ángulo de incidencia; juntos dan la MUF; una tormenta cambia la densidad y por tanto la MUF.
- ⚠️ **Error frecuente:** Confundir `foF2` con la MUF. Se corrige con 8.3.
- 🎯 **Por qué importa:** En un apagón de enlaces por satélite o en regiones remotas, el HF sigue siendo un medio de comunicación; saber qué frecuencia usar a cada hora y distancia, y cómo la perturba una tormenta, decide si el enlace existe.
- 🔗 **Se estudia junto con:** frecuencia de plasma, frecuencia crítica, salto.

📘 **Dónde se aprende** (1 clase): [B89-C22 · Propagación ionosférica y comunicaciones HF](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md).

### Multigrid

- El multigrid combina relajaciones en una jerarquía de mallas.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- Esa asimetría es la propiedad de suavizado, y es la clave del multigrid.
- Si el número de ciclos para una tolerancia dada no depende de `N`, el trabajo total es proporcional al número de incógnitas: Athena++ lo dice con la notación `O(N)` del multigrid completo frente a `O(N log N)` de la FFT (S2).
- ⚠️ **Error frecuente:** Suponer que más relajaciones en la malla fina equivalen a multigrid. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;
- 🔗 **Se estudia junto con:** ecuación de Poisson, elíptico, de Dirichlet, estencil de cinco puntos.

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Multiplicador

- El multiplicador es la producción total que genera una um de demanda final de una etapa.

💡 **Cómo se explica en la clase [B124-C01](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md):**
- El multiplicador de la etapa `j` es la suma de la columna `j` de `(I − A)⁻¹`.
- Las etapas aguas abajo tienen mayor multiplicador porque compran a varias etapas; los materiales, que no compran a nadie de la cadena, tienen 1.
- ⚠️ **Error frecuente:** Pensar que más multiplicador es siempre mejor. Se corrige con 8.4: el multiplicador no dice cuánto valor queda en la etapa.
- 🎯 **Por qué importa:** El bloque necesita un mapa común antes de hablar de costos, financiamiento o contratos: ¿quién le compra a quién y dónde queda el valor? Ninguna clase anterior del programa trata la estructura económica de la industria espacial.
- 🔗 **Se estudia junto con:** producto bruto, compras intermedias, demanda final, valor agregado.

📘 **Dónde se aprende** (1 clase): [B124-C01 · Cadena de valor de industria espacial](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md).

### Multiplicador de Lagrange

- `λ` es el multiplicador de Lagrange.
- El multiplicador de Lagrange convierte un problema con restricción en uno sin ella.

💡 **Contexto en la clase [B11-C23](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md):**
- **Idea central (modelo mental):** Una bola rueda hacia un mínimo pero choca con una pared: se queda pegada a ella. La fuerza con que la pared empuja es el multiplicador; si no hay pared en el camino, la fuerza es cero.
- 🎯 **Por qué importa:** Casi todo problema de diseño de trayectorias tiene límites: tiempo máximo, combustible disponible, distancia mínima a un cuerpo. Un optimizador que ignora las restricciones devuelve un resultado imposible; uno que las trata mal da un resultado que parece factible y no es óptimo.
- 🔗 **Se estudia junto con:** con restricción de igualdad, Lagrangiano, desigualdad, KKT.

📘 **Dónde se aprende** (2 clases): [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md); [B50-C09 · Asignación y balance de tolerancias ópticas](../programa/clases/B50/B50-C09-asignacion-y-balance-de-tolerancias-opticas/CLASE.md).

### Múltiplo de cartera

- El múltiplo de cartera es el valor devuelto entre el invertido.

💡 **Cómo se explica en la clase [B126-C02](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md):**
- Percentiles del múltiplo de cartera: `P10 = 0,86x`, `P50 = 1,86x`, `P90 = 4,88x`.
- Por cartera: múltiplo esperado y percentiles.
- 🎯 **Por qué importa:** El capital de riesgo tiene lógica y condiciones propias que el catálogo no trata. La decisión central: ¿cuánto recibe cada parte en una salida según las condiciones pactadas, y qué retorno cabe esperar de una cartera cuando casi todo el valor viene de pocos casos?
- 🔗 **Se estudia junto con:** preferencia de liquidación, Sin participación, Con participación, salida.

📘 **Dónde se aprende** (1 clase): [B126-C02 · Capital de riesgo en empresas espaciales](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md).

### Multipolo

- El multipolo de orden `n` cae como `(a/r)ⁿ`.

💡 **Contexto en la clase [B53-C03](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md):**
- **Idea central (modelo mental):** Analogía: enfocar una foto borrosa: el monopolo es la mancha, `J2` le da la forma ovalada y los términos siguientes afinan el contorno.
- 🎯 **Por qué importa:** Las trayectorias de una sonda dependen del campo. La decisión central: ¿hasta qué término de la serie hay que llegar a una distancia dada?
- 🔗 **Se estudia junto con:** monopolo, suma directa.

📘 **Dónde se aprende** (1 clase): [B53-C03 · Campo gravitatorio planetario](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md).

### Multivista

- El multivista promedia `L` vistas independientes.

💡 **Cómo se explica en la clase [B69-C03](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md):**
- La página de NASA Earthdata (S1) cuenta que el speckle aparece cuando la resolución no separa los dispersores y que el multivista lo reduce.
- Ejercicio 12 · integrador. Elabora tu *ficha del speckle y su filtrado*: estadística de una vista, tabla multivista, resultados de Lee y lectura del borde.
- 🎯 **Por qué importa:** Un valor de píxel aislado de una imagen SAR no mide la reflectividad de la superficie: es una muestra de una distribución muy ancha. La decisión central: ¿cuánto hay que promediar o filtrar para estimar la reflectividad con una incertidumbre dada, y a qué precio en resolución?
- 🔗 **Se estudia junto con:** speckle, intensidad, contraste, ENL.

📘 **Dónde se aprende** (1 clase): [B69-C03 · Ruido speckle y filtrado en imágenes SAR](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md).

### Mundo de ARN

- El mundo de ARN es la hipótesis de que una etapa temprana usó ARN como información y catalizador.

💡 **Contexto en la clase [B56-C04](../programa/clases/B56/B56-C04-hipotesis-de-abiogenesis/CLASE.md):**
- **Idea central (modelo mental):** El espacio de secuencias es un lago; cada ensayo es una tirada de caña. Sin pistas sobre dónde pescar, hay que tirar tantas veces como peces diferentes hay.
- 🎯 **Por qué importa:** Las hipótesis (mundo de ARN, metabolismo primero, ventilas hidrotermales, charcas con ciclos húmedo–seco, aporte meteorítico) se discuten a menudo con palabras. Una cuenta de espacio de secuencias permite saber cuándo una afirmación es plausible por números y cuándo exige un mecanismo de selección.
- 🔗 **Se estudia junto con:** abiogénesis, espacio de secuencias, cobertura, selección.

📘 **Dónde se aprende** (1 clase): [B56-C04 · Hipótesis de abiogénesis](../programa/clases/B56/B56-C04-hipotesis-de-abiogenesis/CLASE.md).

### Mundo helado

- Un mundo helado es el definido en 5.

💡 **Cómo se explica en la clase [B56-C18](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md):**
- Europa, Encélado y Titán, mundos helados (III orbitador, IV aterrizador por defecto;
- Para Marte y mundos helados el retorno es restringido; para la Luna es no restringido.
- ⚠️ **Error frecuente:** Suponer que los mundos helados son II. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** La política protege los otros mundos de la contaminación (para no estropear la búsqueda de vida) y la Tierra del material devuelto. Saber en qué categoría cae una misión determina su documentación, su limpieza y sus restricciones.
- 🔗 **Se estudia junto con:** categoría, categoría V, restringida, no restringida.

📘 **Dónde se aprende** (1 clase): [B56-C18 · Protección planetaria COSPAR](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md).

### MUSD

- La ventana de cobertura es el periodo en que el seguro responde. MUSD son millones de dólares ficticios.

💡 **Cómo se explica en la clase [B127-C01](../programa/clases/B127/B127-C01-seguros-de-lanzamiento/CLASE.md):**
- El Monte Carlo (200 000 lanzamientos, semilla 127) da una pérdida media de `7,103 MUSD`, error relativo `0,75 %`.
- Paso 3 · Prima pura. `200 × 0,03525 = 7,050 MUSD`.
- 🎯 **Por qué importa:** B124-C08 presenta el riesgo y los seguros en general; el seguro de lanzamiento tiene estructura y coberturas propias. La decisión central: ¿qué prima es coherente con la probabilidad de fallo y qué parte de ella es recargo?
- 🔗 **Se estudia junto con:** valor asegurado, tasa, prima pura, recargo.

📘 **Dónde se aprende** (1 clase): [B127-C01 · Seguros de lanzamiento](../programa/clases/B127/B127-C01-seguros-de-lanzamiento/CLASE.md).

### Mutación

- Una mutación es un defecto introducido a propósito para ver si las pruebas lo detectan.
- La mutación cambia, invierte o inserta bytes.

💡 **Cómo se explica en la clase [B71-C20](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md):**
- *Descripción textual:* los elementos se propagan con Kepler; seis pruebas con tolerancias fijadas de antemano decidieron si se acepta; la mutación demuestra que la comparación con un integrador independiente detecta lo que los invariantes no.
- Mostrar con una mutación que los invariantes no detectan un error de tiempo.
- 🎯 **Por qué importa:** Un propagador que «parece funcionar» puede tener un error de tiempo que ningún invariante detecta. La decisión central: ¿qué pruebas, con qué tolerancias y contra qué referencia independiente demuestran que el propagador es correcto?
- 🔗 **Se estudia junto con:** propagador, prueba de aceptación, integrador independiente, invariante.

📘 **Dónde se aprende** (2 clases): [B71-C20 · Propagador kepleriano verificable](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md); [B88-C37 · Fuzzing autorizado de software embarcado en banco de pruebas](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md).

### Mutante

- Un mutante es una copia del código con un defecto inyectado a propósito; si tus pruebas no lo detectan, la batería es débil.
- Un mutante es el programa con un defecto inyectado (C01).
- Un mutante es un defecto inyectado (C01).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B23-C01](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md):**
- Chequeo de sensibilidad. El mutante de primer orden `E ≈ M + e·sin M` se equivoca en 1,3 × 10⁻⁴ rad para este caso: una tolerancia de 1e-9 lo detecta, una de 1e-3 no.
- Se acepta cualquier solución que justifique cada tolerancia y muestre qué `rtol` mata a cada mutante.
- 🎯 **Por qué importa:** Una prueba con tolerancia muy holgada pasa siempre y no protege nada; una con tolerancia demasiado estricta falla por ruido de redondeo y se termina desactivando. La pregunta motivadora es: ¿cómo elijo una tolerancia que sea lo bastante estricta para detectar un error real y lo bastante amplia para no fallar por redondeo?
- 🔗 **Se estudia junto con:** error absoluto, error relativo, tolerancia, precisión de máquina.

📘 **Dónde se aprende** (5 clases): [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md); [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md); [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md); [B88-C14 · Pruebas de software embarcado](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md); [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Mutex

- El mutex permite un solo dueño.

💡 **Cómo se explica en la clase [B88-C27](../programa/clases/B88/B88-C27-exclusion-mutua-y-semaforos/CLASE.md):**
- Sin mutex, en 200 corridas hubo pérdida en las 200.
- Con mutex, nadie lee entre lectura y escritura de otro: `x = 100` siempre; pérdida 0 en 200 corridas.
- ⚠️ **Error frecuente:** Olvidar liberar el mutex. Libéralo siempre
- 🎯 **Por qué importa:** Una carrera no falla siempre: falla de vez en cuando y no se reproduce. La decisión central: ¿qué mecanismo garantiza que el acceso a un dato compartido sea exclusivo y que un buffer no se desborde ni se vacíe?
- 🔗 **Se estudia junto con:** carrera, semáforo, intercalado.

📘 **Dónde se aprende** (1 clase): [B88-C27 · Exclusión mutua y semáforos](../programa/clases/B88/B88-C27-exclusion-mutua-y-semaforos/CLASE.md).

### Mutuamente excluyentes

- Dos eventos son mutuamente excluyentes si `A∩B` es vacío; no es lo mismo que independientes.

💡 **Contexto en la clase [B12-C01](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md):**
- **Idea central (modelo mental):** Imagina una caja con todas las historias posibles de la misión; cada historia tiene un peso, y los pesos suman 1. Un evento es una etiqueta que pones a un grupo de historias; su probabilidad es la suma de los pesos de ese grupo.
- 🎯 **Por qué importa:** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.
- 🔗 **Se estudia junto con:** experimento aleatorio, espacio muestral, evento, probabilidad.

📘 **Dónde se aprende** (1 clase): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md).
