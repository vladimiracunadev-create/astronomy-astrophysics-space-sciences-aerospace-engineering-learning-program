# Términos · C (parte 3 de 4)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · **C** · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-c.md) · [2](terminos-c-2.md) · **3** · [4](terminos-c-4.md)

### Compuerta

- Verificación geométrica: comprobar que la pose relativa medida es compatible con la odometría. Compuerta: umbral `3σ` sobre la discrepancia.
- La compuerta (*gate*) acepta una observación si `d² = νᵀS⁻¹ν < g`.

💡 **Cómo se explica en la clase [B74-C30](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md):**
- El límite a `6σ` (`85,4 %`) viene de observaciones verdaderas fuera de compuerta y de clutter cerca de una pista.
- P["pistas: prediccion y S"] --> G["compuerta de Mahalanobis"]
- ⚠️ **Error frecuente:** Creer que estar en la compuerta es una asociación correcta. Ver el ejemplo 13 y 8.4.
- 🎯 **Por qué importa:** Una asociación incorrecta no se ve en el filtro: el estado sigue convergiendo, pero hacia el objeto equivocado. La decisión central: ¿qué compuerta y qué regla de asignación equilibran el riesgo de perder una observación verdadera y el de aceptar una falsa o la de otro objeto?
- 🔗 **Se estudia junto con:** asociación de vecino más cercano, asignación global, clutter, pista.

📘 **Dónde se aprende** (2 clases): [B74-C30 · Asociación de observaciones y correlación de pistas](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md); [B99-C04 · Cierre de bucles y consistencia global](../programa/clases/B99/B99-C04-cierre-de-bucles-y-consistencia-global/CLASE.md).

### Compuesto

- El compuesto es la media geométrica de los porcentajes.

💡 **Cómo se explica en la clase [B107-C08](../programa/clases/B107/B107-C08-evaluacion-funcional-posterior-al-vuelo/CLASE.md):**
- El compuesto de cada persona se «mide» dos veces con errores de 2,0 y 2,5 puntos y un sesgo de +1,5 del evaluador B.
- Paso 2 · Compuesto. `exp((ln 69,0 + ln 76,9 + ln 62,5)/3) = 69,2 %`.
- 🎯 **Por qué importa:** El fragmento de Mulavara et al. (2018) describe una batería con siete pruebas funcionales y 15 medidas fisiológicas para entender el desempeño de tareas tras el vuelo, y Clément et al.
- 🔗 **Se estudia junto con:** R+1, porcentaje del previo, Bland–Altman, MDC95.

📘 **Dónde se aprende** (1 clase): [B107-C08 · Evaluación funcional posterior al vuelo](../programa/clases/B107/B107-C08-evaluacion-funcional-posterior-al-vuelo/CLASE.md).

### Comunicación

- La comunicación es el intercambio de datos entre procesos.

💡 **Cómo se explica en la clase [B14-C16](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md):**
- Con `T(p) = W·(s + (1−s)/p) + c·W·log₂ p` (modelo inventado), `T(1) = 1` (no hay comunicación con un proceso).
- Sin el término de comunicación, la aceleración tiende a `1/s = 50`.
- ⚠️ **Error frecuente:** Ignorar la comunicación. Se corrige con los ejercicios 4 y 5.
- 🎯 **Por qué importa:** Una simulación de la población de escombros orbitales requiere cien veces más cálculo del que tu equipo puede dar en una semana. Pides tiempo en un clúster y debes decidir: ¿cuántos procesos pido?
- 🔗 **Se estudia junto con:** clúster, planificador, escalado fuerte, escalado débil.

📘 **Dónde se aprende** (1 clase): [B14-C16 · Computación distribuida y HPC](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md).

### Comunicación del riesgo

- La comunicación del riesgo incluye probabilidad, consecuencia, incertidumbre y qué pasará después.

💡 **Cómo se explica en la clase [B58-C19](../programa/clases/B58/B58-C19-comunicacion-publica-del-riesgo/CLASE.md):**
- La evidencia es la ficha de comunicación del riesgo del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de comunicación del riesgo*: P inicial en frecuencias, evolución simulada y mensaje.
- 🎯 **Por qué importa:** El público oye «1 %» y a veces «ahora 0 %». Si no se explica que las probabilidades cambian con los datos y que la media se conserva, bajar a cero parece un error.
- 🔗 **Se estudia junto con:** frecuencia natural, actualización, martingala, escala de Torino.

📘 **Dónde se aprende** (1 clase): [B58-C19 · Comunicación pública del riesgo](../programa/clases/B58/B58-C19-comunicacion-publica-del-riesgo/CLASE.md).

### Comunicador

- Un comunicador es el grupo de procesos que pueden comunicarse;

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Explicar el modelo SPMD, el rango y el tamaño de un comunicador.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.
- 🔗 **Se estudia junto con:** tamaño, rango, SPMD, punto a punto.

📘 **Dónde se aprende** (1 clase): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md).

### Con participación

- Sin participación: cobra lo mayor entre la preferencia y lo que recibiría al convertir en acciones comunes. Con participación: cobra la preferencia y además su porcentaje del resto.

💡 **Cómo se explica en la clase [B126-C02](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md):**
- P --> Q["con participación: P + p·(S − P)"]
- *Descripción textual:* de la salida se obtiene la preferencia y la conversión; sin participación se cobra la mayor y con participación se cobra la preferencia más una parte del resto; el resto va a los demás accionistas y se verifica que los pagos sumen la salida.
- 🎯 **Por qué importa:** El capital de riesgo tiene lógica y condiciones propias que el catálogo no trata. La decisión central: ¿cuánto recibe cada parte en una salida según las condiciones pactadas, y qué retorno cabe esperar de una cartera cuando casi todo el valor viene de pocos casos?
- 🔗 **Se estudia junto con:** preferencia de liquidación, Sin participación, salida, múltiplo de cartera.

📘 **Dónde se aprende** (1 clase): [B126-C02 · Capital de riesgo en empresas espaciales](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md).

### Con restricción de igualdad

- Un problema con restricción de igualdad es `min f(z)` sujeto a `g(z) = 0`.

💡 **Cómo se explica en la clase [B11-C23](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md):**
- Plantear el Lagrangiano de un problema con restricción de igualdad.
- 🎯 **Por qué importa:** Casi todo problema de diseño de trayectorias tiene límites: tiempo máximo, combustible disponible, distancia mínima a un cuerpo. Un optimizador que ignora las restricciones devuelve un resultado imposible; uno que las trata mal da un resultado que parece factible y no es óptimo.
- 🔗 **Se estudia junto con:** Lagrangiano, multiplicador de Lagrange, desigualdad, KKT.

📘 **Dónde se aprende** (1 clase): [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md).

### Concatenación

- La concatenación usa un código interno (aquí convolucional) y uno externo (RS).

💡 **Cómo se explica en la clase [B94-C02](../programa/clases/B94/B94-C02-entrelazado-y-concatenacion-de-codigos/CLASE.md):**
- Ejercicio 7 · autónomo. ¿Cuál es la tasa global de la concatenación convolucional + RS(255, 223)?
- Ejercicio 12 · integrador. Integrador. Elabora tu *tabla de resistencia a ráfagas por profundidad*: umbral, palabras recuperadas con `E·I` y `E·I + 1`, memoria y retardo por `I`, y el resultado de la concatenación; separa lo consultado de lo sintético.
- 🎯 **Por qué importa:** El decodificador de Viterbi falla en ráfagas y los desvanecimientos también. La decisión central: ¿qué profundidad de entrelazado hace falta para que una ráfaga de `B` octetos no sature ninguna palabra, y qué ganancia da frente a no entrelazar?
- 🔗 **Se estudia junto con:** entrelazado, código convolucional, algoritmo de Viterbi, decisión dura.

📘 **Dónde se aprende** (1 clase): [B94-C02 · Entrelazado y concatenación de códigos](../programa/clases/B94/B94-C02-entrelazado-y-concatenacion-de-codigos/CLASE.md).

### Concentración

- La concentración es `c = r₂₀₀/r_s`.
- La concentración `C = R80/R20` es el cociente entre los radios que contienen el 80 % y el 20 % de la luz.
- La concentración `C` es masa por volumen (mg/m³) o fracción de volumen (ppm).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- Si un ácido fuerte monoprótico tiene concentración `c`, `[H⁺] ≈ c` y `pH = −log₁₀ c`.
- Para `HA ⇌ H⁺ + A⁻` con `K_a` y concentración inicial `c`, si se ioniza `x`: `K_a = x²/(c − x)`, es decir, `x² + K_a x − K_a c = 0`, con solución `x = [−K_a + √(K_a² + 4K_a c)]/2`.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.
- 🔗 **Se estudia junto con:** disolución, soluto, disolvente, molaridad.

📘 **Dónde se aprende** (6 clases): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md); [B25-C15 · Materia oscura en galaxias](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md); [B117-C02 · Contención de riesgos biológicos y químicos en cabina](../programa/clases/B117/B117-C02-contencion-de-riesgos-biologicos-y-quimicos-en-cabina/CLASE.md); [B122-C01 · Dependencias de proveedores y cadena de suministro de infraestructura espacial](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md).

### Concentrador

- El concentrador reúne la luz en el absorbedor.

💡 **Cómo se explica en la clase [B78-C13](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md):**
- Calcular la potencia térmica captada por un colector concentrador.
- 🎯 **Por qué importa:** La energía llega por la óptica y el propelente solo la transporta; el escape depende de la temperatura que resistan los materiales y de la masa molar. La decisión central: ¿qué empuje e `Isp` da un colector de área dada y cómo se compara con un propulsor eléctrico alimentado con la misma potencia?
- 🔗 **Se estudia junto con:** eficiencia óptica, térmica, caudal, propulsor solar térmico.

📘 **Dónde se aprende** (1 clase): [B78-C13 · Propulsión solar térmica](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md).

### Concepción alternativa

- Una concepción alternativa es una idea previa que se opone a la explicación científica.

💡 **Cómo se explica en la clase [B131-C03](../programa/clases/B131/B131-C03-conocimientos-previos-y-concepciones-alternativas/CLASE.md):**
- python programa/clases/B131/B131-C03-conocimientos-previos-y-concepciones-alternativas/concepciones.py
- 🎯 **Por qué importa:** Enseñar sin saber qué creen ya los estudiantes deja intactas las ideas previas. La decisión central: ¿qué distractor elegiste para atrapar qué idea, y cómo sabrás si el cambio es real?
- 🔗 **Se estudia junto con:** distractor diagnóstico, ganancia normalizada, perihelio, afelio.

📘 **Dónde se aprende** (1 clase): [B131-C03 · Conocimientos previos y concepciones alternativas](../programa/clases/B131/B131-C03-conocimientos-previos-y-concepciones-alternativas/CLASE.md).

### Concepto

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C20](../programa/clases/B47/B47-C20-caso-comparativo-de-observatorios-espaciales/CLASE.md):**
- El concepto B gana con los pesos base y en la gran mayoría de los pesos aleatorios, pero eso depende de puntuaciones inventadas.
- C["conceptos A,B,C"] --> M["matriz ponderada"]
- 🎯 **Por qué importa:** Un ranking depende de los pesos elegidos. La decisión central: ¿qué conclusión sobrevive cuando los pesos cambian?
- 🔗 **Se estudia junto con:** banda espectral, década, límite de difracción, matriz de decisión.

📘 **Dónde se aprende** (1 clase): [B47-C20 · Caso comparativo de observatorios espaciales](../programa/clases/B47/B47-C20-caso-comparativo-de-observatorios-espaciales/CLASE.md).

### Conceptual

- Lo conceptual significa que no se analiza ni propone ningún diseño.

💡 **Cómo se explica en la clase [B78-C14](../programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md):**
- python programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/nuclear_termica.py
- 🎯 **Por qué importa:** Un cohete químico limita su `Isp` por la química del propelente; uno térmico lo limita por la temperatura que aguanta el núcleo. La decisión central: ¿cuánto `Isp` puede dar un gas de baja masa molar calentado a una temperatura dada y qué empuje corresponde a una potencia térmica?
- 🔗 **Se estudia junto con:** cohete térmico, núcleo, masa molar baja, temperatura del núcleo.

📘 **Dónde se aprende** (1 clase): [B78-C14 · Propulsión nuclear térmica conceptual](../programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md).

### Concesión

- La concesión es la habilitación estatal para operar un servicio.

💡 **Cómo se explica en la clase [B121-C04](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md):**
- La Ley 18.168 (General de Telecomunicaciones) exige concesión por decreto supremo para ciertos servicios; el contenido de sus artículos satelitales no se leyó (nivel 1).
- 5 Concesion de servicios de telecomunicaciones 1 S1 Ley 18.168 (por decreto supremo)
- 🎯 **Por qué importa:** Un marco nacional se conoce por sus instrumentos, y cada instrumento debe leerse en su texto vigente. La decisión central: ¿qué funciones regulatorias tienen un instrumento chileno identificado y con qué nivel de evidencia?
- 🔗 **Se estudia junto con:** nivel de evidencia, función regulatoria, instrumento, traducción no oficial.

📘 **Dónde se aprende** (1 clase): [B121-C04 · Marco legal espacial en Chile](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md).

### Concha anidada

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C05](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md):**
- Sumar el área efectiva de conchas anidadas.
- 🎯 **Por qué importa:** La reflexión rasante limita la energía y el área útil. La decisión central: ¿cuántas conchas y qué ángulos dan el área efectiva que se necesita a cada energía?
- 🔗 **Se estudia junto con:** reflexión rasante, ángulo crítico, geometría Wolter I, área efectiva.

📘 **Dónde se aprende** (1 clase): [B47-C05 · Instrumentos de rayos X](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md).

### Conciencia de la situación

- La conciencia de la situación es la comprensión del estado actual y su evolución (no se consultó una fuente concreta).

💡 **Contexto en la clase [B98-C04](../programa/clases/B98/B98-C04-interfaces-humano-robot-para-operacion-remota/CLASE.md):**
- 🎯 **Por qué importa:** Un operador que decide con un dato viejo sin saberlo comete errores; uno que recibe 24 alarmas por 3 fallos no ve la causa. La decisión central: ¿qué debe mostrar la interfaz para que el operador sepa qué tan viejo es lo que ve y qué es lo importante?
- 🔗 **Se estudia junto con:** edad del dato, pantalla cruda, pantalla predictiva, alarma dependiente.

📘 **Dónde se aprende** (1 clase): [B98-C04 · Interfaces humano-robot para operación remota](../programa/clases/B98/B98-C04-interfaces-humano-robot-para-operacion-remota/CLASE.md).

### Conciencia situacional

- En el marco de Endsley (1995), la conciencia situacional tiene tres niveles: percepción de los elementos relevantes, comprensión de su significado y proyección de su estado futuro.

💡 **Cómo se explica en la clase [B111-C04](../programa/clases/B111/B111-C04-conciencia-situacional-en-operaciones-de-vuelo/CLASE.md):**
- La evidencia es la ficha de conciencia situacional con intervalo de verificación del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de conciencia situacional con intervalo de verificación*: tabla de niveles, cobertura y acuerdo, curva de vigencia, intervalo para dos umbrales y límites.
- 🎯 **Por qué importa:** Falta la clase que trate la conciencia situacional de la tripulación. La decisión central: ¿cómo se cuantifica lo que el equipo sabe y cada cuánto debe verificarlo para que no se quede desactualizado?
- 🔗 **Se estudia junto con:** percepción, comprensión, proyección, puntuación tipo SAGAT.

📘 **Dónde se aprende** (1 clase): [B111-C04 · Conciencia situacional en operaciones de vuelo](../programa/clases/B111/B111-C04-conciencia-situacional-en-operaciones-de-vuelo/CLASE.md).

### Conciencia situacional espacial

- La conciencia situacional espacial es el conocimiento actualizado de qué objetos hay y dónde.

💡 **Cómo se explica en la clase [B119-C13](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md):**
- python programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/laboratorio.py
- 🎯 **Por qué importa:** El art. VI del Convenio de Registro prevé ayuda en la identificación mediante medios de rastreo; ninguna clase anterior muestra qué cubre un sensor ni cómo se criba un catálogo.
- 🔗 **Se estudia junto con:** paso, ángulo central, cribado, fuerza bruta.

📘 **Dónde se aprende** (1 clase): [B119-C13 · Vigilancia y conciencia situacional espacial](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md).

### Conclusión acotada

- Una conclusión acotada afirma solo lo que los datos permiten, con su incertidumbre y supuestos.

💡 **Cómo se explica en la clase [B01-C20](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md):**
- Una conclusión acotada tiene tres frases: lo que se midió («`h = 56,55° ± 0,20°`, `k = 2`, en [lugar] el [fecha]»), lo que se infiere con supuestos («compatible con `90° − |φ − δ|` si `δ = 0`») y lo que no se puede decir («no se puede afirmar que el modelo valga en otros días ni latitudes»).
- A --> C["Conclusión acotada (C05, C19)"]
- 🎯 **Por qué importa:** Entender el método no es lo mismo que aplicarlo. Cuando mides de verdad, aparecen problemas que los ejercicios no tienen: el cielo se nubla, el palo no está del todo vertical, la regla se mueve, los datos no coinciden con lo que predijiste.
- 🔗 **Se estudia junto con:** protocolo, bitácora, incidencia, criterio de rechazo de datos.

📘 **Dónde se aprende** (1 clase): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md).

### Concurrencia

- La concurrencia es gestionar varias tareas cuyo progreso se entrelaza en el tiempo (aunque haya un solo núcleo); el paralelismo es ejecutar varias a la vez en núcleos distintos.

💡 **Cómo se explica en la clase [B18-C01](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md):**
- Con un solo núcleo puedes tener concurrencia (la CPU alterna entre tareas) sin paralelismo.
- Con hilos de CPython sobre código Python puro tienes concurrencia, pero el paralelismo está limitado por el GIL (S1).
- 🎯 **Por qué importa:** Tienes ocho órbitas simuladas que propagar y un portátil con varios núcleos. La tentación es «lanzar ocho hilos y listo».
- 🔗 **Se estudia junto con:** proceso, hilo, comparten, paralelismo.

📘 **Dónde se aprende** (1 clase): [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md).

### Condensado

- El condensado es el agua que se recupera al enfriar el aire de la cámara.
- Carga latente: potencia por vapor. Condensado: agua líquida retirada.

💡 **Cómo se explica en la clase [B106-C07](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md):**
- Ejercicio 10 · transferencia. En microgravedad, ¿qué falla si el condensado no se separa?
- ⚠️ **Error frecuente:** Pensar que el condensado cae. En microgravedad no cae.
- 🎯 **Por qué importa:** Sin convección y con 4 personas, el vapor se acumula, sube la humedad relativa y se condensa en superficies frías. La decisión central: ¿cuánto vapor hay que retirar y con qué superficie fría, sin condensar sobre las paredes?
- 🔗 **Se estudia junto con:** Presión de saturación e_s(T), Humedad relativa, Punto de rocío, Relación de humedad w.

📘 **Dónde se aprende** (2 clases): [B106-C07 · Gestión de humedad](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md); [B115-C06 · Balance de agua y evapotranspiración en cultivos](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md).

### Condición

- Una condición es una expresión que da `True` o `False`.

💡 **Cómo se explica en la clase [B07-C04](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md):**
- Se evalúa cada condición en orden y solo se ejecuta la primera rama verdadera;
- Combinar condiciones con `and`, `or` y `not`.
- 🎯 **Por qué importa:** Toda clasificación astronómica es una decisión sobre un dato: ¿esta señal supera el ruido?, ¿esta estrella es más brillante que el umbral?, ¿esta imagen está saturada? Una decisión mal escrita no falla ruidosamente: clasifica mal en silencio, justo en los casos frontera, que son los que importan.
- 🔗 **Se estudia junto con:** condicional, rama, umbral, caso frontera.

📘 **Dónde se aprende** (1 clase): [B07-C04 · Condicionales y decisiones](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md).

### Condición CFL

- La condición CFL (de Courant, Friedrichs y Lewy) limita el paso de tiempo para que la información no cruce más de una celda por paso.
- La condición CFL limita `dt`.

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- *Descripción textual:* se parte de los promedios de celda; en cada interfaz se toman los estados de ambos lados; el solucionador de Riemann entrega el flujo en esa interfaz; cada celda se actualiza restando el flujo que sale y sumando el que entra; el paso de tiempo viene de la condición CFL y el ciclo se repite.
- Acotar el paso de tiempo con la condición CFL.
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.
- 🔗 **Se estudia junto con:** ley de conservación, vector de estado conservado, flujo, celda.

📘 **Dónde se aprende** (2 clases): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md); [B30-C09 · Magnetohidrodinámica](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md).

### Condición de acotamiento

- La condición de acotamiento es `ẏ0 = −2 n x0`.

💡 **Cómo se explica en la clase [B76-C09](../programa/clases/B76/B76-C09-dinamica-relativa-de-hill-clohessy-wiltshire/CLASE.md):**
- *Descripción textual:* del movimiento medio y el estado inicial sale la solución cerrada; de ella, la condición de acotamiento y la deriva; la comparación con la integración no lineal da el error de validez.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de validez de HCW*: tabla de error para tres separaciones y dos duraciones, condición de acotamiento y límites, con fuentes.
- ⚠️ **Error frecuente:** Olvidar la condición de acotamiento. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un controlador de encuentro necesita predecir dónde estará la otra nave sin integrar dos cuerpos cada vez. La decisión central: ¿hasta qué distancia y durante cuánto tiempo es válida la solución lineal de HCW, y qué movimientos son acotados?
- 🔗 **Se estudia junto con:** ecuaciones de HCW, error de HCW.

📘 **Dónde se aprende** (1 clase): [B76-C09 · Dinámica relativa de Hill-Clohessy-Wiltshire](../programa/clases/B76/B76-C09-dinamica-relativa-de-hill-clohessy-wiltshire/CLASE.md).

### Condición de ángulo

- La condición de ángulo pide `arg P(s) = 180°` (mod 360°) en cada punto del lugar; la condición de módulo da `K = 1/|P(s)|`.

💡 **Cómo se explica en la clase [B16-C09](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md):**
- Definir el lugar de las raíces y la condición de ángulo.
- Verificar numéricamente el lugar con invariantes (suma de raíces, condición de ángulo).
- 🎯 **Por qué importa:** Subir la ganancia de un lazo hace que responda más rápido, pero también más oscilante, hasta que se desestabiliza. Para decidir cuánta ganancia usar necesitas ver el compromiso de un vistazo.
- 🔗 **Se estudia junto con:** lugar de las raíces, parten, terminan, asíntotas.

📘 **Dónde se aprende** (1 clase): [B16-C09 · Lugar de las raíces](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md).

### Condición de carrera

- Una condición de carrera es un resultado que depende del orden, no controlado, en que varios hilos tocan un dato compartido.

💡 **Cómo se explica en la clase [B18-C01](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md):**
- Reconocer y corregir una condición de carrera con un cerrojo.
- Es una condición de carrera (sección 8.5).
- 🎯 **Por qué importa:** Tienes ocho órbitas simuladas que propagar y un portátil con varios núcleos. La tentación es «lanzar ocho hilos y listo».
- 🔗 **Se estudia junto con:** proceso, hilo, comparten, concurrencia.

📘 **Dónde se aprende** (1 clase): [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md).

### Condición de contorno

- Una condición inicial fija `u` (y `u_t` en la onda) en `t = 0`; una condición de contorno (o de frontera) fija `u` o su derivada en los bordes.

💡 **Cómo se explica en la clase [B11-C13](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md):**
- B -->|"= 0"| C["Parabólica<br/>calor: difunde y suaviza<br/>1 condición inicial + contorno"]
- B -->|"> 0"| D["Hiperbólica<br/>onda: viaja a velocidad c<br/>2 condiciones iniciales + contorno"]
- 🎯 **Por qué importa:** El calor que atraviesa un escudo, las ondas en una estructura, el potencial gravitatorio de un cuerpo extenso, el transporte de partículas en un plasma: todos son EDP. Antes de discretizar hay que saber *qué tipo de problema es* (qué datos pide, cómo viaja la información) porque de ello depende el método.
- 🔗 **Se estudia junto con:** EDP, parabólica, hiperbólica, elíptica.

📘 **Dónde se aprende** (1 clase): [B11-C13 · Ecuaciones en derivadas parciales](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md).

### Condición de energía débil

- La condición de energía débil pide `ρ ≥ 0` y `ρ + p ≥ 0`; la dominante, `ρ ≥ |p|`; la fuerte, `ρ + 3p ≥ 0`.

💡 **Contexto en la clase [B39-C04](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md):**
- **Idea central (modelo mental):** Como el inventario de una caja: cuánta energía hay, cómo fluye y cuánta presión ejerce, expresado de modo que no dependa del observador.
- 🎯 **Por qué importa:** La fuente de la gravedad es `T^ab`. La decisión central: ¿qué tensor describe la materia y qué condiciones debe cumplir para ser físicamente razonable?
- 🔗 **Se estudia junto con:** fluido perfecto, densidad, presión, parámetro.

📘 **Dónde se aprende** (1 clase): [B39-C04 · Tensor de energía-momento y fuentes de curvatura](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md).

### Condición de módulo

- La condición de ángulo pide `arg P(s) = 180°` (mod 360°) en cada punto del lugar; la condición de módulo da `K = 1/|P(s)|`.

💡 **Contexto en la clase [B16-C09](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md):**
- **Idea central (modelo mental):** Con `K = 0`, los polos del lazo cerrado son los de `L` (0, −1, −2). Al subir `K`, se desplazan: los dos primeros se acercan, se encuentran y salen hacia el plano complejo; el tercero se aleja por el eje real negativo. A cierta `K`, el par complejo cruza el eje imaginario.
- 🎯 **Por qué importa:** Subir la ganancia de un lazo hace que responda más rápido, pero también más oscilante, hasta que se desestabiliza. Para decidir cuánta ganancia usar necesitas ver el compromiso de un vistazo.
- 🔗 **Se estudia junto con:** lugar de las raíces, parten, terminan, asíntotas.

📘 **Dónde se aprende** (1 clase): [B16-C09 · Lugar de las raíces](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md).

### Condición de pared

- La condición de pared fija `v = 0`.

💡 **Contexto en la clase [B35-C10](../programa/clases/B35/B35-C10-condiciones-de-frontera-en-modelos-mhd/CLASE.md):**
- **Idea central (modelo mental):** Una frontera rígida devuelve un eco; una frontera que absorbe como un acantilado de arena deja pasar el sonido sin eco. En un modelo, el eco es una onda falsa que contamina la solución.
- 🎯 **Por qué importa:** Las fronteras de los modelos heliosféricos deben dejar salir las ondas. La decisión central: ¿refleja la frontera la onda y con qué signo y amplitud?
- 🔗 **Se estudia junto con:** gradiente nulo, característica saliente, coeficiente de reflexión, malla escalonada.

📘 **Dónde se aprende** (1 clase): [B35-C10 · Condiciones de frontera en modelos MHD](../programa/clases/B35/B35-C10-condiciones-de-frontera-en-modelos-mhd/CLASE.md).

### Condición de precisión intermedia

- Una condición de precisión intermedia mantiene el procedimiento y el lugar pero permite cambios durante un periodo largo, como nuevas calibraciones u operadores (S1, 2.22).

💡 **Cómo se explica en la clase [B13-C14](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md):**
- Definir condiciones de repetibilidad, de precisión intermedia y de reproducibilidad.
- 🎯 **Por qué importa:** Ocho estaciones de seguimiento miden el mismo desfase de un reloj de referencia. Cada una repite su medida cinco veces y obtiene resultados muy parecidos entre sí, pero las estaciones discrepan entre ellas.
- 🔗 **Se estudia junto con:** condición de repetibilidad, condición de reproducibilidad, desviación de repetibilidad s_r, desviación de reproducibilidad s_R.

📘 **Dónde se aprende** (1 clase): [B13-C14 · Repetibilidad y reproducibilidad](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md).

### Condición de repetibilidad

- Una condición de repetibilidad incluye el mismo procedimiento, los mismos operadores, el mismo sistema de medida, las mismas condiciones y el mismo lugar, con medidas repetidas sobre el mismo objeto en un periodo corto (S1, 2.20).

💡 **Cómo se explica en la clase [B13-C14](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md):**
- Definir condiciones de repetibilidad, de precisión intermedia y de reproducibilidad.
- En condiciones de repetibilidad (S1, 2.20).
- 🎯 **Por qué importa:** Ocho estaciones de seguimiento miden el mismo desfase de un reloj de referencia. Cada una repite su medida cinco veces y obtiene resultados muy parecidos entre sí, pero las estaciones discrepan entre ellas.
- 🔗 **Se estudia junto con:** condición de precisión intermedia, condición de reproducibilidad, desviación de repetibilidad s_r, desviación de reproducibilidad s_R.

📘 **Dónde se aprende** (1 clase): [B13-C14 · Repetibilidad y reproducibilidad](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md).

### Condición de reproducibilidad

- Una condición de reproducibilidad incluye lugares, operadores y sistemas de medida distintos (S1, 2.24).

💡 **Cómo se explica en la clase [B13-C14](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md):**
- Definir condiciones de repetibilidad, de precisión intermedia y de reproducibilidad.
- 🎯 **Por qué importa:** Ocho estaciones de seguimiento miden el mismo desfase de un reloj de referencia. Cada una repite su medida cinco veces y obtiene resultados muy parecidos entre sí, pero las estaciones discrepan entre ellas.
- 🔗 **Se estudia junto con:** condición de repetibilidad, condición de precisión intermedia, desviación de repetibilidad s_r, desviación de reproducibilidad s_R.

📘 **Dónde se aprende** (1 clase): [B13-C14 · Repetibilidad y reproducibilidad](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md).

### Condición inicial

- Una condición inicial es un dato (por ejemplo, `v(0) = 0`) que fija `C`.
- Una condición inicial fija `u` (y `u_t` en la onda) en `t = 0`; una condición de contorno (o de frontera) fija `u` o su derivada en los bordes.
- Una condición inicial fija el valor de la función (y de su derivada, si hace falta) en `t = 0`.

💡 **Cómo se explica en la clase [B09-C08](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md):**
- *Descripción textual:* derivar baja de posición a velocidad a aceleración; integrar sube en sentido contrario y cada subida añade una constante que se fija con una condición inicial.
- Fijar la constante con condiciones iniciales.
- 🎯 **Por qué importa:** Un acelerómetro mide aceleración; lo que se necesita es velocidad y posición. Una gravedad `g(r)` se conoce; lo que decide si una sonda escapa es la energía, que sale de «deshacer» esa derivada.
- 🔗 **Se estudia junto con:** antiderivada, integral indefinida, constante de integración, potencial gravitatorio.

📘 **Dónde se aprende** (3 clases): [B09-C08 · Integrales indefinidas](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md); [B11-C13 · Ecuaciones en derivadas parciales](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md); [B17-C03 · Redes neuronales informadas por la física (PINN)](../programa/clases/B17/B17-C03-redes-neuronales-informadas-por-la-fisica-pinn/CLASE.md).

### Condición latente

- Una condición latente común multiplica las `q` por `k`.

💡 **Cómo se explica en la clase [B111-C06](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md):**
- Con probabilidad `c = 0,10` la condición latente está presente y cada `q` se multiplica por `k = 3` (tope 1): `P = 0,90 × 1,5 × 10⁻⁵ + 0,10 × (0,3 × 0,15 × 0,6 × 0,3 × 0,45) = 1,35 × 10⁻⁵ + 3,645 × 10⁻⁴ = 3,780 × 10⁻⁴`.
- Reducir una condición latente compartida vale más que mejorar una sola barrera; el reporte sin represalia revela las barreras ya perforadas; y culpar a la persona no cambia las condiciones.
- 🎯 **Por qué importa:** Falta la clase sobre tipos de error, barreras y reporte. La decisión central: ¿dónde se pone el esfuerzo: en culpar al que erró o en reforzar las barreras y las condiciones que dejaron pasar el error?
- 🔗 **Se estudia junto con:** resbalón, descuido, equivocación, violación.

📘 **Dónde se aprende** (1 clase): [B111-C06 · Gestión del error humano y cultura de seguridad](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md).

### Condición necesaria

- Una condición necesaria debe cumplirse, pero no basta.

💡 **Cómo se explica en la clase [B54-C20](../programa/clases/B54/B54-C20-comparacion-de-habitabilidad-climatica/CLASE.md):**
- AND --> LIM["condición necesaria, no habitabilidad"]
- *Descripción textual:* los datos de fichas dan la tabla; las condiciones de temperatura y presión se combinan en una condición necesaria que no es habitabilidad.
- ⚠️ **Error frecuente:** Tratar una condición necesaria como suficiente. Se corrige con 8.3.
- 🎯 **Por qué importa:** Comparar mundos tienta a ordenarlos por «habitabilidad». La pregunta motivadora: ¿qué dicen realmente la temperatura y la presión de superficie sobre la posibilidad de agua líquida?
- 🔗 **Se estudia junto con:** instalación relativa, efecto atmosférico, zona habitable, agua líquida en superficie.

📘 **Dónde se aprende** (1 clase): [B54-C20 · Comparación de habitabilidad climática](../programa/clases/B54/B54-C20-comparacion-de-habitabilidad-climatica/CLASE.md).

### Condición sin deriva

- La condición sin deriva es `v_y = −2 n x`.

💡 **Cómo se explica en la clase [B97-C11](../programa/clases/B97/B97-C11-robots-de-inspeccion-orbital/CLASE.md):**
- Sin la condición `v_y = −2 n x₀`, el término secular `6(sin nt − nt) x₀` produciría una deriva de `3770` m a lo largo de la traza tras una órbita.
- *Descripción textual:* de `GM` y la altitud sale `n`; la solución CW con la condición sin deriva da una elipse cerrada; la integración RK4 la verifica.
- 🎯 **Por qué importa:** Una inspección segura se diseña de modo que, si falla el empuje, el robot no se acerque ni se aleje: la elipse sin deriva lo garantiza. Con una condición inicial mal elegida, el robot se aleja decenas de veces la distancia deseada en una órbita.
- 🔗 **Se estudia junto con:** movimiento relativo, ecuaciones de Clohessy–Wiltshire (CW), sistema local (LVLH), órbita de inspección.

📘 **Dónde se aprende** (1 clase): [B97-C11 · Robots de inspección orbital](../programa/clases/B97/B97-C11-robots-de-inspeccion-orbital/CLASE.md).

### Condicionado

- ADM son armas de destrucción masiva. Condicionado significa permitido solo con el propósito científico o pacífico.

💡 **Cómo se explica en la clase [B119-C11](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md):**
- ADM en órbita: prohibido; base militar en la Luna: prohibido; científicos militares en la Luna: condicionado; telescopio civil en un asteroide: permitido; satélite de observación en órbita: fuera del art.
- *Descripción textual:* primero se pregunta por armas de destrucción masiva; luego por el cuerpo celeste; por último por bases o ensayos; el resultado puede ser prohibido, condicionado, permitido o fuera del artículo.
- 🎯 **Por qué importa:** C01 reduce el art. IV a una regla booleana; esta clase lo desagrega por ubicación y propósito y conecta con el art. 3 del Acuerdo sobre la Luna, y deja explícito lo no consultado.
- 🔗 **Se estudia junto con:** ADM, Fuera del art. IV, cuerpo celeste, lista de reglas.

📘 **Dónde se aprende** (1 clase): [B119-C11 · Uso pacífico y limitaciones militares](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md).

### Condicional

- Un condicional es una instrucción que ejecuta un bloque solo si se cumple una condición.

💡 **Cómo se explica en la clase [B07-C04](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md):**
- Otra es la expresión condicional `"grande" if d > 20_000 else "pequeño"`, compacta pero menos legible si hay más de dos ramas.
- python programa/clases/B07/B07-C04-condicionales-y-decisiones/clasificar_planetas.py
- 🎯 **Por qué importa:** Toda clasificación astronómica es una decisión sobre un dato: ¿esta señal supera el ruido?, ¿esta estrella es más brillante que el umbral?, ¿esta imagen está saturada? Una decisión mal escrita no falla ruidosamente: clasifica mal en silencio, justo en los casos frontera, que son los que importan.
- 🔗 **Se estudia junto con:** condición, rama, umbral, caso frontera.

📘 **Dónde se aprende** (1 clase): [B07-C04 · Condicionales y decisiones](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md).

### Condicionamiento

- El condicionamiento mide cuánto amplifica el problema una perturbación de la entrada.
- El condicionamiento crece: el radio espectral de `D²` interior sube como `N⁴`.

💡 **Cómo se explica en la clase [B11-C24](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md):**
- Con `N > 24` el error sube un poco por el redondeo (condicionamiento).
- Estimar el costo en condicionamiento (`ρ(D²) ∝ N⁴`).
- ⚠️ **Error frecuente:** Ignorar el condicionamiento al elegir el paso de tiempo. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Cuando la solución es suave, un método espectral reduce un problema que necesita miles de puntos con diferencias a una docena con Chebyshev. Pero tiene un costo: el paso máximo estable de un esquema explícito baja como `1/N⁴`, y funciona mal si la solución no es suave.
- 🔗 **Se estudia junto con:** nodos de Chebyshev–Gauss–Lobatto, matriz de diferenciación, colocación, convergencia exponencial.

📘 **Dónde se aprende** (2 clases): [B11-C24 · Métodos espectrales avanzados (Chebyshev y Fourier)](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md); [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md).

### Condiciones críticas

- Las condiciones críticas (rotular lo sintético, no dar asesoría, citar solo lo consultado) no se compensan.

💡 **Cómo se explica en la clase [B124-C20](../programa/clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md):**
- P2 tiene todos los criterios en nivel 4 (`100,0`) pero no cumple la segunda condición crítica; su categoría es «no logrado».
- Esto es lo que significa que las condiciones críticas no se compensan con el promedio.
- 🎯 **Por qué importa:** Un portafolio con una nota promedio alta puede ocultar una falta grave, como presentar datos inventados como reales. La decisión central: ¿qué hace falta para declarar logrado un portafolio y cómo se sabe que dos revisores miden lo mismo?
- 🔗 **Se estudia junto con:** rúbrica, puntaje, kappa de Cohen, kappa ponderado.

📘 **Dónde se aprende** (1 clase): [B124-C20 · Proyecto integrador y portafolio profesional](../programa/clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md).

### Condiciones de contorno

- Las condiciones de contorno eliminan los GDL fijos.

💡 **Contexto en la clase [B84-C12](../programa/clases/B84/B84-C12-analisis-de-elementos-finitos/CLASE.md):**
- 🎯 **Por qué importa:** Un modelo que da un resultado no es un modelo correcto: la verificación contra una solución conocida es lo que lo convierte en una herramienta. La decisión central: ¿cómo demuestras que un modelo de elementos finitos resuelve bien las ecuaciones que dice resolver?
- 🔗 **Se estudia junto con:** rigidez de elemento, ensamblaje, prueba del parche, orden de convergencia.

📘 **Dónde se aprende** (1 clase): [B84-C12 · Análisis de elementos finitos](../programa/clases/B84/B84-C12-analisis-de-elementos-finitos/CLASE.md).

### Condiciones de frontera

- Las condiciones de frontera se obtienen evaluando `T*` (Dirichlet) o `T*_z` (Neumann) en el borde.

💡 **Cómo se explica en la clase [B23-C04](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md):**
- A["Elegir T*(z,t)<br/>suave y conocida"] --> B["Derivar s = T*_t - κ T*_zz<br/>y las condiciones de frontera"]
- Fabricar una solución, derivar a mano su fuente y sus condiciones de frontera.
- 🎯 **Por qué importa:** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.
- 🔗 **Se estudia junto con:** solución fabricada, término fuente, estudio de refinamiento, nodo fantasma.

📘 **Dónde se aprende** (1 clase): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md).

### Condiciones de Rankine–Hugoniot

- Las condiciones de Rankine–Hugoniot son las leyes de conservación a ambos lados.

💡 **Contexto en la clase [B30-C14](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md):**
- **Idea central (modelo mental):** Una pelota que rebota entre dos paredes que se acercan gana energía en cada rebote, pero cada vez puede escapar: la combinación de ganancia y escape da una ley de potencias.
- 🎯 **Por qué importa:** Las partículas energéticas solares son un riesgo para satélites y astronautas, y los choques de las CME son un origen. La decisión central: ¿qué espectro produce un choque de una compresión dada?
- 🔗 **Se estudia junto con:** choque, razón de compresión, aceleración difusiva, índice espectral.

📘 **Dónde se aprende** (1 clase): [B30-C14 · Choques y aceleración de partículas](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md).

### Condiciones KKT

- Las condiciones KKT de un QP con restricciones de igualdad `A z = b` y coste `½ zᵀHz` son `H z + Aᵀλ = 0` y `A z = b`.

💡 **Cómo se explica en la clase [B81-C03](../programa/clases/B81/B81-C03-metodos-directos-de-transcripcion/CLASE.md):**
- Con `N` tramos hay `3(N+1)` variables (`x`, `v`, `u` en cada nodo) y `2N + 4` restricciones (dos defectos por tramo más las cuatro condiciones de contorno).
- Porque `A` fija `x` y `v` a partir de `u` y las condiciones de contorno; el núcleo de `H` no intersecta el de `A`.
- ⚠️ **Error frecuente:** Olvidar las condiciones de contorno al contar restricciones. Se corrige con 8.1.
- 🎯 **Por qué importa:** Los métodos directos son los más usados cuando no se tiene un buen punto de partida y hay muchas restricciones. La decisión central: ¿cuántos nodos hacen falta y a qué velocidad converge el coste discreto al continuo?
- 🔗 **Se estudia junto con:** colocación trapezoidal, defecto, orden.

📘 **Dónde se aprende** (1 clase): [B81-C03 · Métodos directos de transcripción](../programa/clases/B81/B81-C03-metodos-directos-de-transcripcion/CLASE.md).

### Condiciones totales

- Las condiciones totales o de remanso (`T₀`, `p₀`, `ρ₀`) son las que se alcanzarían al frenar el flujo sin pérdidas.

💡 **Cómo se explica en la clase [B79-C05](../programa/clases/B79/B79-C05-dinamica-de-fluidos-compresibles/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir condiciones totales y estáticas. Se corrige con el vocabulario.
- 🎯 **Por qué importa:** B77-C03 trata fuerzas aerodinámicas sin flujo compresible; en propulsión la densidad varía mucho y sin este modelo no se pueden calcular toberas ni tomas de aire. La decisión central: ¿a partir de qué Mach no puedo tratar el gas como incompresible, y qué relación uso entonces?
- 🔗 **Se estudia junto con:** número de Mach, relaciones isentrópicas, entalpía total.

📘 **Dónde se aprende** (1 clase): [B79-C05 · Dinámica de fluidos compresibles](../programa/clases/B79/B79-C05-dinamica-de-fluidos-compresibles/CLASE.md).

### Condrita

- Una condrita es un meteorito formado por materiales que no se fundieron del todo; las condritas carbonáceas son ricas en carbono, y las CI son las más primitivas en cuanto a su composición.

💡 **Cómo se explica en la clase [B06-C20](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md):**
- El litio es el caso contrario: `Δ = −2,21` (el Sol tiene 0,006 veces el litio relativo al silicio de las condritas);
- Explicar qué es una condrita CI y por qué sirve como referencia de composición.
- 🎯 **Por qué importa:** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.
- 🔗 **Se estudia junto con:** meteorito, condritas carbonáceas, CI, dex.

📘 **Dónde se aprende** (1 clase): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### Condritas carbonáceas

- Una condrita es un meteorito formado por materiales que no se fundieron del todo; las condritas carbonáceas son ricas en carbono, y las CI son las más primitivas en cuanto a su composición.

💡 **Contexto en la clase [B06-C20](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md):**
- **Idea central (modelo mental):** Imagina dos termómetros independientes que miden la misma habitación: uno apunta a la luz que llega de ella (la fotosfera) y otro entra al cuarto a tomar muestras (el meteorito). Si coinciden, confías en la medida.
- 🎯 **Por qué importa:** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.
- 🔗 **Se estudia junto con:** meteorito, condrita, CI, dex.

📘 **Dónde se aprende** (1 clase): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### Conducción

- La conducción `Q = (A/L)∫k dT`.
- La conducción cumple `q = k dT/dz`.
- La conducción transfiere calor por contacto entre partículas.

💡 **Cómo se explica en la clase [B47-C13](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md):**
- Con muchos escudos la conducción por los soportes (8,25 mW) pasa a ser un tercio de la carga.
- *Descripción textual:* la radiación entre escudos y la conducción por soportes suman una carga que consume el criógeno.
- ⚠️ **Error frecuente:** Ignorar la conducción por soportes. Se corrige con 8.3.
- 🎯 **Por qué importa:** Cada vatio parásito acorta la vida de un criógeno. La decisión central: ¿cuántos escudos y qué soportes bastan para una vida útil dada?
- 🔗 **Se estudia junto con:** escudo radiativo, aislamiento multicapa, emisividad, criógeno.

📘 **Dónde se aprende** (3 clases): [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md); [B53-C14 · Geología de Europa](../programa/clases/B53/B53-C14-geologia-de-europa/CLASE.md); [B85-C02 · Conducción térmica en estructuras](../programa/clases/B85/B85-C02-conduccion-termica-en-estructuras/CLASE.md).

### Conductancia

- La capacidad térmica `C` y la conductancia `G` describen la masa y el aislamiento.

💡 **Cómo se explica en la clase [B44-C08](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md):**
- Datos: `k_B` de NIST CODATA 2022 (consultada el 2026-11-09); capacidad, conductancia y potencia ilustrativas.
- 🎯 **Por qué importa:** La cámara no está fría al encenderla. La decisión central: ¿cuánto hay que esperar antes de calibrar y qué temperatura final se alcanza?
- 🔗 **Se estudia junto con:** capacidad térmica, potencia de enfriamiento, constante de tiempo, temperatura límite.

📘 **Dónde se aprende** (2 clases): [B33-C07 · Impactos del clima espacial en redes eléctricas](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md); [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md).

### Conductancia de Pedersen

- La conductancia de Pedersen (a lo largo de `E`) y la de Hall (perpendicular).

💡 **Contexto en la clase [B30-C17](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md):**
- **Idea central (modelo mental):** La precipitación es como una lluvia que moja una capa a cierta altura: cuanto más energético el electrón, más profundo llega; la capa de Chapman describe dónde se concentra la ionización.
- 🎯 **Por qué importa:** La aurora y las corrientes ionosféricas son la parte visible y eléctrica del acoplamiento entre la magnetosfera y la atmósfera. La decisión central: ¿dónde se produce la ionización y cuánta energía se disipa por efecto Joule?
- 🔗 **Se estudia junto con:** capa de Chapman, altura de escala, ángulo cenital, de Hall.

📘 **Dónde se aprende** (1 clase): [B30-C17 · Auroras y corrientes ionosféricas](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md).

### Conductividad eléctrica (EC)

- La conductividad eléctrica (EC) es una medida global de las sales.

💡 **Contexto en la clase [B115-C03](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md):**
- 🎯 **Por qué importa:** Una solución nutritiva que se repone «por conductividad» puede parecer estable y estar desequilibrada. La decisión central: ¿qué se mide, cada cuánto y qué se repone para que cada ion se mantenga cerca de su objetivo, y cuándo conviene renovar la solución?
- 🔗 **Se estudia junto con:** solución nutritiva, macronutrientes, micronutrientes, solución madre.

📘 **Dónde se aprende** (1 clase): [B115-C03 · Control de nutrientes y solución nutritiva](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md).

### Conductividad integral

- La conductividad integral `∫k dT` da el flujo por soporte `Q = (A/L)∫k dT`.

💡 **Contexto en la clase [B85-C17](../programa/clases/B85/B85-C17-criogenia-de-instrumentos/CLASE.md):**
- 🎯 **Por qué importa:** Cada vatio parásito a `80 K` cuesta decenas de vatios eléctricos. La decisión central: ¿qué carga parásita llega a la punta fría, cuánta potencia eléctrica cuesta quitarla y cuánto tarda el enfriamiento?
- 🔗 **Se estudia junto con:** carga parásita, fracción de Carnot, capacidad térmica.

📘 **Dónde se aprende** (1 clase): [B85-C17 · Criogenia de instrumentos](../programa/clases/B85/B85-C17-criogenia-de-instrumentos/CLASE.md).

### Conectividad 4

- Una región conectada es un conjunto de píxeles de objeto unidos por vecindad; la conectividad 4 une píxeles que comparten un lado, la 8 también los que comparten una esquina (S1 describe cómo `scipy.ndimage.label` usa por defecto la cruz de 4 vecinos y cómo pedir 8).

💡 **Cómo se explica en la clase [B15-C13](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md):**
- Con conectividad 4, dos píxeles en diagonal son dos regiones; con conectividad 8, una.
- El laboratorio verifica ese conteo, y que un etiquetador propio (búsqueda en anchura) coincide con `scipy.ndimage.label` en una imagen aleatoria de 60 × 60: 335 regiones con conectividad 4 y 33 con 8.
- ⚠️ **Error frecuente:** No declarar la conectividad. Se corrige con los ejercicios 1 y 11.
- 🎯 **Por qué importa:** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.
- 🔗 **Se estudia junto con:** segmentación, umbralización, método de Otsu, varianza entre clases.

📘 **Dónde se aprende** (1 clase): [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md).

### Conexión de Levi-Civita

- La conexión de Levi-Civita es la única sin torsión y compatible con la métrica.

💡 **Cómo se explica en la clase [B39-C02](../programa/clases/B39/B39-C02-conexion-afin-y-simbolos-de-christoffel/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué hace falta para una conexión distinta de Levi-Civita?
- 🎯 **Por qué importa:** Sin conexión no hay aceleración ni geodésicas. La decisión central: ¿qué símbolos produce una métrica y qué propiedades garantizan que sea la conexión correcta?
- 🔗 **Se estudia junto con:** símbolos de Christoffel, derivada covariante, geodésica, compatibilidad métrica.

📘 **Dónde se aprende** (1 clase): [B39-C02 · Conexión afín y símbolos de Christoffel](../programa/clases/B39/B39-C02-conexion-afin-y-simbolos-de-christoffel/CLASE.md).

### Conexión de salto

- Una conexión de salto copia detalles del camino que contrae al que expande.

💡 **Cómo se explica en la clase [B17-C11](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md):**
- Una U-Net apila muchas capas convolucionales (con no linealidades), reduce la resolución con agrupaciones, la restituye con ampliaciones y une las dos ramas con conexiones de salto (S1).
- *Descripción textual:* la imagen pasa por convoluciones que miran el entorno, se reduce la resolución para ganar contexto y luego se aumenta para recuperar el detalle; una conexión de salto lleva detalle fino del primer tramo al segundo; el resultado es una probabilidad por píxel, que con un umbral de 0,5 da la máscara.
- 🎯 **Por qué importa:** Delimitar una mancha solar, una nube o un cráter a mano en miles de imágenes no escala. Un umbral por píxel falla cuando el ruido es comparable al contraste.
- 🔗 **Se estudia junto con:** segmentación semántica, máscara, convolución, válido.

📘 **Dónde se aprende** (1 clase): [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md).

### Confiabilidad

- La confiabilidad `R(t)` es la probabilidad de funcionar hasta `t`.
- La confiabilidad `R(t)`.
- Confiabilidad `R(t)`: probabilidad de sobrevivir hasta `t`.

💡 **Cómo se explica en la clase [B47-C19](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md):**
- Con tasas ilustrativas, la confiabilidad del sistema a 5 años es `0,6469` (Monte Carlo `0,6472`), baja a `0,8` en `3,24 años`; el propulsor dura `17,3 años` y la potencia llega al 70 % en `14,1 años`.
- Descripción larga: la confiabilidad es el recurso limitante.
- 🎯 **Por qué importa:** No sirve duplicar un equipo si otro componente falla antes. La decisión central: ¿qué recurso limita la vida de la misión y qué redundancia vale la pena?
- 🔗 **Se estudia junto con:** tasa de falla, redundancia, curva de la bañera, propulsor.

📘 **Dónde se aprende** (3 clases): [B47-C19 · Mantenimiento y vida útil](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md); [B48-C14 · Mantenimiento preventivo](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md); [B83-C23 · Redundancia y tolerancia a fallos de misión](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md).

### Confianza

- La confianza de un clasificador es la probabilidad máxima que asigna.
- La confianza `C` es la probabilidad de capturarla al menos una vez.
- La confianza es la probabilidad de que los repuestos cubran las fallas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B17-C07](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md):**
- Y la confianza media del modelo *subió* de 0,842 a 0,867: con más ruido, los puntos se alejan de la frontera y la regresión logística responde con más seguridad.
- La confianza no es una alarma fiable aquí (S2 describe una línea base basada en ella; este ejemplo muestra un caso en que no basta).
- ⚠️ **Error frecuente:** Fiarse de la confianza del modelo. Ejercicio 7.
- 🎯 **Por qué importa:** Un modelo se entrena con un catálogo y se despliega sobre otro: otro telescopio, otra época, otro brillo límite. Su exactitud medida en validación cruzada deja de valer, y el modelo no avisa: responde con la misma seguridad.
- 🔗 **Se estudia junto con:** distribución de entrenamiento, despliegue, cambio de covariables, cambio de prevalencia.

📘 **Dónde se aprende** (4 clases): [B17-C07 · Validación fuera de distribución](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md); [B63-C02 · Muestreo superficial y estrategias de recolección](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md); [B97-C12 · Robots de mantenimiento](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md); [B106-C28 · Monitoreo microbiológico de agua y superficies del hábitat](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md).

### Confianza de misión

- La confianza de misión es la probabilidad de no quedarse sin repuestos en ningún intervalo.

💡 **Cómo se explica en la clase [B97-C19](../programa/clases/B97/B97-C19-logistica-de-piezas-y-reparaciones/CLASE.md):**
- Para cada tipo se elige el menor `s` con `P(X ≤ s) ≥ q`, `q = 0,95^(1/(3k))`: la confianza de misión es el producto sobre intervalos y tipos.
- La misión completa simulada con ese plan (`100 000` repeticiones, semilla fija) da `0,9663` de éxito, a `1,99` desviaciones de la confianza analítica.
- ⚠️ **Error frecuente:** Exigir 95 % por intervalo y tipo. La confianza de misión es un producto (8.2)
- 🎯 **Por qué importa:** Un stock grande cuesta masa inicial; reabastecer a menudo cuesta vuelos. El mínimo está en un punto intermedio que solo aparece al calcular ambos efectos con la misma confianza de misión.
- 🔗 **Se estudia junto con:** stock inicial, intervalo de reabastecimiento, consumo.

📘 **Dónde se aprende** (1 clase): [B97-C19 · Logística de piezas y reparaciones](../programa/clases/B97/B97-C19-logistica-de-piezas-y-reparaciones/CLASE.md).

### Confidencialidad

- La confidencialidad se tramita con petición razonada (art. 17) y las audiencias son a puerta cerrada salvo acuerdo (art. 28(3)).

💡 **Cómo se explica en la clase [B123-C04](../programa/clases/B123/B123-C04-arbitraje-y-resolucion-de-controversias-espaciales/CLASE.md):**
- La confidencialidad se solicita con razones y puede haber un asesor de confidencialidad (art. 17).
- *Descripción textual:* una controversia puede seguir la negociación, la comisión del Convenio o el arbitraje; en el arbitraje se pactan el tribunal, las medidas provisionales y la confidencialidad.
- 🎯 **Por qué importa:** Elegir la vía condiciona plazo, costo, confidencialidad y fuerza obligatoria de la decisión. La decisión central: ¿qué vía y qué reglas conviene pactar, y con qué compromisos?
- 🔗 **Se estudia junto con:** Reglas Opcionales, Secretario General de la CPA, medida provisional, peritos.

📘 **Dónde se aprende** (1 clase): [B123-C04 · Arbitraje y resolución de controversias espaciales](../programa/clases/B123/B123-C04-arbitraje-y-resolucion-de-controversias-espaciales/CLASE.md).

### Configuración

- Una configuración es el conjunto completo de entradas (constantes, estado inicial, duración, método, pasos).

💡 **Cómo se explica en la clase [B11-C20](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md):**
- Con una configuración inmutable, «qué se corrió» queda definido por un objeto.
- La huella se calcula sobre el JSON ordenado de la configuración y las posiciones y velocidades redondeadas a `10⁻⁶` en cada paso.
- ⚠️ **Error frecuente:** Dejar entradas fuera de la configuración. Se corrige con el ejercicio 1.
- 🎯 **Por qué importa:** Un resultado numérico que nadie puede reproducir no es ciencia. Si dentro de un año hay que saber por qué una trayectoria salió así, hacen falta la configuración exacta, las versiones del software y pruebas que digan si el programa sigue funcionando.
- 🔗 **Se estudia junto con:** huella, manifiesto, referencia independiente, prueba de regresión.

📘 **Dónde se aprende** (1 clase): [B11-C20 · Propagador reproducible de trayectoria](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md).

### Configuración electrónica

- La configuración electrónica dice cuántos electrones hay en cada capa y subcapa: por ejemplo, el oxígeno es `1s² 2s² 2p⁴` (S2).

💡 **Contexto en la clase [B06-C02](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md):**
- **Idea central (modelo mental):** Piensa en un edificio de cuartos que se ocupan de abajo hacia arriba: cada «piso» (capa) tiene un número limitado de lugares para electrones. Cuando un piso se llena, el siguiente electrón tiene que ir al piso siguiente, más lejos del núcleo. Cada vez que empieza un piso nuevo, empieza un periodo nuevo.
- 🎯 **Por qué importa:** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?
- 🔗 **Se estudia junto con:** tabla periódica, fila, periodo, columna.

📘 **Dónde se aprende** (1 clase): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md).

### Confirmación

- La confirmación `k` exige `k` evaluaciones seguidas.

💡 **Cómo se explica en la clase [B107-C09](../programa/clases/B107/B107-C09-progresion-de-recuperacion-y-criterios-de-alta/CLASE.md):**
- Ejercicio 5 · autónomo. Si la confirmación `k = 2` exige dos pases independientes de ese indicador, ¿qué probabilidad tienen?
- 🎯 **Por qué importa:** Los fragmentos consultados indican que la pérdida de fuerza tras misiones largas conlleva riesgos operativos y médicos (English et al., 2015) y que existen baterías de pruebas funcionales y medidas fisiológicas (Mulavara et al., 2018). Una regla de alta combina varios indicadores con ruido.
- 🔗 **Se estudia junto con:** indicador, umbral, regla conjuntiva, pase falso.

📘 **Dónde se aprende** (1 clase): [B107-C09 · Progresión de recuperación y criterios de alta](../programa/clases/B107/B107-C09-progresion-de-recuperacion-y-criterios-de-alta/CLASE.md).

### Confirmación «m de n»

- La confirmación «m de n» exige `m` muestras sobre el umbral entre las últimas `n`.

💡 **Cómo se explica en la clase [B114-C03](../programa/clases/B114/B114-C03-alarmas-y-procedimientos-ante-desviaciones-atmosfericas/CLASE.md):**
- La confirmación y la histéresis no son gratuitas: añaden retraso y hay que ajustarlas con datos reales.
- S["sensor + ruido"] --> C["confirmacion m de n"]
- 🎯 **Por qué importa:** Un sensor correcto con una regla mala produce alarmas inútiles o tardías. La decisión central: ¿qué umbral, qué confirmación y qué histéresis dan pocas falsas alarmas sin perder tiempo de respuesta?
- 🔗 **Se estudia junto con:** presión parcial, umbral, histéresis, falsa alarma.

📘 **Dónde se aprende** (1 clase): [B114-C03 · Alarmas y procedimientos ante desviaciones atmosféricas](../programa/clases/B114/B114-C03-alarmas-y-procedimientos-ante-desviaciones-atmosfericas/CLASE.md).

### Confirmado

- Tus archivos pasan por tres estados: modificado (editado, aún no registrado), preparado (*staged*, marcado para el próximo commit) y confirmado (guardado en la base local) (S2).

💡 **Cómo se explica en la clase [B07-C14](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md):**
- Paso 6. `git restore periodos.csv`: el estado queda vacío y el archivo recupera el último contenido confirmado.
- Paso final · incertidumbre. El historial registra qué cambió, no que el contenido sea correcto: si hubieras confirmado `Mercurio,0`, Git lo habría guardado con la misma naturalidad.
- 🎯 **Por qué importa:** Sin control de versiones, un proyecto científico acumula archivos como `analisis_final.py`, `analisis_final2.py` y `analisis_final_ahora_si.py`, y nadie sabe cuál produjo la figura del artículo. Con Git, cada estado importante queda guardado con un mensaje, una fecha y un autor, y puedes comparar o recuperar cualquier versión.
- 🔗 **Se estudia junto con:** repositorio, commit, modificado, preparado.

📘 **Dónde se aprende** (1 clase): [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md).

### Confirmatorio

- Un análisis confirmatorio sigue el plan; uno exploratorio no.

💡 **Cómo se explica en la clase [B14-C23](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md):**
- A --> C["Resultado confirmatorio<br/>α = 0,05 por prueba"]
- *Descripción textual:* el protocolo se congela con una huella antes de ver los datos; el análisis según el protocolo da un resultado confirmatorio con la tasa de error declarada; un análisis no previsto se etiqueta exploratorio; escoger la prueba después de mirar los datos infla los falsos positivos (con 20 pruebas, el 64 %).
- 🎯 **Por qué importa:** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.
- 🔗 **Se estudia junto con:** protocolo preregistrado, exploratorio, desviación, falso positivo.

📘 **Dónde se aprende** (1 clase): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md).

### Conflicto

- Un conflicto (definición del ejemplo) es una diferencia de importancia de 4 o más entre dos partes.

💡 **Cómo se explica en la clase [B83-C02](../programa/clases/B83/B83-C02-partes-interesadas-y-usuarios/CLASE.md):**
- Además hay 8 pares (parte, parte, necesidad) con diferencia de importancia de 4 o más, que deben tratarse como conflictos antes de escribir requisitos.
- *Descripción textual:* los pesos de las partes y sus importancias se combinan en una suma ponderada que da el orden de necesidades; se pone a prueba con perturbaciones, y las importancias también revelan conflictos entre partes.
- ⚠️ **Error frecuente:** Ocultar los conflictos. Regístralos y asígnales un responsable de decisión
- 🎯 **Por qué importa:** Cuando las necesidades de dos partes chocan (alta resolución frente a bajo costo), alguien debe decidir con criterio. La decisión central: ¿qué necesidades pasan a requisitos primero y cuánto confías en ese orden?
- 🔗 **Se estudia junto con:** parte interesada, poder, interés, matriz poder/interés.

📘 **Dónde se aprende** (1 clase): [B83-C02 · Partes interesadas y usuarios](../programa/clases/B83/B83-C02-partes-interesadas-y-usuarios/CLASE.md).

### Conflicto abierto

- El conflicto abierto ocurre cuando la tensión de alguien supera el umbral.

💡 **Cómo se explica en la clase [B104-C16](../programa/clases/B104/B104-C16-manejo-de-conflictos/CLASE.md):**
- Un modelo ilustrativo con persistencia diaria 0,90 y choque diario de 0,35: la tensión estacionaria tiene varianza 0,6447 (el laboratorio mide 0,6431) y el umbral de conflicto abierto de 2,0 equivale a 2,49 desviaciones estándar.
- Descripción larga: en el modelo, actuar antes de que la tensión llegue al umbral evita casi todos los conflictos abiertos.
- 🎯 **Por qué importa:** Un conflicto abierto cuesta tiempo, errores y confianza; prevenirlo cuesta pequeñas conversaciones continuas. La decisión central: ¿cuánto reduce una intervención temprana la probabilidad de que la tensión llegue al conflicto abierto, frente a no hacer nada o reunirse una vez por semana?
- 🔗 **Se estudia junto con:** tensión, persistencia, mediación temprana, reunión de revisión.

📘 **Dónde se aprende** (1 clase): [B104-C16 · Manejo de conflictos](../programa/clases/B104/B104-C16-manejo-de-conflictos/CLASE.md).

### Conflicto de interés

- Un conflicto de interés es un incentivo que puede sesgar a quien informa.
- Un conflicto de interés es cualquier relación que podría sesgar la evaluación o el trabajo (S1).

💡 **Contexto en la clase [B01-C19](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md):**
- **Idea central (modelo mental):** Imagina una escalera en la que cada peldaño es una fuente: abajo, el dato primario con su método y su versión; encima, la documentación oficial; después, los resúmenes y la prensa; arriba del todo, una publicación en redes. Cuanto más arriba, más lejos del dato y más pasos de interpretación.
- 🎯 **Por qué importa:** Un titular dice: «Neutrinos superan la velocidad de la luz: Einstein estaba equivocado». Es una afirmación fuerte.
- 🔗 **Se estudia junto con:** fuente primaria, fuente oficial, fuente secundaria, preprint.

📘 **Dónde se aprende** (2 clases): [B01-C19 · Fuentes confiables y desinformación espacial](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md); [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Conflicto de requisitos

- Un conflicto de requisitos ocurre cuando no se pueden cumplir todos a la vez.

💡 **Cómo se explica en la clase [B03-C20](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md):**
- *Descripción textual:* de los requisitos se calcula el factor de escala; con él se construye la tabla de maqueta; la tabla pasa por tres verificaciones (razones, Kepler y espacio/tiempo de luz); y todo se resume en un informe con límites y conflictos.
- Ejercicio 12 · integrador. Elabora tu *informe de maqueta con verificaciones* (sección 20): requisitos y conflictos, factor de escala, tabla de la maqueta (distancias y diámetros), tres verificaciones, propagación de la incertidumbre de construcción, límites y fuentes.
- ⚠️ **Error frecuente:** No declarar el conflicto de requisitos. Ejercicio 6.
- 🎯 **Por qué importa:** Un ingeniero no recibe un ejercicio con una sola fórmula: recibe requisitos («que quepa en un patio de 350 m», «que se vea el Sol», «que Neptuno esté a su sitio») y debe decidir qué se puede cumplir y qué no.
- 🔗 **Se estudia junto con:** requisito, componente, criterio de comprobación, factor de escala.

📘 **Dónde se aprende** (1 clase): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md).

### Conforme

- Una proyección conforme conserva los ángulos locales; una equivalente conserva las áreas; ninguna puede conservar a la vez ángulos y áreas (salvo en una esfera, que no cabe en un plano).

💡 **Contexto en la clase [B04-C17](../programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/CLASE.md):**
- **Idea central (modelo mental):** Si intentas aplastar la cáscara de una naranja sobre una mesa, se rompe o se estira. Cada proyección decide dónde estirar y dónde romper. Mercator estira hacia los polos de modo que los ángulos se conserven; la ortográfica deja ver una cara y comprime los bordes.
- 🎯 **Por qué importa:** Casi todo lo que ves del espacio, de la Tierra o de otro cuerpo, llega en forma de mapa: la superficie de un planeta, el cielo entero, la huella de un satélite. Y un mapa es una proyección.
- 🔗 **Se estudia junto con:** proyección cartográfica, factor de escala, equivalente, Mercator.

📘 **Dónde se aprende** (1 clase): [B04-C17 · Proyecciones cartográficas elementales](../programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/CLASE.md).

### Conformidad

- La conformidad es el cociente radio del surco/diámetro de la bola.
- La conformidad es el cumplimiento de los requisitos de un estándar.

💡 **Cómo se explica en la clase [B84-C14](../programa/clases/B84/B84-C14-rodamientos-y-lubricacion-espacial/CLASE.md):**
- Una bola de acero de `6,35 mm` con `Q = 100 N` sobre plano da `a = 0,1294 mm` y `p₀ = 2851 MPa`; en un surco de conformidad 52 % (aproximado) da `a = 0,3834 mm` y `p₀ = 325 MPa`.
- Descripción larga: la conformidad baja la presión 9 veces; el calor acorta la vida del lubricante en más de 200 veces entre 20 y 80 °C.
- 🎯 **Por qué importa:** La vida de un rodamiento espacial la limita el lubricante, no la fatiga: un cálculo de evaporación de un minuto dice si basta 2 mg o hace falta un depósito. La decisión central: ¿qué presión de contacto soporta el rodamiento y cuánto dura su lubricante en vacío?
- 🔗 **Se estudia junto con:** contacto de Hertz, vida L10, evaporación.

📘 **Dónde se aprende** (2 clases): [B84-C14 · Rodamientos y lubricación espacial](../programa/clases/B84/B84-C14-rodamientos-y-lubricacion-espacial/CLASE.md); [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Confusión

- La confusión es la dificultad de asignar una línea a una especie.

💡 **Cómo se explica en la clase [B62-C08](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md):**
- La evidencia es la ficha de confusión de líneas del ejercicio 12.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de confusión de líneas*: fracción mezclada, falsas esperadas por `k`, resultado de la búsqueda en velocidad y límites del modelo, rotulando lo sintético.
- 🎯 **Por qué importa:** Una línea que coincide con una frecuencia de catálogo no identifica una molécula: puede ser casualidad. La decisión central: ¿cuántas líneas hacen falta para afirmar una identificación con riesgo bajo de falsa alarma?
- 🔗 **Se estudia junto con:** densidad de líneas, línea mezclada, tolerancia, escalera.

📘 **Dónde se aprende** (1 clase): [B62-C08 · Mezclas moleculares y confusión de líneas](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md).

### Congelación

- La congelación es el momento en que las reacciones débiles dejan de mantener el equilibrio.

💡 **Cómo se explica en la clase [B26-C16](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md):**
- *Descripción textual:* la diferencia de masa fija la razón de equilibrio; tras la congelación los neutrones se desintegran hasta que el deuterio sobrevive; todos los neutrones restantes forman helio-4 y fijan `Y_p`.
- El cálculo de esta clase, con una temperatura de congelación de `0,75 MeV` y un tiempo de inicio de `200 s` (ilustrativos), da `Y_p = 0,2487`; con `n/p = 1/7`, exactamente `0,25`.
- ⚠️ **Error frecuente:** Creer que `Y_p` es insensible a la temperatura de congelación. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** La cuarta parte de la masa bariónica del universo es helio, y la proporción casi no cambió desde los primeros minutos. Su valor da información sobre cuántas especies de neutrinos existen y sobre la densidad de bariones.
- 🔗 **Se estudia junto con:** nucleosíntesis primordial, razón n/p, vida media del neutrón libre, energía de ligadura del deuterón.

📘 **Dónde se aprende** (1 clase): [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Congelado

- El flujo magnético es la integral de `B` por una superficie. Congelado significa que el flujo a través de una superficie material no cambia.

💡 **Cómo se explica en la clase [B35-C07](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md):**
- La evidencia es la ficha del flujo congelado del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha del flujo congelado*: compresión, difusión y enlace.
- 🎯 **Por qué importa:** La conservación del flujo explica por qué el campo se amplifica al comprimirse y por qué la reconexión exige romper la idealidad. La decisión central: ¿cuándo el campo se mueve con el plasma y cuándo se difunde?
- 🔗 **Se estudia junto con:** flujo magnético, resistividad, número de enlace, helicidad.

📘 **Dónde se aprende** (1 clase): [B35-C07 · Congelamiento del flujo magnético y conservación en MHD ideal](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md).

### Congelar

- La huella del protocolo es el SHA-256 de su texto normalizado. Congelar es fijar el protocolo de modo que cambiarlo sea detectable.

💡 **Cómo se explica en la clase [B14-C23](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md):**
- P["Protocolo: hipótesis,<br/>prueba, α, exclusiones"] --> H["Congelar<br/>(huella SHA-256)"]
- Congelar el protocolo con una huella y detectar cualquier desviación posterior.
- ⚠️ **Error frecuente:** Congelar solo en tu equipo. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.
- 🔗 **Se estudia junto con:** protocolo preregistrado, confirmatorio, exploratorio, desviación.

📘 **Dónde se aprende** (1 clase): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md).

### Cónica

- Una cónica es la curva que resulta de cortar un cono con un plano: circunferencia, elipse, parábola o hipérbola.
- Una cónica `z = (R − √(R² − (1+K)y²))/(1+K)` con `K = −1` es un paraboloide.

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- Su límite: el chorro está sujeto a la gravedad terrestre y la cónica orbital a otra ley (la gravitación del Sol, B05); la analogía sirve para la forma, no para la causa.
- Nombrar las cuatro cónicas y su excentricidad: `e = 0`, `0 < e < 1`, `e = 1`, `e > 1`.
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.
- 🔗 **Se estudia junto con:** propiedad foco–directriz, foco, directriz, excentricidad.

📘 **Dónde se aprende** (2 clases): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B43-C02 · Selección de geometría instrumental](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md).

### Conjugada

- Es conjugada de la Poisson: si el prior es Gamma(a, b), la posterior es Gamma(a + n, b + T), sin integrales.

💡 **Cómo se explica en la clase [B19-C01](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md):**
- Alternativas: Gamma (conjugada), log-normal o una Normal truncada en `λ > 0`.
- 🎯 **Por qué importa:** Un contador de partículas a bordo de un CubeSat registra 3 eventos en 1 hora. ¿Cuál es la tasa verdadera `λ`, en eventos por hora?
- 🔗 **Se estudia junto con:** parámetro, datos, verosimilitud, prior.

📘 **Dónde se aprende** (1 clase): [B19-C01 · Priors físicamente informados](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md).

### Conjugado

- El conjugado es `q* = (q₀, −q⃗)`.
- Un prior es conjugado si la posterior pertenece a su misma familia: Beta–Binomial (prior `Beta(a,b)`, `s` éxitos en `n` ensayos → `Beta(a+s, b+n−s)`) y Poisson–Gamma (prior `Gamma(α,β)` con forma `α` y tasa `β`, conteos con suma `S` en `n` intervalos → `Gamma(α+S, β+n)`).

💡 **Cómo se explica en la clase [B10-C15](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md):**
- Hay bibliotecas con el escalar al final, con el producto en orden inverso, o cuyos cuaterniones representan la rotación de coordenadas (el conjugado del que usa esta clase).
- Ejercicio 5. Calcula el conjugado y el producto `q ⊗ q*`.
- 🎯 **Por qué importa:** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.
- 🔗 **Se estudia junto con:** cuaternión, parte escalar, parte vectorial, escalar primero.

📘 **Dónde se aprende** (2 clases): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md); [B12-C12 · Inferencia bayesiana](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md).

### Conjunción

- Una oposición es la configuración en que Tierra y planeta exterior están alineados al mismo lado del Sol; una conjunción, la alineación al lado contrario.
- La conjunción es el alineamiento aparente con el Sol; la oposición (planeta exterior opuesto al Sol, elongación 180°) es su mejor momento para ver.
- Una conjunción es un acercamiento entre dos objetos.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- El retardo de luz es `d/c`: en oposición circular, `78,4 × 10⁶ km / 299 792,458 km/s = 261,5 s = 4,36 min`; en conjunción, 20,99 min.
- En oposición (`φ = 0`) sale 78,4 millones de km; en conjunción (`φ = 180°`), 377,6.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.
- 🔗 **Se estudia junto con:** ley de cosenos, ley de senos, resuelve, LAL.

📖 **Explicado a fondo:** [Oposición y conjunción](esencial/cuarta-fundamentos.md#oposición-y-conjunción) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md); [B08-C10 · Planetas observables y elongación](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md); [B118-C05 · Conjunciones orbitales](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md); [B119-C10 · Responsabilidad por daños espaciales](../programa/clases/B119/B119-C10-responsabilidad-por-danos-espaciales/CLASE.md).

### Conjunción solar

- La conjunción solar es la alineación Tierra–Sol–Marte que bloquea las comunicaciones.

💡 **Cómo se explica en la clase [B75-C19](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md):**
- Límite: el correo no se pierde en conjunción solar ni depende de la geometría orbital.
- Los semiejes y periodos son de las fichas [S1, S2]; la conjunción solar no se modela.
- 🎯 **Por qué importa:** No se puede dirigir desde la Tierra lo que sucede en minutos. La decisión central: ¿qué eventos duran menos que el tiempo mínimo de reacción desde tierra y por tanto deben ser autónomos?
- 🔗 **Se estudia junto con:** retardo unidireccional, RTLT, tiempo de reacción, autonomía.

📘 **Dónde se aprende** (1 clase): [B75-C19 · Restricciones de navegación autónoma](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md).

### Conjunto

- Un conjunto (`set`) es una colección sin orden ni duplicados (S3).
- El conjunto es un grupo de simulaciones con parámetros perturbados.
- El conjunto suma las comparaciones.

💡 **Cómo se explica en la clase [B07-C07](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md):**
- Una lista es una fila de cajones numerados; un diccionario es un fichero con etiquetas (claves) para buscar rápido; una tupla es una fila de cajones sellados; un conjunto es una bolsa donde cada cosa entra una vez.
- Usar conjuntos para pertenencia e intersecciones.
- ⚠️ **Error frecuente:** `{}` como conjunto vacío. Es un diccionario.
- 🎯 **Por qué importa:** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.
- 🔗 **Se estudia junto con:** lista, tupla, inmutable, diccionario.

📘 **Dónde se aprende** (3 clases): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md); [B33-C02 · Modelos de propagación de CME](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md); [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md).

### Conjunto activo

- El conjunto activo es el de los tramos con `|u_k| = U`.

💡 **Cómo se explica en la clase [B81-C12](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md):**
- Con `N = 40` y `U = 5`: conjunto activo `12,096774194`, SLSQP `12,096774194`; diferencia relativa `1 × 10⁻¹⁴`.
- Cerca de la cota mínima casi todos los tramos acaban saturados y el conjunto activo cambia más veces.
- 🎯 **Por qué importa:** Ignorar una cota produce un control irrealizable; imponerla mal produce un problema sin solución. La decisión central: ¿cuánto cuesta una cota de control y cuál es el mínimo valor para el que el problema aún tiene solución?
- 🔗 **Se estudia junto con:** cota, tiempo mínimo.

📘 **Dónde se aprende** (1 clase): [B81-C12 · Restricciones dinámicas en optimización](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md).

### Conjunto de corte

- Un conjunto de corte es una combinación que causa el evento superior; es mínimo si ningún subconjunto propio lo causa.

💡 **Cómo se explica en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- *Descripción textual:* el evento superior se descompone con compuertas en eventos básicos; la expansión da los conjuntos de corte, reducidos por absorción a mínimos; con ellos y las probabilidades se calcula `P(top)` por tres vías y la importancia indica qué proteger primero.
- La expansión da 5 conjuntos de corte y la absorción deja 4: dos de un solo evento (B7 y B5, puntos únicos de fallo) y dos pares (B1·B2 y B3·B4).
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?
- 🔗 **Se estudia junto con:** árbol de fallos, eventos básicos, mínimo, MOCUS.

📘 **Dónde se aprende** (1 clase): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Conjunto de dos líneas

- El conjunto de dos líneas (TLE) son dos líneas de 69 caracteres con los elementos medios.

💡 **Cómo se explica en la clase [B72-C21](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md):**
- *Descripción textual:* el conjunto de dos líneas se lee y valida; el movimiento medio publicado se convierte al de Brouwer; el periodo decide entre SGP4 y SDP4; con el semieje corregido se obtienen las tasas seculares.
- 🎯 **Por qué importa:** Un error clásico es tomar los elementos de dos líneas como elementos keplerianos y propagarlos con dos cuerpos: el error es de kilómetros en minutos. La decisión central: ¿qué propagador corresponde a un conjunto de elementos y qué transformaciones previas exige antes de usarlo?
- 🔗 **Se estudia junto con:** SGP4, SDP4, movimiento medio de Kozai, Brouwer.

📘 **Dónde se aprende** (1 clase): [B72-C21 · Propagador SGP4 y teoría general de perturbaciones](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md).

### Conjunto de entrenamiento

- El conjunto de entrenamiento ajusta el modelo; el de prueba se reserva para la medida final.

💡 **Cómo se explica en la clase [B17-C02](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md):**
- Evaluar en el mismo conjunto de entrenamiento no sirve (da 1,00 con un vecino).
- 🎯 **Por qué importa:** Un modelo que clasifica señales como «candidata» o «no candidata» puede acertar el 100 % de los ejemplos con los que se entrenó y fallar la cuarta parte de los nuevos: memorizó. Lo que importa a un equipo científico es el desempeño en datos que el modelo no vio.
- 🔗 **Se estudia junto con:** aprendizaje supervisado, etiquetas, clasificación, regresión.

📘 **Dónde se aprende** (1 clase): [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md).

### Conjunto de evidencias de aceptación

- Paquete de datos: conjunto de evidencias de aceptación. Certificación: presentación de la evidencia a una autoridad.

💡 **Cómo se explica en la clase [B90-C19](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md):**
- aceptación como probar cada unidad fabricada con un conjunto menor de criterios para confirmar que la mano de obra corresponde al diseño verificado; y certificación como proporcionar la evidencia a una autoridad que aprueba el diseño.
- 🎯 **Por qué importa:** Un ensayo de aceptación demasiado severo gasta vida útil; uno demasiado suave deja pasar defectos. La decisión central: ¿qué nivel y duración demuestran la mano de obra sin dañar la unidad, y con qué evidencia se acepta?
- 🔗 **Se estudia junto con:** Calificación, Protovuelo, Aceptación, calidad de fabricación.

📘 **Dónde se aprende** (1 clase): [B90-C19 · Aceptación de unidades de vuelo](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md).

### Conjunto de referencia

- Un conjunto de referencia (o *dataset* oficial) es un dato publicado con procedencia, versión y marco que se toma como patrón.

💡 **Contexto en la clase [B23-C05](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md):**
- **Idea central (modelo mental):** El modelo y la efeméride parten del mismo estado inicial; se separan porque la efeméride incluye fuerzas que el modelo ignora. La diferencia no es «error» sin más: es la medida de la física omitida.
- 🎯 **Por qué importa:** Un modelo kepleriano de la Tierra pasó todas las pruebas de C01–C04, pero eso no dice nada sobre si la Tierra se mueve como una elipse perfecta. La pregunta motivadora es: ¿contra qué contrasto mi modelo, y qué diferencia estoy dispuesto a aceptar?
- 🔗 **Se estudia junto con:** efeméride, elementos osculadores, criterio de aceptación, dominio de validación.

📘 **Dónde se aprende** (1 clase): [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md).

### Conjunto mínimo de corte

- Un conjunto mínimo de corte no tiene subconjunto que también cause el tope.

💡 **Cómo se explica en la clase [B88-C16](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md):**
- Los conjuntos mínimos de corte son `{C}`, `{A, B}` y `{D, E}`.
- Conjuntos minimos de corte: [['C'], ['A', 'B'], ['D', 'E']]
- 🎯 **Por qué importa:** Una nave tolera fallos si ninguno solo provoca la pérdida y las combinaciones peligrosas son improbables. La decisión central: ¿qué combinaciones mínimas de fallos causan la pérdida y cuál elemento merece más protección?
- 🔗 **Se estudia junto con:** evento tope, eventos básicos, importancia de Birnbaum, matriz severidad–probabilidad.

📘 **Dónde se aprende** (1 clase): [B88-C16 · Ingeniería de seguridad funcional](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md).

### Conjunto ponderado

- El conjunto ponderado aproxima la distribución del estado.

💡 **Contexto en la clase [B15-C18](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md):**
- **Idea central (modelo mental):** Mil exploradores se reparten por el mapa, cada uno con una hipótesis de dónde está el objeto. Cada medida es una pista: los que quedan consistentes con ella ganan crédito (peso); los demás, no. De vez en cuando, los exploradores sin crédito se reubican junto a los que sí lo tienen.
- 🎯 **Por qué importa:** Un sensor mide la distancia oblicua a un objeto que pasa junto a él. Cuando el objeto está justo frente al sensor, un pequeño cambio de posición casi no cambia la distancia: la medida no distingue bien un lado del otro, y la incertidumbre de la posición deja de ser una campana.
- 🔗 **Se estudia junto con:** partícula, Propagar, Pesar, degeneración.

📘 **Dónde se aprende** (1 clase): [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md).

### Conmutación

- Las pérdidas de conducción son `R I²`; las de conmutación son `½ V I (t_r + t_f) f`.

💡 **Cómo se explica en la clase [B86-C08](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md):**
- Por pérdidas: conducción, diodo, conmutación.
- Simular la conmutación y comparar el rizado y la tensión media con las fórmulas.
- 🎯 **Por qué importa:** Un convertidor que reduce la tensión con un interruptor y una bobina puede ser mucho más eficiente que un regulador lineal, pero introduce rizado, ruido y pérdidas de conmutación que hay que dimensionar. La decisión central: ¿qué ciclo de trabajo, bobina y condensador dan `5 V` desde `28 V` con rizado y eficiencia aceptables?
- 🔗 **Se estudia junto con:** ciclo de trabajo, rizado, CCM, DCM.

📘 **Dónde se aprende** (1 clase): [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### Conmutación de Dicke

- La conmutación de Dicke alterna fuente y referencia.

💡 **Cómo se explica en la clase [B46-C06](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md):**
- Explicar la penalización de la conmutación de Dicke.
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué se conmuta con Dicke?
- 🎯 **Por qué importa:** La señal de una fuente astronómica es mucho menor que el ruido, y solo el promedio la hace visible. La decisión central: ¿cuánto tiempo y ancho de banda se necesitan para alcanzar una sensibilidad dada?
- 🔗 **Se estudia junto con:** temperatura de ruido, cascada de Friis, temperatura de sistema, ecuación del radiómetro.

📘 **Dónde se aprende** (1 clase): [B46-C06 · Ruido de sistema y radiometría](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md).

### Conmutación en posición

- La conmutación en posición ON/OFF.

💡 **Contexto en la clase [B46-C20](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md):**
- **Idea central (modelo mental):** Se parte del destino (la sensibilidad), se calcula el consumo (el tiempo) y se añade reserva (la eficiencia) antes de partir.
- 🎯 **Por qué importa:** Un proyecto viable cuadra objetivo, sensibilidad, tiempo y datos. La decisión central: ¿cuánto tiempo de observación pide el objetivo y con qué margen?
- 🔗 **Se estudia junto con:** objetivo científico, criterio de detección, presupuesto de sensibilidad, eficiencia de observación.

📘 **Dónde se aprende** (1 clase): [B46-C20 · Proyecto de observación radioastronómica](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md).

### Conmutación tipo Dicke

- La conmutación tipo Dicke alterna cielo y referencia.

💡 **Contexto en la clase [B49-C08](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md):**
- **Idea central (modelo mental):** Como pesar con una balanza que se descalibra: pesar mucho rato promedia el ruido, pero la descalibración crece; hay que tarar a menudo.
- 🎯 **Por qué importa:** Integrar más tiempo no siempre mejora la medida: la deriva lo impide. La decisión central: ¿hasta qué tiempo de integración vale la pena, y cuándo hay que conmutar?
- 🔗 **Se estudia junto con:** ecuación del radiómetro, deriva de ganancia, desviación de Allan, potencia total.

📘 **Dónde se aprende** (1 clase): [B49-C08 · Estabilidad de ganancia de receptores y variaciones de ganancia](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md).

### Cono de emisión

- El cono de emisión tiene semiángulo `1/γ`.

💡 **Cómo se explica en la clase [B27-C11](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md):**
- Ejercicio 6. Semiángulo del cono de emisión para `γ = 30`.
- 🎯 **Por qué importa:** Un chorro que se acerca puede parecer más rápido que la luz sin violar nada, y su brillo cambia en órdenes de magnitud según el ángulo. Sin estos efectos no se pueden comparar chorros ni inferir su velocidad.
- 🔗 **Se estudia junto con:** velocidad aparente, movimiento superlumínico aparente, factor Doppler, contrachorro.

📘 **Dónde se aprende** (1 clase): [B27-C11 · Chorros relativistas](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md).

### Cono de luz

- El cono de luz de un evento es el conjunto de eventos a intervalo nulo; separa el futuro, el pasado y el «en otra parte».

💡 **Cómo se explica en la clase [B26-C04](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md):**
- Un evento puede influir en otro solo si el segundo está en su cono futuro (o sobre él).
- Cada punto del mapa tiene un cono de luz dibujado: dentro del cono hacia arriba está su futuro, dentro hacia abajo su pasado; fuera, sus eventos inalcanzables.
- 🎯 **Por qué importa:** Comunicar con una sonda, sincronizar relojes de dos estaciones o decidir si un evento puede haber causado otro exige saber cuándo dos sucesos están conectados por una señal. El intervalo lo decide para todos los observadores.
- 🔗 **Se estudia junto con:** espacio-tiempo de Minkowski, intervalo de género tiempo, género espacio, género luz.

📘 **Dónde se aprende** (1 clase): [B26-C04 · Espacio-tiempo de Minkowski](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md).

### Cono de orientación

- El cono de orientación limita `|δ|`.

💡 **Cómo se explica en la clase [B81-C06](../programa/clases/B81/B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md):**
- Aplicar un cono de orientación `|δ| ≤ δ_max`.
- El script [orientacion.py](orientacion.py) calcula `E(ψ, δ)`, el óptimo analítico y por rejilla, el efecto de un cono de orientación y el tiempo de misión (comprueba que la rejilla coincida con el analítico a 1e-6 y `E(30°, 0) = 0,5`).
- 🎯 **Por qué importa:** Una trayectoria óptima en el vacío no es necesariamente volable: el guiado debe respetar la orientación de los paneles. La decisión central: ¿cuánto conviene desviar el empuje de la dirección óptima para recuperar potencia, y dentro de qué cono?
- 🔗 **Se estudia junto con:** eficiencia útil.

📘 **Dónde se aprende** (1 clase): [B81-C06 · Restricciones de orientación del empuje](../programa/clases/B81/B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md).

### Cono de pérdida

- El cono de pérdida es el rango de `α_eq` con espejo bajo la atmósfera.

💡 **Cómo se explica en la clase [B30-C16](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md):**
- En `L = 4` la línea toca la atmósfera (100 km) en `λ = 59,74°`, donde `B = 53 585 nT`; el cono de pérdida es `α_LC = 5,47°`.
- A --> LC["cono de pérdida en la atmósfera"]
- 🎯 **Por qué importa:** Las partículas con ángulo de paso pequeño se pierden en la atmósfera; las demás quedan atrapadas y dañan satélites. La decisión central: ¿qué partículas quedan atrapadas y con qué periodo rebotan?
- 🔗 **Se estudia junto con:** ángulo de paso ecuatorial, punto de espejo, periodo de rebote, cinturones de Van Allen.

📘 **Dónde se aprende** (1 clase): [B30-C16 · Cinturones de Van Allen](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md).

### Conocimiento tradicional

- El conocimiento tradicional es el saber transmitido por una comunidad.

💡 **Cómo se explica en la clase [B02-C20](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md):**
- La iniciativa UNESCO–IAU, lanzada en 2003 como actividad de prueba inicial, vincula ciencia y cultura para reconocer sitios relacionados con la astronomía, incluido el «conocimiento comunitario tradicional»; la IAU participa desde un acuerdo con la UNESCO en 2008.
- 🎯 **Por qué importa:** Los sitios, instrumentos, archivos, saberes y hasta la oscuridad del cielo son patrimonio, y los telescopios, el turismo y las constelaciones de satélites pueden dañarlo. La pregunta motivadora es: ¿qué debo preguntar, a quién y antes de qué, cuando mi trabajo toca un cielo o un lugar que importa a otras personas?
- 🔗 **Se estudia junto con:** patrimonio astronómico, consentimiento libre, previo e informado, UNDRIP, contaminación lumínica.

📘 **Dónde se aprende** (1 clase): [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md).

### CONOPS

- Un CONOPS describe fases, modos, actores y escenarios de operación.
- ConOps: descripción de cómo se opera la misión.

💡 **Cómo se explica en la clase [B83-C03](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md):**
- El CONOPS de ejemplo tiene cuatro fases: lanzamiento y primeras órbitas (7 d), puesta en servicio (30 d), operaciones nominales (3 años) y fin de vida (90 d).
- *Descripción textual:* las fases y modos del CONOPS definen la órbita y la estación; la simulación de visibilidad da pases, duraciones y huecos, de los que sale el tiempo de enlace diario; la cota analítica del pase cenital sirve de comprobación.
- ⚠️ **Error frecuente:** Escribir un CONOPS sin números. Añade pases, huecos y latencias
- 🎯 **Por qué importa:** Los requisitos de datos, energía y operaciones dependen de cuántas veces al día se puede hablar con el satélite y por cuánto tiempo. La decisión central: ¿cuánto contacto real ofrece la órbita y cómo se reparte en las fases de la misión?
- 🔗 **Se estudia junto con:** fases, modo, pase, hueco.

📘 **Dónde se aprende** (2 clases): [B83-C03 · Concepto de operaciones CONOPS](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md); [B96-C02 · Concepto de operaciones de misión](../programa/clases/B96/B96-C02-concepto-de-operaciones-de-mision/CLASE.md).

### Consejo

- El consejo es el órgano que dirige la empresa.

💡 **Cómo se explica en la clase [B125-C03](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md):**
- Consejo sintético con pesos `[3, 2, 1, 1, 1, 1, 1]` y cuota `6` de `10`.
- Descripción larga: con 20 votos por acción, menos del 5 % de las acciones da la mitad del voto; en un consejo ponderado el poder real se aparta del peso nominal, y un peso dominante lo concentra todo.
- 🎯 **Por qué importa:** Las decisiones de una empresa se estructuran en su gobierno y, en el espacio, el capital intensivo hace que quien controla la votación controle el rumbo de misiones de años; ninguna clase lo trata.
- 🔗 **Se estudia junto con:** clase de acciones, poder de voto, cuota, índice de Banzhaf.

📘 **Dónde se aprende** (1 clase): [B125-C03 · Gobierno corporativo de una empresa espacial](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md).

### Consenso

- El consenso exige que nadie bloquee.

💡 **Cómo se explica en la clase [B119-C06](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md):**
- El detalle del reglamento y las decisiones por consenso no se consultaron.
- Para consenso con probabilidad al menos 0,5: `p ≤ 0.03778` con 18 miembros y `p ≤ 0.00691` con 100.
- ⚠️ **Error frecuente:** Creer que consenso es unanimidad de votos. Se corrige con el vocabulario.
- 🎯 **Por qué importa:** Quien estudia el derecho espacial necesita saber dónde se negocia y cómo se decide; ninguna clase anterior trata los organismos. La decisión central: ¿cómo cambia la probabilidad de bloqueo cuando crece el número de miembros que deben consentir?
- 🔗 **Se estudia junto con:** COPUOS, UNOOSA, Bloqueo.

📘 **Dónde se aprende** (1 clase): [B119-C06 · Organismos UNOOSA y COPUOS](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md).

### Consentimiento libre, previo e informado

- El consentimiento libre, previo e informado es el derecho de un pueblo a decidir, antes de un proyecto y con información suficiente, si acepta que afecte su territorio o su conocimiento (S3).
- El consentimiento libre, previo e informado es la aceptación sin coacción, antes de empezar y con información suficiente.
- El consentimiento libre, previo e informado (CLPI) exige obtener el acuerdo de un pueblo antes de un proyecto que afecte sus tierras o territorios, sin coerción y con información suficiente (S2).

💡 **Cómo se explica en la clase [B02-C06](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md):**
- Reconocer las preguntas de consentimiento libre, previo e informado.
- 🎯 **Por qué importa:** Chile alberga algunos de los cielos más oscuros del mundo y los más grandes observatorios, y también pueblos que miraron esos cielos durante milenios. La pregunta motivadora es: ¿cómo hablar de saberes celestes de pueblos vivos sin generalizar, sin apropiarse y sin presentar como establecido lo que no hemos podido verificar?
- 🔗 **Se estudia junto con:** pueblo originario, contaminación lumínica, saber.

📘 **Dónde se aprende** (3 clases): [B02-C06 · Astronomía de pueblos originarios de Chile](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md); [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md); [B133-C03 · Colaboración con comunidades en investigación y educación](../programa/clases/B133/B133-C03-colaboracion-con-comunidades-en-investigacion-y-educacion/CLASE.md).

### Conserva

- La energía mecánica `E = E_c + E_p` se conserva si solo actúan fuerzas conservativas, o si las demás no hacen trabajo.
- Un sobrevuelo lo conserva (en el límite de cónicas empalmadas con planeta en órbita circular).

💡 **Cómo se explica en la clase [B05-C07](../programa/clases/B05/B05-C07-conservacion-de-energia-mecanica/CLASE.md):**
- Paso 4 · Sentido físico. Con `g` constante saldrían 1275 km: la conservación con `E_p = −GM/r` es más fiel.
- En esta clase calcularás ambos valores con conservación de energía y los compararás con los publicados.
- ⚠️ **Error frecuente:** Aplicar conservación con fuerzas no conservativas. Ejercicios 8 y 11.
- 🎯 **Por qué importa:** Si lanzas algo hacia arriba, ¿hasta dónde sube? ¿Con qué rapidez hay que lanzarlo para que no vuelva?
- 🔗 **Se estudia junto con:** energía mecánica, velocidad de escape, órbita ligada, energía específica.

📘 **Dónde se aprende** (2 clases): [B05-C07 · Conservación de energía mecánica](../programa/clases/B05/B05-C07-conservacion-de-energia-mecanica/CLASE.md); [B75-C08 · Secuencias múltiples de sobrevuelos](../programa/clases/B75/B75-C08-secuencias-multiples-de-sobrevuelos/CLASE.md).

### Conserva el volumen

- Es reversible y conserva el volumen, pero no exactamente la energía: su error de energía `ΔH` escala como `ε²`.

💡 **Contexto en la clase [B19-C03](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md):**
- **Idea central (modelo mental):** Piensa que `U(q)` es la altura de un terreno y que lanzas una canica con una velocidad aleatoria. La canica rueda, sube las laderas y desacelera, y al cabo de un tiempo la detienes: esa es tu propuesta. En un cuenco alargado, la canica corre a lo largo del eje largo sin tener que vencer las paredes, algo que un paso aleatorio no puede hacer.
- 🎯 **Por qué importa:** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.
- 🔗 **Se estudia junto con:** posición, momento, energía potencial, cinética.

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
- 🔗 **Se estudia junto con:** análisis nodal, conductancia, corriente de tierra, fuente en serie.

📘 **Dónde se aprende** (3 clases): [B33-C07 · Impactos del clima espacial en redes eléctricas](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md); [B39-C04 · Tensor de energía-momento y fuentes de curvatura](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md); [B55-C20 · Modelo simplificado de red astroquímica](../programa/clases/B55/B55-C20-modelo-simplificado-de-red-astroquimica/CLASE.md).

### Conservación de la masa

- La conservación de la masa limita el modelo.

💡 **Contexto en la clase [B118-C09](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md):**
- 🎯 **Por qué importa:** La directriz 5 de la COPUOS dice que la mayor parte de los desechos catalogados proviene de fragmentaciones; entender cuántos fragmentos produce un evento y de qué tamaño es la base de los escenarios futuros. La decisión central: ¿cuántos fragmentos relevantes genera un evento y cuándo es «catastrófico»?
- 🔗 **Se estudia junto con:** fragmentación, catastrófica, ley de potencias de tamaños, energía relativa.

📘 **Dónde se aprende** (1 clase): [B118-C09 · Generación de desechos](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md).

### Conservación de los átomos

- La conservación de los átomos y de la carga son las condiciones que exigimos a una ecuación balanceada.

💡 **Cómo se explica en la clase [B06-C08](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md):**
- La analogía de las piezas muestra que se conserva el número de átomos; su límite es que no explica la energía: en una reacción química se libera o absorbe, aunque la masa casi no cambie.
- 🎯 **Por qué importa:** Una vela y el Sol liberan energía, pero lo hacen de maneras radicalmente distintas. En la vela, los átomos de carbono e hidrógeno se reordenan con el oxígeno y todos siguen ahí al terminar.
- 🔗 **Se estudia junto con:** reacción química, reactivos, productos, ecuación química.

📘 **Dónde se aprende** (1 clase): [B06-C08 · Reacciones y conservación de masa](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md).

### Conservación del flujo

- La conservación del flujo relaciona campo y sección.

💡 **Cómo se explica en la clase [B30-C05](../programa/clases/B30/B30-C05-campos-magneticos-solares/CLASE.md):**
- *Descripción textual:* la densidad, la temperatura y el campo dan las presiones y el beta; el campo y la densidad dan la velocidad de Alfvén; el campo se rige además por la conservación del flujo.
- Aplicar la conservación del flujo `B₁A₁ = B₂A₂`.
- 🎯 **Por qué importa:** Que el gas domine al campo en la fotosfera y el campo al gas en la corona explica por qué la corona se estructura en lazos y por qué las erupciones liberan energía magnética. La decisión central: ¿en qué capa manda el campo y cuánta energía guarda?
- 🔗 **Se estudia junto con:** beta del plasma, velocidad de Alfvén, densidad de energía magnética, tubo de flujo.

📘 **Dónde se aprende** (2 clases): [B30-C05 · Campos magnéticos solares](../programa/clases/B30/B30-C05-campos-magneticos-solares/CLASE.md); [B34-C03 · Bucles magnéticos coronales](../programa/clases/B34/B34-C03-bucles-magneticos-coronales/CLASE.md).

### Conservación del momento

- Impulso: `F·t`. Conservación del momento: la suma `Σ m v` no cambia sin fuerzas externas.

💡 **Cómo se explica en la clase [B106-C16](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md):**
- Aplicar la conservación del momento lineal a un empujón entre astronauta y carga.
- Comprobar la conservación del momento total.
- 🎯 **Por qué importa:** Sin peso ni fricción, toda fuerza tiene una reacción que mueve al operario o a la carga; un diseño de herramientas y de superficies que lo ignore produce maniobras inseguras. La decisión central: ¿qué sujeciones y qué límites de par o de empuje evitan que la reacción mueva al astronauta fuera de la tarea?
- 🔗 **Se estudia junto con:** Impulso, Momento de inercia I, Par τ, Sujeción.

📘 **Dónde se aprende** (1 clase): [B106-C16 · Ergonomía en microgravedad](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md).

### Conservador

- Optimista significa covarianza menor que el error real; conservador, mayor.

💡 **Cómo se explica en la clase [B74-C23](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md):**
- El conservador (`q` diez veces mayor) tiene NEES `1,132`, por debajo del límite inferior, y NIS `0,865`.
- L --> V["consistente / optimista / conservador"]
- 🎯 **Por qué importa:** Un filtro optimista presenta covarianzas pequeñas y errores grandes, y no avisa. La decisión central: ¿cómo sé, con una prueba estadística, si mi filtro es consistente y qué estadístico me avisa de qué fallo?
- 🔗 **Se estudia junto con:** NEES, NIS, consistente, Optimista.

📘 **Dónde se aprende** (1 clase): [B74-C23 · Consistencia de filtros: innovaciones y pruebas NEES/NIS](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md).

### Conservan

- La energía específica (por unidad de masa) es `E = v²/2 − GM/r` y el momento angular específico, `L = x·vy − y·vx`; ambos se conservan en un campo central.

💡 **Cómo se explica en la clase [B07-C20](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md):**
- (3) Runge-Kutta de orden 4 y los métodos con paso adaptativo: más precisión por paso, pero tampoco conservan la energía exactamente; se estudian en B11 y no se consultaron.
- Ejercicio 8. ¿Qué dos cantidades se conservan en un campo central y cómo se comprueba con el simulador?
- 🎯 **Por qué importa:** Un simulador es la forma de explorar un fenómeno cuya solución no tienes a mano, y de comprobar que entiendes uno cuya solución sí conoces. Aquí conoces la respuesta (una órbita circular se repite con un período dado por una fórmula), así que puedes verificar el simulador antes de confiar en él para casos que no conoces.
- 🔗 **Se estudia junto con:** GM, aceleración gravitatoria, órbita circular, período.

📘 **Dónde se aprende** (1 clase): [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md).

### Conservativa

- Una fuerza conservativa es aquella cuyo trabajo no depende del camino, solo de los extremos (la gravedad lo es).

💡 **Contexto en la clase [B05-C06](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md):**
- **Idea central (modelo mental):** El trabajo es el movimiento de dinero entre cuentas; la energía cinética y la potencial son dos de ellas. El teorema trabajo–energía dice cuánto cambia la cuenta cinética.
- 🎯 **Por qué importa:** Poner 1000 kg en órbita cuesta mucho más que subirlos 400 km. La pregunta motivadora es: ¿cuánta energía hay que entregar para cambiar el estado de un cuerpo, y en qué se convierte?
- 🔗 **Se estudia junto con:** trabajo, energía cinética, energía potencial gravitatoria, energía mecánica.

📘 **Dónde se aprende** (1 clase): [B05-C06 · Trabajo y energía](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md).

### Conservativo

- Un campo es conservativo si `F = ∇f`; entonces `∫_C F·dr = f(B) − f(A)` (ec. 1.6.42) y `∇×F = 0`.

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- Para la gravedad, el rotacional es cero (laboratorio: `< 10⁻¹⁵ s⁻²`): el campo es conservativo.
- Por potencial cuando el campo es conservativo: basta evaluar en los extremos.
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.
- 🔗 **Se estudia junto con:** campo vectorial, divergencia, rotacional, integral de línea.

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
- 🔗 **Se estudia junto con:** fusión, pansharpening, resolución espacial, cobertura espectral.

📘 **Dónde se aprende** (3 clases): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md); [B15-C24 · Fusión de imágenes de distintos sensores](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md); [B80-C08 · Filtrado distribuido y descentralizado](../programa/clases/B80/B80-C08-filtrado-distribuido-y-descentralizado/CLASE.md).

### Consistencia física

- La consistencia física de un modelo es que sus dependencias respeten leyes o restricciones conocidas (exponentes, monotonía, signos, unidades).

💡 **Cómo se explica en la clase [B17-C08](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md):**
- *Descripción textual:* un modelo entrenado se somete a dos revisiones paralelas: la importancia por permutación (de qué depende, con atención a variables espurias y duplicadas) y la consistencia física (exponentes, monotonía y extrapolación).
- Las pruebas de consistencia física (exponentes, signos, monotonía, extrapolación) son las más cercanas a lo que un especialista exige, y se escriben como tests automáticos.
- 🎯 **Por qué importa:** Dos modelos pueden tener el mismo error en validación y haber aprendido cosas muy distintas: uno la ley física, otro un atajo que funciona en el rango visto. Si solo miras la métrica, no los distingues, y el atajo falla al primer dato fuera de rango.
- 🔗 **Se estudia junto con:** importancia por permutación, variable espuria, extrapolación, dependencia parcial.

📘 **Dónde se aprende** (1 clase): [B17-C08 · Interpretabilidad con consistencia física](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md).

### Consistente

- Un estimador es consistente si converge al valor verdadero al crecer `n`.
- Un filtro es consistente si su promedio está dentro de los límites de la `χ²`.

💡 **Cómo se explica en la clase [B74-C23](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md):**
- L --> V["consistente / optimista / conservador"]
- *Descripción textual:* el filtro produce errores con covarianza e innovaciones con su covarianza; los promedios de NEES y NIS sobre las simulaciones se comparan con los límites de la χ² para decidir si el filtro es consistente.
- 🎯 **Por qué importa:** Un filtro optimista presenta covarianzas pequeñas y errores grandes, y no avisa. La decisión central: ¿cómo sé, con una prueba estadística, si mi filtro es consistente y qué estadístico me avisa de qué fallo?
- 🔗 **Se estudia junto con:** NEES, NIS, Optimista, conservador.

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
- 🔗 **Se estudia junto con:** variable, parámetro, exacta por definición, medida.

📘 **Dónde se aprende** (4 clases): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B07-C11 · Gestión de unidades en programas](../programa/clases/B07/B07-C11-gestion-de-unidades-en-programas/CLASE.md); [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md); [B45-C13 · Temperatura y espectro de cuerpo negro](../programa/clases/B45/B45-C13-temperatura-y-espectro-de-cuerpo-negro/CLASE.md).

### Constante cónica

- La constante cónica `k` (0 esfera, −1 paraboloide).

💡 **Contexto en la clase [B41-C04](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md):**
- **Idea central (modelo mental):** Como una antena parabólica de TV: todas las señales paralelas al eje convergen en el mismo punto; con un plato esférico la señal de los bordes llega antes.
- 🎯 **Por qué importa:** El espejo primario de un telescopio reflector es una superficie cónica. La decisión central: ¿por qué se usa un paraboloide y no una esfera?
- 🔗 **Se estudia junto con:** sagita, foco paraxial, aberración esférica longitudinal, espejo cóncavo.

📘 **Dónde se aprende** (2 clases): [B41-C04 · Espejos esféricos y parabólicos](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md); [B41-C17 · Telescopios Cassegrain y derivados](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md).

### Constante cosmológica

- La constante cosmológica `Λ` es una densidad de energía constante.

💡 **Cómo se explica en la clase [B26-C13](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md):**
- La materia frena la expansión como la gravedad frena una pelota; la constante cosmológica añade un empuje que no se diluye.
- *Descripción textual:* la tasa de expansión suma la materia, que decae como `a⁻³`, y la constante cosmológica; integrando `1/(aH)` se obtiene la edad, y el signo de `ä` marca el paso de frenar a acelerar.
- 🎯 **Por qué importa:** La edad del universo, la distancia a una galaxia y el calendario de su historia salen de la ecuación de Friedmann. Con ella se interpreta cualquier parámetro cosmológico.
- 🔗 **Se estudia junto con:** factor de escala, ecuación de Friedmann, densidad crítica, parámetro de densidad.

📘 **Dónde se aprende** (1 clase): [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md).

### Constante de Avogadro

- Su unidad es el mol: un mol contiene exactamente 6,022 140 76 × 10²³ entidades elementales, número que es el valor fijado de la constante de Avogadro `N_A` (en mol⁻¹), según la definición vigente del SI (S2).

💡 **Cómo se explica en la clase [B06-C06](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md):**
- De masa a cantidad se divide entre la masa molar; de cantidad a número de partículas se multiplica por la constante de Avogadro; las flechas inversas deshacen cada paso.
- Enunciar la definición del mol y el valor de la constante de Avogadro.
- 🎯 **Por qué importa:** La misión OSIRIS-REx trajo a la Tierra 121,6 g de material del asteroide Bennu. Los análisis de laboratorio de una parte de esa muestra encontraron entre 4,5 y 4,7 % de carbono y entre 0,23 y 0,25 % de nitrógeno en masa (S1).
- 🔗 **Se estudia junto con:** cantidad de sustancia, mol, masa molar, unidad de masa atómica.

📘 **Dónde se aprende** (1 clase): [B06-C06 · Cantidad de sustancia y mol](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md).

### Constante de Boltzmann

- El SI fija la constante de Boltzmann `k_B = 1,380 649 × 10⁻²³ J/K` (S3), que define el kelvin.

💡 **Contexto en la clase [B05-C13](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md):**
- **Idea central (modelo mental):** La temperatura de un satélite no la fija una «fuente de calor», sino el balance entre lo que absorbe del Sol y lo que irradia al espacio.
- 🎯 **Por qué importa:** Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: ¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?
- 🔗 **Se estudia junto con:** temperatura, calor, energía térmica, capacidad calorífica específica.

📘 **Dónde se aprende** (1 clase): [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md).

### Constante de consumo

- La constante de consumo `k` es la tasa de consumo de primer orden.

💡 **Contexto en la clase [B64-C06](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md):**
- **Idea central (modelo mental):** Los nutrientes entran por la superficie y las células de arriba los consumen primero; a mayor espesor o consumo, menos llega al fondo.
- 🎯 **Por qué importa:** Una película de células y matriz crea su propio microambiente. La pregunta motivadora: ¿hasta qué profundidad llega un nutriente en un biofilm y qué sucede con las células que quedan más adentro?
- 🔗 **Se estudia junto con:** matriz de EPS, difusividad efectiva, módulo de Thiele, factor de efectividad.

📘 **Dónde se aprende** (1 clase): [B64-C06 · Biofilms en ambientes extremos](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md).

### Constante de decaimiento

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B31-C08](../programa/clases/B31/B31-C08-decaimiento-radiactivo/CLASE.md):**
- **Idea central (modelo mental):** Los granos revientan al azar: no se sabe cuál, pero sí cuántos por segundo; la mitad habrá reventado en un tiempo fijo.
- 🎯 **Por qué importa:** Fechar rocas, medir la edad de objetos y modelar la nucleosíntesis usan estas leyes. La decisión central: ¿cómo se estima una constante de decaimiento y cómo evoluciona una cadena?
- 🔗 **Se estudia junto con:** semivida, vida media, actividad, cadena de Bateman.

📘 **Dónde se aprende** (1 clase): [B31-C08 · Decaimiento radiactivo](../programa/clases/B31/B31-C08-decaimiento-radiactivo/CLASE.md).

### Constante de degradación

- La constante de degradación `k` (1/d) fija la velocidad de pérdida.

💡 **Cómo se explica en la clase [B100-C04](../programa/clases/B100/B100-C04-almacenamiento-remoto-y-depositos-de-suministros/CLASE.md):**
- *Descripción textual:* la temperatura fija la constante de degradación y esta la vida útil; la fuga térmica fija la evaporación; ambas determinan cuánto hay que sobredimensionar.
- Límite: se supone un único mecanismo de degradación con una `Ea` constante; los materiales reales tienen varios y distintos.
- 🎯 **Por qué importa:** Guardar más cantidad para cubrir una ventana larga solo sirve si lo guardado sigue siendo útil al final. La decisión central: ¿cuánto sobredimensionar un depósito para que, tras la espera, quede la cantidad útil necesaria, y qué temperatura de almacenamiento reduce esa pérdida?
- 🔗 **Se estudia junto con:** ecuación de Arrhenius, vida útil t90, evaporación.

📘 **Dónde se aprende** (1 clase): [B100-C04 · Almacenamiento remoto y depósitos de suministros](../programa/clases/B100/B100-C04-almacenamiento-remoto-y-depositos-de-suministros/CLASE.md).

### Constante de desintegración

- La constante de desintegración `λ = 1/τ`.

💡 **Contexto en la clase [B27-C14](../programa/clases/B27/B27-C14-supernovas-termonucleares/CLASE.md):**
- **Idea central (modelo mental):** El níquel se agota rápido y alimenta al cobalto, que se agota despacio. La luz al principio la domina el níquel y después el cobalto, que fija la pendiente final.
- 🎯 **Por qué importa:** La luminosidad tardía de estas supernovas sigue la semivida del cobalto-56, y por eso se usan para medir distancias. La decisión central: ¿cuántos núcleos de cada especie quedan en cada instante y qué luminosidad producen?
- 🔗 **Se estudia junto con:** cadena de Bateman, semivida, vida media, deposición completa.

📘 **Dónde se aprende** (1 clase): [B27-C14 · Supernovas termonucleares](../programa/clases/B27/B27-C14-supernovas-termonucleares/CLASE.md).

### Constante de despresurización

- La constante de despresurización `τ = V/(C_d A √(γRT) · 0,5787)`.

💡 **Contexto en la clase [B104-C13](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md):**
- 🎯 **Por qué importa:** Un procedimiento sirve si se puede ejecutar dentro del tiempo disponible. La decisión central: ¿para qué tamaños de orificio alcanza un tiempo de respuesta de 15 minutos y a partir de cuál ya no?
- 🔗 **Se estudia junto con:** flujo ahogado, coeficiente de descarga, tiempo de respuesta.

📘 **Dónde se aprende** (1 clase): [B104-C13 · Procedimientos de emergencia](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md).

### Constante de equilibrio

- La constante de equilibrio `K` es el cociente entre productos y reactivos elevados a sus coeficientes, medido en el equilibrio.
- La constante de equilibrio `K = exp(−ΔG°/RT)`.

💡 **Cómo se explica en la clase [B06-C13](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md):**
- Abajo, una decisión: si el cociente de reacción es menor que la constante, el sistema avanza hacia productos; si es mayor, hacia reactivos; si es igual, está en equilibrio.
- Escribir la constante de equilibrio de una reacción, incluyendo sólidos y gases.
- 🎯 **Por qué importa:** Según el cálculo de esta clase, el CO₂ de Marte puede condensarse como hielo o volver al gas según la temperatura. Es un equilibrio entre CO₂ sólido y gas: `CO₂(s) ⇌ CO₂(g)`.
- 🔗 **Se estudia junto con:** equilibrio químico, sólidos y líquidos puros, cociente de reacción, actuales.

📘 **Dónde se aprende** (2 clases): [B06-C13 · Equilibrio químico](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md); [B56-C07 · Energía química para la vida](../programa/clases/B56/B56-C07-energia-quimica-para-la-vida/CLASE.md).

### Constante de estructura

- La constante de estructura `Cn²` mide la intensidad de la turbulencia, en m^(−2/3).

💡 **Contexto en la clase [B92-C04](../programa/clases/B92/B92-C04-atmosfera-y-nubes-en-enlaces-opticos-con-la-tierra/CLASE.md):**
- 🎯 **Por qué importa:** Un enlace espacial es perfecto hasta que llega a las últimas decenas de kilómetros. La decisión central: ¿cuánto margen exige la turbulencia y cuántas estaciones exige la nubosidad para cumplir una disponibilidad?
- 🔗 **Se estudia junto con:** parámetro de Fried, varianza de Rytov, desvanecimiento, diversidad de estaciones.

📘 **Dónde se aprende** (1 clase): [B92-C04 · Atmósfera y nubes en enlaces ópticos con la Tierra](../programa/clases/B92/B92-C04-atmosfera-y-nubes-en-enlaces-opticos-con-la-tierra/CLASE.md).

### Constante de estructura fina

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B31-C09](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md):**
- La constante de estructura fina calculada es `7,2973525643 × 10⁻³` (`1/α = 137,036`), igual a la de NIST (S1).
- 🎯 **Por qué importa:** Saber qué interacción domina en cada escala explica por qué los núcleos, los átomos y las estrellas son como son. La decisión central: ¿cuánto más fuerte es la fuerza eléctrica que la gravitatoria y qué fija el alcance de una fuerza?
- 🔗 **Se estudia junto con:** radio de Bohr, longitud de Compton, potencial de Yukawa, alcance.

📘 **Dónde se aprende** (1 clase): [B31-C09 · Interacciones fundamentales](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md).

### Constante de fuga

- La constante de fuga `τ` hace `p = p₀ e^(−t/τ)`.

💡 **Cómo se explica en la clase [B104-C05](../programa/clases/B104/B104-C05-sistemas-de-vehiculos-tripulados/CLASE.md):**
- Con una fuga de constante de tiempo de 72 h, la presión baja de 101,3 a 70 kPa en 26,6 h.
- Modelar una fuga lineal con una constante de tiempo y calcular el tiempo hasta un umbral.
- 🎯 **Por qué importa:** Lo que importa para respirar no es la presión total sino la presión parcial de cada gas. La decisión central: ¿cuánto tiempo hay para actuar si la cabina pierde presión o si se acumula CO₂?
- 🔗 **Se estudia junto con:** presión parcial, ley de Dalton, fuga, depuración.

📘 **Dónde se aprende** (1 clase): [B104-C05 · Sistemas de vehículos tripulados](../programa/clases/B104/B104-C05-sistemas-de-vehiculos-tripulados/CLASE.md).

### Constante de gravitación

- La constante de gravitación `G` tiene un valor medido (con incertidumbre) y unidades `m³ kg⁻¹ s⁻²`.

💡 **Cómo se explica en la clase [B05-C10](../programa/clases/B05/B05-C10-gravitacion-universal/CLASE.md):**
- Enunciar la ley de gravitación `F = G M m / r²` con su constante y unidades.
- 🎯 **Por qué importa:** La misma fuerza que hace caer una manzana mantiene a la Luna en órbita: esa idea unificó el cielo y la Tierra. La pregunta motivadora es: ¿cómo comprobar con números que la gravedad de la superficie y la órbita de la Luna son la misma fuerza?
- 🔗 **Se estudia junto con:** ley de gravitación universal, aceleración gravitatoria, ley del cuadrado inverso, parámetro gravitatorio.

📖 **Explicado a fondo:** [Constante de gravitación (G) y parámetro gravitacional (GM)](esencial/esencial-a-c.md#constante-de-gravitación-g-y-parámetro-gravitacional-gm) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B05-C10 · Gravitación universal](../programa/clases/B05/B05-C10-gravitacion-universal/CLASE.md); [B71-C02 · Ley de gravitación universal](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md).

### Constante de Hubble

- La constante de Hubble `H₀` es la razón entre la velocidad de recesión aparente y la distancia, hoy.
- La constante de Hubble `H₀` se da en `km s⁻¹ Mpc⁻¹`.

💡 **Contexto en la clase [B01-C16](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md):**
- **Idea central (modelo mental):** Imagina puntos dibujados sobre un globo que se infla: cualquier punto ve cómo todos los demás se alejan, más rápido los más lejanos, y ninguno es el centro. Eso resume la ley de Hubble: `v ∝ d`.
- 🎯 **Por qué importa:** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).
- 🔗 **Se estudia junto con:** ley de Hubble, tiempo de Hubble, expansión, velocidad peculiar.

📘 **Dónde se aprende** (2 clases): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md); [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md).

### Constante de integración

- La constante de integración `C` es un número arbitrario: derivar lo elimina.

💡 **Cómo se explica en la clase [B09-C08](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md):**
- En física, cada integración sucesiva trae su constante: la velocidad inicial y la posición inicial.
- El script [antiderivadas_y_potencial.py](antiderivadas_y_potencial.py) calcula antiderivadas de polinomios generalizados por la regla de la potencia, las comprueba derivando, integra el perfil de aceleración, muestra que dos antiderivadas difieren en una constante y evalúa el potencial terrestre y el sesgo del acelerómetro.
- ⚠️ **Error frecuente:** Olvidar la constante de integración. Se corrige con los ejercicios 1 y 7.
- 🎯 **Por qué importa:** Un acelerómetro mide aceleración; lo que se necesita es velocidad y posición. Una gravedad `g(r)` se conoce; lo que decide si una sonda escapa es la energía, que sale de «deshacer» esa derivada.
- 🔗 **Se estudia junto con:** antiderivada, integral indefinida, condición inicial, potencial gravitatorio.

📘 **Dónde se aprende** (1 clase): [B09-C08 · Integrales indefinidas](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md).

### Constante de Jacobi

- La constante de Jacobi es `C = 2Ω − v²` con `Ω = (x²+y²)/2 + (1−μ)/r₁ + μ/r₂`.
- La constante de Jacobi es `C = 2Ω − v²`, con `2Ω = x² + y² + 2(1−μ)/r₁ + 2μ/r₂`.
- La constante de Jacobi `C = 2Ω − v²` en el marco sinódico.

💡 **Cómo se explica en la clase [B73-C01](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md):**
- Una masa de prueba que parte de `(0,85, 0)` con velocidad `(0, −0,40)` en el marco sinódico tiene constante de Jacobi `C = 3,030382` y tras `20` unidades de tiempo (`86,97` d) está a `108018` km de la Luna, con una deriva de `C` de `6,94e-09`.
- Calcular la constante de Jacobi y medir su deriva.
- 🎯 **Por qué importa:** Con tres cuerpos no hay solución cerrada, pero sí una cantidad conservada que organiza todo lo demás: puntos de equilibrio, regiones prohibidas y transferencias de bajo costo. La decisión central: ¿cuándo basta el modelo de tres cuerpos restringido, y cómo sé que mi integración no inventa dinámica?
- 🔗 **Se estudia junto con:** CR3BP, parámetro de masa, marco sinódico, unidades adimensionales.

📘 **Dónde se aprende** (3 clases): [B73-C01 · Problema restringido de tres cuerpos](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md); [B73-C07 · Constante de Jacobi](../programa/clases/B73/B73-C07-constante-de-jacobi/CLASE.md); [B76-C08 · Transferencias de baja energía](../programa/clases/B76/B76-C08-transferencias-de-baja-energia/CLASE.md).

### Constante de Lipschitz

- La constante de Lipschitz `L` mide cuánto puede cambiar `f` cuando cambia `y`: `|f(t, y₁) − f(t, y₂)| ≤ L |y₁ − y₂|`.

💡 **Cómo se explica en la clase [B11-C02](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md):**
- En general, si `f` tiene constante de Lipschitz `L`, la diferencia crece como mucho como `δ e^{L t}`.
- Ejercicio 10 · transferencia. Para `f(y) = y²` en `|y| ≤ M`, ¿cuál es una constante de Lipschitz?
- 🎯 **Por qué importa:** Una nave no sigue «la» solución de las ecuaciones del movimiento: sigue la que corresponde a *su* posición y velocidad en el instante en que se midieron. Saber cuántos datos exige la ecuación, cuándo garantizan una única trayectoria y cuánto se amplifica su error es la base de toda predicción de trayectoria.
- 🔗 **Se estudia junto con:** problema de valor inicial, estado, instante inicial, bien planteada.

📘 **Dónde se aprende** (1 clase): [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md).

### Constante de proporcionalidad

- La constante de proporcionalidad `k` es ese valor fijo.

💡 **Contexto en la clase [B03-C10](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md):**
- **Idea central (modelo mental):** Para saber si dos magnitudes son proporcionales, miras la tabla: ¿algún cociente o producto se mantiene?
- 🎯 **Por qué importa:** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?
- 🔗 **Se estudia junto con:** directamente proporcionales, inversamente proporcionales, lineal, ley del inverso del cuadrado.

📘 **Dónde se aprende** (1 clase): [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md).

### Constante de radiación

- La constante de radiación es `a = 4σ/c`.

💡 **Contexto en la clase [B26-C14](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md):**
- **Idea central (modelo mental):** Cada fotón se estira con el universo: su longitud de onda crece como `a`, y la temperatura baja como `1/a`. La densidad de fotones cae como `a⁻⁴` (número `a⁻³` y energía `a⁻¹`), más rápido que la de materia (`a⁻³`).
- 🎯 **Por qué importa:** Casi todo lo observable del universo temprano (radiación de fondo, abundancia de helio) depende de su temperatura y de qué componente dominaba la densidad en cada época.
- 🔗 **Se estudia junto con:** radiación de fondo, densidad de energía de los fotones, parámetro de densidad de fotones, neutrinos.

📘 **Dónde se aprende** (1 clase): [B26-C14 · Evolución térmica del universo](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md).

### Constante de recuperación

- `τ` es la constante de recuperación dentro de una exposición.

💡 **Contexto en la clase [B113-C02](../programa/clases/B113/B113-C02-ansiedad-y-respuesta-emocional-en-escenarios-simulados/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR E1["exposición 1<br/>pico A1"] --> E2["exposición 2"] E2 --> E3["... exposición n"] E3 --> AI["nivel A_inf"] E1 --> REC["recuperación a(t) = pico e^(-t/tau)"] ``` *Descripción textual:* cada exposición tiene un pico menor que la anterior hasta un nivel `A_∞`; dentro de cada una, la activación decae con constante `τ`.
- 🎯 **Por qué importa:** Ninguna clase previa trata la respuesta emocional ante simulaciones de riesgo. La decisión central: ¿cuántas repeticiones de un escenario hacen falta para que el pico baje a un nivel de trabajo, y cuándo la repetición deja de ayudar?
- 🔗 **Se estudia junto con:** activación, habituación, tasa de habituación, sensibilización.

📘 **Dónde se aprende** (1 clase): [B113-C02 · Ansiedad y respuesta emocional en escenarios simulados](../programa/clases/B113/B113-C02-ansiedad-y-respuesta-emocional-en-escenarios-simulados/CLASE.md).

### Constante de Rydberg

- La constante de Rydberg `R` fija las longitudes de onda de las líneas del hidrógeno.

💡 **Cómo se explica en la clase [B02-C16](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md):**
- La constante de Rydberg para núcleo infinitamente pesado es `R∞ = 10 973 731,568 157 m⁻¹` (NIST, CODATA 2022, S2); para el hidrógeno se corrige por la masa del protón: `R_H = R∞/(1 + mₑ/mₚ)`, con `mₚ/mₑ = 1 836,152 673 426` (S3).
- 🎯 **Por qué importa:** Hasta 1859 se pensaba, con razones, que nunca sabríamos de qué están hechas las estrellas: estaban demasiado lejos para tocarlas. La pregunta motivadora es: ¿cómo se puede conocer la composición de un objeto que solo se ve como luz?
- 🔗 **Se estudia junto con:** espectro, espectro continuo, absorción, emisión.

📘 **Dónde se aprende** (3 clases): [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md); [B45-C10 · Líneas de emisión](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md); [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md).

### Constante de Stefan–Boltzmann

- La constante de Stefan–Boltzmann `σ` liga la energía emitida por unidad de superficie con `T⁴`.
- La constante de Stefan–Boltzmann `σ` liga la emisión de un cuerpo negro con `T⁴`.

💡 **Contexto en la clase [B01-C14](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md):**
- **Idea central (modelo mental):** Piensa en un triángulo con vértices temperatura, radio y luminosidad: dos de ellos fijan el tercero por Stefan–Boltzmann. Aparte, la luminosidad y la distancia fijan el flujo por el cuadrado inverso; y la temperatura fija el color por Wien.
- 🎯 **Por qué importa:** Dos estrellas pueden verse igual de brillantes y ser totalmente distintas: una pequeña y cercana, otra enorme y lejana (C09). Para saber cómo es una estrella necesitas separar lo que ves (flujo) de lo que ella es (luminosidad, temperatura, radio) y de dónde está (distancia).
- 🔗 **Se estudia junto con:** temperatura efectiva, luminosidad, radio, flujo.

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
- 🔗 **Se estudia junto con:** separable, lineal, factor integrante, equilibrio.

📘 **Dónde se aprende** (11 clases): [B11-C03 · Ecuaciones de primer orden](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md); [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B43-C11 · Dilatación térmica y estabilidad](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md); [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md); [B85-C11 · Ciclos térmicos](../programa/clases/B85/B85-C11-ciclos-termicos/CLASE.md) y 5 más.

### Constante de tiempo τ

- Nodo concentrado: modelo de una sola temperatura. Constante de tiempo `τ`: `m c/G`.
- Coeficiente de descarga `Cd`: corrección entre el área geométrica y la efectiva. Constante de tiempo `τ`: escala del vaciado exponencial.

💡 **Cómo se explica en la clase [B90-C11](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md):**
- Paso 1 · Constante de tiempo. `τ = m c/G = 1 800/2 = 900 s`.
- Plantear la ecuación de un nodo térmico concentrado y calcular su constante de tiempo.
- 🎯 **Por qué importa:** Una prueba funcional hecha antes de que la unidad se estabilice no demuestra nada sobre la temperatura extrema; una espera excesiva consume cámara y calendario. La decisión central: ¿cuánto debe esperar el ensayo para que la temperatura de la unidad sea la de la prueba?
- 🔗 **Se estudia junto con:** Nodo concentrado, Rampa, tiempo a temperatura constante, estado donde la unidad ya no cambia apreciablemente.

📘 **Dónde se aprende** (2 clases): [B90-C11 · Ensayos térmicos](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md); [B106-C02 · Presurización de módulos](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md).

### Constante de velocidad

- La constante de velocidad `k(T)` es el promedio térmico `⟨σ v⟩`.
- Una reacción de primer orden `A → productos` tiene velocidad `v = −d[A]/dt = k[A]`, con `k` la constante de velocidad (en 1/s).

💡 **Cómo se explica en la clase [B06-C14](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md):**
- Una reacción real puede tener varios pasos, orden distinto de 1 y una constante de velocidad que no se comporta como Arrhenius a baja temperatura.
- *Descripción textual:* arriba, dos valles separados por una barrera de altura `E_a`; abajo, la cadena: la temperatura fija la fracción de moléculas con energía suficiente, esa fracción da la constante de velocidad por Arrhenius, y la constante da la velocidad y la vida media.
- 🎯 **Por qué importa:** Que una reacción sea posible (energía favorable, `K` grande) no significa que ocurra: puede ser tan lenta que no ocurra nunca en la edad del universo. En una nube molecular a 10 K, la energía térmica es de apenas 0,86 meV (C10).
- 🔗 **Se estudia junto con:** velocidad de reacción, primer orden, vida media, energía de activación.

📘 **Dónde se aprende** (2 clases): [B06-C14 · Cinética química inicial](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md); [B60-C01 · Colisiones moleculares y secciones eficaces en gas interestelar](../programa/clases/B60/B60-C01-colisiones-moleculares-y-secciones-eficaces-en-gas-interestelar/CLASE.md).

### Constante definitoria

- Una constante definitoria del SI es una de las siete cuyo valor numérico se fija exactamente (S4).
- Una constante definitoria es una constante física a la que el SI asigna un valor numérico exacto; las unidades se definen fijándola (S2).

💡 **Cómo se explica en la clase [B13-C01](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir constante definitoria con constante medida. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Una señal de radio o de láser viaja a la Luna y regresa. Para decir «la Luna está a 384 400 km» hay que haber acordado qué es un kilómetro, qué es un segundo y a qué velocidad viaja la señal.
- 🔗 **Se estudia junto con:** Sistema Internacional de Unidades (SI), unidad base, exacto, magnitud.

📘 **Dónde se aprende** (2 clases): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md).

### Constante espectroscópica

- Una constante espectroscópica es un parámetro del Hamiltoniano efectivo (`B`, `D`, `H`…).

💡 **Contexto en la clase [B62-C05](../programa/clases/B62/B62-C05-constantes-espectroscopicas-y-ajuste-de-espectros/CLASE.md):**
- **Idea central (modelo mental):** Cada dato es una pesada con su error; los mínimos cuadrados buscan los valores que mejor equilibran todas las pesadas. Límite: supone errores independientes y gaussianos; si hay un error sistemático, la balanza se desplaza sin avisar.
- 🎯 **Por qué importa:** Una constante sin incertidumbre no se puede usar para predecir una línea en otro rango, ni para decidir si una línea observada es de esa molécula. La decisión central: ¿cuántos parámetros justifica el conjunto de datos?
- 🔗 **Se estudia junto con:** matriz de diseño, χ², χ² reducido, covarianza.

📘 **Dónde se aprende** (1 clase): [B62-C05 · Constantes espectroscópicas y ajuste de espectros](../programa/clases/B62/B62-C05-constantes-espectroscopicas-y-ajuste-de-espectros/CLASE.md).

### Constante física

- Una constante física es un valor con unidad, incertidumbre y referencia.

💡 **Contexto en la clase [B14-C04](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md):**
- **Idea central (modelo mental):** Piensa en cada valor como una moneda con su país. Puedes cambiarla de divisa con una tasa conocida, pero no sumar pesos con euros sin convertir. El programa lleva la divisa en la moneda y se niega a mezclarlas.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió al llegar a Marte. NASA atribuye la pérdida a un error de navegación causado por no traducir unidades inglesas a métricas: el software en tierra usaba unidades inglesas y el de a bordo, métricas (S1).
- 🔗 **Se estudia junto con:** unidad, dimensión, magnitud con unidad, conversión.

📘 **Dónde se aprende** (1 clase): [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### Constante molar de los gases

- La ley de los gases ideales relaciona la presión `P`, el volumen `V`, la cantidad de sustancia `n` y la temperatura absoluta `T`: `PV = nRT`, con `R` la constante molar de los gases.

💡 **Contexto en la clase [B06-C09](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md):**
- **Idea central (modelo mental):** Imagina bolitas muy pequeñas, lejos unas de otras, que rebotan contra las paredes de una caja. La presión es la fuerza media de esos choques; sube si las bolitas van más rápido (temperatura mayor) o si hay más (mayor densidad). A presión alta, las bolitas ya no están tan lejos y empiezan a notarse su tamaño y sus atracciones.
- 🎯 **Por qué importa:** La NASA publica para Marte, Venus y la Tierra la presión y la temperatura medias en la superficie, la gravedad, el peso molecular de la atmósfera y su densidad (S1, S2, S3). ¿Puedes reproducir esa densidad con sólo lo anterior?
- 🔗 **Se estudia junto con:** ley de los gases ideales, gas ideal, densidad, altura de escala.

📘 **Dónde se aprende** (1 clase): [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md).

### Constante psicrométrica γ

- La pendiente `Δ` de la curva de saturación y la constante psicrométrica `γ` acoplan temperatura y vapor.

💡 **Contexto en la clase [B115-C06](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md):**
- 🎯 **Por qué importa:** El cultivo es el mayor flujo de agua de un hábitat con plantas. La decisión central: ¿cuánta agua transpira el cultivo, cuánta se recupera y cuánta hay que reponer, y con qué incertidumbre?
- 🔗 **Se estudia junto con:** evapotranspiración de referencia (ETo), del cultivo (ETc), radiación neta (Rn), déficit de presión de vapor.

📘 **Dónde se aprende** (1 clase): [B115-C06 · Balance de agua y evapotranspiración en cultivos](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md).

### Constante rotacional

- La constante rotacional `B` es la energía por unidad de `J(J+1)` expresada en cm⁻¹.
- La constante rotacional `B` (MHz) depende del momento de inercia.

💡 **Cómo se explica en la clase [B62-C01](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md):**
- Calcular la constante rotacional `B` desde la masa reducida y la longitud de enlace.
- 🎯 **Por qué importa:** Una línea de CO a 115,27 GHz no es un dato aislado: es la consecuencia de un momento de inercia. Si entiendes de dónde sale, puedes predecir líneas que nadie ha medido y reconocer cuándo una línea observada no es del CO.
- 🔗 **Se estudia junto con:** rotor rígido, número cuántico rotacional, regla de selección, distorsión centrífuga.

📘 **Dónde se aprende** (2 clases): [B55-C09 · Espectros moleculares de radio](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md); [B62-C01 · Espectros rotacionales de moléculas: niveles y reglas de selección](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md).

### Constante rotacional del nivel

- La constante rotacional del nivel `B_v = Be − αe(v+½)` decrece al vibrar.

💡 **Contexto en la clase [B62-C02](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md):**
- **Idea central (modelo mental):** Un resorte con una masa en cada extremo: cuanto más se estira, más se ablanda (anarmonicidad). Límite: un resorte real se rompe o cambia de régimen; el modelo de `G(v)` vale lejos de la disociación.
- 🎯 **Por qué importa:** Las bandas del CO a 4,67 µm se observan en el infrarrojo, no en milimétricas. Para interpretarlas necesitas saber de dónde sale el origen de banda, por qué las ramas P y R se separan en dos grupos y qué cambia al pasar a un isotopólogo.
- 🔗 **Se estudia junto con:** energía vibracional, origen de banda, rama R, rama P.

📘 **Dónde se aprende** (1 clase): [B62-C02 · Espectros vibracionales de moléculas](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md).

### Constantes de Oort

- Las constantes de Oort `A` y `B` miden la rotación y la cizalla locales.

💡 **Cómo se explica en la clase [B25-C07](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md):**
- A["Curva de rotación<br/>Theta(R)"] --> B["Constantes de Oort<br/>A, B"]
- Bland-Hawthorn y Gerhard (S1) adoptan `R₀ = 8,2 kpc` y `Θ₀ = 238 km/s`, y definen las constantes de Oort por `A − B = Θ₀/R₀` y `A + B = −(∂Θ/∂R)_{R₀}`; recogen valores medidos de `A − B` entre `27` y `32 km s⁻¹ kpc⁻¹`, y describen una curva de rotación casi plana entre `5` y `13 kpc`.
- 🎯 **Por qué importa:** Las estrellas de una galaxia no giran en círculos perfectos: oscilan alrededor de una órbita circular, y su agitación revela la edad y la historia de la población. Además, no nacen todas con la misma masa: la función de masa inicial fija cuántas hay de cada tipo y cuánta luz y metales producirán.
- 🔗 **Se estudia junto con:** población estelar, órbita circular, epiciclo, radio guía.

📘 **Dónde se aprende** (1 clase): [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### Constantes de placa

- Las constantes de placa son los seis coeficientes de la relación lineal entre píxel y `(ξ, η)`.

💡 **Cómo se explica en la clase [B58-C06](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md):**
- Plantear el modelo lineal de seis constantes de placa.
- El script [astrometria.py](astrometria.py) proyecta, ajusta seis constantes de placa con 40 estrellas sintéticas y mide el error de un asteroide (comprueba ida y vuelta de 10⁻⁹, escala y rotación sin ruido con 10⁻⁹ y RMS entre 0,7 y 1,2 veces el esperado).
- 🎯 **Por qué importa:** Una órbita no puede ser mejor que sus posiciones: un error de décimas de segundo de arco se amplifica al propagar. La decisión central: ¿con qué exactitud puedo asignar coordenadas a un objeto en una imagen y qué la limita?
- 🔗 **Se estudia junto con:** proyección gnomónica, coordenadas estándar, astrometría, arrastre.

📘 **Dónde se aprende** (1 clase): [B58-C06 · Astrometría de objetos menores](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md).

### Constantes definitorias

- El SI (Sistema Internacional de Unidades) es el sistema acordado internacionalmente; sus siete unidades base son el segundo (s), el metro (m), el kilogramo (kg), el amperio (A), el kelvin (K), el mol (mol) y la candela (cd), definidas a partir de siete constantes definitorias de valor exacto (S2).

💡 **Contexto en la clase [B03-C06](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md):**
- **Idea central (modelo mental):** Las unidades se multiplican, dividen y elevan igual que los números, pero no se suman si son distintas.
- 🎯 **Por qué importa:** El 23 de septiembre de 1999 la NASA perdió contacto con la sonda Mars Climate Orbiter. Según la agencia, un error de navegación se debió a no traducir unidades inglesas a métricas: el programa en tierra usaba unas y el de la nave otras, y la sonda pasó demasiado cerca de Marte y se quemó en su atmósfera (S1).
- 🔗 **Se estudia junto con:** magnitud, unidad, SI, unidades base.

📘 **Dónde se aprende** (1 clase): [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md).

### Constelación

- Una constelación es, para la IAU, una de las 88 regiones en que se divide toda la esfera celeste, con límites definidos por líneas de ascensión recta y declinación (S1).
- Una constelación es un conjunto de satélites que operan coordinados.

💡 **Cómo se explica en la clase [B08-C06](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md):**
- Eugène Delporte, del Observatorio Real de Bruselas, trazó sus límites con líneas de ascensión recta y declinación; la asamblea de 1928 en Leiden los aprobó y se publicaron en 1930; hoy se distribuyen en coordenadas J2000, y las estrellas variables conocidas se mantuvieron en la constelación en que ya estaban (S1).
- Dos consecuencias: toda posición del cielo cae en una, y solo una, constelación; y el nombre de una constelación sirve para *localizar* («está en…»), no para describir lo que es.
- ⚠️ **Error frecuente:** Creer que una constelación es una agrupación física. Ejercicio 6.
- 🎯 **Por qué importa:** Dos personas dicen «la estrella roja de la Cruz del Sur» y creen hablar de lo mismo; un programa de telescopio pide «HIP 12345». Sin un lenguaje común no puedes repetir una observación ni compartirla.
- 🔗 **Se estudia junto con:** asterismo, catálogo, identificador, magnitud límite.

📖 **Explicado a fondo:** [Constelación y asterismo](esencial/cuarta-fundamentos.md#constelación-y-asterismo) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B08-C06 · Constelaciones y catálogos estelares](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md); [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md).

### Constelación grande

- Una constelación grande son muchos satélites con un mismo diseño.

💡 **Cómo se explica en la clase [B121-C03](../programa/clases/B121/B121-C03-proteccion-ambiental-en-la-legislacion-espacial/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué `p ≥ 0,9` no basta para una constelación grande?
- 🎯 **Por qué importa:** El catálogo no trata la mitigación de desechos como requisito normativo. La decisión central: ¿un diseño cumple el plazo de desorbitación, la probabilidad de éxito y el riesgo de reentrada que exige la norma?
- 🔗 **Se estudia junto con:** vida orbital, desorbitación, coeficiente balístico, altura de escala.

📘 **Dónde se aprende** (1 clase): [B121-C03 · Protección ambiental en la legislación espacial](../programa/clases/B121/B121-C03-proteccion-ambiental-en-la-legislacion-espacial/CLASE.md).

### Constelación oscura

- Una constelación oscura es una figura reconocida no en las estrellas sino en las zonas oscuras de la Vía Láctea, que corresponden a nubes de polvo (S1).

💡 **Cómo se explica en la clase [B02-C05](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md):**
- Describir ejemplos de alineaciones solares y de constelaciones oscuras en la literatura.
- 🎯 **Por qué importa:** Hablar de «astronomía andina» en singular es un error: los Andes reúnen sociedades de épocas y regiones muy distintas. La pregunta motivadora es: ¿cómo se estudia respetuosamente un cielo que otra cultura leyó de otra manera, sin imponerle nuestras categorías y sin inventar lo que las fuentes no dicen?
- 🔗 **Se estudia junto con:** cosmovisión, huaca, solsticio, orto helíaco.

📘 **Dónde se aprende** (1 clase): [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md).

### Constelación Walker delta

- Una constelación Walker delta `i:T/P/F` tiene `T` satélites en `P` planos con inclinación `i`;

💡 **Cómo se explica en la clase [B89-C17](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md):**
- Generar una constelación Walker delta `i:T/P/F`.
- 🎯 **Por qué importa:** El número de satélites, su altitud y la inclinación fijan cuánta gente o cuántos usuarios ven al menos uno (o cuatro, para navegar) y cuánto cuesta lograrlo. La decisión central: ¿cuántos satélites y qué geometría dan la cobertura necesaria?
- 🔗 **Se estudia junto con:** huella, cobertura simple, cuádruple, promedio global de visibles.

📘 **Dónde se aprende** (1 clase): [B89-C17 · Constelaciones y cobertura](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md).

### Consulta

- Una consulta selecciona filas y columnas con criterios.

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- La consulta (`paralaje > 2 mas` y `mag < 15`) devuelve 1594 filas, con distancia mediana 290,12 pc.
- No hay red, autenticación, reintentos, paginación ni descargas parciales; el servidor es local y la consulta ADQL no se envió, de modo que no sé qué respondería un servicio real.
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.
- 🔗 **Se estudia junto con:** flujo de datos, adquisición, verificación, caché.

📘 **Dónde se aprende** (1 clase): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md).

### Consulta de solapamiento

- Una consulta de solapamiento devuelve las cajas que se cruzan con la de consulta.

💡 **Cómo se explica en la clase [B14-C28](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md):**
- Q["Consulta<br/>caja o punto"] --> I["Índice R-tree<br/>candidatos por solapamiento"]
- *Descripción textual:* la consulta (caja o punto) va primero al índice, que devuelve candidatos por solapamiento; se refinan con una prueba exacta de geometría, se unen con los atributos por identificador y se obtiene el resultado.
- 🎯 **Por qué importa:** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.
- 🔗 **Se estudia junto con:** índice espacial, R-tree, tabla virtual, consulta puntual.

📘 **Dónde se aprende** (1 clase): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md).

### Consulta puntual

- Una consulta puntual devuelve las cajas que contienen un punto.

💡 **Contexto en la clase [B14-C28](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md):**
- **Idea central (modelo mental):** El índice responde «¿qué cajas podrían interesarte?» con rapidez y sin perder ninguna; después se refina con la prueba exacta si hace falta. En este experimento la geometría es la propia caja, así que el refinado es trivial.
- 🎯 **Por qué importa:** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.
- 🔗 **Se estudia junto con:** índice espacial, R-tree, tabla virtual, consulta de solapamiento.

📘 **Dónde se aprende** (1 clase): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md).

### Consume

- Una falla se consume si se termina después de su plazo.

💡 **Cómo se explica en la clase [B110-C04](../programa/clases/B110/B110-C04-priorizacion-y-decisiones-bajo-emergencia/CLASE.md):**
- Para el orden `(F2, F4, F5, F1, F3, F6)` se acumulan los esfuerzos y se compara con el plazo: F2 termina a `10 ≤ 15`, F4 a `30 ≤ 55`, F5 a `65 ≤ 120`, F1 a `95 > 90` (se consume una de vehículo), F3 a `120`, F6 a `135`.
- Términos `10, 30, 65, 95, 120, 135`; solo F1 (95 > 90) se consume: `(0, 1, 0)`.
- 🎯 **Por qué importa:** B104 enseña los procedimientos; falta cómo se ordenan cuando coinciden. La decisión central: ¿qué se atiende primero y cuánto cuesta equivocarse de orden?
- 🔗 **Se estudia junto con:** plazo, esfuerzo, pérdida lexicográfica, holgura.

📘 **Dónde se aprende** (1 clase): [B110-C04 · Priorización y decisiones bajo emergencia](../programa/clases/B110/B110-C04-priorizacion-y-decisiones-bajo-emergencia/CLASE.md).

### Consumo

- El consumo es `m = J_total/(Isp g₀)`.
- El consumo es la masa esperada de repuestos usados.

💡 **Cómo se explica en la clase [B87-C13](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md):**
- Estimar el consumo por hora de un ciclo límite.
- La evidencia es la ficha de consumo y ciclo límite de una maniobra con propulsores del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Los propulsores son el actuador de más par y de respuesta rápida, y el único que cambia el momento total del satélite, pero cada pulso gasta masa que no vuelve. La decisión central: ¿cuánto propergol cuesta una maniobra o un año de mantenimiento de actitud, y qué precisión permite el impulso mínimo?
- 🔗 **Se estudia junto con:** par, impulso mínimo, banda muerta, ciclo límite.

📘 **Dónde se aprende** (2 clases): [B87-C13 · Propulsores de control de actitud](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md); [B97-C19 · Logística de piezas y reparaciones](../programa/clases/B97/B97-C19-logistica-de-piezas-y-reparaciones/CLASE.md).

### Consumo específico

- El consumo específico `TSFC = f/(F/ṁ)`.

💡 **Cómo se explica en la clase [B79-C16](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md):**
- El empuje específico máximo (`838,4 N·s/kg`) está en `r = 15,80`, mientras que el consumo mínimo del barrido (`28,60`) está en el borde (`r = 40`): subir `r` ahorra combustible pero a costa de empuje por kg de aire, es decir, de tamaño del motor.
- Calcular el flujo de combustible, el empuje específico y el consumo específico.
- 🎯 **Por qué importa:** Ninguna clase cubre cómo se cuantifica la conversión de energía en propulsión. Sin eficiencias separadas, un cambio de diseño se evalúa a ciegas: no se sabe si mejora el ciclo o el aprovechamiento del chorro.
- 🔗 **Se estudia junto con:** eficiencia térmica, eficiencia propulsiva, eficiencia global.

📘 **Dónde se aprende** (1 clase): [B79-C16 · Eficiencias termodinámicas de motores](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md).

### Consumo específico de oxígeno

- Consumo específico de oxígeno: O₂ por kilogramo y minuto.

💡 **Cómo se explica en la clase [B106-C01](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md):**
- Calcular el oxígeno que consume una persona en reposo a partir de su consumo específico y compararlo con el valor consultado.
- 🎯 **Por qué importa:** Un hábitat se diseña de adentro hacia afuera: primero lo que consume y emite la tripulación, después la máquina que lo repone. Si el balance humano está mal, todo el ECLSS queda mal dimensionado.
- 🔗 **Se estudia junto con:** Cociente respiratorio (RQ), Normoxia, Zona de salud, zona de desempeño.

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
- 🔗 **Se estudia junto con:** retorno radial, endurecimiento isótropo, carga monotónica.

📘 **Dónde se aprende** (4 clases): [B84-C25 · Comportamiento estructural no lineal: plasticidad y contacto](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md); [B89-C13 · Protocolos para espacio profundo](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md); [B94-C04 · Redes con retardo y desconexión: enrutamiento y almacenamiento](../programa/clases/B94/B94-C04-redes-con-retardo-y-desconexion-enrutamiento-y-almacenamiento/CLASE.md); [B96-C02 · Concepto de operaciones de misión](../programa/clases/B96/B96-C02-concepto-de-operaciones-de-mision/CLASE.md).

### Contacto de Hertz

- El contacto de Hertz esfera-plano: `a = (3FR/(4E*))^(1/3)`.
- El contacto de Hertz da el radio de contacto `a = (3 Q R′/(4E*))^(1/3)` y la presión máxima `p₀ = 3Q/(2πa²)`.

💡 **Cómo se explica en la clase [B43-C25](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md):**
- Calcular `a`, `δ` y `p₀` de un contacto de Hertz.
- 🎯 **Por qué importa:** La rigidez del contacto determina cuánto se mueve el eje bajo carga y la frecuencia de resonancia. La decisión central: ¿cuánto se deforma el contacto, cuánta rigidez aporta y qué fracción de la carga soporta la bola más cargada?
- 🔗 **Se estudia junto con:** acercamiento, presión máxima, rigidez, reparto de Stribeck.

📘 **Dónde se aprende** (2 clases): [B43-C25 · Rodamientos y apoyos de precisión en telescopios](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md); [B84-C14 · Rodamientos y lubricación espacial](../programa/clases/B84/B84-C14-rodamientos-y-lubricacion-espacial/CLASE.md).

### Contacto de penalización

- Un contacto de penalización reacciona con una fuerza `k·penetración + c·velocidad` cuando hay interpenetración.

💡 **Cómo se explica en la clase [B102-C01](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md):**
- Una masa de 5 kg sobre un contacto de penalización `k = 2,0 × 10⁴ N/m` termina en reposo con una penetración `m g/k`: `2,4517 mm` en la Tierra, `0,9325 mm` en Marte y `0,4050 mm` en la Luna.
- Modelar un contacto unilateral con penalización y comparar la penetración estática con `m g/k`.
- 🎯 **Por qué importa:** Un manipulador de un rover se diseña y se ensaya en la Tierra, pero trabaja en Marte o en la Luna. La decisión central: ¿qué par necesita cada articulación en otro cuerpo, y qué cambia además del par?
- 🔗 **Se estudia junto con:** coordenadas generalizadas, matriz de masa, Coriolis y centrífugo, par de gravedad.

📘 **Dónde se aprende** (1 clase): [B102-C01 · Dinámica multicuerpo de rovers y manipuladores](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md).

### Contactos

- Los contactos son los instantes en que los discos se tocan.

💡 **Cómo se explica en la clase [B29-C01](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md):**
- T --> NUM["contactos numéricos z = 1 + k"]
- Verificar `T₁₄` buscando numéricamente los contactos.
- 🎯 **Por qué importa:** El tránsito es el método con más planetas descubiertos. Su profundidad da el radio del planeta y su duración informa del semieje y el parámetro de impacto.
- 🔗 **Se estudia junto con:** profundidad, duración, parámetro de impacto, oscurecimiento al limbo.

📘 **Dónde se aprende** (1 clase): [B29-C01 · Tránsitos planetarios](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md).

### Contador de canal maestro

- El contador de canal maestro (MCFC) cuenta todas las tramas; el de canal virtual (VCFC), las del canal.

💡 **Contexto en la clase [B94-C03](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md):**
- 🎯 **Por qué importa:** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?
- 🔗 **Se estudia junto con:** trama de transferencia de telemetría, SCID, VCID, canal virtual.

📘 **Dónde se aprende** (1 clase): [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### Contador de secuencia

- El contador de secuencia debe valer el anterior más uno.

💡 **Cómo se explica en la clase [B88-C09](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md):**
- El último caso muestra que, tras un `TO_SAFE` con secuencia fuera de orden, el contador queda en 200 y hay que resincronizarlo con un procedimiento definido.
- 🎯 **Por qué importa:** Un telecomando aceptado en el estado equivocado puede dañar la nave; uno rechazado en el estado correcto puede perderla. La decisión central: ¿qué comando es válido en cada modo y qué comprobaciones lo protegen?
- 🔗 **Se estudia junto con:** modo, transición, matriz estado–comando, CRC-8.

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
- 🔗 **Se estudia junto con:** meteorito, condrita, condritas carbonáceas, CI.

📘 **Dónde se aprende** (5 clases): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md); [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B45-C23 · Fotometría de apertura y estimación del cielo](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md); [B57-C30 · Nubes de puntos tridimensionales](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md); [B86-C14 · Envejecimiento de paneles](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md).

### Contaminación cruzada

- La contaminación cruzada es la transferencia desde otra muestra o del ambiente.

💡 **Contexto en la clase [B55-C18](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md):**
- **Idea central (modelo mental):** El blanco es la luz de fondo de la habitación; la señal es una linterna. Solo se la ve si supera claramente las fluctuaciones del fondo, y cuanto más variable el fondo, más fuerte debe ser la linterna. ```mermaid flowchart LR M["medida"] --> N["neta = M − blanco"] B["blanco, s, n"] --> N B --> L["LOD = 3s, LOQ = 10s"] N --> C["¿neta > LOD?
- 🎯 **Por qué importa:** En muestras extraterrestres la cantidad buscada puede ser del orden de la contaminación que entra al manipularlas. La decisión central: ¿la señal neta supera el límite de detección y con qué incertidumbre, una vez restado el blanco?
- 🔗 **Se estudia junto con:** señal neta, incertidumbre neta, LOD, LOQ.

📘 **Dónde se aprende** (1 clase): [B55-C18 · Contaminación de muestras](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md).

### Contaminación lumínica

- La contaminación lumínica es el exceso de luz artificial que borra la visibilidad del cielo nocturno.
- La contaminación lumínica es la luz artificial que degrada el cielo nocturno.
- La contaminación lumínica es el brillo del cielo nocturno por luz artificial emitida o reflejada hacia arriba, y su efecto sobre la observación y los ecosistemas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C06](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md):**
- Ejercicio 10 · transferencia. El autor de S3 propone considerar la contaminación lumínica como pérdida cultural.
- 🎯 **Por qué importa:** Chile alberga algunos de los cielos más oscuros del mundo y los más grandes observatorios, y también pueblos que miraron esos cielos durante milenios. La pregunta motivadora es: ¿cómo hablar de saberes celestes de pueblos vivos sin generalizar, sin apropiarse y sin presentar como establecido lo que no hemos podido verificar?
- 🔗 **Se estudia junto con:** pueblo originario, consentimiento libre, previo e informado, saber.

📖 **Explicado a fondo:** [Contaminación lumínica](esencial/ampliacion-a-m.md#contaminación-lumínica) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B02-C06 · Astronomía de pueblos originarios de Chile](../programa/clases/B02/B02-C06-astronomia-de-pueblos-originarios-de-chile/CLASE.md); [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md); [B08-C12 · Limitación por contaminación lumínica](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md); [B48-C18 · Protección del cielo oscuro](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md).

### Contaminación molecular

- La contaminación molecular es una película condensada; su espesor sale de `m/ρ`.

💡 **Cómo se explica en la clase [B85-C16](../programa/clases/B85/B85-C16-polvo-lunar-y-contaminacion/CLASE.md):**
- Contaminacion molecular ILUSTRATIVA: 0.10 g condensables llegan al radiador -> espesor 0.100 um ; delta alfa = 0.0500 ;
- 🎯 **Por qué importa:** Un radiador que se ensucia rechaza menos calor y se calienta; en la Luna la limpieza no es sencilla. La decisión central: ¿qué cobertura de polvo o espesor de película hace subir la temperatura de un radiador por encima de su límite?
- 🔗 **Se estudia junto con:** cobertura, absortividad efectiva, radiador.

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
- 🔗 **Se estudia junto con:** log-odds, línea de evidencia, umbral de comunicación, transparencia.

📘 **Dónde se aprende** (5 clases): [B56-C19 · Ética del descubrimiento de vida](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md); [B63-C05 · Contención de muestras extraterrestres: instalaciones y principios](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md); [B106-C10 · Gestión de residuos humanos](../programa/clases/B106/B106-C10-gestion-de-residuos-humanos/CLASE.md); [B117-C02 · Contención de riesgos biológicos y químicos en cabina](../programa/clases/B117/B117-C02-contencion-de-riesgos-biologicos-y-quimicos-en-cabina/CLASE.md); [B122-C06 · Respuesta a incidentes cibernéticos en operaciones de misión](../programa/clases/B122/B122-C06-respuesta-a-incidentes-ciberneticos-en-operaciones-de-mision/CLASE.md).

### Contenedor

- Una imagen es el paquete inmutable; un contenedor es una instancia en ejecución de una imagen.

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- Según S1, un contenedor es autocontenido y aislado, y comparte el núcleo del anfitrión.
- Por eso dos contenedores idénticos en máquinas distintas pueden diferir en el último dígito de un cálculo (C10) si el procesador es distinto.
- ⚠️ **Error frecuente:** Creer que el contenedor lo reproduce todo. Se corrige con los ejercicios 3 y 8.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?
- 🔗 **Se estudia junto con:** imagen, Dockerfile, capa, caché de capas.

📘 **Dónde se aprende** (1 clase): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md).

### Contenido

- El contenido del elipsoide `k²` es la probabilidad de que el error caiga dentro.

💡 **Cómo se explica en la clase [B74-C11](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md):**
- En 3D el contenido de un elipsoide `1σ` es solo `0,1987`.
- Descripción larga: rotar no cambia la incertidumbre total; la correlación aplana el elipsoide; el contenido de un elipsoide de k sigma en 3D es mucho menor que el intervalo 1D.
- 🎯 **Por qué importa:** Los números de la diagonal engañan: dos errores muy correlacionados pueden ser individualmente grandes y conjuntamente pequeños. La decisión central: ¿qué dicen realmente los autovalores, las correlaciones y el elipsoide, y qué probabilidad encierra cada «k sigma» en tres dimensiones?
- 🔗 **Se estudia junto con:** matriz de covarianza, autovalores, elipsoide de error, correlación.

📘 **Dónde se aprende** (1 clase): [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Contenido canónico

- El contenido canónico es una forma de escribir el registro con claves ordenadas y sin espacios, para que el hash sea reproducible.

💡 **Cómo se explica en la clase [B13-C19](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md):**
- El contenido canónico (claves ordenadas, sin espacios) del registro, sin el campo `sha256`, se codifica en UTF-8 y se procesa con SHA-256; el resultado se guarda en el propio registro.
- R --> H["Hash SHA-256<br/>del contenido canónico"]
- 🎯 **Por qué importa:** Dentro de un año alguien usará los datos de un fotodiodo calibrado hoy. Necesitará saber con qué patrones, a qué temperatura, con qué incertidumbre y hasta cuándo es válida la calibración.
- 🔗 **Se estudia junto con:** metadato, registro de calibración, trazabilidad documentada, vigencia.

📘 **Dónde se aprende** (1 clase): [B13-C19 · Metadatos y registros de calibración](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md).

### Contenido electrónico total

- El contenido electrónico total (TEC), en TECU (`1 TECU = 10¹⁶ m⁻²`).

💡 **Contexto en la clase [B51-C05](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md):**
- **Idea central (modelo mental):** Como un prisma que desvía más la luz azul que la roja: la ionosfera retrasa más las frecuencias bajas, y por eso dos frecuencias bastan para medir cuánto prisma hay en el camino.
- 🎯 **Por qué importa:** A frecuencias bajas la ionosfera domina el error de fase y de polarización. La decisión central: ¿cómo se mide y se quita el efecto con las propias frecuencias de la observación?
- 🔗 **Se estudia junto con:** retardo dispersivo, rotación de Faraday, medida de rotación, ambigüedad nπ.

📘 **Dónde se aprende** (1 clase): [B51-C05 · Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md).

### Conteo

- El conteo `N ~ Poisson(sH + B)`.

💡 **Cómo se explica en la clase [B105-C07](../programa/clases/B105/B105-C07-dosimetria-personal/CLASE.md):**
- En 20.000 repeticiones por dosis, el intervalo `Ĥ ± 1,96 σ_H` cubre el valor verdadero entre 0,949 y 0,950 de los casos: la aproximación gaussiana funciona con estos conteos.
- Con seis dosis de referencia (1, 2, 5, 10, 20 y 50 mSv) y conteos sintéticos, `ŝ = Σ H y/Σ H² = 197,04` cuentas/mSv (verdad 200).
- 🎯 **Por qué importa:** Un número de dosis sin su incertidumbre no es utilizable: cerca del fondo, el dosímetro no distingue una dosis pequeña de cero. La decisión central: ¿desde qué dosis se puede afirmar que el dosímetro vio algo y con qué incertidumbre se informa?
- 🔗 **Se estudia junto con:** estimador, límite crítico, límite de detección, calibración.

📘 **Dónde se aprende** (1 clase): [B105-C07 · Dosimetría personal](../programa/clases/B105/B105-C07-dosimetria-personal/CLASE.md).

### Conteo acumulado

- El conteo acumulado `N(>d)` es el número de objetos mayores que `d`.

💡 **Cómo se explica en la clase [B118-C01](../programa/clases/B118/B118-C01-poblacion-de-objetos-orbitales/CLASE.md):**
- *Descripción textual:* de dos conteos acumulados se obtiene la pendiente de la distribución de tamaños; de la población sintética se obtiene el conteo por capa y, dividido por el volumen, la densidad espacial.
- 🎯 **Por qué importa:** Los catálogos solo contienen los objetos que los sensores pueden seguir; el resto se conoce por modelos y por mediciones in situ. Esta clase fija el vocabulario cuantitativo (conteos acumulados, pendiente, densidad) que usan todas las demás.
- 🔗 **Se estudia junto con:** objeto seguido, desecho, pendiente, densidad espacial.

📘 **Dónde se aprende** (1 clase): [B118-C01 · Población de objetos orbitales](../programa/clases/B118/B118-C01-poblacion-de-objetos-orbitales/CLASE.md).

### Conteo cíclico

- Un conteo cíclico cuenta una parte del inventario cada vez.

💡 **Cómo se explica en la clase [B100-C01](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md):**
- *Descripción textual:* los lotes entran al almacén; salen por emisión (que queda registrada) o por caducidad; el conteo cíclico compara el registro con lo físico.
- Calcular la exactitud del registro con un conteo cíclico.
- 🎯 **Por qué importa:** Un inventario que solo sabe «cuántas unidades hay» no puede decir de qué lote vienen, cuándo caducan ni dónde se usaron. La decisión central: ¿qué registro mínimo hace falta para emitir primero lo que caduca antes y para encontrar, si un lote resulta defectuoso, adónde fue?
- 🔗 **Se estudia junto con:** lote, FIFO, FEFO, Caducado.

📘 **Dónde se aprende** (1 clase): [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Conteo de fotones

- El conteo de fotones registra eventos individuales en vez de energía.
- El conteo de fotones registra eventos individuales.

💡 **Cómo se explica en la clase [B92-C05](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md):**
- *Descripción textual:* la ranura con pulso recibe señal y fondo, las otras solo fondo; el receptor elige la ranura de mayor conteo, de ahí sale el error de símbolo y los fotones necesarios; el tiempo muerto limita la tasa medible.
- Como contexto publicado, el receptor de DSOC en Palomar es un receptor de conteo de fotones de nanohilos superconductores (NASA/JPL), sin más especificaciones en la página consultada.
- 🎯 **Por qué importa:** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?
- 🔗 **Se estudia junto con:** detección directa, eficiencia de detección, conteos oscuros, fondo.

📘 **Dónde se aprende** (2 clases): [B57-C11 · LiDAR satelital](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md); [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Conteo de Poisson

- El conteo de Poisson tiene varianza igual a su media.

💡 **Cómo se explica en la clase [B67-C07](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md):**
- *Descripción textual:* un parámetro físico (la abundancia) produce una señal media; el azar de Poisson la convierte en un conteo; el cálculo inverso devuelve la abundancia con su incertidumbre, y lo mismo con el espectro de masas.
- Invertir un conteo de Poisson y propagar su incertidumbre.
- 🎯 **Por qué importa:** Un sensor no mide «agua»: mide cuentas, y de ellas se infiere la abundancia con un modelo. La decisión central: ¿cuánto tiempo de medición y qué canales hacen falta para detectar y separar un volátil con la incertidumbre requerida?
- 🔗 **Se estudia junto con:** tasa de neutrones epitérmicos, abundancia equivalente en agua (WEH), espectrometría de masas, patrón de fragmentación.

📘 **Dónde se aprende** (1 clase): [B67-C07 · Sensores para volátiles: espectrometría de neutrones y de masas](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md).

### Conteo independiente

- El conteo independiente es un recuento por un método distinto del que se verifica.
- Un conteo independiente usa otro método (C18).

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- Un conteo independiente, con arreglos de NumPy y sin pandas, da 1594: coincide.
- Comprueba con un conteo independiente: 1594.
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.
- 🔗 **Se estudia junto con:** flujo de datos, adquisición, verificación, caché.

📘 **Dónde se aprende** (2 clases): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md); [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md).

### Conteos esperados

- Los conteos esperados son `N [P(X>u_k) − P(X>u_{k+1})]`.

💡 **Cómo se explica en la clase [B33-C04](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md):**
- *Descripción textual:* los umbrales definen niveles; la cola de potencias da conteos esperados que el Monte Carlo verifica.
- Calcular conteos esperados de una cola de potencias.
- 🎯 **Por qué importa:** Comparar severidades exige conocer cómo se definió cada nivel. La decisión central: ¿cuántos eventos caen en cada nivel y por qué no son comparables entre escalas?
- 🔗 **Se estudia junto con:** escala, nivel, razón, cola de potencias.

📘 **Dónde se aprende** (1 clase): [B33-C04 · Escalas de severidad de clima espacial](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md).

### Conteos «off»

- Los conteos «off» `N_off` son los de una región de fondo.

💡 **Cómo se explica en la clase [B27-C19](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md):**
- *Descripción textual:* los conteos alimentan dos fórmulas de significancia; el Monte Carlo bajo la hipótesis nula compara sus tasas de falsos positivos; la razón de verosimilitudes sirve para hallar la señal mínima.
- Aquí no se usa ninguna cifra de su rendimiento: los conteos son sintéticos.
- 🎯 **Por qué importa:** Decir «detectamos la fuente a 5σ» exige saber qué fórmula se usó y cuántos falsos positivos produce. La decisión central: ¿qué significancia tiene un par de conteos y qué señal mínima se necesita para una detección?
- 🔗 **Se estudia junto con:** conteos «on», cociente de exposición, significancia, semilla.

📘 **Dónde se aprende** (1 clase): [B27-C19 · Observatorios de rayos X y gamma](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md).

### Conteos «on»

- Los conteos «on» `N_on` son los de la región de la fuente.

💡 **Cómo se explica en la clase [B27-C19](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md):**
- *Descripción textual:* los conteos alimentan dos fórmulas de significancia; el Monte Carlo bajo la hipótesis nula compara sus tasas de falsos positivos; la razón de verosimilitudes sirve para hallar la señal mínima.
- Aquí no se usa ninguna cifra de su rendimiento: los conteos son sintéticos.
- 🎯 **Por qué importa:** Decir «detectamos la fuente a 5σ» exige saber qué fórmula se usó y cuántos falsos positivos produce. La decisión central: ¿qué significancia tiene un par de conteos y qué señal mínima se necesita para una detección?
- 🔗 **Se estudia junto con:** conteos «off», cociente de exposición, significancia, semilla.

📘 **Dónde se aprende** (1 clase): [B27-C19 · Observatorios de rayos X y gamma](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md).

### Conteos oscuros

- Los conteos oscuros y el fondo son eventos sin señal.

💡 **Contexto en la clase [B92-C05](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md):**
- 🎯 **Por qué importa:** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?
- 🔗 **Se estudia junto con:** detección directa, conteo de fotones, eficiencia de detección, fondo.

📘 **Dónde se aprende** (1 clase): [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Contexto

- El contexto y el objeto y fin son fuentes que restringen la lectura.
- El contexto (`info`) distingue propósito y época.

💡 **Cómo se explica en la clase [B88-C38](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md):**
- Se extrae con una sal y se expande con el contexto `propósito|época=n`.
- Paso 2 · Derivar. `expand(PRK, contexto, 32)`.
- 🎯 **Por qué importa:** Una clave filtrada o reutilizada anula toda la autenticación. La decisión central: ¿cómo se separan las claves por función y época para que el compromiso de una no arrastre a las demás?
- 🔗 **Se estudia junto con:** extracción, expansión, separación de claves, rotación.

📘 **Dónde se aprende** (2 clases): [B88-C38 · Gestión de claves y secretos en aviónica](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md); [B119-C32 · Interpretación de tratados internacionales](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md).

### Contexto ritual y social

- El contexto ritual y social es el conjunto de prácticas, calendarios, jerarquías y creencias en que se inscribe una observación del cielo.

💡 **Cómo se explica en la clase [B132-C05](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md):**
- python programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/contexto.py
- 🎯 **Por qué importa:** El catálogo trata alineaciones sin ese contexto. La decisión central: ¿cuánto apoyo da cada línea de evidencia a la intención de una alineación, y qué parte de la conclusión depende de lo que se supone de antemano?
- 🔗 **Se estudia junto con:** línea de evidencia, factor de Bayes, cota de Sellke–Bayarri–Berger, descuento por dependencia.

📘 **Dónde se aprende** (1 clase): [B132-C05 · Contexto ritual y social de la observación del cielo](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md).

### Contingencia

- DITL: prueba de «día en la vida». Contingencia: tiempo reservado para fallas.

💡 **Cómo se explica en la clase [B90-C20](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md):**
- Para una confianza de 90 % hay que reservar `25 − 15 = 10 d` de contingencia sobre los 15 d sin fallas.
- Por calendario: duración y contingencia (esta clase).
- ⚠️ **Error frecuente:** Planificar con la duración sin fallas. Reserva contingencia (8.4)
- 🎯 **Por qué importa:** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?
- 🔗 **Se estudia junto con:** Campaña de calificación, Flujo de ensayos, Fit check, DITL.

📘 **Dónde se aprende** (1 clase): [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### Continua

- Es discreta si toma valores aislados y continua si toma cualquier valor de un intervalo (S1, C.2.2, nota 1).

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- Su límite: en una variable continua no hay pilas contables; la «pila» de un valor exacto pesa cero y sólo pesan los intervalos.
- Paso 1 · Variables. `X` discreta (pmf de 8.1), `Y` continua (8.3); se supone que `X` e `Y` son independientes (el telémetro no depende de los computadores en este modelo).
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.
- 🔗 **Se estudia junto con:** variable aleatoria, discreta, función de masa de probabilidad, función de distribución acumulada.

📘 **Dónde se aprende** (1 clase): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md).

### Continua en a

- Una función `f` es continua en `a` si existen `f(a)` y `lim_{x→a} f(x)` y son iguales (S1, §1.4(ii)).

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- Para comprobar que `f(x) = x² + 1` es continua en 2: `f(2) = 5`, el límite es 5, coinciden.
- Para polinomios, exponenciales, senos y cosenos basta evaluar; sumas, productos y composiciones de funciones continuas son continuas (S1).
- ⚠️ **Error frecuente:** Creer que «definida» implica «continua». Se corrige con el ejercicio 1.
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.
- 🔗 **Se estudia junto con:** discontinuidad, removible, de salto, infinita.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Continua por tramos

- Una función es continua por tramos si lo es salvo en un número finito de saltos.

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- Calcular el valor que hace continua una función definida por tramos.
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.
- 🔗 **Se estudia junto con:** continua en a, discontinuidad, removible, de salto.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Continuación

- La continuación sigue la familia en `A`.

💡 **Cómo se explica en la clase [B76-C06](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md):**
- Una búsqueda directa a `70.000 km` puede caer en otra solución; la continuación evita ese riesgo.
- Seguir la familia por continuación en la amplitud.
- ⚠️ **Error frecuente:** Buscar la DRO sin continuación. Se corrige con 8.2.
- 🎯 **Por qué importa:** La NRHO es inestable y exige mantenimiento; la DRO es estable. La decisión central: ¿qué se gana y qué se paga al elegir una órbita estable y lejana frente a una NRHO cercana?
- 🔗 **Se estudia junto con:** DRO, amplitud, monodromia plana, par doble en 1.

📘 **Dónde se aprende** (1 clase): [B76-C06 · Órbitas DRO — Dinámica cislunar y operaciones de proximidad](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md).

### Continuidad

- La continuidad estacionaria dice que `ṁ` es el mismo en todas las secciones.
- La continuidad exige que `P` y `e` coincidan en la unión.

💡 **Cómo se explica en la clase [B27-C04](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md):**
- Para `ρ < ρ_t`, `P = K₁ρ^{Γ₁}`; para `ρ ≥ ρ_t`, `P = K₂ρ^{Γ₂}` con `K₂ = K₁ρ_t^{Γ₁−Γ₂}` (continuidad de `P`).
- El laboratorio comprueba ambas continuidades a `10⁻¹²`.
- 🎯 **Por qué importa:** Las estrellas de neutrones son el único laboratorio de materia más allá de la densidad nuclear. Su EOS no se conoce con precisión; las medidas de masa máxima y de radio la acotan.
- 🔗 **Se estudia junto con:** EOS por tramos, velocidad del sonido, causalidad, masa máxima.

📘 **Dónde se aprende** (2 clases): [B27-C04 · Ecuación de estado nuclear](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md); [B79-C01 · Conservación de masa en fluidos](../programa/clases/B79/B79-C01-conservacion-de-masa-en-fluidos/CLASE.md).

### Continuo

- Un modelo es lineal si cumple superposición (lo precisa C03), invariante si sus parámetros no cambian con el tiempo, continuo si el tiempo es una variable real `t` y discreto si solo existe en instantes `kT`.
- El continuo es la opacidad de fondo.
- El continuo es la línea base sin la banda.

💡 **Cómo se explica en la clase [B16-C01](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md):**
- El modelo de la sección 8.2 es lineal (el estado aparece solo multiplicado por constantes), invariante (`J` no cambia), continuo y de orden 2.
- Un modelo continuo describe el fenómeno; uno discreto describe lo que ve el computador de a bordo, que mide y actúa cada `T` segundos (C02).
- 🎯 **Por qué importa:** Un telescopio espacial tiene que apuntar a una estrella y mantenerse allí. El telescopio Hubble lo hace con una desviación de no más de 0,007 segundos de arco durante al menos 24 horas (fuente S2).
- 🔗 **Se estudia junto con:** sistema, entrada, perturbación, salida.

📘 **Dónde se aprende** (4 clases): [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md); [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B32-C10 · Normalización y modelado del continuo espectral](../programa/clases/B32/B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md); [B53-C17 · Mineralogía espectral](../programa/clases/B53/B53-C17-mineralogia-espectral/CLASE.md).

### Contracción

- La contracción (*shrinkage*) acerca cada `y_j` a la media del conjunto con peso `B_j = σ_j²/(σ_j² + τ²)`: la media posterior condicionada a `τ` es `(1 − B_j) y_j + B_j μ̂`.
- La contracción de un par de índices los iguala y suma: `Tᵢᵢ` (traza), `Tᵢⱼ bⱼ` (producto por un vector), `aᵢ bᵢ` (producto escalar).

💡 **Cómo se explica en la clase [B10-C18](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md):**
- La contracción de sus dos índices da `4 + 10 + 18 = 32 = a · b`, y la contracción de un índice con `b` da `(a ⊗ b) b = a (b · b)`.
- Paso 3 · Contracción. `δa = T δx = (2,3242 × 10⁻⁵; 0; 0) m/s²`.
- 🎯 **Por qué importa:** La gravedad no es uniforme a lo largo de un satélite: lo que está más cerca de la Tierra se acelera más que lo que está lejos, y lo que está a los lados se comprime. Con una sola derivada `dg/dr` solo describes la dirección radial; el tensor de marea describe las tres direcciones a la vez.
- 🔗 **Se estudia junto con:** producto tensorial, rango 1, traza, gradiente.

📘 **Dónde se aprende** (2 clases): [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md); [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md).

### Contracción de longitudes

- La contracción de longitudes dice que, en un marco donde el objeto se mueve, su longitud a lo largo del movimiento es `L = L₀/γ`.

💡 **Contexto en la clase [B26-C03](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md):**
- **Idea central (modelo mental):** Desde el laboratorio, el muón vive más porque su reloj va lento. Desde el muón, vive lo habitual, pero la atmósfera que se le acerca está contraída. Los dos relatos dan el mismo número de muones que llegan.
- 🎯 **Por qué importa:** Los muones se producen en la alta atmósfera por rayos cósmicos, viven microsegundos y, sin embargo, llegan al suelo en cantidad. Los relojes de satélites de navegación se ajustan por el mismo efecto.
- 🔗 **Se estudia junto con:** tiempo propio, tiempo coordenado, dilatación temporal, longitud propia.

📘 **Dónde se aprende** (1 clase): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md).

### Contracción global

- La contracción global reduce el radio `ΔR/R = ε/2`, con `ε` la deformación areal.

💡 **Contexto en la clase [B53-C12](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md):**
- **Idea central (modelo mental):** Analogía: una regla de madera apoyada sobre una cama de resortes: la carga la hunde y, más lejos, la levanta un poco.
- 🎯 **Por qué importa:** La flexión revela el espesor elástico de la litosfera y la contracción, el balance térmico global. La decisión central: ¿qué espesor elástico y qué acortamiento explican la deformación observada?
- 🔗 **Se estudia junto con:** rigidez flexural, parámetro flexural, abombamiento periférico.

📘 **Dónde se aprende** (1 clase): [B53-C12 · Tectónica planetaria](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md).

### Contrachorro

- El contrachorro es el que se aleja.

💡 **Cómo se explica en la clase [B27-C11](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md):**
- Por cociente chorro/contrachorro: observacional.
- Estimar la razón de brillos entre el chorro y el contrachorro.
- ⚠️ **Error frecuente:** Olvidar el contrachorro. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un chorro que se acerca puede parecer más rápido que la luz sin violar nada, y su brillo cambia en órdenes de magnitud según el ángulo. Sin estos efectos no se pueden comparar chorros ni inferir su velocidad.
- 🔗 **Se estudia junto con:** velocidad aparente, movimiento superlumínico aparente, factor Doppler, cono de emisión.

📘 **Dónde se aprende** (1 clase): [B27-C11 · Chorros relativistas](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md).

### Contracorriente

- El esquema contracorriente (*upwind*) para `u_t + c u_x = 0` con `c > 0` usa el nodo de aguas arriba: `u_i^{n+1} = u_i^n − ν (u_i^n − u_{i−1}^n)`.

💡 **Cómo se explica en la clase [B11-C14](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md):**
- Para `u_t + c u_x = 0`, el esquema contracorriente es estable si `ν = c Δt/Δx ≤ 1`: la información no puede cruzar más de una celda por paso.
- Contracorriente: para advección, orden 1, estable con `ν ≤ 1` y que difunde el pulso (suaviza la forma).
- 🎯 **Por qué importa:** Casi todo código de simulación de calor, fluidos o plasma en una malla regular usa diferencias finitas. Elegir el paso de tiempo equivocado no da un resultado ligeramente malo: da un resultado que explota.
- 🔗 **Se estudia junto con:** malla, esquema FTCS, esquema BTCS, error de truncamiento.

📘 **Dónde se aprende** (1 clase): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md).

### Contraejemplo

- Un contraejemplo es un caso concreto que hace falsa una afirmación.

💡 **Cómo se explica en la clase [B10-C01](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md):**
- Contraejemplo. `W = {(x, y, 1)}`, el plano `z = 1`: `(0, 0, 0)` no está, y `(1, 0, 1) + (0, 1, 1) = (1, 1, 2)` no está.
- Contraejemplo numérico: basta uno para refutar.
- 🎯 **Por qué importa:** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.
- 🔗 **Se estudia junto con:** espacio vectorial real, cero, opuesto, escalar.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Contraluz

- El contraluz es una fase mayor que `120°` (hipótesis).

💡 **Cómo se explica en la clase [B76-C18](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md):**
- Con `β = 0` solo el `30,5 %` de la órbita está al sol con buena fase; con `β` alto hay más sol pero el contraluz deja de ser el límite y la fase se limita por `β`.
- 🎯 **Por qué importa:** Una aproximación planificada de noche, o con el Sol detrás del objetivo, puede dejar ciego al sensor. La decisión central: ¿qué fracción de la órbita está al sol y con buena fase, según el ángulo `β`?
- 🔗 **Se estudia junto con:** fracción de eclipse, fase.

📘 **Dónde se aprende** (1 clase): [B76-C18 · Restricciones de iluminación](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md).

### Contramedida

- La contramedida es una intervención que reduce la pérdida (aquí, `δ/2`, ilustrativa).
- La contramedida es una medida para prevenir o mitigar un riesgo.

💡 **Cómo se explica en la clase [B105-C03](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md):**
- La contramedida es una suposición del modelo, no una prescripción.
- Con la mitad de `δ` (contramedida simulada) la fuerza a 180 días es 1.335,9 N.
- ⚠️ **Error frecuente:** Tomar la contramedida simulada como recomendación. Es una hipótesis del modelo (8.3).
- 🎯 **Por qué importa:** Sin carga y sin aporte adecuado, el músculo se pierde más rápido que en la Tierra. La decisión central: ¿cuánta área y cuánta fuerza quedan tras 30, 90 y 180 días, y cuánto cambia una contramedida?
- 🔗 **Se estudia junto con:** atrofia, balance proteico, tensión específica, fuerza máxima.

📘 **Dónde se aprende** (2 clases): [B105-C03 · Atrofia muscular](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md); [B113-C05 · Intervenciones de apoyo y contramedidas conductuales](../programa/clases/B113/B113-C05-intervenciones-de-apoyo-y-contramedidas-conductuales/CLASE.md).

### Contrapeso

- El contrapeso `m_c r_c = m_t r_t`.

💡 **Cómo se explica en la clase [B43-C19](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md):**
- Un tubo de 7 kg con el centro a 0,20 m y un contrapeso de 4 kg a 0,35 m dejan un desbalance de `2,2 × 10⁻¹⁶ kg m`; el contrapeso necesario es `4,000 kg`.
- Equilibrar una montura con un contrapeso.
- 🎯 **Por qué importa:** La seguridad empieza por saber cuán grande es el riesgo. La decisión central: ¿cuánta potencia y qué temperatura aparecen en el foco, cómo se balancea la montura y cuánto polvo es aceptable?
- 🔗 **Se estudia junto con:** irradiancia solar total, concentración, temperatura de equilibrio, filtro en la apertura.

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
- 🔗 **Se estudia junto con:** mancha, modulación rotacional, radio angular, periodograma.

📘 **Dónde se aprende** (8 clases): [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md); [B29-C06 · Imagen directa de exoplanetas](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md); [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md); [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md); [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md); [B53-C26 · Publicación de mapas geológicos planetarios: estándares y leyendas](../programa/clases/B53/B53-C26-publicacion-de-mapas-geologicos-planetarios-estandares-y-leyendas/CLASE.md) y 2 más.

### Contribución

- La contribución de `xᵢ` a la varianza combinada es `(cᵢ u(xᵢ))²` (S1, 5.1.2–5.1.3).
- Una contribución es el término `|c_i| u(x_i)`, en unidades del mensurando.
- La contribución de cada dimensión es `tᵢ²/Σt²`.

💡 **Cómo se explica en la clase [B12-C17](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md):**
- Con `u(v_e) = 60 m/s`, `u(m₀) = 5 kg`, `u(m_f) = 3 kg`: contribuciones `(0,51083·60)² = 939,3`, `(3·5)² = 225` y `(5·3)² = 225` m²/s².
- Si `v_e` se mide con 1 % (30 m/s) en vez de 2 %: contribuciones `234,9; 225; 225`, total `684,9`, `u = 26,17 m/s`, es decir, 29,8 % menos.
- 🎯 **Por qué importa:** Mejorar una medida cuesta dinero, masa o tiempo. Si el presupuesto de una misión ofrece mejorar la masa seca o el empuje específico, hay que saber cuál de las dos reduce más la incertidumbre del resultado.
- 🔗 **Se estudia junto con:** sensibilidad local, elasticidad, análisis global, índice de Sobol de primer orden.

📘 **Dónde se aprende** (3 clases): [B12-C17 · Análisis de sensibilidad](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md); [B13-C13 · Presupuestos de incertidumbre](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md); [B84-C16 · Tolerancias de fabricación](../programa/clases/B84/B84-C16-tolerancias-de-fabricacion/CLASE.md).

### Contribución a la varianza

- La contribución a la varianza de un factor es su `σ²` entre la suma de las `σ²` en la escala logarítmica.
- La contribución a la varianza de cada parámetro.

💡 **Cómo se explica en la clase [B33-C02](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md):**
- parametro dT/dp (h por unidad) contribucion a la varianza [h^2]
- 🎯 **Por qué importa:** Un pronóstico de llegada sin incertidumbre es engañoso. La decisión central: ¿qué parámetro domina la incertidumbre del tiempo de llegada?
- 🔗 **Se estudia junto con:** conjunto, propagación lineal, percentil.

📘 **Dónde se aprende** (2 clases): [B33-C02 · Modelos de propagación de CME](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md); [B67-C08 · Informe de disponibilidad de volátiles con incertidumbre](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md).

### Contribuyente

- Un contribuyente es una fuente de error con su `σ` (1σ).

💡 **Cómo se explica en la clase [B87-C22](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md):**
- Sin el mayor contribuyente (el alineamiento), el RSS bajaría a `6,12″`: el alineamiento aporta el 40 % de la varianza y es donde conviene invertir.
- *Descripción textual:* cada contribuyente se describe por su desviación; la suma cuadrática da el error total, el Monte Carlo la confirma y la comparación con el requisito da el margen; con dos ejes aparece el error radial.
- 🎯 **Por qué importa:** Un requisito de apuntamiento solo se cumple si el diseño lo respalda con números. La decisión central: ¿qué contribuyentes dominan, cómo se combinan (suma lineal o cuadrática), con qué margen se cumple el requisito y qué ocurre con dos ejes?
- 🔗 **Se estudia junto con:** RSS, suma lineal, término acotado uniforme, margen.

📘 **Dónde se aprende** (1 clase): [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md).

### Control

- Un control es una medida defensiva.
- Un control reduce la probabilidad de una hoja.

💡 **Cómo se explica en la clase [B119-C14](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md):**
- Cada control reduce a la mitad una hoja.
- Con los cuatro controles el riesgo baja a `0.04719` (`56.1 %` menos).
- 🎯 **Por qué importa:** La amenaza cibernética conecta el derecho con la seguridad operativa; el modelo defensivo de infraestructura espacial (B122-C03) lo desarrolla, y esta clase fija el razonamiento de riesgo. La decisión central: ¿qué control reduce más el riesgo residual y cuánto se gana al combinarlos?
- 🔗 **Se estudia junto con:** árbol de ataque, hoja, riesgo residual, defensa en profundidad.

📘 **Dónde se aprende** (2 clases): [B119-C14 · Amenazas cibernéticas a satélites](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md); [B122-C03 · Modelo defensivo de riesgos de infraestructura espacial](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md).

### Control de actitud fija

- El control de actitud fija mantiene `θ = 0`; la carga ante racha es `q·α`.

💡 **Contexto en la clase [B77-C23](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md):**
- 🎯 **Por qué importa:** Un vehículo inestable es controlable si el control es más rápido que la divergencia, pero el control a su vez fija las cargas ante rachas. La decisión central: ¿cuánto control hace falta para estabilizar un lanzador y qué ángulo de ataque deja una racha según la ganancia?
- 🔗 **Se estudia junto con:** inestabilidad aerodinámica, eficacia de control, ganancia mínima, carga ante racha.

📘 **Dónde se aprende** (1 clase): [B77-C23 · Estabilidad de vuelo de lanzadores en ascenso](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md).

### Control de calidad

- El control de calidad (QC) acepta o rechaza el lote con criterios declarados.

💡 **Cómo se explica en la clase [B14-C30](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md):**
- Cada etapa recibe un dato con su huella, calcula la clave del resultado, y si ya existe lo reutiliza; si no, lo calcula, y si falla lo reintenta; si el control de calidad lo rechaza, detiene el lote.
- I["Ingestar"] --> V["Validar<br/>control de calidad"]
- ⚠️ **Error frecuente:** Dejar pasar un lote sin control de calidad. Se corrige con la sección 8.3 y el ejercicio 7.
- 🎯 **Por qué importa:** Cada madrugada llegan datos nuevos. Si un humano debe lanzar cada paso, tarde o temprano se olvida uno; si un lote corrupto atraviesa la cadena, contamina el producto final; si un fallo de red detiene todo y al reiniciar se repite desde cero, se pierde tiempo.
- 🔗 **Se estudia junto con:** cadena, grafo acíclico dirigido (DAG), orden topológico, idempotencia.

📘 **Dónde se aprende** (1 clase): [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md).

### Control PD

- El control PD usa el error y su derivada: `δ = Kp(θ_c − θ) − Kd θ̇`.

💡 **Cómo se explica en la clase [B77-C24](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md):**
- La ganancia estática es `μ_c Kp/(μ_c Kp − μ_α) = 1,4123`: el vehículo termina a `1,412` veces el comando, porque el control proporcional debe vencer además la rigidez aerodinámica negativa.
- Un control real añade integrador o realimentación de la dirección de vuelo.
- 🎯 **Por qué importa:** El control de un lanzador inestable debe ser lo bastante rápido para estabilizarlo y lo bastante suave para no saturar la tobera. La decisión central: ¿qué ganancias cumplen una especificación dada y qué ocurre cuando la demanda supera los límites del actuador?
- 🔗 **Se estudia junto con:** frecuencia natural, razón de amortiguamiento, sobreimpulso, saturación.

📘 **Dónde se aprende** (1 clase): [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md).

### Control supervisado

- En control supervisado el operador da una meta de mayor alcance y el vehículo la ejecuta con autonomía.

💡 **Cómo se explica en la clase [B98-C03](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md):**
- Sin retardo, «mover y esperar» (pasos de 1 m, `v = 0,04 m/s`, 30 s de decisión por orden) tarda 1,53 h y el control supervisado (metas de 10 m, `v = 0,02 m/s`, 120 s por meta) 1,72 h: gana el manual.
- python programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/supervisado.py
- 🎯 **Por qué importa:** Ni siempre conviene más autonomía ni siempre más control manual: sin retardo, el manual puede ser más rápido. La decisión central: ¿a partir de qué retardo compensa pasar de órdenes cortas a metas supervisadas, y qué se pierde al hacerlo?
- 🔗 **Se estudia junto con:** tiempo de luz de una vía, mover y esperar, autonomía compartida.

📘 **Dónde se aprende** (1 clase): [B98-C03 · Control supervisado y autonomía compartida](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md).

### Controlable

- El sistema `ẋ = A x + B u` (con `n` estados) es controlable si, desde cualquier estado inicial, existe una entrada que lo lleva a cualquier otro estado en un tiempo finito.

💡 **Cómo se explica en la clase [B16-C13](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md):**
- Con `A = [[0,1],[0,0]]`, `B = [0, 1/J]ᵀ`: `AB = [1/J, 0]ᵀ`, luego `𝒞 = [[0, 1/J],[1/J, 0]]` de rango 2: controlable.
- El sistema no lineal real, con momento almacenado, puede ser controlable de otras maneras (por ejemplo, usando el acoplamiento giroscópico); la prueba lineal no lo afirma ni lo descarta.
- ⚠️ **Error frecuente:** Confundir «controlable» con «barato». Se corrige con los ejercicios 5 y 11.
- 🎯 **Por qué importa:** Un satélite puede perder actuadores o sensores en vuelo. Antes de diseñar una ley de control conviene saber si el problema tiene solución: ninguna ley, por ingeniosa que sea, mueve un estado que ningún actuador alcanza, ni estima uno que ningún sensor ve.
- 🔗 **Se estudia junto con:** observable, matriz de controlabilidad, observabilidad, prueba de Kalman.

📘 **Dónde se aprende** (1 clase): [B16-C13 · Observabilidad y controlabilidad](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md).

### Controlador

- Un controlador implementa la HAL para un dispositivo.
- Balance ambiental: suma de generaciones, retiros y acumulación de cada magnitud. Controlador: lazo que enciende o apaga un equipo.

💡 **Cómo se explica en la clase [B88-C24](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md):**
- HAL --> R["Controlador de registros (FIFO 4)"]
- El laboratorio ejecuta la misma aplicación en ambos controladores.
- 🎯 **Por qué importa:** Si la aplicación toca registros, no se puede probar sin el hardware y cada cambio de componente la rompe. La decisión central: ¿qué interfaz mínima expone el dispositivo para que la aplicación no dependa de él?
- 🔗 **Se estudia junto con:** HAL, mock, reintento, tiempo límite.

📘 **Dónde se aprende** (2 clases): [B88-C24 · Capa de abstracción de hardware (HAL) y controladores](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md); [B106-C20 · Proyecto de balance ambiental de hábitat](../programa/clases/B106/B106-C20-proyecto-de-balance-ambiental-de-habitat/CLASE.md).

### Controlador PD

- El controlador PD `τ = K_p e − K_d θ'`.

💡 **Contexto en la clase [B43-C15](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md):**
- **Idea central (modelo mental):** Como una puerta con resorte y amortiguador: más amortiguador evita el rebote, pero la hace más lenta; el control PD ajusta ese balance.
- 🎯 **Por qué importa:** El motor fija la resolución, la fuerza útil y la estabilidad del lazo. La decisión central: ¿cuánto se desvía un motor paso a paso bajo carga y qué ganancias dan una respuesta de servo sin sobreimpulso excesivo?
- 🔗 **Se estudia junto con:** paso, micropaso, par de retención, pares de polos.

📘 **Dónde se aprende** (1 clase): [B43-C15 · Motores paso a paso y servomotores](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md).

### Convección

- La convección es el transporte por movimiento macroscópico del gas.

💡 **Cómo se explica en la clase [B24-C05](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md):**
- Si `∇_rad > ∇_ad`, una burbuja desplazada hacia arriba sigue siendo más caliente que su entorno, sigue subiendo y aparece convección.
- Una opacidad alta (capas externas frías) o una luminosidad alta por unidad de masa (núcleos de estrellas masivas) empujan a la convección.
- 🎯 **Por qué importa:** La energía generada en el núcleo tarda milenios en salir y el modo de transporte decide la estructura: si el interior de una estrella es convectivo, su composición se mezcla; si es radiativo, no. De ello depende cuánto combustible alcanza el núcleo, y por tanto la vida de la estrella.
- 🔗 **Se estudia junto con:** recorrido libre medio, marcha aleatoria, tiempo de difusión, gradiente adiabático.

📘 **Dónde se aprende** (1 clase): [B24-C05 · Transporte radiativo y convectivo](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md).

### Convección natural

- La convección natural se apaga si `Ra` es menor que el valor crítico, aquí `1708`.
- La convección natural depende de la flotabilidad; en microgravedad `h_c ≈ 0` sin ventilación.

💡 **Cómo se explica en la clase [B85-C03](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md):**
- Descripción larga: la convección natural a 1 atm equivale a la radiación; con la presión a la décima parte, `Ra` cae cien veces, y con microgravedad desaparece aunque haya aire.
- Hallar la presión a la que la convección natural se apaga (`Ra = 1708`).
- 🎯 **Por qué importa:** Un equipo que se enfría bien sobre la mesa puede sobrecalentarse en vacío y en microgravedad. La decisión central: ¿cuánto del enfriamiento de un equipo se pierde al quitar la convección y qué queda para sustituirla?
- 🔗 **Se estudia junto con:** número de Rayleigh, número de Nusselt, coeficiente radiativo, camino libre medio.

📘 **Dónde se aprende** (2 clases): [B85-C03 · Convección y ausencia de convección exterior](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md); [B105-C23 · Termorregulación humana en vuelo](../programa/clases/B105/B105-C23-termorregulacion-humana-en-vuelo/CLASE.md).

### Convención

- Una convención es un acuerdo que no se deduce de la naturaleza: el umbral de 20 000 km lo es.

💡 **Cómo se explica en la clase [B07-C04](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md):**
- Se acepta cualquier umbral declarado como convención.
- 🎯 **Por qué importa:** Toda clasificación astronómica es una decisión sobre un dato: ¿esta señal supera el ruido?, ¿esta estrella es más brillante que el umbral?, ¿esta imagen está saturada? Una decisión mal escrita no falla ruidosamente: clasifica mal en silencio, justo en los casos frontera, que son los que importan.
- 🔗 **Se estudia junto con:** condición, condicional, rama, umbral.

📘 **Dónde se aprende** (1 clase): [B07-C04 · Condicionales y decisiones](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md).

### Convención de signo

- Una convención de signo es el acuerdo sobre qué sentido es positivo.

💡 **Cómo se explica en la clase [B03-C09](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md):**
- Para magnitudes que no pueden ser negativas (masa, distancia) un signo menos indica un error de datos, no una convención.
- La evidencia es el registro de signos y convenciones del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Cuando observas una llamarada solar a las 12:00:00, el evento ocurrió antes: su tiempo es el observado menos 499 s. Si sumas en vez de restar, afirmas que la llamarada ocurre en el futuro.
- 🔗 **Se estudia junto con:** número negativo, opuesto, valor absoluto, recta numérica.

📘 **Dónde se aprende** (1 clase): [B03-C09 · Operaciones con números negativos](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md).

### Convención de suma de Einstein

- La convención de suma de Einstein dice que un índice repetido en un término se suma de 1 a 3: `aᵢ bᵢ = Σ aᵢ bᵢ`.

💡 **Contexto en la clase [B10-C17](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md):**
- **Idea central (modelo mental):** Un tensor es el objeto físico; sus componentes son su «fotografía» en una base.
- 🎯 **Por qué importa:** La inercia de un satélite frente a un giro depende de la dirección: se necesita nueve números ordenados en una matriz, y esos nueve números cambian si cambias los ejes del cuerpo, pero de forma que la física no cambie.
- 🔗 **Se estudia junto con:** mudo, libre, delta de Kronecker, símbolo de Levi‑Civita.

📘 **Dónde se aprende** (1 clase): [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md).

### Convenio de signos

- El convenio de signos aquí es el de `U` positivo, con `J_n` positivo para un achatamiento ecuatorial.

💡 **Cómo se explica en la clase [B72-C02](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md):**
- Dos códigos que usen radios o convenios de signo distintos para `J2` no son comparables.
- ⚠️ **Error frecuente:** Mezclar el convenio de signos del potencial. Se corrige con la sección 10: aquí `U` es positivo.
- 🎯 **Por qué importa:** Sin un potencial no hay perturbación gravitatoria que calcular, y los números de la bibliografía (J2, J3, J4) dependen de un convenio de signos y de un radio de referencia. La decisión central: ¿qué términos del potencial incluir y con qué radio y convenio, para que J2 signifique lo mismo en tu código y en la fuente?
- 🔗 **Se estudia junto con:** armónico zonal, J2, polinomio de Legendre, gradiente.

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
- 🔗 **Se estudia junto con:** requisito, verificación, validación, matriz de verificación.

📘 **Dónde se aprende** (5 clases): [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md); [B39-C06 · Introducción a la relatividad numérica: formalismo 3+1](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md); [B73-C20 · Proyecto de integración celeste de precisión](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md); [B116-C03 · Historia clínica remota y registros médicos de misión](../programa/clases/B116/B116-C03-historia-clinica-remota-y-registros-medicos-de-mision/CLASE.md).

### Convergencia en el paso

- La convergencia en el paso es la estabilización del resultado al reducir `Δt`.

💡 **Cómo se explica en la clase [B77-C20](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md):**
- Comprobar la convergencia al reducir el paso (RK4).
- El script [simulacion.py](simulacion.py) integra el ascenso con `Cd(M)`, registra eventos, cierra el presupuesto de pérdidas y estudia la convergencia con tres pasos (comprueba residuo < 1e-6, cambios decrecientes y conservación < 1e-8).
- 🎯 **Por qué importa:** Una simulación solo vale si se sabe cuánto error numérico tiene y a dónde va cada metro por segundo. La decisión central: ¿cómo se verifica que una simulación de vuelo es numéricamente fiable y cómo se lee su presupuesto de pérdidas?
- 🔗 **Se estudia junto con:** simulación académica, presupuesto de velocidad, pérdida por dirección, evento.

📘 **Dónde se aprende** (1 clase): [B77-C20 · Simulación académica de una trayectoria de vuelo](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md).

### Convergencia espectral

- La convergencia espectral (o exponencial) es un error que decae como `e^{−c N}`.

💡 **Cómo se explica en la clase [B11-C16](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md):**
- Espectral: convergencia exponencial en dominios simples con soluciones suaves; delicado con saltos y con condiciones de borde no periódicas.
- 🎯 **Por qué importa:** Cuando la solución es suave y periódica —una señal a lo largo de una órbita, un perfil de temperatura alrededor de un vehículo que gira, el campo en una caja periódica—, un método espectral logra con 24 puntos lo que unas diferencias finitas lograrían con millones.
- 🔗 **Se estudia junto con:** transformada discreta de Fourier, transformada rápida, derivada espectral, aliasing.

📘 **Dónde se aprende** (1 clase): [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md).

### Convergencia exponencial

- La convergencia exponencial es un error `~ e^{−c N}` si la solución es analítica.

💡 **Cómo se explica en la clase [B11-C24](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md):**
- Medir la convergencia exponencial frente a diferencias finitas.
- Chebyshev agrupa nodos en los bordes y ayuda, pero la capa muy delgada exige muchos nodos o un cambio de variable; la convergencia exponencial solo aparece cuando `N` resuelve la capa.
- ⚠️ **Error frecuente:** Esperar convergencia exponencial con funciones no analíticas. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Cuando la solución es suave, un método espectral reduce un problema que necesita miles de puntos con diferencias a una docena con Chebyshev. Pero tiene un costo: el paso máximo estable de un esquema explícito baja como `1/N⁴`, y funciona mal si la solución no es suave.
- 🔗 **Se estudia junto con:** nodos de Chebyshev–Gauss–Lobatto, matriz de diferenciación, colocación, condicionamiento.

📘 **Dónde se aprende** (1 clase): [B11-C24 · Métodos espectrales avanzados (Chebyshev y Fourier)](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md).

### Conversación en tiempo real

- La conversación en tiempo real exige retardos pequeños.

💡 **Cómo se explica en la clase [B113-C03](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md):**
- Distinguir conversación en tiempo real de mensajes asincrónicos.
- 🎯 **Por qué importa:** Ninguna clase trata el efecto del retardo en el apoyo psicológico. La decisión central: ¿qué formatos de apoyo siguen siendo posibles cuando una respuesta tarda decenas de minutos?
- 🔗 **Se estudia junto con:** retardo de ida, intercambio, asincrónico, distancia Tierra–Marte.

📘 **Dónde se aprende** (1 clase): [B113-C03 · Comunicación diferida y soporte psicológico a distancia](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md).

### Conversión

- Una conversión (o *cast*) transforma un valor de un tipo a otro.
- Una conversión cambia la unidad sin cambiar la cantidad física.

💡 **Cómo se explica en la clase [B07-C02](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md):**
- Imprime cada variable con su tipo y añade al menos tres `assert` que comprueben los tipos y una conversión.
- Antes de imprimir ejecuta pruebas: tipos esperados, `0.1 + 0.2 != 0.3` y `isclose`, división real/entera/resto, conversiones de texto, `True + True == 2` y consistencia de la masa en notación científica y diámetro = 2 × radio.
- 🎯 **Por qué importa:** Un dato sin tipo es ambiguo: «12756» puede ser un número con el que calculas o un texto que lees de un archivo. Si el programa los confunde, falla o, peor, da un resultado plausible pero erróneo.
- 🔗 **Se estudia junto con:** variable, tipo, notación científica, palabra reservada.

📘 **Dónde se aprende** (2 clases): [B07-C02 · Tipos de datos y variables](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### Conversión AB

- La conversión AB es `m_AB = −2,5 log₁₀(f/3631 Jy)`.

💡 **Cómo se explica en la clase [B45-C21](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md):**
- Conversión AB: 3631,0 Jy → -0,000, 363,1 Jy → 2,500, 1,0 Jy → 8,900, 0,001 Jy → 16,400.
- 🎯 **Por qué importa:** Sin estándares la escala de un cielo concreto es arbitraria. La decisión central: ¿qué ecuación de transformación se ajusta y con qué error en la magnitud final?
- 🔗 **Se estudia junto con:** punto cero, término de color, estándar, covarianza.

📘 **Dónde se aprende** (1 clase): [B45-C21 · Estándares fotométricos y sistemas de referencia](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md).

### Conversión ida y vuelta

- La conversión ida y vuelta es la prueba `estado → elementos → estado`.

💡 **Cómo se explica en la clase [B72-C12](../programa/clases/B72/B72-C12-variaciones-de-elementos-osculadores/CLASE.md):**
- Comprobar la conversión con un error de ida y vuelta de `10⁻¹⁵`.
- 🎯 **Por qué importa:** Un catálogo publica elementos de un instante; usarlos como si fueran constantes introduce errores de kilómetros. La decisión central: ¿cuánto difiere un elemento osculador del medio y qué error de fase o de periodo produce usar el equivocado?
- 🔗 **Se estudia junto con:** elemento osculador, elemento medio, variaciones de corto periodo, semirrango.

📘 **Dónde se aprende** (1 clase): [B72-C12 · Variaciones de elementos osculadores](../programa/clases/B72/B72-C12-variaciones-de-elementos-osculadores/CLASE.md).

### Conversión superficie–frente de onda

- La conversión superficie–frente de onda es `2 cos θ` en un espejo y `(n − 1)` en una cara refractiva con aire.

💡 **Contexto en la clase [B50-C15](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md):**
- **Idea central (modelo mental):** Como un presupuesto familiar: cada gasto se suma en cuadratura en vez de aritméticamente porque son independientes, y se mira cuánto queda del límite.
- 🎯 **Por qué importa:** El requisito de un instrumento se cumple o no según cómo se reparta el error entre diseño, fabricación y alineación. La decisión central: ¿cuánto frente de onda se puede gastar en cada etapa sin superar el requisito?
- 🔗 **Se estudia junto con:** presupuesto de error de frente de onda, suma cuadrática, margen, Strehl.

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
- 🔗 **Se estudia junto con:** impulso, respuesta impulsional, lineal, invariante en el tiempo.

📘 **Dónde se aprende** (7 clases): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md); [B32-C06 · Micro y macroturbulencia y granulación estelar](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md); [B32-C11 · Ensanchamiento rotacional y v sin i](../programa/clases/B32/B32-C11-ensanchamiento-rotacional-y-v-sin-i/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md) y 1 más.

### Convolución circular

- La convolución circular es la que implícitamente calcula el producto de DFT: supone que las series se repiten.

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- El teorema de convolución (S1, §1.14, la propiedad de convolución: la transformada de `f ∗ g` es el producto de las transformadas, con la normalización de S1) tiene una versión discreta: la DFT de la convolución circular es el producto de las DFT.
- No: obtiene la convolución circular; el laboratorio da una desviación máxima de `2,75` respecto a la lineal.
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.
- 🔗 **Se estudia junto con:** impulso, respuesta impulsional, convolución, lineal.

📘 **Dónde se aprende** (1 clase): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md).

### Coordenada

- La coordenada `r` se define de modo que una circunferencia mide `2πr`.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- Entre `R☉` y `2R☉`, `s = 6,957 010 × 10⁸ m`, `1023,52 m` más que la diferencia de coordenadas `6,957 × 10⁸ m`.
- *Descripción textual:* la masa fija `r_s`; el factor `1 − r_s/r` aparece en la métrica; la distancia propia radial integra su raíz inversa y resulta mayor que la diferencia de coordenadas.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.
- 🔗 **Se estudia junto con:** métrica, distancia propia, curvatura gaussiana, exceso angular.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### Coordenadas

- Las coordenadas de `v` en la base `{b₁, …, b_n}` son los números `c_k` tales que `v = Σ c_k b_k`.

💡 **Cómo se explica en la clase [B10-C02](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md):**
- En `ℝ³` la base canónica es `{(1,0,0), (0,1,0), (0,0,1)}` y las coordenadas son las componentes habituales.
- Una base ortonormal es cómoda (coordenadas por producto escalar) y numéricamente estable.
- ⚠️ **Error frecuente:** Pensar que las coordenadas son el vector. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Un vector es una entidad geométrica; sus «componentes» dependen de los ejes que elijas. Un operador de estación terrestre describe un satélite con ejes ligados al ecuador; el satélite mismo, con ejes ligados a su órbita; un instrumento, con ejes del instrumento.
- 🔗 **Se estudia junto con:** linealmente independiente, dependiente, generador, base.

📘 **Dónde se aprende** (1 clase): [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md).

### Coordenadas cartesianas

- Las coordenadas cartesianas `(x, y)` dan la posición por las distancias a dos ejes perpendiculares.

💡 **Cómo se explica en la clase [B04-C10](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md):**
- python programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/polares_y_orbita.py
- 🎯 **Por qué importa:** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.
- 🔗 **Se estudia junto con:** coordenadas polares, polo, eje polar, anomalía verdadera.

📘 **Dónde se aprende** (1 clase): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md).

### Coordenadas esféricas

- Las coordenadas esféricas dan un punto del espacio por su distancia `r` al origen y dos ángulos.

💡 **Cómo se explica en la clase [B04-C11](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md):**
- Definir coordenadas esféricas `(r, θ, φ)` y su convención de ángulos.
- python programa/clases/B04/B04-C11-coordenadas-esfericas/direcciones_esfericas.py
- 🎯 **Por qué importa:** Un catálogo de estrellas da para cada una dos números: dónde está en el cielo. Pero un programa que cruza catálogos, calcula separaciones o apunta un telescopio no trabaja con horas y grados: trabaja con vectores.
- 🔗 **Se estudia junto con:** ángulo polar, ángulo azimutal, ascensión recta, declinación.

📘 **Dónde se aprende** (1 clase): [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md).

### Coordenadas estándar

- Las coordenadas estándar `(ξ, η)` son las del plano.

💡 **Cómo se explica en la clase [B58-C06](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md):**
- *Descripción textual:* las estrellas de referencia fijan por mínimos cuadrados las constantes que llevan los píxeles a coordenadas estándar; la proyección inversa da la ascensión recta y la declinación.
- 🎯 **Por qué importa:** Una órbita no puede ser mejor que sus posiciones: un error de décimas de segundo de arco se amplifica al propagar. La decisión central: ¿con qué exactitud puedo asignar coordenadas a un objeto en una imagen y qué la limita?
- 🔗 **Se estudia junto con:** proyección gnomónica, constantes de placa, astrometría, arrastre.

📘 **Dónde se aprende** (1 clase): [B58-C06 · Astrometría de objetos menores](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md).

### Coordenadas generalizadas

- Las coordenadas generalizadas `q = (q₁, q₂)` son los ángulos de las articulaciones, medidos desde la horizontal.

💡 **Contexto en la clase [B102-C01](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md):**
- 🎯 **Por qué importa:** Un manipulador de un rover se diseña y se ensaya en la Tierra, pero trabaja en Marte o en la Luna. La decisión central: ¿qué par necesita cada articulación en otro cuerpo, y qué cambia además del par?
- 🔗 **Se estudia junto con:** matriz de masa, Coriolis y centrífugo, par de gravedad, contacto de penalización.

📘 **Dónde se aprende** (1 clase): [B102-C01 · Dinámica multicuerpo de rovers y manipuladores](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md).

### Coordenadas ICRS

- Las coordenadas ICRS `(α, δ)` son ascensión recta y declinación respecto de esos ejes.

💡 **Contexto en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
- **Idea central (modelo mental):** Imagina fijar un mapa a las fuentes más lejanas, que casi no se mueven. Las coordenadas de cada cuásar son las marcas del mapa; los ejes salen de ellas. Cualquier dirección que midas es relativa a esas marcas; cualquier error común de las marcas es un giro de todo el mapa.
- 🎯 **Por qué importa:** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.
- 🔗 **Se estudia junto con:** Sistema Celeste de Referencia Internacional (ICRS), Marco Celeste de Referencia Internacional (ICRF), fuente definidora, cuásar.

📘 **Dónde se aprende** (1 clase): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### Coordenadas polares

- Las coordenadas polares `(r, θ)` la dan por la distancia `r` a un origen (el polo) y el ángulo `θ` medido desde un eje polar.

💡 **Cómo se explica en la clase [B04-C10](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md):**
- python programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/polares_y_orbita.py
- 🎯 **Por qué importa:** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.
- 🔗 **Se estudia junto con:** coordenadas cartesianas, polo, eje polar, anomalía verdadera.

📘 **Dónde se aprende** (1 clase): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md).

### Coordenadas (u, v, w)

- Las coordenadas `(u, v, w)` están en longitudes de onda y miran a la fuente (`w` hacia ella).

💡 **Contexto en la clase [B46-C14](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md):**
- **Idea central (modelo mental):** Como la sombra de un palo cambia con la hora, la línea de base 'vista' desde la fuente cambia con la rotación de la Tierra y traza una elipse.
- 🎯 **Por qué importa:** La línea de base fija la escala angular que se ve y el retardo que hay que compensar. La decisión central: ¿qué punto del plano `uv` y qué retardo corresponden a una línea de base y a una dirección?
- 🔗 **Se estudia junto con:** línea de base, ángulo horario, retardo geométrico, separación de franjas.

📘 **Dónde se aprende** (1 clase): [B46-C14 · Líneas de base interferométricas](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md).

### Coordinación

- La coordinación es la negociación con administraciones cuyos servicios pueden verse afectados.
- La coordinación busca evitar interferencia entre sistemas.

💡 **Cómo se explica en la clase [B119-C09](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md):**
- La UIT-R examina, coordina, inscribe y ayuda con las interferencias; los criterios numéricos quedan como «no consultados».
- N["Notificación a la UIT"] --> C["Coordinación"]
- 🎯 **Por qué importa:** Ninguna clase anterior vincula el derecho de telecomunicaciones con el cálculo de interferencia; B120 trata licencias y espectro en detalle y esta clase fija el marco.
- 🔗 **Se estudia junto con:** notificación, MIFR, interferencia perjudicial, FSPL.

📘 **Dónde se aprende** (2 clases): [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md); [B120-C01 · Licencias satelitales y procedimiento de notificación](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md).

### Copa de Faraday

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C24](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md):**
- **Idea central (modelo mental):** El analizador es una criba que deja pasar solo las partículas de una energía por carga; barriendo la criba se cuenta cuántas hay de cada energía y de ahí se deducen la velocidad media y la dispersión.
- 🎯 **Por qué importa:** La energía por carga elegida por el analizador determina qué se mide; la resolución de los canales limita la temperatura que se recupera. La decisión central: ¿cuántos canales y qué corrección dan la velocidad y la temperatura del plasma con error aceptable?
- 🔗 **Se estudia junto con:** analizador electrostático, energía por carga, distribución de velocidades, velocidad térmica.

📘 **Dónde se aprende** (1 clase): [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md).

### Copia

- Una vista es un arreglo que mira los mismos datos que otro sin copiarlos; una copia tiene datos propios.

💡 **Cómo se explica en la clase [B14-C02](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md):**
- Indexar con una lista de posiciones `est[[0, 1]]` crea una copia.
- Distinguir si una operación devuelve una vista o una copia, y por qué importa.
- ⚠️ **Error frecuente:** Confundir vista y copia. Se corrige con los ejercicios 5 y 11.
- 🎯 **Por qué importa:** Una constelación de seis satélites y cinco estaciones en tierra producen treinta distancias. Un catálogo de estrellas produce millones.
- 🔗 **Se estudia junto con:** arreglo, forma, ejes, tipo.

📘 **Dónde se aprende** (1 clase): [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md).

### COPUOS

- COPUOS es la Comisión sobre la Utilización del Espacio Ultraterrestre con Fines Pacíficos.

💡 **Cómo se explica en la clase [B119-C06](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md):**
- *Descripción textual:* la Asamblea crea COPUOS; este tiene dos subcomités y una secretaría; decide por consenso, lo que da poder de bloqueo a cada miembro.
- Según el resumen de búsqueda de las páginas de UNOOSA (2026-11-11), la Asamblea General creó COPUOS como órgano ad hoc con 18 miembros por la res. 1348 (XIII) del 13-12-1958 y lo hizo permanente por la res. 1472 (XIV) del 12-12-1959; tiene un Subcomité Científico y Técnico y un Subcomité Jurídico, y UNOOSA es su secretaría.
- ⚠️ **Error frecuente:** Atribuir la decisión a UNOOSA y no a COPUOS. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** Quien estudia el derecho espacial necesita saber dónde se negocia y cómo se decide; ninguna clase anterior trata los organismos. La decisión central: ¿cómo cambia la probabilidad de bloqueo cuando crece el número de miembros que deben consentir?
- 🔗 **Se estudia junto con:** UNOOSA, consenso, Bloqueo.

📘 **Dónde se aprende** (1 clase): [B119-C06 · Organismos UNOOSA y COPUOS](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md).

### Cordón

- El cordón es el material depositado; su ancho es `w`.

💡 **Cómo se explica en la clase [B59-C13](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md):**
- Una cúpula hemisférica de 3,0 m de radio exterior y 0,30 m de pared, con cordón de 5 cm y velocidad 0,10 m/s (todo ilustrativo).
- 🎯 **Por qué importa:** Una capa más fina da mejor forma pero más tiempo; y una cúpula tiene una zona alta que no se puede imprimir sin apoyo. La decisión central: ¿qué grosor de capa y qué perfil de cúpula hacen viable la impresión?
- 🔗 **Se estudia junto con:** altura de capa, voladizo, altura límite, catenaria invertida.

📘 **Dónde se aprende** (1 clase): [B59-C13 · Impresión 3D extraterrestre](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md).

### Cordón de seguridad

- El cordón de seguridad ata a la persona a un anclaje; limita la distancia al anclaje.

💡 **Contexto en la clase [B108-C02](../programa/clases/B108/B108-C02-planificacion-de-desplazamientos-y-rutas-de-eva/CLASE.md):**
- 🎯 **Por qué importa:** Ninguna clase planifica rutas y accesibilidad de una EVA en una estructura. La decisión central: ¿por qué asideros pasa la persona, cuánto tarda y qué restricciones (alcance, cordón) pueden dejar un puesto inaccesible?
- 🔗 **Se estudia junto con:** asidero, alcance, anclaje, Dijkstra.

📘 **Dónde se aprende** (1 clase): [B108-C02 · Planificación de desplazamientos y rutas de EVA](../programa/clases/B108/B108-C02-planificacion-de-desplazamientos-y-rutas-de-eva/CLASE.md).

### Coriolis y centrífugo

- El término de Coriolis y centrífugo `C(q, q̇) q̇` aparece al girar varias articulaciones a la vez.

💡 **Contexto en la clase [B102-C01](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md):**
- 🎯 **Por qué importa:** Un manipulador de un rover se diseña y se ensaya en la Tierra, pero trabaja en Marte o en la Luna. La decisión central: ¿qué par necesita cada articulación en otro cuerpo, y qué cambia además del par?
- 🔗 **Se estudia junto con:** coordenadas generalizadas, matriz de masa, par de gravedad, contacto de penalización.

📘 **Dónde se aprende** (1 clase): [B102-C01 · Dinámica multicuerpo de rovers y manipuladores](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md).

### Corona

- La fotosfera es la capa que emite la luz visible; la cromosfera y la corona están encima.
- Una corona es una estructura circular asociada a procesos del manto (concepto; no se calcula aquí).

💡 **Cómo se explica en la clase [B30-C02](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md):**
- Para la corona de `1,5 × 10⁶ K` el exponente en el infinito es `GMμu/(kTR) = 9,18`.
- La corona, 260 veces más caliente que la fotosfera, es un gas que se extiende tanto que su presión a gran distancia no desaparece.
- 🎯 **Por qué importa:** La corona caliente es el origen del viento solar y de gran parte de la actividad. Entender por qué no puede estar en reposo conecta el Sol con el medio interplanetario.
- 🔗 **Se estudia junto con:** altura de escala, equilibrio hidrostático isotermo, velocidad del sonido isoterma, radio sónico.

📘 **Dónde se aprende** (2 clases): [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md); [B70-C05 · Actividad volcánica venusina: llanuras, coronas e indicios de actividad reciente](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md).

### Coronógrafo

- El coronógrafo bloquea el disco solar para ver la corona.

💡 **Cómo se explica en la clase [B30-C13](../programa/clases/B30/B30-C13-eyecciones-de-masa-coronal/CLASE.md):**
- Las eyecciones de masa se observan con coronógrafos; un estudio de 909 CME de tipo *streamer-blowout* con LASCO/C2 forma parte del contexto (S3, solo resumen).
- 🎯 **Por qué importa:** Saber cuándo llegará una CME determina el margen de alerta. La decisión central: ¿cuánto tarda en llegar y cuánto depende ese tiempo del arrastre?
- 🔗 **Se estudia junto con:** viento ambiente, parámetro de arrastre, modelo de arrastre, tiempo de tránsito.

📘 **Dónde se aprende** (1 clase): [B30-C13 · Eyecciones de masa coronal](../programa/clases/B30/B30-C13-eyecciones-de-masa-coronal/CLASE.md).

### Corpus

- El corpus guarda entradas que descubren ramas nuevas.

💡 **Cómo se explica en la clase [B88-C37](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md):**
- C["Corpus de semillas"] --> M["Mutar una entrada"]
- *Descripción textual:* se muta una entrada del corpus y se ejecuta el objetivo; las excepciones se registran y las entradas que abren ramas nuevas pasan al corpus.
- 🎯 **Por qué importa:** Las pruebas diseñadas por una persona no prevén todas las combinaciones. La decisión central: ¿qué estrategia de entradas encuentra más fallos con menos ejecuciones en un banco autorizado?
- 🔗 **Se estudia junto con:** fuzzing, mutación, cobertura de ramas, hallazgo.

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
- 🔗 **Se estudia junto con:** error de medida, error sistemático, error aleatorio, sesgo.

📘 **Dónde se aprende** (6 clases): [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B74-C08 · Filtrado recursivo de estados](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md); [B81-C15 · Robustez de trayectoria ante fallas](../programa/clases/B81/B81-C15-robustez-de-trayectoria-ante-fallas/CLASE.md); [B104-C07 · Factores de liderazgo](../programa/clases/B104/B104-C07-factores-de-liderazgo/CLASE.md); [B104-C12 · Robótica tripulada](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md).

### Corrección atmosférica

- La corrección atmosférica convierte `ρ_TOA` en `ρ_s`.

💡 **Cómo se explica en la clase [B57-C26](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md):**
- La evidencia es la ficha de corrección atmosférica del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de corrección atmosférica*: la tabla de reflectancias del suelo, el TOA y la corregida, el sesgo del NDVI y el error del objeto oscuro y de un `τ` mal estimado.
- 🎯 **Por qué importa:** Comparar imágenes de fechas distintas con atmósferas distintas confunde atmósfera con cambio. La decisión central: ¿cuánto sesga la atmósfera y cómo se estima y descuenta con la información disponible?
- 🔗 **Se estudia junto con:** reflectancia de trayectoria, transmitancia total, albedo esférico, objeto oscuro.

📘 **Dónde se aprende** (1 clase): [B57-C26 · Corrección atmosférica de imágenes](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md).

### Corrección baricéntrica

- La corrección baricéntrica quita el movimiento de la Tierra.

💡 **Cómo se explica en la clase [B45-C12](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Qué es la corrección baricéntrica?
- ⚠️ **Error frecuente:** Olvidar la corrección baricéntrica. Se corrige con 8.3.
- 🎯 **Por qué importa:** Las velocidades radiales descubren planetas, binarias y la expansión del universo. La decisión central: ¿cómo se pasa de un corrimiento a una velocidad y con qué precisión?
- 🔗 **Se estudia junto con:** corrimiento, Doppler clásico, relativista, correlación cruzada.

📘 **Dónde se aprende** (1 clase): [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md).

### Corrección de Bonferroni

- La corrección de Bonferroni usa `α/k` por prueba.
- La corrección de Bonferroni divide `α` entre el número de pruebas.
- Las comparaciones múltiples inflan `α`; la corrección de Bonferroni usa `α/m`.

💡 **Cómo se explica en la clase [B14-C23](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md):**
- Aplicar la corrección de Bonferroni y explicar su coste.
- 🎯 **Por qué importa:** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.
- 🔗 **Se estudia junto con:** protocolo preregistrado, confirmatorio, exploratorio, desviación.

📘 **Dónde se aprende** (3 clases): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md); [B105-C20 · Diseño de protocolo médico simulado](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md).

### Corrección de flujo

- La corrección de flujo (*refluxing*) reemplaza el flujo grueso en una interfaz por el flujo fino.

💡 **Cómo se explica en la clase [B21-C05](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md):**
- Paso 4 · Corrección de flujo. Sea la advección con `a = 1`, `ν = 0,8` y una celda gruesa a la izquierda del parche con `u_viejo = 1,0`.
- Explicar el subciclado y la corrección de flujo en las interfaces grueso–fino.
- 🎯 **Por qué importa:** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.
- 🔗 **Se estudia junto con:** malla adaptativa, nivel, criterio de refinamiento, suavizado de malla.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Corrección de primer orden

- La corrección de primer orden por sesgo usa el jacobiano `J = ∂Δ/∂b` evaluado en el sesgo de linealización.

💡 **Contexto en la clase [B80-C09](../programa/clases/B80/B80-C09-odometria-inercial-y-preintegracion-de-imu/CLASE.md):**
- 🎯 **Por qué importa:** B87-C06 trata los giroscopios; falta la integración conjunta de acelerómetros y giroscopios para estimar el movimiento de un robot y su deriva. La decisión central: ¿cómo se reutiliza una integración inercial cuando cambian el estado inicial y los sesgos estimados?
- 🔗 **Se estudia junto con:** incrementos preintegrados, odometría inercial.

📘 **Dónde se aprende** (1 clase): [B80-C09 · Odometría inercial y preintegración de IMU](../programa/clases/B80/B80-C09-odometria-inercial-y-preintegracion-de-imu/CLASE.md).

### Corrección de sesgo

- La corrección de sesgo resta el aporte esperado del ruido.

💡 **Cómo se explica en la clase [B103-C04](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md):**
- Con el ruido ilustrativo `σ_h = 0,0005 r²` (5 cm a 10 m), el clasificador bruto deja pasar solo 27 peligros de 22 144, pero da un 99,4 % de falsas alarmas entre 10 y 15 m; con corrección de sesgo, las falsas alarmas bajan a 0,6 % pero se pierde el 72,9 % de los peligros en esa banda.
- El script [traversabilidad.py](traversabilidad.py) genera un MDE con rocas, calcula pendiente, escalón y rugosidad en ventanas, clasifica con y sin corrección de sesgo y muestra la matriz de confusión por rango (comprueba 0 errores sin ruido y el compromiso entre falsos «seguro» y falsas alarmas).
- 🎯 **Por qué importa:** El ruido del MDE crece con el cuadrado del rango y, a partir de cierta distancia, la señal de un obstáculo queda por debajo del ruido. La decisión central: ¿hasta qué rango se puede clasificar el terreno de forma útil, y qué política (conservadora o corregida) elegir más allá?
- 🔗 **Se estudia junto con:** pendiente, escalón, rugosidad, traversabilidad.

📘 **Dónde se aprende** (1 clase): [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Corrección de Van Vleck

- La corrección de Van Vleck: `ρ = sin(π ρ_q/2)` para 1 bit.

💡 **Cómo se explica en la clase [B51-C12](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md):**
- Aplicar la corrección de Van Vleck para 1 bit.
- El script [formatos_de_datos.py](formatos_de_datos.py) cuantiza, corrige, empaqueta y arma una cabecera (comprueba `η` a 0,01, la corrección de Van Vleck a tres errores estándar y la ida y vuelta exacta).
- 🎯 **Por qué importa:** La elección de bits y de formato fija cuánta sensibilidad se pierde y cuánto disco y red se necesitan. La decisión central: ¿cuántos bits por muestra, qué eficiencia se obtiene y cómo se empaqueta sin perder información?
- 🔗 **Se estudia junto con:** cuantización, eficiencia de muestreo, empaquetado, tarjeta de cabecera.

📘 **Dónde se aprende** (1 clase): [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md).

### Corrección determinista

- La corrección determinista busca `g * t ≈ error`.

💡 **Contexto en la clase [B43-C05](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md):**
- **Idea central (modelo mental):** Como una brocha: cada pasada retira una cantidad que depende de cuánto tiempo se detiene en cada zona; para igualar la pared se calcula cuánto detenerse, no se pasa al azar.
- 🎯 **Por qué importa:** Pulir es controlar un retiro de décimas de micrón: sin un modelo se oscila entre sobrecorregir y subcorregir. La decisión central: ¿cuánto hay que retirar de la mejor esfera para obtener un paraboloide y cuánto tiempo debe permanecer la herramienta en cada zona?
- 🔗 **Se estudia junto con:** ley de Preston, desviación esfera-paraboloide, mejor esfera, función de influencia.

📘 **Dónde se aprende** (1 clase): [B43-C05 · Pulido óptico](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md).

### Corrección diferencial

- La corrección diferencial ajusta `v_y0` hasta anular `vx` en el cruce.
- La corrección diferencial ajusta el estado inicial hasta que la órbita se cierre.

💡 **Cómo se explica en la clase [B76-C05](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md):**
- Aplicar la corrección diferencial de Newton sobre `x0` y `vy0`.
- 🎯 **Por qué importa:** La NRHO es la órbita de referencia publicada para la estación Gateway. La decisión central: ¿cómo se calcula una órbita periódica inestable y qué tan cerca queda un modelo simple de la referencia en un modelo de efemérides?
- 🔗 **Se estudia junto con:** NRHO, perilune, apolune, monodromia.

📘 **Dónde se aprende** (2 clases): [B73-C05 · Órbitas periódicas](../programa/clases/B73/B73-C05-orbitas-periodicas/CLASE.md); [B76-C05 · Órbitas NRHO](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md).

### Corrección norte-sur

- La corrección norte-sur es la maniobra que devuelve la inclinación a cero.

💡 **Contexto en la clase [B72-C10](../programa/clases/B72/B72-C10-perturbaciones-lunares/CLASE.md):**
- 🎯 **Por qué importa:** Un satélite geoestacionario sin maniobras de inclinación deriva de su plano ecuatorial algo menos de un grado por año, y el combustible de ese mantenimiento fija su vida útil. La decisión central: ¿cuánto contribuye cada cuerpo a la deriva de la inclinación y cuánto de ese resultado depende de simplificar la órbita lunar?
- 🔗 **Se estudia junto con:** deriva de inclinación, ciclo de 18,6 años, órbita lunar simplificada.

📘 **Dónde se aprende** (1 clase): [B72-C10 · Perturbaciones lunares](../programa/clases/B72/B72-C10-perturbaciones-lunares/CLASE.md).

### Correcto pero insuficiente

- Un requisito puede ser correcto pero insuficiente si no cubre un escenario de uso.

💡 **Contexto en la clase [B83-C17](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md):**
- 🎯 **Por qué importa:** Un proyecto puede pasar todas las pruebas de requisitos y fracasar en el uso. La decisión central: ¿además de cumplir los requisitos, el sistema satisface la necesidad en las condiciones reales de uso?
- 🔗 **Se estudia junto con:** Verificación, Validación, MTF, CNR.

📘 **Dónde se aprende** (1 clase): [B83-C17 · Verificación frente a validación](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md).

### Corrector

- `s_{k+1} = s_k + (h/2)(k₁ + k₂)` (corrector).

💡 **Cómo se explica en la clase [B11-C06](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md):**
- Aplicar a mano el método de Heun (predictor y corrector).
- Heun existe precisamente por el corrector.
- 🎯 **Por qué importa:** Una evaluación de `F` en un cálculo de trayectorias es cara cuando incluye gravedad de varios cuerpos o un modelo de atmósfera. La pregunta práctica es siempre cuánta precisión compra cada evaluación.
- 🔗 **Se estudia junto con:** método de Heun, predictor, pendiente, de dos etapas.

📘 **Dónde se aprende** (1 clase): [B11-C06 · Método de Heun](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md).

### Corrector de coma

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C20](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md):**
- El cálculo muestra que el espejo y el plano cumplen, pero que el instrumento no cubre el sensor completo sin un corrector de coma: la conclusión del diseño no es «todo cumple» sino qué hay que añadir.
- La conclusión importante: la coma en el borde del sensor es `100,57 µm`, unas `30` veces el radio de Airy: se necesita un corrector.
- 🎯 **Por qué importa:** Un diseño es un conjunto de compromisos. La decisión central: ¿qué apertura y qué focal cumplen el objetivo y qué defecto domina?
- 🔗 **Se estudia junto con:** presupuesto de diseño, Strehl de Maréchal, suma en cuadratura (RSS), aumento mínimo.

📘 **Dónde se aprende** (1 clase): [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md).

### Corredor de aerofrenado

- El corredor de aerofrenado es el rango de altitudes de periapsis útiles.

💡 **Contexto en la clase [B75-C15](../programa/clases/B75/B75-C15-aerofrenado-conceptual/CLASE.md):**
- 🎯 **Por qué importa:** Cada pasada baja el apoapsis un poco, y hace falta algún margen de seguridad con la densidad. La decisión central: ¿cuántas pasadas y cuánto tiempo hacen falta para bajar el apoapsis, y qué delta-v propulsivo se ahorra?
- 🔗 **Se estudia junto con:** aerofrenado, coeficiente balístico, densidad exponencial, potencia disipada.

📘 **Dónde se aprende** (1 clase): [B75-C15 · Aerofrenado conceptual](../programa/clases/B75/B75-C15-aerofrenado-conceptual/CLASE.md).

### Corredor de entrada

- El corredor de entrada es el intervalo de ángulos de entrada aceptables.

💡 **Cómo se explica en la clase [B77-C25](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md):**
- *Descripción textual:* para cada ángulo de entrada se simula el paso por la atmósfera; el máximo de desaceleración da el límite empinado y el apogeo de salida da el somero; su diferencia es el corredor, que la sustentación ensancha.
- La evidencia es la ficha de corredor de entrada del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** El corredor es la tolerancia que se le deja a la navegación y a la guía antes de entrar. La decisión central: ¿entre qué ángulos puede entrar el vehículo, cuánto ensancha el corredor la sustentación y cuándo falla la estimación de Allen–Eggers?
- 🔗 **Se estudia junto con:** límite empinado, límite somero, perigeo kepleriano, sustentación arriba/abajo.

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
- 🔗 **Se estudia junto con:** verosimilitud conjunta, media ponderada, χ² de consistencia, tensión por pares.

📘 **Dónde se aprende** (7 clases): [B26-C21 · Verosimilitud cosmológica con datos combinados](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md); [B33-C01 · Validación de modelos MHD con eventos solares documentados](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md); [B34-C07 · Comparación de modelos coronales con observaciones](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md); [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md); [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md) y 1 más.

### Correlación cruzada

- La correlación cruzada mide cuánto se parecen dos imágenes al desplazarlas.
- La correlación cruzada compara una curva con otra desplazada.
- La correlación cruzada compara el espectro con una plantilla desplazada.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- Correlación cruzada normalizada: más robusta al ruido, algo más lenta.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».
- 🔗 **Se estudia junto con:** registro, desplazamiento, transformación rígida, afín.

📘 **Dónde se aprende** (5 clases): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md); [B27-C20 · Análisis multibanda de un evento extremo](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md); [B34-C09 · Integración multiinstrumento de datos heliofísicos](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md); [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md); [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Correlación de fase

- La correlación de fase usa solo la fase del espectro cruzado: `R = conj(F₁) F₂ / |conj(F₁) F₂|`, y su transformada inversa tiene un pico en el desplazamiento.

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- Correlación de fase: no necesita identificar estrellas, es rápida (FFT), pero solo traslaciones (con extensiones para giros) y sufre con ruido.
- La correlación de fase hace ese deslizamiento con la FFT, de una sola vez.
- ⚠️ **Error frecuente:** Usar correlación de fase con mucho ruido. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».
- 🔗 **Se estudia junto con:** registro, desplazamiento, transformación rígida, afín.

📘 **Dónde se aprende** (1 clase): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md).

### Correlación ítem–total corregida

- La correlación ítem–total corregida correlaciona un ítem con la suma de los demás.

💡 **Cómo se explica en la clase [B105-C27](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md):**
- Correlaciones ítem–total corregidas: 0,716; 0,623; 0,649; 0,715; 0,624; 0,669; 0,594; 0,689 (ítems 1–8) y 0,283 y 0,145 (9 y 10).
- Calcular la correlación ítem–total corregida y el alfa si se elimina cada ítem.
- 🎯 **Por qué importa:** Un cuestionario con ítems que no miden lo mismo produce una puntuación poco fiable, y con pocos participantes su fiabilidad ni siquiera se puede estimar. La decisión central: ¿qué ítems sobran, cuántos ítems hacen falta y cuántos participantes se necesitan para estimar el alfa con una incertidumbre aceptable?
- 🔗 **Se estudia junto con:** alfa de Cronbach, Spearman–Brown, unidimensionalidad, validez.

📘 **Dónde se aprende** (1 clase): [B105-C27 · Instrumentos validados y psicometría en investigación](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md).

### Correlación positiva

- Independientes (S1, C.3.7) es más fuerte: la distribución de una no cambia al conocer la otra; independientes ⇒ `Cov = 0`, pero no al revés. Correlación positiva significa que tienden a subir juntas;

💡 **Contexto en la clase [B12-C05](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md):**
- **Idea central (modelo mental):** Imagina cada par `(x, y)` como un punto. Si la nube es una bola redonda, no hay relación; si se estira en diagonal, hay correlación; cuanto más delgada la elipse, más cerca de `±1`. La covarianza es la mitad «sin escala» de esa inclinación, y `r` la normaliza.
- 🎯 **Por qué importa:** En navegación espacial, la posición y la velocidad estimadas por un filtro no tienen errores independientes: un error de posición hacia delante suele ir acompañado de uno de velocidad. Ignorar esa relación da incertidumbres falsas, a veces demasiado optimistas y a veces demasiado pesimistas.
- 🔗 **Se estudia junto con:** covarianza, coeficiente de correlación, no correlacionadas, Independientes.

📘 **Dónde se aprende** (1 clase): [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md).

### Correspondencia

- Odometría visual: estimación del movimiento propio a partir de imágenes (F6). Correspondencia: par de observaciones del mismo punto en dos instantes.

💡 **Cómo se explica en la clase [B99-C01](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md):**
- Se eligen 2 correspondencias al azar (basta para fijar un movimiento 2D rígido), se ajusta `(R, t)`, se cuentan los inliers (error `< 0,10 m`) y tras 60 hipótesis se reajusta con los inliers de la mejor.
- A["Observaciones<br/>instante k y k+1"] --> B["Correspondencias<br/>mismo punto"]
- 🎯 **Por qué importa:** Una trayectoria se obtiene sumando movimientos pequeños, y cada uno trae un error; esos errores no se corrigen solos. La decisión central: ¿con qué calidad de correspondencias y de medida puedo confiar en la odometría, y cuándo necesito corregirla con cierres de bucle (C04)?
- 🔗 **Se estudia junto con:** Odometría visual, Ajuste de cuerpo rígido, RANSAC, Inlier / atípico.

📘 **Dónde se aprende** (1 clase): [B99-C01 · Odometría visual](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md).

### Correspondencia por bloques

- La correspondencia por bloques busca, para cada ventana de la imagen izquierda, la ventana de la derecha con menor coste (aquí, la suma de diferencias absolutas, SAD).

💡 **Contexto en la clase [B103-C03](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md):**
- 🎯 **Por qué importa:** La profundidad estéreo es barata y densa, pero su error crece con el cuadrado de la distancia: a 20 m una incertidumbre de 0,3 px en la disparidad son 71 cm. La decisión central: ¿hasta qué distancia se puede confiar en el mapa de profundidad para decidir si un camino es seguro, y qué línea de base lo permite?
- 🔗 **Se estudia junto con:** disparidad, línea de base, refinamiento subpixel, desviación robusta.

📘 **Dónde se aprende** (1 clase): [B103-C03 · Mapas de profundidad y correspondencia estéreo](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md).

### Corriente a la pared

- La corriente a la pared `j` es la densidad de iones que la golpean.

💡 **Cómo se explica en la clase [B78-C21](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md):**
- *Descripción textual:* la tensión fija la energía de impacto y el rendimiento; con la corriente a la pared da la velocidad de recesión; como la energía baja al retirarse la pared resulta una ecuación lineal con solución cerrada, contrastada con una integración numérica.
- 🎯 **Por qué importa:** El impulso total que un propulsor eléctrico puede entregar no lo limita el propelente sino su desgaste. La decisión central: ¿cómo depende la vida útil de la tensión de descarga y qué fracción del empuje máximo posible con el propelente alcanza a entregar?
- 🔗 **Se estudia junto con:** pulverización, rendimiento, velocidad de recesión, vida útil.

📘 **Dónde se aprende** (1 clase): [B78-C21 · Erosión y vida útil de propulsores eléctricos](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md).

### Corriente admisible

- La corriente admisible de una pista depende de su sección y del aumento de temperatura `ΔT` aceptado.

💡 **Cómo se explica en la clase [B93-C01](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md):**
- Por margen: corriente admisible menos corriente real.
- Ejercicio 5 · autónomo. Si el cobre fuera de 70 µm con el mismo ancho, ¿cómo cambia la corriente admisible?
- 🎯 **Por qué importa:** El tronco no trataba el diseño de placas: B90 integra y B86 trata potencia, pero nadie calculaba una pista. La decisión central: ¿qué ancho de cobre y qué geometría de microtira necesita una placa para llevar una corriente y una señal dadas, y qué margen queda?
- 🔗 **Se estudia junto con:** microtira, permitividad efectiva, impedancia característica, velocidad de fase.

📘 **Dónde se aprende** (1 clase): [B93-C01 · Diseño de PCB espacial (conceptual)](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md).

### Corriente anular

- La corriente anular es la corriente equivalente de un anillo de radio `a`.

💡 **Contexto en la clase [B30-C22](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md):**
- **Idea central (modelo mental):** El anillo es como un volante de inercia que almacena energía: cuanta más energía, más disminuye el campo en el centro. El dipolo es la reserva de referencia con la que se compara.
- 🎯 **Por qué importa:** El índice Dst (B30-C23) es un indicador de la energía del anillo de corriente. La decisión central: ¿qué energía y qué corriente corresponden a una disminución dada del campo?
- 🔗 **Se estudia junto con:** energía del dipolo, relación de Dessler–Parker–Sckopke, energía del anillo, índice Dst.

📘 **Dónde se aprende** (1 clase): [B30-C22 · Anillo de corriente y corrientes magnetosféricas](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md).

### Corriente de alimentación

- La corriente de alimentación es la del punto de entrada.

💡 **Cómo se explica en la clase [B49-C01](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md):**
- La resistencia de entrada es `R/sin²(kh)`, porque la corriente de alimentación es `I₀ sin(kh)`.
- A `L = λ` la corriente de alimentación es nula y la resistencia de entrada del modelo diverge.
- 🎯 **Por qué importa:** Sin la resistencia de radiación no se sabe qué carga ve la línea ni cuánta potencia se irradia. La decisión central: ¿de qué longitud hacer el hilo y qué impedancia presentará a la línea?
- 🔗 **Se estudia junto con:** dipolo, monopolo, plano de tierra, resistencia de radiación.

📘 **Dónde se aprende** (1 clase): [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md).
