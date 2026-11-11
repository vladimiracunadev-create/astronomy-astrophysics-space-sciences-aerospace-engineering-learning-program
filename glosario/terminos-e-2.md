# Términos · E (parte 2 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · **E** · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-e.md) · **2** · [3](terminos-e-3.md)

### Ensanchamiento Doppler

- El ensanchamiento Doppler viene de la agitación térmica: perfil gaussiano de FWHM `(ν/c)√(8kT ln2/m)`.

💡 **Cómo se explica en la clase [B62-C06](../programa/clases/B62/B62-C06-ensanchamiento-de-lineas-moleculares-natural-doppler-y-por-presion/CLASE.md):**
- El script [ensanchamiento.py](ensanchamiento.py) calcula los tres anchos, compara el Doppler con la Ec.
- python programa/clases/B62/B62-C06-ensanchamiento-de-lineas-moleculares-natural-doppler-y-por-presion/ensanchamiento.py
- 🎯 **Por qué importa:** El ancho de una línea es un termómetro, un velocímetro y un manómetro a la vez. Si no sabes qué mecanismo domina, lees mal la temperatura o la presión.

📘 **Dónde se aprende** (1 clase): [B62-C06 · Ensanchamiento de líneas moleculares: natural, Doppler y por presión](../programa/clases/B62/B62-C06-ensanchamiento-de-lineas-moleculares-natural-doppler-y-por-presion/CLASE.md).

### Ensanchamiento intra-canal

- El ensanchamiento intra-canal es el retardo dentro de un canal.

💡 **Cómo se explica en la clase [B29-C17](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md):**
- El ensanchamiento intra-canal (`9,38 MHz`, `DM = 300`) sería `9,485 ms`, mayor que el pulso: la simulación no lo incluye, lo que la hace optimista.
- Estimar la resolución en `DM` y el ensanchamiento intra-canal.
- 🎯 **Por qué importa:** La medida de dispersión informa de la distancia a la fuente y de la materia que atravesó. Sin desdispersión, un pulso breve se pierde entre canales.

📘 **Dónde se aprende** (1 clase): [B29-C17 · Fenómenos transitorios rápidos](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md).

### Ensanchamiento natural

- El ensanchamiento natural nace de la vida finita del nivel: perfil lorentziano de FWHM `A/(2π)`.

💡 **Cómo se explica en la clase [B62-C06](../programa/clases/B62/B62-C06-ensanchamiento-de-lineas-moleculares-natural-doppler-y-por-presion/CLASE.md):**
- python programa/clases/B62/B62-C06-ensanchamiento-de-lineas-moleculares-natural-doppler-y-por-presion/ensanchamiento.py
- 🎯 **Por qué importa:** El ancho de una línea es un termómetro, un velocímetro y un manómetro a la vez. Si no sabes qué mecanismo domina, lees mal la temperatura o la presión.

📘 **Dónde se aprende** (1 clase): [B62-C06 · Ensanchamiento de líneas moleculares: natural, Doppler y por presión](../programa/clases/B62/B62-C06-ensanchamiento-de-lineas-moleculares-natural-doppler-y-por-presion/CLASE.md).

### Ensanchamiento por presión

- El ensanchamiento por presión nace de las colisiones: perfil lorentziano de semiancho `γ`.

💡 **Cómo se explica en la clase [B62-C06](../programa/clases/B62/B62-C06-ensanchamiento-de-lineas-moleculares-natural-doppler-y-por-presion/CLASE.md):**
- python programa/clases/B62/B62-C06-ensanchamiento-de-lineas-moleculares-natural-doppler-y-por-presion/ensanchamiento.py
- 🎯 **Por qué importa:** El ancho de una línea es un termómetro, un velocímetro y un manómetro a la vez. Si no sabes qué mecanismo domina, lees mal la temperatura o la presión.

📘 **Dónde se aprende** (1 clase): [B62-C06 · Ensanchamiento de líneas moleculares: natural, Doppler y por presión](../programa/clases/B62/B62-C06-ensanchamiento-de-lineas-moleculares-natural-doppler-y-por-presion/CLASE.md).

### Ensanchamiento viscoso

- El ensanchamiento viscoso hace crecer la varianza como `2νt`.

💡 **Cómo se explica en la clase [B73-C16](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md):**
- Descripción larga: las tres escalas del anillo (marea, cizalla y resonancia) son del orden de decenas de miles de kilómetros y horas; el ensanchamiento viscoso, de miles de años con parámetros ilustrativos.
- El script [anillos.py](anillos.py) calcula límites de Roche y Hill, la cizalla, las resonancias de tres lunas y el ensanchamiento viscoso (comprueba Roche rígido < Hill < fluido, Kepler dentro del 0,5 % y difusión numérica dentro del 1 %).
- 🎯 **Por qué importa:** Un anillo existe donde las mareas impiden que las partículas se junten, se ensancha por viscosidad y se estructura por resonancias con las lunas. La decisión central: ¿qué escalas fijan dónde hay un anillo, cuánto dura y dónde lo moldean las lunas?

📘 **Dónde se aprende** (1 clase): [B73-C16 · Dinámica de anillos](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md).

### Ensayo de la Luna

- El ensayo de la Luna compara la aceleración de la Luna con `g` reducida por `(R/r)²`.

💡 **Cómo se explica en la clase [B71-C02](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md):**
- Repetir el ensayo de la Luna: aceleración cinemática frente a gravitacional.
- La evidencia es la ficha de la gravitación con el ensayo de la Luna del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** La ley de gravitación convierte las leyes de Kepler de reglas empíricas en consecuencias de una fuerza. La decisión central: ¿cuánto vale la aceleración gravitatoria a una distancia dada y qué te dice sobre la masa del cuerpo central?

📘 **Dónde se aprende** (1 clase): [B71-C02 · Ley de gravitación universal](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md).

### Enstatita

- La forsterita (Mg₂SiO₄) y la fayalita (Fe₂SiO₄) son los extremos del olivino; la enstatita (MgSiO₃) es un piroxeno.

💡 **Cómo se explica en la clase [B55-C12](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md):**
- Se resuelve el sistema con pivote parcial: forsterita 30,000000, fayalita 10,000000 y enstatita 60,000000 %, con error máximo `3,6 × 10⁻¹⁴`.
- Un meteorito sintético formado por forsterita 30 %, fayalita 10 % y enstatita 60 % en masa, del que se obtienen los óxidos MgO, FeO y SiO₂.
- 🎯 **Por qué importa:** Un meteorito se describe por su análisis químico, pero lo que interesa es qué minerales lo forman y cómo se compara con otros materiales. La decisión central: ¿qué mezcla de minerales reproduce una composición de óxidos, y qué dicen sus cocientes frente a una referencia?

📘 **Dónde se aprende** (1 clase): [B55-C12 · Geoquímica de meteoritos](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md).

### Entalpía

- La entalpía `H` es una magnitud de energía que, a presión constante, mide el calor intercambiado en una reacción.
- La entalpía `h = u + p v` (para gas ideal calórico, `h = c_p T`) es la energía de flujo por kg.
- La entalpía `h = u + p v` incluye el trabajo de flujo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C12](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md):**
- Las entalpías de formación en kJ/mol a 298,15 K (S1, S2): `H₂O(g) = −241,826 ± 0,040`;
- La diferencia, `88,008 kJ/mol`, es el doble de la entalpía de vaporización (`2 × 44,004`), porque se producen dos moles de agua que o bien quedan líquidos o bien son vapor (C10).
- 🎯 **Por qué importa:** Cualquier combustible, de una hoguera a un cohete, libera energía porque los productos están en un estado más estable que los reactivos. ¿Cuánta energía por kilogramo?

📘 **Dónde se aprende** (4 clases): [B06-C12 · Termoquímica y energía de reacción](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md); [B79-C10 · Primera ley de la termodinámica en sistemas abiertos](../programa/clases/B79/B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md); [B79-C13 · Entalpía de flujo y entalpía total](../programa/clases/B79/B79-C13-entalpia-de-flujo-y-entalpia-total/CLASE.md); [B106-C05 · Suministro y generación de oxígeno](../programa/clases/B106/B106-C05-suministro-y-generacion-de-oxigeno/CLASE.md).

### Entalpía de formación estándar

- La entalpía de formación estándar `Δ_fH°` es la de formar un mol de un compuesto a partir de sus elementos en su estado estándar a 298,15 K y 1 bar; para un elemento en su forma estándar vale cero.

💡 **Cómo se explica en la clase [B06-C12](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md):**
- El NIST WebBook da para el vapor de agua una entalpía de formación estándar de −241,826 ± 0,040 kJ/mol y para el agua líquida de −285,830 ± 0,040 kJ/mol (S1).
- Definir entalpía de reacción y entalpía de formación estándar.
- 🎯 **Por qué importa:** Cualquier combustible, de una hoguera a un cohete, libera energía porque los productos están en un estado más estable que los reactivos. ¿Cuánta energía por kilogramo?

📘 **Dónde se aprende** (1 clase): [B06-C12 · Termoquímica y energía de reacción](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md).

### Entalpía de reacción

- La entalpía de reacción `Δ_rH` es el cambio de entalpía por mol de reacción tal como está escrita; es negativa si la reacción libera energía (exotérmica) y positiva si la absorbe (endotérmica).

💡 **Cómo se explica en la clase [B06-C12](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md):**
- La entalpía no dice si la reacción ocurre sola (espontaneidad, B05), ni con qué rapidez (C14), ni qué parte de la energía se aprovecha.
- El cambio entre ambos, −890,30 kJ/mol, es la entalpía de la reacción.
- 🎯 **Por qué importa:** Cualquier combustible, de una hoguera a un cohete, libera energía porque los productos están en un estado más estable que los reactivos. ¿Cuánta energía por kilogramo?

📘 **Dónde se aprende** (1 clase): [B06-C12 · Termoquímica y energía de reacción](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md).

### Entalpia de sublimación

- La entalpia de sublimación `L` mide cuánta energía cuesta pasar una mol de sólido a gas.

💡 **Cómo se explica en la clase [B67-C03](../programa/clases/B67/B67-C03-muestreo-criogenico-y-preservacion-de-volatiles-en-muestras/CLASE.md):**
- La derivada de `ln p` respecto de `1/T` da la entalpia de sublimación implícita: `50,63 kJ/mol` a `150 K`, `51,03` a `200 K` y `51,14` a `250 K`.
- Ejercicio 7 · autónomo. ¿Cuál es la entalpia de sublimación implícita a `200 K`?
- 🎯 **Por qué importa:** Un error de manipulación de unos grados puede cambiar la pérdida en órdenes de magnitud, porque la presión de vapor del hielo crece exponencialmente con la temperatura. La decisión central: ¿hasta qué temperatura y por cuánto tiempo se puede manipular una muestra sin que la pérdida invalide la medida?

📘 **Dónde se aprende** (1 clase): [B67-C03 · Muestreo criogénico y preservación de volátiles en muestras](../programa/clases/B67/B67-C03-muestreo-criogenico-y-preservacion-de-volatiles-en-muestras/CLASE.md).

### Entalpía de vaporización

- La entalpía de vaporización `ΔH_vap` es la energía por mol necesaria para evaporar un líquido (C12).

💡 **Cómo se explica en la clase [B06-C10](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md):**
- La entalpía de vaporización del agua a 298 K se obtiene de las entalpías de formación del NIST: `ΔfH(vapor) = −241,826 kJ/mol` y `ΔfH(líquido) = −285,830 kJ/mol`, de modo que `ΔH_vap = 44,004 kJ/mol` (S2).
- 🎯 **Por qué importa:** En Marte, la temperatura media es 214 K y la presión media en superficie 6,36 mb (S1). Ese valor está casi en el punto triple del agua, la presión mínima a la que puede existir agua líquida (S2).

📘 **Dónde se aprende** (1 clase): [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md).

### Entalpía sensible

- La entalpía sensible es `H(T) − H₂₉₈`.

🎯 **Por qué importa (clase B79-C14):** B06-C09 trata gases en general; aquí hacen falta propiedades termofísicas a alta temperatura con fuente. Sin ellas, las toberas y las turbinas se dimensionan con un `γ` que no existe a 2000–3000 K.

📘 **Dónde se aprende** (1 clase): [B79-C14 · Propiedades de gases calientes](../programa/clases/B79/B79-C14-propiedades-de-gases-calientes/CLASE.md).

### Entalpía total

- La entalpía total `c_p T₀ = c_p T + V²/2` se conserva en flujo adiabático estacionario.
- La entalpía total `h₀ = h + V²/2 = c_p T₀`.

💡 **Cómo se explica en la clase [B79-C13](../programa/clases/B79/B79-C13-entalpia-de-flujo-y-entalpia-total/CLASE.md):**
- En un choque normal en aire a `M₁ = 2`, `h₀ = 452,104 kJ/kg` a ambos lados: la presión total baja, pero la entalpía total se conserva; la pérdida está en la presión total (C07).
- La entalpía total no cambia en el flujo adiabático sin trabajo, pero la presión total sí cae si hay irreversibilidades.
- 🎯 **Por qué importa:** El concepto de energía de flujo es la base del análisis de motores; ninguna clase del tronco lo trata. Con `h₀` se obtiene el límite de velocidad de escape y se entiende por qué la temperatura total no cambia en un choque.

📘 **Dónde se aprende** (2 clases): [B79-C05 · Dinámica de fluidos compresibles](../programa/clases/B79/B79-C05-dinamica-de-fluidos-compresibles/CLASE.md); [B79-C13 · Entalpía de flujo y entalpía total](../programa/clases/B79/B79-C13-entalpia-de-flujo-y-entalpia-total/CLASE.md).

### Entero

- Un número natural sirve para contar: 1, 2, 3… Un entero añade el cero y los negativos: −3, 0, 5.

💡 **Cómo se explica en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- Los enteros permiten decir «cinco grados bajo cero» o «diez minutos antes del lanzamiento» (volveremos en C09).
- Sumar y restar decimales exige alinear la coma; multiplicar, contar las cifras decimales del resultado (la suma de las de los factores); dividir, convertir si hace falta el divisor en entero desplazando la coma en ambos.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.

📘 **Dónde se aprende** (1 clase): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md).

### Enterramiento

- El enterramiento convierte superficie en manto.

💡 **Cómo se explica en la clase [B60-C04](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md):**
- El enterramiento es `F_ent = F_acc (s/ML)⁴`, de modo que la superficie se llena hasta 1 ML y el exceso se entierra.
- Por flujos: acreción, desorción, enterramiento, intercambio.
- 🎯 **Por qué importa:** Un modelo de dos fases trata todo el hielo como si estuviera expuesto en la superficie; en la realidad la mayor parte queda enterrada bajo capas posteriores. La decisión central: ¿qué cambia en la predicción de cuánto hielo se libera al calentar si se distingue la superficie del manto?

📘 **Dónde se aprende** (1 clase): [B60-C04 · Balance químico gas-grano: modelos de tres fases](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md).

### Entorno análogo

- El entorno análogo reproduce solo parte de las condiciones.

💡 **Cómo se explica en la clase [B97-C18](../programa/clases/B97/B97-C18-pruebas-en-entornos-analogos/CLASE.md):**
- La evidencia es el plan de campaña de pruebas en un entorno análogo del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *plan de campaña de pruebas en un entorno análogo*: tabla de `n` con 0, 1 y 2 fallas, tasa de aprobación simulada, velocidad y descarga de peso escaladas, y los límites del análogo.
- 🎯 **Por qué importa:** Declarar «el robot funciona» tras diez pruebas buenas no dice nada sin una confiabilidad y una confianza; y una prueba en la Tierra con el robot completo solo se parece a una en Marte si se corrige el peso.

📘 **Dónde se aprende** (1 clase): [B97-C18 · Pruebas en entornos análogos](../programa/clases/B97/B97-C18-pruebas-en-entornos-analogos/CLASE.md).

### Entorno relevante

- El entorno relevante es el de prueba que reproduce lo esencial del uso.

🎯 **Por qué importa (clase B78-C19):** Una tecnología con un buen desempeño en papel puede estar lejos de volar. La decisión central: ¿en qué nivel está una tecnología según la evidencia que tiene, y qué nivel tiene un sistema formado por componentes de madureces distintas?

📘 **Dónde se aprende** (1 clase): [B78-C19 · Madurez tecnológica TRL](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md).

### Entorno virtual

- Un entorno virtual es una carpeta con su propio intérprete de Python y sus propios paquetes, aislada del resto del sistema; permite que proyectos con versiones incompatibles convivan (S1).

💡 **Cómo se explica en la clase [B07-C13](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md):**
- Un entorno virtual les da a cada uno su carpeta propia (S1).
- Explicar qué es un entorno virtual y por qué se usa uno por proyecto.
- 🎯 **Por qué importa:** «En mi computador funciona» es la frase más cara de la informática científica: el programa depende, sin decirlo, de la versión de Python y de cada biblioteca instalada. Si cambian, los resultados pueden cambiar o el programa fallar con un `ModuleNotFoundError`.

📘 **Dónde se aprende** (1 clase): [B07-C13 · Entornos y dependencias con uv](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md).

### Entrada

- La entrada son los datos que recibe; la salida, lo que devuelve.
- La entrada `u` es lo que tú puedes aplicar (aquí, el par `τ`).
- Una entrada es un registro de la cadena.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C01](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md):**
- Piensa en un algoritmo como una caja con una ranura de entrada y otra de salida.
- E["Entrada<br/>lista de períodos"] --> P["Pasos<br/>recorrer, comparar, actualizar"]
- 🎯 **Por qué importa:** En astronomía casi todo resultado pasa por un procedimiento repetible: reducir imágenes, ajustar una órbita, buscar el máximo de una curva de luz. Si no puedes describir el procedimiento con precisión, no puedes ejecutarlo en un computador ni dárselo a otra persona para que lo repita.

📘 **Dónde se aprende** (5 clases): [B07-C01 · Pensamiento algorítmico](../programa/clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md); [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md); [B105-C22 · Sistema neuroendocrino y respuesta al estrés en vuelo](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md); [B122-C09 · Preservación de evidencias y cadena de custodia de datos de incidentes](../programa/clases/B122/B122-C09-preservacion-de-evidencias-y-cadena-de-custodia-de-datos-de-incidentes/CLASE.md); [B128-C09 · Apoyo multilingüe y glosarios](../programa/clases/B128/B128-C09-apoyo-multilingue-y-glosarios/CLASE.md).

### Entrada balística

- La entrada balística no usa sustentación.

💡 **Cómo se explica en la clase [B77-C14](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md):**
- Escribir la ecuación de movimiento de una entrada balística.
- El script [reentrada.py](reentrada.py) integra una entrada balística para tres `β` y cuatro ángulos y la contrasta con la solución cerrada; añade una integración con gravedad y Tierra esférica (comprueba error de `a_max` < 5e-3 y dispersión entre `β` < 5e-3).
- 🎯 **Por qué importa:** La desaceleración máxima fija la carga sobre la carga útil y sobre la tripulación. La decisión central: ¿qué ángulo de entrada limita la desaceleración y de qué propiedades del vehículo no depende?

📘 **Dónde se aprende** (1 clase): [B77-C14 · Dinámica de reentrada](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md).

### Entrada base

- La entrada seguida es la ejecución con entrada transformada, y la entrada base, la original.

💡 **Cómo se explica en la clase [B23-C06](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md):**
- *Descripción textual:* la entrada base `x` se transforma con `g` y ambas se pasan por el programa; la salida base `y` se transforma con `h` (la transformación esperada); se comprueba que `y'` coincide con `h(y)` dentro de la tolerancia.
- 🎯 **Por qué importa:** El movimiento de un satélite con achatamiento terrestre (J2) no tiene solución cerrada, y tu código no tiene un valor correcto con el que compararse.

📘 **Dónde se aprende** (1 clase): [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md).

### Entrada seguida

- La entrada seguida es la ejecución con entrada transformada, y la entrada base, la original.

🎯 **Por qué importa (clase B23-C06):** El movimiento de un satélite con achatamiento terrestre (J2) no tiene solución cerrada, y tu código no tiene un valor correcto con el que compararse.

📘 **Dónde se aprende** (1 clase): [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md).

### Entrante

- El cruce saliente ocurre antes del apoapsis de la transferencia y el entrante después.

💡 **Cómo se explica en la clase [B75-C21](../programa/clases/B75/B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md):**
- Una elipse tangente a la órbita terrestre con apoapsis a `1,8 au` y salida en la longitud `100°` corta la órbita de Marte primero a `1,5566 au` en la longitud `227,53°` tras `164,69 d` (cruce saliente) y luego a `1,3879 au` en `355,07°` tras `484,21 d` (entrante).
- Distinguir el cruce saliente y el entrante.
- ⚠️ **Error frecuente:** Usar el cruce entrante sin pensar en el tiempo. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una transferencia que apunta al radio medio de Marte puede pasar por dentro o por fuera de su órbita real, que es excéntrica. La decisión central: ¿dónde corta una elipse de transferencia a la órbita de Marte, a qué distancia y cuánto tarda en llegar allí?

📘 **Dónde se aprende** (1 clase): [B75-C21 · Intersección de cónicas en transferencias](../programa/clases/B75/B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md).

### Entre comillas

- Un campo que contiene el delimitador se pone entre comillas.

💡 **Cómo se explica en la clase [B07-C08](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md):**
- Junto a él hay un segundo archivo, [datos_sinteticos_sucios.csv](datos_sinteticos_sucios.csv), inventado para esta clase y con errores a propósito: un valor vacío, un texto no numérico, un decimal con coma entre comillas y una fila con un campo de más.
- 🎯 **Por qué importa:** Un archivo CSV parece trivial y por eso engaña: todo se lee como texto, un decimal con coma rompe una columna, una línea vacía pasa inadvertida, y una codificación equivocada convierte «Júpiter» en símbolos raros. Un análisis hecho sobre datos mal leídos puede ser plausible y erróneo a la vez.

📘 **Dónde se aprende** (1 clase): [B07-C08 · Lectura de archivos CSV](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md).

### Entrelazado

- El entrelazado de profundidad `I` reparte los octetos de `I` palabras: el octeto `j` del flujo es el símbolo `j // I` de la palabra `j % I`.

💡 **Cómo se explica en la clase [B94-C02](../programa/clases/B94/B94-C02-entrelazado-y-concatenacion-de-codigos/CLASE.md):**
- A `p = 0,05` no hace falta entrelazar; a `p = 0,09` el número total de errores supera la capacidad (80 octetos por bloque) y el entrelazado ya no ayuda; la ventana útil está en medio (`p = 0,07`), donde pasa de 27 a 30.
- Límite: el entrelazado no reduce el número total de errores, solo su distribución, y añade retardo y memoria (`I` palabras).
- ⚠️ **Error frecuente:** Creer que el entrelazado reduce los errores. Solo los reparte; se corrige con 8.4.
- 🎯 **Por qué importa:** El decodificador de Viterbi falla en ráfagas y los desvanecimientos también. La decisión central: ¿qué profundidad de entrelazado hace falta para que una ráfaga de `B` octetos no sature ninguna palabra, y qué ganancia da frente a no entrelazar?

📘 **Dónde se aprende** (1 clase): [B94-C02 · Entrelazado y concatenación de códigos](../programa/clases/B94/B94-C02-entrelazado-y-concatenacion-de-codigos/CLASE.md).

### Entrelazado de profundidad I

- El entrelazado de profundidad `I` reparte los octetos de `I` palabras para dispersar ráfagas de errores.

💡 **Cómo se explica en la clase [B89-C09](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md):**
- Leer la tabla de bloques y profundidad de entrelazado de la CCSDS 131.0-B-5.
- 🎯 **Por qué importa:** La codificación es la herramienta que permite cerrar enlaces de espacio profundo con potencias modestas: cada decibelio de ganancia de código equivale a una antena más grande o a más potencia. La decisión central: ¿cuánta redundancia añadir y cuánto `Eb/N0` se ahorra con ella?

📘 **Dónde se aprende** (1 clase): [B89-C09 · Codificación correctora de errores](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md).

### Entropía

- La entropía (en sentido informal) es cuánto desorden hay en los datos: mayor entropía, menor compresión.
- La entropía mide cuántos mecanismos se mezclan.
- La entropía mide cuánta incertidumbre hay entre lecturas.

💡 **Cómo se explica en la clase [B14-C07](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md):**
- No se puede decir un número exacto sin medirlo; la regla es: baja entropía, alta compresión.
- 🎯 **Por qué importa:** Una simulación o un instrumento moderno produce series de millones de muestras con sus metadatos. Guardarlas en texto es lento y pesado; cargarlas enteras en memoria para leer un fragmento es inviable.

📘 **Dónde se aprende** (3 clases): [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md); [B69-C04 · Polarimetría SAR](../programa/clases/B69/B69-C04-polarimetria-sar/CLASE.md); [B119-C32 · Interpretación de tratados internacionales](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md).

### Entropía comóvil

- La entropía comóvil `s a³`.

🎯 **Por qué importa (clase B40-C03):** Los neutrinos contribuyen a la densidad de radiación y condicionan el ritmo de expansión. La decisión central: ¿cuál es la temperatura del fondo de neutrinos y cuánta radiación añade?

📘 **Dónde se aprende** (1 clase): [B40-C03 · Desacoplamiento de neutrinos y fondo cósmico de neutrinos](../programa/clases/B40/B40-C03-desacoplamiento-de-neutrinos-y-fondo-cosmico-de-neutrinos/CLASE.md).

### Entropía de Shannon

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C16):** La compresión sin pérdida está acotada por la entropía; la con pérdida cambia fidelidad por volumen. La decisión central: ¿cuántos bits por píxel necesita la imagen y cuánto error se acepta a cambio de menos datos?

📘 **Dónde se aprende** (1 clase): [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md).

### ENU

- Velocidad radial: razón de cambio del rango. ENU: marco local este–norte–arriba.

💡 **Cómo se explica en la clase [B96-C05](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md):**
- Con `d = r_sat − r_est` en ECEF y los vectores unitarios ENU `ê`, `n̂`, `û`: `E = d·ê`, `N = d·n̂`, `U = d·û`;
- P["Posicion ECEF del satelite"] --> E["Marco local ENU"]
- 🎯 **Por qué importa:** Para que una antena apunte y un receptor enganche, la estación debe conocer de antemano el azimut, la elevación y el corrimiento de frecuencia. La decisión central: ¿hacia dónde apuntar y qué frecuencia esperar en cada instante?

📘 **Dónde se aprende** (1 clase): [B96-C05 · Estaciones de seguimiento](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md).

### Enumeración

- El método voraz ordena por ganancia de `ln R` por kg; la enumeración prueba todos los casos.

💡 **Cómo se explica en la clase [B83-C23](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md):**
- La enumeración exacta confirma la elección.
- Asignar redundancia bajo un presupuesto de masa por un método voraz y por enumeración.
- 🎯 **Por qué importa:** Duplicar todo es imposible por masa y a veces contraproducente; no duplicar nada deja una misión frágil. La decisión central: ¿qué unidades duplicar, con qué esquema y cuánta confiabilidad compra cada kilogramo?

📘 **Dónde se aprende** (1 clase): [B83-C23 · Redundancia y tolerancia a fallos de misión](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md).

### Enumeración exacta

- Una simulación de Monte Carlo muestrea qué riesgos ocurren; la enumeración exacta suma las probabilidades de los 2¹⁰ casos.

💡 **Cómo se explica en la clase [B83-C16](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md):**
- La probabilidad de que el retraso no supere la reserva es 30,13 % por enumeración exacta y 30,27 % por Monte Carlo.
- *Descripción textual:* cada riesgo da un puntaje y una exposición; sumados definen el retraso total, que se estudia por Monte Carlo y por enumeración exacta; la probabilidad de caber en la reserva se mejora mitigando los mayores puntajes.
- 🎯 **Por qué importa:** Una lista de riesgos sin números no dice cuánta reserva hace falta ni qué mitigar primero. La decisión central: ¿qué riesgos mitigar primero y alcanza la reserva de calendario para los que no se mitiguen?

📘 **Dónde se aprende** (1 clase): [B83-C16 · Gestión de riesgos técnicos](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md).

### Envejecimiento

- El envejecimiento eleva `α` por radiación y contaminación.

💡 **Cómo se explica en la clase [B85-C05](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md):**
- *Descripción textual:* el recubrimiento da `α/ε`, de ahí sale la temperatura; el envejecimiento da `α_EOL` y una segunda temperatura; ambas deben estar dentro del intervalo.
- Descripción larga: el envejecimiento desplaza la pintura blanca unos 40 K; solo uno de los seis recubrimientos cumple el intervalo en BOL y EOL.
- 🎯 **Por qué importa:** Cambiar un recubrimiento es la forma más barata de mover la temperatura de una superficie decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la superficie dentro del intervalo al principio y al final de la vida?

📘 **Dónde se aprende** (1 clase): [B85-C05 · Recubrimientos ópticos térmicos](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md).

### Envoltura

- La envoltura (*wraparound*) devuelve el resultado módulo `2ⁿ`.

💡 **Cómo se explica en la clase [B88-C36](../programa/clases/B88/B88-C36-codificacion-defensiva-y-estandares-de-codigo-seguro/CLASE.md):**
- Paso 2 · Envoltura. `35000 − 65536 = −30536`.
- Paso 4 · Efecto. Un comando positivo pasa a negativo con envoltura.
- 🎯 **Por qué importa:** Un desbordamiento silencioso convierte 35 000 en −30 536 y un comando de giro positivo en negativo. La decisión central: ¿qué operaciones aceptan cualquier entrada y devuelven siempre un resultado dentro del rango?

📘 **Dónde se aprende** (1 clase): [B88-C36 · Codificación defensiva y estándares de código seguro](../programa/clases/B88/B88-C36-codificacion-defensiva-y-estandares-de-codigo-seguro/CLASE.md).

### Envoltura común

- La envoltura común es una fase en que ambas estrellas comparten una envoltura.

💡 **Cómo se explica en la clase [B24-C22](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md):**
- Con hipótesis más realistas (la estrella reacciona al perder masa) el resultado puede ser estable o inestable; si es inestable, la compañera puede acabar dentro de la envoltura (envoltura común), con un desenlace incierto (S3, resumen), o fusionarse (S2).
- Envoltura común: formalismo energético cuestionado (S3).
- 🎯 **Por qué importa:** Una estrella que se expande (C16) o se hincha en una binaria puede llenar la región donde su gravedad domina y verter gas sobre su compañera. Esa transferencia cambia las masas, la órbita y el destino de ambas, y es el camino hacia muchos objetos exóticos.

📘 **Dónde se aprende** (1 clase): [B24-C22 · Evolución binaria: lóbulo de Roche y transferencia de masa](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md).

### Envolvente

- La envolvente de difracción de una rendija es `sinc²`.
- La envolvente es el requisito más estricto de cada fila (mínimo de los límites superiores, máximo de los inferiores).

💡 **Cómo se explica en la clase [B31-C01](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md):**
- Electrones de 50 keV: `λ = 5,3553 × 10⁻¹² m`; con `d = 1 µm` y `L = 1 m`, el espaciado esperado es `5,3553 µm` y la envolvente (`a = 0,1 µm`) se anula en `53,55 µm`.
- electrones de 50 keV: lambda = 5.3553e-12 m ; espaciado de franjas lambda L/d = 5.3553 um ; primer cero de la envolvente en 53.55 um
- 🎯 **Por qué importa:** Sin la dualidad no se entiende la difracción de electrones, los microscopios electrónicos ni la estructura atómica. La decisión central: ¿cuándo importa la longitud de onda de un objeto y cómo se ve en un experimento?

📘 **Dónde se aprende** (2 clases): [B31-C01 · Dualidad onda-partícula](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md); [B121-C05 · Cumplimiento regulatorio en varias jurisdicciones](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md).

### EOL

- BOL y EOL son los extremos de la vida.

💡 **Cómo se explica en la clase [B85-C05](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md):**
- Los que mantienen `250–320 K` en BOL y EOL: pintura blanca.
- El coating a medida (`ε ≈ 0,25`, `α ≈ 0,1` según NASA) en estos números se pasa del intervalo en EOL: `340,49 K`.
- ⚠️ **Error frecuente:** Ignorar el EOL. el caso caliente usa EOL (8.4)
- 🎯 **Por qué importa:** Cambiar un recubrimiento es la forma más barata de mover la temperatura de una superficie decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la superficie dentro del intervalo al principio y al final de la vida?

📘 **Dónde se aprende** (1 clase): [B85-C05 · Recubrimientos ópticos térmicos](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md).

### EOS por tramos

- Una EOS por tramos usa varios politropos unidos en densidades de transición.

💡 **Cómo se explica en la clase [B27-C04](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md):**
- Analogía: una carretera de montaña con un tramo suave y otro empinado.
- Límite: la EOS real tiene más tramos y transiciones de fase.
- 🎯 **Por qué importa:** Las estrellas de neutrones son el único laboratorio de materia más allá de la densidad nuclear. Su EOS no se conoce con precisión; las medidas de masa máxima y de radio la acotan.

📘 **Dónde se aprende** (1 clase): [B27-C04 · Ecuación de estado nuclear](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md).

### EOS rígida

- Una EOS rígida (stiff) sube más rápido `P` con `ρ`.

💡 **Cómo se explica en la clase [B27-C03](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md):**
- Las medidas obligan a ecuaciones de estado más rígidas a alta densidad (C04).
- 🎯 **Por qué importa:** Las masas y radios de las estrellas de neutrones son la mejor ventana a la materia a densidades nucleares. Para interpretarlos hay que saber qué cambia la relatividad respecto de Newton y por qué existe una masa máxima.

📘 **Dónde se aprende** (1 clase): [B27-C03 · Estrellas de neutrones](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md).

### Epiciclo

- Un excéntrico y un epiciclo son dos recursos geométricos para describir el movimiento de un cuerpo (C10).
- El epiciclo es un círculo pequeño cuyo centro recorre el deferente, con el planeta sobre él.
- Un epiciclo es la pequeña oscilación radial de una estrella alrededor del radio guía `R_g`, el de la órbita circular con su mismo momento angular `L = Θ R_g`.

💡 **Cómo se explica en la clase [B02-C10](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md):**
- Según S1, Ptolomeo combinó el excéntrico, el epiciclo y el ecuante para modelar el Sol, la Luna y los planetas, y el conjunto explicaba los movimientos observados dentro de la precisión de su época, incluido el retroceso aparente.
- S2 subraya que Copérnico mantuvo el movimiento circular, de modo que sus órbitas todavía usaban círculos sobre círculos, parecidos a los epiciclos y excéntricos de sus predecesores; sus tablas eran solo ligeramente mejores que las existentes.
- 🎯 **Por qué importa:** La pregunta «¿se mueve la Tierra o el cielo?» se puede responder hoy en una línea, pero en 1500 una persona razonable podía defender cualquiera de las dos. La pregunta motivadora es: ¿con qué criterios se elige entre dos modelos que predicen casi lo mismo?

📘 **Dónde se aprende** (3 clases): [B02-C03 · Astronomía griega y helenística](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md); [B02-C10 · Geocentrismo y heliocentrismo](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md); [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### E-pliegue

- El e-pliegue `N = ln(a_final/a_inicial)`.

💡 **Cómo se explica en la clase [B40-C01](../programa/clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md):**
- Descripción larga: la rodadura lenta subestima en poco más de un e-pliegue.
- 🎯 **Por qué importa:** Sin un mecanismo para las condiciones iniciales, el modelo FLRW deja sin explicar la planitud y la homogeneidad. La decisión central: ¿cuántos e-pliegues produce un campo que rueda lentamente y cuándo termina la inflación?

📘 **Dónde se aprende** (1 clase): [B40-C01 · Inflación cósmica: motivación y dinámica básica](../programa/clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md).

### Época

- Una época es la fecha a la que se refieren las coordenadas; la precesión es el lento giro del eje de la Tierra, que desplaza el sistema entero unos 50″ al año.
- La época es un número que crece en cada traspaso y que acompaña a cada orden; el vehículo rechaza las de época menor que la mayor vista (*fencing*).
- El marco de referencia (por ejemplo, el ICRS) fija dónde están el ecuador, los ejes y el origen; la época dice a qué fecha se refieren las posiciones, porque las estrellas se mueven.

💡 **Cómo se explica en la clase [B04-C11](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md):**
- Las coordenadas dependen del marco de referencia (hacia dónde apunta el eje `x`) y de la época.
- Una estrella cercana como Próxima se desplaza por movimiento propio del orden de segundos de arco al año, de modo que unas coordenadas sin época pueden estar desplazadas de las actuales.
- ⚠️ **Error frecuente:** Dar coordenadas sin marco ni época. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un catálogo de estrellas da para cada una dos números: dónde está en el cielo. Pero un programa que cruza catálogos, calcula separaciones o apunta un telescopio no trabaja con horas y grados: trabaja con vectores.

📘 **Dónde se aprende** (3 clases): [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md); [B08-C03 · Ascensión recta y declinación](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md); [B98-C08 · Protocolos de relevo de control entre operadores](../programa/clases/B98/B98-C08-protocolos-de-relevo-de-control-entre-operadores/CLASE.md).

### Época J2000

- La época J2000 es el mediodía del 1 de enero de 2000 (TDB en SPICE).

🎯 **Por qué importa (clase B13-C08):** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.

📘 **Dónde se aprende** (1 clase): [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### Épsilon

- El épsilon de la máquina es el menor incremento relativo.

💡 **Cómo se explica en la clase [B88-C41](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md):**
- El error de f32 es del orden de 2,5 épsilon de f32; el de Q15, de 4 LSB (`2,44×10⁻⁴`).
- Relacionar el error con el épsilon y el LSB.
- 🎯 **Por qué importa:** La aritmética del procesador objetivo puede ser distinta de la del escritorio. La decisión central: ¿cuánto se aparta la respuesta con la precisión del objetivo y cumple la tolerancia?

📘 **Dónde se aprende** (1 clase): [B88-C41 · Pruebas SIL y PIL del software de vuelo](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md).

### Épsilon de máquina

- El épsilon de máquina `ε = 2⁻⁵² = 2,22 × 10⁻¹⁶` es el espaciado entre 1 y el siguiente número.

💡 **Cómo se explica en la clase [B11-C25](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md):**
- Calcular el épsilon de máquina y el espaciado (ulp) a distintas magnitudes.
- épsilon de máquina: medido 2.2204e-16 = 2^-52 ; sys.float_info.epsilon = 2.2204e-16
- 🎯 **Por qué importa:** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.

📘 **Dónde se aprende** (1 clase): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md).

### Equidad

- La equidad aquí es el criterio de acceso y reparto justo.
- La equidad aquí es acceso similar entre Estados.

💡 **Cómo se explica en la clase [B119-C18](../programa/clases/B119/B119-C18-etica-y-derechos-en-actividades-espaciales/CLASE.md):**
- Con los demás pesos iguales, B supera a A cuando el peso de equidad es mayor que `0.1304`.
- I y IX con criterios de equidad y cooperación.
- 🎯 **Por qué importa:** El art. I y el art.

📘 **Dónde se aprende** (2 clases): [B119-C18 · Ética y derechos en actividades espaciales](../programa/clases/B119/B119-C18-etica-y-derechos-en-actividades-espaciales/CLASE.md); [B119-C34 · Equidad de acceso al espacio](../programa/clases/B119/B119-C34-equidad-de-acceso-al-espacio/CLASE.md).

### Equilibrio

- El equilibrio es el estado en que `ΣF = 0`.
- El equilibrio es un valor `y*` donde `y′ = 0`.
- El equilibrio es el estado donde la entrada compensa las pérdidas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- No hay equilibrio con cable perfectamente horizontal (`sen 0 = 0`).
- Si `E < m g_n` no despega (la normal de la plataforma completa el equilibrio); si `E > m g_n`, sube con `a` positiva.
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?

📘 **Dónde se aprende** (4 clases): [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md); [B11-C03 · Ecuaciones de primer orden](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md); [B38-C07 · Modelos submalla de formación estelar y retroalimentación](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md); [B54-C19 · Modelos climáticos planetarios](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md).

### Equilibrio de Cournot

- El equilibrio de Cournot es el punto en que cada empresa elige su cantidad dada la de las demás.

💡 **Cómo se explica en la clase [B124-C03](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md):**
- D["demanda P = a − bQ"] --> E["equilibrio de Cournot"]
- *Descripción textual:* la demanda y los costos determinan el equilibrio de Cournot; de él salen las cuotas, el HHI y los márgenes, y el equilibrio se comprueba con mejores respuestas.
- 🎯 **Por qué importa:** Hablar de «mercado upstream» o «downstream» sin medir su concentración deja la discusión en opinión. La decisión central: ¿qué tan concentrado está un mercado y qué margen de precio permite esa concentración?

📘 **Dónde se aprende** (1 clase): [B124-C03 · Mercados downstream y upstream](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md).

### Equilibrio del carbonato

- El equilibrio del carbonato liga `CO₂(aq)`, `HCO₃⁻` y `CO₃²⁻` con `[H⁺]`: `[HCO₃⁻] = K₁c/[H⁺]` y `[CO₃²⁻] = K₁K₂c/[H⁺]²`.

🎯 **Por qué importa (clase B55-C15):** El pH de un océano bajo el hielo condiciona qué minerales precipitan y qué química prebiótica es posible. Se calcula con equilibrios acoplados.

📘 **Dónde se aprende** (1 clase): [B55-C15 · Química de océanos internos](../programa/clases/B55/B55-C15-quimica-de-oceanos-internos/CLASE.md).

### Equilibrio estable

- Un equilibrio estable atrae las trayectorias cercanas; uno inestable las repele.

💡 **Cómo se explica en la clase [B118-C10](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md):**
- Con `S = 150` el equilibrio estable baja a 3944 (menos de la mitad: el término cuadrático también se reduce).
- E -- sí --> F["Dos equilibrios<br/>(uno estable)"]
- 🎯 **Por qué importa:** El término cuadrático de las colisiones cambia la naturaleza del problema: por debajo de cierta fuente hay un equilibrio estable; por encima, no hay equilibrio. La decisión central: ¿qué parámetro (fuente, vida orbital, tasa de colisión) lleva el sistema al umbral y cómo se lee un escenario sin confundirlo con un pronóstico?

📘 **Dónde se aprende** (1 clase): [B118-C10 · Síndrome de Kessler como escenario](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md).

### Equilibrio fotoquímico

- El equilibrio fotoquímico iguala producción y pérdida.

🎯 **Por qué importa (clase B54-C10):** La capa de producción fotoquímica explica por qué hay capas de ozono, ionosferas y neblinas a ciertas alturas. La pregunta motivadora: ¿a qué altura se rompen más moléculas y cómo cambia con el ángulo del Sol?

📘 **Dónde se aprende** (1 clase): [B54-C10 · Fotoquímica atmosférica](../programa/clases/B54/B54-C10-fotoquimica-atmosferica/CLASE.md).

### Equilibrio hidrostático

- El equilibrio hidrostático es el balance entre el gradiente de presión y el peso: `dP/dr = −G m(r) ρ / r²`.
- El equilibrio hidrostático iguala el gradiente de presión del gas con la gravedad.
- El equilibrio hidrostático `dP/dτ = g/κ`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C04](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md):**
- Escribir la ecuación de equilibrio hidrostático y explicar cada término.
- python programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/hidrostatica.py
- 🎯 **Por qué importa:** Una estrella es una bola de gas que lleva miles de millones de años sin cambiar de tamaño. Eso exige que, en cada capa, la presión hacia fuera compense el peso del gas de encima.

📖 **Explicado a fondo:** [Equilibrio hidrostático](esencial/tercera-a-e.md#equilibrio-hidrostático) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B24-C04 · Equilibrio hidrostático estelar](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md); [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md); [B32-C05 · Relación T-τ y estructura térmica de la fotosfera](../programa/clases/B32/B32-C05-relacion-t-y-estructura-termica-de-la-fotosfera/CLASE.md); [B54-C01 · Estructura vertical de atmósferas](../programa/clases/B54/B54-C01-estructura-vertical-de-atmosferas/CLASE.md); [B56-C11 · Atmósfera y superficie de Titán](../programa/clases/B56/B56-C11-atmosfera-y-superficie-de-titan/CLASE.md).

### Equilibrio hidrostático isotermo

- El equilibrio hidrostático isotermo da `P ∝ exp(−z/H)` en capa delgada.

🎯 **Por qué importa (clase B30-C02):** La corona caliente es el origen del viento solar y de gran parte de la actividad. Entender por qué no puede estar en reposo conecta el Sol con el medio interplanetario.

📘 **Dónde se aprende** (1 clase): [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md).

### Equilibrio químico

- Un equilibrio químico es un estado en el que las velocidades de la reacción directa e inversa son iguales y las concentraciones no cambian.

💡 **Cómo se explica en la clase [B06-C13](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md):**
- python programa/clases/B06/B06-C13-equilibrio-quimico/equilibrio.py
- 🎯 **Por qué importa:** Según el cálculo de esta clase, el CO₂ de Marte puede condensarse como hielo o volver al gas según la temperatura. Es un equilibrio entre CO₂ sólido y gas: `CO₂(s) ⇌ CO₂(g)`.

📘 **Dónde se aprende** (1 clase): [B06-C13 · Equilibrio químico](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md).

### Equilibrio térmico

- El equilibrio térmico ocurre cuando el calor generado iguala al que sale.

💡 **Cómo se explica en la clase [B65-C06](../programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/CLASE.md):**
- python programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/marea.py
- 🎯 **Por qué importa:** Un satélite pequeño se enfría rápido; si aun así tiene un interior caliente, algo lo calienta. La decisión central: ¿cuánto calor produce una marea y a qué temperatura de equilibrio llevaría la superficie?

📘 **Dónde se aprende** (1 clase): [B65-C06 · Calentamiento por marea y equilibrio térmico en satélites](../programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/CLASE.md).

### Equilibrio transitorio

- El equilibrio transitorio `N₂/N₁ → λ₁/(λ₂ − λ₁)`.

💡 **Cómo se explica en la clase [B31-C08](../programa/clases/B31/B31-C08-decaimiento-radiactivo/CLASE.md):**
- El cociente `N₂/N₁` tiende al equilibrio transitorio `λ₁/(λ₂ − λ₁) = 0,4286`.
- Descripción larga: el cociente tiende al equilibrio transitorio.
- 🎯 **Por qué importa:** Fechar rocas, medir la edad de objetos y modelar la nucleosíntesis usan estas leyes. La decisión central: ¿cómo se estima una constante de decaimiento y cómo evoluciona una cadena?

📘 **Dónde se aprende** (1 clase): [B31-C08 · Decaimiento radiactivo](../programa/clases/B31/B31-C08-decaimiento-radiactivo/CLASE.md).

### Equinoccio

- El solsticio es el día de mayor o menor altura del Sol; el equinoccio, el día en que `δ = 0`.
- El equinoccio de referencia es esa elección de origen.

💡 **Cómo se explica en la clase [B01-C11](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md):**
- Para `φ = −33,45°`: en el solsticio de diciembre, `δ = −23,44°` y `h = 90° − 10,01° = 79,99°`; en el equinoccio, `h = 56,55°`; en el de junio, `h = 33,11°`.
- La duración del día se obtiene de `cos H₀ = −tan φ · tan δ`, con `H₀` el semiángulo horario del Sol en el horizonte y `día = 2H₀/15° por hora`: da 14,22 h en diciembre, 12,00 h en el equinoccio y 9,78 h en junio.
- 🎯 **Por qué importa:** Antes de cualquier telescopio, la humanidad dedujo mucho del cielo a simple vista. Que el Sol «salga» y «se ponga» es una observación; que la Tierra gire es una interpretación (C05) que explica además el movimiento de todas las estrellas.

📖 **Explicado a fondo:** [Equinoccio y solsticio](esencial/esencial-d-l.md#equinoccio-y-solsticio) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B08-C03 · Ascensión recta y declinación](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md).

### Equivalencia

- Una equivalencia es una regla que relaciona dimensiones distintas bajo un supuesto (por ejemplo, `ν = c/λ`).

💡 **Cómo se explica en la clase [B14-C04](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md):**
- Con una equivalencia explícita, `u.spectral()`, sí se permite: `(1000 * u.nm).to(u.THz, equivalencies=u.spectral())` da `299,792 THz`, igual que `c/λ = 299 792 458 / 10⁻⁶ m` en THz.
- Usar equivalencias (por ejemplo, longitud de onda a frecuencia) de forma explícita.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió al llegar a Marte. NASA atribuye la pérdida a un error de navegación causado por no traducir unidades inglesas a métricas: el software en tierra usaba unidades inglesas y el de a bordo, métricas (S1).

📘 **Dónde se aprende** (1 clase): [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### Equivalencia exacta

- Una equivalencia exacta es una relación definida, sin incertidumbre (1 h = 3600 s).

💡 **Cómo se explica en la clase [B03-C07](../programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/CLASE.md):**
- Usar las equivalencias exactas del SI (1 au, 1 h, 1 km) y las de unidades aceptadas (milla náutica, nudo).
- 🎯 **Por qué importa:** Una cifra de la NASA como «velocidad de escape 11,186 km/s» no significa lo mismo para quien trabaja en m/s ni para quien piensa en km/h. Si conviertes mal, el error no es de redondeo sino de factor: mil, tres mil seiscientos.

📘 **Dónde se aprende** (1 clase): [B03-C07 · Conversión de distancia y velocidad](../programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/CLASE.md).

### Equivalente

- Una proyección conforme conserva los ángulos locales; una equivalente conserva las áreas; ninguna puede conservar a la vez ángulos y áreas (salvo en una esfera, que no cabe en un plano).
- Una proyección equivalente conserva áreas.

💡 **Cómo se explica en la clase [B04-C17](../programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/CLASE.md):**
- Para comparar áreas: una proyección equivalente (no tratada aquí).
- 🎯 **Por qué importa:** Casi todo lo que ves del espacio, de la Tierra o de otro cuerpo, llega en forma de mapa: la superficie de un planeta, el cielo entero, la huella de un satélite. Y un mapa es una proyección.

📘 **Dónde se aprende** (2 clases): [B04-C17 · Proyecciones cartográficas elementales](../programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/CLASE.md); [B53-C18 · Cartografía geológica digital](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md).

### Equivalente a tiempo completo (ETC)

- Turno: bloque de 8 h. Equivalente a tiempo completo (ETC): fracción de una posición 24/7.

🎯 **Por qué importa (clase B96-C03):** Un rol vacío durante un contacto es un contacto perdido. La decisión central: ¿cuánto personal exige cubrir una posición 24/7 y cómo se comprueba que el cronograma no deja huecos?

📘 **Dónde se aprende** (1 clase): [B96-C03 · Roles de control de misión](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md).

### Equivalente en nivel del mar

- Un equivalente en nivel del mar es el cambio de altura del océano si toda esa masa de agua se repartiera uniformemente.

🎯 **Por qué importa (clase B57-C14):** Un glaciar que baja medio metro puede haber perdido mucha o poca masa según lo que se pierda sea hielo o nieve. La decisión central: ¿qué densidad uso para convertir cambios de altura en masa y cuánto cambia el resultado?

📘 **Dónde se aprende** (1 clase): [B57-C14 · Glaciares y criósfera](../programa/clases/B57/B57-C14-glaciares-y-criosfera/CLASE.md).

### Equivalente energético

- El equivalente energético es la energía por litro de O₂ consumido.

🎯 **Por qué importa (clase B104-C10):** El oxígeno de un traje es finito y el trabajo manual consume más que el reposo. La decisión central: ¿cuánto margen queda sobre el consumo esperado si la tasa metabólica de cada tarea varía?

📘 **Dónde se aprende** (1 clase): [B104-C10 · Actividades extravehiculares EVA](../programa/clases/B104/B104-C10-actividades-extravehiculares-eva/CLASE.md).

### Equivalentes

- Dos fracciones son equivalentes si valen lo mismo (`6/8 = 3/4`).
- Dos expresiones son equivalentes si valen lo mismo para todos los valores.

💡 **Cómo se explica en la clase [B03-C13](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md):**
- Comprobar que dos expresiones son equivalentes sustituyendo valores.
- 🎯 **Por qué importa:** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.

📘 **Dónde se aprende** (2 clases): [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md); [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md).

### Equivariante

- Un integrador es equivariante ante una simetría si integrar y luego transformar da lo mismo que transformar y luego integrar.

📘 **Dónde se aprende** (1 clase): [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md).

### Equivocación

- Aquí: el resbalón es un fallo de ejecución (hacer otra cosa de la prevista), el descuido un fallo de memoria, la equivocación un plan equivocado y la violación una desviación deliberada de una regla; esta clasificación se toma como convención didáctica.

💡 **Cómo se explica en la clase [B111-C06](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md):**
- Por tipo: resbalón, descuido, equivocación, violación.
- Distinguir resbalón, descuido, equivocación y violación.
- 🎯 **Por qué importa:** Falta la clase sobre tipos de error, barreras y reporte. La decisión central: ¿dónde se pone el esfuerzo: en culpar al que erró o en reforzar las barreras y las condiciones que dejaron pasar el error?

📘 **Dónde se aprende** (1 clase): [B111-C06 · Gestión del error humano y cultura de seguridad](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md).

### Erosión

- La erosión es `Δe = Re F`.

💡 **Cómo se explica en la clase [B85-C13](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md):**
- Paso 3 · Erosión. `Δe = 3 × 10⁻³⁰ m³ × 2,42 × 10²⁶ = 726 µm`.
- La evidencia es la ficha de erosión por oxígeno atómico del ejercicio 12 (sección 20).
- ⚠️ **Error frecuente:** Presentar la erosión como medición. se corrige con la sección 10
- 🎯 **Por qué importa:** Un polímero exterior puede desaparecer en meses en la cara de proa a baja altitud. La decisión central: ¿cuánto espesor pierde una superficie por año según la altitud y la orientación, y qué protección dura la misión?

📘 **Dónde se aprende** (1 clase): [B85-C13 · Efectos de oxígeno atómico](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md).

### Erradicación

- La detección es notar el incidente; la contención limita su alcance; la erradicación elimina la causa; la recuperación restablece el servicio; las lecciones aprendidas mejoran el plan.

🎯 **Por qué importa (clase B122-C06):** B96-C15 trata emergencias operativas, no incidentes cibernéticos. La decisión central: ¿cuánto reduce el daño esperado acortar la detección o la contención?

📘 **Dónde se aprende** (1 clase): [B122-C06 · Respuesta a incidentes cibernéticos en operaciones de misión](../programa/clases/B122/B122-C06-respuesta-a-incidentes-ciberneticos-en-operaciones-de-mision/CLASE.md).

### Error

- El error de una medición es la diferencia entre el valor medido y el verdadero (desconocido).
- El error es la diferencia entre el resultado simulado y el exacto.
- Si `f` tiene derivada continua de orden `n + 1`, el error es `f(x) − P_n(x) = f^{(n+1)}(ξ) ω(x)/(n + 1)!` para algún `ξ` en el intervalo (S1, ec. 3.3.5).
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- Repetir lecturas reduce el error aleatorio, no el sistemático (S1).
- Imagina disparar a una diana: un grupo de impactos muy juntos pero lejos del centro es preciso con error sistemático; impactos dispersos alrededor del centro es exacto con error aleatorio.
- ⚠️ **Error frecuente:** Creer que más lecturas eliminan todo error. Ejercicio 8.
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.

📘 **Dónde se aprende** (6 clases): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B07-C05 · Bucles y simulaciones sencillas](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md); [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md); [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md); [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md); [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md).

### Error a lo largo de la trayectoria

- El error a lo largo de la trayectoria (*along-track*) es la componente del error en la dirección de la velocidad.

🎯 **Por qué importa (clase B72-C01):** Un propagador kepleriano cabe en tres líneas y se usa en cualquier curso, pero ¿hasta cuándo se puede confiar en él? La decisión central: ¿cuál perturbación domina en cada altitud y en cuánto tiempo la solución de dos cuerpos deja de servir?

📘 **Dónde se aprende** (1 clase): [B72-C01 · Limitaciones del problema de dos cuerpos](../programa/clases/B72/B72-C01-limitaciones-del-problema-de-dos-cuerpos/CLASE.md).

### Error absoluto

- El error absoluto de un valor `x` respecto a una referencia `x₀` es `|x − x₀|`, con las unidades de `x`.
- El error absoluto `Δx` tiene la unidad de `x`; el error relativo `Δx/|x|` no tiene unidad.

💡 **Cómo se explica en la clase [B03-C19](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md):**
- Si `x = 365 ± 0,5`, el error absoluto es 0,5 d y el relativo `0,5/365 = 0,137 %`.
- Para `s = x + y` o `x − y`, el error absoluto del peor caso es `Δx + Δy`.
- 🎯 **Por qué importa:** Con los datos de la Tierra redondeados a tres cifras (semieje `1,50 × 10⁸ km` y período `365 d`), la rapidez orbital sale `29,89 km/s`. La NASA publica 29,78 km/s.

📘 **Dónde se aprende** (2 clases): [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md).

### Error acotado

- El error acotado de un método simpléctico significa que la energía oscila alrededor de su valor inicial sin deriva sistemática.

💡 **Cómo se explica en la clase [B73-C09](../programa/clases/B73/B73-C09-integracion-de-largo-plazo/CLASE.md):**
- Analogía: un reloj de péndulo oscila alrededor de la hora correcta (error acotado) mientras que otro se atrasa un poco cada día (deriva secular); tras muchos días el segundo está muy lejos aunque cada día su error sea pequeño.
- Distinguir error acotado (simpléctico) de deriva secular (RK4).
- 🎯 **Por qué importa:** La estabilidad del sistema solar se estudia con integraciones de millones de órbitas, donde un integrador con deriva secular de energía inventa una dinámica que no existe. La decisión central: ¿qué integrador elijo para un horizonte largo y cómo reconozco que ha derivado?

📘 **Dónde se aprende** (2 clases): [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md); [B73-C09 · Integración de largo plazo](../programa/clases/B73/B73-C09-integracion-de-largo-plazo/CLASE.md).

### Error acumulado

- Un error acumulado es el que crece al repetir una predicción.

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- Estimar el error acumulado de una predicción periódica.
- ⚠️ **Error frecuente:** No estimar el error acumulado. Ejercicio 5.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (1 clase): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md).

### Error aleatorio

- El error aleatorio es el componente que varía de forma impredecible en réplicas (VIM 2.19; aquí se usa su sentido habitual).
- El error aleatorio varía de lectura a lectura y se reduce con más lecturas.
- El error aleatorio varía de una medida a otra; el sesgo no.

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- Repetir lecturas reduce el error aleatorio, no el sistemático (S1).
- Imagina disparar a una diana: un grupo de impactos muy juntos pero lejos del centro es preciso con error sistemático; impactos dispersos alrededor del centro es exacto con error aleatorio.
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.

📘 **Dónde se aprende** (3 clases): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md); [B132-C02 · Arqueología de observatorios y de instrumentos antiguos](../programa/clases/B132/B132-C02-arqueologia-de-observatorios-y-de-instrumentos-antiguos/CLASE.md).

### Error angular

- El error angular entre dos actitudes es el ángulo de la rotación relativa `q₁* ⊗ q₂` (C15).

💡 **Cómo se explica en la clase [B10-C20](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md):**
- El error angular es `8 × 10⁻⁵ rad` en un solo paso.
- Medir el error angular de la actitud con una métrica estable.
- 🎯 **Por qué importa:** Los giróscopos de un satélite miden la velocidad angular en ejes del cuerpo. Para saber hacia dónde apunta una cámara, hay que integrar esa velocidad en el tiempo, miles de veces.

📘 **Dónde se aprende** (1 clase): [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md).

### Error cuadrático medio

- El sesgo de una medida es `E[error]`; el error cuadrático medio es `E[error²] = Var + sesgo²`.
- Su error cuadrático medio es `E[(θ̂ − θ)²] = Var(θ̂) + sesgo²`.
- El error cuadrático medio es `ECM = Var + sesgo²`.

💡 **Cómo se explica en la clase [B12-C04](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md):**
- Distinguir sesgo de dispersión y calcular el error cuadrático medio.
- Calcula el error cuadrático medio y explica por qué promediar no lo arregla.
- 🎯 **Por qué importa:** Un ingeniero no maneja distribuciones completas; maneja «la medida es 150,0 m con una incertidumbre de 3 m». Esa frase usa exactamente una esperanza y una desviación típica.

📘 **Dónde se aprende** (3 clases): [B12-C04 · Esperanza y varianza](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md); [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md); [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md).

### Error cuadrático medio (RMSE)

- El error cuadrático medio (RMSE) es `√[Σ(xᵢ − x_ref)²/n]`.

💡 **Cómo se explica en la clase [B13-C03](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md):**
- *Descripción textual:* de una serie salen dos cantidades independientes, el sesgo y la desviación típica; juntas componen el error cuadrático medio.
- Calcular sesgo, desviación típica y error cuadrático medio de una serie.
- 🎯 **Por qué importa:** Un telémetro láser que mide la distancia a un reflector de prueba puede dar lecturas muy agrupadas pero todas desplazadas: es repetible y, aun así, está mal. Otro puede dar lecturas dispersas que, en promedio, caen sobre el valor correcto.

📘 **Dónde se aprende** (1 clase): [B13-C03 · Exactitud frente a precisión](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md).

### Error de acimut

- El error de acimut y el error de altura del eje.

💡 **Cómo se explica en la clase [B43-C17](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md):**
- En el meridiano la deriva depende solo del error de acimut e no depende de la declinación (filas 1 y 2).
- Errores ilustrativos de `10'` en acimut y `6'` en altura.
- ⚠️ **Error frecuente:** Confundir los errores de acimut y altura. Se corrige con 8.1.
- 🎯 **Por qué importa:** La alineación polar se corrige midiendo la deriva de una estrella. La decisión central: ¿qué deriva produce un error de acimut o de altura y cómo se invierte para corregirlo?

📘 **Dónde se aprende** (1 clase): [B43-C17 · Alineación polar](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md).

### Error de ajuste

- El error de ajuste `σ²_fit = μ (d/r₀)^{5/3}`.

💡 **Cómo se explica en la clase [B42-C15](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md):**
- Doblar el paso (la mitad de actuadores por lado) multiplica el error de ajuste por 3,2–3,4.
- Con `r₀ = 0,16 m` y pasos de 8, 16 y 32 cm (ilustrativos) el error de ajuste es `0,0747`, `0,2525` y `0,8356 rad²` (256, 64 y 16 actuadores); el cociente entre pasos consecutivos es `3,38` y `3,31` frente a `2^{5/3} = 3,17`.
- 🎯 **Por qué importa:** El número de actuadores fija el error de ajuste que ninguna medición mejora. La decisión central: ¿cuántos actuadores se necesitan para un `r₀` dado?

📘 **Dónde se aprende** (1 clase): [B42-C15 · Espejos deformables](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md).

### Error de altura

- El error de acimut y el error de altura del eje.

💡 **Cómo se explica en la clase [B43-C17](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md):**
- A seis horas del meridiano depende del error de altura y cambia de signo entre este y oeste (filas 3 y 4).
- El caso de error de altura en el meridiano es nulo en primer orden; la simulación muestra un residuo de segundo orden de `0,0003"/s`.
- ⚠️ **Error frecuente:** Confundir los errores de acimut y altura. Se corrige con 8.1.
- 🎯 **Por qué importa:** La alineación polar se corrige midiendo la deriva de una estrella. La decisión central: ¿qué deriva produce un error de acimut o de altura y cómo se invierte para corregirlo?

📘 **Dónde se aprende** (1 clase): [B43-C17 · Alineación polar](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md).

### Error de apuntamiento

- El error de apuntamiento es verdadero frente al objetivo; el error de estimación, estimado frente al verdadero.
- El error de apuntamiento `δ` es el ángulo entre el eje del haz y la dirección del receptor.

💡 **Cómo se explica en la clase [B87-C20](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md):**
- El apuntamiento real (`296″`) está dominado por el error de estimación (`240″`), que viene de los sensores de vector (`0,5°`–`1°`): sin rastreador estelar no se baja de ahí.
- Con error inicial de `20°`, el lazo entra a `2°` a los `24 s` y mantiene un apuntamiento rms de `0″` los últimos 200 s (error de estimación rms `0″`).
- 🎯 **Por qué importa:** Cada pieza funciona sola; juntas pueden interactuar (el ruido del estimador entra al control, el control mueve la actitud que mide el sensor). La decisión central: ¿qué apuntamiento real se logra con el lazo completo y cómo se sabe que la simulación es coherente?

📘 **Dónde se aprende** (2 clases): [B87-C20 · Simulación ADCS integral](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md); [B92-C02 · Divergencia del haz y pérdidas por apuntamiento óptico](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md).

### Error de apuntamiento absoluto

- El error de apuntamiento absoluto (APE) es la diferencia entre la actitud real y la deseada.

💡 **Cómo se explica en la clase [B87-C15](../programa/clases/B87/B87-C15-apuntamiento-de-alta-precision/CLASE.md):**
- «El error de apuntamiento absoluto del eje x de la antena será `< 60″` (99,7 %, valor medio más 3σ), medido sobre ventanas de 600 s en modo nominal»; incluye valor, eje, índice, estadística, confianza y periodo (S3).
- 🎯 **Por qué importa:** Un requisito de apuntamiento incompleto es ambiguo. La decisión central: ¿cómo se define y se mide el error de apuntamiento, y cómo cambia con el ancho de banda del lazo?

📘 **Dónde se aprende** (1 clase): [B87-C15 · Apuntamiento de alta precisión](../programa/clases/B87/B87-C15-apuntamiento-de-alta-precision/CLASE.md).

### Error de arista e_ij

- Información `Ω_ij`: inversa de la covarianza de la medida. Error de arista `e_ij`: diferencia entre la medida y la predicción `x_i⁻¹ ⊕ x_j`.

💡 **Cómo se explica en la clase [B99-C03](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md):**
- (F4) formulan el SLAM como un grafo: los nodos son las poses `x_i`, una arista `(i, j)` lleva una medida virtual `z_ij` (la transformación que hace coincidir las observaciones de `i` y de `j`) con su matriz de información `Ω_ij`, y el error `e_ij(x_i, x_j)` es la diferencia entre la medida y la predicha.
- Escribir el error de arista `e_ij` y su Jacobiano analítico, y comprobarlo con diferencias finitas.
- 🎯 **Por qué importa:** Sumar movimientos da una trayectoria que no cierra el lazo; una medida de cierre de bucle dice que la pose final es la inicial. La decisión central: ¿cómo repartir el desacuerdo entre cientos de poses de modo coherente con la incertidumbre de cada medida?

📘 **Dónde se aprende** (1 clase): [B99-C03 · SLAM basado en grafos de poses](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md).

### Error de Bayes

- El error de Bayes es el mínimo error posible dadas las distribuciones.
- El error de Bayes es el error mínimo posible con la información disponible.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- Comparar el error observado con el error de Bayes en un caso analítico.
- Matriz 3 × 3 con errores concentrados en las clases cercanas; exactitud ≈ 0,9 y κ ≈ 0,85; ejemplo de fuga con el 1-NN; error de Bayes 1D comparado con el observado.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.

📘 **Dónde se aprende** (2 clases): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md); [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md).

### Error de cierre

- El error de cierre es la distancia entre la posición tras un período y la inicial, relativa a `a`.
- El error de cierre es la distancia entre el estado final y el inicial tras un período exacto.

💡 **Cómo se explica en la clase [B07-C20](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md):**
- (3) Orden de convergencia: al reducir `dt` a la mitad, el error de cierre de leapfrog debe dividirse por 4 y el de Euler por 2.
- El error de cierre de leapfrog, `1,383 × 10⁻⁴`, es casi toda diferencia de fase: `2π · 689/31 558 289 = 1,37 × 10⁻⁴` rad.
- ⚠️ **Error frecuente:** Atribuir el error de cierre al método cuando es de fase. Se corrige con la sección 8.7 y el ejercicio 5.
- 🎯 **Por qué importa:** Un simulador es la forma de explorar un fenómeno cuya solución no tienes a mano, y de comprobar que entiendes uno cuya solución sí conoces. Aquí conoces la respuesta (una órbita circular se repite con un período dado por una fórmula), así que puedes verificar el simulador antes de confiar en él para casos que no conoces.

📘 **Dónde se aprende** (2 clases): [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B71-C03 · Ecuación de movimiento de dos cuerpos](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md).

### Error de cuantización

- El error de cuantización máximo es `±LSB/2`.
- El error de cuantización `q/√12`.

💡 **Cómo se explica en la clase [B43-C16](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md):**
- *Descripción textual:* la cuadratura fija el paso; la cuantización fija el error mínimo; el Gray protege las transiciones; la interpolación añade un error según las señales.
- En palabras: cuantiza el paso y añade errores de señal.
- 🎯 **Por qué importa:** El codificador es el ojo de la montura: lo que no mide, no lo corrige. La decisión central: ¿qué resolución, qué código y qué calidad de señal dan un error angular menor que el presupuesto?

📘 **Dónde se aprende** (2 clases): [B43-C16 · Encoders y medición angular](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md); [B88-C02 · Microcontroladores embarcados](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md).

### Error de cuaternión

- El error de cuaternión es `q_e = q ⊗ q_c⁻¹`.

💡 **Cómo se explica en la clase [B87-C17](../programa/clases/B87/B87-C17-control-de-tres-ejes/CLASE.md):**
- *Descripción textual:* el error de cuaternión actúa como un resorte hacia la actitud objetivo y la velocidad como amortiguador; el par se limita y alimenta la dinámica.
- Calcular el error de cuaternión `q_e = q ⊗ q_c⁻¹` y elegir el signo de `q_{e,w}`.
- 🎯 **Por qué importa:** Es el lazo central del subsistema de actitud. La decisión central: ¿cómo se eligen las ganancias para un tiempo de asentamiento dado, cómo se evita el camino largo (el cuaternión doble) y qué pasa cuando el par se satura?

📘 **Dónde se aprende** (1 clase): [B87-C17 · Control de tres ejes](../programa/clases/B87/B87-C17-control-de-tres-ejes/CLASE.md).

### Error de datos

- El error de datos viene de la incertidumbre de los parámetros.

💡 **Cómo se explica en la clase [B11-C19](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md):**
- Armar un presupuesto de error con truncamiento, redondeo e incertidumbre de datos.
- Ejercicio 12 · integrador. Elabora tu *estudio de convergencia con presupuesto de error*: la curva en V de una derivada (dos fórmulas), Richardson y autoconvergencia de un integrador en tu órbita, y un presupuesto con truncamiento, redondeo y una incertidumbre de datos rotulada, con la decisión de cuántos pasos usar.
- 🎯 **Por qué importa:** Un resultado numérico sin cota de error es una cifra sin sentido. Y gastar horas de cálculo para reducir un error de método que ya es menor que la incertidumbre de los datos es un desperdicio.

📘 **Dónde se aprende** (1 clase): [B11-C19 · Estimación de error y convergencia](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md).

### Error de dirección

- El error de dirección es el ángulo entre `B̂` medido y verdadero.

💡 **Cómo se explica en la clase [B87-C05](../programa/clases/B87/B87-C05-magnetometros/CLASE.md):**
- *Descripción textual:* la posición en la órbita da el campo del modelo; el sensor añade sesgo y ruido; la dirección medida se compara con la del modelo y su diferencia es el error.
- Un ruido de `100 nT` por eje da `0,249°` de error de dirección; un sesgo de `1000 nT` da `1,32°` en media y `2,30°` como máximo.
- 🎯 **Por qué importa:** Un cubesat sin sensores estelares usa el campo magnético para saber hacia dónde apunta y para detumbling (C16). La decisión central: ¿cuánto varía el campo a lo largo de la órbita, cuánto ruido y sesgo tolera la dirección medida y qué parte de la actitud no ve el magnetómetro?

📘 **Dónde se aprende** (1 clase): [B87-C05 · Magnetómetros](../programa/clases/B87/B87-C05-magnetometros/CLASE.md).

### Error de ejecución

- El error de ejecución es el error del impulso aplicado.

💡 **Cómo se explica en la clase [B76-C19](../programa/clases/B76/B76-C19-orbitas-de-mantenimiento/CLASE.md):**
- Se añade un error de ejecución del `2 %`.
- *Descripción textual:* el error de inserción se propaga una revolución; su crecimiento se compara con el autovalor; la jacobiana de la posición permite calcular el impulso que lo corrige, con un error de ejecución, y se repite cada revolución.
- 🎯 **Por qué importa:** Una órbita periódica inestable no se mantiene sola. La decisión central: ¿con qué frecuencia y qué impulso hay que corregir para que el error no crezca?

📘 **Dónde se aprende** (1 clase): [B76-C19 · Órbitas de mantenimiento](../programa/clases/B76/B76-C19-orbitas-de-mantenimiento/CLASE.md).

### Error de energía

- Es reversible y conserva el volumen, pero no exactamente la energía: su error de energía `ΔH` escala como `ε²`.

💡 **Cómo se explica en la clase [B19-C03](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md):**
- Ejecutar a mano un paso del integrador de salto de rana y calcular el error de energía.
- `ε = 0,25` está por debajo: el error de energía es pequeño y se acepta el 93 %.
- 🎯 **Por qué importa:** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.

📘 **Dónde se aprende** (1 clase): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md).

### Error de escala

- Un error de escala es un error que crece con el valor medido (por ejemplo, un `n` equivocado).

💡 **Cómo se explica en la clase [B13-C20](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md):**
- En el caso defectuoso, el aire real tiene `n = 1,000 310` pero el modelo sigue usando `1,000 300`: un error de escala de `10⁻⁵`.
- Una rechazada exige investigar: error de escala, `u` subestimada o referencia dudosa (C18).
- 🎯 **Por qué importa:** Un telémetro calibrado, con presupuesto y registro, puede seguir fallando: un error de escala oculto que la calibración en una sola distancia no ve.

📘 **Dónde se aprende** (1 clase): [B13-C20 · Validación de una cadena de medida](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md).

### Error de estimación

- El error de apuntamiento es verdadero frente al objetivo; el error de estimación, estimado frente al verdadero.
- El error de estimación `e = x − x̂` cumple `ė = (A − L C) e`.

💡 **Cómo se explica en la clase [B16-C14](../programa/clases/B16/B16-C14-observadores-de-estados/CLASE.md):**
- Sin esa estimación, el giróscopo solo acumularía `b·t = 0,2 rad` en 100 s: más de 11° de error.
- Ejercicio 11 · transferencia. Si el modelo tiene una inercia equivocada en 20 %, ¿qué efecto tiene sobre el error de estimación y cómo se reduce?
- 🎯 **Por qué importa:** Los sensores miden poco y mal: un rastreador de estrellas da la orientación, pero a baja frecuencia y con ruido; un giróscopo da la velocidad con un sesgo que deriva. El controlador necesita el estado completo (C15) y limpio.

📘 **Dónde se aprende** (2 clases): [B16-C14 · Observadores de estados](../programa/clases/B16/B16-C14-observadores-de-estados/CLASE.md); [B87-C20 · Simulación ADCS integral](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md).

### Error de fase

- El error de fase es el adelanto o retraso a lo largo de la órbita.
- El error de fase es la diferencia entre la fase calculada y la exacta.

💡 **Cómo se explica en la clase [B11-C11](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md):**
- B --> E["Error de fase<br/>crece con las vueltas"]
- *Descripción textual:* un método simpléctico aplicado a un sistema hamiltoniano conserva muy bien una energía modificada, por lo que el error de la energía real queda acotado y oscilante, pero acumula un error de fase; un método no simpléctico como RK4 deriva en energía de forma secular.
- 🎯 **Por qué importa:** Para el sistema solar, anillos planetarios o constelaciones se necesitan integraciones de millones de vueltas. Un método que añade o quita un poco de energía en cada vuelta termina destruyendo la órbita.

📘 **Dónde se aprende** (2 clases): [B11-C11 · Métodos simplécticos](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md); [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md).

### Error de fase en el borde

- El error de fase en el borde es `π D²/(4λR)`.

💡 **Cómo se explica en la clase [B91-C05](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md):**
- Medirla a esa distancia produce un error de fase de `22,5°` en el borde, que rellena los nulos y apenas cambia el pico (`−0,060 dB`); a un cuarto de la distancia el error sube a `90°` y el pico cae `0,97 dB`.
- Calcular el error de fase en el borde de la apertura por medir a distancia finita.
- 🎯 **Por qué importa:** Una antena se acepta si su ganancia y su patrón medidos cumplen la especificación dentro de una incertidumbre conocida. La decisión central: ¿a qué distancia medir y con qué incertidumbre, para poder afirmar que la antena cumple?

📘 **Dónde se aprende** (1 clase): [B91-C05 · Medición y calibración de antenas](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md).

### Error de frente de onda

- El error de frente de onda `σ` (RMS) mide cuánto se aparta la onda de una esfera ideal.

💡 **Cómo se explica en la clase [B43-C01](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md):**
- Un espejo refleja: el error de frente de onda es el doble del error de superficie.
- Como un presupuesto familiar: se fija el gasto total que se tolera (el error de frente de onda) y se reparte entre rubros; los errores independientes no se suman en bloque sino en cuadratura, igual que la dispersión de varias fuentes de ruido.
- 🎯 **Por qué importa:** Sin requisitos escritos, cada pieza del telescopio se fabrica «lo mejor posible» y no se sabe cuándo basta. La decisión central: ¿qué error de frente de onda, qué escala de imagen y qué tolerancia mecánica hay que pedir, y cómo se reparte el error entre las piezas?

📘 **Dónde se aprende** (1 clase): [B43-C01 · Requisitos ópticos y mecánicos](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md).

### Error de HCW

- El error de HCW es la distancia entre la solución lineal y la no lineal.

💡 **Cómo se explica en la clase [B76-C09](../programa/clases/B76/B76-C09-dinamica-relativa-de-hill-clohessy-wiltshire/CLASE.md):**
- El error crece linealmente con el tiempo (×5 en 5 órbitas) y con el cuadrado de la separación (×100 entre `100` y `1000 m`).
- Para una elipse de `1000 m`, el error tras 5 órbitas es `0,7 %`.
- 🎯 **Por qué importa:** Un controlador de encuentro necesita predecir dónde estará la otra nave sin integrar dos cuerpos cada vez. La decisión central: ¿hasta qué distancia y durante cuánto tiempo es válida la solución lineal de HCW, y qué movimientos son acotados?

📘 **Dónde se aprende** (1 clase): [B76-C09 · Dinámica relativa de Hill-Clohessy-Wiltshire](../programa/clases/B76/B76-C09-dinamica-relativa-de-hill-clohessy-wiltshire/CLASE.md).

### Error de linealización

- El error de linealización es `‖f(p₀ + δ) − f(p₀) − J δ‖`, que crece como `‖δ‖²` si `f` es suave.

💡 **Cómo se explica en la clase [B10-C19](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md):**
- Para un paso `δ = s (577,35 km; 0,577 rad; 0,577 rad)`: `s = 0,1` da un desplazamiento real de `93,9 km` y un error de linealización de `4,957 km`;
- Con pasos de ~5 % de error relativo, la linealización es dudosa; con 0,05 %, excelente.
- 🎯 **Por qué importa:** Una estación mide la distancia, el azimut y la elevación de un objeto con incertidumbres. Para decir dónde está en coordenadas cartesianas y cuánta incertidumbre tiene esa posición, hay que transformar los números y sus errores.

📘 **Dónde se aprende** (1 clase): [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md).

### Error de medida

- El error de medida es el valor medido menos un valor de referencia (S1, 2.16).

💡 **Cómo se explica en la clase [B13-C04](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *diagnóstico de una serie de medidas*: con la tabla de la sección 12, el error total para cada `n`, el `n` a partir del cual domina el sesgo, el sesgo estimado con un patrón y la decisión (promediar, calibrar o rediseñar), con datos rotulados como sintéticos.
- 🎯 **Por qué importa:** Una estación mide el instante de llegada de un pulso de una baliza. Cada lectura fluctúa por ruido electrónico, y además hay un retardo constante del cable que nadie incluyó.

📘 **Dónde se aprende** (2 clases): [B13-C03 · Exactitud frente a precisión](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md); [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md).

### Error de modelo

- Un error de modelo es la discrepancia entre el modelo usado y la realidad física.
- El error de modelo es el que no desaparece al reducir el paso, porque proviene de lo que se planteó mal (constante, fuerza).
- El error de modelo aquí es el efecto de añadir `J₂`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C19](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md):**
- Las tres se complementan; la última no detecta un error que se repita en todas las resoluciones (un modelo equivocado converge, con precisión, a un valor equivocado).
- Autoconvergencia no es exactitud: si el modelo o el código tienen un error sistemático, ambas corridas coincidirán en un valor equivocado.
- 🎯 **Por qué importa:** Un resultado numérico sin cota de error es una cifra sin sentido. Y gastar horas de cálculo para reducir un error de método que ya es menor que la incertidumbre de los datos es un desperdicio.

📘 **Dónde se aprende** (4 clases): [B11-C19 · Estimación de error y convergencia](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md); [B22-C04 · Inversión espectral](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md); [B23-C03 · Casos analíticos de validación](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md); [B73-C20 · Proyecto de integración celeste de precisión](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md).

### Error de módulo

- El error de módulo `σ_μ` en magnitudes se convierte a fraccional con `(ln 10/5) σ_μ`.

🎯 **Por qué importa (clase B26-C12):** Una distancia con un error de `2,6 %` produce un `H₀` con un error similar, y la discusión actual sobre `H₀` gira alrededor de esas décimas de punto porcentual. Entender cómo se acumulan los errores en una cadena de pasos evita confiar en una cifra más de lo debido.

📘 **Dónde se aprende** (1 clase): [B26-C12 · Escalas de distancia cosmológicas](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md).

### Error de Monte Carlo

- El error de Monte Carlo es la variabilidad del resultado debida solo al número finito de muestras.

💡 **Cómo se explica en la clase [B12-C14](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md):**
- Monte Carlo es general y su error no depende de la dimensión, pero converge despacio.
- Monte Carlo: sortear tres cargas, sumar y contar la fracción por encima de 33; con `N = 10⁶` el error típico es `0,00025`.
- ⚠️ **Error frecuente:** Reportar una estimación sin su error de Monte Carlo. Se corrige con 8.2.
- 🎯 **Por qué importa:** Casi ningún modelo de misión admite una fórmula cerrada para la incertidumbre de su salida: hay no linealidades, restricciones y combinaciones de entradas. La simulación Monte Carlo reemplaza el álgebra por repetición: se sortean entradas, se evalúa el modelo y se resume la salida.

📘 **Dónde se aprende** (1 clase): [B12-C14 · Simulación Monte Carlo](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md).

### Error de pose

- Pseudoinversa amortiguada: `Jᵀ(JJᵀ + λ²I)⁻¹`. Error de pose: posición y vector de rotación entre pose deseada y actual.

💡 **Cómo se explica en la clase [B101-C02](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md):**
- Se repite `q ← q + Jᵀ(JJᵀ + λ²I)⁻¹ e`, con `e` el error de pose (posición y vector de rotación) y `λ = 0,05`.
- Verificando siempre el error de pose final con la cinemática directa: si no es menor que la tolerancia, no hay solución, aunque la iteración haya terminado.
- 🎯 **Por qué importa:** El operador pide «lleva la herramienta allí» y el brazo debe decidir cuántos grados gira cada articulación. Hay ninguna, una, varias o infinitas soluciones.

📘 **Dónde se aprende** (1 clase): [B101-C02 · Cinemática inversa y redundancia de manipuladores](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md).

### Error de posición

- El error de posición por eje es la combinación en cuadratura de sus componentes.
- El error de posición es aproximadamente `σ_UERE × DOP`.

💡 **Cómo se explica en la clase [B53-C19](../programa/clases/B53/B53-C19-incertidumbre-en-mapas-planetarios/CLASE.md):**
- El script [incertidumbre.py](incertidumbre.py) sortea 200 000 errores de posición y de diámetro y compara con la propagación (comprueba RMS 1 %, CE90 1 %, `σ_A` a 3000 m 2 %).
- 🎯 **Por qué importa:** Un contorno sin barras de error afirma más de lo que sabe. La decisión central: ¿con qué incertidumbre se conoce una posición y un área en un mapa, y cuándo falla la propagación lineal?

📘 **Dónde se aprende** (2 clases): [B53-C19 · Incertidumbre en mapas planetarios](../programa/clases/B53/B53-C19-incertidumbre-en-mapas-planetarios/CLASE.md); [B89-C16 · GNSS como navegación de satélites](../programa/clases/B89/B89-C16-gnss-como-navegacion-de-satelites/CLASE.md).

### Error de posición de estación

- El error de posición de estación desplaza la línea de base.

💡 **Cómo se explica en la clase [B74-C05](../programa/clases/B74/B74-C05-sesgos-de-estaciones-terrestres/CLASE.md):**
- Un error de posición de estación de 5 m por eje eleva el error a `20,940 m`; un sesgo de 3 m por estación, a `13,030 m`.
- P["error de posicion de estacion"] --> A
- 🎯 **Por qué importa:** Un error sistemático no se promedia: un sesgo de 3 m en cada estación no desaparece con más medidas. La decisión central: ¿qué sesgo conviene estimar, cuál conviene solo reconocer en la covarianza y cuándo el remedio empeora el problema?

📘 **Dónde se aprende** (1 clase): [B74-C05 · Sesgos de estaciones terrestres](../programa/clases/B74/B74-C05-sesgos-de-estaciones-terrestres/CLASE.md).

### Error de proveedor

- Un error de proveedor es un fallo de una fuente que no debe silenciarse.

💡 **Cómo se explica en la clase [B14-C22](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md):**
- S --> I["Inspeccionar<br/>contar, filtrar,<br/>ver errores de proveedor"]
- *Descripción textual:* se define la búsqueda, se ejecuta sin descargar, se inspecciona (conteo, filtros y errores de proveedor); si el número de registros no es razonable se vuelve a definir; si lo es, se descarga y se registran parámetros y resultados.
- 🎯 **Por qué importa:** Quieres estudiar una región activa del Sol durante un día usando imágenes ultravioleta. Hay cientos de miles de archivos repartidos en varios proveedores.

📘 **Dónde se aprende** (1 clase): [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md).

### Error de redondeo

- Un error de redondeo es la diferencia entre el número y su redondeo.
- Un error de redondeo es la diferencia entre el valor y su redondeo; su cota es el máximo posible: ±media unidad de la última cifra conservada (`365` → ±0,5).
- El error de redondeo viene de la aritmética finita; en doble precisión el épsilon de máquina es `ε = 2,22 × 10⁻¹⁶`.

💡 **Cómo se explica en la clase [B03-C11](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md):**
- Funciona porque los errores de redondeo en el numerador y denominador se compensan parcialmente; pero no siempre, así que se compara siempre con el cálculo.
- (Cerca de 0,2 %.) Resultados (2026-11-05, Python 3.12.9): estimado 500 s, exacto 499,005 s, error 0,20 %; diámetros terrestres entre Tierra y Luna 30,2; 1 au con 6, 4, 3 y 2 cifras: `1,495980e11`, `1,496000e11`, `1,500000e11`, `1,500000e11`; redondeo previo 3,8, al final 3,9, exacto 3,88.
- 🎯 **Por qué importa:** Si te piden el tiempo que tarda la luz del Sol en llegar a la Tierra y respondes «499,004783836 s», parece muy preciso, pero tus datos (1 au y `c`) son exactos; en cambio, si respondes lo mismo para la distancia a la Luna, que varía entre unos 357 000 y 407 000 km, esas cifras serían falsas.

📘 **Dónde se aprende** (3 clases): [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B11-C19 · Estimación de error y convergencia](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md).

### Error de reproyección

- El error de reproyección es la distancia entre el píxel observado y el que predice el modelo.

💡 **Cómo se explica en la clase [B103-C01](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md):**
- R --> E["error de reproyección<br/>y comparación con la verdad"]
- *Descripción textual:* de cada vista del patrón se obtiene una homografía; de varias homografías sale `K`; con `K` se estima la distorsión; un refinamiento conjunto ajusta todo y se mide el error de reproyección.
- 🎯 **Por qué importa:** Un rover que mide una distancia con un error de focal del 1 % comete un error del 1 % en la distancia. La decisión central: ¿cuántas vistas y qué modelo de distorsión hacen falta para que la focal y el punto principal sean fiables, y cómo se comprueba?

📘 **Dónde se aprende** (1 clase): [B103-C01 · Calibración intrínseca de cámaras](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md).

### Error de reunión

- Un error de reunión une extremos equivocados y puede originar aberraciones cromosómicas (dicéntricos, translocaciones, deleciones).

💡 **Cómo se explica en la clase [B112-C05](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md):**
- X --> M["errores de reunión<br/>y aberraciones"]
- *Descripción textual:* el LET fija la fracción de daño agrupado, que se repara despacio, mientras el daño simple se repara rápido; las roturas que quedan y los pares cercanos dan los errores de reunión.
- ⚠️ **Error frecuente:** Confundir error de reunión con mutación comprobada. Es un recuento del modelo (8.4).
- 🎯 **Por qué importa:** Falta la clase de mecanismos moleculares de daño y reparación. Sin ella, la diferencia de eficacia biológica entre fotones e iones pesados (B112-C01, C02) y la incertidumbre del riesgo (C04) parecen cifras arbitrarias.

📘 **Dónde se aprende** (1 clase): [B112-C05 · Daño y reparación del ADN por radiación espacial](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md).

### Error de seguimiento

- Ancho de haz: ángulo de media potencia. Error de seguimiento: `velocidad × latencia`.

💡 **Cómo se explica en la clase [B96-C28](../programa/clases/B96/B96-C28-control-y-seguimiento-de-la-antena-de-estacion/CLASE.md):**
- Calcular el error de seguimiento por latencia y la pérdida por apuntamiento.
- Ejercicio 12 · integrador. Integrador. Elabora tu *informe de seguimiento de antena*: pasadas, elevaciones, velocidades, error de seguimiento, pérdida, veredicto y lista de lo consultado, sintético y no consultado.
- 🎯 **Por qué importa:** Una antena que no alcanza la velocidad angular pierde el satélite justo en la mejor parte de la pasada. La decisión central: ¿qué pasadas puede seguir la antena y cuándo se necesita otra estrategia (predicción, giro previo o limitar la elevación)?

📘 **Dónde se aprende** (1 clase): [B96-C28 · Control y seguimiento de la antena de estación](../programa/clases/B96/B96-C28-control-y-seguimiento-de-la-antena-de-estacion/CLASE.md).

### Error de semieje

- Un error de semieje `δa` equivale a un error de velocidad a lo largo de la trayectoria `Δv_y = −n δa/2`.

💡 **Cómo se explica en la clase [B76-C15](../programa/clases/B76/B76-C15-control-de-formacion-satelital/CLASE.md):**
- *Descripción textual:* una elipse de radio `ρ` se cierra sola; un error de semieje equivale a un error de velocidad que desplaza el centro radial y crea una deriva por órbita; un impulso opuesto la anula y su suma anual es el presupuesto.
- Con un error de semieje de `1 m` (`Δv_y = −0,5301 mm/s`), el centro radial queda en `x_c = −1,0 m` y la deriva es `9,4248 m` por órbita, `94,25 m` en 10 órbitas.
- 🎯 **Por qué importa:** Un error de un metro en el semieje parece nada y deriva nueve metros por órbita. La decisión central: ¿cuánto se desvía una formación por un error de inserción y cuánto `Δv` cuesta mantenerla?

📘 **Dónde se aprende** (1 clase): [B76-C15 · Control de formación satelital](../programa/clases/B76/B76-C15-control-de-formacion-satelital/CLASE.md).

### Error de símbolo sin fondo

- El error de símbolo sin fondo es `e^{−n_s}(M−1)/M`.

💡 **Cómo se explica en la clase [B89-C18](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md):**
- Verificar el error de símbolo de PPM sin fondo con una simulación de Poisson.
- Error de simbolo 16-PPM sin fondo (60000 simbolos): simulado frente a e^-ns (M-1)/M
- 🎯 **Por qué importa:** Las comunicaciones ópticas prometen más tasa por masa y potencia que la radio; entender el presupuesto de fotones y la modulación por posición de pulso explica por qué y a qué costo (apuntamiento, nubes). La decisión central: ¿cuántos fotones por bit llegan y qué error de símbolo implica la modulación PPM elegida?

📘 **Dónde se aprende** (1 clase): [B89-C18 · Comunicaciones ópticas espaciales](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md).

### Error de sintaxis

- Un error de sintaxis ocurre cuando el código no es Python válido, antes de ejecutarse; una excepción ocurre durante la ejecución y puede tratarse (S2, §8.1–8.2).

💡 **Cómo se explica en la clase [B07-C12](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md):**
- Un error de sintaxis, en cambio, impide ejecutar: Python señala la línea, aunque el origen puede estar un poco antes (S2, §8.1).
- Distinguir errores de sintaxis de excepciones en ejecución.
- 🎯 **Por qué importa:** Un programa científico recibe archivos con huecos, texto donde esperaba un número y valores imposibles (un período negativo). Hay dos malas respuestas: dejar que el programa se caiga sin explicar nada y, peor, seguir en silencio con un valor inválido (`nan`, `0`) que contamina el resultado final.

📘 **Dónde se aprende** (1 clase): [B07-C12 · Manejo de errores y excepciones](../programa/clases/B07/B07-C12-manejo-de-errores-y-excepciones/CLASE.md).

### Error de tiempo

- El error de tiempo (fase) `x`.

🎯 **Por qué importa (clase B46-C08):** El tiempo de coherencia de un instrumento depende de cómo se acumula el error de un oscilador. La decisión central: ¿a qué escala de tiempo domina cada tipo de ruido y cuánto se puede integrar?

📘 **Dónde se aprende** (1 clase): [B46-C08 · Osciladores y estabilidad](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md).

### Error de truncado

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B42-C13):** La óptica adaptativa solo corrige lo que mide. La decisión central: ¿qué se mide (pendientes o fase), cuántos modos se ajustan y cuánto ruido llega a los coeficientes?

📘 **Dónde se aprende** (1 clase): [B42-C13 · Medición de frente de onda](../programa/clases/B42/B42-C13-medicion-de-frente-de-onda/CLASE.md).

### Error de truncamiento

- El error de truncamiento es lo que sobra al sustituir la solución exacta en el esquema; para la derivada segunda central vale `(Δx²/12) u⁗` (S1, §3.4(iii)).
- El error de truncamiento es del orden de la primera potencia omitida.
- El error de truncamiento viene de aproximar (cortar una serie, discretizar).

💡 **Cómo se explica en la clase [B11-C14](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md):**
- Obtener una aproximación de `u_xx` por diferencias centrales y su error de truncamiento.
- 🎯 **Por qué importa:** Casi todo código de simulación de calor, fluidos o plasma en una malla regular usa diferencias finitas. Elegir el paso de tiempo equivocado no da un resultado ligeramente malo: da un resultado que explota.

📘 **Dónde se aprende** (3 clases): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md); [B11-C19 · Estimación de error y convergencia](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md); [B72-C15 · Aproximaciones perturbativas](../programa/clases/B72/B72-C15-aproximaciones-perturbativas/CLASE.md).

### Error en magnitud

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B29-C02](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md):**
- *Descripción textual:* la PSF da la fracción de estrella dentro de la apertura; el número de pixeles da el ruido del fondo; ambos fijan la SNR, cuyo máximo da la apertura óptima y el error en magnitud.
- Convertir SNR en error en magnitud `1,0857/SNR`.
- 🎯 **Por qué importa:** Una apertura pequeña pierde estrella; una grande suma cielo y ruido de lectura. La decisión central: ¿qué apertura maximiza la relación señal-ruido y qué error en magnitud implica?

📘 **Dónde se aprende** (1 clase): [B29-C02 · Curvas de luz fotométricas](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md).

### Error estacionario

- El error estacionario `e_ss` es `lim (r − y)` cuando `t → ∞`.

💡 **Cómo se explica en la clase [B16-C04](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md):**
- *Descripción textual:* un escalón de referencia produce primero un tramo transitorio, que se describe con cuatro tiempos y sobreimpulso, y luego un régimen estacionario, que se describe con el error final.
- Calcular el error estacionario ante un escalón y una perturbación constante.
- 🎯 **Por qué importa:** Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación.

📘 **Dónde se aprende** (1 clase): [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md).

### Error estadístico

- Un error sistemático afecta a todos los datos de un método en el mismo sentido; un error estadístico varía al azar.

🎯 **Por qué importa (clase B01-C16):** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).

📘 **Dónde se aprende** (1 clase): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md).

### Error estándar

- El error estándar es `σ/√n`.

💡 **Cómo se explica en la clase [B131-C01](../programa/clases/B131/B131-C01-actividades-de-medicion-astronomica-para-el-aula/CLASE.md):**
- Con 20 grupos simulados que leen una vez cada sombra con ruido de `1 cm`: media `6672 km`, desviación `1521 km`, error estándar `340 km`; mediana `6266 km`, mínimo `5059`, máximo `11057`.
- Por aula: media, mediana y error estándar.
- 🎯 **Por qué importa:** El catálogo no tenía clases de didáctica. La decisión central de esta: ¿qué debe llevar una actividad de medición para que enseñe a medir y no solo a calcular un número?

📘 **Dónde se aprende** (1 clase): [B131-C01 · Actividades de medición astronómica para el aula](../programa/clases/B131/B131-C01-actividades-de-medicion-astronomica-para-el-aula/CLASE.md).

### Error estándar de medida

- El error estándar de medida `SEM = s √(1 − KR20)` cuantifica la incertidumbre de una puntuación.

💡 **Cómo se explica en la clase [B131-C08](../programa/clases/B131/B131-C08-evaluacion-formativa-en-el-aula-de-astronomia/CLASE.md):**
- Calcular KR-20, comprobarlo contra el alfa de Cronbach y el error estándar de medida.
- 🎯 **Por qué importa:** Una prueba formativa solo sirve si se usa para decidir. La decisión central: ¿qué ítems, qué ideas y qué estudiantes necesitan algo distinto mañana, y cuánto puedes fiarte de lo que mide la prueba?

📘 **Dónde se aprende** (1 clase): [B131-C08 · Evaluación formativa en el aula de astronomía](../programa/clases/B131/B131-C08-evaluacion-formativa-en-el-aula-de-astronomia/CLASE.md).

### Error final

- Deriva: error acumulado. Error final: distancia entre la pose final estimada y la verdadera.

💡 **Cómo se explica en la clase [B99-C06](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md):**
- El cierre de bucle baja el ATE (0,199 → 0,102 m) y el error final (0,597 → 0,014 m), pero no cambia el RPE de 1 ni de 40 pasos (0,0287 y 0,267 m): corrige el error global, no el local.
- Límite: el ATE penaliza por igual un error al inicio y al final, aunque su efecto en la navegación no lo sea.
- 🎯 **Por qué importa:** «Mi robot deriva poco» no es una afirmación comprobable. La decisión central: ¿qué métrica, con qué alineación y con qué ventana, describe el error que importa para la tarea?

📘 **Dónde se aprende** (1 clase): [B99-C06 · Evaluación de deriva y error de trayectoria](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md).

### Error formal

- El error formal es `σ/√S_XX`.

💡 **Cómo se explica en la clase [B45-C22](../programa/clases/B45/B45-C22-extincion-atmosferica-masa-de-aire-y-coeficientes-de-color/CLASE.md):**
- con un rango estrecho de masa de aire (1,0 a 1,5) el error formal sube a 0.0184 (3.09 veces)
- 🎯 **Por qué importa:** Sin corregir la extinción, la fotometría terrestre depende de la hora. La decisión central: ¿qué `k` y qué fórmula de masa de aire dan la corrección y con qué error?

📘 **Dónde se aprende** (1 clase): [B45-C22 · Extinción atmosférica, masa de aire y coeficientes de color](../programa/clases/B45/B45-C22-extincion-atmosferica-masa-de-aire-y-coeficientes-de-color/CLASE.md).

### Error fotónico

- El error fotónico viene del ruido de Poisson de los fotones.

💡 **Cómo se explica en la clase [B129-C02](../programa/clases/B129/B129-C02-fotometria-participativa/CLASE.md):**
- *Descripción textual:* los flujos dan la magnitud diferencial y su error fotónico; con ellos se combinan los voluntarios con pesos y se obtiene la curva de luz y el periodo, afectados por el sesgo de cada observador.
- Por simulación: el Monte Carlo del error fotónico y de la varianza de la media.
- 🎯 **Por qué importa:** Una curva de luz de una estrella variable se construye con medidas de muchas personas con instrumentos distintos. La decisión central: ¿cómo se combinan sus medidas para que la curva sea más precisa que cada una, y qué error no se puede promediar?

📘 **Dónde se aprende** (1 clase): [B129-C02 · Fotometría participativa](../programa/clases/B129/B129-C02-fotometria-participativa/CLASE.md).

### Error fraccional

- El error fraccional es `σ_d/d`.

💡 **Cómo se explica en la clase [B26-C12](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md):**
- Convertir un error en magnitudes en uno fraccional.
- Ejercicio 1 · con los pasos indicados. Convierte `0,03 mag` en error fraccional.
- 🎯 **Por qué importa:** Una distancia con un error de `2,6 %` produce un `H₀` con un error similar, y la discusión actual sobre `H₀` gira alrededor de esas décimas de punto porcentual. Entender cómo se acumulan los errores en una cadena de pasos evita confiar en una cifra más de lo debido.

📘 **Dónde se aprende** (1 clase): [B26-C12 · Escalas de distancia cosmológicas](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md).

### Error global

- El error global es la diferencia acumulada entre la solución numérica y la exacta en un tiempo fijo.
- El error local es el error de un solo paso; el error global es el acumulado.
- El error global de un integrador en el tiempo `t` es la distancia entre su resultado y la solución exacta.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C05](../programa/clases/B11/B11-C05-metodo-de-euler/CLASE.md):**
- Si el error global es `E ≈ C h` con `C` estimado de la tabla (`C ≈ 0,1356` para `t = 2`), para `E = 10⁻³` se necesita `h ≈ 7,4 × 10⁻³`, es decir, unos 270 pasos.
- D --> E["Error local ∝ h²<br/>Error global ∝ h"]
- ⚠️ **Error frecuente:** Confundir error local con global. Se corrige con el ejercicio 4 y la sección 8.3.
- 🎯 **Por qué importa:** La mayoría de las ecuaciones del movimiento no tiene solución en forma cerrada. Un computador no resuelve la ecuación: da pasos pequeños, y cada paso usa la pendiente conocida para estimar el estado siguiente.

📘 **Dónde se aprende** (4 clases): [B11-C05 · Método de Euler](../programa/clases/B11/B11-C05-metodo-de-euler/CLASE.md); [B14-C03 · Análisis numérico con SciPy](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md); [B23-C03 · Casos analíticos de validación](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md); [B37-C05 · Códigos de evolución estelar: configuración, verificación y límites](../programa/clases/B37/B37-C05-codigos-de-evolucion-estelar-configuracion-verificacion-y-limites/CLASE.md).

### Error L1

- El error L1 es la media del valor absoluto del error.

💡 **Cómo se explica en la clase [B38-C06](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md):**
- El error baja a razón de 1,57–1,58 al duplicar las celdas (orden ≈ 0,65, típico en discontinuidades).
- El error L1 del SPH se pondera por el volumen de cada partícula y se mide en `|x| < 0,45`.
- ⚠️ **Error frecuente:** Medir el error en los bordes no perturbados. Se corrige con 8.3.
- 🎯 **Por qué importa:** Cada método tiene errores distintos en choques y discontinuidades de contacto. La decisión central: ¿qué error comete cada método frente a una solución exacta y cómo cambia con la resolución?

📘 **Dónde se aprende** (1 clase): [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md).

### Error local

- El error local es el error de un solo paso; el error global es el acumulado.

💡 **Cómo se explica en la clase [B14-C03](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md):**
- Pero el error global se acumula sobre muchos pasos, y no hay garantía de que sea tan pequeño como el local.
- Indica que el solver mantiene las estimaciones de error locales por debajo de `atol + rtol·|y|`, con valores por defecto `rtol = 10⁻³` y `atol = 10⁻⁶`; que `rtol` es aproximadamente el número de cifras correctas y `atol` el de decimales correctos; y que `dense_output=True` permite evaluar la solución en cualquier instante.
- 🎯 **Por qué importa:** Un integrador devuelve un número aunque sea malo. Con las tolerancias por defecto, una órbita circular puede no cerrarse después de una vuelta y el programa no se queja.

📘 **Dónde se aprende** (1 clase): [B14-C03 · Análisis numérico con SciPy](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md).

### Error local de truncamiento

- El error local de truncamiento es lo que el método se equivoca en un solo paso partiendo del valor exacto.

🎯 **Por qué importa (clase B11-C05):** La mayoría de las ecuaciones del movimiento no tiene solución en forma cerrada. Un computador no resuelve la ecuación: da pasos pequeños, y cada paso usa la pendiente conocida para estimar el estado siguiente.

📘 **Dónde se aprende** (1 clase): [B11-C05 · Método de Euler](../programa/clases/B11/B11-C05-metodo-de-euler/CLASE.md).

### Error local estimado

- El error local estimado es la diferencia entre dos soluciones del mismo paso con distinta precisión.

🎯 **Por qué importa (clase B11-C08):** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.

📘 **Dónde se aprende** (1 clase): [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md).

### Error Monte Carlo estándar

- El error Monte Carlo estándar de la media es `s/√ESS`.

🎯 **Por qué importa (clase B19-C04):** Una cadena que parece haberse estabilizado puede estar atrapada en una región de la posterior, o llevar meses de iteraciones en una sola zona y no haber visto la otra. Con una sola cadena y una mirada al gráfico, la tentación de decir «ya convergió» es fuerte.

📘 **Dónde se aprende** (1 clase): [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md).

### Error no detectado

- El error no detectado por paso es `u = p (1 − s)(1 − d(1 − ρ))`.

💡 **Cómo se explica en la clase [B110-C05](../programa/clases/B110/B110-C05-checklists-de-emergencia-ejecucion-y-verificacion-cruzada/CLASE.md):**
- Calcular la probabilidad de un error no detectado por paso y en todo el checklist.
- 🎯 **Por qué importa:** Los checklists de emergencia se leen y verifican bajo estrés y no tenían clase propia. La decisión central: ¿cuánta verificación cruzada vale su costo en tiempo, y qué la hace menos eficaz de lo que parece?

📘 **Dónde se aprende** (1 clase): [B110-C05 · Checklists de emergencia: ejecución y verificación cruzada](../programa/clases/B110/B110-C05-checklists-de-emergencia-ejecucion-y-verificacion-cruzada/CLASE.md).

### Error normalizado

- El error normalizado `err = máx_i |Δ_i| / sc_i`; el paso se acepta si `err ≤ 1` y se rechaza si no.

💡 **Cómo se explica en la clase [B11-C08](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md):**
- El error normalizado es `1,52 × 10⁻⁵/6,07 × 10⁻⁶ = 2,5 > 1`: se rechaza el paso.
- Un error normalizado de `0,4` se acepta y sugiere ampliar: `0,9 · 0,4^{−0,2} = 1,08`.
- 🎯 **Por qué importa:** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.

📘 **Dónde se aprende** (1 clase): [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md).

### Error objetivo

- El error objetivo es el nivel de precisión que se quiere.

💡 **Cómo se explica en la clase [B11-C26](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md):**
- Errores objetivo: `10⁵`, `10³`, `10` y `1` m.
- Evaluaciones mínimas del barrido para alcanzar cada error objetivo:
- 🎯 **Por qué importa:** «El método A es mejor que el B» es una afirmación vacía sin el problema, la métrica, la tolerancia y el costo. Una comparación mal diseñada lleva a elegir el algoritmo equivocado para una misión.

📘 **Dónde se aprende** (1 clase): [B11-C26 · Benchmark de algoritmos numéricos](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md).

### Error periódico

- El error periódico `e(t) = A sen(2πt/T_w + φ)`.

💡 **Cómo se explica en la clase [B41-C18](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md):**
- P["error periodico"] --> D["2 A sen(pi T/P)"]
- Con error periódico de `15 "` y periodo `479 s`, la exposición sin guiado para derivar menos de `1 "` es `5,08 s`.
- ⚠️ **Error frecuente:** Creer que el sinfin no tiene error. Tiene un error periódico.
- 🎯 **Por qué importa:** La montura decide cuánto tiempo se puede exponer. La decisión central: ¿altazimutal o ecuatorial y qué exposición máxima sin guiado?

📘 **Dónde se aprende** (2 clases): [B41-C18 · Monturas y mecanismos de seguimiento](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md); [B43-C12 · Montura ecuatorial](../programa/clases/B43/B43-C12-montura-ecuatorial/CLASE.md).

### Error permanente

- El error permanente es `τ/K_p`.

💡 **Cómo se explica en la clase [B87-C18](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md):**
- *Descripción textual:* las cuatro perturbaciones se suman (o se combinan en RSS) para dar un par; el lazo PD lo convierte en un error permanente y la función de Lyapunov desplazada confirma la estabilidad.
- Suma `705 nN·m`; con `ω_n = 0,2 rad/s`, el error permanente es `12,11″`.
- 🎯 **Por qué importa:** El presupuesto de par decide el tamaño de las ruedas y de los magnetopares. La decisión central: ¿qué perturbación domina, qué error permanente deja en el lazo y se mantiene la estabilidad?

📘 **Dónde se aprende** (1 clase): [B87-C18 · Estabilidad ante perturbaciones](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md).

### Error radial

- El error radial es la componente del error en la dirección radial.
- El error radial de dos ejes sigue una Rayleigh.

💡 **Cómo se explica en la clase [B72-C19](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md):**
- Se propaga el estado nominal y el perturbado y se resta; el error se proyecta sobre la velocidad nominal (*along-track*) y sobre la dirección radial.
- El error radial se mantiene en metros (oscila); el de la trayectoria crece linealmente: `δn = −3/2 n δa/a` acumula `δn · a · t`.
- 🎯 **Por qué importa:** Las incertidumbres de la órbita inicial y de los parámetros determinan cuánto tiempo vale una predicción. La decisión central: ¿cómo crece con el tiempo el error de posición por cada fuente de incertidumbre y cuál de ellas manda?

📘 **Dónde se aprende** (2 clases): [B72-C19 · Análisis de sensibilidad orbital](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md); [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md).

### Error relativo

- El error relativo es `(aproximado − exacto)/exacto`.
- El error relativo es `σ_h/h`.
- El error relativo es `|aprox − exacto|/|exacto|`.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C03](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md):**
- Para evaluar un cálculo frente a una referencia: `error relativo = |calculado − referencia| / referencia`.
- Calcular un error relativo porcentual frente a un valor de referencia.
- 🎯 **Por qué importa:** La Tierra no gira en un círculo: su distancia al Sol varía a lo largo del año. ¿Mucho o poco?

📘 **Dónde se aprende** (7 clases): [B03-C03 · Porcentajes y escalas comparativas](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B04-C06 · Identidades trigonométricas](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md); [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md); [B09-C14 · Series y aproximaciones](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md); [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md) y 1 más.

### Error relativo de energía

- El error relativo de energía es `(ε − ε₀)/|ε₀|`.
- El error relativo de energía es `|E(t)/E₀ − 1|`.

💡 **Cómo se explica en la clase [B11-C10](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md):**
- Calcular el error relativo de energía y de momento angular a lo largo de una integración.
- Ejercicio 3 · casi autónomo. Traduce un error relativo de energía de `+9,37 × 10⁻³` a un cambio de semieje mayor en una órbita con `a = 6 778,1 km`.
- 🎯 **Por qué importa:** Un análisis de misión puede necesitar propagar un satélite durante años, es decir, decenas de miles de vueltas. Si cada vuelta añade o quita un poco de energía, la altura de la órbita cambia solo por culpa del programa.

📘 **Dónde se aprende** (2 clases): [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md); [B73-C08 · Sistemas de N cuerpos](../programa/clases/B73/B73-C08-sistemas-de-n-cuerpos/CLASE.md).

### Error residual

- El error residual es lo que queda tras quitar `1` y `ρ²`.
- El error residual es el que sobrevive al protocolo.

💡 **Cómo se explica en la clase [B104-C08](../programa/clases/B104/B104-C08-comunicacion-de-tripulacion/CLASE.md):**
- El error residual baja de 0,1843 a 0,0091 (unas 20 veces), y el 31,5 % de los mensajes se repite (por errores de subida o de bajada).
- *Descripción textual:* la distancia fija el retardo y el tiempo de cada intercambio; el mensaje tiene un error por palabra; la repetición de lectura reduce el error residual al costo de dos retardos adicionales.
- 🎯 **Por qué importa:** A 1,28 s de la Luna aún se conversa; a más de 3 minutos de Marte ya no. La decisión central: ¿qué protocolo de mensajes usar cuando cada ida y vuelta cuesta minutos y un error cuesta caro?

📘 **Dónde se aprende** (2 clases): [B43-C08 · Montaje de espejo primario](../programa/clases/B43/B43-C08-montaje-de-espejo-primario/CLASE.md); [B104-C08 · Comunicación de tripulación](../programa/clases/B104/B104-C08-comunicacion-de-tripulacion/CLASE.md).

### Error rms de superficie

- El error rms de superficie `ε` es la desviación típica de la superficie real respecto de la parabólica ideal.

💡 **Cómo se explica en la clase [B91-C04](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md):**
- Un reflector sintético de `D = 3,0 m` con `η₀ = 0,65` y error rms de superficie `ε = 0,5 mm` tiene su ganancia máxima a `47,71 GHz`, con una eficiencia de superficie de `e⁻¹ = 0,368` (`4,34 dB` perdidos).
- Calcular la ganancia de un reflector con error de superficie con la fórmula de Ruze.
- 🎯 **Por qué importa:** Una malla desplegable pesa poco y cabe plegada, pero su precisión de forma limita la frecuencia útil. La decisión central: ¿hasta qué frecuencia vale la pena usar un reflector con un error de superficie dado, y qué término del presupuesto de error conviene reducir?

📘 **Dónde se aprende** (1 clase): [B91-C04 · Antenas desplegables y estructuras de gran apertura](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md).

### Error sistemático

- El error sistemático es el componente que en réplicas permanece constante o varía de forma predecible (S1, 2.17).
- Un error sistemático afecta a todos los datos de un método en el mismo sentido; un error estadístico varía al azar.
- El error sistemático se repite igual en cada lectura (por ejemplo, un cero mal calibrado).

💡 **Cómo se explica en la clase [B01-C16](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md):**
- Ejercicio 11 · transferencia. La discrepancia entre 67,4 y 73,04 se debe a un error sistemático oculto.
- 🎯 **Por qué importa:** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).

📘 **Dónde se aprende** (3 clases): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md); [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md).

### Error típico

- El error típico (*standard error*) es la desviación típica del estimador.

💡 **Cómo se explica en la clase [B12-C07](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md):**
- C --> E["Curvatura → error típico<br/>√(λ̂/n)"]
- *Descripción textual:* de los datos y del modelo se construye la log-verosimilitud; su máximo es el estimador y su curvatura da el error típico; la calidad del estimador se valida repitiendo el experimento muchas veces.
- ⚠️ **Error frecuente:** Reportar la estimación sin su error típico. Se corrige con el ejercicio 1.
- 🎯 **Por qué importa:** Una misión no «conoce» la tasa de impactos ni el ruido de su sensor: los estima a partir de unas decenas de datos. Un estimador mal elegido, o mal interpretado, da parámetros sesgados o con una confianza injustificada.

📘 **Dónde se aprende** (1 clase): [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md).

### Error típico de medida

- El error típico de medida `SEM` es la dispersión del error.

🎯 **Por qué importa (clase B107-C04):** Los fragmentos consultados describen una batería computarizada de pruebas breves de varios dominios cognitivos diseñada para astronautas de alto rendimiento (Basner et al., 2015; Casario et al., 2022) y preguntan cómo se relacionan sus descensos con el desempeño operativo (Basner et al., 2020).

📘 **Dónde se aprende** (1 clase): [B107-C04 · Evaluación del rendimiento físico y cognitivo de tripulantes](../programa/clases/B107/B107-C04-evaluacion-del-rendimiento-fisico-y-cognitivo-de-tripulantes/CLASE.md).

### Error tipo I

- El error tipo I `α = 0,05`.

💡 **Cómo se explica en la clase [B105-C20](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md):**
- Bajo el nulo (`d = 0`), con valores críticos t de 3, 5, 7, 11, 19 y 29 grados de libertad (recordados por el autor, no consultados): el error tipo I es 0,049; 0,050; 0,050; 0,048; 0,049 y 0,052 para `n = 4, 6, 8, 12, 20, 30`: la simulación reproduce el 0,05 nominal.
- El error tipo I bajo el nulo es 0,050 para todo `n`.
- 🎯 **Por qué importa:** Un estudio con 6 personas solo detecta efectos grandes; sin saberlo, se concluye «no hay efecto» cuando solo no había potencia. La decisión central: ¿qué efecto mínimo puede detectar el protocolo con su `n`, y cuántas comparaciones puede permitirse?

📘 **Dónde se aprende** (1 clase): [B105-C20 · Diseño de protocolo médico simulado](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md).

### Error tipo II

- El nivel de significación `α` es la tasa de falsos rechazos que se acepta (error tipo I); el error tipo II (probabilidad `β`) es no rechazar una `H₀` falsa; la potencia `1 − β` es la probabilidad de detectar un efecto real de un tamaño dado.

💡 **Cómo se explica en la clase [B12-C09](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md):**
- Distinguir error tipo I, error tipo II y potencia, y calcular la potencia en un caso.
- Debe incluir: hipótesis y supuestos; estadístico y `p` comprobado por dos caminos; simulación del error tipo I; potencia y `n` necesario; sensibilidad (correlación, colas); conclusión acotada; datos rotulados como observados/estimados/sintéticos y fuentes con fecha.
- 🎯 **Por qué importa:** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.

📘 **Dónde se aprende** (1 clase): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md).

### Error tipo M

- El error tipo M (magnitud) es la razón entre el efecto estimado medio entre los significativos y el verdadero (exageración); el error tipo S (signo) es la probabilidad de que un resultado significativo tenga signo contrario al efecto verdadero.

💡 **Cómo se explica en la clase [B12-C26](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md):**
- Con `d = 0,2` y `n = 10`, ocurre casi al nivel del error tipo I (7 % frente a 5 %).
- Entre los resultados significativos, el efecto estimado medio es `|d̂| = 1,194`, es decir 3,98 veces el verdadero (error tipo M).
- 🎯 **Por qué importa:** En medicina espacial, en estudios con tripulaciones o en misiones con pocas unidades, los tamaños de muestra son pequeños por necesidad. Con ellos, la mayoría de los efectos reales no se detectan, y los que se detectan suelen estar inflados.

📘 **Dónde se aprende** (1 clase): [B12-C26 · Sesgos y potencia estadística en poblaciones pequeñas](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md).

### Error tipo S

- El error tipo M (magnitud) es la razón entre el efecto estimado medio entre los significativos y el verdadero (exageración); el error tipo S (signo) es la probabilidad de que un resultado significativo tenga signo contrario al efecto verdadero.

💡 **Cómo se explica en la clase [B12-C26](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md):**
- Con `d = 0,2` y `n = 10`, ocurre casi al nivel del error tipo I (7 % frente a 5 %).
- Entre los resultados significativos, el efecto estimado medio es `|d̂| = 1,194`, es decir 3,98 veces el verdadero (error tipo M).
- 🎯 **Por qué importa:** En medicina espacial, en estudios con tripulaciones o en misiones con pocas unidades, los tamaños de muestra son pequeños por necesidad. Con ellos, la mayoría de los efectos reales no se detectan, y los que se detectan suelen estar inflados.

📘 **Dónde se aprende** (1 clase): [B12-C26 · Sesgos y potencia estadística en poblaciones pequeñas](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md).

### Error transversal

- El error transversal (*cross-boresight*) es el giro alrededor de los ejes `x, y` del sensor.

💡 **Cómo se explica en la clase [B87-C07](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md):**
- El error `ΔA = Â Aᵀ` es una rotación pequeña `φ` cuyos dos primeros componentes son el error transversal y el tercero es el balanceo.
- El balanceo se mide con el brazo de palanca `ρ_rms` (el radio medio de las estrellas, unos `4,3°`), mucho menor que 1 rad: `σ_roll ≈ σ_a/(√N ρ_rms)`, del orden de `14` veces el error transversal con 20 estrellas.
- 🎯 **Por qué importa:** Para apuntar un telescopio o una antena con precisión de segundos de arco, un sensor solar o un magnetómetro no bastan. La decisión central: ¿cuántas estrellas hacen falta y por qué el giro alrededor del eje óptico (balanceo) es mucho peor que el apuntamiento?

📘 **Dónde se aprende** (1 clase): [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md).

### Errores formales

- Los errores formales `σ √diag((AᵀA)⁻¹)`.

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Los errores formales más grandes son los de `CA` y `NPAE`, que están más correlacionados con otros términos.
- Calcular los errores formales de los parámetros.
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?

📘 **Dónde se aprende** (1 clase): [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### Erupciones

- Las erupciones son expulsiones violentas y esporádicas de masa.

💡 **Cómo se explica en la clase [B24-C17](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md):**
- Las tasas de pérdida de masa por vientos de estrellas calientes parecen más bajas de lo que suponían los modelos antiguos, y se dan más peso a las pulsaciones, erupciones y la transferencia en binarias, que dependen menos de la metalicidad (S3, resumen).
- Los vientos radiativos escalan con la metalicidad, mientras que las erupciones y la transferencia en binarias son menos sensibles; por eso su importancia crece a baja metalicidad.
- 🎯 **Por qué importa:** La masa que una estrella conserva hasta su final decide el destino: remanente, tipo de supernova, enriquecimiento del medio. Y las estrellas masivas no la conservan: pierden masa por vientos, erupciones y transferencia a una compañera.

📘 **Dónde se aprende** (1 clase): [B24-C17 · Estrellas masivas y pérdida de masa](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md).

### Es el cociente por encima del cual

- `R` es el cociente por encima del cual cualquier `rb` finita mayor que `R` la supera.

🎯 **Por qué importa (clase B75-C05):** El delta-v es lo caro. A veces conviene gastar tiempo para ahorrarlo.

📘 **Dónde se aprende** (1 clase): [B75-C05 · Transferencias bi-elípticas](../programa/clases/B75/B75-C05-transferencias-bi-elipticas/CLASE.md).

### Es el líquido que se vaporiza por el calor que entra. El

- La evaporación (*boil-off*) es el líquido que se vaporiza por el calor que entra. El aislamiento multicapa son láminas reflectantes que reducen la radiación.

🎯 **Por qué importa (clase B59-C21):** Lo extraído sirve si se conserva. La decisión central: ¿se acepta la evaporación o se paga la potencia de un refrigerador de cero evaporación?

📘 **Dónde se aprende** (1 clase): [B59-C21 · Almacenamiento criogénico y aislado de volátiles extraídos](../programa/clases/B59/B59-C21-almacenamiento-criogenico-y-aislado-de-volatiles-extraidos/CLASE.md).

### Es otro nombre para el mismo objeto; una

- Un alias es otro nombre para el mismo objeto; una copia es un objeto nuevo.

🎯 **Por qué importa (clase B07-C07):** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.

📘 **Dónde se aprende** (1 clase): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md).

### Es T_c/(T_h − T_c). La

- El COP de Carnot es `T_c/(T_h − T_c)`. La fracción de Carnot es el cociente entre el COP real y el ideal.

🎯 **Por qué importa (clase B59-C21):** Lo extraído sirve si se conserva. La decisión central: ¿se acepta la evaporación o se paga la potencia de un refrigerador de cero evaporación?

📘 **Dónde se aprende** (1 clase): [B59-C21 · Almacenamiento criogénico y aislado de volátiles extraídos](../programa/clases/B59/B59-C21-almacenamiento-criogenico-y-aislado-de-volatiles-extraidos/CLASE.md).

### Es un objeto nuevo

- Un alias es otro nombre para el mismo objeto; una copia es un objeto nuevo. Mutable significa que se puede modificar en el lugar.

🎯 **Por qué importa (clase B07-C07):** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.

📘 **Dónde se aprende** (1 clase): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md).

### Esbozo preliminar

- El esbozo preliminar es un diseño de cónicas empalmadas sin efemérides.

🎯 **Por qué importa (clase B75-C20):** Antes de diseñar una misión hay que saber si es viable y qué la hace cara. La decisión central: ¿cuánto delta-v y cuánta masa cuesta ir de la Tierra a una luna de Júpiter, y cuánto se ahorra con una misión de sobrevuelos en lugar de un orbitador?

📘 **Dónde se aprende** (1 clase): [B75-C20 · Diseño de una misión a luna helada](../programa/clases/B75/B75-C20-diseno-de-una-mision-a-luna-helada/CLASE.md).

### Escala

- Una escala de un eje indica cuánto vale cada marca; en una escala logarítmica cada marca multiplica por un factor fijo (B01-C02).
- Una escala es una clasificación por umbrales.
- El sesgo `o` es un desplazamiento y la escala `s` un factor por eje.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Antes de interpretar, lee: ¿qué magnitud hay en cada eje, con qué unidad, con qué escala (lineal o logarítmica), y desde dónde empieza el eje?
- En escala log-log, una función de potencia aparece como una recta cuya pendiente es el exponente; entre Venus y Júpiter esa pendiente da 1,499, muy cerca de 1,5 (sección 17).
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.

📘 **Dónde se aprende** (7 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B24-C20 · Modelo simplificado de estructura estelar](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md); [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B33-C04 · Escalas de severidad de clima espacial](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md); [B53-C26 · Publicación de mapas geológicos planetarios: estándares y leyendas](../programa/clases/B53/B53-C26-publicacion-de-mapas-geologicos-planetarios-estandares-y-leyendas/CLASE.md); [B80-C06 · Fusión IMU-cámara](../programa/clases/B80/B80-C06-fusion-imu-camara/CLASE.md) y 1 más.

### Escala acústica

- La escala acústica `θ* = r_s/D_M`.

💡 **Cómo se explica en la clase [B40-C07](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md):**
- *Descripción textual:* los parámetros dan la escala acústica y, por separado, un espectro de juguete se transforma a correlación y vuelve.
- 🎯 **Por qué importa:** Los picos acústicos fijan la geometría y el contenido del universo. La decisión central: ¿dónde caen los picos (`ℓ_A = π/θ*`) y cómo se pasa del espectro a la correlación y de vuelta?

📘 **Dónde se aprende** (1 clase): [B40-C07 · Espectro angular de potencias del CMB](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md).

### Escala de 28 valores

- La escala de 28 valores `0o, 0+, 1−, 1o, …, 9−, 9o`.

💡 **Cómo se explica en la clase [B30-C23](../programa/clases/B30/B30-C23-indices-geomagneticos-kp-y-dst/CLASE.md):**
- Escribir la escala de 28 valores de Kp en tercios.
- escala de Kp: 28 valores: 0o 0+ 1- 1o 1+ 2- 2o 2+ 3- 3o 3+ 4- 4o 4+ 5- 5o 5+ 6- 6o 6+ 7- 7o 7+ 8- 8o 8+ 9- 9o
- 🎯 **Por qué importa:** Kp y Dst son los índices con que se habla de tormentas. Saber cómo se construyen y con qué incertidumbre ayuda a leer un registro.

📘 **Dónde se aprende** (1 clase): [B30-C23 · Índices geomagnéticos Kp y Dst](../programa/clases/B30/B30-C23-indices-geomagneticos-kp-y-dst/CLASE.md).

### Escala de altura

- La escala de altura `H` es la altura en que la presión cae un factor `e`.
- La escala de altura `H = c_s/Ω` mide su espesor vertical y `h/r` es su cociente con el radio.

💡 **Cómo se explica en la clase [B24-C09](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md):**
- Estimar la escala de altura de una atmósfera.
- Ejercicio 5. Calcula la escala de altura para `T = 5772 K`, `μ = 1,3`, `g = 274 m/s²`.
- 🎯 **Por qué importa:** Toda temperatura o composición que atribuimos a una estrella se infiere de una capa delgada. Saber de qué profundidad viene la luz, cuánto vale la opacidad y cuánto puede brillar una estrella sin expulsar su atmósfera es lo que permite interpretar espectros (C10) y entender los vientos (C17).

📘 **Dónde se aprende** (2 clases): [B24-C09 · Atmósferas y opacidades](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md); [B52-C02 · Discos protoplanetarios](../programa/clases/B52/B52-C02-discos-protoplanetarios/CLASE.md).

### Escala de distancias

- La escala de distancias y la de tamaños pueden ser distintas en un modelo, pero entonces hay que declararlo.

💡 **Cómo se explica en la clase [B01-C13](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md):**
- Por eso los dibujos escolares cambian la escala de tamaños y la de distancias, y deben decirlo.
- Un modelo de distancias a escala con planetas «agrandados» es honesto si lo declara; uno que no lo declara engaña.
- ⚠️ **Error frecuente:** Mezclar la escala de tamaños con la de distancias. Ejercicio 9.
- 🎯 **Por qué importa:** Se dice que el sistema solar «está vacío», y es verdad en un sentido preciso: si el Sol midiera 9 mm, la Tierra sería un grano de 0,085 mm a un metro de distancia, y la estrella más cercana quedaría a más de 260 km. Pero esa imagen solo se entiende si la construyes tú con números.

📘 **Dónde se aprende** (1 clase): [B01-C13 · Sistema solar como sistema físico](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md).

### Escala de enfriamiento

- La escala de enfriamiento es `τ = R²/(π²κ)`.

💡 **Cómo se explica en la clase [B52-C17](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md):**
- `κ` y `R` dan la escala de enfriamiento, que se evalúa con una serie y con diferencias finitas y se comparan.
- Definir la escala de enfriamiento `τ = R²/(π²κ)`.
- 🎯 **Por qué importa:** El calor determina si un cuerpo funde, se diferencia o se enfría rápido. La decisión central: ¿cuánto tarda un cuerpo en perder su calor y cuánto lo calienta un impacto?

📘 **Dónde se aprende** (1 clase): [B52-C17 · Colisiones y evolución térmica](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md).

### Escala de imagen

- La escala de imagen de un telescopio.

🎯 **Por qué importa (clase B41-C06):** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Escala de longitud

- La escala de longitud `R_d` fija cómo cae la densidad superficial del disco: `Σ(R) = Σ₀ e^{−R/R_d}`.

💡 **Cómo se explica en la clase [B25-C01](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md):**
- El disco delgado contiene las estrellas jóvenes y el gas; el grueso, estrellas más viejas y a mayor altura (escala de longitud `2,0 ± 0,2 kpc` y masa `6 ± 3 × 10⁹ M☉`, S3); el halo estelar, las más viejas y pobres en metales (C17).
- Definir `R₀`, `Θ₀`, `Ω₀`, escala de longitud del disco y masa estelar, con sus unidades.
- 🎯 **Por qué importa:** Estamos dentro de la galaxia y no podemos fotografiarla desde fuera: su forma se reconstruye midiendo distancias y velocidades desde un punto que no es el centro. Sin un esquema claro de componentes (bulbo, barra, disco, halo) y de cifras de referencia, el resto del bloque carece de escala.

📘 **Dónde se aprende** (1 clase): [B25-C01 · Estructura de la Vía Láctea](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md).

### Escala de migración

- La escala de migración es `τ = a/|ȧ|`.

💡 **Cómo se explica en la clase [B52-C06](../programa/clases/B52/B52-C06-migracion-de-planetas/CLASE.md):**
- En el disco sintético, con `C = −2`, un planeta de `1 M⊕` a 5 ua migra con escala `a/|ȧ| = 1.49e+06` años y cae de 5 a 0,1 ua en `9.91e+05` años; para `10 M⊕`, `9.91e+04`.
- Calcular escalas de tiempo de migración para tres masas.
- 🎯 **Por qué importa:** La migración explica por qué las órbitas finales no coinciden con los lugares de formación. La decisión central: ¿en cuánto tiempo cae un planeta al interior y cómo depende de su masa?

📘 **Dónde se aprende** (1 clase): [B52-C06 · Migración de planetas](../programa/clases/B52/B52-C06-migracion-de-planetas/CLASE.md).

### Escala de Palermo

- La escala de Palermo es logarítmica y continua: compara la probabilidad del evento con la del fondo hasta esa fecha [S2].

💡 **Cómo se explica en la clase [B58-C10](../programa/clases/B58/B58-C10-escalas-de-peligrosidad/CLASE.md):**
- Que un caso de 1 km con `PI = 10⁻⁶` dé un Palermo bajo no significa que sus consecuencias sean pequeñas: la escala compara probabilidades con el fondo.
- Interpretar los tramos de la escala de Palermo.
- 🎯 **Por qué importa:** Dos objetos con la misma probabilidad pueden merecer atención muy distinta si uno es de 20 m y otro de 1 km. Las escalas ordenan casos y sirven para decidir qué vigilar.

📘 **Dónde se aprende** (1 clase): [B58-C10 · Escalas de peligrosidad](../programa/clases/B58/B58-C10-escalas-de-peligrosidad/CLASE.md).

### Escala de placa

- La escala de placa es `206 264,806 p/f` en segundos de arco por píxel.
- La escala de placa es `p/f` en radianes por píxel (`p`: tamaño de píxel, `f`: focal).
- La distancia focal `f` del objetivo (mm) y el tamaño del píxel `p` (µm) fijan la escala de placa: `escala = 206 265 · p / f` en segundos de arco por píxel (con `p` en mm).
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C19](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md):**
- *Descripción textual:* la focal y el píxel dan la escala de placa; combinada con el ritmo del cielo y el tiempo de exposición da la estela en píxeles; si es mayor que el límite aceptado se acorta la exposición o se usa seguimiento.
- Calcular la escala de placa y el campo de una cámara con un objetivo dado.
- 🎯 **Por qué importa:** Un teléfono o una cámara réflex puede captar la Vía Láctea o la Luna con detalle, pero una exposición demasiado larga convierte las estrellas en rayas. La pregunta motivadora: ¿cuánto puedo exponer y con qué focal para obtener estrellas puntuales, y qué debo anotar para que la foto sirva como dato?

📘 **Dónde se aprende** (5 clases): [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md); [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md); [B43-C01 · Requisitos ópticos y mecánicos](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md); [B44-C17 · Escala de imagen y muestreo](../programa/clases/B44/B44-C17-escala-de-imagen-y-muestreo/CLASE.md); [B74-C02 · Observación angular y astrometría](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md).

### Escala de seeing

- La escala de seeing es una convención propia (1 a 5) que debes definir.

💡 **Cómo se explica en la clase [B08-C17](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md):**
- Para una sesión general añade: fecha y hora UT (C05), lugar con latitud y longitud (C01), instrumento y aumento (C13, C14), condiciones (nubosidad en porcentaje, seeing en la escala que definas), fase y altura de la Luna (C08, C12), y el nombre del observador.
- Registrar condiciones (nubes, seeing, Luna) con una escala declarada.
- 🎯 **Por qué importa:** Un dato sin fecha, sin lugar o sin procedencia es una anécdota. La pregunta motivadora: ¿qué debo anotar para que mi observación se pueda repetir, revisar y comparar?

📘 **Dónde se aprende** (1 clase): [B08-C17 · Registro sistemático en bitácora](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md).

### Escala de tiempo

- Una escala de tiempo es una manera de numerar los instantes.
- La escala de tiempo de consumo es `τ = 1/(k n_B)`.
- Un marco de referencia y una escala de tiempo (B01-C04) se declaran en métodos cuando importan.

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- B --> C["Registro: marco, escala de tiempo, unidades"]
- Un evento ocurre en un lugar y un tiempo; la luz viaja y llega al observador; se hace un registro declarando marco, escala de tiempo y unidades; y se corrige restando el tiempo de luz para obtener el tiempo del evento.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).

📘 **Dónde se aprende** (3 clases): [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md); [B55-C03 · Reacciones en medio interestelar](../programa/clases/B55/B55-C03-reacciones-en-medio-interestelar/CLASE.md).

### Escala de tiempo radiativa

- La escala de tiempo radiativa es `c_p P/(g 4σT³)`: cuánto tarda la atmósfera en ajustarse radiativamente.

🎯 **Por qué importa (clase B54-C14):** La presión marciana varía unas decenas de por ciento durante el año porque parte del CO₂ se condensa en los casquetes polares. La pregunta motivadora: ¿cuánta masa de CO₂ participa en ese ciclo?

📘 **Dónde se aprende** (1 clase): [B54-C14 · Atmósfera de Marte](../programa/clases/B54/B54-C14-atmosfera-de-marte/CLASE.md).

### Escala de Torino

- La escala de Torino es entera, de 0 a 10, y comunica al público [S1].
- La escala de Torino comunica el riesgo con un entero [S1].

💡 **Cómo se explica en la clase [B58-C10](../programa/clases/B58/B58-C10-escalas-de-peligrosidad/CLASE.md):**
- Describir los niveles y colores de la escala de Torino.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de escalas de peligro*: energía, Palermo y banda de cinco casos, y la correspondencia de Torino.
- 🎯 **Por qué importa:** Dos objetos con la misma probabilidad pueden merecer atención muy distinta si uno es de 20 m y otro de 1 km. Las escalas ordenan casos y sirven para decidir qué vigilar.

📘 **Dónde se aprende** (2 clases): [B58-C10 · Escalas de peligrosidad](../programa/clases/B58/B58-C10-escalas-de-peligrosidad/CLASE.md); [B58-C19 · Comunicación pública del riesgo](../programa/clases/B58/B58-C19-comunicacion-publica-del-riesgo/CLASE.md).

### Escala dinámica

- La escala dinámica `2π√(R³/GM)` es el orden del periodo.

💡 **Cómo se explica en la clase [B24-C13](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md):**
- Con la escala dinámica `P ≈ 2π√(R³/GM)`: para el Sol `2,78 h`; para una supergigante de `5 M☉` y `50 R☉` (ilustrativa) `18,3 d`.
- Ejercicio 6. Calcula la escala dinámica del Sol en horas.
- 🎯 **Por qué importa:** Las cefeidas y otras estrellas pulsantes cumplen que cuanto más largo es el periodo, mayor es la luminosidad. Medir un periodo equivale entonces a conocer la luminosidad intrínseca y, por comparación con el brillo aparente, la distancia.

📘 **Dónde se aprende** (1 clase): [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md).

### Escala G

- La escala G de NOAA clasifica por Kp.

💡 **Cómo se explica en la clase [B30-C18](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md):**
- Ejercicio 7. Escala G de la etiqueta `7+`.
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué `Dst*` y la escala G no se comparan aquí?
- 🎯 **Por qué importa:** Prever la profundidad y la duración de una tormenta orienta la protección de redes y satélites. La decisión central: ¿qué mínimo alcanza `Dst*` y cuánto tarda en recuperarse?

📘 **Dónde se aprende** (1 clase): [B30-C18 · Tormentas geomagnéticas](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md).

### Escala INFLESZ

- La escala INFLESZ lo clasifica: menos de `40` muy difícil;

💡 **Cómo se explica en la clase [B130-C03](../programa/clases/B130/B130-C03-comunicacion-oral-de-la-ciencia/CLASE.md):**
- La escala INFLESZ fue propuesta por Barrio-Cantalejo et al.
- Interpretar el índice con los tramos de la escala INFLESZ.
- 🎯 **Por qué importa:** Presentar ante público requiere técnicas propias; la clase de comunicación escrita general no cubre el tiempo, el ritmo ni la jerga hablada. La decisión central: ¿qué cabe en el tiempo disponible y qué entenderá una persona que oye el guion una sola vez?

📘 **Dónde se aprende** (1 clase): [B130-C03 · Comunicación oral de la ciencia](../programa/clases/B130/B130-C03-comunicacion-oral-de-la-ciencia/CLASE.md).

### Escala lineal

- Una escala lineal da el mismo espacio a sumas iguales; una escala logarítmica da el mismo espacio a multiplicaciones iguales (cada paso es un factor 10).
- Una escala lineal multiplica todas las longitudes por el mismo factor.

💡 **Cómo se explica en la clase [B01-C13](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md):**
- Modelo a escala lineal: fiel, pero poco visible.
- Construir un modelo a escala lineal con una unidad de referencia declarada.
- 🎯 **Por qué importa:** Se dice que el sistema solar «está vacío», y es verdad en un sentido preciso: si el Sol midiera 9 mm, la Tierra sería un grano de 0,085 mm a un metro de distancia, y la estrella más cercana quedaría a más de 260 km. Pero esa imagen solo se entiende si la construyes tú con números.

📘 **Dónde se aprende** (2 clases): [B01-C13 · Sistema solar como sistema físico](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md); [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md).

### Escala logarítmica

- Una escala lineal da el mismo espacio a sumas iguales; una escala logarítmica da el mismo espacio a multiplicaciones iguales (cada paso es un factor 10).
- Una escala logarítmica muestra el logaritmo de la magnitud: cada marca principal es un factor 10.

💡 **Cómo se explica en la clase [B03-C15](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md):**
- En una escala logarítmica, la posición de un valor es `log₁₀ x`.
- Con una rejilla de `n` columnas y valores entre `x_min` y `x_max`, la columna es `round[(x − x_min)/(x_max − x_min) · (n − 1)]` en escala lineal; en logarítmica se usa `log₁₀` de cada valor.
- 🎯 **Por qué importa:** Las fichas de la NASA dan semiejes y períodos de los ocho planetas. En una tabla son 16 números.

📘 **Dónde se aprende** (2 clases): [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md); [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md).

### Escala logarítmica astronómica

- La abundancia es cuánto hay de un elemento; puede darse en número (átomos), en masa (kg) o con la escala logarítmica astronómica: ```text A(X) = log10(N_X / N_H) + 12 ``` donde `N_X` y `N_H` son números de átomos por unidad de volumen.

🎯 **Por qué importa (clase B06-C02):** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?

📘 **Dónde se aprende** (1 clase): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md).

### Escala log-log

- La escala log-log convierte `a m^b` en una recta.

💡 **Cómo se explica en la clase [B124-C05](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md):**
- En escala logarítmica `ln(costo) = ln a + b ln m`.
- D["datos de misiones análogas"] --> L["escala log-log"]
- 🎯 **Por qué importa:** Un costo sin banda de incertidumbre parece más preciso de lo que es. La decisión central: ¿cuánto cuesta esta misión, con qué banda y cuánto baja el costo unitario si se fabrican varias unidades?

📘 **Dónde se aprende** (1 clase): [B124-C05 · Estimación de costos de misión](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md).

### Escala robusta

- La escala robusta `1,4826·MAD` evita que un error infle la escala.

💡 **Cómo se explica en la clase [B129-C04](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md):**
- Ejercicio 3 · casi autónomo. Calcula la escala robusta con piso 0,10.
- 🎯 **Por qué importa:** Un lote de contribuciones trae errores de tecleo, duplicados, fechas imposibles y mediciones erróneas. La decisión central: ¿qué filtro aplicar para atrapar los errores sin tirar datos buenos, y cómo se sabe que funciona?

📘 **Dónde se aprende** (1 clase): [B129-C04 · Contribución de medidas voluntarias con control de calidad](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md).

### Escala TDB

- La escala TDB (tiempo dinámico baricéntrico) es la escala de la efeméride (B13-C08).

💡 **Cómo se explica en la clase [B23-C05](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md):**
- Declarar marco, centro, unidades, escala de tiempo y versión de un conjunto oficial.
- ⚠️ **Error frecuente:** Omitir centro, marco o escala de tiempo. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** Un modelo kepleriano de la Tierra pasó todas las pruebas de C01–C04, pero eso no dice nada sobre si la Tierra se mueve como una elipse perfecta. La pregunta motivadora es: ¿contra qué contrasto mi modelo, y qué diferencia estoy dispuesto a aceptar?

📘 **Dónde se aprende** (1 clase): [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md).

### Escala viscosa

- La escala viscosa es `t_ν = r²/ν`.

💡 **Cómo se explica en la clase [B52-C09](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md):**
- Calcular la escala viscosa `t_ν` y la tasa de acreción.
- Escala viscosa t_nu = r1^2/nu1 = 1.405e+06 anios ; t_s = t_nu/3 = 4.684e+05 anios ;
- 🎯 **Por qué importa:** La vida del gas fija cuánto tiempo hay para formar núcleos, gigantes y migración. La decisión central: ¿cuánto tarda un disco en perder su gas y cómo se comprueba un esquema numérico de difusión?

📘 **Dónde se aprende** (1 clase): [B52-C09 · Dispersión de discos de gas](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md).

### Escalabilidad

- La escalabilidad es cómo cambian `S` y `E` con `N`.
- La escalabilidad es la capacidad de crecer sin rediseño.

💡 **Cómo se explica en la clase [B18-C05](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md):**
- Ejercicio 11 · transferencia. Un colega informa «escalabilidad perfecta» con 4 procesos, una sola ejecución.
- El script [escalabilidad.py](escalabilidad.py) verifica las fórmulas contra valores exactos, comprueba que Karp–Flatt recupera `s = 0,08` de tiempos sintéticos y mide el escalado fuerte y débil del lote de órbitas.
- 🎯 **Por qué importa:** Un grupo pide tiempo en un clúster para propagar un catálogo grande de órbitas. Antes de pedir mil núcleos hay que saber si el programa los aprovechará.

📘 **Dónde se aprende** (2 clases): [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md); [B109-C05 · Crecimiento modular y escalabilidad de asentamientos](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md).

### Escalada

- La escalada es subir el nivel por una regla.

💡 **Cómo se explica en la clase [B122-C07](../programa/clases/B122/B122-C07-clasificacion-de-severidad-e-impacto-de-incidentes-espaciales/CLASE.md):**
- Aplicar la regla de escalada por personas.
- Por la regla de escalada: `personas = 4`.
- 🎯 **Por qué importa:** B58-C10 clasifica solo impactos de asteroides. La decisión central: ¿en qué orden se atienden los incidentes y qué regla fuerza la escalada?

📘 **Dónde se aprende** (1 clase): [B122-C07 · Clasificación de severidad e impacto de incidentes espaciales](../programa/clases/B122/B122-C07-clasificacion-de-severidad-e-impacto-de-incidentes-espaciales/CLASE.md).

### Escalado

- El escalado divide cada variable por un valor típico.

💡 **Cómo se explica en la clase [B81-C09](../programa/clases/B81/B81-C09-variables-de-diseno-orbital/CLASE.md):**
- El óptimo escalado supera a la rejilla (que es gruesa) y queda en la cota `r_b ≥ r₂`: la solución es una transferencia tipo Hohmann con casi todo el giro en el apoastro.
- Límite: otros optimizadores (con derivadas analíticas) son menos sensibles al escalado, aunque nunca indiferentes.
- 🎯 **Por qué importa:** Un optimizador que se detiene a la primera iteración no ha encontrado nada: puede ser un problema de escala y no de física. La decisión central: ¿qué variables elegir y cómo escalarlas para que el optimizador haga su trabajo?

📘 **Dónde se aprende** (1 clase): [B81-C09 · Variables de diseño orbital](../programa/clases/B81/B81-C09-variables-de-diseno-orbital/CLASE.md).

### Escalado de Kramers

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C03](../programa/clases/B32/B32-C03-opacidad-continua-ligado-libre-libre-libre-y-h/CLASE.md):**
- El escalado de Kramers da `κ(2ρ, T)/κ(ρ, T) = 2` y `κ(ρ, 2T)/κ(ρ, T) = 0,08839`.
- escalado de Kramers: kappa(2 rho, T)/kappa(rho, T) = 2 ; kappa(rho, 2T)/kappa(rho, T) = 0.08839
- 🎯 **Por qué importa:** La opacidad fija la profundidad desde la que escapa la luz. La decisión central: ¿cómo se promedia una opacidad que depende de la frecuencia?

📘 **Dónde se aprende** (1 clase): [B32-C03 · Opacidad continua: ligado-libre, libre-libre y H-](../programa/clases/B32/B32-C03-opacidad-continua-ligado-libre-libre-libre-y-h/CLASE.md).

### Escalado de tasa

- El escalado de tasa a igual margen sigue `R ∝ P D_t² D_r²/d²`.

💡 **Cómo se explica en la clase [B92-C07](../programa/clases/B92/B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md):**
- Las tasas publicadas en abril y junio de 2024 (`25` y `8,3 Mbps`) son `4,95` y `5,19` veces mayores (`6,94` y `7,16 dB`) que el escalado desde `267 Mbps`.
- Comparar el escalado con las tasas publicadas de DSOC y decir qué comparación no es una validación.
- 🎯 **Por qué importa:** El espacio profundo exige otra forma de pensar: pocos fotones, latencia de minutos y apuntamiento predictivo. La decisión central: ¿cómo cambia la tasa con la distancia y qué hay que prever para que el haz llegue al receptor?

📘 **Dónde se aprende** (1 clase): [B92-C07 · Enlaces ópticos de espacio profundo](../programa/clases/B92/B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md).

### Escalado débil

- El escalado débil mantiene fijo el trabajo *por proceso* (el problema crece con `p`); su meta es mantener el tiempo.
- El escalado débil aumenta el problema con `N` (trabajo por procesador constante).

💡 **Cómo se explica en la clase [B14-C16](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md):**
- El escalado débil resulta mucho más favorable porque la parte serie no crece con el problema en este modelo.
- Más trabajo (escalado débil) aprovecha el clúster si el problema puede crecer.
- ⚠️ **Error frecuente:** Confundir escalado fuerte y débil. Se corrige con la sección 8.4 y el ejercicio 6.
- 🎯 **Por qué importa:** Una simulación de la población de escombros orbitales requiere cien veces más cálculo del que tu equipo puede dar en una semana. Pides tiempo en un clúster y debes decidir: ¿cuántos procesos pido?

📘 **Dónde se aprende** (2 clases): [B14-C16 · Computación distribuida y HPC](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md); [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md).

### Escalado fuerte

- El escalado fuerte mantiene fijo el tamaño del problema y aumenta `p`; su meta es reducir el tiempo.
- El escalado fuerte mantiene fijo el tamaño del problema y aumenta los procesadores `N`.

💡 **Cómo se explica en la clase [B14-C16](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md):**
- Si tu problema tiene un tamaño fijo (por ejemplo, ajustar un modelo a un conjunto de datos), el escalado relevante es el fuerte y habrá un número de procesos óptimo.
- Tipo de problema: tamaño fijo → escalado fuerte.
- ⚠️ **Error frecuente:** Confundir escalado fuerte y débil. Se corrige con la sección 8.4 y el ejercicio 6.
- 🎯 **Por qué importa:** Una simulación de la población de escombros orbitales requiere cien veces más cálculo del que tu equipo puede dar en una semana. Pides tiempo en un clúster y debes decidir: ¿cuántos procesos pido?

📘 **Dónde se aprende** (2 clases): [B14-C16 · Computación distribuida y HPC](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md); [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md).

### Escalar

- Un escalar es una magnitud con solo tamaño (masa, tiempo).
- Un escalar es un número real.
- Un escalar es una cantidad independiente de las coordenadas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C12](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md):**
- Para un vector `w` y una dirección unitaria `ê`, su componente a lo largo de `ê` es `w · ê` (el producto escalar, que se verá en C13; aquí se calcula como `wₓêₓ + w_yê_y`).
- Sumar, restar y multiplicar por un escalar vectores, y verificar con un dibujo.
- 🎯 **Por qué importa:** Una sonda que sale de la Tierra tiene una velocidad respecto de la Tierra y la Tierra tiene una velocidad respecto del Sol. ¿Cuál es la velocidad de la sonda respecto del Sol?

📘 **Dónde se aprende** (4 clases): [B04-C12 · Vectores y componentes](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md); [B05-C02 · Posición, velocidad y aceleración](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md); [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md); [B39-C01 · Variedades, tensor métrico y geometría diferencial](../programa/clases/B39/B39-C01-variedades-tensor-metrico-y-geometria-diferencial/CLASE.md).

### Escalar de Kretschmann

- El escalar de Kretschmann `R_abcd R^abcd` es un invariante.

💡 **Cómo se explica en la clase [B39-C03](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md):**
- *Descripción textual:* los Christoffel y sus derivadas dan el Riemann, y sus contracciones dan Ricci, escalar y Kretschmann.
- Descripción larga: la esfera tiene la curvatura escalar esperada y Schwarzschild es vacío con Kretschmann no nulo.
- 🎯 **Por qué importa:** Un espacio-tiempo es curvo si el Riemann no se anula. La decisión central: ¿qué mide cada contracción del Riemann y cómo se comprueba un cálculo de curvatura?

📘 **Dónde se aprende** (1 clase): [B39-C03 · Tensor de Riemann, Ricci y curvatura escalar](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md).

### Escalar primero

- Aquí se escribe con el escalar primero, que es la disposición de SPICE (S1: `q₀ = cos(ángulo/2)` y la parte vectorial es `sin(ángulo/2)` por el eje unitario).

💡 **Cómo se explica en la clase [B10-C15](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md):**
- Límites: convención Hamilton, escalar primero, rotación activa; no se contrasta con el código de SPICE.
- ⚠️ **Error frecuente:** Mezclar escalar‑primero y escalar‑último. Se corrige en la sección 8.8.
- 🎯 **Por qué importa:** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.

📘 **Dónde se aprende** (1 clase): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md).

### Escalera

- Una escalera es el conjunto de líneas de una misma molécula (como las transiciones `J→J−1` del CO) que comparten una velocidad.

💡 **Cómo se explica en la clase [B62-C08](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md):**
- Distinguir la significancia de una coincidencia aislada de la de una escalera de líneas.
- 🎯 **Por qué importa:** Una línea que coincide con una frecuencia de catálogo no identifica una molécula: puede ser casualidad. La decisión central: ¿cuántas líneas hacen falta para afirmar una identificación con riesgo bajo de falsa alarma?

📘 **Dónde se aprende** (1 clase): [B62-C08 · Mezclas moleculares y confusión de líneas](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md).

### Escalera de distancias

- La escalera de distancias es el conjunto de métodos que se encadenan para medir distancias cada vez mayores, de modo que cada uno se calibra con el anterior.
- La escalera de distancias es la cadena de métodos: paralaje trigonométrico, binarias eclipsantes, cefeidas, supernovas Ia, ley de Hubble.

💡 **Cómo se explica en la clase [B01-C02](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *escalera de escalas personal* (sección 20): elige seis objetos de la tabla de la sección 12 (al menos uno de cada rango: planetario, estelar, galáctico y cosmológico) y para cada uno da: distancia con unidad e incertidumbre, `log₁₀`, el método con que se mide, su limitación y la fuente.
- 🎯 **Por qué importa:** Cuando alguien dice que Próxima Centauri está «a cuatro años luz» y que Andrómeda está «a dos millones y medio», es fácil oír solo «lejos» y «más lejos». Pero entre una y otra hay un factor de casi seis cien mil.

📘 **Dónde se aprende** (2 clases): [B01-C02 · Escalas desde la Tierra al cosmos observable](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md); [B26-C12 · Escalas de distancia cosmológicas](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md).

### Escalera de fidelidad

- La escalera de fidelidad ordena propagadores del más simple al más completo.

💡 **Cómo se explica en la clase [B72-C20](../programa/clases/B72/B72-C20-comparacion-de-propagadores-de-fidelidad-distinta/CLASE.md):**
- Describir la escalera de fidelidad de cuatro propagadores.
- 🎯 **Por qué importa:** La fidelidad cuesta cálculo y datos: un propagador analítico es instantáneo pero erra por miles de kilómetros en días; uno numérico con muchas fuerzas es lento. La decisión central: ¿qué propagador basta para una tarea, según el horizonte de predicción y el error aceptable?

📘 **Dónde se aprende** (1 clase): [B72-C20 · Comparación de propagadores de fidelidad distinta](../programa/clases/B72/B72-C20-comparacion-de-propagadores-de-fidelidad-distinta/CLASE.md).

### Escalera de recuperación

- La escalera de recuperación escala la respuesta con los reinicios repetidos: tarea, computador, modo seguro.

💡 **Cómo se explica en la clase [B88-C11](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md):**
- Diseñar una escalera de recuperación por reinicios repetidos.
- El script [watchdog.py](watchdog.py) simula 200 000 ciclos con cuatro niveles de jitter, los compara con `erfc` y aplica una escalera de recuperación, y comprueba 0 reinicios falsos con `σ = 5` y más de 1000 con `σ = 30`.
- 🎯 **Por qué importa:** Un watchdog mal ajustado reinicia sin necesidad o no reinicia cuando hace falta. La decisión central: ¿qué ventana y qué escalera de acciones recuperan un software colgado sin reinicios falsos?

📘 **Dónde se aprende** (1 clase): [B88-C11 · Watchdogs y recuperación](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md).

### Escalón

- Un escalón es la pérdida de masa entre dos mesetas.
- El escalón es la diferencia entre la altura máxima y la mínima en la huella.
- El escalón `u[n]` vale 1 desde `n = 0`.

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- Su respuesta al escalón unitario es `y[n] = 1 − (1 − a)^{n+1} = 1 − e^{−(n+1)Δt/τ}`, que coincide con la analítica del sistema continuo en los instantes de muestreo: el laboratorio da una diferencia de `3,3 × 10⁻¹⁶`.
- Paso 2 · Descomposición. `x = −50 u[n] + 50 u[n − 100]` (escalón hacia abajo y escalón de regreso 100 s después).
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.

📘 **Dónde se aprende** (3 clases): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B59-C03 · Agua en regolito y minerales](../programa/clases/B59/B59-C03-agua-en-regolito-y-minerales/CLASE.md); [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Escalón máximo

- El escalón máximo se obtiene de `F_h = N₁ tan α` con `cos α = (r − h)/r`.

💡 **Cómo se explica en la clase [B102-C04](../programa/clases/B102/B102-C04-suspension-rocker-bogie-y-mecanica-de-rovers/CLASE.md):**
- *Descripción textual:* la carga del cuerpo llega al balancín; este reparte entre la rueda delantera y el bogie, que reparte entre la media y la trasera; las tres cargas fijan el escalón máximo.
- Descripción larga: el reparto igual da a cada rueda un sexto del peso, las cargas escalan con `g` y el escalón máximo no depende de ella.
- 🎯 **Por qué importa:** Un rover cruza rocas sin muelles ni amortiguadores. La decisión central: ¿dónde colocar el pivote del cuerpo para repartir la carga, y qué escalón puede subir una rueda con la tracción disponible?

📘 **Dónde se aprende** (1 clase): [B102-C04 · Suspensión rocker-bogie y mecánica de rovers](../programa/clases/B102/B102-C04-suspension-rocker-bogie-y-mecanica-de-rovers/CLASE.md).

### Escalonado

- El costo fijo `F` se paga siempre; el variable `v`, por producto; el escalonado `S` se suma por cada tramo de capacidad `cap`.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- *Descripción textual:* los costos fijo, variable y escalonado forman el costo total, del que salen el costo medio, el precio con margen y el equilibrio; la incertidumbre de la demanda se evalúa con dos métodos.
- Separar costos fijos, variables y escalonados.
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Escalonamiento

- El escalonamiento es la división del `ΔV` entre etapas.

💡 **Cómo se explica en la clase [B77-C07](../programa/clases/B77/B77-C07-separacion-de-etapas-conceptual/CLASE.md):**
- La evidencia es la ficha de escalonamiento y separación del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de escalonamiento y separación*: tabla de `N`, ahorro por etapa, velocidades de separación y lista de qué es consultado e ilustrativo.
- 🎯 **Por qué importa:** Un `ΔV` alto es inalcanzable con una sola etapa de estructura moderada, pero cada etapa extra rinde menos. La decisión central: ¿cuántas etapas conviene y qué ocurre mecánicamente al separarlas?

📘 **Dónde se aprende** (1 clase): [B77-C07 · Separación de etapas conceptual](../programa/clases/B77/B77-C07-separacion-de-etapas-conceptual/CLASE.md).

### Escape

- Una captura es el paso de la circulación a la libración; un escape, el contrario.

💡 **Cómo se explica en la clase [B73-C12](../programa/clases/B73/B73-C12-captura-y-escape-resonante/CLASE.md):**
- El objetivo es la lógica de captura y escape; no se calculan probabilidades para un sistema real ni se compara con teoría analítica de la probabilidad de captura (no consultada).
- Descripción larga: el área de la separatriz coincide con la fórmula, `J` se conserva, el escape ocurre donde se predice y la captura baja al crecer la deriva.
- 🎯 **Por qué importa:** Muchas resonancias observadas (satélites, planetas migrantes, asteroides) no son primordiales: los cuerpos entraron en ellas. Saber cuándo una captura es segura y cuándo es improbable, y cuándo un cuerpo atrapado debe escapar, evita explicaciones erróneas.

📘 **Dónde se aprende** (1 clase): [B73-C12 · Captura y escape resonante](../programa/clases/B73/B73-C12-captura-y-escape-resonante/CLASE.md).

### Escape de Jeans

- El escape de Jeans es la pérdida de moléculas con velocidad mayor que `v_esc`.

💡 **Cómo se explica en la clase [B54-C11](../programa/clases/B54/B54-C11-escape-atmosferico/CLASE.md):**
- Que `T` es sintética y el escape de Jeans del CO₂ es despreciable (`λ ≫ 1`); la pérdida de Marte involucra otros procesos no tratados aquí.
- El escape sube respecto del cálculo de Jeans; el modelo es solo una referencia.
- 🎯 **Por qué importa:** Por qué la Tierra retiene el N₂ pero pierde el H depende de una razón entre energías. La pregunta motivadora: ¿qué especies puede retener un planeta a cierta temperatura?

📘 **Dónde se aprende** (1 clase): [B54-C11 · Escape atmosférico](../programa/clases/B54/B54-C11-escape-atmosferico/CLASE.md).

### Escenario

- El escenario es una hipótesis.
- Un escenario es una trayectoria condicionada a supuestos.
- Un escenario es un conjunto alternativo de supuestos.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B29-C07](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md):**
- *Descripción textual:* los priors y el observable dan la probabilidad posterior de cada escenario; una simulación con verdades extraídas de los priors comprueba que las probabilidades sean frecuencias reales.
- Esta clase no reproduce ese método: usa tres escenarios sintéticos (planeta `0,30`, binaria de fondo `0,40`, binaria jerárquica `0,30`) y un observable `x` normal en cada uno.
- ⚠️ **Error frecuente:** Tomar los escenarios por reales. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Hay muchos más candidatos que posibilidades de seguimiento. Validar bien exige probabilidades honestas: ni optimistas ni conservadoras en exceso.

📘 **Dónde se aprende** (4 clases): [B29-C07 · Métodos de validación planetaria](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md); [B106-C20 · Proyecto de balance ambiental de hábitat](../programa/clases/B106/B106-C20-proyecto-de-balance-ambiental-de-habitat/CLASE.md); [B118-C10 · Síndrome de Kessler como escenario](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md); [B126-C03 · Proyección de flujos de caja de un proyecto espacial](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md).

### Esclusa

- La esclusa es el recinto por el que se sale de la nave.
- Una esclusa es un volumen entre dos escotillas donde se cambia la presión.

💡 **Cómo se explica en la clase [B104-C10](../programa/clases/B104/B104-C10-actividades-extravehiculares-eva/CLASE.md):**
- La página de NASA sobre las caminatas espaciales de la ISS (consultada el 2026-11-10) registra más de 280 (286 en su gráfico) desde diciembre de 1998; la más larga duró 8 h 56 min, la más corta 19 min, y la mayoría entre 5 y 7 horas; los trajes EMU de NASA salen de la esclusa Quest y los Orlan de Roscosmos, de Poisk.
- 🎯 **Por qué importa:** El oxígeno de un traje es finito y el trabajo manual consume más que el reposo. La decisión central: ¿cuánto margen queda sobre el consumo esperado si la tasa metabólica de cada tarea varía?

📘 **Dónde se aprende** (2 clases): [B104-C10 · Actividades extravehiculares EVA](../programa/clases/B104/B104-C10-actividades-extravehiculares-eva/CLASE.md); [B109-C03 · Accesos, esclusas y transferencia entre ambientes presurizados](../programa/clases/B109/B109-C03-accesos-esclusas-y-transferencia-entre-ambientes-presurizados/CLASE.md).

### Escotilla

- Una escotilla es la puerta presurizada.

💡 **Cómo se explica en la clase [B109-C03](../programa/clases/B109/B109-C03-accesos-esclusas-y-transferencia-entre-ambientes-presurizados/CLASE.md):**
- Sobre una escotilla de `0,8 m` (ilustrativa) con la cabina a `8,2 psi` y vacío fuera actúan `28,4 kN`, unos `2,9` toneladas-fuerza.
- Calcular la fuerza de presión sobre una escotilla.
- 🎯 **Por qué importa:** Un asentamiento con salidas frecuentes pierde aire en cada ciclo. La decisión central: ¿cuánto gas hay que reponer al año y qué ganas recuperándolo?

📘 **Dónde se aprende** (1 clase): [B109-C03 · Accesos, esclusas y transferencia entre ambientes presurizados](../programa/clases/B109/B109-C03-accesos-esclusas-y-transferencia-entre-ambientes-presurizados/CLASE.md).

### Escrow

- El *escrow* es un fondo en garantía.

🎯 **Por qué importa (clase B127-C04):** Leer una póliza exige entender sus exclusiones, deducibles y límites; el catálogo no lo trataba. La decisión central: ¿qué parte de la pérdida retiene el asegurado y cómo cambia el precio al cambiar las condiciones?

📘 **Dónde se aprende** (1 clase): [B127-C04 · Exclusiones, deducibles y límites de pólizas](../programa/clases/B127/B127-C04-exclusiones-deducibles-y-limites-de-polizas/CLASE.md).

### Escudo

- Un escudo es un edificio volcánico ancho y de poca pendiente.

💡 **Cómo se explica en la clase [B70-C01](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md):**
- Imagina el escudo como un cuenco invertido cuyo perfil se ajusta con un exponente, y la fisura como una rendija por la que el fluido avanza más rápido en el centro que en las paredes.
- P["perfil h(r)"] --> V["volumen del escudo"]
- ⚠️ **Error frecuente:** Confundir volumen de cono con el del escudo. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una llanura de lava no dice por sí sola cuánto magma la formó ni cuánto tardó. La decisión central: ¿qué volumen y qué caudal corresponden a este edificio y a esta fisura, y qué cambiaría en otro planeta?

📘 **Dónde se aprende** (1 clase): [B70-C01 · Volcanismo basáltico: escudos, fisuras y llanuras planetarias](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md).

### Escudo radiativo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C13):** Cada vatio parásito acorta la vida de un criógeno. La decisión central: ¿cuántos escudos y qué soportes bastan para una vida útil dada?

📘 **Dónde se aprende** (1 clase): [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md).

### Escudo térmico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C23](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. ¿Por qué el escudo térmico tiene `α/ε` bajo?
- 🎯 **Por qué importa:** Cerca del Sol sobra energía y falta refrigeración; lejos, ocurre lo contrario. La decisión central: ¿qué escudo, qué enlace y qué fuente de energía exige cada extremo?

📘 **Dónde se aprende** (1 clase): [B47-C23 · Sondas heliosféricas: Parker Solar Probe y Voyager](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md).

### ESD

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B90-C03](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md):**
- La ESD Association (F11) publica ANSI/ESD S20.20 (versión 2021 citada en su página) y su página indica que el Departamento de Defensa de EE.
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué la ESD es un tema de integración y no solo de diseño?
- 🎯 **Por qué importa:** Un componente electrónico puede quedar con una falla latente tras una descarga que nadie sintió: una persona percibe una chispa solo por encima de unos miles de voltios (orden de magnitud no consultado), por encima de lo que puede dañar a un componente sensible.

📘 **Dónde se aprende** (1 clase): [B90-C03 · Protección frente a ESD](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md).

### ES/EF

- Camino crítico: cadena de holgura cero. ES/EF: inicio y fin tempranos.

🎯 **Por qué importa (clase B96-C09):** Una secuencia que no cabe en la ventana deja comandos sin ejecutar o telemetría sin confirmar. La decisión central: ¿qué actividades fijan la duración mínima y cuánta holgura queda?

📘 **Dónde se aprende** (1 clase): [B96-C09 · Secuencias de misión](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md).

### Esfera

- Una esfera es el conjunto de puntos a una distancia `R` de un centro.
- Una esfera de radio `r` tiene área superficial `4πr²` y volumen `(4/3)πr³`.

💡 **Cómo se explica en la clase [B03-C17](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md):**
- El elipsoide achatado generaliza la esfera: con `a = c` vuelve a `(4/3)πa³`.
- Si en cambio usaras una esfera de radio `a`, sobrestimarías el volumen en `a/c − 1 ≈ 0,34 %`.
- ⚠️ **Error frecuente:** Tratar la Tierra como esfera sin declararlo. Ejercicio 11.
- 🎯 **Por qué importa:** La NASA publica que la densidad media del Sol es 1408 kg/m³ (S1), cerca de una vez y media la del agua. ¿Cómo se obtiene?

📘 **Dónde se aprende** (2 clases): [B03-C17 · Áreas y volúmenes elementales](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md); [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md).

### Esfera celeste

- La esfera celeste es una esfera imaginaria, de radio arbitrario y centrada en el observador, sobre la que se proyecta la dirección de cada astro.

💡 **Cómo se explica en la clase [B08-C02](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md):**
- Falla porque la esfera celeste es un modelo: todos los astros se «pegan» a ella aunque estén a distancias muy distintas (B01-C02), y para objetos cercanos como la Luna (paralaje cercana a 1°) la dirección depende además del lugar.
- Ese recorrido, de salir, subir, cruzar el meridiano y bajar, es lo que la esfera celeste modela.
- 🎯 **Por qué importa:** Alguien en Punta Arenas ve girar algunas estrellas sin ponerse jamás; alguien en el valle del Elqui las ve rozar el horizonte, y alguien en el hemisferio norte no las ve nunca. Entender por qué evita comprar un telescopio para un objeto que no sale en tu cielo.

📘 **Dónde se aprende** (1 clase): [B08-C02 · Esfera celeste y horizonte local](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md).

### Esfera de exclusión

- La seguridad pasiva exige que la deriva sin maniobras no entre en la esfera de exclusión (aquí `200 m`, hipótesis del autor).

💡 **Cómo se explica en la clase [B76-C11](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md):**
- Con la esfera de exclusión de `200 m`, los dos primeros tramos son pasivamente seguros (`1000` y `285,9 m`), pero el último no: si falla `Δv2`, el perseguidor pasa a `35,7 m`.
- Rotular la esfera de exclusión como hipótesis.
- 🎯 **Por qué importa:** Una aproximación a baja velocidad no puede depender de que todos los impulsos se ejecuten. La decisión central: ¿cuántos tramos usar, cuánto cuestan y qué ocurre si el segundo impulso de un tramo falla?

📘 **Dónde se aprende** (1 clase): [B76-C11 · Operaciones de aproximación](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md).

### Esfera de fotones

- La esfera de fotones es la órbita circular (inestable) de la luz: `r = 3M`.

💡 **Cómo se explica en la clase [B27-C09](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md):**
- Para `10 M☉`, la frecuencia orbital en el ISCO es `219,9 Hz` y en la esfera de fotones `621,9 Hz` (con `f = c³/(2π (r/r_g)^{3/2} GM)`).
- *Descripción textual:* el máximo del potencial del fotón da la esfera de fotones y el parámetro crítico; la ecuación de la órbita da la precesión, que se compara con la fórmula débil.
- ⚠️ **Error frecuente:** Pensar que la esfera de fotones es estable. Se corrige con la sección 7.
- 🎯 **Por qué importa:** La sombra de un agujero negro no es su horizonte: es la imagen de la esfera de fotones ampliada por la curvatura. Y la fórmula `6πM/p` de la precesión solo vale lejos.

📘 **Dónde se aprende** (1 clase): [B27-C09 · Órbitas en campos fuertes](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md).

### Esfera de Hill

- La esfera de Hill es la región donde domina la gravedad del planeta.
- La esfera de Hill tiene radio `R_H = D (m/(3M))^(1/3)`.

💡 **Cómo se explica en la clase [B52-C11](../programa/clases/B52/B52-C11-formacion-de-satelites-naturales/CLASE.md):**
- Descripción larga: los satélites galileanos están muy dentro de la esfera de Hill, y la simulación sitúa el límite prógrado cerca de la mitad del radio de Hill.
- La evidencia es la ficha de los satélites en la esfera de Hill del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Los satélites regulares ocupan una pequeña fracción de la esfera de Hill, y el límite exterior de órbitas estables restringe dónde pudo existir el disco circumplanetario. La decisión central: ¿hasta qué fracción del radio de Hill puede haber satélites y dónde están los reales?

📘 **Dónde se aprende** (2 clases): [B52-C04 · Formación de planetesimales](../programa/clases/B52/B52-C04-formacion-de-planetesimales/CLASE.md); [B52-C11 · Formación de satélites naturales](../programa/clases/B52/B52-C11-formacion-de-satelites-naturales/CLASE.md).

### Esfera de influencia

- La esfera de influencia tiene radio `r_SOI = a_p (m/M)^{2/5}`.

💡 **Cómo se explica en la clase [B75-C07](../programa/clases/B75/B75-C07-sobrevuelos-planetarios/CLASE.md):**
- Un sobrevuelo sintético de la Tierra con `v∞ = 3,0 km/s` a `500 km` de altitud tiene `r_p = 6871 km`, `e = 1,1551`, `δ = 119,925°`, `v_p = 11,1814 km/s` y `B = 25 609 km`; cambia la velocidad heliocéntrica en `5,194 km/s` y la nave pasa `6,224 d` dentro de la esfera de influencia.
- Calcular el radio de la esfera de influencia y el tiempo dentro de ella.
- 🎯 **Por qué importa:** Para apuntar una nave a un sobrevuelo hay que saber a qué distancia pasará, a qué velocidad y cuánto tiempo estará bajo la influencia del planeta. La decisión central: ¿qué hipérbola corresponde a un `v∞` y una altitud de periapsis dados, y cuánto cambia la velocidad heliocéntrica?

📘 **Dónde se aprende** (1 clase): [B75-C07 · Sobrevuelos planetarios](../programa/clases/B75/B75-C07-sobrevuelos-planetarios/CLASE.md).

### Esfera de Laplace

- El radio de Hill aproximado es `a (μ/3)^(1/3)`; la esfera de Laplace es `a (GM_L/GM_T)^(2/5)`.

💡 **Cómo se explica en la clase [B76-C01](../programa/clases/B76/B76-C01-sistema-tierra-luna/CLASE.md):**
- Estimar el radio de Hill y la esfera de influencia de Laplace de la Luna.
- El script [sistema.py](sistema.py) calcula `μ`, el baricentro, `R_H`, la esfera de Laplace, los puntos `L1`–`L3` por bisección y las unidades del sistema Usa la biblioteca común [cislunar_lib.py](../cislunar_lib.py) del bloque (comprueba residuo de `dΩ/dx` < 1e-12, baricentro dentro de la Tierra y `L1`, `L2` cerca del radio de Hill).
- 🎯 **Por qué importa:** Una nave que sale de la Tierra hacia la Luna siente dos atracciones comparables en una región pequeña. La decisión central: ¿en qué punto del sistema deja de bastar el modelo de dos cuerpos y qué escalas gobiernan el problema?

📘 **Dónde se aprende** (1 clase): [B76-C01 · Sistema Tierra-Luna](../programa/clases/B76/B76-C01-sistema-tierra-luna/CLASE.md).

### Esfera de Strömgren

- La esfera de Strömgren es la región ionizada en equilibrio: dentro, cada fotón ionizante repone una recombinación; fuera, el gas es neutro.

💡 **Cómo se explica en la clase [B25-C05](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md):**
- Definir región HII, tasa de fotones ionizantes, recombinación, esfera de Strömgren y ley de Schmidt.
- 🎯 **Por qué importa:** Una galaxia no convierte todo su gas en estrellas a la vez: lo hace a un ritmo que puede medirse y comparar. Entender las regiones donde nacen las estrellas masivas permite reconocerlas desde lejos, y entender la relación entre gas y ritmo de formación permite saber cuánto tiempo puede una galaxia seguir formando estrellas.

📘 **Dónde se aprende** (1 clase): [B25-C05 · Regiones de formación estelar](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md).

### Esfera isoterma singular

- La esfera isoterma singular tiene `θ_E = 4π(σ_v/c)² D_ls/D_s`.

🎯 **Por qué importa (clase B36-C09):** Que la masa esté separada del gas es el argumento clave contra explicaciones sin materia oscura. La decisión central: ¿cuánto debe medir el desplazamiento y con qué incertidumbre se localiza la masa?

📘 **Dónde se aprende** (1 clase): [B36-C09 · Cúmulos en colisión como prueba de materia oscura](../programa/clases/B36/B36-C09-cumulos-en-colision-como-prueba-de-materia-oscura/CLASE.md).

### Esfera isoterma singular (SIS)

- La esfera isoterma singular (SIS) tiene `ρ ∝ r⁻²` y `M(<r) = 2σ² r/G`.
- Para una esfera isoterma singular (SIS) con dispersión `σ`, `θ_E = 4π(σ/c)² D_ls/D_s`.

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- Comparar esa masa con la de una esfera isoterma singular obtenida de la dispersión de las galaxias.
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.

📘 **Dónde se aprende** (2 clases): [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md); [B25-C14 · Lentes gravitacionales galácticas](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md).

### Esferas celestes sólidas

- Las esferas celestes sólidas eran el modelo aristotélico de los cielos como capas de cristal.

💡 **Cómo se explica en la clase [B02-C12](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md):**
- Sus observaciones de la supernova de 1572 y del cometa de 1577 mostraron que ambos objetos estaban más allá de la Luna, de modo que los cielos cambian, y el movimiento del cometa mostró que no podían existir esferas celestes sólidas (S1).
- Refuta la existencia de esferas celestes sólidas; no refuta la posición de la Tierra en el centro, que Tycho mantuvo.
- 🎯 **Por qué importa:** Una teoría solo es tan buena como los datos con que se contrasta. La pregunta motivadora es: ¿qué diferencia hay entre «mirar el cielo» y «observar sistemáticamente», y por qué esa diferencia cambió la astronomía?

📘 **Dónde se aprende** (1 clase): [B02-C12 · Tycho Brahe y observaciones sistemáticas](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md).

### Esferoide oblato

- Un esferoide oblato es una esfera achatada en los polos: semiejes `a` (ecuatorial) y `b < a`.

🎯 **Por qué importa (clase B09-C13):** Un telescopio necesita un espejo con forma de paraboloide. Cuánto vidrio hay que retirar de un disco plano para darle forma, cuánto pesa, y cuánta superficie hay que aluminizar son preguntas de volumen y área.

📘 **Dónde se aprende** (1 clase): [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md).

### Esferómetro

- El esferómetro de tres patas mide una pequeña sagita `h`.

💡 **Cómo se explica en la clase [B43-C04](../programa/clases/B43/B43-C04-fabricacion-y-desbaste-de-espejos/CLASE.md):**
- *Descripción textual:* el radio fija la sagita y el volumen; el esferómetro devuelve el radio; los granos fijan el plan.
- Medir el radio con un esferómetro y verificarlo por dos vías.
- 🎯 **Por qué importa:** El desbaste fija el radio de curvatura; los errores de esta etapa se pagan en horas de pulido. La decisión central: ¿cuánta profundidad hay que excavar, cómo se mide el radio y cuánto abrasivo se necesita en cada etapa?

📘 **Dónde se aprende** (1 clase): [B43-C04 · Fabricación y desbaste de espejos](../programa/clases/B43/B43-C04-fabricacion-y-desbaste-de-espejos/CLASE.md).

### Esfuerzo

- El esfuerzo es el trabajo de atenderla.

💡 **Cómo se explica en la clase [B110-C04](../programa/clases/B110/B110-C04-priorizacion-y-decisiones-bajo-emergencia/CLASE.md):**
- Para el orden `(F2, F4, F5, F1, F3, F6)` se acumulan los esfuerzos y se compara con el plazo: F2 termina a `10 ≤ 15`, F4 a `30 ≤ 55`, F5 a `65 ≤ 120`, F1 a `95 > 90` (se consume una de vehículo), F3 a `120`, F6 a `135`.
- F["fallas: nivel, plazo, esfuerzo"] --> O["orden de atencion"]
- 🎯 **Por qué importa:** B104 enseña los procedimientos; falta cómo se ordenan cuando coinciden. La decisión central: ¿qué se atiende primero y cuánto cuesta equivocarse de orden?

📘 **Dónde se aprende** (1 clase): [B110-C04 · Priorización y decisiones bajo emergencia](../programa/clases/B110/B110-C04-priorizacion-y-decisiones-bajo-emergencia/CLASE.md).

### Esfuerzo de aro

- El esfuerzo de aro de un cilindro delgado es `σ = P r/t`.
- Esfuerzo de aro: esfuerzo circunferencial `σ = P r/t`.

💡 **Cómo se explica en la clase [B59-C11](../programa/clases/B59/B59-C11-construccion-con-regolito/CLASE.md):**
- Calcular el esfuerzo de aro de un recipiente de pared delgada.
- Ejercicio 2 · con una pista. Esfuerzo de aro (8.3).
- 🎯 **Por qué importa:** Enterrar o cubrir un hábitat con regolito protege, pero no sustituye a la estructura. La decisión central: ¿cuánto espesor de regolito hace falta para blindar y cuánto para contener la presión interna?

📘 **Dónde se aprende** (2 clases): [B59-C11 · Construcción con regolito](../programa/clases/B59/B59-C11-construccion-con-regolito/CLASE.md); [B106-C02 · Presurización de módulos](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md).

### Eslabón más débil

- El eslabón más débil es el componente de menor TRL, que fija el del sistema.

🎯 **Por qué importa (clase B78-C19):** Una tecnología con un buen desempeño en papel puede estar lejos de volar. La decisión central: ¿en qué nivel está una tecnología según la evidencia que tiene, y qué nivel tiene un sistema formado por componentes de madureces distintas?

📘 **Dónde se aprende** (1 clase): [B78-C19 · Madurez tecnológica TRL](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md).

### Espaciado

- El espaciado `Δ` es la separación en esa unidad.
- Un espaciado `Δ` pequeño en radios de Hill mutuos favorece los encuentros cercanos.

💡 **Cómo se explica en la clase [B52-C10](../programa/clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md):**
- Construido con `Δ = 12` desde `0,05 ua`, `m = 5 M⊕`, `M* = 0,9 M☉` por bisección: semiejes `0.0500 0.0655 0.0857 0.1122 0.1469` ua, periodos `4.30 6.45 9.66 14.47 21.68` días y razón constante `1.4981` (el espaciado constante en `R_H` implica razón de periodos casi constante).
- Que un sistema esté espaciado en torno de una decena de radios de Hill es un dato descriptivo; no demuestra estabilidad.
- ⚠️ **Error frecuente:** Confundir distancia a escala absoluta con espaciado. Se corrige con 8.2.
- 🎯 **Por qué importa:** El espaciado mide cuán «apretado» está un sistema y cuán cerca está de la inestabilidad. La decisión central: ¿cómo se expresa el espaciado entre planetas independientemente de su escala?

📘 **Dónde se aprende** (2 clases): [B52-C10 · Arquitecturas de sistemas exoplanetarios](../programa/clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md); [B52-C19 · Estabilidad a largo plazo de sistemas](../programa/clases/B52/B52-C19-estabilidad-a-largo-plazo-de-sistemas/CLASE.md).

### Espaciado a lo largo de la traza

- El espaciado a lo largo de la traza es la distancia en el suelo entre pulsos.

💡 **Cómo se explica en la clase [B57-C11](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md):**
- Calcular el espaciado a lo largo de la traza como velocidad sobre el suelo entre tasa de pulsos.
- 🎯 **Por qué importa:** Un láser mide alturas con precisión de centímetros, pero a la luz del día el fondo solar inunda el detector. La decisión central: ¿cuántos fotones de señal hacen falta para distinguir la superficie del ruido y con qué error?

📘 **Dónde se aprende** (1 clase): [B57-C11 · LiDAR satelital](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md).

### Espaciado de períodos

- El espaciado de períodos `ΔΠ_l = Π₀/√(l(l+1))` es el de los modos g.
- El espaciado de períodos `ΔΠ₁` es la constante de los modos g de dipolo.

💡 **Cómo se explica en la clase [B37-C09](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md):**
- Calcular el espaciado de períodos `ΔΠ_l`.
- python programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/observables_sismicos.py
- 🎯 **Por qué importa:** Sin Δν y νmax habría que ajustar modelos para saber masa y radio. La decisión central: ¿qué precisión en masa y radio se obtiene con estos observables y qué supuestos exige?

📘 **Dónde se aprende** (2 clases): [B37-C09 · Frecuencias características: Δν, νmax y espaciado de períodos](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md); [B37-C12 · Gigantes rojas oscilantes y modos mixtos](../programa/clases/B37/B37-C12-gigantes-rojas-oscilantes-y-modos-mixtos/CLASE.md).

### Espaciado entre trazas

- El espaciado entre trazas en el ecuador es `2πR/N`.

💡 **Cómo se explica en la clase [B57-C23](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md):**
- El espaciado entre trazas en el ecuador es `229,0 km`, menor que los 250 km del modo IW: el barrido cubre todo el ecuador en 12 días.
- *Descripción textual:* la altitud fija el periodo y la inclinación heliosíncrona; la condición de repetición fija el número de órbitas por ciclo; el espaciado entre trazas se compara con el barrido.
- 🎯 **Por qué importa:** Si la órbita no repite sus trazas o el barrido no cubre el espacio entre ellas, quedan huecos. La decisión central: ¿qué altitud e inclinación dan un ciclo de repetición que cubre todo con el barrido disponible?

📘 **Dónde se aprende** (1 clase): [B57-C23 · Diseño de órbita y revisita para observación terrestre](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md).

### Espaciado radial

- El espaciado radial es la diferencia entre radios de anillos consecutivos.

🎯 **Por qué importa (clase B61-C07):** Las cuencas dejan huella en la corteza entera. La decisión central: ¿cómo se espacian los anillos, qué proyectil implica una cuenca y cuándo excava hasta el manto?

📘 **Dónde se aprende** (1 clase): [B61-C07 · Cuencas multianillo y grandes impactos](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md).

### Espacio de fase

- El espacio de fase son posición más velocidad.

💡 **Cómo se explica en la clase [B38-C03](../programa/clases/B38/B38-C03-cinematica-estelar-con-gaia-movimientos-propios-y-espacio-de-fase/CLASE.md):**
- python programa/clases/B38/B38-C03-cinematica-estelar-con-gaia-movimientos-propios-y-espacio-de-fase/cinematica.py
- 🎯 **Por qué importa:** El error de distancia se propaga a todas las velocidades tangenciales. La decisión central: ¿cuánto error de paralaje tolera la medida de una dispersión de velocidades?

📘 **Dónde se aprende** (1 clase): [B38-C03 · Cinemática estelar con Gaia: movimientos propios y espacio de fase](../programa/clases/B38/B38-C03-cinematica-estelar-con-gaia-movimientos-propios-y-espacio-de-fase/CLASE.md).

### Espacio de fases

- El espacio de fases es el conjunto de todos los estados posibles.

💡 **Cómo se explica en la clase [B11-C04](../programa/clases/B11/B11-C04-sistemas-de-ecuaciones-diferenciales/CLASE.md):**
- Cada instante es un punto en el espacio de fases; la ecuación `s′ = F(s)` es un campo de velocidades en ese espacio, y la solución es la curva que sigue el punto.
- 🎯 **Por qué importa:** Un programa que propaga una trayectoria no entiende `r″ = −GM r/|r|³`: entiende una función que recibe un estado y devuelve su derivada. Si escribes mal ese puente, ningún método, por bueno que sea, te salva.

📘 **Dónde se aprende** (1 clase): [B11-C04 · Sistemas de ecuaciones diferenciales](../programa/clases/B11/B11-C04-sistemas-de-ecuaciones-diferenciales/CLASE.md).

### Espacio de fases mixto

- Un espacio de fases mixto tiene islas regulares y un mar caótico: `λ` depende de la condición inicial.

💡 **Cómo se explica en la clase [B73-C14](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md):**
- Con `K = 1` y `K = 2` los valores por condición inicial van de casi cero a `0,08` y `0,46`: el espacio de fases es mixto y el promedio engaña.
- 🎯 **Por qué importa:** El exponente de Lyapunov es el número que cuantifica el caos: fija el horizonte de predicción y distingue una trayectoria regular de una caótica. En un espacio de fases mixto, un solo exponente no basta.

📘 **Dónde se aprende** (1 clase): [B73-C14 · Exponentes de Lyapunov](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md).

### Espacio de paridad

- El espacio de paridad es el subespacio de las medidas que ningún vector de estado puede producir.

🎯 **Por qué importa (clase B80-C05):** B88-C12 trata la detección y recuperación de fallas en general, no el arbitraje de las mediciones que alimentan la navegación. La decisión central: ¿cómo sabe el sistema que un sensor miente, y cuál es, sin una referencia externa?

📘 **Dónde se aprende** (1 clase): [B80-C05 · Redundancia de sensores y arbitraje de mediciones](../programa/clases/B80/B80-C05-redundancia-de-sensores-y-arbitraje-de-mediciones/CLASE.md).

### Espacio de secuencias

- El espacio de secuencias es el conjunto de todas las secuencias posibles de longitud `L`, de tamaño `M = 4^L` con cuatro letras.

💡 **Cómo se explica en la clase [B56-C04](../programa/clases/B56/B56-C04-hipotesis-de-abiogenesis/CLASE.md):**
- El espacio de secuencias es un lago; cada ensayo es una tirada de caña.
- Cuenta de espacio de secuencias (esta clase): simple, pone cotas.
- 🎯 **Por qué importa:** Las hipótesis (mundo de ARN, metabolismo primero, ventilas hidrotermales, charcas con ciclos húmedo–seco, aporte meteorítico) se discuten a menudo con palabras. Una cuenta de espacio de secuencias permite saber cuándo una afirmación es plausible por números y cuándo exige un mecanismo de selección.

📘 **Dónde se aprende** (1 clase): [B56-C04 · Hipótesis de abiogénesis](../programa/clases/B56/B56-C04-hipotesis-de-abiogenesis/CLASE.md).

### Espacio de trabajo

- El espacio de trabajo es el conjunto de puntos alcanzables.
- El espacio de trabajo es el conjunto de puntos que alcanza la mano.
- Espacio de trabajo: conjunto de posiciones que alcanza el extremo.

💡 **Cómo se explica en la clase [B97-C02](../programa/clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md):**
- Reconocer la singularidad en el borde del espacio de trabajo y su efecto.
- 🎯 **Por qué importa:** Cada vez que un brazo coge una carga o una herramienta alguien resolvió una cinemática inversa y comprobó que el movimiento no pasa por una singularidad. Sin esa comprobación, un movimiento pequeño de la punta exige velocidades articulares enormes.

📘 **Dónde se aprende** (3 clases): [B97-C02 · Cinemática de manipuladores](../programa/clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md); [B101-C04 · Límites articulares, espacio de trabajo y evitación de colisiones](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md); [B107-C02 · Movilidad articular, flexibilidad y postura](../programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/CLASE.md).

### Espacio generado

- El espacio generado (span) por un conjunto es el conjunto de todas sus combinaciones lineales.

🎯 **Por qué importa (clase B10-C01):** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Espacio interestelar

- El espacio interestelar es la región fuera de la heliosfera (S3).

🎯 **Por qué importa (clase B02-C19):** La exploración espacial es una historia científica y también política. La pregunta motivadora es: ¿qué cambió, para la astronomía y para la sociedad, cuando los instrumentos y las personas empezaron a salir de la atmósfera, y qué reglas se acordaron?

📘 **Dónde se aprende** (1 clase): [B02-C19 · Historia de la exploración espacial](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md).

### Espacio muestral

- El espacio muestral `Ω` es el conjunto de todos los resultados posibles, sin repeticiones ni omisiones.

💡 **Cómo se explica en la clase [B12-C01](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md):**
- A["Experimento:<br/>3 computadores"] --> B["Espacio muestral Ω<br/>8 resultados FFF…XXX"]
- Enumerar el espacio muestral de un experimento sencillo y verificar que sus probabilidades suman 1.
- 🎯 **Por qué importa:** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.

📘 **Dónde se aprende** (1 clase): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md).

### Espacio nulo

- El espacio nulo de `A` son los vectores `v` con `A v = 0`: sumarlos a una solución no cambia los datos.
- Redundancia: más articulaciones que dimensiones de la tarea. Espacio nulo: movimientos articulares que no mueven el extremo.

💡 **Cómo se explica en la clase [B22-C01](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md):**
- Reconocer una no unicidad (espacio nulo) y escribir la familia completa de soluciones.
- (a) Unicidad (espacio nulo de dimensión 1).
- 🎯 **Por qué importa:** Un telescopio nunca entrega la imagen verdadera del cielo: la entrega emborronada por su respuesta óptica y con ruido. Calcular lo que verá el telescopio si conoces el objeto es fácil; el camino contrario, recuperar el objeto desde lo que vio, es el que interesa a la ciencia y el que se complica.

📘 **Dónde se aprende** (2 clases): [B22-C01 · Problemas directos e inversos y mal condicionamiento](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md); [B101-C02 · Cinemática inversa y redundancia de manipuladores](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md).

### Espacio profundo

- El espacio profundo se aproxima aquí como un sumidero a `3 K`.

💡 **Cómo se explica en la clase [B85-C07](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md):**
- Un radiador de `500 W` a `290 K` con `ε = 0,85` necesita `1,47 m²` en espacio profundo, `1,89 m²` en órbita baja con valores iniciales y `2,38 m²` con valores de fin de vida.
- Descripción larga: el entorno y el envejecimiento añaden más de la mitad del área respecto del espacio profundo; subir 20 K la reduce un tercio.
- 🎯 **Por qué importa:** El área del radiador manda en masa, volumen y costo. La decisión central: ¿cuánta área necesita un radiador en el caso caliente de fin de vida y qué la reduce?

📘 **Dónde se aprende** (1 clase): [B85-C07 · Radiadores espaciales](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md).

### Espacio vectorial real

- Un espacio vectorial real es un conjunto `V` con una suma `u + v` y un producto por escalares reales `a·u` que cumplen ocho propiedades: la suma es conmutativa y asociativa; existe un vector cero que no cambia nada; todo vector tiene un opuesto; y el producto por escalares es distributivo sobre la suma de vectores y de escalares, asociativo y con `1·u = u` (S1 usa `ℝⁿ` con estas operaciones en §1.2(v)).

💡 **Cómo se explica en la clase [B10-C01](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md):**
- Enunciar los ocho axiomas de un espacio vectorial real y reconocerlos en `ℝⁿ`.
- 🎯 **Por qué importa:** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Espacio-tiempo de Minkowski

- El espacio-tiempo de Minkowski es el conjunto de eventos con la métrica `s² = (ct)² − x² − y² − z²`.

💡 **Cómo se explica en la clase [B26-C04](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md):**
- Definir el espacio-tiempo de Minkowski y el intervalo.
- python programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/gemelos.py
- 🎯 **Por qué importa:** Comunicar con una sonda, sincronizar relojes de dos estaciones o decidir si un evento puede haber causado otro exige saber cuándo dos sucesos están conectados por una señal. El intervalo lo decide para todos los observadores.

📘 **Dónde se aprende** (1 clase): [B26-C04 · Espacio-tiempo de Minkowski](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md).

### Especie traza

- Una especie traza es una con fracción mucho menor que 1.

🎯 **Por qué importa (clase B54-C02):** Dos atmósferas con la misma temperatura y gravedad tienen alturas de escala distintas si sus gases pesan distinto. La pregunta motivadora: ¿qué parte de la diferencia entre las atmósferas de los planetas viene solo de la composición?

📘 **Dónde se aprende** (1 clase): [B54-C02 · Composición química atmosférica](../programa/clases/B54/B54-C02-composicion-quimica-atmosferica/CLASE.md).

### Especificidad

- La especificidad `e` es `P(negativo | no H)`.
- La sensibilidad, la especificidad, el VPP y el VPN miden un umbral.
- Sensibilidad `TP/(TP+FN)` y especificidad `TN/(TN+FP)`.

💡 **Cómo se explica en la clase [B63-C06](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md):**
- Un marco sintético: la probabilidad previa de peligro es `10⁻³`, cada prueba tiene sensibilidad `0,90` y especificidad `0,95`, y el costo de retener es `1` frente a `10⁵` de liberar una muestra peligrosa (unidades arbitrarias).
- Aplicar el teorema de Bayes a una prueba con sensibilidad y especificidad conocidas.
- 🎯 **Por qué importa:** Ninguna prueba demuestra que no hay peligro; solo reduce la incertidumbre. La decisión central: ¿cuántas pruebas negativas hacen falta antes de que liberar sea preferible a retener, y de qué dependen?

📘 **Dónde se aprende** (3 clases): [B63-C06 · Evaluación de riesgos biológicos de muestras: marcos de decisión](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md); [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md); [B116-C04 · Triage asistido por decisión](../programa/clases/B116/B116-C04-triage-asistido-por-decision/CLASE.md).

### Específico

- Un comentario es específico si cita un dato verificable del trabajo.

💡 **Cómo se explica en la clase [B131-C10](../programa/clases/B131/B131-C10-retroalimentacion-efectiva/CLASE.md):**
- 12 comentarios reescritos: 4 de tarea, 3 de proceso, 4 de autorregulación y 1 de persona (`8,3 %`); 7 son específicos (`58 %`).
- Reescribir mueve el foco de la persona a la acción, y aumenta lo específico.
- 🎯 **Por qué importa:** Un comentario como «muy bien» o «desastre» no dice qué hacer. La decisión central: ¿qué información da este comentario al estudiante para su próximo paso?

📘 **Dónde se aprende** (1 clase): [B131-C10 · Retroalimentación efectiva](../programa/clases/B131/B131-C10-retroalimentacion-efectiva/CLASE.md).

### Espectro

- El espectro es la luz descompuesta por longitud de onda.
- Un espectro es la distribución de la luz por longitud de onda.
- El espectro es el conjunto de autovalores.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- Observa que el patrón (la distancia relativa entre líneas) se conserva aunque todo el espectro se corra.
- Si todas dan el mismo `z` dentro del error, el corrimiento es de todo el espectro, no un error de identificación.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📖 **Explicado a fondo:** [Espectro y espectroscopía](esencial/esencial-d-l.md#espectro-y-espectroscopía) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (9 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md); [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md); [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B35-C09 · Turbulencia en plasmas y MHD](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md); [B36-C02 · Función de transferencia y espectro de materia](../programa/clases/B36/B36-C02-funcion-de-transferencia-y-espectro-de-materia/CLASE.md) y 3 más.

### Espectro angular

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B40-C07](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md):**
- La evidencia es la ficha del espectro angular del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha del espectro angular*: `θ*`, `ℓ_A`, picos y ida y vuelta.
- 🎯 **Por qué importa:** Los picos acústicos fijan la geometría y el contenido del universo. La decisión central: ¿dónde caen los picos (`ℓ_A = π/θ*`) y cómo se pasa del espectro a la correlación y de vuelta?

📘 **Dónde se aprende** (1 clase): [B40-C07 · Espectro angular de potencias del CMB](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md).

### Espectro continuo

- Un espectro continuo tiene luz en todas las longitudes de onda; uno de emisión muestra líneas brillantes sobre fondo oscuro; uno de absorción muestra líneas oscuras sobre un fondo continuo.
- Un espectro continuo tiene todos los colores; uno de absorción tiene líneas oscuras donde un gas absorbe; uno de emisión tiene líneas brillantes donde un gas emite.
- Un espectro continuo tiene luz en todos los colores; un espectro de emisión muestra líneas brillantes (un gas caliente emite sólo a ciertas longitudes de onda); uno de absorción muestra líneas oscuras (un gas más frío delante de una fuente continua absorbe esas mismas longitudes).

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- Distinguir espectro continuo, de emisión y de absorción.
- Ejercicio 12 · integrador. Elabora tu interpretación de un espectro sencillo: con un espectro sintético dado (o uno que construyas con tres líneas), calcula `z` por línea, verifica un corrimiento común, estima velocidad aparente, indica una estimación de temperatura si hay continuo y rotula cada resultado O, I o M con supuestos.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📘 **Dónde se aprende** (3 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md); [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Espectro cruzado

- El espectro cruzado es `conj(F₁) F₂`.
- El espectro cruzado `B A*`.

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- F --> X["Espectro cruzado<br/>normalizado R"]
- *Descripción textual:* con las dos imágenes se calcula el espectro cruzado normalizado, cuyo pico da el desplazamiento entero, que se refina de forma local; alternativamente, con pares de puntos homólogos se estiman ángulo y traslación por Procrustes.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».

📘 **Dónde se aprende** (3 clases): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md); [B36-C08 · Sesgo de galaxias y trazadores de la materia](../programa/clases/B36/B36-C08-sesgo-de-galaxias-y-trazadores-de-la-materia/CLASE.md); [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Espectro de emisión

- Un espectro continuo tiene luz en todos los colores; un espectro de emisión muestra líneas brillantes (un gas caliente emite sólo a ciertas longitudes de onda); uno de absorción muestra líneas oscuras (un gas más frío delante de una fuente continua absorbe esas mismas longitudes).

💡 **Cómo se explica en la clase [B06-C17](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md):**
- Distinguir un espectro continuo, de emisión y de absorción, y decir qué indica cada uno.
- 🎯 **Por qué importa:** En B01-C01 estimaste la velocidad de una galaxia con una sola línea, H-alfa en 662,9 nm. Pero ¿cómo se sabe que esa línea es H-alfa y no otra?

📘 **Dónde se aprende** (1 clase): [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Espectro de masas

- Fuente metabólica: CO₂, vapor y trazas de las personas. Espectro de masas: huella de un compuesto.

🎯 **Por qué importa (clase B106-C22):** Nada sale al exterior de una cabina cerrada: los materiales emiten gases durante meses, los equipos liberan trazas y las personas emiten vapor y CO₂. La decisión central: ¿qué fuentes dominan en cada momento y cómo se identifican los compuestos para decidir qué retirar?

📘 **Dónde se aprende** (1 clase): [B106-C22 · Fuentes e identificación de contaminantes del aire de cabina](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md).

### Espectro de potencia

- El espectro de potencia de Kolmogorov.

🎯 **Por qué importa (clase B42-C11):** La atmósfera fija el límite de resolución de los telescopios terrestres y es la perturbación que corrige la óptica adaptativa. La decisión central: ¿cómo se simula una pantalla de fase con la estadística correcta y qué errores introduce la malla?

📘 **Dónde se aprende** (1 clase): [B42-C11 · Turbulencia atmosférica](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md).

### Espectro de potencias

- El espectro de potencias `P(k)`.

🎯 **Por qué importa (clase B40-C05):** El espectro es el vínculo entre la inflación y las anisotropías. La decisión central: ¿qué predice el modelo para `n_s` y `r`, y es compatible con los límites publicados?

📘 **Dónde se aprende** (1 clase): [B40-C05 · Perturbaciones primordiales y espectro escalar](../programa/clases/B40/B40-C05-perturbaciones-primordiales-y-espectro-escalar/CLASE.md).

### Espectro diferencial

- El espectro diferencial es `dΦ/dL = 2Φ₁L⁻³` si `Φ(>L) = Φ₁L⁻²`.

🎯 **Por qué importa (clase B85-C21):** Un upset en un procesador o en una memoria puede reiniciar un instrumento o corromper un dato. La decisión central: ¿con qué frecuencia ocurre un evento único en un dispositivo dado y cuánto cambia si se elige un componente de mayor umbral de LET?

📘 **Dónde se aprende** (1 clase): [B85-C21 · Efectos de partículas energéticas en electrónica y materiales](../programa/clases/B85/B85-C21-efectos-de-particulas-energeticas-en-electronica-y-materiales/CLASE.md).

### Espectro dinámico

- El espectro dinámico muestra la deriva.

💡 **Cómo se explica en la clase [B30-C21](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md):**
- *Descripción textual:* la posición del haz fija la densidad y la frecuencia; de ahí salen la deriva y el espectro dinámico, del que se recupera la cresta y la velocidad.
- Construir un espectro dinámico sintético con ruido.
- 🎯 **Por qué importa:** Una frecuencia es una altura, y la deriva en frecuencia da la velocidad del haz. La decisión central: ¿cómo se convierte un espectro dinámico en la velocidad de los electrones?

📘 **Dónde se aprende** (1 clase): [B30-C21 · Radioemisión solar: estallidos de radio y su observación](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md).

### Espectro electromagnético

- El espectro electromagnético ordena las ondas por frecuencia: radio, microondas, infrarrojo, visible, ultravioleta, rayos X y gamma.

🎯 **Por qué importa (clase B05-C18):** Un satélite se comunica con ondas de radio, un telescopio observa luz y rayos X, y la misma radiación a otras energías puede dañar electrónica y tejidos. La pregunta motivadora es: ¿qué es la radiación electromagnética, cómo se ordena por frecuencia y energía, cómo decae con la distancia y qué la hace peligrosa?

📘 **Dónde se aprende** (1 clase): [B05-C18 · Electromagnetismo y radiación](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md).

### Espectro molecular

- Un espectro molecular tiene además líneas por la rotación y la vibración de la molécula, que caen en el infrarrojo y las microondas.

💡 **Cómo se explica en la clase [B06-C17](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md):**
- python programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/identificar_lineas.py
- 🎯 **Por qué importa:** En B01-C01 estimaste la velocidad de una galaxia con una sola línea, H-alfa en 662,9 nm. Pero ¿cómo se sabe que esa línea es H-alfa y no otra?

📘 **Dónde se aprende** (1 clase): [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Espectro secundario

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C15](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md):**
- Hay espectro secundario porque las dispersiones parciales no son proporcionales.
- ⚠️ **Error frecuente:** Creer que el doblete elimina todo el color. Queda espectro secundario.
- 🎯 **Por qué importa:** Un refractor sin color necesita combinar vidrios. La decisión central: ¿cuánto color queda con dos o tres vidrios?

📘 **Dónde se aprende** (1 clase): [B41-C15 · Refractores acromáticos y apocromáticos](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md).

### Espectro sintético

- Espesor másico: densidad × espesor (g/cm²). Espectro sintético: distribución de energías inventada.

💡 **Cómo se explica en la clase [B106-C14](../programa/clases/B106/B106-C14-proteccion-contra-radiacion/CLASE.md):**
- S["espectro sintetico E^-2.5"] --> B["blindaje x g/cm2"]
- *Descripción textual:* el espesor fija la energía mínima que lo atraviesa; con el espectro sintético se obtiene la fracción detenida y con la geometría, la masa.
- ⚠️ **Error frecuente:** Tomar el espectro sintético como real. Es inventado (sección 10).
- 🎯 **Por qué importa:** Las paredes y el regolito detienen partículas, pero con límites: la masa es costosa y las partículas secundarias complican el panorama. La decisión central: ¿cuánta masa por área detiene qué parte de las partículas, y dónde el modelo deja de valer?

📘 **Dónde se aprende** (1 clase): [B106-C14 · Protección contra radiación](../programa/clases/B106/B106-C14-proteccion-contra-radiacion/CLASE.md).

### Espectrograma

- El espectrograma es la fotografía de un espectro (C16).

🎯 **Por qué importa (clase B02-C17):** Un dibujo depende de quien lo hace; una placa registra lo que llegó. La pregunta motivadora es: ¿qué cambia cuando la observación puede guardarse, compararse años después y medirse?

📘 **Dónde se aprende** (1 clase): [B02-C17 · Nacimiento de la astrofotografía](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md).

### Espectrometría de masas

- La espectrometría de masas separa iones por su relación masa/carga (`m/z`); cada especie deja un patrón de fragmentación en varios canales.

💡 **Cómo se explica en la clase [B67-C07](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md):**
- B) Espectrometria de masas: desmezcla de 5 especies en 6 canales
- python programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/sensores.py
- 🎯 **Por qué importa:** Un sensor no mide «agua»: mide cuentas, y de ellas se infiere la abundancia con un modelo. La decisión central: ¿cuánto tiempo de medición y qué canales hacen falta para detectar y separar un volátil con la incertidumbre requerida?

📘 **Dónde se aprende** (1 clase): [B67-C07 · Sensores para volátiles: espectrometría de neutrones y de masas](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md).

### Espectrómetro de masas cuadrupolar (QMS)

- El espectrómetro de masas cuadrupolar (QMS) mide el gas por masa.

💡 **Cómo se explica en la clase [B68-C04](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md):**
- Kruczkiewicz y colaboradores (2024) hacen TPD a `0,2 K s⁻¹` desde 10 K y detectan los gases con un espectrómetro de masas cuadrupolar;
- 🎯 **Por qué importa:** Un hielo de 10 ML de CO sobre una superficie a 10 K se contamina con agua residual en horas si la presión de fondo no es lo bastante baja, y una TPD con bombeo insuficiente deforma el pico que se mide.

📘 **Dónde se aprende** (1 clase): [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### Espectroscopio

- Un espectroscopio descompone la luz.

💡 **Cómo se explica en la clase [B02-C16](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md):**
- A["Luz del astro"] --> B["Espectroscopio:<br/>separa por longitud de onda"]
- *Descripción textual:* la luz del astro pasa por un espectroscopio que la separa por longitud de onda; se miden posiciones e intensidades de líneas; se comparan con las del laboratorio para identificar elementos; la conclusión sobre composición tiene límites.
- 🎯 **Por qué importa:** Hasta 1859 se pensaba, con razones, que nunca sabríamos de qué están hechas las estrellas: estaban demasiado lejos para tocarlas. La pregunta motivadora es: ¿cómo se puede conocer la composición de un objeto que solo se ve como luz?

📘 **Dónde se aprende** (1 clase): [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md).

### Espejo cóncavo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C04):** El espejo primario de un telescopio reflector es una superficie cónica. La decisión central: ¿por qué se usa un paraboloide y no una esfera?

📘 **Dónde se aprende** (1 clase): [B41-C04 · Espejos esféricos y parabólicos](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md).

### Espejo deformable

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C15](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md):**
- La evidencia es la ficha del espejo deformable del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha del espejo deformable*: paso, error de ajuste y escala.
- 🎯 **Por qué importa:** El número de actuadores fija el error de ajuste que ninguna medición mejora. La decisión central: ¿cuántos actuadores se necesitan para un `r₀` dado?

📘 **Dónde se aprende** (1 clase): [B42-C15 · Espejos deformables](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md).

### Espejo magnético

- El espejo magnético refleja partículas con ángulo de paso grande.

💡 **Cómo se explica en la clase [B30-C06](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md):**
- *Descripción textual:* la fuerza de Lorentz integrada con Boris da el giro, la deriva y el rebote en el espejo, con el momento magnético conservado.
- 🎯 **Por qué importa:** El movimiento de las partículas explica cómo se atrapan en los cinturones, cómo derivan y cómo se aceleran. La decisión central: ¿cuándo queda atrapada una partícula y cuánto vale su radio de giro?

📘 **Dónde se aprende** (1 clase): [B30-C06 · Partículas cargadas y movimientos](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md).

### Espejo solar óptico (OSR)

- Un espejo solar óptico (OSR) es un radiador de `α` bajo y `ε` alta.

🎯 **Por qué importa (clase B85-C05):** Cambiar un recubrimiento es la forma más barata de mover la temperatura de una superficie decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la superficie dentro del intervalo al principio y al final de la vida?

📘 **Dónde se aprende** (1 clase): [B85-C05 · Recubrimientos ópticos térmicos](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md).

### Espera en cola

- Ocupación `ρ`: tasa de llegada por tiempo de servicio. Espera en cola `W_q`.

💡 **Cómo se explica en la clase [B48-C16](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md):**
- En un programa real los cuadros llegan a cadencia fija (cola D/D/1, sin espera si `D` es menor que la cadencia): el modelo de Poisson sobreestima la espera y sirve para ráfagas, no para el régimen estable.
- *Descripción textual:* la ocupación determina la espera de la cola: pequeña con carga baja, divergente cerca de uno; la recursión de Lindley la verifica.
- ⚠️ **Error frecuente:** Confundir espera en cola con tiempo total. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Si la reducción no sigue el ritmo, se acumulan cuadros y el resultado llega tarde. La decisión central: ¿hasta qué ocupación del procesador es tolerable la espera?

📘 **Dónde se aprende** (1 clase): [B48-C16 · Procesamiento de datos en línea](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md).

### Espera fría

- Repuesto: unidad de reemplazo. Espera fría: unidad apagada que se conecta al fallar la principal.

💡 **Cómo se explica en la clase [B106-C18](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md):**
- La espera fría perfecta da 0,97977 y con conmutador de 0,95, 0,97107: el conmutador limita la mejora.
- Incluir la causa común (factor β) y un conmutador imperfecto en la espera fría.
- 🎯 **Por qué importa:** Ningún equipo es perfecto y una misión larga no se puede reparar con repuestos de la Tierra. La decisión central: ¿qué configuración redundante y cuántos repuestos dan una probabilidad objetivo de cumplir la misión?

📘 **Dónde se aprende** (1 clase): [B106-C18 · Fiabilidad y redundancia](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md).

### Espera media

- Función de distribución: probabilidad de no superar un valor. Espera media: inversa de la probabilidad por noche.

💡 **Cómo se explica en la clase [B48-C11](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md):**
- Calcular la espera media hasta una clase dada.
- Espera media hasta una noche A = 4.97 noches; noches A por año = 73.4
- 🎯 **Por qué importa:** Un programa que exige la mejor calidad espera mucho; uno que acepta cualquiera desperdicia las buenas noches. La decisión central: ¿con qué frecuencia se da cada clase y cuánto hay que esperar?

📘 **Dónde se aprende** (1 clase): [B48-C11 · Calidad y clasificación de datos](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md).

### Espera Wq

- Utilización: `ρ = λ/μ`. Espera `Wq`: tiempo en cola.

💡 **Cómo se explica en la clase [B96-C26](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md):**
- La prioridad no reduce la espera global (1,491 y 1,492 h); la redistribuye: la alta espera la mitad y la baja espera 17 % más.
- *Descripción textual:* los incidentes de dos prioridades entran a una sola cola y un equipo los atiende de a uno; la teoría de colas da la espera por clase y la simulación la verifica.
- 🎯 **Por qué importa:** Sin un procedimiento de priorización, un incidente leve puede retrasar a uno grave. La decisión central: ¿cuánto esperan los incidentes de alta y de baja prioridad y cuánto mejora la priorización al grave sin colapsar al leve?

📘 **Dónde se aprende** (1 clase): [B96-C26 · Gestión de incidentes en la operación de estaciones](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md).

### Esperanza

- La esperanza (o valor esperado) `E[X]` es el promedio de los valores ponderado por su probabilidad (S1, C.2.9): `Σ x p(x)` en una discreta, `∫ x f(x) dx` en una continua.
- La esperanza por orden es `E = T_ok + (1/q − 1) T_to`.

💡 **Cómo se explica en la clase [B12-C04](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md):**
- Aquí `E[X] = 2,7` no es un valor que `X` pueda tomar: la esperanza es un promedio a largo plazo, no un valor típico.
- La esperanza es el punto de equilibrio de la distribución, como el centro de masa de una barra con pesos; la varianza es su momento de inercia respecto de ese centro, y la desviación típica su radio de giro.
- 🎯 **Por qué importa:** Un ingeniero no maneja distribuciones completas; maneja «la medida es 150,0 m con una incertidumbre de 3 m». Esa frase usa exactamente una esperanza y una desviación típica.

📘 **Dónde se aprende** (2 clases): [B12-C04 · Esperanza y varianza](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md); [B98-C06 · Simulación de teleoperación con retardo](../programa/clases/B98/B98-C06-simulacion-de-teleoperacion-con-retardo/CLASE.md).

### Esperanza de bajas

- La esperanza de bajas `E_c` es el número medio de víctimas.
- La esperanza de bajas `Ec = Pf·ρ·Ac·(1 − refugio)` usa la probabilidad de falla, la densidad de población, el área de baja efectiva y la fracción de refugio.

💡 **Cómo se explica en la clase [B83-C21](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md):**
- T["Trayectoria: Pf, densidad, area"] --> E["Esperanza de bajas Ec"]
- *Descripción textual:* la operación se divide en nodos y se recorre con palabras guía para listar peligros con severidad y verosimilitud; los de severidad alta se revisan aunque su índice sea bajo; por separado, la esperanza de bajas de la trayectoria se compara con el umbral y su incertidumbre se estudia por Monte Carlo y por fórmula.
- 🎯 **Por qué importa:** Los peligros que no se identifican no se pueden controlar. La decisión central: ¿qué puede salir mal en cada fase, qué tan grave y probable es, y el riesgo para terceros cabe en el umbral que el proyecto adoptó?

📘 **Dónde se aprende** (2 clases): [B83-C21 · Identificación de peligros en sistemas de lanzamiento (HAZID)](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md); [B119-C22 · Seguridad de instalaciones y operaciones de sitio de lanzamiento](../programa/clases/B119/B119-C22-seguridad-de-instalaciones-y-operaciones-de-sitio-de-lanzamiento/CLASE.md).

### Espesor crítico

- El espesor crítico `h_c` es aquel por debajo del cual la colada se detiene.

💡 **Cómo se explica en la clase [B70-C07](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md):**
- *Descripción textual:* la pendiente, el espesor y la reología dan el caudal si el espesor supera el crítico; la velocidad, el ángulo, la gravedad y el aire dan el alcance de los clastos.
- Calcular el espesor crítico de Bingham `h_c = τ_y/(ρ g sinθ)`.
- 🎯 **Por qué importa:** La misma lava fluye distinto según la pendiente, el espesor y la reología; los piroclastos llegan más lejos si no hay aire. La decisión central: ¿cuánto fluye una colada y hasta dónde llegan los clastos en cada mundo?

📘 **Dónde se aprende** (1 clase): [B70-C07 · Flujos de lava y depósitos piroclásticos](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md).

### Espesor de equilibrio

- El espesor de equilibrio `t_eq = P/(ρ g)` sería el que contiene la presión interna solo con peso.

💡 **Cómo se explica en la clase [B97-C14](../programa/clases/B97/B97-C14-construccion-con-regolito-robotica-y-construccion-extraterrestre/CLASE.md):**
- cuerpo sobrecarga [kPa] fraccion de P espesor de equilibrio [m] presion neta hacia arriba [kPa]
- 🎯 **Por qué importa:** Quien cree que el regolito «sostiene» el hábitat se equivoca: con baja gravedad, el peso de una cubierta de poco más de un metro cubre solo una pequeña fracción de la presión interna. La estructura debe resistir la diferencia por tracción o anclaje.

📘 **Dónde se aprende** (1 clase): [B97-C14 · Construcción con regolito — Robótica y construcción extraterrestre](../programa/clases/B97/B97-C14-construccion-con-regolito-robotica-y-construccion-extraterrestre/CLASE.md).

### Espesor del hielo

- El espesor del hielo `d_h` es la profundidad de la capa sólida.

💡 **Cómo se explica en la clase [B56-C09](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md):**
- El volumen fija casi todo; el espesor del hielo pesa menos en la profundidad y más en la presión.
- Descripción larga: la profundidad del océano casi no depende del espesor del hielo; la presión sí, porque suma la columna de hielo.
- ⚠️ **Error frecuente:** Presentar el espesor del hielo como dato. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un océano global bajo el hielo es un candidato a hábitat, protegido de la radiación y del vacío. Saber cuán profundo es y qué presión soporta fija qué sondas podrían llegar y qué ambientes existen.

📘 **Dónde se aprende** (1 clase): [B56-C09 · Océanos de Europa](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md).

### Espesor en el borde

- El espesor en el borde `t_rim` es la referencia.

💡 **Cómo se explica en la clase [B61-C04](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md):**
- Con `t_rim` = 0,04 R, el espesor cae de 0,0400 R en el borde a 0,0050 R en 2 R y 0,0015 R en 3 R.
- ⚠️ **Error frecuente:** Olvidar que el borde es el espesor máximo. Se corrige con 8.1.
- 🎯 **Por qué importa:** El manto de ejecta es un marcador estratigráfico: cubre lo anterior y es cubierto por lo posterior. La decisión central: ¿cómo decae el espesor con la distancia y cuánto volumen contiene el manto?

📘 **Dónde se aprende** (1 clase): [B61-C04 · Mantos de ejecta y depósitos de impacto](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md).

### Espesor gobernante

- El espesor gobernante es el mayor de los requeridos.

💡 **Cómo se explica en la clase [B85-C28](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md):**
- Con un factor de atenuación `2,2` veces el del aluminio por milímetro y densidad `950 kg/m³`, el polietileno cumple la dosis con `5,33 mm`, pero la perforación impone `21,5 mm` y el espesor gobernante es `21,5 mm`: masa `10,20 kg`, menos de la mitad.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de diseño de una protección pasiva*: espesores por requisito, gobernante, masa por material, contraste Poisson–Monte Carlo y lista de lo sintético.
- 🎯 **Por qué importa:** Cada milímetro de blindaje cuesta masa, y el requisito que manda cambia con el entorno. La decisión central: ¿qué espesor y qué material cumplen la dosis y la probabilidad de perforación con la menor masa?

📘 **Dónde se aprende** (1 clase): [B85-C28 · Protección pasiva frente al ambiente espacial](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md).

### Espesor másico

- Alcance CSDA: distancia media recorrida frenándose de forma continua. Espesor másico: densidad × espesor (g/cm²).
- Cubierta: capa de regolito sobre el habitat. Espesor másico: densidad por espesor (g/cm²).

💡 **Cómo se explica en la clase [B106-C19](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md):**
- Relacionar el espesor másico con el modelo de blindaje (C14).
- Espesor masico de la cubierta: 450 g/cm2 (ver C14: fuera del rango de validez del modelo de protones)
- 🎯 **Por qué importa:** La Luna cambia las reglas: noches de dos semanas, gravedad de un sexto y un regolito que protege pero no contiene la presión. La decisión central: ¿qué recursos (energía, masa de cubierta, esfuerzo de excavación) exige un asentamiento enterrado y qué parte soporta cada elemento?

📘 **Dónde se aprende** (2 clases): [B106-C14 · Protección contra radiación](../programa/clases/B106/B106-C14-proteccion-contra-radiacion/CLASE.md); [B106-C19 · Arquitectura de asentamiento lunar conceptual](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md).

### Espesor opaco

- El espesor opaco deja pasar menos de un umbral.

💡 **Cómo se explica en la clase [B43-C07](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md):**
- Ejercicio 5. Espesor opaco para `T ≤ 10⁻³`.
- Ejercicio 12. Integrador. Elabora tu *ficha de aluminizado*: reflectancia, espesor opaco y uniformidad.
- 🎯 **Por qué importa:** Una película delgada deja pasar luz; una gruesa refleja pero no se adhiere ni es uniforme. La decisión central: ¿qué espesor es opaco, qué reflectancia da y cuánto varía de centro a borde por la geometría del evaporador?

📘 **Dónde se aprende** (1 clase): [B43-C07 · Aluminizado y recubrimientos](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md).

### Espesor óptico

- El espesor óptico `n t`.

💡 **Cómo se explica en la clase [B43-C24](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir espesor físico y óptico. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Cada reflexión sin tratar pierde luz y añade luz parásita. La decisión central: ¿cuántas capas y con qué índices y espesores se logra baja reflectancia en la banda visible?

📘 **Dónde se aprende** (1 clase): [B43-C24 · Recubrimientos antirreflectantes de capas múltiples](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md).

### Espesor óptico de aerosoles

- El espesor óptico de aerosoles (AOD) `τ` es la integral vertical de la extinción.

🎯 **Por qué importa (clase B57-C13):** Un satélite que mira un incendio, un volcán o el mar tiene que descontar la atmósfera, y los aerosoles son lo más variable. La decisión central: ¿cuánto aerosol hay y qué tipo, con qué incertidumbre, a partir de pocas longitudes de onda?

📘 **Dónde se aprende** (1 clase): [B57-C13 · Atmósfera y aerosoles](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md).

### Espín

- El espín es el momento angular interno que absorbe el orbital relativo.
- El espín `a = cJ/(GM²)`.
- El espín `s = 1/2`.

💡 **Cómo se explica en la clase [B27-C07](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md):**
- Sin espín, `r₊ = 2` (el radio de Schwarzschild).
- Con espín prógrado crece la energía liberable y el ISCO baja: `4,2330` (`a = 0,5`), `2,3209` (`0,9`), `1,2370` (`0,998`).
- ⚠️ **Error frecuente:** Olvidar el signo del espín. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El espín cambia el ISCO y, con él, cuánta energía se libera: de `5,7 %` a más de `30 %` de la masa en reposo. La decisión central: ¿dónde están el horizonte y el ISCO para un espín dado y qué eficiencia implica?

📘 **Dónde se aprende** (3 clases): [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md); [B31-C05 · Espín y momento angular](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md); [B52-C20 · Simulación de formación planetaria simplificada](../programa/clases/B52/B52-C20-simulacion-de-formacion-planetaria-simplificada/CLASE.md).

### Espiral

- Los tipos espiral, elíptica e irregular describen su forma (S1).

💡 **Cómo se explica en la clase [B01-C15](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md):**
- NASA agrupa las galaxias en espirales, elípticas e irregulares (S1).
- Por forma (espiral, elíptica): visual, pero superficial.
- 🎯 **Por qué importa:** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Espiral de Edelbaum

- La espiral de Edelbaum es la trayectoria de empuje tangencial entre órbitas circulares coplanares; su delta-v es `|V₁ − V₂|` cuando la aceleración es mucho menor que la gravedad local.

💡 **Cómo se explica en la clase [B75-C11](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md):**
- *Descripción textual:* Se integra la espiral hasta el radio de Marte; el tiempo y la aceleración dan el delta-v; se compara con Edelbaum y se convierte en fracción de propulsante.
- Ejercicio 12 · integrador. Elabora tu *comparación de la espiral de bajo empuje y la transferencia impulsiva*: tabla de tiempo, delta-v, propulsante (dos `I_sp`) y desviación con Edelbaum para tres aceleraciones, con tus conclusiones.
- 🎯 **Por qué importa:** Un motor de alta `I_sp` ahorra propulsante pero tarda mucho. La decisión central: ¿cuánto delta-v y cuánto tiempo cuesta una espiral y cuándo es válida la fórmula de Edelbaum?

📘 **Dónde se aprende** (1 clase): [B75-C11 · Propulsión de bajo empuje](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md).

### Espiral de Parker

- La espiral de Parker es la forma de la línea de campo arrastrada por el viento con el Sol rotando.

💡 **Cómo se explica en la clase [B30-C10](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md):**
- *Descripción textual:* la temperatura da la velocidad del sonido y el radio crítico; la ecuación de Parker da `v(r)`, del que salen el flujo de masa y la espiral.
- Ejercicio 12. Integrador. Elabora tu *ficha del viento de Parker*: tabla de velocidades, perfil, flujo de masa y espiral.
- 🎯 **Por qué importa:** El viento solar es el vehículo que lleva la actividad del Sol a la Tierra. La decisión central: ¿cuándo pasa el viento a supersónico y qué velocidad alcanza a 1 au?

📘 **Dónde se aprende** (1 clase): [B30-C10 · Viento solar y heliosfera](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md).

### Espiral logarítmica

- Una espiral logarítmica es una curva de ángulo de paso constante, `ln(R/R_k) = −(β − β_k) tan ψ`, donde `β` es el acimut galactocéntrico en radianes (0 hacia el Sol, creciente en el sentido de rotación) y `R_k` el radio en el acimut `β_k`.

💡 **Cómo se explica en la clase [B25-C02](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md):**
- Espiral logarítmica con nudos (esta clase y S2): se ajusta a máseres, con pocos parámetros.
- Definir ángulo de paso, espiral logarítmica, barra y brazo.
- 🎯 **Por qué importa:** Los brazos espirales son lo más llamativo de una galaxia de disco, pero la rotación diferencial debería enrollarlos hasta borrarlos en unas pocas vueltas. Entender esa paradoja es entender qué es un brazo: no un montón fijo de materia, sino un patrón.

📘 **Dónde se aprende** (1 clase): [B25-C02 · Brazos espirales y barra galáctica](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md).

### Espiral tangencial

- La espiral tangencial mantiene el empuje en la dirección de la velocidad.

💡 **Cómo se explica en la clase [B81-C04](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md):**
- El script [espiral.py](espiral.py) calcula el `Δv` coplanar y con plano, integra la ecuación promediada e integra el movimiento de dos cuerpos con empuje tangencial hasta alcanzar el semieje final (comprueba las tolerancias de la cabecera).
- 🎯 **Por qué importa:** Una espiral de bajo empuje cuesta más `Δv` que un impulso (Hohmann) pero ahorra propelente por su alto `Isp`. La decisión central: ¿cuánto `Δv` y cuánto tiempo cuesta pasar de una órbita circular a otra, y cuánto más si además hay que cambiar el plano?

📘 **Dónde se aprende** (1 clase): [B81-C04 · Trayectorias espirales de bajo empuje](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md).

### Espora

- Una espora (en el sentido de la política) es el indicador definido en 5.
- Protección planetaria: control de la contaminación hacia adelante (de la Tierra a otro cuerpo) y hacia atrás. Espora: forma latente resistente.

💡 **Cómo se explica en la clase [B56-C17](../programa/clases/B56/B56-C17-control-de-contaminacion-biologica/CLASE.md):**
- Tras ese tiempo, la forma cerrada da `12 000` esporas (`300/m²`);
- Para una muestra de `0,01 m²` a `300/m²` (media 3), la probabilidad de no hallar ninguna espora es `e^{−3} = 0,050`.
- 🎯 **Por qué importa:** Una nave que lleva microorganismos terrestres puede contaminar otro mundo y confundir una futura búsqueda de vida. La política fija límites cuantitativos.

📘 **Dónde se aprende** (2 clases): [B56-C17 · Control de contaminación biológica](../programa/clases/B56/B56-C17-control-de-contaminacion-biologica/CLASE.md); [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md).

### Esporádicos

- Los meteoros esporádicos (SPO) no pertenecen a una lluvia (S4).

💡 **Cómo se explica en la clase [B08-C18](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md):**
- La IMO (S4) pide estimar la magnitud límite en áreas definidas (dos o tres) y revisarla al menos cada hora, anotar el tipo (lluvia o esporádico) y el brillo de cada meteoro comparándolo con estrellas conocidas, tomar la hora y observar al menos una hora.
- 🎯 **Por qué importa:** Cada año, titulares prometen «cientos de estrellas fugaces por hora». Con un cielo contaminado o con el radiante bajo el horizonte, verás muy pocas.

📘 **Dónde se aprende** (1 clase): [B08-C18 · Introducción a meteoros y lluvias](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md).

### Espurio

- Un espurio es un producto no deseado `|m f_RF ± n f_OL|`.

💡 **Cómo se explica en la clase [B49-C11](../programa/clases/B49/B49-C11-mezcladores-de-frecuencia-perdida-de-conversion-y-productos-espurios/CLASE.md):**
- *Descripción textual:* la multiplicación crea suma y diferencia; los armónicos del OL crean espurios; la pérdida de conversión escala el ruido de la FI.
- Paso 4 · Espurio m = 3. `(2/π)/3 = 0,2122`.
- 🎯 **Por qué importa:** Cada producto no deseado puede caer en la banda de FI. La decisión central: ¿qué pérdida de conversión tiene el mezclador y dónde caen sus productos?

📘 **Dónde se aprende** (1 clase): [B49-C11 · Mezcladores de frecuencia: pérdida de conversión y productos espurios](../programa/clases/B49/B49-C11-mezcladores-de-frecuencia-perdida-de-conversion-y-productos-espurios/CLASE.md).

### Esquema

- Un esquema es el documento que dice qué etiquetas XML son válidas; este laboratorio no usa ninguno.
- Un esquema describe la forma de los datos.
- El esquema es la lista de campos exigidos.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C21](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md):**
- Límites: etiqueta inventada; sin esquema; sin SPICE; el valor del máximo depende de la semilla y de la versión de NumPy.
- 🎯 **Por qué importa:** Un archivo binario de una sonda planetaria son bytes sin significado: ¿cuántas filas?, ¿enteros o reales?, ¿qué orden de bytes?, ¿qué número indica «no hay dato»?, ¿qué unidad? Y para interpretarlo, hace falta saber dónde estaba la nave y hacia dónde apuntaba.

📘 **Dónde se aprende** (4 clases): [B14-C21 · Datos de misiones planetarias: PDS4, etiquetas y SPICE](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md); [B14-C31 · APIs de servicios de datos](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md); [B120-C04 · Documentación regulatoria de un sistema satelital](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md); [B129-C04 · Contribución de medidas voluntarias con control de calidad](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md).

### Esquema BTCS

- El esquema BTCS (*backward time, centered space*) evalúa el término espacial en el instante nuevo: `−r u_{i−1}^{n+1} + (1 + 2r) u_i^{n+1} − r u_{i+1}^{n+1} = u_i^n`.

💡 **Cómo se explica en la clase [B11-C14](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md):**
- Usar el esquema implícito BTCS con un sistema tridiagonal.
- 🎯 **Por qué importa:** Casi todo código de simulación de calor, fluidos o plasma en una malla regular usa diferencias finitas. Elegir el paso de tiempo equivocado no da un resultado ligeramente malo: da un resultado que explota.

📘 **Dónde se aprende** (1 clase): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md).

### Esquema de diferencias centrales

- El esquema de diferencias centrales aproxima `y″(x_i) ≈ (y_{i+1} − 2y_i + y_{i−1})/h²`, con error `O(h²)` (S1, §3.4).

🎯 **Por qué importa (clase B11-C12):** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Esquema de Horn

- El esquema de Horn calcula derivadas con una ventana de 3 × 3 ponderada.

💡 **Cómo se explica en la clase [B53-C20](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md):**
- Calcular la pendiente de un MDE con el esquema de Horn.
- 🎯 **Por qué importa:** Un derivado sin verificar propaga errores a la decisión. La decisión central: ¿qué parte del terreno cumple un criterio de pendiente y existe un camino que lo respete?

📘 **Dónde se aprende** (1 clase): [B53-C20 · Proyecto SIG de terreno extraterrestre](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md).

### Esquema de Horner

- El esquema de Horner reescribe `a₀ + a₁x + a₂x² + a₃x³` como `a₀ + x(a₁ + x(a₂ + x a₃))`, lo que evita calcular potencias altas por separado.

💡 **Cómo se explica en la clase [B04-C01](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md):**
- El esquema de Horner es más económico y estable con coeficientes de órdenes de magnitud muy distintos.
- Evaluar un polinomio con el esquema de Horner y comprobar el resultado con la forma directa.
- 🎯 **Por qué importa:** Cuando un observatorio publica dónde está inclinado el eje de la Tierra, no da un solo número: da una *fórmula* para cada fecha, porque ese eje se mueve lentamente. Esa fórmula es un polinomio.

📘 **Dónde se aprende** (1 clase): [B04-C01 · Polinomios y factorización](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md).

### Esquema de salto de rana

- El esquema de salto de rana avanza en tres niveles de tiempo.

💡 **Cómo se explica en la clase [B30-C09](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md):**
- Simular el pulso con un esquema de salto de rana y la condición CFL.
- 🎯 **Por qué importa:** La velocidad de Alfvén fija cuánto tarda una perturbación en recorrer un lazo coronal o una línea de campo del viento solar. La decisión central: ¿con qué velocidad viaja una perturbación magnética y cómo cambia el tiempo de viaje en un medio estratificado?

📘 **Dónde se aprende** (1 clase): [B30-C09 · Magnetohidrodinámica](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md).

### Esquema FTCS

- El esquema FTCS (*forward time, centered space*) es `u_i^{n+1} = u_i^n + r (u_{i+1}^n − 2u_i^n + u_{i−1}^n)`, con `r = α Δt/Δx²`.

💡 **Cómo se explica en la clase [B11-C14](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md):**
- *Descripción textual:* con FTCS, cada nodo se actualiza con sus vecinos; si `r ≤ 1/2` el esquema es estable y suaviza, y si no, las oscilaciones de nodo a nodo crecen;
- Con el esquema FTCS y `r = 0,4`, una malla de 10, 20 y 40 intervalos da `0,670709`, `0,673056` y `0,673634`: el error baja a la cuarta parte cada vez que se duplica la malla.
- 🎯 **Por qué importa:** Casi todo código de simulación de calor, fluidos o plasma en una malla regular usa diferencias finitas. Elegir el paso de tiempo equivocado no da un resultado ligeramente malo: da un resultado que explota.

📘 **Dónde se aprende** (1 clase): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md).

### Esquina

- El centro del píxel es su punto medio; la esquina su punto superior izquierdo.
- Característica local: punto distintivo de una imagen y su entorno. Esquina: punto donde la intensidad varía en dos direcciones.

💡 **Cómo se explica en la clase [B14-C26](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md):**
- La geotransformación del ejemplo: origen en la esquina superior izquierda `(10,0°; 40,0°)` y píxel de 0,001° con el norte arriba.
- Con la convención «el píxel `(fila, col)` cubre desde `lon0 + col·dx` hasta `lon0 + (col+1)·dx` y desde `lat0 − (fila+1)·dy` hasta `lat0 − fila·dy`», el centro del píxel `(0, 0)` es `(10,0005°; 39,9995°)` y la esquina `(10,0°; 40,0°)` cae en el píxel `(0, 0)`.
- ⚠️ **Error frecuente:** Confundir esquina y centro del píxel. Se corrige con los ejercicios 6 y 10.
- 🎯 **Por qué importa:** Una escena de satélite pesa cientos de megabytes y tú necesitas un recuadro de 100 × 120 píxeles. Si el formato obliga a leer todo el archivo, gastas tiempo y ancho de banda.

📘 **Dónde se aprende** (2 clases): [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md); [B99-C02 · Detección y descriptores de características](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md).

### Estabilidad

- La masa formular es la masa molar de la fórmula; la estabilidad de un hielo, en esta clase, es el intervalo de presiones y temperaturas donde no sublima (C11).
- La estabilidad (no explotar) es distinta de la precisión (parecerse a la solución).
- La consistencia es que el error de truncamiento tienda a cero; la estabilidad, que los errores no crezcan.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Sólo toma dos cifras (la temperatura de 176 K y la clasificación de las especies) para ejercitar el cálculo de energías y de estabilidad.
- Ejercicio 6. Calcula la presión mínima de estabilidad del hielo de CO₂ a 170 K con `ΔH_sub = 26,1 kJ/mol`.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).

📘 **Dónde se aprende** (8 clases): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md); [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md); [B13-C23 · Estabilidad y deriva temporal de instrumentos](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md); [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md); [B84-C24 · Factores de seguridad y márgenes estructurales](../programa/clases/B84/B84-C24-factores-de-seguridad-y-margenes-estructurales/CLASE.md) y 2 más.

### Estabilidad asintótica global

- La estabilidad asintótica global significa que toda trayectoria tiende al equilibrio.

🎯 **Por qué importa (clase B16-C17):** Cuando un satélite se separa del cohete puede salir girando de forma desordenada («volteando»).

📘 **Dónde se aprende** (1 clase): [B16-C17 · Control no lineal](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md).

### Estabilidad de frecuencia

- La estabilidad de frecuencia describe cómo fluctúa `y` en el tiempo.

🎯 **Por qué importa (clase B13-C07):** Dos relojes pueden tener la misma desviación de frecuencia media y comportarse de forma muy distinta: uno oscila alrededor de su valor y otro se aleja de él con el tiempo. La desviación típica ordinaria no sirve para describirlo, porque en un reloj con deriva no converge.

📘 **Dónde se aprende** (1 clase): [B13-C07 · Relojes atómicos y frecuencia](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md).

### Estabilidad estática

- La estabilidad estática exige `Cm_α < 0`: un aumento de `α` genera un par que lo reduce.

💡 **Cómo se explica en la clase [B77-C17](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md):**
- Definir estabilidad estática por el signo de `Cm_α`.
- ⚠️ **Error frecuente:** Confundir estabilidad estática con ausencia de oscilación. Se corrige con 8.3.
- 🎯 **Por qué importa:** Una cápsula inestable no entra con el escudo hacia delante. La decisión central: ¿qué pendiente de momento da una oscilación acotada y cuánto tarda en divergir una inestable?

📘 **Dónde se aprende** (1 clase): [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md).

### Estabilidad lineal

- La estabilidad lineal no garantiza la estabilidad no lineal.

💡 **Cómo se explica en la clase [B73-C04](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de estabilidad de cinco puntos y tres sistemas*: tabla de autovalores, tiempos de crecimiento, indicador de Routh, validación por diferencias finitas y por integración no lineal, y lista de límites.
- ⚠️ **Error frecuente:** Concluir estabilidad total de un centro×centro lineal. Se corrige con 8.5.
- 🎯 **Por qué importa:** Que un punto sea de equilibrio no dice si una nave se queda o se va. Los autovalores dicen cuánto tiempo tienes antes de corregir la posición y si un grupo de asteroides puede quedarse en L4.

📘 **Dónde se aprende** (1 clase): [B73-C04 · Estabilidad local de Lagrange](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md).

### Estabilidad numérica

- La estabilidad numérica es la capacidad de un cálculo de no perder cifras.

💡 **Cómo se explica en la clase [B07-C17](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md):**
- ⚠️ **Error frecuente:** Ignorar la estabilidad numérica. Se corrige con la sección 8.6 y el ejercicio 8.
- 🎯 **Por qué importa:** Una función matemática puede dar el resultado correcto en el único caso que probaste y estar mal en los demás. Y es fácil escribir una prueba que no puede fallar: la que compara la función contra sí misma o contra un caso donde el error se esconde.

📘 **Dónde se aprende** (1 clase): [B07-C17 · Pruebas de funciones matemáticas](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md).

### Estabilidad progrado y retrógrada

- La estabilidad progrado y retrógrada se mide por el semieje máximo de una órbita circular que no escapa.

🎯 **Por qué importa (clase B73-C18):** Los satélites irregulares son capturas: están lejos, en órbitas que ningún proceso de formación local explica. Ocupan una fracción de la esfera de Hill que depende del sentido de giro.

📘 **Dónde se aprende** (1 clase): [B73-C18 · Satélites irregulares](../programa/clases/B73/B73-C18-satelites-irregulares/CLASE.md).

### Estabilización

- La estabilización de imagen o un trípode reducen el temblor.
- La estabilización se da cuando `|dT/dt|` cae bajo el criterio.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- NASA recomienda, para empezar, entre 7×35 y 10×50: con más aumento el campo es más estrecho, pesan más y se sacuden, salvo con estabilización o trípode (S2, S3).
- Trípode con adaptador estabiliza y permite 10× o más, a costa de comodidad.
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?

📘 **Dónde se aprende** (2 clases): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md); [B85-C19 · Ensayos de vacío térmico](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md).

### Estable

- Un ordenamiento es estable si los elementos con la misma clave conservan su orden relativo (S2).
- El método es estable para un `z` si `|R(z)| ≤ 1`; la región de estabilidad es el conjunto de `z` donde ocurre.
- Un LTI es estable (en el sentido que usaremos) si su respuesta al impulso tiende a cero.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- Es estable si, en un empate, se toma primero el elemento de la mitad izquierda (como hace el laboratorio).
- Explicar el significado de «estable» y verificarlo.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.

📘 **Dónde se aprende** (6 clases): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md); [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B54-C19 · Modelos climáticos planetarios](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md); [B73-C06 · Variedades invariantes](../programa/clases/B73/B73-C06-variedades-invariantes/CLASE.md); [B77-C21 · Centro de presión y margen estático](../programa/clases/B77/B77-C21-centro-de-presion-y-margen-estatico/CLASE.md).

### Estación

- Pasada: ventana de visibilidad de un satélite. Estación: antena que atiende una pasada a la vez.

💡 **Cómo se explica en la clase [B96-C17](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md):**
- El capítulo de la NASA sobre sistemas terrestres (S1) describe redes de estaciones, como la Near Space Network y proveedores comerciales, y servicios de planificación y programación; también indica que la licencia de bandas tarda meses.
- Se maximiza `Σ wᵢ` sobre las pasadas atendidas con la restricción de no solape por estación.
- ⚠️ **Error frecuente:** Asignar sin comprobar solapes. Verifica cada estación (8.2)
- 🎯 **Por qué importa:** Dos pasadas que se solapan en la misma antena obligan a elegir; sin coordinación se pierde la más valiosa. La decisión central: ¿qué pasadas se atienden y desde qué estación para maximizar el valor sin solapes?

📘 **Dónde se aprende** (1 clase): [B96-C17 · Coordinación de múltiples estaciones](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md).

### Estación de eclipses

- Una estación de eclipses es el período en que la órbita de la Luna cruza el plano de la órbita de la Tierra; ocurre dos veces al año (S3).

💡 **Cómo se explica en la clase [B08-C09](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md):**
- Para las lunas llenas, el criterio de umbra (separación con el punto antisolar menor que ≈ 0,9°–1,0°) da dos candidatas en 2025: 14 de marzo (0,56°) y 7 de septiembre (0,72°); la confirmación con la lista de eclipses lunares de la NASA no se consultó en esta clase.
- Ejercicio 4. Con la inclinación de 5,145° (S4) y el límite de ≈ 1,5° para el eclipse solar, explica por qué hay eclipses solo en estaciones.
- 🎯 **Por qué importa:** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?

📘 **Dónde se aprende** (1 clase): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md).

### Estación de mantenimiento

- Una estación de mantenimiento permite diagnosticar y reparar equipos.

💡 **Cómo se explica en la clase [B109-C11](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md):**
- La estación de mantenimiento ocupa `3,28 m³` en `1,37 m²`, es decir, `2,394 m` de altura: coincide con la altura estándar `2,4 m` (tolerancia del `0,5 %`).
- Ejercicio 6 · autónomo. Altura implícita de la estación de mantenimiento.
- 🎯 **Por qué importa:** Un equipo que no se puede abrir o extraer no se puede reparar, y en un hábitat sin taller externo eso es un riesgo de misión. La decisión central: ¿hay área, paso y holgura para trabajar y mantener cada equipo, y dónde falta?

📘 **Dónde se aprende** (1 clase): [B109-C11 · Diseño de espacios de trabajo, mantenimiento y laboratorio](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md).

### Estación de seguimiento

- Estación de seguimiento: antena, receptor y software que rastrean la nave.

💡 **Cómo se explica en la clase [B96-C05](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md):**
- python programa/clases/B96/B96-C05-estaciones-de-seguimiento/pasada_con_doppler.py
- 🎯 **Por qué importa:** Para que una antena apunte y un receptor enganche, la estación debe conocer de antemano el azimut, la elevación y el corrimiento de frecuencia. La decisión central: ¿hacia dónde apuntar y qué frecuencia esperar en cada instante?

📘 **Dónde se aprende** (1 clase): [B96-C05 · Estaciones de seguimiento](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md).

### Estación de trabajo

- Una estación de trabajo es el lugar donde se hace una tarea.

🎯 **Por qué importa (clase B109-C11):** Un equipo que no se puede abrir o extraer no se puede reparar, y en un hábitat sin taller externo eso es un riesgo de misión. La decisión central: ¿hay área, paso y holgura para trabajar y mantener cada equipo, y dónde falta?

📘 **Dónde se aprende** (1 clase): [B109-C11 · Diseño de espacios de trabajo, mantenimiento y laboratorio](../programa/clases/B109/B109-C11-diseno-de-espacios-de-trabajo-mantenimiento-y-laboratorio/CLASE.md).

### Estacionaria

- La respuesta transitoria es la parte que se extingue con el tiempo; la estacionaria es la que queda cuando el transitorio desapareció.

💡 **Cómo se explica en la clase [B16-C04](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md):**
- Para nuestro estudio, esas dos fases son exactamente la respuesta transitoria (cómo llega) y la respuesta estacionaria (dónde se queda).
- Distinguir la parte transitoria de la estacionaria de una respuesta.
- 🎯 **Por qué importa:** Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación.

📘 **Dónde se aprende** (1 clase): [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md).

### Estadio

- La circunferencia es la longitud del contorno de un círculo; el estadio es una unidad antigua de longitud cuyo valor exacto se discute.

💡 **Cómo se explica en la clase [B02-C03](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md):**
- La distancia cenital en Alejandría fue de 7°12′ (7,2°, o 1/50 de círculo); con unos 5 000 estadios entre las ciudades la circunferencia sale `5 000 × 50 = 250 000` estadios, la cifra que se le atribuye (S2).
- MacTutor recoge además la tesis de Rawlins de que esa medición angular fue la única que Eratóstenes hizo por sí mismo, con un error de unos 16′ (S2); los 5 000 estadios aparecen en la fuente solo de forma indirecta, en el título de una referencia.
- ⚠️ **Error frecuente:** Decir que acertó con un error de 1 %. Depende del estadio.
- 🎯 **Por qué importa:** Un modelo geométrico responde a «¿qué figura reproduce estos movimientos?». Es una forma nueva de preguntar frente a la regla puramente numérica.

📘 **Dónde se aprende** (1 clase): [B02-C03 · Astronomía griega y helenística](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md).

### Estadística

- Una estadística es una función de los datos de la muestra; una estimación es la operación de asignar valores numéricos a los parámetros a partir de una muestra, un estimador es la estadística usada para ello y una estimación (resultado) es su valor para una muestra concreta (S1, C.2.23–C.2.26).

🎯 **Por qué importa (clase B12-C07):** Una misión no «conoce» la tasa de impactos ni el ruido de su sensor: los estima a partir de unas decenas de datos. Un estimador mal elegido, o mal interpretado, da parámetros sesgados o con una confianza injustificada.

📘 **Dónde se aprende** (1 clase): [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md).

### Estadística de Cash

- La estadística de Cash `C = 2Σ(μ − n ln μ)`.

💡 **Cómo se explica en la clase [B27-C22](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md):**
- Con pocas cuentas, el `χ²` con varianza igual a las observadas da un espectro sistemáticamente más blando (`Γ` mayor) y más disperso; la estadística de Cash casi no tiene sesgo.
- Escribir la estadística de Cash y el `χ²` con varianza igual a las cuentas.
- 🎯 **Por qué importa:** Ajustar un espectro «de fotones» directamente a las cuentas da resultados engañosos; hay que plegar el modelo con la respuesta y usar la estadística correcta para conteos pequeños. La decisión central: ¿qué parámetros recupera cada estadística y con qué sesgo cuando las cuentas son pocas?

📘 **Dónde se aprende** (1 clase): [B27-C22 · Análisis espectral de rayos X y gamma: ajuste con respuesta instrumental](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md).

### Estadística de Poisson

- La estadística de Poisson: media igual a varianza.

💡 **Cómo se explica en la clase [B47-C03](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md):**
- Simular la estadística de Poisson con semilla fija.
- 🎯 **Por qué importa:** En el ultravioleta cada fotón es valioso: las tasas son bajas y el ruido es de Poisson. La decisión central: ¿cuánto hay que exponer para llegar a una relación señal/ruido de 10?

📘 **Dónde se aprende** (1 clase): [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md).

### Estadísticas zonales

- Las estadísticas zonales resumen una capa por zona.

💡 **Cómo se explica en la clase [B57-C19](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de análisis de riesgo*: la tabla de pesos y consistencia, el solape entre métodos, la sensibilidad a pesos y las estadísticas zonales.
- 🎯 **Por qué importa:** Los mapas de riesgo orientan decisiones y presupuestos, pero dependen de supuestos de ponderación que suelen quedar ocultos. La decisión central: ¿cómo combino capas y cuánto cambian las zonas prioritarias si cambio los pesos?

📘 **Dónde se aprende** (1 clase): [B57-C19 · SIG y análisis de riesgo](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md).

### Estadístico

- El perfilado determinista instrumenta cada evento de llamada; el estadístico muestrea.

💡 **Cómo se explica en la clase [B18-C04](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md):**
- El perfilado estadístico perturba menos y sirve para programas largos, pero da solo proporciones aproximadas y no cuenta llamadas (S1).
- El estadístico muestrea periódicamente el puntero de instrucciones y deduce dónde se gasta el tiempo; añade menos sobrecoste, pero da solo indicaciones relativas.
- 🎯 **Por qué importa:** Casi todo programa científico tiene un cuello de botella que el autor no sospecha. Optimizar a ojo suele mejorar lo que no importa.

📘 **Dónde se aprende** (1 clase): [B18-C04 · Perfilado de rendimiento](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md).

### Estadístico de chequeo

- Un estadístico de chequeo `T(y)` resume una característica de los datos que importa para la pregunta (aquí, el índice de dispersión `T = varianza/media`).

💡 **Cómo se explica en la clase [B19-C06](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md):**
- Límite de la analogía: el chequeo es siempre *relativo a un estadístico*.
- Diseñar un estadístico de chequeo y calcular un valor p predictivo posterior por simulación.
- ⚠️ **Error frecuente:** Elegir el estadístico después de ver el resultado. Sesga el chequeo: se declara antes.
- 🎯 **Por qué importa:** El contador de partículas lleva 12 horas midiendo. Con la posterior de la tasa `λ`, la pregunta práctica es: ¿cuántos eventos esperar en la hora 13, y qué tan sorprendente sería ver 8?

📘 **Dónde se aprende** (1 clase): [B19-C06 · Distribución predictiva posterior](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md).

### Estadístico de detección

- El estadístico de detección `J = |r|²/σ²` sigue una chi-cuadrado con `n − 3` grados de libertad sin falla.

🎯 **Por qué importa (clase B80-C05):** B88-C12 trata la detección y recuperación de fallas en general, no el arbitraje de las mediciones que alimentan la navegación. La decisión central: ¿cómo sabe el sistema que un sensor miente, y cuál es, sin una referencia externa?

📘 **Dónde se aprende** (1 clase): [B80-C05 · Redundancia de sensores y arbitraje de mediciones](../programa/clases/B80/B80-C05-redundancia-de-sensores-y-arbitraje-de-mediciones/CLASE.md).

### Estadístico de Grubbs

- El estadístico de Grubbs es `G = máx|Yᵢ − Ȳ| / s` (S2).

💡 **Cómo se explica en la clase [B12-C19](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md):**
- Calcular el estadístico de Grubbs y compararlo con su valor crítico.
- 🎯 **Por qué importa:** Un dato aberrante puede ser un error del instrumento, una pérdida de sincronía o el primer indicio de un fenómeno real. Eliminarlo sin criterio esconde información; conservarlo sin revisar contamina el resultado.

📘 **Dónde se aprende** (1 clase): [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md).

### Estadístico de habilidad verdadera

- El estadístico de habilidad verdadera `TSS = POD − POFD` no depende de la tasa base.

🎯 **Por qué importa (clase B12-C24):** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.

📘 **Dónde se aprende** (1 clase): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md).

### Estadístico de Mann–Whitney

- El estadístico de Mann–Whitney es la probabilidad de que una puntuación de suceso supere a una de no suceso.

🎯 **Por qué importa (clase B33-C14):** La verificación decide si una alerta merece confianza. La decisión central: ¿cómo resumir la capacidad de discriminar de un pronóstico?

📘 **Dónde se aprende** (1 clase): [B33-C14 · Verificación de alertas con tablas de contingencia](../programa/clases/B33/B33-C14-verificacion-de-alertas-con-tablas-de-contingencia/CLASE.md).

### Estadístico de prueba

- Un estadístico de prueba es una función de los datos con distribución conocida bajo `H₀`; aquí `z = (H₂ − H₁)/√(s₁² + s₂²)`.

💡 **Cómo se explica en la clase [B12-C09](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md):**
- Con un efecto real `δ = 1 m`, `σ = 3 m` y `n = 25`, el estadístico se desplaza `δ√n/σ = 1,667` errores típicos y la potencia de la prueba bilateral al 5 % es `0,385` (simulada `0,387`): la prueba pasa por alto el efecto el 61 % de las veces.
- 🎯 **Por qué importa:** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.

📘 **Dónde se aprende** (1 clase): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md).

### Estadístico R̂

- El estadístico `R̂` (Gelman–Rubin) compara la varianza entre cadenas con la de dentro de cada una: si todas las cadenas muestrean la misma distribución, `R̂ ≈ 1`; si están en regiones distintas, `R̂ > 1`.

🎯 **Por qué importa (clase B12-C23):** Un análisis MCMC cuya cadena no convergió da intervalos falsos con apariencia de precisión; y uno que no se puede repetir es irrevisable. En una misión, un parámetro estimado con cadenas defectuosas puede determinar una maniobra o un diagnóstico de salud de un instrumento.

📘 **Dónde se aprende** (1 clase): [B12-C23 · Diagnóstico de convergencia y reproducibilidad de cadenas MCMC](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md).

### Estado

- El estado es el conjunto de esos valores.
- El estado `x` es el menor conjunto de variables que, junto con la entrada futura, determina todo el futuro del sistema.
- El estado es el par posición–velocidad en un instante.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C02](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md):**
- A["EDO de orden m"] --> B["Estado inicial:<br/>y y sus m−1 derivadas<br/>en t₀"]
- *Descripción textual:* para una EDO de orden `m` se fija el estado inicial; si la función `f` es lipschitziana la solución es única; luego se pregunta cuánto crece una diferencia inicial, lo que limita el horizonte útil de predicción.
- 🎯 **Por qué importa:** Una nave no sigue «la» solución de las ecuaciones del movimiento: sigue la que corresponde a *su* posición y velocidad en el instante en que se midieron. Saber cuántos datos exige la ecuación, cuándo garantizan una única trayectoria y cuánto se amplifica su error es la base de toda predicción de trayectoria.

📘 **Dónde se aprende** (6 clases): [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md); [B71-C10 · Semieje mayor y excentricidad](../programa/clases/B71/B71-C10-semieje-mayor-y-excentricidad/CLASE.md); [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md); [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md).

### Estado aumentado

- El sesgo (*bias*) `b` es un offset de la medida del giróscopo; se modela como un estado constante `ḃ = 0` (estado aumentado).

🎯 **Por qué importa (clase B16-C14):** Los sensores miden poco y mal: un rastreador de estrellas da la orientación, pero a baja frecuencia y con ruido; un giróscopo da la velocidad con un sesgo que deriva. El controlador necesita el estado completo (C15) y limpio.

📘 **Dónde se aprende** (1 clase): [B16-C14 · Observadores de estados](../programa/clases/B16/B16-C14-observadores-de-estados/CLASE.md).

### Estado de carga

- El estado de carga (SOC) es la fracción restante.

🎯 **Por qué importa (clase B86-C05):** Una batería de órbita baja hace unos `5400` ciclos al año. Dimensionarla por la energía de un solo eclipse sin mirar la profundidad de descarga la agota mucho antes del fin de la misión.

📘 **Dónde se aprende** (1 clase): [B86-C05 · Baterías de ion-litio](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md).

### Estado de error

- El estado de error es `(δθ, Δb)` con `A_true = (I − [δθ×]) Â`.

💡 **Cómo se explica en la clase [B87-C10](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md):**
- Plantear el estado de error `x = (δθ, Δb)` y su dinámica `δθ̇ = −ω̂×δθ − Δb − η_v`.
- El script [mekf.py](mekf.py) simula la actitud verdadera, el giroscopio con ARW, RRW y sesgo, y los vectores con ruido; ejecuta el MEKF de 6 estados, el giroscopio solo y el SVD por época; y calcula el NEES (comprueba error del giroscopio solo `> 10×` el del filtro, filtro mejor que el SVD, error de sesgo `< 30 %` y NEES razonable).
- ⚠️ **Error frecuente:** Filtrar el cuaternión como si fuera un vector de 4 estados. Filtra el error de 3 componentes (8.1)
- 🎯 **Por qué importa:** Un giroscopio sin corregir se desvía decenas de grados en minutos; un vector solo da `~1°` por época. La decisión central: ¿cómo se combinan para obtener una actitud mejor que cada uno, y cómo se sabe que el filtro es honesto?

📘 **Dónde se aprende** (1 clase): [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md).

### Estado de lanzamiento

- El Estado de lanzamiento es el que lanza, hace lanzar o cede territorio o instalación.
- El Estado de lanzamiento es el que lanza o hace lanzar.
- El Estado de lanzamiento y el Estado de registro pueden ser distintos.

💡 **Cómo se explica en la clase [B118-C18](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md):**
- II (el Estado de lanzamiento registra el objeto).
- II: responsabilidad absoluta del Estado de lanzamiento por el daño en la superficie.
- ⚠️ **Error frecuente:** Confundir Estado de lanzamiento y de registro. Se corrige con el vocabulario y el ejercicio 6.
- 🎯 **Por qué importa:** Con decenas de miles de objetos, comparar todos los pares es costoso; un buen cribado descarta de entrada los pares imposibles sin perder ninguno posible. Y cuando algo sale mal, los tratados determinan responsabilidad y jurisdicción.

📘 **Dónde se aprende** (3 clases): [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md); [B119-C04 · Convenio de Registro](../programa/clases/B119/B119-C04-convenio-de-registro/CLASE.md); [B119-C33 · Matriz comparativa de obligaciones jurídicas por actor](../programa/clases/B119/B119-C33-matriz-comparativa-de-obligaciones-juridicas-por-actor/CLASE.md).
