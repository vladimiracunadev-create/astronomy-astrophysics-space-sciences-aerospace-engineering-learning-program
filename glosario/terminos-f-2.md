# Términos · F (parte 2 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · **F** · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-f.md) · **2**

### Fracción de eclipse

- La fracción de eclipse es `f = (1/π) arccos(√(h² + 2Rh)/((R + h) cos β))` para `|β|` menor que `β* = asin(R/(R + h))`.
- Sombra cilíndrica: modelo de sombra sin penumbra. Fracción de eclipse: parte de la vuelta en sombra.

💡 **Cómo se explica en la clase [B76-C18](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md):**
- G["R, h, beta"] --> F["fraccion de eclipse"]
- *Descripción textual:* la geometría da la fracción de eclipse y el `β` crítico, que se verifican numéricamente; la fase de la aproximación V-bar y el eclipse dan la fracción de órbita utilizable.
- 🎯 **Por qué importa:** Una aproximación planificada de noche, o con el Sol detrás del objetivo, puede dejar ciego al sensor. La decisión central: ¿qué fracción de la órbita está al sol y con buena fase, según el ángulo `β`?
- 🔗 **Se estudia junto con:** fase, contraluz.

📘 **Dónde se aprende** (2 clases): [B76-C18 · Restricciones de iluminación](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md); [B96-C11 · Operación durante eclipse](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md).

### Fracción de gas

- La fracción de gas es `M_gas/M`.
- La fracción de gas `μ = M_gas/M_total`.

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- F["Perfil de gas"] --> G["M_gas(<r)"] --> H["Fracción de gas"]
- *Descripción textual:* con la temperatura y la forma del gas se obtiene la masa hidrostática; con la dispersión de las galaxias, la de una esfera isoterma; se comparan, y el perfil de gas da su masa y la fracción respecto del total.
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.
- 🔗 **Se estudia junto con:** cúmulo de galaxias, medio intracúmulo (ICM), temperatura, equilibrio hidrostático.

📘 **Dónde se aprende** (2 clases): [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md); [B25-C17 · Metalicidad y evolución química](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md).

### Fracción de helio

- La fracción de helio `Y_p` es la fracción de masa en helio-4.

💡 **Cómo se explica en la clase [B26-C16](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md):**
- Relacionar `n/p` con la fracción de helio `Y_p`.
- La evidencia es el cálculo de la fracción de helio del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** La cuarta parte de la masa bariónica del universo es helio, y la proporción casi no cambió desde los primeros minutos. Su valor da información sobre cuántas especies de neutrinos existen y sobre la densidad de bariones.
- 🔗 **Se estudia junto con:** nucleosíntesis primordial, razón n/p, congelación, vida media del neutrón libre.

📘 **Dónde se aprende** (1 clase): [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Fracción de inercia

- La fracción de inercia `ζ` pesa cada región.

💡 **Cómo se explica en la clase [B37-C11](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md):**
- *Descripción textual:* cada modo promedia la rotación según su fracción de inercia y varios modos permiten separar las dos zonas.
- 🎯 **Por qué importa:** El desdoblamiento promedia la rotación de las regiones que el modo explora. La decisión central: ¿cuánto giran el núcleo y la envoltura y con qué incertidumbre y correlación?
- 🔗 **Se estudia junto con:** desdoblamiento rotacional, rotación diferencial, coeficiente de Ledoux, cuerpo rígido.

📘 **Dónde se aprende** (1 clase): [B37-C11 · Rotación interna a partir del desdoblamiento de frecuencias](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md).

### Fracción de masa

- La fracción de masa `F(>M) = erfc(ν/√2)`.
- La fracción de masa usa `m ∝ D³`.

💡 **Cómo se explica en la clase [B36-C06](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md):**
- Es como una piscina con un borde: el agua (la densidad) sube al azar y la fracción de caminos que alguna vez pasan el borde es la fracción de masa en halos.
- *Descripción textual:* el colapso esférico fija el umbral, que junto con σ(M) da la fracción de masa y la función de masa; las caminatas lo verifican.
- ⚠️ **Error frecuente:** Olvidar el factor 2 de Press–Schechter. Se corrige con la fracción de masa.
- 🎯 **Por qué importa:** Contar halos exige un umbral de colapso y una función de masa. La decisión central: ¿cuánta masa del universo está en halos de más de cierta masa?
- 🔗 **Se estudia junto con:** umbral de colapso, altura, función de masa, caminata del conjunto de excursión.

📘 **Dónde se aprende** (2 clases): [B36-C06 · Formación de halos y función de masa](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md); [B52-C13 · Pequeños cuerpos remanentes](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md).

### Fracción de masa convertida

- La fracción de masa convertida `ε = Δm/m` indica qué porción de la masa de combustible pasa a energía.
- La fracción de masa convertida `ε` es la porción de masa que se vuelve energía.
- La fracción de masa convertida es `E/(M c²)`.

💡 **Cómo se explica en la clase [B24-C06](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md):**
- Calcular la fracción de masa convertida y la energía por kilogramo.
- fraccion de masa convertida epsilon = 0.00712
- 🎯 **Por qué importa:** Una estrella como el Sol brilla desde hace miles de millones de años; ninguna fuente química ni gravitatoria alcanza (C02). La fusión nuclear sí.
- 🔗 **Se estudia junto con:** fusión nuclear, defecto de masa, protón, partícula alfa.

📘 **Dónde se aprende** (3 clases): [B24-C06 · Fusión de hidrógeno](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md); [B24-C08 · Nucleosíntesis estelar](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md); [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md).

### Fracción de nubes

- La fracción de nubes `k` descuenta el cielo cubierto.

💡 **Cómo se explica en la clase [B129-C03](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md):**
- Hora de inicio y fin, tiempo efectivo, fracción de nubes, magnitud límite medida con estrellas de referencia, campo observado, altura del radiante y recuento por lluvia; además identificar el sitio sin dar coordenadas exactas de la vivienda.
- 🎯 **Por qué importa:** Cuarenta personas cuentan meteoros una noche: unos con un cielo más oscuro, otros bajo nubes, otros con el radiante bajo. La decisión central: ¿cómo se combinan sus recuentos en una sola tasa comparable, y con qué incertidumbre?
- 🔗 **Se estudia junto con:** ZHR, índice de población, magnitud límite, tiempo efectivo.

📘 **Dónde se aprende** (1 clase): [B129-C03 · Seguimiento ciudadano de meteoros](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md).

### Fracción de píxel

- La fracción de píxel `p` es la parte del píxel en llamas.

💡 **Cómo se explica en la clase [B57-C16](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md):**
- Con un ruido de `0,5 K` a 300 K y un umbral de 3 veces el ruido, la fracción mínima detectable es `2,80e-05`, es decir, un área de `3,9 m²` en un píxel de 375 m y de `28 m²` en uno de 1 km.
- Datos: píxeles de FIRMS (S1); temperaturas, fracción y ruido ilustrativos / sintéticos.
- ⚠️ **Error frecuente:** Confundir el tamaño del píxel con el del incendio. El incendio ocupa una fracción `p` (sección 6).
- 🎯 **Por qué importa:** Un incendio pequeño puede ser un desastre en horas, pero un píxel mide cientos de metros. La decisión central: ¿cuál es la fracción de píxel más pequeña que se puede detectar y cuánto sesga la estimación un error en el fondo?
- 🔗 **Se estudia junto con:** detección activa de fuego, banda de infrarrojo medio, infrarrojo térmico, radiancia mixta.

📘 **Dónde se aprende** (1 clase): [B57-C16 · Incendios forestales](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md).

### Fracción de propelente

- La fracción de propelente es `1 − m_f/m₀`.

💡 **Contexto en la clase [B05-C20](../programa/clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md):**
- **Idea central (modelo mental):** El satélite ideal es una masa puntual sobre la que solo actúa la gravedad de la Tierra. Cada pregunta del bloque es una lente distinta sobre el mismo modelo.
- 🎯 **Por qué importa:** Un problema real no viene etiquetado «esto es de energía» o «esto es de momento». La pregunta motivadora es: ¿cómo planteo, resuelvo y valido un problema físico completo, eligiendo el modelo correcto para cada parte y declarando dónde dejan de valer?
- 🔗 **Se estudia junto con:** órbita de transferencia de Hohmann, impulso, semieje mayor, ecuación vis-viva.

📘 **Dónde se aprende** (1 clase): [B05-C20 · Problema físico integrado de satélite ideal](../programa/clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md).

### Fracción de propergol

- La fracción de propergol es `1 − exp(−Δv/(Isp g0))`.

💡 **Cómo se explica en la clase [B76-C07](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md):**
- Convertir el `Δv` en fracción de propergol con la ecuación de Tsiolkovsky.
- Ejercicio 4 · autónomo. Calcula la fracción de propergol solo de la LOI.
- ⚠️ **Error frecuente:** Sumar fracciones de propergol. No son aditivas.
- 🎯 **Por qué importa:** Un diseño preliminar de misión empieza por el presupuesto de velocidad. La decisión central: ¿cuánto `Δv` cuestan la salida de la Tierra y la captura en la Luna, y cuánto cambia la segunda según la órbita lunar elegida?
- 🔗 **Se estudia junto con:** inyección translunar (TLI), inserción en órbita lunar (LOI), velocidad de llegada, excentricidad hiperbólica.

📘 **Dónde se aprende** (1 clase): [B76-C07 · Maniobras de inserción cislunar](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md).

### Fracción de propulsante

- La fracción de propulsante es `1 − e^{−Δv/(I_sp g₀)}`.

💡 **Cómo se explica en la clase [B75-C11](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md):**
- *Descripción textual:* Se integra la espiral hasta el radio de Marte; el tiempo y la aceleración dan el delta-v; se compara con Edelbaum y se convierte en fracción de propulsante.
- Fracción de propulsante: la ecuación del cohete con `I_sp` alta frente a baja.
- 🎯 **Por qué importa:** Un motor de alta `I_sp` ahorra propulsante pero tarda mucho. La decisión central: ¿cuánto delta-v y cuánto tiempo cuesta una espiral y cuándo es válida la fórmula de Edelbaum?
- 🔗 **Se estudia junto con:** propulsión de bajo empuje, espiral de Edelbaum, cociente a/g☉.

📘 **Dónde se aprende** (1 clase): [B75-C11 · Propulsión de bajo empuje](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md).

### Fracción de reserva

- La fracción de reserva es `(FC − FC_reposo)/(FC_máx − FC_reposo)`.

💡 **Cómo se explica en la clase [B104-C04](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md):**
- Con FC de reposo 55 y máxima 190 lpm (valores de ejemplo), a 140 lpm la fracción de reserva es `(140−55)/135 = 0,630` y la carga de 30 min `30·0,630·0,64·e^(1,92·0,630) = 40,5` unidades; a 110 lpm, 17,1; a 165 lpm, 74,8.
- Paso 1 · Fracción de reserva. `(140 − 55)/(190 − 55) = 0,630`.
- 🎯 **Por qué importa:** Entrenar más no siempre significa rendir más el día que importa. La decisión central: ¿cómo distribuir una misma carga total para llegar con la mejor combinación de aptitud y fatiga?
- 🔗 **Se estudia junto con:** carga, aptitud, fatiga, rendimiento.

📘 **Dónde se aprende** (1 clase): [B104-C04 · Acondicionamiento físico general](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md).

### Fracción de tanques

- La fracción de tanques `k` es la masa de tanque por kilo de propelente.

💡 **Cómo se explica en la clase [B78-C02](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md):**
- Descripción larga: el Δv crece con el logaritmo de la razón de masas y tiene una cota que depende solo de la fracción de tanques y del `Isp`.
- Calcular la cota de Δv que impone la fracción de tanques.
- 🎯 **Por qué importa:** Más propelente da más Δv, pero cada kilo de propelente exige tanques, y esos tanques también se aceleran. La decisión central: ¿cuánto propelente hace falta para un Δv dado y existe un máximo de Δv que ninguna cantidad de propelente supera?
- 🔗 **Se estudia junto con:** ecuación del cohete, masa inicial, masa final, cota de Δv.

📘 **Dónde se aprende** (2 clases): [B78-C02 · Propulsión química como sistema físico](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md); [B78-C17 · Masa de propelente y presupuesto](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md).

### Fracción del cielo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B28-C11](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md):**
- *Descripción textual:* la tasa y la ventana dan el número medio de eventos de fondo; el área da la fracción del cielo; su producto, en una distribución de Poisson, da la probabilidad fortuita, que se verifica por simulación.
- 🎯 **Por qué importa:** Que dos señales coincidan no prueba que estén relacionadas: la pregunta es cuán probable es la coincidencia por azar. Una probabilidad fortuita muy baja es lo que convierte una coincidencia en un descubrimiento.
- 🔗 **Se estudia junto con:** probabilidad fortuita, ventana, tasa, isotropía.

📘 **Dónde se aprende** (1 clase): [B28-C11 · Coincidencias entre observatorios](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md).

### Fracción dirigida

- La fracción dirigida `f` es la parte de la energía que queda como energía cinética del escape.

💡 **Cómo se explica en la clase [B78-C16](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md):**
- *Descripción textual:* la energía por reacción y la masa de los reactivos dan la energía específica; ésta da la fracción de masa convertida y, con la fracción dirigida, la cota de escape, que se contrasta con la relativista; con una potencia dada se calcula el consumo.
- Acotar el escape `Vₑ = √(2 f ε)` según la fracción dirigida `f`.
- ⚠️ **Error frecuente:** Olvidar la fracción dirigida. Se corrige con 8.2.
- 🎯 **Por qué importa:** Si la energía por kilo es millones de veces mayor, el escape posible es enorme; pero eso es una cota, no un propulsor. La decisión central: ¿cuánta energía por kilo libera cada reacción y cuánto escape acotaría, según la fracción que se logre dirigir?
- 🔗 **Se estudia junto con:** energía específica, fracción de masa convertida, cota de escape, fusión como investigación.

📘 **Dónde se aprende** (1 clase): [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md).

### Fracción disociada

- La fracción disociada `a` es la parte del amoníaco que se separa en nitrógeno e hidrógeno.

💡 **Cómo se explica en la clase [B78-C04](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md):**
- *Descripción textual:* el propelente se descompone en amoníaco y nitrógeno liberando calor; la fracción disociada fija la temperatura (baja) y la masa molar (baja); ambas determinan el escape.
- Calcular la masa molar media de los productos según la fracción disociada `a`.
- 🎯 **Por qué importa:** La descomposición de un monopropelente tiene dos pasos: uno que libera calor y otro que lo absorbe. La decisión central: ¿conviene que el amoníaco intermedio se disocie del todo, por la menor masa molar, o que se conserve, por la mayor temperatura?
- 🔗 **Se estudia junto con:** monopropelente, descomposición exotérmica, disociación, temperatura adiabática.

📘 **Dónde se aprende** (1 clase): [B78-C04 · Propulsión monopropelente conceptual](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md).

### Fracción en masa

- La fracción en número es `N_i / ΣN`; la fracción en masa es `N_i m_i / ΣN_j m_j`.

💡 **Cómo se explica en la clase [B55-C01](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md):**
- *Descripción textual:* la tabla logarítmica se exponencia para obtener cantidades relativas al hidrógeno; multiplicadas por la masa atómica y normalizadas dan las fracciones en masa, que se verifican convirtiendo de vuelta.
- Paso 4 · Masa. `N m = 5,012 × 10⁻⁴ × 15,9994 = 8,019 × 10⁻³` y la suma de todos los `N m` vale `1,3413`: fracción `5,978 × 10⁻³`.
- ⚠️ **Error frecuente:** Olvidar que la fracción en masa depende de las masas atómicas. Se aplica 8.3.
- 🎯 **Por qué importa:** Cualquier modelo químico del espacio parte de una composición inicial: cuánto hidrógeno, helio, carbono u oxígeno hay. Las fuentes dan esa composición en una escala logarítmica poco intuitiva, y los modelos piden fracciones en número o en masa.
- 🔗 **Se estudia junto con:** abundancia logarítmica, fracción en número, dex, metalicidad.

📘 **Dónde se aprende** (1 clase): [B55-C01 · Abundancia química cósmica](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md).

### Fracción en número

- La fracción en número es `N_i / ΣN`; la fracción en masa es `N_i m_i / ΣN_j m_j`.

💡 **Cómo se explica en la clase [B55-C01](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md):**
- Paso 3 · Fracción en número de O. `5,012 × 10⁻⁴ / 1,0803 = 4,639 × 10⁻⁴`.
- Por fracción en número: natural para la química (reacciones entre átomos).
- 🎯 **Por qué importa:** Cualquier modelo químico del espacio parte de una composición inicial: cuánto hidrógeno, helio, carbono u oxígeno hay. Las fuentes dan esa composición en una escala logarítmica poco intuitiva, y los modelos piden fracciones en número o en masa.
- 🔗 **Se estudia junto con:** abundancia logarítmica, fracción en masa, dex, metalicidad.

📘 **Dónde se aprende** (1 clase): [B55-C01 · Abundancia química cósmica](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md).

### Fracción encerrada

- La fracción encerrada continua es `1 − exp(−r²/2σ²)`.

💡 **Cómo se explica en la clase [B45-C23](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md):**
- *Descripción textual:* la fracción encerrada y el ruido del cielo compiten y dan un máximo de S/N en un radio cercano a la FWHM.
- Calcular la fracción encerrada de una PSF gaussiana.
- 🎯 **Por qué importa:** Una apertura pequeña pierde flujo y una grande añade ruido de cielo. La decisión central: ¿qué radio da el mejor S/N y cómo se mide el cielo?
- 🔗 **Se estudia junto con:** apertura, anillo de cielo, mediana, contaminación.

📘 **Dónde se aprende** (1 clase): [B45-C23 · Fotometría de apertura y estimación del cielo](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md).

### Fracción estacional

- La fracción estacional compara el rango de presión con la media.

💡 **Cómo se explica en la clase [B54-C14](../programa/clases/B54/B54-C14-atmosfera-de-marte/CLASE.md):**
- P["P media, rango"] --> F["fracción estacional"]
- Estimar la fracción estacional `(P_max − P_min)/P_media`.
- 🎯 **Por qué importa:** La presión marciana varía unas decenas de por ciento durante el año porque parte del CO₂ se condensa en los casquetes polares. La pregunta motivadora: ¿cuánta masa de CO₂ participa en ese ciclo?
- 🔗 **Se estudia junto con:** masa de la atmósfera, temperatura de escarcha, escala de tiempo radiativa.

📘 **Dónde se aprende** (1 clase): [B54-C14 · Atmósfera de Marte](../programa/clases/B54/B54-C14-atmosfera-de-marte/CLASE.md).

### Fracción estructural

- La fracción estructural `ε` es la estructura sobre el propelente de la etapa en este modelo.

💡 **Cómo se explica en la clase [B100-C02](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md):**
- Límite: cada tramo usa una etapa nueva con fracción estructural constante; en una misión real las etapas se reutilizan o se dimensionan por separado.
- Con tres tramos de Δv ilustrativos (3,1 + 0,9 + 1,9 km/s), `Isp = 450 s` y fracción estructural 0,10, hacen falta `3924,7 kg` en órbita baja: un factor `4,584`.
- 🎯 **Por qué importa:** La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: ¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?
- 🔗 **Se estudia junto con:** masa neta, factor de embalaje, repuestos, ecuación ideal del cohete.

📘 **Dónde se aprende** (1 clase): [B100-C02 · Dimensionamiento de carga y volumen de misión](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md).

### Fracción expuesta

- La fracción expuesta `c` es el área con abrasivo.

💡 **Cómo se explica en la clase [B84-C36](../programa/clases/B84/B84-C36-desgaste-abrasivo-por-regolito-en-mecanismos/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar la fracción expuesta. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** Un sello de acero inoxidable bajo regolito pierde 1,8 mm en 1000 h con un 10 % del área expuesta a polvo, y uno de carburo de volframio pierde 0,18 µm: la elección de dureza decide si el mecanismo vive. La decisión central: ¿qué superficie y qué estrategia de protección permiten que un mecanismo sobreviva al regolito?
- 🔗 **Se estudia junto con:** ley de Archard, regla de dureza relativa, vida.

📘 **Dónde se aprende** (1 clase): [B84-C36 · Desgaste abrasivo por regolito en mecanismos](../programa/clases/B84/B84-C36-desgaste-abrasivo-por-regolito-en-mecanismos/CLASE.md).

### Fracción iluminada

- La fracción iluminada `f` es la parte del disco que se ve iluminada.
- La fracción iluminada `k` es la parte del disco visible que recibe luz solar.
- La fracción iluminada `k_f` es la parte del disco visible que está iluminada.

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- Si la edad es `a`, el ángulo es `2π·a/P` y la fracción iluminada es `f = (1 − cos(2π·a/P))/2`.
- (El cuarto menguante cae en 22,1 d, no exactamente en `3P/4 = 22,15 d`, por el redondeo de la edad.) Descripción larga: la fracción iluminada sube de 0 a 1 en medio ciclo y baja de nuevo.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.
- 🔗 **Se estudia junto con:** fase, luna nueva, luna llena, cuartos.

📘 **Dónde se aprende** (3 clases): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B128-C03 · Alternativas a la observación visual](../programa/clases/B128/B128-C03-alternativas-a-la-observacion-visual/CLASE.md); [B131-C05 · Demostraciones visuales y modelos para el aula](../programa/clases/B131/B131-C05-demostraciones-visuales-y-modelos-para-el-aula/CLASE.md).

### Fracción inspirada

- La fracción inspirada `FiO₂` es la proporción de O₂ del aire que se respira.

💡 **Cómo se explica en la clase [B117-C04](../programa/clases/B117/B117-C04-problemas-respiratorios-simulados/CLASE.md):**
- *Descripción textual:* la cabina fija la fracción de O₂ inspirada; con la ventilación (CO₂) se obtiene la presión alveolar, después la arterial y la saturación; una fuga reduce `Pb` con el tiempo.
- Calcular la fracción inspirada de O₂ `FiO₂ = ppO₂/Pb`.
- 🎯 **Por qué importa:** Ninguna clase anterior simula problemas respiratorios. La decisión central: ¿cuánto margen de oxigenación hay entre la atmósfera nominal de la cabina y una condición peligrosa, y qué variable lo consume más rápido?
- 🔗 **Se estudia junto con:** presión alveolar, gradiente alvéolo-arterial, saturación, hipoventilación.

📘 **Dónde se aprende** (1 clase): [B117-C04 · Problemas respiratorios simulados](../programa/clases/B117/B117-C04-problemas-respiratorios-simulados/CLASE.md).

### Fracción ionizada

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C02](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md):**
- *Descripción textual:* la temperatura da la razón de poblaciones y la constante de Saha, que determina la fracción ionizada y la temperatura del 50 %.
- Descripción larga: la fracción ionizada pasa de casi cero a casi uno en pocas decenas de miles de kelvin.
- 🎯 **Por qué importa:** Si el ETL falla, las abundancias que se derivan son erróneas. La decisión central: ¿cuánto hidrógeno está ionizado a cada temperatura y densidad?
- 🔗 **Se estudia junto con:** ecuación de Boltzmann, ecuación de Saha, ETL, desviación no ETL.

📘 **Dónde se aprende** (1 clase): [B32-C02 · Equilibrio termodinámico local y desviaciones no LTE](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md).

### Fracción molar

- La fracción molar `y_i` de un componente de una mezcla es su cantidad de sustancia dividida entre la total; para gases ideales, coincide con la fracción en volumen.

💡 **Cómo se explica en la clase [B06-C07](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md):**
- Si `y_i` son fracciones molares, `M̄ = Σ y_i M_i / Σ y_i` (se normaliza cuando las fichas redondean y no suman 100).
- Un componente «importa» según su fracción y según cuánto se aparta su masa molar de la media.
- 🎯 **Por qué importa:** Si quieres saber cuánto pesa una columna de atmósfera de Marte, necesitas su masa molar media, y para eso, su composición. La NASA publica la composición en volumen de las atmósferas de Marte, Venus y la Tierra y también un «peso molecular» medio (S1, S2, S3).
- 🔗 **Se estudia junto con:** fórmula molecular, fórmula empírica, composición porcentual, masa molar media.

📘 **Dónde se aprende** (1 clase): [B06-C07 · Estequiometría elemental](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md).

### Fracción no cubierta

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C18](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md):**
- Con dos capas (suelo 60 % y 8 km 40 %), `r₀ = 0,13 m` a 500 nm (ilustrativos) `θ₀ = 1,825 arcsec`; con cuatro guías a ±30 arcsec la fracción no cubierta es `0` hasta 20 arcsec, `0,0021` a 30 y `0,1667` en la diagonal de 50 arcsec.
- Estimar la fracción no cubierta por cuatro guías.
- 🎯 **Por qué importa:** Una sola corrección solo vale dentro del ángulo isoplanático (unos segundos de arco). La decisión central: ¿cómo se amplía el campo y qué parte de la turbulencia queda sin restricción?
- 🔗 **Se estudia junto con:** anisoplanatismo, ángulo isoplanático, altura efectiva, MCAO.

📘 **Dónde se aprende** (1 clase): [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### Fracción por volumen

- La fracción por volumen es la proporción de moléculas de una especie.

💡 **Cómo se explica en la clase [B54-C02](../programa/clases/B54/B54-C02-composicion-quimica-atmosferica/CLASE.md):**
- F["fracciones por volumen"] --> M["masa molar media M"]
- Calcular la masa molar media de una mezcla a partir de fracciones por volumen.
- ⚠️ **Error frecuente:** Confundir fracción por volumen con fracción por masa. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Dos atmósferas con la misma temperatura y gravedad tienen alturas de escala distintas si sus gases pesan distinto. La pregunta motivadora: ¿qué parte de la diferencia entre las atmósferas de los planetas viene solo de la composición?
- 🔗 **Se estudia junto con:** masa molar media, especie traza, renormalización, altura de escala.

📘 **Dónde se aprende** (1 clase): [B54-C02 · Composición química atmosférica](../programa/clases/B54/B54-C02-composicion-quimica-atmosferica/CLASE.md).

### Fracción reportada

- La fracción reportada `r(t)` es la proporción de incidentes que se informan.

💡 **Cómo se explica en la clase [B119-C21](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md):**
- *Descripción textual:* los incidentes verdaderos pasan por el filtro de la fracción reportada; corregir por ella permite estimar el aprendizaje real.
- No se consultó ninguna norma de seguridad ni estudio de cultura. El ejemplo conductor: una organización ficticia con 100 unidades de exposición por año, tasa verdadera `λ(t) = 12 t^(−0,30)` incidentes por unidad de exposición (1200 esperados el año 1) y una fracción reportada que crece de 0,35 a 0,90 en 10 años.
- 🎯 **Por qué importa:** B88-C16 cubre la seguridad funcional técnica; ninguna clase trata la dimensión cultural, y los indicadores de reportes se malinterpretan con facilidad. La decisión central: ¿qué indicador permite saber si una organización aprende cuando los reportes dependen de la confianza para informar?
- 🔗 **Se estudia junto con:** cultura de seguridad, curva de aprendizaje, cultura justa, Subnotificación.

📘 **Dónde se aprende** (1 clase): [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md).

### Fracción serial

- La fracción serial `s` es la parte del tiempo en un procesador que no se puede repartir; la paralelizable es `1 − s`.

💡 **Cómo se explica en la clase [B18-C05](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md):**
- Ahora el problema crece con `N` y el tiempo en la máquina paralela es fijo, de valor 1: una fracción `s` serial y `1−s` paralela ejecutada por `N` procesadores.
- Si `e` es constante al variar `N`, la pérdida se explica por una fracción serial.
- 🎯 **Por qué importa:** Un grupo pide tiempo en un clúster para propagar un catálogo grande de órbitas. Antes de pedir mil núcleos hay que saber si el programa los aprovechará.
- 🔗 **Se estudia junto con:** escalado fuerte, escalado débil, aceleración, eficiencia.

📘 **Dónde se aprende** (1 clase): [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md).

### Fracción serie

- La fracción serie `s` es la parte del tiempo que no se puede repartir.

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Esa fracción serie incluye el coste de crear el `Pool`, no solo el código serie del programa.
- Aplicar la ley de Amdahl para predecir el techo y estimar la fracción serie.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.
- 🔗 **Se estudia junto con:** proceso, hilo, GIL, trabajador.

📘 **Dónde se aprende** (1 clase): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md).

### Fracción sin voltear

- La fracción sin voltear tras `t` es `e^(−λt)`.

💡 **Cómo se explica en la clase [B55-C14](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md):**
- *Descripción textual:* la tasa de volteo da la fracción sin voltear y los tiempos; la mezcla de componentes se invierte con un sistema lineal cuya precisión depende del ruido.
- Poisson analítico: la fracción sin voltear.
- 🎯 **Por qué importa:** El regolito es el suelo de un cuerpo sin atmósfera y su química depende de qué impactos lo removieron y de qué componentes lo formaron. La decisión central: ¿cuánto tiempo hace falta para que una capa se voltee y qué mezcla de componentes explica la composición medida?
- 🔗 **Se estudia junto con:** jardineria, tasa de volteo, componente, mezcla lineal.

📘 **Dónde se aprende** (1 clase): [B55-C14 · Química de regolitos](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md).

### Fracción termalizada

- La fracción termalizada `η` es la parte que se convierte en calor.

💡 **Cómo se explica en la clase [B52-C17](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md):**
- Impacto a 5 km/s, fraccion termalizada 0.1: energia cinetica especifica = 1.250e+07 J/kg ;
- 🎯 **Por qué importa:** El calor determina si un cuerpo funde, se diferencia o se enfría rápido. La decisión central: ¿cuánto tarda un cuerpo en perder su calor y cuánto lo calienta un impacto?
- 🔗 **Se estudia junto con:** difusividad térmica, escala de enfriamiento, energía de impacto específica, Crank–Nicolson.

📘 **Dónde se aprende** (1 clase): [B52-C17 · Colisiones y evolución térmica](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md).

### Fracción térmica

- La fracción térmica `f_th` de la energía que calienta el gas.

💡 **Cómo se explica en la clase [B38-C07](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md):**
- Descripción larga: al aumentar la fracción térmica el gas y la formación de equilibrio bajan.
- 🎯 **Por qué importa:** El gas denso forma estrellas por debajo de la resolución de la simulación y las supernovas devuelven energía. La decisión central: ¿cuánto gas expulsa la retroalimentación y a qué equilibrio llega la zona?
- 🔗 **Se estudia junto con:** modelo submalla, ley de Schmidt, eficiencia, número de supernovas por masa.

📘 **Dónde se aprende** (1 clase): [B38-C07 · Modelos submalla de formación estelar y retroalimentación](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md).

### Fracción terrestre

- La fracción terrestre es `R/D`.

💡 **Cómo se explica en la clase [B100-C07](../programa/clases/B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md):**
- Calcular la reposición terrestre y su fracción del consumo.
- Ejercicio 2 · con una pista. Calcula la fracción terrestre de ese caso.
- 🎯 **Por qué importa:** Reciclar el 90 % del agua no reduce la dependencia en un 90 %: quedan repuestos, fugas y averías, y el equipo pesa. La decisión central: ¿cuánta reposición terrestre queda según la eficiencia del lazo y cuántos días tarda el equipo en compensar su propia masa?
- 🔗 **Se estudia junto con:** eficiencia de recuperación, producción in situ, reposición terrestre, punto de equilibrio.

📘 **Dónde se aprende** (1 clase): [B100-C07 · Dependencia de suministros terrestres y cierre de lazos logísticos](../programa/clases/B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md).

### Fracción útil

- La fracción útil `π` es la carga útil entre la masa inicial.
- La fracción útil es la parte de la órbita con la actitud adecuada.
- La fracción útil es la proporción de direcciones con tres celdas dentro del campo.

💡 **Cómo se explica en la clase [B78-C15](../programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/CLASE.md):**
- *Descripción textual:* el Δv y el escape dan la fracción de propelente; ésta y el tiempo fijan la potencia y con `α` la masa de la planta; la carga útil es lo que queda y se busca el escape que la maximiza.
- Paso 4 · Fracción útil. `π = 1 − 0,1563 − 0,0870 = 0,7567`.
- 🎯 **Por qué importa:** Subir la velocidad de escape reduce el propelente pero obliga a más potencia, y por tanto a más planta, para el mismo tiempo de empuje. La decisión central: ¿existe un `Isp` que maximice la carga útil y cómo cambia con el Δv y con la masa específica de la planta?
- 🔗 **Se estudia junto con:** masa específica, velocidad característica, tiempo de empuje, propulsión nuclear-eléctrica.

📘 **Dónde se aprende** (3 clases): [B78-C15 · Propulsión nuclear eléctrica conceptual](../programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/CLASE.md); [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md); [B87-C03 · Sensores solares](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md).

### Fraccionamiento dependiente de la masa

- Un fraccionamiento dependiente de la masa sigue `δ'¹⁷ = β δ'¹⁸` con `δ' = 1000 ln(1+δ/1000)`.

💡 **Cómo se explica en la clase [B55-C13](../programa/clases/B55/B55-C13-isotopos-como-trazadores/CLASE.md):**
- Exponente de fraccionamiento dependiente de la masa beta = (1/m16 - 1/m17)/(1/m16 - 1/m18) = 0.530521
- 🎯 **Por qué importa:** Los isótopos son la «huella dactilar» de un reservorio: aguas, minerales y gases de distinto origen tienen razones distintas. Interpretarlas exige saber mezclar y distinguir fraccionamientos de procedencias.
- 🔗 **Se estudia junto con:** exponente, mezcla.

📘 **Dónde se aprende** (1 clase): [B55-C13 · Isótopos como trazadores](../programa/clases/B55/B55-C13-isotopos-como-trazadores/CLASE.md).

### Fraccionario

- El retardo entero y el fraccionario.

💡 **Contexto en la clase [B51-C08](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md):**
- **Idea central (modelo mental):** Como alinear dos grabaciones de la misma canción: primero deslizas compases enteros hasta que coinciden más o menos y después ajustas la fracción con una pendiente suave.
- 🎯 **Por qué importa:** Un retardo mal compensado reduce la coherencia y en VLBI hace perder la detección. La decisión central: ¿cómo se estima y se aplica un retardo con fracción de muestra y qué correlación se espera tras alinear?
- 🔗 **Se estudia junto con:** retardo entero, correlación cruzada, espectro cruzado, rampa de fase.

📘 **Dónde se aprende** (1 clase): [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Fragmentación

- Una fragmentación es la ruptura de un objeto en piezas.

💡 **Cómo se explica en la clase [B118-C09](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md):**
- La evidencia es la ficha de fragmentación ilustrativa del ejercicio 12 (sección 20).
- Que la mayor parte proviene de la fragmentación de naves y etapas, en su mayoría por ruptura involuntaria.
- 🎯 **Por qué importa:** La directriz 5 de la COPUOS dice que la mayor parte de los desechos catalogados proviene de fragmentaciones; entender cuántos fragmentos produce un evento y de qué tamaño es la base de los escenarios futuros. La decisión central: ¿cuántos fragmentos relevantes genera un evento y cuándo es «catastrófico»?
- 🔗 **Se estudia junto con:** catastrófica, ley de potencias de tamaños, conservación de la masa, energía relativa.

📘 **Dónde se aprende** (1 clase): [B118-C09 · Generación de desechos](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md).

### Fragmentación externa

- La fragmentación externa `1 − mayor_libre/total_libre`.

💡 **Cómo se explica en la clase [B88-C29](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md):**
- Primer ajuste sobre 4096 B: 0 fallos en 5000 pasos, pero la fragmentación externa máxima fue `0,239`: casi un cuarto de la memoria libre no era contigua con el mayor hueco.
- En 5000 pasos: el montón no falló pero llegó a `0,239` de fragmentación externa; el pool no falló.
- 🎯 **Por qué importa:** Un montón puede fallar después de horas por fragmentación aunque haya memoria libre; un pool de bloques fijos no. La decisión central: ¿qué esquema de memoria garantiza que una asignación nunca falle en vuelo?
- 🔗 **Se estudia junto con:** regla R3, pool, pila máxima.

📘 **Dónde se aprende** (1 clase): [B88-C29 · Gestión de memoria determinista en software de vuelo](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md).

### Fragmento

- Un fragmento (*chunk*) es el bloque de un dataset que se guarda y comprime como una unidad.

💡 **Cómo se explica en la clase [B14-C07](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md):**
- Cada documento está troceado en fragmentos que se leen o escriben por separado y se pueden comprimir.
- G --> F["flujo<br/>fragmentos de 10 000, gzip<br/>atributos: unidad, cadencia, procedencia"]
- ⚠️ **Error frecuente:** Cargar todo para leer un fragmento. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Una simulación o un instrumento moderno produce series de millones de muestras con sus metadatos. Guardarlas en texto es lento y pesado; cargarlas enteras en memoria para leer un fragmento es inviable.
- 🔗 **Se estudia junto con:** grupo, dataset, atributo, compresión sin pérdida.

📘 **Dónde se aprende** (1 clase): [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md).

### Franja

- Una franja es un ciclo de `2π`, equivalente a `λ/2` de desplazamiento.
- Una franja es un ciclo de 2π.
- La franja es el ancho que cubre la cámara.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B42-C09](../programa/clases/B42/B42-C09-interferometria-de-dos-haces/CLASE.md):**
- Un desplazamiento de 80 nm equivale a `1,5887 rad = 0,2528` franjas.
- Con `λ = 632,8 nm`, brazos 1 y 0,5 y ruido `σ = 0,01` (ilustrativos) la visibilidad es `0,942809`, las franjas distan `316,40 nm` y la fase de cuatro pasos tiene una dispersión de `4,9744 mrad` frente a `5,0000 mrad` previstos.
- ⚠️ **Error frecuente:** Olvidar el factor 2 del camino. Franja cada `λ/2` de espejo.
- 🎯 **Por qué importa:** La medida interferométrica de fase es la base de la metrología óptica (superficies, frentes de onda; C13).
- 🔗 **Se estudia junto con:** interferómetro de Michelson, diferencia de camino, paso de fase, amplitud de modulación.

📘 **Dónde se aprende** (4 clases): [B42-C09 · Interferometría de dos haces](../programa/clases/B42/B42-C09-interferometria-de-dos-haces/CLASE.md); [B57-C08 · Interferometría radar InSAR](../programa/clases/B57/B57-C08-interferometria-radar-insar/CLASE.md); [B69-C06 · Deslizamientos y subsidencia medidos con InSAR](../programa/clases/B69/B69-C06-deslizamientos-y-subsidencia-medidos-con-insar/CLASE.md); [B97-C01 · Robots rover y orbitadores](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md).

### Frecuencia

- La longitud de onda `λ` es la distancia entre dos crestas de la onda; la frecuencia `ν`, cuántas pasan por segundo; se relacionan con `c = λ·ν`.
- El período `T` es el tiempo de una vuelta; la frecuencia `f = 1/T` es el número de vueltas por segundo (hertz, Hz); la velocidad angular `ω = 2π/T` (rad/s) es el ángulo recorrido por unidad de tiempo.
- La longitud de onda `λ` es la distancia entre dos puntos iguales consecutivos (m); la frecuencia `f` (Hz) es el número de ciclos por segundo en un punto; la velocidad de propagación `v` cumple `v = f λ`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C03](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md):**
- Relacionar período, frecuencia, velocidad angular y rapidez en un círculo.
- 🎯 **Por qué importa:** Un cohete que enciende su motor un tiempo corto y un satélite que da vueltas son, a primera aproximación, estos dos movimientos. La pregunta motivadora es: ¿qué fórmulas valen cuando la aceleración es constante o cuando la rapidez es constante en un círculo, y hasta dónde son confiables?
- 🔗 **Se estudia junto con:** movimiento rectilíneo uniforme (MRU), movimiento rectilíneo uniformemente acelerado (MRUA), movimiento circular uniforme (MCU), período.

📖 **Explicado a fondo:** [Longitud de onda y frecuencia](esencial/esencial-d-l.md#longitud-de-onda-y-frecuencia) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md); [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B84-C20 · Diseño estructural de plataforma satelital](../programa/clases/B84/B84-C20-diseno-estructural-de-plataforma-satelital/CLASE.md); [B127-C05 · Evaluación actuarial básica del riesgo espacial](../programa/clases/B127/B127-C05-evaluacion-actuarial-basica-del-riesgo-espacial/CLASE.md).

### Frecuencia angular

- El número de onda `k = 2π/λ` y la frecuencia angular `ω` se relacionan con `ω = ck`: es la relación de dispersión.
- `ω` la frecuencia angular (rad/s);
- La frecuencia angular `ω = 2πf`.

💡 **Contexto en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- **Idea central (modelo mental):** La energía pasa de cinética a potencial y viceversa, como una bola que rueda dentro de un cuenco; si hay roce, cada subida es más baja.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?
- 🔗 **Se estudia junto con:** movimiento armónico simple (MAS), amplitud, fase, fuerza restauradora.

📘 **Dónde se aprende** (3 clases): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md); [B42-C01 · Ecuaciones de onda electromagnética](../programa/clases/B42/B42-C01-ecuaciones-de-onda-electromagnetica/CLASE.md).

### Frecuencia cardiaca

- La frecuencia cardiaca es el número de latidos por minuto (lpm).

💡 **Cómo se explica en la clase [B116-C01](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md):**
- Explicar cómo una señal PPG se convierte en frecuencia cardiaca con un espectro.
- 🎯 **Por qué importa:** Una pulsera que da «72 lpm» no dice «72 ± 0,1». Con movimiento puede dar 120 cuando el pulso real es 70.
- 🔗 **Se estudia junto con:** fotopletismografía (PPG), artefacto de movimiento, resolución espectral, Bland–Altman.

📘 **Dónde se aprende** (1 clase): [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Frecuencia ciclotrónica

- El radio de giro es `r = m v/(|q| B)` y la frecuencia ciclotrónica `f = |q| B/(2π m)`.

💡 **Cómo se explica en la clase [B05-C17](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md):**
- Ejercicio 4. ¿Qué frecuencia ciclotrónica tiene un protón en 50 µT?
- 🎯 **Por qué importa:** La Tierra tiene un campo magnético que un satélite puede medir con un magnetómetro y que actúa sobre las partículas cargadas que lo atraviesan; además, una corriente a bordo crea su propio campo, que puede perturbar esas medidas.
- 🔗 **Se estudia junto con:** campo magnético, fuerza magnética, radio de giro, permeabilidad del vacío.

📘 **Dónde se aprende** (1 clase): [B05-C17 · Campos magnéticos](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md).

### Frecuencia crítica

- La frecuencia crítica `ν_c` es la que acota el espectro de un electrón.
- La frecuencia crítica `foF2` es la de plasma en el máximo de la capa F2: una onda vertical de frecuencia mayor la atraviesa.

💡 **Cómo se explica en la clase [B27-C12](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md):**
- *Descripción textual:* el campo y el factor de Lorentz fijan la potencia, la frecuencia crítica y el tiempo de enfriamiento; el núcleo `F` integrado sobre una población da una ley de potencias.
- Calcular la frecuencia crítica `ν_c = 3γ²eB/(4π m_e)`.
- 🎯 **Por qué importa:** El índice espectral de una fuente sincrotrón entrega el índice de energía de sus electrones; la frecuencia crítica entrega `γ²B`. Sin estas relaciones no se puede leer un espectro de radio o rayos X.
- 🔗 **Se estudia junto con:** radiación sincrotrón, núcleo, índice del electrón, índice espectral.

📘 **Dónde se aprende** (2 clases): [B27-C12 · Radiación sincrotrón](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md); [B89-C22 · Propagación ionosférica y comunicaciones HF](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md).

### Frecuencia de Brunt–Väisälä

- La frecuencia de Brunt–Väisälä `N` es la de oscilación de una burbuja estable.
- La frecuencia de Brunt–Väisälä `N` mide la oscilación de una parcela desplazada en una capa estable (`N² > 0`).

💡 **Contexto en la clase [B37-C08](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md):**
- **Idea central (modelo mental):** Es como un tambor (la tensión restaura: p) y un péndulo (el peso restaura: g). El tambor suena agudo y el péndulo lento; una estrella tiene ambos.
- 🎯 **Por qué importa:** Los modos p y g sondean regiones distintas. La decisión central: ¿en qué cavidad se propaga un modo de frecuencia y grado dados?
- 🔗 **Se estudia junto con:** armónico esférico, modo p, g, frecuencia de Lamb.

📘 **Dónde se aprende** (2 clases): [B37-C08 · Oscilaciones no radiales: modos p, g y mixtos](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md); [B54-C05 · Transporte convectivo](../programa/clases/B54/B54-C05-transporte-convectivo/CLASE.md).

### Frecuencia de ciclotrón

- La frecuencia de ciclotrón `ω_c = q B/m`.

💡 **Cómo se explica en la clase [B78-C08](../programa/clases/B78/B78-C08-propulsores-hall/CLASE.md):**
- Calcular la frecuencia de ciclotrón y el parámetro de Hall clásico.
- 🎯 **Por qué importa:** Sin rejillas no hay límite de Child–Langmuir, pero el propulsor depende de que los electrones giren en un radio pequeño y los iones pasen casi rectos. La decisión central: ¿cuánto vale cada radio de giro frente al largo del canal y qué cambia al subir la tensión?
- 🔗 **Se estudia junto con:** radio de giro, parámetro de Hall, magnetizado, deriva E×B.

📘 **Dónde se aprende** (1 clase): [B78-C08 · Propulsores Hall](../programa/clases/B78/B78-C08-propulsores-hall/CLASE.md).

### Frecuencia de corte

- La frecuencia de corte `D/λ`.

💡 **Contexto en la clase [B42-C07](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md):**
- **Idea central (modelo mental):** Como un filtro de audio que deja pasar graves y corta agudos: la OTF deja pasar las frecuencias espaciales bajas y corta las altas.
- 🎯 **Por qué importa:** La OTF dice qué detalles (frecuencias espaciales) pasan por el sistema y cuáles se pierden; fija el muestreo necesario del detector. La decisión central: ¿hasta qué frecuencia transmite el telescopio y qué muestreo exige?
- 🔗 **Se estudia junto con:** OTF, MTF, autocorrelación, muestreo de Nyquist.

📘 **Dónde se aprende** (1 clase): [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md).

### Frecuencia de cruce

- La frecuencia de cruce `f_c` es el ancho de banda del lazo.

💡 **Cómo se explica en la clase [B92-C03](../programa/clases/B92/B92-C03-adquisicion-apuntamiento-y-seguimiento-opticos/CLASE.md):**
- Un lazo de primer orden con frecuencia de cruce `f_c` la reduce a `σ_d² = (A/f_c)[atan(f₂/f_c) − atan(f₁/f_c)]`: `3,82 µrad` con 10 Hz, `1,21 µrad` con 100 Hz y `0,30 µrad` con 900 Hz.
- Ejercicio 11 · transferencia. Transferencia. Un ingeniero sube la frecuencia de cruce de `300` a `900 Hz` para «seguir mejor».
- 🎯 **Por qué importa:** Un satélite conoce su posición y su actitud con una incertidumbre mucho mayor que el haz de comunicaciones. La decisión central: ¿cómo se cubre la incertidumbre en un tiempo razonable y con qué ancho de banda se cierra el lazo para que el jitter no cueste potencia?
- 🔗 **Se estudia junto con:** adquisición, baliza, seguimiento, jitter.

📘 **Dónde se aprende** (1 clase): [B92-C03 · Adquisición, apuntamiento y seguimiento ópticos](../programa/clases/B92/B92-C03-adquisicion-apuntamiento-y-seguimiento-opticos/CLASE.md).

### Frecuencia de fondo

- La frecuencia de fondo `f_B = 0,03 E^(−4/5)` da los impactos por año con energía al menos `E` Mt [S2].

💡 **Cómo se explica en la clase [B58-C20](../programa/clases/B58/B58-C20-simulador-de-riesgo-de-impacto-basado-en-datos/CLASE.md):**
- F["frecuencia de fondo"] --> S["impactos de Poisson"]
- 🎯 **Por qué importa:** Un simulador convierte reglas sueltas en un flujo reproducible: leer datos, filtrar, calcular y ordenar. La decisión central: ¿qué objetos del catálogo merecen atención primero y qué número de impactos de fondo es coherente con la ley de frecuencias?
- 🔗 **Se estudia junto con:** API SBDB, proceso de Poisson, simulador basado en datos.

📘 **Dónde se aprende** (1 clase): [B58-C20 · Simulador de riesgo de impacto basado en datos](../programa/clases/B58/B58-C20-simulador-de-riesgo-de-impacto-basado-en-datos/CLASE.md).

### Frecuencia de giro

- La frecuencia de giro `ω = |q|B/m`.

💡 **Cómo se explica en la clase [B30-C06](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md):**
- Ejercicio 1 · con los pasos indicados. Frecuencia de giro de un protón en `100 nT`.
- 🎯 **Por qué importa:** El movimiento de las partículas explica cómo se atrapan en los cinturones, cómo derivan y cómo se aceleran. La decisión central: ¿cuándo queda atrapada una partícula y cuánto vale su radio de giro?
- 🔗 **Se estudia junto con:** radio de Larmor, deriva E×B, momento magnético, espejo magnético.

📘 **Dónde se aprende** (1 clase): [B30-C06 · Partículas cargadas y movimientos](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md).

### Frecuencia de la transición hiperfina del cesio-133

- La frecuencia de la transición hiperfina del cesio-133, `Δν_Cs`, es la frecuencia de una radiación atómica concreta que define el segundo.

💡 **Contexto en la clase [B13-C01](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md):**
- **Idea central (modelo mental):** Imagina el SI como un edificio cuyos siete pilares son números exactos. Todo lo demás (unidades derivadas, patrones, instrumentos) se apoya en ellos. Antes de 2019 algunos pilares eran objetos; ahora todos son números.
- 🎯 **Por qué importa:** Una señal de radio o de láser viaja a la Luna y regresa. Para decir «la Luna está a 384 400 km» hay que haber acordado qué es un kilómetro, qué es un segundo y a qué velocidad viaja la señal.
- 🔗 **Se estudia junto con:** Sistema Internacional de Unidades (SI), unidad base, constante definitoria, exacto.

📘 **Dónde se aprende** (1 clase): [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md).

### Frecuencia de Lamb

- La frecuencia de Lamb `L_l = √(l(l+1)) c/r`.

💡 **Contexto en la clase [B37-C08](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md):**
- **Idea central (modelo mental):** Es como un tambor (la tensión restaura: p) y un péndulo (el peso restaura: g). El tambor suena agudo y el péndulo lento; una estrella tiene ambos.
- 🎯 **Por qué importa:** Los modos p y g sondean regiones distintas. La decisión central: ¿en qué cavidad se propaga un modo de frecuencia y grado dados?
- 🔗 **Se estudia junto con:** armónico esférico, modo p, g, frecuencia de Brunt–Väisälä.

📘 **Dónde se aprende** (1 clase): [B37-C08 · Oscilaciones no radiales: modos p, g y mixtos](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md).

### Frecuencia de muestreo

- La frecuencia de muestreo `f_s` es cuántas medidas por segundo se toman; la frecuencia de Nyquist es `f_s/2`.
- La frecuencia de muestreo `f_s = 1/Δt` es cuántas muestras hay por unidad de tiempo.
- La frecuencia de muestreo es `f_s = 1/Δt`.

💡 **Cómo se explica en la clase [B05-C12](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md):**
- Debe incluir las frecuencias reales, `f_s` y Nyquist, los picos estimados, la explicación de cualquier pico falso con `|f − k f_s|` y el criterio de validez del muestreo.
- 🎯 **Por qué importa:** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.
- 🔗 **Se estudia junto con:** onda mecánica, transversal, longitudinal, longitud de onda.

📘 **Dónde se aprende** (3 clases): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md).

### Frecuencia de muestreo fs

- Frecuencia de muestreo `fs`: muestras por segundo.

💡 **Cómo se explica en la clase [B90-C23](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md):**
- Porque el aliasing es un error de muestreo en frecuencia, no de resolución en amplitud.
- 🎯 **Por qué importa:** Un ensayo de vibración que muestrea a 2 048 Hz un tono de 1 500 Hz lo registra como si fuera de 548 Hz y no se nota. La decisión central: ¿qué frecuencia de muestreo, qué filtro y cuántos bits aseguran que lo que se registra es lo que ocurrió?
- 🔗 **Se estudia junto con:** Nyquist, Aliasing, Filtro antialias, Cuantización.

📘 **Dónde se aprende** (1 clase): [B90-C23 · Instrumentación y adquisición de datos en ensayos](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md).

### Frecuencia de Nyquist

- La frecuencia de muestreo `f_s` es cuántas medidas por segundo se toman; la frecuencia de Nyquist es `f_s/2`.
- La frecuencia de Nyquist es `k = N/2`; su modo no tiene derivada bien definida y se anula en la derivada primera.
- La frecuencia de Nyquist es `f_N = f_s/2`, el límite superior de las frecuencias distinguibles; el valor `0,5 ciclos por observación` que describe S2 es el mismo límite expresado en ciclos por muestra.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C12](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md):**
- Debe incluir las frecuencias reales, `f_s` y Nyquist, los picos estimados, la explicación de cualquier pico falso con `|f − k f_s|` y el criterio de validez del muestreo.
- 🎯 **Por qué importa:** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.
- 🔗 **Se estudia junto con:** onda mecánica, transversal, longitudinal, longitud de onda.

📘 **Dónde se aprende** (5 clases): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md); [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md); [B37-C13 · Series fotométricas de Kepler, TESS y PLATO para asterosismología](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md); [B42-C11 · Turbulencia atmosférica](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md).

### Frecuencia de plasma

- La frecuencia de plasma `ω_p = √(n e²/(ε₀ m))` es la de oscilación colectiva.
- La frecuencia de plasma es `f_p = 8,98√N` Hz (con `N` en m⁻³).

💡 **Cómo se explica en la clase [B30-C08](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md):**
- *Descripción textual:* la densidad fija la frecuencia de plasma; de ella salen la relación de dispersión, las velocidades, el retardo y la corrección térmica.
- Con `n = 1 cm⁻³` la frecuencia de plasma es `8978,66 Hz`, que reproduce el coeficiente `8,98 kHz`.
- 🎯 **Por qué importa:** La radiación de las erupciones se emite cerca de la frecuencia de plasma local, de modo que una frecuencia es una altura. La decisión central: ¿qué frecuencia corresponde a cada densidad y cuánto se retrasa una señal?
- 🔗 **Se estudia junto con:** girofrecuencia, velocidad de grupo, velocidad de fase, retardo de grupo.

📘 **Dónde se aprende** (5 clases): [B30-C08 · Frecuencias y ondas de plasma](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md); [B46-C02 · Propagación de ondas de radio](../programa/clases/B46/B46-C02-propagacion-de-ondas-de-radio/CLASE.md); [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md); [B78-C09 · Propulsión por plasma](../programa/clases/B78/B78-C09-propulsion-por-plasma/CLASE.md); [B89-C22 · Propagación ionosférica y comunicaciones HF](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md).

### Frecuencia de Schuler

- La frecuencia de Schuler `ω_s = √(g/R)` es la frecuencia propia de un péndulo de longitud igual al radio de la Tierra; su período es `2π/ω_s`.

💡 **Cómo se explica en la clase [B80-C01](../programa/clases/B80/B80-C01-principios-de-navegacion-inercial-espacial/CLASE.md):**
- Por frecuencia: oscilación de Schuler de `84,4 min`.
- Obtener la frecuencia y el período de Schuler a partir de `g` y del radio.
- 🎯 **Por qué importa:** Una sonda que sale de la cobertura de seguimiento, un lanzador en ascenso o un módulo de aterrizaje en su descenso necesitan saber dónde están sin ayuda externa. B87 trata el giroscopio como sensor de actitud y B74 estima la órbita con observaciones externas; ninguna clase actual enseña cómo se propaga una solución desde una IMU.
- 🔗 **Se estudia junto con:** fuerza específica, navegación inercial, sesgo, Deriva.

📘 **Dónde se aprende** (1 clase): [B80-C01 · Principios de navegación inercial espacial](../programa/clases/B80/B80-C01-principios-de-navegacion-inercial-espacial/CLASE.md).

### Frecuencia del máximo

- La frecuencia del máximo de `B_ν` es `ν_máx = (5,8789 × 10¹⁰ Hz/K) T` (S1).

💡 **Cómo se explica en la clase [B26-C15](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md):**
- Ejercicio 8. Máximo de `B_ν` en `z = 1089` en frecuencia y longitud.
- Predice antes de ejecutar: ¿en qué frecuencia está el máximo?
- 🎯 **Por qué importa:** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.
- 🔗 **Se estudia junto con:** función de Planck, densidad numérica de fotones, energía media, razón barión–fotón.

📘 **Dónde se aprende** (1 clase): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### Frecuencia Doppler

- La frecuencia Doppler `f_D` varía con el tiempo lento `t`.

💡 **Cómo se explica en la clase [B69-C01](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md):**
- La frecuencia Doppler es `f_D = −(1/2π) dφ/dt = 2v²t/(λR)`, que cerca de `t = 0` vale `Ka·t` con `Ka = 2v²/(λR₀)`.
- En ese tiempo la frecuencia Doppler barre `Ba = Ka·T = 2v/L = 1183,3 Hz` (de −591,6 a +591,5 Hz).
- 🎯 **Por qué importa:** Sin el principio Doppler, la resolución en azimut de un radar quedaría fijada por el ancho del haz de la antena: a 850 km, una antena de 12 m (λ = 0,0555 m) iluminaría una franja de unos 3,9 km. La decisión central: ¿qué resolución obtiene el sistema, de qué depende y qué hay que muestrear para no perderla?
- 🔗 **Se estudia junto con:** dirección de azimut, alcance oblicuo, apertura sintética, tasa Doppler.

📘 **Dónde se aprende** (1 clase): [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md).

### Frecuencia en el plano

- `λ` es el exponente inestable real, `ω` la frecuencia en el plano y `ν = √c2` la frecuencia vertical.

💡 **Cómo se explica en la clase [B76-C04](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md):**
- Al crecer la amplitud, la frecuencia del plano baja hasta igualar a la vertical y se abre una familia que sale del plano: la halo.
- 🎯 **Por qué importa:** Una órbita halo no es un círculo: es un compromiso entre un modo inestable y dos oscilaciones. La decisión central: ¿qué dicen los modos lineales de `L2` sobre el tiempo de crecimiento de un error y sobre los periodos de la órbita?
- 🔗 **Se estudia junto con:** ecuación característica, exponente inestable, frecuencia vertical, halo.

📘 **Dónde se aprende** (1 clase): [B76-C04 · Órbitas halo](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md).

### Frecuencia epicíclica

- La frecuencia epicíclica `κ` es la de esa oscilación radial.

💡 **Cómo se explica en la clase [B25-C07](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md):**
- Definir población estelar, órbita circular, epiciclo, frecuencia epicíclica y constantes de Oort.
- 🎯 **Por qué importa:** Las estrellas de una galaxia no giran en círculos perfectos: oscilan alrededor de una órbita circular, y su agitación revela la edad y la historia de la población. Además, no nacen todas con la misma masa: la función de masa inicial fija cuántas hay de cada tipo y cuánta luz y metales producirán.
- 🔗 **Se estudia junto con:** población estelar, órbita circular, epiciclo, radio guía.

📘 **Dónde se aprende** (1 clase): [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### Frecuencia espacial

- La frecuencia espacial `u = sen θ/λ`.

💡 **Contexto en la clase [B42-C04](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md):**
- **Idea central (modelo mental):** Como una chispa que se descompone en frecuencias: una apertura estrecha tiene un patrón ancho y viceversa.
- 🎯 **Por qué importa:** La pupila de un telescopio es una apertura: su forma fija la imagen de una estrella. La decisión central: ¿cómo cambia el patrón cuando cambia la forma o el número de aberturas?
- 🔗 **Se estudia junto con:** transmitancia, rendija, doble rendija, red.

📘 **Dónde se aprende** (1 clase): [B42-C04 · Difracción de aperturas](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md).

### Frecuencia estructural

- La frecuencia estructural `f = √(k/m)/(2π)`.

💡 **Cómo se explica en la clase [B43-C20](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md):**
- *Descripción textual:* las fuentes se suman en cuadratura y se contrastan; el Strehl y la frecuencia estructural se comparan con los requisitos.
- Comparar la frecuencia estructural con el ancho de banda del servo.
- 🎯 **Por qué importa:** El proyecto completo exige que los errores se sumen, se verifiquen y se comparen con los requisitos. La decisión central: ¿qué fuente domina el error, cuánto margen queda y la estructura es lo bastante rígida para el servo?
- 🔗 **Se estudia junto con:** presupuesto de error, suma en cuadratura (RSS), requisito, margen.

📘 **Dónde se aprende** (1 clase): [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md).

### Frecuencia fraccional

- La frecuencia fraccional `y = dx/dt`.

💡 **Contexto en la clase [B46-C08](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md):**
- **Idea central (modelo mental):** Como un reloj cuyo error diario varía: mirando horas, domina el ruido rápido; mirando meses, la deriva lenta.
- 🎯 **Por qué importa:** El tiempo de coherencia de un instrumento depende de cómo se acumula el error de un oscilador. La decisión central: ¿a qué escala de tiempo domina cada tipo de ruido y cuánto se puede integrar?
- 🔗 **Se estudia junto con:** error de tiempo, varianza de Allan, ruido blanco de frecuencia, marcha aleatoria de frecuencia.

📘 **Dónde se aprende** (2 clases): [B46-C08 · Osciladores y estabilidad](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md); [B74-C16 · Sincronización temporal](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md).

### Frecuencia gravitacional

- La frecuencia gravitacional `f_GW = 2/P`.

💡 **Contexto en la clase [B27-C13](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md):**
- **Idea central (modelo mental):** Cada órbita pierde energía, se acerca, orbita más rápido y pierde energía aún más rápido. El tiempo restante cae como `a⁴`, así que la mayor parte de la vida es lenta y los últimos segundos son vertiginosos.
- 🎯 **Por qué importa:** La fusión de dos estrellas de neutrones fue el primer evento detectado en ondas gravitacionales y en luz. Saber cuánto falta para una fusión, a qué frecuencia, y cómo la excentricidad la acelera, es la base de toda búsqueda.
- 🔗 **Se estudia junto con:** masa de chirrido, tiempo de fusión, orden de cuadrupolo, chirrido.

📘 **Dónde se aprende** (1 clase): [B27-C13 · Binarias compactas](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md).

### Frecuencia imagen

- La frecuencia imagen es `2f_LO − f_RF`.

💡 **Contexto en la clase [B46-C07](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md):**
- **Idea central (modelo mental):** Como un espejo que refleja el espectro alrededor del oscilador local: lo que está a un lado y a otro a la misma distancia cae en el mismo sitio.
- 🎯 **Por qué importa:** La mezcla es lo que permite procesar en una banda cómoda, pero trae consigo una segunda frecuencia que cae en la misma FI. La decisión central: ¿qué rechazo de imagen exige el receptor y cómo se logra?
- 🔗 **Se estudia junto con:** mezclador, oscilador local, frecuencia intermedia, rechazo de imagen.

📘 **Dónde se aprende** (1 clase): [B46-C07 · Receptores superheterodinos](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md).

### Frecuencia intermedia

- La frecuencia intermedia (FI) es `|f_RF − f_LO|`.

💡 **Contexto en la clase [B46-C07](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md):**
- **Idea central (modelo mental):** Como un espejo que refleja el espectro alrededor del oscilador local: lo que está a un lado y a otro a la misma distancia cae en el mismo sitio.
- 🎯 **Por qué importa:** La mezcla es lo que permite procesar en una banda cómoda, pero trae consigo una segunda frecuencia que cae en la misma FI. La decisión central: ¿qué rechazo de imagen exige el receptor y cómo se logra?
- 🔗 **Se estudia junto con:** mezclador, oscilador local, frecuencia imagen, rechazo de imagen.

📘 **Dónde se aprende** (1 clase): [B46-C07 · Receptores superheterodinos](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md).

### Frecuencia ISCO

- La frecuencia ISCO es la frecuencia gravitacional en la última órbita estable.

💡 **Contexto en la clase [B28-C07](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md):**
- **Idea central (modelo mental):** El detector tiene una red cuyo radio es el alcance. El número de peces (eventos) crece con el volumen. Si los peces no miran de frente, la red atrapa solo una fracción.
- 🎯 **Por qué importa:** La tasa de eventos detectados depende del volumen que el detector ve, que crece como el cubo del alcance. Una mejora pequeña en sensibilidad se traduce en muchos más eventos.
- 🔗 **Se estudia junto con:** alcance, volumen, tasa, factor de orientación.

📘 **Dónde se aprende** (1 clase): [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md).

### Frecuencia natural

- La frecuencia natural `ω₀ = √(k/m)` es la del sistema libre.
- La frecuencia natural es `ω_n² = −Cm_α q S d/I_y`.
- La frecuencia natural de lazo cerrado es `ω_n² = μ_c Kp − μ_α`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- Planteamiento. Hallar la frecuencia natural del mástil, su energía a 10 mm de amplitud y el efecto de una excitación a esa frecuencia.
- Aquí lo calcularás en dos pasos y verás qué pasa si la excitación coincide con la frecuencia natural.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?
- 🔗 **Se estudia junto con:** movimiento armónico simple (MAS), amplitud, frecuencia angular, fase.

📘 **Dónde se aprende** (7 clases): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B58-C19 · Comunicación pública del riesgo](../programa/clases/B58/B58-C19-comunicacion-publica-del-riesgo/CLASE.md); [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md); [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md) y 1 más.

### Frecuencia óptima

- La frecuencia óptima es aquella en la que ganar apertura eléctrica deja de compensar la pérdida.
- La frecuencia óptima `f* = c/(4πσ)` maximiza la ganancia de una parábola con `σ` fija.

💡 **Cómo se explica en la clase [B89-C06](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md):**
- El script [antena.py](antena.py) calcula la ganancia ideal y efectiva en X y Ka, el haz, las pérdidas por apuntamiento y la frecuencia óptima de Ruze (comprueba que la búsqueda numérica del máximo coincide con `c/(4πσ)` a 1e-3 y que duplicar `D` suma 6,02 dB).
- 🎯 **Por qué importa:** Una antena mal apuntada o con la superficie deformada pierde decibelios que ningún amplificador recupera, y esas pérdidas crecen con la frecuencia. La decisión central: ¿qué ganancia efectiva da una antena y a qué frecuencia deja de compensar subir la frecuencia?
- 🔗 **Se estudia junto con:** ganancia, Ruze, ancho de haz, pérdida por apuntamiento.

📘 **Dónde se aprende** (2 clases): [B89-C06 · Ganancias y pérdidas de antena](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md); [B91-C04 · Antenas desplegables y estructuras de gran apertura](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md).

### Frecuencia orbital

- La frecuencia orbital `f = c³/(2π (r/r_g)^{3/2} GM)`.

💡 **Cómo se explica en la clase [B27-C09](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md):**
- Para `10 M☉`, la frecuencia orbital en el ISCO es `219,9 Hz` y en la esfera de fotones `621,9 Hz` (con `f = c³/(2π (r/r_g)^{3/2} GM)`).
- Calcular frecuencias orbitales en el ISCO y en la esfera de fotones.
- 🎯 **Por qué importa:** La sombra de un agujero negro no es su horizonte: es la imagen de la esfera de fotones ampliada por la curvatura. Y la fórmula `6πM/p` de la precesión solo vale lejos.
- 🔗 **Se estudia junto con:** esfera de fotones, parámetro de impacto crítico, sombra, precesión.

📘 **Dónde se aprende** (1 clase): [B27-C09 · Órbitas en campos fuertes](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md).

### Frecuencia vertical

- `λ` es el exponente inestable real, `ω` la frecuencia en el plano y `ν = √c2` la frecuencia vertical.

💡 **Cómo se explica en la clase [B76-C04](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md):**
- Al crecer la amplitud, la frecuencia del plano baja hasta igualar a la vertical y se abre una familia que sale del plano: la halo.
- Calcular `c2` en `L1` y `L2` y la frecuencia vertical `ν = √c2`.
- 🎯 **Por qué importa:** Una órbita halo no es un círculo: es un compromiso entre un modo inestable y dos oscilaciones. La decisión central: ¿qué dicen los modos lineales de `L2` sobre el tiempo de crecimiento de un error y sobre los periodos de la órbita?
- 🔗 **Se estudia junto con:** ecuación característica, exponente inestable, frecuencia en el plano, halo.

📘 **Dónde se aprende** (1 clase): [B76-C04 · Órbitas halo](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md).

### Frecuencia ν_max

- La frecuencia `ν_max` es la de máxima potencia.

💡 **Contexto en la clase [B37-C09](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md):**
- **Idea central (modelo mental):** Es como los trastes de una guitarra: su separación depende del tamaño del instrumento. Medir la separación de las frecuencias da el tamaño y la masa de la estrella, igual que un luthier mide el diapasón.
- 🎯 **Por qué importa:** Sin Δν y νmax habría que ajustar modelos para saber masa y radio. La decisión central: ¿qué precisión en masa y radio se obtiene con estos observables y qué supuestos exige?
- 🔗 **Se estudia junto con:** separación grande, relación de escala, espaciado de períodos, asintótica.

📘 **Dónde se aprende** (1 clase): [B37-C09 · Frecuencias características: Δν, νmax y espaciado de períodos](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md).

### Frecuencias propias

- Las frecuencias propias `g_k` son los autovalores de `A` y `f_k` los de `B` (inclinaciones; un modo es nulo).

💡 **Cómo se explica en la clase [B73-C11](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md):**
- *Descripción textual:* los datos dan los coeficientes de Laplace, éstos las matrices, y de ellas salen las frecuencias propias, la evolución de `e` y la posición de las resonancias seculares.
- Analogía: dos péndulos unidos por un muelle muy blando intercambian energía lentamente: las frecuencias propias son los modos en que oscilan en conjunto.
- 🎯 **Por qué importa:** La excentricidad de una órbita varía durante millones de años por la atracción promediada de los demás planetas, y esa variación se vuelve violenta cuando una frecuencia propia coincide con la de precesión de un asteroide.
- 🔗 **Se estudia junto con:** teoría de Laplace–Lagrange, coeficientes de Laplace, resonancia secular.

📘 **Dónde se aprende** (1 clase): [B73-C11 · Resonancias seculares](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md).

### Frenador

- Un sobrevuelo es acelerador si `v∞` queda más alineado con la velocidad del planeta y frenador si queda menos.

💡 **Contexto en la clase [B75-C06](../programa/clases/B75/B75-C06-asistencias-gravitacionales/CLASE.md):**
- 🎯 **Por qué importa:** Un cohete que sale de la Tierra no puede llevar combustible para ir a Júpiter con una trayectoria directa de baja energía y además frenar. La decisión central: ¿cuánta velocidad heliocéntrica puede ganar o perder una nave pasando cerca de un planeta, y de qué depende?
- 🔗 **Se estudia junto con:** sobrevuelo, ángulo de giro, periapsis, acelerador.

📘 **Dónde se aprende** (1 clase): [B75-C06 · Asistencias gravitacionales](../programa/clases/B75/B75-C06-asistencias-gravitacionales/CLASE.md).

### Frente de onda

- El frente de onda `W(x,y)`.

💡 **Cómo se explica en la clase [B42-C13](../programa/clases/B42/B42-C13-medicion-de-frente-de-onda/CLASE.md):**
- La evidencia es la ficha de la medición de frente de onda del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de la medición de frente de onda*: método, coeficientes y ruido.
- 🎯 **Por qué importa:** La óptica adaptativa solo corrige lo que mide. La decisión central: ¿qué se mide (pendientes o fase), cuántos modos se ajustan y cuánto ruido llega a los coeficientes?
- 🔗 **Se estudia junto con:** modos de Zernike, matriz de diseño, sensor de pendientes, fase.

📘 **Dónde se aprende** (1 clase): [B42-C13 · Medición de frente de onda](../programa/clases/B42/B42-C13-medicion-de-frente-de-onda/CLASE.md).

### Frente de onda secundario

- El frente de onda secundario: onda esférica (aquí cilíndrica, 2D) emitida por cada punto.

💡 **Contexto en la clase [B42-C02](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md):**
- **Idea central (modelo mental):** Como gotas que caen en cada punto de una rendija de un estanque: cada gota crea ondas circulares y lo que ves lejos es su suma con diferencias de camino.
- 🎯 **Por qué importa:** Sin este principio no hay un procedimiento para calcular qué le pasa a la luz al pasar por una apertura (la pupila de un telescopio es una). La decisión central: ¿a qué distancia vale la aproximación de campo lejano y cuándo hay que sumar las ondas secundarias una por una?
- 🔗 **Se estudia junto con:** apertura, campo lejano, campo cercano, número de Fresnel.

📘 **Dónde se aprende** (1 clase): [B42-C02 · Principio de Huygens-Fresnel](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md).

### Frente de Pareto

- El frente de Pareto es el conjunto de sitios no dominados.
- El frente de Pareto es el conjunto de las opciones no dominadas.
- El frente de Pareto es el conjunto de diseños no dominados.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- *Descripción textual:* los datos de cada sitio se normalizan; los dominados se descartan con el frente de Pareto; los pesos convierten los datos normalizados en un puntaje y un orden; repetir con pesos aleatorios mide qué tan estable es el primero.
- Identificar los sitios dominados (frente de Pareto) y descartarlos sin discutir pesos.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?
- 🔗 **Se estudia junto con:** criterio, normalización min-max, puntaje ponderado, domina.

📘 **Dónde se aprende** (4 clases): [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B78-C20 · Comparación no operativa de arquitecturas de propulsión](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md); [B81-C11 · Optimización multicriterio y frentes de Pareto](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md); [B91-C06 · Selección y compromiso de diseño de antenas](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md).

### Fría

- La redundancia activa (caliente) y la fría (reserva) se diferencian en si la unidad extra funciona desde el principio.
- La redundancia caliente tiene las unidades encendidas a la vez; la fría deja la reserva apagada y sin desgaste hasta conmutar.
- La fría `R_f = r + c·λT·r`, con reserva apagada sin desgaste.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B86-C11](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md):**
- Un paralelo activo sube a `0,9613`, una reserva fría perfecta a `0,9792`, un 2 de 3 a `0,8991`, y un paralelo con `10 %` de causa común cae a `0,9470`.
- Calcular la confiabilidad de un paralelo activo, una reserva fría, una arquitectura 2 de 3 y un paralelo con causa común.
- 🎯 **Por qué importa:** Duplicar un equipo no duplica la confiabilidad ni resuelve todas las fallas: depende de cómo se conmuta, de si las unidades comparten una causa común y de cuánto cuesta en masa y en potencia. La decisión central: ¿qué arquitectura redundante da la confiabilidad necesaria sin pagar más masa y potencia de las debidas?
- 🔗 **Se estudia junto con:** tasa de falla, MTBF, redundancia activa, k de n.

📘 **Dónde se aprende** (4 clases): [B86-C11 · Redundancia eléctrica](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md); [B88-C01 · Arquitectura de computador de vuelo](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md); [B88-C32 · Redundancia fría y caliente: estrategias y conmutación](../programa/clases/B88/B88-C32-redundancia-fria-y-caliente-estrategias-y-conmutacion/CLASE.md); [B93-C04 · Análisis de confiabilidad de electrónica (MTBF y derating)](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md).

### Fricción de Coulomb

- La fricción de Coulomb limita la fuerza tangencial a `μ N`.

💡 **Cómo se explica en la clase [B97-C10](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md):**
- Límite: el contacto es puntual con fricción de Coulomb y sin deformación.
- Límites: fricción de Coulomb con contacto puntual, sin deformación ni dinámica; la órbita se idealiza con `g = 0`.
- 🎯 **Por qué importa:** Un agarre insuficiente deja caer o gira la herramienta; uno excesivo daña el mango. Saber qué carga domina evita diseñar el agarre solo con el peso, error frecuente cuando se reduce la gravedad.
- 🔗 **Se estudia junto con:** par de reacción, carga lineal, fuerza mínima de agarre, factor de seguridad.

📘 **Dónde se aprende** (1 clase): [B97-C10 · Manipulación de herramientas](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md).

### Fricción de Hubble

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B40-C06](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar la fricción de Hubble. Se corrige con 8.3.
- 🎯 **Por qué importa:** La ecuación de estado de un campo decide cómo se diluye y qué domina el universo. La decisión central: ¿qué `w` promedio y qué ley de dilución tiene un campo que oscila en `V ∝ φⁿ`?
- 🔗 **Se estudia junto con:** campo escalar, energía cinética, potencial, ecuación de estado.

📘 **Dónde se aprende** (1 clase): [B40-C06 · Campos escalares en cosmología: potenciales y evolución](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md).

### Fringe stopping

- El fringe stopping: multiplicar por `e^{−iφ_modelo}`.

💡 **Cómo se explica en la clase [B51-C09](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md):**
- P --> S["fringe stopping: quita la fase"]
- La evidencia es la ficha del fringe stopping del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Si se promedia sin detener las franjas, la señal se anula. La decisión central: ¿qué tasa de franjas tiene una fuente, cuánto se pierde al promediar y qué precisión pide el modelo?
- 🔗 **Se estudia junto con:** retardo geométrico, ángulo horario, tasa de franjas, función seno cardinal.

📘 **Dónde se aprende** (1 clase): [B51-C09 · Fringe stopping y rotación de fase por retardo geométrico](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md).

### Frontera

- Una frontera es una celda libre conocida adyacente a una desconocida.

💡 **Cómo se explica en la clase [B97-C16](../programa/clases/B97/B97-C16-autonomia-de-exploracion/CLASE.md):**
- Una frontera es una celda libre conocida con una vecina desconocida; cuando no quedan, la exploración termina.
- Por fronteras gana en `15` de `15` mapas.
- ⚠️ **Error frecuente:** Confundir frontera con obstáculo. Es una celda libre junto a lo desconocido (8.1)
- 🎯 **Por qué importa:** Con retardo de comunicación, el robot que decide qué explorar ahorra horas de operación. Medir cuánto ahorra una estrategia frente a otra permite justificar la autonomía a bordo.
- 🔗 **Se estudia junto con:** cobertura, paseo aleatorio, tope.

📘 **Dónde se aprende** (1 clase): [B97-C16 · Autonomía de exploración](../programa/clases/B97/B97-C16-autonomia-de-exploracion/CLASE.md).

### Frontera de Pareto

- La frontera de Pareto reúne las no dominadas.

💡 **Cómo se explica en la clase [B124-C12](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md):**
- *Descripción textual:* las capacidades y los pesos dan un valor científico que, junto con el costo, define la frontera de Pareto; esta se comprueba con dos algoritmos y se mide su pendiente marginal.
- Calcular la frontera de Pareto de forma exhaustiva y por barrido.
- 🎯 **Por qué importa:** El retorno científico no tiene un precio de mercado, pero se puede razonar con una función de valor explícita y una frontera de eficiencia. La decisión central: ¿qué opciones valen la pena a su costo y cuáles están dominadas?
- 🔗 **Se estudia junto con:** valor científico, rendimientos decrecientes, domina, efectividad.

📘 **Dónde se aprende** (1 clase): [B124-C12 · Evaluación de retorno científico](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md).

### FSPL

- La FSPL es la pérdida en espacio libre.

💡 **Cómo se explica en la clase [B119-C09](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md):**
- Paso 2. Se despeja `FSPL` igual a ese margen.
- Paso 3. `d = 10^((FSPL − 20 log f − 32,45)/20) = 29654 km`.
- 🎯 **Por qué importa:** Ninguna clase anterior vincula el derecho de telecomunicaciones con el cálculo de interferencia; B120 trata licencias y espectro en detalle y esta clase fija el marco.
- 🔗 **Se estudia junto con:** notificación, coordinación, MIFR, interferencia perjudicial.

📘 **Dónde se aprende** (1 clase): [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md).

### Fuente

- La fuente `S` es la tasa de entrada de objetos.

💡 **Cómo se explica en la clase [B118-C10](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md):**
- *Descripción textual:* tres términos (entrada, colisiones, reentrada) determinan la derivada de la población; si la fuente es menor que el valor crítico hay dos equilibrios, y si no, la población crece sin cota.
- Paso 1 · Fuente crítica. `S_c = 1/(4 × 5×10⁻⁷ × 625) = 800`.
- ⚠️ **Error frecuente:** Reducir solo la fuente y olvidar la vida orbital. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El término cuadrático de las colisiones cambia la naturaleza del problema: por debajo de cierta fuente hay un equilibrio estable; por encima, no hay equilibrio. La decisión central: ¿qué parámetro (fuente, vida orbital, tasa de colisión) lleva el sistema al umbral y cómo se lee un escenario sin confundirlo con un pronóstico?
- 🔗 **Se estudia junto con:** escenario, vida orbital, término cuadrático, equilibrio estable.

📘 **Dónde se aprende** (1 clase): [B118-C10 · Síndrome de Kessler como escenario](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md).

### Fuente compacta binaria

- Una fuente compacta binaria es un par de estrellas de neutrones o agujeros negros.

💡 **Contexto en la clase [B28-C07](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md):**
- **Idea central (modelo mental):** El detector tiene una red cuyo radio es el alcance. El número de peces (eventos) crece con el volumen. Si los peces no miran de frente, la red atrapa solo una fracción.
- 🎯 **Por qué importa:** La tasa de eventos detectados depende del volumen que el detector ve, que crece como el cubo del alcance. Una mejora pequeña en sensibilidad se traduce en muchos más eventos.
- 🔗 **Se estudia junto con:** frecuencia ISCO, alcance, volumen, tasa.

📘 **Dónde se aprende** (1 clase): [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md).

### Fuente de irreversibilidad

- Una fuente de irreversibilidad puede ser fricción, mezcla, transferencia de calor con salto finito o estrangulamiento.

💡 **Cómo se explica en la clase [B79-C11](../programa/clases/B79/B79-C11-segunda-ley-y-entropia/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué fuente de irreversibilidad no está en el modelo de turbina?
- 🎯 **Por qué importa:** Ninguna clase del tronco trata entropía ni irreversibilidad, necesarias para entender por qué un compresor real consume más que uno ideal y por qué un choque pierde presión total. La decisión central: ¿cuánta capacidad de trabajo pierde cada componente y por qué mecanismo?
- 🔗 **Se estudia junto con:** segunda ley, isentrópico, trabajo perdido.

📘 **Dónde se aprende** (1 clase): [B79-C11 · Segunda ley y entropía](../programa/clases/B79/B79-C11-segunda-ley-y-entropia/CLASE.md).

### Fuente de Mogi

- La fuente de Mogi es una cavidad esférica pequeña presurizada en un semiespacio elástico.

💡 **Cómo se explica en la clase [B57-C18](../programa/clases/B57/B57-C18-volcanismo-y-monitoreo/CLASE.md):**
- F["fuente d, dV"] --> U["u_z, u_r (Mogi)"]
- Evaluar la deformación vertical y radial de una fuente de Mogi.
- 🎯 **Por qué importa:** Medir la deformación de un volcán permite inferir qué ocurre bajo tierra, pero la inversión no tiene respuesta única. La decisión central: ¿qué profundidad y qué volumen explican la deformación y con qué incertidumbre conjunta?
- 🔗 **Se estudia junto con:** inversión, trade-off.

📘 **Dónde se aprende** (1 clase): [B57-C18 · Volcanismo y monitoreo](../programa/clases/B57/B57-C18-volcanismo-y-monitoreo/CLASE.md).

### Fuente definidora

- Una fuente definidora es la que tiene observaciones suficientes para asegurar su estabilidad y mantiene los ejes (S1, 2.2).

💡 **Contexto en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
- **Idea central (modelo mental):** Imagina fijar un mapa a las fuentes más lejanas, que casi no se mueven. Las coordenadas de cada cuásar son las marcas del mapa; los ejes salen de ellas. Cualquier dirección que midas es relativa a esas marcas; cualquier error común de las marcas es un giro de todo el mapa.
- 🎯 **Por qué importa:** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.
- 🔗 **Se estudia junto con:** Sistema Celeste de Referencia Internacional (ICRS), Marco Celeste de Referencia Internacional (ICRF), cuásar, suelo de ruido.

📘 **Dónde se aprende** (1 clase): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### Fuente en serie

- La fuente en serie representa el campo inducido en una línea.

💡 **Cómo se explica en la clase [B33-C07](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar la fuente en serie. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Una subestación con una corriente de tierra alta puede saturar un transformador. La decisión central: ¿cómo se reparte la corriente inducida entre las subestaciones?
- 🔗 **Se estudia junto con:** análisis nodal, conductancia, corriente de tierra, conservación.

📘 **Dónde se aprende** (1 clase): [B33-C07 · Impactos del clima espacial en redes eléctricas](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md).

### Fuente isótropa

- Una fuente isótropa emite igual en todas direcciones.

💡 **Cómo se explica en la clase [B05-C18](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md):**
- Aplicar la ley del cuadrado inverso al flujo de una fuente isótropa.
- Ejercicio 3. Una fuente isótropa de 10 W: ¿cuánto vale el flujo a 2 m?
- 🎯 **Por qué importa:** Un satélite se comunica con ondas de radio, un telescopio observa luz y rayos X, y la misma radiación a otras energías puede dañar electrónica y tejidos. La pregunta motivadora es: ¿qué es la radiación electromagnética, cómo se ordena por frecuencia y energía, cómo decae con la distancia y qué la hace peligrosa?
- 🔗 **Se estudia junto con:** onda electromagnética, magnitudes, fotón, intensidad o flujo.

📘 **Dónde se aprende** (1 clase): [B05-C18 · Electromagnetismo y radiación](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md).

### Fuente metabólica

- Desgasificación: emisión de gases de un material. Fuente metabólica: CO₂, vapor y trazas de las personas.

💡 **Contexto en la clase [B106-C22](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md):**
- 🎯 **Por qué importa:** Nada sale al exterior de una cabina cerrada: los materiales emiten gases durante meses, los equipos liberan trazas y las personas emiten vapor y CO₂. La decisión central: ¿qué fuentes dominan en cada momento y cómo se identifican los compuestos para decidir qué retirar?
- 🔗 **Se estudia junto con:** Desgasificación, Espectro de masas, Biblioteca, NNLS.

📘 **Dónde se aprende** (1 clase): [B106-C22 · Fuentes e identificación de contaminantes del aire de cabina](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md).

### Fuente oficial

- Una fuente oficial es la de una institución responsable de un estándar o de datos (BIPM, IAU, NASA, ESA, ESO).

💡 **Cómo se explica en la clase [B01-C19](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md):**
- Una ficha de NASA es una fuente oficial de datos, pero tiene fecha de actualización (la del planeta es del 18 de marzo de 2025) y su fila de distancia no se rotula como semieje mayor (C13): oficial no significa infalible.
- Imagina una escalera en la que cada peldaño es una fuente: abajo, el dato primario con su método y su versión; encima, la documentación oficial; después, los resúmenes y la prensa; arriba del todo, una publicación en redes.
- 🎯 **Por qué importa:** Un titular dice: «Neutrinos superan la velocidad de la luz: Einstein estaba equivocado». Es una afirmación fuerte.
- 🔗 **Se estudia junto con:** fuente primaria, fuente secundaria, preprint, trazabilidad.

📘 **Dónde se aprende** (1 clase): [B01-C19 · Fuentes confiables y desinformación espacial](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md).

### Fuente primaria

- Una fuente primaria es el origen del dato: el artículo con la medición, el catálogo, la ficha de la misión.
- Una fuente primaria es un documento de la propia misión o agencia; una de divulgación resume a otras.
- Una fuente primaria es el documento original.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C19](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md):**
- Predice antes: ¿qué porcentaje de afirmaciones del titular podrás respaldar con una fuente primaria?
- 🎯 **Por qué importa:** Un titular dice: «Neutrinos superan la velocidad de la luz: Einstein estaba equivocado». Es una afirmación fuerte.
- 🔗 **Se estudia junto con:** fuente oficial, fuente secundaria, preprint, trazabilidad.

📘 **Dónde se aprende** (4 clases): [B01-C19 · Fuentes confiables y desinformación espacial](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md); [B104-C01 · Historia de vuelos tripulados](../programa/clases/B104/B104-C01-historia-de-vuelos-tripulados/CLASE.md); [B119-C12 · Historia de competencia estratégica espacial](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md); [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Fuente puntual

- Una fuente puntual es un modelo sin tamaño que emite igual en todas las direcciones.
- Una fuente puntual es la que el instrumento no resuelve (una estrella); un objeto extenso (la Luna, una nebulosa) no cumple las reglas de esta clase.

💡 **Cómo se explica en la clase [B03-C10](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md):**
- Estas cifras no son medidas: son calculadas con el modelo de fuente puntual a partir del valor nominal.
- Límites: fuente puntual; órbitas circulares de semieje medio; sin atmósfera.
- 🎯 **Por qué importa:** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?
- 🔗 **Se estudia junto con:** directamente proporcionales, inversamente proporcionales, constante de proporcionalidad, lineal.

📘 **Dónde se aprende** (2 clases): [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md); [B08-C11 · Magnitudes aparentes y brillo](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md).

### Fuente secundaria

- Una fuente secundaria resume o comenta (prensa, divulgación, enciclopedias).

💡 **Contexto en la clase [B01-C19](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md):**
- **Idea central (modelo mental):** Imagina una escalera en la que cada peldaño es una fuente: abajo, el dato primario con su método y su versión; encima, la documentación oficial; después, los resúmenes y la prensa; arriba del todo, una publicación en redes. Cuanto más arriba, más lejos del dato y más pasos de interpretación.
- 🎯 **Por qué importa:** Un titular dice: «Neutrinos superan la velocidad de la luz: Einstein estaba equivocado». Es una afirmación fuerte.
- 🔗 **Se estudia junto con:** fuente primaria, fuente oficial, preprint, trazabilidad.

📘 **Dónde se aprende** (1 clase): [B01-C19 · Fuentes confiables y desinformación espacial](../programa/clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md).

### Fuente tardía

- Una fuente tardía es un texto escrito mucho después del autor del que informa.

💡 **Cómo se explica en la clase [B02-C03](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md):**
- Una fuente tardía transmite el método, pero puede simplificarlo.
- Distinguir fuente primaria, fuente tardía y reconstrucción moderna.
- ⚠️ **Error frecuente:** Olvidar que la fuente es tardía. Ejercicio 8.
- 🎯 **Por qué importa:** Un modelo geométrico responde a «¿qué figura reproduce estos movimientos?». Es una forma nueva de preguntar frente a la regla puramente numérica.
- 🔗 **Se estudia junto con:** circunferencia, estadio, meridiano, precesión de los equinoccios.

📘 **Dónde se aprende** (1 clase): [B02-C03 · Astronomía griega y helenística](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md).

### Fuente turística

- Una fuente turística es la de un portal de visitantes, útil para localizar pero débil como evidencia.

💡 **Cómo se explica en la clase [B02-C04](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md):**
- Reconocer cuándo una fuente es turística, enciclopédica o académica.
- Ejercicio 6. Clasifica S1 a S7 por tipo de fuente (institucional, académica, turística, secundaria académica).
- 🎯 **Por qué importa:** Contar la historia de la astronomía como una línea recta de Grecia a Europa deja fuera lo que otras sociedades observaron, calcularon y construyeron. La pregunta motivadora es: ¿qué sabemos con precisión de estas tradiciones, qué falta y cómo evitar contar la historia desde un solo lado?
- 🔗 **Se estudia junto con:** estrella visitante, instrumento, gnomon, cuadrante.

📘 **Dónde se aprende** (1 clase): [B02-C04 · Astronomía de India, China y mundo islámico](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md).

### Fuente y víctima

- EMI: interferencia electromagnética. Fuente y víctima: quien emite y quien sufre.

💡 **Contexto en la clase [B90-C14](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md):**
- 🎯 **Por qué importa:** Un transmisor de 1 W deja un armónico de −30 dBm; el piso de ruido de un receptor estrecho está cerca de −132 dBm. La diferencia de más de 100 dB se pierde con facilidad en un chasis de 10 cm.
- 🔗 **Se estudia junto con:** EMI, Piso de ruido, I/N, Desensibilización.

📘 **Dónde se aprende** (1 clase): [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md).

### Fuera de límites

- Un valor fuera de límites (OOL) activa una alarma.

💡 **Cómo se explica en la clase [B83-C19](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md):**
- Aplicar límites amarillo y rojo y contar muestras fuera de límites.
- 🎯 **Por qué importa:** Un satélite entregado con una base de datos errónea muestra valores falsos o alarmas inútiles; operadores sin entrenamiento no saben responder. La decisión central: ¿la base de datos, los comandos y las personas están listos, de modo que operaciones pueda recibir el sistema?
- 🔗 **Se estudia junto con:** base de datos de telemetría y comandos, calibración polinómica, aceptación, transferencia a operaciones.

📘 **Dónde se aprende** (1 clase): [B83-C19 · Aceptación y transferencia a operaciones](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md).

### Fuera del art. IV

- Condicionado significa permitido solo con el propósito científico o pacífico. Fuera del art. IV significa que el artículo no la regula expresamente (no que esté permitida).

💡 **Cómo se explica en la clase [B119-C11](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md):**
- Resultado: `14` prohibidas, `1` condicionadas, `1` permitidas y `8` fuera del art.
- ADM en órbita: prohibido; base militar en la Luna: prohibido; científicos militares en la Luna: condicionado; telescopio civil en un asteroide: permitido; satélite de observación en órbita: fuera del art.
- 🎯 **Por qué importa:** C01 reduce el art. IV a una regla booleana; esta clase lo desagrega por ubicación y propósito y conecta con el art. 3 del Acuerdo sobre la Luna, y deja explícito lo no consultado.
- 🔗 **Se estudia junto con:** ADM, Condicionado, cuerpo celeste, lista de reglas.

📘 **Dónde se aprende** (1 clase): [B119-C11 · Uso pacífico y limitaciones militares](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md).

### Fuerte

- La condición de energía débil pide `ρ ≥ 0` y `ρ + p ≥ 0`; la dominante, `ρ ≥ |p|`; la fuerte, `ρ + 3p ≥ 0`.
- La solución débil del choque oblicuo tiene `M₂ > 1` (casi siempre); la fuerte, `M₂ < 1`.

💡 **Cómo se explica en la clase [B39-C04](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md):**
- Ejercicio 6. ¿Cumple la constante cosmológica la condición fuerte?
- ecuacion de estado w = p/rho debil dominante fuerte
- 🎯 **Por qué importa:** La fuente de la gravedad es `T^ab`. La decisión central: ¿qué tensor describe la materia y qué condiciones debe cumplir para ser físicamente razonable?
- 🔗 **Se estudia junto con:** fluido perfecto, densidad, presión, parámetro.

📘 **Dónde se aprende** (2 clases): [B39-C04 · Tensor de energía-momento y fuentes de curvatura](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md); [B79-C07 · Ondas de choque normales y oblicuas](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md).

### Fuerza

- La fuerza `F` es una interacción que cambia el estado de movimiento; es un vector, con unidad newton (N).

💡 **Cómo se explica en la clase [B05-C04](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md):**
- Un cuerpo sobre el que la fuerza neta es cero conserva su velocidad (reposo o recta con rapidez constante).
- La aceleración tiene la dirección de la fuerza neta y módulo `|ΣF|/m`.
- ⚠️ **Error frecuente:** Pensar que la fuerza es necesaria para mantener el movimiento. Ejercicio 7.
- 🎯 **Por qué importa:** Un satélite no tiene motor encendido y aun así gira. Una nave en el espacio vacío mantiene su velocidad sin esfuerzo.
- 🔗 **Se estudia junto con:** masa inercial, fuerza neta, marco inercial, peso.

📘 **Dónde se aprende** (1 clase): [B05-C04 · Leyes del movimiento de Newton](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md).

### Fuerza aerodinámica

- La fuerza aerodinámica se descompone en arrastre `D = Cd·q·A` y sustentación `L = CL·q·A`.

💡 **Cómo se explica en la clase [B77-C03](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md):**
- python programa/clases/B77/B77-C03-fuerzas-aerodinamicas/presion_dinamica.py
- 🎯 **Por qué importa:** El momento de mayor carga aerodinámica no es el de mayor velocidad ni el de menor altitud. La decisión central: ¿cuándo ocurre el máximo de la presión dinámica y qué fuerzas produce?
- 🔗 **Se estudia junto con:** presión dinámica, arrastre, sustentación, Max-q.

📘 **Dónde se aprende** (1 clase): [B77-C03 · Fuerzas aerodinámicas](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md).

### Fuerza bruta

- La fuerza bruta compara con todo.
- La fuerza bruta compara todos los pares.

💡 **Cómo se explica en la clase [B14-C28](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md):**
- «¿Qué escenas contienen el punto (180°, 0°)?» se resuelve con una unión entre el índice y la tabla de nombres: 3 escenas, igual que la fuerza bruta.
- No es una comparación válida: es una medición única (no el mejor de varias, C14), con NumPy vectorizado y 50 000 cajas, un tamaño en el que la fuerza bruta aún es barata.
- ⚠️ **Error frecuente:** No verificar contra fuerza bruta. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.
- 🔗 **Se estudia junto con:** índice espacial, R-tree, tabla virtual, consulta de solapamiento.

📘 **Dónde se aprende** (2 clases): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md); [B119-C13 · Vigilancia y conciencia situacional espacial](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md).

### Fuerza central

- La fuerza central no genera torque respecto del centro.

💡 **Cómo se explica en la clase [B71-C06](../programa/clases/B71/B71-C06-momento-angular-especifico/CLASE.md):**
- F["fuerza central"] --> T["torque nulo"]
- *Descripción textual:* una fuerza central no ejerce torque, por lo que `h` es constante; de ahí salen el plano fijo, la ley de las áreas, el semilado recto y la velocidad transversal.
- 🎯 **Por qué importa:** Si `h` es constante, el movimiento ocurre en un plano y la velocidad en el periapsis y el apoapsis queda ligada a la distancia. La decisión central: ¿qué dice `h` sobre la forma y la orientación de la órbita y cómo se usa para obtener velocidades?
- 🔗 **Se estudia junto con:** momento angular específico, semilado recto, velocidad areolar, velocidad transversal.

📘 **Dónde se aprende** (1 clase): [B71-C06 · Momento angular específico](../programa/clases/B71/B71-C06-momento-angular-especifico/CLASE.md).

### Fuerza de arrastre

- La fuerza de arrastre `K` mide cuánto corrige la luz.

💡 **Cómo se explica en la clase [B105-C08](../programa/clases/B105/B105-C08-sueno-y-ritmos-circadianos/CLASE.md):**
- *Descripción textual:* el periodo de la luz fija el desajuste con el reloj; la ecuación de Adler lo compara con la fuerza de arrastre y da bloqueo de fase o deriva con un periodo de batido.
- Un reloj de periodo intrínseco 24,2 h con fuerza de arrastre `K = 0,01 rad/h` (ambos ilustrativos) se sincroniza con ciclos de luz de periodo entre 23,30 y 25,17 h.
- 🎯 **Por qué importa:** En órbita hay unos 16 amaneceres al día: la luz externa no sirve de reloj. La decisión central: ¿qué ciclo de luz puede sincronizar a un reloj de periodo 24,2 h con una fuerza de arrastre dada y cuánto tarda en realinearse tras un salto?
- 🔗 **Se estudia junto con:** fase, desajuste, bloqueo de fase, periodo de batido.

📘 **Dónde se aprende** (1 clase): [B105-C08 · Sueño y ritmos circadianos](../programa/clases/B105/B105-C08-sueno-y-ritmos-circadianos/CLASE.md).

### Fuerza de avance

- La fuerza de avance es la suma, sin valores negativos (sin regeneración en este modelo).

💡 **Cómo se explica en la clase [B100-C05](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md):**
- Calcular la fuerza de avance con rodadura y pendiente.
- Ejercicio 7 · autónomo. ¿A qué pendiente de bajada se anula la fuerza de avance?
- 🎯 **Por qué importa:** Mover una tonelada un kilómetro cuesta energía, y esa energía depende de la gravedad, del suelo y de la pendiente. La decisión central: ¿cuánta carga y qué ruta permiten llegar con la batería disponible, y cuánto cambia el costo entre la Luna y Marte?
- 🔗 **Se estudia junto con:** resistencia a la rodadura, fuerza de pendiente, energía, alcance.

📘 **Dónde se aprende** (1 clase): [B100-C05 · Transporte de carga sobre superficie planetaria](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md).

### Fuerza de banda

- La fuerza de banda `A` (cm por molécula) relaciona el área de la banda con el número de moléculas.

💡 **Cómo se explica en la clase [B55-C06](../programa/clases/B55/B55-C06-hielos-astrofisicos/CLASE.md):**
- Un ±20 % en `A` cambia `N` entre +25 % y −17 %: la fuerza de banda domina el error, no el ruido.
- A["fuerza de banda A (cm/molécula)"] --> N["N = ∫τ dν̃ / A"]
- ⚠️ **Error frecuente:** Olvidar que la fuerza de banda domina el error. Se muestra en 8.4.
- 🎯 **Por qué importa:** Los hielos de los granos guardan gran parte de la química fría y se estudian por su absorción infrarroja. Para comparar con modelos hay que convertir una banda en moléculas por cm².
- 🔗 **Se estudia junto con:** profundidad óptica, densidad de columna, FWHM, monocapa.

📘 **Dónde se aprende** (1 clase): [B55-C06 · Hielos astrofísicos](../programa/clases/B55/B55-C06-hielos-astrofisicos/CLASE.md).

### Fuerza de corte

- La fuerza de corte es la resistencia del suelo a la cuchara.

💡 **Cómo se explica en la clase [B97-C25](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md):**
- *Descripción textual:* la fuerza de corte del suelo y la reacción máxima de la máquina se igualan para dar la profundidad máxima, que fija el volumen y la productividad.
- Calcular la fuerza de corte por una ecuación de capacidad con cohesión y peso del suelo.
- 🎯 **Por qué importa:** Una excavadora diseñada y probada en la Tierra puede ser incapaz de cortar en la Luna por falta de reacción, no por falta de potencia. Es un error de diseño caro que un cálculo de pocos renglones evita.
- 🔗 **Se estudia junto con:** reacción máxima, profundidad máxima, ciclo, productividad.

📘 **Dónde se aprende** (1 clase): [B97-C25 · Excavación y manejo de regolito con robots](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md).

### Fuerza de línea

- La fuerza de línea `S` es el factor de geometría (suma sobre orientaciones); para una transición `J→J−1` de molécula lineal, `S = J` (con `J` el nivel superior).

💡 **Cómo se explica en la clase [B62-C04](../programa/clases/B62/B62-C04-momentos-dipolares-y-fuerza-de-linea/CLASE.md):**
- M["μ (D)"] --> S["fuerza de línea S = J"]
- Aplicar la fuerza de línea `S = J` y la ecuación de intensidad del catálogo JPL.
- 🎯 **Por qué importa:** Una frecuencia identifica la especie, pero solo la intensidad dice cuánta hay. Y la intensidad contiene `μ²`: un error del 10 % en el dipolo es un 20 % en la cantidad de moléculas.
- 🔗 **Se estudia junto con:** momento dipolar permanente, coeficiente de Einstein A, intensidad integrada, vida radiativa.

📘 **Dónde se aprende** (1 clase): [B62-C04 · Momentos dipolares y fuerza de línea](../programa/clases/B62/B62-C04-momentos-dipolares-y-fuerza-de-linea/CLASE.md).

### Fuerza de marea

- La fuerza de marea es la diferencia de atracción entre dos puntos de un cuerpo extenso.

💡 **Contexto en la clase [B25-C12](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md):**
- **Idea central (modelo mental):** Piensa en dos bailarines que pasan cerca; las personas que giran alrededor de cada uno quedan arrastradas o cambian de pareja. Analogía: las personas alrededor son las estrellas del disco y el paso cercano, el pericentro.
- 🎯 **Por qué importa:** Las galaxias no evolucionan aisladas: se atraen, se deforman y a veces se funden. Muchas elípticas masivas pueden provenir de fusiones, y los encuentros llevan gas al centro, alimentando la formación estelar y los núcleos activos de C11.
- 🔗 **Se estudia junto con:** interacción, fusión, cola de marea, órbita parabólica.

📘 **Dónde se aprende** (1 clase): [B25-C12 · Interacciones y fusiones galácticas](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md).

### Fuerza de oscilador

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B45-C11](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md):**
- **Idea central (modelo mental):** Como cerrar una persiana: las primeras láminas oscurecen mucho; cuando ya está casi cerrada, más láminas apenas cambian la luz.
- 🎯 **Por qué importa:** Las líneas de absorción dan abundancias, pero las líneas fuertes no son proporcionales a la cantidad de átomos. La decisión central: ¿en qué régimen está la línea y cómo se obtiene la columna?
- 🔗 **Se estudia junto con:** profundidad óptica, transmisión, ancho equivalente, curva de crecimiento.

📘 **Dónde se aprende** (1 clase): [B45-C11 · Líneas de absorción](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md).

### Fuerza de pendiente

- La fuerza de pendiente es `m g sin θ`.

💡 **Cómo se explica en la clase [B100-C05](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md):**
- *Descripción textual:* la gravedad, la masa y la pendiente de cada arista dan su fuerza y su energía; con esos costos, Dijkstra y Bellman–Ford encuentran la ruta de mínima energía y se comparan entre sí.
- Calcular la fuerza de avance con rodadura y pendiente.
- 🎯 **Por qué importa:** Mover una tonelada un kilómetro cuesta energía, y esa energía depende de la gravedad, del suelo y de la pendiente. La decisión central: ¿cuánta carga y qué ruta permiten llegar con la batería disponible, y cuánto cambia el costo entre la Luna y Marte?
- 🔗 **Se estudia junto con:** resistencia a la rodadura, fuerza de avance, energía, alcance.

📘 **Dónde se aprende** (1 clase): [B100-C05 · Transporte de carga sobre superficie planetaria](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md).

### Fuerza de reacción

- La fuerza de reacción `F = m a`.

💡 **Cómo se explica en la clase [B105-C16](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md):**
- Calcular una fuerza de reacción `F = m a` y compararla con el peso.
- El script [ejercicio.py](ejercicio.py) calcula la energía por MET, la fuerza de reacción, ajusta una curva de Hill a datos sintéticos y traduce la reducción en pérdida ósea a 6 meses (comprueba `R(L50) = Rmax/2`, los 900 kcal y que el ajuste recupera `Rmax` y `L50` dentro de tolerancia).
- 🎯 **Por qué importa:** Más ejercicio ayuda, pero con rendimientos decrecientes y con un costo de energía y tiempo. La decisión central: ¿qué parte de la pérdida se evita con una carga dada y cuánta energía extra exige?
- 🔗 **Se estudia junto con:** MET, carga semanal, curva de Hill, reducción relativa.

📘 **Dónde se aprende** (1 clase): [B105-C16 · Contramedidas de ejercicio](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md).

### Fuerza específica

- La fuerza específica `f` es lo que mide un acelerómetro: `f = a − g`, aceleración total menos la gravitacional.

💡 **Cómo se explica en la clase [B80-C01](../programa/clases/B80/B80-C01-principios-de-navegacion-inercial-espacial/CLASE.md):**
- Un acelerómetro mide la fuerza específica `f`, no la aceleración.
- F["Fuerza específica f"] --> V["Integrar: velocidad"]
- 🎯 **Por qué importa:** Una sonda que sale de la cobertura de seguimiento, un lanzador en ascenso o un módulo de aterrizaje en su descenso necesitan saber dónde están sin ayuda externa. B87 trata el giroscopio como sensor de actitud y B74 estima la órbita con observaciones externas; ninguna clase actual enseña cómo se propaga una solución desde una IMU.
- 🔗 **Se estudia junto con:** navegación inercial, sesgo, frecuencia de Schuler, Deriva.

📘 **Dónde se aprende** (1 clase): [B80-C01 · Principios de navegación inercial espacial](../programa/clases/B80/B80-C01-principios-de-navegacion-inercial-espacial/CLASE.md).

### Fuerza externa F_ext

- Inercia deseada `M_d`: kg. Fuerza externa `F_ext`: fuerza de la pared sobre el extremo.

💡 **Contexto en la clase [B101-C07](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md):**
- 🎯 **Por qué importa:** Si un brazo muy rígido empuja una pieza que está 5 mm más lejos de lo que cree, aplica una fuerza grande. La decisión central: ¿qué rigidez y qué amortiguamiento le doy al extremo para que el contacto sea suave y la fuerza predecible?
- 🔗 **Se estudia junto con:** Impedancia, Rigidez deseada K_d, Amortiguamiento B_d, Inercia deseada M_d.

📘 **Dónde se aprende** (1 clase): [B101-C07 · Control de fuerza e impedancia en manipulación](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md).

### Fuerza iónica

- La fuerza iónica `I = ½Σ c z²` mide la «carga» del conjunto de iones.

💡 **Contexto en la clase [B115-C03](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md):**
- 🎯 **Por qué importa:** Una solución nutritiva que se repone «por conductividad» puede parecer estable y estar desequilibrada. La decisión central: ¿qué se mide, cada cuánto y qué se repone para que cada ion se mantenga cerca de su objetivo, y cuándo conviene renovar la solución?
- 🔗 **Se estudia junto con:** solución nutritiva, macronutrientes, micronutrientes, solución madre.

📘 **Dónde se aprende** (1 clase): [B115-C03 · Control de nutrientes y solución nutritiva](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md).

### Fuerza magnética

- La fuerza magnética sobre una carga `q` con velocidad `v` es `F = q v × B`, de módulo `q v B sen θ` y perpendicular a `v` y a `B`.

💡 **Cómo se explica en la clase [B05-C17](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md):**
- La fuerza magnética siempre es perpendicular a la velocidad: no empuja ni frena, solo desvía.
- Su límite: la tensión es una fuerza de contacto; la fuerza magnética actúa a distancia y solo sobre cargas.
- 🎯 **Por qué importa:** La Tierra tiene un campo magnético que un satélite puede medir con un magnetómetro y que actúa sobre las partículas cargadas que lo atraviesan; además, una corriente a bordo crea su propio campo, que puede perturbar esas medidas.
- 🔗 **Se estudia junto con:** campo magnético, radio de giro, frecuencia ciclotrónica, permeabilidad del vacío.

📘 **Dónde se aprende** (1 clase): [B05-C17 · Campos magnéticos](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md).

### Fuerza máxima

- La tensión específica `σ` es la fuerza por área, y la fuerza máxima es `F = σ A`.

💡 **Cómo se explica en la clase [B105-C03](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md):**
- *Descripción textual:* la carga y el aporte reducidos dejan un balance proteico negativo; la reserva decae de forma exponencial, el área baja y la fuerza máxima con ella, y se compara con lo que exige una tarea.
- Convertir sección transversal en fuerza máxima con una tensión específica.
- 🎯 **Por qué importa:** Sin carga y sin aporte adecuado, el músculo se pierde más rápido que en la Tierra. La decisión central: ¿cuánta área y cuánta fuerza quedan tras 30, 90 y 180 días, y cuánto cambia una contramedida?
- 🔗 **Se estudia junto con:** atrofia, balance proteico, tensión específica, contramedida.

📘 **Dónde se aprende** (1 clase): [B105-C03 · Atrofia muscular](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md).

### Fuerza mínima de agarre

- La fuerza mínima de agarre es la que hace que cada dedo no resbale.

💡 **Cómo se explica en la clase [B97-C10](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md):**
- La fuerza mínima de agarre es `102,11` N en la Tierra, `100,36` N en Marte, `100,09` N en la Luna y `100,00` N en órbita: casi igual en todas porque domina el par.
- Descripción larga: con un par de reacción de 2 N·m el agarre casi no depende de la gravedad; sin ese par, la fuerza mínima caería con ella.
- 🎯 **Por qué importa:** Un agarre insuficiente deja caer o gira la herramienta; uno excesivo daña el mango. Saber qué carga domina evita diseñar el agarre solo con el peso, error frecuente cuando se reduce la gravedad.
- 🔗 **Se estudia junto con:** fricción de Coulomb, par de reacción, carga lineal, factor de seguridad.

📘 **Dónde se aprende** (1 clase): [B97-C10 · Manipulación de herramientas](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md).

### Fuerza neta

- La fuerza neta `ΣF` es la suma vectorial de todas las fuerzas sobre el cuerpo.

💡 **Cómo se explica en la clase [B05-C04](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md):**
- Un cuerpo sobre el que la fuerza neta es cero conserva su velocidad (reposo o recta con rapidez constante).
- La aceleración tiene la dirección de la fuerza neta y módulo `|ΣF|/m`.
- 🎯 **Por qué importa:** Un satélite no tiene motor encendido y aun así gira. Una nave en el espacio vacío mantiene su velocidad sin esfuerzo.
- 🔗 **Se estudia junto con:** fuerza, masa inercial, marco inercial, peso.

📘 **Dónde se aprende** (1 clase): [B05-C04 · Leyes del movimiento de Newton](../programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/CLASE.md).

### Fuerza no gravitacional

- Una fuerza no gravitacional es un empuje por la salida de gas que altera la órbita.

💡 **Cómo se explica en la clase [B58-C04](../programa/clases/B58/B58-C04-nucleos-y-colas-cometarias/CLASE.md):**
- El gas que sale ejerce un empuje reactivo (fuerza no gravitacional); su tamaño depende de `Z`.
- 🎯 **Por qué importa:** La actividad de un cometa cambia su órbita (empujes no gravitacionales) y su brillo, y decide qué se observa. La decisión central: ¿a qué distancia del Sol el hielo empieza a sublimar de forma apreciable y qué tamaño de grano barre la radiación?
- 🔗 **Se estudia junto con:** sublimación, coma, cola de polvo, cola de iones.

📘 **Dónde se aprende** (1 clase): [B58-C04 · Núcleos y colas cometarias](../programa/clases/B58/B58-C04-nucleos-y-colas-cometarias/CLASE.md).

### Fuerza pico

- Sobreimpulso: exceso máximo sobre el valor final. Fuerza pico: máximo de la fuerza de contacto.

💡 **Cómo se explica en la clase [B101-C07](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md):**
- Un impacto a 0,05 m/s contra la pared (`K_d = 1 000`) da una fuerza pico menor que la cota sin amortiguamiento `k_e (x_eq + √(x_eq² + M_d v_c²/(K_d + k_e)))`, donde `v_c` es la velocidad al tocar:
- Calcular una cota de la fuerza pico en un impacto.
- ⚠️ **Error frecuente:** Olvidar el amortiguamiento en el impacto. Mira la fuerza pico (8.4)
- 🎯 **Por qué importa:** Si un brazo muy rígido empuja una pieza que está 5 mm más lejos de lo que cree, aplica una fuerza grande. La decisión central: ¿qué rigidez y qué amortiguamiento le doy al extremo para que el contacto sea suave y la fuerza predecible?
- 🔗 **Se estudia junto con:** Impedancia, Rigidez deseada K_d, Amortiguamiento B_d, Inercia deseada M_d.

📘 **Dónde se aprende** (1 clase): [B101-C07 · Control de fuerza e impedancia en manipulación](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md).

### Fuerza protonmotriz

- La fuerza protonmotriz `Δp` es la energía por carga almacenada en el gradiente de protones.

💡 **Cómo se explica en la clase [B64-C05](../programa/clases/B64/B64-C05-acidofilos-y-alcalofilos/CLASE.md):**
- En el alcalófilo el pH interno es menor que el externo y el término de pH se suma con signo opuesto: la fuerza protonmotriz del ejemplo es pequeña y de signo positivo; cómo producen ATP estos organismos es una cuestión que no se trata aquí (no consultado).
- *Descripción textual:* el potencial de membrana y los pH dan la fuerza protonmotriz; los pH y el pKa fijan cuánto de un ácido débil se acumula dentro, lo que se verifica simulando la permeación de la forma neutra.
- 🎯 **Por qué importa:** Un acidófilo vive en un medio miles de veces más ácido que su citoplasma. La pregunta motivadora: ¿cómo mantiene una célula un interior casi neutro y qué le cuesta?
- 🔗 **Se estudia junto con:** acidófilo, alcalófilo, atrapamiento.

📘 **Dónde se aprende** (1 clase): [B64-C05 · Acidófilos y alcalófilos](../programa/clases/B64/B64-C05-acidofilos-y-alcalofilos/CLASE.md).

### Fuerza restauradora

- La fuerza restauradora apunta al equilibrio y es proporcional al desplazamiento: `F = −k x` (ley de Hooke), con `k` la rigidez (N/m).

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- Para un péndulo de longitud `L`, la fuerza restauradora es `−m g sen θ`.
- A["Desplazamiento x"] --> B["Fuerza restauradora F = −k x"]
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?
- 🔗 **Se estudia junto con:** movimiento armónico simple (MAS), amplitud, frecuencia angular, fase.

📘 **Dónde se aprende** (1 clase): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md).

### Fuga

- La fuga E→B es la potencia de B espuria que produce una máscara.
- Una fuga es transmisión residual fuera de banda.
- La fuga es la señal que pasa al puerto de salida sin mezclar.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B40-C08](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md):**
- Las dos máscaras no tienen la misma área, así que la comparación indica la dirección (apodizar reduce la fuga) y no una ley cuantitativa.
- Descripción larga: apodizar reduce la fuga a la mitad aproximadamente.
- ⚠️ **Error frecuente:** Medir B en un mapa enmascarado sin corregir la fuga. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un modo B primordial sería una huella de ondas gravitacionales, pero las máscaras filtran E hacia B. La decisión central: ¿cómo se separan E y B y cuánto contamina una máscara?
- 🔗 **Se estudia junto con:** modo E, modo B, parámetros de Stokes, ángulo.

📘 **Dónde se aprende** (6 clases): [B40-C08 · Polarización E y B del fondo cósmico](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md); [B45-C03 · Curvas de transmisión](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md); [B49-C11 · Mezcladores de frecuencia: pérdida de conversión y productos espurios](../programa/clases/B49/B49-C11-mezcladores-de-frecuencia-perdida-de-conversion-y-productos-espurios/CLASE.md); [B104-C05 · Sistemas de vehículos tripulados](../programa/clases/B104/B104-C05-sistemas-de-vehiculos-tripulados/CLASE.md); [B117-C04 · Problemas respiratorios simulados](../programa/clases/B117/B117-C04-problemas-respiratorios-simulados/CLASE.md); [B118-C10 · Síndrome de Kessler como escenario](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md).

### Fuga de datos

- La fuga de datos (*data leakage*) es el uso, al entrenar o ajustar, de información que no estará disponible al predecir (S1).

💡 **Cómo se explica en la clase [B17-C09](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md):**
- La documentación de buenas prácticas de scikit-learn define la fuga de datos como usar, al construir el modelo, información que no estaría disponible al predecir, lo que produce estimaciones optimistas en validación cruzada y peor desempeño con datos nuevos (S1).
- Definir fuga de datos y reconocer sus tres formas más comunes: preprocesamiento global, dependencia temporal y dependencia por fuente.
- 🎯 **Por qué importa:** Un equipo anuncia una exactitud del 95 % para clasificar señales; al aplicarlo a datos de una campaña nueva, baja al 55 %. Nadie mintió: la validación estaba mal hecha.
- 🔗 **Se estudia junto con:** Preprocesamiento global, Pipeline, autocorrelación, grupo.

📘 **Dónde se aprende** (1 clase): [B17-C09 · Prevención de fuga de datos](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md).

### Fuga de especificación

- La fuga de especificación es la pérdida admisible de diseño.

💡 **Contexto en la clase [B110-C01](../programa/clases/B110/B110-C01-despresurizacion-deteccion-aislamiento-y-respuesta/CLASE.md):**
- 🎯 **Por qué importa:** Un módulo presurizado siempre pierde algo de aire; lo grave es la fuga por encima de lo especificado. La decisión central: ¿cuánto tiempo queda antes de la presión mínima y qué se hace con ese tiempo (medir, aislar o retirarse)?
- 🔗 **Se estudia junto con:** despresurización rápida, flujo estrangulado, constante de tiempo, tiempo de reserva.

📘 **Dónde se aprende** (1 clase): [B110-C01 · Despresurización: detección, aislamiento y respuesta](../programa/clases/B110/B110-C01-despresurizacion-deteccion-aislamiento-y-respuesta/CLASE.md).

### Fuga espectral

- La fuga espectral (*spectral leakage*) es el reparto de la energía de una frecuencia en bins vecinos cuando no cae exactamente en uno.
- La fuga espectral es la potencia que se filtra entre bins.

💡 **Cómo se explica en la clase [B15-C04](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md):**
- Reconocer y explicar la fuga espectral cuando la frecuencia no cae en un `k` entero.
- 🎯 **Por qué importa:** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.
- 🔗 **Se estudia junto con:** número complejo, módulo, fórmula de Euler, transformada de Fourier continua.

📘 **Dónde se aprende** (2 clases): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md); [B28-C14 · Ruidos instrumentales](../programa/clases/B28/B28-C14-ruidos-instrumentales/CLASE.md).

### Función

- Una función `f` asigna a cada valor `x` de un conjunto (el dominio) un único valor `f(x)`; el conjunto de los resultados es el rango.
- Una función es un bloque con nombre que recibe datos, hace algo y puede devolver un valor (S2).
- Una función es lo que el sistema hace.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Cambiar de unidades cambia `k`, no la forma de la función.
- En escala log-log, una función de potencia aparece como una recta cuya pendiente es el exponente; entre Venus y Júpiter esa pendiente da 1,499, muy cerca de 1,5 (sección 17).
- ⚠️ **Error frecuente:** Creer que duplicar `x` duplica `y` en cualquier función. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.
- 🔗 **Se estudia junto con:** dominio, rango, variable independiente, dependiente.

📘 **Dónde se aprende** (4 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md); [B09-C01 · Límites de funciones reales](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md); [B83-C06 · Descomposición funcional](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md).

### Función de acoplamiento

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B33-C13](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. Un compañero usa la función de acoplamiento como operativa.
- 🎯 **Por qué importa:** Predecir una tormenta es predecir un evento raro. La decisión central: ¿qué precisión tiene un pronóstico por umbral de un evento raro?
- 🔗 **Se estudia junto con:** regresión, umbral, POD, FAR.

📘 **Dónde se aprende** (1 clase): [B33-C13 · Pronóstico de actividad geomagnética](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md).

### Función de Bessel

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C12](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md):**
- **Idea central (modelo mental):** Como las ondas en un estanque que pasan por un agujero: se abren en anillos; dos fuentes cercanas se confunden cuando el máximo de una cae sobre el primer mínimo de la otra.
- 🎯 **Por qué importa:** La difracción fija el mejor detalle posible. La decisión central: ¿cuándo se resuelven dos estrellas y qué cuesta una obstrucción?
- 🔗 **Se estudia junto con:** disco de Airy, criterio de Rayleigh, criterio de Sparrow, regla de Dawes.

📘 **Dónde se aprende** (2 clases): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md).

### Función de Bessel esférica

- `j_ℓ` es la función de Bessel esférica.

💡 **Contexto en la clase [B40-C09](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md):**
- **Idea central (modelo mental):** Como subir y bajar una cuesta: si la cuesta cambia de altura mientras la recorres, no recuperas toda la energía invertida.
- 🎯 **Por qué importa:** SW domina las escalas grandes; el ISW es una señal de la energía oscura. La decisión central: ¿qué amplitud tiene la meseta y cuánto decaen los potenciales?
- 🔗 **Se estudia junto con:** potencial, factor de crecimiento, ISW.

📘 **Dónde se aprende** (1 clase): [B40-C09 · Efecto Sachs-Wolfe y efecto Sachs-Wolfe integrado](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md).

### Función de Chandrasekhar

- La función de Chandrasekhar es la forma cerrada de `P(x)`.

💡 **Contexto en la clase [B27-C01](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md):**
- **Idea central (modelo mental):** Cada butaca (estado) admite dos personas (espines). Aunque la sala esté a temperatura cero, las butacas bajas se llenan y las últimas personas quedan sentadas en niveles altos, con mucha energía y empujando.
- 🎯 **Por qué importa:** Una estrella sin fusión no se desploma porque los electrones (o neutrones) no pueden apretarse más allá de lo que permite el principio de exclusión, aunque la temperatura sea cero. La decisión central: dada la densidad de un gas degenerado, ¿cuánto vale el momento de Fermi, la presión y cuál de los dos límites aplica?
- 🔗 **Se estudia junto con:** fermión, momento de Fermi, presión de degeneración, régimen no relativista.

📘 **Dónde se aprende** (1 clase): [B27-C01 · Presión de degeneración](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md).

### Función de coalición

- La función de coalición `v(S)` es el valor que logra el subconjunto `S`.

💡 **Cómo se explica en la clase [B125-C04](../programa/clases/B125/B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md):**
- Definir una función de coalición `v(S)` y calcular el excedente de la alianza.
- 🎯 **Por qué importa:** Las empresas espaciales dependen de alianzas con socios de otros países y la clase de gobierno no explica cómo se reparte el valor ni cuánta dependencia se acepta; no está tratado. La decisión central: ¿cómo se reparte de forma justa el excedente de una alianza y cuánta dependencia de un solo socio o país es prudente?
- 🔗 **Se estudia junto con:** alianza, excedente, valor de Shapley, núcleo.

📘 **Dónde se aprende** (1 clase): [B125-C04 · Alianzas y cooperación internacional empresarial](../programa/clases/B125/B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md).

### Función de correlación de dos puntos

- La función de correlación de dos puntos `ξ(r)` mide el exceso de pares a separación `r` respecto del azar: la probabilidad de hallar un par es `n² [1 + ξ(r)] dV₁ dV₂`;

💡 **Cómo se explica en la clase [B25-C18](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md):**
- Definir red cósmica, vacío, función de correlación de dos puntos y catálogo aleatorio.
- 🎯 **Por qué importa:** Las galaxias no se reparten al azar: forman filamentos, paredes, cúmulos y vacíos, la llamada red cósmica. La forma en que se agrupan guarda información de la materia oscura y de la historia del universo.
- 🔗 **Se estudia junto con:** red cósmica, vacíos, densidad numérica, estimador natural.

📘 **Dónde se aprende** (1 clase): [B25-C18 · Estructura cósmica a gran escala](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md).

### Función de cronología

- La función de producción da el número de cráteres por tamaño; la función de cronología da el número acumulado de cráteres de 1 km en el tiempo.

💡 **Cómo se explica en la clase [B61-C06](../programa/clases/B61/B61-C06-datacion-por-conteo-de-crateres-funciones-de-produccion-y-edades-de-modelo/CLASE.md):**
- Evaluar la función de producción `log₁₀ N = Σ aⱼ (log₁₀ D)ʲ` y la cronología `N1(T)`.
- Saturación, resurfacing, secundarios, elección del área, calibración de la cronología y la función de producción.
- 🎯 **Por qué importa:** Una edad absoluta de una superficie planetaria sale del conteo de cráteres calibrado con muestras. La decisión central: ¿qué edad implica un conteo y con qué incertidumbre?
- 🔗 **Se estudia junto con:** función de producción, edad de modelo, densidad acumulada, saturación.

📘 **Dónde se aprende** (1 clase): [B61-C06 · Datación por conteo de cráteres: funciones de producción y edades de modelo](../programa/clases/B61/B61-C06-datacion-por-conteo-de-crateres-funciones-de-produccion-y-edades-de-modelo/CLASE.md).

### Función de dispersión de Faraday

- La síntesis de RM transforma `P(λ²)` en la función de dispersión de Faraday.

💡 **Contexto en la clase [B46-C13](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md):**
- **Idea central (modelo mental):** El ángulo de la veleta depende del cuadrado de la longitud de onda; mirando a muchas longitudes, se ve cuántas vueltas ha dado.
- 🎯 **Por qué importa:** El ángulo de polarización gira con `λ²`, y hay que medirlo en varias frecuencias para saber cuánto. La decisión central: ¿cómo se obtiene la medida de rotación sin ambigüedad de `nπ`?
- 🔗 **Se estudia junto con:** parámetros de Stokes, polarización lineal, rotación de Faraday, síntesis de RM.

📘 **Dónde se aprende** (1 clase): [B46-C13 · Polarimetría de radio](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md).

### Función de distribución

- La función de distribución `f(v)` da la densidad en el espacio de velocidades.
- Mediana: valor que deja la mitad debajo. Función de distribución: probabilidad de no superar un valor.

💡 **Cómo se explica en la clase [B35-C01](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md):**
- python programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/distribuciones.py
- 🎯 **Por qué importa:** Los instrumentos miden distribuciones, y casi todas las fórmulas de fluido son momentos de ellas. La decisión central: ¿basta una maxwelliana o hay que conservar la cola?
- 🔗 **Se estudia junto con:** maxwelliana, distribución kappa, momento, rapidez térmica.

📘 **Dónde se aprende** (2 clases): [B35-C01 · Funciones de distribución de velocidades en plasmas](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md); [B48-C11 · Calidad y clasificación de datos](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md).

### Función de distribución acumulada

- La función de distribución acumulada (cdf) `F(x) = P(X ≤ x)` (S1, C.2.4) existe para ambos tipos y no decrece.

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- Usar la función de distribución acumulada `F` para obtener `P(X ≤ x)`, `P(X > x)` y cuantiles.
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.
- 🔗 **Se estudia junto con:** variable aleatoria, discreta, continua, función de masa de probabilidad.

📘 **Dónde se aprende** (1 clase): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md).

### Función de dos variables

- Una función de dos variables asigna a cada par `(x, y)` de su dominio un número `f(x, y)` (S1, §1.5).

💡 **Cómo se explica en la clase [B09-C15](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md):**
- Una función de dos variables es un terreno: el valor es la altura.
- *Descripción textual:* una función de dos variables se estudia con cortes (funciones de una variable) y con curvas de nivel; ambos permiten clasificar puntos especiales como máximos, mínimos y sillas.
- 🎯 **Por qué importa:** Una sonda que viaja de la Tierra a la Luna se mueve en un campo de potencial que depende de dos coordenadas del plano. Dónde están los puntos de equilibrio y qué forma tiene el campo alrededor de ellos se lee en un mapa de curvas de nivel.
- 🔗 **Se estudia junto con:** dominio, gráfica, corte, curva de nivel.

📘 **Dónde se aprende** (1 clase): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md).

### Función de estructura

- La función de estructura `S₂(l)` es el promedio del incremento al cuadrado.
- La función de estructura `D(r) = ⟨[φ(x)−φ(x+r)]²⟩`.

💡 **Cómo se explica en la clase [B42-C11](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md):**
- *Descripción textual:* una pantalla gaussiana con el espectro de Kolmogorov reproduce, con déficit conocido, la función de estructura teórica.
- Con `r₀ = 0,15 m`, malla de 128 × 128 con paso 0,02 m y 40 pantallas (ilustrativos) la función de estructura medida a `r = 0,08 m` es `1,9643 rad²` frente a `2,0628` de la integral espectral y `2,4132` de la teoría infinita; la pendiente log-log es `1,640`.
- 🎯 **Por qué importa:** La atmósfera fija el límite de resolución de los telescopios terrestres y es la perturbación que corrige la óptica adaptativa. La decisión central: ¿cómo se simula una pantalla de fase con la estadística correcta y qué errores introduce la malla?
- 🔗 **Se estudia junto con:** pantalla de fase, espectro de potencia, parámetro, subarmónicos.

📘 **Dónde se aprende** (2 clases): [B35-C09 · Turbulencia en plasmas y MHD](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md); [B42-C11 · Turbulencia atmosférica](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md).

### Función de Faddeeva

- La función de Faddeeva equivale al perfil complejo.

💡 **Contexto en la clase [B32-C04](../programa/clases/B32/B32-C04-opacidad-de-lineas-ensanchamiento-y-perfil-de-voigt/CLASE.md):**
- **Idea central (modelo mental):** El núcleo es una campana que cae rápido y las alas son una cola que cae como una potencia: lejos del centro solo queda la cola.
- 🎯 **Por qué importa:** Las alas de la línea dan la presión y las abundancias. La decisión central: ¿cuándo domina el núcleo gaussiano y cuándo las alas?
- 🔗 **Se estudia junto con:** perfil de Voigt, parámetro de amortiguamiento, núcleo, alas.

📘 **Dónde se aprende** (1 clase): [B32-C04 · Opacidad de líneas: ensanchamiento y perfil de Voigt](../programa/clases/B32/B32-C04-opacidad-de-lineas-ensanchamiento-y-perfil-de-voigt/CLASE.md).

### Función de fase

- La función de fase `P` da la dirección de la luz dispersada.

💡 **Contexto en la clase [B57-C13](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md):**
- **Idea central (modelo mental):** El vaho del vidrio quita luz directa y la reparte en todas direcciones; cuanto más vaho, menos pasa. Si el vaho es de gotas finas, quita más luz azul que roja.
- 🎯 **Por qué importa:** Un satélite que mira un incendio, un volcán o el mar tiene que descontar la atmósfera, y los aerosoles son lo más variable. La decisión central: ¿cuánto aerosol hay y qué tipo, con qué incertidumbre, a partir de pocas longitudes de onda?
- 🔗 **Se estudia junto con:** espesor óptico de aerosoles, ley de Beer–Lambert, exponente de Ångström, albedo de dispersión simple.

📘 **Dónde se aprende** (1 clase): [B57-C13 · Atmósfera y aerosoles](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md).

### Función de fase de Lambert

- La función de fase de Lambert `Φ(α) = (2/3π)[(π−α)cos α + sin α]` describe una esfera difusa.

💡 **Contexto en la clase [B118-C03](../programa/clases/B118/B118-C03-deteccion-y-seguimiento-optico/CLASE.md):**
- 🎯 **Por qué importa:** La óptica es el medio principal para ver objetos lejanos, pero depende de la iluminación, la distancia y el tiempo de exposición. La decisión central: ¿qué diámetro mínimo se puede detectar con una apertura y un tiempo dados, y cómo cambia con el rango?
- 🔗 **Se estudia junto con:** magnitud aparente, ángulo de fase, albedo, relación señal-ruido.

📘 **Dónde se aprende** (1 clase): [B118-C03 · Detección y seguimiento óptico](../programa/clases/B118/B118-C03-deteccion-y-seguimiento-optico/CLASE.md).

### Función de hash criptográfica

- Una función de hash criptográfica como SHA-256 convierte cualquier secuencia de bytes en un resumen de 256 bits; cambiar un solo bit del mensaje cambia el resumen por completo.

💡 **Contexto en la clase [B14-C11](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md):**
- **Idea central (modelo mental):** En Git, DVC y en el laboratorio de esta clase, un objeto se guarda bajo su huella. Una versión no contiene datos: contiene una lista de huellas. Para recuperar una versión, se pide cada huella al almacén y se comprueba que los bytes recibidos tienen esa huella.
- 🎯 **Por qué importa:** Un análisis usó «la tabla de catálogo de octubre». En noviembre alguien reemplazó el archivo por otro con el mismo nombre.
- 🔗 **Se estudia junto con:** suma de verificación, direccionamiento por contenido, deduplicación, manifiesto.

📘 **Dónde se aprende** (1 clase): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md).

### Función de ida y vuelta

- Una función de ida y vuelta es la composición de una conversión y su inversa que devuelve el punto original.

💡 **Contexto en la clase [B04-C10](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md):**
- **Idea central (modelo mental):** Las cartesianas piden «cuánto a la derecha y cuánto arriba». Las polares piden «cuánto lejos y en qué dirección». El mismo punto tiene los dos pares de valores.
- 🎯 **Por qué importa:** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.
- 🔗 **Se estudia junto con:** coordenadas cartesianas, coordenadas polares, polo, eje polar.

📘 **Dónde se aprende** (1 clase): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md).

### Función de influencia

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B43-C05](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md):**
- *Descripción textual:* la tasa de Preston y la función de influencia convierten un mapa de error en tiempos de permanencia no negativos.
- Límite: perfil 1D, función de influencia invariante.
- ⚠️ **Error frecuente:** Olvidar la función de influencia. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Pulir es controlar un retiro de décimas de micrón: sin un modelo se oscila entre sobrecorregir y subcorregir. La decisión central: ¿cuánto hay que retirar de la mejor esfera para obtener un paraboloide y cuánto tiempo debe permanecer la herramienta en cada zona?
- 🔗 **Se estudia junto con:** ley de Preston, desviación esfera-paraboloide, mejor esfera, tiempo de permanencia.

📘 **Dónde se aprende** (2 clases): [B42-C15 · Espejos deformables](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md); [B43-C05 · Pulido óptico](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md).

### Función de interpolación

- La función de interpolación `μ(x) = x/(1+x)`.

💡 **Contexto en la clase [B36-C11](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md):**
- **Idea central (modelo mental):** Es como una cuesta que se hace menos empinada a gran distancia: la regla de la caída cambia por debajo de una aceleración crítica.
- 🎯 **Por qué importa:** Una alternativa debe confrontarse con todas las pruebas. La decisión central: ¿qué observación separa la materia oscura de la gravedad modificada?
- 🔗 **Se estudia junto con:** aceleración de Milgrom, aceleración newtoniana, relación de Tully–Fisher bariónica, halo NFW.

📘 **Dónde se aprende** (1 clase): [B36-C11 · Gravedad modificada (MOND y relativistas) frente a materia oscura](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md).

### Función de lazo

- La función de lazo es `L = C G H` (lo que da una vuelta al lazo).
- La función de lazo `L(s)`.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- En realimentación negativa, `y = G (u − H y)`, luego `y = G u/(1 + G H)`: la función de transferencia en lazo cerrado es `G/(1 + G H)`.
- Entonces la función de la referencia a la salida es `Kp/(J s² + Kd s + Kp)`, sin el cero en `−Kp/Kd`, mientras el lazo tiene los mismos polos.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.
- 🔗 **Se estudia junto con:** diagrama de bloques, sumador, punto de bifurcación, lazo cerrado.

📘 **Dónde se aprende** (2 clases): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md); [B87-C19 · Verificación de ley de control](../programa/clases/B87/B87-C19-verificacion-de-ley-de-control/CLASE.md).

### Función de luminosidad

- La función de luminosidad `Φ(M)` es la densidad numérica por intervalo de magnitud.

💡 **Cómo se explica en la clase [B38-C01](../programa/clases/B38/B38-C01-funciones-de-luminosidad-estelar/CLASE.md):**
- La evidencia es la ficha de la función de luminosidad del ejercicio 12 (sección 20).
- Ejercicio 9 · transferencia. Transferencia. Un compañero dice que la curva de recuento crudo es la función de luminosidad.
- ⚠️ **Error frecuente:** Usar el recuento crudo como función de luminosidad. Se corrige con 8.3.
- 🎯 **Por qué importa:** Contar las estrellas que se ven no es contar las que hay: las brillantes se ven desde lejos y las débiles solo de cerca. La decisión central: ¿cómo corrijo la selección para recuperar la densidad real por intervalo de luminosidad?
- 🔗 **Se estudia junto con:** magnitud absoluta bolométrica, magnitud aparente, límite de magnitud, volumen máximo.

📘 **Dónde se aprende** (1 clase): [B38-C01 · Funciones de luminosidad estelar](../programa/clases/B38/B38-C01-funciones-de-luminosidad-estelar/CLASE.md).

### Función de Lyapunov

- Una función de Lyapunov `V(x)` es una función definida positiva cuya derivada a lo largo de las trayectorias es no positiva.
- La función de Lyapunov es `V = ½ ωᵀIω + 2K_p(1 − |q_{e,w}|)`.
- La función de Lyapunov `V` incluye el desplazamiento del equilibrio.

💡 **Cómo se explica en la clase [B16-C17](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md):**
- Cuando falla la función de Lyapunov propuesta, no se prueba nada: otra podría servir.
- La función de Lyapunov es como la altura de una bola en un paisaje: si el control garantiza que la bola siempre baja (o se queda), y el único punto de reposo es el fondo, la bola termina en el fondo sin importar de dónde parta.
- 🎯 **Por qué importa:** Cuando un satélite se separa del cohete puede salir girando de forma desordenada («volteando»).
- 🔗 **Se estudia junto con:** ecuaciones de Euler, momento angular, energía cinética de rotación, eje principal.

📘 **Dónde se aprende** (3 clases): [B16-C17 · Control no lineal](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md); [B87-C17 · Control de tres ejes](../programa/clases/B87/B87-C17-control-de-tres-ejes/CLASE.md); [B87-C18 · Estabilidad ante perturbaciones](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md).

### Función de mapeo

- La función de mapeo `m(e)`.

💡 **Contexto en la clase [B51-C10](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md):**
- **Idea central (modelo mental):** Como mirar a través de una ventana: de frente atraviesas un vidrio fino y casi sin retraso; muy inclinado atraviesas mucho más grosor, y por eso el mismo vidrio retrasa más a baja elevación.
- 🎯 **Por qué importa:** Un error atmosférico de centímetros es un error de posición en geodesia y un error de fase en imagen. La decisión central: ¿cómo se mapea el retardo con la elevación y cómo se separa lo dispersivo de lo no dispersivo?
- 🔗 **Se estudia junto con:** retardo cenital, elevación, capa delgada, retardo ionosférico.

📘 **Dónde se aprende** (1 clase): [B51-C10 · Retardo troposférico e ionosférico en VLBI y su modelado](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md).

### Función de masa

- La función de masa `f = (m₂ sen i)³/(m₁+m₂)²` liga las masas con el semieje y el periodo orbital.
- La función de masa `dn/dlnM`.

💡 **Cómo se explica en la clase [B27-C05](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md):**
- *Descripción textual:* del periodo y su derivada salen la pérdida de energía rotacional, el campo y la edad; en una binaria, el semieje y el periodo orbital dan la función de masa y, con la masa del púlsar, la de la compañera.
- Paso 2 · Función de masa. `f = 4π²a³/(GP_b²) = 1,069 × 10⁻³ M☉`.
- ⚠️ **Error frecuente:** Ignorar la inclinación en la función de masa. Se corrige con la sección 13.
- 🎯 **Por qué importa:** Un púlsar da, a la vez, un reloj de precisión, la medida de su campo magnético y, en una binaria, la masa de las estrellas y una prueba de la relatividad general. La decisión central: dados el periodo y su derivada, ¿qué campo, edad y potencia de frenado tiene el púlsar y qué se aprende de su binaria?
- 🔗 **Se estudia junto con:** púlsar, periodo, dipolo magnético en rotación, campo ecuatorial.

📘 **Dónde se aprende** (2 clases): [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md); [B36-C06 · Formación de halos y función de masa](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md).

### Función de masa de probabilidad

- La función de masa de probabilidad (pmf) `p_X(k) = P(X = k)` da la probabilidad de cada valor de una discreta; suma 1.

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- Construir y verificar una función de masa (suma 1) y calcular probabilidades con ella.
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.
- 🔗 **Se estudia junto con:** variable aleatoria, discreta, continua, función de distribución acumulada.

📘 **Dónde se aprende** (1 clase): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md).

### Función de masa inicial

- La función de masa inicial (IMF) `ξ(m) = dN/dm` da cuántas estrellas nacen por intervalo de masa.

💡 **Cómo se explica en la clase [B25-C07](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md):**
- Kroupa (S2) halla cambios de pendiente de la función de masa inicial hacia `0,5` y `0,08 M☉`.
- Describir una función de masa inicial por tramos y calcular su masa media y fracciones.
- 🎯 **Por qué importa:** Las estrellas de una galaxia no giran en círculos perfectos: oscilan alrededor de una órbita circular, y su agitación revela la edad y la historia de la población. Además, no nacen todas con la misma masa: la función de masa inicial fija cuántas hay de cada tipo y cuánta luz y metales producirán.
- 🔗 **Se estudia junto con:** población estelar, órbita circular, epiciclo, radio guía.

📘 **Dónde se aprende** (1 clase): [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### Función de mérito

- La función de mérito es el número que se minimiza.

💡 **Cómo se explica en la clase [B50-C02](../programa/clases/B50/B50-C02-optimizacion-de-superficies-funcion-de-merito-y-restricciones/CLASE.md):**
- Escribir una función de mérito como suma de residuos al cuadrado.
- python programa/clases/B50/B50-C02-optimizacion-de-superficies-funcion-de-merito-y-restricciones/optimizacion.py
- 🎯 **Por qué importa:** Un diseñador no ajusta curvaturas a mano: define qué es «bueno» como un número y deja que el cálculo busque. La decisión central: ¿qué mide la función de mérito y qué fija la restricción?
- 🔗 **Se estudia junto con:** variable de diseño, residuo, Levenberg–Marquardt, restricción.

📘 **Dónde se aprende** (1 clase): [B50-C02 · Optimización de superficies: función de mérito y restricciones](../programa/clases/B50/B50-C02-optimizacion-de-superficies-funcion-de-merito-y-restricciones/CLASE.md).

### Función de partición

- La función de partición `U` suma los niveles.

💡 **Cómo se explica en la clase [B45-C14](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md):**
- A 10 000 K, la fracción de n = 2 respecto de los neutros es `2,897923 × 10⁻⁵` por suma directa de niveles y `2,897923 × 10⁻⁵` por la fórmula con la función de partición; el cociente de Boltzmann entre n = 2 y n = 1 es `2,8982 × 10⁻⁵`.
- 🎯 **Por qué importa:** Las líneas de Balmer son más fuertes en estrellas A que en estrellas frías o calientes. La decisión central: ¿por qué hay un máximo de temperatura y cómo se pasa de intensidades a abundancias?
- 🔗 **Se estudia junto con:** ecuación de Boltzmann, ecuación de Saha, presión electrónica, abundancia.

📘 **Dónde se aprende** (2 clases): [B45-C14 · Composición química por espectros](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md); [B46-C12 · Emisiones moleculares](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md).

### Función de peso

- La función de peso `W(z)` indica de qué altura procede la señal.

💡 **Cómo se explica en la clase [B54-C18](../programa/clases/B54/B54-C18-medicion-remota-atmosferica/CLASE.md):**
- *Descripción textual:* el coeficiente de absorción y la densidad dan la función de peso y su máximo; una ocultación con ruido se ajusta linealmente para recuperar `H`.
- El canal solo ve por encima de las nubes y su función de peso queda truncada.
- 🎯 **Por qué importa:** Cada canal 've' una capa distinta según su absorción. La pregunta motivadora: ¿a qué altura 'mira' cada canal y cómo se recupera la altura de escala con ruido?
- 🔗 **Se estudia junto con:** profundidad óptica, ocultación, recuperación, ruido.

📘 **Dónde se aprende** (1 clase): [B54-C18 · Medición remota atmosférica](../programa/clases/B54/B54-C18-medicion-remota-atmosferica/CLASE.md).

### Función de Planck

- La función de Planck `B_ν = (2hν³/c²)/(e^{hν/kT} − 1)` da la intensidad espectral.

💡 **Contexto en la clase [B26-C15](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md):**
- **Idea central (modelo mental):** El universo temprano fue un horno en equilibrio térmico. Cuando se enfrió y se hizo transparente, la radiación quedó con la forma del cuerpo negro y desde entonces solo cambia su temperatura.
- 🎯 **Por qué importa:** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.
- 🔗 **Se estudia junto con:** densidad numérica de fotones, frecuencia del máximo, energía media, razón barión–fotón.

📘 **Dónde se aprende** (1 clase): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### Función de potencia

- Una función de potencia tiene la forma `y = k xⁿ`; el exponente `n` puede ser fraccionario.

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- En escala log-log, una función de potencia aparece como una recta cuya pendiente es el exponente; entre Venus y Júpiter esa pendiente da 1,499, muy cerca de 1,5 (sección 17).
- Evaluar y representar funciones lineales, cuadráticas y de potencia.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.
- 🔗 **Se estudia junto con:** función, dominio, rango, variable independiente.

📘 **Dónde se aprende** (1 clase): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md).

### Función de Prandtl–Meyer

- La función de Prandtl–Meyer `ν(M)` mide el giro total desde `M = 1`.

💡 **Cómo se explica en la clase [B79-C06](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md):**
- *Descripción textual:* el Mach supersónico determina la relación de áreas, el ángulo de Mach y la función de Prandtl–Meyer; las dos relaciones se verifican con integrales numéricas.
- Calcular la función de Prandtl–Meyer y el Mach tras una expansión.
- 🎯 **Por qué importa:** El comportamiento de un flujo a `M > 1` en toberas y vehículos no lo trata ninguna clase del tronco. Sin él no se entiende por qué una tobera necesita una parte divergente.
- 🔗 **Se estudia junto con:** relación área–Mach, ángulo de Mach, expansión de Prandtl–Meyer.

📘 **Dónde se aprende** (1 clase): [B79-C06 · Flujos supersónicos](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md).

### Función de producción

- La función de producción da el número de cráteres por tamaño; la función de cronología da el número acumulado de cráteres de 1 km en el tiempo.

💡 **Cómo se explica en la clase [B61-C06](../programa/clases/B61/B61-C06-datacion-por-conteo-de-crateres-funciones-de-produccion-y-edades-de-modelo/CLASE.md):**
- Evaluar la función de producción `log₁₀ N = Σ aⱼ (log₁₀ D)ʲ` y la cronología `N1(T)`.
- Saturación, resurfacing, secundarios, elección del área, calibración de la cronología y la función de producción.
- 🎯 **Por qué importa:** Una edad absoluta de una superficie planetaria sale del conteo de cráteres calibrado con muestras. La decisión central: ¿qué edad implica un conteo y con qué incertidumbre?
- 🔗 **Se estudia junto con:** función de cronología, edad de modelo, densidad acumulada, saturación.

📘 **Dónde se aprende** (1 clase): [B61-C06 · Datación por conteo de cráteres: funciones de producción y edades de modelo](../programa/clases/B61/B61-C06-datacion-por-conteo-de-crateres-funciones-de-produccion-y-edades-de-modelo/CLASE.md).

### Función de prueba

- La forma débil de `−u″ = f` con `u(0) = u(1) = 0` multiplica por una función de prueba `v` (también nula en los extremos) e integra por partes: `∫ u′ v′ dx = ∫ f v dx` para toda `v`.

💡 **Cómo se explica en la clase [B11-C15](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar que las funciones de prueba deben anularse en el borde. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Las estructuras y los escudos de una nave no son barras rectas con mallas regulares. El análisis térmico y estructural de ingeniería espacial se hace casi siempre con elementos finitos sobre geometrías reales.
- 🔗 **Se estudia junto con:** forma débil, malla, elementos, función sombrero.

📘 **Dónde se aprende** (1 clase): [B11-C15 · Elementos finitos introductorios](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md).

### Función de rechazo

- La función de rechazo `H_r` y la de ruido `H_n`.

💡 **Contexto en la clase [B42-C16](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md):**
- **Idea central (modelo mental):** Como regular una ducha con agua que tarda en llegar: si giras la llave muy rápido, oscilas; muy lento, no sigues la temperatura.
- 🎯 **Por qué importa:** El lazo decide qué tan rápido es el rechazo y cuánto ruido se amplifica. La decisión central: ¿qué ganancia da el mejor compromiso entre rechazo, ruido y estabilidad con retardo?
- 🔗 **Se estudia junto con:** integrador, retardo, ruido, ancho de banda de rechazo.

📘 **Dónde se aprende** (1 clase): [B42-C16 · Lazo de control de óptica adaptativa](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md).

### Función de Schechter

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B38-C09](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md):**
- Aquí además la "simulación" es una función de Schechter, no una simulación.
- 🎯 **Por qué importa:** Una simulación calibrada para coincidir con los datos no queda validada por coincidir con ellos. La decisión central: ¿qué parte del acuerdo es una predicción y qué parte es un ajuste?
- 🔗 **Se estudia junto con:** residuo en dex, prueba KS, chi cuadrado de Poisson, calibración.

📘 **Dónde se aprende** (1 clase): [B38-C09 · Validación de galaxias simuladas frente a observaciones](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md).

### Función de selección

- La función de selección `Φ(z)`.

💡 **Cómo se explica en la clase [B28-C19](../programa/clases/B28/B28-C19-limitaciones-y-sesgos-de-deteccion/CLASE.md):**
- Para corregir hay que conocer la función de selección y ponderar por `1/Φ(z)`, o modelar conjuntamente la población y la selección.
- ⚠️ **Error frecuente:** Ignorar la función de selección. Se corrige con 8.5.
- 🎯 **Por qué importa:** Si se promedia la luminosidad de los eventos detectados sin corregir, se sobrestima la luminosidad típica de la población. El mismo razonamiento vale para las masas de fusiones de ondas gravitacionales detectadas.
- 🔗 **Se estudia junto con:** sesgo de Malmquist, muestra limitada por flujo, normal truncada, módulo de distancia.

📘 **Dónde se aprende** (1 clase): [B28-C19 · Limitaciones y sesgos de detección](../programa/clases/B28/B28-C19-limitaciones-y-sesgos-de-deteccion/CLASE.md).

### Función de sensibilidad

- La función de sensibilidad es `S = 1/(1 + L)` y la complementaria `T = L/(1+L)`.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- Calcular las funciones de lazo `L`, sensibilidad `S` y sensibilidad complementaria `T`.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.
- 🔗 **Se estudia junto con:** diagrama de bloques, sumador, punto de bifurcación, lazo cerrado.

📘 **Dónde se aprende** (1 clase): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md).

### Función de transferencia

- La función de transferencia `Ĥ(f)` es la DFT de la PSF: para una gaussiana, `Ĥ(f) = exp(−2π²σ²f²)`, que cae muy rápido con la frecuencia espacial `f`.
- La función de transferencia `G(s)` es el cociente `Y(s)/U(s)` con condiciones iniciales nulas.
- La función de transferencia `T(k)` pasa de 1 en escalas grandes a decaer en escalas pequeñas.

💡 **Cómo se explica en la clase [B16-C05](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md):**
- El espacio de estados (C02) conserva todos los estados internos y vale para varias entradas y salidas; la función de transferencia solo describe la relación de una entrada con una salida, ignora lo que se cancele entre polos y ceros, y es compacta.
- La respuesta en frecuencia (C10) es la función de transferencia evaluada en `s = jω`.
- 🎯 **Por qué importa:** Un ingeniero que diseña el control de actitud de un telescopio revisa decenas de variantes de ganancias.
- 🔗 **Se estudia junto con:** transformada de Laplace, polos, ceros, orden.

📘 **Dónde se aprende** (3 clases): [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B16-C05 · Funciones de transferencia](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md); [B36-C02 · Función de transferencia y espectro de materia](../programa/clases/B36/B36-C02-funcion-de-transferencia-y-espectro-de-materia/CLASE.md).

### Función esencial

- Una función esencial es la que no puede interrumpirse.

💡 **Cómo se explica en la clase [B122-C10](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md):**
- F["funcion esencial: minimo k"] --> B["P(>=k de n) binomial"]
- El ejemplo conductor es una institución sintética con cuatro funciones esenciales (Control de la misión `k = 3`, Seguridad de las comunicaciones `k = 2`, Comunicación de crisis `k = 1`, Soporte de TI `k = 2`), disponibilidad individual `p = 0,85` y objetivo `0,99`.
- 🎯 **Por qué importa:** No hay clase equivalente sobre continuidad de funciones institucionales. La decisión central: ¿qué dotación mínima asegura que cada función esencial se cubra con al menos el 99 %?
- 🔗 **Se estudia junto con:** dotación mínima, plantilla, disponibilidad individual, plan de continuidad de operaciones.

📘 **Dónde se aprende** (1 clase): [B122-C10 · Planes de continuidad institucional y de operaciones](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md).

### Función espectral

- La función espectral `g(x) = x coth(x/2) − 4`.

💡 **Cómo se explica en la clase [B40-C11](../programa/clases/B40/B40-C11-efecto-sunyaev-zeldovich-termico-y-cinematico/CLASE.md):**
- *Descripción textual:* la densidad y la temperatura del gas dan `y`; la función espectral se verifica con Kompaneets y fija el nulo.
- 🎯 **Por qué importa:** El tSZ no depende del corrimiento al rojo y permite detectar cúmulos lejanos. La decisión central: ¿cuánto vale la distorsión a cada frecuencia y dónde se anula?
- 🔗 **Se estudia junto con:** parámetro de Compton, nulo, profundidad óptica, operador de Kompaneets.

📘 **Dónde se aprende** (1 clase): [B40-C11 · Efecto Sunyaev-Zeldovich térmico y cinemático](../programa/clases/B40/B40-C11-efecto-sunyaev-zeldovich-termico-y-cinematico/CLASE.md).

### Función exponencial

- Una función exponencial tiene la forma `y = a·bˣ`, con base `b > 0` y `b ≠ 1`; el número de Euler `e ≈ 2,71828` es la base natural.

💡 **Cómo se explica en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- python programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/magnitudes_y_logaritmos.py
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.
- 🔗 **Se estudia junto con:** número de Euler, logaritmo en base b, logaritmo decimal, natural.

📘 **Dónde se aprende** (1 clase): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md).

### Función fuente

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C01](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md):**
- La intensidad en `μ` refleja la función fuente en `τ ≈ μ`.
- *Descripción textual:* la función fuente da la intensidad emergente por integración; para una fuente lineal se obtiene `a + bμ`, de la que salen el limbo y el flujo.
- 🎯 **Por qué importa:** El espectro depende de dónde se forma la luz. La decisión central: ¿qué capa determina la intensidad emergente y cómo cambia con el ángulo?
- 🔗 **Se estudia junto con:** intensidad específica, profundidad óptica, ángulo, oscurecimiento del limbo.

📘 **Dónde se aprende** (1 clase): [B32-C01 · Ecuación de transferencia radiativa en atmósferas estelares](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md).

### Función inicial de masa

- La función inicial de masa es la distribución de masas al nacer; en el campo galáctico presenta cambios de pendiente hacia `0,5` y `0,08 M☉` (S4, resumen).
- La función inicial de masa `dN/dM ∝ M^{−α}` da el reparto de masas al nacer; la pendiente `α` es aquí `2,3`, un parámetro ilustrativo (Kroupa señala cambios de pendiente hacia `0,5` y `0,08 M☉`, S3).

💡 **Cómo se explica en la clase [B24-C15](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md):**
- Las poblaciones que se observan dependen de la función inicial de masa: muchas más estrellas de baja masa que de alta (S4, resumen), y su suma domina la masa estelar en un cúmulo joven.
- 🎯 **Por qué importa:** La masa decide casi todo en la vida de una estrella: cuánto brilla, cuánto dura y cómo termina. Entender por qué una estrella de la mitad de la masa del Sol vive varias veces más tiempo, y por qué las más pequeñas casi no han evolucionado, explica la composición de las poblaciones estelares y la edad de los cúmulos.
- 🔗 **Se estudia junto con:** secuencia principal, relación masa–luminosidad, tiempo nuclear, enana roja.

📘 **Dónde se aprende** (2 clases): [B24-C15 · Estrellas de baja masa](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md); [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Función interior

- La función interior es `g`, la exterior `f`.

💡 **Cómo se explica en la clase [B09-C09](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md):**
- *Descripción textual:* se nombra la función interior `u`, se traduce el diferencial, se integra en `u` y se devuelve el resultado a `x`.
- 🎯 **Por qué importa:** La densidad del aire decae con la altitud de forma exponencial, y la masa de aire sobre un punto determina la presión y la extinción de la luz. Para obtenerla hay que integrar `e^{−h/H}`, que no es una integral básica: la variable aparece dentro de un exponente.
- 🔗 **Se estudia junto con:** sustitución, diferencial, exterior, altura de escala.

📘 **Dónde se aprende** (1 clase): [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md).

### Función objetivo

- Una función objetivo es la cantidad que se quiere maximizar o minimizar.

💡 **Cómo se explica en la clase [B09-C07](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md):**
- Plantear una función objetivo con una sola variable a partir de un enunciado.
- 🎯 **Por qué importa:** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.
- 🔗 **Se estudia junto con:** punto crítico, máximo (mínimo) local, extremo global, prueba de la segunda derivada.

📘 **Dónde se aprende** (1 clase): [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md).

### Función periódica

- Una función periódica se repite cada periodo `P`.

💡 **Contexto en la clase [B09-C05](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md):**
- **Idea central (modelo mental):** La gráfica de `sin x` sube más rápido en 0 (pendiente 1), se aplana en su máximo (pendiente 0) y baja en el cruce siguiente. La pendiente en cada punto describe otra onda: el coseno, desfasado un cuarto de ciclo. Derivar de nuevo desfasa otro cuarto: `sin → cos → −sin → −cos → sin`.
- 🎯 **Por qué importa:** Un telescopio con montura altacimutal apunta con dos ejes: altitud y azimut. Para mantener una estrella en el centro del campo, cada eje debe girar a una velocidad que cambia con el tiempo.
- 🔗 **Se estudia junto con:** declinación, ángulo horario, altitud, culminación.

📘 **Dónde se aprende** (1 clase): [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md).

### Función pura

- Una función pura devuelve siempre el mismo resultado para los mismos argumentos y no cambia nada fuera de sí misma: no lee archivos, no imprime, no usa variables globales que cambien.

💡 **Cómo se explica en la clase [B14-C01](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md):**
- Para un proyecto de varios archivos, una organización razonable es una carpeta `nucleo/` con funciones puras, `adaptadores/` con lectura y conversión, un archivo de orquestación, `pruebas/` y un `README`.
- Escribir funciones puras para una fórmula física, con unidades y dominio de validez declarados.
- 🎯 **Por qué importa:** Un script de 300 líneas que lee un archivo, calcula una órbita, dibuja una figura y escribe un informe funciona hasta el día en que cambias el archivo de entrada. Entonces no sabes si un resultado distinto viene de los datos, de la fórmula o de un error nuevo.
- 🔗 **Se estudia junto con:** efecto secundario, núcleo, adaptador, orquestación.

📘 **Dónde se aprende** (1 clase): [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md).

### Función regulatoria

- La función regulatoria es lo que una norma debe lograr (autorizar, supervisar, registrar).

💡 **Cómo se explica en la clase [B121-C04](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md):**
- O["Función regulatoria"] --> I["Instrumento chileno identificado?"]
- El ejemplo conductor es una matriz de 10 funciones regulatorias: 4 con evidencia leída, 2 con indicios y 4 sin evidencia hallada.
- 🎯 **Por qué importa:** Un marco nacional se conoce por sus instrumentos, y cada instrumento debe leerse en su texto vigente. La decisión central: ¿qué funciones regulatorias tienen un instrumento chileno identificado y con qué nivel de evidencia?
- 🔗 **Se estudia junto con:** nivel de evidencia, instrumento, traducción no oficial, concesión.

📘 **Dónde se aprende** (1 clase): [B121-C04 · Marco legal espacial en Chile](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md).

### Función seno cardinal

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B51-C09](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md):**
- **Idea central (modelo mental):** Como un estroboscopio que se sincroniza con la rueda que gira: si la luz parpadea a la tasa de franjas, la rueda parece quieta y puedes promediar sin que se borre.
- 🎯 **Por qué importa:** Si se promedia sin detener las franjas, la señal se anula. La decisión central: ¿qué tasa de franjas tiene una fuente, cuánto se pierde al promediar y qué precisión pide el modelo?
- 🔗 **Se estudia junto con:** retardo geométrico, ángulo horario, tasa de franjas, fringe stopping.

📘 **Dónde se aprende** (1 clase): [B51-C09 · Fringe stopping y rotación de fase por retardo geométrico](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md).

### Función sombrero

- La función sombrero (o de base lineal) `φ_i` vale 1 en el nodo `i`, 0 en los demás y es lineal a trozos.

💡 **Cómo se explica en la clase [B11-C15](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md):**
- *Descripción textual:* de la ecuación se pasa a la forma débil; se aproxima la solución con funciones sombrero; se ensambla el sistema `K u = b` sumando las contribuciones de los elementos; se resuelve y se mide el error en las normas `L²` y `H¹`.
- Construir las funciones de base lineales a trozos («sombrero»).
- 🎯 **Por qué importa:** Las estructuras y los escudos de una nave no son barras rectas con mallas regulares. El análisis térmico y estructural de ingeniería espacial se hace casi siempre con elementos finitos sobre geometrías reales.
- 🔗 **Se estudia junto con:** forma débil, función de prueba, malla, elementos.

📘 **Dónde se aprende** (1 clase): [B11-C15 · Elementos finitos introductorios](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md).

### Función unimodal

- Una función unimodal en un intervalo tiene un solo mínimo.

💡 **Contexto en la clase [B11-C17](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md):**
- **Idea central (modelo mental):** Se busca el fondo de un valle con niebla. Con la sección áurea se sondean dos puntos y se descarta el tramo peor; con el gradiente se baja por la pendiente; con Newton se supone que el valle es una parábola y se salta a su fondo.
- 🎯 **Por qué importa:** Diseñar una transferencia, ajustar un modelo a datos de seguimiento o calibrar un instrumento son problemas de optimización. Un algoritmo de búsqueda siempre devuelve *algún* número: la tarea del ingeniero es saber si es un mínimo, si es el global, si está en una frontera y con qué incertidumbre.
- 🔗 **Se estudia junto con:** mínimo local, global, sección áurea, método de Newton.

📘 **Dónde se aprende** (1 clase): [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md).

### Función ventana

- La función ventana `W(f) = |Σe^{−2πift}|/N`.

💡 **Cómo se explica en la clase [B29-C19](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md):**
- *Descripción textual:* con los tiempos se calcula la potencia de Lomb–Scargle, que coincide con el ajuste de mínimos cuadrados; la función ventana explica los alias; bajo el ruido la potencia normalizada es exponencial.
- 🎯 **Por qué importa:** Un periodograma sin cuidado señala alias en lugar del periodo verdadero, y una potencia alta puede ser una fluctuación del ruido. La decisión central: ¿qué picos son del periodo verdadero, cuáles son alias y qué potencia es significativa?
- 🔗 **Se estudia junto con:** periodograma, desfase, alias, potencia normalizada.

📘 **Dónde se aprende** (1 clase): [B29-C19 · Análisis de series temporales irregularmente muestreadas](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md).

### Función zeta

- La función zeta `ζ(−1) = −1/12`, `ζ(−3) = 1/120`.

💡 **Contexto en la clase [B31-C19](../programa/clases/B31/B31-C19-vacio-cuantico-y-limites-conceptuales/CLASE.md):**
- **Idea central (modelo mental):** Una cuerda con infinitos modos tiene energía infinita; lo que se mide es la diferencia entre dos configuraciones, donde los infinitos se cancelan y queda un número finito.
- 🎯 **Por qué importa:** Las sumas infinitas de la teoría cuántica de campos exigen regularización, y el vacío tiene consecuencias medibles. La decisión central: ¿cuánto vale la presión de Casimir y qué parte de una suma divergente es física?
- 🔗 **Se estudia junto con:** energía de punto cero, presión de Casimir, regularización, parte finita.

📘 **Dónde se aprende** (1 clase): [B31-C19 · Vacío cuántico y límites conceptuales](../programa/clases/B31/B31-C19-vacio-cuantico-y-limites-conceptuales/CLASE.md).

### Funciones de Bessel modificadas

- Las funciones `I_n` y `K_n` (n = 0, 1) son las funciones de Bessel modificadas; aparecen en la solución de Freeman.

💡 **Contexto en la clase [B25-C08](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md):**
- **Idea central (modelo mental):** Piensa en una cuerda con una bola que gira: la tensión equilibra la fuerza centrífuga. Si la bola gira más rápido sin que la cuerda cambie, habrá que tirar más fuerte. Analogía: la tensión es la gravedad de la masa interior y la bola es la estrella.
- 🎯 **Por qué importa:** Si la masa estuviera donde brilla, la velocidad de rotación debería caer en las afueras de una galaxia, como la de los planetas lejanos del Sol. Que una curva de rotación se mantenga plana indica más masa de la que se ve.
- 🔗 **Se estudia junto con:** curva de rotación, velocidad circular, disco exponencial delgado, halo pseudo-isotermo.

📘 **Dónde se aprende** (1 clase): [B25-C08 · Curvas de rotación de galaxias](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md).

### Funciones de Stumpff

- Las funciones de Stumpff son `C(z) = (1 − cos √z)/z` y `S(z) = (√z − sin √z)/√z³` (con las formas hiperbólicas para `z < 0`).
- Las funciones de Stumpff `C(z)` y `S(z)` evitan separar casos.

💡 **Cómo se explica en la clase [B82-C03](../programa/clases/B82/B82-C03-formulacion-de-variables-universales/CLASE.md):**
- Definir `z = α χ²` y las funciones de Stumpff `C(z)` y `S(z)`.
- `|z| < 4π²`; no trata `Δθ = π`; el propagador comparte las funciones de Stumpff con el solucionador.
- 🎯 **Por qué importa:** El tiempo de vuelo decide el tipo de cónica: si es corto, la nave necesita energía positiva. La decisión central: ¿cómo se resuelve Lambert con una sola ecuación que funcione para cualquier tiempo de vuelo, y qué dice el signo de `z`?
- 🔗 **Se estudia junto con:** variable universal.

📘 **Dónde se aprende** (2 clases): [B75-C04 · Ecuación de Lambert](../programa/clases/B75/B75-C04-ecuacion-de-lambert/CLASE.md); [B82-C03 · Formulación de variables universales](../programa/clases/B82/B82-C03-formulacion-de-variables-universales/CLASE.md).

### Fusible

- El fusible abre el circuito al fundirse un elemento.

💡 **Cómo se explica en la clase [B86-C10](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md):**
- A corriente alta `I²t → τ I_f²` (`4,50 A²s` para el fusible de `3 A`).
- Con fallas de alta resistencia la corriente baja: por debajo de `15 A` el fusible de aguas arriba no llega a fundirse y la falla la despeja solo F2, que a su vez no actúa si `I ≤ 3 A`.
- ⚠️ **Error frecuente:** Aumentar el fusible para evitar disparos. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Si el fusible aguas arriba se funde antes que el de la rama averiada, un fallo local deja sin energía a toda la nave. Una protección bien coordinada aísla la rama y conserva el resto.
- 🔗 **Se estudia junto con:** corriente de fusión, integral I²t, despeje, selectividad.

📘 **Dónde se aprende** (1 clase): [B86-C10 · Protección contra sobrecorriente](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md).

### Fusión

- Una interacción es un encuentro gravitatorio que deforma a las galaxias sin fundirlas; una fusión las une.
- Las curvas de equilibrio separan regiones: fusión (sólido–líquido), vaporización (líquido–gas) y sublimación (sólido–gas).
- La fusión combina datos de sensores distintos.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- Límites: `ΔH` constante, gas ideal, curvas aproximadas y válidas cerca del punto triple; no se calcula la curva de fusión.
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.
- 🔗 **Se estudia junto con:** diagrama de fases, curvas de equilibrio, vaporización, sublimación.

📘 **Dónde se aprende** (5 clases): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md); [B15-C24 · Fusión de imágenes de distintos sensores](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md); [B25-C12 · Interacciones y fusiones galácticas](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md); [B76-C13 · Sensores de proximidad](../programa/clases/B76/B76-C13-sensores-de-proximidad/CLASE.md); [B124-C03 · Mercados downstream y upstream](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md).

### Fusión como investigación

- La fusión como investigación significa que se estudia en laboratorio y no hay dispositivo en vuelo.

💡 **Cómo se explica en la clase [B78-C16](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md):**
- Límite: la energía de la fusión no se «quema» en un motor ya construido; se aprovecha solo con un dispositivo aún en investigación.
- python programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/fusion.py
- 🎯 **Por qué importa:** Si la energía por kilo es millones de veces mayor, el escape posible es enorme; pero eso es una cota, no un propulsor. La decisión central: ¿cuánta energía por kilo libera cada reacción y cuánto escape acotaría, según la fracción que se logre dirigir?
- 🔗 **Se estudia junto con:** energía específica, fracción de masa convertida, fracción dirigida, cota de escape.

📘 **Dónde se aprende** (1 clase): [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md).

### Fusión ingenua

- La fusión ingenua supone errores independientes.

💡 **Cómo se explica en la clase [B80-C08](../programa/clases/B80/B80-C08-filtrado-distribuido-y-descentralizado/CLASE.md):**
- *Descripción textual:* dos estimaciones llegan a un nodo de fusión; si se conoce su correlación se usa; si no, la intersección de covarianzas con peso optimizado; si se ignora, la suma ingenua declara una confianza excesiva.
- El script [descentralizado.py](descentralizado.py) calcula la covarianza real de dos fusiones con errores correlacionados, optimiza el peso de la CI y mide el NEES por Monte Carlo (comprueba ingenua inconsistente, CI consistente).
- 🎯 **Por qué importa:** B74-C08..C10 tratan filtros centralizados, en los que un solo nodo ve todas las mediciones. La decisión central: ¿cómo fundir estimaciones de varios nodos sin conocer la correlación entre sus errores y sin declarar más confianza de la que se tiene?
- 🔗 **Se estudia junto con:** intersección de covarianzas, NEES, consistencia.

📘 **Dónde se aprende** (1 clase): [B80-C08 · Filtrado distribuido y descentralizado](../programa/clases/B80/B80-C08-filtrado-distribuido-y-descentralizado/CLASE.md).

### Fusión nuclear

- La fusión nuclear une núcleos ligeros en uno más pesado.

💡 **Contexto en la clase [B24-C06](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md):**
- **Idea central (modelo mental):** Cuatro protones pesan algo más que un núcleo de helio con sus dos electrones asociados; la diferencia (0,7 %) desaparece como energía.
- 🎯 **Por qué importa:** Una estrella como el Sol brilla desde hace miles de millones de años; ninguna fuente química ni gravitatoria alcanza (C02). La fusión nuclear sí.
- 🔗 **Se estudia junto con:** defecto de masa, protón, partícula alfa, positrón.

📘 **Dónde se aprende** (1 clase): [B24-C06 · Fusión de hidrógeno](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md).

### Fusión pancromática

- La fusión pancromática (*pansharpening*) combina baja resolución espectral-espacial con alta resolución espacial.

💡 **Cómo se explica en la clase [B57-C05](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md):**
- Se promedia la verdad en bloques de `2 × 2` (baja resolución) y se reconstruye de dos maneras: vecino más cercano y fusión de Brovey con la pancromática.
- Por fusión: Brovey, con la pancromática.
- 🎯 **Por qué importa:** Con una sola banda el agua oscura, la sombra y el asfalto se confunden; con varias, cada cubierta deja una firma distinta. La decisión central: ¿qué combinación de bandas separa las cubiertas que me interesan y cómo recupero detalle espacial sin falsear los colores?
- 🔗 **Se estudia junto con:** banda, composición, falso color, razón de bandas.

📘 **Dónde se aprende** (1 clase): [B57-C05 · Imágenes multiespectrales](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md).

### Fusión perfectamente inelástica

- Una fusión perfectamente inelástica une dos cuerpos en el centro de masa del par con la velocidad del centro de masa.

💡 **Contexto en la clase [B52-C20](../programa/clases/B52/B52-C20-simulacion-de-formacion-planetaria-simplificada/CLASE.md):**
- **Idea central (modelo mental):** Como un juego de billar con bolas pegajosas: al chocar quedan unidas, el movimiento total se mantiene, el giro de la pareja queda como espín y parte de la energía desaparece. Límite: planar, circular al inicio, sin gas, fragmentación ni migración.
- 🎯 **Por qué importa:** Una simulación de formación sin sus controles de conservación no es evidencia de nada. La decisión central: ¿qué comprobaciones demuestran que la simulación se ejecutó correctamente antes de interpretar su resultado?
- 🔗 **Se estudia junto con:** espín, radio de fusión inflado, comprobación de conservación.

📘 **Dónde se aprende** (1 clase): [B52-C20 · Simulación de formación planetaria simplificada](../programa/clases/B52/B52-C20-simulacion-de-formacion-planetaria-simplificada/CLASE.md).

### Fusión por varianza inversa

- La fusión por varianza inversa pondera cada medida por `1/σ²`.

💡 **Contexto en la clase [B97-C03](../programa/clases/B97/B97-C03-sensores-y-percepcion-robotica/CLASE.md):**
- 🎯 **Por qué importa:** Un sensor con ruido bajo parece suficiente hasta que se ensucia, se descalibra o falla; entonces el robot necesita saber cuánto confiar en cada lectura. La fusión da la respuesta de forma cuantitativa, y también muestra su punto débil.
- 🔗 **Se estudia junto con:** ruido, sesgo, incertidumbre fusionada, Monte Carlo.

📘 **Dónde se aprende** (1 clase): [B97-C03 · Sensores y percepción robótica](../programa/clases/B97/B97-C03-sensores-y-percepcion-robotica/CLASE.md).

### Fussell–Vesely

- Birnbaum mide `P(top | i falla) − P(top | i no falla)`. Fussell–Vesely mide la fracción del riesgo que se elimina si `i` nunca falla.

💡 **Cómo se explica en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- Calcular la importancia de Birnbaum y de Fussell–Vesely y priorizar.
- Mayor contribuyente (Fussell-Vesely): B5 (0.616)
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?
- 🔗 **Se estudia junto con:** árbol de fallos, eventos básicos, conjunto de corte, mínimo.

📘 **Dónde se aprende** (1 clase): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Fuzzing

- El fuzzing genera entradas masivas.

💡 **Cómo se explica en la clase [B88-C37](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md):**
- Analogía: el fuzzing guiado es como explorar una casa tocando todas las puertas y recordando las que se abren: el azar puro toca a ciegas.
- Con fuzzing aleatorio puro: 2 hallazgos en 10 campañas y `5,2` de 13 ramas; primer hallazgo tras `10 513` ejecuciones.
- 🎯 **Por qué importa:** Las pruebas diseñadas por una persona no prevén todas las combinaciones. La decisión central: ¿qué estrategia de entradas encuentra más fallos con menos ejecuciones en un banco autorizado?
- 🔗 **Se estudia junto con:** corpus, mutación, cobertura de ramas, hallazgo.

📘 **Dónde se aprende** (1 clase): [B88-C37 · Fuzzing autorizado de software embarcado en banco de pruebas](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md).

### FWHM

- El FWHM es la anchura a media altura.
- La FWHM es el ancho a media altura.
- Una PSF gaussiana de desviación `σ` tiene FWHM `= 2√(2 ln 2) σ = 2,355 σ`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- Con PSF gaussiana: `FWHM = 2,355 σ` y pico normalizado `1/(2πσ²)`.
- Para `σ = 1`: FWHM 2,35 y pico 0,1592; para `σ = 1,5`: 3,53 y 0,0707; para `σ = 2`: 4,71 y 0,0398.
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.
- 🔗 **Se estudia junto con:** PSF, gaussiana, desenfoque, función de transferencia.

📘 **Dónde se aprende** (7 clases): [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md); [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md); [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md) y 1 más.

### FX

- El correlador XF correlaciona en el tiempo y luego transforma; el FX transforma y luego multiplica.

💡 **Cómo se explica en la clase [B46-C15](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md):**
- La diferencia máxima relativa entre el espectro cruzado FX y la FFT de la correlación XF es `5,6 × 10^-16` (error de redondeo).
- F["FX: FFT y producto"] --> EQ["mismo espectro cruzado"]
- ⚠️ **Error frecuente:** Creer que FX y XF difieren. Se corrige con 8.2.
- 🎯 **Por qué importa:** La visibilidad es el dato básico de la imagen, y su ruido determina la sensibilidad. La decisión central: ¿cuántas muestras hay que correlacionar para fijar amplitud y fase con la precisión requerida?
- 🔗 **Se estudia junto con:** visibilidad, ruido de correlación, XF, lag.

📘 **Dónde se aprende** (1 clase): [B46-C15 · Correladores y visibilidades](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md).
