# Términos · 0-9

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · **0-9**

### 16QAM

- 8PSK, 8 (3 bits); 16QAM, 16 amplitudes y fases (4 bits).

💡 **Cómo se explica en la clase [B89-C08](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md):**
- BPSK y QPSK: `Q(√(2γ))`, con `γ = Eb/N0`. 8PSK: `erfc(√(3γ) sin(π/8))/3`. 16QAM: `(3/8) erfc(√(0,4γ))` (aproximaciones con Gray, relaciones estándar no consultadas).
- A 8 dB: BPSK `1,91e-04`; 8PSK `6,18e-03`; 16QAM `9,25e-03`.
- 🎯 **Por qué importa:** La elección de la modulación fija el `Eb/N0` requerido en el presupuesto de enlace y el ancho de banda ocupado; es la base de la codificación y la sincronización siguientes. La decisión central: ¿qué modulación da la tasa que necesito con el `Eb/N0` que mi enlace puede ofrecer?

📘 **Dónde se aprende** (1 clase): [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md).

### 1oo1

- 1oo1, 1oo2, 2oo2 y 2oo3 indican cuántos canales hacen falta para que la función exista: `k` de `n`.

💡 **Cómo se explica en la clase [B97-C17](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md):**
- 1oo1: `0,09516`; 1oo2 (fallan los dos): `p² = 0,009056`; 2oo2 (falla cualquiera): `0,18127`; 2oo3 (fallan dos o más): `0,025444`.
- La mejora de 1oo2 frente a 1oo1 baja de `10,5` a `7,4`.
- 🎯 **Por qué importa:** Duplicar un canal parece bajar la probabilidad de falla al cuadrado; pero si una causa afecta a ambos, la mejora real es mucho menor. Calcularlo evita sobreestimar la seguridad de una arquitectura redundante.

📘 **Dónde se aprende** (1 clase): [B97-C17 · Seguridad funcional robótica](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md).

### 1oo2

- 1oo1, 1oo2, 2oo2 y 2oo3 indican cuántos canales hacen falta para que la función exista: `k` de `n`.

💡 **Cómo se explica en la clase [B97-C17](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md):**
- 1oo1: `0,09516`; 1oo2 (fallan los dos): `p² = 0,009056`; 2oo2 (falla cualquiera): `0,18127`; 2oo3 (fallan dos o más): `0,025444`.
- Con `β = 0,05`, la parte común es `β p = 0,004758` y actúa como un piso. 1oo2 pasa de `0,009056` a `0,012892`; 2oo3, de `0,025444` a `0,027690`.
- 🎯 **Por qué importa:** Duplicar un canal parece bajar la probabilidad de falla al cuadrado; pero si una causa afecta a ambos, la mejora real es mucho menor. Calcularlo evita sobreestimar la seguridad de una arquitectura redundante.

📘 **Dónde se aprende** (1 clase): [B97-C17 · Seguridad funcional robótica](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md).

### 1/V_max

- El volumen máximo `V_max` es el de la esfera dentro de la cual una galaxia dada todavía se detectaría, y el estimador `1/V_max` pesa cada galaxia por su inverso.

💡 **Cómo se explica en la clase [B25-C19](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md):**
- Con `V_max = (4π/3) d_max³` (acotado por la esfera de la simulación), el peso `1/V_max` compensa que las galaxias débiles se vean en menos volumen.
- Con las galaxias de `M < −18` (completas hasta 100 Mpc) la media de la población es `−20,055`; la media sin pesos es `−21,27` (sesgo de `1,2` mag); con `1/V_max`, `−20,03 ± 0,02`.
- ⚠️ **Error frecuente:** Aplicar `1/V_max` con densidad no uniforme. Se corrige en 8.5.
- 🎯 **Por qué importa:** Un catálogo limitado por flujo ve las galaxias brillantes a gran distancia y casi solo ellas; si se promedian sus luminosidades sin cuidado, el resultado depende de la distancia del catálogo y no de las galaxias. Saber qué falta es tan importante como saber qué hay.

📘 **Dónde se aprende** (1 clase): [B25-C19 · Catálogos y sesgos de selección](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md).

### 2 for x in lista if x > 0]. Un

- Una comprensión de lista construye una lista nueva a partir de otra: `[x2 for x in lista if x > 0]`. Un alias es otro nombre para el mismo objeto; una copia es un objeto nuevo.

💡 **Cómo se explica en la clase [B07-C07](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md):**
- Una lista es una fila de cajones numerados; un diccionario es un fichero con etiquetas (claves) para buscar rápido; una tupla es una fila de cajones sellados; un conjunto es una bolsa donde cada cosa entra una vez.
- L["lista PLANETAS<br/>posiciones 0..7"] --> D0["0 → dict Mercurio"]
- ⚠️ **Error frecuente:** `lista = lista.sort()`. Deja `None`.
- 🎯 **Por qué importa:** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.

📘 **Dónde se aprende** (1 clase): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md).

### 2-de-3

- Redundancia fría con conmutador de confiabilidad `Rs`: `e^{−x}(1 + Rs·x)`. 2-de-3 con votador perfecto: `3R² − 2R³`.

💡 **Cómo se explica en la clase [B83-C23](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md):**
- Con `x = 0,3504`: simple `e^{−x} = 70,44 %`; paralelo activo `2R − R² = 91,26 %`; fría `e^{−x}(1 + 0,98x) = 94,63 %` (supera al activo porque la unidad de repuesto no envejece mientras espera, a menos que el conmutador falle); 2-de-3 `3R² − 2R³ = 78,95 %`.
- Para una unidad sintética de 8000 FIT en una misión de 5 años (`x = λt = 0,3504`), la confiabilidad es 70,44 % sin redundancia, 91,26 % con paralelo activo, 94,63 % con redundancia fría (conmutador de 0,98) y 78,95 % con 2-de-3.
- 🎯 **Por qué importa:** Duplicar todo es imposible por masa y a veces contraproducente; no duplicar nada deja una misión frágil. La decisión central: ¿qué unidades duplicar, con qué esquema y cuánta confiabilidad compra cada kilogramo?

📘 **Dónde se aprende** (1 clase): [B83-C23 · Redundancia y tolerancia a fallos de misión](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md).

### 2DRMS

- El 2DRMS es `2√(σ_x²+σ_y²)` y contiene entre 95 y 98 %.

💡 **Cómo se explica en la clase [B74-C19](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *tabla de métricas con su incertidumbre*: RMS, CEP, SEP, P95 y 2DRMS para una distribución dada, variabilidad con 50 muestras e intervalo bootstrap, rotulando lo sintético.
- 2DRMS = 6.462 m contiene el 96.53 % de los puntos horizontales
- 🎯 **Por qué importa:** Dos informes pueden decir «3 m» y referirse a cosas distintas (RMS, 50 %, 95 %). La decisión central: ¿qué métrica comunica el riesgo que importa, con qué probabilidad y con qué incertidumbre muestral?

📘 **Dónde se aprende** (1 clase): [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md).

### 2oo2

- 1oo1, 1oo2, 2oo2 y 2oo3 indican cuántos canales hacen falta para que la función exista: `k` de `n`.

💡 **Cómo se explica en la clase [B97-C17](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md):**
- 1oo1: `0,09516`; 1oo2 (fallan los dos): `p² = 0,009056`; 2oo2 (falla cualquiera): `0,18127`; 2oo3 (fallan dos o más): `0,025444`.
- Calcular la probabilidad de falla de arquitecturas 1oo1, 1oo2, 2oo2 y 2oo3.
- ⚠️ **Error frecuente:** Confundir 2oo2 con redundancia de disponibilidad. Se necesitan ambos (ejercicio 3)
- 🎯 **Por qué importa:** Duplicar un canal parece bajar la probabilidad de falla al cuadrado; pero si una causa afecta a ambos, la mejora real es mucho menor. Calcularlo evita sobreestimar la seguridad de una arquitectura redundante.

📘 **Dónde se aprende** (1 clase): [B97-C17 · Seguridad funcional robótica](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md).

### 2oo3

- 1oo1, 1oo2, 2oo2 y 2oo3 indican cuántos canales hacen falta para que la función exista: `k` de `n`.

💡 **Cómo se explica en la clase [B97-C17](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md):**
- 1oo1: `0,09516`; 1oo2 (fallan los dos): `p² = 0,009056`; 2oo2 (falla cualquiera): `0,18127`; 2oo3 (fallan dos o más): `0,025444`.
- Con `β = 0,05`, la parte común es `β p = 0,004758` y actúa como un piso. 1oo2 pasa de `0,009056` a `0,012892`; 2oo3, de `0,025444` a `0,027690`.
- 🎯 **Por qué importa:** Duplicar un canal parece bajar la probabilidad de falla al cuadrado; pero si una causa afecta a ambos, la mejora real es mucho menor. Calcularlo evita sobreestimar la seguridad de una arquitectura redundante.

📘 **Dónde se aprende** (1 clase): [B97-C17 · Seguridad funcional robótica](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md).

### 8

- Una región conectada es un conjunto de píxeles de objeto unidos por vecindad; la conectividad 4 une píxeles que comparten un lado, la 8 también los que comparten una esquina (S1 describe cómo `scipy.ndimage.label` usa por defecto la cruz de 4 vecinos y cómo pedir 8).

🎯 **Por qué importa (clase B15-C13):** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.

📘 **Dónde se aprende** (1 clase): [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md).

### 8PSK

- QPSK, 4 (2 bits); 8PSK, 8 (3 bits);

💡 **Cómo se explica en la clase [B89-C08](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md):**
- BPSK y QPSK: `Q(√(2γ))`, con `γ = Eb/N0`. 8PSK: `erfc(√(3γ) sin(π/8))/3`. 16QAM: `(3/8) erfc(√(0,4γ))` (aproximaciones con Gray, relaciones estándar no consultadas).
- A 8 dB: BPSK `1,91e-04`; 8PSK `6,18e-03`; 16QAM `9,25e-03`.
- 🎯 **Por qué importa:** La elección de la modulación fija el `Eb/N0` requerido en el presupuesto de enlace y el ancho de banda ocupado; es la base de la codificación y la sincronización siguientes. La decisión central: ¿qué modulación da la tasa que necesito con el `Eb/N0` que mi enlace puede ofrecer?

📘 **Dónde se aprende** (1 clase): [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md).

### Β crítico

- El β crítico `β* = asin(R/(R+h))` es el `β` desde el cual no hay eclipse.

💡 **Cómo se explica en la clase [B86-C04](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md):**
- *Descripción textual:* la altitud da el `β` crítico; con `β` se obtiene la fracción de eclipse y su duración;
- En la órbita sintética de `600 km` (`T = 5792,3 s`) el eclipse ocupa `36,70 %` con `β = 0` (`2126 s`), `34,47 %` con `β = 30°`, `28,25 %` con `β = 50°` y desaparece con `β = 70°`, porque el `β` crítico es `66,05°`.
- 🎯 **Por qué importa:** El eclipse más largo fija el tamaño de la batería y el peor `β` fija el de la ala. Un diseño que mire solo `β = 0` ignora que a `β` alto no hay eclipse pero el coseno cae.

📘 **Dónde se aprende** (1 clase): [B86-C04 · Orientación solar y eclipses](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md).

### ΔT/T = I/(k T B)

- `N = k T B`. `ΔT/T = I/(k T B)` es el aumento relativo de la temperatura de ruido del sistema.

🎯 **Por qué importa (clase B89-C19):** Sin coordinación no hay licencia ni protección: la separación orbital, la potencia y el diagrama de antena se negocian con números como los de esta clase. La decisión central: ¿qué separación orbital hace aceptable la interferencia de un sistema hacia otro?

📘 **Dónde se aprende** (1 clase): [B89-C19 · Coordinación del espectro ante ITU](../programa/clases/B89/B89-C19-coordinacion-del-espectro-ante-itu/CLASE.md).

### Δv

- El Δv es el cambio de velocidad necesario.
- El Δv es la variación de velocidad.
- Disposición: retiro de la nave al final de su vida. Δv: cambio de velocidad.

💡 **Cómo se explica en la clase [B56-C20](../programa/clases/B56/B56-C20-diseno-de-mision-astrobiologica-conceptual/CLASE.md):**
- Con `μ = 1,327 124 400 18 × 10²⁰ m³/s²` (no consultado), `r₁ = 1 UA` y `r₂ = 227,956 × 10⁹ m`: Δv de salida (exceso heliocéntrico) `2,945 km/s`, de llegada `2,649 km/s` y tiempo de vuelo `258,9 d`.
- Con `Isp = 320 s` y masa seca `1000 kg` (sintéticos): para `Δv = 2,945 km/s`, `m₀/m_f = 2,556` y propelente `1556 kg`; para `Δv = 5,594 km/s` (salida más llegada), `5,946` y `4946 kg`.
- 🎯 **Por qué importa:** Una misión que busca vida combina ciencia, ingeniería y protección planetaria. Para decidir si es viable hay que traducir la pregunta científica en requisitos y comprobar que el presupuesto cierra.

📘 **Dónde se aprende** (3 clases): [B56-C20 · Diseño de misión astrobiológica conceptual](../programa/clases/B56/B56-C20-diseno-de-mision-astrobiologica-conceptual/CLASE.md); [B96-C18 · Fin de vida y disposición orbital](../programa/clases/B96/B96-C18-fin-de-vida-y-disposicion-orbital/CLASE.md); [B118-C07 · Estrategias de evasión](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md).

### Δv de corrección

- El `Δv` de corrección es un vector `dv ~ N(0, Σ)`.

💡 **Cómo se explica en la clase [B81-C14](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md):**
- La elección entre estas reglas es de ingeniería: el MC de la suma es la estimación más cercana a «99 % de probabilidad de cubrir las cinco correcciones», pero depende de los supuestos (independencia, gaussianidad) que aquí son sintéticos.
- *Descripción textual:* la desviación por eje define un `Δv` gaussiano; la cuantila de su magnitud se compara con la fórmula chi y con las reglas de combinación para varias correcciones.
- 🎯 **Por qué importa:** Un presupuesto muy bajo deja a la nave sin propelente; uno muy alto la lastra. La decisión central: ¿qué cuantila de `Δv` reservar para una o varias correcciones, y cómo se combinan?

📘 **Dónde se aprende** (1 clase): [B81-C14 · Presupuestos de maniobras de corrección](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md).

### Δv neto

- El `Δv` neto es `Δv_ideal − L_g` (sin aire).

💡 **Cómo se explica en la clase [B77-C08](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md):**
- DV["DV ideal"] --> N["DV neto = ideal - L_g"]
- *Descripción textual:* el empuje inicial fija el tiempo de combustión; con el programa de cabeceo se integra la pérdida gravitacional, que se resta del `Δv` ideal para dar el `Δv` neto.
- 🎯 **Por qué importa:** Un `Δv` ideal alto no garantiza velocidad alta al final. La decisión central: ¿cuánto del `Δv` se pierde por gravedad y cómo se reduce con más empuje o con una trayectoria más inclinada?

📘 **Dónde se aprende** (1 clase): [B77-C08 · Pérdidas gravitacionales](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md).

### Κ de Cohen

- La `κ` de Cohen es `(po − pe)/(1 − pe)`: 0 es acuerdo al azar y 1 es acuerdo total.

💡 **Cómo se explica en la clase [B129-C07](../programa/clases/B129/B129-C07-proyecto-de-ciencia-ciudadana-validable/CLASE.md):**
- Calcular la `κ` de Cohen entre el consenso ciudadano y la referencia experta.
- 🎯 **Por qué importa:** Un proyecto ciudadano que produce datos sin validar es una anécdota; con validación es evidencia. La decisión central: ¿cuántos votos por objeto hacen falta, cómo se sabe que el resultado coincide con el de los expertos y qué le falta al plan para ser una ciencia ciudadana bien hecha?

📘 **Dónde se aprende** (1 clase): [B129-C07 · Proyecto de ciencia ciudadana validable](../programa/clases/B129/B129-C07-proyecto-de-ciencia-ciudadana-validable/CLASE.md).

### Σ robusta

- La σ robusta `1,4826 MAD`.

💡 **Cómo se explica en la clase [B51-C13](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md):**
- Umbral 3,5 σ robusta en 819200 muestras: falsas marcas 0,0426 %; gaussiana `erfc(χ/√2)` = 0,0465 %.
- La mediana robusta sube a +0,121 y la σ robusta a 1,096, porque el 7,9 % de las muestras está contaminado.
- 🎯 **Por qué importa:** Dejar RFI en los datos degrada la imagen; marcar demasiado pierde señal. La decisión central: ¿qué umbral marca la interferencia sin marcar el ruido, y cómo se detecta la interferencia débil y extendida?

📘 **Dónde se aprende** (1 clase): [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md).

### Χ²

- El `χ²` es la suma de residuos al cuadrado divididos por la varianza.
- El `χ²` es `Σ((obs − mod)/σ)²`.
- El χ² es la suma de residuos al cuadrado divididos por `σ²`; el χ² reducido lo divide por los grados de libertad `N − p`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B26-C20](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md):**
- Con `μ_i` observados, `μ_t(z_i; Ω_m)` teóricos (C19) y error `σ = 0,15 mag`, `χ²(Ω_m) = Σ[(μ_i − μ_t,i) − ⟨μ − μ_t⟩]²/σ²`: restar la media de los residuos marginaliza la constante de calibración.
- El laboratorio evalúa `χ²` en una rejilla de `Ω_m` de `0,05` a `0,80` (paso `0,005`) para `100` supernovas con `z` entre `0,02` y `1`.
- 🎯 **Por qué importa:** Una cifra cosmológica sin incertidumbre no significa nada. Para decidir si dos resultados concuerdan, o si un modelo queda excluido, hay que saber construir y leer un intervalo de confianza.

📘 **Dónde se aprende** (4 clases): [B26-C20 · Límites observacionales de modelos cosmológicos](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md); [B37-C14 · Ajuste de modelos estelares a frecuencias sísmicas](../programa/clases/B37/B37-C14-ajuste-de-modelos-estelares-a-frecuencias-sismicas/CLASE.md); [B62-C05 · Constantes espectroscópicas y ajuste de espectros](../programa/clases/B62/B62-C05-constantes-espectroscopicas-y-ajuste-de-espectros/CLASE.md); [B74-C07 · Ajuste por mínimos cuadrados](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md).

### Χ² con varianza igual a las cuentas

- El `χ²` con varianza igual a las cuentas `Σ(n − μ)²/n`.

💡 **Cómo se explica en la clase [B27-C22](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md):**
- Con pocas cuentas, el `χ²` con varianza igual a las observadas da un espectro sistemáticamente más blando (`Γ` mayor) y más disperso; la estadística de Cash casi no tiene sesgo.
- Escribir la estadística de Cash y el `χ²` con varianza igual a las cuentas.
- 🎯 **Por qué importa:** Ajustar un espectro «de fotones» directamente a las cuentas da resultados engañosos; hay que plegar el modelo con la respuesta y usar la estadística correcta para conteos pequeños. La decisión central: ¿qué parámetros recupera cada estadística y con qué sesgo cuando las cuentas son pocas?

📘 **Dónde se aprende** (1 clase): [B27-C22 · Análisis espectral de rayos X y gamma: ajuste con respuesta instrumental](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md).

### Χ² de consistencia

- El `χ²` de consistencia es `Σ(μ_i − μ)²/σ_i²` con `n − 1` grados de libertad.

💡 **Cómo se explica en la clase [B26-C21](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md):**
- No se debe combinar si (a) las medidas dependen de los mismos datos, (b) están obtenidas bajo modelos distintos (por ejemplo `w` libre frente a `w = −1`) o (c) el `χ²` de consistencia es alto.
- Calcular el `χ²` de consistencia y su p-valor.
- ⚠️ **Error frecuente:** Ignorar el `χ²` de consistencia. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Ninguna sonda fija sola todos los parámetros; combinarlas reduce la incertidumbre, pero solo si son compatibles entre sí y si se tratan bien sus correlaciones. La decisión central: dadas tres restricciones sobre `Ω_m`, ¿cuál es el valor combinado, qué incertidumbre tiene y son consistentes entre sí?

📘 **Dónde se aprende** (1 clase): [B26-C21 · Verosimilitud cosmológica con datos combinados](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md).

### Χ² reducido

- El χ² es la suma de residuos al cuadrado divididos por `σ²`; el χ² reducido lo divide por los grados de libertad `N − p`.
- El χ² reducido `χ²/gl`.
- El `χ²` reducido divide por los grados de libertad.

💡 **Cómo se explica en la clase [B32-C08](../programa/clases/B32/B32-C08-sintesis-espectral-e-inversion-de-perfiles/CLASE.md):**
- Con `η₀ = 2,0`, `w = 0,05` y `x₀ = 0` se recupera `η₀ = 1,9709`, `w = 0,05036` y `x₀ = −0,00000`, con `χ²` reducido `1,19`.
- Ejercicio 2 · con una pista. `χ²` reducido.
- 🎯 **Por qué importa:** Una inversión sin barras de error no sirve. La decisión central: ¿qué parámetros se recuperan y con qué incertidumbre?

📘 **Dónde se aprende** (4 clases): [B32-C08 · Síntesis espectral e inversión de perfiles](../programa/clases/B32/B32-C08-sintesis-espectral-e-inversion-de-perfiles/CLASE.md); [B37-C14 · Ajuste de modelos estelares a frecuencias sísmicas](../programa/clases/B37/B37-C14-ajuste-de-modelos-estelares-a-frecuencias-sismicas/CLASE.md); [B51-C07 · Evaluación de residuos y diagnóstico de calidad de calibración](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md); [B62-C05 · Constantes espectroscópicas y ajuste de espectros](../programa/clases/B62/B62-C05-constantes-espectroscopicas-y-ajuste-de-espectros/CLASE.md).
