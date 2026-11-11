# Términos · E (parte 1 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · **E** · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: **1** · [2](terminos-e-2.md) · [3](terminos-e-3.md)

### EAC

- El EAC es la estimación del costo final; el ETC, lo que falta gastar; el VAC, `BAC − EAC`.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- Si el rendimiento de costo se mantiene, `EAC = BAC/CPI = 100,63` Mum (ETC `40,63`, VAC `-20,63`), idéntico a `AC + (BAC − EV)/CPI` (error `0,0e+00`).
- Si el resto se hace según lo presupuestado, `EAC = AC + (BAC − EV) = 92,30`; si el costo depende de CPI y SPI juntos, `108,55`.
- ⚠️ **Error frecuente:** Usar un solo EAC sin explicar su supuesto. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?

📘 **Dónde se aprende** (1 clase): [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### Eb/N₀

- `C/N₀`: portadora sobre densidad de ruido. `Eb/N₀`: energía por bit sobre densidad de ruido.

💡 **Cómo se explica en la clase [B96-C27](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md):**
- *Descripción textual:* la potencia, la ganancia y las pérdidas dan la PIRE; con la pérdida en espacio libre y el ruido del receptor se obtiene `C/N₀`; restando la tasa en dB da `Eb/N₀` y el margen; la PIRE se compara con el límite autorizado.
- Paso 4 · `Eb/N₀`. `65,66 − 54,08 = 11,58 dB`.
- 🎯 **Por qué importa:** Un transmisor con potencia de más interfiere con otros y viola la licencia; con potencia de menos, no cierra el enlace. La decisión central: ¿qué potencia hace falta para un margen suficiente sin exceder el límite autorizado?

📘 **Dónde se aprende** (1 clase): [B96-C27 · Operación de equipos de radiofrecuencia en la estación](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md).

### Eb/N0 = C/N0 − 10 log₁₀ R_b

- `C/N0 = PIRE − L_total + G/T − 10 log₁₀ k` (dB-Hz). `Eb/N0 = C/N0 − 10 log₁₀ R_b`.

💡 **Cómo se explica en la clase [B89-C05](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md):**
- A 100 kbit/s, `10 log₁₀ R_b = 50 dB`: `Eb/N0 = 9,20 dB`.
- El margen actual es `-1,39 dB` (negativo: no cierra); el margen cae `20 log₁₀` de la razón de distancias, de modo que se anula a `d = 1 UA × 10^(-1,39/20) = 0,85 UA`.
- 🎯 **Por qué importa:** El presupuesto de enlace es el documento donde se decide si una misión puede transmitir; un error de 3 dB equivale a duplicar la potencia o el tamaño de la antena. La decisión central: ¿cuánto margen queda y qué tasa de datos máxima admite este enlace?

📘 **Dónde se aprende** (1 clase): [B89-C05 · Presupuesto de enlace](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md).

### Eb/N0 requerido

- El `Eb/N0` requerido es el que da una BER objetivo.

💡 **Cómo se explica en la clase [B89-C08](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md):**
- *Descripción textual:* más bits por símbolo dan una constelación más densa y una menor distancia entre puntos, lo que eleva el `Eb/N0` requerido; la simulación contrasta la BER teórica.
- Hallar el `Eb/N0` requerido para una BER objetivo por bisección.
- 🎯 **Por qué importa:** La elección de la modulación fija el `Eb/N0` requerido en el presupuesto de enlace y el ancho de banda ocupado; es la base de la codificación y la sincronización siguientes. La decisión central: ¿qué modulación da la tasa que necesito con el `Eb/N0` que mi enlace puede ofrecer?

📘 **Dónde se aprende** (1 clase): [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md).

### Ebullismo

- Psia: libras por pulgada cuadrada absolutas. Ebullismo: vaporización de fluidos corporales a baja presión.

🎯 **Por qué importa (clase B106-C03):** El cuerpo no responde a la fracción de oxígeno sino a su presión parcial; bajar la presión total exige subir la fracción, y eso trae riesgo de incendio (C17). La decisión central: ¿qué par presión–composición da normoxia dentro de los límites consultados?

📘 **Dónde se aprende** (1 clase): [B106-C03 · Composición atmosférica respirable](../programa/clases/B106/B106-C03-composicion-atmosferica-respirable/CLASE.md).

### ECEF

- La latitud geodésica `φ` es el ángulo de la normal al elipsoide con el plano ecuatorial; la longitud `λ`, el ángulo desde el meridiano origen; la altura elipsoidal `h`, la distancia a lo largo de la normal. ECEF (*Earth-centered, Earth-fixed*) designa coordenadas cartesianas terrestres.

💡 **Cómo se explica en la clase [B13-C11](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md):**
- A["(φ, λ, h)<br/>geodésicas"] -->|"N = a/√(1−e² sen²φ)"| B["(X, Y, Z)<br/>cartesianas ECEF"]
- 🎯 **Por qué importa:** Una estación terrestre transmite a un satélite; el software de seguimiento necesita su posición en X, Y, Z. El técnico de campo tiene su posición en latitud, longitud y altura.

📘 **Dónde se aprende** (1 clase): [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### ECI/ECEF

- Elevación máxima: pico de la pasada. ECI/ECEF: marcos inercial y fijo a la Tierra.

💡 **Cómo se explica en la clase [B96-C04](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md):**
- Se rota a ECEF con `θ = ωₑ t` y se calcula la elevación con el vector hacia arriba de la estación.
- O["Orbita circular ECI"] --> R["Rotacion a ECEF"]
- ⚠️ **Error frecuente:** Olvidar la rotación terrestre. Pasa de ECI a ECEF (8.2)
- 🎯 **Por qué importa:** Un contacto perdido por mala planificación no se recupera hasta la siguiente pasada, que puede estar a horas. La decisión central: ¿qué ventanas hay, cuánto duran y cuáles merece la pena usar?

📘 **Dónde se aprende** (1 clase): [B96-C04 · Planificación de contactos](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md).

### Eclipse

- Un eclipse es el alineamiento en que un cuerpo proyecta su sombra sobre otro.
- El eclipse es el tiempo en sombra; su fracción en sombra cilíndrica es `asin(R/a)/π`.
- El eclipse es el tramo de la órbita en que la Tierra tapa al Sol.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- No es la sombra de la Tierra: esa sombra solo cae sobre la Luna en un eclipse lunar, que es raro, y las fases ocurren todos los meses.
- Solo cuando la luna nueva o llena ocurre cerca de donde los dos planos se cruzan hay eclipse.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📖 **Explicado a fondo:** [Eclipse](esencial/ampliacion-a-m.md#eclipse) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (6 clases): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B02-C02 · Observación mesopotámica y egipcia](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md); [B47-C02 · Requisitos de instrumentos orbitales](../programa/clases/B47/B47-C02-requisitos-de-instrumentos-orbitales/CLASE.md); [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md); [B83-C10 · Presupuestos de energía](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md); [B96-C11 · Operación durante eclipse](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md).

### Eclipse secundario

- El eclipse secundario es el de la estrella más fría.

💡 **Cómo se explica en la clase [B29-C08](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md):**
- Ejercicio 10 · transferencia. ¿Por qué se mide también el eclipse secundario?
- Límites: ruido gaussiano, eclipses independientes, sin eclipse secundario ni variabilidad estelar.
- 🎯 **Por qué importa:** Una pequeña fracción de falsos positivos contamina cualquier muestra de planetas. Conocer qué pruebas los detectan, con qué potencia y con qué falsas alarmas, permite diseñar cribados honestos.

📘 **Dónde se aprende** (1 clase): [B29-C08 · Falsos positivos de tránsito](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md).

### Eclíptico

- El sistema ecuatorial usa el polo celeste norte y el equinoccio como origen; el eclíptico, el polo de la eclíptica y el mismo equinoccio; el galáctico, el polo norte galáctico y, como origen, la dirección con `l = 0` en el plano galáctico (el centro de la galaxia).

💡 **Cómo se explica en la clase [B04-C19](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md):**
- La cadena `ecuatorial → eclíptico → ecuatorial → galáctico` es igual a la transformación directa `ecuatorial → galáctico`: el laboratorio lo verifica para una dirección arbitraria a `10⁻¹²`.
- EQ["Ecuatorial (α, δ)<br/>vector v_eq"] -->|"R_x(ε)"| EC["Eclíptico (λ, β)"]
- 🎯 **Por qué importa:** Un catálogo da las posiciones en ecuatoriales; un estudio de la Vía Láctea necesita galácticas; un análisis del plano del sistema solar usa eclípticas. Cambiar de sistema es rutina, y un error de signo o de matriz mueve el objeto decenas de grados.

📘 **Dónde se aprende** (1 clase): [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md).

### ECLSS

- zona de desempeño: el más estrecho en el que el trabajo rutinario no se degrada por estrés térmico. ECLSS: sistema de control ambiental y soporte vital.
- ECLSS: sistema de control ambiental y soporte vital.

💡 **Cómo se explica en la clase [B106-C01](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md):**
- H --> E["ECLSS repone, recicla, evacua"]
- *Descripción textual:* la persona toma oxígeno, agua y alimento y emite CO₂, vapor, calor y residuos a la cabina; el ECLSS cierra el lazo reponiendo o reciclando.
- 🎯 **Por qué importa:** Un hábitat se diseña de adentro hacia afuera: primero lo que consume y emite la tripulación, después la máquina que lo repone. Si el balance humano está mal, todo el ECLSS queda mal dimensionado.

📖 **Explicado a fondo:** [Soporte vital (ECLSS)](esencial/tercera-f-t.md#soporte-vital-eclss) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B106-C01 · Requisitos de habitabilidad](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md); [B106-C09 · Sistemas ECLSS](../programa/clases/B106/B106-C09-sistemas-eclss/CLASE.md).

### ECM

- El ECM es el error cuadrático medio.

💡 **Cómo se explica en la clase [B74-C10](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md):**
- Ejercicio 4 · autónomo. ¿Por qué el ECM de los tres es casi igual?
- Ejercicio 12 · integrador. Integrador. Elabora tu *comparación EKF frente a UKF*: ECM y NEES de EKF, UKF y Bayes, explicación de la diferencia y límites, rotulando lo sintético.
- 🎯 **Por qué importa:** Un filtro puede dar una estimación aceptable y una covarianza falsa. La decisión central: ¿cuándo basta el EKF y cuándo la covarianza obliga a usar un filtro no lineal, y cómo lo verifico con una referencia?

📘 **Dónde se aprende** (1 clase): [B74-C10 · Filtro de Kalman no lineal](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md).

### Eco radar

- El eco radar es la señal que vuelve del objeto.

💡 **Cómo se explica en la clase [B58-C12](../programa/clases/B58/B58-C12-radar-planetario/CLASE.md):**
- Por eso el radar solo trabaja con objetos relativamente cercanos.
- Parámetros ilustrativos, sin radar real.
- ⚠️ **Error frecuente:** Creer que el radar llega lejos. Se corrige con 8.4.
- 🎯 **Por qué importa:** El radar aporta lo que la fotometría no da: tamaño directo (sin albedo) y distancias de precisión que reducen la incertidumbre orbital. La decisión central: ¿qué resolución y qué señal se obtienen de un objeto de cierto tamaño a cierta distancia?

📘 **Dónde se aprende** (1 clase): [B58-C12 · Radar planetario](../programa/clases/B58/B58-C12-radar-planetario/CLASE.md).

### Ecuación

- Una ecuación es una igualdad con una o más incógnitas.
- Una ecuación es una igualdad con una incógnita;

💡 **Cómo se explica en la clase [B03-C14](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md):**
- Todo despeje se comprueba de tres maneras: (1) sustituir la solución en la ecuación original;
- Una ecuación es una balanza equilibrada: lo que haces a un platillo debes hacerlo al otro.
- 🎯 **Por qué importa:** La fórmula de la velocidad de escape, `v = √(2GM/R)`, aparece en las fichas de la NASA como un número (11,186 km/s). Pero un ingeniero puede necesitar lo contrario: dado `v`, ¿cuál es el radio?

📖 **Explicado a fondo:** [Vis-viva (ecuación)](esencial/esencial-m-z.md#vis-viva-ecuación) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B03-C14 · Despeje de ecuaciones elementales](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md); [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md).

### Ecuación algebraica de Riccati

- El LQR es la ley `u = −K x` que minimiza `C`; se obtiene con `K = R⁻¹ Bᵀ P`, donde `P` resuelve la ecuación algebraica de Riccati `AᵀP + PA − P B R⁻¹ Bᵀ P + Q = 0` (S2 la presenta como `X A + AᴴX − X B R⁻¹ Bᴴ X + Q = 0`).

💡 **Cómo se explica en la clase [B16-C15](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md):**
- Un texto de modelado y control de naves espaciales disponible en el servidor de informes técnicos de la NASA (S1) presenta el control LQR para satélites que apuntan al nadir o a una dirección inercial: la ley es `u = −R⁻¹BᵀF x`, donde `F` resuelve la ecuación algebraica de Riccati (capítulo 9).
- Plantear la ecuación algebraica de Riccati y resolverla en un caso simple.
- 🎯 **Por qué importa:** Con un PD hay dos perillas, `Kp` y `Kd`, y no es obvio cuánto esfuerzo gasta cada combinación. En un satélite el esfuerzo tiene un costo real: energía de las ruedas, momento almacenado, desgaste.

📘 **Dónde se aprende** (1 clase): [B16-C15 · Control óptimo LQR](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md).

### Ecuación biarmónica

- La ecuación biarmónica `∇⁴w = q/D` gobierna su flexión.

💡 **Cómo se explica en la clase [B43-C03](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md):**
- Se sustituye `w(r)` en la ecuación biarmónica axisimétrica con diferencias finitas: el residuo relativo es `3,67 × 10⁻⁹`; la flecha en el borde es `0` y el momento radial en el borde, en unidades de `q a²`, `3,79 × 10⁻⁵`: se cumplen las condiciones de apoyo simple.
- Verificar una solución de placa sustituyéndola en la ecuación biarmónica.
- 🎯 **Por qué importa:** Un buen material no es el más duro ni el más estable: es el que deja el menor error de forma para una masa y un presupuesto. La decisión central: ¿qué material y qué espesor mantienen la flexión y la deriva térmica por debajo de la tolerancia?

📘 **Dónde se aprende** (1 clase): [B43-C03 · Materiales para espejos](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md).

### Ecuación característica

- Los autovalores son las raíces de la ecuación característica `det(A − λI) = 0` (S1, 1.2.71); el polinomio correspondiente es el polinomio característico.
- La ecuación característica de la linealización plana es `λ⁴ + (4 − Ω_xx − Ω_yy)λ² + (Ω_xxΩ_yy − Ω_xy²) = 0`, una cuadrática en `λ²`.
- La ecuación característica del plano es `λ⁴ + (2 − c2) λ² + (1 + 2 c2)(1 − c2) = 0`.

💡 **Cómo se explica en la clase [B10-C08](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md):**
- Ecuación característica: exacta para `2×2` y `3×3`.
- Calcular autovalores de una matriz `2×2` con la ecuación característica.
- 🎯 **Por qué importa:** Un satélite que rota libremente no gira igual alrededor de cualquier eje: tiene tres ejes especiales —los ejes principales de inercia— en los que la rotación es simple. Conocerlos permite diseñar su estabilización, decidir dónde colocar instrumentos sensibles al giro y entender por qué ciertos giros se desestabilizan.

📘 **Dónde se aprende** (3 clases): [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B73-C04 · Estabilidad local de Lagrange](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md); [B76-C04 · Órbitas halo](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md).

### Ecuación cinemática del cuaternión

- La ecuación cinemática del cuaternión (con rotación activa cuerpo → inercial y `ω` en el cuerpo) es `q̇ = ½ q ⊗ (0, ω)`.

💡 **Cómo se explica en la clase [B10-C20](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md):**
- Escribir la ecuación cinemática del cuaternión y deducir `ω = 2 q* ⊗ q̇`.
- 🎯 **Por qué importa:** Los giróscopos de un satélite miden la velocidad angular en ejes del cuerpo. Para saber hacia dónde apunta una cámara, hay que integrar esa velocidad en el tiempo, miles de veces.

📘 **Dónde se aprende** (1 clase): [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md).

### Ecuación de Adler

- Sol marciano: día solar de Marte. Ecuación de Adler: `dδ/dt = Δω − ε sin δ`.

💡 **Cómo se explica en la clase [B106-C13](../programa/clases/B106/B106-C13-iluminacion-y-ciclos-circadianos/CLASE.md):**
- Describir el arrastre de un oscilador por una señal periódica (ecuación de Adler).
- 🎯 **Por qué importa:** El reloj interno no mide exactamente 24 h; la luz lo corrige. Un hábitat con otra duración de día pide programar la luz.

📘 **Dónde se aprende** (1 clase): [B106-C13 · Iluminación y ciclos circadianos](../programa/clases/B106/B106-C13-iluminacion-y-ciclos-circadianos/CLASE.md).

### Ecuación de Arrhenius

- La ecuación de Arrhenius dice ```text k = A_f · exp(−E_a / (R T)) ``` con `A_f` el factor preexponencial (en 1/s para primer orden), `R` la constante de los gases y `T` la temperatura en kelvin.
- La ecuación de Arrhenius da `k(T) = k_ref exp[−Ea/R (1/T − 1/T_ref)]`.

💡 **Cómo se explica en la clase [B06-C14](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md):**
- Con la ecuación de Arrhenius y una barrera de 50 kJ/mol (valor sintético), una reacción que a 300 K tiene vida media de 0,35 s no ocurriría a 10 K en ninguna escala de tiempo: su vida media sería de 10²⁵² segundos.
- Aplicar la ecuación de Arrhenius para comparar velocidades a dos temperaturas.
- 🎯 **Por qué importa:** Que una reacción sea posible (energía favorable, `K` grande) no significa que ocurra: puede ser tan lenta que no ocurra nunca en la edad del universo. En una nube molecular a 10 K, la energía térmica es de apenas 0,86 meV (C10).

📘 **Dónde se aprende** (2 clases): [B06-C14 · Cinética química inicial](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md); [B100-C04 · Almacenamiento remoto y depósitos de suministros](../programa/clases/B100/B100-C04-almacenamiento-remoto-y-depositos-de-suministros/CLASE.md).

### Ecuación de Barker

- La ecuación de Barker da el tiempo desde el pericentro en una parábola.

💡 **Cómo se explica en la clase [B25-C12](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md):**
- Calcular el tiempo de una aproximación parabólica con la ecuación de Barker.
- 🎯 **Por qué importa:** Las galaxias no evolucionan aisladas: se atraen, se deforman y a veces se funden. Muchas elípticas masivas pueden provenir de fusiones, y los encuentros llevan gas al centro, alimentando la formación estelar y los núcleos activos de C11.

📘 **Dónde se aprende** (1 clase): [B25-C12 · Interacciones y fusiones galácticas](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md).

### Ecuación de Bernoulli

- La ecuación de Bernoulli `p + ½ ρ u² = constante` vale a lo largo de una línea de corriente en flujo estacionario, no viscoso e incompresible.

💡 **Cómo se explica en la clase [B79-C02](../programa/clases/B79/B79-C02-ecuaciones-de-euler-para-flujo-no-viscoso/CLASE.md):**
- *Descripción textual:* de la continuidad sale la velocidad en cada sección; la ecuación de momento integrada da Bernoulli, que se contrasta con una integración numérica y se usa para inferir la velocidad de entrada.
- Verificar Bernoulli con una integración numérica independiente de la ecuación de momento.
- 🎯 **Por qué importa:** Las ecuaciones de flujo ideal son la base del análisis de toberas y del reconocimiento de cuándo la viscosidad importa. Sin Euler no se sabe qué ignora cada modelo posterior.

📘 **Dónde se aprende** (1 clase): [B79-C02 · Ecuaciones de Euler para flujo no viscoso](../programa/clases/B79/B79-C02-ecuaciones-de-euler-para-flujo-no-viscoso/CLASE.md).

### Ecuación de Boltzmann

- La ecuación de Boltzmann da la fracción de átomos en un nivel excitado: `n₂/n₁ = (g₂/g₁) exp(−ΔE/kT)`, con `g` los pesos estadísticos.
- La ecuación de Boltzmann `n₂/n₁ = (g₂/g₁) e^(−ΔE/kT)`.

💡 **Cómo se explica en la clase [B24-C10](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md):**
- Aplicar la ecuación de Boltzmann a poblaciones de niveles.
- 🎯 **Por qué importa:** La intensidad de una línea espectral no crece simplemente con la temperatura: depende de cuántos átomos están en el nivel adecuado y de cuántos están ionizados. Por eso un mismo elemento domina en estrellas de temperaturas muy distintas.

📘 **Dónde se aprende** (3 clases): [B24-C10 · Espectros y clasificación estelar](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md); [B32-C02 · Equilibrio termodinámico local y desviaciones no LTE](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md); [B45-C14 · Composición química por espectros](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md).

### Ecuación de Clausius–Clapeyron

- La ecuación de Clausius–Clapeyron describe la curva de equilibrio entre una fase condensada y el vapor si la entalpía de cambio de fase `ΔH` es constante y el vapor es ideal: ```text ln(P / P_tp) = −(ΔH / R) (1/T − 1/T_tp) ``` con `R` la constante molar de los gases (C09) y `(T_tp, P_tp)` el punto triple.
- La ecuación de Clausius–Clapeyron relaciona la presión de saturación con la temperatura: `d ln e_s/dT = L/(R_v T²)`.

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- Usar la ecuación de Clausius–Clapeyron para obtener una temperatura a otra presión.
- ⚠️ **Error frecuente:** Usar °C en la ecuación de Clausius–Clapeyron. Debe ser kelvin; se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.

📘 **Dónde se aprende** (2 clases): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md); [B54-C08 · Nubes y aerosoles](../programa/clases/B54/B54-C08-nubes-y-aerosoles/CLASE.md).

### Ecuación de crecimiento

- La ecuación de crecimiento (en `x = ln a`) es `δ_xx + (2 + dlnE/dlna) δ_x − (3/2)Ω_m/(a³E²) δ = 0`.

💡 **Cómo se explica en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- Escribir la ecuación de crecimiento lineal.
- El script [crecimiento.py](crecimiento.py) integra la ecuación de crecimiento en `ln a`, comprueba `δ = a` en EdS (`10⁻⁸`) y que la ODE coincide con la integral de crecimiento (`10⁻⁵`); calcula `D_C` y comprueba la solución de EdS (`10⁻⁹`).
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.

📘 **Dónde se aprende** (1 clase): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md).

### Ecuación de Darcy–Weisbach

- La ecuación de Darcy–Weisbach da la velocidad media `u = √(8 g R_h S / f)`.

💡 **Cómo se explica en la clase [B66-C01](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md):**
- Con Manning y `n = R_h^(1/6) √(f/(8g))`, la diferencia relativa máxima con Darcy–Weisbach es `1,58 × 10⁻¹⁶`: son la misma ecuación escrita de otra forma, de modo que la comprobación valida el código, no la física.
- 🎯 **Por qué importa:** Un valle visto desde órbita no dice por sí solo cuánta agua (o metano) pasó por él. La decisión central: ¿cuánto caudal transporta un canal de la misma geometría en otro cuerpo, y qué cambia además del caudal?

📘 **Dónde se aprende** (1 clase): [B66-C01 · Valles y canales: morfología y origen en superficies planetarias](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md).

### Ecuación de estado

- La ecuación de estado es `P(ρ)`.
- La ecuación de estado `w = p/ρ` de la energía oscura vale `−1` para una constante cosmológica.
- La ecuación de estado (EOS) liga `P` con `ρ`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B26-C19](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md):**
- Leer una restricción publicada sobre la ecuación de estado `w`.
- 🎯 **Por qué importa:** La aceleración cósmica se descubrió porque las supernovas Ia lejanas aparecían más débiles de lo esperado. Para reproducir ese razonamiento hay que saber calcular la distancia de luminosidad y ver cuánto cambia con el contenido del universo.

📘 **Dónde se aprende** (4 clases): [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md); [B27-C02 · Enanas blancas y límite de Chandrasekhar](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md); [B27-C03 · Estrellas de neutrones](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md); [B40-C06 · Campos escalares en cosmología: potenciales y evolución](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md).

### Ecuación de Frantz–Nodvik

- La ecuación de Frantz–Nodvik da la energía de salida de un amplificador de pulsos.

🎯 **Por qué importa (clase B92-C01):** Un enlace óptico se dimensiona con fotones, no con vatios. La decisión central: ¿cuánta potencia de pico y cuánta energía por pulso debe entregar la fuente para una potencia media dada, y hasta dónde sirve aumentar la ganancia del amplificador?

📘 **Dónde se aprende** (1 clase): [B92-C01 · Fuentes láser y amplificadores para enlaces espaciales](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md).

### Ecuación de Friedmann

- La ecuación de Friedmann (plano) es `H² = H₀²(Ω_m a⁻³ + Ω_Λ)`, con `Ω_Λ = 1 − Ω_m`.

💡 **Cómo se explica en la clase [B26-C13](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md):**
- Escribir la ecuación de Friedmann para un universo plano.
- 🎯 **Por qué importa:** La edad del universo, la distancia a una galaxia y el calendario de su historia salen de la ecuación de Friedmann. Con ella se interpreta cualquier parámetro cosmológico.

📘 **Dónde se aprende** (1 clase): [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md).

### Ecuación de Gauss

- La ecuación de Gauss da la variación de los elementos por una fuerza perturbadora; para una órbita circular, `da/dt = 2 a_T / n`.

💡 **Cómo se explica en la clase [B58-C14](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md):**
- Aplicar la ecuación de Gauss a una aceleración tangencial.
- 🎯 **Por qué importa:** Una deriva de decenas de kilómetros en un siglo puede decidir si un acercamiento ocurre. La decisión central: ¿cuánto se desplaza un asteroide por empuje térmico y por qué los cuerpos pequeños son más sensibles?

📘 **Dónde se aprende** (1 clase): [B58-C14 · Efectos Yarkovsky y YORP](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md).

### Ecuación de Jeans

- La ecuación de Jeans relaciona el gradiente de presión del sistema con la gravedad; el virial relaciona energías.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- Si el sistema es isótropo y está en equilibrio, la ecuación de Jeans `d(ρσ²)/dr = −ρ GM(<r)/r²` tiene solución `σ²(r) = GM/(6√(r² + a²))` para el perfil de Plummer.
- *Descripción textual:* de la masa y la escala se obtiene la densidad; de ella, la dispersión por la ecuación de Jeans; el virial comprueba el equilibrio; el tiempo dinámico y la relajación dan las escalas temporales.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Ecuación de Jeffreys

- La ecuación de Jeffreys para la velocidad media es `ū = ρ g h² sin α/(3η)`.

🎯 **Por qué importa (clase B53-C11):** La forma de un edificio volcánico delata la reología de la lava y la gravedad del cuerpo. La decisión central: ¿cómo cambian la velocidad, el espesor y el largo de una colada al cambiar de planeta?

📘 **Dónde se aprende** (1 clase): [B53-C11 · Vulcanismo extraterrestre](../programa/clases/B53/B53-C11-vulcanismo-extraterrestre/CLASE.md).

### Ecuación de Kepler

- La anomalía excéntrica `E` es un ángulo auxiliar que cumple la ecuación de Kepler, `M = E − e sen E`.
- La ecuación de Kepler `M = E − e sin E`.

💡 **Cómo se explica en la clase [B02-C14](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md):**
- *Descripción textual:* con `a`, `e` y `T` se calcula la anomalía media en cada instante; se resuelve la ecuación de Kepler para hallar la anomalía excéntrica; de ella salen las coordenadas; y se comprueban las leyes de las áreas y del período.
- Resolver la ecuación de Kepler para obtener una posición.
- 🎯 **Por qué importa:** Para Kepler, como para todos antes, el círculo era la figura natural del cielo. Los datos de Tycho no se dejaban describir con círculos.

📖 **Explicado a fondo:** [Anomalía y ecuación de Kepler](esencial/tercera-a-e.md#anomalía-y-ecuación-de-kepler) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md); [B29-C03 · Velocidad radial estelar](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md).

### Ecuación de la lente

- La ecuación de la lente liga la posición angular real de la fuente `β` con la de la imagen `θ`.

💡 **Cómo se explica en la clase [B25-C14](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md):**
- *Descripción textual:* de la masa y las distancias se obtiene el radio de Einstein; con la posición de la fuente se resuelve la ecuación de la lente (dos imágenes) y se calcula la magnificación; a la inversa, de un anillo medido se deduce la masa interior.
- Comprueba que la bisección de la ecuación de la lente coincide con la forma cerrada (`10⁻⁹`), que la magnificación calculada con la derivada numérica coincide con `(u² + 2)/(u√(u² + 4))` para cuatro valores de `u` (`10⁻⁶`) y que la masa proyectada de Einstein de la SIS coincide con `πσ²R_E/G` (`10⁻⁹`).
- 🎯 **Por qué importa:** La luz de una galaxia lejana se curva al pasar cerca de una masa, y la masa interior se deduce del tamaño de la distorsión sin importar si es luminosa u oscura ni si está en equilibrio. Por eso las lentes son una prueba directa de la distribución de masa.

📘 **Dónde se aprende** (1 clase): [B25-C14 · Lentes gravitacionales galácticas](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md).

### Ecuación de la órbita

- La ecuación de la órbita para `u = 1/r` en la métrica de Schwarzschild es `u'' + u = GM/h² + 3GMu²/c²`, con `' = d/dφ`.

💡 **Cómo se explica en la clase [B26-C08](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md):**
- Escribir la ecuación de la órbita en Schwarzschild.
- No: el cuerpo sigue una geodésica; la diferencia con Newton aparece en el término extra de la ecuación de la órbita, no en una fuerza adicional.
- 🎯 **Por qué importa:** Calcular una trayectoria de una nave o un planeta con precisión de arcosegundos exige saber cuándo la mecánica newtoniana deja de ser suficiente. La precesión del perihelio es la manifestación más simple de esa diferencia.

📘 **Dónde se aprende** (1 clase): [B26-C08 · Geodésicas gravitacionales](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md).

### Ecuación de la red

- La ecuación de la red `mλ = d(sin α + sin β)`.

💡 **Cómo se explica en la clase [B45-C04](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md):**
- Paso 1 · Ecuación. `sin β = λ/d − sin α`.
- ⚠️ **Error frecuente:** Olvidar el ángulo de incidencia en la ecuación. Se corrige con 8.1.
- 🎯 **Por qué importa:** La red es el elemento dispersor de casi todos los espectrógrafos. La decisión central: ¿en qué ángulo sale cada longitud de onda y qué resolución se obtiene?

📘 **Dónde se aprende** (1 clase): [B45-C04 · Redes de difracción](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md).

### Ecuación de Lane–Emden

- La ecuación de Lane–Emden describe un politropo: `θ'' + 2θ'/ξ + θⁿ = 0`.
- La ecuación de Lane–Emden describe su estructura con variables adimensionales `θ` y `ξ`.
- La ecuación de Lane–Emden `θ″ + 2θ′/ξ + θⁿ = 0` describe un politropo `P ∝ ρ^{1+1/n}`.

💡 **Cómo se explica en la clase [B24-C14](../programa/clases/B24/B24-C14-asterosismologia-inicial/CLASE.md):**
- Resolver la ecuación de Lane–Emden y verificar el solver con soluciones analíticas.
- 🎯 **Por qué importa:** La asterosismología es la única manera de «ver» el interior de estrellas lejanas: da densidad media, masa y radio con una precisión que la fotometría y la espectroscopía no alcanzan, y distingue si una gigante quema hidrógeno en capa o helio en el núcleo.

📘 **Dónde se aprende** (3 clases): [B24-C14 · Asterosismología inicial](../programa/clases/B24/B24-C14-asterosismologia-inicial/CLASE.md); [B30-C01 · Estructura interna del Sol](../programa/clases/B30/B30-C01-estructura-interna-del-sol/CLASE.md); [B37-C04 · Condiciones de frontera centrales y superficiales en modelos estelares](../programa/clases/B37/B37-C04-condiciones-de-frontera-centrales-y-superficiales-en-modelos-estelares/CLASE.md).

### Ecuación de Manning

- La ecuación de Manning la expresa con un coeficiente `n`.
- La ecuación de Manning relaciona caudal, geometría, pendiente y rugosidad.

💡 **Cómo se explica en la clase [B66-C01](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md):**
- Con Manning y `n = R_h^(1/6) √(f/(8g))`, la diferencia relativa máxima con Darcy–Weisbach es `1,58 × 10⁻¹⁶`: son la misma ecuación escrita de otra forma, de modo que la comprobación valida el código, no la física.
- Manning es la misma ecuación reescrita, no una validación independiente de la física.
- 🎯 **Por qué importa:** Un valle visto desde órbita no dice por sí solo cuánta agua (o metano) pasó por él. La decisión central: ¿cuánto caudal transporta un canal de la misma geometría en otro cuerpo, y qué cambia además del caudal?

📘 **Dónde se aprende** (2 clases): [B66-C01 · Valles y canales: morfología y origen en superficies planetarias](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md); [B115-C01 · Cultivos hidropónicos para hábitats](../programa/clases/B115/B115-C01-cultivos-hidroponicos-para-habitats/CLASE.md).

### Ecuación de medida

- La ecuación de medida (RIME) en su forma escalar.

🎯 **Por qué importa (clase B51-C03):** Sin ganancias el conjunto de datos no sirve para formar imágenes. La decisión central: ¿cómo se estiman las ganancias a partir de un modelo de cielo conocido y qué precisión se alcanza?

📘 **Dónde se aprende** (1 clase): [B51-C03 · Ganancias complejas por antena y soluciones de calibración](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md).

### Ecuación de Mifflin–St Jeor

- La ecuación de Mifflin–St Jeor estima el metabolismo basal: `10 w + 6,25 h − 5 a + 5` (hombre) o `−161` (mujer), en kcal/día, con `w` en kg, `h` en cm, `a` en años (recordada por el autor; no consultada aquí).

🎯 **Por qué importa (clase B105-C12):** Cada kilogramo de alimento que se lanza cuesta; cada kilocaloría que falta se paga con masa corporal. La decisión central: ¿cuánto alimento hay que transportar para una misión y con qué margen frente a la incertidumbre del gasto?

📘 **Dónde se aprende** (1 clase): [B105-C12 · Nutrición espacial](../programa/clases/B105/B105-C12-nutricion-espacial/CLASE.md).

### Ecuación de Miles

- La ecuación de Miles da `g_rms = √(π/2 · f_n Q · ASD(f_n))` y supone ASD plana cerca de `f_n` y `Q` alto.
- Transmisibilidad: cociente respuesta/entrada en función de la frecuencia. Ecuación de Miles: aproximación de la respuesta rms para un oscilador de banda estrecha con PSD plana.

💡 **Cómo se explica en la clase [B84-C11](../programa/clases/B84/B84-C11-vibraciones-y-resonancias/CLASE.md):**
- Aplicar la ecuación de Miles `g_rms = √(π/2 f_n Q ASD(f_n))`.
- 🎯 **Por qué importa:** Un equipo con `Q = 10` en resonancia recibe 10 veces la aceleración de entrada; Miles da la respuesta rms en una línea.

📘 **Dónde se aprende** (2 clases): [B84-C11 · Vibraciones y resonancias](../programa/clases/B84/B84-C11-vibraciones-y-resonancias/CLASE.md); [B90-C09 · Ensayos de vibración](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md).

### Ecuación de Navier–Stokes

- La ecuación de Navier–Stokes unidireccional es `ρ ∂u/∂t = −dp/dx + μ ∂²u/∂y²`.

💡 **Cómo se explica en la clase [B79-C03](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md):**
- python programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/couette_poiseuille.py
- 🎯 **Por qué importa:** Casi todo flujo de ingeniería tiene paredes, y en ellas la viscosidad impone velocidad cero. Sin Navier–Stokes no hay arrastre ni fricción ni calentamiento por pared.

📘 **Dónde se aprende** (1 clase): [B79-C03 · Ecuaciones de Navier-Stokes](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md).

### Ecuación de onda

- La ecuación de onda es `∂²u/∂t² = c² ∂²u/∂x²`, donde `u(x, t)` es el desplazamiento y `c` la velocidad de la onda.

💡 **Cómo se explica en la clase [B21-C02](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md):**
- *Descripción textual:* de la ecuación continua se pasa a una malla; el esquema de salto de rana se escribe con tres niveles de tiempo; al probar ondas senoidales se obtiene la relación de dispersión discreta, de la que se leen la velocidad de fase numérica y el límite de estabilidad.
- El modelo es la ecuación de onda de una cuerda tensa de densidad uniforme, una idealización de lo que ocurre a lo largo del campo.
- 🎯 **Por qué importa:** Casi toda señal que viaja en el espacio —ondas de radio, ondas de Alfvén en la corona solar, ondas sísmicas en una luna, vibraciones de una estructura— obedece alguna forma de la ecuación de onda.

📘 **Dónde se aprende** (1 clase): [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md).

### Ecuación de Poisson

- La ecuación de Poisson es `∇²φ = s` con `∇²φ = ∂²φ/∂x² + ∂²φ/∂y²` y `s` una fuente conocida.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- Plantear la ecuación de Poisson con condiciones de frontera de Dirichlet y discretizarla con el estencil de cinco puntos.
- python programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/poisson_relajacion_multigrid.py
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Ecuación de prueba

- La ecuación de prueba es `y′ = λ y`, con `λ` complejo; su solución es `e^{λ t}`, que decae si `Re λ < 0`.

💡 **Cómo se explica en la clase [B11-C09](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md):**
- A["Ecuación de prueba<br/>y′ = λ y"] --> B["Método de un paso<br/>y_{k+1} = R(hλ) y_k"]
- *Descripción textual:* la ecuación de prueba reduce cada paso a una multiplicación por `R(hλ)`; si su módulo es menor o igual que uno el método es estable y se pasa a comprobar la precisión; si no, hay que reducir el paso o cambiar a un método implícito.
- 🎯 **Por qué importa:** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.

📘 **Dónde se aprende** (1 clase): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md).

### Ecuación de Riccati

- La ecuación de Riccati da la covarianza estacionaria del filtro.
- La ecuación de Riccati da la varianza estacionaria del filtro `P`.

💡 **Cómo se explica en la clase [B15-C17](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md):**
- Con el modelo de 8.1, la covarianza de predicción converge a una matriz fija, solución de la ecuación de Riccati: `P⁻ = [[5,533; 0,553],[0,553; 0,105]]`, con ganancia `K = [0,1812; 0,0181]`.
- Comprobar el filtro contra la media aritmética y contra la ecuación de Riccati.
- 🎯 **Por qué importa:** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.

📘 **Dónde se aprende** (2 clases): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B102-C03 · Deslizamiento y estimación de patinaje](../programa/clases/B102/B102-C03-deslizamiento-y-estimacion-de-patinaje/CLASE.md).

### Ecuación de Saha

- La ecuación de Saha da la fracción de átomos ionizados, función de `T` y de la presión electrónica `P_e`.
- La ecuación de Saha relaciona los iones con los neutros y la densidad de electrones.

💡 **Cómo se explica en la clase [B24-C10](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md):**
- Aplicar la ecuación de Saha a la ionización.
- 🎯 **Por qué importa:** La intensidad de una línea espectral no crece simplemente con la temperatura: depende de cuántos átomos están en el nivel adecuado y de cuántos están ionizados. Por eso un mismo elemento domina en estrellas de temperaturas muy distintas.

📘 **Dónde se aprende** (3 clases): [B24-C10 · Espectros y clasificación estelar](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md); [B32-C02 · Equilibrio termodinámico local y desviaciones no LTE](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md); [B45-C14 · Composición química por espectros](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md).

### Ecuación de Sellmeier

- La ecuación de Sellmeier `n² − 1 = Σ B_i λ²/(λ² − C_i)`.
- La ecuación de Sellmeier `n² = 1 + Σ Bᵢλ²/(λ² − Cᵢ)`.

💡 **Cómo se explica en la clase [B43-C21](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md):**
- Evaluar la ecuación de Sellmeier de dos vidrios.
- 🎯 **Por qué importa:** Un telescopio refractor o un corrector necesita vidrios que compensen el color. La decisión central: ¿qué par de vidrios, con qué potencias, anula el cromatismo primario de un doblete y qué error aporta la falta de homogeneidad?

📘 **Dónde se aprende** (2 clases): [B43-C21 · Selección de vidrios ópticos: catálogos, homogeneidad y diagramas](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md); [B45-C05 · Prismas y dispersión](../programa/clases/B45/B45-C05-prismas-y-dispersion/CLASE.md).

### Ecuación de Tsiolkovsky

- La ecuación de Tsiolkovsky relaciona Δv y masa de propelente.

💡 **Cómo se explica en la clase [B118-C07](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md):**
- Calcular el combustible con la ecuación de Tsiolkovsky.
- 🎯 **Por qué importa:** La evasión es la respuesta operativa a una conjunción, pero cada maniobra cuesta combustible y vida útil. La decisión central: ¿cuánto Δv hace falta para lograr una separación dada y cuánto más cuesta decidir tarde?

📘 **Dónde se aprende** (2 clases): [B47-C19 · Mantenimiento y vida útil](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md); [B118-C07 · Estrategias de evasión](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md).

### Ecuación de van der Waals

- La ecuación de van der Waals es un modelo sencillo con dos parámetros, `a` (atracción) y `b` (volumen propio).

🎯 **Por qué importa (clase B06-C09):** La NASA publica para Marte, Venus y la Tierra la presión y la temperatura medias en la superficie, la gravedad, el peso molecular de la atmósfera y su densidad (S1, S2, S3). ¿Puedes reproducir esa densidad con sólo lo anterior?

📘 **Dónde se aprende** (1 clase): [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md).

### Ecuación del calor

- La ecuación del calor es `ρ c ∂T/∂t = k ∂²T/∂x²`.

🎯 **Por qué importa (clase B77-C16):** La temperatura de la cara trasera es la que decide si la estructura sobrevive. La decisión central: ¿cuánto del calor entrante se re-radia, cuánto se almacena y cuánto sube la temperatura trasera con un espesor dado?

📘 **Dónde se aprende** (1 clase): [B77-C16 · Protección térmica](../programa/clases/B77/B77-C16-proteccion-termica/CLASE.md).

### Ecuación del CCD

- La ecuación del CCD es `S/N = S/√(S + n(B + D + RN²))`.

💡 **Cómo se explica en la clase [B45-C19](../programa/clases/B45/B45-C19-reduccion-e-incertidumbre-instrumental/CLASE.md):**
- Estimar el cielo añade error y baja el S/N un `5,8 %`; el Monte Carlo queda `3,2 %` por debajo de esa ecuación.
- *Descripción textual:* los calibrados dan ganancia y ruido de lectura y estos alimentan la ecuación del CCD que predice el S/N.
- 🎯 **Por qué importa:** Un flujo sin incertidumbre no es una medida. La decisión central: ¿qué términos dominan el ruido y cómo se estiman ganancia y ruido de lectura?

📘 **Dónde se aprende** (1 clase): [B45-C19 · Reducción e incertidumbre instrumental](../programa/clases/B45/B45-C19-reduccion-e-incertidumbre-instrumental/CLASE.md).

### Ecuación del centro

- La ecuación del centro es `ν − M` como función de `M`.

💡 **Cómo se explica en la clase [B71-C13](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md):**
- Paso 3 · Resultado. `ν = 100,6526°`; la ecuación del centro vale `10,6526°`, cerca de `2e sin M = 10,7°`.
- Evaluar la ecuación del centro `ν − M ≈ 2e sin M + 1,25 e² sin 2M` y su error.
- 🎯 **Por qué importa:** Confundir una anomalía con otra es el error más común al propagar órbitas. La decisión central: ¿cómo conviertes entre `ν`, `E` y `M` sin ambigüedad y cuánto difieren cuando `e` es grande?

📘 **Dónde se aprende** (1 clase): [B71-C13 · Anomalías orbitales](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md).

### Ecuación del cohete

- La ecuación del cohete es `Δv = g₀ Isp ln(m₀/m_f)`.
- La ecuación del cohete liga Δv y masas: `m₀/m_f = exp(Δv/(Isp g₀))`.
- La ecuación del cohete relaciona el Δv con el `Isp` y la razón de masas `m₀/m_f`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B56-C20](../programa/clases/B56/B56-C20-diseno-de-mision-astrobiologica-conceptual/CLASE.md):**
- Definir requisito, criterio de verificación, Δv de Hohmann y ecuación del cohete.
- Calcular la masa de propelente con la ecuación del cohete.
- 🎯 **Por qué importa:** Una misión que busca vida combina ciencia, ingeniería y protección planetaria. Para decidir si es viable hay que traducir la pregunta científica en requisitos y comprobar que el presupuesto cierra.

📖 **Explicado a fondo:** [Ecuación del cohete (Tsiolkovski)](esencial/esencial-d-l.md#ecuación-del-cohete-tsiolkovski) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B56-C20 · Diseño de misión astrobiológica conceptual](../programa/clases/B56/B56-C20-diseno-de-mision-astrobiologica-conceptual/CLASE.md); [B78-C02 · Propulsión química como sistema físico](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md); [B83-C09 · Presupuestos de masa](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md); [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Ecuación del fabricante

- La ecuación del fabricante `1/f = (n−1)(1/R₁−1/R₂)`.

💡 **Cómo se explica en la clase [B41-C05](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md):**
- Calcular `f` con la ecuación del fabricante.
- 🎯 **Por qué importa:** El objetivo de un refractor es una lente. La decisión central: ¿cuánto se equivoca la fórmula de lente delgada cuando la lente es gruesa?

📘 **Dónde se aprende** (1 clase): [B41-C05 · Lentes delgadas y gruesas](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md).

### Ecuación del gas alveolar

- La ecuación del gas alveolar es `PAO₂ = FiO₂ (Pb − PH₂O) − PaCO₂/R`.

💡 **Cómo se explica en la clase [B105-C21](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md):**
- *Descripción textual:* la presión y la fracción de oxígeno de la cabina dan la presión inspirada; la ventilación y el CO₂ ambiente fijan el CO₂ alveolar; la ecuación del gas alveolar combina ambos para dar el oxígeno alveolar.
- Calcular la presión inspirada `PIO₂ = FiO₂ (Pb − PH₂O)` y la alveolar `PAO₂` con la ecuación del gas alveolar.
- 🎯 **Por qué importa:** La misma cantidad de oxígeno inspirado no significa lo mismo a 101 kPa que a 70 kPa: importa la presión parcial. La decisión central: ¿qué presión parcial de oxígeno alveolar resulta de una atmósfera dada y cómo cambia con el CO₂ ambiente y la ventilación?

📘 **Dónde se aprende** (1 clase): [B105-C21 · Fisiología respiratoria en microgravedad y atmósferas de cabina](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md).

### Ecuación del radiómetro

- La ecuación del radiómetro dice que la fluctuación relativa del ruido promediado es `1/√(Δν τ)`.
- La ecuación del radiómetro `σ_T = T_sys/√(Bτ)`.
- La ecuación del radiómetro da la sensibilidad.

💡 **Cómo se explica en la clase [B49-C08](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md):**
- Ecuacion del radiometro: sigma por muestra = T_sys/sqrt(B dt) = 0.15811 K (0.3162 % de T_sys) ; 1 s: 0.005000 K
- 🎯 **Por qué importa:** Integrar más tiempo no siempre mejora la medida: la deriva lo impide. La decisión central: ¿hasta qué tiempo de integración vale la pena, y cuándo hay que conmutar?

📘 **Dónde se aprende** (3 clases): [B46-C06 · Ruido de sistema y radiometría](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md); [B49-C08 · Estabilidad de ganancia de receptores y variaciones de ganancia](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md); [B56-C16 · Tecnofirmas y búsqueda SETI](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md).

### Ecuación del tiempo

- La ecuación del tiempo es la diferencia entre el mediodía solar verdadero y el medio.

💡 **Cómo se explica en la clase [B08-C05](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md):**
- Este desfase se llama ecuación del tiempo y ocurre porque la rapidez con que el Sol recorre el ecuador celeste no es constante (la causa, ligada a la elipticidad de la órbita y a la inclinación del eje, se estudia en B71 y B13; aquí es un resultado de cálculo).
- Falla en que el avance no es uniforme todo el año (ecuación del tiempo).
- 🎯 **Por qué importa:** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.

📘 **Dónde se aprende** (1 clase): [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md).

### Ecuación diferencial

- Una ecuación diferencial relaciona una función desconocida con sus derivadas.

💡 **Cómo se explica en la clase [B11-C01](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md):**
- python programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/residuo_de_soluciones.py
- 🎯 **Por qué importa:** Casi ninguna ley de la mecánica espacial nos dice *dónde está* un satélite; nos dice *cómo cambia* su movimiento: la aceleración depende de la posición. Eso es una ecuación diferencial.

📘 **Dónde se aprende** (1 clase): [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md).

### Ecuación diferencial ordinaria (EDO)

- Una ecuación diferencial ordinaria (EDO) relaciona una función de una variable con sus derivadas.
- Una ecuación diferencial ordinaria (EDO) relaciona una función con sus derivadas.

🎯 **Por qué importa (clase B14-C03):** Un integrador devuelve un número aunque sea malo. Con las tolerancias por defecto, una órbita circular puede no cerrarse después de una vuelta y el programa no se queja.

📘 **Dónde se aprende** (2 clases): [B14-C03 · Análisis numérico con SciPy](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md); [B17-C03 · Redes neuronales informadas por la física (PINN)](../programa/clases/B17/B17-C03-redes-neuronales-informadas-por-la-fisica-pinn/CLASE.md).

### Ecuación equivalente

- Una ecuación equivalente tiene las mismas soluciones.

🎯 **Por qué importa (clase B03-C14):** La fórmula de la velocidad de escape, `v = √(2GM/R)`, aparece en las fichas de la NASA como un número (11,186 km/s). Pero un ingeniero puede necesitar lo contrario: dado `v`, ¿cuál es el radio?

📘 **Dónde se aprende** (1 clase): [B03-C14 · Despeje de ecuaciones elementales](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md).

### Ecuación hidrostática

- La ecuación hidrostática es `dP/dr = −ρ g`.

🎯 **Por qué importa (clase B53-C01):** Dos cuerpos con la misma masa y radio pueden tener interiores distintos. La decisión central: ¿qué observable separa un cuerpo homogéneo de uno diferenciado?

📘 **Dónde se aprende** (1 clase): [B53-C01 · Interior de planetas rocosos](../programa/clases/B53/B53-C01-interior-de-planetas-rocosos/CLASE.md).

### Ecuación hiperbólica

- La ecuación hiperbólica es `M = e sinh H − H`, con `H` la anomalía hiperbólica.

💡 **Cómo se explica en la clase [B71-C14](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md):**
- Resolver la ecuación hiperbólica `M = e sinh H − H`.
- El script [ecuacion_kepler.py](ecuacion_kepler.py) resuelve la ecuación de Kepler elíptica en 2000 casos con tres métodos y la hiperbólica en 500 casos (comprueba residuo < 1e-12, acuerdo Newton–bisección < 1e-11 y que el punto fijo es el más lento).
- ⚠️ **Error frecuente:** Olvidar que la ecuación hiperbólica usa `sinh`. Se corrige con 8.4.
- 🎯 **Por qué importa:** Propagar una órbita kepleriana exige resolver esta ecuación miles de veces; un método que no converge en `e` alto rompe todo el cálculo. La decisión central: ¿qué solucionador y qué valor inicial usas para que converja siempre y con cuántas iteraciones?

📘 **Dónde se aprende** (1 clase): [B71-C14 · Ecuación de Kepler](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md).

### Ecuación ideal del cohete

- La ecuación ideal del cohete relaciona el cambio de velocidad con la razón de masas: `Δv = ve ln(m₀/m_f)`.

💡 **Cómo se explica en la clase [B100-C02](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md):**
- Aplicar la ecuación ideal del cohete por tramos y hacia atrás.
- Datos: ecuación ideal del cohete (NASA Glenn, consultada); tasas, densidades, factores, Δv, Isp y ε ilustrativos;
- 🎯 **Por qué importa:** La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: ¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?

📘 **Dónde se aprende** (1 clase): [B100-C02 · Dimensionamiento de carga y volumen de misión](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md).

### Ecuación polar común

- La ecuación polar común con el foco en el origen y `θ` desde el punto más cercano (periastro) es `r = p/(1 + e cos θ)`, con `p` el semilado recto; la distancia mínima es `q = p/(1 + e)`.

🎯 **Por qué importa (clase B04-C18):** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.

📘 **Dónde se aprende** (1 clase): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md).

### Ecuación promediada

- La ecuación promediada `da/dt = 2 a_t √(a³/μ)` describe el semieje mayor de una órbita casi circular.

💡 **Cómo se explica en la clase [B81-C04](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md):**
- *Descripción textual:* de las órbitas inicial y final salen las velocidades circulares y de ahí el `Δv` y el tiempo; la ecuación promediada y la integración directa dan otras dos vías que se comparan.
- Por semieje: `a(t)` de la ecuación promediada.
- 🎯 **Por qué importa:** Una espiral de bajo empuje cuesta más `Δv` que un impulso (Hohmann) pero ahorra propelente por su alto `Isp`. La decisión central: ¿cuánto `Δv` y cuánto tiempo cuesta pasar de una órbita circular a otra, y cuánto más si además hay que cambiar el plano?

📘 **Dónde se aprende** (1 clase): [B81-C04 · Trayectorias espirales de bajo empuje](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md).

### Ecuación química

- Los reactivos están a la izquierda y los productos a la derecha de una ecuación química.

🎯 **Por qué importa (clase B06-C08):** Una vela y el Sol liberan energía, pero lo hacen de maneras radicalmente distintas. En la vela, los átomos de carbono e hidrógeno se reordenan con el oxígeno y todos siguen ahí al terminar.

📘 **Dónde se aprende** (1 clase): [B06-C08 · Reacciones y conservación de masa](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md).

### Ecuación TOV

- La ecuación TOV es la de equilibrio hidrostático relativista: `dP/dr = −(e+P)(m + 4πr³P/c²)G/[c²r(r − 2Gm/c²)]`.

💡 **Cómo se explica en la clase [B27-C03](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md):**
- La masa máxima de esta EOS (`1,055 M☉`) queda por debajo de `2,01` y `2,14 M☉` (S3, S4): esta ecuación de estado queda excluida.
- Las medidas obligan a ecuaciones de estado más rígidas a alta densidad (C04).
- 🎯 **Por qué importa:** Las masas y radios de las estrellas de neutrones son la mejor ventana a la materia a densidades nucleares. Para interpretarlos hay que saber qué cambia la relatividad respecto de Newton y por qué existe una masa máxima.

📘 **Dónde se aprende** (1 clase): [B27-C03 · Estrellas de neutrones](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md).

### Ecuación vis-viva

- La ecuación vis-viva `v² = GM (2/r − 1/a)` da la rapidez en cualquier punto (se deduce con la conservación de la energía, C07).
- La ecuación vis‑viva `v² = μ(2/r − 1/a)` liga velocidad y distancia.
- La ecuación vis-viva relaciona velocidad, radio y semieje.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B71-C05](../programa/clases/B71/B71-C05-energia-orbital-especifica/CLASE.md):**
- *Descripción textual:* de la energía salen el semieje, la ecuación vis‑viva y las velocidades extremas; que la energía sea constante es la prueba de la integración.
- Aplicar la ecuación vis‑viva `v² = μ(2/r − 1/a)`.
- 🎯 **Por qué importa:** El semieje fija el período y la energía; cambiar de órbita es cambiar de energía. La decisión central: ¿cuánta energía por kilogramo tiene una órbita y qué velocidad corresponde a cada distancia?

📘 **Dónde se aprende** (6 clases): [B05-C20 · Problema físico integrado de satélite ideal](../programa/clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md); [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md); [B47-C23 · Sondas heliosféricas: Parker Solar Probe y Voyager](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md); [B71-C05 · Energía orbital específica](../programa/clases/B71/B71-C05-energia-orbital-especifica/CLASE.md); [B75-C01 · Geometría de transferencias heliocéntricas](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md); [B77-C12 · Perfil de ascenso orbital](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md).

### Ecuación β

- La ecuación `β` `R = R₀ exp(β(1/T − 1/T₀))`.

💡 **Cómo se explica en la clase [B85-C25](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md):**
- Modelar un NTC con la ecuación `β` y su inversa.
- 🎯 **Por qué importa:** Una temperatura mal medida lleva a una decisión errónea de control o de margen. La decisión central: ¿qué error total tiene la cadena de medida a una temperatura dada y qué término lo domina?

📘 **Dónde se aprende** (1 clase): [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md).

### Ecuaciones de campo

- Las ecuaciones de campo son `G_ab = (8πG/c⁴) T_ab`.

💡 **Cómo se explica en la clase [B39-C05](../programa/clases/B39/B39-C05-ecuaciones-de-campo-de-einstein-y-limite-newtoniano/CLASE.md):**
- La evidencia es la ficha de las ecuaciones de campo del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de las ecuaciones de campo*: límite newtoniano, FLRW y Bianchi.
- 🎯 **Por qué importa:** Las ecuaciones de campo conectan la geometría con la materia. La decisión central: ¿en qué régimen la gravedad de Einstein se reduce a la de Newton y qué garantiza la consistencia de las ecuaciones?

📘 **Dónde se aprende** (1 clase): [B39-C05 · Ecuaciones de campo de Einstein y límite newtoniano](../programa/clases/B39/B39-C05-ecuaciones-de-campo-de-einstein-y-limite-newtoniano/CLASE.md).

### Ecuaciones de Clohessy–Wiltshire

- Las ecuaciones de Clohessy–Wiltshire lo aproximan para órbitas circulares y separaciones pequeñas.

🎯 **Por qué importa (clase B119-C28):** B119-C11 trata límites militares; las normas voluntarias de conducta responsable no tienen clase y se apoyan en conceptos físicos (distancia relativa, deriva, previsibilidad) que esta clase muestra. La decisión central: ¿qué condiciones iniciales mantienen al vecino a distancia constante y cuáles lo hacen derivar o acercarse?

📘 **Dónde se aprende** (1 clase): [B119-C28 · Normas de comportamiento responsable en el espacio](../programa/clases/B119/B119-C28-normas-de-comportamiento-responsable-en-el-espacio/CLASE.md).

### Ecuaciones de Clohessy–Wiltshire (CW)

- Las ecuaciones de Clohessy–Wiltshire (CW) lo describen linealizado alrededor de una órbita circular.

🎯 **Por qué importa (clase B97-C11):** Una inspección segura se diseña de modo que, si falla el empuje, el robot no se acerque ni se aleje: la elipse sin deriva lo garantiza. Con una condición inicial mal elegida, el robot se aleja decenas de veces la distancia deseada en una órbita.

📘 **Dónde se aprende** (1 clase): [B97-C11 · Robots de inspección orbital](../programa/clases/B97/B97-C11-robots-de-inspeccion-orbital/CLASE.md).

### Ecuaciones de Einstein

- Las ecuaciones de Einstein relacionan la curvatura con la energía y el momento de la materia.

🎯 **Por qué importa (clase B26-C09):** La luz de una estrella lejana que pasa cerca del Sol, o de una galaxia, se desvía: es la base de las lentes gravitacionales que miden masas de cúmulos (C18) y de las correcciones al seguimiento de naves en el espacio profundo.

📘 **Dónde se aprende** (1 clase): [B26-C09 · Relatividad general introductoria](../programa/clases/B26/B26-C09-relatividad-general-introductoria/CLASE.md).

### Ecuaciones de estructura estelar

- Las ecuaciones de estructura estelar son cuatro: equilibrio hidrostático `dP/dr = −Gmρ/r²`, continuidad de masa `dm/dr = 4πr²ρ`, transporte de energía y generación de energía.

🎯 **Por qué importa (clase B24-C20):** Un modelo de estructura real resuelve cuatro ecuaciones acopladas con física detallada; un politropo sustituye esa física por una sola relación `P ∝ ρ^{1+1/n}` y permite resolver todo con una ecuación. Es el mejor modo de ver qué se obtiene con poco y qué falta.

📘 **Dónde se aprende** (1 clase): [B24-C20 · Modelo simplificado de estructura estelar](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md).

### Ecuaciones de Euler

- Las ecuaciones de Euler para un cuerpo rígido con inercias principales `J = diag(J1, J2, J3)` en los ejes del cuerpo son `J ω̇ = −ω × (J ω) + u`, con `ω` la velocidad angular del cuerpo respecto de un sistema inercial, expresada en el sistema del cuerpo (rad/s), y `u` el par de control (N·m).
- Las ecuaciones de Euler son su versión sin viscosidad (S2).
- Las ecuaciones de Euler son las de Navier–Stokes sin viscosidad.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C17](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md):**
- A["Ecuaciones de Euler<br/>no lineales"] --> B["Energía V = ½ ω·Jω"]
- *Descripción textual:* de las ecuaciones de Euler se toma la energía como función de Lyapunov; con el control `u = −k ω` su derivada es `−k|ω|²`, que es negativa salvo en reposo; por tanto la energía baja a cero y la velocidad tiende a cero.
- 🎯 **Por qué importa:** Cuando un satélite se separa del cohete puede salir girando de forma desordenada («volteando»).

📘 **Dónde se aprende** (4 clases): [B16-C17 · Control no lineal](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md); [B21-C04 · Ecuaciones de Navier-Stokes y dinámica de fluidos computacional](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md); [B79-C02 · Ecuaciones de Euler para flujo no viscoso](../programa/clases/B79/B79-C02-ecuaciones-de-euler-para-flujo-no-viscoso/CLASE.md); [B87-C01 · Dinámica de cuerpo rígido](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md).

### Ecuaciones de HCW

- Las ecuaciones de HCW son `ẍ = 3n²x + 2nẏ`, `ÿ = −2nẋ`, `z̈ = −n²z`.

💡 **Cómo se explica en la clase [B76-C09](../programa/clases/B76/B76-C09-dinamica-relativa-de-hill-clohessy-wiltshire/CLASE.md):**
- Escribir las ecuaciones de HCW en el marco radial–a lo largo de la trayectoria–normal.
- 🎯 **Por qué importa:** Un controlador de encuentro necesita predecir dónde estará la otra nave sin integrar dos cuerpos cada vez. La decisión central: ¿hasta qué distancia y durante cuánto tiempo es válida la solución lineal de HCW, y qué movimientos son acotados?

📘 **Dónde se aprende** (1 clase): [B76-C09 · Dinámica relativa de Hill-Clohessy-Wiltshire](../programa/clases/B76/B76-C09-dinamica-relativa-de-hill-clohessy-wiltshire/CLASE.md).

### Ecuaciones de Navier–Stokes

- Las ecuaciones de Navier–Stokes expresan la conservación de masa, momento y energía de un fluido con viscosidad (S1).

💡 **Cómo se explica en la clase [B21-C04](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md):**
- NASA Glenn presenta las ecuaciones de Navier–Stokes tridimensionales como cinco ecuaciones (continuidad, tres de momento y una de energía) con seis variables dependientes (presión, densidad, temperatura y tres velocidades), por lo que se necesita además una ecuación de estado y un modelo del tensor de esfuerzos (S1).
- Escribir las ecuaciones de Navier–Stokes y reconocer en ellas conservación de masa, momento y energía.
- 🎯 **Por qué importa:** Un fluido aparece en casi toda la ingeniería aeroespacial: el aire alrededor de un cohete, el propelente que se mueve en un tanque, el refrigerante de un satélite.

📘 **Dónde se aprende** (1 clase): [B21-C04 · Ecuaciones de Navier-Stokes y dinámica de fluidos computacional](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md).

### Ecuaciones normales

- Las ecuaciones normales son `AᵀA x = Aᵀ y`.
- Mínimos cuadrados ordinarios (OLS) elige `β̂` que minimiza la suma de cuadrados de los residuos; las ecuaciones normales son `XᵀX β̂ = Xᵀ y`.
- Número f: foco entre apertura. Ecuaciones normales: sistema del ajuste por mínimos cuadrados.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B10-C07](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md):**
- Ecuaciones normales: `4a + 6b = 10,1`, `6a + 14b = 20,2`, con `det = 20`: `a = 1,01`, `b = 1,01`.
- Con QR, `A = QR` y las ecuaciones normales se convierten en `R x = Qᵀ y`, sin formar `AᵀA`.
- 🎯 **Por qué importa:** Una estación mide la distancia a un satélite cada segundo durante diez segundos. Hay once medidas y solo tres parámetros que describir (posición, velocidad y aceleración radiales).

📘 **Dónde se aprende** (5 clases): [B10-C07 · Proyecciones y mínimos cuadrados](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md); [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md); [B32-C10 · Normalización y modelado del continuo espectral](../programa/clases/B32/B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md); [B48-C22 · Control automático del enfocador y autoenfoque](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md); [B74-C07 · Ajuste por mínimos cuadrados](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md).

### Ecuaciones variacionales

- Las ecuaciones variacionales son `Φ' = A(t) Φ` con `Φ(t₀) = I`.

💡 **Cómo se explica en la clase [B81-C01](../programa/clases/B81/B81-C01-ecuaciones-variacionales-y-matriz-de-transicion-de-estados/CLASE.md):**
- Escribir la ecuación variacional `Φ' = A(t) Φ` con `A = [[0, I], [G, 0]]` y el gradiente de gravedad `G`.
- Ejercicio 1 · con los pasos indicados. Escribe la matriz `A` de las ecuaciones variacionales de dos cuerpos con sus cuatro bloques.
- 🎯 **Por qué importa:** Cada método de optimización y de corrección de este bloque pide derivadas: el disparo (C02) necesita `∂r_f/∂v₀`, la validación (C08) y la recuperación (C15) también. La decisión central: ¿cómo se calcula `Φ` de forma exacta y barata, y cómo se sabe que está bien?

📘 **Dónde se aprende** (1 clase): [B81-C01 · Ecuaciones variacionales y matriz de transición de estados](../programa/clases/B81/B81-C01-ecuaciones-variacionales-y-matriz-de-transicion-de-estados/CLASE.md).

### Ecuador celeste

- El polo celeste sur es la prolongación del eje de la Tierra hacia el sur y el ecuador celeste es la prolongación del plano ecuatorial.
- La declinación (Dec, `δ`) es el ángulo de un astro sobre (+) o bajo (−) el ecuador celeste.

💡 **Cómo se explica en la clase [B08-C02](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md):**
- Si estás en el polo sur, el polo celeste está sobre tu cabeza (altura 90°), y el horizonte coincide con el ecuador celeste.
- Para el ecuador celeste (`δ = 0`) siempre son 12 h; para objetos del lado del polo visible son más de 12 h; del lado contrario, menos.
- 🎯 **Por qué importa:** Alguien en Punta Arenas ve girar algunas estrellas sin ponerse jamás; alguien en el valle del Elqui las ve rozar el horizonte, y alguien en el hemisferio norte no las ve nunca. Entender por qué evita comprar un telescopio para un objeto que no sale en tu cielo.

📘 **Dónde se aprende** (2 clases): [B08-C02 · Esfera celeste y horizonte local](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md); [B08-C03 · Ascensión recta y declinación](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md).

### Ecualización

- La ecualización reasigna valores para que el histograma sea casi plano.

💡 **Cómo se explica en la clase [B15-C10](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md):**
- La ecualización por función de distribución acumulada reasigna cada valor a su rango: el histograma resultante es casi plano (en el laboratorio, la desviación máxima respecto a un histograma plano de 20 intervalos es `0,0000`, porque casi todos los valores son distintos).
- Ecualización: máxima visibilidad local, ninguna proporcionalidad.
- ⚠️ **Error frecuente:** Creer que la ecualización «mejora» los datos. Solo mejora la visibilidad; sección 8.5.
- 🎯 **Por qué importa:** Tienes una imagen con un cielo de 50 ADU, una estructura difusa tenue 15 ADU por encima y una estrella de 9000 ADU. Si la muestras con una escala lineal entre mínimo y máximo, el cielo y la estructura quedan en los niveles de gris 1 y 2 de 255: parece una pantalla negra con un punto.

📘 **Dónde se aprende** (1 clase): [B15-C10 · Histogramas y normalización](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md).

### Ecuante

- El ecuante es un punto desplazado respecto del cual el centro del epiciclo se mueve de manera uniforme (S1).

💡 **Cómo se explica en la clase [B02-C10](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md):**
- Según S1, Ptolomeo combinó el excéntrico, el epiciclo y el ecuante para modelar el Sol, la Luna y los planetas, y el conjunto explicaba los movimientos observados dentro de la precisión de su época, incluido el retroceso aparente.
- Ptolomeo usó tres construcciones geométricas: el círculo excéntrico, el epiciclo y el ecuante (S1).
- 🎯 **Por qué importa:** La pregunta «¿se mueve la Tierra o el cielo?» se puede responder hoy en una línea, pero en 1500 una persona razonable podía defender cualquiera de las dos. La pregunta motivadora es: ¿con qué criterios se elige entre dos modelos que predicen casi lo mismo?

📘 **Dónde se aprende** (1 clase): [B02-C10 · Geocentrismo y heliocentrismo](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md).

### Ecuatorial

- El sistema ecuatorial usa el polo celeste norte y el equinoccio como origen; el eclíptico, el polo de la eclíptica y el mismo equinoccio; el galáctico, el polo norte galáctico y, como origen, la dirección con `l = 0` en el plano galáctico (el centro de la galaxia).
- La altacimutal tiene un eje vertical (acimut) y uno horizontal (altura); la ecuatorial tiene un eje (de ascensión recta) paralelo al eje de la Tierra y otro (de declinación) perpendicular.

💡 **Cómo se explica en la clase [B04-C19](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md):**
- S1 da `A_G` con diez decimales; por ejemplo la tercera columna, `(−0,8676661490; −0,1980763734; +0,4559837762)`, es el polo norte galáctico escrito en ecuatoriales.
- Convención de S1: `[x_G y_G z_G] = [x y z] A_G`: las columnas de `A_G` son los ejes galácticos escritos en el sistema ecuatorial.
- 🎯 **Por qué importa:** Un catálogo da las posiciones en ecuatoriales; un estudio de la Vía Láctea necesita galácticas; un análisis del plano del sistema solar usa eclípticas. Cambiar de sistema es rutina, y un error de signo o de matriz mueve el objeto decenas de grados.

📘 **Dónde se aprende** (2 clases): [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md); [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md).

### Edad

- La edad de la Luna es el tiempo transcurrido desde la luna nueva.
- La edad es `t₀ = ∫₀¹ da/(aH)`.
- La edad es el tiempo entre la época de los elementos y su uso.

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- Si la edad es `a`, el ángulo es `2π·a/P` y la fracción iluminada es `f = (1 − cos(2π·a/P))/2`.
- N["Luna nueva: edad 0"] --> C1["Cuarto creciente: edad ≈ P/4"]
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (3 clases): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md); [B118-C21 · Calidad, latencia y trazabilidad de datos de vigilancia espacial](../programa/clases/B118/B118-C21-calidad-latencia-y-trazabilidad-de-datos-de-vigilancia-espacial/CLASE.md).

### Edad característica

- La edad característica es `τ = P/(2Ṗ)`.

💡 **Cómo se explica en la clase [B27-C05](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md):**
- Como `E_rot/Ė = ω/(2|ω̇|) = P/(2Ṗ)`, la edad característica es exactamente el tiempo en que la energía rotacional se agotaría al ritmo actual (`3,93 × 10¹⁰ s = 1245 años`).
- Para el campo y la edad se usa un púlsar ilustrativo (`P = 0,033 s`, `Ṗ = 4,2 × 10⁻¹³`): `B = 3,77 × 10⁸ T`, edad característica `1245 años`.
- ⚠️ **Error frecuente:** Tomar la edad característica por la edad real. Se corrige con la sección 8.3: asume `Ṗ` constante.
- 🎯 **Por qué importa:** Un púlsar da, a la vez, un reloj de precisión, la medida de su campo magnético y, en una binaria, la masa de las estrellas y una prueba de la relatividad general. La decisión central: dados el periodo y su derivada, ¿qué campo, edad y potencia de frenado tiene el púlsar y qué se aprende de su binaria?

📘 **Dónde se aprende** (1 clase): [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md).

### Edad de modelo

- La edad de modelo es `N/(tasa·área)`.
- Una edad de modelo es la edad que hace coincidir la densidad contada con la cronología.
- La edad de modelo es la que resulta de aplicar una cronología.

💡 **Cómo se explica en la clase [B53-C09](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md):**
- La edad de modelo cubre la edad verdadera dentro de 2σ en `0,942` de los casos.
- cobertura de la edad de modelo a 2 sigma: 0.9415
- 🎯 **Por qué importa:** Un mapa geológico es una hipótesis sobre el tiempo. La decisión central: ¿qué parte del orden temporal está fijada por contacto y qué parte solo sugerida por conteos con incertidumbre?

📘 **Dónde se aprende** (3 clases): [B53-C09 · Estratigrafía planetaria](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md); [B61-C06 · Datación por conteo de cráteres: funciones de producción y edades de modelo](../programa/clases/B61/B61-C06-datacion-por-conteo-de-crateres-funciones-de-produccion-y-edades-de-modelo/CLASE.md); [B70-C04 · Vulcanismo marciano: provincias, edades y evolución](../programa/clases/B70/B70-C04-vulcanismo-marciano-provincias-edades-y-evolucion/CLASE.md).

### Edad del cúmulo

- La edad del cúmulo es la vida en secuencia principal de la estrella en el punto de desvío.

💡 **Cómo se explica en la clase [B24-C19](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md):**
- Por eso la edad de un cúmulo es sensible a la masa de desvío y a la relación masa–luminosidad.
- Esta clase no usa datos reales ni calibra edades de cúmulos concretos.
- ⚠️ **Error frecuente:** Presentar la edad sintética como de un cúmulo real. Se corrige con la sección 10.
- 🎯 **Por qué importa:** La edad de una estrella aislada es difícil de medir; la de un cúmulo se puede leer en su diagrama HR, porque las estrellas más masivas ya han salido de la secuencia principal y el «punto de desvío» marca la edad. Esas edades fijan la cronología de la Galaxia y calibran los modelos.

📘 **Dónde se aprende** (1 clase): [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Edad del dato

- La edad del dato es el tiempo transcurrido entre que el sensor lo midió y el operador lo ve: `A = t_luz + t_proceso + T_tel/2` (valor medio).

💡 **Cómo se explica en la clase [B98-C04](../programa/clases/B98/B98-C04-interfaces-humano-robot-para-operacion-remota/CLASE.md):**
- *Descripción textual:* el dato recorre el retardo de luz, el proceso y la espera del siguiente paquete; la edad es la suma; la predicción compensa lo que se movió el vehículo en ese tiempo.
- Con Marte cercano la edad media del dato es `182,1 + 5 + 30 = 217,1 s` y la pantalla cruda se equivoca en `8,81 m` (rms); la predictiva, en `0,23 m`.
- ⚠️ **Error frecuente:** Mostrar el dato sin su edad. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un operador que decide con un dato viejo sin saberlo comete errores; uno que recibe 24 alarmas por 3 fallos no ve la causa. La decisión central: ¿qué debe mostrar la interfaz para que el operador sepa qué tan viejo es lo que ve y qué es lo importante?

📘 **Dónde se aprende** (1 clase): [B98-C04 · Interfaces humano-robot para operación remota](../programa/clases/B98/B98-C04-interfaces-humano-robot-para-operacion-remota/CLASE.md).

### EDF

- La cota de Liu y Layland `U ≤ n(2^(1/n) − 1)` es suficiente para RM con plazos iguales a los períodos y tiende a `ln 2 = 0,6931`. EDF es óptimo para una CPU con tareas expulsables y plazo igual al período: cumple si `U ≤ 1`.
- La holgura es `plazo − hora de término`. EDF es la regla del plazo más cercano.

💡 **Cómo se explica en la clase [B88-C06](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md):**
- Es armónico con `U = 1,0000`: RM y EDF cumplen, con 7 cambios cada una.
- EDF es una fila donde pasa primero quien tiene la cita más próxima.
- ⚠️ **Error frecuente:** Creer que EDF no puede fallar. Falla si `U > 1` (ejercicio 9)
- 🎯 **Por qué importa:** Elegir la política determina cuánta CPU se puede usar con garantías. La decisión central: ¿RM basta, o se necesita EDF para el conjunto de tareas?

📘 **Dónde se aprende** (2 clases): [B88-C06 · Planificación de tareas RTOS](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md); [B110-C04 · Priorización y decisiones bajo emergencia](../programa/clases/B110/B110-C04-priorizacion-y-decisiones-bajo-emergencia/CLASE.md).

### Editor

- El autor responde por el trabajo; el árbitro (*referee*, *reviewer*) lo evalúa y emite un informe; el editor decide, con base en los informes y en su criterio (S1).

💡 **Cómo se explica en la clase [B20-C03](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md):**
- El editor es responsable del contenido y toma la decisión; no está obligado a seguir la recomendación de cada árbitro, y puede rechazar en cualquier momento antes de la publicación si surgen problemas de integridad (S1).
- Si recibes un comentario irrespetuoso, no respondas con el mismo tono: señálalo al editor con calma y responde al contenido técnico.
- 🎯 **Por qué importa:** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### EDP

- Una EDP relaciona una función de varias variables con sus derivadas parciales.

💡 **Cómo se explica en la clase [B11-C13](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md):**
- Escribir las EDP del calor, de la onda, de Laplace y de la advección.
- Clasificar una EDP lineal de segundo orden con `B² − 4AC`.
- ⚠️ **Error frecuente:** Confundir EDO y EDP. Se corrige con el ejercicio 1 y el vocabulario (sección 6).
- 🎯 **Por qué importa:** El calor que atraviesa un escudo, las ondas en una estructura, el potencial gravitatorio de un cuerpo extenso, el transporte de partículas en un plasma: todos son EDP. Antes de discretizar hay que saber *qué tipo de problema es* (qué datos pide, cómo viaja la información) porque de ello depende el método.

📘 **Dónde se aprende** (1 clase): [B11-C13 · Ecuaciones en derivadas parciales](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md).

### Efectividad

- La efectividad es `V/C`.

💡 **Cómo se explica en la clase [B124-C12](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md):**
- La mejor relación `V/C` es `M05`, pero no es necesariamente la más científica: la efectividad favorece misiones pequeñas.
- La opción de mayor efectividad aparece en `100,0%`.
- ⚠️ **Error frecuente:** Elegir solo por efectividad. Se corrige con 8.3.
- 🎯 **Por qué importa:** El retorno científico no tiene un precio de mercado, pero se puede razonar con una función de valor explícita y una frontera de eficiencia. La decisión central: ¿qué opciones valen la pena a su costo y cuáles están dominadas?

📘 **Dónde se aprende** (1 clase): [B124-C12 · Evaluación de retorno científico](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md).

### Efectividad de recuperación de calor

- La efectividad de recuperación de calor es la fracción del calor latente que se reutiliza.

🎯 **Por qué importa (clase B59-C07):** El agua extraída trae sales y otros solutos, y recuperar más agua concentra la salmuera. La decisión central: ¿qué recuperación se fija para no saturar la salmuera y qué energía cuesta?

📘 **Dónde se aprende** (1 clase): [B59-C07 · Purificación de agua](../programa/clases/B59/B59-C07-purificacion-de-agua/CLASE.md).

### Efecto

- Un modo de fallo es la forma de fallar; su efecto es la consecuencia.

💡 **Cómo se explica en la clase [B83-C22](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md):**
- Ejemplo: rueda de reacción, modo «fricción creciente», efecto «apuntamiento degradado», `S = 6`, `O = 5`, `D = 5`: `RPN = 150`, el mayor.
- La probabilidad de los modos no cambia: la detección reduce su efecto, no su ocurrencia.
- 🎯 **Por qué importa:** Los fallos que no se anticipan se descubren en órbita. La decisión central: ¿qué modos de fallo hay que atacar primero, cuánta probabilidad tienen en la vida de la misión y qué cambia si mejoro su detección?

📖 **Explicado a fondo:** [Doppler (efecto)](esencial/esencial-d-l.md#doppler-efecto) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B83-C22 · Análisis de modos y efectos de fallo (FMEA) en sistemas espaciales](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md).

### Efecto aleatorio

- El modelo de intercepto aleatorio escribe `y_ij = β₀ + β₁ t_j + u_i + e_ij`: `β₀, β₁` son efectos fijos (comunes), `u_i` es el efecto aleatorio de la unidad `i` (su diferencia estable) y `e_ij` el error de medida.

💡 **Cómo se explica en la clase [B12-C25](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md):**
- (iii) la normalidad de los efectos aleatorios no se puede comprobar;
- 🎯 **Por qué importa:** Seis personas medidas cuatro veces dan 24 números, pero no 24 piezas de información independientes: las de una misma persona se parecen. Ignorar eso produce intervalos demasiado angostos para el nivel medio y, paradójicamente, demasiado anchos para los cambios dentro de cada persona.

📘 **Dónde se aprende** (1 clase): [B12-C25 · Modelos longitudinales y de efectos mixtos para muestras pequeñas](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md).

### Efecto atmosférico

- El efecto atmosférico es `T_s − T_e`.

💡 **Cómo se explica en la clase [B54-C20](../programa/clases/B54/B54-C20-comparacion-de-habitabilidad-climatica/CLASE.md):**
- Calcular el efecto atmosférico `T_s − T_e`.
- 🎯 **Por qué importa:** Comparar mundos tienta a ordenarlos por «habitabilidad». La pregunta motivadora: ¿qué dicen realmente la temperatura y la presión de superficie sobre la posibilidad de agua líquida?

📘 **Dónde se aprende** (1 clase): [B54-C20 · Comparación de habitabilidad climática](../programa/clases/B54/B54-C20-comparacion-de-habitabilidad-climatica/CLASE.md).

### Efecto avalancha

- El efecto avalancha es la propiedad por la que un cambio mínimo del mensaje altera, en promedio, la mitad de los bits del resumen.
- El efecto avalancha es que cambiar un bit cambia la mitad de los bits del hash.
- El efecto avalancha: un bit cambiado altera cerca de la mitad de los bits del hash.

💡 **Cómo se explica en la clase [B14-C11](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md):**
- El laboratorio mide además el efecto avalancha con 20 cambios de un bit: entre 103 y 144 bits distintos, con media 125,9 (cerca de 128).
- El script [versiones_de_datos.py](versiones_de_datos.py) implementa un almacén direccionado por contenido con SHA-256, comprueba el vector de prueba del NIST, inserta dos versiones y un duplicado, usa manifiestos como versiones, localiza el cambio, detecta la corrupción de un bit y mide el efecto avalancha.
- 🎯 **Por qué importa:** Un análisis usó «la tabla de catálogo de octubre». En noviembre alguien reemplazó el archivo por otro con el mismo nombre.

📘 **Dónde se aprende** (3 clases): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md); [B88-C18 · Control de configuración de firmware](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md); [B122-C09 · Preservación de evidencias y cadena de custodia de datos de incidentes](../programa/clases/B122/B122-C09-preservacion-de-evidencias-y-cadena-de-custodia-de-datos-de-incidentes/CLASE.md).

### Efecto cono

- El efecto cono: la luz de la estrella a altura finita no atraviesa la misma turbulencia que la de una estrella lejana.

💡 **Cómo se explica en la clase [B42-C17](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md):**
- El efecto cono domina cuando la estrella es baja.
- Porque es más alta y reduce el efecto cono.
- 🎯 **Por qué importa:** Sin estrella guía no hay corrección en casi todo el cielo. La decisión central: ¿a qué altitud conviene crear la estrella y qué error de cono y qué elongación trae?

📘 **Dónde se aprende** (1 clase): [B42-C17 · Estrellas guía artificiales](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md).

### Efecto de J3

- El efecto de J3 crece como `1/e` en `ω̇` y es proporcional a `cos ω` en `ė`.

💡 **Cómo se explica en la clase [B72-C14](../programa/clases/B72/B72-C14-orbitas-congeladas/CLASE.md):**
- Con `ω = 90°`, `de/dt = 0` (el efecto de J3 sobre `e` es proporcional a `cos ω`).
- El efecto de J3 es mínimo en aceleración (`~10⁻⁶` de la central) pero, al ser inversamente proporcional a `e`, domina cuando la órbita es casi circular.
- 🎯 **Por qué importa:** Un altímetro o un radar que observa la misma traza necesita pasar por cada latitud a la misma altitud; si el perigeo girara, la altitud sobre un punto cambiaría decenas de kilómetros. La decisión central: ¿qué excentricidad y argumento del perigeo congelan la órbita para una inclinación y altitud dadas?

📘 **Dónde se aprende** (1 clase): [B72-C14 · Órbitas congeladas](../programa/clases/B72/B72-C14-orbitas-congeladas/CLASE.md).

### Efecto de la atmósfera

- El efecto de la atmósfera `ΔT = T_obs − T_e` mide cuánto supera la temperatura observada a la de equilibrio.

🎯 **Por qué importa (clase B54-C03):** La temperatura de un planeta no la fija solo lo que recibe sino cuánto absorbe y cómo se deshace de la energía. La pregunta motivadora: ¿cuánto más caliente es un mundo que su temperatura de equilibrio, y qué dice eso de su atmósfera?

📘 **Dónde se aprende** (1 clase): [B54-C03 · Equilibrio radiativo](../programa/clases/B54/B54-C03-equilibrio-radiativo/CLASE.md).

### Efecto de «mirar en muchos sitios»

- El efecto de «mirar en muchos sitios» hace más probable encontrar alguna discrepancia alta.

🎯 **Por qué importa (clase B26-C23):** Decir «hay una tensión» solo tiene sentido con un número: ¿cuántas sigmas?, ¿qué probabilidad de ocurrir por azar?, ¿qué se asume? Sin ese rigor, una discrepancia se exagera o se descarta.

📘 **Dónde se aprende** (1 clase): [B26-C23 · Tensiones observacionales: constante de Hubble y S8](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md).

### Efecto de mirar en otros lugares

- El efecto de mirar en otros lugares (*look-elsewhere*).

💡 **Cómo se explica en la clase [B31-C20](../programa/clases/B31/B31-C20-evaluacion-critica-de-afirmaciones-extraordinarias/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Qué supone el efecto de mirar en otros lugares?
- El script [afirmaciones.py](afirmaciones.py) calcula valores p, el efecto de mirar en otros lugares y la actualización bayesiana (comprueba la inversa a `10⁻⁹`, Monte Carlo a 4 errores y `P = 0,5` a `10⁻¹²`).
- 🎯 **Por qué importa:** Muchos «descubrimientos» desaparecen al contar los lugares donde se buscó o al pesar una probabilidad previa baja. La decisión central: ¿cuánta evidencia hace falta para creer una afirmación improbable?

📘 **Dónde se aprende** (1 clase): [B31-C20 · Evaluación crítica de afirmaciones extraordinarias](../programa/clases/B31/B31-C20-evaluacion-critica-de-afirmaciones-extraordinarias/CLASE.md).

### Efecto de superficie

- El efecto de superficie es un desplazamiento de frecuencias por las capas externas, aquí modelado como `a(ν/ν_max)^b`.

🎯 **Por qué importa (clase B37-C14):** Las capas superficiales cambian las frecuencias de modo sistemático. La decisión central: ¿se corrige el efecto de superficie y qué parámetros se recuperan con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B37-C14 · Ajuste de modelos estelares a frecuencias sísmicas](../programa/clases/B37/B37-C14-ajuste-de-modelos-estelares-a-frecuencias-sismicas/CLASE.md).

### Efecto de tamaño

- El efecto de tamaño dice que más volumen implica más defectos.

💡 **Cómo se explica en la clase [B84-C04](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md):**
- *Descripción textual:* las resistencias ordenadas dan `m` y `σ₀` por dos vías; con ellos se calculan el efecto de tamaño y la resistencia para una `P_f`.
- Aplicar el efecto de tamaño `V σᵐ = const`.
- 🎯 **Por qué importa:** Un metal avisa antes de romper; una cerámica no. Diseñar con la resistencia media de una probeta pequeña sobreestima la de una pieza grande en 40 %.

📘 **Dónde se aprende** (1 clase): [B84-C04 · Cerámicos y polímeros espaciales](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md).

### Efecto del diseño

- El efecto del diseño `1 + (n_t − 1) ICC` mide cuánto reduce la correlación el tamaño muestral efectivo.

💡 **Cómo se explica en la clase [B12-C25](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md):**
- La causa: las 24 observaciones valen mucho menos que 24 independientes (efecto del diseño `1 + 3 · 0,8 = 3,4`, tamaño efectivo `24/3,4 ≈ 7`).
- Ejercicio 4. Calcula el efecto del diseño y el tamaño muestral efectivo con `ICC = 0,8`, `n_t = 4`, `N = 24`.
- 🎯 **Por qué importa:** Seis personas medidas cuatro veces dan 24 números, pero no 24 piezas de información independientes: las de una misma persona se parecen. Ignorar eso produce intervalos demasiado angostos para el nivel medio y, paradójicamente, demasiado anchos para los cambios dentro de cada persona.

📘 **Dónde se aprende** (1 clase): [B12-C25 · Modelos longitudinales y de efectos mixtos para muestras pequeñas](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md).

### Efecto Doppler

- El efecto Doppler es el cambio de frecuencia percibida por el movimiento relativo entre fuente y observador.

🎯 **Por qué importa (clase B05-C12):** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.

📘 **Dónde se aprende** (1 clase): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md).

### Efecto escalera

- El efecto escalera (*stair-step*) es la rugosidad por capas en superficies inclinadas.

🎯 **Por qué importa (clase B84-C15):** Dos piezas idénticas con otra velocidad de barrido pueden salir porosas; una ventana de proceso bien trazada evita el desperdicio, y la rugosidad escalonada decide qué superficies se mecanizan. La decisión central: ¿con qué potencia y velocidad se imprime dentro de la ventana y cuánto tarda y qué acabado deja?

📘 **Dónde se aprende** (1 clase): [B84-C15 · Manufactura aditiva](../programa/clases/B84/B84-C15-manufactura-aditiva/CLASE.md).

### Efecto estocástico

- Un efecto estocástico es aquel cuya probabilidad, no su gravedad, crece con la dosis.

🎯 **Por qué importa (clase B112-C04):** Ninguna clase cubre riesgo de cáncer y efectos tardíos. Los límites de carrera de una misión se expresan como riesgo, no como umbral, y sin entender cómo se estima y cuán incierta es esa estimación, un límite en mSv parece más preciso de lo que es.

📘 **Dónde se aprende** (1 clase): [B112-C04 · Efectos crónicos y carcinogénesis por radiación](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md).

### Efecto invernadero

- El efecto invernadero eleva la temperatura superficial sobre `T_eq`.

💡 **Cómo se explica en la clase [B29-C13](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md):**
- Con los valores nominales de la UAI (S1), el flujo a 1 au es `1361,16 W/m²`, y un planeta con albedo `0,3` tiene `T_eq = 254,59 K`; con un efecto invernadero ilustrativo de `+33 K`, `287,59 K`.
- Sin atmósfera sí; con el efecto invernadero la superficie puede estar `33 K` más caliente (ilustrativo).
- 🎯 **Por qué importa:** La temperatura de equilibrio es la primera estimación de si un mundo es cálido o helado, pero no es la temperatura de la superficie: depende del albedo y del efecto invernadero. La decisión central: ¿a qué distancias una estrella da una temperatura de equilibrio dada y cuánto cambia con el albedo?

📖 **Explicado a fondo:** [Efecto invernadero](esencial/esencial-d-l.md#efecto-invernadero) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B29-C13 · Zonas de habitabilidad](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md).

### Efecto mínimo detectable

- El efecto mínimo detectable es el `d` con 80 % de potencia.

💡 **Cómo se explica en la clase [B105-C20](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md):**
- *Descripción textual:* el número de participantes, el tamaño del efecto y `α` fijan la potencia; con ella se calcula el efecto mínimo detectable, y las comparaciones múltiples exigen corregir `α`.
- Calcular el efecto mínimo detectable con 80 % de potencia para un `n` dado.
- 🎯 **Por qué importa:** Un estudio con 6 personas solo detecta efectos grandes; sin saberlo, se concluye «no hay efecto» cuando solo no había potencia. La decisión central: ¿qué efecto mínimo puede detectar el protocolo con su `n`, y cuántas comparaciones puede permitirse?

📘 **Dónde se aprende** (1 clase): [B105-C20 · Diseño de protocolo médico simulado](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md).

### Efecto Neupert

- El efecto Neupert es la relación entre rayos X blandos y duros.

💡 **Cómo se explica en la clase [B30-C12](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md):**
- *Descripción textual:* el flujo da la clase y la escala R; la ley de potencias da la estadística; el efecto Neupert relaciona los rayos X; el flujo integrado da la energía.
- Verificar el efecto Neupert numéricamente.
- 🎯 **Por qué importa:** Para alertar de una erupción hay que saber qué magnitud tiene, con qué frecuencia ocurren eventos grandes y cuánta energía liberan. La decisión central: ¿cómo se clasifica una fulguración y qué dice una ley de potencias sobre la frecuencia de las grandes?

📘 **Dónde se aprende** (1 clase): [B30-C12 · Erupciones y fulguraciones solares](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md).

### Efecto secundario

- Un efecto secundario es algo que la función hace además de devolver (imprimir, modificar un archivo).
- Un efecto secundario es cualquier cosa que una función hace además de devolver un valor (escribir, imprimir, modificar un objeto compartido).

💡 **Cómo se explica en la clase [B07-C06](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md):**
- Límite de la analogía: una máquina física no puede cambiar el mundo exterior sin que se note; una función sí (con efectos secundarios, como modificar una lista que recibe).
- Distinguir parámetro, argumento, valor devuelto y efecto secundario.
- 🎯 **Por qué importa:** Copiar y pegar el mismo cálculo en cinco sitios es la forma más rápida de tener cinco versiones distintas y un error corregido solo en una. Una función concentra la lógica en un lugar, le da un nombre que expresa su intención y permite probarla aislada.

📘 **Dónde se aprende** (2 clases): [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md); [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md).

### Efecto túnel

- El efecto túnel es la transmisión a través de una barrera con `E < V₀`.
- El efecto túnel permite atravesarla.

💡 **Cómo se explica en la clase [B24-C07](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md):**
- El pico está en `6 keV`, mucho menor que la escala de la barrera (`E_G = 493 keV`); la fusión ocurre por efecto túnel, no por superar la barrera.
- 🎯 **Por qué importa:** Dos protones se repelen con una fuerza eléctrica enorme; a las temperaturas de una estrella casi ninguno tiene energía para acercarse lo suficiente. Aun así la fusión ocurre, por efecto túnel.

📘 **Dónde se aprende** (2 clases): [B24-C07 · Ciclo CNO y cadena protón-protón](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md); [B31-C02 · Ecuación de Schrödinger](../programa/clases/B31/B31-C02-ecuacion-de-schrodinger/CLASE.md).

### Efecto Yarkovsky

- El efecto Yarkovsky es el empuje por la reemisión térmica anisótropa de un cuerpo que rota.

💡 **Cómo se explica en la clase [B58-C14](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md):**
- python programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/yarkovsky.py
- 🎯 **Por qué importa:** Una deriva de decenas de kilómetros en un siglo puede decidir si un acercamiento ocurre. La decisión central: ¿cuánto se desplaza un asteroide por empuje térmico y por qué los cuerpos pequeños son más sensibles?

📘 **Dónde se aprende** (1 clase): [B58-C14 · Efectos Yarkovsky y YORP](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md).

### Efecto Zeeman

- El efecto Zeeman es el desdoblamiento de niveles en un campo.

💡 **Cómo se explica en la clase [B32-C12](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md):**
- La evidencia es la ficha del efecto Zeeman estelar del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha del efecto Zeeman estelar*: tabla, comparación con el Doppler y error de la aproximación.
- 🎯 **Por qué importa:** Medir campos estelares exige saber cuándo el desdoblamiento se resuelve y cuándo basta la polarización. La decisión central: ¿qué campo produce un desdoblamiento comparable al ancho de la línea?

📘 **Dónde se aprende** (3 clases): [B31-C05 · Espín y momento angular](../programa/clases/B31/B31-C05-espin-y-momento-angular/CLASE.md); [B32-C12 · Efecto Zeeman y diagnóstico de campos magnéticos estelares](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md); [B47-C21 · Magnetógrafos y medición de campos solares](../programa/clases/B47/B47-C21-magnetografos-y-medicion-de-campos-solares/CLASE.md).

### Efectos fijos

- El modelo de intercepto aleatorio escribe `y_ij = β₀ + β₁ t_j + u_i + e_ij`: `β₀, β₁` son efectos fijos (comunes), `u_i` es el efecto aleatorio de la unidad `i` (su diferencia estable) y `e_ij` el error de medida.

🎯 **Por qué importa (clase B12-C25):** Seis personas medidas cuatro veces dan 24 números, pero no 24 piezas de información independientes: las de una misma persona se parecen. Ignorar eso produce intervalos demasiado angostos para el nivel medio y, paradójicamente, demasiado anchos para los cambios dentro de cada persona.

📘 **Dónde se aprende** (1 clase): [B12-C25 · Modelos longitudinales y de efectos mixtos para muestras pequeñas](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md).

### Efeméride

- Una efeméride es una tabla de posiciones y velocidades en función del tiempo.
- Una efeméride da la posición de un cuerpo en función del tiempo.

💡 **Cómo se explica en la clase [B23-C05](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md):**
- Antes de usar números, se escribe: fuente (Horizons API), cuerpo y centro (399 respecto de 10), marco (eclíptica J2000, ICRF), unidades (au, au/d), tiempo (JD TDB), efeméride (DE441), tipo de estado (geométrico), fecha de consulta (2026-11-05).
- El modelo y la efeméride parten del mismo estado inicial; se separan porque la efeméride incluye fuerzas que el modelo ignora.
- ⚠️ **Error frecuente:** Presentar una efeméride como observación. Se corrige con la sección 5.
- 🎯 **Por qué importa:** Un modelo kepleriano de la Tierra pasó todas las pruebas de C01–C04, pero eso no dice nada sobre si la Tierra se mueve como una elipse perfecta. La pregunta motivadora es: ¿contra qué contrasto mi modelo, y qué diferencia estoy dispuesto a aceptar?

📘 **Dónde se aprende** (2 clases): [B14-C21 · Datos de misiones planetarias: PDS4, etiquetas y SPICE](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md); [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md).

### Efeméride de referencia

- Una efeméride de referencia es una trayectoria independiente (de otra herramienta o de otra solución).

💡 **Cómo se explica en la clase [B74-C20](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md):**
- Es el ejemplo conductor; la referencia es sintética, no una efeméride real.
- ⚠️ **Error frecuente:** Presentar la referencia sintética como una efeméride real. Rotula como sintético, como en la sección 10.
- 🎯 **Por qué importa:** Una solución que ajusta bien sus datos puede predecir pésimamente. La decisión central: ¿dentro de qué tolerancia coincide mi solución con la referencia, en qué componente falla y qué modelo falta?

📘 **Dónde se aprende** (1 clase): [B74-C20 · Validación frente a efemérides de referencia](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md).

### Eficacia

- La eficacia de los LED es µmol por julio.
- La eficacia `e` es la fracción en que un control reduce la probabilidad.
- La eficacia `e` es la probabilidad de que la capa detenga la acción.

💡 **Cómo se explica en la clase [B59-C14](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md):**
- AREA --> P["× PPFD ÷ eficacia: potencia"]
- Calcular la potencia de iluminación con la eficacia de los LED.
- 🎯 **Por qué importa:** Cultivar exige luz, y la luz eléctrica cuesta potencia. La decisión central: ¿cuántos metros cuadrados y cuántos kilovatios necesita un cultivo para producir el oxígeno de una persona?

📘 **Dónde se aprende** (3 clases): [B59-C14 · Agricultura y sustratos artificiales](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md); [B122-C03 · Modelo defensivo de riesgos de infraestructura espacial](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md); [B122-C04 · Seguridad de estaciones terrestres y segmento de control](../programa/clases/B122/B122-C04-seguridad-de-estaciones-terrestres-y-segmento-de-control/CLASE.md).

### Eficacia biológica relativa

- La eficacia biológica relativa (RBE) compara el efecto de dos radiaciones a igual dosis; aquí se trata solo de forma cualitativa.

💡 **Cómo se explica en la clase [B112-C01](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md):**
- A igual dosis, una radiación de alto LET concentra la energía en pocas trazas muy densas, lo que está asociado a más daño complejo por traza (B112-C05) y, por eso, a más eficacia biológica relativa.
- 🎯 **Por qué importa:** B105-C06 introduce la exposición a la radiación espacial como un hecho del entorno, pero no define qué se mide ni en qué unidades. Sin esa definición no se puede leer una tasa de dosis de una misión ni entender por qué los iones pesados preocupan más que los protones.

📘 **Dónde se aprende** (1 clase): [B112-C01 · Magnitudes dosimétricas: dosis absorbida, LET y eficacia biológica](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md).

### Eficacia de control

- La eficacia de control `μ_c = T·l_t/I_y` mide el momento por radián de tobera.

💡 **Cómo se explica en la clase [B77-C23](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md):**
- *Descripción textual:* la rigidez aerodinámica negativa da la divergencia de lazo abierto; la eficacia de control da la ganancia mínima; con ganancia mayor, el lazo cerrado es estable y fija el ángulo de ataque ante una racha.
- 🎯 **Por qué importa:** Un vehículo inestable es controlable si el control es más rápido que la divergencia, pero el control a su vez fija las cargas ante rachas. La decisión central: ¿cuánto control hace falta para estabilizar un lanzador y qué ángulo de ataque deja una racha según la ganancia?

📘 **Dónde se aprende** (1 clase): [B77-C23 · Estabilidad de vuelo de lanzadores en ascenso](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md).

### Eficacia de la lámpara

- DLI: mol de fotones por m² y día. Eficacia de la lámpara: µmol por julio.

🎯 **Por qué importa (clase B106-C12):** Cultivar reduce la masa de alimento a lanzar y devuelve oxígeno, pero cuesta mucha área y electricidad. La decisión central: ¿qué fracción de la dieta compensa cultivar dado el costo en área y energía?

📘 **Dónde se aprende** (1 clase): [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md).

### Eficacia fotónica

- La eficacia fotónica son los micromoles de fotones por julio eléctrico (µmol/J).

🎯 **Por qué importa (clase B115-C02):** La luz es el mayor consumo eléctrico de un cultivo cerrado. La decisión central: ¿cuántos fotones por metro cuadrado y día hacen falta, con qué eficacia se producen y qué potencia y calor suponen para el hábitat?

📘 **Dónde se aprende** (1 clase): [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### Eficiencia

- La eficiencia es `E = S/p`.
- La eficiencia es `E = S/N`.
- La eficiencia es obturador/(obturador + sobrecarga).
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Aceleración: `S(2) = 1,16` y `S(4) = 0,99`, con eficiencias de 0,58 y 0,25.
- Calcular aceleración y eficiencia a partir de tiempos medidos.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.

📘 **Dónde se aprende** (12 clases): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md); [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md); [B27-C10 · Discos de acreción](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md); [B38-C07 · Modelos submalla de formación estelar y retroalimentación](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md); [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B56-C02 · Bioquímica y metabolismo terrestre](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md) y 6 más.

### Eficiencia aerodinámica

- La eficiencia aerodinámica es `L/D`.

🎯 **Por qué importa (clase B77-C04):** Un coeficiente se mide en un túnel y se usa en vuelo. La decisión central: ¿cómo se obtienen y se declaran `Cd` y `CL` para que las fuerzas calculadas sean reproducibles y de qué dependen?

📘 **Dónde se aprende** (1 clase): [B77-C04 · Coeficientes de arrastre y sustentación](../programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/CLASE.md).

### Eficiencia cuántica

- La eficiencia cuántica `QE(λ)` es la fracción de fotones que se convierten en electrones.
- La eficiencia cuántica `QE` es la fracción de fotones que genera un electrón.

💡 **Cómo se explica en la clase [B44-C04](../programa/clases/B44/B44-C04-eficiencia-cuantica-espectral/CLASE.md):**
- Evaluar una curva de eficiencia cuántica.
- La evidencia es la ficha de la eficiencia cuántica del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** La luz de una estrella llega repartida en longitudes de onda y el detector responde distinto a cada una. La decisión central: ¿qué eficiencia efectiva tiene el detector en esta banda?

📘 **Dónde se aprende** (2 clases): [B44-C04 · Eficiencia cuántica espectral](../programa/clases/B44/B44-C04-eficiencia-cuantica-espectral/CLASE.md); [B57-C04 · Satélites ópticos de observación](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md).

### Eficiencia de acoplamiento

- La eficiencia de acoplamiento `ε` es la fracción de la energía de la explosión que acaba empujando gas (aquí `0,1`, ilustrativa).

💡 **Cómo se explica en la clase [B25-C16](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md):**
- Definir retroalimentación, supernova, eficiencia de acoplamiento y energía de ligadura.
- 🎯 **Por qué importa:** Sin retroalimentación, el gas de una galaxia se convertiría en estrellas mucho más deprisa de lo observado. Las supernovas, los vientos y la radiación de las estrellas masivas calientan y expulsan gas, y lo enriquecen con metales (C17).

📘 **Dónde se aprende** (1 clase): [B25-C16 · Retroalimentación estelar](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md).

### Eficiencia de apertura

- La eficiencia de apertura compara con la iluminación uniforme.
- La eficiencia de apertura `η` agrupa las pérdidas de iluminación y desbordamiento.

💡 **Cómo se explica en la clase [B89-C03](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md):**
- ILUSTRATIVO: frecuencias centrales; eficiencia de apertura 0.60 (sintetica)
- 🎯 **Por qué importa:** Elegir la banda es la primera decisión de diseño de un enlace y determina el tamaño de la antena y la tasa alcanzable. La decisión central: ¿qué banda usar para una ganancia de antena dada y qué se paga en apuntamiento por usarla?

📘 **Dónde se aprende** (2 clases): [B46-C04 · Diagramas de radiación](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md); [B89-C03 · Bandas VHF UHF S X Ka](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md).

### Eficiencia de cadena

- La eficiencia de cadena es el producto de las eficiencias.

💡 **Cómo se explica en la clase [B86-C12](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md):**
- La potencia de ala es `118,899 W`, la eficiencia total `84,78 %` y el calor total de la cadena `18,099 W`, con un residuo del balance de `0,0e+00 W`.
- Una carga sintética de `100,8 W` pasa por convertidores (`0,92`), PCDU (`0,95`) y seguidor (`0,97`): el ala debe dar `118,90 W` (eficiencia total `84,8 %`) y la cadena genera `18,10 W` de calor; la batería aporta `2,03 W` más como promedio.
- 🎯 **Por qué importa:** Una eficiencia de `92 %` parece alta hasta que se multiplica por las demás etapas y se ve el calor que queda. Cada vatio perdido debe radiarse: el calor decide el tamaño del radiador y la potencia del ala.

📘 **Dónde se aprende** (1 clase): [B86-C12 · Eficiencia y disipación](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md).

### Eficiencia de camino

- La eficiencia de camino (`X_d` en luz, `X_e` en eclipse) es la fracción de potencia que llega a la carga por el camino indicado.

💡 **Cómo se explica en la clase [B86-C01](../programa/clases/B86/B86-C01-balance-de-potencia-electrica/CLASE.md):**
- Calcular la potencia de ala requerida con las eficiencias de camino de la batería.
- ⚠️ **Error frecuente:** Olvidar las eficiencias de camino. Se corrige con 8.2 y el ejemplo 13.
- 🎯 **Por qué importa:** Un satélite no consume lo mismo en la luz que en el eclipse, y la batería solo transfiere energía, no la crea. Si se dimensiona con la potencia instantánea y no con la energía por órbita, el ala queda corta o sobrada.

📘 **Dónde se aprende** (1 clase): [B86-C01 · Balance de potencia eléctrica](../programa/clases/B86/B86-C01-balance-de-potencia-electrica/CLASE.md).

### Eficiencia de captura

- La eficiencia de captura es la fracción del calor producido que llega al material.

💡 **Cómo se explica en la clase [B59-C06](../programa/clases/B59/B59-C06-extraccion-y-procesamiento-de-volatiles/CLASE.md):**
- Energia termica = 1.675 kWh/kg ; con eficiencia de captura 50 % = 3.350 kWh/kg de agua
- 🎯 **Por qué importa:** Con poco hielo hay que calentar mucha roca. La decisión central: ¿cuánta energía por kilogramo de agua pide una abundancia de 5,6 % frente a 2,7 %?

📘 **Dónde se aprende** (1 clase): [B59-C06 · Extracción y procesamiento de volátiles](../programa/clases/B59/B59-C06-extraccion-y-procesamiento-de-volatiles/CLASE.md).

### Eficiencia de carga

- Balance neto: entrada − salida. Eficiencia de carga: parte de la energía generada que se almacena.

💡 **Cómo se explica en la clase [B96-C12](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md):**
- Un satélite sintético con paneles de 45 W en luz, carga base de 16 W, carga útil de 14 W, batería de 40 Wh y eficiencia de 0,92 pasa 35,61 min en eclipse y 60,04 min en luz.
- ⚠️ **Error frecuente:** Olvidar la eficiencia de carga. Aplícala a la generación (8.2)
- 🎯 **Por qué importa:** Una batería descargada en exceso se degrada y una nave sin energía deja de ser comandable. La decisión central: ¿qué plan de operación mantiene la batería dentro de su criterio de descarga y recupera la carga en cada órbita?

📘 **Dónde se aprende** (1 clase): [B96-C12 · Gestión de energía en operaciones](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md).

### Eficiencia de datos

- La eficiencia de datos es datos de usuario dividido por octetos de canal.

💡 **Cómo se explica en la clase [B89-C11](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md):**
- Calcular la eficiencia de datos de una trama con cabecera y control de errores.
- I k [oct] n [oct] canal [oct] datos [oct] eficiencia k [bits]
- 🎯 **Por qué importa:** El receptor solo puede decodificar si encuentra el comienzo de cada bloque; la elección del marcador, su tolerancia y la profundidad de entrelazado deciden la latencia, el rendimiento y la pérdida de tramas.

📘 **Dónde se aprende** (1 clase): [B89-C11 · Telemetría CCSDS](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md).

### Eficiencia de detección

- La eficiencia de detección `η` es la fracción de fotones que se cuenta.

💡 **Cómo se explica en la clase [B92-C05](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md):**
- Convertir fotones detectados en fotones incidentes con la eficiencia de detección.
- 🎯 **Por qué importa:** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?

📘 **Dónde se aprende** (1 clase): [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Eficiencia de energía

- La eficiencia de energía es energía almacenada entre energía de entrada.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- La energía almacenada (integral de la OCV) con `1 A` es `42,42 Wh` y la de entrada `42,59 Wh`: la eficiencia de energía es `99,60 %`, y la diferencia se disipa como calor en la resistencia interna.
- Calcular la energía de entrada, la almacenada y la eficiencia de energía de la carga.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Eficiencia de impactación

- La eficiencia de impactación es la fracción de gotas que chocan con la raíz.

💡 **Cómo se explica en la clase [B115-C04](../programa/clases/B115/B115-C04-sistemas-aeroponicos/CLASE.md):**
- Para una gota de 20 µm en aire a 22 °C: `τ = 1,235 ms`, `St = τ·v/D = 4,94` con un chorro de 2 m/s y una raíz de 0,5 mm; la eficiencia de impactación (una forma sigmoide ilustrativa, `(St/(St+0,5))²`) es 0,82.
- 🎯 **Por qué importa:** En un hábitat, cada litro y cada kilogramo cuentan. La decisión central: ¿cuánto tiempo puede pasar entre dos nieblas sin que la raíz se seque, y cómo depende eso de la humedad de la cámara y del tamaño de las gotas?

📘 **Dónde se aprende** (1 clase): [B115-C04 · Sistemas aeropónicos](../programa/clases/B115/B115-C04-sistemas-aeroponicos/CLASE.md).

### Eficiencia de muestreo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B51-C12):** La elección de bits y de formato fija cuánta sensibilidad se pierde y cuánto disco y red se necesitan. La decisión central: ¿cuántos bits por muestra, qué eficiencia se obtiene y cómo se empaqueta sin perder información?

📘 **Dónde se aprende** (1 clase): [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md).

### Eficiencia de observación

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B46-C20):** Un proyecto viable cuadra objetivo, sensibilidad, tiempo y datos. La decisión central: ¿cuánto tiempo de observación pide el objetivo y con qué margen?

📘 **Dónde se aprende** (1 clase): [B46-C20 · Proyecto de observación radioastronómica](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md).

### Eficiencia de protocolo

- Contacto: intervalo de comunicación. Eficiencia de protocolo: fracción de la tasa que lleva datos útiles.

🎯 **Por qué importa (clase B96-C02):** Un ConOps que no cierra se descubre en órbita, cuando ya no tiene arreglo barato. La decisión central: ¿alcanzan los contactos para bajar lo que la misión genera, con margen?

📘 **Dónde se aprende** (1 clase): [B96-C02 · Concepto de operaciones de misión](../programa/clases/B96/B96-C02-concepto-de-operaciones-de-mision/CLASE.md).

### Eficiencia de recuperación

- La eficiencia de recuperación `η` es la fracción del consumo `D` que vuelve a estar disponible.
- UFC: unidad formadora de colonias. Eficiencia de recuperación: fracción recuperada por el hisopo.

💡 **Cómo se explica en la clase [B90-C21](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md):**
- Se toman 20 hisopos de 0,01 m² (0,20 m²) sobre una unidad de ejemplo; se cuentan 8 colonias y la eficiencia de recuperación es 0,15.
- Descripción larga: la cota baja al aumentar los conteos o la superficie muestreada y sube cuando la eficiencia de recuperación es baja.
- ⚠️ **Error frecuente:** Olvidar la eficiencia de recuperación. Corrige la cuenta (8.2)
- 🎯 **Por qué importa:** Un hisopo recoge solo una fracción de las esporas de una superficie y se cuentan pocas colonias; el resultado es una estimación con incertidumbre. La decisión central: ¿la biocarga cumple el límite con la confianza exigida o hace falta muestrear más o reducir?

📘 **Dónde se aprende** (2 clases): [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md); [B100-C07 · Dependencia de suministros terrestres y cierre de lazos logísticos](../programa/clases/B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md).

### Eficiencia de sistema

- La eficiencia de sistema es `P_e/P_t`.

🎯 **Por qué importa (clase B86-C16):** Un generador radioisotópico no depende de la distancia al Sol ni del eclipse, pero su potencia decae con el combustible y con los termopares y su eficiencia es baja. Entender esa curva decide qué misiones lo usan.

📘 **Dónde se aprende** (1 clase): [B86-C16 · Generadores radioisotópicos](../programa/clases/B86/B86-C16-generadores-radioisotopicos/CLASE.md).

### Eficiencia de tensión

- La eficiencia de tensión `η_v` es la fracción de la tensión de descarga que gana el ion.

🎯 **Por qué importa (clase B78-C08):** Sin rejillas no hay límite de Child–Langmuir, pero el propulsor depende de que los electrones giren en un radio pequeño y los iones pasen casi rectos. La decisión central: ¿cuánto vale cada radio de giro frente al largo del canal y qué cambia al subir la tensión?

📘 **Dónde se aprende** (1 clase): [B78-C08 · Propulsores Hall](../programa/clases/B78/B78-C08-propulsores-hall/CLASE.md).

### Eficiencia de tobera

- La eficiencia de tobera `P_jet/P_th` mide qué parte del calor pasa a energía cinética.

💡 **Cómo se explica en la clase [B78-C13](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md):**
- La potencia del chorro es `63,38 kW`: la eficiencia de tobera es `0,832` y nunca supera `1`.
- Potencia del chorro = 63.38 kW ; eficiencia de tobera P_jet/P_th = 0.832
- 🎯 **Por qué importa:** La energía llega por la óptica y el propelente solo la transporta; el escape depende de la temperatura que resistan los materiales y de la masa molar. La decisión central: ¿qué empuje e `Isp` da un colector de área dada y cómo se compara con un propulsor eléctrico alimentado con la misma potencia?

📘 **Dónde se aprende** (1 clase): [B78-C13 · Propulsión solar térmica](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md).

### Eficiencia de tramas

- La eficiencia de tramas (sintética) descuenta cabeceras.

💡 **Cómo se explica en la clase [B83-C11](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md):**
- El código LDPC (8160, 7136) con ASM de 32 bits tiene eficiencia `7136/8192 = 0,871094`; con tramas al 97 % la eficiencia total es 84,50 %.
- Eficiencia del codigo = 7136/(8160+32) = 0.871094 ; eficiencia total con tramas = 84.496 %
- ⚠️ **Error frecuente:** Olvidar la sobrecarga de codificación. Aplica `7136/8192` y la eficiencia de tramas
- 🎯 **Por qué importa:** Un satélite que produce más datos de los que puede bajar los pierde o se satura. La decisión central: ¿cabe todo lo que se produce en los minutos de contacto, y qué tamaño de registrador cubre el peor hueco?

📘 **Dónde se aprende** (1 clase): [B83-C11 · Presupuestos de datos](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md).

### Eficiencia de uso de la luz

- Eficacia de la lámpara: µmol por julio. Eficiencia de uso de la luz: g de biomasa por mol de fotones.

💡 **Cómo se explica en la clase [B106-C12](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md):**
- Límite: aquí la planta se reduce a una eficiencia fija; la real depende de la especie, la edad, el CO₂, la temperatura y el estrés.
- Límites: cultivo único con eficiencia fija, sin ciclo de vida, sin nutrientes ni agua, sin evaporación ni CO₂ limitante.
- 🎯 **Por qué importa:** Cultivar reduce la masa de alimento a lanzar y devuelve oxígeno, pero cuesta mucha área y electricidad. La decisión central: ¿qué fracción de la dieta compensa cultivar dado el costo en área y energía?

📘 **Dónde se aprende** (1 clase): [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md).

### Eficiencia de uso de la radiación (RUE)

- La eficiencia de uso de la radiación (RUE) son los gramos de biomasa por mol de fotones.

💡 **Cómo se explica en la clase [B115-C02](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md):**
- Wheeler (NASA/KSC) tabula el área necesaria para el oxígeno de una persona: con 500 µmol m⁻² s⁻¹ y una eficiencia de uso de la radiación de 0,75 g/mol, 31,5 m².
- 🎯 **Por qué importa:** La luz es el mayor consumo eléctrico de un cultivo cerrado. La decisión central: ¿cuántos fotones por metro cuadrado y día hacen falta, con qué eficacia se producen y qué potencia y calor suponen para el hábitat?

📘 **Dónde se aprende** (1 clase): [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### Eficiencia débil

- La eficiencia débil es `T(1)/T(p)`.

💡 **Cómo se explica en la clase [B14-C16](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md):**
- Con el término de comunicación: `T(8) = 1,015`, `T(64) = 1,030`, `T(512) = 1,045`, de modo que la eficiencia débil es `0,985`, `0,971` y `0,957`.
- Escalado débil: eficiencia 0,985 (`p = 8`), 0,971 (`p = 64`), 0,957 (`p = 512`).
- 🎯 **Por qué importa:** Una simulación de la población de escombros orbitales requiere cien veces más cálculo del que tu equipo puede dar en una semana. Pides tiempo en un clúster y debes decidir: ¿cuántos procesos pido?

📘 **Dónde se aprende** (1 clase): [B14-C16 · Computación distribuida y HPC](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md).

### Eficiencia efectiva

- La eficiencia efectiva es su promedio ponderado por el espectro.

💡 **Cómo se explica en la clase [B44-C04](../programa/clases/B44/B44-C04-eficiencia-cuantica-espectral/CLASE.md):**
- La eficiencia efectiva (`0,77`) es menor que el máximo (`0,90`).
- *Descripción textual:* el espectro ponderado por la curva da una eficiencia efectiva y de ella el número de electrones.
- 🎯 **Por qué importa:** La luz de una estrella llega repartida en longitudes de onda y el detector responde distinto a cada una. La decisión central: ¿qué eficiencia efectiva tiene el detector en esta banda?

📘 **Dónde se aprende** (1 clase): [B44-C04 · Eficiencia cuántica espectral](../programa/clases/B44/B44-C04-eficiencia-cuantica-espectral/CLASE.md).

### Eficiencia espectral

- La eficiencia espectral `η = Rb/B` se mide en bit/s/Hz.

💡 **Cómo se explica en la clase [B89-C02](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md):**
- Aplicar el límite de Shannon y el mínimo de `Eb/N0` para una eficiencia espectral.
- 🎯 **Por qué importa:** Sin una idea cuantitativa del ancho de banda no se puede decidir cuántos enlaces caben en una banda ni cuánta tasa de datos es posible. La regulación (C19) trabaja con exactamente estas magnitudes.

📘 **Dónde se aprende** (1 clase): [B89-C02 · Frecuencia y espectro espacial](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md).

### Eficiencia farádica

- La eficiencia farádica es la fracción de la corriente que produce H₂.

💡 **Cómo se explica en la clase [B59-C10](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md):**
- Energía mínima (`ΔH/M`) y a tensión de operación (`2FV/(η M)`) difieren por la sobretensión y la eficiencia farádica.
- 🎯 **Por qué importa:** La electrólisis es el mayor consumidor de energía de la planta. La decisión central: ¿a qué densidad de corriente conviene operar, entre una celda pequeña que gasta más electricidad y una grande que gasta menos?

📘 **Dónde se aprende** (1 clase): [B59-C10 · Electrólisis y balances energéticos](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md).

### Eficiencia global

- La eficiencia global `η_o = η_th η_p = F V₀/(ṁ_c Q_R)`.

💡 **Cómo se explica en la clase [B79-C16](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md):**
- La eficiencia global depende de las dos: mejorar el ciclo sin mirar el chorro (o al revés) deja a la otra intacta.
- *Descripción textual:* la energía del combustible se convierte en energía cinética del chorro y esta en potencia propulsiva; la eficiencia global es el producto de las dos.
- 🎯 **Por qué importa:** Ninguna clase cubre cómo se cuantifica la conversión de energía en propulsión. Sin eficiencias separadas, un cambio de diseño se evalúa a ciegas: no se sabe si mejora el ciclo o el aprovechamiento del chorro.

📘 **Dónde se aprende** (1 clase): [B79-C16 · Eficiencias termodinámicas de motores](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md).

### Eficiencia óptica

- La eficiencia óptica y la térmica miran las pérdidas de la óptica y del absorbedor.

💡 **Cómo se explica en la clase [B78-C13](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md):**
- Un colector ilustrativo de `100 m²` con eficiencias óptica `0,70` y térmica `0,80` capta `76,22 kW` a 1 UA.
- Ejercicio 7 · autónomo. ¿Qué pasa con `F` si la eficiencia óptica baja a 0,5 (resto igual)?
- 🎯 **Por qué importa:** La energía llega por la óptica y el propelente solo la transporta; el escape depende de la temperatura que resistan los materiales y de la masa molar. La decisión central: ¿qué empuje e `Isp` da un colector de área dada y cómo se compara con un propulsor eléctrico alimentado con la misma potencia?

📘 **Dónde se aprende** (1 clase): [B78-C13 · Propulsión solar térmica](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md).

### Eficiencia por tiempo de caída libre

- La eficiencia por tiempo de caída libre `ε_ff` es la fracción de la masa de una nube que se convierte en estrellas por cada `t_ff`.

💡 **Cómo se explica en la clase [B25-C05](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md):**
- Estimar una tasa de formación estelar a partir de una eficiencia por tiempo de caída libre.
- 🎯 **Por qué importa:** Una galaxia no convierte todo su gas en estrellas a la vez: lo hace a un ritmo que puede medirse y comparar. Entender las regiones donde nacen las estrellas masivas permite reconocerlas desde lejos, y entender la relación entre gas y ritmo de formación permite saber cuánto tiempo puede una galaxia seguir formando estrellas.

📘 **Dónde se aprende** (1 clase): [B25-C05 · Regiones de formación estelar](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md).

### Eficiencia propulsiva

- La eficiencia propulsiva es `η_p = F V₀/{ṁ[½(1+f)V_e² − ½V₀²]}`.

💡 **Cómo se explica en la clase [B79-C16](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md):**
- La eficiencia propulsiva es cero con el avión parado (todo el empuje es estático y ninguna potencia útil) y sube con la velocidad; la térmica sube con el Mach por la compresión dinámica de la toma.
- *Descripción textual:* la energía del combustible se convierte en energía cinética del chorro y esta en potencia propulsiva; la eficiencia global es el producto de las dos.
- 🎯 **Por qué importa:** Ninguna clase cubre cómo se cuantifica la conversión de energía en propulsión. Sin eficiencias separadas, un cambio de diseño se evalúa a ciegas: no se sabe si mejora el ciclo o el aprovechamiento del chorro.

📘 **Dónde se aprende** (1 clase): [B79-C16 · Eficiencias termodinámicas de motores](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md).

### Eficiencia radiativa

- La eficiencia radiativa `η` es la fracción de la energía en reposo acretada que se emite como luz: `L = η Ṁ c²`, con `Ṁ` la masa acretada por unidad de tiempo.
- La eficiencia radiativa `η = 1 − E_ISCO`.

💡 **Cómo se explica en la clase [B25-C11](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md):**
- Definir AGN, acreción, eficiencia radiativa, luminosidad de Eddington y sombra de un agujero negro.
- Obtener la eficiencia radiativa de un agujero sin rotación desde la órbita estable más interna.
- 🎯 **Por qué importa:** Algunas galaxias tienen en el centro una fuente que supera a todas sus estrellas, y casi todas las galaxias grandes albergan un agujero negro supermasivo. Entender el AGN une el centro de la galaxia, su gas y su evolución.

📘 **Dónde se aprende** (2 clases): [B25-C11 · Núcleos activos de galaxias](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md); [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md).

### Eficiencia relativa

- La eficiencia relativa compara las varianzas de dos estimadores en datos que cumplen el modelo ideal.

🎯 **Por qué importa (clase B12-C11):** Los datos reales traen errores de transmisión, rayos cósmicos en un detector, una lectura perdida o un salto del sensor. Un solo punto muy alejado puede torcer la recta de mínimos cuadrados y producir parámetros y predicciones erróneos con errores típicos pequeños y engañosos.

📘 **Dónde se aprende** (1 clase): [B12-C11 · Regresión robusta](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md).

### Eficiencia térmica

- La eficiencia térmica es `η_th = [½(1+f)V_e² − ½V₀²]/(f Q_R)`.

💡 **Cómo se explica en la clase [B79-C16](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md):**
- La eficiencia propulsiva es cero con el avión parado (todo el empuje es estático y ninguna potencia útil) y sube con la velocidad; la térmica sube con el Mach por la compresión dinámica de la toma.
- Descripción larga: la eficiencia térmica y la propulsiva suben con la velocidad de vuelo, y la global es su producto.
- ⚠️ **Error frecuente:** Maximizar solo la eficiencia térmica. Se corrige con 8.3.
- 🎯 **Por qué importa:** Ninguna clase cubre cómo se cuantifica la conversión de energía en propulsión. Sin eficiencias separadas, un cambio de diseño se evalúa a ciegas: no se sabe si mejora el ciclo o el aprovechamiento del chorro.

📘 **Dónde se aprende** (1 clase): [B79-C16 · Eficiencias termodinámicas de motores](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md).

### Eficiencia total

- La eficiencia total `η = P_jet/P_in` incluye todas las pérdidas.

🎯 **Por qué importa (clase B78-C06):** Subir el `Isp` ahorra propelente, pero el mismo vatio produce menos empuje y la maniobra tarda más. La decisión central: ¿cuánto empuje da cada kilovatio, cómo cae con el `Isp` y qué pasa con el tiempo de maniobra?

📘 **Dónde se aprende** (1 clase): [B78-C06 · Propulsión eléctrica general](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md).

### Eficiencia útil

- La eficiencia útil `E(ψ, δ) = cos δ · |sin(ψ − δ)|` combina la proyección del empuje sobre la dirección deseada (`cos δ`) y la fracción de potencia disponible (`|sin(ψ − δ)|`, la incidencia del Sol sobre el panel).

💡 **Cómo se explica en la clase [B81-C06](../programa/clases/B81/B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md):**
- *Descripción textual:* el ángulo entre Sol y empuje y el desvío elegido fijan la potencia y la proyección útil del empuje; su producto es la eficiencia, que se optimiza con o sin cono.
- Escribir la eficiencia útil `E(ψ, δ) = cos δ · |sin(ψ − δ)|`.
- 🎯 **Por qué importa:** Una trayectoria óptima en el vacío no es necesariamente volable: el guiado debe respetar la orientación de los paneles. La decisión central: ¿cuánto conviene desviar el empuje de la dirección óptima para recuperar potencia, y dentro de qué cono?

📘 **Dónde se aprende** (1 clase): [B81-C06 · Restricciones de orientación del empuje](../programa/clases/B81/B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md).

### Eficiencia η

- Caudal `Q`: volumen de aire procesado por segundo. Eficiencia `η`: fracción retirada.

💡 **Cómo se explica en la clase [B106-C04](../programa/clases/B106/B106-C04-control-de-dioxido-de-carbono/CLASE.md):**
- Con un depurador de 10 L/s y 70 % de eficiencia (ilustrativos) queda en 2,48 mmHg, bajo el límite consultado de 3 mmHg; con 5 L/s llega a 4,95 mmHg.
- Rotular que caudal y eficiencia son ilustrativos y los límites consultados.
- 🎯 **Por qué importa:** Una cabina cerrada acumula el CO₂ de la tripulación hasta que un depurador lo retira. Si el depurador es insuficiente o falla, hay un tiempo finito antes de pasar los límites.

📘 **Dónde se aprende** (1 clase): [B106-C04 · Control de dióxido de carbono](../programa/clases/B106/B106-C04-control-de-dioxido-de-carbono/CLASE.md).

### Eficiente

- Un estimador eficiente la alcanza.

💡 **Cómo se explica en la clase [B15-C15](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md):**
- Método de los momentos: iguala promedios teóricos y observados; simple, pero menos eficiente.
- Máxima verosimilitud: eficiente para muestras grandes, con sesgo en pequeñas.
- 🎯 **Por qué importa:** Un telescopio recoge 100 fotones de una estrella y quieres su posición con la mayor exactitud posible. ¿Basta con promediar las posiciones?

📘 **Dónde se aprende** (1 clase): [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md).

### Einstein

- La energía de un mol de fotones (un einstein) es `N_A E`; en kJ/mol, `1 eV = 96,485 kJ/mol`.

🎯 **Por qué importa (clase B06-C18):** El hidrógeno de una nube o de una atmósfera puede ser ionizado por un fotón de longitud de onda menor que 91,2 nm. Un fotón de Lyman-alfa (121,6 nm) no lo ioniza desde el estado fundamental, pero tiene 22 veces la energía necesaria para evaporar una molécula de agua.

📘 **Dónde se aprende** (1 clase): [B06-C18 · Fotoquímica y radiación](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md).

### Einstein–de Sitter

- El corrimiento de transición `z_t` es aquel en que `ä = 0`. Einstein–de Sitter es el caso `Ω_m = 1`.
- El caso Einstein–de Sitter (EdS) tiene `Ωm = 1`.

💡 **Cómo se explica en la clase [B26-C13](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md):**
- Comparar con el universo de Einstein–de Sitter.
- Ejercicio 2 · con una pista. Calcula la edad de Einstein–de Sitter.
- 🎯 **Por qué importa:** La edad del universo, la distancia a una galaxia y el calendario de su historia salen de la ecuación de Friedmann. Con ella se interpreta cualquier parámetro cosmológico.

📘 **Dónde se aprende** (2 clases): [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md); [B36-C01 · Crecimiento lineal de perturbaciones de densidad](../programa/clases/B36/B36-C01-crecimiento-lineal-de-perturbaciones-de-densidad/CLASE.md).

### EIRP

- La EIRP es la potencia isotrópica equivalente radiada.
- La EIRP es `P_tx − L + G`.

💡 **Cómo se explica en la clase [B56-C16](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md):**
- Paso 1 · Datos. `S_min = 4,88 × 10⁻²⁶ W/m²`, `EIRP = 2 × 10¹³ W`.
- El ejemplo conductor sintético es un receptor de radio con `T_sis = 25 K`, `A_ef = 5000 m²`, `Δν = 1 Hz`, `τ = 100 s`, dos polarizaciones y `SNR = 10`, frente a un transmisor de `EIRP = 2 × 10¹³ W`.
- ⚠️ **Error frecuente:** Confundir EIRP y potencia del transmisor. Se corrige con el vocabulario.
- 🎯 **Por qué importa:** Buscar tecnología exige saber qué flujo mínimo detecta un receptor y qué potencia debería tener un transmisor a una distancia dada. La decisión central: dados la temperatura del sistema, el área efectiva, el ancho de banda y el tiempo de integración, ¿qué flujo mínimo se detecta y hasta qué distancia llega un transmisor dado?

📘 **Dónde se aprende** (2 clases): [B56-C16 · Tecnofirmas y búsqueda SETI](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md); [B91-C08 · Antenas de gran apertura y estaciones de espacio profundo](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md).

### EIRP espectral

- El EIRP espectral es la potencia isótropa equivalente por Hz.

💡 **Cómo se explica en la clase [B118-C17](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md):**
- Para quedar en el umbral a 1000 km habría que reducir el EIRP espectral en 46,9 dB.
- Calcular la densidad de flujo de un satélite a 1000 km con EIRP espectral −70 dBW/Hz.
- 🎯 **Por qué importa:** La radioastronomía opera en bandas donde la ITU asigna protección, pero las constelaciones numerosas y sus emisiones no deseadas pueden degradar la sensibilidad. La decisión central: ¿cuánto debe bajar una emisión para quedar por debajo del umbral de daño y de qué depende ese umbral?

📘 **Dónde se aprende** (1 clase): [B118-C17 · Interferencia radioastronómica](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md).

### Eje de Euler

- El eje de Euler de la maniobra es `(1; 2; 3)/√14`.

🎯 **Por qué importa (clase B87-C17):** Es el lazo central del subsistema de actitud. La decisión central: ¿cómo se eligen las ganancias para un tiempo de asentamiento dado, cómo se evita el camino largo (el cuaternión doble) y qué pasa cuando el par se satura?

📘 **Dónde se aprende** (1 clase): [B87-C17 · Control de tres ejes](../programa/clases/B87/B87-C17-control-de-tres-ejes/CLASE.md).

### Eje de rotación

- El eje de rotación es el conjunto de puntos que no se mueve.

💡 **Cómo se explica en la clase [B10-C12](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md):**
- En SPICE, la matriz `[w]ᵢ` «rota el sistema de coordenadas `w` radianes alrededor del eje `i` y rota los vectores `−w`» (S1): su matriz es la transpuesta de la activa.
- *Descripción textual:* para un mismo ángulo, la rotación activa aplica `R(θ)` y la pasiva aplica su transpuesta; los números se parecen pero los signos difieren, y confundirlas es el error más común.
- ⚠️ **Error frecuente:** Confundir rotación activa y pasiva (signo). Se corrige con los ejercicios 2 y 11.
- 🎯 **Por qué importa:** La Tierra gira una vuelta cada 23,93 horas: una estación de seguimiento ve pasar los satélites porque sus ejes locales rotan respecto del espacio inercial. Un satélite recibe órdenes expresadas en ejes terrestres y debe saber dónde están en ejes inerciales.

📘 **Dónde se aprende** (1 clase): [B10-C12 · Rotaciones en el plano y espacio](../programa/clases/B10/B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md).

### Eje de simetría

- El eje de simetría de la Tierra axisimétrica con J2 es `z`.

💡 **Cómo se explica en la clase [B23-C06](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md):**
- Girar 37° alrededor del eje `x` no es una simetría de J2.
- Con la tolerancia de 4,3 × 10⁻⁵ km: composición `2,8 × 10⁻⁸ km`, giro alrededor de `z` `2,9 × 10⁻⁷ km`, reflexión `0` (la simetría es exacta en coma flotante), unidades `3,0 × 10⁻¹⁰ km`, reversibilidad `3,6 × 10⁻⁶ km`.
- 🎯 **Por qué importa:** El movimiento de un satélite con achatamiento terrestre (J2) no tiene solución cerrada, y tu código no tiene un valor correcto con el que compararse.

📘 **Dónde se aprende** (1 clase): [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md).

### Eje horario

- El eje horario gira a esa velocidad.

💡 **Cómo se explica en la clase [B43-C12](../programa/clases/B43/B43-C12-montura-ecuatorial/CLASE.md):**
- *Descripción textual:* el eje horario gira a la velocidad sidérea; el tornillo añade un error periódico cuya deriva depende de la exposición.
- 🎯 **Por qué importa:** Una exposición larga solo es nítida si el error de seguimiento es menor que un píxel. La decisión central: ¿a qué velocidad hay que girar el eje horario y cuánto puede derivar la imagen durante la exposición?

📘 **Dónde se aprende** (1 clase): [B43-C12 · Montura ecuatorial](../programa/clases/B43/B43-C12-montura-ecuatorial/CLASE.md).

### Eje horizontal

- El eje horizontal suele llevar la variable que controlas o que ordena los datos, y el vertical la que responde.

💡 **Cómo se explica en la clase [B03-C15](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md):**
- En el eje horizontal va la variable que controlas o que ordena los datos (el semieje `a`); en el vertical, la que quieres explicar (el período `T`).
- El eje horizontal es el semieje mayor en unidades astronómicas, de 0,3 a 30; el vertical, el período en años, de 0,2 a 160.
- 🎯 **Por qué importa:** Las fichas de la NASA dan semiejes y períodos de los ocho planetas. En una tabla son 16 números.

📘 **Dónde se aprende** (1 clase): [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md).

### Eje intermedio

- El eje intermedio es el de momento de inercia intermedio.

💡 **Cómo se explica en la clase [B87-C01](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md):**
- Si es el intermedio, es positivo y hay crecimiento exponencial con
- Analogía: una peonza (trompo) que gira sobre su eje largo es estable, igual que un giro sobre el eje de mayor o menor inercia; una raqueta lanzada al aire girando sobre su eje intermedio da una vuelta extra impredecible.
- 🎯 **Por qué importa:** Un diseñador de actitud necesita saber qué hace el vehículo cuando nadie lo controla: ¿cuánto vale el momento angular, cómo se mueve el eje de giro y cuándo un giro aparentemente tranquilo se desestabiliza?

📘 **Dónde se aprende** (1 clase): [B87-C01 · Dinámica de cuerpo rígido](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md).

### Eje mayor

- El eje menor y el eje mayor (`a√2`).

💡 **Cómo se explica en la clase [B41-C16](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md):**
- Ejercicio 3 · casi autónomo. Eje mayor con `a = 43,4`.
- eje menor del plano a = w + (D - w) q/F = 43.40 mm ; eje mayor (a por raiz de 2) = 61.38 mm
- 🎯 **Por qué importa:** El Newton es el reflector más simple y el Dobson su montura más barata. La decisión central: ¿qué tamaño de plano y qué ocular conviene?

📘 **Dónde se aprende** (1 clase): [B41-C16 · Telescopios Newton y Dobson](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md).

### Eje menor

- El eje menor y el eje mayor (`a√2`).

💡 **Cómo se explica en la clase [B41-C16](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md):**
- Calcular el eje menor del plano `a = w + (D−w) q/F`.
- eje menor del plano a = w + (D - w) q/F = 43.40 mm ; eje mayor (a por raiz de 2) = 61.38 mm
- 🎯 **Por qué importa:** El Newton es el reflector más simple y el Dobson su montura más barata. La decisión central: ¿qué tamaño de plano y qué ocular conviene?

📘 **Dónde se aprende** (1 clase): [B41-C16 · Telescopios Newton y Dobson](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md).

### Eje nuevo

- Un eje nuevo (`None` o `np.newaxis`) inserta una dimensión de tamaño 1.

🎯 **Por qué importa (clase B14-C02):** Una constelación de seis satélites y cinco estaciones en tierra producen treinta distancias. Un catálogo de estrellas produce millones.

📘 **Dónde se aprende** (1 clase): [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md).

### Eje óptico

- Pivote: punto donde se cruzan los ejes. Eje óptico: recta de apuntado.
- Campo de visión (FOV): ángulo total del cono de la cámara. Eje óptico: dirección central.

💡 **Cómo se explica en la clase [B48-C08](../programa/clases/B48/B48-C08-automatizacion-de-cupulas/CLASE.md):**
- Escribir la recta del eje óptico desde el punto de pivote.
- 🎯 **Por qué importa:** Una ranura mal orientada viñetea o bloquea el haz. La decisión central: ¿qué azimut debe tener la cúpula para un telescopio descentrado?

📘 **Dónde se aprende** (2 clases): [B48-C08 · Automatización de cúpulas](../programa/clases/B48/B48-C08-automatizacion-de-cupulas/CLASE.md); [B101-C09 · Coordinación visual y cámaras en operaciones con manipulador](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md).

### Eje polar

- Las coordenadas polares `(r, θ)` la dan por la distancia `r` a un origen (el polo) y el ángulo `θ` medido desde un eje polar.

💡 **Cómo se explica en la clase [B04-C10](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md):**
- De polares a cartesianas: `x = r cos θ`, `y = r sen θ`.
- De cartesianas a polares: `r = √(x² + y²)` y `θ = atan2(y, x)`.
- ⚠️ **Error frecuente:** Confundir el eje polar. El perihelio es `θ = 0`.
- 🎯 **Por qué importa:** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.

📘 **Dónde se aprende** (1 clase): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md).

### Eje principal

- Un eje principal es un eje para el que `ω` paralelo a él da `H` paralelo.

💡 **Cómo se explica en la clase [B16-C17](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md):**
- Hay tres ejes principales: el mayor (J = 50), el intermedio (40) y el menor (30).
- Aquí trabajamos con un cuerpo sintético de inercias principales `(50, 40, 30) kg·m²` y velocidades iniciales `(0,10; 0,05; −0,08) rad/s`.
- ⚠️ **Error frecuente:** Creer que todos los ejes principales son igual de estables. Se corrige con los ejercicios 2, 3 y 9.
- 🎯 **Por qué importa:** Cuando un satélite se separa del cohete puede salir girando de forma desordenada («volteando»).

📘 **Dónde se aprende** (1 clase): [B16-C17 · Control no lineal](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md).

### Eje-ángulo

- El eje-ángulo `(n, φ)` cumple `q = [n sin(φ/2); cos(φ/2)]`.

💡 **Cómo se explica en la clase [B87-C02](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md):**
- *Descripción textual:* la rotación es una sola; la matriz y el cuaternión se convierten sin pérdida, el eje-ángulo es una lectura geométrica del cuaternión y Euler es la forma legible pero singular; el producto de cuaterniones compone rotaciones.
- Analogía: una misma dirección puede darse como «40° al noreste» (Euler), como un vector (matriz) o como una brújula con un giro (eje-ángulo); cada forma es buena para algo.
- 🎯 **Por qué importa:** Casi todos los errores de actitud en software vienen de convenciones mezcladas: orden de ejes, sentido de la rotación, posición de la parte escalar. La decisión central: ¿qué representación uso para integrar, cuál para filtrar y cuál para mostrar?

📘 **Dónde se aprende** (1 clase): [B87-C02 · Representaciones de orientación](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md).

### Ejecta distal

- El manto de ejecta es el depósito continuo; la ejecta distal es la que llega más lejos.

🎯 **Por qué importa (clase B61-C04):** El manto de ejecta es un marcador estratigráfico: cubre lo anterior y es cubierto por lo posterior. La decisión central: ¿cómo decae el espesor con la distancia y cuánto volumen contiene el manto?

📘 **Dónde se aprende** (1 clase): [B61-C04 · Mantos de ejecta y depósitos de impacto](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md).

### Ejecutiva

- La capa reactiva (reflejos) responde al ritmo del sensor; la ejecutiva interpreta el plan y vigila su ejecución; la deliberativa planifica.

💡 **Cómo se explica en la clase [B98-C07](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md):**
- D["deliberativa<br/>planifica (minutos)"] --> X["ejecutiva<br/>secuencia y vigila (1 s)"]
- *Descripción textual:* el planificador lento fija los objetivos; la ejecutiva los convierte en acciones y vigila; la reactiva actúa sobre los actuadores con lo percibido y puede interrumpir.
- 🎯 **Por qué importa:** Una arquitectura sin presupuesto de tiempos puede parecer correcta hasta que una tarea lenta retrasa un reflejo. La decisión central: ¿cada capa cumple sus plazos aunque las demás consuman su peor caso, y qué pasa cuando el planificador tarda más de lo previsto?

📘 **Dónde se aprende** (1 clase): [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md).

### Ejecutor

- Ejecutor: programa que corre una secuencia.

💡 **Cómo se explica en la clase [B96-C24](../programa/clases/B96/B96-C24-operacion-remota-y-automatizada-de-estaciones/CLASE.md):**
- El ejecutor de esta clase es un modelo sintético de banco, no una implementación de esas normas.
- Tras agotar los reintentos el ejecutor aborta.
- 🎯 **Por qué importa:** Un ejecutor automático sin límites puede colgarse o comandar con el enlace caído. La decisión central: ¿qué debe garantizar el ejecutor ante cualquier combinación de fallos y cómo se prueba?

📘 **Dónde se aprende** (1 clase): [B96-C24 · Operación remota y automatizada de estaciones](../programa/clases/B96/B96-C24-operacion-remota-y-automatizada-de-estaciones/CLASE.md).

### Ejes

- Una figura (`Figure`) es el lienzo completo; los ejes (`Axes`) son la región donde se dibujan los datos, con sus dos ejes de coordenadas (`Axis`) que fijan escala, límites y marcas (S2).
- Su forma (`shape`) es la tupla de longitudes por eje; sus ejes se numeran desde 0.

💡 **Cómo se explica en la clase [B07-C10](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md):**
- `ax.loglog(x, y)` usa escala logarítmica en ambos ejes: las separaciones iguales son factores iguales, y los ocho puntos se ven distribuidos.
- D["datos<br/>a, T (arreglos)"] --> E["ejes<br/>escala, etiquetas, unidades"]
- ⚠️ **Error frecuente:** Ejes sin unidades. Se corrige con la sección 8.2 y el ejercicio 8.
- 🎯 **Por qué importa:** Un gráfico es una afirmación: dice «mira esta relación». Un gráfico sin unidades, con una escala que esconde la mitad de los datos o sin leyenda puede inducir a error aunque los números sean correctos.

📘 **Dónde se aprende** (2 clases): [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md); [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md).

### Ejes de coordenadas

- Una figura (`Figure`) es el lienzo completo; los ejes (`Axes`) son la región donde se dibujan los datos, con sus dos ejes de coordenadas (`Axis`) que fijan escala, límites y marcas (S2).

🎯 **Por qué importa (clase B07-C10):** Un gráfico es una afirmación: dice «mira esta relación». Un gráfico sin unidades, con una escala que esconde la mitad de los datos o sin leyenda puede inducir a error aunque los números sean correctos.

📘 **Dónde se aprende** (1 clase): [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md).

### Ejes paralelos

- Tensor de inercia: matriz de momentos y productos de inercia. Ejes paralelos: teorema para trasladar la inercia.

💡 **Cómo se explica en la clase [B90-C06](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md):**
- Calcular el centro de masa y el tensor de inercia de un ensamble por ejes paralelos.
- 🎯 **Por qué importa:** Un perno mal apretado se afloja con la vibración o se rompe por exceso de carga; un centro de masa fuera de rango desvía la nave en el despliegue. La decisión central: ¿qué par de apriete garantiza que la unión no se separe ni se plastifique, y el conjunto queda dentro de los límites de masa?

📘 **Dónde se aprende** (1 clase): [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md).

### Ejes principales

- Los ejes principales de un tensor de inercia son sus autovectores; los momentos principales, sus autovalores.
- Los ejes principales lo diagonalizan; sus momentos son `I₁`, `I₂`, `I₃`.
- La descomposición espectral `P = V Λ Vᵀ` da los ejes principales (columnas de `V`) y las varianzas a lo largo de ellos (autovalores `λ`).

💡 **Cómo se explica en la clase [B10-C08](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md):**
- Los tensores de inercia son simétricos, por lo que sus ejes principales son perpendiculares.
- Los ejes principales están girados 22,5° respecto de los del cuerpo: un instrumento o un volante alineado con `x` no está sobre un eje principal.
- 🎯 **Por qué importa:** Un satélite que rota libremente no gira igual alrededor de cualquier eje: tiene tres ejes especiales —los ejes principales de inercia— en los que la rotación es simple. Conocerlos permite diseñar su estabilización, decidir dónde colocar instrumentos sensibles al giro y entender por qué ciertos giros se desestabilizan.

📘 **Dónde se aprende** (3 clases): [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B12-C18 · Matrices de covarianza](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md); [B87-C01 · Dinámica de cuerpo rígido](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md).

### EKF

- El EKF linealiza la dinámica y la medida alrededor de la estimación actual.

💡 **Cómo se explica en la clase [B74-C09](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md):**
- El ajuste por lotes de los mismos datos, propagado al instante final, difiere del EKF en `1,037 m`: la pequeña diferencia es el efecto de linealizar paso a paso.
- Límite: el EKF usa solo la derivada primera; con errores iniciales grandes la aproximación falla.
- ⚠️ **Error frecuente:** Creer que el EKF siempre es consistente. Comprueba el NEES, como en 8.4.
- 🎯 **Por qué importa:** Una órbita no es lineal en el estado, pero a cortos intervalos y con errores pequeños se comporta casi como tal. La decisión central: ¿hasta cuándo es válida la linealización del EKF y cómo me doy cuenta de que dejó de serlo?

📘 **Dónde se aprende** (1 clase): [B74-C09 · Filtro de Kalman extendido](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md).

### Elasticidad

- La elasticidad `Sᵢ = (∂y/∂xᵢ)(xᵢ/y)` es adimensional: el cambio relativo de `y` por cada cambio relativo de `xᵢ`.
- La elasticidad `ε` mide la sensibilidad de la demanda.

💡 **Cómo se explica en la clase [B12-C17](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md):**
- A["Modelo y = f(x₁…x_N)<br/>+ incertidumbre de cada xᵢ"] --> B["Local: cᵢ = ∂f/∂xᵢ<br/>elasticidad Sᵢ"]
- *Descripción textual:* el modelo y las incertidumbres de entrada alimentan dos análisis: el local, con derivadas, elasticidades y contribuciones de varianza; y el global, con índices de Sobol que capturan no linealidad e interacciones; ambos orientan qué entrada mejorar.
- ⚠️ **Error frecuente:** Comparar derivadas de unidades distintas. Se corrige con las elasticidades (8.2) y el ejercicio 2.
- 🎯 **Por qué importa:** Mejorar una medida cuesta dinero, masa o tiempo. Si el presupuesto de una misión ofrece mejorar la masa seca o el empuje específico, hay que saber cuál de las dos reduce más la incertidumbre del resultado.

📘 **Dónde se aprende** (2 clases): [B12-C17 · Análisis de sensibilidad](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md); [B124-C03 · Mercados downstream y upstream](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md).

### ELBO

- El ELBO (*evidence lower bound*) es `E_q[log p(y, θ)] − E_q[log q(θ)]`.

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- En cambio, el ELBO es una esperanza respecto de `q`, que se puede calcular o estimar si `q` es sencilla.
- Maximizar el ELBO sobre `φ` es una optimización.
- ⚠️ **Error frecuente:** Pensar que `ELBO` alto significa aproximación fiel. Ejercicios 7 y 11.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.

📘 **Dónde se aprende** (1 clase): [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### Elección del paso nuevo

- La elección del paso nuevo usa `h · 0,9 · err^{−1/5}` para un método de orden 4, acotado entre `0,2 h` y `5 h`.

🎯 **Por qué importa (clase B11-C08):** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.

📘 **Dónde se aprende** (1 clase): [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md).

### Electrólisis

- Electrólisis: `2 H₂O → 2 H₂ + O₂`.

💡 **Cómo se explica en la clase [B106-C05](../programa/clases/B106/B106-C05-suministro-y-generacion-de-oxigeno/CLASE.md):**
- A["agua"] -->|"electrolisis"| B["O2 a la cabina"]
- *Descripción textual:* la electrólisis da O₂ y H₂ desde el agua; el H₂ reacciona con el CO₂ exhalado y devuelve agua y metano.
- 🎯 **Por qué importa:** Llevar oxígeno comprimido o líquido pesa; electrolizar agua exige energía y reponer agua. La decisión central: ¿cuánta agua, hidrógeno y energía implica producir el oxígeno de una tripulación y qué parte del agua devuelve la reacción de Sabatier?

📘 **Dónde se aprende** (1 clase): [B106-C05 · Suministro y generación de oxígeno](../programa/clases/B106/B106-C05-suministro-y-generacion-de-oxigeno/CLASE.md).

### Electrólisis de óxido sólido

- La electrólisis de óxido sólido usa una cerámica que conduce iones de oxígeno a alta temperatura.

💡 **Cómo se explica en la clase [B59-C08](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md):**
- La nota de NASA (S4) informa de picos de 10,44 g/h (sol 534) y casi 10,56 g/h (sol 630) de O₂ por electrólisis de óxido sólido de CO₂, frente a una meta de diseño de 6 g/h, y de 9,79 g/h sostenidos casi 40 min.
- 🎯 **Por qué importa:** Un oxidante producido en destino se mide en gramos por hora, pero el diseñador piensa en amperios y vatios. La decisión central: ¿qué corriente y qué potencia exige una tasa de oxígeno dada?

📘 **Dónde se aprende** (1 clase): [B59-C08 · Producción de oxígeno](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md).

### Electrones

- Tiene un núcleo, minúsculo y denso, formado por protones (carga positiva) y neutrones (sin carga), y a su alrededor electrones (carga negativa).

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Un átomo de hidrógeno ordinario tiene un protón y un electrón; el helio, dos protones (`Z = 2`); el carbono, seis.
- La masa está casi toda en el núcleo: un protón pesa unas 1836 veces más que un electrón (S1).
- ⚠️ **Error frecuente:** Creer que el electrón «gira» como un planeta. Es una imagen del modelo, no una descripción física completa (sección 8.5).
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.

📘 **Dónde se aprende** (1 clase): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md).

### Electrones de valencia

- Los electrones de la capa más externa son los electrones de valencia y determinan en buena medida cómo reacciona el elemento.
- Los electrones de valencia son los de la capa externa (C02).

💡 **Cómo se explica en la clase [B06-C02](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md):**
- ¿Cuántos electrones tiene el átomo neutro y cuántos de valencia?
- 🎯 **Por qué importa:** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?

📘 **Dónde se aprende** (2 clases): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md); [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Electrones por O₂

- Los electrones por O₂ son 4.

💡 **Cómo se explica en la clase [B59-C08](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md):**
- Como una cinta que mueve una caja de oxígeno por cada cuatro electrones: la tasa depende de la corriente.
- Escribir la reacción global `2 CO₂ → 2 CO + O₂` y sus 4 electrones por O₂.
- ⚠️ **Error frecuente:** Usar 2 electrones por O₂. Son 4; se corrige con 8.1.
- 🎯 **Por qué importa:** Un oxidante producido en destino se mide en gramos por hora, pero el diseñador piensa en amperios y vatios. La decisión central: ¿qué corriente y qué potencia exige una tasa de oxígeno dada?

📘 **Dónde se aprende** (1 clase): [B59-C08 · Producción de oxígeno](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md).

### Electroneutralidad

- La electroneutralidad exige que las cargas positivas y negativas sumen lo mismo.

💡 **Cómo se explica en la clase [B115-C03](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md):**
- Electroneutralidad: cationes `6 + 2·5 + 2·2 = 20 meq/L`; aniones `15 + 1 + 2·2 = 20 meq/L`.
- Comprobar la electroneutralidad de una solución.
- 🎯 **Por qué importa:** Una solución nutritiva que se repone «por conductividad» puede parecer estable y estar desequilibrada. La decisión central: ¿qué se mide, cada cuánto y qué se repone para que cada ion se mantenga cerca de su objetivo, y cuándo conviene renovar la solución?

📘 **Dónde se aprende** (1 clase): [B115-C03 · Control de nutrientes y solución nutritiva](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md).

### Elemento de configuración

- Un elemento de configuración (CI) es un producto bajo control (documento, plano, software).

💡 **Cómo se explica en la clase [B83-C15](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md):**
- C["Elementos de configuracion"] --> H["Huella SHA-256 de cada uno"]
- ESTRELLA-S (sintética) tiene 6 elementos de configuración y una línea base con huella `c4bbd14a0918…`.
- 🎯 **Por qué importa:** Si nadie sabe qué versión de qué documento se ensayó, no se puede demostrar nada. La decisión central: ¿la configuración actual es la aprobada, y qué se afecta si apruebo este cambio?

📘 **Dónde se aprende** (1 clase): [B83-C15 · Gestión de configuración](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md).

### Elemento de resolución

- El elemento de resolución es la imagen de la rendija.

🎯 **Por qué importa (clase B45-C06):** El diseño se decide con unos pocos parámetros que se compensan entre sí. La decisión central: ¿qué ancho de rendija da la resolución deseada y cuántos píxeles muestrean cada elemento?

📘 **Dónde se aprende** (1 clase): [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md).

### Elemento indefinido

- Un elemento indefinido es el que pierde sentido en un límite (aquí `ω` si `e = 0`).

🎯 **Por qué importa (clase B71-C12):** Un elemento mal condicionado puede dar un valor sin sentido aunque el estado sea exacto. La decisión central: ¿cuándo puedes fiarte de `ω` y qué ángulo usas cuando no?

📘 **Dónde se aprende** (1 clase): [B71-C12 · Argumento del periapsis](../programa/clases/B71/B71-C12-argumento-del-periapsis/CLASE.md).

### Elemento medio

- El elemento medio es su promedio sobre las oscilaciones de corto periodo.

💡 **Cómo se explica en la clase [B72-C12](../programa/clases/B72/B72-C12-variaciones-de-elementos-osculadores/CLASE.md):**
- Para propagar con un modelo medio hay que partir de elementos medios; para una efeméride exacta, de osculadores del mismo modelo.
- El conjunto de elementos del catálogo de dos líneas contiene elementos medios del modelo SGP4 ([C21](../B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md)), no osculadores.
- ⚠️ **Error frecuente:** Mezclar elementos medios y osculadores. Se corrige con 8.5.
- 🎯 **Por qué importa:** Un catálogo publica elementos de un instante; usarlos como si fueran constantes introduce errores de kilómetros. La decisión central: ¿cuánto difiere un elemento osculador del medio y qué error de fase o de periodo produce usar el equivocado?

📘 **Dónde se aprende** (1 clase): [B72-C12 · Variaciones de elementos osculadores](../programa/clases/B72/B72-C12-variaciones-de-elementos-osculadores/CLASE.md).

### Elemento osculador

- Un elemento osculador es el elemento kepleriano de la órbita que seguiría el satélite si las perturbaciones se apagaran en ese instante.
- Un elemento osculador es el elemento instantáneo, con oscilaciones de corto periodo.
- El elemento osculador corresponde al estado `(r, v)` de un instante.

💡 **Cómo se explica en la clase [B72-C03](../programa/clases/B72/B72-C03-perturbacion-j2-terrestre/CLASE.md):**
- Los elementos osculadores oscilan con el periodo orbital con amplitudes que dependen de `J2` y, para `ω`, de `1/e`; con `e = 0,001` el ajuste de `ω` fallaba un `8 %`, y por eso se usó `e = 0,02`.
- N["integracion RK4"] --> E["elementos osculadores"]
- ⚠️ **Error frecuente:** Confundir elemento osculador con medio. Se corrige con el vocabulario.
- 🎯 **Por qué importa:** J2 no cambia el semieje mayor ni la inclinación en promedio, pero hace girar el plano y el perigeo; con ello se diseñan órbitas heliosíncronas y Molniya. La decisión central: ¿cuánto se mueven `Ω` y `ω` por día en una órbita dada y cuánto confiar en la fórmula de primer orden?

📘 **Dónde se aprende** (3 clases): [B72-C01 · Limitaciones del problema de dos cuerpos](../programa/clases/B72/B72-C01-limitaciones-del-problema-de-dos-cuerpos/CLASE.md); [B72-C03 · Perturbación J2 terrestre](../programa/clases/B72/B72-C03-perturbacion-j2-terrestre/CLASE.md); [B72-C12 · Variaciones de elementos osculadores](../programa/clases/B72/B72-C12-variaciones-de-elementos-osculadores/CLASE.md).

### Elemento volátil

- Un elemento volátil es el que pasa fácilmente a fase gaseosa; los elementos refractarios son los que permanecen sólidos a altas temperaturas.

💡 **Cómo se explica en la clase [B06-C20](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md):**
- Con la tabla de S1 (C02 y el script de la sección 17), para 17 elementos no volátiles de sodio a zinc, la media de `Δ` es `+0,002 dex` y la dispersión `0,052 dex`: coinciden dentro de 0,05 dex (un 12 %), como informa la fuente para su muestra más grande (S1).
- Si uno discrepa para ciertos elementos, hay una razón física: el material perdió elementos volátiles al formarse o el elemento se destruye en el Sol.
- 🎯 **Por qué importa:** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.

📘 **Dónde se aprende** (1 clase): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### Elementos

- Una malla divide el intervalo en `N` elementos de longitud `h`.

💡 **Cómo se explica en la clase [B11-C15](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md):**
- Con malla uniforme, `φ_i′ = ±1/h` en los dos elementos que comparten el nodo `i`.
- Para `−u″ = 1` (o `−k T″ = q`), la solución exacta es cuadrática y los valores nodales del método lineal resultan exactos (propiedad de los elementos lineales 1D).
- 🎯 **Por qué importa:** Las estructuras y los escudos de una nave no son barras rectas con mallas regulares. El análisis térmico y estructural de ingeniería espacial se hace casi siempre con elementos finitos sobre geometrías reales.

📘 **Dónde se aprende** (1 clase): [B11-C15 · Elementos finitos introductorios](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md).

### Elementos medios

- Los elementos medios son parámetros promedio que no sirven para efemérides.

💡 **Cómo se explica en la clase [B75-C16](../programa/clases/B75/B75-C16-navegacion-relativa-a-lunas/CLASE.md):**
- Ejercicio 11 · transferencia. Las tablas del JPL advierten que los elementos son medios.
- Límites: órbitas lunares circulares, elementos medios, nave sin perturbaciones.
- ⚠️ **Error frecuente:** Usar elementos medios como efemérides. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Para navegar en un sistema de lunas hay que saber en qué marco se mide cada cosa y qué tan grande es la esfera de influencia de cada luna. La decisión central: ¿con qué velocidad relativa llega una nave a cada luna y cuán grande es la región donde la luna manda?

📘 **Dónde se aprende** (1 clase): [B75-C16 · Navegación relativa a lunas](../programa/clases/B75/B75-C16-navegacion-relativa-a-lunas/CLASE.md).

### Elementos orbitales

- Los elementos orbitales son `P`, `a`, `e`, `ω`, `M₀`, `i`.

🎯 **Por qué importa (clase B29-C09):** La excentricidad y el argumento del periastro cambian la forma de la curva y el sesgo de `K` que vimos en C03. Y la densidad de la estrella que sale del tránsito ayuda a validar al anfitrión.

📘 **Dónde se aprende** (1 clase): [B29-C09 · Parámetros orbitales exoplanetarios](../programa/clases/B29/B29-C09-parametros-orbitales-exoplanetarios/CLASE.md).

### Elementos osculadores

- Los elementos osculadores son los de la órbita kepleriana que coincide con el estado instantáneo.

🎯 **Por qué importa (clase B23-C05):** Un modelo kepleriano de la Tierra pasó todas las pruebas de C01–C04, pero eso no dice nada sobre si la Tierra se mueve como una elipse perfecta. La pregunta motivadora es: ¿contra qué contrasto mi modelo, y qué diferencia estoy dispuesto a aceptar?

📘 **Dónde se aprende** (1 clase): [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md).

### Elementos refractarios

- Un elemento volátil es el que pasa fácilmente a fase gaseosa; los elementos refractarios son los que permanecen sólidos a altas temperaturas.

🎯 **Por qué importa (clase B06-C20):** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.

📘 **Dónde se aprende** (1 clase): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### Elevación

- La elevación `ΔP_g = ρ_l g h` se opone al retorno.

💡 **Cómo se explica en la clase [B51-C10](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md):**
- Como mirar a través de una ventana: de frente atraviesas un vidrio fino y casi sin retraso; muy inclinado atraviesas mucho más grosor, y por eso el mismo vidrio retrasa más a baja elevación.
- *Descripción textual:* el retardo troposférico se mapea con la elevación y el ionosférico se elimina con dos frecuencias.
- ⚠️ **Error frecuente:** Usar `1/sin e` a baja elevación. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un error atmosférico de centímetros es un error de posición en geodesia y un error de fase en imagen. La decisión central: ¿cómo se mapea el retardo con la elevación y cómo se separa lo dispersivo de lo no dispersivo?

📘 **Dónde se aprende** (2 clases): [B51-C10 · Retardo troposférico e ionosférico en VLBI y su modelado](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md); [B85-C09 · Tubos de calor](../programa/clases/B85/B85-C09-tubos-de-calor/CLASE.md).

### Elevación de órbita

- La elevación de órbita con empuje tangencial necesita `Δv = v₁ − v₂`.

💡 **Cómo se explica en la clase [B78-C22](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md):**
- Calcular el Δv por día y el tiempo de elevación de órbita.
- 🎯 **Por qué importa:** El Δv diario de un propulsor eléctrico es el ideal multiplicado por el ciclo de trabajo, y este puede ser menos de la mitad. La decisión central: ¿cuánto tiempo del día puede empujar un propulsor ilustrativo y cuánto tarda entonces en elevar la órbita?

📘 **Dónde se aprende** (1 clase): [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md).

### Elevación del horizonte

- La elevación del horizonte `e` es la altura angular de la línea del terreno (una cumbre, un cerro) sobre el horizonte matemático.

💡 **Cómo se explica en la clase [B133-C01](../programa/clases/B133/B133-C01-relaciones-entre-cielo-y-territorio-en-los-saberes-tradicionales/CLASE.md):**
- Para un borde superior que toca un horizonte de elevación `e`, `h = e − 0,833°` (radio solar 0,267° más refracción 0,566°).
- Calcular el acimut de salida del sol a partir de la latitud, la declinación y la elevación del horizonte.
- 🎯 **Por qué importa:** Los saberes del cielo se enseñan a menudo como listas de constelaciones o de relatos sueltos, sin el territorio que los sostiene. La decisión central: ¿qué puede decir una geometría astronómica sobre una práctica ligada a un lugar, y qué le corresponde decir solo a quienes la portan?

📘 **Dónde se aprende** (1 clase): [B133-C01 · Relaciones entre cielo y territorio en los saberes tradicionales](../programa/clases/B133/B133-C01-relaciones-entre-cielo-y-territorio-en-los-saberes-tradicionales/CLASE.md).

### Elevación del perigeo

- La elevación del perigeo es el aumento de la altitud mínima en la órbita de disposición.

💡 **Cómo se explica en la clase [B118-C12](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md):**
- GEO: elevacion minima del perigeo 235 + 1000 CR A/m (CR = 1.3) y dv de dos impulsos:
- 🎯 **Por qué importa:** La disposición es la principal medida de mitigación: en LEO, que la vida residual sea corta; en GEO, que el satélite quede por encima de la región protegida. La decisión central: ¿desde qué altitud se puede dejar un satélite en LEO para que decaiga en 25 años, y cuánta elevación necesita un satélite de GEO?

📘 **Dónde se aprende** (1 clase): [B118-C12 · Disposición al fin de vida](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md).

### Elevación máxima

- Ventana: intervalo con elevación ≥ mínima. Elevación máxima: pico de la pasada.

💡 **Cómo se explica en la clase [B96-C04](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md):**
- Un filtro de elevación máxima ≥ 25° deja 2 pasadas y 14,1 min: las de baja elevación tienen señal más débil y se usan para tareas cortas.
- Paso 5 · Filtrar. Elevación máxima ≥ 25°: 2 pasadas, 14,1 min.
- 🎯 **Por qué importa:** Un contacto perdido por mala planificación no se recupera hasta la siguiente pasada, que puede estar a horas. La decisión central: ¿qué ventanas hay, cuánto duran y cuáles merece la pena usar?

📘 **Dónde se aprende** (1 clase): [B96-C04 · Planificación de contactos](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md).

### Elevación mínima

- La elevación mínima es el límite de observación.

💡 **Cómo se explica en la clase [B118-C16](../programa/clases/B118/B118-C16-contaminacion-luminica/CLASE.md):**
- Campo, exposición, horario, elevación mínima, número de satélites y método de conteo; sin ellos no se puede contrastar.
- 🎯 **Por qué importa:** El brillo y el número de satélites visibles dependen de la altitud y de la profundidad del Sol bajo el horizonte; para un telescopio, una traza arruina la zona que cruza. La decisión central: ¿cuánto dura la ventana de iluminación, qué tan brillante es el satélite y cuántas trazas esperar en una exposición?

📘 **Dónde se aprende** (1 clase): [B118-C16 · Contaminación lumínica](../programa/clases/B118/B118-C16-contaminacion-luminica/CLASE.md).

### Eliminación

- La eliminación suma o resta ecuaciones multiplicadas por números para anular una incógnita.

💡 **Cómo se explica en la clase [B04-C03](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md):**
- Se elimina la primera incógnita de las ecuaciones 2 y 3 usando la 1; luego se elimina la segunda de la 3.
- Resolver sistemas 2×2 por sustitución y por eliminación.
- 🎯 **Por qué importa:** Un detector no entrega «brillo»: entrega cuentas. Para convertir cuentas en flujo hay que descubrir dos números, una pendiente y un desfase, y para ello se miden dos fuentes de referencia.

📘 **Dónde se aprende** (1 clase): [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md).

### Eliminación gaussiana

- La eliminación gaussiana las usa para llegar a una forma triangular superior.

💡 **Cómo se explica en la clase [B10-C05](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md):**
- Resolver un sistema pequeño por eliminación gaussiana y sustitución hacia atrás.
- 🎯 **Por qué importa:** Para fijar la posición de un objeto a partir de las distancias a tres estaciones se plantean tres ecuaciones con dos incógnitas (plano). Los sistemas reales tienen decenas o miles de incógnitas: parámetros orbitales, sesgos de relojes, coeficientes de calibración.

📘 **Dónde se aprende** (1 clase): [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md).

### Elipse

- Una elipse es el conjunto de puntos para los que la suma de las distancias a dos puntos fijos, los focos, es constante.
- La elipse es el lugar de los puntos con suma constante de distancias a los focos.

💡 **Cómo se explica en la clase [B04-C09](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md):**
- Observa que es mucho menor que `2πa = 112,65 au`: el perímetro de una elipse muy aplastada no es el de la circunferencia de su semieje mayor.
- Clava dos chinchetas (los focos), ata un hilo de longitud `2a` y tensa con un lápiz: dibujas una elipse.
- 🎯 **Por qué importa:** Las órbitas de planetas y cometas son, en buena aproximación, elipses con el Sol en uno de sus focos. Si no sabes qué es un semieje, un foco o la excentricidad, no puedes leer una tabla de elementos orbitales ni distinguir una órbita casi circular, como la de la Tierra, de una muy alargada, como la del cometa Halley.

📘 **Dónde se aprende** (2 clases): [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B71-C08 · Órbitas elípticas](../programa/clases/B71/B71-C08-orbitas-elipticas/CLASE.md).

### Elipse 2:1

- La elipse 2:1 es `x = ρ cos nt`, `y = −2ρ sin nt`.

💡 **Cómo se explica en la clase [B76-C15](../programa/clases/B76/B76-C15-control-de-formacion-satelital/CLASE.md):**
- Con estado inicial `(ρ, 0, 0, 0, −2nρ, 0)`, `x` y `y` describen una elipse de eje `2ρ × 4ρ`.
- *Descripción textual:* una elipse de radio `ρ` se cierra sola; un error de semieje equivale a un error de velocidad que desplaza el centro radial y crea una deriva por órbita; un impulso opuesto la anula y su suma anual es el presupuesto.
- ⚠️ **Error frecuente:** Creer que una elipse pequeña no deriva. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un error de un metro en el semieje parece nada y deriva nueve metros por órbita. La decisión central: ¿cuánto se desvía una formación por un error de inserción y cuánto `Δv` cuesta mantenerla?

📘 **Dónde se aprende** (1 clase): [B76-C15 · Control de formación satelital](../programa/clases/B76/B76-C15-control-de-formacion-satelital/CLASE.md).

### Elipse de confianza

- La elipse de confianza tiene un área proporcional a `1/√det F`.

💡 **Cómo se explica en la clase [B26-C22](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md):**
- Interpretar el área de la elipse de confianza.
- 🎯 **Por qué importa:** Una incertidumbre marginal puede ser mucho mayor que la que se obtendría si el otro parámetro estuviera fijo, porque ambos se compensan. Sin analizar la degeneración se interpretan mal las barras de error y se desaprovechan las combinaciones de datos.

📘 **Dónde se aprende** (1 clase): [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md).

### Elipse de error

- La elipse de error es el conjunto `{e : eᵀP⁻¹e = c}`; sus semiejes son `√(c λᵢ)`.

💡 **Cómo se explica en la clase [B12-C18](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md):**
- B --> C["Autovalores y ejes<br/>→ elipse de error"]
- Hallar semiejes y orientación de la elipse de error y la del 95 % en 2D.
- 🎯 **Por qué importa:** El resultado de una determinación de órbita o de un ajuste no es un número sino un vector con una matriz de covarianza; sin ella no se puede propagar, comparar con otro resultado ni calcular probabilidades.

📘 **Dónde se aprende** (1 clase): [B12-C18 · Matrices de covarianza](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md).

### Elipse de incertidumbre

- La elipse de incertidumbre es el contorno de probabilidad constante.

🎯 **Por qué importa (clase B58-C08):** La incertidumbre tiende a crecer con el tiempo y se estira a lo largo de la órbita, aunque la geometría con la Tierra la modula. La decisión central: ¿cuánto se estira la región de búsqueda en cada fecha y hasta cuándo sirve la covarianza lineal?

📘 **Dónde se aprende** (1 clase): [B58-C08 · Propagación de incertidumbre orbital](../programa/clases/B58/B58-C08-propagacion-de-incertidumbre-orbital/CLASE.md).

### Elipse de transferencia de Hohmann

- La elipse de transferencia de Hohmann es la mitad de una elipse tangente a las dos órbitas circulares.

🎯 **Por qué importa (clase B75-C01):** Para ir a Marte no se apunta a donde está Marte: se elige una elipse alrededor del Sol que toque la órbita de la Tierra al salir y la de Marte al llegar. La decisión central: ¿cuál es la elipse de menor energía que une dos órbitas circulares, cuánto dura el viaje y qué velocidad exige a la salida y a la llegada?

📘 **Dónde se aprende** (1 clase): [B75-C01 · Geometría de transferencias heliocéntricas](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md).

### Elipsoide

- Un elipsoide es una figura matemática de la Tierra con semieje mayor `a` y aplanamiento `f`.

💡 **Cómo se explica en la clase [B13-C11](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md):**
- La latitud geocéntrica es el ángulo entre el plano ecuatorial y la línea al centro; difiere de la geodésica porque la normal al elipsoide no pasa por el centro.
- Un punto se puede nombrar de dos modos equivalentes: por dónde está sobre el elipsoide y a qué altura (φ, λ, h) o por tres distancias a lo largo de ejes fijados a la Tierra (X, Y, Z).
- ⚠️ **Error frecuente:** No declarar el elipsoide o el marco. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Una estación terrestre transmite a un satélite; el software de seguimiento necesita su posición en X, Y, Z. El técnico de campo tiene su posición en latitud, longitud y altura.

📘 **Dónde se aprende** (1 clase): [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### Elipsoide de dispersión

- La elipsoide de dispersión tiene semiejes dados por los valores singulares de `Φ` por `σ`.

💡 **Cómo se explica en la clase [B75-C18](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md):**
- Interpretar los ejes principales de la elipsoide de dispersión.
- 🎯 **Por qué importa:** Para decidir cuántas correcciones de trayectoria hacen falta hay que saber cuánto se dispersa la llegada. La decisión central: ¿qué dispersión de posición produce un error de velocidad dado en la salida y cuán buena es la aproximación lineal?

📘 **Dónde se aprende** (1 clase): [B75-C18 · Propagación de dispersión inicial](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md).

### Elipsoide de error

- Los autovalores son las varianzas en los ejes principales del elipsoide de error.

💡 **Cómo se explica en la clase [B74-C11](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md):**
- Porque el error de velocidad se convierte en desplazamiento a lo largo de un arco; el elipsoide lineal lo aproxima mal.
- 🎯 **Por qué importa:** Los números de la diagonal engañan: dos errores muy correlacionados pueden ser individualmente grandes y conjuntamente pequeños. La decisión central: ¿qué dicen realmente los autovalores, las correlaciones y el elipsoide, y qué probabilidad encierra cada «k sigma» en tres dimensiones?

📘 **Dónde se aprende** (1 clase): [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Elipsoide de referencia

- El elipsoide de referencia es una figura de revolución elegida por convención.

🎯 **Por qué importa (clase B53-C04):** Una altura solo tiene sentido respecto de una superficie de referencia. La decisión central: ¿contra qué superficie se mide la altura y cuánto se aparta el geoide de ella?

📘 **Dónde se aprende** (1 clase): [B53-C04 · Geoides y elipsoides](../programa/clases/B53/B53-C04-geoides-y-elipsoides/CLASE.md).

### Elipsoide de revolución achatado

- Un elipsoide de revolución achatado de radio ecuatorial `a` y polar `c < a` tiene volumen `(4/3)πa²c`.

🎯 **Por qué importa (clase B03-C17):** La NASA publica que la densidad media del Sol es 1408 kg/m³ (S1), cerca de una vez y media la del agua. ¿Cómo se obtiene?

📘 **Dónde se aprende** (1 clase): [B03-C17 · Áreas y volúmenes elementales](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md).

### Elipsoide de velocidades

- El elipsoide de velocidades son las dispersiones `(σ_U, σ_V, σ_W)`.

🎯 **Por qué importa (clase B38-C03):** El error de distancia se propaga a todas las velocidades tangenciales. La decisión central: ¿cuánto error de paralaje tolera la medida de una dispersión de velocidades?

📘 **Dónde se aprende** (1 clase): [B38-C03 · Cinemática estelar con Gaia: movimientos propios y espacio de fase](../programa/clases/B38/B38-C03-cinematica-estelar-con-gaia-movimientos-propios-y-espacio-de-fase/CLASE.md).

### Elipsoide lineal

- El elipsoide lineal deja de contener la distribución cuando la nube se curva.

💡 **Cómo se explica en la clase [B74-C12](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md):**
- Tras un periodo la desviación a lo largo de la trayectoria es `2691,9`, `2699,2` y `2691,9 m` con STM, Monte Carlo y puntos sigma; la fracción dentro del elipsoide lineal del 95 % es `0,950`.
- A 10 periodos solo `0,863` de las muestras queda dentro del elipsoide lineal del 95 %; a 50 periodos, `0,264`.
- 🎯 **Por qué importa:** Una predicción de dónde estará un satélite dentro de semanas necesita su incertidumbre, y esa incertidumbre se vuelve curva. La decisión central: ¿cuándo basta la covarianza lineal y cuándo hay que propagar la distribución completa?

📘 **Dónde se aprende** (1 clase): [B74-C12 · Propagación de incertidumbre — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Elíptica

- Una galaxia espiral tiene un disco con brazos, gas y formación estelar; una elíptica es un sistema de estrellas viejas sin disco notable; una lenticular tiene disco pero sin brazos (S1).
- Los tipos espiral, elíptica e irregular describen su forma (S1).
- Para `A u_xx + B u_xy + C u_yy + (términos de orden menor) = 0`, el signo de `B² − 4AC` la clasifica: parabólica (`= 0`; ejemplo: calor `u_t = α u_xx`), hiperbólica (`> 0`; ejemplo: onda `u_tt = c² u_xx`) o elíptica (`< 0`; ejemplo: Laplace `u_xx + u_yy = 0`).

💡 **Cómo se explica en la clase [B01-C15](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md):**
- NASA agrupa las galaxias en espirales, elípticas e irregulares (S1).
- Por forma (espiral, elíptica): visual, pero superficial.
- 🎯 **Por qué importa:** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?

📘 **Dónde se aprende** (3 clases): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md); [B11-C13 · Ecuaciones en derivadas parciales](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md); [B25-C09 · Galaxias elípticas y espirales](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md).

### Elíptico

- Un problema elíptico es el que no tiene tiempo y acopla todo el dominio.

🎯 **Por qué importa (clase B21-C03):** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Elongación

- La elongación de un planeta es el ángulo Sol–Tierra–planeta.
- La elongación `ψ` es la separación angular entre la Luna y el Sol en el cielo.
- La elongación es el ángulo en el cielo entre un planeta y el Sol; es este si el planeta sale después que el Sol y se ve en el cielo vespertino, y oeste si sale antes y se ve en el cielo matutino.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- La elongación observada varía algo con la excentricidad; el valor de la clase es el del modelo circular.
- Descripción larga: la distancia crece de forma suave y no lineal con `φ`, más deprisa cerca de la oposición y más despacio cerca de la conjunción; la elongación de Marte baja de 180° a 0°.
- ⚠️ **Error frecuente:** Confundir la elongación con el ángulo heliocéntrico. Se corrige con el ejercicio 3 y la sección 6.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

📘 **Dónde se aprende** (5 clases): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md); [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md); [B08-C10 · Planetas observables y elongación](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md); [B42-C17 · Estrellas guía artificiales](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md); [B128-C03 · Alternativas a la observación visual](../programa/clases/B128/B128-C03-alternativas-a-la-observacion-visual/CLASE.md).

### Elongación máxima

- La elongación máxima es la mayor separación angular que un planeta interior alcanza.

💡 **Cómo se explica en la clase [B08-C10](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md):**
- Son valores de un modelo circular: la órbita real de Mercurio es notablemente excéntrica y su elongación máxima real varía respecto de 22,8° (cifra real no consultada).
- ¿Está cerca de su elongación máxima? <details><summary>Respuesta</summary>No: 15,3° es un tercio de 46,3°.
- 🎯 **Por qué importa:** Los planetas parecen «estrellas errantes» y un titular promete «alineación de planetas». La pregunta motivadora: ¿qué planetas puedo ver esta noche, dónde y a qué hora?

📘 **Dónde se aprende** (1 clase): [B08-C10 · Planetas observables y elongación](../programa/clases/B08/B08-C10-planetas-observables-y-elongacion/CLASE.md).

### Embudo

- El embudo es la secuencia de etapas con tasas de paso.

💡 **Cómo se explica en la clase [B124-C18](../programa/clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md):**
- Paso 1 · Embudo. 10 000 impresiones, clic 2 %, lectura 50 %: `10 000 · 0,02 · 0,5 = 100` lecturas.
- Descripción larga: el embudo pierde casi todo el alcance antes de convertir en seguidores y la prueba solo es confiable con una muestra suficiente.
- 🎯 **Por qué importa:** Sin medir, la divulgación se evalúa por impresión. La decisión central: ¿cuántas personas hay que observar para saber si un mensaje funciona mejor que otro, y cuánto alcance real tiene una campaña?

📘 **Dónde se aprende** (1 clase): [B124-C18 · Comunicación y divulgación](../programa/clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md).

### EMC

- EMC: capacidad de un equipo de funcionar en su entorno sin perturbarlo ni ser perturbado.

💡 **Cómo se explica en la clase [B90-C13](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md):**
- No: el límite es sintético; el vigente sale de los requisitos de EMC del proyecto.
- python programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/margenes_emc.py
- 🎯 **Por qué importa:** Un convertidor de potencia emite armónicos que viajan por el arnés y pueden perturbar a otro equipo. El margen de 2 dB que pasa hoy puede ser negativo mañana si cambia la incertidumbre.

📘 **Dónde se aprende** (1 clase): [B90-C13 · Compatibilidad electromagnética EMC](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md).

### Emergencia

- Emergencia: situación que exige acción inmediata.

💡 **Cómo se explica en la clase [B96-C15](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md):**
- En una emergencia real la regla es primero ganar tiempo (apagar lo no esencial) y después diagnosticar.
- La evidencia es la árbol de decisión de emergencia con tiempos del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Cuando falta el contacto, esperar tiene un costo medible. La decisión central: ¿alcanza el tiempo de respuesta antes del límite crítico y qué se puede hacer para ganar margen?

📘 **Dónde se aprende** (1 clase): [B96-C15 · Operaciones de emergencia](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md).

### EMI

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B90-C14](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Qué medidas reducen la EMI sin cambiar la distancia?
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué la prueba de EMI se hace con el sistema integrado?
- 🎯 **Por qué importa:** Un transmisor de 1 W deja un armónico de −30 dBm; el piso de ruido de un receptor estrecho está cerca de −132 dBm. La diferencia de más de 100 dB se pierde con facilidad en un chasis de 10 cm.

📘 **Dónde se aprende** (1 clase): [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md).

### Emisión

- Un espectro continuo tiene luz en todas las longitudes de onda; uno de emisión muestra líneas brillantes sobre fondo oscuro; uno de absorción muestra líneas oscuras sobre un fondo continuo.
- Un espectro continuo tiene todos los colores; uno de absorción tiene líneas oscuras donde un gas absorbe; uno de emisión tiene líneas brillantes donde un gas emite.

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- Distinguir espectro continuo, de emisión y de absorción.
- Ejercicio 7. Distingue emisión de absorción: un espectro muestra un fondo brillante con tres líneas oscuras.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📘 **Dónde se aprende** (2 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md).

### Emisión conducida

- EMC: capacidad de un equipo de funcionar en su entorno sin perturbarlo ni ser perturbado. Emisión conducida: perturbación que viaja por los cables.

💡 **Cómo se explica en la clase [B90-C13](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué diferencia hay entre emisión conducida y radiada?
- Límites: solo emisiones conducidas; detector y ancho de banda no modelados; una línea; una incertidumbre constante.
- 🎯 **Por qué importa:** Un convertidor de potencia emite armónicos que viajan por el arnés y pueden perturbar a otro equipo. El margen de 2 dB que pasa hoy puede ser negativo mañana si cambia la incertidumbre.

📘 **Dónde se aprende** (1 clase): [B90-C13 · Compatibilidad electromagnética EMC](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md).

### Emisión fundamental

- La emisión fundamental está en `f_p`, el armónico en `2f_p`.

🎯 **Por qué importa (clase B30-C21):** Una frecuencia es una altura, y la deriva en frecuencia da la velocidad del haz. La decisión central: ¿cómo se convierte un espectro dinámico en la velocidad de los electrones?

📘 **Dónde se aprende** (1 clase): [B30-C21 · Radioemisión solar: estallidos de radio y su observación](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md).

### Emisión térmica

- La emisión térmica es la propia del planeta.

💡 **Cómo se explica en la clase [B29-C06](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md):**
- Descripción larga: la emisión térmica en el infrarrojo medio es mucho más favorable que la luz reflejada para planetas terrestres.
- Porque su emisión térmica es mucho mayor: el contraste es unas 500 veces mejor que en luz reflejada para la Tierra (8.5).
- 🎯 **Por qué importa:** La imagen directa entrega espectros del planeta y la órbita completa, pero solo es posible con planetas jóvenes, calientes y lejanos de la estrella. La decisión central: ¿qué contraste y qué separación angular hay que alcanzar para ver un planeta dado?

📘 **Dónde se aprende** (1 clase): [B29-C06 · Imagen directa de exoplanetas](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md).

### Emisividad

- La emisividad `ε` es la razón entre lo que emite un cuerpo y lo que emitiría un cuerpo negro.
- La emisividad es la fracción de lo que emitiría un cuerpo negro.
- La emisividad `ε` es el cociente con el cuerpo negro.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C17](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md):**
- Su límite: un cuerpo negro real tiene emisividad algo menor que 1 y un campo no uniforme; ambos son una fuente de incertidumbre (C13).
- Paso 4 · Efecto de la emisividad. Si el cuerpo negro real tiene `ε = 0,95` y se supone 1, las radiancias reales son `5 %` menores que las asumidas: la ganancia estimada sale `5 %` mayor (`≈ 0,84`).
- 🎯 **Por qué importa:** Una cámara infrarroja de una nave mide el calor emitido por la superficie de un planeta. Sus cuentas no significan nada hasta saberse cuánta radiancia corresponde a cada una.

📘 **Dónde se aprende** (7 clases): [B13-C17 · Calibración radiométrica](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md); [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md); [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md); [B47-C23 · Sondas heliosféricas: Parker Solar Probe y Voyager](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md); [B57-C01 · Fundamentos de teledetección](../programa/clases/B57/B57-C01-fundamentos-de-teledeteccion/CLASE.md); [B85-C04 · Radiación térmica de superficies](../programa/clases/B85/B85-C04-radiacion-termica-de-superficies/CLASE.md) y 1 más.

### Emisividad efectiva

- La emisividad efectiva `ε_eff = q/(σ(T_h⁴ − T_c⁴))` es la de una sola superficie que daría el mismo flujo.
- La emisividad efectiva `ε` resume el efecto del invernadero.

💡 **Cómo se explica en la clase [B85-C06](../programa/clases/B85/B85-C06-aislamiento-multicapa/CLASE.md):**
- Calcular el flujo radiativo a través de N pantallas y la emisividad efectiva.
- 🎯 **Por qué importa:** Aislar una caja que opera a `300 K` de un entorno a `100 K` con una sola superficie cuesta cientos de W/m²; con unas pocas capas cuesta unidades. La decisión central: ¿cuántas capas y de qué emisividad hacen falta para limitar el flujo, y cuánto se pierde si se comprimen?

📘 **Dónde se aprende** (2 clases): [B54-C19 · Modelos climáticos planetarios](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md); [B85-C06 · Aislamiento multicapa](../programa/clases/B85/B85-C06-aislamiento-multicapa/CLASE.md).

### Emisor estático

- El emisor estático está en reposo respecto de la masa.

💡 **Cómo se explica en la clase [B26-C10](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md):**
- Para un emisor estático en `R` y un receptor lejano, `1 + z = 1/√(1 − r_s/R)`, con `r_s = 2GM/c²`.
- Límites: emisor estático, sin rotación ni movimiento orbital en el efecto del reloj.
- 🎯 **Por qué importa:** El corrimiento gravitacional ajusta los relojes de los satélites de navegación, contamina la medida de velocidades en enanas blancas y revela la compacidad de las estrellas de neutrones. La decisión central: dada la compacidad de un cuerpo, ¿cuánto vale el corrimiento de su luz y cuándo falla la aproximación de campo débil?

📘 **Dónde se aprende** (1 clase): [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md).

### Empaquetado

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B51-C12](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de los formatos de datos*: eficiencia, Van Vleck, empaquetado, tasa y límites.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de los formatos de datos*: eficiencia, Van Vleck, empaquetado, tasa y límites.
- 🎯 **Por qué importa:** La elección de bits y de formato fija cuánta sensibilidad se pierde y cuánto disco y red se necesitan. La decisión central: ¿cuántos bits por muestra, qué eficiencia se obtiene y cómo se empaqueta sin perder información?

📘 **Dónde se aprende** (1 clase): [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md).

### Empaquetado en bolsas

- El empaquetado en bolsas minimiza el número de contenedores.

💡 **Cómo se explica en la clase [B104-C21](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md):**
- La cota inferior es `⌈1,063/0,05⌉ = 22` bolsas; el empaquetado de primero el mayor que cabe usa 22 (96,6 % de llenado), dentro de la garantía de `11/9 · óptimo + 1`.
- El script [inventario.py](inventario.py) simula 4 000 años de inventario para tres puntos de reorden y empaqueta 60 objetos en bolsas (comprueba que más reserva reduzca los faltantes, que el empaquetado respete su garantía y que ninguna bolsa supere su volumen).
- 🎯 **Por qué importa:** Quedarse sin un consumible a bordo no se arregla enviando a alguien a comprarlo. La decisión central: ¿con qué punto de reorden se pide para que el faltante sea raro, y cuánto volumen cuesta guardar lo pedido?

📘 **Dónde se aprende** (1 clase): [B104-C21 · Inventario, logística y estiba a bordo](../programa/clases/B104/B104-C21-inventario-logistica-y-estiba-a-bordo/CLASE.md).

### Emplazamiento

- Un emplazamiento es el lugar elegido para construir.

💡 **Cómo se explica en la clase [B109-C01](../programa/clases/B109/B109-C01-seleccion-de-emplazamiento-para-un-asentamiento-extraterrestre/CLASE.md):**
- python programa/clases/B109/B109-C01-seleccion-de-emplazamiento-para-un-asentamiento-extraterrestre/sitios.py
- 🎯 **Por qué importa:** Un asentamiento no se puede mover una vez construido. La decisión central: ¿cómo comparar sitios con criterios distintos sin esconder los juicios de valor en un número?

📘 **Dónde se aprende** (1 clase): [B109-C01 · Selección de emplazamiento para un asentamiento extraterrestre](../programa/clases/B109/B109-C01-seleccion-de-emplazamiento-para-un-asentamiento-extraterrestre/CLASE.md).

### Empuje

- El empuje es la fuerza de un motor o un fluido.
- El empuje es `E = ṁ v_e`, con `ṁ` el flujo de masa expulsada.
- El empuje `F` es la fuerza que el motor ejerce sobre la nave.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- Un cohete de masa `m` en una plataforma, con empuje vertical `E` y peso `m g_n`, tiene `a = (E − m g_n)/m`.
- En el espacio, el satélite ideal bajo gravedad y un empuje tangencial pequeño tiene `ΣF` con dos componentes: una radial (gravedad) y otra tangencial (empuje).
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?

📘 **Dónde se aprende** (7 clases): [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md); [B05-C08 · Momento lineal e impulsos](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md); [B78-C01 · Empuje e impulso específico](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md); [B79-C08 · Flujo en toberas convergente-divergentes](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md); [B81-C05 · Limitaciones de potencia en propulsión eléctrica](../programa/clases/B81/B81-C05-limitaciones-de-potencia-en-propulsion-electrica/CLASE.md); [B97-C06 · Control de movilidad sobre regolito](../programa/clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md) y 1 más.

### Empuje finito

- El empuje finito es una fuerza constante durante un tiempo.

💡 **Cómo se explica en la clase [B75-C10](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md):**
- *Descripción textual:* Se integra el movimiento con empuje prógrado hasta alcanzar la energía de escape objetivo; el delta-v finito se obtiene de la masa gastada y se compara con el impulsivo.
- Distinguir impulso instantáneo y empuje finito.
- 🎯 **Por qué importa:** El modelo impulsivo es útil, pero ¿cuándo es un buen modelo? La decisión central: ¿cuánto delta-v se pierde por quemar durante un tiempo finito y de qué depende, en particular del cociente empuje/peso?

📘 **Dónde se aprende** (1 clase): [B75-C10 · Maniobras impulsivas](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md).

### Empuje por potencia

- El empuje por potencia `F/P` se mide en mN/kW.

💡 **Cómo se explica en la clase [B78-C06](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md):**
- *Descripción textual:* la potencia de entrada, por la eficiencia, da la potencia del chorro; con la velocidad de escape fija el empuje; el empuje por potencia cae como `1/Vₑ` y fija el tiempo de maniobra.
- Paso 3 · Empuje por potencia. `0,091/2123 = 4,29×10⁻⁵ N/W = 42,9 mN/kW`.
- 🎯 **Por qué importa:** Subir el `Isp` ahorra propelente, pero el mismo vatio produce menos empuje y la maniobra tarda más. La decisión central: ¿cuánto empuje da cada kilovatio, cómo cae con el `Isp` y qué pasa con el tiempo de maniobra?

📘 **Dónde se aprende** (1 clase): [B78-C06 · Propulsión eléctrica general](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md).

### Empuje por potencia térmica

- El empuje por potencia térmica es `F = 2ηP/Vₑ`.

💡 **Cómo se explica en la clase [B78-C14](../programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md):**
- *Descripción textual:* la temperatura y la masa molar dan el escape y el `Isp`, que se contrasta con las cifras consultadas; con la potencia térmica se obtiene el empuje; el escape fija la fracción de propelente para un Δv.
- Calcular el empuje para una potencia térmica dada.
- 🎯 **Por qué importa:** Un cohete químico limita su `Isp` por la química del propelente; uno térmico lo limita por la temperatura que aguanta el núcleo. La decisión central: ¿cuánto `Isp` puede dar un gas de baja masa molar calentado a una temperatura dada y qué empuje corresponde a una potencia térmica?

📘 **Dónde se aprende** (1 clase): [B78-C14 · Propulsión nuclear térmica conceptual](../programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md).

### Empuje-tirón

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C23](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md):**
- Calibrar por empuje-tirón y medir el error.
- pendiente log-log error vs amplitud = -0.885 (esperada -1: el error del empuje-tiron escala como sigma / a)
- 🎯 **Por qué importa:** Una matriz mal calibrada degrada el lazo y las aberraciones del camino de ciencia no las ve el sensor. La decisión central: ¿con qué amplitud calibrar y cómo corregir lo que el sensor no ve?

📘 **Dónde se aprende** (1 clase): [B42-C23 · Calibración de la matriz de interacción y aberraciones no comunes](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md).

### En aire

- La longitud de onda en vacío y en aire difieren porque el aire tiene índice de refracción mayor que 1.

💡 **Cómo se explica en la clase [B02-C16](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md):**
- Las tablas del NIST para las líneas del hidrógeno dan longitudes de onda en aire (S4).
- El aire hace que la longitud de onda sea unos 0,03 % menor que en vacío (656,4696 → 656,288 nm para Hα).
- ⚠️ **Error frecuente:** Mezclar aire y vacío. Ejercicios 4 y 10.
- 🎯 **Por qué importa:** Hasta 1859 se pensaba, con razones, que nunca sabríamos de qué están hechas las estrellas: estaban demasiado lejos para tocarlas. La pregunta motivadora es: ¿cómo se puede conocer la composición de un objeto que solo se ve como luz?

📘 **Dónde se aprende** (1 clase): [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md).

### En masa

- La abundancia es cuánto hay de un elemento; puede darse en número (átomos), en masa (kg) o con la escala logarítmica astronómica: ```text A(X) = log10(N_X / N_H) + 12 ``` donde `N_X` y `N_H` son números de átomos por unidad de volumen.

💡 **Cómo se explica en la clase [B06-C02](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md):**
- La fracción en masa necesita además el peso atómico `M_X` (g/mol): `m_X ∝ N_X M_X`.
- Una consecuencia: en número, el hidrógeno es el 92 % de los átomos y el helio el 7,8 %; en masa, 73,7 % y 24,9 %.
- ⚠️ **Error frecuente:** Confundir número con masa. Se corrige con la sección 14 y los ejercicios 7 y 10.
- 🎯 **Por qué importa:** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?

📘 **Dónde se aprende** (1 clase): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md).

### En número

- La abundancia es cuánto hay de un elemento; puede darse en número (átomos), en masa (kg) o con la escala logarítmica astronómica: ```text A(X) = log10(N_X / N_H) + 12 ``` donde `N_X` y `N_H` son números de átomos por unidad de volumen.

💡 **Cómo se explica en la clase [B06-C02](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md):**
- Lo que identifica a un elemento es `Z`, el número de protones.
- Para pasar a número: `N_X/N_H = 10^(A − 12)`.
- ⚠️ **Error frecuente:** Confundir número con masa. Se corrige con la sección 14 y los ejercicios 7 y 10.
- 🎯 **Por qué importa:** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?

📘 **Dónde se aprende** (1 clase): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md).

### En paralelo

- Dos resistencias están en serie si las atraviesa la misma corriente y en paralelo si soportan la misma tensión.

💡 **Cómo se explica en la clase [B05-C16](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md):**
- En paralelo: `1/R_eq = 1/R₁ + 1/R₂` (misma tensión).
- Con `6 Ω` y `12 Ω` en paralelo, `R_eq = 4 Ω`, menor que la menor de ambas.
- ⚠️ **Error frecuente:** Confundir serie y paralelo. Ejercicio 2.
- 🎯 **Por qué importa:** Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: ¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?

📘 **Dónde se aprende** (1 clase): [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md).

### En serie

- Dos resistencias están en serie si las atraviesa la misma corriente y en paralelo si soportan la misma tensión.

💡 **Cómo se explica en la clase [B05-C16](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md):**
- En serie: `R_eq = R₁ + R₂` (misma corriente).
- En un divisor de tensión (4 Ω y 8 Ω en serie con 12 V), la tensión sobre los 8 Ω es `8 V`.
- ⚠️ **Error frecuente:** Confundir serie y paralelo. Ejercicio 2.
- 🎯 **Por qué importa:** Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: ¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?

📘 **Dónde se aprende** (1 clase): [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md).

### En vacío

- La longitud de onda en vacío y en aire difieren porque el aire tiene índice de refracción mayor que 1.

💡 **Cómo se explica en la clase [B02-C16](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md):**
- El aire hace que la longitud de onda sea unos 0,03 % menor que en vacío (656,4696 → 656,288 nm para Hα).
- Mezclar vacío con aire introduce un error de 0,18 nm en Hα, mayor que la precisión de un instrumento espectral moderno (B01-C04, ejemplo trabajado).
- ⚠️ **Error frecuente:** Mezclar aire y vacío. Ejercicios 4 y 10.
- 🎯 **Por qué importa:** Hasta 1859 se pensaba, con razones, que nunca sabríamos de qué están hechas las estrellas: estaban demasiado lejos para tocarlas. La pregunta motivadora es: ¿cómo se puede conocer la composición de un objeto que solo se ve como luz?

📘 **Dónde se aprende** (1 clase): [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md).

### Enana blanca

- Una enana blanca es un remanente caliente y poco luminoso, de radio pequeño.
- Una enana blanca es el remanente de una estrella de baja o media masa, sostenido por la presión de electrones degenerados.
- Una enana blanca es un remanente compacto (B24-C18).
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C03](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md):**
- Con el cálculo del laboratorio: una enana roja (`L = 0,01 L☉`, `3200 K`) tiene `R = 0,33 R☉`; una estrella como el Sol, `1 R☉`; una gigante roja (`L = 100 L☉`, `4500 K`), `16,5 R☉`; una enana blanca (`L = 0,003 L☉`, `12 000 K`), `0,013 R☉`, del orden del tamaño de un planeta.
- Las gigantes quedan arriba a la derecha (grandes y frías), las enanas blancas abajo a la izquierda (pequeñas y calientes) y la secuencia principal en la diagonal.
- 🎯 **Por qué importa:** Casi todas las propiedades de una estrella (tamaño, masa, edad, fase) se resumen en dos medidas: cuánta energía emite y a qué temperatura. El diagrama HR convierte esas dos medidas en un mapa donde cada región corresponde a un estado físico.

📖 **Explicado a fondo:** [Enana blanca](esencial/esencial-d-l.md#enana-blanca) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B24-C03 · Diagrama de Hertzsprung-Russell](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md); [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md); [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md); [B27-C02 · Enanas blancas y límite de Chandrasekhar](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md).

### Enana blanca de C/O

- Una enana blanca de C/O tiene `μ_e = 2`.

💡 **Cómo se explica en la clase [B27-C02](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md):**
- Una enana blanca que gana masa de una compañera puede aproximarse al límite (B27-C14).
- El púlsar PSR J0348+0432 (de `2,01 ± 0,04 M☉`) tiene una compañera enana blanca de `0,172 ± 0,003 M☉` en una órbita de `2,46 h` (S4, resumen).
- 🎯 **Por qué importa:** Las enanas blancas son el destino de la mayoría de las estrellas, sirven de relojes cosmológicos y, al acercarse a su masa límite, pueden explotar. Una relación masa–radio correcta separa masas y radios que la fotometría sola confunde.

📘 **Dónde se aprende** (1 clase): [B27-C02 · Enanas blancas y límite de Chandrasekhar](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md).

### Enana roja

- Una enana roja es una estrella de secuencia principal de baja masa y baja luminosidad.

💡 **Cómo se explica en la clase [B24-C15](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md):**
- Con ello, las enanas rojas de menos de `0,2 M☉` no han salido nunca de la secuencia principal.
- Ejercicio 10 · transferencia. Un compañero dice que «las enanas rojas ya se están apagando».
- 🎯 **Por qué importa:** La masa decide casi todo en la vida de una estrella: cuánto brilla, cuánto dura y cómo termina. Entender por qué una estrella de la mitad de la masa del Sol vive varias veces más tiempo, y por qué las más pequeñas casi no han evolucionado, explica la composición de las poblaciones estelares y la edad de los cúmulos.

📘 **Dónde se aprende** (1 clase): [B24-C15 · Estrellas de baja masa](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md).

### Enanas esferoidales

- Una galaxia enana es una galaxia de baja masa y luminosidad; las enanas esferoidales (dSph) son pobres en gas y se sostienen por agitación; las ultratenues son las menos luminosas.

💡 **Cómo se explica en la clase [B25-C10](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md):**
- Definir galaxia irregular, enana esferoidal, enana ultratenue y radio de media luz.
- 🎯 **Por qué importa:** Las galaxias enanas son las más abundantes y las más ricas en materia oscura según su masa dinámica; además son los sitios donde las predicciones del modelo cosmológico se ponen a prueba. Pero con pocas estrellas medidas y sin rotación ordenada, su masa depende de un estimador.

📘 **Dónde se aprende** (1 clase): [B25-C10 · Galaxias irregulares y enanas](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md).

### ENBW

- El ENBW es el ancho de un filtro rectangular con el mismo ruido.

💡 **Cómo se explica en la clase [B46-C10](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md):**
- Con `fs = 2,4 MHz` y `N = 1024` la resolución es `2343,75 Hz`; el ENBW de Hann vale `1,5000` bines; la dispersión relativa de un canal pasa de `0,963` con `M = 1` a `0,128` con `M = 64`.
- Ejercicio 4. ENBW en Hz de Hann con `Δf = 2343,75 Hz`.
- ⚠️ **Error frecuente:** Olvidar el ENBW. Se corrige con 8.1.
- 🎯 **Por qué importa:** Promediar espectros es la forma práctica de aplicar la ecuación del radiómetro con un instrumento barato, pero la ventana cambia el ancho de banda efectivo. La decisión central: ¿cuántos espectros promediar para detectar una línea débil?

📘 **Dónde se aprende** (1 clase): [B46-C10 · Radioastronomía mediante SDR](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md).

### Encabezado

- Un encabezado es una lista de tarjetas (registros de 80 caracteres) con una palabra clave, un valor y un comentario.
- La primera línea suele ser el encabezado.
- Un encabezado (`h1`–`h6`) marca la estructura.

💡 **Cómo se explica en la clase [B07-C08](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md):**
- Paso 5. Compara el encabezado con el esperado.
- Validar encabezado, número de filas y rangos.
- 🎯 **Por qué importa:** Un archivo CSV parece trivial y por eso engaña: todo se lee como texto, un decimal con coma rompe una columna, una línea vacía pasa inadvertida, y una codificación equivocada convierte «Júpiter» en símbolos raros. Un análisis hecho sobre datos mal leídos puede ser plausible y erróneo a la vez.

📘 **Dónde se aprende** (3 clases): [B07-C08 · Lectura de archivos CSV](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md); [B14-C06 · Formato FITS y encabezados](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md); [B128-C04 · Documentos y contenidos para lectores de pantalla](../programa/clases/B128/B128-C04-documentos-y-contenidos-para-lectores-de-pantalla/CLASE.md).

### Encadenamiento

- El encadenamiento hace que cada registro incluya el hash del anterior.

🎯 **Por qué importa (clase B63-C03):** Una muestra planetaria es irrepetible y se estudia durante décadas. La decisión central: ¿cómo demuestras, años después, qué le pasó a una muestra y cuánto de lo que mides es suyo?

📘 **Dónde se aprende** (1 clase): [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md).

### Encendido tardío

- El encendido tardío (suicide burn) enciende el motor lo más tarde posible: `h = v²/(2(a − g))`.

🎯 **Por qué importa (clase B77-C18):** Un paracaídas grande da un aterrizaje suave pero una apertura brusca; un motor da control pero consume propelente. La decisión central: ¿qué velocidad de contacto, qué carga de apertura y qué altura de encendido resultan de cada opción?

📘 **Dónde se aprende** (1 clase): [B77-C18 · Aterrizaje y recuperación](../programa/clases/B77/B77-C18-aterrizaje-y-recuperacion/CLASE.md).

### Encuentro

- Un encuentro es la situación geométrica completa.

💡 **Cómo se explica en la clase [B118-C05](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md):**
- Descripción larga: la distancia de paso es proporcional al retraso; la velocidad relativa de más de 2 km/s hace que el encuentro dure unos segundos.
- Reconocer que dos órbitas que se cruzan generan encuentros a más de 2 km/s.
- 🎯 **Por qué importa:** La alerta de conjunción es el producto básico del tráfico espacial. Su geometría explica por qué los encuentros son tan rápidos y por qué un pequeño desfase en el tiempo produce un cambio grande en la distancia.

📘 **Dónde se aprende** (1 clase): [B118-C05 · Conjunciones orbitales](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md).

### Encuentro cercano

- Un encuentro cercano es una separación entre planetas menor que `R_H`.

💡 **Cómo se explica en la clase [B73-C17](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md):**
- *Descripción textual:* a partir de `Δ` se obtiene `a₂`, se integra el sistema y se registra el primer encuentro cercano; las simulaciones se contrastan con el criterio `2√3` y con las conservaciones de la integración.
- Con dos planetas sintéticos de `m/M = 3×10⁻⁴` (R_H mutuo = `0,05848 (a₁+a₂)/2`), una separación `Δ = 2` provoca un encuentro cercano en `1,6` a `44,6` órbitas interiores según la fase inicial; con `Δ = 3`, en `41,8` y `348,8` órbitas para dos fases y ninguno en 2000 para la tercera; con `Δ ≥ 3,5` ninguno en 2000 órbitas.
- 🎯 **Por qué importa:** Muchos sistemas exoplanetarios son compactos y su existencia depende de no haberse desestabilizado. Un criterio simple de separación permite descartar configuraciones inviables antes de integrar.

📘 **Dónde se aprende** (1 clase): [B73-C17 · Estabilidad de sistemas exoplanetarios](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md).

### Encuentro rápido

- Un encuentro rápido es aquel en que la geometría se resume en el plano B.

💡 **Cómo se explica en la clase [B58-C09](../programa/clases/B58/B58-C09-probabilidades-de-impacto/CLASE.md):**
- Límites: encuentro rápido, gaussiana exacta, sin correlaciones, sin ojos de cerradura.
- 🎯 **Por qué importa:** La probabilidad de impacto resume la incertidumbre en un número que alimenta las escalas (C10) y las decisiones (C17–C19). La decisión central: ¿qué área de la nube de posibles posiciones cae sobre la Tierra, y cuánto cambia si la nube se achica o se desplaza?

📘 **Dónde se aprende** (1 clase): [B58-C09 · Probabilidades de impacto](../programa/clases/B58/B58-C09-probabilidades-de-impacto/CLASE.md).

### Endogrupo

- El endogrupo es la tendencia a interactuar dentro del propio grupo; su índice compara la fracción observada con `Σ pg²`.

💡 **Cómo se explica en la clase [B111-C02](../programa/clases/B111/B111-C02-gestion-intercultural-en-tripulaciones-multinacionales/CLASE.md):**
- Pero los índices no explican causas: una distancia grande o un endogrupo alto no son «problemas culturales» en sí.
- Calcular el índice de endogrupo frente a la mezcla al azar.
- 🎯 **Por qué importa:** Ninguna clase del programa trataba las diferencias culturales y de idioma en equipos internacionales. La decisión central: ¿cómo se vuelve un riesgo de comunicación cuantificable y cómo se mitiga con procedimientos y no con estereotipos?

📘 **Dónde se aprende** (1 clase): [B111-C02 · Gestión intercultural en tripulaciones multinacionales](../programa/clases/B111/B111-C02-gestion-intercultural-en-tripulaciones-multinacionales/CLASE.md).

### Endurecimiento isótropo

- El endurecimiento isótropo eleva el límite `σ_y + Hα`.

💡 **Cómo se explica en la clase [B84-C25](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md):**
- Límite: el modelo es 1D, sin efecto Bauschinger (endurecimiento isótropo, no cinemático) y sin temperatura.
- Aplicar el algoritmo de retorno 1D con endurecimiento isótropo.
- 🎯 **Por qué importa:** Un modelo lineal da tensiones de 400 MPa en un material que cedió a 275: el resultado correcto es una deformación permanente y una tensión residual que solo el análisis no lineal muestra. La decisión central: ¿qué deformación permanente y tensión residual deja una carga que excede el límite elástico, y cuándo actúa un contacto?

📘 **Dónde se aprende** (1 clase): [B84-C25 · Comportamiento estructural no lineal: plasticidad y contacto](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md).

### Energía

- Un límite de energía es el de una fuente que se agota (batería).
- La capacidad se mide en Ah y la energía en Wh.
- La energía de un tramo es `F d/η`, con `η` la eficiencia.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B29-C15](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md):**
- La energía total de las `6100` llamaradas es `1,443 × 10³⁴ erg`; el `1 %` más energético concentra el `62,4 %`.
- Con índice menor que 2 la energía total está dominada por las llamaradas grandes, aunque son pocas.
- 🎯 **Por qué importa:** La distribución de energías de las llamaradas determina cuánta energía total reciben los planetas cercanos. Estimar su índice con poco sesgo exige usar el estimador correcto.

📘 **Dónde se aprende** (4 clases): [B29-C15 · Eventos eruptivos estelares](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md); [B78-C18 · Energía específica y limitaciones](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md); [B86-C05 · Baterías de ion-litio](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md); [B100-C05 · Transporte de carga sobre superficie planetaria](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md).

### Energía característica

- La energía característica es `C3 = v∞²`, en km²/s².
- La energía característica `C3 = v∞²` (m²/s² o km²/s²).

💡 **Cómo se explica en la clase [B75-C23](../programa/clases/B75/B75-C23-energia-caracteristica-c3-y-exceso-hiperbolico/CLASE.md):**
- python programa/clases/B75/B75-C23-energia-caracteristica-c3-y-exceso-hiperbolico/c3.py
- 🎯 **Por qué importa:** Un lanzador entrega una masa distinta según la energía que se le pida. La decisión central: ¿cuánta energía característica y cuánto delta-v hay que dar desde una órbita baja para alcanzar un destino?

📘 **Dónde se aprende** (2 clases): [B71-C09 · Órbitas parabólicas e hiperbólicas](../programa/clases/B71/B71-C09-orbitas-parabolicas-e-hiperbolicas/CLASE.md); [B75-C23 · Energía característica C3 y exceso hiperbólico](../programa/clases/B75/B75-C23-energia-caracteristica-c3-y-exceso-hiperbolico/CLASE.md).

### Energía ciclotrónica

- La energía ciclotrónica `ħω_c = ħeB/m = 2μ_BB`.

💡 **Cómo se explica en la clase [B27-C06](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md):**
- Para ilustrar la escala se usa un campo ilustrativo de `10¹¹ T` (`10¹⁵ G`): `22,7` veces el campo crítico, con una energía ciclotrónica del electrón de `11,6 MeV` y una energía magnética de `1,7 × 10⁴⁰ J`.
- Descripción larga: la energía ciclotrónica crece en proporción al campo y a `10¹¹ T` supera con creces la energía en reposo del electrón.
- 🎯 **Por qué importa:** Los magnetares producen estallidos y llamaradas gigantes que alimenta su campo, no su rotación. Entender la escala del campo y de su energía explica por qué son una familia aparte y cómo se interpretan sus espectros.

📘 **Dónde se aprende** (1 clase): [B27-C06 · Magnetares y campos extremos](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md).

### Energía cinética

- La energía cinética es `E_c = ½ m v²`.
- La energía cinética es `K = (γ − 1)mc²`.
- La energía cinética `K = φ̇²/2` y la potencial `V`.

💡 **Cómo se explica en la clase [B05-C06](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md):**
- Con `ΣF = m a` y `v² = v₀² + 2 a d` (C03) se obtiene `ΣF d = ½ m v² − ½ m v₀²`; es decir, el trabajo de la fuerza neta es el cambio de energía cinética: `W_neto = ΔE_c`.
- Con `v = √(GM/r)`, la energía cinética es `E_c = GMm/(2r)` y la potencial `E_p = −GMm/r`; la mecánica vale `E = −GMm/(2r) = −E_c`.
- 🎯 **Por qué importa:** Poner 1000 kg en órbita cuesta mucho más que subirlos 400 km. La pregunta motivadora es: ¿cuánta energía hay que entregar para cambiar el estado de un cuerpo, y en qué se convierte?

📘 **Dónde se aprende** (3 clases): [B05-C06 · Trabajo y energía](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md); [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md); [B40-C06 · Campos escalares en cosmología: potenciales y evolución](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md).

### Energía cinética de la explosión

- La energía cinética de la explosión es la que mueve las capas externas.

💡 **Cómo se explica en la clase [B27-C15](../programa/clases/B27/B27-C15-supernovas-de-colapso/CLASE.md):**
- Si la energía cinética de la explosión es `10⁴⁴ J` (ilustrativa), corresponde al `0,390 %` de `ΔE` y el resto, `99,61 %`, se va en neutrinos y otras formas.
- si la energia cinetica de la explosion es 1e44 J, fraccion = 0.390 % ; resto (neutrinos y otros) = 99.61 %
- 🎯 **Por qué importa:** El colapso libera cerca de un décimo de `Mc²`; casi todo sale en neutrinos y solo una milésima en la explosión visible. La decisión central: ¿cuánta energía libera el colapso, a qué fracción corresponde la explosión y cuánto tarda?

📘 **Dónde se aprende** (1 clase): [B27-C15 · Supernovas de colapso](../programa/clases/B27/B27-C15-supernovas-de-colapso/CLASE.md).

### Energía cinética de rotación

- El momento angular es `H = J ω` (N·m·s); la energía cinética de rotación es `T = ½ ω·J ω` (J).

🎯 **Por qué importa (clase B16-C17):** Cuando un satélite se separa del cohete puede salir girando de forma desordenada («volteando»).

📘 **Dónde se aprende** (1 clase): [B16-C17 · Control no lineal](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md).

### Energía crítica

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B31-C13):** La energía y la composición de un rayo cósmico se infieren de la forma de su cascada, y el fondo de microondas limita la energía que llega. La decisión central: ¿qué profundidad y tamaño tiene una cascada y a qué energía aparece un corte?

📘 **Dónde se aprende** (1 clase): [B31-C13 · Rayos cósmicos y cascadas](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md).

### Energía de activación

- La energía de activación `E_a` es la barrera de energía que deben superar las moléculas para reaccionar.
- La energía de activación `Eₐ` es la barrera de la ecuación de Arrhenius.
- La energía de activación `E_a` fija su dependencia exponencial.

💡 **Cómo se explica en la clase [B44-C07](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md):**
- Límite: modelo de juguete con prefactor `T^1,5` y una sola energía de activación.
- Datos: `k_B` de NIST CODATA 2022 (consultada el 2026-11-09); energía de activación, tasas y exposiciones ilustrativas; semilla `20261109`.
- 🎯 **Por qué importa:** La oscuridad añade señal y ruido; saber cómo escala permite elegir temperatura y exposición. La decisión central: ¿cuánto hay que enfriar para que la corriente oscura deje de importar?

📘 **Dónde se aprende** (3 clases): [B06-C14 · Cinética química inicial](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md); [B44-C07 · Corriente oscura](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md); [B64-C03 · Psicrófilos y vida en frío](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md).

### Energía de activación aparente

- La energía de activación aparente `Eₐ` se obtiene de la pendiente de `ln k` frente a `1/T`.

💡 **Cómo se explica en la clase [B64-C02](../programa/clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md):**
- *Descripción textual:* la temperatura entra en un modelo cardinal que da la tasa; de la rama ascendente sale la energía de activación aparente, del máximo la temperatura óptima, y por separado la temperatura fija la presión de saturación que exige el medio.
- Estimar una energía de activación aparente con un ajuste lineal de ln k frente a 1/T.
- 🎯 **Por qué importa:** Un hipertermófilo crece donde casi todo lo demás muere, pero el agua hierve a 100 °C a presión ambiente. La pregunta motivadora: ¿qué fija el límite superior de temperatura de la vida y cómo se mide ese límite?

📘 **Dónde se aprende** (1 clase): [B64-C02 · Termófilos e hipertermófilos](../programa/clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md).

### Energía de cohesión

- La energía de cohesión `ε` es la que cuesta separar una partícula de sus vecinas; para un líquido que se evapora, es la entalpía de vaporización dividida entre `N_A`.

💡 **Cómo se explica en la clase [B06-C10](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md):**
- La «fuerza» con que se agarran es la energía de cohesión; el ritmo de la música, `kT`.
- *Descripción textual:* cuatro cajas ordenadas por el cociente de la energía de cohesión entre la térmica.
- 🎯 **Por qué importa:** En Marte, la temperatura media es 214 K y la presión media en superficie 6,36 mb (S1). Ese valor está casi en el punto triple del agua, la presión mínima a la que puede existir agua líquida (S2).

📘 **Dónde se aprende** (1 clase): [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md).

### Energía de cruce

- La energía de cruce es la que iguala las masas del sistema de pila y de la batería.

💡 **Cómo se explica en la clase [B86-C15](../programa/clases/B86/B86-C15-sistemas-de-combustible-como-alternativa/CLASE.md):**
- *Descripción textual:* la termodinámica da las tensiones y la eficiencia; la energía y la tensión dan los reactivos; con la pila forman la masa del sistema, que se compara con la de la batería para hallar la energía de cruce.
- Descripción larga: la masa de la batería crece en proporción a la energía mientras la de la pila crece más despacio sobre una base fija; se cruzan en la energía de cruce.
- 🎯 **Por qué importa:** Una batería guarda la energía y la entrega en la misma masa; una pila separa la potencia (la pila) de la energía (los reactivos). Para misiones largas esa separación puede ser más liviana, pero añade tanques, gestión del agua y complejidad.

📘 **Dónde se aprende** (1 clase): [B86-C15 · Sistemas de combustible como alternativa](../programa/clases/B86/B86-C15-sistemas-de-combustible-como-alternativa/CLASE.md).

### Energía de enlace

- La energía de enlace `B` es la energía que habría que aportar para separar el núcleo en nucleones libres;
- La energía de enlace `E` (en K) es la energía que ata la molécula a la superficie dividida por `k_B`.

💡 **Cómo se explica en la clase [B55-C02](../programa/clases/B55/B55-C02-nucleosintesis-y-elementos/CLASE.md):**
- Un núcleo pesa menos que sus piezas sueltas; esa diferencia, multiplicada por `c²`, es la energía de enlace.
- *Descripción textual:* las masas atómicas dan el defecto de masa y la energía de enlace por nucleón, con un máximo en la región del hierro y el níquel; las diferencias de masa entre reactivos y productos dan los valores `Q`.
- 🎯 **Por qué importa:** Los elementos que encontramos en el espacio, en cometas y en meteoritos se formaron en estrellas. Para saber hasta dónde puede llegar una cadena de fusión y cuánta energía libera hay que mirar la energía de enlace.

📘 **Dónde se aprende** (2 clases): [B55-C02 · Nucleosíntesis y elementos](../programa/clases/B55/B55-C02-nucleosintesis-y-elementos/CLASE.md); [B68-C01 · Desorción térmica de hielos interestelares](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md).

### Energía de escape

- La energía de escape es el trabajo para llegar a `r → ∞`.

💡 **Cómo se explica en la clase [B09-C12](../programa/clases/B09/B09-C12-teorema-fundamental-del-calculo/CLASE.md):**
- Llevar 1 kg de `R` a `2R` cuesta `GM/(2R) = 3,125 × 10⁷ J/kg`, la mitad de la energía de escape; a `10R`, el 90 %; a `100R`, el 99 %; a `1000R`, el 99,9 %.
- El ejemplo conductor es esta energía de escape, que toda misión interplanetaria debe suministrar o sobrepasar.
- 🎯 **Por qué importa:** Para que una sonda abandone la Tierra hay que darle energía suficiente para vencer la gravedad hasta una distancia infinita. Esa energía es una integral de la fuerza sobre una distancia sin cota superior.

📘 **Dónde se aprende** (1 clase): [B09-C12 · Teorema fundamental del cálculo](../programa/clases/B09/B09-C12-teorema-fundamental-del-calculo/CLASE.md).

### Energía de Fermi

- La energía de Fermi es la energía cinética en `p_F`.

💡 **Cómo se explica en la clase [B27-C01](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md):**
- Se compara `kT` con la energía de Fermi: a `10⁶ kg/m³`, `E_F = 1,64 keV` (`T_F = 1,9 × 10⁷ K`); a `10⁹`, `143,6 keV` (`1,7 × 10⁹ K`).
- La energía cinética de Fermi vale `143,6 keV`, equivalente a `1,7 × 10⁹ K`: a las temperaturas de un núcleo estelar (decenas de millones de kelvin) el gas está profundamente degenerado.
- 🎯 **Por qué importa:** Una estrella sin fusión no se desploma porque los electrones (o neutrones) no pueden apretarse más allá de lo que permite el principio de exclusión, aunque la temperatura sea cero. La decisión central: dada la densidad de un gas degenerado, ¿cuánto vale el momento de Fermi, la presión y cuál de los dos límites aplica?

📘 **Dónde se aprende** (2 clases): [B27-C01 · Presión de degeneración](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md); [B31-C06 · Estadísticas cuánticas](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md).

### Energía de Gamow

- La energía de Gamow `E_G = 2 μ c² (π α Z₁ Z₂)²` mide la dificultad de la barrera;
- La energía de Gamow `E_G = 2m_rc²(παZ₁Z₂)²`.

💡 **Cómo se explica en la clase [B24-C07](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md):**
- A["Distribución de energías<br/>exp(−E/kT)"] --> C["Producto = pico<br/>de Gamow E₀"]
- *Descripción textual:* la tasa de reacción es el producto de la distribución térmica de energías, que cae con `E`, y de la probabilidad de túnel, que crece con `E`; el máximo es el pico de Gamow y su anchura fija cómo crece la tasa con la temperatura.
- 🎯 **Por qué importa:** Dos protones se repelen con una fuerza eléctrica enorme; a las temperaturas de una estrella casi ninguno tiene energía para acercarse lo suficiente. Aun así la fusión ocurre, por efecto túnel.

📘 **Dónde se aprende** (2 clases): [B24-C07 · Ciclo CNO y cadena protón-protón](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md); [B31-C07 · Estructura nuclear](../programa/clases/B31/B31-C07-estructura-nuclear/CLASE.md).

### Energía de impacto específica

- La energía de impacto específica es `v²/2`.

💡 **Cómo se explica en la clase [B52-C17](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md):**
- Impacto a 5 km/s, fraccion termalizada 0.1: energia cinetica especifica = 1.250e+07 J/kg ;
- 🎯 **Por qué importa:** El calor determina si un cuerpo funde, se diferencia o se enfría rápido. La decisión central: ¿cuánto tarda un cuerpo en perder su calor y cuánto lo calienta un impacto?

📘 **Dónde se aprende** (1 clase): [B52-C17 · Colisiones y evolución térmica](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md).

### Energía de ionización

- La energía de ionización es la necesaria para arrancar el electrón desde un nivel hasta el infinito.
- La energía de ionización (C01) es la que cuesta arrancar el electrón más externo.

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- La energía de ionización del hidrógeno en su estado fundamental es entonces 13,606 eV (S1); el valor medido que publica la NIST es 13,5984 eV (S2), 0,05 % menor por la misma corrección de masa del núcleo que verás en 8.3.
- ⚠️ **Error frecuente:** Se detecta porque la energía de ionización sale negativa.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.

📘 **Dónde se aprende** (2 clases): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md).

### Energía de Kirchhoff

- La energía de Kirchhoff de la placa.

💡 **Cómo se explica en la clase [B43-C08](../programa/clases/B43/B43-C08-montaje-de-espejo-primario/CLASE.md):**
- E["energía de Kirchhoff"] --> B["base polinómica"]
- 🎯 **Por qué importa:** Un apoyo mal elegido deja un error de forma que ninguna pieza posterior corrige. La decisión central: ¿en qué radio conviene apoyar el espejo para que, tras quitar piston y desenfoque, quede el menor error?

📘 **Dónde se aprende** (1 clase): [B43-C08 · Montaje de espejo primario](../programa/clases/B43/B43-C08-montaje-de-espejo-primario/CLASE.md).

### Energía de ligadura

- La energía de ligadura es `−ε`: lo que falta para escapar.

💡 **Cómo se explica en la clase [B31-C07](../programa/clases/B31/B31-C07-estructura-nuclear/CLASE.md):**
- La evidencia es la ficha de la energía de ligadura del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de la energía de ligadura*: tabla de `B`, `Q`, barrera y lectura.
- 🎯 **Por qué importa:** La energía de las estrellas viene de la fusión y su cálculo parte de las masas. La decisión central: ¿cuánta energía libera una reacción y por qué ocurre pese a la barrera de Coulomb?

📘 **Dónde se aprende** (2 clases): [B31-C07 · Estructura nuclear](../programa/clases/B31/B31-C07-estructura-nuclear/CLASE.md); [B71-C05 · Energía orbital específica](../programa/clases/B71/B71-C05-energia-orbital-especifica/CLASE.md).

### Energía de ligadura del deuterón

- La energía de ligadura del deuterón `B_d` es la que separa un deuterón en un protón y un neutrón.

💡 **Cómo se explica en la clase [B26-C16](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md):**
- La energía de ligadura del deuterón es `B_d = (m_p + m_n − m_d)c² = 2,22457 MeV` (con masas nucleares, S1).
- Calcular la diferencia de energía neutrón–protón y la energía de ligadura del deuterón con masas de referencia.
- 🎯 **Por qué importa:** La cuarta parte de la masa bariónica del universo es helio, y la proporción casi no cambió desde los primeros minutos. Su valor da información sobre cuántas especies de neutrinos existen y sobre la densidad de bariones.

📘 **Dónde se aprende** (1 clase): [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Energía de ligadura del gas

- La energía de ligadura del gas es la que habría que darle para sacarlo del pozo: `E_b = ½ M_gas v²`, con `v = 3σ` ilustrativa.

💡 **Cómo se explica en la clase [B25-C16](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md):**
- La energía de ligadura crece con `M_gas v²`.
- *Descripción textual:* la función de masa da cuántas supernovas hay por masa estelar; la dispersión y la masa de gas dan la energía de ligadura; dividiendo por la energía útil de cada supernova se obtiene su número y, con él, la masa estelar necesaria.
- 🎯 **Por qué importa:** Sin retroalimentación, el gas de una galaxia se convertiría en estrellas mucho más deprisa de lo observado. Las supernovas, los vientos y la radiación de las estrellas masivas calientan y expulsan gas, y lo enriquecen con metales (C17).

📘 **Dónde se aprende** (1 clase): [B25-C16 · Retroalimentación estelar](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md).

### Energía de ligadura gravitatoria

- La energía de ligadura gravitatoria de una esfera uniforme es `3GM²/(5R)`.
- La energía de ligadura gravitatoria `E = (3/5)GM²/R`.

🎯 **Por qué importa (clase B27-C15):** El colapso libera cerca de un décimo de `Mc²`; casi todo sale en neutrinos y solo una milésima en la explosión visible. La decisión central: ¿cuánta energía libera el colapso, a qué fracción corresponde la explosión y cuánto tarda?

📘 **Dónde se aprende** (2 clases): [B27-C15 · Supernovas de colapso](../programa/clases/B27/B27-C15-supernovas-de-colapso/CLASE.md); [B52-C18 · Diferenciación planetaria](../programa/clases/B52/B52-C18-diferenciacion-planetaria/CLASE.md).

### Energía de punto cero

- La energía de punto cero es la energía mínima por confinamiento.

💡 **Cómo se explica en la clase [B31-C19](../programa/clases/B31/B31-C19-vacio-cuantico-y-limites-conceptuales/CLASE.md):**
- *Descripción textual:* la energía de punto cero suma sobre modos; la regularización aísla la parte finita, que produce la presión de Casimir con escala `d⁻⁴`.
- energia de punto cero hbar omega/2 con omega = 1e15 rad/s: 5.2729e-20 J = 0.3291 eV
- 🎯 **Por qué importa:** Las sumas infinitas de la teoría cuántica de campos exigen regularización, y el vacío tiene consecuencias medibles. La decisión central: ¿cuánto vale la presión de Casimir y qué parte de una suma divergente es física?

📘 **Dónde se aprende** (2 clases): [B31-C04 · Principio de incertidumbre](../programa/clases/B31/B31-C04-principio-de-incertidumbre/CLASE.md); [B31-C19 · Vacío cuántico y límites conceptuales](../programa/clases/B31/B31-C19-vacio-cuantico-y-limites-conceptuales/CLASE.md).

### Energía de reposo

- La energía de reposo es `E₀ = mc²`, con `m` la masa invariante.

💡 **Cómo se explica en la clase [B26-C05](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md):**
- *Descripción textual:* la energía total es la hipotenusa de un triángulo cuyos catetos son la energía de reposo, fija, y el término de momento, variable; la energía cinética es la diferencia entre la hipotenusa y el cateto fijo.
- Calcular la energía de reposo de partículas con masas de referencia.
- 🎯 **Por qué importa:** El Sol, un acelerador de partículas y la fusión de dos agujeros negros son balances de masa y energía. Para calcularlos hay que saber cuánta energía tiene una partícula en reposo y en movimiento, y por qué no puede acelerarse hasta `c`.

📘 **Dónde se aprende** (1 clase): [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md).

### Energía de retroceso

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B31-C17](../programa/clases/B31/B31-C17-materias-oscuras-candidatas/CLASE.md):**
- *Descripción textual:* el disco y el halo dan la curva total y su pendiente; la masa y la velocidad dan la longitud de onda; las masas y la velocidad dan la energía de retroceso.
- 🎯 **Por qué importa:** Una curva plana sin halo es inexplicable con la materia visible; cada candidato predice una escala distinta. La decisión central: ¿qué distingue la curva de rotación con halo y qué escalas predicen los candidatos?

📘 **Dónde se aprende** (1 clase): [B31-C17 · Materias oscuras candidatas](../programa/clases/B31/B31-C17-materias-oscuras-candidatas/CLASE.md).

### Energía de rotación

- El momento angular es `H = Iω`; la energía de rotación es `T = ½ ω·Iω`.

💡 **Cómo se explica en la clase [B87-C01](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md):**
- Calcular el momento angular `H = Iω` y la energía cinética de rotación `T = ½ ω·Iω` de un cuerpo con ejes principales.
- 🎯 **Por qué importa:** Un diseñador de actitud necesita saber qué hace el vehículo cuando nadie lo controla: ¿cuánto vale el momento angular, cómo se mueve el eje de giro y cuándo un giro aparentemente tranquilo se desestabiliza?

📘 **Dónde se aprende** (1 clase): [B87-C01 · Dinámica de cuerpo rígido](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md).

### Energía de saturación

- La energía de saturación `E_sat` es la energía por pulso a la que la ganancia del amplificador cae de forma apreciable.

💡 **Cómo se explica en la clase [B92-C01](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md):**
- Un amplificador de `30 dB` de pequeña señal y `20 µJ` de energía de saturación entrega solo `18,98 dB` si el pulso de entrada es de `1 µJ`.
- Descripción larga: al subir el orden PPM la potencia de pico crece en proporción y el amplificador entra en saturación; la ganancia efectiva cae al crecer la energía del pulso.
- 🎯 **Por qué importa:** Un enlace óptico se dimensiona con fotones, no con vatios. La decisión central: ¿cuánta potencia de pico y cuánta energía por pulso debe entregar la fuente para una potencia media dada, y hasta dónde sirve aumentar la ganancia del amplificador?

📘 **Dónde se aprende** (1 clase): [B92-C01 · Fuentes láser y amplificadores para enlaces espaciales](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md).

### Energía de un fotón

- La energía de un fotón es `E = h c/λ`, con `h c = 1239,84 eV·nm`.

💡 **Cómo se explica en la clase [B06-C18](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md):**
- Un fotón de infrarrojo (1 μm, 1,24 eV) tiene mucha energía comparada con `kT` a temperatura ambiente (0,026 eV) pero no para ionizar.
- Un fotón ultravioleta de 250 nm (4,96 eV) tiene algo menos que la energía de ionización del sodio (5,14 eV, C02), y es comparable con las energías de Coulomb entre iones (5,76 eV, C04).
- 🎯 **Por qué importa:** El hidrógeno de una nube o de una atmósfera puede ser ionizado por un fotón de longitud de onda menor que 91,2 nm. Un fotón de Lyman-alfa (121,6 nm) no lo ioniza desde el estado fundamental, pero tiene 22 veces la energía necesaria para evaporar una molécula de agua.

📘 **Dónde se aprende** (1 clase): [B06-C18 · Fotoquímica y radiación](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md).

### Energía del anillo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B30-C22](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md):**
- El anillo es como un volante de inercia que almacena energía: cuanta más energía, más disminuye el campo en el centro.
- *Descripción textual:* el campo y el radio terrestres dan la energía del dipolo; con la perturbación se obtiene la energía del anillo, el número de iones y la corriente.
- 🎯 **Por qué importa:** El índice Dst (B30-C23) es un indicador de la energía del anillo de corriente. La decisión central: ¿qué energía y qué corriente corresponden a una disminución dada del campo?

📘 **Dónde se aprende** (1 clase): [B30-C22 · Anillo de corriente y corrientes magnetosféricas](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md).

### Energía del dipolo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B30-C22](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md):**
- Esa energía es una fracción pequeña de la del dipolo (≤ 1,4 %) y la masa de iones es de cientos de kilogramos: la corriente (megaamperios) es grande, la masa pequeña.
- *Descripción textual:* el campo y el radio terrestres dan la energía del dipolo; con la perturbación se obtiene la energía del anillo, el número de iones y la corriente.
- 🎯 **Por qué importa:** El índice Dst (B30-C23) es un indicador de la energía del anillo de corriente. La decisión central: ¿qué energía y qué corriente corresponden a una disminución dada del campo?

📘 **Dónde se aprende** (1 clase): [B30-C22 · Anillo de corriente y corrientes magnetosféricas](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md).

### Energía del fotón

- La energía del fotón es `E = hc/λ`.

💡 **Cómo se explica en la clase [B92-C01](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md):**
- *Descripción textual:* la semilla pasa por el amplificador; la potencia media, con el factor de trabajo de PPM, da la potencia de pico y la energía por pulso; con la energía del fotón da la tasa de fotones.
- Calcular la energía de un fotón y la tasa de fotones de una potencia dada.
- 🎯 **Por qué importa:** Un enlace óptico se dimensiona con fotones, no con vatios. La decisión central: ¿cuánta potencia de pico y cuánta energía por pulso debe entregar la fuente para una potencia media dada, y hasta dónde sirve aumentar la ganancia del amplificador?

📘 **Dónde se aprende** (1 clase): [B92-C01 · Fuentes láser y amplificadores para enlaces espaciales](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md).

### Energía del neutrino

- La energía del neutrino en el decaimiento del pion.

💡 **Cómo se explica en la clase [B31-C16](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md):**
- *Descripción textual:* el campo y el tamaño fijan la energía máxima; el decaimiento del pion da la fracción del neutrino; el flujo y el área dan el número de eventos y la probabilidad de un exceso.
- En el decaimiento `π⁺ → μ⁺ν_μ` el neutrino lleva en promedio `0,2135` de la energía del pion.
- 🎯 **Por qué importa:** Para decir si una fuente puede producir rayos cósmicos de cierta energía y cuántos neutrinos habría, se necesitan estimaciones cuantitativas. La decisión central: ¿hasta qué energía acelera una fuente y cuántos eventos se esperan?

📘 **Dónde se aprende** (1 clase): [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md).

### Energía disipada

- La energía disipada es `½ μ v²`.

💡 **Cómo se explica en la clase [B76-C16](../programa/clases/B76/B76-C16-acoplamiento-y-captura/CLASE.md):**
- El error de momento es `3,18 × 10⁻¹⁴` y la energía disipada coincide con `½ μ v²` (`23,8636 J`).
- Comparar la energía disipada con `½ μ v²`.
- 🎯 **Por qué importa:** A velocidades de centímetros por segundo, la captura se decide por la masa, la rigidez y el amortiguamiento. La decisión central: ¿cuánta energía hay que disipar y qué fuerzas aparecen en el contacto?

📘 **Dónde se aprende** (1 clase): [B76-C16 · Acoplamiento y captura](../programa/clases/B76/B76-C16-acoplamiento-y-captura/CLASE.md).

### Energía encerrada

- La energía encerrada `EE(r)`.

💡 **Cómo se explica en la clase [B41-C12](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md):**
- El script [difraccion.py](difraccion.py) calcula Airy, los ceros de `J₁`, la energía encerrada y la obstrucción (comprueba el 1.er cero a `10⁻⁴` y la EE contra la forma cerrada a `10⁻⁶`).
- 🎯 **Por qué importa:** La difracción fija el mejor detalle posible. La decisión central: ¿cuándo se resuelven dos estrellas y qué cuesta una obstrucción?

📘 **Dónde se aprende** (4 clases): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md); [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md); [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md).

### Energía específica

- La energía específica es energía por unidad de masa (J/kg).
- La energía específica es energía por unidad de masa (J/kg), útil porque no depende de `m`.
- La energía específica (por unidad de masa) es `E = v²/2 − GM/r` y el momento angular específico, `L = x·vy − y·vx`; ambos se conservan en un campo central.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C09](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md):**
- La energía específica de un cuerpo que se mueve a rapidez `v` a distancia `r` del centro es `e = v²/2 − GM/r`.
- El script [laboratorio_signos.py](laboratorio_signos.py) calcula la energía específica de la Luna de las dos maneras de la sección 8.7, la corrección por tiempo de luz y el formato T−/T+.
- 🎯 **Por qué importa:** Cuando observas una llamarada solar a las 12:00:00, el evento ocurrió antes: su tiempo es el observado menos 499 s. Si sumas en vez de restar, afirmas que la llamarada ocurre en el futuro.

📘 **Dónde se aprende** (8 clases): [B03-C09 · Operaciones con números negativos](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md); [B05-C07 · Conservación de energía mecánica](../programa/clases/B05/B05-C07-conservacion-de-energia-mecanica/CLASE.md); [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md); [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md); [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md) y 2 más.

### Energía gravitatoria

- La energía gravitatoria `Ω` es la energía que hay que aportar para dispersar la masa hasta el infinito; es negativa.

💡 **Cómo se explica en la clase [B24-C02](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md):**
- Hasta alcanzarlas, la fuente de energía es gravitatoria.
- Al contraerse, el gas pierde energía gravitatoria; la mitad calienta el gas (la presión crece) y la otra mitad se irradia.
- ⚠️ **Error frecuente:** Pensar que toda la energía gravitatoria sale como luz. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** Una protoestrella brilla, pero no por el motor que alimenta al Sol. Para saber de dónde sale su energía, cuánto tiempo puede brillar así y cómo distinguirla de una estrella ya estable hay que seguir la energía gravitatoria.

📘 **Dónde se aprende** (1 clase): [B24-C02 · Formación de protoestrellas](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md).

### Energía isótropa

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B27-C17](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md):**
- *Descripción textual:* con `Γ` y `R` se obtiene el retardo, y al revés; la energía real se obtiene de la isótropa con la colimación; el retardo observado frente al tiempo de viaje da una cota.
- Porque supone emisión isótropa; con chorro estrecho la energía real es `f_b` veces menor.
- 🎯 **Por qué importa:** Una explosión que parece de energía enorme puede ser de energía moderada vista de frente, y un retardo de segundos entre dos mensajeros, tras viajar 130 millones de años, es una medición extraordinariamente precisa. La decisión central: ¿qué retardo y qué energía real implican un factor de Lorentz y un ángulo dados?

📘 **Dónde se aprende** (1 clase): [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md).

### Energía libre

- Entalpía: energía total de la reacción; energía libre: mínimo reversible.

💡 **Cómo se explica en la clase [B106-C05](../programa/clases/B106/B106-C05-suministro-y-generacion-de-oxigeno/CLASE.md):**
- Por kilogramo de O₂, la electrólisis consume 1,126 kg de agua, produce 0,126 kg de H₂ y exige como mínimo 4,96 kWh (entalpía; 4,12 con energía libre).
- 🎯 **Por qué importa:** Llevar oxígeno comprimido o líquido pesa; electrolizar agua exige energía y reponer agua. La decisión central: ¿cuánta agua, hidrógeno y energía implica producir el oxígeno de una tripulación y qué parte del agua devuelve la reacción de Sabatier?

📘 **Dónde se aprende** (1 clase): [B106-C05 · Suministro y generación de oxígeno](../programa/clases/B106/B106-C05-suministro-y-generacion-de-oxigeno/CLASE.md).

### Energía libre de formación estándar

- La energía libre de formación estándar `ΔG_f°` es el cambio al formar un mol de compuesto desde sus elementos a 298,15 K y 1 bar.

🎯 **Por qué importa (clase B56-C02):** Para buscar vida hay que saber qué hace la vida conocida con la materia: qué elementos usa y de dónde saca energía. La decisión central: dada una reacción metabólica, ¿está balanceada y cuánta energía libre libera o consume por mol?

📘 **Dónde se aprende** (1 clase): [B56-C02 · Bioquímica y metabolismo terrestre](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md).

### Energía libre de Gibbs

- La energía libre de Gibbs `G` mide cuánta energía puede convertirse en trabajo a `T` y `P` constantes;

💡 **Cómo se explica en la clase [B56-C02](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md):**
- Definir metabolismo, energía libre de Gibbs, energía libre de formación y eficiencia.
- 🎯 **Por qué importa:** Para buscar vida hay que saber qué hace la vida conocida con la materia: qué elementos usa y de dónde saca energía. La decisión central: dada una reacción metabólica, ¿está balanceada y cuánta energía libre libera o consume por mol?

📘 **Dónde se aprende** (1 clase): [B56-C02 · Bioquímica y metabolismo terrestre](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md).

### Energía libre de reacción

- La energía libre de reacción `ΔG` es la energía disponible por mol de reacción;

💡 **Cómo se explica en la clase [B56-C07](../programa/clases/B56/B56-C07-energia-quimica-para-la-vida/CLASE.md):**
- Definir energía libre de reacción, cociente de reacción, constante de equilibrio y potencia de mantenimiento.
- 🎯 **Por qué importa:** Un ambiente con agua pero sin fuente de energía química es un desierto para la vida. En un océano sin luz, la energía viene de reacciones entre compuestos reducidos y oxidados.

📘 **Dónde se aprende** (1 clase): [B56-C07 · Energía química para la vida](../programa/clases/B56/B56-C07-energia-quimica-para-la-vida/CLASE.md).

### Energía magnética

- La energía magnética `U = B²V/(2μ₀)`.

💡 **Cómo se explica en la clase [B27-C06](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md):**
- Para un magnetar de periodo `5 s` (ilustrativo), la energía rotacional es `½Iω² = 7,9 × 10³⁷ J`: la energía magnética es unas `210` veces mayor; por eso la emisión del magnetar no la alimenta la rotación.
- Límite: la energía magnética no se libera toda; solo una fracción puede convertirse en estallidos.
- ⚠️ **Error frecuente:** Despreciar la energía magnética. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Los magnetares producen estallidos y llamaradas gigantes que alimenta su campo, no su rotación. Entender la escala del campo y de su energía explica por qué son una familia aparte y cómo se interpretan sus espectros.

📘 **Dónde se aprende** (1 clase): [B27-C06 · Magnetares y campos extremos](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md).

### Energía máxima transferible

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C09):** Medir ΔE y E permite identificar la partícula. La decisión central: ¿qué espesor de detector y qué energía separan protones de partículas alfa?

📘 **Dónde se aprende** (1 clase): [B47-C09 · Detectores de partículas — Instrumentación y observatorios espaciales](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md).

### Energía mecánica

- La energía mecánica es `E = E_c + E_p`.
- La energía mecánica `E = E_c + E_p` se conserva si solo actúan fuerzas conservativas, o si las demás no hacen trabajo.

💡 **Cómo se explica en la clase [B05-C06](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md):**
- Con `v = √(GM/r)`, la energía cinética es `E_c = GMm/(2r)` y la potencial `E_p = −GMm/r`; la mecánica vale `E = −GMm/(2r) = −E_c`.
- Ejercicio 8. Si `E = −GMm/(2r)` y `r` crece, ¿la energía mecánica aumenta o disminuye?
- 🎯 **Por qué importa:** Poner 1000 kg en órbita cuesta mucho más que subirlos 400 km. La pregunta motivadora es: ¿cuánta energía hay que entregar para cambiar el estado de un cuerpo, y en qué se convierte?

📘 **Dónde se aprende** (2 clases): [B05-C06 · Trabajo y energía](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md); [B05-C07 · Conservación de energía mecánica](../programa/clases/B05/B05-C07-conservacion-de-energia-mecanica/CLASE.md).

### Energía media

- La energía media de un fotón es `u/n_γ = 2,701 kT`.

💡 **Cómo se explica en la clase [B26-C15](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md):**
- *Descripción textual:* la temperatura determina el número de fotones, el máximo espectral y la energía media; con la densidad de bariones del modelo se obtiene la razón barión–fotón.
- Con `T₀ = 2,72548 ± 0,00057 K` (S2, resumen), el fondo tiene `410,72` fotones por centímetro cúbico, un máximo de `B_ν` en `160,23 GHz` (`λ = 1,871 mm`) y una energía media de `0,6344 meV` por fotón (`2,701 kT`).
- ⚠️ **Error frecuente:** Pensar que la energía media es `kT`. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.

📘 **Dónde se aprende** (1 clase): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### Energía orbital específica

- La energía orbital específica `ε` es la energía mecánica por unidad de masa en J/kg.

💡 **Cómo se explica en la clase [B71-C05](../programa/clases/B71/B71-C05-energia-orbital-especifica/CLASE.md):**
- python programa/clases/B71/B71-C05-energia-orbital-especifica/energia.py
- 🎯 **Por qué importa:** El semieje fija el período y la energía; cambiar de órbita es cambiar de energía. La decisión central: ¿cuánta energía por kilogramo tiene una órbita y qué velocidad corresponde a cada distancia?

📘 **Dónde se aprende** (1 clase): [B71-C05 · Energía orbital específica](../programa/clases/B71/B71-C05-energia-orbital-especifica/CLASE.md).

### Energía por carga

- La energía por carga `E/q`.

💡 **Cómo se explica en la clase [B47-C24](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md):**
- El analizador es una criba que deja pasar solo las partículas de una energía por carga; barriendo la criba se cuenta cuántas hay de cada energía y de ahí se deducen la velocidad media y la dispersión.
- Convertir velocidad en energía por carga.
- 🎯 **Por qué importa:** La energía por carga elegida por el analizador determina qué se mide; la resolución de los canales limita la temperatura que se recupera. La decisión central: ¿cuántos canales y qué corrección dan la velocidad y la temperatura del plasma con error aceptable?

📘 **Dónde se aprende** (1 clase): [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md).

### Energía potencial

- La energía potencial es `U(q) = −log π(q)` (salvo constante), la cinética `K(p) = ½ pᵀp` y el hamiltoniano `H(q, p) = U(q) + K(p)`.

🎯 **Por qué importa (clase B19-C03):** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.

📘 **Dónde se aprende** (1 clase): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md).

### Energía potencial gravitatoria

- La energía potencial gravitatoria de una masa `m` a distancia `r` del centro de un astro de parámetro `GM` es `E_p = −GMm/r`, con cero en el infinito.

💡 **Cómo se explica en la clase [B05-C06](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md):**
- Calcular energía cinética y energía potencial gravitatoria (cerca y lejos de la Tierra).
- 🎯 **Por qué importa:** Poner 1000 kg en órbita cuesta mucho más que subirlos 400 km. La pregunta motivadora es: ¿cuánta energía hay que entregar para cambiar el estado de un cuerpo, y en qué se convierte?

📘 **Dónde se aprende** (1 clase): [B05-C06 · Trabajo y energía](../programa/clases/B05/B05-C06-trabajo-y-energia/CLASE.md).

### Energía relativa

- La energía relativa `E/m` es la energía cinética del impactor dividida por la masa del objetivo.

💡 **Cómo se explica en la clase [B118-C09](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md):**
- Calcular la energía relativa `E/m` de un impacto y compararla con el umbral ilustrativo de 40 J/g.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de fragmentación ilustrativa*: la ley, `k` y los conteos, la masa verificada por dos vías, la energía relativa de dos impactos y la lista de qué es consultado, ilustrativo y no consultado.
- 🎯 **Por qué importa:** La directriz 5 de la COPUOS dice que la mayor parte de los desechos catalogados proviene de fragmentaciones; entender cuántos fragmentos produce un evento y de qué tamaño es la base de los escenarios futuros. La decisión central: ¿cuántos fragmentos relevantes genera un evento y cuándo es «catastrófico»?

📘 **Dónde se aprende** (1 clase): [B118-C09 · Generación de desechos](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md).

### Energía requerida

- La energía requerida `ε_req = Vₑ²/(2η)` es la que la fuente debe aportar por kilo de propelente.
- La energía requerida suma las cargas de luz y de eclipse con las pérdidas de regulación y descarga.

💡 **Cómo se explica en la clase [B78-C18](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md):**
- *Descripción textual:* el escape fija la energía requerida; si la fuente la iguala o supera, el `Isp` es posible; si no, hace falta una fuente externa y el límite pasa a ser la potencia; la cota de escape es la inversa.
- Paso 2 · Energía requerida. `ε_req = 9807²/(2 × 0,6) = 8,014×10⁷ J/kg`.
- 🎯 **Por qué importa:** No todo `Isp` es posible con cualquier fuente. La decisión central: ¿qué fuente de energía alcanza para un `Isp` dado, y cuándo el límite es la energía almacenada y cuándo la potencia disponible?

📘 **Dónde se aprende** (2 clases): [B78-C18 · Energía específica y limitaciones](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md); [B83-C10 · Presupuestos de energía](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md).

### Energía térmica

- La energía térmica es la energía cinética y potencial desordenada de las partículas.
- La energía térmica característica por partícula es `kT`, con `k` la constante de Boltzmann y `T` la temperatura absoluta.

💡 **Cómo se explica en la clase [B05-C13](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md):**
- *Descripción textual:* la luz solar de potencia `S × área` es absorbida y aumenta la energía térmica; el cuerpo emite `σ A T⁴`; en el equilibrio, entrada y salida se igualan y eso fija la temperatura.
- Distinguir temperatura, calor y energía térmica, con unidades.
- 🎯 **Por qué importa:** Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: ¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?

📘 **Dónde se aprende** (3 clases): [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md); [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md); [B34-C02 · Emisión EUV y rayos X de la corona](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md).

### Energía total

- La energía total es `E = γmc²`.

💡 **Cómo se explica en la clase [B26-C05](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md):**
- *Descripción textual:* la energía total es la hipotenusa de un triángulo cuyos catetos son la energía de reposo, fija, y el término de momento, variable; la energía cinética es la diferencia entre la hipotenusa y el cateto fijo.
- Paso 3 · Energía total. `E = 2,29416 × 938,272 = 2152,5 MeV`.
- ⚠️ **Error frecuente:** Confundir energía total con cinética. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** El Sol, un acelerador de partículas y la fusión de dos agujeros negros son balances de masa y energía. Para calcularlos hay que saber cuánta energía tiene una partícula en reposo y en movimiento, y por qué no puede acelerarse hasta `c`.

📘 **Dónde se aprende** (1 clase): [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md).

### Energía umbral

- La energía umbral `E₀` es la energía mínima para reaccionar.

🎯 **Por qué importa (clase B60-C01):** Un modelo astroquímico necesita miles de constantes de velocidad. Antes de usar las de una base de datos conviene saber qué hay dentro de una: una colisión, una sección eficaz y un promedio térmico.

📘 **Dónde se aprende** (1 clase): [B60-C01 · Colisiones moleculares y secciones eficaces en gas interestelar](../programa/clases/B60/B60-C01-colisiones-moleculares-y-secciones-eficaces-en-gas-interestelar/CLASE.md).

### Energía vibracional

- La energía vibracional anarmónica es `G(v) = ωe(v+½) − ωexe(v+½)²`.

🎯 **Por qué importa (clase B62-C02):** Las bandas del CO a 4,67 µm se observan en el infrarrojo, no en milimétricas. Para interpretarlas necesitas saber de dónde sale el origen de banda, por qué las ramas P y R se separan en dos grupos y qué cambia al pasar a un isotopólogo.

📘 **Dónde se aprende** (1 clase): [B62-C02 · Espectros vibracionales de moléculas](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md).

### Enfocador

- Curva en V: HFD contra posición. Enfocador: mecanismo que mueve el foco.

💡 **Cómo se explica en la clase [B48-C22](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md):**
- La desviación de 0,10 pasos equivale a 0,52 µm de enfocador, menos que la profundidad de foco de un f/8, que una relación de libro (no consultada) sitúa en `±2 λ N²`, unos 64 µm para λ = 0,5 µm.
- Ejercicio 7. Dispersión en µm de enfocador.
- 🎯 **Por qué importa:** Un enfoque erróneo pierde resolución en todas las imágenes de la noche. La decisión central: ¿en qué posición del enfocador está el mínimo y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B48-C22 · Control automático del enfocador y autoenfoque](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md).

### Enfoque gravitacional

- El enfoque gravitacional `F_g = 1 + (v_esc/v_rel)²` aumenta la sección eficaz de captura.

💡 **Cómo se explica en la clase [B52-C05](../programa/clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md):**
- Descripción larga: el enfoque gravitacional hace el crecimiento miles de veces más rápido que el límite geométrico, aun llegando a una masa un millón de veces mayor, y el crecimiento acaba en la masa de aislamiento.
- 🎯 **Por qué importa:** El tiempo de crecimiento decide si un núcleo existe antes de que el gas se disipe. La decisión central: ¿cómo cambia la tasa de acreción con la masa y cuándo se detiene?

📘 **Dónde se aprende** (1 clase): [B52-C05 · Crecimiento de embriones planetarios](../programa/clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md).

### Enfriamiento secular

- El enfriamiento secular es la pérdida del calor almacenado.

💡 **Cómo se explica en la clase [B65-C04](../programa/clases/B65/B65-C04-flujo-termico-planetario-y-balance-termico-del-interior/CLASE.md):**
- Con una producción radiactiva ilustrativa de 20 TW, la razón de Urey es `20/47 = 0,426` y el enfriamiento secular saca `27 TW`, lo que equivale a `dT/dt = −122 K/Ga` con `C = 7×10²⁷ J/K`.
- Una casa pierde calor por las paredes; una parte la repone la calefacción (la producción radiactiva) y el resto la pierde el aire acumulado que se enfría (el enfriamiento secular).
- 🎯 **Por qué importa:** Un planeta se enfría en parte porque pierde calor guardado y en parte vive del que producen sus isótopos radiactivos. La decisión central: ¿qué fracción del calor que sale es producción actual y qué fracción es enfriamiento?

📘 **Dónde se aprende** (1 clase): [B65-C04 · Flujo térmico planetario y balance térmico del interior](../programa/clases/B65/B65-C04-flujo-termico-planetario-y-balance-termico-del-interior/CLASE.md).

### Enjambre de partículas

- El enjambre de partículas mueve partículas con inercia y atracción hacia su mejor posición y la mejor global.

💡 **Cómo se explica en la clase [B81-C13](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md):**
- Describir un algoritmo genético y un enjambre de partículas.
- 🎯 **Por qué importa:** Un método heurístico no garantiza el óptimo, pero puede evitar los mínimos locales. La decisión central: ¿qué método global elegir y cuántas evaluaciones se gastan para una tasa de éxito dada?

📘 **Dónde se aprende** (1 clase): [B81-C13 · Optimización heurística (algoritmos genéticos y enjambres)](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md).

### ENL

- El ENL (número equivalente de vistas) mide cuánto speckle queda.

💡 **Cómo se explica en la clase [B69-C03](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md):**
- Al promediar `L` vistas independientes, `CV = 1/√L` y `ENL = L`.
- En la zona de reflectividad 1, el ENL pasa de 1,01 a 21,19; en la de 4, de 0,94 a 16,60; las medias no cambian (0,984 → 0,984 y 4,112 → 4,115).
- 🎯 **Por qué importa:** Un valor de píxel aislado de una imagen SAR no mide la reflectividad de la superficie: es una muestra de una distribución muy ancha. La decisión central: ¿cuánto hay que promediar o filtrar para estimar la reflectividad con una incertidumbre dada, y a qué precio en resolución?

📘 **Dónde se aprende** (1 clase): [B69-C03 · Ruido speckle y filtrado en imágenes SAR](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md).

### Enlace covalente

- En un enlace covalente dos átomos comparten uno o más pares de electrones: un par es enlace simple; dos, doble; tres, triple.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- El enlace O–H del agua es covalente, pero el oxígeno atrae más a los electrones que el hidrógeno, por lo que cada hidrógeno queda con una carga parcial positiva y el oxígeno con una negativa.
- B -->|"No: ambos atraen electrones"| D["Pares compartidos: enlace covalente"]
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Enlace directo a la Tierra (DTE)

- Rango oblicuo: distancia estación–satélite según la elevación. Enlace directo a la Tierra (DTE): comunicación sin relé.

🎯 **Por qué importa (clase B96-C01):** Quien opera una nave no puede tratarla como un equipo de laboratorio: cada comando viaja a la velocidad de la luz y cada contacto dura minutos. La decisión central: ¿qué segmento hace qué y cuánto tardan en comunicarse?

📘 **Dónde se aprende** (1 clase): [B96-C01 · Segmento espacial y segmento terrestre](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md).

### Enlace iónico

- En un enlace iónico la atracción entre iones de signo opuesto mantiene la unión.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- B -->|"Sí"| C["Iones de signo opuesto: enlace iónico (atracción de Coulomb)"]
- Distinguir enlace iónico, covalente y covalente polar con ejemplos.
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Enmascaramiento

- El enmascaramiento ocurre cuando varios atípicos inflan la media y la desviación y ninguno se detecta.

💡 **Cómo se explica en la clase [B12-C19](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md):**
- Puntaje z modificado: robusto, resiste el enmascaramiento, el umbral es convencional.
- Un segundo caso muestra el enmascaramiento con dos errores, y un tercero un atípico bivariado.
- 🎯 **Por qué importa:** Un dato aberrante puede ser un error del instrumento, una pérdida de sincronía o el primer indicio de un fenómeno real. Eliminarlo sin criterio esconde información; conservarlo sin revisar contamina el resultado.

📘 **Dónde se aprende** (1 clase): [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md).

### Enrojecimiento

- El enrojecimiento es el aumento del pendiente hacia el rojo.

🎯 **Por qué importa (clase B53-C22):** Una superficie «vieja» se ve distinta de una «fresca» aunque tenga la misma composición. La decisión central: ¿cuánto del cambio espectral se debe al tiempo de exposición y con qué incertidumbre se estima su escala?

📘 **Dónde se aprende** (1 clase): [B53-C22 · Meteorización espacial: micrometeoritos, viento solar y maduración del regolito](../programa/clases/B53/B53-C22-meteorizacion-espacial-micrometeoritos-viento-solar-y-maduracion-del-regolito/CLASE.md).

### Ensamblaje

- El ensamblaje suma las contribuciones de cada elemento.
- El ensamblaje suma las contribuciones en la matriz global `K`.
- Ensamblaje: unir piezas mecánicamente.

💡 **Cómo se explica en la clase [B90-C01](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md):**
- python programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/plan_ensamblaje.py
- 🎯 **Por qué importa:** La integración es la fase donde los errores de diseño se vuelven visibles y caros. Un plan que no distingue las tareas críticas de las que tienen holgura gasta esfuerzo en el lugar equivocado.

📘 **Dónde se aprende** (3 clases): [B11-C15 · Elementos finitos introductorios](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md); [B84-C12 · Análisis de elementos finitos](../programa/clases/B84/B84-C12-analisis-de-elementos-finitos/CLASE.md); [B90-C01 · Plan de ensamblaje e integración](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md).

### Ensanchamiento

- El ensanchamiento (factor 1,25 aquí) es el crecimiento del diámetro por el colapso de la pared.

💡 **Cómo se explica en la clase [B61-C02](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md):**
- T["cráter transitorio D_t, d_t"] --> A["ensanchamiento x1,25"]
- Distinguir el cráter transitorio del aparente y usar el factor de ensanchamiento.
- 🎯 **Por qué importa:** Medir un cráter es medir un bol, pero lo que se ve es el bol después de colapsar y rellenarse. La decisión central: ¿cuánto volumen tenía la cavidad original y cuánto se perdió en el relleno de brecha?

📘 **Dónde se aprende** (1 clase): [B61-C02 · Cráteres simples: morfología y formación](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md).
