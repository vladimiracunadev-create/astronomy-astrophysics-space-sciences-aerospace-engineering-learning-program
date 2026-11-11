# Términos · E (parte 3 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · **E** · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-e.md) · [2](terminos-e-2.md) · **3**

### Evidencias

- Las evidencias son los resultados trazables que sostienen cada veredicto.

🎯 **Por qué importa (clase B23-C08):** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.

📘 **Dónde se aprende** (1 clase): [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Evolución darwiniana

- Homeostasis es la regulación del medio interno. Evolución darwiniana es el cambio de una población por variación heredable y reproducción diferencial.

💡 **Cómo se explica en la clase [B56-C01](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md):**
- La NASA describe la astrobiología como el estudio del origen, la evolución y la distribución de la vida en el universo, y cita como definición de trabajo frecuente «un sistema autosostenido capaz de evolución darwiniana»; añade que existen varios cientos de otras definiciones (S1, consultada el 2026-11-09).
- 🎯 **Por qué importa:** Una misión que busca vida necesita saber qué buscar y qué contará como hallazgo. Si el criterio es vago, cualquier resultado se puede discutir; si es demasiado estrecho, se pasa por alto lo que no se parece a la vida terrestre.

📘 **Dónde se aprende** (1 clase): [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md).

### Evolución térmica parametrizada

- La evolución térmica parametrizada reemplaza la convección completa por una ley `Nu(Ra)`.

🎯 **Por qué importa (clase B65-C01):** Sin convección, el interior de un planeta rocoso solo perdería calor por conducción y se enfriaría con una escala de tiempo mucho mayor. La decisión central: ¿cuánto calor saca la convección y a qué temperatura se estabiliza un manto que sigue produciendo calor radiactivo?

📘 **Dónde se aprende** (1 clase): [B65-C01 · Convección del manto y evolución térmica de interiores planetarios](../programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/CLASE.md).

### EWMA

- La EWMA usa `z_t = λ x̄_t + (1−λ) z_{t−1}`.
- La EWMA pondera con `λ = 2/(N + 1)`.

💡 **Cómo se explica en la clase [B84-C35](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md):**
- Shewhart señala en los subgrupos `22, 29, 31, 32, 34, 36, 37`; la EWMA, de forma sostenida desde el `22`.
- Con `ARL₀` iguales (~370), la EWMA detecta desplazamientos pequeños mucho antes que Shewhart.
- 🎯 **Por qué importa:** Un proceso con `Cpk` de 1,33 puede desplazarse 1σ sin dejar piezas fuera de tolerancia durante semanas si solo se inspecciona el producto; la carta lo detecta en pocos subgrupos. La decisión central: ¿qué carta detecta antes un desplazamiento del proceso y qué capacidad tiene el proceso antes y después?

📘 **Dónde se aprende** (2 clases): [B84-C35 · Control de procesos de fabricación y calidad](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md); [B107-C05 · Prevención de lesiones en entrenamiento y trabajo operativo](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md).

### Exacta por definición

- Una constante es un valor que no cambia: exacta por definición (como `c = 299 792 458 m/s` en el SI, S4), medida (como `G`, con incertidumbre) o nominal (valor de conversión fijado por acuerdo, como el `(GM)☉` de la IAU).

🎯 **Por qué importa (clase B03-C12):** La masa del Sol se conoce con unas cinco cifras. Sin embargo, el producto `GM` del Sol se conoce con diez, y la constante `G` por sí sola con apenas cinco.

📘 **Dónde se aprende** (1 clase): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md).

### Exactitud

- La exactitud `(a+d)/N` es la fracción de aciertos totales.
- La exactitud es la fracción de predicciones correctas.
- La exactitud es `(TP + TN)/total`; la precisión, `TP/(TP + FP)`; la exhaustividad (*recall*), `TP/(TP + FN)`; el F1, la media armónica de las dos últimas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C24](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md):**
- La exactitud engaña: un pronóstico «siempre no» tiene `TSS = 0` y una exactitud de `0,899` en los datos sintéticos.
- Exactitud: simple, engañosa con eventos raros.
- ⚠️ **Error frecuente:** Usar la exactitud con eventos raros. Se corrige con 8.3 y el ejercicio 4.
- 🎯 **Por qué importa:** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.

📘 **Dónde se aprende** (4 clases): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md); [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B129-C07 · Proyecto de ciencia ciudadana validable](../programa/clases/B129/B129-C07-proyecto-de-ciencia-ciudadana-validable/CLASE.md).

### Exactitud de medida

- La exactitud de medida es la cercanía entre un valor medido y un valor verdadero del mensurando (S1, 2.13); no es una cantidad, y una medida es «más exacta» cuando su error es menor.

🎯 **Por qué importa (clase B13-C03):** Un telémetro láser que mide la distancia a un reflector de prueba puede dar lecturas muy agrupadas pero todas desplazadas: es repetible y, aun así, está mal. Otro puede dar lecturas dispersas que, en promedio, caen sobre el valor correcto.

📘 **Dónde se aprende** (1 clase): [B13-C03 · Exactitud frente a precisión](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md).

### Exactitud del registro

- La exactitud del registro es la fracción de posiciones cuyo conteo físico coincide con el registro.

🎯 **Por qué importa (clase B100-C01):** Un inventario que solo sabe «cuántas unidades hay» no puede decir de qué lote vienen, cuándo caducan ni dónde se usaron. La decisión central: ¿qué registro mínimo hace falta para emitir primero lo que caduca antes y para encontrar, si un lote resulta defectuoso, adónde fue?

📘 **Dónde se aprende** (1 clase): [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Exactitud global

- La exactitud global es la fracción de aciertos.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- La exactitud global (90,3 %) oculta esa asimetría.
- ⚠️ **Error frecuente:** Reportar solo la exactitud global. Se corrige con los ejercicios 5, 6 y 9.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Exacto

- Una constante definitoria es una constante física a la que el SI asigna un valor numérico exacto; las unidades se definen fijándola (S2).
- Un valor exacto no tiene incertidumbre porque es una definición; un valor medido sí la tiene.

💡 **Cómo se explica en la clase [B13-C01](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md):**
- Si el factor es exacto (`1 km = 10³ m`), el resultado conserva todas las cifras del dato.
- El parámetro gravitacional geocéntrico del IERS (S3, Tabla 1.1) `3,986 004 418 × 10¹⁴ m³/s²` equivale a `398 600,4418 km³/s²` porque `1 km³ = 10⁹ m³` exacto.
- 🎯 **Por qué importa:** Una señal de radio o de láser viaja a la Luna y regresa. Para decir «la Luna está a 384 400 km» hay que haber acordado qué es un kilómetro, qué es un segundo y a qué velocidad viaja la señal.

📘 **Dónde se aprende** (1 clase): [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md).

### Excedente

- El excedente es `v(N) − Σ v(i)`.

💡 **Cómo se explica en la clase [B125-C04](../programa/clases/B125/B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md):**
- El socio C, que solo no vale nada, recibe `20` porque sin él el excedente cae: el reparto proporcional a lo individual lo dejaría sin nada.
- 🎯 **Por qué importa:** Las empresas espaciales dependen de alianzas con socios de otros países y la clase de gobierno no explica cómo se reparte el valor ni cuánta dependencia se acepta; no está tratado. La decisión central: ¿cómo se reparte de forma justa el excedente de una alianza y cuánta dependencia de un solo socio o país es prudente?

📘 **Dónde se aprende** (1 clase): [B125-C04 · Alianzas y cooperación internacional empresarial](../programa/clases/B125/B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md).

### Excedente público

- El excedente público es el pago del Estado por encima del seguro.

💡 **Cómo se explica en la clase [B127-C03](../programa/clases/B127/B127-C03-seguros-de-responsabilidad-civil-espacial/CLASE.md):**
- Un evento de `800 MUSD` se reparte `500` (seguro), `300` (excedente público) y `0` no cubierto.
- *Descripción textual:* el cuantil `1 − 10⁻⁷` define la MPL; el seguro exigido `S` es su mínimo con el tope de 500; la pérdida de un evento se reparte en seguro, excedente público y resto.
- ⚠️ **Error frecuente:** Tratar el excedente público como un derecho automático. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** La responsabilidad por daños a terceros se asegura aparte y ninguna clase la trataba. La decisión central: ¿cuánto seguro de terceros se exige y quién paga lo que lo supera?

📘 **Dónde se aprende** (1 clase): [B127-C03 · Seguros de responsabilidad civil espacial](../programa/clases/B127/B127-C03-seguros-de-responsabilidad-civil-espacial/CLASE.md).

### Excéntrica

- La excéntrica `E` es el ángulo auxiliar sobre el círculo circunscrito.

💡 **Cómo se explica en la clase [B71-C13](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md):**
- En la órbita excéntrica, un cuarto de vuelta angular se recorre en solo el 3,8 % del período, y `M` correspondiente es `13.74°`.
- Límite: la pista elíptica no explica la anomalía excéntrica, que es una construcción geométrica.
- 🎯 **Por qué importa:** Confundir una anomalía con otra es el error más común al propagar órbitas. La decisión central: ¿cómo conviertes entre `ν`, `E` y `M` sin ambigüedad y cuánto difieren cuando `e` es grande?

📘 **Dónde se aprende** (1 clase): [B71-C13 · Anomalías orbitales](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md).

### Excentricidad

- La excentricidad `e` mide cuánto se aparta la órbita de un círculo (0 es círculo).
- La excentricidad `e` mide su achatamiento: la distancia entre focos es `2ae`.
- La excentricidad `e = c/a` mide cuánto se aleja la elipse de una circunferencia: `e = 0` es una circunferencia y `e` cercano a 1 es una elipse muy alargada.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C13](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md):**
- La ficha de planetas de NASA (actualizada el 18 de marzo de 2025) tabula masa, diámetro, densidad, período orbital, distancia al Sol, excentricidad y número de lunas para los ocho planetas y Plutón (S1).
- 🎯 **Por qué importa:** Se dice que el sistema solar «está vacío», y es verdad en un sentido preciso: si el Sol midiera 9 mm, la Tierra sería un grano de 0,085 mm a un metro de distancia, y la estrella más cercana quedaría a más de 260 km. Pero esa imagen solo se entiende si la construyes tú con números.

📖 **Explicado a fondo:** [Excentricidad](esencial/esencial-d-l.md#excentricidad) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (9 clases): [B01-C13 · Sistema solar como sistema físico](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md); [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B26-C08 · Geodésicas gravitacionales](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md) y 3 más.

### Excentricidad congelada

- La excentricidad congelada `e_f` cumple `ω̇_J2 + ω̇_J3 = 0`.

💡 **Cómo se explica en la clase [B72-C14](../programa/clases/B72/B72-C14-orbitas-congeladas/CLASE.md):**
- A `700 km` y `98,188°` (heliosíncrona), la excentricidad congelada con `ω = 90°` vale `0,001046`, y la raíz numérica de las ecuaciones de Gauss con J2 y J3 coincide (`0,00 %` en cuatro cifras).
- Descripción larga: La excentricidad congelada es del orden de 10⁻³ y depende de la razón J3/(2 J2); el efecto de J3 invierte el signo del giro del perigeo para excentricidades mayores que la congelada.
- 🎯 **Por qué importa:** Un altímetro o un radar que observa la misma traza necesita pasar por cada latitud a la misma altitud; si el perigeo girara, la altitud sobre un punto cambiaría decenas de kilómetros. La decisión central: ¿qué excentricidad y argumento del perigeo congelan la órbita para una inclinación y altitud dadas?

📘 **Dónde se aprende** (1 clase): [B72-C14 · Órbitas congeladas](../programa/clases/B72/B72-C14-orbitas-congeladas/CLASE.md).

### Excentricidad forzada

- La excentricidad forzada es el vector de excentricidad que crece por una fuerza casi constante.

💡 **Cómo se explica en la clase [B72-C08](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md):**
- La aceleración es `10⁻⁸`–`10⁻⁶ m/s²`, minúscula frente a `0,22 m/s²` de la gravedad en GEO, pero sin freno acumula el desplazamiento: en un año la excentricidad forzada sin compensación llegaría a décimas de milésima por mes.
- 🎯 **Por qué importa:** En órbita geoestacionaria no hay arrastre, y el empuje solar domina las maniobras de mantenimiento de un satélite con paneles grandes; en una vela solar es el propulsor. La decisión central: ¿cuánto vale la aceleración por presión de radiación y cuánto deforma una órbita alta en semanas?

📘 **Dónde se aprende** (1 clase): [B72-C08 · Presión de radiación solar](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md).

### Excentricidad hiperbólica

- La excentricidad hiperbólica es `e = 1 + r v_inf²/GM_L`.

🎯 **Por qué importa (clase B76-C07):** Un diseño preliminar de misión empieza por el presupuesto de velocidad. La decisión central: ¿cuánto `Δv` cuestan la salida de la Tierra y la captura en la Luna, y cuánto cambia la segunda según la órbita lunar elegida?

📘 **Dónde se aprende** (1 clase): [B76-C07 · Maniobras de inserción cislunar](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md).

### Excéntrico

- Un excéntrico y un epiciclo son dos recursos geométricos para describir el movimiento de un cuerpo (C10).

🎯 **Por qué importa (clase B02-C03):** Un modelo geométrico responde a «¿qué figura reproduce estos movimientos?». Es una forma nueva de preguntar frente a la regla puramente numérica.

📘 **Dónde se aprende** (1 clase): [B02-C03 · Astronomía griega y helenística](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md).

### Excepción

- Un error de sintaxis ocurre cuando el código no es Python válido, antes de ejecutarse; una excepción ocurre durante la ejecución y puede tratarse (S2, §8.1–8.2).

💡 **Cómo se explica en la clase [B07-C12](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md):**
- Una excepción es una alarma que sube por la pila de llamadas hasta que alguien la atiende.
- La función que lee el CSV puede atender la excepción con `try/except`, anotando la línea y el motivo y siguiendo con la fila siguiente; si no la atiende, la excepción sube hasta el programa principal y lo detiene mostrando la traza.
- 🎯 **Por qué importa:** Un programa científico recibe archivos con huecos, texto donde esperaba un número y valores imposibles (un período negativo). Hay dos malas respuestas: dejar que el programa se caiga sin explicar nada y, peor, seguir en silencio con un valor inválido (`nan`, `0`) que contamina el resultado final.

📘 **Dónde se aprende** (1 clase): [B07-C12 · Manejo de errores y excepciones](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md).

### Excepción propia

- Una excepción propia es una clase que heredas de otra (aquí `DatoInvalido(ValueError)`).

🎯 **Por qué importa (clase B07-C12):** Un programa científico recibe archivos con huecos, texto donde esperaba un número y valores imposibles (un período negativo). Hay dos malas respuestas: dejar que el programa se caiga sin explicar nada y, peor, seguir en silencio con un valor inválido (`nan`, `0`) que contamina el resultado final.

📘 **Dónde se aprende** (1 clase): [B07-C12 · Manejo de errores y excepciones](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md).

### Exceso

- Un exceso es la diferencia entre lo observado y `b`.

💡 **Cómo se explica en la clase [B31-C16](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md):**
- *Descripción textual:* el campo y el tamaño fijan la energía máxima; el decaimiento del pion da la fracción del neutrino; el flujo y el área dan el número de eventos y la probabilidad de un exceso.
- 🎯 **Por qué importa:** Para decir si una fuente puede producir rayos cósmicos de cierta energía y cuántos neutrinos habría, se necesitan estimaciones cuantitativas. La decisión central: ¿hasta qué energía acelera una fuente y cuántos eventos se esperan?

📘 **Dónde se aprende** (1 clase): [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md).

### Exceso angular

- El exceso angular de un triángulo es la suma de sus ángulos menos `π`, y vale `K A`, con `A` el área.

🎯 **Por qué importa (clase B26-C07):** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### Exceso de energía

- La falta de fusión ocurre con `E_v` bajo y el exceso de energía (ojo de cerradura) con `E_v` alto.

🎯 **Por qué importa (clase B84-C15):** Dos piezas idénticas con otra velocidad de barrido pueden salir porosas; una ventana de proceso bien trazada evita el desperdicio, y la rugosidad escalonada decide qué superficies se mecanizan. La decisión central: ¿con qué potencia y velocidad se imprime dentro de la ventana y cuánto tarda y qué acabado deja?

📘 **Dónde se aprende** (1 clase): [B84-C15 · Manufactura aditiva](../programa/clases/B84/B84-C15-manufactura-aditiva/CLASE.md).

### Exceso de pérdida

- El exceso de pérdida (*per risk*) paga por siniestro `min(max(X − P, 0), L)`, con prioridad `P` y límite `L`.

💡 **Cómo se explica en la clase [B127-C07](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md):**
- La cuota parte lo hace barato porque la comisión es generosa (dato sintético); el exceso de pérdida lo hace caro pero solo protege contra siniestros grandes, como los que dominan este tipo de cartera, y deja intacta la frecuencia de los pequeños.
- X --> E["exceso de pérdida: paga min(max(X - P, 0), L)"]
- 🎯 **Por qué importa:** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Exceso de velocidad hiperbólica

- El exceso de velocidad hiperbólica `v∞` es la velocidad lejos del cuerpo.

🎯 **Por qué importa (clase B71-C09):** Las trayectorias de escape y de sobrevuelo son hipérbolas respecto del cuerpo local. La decisión central: ¿qué velocidad en el periapsis produce un exceso `v∞` dado y cuánto se desvía la trayectoria?

📘 **Dónde se aprende** (1 clase): [B71-C09 · Órbitas parabólicas e hiperbólicas](../programa/clases/B71/B71-C09-orbitas-parabolicas-e-hiperbolicas/CLASE.md).

### Exceso enantiomérico

- El exceso enantiomérico es `ee = (L−D)/(L+D)`.

💡 **Cómo se explica en la clase [B55-C17](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md):**
- *Descripción textual:* la tasa y el tiempo dan la dosis, de la que sale la supervivencia; en paralelo, el número de moléculas contadas fija la incertidumbre del exceso enantiomérico.
- Un aminoácido hipotético con dosis característica `D₀ = 10⁶ Gy` y tasa de dosis de `10⁻³ Gy/año` (ambas ilustrativas), y una proporción verdadera de forma L de 0,55 (exceso enantiomérico 0,10).
- 🎯 **Por qué importa:** Que un compuesto prebiótico llegue intacto hasta nosotros depende de cuánta radiación recibió, y que un exceso entre dos formas quirales sea real depende de cuántas moléculas se contaron. La decisión central: ¿cuánto sobrevive y con qué incertidumbre puedo afirmar un exceso enantiomérico distinto de cero?

📘 **Dónde se aprende** (1 clase): [B55-C17 · Compuestos prebióticos](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md).

### Exceso hiperbólico

- El exceso hiperbólico `v∞` es lo que sobra tras escapar.
- El exceso hiperbólico `v∞` es la velocidad respecto a la Tierra lejos de ella.

🎯 **Por qué importa (clase B71-C15):** La velocidad de escape es el umbral entre una órbita cerrada y una trayectoria abierta. La decisión central: ¿qué velocidad hay que alcanzar para no volver y cuánto la reduce partir de una altura o de una superficie que gira?

📘 **Dónde se aprende** (2 clases): [B71-C15 · Velocidad de escape](../programa/clases/B71/B71-C15-velocidad-de-escape/CLASE.md); [B75-C23 · Energía característica C3 y exceso hiperbólico](../programa/clases/B75/B75-C23-energia-caracteristica-c3-y-exceso-hiperbolico/CLASE.md).

### Exceso hiperbólico de velocidad

- El exceso hiperbólico de velocidad `v∞` es la velocidad de la nave respecto al planeta, lejos de él: aquí, la diferencia entre la velocidad heliocéntrica de la nave y la del planeta.

🎯 **Por qué importa (clase B75-C01):** Para ir a Marte no se apunta a donde está Marte: se elige una elipse alrededor del Sol que toque la órbita de la Tierra al salir y la de Marte al llegar. La decisión central: ¿cuál es la elipse de menor energía que une dos órbitas circulares, cuánto dura el viaje y qué velocidad exige a la salida y a la llegada?

📘 **Dónde se aprende** (1 clase): [B75-C01 · Geometría de transferencias heliocéntricas](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md).

### Exclusión

- La exclusión deja sin pago un evento.

💡 **Cómo se explica en la clase [B127-C04](../programa/clases/B127/B127-C04-exclusiones-deducibles-y-limites-de-polizas/CLASE.md):**
- La exclusión y el coaseguro actúan multiplicando: `0,9 × 0,8 = 0,72` sobre el pago de C.
- Paso 1 · Exclusión. Si el evento no está excluido, continúa.
- 🎯 **Por qué importa:** Leer una póliza exige entender sus exclusiones, deducibles y límites; el catálogo no lo trataba. La decisión central: ¿qué parte de la pérdida retiene el asegurado y cómo cambia el precio al cambiar las condiciones?

📘 **Dónde se aprende** (1 clase): [B127-C04 · Exclusiones, deducibles y límites de pólizas](../programa/clases/B127/B127-C04-exclusiones-deducibles-y-limites-de-polizas/CLASE.md).

### Exclusiva

- La licencia exclusiva se da a un solo licenciatario; la no exclusiva, a varios.

💡 **Cómo se explica en la clase [B124-C09](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md):**
- Exclusiva: un licenciatario con ventas 1,6 veces mayores, regalía de 6 % y cuota de 5 Mum, vale `45,997` Mum para el licenciante.
- No exclusiva: tres licenciatarios, regalía de 4 % y cuota de 1 Mum cada uno, valen `54,247` Mum.
- ⚠️ **Error frecuente:** Suponer que la exclusiva siempre vale más. Se corrige con 8.3–8.4.
- 🎯 **Por qué importa:** La propiedad intelectual es un activo, pero su valor depende de cuánto se vende con ella y de cuánto del margen se queda el que la usa. La decisión central: ¿qué licencia conviene ofrecer y cuántas regalías soporta el licenciatario?

📘 **Dónde se aprende** (1 clase): [B124-C09 · Propiedad intelectual y licencias](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md).

### Exhaustiva

- La exhaustiva requiere `2ⁿ`.

💡 **Cómo se explica en la clase [B88-C39](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md):**
- Descripción larga: MC/DC cuesta el doble de la cobertura de decisión y la mitad de la exhaustiva en este caso.
- 🎯 **Por qué importa:** Elegir el nivel de cobertura determina el esfuerzo de prueba. La decisión central: ¿qué cobertura piden los distintos niveles y cuánto cuesta cada una en pruebas?

📘 **Dónde se aprende** (1 clase): [B88-C39 · Normas de aseguramiento de software (ECSS, DO-178C)](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md).

### Exhaustividad

- La exhaustividad (*recall*, sensibilidad, tasa de verdaderos positivos) es `TP/(TP + FN)`: de los reales, cuántos se encontraron (S2).
- La exactitud es `(TP + TN)/total`; la precisión, `TP/(TP + FP)`; la exhaustividad (*recall*), `TP/(TP + FN)`; el F1, la media armónica de las dos últimas.
- La precisión es `TP/(TP + FP)`, la exhaustividad `TP/(TP + FN)` y `F1 = 2PR/(P + R)`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Precisión `3/(3 + 1) = 0,75`; exhaustividad `3/(3 + 2) = 0,6`;
- Con `β = 2` (más peso a la exhaustividad): `F₂ = 5(0,75)(0,6)/(4 × 0,75 + 0,6) = 2,25/3,6 = 0,625`; con `β = 0,5`: `F₀,₅ = 1,25 × 0,45/(0,25 × 0,75 + 0,6) = 0,714`.
- ⚠️ **Error frecuente:** Confiar en el AUC sin mirar precisión–exhaustividad. Ejercicio 5.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.

📘 **Dónde se aprende** (5 clases): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md); [B104-C03 · Selección y aptitud](../programa/clases/B104/B104-C03-seleccion-y-aptitud/CLASE.md); [B119-C07 · Registro nacional de objetos](../programa/clases/B119/B119-C07-registro-nacional-de-objetos/CLASE.md).

### Existencias de seguridad

- Las existencias de seguridad cubren la variación.

🎯 **Por qué importa (clase B104-C21):** Quedarse sin un consumible a bordo no se arregla enviando a alguien a comprarlo. La decisión central: ¿con qué punto de reorden se pide para que el faltante sea raro, y cuánto volumen cuesta guardar lo pedido?

📘 **Dónde se aprende** (1 clase): [B104-C21 · Inventario, logística y estiba a bordo](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md).

### Exitancia

- La exitancia `M` es la potencia emitida por área (`π B` si es lambertiana).

💡 **Cómo se explica en la clase [B45-C01](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md):**
- Con `x = hc/(λkT)`, la exitancia es `2π k⁴T⁴/(h³c²) ∫ x³/(eˣ − 1) dx`.
- Como el agua: la radiancia es el chorro por unidad de sección y ángulo; la exitancia, el caudal total del grifo por área; la irradiancia, lo que cae sobre una hoja de papel a cierta distancia.
- ⚠️ **Error frecuente:** Olvidar el factor `π` entre radiancia y exitancia. Se corrige con 8.2.
- 🎯 **Por qué importa:** Todo flujo medido en un telescopio es una cantidad radiométrica o fotométrica con una definición precisa; confundir vatios, lúmenes y fotones arruina la calibración. La decisión central: ¿en qué unidades se expresa lo que llega al detector y cómo se pasa de una a otra?

📘 **Dónde se aprende** (1 clase): [B45-C01 · Radiometría y fotometría](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md).

### Exitancia espectral

- La exitancia espectral de Planck es `M_λ = 2πhc²/(λ⁵(e^(hc/λkT) − 1))`.

🎯 **Por qué importa (clase B85-C04):** La mitad del control térmico es elegir cuánto emite o absorbe cada superficie. La decisión central: ¿cuánto calor intercambian dos superficies y cómo lo cambia poner una emisividad baja entre ellas?

📘 **Dónde se aprende** (1 clase): [B85-C04 · Radiación térmica de superficies](../programa/clases/B85/B85-C04-radiacion-termica-de-superficies/CLASE.md).

### Éxito

- El éxito es un mejor valor menor que `10⁻³`.
- El éxito exige residuo relativo `< 10⁻⁸`.

💡 **Cómo se explica en la clase [B81-C13](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md):**
- *Descripción textual:* la misma función se resuelve con tres métodos, cada uno repetido con 30 semillas; se comparan la tasa de éxito y las evaluaciones.
- Por éxito: fracción que alcanza el mínimo.
- 🎯 **Por qué importa:** Un método heurístico no garantiza el óptimo, pero puede evitar los mínimos locales. La decisión central: ¿qué método global elegir y cuántas evaluaciones se gastan para una tasa de éxito dada?

📘 **Dónde se aprende** (2 clases): [B81-C13 · Optimización heurística (algoritmos genéticos y enjambres)](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md); [B82-C07 · Benchmark entre solucionadores de Lambert](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md).

### Éxito de la maniobra

- Recalibración: actualizar los parámetros del gemelo. Éxito de la maniobra: error menor que el umbral.

🎯 **Por qué importa (clase B101-C08):** Una reparación robótica no se improvisa: se ensaya. Pero un ensayo vale solo si el gemelo se parece a la realidad.

📘 **Dónde se aprende** (1 clase): [B101-C08 · Gemelo digital para ensayo de reparaciones robóticas](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md).

### Exobase

- El exobase es la altura sobre la cual las colisiones son raras.
- La exobase es la altura sobre la cual las colisiones son raras.

💡 **Cómo se explica en la clase [B54-C11](../programa/clases/B54/B54-C11-escape-atmosferico/CLASE.md):**
- Límite: los corredores no chocan entre sí; las moléculas del exobase casi no lo hacen, pero la atmósfera debajo sí.
- Temperaturas de exobase sintéticas: 1000 K para la Tierra y 200 K para Marte y Venus.
- ⚠️ **Error frecuente:** Usar el radio de la superficie como si fuera el del exobase. Se corrige con la sección 10: es una aproximación declarada.
- 🎯 **Por qué importa:** Por qué la Tierra retiene el N₂ pero pierde el H depende de una razón entre energías. La pregunta motivadora: ¿qué especies puede retener un planeta a cierta temperatura?

📘 **Dónde se aprende** (2 clases): [B54-C11 · Escape atmosférico](../programa/clases/B54/B54-C11-escape-atmosferico/CLASE.md); [B56-C11 · Atmósfera y superficie de Titán](../programa/clases/B56/B56-C11-atmosfera-y-superficie-de-titan/CLASE.md).

### Exotérmico

- En modo endotérmico (`V < E_tn`) la celda absorbe calor; en exotérmico (`V > E_tn`) lo cede.

🎯 **Por qué importa (clase B59-C10):** La electrólisis es el mayor consumidor de energía de la planta. La decisión central: ¿a qué densidad de corriente conviene operar, entre una celda pequeña que gasta más electricidad y una grande que gasta menos?

📘 **Dónde se aprende** (1 clase): [B59-C10 · Electrólisis y balances energéticos](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md).

### Expandida

- La incertidumbre combinada es la raíz de la suma cuadrática de los términos independientes; la expandida la multiplica por un factor de cobertura `k` (aquí 2).

💡 **Cómo se explica en la clase [B91-C05](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir incertidumbre combinada con expandida. Ver la sección 6.
- 🎯 **Por qué importa:** Una antena se acepta si su ganancia y su patrón medidos cumplen la especificación dentro de una incertidumbre conocida. La decisión central: ¿a qué distancia medir y con qué incertidumbre, para poder afirmar que la antena cumple?

📘 **Dónde se aprende** (1 clase): [B91-C05 · Medición y calibración de antenas](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md).

### Expansión

- La expansión del universo es el aumento de las distancias entre galaxias no ligadas.
- La expansión produce `n` bytes con `T(i) = HMAC(PRK, T(i−1) ‖ info ‖ i)`.

🎯 **Por qué importa (clase B01-C16):** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).

📘 **Dónde se aprende** (2 clases): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md); [B88-C38 · Gestión de claves y secretos en aviónica](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md).

### Expansión de Prandtl–Meyer

- Una expansión de Prandtl–Meyer es el giro continuo de un flujo supersónico alrededor de una esquina convexa.

💡 **Cómo se explica en la clase [B79-C06](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md):**
- La expansión de Prandtl–Meyer es isentrópica: no hay pérdida de presión total, a diferencia del choque (C07).
- 🎯 **Por qué importa:** El comportamiento de un flujo a `M > 1` en toberas y vehículos no lo trata ninguna clase del tronco. Sin él no se entiende por qué una tobera necesita una parte divergente.

📘 **Dónde se aprende** (1 clase): [B79-C06 · Flujos supersónicos](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md).

### Expansión por cofactores

- El determinante de `[[a, b], [c, d]]` es `ad − bc`; el de una matriz `3×3` se obtiene por expansión por cofactores: se desarrolla por una fila sumando cada elemento por el determinante de la submatriz que queda al tachar su fila y columna, con signo alterno (S1, §1.3(i), ecs. 1.3.1–1.3.4).

🎯 **Por qué importa (clase B10-C04):** Dos estaciones terrestres miden la dirección hacia un mismo objeto y quieren fijar su posición cruzando las visuales. Si el objeto está cerca y las visuales forman un buen ángulo, el cruce es nítido.

📘 **Dónde se aprende** (1 clase): [B10-C04 · Determinantes y soluciones](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md).

### Expectativa de gas uniforme

- La expectativa de gas uniforme estima los pares por razón de volúmenes.

🎯 **Por qué importa (clase B118-C15):** La sección 5.5 de la IADC Rev. 4 pide planificar y operar las constelaciones para minimizar la probabilidad de colisión entre sus miembros, en los cruces de planos y con otras constelaciones, y minimizar el riesgo acumulado de reentradas.

📘 **Dónde se aprende** (1 clase): [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md).

### Expediente

- El expediente es el conjunto de documentos y datos de un trámite.

💡 **Cómo se explica en la clase [B120-C04](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md):**
- El expediente base tiene 0 faltantes (100 %).
- *Descripción textual:* el expediente se compara con el esquema (completitud) y consigo mismo (coherencia); la mutación prueba al verificador.
- 🎯 **Por qué importa:** El expediente regulatorio es un entregable del rol; B90-C05 documenta interfaces, no trámites regulatorios.

📘 **Dónde se aprende** (1 clase): [B120-C04 · Documentación regulatoria de un sistema satelital](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md).

### Experimento aleatorio

- Un experimento aleatorio es un proceso cuyo resultado no se puede predecir con certeza aunque se conozcan sus condiciones.

🎯 **Por qué importa (clase B12-C01):** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.

📘 **Dónde se aprende** (1 clase): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md).

### Explicabilidad

- Aporte: `log₁₀` de la razón de verosimilitud de un síntoma. Explicabilidad: capacidad de justificar una conclusión.

🎯 **Por qué importa (clase B96-C21):** C13 detecta que algo anda mal; esta clase responde por qué la máquina cree lo que cree. La decisión central: ¿qué hipótesis es la más probable y qué evidencia la sostiene, de modo que un operador pueda aceptarla o refutarla?

📘 **Dónde se aprende** (1 clase): [B96-C21 · Diagnóstico explicable de anomalías](../programa/clases/B96/B96-C21-diagnostico-explicable-de-anomalias/CLASE.md).

### Explícita

- Una relación explícita da `y` en función de `x`; una implícita la define mediante `F(x, y) = 0` (S1, §1.5(i)).

🎯 **Por qué importa (clase B09-C06):** Para saber dónde está un planeta en su órbita en un instante dado hay que resolver la ecuación de Kepler, `M = E − e sin E`, que no tiene solución en funciones elementales: no se puede despejar `E`.

📘 **Dónde se aprende** (1 clase): [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md).

### Explícito

- Un método explícito calcula el nuevo estado solo con valores ya conocidos.

🎯 **Por qué importa (clase B11-C06):** Una evaluación de `F` en un cálculo de trayectorias es cara cuando incluye gravedad de varios cuerpos o un modelo de atmósfera. La pregunta práctica es siempre cuánta precisión compra cada evaluación.

📘 **Dónde se aprende** (1 clase): [B11-C06 · Método de Heun](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md).

### Exploratorio

- Un análisis confirmatorio sigue el plan; uno exploratorio no.
- El análisis confirmatorio prueba lo especificado antes; el exploratorio busca patrones sin plan previo (S1).

💡 **Cómo se explica en la clase [B14-C23](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md):**
- No prohíbe lo exploratorio (S1): permite explorar si se etiqueta.
- E --> X["Resultado exploratorio<br/>declarado como tal"]
- ⚠️ **Error frecuente:** Ocultar lo exploratorio. Se corrige con los ejercicios 3 y 10.
- 🎯 **Por qué importa:** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.

📘 **Dónde se aprende** (2 clases): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md).

### Exponencial

- El modelo exponencial es `BMD(t) = BMD₀ (1 − r)^t` y el lineal `BMD₀ (1 − r t)`, con `t` en meses.

💡 **Cómo se explica en la clase [B105-C02](../programa/clases/B105/B105-C02-perdida-de-masa-osea/CLASE.md):**
- El exponencial da menos pérdida acumulada que el lineal porque cada mes se pierde una fracción del saldo restante; a 12 meses la diferencia es 0,99 puntos con `r = 1,25 %`.
- R --> M["modelo exponencial<br/>o lineal"]
- 🎯 **Por qué importa:** Un porcentaje por mes parece simple, pero hay que decidir cómo se acumula (lineal o exponencial), para quién vale (promedio o individuo) y qué recupera el cuerpo al volver. La decisión central: ¿qué pérdida esperar a 6 y 12 meses, con qué dispersión y qué parte se recupera?

📘 **Dónde se aprende** (1 clase): [B105-C02 · Pérdida de masa ósea](../programa/clases/B105/B105-C02-perdida-de-masa-osea/CLASE.md).

### Exponencial matricial

- La exponencial matricial es `exp(A t) = Σ (A t)ᵏ/k!`; si `A = V Λ V⁻¹`, entonces `exp(A t) = V exp(Λ t) V⁻¹`.
- La exponencial matricial `e^(At)` se define con la serie `I + At + (At)²/2! + …`.

🎯 **Por qué importa (clase B10-C09):** Un panel solar largo y delgado vibra después de una maniobra. Si la vibración se amortigua, el panel es estable; si crece, hay un problema serio.

📘 **Dónde se aprende** (2 clases): [B10-C09 · Diagonalización y estabilidad](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md); [B16-C02 · Representaciones en espacio de estados](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md).

### Exponente

- `a` es la base y `n` el exponente.
- La mantisa `m` cumple `1 ≤ |m| < 10` en la forma normalizada; el exponente `e` es un entero.
- El exponente es `β = (1/m₁₆ − 1/m₁₇)/(1/m₁₆ − 1/m₁₈)`.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Con exponente fraccionario (`a1.5`) es directo y cabe en una línea.
- Ninguno es mejor siempre: para ver el principio, descompone; para calcular muchos casos, usa el exponente.
- ⚠️ **Error frecuente:** Multiplicar la base por el exponente (`2⁵ = 10`).
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.

📘 **Dónde se aprende** (3 clases): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md); [B03-C05 · Notación científica y órdenes de magnitud](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md); [B55-C13 · Isótopos como trazadores](../programa/clases/B55/B55-C13-isotopos-como-trazadores/CLASE.md).

### Exponente de acoplamiento

- `π₂ = g a/U²` es el grupo adimensional de gravedad. μ es el exponente de acoplamiento entre energía y momento.

🎯 **Por qué importa (clase B61-C01):** Para leer un cráter hay que invertir la pregunta: del tamaño observado al proyectil. Sin las leyes de escalado no hay estimación de energía ni de la cantidad de material que sale despedido.

📘 **Dónde se aprende** (1 clase): [B61-C01 · Dinámica de eyección y escalado de cráteres](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md).

### Exponente de Ångström

- El exponente de Ångström `α` ajusta `τ ∝ λ^{−α}`; valores altos indican partículas pequeñas.

💡 **Cómo se explica en la clase [B57-C13](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md):**
- *Descripción textual:* el espesor óptico determina la transmitancia, el exponente de Ångström y, cuando es pequeño, la reflectancia dispersada, mientras el ruido de medición se propaga al exponente.
- Una columna de aire con `AOD(550 nm) = 0,30` y exponente de Ångström `1,3` (ambos ilustrativos) se mide en `440` y `870 nm` con un ruido de `0,01`.
- 🎯 **Por qué importa:** Un satélite que mira un incendio, un volcán o el mar tiene que descontar la atmósfera, y los aerosoles son lo más variable. La decisión central: ¿cuánto aerosol hay y qué tipo, con qué incertidumbre, a partir de pocas longitudes de onda?

📘 **Dónde se aprende** (1 clase): [B57-C13 · Atmósfera y aerosoles](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md).

### Exponente de Lyapunov máximo

- El exponente de Lyapunov máximo es `λ = lim (1/n) ln(|δ_n|/|δ_0|)`.

🎯 **Por qué importa (clase B73-C14):** El exponente de Lyapunov es el número que cuantifica el caos: fija el horizonte de predicción y distingue una trayectoria regular de una caótica. En un espacio de fases mixto, un solo exponente no basta.

📘 **Dónde se aprende** (1 clase): [B73-C14 · Exponentes de Lyapunov](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md).

### Exponente de temperatura

- El exponente de temperatura `ν` es el valor de `d ln(tasa)/d ln T`.

🎯 **Por qué importa (clase B24-C07):** Dos protones se repelen con una fuerza eléctrica enorme; a las temperaturas de una estrella casi ninguno tiene energía para acercarse lo suficiente. Aun así la fusión ocurre, por efecto túnel.

📘 **Dónde se aprende** (1 clase): [B24-C07 · Ciclo CNO y cadena protón-protón](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md).

### Exponente de transporte

- El exponente de transporte `α` cumple `⟨(Δp)²⟩ ∝ n^α`: `α = 1` es difusión normal, `α = 2` es balístico.

🎯 **Por qué importa (clase B73-C15):** Un conjunto de cuerpos en una región caótica no escapa de golpe: su excentricidad o su semieje se esparce como una caminata aleatoria, y el tiempo que tarda en recorrer una región fija la escala de supervivencia de la población. La decisión central: ¿cómo medir un coeficiente de difusión y cuándo no tiene sentido hablar de él?

📘 **Dónde se aprende** (1 clase): [B73-C15 · Difusión orbital](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md).

### Exponente Doppler

- El exponente Doppler `p` de `δ^p`.

💡 **Cómo se explica en la clase [B28-C12](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md):**
- Esta clase no ajusta ninguna observación: con `Γ = 100`, `θ_c = 0,1 rad` y exponente Doppler `3` (ilustrativos) calcula cómo cae el brillo con el ángulo de visión.
- 🎯 **Por qué importa:** Un destello gamma débil puede ser un evento normal visto de lado. Un modelo de emisión conjunta permite relacionar qué se ve en cada mensajero con el ángulo de visión.

📘 **Dónde se aprende** (1 clase): [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md).

### Exponente fraccionario

- Un exponente fraccionario como `3/2` combina una potencia y una raíz.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Con exponente fraccionario (`a1.5`) es directo y cabe en una línea.
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.

📘 **Dónde se aprende** (1 clase): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md).

### Exponente inestable

- `λ` es el exponente inestable real, `ω` la frecuencia en el plano y `ν = √c2` la frecuencia vertical.

🎯 **Por qué importa (clase B76-C04):** Una órbita halo no es un círculo: es un compromiso entre un modo inestable y dos oscilaciones. La decisión central: ¿qué dicen los modos lineales de `L2` sobre el tiempo de crecimiento de un error y sobre los periodos de la órbita?

📘 **Dónde se aprende** (1 clase): [B76-C04 · Órbitas halo](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md).

### Exportación

- La exportación es el envío de un artículo o la transferencia de tecnología a un destino extranjero.

💡 **Cómo se explica en la clase [B125-C05](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md):**
- Se controlan objetos, pero también tecnología: según el Reglamento 2021/821, enviar por correo, subir a un servicio en línea o describir por teléfono una tecnología a alguien fuera de la UE cuenta como exportación.
- 🎯 **Por qué importa:** La tecnología espacial está sujeta a controles de exportación que condicionan el negocio, y las alianzas de la clase anterior chocan con ellos; ninguna clase los trata. La decisión central: ¿qué ruta de exportación debe esperar un producto o una transferencia de tecnología y cuánto cuesta, en promedio, esperar la licencia?

📘 **Dónde se aprende** (1 clase): [B125-C05 · Control de exportaciones y transferencia de tecnología](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md).

### Exposición

- La exposición es el tiempo de captura.
- La exposición es el tiempo con el obturador abierto; el ISO es la amplificación de la señal; la apertura relativa del objetivo (f/) controla la luz.
- La amenaza es la probabilidad e intensidad del fenómeno; la exposición es lo que está en su camino; la vulnerabilidad es cuán dañable es.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C17](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md):**
- En una exposición, lo que se acumula es luz: un objeto de la mitad de brillo necesita el doble de tiempo para dejar la misma marca (aproximación válida mientras la placa responda de forma lineal, lo que no siempre ocurre con las emulsiones antiguas).
- Una fotografía es un dato si se registran fecha, hora, instrumento, exposición y placa.
- 🎯 **Por qué importa:** Un dibujo depende de quien lo hace; una placa registra lo que llegó. La pregunta motivadora es: ¿qué cambia cuando la observación puede guardarse, compararse años después y medirse?

📘 **Dónde se aprende** (4 clases): [B02-C17 · Nacimiento de la astrofotografía](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md); [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md); [B57-C19 · SIG y análisis de riesgo](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md); [B127-C05 · Evaluación actuarial básica del riesgo espacial](../programa/clases/B127/B127-C05-evaluacion-actuarial-basica-del-riesgo-espacial/CLASE.md).

### Exposición característica

- `E₀` es la exposición característica.

🎯 **Por qué importa (clase B85-C14):** Un recubrimiento que cumple al inicio puede salirse del intervalo con la exposición. La decisión central: ¿cuánto sube `α` y cuánto sube la temperatura al final de la misión, y qué incertidumbre trae el ajuste?

📘 **Dónde se aprende** (1 clase): [B85-C14 · Degradación ultravioleta](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md).

### Exposición de neutrones

- La exposición de neutrones `τ = ∫ σ n_n v dt` mide cuántas capturas ocurren por núcleo.

🎯 **Por qué importa (clase B24-C21):** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.

📘 **Dónde se aprende** (1 clase): [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### Exposición esperada

- La exposición esperada es `p×impacto`.

💡 **Cómo se explica en la clase [B83-C16](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md):**
- La exposición esperada es `Σ p·d = 89,35` días, mayor que la reserva de 60 días: en media la reserva no alcanza.
- Exposición esperada (esta clase): suma lineal.
- 🎯 **Por qué importa:** Una lista de riesgos sin números no dice cuánta reserva hace falta ni qué mitigar primero. La decisión central: ¿qué riesgos mitigar primero y alcanza la reserva de calendario para los que no se mitiguen?

📘 **Dónde se aprende** (1 clase): [B83-C16 · Gestión de riesgos técnicos](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md).

### Exposición limitada por el cielo

- La exposición limitada por el cielo es aquella en que el fondo supera con holgura a la lectura.

🎯 **Por qué importa (clase B44-C11):** Exponer poco multiplica el ruido de lectura; exponer mucho arriesga la saturación. La decisión central: ¿cuánto debe durar cada cuadro dentro de un tiempo total dado?

📘 **Dónde se aprende** (1 clase): [B44-C11 · Tiempo de exposición](../programa/clases/B44/B44-C11-tiempo-de-exposicion/CLASE.md).

### Expresión

- Una expresión es una cadena de números y operaciones.
- Una expresión es una combinación de valores, variables y operadores que Python evalúa a un valor: `2 + 3 * 4` evalúa a `14`.

💡 **Cómo se explica en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- Esta convención existe para que todas las personas lean igual una misma expresión; no es una ley de la naturaleza, es un acuerdo, como el idioma.
- Piensa en una expresión como una receta con pasos ordenados.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.

📘 **Dónde se aprende** (2 clases): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md); [B07-C03 · Operadores y expresiones](../programa/clases/B07/B07-C03-operadores-y-expresiones/CLASE.md).

### Expresión algebraica

- Una expresión algebraica combina números, variables y operaciones (`a₁ + a₂`).

🎯 **Por qué importa (clase B03-C13):** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.

📘 **Dónde se aprende** (1 clase): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md).

### Extensión

- Una extensión (`.csv`) es el sufijo del nombre.

💡 **Cómo se explica en la clase [B07-C15](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md):**
- El laboratorio imprime la ruta relativa a la raíz del repositorio, el nombre, la extensión y la carpeta del CSV; y comprueba las diferencias Windows/POSIX con rutas «puras».
- 🎯 **Por qué importa:** Una causa muy común de «el programa no encuentra el archivo» es que la ruta funciona en el computador del autor y no en otro: se escribió con `C:\Usuarios\ana\datos\...`, o se asumió que el programa se ejecuta desde cierta carpeta.

📘 **Dónde se aprende** (1 clase): [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md).

### Extensión de reacción

- La extensión de reacción `p` es la probabilidad de que un extremo haya reaccionado.

🎯 **Por qué importa (clase B56-C21):** C03 trata el origen de autorreplicantes, pero ninguna clase trata la polimerización experimental y sus límites. Antes de que un replicador pueda copiarse, hay que formar cadenas lo bastante largas.

📘 **Dónde se aprende** (1 clase): [B56-C21 · Polimerización prebiótica experimental: oligómeros y condiciones de laboratorio](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md).

### Exterior

- La función interior es `g`, la exterior `f`.
- Un planeta interior (Mercurio, Venus) tiene su órbita dentro de la de la Tierra; uno exterior (Marte, Júpiter, Saturno), fuera.
- Un destino exterior (Marte, Júpiter) tiene `φ` positivo; un destino interior (Venus), negativo.

💡 **Cómo se explica en la clase [B08-C10](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md):**
- Un planeta exterior corre más lento y la Tierra lo alcanza una vez por período sinódico: en ese momento está en oposición.
- C["Planeta exterior"] --> D["Puede estar a cualquier ángulo<br/>0°–180°<br/>oposición = 180°"]
- 🎯 **Por qué importa:** Los planetas parecen «estrellas errantes» y un titular promete «alineación de planetas». La pregunta motivadora: ¿qué planetas puedo ver esta noche, dónde y a qué hora?

📘 **Dónde se aprende** (3 clases): [B08-C10 · Planetas observables y elongación](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md); [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md); [B75-C02 · Ángulos de fase planetaria](../programa/clases/B75/B75-C02-angulos-de-fase-planetaria/CLASE.md).

### Externo

- El borde interno es la pérdida de agua; el externo, el máximo invernadero de CO₂.

💡 **Cómo se explica en la clase [B56-C12](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md):**
- Con `T_ef = 5780 K` y `L = 1`: borde interno `0,993 UA`, externo `1,705 UA`.
- Los límites a 3300 K son `0,234` (externo) y `0,863` (interno) en unidades de `S_⊕`;
- 🎯 **Por qué importa:** Elegir blancos para buscar biofirmas exige un criterio objetivo. La zona habitable lo ofrece, con limitaciones.

📘 **Dónde se aprende** (1 clase): [B56-C12 · Exoplanetas potencialmente habitables](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md).

### Extinción

- La extinción es la pérdida de luz por absorción y dispersión en el camino; si es exponencial, `I = I₀ e^(−τ)` con `τ` la profundidad óptica.
- La extinción `A` (en magnitudes) mide la pérdida de luz: `A = −2,5 log₁₀(F/F₀)`;
- La extinción `A_V` mide el polvo atravesado.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C13](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md):**
- Por eso se observa en el infrarrojo, donde la extinción es menor, y se miden los tres factores con cuidado (S1, resumen, indica un sistema fotométrico homogéneo).
- Paso 1 · Datos. Una cefeida de `P = 10 d` tiene `m = 15,50` (sin extinción; sintético).
- ⚠️ **Error frecuente:** Olvidar la extinción. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Las cefeidas y otras estrellas pulsantes cumplen que cuanto más largo es el periodo, mayor es la luminosidad. Medir un periodo equivale entonces a conocer la luminosidad intrínseca y, por comparación con el brillo aparente, la distancia.

📘 **Dónde se aprende** (6 clases): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md); [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B48-C05 · Ventanas atmosféricas](../programa/clases/B48/B48-C05-ventanas-atmosfericas/CLASE.md); [B55-C08 · Fotoquímica cósmica](../programa/clases/B55/B55-C08-fotoquimica-cosmica/CLASE.md).

### Extracción

- La extracción es el espacio frente a un equipo para abrirlo o sacarlo.
- La extracción `PRK = HMAC(sal, IKM)`.

💡 **Cómo se explica en la clase [B109-C11](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md):**
- Desde una pista de `1,00 m`, cinco de siete equipos son accesibles; la unidad sustituible (`1,30 m`) y la extracción de paleta (`1,40 m`) no.
- *Descripción textual:* la comparación de áreas da holguras y déficits; la paleta y la pista dan un margen de paso; la extracción de cada equipo más el cuerpo da la profundidad necesaria, que se compara con el ancho de pista.
- 🎯 **Por qué importa:** Un equipo que no se puede abrir o extraer no se puede reparar, y en un hábitat sin taller externo eso es un riesgo de misión. La decisión central: ¿hay área, paso y holgura para trabajar y mantener cada equipo, y dónde falta?

📘 **Dónde se aprende** (2 clases): [B88-C38 · Gestión de claves y secretos en aviónica](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md); [B109-C11 · Diseño de espacios de trabajo, mantenimiento y laboratorio](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md).

### Extracción óptima

- La extracción óptima (de Horne, citada de memoria) usa `F = Σ P D/V / Σ P²/V`.

💡 **Cómo se explica en la clase [B45-C18](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md):**
- Para una columna de 400 e⁻ con perfil gaussiano de `σ = 2` píxeles, cielo de 60 e⁻/píxel y ruido de lectura de 6 e⁻, la suma da `σ = 40,18 e⁻` y la extracción óptima `33,22 e⁻`: mejora de `1,209`.
- 🎯 **Por qué importa:** Una extracción ingenua pierde señal a ruido y es sensible a defectos. La decisión central: ¿qué pesos dan la menor varianza y cómo se protege la extracción de valores atípicos?

📘 **Dónde se aprende** (1 clase): [B45-C18 · Extracción de espectros](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md).

### Extrae el calor que entra. El

- Un refrigerador de cero evaporación extrae el calor que entra. El COP de Carnot es `T_c/(T_h − T_c)`.

🎯 **Por qué importa (clase B59-C21):** Lo extraído sirve si se conserva. La decisión central: ¿se acepta la evaporación o se paga la potencia de un refrigerador de cero evaporación?

📘 **Dónde se aprende** (1 clase): [B59-C21 · Almacenamiento criogénico y aislado de volátiles extraídos](../programa/clases/B59/B59-C21-almacenamiento-criogenico-y-aislado-de-volatiles-extraidos/CLASE.md).

### Extrapolación

- Una extrapolación es usar el modelo fuera de su dominio.
- La extrapolación es predecir fuera del rango de entrenamiento.
- La extrapolación va más allá del registro.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B17-C08](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md):**
- Extrapolación: pide predicciones fuera del rango y compáralas con la ley.
- A --> C["¿Respeta la física?<br/>Exponentes, monotonía, extrapolación"]
- 🎯 **Por qué importa:** Dos modelos pueden tener el mismo error en validación y haber aprendido cosas muy distintas: uno la ley física, otro un atajo que funciona en el rango visto. Si solo miras la métrica, no los distingues, y el atajo falla al primer dato fuera de rango.

📘 **Dónde se aprende** (4 clases): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B17-C08 · Interpretabilidad con consistencia física](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md); [B30-C19 · Impactos del clima espacial](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md); [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md).

### Extrapolación de banda limitada

- La extrapolación de banda limitada (*Gerchberg–Papoulis*) alterna dos operaciones: imponer los datos conocidos y filtrar a la banda de frecuencias donde se sabe que está la señal.

💡 **Cómo se explica en la clase [B15-C19](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md):**
- *Descripción textual:* según lo que se sepa de la señal se elige interpolación, ajuste de modelo o extrapolación de banda limitada; el resultado se verifica con una simulación de hueco conocido y con los residuos en los puntos medidos, y lo reconstruido se marca.
- 🎯 **Por qué importa:** Si falta el 8 % de una serie, ¿se puede rellenar sin contaminar el análisis? Depende de lo que se sepa de la señal: si es suave y se conoce su forma, el relleno es casi exacto; si es un evento breve que cayó en el hueco, no hay método que lo recupere.

📘 **Dónde se aprende** (1 clase): [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md).

### Extrapolación de Richardson

- La extrapolación de Richardson estima el error de un método de orden `p` comparando resultados con `h` y `h/2`: `error(h/2) ≈ |y_{h/2} − y_h|/(2^p − 1)`.
- Esa propiedad permite la extrapolación de Richardson repetida: `T_{k,j} = T_{k,j−1} + (T_{k,j−1} − T_{k−1,j−1})/((n_k/n_{k−j})² − 1)`, y la columna `j` tiene orden `2j`.
- La extrapolación de Richardson combina un paso completo y dos medios para ganar un orden.

🎯 **Por qué importa (clase B11-C19):** Un resultado numérico sin cota de error es una cifra sin sentido. Y gastar horas de cálculo para reducir un error de método que ya es menor que la incertidumbre de los datos es un desperdicio.

📘 **Dónde se aprende** (3 clases): [B11-C19 · Estimación de error y convergencia](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md); [B11-C21 · Integración numérica de alta precisión](../programa/clases/B11/B11-C21-integracion-numerica-de-alta-precision/CLASE.md); [B60-C03 · Integración numérica de redes químicas rígidas](../programa/clases/B60/B60-C03-integracion-numerica-de-redes-quimicas-rigidas/CLASE.md).

### Extrapolar

- Interpolar es evaluar dentro del intervalo de los nodos; extrapolar, fuera.
- El dominio de entrenamiento es el rango de entradas cubierto. Extrapolar es predecir fuera de él.

💡 **Cómo se explica en la clase [B11-C18](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md):**
- La regla práctica: no extrapolar; si hace falta, ampliar la tabla.
- ⚠️ **Error frecuente:** Extrapolar sin cota. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.

📘 **Dónde se aprende** (2 clases): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md); [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### Extremo aislado

- El extremo aislado no intercambia calor.

🎯 **Por qué importa (clase B85-C02):** El calor generado por un equipo debe llegar al radiador por algún camino; una unión mal conductora puede ser la resistencia dominante. La decisión central: ¿qué parte del camino de conducción limita el flujo y qué cambio lo mejora más?

📘 **Dónde se aprende** (1 clase): [B85-C02 · Conducción térmica en estructuras](../programa/clases/B85/B85-C02-conduccion-termica-en-estructuras/CLASE.md).

### Extremo global

- Un máximo (mínimo) local es un valor mayor (menor) que sus vecinos; un extremo global lo es en todo el dominio.

💡 **Cómo se explica en la clase [B09-C07](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md):**
- Sobre un intervalo cerrado `[a, b]` el extremo global está entre los puntos críticos y los bordes.
- 🎯 **Por qué importa:** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.

📘 **Dónde se aprende** (1 clase): [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md).

### Extremófilo

- Un extremófilo es un organismo que prospera o se replica en condiciones extremas para la mayoría.

🎯 **Por qué importa (clase B56-C05):** Decidir si un ambiente es habitable, o si una nave puede contaminarlo, exige umbrales de temperatura y de agua disponible. La decisión central: dada la temperatura y la actividad del agua de un ambiente, ¿está dentro de los límites en que la vida terrestre puede replicarse?

📘 **Dónde se aprende** (1 clase): [B56-C05 · Extremófilos y límites ambientales](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md).

### Eyecta

- La eyecta es el material lanzado.
- La eyecta es el material expulsado; su velocidad `v` decrece con la distancia `x` al punto de impacto.

💡 **Cómo se explica en la clase [B59-C17](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md):**
- Con `300 m/s` el alcance es `56 km`: un sitio a esa distancia de una zona sensible ya recibe eyecta.
- 🎯 **Por qué importa:** Sin atmósfera, la eyecta viaja lejos y sin frenar. La decisión central: ¿a qué distancia de una zona sensible, como una sombra permanente, hay que operar para que la eyecta no la alcance?

📘 **Dónde se aprende** (2 clases): [B59-C17 · Impacto ambiental extraterrestre](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md); [B61-C01 · Dinámica de eyección y escalado de cráteres](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md).
