# Términos · A (parte 1 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

**A** · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: **1** · [2](terminos-a-2.md)

### A\*

- Una rejilla de costos asigna un costo a cada celda. A\* expande primero los nodos con menor `g + h`.

🎯 **Por qué importa (clase B97-C08):** Con retardo de comunicación y poca energía, la ruta debe salir buena a la primera. A* garantiza la ruta de costo mínimo si la heurística es admisible, y ahorra cómputo, que a bordo es escaso.

📘 **Dónde se aprende** (1 clase): [B97-C08 · Planificación de trayectorias robóticas](../programa/clases/B97/B97-C08-planificacion-de-trayectorias-roboticas/CLASE.md).

### A priori

- El a priori es información externa que se suma a `F`.

💡 **Cómo se explica en la clase [B26-C22](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md):**
- Se suma un a priori sintético `σ(Ω_m) = 0,015` (como el de DESI BAO, S2): `F₁₁ → F₁₁ + 1/0,015² = F₁₁ + 4444`.
- Aquí el a priori es sintético, no el análisis de DESI.
- ⚠️ **Error frecuente:** Sumar a priori y datos sin comprobar independencia. Se corrige con C21.
- 🎯 **Por qué importa:** Una incertidumbre marginal puede ser mucho mayor que la que se obtendría si el otro parámetro estuviera fijo, porque ambos se compensan. Sin analizar la degeneración se interpretan mal las barras de error y se desaprovechan las combinaciones de datos.

📘 **Dónde se aprende** (1 clase): [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md).

### A2

- Los niveles I, II y III escalan la revisión según actividad, probabilidad de dosis y fisión. A2 es el valor de actividad de la tabla de la IAEA SSR-6.

🎯 **Por qué importa (clase B86-C18):** Los límites de la energía nuclear en el espacio son tanto jurídicos y de seguridad como técnicos: quién aprueba, con qué análisis y con qué umbrales. Un ingeniero de potencia debe saber que estas decisiones existen y qué datos las gobiernan.

📘 **Dónde se aprende** (1 clase): [B86-C18 · Seguridad y licenciamiento energético](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md).

### Abandono

- El abandono `c` es la fracción de clientes que se va por mes.
- El abandono `c` es la fracción de clientes que se va cada mes.

💡 **Cómo se explica en la clase [B125-C02](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md):**
- Con abandono `c`, la fracción viva tras `k` meses es `(1 − c)^k` y `LTV = Σ ARPU · margen · (1 − c)^k = ARPU · margen / c`.
- Duplicar el abandono divide el valor por dos.
- 🎯 **Por qué importa:** El modelo de ingresos define cuándo entra el dinero y cuánto vale un cliente; ninguna clase anterior lo trata. La decisión central: ¿cuánto vale un cliente de suscripción, cuándo se reconoce su ingreso y cuánto abandono puede tolerar el negocio?

📘 **Dónde se aprende** (2 clases): [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md); [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### Abanico tangencial

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C13):** Dos defectos limitan el campo y la relación focal. La decisión central: ¿hasta qué f/ sirve una esfera y qué campo tolera un paraboloide?

📘 **Dónde se aprende** (1 clase): [B41-C13 · Aberración esférica y coma](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md).

### Aberración

- La aberración desplaza la dirección aparente por la velocidad del observador: máximo `v/c`.

💡 **Cómo se explica en la clase [B74-C02](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md):**
- *Descripción textual:* los fotones y la PSF fijan el centroide, la escala lo convierte en ángulo, la aberración añade un efecto sistemático y la distancia convierte el ángulo en metros.
- Por tipo: aleatorio (fotones) o sistemático (aberración).
- ⚠️ **Error frecuente:** Tratar la aberración como ruido. Es un sistemático que se modela, como en 8.3.
- 🎯 **Por qué importa:** Un ángulo de `0,01″` parece pequeño, pero a un millón de kilómetros son decenas de metros. La decisión central: ¿cuánta incertidumbre angular aporta el detector y cuánta es un efecto físico que hay que modelar (aberración)?

📘 **Dónde se aprende** (1 clase): [B74-C02 · Observación angular y astrometría](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md).

### Aberración cromática longitudinal

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C14):** El color y el astigmatismo degradan el campo de refractores y espejos. La decisión central: ¿cuánto se separan los focos por color y por plano?

📘 **Dónde se aprende** (1 clase): [B41-C14 · Aberración cromática y astigmatismo](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md).

### Aberración esférica

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C13](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md):**
- *Descripción textual:* la diferencia de superficie da la aberración esférica y el trazado fuera de eje da la coma.
- 🎯 **Por qué importa:** Dos defectos limitan el campo y la relación focal. La decisión central: ¿hasta qué f/ sirve una esfera y qué campo tolera un paraboloide?

📖 **Explicado a fondo:** [Aberración esférica](esencial/esencial-a-c.md#aberración-esférica) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B41-C13 · Aberración esférica y coma](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md).

### Aberración esférica longitudinal

- La aberración esférica longitudinal (`LSA`) es la diferencia entre el cruce con el eje de un rayo de altura `h` y el paraxial.
- La aberración esférica longitudinal de la lente.

🎯 **Por qué importa (clase B41-C04):** El espejo primario de un telescopio reflector es una superficie cónica. La decisión central: ¿por qué se usa un paraboloide y no una esfera?

📘 **Dónde se aprende** (3 clases): [B41-C04 · Espejos esféricos y parabólicos](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md); [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md); [B50-C01 · Trazado exacto de rayos y aberraciones de orden superior](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md).

### Aberración longitudinal

- La aberración longitudinal `y²/R` de un paraboloide.

🎯 **Por qué importa (clase B43-C06):** La prueba convierte una desviación de nanómetros en un desplazamiento de milímetros de la cuchilla. La decisión central: ¿en cuánto debe desplazarse la cuchilla para cada zona del paraboloide y cuántas bandas de Ronchi se esperan?

📘 **Dónde se aprende** (1 clase): [B43-C06 · Pruebas de Ronchi y Foucault](../programa/clases/B43/B43-C06-pruebas-de-ronchi-y-foucault/CLASE.md).

### Aberraciones cromosómicas

- Un error de reunión une extremos equivocados y puede originar aberraciones cromosómicas (dicéntricos, translocaciones, deleciones).

🎯 **Por qué importa (clase B112-C05):** Falta la clase de mecanismos moleculares de daño y reparación. Sin ella, la diferencia de eficacia biológica entre fotones e iones pesados (B112-C01, C02) y la incertidumbre del riesgo (C04) parecen cifras arbitrarias.

📘 **Dónde se aprende** (1 clase): [B112-C05 · Daño y reparación del ADN por radiación espacial](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md).

### Abertura efectiva

- La abertura efectiva `A_e = G λ²/(4π)` es el área equivalente con que la antena captura potencia.

💡 **Cómo se explica en la clase [B91-C01](../programa/clases/B91/B91-C01-fundamentos-de-teoria-de-antenas/CLASE.md):**
- Su abertura efectiva es `A_e = 0,1306 λ²`.
- La abertura efectiva de la antena de 70 m en X es `2876 m²` frente a `3848 m²` de área geométrica (razón `0,747`, la misma `η`).
- 🎯 **Por qué importa:** Elegir o diseñar una antena empieza por saber qué fija su ganancia y su haz. La decisión central: ¿cuánta ganancia da una apertura de diámetro `D` a la frecuencia `f`, y qué parte de esa ganancia ideal se pierde en la práctica?

📘 **Dónde se aprende** (1 clase): [B91-C01 · Fundamentos de teoría de antenas](../programa/clases/B91/B91-C01-fundamentos-de-teoria-de-antenas/CLASE.md).

### Abiogénesis

- La abiogénesis es el origen de la vida a partir de materia sin vida.

🎯 **Por qué importa (clase B56-C04):** Las hipótesis (mundo de ARN, metabolismo primero, ventilas hidrotermales, charcas con ciclos húmedo–seco, aporte meteorítico) se discuten a menudo con palabras. Una cuenta de espacio de secuencias permite saber cuándo una afirmación es plausible por números y cuándo exige un mecanismo de selección.

📘 **Dónde se aprende** (1 clase): [B56-C04 · Hipótesis de abiogénesis](../programa/clases/B56/B56-C04-hipotesis-de-abiogenesis/CLASE.md).

### Abombamiento periférico

- El abombamiento periférico es el máximo secundario a distancia `≈ π α` de la carga.

💡 **Cómo se explica en la clase [B53-C12](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md):**
- Para una carga lineal de `10¹¹ N/m`, la deflexión máxima es `58,8 m` (analítica `58,8 m`) y el abombamiento periférico está a `219 km` (teórico `218 km`).
- 🎯 **Por qué importa:** La flexión revela el espesor elástico de la litosfera y la contracción, el balance térmico global. La decisión central: ¿qué espesor elástico y qué acortamiento explican la deformación observada?

📘 **Dónde se aprende** (1 clase): [B53-C12 · Tectónica planetaria](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md).

### Abscisa

- Un par ordenado `(x, y)` es la posición de un punto: `x` es la abscisa (horizontal) e `y` la ordenada (vertical).

🎯 **Por qué importa (clase B03-C15):** Las fichas de la NASA dan semiejes y períodos de los ocho planetas. En una tabla son 16 números.

📘 **Dónde se aprende** (1 clase): [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md).

### Absoluta

- La tolerancia relativa `rtol` escala con el tamaño de la referencia; la absoluta `atol` es un piso fijo.
- Una ruta absoluta está completa desde la raíz (`C:\...` o `/home/...`); una relativa se interpreta desde el directorio de trabajo.
- La tolerancia relativa `rtol` y la absoluta `atol` fijan el error permitido por paso.

💡 **Cómo se explica en la clase [B07-C15](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md):**
- Una ruta relativa son pasos desde ese punto; una absoluta, pasos desde la raíz.
- (4) Ruta absoluta fija: la peor opción para código compartido.
- ⚠️ **Error frecuente:** Ruta absoluta fija. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Una causa muy común de «el programa no encuentra el archivo» es que la ruta funciona en el computador del autor y no en otro: se escribió con `C:\Usuarios\ana\datos\...`, o se asumió que el programa se ejecuta desde cierta carpeta.

📘 **Dónde se aprende** (3 clases): [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md); [B14-C03 · Análisis numérico con SciPy](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md); [B14-C10 · Pruebas de regresión numérica](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md).

### Absorción

- La absorción `A` es la superficie equivalente que absorbe.
- La absorción es terminar en resuelto o conflicto.
- Un espectro continuo tiene luz en todas las longitudes de onda; uno de emisión muestra líneas brillantes sobre fondo oscuro; uno de absorción muestra líneas oscuras sobre un fondo continuo.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C17](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md):**
- El mismo gas, más frío y delante de una fuente continua, da líneas de absorción en las mismas posiciones.
- ⚠️ **Error frecuente:** Confundir emisión con absorción. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** En B01-C01 estimaste la velocidad de una galaxia con una sola línea, H-alfa en 662,9 nm. Pero ¿cómo se sabe que esa línea es H-alfa y no otra?

📘 **Dónde se aprende** (5 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md); [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md); [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md); [B119-C29 · Escalada, desescalada y medidas de fomento de la confianza](../programa/clases/B119/B119-C29-escalada-desescalada-y-medidas-de-fomento-de-la-confianza/CLASE.md).

### Absortividad

- La absortividad `α` es la fracción de la irradiancia que absorbe una superficie.

🎯 **Por qué importa (clase B13-C16):** Un sensor de temperatura pegado a un panel de una nave devuelve una resistencia. Convertirla en kelvin exige calibrarlo contra referencias conocidas, y comprobar que la temperatura medida concuerda con un balance térmico previsto.

📘 **Dónde se aprende** (2 clases): [B13-C16 · Calibración térmica](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md); [B47-C23 · Sondas heliosféricas: Parker Solar Probe y Voyager](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md).

### Absortividad acumulada

- La absortividad acumulada `α(t) = α₀ + Δα(1 − e^(−ESH/E₀)) + Δα_capa·[t > t_capa] + Δα_cont·min(1, t/2)`.

🎯 **Por qué importa (clase B85-C29):** La vida de un recubrimiento depende de varios efectos que se suman y de parámetros inciertos. La decisión central: ¿cuál es la probabilidad de que la temperatura supere el límite al final de la vida y qué incertidumbre la domina?

📘 **Dónde se aprende** (1 clase): [B85-C29 · Evaluación y modelado de la degradación en órbita](../programa/clases/B85/B85-C29-evaluacion-y-modelado-de-la-degradacion-en-orbita/CLASE.md).

### Absortividad efectiva

- La absortividad efectiva `α_ef = α_r(1 − f) + α_d f`.

💡 **Cómo se explica en la clase [B85-C16](../programa/clases/B85/B85-C16-polvo-lunar-y-contaminacion/CLASE.md):**
- *Descripción textual:* la masa de polvo da el número de granos y la cobertura; junto con la película contaminante, determina la absortividad efectiva y la temperatura del radiador;
- 🎯 **Por qué importa:** Un radiador que se ensucia rechaza menos calor y se calienta; en la Luna la limpieza no es sencilla. La decisión central: ¿qué cobertura de polvo o espesor de película hace subir la temperatura de un radiador por encima de su límite?

📘 **Dónde se aprende** (1 clase): [B85-C16 · Polvo lunar y contaminación](../programa/clases/B85/B85-C16-polvo-lunar-y-contaminacion/CLASE.md).

### Absortividad solar

- Salto de temperatura `ΔT`: diferencia entrada–salida del refrigerante. Absortividad solar: fracción de la radiación solar absorbida.

🎯 **Por qué importa (clase B106-C08):** En el vacío el calor solo sale por radiación; el área del radiador depende de la temperatura y de lo que «ve». La decisión central: ¿cuánta área y qué caudal de refrigerante para evacuar la carga, y cuánto tiempo hay si el enfriamiento falla?

📘 **Dónde se aprende** (1 clase): [B106-C08 · Control térmico interior](../programa/clases/B106/B106-C08-control-termico-interior/CLASE.md).

### AbsRel

- MAE es el error absoluto medio, RMSE el cuadrático medio, AbsRel la media de `|ẑ − z|/z` y delta1 la fracción de puntos con `máx(z/ẑ, ẑ/z) < 1,25`.

💡 **Cómo se explica en la clase [B103-C08](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md):**
- En profundidad (5000 puntos de 4 a 40 m con error `Z²σ_d/(f B)` y 2 % de valores atípicos): global `MAE = 1,058 m`, `RMSE = 2,262 m`, `AbsRel = 0,0409`, `delta1 = 0,9788`; por rango, `RMSE` pasa de 0,519 m (4–10 m) a 2,924 m (20–40 m) mientras `AbsRel` va de 0,0187 a 0,0533: el RMSE refleja sobre todo el rango lejano.
- S --> D["errores de profundidad<br/>MAE, RMSE, AbsRel, delta1"]
- 🎯 **Por qué importa:** Un segmentador que acierta el 99 % de los píxeles puede no encontrar nunca la clase que importa, y dos detectores con AP de 0,58 y 0,60 pueden ser indistinguibles con 100 imágenes. La decisión central: ¿qué métricas y qué intervalo hacen falta para afirmar que un algoritmo de percepción es suficiente para una tarea?

📘 **Dónde se aprende** (1 clase): [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md).

### Abultamiento

- El abultamiento es el aumento de volumen del material removido.

🎯 **Por qué importa (clase B61-C02):** Medir un cráter es medir un bol, pero lo que se ve es el bol después de colapsar y rellenarse. La decisión central: ¿cuánto volumen tenía la cavidad original y cuánto se perdió en el relleno de brecha?

📘 **Dónde se aprende** (1 clase): [B61-C02 · Cráteres simples: morfología y formación](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md).

### Abundancia

- La abundancia es cuánto hay de un elemento; puede darse en número (átomos), en masa (kg) o con la escala logarítmica astronómica: ```text A(X) = log10(N_X / N_H) + 12 ``` donde `N_X` y `N_H` son números de átomos por unidad de volumen.
- La abundancia `Y` es cuántos núcleos de helio quedan, en unidades relativas.
- La abundancia es su fracción.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C02](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md):**
- Los astrónomos dan la abundancia de un elemento X respecto de hidrógeno con `A(X) = log10(N_X/N_H) + 12`.
- 🎯 **Por qué importa:** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?

📘 **Dónde se aprende** (6 clases): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md); [B24-C08 · Nucleosíntesis estelar](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md); [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B45-C14 · Composición química por espectros](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md); [B53-C29 · Imágenes hiperespectrales de superficies planetarias](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md); [B59-C02 · Prospección de hielo lunar](../programa/clases/B59/B59-C02-prospeccion-de-hielo-lunar/CLASE.md).

### Abundancia equivalente en agua (WEH)

- La abundancia equivalente en agua (WEH) es la masa de agua que daría la misma señal por cada 100 de regolito.

🎯 **Por qué importa (clase B67-C07):** Un sensor no mide «agua»: mide cuentas, y de ellas se infiere la abundancia con un modelo. La decisión central: ¿cuánto tiempo de medición y qué canales hacen falta para detectar y separar un volátil con la incertidumbre requerida?

📘 **Dónde se aprende** (1 clase): [B67-C07 · Sensores para volátiles: espectrometría de neutrones y de masas](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md).

### Abundancia isotópica

- La abundancia isotópica es la fracción de átomos del elemento que son de ese isótopo.

🎯 **Por qué importa (clase B06-C03):** El carbono del Sol, ¿es igual que el de la Tierra? Una forma de preguntarlo con rigor es comparar cuántos átomos de carbono-12 hay por cada uno de carbono-13.

📘 **Dónde se aprende** (1 clase): [B06-C03 · Isótopos y masa atómica](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md).

### Abundancia logarítmica

- La abundancia logarítmica `log ε_i = log₁₀(N_i/N_H) + 12` fija el hidrógeno en 12 por definición.

🎯 **Por qué importa (clase B55-C01):** Cualquier modelo químico del espacio parte de una composición inicial: cuánto hidrógeno, helio, carbono u oxígeno hay. Las fuentes dan esa composición en una escala logarítmica poco intuitiva, y los modelos piden fracciones en número o en masa.

📘 **Dónde se aprende** (1 clase): [B55-C01 · Abundancia química cósmica](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md).

### Abundancias

- El desmezclado lineal estima las abundancias de cada miembro.

💡 **Cómo se explica en la clase [B57-C22](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md):**
- Sin ruido, el desmezclado con suma 1 recupera las abundancias con error `4,7e-15`.
- *Descripción textual:* el espectro del píxel es una combinación de miembros extremos con ruido; el desmezclado estima las abundancias y el número de bandas fija cuánto ruido se transmite.
- 🎯 **Por qué importa:** Dos materiales distintos pueden parecer iguales en cuatro bandas anchas y diferenciarse en cientos de bandas estrechas. La decisión central: ¿cuándo vale la pena el costo en datos de un sensor hiperespectral y cómo se separa una mezcla de materiales?

📘 **Dónde se aprende** (1 clase): [B57-C22 · Espectrómetros de imagen e hiperespectrales](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md).

### AC

- El PV es el valor del trabajo planificado a la fecha; el EV, el valor del trabajo logrado; el AC, el costo real.

🎯 **Por qué importa (clase B124-C15):** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?

📘 **Dónde se aprende** (1 clase): [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### Accesibilidad

- La accesibilidad es la posibilidad de usar un entorno sin barreras.

💡 **Cómo se explica en la clase [B109-C08](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md):**
- Los valores son de una población inventada y no son una norma de accesibilidad, que no se consultó.
- ⚠️ **Error frecuente:** Presentar la banda como norma de accesibilidad. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Un control puesto «a la altura normal» deja fuera a quien no la alcanza. La decisión central: ¿a qué altura (o con qué ajuste) un puesto sirve al mayor número de usuarios y a quién deja fuera?

📘 **Dónde se aprende** (1 clase): [B109-C08 · Diseño inclusivo en hábitats](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md).

### Accesibilidad de un equipo

- La accesibilidad de un equipo es la posibilidad de llegar a él con la profundidad libre necesaria.

🎯 **Por qué importa (clase B109-C11):** Un equipo que no se puede abrir o extraer no se puede reparar, y en un hábitat sin taller externo eso es un riesgo de misión. La decisión central: ¿hay área, paso y holgura para trabajar y mantener cada equipo, y dónde falta?

📘 **Dónde se aprende** (1 clase): [B109-C11 · Diseño de espacios de trabajo, mantenimiento y laboratorio](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md).

### Acceso equitativo

- El acceso equitativo es la oportunidad de uso para todos los países.

🎯 **Por qué importa (clase B120-C03):** Las posiciones orbitales y el espectro son recursos escasos con reglas de asignación y no están tratados como concepto jurídico. La decisión central: ¿cuánto recurso hay, quién lo obtiene bajo cada régimen y qué mide la desigualdad del reparto?

📘 **Dónde se aprende** (1 clase): [B120-C03 · Posiciones orbitales y espectro como recursos limitados](../programa/clases/B120/B120-C03-posiciones-orbitales-y-espectro-como-recursos-limitados/CLASE.md).

### Aceleración

- La aceleración `a` es el ritmo de cambio de la velocidad: `a = Δv/Δt` en media y su límite en instantánea.
- La aceleración es el cociente de tiempos antes/después.
- La aceleración es `S(N) = T(1)/T(N)`, con `T` el tiempo de pared.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C02](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md):**
- Si la rapidez es constante pero la dirección cambia, `v` cambia y por tanto hay aceleración.
- Para una circunferencia de radio `r` con rapidez `v`, la aceleración apunta al centro y vale `a = v²/r`.
- ⚠️ **Error frecuente:** Creer que sin cambio de rapidez no hay aceleración. Ejercicio 9.
- 🎯 **Por qué importa:** Cuando una agencia dice que un satélite «va a 7,7 km/s», ¿respecto de qué y en qué dirección? La pregunta motivadora es: ¿cómo describo un movimiento de forma que otra persona lo reconstruya sin ambigüedad?

📘 **Dónde se aprende** (4 clases): [B05-C02 · Posición, velocidad y aceleración](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md); [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md); [B14-C14 · Vectorización y rendimiento](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md); [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md).

### Aceleración angular

- La aceleración angular `α` es el cambio de velocidad angular por unidad de tiempo (rad/s²).

🎯 **Por qué importa (clase B05-C09):** Un satélite en órbita elíptica va más rápido cerca de la Tierra que lejos; un patinador gira más rápido al recoger los brazos. La pregunta motivadora es: ¿qué cantidad se mantiene constante cuando algo gira bajo una fuerza central, y qué hace falta para cambiar un giro?

📘 **Dónde se aprende** (1 clase): [B05-C09 · Momento angular y torque](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md).

### Aceleración axial

- La aceleración axial (carga axial) es `n = (F − D)/(m g₀)` en g.

💡 **Cómo se explica en la clase [B77-C10](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md):**
- *Descripción textual:* empuje, arrastre y masa dan la aceleración axial; si supera el límite se estrangula el empuje, con un costo en velocidad; por otra vía, `q` y la racha dan la carga lateral.
- Con el cohete de C09 sin límite, la aceleración axial llega a `10,19 g` al final del quemado, la presión dinámica máxima es `62,7 kPa` a los `35,0 s` y `q·α` (racha de 10 m/s) llega a `1,35 kPa·rad` a los `24,0 s`.
- 🎯 **Por qué importa:** El mayor empuje reduce las pérdidas pero carga la estructura, sobre todo al final del quemado, cuando la masa es menor. La decisión central: ¿qué límite de carga impone la estructura y cuánta velocidad cuesta respetarlo?

📘 **Dónde se aprende** (1 clase): [B77-C10 · Restricciones de cargas estructurales](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md).

### Aceleración centrípeta

- La aceleración centrípeta de un cuerpo en órbita circular es `a_c = 4π²r/T²`.
- La aceleración centrípeta `a_c` es la que apunta al centro de la circunferencia.

💡 **Cómo se explica en la clase [B02-C15](../programa/clases/B02/B02-C15-newton-y-gravitacion-universal/CLASE.md):**
- *Descripción textual:* desde la gravedad de superficie y la regla del inverso del cuadrado se predice la aceleración a la distancia de la Luna; se compara con la aceleración centrípeta calculada del período y la distancia; si coinciden, es la misma fuerza.
- 🎯 **Por qué importa:** Una ley que describe es útil; una ley que explica unifica. La pregunta motivadora es: ¿es la misma fuerza la que hace caer una piedra y la que mantiene a la Luna en órbita?

📖 **Explicado a fondo:** [Aceleración centrípeta](esencial/esencial-a-c.md#aceleración-centrípeta) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B02-C15 · Newton y gravitación universal](../programa/clases/B02/B02-C15-newton-y-gravitacion-universal/CLASE.md); [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md).

### Aceleración de Coriolis

- La aceleración de Coriolis es `−2ω × v_rot`; la centrífuga, `−ω × (ω × r)`.

💡 **Cómo se explica en la clase [B73-C02](../programa/clases/B73/B73-C02-marcos-rotatorios-sinodicos/CLASE.md):**
- Un satélite sintético en órbita circular inercial a `38 440 km` de la Tierra tiene `|v| = 3,2193 km/s` en el marco inercial y `3,1134 km/s` en el sinódico; sufre una aceleración de Coriolis de `1,657e-02 m/s²` y centrífuga de `2,835e-04 m/s²`.
- 🎯 **Por qué importa:** Un radar, un archivo de efemérides y un diseño de trayectoria rara vez usan el mismo marco. Confundir una velocidad inercial con una giratoria cambia el resultado en kilómetros por segundo.

📘 **Dónde se aprende** (1 clase): [B73-C02 · Marcos rotatorios sinódicos](../programa/clases/B73/B73-C02-marcos-rotatorios-sinodicos/CLASE.md).

### Aceleración de marea

- La aceleración de marea es la diferencia de aceleración gravitatoria entre dos puntos del cuerpo.
- La aceleración de marea entre dos puntos separados `L` es `2GML/r³`.
- La aceleración de marea es la diferencia de la gravedad del planeta entre dos puntos.

🎯 **Por qué importa (clase B09-C04):** La gravedad que siente un cuerpo depende de su distancia al astro: `g(r) = GM/r²`. La marea nace de que esa gravedad cambia de un lado a otro de un cuerpo extenso.

📘 **Dónde se aprende** (3 clases): [B09-C04 · Reglas de derivación](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md); [B27-C08 · Horizonte de sucesos](../programa/clases/B27/B27-C08-horizonte-de-sucesos/CLASE.md); [B52-C12 · Anillos planetarios](../programa/clases/B52/B52-C12-anillos-planetarios/CLASE.md).

### Aceleración de Milgrom

- La aceleración de Milgrom `a₀ ≈ 1,2×10⁻¹⁰ m/s²` (valor convencional no consultado).

🎯 **Por qué importa (clase B36-C11):** Una alternativa debe confrontarse con todas las pruebas. La decisión central: ¿qué observación separa la materia oscura de la gravedad modificada?

📘 **Dónde se aprende** (1 clase): [B36-C11 · Gravedad modificada (MOND y relativistas) frente a materia oscura](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md).

### Aceleración de Schwarzschild post-newtoniana

- La aceleración de Schwarzschild post-newtoniana es `a = −GM r/r³ + (GM/(c² r³)) [(4GM/r − v²) r + 4 (r·v) v]`.

🎯 **Por qué importa (clase B72-C17):** La corrección relativista es un test histórico de la teoría y, en navegación por satélite, un término que los modelos de precisión no pueden ignorar. La decisión central: ¿cuánto vale el avance relativista del periapsis, cuándo es relevante y qué parte de la relatividad queda fuera de este cálculo?

📘 **Dónde se aprende** (1 clase): [B72-C17 · Efectos relativistas orbitales](../programa/clases/B72/B72-C17-efectos-relativistas-orbitales/CLASE.md).

### Aceleración del cohete

- La aceleración del cohete `a` equivale a `g`.

🎯 **Por qué importa (clase B26-C06):** Los relojes de los satélites de navegación van a un ritmo ligeramente distinto de los terrestres, y un maser en una torre ve su frecuencia cambiar con la altura. Todo eso se deduce de la equivalencia entre aceleración y gravedad.

📘 **Dónde se aprende** (1 clase): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md).

### Aceleración difusiva

- La aceleración difusiva es la ganancia de energía al cruzar repetidamente.

💡 **Cómo se explica en la clase [B30-C14](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md):**
- La aceleración difusiva da un índice integral `s = 3/(r − 1)`: `1,5` para `r = 3`.
- 🎯 **Por qué importa:** Las partículas energéticas solares son un riesgo para satélites y astronautas, y los choques de las CME son un origen. La decisión central: ¿qué espectro produce un choque de una compresión dada?

📘 **Dónde se aprende** (1 clase): [B30-C14 · Choques y aceleración de partículas](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md).

### Aceleración gravitatoria

- La aceleración gravitatoria a distancia `r` de una masa `M` es `g(r) = GM/r²`.
- La aceleración gravitatoria hacia un cuerpo central en el origen es `a = −GM · r / |r|³`, donde `r` es el vector de posición; apunta al centro y su módulo es `GM/r²`.
- La aceleración gravitatoria `g = GM/r²`.

🎯 **Por qué importa (clase B05-C10):** La misma fuerza que hace caer una manzana mantiene a la Luna en órbita: esa idea unificó el cielo y la Tierra. La pregunta motivadora es: ¿cómo comprobar con números que la gravedad de la superficie y la órbita de la Luna son la misma fuerza?

📘 **Dónde se aprende** (3 clases): [B05-C10 · Gravitación universal](../programa/clases/B05/B05-C10-gravitacion-universal/CLASE.md); [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B71-C02 · Ley de gravitación universal](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md).

### Aceleración lateral crítica

- La aceleración lateral crítica de un giro es `g T/(2h)`.

🎯 **Por qué importa (clase B102-C05):** Las leyes de operación de un rover fijan un máximo de inclinación. La decisión central: ¿cuánto margen queda frente al vuelco en una pendiente dada, y qué parte de ese margen depende de la gravedad?

📘 **Dónde se aprende** (1 clase): [B102-C05 · Distribución de cargas y estabilidad ante vuelco](../programa/clases/B102/B102-C05-distribucion-de-cargas-y-estabilidad-ante-vuelco/CLASE.md).

### Aceleración media

- La aceleración media sobre `[0, T]` es `Δv/T`.

🎯 **Por qué importa (clase B09-C11):** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.

📘 **Dónde se aprende** (1 clase): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md).

### Aceleración newtoniana

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B36-C11):** Una alternativa debe confrontarse con todas las pruebas. La decisión central: ¿qué observación separa la materia oscura de la gravedad modificada?

📘 **Dónde se aprende** (1 clase): [B36-C11 · Gravedad modificada (MOND y relativistas) frente a materia oscura](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md).

### Aceleración perturbadora relativa

- La aceleración perturbadora relativa es `a_p/(μ/r²)`.

🎯 **Por qué importa (clase B72-C01):** Un propagador kepleriano cabe en tres líneas y se usa en cualquier curso, pero ¿hasta cuándo se puede confiar en él? La decisión central: ¿cuál perturbación domina en cada altitud y en cuánto tiempo la solución de dos cuerpos deja de servir?

📘 **Dónde se aprende** (1 clase): [B72-C01 · Limitaciones del problema de dos cuerpos](../programa/clases/B72/B72-C01-limitaciones-del-problema-de-dos-cuerpos/CLASE.md).

### Acelerador

- Un sobrevuelo es acelerador si `v∞` queda más alineado con la velocidad del planeta y frenador si queda menos.

🎯 **Por qué importa (clase B75-C06):** Un cohete que sale de la Tierra no puede llevar combustible para ir a Júpiter con una trayectoria directa de baja energía y además frenar. La decisión central: ¿cuánta velocidad heliocéntrica puede ganar o perder una nave pasando cerca de un planeta, y de qué depende?

📘 **Dónde se aprende** (1 clase): [B75-C06 · Asistencias gravitacionales](../programa/clases/B75/B75-C06-asistencias-gravitacionales/CLASE.md).

### Acepta

- El error normalizado `err = máx_i |Δ_i| / sc_i`; el paso se acepta si `err ≤ 1` y se rechaza si no.

💡 **Cómo se explica en la clase [B11-C08](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md):**
- Un error normalizado de `0,4` se acepta y sugiere ampliar: `0,9 · 0,4^{−0,2} = 1,08`.
- Al repetir con `0,375`, el error baja por un factor `(0,375/0,5)⁵ = 0,24`: `err ≈ 0,6 < 1`, se acepta.
- 🎯 **Por qué importa:** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.

📘 **Dónde se aprende** (1 clase): [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md).

### Aceptación

- La aceptación es `min(1, exp(−ΔH))`, que corrige ese error.
- La aceptación es la decisión formal de recibir el producto.
- Calificación es el ensayo a nivel superior al de vuelo; aceptación el de la unidad de vuelo;
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B19-C03](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md):**
- Para el banco de pruebas, `λ_max = 20` y `ε < 0,447`: más allá, la energía explota y la aceptación cae a cero.
- La aceptación es `min(1, exp(0,00732)) = 1`: se acepta siempre.
- ⚠️ **Error frecuente:** Tomar la aceptación alta como señal de buen muestreo. Ejercicio 11.
- 🎯 **Por qué importa:** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.

📘 **Dónde se aprende** (4 clases): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md); [B83-C19 · Aceptación y transferencia a operaciones](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md); [B84-C01 · Entorno mecánico de lanzamiento](../programa/clases/B84/B84-C01-entorno-mecanico-de-lanzamiento/CLASE.md); [B90-C19 · Aceptación de unidades de vuelo](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md).

### Acercamiento

- El acercamiento `δ = a²/R`.

💡 **Cómo se explica en la clase [B43-C25](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md):**
- La presión de Hertz integrada con Simpson devuelve `F = 99,99986 N` (fórmula `100,00000 N`) y el acercamiento `δ = (2/E*) ∫p dr = 5,37479 µm` (fórmula `5,37479 µm`).
- Paso 2 · Acercamiento. `δ = a²/R = 5,375 µm`.
- 🎯 **Por qué importa:** La rigidez del contacto determina cuánto se mueve el eje bajo carga y la frecuencia de resonancia. La decisión central: ¿cuánto se deforma el contacto, cuánta rigidez aporta y qué fracción de la carga soporta la bola más cargada?

📘 **Dónde se aprende** (1 clase): [B43-C25 · Rodamientos y apoyos de precisión en telescopios](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md).

### ACH

- La presión negativa es una presión interior menor que la exterior. ACH es el número de renovaciones de aire por hora.

💡 **Cómo se explica en la clase [B63-C05](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md):**
- Con mezcla perfecta, `dC/dt = −ACH·C`, luego `C(t) = C₀ e^(−ACH·t)`.
- Para reducir la concentración por un factor `R`, `t = ln R / ACH`.
- ⚠️ **Error frecuente:** Usar ACH en 1/h con el tiempo en segundos. Se corrige con la tabla de la sección 9.
- 🎯 **Por qué importa:** Contener no es un adjetivo: es un conjunto de diferencias de presión, flujos y filtros que se pueden calcular. La decisión central: ¿qué impide que el aire de la sala salga, y cuánto tarda en limpiarse si se contamina?

📘 **Dónde se aprende** (1 clase): [B63-C05 · Contención de muestras extraterrestres: instalaciones y principios](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md).

### Achatamiento

- El achatamiento mide cuánto difiere `c` de `a`.
- El achatamiento `f = (a − c)/a` mide cuánto se aplana un esferoide.

💡 **Cómo se explica en la clase [B03-C17](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md):**
- El achatamiento es pequeño: la Tierra es una esfera con una precisión del 0,3 %.
- 🎯 **Por qué importa:** La NASA publica que la densidad media del Sol es 1408 kg/m³ (S1), cerca de una vez y media la del agua. ¿Cómo se obtiene?

📘 **Dónde se aprende** (2 clases): [B03-C17 · Áreas y volúmenes elementales](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md); [B09-C20 · Aplicaciones a campos gravitatorios](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md).

### Ácido

- Un ácido (de Brønsted–Lowry) es una sustancia que cede un protón (H⁺); una base, la que lo acepta.

💡 **Cómo se explica en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- Si un ácido fuerte monoprótico tiene concentración `c`, `[H⁺] ≈ c` y `pH = −log₁₀ c`.
- Con `c = 1,0 × 10⁻⁴` el mismo ácido se ioniza el 71,6 % y la aproximación da `pH = 3,87` frente al exacto `4,145`: un error de 0,27.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Ácido carboxílico

- Un grupo funcional es una agrupación de átomos que da propiedades características: alcohol (–OH, como el etanol `C₂H₆O`), aldehído (–CHO, como el formaldehído `CH₂O`), ácido carboxílico (–COOH, como el fórmico `CH₂O₂` y el acético `C₂H₄O₂`) y amina (–NH₂, como la metilamina `CH₅N`).

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- Un ácido carboxílico (–COOH) cede un protón (C15): el fórmico `HCOOH` da formiato `HCOO⁻`.
- La segunda son los grupos funcionales con oxígeno y nitrógeno: alcohol, aldehído, ácido carboxílico y amina.
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Ácido conjugado

- Al ceder el protón, un ácido `HA` da su base conjugada `A⁻`; al aceptarlo, una base `B` da su ácido conjugado `BH⁺`.

💡 **Cómo se explica en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- C["Base B"] -->|"acepta H+"| D["Ácido conjugado BH+"]
- *Descripción textual:* a la izquierda, un ácido que cede un protón y se convierte en su base conjugada; abajo, una base que acepta un protón y se convierte en su ácido conjugado.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Acidófilo

- Un acidófilo crece a pH bajo y un alcalófilo a pH alto.

💡 **Cómo se explica en la clase [B64-C05](../programa/clases/B64/B64-C05-acidofilos-y-alcalofilos/CLASE.md):**
- En un acidófilo, un ácido débil orgánico entra como neutro y se acumula disociado dentro: una razón de 18 a 55 anticipa toxicidad.
- Por contraste: neutrófilo frente a acidófilo y alcalófilo.
- ⚠️ **Error frecuente:** Creer que un potencial positivo aumenta Δp. En el acidófilo lo reduce (ejemplo 13).
- 🎯 **Por qué importa:** Un acidófilo vive en un medio miles de veces más ácido que su citoplasma. La pregunta motivadora: ¿cómo mantiene una célula un interior casi neutro y qué le cuesta?

📘 **Dónde se aprende** (1 clase): [B64-C05 · Acidófilos y alcalófilos](../programa/clases/B64/B64-C05-acidofilos-y-alcalofilos/CLASE.md).

### Ácidos o bases fuertes

- Los ácidos o bases fuertes se ionizan prácticamente por completo; los débiles, sólo en parte, y su equilibrio se describe con `K_a` o `K_b`.

🎯 **Por qué importa (clase B06-C15):** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Acierto

- Un acierto (*hit*) es encontrar el dato en caché; un fallo (*miss*), tener que ir a un nivel inferior.
- Un acierto (`a`), una falsa alarma (`b`), un fallo (`c`) y un negativo correcto (`d`) forman la tabla.

🎯 **Por qué importa (clase B18-C03):** Un catálogo con millones de estrellas o una rejilla de simulación pasan cada dato por la CPU una o pocas veces. Cuando las operaciones por dato son pocas, el tiempo no lo fija la CPU sino el viaje de los datos.

📘 **Dónde se aprende** (2 clases): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md); [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md).

### Aciertos

- Los aciertos son las estructuras dentro de una ventana.

💡 **Cómo se explica en la clase [B02-C09](../programa/clases/B02/B02-C09-alineaciones-arqueologicas-y-sesgos/CLASE.md):**
- Con `N` estructuras, el número esperado de aciertos es `N·p`.
- El número de aciertos sigue una distribución binomial: `P(≥ 1) = 1 − (1−p)^N = 0,937`, es decir, casi seguro que al menos una estructura «acierta»;
- 🎯 **Por qué importa:** Con suficientes estructuras, suficientes objetivos celestes y una tolerancia generosa, siempre aparece alguna «alineación». La pregunta motivadora es: ¿cuántas alineaciones esperaríamos si nadie hubiese mirado el cielo?

📘 **Dónde se aprende** (1 clase): [B02-C09 · Alineaciones arqueológicas y sesgos](../programa/clases/B02/B02-C09-alineaciones-arqueologicas-y-sesgos/CLASE.md).

### Acimut

- El acimut `Az` de un trayecto es el ángulo desde el norte, hacia el este (0° norte, 90° este).
- El acimut de una dirección es su ángulo medido desde el norte hacia el este (0° norte, 90° este, 180° sur, 270° oeste).
- El acimut `A` es el ángulo desde el norte hacia el este (C01).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- El acimut inicial sale de `tan Az = cos φ₂ sen Δλ / (cos φ₁ sen φ₂ − sen φ₁ cos φ₂ cos Δλ)` (S2, ec. 5-4b), que se evalúa con `atan2` para obtener el cuadrante (C10).
- Quien lea un mapa con ejes rectos pensará que ir «hacia el este» es lo más corto; el círculo máximo sube hacia el polo (su acimut inicial es 11,5°, casi hacia el norte) y es mucho más corto.
- ⚠️ **Error frecuente:** Olvidar el cuadrante del acimut. Se corrige con `atan2` y el ejercicio 5.
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.

📘 **Dónde se aprende** (5 clases): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md); [B08-C01 · Orientación geográfica y puntos cardinales](../programa/clases/B08/B08-C01-orientacion-geografica-y-puntos-cardinales/CLASE.md); [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B57-C07 · Sistemas radar SAR](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md); [B133-C01 · Relaciones entre cielo y territorio en los saberes tradicionales](../programa/clases/B133/B133-C01-relaciones-entre-cielo-y-territorio-en-los-saberes-tradicionales/CLASE.md).

### Acimut de lanzamiento

- El acimut de lanzamiento es la dirección horizontal de la velocidad.

🎯 **Por qué importa (clase B77-C11):** Si el vehículo despega fuera de la ventana, el plano que alcanza no es el deseado y corregirlo cuesta `Δv`. La decisión central: ¿a qué hora sideral y con qué acimut se lanza para entrar en un plano dado, y cuánto error produce un retraso?

📘 **Dónde se aprende** (1 clase): [B77-C11 · Ventanas de lanzamiento — Dinámica de lanzamiento y reentrada](../programa/clases/B77/B77-C11-ventanas-de-lanzamiento-dinamica-de-lanzamiento-y-reentrada/CLASE.md).

### Acoplamiento

- El acoplamiento mide cuánto depende una parte de otra: bajo acoplamiento significa que puedes cambiar una sin romper la otra.
- El acoplamiento `q` mide cuánto se filtran.
- El acoplamiento `χ` es la fracción de ese ritmo que se acumula.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B37-C12](../programa/clases/B37/B37-C12-gigantes-rojas-oscilantes-y-modos-mixtos/CLASE.md):**
- *Descripción textual:* la relación de acoplamiento se resuelve por raíces en cada orden p y se contrasta con el recuento de modos g.
- Límite: forma asintótica con acoplamiento constante.
- 🎯 **Por qué importa:** El espaciado de los períodos mixtos revela el núcleo. La decisión central: ¿cuántos modos mixtos hay por orden p y cómo distingue `ΔΠ₁` la rama de gigantes del núcleo de helio?

📘 **Dónde se aprende** (8 clases): [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md); [B37-C12 · Gigantes rojas oscilantes y modos mixtos](../programa/clases/B37/B37-C12-gigantes-rojas-oscilantes-y-modos-mixtos/CLASE.md); [B42-C15 · Espejos deformables](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md); [B57-C20 · Caso de estudio climático o geológico de Chile](../programa/clases/B57/B57-C20-caso-de-estudio-climatico-o-geologico-de-chile/CLASE.md); [B78-C17 · Masa de propelente y presupuesto](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md); [B97-C15 · Impresión 3D espacial](../programa/clases/B97/B97-C15-impresion-3d-espacial/CLASE.md) y 2 más.

### Acoplamiento débil

- El acoplamiento débil (*loosely coupled*) usa como medición una posición que otro módulo ya calculó.

💡 **Cómo se explica en la clase [B80-C04](../programa/clases/B80/B80-C04-fusion-inercial-con-mediciones-externas-acoplamiento-debil-y-fuerte/CLASE.md):**
- Con distancias a dos balizas cada `10 s` (excepto en `100–200 s`, en que solo se ve una), el acoplamiento débil deja `7,20 m` y el fuerte `5,95 m`, `1,21` veces mejor.
- ⚠️ **Error frecuente:** Creer que el acoplamiento débil siempre equivale al fuerte. Se corrige con 8.3.
- 🎯 **Por qué importa:** B74-C08..C10 dan los filtros, pero ninguna clase los aplica a la unión de una IMU con una fuente externa. La decisión central: ¿en qué nivel se funden la inercia y la medición externa, y qué se pierde o se gana al elegirlo?

📘 **Dónde se aprende** (1 clase): [B80-C04 · Fusión inercial con mediciones externas (acoplamiento débil y fuerte)](../programa/clases/B80/B80-C04-fusion-inercial-con-mediciones-externas-acoplamiento-debil-y-fuerte/CLASE.md).

### Acoplamiento fuerte

- El acoplamiento fuerte (*tightly coupled*) usa las observaciones brutas (aquí, distancias).

💡 **Cómo se explica en la clase [B80-C04](../programa/clases/B80/B80-C04-fusion-inercial-con-mediciones-externas-acoplamiento-debil-y-fuerte/CLASE.md):**
- Por eso el acoplamiento fuerte no se detiene entre `100 s` y `200 s`.
- 🎯 **Por qué importa:** B74-C08..C10 dan los filtros, pero ninguna clase los aplica a la unión de una IMU con una fuente externa. La decisión central: ¿en qué nivel se funden la inercia y la medición externa, y qué se pierde o se gana al elegirlo?

📘 **Dónde se aprende** (1 clase): [B80-C04 · Fusión inercial con mediciones externas (acoplamiento débil y fuerte)](../programa/clases/B80/B80-C04-fusion-inercial-con-mediciones-externas-acoplamiento-debil-y-fuerte/CLASE.md).

### Acortamiento axial

- El acortamiento axial `ΔL` es el cambio de longitud.

💡 **Cómo se explica en la clase [B105-C05](../programa/clases/B105/B105-C05-cambios-de-vision/CLASE.md):**
- *Descripción textual:* el desplazamiento de líquidos presiona el globo; el acortamiento axial se convierte en dioptrías con la sensibilidad `n/L²` y se estima cuántas personas de una población sintética superan un umbral.
- 🎯 **Por qué importa:** Una variación de décimas de milímetro puede cambiar la refracción en fracciones de dioptría y comparar eso con el error de medida decide si un cambio es real. La decisión central: ¿cuántos milímetros de acortamiento equivalen a una dioptría y cuántas personas la superarían?

📘 **Dónde se aprende** (1 clase): [B105-C05 · Cambios de visión](../programa/clases/B105/B105-C05-cambios-de-vision/CLASE.md).

### Acotada u oscilante

- Es secular si crece de forma sistemática con el tiempo (lineal en el número de vueltas) y acotada u oscilante si sube y baja sin acumularse.

🎯 **Por qué importa (clase B11-C10):** Un análisis de misión puede necesitar propagar un satélite durante años, es decir, decenas de miles de vueltas. Si cada vuelta añade o quita un poco de energía, la altura de la órbita cambia solo por culpa del programa.

📘 **Dónde se aprende** (1 clase): [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md).

### Acreción

- La acreción es la caída de gas sobre el objeto, a un ritmo `Ṁ` (masa por tiempo).
- La acreción es la caída de materia sobre un cuerpo compacto.
- La acreción es la captura de una molécula del gas por un grano.

💡 **Cómo se explica en la clase [B24-C02](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md):**
- Un ritmo natural de acreción es del orden de `c_s³/G` (estimación de orden de magnitud con el `c_s` de C01): para `10 K` da `1,6 × 10⁻⁶ M☉/año`.
- Paso 4 · Sentido. Por acreción la protoestrella puede ser casi ocho veces más luminosa que el Sol aunque no fusione nada.
- ⚠️ **Error frecuente:** Pensar que acreción y fusión son lo mismo. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una protoestrella brilla, pero no por el motor que alimenta al Sol. Para saber de dónde sale su energía, cuánto tiempo puede brillar así y cómo distinguirla de una estrella ya estable hay que seguir la energía gravitatoria.

📘 **Dónde se aprende** (3 clases): [B24-C02 · Formación de protoestrellas](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md); [B25-C11 · Núcleos activos de galaxias](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md); [B60-C04 · Balance químico gas-grano: modelos de tres fases](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md).

### Acreción de guijarros

- La acreción de guijarros es la captura de partículas de centímetros arrastradas por el gas.

🎯 **Por qué importa (clase B52-C08):** El orden de magnitud de la masa del núcleo y el tiempo en alcanzarlo deciden si hay gigantes gaseosos. La decisión central: ¿a qué masa un núcleo pasa de capturar gas hasta Bondi a capturarlo hasta Hill, y cuánto tarda en crecer?

📘 **Dónde se aprende** (1 clase): [B52-C08 · Formación de gigantes gaseosos](../programa/clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md).

### Actitud de punto medio

- La actitud de punto medio usa `q` a mitad del paso para rotar `f`, lo que sube el orden del método de uno a dos.

💡 **Cómo se explica en la clase [B80-C03](../programa/clases/B80/B80-C03-mecanizacion-strapdown-e-integracion-de-actitud-y-velocidad/CLASE.md):**
- La mecanización con la exponencial del cuaternión y actitud de punto medio (`Δt = 0,01 s`) tiene un error de posición de `4,014 × 10⁻⁵ m`; la integración con Euler y actitud de inicio de paso, `0,1071 m`.
- 🎯 **Por qué importa:** Las clases B10-C12..C15 dan las rotaciones y los cuaterniones, pero ninguna construye la cadena completa actitud → velocidad → posición. La decisión central: ¿cómo se integra la actitud para que el error numérico no domine al error del sensor?

📘 **Dónde se aprende** (1 clase): [B80-C03 · Mecanización strapdown e integración de actitud y velocidad](../programa/clases/B80/B80-C03-mecanizacion-strapdown-e-integracion-de-actitud-y-velocidad/CLASE.md).

### Activa

- La rotación activa mueve el vector y deja fijos los ejes; la pasiva deja fijo el vector y expresa sus coordenadas en ejes girados.

💡 **Cómo se explica en la clase [B10-C12](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md):**
- Con `θ = 30°` y `v = (1, 0)`: activa, `R(30°) v = (0,866; 0,5)` (el vector se gira hacia arriba); pasiva, `R(30°)ᵀ v = (0,866; −0,5)` (las coordenadas de `v` en ejes que giraron 30° tienen la componente `y` negativa).
- En SPICE, la matriz `[w]ᵢ` «rota el sistema de coordenadas `w` radianes alrededor del eje `i` y rota los vectores `−w`» (S1): su matriz es la transpuesta de la activa.
- ⚠️ **Error frecuente:** Confundir rotación activa y pasiva (signo). Se corrige con los ejercicios 2 y 11.
- 🎯 **Por qué importa:** La Tierra gira una vuelta cada 23,93 horas: una estación de seguimiento ve pasar los satélites porque sus ejes locales rotan respecto del espacio inercial. Un satélite recibe órdenes expresadas en ejes terrestres y debe saber dónde están en ejes inerciales.

📘 **Dónde se aprende** (1 clase): [B10-C12 · Rotaciones en el plano y espacio](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md).

### Activación

- La activación `A` es la desviación de una respuesta fisiológica o emocional respecto de su línea base, en unidades arbitrarias.

💡 **Cómo se explica en la clase [B113-C02](../programa/clases/B113/B113-C02-ansiedad-y-respuesta-emocional-en-escenarios-simulados/CLASE.md):**
- Dentro de una exposición, con `τ = 8 min`, la activación vuelve al `10 %` del pico a los `τ ln 10 = 18,42 min`.
- *Descripción textual:* cada exposición tiene un pico menor que la anterior hasta un nivel `A_∞`; dentro de cada una, la activación decae con constante `τ`.
- 🎯 **Por qué importa:** Ninguna clase previa trata la respuesta emocional ante simulaciones de riesgo. La decisión central: ¿cuántas repeticiones de un escenario hacen falta para que el pico baje a un nivel de trabajo, y cuándo la repetición deja de ayudar?

📘 **Dónde se aprende** (1 clase): [B113-C02 · Ansiedad y respuesta emocional en escenarios simulados](../programa/clases/B113/B113-C02-ansiedad-y-respuesta-emocional-en-escenarios-simulados/CLASE.md).

### Actividad

- La actividad agrupa manchas, fulguraciones y emisión coronal.
- La actividad `A = λN`.

💡 **Cómo se explica en la clase [B24-C12](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md):**
- Los ciclos de actividad, como el solar, se observan en el largo plazo (S1).
- Monitorización de líneas cromosféricas: ciclos de actividad.
- 🎯 **Por qué importa:** La modulación del brillo por manchas permite medir el periodo de rotación de miles de estrellas sin necesitar espectros, pero también contamina la búsqueda de exoplanetas y limita la precisión de las velocidades radiales.

📘 **Dónde se aprende** (2 clases): [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md); [B31-C08 · Decaimiento radiactivo](../programa/clases/B31/B31-C08-decaimiento-radiactivo/CLASE.md).

### Actividad de ciencia

- Una actividad de ciencia enseña un método o resultado científico.

🎯 **Por qué importa (clase B133-C05):** Enseñar «con» una cultura es más que añadir una diapositiva: exige repartir roles, acordar protocolos y medir bien. La decisión central: ¿cómo se organiza una unidad para que el saber lo presente quien lo porta y la ciencia se enseñe con rigor, en el mismo hilo?

📘 **Dónde se aprende** (1 clase): [B133-C05 · Diseño de una unidad de enseñanza intercultural](../programa/clases/B133/B133-C05-diseno-de-una-unidad-de-ensenanza-intercultural/CLASE.md).

### Actividad de diálogo

- Una actividad de diálogo pone ambos en conversación.

🎯 **Por qué importa (clase B133-C05):** Enseñar «con» una cultura es más que añadir una diapositiva: exige repartir roles, acordar protocolos y medir bien. La decisión central: ¿cómo se organiza una unidad para que el saber lo presente quien lo porta y la ciencia se enseñe con rigor, en el mismo hilo?

📘 **Dónde se aprende** (1 clase): [B133-C05 · Diseño de una unidad de enseñanza intercultural](../programa/clases/B133/B133-C05-diseno-de-una-unidad-de-ensenanza-intercultural/CLASE.md).

### Actividad de saber

- Una actividad de saber presenta un saber de la comunidad y la lidera quien lo porta.

🎯 **Por qué importa (clase B133-C05):** Enseñar «con» una cultura es más que añadir una diapositiva: exige repartir roles, acordar protocolos y medir bien. La decisión central: ¿cómo se organiza una unidad para que el saber lo presente quien lo porta y la ciencia se enseñe con rigor, en el mismo hilo?

📘 **Dónde se aprende** (1 clase): [B133-C05 · Diseño de una unidad de enseñanza intercultural](../programa/clases/B133/B133-C05-diseno-de-una-unidad-de-ensenanza-intercultural/CLASE.md).

### Actividad del agua

- La actividad del agua `aw` mide cuánta agua está disponible para los organismos.
- La actividad del agua `a_w` es 1 para agua pura y menor con solutos.

💡 **Cómo se explica en la clase [B56-C05](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md):**
- Cada ambiente es un punto en el plano (temperatura, actividad del agua); los límites forman un rectángulo.
- La política COSPAR de 2026 fija, para la replicación de microorganismos terrestres, una actividad del agua mínima de 0,5 y una temperatura mínima de −28 °C, e indica que ambos límites incluyen márgenes por debajo de los límites reportados de la biología terrestre (S1, consultada el 2026-11-09).
- 🎯 **Por qué importa:** Decidir si un ambiente es habitable, o si una nave puede contaminarlo, exige umbrales de temperatura y de agua disponible. La decisión central: dada la temperatura y la actividad del agua de un ambiente, ¿está dentro de los límites en que la vida terrestre puede replicarse?

📘 **Dónde se aprende** (2 clases): [B56-C05 · Extremófilos y límites ambientales](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md); [B64-C04 · Halófilos y vida en salmueras](../programa/clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md).

### Activo

- Un activo es un enlace a un archivo.
- Un activo es algo que vale la pena proteger.

💡 **Cómo se explica en la clase [B122-C03](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md):**
- R6 (proveedor único de software) no tiene ningún control: es el activo sin protección.
- *Descripción textual:* activo y amenaza definen un riesgo inherente; los controles reducen la probabilidad y dejan el riesgo residual, que se clasifica.
- 🎯 **Por qué importa:** B83-C16 trata riesgos técnicos y B119-C14 amenazas sin modelo. La decisión central: ¿qué riesgo residual domina y qué activo carece de controles?

📘 **Dónde se aprende** (2 clases): [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md); [B122-C03 · Modelo defensivo de riesgos de infraestructura espacial](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md).

### Actor

- Un actor es quien tiene obligaciones.

🎯 **Por qué importa (clase B119-C33):** B119 presenta los instrumentos uno por uno; distinguir qué obligaciones recaen en Estados y en operadores exige compararlos sistemáticamente. Esta clase integra las clases C01 a C11 y es la evidencia de portafolio del bloque.

📘 **Dónde se aprende** (1 clase): [B119-C33 · Matriz comparativa de obligaciones jurídicas por actor](../programa/clases/B119/B119-C33-matriz-comparativa-de-obligaciones-juridicas-por-actor/CLASE.md).

### Actuales

- El cociente de reacción `Q` tiene la misma forma que `K` pero con las concentraciones o presiones actuales.

🎯 **Por qué importa (clase B06-C13):** Según el cálculo de esta clase, el CO₂ de Marte puede condensarse como hielo o volver al gas según la temperatura. Es un equilibrio entre CO₂ sólido y gas: `CO₂(s) ⇌ CO₂(g)`.

📘 **Dónde se aprende** (1 clase): [B06-C13 · Equilibrio químico](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md).

### Actualización

- Una actualización combina la posición previa con una observación.
- La actualización minimiza el error relativo de frecuencias en `(s_E, s₃)`.
- La actualización usa el residuo `z = b_m − Â r`.

💡 **Cómo se explica en la clase [B84-C30](../programa/clases/B84/B84-C30-correlacion-modelo-ensayo-y-actualizacion-de-modelos/CLASE.md):**
- *Descripción textual:* el modelo y el ensayo se comparan por frecuencia, MAC y ortogonalidad cruzada; una actualización de parámetros cierra el ciclo.
- Descripción larga: el modelo cumple los criterios antes y después; la actualización mejora el error pero no recupera los parámetros verdaderos.
- 🎯 **Por qué importa:** Un MAC de 0,999 no basta: puede coexistir con un error de 3,6 % en frecuencia, y actualizar parámetros que no se pueden identificar da un modelo que ajusta pero no es físico. La decisión central: ¿cumple el modelo los criterios de correlación y qué parámetros se pueden actualizar con los datos?

📘 **Dónde se aprende** (3 clases): [B58-C19 · Comunicación pública del riesgo](../programa/clases/B58/B58-C19-comunicacion-publica-del-riesgo/CLASE.md); [B84-C30 · Correlación modelo-ensayo y actualización de modelos](../programa/clases/B84/B84-C30-correlacion-modelo-ensayo-y-actualizacion-de-modelos/CLASE.md); [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md).

### Actualización bayesiana

- La actualización bayesiana usa sensibilidad `s` y tasa de falsa alarma `f`.

🎯 **Por qué importa (clase B111-C05):** B12 da herramientas estadísticas, no la decisión grupal bajo presión. La decisión central: ¿cuándo vale más el grupo que el individuo y cuándo la correlación borra esa ventaja?

📘 **Dónde se aprende** (1 clase): [B111-C05 · Toma de decisiones con incertidumbre en equipo](../programa/clases/B111/B111-C05-toma-de-decisiones-con-incertidumbre-en-equipo/CLASE.md).

### Acuerdo

- El acuerdo entre dos definiciones es la fracción de casos con el mismo veredicto; el kappa de Cohen descuenta el acuerdo esperado por azar: `κ = (p_o − p_e)/(1 − p_e)`.
- El acuerdo es el documento que fija todo lo anterior.

💡 **Cómo se explica en la clase [B56-C01](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md):**
- El acuerdo de `D1` con `D2` es 7 de 8 y `κ = 0,600`; el de `D2` con `D4` es 5 de 8 y `κ = 0,143`.
- El kappa corrige por azar: si ambas reglas dicen «no vivo» casi siempre, el acuerdo alto es poco informativo.
- 🎯 **Por qué importa:** Una misión que busca vida necesita saber qué buscar y qué contará como hallazgo. Si el criterio es vago, cualquier resultado se puede discutir; si es demasiado estrecho, se pasa por alto lo que no se parece a la vida terrestre.

📘 **Dónde se aprende** (2 clases): [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md); [B133-C03 · Colaboración con comunidades en investigación y educación](../programa/clases/B133/B133-C03-colaboracion-con-comunidades-en-investigacion-y-educacion/CLASE.md).

### Acuerdo entre revisores

- Correlación: acuerdo lineal entre nota y mérito. Acuerdo entre revisores: cuánto coinciden entre sí.

🎯 **Por qué importa (clase B48-C03):** Si la nota es muy ruidosa, el comité selecciona al azar sin saberlo. La decisión central: ¿cuántos revisores hacen falta para que la nota sea confiable?

📘 **Dónde se aprende** (1 clase): [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md).

### Acuerdo entre vías

- El estado es el par posición–velocidad en un instante. Acuerdo entre vías es la diferencia relativa máxima entre los resultados.

🎯 **Por qué importa (clase B71-C10):** Dos números describen la forma de la órbita, y un error pequeño de velocidad los cambia mucho. La decisión central: ¿cómo recuperas `a` y `e` desde un estado medido y cuánto cambian si la velocidad tiene un error?

📘 **Dónde se aprende** (1 clase): [B71-C10 · Semieje mayor y excentricidad](../programa/clases/B71/B71-C10-semieje-mayor-y-excentricidad/CLASE.md).

### Acuerdo esperado por azar

- El acuerdo esperado por azar `pₑ` se calcula con las proporciones de cada anotador; el kappa de Cohen es `κ = (pₒ − pₑ)/(1 − pₑ)`, mide el acuerdo más allá del azar y compara a dos anotadores entre sí, no a un modelo con la verdad (S2).

🎯 **Por qué importa (clase B17-C10):** Se quiere entrenar un modelo que distinga galaxias espirales de elípticas. Hay un millón de imágenes y nadie las ha etiquetado.

📘 **Dónde se aprende** (1 clase): [B17-C10 · Conjuntos de datos etiquetados para aprendizaje supervisado](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md).

### Acuerdo exacto

- El acuerdo exacto es la fracción de pares con el mismo nivel; el adyacente, con diferencia de a lo sumo un nivel.

💡 **Cómo se explica en la clase [B131-C09](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md):**
- Acuerdo exacto `50/120 = 0,417`, adyacente `101/120 = 0,842`, `κ = 0,205`, `κ ponderado = 0,435` y un sesgo de `+0,32` niveles del evaluador B (configurado así en la simulación).
- Con ruido menor y sin sesgo: acuerdo exacto `0,675`, adyacente `0,983`, `κ = 0,531`, `κ ponderado = 0,757`, sesgo `+0,01`.
- ⚠️ **Error frecuente:** Reportar solo el acuerdo exacto. Se corrige con 8.1 y el ejercicio 7.
- 🎯 **Por qué importa:** Una rúbrica sin acuerdo entre evaluadores asigna notas que dependen de quién corrige. La decisión central: ¿dos personas distintas darían el mismo nivel a este trabajo, y cómo lo sabes?

📘 **Dónde se aprende** (1 clase): [B131-C09 · Rúbricas de evaluación](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md).

### Acuerdo observado

- El acuerdo observado `pₒ` es la fracción de objetos en que dos anotadores dan la misma etiqueta.
- El acuerdo observado `p_o` es la fracción de coincidencias.

💡 **Cómo se explica en la clase [B119-C26](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md):**
- Descripción larga: el acuerdo observado es moderado y el kappa lo corrige a la baja al descontar el azar.
- 🎯 **Por qué importa:** C11 y C12 tratan los límites militares y la historia; ninguna clase enseña a leer doctrinas públicas con rigor. La lectura real de documentos oficiales exige fuentes que no se consultaron aquí.

📘 **Dónde se aprende** (2 clases): [B17-C10 · Conjuntos de datos etiquetados para aprendizaje supervisado](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md); [B119-C26 · Doctrinas y políticas espaciales declaradas públicamente](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md).

### Acuerdo por azar

- El acuerdo por azar `p_e` se calcula de las marginales.

🎯 **Por qué importa (clase B119-C26):** C11 y C12 tratan los límites militares y la historia; ninguna clase enseña a leer doctrinas públicas con rigor. La lectura real de documentos oficiales exige fuentes que no se consultaron aquí.

📘 **Dónde se aprende** (1 clase): [B119-C26 · Doctrinas y políticas espaciales declaradas públicamente](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md).

### Acumulación

- La acumulación cuenta cuántas celdas drenan a cada una.
- La acumulación eleva la temperatura `dT/dt = S/(m c)` con `c = 3.470 J/(kg·K)`.

💡 **Cómo se explica en la clase [B66-C04](../programa/clases/B66/B66-C04-redes-fluviales-fosiles-y-paleohidrologia-marciana/CLASE.md):**
- En un plano inclinado sin ruido que desciende hacia `+j`, la acumulación exacta en la columna `j` es `j + 1` para cualquier fila.
- *Descripción textual:* el terreno se rellena, se calculan direcciones y acumulación, se definen canales con un umbral y del área mayor sale el caudal y la duración mínima.
- 🎯 **Por qué importa:** Un mapa de valles marcianos invita a decir «hubo un océano» o «hubo lluvia». La decisión central: ¿qué se puede inferir del caudal y de la duración con una red, un volumen y supuestos explícitos, y qué incertidumbre arrastra?

📘 **Dónde se aprende** (2 clases): [B66-C04 · Redes fluviales fósiles y paleohidrología marciana](../programa/clases/B66/B66-C04-redes-fluviales-fosiles-y-paleohidrologia-marciana/CLASE.md); [B105-C23 · Termorregulación humana en vuelo](../programa/clases/B105/B105-C23-termorregulacion-humana-en-vuelo/CLASE.md).

### Acumulador

- Un acumulador es una variable que se actualiza en cada vuelta (`total = total + x`).

🎯 **Por qué importa (clase B07-C05):** Una simulación es un bucle: calcula el estado siguiente a partir del actual, una y otra vez. Si el paso es demasiado grande, el resultado se aparta de la realidad; si es demasiado pequeño, tarda.

📘 **Dónde se aprende** (1 clase): [B07-C05 · Bucles y simulaciones sencillas](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md).

### Acusar recibo

- La potencia permisible es el nivel máximo de interferencia aceptado en la estación afectada. Acusar recibo es confirmar que se recibió la solicitud.

🎯 **Por qué importa (clase B120-C02):** Coordinar con otros servicios define dónde y cómo se puede operar y ninguna clase lo trata. La decisión central: ¿con qué administraciones hay que coordinar una estación terrena y en cuánto tiempo deben responder?

📘 **Dónde se aprende** (1 clase): [B120-C02 · Zonas de coordinación entre servicios radioeléctricos](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md).

### ACWR

- La ACWR es su cociente.

💡 **Cómo se explica en la clase [B107-C05](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md):**
- Para `ACWR ≤ 1,3` con crónica previa de 100: `a/((300 + a)/4) ≤ 1,3`, es decir `a ≤ 144,4`: un aumento del 44 %.
- Una curva logística en U inventada (`logit = −3 + 3 (ACWR − 1)²`) da `7,4 %` para 0,6, `4,7 %` para 1,0, `6,1 %` para 1,3 y `12,8 %` para 1,6.
- 🎯 **Por qué importa:** El fragmento consultado de English et al. (2015) subraya que la pérdida de fuerza en misiones largas implica riesgos operativos y médicos, entre ellos el egreso de emergencia; y Loehr et al.

📘 **Dónde se aprende** (1 clase): [B107-C05 · Prevención de lesiones en entrenamiento y trabajo operativo](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md).

### AD2

- La AD2 (dificultad de avance, S5) estima cuán difícil es subir de nivel; aquí es una escala 1–5 sintética.

💡 **Cómo se explica en la clase [B83-C18](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md):**
- Con 3 meses por nivel y un factor de dificultad `1 + 0,25·(AD2 − 1)`, el esfuerzo a TRL 6 es de 18,75 meses-elemento; si todo avanza en paralelo, el plazo lo fija Detector de imagen: 10,50 meses.
- A["AD2 por elemento"] --> P["Esfuerzo de madurizacion"]
- 🎯 **Por qué importa:** Un elemento «con herencia de vuelo» que se usa en otro entorno no es TRL 9. La decisión central: ¿cuál es el TRL real del sistema, qué elementos lo frenan y cuánto cuesta llevarlos al nivel que pide la revisión?

📘 **Dónde se aprende** (1 clase): [B83-C18 · Niveles de madurez tecnológica](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md).

### Adaptación a la oscuridad

- La adaptación a la oscuridad es el proceso por el que el ojo gana sensibilidad tras minutos en la oscuridad.

🎯 **Por qué importa (clase B08-C12):** La mayoría de las personas ya no ve la Vía Láctea desde su casa. La pregunta motivadora: ¿qué tan oscuro es mi cielo, cuánto de eso es culpa de la Luna y cuánto de las luces, y qué puedo hacer?

📘 **Dónde se aprende** (1 clase): [B08-C12 · Limitación por contaminación lumínica](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md).

### Adaptación de impedancias

- La adaptación de impedancias impone igualdad de presión y velocidad de partícula en el contacto.

🎯 **Por qué importa (clase B53-C10):** Un cráter es una medida indirecta del impacto. La decisión central: ¿cómo cambia el diámetro del cráter con la gravedad y qué incertidumbre tiene un exponente ajustado a pocos experimentos?

📘 **Dónde se aprende** (1 clase): [B53-C10 · Geología de impacto](../programa/clases/B53/B53-C10-geologia-de-impacto/CLASE.md).

### Adaptación incompleta

- La adaptación incompleta ocurre porque `A < 1`.

🎯 **Por qué importa (clase B105-C25):** Quien se adapta a un entorno nuevo comete errores al volver al anterior. Entender el ritmo de adaptación y el postefecto permite diseñar el entrenamiento y anticipar las torpezas.

📘 **Dónde se aprende** (1 clase): [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md).

### Adaptador

- Un adaptador traduce entre el mundo exterior (archivos, unidades, formatos, configuración) y el núcleo.
- Propiedad: valor expuesto por un driver. Adaptador: capa que traduce a una operación común.

💡 **Cómo se explica en la clase [B14-C01](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md):**
- Dentro del núcleo todo está en SI; convertir es trabajo del adaptador.
- El adaptador convierte a SI y rechaza las unidades que no conoce.
- 🎯 **Por qué importa:** Un script de 300 líneas que lee un archivo, calcula una órbita, dibuja una figura y escribe un informe funciona hasta el día en que cambias el archivo de entrada. Entonces no sabes si un resultado distinto viene de los datos, de la fórmula o de un error nuevo.

📘 **Dónde se aprende** (2 clases): [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md); [B48-C21 · Protocolos estándar de control instrumental (ASCOM e INDI)](../programa/clases/B48/B48-C21-protocolos-estandar-de-control-instrumental-ascom-e-indi/CLASE.md).

### Adaptativo

- Un procedimiento adaptativo aumenta el número de pruebas hasta que los resultados se estabilizan en un sentido estadístico (S1, 7.9).

💡 **Cómo se explica en la clase [B12-C14](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md):**
- También propone un procedimiento adaptativo que detiene la simulación cuando los resultados se estabilizan (S1, 7.9).
- 🎯 **Por qué importa:** Casi ningún modelo de misión admite una fórmula cerrada para la incertidumbre de su salida: hay no linealidades, restricciones y combinaciones de entradas. La simulación Monte Carlo reemplaza el álgebra por repetición: se sortean entradas, se evalúa el modelo y se resume la salida.

📘 **Dónde se aprende** (1 clase): [B12-C14 · Simulación Monte Carlo](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md).

### ADC

- El ADC convierte voltaje en cuentas con `b` bits.

💡 **Cómo se explica en la clase [B44-C18](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md):**
- Un ADC de 12 bits (`7,05 e⁻`) con este pozo supera al ruido de lectura de `4 e⁻`.
- ADC["bits del ADC"] --> Q["cuantización"]
- 🎯 **Por qué importa:** Leer lento reduce ruido pero desperdicia tiempo de observación. La decisión central: ¿qué modo de lectura equilibra ruido y tiempo muerto?

📘 **Dónde se aprende** (1 clase): [B44-C18 · Control electrónico de cámaras](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md).

### Adiabata

- La adiabata `T = T₀ (P/P₀)^κ` con `κ = R/(M c_p)`.

💡 **Cómo se explica en la clase [B54-C13](../programa/clases/B54/B54-C13-atmosfera-de-venus/CLASE.md):**
- Adiabata de gas ideal: lo que hace la clase.
- ⚠️ **Error frecuente:** Presentar la adiabata como perfil medido. Se corrige con 8.4.
- 🎯 **Por qué importa:** Venus es el caso extremo de atmósfera densa y caliente. La pregunta motivadora: ¿cómo se enfría su atmósfera con la altura y cuánto pesa?

📘 **Dónde se aprende** (1 clase): [B54-C13 · Atmósfera de Venus](../programa/clases/B54/B54-C13-atmosfera-de-venus/CLASE.md).

### Adiabata profunda

- La adiabata profunda es `T = T₁ (P/P₁)^κ`.

💡 **Cómo se explica en la clase [B54-C15](../programa/clases/B54/B54-C15-atmosferas-de-gigantes-gaseosos/CLASE.md):**
- KAP["kappa = 2/7"] --> AD["adiabata profunda"]
- 🎯 **Por qué importa:** La atmósfera de Júpiter es una capa convectiva muy profunda. La pregunta motivadora: ¿cuánto más caliente es el nivel de 1 bar que el equilibrio solar y cómo crece la temperatura hacia dentro?

📘 **Dónde se aprende** (1 clase): [B54-C15 · Atmósferas de gigantes gaseosos](../programa/clases/B54/B54-C15-atmosferas-de-gigantes-gaseosos/CLASE.md).

### Adiabático

- El modelo isotermo supone temperatura constante del gas; el adiabático, ausencia de intercambio de calor.

💡 **Cómo se explica en la clase [B114-C05](../programa/clases/B114/B114-C05-despresurizacion-escenarios-tiempos-y-respuesta/CLASE.md):**
- El modelo adiabático da `1666,5 s`, un `77 %` del isotermo: al enfriarse el gas restante, la presión cae antes.
- 🎯 **Por qué importa:** Entre una grieta de `1 mm` y una brecha de `100 mm` el tiempo disponible pasa de días a segundos. La decisión central: ¿cuánto tiempo hay hasta un umbral de presión y alcanza para responder?

📘 **Dónde se aprende** (1 clase): [B114-C05 · Despresurización: escenarios, tiempos y respuesta](../programa/clases/B114/B114-C05-despresurizacion-escenarios-tiempos-y-respuesta/CLASE.md).

### Adimensional

- Una cantidad adimensional no tiene unidad (es un cociente de magnitudes con la misma dimensión), por lo que no cambia al cambiar de sistema de unidades.
- Una cantidad adimensional tiene todas las potencias en cero, como un cociente de dos longitudes.
- Una cantidad adimensional no tiene unidad neta.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B17-C01](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md):**
- Lo importante es que cada característica tenga una unidad declarada (o sea adimensional) y una fórmula escrita.
- Segundo, la razón de duración `T_obs / T₀` es adimensional: vale cerca de 1 para un planeta en una estrella como la supuesta y se aleja de 1 si la señal viene de otro fenómeno o de otra estrella (un falso positivo).
- 🎯 **Por qué importa:** Un modelo de aprendizaje automático no sabe física: solo ve números. Si le das la duración de un tránsito en segundos y el periodo en días, la columna con números más grandes domina cualquier cálculo de distancias, y la clasificación depende de una elección de unidades que nada tiene que ver con el cielo.

📘 **Dónde se aprende** (4 clases): [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md); [B07-C11 · Gestión de unidades en programas](../programa/clases/B07/B07-C11-gestion-de-unidades-en-programas/CLASE.md); [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md); [B17-C01 · Ingeniería de características científicas](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md).

### Aditividad

- Un sistema es lineal si cumple aditividad (la respuesta a `u₁ + u₂` es la suma de respuestas) y homogeneidad (la respuesta a `a u` es `a` por la respuesta a `u`); juntas, superposición.

🎯 **Por qué importa (clase B16-C03):** Un ingeniero de control no puede ensayar todos los pares posibles en un telescopio de miles de millones de euros. La esperanza es que, con unas pocas pruebas, se pueda predecir la respuesta a cualquier par.

📘 **Dónde se aprende** (1 clase): [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md).

### ADM

- ADM son armas de destrucción masiva.

💡 **Cómo se explica en la clase [B119-C11](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md):**
- ADM en órbita: prohibido; base militar en la Luna: prohibido; científicos militares en la Luna: condicionado; telescopio civil en un asteroide: permitido; satélite de observación en órbita: fuera del art.
- Paso 2. Sin ADM; hay cuerpo celeste; sin base.
- 🎯 **Por qué importa:** C01 reduce el art. IV a una regla booleana; esta clase lo desagrega por ubicación y propósito y conecta con el art. 3 del Acuerdo sobre la Luna, y deja explícito lo no consultado.

📘 **Dónde se aprende** (1 clase): [B119-C11 · Uso pacífico y limitaciones militares](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md).

### Administración

- Una administración es la autoridad estatal responsable.

💡 **Cómo se explica en la clase [B120-C01](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md):**
- Según el documento consultado, antes de actuar bajo el Artículo 11 la administración envía la publicación anticipada «no antes de siete años y preferentemente no después de dos años» antes de la puesta en servicio planeada.
- Una asignación a una estación espacial geoestacionaria se considera puesta en servicio cuando una estación con capacidad de transmitir o recibir esa frecuencia ha estado desplegada y mantenida en la posición notificada 90 días continuos; la administración informa a la Oficina en los 30 días siguientes (No. 11.44B).
- 🎯 **Por qué importa:** B119-C09 presenta las normas sin el procedimiento. La decisión central: dada la fecha de recepción de la publicación anticipada, ¿entre qué fechas deben ocurrir la coordinación, la notificación y la puesta en servicio, y qué se pierde si no ocurren?

📘 **Dónde se aprende** (1 clase): [B120-C01 · Licencias satelitales y procedimiento de notificación](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md).

### Admisible

- Una variación admisible `η` conserva las condiciones de contorno.

🎯 **Por qué importa (clase B81-C08):** Un resultado que solo se ha verificado con el mismo código no está validado. La decisión central: ¿qué chequeos independientes demuestran que una trayectoria de empuje continuo es correcta y que es un óptimo local?

📘 **Dónde se aprende** (1 clase): [B81-C08 · Validación de trayectorias de empuje continuo](../programa/clases/B81/B81-C08-validacion-de-trayectorias-de-empuje-continuo/CLASE.md).

### ADQL

- Una consulta selecciona filas y columnas con criterios. ADQL es el lenguaje de consultas astronómicas del IVOA y TAP el protocolo para enviarlas (S1).

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- No hay red, autenticación, reintentos, paginación ni descargas parciales; el servidor es local y la consulta ADQL no se envió, de modo que no sé qué respondería un servicio real.
- Consultar en el servidor (TAP/ADQL) reduce lo transferido pero depende de la disponibilidad y del servicio.
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.

📘 **Dónde se aprende** (1 clase): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md).

### Adquisición

- La adquisición es la etapa en que cada terminal localiza al otro.
- La adquisición obtiene los datos del origen.

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- Si el archivo del servidor se altera (el laboratorio le añade un salto de línea), la huella ya no coincide y la adquisición rechaza el archivo con un error explícito.
- Altera el archivo del servidor: la adquisición lo rechaza.
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.

📘 **Dónde se aprende** (2 clases): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md); [B92-C03 · Adquisición, apuntamiento y seguimiento ópticos](../programa/clases/B92/B92-C03-adquisicion-apuntamiento-y-seguimiento-opticos/CLASE.md).

### Adsorción

- Traza: contaminante a concentración muy baja. Adsorción: retención en la superficie de un sólido.

🎯 **Por qué importa (clase B106-C21):** Una cabina cerrada acumula trazas que no son CO₂ ni agua; hay que retirarlas con lechos y catalizadores que se saturan o dependen de la temperatura. La decisión central: ¿cuánto dura un lecho, a qué temperatura debe operar el catalizador y qué concentración queda en la cabina?

📘 **Dónde se aprende** (1 clase): [B106-C21 · Depuración de trazas gaseosas de la atmósfera de cabina](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md).

### ADU

- El ADU (*analog-to-digital unit*) es la unidad del número que entrega el conversor.

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- Con `K = 1`: `10,30` ADU (observado `10,34`).
- La apertura contiene el 99,65 % del flujo (1993 de 2000 ADU).
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.

📘 **Dónde se aprende** (1 clase): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md).

### Advección

- La advección `u_t + c u_x = 0` es de primer orden: transporta el perfil con velocidad `c`.

💡 **Cómo se explica en la clase [B11-C13](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md):**
- Laplace `6,5 × 10⁻⁸`; advección `1,2 × 10⁻¹⁰` absoluto.
- 🎯 **Por qué importa:** El calor que atraviesa un escudo, las ondas en una estructura, el potencial gravitatorio de un cuerpo extenso, el transporte de partículas en un plasma: todos son EDP. Antes de discretizar hay que saber *qué tipo de problema es* (qué datos pide, cómo viaja la información) porque de ello depende el método.

📘 **Dónde se aprende** (1 clase): [B11-C13 · Ecuaciones en derivadas parciales](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md).

### Advertencia

- Una advertencia es la declaración explícita de que un criterio no se cumplió, un supuesto se violó o un límite se alcanzó, con su impacto.

💡 **Cómo se explica en la clase [B23-C08](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md):**
- Pero el informe incluye la advertencia: «Criterio D2 no cumplido: valor 8,806 × 10⁻³ frente a umbral ≤ 0,005 — fuera del uso previsto; limita la extrapolación».
- Después prueba la coherencia: el informe tiene sus siete secciones; cada criterio aparece en la tabla; la decisión coincide con los veredictos de los criterios de uso; cada criterio no cumplido genera una advertencia; y, como control negativo, si se corrompe el valor de D1 (`5 × 10⁻³`), la decisión cambia a NO APTO.
- 🎯 **Por qué importa:** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.

📘 **Dónde se aprende** (1 clase): [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Adyacencia

- Una adyacencia es la cercanía deseada.

🎯 **Por qué importa (clase B109-C02):** Un buen plano ahorra pasos, separa lo sucio de lo limpio y deja las zonas tranquilas lejos de las ruidosas. La decisión central: ¿dónde pongo cada zona para que los recorridos frecuentes sean cortos y las zonas incompatibles estén lejos?

📘 **Dónde se aprende** (1 clase): [B109-C02 · Zonificación y distribución funcional de módulos de un hábitat](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md).

### Adyacente

- El acuerdo exacto es la fracción de pares con el mismo nivel; el adyacente, con diferencia de a lo sumo un nivel.

💡 **Cómo se explica en la clase [B131-C09](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md):**
- Acuerdo exacto `50/120 = 0,417`, adyacente `101/120 = 0,842`, `κ = 0,205`, `κ ponderado = 0,435` y un sesgo de `+0,32` niveles del evaluador B (configurado así en la simulación).
- Con ruido menor y sin sesgo: acuerdo exacto `0,675`, adyacente `0,983`, `κ = 0,531`, `κ ponderado = 0,757`, sesgo `+0,01`.
- 🎯 **Por qué importa:** Una rúbrica sin acuerdo entre evaluadores asigna notas que dependen de quién corrige. La decisión central: ¿dos personas distintas darían el mismo nivel a este trabajo, y cómo lo sabes?

📘 **Dónde se aprende** (1 clase): [B131-C09 · Rúbricas de evaluación](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md).

### Aerofrenado

- El aerofrenado reduce la energía orbital con el arrastre atmosférico en el periapsis.

🎯 **Por qué importa (clase B75-C15):** Cada pasada baja el apoapsis un poco, y hace falta algún margen de seguridad con la densidad. La decisión central: ¿cuántas pasadas y cuánto tiempo hacen falta para bajar el apoapsis, y qué delta-v propulsivo se ahorra?

📖 **Explicado a fondo:** [Aerofrenado](esencial/ampliacion-a-m.md#aerofrenado) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B75-C15 · Aerofrenado conceptual](../programa/clases/B75/B75-C15-aerofrenado-conceptual/CLASE.md).

### Aeroponía

- La aeroponía cultiva con las raíces en el aire y las moja con niebla.

💡 **Cómo se explica en la clase [B115-C04](../programa/clases/B115/B115-C04-sistemas-aeroponicos/CLASE.md):**
- En la comparación de Monje y colaboradores, el APH con sustrato rindió el 51 % del NFT en un experimento puntual, y la aeroponía no apareció como solución ya resuelta.
- Casos de referencia consultados: Monje y colaboradores (2019) señalan que la hidroponía y la aeroponía en el espacio comparten retos de contención, aireación de las raíces y separación líquido/gas; y citan un estudio en el que la masa fresca de brotes de lechuga hidropónica fue el doble que la aeropónica y la de suelo.
- 🎯 **Por qué importa:** En un hábitat, cada litro y cada kilogramo cuentan. La decisión central: ¿cuánto tiempo puede pasar entre dos nieblas sin que la raíz se seque, y cómo depende eso de la humedad de la cámara y del tamaño de las gotas?

📘 **Dónde se aprende** (1 clase): [B115-C04 · Sistemas aeropónicos](../programa/clases/B115/B115-C04-sistemas-aeroponicos/CLASE.md).

### Aerosol

- Un aerosol es una partícula sólida o líquida suspendida en el gas.
- Velocidad de Stokes: velocidad terminal de una esfera pequeña en un fluido viscoso. Aerosol: partículas en suspensión.

🎯 **Por qué importa (clase B54-C08):** La condensación libera calor, forma nubes que cambian el albedo y limita cuánto vapor admite el aire. La pregunta motivadora: ¿a qué altura se forma una nube y cuánto tarda una partícula en caer de ella?

📘 **Dónde se aprende** (2 clases): [B54-C08 · Nubes y aerosoles](../programa/clases/B54/B54-C08-nubes-y-aerosoles/CLASE.md); [B106-C23 · Control de partículas y polvo respirable en cabina](../programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/CLASE.md).

### A-estable

- Un método implícito define el nuevo estado mediante una ecuación que lo contiene; A-estable es el que es estable para todo `Re z < 0`.
- Un método es A-estable si es estable para todo `Re z < 0` y L-estable si además `|R(z)| → 0` cuando `z → −∞`: amortigua del todo los modos muy rápidos.

🎯 **Por qué importa (clase B11-C09):** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.

📘 **Dónde se aprende** (2 clases): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md).

### Afelio

- El perihelio es el punto más cercano al Sol (`a(1−e)`) y el afelio, el más lejano (`a(1+e)`).
- El perihelio `q` es el punto de la órbita más cercano al Sol (que está en un foco) y el afelio `Q` el más lejano.
- El perihelio es el punto más cercano al Sol; el afelio, el más lejano.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C14](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md):**
- Con `a = 227,956` millones de km (Marte, S3) y una excentricidad sintética `e = 0,2`: perihelio `a(1−e) = 182,4` y afelio `a(1+e) = 273,5` millones de km.
- El laboratorio calcula el área barrida durante un décimo del período partiendo del perihelio y durante otro décimo partiendo del afelio: ambas valen `1,5995×10⁴` (unidades de 10¹² km²) y su razón es `1,000000`.
- 🎯 **Por qué importa:** Para Kepler, como para todos antes, el círculo era la figura natural del cielo. Los datos de Tycho no se dejaban describir con círculos.

📘 **Dónde se aprende** (6 clases): [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md); [B75-C01 · Geometría de transferencias heliocéntricas](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md); [B131-C03 · Conocimientos previos y concepciones alternativas](../programa/clases/B131/B131-C03-conocimientos-previos-y-concepciones-alternativas/CLASE.md).

### Afín

- Un desplazamiento `(dy, dx)` es una traslación; una transformación rígida añade rotación; una afín añade escala y cizalla.

🎯 **Por qué importa (clase B15-C14):** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».

📘 **Dónde se aprende** (1 clase): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md).

### Afinado

- El afinado es la reducción de carga antes de un día clave.

💡 **Cómo se explica en la clase [B107-C01](../programa/clases/B107/B107-C01-entrenamiento-cardiorrespiratorio-y-de-resistencia-de-astronautas/CLASE.md):**
- Tras 14 días de afinado, ambos dan máximos casi iguales (`241,83` y `241,91`, día 93).
- El modelo (parámetros inventados: `k1 = 0,10`, `k2 = 0,30`, `τ1 = 42 d`, `τ2 = 7 d`) da `p(día 83) = 193,30` para A y `199,58` para B, y tras 14 días de afinado ambos llegan a un máximo de `241,83` y `241,91` el día 93.
- 🎯 **Por qué importa:** En la literatura consultada, el entrenamiento físico se hace en la ISS desde hace unos diez años y cada agencia diseñó su enfoque (Loehr et al., 2015); las misiones largas causan pérdida de fuerza con riesgos operativos y médicos (English et al., 2015).

📘 **Dónde se aprende** (1 clase): [B107-C01 · Entrenamiento cardiorrespiratorio y de resistencia de astronautas](../programa/clases/B107/B107-C01-entrenamiento-cardiorrespiratorio-y-de-resistencia-de-astronautas/CLASE.md).

### Afirmación

- Una afirmación es lo que el artículo sostiene; la evidencia es lo que la apoya; el límite es lo que la evidencia no permite concluir.

💡 **Cómo se explica en la clase [B20-C04](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md):**
- Antes de redactar, escribe en tres líneas: la afirmación principal, la evidencia (la cifra o figura que la apoya) y el límite.
- Paso 1 · Tres líneas. Afirmación: «en 32 series simuladas, A tiene menor error relativo de período que B».
- 🎯 **Por qué importa:** Un resultado correcto mal comunicado se pierde: nadie sabe qué se midió, con qué incertidumbre ni qué supuestos hay detrás, y no puede reproducirse ni usarse.

📘 **Dónde se aprende** (1 clase): [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Afirmar

- Validar es comprobar la entrada y avisar si es inválida; afirmar (`assert`) es comprobar una condición que el programador cree siempre cierta.

🎯 **Por qué importa (clase B07-C12):** Un programa científico recibe archivos con huecos, texto donde esperaba un número y valores imposibles (un período negativo). Hay dos malas respuestas: dejar que el programa se caiga sin explicar nada y, peor, seguir en silencio con un valor inválido (`nan`, `0`) que contamina el resultado final.

📘 **Dónde se aprende** (1 clase): [B07-C12 · Manejo de errores y excepciones](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md).

### Afrontamiento

- El afrontamiento es el conjunto de maneras de responder a esa carga.

🎯 **Por qué importa (clase B113-C01):** B105-C09 presenta la salud mental en aislamiento, pero no el estrés operacional. La decisión central: ¿sobre qué palanca actuar, bajar la demanda vivida o acelerar la recuperación, y cómo saber si funcionó?

📘 **Dónde se aprende** (1 clase): [B113-C01 · Estrés operacional y estrategias de afrontamiento](../programa/clases/B113/B113-C01-estres-operacional-y-estrategias-de-afrontamiento/CLASE.md).

### Agotamiento

- El agotamiento (burnout) es el fin del empuje.

🎯 **Por qué importa (clase B77-C12):** La trayectoria de ascenso decide a la vez las pérdidas, las cargas y la órbita alcanzada. La decisión central: ¿qué perfil de inclinación lleva al vehículo a una órbita casi circular y qué cuesta?

📘 **Dónde se aprende** (1 clase): [B77-C12 · Perfil de ascenso orbital](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md).

### Agrupación completa

- La agrupación completa fija `θ_j = μ` (equivale a `τ = 0`);
- Agrupación nula (*no pooling*): cada `θ_j` se estima con su `y_j` (equivale a `τ → ∞`). Agrupación completa (*complete pooling*): todos los sensores comparten un valor, el promedio ponderado (equivale a `τ = 0`).

💡 **Cómo se explica en la clase [B12-C21](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md):**
- Agrupación completa: simple, bajo error si los grupos son idénticos, sesgada si no.
- 🎯 **Por qué importa:** Ocho sensores del mismo tipo miden un mismo desfase con errores distintos. Tratarlos como idénticos (agrupación completa) ignora diferencias reales entre ellos; tratarlos como independientes (sin agrupación) desperdicia lo que cada uno enseña de los demás.

📘 **Dónde se aprende** (2 clases): [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md); [B19-C02 · Modelos jerárquicos](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md).

### Agrupación nula

- Nivel 3: ese hiperprior (aquí, plano). Agrupación nula (*no pooling*): cada `θ_j` se estima con su `y_j` (equivale a `τ → ∞`).

💡 **Cómo se explica en la clase [B19-C02](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md):**
- La agrupación nula no toma prestado nada: es honesta con cada sensor pero tiene intervalos anchos y trata como señal lo que puede ser ruido.
- 🎯 **Por qué importa:** Seis sensores de temperatura de un satélite miden cada uno un desvío de calibración. Tres decisiones ingenuas son posibles: tratar a cada sensor por separado, ignorar las diferencias y promediar todo, o confiar en el sensor más preciso.

📘 **Dónde se aprende** (1 clase): [B19-C02 · Modelos jerárquicos](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md).

### Agrupación parcial

- sin agrupación, cada `θ_j` se estima solo con `y_j` (equivale a `τ → ∞`); la agrupación parcial es el caso intermedio.
- Agrupación completa (*complete pooling*): todos los sensores comparten un valor, el promedio ponderado (equivale a `τ = 0`). Agrupación parcial: un compromiso aprendido de los datos.

💡 **Cómo se explica en la clase [B12-C21](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md):**
- Agrupación parcial jerárquica: compromiso, estima la heterogeneidad.
- 🎯 **Por qué importa:** Ocho sensores del mismo tipo miden un mismo desfase con errores distintos. Tratarlos como idénticos (agrupación completa) ignora diferencias reales entre ellos; tratarlos como independientes (sin agrupación) desperdicia lo que cada uno enseña de los demás.

📘 **Dónde se aprende** (2 clases): [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md); [B19-C02 · Modelos jerárquicos](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md).

### Agrupamiento

- El agrupamiento (*clustering*) divide los datos en grupos de elementos similares.
- El agrupamiento (*clustering*) asigna cada objeto a un grupo.

💡 **Cómo se explica en la clase [B15-C23](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md):**
- El agrupamiento puede recuperar las clases solo si están separadas respecto a su dispersión; con mucho solapamiento, el resultado se parece poco a las clases reales.
- 🎯 **Por qué importa:** Un satélite fotografía una región que nadie ha cartografiado. Sin muestras, no se puede entrenar un clasificador, pero sí se puede preguntar cuántos «tipos» de superficie distintos hay en las bandas.

📘 **Dónde se aprende** (2 clases): [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md); [B17-C06 · Aprendizaje no supervisado](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md).

### Agua de hidrato

- El agua de hidrato forma parte de la estructura cristalina de un mineral y se libera calentando.

💡 **Cómo se explica en la clase [B59-C03](../programa/clases/B59/B59-C03-agua-en-regolito-y-minerales/CLASE.md):**
- Una muestra sintética contiene 3,0 % de hielo (se pierde en torno a 190 K), 2,0 % de agua de hidrato (500 K) y 0,5 % de hidroxilo (950 K).
- 🎯 **Por qué importa:** No toda el agua es igual de fácil de extraer: el hielo sale con poco calor y el hidroxilo exige temperaturas casi de fusión. La decisión central: ¿qué parte del agua total se obtiene calentando solo hasta 300 K?

📘 **Dónde se aprende** (1 clase): [B59-C03 · Agua en regolito y minerales](../programa/clases/B59/B59-C03-agua-en-regolito-y-minerales/CLASE.md).

### Agua líquida en superficie

- El agua líquida en superficie exige, al menos, `P > 611,657 Pa` y `273,16 K < T < 647,1 K`.

🎯 **Por qué importa (clase B54-C20):** Comparar mundos tienta a ordenarlos por «habitabilidad». La pregunta motivadora: ¿qué dicen realmente la temperatura y la presión de superficie sobre la posibilidad de agua líquida?

📘 **Dónde se aprende** (1 clase): [B54-C20 · Comparación de habitabilidad climática](../programa/clases/B54/B54-C20-comparacion-de-habitabilidad-climatica/CLASE.md).

### Aguas abajo

- Aguas arriba son las etapas proveedoras; aguas abajo, las que usan sus productos.
- Aguas arriba se llega al origen (necesidad); aguas abajo, a diseño y verificación.

💡 **Cómo se explica en la clase [B83-C05](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md):**
- Si cambia R03 (2 Gbit/día), el recorrido aguas abajo llega a D4 (computadora), D5 (radio) y V3 (ensayo de enlace): 3 elementos.
- Paso 2 · Aguas abajo. R03 → D5 (radio) y D4 (computadora);
- 🎯 **Por qué importa:** Cuando cambia un requisito, ¿qué piezas y qué pruebas hay que revisar? Sin trazabilidad, nadie lo sabe y el cambio rompe algo en silencio.

📘 **Dónde se aprende** (2 clases): [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md); [B124-C01 · Cadena de valor de industria espacial](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md).

### Aguas arriba

- La trazabilidad es el enlace verificable entre elementos del desarrollo. Aguas arriba se llega al origen (necesidad);
- El multiplicador es la producción total que genera una um de demanda final de una etapa. Aguas arriba son las etapas proveedoras;

💡 **Cómo se explica en la clase [B124-C01](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md):**
- El Handbook on Measuring the Space Economy de la OCDE (2.ª ed., 2022) es la referencia habitual para definir los segmentos aguas arriba y aguas abajo, pero no se consultó: solo apareció en una búsqueda el 2026-11-11 y por eso la clase no cita ninguna de sus definiciones ni cifras.
- 🎯 **Por qué importa:** El bloque necesita un mapa común antes de hablar de costos, financiamiento o contratos: ¿quién le compra a quién y dónde queda el valor? Ninguna clase anterior del programa trata la estructura económica de la industria espacial.

📘 **Dónde se aprende** (2 clases): [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md); [B124-C01 · Cadena de valor de industria espacial](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md).

### Aguas grises

- Aguas grises: agua de higiene sin orina.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- G["aguas grises F, S0"] --> B["biorreactor tau"]
- *Descripción textual:* las aguas grises pasan por un biorreactor que baja la carga orgánica, por filtros y por una desinfección antes de entrar al lazo de agua.
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?

📘 **Dónde se aprende** (1 clase): [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### Agujero negro

- Un agujero negro es un remanente sin soporte posible.

💡 **Cómo se explica en la clase [B24-C18](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md):**
- B -- "> M_Ch" --> D["Colapso: estrella de<br/>neutrones o agujero negro"]
- *Descripción textual:* según la masa del núcleo al fin de la fusión, queda una enana blanca (por debajo de la masa de Chandrasekhar) o se produce un colapso a una estrella de neutrones o un agujero negro, con una liberación de energía de una fracción apreciable de `Mc²`.
- 🎯 **Por qué importa:** El destino de una estrella es una enana blanca, una estrella de neutrones o un agujero negro; hay una masa límite que separa los dos primeros destinos. Calcularla muestra cómo la mecánica cuántica (presión de degeneración) sostiene a una estrella cuando ya no hay fusión.

📖 **Explicado a fondo:** [Agujero negro](esencial/ampliacion-a-m.md#agujero-negro) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md).

### AHP

- Un estudio de compromiso (*trade study*) compara candidatas con criterios. AHP convierte comparaciones por pares (escala 1–9) en pesos.

🎯 **Por qué importa (clase B83-C07):** Elegir una arquitectura «porque sí» es una decisión sin rastro. La decisión central: ¿qué arquitectura conviene, con qué criterios y qué tan firme es la elección?

📘 **Dónde se aprende** (1 clase): [B83-C07 · Arquitecturas de sistemas](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md).

### Aislamiento

- El aislamiento elige el sensor cuya columna de `P` está más alineada con `r`.
- Desensibilización: pérdida de sensibilidad por interferencia. Aislamiento: atenuación entre fuente y víctima.

💡 **Cómo se explica en la clase [B80-C05](../programa/clases/B80/B80-C05-redundancia-de-sensores-y-arbitraje-de-mediciones/CLASE.md):**
- Descripción larga: el sistema casi no ve fallas de `2 σ`, ve la mitad de las de `5 σ` y todas las de `10 σ`; el aislamiento correcto es casi perfecto cuando la falla se detecta.
- 🎯 **Por qué importa:** B88-C12 trata la detección y recuperación de fallas en general, no el arbitraje de las mediciones que alimentan la navegación. La decisión central: ¿cómo sabe el sistema que un sensor miente, y cuál es, sin una referencia externa?

📘 **Dónde se aprende** (2 clases): [B80-C05 · Redundancia de sensores y arbitraje de mediciones](../programa/clases/B80/B80-C05-redundancia-de-sensores-y-arbitraje-de-mediciones/CLASE.md); [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md).

### Aislamiento de polarización cruzada

- El aislamiento de polarización cruzada es la atenuación entre dos polarizaciones ortogonales.

🎯 **Por qué importa (clase B91-C02):** Un enlace pierde potencia si las polarizaciones no coinciden, y puede perderla toda si son ortogonales. La decisión central: ¿qué polarización y qué razón axial exigir a las dos antenas para que la desadaptación quede por debajo del margen del enlace?

📘 **Dónde se aprende** (1 clase): [B91-C02 · Polarización de antenas y pérdidas por desadaptación](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md).

### Aislamiento multicapa

- El aislamiento multicapa son láminas reflectantes que reducen la radiación.

🎯 **Por qué importa (clase B47-C13):** Cada vatio parásito acorta la vida de un criógeno. La decisión central: ¿cuántos escudos y qué soportes bastan para una vida útil dada?

📘 **Dónde se aprende** (2 clases): [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md); [B49-C07 · Criogenia y refrigeración de receptores de radio](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md).

### Ajuste

- El ajuste es el procedimiento que elige los parámetros que dejan menores residuos.
- Un ajuste es la curva que mejor representa los datos según un criterio.
- El ajuste de `AVAR` es lineal en `N²` y `K²`.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- Con 8 planetas (S3), el ajuste da `p = 1,4978` y `k = 0,9998`, es decir, `T = 0,9998·a^1,4978`.
- El ajuste mejora apenas, a costa de un parámetro más: no hay motivo para preferirlo.
- ⚠️ **Error frecuente:** Exigir un ajuste perfecto. Ejercicio 11.
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?

📘 **Dónde se aprende** (7 clases): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md); [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md); [B85-C14 · Degradación ultravioleta](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md); [B87-C04 · Sensores terrestres](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md); [B87-C06 · Giroscopios MEMS](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md) y 1 más.

### Ajuste algebraico (Kåsa)

- El ajuste algebraico (Kåsa) resuelve `x² + y² = 2ax + 2by + c`.

🎯 **Por qué importa (clase B84-C18):** Una pieza «dentro de tolerancia» con una medida que tiene 5 µm de incertidumbre en una tolerancia de 10 µm no está demostrada. La decisión central: ¿qué diámetro tiene el agujero, con qué incertidumbre y cuántos puntos hacen falta?

📘 **Dónde se aprende** (1 clase): [B84-C18 · Control dimensional](../programa/clases/B84/B84-C18-control-dimensional/CLASE.md).

### Ajuste circular

- El ajuste circular usa una sola sinusoide.

💡 **Cómo se explica en la clase [B29-C03](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md):**
- Descripción larga: el ajuste circular pierde las armónicas superiores de la órbita excéntrica y reduce la amplitud recuperada.
- 🎯 **Por qué importa:** La velocidad radial da la masa mínima del planeta, que el tránsito no da. Combinados, dan la densidad.

📘 **Dónde se aprende** (1 clase): [B29-C03 · Velocidad radial estelar](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md).

### Ajuste cuadrático

- El ajuste cuadrático estima el mínimo con sub-muestreo.

🎯 **Por qué importa (clase B53-C17):** La misma banda se mide distinto según cómo se defina el continuo y el ruido. La decisión central: ¿con qué incertidumbre se conocen el centro y la profundidad de una banda y qué sesgo introduce el método?

📘 **Dónde se aprende** (1 clase): [B53-C17 · Mineralogía espectral](../programa/clases/B53/B53-C17-mineralogia-espectral/CLASE.md).

### Ajuste de cajas

- El ajuste de cajas (BLS) busca una caída rectangular periódica.

💡 **Cómo se explica en la clase [B29-C20](../programa/clases/B29/B29-C20-proyecto-de-deteccion-exoplanetaria/CLASE.md):**
- Kovács, Zucker y Mazeh estudian las características estadísticas de un algoritmo de ajuste de cajas para buscar tránsitos periódicos y muestran que el parámetro crucial es la relación señal-ruido efectiva (S2, resumen).
- 🎯 **Por qué importa:** Una detección sin completitud no se puede contar: ¿cuántos planetas se perdieron? La inyección y recuperación responde.

📘 **Dónde se aprende** (1 clase): [B29-C20 · Proyecto de detección exoplanetaria](../programa/clases/B29/B29-C20-proyecto-de-deteccion-exoplanetaria/CLASE.md).

### Ajuste de cuerpo rígido

- Correspondencia: par de observaciones del mismo punto en dos instantes. Ajuste de cuerpo rígido: transformación `(R, t)` que mejor lleva un conjunto al otro.

🎯 **Por qué importa (clase B99-C01):** Una trayectoria se obtiene sumando movimientos pequeños, y cada uno trae un error; esos errores no se corrigen solos. La decisión central: ¿con qué calidad de correspondencias y de medida puedo confiar en la odometría, y cuándo necesito corregirla con cierres de bucle (C04)?

📘 **Dónde se aprende** (1 clase): [B99-C01 · Odometría visual](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md).

### Ajuste de Kåsa

- El ajuste de Kåsa es un ajuste circular de mínimos cuadrados lineal.

🎯 **Por qué importa (clase B74-C25):** En un disco iluminado a medias, el borde oscuro no existe y un ajuste ingenuo se sesga. La decisión central: ¿qué parte del limbo es utilizable, con qué incertidumbre, y qué sesgo introduce la fase?

📘 **Dónde se aprende** (1 clase): [B74-C25 · Detección de limbo y bordes planetarios en imágenes de navegación](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md).

### Ajuste de modos

- El ajuste de modos quita `1, x, y, r²`.

💡 **Cómo se explica en la clase [B43-C22](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md):**
- *Descripción textual:* cuatro imágenes dan la fase envuelta; el desenvolvimiento la completa y el ajuste de modos deja el error de forma.
- 🎯 **Por qué importa:** El mapa de error de forma es la prueba de aceptación de un espejo. La decisión central: ¿cómo se recupera la fase, qué se descuenta y qué PV y RMS quedan?

📘 **Dónde se aprende** (1 clase): [B43-C22 · Interferometría de superficie y mapas de error de forma](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md).

### Ajuste de PSF

- El ajuste de PSF modela cada estrella como flujo × PSF.

💡 **Cómo se explica en la clase [B45-C24](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md):**
- Dos estrellas (3000 y 1000 e⁻) separadas 3 píxeles con PSF de `σ = 2` se miden con apertura sesgada `+664 e⁻`, mientras que el ajuste de PSF da `2997,8` y `999,8 e⁻` (errores `94,0` y `84,2`).
- 🎯 **Por qué importa:** La apertura sesga los flujos de estrellas próximas y el ajuste de PSF los separa. La decisión central: ¿qué sesgo evita el ajuste y con qué incertidumbre y correlación?

📘 **Dónde se aprende** (1 clase): [B45-C24 · Fotometría por ajuste de PSF](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md).

### Ajuste dióptrico

- La distancia interpupilar es la separación de tus ojos que debes igualar con las bisagras; el ajuste dióptrico corrige la diferencia entre tus dos ojos.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- Enfoca con el ojo izquierdo cerrado sobre un objeto lejano, usando la rueda central; luego con el derecho cerrado, corrige con el ajuste dióptrico.
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?

📘 **Dónde se aprende** (1 clase): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md).

### Ajuste directo

- El ajuste log-log linealiza con logaritmos; el ajuste directo minimiza `Σ(ΔV − a D^b)²`.

🎯 **Por qué importa (clase B85-C23):** Un monitor mal calibrado no distingue una dosis real del ruido. La decisión central: ¿cuál es la relación señal–dosis, desde qué dosis es fiable y hasta qué tasa de cuentas se puede corregir el tiempo muerto?

📘 **Dónde se aprende** (1 clase): [B85-C23 · Dosímetros y monitores de radiación a bordo](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md).

### Ajuste kepleriano

- El ajuste kepleriano modela la curva completa.

💡 **Cómo se explica en la clase [B29-C09](../programa/clases/B29/B29-C09-parametros-orbitales-exoplanetarios/CLASE.md):**
- A diferencia del ajuste circular de B29-C03 (que perdía el 8 % a `e = 0,3`), el ajuste kepleriano recupera `K`, `e` y `ω` sin sesgo apreciable.
- 🎯 **Por qué importa:** La excentricidad y el argumento del periastro cambian la forma de la curva y el sesgo de `K` que vimos en C03. Y la densidad de la estrella que sale del tránsito ayuda a validar al anfitrión.

📘 **Dónde se aprende** (1 clase): [B29-C09 · Parámetros orbitales exoplanetarios](../programa/clases/B29/B29-C09-parametros-orbitales-exoplanetarios/CLASE.md).

### Ajuste lineal

- El ajuste lineal estima la tasa como pendiente de la media frente a la exposición.
- El ajuste lineal estima `a` y `b`.

💡 **Cómo se explica en la clase [B44-C07](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md):**
- Un ajuste lineal recupera `0,93751 e⁻/s` frente a `0,93685` verdadero.
- 🎯 **Por qué importa:** La oscuridad añade señal y ruido; saber cómo escala permite elegir temperatura y exposición. La decisión central: ¿cuánto hay que enfriar para que la corriente oscura deje de importar?

📘 **Dónde se aprende** (2 clases): [B44-C07 · Corriente oscura](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md); [B102-C06 · Dinamometría y medición de fuerzas de tracción](../programa/clases/B102/B102-C06-dinamometria-y-medicion-de-fuerzas-de-traccion/CLASE.md).

### Ajuste log-log

- El ajuste log-log linealiza con logaritmos; el ajuste directo minimiza `Σ(ΔV − a D^b)²`.

💡 **Cómo se explica en la clase [B85-C23](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md):**
- El ajuste log-log da `a = 0,01214`, `b = 0,8472`; el directo, `a = 0,01201`, `b = 0,8500`.
- 🎯 **Por qué importa:** Un monitor mal calibrado no distingue una dosis real del ruido. La decisión central: ¿cuál es la relación señal–dosis, desde qué dosis es fiable y hasta qué tasa de cuentas se puede corregir el tiempo muerto?

📘 **Dónde se aprende** (1 clase): [B85-C23 · Dosímetros y monitores de radiación a bordo](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md).

### Ajuste polinomico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B32-C10):** Un continuo mal puesto sesga los anchos equivalentes. La decisión central: ¿cómo estimar el continuo ignorando las líneas?

📘 **Dónde se aprende** (1 clase): [B32-C10 · Normalización y modelado del continuo espectral](../programa/clases/B32/B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md).

### Ajuste por cruces

- El ajuste por cruces estima correcciones que minimizan las discrepancias.

🎯 **Por qué importa (clase B53-C07):** Las pasadas se cruzan y deben coincidir en ese punto. La decisión central: ¿cuánto del desacuerdo en los cruces es error de órbita que se puede estimar y corregir, y cuánto queda como ruido?

📘 **Dónde se aprende** (1 clase): [B53-C07 · Topografía por altimetría](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md).

### Ajuste por mínimos cuadrados

- Un ajuste por mínimos cuadrados busca la recta que minimiza la suma de los cuadrados de las distancias verticales entre los puntos y la recta.
- El ajuste por mínimos cuadrados busca los parámetros que minimizan la suma de residuos al cuadrado ponderados.

💡 **Cómo se explica en la clase [B03-C16](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md):**
- Ajuste por mínimos cuadrados usa todos, pero es sensible a valores extremos y supone errores solo en `y`.
- 🎯 **Por qué importa:** Si sitúas en un gráfico logarítmico el período frente al semieje de los planetas, los puntos forman una recta. Su pendiente es 1,5: ese número es el exponente de la tercera ley de Kepler.

📘 **Dónde se aprende** (2 clases): [B03-C16 · Pendiente e interpretación de gráficos](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md); [B14-C20 · Proyecto reproducible de análisis astronómico](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md).

### ALA

- Un ala es un conjunto de paneles unidos por bisagras.
- Los esquemas de datos se nombran LAL (lado–ángulo–lado), LLL (tres lados), ALA (ángulo–lado–ángulo) y LLA (lado–lado–ángulo no incluido).

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- B -->|"ALA"| D["Tercer ángulo = 180° − A − B; luego ley de senos"]
- *Descripción textual:* según los datos (LAL o LLL, ALA o LLA) se usa la ley de cosenos, el tercer ángulo y la de senos, o la de senos con posible ambigüedad; todo termina comprobando que los ángulos suman 180°.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

📘 **Dónde se aprende** (2 clases): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md); [B86-C03 · Arreglos fotovoltaicos desplegables](../programa/clases/B86/B86-C03-arreglos-fotovoltaicos-desplegables/CLASE.md).

### Ala fija

- La ala fija no se mueve respecto del cuerpo;

💡 **Cómo se explica en la clase [B86-C04](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md):**
- Con dos ejes el coseno medio es `1 − f`; con un eje es `(1 − f) cosβ`; con el ala fija al cenit es mucho menor (`≈ cosβ/π` antes de restar el eclipse).
- 🎯 **Por qué importa:** El eclipse más largo fija el tamaño de la batería y el peor `β` fija el de la ala. Un diseño que mire solo `β = 0` ignora que a `β` alto no hay eclipse pero el coseno cae.

📘 **Dónde se aprende** (1 clase): [B86-C04 · Orientación solar y eclipses](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md).

### Alabeo

- La guiñada (*yaw*) gira alrededor de `z`, el cabeceo (*pitch*) alrededor de `y`, el alabeo (*roll*) alrededor de `x`.

💡 **Cómo se explica en la clase [B10-C14](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md):**
- *Descripción textual:* con el cabeceo lejos de `±90°`, cada orientación tiene un único trío de ángulos que varía suavemente; cuando el cabeceo se acerca a `±90°`, el alabeo y la guiñada se mezclan, varias parejas dan la misma matriz y las tasas de cambio crecen sin límite.
- Un satélite (escenario sintético) describe su actitud con la secuencia 3‑2‑1: guiñada `ψ` alrededor de `z`, cabeceo `θ` alrededor de `y` y alabeo `φ` alrededor de `x`, con `R = R_z(ψ) R_y(θ) R_x(φ)` (activa, cuerpo → inercial).
- 🎯 **Por qué importa:** Un satélite que apunta una antena al cenit tiene el cabeceo cerca de `90°`; si la actitud se guarda con ángulos de Euler, justo ahí el cálculo se vuelve inestable: ángulos que cambian muy rápido para movimientos pequeños, o dos conjuntos de ángulos distintos para la misma orientación.

📘 **Dónde se aprende** (1 clase): [B10-C14 · Ángulos de Euler y singularidades](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md).

### ALARA

- Un límite administrativo es un valor más estricto que se usa para cumplir el estándar. ALARA es el principio de mantener la exposición tan baja como sea razonablemente alcanzable.

🎯 **Por qué importa (clase B112-C06):** Falta la clase de estimación de riesgo por misión. Es la que usa un planificador: suma dosis de cada tramo, la convierte en riesgo y decide si cabe dentro de un límite.

📘 **Dónde se aprende** (1 clase): [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Alarma dependiente

- Una alarma dependiente se deriva de una causa raíz ya activa; la supresión la oculta para no saturar.

🎯 **Por qué importa (clase B98-C04):** Un operador que decide con un dato viejo sin saberlo comete errores; uno que recibe 24 alarmas por 3 fallos no ve la causa. La decisión central: ¿qué debe mostrar la interfaz para que el operador sepa qué tan viejo es lo que ve y qué es lo importante?

📘 **Dónde se aprende** (1 clase): [B98-C04 · Interfaces humano-robot para operación remota](../programa/clases/B98/B98-C04-interfaces-humano-robot-para-operacion-remota/CLASE.md).

### Alas

- El núcleo y las alas.

💡 **Cómo se explica en la clase [B32-C04](../programa/clases/B32/B32-C04-opacidad-de-lineas-ensanchamiento-y-perfil-de-voigt/CLASE.md):**
- En `v = 3` el perfil con `a = 0,1` es 65 veces mayor que el gaussiano: las alas dominan lejos del centro.
- El núcleo es una campana que cae rápido y las alas son una cola que cae como una potencia: lejos del centro solo queda la cola.
- ⚠️ **Error frecuente:** Despreciar las alas. Se corrige con 8.3.
- 🎯 **Por qué importa:** Las alas de la línea dan la presión y las abundancias. La decisión central: ¿cuándo domina el núcleo gaussiano y cuándo las alas?

📘 **Dónde se aprende** (1 clase): [B32-C04 · Opacidad de líneas: ensanchamiento y perfil de Voigt](../programa/clases/B32/B32-C04-opacidad-de-lineas-ensanchamiento-y-perfil-de-voigt/CLASE.md).

### Albedo

- El albedo `p` es la fracción de luz reflejada.
- El albedo `a` es la fracción de luz solar que la Tierra refleja.
- El albedo `p` es la reflectividad.

💡 **Cómo se explica en la clase [B29-C13](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md):**
- Con albedo uniforme en `[0,1; 0,6]`: `T_eq` media `248,70 K`, desviación Monte Carlo `14,209 K` frente a `13,874 K` lineal (cociente `1,0242`).
- *Descripción textual:* la estrella fija el flujo y la temperatura de equilibrio; la fórmula se invierte para hallar la distancia; la incertidumbre del albedo se propaga por simulación y por la derivada; la atmósfera añade un desplazamiento ilustrativo.
- ⚠️ **Error frecuente:** Olvidar el albedo. Se corrige con el ejercicio 3.
- 🎯 **Por qué importa:** La temperatura de equilibrio es la primera estimación de si un mundo es cálido o helado, pero no es la temperatura de la superficie: depende del albedo y del efecto invernadero. La decisión central: ¿a qué distancias una estrella da una temperatura de equilibrio dada y cuánto cambia con el albedo?

📖 **Explicado a fondo:** [Albedo](esencial/esencial-a-c.md#albedo) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B29-C13 · Zonas de habitabilidad](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md); [B58-C01 · Clasificación de cuerpos menores](../programa/clases/B58/B58-C01-clasificacion-de-cuerpos-menores/CLASE.md); [B85-C01 · Balance radiativo de satélite](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md); [B118-C03 · Detección y seguimiento óptico](../programa/clases/B118/B118-C03-deteccion-y-seguimiento-optico/CLASE.md).

### Albedo de Bond

- El albedo de Bond `A` es la fracción de luz reflejada.
- El albedo de Bond es la fracción reflejada de toda la energía incidente.
- El albedo de Bond es la fracción de la luz solar incidente que se refleja.

💡 **Cómo se explica en la clase [B54-C03](../programa/clases/B54/B54-C03-equilibrio-radiativo/CLASE.md):**
- Las fichas NASA dan para cada planeta la irradiancia solar `S`, el albedo de Bond `A` y la temperatura de cuerpo negro (S1–S4); σ viene de NIST (S5).
- 🎯 **Por qué importa:** La temperatura de un planeta no la fija solo lo que recibe sino cuánto absorbe y cómo se deshace de la energía. La pregunta motivadora: ¿cuánto más caliente es un mundo que su temperatura de equilibrio, y qué dice eso de su atmósfera?

📘 **Dónde se aprende** (3 clases): [B52-C15 · Cinturón de Kuiper](../programa/clases/B52/B52-C15-cinturon-de-kuiper/CLASE.md); [B54-C03 · Equilibrio radiativo](../programa/clases/B54/B54-C03-equilibrio-radiativo/CLASE.md); [B56-C08 · Habitabilidad de Marte](../programa/clases/B56/B56-C08-habitabilidad-de-marte/CLASE.md).

### Albedo de dispersión simple

- El albedo de dispersión simple `ω₀` es la fracción de extinción que es dispersión.

🎯 **Por qué importa (clase B57-C13):** Un satélite que mira un incendio, un volcán o el mar tiene que descontar la atmósfera, y los aerosoles son lo más variable. La decisión central: ¿cuánto aerosol hay y qué tipo, con qué incertidumbre, a partir de pocas longitudes de onda?

📘 **Dónde se aprende** (1 clase): [B57-C13 · Atmósfera y aerosoles](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md).

### Albedo esférico

- El albedo esférico `s` mide el rebote entre superficie y atmósfera.

🎯 **Por qué importa (clase B57-C26):** Comparar imágenes de fechas distintas con atmósferas distintas confunde atmósfera con cambio. La decisión central: ¿cuánto sesga la atmósfera y cómo se estima y descuenta con la información disponible?

📘 **Dónde se aprende** (1 clase): [B57-C26 · Corrección atmosférica de imágenes](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md).

### Alcalófilo

- Un acidófilo crece a pH bajo y un alcalófilo a pH alto.

💡 **Cómo se explica en la clase [B64-C05](../programa/clases/B64/B64-C05-acidofilos-y-alcalofilos/CLASE.md):**
- En el alcalófilo el pH interno es menor que el externo y el término de pH se suma con signo opuesto: la fuerza protonmotriz del ejemplo es pequeña y de signo positivo; cómo producen ATP estos organismos es una cuestión que no se trata aquí (no consultado).
- Por contraste: neutrófilo frente a acidófilo y alcalófilo.
- 🎯 **Por qué importa:** Un acidófilo vive en un medio miles de veces más ácido que su citoplasma. La pregunta motivadora: ¿cómo mantiene una célula un interior casi neutro y qué le cuesta?

📘 **Dónde se aprende** (1 clase): [B64-C05 · Acidófilos y alcalófilos](../programa/clases/B64/B64-C05-acidofilos-y-alcalofilos/CLASE.md).

### Alcance

- El alcance es hasta dónde pretende llegar la respuesta.
- El alcance (*scope*) es la región donde un nombre existe: una variable creada dentro de la función es local.
- El alcance (o distancia de horizonte) es hasta donde se supera el umbral.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C07](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md):**
- Duplicar el alcance multiplica los eventos por 8.
- El detector tiene una red cuyo radio es el alcance.
- ⚠️ **Error frecuente:** Olvidar el cubo del alcance. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** La tasa de eventos detectados depende del volumen que el detector ve, que crece como el cubo del alcance. Una mejora pequeña en sensibilidad se traduce en muchos más eventos.

📘 **Dónde se aprende** (13 clases): [B01-C06 · Preguntas investigables en astronomía](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md); [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md); [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md); [B31-C09 · Interacciones fundamentales](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md); [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md); [B53-C07 · Topografía por altimetría](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md) y 7 más.

### Alcance CSDA

- Alcance CSDA: distancia media recorrida frenándose de forma continua.

🎯 **Por qué importa (clase B47-C09):** Medir ΔE y E permite identificar la partícula. La decisión central: ¿qué espesor de detector y qué energía separan protones de partículas alfa?

📘 **Dónde se aprende** (2 clases): [B47-C09 · Detectores de partículas — Instrumentación y observatorios espaciales](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md); [B106-C14 · Protección contra radiación](../programa/clases/B106/B106-C14-proteccion-contra-radiacion/CLASE.md).

### Alcance máximo

- El alcance máximo es la distancia en la que la SNR cae al mínimo.

🎯 **Por qué importa (clase B118-C04):** Para los desechos pequeños en LEO el radar es el sensor más usado, pero su alcance cae rápido con el tamaño. La decisión central: ¿hasta qué distancia ve un radar un objeto de un tamaño dado, y cuánto pierde cuando el objeto se aleja?

📘 **Dónde se aprende** (1 clase): [B118-C04 · Detección por radar](../programa/clases/B118/B118-C04-deteccion-por-radar/CLASE.md).

### Alcance mínimo

- El alcance mínimo pide declarar los datos en el ámbito más pequeño.

🎯 **Por qué importa (clase B88-C36):** Un desbordamiento silencioso convierte 35 000 en −30 536 y un comando de giro positivo en negativo. La decisión central: ¿qué operaciones aceptan cualquier entrada y devuelven siempre un resultado dentro del rango?

📘 **Dónde se aprende** (1 clase): [B88-C36 · Codificación defensiva y estándares de código seguro](../programa/clases/B88/B88-C36-codificacion-defensiva-y-estandares-de-codigo-seguro/CLASE.md).

### Alcance oblicuo

- La dirección de azimut es la de vuelo; el alcance oblicuo `R` es la distancia al blanco.

🎯 **Por qué importa (clase B69-C01):** Sin el principio Doppler, la resolución en azimut de un radar quedaría fijada por el ancho del haz de la antena: a 850 km, una antena de 12 m (λ = 0,0555 m) iluminaría una franja de unos 3,9 km. La decisión central: ¿qué resolución obtiene el sistema, de qué depende y qué hay que muestrear para no perderla?

📘 **Dónde se aprende** (1 clase): [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md).

### Alcance transitivo

- El alcance transitivo de Y es todo lo que depende de él directa o indirectamente.

💡 **Cómo se explica en la clase [B119-C16](../programa/clases/B119/B119-C16-proteccion-de-infraestructura-critica/CLASE.md):**
- Cada nodo tiene un alcance transitivo (BFS y Warshall coinciden).
- 🎯 **Por qué importa:** C14 y C15 modelan amenazas sobre un enlace; esta clase muestra cómo una falla local se propaga, que ninguna clase anterior trata y que B122 desarrolla con proveedores y modelos defensivos. La decisión central: ¿qué nodos conviene proteger primero, dado cómo se propagan las fallas?

📘 **Dónde se aprende** (1 clase): [B119-C16 · Protección de infraestructura crítica](../programa/clases/B119/B119-C16-proteccion-de-infraestructura-critica/CLASE.md).

### Alcano

- Un hidrocarburo contiene sólo carbono e hidrógeno: alcano (enlaces simples, `CₙH₂ₙ₊₂`, como el metano `CH₄`), alqueno (un doble enlace, `CₙH₂ₙ`, como el eteno `C₂H₄`), alquino (un triple enlace) y aromático (anillos con enlaces alternados, como el benceno `C₆H₆`).

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- H --> A1["Alcano: CnH2n+2, insaturación 0"]
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Alcanzabilidad

- Transición: cambio permitido. Alcanzabilidad: estados a los que se llega desde otro.

🎯 **Por qué importa (clase B96-C08):** Un comando válido en un estado puede ser peligroso en otro; y un modo seguro al que no se puede volver es una trampa. La decisión central: ¿qué transiciones existen y se puede siempre llegar al estado seguro?

📘 **Dónde se aprende** (1 clase): [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md).

### Alcohol

- Un grupo funcional es una agrupación de átomos que da propiedades características: alcohol (–OH, como el etanol `C₂H₆O`), aldehído (–CHO, como el formaldehído `CH₂O`), ácido carboxílico (–COOH, como el fórmico `CH₂O₂` y el acético `C₂H₄O₂`) y amina (–NH₂, como la metilamina `CH₅N`).

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- La segunda son los grupos funcionales con oxígeno y nitrógeno: alcohol, aldehído, ácido carboxílico y amina.
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Aldehído

- Un grupo funcional es una agrupación de átomos que da propiedades características: alcohol (–OH, como el etanol `C₂H₆O`), aldehído (–CHO, como el formaldehído `CH₂O`), ácido carboxílico (–COOH, como el fórmico `CH₂O₂` y el acético `C₂H₄O₂`) y amina (–NH₂, como la metilamina `CH₅N`).

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- El aldehído (–CHO) más sencillo es el formaldehído, `CH₂O`.
- La segunda son los grupos funcionales con oxígeno y nitrógeno: alcohol, aldehído, ácido carboxílico y amina.
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Aleatoria

- La incertidumbre sistemática afecta a todos los datos del mismo método por igual; la aleatoria varía de un dato a otro.

🎯 **Por qué importa (clase B01-C15):** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Alerta

- Una alerta es el mensaje a la comunidad.
- Métrica: serie numérica. Alerta: aviso por regla.
- La alerta se modela como `C − S + 0,5`.

💡 **Cómo se explica en la clase [B28-C09](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md):**
- Paso 4 · Sentido. Se alerta solo con SNR mayor que `6,05`.
- 🎯 **Por qué importa:** Una alerta tardía pierde el evento; una alerta con muchas falsas alarmas agota a los observadores. La decisión central: ¿qué umbral produce una tasa de falsas alarmas aceptable y cuánto tarda la alerta en llegar?

📘 **Dónde se aprende** (3 clases): [B28-C09 · Alertas científicas en tiempo real](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md); [B48-C23 · Observabilidad del software de observatorio: registros, métricas y alertas](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md); [B104-C17 · Gestión de fatiga](../programa/clases/B104/B104-C17-gestion-de-fatiga/CLASE.md).

### Alerta temprana

- La alerta temprana es el primer aviso breve.

💡 **Cómo se explica en la clase [B122-C08](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md):**
- Alerta temprana: `+24 h = 2026-03-06 22:30`.
- K["conocimiento t0"] --> A["alerta temprana: t0 + 24 h"]
- 🎯 **Por qué importa:** B124-C18 trata divulgación; la comunicación de crisis con mensajes oportunos no está cubierta. La decisión central: ¿qué hay que comunicar, a quién y antes de qué plazo?

📘 **Dónde se aprende** (1 clase): [B122-C08 · Comunicación de crisis con operadores, autoridades y público](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md).

### Aleta

- La aleta es una superficie extendida que disipa calor al ambiente; su eficiencia `η = tanh(mL)/(mL)` compara el flujo real con el ideal.

💡 **Cómo se explica en la clase [B85-C02](../programa/clases/B85/B85-C02-conduccion-termica-en-estructuras/CLASE.md):**
- Descripción larga: la unión añade una resistencia comparable a la de la barra y recorta el flujo en un tercio; la aleta corta es casi ideal.
- 🎯 **Por qué importa:** El calor generado por un equipo debe llegar al radiador por algún camino; una unión mal conductora puede ser la resistencia dominante. La decisión central: ¿qué parte del camino de conducción limita el flujo y qué cambio lo mejora más?

📘 **Dónde se aprende** (1 clase): [B85-C02 · Conducción térmica en estructuras](../programa/clases/B85/B85-C02-conduccion-termica-en-estructuras/CLASE.md).

### Aleta radiante

- Una aleta radiante extiende el radiador con una lámina conductora; su eficiencia `η = tanh(mL)/(mL)` (lineal, con `m² = 2h_r/(k e)`) mide cuánto de la lámina trabaja.

🎯 **Por qué importa (clase B85-C07):** El área del radiador manda en masa, volumen y costo. La decisión central: ¿cuánta área necesita un radiador en el caso caliente de fin de vida y qué la reduce?

📘 **Dónde se aprende** (1 clase): [B85-C07 · Radiadores espaciales](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md).

### Alfa de Cronbach

- El alfa de Cronbach mide la consistencia interna: `α = k/(k − 1)(1 − Σσ²_j/σ²_total)`.
- KR-20 y el alfa de Cronbach miden la consistencia interna; para ítems dicotómicos coinciden.

💡 **Cómo se explica en la clase [B105-C27](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md):**
- D["respuestas 10 items<br/>n personas"] --> A["alfa de Cronbach"]
- 🎯 **Por qué importa:** Un cuestionario con ítems que no miden lo mismo produce una puntuación poco fiable, y con pocos participantes su fiabilidad ni siquiera se puede estimar. La decisión central: ¿qué ítems sobran, cuántos ítems hacen falta y cuántos participantes se necesitan para estimar el alfa con una incertidumbre aceptable?

📘 **Dónde se aprende** (2 clases): [B105-C27 · Instrumentos validados y psicometría en investigación](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md); [B130-C05 · Evaluación de la comprensión del público](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md).

### Algoritmo

- Un algoritmo es una secuencia finita de pasos precisos que, a partir de unas entradas, produce unas salidas y termina (la definición de uso en informática; el Tutorial de Python lo ilustra con ejemplos como la serie de Fibonacci, S2).

💡 **Cómo se explica en la clase [B07-C01](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md):**
- Elegir bien el punto de partida es parte del algoritmo.
- Con eso, el algoritmo se lee casi igual que el pseudocódigo:
- ⚠️ **Error frecuente:** Suponer que el algoritmo valida los datos. Se corrige con el ejercicio 11 y la sección 13.
- 🎯 **Por qué importa:** En astronomía casi todo resultado pasa por un procedimiento repetible: reducir imágenes, ajustar una órbita, buscar el máximo de una curva de luz. Si no puedes describir el procedimiento con precisión, no puedes ejecutarlo en un computador ni dárselo a otra persona para que lo repita.

📘 **Dónde se aprende** (1 clase): [B07-C01 · Pensamiento algorítmico](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md).

### Algoritmo de Goertzel

- El algoritmo de Goertzel mide una sola frecuencia.

🎯 **Por qué importa (clase B46-C07):** La mezcla es lo que permite procesar en una banda cómoda, pero trae consigo una segunda frecuencia que cae en la misma FI. La decisión central: ¿qué rechazo de imagen exige el receptor y cómo se logra?

📘 **Dónde se aprende** (1 clase): [B46-C07 · Receptores superheterodinos](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md).

### Algoritmo de Lloyd

- El algoritmo de Lloyd alterna dos pasos: asignar cada punto al centroide más cercano y recalcular cada centroide como media de sus puntos; scipy implementa esa idea con distintas inicializaciones, entre ellas `'++'` (k-means++, siembra cuidadosa) y `'matrix'` (centroides dados) (S1).

🎯 **Por qué importa (clase B15-C23):** Un satélite fotografía una región que nadie ha cartografiado. Sin muestras, no se puede entrenar un clasificador, pero sí se puede preguntar cuántos «tipos» de superficie distintos hay en las bandas.

📘 **Dónde se aprende** (1 clase): [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md).

### Algoritmo de Metropolis

- El algoritmo de Metropolis propone `y` desde una distribución simétrica alrededor del actual `x` y lo acepta con probabilidad `min(1, π(y)/π(x))`; si no, repite `x`.

🎯 **Por qué importa (clase B12-C13):** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.

📘 **Dónde se aprende** (1 clase): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md).

### Algoritmo de Thomas

- Un sistema tridiagonal solo tiene tres diagonales distintas de cero y se resuelve con el algoritmo de Thomas (eliminación sin pivoteo, `O(N)`).

🎯 **Por qué importa (clase B11-C12):** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Algoritmo de Viterbi

- El algoritmo de Viterbi halla la secuencia de máxima verosimilitud; en decisión dura usa la distancia de Hamming.

🎯 **Por qué importa (clase B94-C02):** El decodificador de Viterbi falla en ráfagas y los desvanecimientos también. La decisión central: ¿qué profundidad de entrelazado hace falta para que una ráfaga de `B` octetos no sature ninguna palabra, y qué ganancia da frente a no entrelazar?

📘 **Dónde se aprende** (1 clase): [B94-C02 · Entrelazado y concatenación de códigos](../programa/clases/B94/B94-C02-entrelazado-y-concatenacion-de-codigos/CLASE.md).

### Algoritmo genético

- El algoritmo genético evoluciona una población por selección (torneo), cruce (promedio ponderado), mutación (ruido gaussiano) y elitismo.

🎯 **Por qué importa (clase B81-C13):** Un método heurístico no garantiza el óptimo, pero puede evitar los mínimos locales. La decisión central: ¿qué método global elegir y cuántas evaluaciones se gastan para una tasa de éxito dada?

📘 **Dónde se aprende** (1 clase): [B81-C13 · Optimización heurística (algoritmos genéticos y enjambres)](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md).

### Algoritmo voraz

- El algoritmo voraz escoge en cada paso el campo con más probabilidad no cubierta.

💡 **Cómo se explica en la clase [B28-C15](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md):**
- MAP["mapa de probabilidad (4000 celdas)"] --> V["algoritmo voraz"]
- *Descripción textual:* el mapa alimenta un algoritmo voraz que da la cobertura en función de los campos; el tiempo por campo da la profundidad; el producto de cobertura y detectabilidad se maximiza.
- 🎯 **Por qué importa:** Observar más campos cubre más probabilidad, pero cada campo recibe menos tiempo y es menos profundo. Si la fuente es débil, el exceso de campos hace que no se vea.

📘 **Dónde se aprende** (1 clase): [B28-C15 · Búsqueda de contrapartidas ópticas](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md).

### Alianza

- Una alianza es una cooperación estable entre empresas.

💡 **Cómo se explica en la clase [B125-C04](../programa/clases/B125/B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md):**
- El artículo VI del Tratado del Espacio Ultraterrestre —por un resumen de búsqueda, texto no leído— hace responsable al Estado de las actividades nacionales, también las privadas, que requieren autorización y supervisión continua; por eso una alianza internacional de empresas siempre involucra a los Estados de cada socio.
- 🎯 **Por qué importa:** Las empresas espaciales dependen de alianzas con socios de otros países y la clase de gobierno no explica cómo se reparte el valor ni cuánta dependencia se acepta; no está tratado. La decisión central: ¿cómo se reparte de forma justa el excedente de una alianza y cuánta dependencia de un solo socio o país es prudente?

📘 **Dónde se aprende** (1 clase): [B125-C04 · Alianzas y cooperación internacional empresarial](../programa/clases/B125/B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md).

### Alias

- El alias es el pico espurio a `f₀ ± 1/Δ`.
- Un alias es una frecuencia por encima de Nyquist que aparece reflejada.
- El alias es un pico falso por el muestreo.

💡 **Cómo se explica en la clase [B29-C19](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md):**
- El pico principal está en `0,366` (verdadero `0,37`) y los alias en `1,368` (`f₀ + 1`) y `0,636` (`1 − f₀`) tienen potencias del 90 % y 65 % de la del principal.
- Con una luz que parpadea una vez al día, una rueda que gira a 1,37 vueltas por día parece girar a 0,37: los alias son lo que el muestreo no distingue.
- ⚠️ **Error frecuente:** Tomar un alias por una señal. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Un periodograma sin cuidado señala alias en lugar del periodo verdadero, y una potencia alta puede ser una fluctuación del ruido. La decisión central: ¿qué picos son del periodo verdadero, cuáles son alias y qué potencia es significativa?

📘 **Dónde se aprende** (3 clases): [B29-C19 · Análisis de series temporales irregularmente muestreadas](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md); [B37-C13 · Series fotométricas de Kepler, TESS y PLATO para asterosismología](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md); [B58-C13 · Caracterización de rotación](../programa/clases/B58/B58-C13-caracterizacion-de-rotacion/CLASE.md).

### Alias de periodo

- El alias de periodo es un múltiplo o submúltiplo del verdadero.

🎯 **Por qué importa (clase B29-C20):** Una detección sin completitud no se puede contar: ¿cuántos planetas se perdieron? La inyección y recuperación responde.

📘 **Dónde se aprende** (1 clase): [B29-C20 · Proyecto de detección exoplanetaria](../programa/clases/B29/B29-C20-proyecto-de-deteccion-exoplanetaria/CLASE.md).

### Aliasing

- El aliasing es el falso aspecto de baja frecuencia que adopta una señal más rápida que Nyquist.
- El aliasing es que una frecuencia mayor que Nyquist (`N/2`) aparece disfrazada de una menor.
- El aliasing (en español, *solapamiento* o *alias*) es el fenómeno por el cual una frecuencia por encima de `f_N` aparece como otra, más baja.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C12](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md):**
- E -- "no" --> G["Aliasing: aparece una frecuencia falsa"]
- *Descripción textual:* una fuente que oscila a frecuencia `f` transmite la perturbación por el medio a velocidad `v`, lo que define `λ = v/f`; el receptor muestrea con `f_s`; si `f` es menor que `f_s/2` la frecuencia se reconstruye bien y si no, aparece una frecuencia falsa (aliasing).
- 🎯 **Por qué importa:** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.

📘 **Dónde se aprende** (5 clases): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md); [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md); [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md); [B90-C23 · Instrumentación y adquisición de datos en ensayos](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md).

### Aliasing perceptual

- Descriptor de lugar: vector que resume lo observado en una pose. Aliasing perceptual: lugares distintos con descriptor parecido.

🎯 **Por qué importa (clase B99-C04):** Aceptar un cierre verdadero reduce el error; aceptar uno falso lo multiplica. La decisión central: ¿con qué umbral y con qué prueba geométrica acepto un cierre de bucle?

📘 **Dónde se aprende** (1 clase): [B99-C04 · Cierre de bucles y consistencia global](../programa/clases/B99/B99-C04-cierre-de-bucles-y-consistencia-global/CLASE.md).

### Alícuota

- Una alícuota es una porción.

🎯 **Por qué importa (clase B63-C03):** Una muestra planetaria es irrepetible y se estudia durante décadas. La decisión central: ¿cómo demuestras, años después, qué le pasó a una muestra y cuánto de lo que mides es suyo?

📘 **Dónde se aprende** (1 clase): [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md).

### Alineación

- La alineación es la correspondencia entre resultado, actividad e ítem.
- La alineación es la correspondencia entre resultados, actividades e ítems.
- RPE: error del movimiento relativo entre pares de poses separados por una ventana (F2). Alineación: hallar el giro y la traslación que mejor superponen ambas trayectorias (SVD).

💡 **Cómo se explica en la clase [B99-C06](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md):**
- Mide la consistencia global y depende de la alineación elegida.
- No necesita alineación y es invariante a una transformación rígida global.
- ⚠️ **Error frecuente:** Olvidar la alineación. Sin alinear, un desplazamiento global se cuenta como error (8.4).
- 🎯 **Por qué importa:** «Mi robot deriva poco» no es una afirmación comprobable. La decisión central: ¿qué métrica, con qué alineación y con qué ventana, describe el error que importa para la tarea?

📘 **Dónde se aprende** (3 clases): [B99-C06 · Evaluación de deriva y error de trayectoria](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md); [B131-C02 · Resultados de aprendizaje observables en astronomía](../programa/clases/B131/B131-C02-resultados-de-aprendizaje-observables-en-astronomia/CLASE.md); [B131-C11 · Plan completo de una clase de astronomía](../programa/clases/B131/B131-C11-plan-completo-de-una-clase-de-astronomia/CLASE.md).

### Alineación polar

- La alineación polar es apuntar el eje de ascensión recta al polo celeste (el polo sur, en Chile).

💡 **Cómo se explica en la clase [B08-C15](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md):**
- La ecuatorial sigue con un solo movimiento y sirve para exposiciones largas, pero pesa más y exige alineación polar.
- 🎯 **Por qué importa:** A 120 aumentos, un planeta cruza el ocular en menos de dos minutos y tienes que empujar el tubo constantemente. La pregunta motivadora: ¿qué montura necesito y qué error puedo tolerar al seguir un objeto?

📘 **Dónde se aprende** (1 clase): [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md).

### Allen–Eggers

- El ángulo de trayectoria `γ` es la inclinación de la entrada. Allen–Eggers es la solución analítica de un reingreso balístico en atmósfera exponencial.

💡 **Cómo se explica en la clase [B104-C19](../programa/clases/B104/B104-C19-operaciones-de-retorno-y-reintegracion/CLASE.md):**
- Con `V = 7,8 km/s` (ilustrativa), altura de escala `H = 7,2 km` y atmósfera exponencial, la fórmula de Allen–Eggers `a_max = V² sin γ/(2 e H)` da 2,77 g con 1°, 4,15 g con 1,5°, 8,29 g con 3° y 22,06 g con 8°.
- 🎯 **Por qué importa:** Un ángulo de entrada más empinado reduce el calentamiento total pero aumenta la desaceleración. La decisión central: ¿cuántos g máximos soporta la tripulación según el ángulo de entrada, y por qué ese máximo no depende de la masa de la nave?

📘 **Dónde se aprende** (1 clase): [B104-C19 · Operaciones de retorno y reintegración](../programa/clases/B104/B104-C19-operaciones-de-retorno-y-reintegracion/CLASE.md).

### Almacenamiento y reenvío

- El Bundle Protocol (BP) crea una red de almacenamiento y reenvío con tolerancia a conectividad intermitente, retransmisión basada en custodia y reportes de estado (CCSDS 734.2-B-1).
- El almacenamiento y reenvío (*store-and-forward*) guarda el paquete hasta el siguiente contacto.

🎯 **Por qué importa (clase B89-C13):** Sin almacenamiento y reenvío, un rover marciano no podría comunicarse con Tierra: nunca hay una ruta continua. Entender los contactos, las capacidades y el encaminamiento es la base del diseño de redes interplanetarias.

📘 **Dónde se aprende** (2 clases): [B89-C13 · Protocolos para espacio profundo](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md); [B94-C04 · Redes con retardo y desconexión: enrutamiento y almacenamiento](../programa/clases/B94/B94-C04-redes-con-retardo-y-desconexion-enrutamiento-y-almacenamiento/CLASE.md).

### Almacenar y reenviar

- El modelo circular supone órbitas circulares coplanares de 1 UA y 1,524 UA; la distancia es `√(1 + 1,524² − 2·1,524·cos θ)` UA con `θ = 2π t/779,9 d`. Almacenar y reenviar envía toda la información en un solo paquete.
- La convergencia es que dos copias acaban idénticas. Almacenar y reenviar guarda localmente hasta que hay enlace.
- La razón de verosimilitud positiva es `S/(1 − E)`. Almacenar y reenviar guarda las imágenes para enviarlas después.

💡 **Cómo se explica en la clase [B105-C15](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md):**
- P --> E["varios turnos o<br/>almacenar y reenviar"]
- 🎯 **Por qué importa:** Una conversación en tiempo real es posible a la Luna (2,6 s de ida y vuelta) y deja de serlo a Marte (hasta 42 min). La decisión central: ¿cuánto dura una consulta según el destino y el diseño del intercambio (varios turnos o un paquete completo)?

📘 **Dónde se aprende** (3 clases): [B105-C15 · Telemedicina espacial](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md); [B116-C03 · Historia clínica remota y registros médicos de misión](../programa/clases/B116/B116-C03-historia-clinica-remota-y-registros-medicos-de-mision/CLASE.md); [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### Alpha-5

- OMM es un mensaje de elementos orbitales por campos. Alpha-5 es la ampliación del campo numérico con una letra inicial.

💡 **Cómo se explica en la clase [B118-C02](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md):**
- Por identificador: número de 5 dígitos o Alpha-5.
- El ejemplo conductor: el número 123 456 se escribe `C3456` en Alpha-5.
- ⚠️ **Error frecuente:** Creer que Alpha-5 usa la I y la O. Se corrige con 8.1: se omiten.
- 🎯 **Por qué importa:** Sin un catálogo no hay conjunciones: cada alerta empieza identificando de qué objeto habla. Los formatos antiguos tienen límites de tamaño y la asociación de observaciones puede equivocarse.

📘 **Dónde se aprende** (1 clase): [B118-C02 · Catálogos de objetos espaciales](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md).

### Alqueno

- Un hidrocarburo contiene sólo carbono e hidrógeno: alcano (enlaces simples, `CₙH₂ₙ₊₂`, como el metano `CH₄`), alqueno (un doble enlace, `CₙH₂ₙ`, como el eteno `C₂H₄`), alquino (un triple enlace) y aromático (anillos con enlaces alternados, como el benceno `C₆H₆`).

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- H --> A2["Alqueno: CnH2n, insaturación 1"]
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Alquino

- Un hidrocarburo contiene sólo carbono e hidrógeno: alcano (enlaces simples, `CₙH₂ₙ₊₂`, como el metano `CH₄`), alqueno (un doble enlace, `CₙH₂ₙ`, como el eteno `C₂H₄`), alquino (un triple enlace) y aromático (anillos con enlaces alternados, como el benceno `C₆H₆`).

🎯 **Por qué importa (clase B06-C16):** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Alta

- Un pase falso es cumplir el criterio por ruido. Alta aquí es solo el nombre del evento simulado, no un criterio clínico.

💡 **Cómo se explica en la clase [B107-C09](../programa/clases/B107/B107-C09-progresion-de-recuperacion-y-criterios-de-alta/CLASE.md):**
- Sin ruido, la regla da el alta en la primera evaluación (cada 5 d) posterior a 50,2: el día 55 con `k = 1` y el 60 con `k = 2`.
- Con 4.000 simulaciones: `k = 1` da mediana del día de alta 50 (P10–P90: 40–60) y `66,8 %` de altas antes del día 55;
- ⚠️ **Error frecuente:** Presentar la regla como criterio real de alta. La clase no fija criterios (sección 21).
- 🎯 **Por qué importa:** Los fragmentos consultados indican que la pérdida de fuerza tras misiones largas conlleva riesgos operativos y médicos (English et al., 2015) y que existen baterías de pruebas funcionales y medidas fisiológicas (Mulavara et al., 2018). Una regla de alta combina varios indicadores con ruido.

📘 **Dónde se aprende** (1 clase): [B107-C09 · Progresión de recuperación y criterios de alta](../programa/clases/B107/B107-C09-progresion-de-recuperacion-y-criterios-de-alta/CLASE.md).

### Altacimutal

- La altacimutal tiene un eje vertical (acimut) y uno horizontal (altura); la ecuatorial tiene un eje (de ascensión recta) paralelo al eje de la Tierra y otro (de declinación) perpendicular.

💡 **Cómo se explica en la clase [B08-C15](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md):**
- Un objeto a 85° de altura y acimut 100° pide `+12,8″/s` en altura y `+18,3″/s` en acimut; cerca del cenit, `tan h` crece sin límite y el acimut debe cambiar muy rápido: la montura altacimutal pierde el objeto («agujero del cenit»).
- Una altacimutal debe mover dos ejes a velocidades que cambian con la posición del objeto.
- 🎯 **Por qué importa:** A 120 aumentos, un planeta cruza el ocular en menos de dos minutos y tienes que empujar el tubo constantemente. La pregunta motivadora: ¿qué montura necesito y qué error puedo tolerar al seguir un objeto?

📘 **Dónde se aprende** (1 clase): [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md).

### Alternativa

- La hipótesis nula `H₀` es la afirmación que se pone a prueba (aquí: «las dos estimaciones apuntan al mismo valor»); la alternativa `H₁` es su negación.
- Una hipótesis de investigación es la afirmación sustantiva que quieres evaluar; la hipótesis nula `H₀` es la que niega el efecto, y la alternativa `H₁` la que lo afirma.

💡 **Cómo se explica en la clase [B12-C09](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md):**
- ⚠️ **Error frecuente:** Elegir la alternativa o la prueba tras ver los datos. Se corrige con el ejercicio 3.
- 🎯 **Por qué importa:** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.

📘 **Dónde se aprende** (2 clases): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md).

### Alternativa equivalente

- Una alternativa equivalente entrega la misma información por otra vía.

🎯 **Por qué importa (clase B128-C03):** «Alternativa» no significa «versión reducida». Si el relieve pierde resolución o el texto omite el lado iluminado, la persona recibe menos información que quien mira.

📘 **Dónde se aprende** (1 clase): [B128-C03 · Alternativas a la observación visual](../programa/clases/B128/B128-C03-alternativas-a-la-observacion-visual/CLASE.md).

### Altitud

- La altitud `h` es el ángulo sobre el horizonte.
- La altitud es `r` menos el radio del cuerpo.
- La altitud es el ángulo de un objeto sobre el horizonte.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C05](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md):**
- (Esto es derivación implícita en pequeño; se generaliza en C06.) Se anula en `H = 0`: en la culminación la altitud deja de subir y todavía no baja.
- Paso 1 · Altitud. `sin h = cos φ · cos H = 0,83437 · 0,5 = 0,41718`;
- 🎯 **Por qué importa:** Un telescopio con montura altacimutal apunta con dos ejes: altitud y azimut. Para mantener una estrella en el centro del campo, cada eje debe girar a una velocidad que cambia con el tiempo.

📘 **Dónde se aprende** (5 clases): [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md); [B42-C17 · Estrellas guía artificiales](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md); [B48-C04 · Planificación por visibilidad](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md); [B71-C07 · Órbitas circulares](../programa/clases/B71/B71-C07-orbitas-circulares/CLASE.md); [B128-C01 · Accesibilidad de la observación nocturna](../programa/clases/B128/B128-C01-accesibilidad-de-la-observacion-nocturna/CLASE.md).

### Altitud de quemado

- La altitud de quemado es la altitud al agotarse el propelente.

🎯 **Por qué importa (clase B77-C09):** La velocidad final de un ascenso es el `Δv` ideal menos dos pérdidas. La decisión central: ¿cuánto vale la pérdida aerodinámica frente a la gravitacional y de qué depende?

📘 **Dónde se aprende** (1 clase): [B77-C09 · Pérdidas aerodinámicas](../programa/clases/B77/B77-C09-perdidas-aerodinamicas/CLASE.md).

### Altitud del pico

- La altitud del pico es donde ocurre ese máximo.

💡 **Cómo se explica en la clase [B77-C14](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md):**
- *Descripción textual:* la entrada, el ángulo y el coeficiente balístico dan la ecuación de movimiento; su solución cerrada da la desaceleración máxima y la altitud del pico, que se contrastan con una integración numérica.
- Descripción larga: la desaceleración máxima crece con el seno del ángulo de entrada y no depende del coeficiente balístico; este solo mueve la altitud del pico.
- 🎯 **Por qué importa:** La desaceleración máxima fija la carga sobre la carga útil y sobre la tripulación. La decisión central: ¿qué ángulo de entrada limita la desaceleración y de qué propiedades del vehículo no depende?

📘 **Dónde se aprende** (1 clase): [B77-C14 · Dinámica de reentrada](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md).

### Altitud equivalente

- La altitud equivalente sigue la atmósfera estándar ISA: `p = 101,325 (1 − 2,25577·10⁻⁵ h)^5,25588 kPa`.

💡 **Cómo se explica en la clase [B105-C21](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md):**
- La altitud equivalente solo compara presión total y no es una medida de riesgo.
- ⚠️ **Error frecuente:** Tomar la altitud equivalente como riesgo. Solo equivale en presión total.
- 🎯 **Por qué importa:** La misma cantidad de oxígeno inspirado no significa lo mismo a 101 kPa que a 70 kPa: importa la presión parcial. La decisión central: ¿qué presión parcial de oxígeno alveolar resulta de una atmósfera dada y cómo cambia con el CO₂ ambiente y la ventilación?

📘 **Dónde se aprende** (1 clase): [B105-C21 · Fisiología respiratoria en microgravedad y atmósferas de cabina](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md).

### Altitud máxima

- La altitud máxima es aquella en que `cos i = −1`.

💡 **Cómo se explica en la clase [B72-C13](../programa/clases/B72/B72-C13-orbitas-heliosincronicas/CLASE.md):**
- Por periodo y LTAN. Por altitud máxima. Por deriva: minutos por año por cada décima de grado.
- La altitud máxima circular es `5974 km`.
- 🎯 **Por qué importa:** La misma hora local de paso significa la misma iluminación en cada imagen: es lo que usan las misiones de observación de la Tierra. La decisión central: ¿qué inclinación corresponde a cada altitud y cuánta deriva de hora local produce un error de inclinación?

📘 **Dónde se aprende** (1 clase): [B72-C13 · Órbitas heliosincrónicas](../programa/clases/B72/B72-C13-orbitas-heliosincronicas/CLASE.md).

### Altura

- La altura de un astro es su ángulo sobre el horizonte.
- La altura `h` es la distancia del objeto a la base.
- La altura `h` es el ángulo de un astro sobre el horizonte (0° horizonte, 90° cenit); la distancia cenital es `z = 90° − h`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C11](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md):**
- Su altura sobre el horizonte es igual a la latitud: `|φ| = 33,45°` para nuestro lugar.
- La altura meridiana es `h = 90° − |φ − δ|`.
- 🎯 **Por qué importa:** Antes de cualquier telescopio, la humanidad dedujo mucho del cielo a simple vista. Que el Sol «salga» y «se ponga» es una observación; que la Tierra gire es una interpretación (C05) que explica además el movimiento de todas las estrellas.

📘 **Dónde se aprende** (5 clases): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md); [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B28-C16 · Redes internacionales de alertas](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md); [B36-C06 · Formación de halos y función de masa](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md).

### Altura balística

- La altura balística sale de la conservación de energía.

🎯 **Por qué importa (clase B53-C15):** La fracción que escapa decide cuánto material llega al anillo y cuánto se deposita en la superficie. La decisión central: ¿qué parte de los granos supera la velocidad de escape y a qué altura llegan los demás?

📘 **Dónde se aprende** (1 clase): [B53-C15 · Geología de Encélado](../programa/clases/B53/B53-C15-geologia-de-encelado/CLASE.md).

### Altura crítica

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B34-C08](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md):**
- *Descripción textual:* el campo externo define el índice de decaimiento y la altura crítica; la masa y la altura dan las energías.
- Con `h₀ = 50 Mm` y `n_c = 1,5` (ilustrativo), la altura crítica es `50 Mm`.
- 🎯 **Por qué importa:** Saber a qué altura el campo ya no sostiene al filamento sirve para anticipar erupciones. La decisión central: ¿a qué altura el decaimiento del campo supera el umbral?

📘 **Dónde se aprende** (1 clase): [B34-C08 · Erupciones de filamentos y prominencias](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md).

### Altura de capa

- La altura de capa `h` es el grosor de cada pasada.

🎯 **Por qué importa (clase B59-C13):** Una capa más fina da mejor forma pero más tiempo; y una cúpula tiene una zona alta que no se puede imprimir sin apoyo. La decisión central: ¿qué grosor de capa y qué perfil de cúpula hacen viable la impresión?

📘 **Dónde se aprende** (1 clase): [B59-C13 · Impresión 3D extraterrestre](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md).

### Altura de escala

- La altura de escala `H` es la distancia en que la presión baja un factor `e` en una atmósfera isoterma.
- La altura de escala `H` es la altura a la que la presión de una atmósfera isoterma cae por un factor `e ≈ 2,718`.
- La altura de escala `H` de una atmósfera exponencial es la altitud en la que la densidad cae a `1/e`.
- *(y 8 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C09](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md):**
- A --> D["Altura de escala: H = R T / (M g)"]
- *Descripción textual:* a partir de los datos de presión, temperatura, masa molar y gravedad se calcula la densidad y la altura de escala; después se decide si el modelo ideal sirve, según si la presión es baja y la temperatura alta respecto del punto crítico, o si hay que usar el factor `Z` o datos reales.
- 🎯 **Por qué importa:** La NASA publica para Marte, Venus y la Tierra la presión y la temperatura medias en la superficie, la gravedad, el peso molecular de la atmósfera y su densidad (S1, S2, S3). ¿Puedes reproducir esa densidad con sólo lo anterior?

📘 **Dónde se aprende** (18 clases): [B05-C14 · Gases y presión](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md); [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md); [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md); [B29-C11 · Atmósferas exoplanetarias](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md); [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md); [B30-C17 · Auroras y corrientes ionosféricas](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md) y 12 más.

### Altura de la superficie

- La altura de la superficie es `SSH = H − R` más correcciones.

💡 **Cómo se explica en la clase [B57-C09](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md):**
- La altura de la superficie requiere restar al `R` el retraso atmosférico, las mareas, la presión y el sesgo de estado del mar, y conocer la órbita del satélite con precisión de centímetros.
- 🎯 **Por qué importa:** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Altura de obstáculo

- La altura de obstáculo es la diferencia entre la altura central y el plano ajustado a su vecindad 3×3.

💡 **Cómo se explica en la clase [B102-C08](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md):**
- *Descripción textual:* las elevaciones dan la pendiente y, con el plano local, la altura de obstáculo y la rugosidad; los tres forman el coste de celda y Dijkstra obtiene la ruta de mínimo coste.
- 🎯 **Por qué importa:** Elegir la ruta es elegir qué riesgo se acepta. La decisión central: ¿qué celdas son intransitables, cuánto cuesta cruzar las demás y cuánto se alarga la ruta de mínimo riesgo respecto de la recta?

📘 **Dónde se aprende** (1 clase): [B102-C08 · Traversabilidad y evaluación de riesgo de terreno](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md).

### Altura del horizonte

- La altura del horizonte `h` es el ángulo sobre el horizonte matemático de la línea visible hacia esa dirección.

💡 **Cómo se explica en la clase [B02-C08](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md):**
- El estudio de S1 midió el azimut de cada eje con imágenes satelitales y el ángulo de altura del horizonte con un modelo digital de elevación (SRTM) con una aproximación de unos 0,5°; cuando el horizonte estaba muy cerca, usó una herramienta de perfil de elevación para precisar (S1).
- La altura del horizonte no es una variable aleatoria: es un hecho de cada lugar, y por eso S1 la obtiene para cada edificio en lugar de suponer un horizonte plano.
- 🎯 **Por qué importa:** Decir «esta puerta mira al solsticio» es fácil; demostrarlo es difícil. Hay que medir bien, conocer el horizonte, descartar el azar y entender el contexto cultural.

📘 **Dónde se aprende** (1 clase): [B02-C08 · Arqueoastronomía y sus métodos](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md).

### Altura del ocular

- La altura del ocular `h` es su distancia vertical al suelo.

💡 **Cómo se explica en la clase [B128-C01](../programa/clases/B128/B128-C01-accesibilidad-de-la-observacion-nocturna/CLASE.md):**
- *Descripción textual:* la altura del pivote, el largo del tubo y la altitud fijan la altura del ocular; se compara con el rango cómodo de cada persona y de ahí sale el plan.
- 🎯 **Por qué importa:** Un telescopio apuntado a un objeto alto pone el ocular fuera del alcance de quien está sentado o es de menor estatura, y uno apuntado a un objeto bajo lo pone incómodo para quien está de pie. La barrera no está en la persona sino en el montaje.

📘 **Dónde se aprende** (1 clase): [B128-C01 · Accesibilidad de la observación nocturna](../programa/clases/B128/B128-C01-accesibilidad-de-la-observacion-nocturna/CLASE.md).

### Altura del rayo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C08):** Los programas de diseño óptico trazan rayos exactos. La decisión central: ¿cuándo se separa el rayo real del paraxial y cómo crece esa diferencia?

📘 **Dónde se aprende** (1 clase): [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md).

### Altura efectiva

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B42-C18):** Una sola corrección solo vale dentro del ángulo isoplanático (unos segundos de arco). La decisión central: ¿cómo se amplía el campo y qué parte de la turbulencia queda sin restricción?

📘 **Dónde se aprende** (1 clase): [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### Altura elipsoidal

- La latitud geodésica `φ` es el ángulo de la normal al elipsoide con el plano ecuatorial; la longitud `λ`, el ángulo desde el meridiano origen; la altura elipsoidal `h`, la distancia a lo largo de la normal.
- La altura elipsoidal `h` es la distancia a lo largo de la normal.

💡 **Cómo se explica en la clase [B13-C11](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md):**
- Una estación de ejemplo está a latitud `−24,6°`, longitud `−70,4°` y altura elipsoidal `2500 m` (valores sintéticos aproximados de un sitio del desierto de Atacama, no de un instrumento concreto).
- ⚠️ **Error frecuente:** Mezclar altura elipsoidal y ortométrica. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una estación terrestre transmite a un satélite; el software de seguimiento necesita su posición en X, Y, Z. El técnico de campo tiene su posición en latitud, longitud y altura.

📘 **Dónde se aprende** (2 clases): [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md); [B53-C06 · Geodesia de Marte](../programa/clases/B53/B53-C06-geodesia-de-marte/CLASE.md).

### Altura límite

- La altura límite es aquella a partir de la cual el voladizo supera `w/2`.

🎯 **Por qué importa (clase B59-C13):** Una capa más fina da mejor forma pero más tiempo; y una cúpula tiene una zona alta que no se puede imprimir sin apoyo. La decisión central: ¿qué grosor de capa y qué perfil de cúpula hacen viable la impresión?

📘 **Dónde se aprende** (1 clase): [B59-C13 · Impresión 3D extraterrestre](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md).

### Altura sobre la superficie

- La altura sobre la superficie sigue de `dz = −(c_p/g) dT`.

🎯 **Por qué importa (clase B54-C13):** Venus es el caso extremo de atmósfera densa y caliente. La pregunta motivadora: ¿cómo se enfría su atmósfera con la altura y cuánto pesa?

📘 **Dónde se aprende** (1 clase): [B54-C13 · Atmósfera de Venus](../programa/clases/B54/B54-C13-atmosfera-de-venus/CLASE.md).

### Ambigüedad

- La ambigüedad es la coexistencia de varias lecturas plausibles.

💡 **Cómo se explica en la clase [B119-C32](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md):**
- Límite: la interpretación jurídica no es un concurso de votos; un panel mide ambigüedad, no corrección.
- Descripción larga: cada fuente adicional reduce la ambigüedad y fortalece una lectura, pero no la elimina.
- ⚠️ **Error frecuente:** Confundir ambigüedad con error. Se corrige con 8.4.
- 🎯 **Por qué importa:** B119 enseña los tratados y su contenido, no el método para interpretarlos, que el rol de derecho espacial exige; la regla general de interpretación se menciona como conocimiento no verificado. La decisión central: ¿cuánta ambigüedad queda en una cláusula y qué fuentes de interpretación la reducen más?

📘 **Dónde se aprende** (1 clase): [B119-C32 · Interpretación de tratados internacionales](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md).

### Ambigüedad de ciclo

- La ambigüedad de ciclo es un salto de `1/Δν_canal`.

💡 **Cómo se explica en la clase [B46-C18](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar la ambigüedad de ciclo. Se corrige con 8.3.
- 🎯 **Por qué importa:** La precisión del retardo es lo que permite la geodesia por VLBI: milímetros de línea de base. La decisión central: ¿cuánta banda y S/N se necesitan para fijar el retardo a una precisión dada?

📘 **Dónde se aprende** (1 clase): [B46-C18 · VLBI y geodesia](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md).

### Ambigüedad de declinación

- La ambigüedad de declinación es la pérdida de sensibilidad a `δ` cuando `δ → 0`.

🎯 **Por qué importa (clase B74-C17):** El Doppler apenas distingue la declinación cuando la nave está cerca del ecuador celeste: la firma de la rotación terrestre depende de `sin δ`. La decisión central: ¿qué observable cubre la dirección que los demás no ven?

📘 **Dónde se aprende** (1 clase): [B74-C17 · Navegación en espacio profundo](../programa/clases/B74/B74-C17-navegacion-en-espacio-profundo/CLASE.md).

### Ambigüedad de pose

- La ambigüedad de pose aparece con poca perspectiva (objeto pequeño, lejano o visto de frente).

🎯 **Por qué importa (clase B103-C07):** A 8 m un marcador de 10 cm mide 10 px y su pose es casi indeterminada; a 1 m, el error de profundidad es de unos 3 mm. La decisión central: ¿hasta qué distancia es fiable la pose estimada con un objeto de cierto tamaño, y cuándo hay que dudar de ella?

📘 **Dónde se aprende** (1 clase): [B103-C07 · Estimación de pose de objetos y objetivos por visión](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md).

### Ambigüedad inclinación–traslación

- La ambigüedad inclinación-traslación es que una inclinación `θ` y una aceleración `a = g sen θ` dan la misma fuerza en el eje.
- La ambigüedad inclinación–traslación surge porque `f` mezcla gravedad y aceleración.

🎯 **Por qué importa (clase B105-C04):** En la Tierra el cerebro usa la gravedad como referencia de «abajo». En caída libre esa referencia desaparece y el sensor sigue midiendo, pero su señal significa otra cosa.

📘 **Dónde se aprende** (2 clases): [B105-C04 · Sistema vestibular](../programa/clases/B105/B105-C04-sistema-vestibular/CLASE.md); [B107-C03 · Entrenamiento vestibular y de orientación espacial](../programa/clases/B107/B107-C03-entrenamiento-vestibular-y-de-orientacion-espacial/CLASE.md).

### Ambigüedad nπ

- La ambigüedad `nπ` del ángulo de polarización.

🎯 **Por qué importa (clase B51-C05):** A frecuencias bajas la ionosfera domina el error de fase y de polarización. La decisión central: ¿cómo se mide y se quita el efecto con las propias frecuencias de la observación?

📘 **Dónde se aprende** (1 clase): [B51-C05 · Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md).

### Amenaza

- La amenaza es la probabilidad e intensidad del fenómeno; la exposición es lo que está en su camino; la vulnerabilidad es cuán dañable es.
- Una amenaza es una causa potencial de daño.

💡 **Cómo se explica en la clase [B57-C19](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md):**
- H["amenaza"] --> P["producto H x E x V"]
- Tres capas de `60 × 60` celdas sintéticas: la amenaza se concentra en el noroeste, la exposición en el centro y la vulnerabilidad crece hacia el este.
- 🎯 **Por qué importa:** Los mapas de riesgo orientan decisiones y presupuestos, pero dependen de supuestos de ponderación que suelen quedar ocultos. La decisión central: ¿cómo combino capas y cuánto cambian las zonas prioritarias si cambio los pesos?

📘 **Dónde se aprende** (2 clases): [B57-C19 · SIG y análisis de riesgo](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md); [B122-C03 · Modelo defensivo de riesgos de infraestructura espacial](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md).

### Amina

- Un grupo funcional es una agrupación de átomos que da propiedades características: alcohol (–OH, como el etanol `C₂H₆O`), aldehído (–CHO, como el formaldehído `CH₂O`), ácido carboxílico (–COOH, como el fórmico `CH₂O₂` y el acético `C₂H₄O₂`) y amina (–NH₂, como la metilamina `CH₅N`).

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- Una amina (–NH₂) acepta un protón: la metilamina `CH₃NH₂` forma `CH₃NH₃⁺`.
- Los aminoácidos tienen a la vez un grupo amina y uno carboxílico: la glicina es `C₂H₅NO₂`, de masa molar 75,067 g/mol y grado de insaturación 1.
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Amortiguamiento

- El amortiguamiento disipa energía; su medida adimensional es `ζ` (razón de amortiguamiento).
- La rigidez `Kp` y el amortiguamiento `Kd` son las ganancias del control.
- En un sistema de segundo orden, la frecuencia natural `ωn` (rad/s) y el amortiguamiento `ζ` (adimensional) fijan la forma: `θ̈ + 2ζωn θ̇ + ωn² θ = ωn² r`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- Menos amortiguamiento, más amplificación; por eso se evita excitar una estructura en su frecuencia propia.
- Los resultados valen si `F = −k x` (resorte lineal, deformaciones pequeñas) y si el amortiguamiento es simple.
- ⚠️ **Error frecuente:** Ignorar el amortiguamiento al hablar de resonancia. Ejercicio 7.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende** (6 clases): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md); [B87-C17 · Control de tres ejes](../programa/clases/B87/B87-C17-control-de-tres-ejes/CLASE.md); [B107-C07 · Rehabilitación vestibular y del equilibrio posterior al vuelo](../programa/clases/B107/B107-C07-rehabilitacion-vestibular-y-del-equilibrio-posterior-al-vuelo/CLASE.md).

### Amortiguamiento B_d

- Rigidez deseada `K_d`: N/m. Amortiguamiento `B_d`: N s/m.

🎯 **Por qué importa (clase B101-C07):** Si un brazo muy rígido empuja una pieza que está 5 mm más lejos de lo que cree, aplica una fuerza grande. La decisión central: ¿qué rigidez y qué amortiguamiento le doy al extremo para que el contacto sea suave y la fuerza predecible?

📘 **Dónde se aprende** (1 clase): [B101-C07 · Control de fuerza e impedancia en manipulación](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md).

### Amortiguamiento de Landau

- El amortiguamiento de Landau es la pérdida sin colisiones de una onda.

💡 **Cómo se explica en la clase [B35-C04](../programa/clases/B35/B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md):**
- El amortiguamiento de Landau es el intercambio de energía con los autos que van casi a la velocidad de la onda.
- 🎯 **Por qué importa:** Saber si un plasma es colisional decide qué modelo usar. La decisión central: ¿es el camino libre medio mayor o menor que la escala del problema?

📘 **Dónde se aprende** (1 clase): [B35-C04 · Colisiones, régimen cinético y ecuación de Vlasov](../programa/clases/B35/B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md).

### Amortiguamiento λ

- Número de condición: `σ_max/σ_min`. Amortiguamiento `λ`: parámetro del método DLS.

🎯 **Por qué importa (clase B101-C03):** Con el brazo casi estirado, pedirle un movimiento de 5 cm/s a lo largo de su eje exige velocidades articulares de varios rad/s. La decisión central: ¿cuán cerca de una singularidad estoy y qué error de seguimiento acepto para no exigir lo imposible?

📘 **Dónde se aprende** (1 clase): [B101-C03 · Singularidades y manipulabilidad de brazos robóticos](../programa/clases/B101/B101-C03-singularidades-y-manipulabilidad-de-brazos-roboticos/CLASE.md).

### Amortización

- La amortización (*payback*) es el tiempo en que la masa evitada iguala la masa invertida.

💡 **Cómo se explica en la clase [B59-C19](../programa/clases/B59/B59-C19-evaluacion-logistica-de-una-instalacion/CLASE.md):**
- *Descripción textual:* la masa total y la producción efectiva fijan el tiempo de amortización; la simulación da su dispersión por las paradas.
- La disponibilidad es `0,9259`, la amortización ideal `236 días` y con paradas `255 días`; la simulación da P10 = `245`, P50 = `254` y P90 = `267` días.
- 🎯 **Por qué importa:** Una planta que produce 10 kg/día no se paga sola si está parada. La decisión central: ¿cuántos días de operación hacen falta para que la masa de producto evitada iguale la masa de la planta?

📘 **Dónde se aprende** (1 clase): [B59-C19 · Evaluación logística de una instalación](../programa/clases/B59/B59-C19-evaluacion-logistica-de-una-instalacion/CLASE.md).

### Ampliación

- La ampliación (o aumento) es cuántas veces se magnifica la imagen.

🎯 **Por qué importa (clase B02-C13):** Un instrumento nuevo da datos nuevos, pero los datos nuevos no se interpretan solos. La pregunta motivadora es: ¿qué podía concluir Galileo de lo que veía, y qué le faltaba para convencer a quienes no creían?

📘 **Dónde se aprende** (1 clase): [B02-C13 · Galileo y primeras observaciones telescópicas](../programa/clases/B02/B02-C13-galileo-y-primeras-observaciones-telescopicas/CLASE.md).

### Ampliada

- La incertidumbre combinada `u_c` es su suma en cuadratura y la ampliada es `U = k u_c`.

💡 **Cómo se explica en la clase [B102-C06](../programa/clases/B102/B102-C06-dinamometria-y-medicion-de-fuerzas-de-traccion/CLASE.md):**
- Paso 4 · Ampliada. `U = 2 × 0,251 = 0,502 N`.
- 🎯 **Por qué importa:** Un tiro de barra de `176,8 N` sin incertidumbre no se puede comparar con un modelo. La decisión central: ¿con qué incertidumbre se mide una fuerza de tracción y qué parte viene del ruido, de la calibración y de la referencia?

📘 **Dónde se aprende** (1 clase): [B102-C06 · Dinamometría y medición de fuerzas de tracción](../programa/clases/B102/B102-C06-dinamometria-y-medicion-de-fuerzas-de-traccion/CLASE.md).

### Amplificación

- La amplificación escala como `δ^{2+α}` para un chorro continuo y `δ^{3+α}` para un blob, con `α` el índice espectral.

💡 **Cómo se explica en la clase [B27-C11](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md):**
- Con `γ = 10`, `β = 0,994 987`, el máximo de `β_app` es `9,9499` a `5,7392°` de la visual (`1/γ = 5,7296°`); la amplificación Doppler va de `δ = 19,95` si el chorro apunta hacia nosotros a `δ = 0,1` si lo vemos de lado.
- 🎯 **Por qué importa:** Un chorro que se acerca puede parecer más rápido que la luz sin violar nada, y su brillo cambia en órdenes de magnitud según el ángulo. Sin estos efectos no se pueden comparar chorros ni inferir su velocidad.

📘 **Dónde se aprende** (1 clase): [B27-C11 · Chorros relativistas](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md).

### Amplificación de libración

- La amplificación de libración es `C_total/C_capa`.

💡 **Cómo se explica en la clase [B53-C27](../programa/clases/B53/B53-C27-deteccion-remota-de-oceanos-subsuperficiales-induccion-magnetica-libracion-y-radar/CLASE.md):**
- Una amplificación de libración por encima de 1 apunta a desacoplamiento, pero depende de la inercia asumida; la inducción magnética necesita que el océano sea más grueso que `δ` para dar señal clara.
- 🎯 **Por qué importa:** Cada método ve algo distinto y ninguno basta solo. La decisión central: ¿qué señal esperaría un océano de cierta conductividad y espesor y cuánto se distingue de un cuerpo sólido?

📘 **Dónde se aprende** (1 clase): [B53-C27 · Detección remota de océanos subsuperficiales: inducción magnética, libración y radar](../programa/clases/B53/B53-C27-deteccion-remota-de-oceanos-subsuperficiales-induccion-magnetica-libracion-y-radar/CLASE.md).

### Amplificación del eje

- La amplificación del eje es ensanchar un rango pequeño para que se note.

🎯 **Por qué importa (clase B128-C07):** Un mapeo sin reglas explícitas engaña: si la escala de tono se estira para que se oiga una caída de 1 %, el oyente puede creer que la caída fue enorme. La decisión central: ¿qué se mapea a qué, con qué escala, y cómo se avisa de la amplificación?

📘 **Dónde se aprende** (1 clase): [B128-C07 · Modelos táctiles y sonificación](../programa/clases/B128/B128-C07-modelos-tactiles-y-sonificacion/CLASE.md).

### Amplificación del ruido

- La amplificación del ruido del escalado es el factor `t₂/t₁`.
- La amplificación del ruido de dos bandas.

🎯 **Por qué importa (clase B44-C13):** La oscuridad depende de la exposición y de la temperatura, y algunos píxeles son muy calientes. La decisión central: ¿se puede reutilizar un dark de otra exposición, y a qué costo en ruido?

📘 **Dónde se aprende** (2 clases): [B44-C13 · Calibración con dark](../programa/clases/B44/B44-C13-calibracion-con-dark/CLASE.md); [B51-C10 · Retardo troposférico e ionosférico en VLBI y su modelado](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md).

### Amplificación máxima

- Q: factor de calidad del oscilador de análisis. Amplificación máxima: SRS máximo dividido por `A`.

🎯 **Por qué importa (clase B90-C10):** Dos pulsos con distinta forma pueden dañar lo mismo si sus SRS coinciden, y un pulso con gran aceleración pico puede ser inofensivo para un equipo de baja frecuencia. La decisión central: ¿qué frecuencias de mi equipo están amenazadas por este choque y con qué nivel?

📘 **Dónde se aprende** (1 clase): [B90-C10 · Ensayos de choque](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md).

### Amplitud

- La amplitud `A` es el desplazamiento máximo;
- La amplitud `A` es su valor máximo desde el centro.
- La amplitud `A_x` es la distancia de partida a L1.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- El período es `T = 2π√(m/k)`, independiente de la amplitud.
- Con roce proporcional a la velocidad, la amplitud decae exponencialmente.
- ⚠️ **Error frecuente:** Pensar que el período depende de la amplitud. Ejercicio 9.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende** (8 clases): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md); [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md); [B40-C05 · Perturbaciones primordiales y espectro escalar](../programa/clases/B40/B40-C05-perturbaciones-primordiales-y-espectro-escalar/CLASE.md); [B73-C05 · Órbitas periódicas](../programa/clases/B73/B73-C05-orbitas-periodicas/CLASE.md) y 2 más.

### Amplitud de cierre

- La amplitud de cierre (razón de cuatro amplitudes).

💡 **Cómo se explica en la clase [B51-C02](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md):**
- El máximo de diferencias en los 20 triángulos es 2,22 × 10⁻¹⁶ rad; en amplitud de cierre, 6,66 × 10⁻¹⁶.
- 🎯 **Por qué importa:** Cuando las ganancias no se pueden calibrar (VLBI con atmósfera rápida, autocalibración), los cierres son los observables robustos. La decisión central: ¿qué información sobrevive a los errores por antena y cuánta se pierde?

📘 **Dónde se aprende** (1 clase): [B51-C02 · Cantidades de cierre: fase y amplitud de cierre](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md).

### Amplitud de modulación

- La amplitud de modulación `A = 2√(I₁I₂)`.

💡 **Cómo se explica en la clase [B42-C09](../programa/clases/B42/B42-C09-interferometria-de-dos-haces/CLASE.md):**
- La fase mejora con visibilidad alta y amplitud de modulación grande; con la mitad de visibilidad el error se duplicaría.
- 🎯 **Por qué importa:** La medida interferométrica de fase es la base de la metrología óptica (superficies, frentes de onda; C13).

📘 **Dónde se aprende** (1 clase): [B42-C09 · Interferometría de dos haces](../programa/clases/B42/B42-C09-interferometria-de-dos-haces/CLASE.md).

### Amplitud y fase

- La solución de fase sola frente a amplitud y fase.

💡 **Cómo se explica en la clase [B51-C06](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md):**
- El paso a amplitud y fase corrige la escala de 6,9 % a 0,74 %.
- 🎯 **Por qué importa:** Sin autocalibración, los errores de ganancia de la atmósfera limitan el rango dinámico. La decisión central: ¿converge el ciclo modelo–ganancias, a qué valor y con qué sesgo?

📘 **Dónde se aprende** (1 clase): [B51-C06 · Autocalibración iterativa con modelo de cielo](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md).

### AN

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

🎯 **Por qué importa (clase B43-C26):** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?

📘 **Dónde se aprende** (1 clase): [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### Análisis

- El análisis hace lo inverso.

🎯 **Por qué importa (clase B118-C22):** B118-C18 trata la gestión del tráfico en general, pero no cubre formatos ni acuerdos de intercambio. Un error de unidades (metros contra kilómetros) puede cambiar una decisión por un factor 1000.

📘 **Dónde se aprende** (1 clase): [B118-C22 · Intercambio de datos de vigilancia entre operadores y Estados](../programa/clases/B118/B118-C22-intercambio-de-datos-de-vigilancia-entre-operadores-y-estados/CLASE.md).

### Análisis confirmatorio

- El análisis confirmatorio prueba lo especificado antes; el exploratorio busca patrones sin plan previo (S1).

💡 **Cómo se explica en la clase [B20-C02](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md):**
- D --> E["Análisis confirmatorio según el plan"]
- De la hipótesis se pasa a un plan escrito; el plan se archiva con fecha; luego se obtienen los datos; de ahí salen dos ramas, un análisis confirmatorio que sigue el plan y un análisis exploratorio rotulado; ambas confluyen en un informe que incluye las desviaciones declaradas.
- 🎯 **Por qué importa:** Un grupo mide cinco variantes razonables de un mismo análisis y publica la que da «un resultado significativo». Nadie mintió con un número, y sin embargo el resultado ya no significa lo que dice.

📘 **Dónde se aprende** (1 clase): [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md).

### Análisis de impacto

- El análisis de impacto calcula qué se afecta si algo cambia.

🎯 **Por qué importa (clase B83-C05):** Cuando cambia un requisito, ¿qué piezas y qué pruebas hay que revisar? Sin trazabilidad, nadie lo sabe y el cambio rompe algo en silencio.

📘 **Dónde se aprende** (1 clase): [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md).

### Análisis de sensibilidad

- Un análisis de sensibilidad es repetir el análisis cambiando una decisión para ver cuánto cambia la conclusión.

💡 **Cómo se explica en la clase [B47-C20](../programa/clases/B47/B47-C20-caso-comparativo-de-observatorios-espaciales/CLASE.md):**
- ⚠️ **Error frecuente:** Concluir sin análisis de sensibilidad. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un ranking depende de los pesos elegidos. La decisión central: ¿qué conclusión sobrevive cuando los pesos cambian?

📘 **Dónde se aprende** (2 clases): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md); [B47-C20 · Caso comparativo de observatorios espaciales](../programa/clases/B47/B47-C20-caso-comparativo-de-observatorios-espaciales/CLASE.md).

### Análisis de varianza (ANOVA) de un factor

- Un análisis de varianza (ANOVA) de un factor descompone la variación total en una parte entre grupos y una parte dentro de los grupos.

🎯 **Por qué importa (clase B13-C14):** Ocho estaciones de seguimiento miden el mismo desfase de un reloj de referencia. Cada una repite su medida cinco veces y obtiene resultados muy parecidos entre sí, pero las estaciones discrepan entre ellas.

📘 **Dónde se aprende** (1 clase): [B13-C14 · Repetibilidad y reproducibilidad](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md).

### Análisis dimensional

- Las dimensiones de una magnitud son sus bases (longitud L, tiempo T, masa M); el análisis dimensional comprueba que ambos lados de una ecuación tengan las mismas dimensiones.
- El análisis dimensional es comprobar que ambos lados de una fórmula tienen la misma dimensión.
- El análisis dimensional comprueba que cada ecuación sea coherente en unidades.

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- El análisis dimensional no garantiza que la fórmula sea correcta, pero detecta una gran parte de los errores.
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.

📘 **Dónde se aprende** (3 clases): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md); [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md); [B83-C12 · Model-Based Systems Engineering](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md).

### Análisis global

- El análisis global examina todo el rango de las entradas.

🎯 **Por qué importa (clase B12-C17):** Mejorar una medida cuesta dinero, masa o tiempo. Si el presupuesto de una misión ofrece mejorar la masa seca o el empuje específico, hay que saber cuál de las dos reduce más la incertidumbre del resultado.

📘 **Dónde se aprende** (1 clase): [B12-C17 · Análisis de sensibilidad](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md).

### Análisis nodal

- El análisis nodal resuelve las tensiones de los nodos.

💡 **Cómo se explica en la clase [B05-C16](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md):**
- Kirchhoff y análisis nodal valen para cualquier red y se programan;
- 🎯 **Por qué importa:** Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: ¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?

📘 **Dónde se aprende** (2 clases): [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md); [B33-C07 · Impactos del clima espacial en redes eléctricas](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md).

### Analizador de Stern–Gerlach

- Un analizador de Stern–Gerlach mide la componente del espín.

🎯 **Por qué importa (clase B31-C05):** El espín explica los desdoblamientos de líneas espectrales y la estructura de la materia. La decisión central: ¿qué probabilidades y qué energías resultan de un espín en un campo?

📘 **Dónde se aprende** (1 clase): [B31-C05 · Espín y momento angular](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md).

### Analizador electrostático

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C24):** La energía por carga elegida por el analizador determina qué se mide; la resolución de los canales limita la temperatura que se recupera. La decisión central: ¿cuántos canales y qué corrección dan la velocidad y la temperatura del plasma con error aceptable?

📘 **Dónde se aprende** (1 clase): [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md).

### Analizador fijo

- La placa de media onda gira el plano; con un analizador fijo la señal es `I_k = ½[I + Q cos 4θ_k + U sin 4θ_k]`.

🎯 **Por qué importa (clase B45-C16):** La polarización medida es siempre positiva y por eso sesgada hacia arriba cuando el ruido es comparable a la señal. La decisión central: ¿cómo se miden Q y U y cómo se corrige el sesgo?

📘 **Dónde se aprende** (1 clase): [B45-C16 · Polarímetros astronómicos](../programa/clases/B45/B45-C16-polarimetros-astronomicos/CLASE.md).

### Analógica

- Una misión analógica reproduce condiciones espaciales en tierra.

💡 **Cómo se explica en la clase [B104-C20](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md):**
- Una misión analógica real tiene objetivos de investigación propios que esta clase no modela.
- 🎯 **Por qué importa:** Cada margen parece suficiente por separado, pero las fallas consumen a la vez agua y tiempo. La decisión central: ¿hasta qué tasa de fallas mantiene la misión una probabilidad de éxito alta, y cuál recurso se agota primero?

📘 **Dónde se aprende** (1 clase): [B104-C20 · Misión tripulada simulada](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md).

### Ancho a media altura

- La banda espectral tiene una respuesta espectral `S(λ)`; su ancho a media altura (FWHM) mide cuán estrecha es.

🎯 **Por qué importa (clase B57-C03):** Dos sensores con el mismo píxel pueden dar información muy distinta si uno distingue 256 niveles y otro 65.536, o si una banda es ancha y otra estrecha. La decisión central: ¿cuántos bits y qué ancho de banda hacen falta para ver el cambio que me interesa?

📘 **Dónde se aprende** (1 clase): [B57-C03 · Resolución radiométrica y espectral](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md).

### Ancho a media potencia

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B46-C03](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md):**
- Una antena de `25 m` a `1,4 GHz` (`λ = 21,41 cm`) con `f = 9 m` tiene `f/D = 0,36`, un plato de `4,34 m` de profundidad, un ancho a media potencia de `30,3 arcmin` y una directividad de `134522`.
- 🎯 **Por qué importa:** El tamaño de la antena fija a la vez la resolución y la sensibilidad. La decisión central: ¿qué diámetro y qué razón focal dan el haz y la ganancia requeridos?

📘 **Dónde se aprende** (1 clase): [B46-C03 · Antenas parabólicas](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md).

### Ancho a mitad de potencia

- El ancho a mitad de potencia (HPBW) mide el haz.
- El ancho a mitad de potencia (HPBW) es el ancho a −3 dB.
- El ancho a mitad de potencia de un pulso comprimido sin ventana es `0,886/B` en tiempo.

💡 **Cómo se explica en la clase [B53-C24](../programa/clases/B53/B53-C24-sondeo-radar-de-penetracion-de-hielo/CLASE.md):**
- El filtro adaptado da un pico con ancho a mitad de potencia:
- La compresión de pulso da un ancho a mitad de potencia de `7,44 m` (teórico `7,48 m`).
- 🎯 **Por qué importa:** Un eco sin escala de profundidad no dice nada. La decisión central: ¿a qué profundidad está una interfaz según su retardo y qué separación mínima permite distinguir dos interfaces?

📘 **Dónde se aprende** (3 clases): [B49-C03 · Apuntamiento y seguimiento de radiotelescopios: modelos de apuntado y errores](../programa/clases/B49/B49-C03-apuntamiento-y-seguimiento-de-radiotelescopios-modelos-de-apuntado-y-errores/CLASE.md); [B49-C05 · Medición y calibración de patrones de antena](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md); [B53-C24 · Sondeo radar de penetración de hielo](../programa/clases/B53/B53-C24-sondeo-radar-de-penetracion-de-hielo/CLASE.md).

### Ancho de banda

- El ancho de banda es los bytes movidos por segundo.
- El ancho de banda es `ω_n`.
- El ancho de banda es la capacidad del enlace (bit/s).
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B18-C03](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md):**
- Si el ancho de banda sostenido es `B` bytes/s, el máximo es `B/24` operaciones/s por mucha CPU que sobre.
- El *benchmark* STREAM (S2) mide el ancho de banda de memoria sostenible con cuatro núcleos sencillos: copia `a = b`, escala `a = q·b`, suma `a = b + c` y *triad* `a = b + q·c`.
- 🎯 **Por qué importa:** Un catálogo con millones de estrellas o una rejilla de simulación pasan cada dato por la CPU una o pocas veces. Cuando las operaciones por dato son pocas, el tiempo no lo fija la CPU sino el viaje de los datos.

📖 **Explicado a fondo:** [Ancho de banda y capacidad de un canal](esencial/ampliacion-a-m.md#ancho-de-banda-y-capacidad-de-un-canal) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md); [B51-C04 · Respuesta de banda y errores dependientes de la frecuencia](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md); [B87-C15 · Apuntamiento de alta precisión](../programa/clases/B87/B87-C15-apuntamiento-de-alta-precision/CLASE.md); [B87-C17 · Control de tres ejes](../programa/clases/B87/B87-C17-control-de-tres-ejes/CLASE.md); [B128-C10 · Acceso con baja conectividad](../programa/clases/B128/B128-C10-acceso-con-baja-conectividad/CLASE.md).

### Ancho de banda de lazo

- El ancho de banda de lazo `B_L` fija ruido y seguimiento.

💡 **Cómo se explica en la clase [B89-C10](../programa/clases/B89/B89-C10-sincronizacion-de-portadora/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir ancho de banda de lazo con ancho de banda de señal. Se corrige con el vocabulario.
- 🎯 **Por qué importa:** Un lazo demasiado ancho deja pasar ruido; uno demasiado estrecho pierde el Doppler. Ajustarlo es el equilibrio central de la sincronización y condiciona la recepción de señales débiles (C24).

📘 **Dónde se aprende** (1 clase): [B89-C10 · Sincronización de portadora](../programa/clases/B89/B89-C10-sincronizacion-de-portadora/CLASE.md).

### Ancho de banda de rechazo

- El ancho de banda de rechazo (0 dB).

🎯 **Por qué importa (clase B42-C16):** El lazo decide qué tan rápido es el rechazo y cuánto ruido se amplifica. La decisión central: ¿qué ganancia da el mejor compromiso entre rechazo, ruido y estabilidad con retardo?

📘 **Dónde se aprende** (1 clase): [B42-C16 · Lazo de control de óptica adaptativa](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md).

### Ancho de banda Doppler

- El ancho de banda Doppler `Ba` es el intervalo de `f_D` barrido en `T`.

🎯 **Por qué importa (clase B69-C01):** Sin el principio Doppler, la resolución en azimut de un radar quedaría fijada por el ancho del haz de la antena: a 850 km, una antena de 12 m (λ = 0,0555 m) iluminaría una franja de unos 3,9 km. La decisión central: ¿qué resolución obtiene el sistema, de qué depende y qué hay que muestrear para no perderla?

📘 **Dónde se aprende** (1 clase): [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md).

### Ancho de banda efectivo

- El ancho de banda efectivo es el que aporta pendiente a la señal.

🎯 **Por qué importa (clase B74-C03):** Un nanosegundo son quince centímetros de alcance, y un pulso ancho en ruido se mide con nanosegundos de incertidumbre. La decisión central: ¿cuánta precisión de alcance permite el ancho de banda y la relación señal/ruido, y qué hay que corregir además del retardo?

📘 **Dónde se aprende** (1 clase): [B74-C03 · Medición de alcance por radio](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md).

### Ancho de haz

- El ancho de haz a media potencia es aproximadamente `70 λ/D` grados.
- El ancho de haz es `θ₃dB ≈ 70 λ/D`.
- Paso por el cenit (keyhole): pasada casi vertical con giro rápido de azimut. Ancho de haz: ángulo de media potencia.

💡 **Cómo se explica en la clase [B89-C03](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md):**
- *Descripción textual:* la frecuencia da la longitud de onda; con el diámetro y la eficiencia se obtiene la ganancia y el ancho de haz, y de este la exigencia de apuntamiento.
- Paso 4 · Ancho de haz. `70 λ/D = 5,39°`.
- 🎯 **Por qué importa:** Elegir la banda es la primera decisión de diseño de un enlace y determina el tamaño de la antena y la tasa alcanzable. La decisión central: ¿qué banda usar para una ganancia de antena dada y qué se paga en apuntamiento por usarla?

📘 **Dónde se aprende** (3 clases): [B89-C03 · Bandas VHF UHF S X Ka](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md); [B89-C06 · Ganancias y pérdidas de antena](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md); [B96-C28 · Control y seguimiento de la antena de estación](../programa/clases/B96/B96-C28-control-y-seguimiento-de-la-antena-de-estacion/CLASE.md).

### Ancho de haz de media potencia

- El ancho de haz de media potencia (HPBW) es el ángulo entre los puntos a −3 dB.

🎯 **Por qué importa (clase B91-C01):** Elegir o diseñar una antena empieza por saber qué fija su ganancia y su haz. La decisión central: ¿cuánta ganancia da una apertura de diámetro `D` a la frecuencia `f`, y qué parte de esa ganancia ideal se pierde en la práctica?

📘 **Dónde se aprende** (1 clase): [B91-C01 · Fundamentos de teoría de antenas](../programa/clases/B91/B91-C01-fundamentos-de-teoria-de-antenas/CLASE.md).

### Ancho de rotación

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B32-C11):** `v sin i` es la rotación proyectada y da pistas de edad y actividad. La decisión central: ¿cómo se mide `v sin i` de un perfil?

📘 **Dónde se aprende** (1 clase): [B32-C11 · Ensanchamiento rotacional y v sin i](../programa/clases/B32/B32-C11-ensanchamiento-rotacional-y-v-sin-i/CLASE.md).

### Ancho de transición

- El ancho de transición es la distancia entre niveles.

🎯 **Por qué importa (clase B21-C05):** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Ancho Doppler

- El ancho Doppler `B` es la dispersión en frecuencia por la rotación.
- El ancho Doppler `(λ/c)√(2kT/m)`.

💡 **Cómo se explica en la clase [B32-C04](../programa/clases/B32/B32-C04-opacidad-de-lineas-ensanchamiento-y-perfil-de-voigt/CLASE.md):**
- A 5772 K el hidrógeno tiene una velocidad térmica de `9,762 km/s` y, en 656,28 nm, un ancho Doppler de `0,02137 nm`.
- 🎯 **Por qué importa:** Las alas de la línea dan la presión y las abundancias. La decisión central: ¿cuándo domina el núcleo gaussiano y cuándo las alas?

📘 **Dónde se aprende** (2 clases): [B32-C04 · Opacidad de líneas: ensanchamiento y perfil de Voigt](../programa/clases/B32/B32-C04-opacidad-de-lineas-ensanchamiento-y-perfil-de-voigt/CLASE.md); [B58-C12 · Radar planetario](../programa/clases/B58/B58-C12-radar-planetario/CLASE.md).

### Ancho equivalente

- El ancho equivalente `W = ∫T dλ`.
- El ancho equivalente de una línea no cambia al convolucionarla.

💡 **Cómo se explica en la clase [B32-C09](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md):**
- *Descripción textual:* la profundidad óptica determina el ancho equivalente, que crece linealmente al principio y luego se satura.
- 🎯 **Por qué importa:** Medir una abundancia exige saber en qué régimen está la línea. La decisión central: ¿cómo depende el ancho equivalente de la columna de absorbedores?

📘 **Dónde se aprende** (5 clases): [B32-C09 · Medición de perfiles de línea: ancho equivalente y ajuste](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md); [B45-C03 · Curvas de transmisión](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md); [B45-C07 · Resolución espectral](../programa/clases/B45/B45-C07-resolucion-espectral/CLASE.md); [B45-C10 · Líneas de emisión](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md); [B45-C11 · Líneas de absorción](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md).

### Ancho ocupado

- El roll-off `α` es el exceso de banda del filtro de coseno alzado; el ancho ocupado es `Rs(1+α)`.

💡 **Cómo se explica en la clase [B89-C02](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md):**
- *Descripción textual:* la tasa de bits, el código y la modulación dan la tasa de símbolos; con el roll-off, el ancho ocupado; este decide cuántos canales caben y la capacidad de Shannon; el Doppler se suma por separado.
- Paso 2 · Ancho ocupado. `B = 10 × 1,35 = 13,5 MHz`.
- 🎯 **Por qué importa:** Sin una idea cuantitativa del ancho de banda no se puede decidir cuántos enlaces caben en una banda ni cuánta tasa de datos es posible. La regulación (C19) trabaja con exactamente estas magnitudes.

📘 **Dónde se aprende** (1 clase): [B89-C02 · Frecuencia y espectro espacial](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md).

### Anchura de ventana

- La anchura de ventana es el intervalo de fechas que cumple una tolerancia angular.

🎯 **Por qué importa (clase B75-C03):** Una ventana de lanzamiento no es un capricho de calendario: es el instante en que la geometría de los dos planetas coincide con la de la elipse de transferencia. La decisión central: ¿en qué fechas se cumple la fase de salida y cuánto margen de días da una tolerancia angular?

📘 **Dónde se aprende** (1 clase): [B75-C03 · Ventanas de lanzamiento](../programa/clases/B75/B75-C03-ventanas-de-lanzamiento/CLASE.md).

### Anchura del pulso

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C08):** La resolución de masa decide qué especies se separan. La decisión central: ¿qué tiempo de vuelo, qué dispersión y qué resolución permiten distinguir dos iones casi isobáricos?

📘 **Dónde se aprende** (1 clase): [B47-C08 · Espectrómetros de masas orbitales](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md).

### Ancla

- Gauss–Newton: iteración que linealiza y resuelve `H Δx = −b`. Ancla: pose fija que elimina la libertad de colocar el grafo en cualquier lugar.

💡 **Cómo se explica en la clase [B99-C03](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md):**
- Se fija la primera pose (ancla); sin ella `H` es singular, porque el coste no cambia al mover todo el grafo rígidamente.
- ⚠️ **Error frecuente:** Olvidar fijar una pose. Sin ancla `H` es singular (8.3).
- 🎯 **Por qué importa:** Sumar movimientos da una trayectoria que no cierra el lazo; una medida de cierre de bucle dice que la pose final es la inicial. La decisión central: ¿cómo repartir el desacuerdo entre cientos de poses de modo coherente con la incertidumbre de cada medida?

📘 **Dónde se aprende** (1 clase): [B99-C03 · SLAM basado en grafos de poses](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md).

### Anclaje

- Un anclaje es la distancia geométrica a la primera galaxia de la cadena.
- El cordón de seguridad ata a la persona a un anclaje; limita la distancia al anclaje.

💡 **Cómo se explica en la clase [B26-C12](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md):**
- A["Anclaje: LMC<br/>σ = 1,2 %"] --> B["Peldaño 2<br/>σ_μ = 0,03 mag → 1,38 %"]
- La distancia a la LMC se conoce con `1,2 %` por binarias eclipsantes; la incertidumbre total de la escalera pasó de `2,5 %` a `1,3 %`, y `H₀ = 74,22 ± 1,82 km/s/Mpc` con solo ese anclaje (S1, resumen), una precisión de `2,45 %`.
- 🎯 **Por qué importa:** Una distancia con un error de `2,6 %` produce un `H₀` con un error similar, y la discusión actual sobre `H₀` gira alrededor de esas décimas de punto porcentual. Entender cómo se acumulan los errores en una cadena de pasos evita confiar en una cifra más de lo debido.

📘 **Dónde se aprende** (2 clases): [B26-C12 · Escalas de distancia cosmológicas](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md); [B108-C02 · Planificación de desplazamientos y rutas de EVA](../programa/clases/B108/B108-C02-planificacion-de-desplazamientos-y-rutas-de-eva/CLASE.md).

### Anexado solo

- Cadena de hashes: cada entrada incluye el hash de la anterior. Anexado solo: no se editan entradas previas.

🎯 **Por qué importa (clase B96-C30):** Sin registro verificable no se puede reconstruir un incidente ni demostrar quién aprobó un comando. La decisión central: ¿cómo se registra para que una alteración se detecte y cuánto hay que revisar en una auditoría?

📘 **Dónde se aprende** (1 clase): [B96-C30 · Registro y auditoría de operaciones](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md).

### Angular

- Con pares solitarios aparecen la forma angular (como el agua) y la piramidal (como el amoníaco).

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- Con 4, la geometría electrónica es tetraédrica; si todos son enlaces, la forma también lo es (109,47°); si hay un par solitario, la forma es piramidal; si hay dos, angular.
- En el agua angular con 104,48°, la suma tiene módulo `2 cos(52,24°) = 1,2247` (en unidades del dipolo de enlace): molécula polar.
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).

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

📘 **Dónde se aprende** (7 clases): [B10-C06 · Producto interno y ortogonalidad](../programa/clases/B10/B10-C06-producto-interno-y-ortogonalidad/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md); [B30-C10 · Viento solar y heliosfera](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md); [B32-C01 · Ecuación de transferencia radiativa en atmósferas estelares](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md); [B40-C08 · Polarización E y B del fondo cósmico](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md); [B45-C15 · Polarización lineal y circular](../programa/clases/B45/B45-C15-polarizacion-lineal-y-circular/CLASE.md) y 1 más.

### Ángulo azimutal

- En matemáticas y física se usan el ángulo polar `θ` (desde el eje `z`, de 0° a 180°) y el ángulo azimutal `φ` (en el plano `xy` desde el eje `x`, de 0° a 360°).

🎯 **Por qué importa (clase B04-C11):** Un catálogo de estrellas da para cada una dos números: dónde está en el cielo. Pero un programa que cruza catálogos, calcula separaciones o apunta un telescopio no trabaja con horas y grados: trabaja con vectores.

📘 **Dónde se aprende** (1 clase): [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md).

### Ángulo beta

- El ángulo beta (β) fija su duración: `fracción = arccos(√(h²+2Rh)/((R+h)cos β))/π`, y es cero si el argumento es 1 o mayor.
- El ángulo beta `β` es el ángulo entre el Sol y el plano orbital.
- El ángulo beta del blanco respecto del plano.

🎯 **Por qué importa (clase B47-C17):** Sin planificación se desperdicia tiempo de observación. La decisión central: ¿qué blancos observar con un presupuesto de tiempo limitado y cuánto tiempo hay de visibilidad?

📘 **Dónde se aprende** (3 clases): [B47-C17 · Planificación de observaciones](../programa/clases/B47/B47-C17-planificacion-de-observaciones/CLASE.md); [B83-C10 · Presupuestos de energía](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md); [B86-C04 · Orientación solar y eclipses](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md).

### Ángulo causal

- El ángulo causal `η/χ`.

💡 **Cómo se explica en la clase [B40-C04](../programa/clases/B40/B40-C04-problemas-del-horizonte-y-de-la-planitud/CLASE.md):**
- Con `H₀ = 67,4` y `Ω_m = 0,315` (Planck 2018 VI, resumen), el horizonte comóvil en `z* = 1090` es `280,11 Mpc` y la distancia es `13 864,3 Mpc`: el ángulo causal es `1,158°`, unos `2450` parches desconectados.
- 🎯 **Por qué importa:** Regiones del fondo separadas más de un grado nunca se comunicaron en el modelo sin inflación, y la curvatura tendría que ser fantásticamente pequeña al principio. La decisión central: ¿qué tan grande es el problema, en números?

📘 **Dónde se aprende** (1 clase): [B40-C04 · Problemas del horizonte y de la planitud](../programa/clases/B40/B40-C04-problemas-del-horizonte-y-de-la-planitud/CLASE.md).

### Ángulo cenital

- El ángulo cenital `χ` es el ángulo del Sol con la vertical.
- El ángulo cenital `θ` es el que forma el Sol con la vertical: `tan θ = S/H`.

💡 **Cómo se explica en la clase [B30-C17](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md):**
- *Descripción textual:* la altura y el ángulo cenital dan la capa de Chapman; la energía de los electrones da los pares; la longitud de onda da la energía de los fotones; las conductancias dan la corriente y el calentamiento.
- 🎯 **Por qué importa:** La aurora y las corrientes ionosféricas son la parte visible y eléctrica del acoplamiento entre la magnetosfera y la atmósfera. La decisión central: ¿dónde se produce la ionización y cuánta energía se disipa por efecto Joule?

📘 **Dónde se aprende** (3 clases): [B30-C17 · Auroras y corrientes ionosféricas](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md); [B54-C10 · Fotoquímica atmosférica](../programa/clases/B54/B54-C10-fotoquimica-atmosferica/CLASE.md); [B131-C01 · Actividades de medición astronómica para el aula](../programa/clases/B131/B131-C01-actividades-de-medicion-astronomica-para-el-aula/CLASE.md).

### Ángulo central

- El ángulo central `λ` es el ángulo en el centro de la Tierra entre el sensor y el límite de visibilidad.
- El ángulo central `λ` entre la estación y el nadir del satélite cumple `tan ε = (cos λ − R/(R+h))/sin λ`.

💡 **Cómo se explica en la clase [B119-C13](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md):**
- A 550 km: período `95.65 min`, ángulo central `14.96°`, paso máximo `477 s` (`7.95 min`).
- 🎯 **Por qué importa:** El art. VI del Convenio de Registro prevé ayuda en la identificación mediante medios de rastreo; ninguna clase anterior muestra qué cubre un sensor ni cómo se criba un catálogo.

📘 **Dónde se aprende** (2 clases): [B89-C14 · Estaciones terrestres](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md); [B119-C13 · Vigilancia y conciencia situacional espacial](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md).

### Ángulo coorbital

- El ángulo coorbital `θ = λ_part − λ_Tierra` (sin envolver) distingue: tadpole (`θ` oscila alrededor de `±60°` sin cruzar `0` ni `π`), herradura (`θ` cubre `π` sin cruzar `0` ni `2π`) y cuasi-satélite (`θ` oscila alrededor de `0` con una amplitud pequeña y la partícula se mantiene a unos pocos `R_H`).

💡 **Cómo se explica en la clase [B73-C22](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md):**
- Descripción larga: tres comportamientos del ángulo coorbital en 200 años, con la constante de Jacobi intacta y una captura temporal que dura menos de un año con velocidad alta.
- 🎯 **Por qué importa:** Un asteroide puede acompañar a la Tierra durante siglos sin orbitarla: dando vueltas alrededor de L4 (tadpole), de L3–L4–L5 (herradura) o de la propia Tierra (cuasi-satélite); y puede ser capturado temporalmente dentro de su esfera de Hill. Distinguirlos requiere una clasificación operativa y una advertencia: no son satélites.

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

📘 **Dónde se aprende** (4 clases): [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md); [B41-C02 · Índice de refracción y ley de Snell](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md); [B47-C05 · Instrumentos de rayos X](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md); [B61-C03 · Cráteres complejos: colapso, picos centrales y terrazas](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md).

### Ángulo de anticipación

- El ángulo de anticipación (*point-ahead*) `α = v_⊥/c` es la diferencia entre la dirección a la posición actual del receptor y a la que tendrá cuando llegue la luz.

💡 **Cómo se explica en la clase [B92-C07](../programa/clases/B92/B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md):**
- *Descripción textual:* la distancia fija el tiempo de luz y la caída de la tasa; la velocidad transversal fija el ángulo de anticipación, que comparado con la divergencia decide la pérdida si no se aplica; las aperturas escalan la tasa.
- Descripción larga: la tasa cae con el cuadrado de la distancia y el tiempo de luz crece con ella; el ángulo de anticipación crece con la velocidad transversal y supera al ancho del haz por encima de unos 10 km/s.
- 🎯 **Por qué importa:** El espacio profundo exige otra forma de pensar: pocos fotones, latencia de minutos y apuntamiento predictivo. La decisión central: ¿cómo cambia la tasa con la distancia y qué hay que prever para que el haz llegue al receptor?

📘 **Dónde se aprende** (1 clase): [B92-C07 · Enlaces ópticos de espacio profundo](../programa/clases/B92/B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md).

### Ángulo de ataque

- El ángulo de ataque `α` es el que forman el eje del vehículo y la velocidad relativa al aire.

🎯 **Por qué importa (clase B77-C03):** El momento de mayor carga aerodinámica no es el de mayor velocidad ni el de menor altitud. La decisión central: ¿cuándo ocurre el máximo de la presión dinámica y qué fuerzas produce?

📘 **Dónde se aprende** (1 clase): [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md).

### Ángulo de avance

- El ángulo de avance `λ = atan(L/(π d))`.

💡 **Cómo se explica en la clase [B43-C14](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md):**
- *Descripción textual:* el ángulo de avance y la fricción fijan el rendimiento y el autobloqueo; la relación y la rigidez fijan la resolución y la resonancia.
- El ángulo de avance es `2,734°` frente a `φ = 5,711°` (`μ = 0,1`): hay autobloqueo y el rendimiento es `0,3216`.
- 🎯 **Por qué importa:** El reductor fija la resolución, la fuerza disponible y el comportamiento dinámico. La decisión central: ¿qué relación, qué rendimiento y qué rigidez permiten apuntar con la resolución pedida sin resonancias?

📘 **Dónde se aprende** (1 clase): [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md).

### Ángulo de Brewster

- El ángulo de Brewster `atan(n₂/n₁)`.

💡 **Cómo se explica en la clase [B41-C02](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md):**
- El ángulo de Brewster es `56,5994°` con `Rp = 4 × 10⁻³³` y `Rs = 0,15518`.
- Para aire (`1,0003`) a vidrio (`1,517`), la reflectancia en incidencia normal es `0,042132`, el ángulo de Brewster es `56,5994°` (donde `Rp = 0`) y de vidrio a aire el ángulo crítico es `41,2536°`.
- 🎯 **Por qué importa:** Un telescopio refractor y los recubrimientos dependen de cuánta luz se refleja y a qué ángulo se dobla. La decisión central: ¿qué fracción de luz se pierde por reflexión y cuándo hay reflexión total?

📘 **Dónde se aprende** (1 clase): [B41-C02 · Índice de refracción y ley de Snell](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md).

### Ángulo de Cherenkov

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B31-C14):** Interpretar una señal exige saber qué partículas la producen y con qué precisión se mide su energía. La decisión central: ¿qué umbral y qué resolución tiene un detector?

📘 **Dónde se aprende** (1 clase): [B31-C14 · Detectores de partículas](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md).

### Ángulo de contacto

- El ángulo de contacto `θ₀ = arccos(1 − z₀/R)` fija el arco en que la rueda toca el suelo.

🎯 **Por qué importa (clase B102-C02):** La tracción de un rover en regolito no sale de un coeficiente de rozamiento único. La decisión central: ¿cuánta fuerza neta de empuje queda para tirar del vehículo, una vez descontada la resistencia que crea el propio hundimiento, y cómo depende del patinaje y de la gravedad?

📘 **Dónde se aprende** (1 clase): [B102-C02 · Terramecánica: tracción y hundimiento en suelos sueltos](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md).

### Ángulo de desviación

- El ángulo de desviación de un rayo que pasa a distancia `b` de una masa puntual `M` es, en campo débil, `4GM/(c²b)` (dato de la relatividad general, B26).

🎯 **Por qué importa (clase B25-C14):** La luz de una galaxia lejana se curva al pasar cerca de una masa, y la masa interior se deduce del tamaño de la distorsión sin importar si es luminosa u oscura ni si está en equilibrio. Por eso las lentes son una prueba directa de la distribución de masa.

📘 **Dónde se aprende** (1 clase): [B25-C14 · Lentes gravitacionales galácticas](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md).

### Ángulo de entrada

- El ángulo de entrada `γ_E` se mide bajo el horizonte.

💡 **Cómo se explica en la clase [B77-C14](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md):**
- Con ángulo de entrada de `5°` la desaceleración máxima es `11,70 g` tanto con `β = 100` como con `1000 kg/m²` (la integración da `11,71` y `11,70 g`), pero el pico ocurre a `60,2 km` en el primero y a `40,6 km` en el segundo.
- Descripción larga: la desaceleración máxima crece con el seno del ángulo de entrada y no depende del coeficiente balístico; este solo mueve la altitud del pico.
- 🎯 **Por qué importa:** La desaceleración máxima fija la carga sobre la carga útil y sobre la tripulación. La decisión central: ¿qué ángulo de entrada limita la desaceleración y de qué propiedades del vehículo no depende?

📘 **Dónde se aprende** (1 clase): [B77-C14 · Dinámica de reentrada](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md).

### Ángulo de equilibrio

- El ángulo de equilibrio (trim) es donde `Cm = 0`.

💡 **Cómo se explica en la clase [B77-C17](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md):**
- *Descripción textual:* el momento de cabeceo da el ángulo de equilibrio y la frecuencia natural;
- 🎯 **Por qué importa:** Una cápsula inestable no entra con el escudo hacia delante. La decisión central: ¿qué pendiente de momento da una oscilación acotada y cuánto tarda en divergir una inestable?

📘 **Dónde se aprende** (1 clase): [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md).

### Ángulo de fase

- El ángulo de fase `i` es el ángulo Sol–Luna–Tierra visto desde la Luna.
- El ángulo de fase es el que debe separar a los cuerpos al salir.
- El ángulo de fase `φ` es la posición angular del objetivo menos la del perseguidor.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C08](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md):**
- La diferencia se debe a que el Sol está a una distancia finita: el ángulo de fase exacto es `tan i = R sen ψ / (d − R cos ψ)`, con `R` la distancia al Sol y `d` la de la Luna.
- 🎯 **Por qué importa:** La Luna es el primer blanco de cualquier observación y el principal enemigo de las observaciones de objetos débiles (C12). Saber su fase y cuándo está en el cielo es parte de toda planificación.

📘 **Dónde se aprende** (5 clases): [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md); [B71-C18 · Maniobra de Hohmann](../programa/clases/B71/B71-C18-maniobra-de-hohmann/CLASE.md); [B76-C10 · Encuentro orbital](../programa/clases/B76/B76-C10-encuentro-orbital/CLASE.md); [B118-C03 · Detección y seguimiento óptico](../programa/clases/B118/B118-C03-deteccion-y-seguimiento-optico/CLASE.md); [B131-C05 · Demostraciones visuales y modelos para el aula](../programa/clases/B131/B131-C05-demostraciones-visuales-y-modelos-para-el-aula/CLASE.md).

### Ángulo de fase de salida

- El ángulo de fase de salida `φ` es la diferencia de longitud heliocéntrica destino − Tierra al partir.

🎯 **Por qué importa (clase B75-C02):** Una nave que llega al afelio de su elipse debe encontrar allí al planeta. Como el planeta se mueve mientras la nave vuela, hay que salir cuando el destino va por delante (o por detrás) un ángulo preciso.

📘 **Dónde se aprende** (1 clase): [B75-C02 · Ángulos de fase planetaria](../programa/clases/B75/B75-C02-angulos-de-fase-planetaria/CLASE.md).

### Ángulo de fricción

- La cohesión `c` es la resistencia al corte sin carga y `φ` el ángulo de fricción.
- El ángulo de fricción `φ = atan μ`.

🎯 **Por qué importa (clase B43-C14):** El reductor fija la resolución, la fuerza disponible y el comportamiento dinámico. La decisión central: ¿qué relación, qué rendimiento y qué rigidez permiten apuntar con la resolución pedida sin resonancias?

📘 **Dónde se aprende** (2 clases): [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md); [B97-C06 · Control de movilidad sobre regolito](../programa/clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md).

### Ángulo de giro

- El ángulo de giro `δ` es la desviación entre las direcciones de llegada y salida.
- El ángulo de giro `δ` es lo que se desvía `v∞`.

🎯 **Por qué importa (clase B71-C09):** Las trayectorias de escape y de sobrevuelo son hipérbolas respecto del cuerpo local. La decisión central: ¿qué velocidad en el periapsis produce un exceso `v∞` dado y cuánto se desvía la trayectoria?

📘 **Dónde se aprende** (2 clases): [B71-C09 · Órbitas parabólicas e hiperbólicas](../programa/clases/B71/B71-C09-orbitas-parabolicas-e-hiperbolicas/CLASE.md); [B75-C06 · Asistencias gravitacionales](../programa/clases/B75/B75-C06-asistencias-gravitacionales/CLASE.md).

### Ángulo de incidencia

- El ángulo de incidencia `α` entre la normal y el Sol reduce la fuerza como `cos²α` para una vela ideal.

🎯 **Por qué importa (clase B78-C12):** La vela no gasta propelente, pero su empuje es del orden de los micronewton por metro cuadrado y cae con el cuadrado de la distancia al Sol. La decisión central: ¿cuánta aceleración da una vela real y cómo depende de su orientación y de su distancia?

📘 **Dónde se aprende** (1 clase): [B78-C12 · Velas solares](../programa/clases/B78/B78-C12-velas-solares/CLASE.md).

### Ángulo de inclinación

- El ángulo de inclinación es el del eje mayor respecto del eje de referencia.

🎯 **Por qué importa (clase B91-C02):** Un enlace pierde potencia si las polarizaciones no coinciden, y puede perderla toda si son ortogonales. La decisión central: ¿qué polarización y qué razón axial exigir a las dos antenas para que la desadaptación quede por debajo del margen del enlace?

📘 **Dónde se aprende** (1 clase): [B91-C02 · Polarización de antenas y pérdidas por desadaptación](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md).

### Ángulo de la regla

- El ángulo de la regla es `θ = r_BAO/D_C`.

🎯 **Por qué importa (clase B26-C17):** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.

📘 **Dónde se aprende** (1 clase): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md).

### Ángulo de la trayectoria

- El ángulo de la trayectoria `γ` se mide sobre el horizonte local.

🎯 **Por qué importa (clase B77-C12):** La trayectoria de ascenso decide a la vez las pérdidas, las cargas y la órbita alcanzada. La decisión central: ¿qué perfil de inclinación lleva al vehículo a una órbita casi circular y qué cuesta?

📘 **Dónde se aprende** (1 clase): [B77-C12 · Perfil de ascenso orbital](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md).

### Ángulo de Mach

- El ángulo de Mach es `μ = arcsin(1/M)`.

💡 **Cómo se explica en la clase [B79-C06](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md):**
- *Descripción textual:* el Mach supersónico determina la relación de áreas, el ángulo de Mach y la función de Prandtl–Meyer; las dos relaciones se verifican con integrales numéricas.
- Una tobera con `A/A* = 5` produce `M = 3,17478` con ángulo de Mach `18,36°`.
- 🎯 **Por qué importa:** El comportamiento de un flujo a `M > 1` en toberas y vehículos no lo trata ninguna clase del tronco. Sin él no se entiende por qué una tobera necesita una parte divergente.

📘 **Dónde se aprende** (1 clase): [B79-C06 · Flujos supersónicos](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md).

### Ángulo de mezcla

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B31-C11):** Detectar neutrinos del Sol, la atmósfera y aceleradores exige saber cuánto oscilan. La decisión central: ¿cuál es la probabilidad de oscilación a cierta distancia y energía?

📘 **Dónde se aprende** (1 clase): [B31-C11 · Neutrinos y oscilaciones](../programa/clases/B31/B31-C11-neutrinos-y-oscilaciones/CLASE.md).

### Ángulo de paso

- El ángulo de paso `ψ` es el ángulo entre la tangente al brazo y la tangente al círculo que pasa por ese punto: `ψ = 0` es un círculo y `ψ = 90°` un rayo.

💡 **Cómo se explica en la clase [B25-C02](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md):**
- Si `R = R_k e^{−(β−β_k) tan ψ}`, entonces `dR/dβ = −R tan ψ`: la razón entre el avance radial y el avance a lo largo del círculo vale `tan ψ` en todos los puntos, lo que fija un ángulo de paso constante.
- El ángulo de paso medio de los brazos mayores es de unos `10°`.
- 🎯 **Por qué importa:** Los brazos espirales son lo más llamativo de una galaxia de disco, pero la rotación diferencial debería enrollarlos hasta borrarlos en unas pocas vueltas. Entender esa paradoja es entender qué es un brazo: no un montón fijo de materia, sino un patrón.

📘 **Dónde se aprende** (1 clase): [B25-C02 · Brazos espirales y barra galáctica](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md).

### Ángulo de paso ecuatorial

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B30-C16):** Las partículas con ángulo de paso pequeño se pierden en la atmósfera; las demás quedan atrapadas y dañan satélites. La decisión central: ¿qué partículas quedan atrapadas y con qué periodo rebotan?

📘 **Dónde se aprende** (1 clase): [B30-C16 · Cinturones de Van Allen](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md).

### Ángulo de rotación

- El ángulo de rotación `θ` es positivo en sentido antihorario visto desde el extremo positivo del eje (regla de la mano derecha).

🎯 **Por qué importa (clase B10-C12):** La Tierra gira una vuelta cada 23,93 horas: una estación de seguimiento ve pasar los satélites porque sus ejes locales rotan respecto del espacio inercial. Un satélite recibe órdenes expresadas en ejes terrestres y debe saber dónde están en ejes inerciales.

📘 **Dónde se aprende** (1 clase): [B10-C12 · Rotaciones en el plano y espacio](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md).

### Ángulo de rotación terrestre

- El ángulo de rotación terrestre (ERA) es el ángulo de `R`, y se define por `ERA(Tu) = 2π(0,7790572732640 + 1,00273781191135448 Tu)` con `Tu = (fecha juliana UT1 − 2451545,0)` (S1, ec. 5.14).

🎯 **Por qué importa (clase B10-C16):** Una estación terrestre tiene coordenadas fijas en la Tierra. Un satélite se propaga en un sistema inercial, donde las leyes de Newton valen.

📘 **Dónde se aprende** (1 clase): [B10-C16 · Transformación de marcos de referencia](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md).

### Ángulo de rotación terrestre (ERA)

- El ángulo de rotación terrestre (ERA) es el ángulo entre un origen celeste de referencia y un origen terrestre, que describe la rotación de la Tierra en torno a su eje; la convención IERS lo define como una función lineal de `UT1` (S1, ec. 5.14).

🎯 **Por qué importa (clase B13-C10):** Un telescopio en el desierto debe saber cuándo un objeto pasa por su meridiano, que es cuando está más alto y se observa mejor. Esa hora no es la del reloj civil: el cielo se adelanta casi cuatro minutos cada día.

📘 **Dónde se aprende** (1 clase): [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md).

### Ángulo de salida

- El ángulo de salida `θ` es la posición de partida en la órbita baja.

🎯 **Por qué importa (clase B76-C08):** Una transferencia de baja energía promete ahorrar propergol a cambio de tiempo, pero ¿qué ahorra y qué no? La decisión central: ¿qué energía hace falta para que una trayectoria pueda pasar por los cuellos de `L1` y `L2`, y qué no explica un modelo sin el Sol?

📘 **Dónde se aprende** (1 clase): [B76-C08 · Transferencias de baja energía](../programa/clases/B76/B76-C08-transferencias-de-baja-energia/CLASE.md).

### Ángulo de transferencia

- El ángulo de transferencia `Δθ` es el que forman `r₁` y `r₂`.

🎯 **Por qué importa (clase B75-C04):** Con ventanas fijas solo se calcula el caso ideal. Para cualquier fecha de salida y llegada hace falta resolver la geometría entre dos posiciones.

📘 **Dónde se aprende** (1 clase): [B75-C04 · Ecuación de Lambert](../programa/clases/B75/B75-C04-ecuacion-de-lambert/CLASE.md).

### Ángulo de trayectoria

- El ángulo de trayectoria `γ` es la inclinación de la entrada.
- El ángulo de trayectoria `γ` es el ángulo bajo el horizonte local.

🎯 **Por qué importa (clase B104-C19):** Un ángulo de entrada más empinado reduce el calentamiento total pero aumenta la desaceleración. La decisión central: ¿cuántos g máximos soporta la tripulación según el ángulo de entrada, y por qué ese máximo no depende de la masa de la nave?

📘 **Dónde se aprende** (2 clases): [B104-C19 · Operaciones de retorno y reintegración](../programa/clases/B104/B104-C19-operaciones-de-retorno-y-reintegracion/CLASE.md); [B118-C13 · Desorbitación controlada](../programa/clases/B118/B118-C13-desorbitacion-controlada/CLASE.md).

### Ángulo de triangulación

- Tamaño de pixel en el objeto (GSD): `2 d tan(θ)/N`. Ángulo de triangulación: ángulo entre las líneas de vista de dos cámaras.

🎯 **Por qué importa (clase B101-C09):** Si el operador no ve el punto de contacto, depende de la imaginación. La decisión central: ¿qué cámaras necesito y dónde para que la zona de trabajo se vea, con qué resolución y sin puntos ciegos críticos?

📘 **Dónde se aprende** (1 clase): [B101-C09 · Coordinación visual y cámaras en operaciones con manipulador](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md).

### Ángulo de visión

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B28-C12](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md):**
- Esta clase no ajusta ninguna observación: con `Γ = 100`, `θ_c = 0,1 rad` y exponente Doppler `3` (ilustrativos) calcula cómo cae el brillo con el ángulo de visión.
- 🎯 **Por qué importa:** Un destello gamma débil puede ser un evento normal visto de lado. Un modelo de emisión conjunta permite relacionar qué se ve en cada mensajero con el ángulo de visión.

📘 **Dónde se aprende** (1 clase): [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md).

### Ángulo entre planos

- El ángulo entre planos al cambiar `Ω` es `θ` con `cos θ = cos² i + sin² i cos ΔΩ`.

💡 **Cómo se explica en la clase [B71-C19](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md):**
- Con `i = 51,6°` (ilustrativa) y `ΔΩ = 10°`, el ángulo entre planos es `θ = 7.8331°`, a pesar de que `ΔΩ = 10°`.
- 🎯 **Por qué importa:** Un cambio de plano mal ubicado puede costar más que todo el resto de la misión orbital. La decisión central: ¿dónde y cómo conviene cambiar el plano para gastar el mínimo `Δv`?

📘 **Dónde se aprende** (1 clase): [B71-C19 · Cambios de plano simples](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md).

### Ángulo entre vectores

- Geométricamente `u · v = |u||v| cos γ`, donde `γ` es el ángulo entre vectores (entre 0° y 180°).

🎯 **Por qué importa (clase B04-C13):** Antes de apuntar un telescopio de una estrella a otra, antes de saber si dos objetos caben en el mismo campo de visión, antes de decidir si un planeta está demasiado cerca del Sol para observarlo, hay que saber cuántos grados los separan en el cielo.

📘 **Dónde se aprende** (1 clase): [B04-C13 · Producto escalar y ángulo entre vectores](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md).

### Ángulo espectral

- El ángulo espectral (SAM) es el ángulo entre dos espectros vistos como vectores; no cambia si un espectro se multiplica por un factor.

💡 **Cómo se explica en la clase [B57-C22](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md):**
- El ángulo espectral entre arcilla y hematita es `9,78°`, entre arcilla y vegetación `19,92°` y entre hematita y vegetación `14,52°`.
- 🎯 **Por qué importa:** Dos materiales distintos pueden parecer iguales en cuatro bandas anchas y diferenciarse en cientos de bandas estrechas. La decisión central: ¿cuándo vale la pena el costo en datos de un sensor hiperespectral y cómo se separa una mezcla de materiales?

📘 **Dónde se aprende** (1 clase): [B57-C22 · Espectrómetros de imagen e hiperespectrales](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md).

### Ángulo espectral (SAM)

- El ángulo espectral (SAM) es `arccos(u·v/(|u||v|))`.

🎯 **Por qué importa (clase B53-C29):** Un píxel gris puede ser una mezcla de tres minerales. La decisión central: ¿qué abundancias explican el espectro de un píxel y con qué error, dado el ruido y la similitud entre miembros extremos?

📘 **Dónde se aprende** (1 clase): [B53-C29 · Imágenes hiperespectrales de superficies planetarias](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md).

### Ángulo heliocéntrico

- El ángulo heliocéntrico es el ángulo entre las direcciones al Sol de dos planetas medido desde el Sol.

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- Si dibujas las órbitas como circunferencias con el Sol en el centro, la Tierra y Marte son dos puntos y el Sol el tercero: un triángulo con dos lados conocidos (149,6 y 228,0) y el ángulo entre ellos (el ángulo heliocéntrico `φ`).
- ⚠️ **Error frecuente:** Confundir la elongación con el ángulo heliocéntrico. Se corrige con el ejercicio 3 y la sección 6.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

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

📘 **Dónde se aprende** (7 clases): [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md); [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B46-C14 · Líneas de base interferométricas](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md); [B48-C04 · Planificación por visibilidad](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md) y 1 más.

### Ángulo isoplanático

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B42-C18):** Una sola corrección solo vale dentro del ángulo isoplanático (unos segundos de arco). La decisión central: ¿cómo se amplía el campo y qué parte de la turbulencia queda sin restricción?

📘 **Dónde se aprende** (1 clase): [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### Ángulo paralactico

- La rotación de campo es el giro de la imagen respecto del horizonte; es el ángulo paraláctico `q`.

💡 **Cómo se explica en la clase [B41-C18](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md):**
- Paso 3 · Comprobación. La derivada numérica del ángulo paralactico da `24,4448 "/s` (módulo).
- 🎯 **Por qué importa:** La montura decide cuánto tiempo se puede exponer. La decisión central: ¿altazimutal o ecuatorial y qué exposición máxima sin guiado?

📘 **Dónde se aprende** (2 clases): [B41-C18 · Monturas y mecanismos de seguimiento](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md); [B43-C13 · Montura altacimutal](../programa/clases/B43/B43-C13-montura-altacimutal/CLASE.md).

### Ángulo polar

- En matemáticas y física se usan el ángulo polar `θ` (desde el eje `z`, de 0° a 180°) y el ángulo azimutal `φ` (en el plano `xy` desde el eje `x`, de 0° a 360°).

💡 **Cómo se explica en la clase [B04-C11](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md):**
- Ángulo polar y azimut: convención matemática; exige no confundir `θ` con `δ`.
- 🎯 **Por qué importa:** Un catálogo de estrellas da para cada una dos números: dónde está en el cielo. Pero un programa que cruza catálogos, calcula separaciones o apunta un telescopio no trabaja con horas y grados: trabaja con vectores.

📘 **Dónde se aprende** (1 clase): [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md).

### Ángulo resonante

- El ángulo resonante `φ` libra alrededor de un valor en la resonancia.

💡 **Cómo se explica en la clase [B72-C11](../programa/clases/B72/B72-C11-resonancias-orbitales-perturbaciones-y-evolucion-de-orbitas/CLASE.md):**
- Para mostrarlo en un sistema real hay que calcular el ángulo resonante con elementos medidos; el laboratorio solo prueba la combinación de movimientos medios.
- Límite: el péndulo es un modelo de una sola resonancia aislada; las resonancias reales se solapan y su ángulo resonante exige elementos que no se calculan aquí.
- 🎯 **Por qué importa:** Una resonancia mantiene a los satélites de Júpiter en equilibrio dinámico y obliga a gestionar un satélite geoestacionario, que se desplaza hacia dos puntos de equilibrio por el campo no esférico.

📘 **Dónde se aprende** (1 clase): [B72-C11 · Resonancias orbitales — Perturbaciones y evolución de órbitas](../programa/clases/B72/B72-C11-resonancias-orbitales-perturbaciones-y-evolucion-de-orbitas/CLASE.md).

### Ángulo sólido

- El ángulo sólido mide la extensión de cielo.
- El ángulo sólido del cono.

🎯 **Por qué importa (clase B41-C10):** La relación focal decide si un telescopio es «rápido» o «lento». La decisión central: ¿qué importa más, el diámetro o la relación focal?

📘 **Dónde se aprende** (2 clases): [B41-C10 · Apertura y relación focal](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md); [B118-C16 · Contaminación lumínica](../programa/clases/B118/B118-C16-contaminacion-luminica/CLASE.md).

### Ángulo sólido del haz

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B46-C05):** Para saber cuánto flujo hay en una fuente hay que conocer cuánta fracción del haz llena. La decisión central: ¿cuánto vale la temperatura de antena de una fuente extensa en un haz dado?

📘 **Dónde se aprende** (1 clase): [B46-C05 · Ganancia y temperatura de antena](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md).

### Ángulos de Euler

- Los ángulos de Euler son tres rotaciones sucesivas alrededor de ejes del cuerpo (o fijos) que componen una orientación.

💡 **Cómo se explica en la clase [B10-C14](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md):**
- Paso 5 · Sentido. La singularidad está en la representación, no en el satélite: el movimiento es suave, pero los ángulos de Euler no pueden seguirlo.
- Ángulos de Euler: intuitivos, singulares.
- 🎯 **Por qué importa:** Un satélite que apunta una antena al cenit tiene el cabeceo cerca de `90°`; si la actitud se guarda con ángulos de Euler, justo ahí el cálculo se vuelve inestable: ángulos que cambian muy rápido para movimientos pequeños, o dos conjuntos de ángulos distintos para la misma orientación.

📘 **Dónde se aprende** (1 clase): [B10-C14 · Ángulos de Euler y singularidades](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md).

### Ángulos de Euler 3-2-1

- Los ángulos de Euler 3-2-1 son *yaw* (eje z), *pitch* (eje y) y *roll* (eje x): `A = Rx(roll) Ry(pitch) Rz(yaw)`.

🎯 **Por qué importa (clase B87-C02):** Casi todos los errores de actitud en software vienen de convenciones mezcladas: orden de ejes, sentido de la rotación, posición de la parte escalar. La decisión central: ¿qué representación uso para integrar, cuál para filtrar y cuál para mostrar?

📘 **Dónde se aprende** (1 clase): [B87-C02 · Representaciones de orientación](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md).

### Anidamiento

- El anidamiento deja que una prioridad mayor interrumpa a una menor.

💡 **Cómo se explica en la clase [B88-C22](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md):**
- Q -->|si| P{"Prioridad mayor y anidamiento?"}
- Con anidamiento, la pila máxima es `80 B` y la UART termina a 220 µs; sin anidar, `48 B`, pero TIMER2 espera 40 µs.
- 🎯 **Por qué importa:** Las interrupciones fijan cuánto tarda el sistema en reaccionar y cuánta pila usa. La decisión central: ¿se permite que una interrupción de mayor prioridad interrumpa a otra, y qué cuesta eso en latencia y pila?

📘 **Dónde se aprende** (1 clase): [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md).

### Anillo

- El anillo es el conjunto de direcciones con la misma diferencia de tiempo.
- Un anillo es un disco delgado de partículas.
- La malla completa tiene `n(n−1)/2` enlaces; el anillo, `n`; la estrella, `n − 1`.

💡 **Cómo se explica en la clase [B28-C10](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md):**
- Con dos detectores la fuente está sobre un anillo ancho; un tercero añade otro anillo y la intersección reduce el área a dos manchas simétricas respecto del plano de los detectores.
- 🎯 **Por qué importa:** El área de localización decide cuántas fotos hacen falta para encontrar la contrapartida. Un mapa mal calibrado engaña.

📘 **Dónde se aprende** (3 clases): [B28-C10 · Localización probabilística de eventos](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md); [B52-C12 · Anillos planetarios](../programa/clases/B52/B52-C12-anillos-planetarios/CLASE.md); [B88-C31 · Topologías de red de datos a bordo](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md).

### Anillo atmosférico

- El anillo atmosférico tiene espesor `NH`.

🎯 **Por qué importa (clase B29-C11):** Los planetas inflados y calientes tienen señales de cientos de ppm; las Tierras alrededor de estrellas como el Sol, de ~1 ppm, que no se alcanzan. La decisión central: ¿qué señal produce una atmósfera dada y cuántos tránsitos hacen falta para verla?

📘 **Dónde se aprende** (1 clase): [B29-C11 · Atmósferas exoplanetarias](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md).

### Anillo de apoyo

- El anillo de apoyo de radio `b`.

🎯 **Por qué importa (clase B43-C08):** Un apoyo mal elegido deja un error de forma que ninguna pieza posterior corrige. La decisión central: ¿en qué radio conviene apoyar el espejo para que, tras quitar piston y desenfoque, quede el menor error?

📘 **Dónde se aprende** (1 clase): [B43-C08 · Montaje de espejo primario](../programa/clases/B43/B43-C08-montaje-de-espejo-primario/CLASE.md).

### Anillo de cielo

- El anillo de cielo da el fondo.

💡 **Cómo se explica en la clase [B45-C23](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md):**
- El anillo de cielo (12 a 19 píxeles) tiene 692 píxeles.
- A["anillo de cielo"] --> C["cielo (mediana)"]
- 🎯 **Por qué importa:** Una apertura pequeña pierde flujo y una grande añade ruido de cielo. La decisión central: ¿qué radio da el mejor S/N y cómo se mide el cielo?

📘 **Dónde se aprende** (1 clase): [B45-C23 · Fotometría de apertura y estimación del cielo](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md).

### Anillo de eventos

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C06):** Cada proceso (Compton, pares) domina a una energía distinta y fija el tipo de instrumento. La decisión central: ¿qué proceso usa el detector y con qué incertidumbre angular reconstruye la dirección?

📘 **Dónde se aprende** (1 clase): [B47-C06 · Instrumentos de rayos gamma](../programa/clases/B47/B47-C06-instrumentos-de-rayos-gamma/CLASE.md).

### Anillo de fondo

- Una apertura es el conjunto de píxeles que se suman para medir una estrella y un anillo de fondo el conjunto alrededor que estima el cielo.

🎯 **Por qué importa (clase B15-C09):** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.

📘 **Dónde se aprende** (1 clase): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md).

### Anillo E

- El anillo E es el anillo de Saturno formado por material del penacho.

💡 **Cómo se explica en la clase [B56-C10](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md):**
- C -- "no" --> E["Escapa:<br/>alimenta el anillo E"]
- Modelo con gas, rotación y Saturno: necesario para predecir el anillo E.
- 🎯 **Por qué importa:** El penacho permite muestrear un océano sin aterrizar. Para diseñar un sobrevuelo hace falta saber hasta dónde llegan los granos y cuáles escapan al anillo E.

📘 **Dónde se aprende** (1 clase): [B56-C10 · Océanos de Encélado](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md).

### Anión

- Un ion es un átomo o grupo con carga neta: un catión (positivo) pierde electrones; un anión (negativo) los gana.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- Pregunta: un par catión +1 / anión −1 a 0,30 nm (distancia sintética), ¿resiste la agitación térmica a 176 K, la temperatura del eutéctico NH₃–H₂O (S1)?
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Aniquilación

- La aniquilación electrón–positrón convierte sus masas en fotones.
- La aniquilación convierte materia y antimateria en radiación.
- La aniquilación `e⁺e⁻ → γγ`.

💡 **Cómo se explica en la clase [B31-C12](../programa/clases/B31/B31-C12-antimateria-y-aniquilacion/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir aniquilación y producción. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Producir antimateria o partículas pesadas requiere una energía mínima que depende de la configuración. La decisión central: ¿cuál es la energía umbral de una reacción y por qué un colisionador ahorra energía?

📘 **Dónde se aprende** (3 clases): [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md); [B31-C12 · Antimateria y aniquilación](../programa/clases/B31/B31-C12-antimateria-y-aniquilacion/CLASE.md); [B40-C03 · Desacoplamiento de neutrinos y fondo cósmico de neutrinos](../programa/clases/B40/B40-C03-desacoplamiento-de-neutrinos-y-fondo-cosmico-de-neutrinos/CLASE.md).

### Anisoplanatismo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C18](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md):**
- *Descripción textual:* el anisoplanatismo crece como `(θ/θ₀)^{5/3}`; la MCAO lo reduce hasta que la huella queda fuera de las guías.
- 🎯 **Por qué importa:** Una sola corrección solo vale dentro del ángulo isoplanático (unos segundos de arco). La decisión central: ¿cómo se amplía el campo y qué parte de la turbulencia queda sin restricción?

📘 **Dónde se aprende** (1 clase): [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### Anisotropía

- La anisotropía es su pequeña variación de temperatura, del orden de `10⁻⁵`.

🎯 **Por qué importa (clase B26-C15):** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.

📘 **Dónde se aprende** (1 clase): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### Anodizado

- El anodizado genera óxido: `espesor = η j t M_ox/(3Fρ_ox)`.

💡 **Cómo se explica en la clase [B84-C34](../programa/clases/B84/B84-C34-tratamientos-y-recubrimientos-superficiales-de-componentes-espaciales/CLASE.md):**
- *Descripción textual:* `α`, `ε` y `S` dan la temperatura de equilibrio, comprobada con el balance; la degradación la desplaza; el anodizado se calcula aparte con Faraday.
- Una placa con la cara al Sol (`S = 1361 W/m²`, ilustrativo) alcanza `14,2 °C` con pintura blanca (`α/ε = 0,284`), `125,8 °C` con pintura negra, `283,5 °C` con aluminio pulido, `47,0 °C` con aluminio anodizado, `426,8 °C` con oro y `−51,8 °C` con un reflector solar óptico.
- 🎯 **Por qué importa:** Cambiar el recubrimiento de una placa de aluminio cambia su temperatura de equilibrio en 400 K; la degradación en órbita lo desplaza decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la temperatura de una superficie en su rango y qué espesor de anodizado se necesita?

📘 **Dónde se aprende** (1 clase): [B84-C34 · Tratamientos y recubrimientos superficiales de componentes espaciales](../programa/clases/B84/B84-C34-tratamientos-y-recubrimientos-superficiales-de-componentes-espaciales/CLASE.md).

### Anomalía

- Una anomalía es una observación que no se parece a lo esperado según un modelo de lo normal.
- Anomalía: desvío de lo esperado.
- Una anomalía pierde el día.

💡 **Cómo se explica en la clase [B96-C13](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md):**
- *Descripción textual:* la misma serie con anomalías inyectadas pasa por tres detectores; cada uno se evalúa por sus falsas alarmas y su latencia en cada anomalía.
- ⚠️ **Error frecuente:** Elegir el detector por la tasa de aciertos de un solo tipo. Prueba varios tipos de anomalía (8.4)
- 🎯 **Por qué importa:** Un detector que no ve una deriva lenta avisa cuando ya es tarde, y uno que alarma por todo se ignora. La decisión central: ¿qué detector ve cada tipo de anomalía, con qué retraso y a qué costo en falsas alarmas?

📖 **Explicado a fondo:** [Anomalía y ecuación de Kepler](esencial/tercera-a-e.md#anomalía-y-ecuación-de-kepler) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md); [B96-C13 · Detección de anomalías](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md); [B97-C20 · Misión robótica integrada simulada](../programa/clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md).

### Anomalía de altura

- La anomalía de altura `η` es la altura respecto de una referencia.

🎯 **Por qué importa (clase B57-C12):** El océano se mueve lento y se eleva más lento aún. La decisión central: ¿qué pendiente de la superficie equivale a una corriente y cuántos años de datos se necesitan para ver una tendencia de pocos milímetros por año entre un ruido de centímetros?

📘 **Dónde se aprende** (1 clase): [B57-C12 · Oceanografía desde órbita](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md).

### Anomalía estandarizada

- La anomalía estandarizada `z = (x − μ)/σ` mide cuántas desviaciones se aleja un valor del promedio.

💡 **Cómo se explica en la clase [B57-C15](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md):**
- La anomalía estandarizada supone distribución normal, que no vale para lluvias muy sesgadas.
- 🎯 **Por qué importa:** Las agencias necesitan mapas de inundación en horas y alertas de sequía en meses. La decisión central: ¿cómo se fija el umbral entre agua y tierra sin fijarlo a ojo, y cómo se declara que un año es seco?

📘 **Dónde se aprende** (1 clase): [B57-C15 · Sequías e inundaciones](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md).

### Anomalía excéntrica

- La anomalía excéntrica `E` es un ángulo auxiliar que cumple la ecuación de Kepler, `M = E − e sen E`.
- La anomalía excéntrica `E` es un ángulo auxiliar que sitúa al planeta en la elipse.
- La anomalía excéntrica `E` y la media `M = E − e sin E`.

💡 **Cómo se explica en la clase [B02-C14](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md):**
- *Descripción textual:* con `a`, `e` y `T` se calcula la anomalía media en cada instante; se resuelve la ecuación de Kepler para hallar la anomalía excéntrica; de ella salen las coordenadas; y se comprueban las leyes de las áreas y del período.
- 🎯 **Por qué importa:** Para Kepler, como para todos antes, el círculo era la figura natural del cielo. Los datos de Tycho no se dejaban describir con círculos.

📘 **Dónde se aprende** (3 clases): [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B71-C14 · Ecuación de Kepler](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md).

### Anomalía magnética

- Una anomalía magnética es la diferencia entre el campo observado y el campo de referencia.

🎯 **Por qué importa (clase B65-C03):** La corteza magnetizada permite reconstruir campos de cuerpos que hoy no tienen dinamo. La decisión central: ¿qué parte de un mapa de anomalías es información sobre la magnetización y qué parte es ambigüedad geométrica?

📘 **Dónde se aprende** (1 clase): [B65-C03 · Magnetismo cortical remanente y anomalías magnéticas](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md).

### Anomalía media

- La anomalía media `M = 2π t/T` crece de manera uniforme con el tiempo.
- La anomalía media `M` crece uniformemente con el tiempo, `M = n t`, con `n` el movimiento medio.
- La anomalía media `M = 2π(t − t₀)/P`.

💡 **Cómo se explica en la clase [B02-C14](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md):**
- La anomalía media crece de manera uniforme: `M = 2π t/T`.
- A["Parámetros:<br/>a, e, T"] --> B["Tiempo t → anomalía media<br/>M = 2π t / T"]
- 🎯 **Por qué importa:** Para Kepler, como para todos antes, el círculo era la figura natural del cielo. Los datos de Tycho no se dejaban describir con círculos.

📘 **Dónde se aprende** (3 clases): [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B29-C03 · Velocidad radial estelar](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md).

### Anomalía verdadera

- La anomalía verdadera es el ángulo `θ` de un cuerpo en órbita medido desde el perihelio, con el Sol en el origen.
- La anomalía verdadera `ν` es el ángulo real desde el periapsis.

🎯 **Por qué importa (clase B04-C10):** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.

📘 **Dónde se aprende** (2 clases): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md); [B71-C13 · Anomalías orbitales](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md).

### Anomalía/discrepancia

- Anomalía/discrepancia: variación frente a lo esperado.

🎯 **Por qué importa (clase B90-C17):** Una falla única en 500 horas de ensayo no demuestra que el equipo sea confiable: solo acota la tasa de fallas. Y una anomalía mal registrada se pierde.

📘 **Dónde se aprende** (1 clase): [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md).

### Anotador

- Un anotador es quien etiqueta.

💡 **Cómo se explica en la clase [B17-C10](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md):**
- Con clases equiprobables, cada anotador da 50 % a cada clase, y `pₑ = 0,5`.
- Que cada anotador acierte el 80 % no basta para un acuerdo alto entre ellos.
- 🎯 **Por qué importa:** Se quiere entrenar un modelo que distinga galaxias espirales de elípticas. Hay un millón de imágenes y nadie las ha etiquetado.

📘 **Dónde se aprende** (1 clase): [B17-C10 · Conjuntos de datos etiquetados para aprendizaje supervisado](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md).

### Antena de referencia

- La antena de referencia (fase 0).

🎯 **Por qué importa (clase B51-C03):** Sin ganancias el conjunto de datos no sirve para formar imágenes. La decisión central: ¿cómo se estiman las ganancias a partir de un modelo de cielo conocido y qué precisión se alcanza?

📘 **Dónde se aprende** (1 clase): [B51-C03 · Ganancias complejas por antena y soluciones de calibración](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md).

### Antes

- El de ventana también reinicia si la patada llega antes de `t_min`.

💡 **Cómo se explica en la clase [B88-C11](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md):**
- Analogía: un watchdog de ventana es como un guardia que exige que lo saludes cada hora, ni antes de los 40 minutos ni después de los 80.
- 🎯 **Por qué importa:** Un watchdog mal ajustado reinicia sin necesidad o no reinicia cuando hace falta. La decisión central: ¿qué ventana y qué escalera de acciones recuperan un software colgado sin reinicios falsos?

📘 **Dónde se aprende** (1 clase): [B88-C11 · Watchdogs y recuperación](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md).

### Anticonmutativo

- Es anticonmutativo: `v × u = −(u × v)`.

🎯 **Por qué importa (clase B04-C14):** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?

📘 **Dónde se aprende** (1 clase): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md).

### Antiderivada

- Una antiderivada de `f` es una función `F` tal que `F′ = f`.

💡 **Cómo se explica en la clase [B09-C08](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md):**
- Si `F` es antiderivada, también lo es `F + C`.
- Toda antiderivada se valida derivándola.
- 🎯 **Por qué importa:** Un acelerómetro mide aceleración; lo que se necesita es velocidad y posición. Una gravedad `g(r)` se conoce; lo que decide si una sonda escapa es la energía, que sale de «deshacer» esa derivada.

📘 **Dónde se aprende** (1 clase): [B09-C08 · Integrales indefinidas](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md).

### Antidisipativo

- Un método es disipativo si reduce la energía y antidisipativo si la aumenta.

💡 **Cómo se explica en la clase [B11-C10](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md):**
- Es antidisipativo y no sirve para ninguna propagación seria.
- 🎯 **Por qué importa:** Un análisis de misión puede necesitar propagar un satélite durante años, es decir, decenas de miles de vueltas. Si cada vuelta añade o quita un poco de energía, la altura de la órbita cambia solo por culpa del programa.

📘 **Dónde se aprende** (1 clase): [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md).

### Antigüedad

- La antigüedad es `ahora − instante efectivo`.

💡 **Cómo se explica en la clase [B116-C07](../programa/clases/B116/B116-C07-diseno-de-paneles-de-monitoreo-de-salud/CLASE.md):**
- La antigüedad es `ahora − efectivo`; el retardo de comunicaciones ya está en ese desfase.
- El campo `effective` de una observación FHIR es el instante clínicamente relevante; la antigüedad se calcula contra ese instante y no contra el de recepción.
- ⚠️ **Error frecuente:** Mostrar el último valor sin su edad. Calcula y muestra la antigüedad (8.3).
- 🎯 **Por qué importa:** Un panel que muestra «FC 72» sin decir de cuándo es, o que usa un gris que no se lee, puede ser peor que no tener panel. La decisión central: ¿qué debe mostrar un panel de salud para que quien lo mira sepa qué está pasando, cuán fresco es el dato y a quién atender primero?

📘 **Dónde se aprende** (1 clase): [B116-C07 · Diseño de paneles de monitoreo de salud](../programa/clases/B116/B116-C07-diseno-de-paneles-de-monitoreo-de-salud/CLASE.md).

### Antisimétrica

- Una matriz antisimétrica cumple `Kᵀ = −K`; la del eje unitario `u` es `K = [[0, −u₃, u₂], [u₃, 0, −u₁], [−u₂, u₁, 0]]` y cumple `K v = u × v`.

🎯 **Por qué importa (clase B10-C13):** La actitud de un satélite (hacia dónde apuntan sus ejes) se guarda como una matriz de rotación: sus columnas son los ejes del cuerpo expresados en el sistema inercial. Con ella, un seguidor estelar, un panel o una antena se orientan sin ambigüedad.

📘 **Dónde se aprende** (1 clase): [B10-C13 · Matrices de rotación tridimensional](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md).

### Anti-windup

- El anti-windup es cualquier mecanismo que lo evita.
- El antiwindup detiene la integral cuando el actuador satura.

💡 **Cómo se explica en la clase [B16-C18](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md):**
- Sin anti-windup, `ξ̇ = e` todo el tiempo, también durante la saturación.
- Resultado: la integral máxima es 0,099 rad·s (frente a 5,29), el sobreimpulso baja a 0,8 % y el asentamiento (2 %) a 40,9 s (frente a 61,9 s sin anti-windup).
- ⚠️ **Error frecuente:** Medir el anti-windup solo en el caso saturado. Se corrige con el ejercicio 6 y la sección 8.4.
- 🎯 **Por qué importa:** Una rueda de reacción entrega un par máximo y almacena un momento angular máximo (el Hubble usa ruedas de hasta unas 3000 rpm, y magnetopares para gestionar su velocidad, S1). Cuando el controlador pide más de lo que el actuador puede dar, el lazo deja de comportarse como se diseñó.

📘 **Dónde se aprende** (2 clases): [B16-C18 · Saturación y anti-windup](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md); [B85-C10 · Control térmico activo](../programa/clases/B85/B85-C10-control-termico-activo/CLASE.md).

### Antropometría

- La antropometría mide las dimensiones del cuerpo.

💡 **Cómo se explica en la clase [B109-C06](../programa/clases/B109/B109-C06-antropometria-y-dimensionamiento-para-tripulacion/CLASE.md):**
- Con `g = 1,62 m/s²` (NASA/NSSDC) la gravedad parcial permite posturas verticales y movimientos que en microgravedad no existen, y por eso la antropometría de microgravedad no se traslada sin revisión.
- El concepto de hábitat lunar de NASA (Burke et al., 2022) define sus volúmenes funcionales con la antropometría del percentil 99 de hombres y mujeres y una altura estándar de `2,4 m`; el volumen de sueño es de `1 m` de altura y la longitud del cuerpo manda sobre la litera.
- 🎯 **Por qué importa:** Si se dimensiona para la media, la mitad de las personas no cabe o no alcanza. La decisión central: ¿qué percentil de qué población usar para cada dimensión?

📘 **Dónde se aprende** (1 clase): [B109-C06 · Antropometría y dimensionamiento para tripulación](../programa/clases/B109/B109-C06-antropometria-y-dimensionamiento-para-tripulacion/CLASE.md).

### Anular

- Un eclipse solar es total si la Luna cubre por completo el Sol; anular si la Luna parece más pequeña que el Sol y deja un anillo brillante;

💡 **Cómo se explica en la clase [B08-C09](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md):**
- En 2025 la distancia varió entre 356 830 y 406 690 km (S2): cerca del perigeo un eclipse central sería total, cerca del apogeo, anular.
- Pausa. El 21 de septiembre de 2025 la Luna estaba a 396 872 km; si el eclipse hubiese sido central, ¿habría sido total o anular? <details><summary>Respuesta</summary>`396 872 > 380 909 km`: el vértice no llega: anular.</details>
- ⚠️ **Error frecuente:** Creer que un eclipse anular es seguro a simple vista. Ejercicio 10.
- 🎯 **Por qué importa:** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?

📘 **Dónde se aprende** (1 clase): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md).

### Año juliano

- El año juliano es, por convención del programa, 365,25 d.

🎯 **Por qué importa (clase B03-C08):** El período de Neptuno en las fichas de la NASA es 60 189,018 días. Nadie piensa en 60 mil días; se piensa en años.

📘 **Dónde se aprende** (1 clase): [B03-C08 · Tiempo y conversiones astronómicas](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md).
