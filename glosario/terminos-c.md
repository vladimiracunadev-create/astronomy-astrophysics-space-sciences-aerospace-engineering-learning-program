# Términos · C (parte 1 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · **C** · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: **1** · [2](terminos-c-2.md) · [3](terminos-c-3.md)

### CA

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

🎯 **Por qué importa (clase B43-C26):** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?

📘 **Dónde se aprende** (1 clase): [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### Cabeceo

- El cabeceo `θ` es la inclinación longitudinal (morro arriba) y el balanceo `φ` la lateral.
- La guiñada (*yaw*) gira alrededor de `z`, el cabeceo (*pitch*) alrededor de `y`, el alabeo (*roll*) alrededor de `x`.

💡 **Cómo se explica en la clase [B10-C14](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md):**
- Se puede comprobar que `R₃₁ = −sin θ = −0,5` (así sale el cabeceo).
- *Descripción textual:* con el cabeceo lejos de `±90°`, cada orientación tiene un único trío de ángulos que varía suavemente; cuando el cabeceo se acerca a `±90°`, el alabeo y la guiñada se mezclan, varias parejas dan la misma matriz y las tasas de cambio crecen sin límite.
- 🎯 **Por qué importa:** Un satélite que apunta una antena al cenit tiene el cabeceo cerca de `90°`; si la actitud se guarda con ángulos de Euler, justo ahí el cálculo se vuelve inestable: ángulos que cambian muy rápido para movimientos pequeños, o dos conjuntos de ángulos distintos para la misma orientación.

📘 **Dónde se aprende** (2 clases): [B10-C14 · Ángulos de Euler y singularidades](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md); [B102-C05 · Distribución de cargas y estabilidad ante vuelco](../programa/clases/B102/B102-C05-distribucion-de-cargas-y-estabilidad-ante-vuelco/CLASE.md).

### Cabeza fría

- La cabeza fría es la etapa de un refrigerador.

🎯 **Por qué importa (clase B49-C07):** Cada kelvin ahorrado exige vatios en la cabeza fría, y cada vatio de carga reduce el margen. La decisión central: ¿a qué temperatura enfriar y cuánta carga admite el criostato?

📘 **Dónde se aprende** (1 clase): [B49-C07 · Criogenia y refrigeración de receptores de radio](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md).

### CAC

- El CAC es el costo de conseguirlo.
- El CAC es gasto de captación entre clientes nuevos.

💡 **Cómo se explica en la clase [B125-C02](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md):**
- Con `CAC = 6 000`: `LTV/CAC = 5,83` y el CAC se recupera en `6 000/700 = 8,6` meses.
- 🎯 **Por qué importa:** El modelo de ingresos define cuándo entra el dinero y cuánto vale un cliente; ninguna clase anterior lo trata. La decisión central: ¿cuánto vale un cliente de suscripción, cuándo se reconoce su ingreso y cuánto abandono puede tolerar el negocio?

📘 **Dónde se aprende** (2 clases): [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md); [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### Caché

- La caché guarda localmente lo ya adquirido.
- Una caché guarda copias de datos recientes.
- La caché guarda recursos ya descargados.

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- La primera ejecución copia el archivo a la caché verificando que su huella coincide con la publicada; la segunda ejecución encuentra la caché, vuelve a comprobar su huella y no descarga de nuevo: dos ejecuciones, una descarga.
- La verificación se repite aunque haya caché: una caché alterada se detectaría.
- ⚠️ **Error frecuente:** Confiar en la caché sin verificar. Se corrige con el ejercicio 2.
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.

📘 **Dónde se aprende** (3 clases): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md); [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md); [B128-C10 · Acceso con baja conectividad](../programa/clases/B128/B128-C10-acceso-con-baja-conectividad/CLASE.md).

### Caché de capas

- El caché de capas reutiliza las capas cuya instrucción y entradas no cambiaron.

🎯 **Por qué importa (clase B14-C17):** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende** (1 clase): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md).

### Cadena

- Una cadena (*pipeline*) es una secuencia de etapas con dependencias.
- Una cadena es la secuencia de muestras de un algoritmo de Markov.

💡 **Cómo se explica en la clase [B14-C30](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md):**
- Así, repetir la cadena sobre los mismos datos no recalcula nada.
- Con 2 fallos inyectados en `procesar`, la cadena termina bien tras 2 reintentos (registro: 4 etapas ejecutadas, `reintento 1` y `reintento 2`).
- 🎯 **Por qué importa:** Cada madrugada llegan datos nuevos. Si un humano debe lanzar cada paso, tarde o temprano se olvida uno; si un lote corrupto atraviesa la cadena, contamina el producto final; si un fallo de red detiene todo y al reiniciar se repite desde cero, se pierde tiempo.

📘 **Dónde se aprende** (2 clases): [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md); [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md).

### Cadena contigua

- La cadena contigua es la regla de esta clase: el TRL es el mayor nivel `L` tal que los hitos 1 a `L` están todos.

💡 **Cómo se explica en la clase [B78-C19](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md):**
- El TRL es la longitud de la cadena contigua de hitos desde el 1.
- H["hitos con evidencia"] --> CAD["cadena contigua 1..L"]
- 🎯 **Por qué importa:** Una tecnología con un buen desempeño en papel puede estar lejos de volar. La decisión central: ¿en qué nivel está una tecnología según la evidencia que tiene, y qué nivel tiene un sistema formado por componentes de madureces distintas?

📘 **Dónde se aprende** (1 clase): [B78-C19 · Madurez tecnológica TRL](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md).

### Cadena de barreras

- Una cadena de barreras las pone en serie.

🎯 **Por qué importa (clase B109-C04):** Cada salida y cada regreso trae polvo a un lugar donde la tripulación respira, duerme y repara equipos. La decisión central: ¿cuántas barreras en serie hacen falta y qué arquitectura de acceso reduce más la entrada?

📘 **Dónde se aprende** (1 clase): [B109-C04 · Mitigación de polvo lunar en accesos y hábitats](../programa/clases/B109/B109-C04-mitigacion-de-polvo-lunar-en-accesos-y-habitats/CLASE.md).

### Cadena de Bateman

- La cadena de Bateman da las poblaciones sucesivas.

🎯 **Por qué importa (clase B27-C14):** La luminosidad tardía de estas supernovas sigue la semivida del cobalto-56, y por eso se usan para medir distancias. La decisión central: ¿cuántos núcleos de cada especie quedan en cada instante y qué luminosidad producen?

📘 **Dónde se aprende** (2 clases): [B27-C14 · Supernovas termonucleares](../programa/clases/B27/B27-C14-supernovas-termonucleares/CLASE.md); [B31-C08 · Decaimiento radiactivo](../programa/clases/B31/B31-C08-decaimiento-radiactivo/CLASE.md).

### Cadena de consulta

- Una cadena de consulta es el texto que se envía a la base de datos, con sus términos, campos y operadores.

🎯 **Por qué importa (clase B20-C01):** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.

📘 **Dónde se aprende** (1 clase): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md).

### Cadena de custodia

- La cadena de custodia es el registro continuo de quién tuvo la muestra, cuándo y qué hizo.
- La cadena de custodia es el registro de quién tuvo la evidencia y cuándo.

🎯 **Por qué importa (clase B63-C03):** Una muestra planetaria es irrepetible y se estudia durante décadas. La decisión central: ¿cómo demuestras, años después, qué le pasó a una muestra y cuánto de lo que mides es suyo?

📘 **Dónde se aprende** (2 clases): [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md); [B122-C09 · Preservación de evidencias y cadena de custodia de datos de incidentes](../programa/clases/B122/B122-C09-preservacion-de-evidencias-y-cadena-de-custodia-de-datos-de-incidentes/CLASE.md).

### Cadena de hashes

- La cadena de hashes `hᵢ = H(hᵢ₋₁ ‖ entradaᵢ)`.
- Bitácora: registro de operaciones. Cadena de hashes: cada entrada incluye el hash de la anterior.

💡 **Cómo se explica en la clase [B88-C40](../programa/clases/B88/B88-C40-auditoria-de-software-espacial/CLASE.md):**
- L["Registro de auditoria"] --> C["Cadena de hashes"]
- *Descripción textual:* de la población se toma una muestra, se revisa y se clasifican los hallazgos; el registro de auditoría se protege con una cadena de hashes.
- 🎯 **Por qué importa:** No se puede revisar todo; se revisa una muestra. La decisión central: ¿qué tamaño de muestra da una probabilidad aceptable de detectar desviaciones y cómo se protege el registro de lo auditado?

📘 **Dónde se aprende** (2 clases): [B88-C40 · Auditoría de software espacial](../programa/clases/B88/B88-C40-auditoria-de-software-espacial/CLASE.md); [B96-C30 · Registro y auditoría de operaciones](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md).

### Cadena de huellas

- Una cadena de huellas hace que cada entrada incluya la huella de la anterior.

🎯 **Por qué importa (clase B14-C24):** Seis meses después de un análisis, nadie recuerda por qué se excluyeron tres puntos ni cuándo se cambió el modelo. Y un revisor pregunta si la exclusión estaba prevista.

📘 **Dónde se aprende** (1 clase): [B14-C24 · Documentación de hipótesis y decisiones de análisis](../programa/clases/B14/B14-C24-documentacion-de-hipotesis-y-decisiones-de-analisis/CLASE.md).

### Cadena de Markov

- Una cadena de Markov es una secuencia de estados `X₀, X₁, …` en que el siguiente depende solo del actual: `P(Xₙ₊₁ | Xₙ, Xₙ₋₁, …) = P(Xₙ₊₁ | Xₙ)`.
- Binomial: número de éxitos en n ensayos. Cadena de Markov: estado que depende del anterior.

💡 **Cómo se explica en la clase [B48-C20](../programa/clases/B48/B48-C20-diseno-de-una-campana-observacional-profesional/CLASE.md):**
- *Descripción textual:* la binomial da la probabilidad con noches independientes y la cadena de Markov la rebaja al incluir la persistencia, con la misma fracción media de noches despejadas.
- 🎯 **Por qué importa:** Planificar con el clima medio sin considerar su persistencia da una confianza falsa. La decisión central: ¿qué ventana asegura completar la campaña con 95 % de probabilidad?

📘 **Dónde se aprende** (2 clases): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md); [B48-C20 · Diseño de una campaña observacional profesional](../programa/clases/B48/B48-C20-diseno-de-una-campana-observacional-profesional/CLASE.md).

### Cadena de resúmenes

- SHA-256: función resumen de 256 bits. Cadena de resúmenes: cada registro incorpora el resumen del anterior.

💡 **Cómo se explica en la clase [B90-C18](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md):**
- La cadena de resúmenes añade la vista de integridad.
- Descripción larga: la matriz tiene una fila vacía y una abierta; la cadena de resúmenes se rompe desde el registro editado hasta el final.
- 🎯 **Por qué importa:** Una campaña de ensayos produce informes, fotos y registros; si no se sabe qué requisito respalda cada uno o si un informe fue editado después, la verificación no vale como evidencia. La decisión central: ¿qué requisitos faltan por verificar y cómo se demuestra que la evidencia no fue alterada?

📘 **Dónde se aprende** (1 clase): [B90-C18 · Trazabilidad de evidencias](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md).

### Cadena de sobrevuelos

- Una cadena de sobrevuelos es una secuencia de ellos.

🎯 **Por qué importa (clase B75-C08):** Una misión que usa sobrevuelos de la Tierra, Venus o Júpiter no puede ir a cualquier órbita: depende del `v∞` con el que llega a cada planeta. La decisión central: ¿qué órbitas puede alcanzar una nave con un sobrevuelo de un planeta y cuánto `v∞` hace falta para llegar a una órbita dada?

📘 **Dónde se aprende** (1 clase): [B75-C08 · Secuencias múltiples de sobrevuelos](../programa/clases/B75/B75-C08-secuencias-multiples-de-sobrevuelos/CLASE.md).

### Cadena de suministro

- La cadena de suministro es la red de proveedores y subproveedores.

💡 **Cómo se explica en la clase [B122-C01](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md):**
- NIST publicó en mayo de 2022 la SP 800-161 Rev. 1 sobre gestión de riesgos de la cadena de suministro de ciberseguridad (su ficha indica que fue retirada el 2024-11-01 y sustituida por una versión actualizada); su resumen señala que los riesgos nacen del poco conocimiento de cómo se construyen y despliegan los productos adquiridos.
- 🎯 **Por qué importa:** B119-C16 solo introduce la infraestructura crítica y no analiza de quién depende. La decisión central: ¿qué proveedor, si cae, daña más servicios, y cuánto baja el riesgo si hay una segunda fuente?

📘 **Dónde se aprende** (1 clase): [B122-C01 · Dependencias de proveedores y cadena de suministro de infraestructura espacial](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md).

### Cadena de transformaciones

- Una cadena de transformaciones es una composición de matrices: `v_G = A_Gᵀ v_eq` y `v_ecl = R_x(ε) v_eq`; la cadena ecliptica→galáctica es `A_Gᵀ R_x(ε)ᵀ`.

🎯 **Por qué importa (clase B04-C19):** Un catálogo da las posiciones en ecuatoriales; un estudio de la Vía Láctea necesita galácticas; un análisis del plano del sistema solar usa eclípticas. Cambiar de sistema es rutina, y un error de signo o de matriz mueve el objeto decenas de grados.

📘 **Dónde se aprende** (1 clase): [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md).

### Cadena de valor

- Una cadena de valor ordena el dato crudo, el procesado y el análisis.

💡 **Cómo se explica en la clase [B125-C01](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md):**
- Por cadena de valor: crudo, procesado, analítico.
- 🎯 **Por qué importa:** [B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) trata los segmentos de la industria en general; ninguna clase explica por qué un dato crudo puede valer cero y aun así sostener empresas.

📘 **Dónde se aprende** (1 clase): [B125-C01 · Mercado de datos espaciales](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md).

### Cadena f

- Una cadena f (*f-string*) es un texto con `f` delante cuyas llaves `{}` insertan expresiones formateadas.

🎯 **Por qué importa (clase B07-C03):** Casi cualquier resultado científico es una expresión: una masa dividida por un volumen, un cociente de períodos. Si no sabes en qué orden Python evalúa `a / b  3`, escribirás una fórmula distinta de la que piensas y no recibirás ningún aviso: el programa funcionará y dará un número equivocado.

📘 **Dónde se aprende** (1 clase): [B07-C03 · Operadores y expresiones](../programa/clases/B07/B07-C03-operadores-y-expresiones/CLASE.md).

### Cadena protón–protón (p–p)

- La cadena protón–protón (p–p) fusiona hidrógeno a través de la unión de dos protones y reacciones posteriores.

🎯 **Por qué importa (clase B24-C07):** Dos protones se repelen con una fuerza eléctrica enorme; a las temperaturas de una estrella casi ninguno tiene energía para acercarse lo suficiente. Aun así la fusión ocurre, por efecto túnel.

📘 **Dónde se aprende** (1 clase): [B24-C07 · Ciclo CNO y cadena protón-protón](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md).

### Cadenas

- `csv.reader` devuelve cada fila como una lista de cadenas;

💡 **Cómo se explica en la clase [B07-C08](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md):**
- *Descripción textual:* el archivo de texto se abre, el `DictReader` entrega cada fila como diccionario de cadenas, se convierten los campos numéricos y se decide si la fila es válida.
- 🎯 **Por qué importa:** Un archivo CSV parece trivial y por eso engaña: todo se lee como texto, un decimal con coma rompe una columna, una línea vacía pasa inadvertida, y una codificación equivocada convierte «Júpiter» en símbolos raros. Un análisis hecho sobre datos mal leídos puede ser plausible y erróneo a la vez.

📘 **Dónde se aprende** (1 clase): [B07-C08 · Lectura de archivos CSV](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md).

### Cadencia

- La cadencia es el intervalo entre observaciones;
- La cadencia `Δt` es el intervalo entre muestras consecutivas.
- La cadencia `D_cad` es el intervalo entre visitas.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C22](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md):**
- El laboratorio lo comprueba: entre `t = 3600 s` y `7200 s`, un instrumento con cadencia de 12 s tiene `3600/12 = 300` registros, con el último en `7188 s`; el de `7200 s` no cuenta.
- Antes de ejecutar, calcula cuántos registros esperas. 24 h con cadencia de 12 s: 7200 registros por banda; la búsqueda devuelve 7200.
- 🎯 **Por qué importa:** Quieres estudiar una región activa del Sol durante un día usando imágenes ultravioleta. Hay cientos de miles de archivos repartidos en varios proveedores.

📘 **Dónde se aprende** (6 clases): [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md); [B34-C09 · Integración multiinstrumento de datos heliofísicos](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md); [B37-C13 · Series fotométricas de Kepler, TESS y PLATO para asterosismología](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md); [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Caducado

- FEFO emite el que caduca antes. Caducado es lo no emitido al vencer la vida útil del lote.

💡 **Cómo se explica en la clase [B100-C01](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md):**
- En FIFO: emitido `1449`, caducado `324`, existencia final `307`;
- Paso 3 · Diferencia. `324 − 164 = 160 u` menos de caducado;
- 🎯 **Por qué importa:** Un inventario que solo sabe «cuántas unidades hay» no puede decir de qué lote vienen, cuándo caducan ni dónde se usaron. La decisión central: ¿qué registro mínimo hace falta para emitir primero lo que caduca antes y para encontrar, si un lote resulta defectuoso, adónde fue?

📘 **Dónde se aprende** (1 clase): [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Caída de tensión

- La caída de tensión es `ΔV = I·R` a lo largo del arnés.
- La caída de tensión es `ΔV = R I`.
- Carga de potencia constante: carga cuya corriente sube cuando baja la tensión. Caída de tensión: `I R` a lo largo del arnés.

💡 **Cómo se explica en la clase [B83-C08](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md):**
- *Descripción textual:* cada interfaz se describe con parámetros; de ellos se calculan la caída de tensión y el margen de datos, y de ahí un veredicto; la caída se comprueba por una segunda formulación.
- 🎯 **Por qué importa:** La mayoría de los fallos de integración aparecen en las interfaces: un conector mal definido, una tensión fuera de rango o una tasa de datos insuficiente. La decisión central: ¿cada interfaz cumple en su caso más desfavorable, con margen, antes de construir?

📘 **Dónde se aprende** (3 clases): [B83-C08 · Interfaz entre subsistemas](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md); [B86-C07 · Distribución de potencia](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md); [B90-C07 · Integración eléctrica de buses](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md).

### Caída libre

- Una caída libre es un movimiento en que solo actúa la gravedad.

🎯 **Por qué importa (clase B05-C04):** Un satélite no tiene motor encendido y aun así gira. Una nave en el espacio vacío mantiene su velocidad sin esfuerzo.

📘 **Dónde se aprende** (1 clase): [B05-C04 · Leyes del movimiento de Newton](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md).

### Caída libre radial

- La caída libre radial parte del reposo en `r₀`.

🎯 **Por qué importa (clase B27-C08):** Para quien cae, el horizonte se cruza en un tiempo finito y, en un agujero grande, sin marea notable; para quien observa desde lejos, la caída parece no terminar. La decisión central: ¿cuánto dura la caída en cada reloj y qué marea se siente en el horizonte?

📘 **Dónde se aprende** (1 clase): [B27-C08 · Horizonte de sucesos](../programa/clases/B27/B27-C08-horizonte-de-sucesos/CLASE.md).

### Caja

- La caja es el pozo infinito.
- La caja es el dinero disponible.

💡 **Cómo se explica en la clase [B31-C04](../programa/clases/B31/B31-C04-principio-de-incertidumbre/CLASE.md):**
- El mínimo solo lo alcanza el paquete gaussiano; los estados de la caja tienen un producto mayor que crece con `n`.
- El estado fundamental de la caja da `0,567862 ħ`.
- 🎯 **Por qué importa:** La incertidumbre explica el tamaño de los átomos y la energía de punto cero. La decisión central: ¿cuánto vale el producto de incertidumbres de un estado y qué energía implica un confinamiento?

📘 **Dónde se aprende** (2 clases): [B31-C04 · Principio de incertidumbre](../programa/clases/B31/B31-C04-principio-de-incertidumbre/CLASE.md); [B125-C06 · Plan empresarial de una empresa espacial](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md).

### Caja acumulada

- La caja acumulada es su suma corrida.

💡 **Cómo se explica en la clase [B126-C03](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md):**
- La caja acumulada es positiva desde el año 5.
- 🎯 **Por qué importa:** [B124-C05](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) estima costos sin flujos de caja. La decisión central: ¿cuánto dinero hay que levantar y cuándo, y qué tan sensible es esa cifra a un retraso o a un sobrecosto?

📘 **Dónde se aprende** (1 clase): [B126-C03 · Proyección de flujos de caja de un proyecto espacial](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md).

### Caja cerrada

- La caja cerrada es una galaxia sin entrada ni salida de masa.

💡 **Cómo se explica en la clase [B25-C17](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md):**
- En la caja cerrada con `μ = 0,3` se produjeron `y s = 0,0070` de metales (por unidad de masa total); el gas retiene `Zμ = 0,0036`, el `51,6 %`, y las estrellas conservan el `48,4 %`.
- Paso 5 · Sentido. Con ese rendimiento ilustrativo, una caja cerrada que ha convertido el `70 %` de su gas en estrellas alcanza casi el valor solar; con salida de gas `λ = 1` sería la mitad.
- 🎯 **Por qué importa:** Cada generación de estrellas fabrica elementos pesados y los devuelve al gas; la proporción de metales de una galaxia cuenta cuánto se ha procesado su gas. En astronomía, «metales» son todos los elementos más pesados que el helio.

📘 **Dónde se aprende** (1 clase): [B25-C17 · Metalicidad y evolución química](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md).

### Caja envolvente

- La caja envolvente `[minX, minY, maxX, maxY]` acota la escena.

💡 **Cómo se explica en la clase [B14-C25](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md):**
- Los ítems tienen geometría, caja envolvente, propiedades (los proveedores pueden añadir campos) y activos.
- 🎯 **Por qué importa:** Un satélite produce miles de escenas al día. Para estudiar una inundación necesitas las que cubren una región, en unas fechas, con poca nube.

📘 **Dónde se aprende** (1 clase): [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md).

### Caja mínima

- La caja mínima es el punto más bajo de esa suma y fija el financiamiento necesario.

💡 **Cómo se explica en la clase [B126-C03](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md):**
- La caja mínima es `−46,75 M USD` (año 2); con un 15 % de margen, el financiamiento a levantar es `53,76 M USD`.
- Un año de retraso en los ingresos eleva la caja mínima de `46,75` a `55,75`: 9,00 M USD más de financiamiento, porque los ingresos se corren un año mientras los costos fijos y la inversión siguen su calendario.
- 🎯 **Por qué importa:** [B124-C05](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) estima costos sin flujos de caja. La decisión central: ¿cuánto dinero hay que levantar y cuándo, y qué tan sensible es esa cifra a un retraso o a un sobrecosto?

📘 **Dónde se aprende** (1 clase): [B126-C03 · Proyección de flujos de caja de un proyecto espacial](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md).

### Caja periódica

- La caja periódica elimina los bordes.
- La caja periódica identifica los bordes.

💡 **Cómo se explica en la clase [B25-C18](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md):**
- En una caja periódica, los pares esperados al azar en un contenedor entre `r₁` y `r₂` son `RR = [N(N−1)/2] × V_cont/L³`, con `V_cont = 4π(r₂³ − r₁³)/3`.
- C["Caja periódica de lado L"] --> D["RR(r) = N(N-1)/2 · V_cont / L³"]
- 🎯 **Por qué importa:** Las galaxias no se reparten al azar: forman filamentos, paredes, cúmulos y vacíos, la llamada red cósmica. La forma en que se agrupan guarda información de la materia oscura y de la historia del universo.

📘 **Dónde se aprende** (3 clases): [B25-C18 · Estructura cósmica a gran escala](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md); [B36-C03 · Funciones de correlación de galaxias](../programa/clases/B36/B36-C03-funciones-de-correlacion-de-galaxias/CLASE.md); [B36-C05 · Simulaciones cosmológicas de N cuerpos: condiciones iniciales y caja periódica](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md).

### Calcita

- Un mineral es un sólido cristalino natural de composición química definida: el olivino `(Mg,Fe)₂SiO₄` es una serie entre la forsterita `Mg₂SiO₄` y la fayalita `Fe₂SiO₄`; el piroxeno más sencillo es `MgSiO₃`; la calcita es `CaCO₃`.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Con los pesos atómicos de la NIST (C03): `H₂O = 18,0153`, `CO₂ = 44,0094`, `NH₃ = 17,0308`, forsterita `Mg₂SiO₄ = 2 × 24,3055 + 28,085 + 4 × 15,9994 = 140,6936`, fayalita `Fe₂SiO₄ = 203,7726`, piroxeno `MgSiO₃ = 100,3887` y calcita `CaCO₃ = 100,0868 g/mol`.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).

📘 **Dónde se aprende** (1 clase): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md).

### Cálculo de Jones

- La matriz de Mueller 4×4 actúa sobre Stokes; el cálculo de Jones actúa sobre el campo.

🎯 **Por qué importa (clase B45-C15):** La polarización informa de campos magnéticos, dispersión y geometría. La decisión central: ¿cómo se calcula el estado de polarización tras cada elemento?

📘 **Dónde se aprende** (1 clase): [B45-C15 · Polarización lineal y circular](../programa/clases/B45/B45-C15-polarizacion-lineal-y-circular/CLASE.md).

### Caleidoscopio

- El caleidoscopio: dos espejos en ángulo.

🎯 **Por qué importa (clase B41-C03):** Los espejos planos pliegan el haz de un telescopio y de un periscopio. La decisión central: ¿dónde está la imagen y cuánto gira el haz cuando se mueve el espejo?

📘 **Dónde se aprende** (1 clase): [B41-C03 · Reflexión y espejos planos](../programa/clases/B41/B41-C03-reflexion-y-espejos-planos/CLASE.md).

### Calendario

- Un calendario es un sistema para numerar los días a partir de ciclos astronómicos.
- Un calendario es un sistema para numerar y agrupar días.

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- Doce meses sinódicos suman `12 × 29,53 = 354,36 d`, `10,88 d` menos que el año trópico de 365,242 d (S2): un calendario de 12 meses lunares se corre unos 11 días por año respecto de las estaciones.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (2 clases): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B02-C01 · Calendarios astronómicos en civilizaciones antiguas](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md).

### Calendario circular

- Un calendario circular combina dos o más ciclos que se repiten juntos tras un número entero de vueltas; ese número es su mínimo común múltiplo (mcm).

💡 **Cómo se explica en la clase [B02-C01](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md):**
- E --> H["Combinar ciclos<br/>(mcm, calendario circular)"]
- 🎯 **Por qué importa:** Un calendario es una promesa: «dentro de tantos días ocurrirá tal cosa en el cielo o en la tierra». Esa promesa solo se cumple si el calendario sigue algún ciclo natural.

📘 **Dónde se aprende** (1 clase): [B02-C01 · Calendarios astronómicos en civilizaciones antiguas](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md).

### Calendario civil egipcio

- El calendario civil egipcio tenía 365 días: tres estaciones de cuatro meses de 30 días y cinco días adicionales al final (S3).

💡 **Cómo se explica en la clase [B02-C02](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md):**
- El calendario civil egipcio tuvo 365 días (tres estaciones de cuatro meses de 30 días, más cinco días adicionales); según Parker, su introducción se sitúa entre unos 2937 y 2821 a.
- 🎯 **Por qué importa:** Una predicción necesita una larga memoria. Para decir que un fenómeno volverá, alguien tuvo que anotarlo muchas veces y compararlo.

📘 **Dónde se aprende** (1 clase): [B02-C02 · Observación mesopotámica y egipcia](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md).

### Calendario gregoriano

- El calendario gregoriano es el calendario civil actual; un año es bisiesto si es divisible por 4, salvo los divisibles por 100 que no lo sean por 400 (así, 1900 no lo fue y 2000 sí).

💡 **Cómo se explica en la clase [B13-C09](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md):**
- A["Fecha UTC<br/>aaaa-mm-dd hh:mm:ss"] --> B["MJD entero<br/>(calendario gregoriano)"]
- 🎯 **Por qué importa:** Una nave graba un evento a las `23:59:59` del 31 de diciembre de 2016 y otro a las `00:00:00` del 1 de enero de 2017. ¿Cuánto tiempo pasó?

📘 **Dónde se aprende** (1 clase): [B13-C09 · Segundos intercalares y cronología](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md).

### Calendario lunisolar

- Un calendario lunisolar intenta seguir a la vez la Luna y el Sol.

💡 **Cómo se explica en la clase [B02-C01](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md):**
- Por eso 19 años equivalen casi exactamente a 235 meses, y un calendario lunisolar puede repartir 7 meses extra en 19 años.
- 🎯 **Por qué importa:** Un calendario es una promesa: «dentro de tantos días ocurrirá tal cosa en el cielo o en la tierra». Esa promesa solo se cumple si el calendario sigue algún ciclo natural.

📘 **Dónde se aprende** (1 clase): [B02-C01 · Calendarios astronómicos en civilizaciones antiguas](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md).

### Calentador

- El calentador cubre en el frío lo que el radiador rechaza.

💡 **Cómo se explica en la clase [B85-C20](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md):**
- Con `2 W` de supervivencia, el calentador es `113,5 W` (`141,9 W` con `25 %`).
- Un radiador descubierto cuesta mucho calentador; en la práctica se usan persianas o aislamiento para reducir esa pérdida.
- ⚠️ **Error frecuente:** Ignorar el frío. el calentador sale del frío (8.3)
- 🎯 **Por qué importa:** Un presupuesto sin margen no resiste un cambio de diseño. La decisión central: ¿qué modo gobierna el caso caliente, con cuánto margen cierra y qué calentador pide el frío?

📘 **Dónde se aprende** (1 clase): [B85-C20 · Presupuesto térmico de carga útil](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md).

### Calentador de supervivencia

- El calentador de supervivencia mantiene el mínimo de no operación.

🎯 **Por qué importa (clase B85-C08):** Un calentador pequeño no sostiene la temperatura y uno grande gasta energía que una batería no tiene. La decisión central: ¿cuánta potencia de calentador mantiene la temperatura mínima en el peor eclipse y cuánta energía cuesta por órbita?

📘 **Dónde se aprende** (1 clase): [B85-C08 · Calentadores y termostatos](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md).

### Calentador resistivo

- El calentador resistivo convierte potencia eléctrica en calor.

🎯 **Por qué importa (clase B85-C08):** Un calentador pequeño no sostiene la temperatura y uno grande gasta energía que una batería no tiene. La decisión central: ¿cuánta potencia de calentador mantiene la temperatura mínima en el peor eclipse y cuánta energía cuesta por órbita?

📘 **Dónde se aprende** (1 clase): [B85-C08 · Calentadores y termostatos](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md).

### Calentamiento

- El calentamiento (*burn-in*) son los primeros pasos, que se descartan porque aún no reflejan `π`.
- Un calentamiento (*warm-up*) son las primeras iteraciones, que se descartan.
- El calentamiento `Q(t)` es la potencia de la desintegración radiactiva depositada.

💡 **Cómo se explica en la clase [B12-C13](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md):**
- (i) Calentamiento insuficiente: la cadena que empezó en `8,41` tardó en acercarse a `3,7`; las primeras muestras no son de `π`.
- Paso 3 · Ejecución. 400 000 pasos, 5 000 de calentamiento.
- ⚠️ **Error frecuente:** Incluir el calentamiento en las estimaciones. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.

📘 **Dónde se aprende** (3 clases): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md); [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md); [B28-C18 · Interpretación de kilonovas](../programa/clases/B28/B28-C18-interpretacion-de-kilonovas/CLASE.md).

### Calentamiento coronal

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B34-C01):** Elegir un mecanismo de calentamiento exige saber cuánta energía hay que reponer y de dónde sale. La decisión central: ¿cuánta energía pierde un bucle y qué eventos pueden reponerla?

📘 **Dónde se aprende** (1 clase): [B34-C01 · Calentamiento coronal: mecanismos y evidencias](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md).

### Calentamiento Joule

- El calentamiento Joule `Σ_P E²`.

💡 **Cómo se explica en la clase [B30-C17](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md):**
- El calentamiento Joule es `12,50 mW/m²` y, sobre `10¹² m²`, `1,25 × 10¹⁰ W`.
- Con valores ilustrativos (`Σ_P = 5 S`, `Σ_H = 8 S`, `E = 50 mV/m`) el calentamiento Joule es `12,5 mW/m²`, 12,5 veces la precipitación de `1 mW/m²`.
- 🎯 **Por qué importa:** La aurora y las corrientes ionosféricas son la parte visible y eléctrica del acoplamiento entre la magnetosfera y la atmósfera. La decisión central: ¿dónde se produce la ionización y cuánta energía se disipa por efecto Joule?

📘 **Dónde se aprende** (1 clase): [B30-C17 · Auroras y corrientes ionosféricas](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md).

### Calibración

- La calibración es la operación que, bajo condiciones especificadas, establece primero una relación entre los valores de los patrones (con sus incertidumbres) y las indicaciones correspondientes (con las suyas) y luego usa esa relación para obtener un resultado de medida a partir de una indicación (S1, 2.39).
- La calibración de un intervalo es su cobertura empírica frente a su cobertura declarada.
- La calibración es el trabajo conjunto de los evaluadores con ejemplares.
- *(y 11 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C05](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md):**
- Para una indicación media `y₀` de `m` lecturas de una fuente desconocida: `x̂₀ = (y₀ − â)/b̂`, con `u(x̂₀) = (s/|b̂|) √(1/m + 1/n + (x̂₀ − x̄)²/Sxx)` (fórmula clásica de la calibración lineal inversa; no se consultó una fuente específica en esta clase).
- Se interpreta así: el primer término es el ruido de las `m` lecturas nuevas, el segundo es la incertidumbre de la recta en su centro, y el tercero crece cuando `x̂₀` se aleja del centro de calibración.
- ⚠️ **Error frecuente:** Extrapolar fuera del intervalo de calibración. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Un sensor solar de una nave devuelve cuentas digitales (DN), no vatios por metro cuadrado. Para saber cuánta luz recibe hay que haberlo expuesto antes a fuentes de irradiancia conocida y haber establecido la relación entre ambas.

📘 **Dónde se aprende** (14 clases): [B13-C05 · Calibración instrumental](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md); [B13-C20 · Validación de una cadena de medida](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md); [B28-C22 · Inferencia bayesiana conjunta de parámetros de fuente multimensajero](../programa/clases/B28/B28-C22-inferencia-bayesiana-conjunta-de-parametros-de-fuente-multimensajero/CLASE.md); [B29-C07 · Métodos de validación planetaria](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md); [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md); [B38-C09 · Validación de galaxias simuladas frente a observaciones](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md) y 8 más.

### Calibración de dos puntos

- La calibración de dos puntos determina la recta de un sensor con dos referencias.

💡 **Cómo se explica en la clase [B13-C16](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md):**
- Paso 2 · Lectura. Con `R = 110,0 Ω` (sintético): `T = 299,13 K` por la calibración de dos puntos, con `u ≈ 0,033 K`.
- 🎯 **Por qué importa:** Un sensor de temperatura pegado a un panel de una nave devuelve una resistencia. Convertirla en kelvin exige calibrarlo contra referencias conocidas, y comprobar que la temperatura medida concuerda con un balance térmico previsto.

📘 **Dónde se aprende** (1 clase): [B13-C16 · Calibración térmica](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md).

### Calibración dependiente del tiempo

- Una calibración dependiente del tiempo es una calibración cuyos parámetros se expresan como función de la fecha (S1).

🎯 **Por qué importa (clase B13-C23):** Un detector espacial lleva años en órbita. Su sensibilidad cambia lentamente por daño de radiación, contaminación y envejecimiento.

📘 **Dónde se aprende** (1 clase): [B13-C23 · Estabilidad y deriva temporal de instrumentos](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md).

### Calibración extrínseca

- La calibración extrínseca estima la pose de un sensor respecto de otro marco.

🎯 **Por qué importa (clase B103-C02):** Un error de 0,02° en la rotación entre una cámara y el brazo de un robot parece nada, pero a 10 m son 3,5 mm de error de posición, y a más distancia crece sin límite. La decisión central: ¿cuántas correspondencias y con qué geometría hacen falta para que la pose entre sensores cumpla un presupuesto de error dado?

📘 **Dónde se aprende** (1 clase): [B103-C02 · Calibración extrínseca y registro multisensor](../programa/clases/B103/B103-C02-calibracion-extrinseca-y-registro-multisensor/CLASE.md).

### Calibración nula

- La calibración nula exige que `P(p < α) = α`.

🎯 **Por qué importa (clase B28-C13):** Un valor p de `5 × 10⁻⁸` y una tasa de falsas alarmas de uno por 203 000 años no son comparables sin traducirlos a la misma escala. La decisión central: ¿cuántas sigmas equivale un valor p, cómo se corrige por las pruebas realizadas y cómo se combinan evidencias independientes?

📘 **Dónde se aprende** (1 clase): [B28-C13 · Estadística de significancia](../programa/clases/B28/B28-C13-estadistica-de-significancia/CLASE.md).

### Calibración polinómica

- La calibración polinómica es `eng = c₀ + c₁x + c₂x²`.

🎯 **Por qué importa (clase B83-C19):** Un satélite entregado con una base de datos errónea muestra valores falsos o alarmas inútiles; operadores sin entrenamiento no saben responder. La decisión central: ¿la base de datos, los comandos y las personas están listos, de modo que operaciones pueda recibir el sistema?

📘 **Dónde se aprende** (1 clase): [B83-C19 · Aceptación y transferencia a operaciones](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md).

### Calibración vicaria

- La calibración vicaria usa una superficie conocida en vez de una fuente a bordo.

🎯 **Por qué importa (clase B57-C32):** Sin calibración, una serie de décadas confunde la deriva del instrumento con cambios de la Tierra. La decisión central: ¿cuánta incertidumbre del sitio y cuántas pasadas hacen falta para detectar una deriva de décimas de porcentaje por año?

📘 **Dónde se aprende** (1 clase): [B57-C32 · Sitios de calibración terrestres](../programa/clases/B57/B57-C32-sitios-de-calibracion-terrestres/CLASE.md).

### Calibrado

- Un procedimiento está calibrado si sus probabilidades coinciden con las frecuencias: de los intervalos creíbles al 90 % que reporta, el 90 % contiene el valor verdadero.

💡 **Cómo se explica en la clase [B19-C08](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md):**
- Si el analista acierta con el prior y el ruido, el procedimiento está calibrado por construcción: es la prueba de que la maquinaria de simulación funciona.
- Un pronóstico calibrado sigue la diagonal.
- ⚠️ **Error frecuente:** Creer que calibrado significa útil. Ejercicio 11.
- 🎯 **Por qué importa:** Un intervalo del 90 % que cubre el valor verdadero solo la mitad de las veces es peor que no tener intervalo: transmite una seguridad falsa. Los diagnósticos de C04 dicen si el cómputo funcionó; los chequeos de C06 si el modelo reproduce los datos.

📘 **Dónde se aprende** (1 clase): [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md).

### Calibrador de banda

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B51-C14):** Una línea débil sobre un continuo brillante solo se ve si la banda está calibrada mejor que la razón línea/continuo. La decisión central: ¿cuánto ruido inyecta la solución de banda y por qué no basta con restar un polinomio?

📘 **Dónde se aprende** (1 clase): [B51-C14 · Calibración de banda en la reducción de datos de síntesis](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md).

### Calibrador primario

- El calibrador primario: fuente de flujo conocido a la frecuencia de observación.

🎯 **Por qué importa (clase B51-C01):** Sin una escala de flujo, dos observaciones de la misma fuente en días distintos no se pueden comparar. La decisión central: ¿cómo se fija y se propaga una escala absoluta, y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B51-C01 · Calibración de amplitud y escala de flujo con calibradores primarios](../programa/clases/B51/B51-C01-calibracion-de-amplitud-y-escala-de-flujo-con-calibradores-primarios/CLASE.md).

### Calibre

- Un calibre es un diámetro.

🎯 **Por qué importa (clase B77-C21):** Un lanzador sin margen estático positivo se voltea con la primera ráfaga; con demasiado margen es rígido y carga mucho el control. La decisión central: ¿dónde está el centro de presión, cuánto margen hay y qué lo cambia?

📘 **Dónde se aprende** (1 clase): [B77-C21 · Centro de presión y margen estático](../programa/clases/B77/B77-C21-centro-de-presion-y-margen-estatico/CLASE.md).

### Calidad

- Precisión y exhaustividad miden la detección. Calidad es la fracción de objetos sin errores.

💡 **Cómo se explica en la clase [B119-C07](../programa/clases/B119/B119-C07-registro-nacional-de-objetos/CLASE.md):**
- C --> Q["Precisión, exhaustividad, calidad"]
- *Descripción textual:* las reglas procesan los datos y producen errores; se comparan con los inyectados para medir precisión y exhaustividad y obtener la calidad.
- 🎯 **Por qué importa:** C04 estudia qué se registra y calcula el período; esta clase estudia la calidad del registro como sistema y la auditoría de coherencia, que ninguna otra clase trata. La decisión central: ¿qué reglas mínimas permiten confiar en un registro nacional y cómo se mide su calidad?

📘 **Dónde se aprende** (1 clase): [B119-C07 · Registro nacional de objetos](../programa/clases/B119/B119-C07-registro-nacional-de-objetos/CLASE.md).

### Calidad de copia

- La calidad de copia `Q = q^L` es la probabilidad de copiar bien una secuencia de `L` letras.

💡 **Cómo se explica en la clase [B56-C03](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md):**
- *Descripción textual:* se calcula la calidad de copia; si la tasa efectiva de la maestra supera a la de los mutantes, se mantiene con una fracción estacionaria; si no, desaparece.
- 🎯 **Por qué importa:** Un replicador que copia mal pierde su información; uno que copia bien necesita una maquinaria que, sin vida previa, aún no existe. Esa tensión limita el tamaño de los primeros genomas.

📘 **Dónde se aprende** (1 clase): [B56-C03 · Origen de moléculas autorreplicantes](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md).

### Calidad de fabricación

- Mano de obra (*workmanship*): calidad de fabricación. Daño acumulado: suma de fracciones de vida consumidas.

🎯 **Por qué importa (clase B90-C19):** Un ensayo de aceptación demasiado severo gasta vida útil; uno demasiado suave deja pasar defectos. La decisión central: ¿qué nivel y duración demuestran la mano de obra sin dañar la unidad, y con qué evidencia se acepta?

📘 **Dónde se aprende** (1 clase): [B90-C19 · Aceptación de unidades de vuelo](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md).

### Caliente

- La caliente `R_h = r + (1 − r)·r·c`.

💡 **Cómo se explica en la clase [B88-C32](../programa/clases/B88/B88-C32-redundancia-fria-y-caliente-estrategias-y-conmutacion/CLASE.md):**
- La fría iguala a la caliente perfecta si `c ≥ (R_h(1) − r)/(λT·r) = 0,8242`.
- La fría gana a igual cobertura en este caso (`+0,047` con `c = 1`); la caliente conviene cuando la conmutación es poco fiable o rápida es esencial (sin reinicio).
- ⚠️ **Error frecuente:** Olvidar que la caliente envejece. Incluye el factor `r` de la reserva
- 🎯 **Por qué importa:** La reserva fría gana por no envejecer, pero depende de que la conmutación funcione. La decisión central: ¿qué cobertura de conmutación hace que la fría supere a la caliente y cuándo conviene cada una?

📘 **Dónde se aprende** (1 clase): [B88-C32 · Redundancia fría y caliente: estrategias y conmutación](../programa/clases/B88/B88-C32-redundancia-fria-y-caliente-estrategias-y-conmutacion/CLASE.md).

### Calificación

- El nivel de calificación del ejemplo es el de aceptación más 3 dB.
- Una pendiente de `N` dB/oct equivale a `G ∝ f^m` con `m = N/3,01`: +6 dB/oct es `f²`, +3 dB/oct es `f`. Calificación es el ensayo a nivel superior al de vuelo;
- Calificación: demostración del diseño en niveles extremos con una unidad.

💡 **Cómo se explica en la clase [B83-C14](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md):**
- El nivel de calificación duplica la DSP (+3 dB): 10,4030 g, razón `√2 = 1,4142`.
- Las dosis `g²·s` por eje son 3247 (60 s de aceptación) y 12987 (120 s de calificación).
- ⚠️ **Error frecuente:** Confundir aceptación con calificación. La calificación demuestra el diseño; la aceptación, la unidad
- 🎯 **Por qué importa:** Un ensayo mal preparado destruye hardware o no demuestra nada. La decisión central: ¿cada requisito tiene un método asignado, y cada ensayo está listo (procedimiento, equipo, configuración, personal e instalación) y con un nivel de carga definido?

📘 **Dónde se aprende** (3 clases): [B83-C14 · Revisiones CDR y TRR](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md); [B84-C01 · Entorno mecánico de lanzamiento](../programa/clases/B84/B84-C01-entorno-mecanico-de-lanzamiento/CLASE.md); [B90-C19 · Aceptación de unidades de vuelo](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md).

### Calípico

- El ciclo metónico son 235 meses sinódicos (≈ 19 años); el calípico son cuatro metónicos menos un día; el ciclo de Saros son 223 meses sinódicos.

💡 **Cómo se explica en la clase [B132-C01](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md):**
- El calípico `4 × 6940 − 1 = 27759 d` frente a 76 años = `27758,4072 d`: diferencia `0,5928 d`.
- 🎯 **Por qué importa:** Un relato histórico es tan fiable como las fuentes que lo sostienen, y tres copias de una misma fuente no son tres fuentes. La decisión central: ¿cuánto apoyo da realmente un conjunto de fuentes a una afirmación y cuánto de ese apoyo es robusto ante cambios razonables de criterio?

📘 **Dónde se aprende** (1 clase): [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Callendar–Van Dusen

- El autocalentamiento `ΔT = P/δ` con `δ` la constante de disipación. Callendar–Van Dusen: `R = R₀(1 + A T + B T²)` para `T > 0 °C`.

🎯 **Por qué importa (clase B85-C25):** Una temperatura mal medida lleva a una decisión errónea de control o de margen. La decisión central: ¿qué error total tiene la cadena de medida a una temperatura dada y qué término lo domina?

📘 **Dónde se aprende** (1 clase): [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md).

### Calor

- El calor `Q` es energía transferida por una diferencia de temperatura (J).

💡 **Cómo se explica en la clase [B05-C13](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md):**
- Si un cuerpo recibe un calor `Q` sin cambiar de fase, `Q = m c ΔT`.
- La Tierra tiene una temperatura media de 288 K (S2): la diferencia (unos 10 K) se debe a que la Tierra no es un cuerpo negro (refleja parte de la luz) y a su atmósfera (que retiene calor).
- ⚠️ **Error frecuente:** Confundir calor con temperatura. Ejercicios 2 y 3.
- 🎯 **Por qué importa:** Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: ¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?

📘 **Dónde se aprende** (1 clase): [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md).

### Calor de combustión

- Calor de combustión: energía por kg quemado.

🎯 **Por qué importa (clase B106-C17):** Un incendio en una cabina cerrada no puede salir al exterior: calienta, sube la presión, consume oxígeno y produce CO₂ y humo. La decisión central: ¿qué efectos tiene una cantidad dada de combustible y con qué tiempo y ventilación se puede detectar?

📘 **Dónde se aprende** (1 clase): [B106-C17 · Prevención y respuesta a incendios](../programa/clases/B106/B106-C17-prevencion-y-respuesta-a-incendios/CLASE.md).

### Calor de reacción

- El calor de reacción debe evacuarse del reactor.

🎯 **Por qué importa (clase B59-C09):** Un combustible fabricado en destino depende de qué parte del hidrógeno se recicla. La decisión central: ¿cuánto hidrógeno hay que importar para fabricar 1 000 kg de propelente O₂/CH₄?

📘 **Dónde se aprende** (1 clase): [B59-C09 · Fabricación de combustibles conceptuales](../programa/clases/B59/B59-C09-fabricacion-de-combustibles-conceptuales/CLASE.md).

### Calor interno

- El calor interno es el flujo que sale del interior.

💡 **Cómo se explica en la clase [B54-C15](../programa/clases/B54/B54-C15-atmosferas-de-gigantes-gaseosos/CLASE.md):**
- Una olla caliente desde abajo mueve el líquido en corrientes; en Júpiter, el calor interno hace lo mismo con el gas.
- 🎯 **Por qué importa:** La atmósfera de Júpiter es una capa convectiva muy profunda. La pregunta motivadora: ¿cuánto más caliente es el nivel de 1 bar que el equilibrio solar y cómo crece la temperatura hacia dentro?

📘 **Dónde se aprende** (1 clase): [B54-C15 · Atmósferas de gigantes gaseosos](../programa/clases/B54/B54-C15-atmosferas-de-gigantes-gaseosos/CLASE.md).

### Calor latente

- El calor sensible eleva la temperatura; el calor latente cambia de fase.

💡 **Cómo se explica en la clase [B97-C15](../programa/clases/B97/B97-C15-impresion-3d-espacial/CLASE.md):**
- El calor latente por la fracción fundida aporta `0,074` del total; la energía específica es `1217280` J/kg (`0,338` kWh/kg).
- F["fraccion fundida, L"] --> LAT["calor latente"]
- 🎯 **Por qué importa:** La impresión 3D parece barata en masa (se usa material local), pero cuesta energía y tiempo. Sin un presupuesto, no se sabe si la fuente de energía alcanza ni cuántas horas se necesitan para un muro.

📘 **Dónde se aprende** (2 clases): [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md); [B97-C15 · Impresión 3D espacial](../programa/clases/B97/B97-C15-impresion-3d-espacial/CLASE.md).

### Calor latente de vaporización

- El calor latente de vaporización `L` es la energía por kilogramo para evaporar.

🎯 **Por qué importa (clase B56-C06):** «Sigue el agua» es una consigna de la exploración, pero tener hielo o vapor no es tener un líquido. La presión y la temperatura mandan.

📘 **Dónde se aprende** (1 clase): [B56-C06 · Agua líquida y solventes alternativos](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md).

### Calor residual

- El calor residual es energía reemitida en el infrarrojo.

💡 **Cómo se explica en la clase [B56-C16](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md):**
- Búsquedas en infrarrojo (calor residual): otro tipo de tecnofirma.
- (2014) describe una búsqueda de civilizaciones con grandes suministros de energía por su calor residual en el infrarrojo medio con datos de WISE y Spitzer; identifica el polvo como principal fuente de falsos positivos y un primer resultado nulo para civilizaciones de tipo III de Kardashev (S1, solo resumen, consultado el 2026-11-09).
- 🎯 **Por qué importa:** Buscar tecnología exige saber qué flujo mínimo detecta un receptor y qué potencia debería tener un transmisor a una distancia dada. La decisión central: dados la temperatura del sistema, el área efectiva, el ancho de banda y el tiempo de integración, ¿qué flujo mínimo se detecta y hasta qué distancia llega un transmisor dado?

📘 **Dónde se aprende** (1 clase): [B56-C16 · Tecnofirmas y búsqueda SETI](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md).

### Calor seco

- Reducción logarítmica: `log₁₀(N₀/N)`. Calor seco: método térmico sin humedad.

💡 **Cómo se explica en la clase [B90-C22](../programa/clases/B90/B90-C22-validacion-de-procesos-de-reduccion-de-biocarga/CLASE.md):**
- La página de protección planetaria de NASA (F5) menciona que, según lo que el hardware tolere, se usan reducción microbiana por calor seco, peróxido de hidrógeno en vapor y exposición a luz ultravioleta, que las superficies expuestas se limpian con alcohol y que, si la biocarga excede el límite, se vuelve a limpiar y a medir.
- 🎯 **Por qué importa:** Cada hora de calor consume vida del hardware; poca exposición deja sobrevivientes. La decisión central: ¿cuánta exposición garantiza la reducción pedida con una probabilidad de sobreviviente aceptable, y cómo cambia con la temperatura?

📘 **Dónde se aprende** (1 clase): [B90-C22 · Validación de procesos de reducción de biocarga](../programa/clases/B90/B90-C22-validacion-de-procesos-de-reduccion-de-biocarga/CLASE.md).

### Calor sensible

- El calor sensible es el de cambiar la temperatura.
- El calor sensible eleva la temperatura; el calor latente cambia de fase.

💡 **Cómo se explica en la clase [B97-C15](../programa/clases/B97/B97-C15-impresion-3d-espacial/CLASE.md):**
- Con `cp(T) = 840 (1 + 0,0004 (T − 300))`, el calor sensible entre `300 K` y `1400 K` es `1127280` J/kg.
- C["cp(T), T0, T1"] --> S["calor sensible"]
- 🎯 **Por qué importa:** La impresión 3D parece barata en masa (se usa material local), pero cuesta energía y tiempo. Sin un presupuesto, no se sabe si la fuente de energía alcanza ni cuántas horas se necesitan para un muro.

📘 **Dónde se aprende** (2 clases): [B59-C06 · Extracción y procesamiento de volátiles](../programa/clases/B59/B59-C06-extraccion-y-procesamiento-de-volatiles/CLASE.md); [B97-C15 · Impresión 3D espacial](../programa/clases/B97/B97-C15-impresion-3d-espacial/CLASE.md).

### Calorímetro

- Un calorímetro mide la energía.

💡 **Cómo se explica en la clase [B31-C14](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md):**
- *Descripción textual:* el índice fija el umbral, el ángulo y el rendimiento; los parámetros del calorímetro fijan la resolución, que se comprueba con Monte Carlo.
- 🎯 **Por qué importa:** Interpretar una señal exige saber qué partículas la producen y con qué precisión se mide su energía. La decisión central: ¿qué umbral y qué resolución tiene un detector?

📘 **Dónde se aprende** (1 clase): [B31-C14 · Detectores de partículas](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md).

### Cámara análoga

- Una cámara análoga reproduce algunas condiciones (gases, presión, temperatura) de un ambiente.

🎯 **Por qué importa (clase B64-C07):** Un análogo no es el otro mundo: reproduce algunas variables y deja otras. La pregunta motivadora: ¿qué parte del ambiente real estás imitando, qué parte no y qué puedes concluir de un cultivo en la cámara?

📘 **Dónde se aprende** (1 clase): [B64-C07 · Cultivo de extremófilos no patógenos en condiciones análogas](../programa/clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md).

### Cambio absoluto

- El cambio absoluto es `final − inicial`.

💡 **Cómo se explica en la clase [B03-C03](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md):**
- A["Valor inicial (base)"] --> C["Cambio absoluto = final − inicial"]
- *Descripción textual:* dos valores (inicial y final) generan el cambio absoluto; este se divide entre la base, se multiplica por 100 y el resultado se acompaña de la base que se usó.
- 🎯 **Por qué importa:** La Tierra no gira en un círculo: su distancia al Sol varía a lo largo del año. ¿Mucho o poco?

📘 **Dónde se aprende** (1 clase): [B03-C03 · Porcentajes y escalas comparativas](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md).

### Cambio de concepto

- El cambio de covariables altera la distribución de las entradas `x`; el cambio de prevalencia (o de etiquetas), la proporción de cada clase; el cambio de concepto, la relación entre `x` y la clase.

🎯 **Por qué importa (clase B17-C07):** Un modelo se entrena con un catálogo y se despliega sobre otro: otro telescopio, otra época, otro brillo límite. Su exactitud medida en validación cruzada deja de valer, y el modelo no avisa: responde con la misma seguridad.

📘 **Dónde se aprende** (1 clase): [B17-C07 · Validación fuera de distribución](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md).

### Cambio de contexto

- Un cambio de contexto cuesta tiempo real; aquí solo se cuentan.

🎯 **Por qué importa (clase B88-C06):** Elegir la política determina cuánta CPU se puede usar con garantías. La decisión central: ¿RM basta, o se necesita EDF para el conjunto de tareas?

📘 **Dónde se aprende** (1 clase): [B88-C06 · Planificación de tareas RTOS](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md).

### Cambio de coordenadas

- Un cambio de coordenadas es una función invertible entre sistemas.

🎯 **Por qué importa (clase B10-C19):** Una estación mide la distancia, el azimut y la elevación de un objeto con incertidumbres. Para decir dónde está en coordenadas cartesianas y cuánta incertidumbre tiene esa posición, hay que transformar los números y sus errores.

📘 **Dónde se aprende** (1 clase): [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md).

### Cambio de covariables

- El cambio de covariables altera la distribución de las entradas `x`; el cambio de prevalencia (o de etiquetas), la proporción de cada clase; el cambio de concepto, la relación entre `x` y la clase.

🎯 **Por qué importa (clase B17-C07):** Un modelo se entrena con un catálogo y se despliega sobre otro: otro telescopio, otra época, otro brillo límite. Su exactitud medida en validación cruzada deja de valer, y el modelo no avisa: responde con la misma seguridad.

📘 **Dónde se aprende** (1 clase): [B17-C07 · Validación fuera de distribución](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md).

### Cambio de dominio

- El cambio de dominio es una diferencia entre las condiciones de entrenamiento y de uso.

💡 **Cómo se explica en la clase [B103-C05](../programa/clases/B103/B103-C05-segmentacion-semantica-de-superficies-planetarias/CLASE.md):**
- Límite: aquí el clasificador solo ve una vecindad pequeña; un modelo convolucional profundo usa más contexto, pero comparte el riesgo de cambio de dominio.
- 🎯 **Por qué importa:** Un modelo que acierta el 91 % de los píxeles en el dominio de entrenamiento puede acertar el 45 % cuando cambia la luz. La decisión central: ¿qué métrica y qué prueba demuestran que un segmentador es utilizable en otras condiciones, y no solo en las de entrenamiento?

📘 **Dónde se aprende** (1 clase): [B103-C05 · Segmentación semántica de superficies planetarias](../programa/clases/B103/B103-C05-segmentacion-semantica-de-superficies-planetarias/CLASE.md).

### Cambio de fase

- Un cambio de fase (fusión, vaporización, sublimación…) ocurre cuando `kT` se acerca a una fracción de `ε`.

💡 **Cómo se explica en la clase [B06-C10](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md):**
- ⚠️ **Error frecuente:** Esperar que el cambio de fase ocurra cuando `kT = ε`. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** En Marte, la temperatura media es 214 K y la presión media en superficie 6,36 mb (S1). Ese valor está casi en el punto triple del agua, la presión mínima a la que puede existir agua líquida (S2).

📘 **Dónde se aprende** (1 clase): [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md).

### Cambio de plano puro

- Un cambio de plano puro gira el vector velocidad sin cambiar su módulo.
- El cambio de plano puro gira la dirección de la velocidad sin cambiar su módulo: `Δv = 2 v sin(i/2)`.

💡 **Cómo se explica en la clase [B71-C19](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md):**
- Un cambio de plano puro de 28,5° (ilustrativo) cuesta `3775.3 m/s` a 400 km de altitud y solo `1513.7 m/s` en GEO.
- 🎯 **Por qué importa:** Un cambio de plano mal ubicado puede costar más que todo el resto de la misión orbital. La decisión central: ¿dónde y cómo conviene cambiar el plano para gastar el mínimo `Δv`?

📘 **Dónde se aprende** (2 clases): [B71-C19 · Cambios de plano simples](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md); [B75-C13 · Cambios de plano interplanetarios](../programa/clases/B75/B75-C13-cambios-de-plano-interplanetarios/CLASE.md).

### Cambio de prevalencia

- El cambio de covariables altera la distribución de las entradas `x`; el cambio de prevalencia (o de etiquetas), la proporción de cada clase; el cambio de concepto, la relación entre `x` y la clase.

🎯 **Por qué importa (clase B17-C07):** Un modelo se entrena con un catálogo y se despliega sobre otro: otro telescopio, otra época, otro brillo límite. Su exactitud medida en validación cruzada deja de valer, y el modelo no avisa: responde con la misma seguridad.

📘 **Dónde se aprende** (1 clase): [B17-C07 · Validación fuera de distribución](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md).

### Cambio de velocidad ideal

- El cambio de velocidad ideal es `Δv = V_eq·ln(MR)`.

🎯 **Por qué importa (clase B77-C05):** El propelente es casi toda la masa de un lanzador porque la velocidad crece solo con el logaritmo de la razón de masas. La decisión central: ¿qué razón de masas y qué `Isp` hacen falta para un `ΔV` dado, y qué parte se pierde por gravedad?

📘 **Dónde se aprende** (1 clase): [B77-C05 · Ecuación de cohete ideal](../programa/clases/B77/B77-C05-ecuacion-de-cohete-ideal/CLASE.md).

### Cambio de velocidad ΔV

- Pulso semisenoidal: medio ciclo de seno de amplitud `A` y duración `T`. Cambio de velocidad `ΔV`: integral de la aceleración.

🎯 **Por qué importa (clase B90-C10):** Dos pulsos con distinta forma pueden dañar lo mismo si sus SRS coinciden, y un pulso con gran aceleración pico puede ser inofensivo para un equipo de baja frecuencia. La decisión central: ¿qué frecuencias de mi equipo están amenazadas por este choque y con qué nivel?

📘 **Dónde se aprende** (1 clase): [B90-C10 · Ensayos de choque](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md).

### Cambio inocuo

- Un cambio inocuo es uno que no altera el resultado más allá del redondeo.

💡 **Cómo se explica en la clase [B14-C10](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md):**
- (Una reescritura algebraica del período, `2π·a^{3/2}/√GM` frente a `2π√(a³/GM)`, dio resultados idénticos bit a bit en esta máquina: un cambio inocuo puede no cambiar ni un bit, y otro, en otra plataforma, sí.)
- Cambio inocuo. Reescribe la fórmula de `T`: diferencia 0; pasa con `rtol = 10⁻⁹`.
- 🎯 **Por qué importa:** Cambias una línea de un propagador orbital «solo para ordenarlo» y el período de una órbita pasa de 5553,624562 s a 5553,627342 s (situación ilustrativa con cifras de esta clase). ¿Es un error o ruido?

📘 **Dónde se aprende** (1 clase): [B14-C10 · Pruebas de regresión numérica](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md).

### Cambio mínimo detectable

- El cambio mínimo detectable `MDC95` es la diferencia más pequeña que supera el error al 95 %.

💡 **Cómo se explica en la clase [B107-C04](../programa/clases/B107/B107-C04-evaluacion-del-rendimiento-fisico-y-cognitivo-de-tripulantes/CLASE.md):**
- *Descripción textual:* la fiabilidad da el error típico, de él sale la dispersión de una diferencia, y con ella el índice de cambio, el cambio mínimo detectable y las tasas de error.
- La desviación de la diferencia es `8,05` y el cambio mínimo detectable `MDC95 = 15,79` puntos.
- 🎯 **Por qué importa:** Los fragmentos consultados describen una batería computarizada de pruebas breves de varios dominios cognitivos diseñada para astronautas de alto rendimiento (Basner et al., 2015; Casario et al., 2022) y preguntan cómo se relacionan sus descensos con el desempeño operativo (Basner et al., 2020).

📘 **Dónde se aprende** (1 clase): [B107-C04 · Evaluación del rendimiento físico y cognitivo de tripulantes](../programa/clases/B107/B107-C04-evaluacion-del-rendimiento-fisico-y-cognitivo-de-tripulantes/CLASE.md).

### Cambio porcentual

- El cambio relativo es el cambio absoluto dividido entre la base: `(final − inicial) / inicial`; expresado en porcentaje es el cambio porcentual.

💡 **Cómo se explica en la clase [B03-C03](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md):**
- Si el valor pasa de `x₀` a `x₁`, el cambio porcentual respecto de `x₀` es `(x₁ − x₀)/x₀ × 100`.
- 🎯 **Por qué importa:** La Tierra no gira en un círculo: su distancia al Sol varía a lo largo del año. ¿Mucho o poco?

📘 **Dónde se aprende** (1 clase): [B03-C03 · Porcentajes y escalas comparativas](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md).

### Cambio relativo

- El cambio relativo es el cambio absoluto dividido entre la base: `(final − inicial) / inicial`; expresado en porcentaje es el cambio porcentual.

🎯 **Por qué importa (clase B03-C03):** La Tierra no gira en un círculo: su distancia al Sol varía a lo largo del año. ¿Mucho o poco?

📘 **Dónde se aprende** (1 clase): [B03-C03 · Porcentajes y escalas comparativas](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md).

### Cambios de aire por hora

- HEPA: filtro de alta eficiencia. Cambios de aire por hora: `3600 Q/V`.

💡 **Cómo se explica en la clase [B106-C23](../programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/CLASE.md):**
- Un filtro de 99,97 % con 0,6 m³/s en 100 m³ da `k = 0,00600 s⁻¹` y reduce la concentración al 1 % en 12,8 min (21,6 cambios de aire por hora); en 1 g la sedimentación añade y baja el tiempo a 9,3 min; con filtro de 90 %, 14,2 min.
- 🎯 **Por qué importa:** En 1 g las partículas grandes caen al suelo; en microgravedad no, y en gravedad parcial caen más despacio. La decisión central: ¿qué eficiencia de filtro y qué caudal limpian la cabina en un tiempo dado según la gravedad y el tamaño?

📘 **Dónde se aprende** (1 clase): [B106-C23 · Control de partículas y polvo respirable en cabina](../programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/CLASE.md).

### Caminata del conjunto de excursión

- La caminata del conjunto de excursión sigue `δ(S)` con `S = σ²`.

🎯 **Por qué importa (clase B36-C06):** Contar halos exige un umbral de colapso y una función de masa. La decisión central: ¿cuánta masa del universo está en halos de más de cierta masa?

📘 **Dónde se aprende** (1 clase): [B36-C06 · Formación de halos y función de masa](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md).

### Camino crítico

- El camino crítico es la suma de las etapas que no se pueden solapar.
- El camino crítico es la cadena más larga de dependencias.
- Secuencia: lista ordenada de actividades. Camino crítico: cadena de holgura cero.

💡 **Cómo se explica en la clase [B96-C09](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md):**
- El método de camino crítico es estándar y se verifica en el laboratorio; las actividades son sintéticas.
- Una enumeración de todos los caminos del grafo da 255 s como el más largo, con las mismas actividades que el camino crítico.
- 🎯 **Por qué importa:** Una secuencia que no cabe en la ventana deja comandos sin ejecutar o telemetría sin confirmar. La decisión central: ¿qué actividades fijan la duración mínima y cuánta holgura queda?

📘 **Dónde se aprende** (3 clases): [B96-C09 · Secuencias de misión](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md); [B121-C05 · Cumplimiento regulatorio en varias jurisdicciones](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md); [B131-C04 · Secuenciación conceptual de una unidad](../programa/clases/B131/B131-C04-secuenciacion-conceptual-de-una-unidad/CLASE.md).

### Camino libre medio

- El camino libre medio es `λ = k_B T/(√2 π d² P)`.
- El camino libre medio `λ = v_t/ν`.

💡 **Cómo se explica en la clase [B35-C04](../programa/clases/B35/B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md):**
- Para el viento solar a 1 au (`n = 5 cm⁻³`, `T = 10⁵ K`) el camino libre medio de Coulomb es `8,3×10¹⁰ m` (`Kn = 0,55` frente a 1 au), mientras que en la ionosfera F es `83 m`.
- 🎯 **Por qué importa:** Saber si un plasma es colisional decide qué modelo usar. La decisión central: ¿es el camino libre medio mayor o menor que la escala del problema?

📘 **Dónde se aprende** (5 clases): [B35-C04 · Colisiones, régimen cinético y ecuación de Vlasov](../programa/clases/B35/B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md); [B47-C12 · Óptica en ambientes de vacío](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md); [B84-C06 · Comportamiento bajo vacío](../programa/clases/B84/B84-C06-comportamiento-bajo-vacio/CLASE.md); [B85-C03 · Convección y ausencia de convección exterior](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md); [B85-C12 · Entorno de vacío](../programa/clases/B85/B85-C12-entorno-de-vacio/CLASE.md).

### Camino más largo

- El camino más largo maximiza ciclos con cotas de bucle.

🎯 **Por qué importa (clase B88-C30):** El análisis de planificación (C05) necesita `C` de cada tarea, y medir no basta porque el peor camino puede no ejercitarse. La decisión central: ¿cuál es una cota segura del tiempo de ejecución y cuánto pesimismo trae?

📘 **Dónde se aprende** (1 clase): [B88-C30 · Análisis de peor caso de tiempo de ejecución (WCET)](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md).

### Camino mínimo

- El camino mínimo es el de menor longitud total.

🎯 **Por qué importa (clase B114-C01):** Una salida existe en el plano, pero la evacuación depende de cuánto se tarda en llegar a ella y de qué pasa si el camino principal queda bloqueado. La decisión central: ¿cuánto tarda en salir toda la tripulación y qué ruta queda si falla la principal?

📘 **Dónde se aprende** (1 clase): [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md).

### Camino óptico

- El camino óptico `Σ nᵢdᵢ`.

💡 **Cómo se explica en la clase [B41-C01](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md):**
- Paso 1 · Camino óptico. `1,517 × 10 + 1,333 × 50 + 1,0003 × 200 = 15,17 + 66,65 + 200,06 = 281,88 mm`.
- ⚠️ **Error frecuente:** Olvidar multiplicar por `n` en el camino óptico. Se corrige con 8.2.
- 🎯 **Por qué importa:** Sin un modelo de rayos no se puede diseñar un telescopio. La decisión central: ¿cuándo basta con rayos y cuánto tarda la luz en cada medio?

📘 **Dónde se aprende** (1 clase): [B41-C01 · Naturaleza y propagación de la luz](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md).

### Campaña

- La campaña es el conjunto de inyecciones con su criterio de resultado.
- Campaña: conjunto de observaciones con un objetivo.

💡 **Cómo se explica en la clase [B48-C20](../programa/clases/B48/B48-C20-diseno-de-una-campana-observacional-profesional/CLASE.md):**
- Una campaña planificada con el modelo independiente promete 96 % y entrega 86 %.
- El clima viene en rachas: un día nublado suele seguirse de otro, y esas rachas hacen más probable terminar mal una campaña que lo que predice el promedio.
- 🎯 **Por qué importa:** Planificar con el clima medio sin considerar su persistencia da una confianza falsa. La decisión central: ¿qué ventana asegura completar la campaña con 95 % de probabilidad?

📘 **Dónde se aprende** (2 clases): [B48-C20 · Diseño de una campaña observacional profesional](../programa/clases/B48/B48-C20-diseno-de-una-campana-observacional-profesional/CLASE.md); [B88-C34 · Pruebas de inyección de fallos](../programa/clases/B88/B88-C34-pruebas-de-inyeccion-de-fallos/CLASE.md).

### Campaña con fallas permitidas

- Una campaña con fallas permitidas usa la binomial.

🎯 **Por qué importa (clase B97-C18):** Declarar «el robot funciona» tras diez pruebas buenas no dice nada sin una confiabilidad y una confianza; y una prueba en la Tierra con el robot completo solo se parece a una en Marte si se corrige el peso.

📘 **Dónde se aprende** (1 clase): [B97-C18 · Pruebas en entornos análogos](../programa/clases/B97/B97-C18-pruebas-en-entornos-analogos/CLASE.md).

### Campaña de calificación

- Campaña de calificación: secuencia de ensayos que demuestra la unidad.

🎯 **Por qué importa (clase B90-C20):** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### Campo

- El campo es el ángulo que abarca el sensor: `2 arctan(w/2f)`, con `w` el ancho del sensor.
- El campo tiene nombre, tipo, unidad y escala.
- Un campo tiene nombre, tipo y unidad.

💡 **Cómo se explica en la clase [B08-C19](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md):**
- Para 50 mm y píxeles de 4,3 µm: `escala = 206 265 × 0,0043 / 50 = 17,74″/px`; el campo de un sensor de 36 mm es `2 arctan(18/50) = 39,6°`.
- ⚠️ **Error frecuente:** Confundir campo con escala. Ejercicio 3.
- 🎯 **Por qué importa:** Un teléfono o una cámara réflex puede captar la Vía Láctea o la Luna con detalle, pero una exposición demasiado larga convierte las estrellas en rayas. La pregunta motivadora: ¿cuánto puedo exponer y con qué focal para obtener estrellas puntuales, y qué debo anotar para que la foto sirva como dato?

📘 **Dónde se aprende** (3 clases): [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md); [B88-C21 · Interfaces y documentos de control de software de vuelo](../programa/clases/B88/B88-C21-interfaces-y-documentos-de-control-de-software-de-vuelo/CLASE.md); [B118-C22 · Intercambio de datos de vigilancia entre operadores y Estados](../programa/clases/B118/B118-C22-intercambio-de-datos-de-vigilancia-entre-operadores-y-estados/CLASE.md).

### Campo aparente

- El campo de visión (real) es el ángulo de cielo que ves; el campo aparente es el ángulo que ocupa la imagen en tu vista; el real es aproximadamente `aparente/M`.
- El campo real y el campo aparente.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- El campo real aproximado con un campo aparente de 60° (supuesto) es `60/7 = 8,6°` para 7× y `6,0°` para 10×.
- Paso final · incertidumbre. La ganancia es ideal; la pupila, el campo aparente y el temblor cambian los números.
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?

📘 **Dónde se aprende** (2 clases): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md); [B41-C16 · Telescopios Newton y Dobson](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md).

### Campo cercano

- El campo lejano (Fraunhofer) y el campo cercano (Fresnel).

💡 **Cómo se explica en la clase [B42-C02](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md):**
- Descripción larga: en campo lejano la suma coincide con `sinc²`; en campo cercano no.
- 🎯 **Por qué importa:** Sin este principio no hay un procedimiento para calcular qué le pasa a la luz al pasar por una apertura (la pupila de un telescopio es una). La decisión central: ¿a qué distancia vale la aproximación de campo lejano y cuándo hay que sumar las ondas secundarias una por una?

📘 **Dónde se aprende** (1 clase): [B42-C02 · Principio de Huygens-Fresnel](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md).

### Campo crítico cuántico

- El campo crítico cuántico `B_Q = m_e²c²/(eħ) = 4,414 × 10⁹ T` es aquel en que la energía ciclotrónica iguala `m_ec²`.

🎯 **Por qué importa (clase B27-C06):** Los magnetares producen estallidos y llamaradas gigantes que alimenta su campo, no su rotación. Entender la escala del campo y de su energía explica por qué son una familia aparte y cómo se interpretan sus espectros.

📘 **Dónde se aprende** (1 clase): [B27-C06 · Magnetares y campos extremos](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md).

### Campo de búsqueda

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B42-C21):** La mayoría del cielo no tiene una estrella brillante cerca: la cobertura limita a la óptica adaptativa natural. La decisión central: ¿hasta qué magnitud corrige el lazo y qué fracción del cielo queda cubierta?

📘 **Dónde se aprende** (1 clase): [B42-C21 · Estrellas guía naturales y cobertura de cielo](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md).

### Campo de pendientes

- El campo de pendientes es el conjunto de pendientes `f(t, y)` en una malla de puntos.

🎯 **Por qué importa (clase B11-C03):** Muchos procesos espaciales relajan hacia un equilibrio: una cápsula que cae frena hasta una velocidad terminal, un instrumento se enfría hacia la temperatura de su entorno, una población de partículas decae.

📘 **Dónde se aprende** (1 clase): [B11-C03 · Ecuaciones de primer orden](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md).

### Campo de radiación

- El campo de radiación es el flujo de fotones.

🎯 **Por qué importa (clase B55-C08):** La luz ultravioleta del campo estelar destruye moléculas, y el polvo la apaga: por eso las moléculas sobreviven en el interior de las nubes y no en su superficie. La decisión central: ¿a qué profundidad de nube una molécula deja de ser destruida más rápido de lo que dura la nube?

📘 **Dónde se aprende** (1 clase): [B55-C08 · Fotoquímica cósmica](../programa/clases/B55/B55-C08-fotoquimica-cosmica/CLASE.md).

### Campo de visión

- El campo de visión es el ángulo de cielo visible.
- El campo de visión (real) es el ángulo de cielo que ves; el campo aparente es el ángulo que ocupa la imagen en tu vista; el real es aproximadamente `aparente/M`.
- El campo de visión es el ángulo total de la línea.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B57-C24](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md):**
- El campo de visión de la línea es `20,90°` (Tierra plana).
- 🎯 **Por qué importa:** Cada requisito empuja a los demás: más resolución exige más datos, más barrido exige un campo de visión mayor, y el enlace de bajada limita cuánto se puede adquirir. La decisión central: ¿qué requisito se relaja cuando el presupuesto de datos no cierra?

📘 **Dónde se aprende** (6 clases): [B02-C13 · Galileo y primeras observaciones telescópicas](../programa/clases/B02/B02-C13-galileo-y-primeras-observaciones-telescopicas/CLASE.md); [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md); [B57-C24 · Diseño de una carga útil de observación terrestre](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md); [B58-C11 · Observaciones de seguimiento](../programa/clases/B58/B58-C11-observaciones-de-seguimiento/CLASE.md); [B74-C14 · Navegación con cámaras estelares](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md); [B87-C03 · Sensores solares](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md).

### Campo de visión (FOV)

- Campo de visión (FOV): ángulo total del cono de la cámara.

💡 **Cómo se explica en la clase [B101-C09](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md):**
- De cuántas cámaras, con qué campo de visión y dónde, no se consultó nada (N7).
- La escena de la clase es sintética: una caja de trabajo de 2 × 2 × 1 m centrada en el origen, una carga esférica de 0,4 m de radio en el centro que ocluye, y tres cámaras de 60° de campo de visión circular.
- 🎯 **Por qué importa:** Si el operador no ve el punto de contacto, depende de la imaginación. La decisión central: ¿qué cámaras necesito y dónde para que la zona de trabajo se vea, con qué resolución y sin puntos ciegos críticos?

📘 **Dónde se aprende** (1 clase): [B101-C09 · Coordinación visual y cámaras en operaciones con manipulador](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md).

### Campo dipolar

- El campo dipolar es `B = B₀ (R/r)³ [3(m̂·r̂) r̂ − m̂]`, con `B₀` la intensidad ecuatorial y `m̂` el eje del dipolo.

💡 **Cómo se explica en la clase [B87-C05](../programa/clases/B87/B87-C05-magnetometros/CLASE.md):**
- O["posicion orbital r(t)"] --> D["campo dipolar B(r)"]
- 🎯 **Por qué importa:** Un cubesat sin sensores estelares usa el campo magnético para saber hacia dónde apunta y para detumbling (C16). La decisión central: ¿cuánto varía el campo a lo largo de la órbita, cuánto ruido y sesgo tolera la dirección medida y qué parte de la actitud no ve el magnetómetro?

📘 **Dónde se aprende** (1 clase): [B87-C05 · Magnetómetros](../programa/clases/B87/B87-C05-magnetometros/CLASE.md).

### Campo directo

- El campo directo viene de la fuente; el reverberante, de los rebotes.

💡 **Cómo se explica en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- *Descripción textual:* las fuentes se suman en energía; el recinto aporta absorción y constante; el nivel en un punto mezcla campo directo y reverberante y se compara con el límite y el objetivo para decidir qué fuente bajar.
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Campo ecuatorial

- El campo ecuatorial `B` sale de igualar esa pérdida con la de energía rotacional.

💡 **Cómo se explica en la clase [B27-C05](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md):**
- Un dipolo magnético de campo ecuatorial `B` y radio `R` que rota con `ω` radia en el vacío `P_rad = (8π/3) B² R⁶ ω⁴/(μ₀c³)`.
- 🎯 **Por qué importa:** Un púlsar da, a la vez, un reloj de precisión, la medida de su campo magnético y, en una binaria, la masa de las estrellas y una prueba de la relatividad general. La decisión central: dados el periodo y su derivada, ¿qué campo, edad y potencia de frenado tiene el púlsar y qué se aprende de su binaria?

📘 **Dónde se aprende** (1 clase): [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md).

### Campo eléctrico

- El campo eléctrico `E` en un punto es la fuerza por unidad de carga de prueba, `E = F/q` (N/C = V/m).
- El campo eléctrico `E` y el campo magnético `B`.

💡 **Cómo se explica en la clase [B05-C15](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md):**
- El límite: la masa gravitatoria siempre atrae, pero la carga puede atraer o repeler; y el campo eléctrico se puede apantallar con conductores, la gravedad no.
- 🎯 **Por qué importa:** El espacio está lleno de partículas cargadas que un satélite atraviesa, y un satélite puede acumular carga. La pregunta motivadora es: ¿cómo describir la fuerza eléctrica sobre una carga sin conocer a la vez todas las demás, y cuánto más fuerte es que la gravedad?

📘 **Dónde se aprende** (2 clases): [B05-C15 · Campos eléctricos](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md); [B42-C01 · Ecuaciones de onda electromagnética](../programa/clases/B42/B42-C01-ecuaciones-de-onda-electromagnetica/CLASE.md).

### Campo equivalente

- El campo equivalente es el ángulo del sistema nominal con el mismo RMS.

🎯 **Por qué importa (clase B50-C10):** El descentramiento es una de las tolerancias de montaje que más pesan en un telescopio. La decisión central: ¿cuánto puede desplazarse el secundario antes de degradar la imagen?

📘 **Dónde se aprende** (1 clase): [B50-C10 · Errores de centrado y su efecto en el desempeño](../programa/clases/B50/B50-C10-errores-de-centrado-y-su-efecto-en-el-desempeno/CLASE.md).

### Campo escalar

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B40-C01):** Sin un mecanismo para las condiciones iniciales, el modelo FLRW deja sin explicar la planitud y la homogeneidad. La decisión central: ¿cuántos e-pliegues produce un campo que rueda lentamente y cuándo termina la inflación?

📘 **Dónde se aprende** (2 clases): [B40-C01 · Inflación cósmica: motivación y dinámica básica](../programa/clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md); [B40-C06 · Campos escalares en cosmología: potenciales y evolución](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md).

### Campo geoeléctrico

- El campo geoeléctrico es el campo `E` en el suelo.

💡 **Cómo se explica en la clase [B30-C19](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md):**
- Con un campo geoeléctrico ilustrativo de `1 V/km` en una línea de `100 km` (`R = 5 Ω` y dos tomas de `0,5 Ω`), la corriente es `16,67 A`.
- 🎯 **Por qué importa:** Las infraestructuras se diseñan para eventos raros, que no están en un registro corto. La decisión central: ¿qué corriente induce un campo dado y cuán fiable es extrapolar un nivel de 100 años?

📘 **Dónde se aprende** (2 clases): [B30-C19 · Impactos del clima espacial](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md); [B33-C06 · Corrientes geomagnéticas inducidas (GIC)](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md).

### Campo lejano

- El campo lejano es el de distancias mucho mayores que `λ` y que la antena.
- El campo lejano es la región donde la fase es casi plana.
- El campo lejano es la región donde la onda es localmente plana y `S` decae como `1/r²`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B42-C02](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md):**
- *Descripción textual:* la suma de ondas secundarias de la rendija se compara con la fórmula analítica de campo lejano, y el número de Fresnel decide cuál vale.
- Descripción larga: en campo lejano la suma coincide con `sinc²`; en campo cercano no.
- 🎯 **Por qué importa:** Sin este principio no hay un procedimiento para calcular qué le pasa a la luz al pasar por una apertura (la pupila de un telescopio es una). La decisión central: ¿a qué distancia vale la aproximación de campo lejano y cuándo hay que sumar las ondas secundarias una por una?

📘 **Dónde se aprende** (4 clases): [B42-C02 · Principio de Huygens-Fresnel](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md); [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md); [B49-C05 · Medición y calibración de patrones de antena](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md); [B89-C01 · Electromagnetismo aplicado a enlaces](../programa/clases/B89/B89-C01-electromagnetismo-aplicado-a-enlaces/CLASE.md).

### Campo magnético

- El campo magnético `B` es un campo vectorial que ejerce fuerza sobre cargas en movimiento; su unidad es el tesla (T): `1 T = 1 N/(A·m)`.
- El campo eléctrico `E` y el campo magnético `B`.

💡 **Cómo se explica en la clase [B05-C17](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md):**
- El campo magnético cambia la dirección, no la rapidez.
- Esa página no describe por qué las partículas quedan atrapadas; el mecanismo que enseñamos aquí (giro en un campo magnético) es nuestra explicación, no una cita.
- 🎯 **Por qué importa:** La Tierra tiene un campo magnético que un satélite puede medir con un magnetómetro y que actúa sobre las partículas cargadas que lo atraviesan; además, una corriente a bordo crea su propio campo, que puede perturbar esas medidas.

📖 **Explicado a fondo:** [Campo magnético](esencial/esencial-a-c.md#campo-magnético) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B05-C17 · Campos magnéticos](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md); [B42-C01 · Ecuaciones de onda electromagnética](../programa/clases/B42/B42-C01-ecuaciones-de-onda-electromagnetica/CLASE.md).

### Campo medio

- El campo medio (*mean field*) exige que `q` se factorice en factores independientes, `q(θ) = Π q_i(θ_i)`.

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- Si la pantalla solo admite elipses alineadas con los ejes (campo medio), la sombra de un óvalo inclinado es una elipse más pequeña.
- VI de campo medio es rápido y escalable, con media razonable pero incertidumbre subestimada si hay correlación.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.

📘 **Dónde se aprende** (1 clase): [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### Campo plano

- El campo plano (*flat*) describe la sensibilidad relativa píxel a píxel (S1).
- El campo plano corrige la ganancia píxel a píxel.
- El campo plano (*flat field*).

💡 **Cómo se explica en la clase [B47-C15](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md):**
- Un campo plano a `20 000 e⁻` se reduce de `1,23 %` a `0,72 %`.
- 🎯 **Por qué importa:** Sin ganancia ni ruido calibrados no se puede convertir cuentas en fotones ni dar incertidumbres. La decisión central: ¿cómo se obtiene la ganancia sin conocerla y cuánto residuo deja la corrección de campo plano?

📘 **Dónde se aprende** (3 clases): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B45-C09 · Calibración de respuesta instrumental](../programa/clases/B45/B45-C09-calibracion-de-respuesta-instrumental/CLASE.md); [B47-C15 · Calibración a bordo](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md).

### Campo plenamente iluminado

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C16](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md):**
- En un Newton f/5 de `D = 200 mm` con campo plenamente iluminado de `20 mm` y `q = 130 mm`, el plano necesita `a = 43,40 mm` (`21,7 %` lineal, `4,71 %` por área, `0,0524` mag).
- 🎯 **Por qué importa:** El Newton es el reflector más simple y el Dobson su montura más barata. La decisión central: ¿qué tamaño de plano y qué ocular conviene?

📘 **Dónde se aprende** (1 clase): [B41-C16 · Telescopios Newton y Dobson](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md).

### Campo real

- El campo real y el campo aparente.

💡 **Cómo se explica en la clase [B41-C16](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md):**
- Con ocular de 25 mm (aumento 40) y campo aparente de 52° el campo real es `1,3000° = 4680 "`.
- D["Dobson: campo real"] --> T["transito = campo/(vel. sideral cos dec)"]
- 🎯 **Por qué importa:** El Newton es el reflector más simple y el Dobson su montura más barata. La decisión central: ¿qué tamaño de plano y qué ocular conviene?

📘 **Dónde se aprende** (1 clase): [B41-C16 · Telescopios Newton y Dobson](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md).

### Campo vectorial

- Un campo vectorial asigna un vector a cada punto.

🎯 **Por qué importa (clase B09-C19):** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.

📘 **Dónde se aprende** (1 clase): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md).

### Campo visual

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C11):** Un sensor mal emparejado desperdicia resolución o campo. La decisión central: ¿qué focal y qué píxel dan el campo y el muestreo que busco?

📘 **Dónde se aprende** (1 clase): [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md).

### Campos

- Un registro (fila) contiene los campos: fecha y hora, lugar, objeto, método, instrumento, condiciones, procedencia, observador y notas.

💡 **Cómo se explica en la clase [B08-C17](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md):**
- Estos campos son una propuesta de la clase, no un estándar externo.
- Pausa. Si solo pudieras anotar cuatro campos, ¿cuáles elegirías? <details><summary>Respuesta</summary>Fecha-hora en UT, lugar, objeto o evento y procedencia del dato (observado o calculado): sin ellos no se puede repetir ni juzgar.</details>
- 🎯 **Por qué importa:** Un dato sin fecha, sin lugar o sin procedencia es una anécdota. La pregunta motivadora: ¿qué debo anotar para que mi observación se pueda repetir, revisar y comparar?

📘 **Dónde se aprende** (1 clase): [B08-C17 · Registro sistemático en bitácora](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md).

### Canal

- Un canal es el medio.
- Un canal es una vía de conservación (un relato, un lugar, un canto, una práctica).

💡 **Cómo se explica en la clase [B122-C08](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md):**
- K --> M["matriz: audiencia, canal, aprobador"]
- Por canal: formulario, canal operativo, intranet, comunicado.
- 🎯 **Por qué importa:** B124-C18 trata divulgación; la comunicación de crisis con mensajes oportunos no está cubierta. La decisión central: ¿qué hay que comunicar, a quién y antes de qué plazo?

📘 **Dónde se aprende** (2 clases): [B122-C08 · Comunicación de crisis con operadores, autoridades y público](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md); [B133-C02 · Narrativas orales y transmisión del saber del cielo](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md).

### Canal semicircular

- El canal semicircular mide velocidad angular de la cabeza y su señal decae en un giro constante.

🎯 **Por qué importa (clase B107-C03):** Los fragmentos consultados indican que tras el vuelo hay alteraciones del control postural y locomotor (Macaulay et al., 2021) y que el equilibrio dinámico, la percepción del tiempo y el tiempo de reacción cambian tras el aterrizaje (Clément et al., 2023). Antes del vuelo la pregunta es cómo preparar la desorientación.

📘 **Dónde se aprende** (1 clase): [B107-C03 · Entrenamiento vestibular y de orientación espacial](../programa/clases/B107/B107-C03-entrenamiento-vestibular-y-de-orientacion-espacial/CLASE.md).

### Canal virtual

- El contador de canal maestro (MCFC) cuenta todas las tramas; el de canal virtual (VCFC), las del canal.

💡 **Cómo se explica en la clase [B94-C03](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md):**
- Una trama sintética de 64 octetos lleva SCID `0x2A5`, canal virtual 1, contadores 255 y 7 y puntero 10.
- 🎯 **Por qué importa:** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?

📘 **Dónde se aprende** (1 clase): [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### Canales de comunicación

- Los canales de comunicación de `n` personas son los pares posibles, `n(n−1)/2`.

🎯 **Por qué importa (clase B124-C17):** Agregar gente no siempre acelera: cada persona nueva añade canales de coordinación. La decisión central: ¿cuántas personas y con qué competencias forman un equipo viable?

📘 **Dónde se aprende** (1 clase): [B124-C17 · Gestión de equipos multidisciplinarios](../programa/clases/B124/B124-C17-gestion-de-equipos-multidisciplinarios/CLASE.md).

### Canales libres de línea

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B51-C14):** Una línea débil sobre un continuo brillante solo se ve si la banda está calibrada mejor que la razón línea/continuo. La decisión central: ¿cuánto ruido inyecta la solución de banda y por qué no basta con restar un polinomio?

📘 **Dónde se aprende** (1 clase): [B51-C14 · Calibración de banda en la reducción de datos de síntesis](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md).

### Canales semicirculares

- Los canales semicirculares detectan la velocidad angular.

🎯 **Por qué importa (clase B105-C04):** En la Tierra el cerebro usa la gravedad como referencia de «abajo». En caída libre esa referencia desaparece y el sensor sigue midiendo, pero su señal significa otra cosa.

📘 **Dónde se aprende** (1 clase): [B105-C04 · Sistema vestibular](../programa/clases/B105/B105-C04-sistema-vestibular/CLASE.md).

### Cancelación

- La cancelación es la pérdida de cifras significativas al restar dos números casi iguales.
- Una cancelación numérica es la pérdida de cifras al restar números casi iguales.
- La cancelación (C01) afecta al cálculo numérico cuando `h` es muy pequeño.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C03](../programa/clases/B09/B09-C03-derivada-como-tasa-de-cambio/CLASE.md):**
- Pero reducir `h` sin límite empeora el resultado: con `h = 10⁻¹²` el error sube a `1,6 × 10⁻² m/s` por redondeo y cancelación.
- 🎯 **Por qué importa:** Casi toda cantidad en ciencias espaciales cambia con el tiempo o la posición: la altura de un cohete, la fase de una estrella variable, el brillo de un cometa. Lo que se quiere saber suele ser con qué rapidez cambia, y en qué instante deja de crecer.

📘 **Dónde se aprende** (4 clases): [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B09-C01 · Límites de funciones reales](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md); [B09-C03 · Derivada como tasa de cambio](../programa/clases/B09/B09-C03-derivada-como-tasa-de-cambio/CLASE.md); [B82-C05 · Singularidades del problema de Lambert](../programa/clases/B82/B82-C05-singularidades-del-problema-de-lambert/CLASE.md).

### Cancelación catastrófica

- Una prueba sensible falla cuando el código está mal. Cancelación catastrófica es la pérdida de cifras al restar números casi iguales.
- La cancelación catastrófica es la pérdida de cifras al restar números casi iguales.
- La cancelación catastrófica pierde cifras al restar números casi iguales.

🎯 **Por qué importa (clase B07-C17):** Una función matemática puede dar el resultado correcto en el único caso que probaste y estar mal en los demás. Y es fácil escribir una prueba que no puede fallar: la que compara la función contra sí misma o contra un caso donde el error se esconde.

📘 **Dónde se aprende** (3 clases): [B07-C17 · Pruebas de funciones matemáticas](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md); [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md); [B27-C18 · Neutrinos de supernova](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md).

### Cancelación manual

- Precondición: condición previa. Cancelación manual: orden del operador que detiene la pasada.

🎯 **Por qué importa (clase B96-C24):** Un ejecutor automático sin límites puede colgarse o comandar con el enlace caído. La decisión central: ¿qué debe garantizar el ejecutor ante cualquier combinación de fallos y cómo se prueba?

📘 **Dónde se aprende** (1 clase): [B96-C24 · Operación remota y automatizada de estaciones](../programa/clases/B96/B96-C24-operacion-remota-y-automatizada-de-estaciones/CLASE.md).

### Cancelación numérica

- La cancelación numérica es la pérdida de cifras al restar dos números casi iguales;

🎯 **Por qué importa (clase B04-C13):** Antes de apuntar un telescopio de una estrella a otra, antes de saber si dos objetos caben en el mismo campo de visión, antes de decidir si un planeta está demasiado cerca del Sol para observarlo, hay que saber cuántos grados los separan en el cielo.

📘 **Dónde se aprende** (1 clase): [B04-C13 · Producto escalar y ángulo entre vectores](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md).

### Cancelar unidades

- Un nudo es una milla náutica por hora, es decir, `1852/3600 m/s` (S2). Cancelar unidades es dividir una unidad entre sí misma para eliminarla del resultado.

🎯 **Por qué importa (clase B03-C07):** Una cifra de la NASA como «velocidad de escape 11,186 km/s» no significa lo mismo para quien trabaja en m/s ni para quien piensa en km/h. Si conviertes mal, el error no es de redondeo sino de factor: mil, tres mil seiscientos.

📘 **Dónde se aprende** (1 clase): [B03-C07 · Conversión de distancia y velocidad](../programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/CLASE.md).

### Candidato

- Un candidato es un resultado del índice que aún no se ha verificado con una prueba exacta.
- Un candidato es una hipótesis para la naturaleza de la materia oscura.

🎯 **Por qué importa (clase B14-C28):** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.

📘 **Dónde se aprende** (2 clases): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md); [B31-C17 · Materias oscuras candidatas](../programa/clases/B31/B31-C17-materias-oscuras-candidatas/CLASE.md).

### Cantidad

- Una cantidad es un número con su unidad: 1,022 km/s es una cantidad; 1,022 solo es un número.
- Una cantidad (`Quantity`) en Astropy es un número —o un arreglo— acompañado de una unidad: `15 * u.m / u.s` es `15 m / s` (S2).

💡 **Cómo se explica en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- No es un fallo del programa: es la consecuencia de usar una cantidad finita de cifras binarias.
- ⚠️ **Error frecuente:** Confundir un número con una cantidad. Dar `27,35` sin decir días.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.

📘 **Dónde se aprende** (2 clases): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md); [B07-C11 · Gestión de unidades en programas](../programa/clases/B07/B07-C11-gestion-de-unidades-en-programas/CLASE.md).

### Cantidad adimensional

- Una cantidad adimensional es un número puro, sin unidad.

🎯 **Por qué importa (clase B03-C02):** Una cifra aislada como «69 911 km» no dice si Júpiter es grande o pequeño. Una razón sí: Júpiter tiene un radio unas 11 veces el terrestre.

📘 **Dónde se aprende** (1 clase): [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md).

### Cantidad conservada

- Una cantidad conservada es una función del estado que no cambia a lo largo de una solución.
- Una cantidad conservada es una función del estado que no cambia en la solución exacta (aquí `ε` y `h`, C04).
- Una cantidad conservada es una función del estado que no cambia en el modelo (aquí, la energía específica).

💡 **Cómo se explica en la clase [B14-C03](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md):**
- El árbitro es la verificación: una solución exacta o una cantidad conservada.
- *Descripción textual:* el problema entra al método con sus tolerancias; el resultado se verifica contra una solución exacta o una cantidad conservada; si falla, se vuelve a ajustar el método; si pasa, se registra el método y las tolerancias usados.
- ⚠️ **Error frecuente:** No verificar con una cantidad conservada. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Un integrador devuelve un número aunque sea malo. Con las tolerancias por defecto, una órbita circular puede no cerrarse después de una vuelta y el programa no se queja.

📘 **Dónde se aprende** (3 clases): [B11-C04 · Sistemas de ecuaciones diferenciales](../programa/clases/B11/B11-C04-sistemas-de-ecuaciones-diferenciales/CLASE.md); [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md); [B14-C03 · Análisis numérico con SciPy](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md).

### Cantidad de movimiento

- La cantidad de movimiento es `p = m·v`.

💡 **Cómo se explica en la clase [B77-C07](../programa/clases/B77/B77-C07-separacion-de-etapas-conceptual/CLASE.md):**
- Antes de separar, el marco del centro de masa es inercial y la cantidad de movimiento total vale 0.
- La cantidad de movimiento total sale `0,0e+00` y la energía `3000,0000 J`, iguales a la entrada.
- 🎯 **Por qué importa:** Un `ΔV` alto es inalcanzable con una sola etapa de estructura moderada, pero cada etapa extra rinde menos. La decisión central: ¿cuántas etapas conviene y qué ocurre mecánicamente al separarlas?

📘 **Dónde se aprende** (1 clase): [B77-C07 · Separación de etapas conceptual](../programa/clases/B77/B77-C07-separacion-de-etapas-conceptual/CLASE.md).

### Cantidad de sustancia

- La cantidad de sustancia `n` mide cuántas entidades elementales (átomos, moléculas, iones, electrones…) hay en una muestra.

🎯 **Por qué importa (clase B06-C06):** La misión OSIRIS-REx trajo a la Tierra 121,6 g de material del asteroide Bennu. Los análisis de laboratorio de una parte de esa muestra encontraron entre 4,5 y 4,7 % de carbono y entre 0,23 y 0,25 % de nitrógeno en masa (S1).

📘 **Dónde se aprende** (1 clase): [B06-C06 · Cantidad de sustancia y mol](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md).

### Caos

- El caos es la sensibilidad exponencial a las condiciones iniciales.

🎯 **Por qué importa (clase B52-C19):** Una simulación solo es creíble si conserva lo que debe conservar y si se sabe qué tan sensible es a los datos de partida. La decisión central: ¿cuándo se puede confiar en una integración de largo plazo y cómo se mide el caos?

📘 **Dónde se aprende** (1 clase): [B52-C19 · Estabilidad a largo plazo de sistemas](../programa/clases/B52/B52-C19-estabilidad-a-largo-plazo-de-sistemas/CLASE.md).

### Caótico

- Un régimen regular (`K` pequeño) tiene curvas invariantes que acotan las trayectorias; en el caótico (`K` grande) las trayectorias llenan una región.

💡 **Cómo se explica en la clase [B73-C13](../programa/clases/B73/B73-C13-caos-determinista/CLASE.md):**
- En el caso regular la separación oscila en torno a `10⁻⁹–10⁻⁸` sin crecer exponencialmente; en el caótico crece un factor `e^{1,02}` por iteración hasta saturar en el tamaño del espacio de fases.
- La pendiente de `ln d` entre `n = 0` y `20` en el caso caótico es `1,022`; en el regular, entre `n = 10` y `60`, `-0,030`.
- 🎯 **Por qué importa:** Un sistema determinista puede ser impredecible a largo plazo: el error de medida se amplifica exponencialmente y fija un horizonte más allá del cual la predicción no vale, por más cómputo que se use. La decisión central: ¿hasta cuándo puedo confiar en una integración y cómo reconozco el régimen caótico?

📘 **Dónde se aprende** (1 clase): [B73-C13 · Caos determinista](../programa/clases/B73/B73-C13-caos-determinista/CLASE.md).

### Capa

- Una capa es el resultado de una instrucción apilada sobre las anteriores.
- Una capa es un conjunto de datos servido.
- Una capa es un cascarón de densidad uniforme.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- El orden «dependencias primero, código después» ahorra la capa lenta cuando cambia el código.
- Cada instrucción añade una capa sobre la anterior.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende** (7 clases): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md); [B14-C29 · Servicios de datos geoespaciales estándar (OGC)](../programa/clases/B14/B14-C29-servicios-de-datos-geoespaciales-estandar-ogc/CLASE.md); [B53-C01 · Interior de planetas rocosos](../programa/clases/B53/B53-C01-interior-de-planetas-rocosos/CLASE.md); [B88-C23 · Arquitectura de software de vuelo: capas y ejecutivo](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md); [B118-C01 · Población de objetos orbitales](../programa/clases/B118/B118-C01-poblacion-de-objetos-orbitales/CLASE.md); [B122-C04 · Seguridad de estaciones terrestres y segmento de control](../programa/clases/B122/B122-C04-seguridad-de-estaciones-terrestres-y-segmento-de-control/CLASE.md) y 1 más.

### Capa convolucional aprendida

- Una capa convolucional aprendida ajusta los pesos del núcleo con las etiquetas.

🎯 **Por qué importa (clase B17-C11):** Delimitar una mancha solar, una nube o un cráter a mano en miles de imágenes no escala. Un umbral por píxel falla cuando el ruido es comparable al contraste.

📘 **Dónde se aprende** (1 clase): [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md).

### Capa de Chapman

- La capa de Chapman es la capa donde la producción por fotólisis es máxima.
- La capa de Chapman `q(y)` tiene un máximo único.

💡 **Cómo se explica en la clase [B30-C17](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md):**
- La precipitación es como una lluvia que moja una capa a cierta altura: cuanto más energético el electrón, más profundo llega; la capa de Chapman describe dónde se concentra la ionización.
- *Descripción textual:* la altura y el ángulo cenital dan la capa de Chapman; la energía de los electrones da los pares; la longitud de onda da la energía de los fotones; las conductancias dan la corriente y el calentamiento.
- 🎯 **Por qué importa:** La aurora y las corrientes ionosféricas son la parte visible y eléctrica del acoplamiento entre la magnetosfera y la atmósfera. La decisión central: ¿dónde se produce la ionización y cuánta energía se disipa por efecto Joule?

📘 **Dónde se aprende** (2 clases): [B30-C17 · Auroras y corrientes ionosféricas](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md); [B54-C10 · Fotoquímica atmosférica](../programa/clases/B54/B54-C10-fotoquimica-atmosferica/CLASE.md).

### Capa de cuarto de onda

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B43-C24):** Cada reflexión sin tratar pierde luz y añade luz parásita. La decisión central: ¿cuántas capas y con qué índices y espesores se logra baja reflectancia en la banda visible?

📘 **Dónde se aprende** (1 clase): [B43-C24 · Recubrimientos antirreflectantes de capas múltiples](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md).

### Capa de protección

- Capa de protección: medida física con detección y retardo.

🎯 **Por qué importa (clase B96-C25):** Una alarma que llega tarde no sirve: lo que importa es si el retardo restante supera el tiempo de respuesta cuando se detecta. La decisión central: ¿qué capas y qué tiempo de respuesta dan una probabilidad de interrupción aceptable?

📘 **Dónde se aprende** (1 clase): [B96-C25 · Seguridad física y control de acceso de estaciones terrestres](../programa/clases/B96/B96-C25-seguridad-fisica-y-control-de-acceso-de-estaciones-terrestres/CLASE.md).

### Capa delgada

- La capa delgada: toda la ionosfera en una lámina.
- La capa delgada de altura `H`.

💡 **Cómo se explica en la clase [B51-C05](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md):**
- Límite: plasma frío, capa delgada y campo constante.
- 🎯 **Por qué importa:** A frecuencias bajas la ionosfera domina el error de fase y de polarización. La decisión central: ¿cómo se mide y se quita el efecto con las propias frecuencias de la observación?

📘 **Dónde se aprende** (2 clases): [B51-C05 · Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md); [B51-C10 · Retardo troposférico e ionosférico en VLBI y su modelado](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md).

### Capa isoterma

- Una capa isoterma es una capa de temperatura uniforme que absorbe y emite.
- Una capa isoterma tiene `T` constante.

💡 **Cómo se explica en la clase [B54-C01](../programa/clases/B54/B54-C01-estructura-vertical-de-atmosferas/CLASE.md):**
- En una capa isoterma, `H` es constante y `P = P_b exp(−(z − z_b)/H)`.
- 🎯 **Por qué importa:** Todo lo que sigue en el bloque (balance de energía, convección, nubes, escape) ocurre en una columna de gas con una presión y una temperatura que dependen de la altura. La pregunta motivadora: ¿cómo cae la presión con la altura cuando la temperatura también cambia?

📘 **Dónde se aprende** (2 clases): [B54-C01 · Estructura vertical de atmósferas](../programa/clases/B54/B54-C01-estructura-vertical-de-atmosferas/CLASE.md); [B54-C09 · Efecto invernadero](../programa/clases/B54/B54-C09-efecto-invernadero/CLASE.md).

### Capa L

- La capa `L` es el conjunto de líneas que cruzan el ecuador a `L R_⊕`.

🎯 **Por qué importa (clase B30-C15):** Los satélites geosíncronos están cerca del borde de la magnetosfera cuando el viento es fuerte. La decisión central: ¿dónde está la magnetopausa y qué pasa cuando se comprime?

📘 **Dónde se aprende** (1 clase): [B30-C15 · Magnetosfera terrestre](../programa/clases/B30/B30-C15-magnetosfera-terrestre/CLASE.md).

### Capa protectora

- Una capa protectora de óxido tiene una reactividad mucho menor.

💡 **Cómo se explica en la clase [B85-C13](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md):**
- Por eso los polímeros expuestos en proa a baja altitud necesitan capa protectora o un material resistente.
- Límite: la reactividad real depende de la energía de impacto, la temperatura y de si hay defectos que permiten socavar la capa protectora.
- 🎯 **Por qué importa:** Un polímero exterior puede desaparecer en meses en la cara de proa a baja altitud. La decisión central: ¿cuánto espesor pierde una superficie por año según la altitud y la orientación, y qué protección dura la misión?

📘 **Dónde se aprende** (1 clase): [B85-C13 · Efectos de oxígeno atómico](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md).

### Capa reactiva

- La capa reactiva (reflejos) responde al ritmo del sensor; la ejecutiva interpreta el plan y vigila su ejecución; la deliberativa planifica.

🎯 **Por qué importa (clase B98-C07):** Una arquitectura sin presupuesto de tiempos puede parecer correcta hasta que una tarea lenta retrasa un reflejo. La decisión central: ¿cada capa cumple sus plazos aunque las demás consuman su peor caso, y qué pasa cuando el planificador tarda más de lo previsto?

📘 **Dónde se aprende** (1 clase): [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md).

### Capacidad

- La capacidad se mide en Ah y la energía en Wh.
- La capacidad es `tasa × (fin − inicio)`.
- La capacidad de un canal sin fondo es `(1 − e^{−n_s}) log₂ M` bits por símbolo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B86-C05](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md):**
- Con pérdida de capacidad del `20 %` al fin de vida la energía nominal es `249,8 Wh`, es decir `8,67 Ah` a `28,8 V` (`8S`), lo que exige `3` ramas en paralelo de celdas de `3 Ah`: `24` celdas, `259,2 Wh` instalados y `2,160 kg` a `120 Wh/kg` (dentro del rango de `91` a `250 Wh/kg` de paquetes citado por la NASA).
- ⚠️ **Error frecuente:** Confundir capacidad con energía. Se corrige con 8.2: Ah por tensión da Wh.
- 🎯 **Por qué importa:** Una batería de órbita baja hace unos `5400` ciclos al año. Dimensionarla por la energía de un solo eclipse sin mirar la profundidad de descarga la agota mucho antes del fin de la misión.

📘 **Dónde se aprende** (4 clases): [B86-C05 · Baterías de ion-litio](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md); [B89-C13 · Protocolos para espacio profundo](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md); [B92-C06 · Modulación y codificación en enlaces ópticos](../programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/CLASE.md); [B94-C01 · Códigos Reed-Solomon y LDPC](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md).

### Capacidad aparente

- La capacidad aparente `ID/MT` se mide en bit/s.

🎯 **Por qué importa (clase B111-C01):** Una interfaz mal diseñada convierte a una tripulación competente en una fuente de errores. La decisión central: ¿qué parte del tiempo y del error es del diseño y no de la persona?

📘 **Dónde se aprende** (1 clase): [B111-C01 · Fundamentos de factores humanos en operaciones espaciales](../programa/clases/B111/B111-C01-fundamentos-de-factores-humanos-en-operaciones-espaciales/CLASE.md).

### Capacidad calorífica efectiva

- La capacidad calorífica efectiva `C` fija la inercia térmica.

💡 **Cómo se explica en la clase [B54-C19](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md):**
- Capacidad calorífica efectiva `C = 4,0 × 10⁸ J m⁻² K⁻¹` y albedo `0,62` por debajo de `250 K`, `0,294` por encima de `280 K` y lineal entre ambos: sintéticos.
- 🎯 **Por qué importa:** Un modelo permite preguntar qué pasa si cambia la energía recibida. La pregunta motivadora: ¿puede un mismo planeta tener dos climas estables con la misma energía?

📘 **Dónde se aprende** (1 clase): [B54-C19 · Modelos climáticos planetarios](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md).

### Capacidad calorífica específica

- La capacidad calorífica específica `c` es la energía por kilogramo y por kelvin (J/(kg·K)).

🎯 **Por qué importa (clase B05-C13):** Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: ¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?

📘 **Dónde se aprende** (1 clase): [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md).

### Capacidad de bajada

- La capacidad de bajada es `t_útil × R × eficiencia`.

💡 **Cómo se explica en la clase [B83-C11](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md):**
- E["Enlace y LDPC 7136/8192"] --> K["Capacidad de bajada"]
- *Descripción textual:* la cámara y la velocidad en tierra dan la tasa bruta y, con compresión, la producción diaria; el enlace, la codificación y el contacto dan la capacidad de bajada; su comparación es el margen y la producción en el hueco máximo dimensiona el registrador.
- 🎯 **Por qué importa:** Un satélite que produce más datos de los que puede bajar los pierde o se satura. La decisión central: ¿cabe todo lo que se produce en los minutos de contacto, y qué tamaño de registrador cubre el peor hueco?

📘 **Dónde se aprende** (1 clase): [B83-C11 · Presupuestos de datos](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md).

### Capacidad de carga

- La capacidad de carga `K` es la densidad máxima del cultivo.

💡 **Cómo se explica en la clase [B64-C07](../programa/clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md):**
- Descripción larga: el cultivo sintético crece 4000 veces en 24 h; el oxígeno de una cámara cerrada de 10 L a 100 kPa no basta para llevarlo a la capacidad de carga.
- 🎯 **Por qué importa:** Un análogo no es el otro mundo: reproduce algunas variables y deja otras. La pregunta motivadora: ¿qué parte del ambiente real estás imitando, qué parte no y qué puedes concluir de un cultivo en la cámara?

📘 **Dónde se aprende** (1 clase): [B64-C07 · Cultivo de extremófilos no patógenos en condiciones análogas](../programa/clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md).

### Capacidad de corrección

- Su capacidad de corrección `t` es el número de símbolos erróneos que corrige;

🎯 **Por qué importa (clase B89-C09):** La codificación es la herramienta que permite cerrar enlaces de espacio profundo con potencias modestas: cada decibelio de ganancia de código equivale a una antena más grande o a más potencia. La decisión central: ¿cuánta redundancia añadir y cuánto `Eb/N0` se ahorra con ella?

📘 **Dónde se aprende** (1 clase): [B89-C09 · Codificación correctora de errores](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md).

### Capacidad de reparación

- La capacidad de reparación `n_rep` es el máximo de DSB que la célula repara con fidelidad (simplificación del modelo).

💡 **Cómo se explica en la clase [B64-C01](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md):**
- En la D10 el sensible tiene 5,3 DSB de media y el tolerante 166,9: la D10 corresponde a una media de roturas mayor que la capacidad de reparación porque la distribución de Poisson tiene dispersión.
- *Descripción textual:* la dosis fija la media λ de roturas; la distribución de Poisson da la probabilidad de cada número de roturas; la supervivencia es la probabilidad acumulada hasta la capacidad de reparación; la D10 se busca invirtiendo esa función.
- 🎯 **Por qué importa:** La radiación ionizante rompe el ADN, y una célula muere cuando el daño supera su capacidad de reparación. La pregunta motivadora: ¿por qué dos organismos con el mismo daño inicial por gray sobreviven a dosis tan distintas?

📘 **Dónde se aprende** (1 clase): [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md).

### Capacidad de un lanzador

- La capacidad de un lanzador se expresa como masa útil en función de `C3`.

🎯 **Por qué importa (clase B75-C23):** Un lanzador entrega una masa distinta según la energía que se le pida. La decisión central: ¿cuánta energía característica y cuánto delta-v hay que dar desde una órbita baja para alcanzar un destino?

📘 **Dónde se aprende** (1 clase): [B75-C23 · Energía característica C3 y exceso hiperbólico](../programa/clases/B75/B75-C23-energia-caracteristica-c3-y-exceso-hiperbolico/CLASE.md).

### Capacidad del radiador

- La capacidad del radiador `A(εσT⁴ − q_abs)`.

💡 **Cómo se explica en la clase [B85-C20](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md):**
- *Descripción textual:* la disipación por modo con margen se compara con la capacidad del radiador en el caso caliente; en el frío la capacidad define el calentador; el menor margen indica el modo gobernante.
- 🎯 **Por qué importa:** Un presupuesto sin margen no resiste un cambio de diseño. La decisión central: ¿qué modo gobierna el caso caliente, con cuánto margen cierra y qué calentador pide el frío?

📘 **Dónde se aprende** (1 clase): [B85-C20 · Presupuesto térmico de carga útil](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md).

### Capacidad efectiva

- La capacidad efectiva `E(n)` es el trabajo útil del equipo.

💡 **Cómo se explica en la clase [B124-C17](../programa/clases/B124/B124-C17-gestion-de-equipos-multidisciplinarios/CLASE.md):**
- *Descripción textual:* el tamaño del equipo genera canales y sobrecarga, que limitan la capacidad efectiva; la composición se decide por cobertura de competencias con dos algoritmos; ambas dan la decisión.
- El ejemplo conductor es un modelo sintético: con una pérdida de 4 % del tiempo por cada otra persona, la capacidad efectiva se maximiza en `n* = 13,0` personas (`13` por barrido) y cada persona rinde menos a medida que el equipo crece; de 8 candidatos con 6 competencias, el equipo mínimo que cubre todo tiene `3` personas (`P1,P4,P5`).
- 🎯 **Por qué importa:** Agregar gente no siempre acelera: cada persona nueva añade canales de coordinación. La decisión central: ¿cuántas personas y con qué competencias forman un equipo viable?

📘 **Dónde se aprende** (1 clase): [B124-C17 · Gestión de equipos multidisciplinarios](../programa/clases/B124/B124-C17-gestion-de-equipos-multidisciplinarios/CLASE.md).

### Capacidad térmica

- La capacidad térmica `C` y la conductancia `G` describen la masa y el aislamiento.
- La capacidad térmica `C(T) = m c₀ (T/300)^1,5`.

🎯 **Por qué importa (clase B44-C08):** La cámara no está fría al encenderla. La decisión central: ¿cuánto hay que esperar antes de calibrar y qué temperatura final se alcanza?

📘 **Dónde se aprende** (2 clases): [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md); [B85-C17 · Criogenia de instrumentos](../programa/clases/B85/B85-C17-criogenia-de-instrumentos/CLASE.md).

### Capacidades

- Las capacidades son la descripción de lo que el servicio ofrece (capas, dominios, formatos).

💡 **Cómo se explica en la clase [B14-C29](../programa/clases/B14/B14-C29-servicios-de-datos-geoespaciales-estandar-ogc/CLASE.md):**
- La petición de capacidades devuelve 200 con la capa `demo`, su dominio `[0, 0, 40, 40]`, el máximo de 512 píxeles por lado y el formato `image/x-portable-graymap`.
- *Descripción textual:* el cliente pide las capacidades y el servicio responde con las capas, el dominio, los formatos y los límites.
- 🎯 **Por qué importa:** Has producido un mosaico de imágenes y varias organizaciones quieren verlo en sus propios visores. Enviar archivos a cada una no escala, y cada una usa un programa distinto.

📘 **Dónde se aprende** (1 clase): [B14-C29 · Servicios de datos geoespaciales estándar (OGC)](../programa/clases/B14/B14-C29-servicios-de-datos-geoespaciales-estandar-ogc/CLASE.md).

### CAPE

- La CAPE (energía potencial convectiva disponible) es la integral de la flotabilidad en la capa donde `T_p > T_e`.

💡 **Cómo se explica en la clase [B54-C07](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md):**
- Con exceso constante `ΔT = 2 K` sobre `T_e = 280 K` entre 2 y 10 km, `CAPE = g (ΔT/T_e) H = 9,820 × (2/280) × 8000 = 561,1429 J/kg`.
- Para el ambiente y la parcela de la sección 5, el laboratorio obtiene `CAPE = 2479,8 J/kg` y `w_max = 70,4 m/s`.
- 🎯 **Por qué importa:** La energía convectiva disponible decide si una tormenta tiene vigor o no. La pregunta motivadora: ¿cuánta velocidad puede alcanzar el aire que sube si toda la flotabilidad se convierte en movimiento?

📘 **Dónde se aprende** (1 clase): [B54-C07 · Dinámica de tormentas](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md).

### Capex

- El capex `K` es el costo de capital;
- El CapEx es el costo inicial; el OpEx, el anual.

💡 **Cómo se explica en la clase [B124-C24](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md):**
- Con `r = 8 %` y `n = 15`, `CRF = 0,11683`: el CapEx equivale a `116,689` Mum al año, y el costo anual total a `155,929` Mum.
- M["masa de equipo M"] --> X["CapEx = M (h + c_t)(1 + i)"]
- ⚠️ **Error frecuente:** Comparar CapEx con OpEx sin pasarlos a la misma base anual. Se corrige con 8.2.
- 🎯 **Por qué importa:** B124 estima costos de misión, pero una instalación que opera años necesita separar el capital de la operación y ponerlos en una misma unidad. La decisión central: ¿a qué costo por kilogramo produce la instalación y desde qué producción conviene frente a traer el producto?

📘 **Dónde se aprende** (2 clases): [B124-C02 · Agencias científicas y empresas](../programa/clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md); [B124-C24 · CapEx y OpEx de una instalación extraterrestre](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md).

### Capital

- El capital es el colchón del asegurador.

💡 **Cómo se explica en la clase [B124-C08](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md):**
- El asegurador se arruina si `300 K > 724,0` (primas más capital), es decir `K ≥ 3`: probabilidad exacta `0,0439`, Monte Carlo `0,0445` (diferencia `0,0007`).
- 🎯 **Por qué importa:** El seguro no elimina el riesgo: lo traslada a quien puede juntarlo. La decisión central: ¿cuánto cobrar por cubrir un riesgo y con qué probabilidad el asegurador se queda sin capital?

📘 **Dónde se aprende** (1 clase): [B124-C08 · Seguros y riesgo espacial](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md).

### Cápsula

- Tope articular: límite de ángulo. Cápsula: segmento con radio, modelo de un eslabón.

💡 **Cómo se explica en la clase [B101-C04](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md):**
- Paso 2 · Radios. Cada cápsula mide 0,08 m: suman 0,16 m.
- La cápsula es la más barata y la menos fiel.
- 🎯 **Por qué importa:** Una solución de cinemática inversa que exceda un tope o atraviese el propio brazo no sirve. La decisión central: ¿esta configuración es admisible: respeta los topes y deja holgura entre eslabones?

📘 **Dónde se aprende** (1 clase): [B101-C04 · Límites articulares, espacio de trabajo y evitación de colisiones](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md).

### Captura

- Una captura es el paso de la circulación a la libración; un escape, el contrario.
- La captura es el impulso que reduce la energía para pasar de hipérbola a elipse.

💡 **Cómo se explica en la clase [B73-C12](../programa/clases/B73/B73-C12-captura-y-escape-resonante/CLASE.md):**
- Sin deriva, el ojo en expansión engulle todas las partículas; con deriva, la captura se vuelve probabilística y decrece al aumentar `ν`.
- El objetivo es la lógica de captura y escape; no se calculan probabilidades para un sistema real ni se compara con teoría analítica de la probabilidad de captura (no consultada).
- ⚠️ **Error frecuente:** Esperar captura con deriva grande. Se corrige con 8.4.
- 🎯 **Por qué importa:** Muchas resonancias observadas (satélites, planetas migrantes, asteroides) no son primordiales: los cuerpos entraron en ellas. Saber cuándo una captura es segura y cuándo es improbable, y cuándo un cuerpo atrapado debe escapar, evita explicaciones erróneas.

📘 **Dónde se aprende** (2 clases): [B73-C12 · Captura y escape resonante](../programa/clases/B73/B73-C12-captura-y-escape-resonante/CLASE.md); [B75-C14 · Captura en destino](../programa/clases/B75/B75-C14-captura-en-destino/CLASE.md).

### Captura blanda

- La captura blanda une las naves con baja velocidad relativa y energía disipada.

🎯 **Por qué importa (clase B76-C16):** A velocidades de centímetros por segundo, la captura se decide por la masa, la rigidez y el amortiguamiento. La decisión central: ¿cuánta energía hay que disipar y qué fuerzas aparecen en el contacto?

📘 **Dónde se aprende** (1 clase): [B76-C16 · Acoplamiento y captura](../programa/clases/B76/B76-C16-acoplamiento-y-captura/CLASE.md).

### Captura exitosa

- Inversión de orden: cambio de signo de la orden. Captura exitosa: dentro de las tolerancias de posición y velocidad.

🎯 **Por qué importa (clase B101-C10):** Cuanto más tarda en llegar la imagen y la orden, más difícil es corregir. La decisión central: ¿con qué retardo total y qué ganancia el operador puede capturar con éxito y cuándo conviene pasar a «mover y esperar»?

📘 **Dónde se aprende** (1 clase): [B101-C10 · Simulación de una tarea tripulada con manipulador](../programa/clases/B101/B101-C10-simulacion-de-una-tarea-tripulada-con-manipulador/CLASE.md).

### Captura temporal

- Una captura temporal es una permanencia dentro de la esfera de Hill por un tiempo finito antes de escapar.

💡 **Cómo se explica en la clase [B73-C22](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md):**
- Por tiempo de residencia: captura temporal.
- Descripción larga: tres comportamientos del ángulo coorbital en 200 años, con la constante de Jacobi intacta y una captura temporal que dura menos de un año con velocidad alta.
- 🎯 **Por qué importa:** Un asteroide puede acompañar a la Tierra durante siglos sin orbitarla: dando vueltas alrededor de L4 (tadpole), de L3–L4–L5 (herradura) o de la propia Tierra (cuasi-satélite); y puede ser capturado temporalmente dentro de su esfera de Hill. Distinguirlos requiere una clasificación operativa y una advertencia: no son satélites.

📘 **Dónde se aprende** (1 clase): [B73-C22 · Capturas temporales y cuasi-satélites](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md).

### Cara de proa

- La cara de proa es la que mira en el sentido del movimiento.

💡 **Cómo se explica en la clase [B85-C13](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md):**
- A `400 km`, una película de `25 µm` dura `0,41 meses` en la cara de proa; una capa de óxido de `100 nm` con `Re = 3 × 10⁻²⁸ cm³/átomo` (ilustrativa) dura `16,5 meses`.
- A `400 km` con `n_O = 10¹⁵ m⁻³`, la cara de proa recibe `7,67 × 10¹⁸ átomos/(m² s)` y un polímero con `Re = 3 × 10⁻²⁴ cm³/átomo` pierde `726 µm` al año: una película de `25 µm` dura `0,41 meses`.
- 🎯 **Por qué importa:** Un polímero exterior puede desaparecer en meses en la cara de proa a baja altitud. La decisión central: ¿cuánto espesor pierde una superficie por año según la altitud y la orientación, y qué protección dura la misión?

📘 **Dónde se aprende** (1 clase): [B85-C13 · Efectos de oxígeno atómico](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md).

### Cara trasera adiabática

- La cara trasera adiabática modela una estructura que no conduce el calor hacia fuera.

🎯 **Por qué importa (clase B77-C16):** La temperatura de la cara trasera es la que decide si la estructura sobrevive. La decisión central: ¿cuánto del calor entrante se re-radia, cuánto se almacena y cuánto sube la temperatura trasera con un espesor dado?

📘 **Dónde se aprende** (1 clase): [B77-C16 · Protección térmica](../programa/clases/B77/B77-C16-proteccion-termica/CLASE.md).

### Carácter de datos

- En SpaceWire, el carácter de datos usa 10 bits en este laboratorio (supuesto).

💡 **Cómo se explica en la clase [B88-C07](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md):**
- Con 10 bits por carácter de datos (supuesto) y 4 bits para el fin de paquete: `(2 + n)·10 + 4` bits.
- 🎯 **Por qué importa:** El bus fija cuánta telemetría y cuántos comandos caben y con qué retardo. La decisión central: ¿cuál es el caudal útil y el peor tiempo de trama de cada bus para mi carga?

📘 **Dónde se aprende** (1 clase): [B88-C07 · Buses I2C SPI CAN y SpaceWire](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md).

### Característica

- Una característica (*feature*) es una variable de entrada del modelo; puede ser una columna medida o una calculada a partir de otras.

💡 **Cómo se explica en la clase [B17-C01](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md):**
- Una característica puede ser una de ellas tal cual, o una combinación como `T_obs / P`.
- Lo importante es que cada característica tenga una unidad declarada (o sea adimensional) y una fórmula escrita.
- ⚠️ **Error frecuente:** Confundir la característica con la verdad. Una razón fuera de 1 señala, no condena (ejercicio 7).
- 🎯 **Por qué importa:** Un modelo de aprendizaje automático no sabe física: solo ve números. Si le das la duración de un tránsito en segundos y el periodo en días, la columna con números más grandes domina cualquier cálculo de distancias, y la clasificación depende de una elección de unidades que nada tiene que ver con el cielo.

📘 **Dónde se aprende** (1 clase): [B17-C01 · Ingeniería de características científicas](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md).

### Característica local

- Característica local: punto distintivo de una imagen y su entorno.

🎯 **Por qué importa (clase B99-C02):** Una esquina de una roca puede verse distinta cuando cambian el brillo, el ruido o el punto de vista, y dos rocas parecidas se confunden. La decisión central: ¿qué puntos conviene usar, cómo se describen y cuándo se acepta un emparejamiento?

📘 **Dónde se aprende** (1 clase): [B99-C02 · Detección y descriptores de características](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md).

### Característica saliente

- La característica saliente anula la onda entrante.

🎯 **Por qué importa (clase B35-C10):** Las fronteras de los modelos heliosféricos deben dejar salir las ondas. La decisión central: ¿refleja la frontera la onda y con qué signo y amplitud?

📘 **Dónde se aprende** (1 clase): [B35-C10 · Condiciones de frontera en modelos MHD](../programa/clases/B35/B35-C10-condiciones-de-frontera-en-modelos-mhd/CLASE.md).

### Carcasa atérmica

- La carcasa atérmica tiene `α_h = α_f`.

💡 **Cómo se explica en la clase [B50-C12](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md):**
- Descripción larga: la carcasa atérmica casi anula el defocus.
- 🎯 **Por qué importa:** Un telescopio que se enfría de noche se desenfoca si sus materiales se dilatan distinto. La decisión central: ¿qué dilatación debe tener la estructura para que el foco no se mueva?

📘 **Dónde se aprende** (1 clase): [B50-C12 · Sensibilidad térmica del desempeño óptico y atermalización](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md).

### Carga

- La conservación de los átomos y de la carga son las condiciones que exigimos a una ecuación balanceada.
- La carga `w(t)` es el esfuerzo del día `t`.
- La carga `w` es la dosis diaria de entrenamiento (u.a.).

💡 **Cómo se explica en la clase [B06-C08](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md):**
- En las ecuaciones con iones también se conserva la carga neta.
- `NH₃ + HCOOH → NH₄⁺ + HCOO⁻`: a la izquierda, carga 0; a la derecha, +1 − 1 = 0.
- ⚠️ **Error frecuente:** Olvidar la carga en una ecuación iónica. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Una vela y el Sol liberan energía, pero lo hacen de maneras radicalmente distintas. En la vela, los átomos de carbono e hidrógeno se reordenan con el oxígeno y todos siguen ahí al terminar.

📘 **Dónde se aprende** (3 clases): [B06-C08 · Reacciones y conservación de masa](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md); [B104-C04 · Acondicionamiento físico general](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md); [B107-C01 · Entrenamiento cardiorrespiratorio y de resistencia de astronautas](../programa/clases/B107/B107-C01-entrenamiento-cardiorrespiratorio-y-de-resistencia-de-astronautas/CLASE.md).

### Carga aguda

- La carga aguda es el promedio de los últimos 7 días; la crónica, el de 28.

🎯 **Por qué importa (clase B107-C05):** El fragmento consultado de English et al. (2015) subraya que la pérdida de fuerza en misiones largas implica riesgos operativos y médicos, entre ellos el egreso de emergencia; y Loehr et al.

📘 **Dónde se aprende** (1 clase): [B107-C05 · Prevención de lesiones en entrenamiento y trabajo operativo](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md).

### Carga ante racha

- El control de actitud fija mantiene `θ = 0`; la carga ante racha es `q·α`.

🎯 **Por qué importa (clase B77-C23):** Un vehículo inestable es controlable si el control es más rápido que la divergencia, pero el control a su vez fija las cargas ante rachas. La decisión central: ¿cuánto control hace falta para estabilizar un lanzador y qué ángulo de ataque deja una racha según la ganancia?

📘 **Dónde se aprende** (1 clase): [B77-C23 · Estabilidad de vuelo de lanzadores en ascenso](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md).

### Carga axial equivalente

- La carga axial equivalente de un momento en un anillo de diámetro `D` es `4M/D`.

🎯 **Por qué importa (clase B84-C09):** Un margen sin una carga bien planteada no vale: la carga lateral actúa con brazo de palanca y puede exigir más al anillo que la axial. La decisión central: ¿qué margen tiene el anillo de interfaz con las cargas límite y los factores de seguridad estándar?

📘 **Dónde se aprende** (1 clase): [B84-C09 · Análisis de cargas](../programa/clases/B84/B84-C09-analisis-de-cargas/CLASE.md).

### Carga bariónica

- La carga bariónica `R = 3ρ_b/(4ρ_γ)`.

🎯 **Por qué importa (clase B36-C07):** Una regla estándar permite medir distancias si se conoce su longitud. La decisión central: ¿cuánto mide la regla y cuál es la precisión con que se puede medir su dilatación?

📘 **Dónde se aprende** (1 clase): [B36-C07 · Oscilaciones acústicas bariónicas como regla estándar](../programa/clases/B36/B36-C07-oscilaciones-acusticas-barionicas-como-regla-estandar/CLASE.md).

### Carga base

- DoD: profundidad de descarga. Carga base: consumo de la plataforma.

💡 **Cómo se explica en la clase [B96-C12](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md):**
- Un satélite sintético con paneles de 45 W en luz, carga base de 16 W, carga útil de 14 W, batería de 40 Wh y eficiencia de 0,92 pasa 35,61 min en eclipse y 60,04 min en luz.
- Con solo la carga base la DoD es de 23,8 %; con la carga útil 20 min en luz, 23,8 %; 20 min en eclipse, 35,4 %; 30 min en eclipse, 41,3 %.
- 🎯 **Por qué importa:** Una batería descargada en exceso se degrada y una nave sin energía deja de ser comandable. La decisión central: ¿qué plan de operación mantiene la batería dentro de su criterio de descarga y recupera la carga en cada órbita?

📘 **Dónde se aprende** (1 clase): [B96-C12 · Gestión de energía en operaciones](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md).

### Carga biológica

- La carga biológica es el número de microorganismos viables en una nave.

💡 **Cómo se explica en la clase [B56-C17](../programa/clases/B56/B56-C17-control-de-contaminacion-biologica/CLASE.md):**
- La política COSPAR 2026 (S1, texto completo consultado el 2026-11-09), sección 6.1.2.2.2, exige a las misiones de categoría IVa a Marte: carga biológica total en Marte `≤ 5 × 10⁵` esporas (superficial, de contacto y encapsulada), carga superficial `≤ 3 × 10⁵` esporas y densidad media `≤ 300 esporas/m²`.
- 🎯 **Por qué importa:** Una nave que lleva microorganismos terrestres puede contaminar otro mundo y confundir una futura búsqueda de vida. La política fija límites cuantitativos.

📘 **Dónde se aprende** (1 clase): [B56-C17 · Control de contaminación biológica](../programa/clases/B56/B56-C17-control-de-contaminacion-biologica/CLASE.md).

### Carga crítica

- Proceso de Poisson: llegada aleatoria de cortes. Carga crítica: lo que no puede apagarse.
- Una carga crítica no se deslastra.

🎯 **Por qué importa (clase B48-C07):** Un respaldo mal dimensionado deja la cúpula abierta con lluvia. La decisión central: ¿qué autonomía cubre la mayoría de los cortes?

📘 **Dónde se aprende** (2 clases): [B48-C07 · Seguridad en instalaciones remotas](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md); [B86-C23 · Priorización y deslastre de cargas eléctricas](../programa/clases/B86/B86-C23-priorizacion-y-deslastre-de-cargas-electricas/CLASE.md).

### Carga crítica de Euler

- La carga crítica de Euler es `P_cr = π²EI/(KL)²` con `K = 1; 0,5; 0,7; 2` según los apoyos.

🎯 **Por qué importa (clase B84-C23):** Una columna de aluminio de 30 × 10 mm y 0,5 m se pandea a 6810 N, cuando su sección podría soportar 82 500 N en compresión simple: el 8 %. La decisión central: ¿a qué carga pandea un elemento esbelto y cómo cambia con los apoyos y con el espesor?

📘 **Dónde se aprende** (1 clase): [B84-C23 · Vigas y placas: flexión y pandeo](../programa/clases/B84/B84-C23-vigas-y-placas-flexion-y-pandeo/CLASE.md).

### Carga de apertura

- La carga de apertura es `F = Cx·q·CdA`, con `Cx` el factor de inflado.

💡 **Cómo se explica en la clase [B77-C18](../programa/clases/B77/B77-C18-aterrizaje-y-recuperacion/CLASE.md):**
- ⚠️ **Error frecuente:** Ignorar el factor de inflado en la carga de apertura. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un paracaídas grande da un aterrizaje suave pero una apertura brusca; un motor da control pero consume propelente. La decisión central: ¿qué velocidad de contacto, qué carga de apertura y qué altura de encendido resultan de cada opción?

📘 **Dónde se aprende** (1 clase): [B77-C18 · Aterrizaje y recuperación](../programa/clases/B77/B77-C18-aterrizaje-y-recuperacion/CLASE.md).

### Carga de gas

- La velocidad de bombeo `S` y la carga de gas `Q = q A` fijan `p(t) = p_u + (p₀ − p_u)e^(−St/V)` con `p_u = Q/S`.

🎯 **Por qué importa (clase B85-C12):** El vacío cambia cómo el gas conduce el calor, cómo se desgasifican los materiales y cuánto tarda un ensayo. La decisión central: ¿cuánto tarda una cámara en llegar a la presión de ensayo y qué la limita?

📘 **Dónde se aprende** (1 clase): [B85-C12 · Entorno de vacío](../programa/clases/B85/B85-C12-entorno-de-vacio/CLASE.md).

### Carga de masa

- La carga de masa `λ` es la masa de gas expulsada por cada unidad de masa estelar formada.
- La carga de masa `β = f_th η_SN E_SN/(½ v_w²)`.

💡 **Cómo se explica en la clase [B38-C07](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md):**
- *Descripción textual:* la formación estelar produce supernovas cuya energía expulsa gas con una carga de masa, y el gas se estabiliza donde la entrada iguala a las pérdidas.
- 🎯 **Por qué importa:** El gas denso forma estrellas por debajo de la resolución de la simulación y las supernovas devuelven energía. La decisión central: ¿cuánto gas expulsa la retroalimentación y a qué equilibrio llega la zona?

📘 **Dónde se aprende** (2 clases): [B25-C17 · Metalicidad y evolución química](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md); [B38-C07 · Modelos submalla de formación estelar y retroalimentación](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md).

### Carga de potencia constante

- La carga de potencia constante demanda más corriente si baja su tensión.
- Arnés: conjunto de cables y conectores. Carga de potencia constante: carga cuya corriente sube cuando baja la tensión.

💡 **Cómo se explica en la clase [B86-C07](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md):**
- Una carga de potencia constante cumple `P = (V − R I) I` (con `R` de ida y vuelta), lo que da `I = (V − √(V² − 4RP))/(2R)`.
- Con `R = 1,376 Ω` (`2 m`, `0,05 mm²`) y `28 V`, una carga de potencia constante no puede pedir más de `V²/(4R) = 142,4 W`; por encima de eso la ecuación no tiene solución.
- 🎯 **Por qué importa:** Un cable largo y fino desperdicia potencia y baja la tensión que ve el equipo; uno grueso pesa. La tensión del bus cambia la corriente, y por tanto las pérdidas, con el cuadrado.

📘 **Dónde se aprende** (2 clases): [B86-C07 · Distribución de potencia](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md); [B90-C07 · Integración eléctrica de buses](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md).

### Carga de puerta

- La carga de puerta `Q_g` cuesta energía en cada ciclo.

🎯 **Por qué importa (clase B86-C09):** La eficiencia no se mejora subiendo o bajando la frecuencia sin más: las pérdidas de conmutación crecen con ella y las de rizado decrecen. La temperatura de unión marca además el límite de fiabilidad del componente.

📘 **Dónde se aprende** (1 clase): [B86-C09 · Electrónica de potencia](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md).

### Carga de supervivencia

- La carga de supervivencia es la mínima para mantener la nave viva y caliente.

💡 **Cómo se explica en la clase [B86-C22](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md):**
- P["carga de supervivencia P"] --> E["E = P x t_noche"]
- *Descripción textual:* el periodo sinódico da la duración de la noche; con la carga de supervivencia se obtiene la energía; ésta fija la masa de batería y de pila, mientras el RTG se dimensiona por potencia; la comparación da el mejor sistema y los cruces.
- 🎯 **Por qué importa:** Una batería dimensionada para un eclipse orbital no sirve para una noche lunar: la energía crece unas doscientas veces y la masa de la batería deja de ser razonable. Por eso la estrategia cambia de almacenar a generar de otra manera.

📘 **Dónde se aprende** (1 clase): [B86-C22 · Suministro de energía durante la noche lunar](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md).

### Carga de trabajo

- La carga de trabajo es la demanda que una tarea impone a una persona.
- Margen de datos: `capacidad/demanda − 1`. Carga de trabajo: minutos de operador por día.

💡 **Cómo se explica en la clase [B96-C02](../programa/clases/B96/B96-C02-concepto-de-operaciones-de-mision/CLASE.md):**
- La carga de trabajo es de `5 × (4,77 + 10) = 73,8 min/día`.
- 🎯 **Por qué importa:** Un ConOps que no cierra se descubre en órbita, cuando ya no tiene arreglo barato. La decisión central: ¿alcanzan los contactos para bajar lo que la misión genera, con margen?

📘 **Dónde se aprende** (2 clases): [B96-C02 · Concepto de operaciones de misión](../programa/clases/B96/B96-C02-concepto-de-operaciones-de-mision/CLASE.md); [B111-C03 · Carga cognitiva y gestión de la atención](../programa/clases/B111/B111-C03-carga-cognitiva-y-gestion-de-la-atencion/CLASE.md).

### Carga diferencial

- La carga diferencial entre superficies y la descarga son los riesgos.

🎯 **Por qué importa (clase B85-C15):** Una carga diferencial de kilovoltios entre superficies puede producir una descarga que daña la electrónica. La decisión central: ¿a qué potencial flota una superficie en un plasma dado y es probable que alcance un umbral de riesgo?

📘 **Dónde se aprende** (1 clase): [B85-C15 · Electrificación superficial](../programa/clases/B85/B85-C15-electrificacion-superficial/CLASE.md).

### Carga efectiva

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C09):** Medir ΔE y E permite identificar la partícula. La decisión central: ¿qué espesor de detector y qué energía separan protones de partículas alfa?

📘 **Dónde se aprende** (1 clase): [B47-C09 · Detectores de partículas — Instrumentación y observatorios espaciales](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md).

### Carga eléctrica

- La carga eléctrica `q` es una propiedad de la materia, con signo; su unidad es el culombio (C); la carga elemental es `e`.

🎯 **Por qué importa (clase B05-C15):** El espacio está lleno de partículas cargadas que un satélite atraviesa, y un satélite puede acumular carga. La pregunta motivadora es: ¿cómo describir la fuerza eléctrica sobre una carga sin conocer a la vez todas las demás, y cuánto más fuerte es que la gravedad?

📘 **Dónde se aprende** (1 clase): [B05-C15 · Campos eléctricos](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md).

### Carga elemental

- La carga eléctrica `q` es una propiedad de la materia, con signo; su unidad es el culombio (C); la carga elemental es `e`.

💡 **Cómo se explica en la clase [B05-C15](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md):**
- CODATA 2022 da la carga elemental `e = 1,602 176 634 × 10⁻¹⁹ C` (exacta, S2), la masa del protón `1,672 621 925 95 × 10⁻²⁷ kg` y la del electrón `9,109 383 7139 × 10⁻³¹ kg` (S3, S4), la permitividad del vacío `8,854 187 8188 × 10⁻¹² F/m` (S1) y la constante de gravitación `6,674 30 × 10⁻¹¹` (S5).
- 🎯 **Por qué importa:** El espacio está lleno de partículas cargadas que un satélite atraviesa, y un satélite puede acumular carga. La pregunta motivadora es: ¿cómo describir la fuerza eléctrica sobre una carga sin conocer a la vez todas las demás, y cuánto más fuerte es que la gravedad?

📘 **Dónde se aprende** (1 clase): [B05-C15 · Campos eléctricos](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md).

### Carga latente

- Relación de humedad `w`: `0,622 p_v/(P − p_v)`. Carga latente: potencia por vapor.

💡 **Cómo se explica en la clase [B106-C07](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md):**
- En 120 m³ a 22 °C y 45 % de humedad (punto de rocío 9,52 °C), cuatro personas que emiten 6 kg/día de vapor (ilustrativo) llevan la humedad al 75 % (límite de salud consultado) en 2,9 h si no se retira nada; la carga latente es 170 W.
- 🎯 **Por qué importa:** Sin convección y con 4 personas, el vapor se acumula, sube la humedad relativa y se condensa en superficies frías. La decisión central: ¿cuánto vapor hay que retirar y con qué superficie fría, sin condensar sobre las paredes?

📘 **Dónde se aprende** (1 clase): [B106-C07 · Gestión de humedad](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md).

### Carga lateral

- La carga lateral se estima con `q·α`.

💡 **Cómo se explica en la clase [B77-C10](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md):**
- La carga lateral por una racha `w` induce `α ≈ w/v`; entonces `q·α = ½ρ·v·w`, máxima a los `24,0 s` (`1,35 kPa·rad`), antes que max-q: cuando el cohete aún va lento la racha inclina más el flujo.
- *Descripción textual:* empuje, arrastre y masa dan la aceleración axial; si supera el límite se estrangula el empuje, con un costo en velocidad; por otra vía, `q` y la racha dan la carga lateral.
- 🎯 **Por qué importa:** El mayor empuje reduce las pérdidas pero carga la estructura, sobre todo al final del quemado, cuando la masa es menor. La decisión central: ¿qué límite de carga impone la estructura y cuánta velocidad cuesta respetarlo?

📘 **Dónde se aprende** (1 clase): [B77-C10 · Restricciones de cargas estructurales](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md).

### Carga límite

- La carga límite es la máxima esperada en servicio.
- La carga límite es la máxima esperada; la carga última es `FS × límite`.

💡 **Cómo se explica en la clase [B77-C10](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md):**
- Por diseño: carga límite × factor de seguridad.
- ⚠️ **Error frecuente:** Confundir carga límite con carga de diseño. Se corrige con 8.3.
- 🎯 **Por qué importa:** El mayor empuje reduce las pérdidas pero carga la estructura, sobre todo al final del quemado, cuando la masa es menor. La decisión central: ¿qué límite de carga impone la estructura y cuánta velocidad cuesta respetarlo?

📘 **Dónde se aprende** (2 clases): [B77-C10 · Restricciones de cargas estructurales](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md); [B84-C09 · Análisis de cargas](../programa/clases/B84/B84-C09-analisis-de-cargas/CLASE.md).

### Carga lineal

- La carga lineal es el peso más la inercia.

💡 **Cómo se explica en la clase [B97-C10](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md):**
- M["masa m, g, a"] --> W["carga lineal W/2"]
- Paso 1 · Carga lineal. `W = 2 × (3,73 + 0,5) = 8,46` N en Marte;
- 🎯 **Por qué importa:** Un agarre insuficiente deja caer o gira la herramienta; uno excesivo daña el mango. Saber qué carga domina evita diseñar el agarre solo con el peso, error frecuente cuando se reduce la gravedad.

📘 **Dónde se aprende** (1 clase): [B97-C10 · Manipulación de herramientas](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md).

### Carga microbiana

- La carga microbiana son los microorganismos por gramo o por mililitro.

💡 **Cómo se explica en la clase [B115-C07](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md):**
- El artículo señala que no hay norma de carga microbiana para producto fresco cultivado en el espacio; los límites de la NASA para alimento no termoestabilizado (< 2×10⁴ UFC/g en una muestra o < 1×10⁴ en dos de cinco) se aplican a alimento preenvasado.
- 🎯 **Por qué importa:** Una contaminación en un circuito compartido afecta a todos los lotes a la vez. La decisión central: ¿con qué frecuencia se muestrea, qué se mide y qué barreras (desinfección, lavado, temperatura) hacen falta para que una contaminación se detecte antes de llegar a un nivel de acción?

📘 **Dónde se aprende** (1 clase): [B115-C07 · Bioseguridad e inocuidad alimentaria en hábitats](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md).

### Carga monotónica

- La carga monotónica analítica es `σ = σ_y + E_t(ε − σ_y/E)` con `E_t = EH/(E+H)`.

🎯 **Por qué importa (clase B84-C25):** Un modelo lineal da tensiones de 400 MPa en un material que cedió a 275: el resultado correcto es una deformación permanente y una tensión residual que solo el análisis no lineal muestra. La decisión central: ¿qué deformación permanente y tensión residual deja una carga que excede el límite elástico, y cuándo actúa un contacto?

📘 **Dónde se aprende** (1 clase): [B84-C25 · Comportamiento estructural no lineal: plasticidad y contacto](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md).

### Carga parásita

- La carga parásita es el calor que llega a la punta fría.

💡 **Cómo se explica en la clase [B47-C13](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md):**
- Con emisividad `0,02`, área `0,2 m²`, 4 soportes y 50 kg de criógeno (ilustrativos), la carga parásita baja de `818,2 mW` sin escudos a `28,0 mW` con 40 escudos, y la vida pasa de `0,040` a `1,182 años`.
- 🎯 **Por qué importa:** Cada vatio parásito acorta la vida de un criógeno. La decisión central: ¿cuántos escudos y qué soportes bastan para una vida útil dada?

📘 **Dónde se aprende** (2 clases): [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md); [B85-C17 · Criogenia de instrumentos](../programa/clases/B85/B85-C17-criogenia-de-instrumentos/CLASE.md).

### Carga ponderada

- La carga ponderada es `Σ valoración × peso / 15`; la cruda, la media simple.

💡 **Cómo se explica en la clase [B111-C03](../programa/clases/B111/B111-C03-carga-cognitiva-y-gestion-de-la-atencion/CLASE.md):**
- La carga ponderada es `(70×5 + 20×0 + 80×4 + 35×1 + 65×3 + 40×2)/15 = 980/15 = 65,333`.
- La carga ponderada es una medida subjetiva; no equivale a la capacidad real, y un valor alto no dice qué rediseñar.
- 🎯 **Por qué importa:** Ninguna clase trataba la carga cognitiva ni el diseño de tareas para limitarla. La decisión central: ¿cómo se mide la carga y cómo se rediseña una secuencia para que no haya picos que superen la capacidad?

📘 **Dónde se aprende** (1 clase): [B111-C03 · Carga cognitiva y gestión de la atención](../programa/clases/B111/B111-C03-carga-cognitiva-y-gestion-de-la-atencion/CLASE.md).

### Carga por rueda

- La carga por rueda `N` es la fuerza normal.

🎯 **Por qué importa (clase B102-C04):** Un rover cruza rocas sin muelles ni amortiguadores. La decisión central: ¿dónde colocar el pivote del cuerpo para repartir la carga, y qué escalón puede subir una rueda con la tracción disponible?

📘 **Dónde se aprende** (1 clase): [B102-C04 · Suspensión rocker-bogie y mecánica de rovers](../programa/clases/B102/B102-C04-suspension-rocker-bogie-y-mecanica-de-rovers/CLASE.md).

### Carga semanal

- La carga semanal `L` está en unidades arbitrarias.

💡 **Cómo se explica en la clase [B105-C16](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md):**
- L["carga semanal L"] --> R["R = Rmax L/(L+L50)"]
- *Descripción textual:* la carga semanal reduce la tasa de pérdida con una curva saturante y, a la vez, cuesta energía; se compara el beneficio con el costo.
- 🎯 **Por qué importa:** Más ejercicio ayuda, pero con rendimientos decrecientes y con un costo de energía y tiempo. La decisión central: ¿qué parte de la pérdida se evita con una carga dada y cuánta energía extra exige?

📘 **Dónde se aprende** (1 clase): [B105-C16 · Contramedidas de ejercicio](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md).

### Carga térmica

- La carga térmica es el calor que llega a una etapa.
- La carga térmica es `Q = ∫q̇ dt`.
- Carga térmica: potencia que hay que evacuar.

🎯 **Por qué importa (clase B49-C07):** Cada kelvin ahorrado exige vatios en la cabeza fría, y cada vatio de carga reduce el margen. La decisión central: ¿a qué temperatura enfriar y cuánta carga admite el criostato?

📘 **Dónde se aprende** (3 clases): [B49-C07 · Criogenia y refrigeración de receptores de radio](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md); [B77-C15 · Calentamiento aerodinámico](../programa/clases/B77/B77-C15-calentamiento-aerodinamico/CLASE.md); [B106-C08 · Control térmico interior](../programa/clases/B106/B106-C08-control-termico-interior/CLASE.md).

### Carga triboeléctrica

- Modelo de cuerpo humano: circuito RC que representa la descarga de una persona. Carga triboeléctrica: carga generada por contacto y separación de materiales.

🎯 **Por qué importa (clase B90-C03):** Un componente electrónico puede quedar con una falla latente tras una descarga que nadie sintió: una persona percibe una chispa solo por encima de unos miles de voltios (orden de magnitud no consultado), por encima de lo que puede dañar a un componente sensible.

📘 **Dónde se aprende** (1 clase): [B90-C03 · Protección frente a ESD](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md).

### Carga última

- La carga límite es la máxima esperada; la carga última es `FS × límite`.
- La carga última es `FS × carga límite`.

🎯 **Por qué importa (clase B84-C09):** Un margen sin una carga bien planteada no vale: la carga lateral actúa con brazo de palanca y puede exigir más al anillo que la axial. La decisión central: ¿qué margen tiene el anillo de interfaz con las cargas límite y los factores de seguridad estándar?

📘 **Dónde se aprende** (2 clases): [B84-C09 · Análisis de cargas](../programa/clases/B84/B84-C09-analisis-de-cargas/CLASE.md); [B84-C24 · Factores de seguridad y márgenes estructurales](../programa/clases/B84/B84-C24-factores-de-seguridad-y-margenes-estructurales/CLASE.md).

### Carga útil

- La carga útil es el conjunto de instrumentos que cumple la misión.
- La carga útil es `m₀ e^{−Δv/v_e} − α P`, con `P = m₀ a v_e/(2η)` la potencia y `α` la masa específica.

💡 **Cómo se explica en la clase [B57-C24](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md):**
- Es el ejemplo conductor; no es la carga útil de ninguna misión.
- 🎯 **Por qué importa:** Cada requisito empuja a los demás: más resolución exige más datos, más barrido exige un campo de visión mayor, y el enlace de bajada limita cuánto se puede adquirir. La decisión central: ¿qué requisito se relaja cuando el presupuesto de datos no cierra?

📘 **Dónde se aprende** (3 clases): [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md); [B57-C24 · Diseño de una carga útil de observación terrestre](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md); [B81-C10 · Funciones objetivo de diseño de trayectorias](../programa/clases/B81/B81-C10-funciones-objetivo-de-diseno-de-trayectorias/CLASE.md).

### Carga visual

- La carga visual es el número de elementos que compiten por la atención a la vez.

🎯 **Por qué importa (clase B116-C07):** Un panel que muestra «FC 72» sin decir de cuándo es, o que usa un gris que no se lee, puede ser peor que no tener panel. La decisión central: ¿qué debe mostrar un panel de salud para que quien lo mira sepa qué está pasando, cuán fresco es el dato y a quién atender primero?

📘 **Dónde se aprende** (1 clase): [B116-C07 · Diseño de paneles de monitoreo de salud](../programa/clases/B116/B116-C07-diseno-de-paneles-de-monitoreo-de-salud/CLASE.md).

### Cargas consistentes

- Las cargas consistentes de `q` uniforme son `[qL/2, qL²/12, qL/2, −qL²/12]`.

🎯 **Por qué importa (clase B84-C28):** Una restricción de menos deja la matriz singular; una de más introduce tensiones falsas; una carga mal repartida cambia la flecha 1,25 %: son los errores más frecuentes en los modelos. La decisión central: ¿está el modelo bien restringido y cargado y cómo lo demuestro?

📘 **Dónde se aprende** (1 clase): [B84-C28 · Condiciones de contorno y cargas en modelos de elementos finitos](../programa/clases/B84/B84-C28-condiciones-de-contorno-y-cargas-en-modelos-de-elementos-finitos/CLASE.md).

### Carrera

- La carrera es un resultado que depende del intercalado.

🎯 **Por qué importa (clase B88-C27):** Una carrera no falla siempre: falla de vez en cuando y no se reproduce. La decisión central: ¿qué mecanismo garantiza que el acceso a un dato compartido sea exclusivo y que un buffer no se desborde ni se vacíe?

📘 **Dónde se aprende** (1 clase): [B88-C27 · Exclusión mutua y semáforos](../programa/clases/B88/B88-C27-exclusion-mutua-y-semaforos/CLASE.md).

### Carta

- Una carta son coordenadas locales.

💡 **Cómo se explica en la clase [B39-C01](../programa/clases/B39/B39-C01-variedades-tensor-metrico-y-geometria-diferencial/CLASE.md):**
- Con la carta `x = tan(θ/2) cos φ`, `y = tan(θ/2) sin φ`, la métrica transformada por diferencias finitas da `9,4901248` en la diagonal y `3,7 × 10⁻¹⁰` fuera de ella; la fórmula `4a²/(1 + r²)²` da `9,4901248`.
- La longitud del paralelo en la nueva carta es `10,574236256`, igual que antes.
- ⚠️ **Error frecuente:** Usar la carta en el polo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Sin métrica no hay distancias ni tiempo propio. La decisión central: ¿qué representa la métrica y qué cantidades no cambian al cambiar de coordenadas?

📘 **Dónde se aprende** (1 clase): [B39-C01 · Variedades, tensor métrico y geometría diferencial](../programa/clases/B39/B39-C01-variedades-tensor-metrico-y-geometria-diferencial/CLASE.md).

### Carta de respuesta

- Una carta de respuesta es el documento que acompaña la versión revisada: reproduce cada comentario y señala qué decidiste, qué hiciste y dónde.

💡 **Cómo se explica en la clase [B20-C03](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md):**
- El registro (la carta de respuesta y la versión con cambios marcados) es lo que permite al editor y a los árbitros comprobar rápido qué cambió.
- D -->|"revisión solicitada"| E["Autores: análisis + carta de respuesta + versión marcada"]
- 🎯 **Por qué importa:** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Carta de Smith

- La carta de Smith representa `Γ` en el plano complejo.

🎯 **Por qué importa (clase B49-C02):** Una antena desadaptada devuelve potencia y empeora la sensibilidad. La decisión central: ¿cuánta potencia se refleja y cómo se adapta con un tramo de línea?

📘 **Dónde se aprende** (1 clase): [B49-C02 · Adaptación de impedancias y líneas de transmisión en antenas](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md).

### Carta X-barra

- La carta X-barra señala si `|x̄ − μ| > 3σ/√n`.

🎯 **Por qué importa (clase B84-C35):** Un proceso con `Cpk` de 1,33 puede desplazarse 1σ sin dejar piezas fuera de tolerancia durante semanas si solo se inspecciona el producto; la carta lo detecta en pocos subgrupos. La decisión central: ¿qué carta detecta antes un desplazamiento del proceso y qué capacidad tiene el proceso antes y después?

📘 **Dónde se aprende** (1 clase): [B84-C35 · Control de procesos de fabricación y calidad](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md).

### Cascada

- La cascada es la propagación de fallas.
- Una cascada es el conjunto de reenvíos que parte de una publicación.
- La cascada se multiplica por generaciones.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B31-C13](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md):**
- El máximo de la cascada se retrasa `85 g/cm²` por década de energía y es menos profundo para núcleos pesados; esa diferencia sirve para inferir la masa del primario.
- 🎯 **Por qué importa:** La energía y la composición de un rayo cósmico se infieren de la forma de su cascada, y el fondo de microondas limita la energía que llega. La decisión central: ¿qué profundidad y tamaño tiene una cascada y a qué energía aparece un corte?

📘 **Dónde se aprende** (4 clases): [B31-C13 · Rayos cósmicos y cascadas](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md); [B35-C09 · Turbulencia en plasmas y MHD](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md); [B119-C16 · Protección de infraestructura crítica](../programa/clases/B119/B119-C16-proteccion-de-infraestructura-critica/CLASE.md); [B130-C04 · Divulgación científica en redes sociales](../programa/clases/B130/B130-C04-divulgacion-cientifica-en-redes-sociales/CLASE.md).

### Cascada de Friis

- La cascada de Friis: `T = T₁ + T₂/G₁ + T₃/(G₁G₂)`.

💡 **Cómo se explica en la clase [B46-C06](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md):**
- L["LNA, mezclador, FI"] --> F["cascada de Friis"]
- 🎯 **Por qué importa:** La señal de una fuente astronómica es mucho menor que el ruido, y solo el promedio la hace visible. La decisión central: ¿cuánto tiempo y ancho de banda se necesitan para alcanzar una sensibilidad dada?

📘 **Dónde se aprende** (1 clase): [B46-C06 · Ruido de sistema y radiometría](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md).

### Cascarón esférico

- Un cascarón esférico es la región entre dos esferas concéntricas.

🎯 **Por qué importa (clase B56-C09):** Un océano global bajo el hielo es un candidato a hábitat, protegido de la radiación y del vacío. Saber cuán profundo es y qué presión soporta fija qué sondas podrían llegar y qué ambientes existen.

📘 **Dónde se aprende** (1 clase): [B56-C09 · Océanos de Europa](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md).

### Caso ambiguo

- El caso ambiguo es el LLA, que puede tener cero, una o dos soluciones.

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- La ley de senos es más corta con ALA y LLA, pero exige vigilar el caso ambiguo.
- ⚠️ **Error frecuente:** Ignorar el caso ambiguo. Se corrige con los ejercicios 6, 7 y 10.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

📘 **Dónde se aprende** (1 clase): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### Caso analítico

- Un caso analítico es uno cuyo resultado se deduce con matemáticas, sin la función.

💡 **Cómo se explica en la clase [B07-C17](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md):**
- Para el volumen: caso analítico (radio 1), borde (radio 0 da 0) y propiedad de escala (duplicar el radio multiplica el volumen por 8), parametrizada con cuatro radios (0,5; 1; 6371; 0,001).
- 🎯 **Por qué importa:** Una función matemática puede dar el resultado correcto en el único caso que probaste y estar mal en los demás. Y es fácil escribir una prueba que no puede fallar: la que compara la función contra sí misma o contra un caso donde el error se esconde.

📘 **Dónde se aprende** (1 clase): [B07-C17 · Pruebas de funciones matemáticas](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md).

### Caso borde

- Un caso borde es una entrada extrema o inusual (lista vacía, un solo elemento) donde los errores suelen esconderse.
- Un caso borde es una entrada extrema (0, negativos, `nan`).

🎯 **Por qué importa (clase B07-C01):** En astronomía casi todo resultado pasa por un procedimiento repetible: reducir imágenes, ajustar una órbita, buscar el máximo de una curva de luz. Si no puedes describir el procedimiento con precisión, no puedes ejecutarlo en un computador ni dárselo a otra persona para que lo repita.

📘 **Dónde se aprende** (2 clases): [B07-C01 · Pensamiento algorítmico](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md); [B07-C17 · Pruebas de funciones matemáticas](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md).

### Caso caliente

- El caso caliente suma Sol, albedo e infrarrojo; el caso frío es el eclipse.

💡 **Cómo se explica en la clase [B85-C01](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md):**
- Subir la absortividad a `α = 0,9` lleva el caso caliente a `323,01 K` (`+60,76 K`); subir la disipación a `200 W` lleva el caso frío a `228,06 K`.
- Una esfera de `0,5 m` de radio a `500 km` de altura, con `α = 0,30`, `ε = 0,80` y `50 W` de disipación interna, alcanza `262,26 K` en el caso caliente y `201,62 K` en eclipse.
- 🎯 **Por qué importa:** Las temperaturas de una nave no se miden primero: se predicen con un balance de energía. Un error de 30 K en el equilibrio decide si una batería sobrevive.

📘 **Dónde se aprende** (1 clase): [B85-C01 · Balance radiativo de satélite](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md).

### Caso científico

- El caso científico argumenta por qué responderla aporta conocimiento.

🎯 **Por qué importa (clase B83-C01):** Un equipo sabe que quiere «mirar la costa» pero no cuánto debe resolver ni qué objetivo merece el presupuesto. La decisión central: ¿qué requisito de medición se deduce de la pregunta científica y qué objetivo conviene perseguir primero?

📘 **Dónde se aprende** (1 clase): [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md).

### Caso extremo

- El caso extremo es el de menor o mayor temperatura de diseño.

💡 **Cómo se explica en la clase [B85-C26](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md):**
- Para un análisis fiable se usa un paso menor que `τ/10` en explícito, o implícito con control del error; el caso extremo se busca variando duración y fase del eclipse y tiempos de arranque.
- 🎯 **Por qué importa:** El peor caso de temperatura casi nunca es el de régimen. La decisión central: ¿qué paso de tiempo y qué esquema dan una respuesta fiable y cuál es la temperatura extrema en el eclipse o en el arranque?

📘 **Dónde se aprende** (1 clase): [B85-C26 · Análisis térmico transitorio y casos extremos](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md).

### Caso frío

- El caso caliente suma Sol, albedo e infrarrojo; el caso frío es el eclipse.

💡 **Cómo se explica en la clase [B85-C01](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md):**
- Subir la absortividad a `α = 0,9` lleva el caso caliente a `323,01 K` (`+60,76 K`); subir la disipación a `200 W` lleva el caso frío a `228,06 K`.
- Paso 3 · Caso frío. `Q = 185,5 + 50 = 235,5 W`;
- 🎯 **Por qué importa:** Las temperaturas de una nave no se miden primero: se predicen con un balance de energía. Un error de 30 K en el equilibrio decide si una batería sobrevive.

📘 **Dónde se aprende** (1 clase): [B85-C01 · Balance radiativo de satélite](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md).

### Caso frontera

- Un caso frontera es un dato igual o muy cercano al umbral.

🎯 **Por qué importa (clase B07-C04):** Toda clasificación astronómica es una decisión sobre un dato: ¿esta señal supera el ruido?, ¿esta estrella es más brillante que el umbral?, ¿esta imagen está saturada? Una decisión mal escrita no falla ruidosamente: clasifica mal en silencio, justo en los casos frontera, que son los que importan.

📘 **Dónde se aprende** (1 clase): [B07-C04 · Condicionales y decisiones](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md).

### Caso límite

- Un caso límite es uno donde las definiciones discrepan.
- Un caso límite es un valor justo en el borde.

🎯 **Por qué importa (clase B56-C01):** Una misión que busca vida necesita saber qué buscar y qué contará como hallazgo. Si el criterio es vago, cualquier resultado se puede discutir; si es demasiado estrecho, se pasa por alto lo que no se parece a la vida terrestre.

📘 **Dónde se aprende** (2 clases): [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md); [B118-C24 · Directrices técnicas de mitigación de desechos (IADC, ISO 24113)](../programa/clases/B118/B118-C24-directrices-tecnicas-de-mitigacion-de-desechos-iadc-iso-24113/CLASE.md).

### Caso más desfavorable

- Un caso más desfavorable combina los extremos (corriente máxima, largo máximo).

🎯 **Por qué importa (clase B83-C08):** La mayoría de los fallos de integración aparecen en las interfaces: un conector mal definido, una tensión fuera de rango o una tasa de datos insuficiente. La decisión central: ¿cada interfaz cumple en su caso más desfavorable, con margen, antes de construir?

📘 **Dónde se aprende** (1 clase): [B83-C08 · Interfaz entre subsistemas](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md).

### Caso simétrico

- El caso simétrico es aquel en que ambas visuales forman el mismo ángulo con la base.

🎯 **Por qué importa (clase B04-C20):** Las distancias a las estrellas más cercanas se obtienen con un triángulo (el paralaje de C07): la base es la órbita de la Tierra y el ángulo es lo que cambia la dirección de la estrella.

📘 **Dónde se aprende** (1 clase): [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md).

### Caso simple

- Un caso simple (oscilador armónico `x'' = −ω²x`, solución `cos ωt`) es un banco de pruebas de solución obvia.

🎯 **Por qué importa (clase B23-C03):** Un integrador de órbitas puede conservar la energía, ser reversible e invariante ante rotaciones y aun así describir un Sol con otra masa o una ley de fuerza distinta. Para detectarlo necesitas una referencia con valores: «tras exactamente un período, el planeta vuelve a su punto de partida».

📘 **Dónde se aprende** (1 clase): [B23-C03 · Casos analíticos de validación](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md).

### Casquete esférico

- El casquete esférico es el volumen entre el plano y la esfera.
- El casquete esférico es la forma del suelo.

🎯 **Por qué importa (clase B43-C04):** El desbaste fija el radio de curvatura; los errores de esta etapa se pagan en horas de pulido. La decisión central: ¿cuánta profundidad hay que excavar, cómo se mide el radio y cuánto abrasivo se necesita en cada etapa?

📘 **Dónde se aprende** (2 clases): [B43-C04 · Fabricación y desbaste de espejos](../programa/clases/B43/B43-C04-fabricacion-y-desbaste-de-espejos/CLASE.md); [B61-C02 · Cráteres simples: morfología y formación](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md).

### Casquete polar

- El casquete polar es la zona `abs(z) > 2/3`.

🎯 **Por qué importa (clase B40-C12):** Sin una pixelización de área igual, el ruido y las estadísticas dependen de la posición. La decisión central: ¿cuántos pixeles, de qué tamaño, y cómo se cuenta la fracción de cielo de una máscara?

📘 **Dónde se aprende** (1 clase): [B40-C12 · Análisis de mapas del CMB: pixelización esférica y máscaras](../programa/clases/B40/B40-C12-analisis-de-mapas-del-cmb-pixelizacion-esferica-y-mascaras/CLASE.md).

### Cassegrain clásico

- El Cassegrain clásico (primario parabólico, secundario hiperbólico).
- El Cassegrain clásico tiene primario parabólico y secundario hiperbólico convexo.

💡 **Cómo se explica en la clase [B41-C17](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md):**
- La coma del paraboloide f/10 con la misma focal es `10,908 µm`: el Cassegrain clásico (`10,955`) coincide (razón `1,004`).
- 🎯 **Por qué importa:** Dos espejos permiten un tubo corto y focal larga, y distintos diseños eligen qué aberración corregir. La decisión central: ¿qué diseño corrige la coma y a qué costo?

📘 **Dónde se aprende** (2 clases): [B41-C17 · Telescopios Cassegrain y derivados](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md); [B43-C02 · Selección de geometría instrumental](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md).

### Catálogo

- Un catálogo es una lista de objetos con identificador, coordenadas y propiedades medidas.
- Un catálogo es una tabla de objetos con procedencia (instrumento, época, versión, criterios de selección).
- Un catálogo es una lista de objetos con propiedades medidas.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C06](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md):**
- Una misma estrella puede tener un nombre tradicional, una letra griega con la constelación (por ejemplo, «α Cru» para la más brillante de la Cruz) y un número de catálogo.
- Las letras griegas y los números se asignan por reglas de cada catálogo (no consultadas en detalle aquí).
- ⚠️ **Error frecuente:** Confundir rango de numeración con tamaño del catálogo. Ejercicio 8.
- 🎯 **Por qué importa:** Dos personas dicen «la estrella roja de la Cruz del Sur» y creen hablar de lo mismo; un programa de telescopio pide «HIP 12345». Sin un lenguaje común no puedes repetir una observación ni compartirla.

📘 **Dónde se aprende** (5 clases): [B08-C06 · Constelaciones y catálogos estelares](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md); [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md); [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md); [B25-C19 · Catálogos y sesgos de selección](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md); [B118-C02 · Catálogos de objetos espaciales](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md).

### Catálogo aleatorio

- Un catálogo aleatorio es el de Poisson usado como referencia.
- Un catálogo aleatorio reproduce la geometría sin agrupación.

💡 **Cómo se explica en la clase [B25-C18](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md):**
- Los catálogos reales requieren un catálogo aleatorio con la misma máscara y selección, corrección de las distorsiones por velocidades peculiares (la distancia sale del corrimiento al rojo) y estimadores con menor varianza.
- 🎯 **Por qué importa:** Las galaxias no se reparten al azar: forman filamentos, paredes, cúmulos y vacíos, la llamada red cósmica. La forma en que se agrupan guarda información de la materia oscura y de la historia del universo.

📘 **Dónde se aprende** (2 clases): [B25-C18 · Estructura cósmica a gran escala](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md); [B36-C03 · Funciones de correlación de galaxias](../programa/clases/B36/B36-C03-funciones-de-correlacion-de-galaxias/CLASE.md).

### Catálogo estelar

- Un catálogo estelar es una lista de estrellas con sus posiciones.

🎯 **Por qué importa (clase B02-C03):** Un modelo geométrico responde a «¿qué figura reproduce estos movimientos?». Es una forma nueva de preguntar frente a la regla puramente numérica.

📘 **Dónde se aprende** (1 clase): [B02-C03 · Astronomía griega y helenística](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md).

### Catálogo JPL

- El catálogo JPL lista frecuencias, incertidumbres e intensidades.

💡 **Cómo se explica en la clase [B55-C09](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md):**
- DC --> CAT["comparación con catálogo JPL"]
- Las ocho primeras líneas de rotación del CO del catálogo JPL (etiqueta 28001, versión 4) con `B = 57635,968 MHz`, y las tres componentes hiperfinas de la transición `J = 1–0` del HCN (etiqueta 27001, versión 2).
- 🎯 **Por qué importa:** Las moléculas del espacio frío se detectan casi siempre por sus líneas de rotación en milimétrico y submilimétrico. Para identificar una línea hay que saber de dónde sale su frecuencia, qué fracción de niveles está poblada y cómo corregirla por la velocidad de la nube.

📘 **Dónde se aprende** (1 clase): [B55-C09 · Espectros moleculares de radio](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md).

### Catastrófica

- Una colisión es catastrófica si destruye al objetivo; el umbral habitual se expresa como energía por masa del objetivo.

🎯 **Por qué importa (clase B118-C09):** La directriz 5 de la COPUOS dice que la mayor parte de los desechos catalogados proviene de fragmentaciones; entender cuántos fragmentos produce un evento y de qué tamaño es la base de los escenarios futuros. La decisión central: ¿cuántos fragmentos relevantes genera un evento y cuándo es «catastrófico»?

📘 **Dónde se aprende** (1 clase): [B118-C09 · Generación de desechos](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md).

### Categoría

- Cota superior: valor que, con confianza `CL`, no es menor que la densidad verdadera. Categoría: nivel de requisitos de la misión (I a V).
- La categoría (I a V) refleja el interés científico del cuerpo y el riesgo de contaminación.
- La categoría (baja, media, alta) agrupa el total.

💡 **Cómo se explica en la clase [B56-C18](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md):**
- Para mundos helados en categoría II o III: probabilidad de inoculación `< 1 × 10⁻⁴` en 1000 años, es decir una media anual de `10⁻⁷`.
- Para categoría III a Marte: probabilidad de impacto `≤ 10⁻²` en los primeros 20 años y `≤ 5 × 10⁻²` de 20 a 50 años, o cumplir la limpieza de IVa (C17).
- ⚠️ **Error frecuente:** Olvidar la categoría V del retorno. Se corrige con el ejercicio 3.
- 🎯 **Por qué importa:** La política protege los otros mundos de la contaminación (para no estropear la búsqueda de vida) y la Tierra del material devuelto. Saber en qué categoría cae una misión determina su documentación, su limpieza y sus restricciones.

📘 **Dónde se aprende** (3 clases): [B56-C18 · Protección planetaria COSPAR](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md); [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md); [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Categoría de peor caso

- La categoría de peor caso usa el máximo de `Pc` en el barrido.

🎯 **Por qué importa (clase B118-C20):** Una decisión de maniobra se justifica meses después: ¿con qué datos, qué método y qué sensibilidad? La decisión central: ¿qué debe contener un registro para que el resultado sea reproducible, y cómo se evita decidir con un único número?

📘 **Dónde se aprende** (1 clase): [B118-C20 · Evaluación de riesgo de conjunción documentada](../programa/clases/B118/B118-C20-evaluacion-de-riesgo-de-conjuncion-documentada/CLASE.md).

### Categoría V

- La categoría V se añade a las misiones que traen muestras a la Tierra; es restringida o no restringida.
- La Categoría V agrupa las misiones de retorno a la Tierra. «Retorno restringido» es la subcategoría de mayor preocupación.

💡 **Cómo se explica en la clase [B56-C18](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md):**
- *Descripción textual:* según el cuerpo, la categoría es fija (I, II) o depende del tipo de misión (III o IV para Marte y mundos helados); el retorno de muestras añade la categoría V.
- ⚠️ **Error frecuente:** Olvidar la categoría V del retorno. Se corrige con el ejercicio 3.
- 🎯 **Por qué importa:** La política protege los otros mundos de la contaminación (para no estropear la búsqueda de vida) y la Tierra del material devuelto. Saber en qué categoría cae una misión determina su documentación, su limpieza y sus restricciones.

📘 **Dónde se aprende** (2 clases): [B56-C18 · Protección planetaria COSPAR](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md); [B63-C04 · Misiones de retorno de muestras: salvaguardas históricas y regulatorias](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md).

### Categorías

- Las categorías (aquí Inferido, Indicado, Medido) expresan la confianza en la estimación.

🎯 **Por qué importa (clase B67-C04):** Decir «hay 330 kt» sin intervalo ni categoría invita a decisiones equivocadas. La decisión central: ¿cuánto del recurso se puede llamar reserva, y qué falta para subir de categoría?

📘 **Dónde se aprende** (1 clase): [B67-C04 · Estimación de reservas y categorías de recursos](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md).

### Catenaria invertida

- Una catenaria invertida es un perfil de cúpula que trabaja en compresión pura.

💡 **Cómo se explica en la clase [B59-C13](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md):**
- Una cúpula hemisférica no se puede imprimir entera por capas horizontales; se usa un perfil más apuntado (catenaria invertida) o apoyo temporal.
- 🎯 **Por qué importa:** Una capa más fina da mejor forma pero más tiempo; y una cúpula tiene una zona alta que no se puede imprimir sin apoyo. La decisión central: ¿qué grosor de capa y qué perfil de cúpula hacen viable la impresión?

📘 **Dónde se aprende** (1 clase): [B59-C13 · Impresión 3D extraterrestre](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md).

### Cateto adyacente

- En un triángulo rectángulo, el cateto opuesto a un ángulo `θ` es el lado frente a él, el cateto adyacente es el lado que lo forma junto con la hipotenusa, y la hipotenusa es el lado mayor, frente al ángulo recto.

💡 **Cómo se explica en la clase [B03-C18](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md):**
- D["Distancia d (cateto adyacente)"] --> T
- 🎯 **Por qué importa:** El Sol y la Luna se ven en el cielo con tamaños angulares muy parecidos, de alrededor de medio grado. ¿Es casualidad que midan lo mismo en el cielo siendo tan distintos?

📘 **Dónde se aprende** (1 clase): [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md).

### Cateto opuesto

- En un triángulo rectángulo, el cateto opuesto a un ángulo `θ` es el lado frente a él, el cateto adyacente es el lado que lo forma junto con la hipotenusa, y la hipotenusa es el lado mayor, frente al ángulo recto.

💡 **Cómo se explica en la clase [B03-C18](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md):**
- R["Radio r (cateto opuesto)"] --> T["tan(θ/2) = r / d"]
- Paso 1 · triángulo. Cateto opuesto `r = 1 737,4 km`; adyacente `d = 378 000 km`.
- ⚠️ **Error frecuente:** Confundir cateto opuesto y adyacente. Ejercicio 1.
- 🎯 **Por qué importa:** El Sol y la Luna se ven en el cielo con tamaños angulares muy parecidos, de alrededor de medio grado. ¿Es casualidad que midan lo mismo en el cielo siendo tan distintos?

📘 **Dónde se aprende** (1 clase): [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md).

### Catetos

- Un triángulo rectángulo tiene un ángulo de 90°; el lado opuesto a él es la hipotenusa y los otros dos son los catetos.

💡 **Cómo se explica en la clase [B04-C07](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md):**
- Para los catetos `a` (opuesto a `θ`) y `b` (adyacente) y la hipotenusa `c`: `sen θ = a/c`, `cos θ = b/c`, `tan θ = a/b`, y `c² = a² + b²`.
- Si conoces los dos catetos y buscas el ángulo: `θ = arctan(a/b)`.
- 🎯 **Por qué importa:** Nadie puede llevar una cinta métrica a una estrella. Pero sí se puede observar la misma estrella desde dos puntos separados una distancia conocida y medir cuánto cambia su dirección.

📘 **Dónde se aprende** (1 clase): [B04-C07 · Triángulos y distancias angulares](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md).

### Catión

- Un ion es un átomo o grupo con carga neta: un catión (positivo) pierde electrones; un anión (negativo) los gana.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- Pregunta: un par catión +1 / anión −1 a 0,30 nm (distancia sintética), ¿resiste la agitación térmica a 176 K, la temperatura del eutéctico NH₃–H₂O (S1)?
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Caudal

- El caudal `ṁ = P_th/(c_p ΔT)` es lo que esa potencia puede calentar.

💡 **Cómo se explica en la clase [B78-C13](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md):**
- *Descripción textual:* la irradiancia y el área dan la potencia térmica; con la temperatura fija el caudal; la temperatura y la masa molar fijan el escape; caudal y escape dan el empuje y el balance exige que la potencia del chorro no supere la térmica.
- Paso 2 · Caudal. `76 220/(14 435 × 2200) = 2,400 g/s`.
- 🎯 **Por qué importa:** La energía llega por la óptica y el propelente solo la transporta; el escape depende de la temperatura que resistan los materiales y de la masa molar. La decisión central: ¿qué empuje e `Isp` da un colector de área dada y cómo se compara con un propulsor eléctrico alimentado con la misma potencia?

📘 **Dónde se aprende** (1 clase): [B78-C13 · Propulsión solar térmica](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md).

### Caudal másico

- El caudal másico `ṁ` es la masa de propelente expulsada por segundo.

🎯 **Por qué importa (clase B78-C01):** Dos motores con el mismo empuje pueden gastar propelente a ritmos muy distintos, y dos con el mismo consumo pueden empujar muy distinto según la presión ambiente. La decisión central: ¿qué mide el impulso específico, qué no mide, y por qué el mismo motor tiene un `Isp` distinto en el mar y en el vacío?

📘 **Dónde se aprende** (1 clase): [B78-C01 · Empuje e impulso específico](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md).

### Caudal Q

- Depurador: equipo que retira CO₂ del aire (tamices moleculares en la página consultada). Caudal `Q`: volumen de aire procesado por segundo.

🎯 **Por qué importa (clase B106-C04):** Una cabina cerrada acumula el CO₂ de la tripulación hasta que un depurador lo retira. Si el depurador es insuficiente o falla, hay un tiempo finito antes de pasar los límites.

📘 **Dónde se aprende** (1 clase): [B106-C04 · Control de dióxido de carbono](../programa/clases/B106/B106-C04-control-de-dioxido-de-carbono/CLASE.md).

### Causa común

- Una causa común es un evento que falla varias barreras a la vez.
- La causa común es una falla que afecta a varias unidades a la vez.
- Redundancia: unidad de respaldo. Causa común: falla que afecta a ambas unidades.

💡 **Cómo se explica en la clase [B33-C09](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md):**
- La cuarta unidad aporta 1,9 puntos; con 30 % de causa común, la ganancia se aplana en torno a 0,90: la diversidad importa más que la cantidad.
- *Descripción textual:* la probabilidad de servicio depende de `n` y de la causa común; la disponibilidad depende de fallas y reparación.
- ⚠️ **Error frecuente:** Ignorar la causa común. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una unidad adicional mejora menos que la anterior y las fallas comunes limitan la ganancia. La decisión central: ¿cuántas unidades de respaldo valen la pena?

📘 **Dónde se aprende** (4 clases): [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B63-C04 · Misiones de retorno de muestras: salvaguardas históricas y regulatorias](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md); [B86-C11 · Redundancia eléctrica](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md).

### Causa común (β)

- Paralelo: basta uno. Causa común (β): fracción de la indisponibilidad que afecta a todas las unidades.
- Redundancia k de n: funciona si funcionan `k` de `n`. Causa común (β): fracción de fallas que afecta a todos.

💡 **Cómo se explica en la clase [B96-C23](../programa/clases/B96/B96-C23-continuidad-y-redundancia-de-las-operaciones-terrestres/CLASE.md):**
- Con causa común `β = 0,10`: `P = β(1 − A) + ((1 − β)(1 − A))ᴺ`: 1,104×10⁻³ (2) y 1,020×10⁻³ (3).
- El Monte Carlo de 10⁶ instantes con N = 2 da 95 pérdidas frente a 103,9 esperadas; con causa común, 1 046 frente a 1 103,5.
- ⚠️ **Error frecuente:** Olvidar la causa común. Añade `β` (8.3)
- 🎯 **Por qué importa:** Redundancia no es solo tener más estaciones: si comparten la causa de falla (red, energía, software) el beneficio desaparece. La decisión central: ¿cuántas estaciones y qué independencia hacen falta para que la probabilidad de perder un contacto sea aceptable?

📘 **Dónde se aprende** (2 clases): [B96-C23 · Continuidad y redundancia de las operaciones terrestres](../programa/clases/B96/B96-C23-continuidad-y-redundancia-de-las-operaciones-terrestres/CLASE.md); [B106-C18 · Fiabilidad y redundancia](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md).

### Causa raíz

- Severidad: gravedad del efecto (S1 la mayor). Causa raíz: origen de la falla.

💡 **Cómo se explica en la clase [B90-C17](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md):**
- S2: analizar la causa raíz antes de continuar (primera vez) o detener y corregir (repetida).
- A06 y A11 (funcionales recurrentes) exigen causa raíz.
- 🎯 **Por qué importa:** Una falla única en 500 horas de ensayo no demuestra que el equipo sea confiable: solo acota la tasa de fallas. Y una anomalía mal registrada se pierde.

📘 **Dónde se aprende** (1 clase): [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md).

### Causal

- Un filtro es causal si `y[n]` solo usa datos presentes y pasados.

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- El filtro de un polo es barato y causal, pero retrasa.
- ⚠️ **Error frecuente:** Ignorar el retardo de un filtro causal. Se corrige con los ejercicios 4 y 10.
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.

📘 **Dónde se aprende** (1 clase): [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### Causalidad

- La causalidad es `c_s ≤ c`.
- La causalidad es el nexo entre un objeto y el daño.

💡 **Cómo se explica en la clase [B27-C04](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md):**
- La causalidad (`c_s < c`) descarta EOS demasiado rígidas: en una variante con `Γ₂ = 3`, el resultado del barrido mostraba `c_s > c` y se descartó.
- *Descripción textual:* cada EOS genera una familia TOV, de la que se leen `M_max` y `R_{1,4}`; se comprueban las dos restricciones y la causalidad.
- ⚠️ **Error frecuente:** Olvidar la causalidad. Se corrige con la sección 8.5 y el ejercicio 8.
- 🎯 **Por qué importa:** Las estrellas de neutrones son el único laboratorio de materia más allá de la densidad nuclear. Su EOS no se conoce con precisión; las medidas de masa máxima y de radio la acotan.

📘 **Dónde se aprende** (2 clases): [B27-C04 · Ecuación de estado nuclear](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md); [B123-C02 · Causalidad y atribución jurídica del daño](../programa/clases/B123/B123-C02-causalidad-y-atribucion-juridica-del-dano/CLASE.md).

### Causalidad de Granger

- La causalidad de Granger pregunta si los retardos de `x` mejoran la predicción de `y` más allá de sus propios retardos; se contrasta con una razón de F entre el modelo restringido y el completo (S2 menciona la prueba con Wald o F).

💡 **Cómo se explica en la clase [B15-C21](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir causalidad de Granger con causa física. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** El índice Kp de actividad geomagnética se publica en intervalos de 3 horas y refleja las perturbaciones del campo magnético terrestre (S1). Un pronosticador quiere saber cuánto y con qué retardo responde ese índice a una variable del viento solar.

📘 **Dónde se aprende** (1 clase): [B15-C21 · Series temporales multivariadas y regresión dinámica](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md).

### CAVI

- El campo medio (*mean field*) exige que `q` se factorice en factores independientes, `q(θ) = Π q_i(θ_i)`. CAVI (ascenso coordenado) actualiza un factor por vez manteniendo los demás fijos.

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- CAVI converge a factores normales con media exacta y varianza `1/Λ_ii = 1 − r²`, es decir, desviación `√(1 − r²)`.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.

📘 **Dónde se aprende** (1 clase): [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### Cavidad

- Una cavidad es un recinto cuya radiación interna se aproxima a la de un cuerpo negro.

🎯 **Por qué importa (clase B85-C04):** La mitad del control térmico es elegir cuánto emite o absorbe cada superficie. La decisión central: ¿cuánto calor intercambian dos superficies y cómo lo cambia poner una emisividad baja entre ellas?

📘 **Dónde se aprende** (1 clase): [B85-C04 · Radiación térmica de superficies](../programa/clases/B85/B85-C04-radiacion-termica-de-superficies/CLASE.md).

### CBE

- La CBE es la mejor estimación actual; la MEV, la masa máxima esperada, que añade el crecimiento por madurez.

💡 **Cómo se explica en la clase [B124-C19](../programa/clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md):**
- La CBE total es `355,0` kg y cada componente se infla según su madurez: 5 % heredado, 10 % modificado, 20 % nuevo diseño, 30 % nueva tecnología (ilustrativos).
- C["CBE por componente"] --> M["MEV = CBE (1 + g)"]
- 🎯 **Por qué importa:** Una propuesta pierde puntos cuando algo prometido no tiene sección que lo sostenga o cuando el presupuesto no tiene margen. La decisión central: ¿está todo lo prometido cubierto y cuánta reserva necesita el diseño para ser creíble?

📘 **Dónde se aprende** (1 clase): [B124-C19 · Redacción de propuesta de misión](../programa/clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md).

### CCB

- Una solicitud de cambio (CR) propone un cambio; la CCB la decide tras un análisis de impacto.

💡 **Cómo se explica en la clase [B83-C15](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md):**
- Con las dependencias (ICD y plan de ensayos dependen de los requisitos, el software depende del ICD, el presupuesto de masa depende de la estructura y los requisitos), CR-01 afecta a 4 elementos: clase I, va a la CCB.
- CR-02 afecta a 1 elemento: clase II, puede resolverse con aprobación del responsable y aviso a la CCB.
- 🎯 **Por qué importa:** Si nadie sabe qué versión de qué documento se ensayó, no se puede demostrar nada. La decisión central: ¿la configuración actual es la aprobada, y qué se afecta si apruebo este cambio?

📘 **Dónde se aprende** (1 clase): [B83-C15 · Gestión de configuración](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md).

### CCM

- El rizado es la variación pico a pico en un periodo. CCM es la conducción continua y DCM la discontinua.

💡 **Cómo se explica en la clase [B86-C08](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md):**
- En CCM ideal `D = V_o/V_in = 5/28 = 0,1786`.
- La inductancia crítica es `5,04 µH`, menor que `22 µH`: el convertidor opera en CCM.
- ⚠️ **Error frecuente:** Ignorar CCM/DCM. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un convertidor que reduce la tensión con un interruptor y una bobina puede ser mucho más eficiente que un regulador lineal, pero introduce rizado, ruido y pérdidas de conmutación que hay que dimensionar. La decisión central: ¿qué ciclo de trabajo, bobina y condensador dan `5 V` desde `28 V` con rizado y eficiencia aceptables?

📘 **Dónde se aprende** (1 clase): [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### CDMS

- Un banco de datos espectroscópicos reúne frecuencias, intensidades y niveles con procedencia. CDMS (Cologne Database for Molecular Spectroscopy) y JPL son catálogos de líneas milimétricas y submilimétricas.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- L["datos de laboratorio"] --> J["JPL / CDMS: FREQ, ERR, LGINT, ELO, GUP"]
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.

📘 **Dónde se aprende** (1 clase): [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### CDR

- La CDR revisa que el diseño esté completo (planos, análisis, compras).

💡 **Cómo se explica en la clase [B83-C14](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md):**
- Solo 2 de 3 criterios de CDR del ejemplo se cumplen.
- 🎯 **Por qué importa:** Un ensayo mal preparado destruye hardware o no demuestra nada. La decisión central: ¿cada requisito tiene un método asignado, y cada ensayo está listo (procedimiento, equipo, configuración, personal e instalación) y con un nivel de carga definido?

📘 **Dónde se aprende** (1 clase): [B83-C14 · Revisiones CDR y TRR](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md).

### CDS

- El CDS resta la lectura del reinicio de la lectura de señal.

💡 **Cómo se explica en la clase [B44-C03](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md):**
- Sin CDS el ruido es `40,24 e⁻` (esperado `40,22`); con CDS, `2,85 e⁻` (esperado `√2 × 2 = 2,83`).
- El CDS lo elimina pero suma la lectura dos veces (`√2`).
- ⚠️ **Error frecuente:** Pensar que el CDS elimina todo el ruido. Se corrige con 8.2.
- 🎯 **Por qué importa:** El diseño CMOS cambia el ruido y la geometría de la lectura. La decisión central: ¿qué ruido elimina el CDS y qué artefacto introduce el obturador rodante?

📘 **Dónde se aprende** (1 clase): [B44-C03 · Sensores CMOS](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md).

### CE90

- El CE90 contiene el 90 % de los errores radiales.

💡 **Cómo se explica en la clase [B53-C19](../programa/clases/B53/B53-C19-incertidumbre-en-mapas-planetarios/CLASE.md):**
- El valor `2,146` del CE90 es el de un error circular gaussiano.
- Analogía: tirar dardos con manos temblorosas: el error se compone de varios temblores, y el círculo que contiene nueve de cada diez dardos es el CE90.
- 🎯 **Por qué importa:** Un contorno sin barras de error afirma más de lo que sabe. La decisión central: ¿con qué incertidumbre se conoce una posición y un área en un mapa, y cuándo falla la propagación lineal?

📘 **Dónde se aprende** (1 clase): [B53-C19 · Incertidumbre en mapas planetarios](../programa/clases/B53/B53-C19-incertidumbre-en-mapas-planetarios/CLASE.md).

### Cefeida clásica

- Una cefeida clásica es una supergigante pulsante de periodo de días a meses.

🎯 **Por qué importa (clase B24-C13):** Las cefeidas y otras estrellas pulsantes cumplen que cuanto más largo es el periodo, mayor es la luminosidad. Medir un periodo equivale entonces a conocer la luminosidad intrínseca y, por comparación con el brillo aparente, la distancia.

📘 **Dónde se aprende** (1 clase): [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md).

### Celda

- Una celda es un tramo de longitud `Δx` del dominio; el promedio de celda `q_i` es el valor medio de `q` en ella.

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- Si integras en una celda `[x_{i−½}, x_{i+½}]`, el término del flujo se convierte en la diferencia de flujos en los dos bordes: es la contabilidad de cajas, escrita con símbolos.
- Si el promedio de celda es `q_i^n` en el instante `t_n`, la actualización de volúmenes finitos es
- ⚠️ **Error frecuente:** Usar en una interfaz un flujo distinto para cada celda vecina. Rompe la conservación; se detecta con el residuo del ejercicio 7.
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.

📘 **Dónde se aprende** (1 clase): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md).

### Celda de encabezado

- Una celda de encabezado (`th`) etiqueta filas o columnas de una tabla.

🎯 **Por qué importa (clase B128-C04):** Una imagen sin texto alternativo, una tabla sin encabezados o un enlace «haz clic aquí» no se ven como problema a simple vista pero dejan a una persona sin la información. La decisión central: ¿qué comprobaciones mínimas puedo automatizar y qué debo revisar a mano?

📘 **Dónde se aprende** (1 clase): [B128-C04 · Documentos y contenidos para lectores de pantalla](../programa/clases/B128/B128-C04-documentos-y-contenidos-para-lectores-de-pantalla/CLASE.md).

### Celda de Hadley

- La celda de Hadley es la circulación meridional que lleva aire del ecuador hacia latitudes medias.

💡 **Cómo se explica en la clase [B54-C06](../programa/clases/B54/B54-C06-circulacion-general-planetaria/CLASE.md):**
- *Descripción textual:* la rotación da `f`; con el gradiente de presión resulta el viento geostrófico y con él el número de Rossby; la rotación también da la escala de la celda de Hadley.
- 🎯 **Por qué importa:** La rotación decide si el aire va de los polos al ecuador en una sola celda o se divide en bandas. La pregunta motivadora: ¿cuándo manda la rotación y cuándo no?

📘 **Dónde se aprende** (1 clase): [B54-C06 · Circulación general planetaria](../programa/clases/B54/B54-C06-circulacion-general-planetaria/CLASE.md).

### Celda en serie

- Una celda en serie comparte la corriente con las demás: `N` celdas multiplican la tasa por `N` con la misma corriente.

🎯 **Por qué importa (clase B59-C08):** Un oxidante producido en destino se mide en gramos por hora, pero el diseñador piensa en amperios y vatios. La decisión central: ¿qué corriente y qué potencia exige una tasa de oxígeno dada?

📘 **Dónde se aprende** (1 clase): [B59-C08 · Producción de oxígeno](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md).

### Celdas independientes

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B51-C11](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md):**
- Con `M = 1024` celdas independientes y umbral `|z|² > 6,0`, la probabilidad de que el máximo de ruido lo supere es 0,9212; el Monte Carlo (1500 ensayos) da 0,9093.
- 🎯 **Por qué importa:** Declarar una detección sin umbral estadístico es un riesgo de falsos positivos. La decisión central: ¿qué pico es una señal y cuál es ruido, y con qué precisión se estiman retardo y tasa?

📘 **Dónde se aprende** (1 clase): [B51-C11 · Búsqueda de franjas VLBI: ajuste de retardo y tasa](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md).

### Cénit

- El horizonte es el límite del cielo visible; el cénit, el punto justo encima; el meridiano es la línea imaginaria que une norte, cénit y sur.
- El horizonte local es el círculo máximo que separa la mitad visible de la oculta; el cenit es el punto sobre tu cabeza y el nadir su opuesto.

💡 **Cómo se explica en la clase [B08-C02](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md):**
- La colatitud es `90° − |φ|`: la distancia angular entre el polo visible y el cenit.
- 🎯 **Por qué importa:** Alguien en Punta Arenas ve girar algunas estrellas sin ponerse jamás; alguien en el valle del Elqui las ve rozar el horizonte, y alguien en el hemisferio norte no las ve nunca. Entender por qué evita comprar un telescopio para un objeto que no sale en tu cielo.

📘 **Dónde se aprende** (2 clases): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B08-C02 · Esfera celeste y horizonte local](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md).

### Cenital

- El pase cenital pasa justo sobre la estación y es el más largo.

💡 **Cómo se explica en la clase [B83-C03](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md):**
- Un pase cenital con elevación mínima de 10° tiene un semiángulo central `λ = arccos(R cos ε/(R+h)) − ε` y dura `2λ/n`: 7,95 min si la Tierra no girara.
- *Descripción textual:* las fases y modos del CONOPS definen la órbita y la estación; la simulación de visibilidad da pases, duraciones y huecos, de los que sale el tiempo de enlace diario; la cota analítica del pase cenital sirve de comprobación.
- ⚠️ **Error frecuente:** Tratar la cota cenital como duración típica. Es un máximo; los pases típicos son más cortos
- 🎯 **Por qué importa:** Los requisitos de datos, energía y operaciones dependen de cuántas veces al día se puede hablar con el satélite y por cuánto tiempo. La decisión central: ¿cuánto contacto real ofrece la órbita y cómo se reparte en las fases de la misión?

📘 **Dónde se aprende** (1 clase): [B83-C03 · Concepto de operaciones CONOPS](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md).

### Censura

- La censura es no haber alcanzado el criterio al terminar.

💡 **Cómo se explica en la clase [B107-C10](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md):**
- Con la cohorte sintética de 40, KM coincide con el conteo directo (sin censura antes del final del seguimiento) y difiere de la teórica hasta 0,08 por tamaño muestral.
- T["tiempo al criterio, con censura"] --> K["Kaplan-Meier S(t)"]
- ⚠️ **Error frecuente:** Ignorar la censura. Subestima el tiempo (8.3).
- 🎯 **Por qué importa:** Los fragmentos consultados describen el entrenamiento en la ISS (Loehr et al., 2015) y baterías funcionales con medidas fisiológicas (Mulavara et al., 2018), pero un seguimiento necesita indicadores bien definidos y bien calculados.

📘 **Dónde se aprende** (1 clase): [B107-C10 · Indicadores de rehabilitación y seguimiento](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md).

### Centinela

- Un centinela es un valor reservado (como `-99`) que codifica «sin dato».
- BINTABLE: tabla binaria. Centinela: valor que marca pixeles sin dato.

💡 **Cómo se explica en la clase [B14-C08](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md):**
- El ejemplo conductor es una bitácora sintética de 200 filas con defectos de cantidad conocida: 7 valores centinela `-99`, 5 valores ausentes, 4 filas duplicadas, 3 atípicos de +5 magnitudes y nombres con mayúsculas y espacios inconsistentes.
- 🎯 **Por qué importa:** Una bitácora de observación real tiene errores: alguien escribió `-99` donde faltaba un dato, el mismo objeto aparece con tres grafías, una fila se copió dos veces, un valor tiene un dígito de más. Si calculas una media sin limpiar, el resultado es otro número.

📘 **Dónde se aprende** (2 clases): [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md); [B40-C14 · Productos de datos de Planck y misiones del CMB](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md).

### Centrado de articulaciones

- Autocolisión: holgura negativa entre eslabones no adyacentes. Centrado de articulaciones: criterio `Σ (qᵢ/límite)²`.

🎯 **Por qué importa (clase B101-C04):** Una solución de cinemática inversa que exceda un tope o atraviese el propio brazo no sirve. La decisión central: ¿esta configuración es admisible: respeta los topes y deja holgura entre eslabones?

📘 **Dónde se aprende** (1 clase): [B101-C04 · Límites articulares, espacio de trabajo y evitación de colisiones](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md).

### Centrífuga

- La aceleración de Coriolis es `−2ω × v_rot`; la centrífuga, `−ω × (ω × r)`.

💡 **Cómo se explica en la clase [B73-C02](../programa/clases/B73/B73-C02-marcos-rotatorios-sinodicos/CLASE.md):**
- Las aceleraciones aparentes son `2 n |v_rot| = 1,657e-02 m/s²` (Coriolis) y `n² ρ = 2,835e-04 m/s²` (centrífuga); en esta órbita cercana a la Tierra ambas son pequeñas frente a la atracción terrestre.
- Sinódico: (r, v) con Coriolis y centrífuga.
- ⚠️ **Error frecuente:** Creer que la fuerza centrífuga es real. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un radar, un archivo de efemérides y un diseño de trayectoria rara vez usan el mismo marco. Confundir una velocidad inercial con una giratoria cambia el resultado en kilómetros por segundo.

📘 **Dónde se aprende** (1 clase): [B73-C02 · Marcos rotatorios sinódicos](../programa/clases/B73/B73-C02-marcos-rotatorios-sinodicos/CLASE.md).

### Centro

- El centro es la longitud de onda del mínimo.

💡 **Cómo se explica en la clase [B53-C17](../programa/clases/B53/B53-C17-mineralogia-espectral/CLASE.md):**
- Conviene declarar ambas cantidades al reportar un centro de banda.
- *Descripción textual:* Del espectro se ajusta el continuo, se divide, se ajusta una parábola al mínimo y se obtienen centro y profundidad.
- ⚠️ **Error frecuente:** Reportar un centro sin incertidumbre. se corrige con 8,2
- 🎯 **Por qué importa:** La misma banda se mide distinto según cómo se defina el continuo y el ruido. La decisión central: ¿con qué incertidumbre se conocen el centro y la profundidad de una banda y qué sesgo introduce el método?

📘 **Dónde se aprende** (1 clase): [B53-C17 · Mineralogía espectral](../programa/clases/B53/B53-C17-mineralogia-espectral/CLASE.md).

### Centro de curvatura

- El centro de curvatura `C` es el centro de la esfera del espejo.

💡 **Cómo se explica en la clase [B41-C19](../programa/clases/B41/B41-C19-colimacion-y-prueba-de-enfoque/CLASE.md):**
- Un paraboloide de `R = 2000 mm` probado en su centro de curvatura corta el eje a `R + 5,006 mm` en `h = 100 mm`; el desenfoque que baja el Strehl a `0,8` es `±28,33 µm` (`2,060 λN²`); un secundario inclinado `0,0986°` produce coma igual al radio de Airy y con sigma `0,1°` el `67,5 %` queda dentro.
- ⚠️ **Error frecuente:** Confundir el centro de curvatura con el foco. Está al doble.
- 🎯 **Por qué importa:** Un buen espejo mal colimado rinde mal. La decisión central: ¿cuánta descolimación y cuánto desenfoque se toleran?

📘 **Dónde se aprende** (2 clases): [B41-C19 · Colimación y prueba de enfoque](../programa/clases/B41/B41-C19-colimacion-y-prueba-de-enfoque/CLASE.md); [B50-C03 · Sistemas catadióptricos: Schmidt y Maksutov](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md).

### Centro de gravedad

- El centro de gravedad (CG) es el promedio de las posiciones ponderado por la masa.

💡 **Cómo se explica en la clase [B95-C01](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md):**
- Un 3U sintético suma `5,000 kg` (límite `6,00 kg`) y tiene el centro de gravedad en `(0,094; 0,115; 2,025) cm`, dentro de `±2 / ±2 / ±7 cm`.
- 🎯 **Por qué importa:** Un CubeSat que no cumple el estándar no entra en el dispensador, aunque funcione perfectamente. La decisión central: ¿esta configuración cabe, pesa y se equilibra dentro de lo que el estándar permite, y cuándo puede encenderse, desplegar y transmitir?

📘 **Dónde se aprende** (1 clase): [B95-C01 · Unidad CubeSat, dimensiones y formatos](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md).

### Centro de masa

- El centro de masa (`x_cg`) es `Σ m x/Σ m`.

💡 **Cómo se explica en la clase [B77-C22](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md):**
- El centro de masa no se mueve de forma monótona: se corre hacia la cola hasta `11,27 m` (a `25 %` de propelente) y luego vuelve a `10,60 m`, porque primero se vacía el tanque superior (delante) y después el inferior.
- *Descripción textual:* la fracción de propelente restante fija la masa y la longitud de cada columna de líquido; con los elementos secos se obtienen el centro de masa, la inercia y el margen, y las rebanadas comprueban la forma cerrada.
- ⚠️ **Error frecuente:** Usar el centro de masa inicial para todo el vuelo. Se corrige con 8.3.
- 🎯 **Por qué importa:** El control de actitud se diseña para una masa, un centro de masa y una inercia que ya no son los mismos al final del quemado. La decisión central: ¿cuánto se mueve el centro de masa, cuánto cae la inercia y qué le pasa al margen?

📘 **Dónde se aprende** (1 clase): [B77-C22 · Centro de masa y su variación con el consumo de propelente](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md).

### Centro de masa (CG)

- Margen de separación: margen de que la unión no se abra. Centro de masa (CG): punto promedio de la masa.

💡 **Cómo se explica en la clase [B90-C06](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md):**
- Un CubeSat 3U de siete piezas suma 3,25 kg, con centro de masa en (1,85; −1,11; 22,92) mm, dentro de los límites de ±20, ±20 y ±70 mm.
- 🎯 **Por qué importa:** Un perno mal apretado se afloja con la vibración o se rompe por exceso de carga; un centro de masa fuera de rango desvía la nave en el despliegue. La decisión central: ¿qué par de apriete garantiza que la unión no se separe ni se plastifique, y el conjunto queda dentro de los límites de masa?

📘 **Dónde se aprende** (1 clase): [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md).

### Centro de masas

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B31-C15):** El diseño de un acelerador depende de cuánta energía se pierde por radiación y de cuánta energía útil se obtiene. La decisión central: ¿qué campo y qué radio se necesitan y por qué los electrones pierden tanto?

📘 **Dónde se aprende** (1 clase): [B31-C15 · Física de aceleradores](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md).

### Centro del píxel

- El centro del píxel es su punto medio; la esquina su punto superior izquierdo.

💡 **Cómo se explica en la clase [B14-C26](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md):**
- Con la convención «el píxel `(fila, col)` cubre desde `lon0 + col·dx` hasta `lon0 + (col+1)·dx` y desde `lat0 − (fila+1)·dy` hasta `lat0 − fila·dy`», el centro del píxel `(0, 0)` es `(10,0005°; 39,9995°)` y la esquina `(10,0°; 40,0°)` cae en el píxel `(0, 0)`.
- ⚠️ **Error frecuente:** Confundir esquina y centro del píxel. Se corrige con los ejercicios 6 y 10.
- 🎯 **Por qué importa:** Una escena de satélite pesa cientos de megabytes y tú necesitas un recuadro de 100 × 120 píxeles. Si el formato obliga a leer todo el archivo, gastas tiempo y ancho de banda.

📘 **Dónde se aprende** (1 clase): [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md).

### Centro radial

- El centro radial `x_c = 4x0 + 2ẏ0/n` es constante del movimiento.

💡 **Cómo se explica en la clase [B76-C15](../programa/clases/B76/B76-C15-control-de-formacion-satelital/CLASE.md):**
- El centro radial pasa a `x_c = 4x0 + 2ẏ0/n = −1,0000 m`.
- *Descripción textual:* una elipse de radio `ρ` se cierra sola; un error de semieje equivale a un error de velocidad que desplaza el centro radial y crea una deriva por órbita; un impulso opuesto la anula y su suma anual es el presupuesto.
- 🎯 **Por qué importa:** Un error de un metro en el semieje parece nada y deriva nueve metros por órbita. La decisión central: ¿cuánto se desvía una formación por un error de inserción y cuánto `Δv` cuesta mantenerla?

📘 **Dónde se aprende** (1 clase): [B76-C15 · Control de formación satelital](../programa/clases/B76/B76-C15-control-de-formacion-satelital/CLASE.md).

### Centro×centro

- Un punto es silla×centro si tiene un par real y un par imaginario, y centro×centro si tiene dos pares imaginarios.

💡 **Cómo se explica en la clase [B73-C04](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md):**
- *Descripción textual:* la hessiana de `Ω` alimenta una cuadrática en `λ²`; según el signo de sus dos raíces el punto es silla×centro (inestable) o centro×centro (estable lineal), y para L4 y L5 la condición es la de Routh.
- ⚠️ **Error frecuente:** Concluir estabilidad total de un centro×centro lineal. Se corrige con 8.5.
- 🎯 **Por qué importa:** Que un punto sea de equilibrio no dice si una nave se queda o se va. Los autovalores dicen cuánto tiempo tienes antes de corregir la posición y si un grupo de asteroides puede quedarse en L4.

📘 **Dónde se aprende** (1 clase): [B73-C04 · Estabilidad local de Lagrange](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md).

### Centroide

- El centroide tiene ruido `σ_px`; el ruido angular por estrella es `σ_a = atan(σ_px/f)`.
- El centroide de una línea.

💡 **Cómo se explica en la clase [B42-C14](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md):**
- Con `0,5 arcsec/px` un centroide de `0,05 px` es `0,025 arcsec = 1,212 × 10⁻⁷ rad` de pendiente y, sobre `0,2 m`, `24,24 nm` de camino óptico.
- Con mancha gaussiana de `σ = 0,85 px`, ventana de 8 × 8 y lectura de 3 e⁻ (ilustrativos) 400 fotones dan un centroide con `0,1461 px` (previsto `0,1446`); un centroide de `0,05 px` es `24,24 nm` de camino óptico en una subapertura de `0,2 m`.
- 🎯 **Por qué importa:** El Shack-Hartmann es el sensor más usado en óptica adaptativa. La decisión central: ¿cuántos fotones hacen falta por subapertura para que el centroide sea preciso?

📘 **Dónde se aprende** (4 clases): [B42-C14 · Sensores Shack-Hartmann](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md); [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md); [B45-C10 · Líneas de emisión](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md); [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md).

### Centroide por momentos

- El centroide por momentos es `Σ I x / Σ I`.

🎯 **Por qué importa (clase B74-C02):** Un ángulo de `0,01″` parece pequeño, pero a un millón de kilómetros son decenas de metros. La decisión central: ¿cuánta incertidumbre angular aporta el detector y cuánta es un efecto físico que hay que modelar (aberración)?

📘 **Dónde se aprende** (1 clase): [B74-C02 · Observación angular y astrometría](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md).

### CEP

- El CEP es el radio del círculo horizontal con 50 % de probabilidad; el SEP, de la esfera con 50 %.

💡 **Cómo se explica en la clase [B74-C19](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md):**
- Con `σ = (3; 1,2; 2) m`: RMS 3D `3,8000 m` (muestral `3,8012 m`), percentil 95 de la norma 3D `6,493 m`, SEP (50 %) `3,190 m`, CEP (50 %, horizontal) `2,425 m`.
- Con `N = 50`, el RMS 3D es `3,816 ± 0,245 m`, el percentil 95 `6,316 ± 0,634 m` y el CEP `2,457 ± 0,264 m`.
- ⚠️ **Error frecuente:** Comparar un CEP con un 95 %. Son probabilidades distintas; ver 8.1.
- 🎯 **Por qué importa:** Dos informes pueden decir «3 m» y referirse a cosas distintas (RMS, 50 %, 95 %). La decisión central: ¿qué métrica comunica el riesgo que importa, con qué probabilidad y con qué incertidumbre muestral?

📘 **Dónde se aprende** (1 clase): [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md).

### Cercana

- Una variante cercana cambia los números; una media, además el cuerpo central o la magnitud pedida; una lejana, también el contexto y las unidades.

💡 **Cómo se explica en la clase [B131-C07](../programa/clases/B131/B131-C07-ejercicios-de-transferencia/CLASE.md):**
- Cercana (1): cuerpo con `P = 15,9 años` alrededor del Sol, se pide `a` → `6,323 UA`.
- La cercana mide ejecución del procedimiento; la media, si el estudiante reconoce el papel de `M`; la lejana, si entiende la ley como relación entre magnitudes y no como una receta en UA y años.
- 🎯 **Por qué importa:** Resolver bien un problema practicado puede ser memoria. La decisión central: ¿qué debe cambiar para que el ejercicio mida que el estudiante comprendió la ley y no el procedimiento?

📘 **Dónde se aprende** (1 clase): [B131-C07 · Ejercicios de transferencia](../programa/clases/B131/B131-C07-ejercicios-de-transferencia/CLASE.md).

### Cercha Serrurier

- La cercha Serrurier son dos brazos que soportan los extremos.

🎯 **Por qué importa (clase B43-C10):** Lo que decolima no es la flexión sino la flexión diferencial entre primario y secundario. La decisión central: ¿qué rigideces hacen que los dos extremos se muevan lo mismo, de modo que el eje óptico solo se desplace en paralelo?

📘 **Dónde se aprende** (1 clase): [B43-C10 · Estructura de tubo óptico](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md).

### Cero

- Un espacio vectorial real es un conjunto `V` con una suma `u + v` y un producto por escalares reales `a·u` que cumplen ocho propiedades: la suma es conmutativa y asociativa; existe un vector cero que no cambia nada; todo vector tiene un opuesto; y el producto por escalares es distributivo sobre la suma de vectores y de escalares, asociativo y con `1·u = u` (S1 usa `ℝⁿ` con estas operaciones en §1.2(v)).

💡 **Cómo se explica en la clase [B10-C01](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md):**
- La palabra clave es homogénea (lado derecho cero).
- Con lado derecho distinto de cero no hay subespacio (el origen no es solución).
- ⚠️ **Error frecuente:** Olvidar comprobar el cero. Se corrige con el ejercicio 3.
- 🎯 **Por qué importa:** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Ceros

- Sus polos son las raíces del denominador; sus ceros, las del numerador.

💡 **Cómo se explica en la clase [B16-C05](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md):**
- Un sistema de segundo orden sin ceros es `ωn²/(s² + 2ζωn s + ωn²)`.
- El espacio de estados (C02) conserva todos los estados internos y vale para varias entradas y salidas; la función de transferencia solo describe la relación de una entrada con una salida, ignora lo que se cancele entre polos y ceros, y es compacta.
- 🎯 **Por qué importa:** Un ingeniero que diseña el control de actitud de un telescopio revisa decenas de variantes de ganancias.

📘 **Dónde se aprende** (1 clase): [B16-C05 · Funciones de transferencia](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md).

### Cerrojo

- Un cerrojo (*lock*) deja pasar a un solo hilo a la vez por un trozo de código.

💡 **Cómo se explica en la clase [B18-C01](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md):**
- La defensa es un cerrojo (`with cerrojo: cuenta += 1`) o, mejor, no compartir datos mutables: que cada hilo devuelva su resultado y combinarlos al final.
- 🎯 **Por qué importa:** Tienes ocho órbitas simuladas que propagar y un portátil con varios núcleos. La tentación es «lanzar ocho hilos y listo».

📘 **Dónde se aprende** (1 clase): [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md).

### Cesión

- La cesión es la parte del riesgo transferida.

🎯 **Por qué importa (clase B127-C07):** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Chebyshev

- Los nodos equiespaciados están a igual distancia; los de Chebyshev son `cos(π(2i + 1)/(2(n + 1)))` y se acumulan hacia los extremos.

💡 **Cómo se explica en la clase [B11-C18](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md):**
- Con nodos de Chebyshev decrece: `0,40`, `0,17`, `0,069`, `0,033`, `0,015`.
- F -->|Chebyshev| H["Error decrece con n"]
- 🎯 **Por qué importa:** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.

📘 **Dónde se aprende** (1 clase): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md).

### Checksum

- El checksum (columna 69) es la suma de los dígitos (el signo menos vale 1) módulo 10.

💡 **Cómo se explica en la clase [B74-C29](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md):**
- *Descripción textual:* los elementos se escriben en un TLE de columnas fijas, se calcula el checksum, se lee por columnas, se obtienen magnitudes de dos cuerpos y un mensaje tipo OMM; el checksum determina qué errores se detectan.
- ⚠️ **Error frecuente:** Creer que el checksum protege contra todo error. No detecta transposiciones; ver 8.3.
- 🎯 **Por qué importa:** Un TLE mal copiado o mal leído da una órbita equivocada sin avisar. La decisión central: ¿qué errores detecta la suma de verificación, qué resolución tiene cada campo y qué significan realmente esos «elementos medios»?

📘 **Dónde se aprende** (1 clase): [B74-C29 · Formatos TLE y OMM de elementos orbitales](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md).

### Chi cuadrado

- El chi cuadrado `χ² = Σ(xᵢ − x_w)²/uᵢ²` mide la dispersión respecto de la media ponderada en unidades de incertidumbre.
- El chi cuadrado mide el ajuste;

🎯 **Por qué importa (clase B13-C18):** Tres radiómetros miden la misma irradiancia solar y dan `1361,4`, `1360,1` y `1362,9 W/m²`. Cada uno declara una incertidumbre.

📘 **Dónde se aprende** (2 clases): [B13-C18 · Intercomparación de instrumentos](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md); [B45-C13 · Temperatura y espectro de cuerpo negro](../programa/clases/B45/B45-C13-temperatura-y-espectro-de-cuerpo-negro/CLASE.md).

### Chi cuadrado de Poisson

- El chi cuadrado de Poisson `Σ (O − E)²/E`.

🎯 **Por qué importa (clase B38-C09):** Una simulación calibrada para coincidir con los datos no queda validada por coincidir con ellos. La decisión central: ¿qué parte del acuerdo es una predicción y qué parte es un ajuste?

📘 **Dónde se aprende** (1 clase): [B38-C09 · Validación de galaxias simuladas frente a observaciones](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md).

### Chick–Watson

- Flujo pistón (PFR): flujo sin mezcla longitudinal. Chick–Watson: inactivación proporcional a `C·t`.

🎯 **Por qué importa (clase B106-C26):** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?

📘 **Dónde se aprende** (1 clase): [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### Chirp

- El chirp es un pulso cuya frecuencia varía linealmente.
- El chirp es el pulso transmitido.

💡 **Cómo se explica en la clase [B57-C07](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md):**
- El mayor lóbulo lateral cercano al pico del chirp sin ventana, medido en la simulación, es de `-13,5 dB`; en la práctica se aplican ventanas para bajarlo a costa de ensanchar el pico.
- P["chirp de ancho B y duracion tau"] --> E["eco de un blanco"]
- ⚠️ **Error frecuente:** Presentar el chirp como el de Sentinel-1. Es ilustrativo (sección 5).
- 🎯 **Por qué importa:** La luz visible no atraviesa nubes ni sirve de noche; las microondas sí. Pero un radar no «fotografía»: mide distancia y fase de ecos.

📘 **Dónde se aprende** (2 clases): [B57-C07 · Sistemas radar SAR](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md); [B69-C02 · Formación de imágenes SAR](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md).

### Chirrido

- El chirrido es el aumento conjunto de frecuencia y amplitud.

💡 **Cómo se explica en la clase [B28-C21](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md):**
- Para `M ≥ 0,97` (pérdida del 3 % de la señal-ruido) con el tiempo de coalescencia fijo, la masa de chirrido debe conocerse con `0,15 %`: el banco necesita plantillas muy próximas.
- *Descripción textual:* la masa de chirrido da la frecuencia y la fase, de ahí la forma de onda; el filtro acoplado la correlaciona con los datos y el desajuste con plantillas vecinas fija el banco.
- ⚠️ **Error frecuente:** Tomar el chirrido sintético por real. Se corrige con la sección 5.
- 🎯 **Por qué importa:** Una plantilla ligeramente errada pierde mucha señal-ruido, porque la fase acumula miles de ciclos. Entender cuánto determina cuántas plantillas hacen falta.

📘 **Dónde se aprende** (2 clases): [B27-C13 · Binarias compactas](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md); [B28-C21 · Formas de onda gravitacionales y filtro acoplado](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md).

### CHNOPS

- Los elementos CHNOPS (carbono, hidrógeno, nitrógeno, oxígeno, fósforo, azufre) forman la mayor parte de la materia viva conocida.

💡 **Cómo se explica en la clase [B56-C02](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md):**
- ⚠️ **Error frecuente:** Generalizar CHNOPS a toda la vida posible. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Para buscar vida hay que saber qué hace la vida conocida con la materia: qué elementos usa y de dónde saca energía. La decisión central: dada una reacción metabólica, ¿está balanceada y cuánta energía libre libera o consume por mol?

📘 **Dónde se aprende** (1 clase): [B56-C02 · Bioquímica y metabolismo terrestre](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md).

### Cholesky

- QR: `A = Q R` con `Q` de columnas ortonormales y `R` triangular superior. Cholesky: `A = L Lᵀ` con `L` triangular inferior de diagonal positiva, para `A` simétrica definida positiva (`xᵀA x > 0` para todo `x ≠ 0`; sus autovalores son positivos, C08).

💡 **Cómo se explica en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- Aproximadamente: LU cuesta `2n³/3` operaciones, Cholesky `n³/3` (la mitad, por usar la simetría), QR cerca de `4n³/3` para matrices cuadradas.
- Regla práctica: Cholesky si hay simetría definida positiva;
- ⚠️ **Error frecuente:** Aplicar Cholesky a una matriz que no es definida positiva. Se corrige con los ejercicios 5 y 10.
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.

📘 **Dónde se aprende** (1 clase): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md).

### Choque

- El choque es una discontinuidad que cruza el flujo.
- La onda de rarefacción, la discontinuidad de contacto y el choque son las tres ondas del tubo de Sod.
- Choque: excitación transitoria breve.

💡 **Cómo se explica en la clase [B30-C14](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md):**
- Cuanto más fuerte el choque, más duro el espectro (índice menor).
- Límite: partículas de prueba y choque plano.
- 🎯 **Por qué importa:** Las partículas energéticas solares son un riesgo para satélites y astronautas, y los choques de las CME son un origen. La decisión central: ¿qué espectro produce un choque de una compresión dada?

📘 **Dónde se aprende** (3 clases): [B30-C14 · Choques y aceleración de partículas](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md); [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md); [B90-C10 · Ensayos de choque](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md).

### Choque desprendido

- El choque desprendido aparece cuando `θ` supera el máximo.

💡 **Cómo se explica en la clase [B79-C07](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md):**
- A `M₁ = 2` una deflexión de `30°` supera `θ_máx` y no tiene solución adjunta (choque desprendido).
- 🎯 **Por qué importa:** B30-C14 trata choques astrofísicos, no gasdinámicos. Para tomas de aire, toberas y reentrada hace falta saber cuánto sube la presión y cuánta energía útil se pierde.

📘 **Dónde se aprende** (1 clase): [B79-C07 · Ondas de choque normales y oblicuas](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md).

### Choque normal

- Un choque normal es perpendicular al flujo; uno oblicuo está inclinado un ángulo `β` y desvía el flujo un ángulo `θ`.

💡 **Cómo se explica en la clase [B79-C07](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md):**
- *Descripción textual:* el choque oblicuo se reduce a un choque normal con la componente normal del Mach; las propiedades se verifican con los balances de conservación.
- Un choque normal a `M₁ = 2` en aire a `250 K` y `50000 Pa` da `p₂/p₁ = 4,5`, `T₂/T₁ = 1,6875`, `M₂ = 0,5774` y conserva el `72,09 %` de la presión total.
- 🎯 **Por qué importa:** B30-C14 trata choques astrofísicos, no gasdinámicos. Para tomas de aire, toberas y reentrada hace falta saber cuánto sube la presión y cuánta energía útil se pierde.

📘 **Dónde se aprende** (1 clase): [B79-C07 · Ondas de choque normales y oblicuas](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md).

### Choque perfectamente inelástico

- Un choque perfectamente inelástico es aquel en que los cuerpos quedan unidos.

🎯 **Por qué importa (clase B05-C08):** Un cohete en el vacío no tiene nada contra lo que empujar y aun así acelera. La pregunta motivadora es: ¿cómo cambia la velocidad de un cuerpo cuando expulsa masa o cuando choca, si no hay fuerzas externas?

📘 **Dónde se aprende** (1 clase): [B05-C08 · Momento lineal e impulsos](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md).

### Choque térmico

- El choque térmico crítico es `ΔT = σ_f(1 − ν)/(Eα)`.

🎯 **Por qué importa (clase B84-C04):** Un metal avisa antes de romper; una cerámica no. Diseñar con la resistencia media de una probeta pequeña sobreestima la de una pieza grande en 40 %.

📘 **Dónde se aprende** (1 clase): [B84-C04 · Cerámicos y polímeros espaciales](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md).

### Chorro estructurado

- El chorro estructurado tiene energía que decrece con el ángulo al eje.

🎯 **Por qué importa (clase B28-C12):** Un destello gamma débil puede ser un evento normal visto de lado. Un modelo de emisión conjunta permite relacionar qué se ve en cada mensajero con el ángulo de visión.

📘 **Dónde se aprende** (1 clase): [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md).

### CI

- Una condrita es un meteorito formado por materiales que no se fundieron del todo; las condritas carbonáceas son ricas en carbono, y las CI son las más primitivas en cuanto a su composición.

🎯 **Por qué importa (clase B06-C20):** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.

📘 **Dónde se aprende** (1 clase): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### Ciclado

- Bakeout: calentamiento en vacío para expulsar volátiles. Ciclado: repetición de ciclos entre dos temperaturas.

💡 **Cómo se explica en la clase [B90-C12](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md):**
- Para un año de órbita (5 840 ciclos de −10 a +30 °C), el factor de aceleración de un ciclado de −40 a +60 °C es 12,04, es decir 485 ciclos de ensayo, 42,7 días de cámara.
- 🎯 **Por qué importa:** Una nave en órbita baja sufre unos 16 ciclos térmicos por día; no se pueden repetir 5 840 ciclos en tierra. La decisión central: ¿cuántos ciclos de ensayo con mayor amplitud representan un año de órbita y cuánto tarda la campaña?

📘 **Dónde se aprende** (1 clase): [B90-C12 · Vacío térmico y ciclos](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md).

### Ciclado térmico

- El ciclado térmico produce fatiga en soldaduras.

💡 **Cómo se explica en la clase [B86-C14](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md):**
- N["ciclos = ciclos/año x t"] --> TH["ciclado térmico"]
- 🎯 **Por qué importa:** Dimensionar un ala con su potencia de inicio de vida deja a la misión sin energía al final. El factor de fin de vida que se usó como `0,85` en la primera clase sale de un cálculo como este.

📘 **Dónde se aprende** (1 clase): [B86-C14 · Envejecimiento de paneles](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md).

### Cíclico

- El par secular acumula; el cíclico oscila con amplitud `τ_c/n` en `h`.

💡 **Cómo se explica en la clase [B87-C14](../programa/clases/B87/B87-C14-saturacion-y-descarga-de-momento/CLASE.md):**
- Un par cíclico de `20 µN·m` a la frecuencia orbital añade `±0,0181 N·m·s` de oscilación (amplitud `τ_c/n`).
- 🎯 **Por qué importa:** Una rueda saturada deja de controlar. La decisión central: ¿en cuánto tiempo se satura, cuánto par magnético hace falta para sostener la descarga y qué nivel de momento queda en régimen?

📘 **Dónde se aprende** (1 clase): [B87-C14 · Saturación y descarga de momento](../programa/clases/B87/B87-C14-saturacion-y-descarga-de-momento/CLASE.md).

### Ciclo

- Un ciclo es un fenómeno que se repite, como una vuelta de la Tierra sobre su eje o de la Luna alrededor de la Tierra.
- Un ciclo es una contradicción.
- Un ciclo es un paso al caliente y al frío.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- Pero cada ciclo se puede medir de más de una manera, y eso produce unidades distintas.
- El ciclo natural (día, mes, año) es fácil de observar pero cambia según el modo de medirlo: día solar o sidéreo, año sidéreo o trópico.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).

📘 **Dónde se aprende** (8 clases): [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B30-C03 · Ciclo de actividad solar](../programa/clases/B30/B30-C03-ciclo-de-actividad-solar/CLASE.md); [B53-C09 · Estratigrafía planetaria](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md); [B85-C19 · Ensayos de vacío térmico](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md); [B97-C25 · Excavación y manejo de regolito con robots](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md); [B109-C03 · Accesos, esclusas y transferencia entre ambientes presurizados](../programa/clases/B109/B109-C03-accesos-esclusas-y-transferencia-entre-ambientes-presurizados/CLASE.md) y 2 más.

### Ciclo anual

- El ciclo anual es la oscilación estacional que se ajusta aparte.

💡 **Cómo se explica en la clase [B57-C12](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md):**
- Un remolino de `0,20 m` de altura y `50 km` de radio característico a `33°` sur (ilustrativo) y una serie mensual de `30` años con una tendencia impuesta de `3 mm/año` (ilustrativa, no es una medición) con ciclo anual de `40 mm` y ruido de `20 mm`.
- ⚠️ **Error frecuente:** Ignorar el ciclo anual. Sesga la pendiente (ejercicio 6).
- 🎯 **Por qué importa:** El océano se mueve lento y se eleva más lento aún. La decisión central: ¿qué pendiente de la superficie equivale a una corriente y cuántos años de datos se necesitan para ver una tendencia de pocos milímetros por año entre un ruido de centímetros?

📘 **Dónde se aprende** (1 clase): [B57-C12 · Oceanografía desde órbita](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md).

### Ciclo CNO

- El ciclo CNO usa carbono, nitrógeno y oxígeno como catalizadores para el mismo resultado neto.

💡 **Cómo se explica en la clase [B24-C07](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md):**
- En el ciclo CNO, un protón se une al carbono-12, al nitrógeno-14 y a otros núcleos en secuencia y al final se libera un helio-4 y se recupera el catalizador.
- El ciclo CNO cambia más con la temperatura, de modo que domina en núcleos más calientes (estrellas más masivas) y p–p en núcleos más fríos.
- 🎯 **Por qué importa:** Dos protones se repelen con una fuerza eléctrica enorme; a las temperaturas de una estrella casi ninguno tiene energía para acercarse lo suficiente. Aun así la fusión ocurre, por efecto túnel.

📘 **Dónde se aprende** (1 clase): [B24-C07 · Ciclo CNO y cadena protón-protón](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md).

### Ciclo de 18,6 años

- El ciclo de 18,6 años es la regresión del nodo de la órbita lunar sobre la eclíptica, que hace variar su inclinación al ecuador entre `18,3°` y `28,6°`; no se consultó, se menciona como contexto.

🎯 **Por qué importa (clase B72-C10):** Un satélite geoestacionario sin maniobras de inclinación deriva de su plano ecuatorial algo menos de un grado por año, y el combustible de ese mantenimiento fija su vida útil. La decisión central: ¿cuánto contribuye cada cuerpo a la deriva de la inclinación y cuánto de ese resultado depende de simplificar la órbita lunar?

📘 **Dónde se aprende** (1 clase): [B72-C10 · Perturbaciones lunares](../programa/clases/B72/B72-C10-perturbaciones-lunares/CLASE.md).

### Ciclo de actividad

- El ciclo de actividad es la variación de largo plazo de la actividad.

🎯 **Por qué importa (clase B24-C12):** La modulación del brillo por manchas permite medir el periodo de rotación de miles de estrellas sin necesitar espectros, pero también contamina la búsqueda de exoplanetas y limita la precisión de las velocidades radiales.

📘 **Dónde se aprende** (1 clase): [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md).

### Ciclo de Brayton

- El ciclo de Brayton tiene compresión isentrópica, calentamiento isobaro, expansión isentrópica y enfriamiento isobaro.

🎯 **Por qué importa (clase B79-C15):** B85-C11 trata ciclos térmicos de ensayo, no termodinámicos. Para entender el rendimiento de una turbina de gas hay que ver el ciclo que lo origina.

📘 **Dónde se aprende** (1 clase): [B79-C15 · Ciclos termodinámicos de propulsión](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md).

### Ciclo de repetición

- La resolución temporal es el intervalo entre observaciones del mismo punto; el ciclo de repetición es el tiempo tras el cual la traza se repite.

💡 **Cómo se explica en la clase [B57-C02](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md):**
- ⚠️ **Error frecuente:** Tomar el ciclo de repetición como imágenes útiles. Las nubes reducen los datos válidos (8.4).
- 🎯 **Por qué importa:** Un satélite con píxeles de 30 m no ve una casa y uno que vuelve cada 16 días no ve una tormenta. La decisión central: ¿qué tamaño de píxel, qué ancho de barrido y qué ciclo de repetición necesita el fenómeno que quiero estudiar?

📘 **Dónde se aprende** (1 clase): [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md).

### Ciclo de Saros

- El ciclo metónico son 235 meses sinódicos (≈ 19 años); el calípico son cuatro metónicos menos un día; el ciclo de Saros son 223 meses sinódicos.

💡 **Cómo se explica en la clase [B132-C01](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md):**
- Sus inscripciones citan periodos como el 223 del ciclo de Saros y una espiral dividida en 235 secciones (ciclo metónico).
- 🎯 **Por qué importa:** Un relato histórico es tan fiable como las fuentes que lo sostienen, y tres copias de una misma fuente no son tres fuentes. La decisión central: ¿cuánto apoyo da realmente un conjunto de fuentes a una afirmación y cuánto de ese apoyo es robusto ante cambios razonables de criterio?

📘 **Dónde se aprende** (1 clase): [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Ciclo de trabajo

- El ciclo de trabajo es la fracción de muestras válidas.
- El ciclo de trabajo es la fracción de la órbita en que se adquiere.
- El ciclo de trabajo es la fracción del tiempo que el propulsor empuja de forma útil.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B37-C13](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md):**
- Con ciclo de trabajo `0,900` y `σ(A) = 1,76 ppm`:
- 🎯 **Por qué importa:** El análisis sísmico depende de cómo se prepara la serie. La decisión central: ¿qué hace el muestreo, los huecos y el filtro con las frecuencias y amplitudes recuperadas?

📘 **Dónde se aprende** (5 clases): [B37-C13 · Series fotométricas de Kepler, TESS y PLATO para asterosismología](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md); [B57-C24 · Diseño de una carga útil de observación terrestre](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md); [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md); [B85-C08 · Calentadores y termostatos](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md); [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### Ciclo húmedo–seco

- Un ciclo húmedo–seco alterna agua y secado, favoreciendo la unión por pérdida de agua.

🎯 **Por qué importa (clase B56-C21):** C03 trata el origen de autorreplicantes, pero ninguna clase trata la polimerización experimental y sus límites. Antes de que un replicador pueda copiarse, hay que formar cadenas lo bastante largas.

📘 **Dónde se aprende** (1 clase): [B56-C21 · Polimerización prebiótica experimental: oligómeros y condiciones de laboratorio](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md).

### Ciclo límite

- El ciclo límite es la oscilación permanente entre las paredes de la banda.

💡 **Cómo se explica en la clase [B87-C13](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md):**
- Un ciclo límite sin perturbaciones gasta propergol continuamente; en la práctica se amplía la banda muerta o se usan ruedas y se reserva el propulsor para maniobras y descargas.
- *Descripción textual:* el par de las toberas da un salto de velocidad angular por pulso mínimo, que fija el ciclo límite; el impulso total, dividido por `Isp g₀`, da el propergol gastado.
- 🎯 **Por qué importa:** Los propulsores son el actuador de más par y de respuesta rápida, y el único que cambia el momento total del satélite, pero cada pulso gasta masa que no vuelve. La decisión central: ¿cuánto propergol cuesta una maniobra o un año de mantenimiento de actitud, y qué precisión permite el impulso mínimo?

📘 **Dónde se aprende** (1 clase): [B87-C13 · Propulsores de control de actitud](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md).

### Ciclo menor

- El ciclo menor es el `mcd` de los períodos y el mayor el `mcm`.

💡 **Cómo se explica en la clase [B88-C23](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md):**
- El ejecutivo tiene ciclo menor de 100 ms, mayor de 400 ms y 4 tramas con cargas de 62, 12, 37 y 12 ms.
- 🎯 **Por qué importa:** Las dependencias hacia arriba y los ciclos hacen imposible probar un módulo por separado y convierten un cambio en riesgo global. La decisión central: ¿qué módulo depende de quién, y puede ordenarse el sistema en capas sin ciclos?

📘 **Dónde se aprende** (1 clase): [B88-C23 · Arquitectura de software de vuelo: capas y ejecutivo](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md).

### Ciclo metónico

- El ciclo metónico es la casi coincidencia entre 19 años trópicos y 235 meses sinódicos, que sirvió de base a calendarios lunisolares de la Antigüedad (la fuente que consultamos lo menciona en el mecanismo de Anticitera, S4).
- El ciclo metónico son 235 meses sinódicos (≈ 19 años); el calípico son cuatro metónicos menos un día; el ciclo de Saros son 223 meses sinódicos.

💡 **Cómo se explica en la clase [B132-C01](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md):**
- Sus inscripciones citan periodos como el 223 del ciclo de Saros y una espiral dividida en 235 secciones (ciclo metónico).
- 🎯 **Por qué importa:** Un relato histórico es tan fiable como las fuentes que lo sostienen, y tres copias de una misma fuente no son tres fuentes. La decisión central: ¿cuánto apoyo da realmente un conjunto de fuentes a una afirmación y cuánto de ese apoyo es robusto ante cambios razonables de criterio?

📘 **Dónde se aprende** (2 clases): [B02-C01 · Calendarios astronómicos en civilizaciones antiguas](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md); [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Ciclo mover y esperar

- El ciclo mover y esperar es: ejecutar, enviar telemetría, decidir y enviar la orden.

🎯 **Por qué importa (clase B97-C07):** Con un retardo de unos segundos se puede teleoperar casi en vivo; con minutos, no. La diferencia se traduce en horas o días de tarea y en la necesidad de dar autonomía al robot.

📘 **Dónde se aprende** (1 clase): [B97-C07 · Teleoperación con latencia](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md).

### Ciclo por día

- Un ciclo por día (c/d) es una unidad de frecuencia: 1 c/d = 11,574 µHz.

🎯 **Por qué importa (clase B15-C02):** Un detector que mide una estrella cada 2 minutos no puede ver directamente algo que oscila cada 3 minutos con precisión, pero tampoco lo ignora: ese movimiento rápido queda registrado como una oscilación lenta y falsa. Si no sabes que eso ocurre, publicarías un periodo que no existe.

📘 **Dónde se aprende** (1 clase): [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md).

### Ciclo sísmico

- El ciclo sísmico alterna acumulación lenta de deformación y liberación brusca.

🎯 **Por qué importa (clase B57-C20):** Chile vive sobre una zona de subducción activa y las instituciones deben comprender cuánta deformación se acumula y se libera. La decisión central: ¿qué puede decir una cuenta de balance de deslizamiento y qué no puede decir sobre cuándo ocurrirá el próximo terremoto?

📘 **Dónde se aprende** (1 clase): [B57-C20 · Caso de estudio climático o geológico de Chile](../programa/clases/B57/B57-C20-caso-de-estudio-climatico-o-geologico-de-chile/CLASE.md).

### Ciclo térmico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C02):** Un instrumento sin requisitos cuantificados no se puede diseñar ni verificar. La decisión central: ¿qué cifras de apertura, órbita, datos y masa se derivan de lo que se quiere medir?

📘 **Dónde se aprende** (1 clase): [B47-C02 · Requisitos de instrumentos orbitales](../programa/clases/B47/B47-C02-requisitos-de-instrumentos-orbitales/CLASE.md).

### Ciclo V

- Un ciclo V baja de la malla fina a la más gruesa y vuelve a subir.

🎯 **Por qué importa (clase B21-C03):** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Ciclos por kg de reposición

- Los ciclos por kg de reposición son `1/(1 − ρ)`.

🎯 **Por qué importa (clase B59-C15):** Cerrar el 87 % de un lazo no deja una reposición del 13 % sino una dependencia permanente del 13 %. La decisión central: ¿qué etapa del lazo conviene mejorar para reducir más la reposición?

📘 **Dónde se aprende** (1 clase): [B59-C15 · Ciclo cerrado de materiales](../programa/clases/B59/B59-C15-ciclo-cerrado-de-materiales/CLASE.md).

### Ciclotrón

- El ciclotrón gira a `f = eB/(2πγm)`.

🎯 **Por qué importa (clase B31-C15):** El diseño de un acelerador depende de cuánta energía se pierde por radiación y de cuánta energía útil se obtiene. La decisión central: ¿qué campo y qué radio se necesitan y por qué los electrones pierden tanto?

📘 **Dónde se aprende** (1 clase): [B31-C15 · Física de aceleradores](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md).

### Cielo

- El cielo es un parámetro más.
- El cielo (`B`) y la oscuridad (`D`) añaden fondo.

💡 **Cómo se explica en la clase [B44-C11](../programa/clases/B44/B44-C11-tiempo-de-exposicion/CLASE.md):**
- Con una fuente de `20 e⁻/s`, cielo de `2 e⁻/s/pix`, oscuridad de `0,1 e⁻/s/pix`, lectura de `6 e⁻` y `20` píxeles, un cuadro de `100 s` tiene SNR `24,042`;
- 🎯 **Por qué importa:** Exponer poco multiplica el ruido de lectura; exponer mucho arriesga la saturación. La decisión central: ¿cuánto debe durar cada cuadro dentro de un tiempo total dado?

📘 **Dónde se aprende** (2 clases): [B44-C11 · Tiempo de exposición](../programa/clases/B44/B44-C11-tiempo-de-exposicion/CLASE.md); [B45-C24 · Fotometría por ajuste de PSF](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md).

### Cielo completo

- El cielo completo supone exposición uniforme.

💡 **Cómo se explica en la clase [B28-C04](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md):**
- La significancia típica es `d/σ = 6,5` con cielo completo.
- 🎯 **Por qué importa:** El origen de los rayos cósmicos de mayor energía sigue abierto; el criterio de Hillas descarta fuentes y la anisotropía apunta a regiones. La decisión central: ¿qué fuentes pueden alcanzar una energía dada y qué anisotropía se puede detectar con un número dado de eventos?

📘 **Dónde se aprende** (1 clase): [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md).

### Cielo oscuro

- Un cielo oscuro es un cielo con poca luz artificial.

💡 **Cómo se explica en la clase [B02-C20](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md):**
- Según S3, el estudio temático de 2017 concluye que los lugares de cielo oscuro no pueden ser por sí mismos una categoría de Patrimonio Mundial, aunque la calidad del cielo oscuro puede reforzar el valor cultural o natural de un sitio; las Reservas Starlight y los Parques de Cielo Oscuro tampoco son categorías de Patrimonio Mundial.
- ⚠️ **Error frecuente:** Pensar que el cielo oscuro es solo asunto científico. Ejercicio 7.
- 🎯 **Por qué importa:** Los sitios, instrumentos, archivos, saberes y hasta la oscuridad del cielo son patrimonio, y los telescopios, el turismo y las constelaciones de satélites pueden dañarlo. La pregunta motivadora es: ¿qué debo preguntar, a quién y antes de qué, cuando mi trabajo toca un cielo o un lugar que importa a otras personas?

📘 **Dónde se aprende** (1 clase): [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md).

### Cielos oscuros

- Un interferómetro combina varias antenas para actuar como una más grande (ALMA). Cielos oscuros son cielos con poca luz artificial.

💡 **Cómo se explica en la clase [B02-C18](../programa/clases/B02/B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md):**
- C --> D["Preguntas actuales:<br/>territorio, comunidades,<br/>cielos oscuros"]
- *Descripción textual:* tres etapas encadenadas: una expedición que da origen a un observatorio nacional (1849–1853), la búsqueda de sitios y llegada de observatorios internacionales (1958–1974) y la expansión posterior con Paranal, Las Campanas y ALMA; todas conducen a preguntas actuales sobre territorio, comunidades y cielos oscuros.
- 🎯 **Por qué importa:** Chile alberga observatorios de primer nivel porque combina cielos oscuros, aire seco y altitud. Pero un observatorio también es una historia de decisiones, instituciones y territorios.

📘 **Dónde se aprende** (1 clase): [B02-C18 · Expansión de la astronomía en Chile](../programa/clases/B02/B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md).

### Cierra

- Un diseño cierra cuando todos los presupuestos son coherentes y cumplen sus márgenes.

💡 **Cómo se explica en la clase [B83-C20](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md):**
- Límite: en un velero el lazo se corta con la experiencia; aquí se cierra con una iteración y un modelo.
- El margen de datos de C11 es 43,38 %: el diseño cierra en masa y datos.
- ⚠️ **Error frecuente:** Resolver cada presupuesto por separado. Cierra el lazo completo
- 🎯 **Por qué importa:** Cada presupuesto aislado puede cerrar y el conjunto no. La decisión central: ¿existe una masa seca que sea coherente con la potencia, las baterías, la estructura y el propelente que ella misma exige, y cabe en el límite?

📘 **Dónde se aprende** (1 clase): [B83-C20 · Diseño preliminar completo de misión](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md).

### Cierre

- El cierre del balance es que la masa que entra iguale la que sale.
- Arquitectura: combinación de subsistemas. Cierre: fracción reciclada.

💡 **Cómo se explica en la clase [B59-C16](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md):**
- Balance de masa y de carbono verifican el cierre de forma independiente.
- 🎯 **Por qué importa:** Los residuos son una fuente de agua y de dióxido de carbono, pero también consumen oxígeno. La decisión central: ¿cuánto oxígeno cuesta cerrar el residuo y cuánta agua se recupera?

📘 **Dónde se aprende** (2 clases): [B59-C16 · Desechos y reciclaje](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md); [B106-C09 · Sistemas ECLSS](../programa/clases/B106/B106-C09-sistemas-eclss/CLASE.md).

### Cierre de bucle

- Un cierre de bucle es la restricción entre dos poses que representan el mismo lugar.
- Cierre de bucle: restricción entre dos poses del mismo lugar (F4, F7).

💡 **Cómo se explica en la clase [B97-C05](../programa/clases/B97/B97-C05-localizacion-y-mapeo-slam/CLASE.md):**
- La odometría pura termina a `0,856` m del punto de partida; con el cierre de bucle (σ = `0,02 m`) queda a `0,003` m.
- Descripción larga: el cierre de bucle reduce el error de cierre en un factor de 251,0 y el RMS de la trayectoria en 2,95.
- 🎯 **Por qué importa:** Sin una corrección, el error de la odometría crece con el recorrido y el mapa se deforma. El cierre de bucle reparte ese error por toda la trayectoria; entender cuánto y cómo evita fiarse de un mapa que se «cierra» solo en apariencia.

📘 **Dónde se aprende** (2 clases): [B97-C05 · Localización y mapeo SLAM](../programa/clases/B97/B97-C05-localizacion-y-mapeo-slam/CLASE.md); [B99-C04 · Cierre de bucles y consistencia global](../programa/clases/B99/B99-C04-cierre-de-bucles-y-consistencia-global/CLASE.md).

### Cierre de energía

- El cierre de energía verifica que lo que entra, sale o se almacena suma cero.

💡 **Cómo se explica en la clase [B85-C08](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md):**
- ⚠️ **Error frecuente:** Tomar el cierre de energía como validación física. valida el código (8.3)
- 🎯 **Por qué importa:** Un calentador pequeño no sostiene la temperatura y uno grande gasta energía que una batería no tiene. La decisión central: ¿cuánta potencia de calentador mantiene la temperatura mínima en el peor eclipse y cuánta energía cuesta por órbita?

📘 **Dónde se aprende** (1 clase): [B85-C08 · Calentadores y termostatos](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md).

### Cierre de fase

- El cierre de fase `φ₁₂ + φ₂₃ − φ₁₃` debe ser cero (mod 2π) si el triplete es consistente.

💡 **Cómo se explica en la clase [B69-C07](../programa/clases/B69/B69-C07-evaluacion-de-la-calidad-de-un-interferograma/CLASE.md):**
- T["φ12 + φ23 − φ13"] --> CL["cierre de fase"]
- 🎯 **Por qué importa:** Un interferograma bonito puede ser incorrecto. La decisión central: ¿qué números justifican aceptar, enmascarar o descartar un interferograma?

📘 **Dónde se aprende** (1 clase): [B69-C07 · Evaluación de la calidad de un interferograma](../programa/clases/B69/B69-C07-evaluacion-de-la-calidad-de-un-interferograma/CLASE.md).

### Cierre de lazo

- El cierre de lazo es la fracción de un consumible que se recupera.

🎯 **Por qué importa (clase B104-C02):** «La tripulación tendrá agua suficiente» no se puede comprobar; «4 personas, 30 días, 2,5 kg por persona y día más un 10 % de margen» sí. La decisión central: ¿cuánto hay que llevar, y a partir de cuántos días compensa un equipo que recicla?

📘 **Dónde se aprende** (1 clase): [B104-C02 · Requisitos de tripulación](../programa/clases/B104/B104-C02-requisitos-de-tripulacion/CLASE.md).

### Cierre del balance

- El cierre del balance es que el residuo sea cero.

💡 **Cómo se explica en la clase [B86-C20](../programa/clases/B86/B86-C20-simulacion-de-ciclo-energetico-orbital/CLASE.md):**
- *Descripción textual:* `β` fija el eclipse y el coseno del ala; con la degradación da la generación; en cada paso el balance con las cargas determina la batería, la energía descartada y las pérdidas; de ahí salen el SOC mínimo y el cierre del balance.
- 🎯 **Por qué importa:** Los cálculos por órbita aislada no ven que `β` cambia día a día ni que la degradación se acumula. Una simulación larga revela el peor día y comprueba que la energía se conserva en todo el recorrido.

📘 **Dónde se aprende** (1 clase): [B86-C20 · Simulación de ciclo energético orbital](../programa/clases/B86/B86-C20-simulacion-de-ciclo-energetico-orbital/CLASE.md).

### Cierre del ciclo

- El cierre del ciclo es que la energía recuperada iguale a la gastada.

🎯 **Por qué importa (clase B86-C13):** Una batería que cubre bien un eclipse puede fallar tras cien porque cada órbita pierde un poco más de lo que recupera. El cierre del ciclo es la prueba de que el diseño es sostenible.

📘 **Dónde se aprende** (1 clase): [B86-C13 · Energía durante eclipse](../programa/clases/B86/B86-C13-energia-durante-eclipse/CLASE.md).

### Cierre del lazo

- Cociente respiratorio: CO₂ por O₂ (0,85). Cierre del lazo: fracción recuperada.

🎯 **Por qué importa (clase B106-C05):** Llevar oxígeno comprimido o líquido pesa; electrolizar agua exige energía y reponer agua. La decisión central: ¿cuánta agua, hidrógeno y energía implica producir el oxígeno de una tripulación y qué parte del agua devuelve la reacción de Sabatier?

📘 **Dónde se aprende** (1 clase): [B106-C05 · Suministro y generación de oxígeno](../programa/clases/B106/B106-C05-suministro-y-generacion-de-oxigeno/CLASE.md).

### Cierre independiente

- El cierre independiente: los demás se obtienen de estos.

🎯 **Por qué importa (clase B51-C02):** Cuando las ganancias no se pueden calibrar (VLBI con atmósfera rápida, autocalibración), los cierres son los observables robustos. La decisión central: ¿qué información sobrevive a los errores por antena y cuánta se pierde?

📘 **Dónde se aprende** (1 clase): [B51-C02 · Cantidades de cierre: fase y amplitud de cierre](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md).

### Cifra de ruido

- La cifra de ruido `NF = 10 log₁₀(1 + T/T₀)` con `T₀ = 290 K`.

🎯 **Por qué importa (clase B49-C06):** Una décima de decibelio antes del primer amplificador cuesta más que mejorar el mezclador. La decisión central: ¿qué bloque domina la temperatura de ruido y qué pérdidas deben evitarse antes de él?

📘 **Dónde se aprende** (1 clase): [B49-C06 · Amplificadores de bajo ruido (LNA): tecnología, ganancia y adaptación](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md).

### Cifra derivada

- La cifra derivada se calcula aquí.

🎯 **Por qué importa (clase B28-C20):** Un caso de estudio sirve si es verificable: cada cifra debe llevar su fuente, y lo calculado debe distinguirse de lo publicado. La decisión central: ¿qué cifras del evento están respaldadas por lo consultado, cuáles se derivan y cuáles quedan fuera?

📘 **Dónde se aprende** (1 clase): [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md).

### Cifra excluida

- La cifra excluida no se consultó.

🎯 **Por qué importa (clase B28-C20):** Un caso de estudio sirve si es verificable: cada cifra debe llevar su fuente, y lo calculado debe distinguirse de lo publicado. La decisión central: ¿qué cifras del evento están respaldadas por lo consultado, cuáles se derivan y cuáles quedan fuera?

📘 **Dónde se aprende** (1 clase): [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md).

### Cifra publicada

- La cifra publicada viene de una fuente consultada.

🎯 **Por qué importa (clase B28-C20):** Un caso de estudio sirve si es verificable: cada cifra debe llevar su fuente, y lo calculado debe distinguirse de lo publicado. La decisión central: ¿qué cifras del evento están respaldadas por lo consultado, cuáles se derivan y cuáles quedan fuera?

📘 **Dónde se aprende** (1 clase): [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md).

### Cifra significativa

- Una cifra significativa es un dígito que aporta información sobre el valor; cuentan todos los dígitos desde el primero distinto de cero hasta el último que se ha medido o calculado con sentido (`0,00450` tiene 3).
- Una cifra significativa es un dígito con información.

🎯 **Por qué importa (clase B03-C11):** Si te piden el tiempo que tarda la luz del Sol en llegar a la Tierra y respondes «499,004783836 s», parece muy preciso, pero tus datos (1 au y `c`) son exactos; en cambio, si respondes lo mismo para la distancia a la Luna, que varía entre unos 357 000 y 407 000 km, esas cifras serían falsas.

📘 **Dónde se aprende** (2 clases): [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Cifrado autenticado AES en modo Galois/Counter (GCM)

- Su base de interoperabilidad es el cifrado autenticado AES en modo Galois/Counter (GCM) con clave de 256 bits.

🎯 **Por qué importa (clase B89-C25):** Los comandos son la superficie más sensible de una misión; sin autenticación y sin protección contra repetición, una trama capturada podría reutilizarse, y un CRC solo detecta errores, no ataques (C12). La decisión central: ¿cómo garantizar que una trama es auténtica, íntegra y no repetida, y cuánto cuesta en sobrecarga?

📘 **Dónde se aprende** (1 clase): [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md).

### Cifras significativas

- Las cifras significativas son las que aportan información; el resto sobra.
- Las cifras significativas son las que aporta la medida; la incertidumbre dice dónde cortar.

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- Si `d = 43 Mpc` tiene dos cifras significativas, escribe `1,3 × 10²⁴ m`, no `1,3268 × 10²⁴ m`.
- Paso 6 · Cifras. Con dos cifras significativas: `1,3 × 10²⁴ m`, `1,4 × 10⁸ ly`, `8,9 × 10¹² au`.
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.

📘 **Dónde se aprende** (2 clases): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md); [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md).

### Cilindro

- Un cilindro de radio `r` y altura `h` tiene volumen `πr²h`.

💡 **Cómo se explica en la clase [B03-C17](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md):**
- Un cilindro de radio `r` y altura `h` tiene volumen `πr²h`: el área de la base por la altura.
- 🎯 **Por qué importa:** La NASA publica que la densidad media del Sol es 1408 kg/m³ (S1), cerca de una vez y media la del agua. ¿Cómo se obtiene?

📘 **Dónde se aprende** (1 clase): [B03-C17 · Áreas y volúmenes elementales](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md).

### Cinemática

- La cinemática es `q̇ = ½ q ⊗ [0, ω]`, con `ω` la velocidad angular del cuerpo en su propio sistema.
- La cinemática `E_R = (μ² v²/m_N)(1 − cosθ)`.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- La cinemática `q̇ = ½ q ⊗ [0, ω]` conserva la norma de `q` de forma exacta en tiempo continuo; la dinámica es `J ω̇ = −ω × (J ω) + u`.
- D --> F["cuerpo rígido<br/>Euler + cinemática"]
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.

📘 **Dónde se aprende** (2 clases): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md); [B36-C10 · Búsqueda directa de materia oscura en laboratorio](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md).

### Cinemática directa

- La cinemática directa calcula la posición de la punta a partir de los ángulos.
- Parámetros D-H: `a` (longitud), `α` (torsión), `d` (desplazamiento) y `θ` (ángulo articular). Cinemática directa: de los ángulos al extremo.

💡 **Cómo se explica en la clase [B97-C02](../programa/clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md):**
- Al aplicar la cinemática directa a ambas se recupera el objetivo con error `1,78e-15` m.
- *Descripción textual:* los ángulos dan la posición por cinemática directa y se recuperan por la inversa; el jacobiano relaciona velocidades y su determinante anuncia las singularidades.
- 🎯 **Por qué importa:** Cada vez que un brazo coge una carga o una herramienta alguien resolvió una cinemática inversa y comprobó que el movimiento no pasa por una singularidad. Sin esa comprobación, un movimiento pequeño de la punta exige velocidades articulares enormes.

📘 **Dónde se aprende** (2 clases): [B97-C02 · Cinemática de manipuladores](../programa/clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md); [B101-C01 · Transformaciones homogéneas y parametrización de eslabones (Denavit-Hartenberg)](../programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/CLASE.md).

### Cinemática inversa

- La cinemática inversa calcula los ángulos para una posición.
- Cinemática inversa: de la pose del extremo a los ángulos.

🎯 **Por qué importa (clase B97-C02):** Cada vez que un brazo coge una carga o una herramienta alguien resolvió una cinemática inversa y comprobó que el movimiento no pasa por una singularidad. Sin esa comprobación, un movimiento pequeño de la punta exige velocidades articulares enormes.

📘 **Dónde se aprende** (2 clases): [B97-C02 · Cinemática de manipuladores](../programa/clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md); [B101-C02 · Cinemática inversa y redundancia de manipuladores](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md).

### Cinética

- La energía potencial es `U(q) = −log π(q)` (salvo constante), la cinética `K(p) = ½ pᵀp` y el hamiltoniano `H(q, p) = U(q) + K(p)`.

🎯 **Por qué importa (clase B19-C03):** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.

📘 **Dónde se aprende** (1 clase): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md).

### Cinética de reparación

- La cinética de reparación es la evolución del número de roturas con el tiempo.

💡 **Cómo se explica en la clase [B112-C05](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md):**
- Límite: la cinética de reparación real depende de la fase del ciclo celular, de las proteínas implicadas y de la cromatina, nada de lo cual se modela aquí.
- 🎯 **Por qué importa:** Falta la clase de mecanismos moleculares de daño y reparación. Sin ella, la diferencia de eficacia biológica entre fotones e iones pesados (B112-C01, C02) y la incertidumbre del riesgo (C04) parecen cifras arbitrarias.

📘 **Dónde se aprende** (1 clase): [B112-C05 · Daño y reparación del ADN por radiación espacial](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md).

### Cinta elástica

- Una cinta elástica (*tape spring*) es una lámina curvada que se aplana y enrolla y recupera su forma al soltarse.

🎯 **Por qué importa (clase B95-C04):** Un enlace con la Tierra necesita una antena, y una antena que no se despliega deja el satélite mudo. La decisión central: ¿qué longitud necesita la antena, cómo se pliega sin dañarla y qué riesgo añade el mecanismo?

📘 **Dónde se aprende** (1 clase): [B95-C04 · Antenas desplegables para satélites pequeños](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md).

### Cintura

- La cintura `w₀` es el radio del haz en su punto más estrecho (donde la intensidad cae a `1/e²`).

💡 **Cómo se explica en la clase [B92-C02](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md):**
- Reducir `θ` a la mitad (duplicar la cintura) suma `6,02 dB`.
- W["cintura w0"] --> T["divergencia theta = lambda/(pi w0)"]
- 🎯 **Por qué importa:** Una antena de radiofrecuencia tolera décimas de grado; un haz óptico, microrradianes. La decisión central: ¿qué divergencia conviene y qué apuntamiento hay que garantizar para que la ganancia ganada no se pierda?

📘 **Dónde se aprende** (1 clase): [B92-C02 · Divergencia del haz y pérdidas por apuntamiento óptico](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md).

### Cinturón principal

- El cinturón principal es la región entre Marte y Júpiter.

🎯 **Por qué importa (clase B52-C14):** Las posiciones de las resonancias fijan dónde mirar en un cinturón. La decisión central: ¿en qué semiejes están las resonancias de Júpiter y cómo se comprueba el cálculo?

📘 **Dónde se aprende** (1 clase): [B52-C14 · Cinturones de asteroides](../programa/clases/B52/B52-C14-cinturones-de-asteroides/CLASE.md).

### Cinturones de Van Allen

- Los cinturones de Van Allen son las regiones de partículas atrapadas.

🎯 **Por qué importa (clase B30-C16):** Las partículas con ángulo de paso pequeño se pierden en la atmósfera; las demás quedan atrapadas y dañan satélites. La decisión central: ¿qué partículas quedan atrapadas y con qué periodo rebotan?

📖 **Explicado a fondo:** [Cinturones de Van Allen](esencial/esencial-a-c.md#cinturones-de-van-allen) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B30-C16 · Cinturones de Van Allen](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md).

### CIP

- El CIP es el polo de referencia que separa el movimiento del eje en precesión-nutación y en movimiento polar (S1, glosario).

🎯 **Por qué importa (clase B13-C22):** Una estación terrestre apunta a una nave en el sistema celeste. Para ello debe saber cuánto ha girado la Tierra, hacia dónde apunta su eje en el cielo y dónde está ese eje dentro de la corteza.

📘 **Dónde se aprende** (1 clase): [B13-C22 · Parámetros de orientación terrestre: precesión, nutación, UT1 y movimiento polar](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md).

### Circulación

- La circulación es la integral de línea sobre una curva cerrada.
- La circulación de la línea de conjunción tiene tasa `|q n₁ − p n₂|`.

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- La circulación a lo largo del ecuador es `∮ v·dr = 2π a_E · (ω a_E) = 2π a_E² ω = 1,8639 × 10¹⁰ m²/s`.
- Stokes dice que el total de remolino en una superficie es la circulación en su borde.
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.

📘 **Dónde se aprende** (2 clases): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md); [B73-C10 · Resonancias de movimiento medio](../programa/clases/B73/B73-C10-resonancias-de-movimiento-medio/CLASE.md).

### Circular

- Es `√2` veces la circular.

💡 **Cómo se explica en la clase [B71-C15](../programa/clases/B71/B71-C15-velocidad-de-escape/CLASE.md):**
- La relación con la circular rasante terrestre (`7905.37 m/s`) cumple `√2 v_c` con diferencia `0e+00`.
- *Descripción textual:* anular la energía da el umbral; es `√2` veces la circular, se contrasta con las fichas, la rotación lo reduce algo y la integración confirma el umbral.
- 🎯 **Por qué importa:** La velocidad de escape es el umbral entre una órbita cerrada y una trayectoria abierta. La decisión central: ¿qué velocidad hay que alcanzar para no volver y cuánto la reduce partir de una altura o de una superficie que gira?

📘 **Dónde se aprende** (1 clase): [B71-C15 · Velocidad de escape](../programa/clases/B71/B71-C15-velocidad-de-escape/CLASE.md).
