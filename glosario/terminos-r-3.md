# Términos · R (parte 3 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · **R** · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-r.md) · [2](terminos-r-2.md) · **3**

### ROE

- La ROE (razón de onda estacionaria) `(1 + |Γ|)/(1 − |Γ|)`.

💡 **Cómo se explica en la clase [B49-C02](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md):**
- El patrón de ondas estacionarias de esa carga da ROE muestreada `1,64872`, igual a la analítica (`|Γ| = 0,24492`).
- Una ROE de 1,46 pierde solo 0,155 dB; una de 5 pierde 2,55 dB.
- ⚠️ **Error frecuente:** Confundir ROE y pérdida de retorno. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una antena desadaptada devuelve potencia y empeora la sensibilidad. La decisión central: ¿cuánta potencia se refleja y cómo se adapta con un tramo de línea?

📘 **Dónde se aprende** (1 clase): [B49-C02 · Adaptación de impedancias y líneas de transmisión en antenas](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md).

### Rol

- Un rol es una responsabilidad asignada a una persona.
- Criticidad: consecuencia de un comando. Rol: nivel de autoridad.

💡 **Cómo se explica en la clase [B96-C07](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md):**
- Se evalúan `3 × 4 × 5 × 2 = 120` combinaciones (rol, criticidad, cinco listas de aprobaciones, armado sí/no) con la política y con una referencia independiente basada en tablas de mínimos.
- (3) Monotonía: si un rol menor está autorizado, el siguiente también lo está.
- 🎯 **Por qué importa:** Un comando enviado por la persona equivocada o sin segunda revisión puede perder la misión. La decisión central: ¿qué rol, qué aprobaciones y qué armado exige cada nivel de criticidad y cómo se prueba que la política no tiene huecos?

📘 **Dónde se aprende** (2 clases): [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B96-C07 · Telecomandos y autorizaciones](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md).

### Roll-off

- El roll-off `α` es el exceso de banda del filtro de coseno alzado; el ancho ocupado es `Rs(1+α)`.

💡 **Cómo se explica en la clase [B89-C02](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md):**
- *Descripción textual:* la tasa de bits, el código y la modulación dan la tasa de símbolos; con el roll-off, el ancho ocupado; este decide cuántos canales caben y la capacidad de Shannon; el Doppler se suma por separado.
- ILUSTRATIVO: Rb = 2 Mbit/s, codigo 1/2, QPSK, roll-off 0.35, guarda 0.3 MHz, banda 50 MHz
- ⚠️ **Error frecuente:** Olvidar el roll-off al calcular el ancho. Se corrige con 8.1.
- 🎯 **Por qué importa:** Sin una idea cuantitativa del ancho de banda no se puede decidir cuántos enlaces caben en una banda ni cuánta tasa de datos es posible. La regulación (C19) trabaja con exactamente estas magnitudes.

📘 **Dónde se aprende** (1 clase): [B89-C02 · Frecuencia y espectro espacial](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md).

### Romper la cadena de contacto

- La Categoría V agrupa las misiones de retorno a la Tierra. «Retorno restringido» es la subcategoría de mayor preocupación. Romper la cadena de contacto es evitar que hardware que tocó el cuerpo regrese sin contención.

💡 **Cómo se explica en la clase [B63-C04](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md):**
- Explicar qué significa «romper la cadena de contacto».
- Ejercicio 9 · transferencia. Transferencia. ¿Qué quiere decir «romper la cadena de contacto»?
- 🎯 **Por qué importa:** Traer material de otro cuerpo exige proteger a la Tierra y a la muestra. La decisión central: ¿cuántas barreras independientes hacen falta, y qué pasa si dejan de ser independientes?

📘 **Dónde se aprende** (1 clase): [B63-C04 · Misiones de retorno de muestras: salvaguardas históricas y regulatorias](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md).

### Ronda con precio

- La ronda con precio vende acciones preferentes a un precio por acción.

💡 **Cómo se explica en la clase [B126-C01](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md):**
- Si el precio de la ronda es `P = V/(C+s)` y el SAFE paga `(1 − d)P`, entonces `s = INV/((1 − d)P)`.
- *Descripción textual:* el SAFE se convierte por dos caminos (tope o descuento) y recibe el que da más acciones; con eso se obtiene el precio de la ronda y la tabla de capitalización, y se verifica con una iteración de punto fijo.
- 🎯 **Por qué importa:** El catálogo trata el financiamiento privado en general (B124-C07, «Financiamiento privado», en la [guía del bloque B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md)), no la mecánica de las etapas iniciales.

📘 **Dónde se aprende** (1 clase): [B126-C01 · Capital semilla y financiamiento inicial](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md).

### Root

- Un resumen (*digest*) identifica una imagen por su contenido. Root es el usuario con todos los privilegios.

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- ⚠️ **Error frecuente:** Ejecutar como root. Se corrige con la regla `USER` de la sección 8.2.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende** (1 clase): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md).

### Rotación

- Una rotación es una transformación lineal que conserva longitudes y ángulos y no invierte la orientación: su matriz `R` cumple `RᵀR = I` y `det R = +1` (una matriz ortogonal, con el determinante de C04).
- La rotación cambia de época.

💡 **Cómo se explica en la clase [B10-C12](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md):**
- En SPICE, la matriz `[w]ᵢ` «rota el sistema de coordenadas `w` radianes alrededor del eje `i` y rota los vectores `−w`» (S1): su matriz es la transpuesta de la activa.
- *Descripción textual:* para un mismo ángulo, la rotación activa aplica `R(θ)` y la pasiva aplica su transpuesta; los números se parecen pero los signos difieren, y confundirlas es el error más común.
- ⚠️ **Error frecuente:** Confundir rotación activa y pasiva (signo). Se corrige con los ejercicios 2 y 11.
- 🎯 **Por qué importa:** La Tierra gira una vuelta cada 23,93 horas: una estación de seguimiento ve pasar los satélites porque sus ejes locales rotan respecto del espacio inercial. Un satélite recibe órdenes expresadas en ejes terrestres y debe saber dónde están en ejes inerciales.

📘 **Dónde se aprende** (2 clases): [B10-C12 · Rotaciones en el plano y espacio](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md); [B88-C38 · Gestión de claves y secretos en aviónica](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md).

### Rotación 3‑1‑3

- La rotación 3‑1‑3 es `R_z(Ω) R_x(i) R_z(ω)`.

💡 **Cómo se explica en la clase [B71-C17](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md):**
- En 500 estados sintéticos (semilla 17) cumple `max|M Mᵀ − I| = 4.4e-16` y `|det M − 1| = 4.4e-16`: es una rotación propia.
- *Descripción textual:* las coordenadas perifocales se rotan al marco inercial; los invariantes (`h`, energía, componentes) y una integración inercial comprueban que la rotación es correcta.
- 🎯 **Por qué importa:** Casi todo error de signo o de orden en una rotación aparece como un plano equivocado. La decisión central: ¿cómo pasas del plano orbital al marco inercial y cómo compruebas que la transformación es correcta?

📘 **Dónde se aprende** (1 clase): [B71-C17 · Movimientos en planos orbitales](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md).

### Rotación activa

- Una rotación activa gira el punto manteniendo los ejes; una rotación pasiva gira los ejes y deja el punto, de modo que sus componentes cambian.

💡 **Cómo se explica en la clase [B04-C15](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md):**
- Distinguir rotación activa (de puntos) y pasiva (de ejes) y sus signos.
- Ejercicio 7. Gira el vector `(1; 1; 0)` +0,5 rad de forma activa alrededor de `x` y comprueba que es igual a la rotación pasiva de −0,5 rad.
- 🎯 **Por qué importa:** El ecuador de la Tierra y el plano de su órbita (la eclíptica) forman un ángulo de unos 23,4°. Los catálogos de estrellas se dan en coordenadas ecuatoriales; el movimiento del Sol, la Luna y los planetas es más simple en coordenadas eclípticas.

📘 **Dónde se aprende** (1 clase): [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md).

### Rotación de campo

- La rotación de campo es el giro de la imagen que sufre una montura altacimutal al seguir un objeto.
- La rotación de campo es el giro de la imagen respecto del horizonte; es el ángulo paraláctico `q`.

💡 **Cómo se explica en la clase [B08-C15](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md):**
- Además, la imagen gira (rotación de campo), irrelevante a ojo pero grave para fotografiar (C19).
- C --> E["Dos movimientos variables<br/>y rotación de campo"]
- 🎯 **Por qué importa:** A 120 aumentos, un planeta cruza el ocular en menos de dos minutos y tienes que empujar el tubo constantemente. La pregunta motivadora: ¿qué montura necesito y qué error puedo tolerar al seguir un objeto?

📘 **Dónde se aprende** (3 clases): [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md); [B41-C18 · Monturas y mecanismos de seguimiento](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md); [B43-C13 · Montura altacimutal](../programa/clases/B43/B43-C13-montura-altacimutal/CLASE.md).

### Rotación de Faraday

- La rotación de Faraday `χ = χ₀ + RM λ²`.
- La rotación de Faraday: `χ = RM λ²`.

💡 **Cómo se explica en la clase [B51-C05](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md):**
- python programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/ionosfera.py
- 🎯 **Por qué importa:** A frecuencias bajas la ionosfera domina el error de fase y de polarización. La decisión central: ¿cómo se mide y se quita el efecto con las propias frecuencias de la observación?

📘 **Dónde se aprende** (2 clases): [B46-C13 · Polarimetría de radio](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md); [B51-C05 · Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md).

### Rotación de Rodrigues

- La rotación de Rodrigues `v cos θ + (k×v) sen θ + k (k·v)(1−cos θ)`.

💡 **Cómo se explica en la clase [B43-C17](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md):**
- Calcular la deriva con rotaciones de Rodrigues exactas.
- El script [alineacion_polar.py](alineacion_polar.py) simula la deriva con rotaciones de Rodrigues, la compara con la predicción lineal e invierte para estimar el error (comprueba `1 %`).
- 🎯 **Por qué importa:** La alineación polar se corrige midiendo la deriva de una estrella. La decisión central: ¿qué deriva produce un error de acimut o de altura y cómo se invierte para corregirlo?

📘 **Dónde se aprende** (1 clase): [B43-C17 · Alineación polar](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md).

### Rotación diferencial

- La rotación diferencial es girar a distinto ritmo según la latitud.
- La rotación diferencial es que la velocidad angular depende del radio.
- La rotación diferencial es que las zonas giran distinto.

💡 **Cómo se explica en la clase [B24-C11](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md):**
- Nombrar qué limita el modelo (rotación diferencial, pérdida de momento angular).
- 🎯 **Por qué importa:** La rotación y el campo explican por qué las estrellas jóvenes son más activas, por qué las enanas blancas y las estrellas de neutrones giran y se magnetizan tanto, y por qué no pueden girar a cualquier velocidad.

📘 **Dónde se aprende** (3 clases): [B24-C11 · Rotación y campos magnéticos](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md); [B25-C02 · Brazos espirales y barra galáctica](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md); [B37-C11 · Rotación interna a partir del desdoblamiento de frecuencias](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md).

### Rotación pasiva

- Una rotación activa gira el punto manteniendo los ejes; una rotación pasiva gira los ejes y deja el punto, de modo que sus componentes cambian.

💡 **Cómo se explica en la clase [B04-C15](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md):**
- A["Componentes ecuatoriales<br/>(x, y, z)"] -->|"R_x(ε): rotación pasiva de ejes"| B["Componentes eclípticas"]
- *Descripción textual:* de las componentes ecuatoriales se pasa a las eclípticas con la rotación pasiva `R_x(ε)`; la traspuesta devuelve las ecuatoriales; de las eclípticas salen longitud y latitud con `atan2` y `arcsen`; y la matriz se comprueba con ortogonalidad y determinante 1.
- 🎯 **Por qué importa:** El ecuador de la Tierra y el plano de su órbita (la eclíptica) forman un ángulo de unos 23,4°. Los catálogos de estrellas se dan en coordenadas ecuatoriales; el movimiento del Sol, la Luna y los planetas es más simple en coordenadas eclípticas.

📘 **Dónde se aprende** (1 clase): [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md).

### Rotación sincrónica

- La rotación sincrónica es que la Luna gira sobre su eje una vez por cada vuelta alrededor de la Tierra, por lo que muestra siempre la misma cara; la libración son pequeños balanceos que dejan ver algo más de la mitad (S3).

💡 **Cómo se explica en la clase [B08-C08](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md):**
- Como la rotación es sincrónica, ves siempre la misma cara, pero las tablas de la NASA muestran el punto de la Luna que mira a la Tierra (el «punto subterrestre») moviéndose: en 2025 su longitud selenográfica varió entre −7,7° y +8,0°, y su latitud entre −6,8° y +6,9°.
- Explicar la rotación sincrónica y la libración, con sus magnitudes de 2025.
- 🎯 **Por qué importa:** La Luna es el primer blanco de cualquier observación y el principal enemigo de las observaciones de objetos débiles (C12). Saber su fase y cuándo está en el cielo es parte de toda planificación.

📘 **Dónde se aprende** (1 clase): [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md).

### Rotacional

- El rotacional `∇×F` mide cuánto «gira» (ec. 1.6.22).

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- Para la gravedad, el rotacional es cero (laboratorio: `< 10⁻¹⁵ s⁻²`): el campo es conservativo.
- Rotacional cero no significa «sin movimiento».
- ⚠️ **Error frecuente:** Confundir divergencia (escalar) con rotacional (vector). Se corrige con los ejercicios 1 y 2.
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.

📘 **Dónde se aprende** (1 clase): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md).

### Rotaciones elementales

- Las rotaciones elementales (activas, regla de la mano derecha) son `Rₓ(a) = [[1, 0, 0], [0, cos a, −sin a], [0, sin a, cos a]]`, `R_y(a) = [[cos a, 0, sin a], [0, 1, 0], [−sin a, 0, cos a]]`, `R_z(a) = [[cos a, −sin a, 0], [sin a, cos a, 0], [0, 0, 1]]`.

💡 **Cómo se explica en la clase [B10-C13](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu cuaderno de matrices de rotación: tres matrices elementales con su verificación, una composición de dos giros en ambos órdenes con el efecto sobre un vector, el eje y el ángulo de la composición, la matriz de marco de SPICE y la prueba de deriva.
- 🎯 **Por qué importa:** La actitud de un satélite (hacia dónde apuntan sus ejes) se guarda como una matriz de rotación: sus columnas son los ejes del cuerpo expresados en el sistema inercial. Con ella, un seguidor estelar, un panel o una antena se orientan sin ambigüedad.

📘 **Dónde se aprende** (1 clase): [B10-C13 · Matrices de rotación tridimensional](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md).

### Rotador rápido

- Un rotador rápido tiene rotación ordenada comparable a su dispersión; uno lento, poca rotación (S2).

💡 **Cómo se explica en la clase [B25-C09](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md):**
- Cappellari (S2), con espectroscopía de campo integral, separa las galaxias de tipo temprano en rotadores rápidos y lentos: los lentos son débilmente triaxiales y dominan por encima de una masa crítica de unos `2 × 10¹¹ M☉`; los rápidos, por debajo, se parecen a las espirales.
- Describir qué distingue rotadores rápidos y lentos entre las galaxias de tipo temprano.
- 🎯 **Por qué importa:** Las galaxias parecen muy distintas: discos con brazos y gas, o bolas suaves de estrellas viejas. Esa diferencia guarda su historia (formación estelar, fusiones) y exige un lenguaje común para compararlas.

📘 **Dónde se aprende** (1 clase): [B25-C09 · Galaxias elípticas y espirales](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md).

### Rotor rígido

- El rotor rígido es una molécula lineal que gira sin deformarse; sus niveles son `E_J = h B J(J+1)` y las transiciones `J → J−1` caen en `ν = 2 B J`.
- Un rotor rígido es una molécula cuyos núcleos giran a distancia fija.
- El rotor rígido: `E_J = hB J(J+1)`.

💡 **Cómo se explica en la clase [B46-C12](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md):**
- Límite: rotor rígido, ETL y sin profundidad óptica.
- Límites: rotor rígido, ETL, sin opacidad.
- 🎯 **Por qué importa:** Qué transición observar depende de la temperatura del gas, porque la población de cada nivel cambia. La decisión central: ¿qué línea es la más intensa a una temperatura dada?

📘 **Dónde se aprende** (3 clases): [B46-C12 · Emisiones moleculares](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md); [B55-C09 · Espectros moleculares de radio](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md); [B62-C01 · Espectros rotacionales de moléculas: niveles y reglas de selección](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md).

### Rótulo

- Un rótulo es consultada, sintética o calculada.
- Un rótulo nombra la magnitud y su unidad.

💡 **Cómo se explica en la clase [B126-C06](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md):**
- Una cifra en una presentación debe llevar: valor, unidad, año, rótulo y fuente (o su fórmula y entradas).
- *Descripción textual:* las entradas rotuladas permiten recalcular cada cifra de la presentación y compararla con lo mostrado; el resultado marca errores o cifras sin rótulo; con la simulación se agrega el rango, y todo va al anexo.
- 🎯 **Por qué importa:** [B124-C19](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) redacta propuestas de misión, no financieras. La decisión central: ¿qué cifra se muestra, con qué rótulo y con qué rango, de modo que un tercero pueda comprobarla?

📘 **Dónde se aprende** (2 clases): [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md); [B126-C06 · Presentación financiera ante inversionistas con evidencia](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md).

### Rotura de doble cadena (DSB)

- Una rotura de doble cadena (DSB) corta las dos hebras del ADN.

🎯 **Por qué importa (clase B64-C01):** La radiación ionizante rompe el ADN, y una célula muere cuando el daño supera su capacidad de reparación. La pregunta motivadora: ¿por qué dos organismos con el mismo daño inicial por gray sobreviven a dosis tan distintas?

📘 **Dónde se aprende** (1 clase): [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md).

### Rotura doble

- Una rotura doble (DSB) rompe las dos hebras del ADN; es el daño más peligroso.

🎯 **Por qué importa (clase B112-C05):** Falta la clase de mecanismos moleculares de daño y reparación. Sin ella, la diferencia de eficacia biológica entre fotones e iones pesados (B112-C01, C02) y la incertidumbre del riesgo (C04) parecen cifras arbitrarias.

📘 **Dónde se aprende** (1 clase): [B112-C05 · Daño y reparación del ADN por radiación espacial](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md).

### Rover

- Un rover es un robot móvil de superficie; un orbitador es una nave robótica en órbita.

💡 **Cómo se explica en la clase [B97-C01](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md):**
- Analogía: el orbitador es un dron que barre un campo desde arriba y el rover es una persona que camina entre los surcos.
- Un orbitador ilustrativo a `300 km` con una franja de `12 km` la cubre con 4,44 min de imagen continua; un rover que debe recorrer `5 km` con un factor de uso `0,5` tarda 16,45 días de operación.
- 🎯 **Por qué importa:** Elegir entre «ir con un rover» y «mirar desde órbita» es la primera decisión de una misión robótica, y se toma con órdenes de magnitud. Sin ellos, se prometen traslados que tardan meses o coberturas que una órbita no entrega.

📖 **Explicado a fondo:** [Rover y movilidad planetaria](esencial/ampliacion-n-z.md#rover-y-movilidad-planetaria) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B97-C01 · Robots rover y orbitadores](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md).

### Rozamiento

- El rozamiento es la fuerza de contacto paralela a la superficie que se opone al deslizamiento.

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- En un plano inclinado, un eje a lo largo de la rampa y otro perpendicular evita descomponer la normal y el rozamiento.
- Ejercicio 6. Un bloque de 20 kg en una rampa de 30° sin rozamiento: ¿qué componente del peso va a lo largo de la rampa?
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?

📘 **Dónde se aprende** (1 clase): [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md).

### RPE

- ATE: RMSE de la traslación tras alinear la estimación con la verdad por cuerpo rígido (F2). RPE: error del movimiento relativo entre pares de poses separados por una ventana (F2).

💡 **Cómo se explica en la clase [B99-C06](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md):**
- Para el RPE se mide el error del movimiento relativo entre pares de poses, y la opción de ventana fija permite comparar cada pose con otra posterior a una separación dada (en segundos, metros, radianes o cuadros), útil para estimar la deriva.
- La página no escribe las fórmulas del RMSE ni del RPE; las que siguen son las del laboratorio.
- ⚠️ **Error frecuente:** Creer que ATE bajo implica RPE bajo. El grafo bajó el ATE sin cambiar el RPE (8.5).
- 🎯 **Por qué importa:** «Mi robot deriva poco» no es una afirmación comprobable. La decisión central: ¿qué métrica, con qué alineación y con qué ventana, describe el error que importa para la tarea?

📘 **Dónde se aprende** (1 clase): [B99-C06 · Evaluación de deriva y error de trayectoria](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md).

### RPN

- El RPN es `S×O×D`.

💡 **Cómo se explica en la clase [B83-C22](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md):**
- Ejemplo: rueda de reacción, modo «fricción creciente», efecto «apuntamiento degradado», `S = 6`, `O = 5`, `D = 5`: `RPN = 150`, el mayor.
- La batería (cortocircuito de celda, `S = 9`) tiene RPN 135 y `p = 1,56 %`.
- ⚠️ **Error frecuente:** Multiplicar escalas ordinales como si fueran números exactos. Usa el RPN para priorizar, no como medida absoluta
- 🎯 **Por qué importa:** Los fallos que no se anticipan se descubren en órbita. La decisión central: ¿qué modos de fallo hay que atacar primero, cuánta probabilidad tienen en la vida de la misión y qué cambia si mejoro su detección?

📘 **Dónde se aprende** (1 clase): [B83-C22 · Análisis de modos y efectos de fallo (FMEA) en sistemas espaciales](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md).

### RPO

- El RPO es la pérdida máxima de datos aceptable, medida en tiempo.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- Con RPO de 4 h, una copia cada 1 h cumple (pérdida máxima 1 h) y cada 6 h o 24 h no.
- D["copias cada T"] --> P["perdida maxima = T vs RPO"]
- ⚠️ **Error frecuente:** Confundir RPO con RTO. El RPO es de datos y el RTO de servicio; ver sección 6.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?

📘 **Dónde se aprende** (1 clase): [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### RRW

- El RRW (*rate random walk*) `K` es la deriva aleatoria del sesgo, en `rad/s/√s`.

💡 **Cómo se explica en la clase [B87-C06](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md):**
- G["tasa medida = verdad + ARW + sesgo RRW"] --> P["promedios de duracion tau"]
- Analogía: un reloj que se adelanta con un tic aleatorio (ARW) y que además cambia de ritmo a lo largo del día (RRW): para periodos cortos domina el tic y para largos domina el cambio de ritmo.
- 🎯 **Por qué importa:** Entre dos medidas de un sensor de vector, la actitud se propaga integrando el giroscopio, y esa integración se desvía. La decisión central: ¿cada cuánto hay que corregir con otro sensor, y qué parte de la deriva es ruido blanco y cuál sesgo?

📘 **Dónde se aprende** (1 clase): [B87-C06 · Giroscopios MEMS](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md).

### RSET

- El RSET (*required safe egress time*) es el tiempo necesario: detección, reunión, traslado, paso por escotilla y verificación.

💡 **Cómo se explica en la clase [B110-C03](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md):**
- Con `N = 4` y sin varianza, `RSET = 20 + 60 + 90 + 4 × 20 + 120 = 370 s`; el laboratorio lo reproduce de forma exacta.
- Pasar de 2 a 6 personas añade `1,78 min` al RSET mediano por el cuello de botella de la escotilla y por el máximo de las reuniones.
- ⚠️ **Error frecuente:** Tomar el RSET como un número único. Es una distribución con cola larga (8.2 y 8.3).
- 🎯 **Por qué importa:** Ninguna clase anterior trata evacuación, refugio y vehículos de escape. La decisión central: ¿alcanza el margen entre ASET y RSET, y cuánto de ese margen depende de supuestos que no se conocen?

📘 **Dónde se aprende** (1 clase): [B110-C03 · Evacuación y refugio de emergencia](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md).

### RSS

- La RSS es `√Σtᵢ²`.
- El RSS suma errores independientes en cuadratura.
- El RSS (raíz de la suma de cuadrados) combina contribuyentes independientes.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B84-C16](../programa/clases/B84/B84-C16-tolerancias-de-fabricacion/CLASE.md):**
- Si D pasa a `± 0,04`: RSS `0,1382` y peor caso `0,290 mm`, que ya cumple.
- RSS o Monte Carlo cuando el proceso está controlado y se acepta un riesgo declarado.
- ⚠️ **Error frecuente:** Sumar tolerancias por RSS en funciones críticas. Se corrige con 8.4.
- 🎯 **Por qué importa:** El peor caso rechaza diseños que en la práctica funcionan y la RSS acepta riesgos que hay que cuantificar; elegir sin cálculo cuesta o dinero o fallas. La decisión central: ¿cumple el hueco del ensamble y con qué probabilidad, según el método de apilamiento?

📘 **Dónde se aprende** (4 clases): [B84-C16 · Tolerancias de fabricación](../programa/clases/B84/B84-C16-tolerancias-de-fabricacion/CLASE.md); [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md); [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md); [B90-C05 · Documentación de interfaces](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md).

### RTG

- Un RTG (*radioisotope thermoelectric generator*) convierte el calor del decaimiento en electricidad sin partes móviles.

🎯 **Por qué importa (clase B86-C16):** Un generador radioisotópico no depende de la distancia al Sol ni del eclipse, pero su potencia decae con el combustible y con los termopares y su eficiencia es baja. Entender esa curva decide qué misiones lo usan.

📘 **Dónde se aprende** (1 clase): [B86-C16 · Generadores radioisotópicos](../programa/clases/B86/B86-C16-generadores-radioisotopicos/CLASE.md).

### RTLT

- El RTLT es el tiempo de ida y vuelta de la luz.

💡 **Cómo se explica en la clase [B75-C19](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md):**
- `50,6 %` por muestreo) tiene un RTLT mayor que 30 min.
- Reacción = `RTLT + 1800 s` (sintético): `2323 s` en el mínimo, `3489 s` en el medio y `4319 s` en el máximo.
- ⚠️ **Error frecuente:** Confundir retardo unidireccional con RTLT. Se corrige con la sección 6.
- 🎯 **Por qué importa:** No se puede dirigir desde la Tierra lo que sucede en minutos. La decisión central: ¿qué eventos duran menos que el tiempo mínimo de reacción desde tierra y por tanto deben ser autónomos?

📘 **Dónde se aprende** (1 clase): [B75-C19 · Restricciones de navegación autónoma](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md).

### RTO

- El RTO es el tiempo objetivo para restablecer el servicio; el WRT es el tiempo adicional para recuperar el trabajo; el MTD es el tiempo máximo tolerable de interrupción.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- F["fallo"] --> R["recuperar el servicio: RTO"]
- *Descripción textual:* desde el fallo corren el RTO y el WRT, cuya suma no debe pasar del MTD, mientras el costo crece; el RPO limita el intervalo entre copias.
- ⚠️ **Error frecuente:** Confundir RTO con MTTR. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?

📘 **Dónde se aprende** (1 clase): [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### R-tree

- Un R-tree es un índice jerárquico de cajas.

💡 **Cómo se explica en la clase [B14-C28](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md):**
- Resultado: el R-tree devuelve 101 escenas.
- Una sola medición dio 0,27 ms con el R-tree y 0,77 ms con NumPy sobre todas las cajas.
- 🎯 **Por qué importa:** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.

📘 **Dónde se aprende** (1 clase): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md).

### Rúbrica

- La rúbrica define niveles 1 a 4 por criterio.

💡 **Cómo se explica en la clase [B124-C20](../programa/clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md):**
- Un kappa de ese orden es bajo e indica que la rúbrica o su entrenamiento necesitan afinarse; no hay umbral universal.
- Calcular un puntaje ponderado de rúbrica en escala 0–100.
- 🎯 **Por qué importa:** Un portafolio con una nota promedio alta puede ocultar una falta grave, como presentar datos inventados como reales. La decisión central: ¿qué hace falta para declarar logrado un portafolio y cómo se sabe que dos revisores miden lo mismo?

📘 **Dónde se aprende** (1 clase): [B124-C20 · Proyecto integrador y portafolio profesional](../programa/clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md).

### Rúbrica analítica

- Una rúbrica analítica puntúa cada criterio por separado; una holística, el trabajo en conjunto.

💡 **Cómo se explica en la clase [B131-C09](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md):**
- Redactar una rúbrica analítica con criterios y niveles descritos en términos observables.
- 🎯 **Por qué importa:** Una rúbrica sin acuerdo entre evaluadores asigna notas que dependen de quién corrige. La decisión central: ¿dos personas distintas darían el mismo nivel a este trabajo, y cómo lo sabes?

📘 **Dónde se aprende** (1 clase): [B131-C09 · Rúbricas de evaluación](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md).

### Rueda

- Una rueda (*wheel*) es un paquete ya compilado para una plataforma; una distribución fuente (*sdist*) es el código sin compilar.

💡 **Cómo se explica en la clase [B14-C12](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md):**
- Hay una por cada archivo descargable: la distribución fuente y una rueda por plataforma, versión de Python y arquitectura.
- sumas SHA-256 en el bloqueo: 66 (sdist + ruedas de cada plataforma)
- 🎯 **Por qué importa:** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.

📘 **Dónde se aprende** (1 clase): [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Rueda de reacción

- La rueda de reacción intercambia momento con el cuerpo.

💡 **Cómo se explica en la clase [B87-C11](../programa/clases/B87/B87-C11-ruedas-de-reaccion/CLASE.md):**
- La evidencia es la maniobra de un eje con el histórico de la rueda de reacción del ejercicio 12 (sección 20).
- B87-C11 rueda de reaccion | SINTETICO: I = diag(0.35, 0.40, 0.30) kg m^2; par max 0.01 N m, momento max 0.05 N m s, I_rueda = 5e-5 kg m^2
- 🎯 **Por qué importa:** La rueda es el actuador estándar del control fino de tres ejes. La decisión central: ¿cuánto tarda una maniobra con límites de par y de momento, y qué velocidad alcanza la rueda?

📘 **Dónde se aprende** (2 clases): [B47-C10 · Estabilidad de apuntamiento](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md); [B87-C11 · Ruedas de reacción](../programa/clases/B87/B87-C11-ruedas-de-reaccion/CLASE.md).

### Rugosidad

- La rugosidad es la desviación típica de los residuos de ese plano.
- La rugosidad es la desviación típica del residuo respecto del plano.
- Rejilla de elevación (2.5D): un valor de altura por celda (F5). Rugosidad: dispersión de la altura respecto de un plano local.

💡 **Cómo se explica en la clase [B99-C05](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md):**
- La rugosidad es la desviación típica del residuo de las medias de una ventana `3×3` respecto de su plano ajustado.
- Con umbrales de 15° y 5 cm (sintéticos) se declara traversable 96 % del interior; la roca (pendiente máxima 22,9°) queda no traversable en 8 de sus 12 celdas, por pendiente y no por rugosidad (rugosidad máxima 4,9 cm).
- 🎯 **Por qué importa:** Un mapa útil para navegar distingue lo ocupado, lo libre y lo que no se sabe, y dice si el terreno es pisable. La decisión central: ¿cómo fusionar medidas ruidosas en cada celda y qué umbrales de pendiente y rugosidad declaran un terreno traversable?

📘 **Dónde se aprende** (3 clases): [B99-C05 · Mapas de ocupación y rejillas de elevación](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md); [B102-C08 · Traversabilidad y evaluación de riesgo de terreno](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md); [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Rugosidad RMS

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B43-C23](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md):**
- Como una pared con polvo fino: la rugosidad no se ve, pero cada grano esparce un poco de luz; cuanto más corta la longitud de onda, más se nota.
- *Descripción textual:* una PSD fija la rugosidad en una banda; la TIS la convierte en luz dispersa por la fórmula escalar.
- 🎯 **Por qué importa:** La luz dispersa reduce el contraste y la reflectancia especular. La decisión central: ¿qué rugosidad RMS, en qué banda de frecuencias espaciales, deja la luz dispersa por debajo del presupuesto?

📘 **Dónde se aprende** (1 clase): [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md).

### Ruido

- El ruido es una perturbación aleatoria de las muestras.
- El ruido es la parte de la serie que no se explica con el modelo.
- El fondo (*background*) es el nivel del cielo sin fuentes; el ruido `σ` su desviación.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C11](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md):**
- Si cada muestra tiene ruido independiente de desviación `σ` y paso `Δt`, el error en la integral crece como `σ Δt √N` (no como `N`).
- La elección del método importa más que añadir ruido o decimales.
- ⚠️ **Error frecuente:** Esperar que más puntos eliminen el ruido. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.

📘 **Dónde se aprende** (9 clases): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B22-C01 · Problemas directos e inversos y mal condicionamiento](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md); [B42-C16 · Lazo de control de óptica adaptativa](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md) y 3 más.

### Ruido 1/f

- El ruido 1/f tiene más potencia a baja frecuencia.

💡 **Cómo se explica en la clase [B49-C08](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md):**
- El ruido blanco sigue `τ^(−1/2)` (la estimación de Allan con pocos intervalos tiene una incertidumbre del orden de `1/√(2n)`, hasta 12 % en `τ` largos).
- Como pesar con una balanza que se descalibra: pesar mucho rato promedia el ruido, pero la descalibración crece; hay que tarar a menudo.
- 🎯 **Por qué importa:** Integrar más tiempo no siempre mejora la medida: la deriva lo impide. La decisión central: ¿hasta qué tiempo de integración vale la pena, y cuándo hay que conmutar?

📘 **Dónde se aprende** (1 clase): [B49-C08 · Estabilidad de ganancia de receptores y variaciones de ganancia](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md).

### Ruido angular

- El centroide tiene ruido `σ_px`; el ruido angular por estrella es `σ_a = atan(σ_px/f)`.

💡 **Cómo se explica en la clase [B87-C07](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md):**
- Paso 1 · Ruido angular. `σ_a = atan(0,1/3889) = 5,30″`.
- Pasar el ruido de centroide en píxeles a ruido angular por estrella.
- 🎯 **Por qué importa:** Para apuntar un telescopio o una antena con precisión de segundos de arco, un sensor solar o un magnetómetro no bastan. La decisión central: ¿cuántas estrellas hacen falta y por qué el giro alrededor del eje óptico (balanceo) es mucho peor que el apuntamiento?

📘 **Dónde se aprende** (1 clase): [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md).

### Ruido blanco

- El ruido blanco `w[n]` es una sucesión de variables independientes, de media 0 y varianza `σ²`: no tiene memoria y su espectro es plano (el nombre viene de la luz blanca, que mezcla todas las frecuencias por igual).
- El ruido blanco `N` produce un paseo aleatorio de velocidad (VRW) con densidad `N` en `m/s/√s`.

💡 **Cómo se explica en la clase [B15-C03](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md):**
- El ruido blanco es el ruido de la lluvia sobre un techo: cada gota es independiente de la anterior.
- W["Ruido blanco<br/>w[n]"] --> A["AR(1):<br/>x = φx₋₁ + w"]
- ⚠️ **Error frecuente:** Creer que un histograma gaussiano implica ruido blanco. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una regla heredada de la física del laboratorio dice que, al promediar `N` mediciones, el error baja como `1/√N`. Esa regla solo vale si los errores de cada medición son independientes.

📘 **Dónde se aprende** (3 clases): [B15-C03 · Ruido blanco y coloreado](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md); [B80-C02 · Modelo de error de acelerómetros](../programa/clases/B80/B80-C02-modelo-de-error-de-acelerometros/CLASE.md).

### Ruido blanco de frecuencia

- El ruido blanco de frecuencia tiene muestras independientes de `y`.
- El ruido blanco de frecuencia (pendiente −1/2).
- El ruido blanco de frecuencia domina a corto plazo y el paseo aleatorio de frecuencia a largo plazo.

💡 **Cómo se explica en la clase [B13-C07](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md):**
- Tres relojes simulados tienen un ruido blanco de frecuencia (`σ = 10⁻¹²`), un paseo aleatorio de frecuencia y una deriva lineal.
- Reconocer la pendiente de la curva para ruido blanco de frecuencia (`−1/2`), paseo aleatorio (`+1/2`) y deriva lineal (`+1`).
- 🎯 **Por qué importa:** Dos relojes pueden tener la misma desviación de frecuencia media y comportarse de forma muy distinta: uno oscila alrededor de su valor y otro se aleja de él con el tiempo. La desviación típica ordinaria no sirve para describirlo, porque en un reloj con deriva no converge.

📘 **Dónde se aprende** (3 clases): [B13-C07 · Relojes atómicos y frecuencia](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md); [B46-C08 · Osciladores y estabilidad](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md); [B74-C16 · Sincronización temporal](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md).

### Ruido coloreado

- El ruido coloreado es cualquier ruido con memoria; el ruido rojo concentra su potencia en las frecuencias bajas.

💡 **Cómo se explica en la clase [B15-C03](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md):**
- Los dos primeros se parecen al ruido blanco; las variaciones lentas son ruido coloreado.
- python programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/ruido.py
- 🎯 **Por qué importa:** Una regla heredada de la física del laboratorio dice que, al promediar `N` mediciones, el error baja como `1/√N`. Esa regla solo vale si los errores de cada medición son independientes.

📘 **Dónde se aprende** (1 clase): [B15-C03 · Ruido blanco y coloreado](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md).

### Ruido de correlación

- El ruido de correlación: por parte `(S+N)/√(2M)`.

💡 **Cómo se explica en la clase [B46-C15](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md):**
- *Descripción textual:* la correlación cruzada de dos flujos con una señal común da la visibilidad, con un ruido que baja con el número de muestras.
- El script [correlador.py](correlador.py) simula la correlación, estima la visibilidad y compara FX con XF (comprueba el ruido y la coincidencia).
- 🎯 **Por qué importa:** La visibilidad es el dato básico de la imagen, y su ruido determina la sensibilidad. La decisión central: ¿cuántas muestras hay que correlacionar para fijar amplitud y fase con la precisión requerida?

📘 **Dónde se aprende** (1 clase): [B46-C15 · Correladores y visibilidades](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md).

### Ruido de disparo

- El ruido de disparo es la incertidumbre por conteo de fotones.
- El ruido de disparo es la fluctuación de Poisson.
- El ruido de disparo es la fluctuación de Poisson del número de fotones: varianza igual a la media.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C15](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md):**
- *Descripción textual:* la varianza total suma el ruido de disparo de la señal (`N`), el del cielo, el de la oscuridad y el de lectura; la SNR es la señal dividida por la raíz de esa suma.
- Su límite: la ecuación supone ruido de disparo de Poisson y lectura gaussiana, sin ruido de patrón fijo ni errores de aplanado.
- ⚠️ **Error frecuente:** Olvidar el ruido de disparo de la propia señal. Se corrige con los ejercicios 1 y 3.
- 🎯 **Por qué importa:** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.

📘 **Dónde se aprende** (5 clases): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md); [B28-C06 · Interferómetros gravitacionales](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md); [B29-C02 · Curvas de luz fotométricas](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md); [B44-C01 · Principios fotoeléctricos](../programa/clases/B44/B44-C01-principios-fotoelectricos/CLASE.md); [B48-C13 · Calibraciones nocturnas](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md).

### Ruido de etiquetas

- El ruido de etiquetas es la fracción de etiquetas incorrectas.

💡 **Cómo se explica en la clase [B17-C10](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md):**
- En el laboratorio, un modelo entrenado con etiquetas con 20 % de ruido simétrico, y evaluado con etiquetas limpias, dio 0,843, igual que uno entrenado con etiquetas limpias (0,843): el ruido simétrico apenas afectó el entrenamiento en este caso (muchos datos, un modelo simple).
- Pero la evaluación sí cambia: si se mide el modelo contra las etiquetas ruidosas, la exactitud aparente es `A(1 − η) + (1 − A)η`, con `A` la exactitud real y `η` el ruido.
- 🎯 **Por qué importa:** Se quiere entrenar un modelo que distinga galaxias espirales de elípticas. Hay un millón de imágenes y nadie las ha etiquetado.

📘 **Dónde se aprende** (1 clase): [B17-C10 · Conjuntos de datos etiquetados para aprendizaje supervisado](../programa/clases/B17/B17-C10-conjuntos-de-datos-etiquetados-para-aprendizaje-supervisado/CLASE.md).

### Ruido de fondo

- El ruido de fondo es el nivel del recinto receptor.

💡 **Cómo se explica en la clase [B109-C09](../programa/clases/B109/B109-C09-privacidad-y-espacios-personales/CLASE.md):**
- Más ruido de fondo da más privacidad (a costa de otros criterios, ver [B109-C10](../B109-C10-acustica-y-control-de-ruido-interior/CLASE.md)).
- Comparar con el ruido de fondo según un criterio de privacidad.
- 🎯 **Por qué importa:** Una división que no se ve a través pero que deja pasar cada palabra no da privacidad. La decisión central: ¿qué masa debe tener una división para que lo que se dice al otro lado quede por debajo del ruido de fondo?

📘 **Dónde se aprende** (1 clase): [B109-C09 · Privacidad y espacios personales](../programa/clases/B109/B109-C09-privacidad-y-espacios-personales/CLASE.md).

### Ruido de fotones

- El ruido de fotones relativo es `1/√N`.
- El ruido de fotones (o de disparo) es de tamaño `√N`; el criterio de Rayleigh da el límite de difracción `1,22 λ/D`.
- El ruido de fotones sigue una ley de Poisson: su varianza es igual a la señal.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B42-C14](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md):**
- A 400 fotones el ruido de lectura (`0,1375 px`) domina sobre el de fotones (`0,0449 px`).
- Ejercicio 10 · transferencia. Transferencia. Un compañero dice que más fotones siempre reducen el ruido como `1/√N`.
- 🎯 **Por qué importa:** El Shack-Hartmann es el sensor más usado en óptica adaptativa. La decisión central: ¿cuántos fotones hacen falta por subapertura para que el centroide sea preciso?

📘 **Dónde se aprende** (4 clases): [B42-C14 · Sensores Shack-Hartmann](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md); [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md); [B57-C04 · Satélites ópticos de observación](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md).

### Ruido de Johnson

- El ruido de Johnson es el ruido térmico de una resistencia.

🎯 **Por qué importa (clase B49-C07):** Cada kelvin ahorrado exige vatios en la cabeza fría, y cada vatio de carga reduce el margen. La decisión central: ¿a qué temperatura enfriar y cuánta carga admite el criostato?

📘 **Dónde se aprende** (1 clase): [B49-C07 · Criogenia y refrigeración de receptores de radio](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md).

### Ruido de lectura

- El ruido de lectura viene de la electrónica; el ruido de Poisson (de fotones), de la naturaleza discreta de la luz: su varianza es igual a la señal en electrones.
- El ruido de lectura es constante por pixel.
- El ruido de lectura es la parte aleatoria de cada lectura.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- La varianza de un píxel de cielo es: lectura `σ_L²` + fotones (`cielo + oscuro`) + el ruido del oscuro maestro, que vale `(σ_L² + oscuro)/K` si se promedian `K` oscuros.
- Ejercicio 4. En un píxel de cielo de 50 e⁻ con lectura 5 ADU, ¿domina el ruido de lectura o el de fotones?
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.

📘 **Dónde se aprende** (6 clases): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B29-C02 · Curvas de luz fotométricas](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md); [B44-C06 · Ruido de lectura](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md); [B47-C15 · Calibración a bordo](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md); [B48-C13 · Calibraciones nocturnas](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md).

### Ruido de lectura R

- El ruido de lectura `R` es el ruido del electrónico al leer cada píxel, en `e⁻` rms, independiente del tiempo.

💡 **Cómo se explica en la clase [B13-C15](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md):**
- Para verificar la fórmula, se simulan `2 × 10⁵` medidas con Poisson (señal y fondo) y ruido de lectura gaussiano: `SNR = 10,674` frente a `10,687` de la ecuación (`0,1 %` de diferencia).
- La señal llena una cubeta (el pozo); el fondo, la oscuridad y el ruido de lectura son cuatro «grifos» que añaden incertidumbre.
- ⚠️ **Error frecuente:** Pensar que muchas lecturas cortas eliminan el ruido de lectura. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.

📘 **Dónde se aprende** (1 clase): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md).

### Ruido de medición

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B42-C20):** El producto es un informe con evidencia numérica de cuánto corrige un lazo dado, con sus límites. La decisión central: ¿qué ganancia y qué ruido dan el Strehl más alto y cómo se comprueba?

📘 **Dónde se aprende** (1 clase): [B42-C20 · Laboratorio de corrección óptica simulada](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md).

### Ruido de medida

- En un lazo cerrado, la referencia `r` es lo que se desea, la salida `y` lo que se tiene, el error `e = r − H y` su diferencia, `d` una perturbación y `n` el ruido de medida.
- El ruido de medida es la variación aleatoria del sensor.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- El ruido de medida `n` llega a `θ` con la misma `T` que la referencia pero con signo contrario: el lazo sigue fielmente tanto la referencia como el ruido, por eso se filtra (C14).
- *Descripción textual:* la referencia `r` entra a un sumador que resta la medida; el error `e` alimenta al controlador `C`; su salida se suma con la perturbación `d` y entra al cuerpo `G`; la salida `y` se mide, se le suma el ruido `n` y vuelve al primer sumador.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.

📘 **Dónde se aprende** (2 clases): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md); [B116-C02 · Signos vitales: medición, interpretación y límites](../programa/clases/B116/B116-C02-signos-vitales-medicion-interpretacion-y-limites/CLASE.md).

### Ruido de partículas

- El ruido de partículas es la fluctuación estadística.

💡 **Cómo se explica en la clase [B35-C05](../programa/clases/B35/B35-C05-simulacion-de-plasmas-por-particulas-pic/CLASE.md):**
- Con pocas partículas el ruido sube y la deriva de energía crece; el método no sustituye a los códigos de investigación.
- 🎯 **Por qué importa:** Un código sin validar produce figuras bonitas y físicas falsas. La decisión central: ¿reproduce el código la frecuencia y la tasa de crecimiento conocidas?

📘 **Dónde se aprende** (1 clase): [B35-C05 · Simulación de plasmas por partículas (PIC)](../programa/clases/B35/B35-C05-simulacion-de-plasmas-por-particulas-pic/CLASE.md).

### Ruido de Poisson

- El ruido de lectura viene de la electrónica; el ruido de Poisson (de fotones), de la naturaleza discreta de la luz: su varianza es igual a la señal en electrones.
- El ruido de Poisson es la fluctuación de contar `n` objetos.
- El ruido de Poisson crece como la raíz de las cuentas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B35-C06](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md):**
- El ruido de Poisson se controla con más cuentas (`σ_V ∝ 1/√N`).
- El script [momentos.py](momentos.py) genera cuentas de Poisson y calcula momentos, ruido y sesgos (comprueba el ruido frente a `σ/√N` y el sesgo frente a la gaussiana truncada).
- ⚠️ **Error frecuente:** Ignorar el ruido de Poisson. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un momento sin su incertidumbre ni sus sesgos no es una medición. La decisión central: ¿cuántas cuentas hacen falta y qué sesgos introduce el instrumento?

📘 **Dónde se aprende** (4 clases): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B35-C06 · Mediciones in situ de plasmas espaciales](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md); [B36-C04 · Espectro de potencia de materia](../programa/clases/B36/B36-C04-espectro-de-potencia-de-materia/CLASE.md); [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md).

### Ruido de proceso

- El ruido de proceso `Q` modela lo que el modelo no sabe.
- El ruido de proceso viene de ARW y RRW (C06).

💡 **Cómo se explica en la clase [B74-C08](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md):**
- Con previa difusa y sin ruido de proceso, mínimos cuadrados recursivos y el ajuste por lotes coinciden con diferencia máxima `1,78e-10`.
- Distinguir ruido de medida `R` de ruido de proceso `Q`.
- 🎯 **Por qué importa:** Una nave en vuelo recibe medidas continuamente y necesita su estado ahora. La decisión central: ¿cuándo es el filtro equivalente al ajuste por lotes, qué añade el ruido de proceso y cómo evito que una previa errónea domine?

📘 **Dónde se aprende** (2 clases): [B74-C08 · Filtrado recursivo de estados](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md); [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md).

### Ruido del integrador

- El ruido del integrador es la diferencia entre dos ejecuciones con tolerancias muy distintas.

💡 **Cómo se explica en la clase [B23-C06](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md):**
- Esa diferencia es el ruido del integrador.
- Fijar la tolerancia de cada relación desde el ruido del integrador.
- 🎯 **Por qué importa:** El movimiento de un satélite con achatamiento terrestre (J2) no tiene solución cerrada, y tu código no tiene un valor correcto con el que compararse.

📘 **Dónde se aprende** (1 clase): [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md).

### Ruido inyectado

- El ruido inyectado por la banda.

💡 **Cómo se explica en la clase [B51-C14](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md):**
- Predecir el ruido inyectado `S_obj σ rms(1/B)/(S_cal √n)`.
- Ejercicio 2 · con una pista. Ruido inyectado con `B = 1`, `S_obj = 0,5`.
- 🎯 **Por qué importa:** Una línea débil sobre un continuo brillante solo se ve si la banda está calibrada mejor que la razón línea/continuo. La decisión central: ¿cuánto ruido inyecta la solución de banda y por qué no basta con restar un polinomio?

📘 **Dónde se aprende** (1 clase): [B51-C14 · Calibración de banda en la reducción de datos de síntesis](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md).

### Ruido kTC

- El ruido kTC es el ruido térmico de la carga al reiniciar un condensador, `√(k_B T C)/e`.

💡 **Cómo se explica en la clase [B44-C03](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md):**
- Sin CDS el ruido es `40,24 e⁻` (esperado `40,22`); con CDS, `2,85 e⁻` (esperado `√2 × 2 = 2,83`).
- R["reinicio con ruido kTC"] --> L1["lectura de reinicio"]
- ⚠️ **Error frecuente:** Pensar que el CDS elimina todo el ruido. Se corrige con 8.2.
- 🎯 **Por qué importa:** El diseño CMOS cambia el ruido y la geometría de la lectura. La decisión central: ¿qué ruido elimina el CDS y qué artefacto introduce el obturador rodante?

📘 **Dónde se aprende** (1 clase): [B44-C03 · Sensores CMOS](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md).

### Ruido rms

- El ruido rms `ΔT_rms` es la fluctuación de la medida tras integrar.

💡 **Cómo se explica en la clase [B118-C17](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md):**
- `pfd = EIRP/(4π d²) = 7,958 × 10⁻²¹ W m⁻² Hz⁻¹ = 7,958 × 10⁵ Jy` a 1000 km: unos 10⁸ veces el ruido.
- Paso 1 · Ruido. `25/√(10⁶ × 3600) = 0,417 mK`.
- ⚠️ **Error frecuente:** Esperar que más integración elimine una interferencia constante. Se corrige con 8.1: reduce el ruido, no la señal de interferencia.
- 🎯 **Por qué importa:** La radioastronomía opera en bandas donde la ITU asigna protección, pero las constelaciones numerosas y sus emisiones no deseadas pueden degradar la sensibilidad. La decisión central: ¿cuánto debe bajar una emisión para quedar por debajo del umbral de daño y de qué depende ese umbral?

📘 **Dónde se aprende** (1 clase): [B118-C17 · Interferencia radioastronómica](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md).

### Ruido rojo

- El ruido coloreado es cualquier ruido con memoria; el ruido rojo concentra su potencia en las frecuencias bajas.

💡 **Cómo se explica en la clase [B15-C03](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md):**
- El ruido rojo es el vaivén de un tren sobre una vía irregular: cada movimiento depende del anterior.
- Paso 6 · Lectura. El mismo promedio es 9 a 10 veces menos preciso con ruido rojo.
- 🎯 **Por qué importa:** Una regla heredada de la física del laboratorio dice que, al promediar `N` mediciones, el error baja como `1/√N`. Esa regla solo vale si los errores de cada medición son independientes.

📘 **Dónde se aprende** (1 clase): [B15-C03 · Ruido blanco y coloreado](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md).

### Ruina

- La ruina es una pérdida mayor que primas más capital.

💡 **Cómo se explica en la clase [B124-C08](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md):**
- *Descripción textual:* la probabilidad de falla da la pérdida esperada y la prima; la cola de pérdidas, agravada por las fallas en grupo, da la probabilidad de ruina, que se comprueba con una simulación.
- El ejemplo conductor es una cartera sintética de 20 satélites con prima total de `324,0` um y una probabilidad de ruina de `0,0439`; si los satélites vuelan de a 4 por cohete, esa probabilidad es `0,1846`.
- 🎯 **Por qué importa:** El seguro no elimina el riesgo: lo traslada a quien puede juntarlo. La decisión central: ¿cuánto cobrar por cubrir un riesgo y con qué probabilidad el asegurador se queda sin capital?

📘 **Dónde se aprende** (1 clase): [B124-C08 · Seguros y riesgo espacial](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md).

### RUL

- La RUL `= t_cruce − t_actual`.

💡 **Cómo se explica en la clase [B88-C44](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md):**
- *Descripción textual:* la serie se ajusta con un modelo exponencial; el cruce del umbral da la RUL; el remuestreo da su intervalo y la política decide si alertar.
- El ajuste da `a = 1,9958`, `b = 0,000601 /h`; la RUL estimada es `88,1` días (real `88,2`); el intervalo de remuestreo 95 % es `[86,5; 89,6]` días.
- 🎯 **Por qué importa:** Detectar una falla (C12) llega tarde para planificar; anticiparla da tiempo para actuar. La decisión central: ¿cuándo cruzará el umbral y con qué incertidumbre, para decidir si alertar?

📘 **Dónde se aprende** (1 clase): [B88-C44 · Mantenimiento predictivo y pronóstico de salud de sistemas](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md).

### Runge–Kutta de cuarto orden (RK4)

- Euler explícito: `q + h q̇`. Runge–Kutta de cuarto orden (RK4): combina cuatro evaluaciones de `q̇` por paso.

🎯 **Por qué importa (clase B10-C20):** Los giróscopos de un satélite miden la velocidad angular en ejes del cuerpo. Para saber hacia dónde apunta una cámara, hay que integrar esa velocidad en el tiempo, miles de veces.

📘 **Dónde se aprende** (1 clase): [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md).

### Ruptura

- Adsorción: retención en la superficie de un sólido. Ruptura: momento en que el lecho deja pasar el contaminante.

💡 **Cómo se explica en la clase [B106-C21](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md):**
- Usar el modelo de Yoon–Nelson para el tiempo al 10 % y 90 % de ruptura.
- La concentración a la salida (ruptura) y la caída de presión; en el modelo, el 10 % de `C₀`.
- 🎯 **Por qué importa:** Una cabina cerrada acumula trazas que no son CO₂ ni agua; hay que retirarlas con lechos y catalizadores que se saturan o dependen de la temperatura. La decisión central: ¿cuánto dura un lecho, a qué temperatura debe operar el catalizador y qué concentración queda en la cabina?

📘 **Dónde se aprende** (1 clase): [B106-C21 · Depuración de trazas gaseosas de la atmósfera de cabina](../programa/clases/B106/B106-C21-depuracion-de-trazas-gaseosas-de-la-atmosfera-de-cabina/CLASE.md).

### Ruta

- Una ruta (*path*) es la dirección de un archivo o carpeta.
- Una ruta es su dirección.

💡 **Cómo se explica en la clase [B07-C15](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md):**
- Ejemplo real de esta clase, en la carpeta C15 de un equipo Windows: bash mostró una ruta con barras `/c/dev/.../B07-C15-terminal-y-rutas-de-archivos` y PowerShell, la misma carpeta como `C:\dev\...\B07-C15-terminal-y-rutas-de-archivos`.
- Las comillas protegen espacios en rutas: `cd "Mis datos"`.
- ⚠️ **Error frecuente:** Ruta absoluta fija. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Una causa muy común de «el programa no encuentra el archivo» es que la ruta funciona en el computador del autor y no en otro: se escribió con `C:\Usuarios\ana\datos\...`, o se asumió que el programa se ejecuta desde cierta carpeta.

📘 **Dónde se aprende** (2 clases): [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md); [B14-C31 · APIs de servicios de datos](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md).

### Ruta alternativa

- La ruta alternativa es otra que no comparte pasillos con la principal.

💡 **Cómo se explica en la clase [B114-C01](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md):**
- Comprobar la existencia de una ruta alternativa que no comparte pasillos.
- No tiene ruta alternativa: es un punto único de fallo que debe señalarse en el análisis.
- ⚠️ **Error frecuente:** Suponer que una salida basta sin ruta alternativa. Se corrige con 8.3.
- 🎯 **Por qué importa:** Una salida existe en el plano, pero la evacuación depende de cuánto se tarda en llegar a ella y de qué pasa si el camino principal queda bloqueado. La decisión central: ¿cuánto tarda en salir toda la tripulación y qué ruta queda si falla la principal?

📘 **Dónde se aprende** (1 clase): [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md).

### Ruta crítica

- La ruta crítica es el camino de mayor duración; la holgura es el margen de una actividad fuera de ella.
- La ruta crítica es el camino de mayor duración.
- La ruta crítica es la cadena de pasos que fija la fecha más temprana posible.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B83-C06](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md):**
- *Descripción textual:* la función de misión se divide en hijas; sus dependencias dan la ruta crítica y las holguras, y su asignación a subsistemas da los flujos cruzados, que se convertirán en interfaces.
- La secuencia de una toma dura 655 s por la ruta crítica; las funciones de comando (F1) y calentamiento del detector (F4) tienen 88 s de holgura.
- 🎯 **Por qué importa:** Si se salta a las piezas demasiado pronto, se diseñan cosas que nadie sabe para qué sirven; si se descompone bien, se ve qué función domina el tiempo y dónde se acoplan los subsistemas. La decisión central: ¿qué funciones son críticas para el tiempo y qué subsistemas quedan más acoplados?

📘 **Dónde se aprende** (5 clases): [B83-C06 · Descomposición funcional](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md); [B90-C01 · Plan de ensamblaje e integración](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md); [B97-C13 · Ensamblaje de estructuras en órbita](../programa/clases/B97/B97-C13-ensamblaje-de-estructuras-en-orbita/CLASE.md); [B120-C06 · Caso de planificación regulatoria de un sistema satelital](../programa/clases/B120/B120-C06-caso-de-planificacion-regulatoria-de-un-sistema-satelital/CLASE.md); [B124-C16 · Planificación de cronograma y entregables](../programa/clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md).

### Ruta de evacuación

- La ruta de evacuación es el camino desde un módulo hasta una salida.

💡 **Cómo se explica en la clase [B114-C01](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *plano de evacuación sintético con tiempos*: grafo, tabla de tiempos por módulo, rutas alternativas, tiempo de cola y lista de qué es sintético y qué no se consultó.
- El script [evacuacion.py](evacuacion.py) calcula el camino mínimo con Dijkstra, lo verifica por enumeración, busca rutas alternativas y estima la cola (comprueba diferencia < 1e-9 m y que repartir en dos salidas reduce la cola).
- 🎯 **Por qué importa:** Una salida existe en el plano, pero la evacuación depende de cuánto se tarda en llegar a ella y de qué pasa si el camino principal queda bloqueado. La decisión central: ¿cuánto tarda en salir toda la tripulación y qué ruta queda si falla la principal?

📘 **Dónde se aprende** (1 clase): [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md).

### Ruta de mínima energía

- La ruta de mínima energía minimiza la suma de energías de las aristas, no la distancia.

💡 **Cómo se explica en la clase [B100-C05](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md):**
- Luna: la ruta de mínima energía cuesta `0,3597 kWh`; la de mínima distancia (`2162,6 m`) cuesta `0,3679 kWh`, un `2,28 %` más.
- *Descripción textual:* la gravedad, la masa y la pendiente de cada arista dan su fuerza y su energía; con esos costos, Dijkstra y Bellman–Ford encuentran la ruta de mínima energía y se comparan entre sí.
- 🎯 **Por qué importa:** Mover una tonelada un kilómetro cuesta energía, y esa energía depende de la gravedad, del suelo y de la pendiente. La decisión central: ¿cuánta carga y qué ruta permiten llegar con la batería disponible, y cuánto cambia el costo entre la Luna y Marte?

📘 **Dónde se aprende** (1 clase): [B100-C05 · Transporte de carga sobre superficie planetaria](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md).

### Ruta de mínimo coste

- La ruta de mínimo coste se obtiene con el algoritmo de Dijkstra.

💡 **Cómo se explica en la clase [B102-C08](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md):**
- *Descripción textual:* las elevaciones dan la pendiente y, con el plano local, la altura de obstáculo y la rugosidad; los tres forman el coste de celda y Dijkstra obtiene la ruta de mínimo coste.
- La ruta de mínimo coste entre dos puntos a `99,0 m` mide `122,4 m`, con una pendiente máxima de `18,83°`.
- 🎯 **Por qué importa:** Elegir la ruta es elegir qué riesgo se acepta. La decisión central: ¿qué celdas son intransitables, cuánto cuesta cruzar las demás y cuánto se alarga la ruta de mínimo riesgo respecto de la recta?

📘 **Dónde se aprende** (1 clase): [B102-C08 · Traversabilidad y evaluación de riesgo de terreno](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md).

### Ruze

- La ganancia es `G = η e^{−(4πσ/λ)²} (πD/λ)²`. Ruze es el factor `e^{−(4πσ/λ)²}` de pérdida por error de superficie rms `σ`.

💡 **Cómo se explica en la clase [B89-C06](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md):**
- S["sigma rms"] --> RZ["Ruze = exp(-(4 pi sigma / lambda)^2)"]
- *Descripción textual:* la ganancia ideal se corrige con Ruze y con la pérdida por apuntamiento, que depende del ancho de haz.
- 🎯 **Por qué importa:** Una antena mal apuntada o con la superficie deformada pierde decibelios que ningún amplificador recupera, y esas pérdidas crecen con la frecuencia. La decisión central: ¿qué ganancia efectiva da una antena y a qué frecuencia deja de compensar subir la frecuencia?

📘 **Dónde se aprende** (1 clase): [B89-C06 · Ganancias y pérdidas de antena](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md).
