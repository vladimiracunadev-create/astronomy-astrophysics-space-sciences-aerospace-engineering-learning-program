# Términos · D (parte 3 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · **D** · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-d.md) · [2](terminos-d-2.md) · **3**

### Dosis absorbida

- La dosis absorbida `D` se mide en gray.
- La dosis absorbida `D` (Gy = J/kg) es energía por masa.
- La dosis absorbida `D` es la energía depositada por unidad de masa, `D = E/m`, y su unidad es el gray (1 Gy = 1 J/kg).

💡 **Cómo se explica en la clase [B64-C01](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md):**
- Definir dosis absorbida en gray (J/kg) y convertirla en número medio de DSB por genoma.
- 🎯 **Por qué importa:** La radiación ionizante rompe el ADN, y una célula muere cuando el daño supera su capacidad de reparación. La pregunta motivadora: ¿por qué dos organismos con el mismo daño inicial por gray sobreviven a dosis tan distintas?
- 🔗 **Se estudia junto con:** rotura de doble cadena (DSB), rendimiento, capacidad de reparación, supervivencia.

📘 **Dónde se aprende** (3 clases): [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md); [B105-C06 · Radiación ionizante y exposición](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md); [B112-C01 · Magnitudes dosimétricas: dosis absorbida, LET y eficacia biológica](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md).

### Dosis característica

- La dosis característica `D₀` es la que reduce la población a `1/e`.

💡 **Cómo se explica en la clase [B55-C17](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md):**
- Un aminoácido hipotético con dosis característica `D₀ = 10⁶ Gy` y tasa de dosis de `10⁻³ Gy/año` (ambas ilustrativas), y una proporción verdadera de forma L de 0,55 (exceso enantiomérico 0,10).
- 🎯 **Por qué importa:** Que un compuesto prebiótico llegue intacto hasta nosotros depende de cuánta radiación recibió, y que un exceso entre dos formas quirales sea real depende de cuántas moléculas se contaron. La decisión central: ¿cuánto sobrevive y con qué incertidumbre puedo afirmar un exceso enantiomérico distinto de cero?
- 🔗 **Se estudia junto con:** radiólisis, exceso enantiomérico, desviación del conteo, distinguible de cero.

📘 **Dónde se aprende** (1 clase): [B55-C17 · Compuestos prebióticos](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md).

### Dosis de gravedad

- La dosis de gravedad sería la relación entre `g` y la respuesta biológica: se desconoce en este texto.

💡 **Contexto en la clase [B105-C18](../programa/clases/B105/B105-C18-investigacion-de-efectos-de-gravedad-parcial/CLASE.md):**
- 🎯 **Por qué importa:** Se puede calcular con exactitud cuánto pesa y cómo se mueve un cuerpo en la Luna; no se puede deducir de eso cuánta gravedad hace falta para mantener el hueso. La decisión central: ¿qué parte de la respuesta a la gravedad parcial es física calculable y qué parte es una pregunta de investigación abierta?
- 🔗 **Se estudia junto con:** gravedad parcial, número de Froude, peso.

📘 **Dónde se aprende** (1 clase): [B105-C18 · Investigación de efectos de gravedad parcial](../programa/clases/B105/B105-C18-investigacion-de-efectos-de-gravedad-parcial/CLASE.md).

### Dosis efectiva

- La dosis efectiva es `E = Σ_T w_T H_T`, con `w_T` el factor de ponderación del tejido, que representa su contribución relativa al detrimento total y cuya suma vale 1 (definiciones del glosario de ICRP 103, consultado).
- La dosis efectiva `E = Σ w_T H_T` (Sv) pondera por tejido; sus factores los fija la ICRP en su Publicación 103 (2007), página consultada el 2026-11-10 en resumen.

💡 **Cómo se explica en la clase [B105-C06](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md):**
- *Descripción textual:* la dosis absorbida se pondera por radiación y por tejido para dar la dosis efectiva; se acumula en un presupuesto de misión, se compara con un límite y se acompaña de su incertidumbre.
- Analogía: una cuenta en la que cada gasto se multiplica por un tipo de cambio según la moneda; la dosis efectiva es el total convertido.
- 🎯 **Por qué importa:** La dosis no se «lee»: se calcula a partir de una dosis absorbida, de factores de calidad y de ponderación, y esos factores tienen incertidumbre. La decisión central: ¿qué fracción del límite de carrera consume una misión y con qué probabilidad lo supera una secuencia de misiones?
- 🔗 **Se estudia junto con:** dosis absorbida, dosis equivalente, límite de carrera, evento de partículas solares.

📘 **Dónde se aprende** (2 clases): [B105-C06 · Radiación ionizante y exposición](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md); [B112-C02 · Dosis equivalente y dosis efectiva](../programa/clases/B112/B112-C02-dosis-equivalente-y-dosis-efectiva/CLASE.md).

### Dosis equivalente

- La dosis equivalente de un tejido es `H_T = Σ_R w_R D_{T,R}`, con `w_R` el factor de ponderación de la radiación (adimensional) que refleja la mayor eficacia biológica del alto LET; su unidad es el sievert.
- La dosis equivalente `H` se mide en mSv.
- La dosis equivalente `H_T = w_R D_T` (Sv) pondera por el tipo de radiación.

💡 **Cómo se explica en la clase [B105-C06](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md):**
- Paso 1 · Dosis equivalente diaria. `0,30 mGy·2,5 = 0,75 mSv`.
- Convertir dosis absorbida en dosis equivalente (`H = w_R D`) y esta en dosis efectiva (`E = Σ w_T H_T`).
- 🎯 **Por qué importa:** La dosis no se «lee»: se calcula a partir de una dosis absorbida, de factores de calidad y de ponderación, y esos factores tienen incertidumbre. La decisión central: ¿qué fracción del límite de carrera consume una misión y con qué probabilidad lo supera una secuencia de misiones?
- 🔗 **Se estudia junto con:** dosis absorbida, dosis efectiva, límite de carrera, evento de partículas solares.

📘 **Dónde se aprende** (3 clases): [B105-C06 · Radiación ionizante y exposición](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md); [B112-C02 · Dosis equivalente y dosis efectiva](../programa/clases/B112/B112-C02-dosis-equivalente-y-dosis-efectiva/CLASE.md); [B114-C04 · Refugio contra tormentas solares y compartimentos de protección](../programa/clases/B114/B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md).

### Dosis ionizante total

- La dosis ionizante total (TID, en Gy).

💡 **Contexto en la clase [B47-C14](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md):**
- **Idea central (modelo mental):** El blindaje es un paraguas: detiene las gotas lentas y deja pasar las rápidas, pero las gotas que casi se detienen son las que más mojan al final.
- 🎯 **Por qué importa:** El blindaje reduce la dosis hasta que el protón se detiene; los eventos de partícula simple, en cambio, son aleatorios. La decisión central: ¿qué espesor de blindaje y qué probabilidad de eventos son aceptables?
- 🔗 **Se estudia junto con:** fluencia, blindaje, evento de partícula simple, sección eficaz.

📘 **Dónde se aprende** (1 clase): [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md).

### Dosis por órbita

- La dosis por órbita es `∫ D dt`.

💡 **Cómo se explica en la clase [B75-C28](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md):**
- La dosis por órbita es `D₀ R_J³/(86 400)·2π/(h p)` en `u` (con `h` en km²/s y `p` en km).
- Blindaje (`λ = 10 g/cm²`, sintético): factor `0,9048` con 1 g/cm², `0,6065` con 5, `0,3679` con 10 y `0,1353` con 20; la dosis por órbita de la primera órbita baja de `4624` a `4184`, `2805`, `1701` y `626 u`.
- 🎯 **Por qué importa:** Una trayectoria es también un perfil de exposición. La decisión central: ¿cuánta dosis acumula una nave por órbita y cuántas órbitas aguanta, según el periapsis y el blindaje?
- 🔗 **Se estudia junto con:** tasa de dosis, blindaje, límite de dosis, unidad.

📘 **Dónde se aprende** (1 clase): [B75-C28 · Restricciones de radiación en trayectorias](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md).

### Dosis total ionizante

- La dosis total ionizante acumulada se compara con umbrales de material.

💡 **Contexto en la clase [B85-C24](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md):**
- 🎯 **Por qué importa:** Una celda solar o un polímero no fallan de golpe: pierden prestaciones con la exposición. La decisión central: ¿cuánta potencia queda al final de la misión y cuánto cambia con un blindaje que reduce la fluencia?
- 🔗 **Se estudia junto con:** ley de degradación, NIEL, umbrales, inversa.

📘 **Dónde se aprende** (1 clase): [B85-C24 · Efectos de la radiación ionizante en materiales y electrónica](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md).

### Dossier

- El dossier reúne cifras, fuentes y derivaciones.
- El dossier documenta requisitos, cálculos y verificación.

💡 **Cómo se explica en la clase [B28-C20](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md):**
- La huella SHA-256 del dossier empieza por `032988a045c269cc`; es estable al reserializar el mismo contenido.
- *Descripción textual:* los resúmenes dan cifras publicadas; se comprueba su coherencia y se calculan magnitudes derivadas; el dossier incluye la lista de lo no consultado y se firma con una huella.
- 🎯 **Por qué importa:** Un caso de estudio sirve si es verificable: cada cifra debe llevar su fuente, y lo calculado debe distinguirse de lo publicado. La decisión central: ¿qué cifras del evento están respaldadas por lo consultado, cuáles se derivan y cuáles quedan fuera?
- 🔗 **Se estudia junto con:** cifra publicada, cifra derivada, coherencia, cifra excluida.

📘 **Dónde se aprende** (2 clases): [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md); [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md).

### Dotación mínima

- La dotación mínima `k` es el número de personas que necesita.

💡 **Cómo se explica en la clase [B122-C10](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md):**
- Identificar funciones esenciales y su dotación mínima `k`.
- 🎯 **Por qué importa:** No hay clase equivalente sobre continuidad de funciones institucionales. La decisión central: ¿qué dotación mínima asegura que cada función esencial se cubra con al menos el 99 %?
- 🔗 **Se estudia junto con:** función esencial, plantilla, disponibilidad individual, plan de continuidad de operaciones.

📘 **Dónde se aprende** (1 clase): [B122-C10 · Planes de continuidad institucional y de operaciones](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md).

### Dragado

- El dragado (*dredge-up*) es la mezcla convectiva que lleva a la superficie material procesado.

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- Tras cada pulso, la convección puede arrastrar material procesado a la envoltura (dragado).
- Si en cada pulso un dragado lleva `ΔM` de material con fracción de masa de carbono `X_C,dr` y de oxígeno `X_O,dr` a la envoltura, la masa de carbono crece en `ΔM X_C,dr` y la envoltura en `ΔM`.
- ⚠️ **Error frecuente:** Olvidar que el dragado también añade masa a la envoltura. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.
- 🔗 **Se estudia junto con:** rama asintótica de gigantes (AGB), pulso térmico, proceso s, exposición de neutrones.

📘 **Dónde se aprende** (1 clase): [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### DRO

- Una DRO es una órbita periódica retrógrada y plana alrededor de la Luna.

💡 **Cómo se explica en la clase [B76-C06](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md):**
- Una DRO de `70.000 km` supera el radio de Hill (`61.274 km`) y permanece ligada porque es periódica y retrógrada.
- Una DRO que cruza `y = 0` a `70.000 km` de la Luna tiene `vy0 = 0,519364` (adimensional), periodo `13,916 d` y `C = 2,92852`; su máxima separación al otro lado es `73.434 km`.
- ⚠️ **Error frecuente:** Buscar la DRO sin continuación. Se corrige con 8.2.
- 🎯 **Por qué importa:** La NRHO es inestable y exige mantenimiento; la DRO es estable. La decisión central: ¿qué se gana y qué se paga al elegir una órbita estable y lejana frente a una NRHO cercana?
- 🔗 **Se estudia junto con:** amplitud, continuación, monodromia plana, par doble en 1.

📘 **Dónde se aprende** (1 clase): [B76-C06 · Órbitas DRO — Dinámica cislunar y operaciones de proximidad](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md).

### DSK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Contexto en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, CK, PCK.

📘 **Dónde se aprende** (1 clase): [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### Dunas

- Las ripples y dunas son formas que el transporte genera en el lecho.

💡 **Cómo se explica en la clase [B66-C03](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. Una duna observada en Titán, ¿prueba que el viento actual supera el umbral?
- No: las dunas pueden ser antiguas o formadas por vientos raros; esta clase no usa observaciones.
- 🎯 **Por qué importa:** Marte tiene dunas y una atmósfera cien veces menos densa que la terrestre; Venus, una atmósfera enorme y casi sin viento.
- 🔗 **Se estudia junto con:** velocidad umbral de fricción, parámetro de Shields, saltación, longitud de saltación.

📘 **Dónde se aprende** (1 clase): [B66-C03 · Procesos eólicos: dunas, ripples y erosión planetaria](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md).

### Duplicación de paso

- La duplicación de paso compara un paso de tamaño `h` con dos de tamaño `h/2`; para un método de orden 4, el error del resultado de dos pasos medios es aproximadamente `|s₂ − s₁|/15` (extrapolación de Richardson).

💡 **Cómo se explica en la clase [B11-C08](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md):**
- El adaptativo por duplicación gasta tres pasos por intento (12 evaluaciones) pero es fácil de entender y de programar.
- El script [paso_adaptativo_excentrica.py](paso_adaptativo_excentrica.py) implementa RK4 con duplicación de paso, lo compara con la solución exacta de Kepler y con paso fijo (mismos pasos y mismo costo).
- 🎯 **Por qué importa:** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.
- 🔗 **Se estudia junto con:** error local estimado, tolerancia, error normalizado, acepta.

📘 **Dónde se aprende** (1 clase): [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md).

### Duplicado

- Un duplicado es la misma obra registrada más de una vez, por ejemplo la versión de un manuscrito y la del artículo publicado.
- Un duplicado repite una clave.

💡 **Cómo se explica en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- Cuenta en cada etapa: identificados; duplicados eliminados; cribados; excluidos por cada motivo; incluidos.
- Debe cumplirse una conservación sencilla: `identificados − duplicados = cribados = incluidos + excluidos`.
- ⚠️ **Error frecuente:** Eliminar duplicados solo por título parecido. Dos obras distintas pueden compartir título; se confirma con identificador y autores (ejercicios 1 y 8).
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.
- 🔗 **Se estudia junto con:** pregunta de revisión, cadena de consulta, operador lógico, criterios de inclusión y exclusión.

📘 **Dónde se aprende** (2 clases): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md); [B129-C04 · Contribución de medidas voluntarias con control de calidad](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md).

### Duplicado exacto

- Un duplicado exacto es una fila repetida en todas sus columnas, incluido su identificador.

💡 **Cómo se explica en la clase [B14-C08](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md):**
- C --> D["Quitar duplicados<br/>4 exactos"]
- *Descripción textual:* la tabla de 200 filas pasa por cuatro pasos encadenados: normalizar los nombres (de siete grafías a tres), convertir centinelas en `NaN` (con lo que hay 12 faltantes en total), quitar cuatro duplicados exactos y marcar tres atípicos sin borrarlos.
- 🎯 **Por qué importa:** Una bitácora de observación real tiene errores: alguien escribió `-99` donde faltaba un dato, el mismo objeto aparece con tres grafías, una fila se copió dos veces, un valor tiene un dígito de más. Si calculas una media sin limpiar, el resultado es otro número.
- 🔗 **Se estudia junto con:** magnitud, centinela, valor ausente, atípico.

📘 **Dónde se aprende** (1 clase): [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md).

### Duración

- La duración es el tiempo del tránsito.
- La duración `T₁₄` va del primer al último contacto.

💡 **Cómo se explica en la clase [B29-C01](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md):**
- El radio se infiere de la profundidad, pero hay que corregir por oscurecimiento al limbo y por el parámetro de impacto; la duración, a su vez, depende de `a`, `b` y `k`.
- *Descripción textual:* los radios dan la profundidad; el periodo y la masa estelar dan el semieje, y con el parámetro de impacto la duración, que se verifica con una búsqueda numérica; el oscurecimiento al limbo modifica la profundidad central.
- 🎯 **Por qué importa:** El tránsito es el método con más planetas descubiertos. Su profundidad da el radio del planeta y su duración informa del semieje y el parámetro de impacto.
- 🔗 **Se estudia junto con:** profundidad, parámetro de impacto, oscurecimiento al limbo, contactos.

📘 **Dónde se aprende** (2 clases): [B29-C01 · Tránsitos planetarios](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md); [B131-C06 · Aprendizaje basado en problemas con datos astronómicos](../programa/clases/B131/B131-C06-aprendizaje-basado-en-problemas-con-datos-astronomicos/CLASE.md).

### Duración cenital

- La duración cenital `2λ_max/n` es la máxima.

💡 **Cómo se explica en la clase [B89-C14](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md):**
- L --> D["duracion cenital = 2 lambda / n"]
- *Descripción textual:* la altura y la máscara dan el semiángulo central y la duración cenital; la simulación de un día da las pasadas reales; con la tasa se obtiene el volumen de datos.
- ⚠️ **Error frecuente:** Usar la duración cenital como típica. Se corrige con 8.4.
- 🎯 **Por qué importa:** El tiempo de contacto es el recurso más escaso de un satélite de órbita baja: define cuántos datos bajan por día y cuántas estaciones se necesitan. La decisión central: ¿cuánto contacto y cuántos datos da una estación a un satélite de órbita baja?
- 🔗 **Se estudia junto con:** máscara de elevación, ángulo central, pasada, volumen de datos.

📘 **Dónde se aprende** (1 clase): [B89-C14 · Estaciones terrestres](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md).

### Duración del vuelo

- La duración del vuelo es el tiempo total de una misión; el período orbital es el de una sola vuelta.

💡 **Cómo se explica en la clase [B02-C19](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md):**
- Cuidado: los 108 minutos son la duración del vuelo (ascenso, una vuelta, descenso), no el período orbital; por eso no sirven para el cálculo de la tercera ley.
- Distinguir duración de un vuelo de período orbital.
- ⚠️ **Error frecuente:** Usar la duración del vuelo como período. Ejercicio 6.
- 🎯 **Por qué importa:** La exploración espacial es una historia científica y también política. La pregunta motivadora es: ¿qué cambió, para la astronomía y para la sociedad, cuando los instrumentos y las personas empezaron a salir de la atmósfera, y qué reglas se acordaron?
- 🔗 **Se estudia junto con:** satélite artificial, órbita baja, período orbital, órbita geoestacionaria.

📘 **Dónde se aprende** (1 clase): [B02-C19 · Historia de la exploración espacial](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md).

### Duración mínima

- La duración mínima `T = V/(C_s Q)` supone caudal de banca llena continuo.

💡 **Cómo se explica en la clase [B66-C04](../programa/clases/B66/B66-C04-redes-fluviales-fosiles-y-paleohidrologia-marciana/CLASE.md):**
- *Descripción textual:* el terreno se rellena, se calculan direcciones y acumulación, se definen canales con un umbral y del área mayor sale el caudal y la duración mínima.
- Estimar `Q = r A` y la duración mínima `T = V/(C_s Q)`.
- 🎯 **Por qué importa:** Un mapa de valles marcianos invita a decir «hubo un océano» o «hubo lluvia». La decisión central: ¿qué se puede inferir del caudal y de la duración con una red, un volumen y supuestos explícitos, y qué incertidumbre arrastra?
- 🔗 **Se estudia junto con:** método D8, acumulación, llenado de depresiones, densidad de drenaje.

📘 **Dónde se aprende** (1 clase): [B66-C04 · Redes fluviales fósiles y paleohidrología marciana](../programa/clases/B66/B66-C04-redes-fluviales-fosiles-y-paleohidrologia-marciana/CLASE.md).

### Duración nominal

- Reintento: repetición de un paso fallido. Duración nominal: suma sin fallos.

💡 **Cómo se explica en la clase [B96-C14](../programa/clases/B96/B96-C14-procedimientos-de-recuperacion/CLASE.md):**
- Duración nominal `= 30 + 25 + 60 + 40 + 35 + 30 = 220 s`.
- Calcular la duración nominal y compararla con la ventana.
- 🎯 **Por qué importa:** Una recuperación que no cabe en la pasada o que falla en un paso sin reintento deja a la nave a medias hasta el siguiente contacto. La decisión central: ¿cabe el procedimiento en la ventana y qué probabilidad tiene de completarse con reintentos?
- 🔗 **Se estudia junto con:** Procedimiento, Reintento, Probabilidad de éxito, Monte Carlo.

📘 **Dónde se aprende** (1 clase): [B96-C14 · Procedimientos de recuperación](../programa/clases/B96/B96-C14-procedimientos-de-recuperacion/CLASE.md).

### Duración singular

- Una duración singular es un `T` en que `det Φ_rv` es casi nulo.

💡 **Cómo se explica en la clase [B76-C12](../programa/clases/B76/B76-C12-guiado-relativo/CLASE.md):**
- *Descripción textual:* de los estados y la duración salen los bloques de la matriz; invertir `Φ_rv` da la velocidad necesaria y de ella los dos impulsos; el determinante avisa de las duraciones singulares.
- Reconocer las duraciones singulares (`det Φ_rv ≈ 0`).
- ⚠️ **Error frecuente:** Pensar que más tiempo siempre cuesta menos. Hay duraciones singulares.
- 🎯 **Por qué importa:** El mismo algoritmo sirve para cientos de maniobras, pero falla en tiempos singulares. La decisión central: ¿cómo se calculan los impulsos y para qué duraciones el problema está mal condicionado?
- 🔗 **Se estudia junto con:** bloques de transición, primer impulso, segundo.

📘 **Dónde se aprende** (1 clase): [B76-C12 · Guiado relativo](../programa/clases/B76/B76-C12-guiado-relativo/CLASE.md).
