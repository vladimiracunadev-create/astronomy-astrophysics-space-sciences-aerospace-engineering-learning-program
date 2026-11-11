# Siglas y acrónimos (parte 1 de 2)

[⬅️ Índice del glosario](README.md)

Siglas y acrónimos que las clases definen en su vocabulario, en orden alfabético. Si una sigla no aparece, ninguna clase la presentó en su vocabulario.

Partes: **1** · [2](siglas-2.md)

### A2

- Los niveles I, II y III escalan la revisión según actividad, probabilidad de dosis y fisión. A2 es el valor de actividad de la tabla de la IAEA SSR-6.

💡 **Cómo se explica en la clase [B86-C18](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md):**
- El Nivel I cubre fuentes radiactivas hasta `100000 × A2` (valor de la tabla 2 de la IAEA SSR-6, Rev.1).
- El nivel de la fuente de `3408 g` con `A2 = 10⁸`, `10⁹`, `10¹⁰` y `10¹¹ Bq` es `2`, `2`, `2` y `1`, y el umbral de masa del Nivel I se mueve de `15,8 g` a `15783 g`.
- ⚠️ **Error frecuente:** Tomar el `A2` ilustrativo como dato real. Se corrige con 8.3.
- 🎯 **Por qué importa:** Los límites de la energía nuclear en el espacio son tanto jurídicos y de seguridad como técnicos: quién aprueba, con qué análisis y con qué umbrales. Un ingeniero de potencia debe saber que estas decisiones existen y qué datos las gobiernan.
- 🔗 **Se estudia junto con:** NSPM-20, niveles I, II y III, TED, LEU.

📘 **Dónde se aprende:** [B86-C18 · Seguridad y licenciamiento energético](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md).

### AC

- El PV es el valor del trabajo planificado a la fecha; el EV, el valor del trabajo logrado; el AC, el costo real.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- La suma de los paquetes coincide con la de los elementos y con el proyecto para BAC, PV, EV y AC (error `0,0e+00`): lo que está en los hijos es todo lo que está en el padre.
- Con `PV = 57,00`, `EV = 47,70` y `AC = 60,00`: `CV = EV − AC = -12,30` y `SV = EV − PV = -9,30` Mum;
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, EV, CPI.

📘 **Dónde se aprende:** [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### ACH

- **Significa:** Renovaciones por hora (ACH).
- La presión negativa es una presión interior menor que la exterior. ACH es el número de renovaciones de aire por hora.
- Filtro de alta eficiencia: filtro que retiene la fracción `η` de las partículas del aire que lo cruza. Renovaciones por hora (ACH): `Q·3600/V`.

💡 **Cómo se explica en la clase [B63-C05](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md):**
- Con mezcla perfecta, `dC/dt = −ACH·C`, luego `C(t) = C₀ e^(−ACH·t)`.
- Para reducir la concentración por un factor `R`, `t = ln R / ACH`.
- ⚠️ **Error frecuente:** Usar ACH en 1/h con el tiempo en segundos. Se corrige con la tabla de la sección 9.
- 🎯 **Por qué importa:** Contener no es un adjetivo: es un conjunto de diferencias de presión, flujos y filtros que se pueden calcular. La decisión central: ¿qué impide que el aire de la sala salga, y cuánto tarda en limpiarse si se contamina?
- 🔗 **Se estudia junto con:** contención, presión negativa, mezcla perfecta, eficiencia.

📘 **Dónde se aprende:** [B63-C05 · Contención de muestras extraterrestres: instalaciones y principios](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md); [B90-C02 · Buenas prácticas de sala limpia](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md).

### ACWR

- La ACWR es su cociente.

💡 **Cómo se explica en la clase [B107-C05](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md):**
- Para `ACWR ≤ 1,3` con crónica previa de 100: `a/((300 + a)/4) ≤ 1,3`, es decir `a ≤ 144,4`: un aumento del 44 %.
- Una curva logística en U inventada (`logit = −3 + 3 (ACWR − 1)²`) da `7,4 %` para 0,6, `4,7 %` para 1,0, `6,1 %` para 1,3 y `12,8 %` para 1,6.
- 🎯 **Por qué importa:** El fragmento consultado de English et al. (2015) subraya que la pérdida de fuerza en misiones largas implica riesgos operativos y médicos, entre ellos el egreso de emergencia; y Loehr et al.
- 🔗 **Se estudia junto con:** carga aguda, crónica, EWMA, acoplamiento.

📘 **Dónde se aprende:** [B107-C05 · Prevención de lesiones en entrenamiento y trabajo operativo](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md).

### AD2

- La AD2 (dificultad de avance, S5) estima cuán difícil es subir de nivel; aquí es una escala 1–5 sintética.

💡 **Cómo se explica en la clase [B83-C18](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md):**
- Con 3 meses por nivel y un factor de dificultad `1 + 0,25·(AD2 − 1)`, el esfuerzo a TRL 6 es de 18,75 meses-elemento; si todo avanza en paralelo, el plazo lo fija Detector de imagen: 10,50 meses.
- A["AD2 por elemento"] --> P["Esfuerzo de madurizacion"]
- 🎯 **Por qué importa:** Un elemento «con herencia de vuelo» que se usa en otro entorno no es TRL 9. La decisión central: ¿cuál es el TRL real del sistema, qué elementos lo frenan y cuánto cuesta llevarlos al nivel que pide la revisión?
- 🔗 **Se estudia junto con:** TRL, TRL del sistema, herencia, evaluación de madurez.

📘 **Dónde se aprende:** [B83-C18 · Niveles de madurez tecnológica](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md).

### ADC

- El ADC convierte voltaje en cuentas con `b` bits.

💡 **Cómo se explica en la clase [B44-C18](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md):**
- Un ADC de 12 bits (`7,05 e⁻`) con este pozo supera al ruido de lectura de `4 e⁻`.
- ADC["bits del ADC"] --> Q["cuantización"]
- 🎯 **Por qué importa:** Leer lento reduce ruido pero desperdicia tiempo de observación. La decisión central: ¿qué modo de lectura equilibra ruido y tiempo muerto?
- 🔗 **Se estudia junto con:** puerto, binning, tiempo muerto, sobrecarga.

📘 **Dónde se aprende:** [B44-C18 · Control electrónico de cámaras](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md).

### ADM

- ADM son armas de destrucción masiva.

💡 **Cómo se explica en la clase [B119-C11](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md):**
- ADM en órbita: prohibido; base militar en la Luna: prohibido; científicos militares en la Luna: condicionado; telescopio civil en un asteroide: permitido; satélite de observación en órbita: fuera del art.
- Paso 2. Sin ADM; hay cuerpo celeste; sin base.
- 🎯 **Por qué importa:** C01 reduce el art. IV a una regla booleana; esta clase lo desagrega por ubicación y propósito y conecta con el art. 3 del Acuerdo sobre la Luna, y deja explícito lo no consultado.
- 🔗 **Se estudia junto con:** Condicionado, Fuera del art. IV, cuerpo celeste, lista de reglas.

📘 **Dónde se aprende:** [B119-C11 · Uso pacífico y limitaciones militares](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md).

### ADQL

- Una consulta selecciona filas y columnas con criterios. ADQL es el lenguaje de consultas astronómicas del IVOA y TAP el protocolo para enviarlas (S1).

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- No hay red, autenticación, reintentos, paginación ni descargas parciales; el servidor es local y la consulta ADQL no se envió, de modo que no sé qué respondería un servicio real.
- Consultar en el servidor (TAP/ADQL) reduce lo transferido pero depende de la disponibilidad y del servicio.
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.
- 🔗 **Se estudia junto con:** flujo de datos, adquisición, verificación, caché.

📘 **Dónde se aprende:** [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md).

### ADU

- El ADU (*analog-to-digital unit*) es la unidad del número que entrega el conversor.

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- Con `K = 1`: `10,30` ADU (observado `10,34`).
- La apertura contiene el 99,65 % del flujo (1993 de 2000 ADU).
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.
- 🔗 **Se estudia junto con:** imagen digital, píxel, ganancia, bias.

📘 **Dónde se aprende:** [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md).

### AF

- **Significa:** Factor de aceleración (AF).
- Presión límite: `Q_gas/S`. Factor de aceleración (AF): ciclos de servicio por ciclo de ensayo.

💡 **Cómo se explica en la clase [B90-C12](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md):**
- El coeficiente 1,9, el exponente 1/3 y el 1 414 K del factor de aceleración son valores de la literatura que no se consultaron.
- O["Orbita: dT 40 K<br/>5840 ciclos/ano"] --> A["Factor de aceleracion<br/>AF = 12.04"]
- 🎯 **Por qué importa:** Una nave en órbita baja sufre unos 16 ciclos térmicos por día; no se pueden repetir 5 840 ciclos en tierra. La decisión central: ¿cuántos ciclos de ensayo con mayor amplitud representan un año de órbita y cuánto tarda la campaña?
- 🔗 **Se estudia junto con:** Vacío térmico (TVAC), Bakeout, Ciclado, Presión límite.

📘 **Dónde se aprende:** [B90-C12 · Vacío térmico y ciclos](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md).

### AGB

- **Significa:** rama asintótica de gigantes (AGB).
- La rama asintótica de gigantes (AGB) es la fase de masa baja e intermedia con un núcleo inerte de carbono y oxígeno rodeado de dos capas de fusión, de helio y de hidrógeno (descripción cualitativa estándar; las cifras no se consultaron).

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- python programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/proceso_s.py
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.
- 🔗 **Se estudia junto con:** pulso térmico, dragado, proceso s, exposición de neutrones.

📘 **Dónde se aprende:** [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### AGN

- **Significa:** núcleo activo de galaxia (AGN).
- Un núcleo activo de galaxia (AGN) es una región central cuya luminosidad no procede de estrellas sino de la acreción de gas sobre un agujero negro supermasivo.

💡 **Cómo se explica en la clase [B25-C11](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md):**
- python programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/agn_basico.py
- 🎯 **Por qué importa:** Algunas galaxias tienen en el centro una fuente que supera a todas sus estrellas, y casi todas las galaxias grandes albergan un agujero negro supermasivo. Entender el AGN une el centro de la galaxia, su gas y su evolución.
- 🔗 **Se estudia junto con:** acreción, eficiencia radiativa, luminosidad de Eddington, tiempo de Salpeter.

📘 **Dónde se aprende:** [B25-C11 · Núcleos activos de galaxias](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md).

### AHP

- **Significa:** proceso analítico jerárquico (AHP).
- El proceso analítico jerárquico (AHP) deriva pesos de comparaciones pareadas.
- Un estudio de compromiso (*trade study*) compara candidatas con criterios. AHP convierte comparaciones por pares (escala 1–9) en pesos.

💡 **Contexto en la clase [B57-C19](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md):**
- **Idea central (modelo mental):** Un mapa de riesgo es una receta: los pesos dicen cuánto vale cada ingrediente y el resultado cambia si cambias las proporciones.
- 🎯 **Por qué importa:** Los mapas de riesgo orientan decisiones y presupuestos, pero dependen de supuestos de ponderación que suelen quedar ocultos. La decisión central: ¿cómo combino capas y cuánto cambian las zonas prioritarias si cambio los pesos?
- 🔗 **Se estudia junto con:** amenaza, exposición, vulnerabilidad, razón de consistencia.

📘 **Dónde se aprende:** [B57-C19 · SIG y análisis de riesgo](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md); [B83-C07 · Arquitecturas de sistemas](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md).

### ALA

- **Significa:** ala.
- Un ala es un conjunto de paneles unidos por bisagras.
- Los esquemas de datos se nombran LAL (lado–ángulo–lado), LLL (tres lados), ALA (ángulo–lado–ángulo) y LLA (lado–lado–ángulo no incluido).

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- B -->|"ALA"| D["Tercer ángulo = 180° − A − B; luego ley de senos"]
- *Descripción textual:* según los datos (LAL o LLL, ALA o LLA) se usa la ley de cosenos, el tercer ángulo y la de senos, o la de senos con posible ambigüedad; todo termina comprobando que los ángulos suman 180°.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.
- 🔗 **Se estudia junto con:** ley de cosenos, ley de senos, resuelve, LAL.

📘 **Dónde se aprende:** [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md); [B86-C03 · Arreglos fotovoltaicos desplegables](../programa/clases/B86/B86-C03-arreglos-fotovoltaicos-desplegables/CLASE.md).

### ALARA

- Un límite administrativo es un valor más estricto que se usa para cumplir el estándar. ALARA es el principio de mantener la exposición tan baja como sea razonablemente alcanzable.

💡 **Contexto en la clase [B112-C06](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md):**
- 🎯 **Por qué importa:** Falta la clase de estimación de riesgo por misión. Es la que usa un planificador: suma dosis de cada tramo, la convierte en riesgo y decide si cabe dentro de un límite.
- 🔗 **Se estudia junto con:** riesgo de exceso de muerte inducida por exposición, límite de carrera, nivel del 95 % de confianza, límite administrativo.

📘 **Dónde se aprende:** [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### AN

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?
- 🔗 **Se estudia junto con:** términos, IA, IE, CA.

📘 **Dónde se aprende:** [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### ANOVA

- **Significa:** análisis de varianza (ANOVA) de un factor.
- Un análisis de varianza (ANOVA) de un factor descompone la variación total en una parte entre grupos y una parte dentro de los grupos.

💡 **Cómo se explica en la clase [B13-C14](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md):**
- Realizar un análisis de varianza de un factor con diseño equilibrado.
- 🎯 **Por qué importa:** Ocho estaciones de seguimiento miden el mismo desfase de un reloj de referencia. Cada una repite su medida cinco veces y obtiene resultados muy parecidos entre sí, pero las estaciones discrepan entre ellas.
- 🔗 **Se estudia junto con:** condición de repetibilidad, condición de precisión intermedia, condición de reproducibilidad, desviación de repetibilidad s_r.

📘 **Dónde se aprende:** [B13-C14 · Repetibilidad y reproducibilidad](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md).

### AOS/LOS

- Holgura: `LS − ES`. AOS/LOS: inicio y fin del contacto.

💡 **Contexto en la clase [B96-C09](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md):**
- 🎯 **Por qué importa:** Una secuencia que no cabe en la ventana deja comandos sin ejecutar o telemetría sin confirmar. La decisión central: ¿qué actividades fijan la duración mínima y cuánta holgura queda?
- 🔗 **Se estudia junto con:** Secuencia, Camino crítico, ES/EF, LS/LF.

📘 **Dónde se aprende:** [B96-C09 · Secuencias de misión](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md).

### AP

- El AP es el área bajo la curva precisión-exhaustividad con la precisión interpolada.

💡 **Cómo se explica en la clase [B103-C08](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md):**
- Control: un detector perfecto da `AP = 1,000`.
- El AP es el área bajo la curva con precisión interpolada: `AP50 = 0,581`.
- 🎯 **Por qué importa:** Un segmentador que acierta el 99 % de los píxeles puede no encontrar nunca la clase que importa, y dos detectores con AP de 0,58 y 0,60 pueden ser indistinguibles con 100 imágenes. La decisión central: ¿qué métricas y qué intervalo hacen falta para afirmar que un algoritmo de percepción es suficiente para una tarea?
- 🔗 **Se estudia junto con:** IoU, precisión, exhaustividad, MAE.

📘 **Dónde se aprende:** [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md).

### API

- Una API (interfaz de programación) es el contrato por el que un programa pide datos a otro.

💡 **Cómo se explica en la clase [B14-C31](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md):**
- La paginación por desplazamiento es sensible a inserciones durante el recorrido (un elemento nuevo desplaza los siguientes); en una API con datos cambiantes se prefiere un cursor, que no se trata aquí.
- La API paginada entrega por partes y permite filtros.
- 🎯 **Por qué importa:** Tu catálogo de escenas tiene 250 000 ítems y un programa ajeno quiere recorrerlos. Si le entregas una lista de golpe, se cae; si cada petición repite lo que ya tiene, desperdicias ancho de banda; si cambia un parámetro y falla sin explicación, nadie sabe qué hizo mal.
- 🔗 **Se estudia junto con:** recurso, ruta, Paginar, código de estado.

📘 **Dónde se aprende:** [B14-C31 · APIs de servicios de datos](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md).

### ARF

- La ARF es el área efectiva en función de la energía.

💡 **Cómo se explica en la clase [B27-C22](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md):**
- M["modelo K(E/3)^−Γ"] --> A["× ARF × exposición × ΔE"]
- El manual de XSPEC describe el ajuste de modelos a datos con respuesta (S2, página consultada sin las definiciones de `χ²`, C-stat, RMF ni ARF); el telescopio Fermi-LAT cubre de menos de `20 MeV` a más de `300 GeV` (S3, resumen).
- 🎯 **Por qué importa:** Ajustar un espectro «de fotones» directamente a las cuentas da resultados engañosos; hay que plegar el modelo con la respuesta y usar la estadística correcta para conteos pequeños. La decisión central: ¿qué parámetros recupera cada estadística y con qué sesgo cuando las cuentas son pocas?
- 🔗 **Se estudia junto con:** RMF, plegado, estadística de Cash, χ² con varianza igual a las cuentas.

📘 **Dónde se aprende:** [B27-C22 · Análisis espectral de rayos X y gamma: ajuste con respuesta instrumental](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md).

### ARL

- **Significa:** ARL₀.
- El ARL es la longitud media de racha: `ARL₀` en control (falsas alarmas) y `ARL₁` bajo desplazamiento.
- El ARL₀ es la longitud media hasta una falsa alarma.

💡 **Cómo se explica en la clase [B84-C35](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md):**
- *Descripción textual:* los subgrupos alimentan las dos cartas; la simulación da los ARL, que se contrastan con la teoría;
- ARL en control: `369,7` (teórica `370,4`); con `+1σ`, Shewhart `4,50` y EWMA `2,31`.
- 🎯 **Por qué importa:** Un proceso con `Cpk` de 1,33 puede desplazarse 1σ sin dejar piezas fuera de tolerancia durante semanas si solo se inspecciona el producto; la carta lo detecta en pocos subgrupos. La decisión central: ¿qué carta detecta antes un desplazamiento del proceso y qué capacidad tiene el proceso antes y después?
- 🔗 **Se estudia junto con:** carta X-barra, EWMA.

📘 **Dónde se aprende:** [B84-C35 · Control de procesos de fabricación y calidad](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md); [B97-C22 · Detección autónoma de eventos científicos](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md).

### ARPA

- El ARPA es el ingreso medio por cliente y mes.

💡 **Cómo se explica en la clase [B126-C04](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md):**
- El ejemplo conductor es un servicio sintético de datos de observación de la Tierra por suscripción: gasto de captación de 240 000 USD por trimestre con 60 clientes nuevos, ingreso mensual por cliente (ARPA) de 900 USD, margen bruto de 70 % y abandono mensual de 2 %.
- 🎯 **Por qué importa:** Un negocio espacial debe medir cuánto cuesta ganar un cliente; el catálogo no lo trata. La decisión central: ¿vale la pena el gasto de captación, dado cuánto tiempo se queda el cliente y cuánto margen deja?
- 🔗 **Se estudia junto con:** CAC, margen bruto, abandono, LTV.

📘 **Dónde se aprende:** [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### ARPU

- El ARPU es el ingreso por suscriptor y mes.
- El ARPU es el ingreso mensual medio por cliente.

💡 **Cómo se explica en la clase [B124-C11](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md):**
- Si la vida útil baja a 3,5 años el equilibrio sube a `78333` (`1,21` veces); si sube a 7, baja a `55833`; si el ARPU cae a 40 um/mes, sube a `81042`.
- *Descripción textual:* la flota y su vida dan la tasa de reposición, que se verifica por simulación; esta, más el costo operativo, da el costo anual y, con el ARPU, el equilibrio en suscriptores.
- 🎯 **Por qué importa:** Una constelación puede ser técnicamente exitosa y económicamente inviable si la reposición se come el margen. La decisión central: ¿cuántos suscriptores se necesitan para cubrir la reposición y la operación, y qué tan sensible es eso a la vida útil?
- 🔗 **Se estudia junto con:** reposición, tasa de renovación, reserva de desorbitación, punto de equilibrio.

📘 **Dónde se aprende:** [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md); [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md).

### ARQ

- Ráfaga: error en bits consecutivos. ARQ: retransmisión automática.

💡 **Contexto en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?
- 🔗 **Se estudia junto con:** Prueba de extremo a extremo, CRC, BER, FER.

📘 **Dónde se aprende:** [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### ARW

- El ARW (*angle random walk*) `N` es el ruido blanco de la tasa, en `rad/√s`.

💡 **Cómo se explica en la clase [B87-C06](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md):**
- G["tasa medida = verdad + ARW + sesgo RRW"] --> P["promedios de duracion tau"]
- Analogía: un reloj que se adelanta con un tic aleatorio (ARW) y que además cambia de ritmo a lo largo del día (RRW): para periodos cortos domina el tic y para largos domina el cambio de ritmo.
- 🎯 **Por qué importa:** Entre dos medidas de un sensor de vector, la actitud se propaga integrando el giroscopio, y esa integración se desvía. La decisión central: ¿cada cuánto hay que corregir con otro sensor, y qué parte de la deriva es ruido blanco y cuál sesgo?
- 🔗 **Se estudia junto con:** RRW, varianza de Allan, inestabilidad de sesgo, tasa de muestreo.

📘 **Dónde se aprende:** [B87-C06 · Giroscopios MEMS](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md).

### ASD

- La ASD (*acceleration spectral density*) es `G(f)` en g²/Hz.

💡 **Cómo se explica en la clase [B84-C01](../programa/clases/B84/B84-C01-entorno-mecanico-de-lanzamiento/CLASE.md):**
- La aceptación es la mitad de la ASD (−3 dB) y su `g` rms es `14,14/√2 ≈ 10,0`.
- A["ASD por tramos<br/>f, G"] --> B["exponente m<br/>por tramo"]
- 🎯 **Por qué importa:** Un satélite no falla en órbita por el empuje del motor sino por la sacudida de la subida; esa sacudida se especifica con un espectro, no con un número. Un espectro con 0,16 g²/Hz de meseta no dice nada hasta que se integra.
- 🔗 **Se estudia junto con:** valor eficaz, Calificación, aceptación, mano de obra mínima.

📘 **Dónde se aprende:** [B84-C01 · Entorno mecánico de lanzamiento](../programa/clases/B84/B84-C01-entorno-mecanico-de-lanzamiento/CLASE.md).

### ASET

- El ASET (*available safe egress time*) es el tiempo disponible antes de que el peligro impida la salida; aquí se toma igual a `T_Res`.

💡 **Cómo se explica en la clase [B110-C03](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md):**
- Paso 1 · ASET. `58,19 × (10/20)² = 14,55 min`.
- Una cabina de 100 m³ con un orificio de 20 mm da un ASET de `14,55 min`.
- 🎯 **Por qué importa:** Ninguna clase anterior trata evacuación, refugio y vehículos de escape. La decisión central: ¿alcanza el margen entre ASET y RSET, y cuánto de ese margen depende de supuestos que no se conocen?
- 🔗 **Se estudia junto con:** RSET, margen, refugio, cuello de botella.

📘 **Dónde se aprende:** [B110-C03 · Evacuación y refugio de emergencia](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md).

### ATE

- Ancla: pose fija que elimina la libertad de colocar el grafo en cualquier lugar. ATE: error absoluto de trayectoria (C06).
- ATE: RMSE de la traslación tras alinear la estimación con la verdad por cuerpo rígido (F2).

💡 **Cómo se explica en la clase [B99-C03](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md):**
- La odometría sola termina a 1,741 m del origen (ATE 0,576 m); tras optimizar, a 0,028 m (ATE 0,172 m), con el `χ²` cayendo de 7 603,3 a 4,2 en dos iteraciones.
- Descripción larga: el cierre de bucle reduce el error de la pose final en un factor 60, pero el ATE solo baja a 0,17 m, porque el error se reparte a lo largo de toda la trayectoria.
- 🎯 **Por qué importa:** Sumar movimientos da una trayectoria que no cierra el lazo; una medida de cierre de bucle dice que la pose final es la inicial. La decisión central: ¿cómo repartir el desacuerdo entre cientos de poses de modo coherente con la incertidumbre de cada medida?
- 🔗 **Se estudia junto con:** Grafo de poses, Medida z_ij, Información Ω_ij, Error de arista e_ij.

📘 **Dónde se aprende:** [B99-C03 · SLAM basado en grafos de poses](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md); [B99-C06 · Evaluación de deriva y error de trayectoria](../programa/clases/B99/B99-C06-evaluacion-de-deriva-y-error-de-trayectoria/CLASE.md).

### AUC

- **Significa:** área (AUC).
- El AUC es el área bajo ella.
- El AUC es `F D/CL`.
- El AUC es la probabilidad de que un afectado supere a un sano.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B17-C05](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md):**
- Comparar métodos con el área bajo la curva ROC.
- 🎯 **Por qué importa:** El subsistema térmico de un satélite entrega temperatura y corriente. Cada una, por separado, puede estar dentro de su rango normal y sin embargo la pareja ser imposible: la corriente alta con temperatura baja no ocurre nunca en operación sana.
- 🔗 **Se estudia junto con:** anomalía, distancia de Mahalanobis, distribución chi-cuadrado, bosque de aislamiento.

📘 **Dónde se aprende:** [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md); [B33-C14 · Verificación de alertas con tablas de contingencia](../programa/clases/B33/B33-C14-verificacion-de-alertas-con-tablas-de-contingencia/CLASE.md); [B105-C13 · Farmacología y microgravedad](../programa/clases/B105/B105-C13-farmacologia-y-microgravedad/CLASE.md); [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md).

### AW

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?
- 🔗 **Se estudia junto con:** términos, IA, IE, CA.

📘 **Dónde se aprende:** [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### BAC

- El BAC es el presupuesto total.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- La suma de los paquetes coincide con la de los elementos y con el proyecto para BAC, PV, EV y AC (error `0,0e+00`): lo que está en los hijos es todo lo que está en el padre.
- Gastado: `75,0%` del BAC; logrado: `59,6%`.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** PV, EV, AC, CPI.

📘 **Dónde se aprende:** [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### BAO

- **Significa:** oscilaciones acústicas de bariones (BAO).
- Las oscilaciones acústicas de bariones (BAO) dejaron una escala característica en la distribución de galaxias.

💡 **Contexto en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- **Idea central (modelo mental):** En un universo solo de materia, cada fluctuación crece como el factor de escala. Cuando la constante cosmológica domina, la expansión se acelera y las fluctuaciones dejan de crecer con tanta facilidad: la gravedad pierde la pelea contra la expansión.
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.
- 🔗 **Se estudia junto con:** perturbación de densidad, crecimiento lineal, ecuación de crecimiento, supresión.

📘 **Dónde se aprende:** [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md).

### BCET

- El BCET es la inferior.

💡 **Cómo se explica en la clase [B88-C30](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md):**
- El script [wcet.py](wcet.py) calcula el WCET y el BCET estáticos, mide 100 000 entradas aleatorias, estima el efecto de la caché y convierte a µs y utilización, y comprueba que el máximo medido no supera la cota.
- 🎯 **Por qué importa:** El análisis de planificación (C05) necesita `C` de cada tarea, y medir no basta porque el peor camino puede no ejercitarse. La decisión central: ¿cuál es una cota segura del tiempo de ejecución y cuánto pesimismo trae?
- 🔗 **Se estudia junto con:** WCET, camino más largo, pesimismo, fallo de caché.

📘 **Dónde se aprende:** [B88-C30 · Análisis de peor caso de tiempo de ejecución (WCET)](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md).

### BDF2

- Euler implícito: `y_{n+1} = y_n + h f(t_{n+1}, y_{n+1})`. BDF2 (fórmula de diferenciación hacia atrás de orden 2): `y_{n+1} = (4 y_n − y_{n−1})/3 + (2h/3) f(t_{n+1}, y_{n+1})`.

💡 **Cómo se explica en la clase [B11-C22](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md):**
- BDF2 `1,6 × 10⁻⁸ … 2,5 × 10⁻¹⁰`, órdenes `2,00`; trapezoidal `4,0 × 10⁻⁹ … 6,3 × 10⁻¹¹`, órdenes `2,00`.
- Con una condición inicial fuera de la solución lenta (`y(0) = 3,5`) y `h = 0,01`: BDF2 elimina el transitorio (desvío `4 × 10⁻⁹` en la mitad final);
- 🎯 **Por qué importa:** Los modelos térmicos, de combustión, de propulsión y de química atmosférica mezclan escalas de microsegundos con horas. Un integrador explícito pagaría el paso del más rápido durante toda la simulación.
- 🔗 **Se estudia junto con:** implícito, Euler implícito, Trapezoidal, Newton.

📘 **Dónde se aprende:** [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md).

### BER

- La BER de BPSK en AWGN es `Q(√(2Eb/N0)) = ½ erfc(√(Eb/N0))`.
- CRC: código de redundancia cíclica. BER: tasa de error de bit.

💡 **Cómo se explica en la clase [B47-C18](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md):**
- *Descripción textual:* la potencia radiada, las ganancias y las pérdidas dan `C/N₀`; dividido por la velocidad da `Eb/N₀`, que fija la BER.
- Hallar la `Eb/N₀` requerida para BER 10⁻⁵.
- ⚠️ **Error frecuente:** Tomar la BER teórica como medida. Se corrige con 8.2.
- 🎯 **Por qué importa:** Los datos que no caben en un paso se pierden o se acumulan. La decisión central: ¿cuántos bits por paso admite el enlace con margen suficiente?
- 🔗 **Se estudia junto con:** presupuesto de enlace, pérdida de espacio libre, PIRE, relación G/T.

📘 **Dónde se aprende:** [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md); [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md); [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### BFD

- **Significa:** distancia focal posterior (BFD).
- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C08](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md):**
- Medir la distancia focal posterior exacta por altura.
- paraxial (matrices): f = 195.0857 mm ; distancia focal posterior (vertice) = 191.7614 mm
- 🎯 **Por qué importa:** Los programas de diseño óptico trazan rayos exactos. La decisión central: ¿cuándo se separa el rayo real del paraxial y cómo crece esa diferencia?
- 🔗 **Se estudia junto con:** trazado exacto, aproximación paraxial, aberración esférica longitudinal, altura del rayo.

📘 **Dónde se aprende:** [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md).

### BINTABLE

- FITS: bloques de 2880 bytes con tarjetas de 80 caracteres. BINTABLE: tabla binaria.

💡 **Contexto en la clase [B40-C14](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md):**
- **Idea central (modelo mental):** Como la etiqueta de una caja: dice qué lleva dentro, en qué unidades y cómo abrirla; sin leerla el contenido se interpreta mal.
- 🎯 **Por qué importa:** Usar un producto sin leer su cabecera es una fuente clásica de errores de unidades y de orden de pixeles. La decisión central: ¿qué dice la cabecera y cómo se convierte y se compara con un modelo?
- 🔗 **Se estudia junto con:** FITS, Centinela, verosimilitud gaussiana, banda.

📘 **Dónde se aprende:** [B40-C14 · Productos de datos de Planck y misiones del CMB](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md).

### BOL

- El envejecimiento eleva `α` por radiación y contaminación. BOL y EOL son los extremos de la vida.

💡 **Cómo se explica en la clase [B85-C05](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md):**
- Los que mantienen `250–320 K` en BOL y EOL: pintura blanca.
- Para `293,15 K` al Sol se necesita `α/ε = σT⁴/S₀ = 0,3077`: entre la pintura blanca BOL (`0,222`) y la del coating a medida.
- 🎯 **Por qué importa:** Cambiar un recubrimiento es la forma más barata de mover la temperatura de una superficie decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la superficie dentro del intervalo al principio y al final de la vida?
- 🔗 **Se estudia junto con:** cociente α/ε, espejo solar óptico (OSR), envejecimiento, EOL.

📘 **Dónde se aprende:** [B85-C05 · Recubrimientos ópticos térmicos](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md).

### BP

- **Significa:** Bundle Protocol (BP).
- El Bundle Protocol (BP) crea una red de almacenamiento y reenvío con tolerancia a conectividad intermitente, retransmisión basada en custodia y reportes de estado (CCSDS 734.2-B-1).

💡 **Cómo se explica en la clase [B89-C13](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md):**
- Describir el almacenamiento y reenvío del Bundle Protocol.
- 🎯 **Por qué importa:** Sin almacenamiento y reenvío, un rover marciano no podría comunicarse con Tierra: nunca hay una ruta continua. Entender los contactos, las capacidades y el encaminamiento es la base del diseño de redes interplanetarias.
- 🔗 **Se estudia junto con:** almacenamiento y reenvío, contacto, capacidad, llegada más temprana.

📘 **Dónde se aprende:** [B89-C13 · Protocolos para espacio profundo](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md).

### BPSK

- BPSK usa 2 fases (1 bit/símbolo);

💡 **Cómo se explica en la clase [B89-C08](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md):**
- BPSK y QPSK: `Q(√(2γ))`, con `γ = Eb/N0`. 8PSK: `erfc(√(3γ) sin(π/8))/3`. 16QAM: `(3/8) erfc(√(0,4γ))` (aproximaciones con Gray, relaciones estándar no consultadas).
- A 8 dB: BPSK `1,91e-04`; 8PSK `6,18e-03`; 16QAM `9,25e-03`.
- 🎯 **Por qué importa:** La elección de la modulación fija el `Eb/N0` requerido en el presupuesto de enlace y el ancho de banda ocupado; es la base de la codificación y la sincronización siguientes. La decisión central: ¿qué modulación da la tasa que necesito con el `Eb/N0` que mi enlace puede ofrecer?
- 🔗 **Se estudia junto con:** QPSK, 8PSK, 16QAM, BER.

📘 **Dónde se aprende:** [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md).

### CA

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Los errores formales más grandes son los de `CA` y `NPAE`, que están más correlacionados con otros términos.
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?
- 🔗 **Se estudia junto con:** términos, IA, IE, NPAE.

📘 **Dónde se aprende:** [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### CAC

- El CAC es el costo de conseguirlo.
- El CAC es gasto de captación entre clientes nuevos.

💡 **Cómo se explica en la clase [B125-C02](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md):**
- Con `CAC = 6 000`: `LTV/CAC = 5,83` y el CAC se recupera en `6 000/700 = 8,6` meses.
- Calcular la recuperación del costo de adquisición y la relación `LTV/CAC`.
- 🎯 **Por qué importa:** El modelo de ingresos define cuándo entra el dinero y cuánto vale un cliente; ninguna clase anterior lo trata. La decisión central: ¿cuánto vale un cliente de suscripción, cuándo se reconoce su ingreso y cuánto abandono puede tolerar el negocio?
- 🔗 **Se estudia junto con:** suscripción, ingreso diferido, reconocimiento ratable, hito.

📘 **Dónde se aprende:** [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md); [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### CAPE

- La CAPE (energía potencial convectiva disponible) es la integral de la flotabilidad en la capa donde `T_p > T_e`.

💡 **Cómo se explica en la clase [B54-C07](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md):**
- Con exceso constante `ΔT = 2 K` sobre `T_e = 280 K` entre 2 y 10 km, `CAPE = g (ΔT/T_e) H = 9,820 × (2/280) × 8000 = 561,1429 J/kg`.
- Para el ambiente y la parcela de la sección 5, el laboratorio obtiene `CAPE = 2479,8 J/kg` y `w_max = 70,4 m/s`.
- 🎯 **Por qué importa:** La energía convectiva disponible decide si una tormenta tiene vigor o no. La pregunta motivadora: ¿cuánta velocidad puede alcanzar el aire que sube si toda la flotabilidad se convierte en movimiento?
- 🔗 **Se estudia junto con:** flotabilidad, parcela, arrastre.

📘 **Dónde se aprende:** [B54-C07 · Dinámica de tormentas](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md).

### CAVI

- El campo medio (*mean field*) exige que `q` se factorice en factores independientes, `q(θ) = Π q_i(θ_i)`. CAVI (ascenso coordenado) actualiza un factor por vez manteniendo los demás fijos.

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- CAVI converge a factores normales con media exacta y varianza `1/Λ_ii = 1 − r²`, es decir, desviación `√(1 − r²)`.
- (b) CAVI da media 0 y desviación 0,4359 = `√(1 − r²)` para `r = 0,9`; cobertura nominal 90 % → ≈ 53 %.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.
- 🔗 **Se estudia junto con:** divergencia de Kullback–Leibler, familia variacional, aproximación variacional, ELBO.

📘 **Dónde se aprende:** [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### CBE

- La CBE es la mejor estimación actual; la MEV, la masa máxima esperada, que añade el crecimiento por madurez.

💡 **Cómo se explica en la clase [B124-C19](../programa/clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md):**
- La CBE total es `355,0` kg y cada componente se infla según su madurez: 5 % heredado, 10 % modificado, 20 % nuevo diseño, 30 % nueva tecnología (ilustrativos).
- C["CBE por componente"] --> M["MEV = CBE (1 + g)"]
- 🎯 **Por qué importa:** Una propuesta pierde puntos cuando algo prometido no tiene sección que lo sostenga o cuando el presupuesto no tiene margen. La decisión central: ¿está todo lo prometido cubierto y cuánta reserva necesita el diseño para ser creíble?
- 🔗 **Se estudia junto con:** trazabilidad, cobertura, sección huérfana, MEV.

📘 **Dónde se aprende:** [B124-C19 · Redacción de propuesta de misión](../programa/clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md).

### CCB

- Una solicitud de cambio (CR) propone un cambio; la CCB la decide tras un análisis de impacto.

💡 **Cómo se explica en la clase [B83-C15](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md):**
- Con las dependencias (ICD y plan de ensayos dependen de los requisitos, el software depende del ICD, el presupuesto de masa depende de la estructura y los requisitos), CR-01 afecta a 4 elementos: clase I, va a la CCB.
- CR-02 afecta a 1 elemento: clase II, puede resolverse con aprobación del responsable y aviso a la CCB.
- 🎯 **Por qué importa:** Si nadie sabe qué versión de qué documento se ensayó, no se puede demostrar nada. La decisión central: ¿la configuración actual es la aprobada, y qué se afecta si apruebo este cambio?
- 🔗 **Se estudia junto con:** elemento de configuración, línea base, huella, deriva.

📘 **Dónde se aprende:** [B83-C15 · Gestión de configuración](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md).

### CCM

- El rizado es la variación pico a pico en un periodo. CCM es la conducción continua y DCM la discontinua.

💡 **Cómo se explica en la clase [B86-C08](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md):**
- En CCM ideal `D = V_o/V_in = 5/28 = 0,1786`.
- La inductancia crítica es `5,04 µH`, menor que `22 µH`: el convertidor opera en CCM.
- ⚠️ **Error frecuente:** Ignorar CCM/DCM. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un convertidor que reduce la tensión con un interruptor y una bobina puede ser mucho más eficiente que un regulador lineal, pero introduce rizado, ruido y pérdidas de conmutación que hay que dimensionar. La decisión central: ¿qué ciclo de trabajo, bobina y condensador dan `5 V` desde `28 V` con rizado y eficiencia aceptables?
- 🔗 **Se estudia junto con:** ciclo de trabajo, rizado, DCM, inductancia crítica.

📘 **Dónde se aprende:** [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### CDMS

- Un banco de datos espectroscópicos reúne frecuencias, intensidades y niveles con procedencia. CDMS (Cologne Database for Molecular Spectroscopy) y JPL son catálogos de líneas milimétricas y submilimétricas.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- L["datos de laboratorio"] --> J["JPL / CDMS: FREQ, ERR, LGINT, ELO, GUP"]
- Describir qué contiene y para qué sirve cada banco (CDMS, JPL, HITRAN, LAMDA).
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.
- 🔗 **Se estudia junto con:** banco de datos espectroscópicos, JPL, HITRAN, LAMDA.

📘 **Dónde se aprende:** [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### CDR

- La CDR revisa que el diseño esté completo (planos, análisis, compras).

💡 **Cómo se explica en la clase [B83-C14](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md):**
- Solo 2 de 3 criterios de CDR del ejemplo se cumplen.
- La evidencia es la informe de preparación de CDR/TRR y nivel de ensayo del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un ensayo mal preparado destruye hardware o no demuestra nada. La decisión central: ¿cada requisito tiene un método asignado, y cada ensayo está listo (procedimiento, equipo, configuración, personal e instalación) y con un nivel de carga definido?
- 🔗 **Se estudia junto con:** matriz de verificación, TRR, vibración aleatoria, Grms.

📘 **Dónde se aprende:** [B83-C14 · Revisiones CDR y TRR](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md).

### CDS

- El CDS resta la lectura del reinicio de la lectura de señal.

💡 **Cómo se explica en la clase [B44-C03](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md):**
- Sin CDS el ruido es `40,24 e⁻` (esperado `40,22`); con CDS, `2,85 e⁻` (esperado `√2 × 2 = 2,83`).
- El CDS lo elimina pero suma la lectura dos veces (`√2`).
- ⚠️ **Error frecuente:** Pensar que el CDS elimina todo el ruido. Se corrige con 8.2.
- 🎯 **Por qué importa:** El diseño CMOS cambia el ruido y la geometría de la lectura. La decisión central: ¿qué ruido elimina el CDS y qué artefacto introduce el obturador rodante?
- 🔗 **Se estudia junto con:** ruido kTC, obturador rodante, lectura por columna.

📘 **Dónde se aprende:** [B44-C03 · Sensores CMOS](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md).

### CE90

- El CE90 contiene el 90 % de los errores radiales.

💡 **Cómo se explica en la clase [B53-C19](../programa/clases/B53/B53-C19-incertidumbre-en-mapas-planetarios/CLASE.md):**
- El valor `2,146` del CE90 es el de un error circular gaussiano.
- Analogía: tirar dardos con manos temblorosas: el error se compone de varios temblores, y el círculo que contiene nueve de cada diez dardos es el CE90.
- 🎯 **Por qué importa:** Un contorno sin barras de error afirma más de lo que sabe. La decisión central: ¿con qué incertidumbre se conoce una posición y un área en un mapa, y cuándo falla la propagación lineal?
- 🔗 **Se estudia junto con:** error de posición, propagación lineal, sesgo por no linealidad.

📘 **Dónde se aprende:** [B53-C19 · Incertidumbre en mapas planetarios](../programa/clases/B53/B53-C19-incertidumbre-en-mapas-planetarios/CLASE.md).

### CEP

- El CEP es el radio del círculo horizontal con 50 % de probabilidad; el SEP, de la esfera con 50 %.

💡 **Cómo se explica en la clase [B74-C19](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md):**
- Con `σ = (3; 1,2; 2) m`: RMS 3D `3,8000 m` (muestral `3,8012 m`), percentil 95 de la norma 3D `6,493 m`, SEP (50 %) `3,190 m`, CEP (50 %, horizontal) `2,425 m`.
- Con `N = 50`, el RMS 3D es `3,816 ± 0,245 m`, el percentil 95 `6,316 ± 0,634 m` y el CEP `2,457 ± 0,264 m`.
- ⚠️ **Error frecuente:** Comparar un CEP con un 95 %. Son probabilidades distintas; ver 8.1.
- 🎯 **Por qué importa:** Dos informes pueden decir «3 m» y referirse a cosas distintas (RMS, 50 %, 95 %). La decisión central: ¿qué métrica comunica el riesgo que importa, con qué probabilidad y con qué incertidumbre muestral?
- 🔗 **Se estudia junto con:** RMS 3D, SEP, 2DRMS, percentil.

📘 **Dónde se aprende:** [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md).

### CER

- **Significa:** relación de estimación de costo (CER).
- Una relación de estimación de costo (CER) es una ecuación que da el costo en función de un atributo.

💡 **Cómo se explica en la clase [B124-C05](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md):**
- El NASA Cost Estimating Handbook v4.0 (febrero de 2015) es la guía de la agencia para estimar costos; su apéndice E menciona relaciones de estimación de costo (CER) y reportes de curvas de aprendizaje, y su glosario dice que, en la teoría de la curva de aprendizaje, la primera unidad es la más cara.
- 🎯 **Por qué importa:** Un costo sin banda de incertidumbre parece más preciso de lo que es. La decisión central: ¿cuánto cuesta esta misión, con qué banda y cuánto baja el costo unitario si se fabrican varias unidades?
- 🔗 **Se estudia junto con:** escala log-log, SEE, intervalo de predicción, curva de aprendizaje.

📘 **Dónde se aprende:** [B124-C05 · Estimación de costos de misión](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md).

### CG

- **Significa:** Centro de masa (CG).
- Margen de separación: margen de que la unión no se abra. Centro de masa (CG): punto promedio de la masa.

💡 **Cómo se explica en la clase [B90-C06](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md):**
- Un CubeSat 3U de siete piezas suma 3,25 kg, con centro de masa en (1,85; −1,11; 22,92) mm, dentro de los límites de ±20, ±20 y ±70 mm.
- Calcular el centro de masa y el tensor de inercia de un ensamble por ejes paralelos.
- 🎯 **Por qué importa:** Un perno mal apretado se afloja con la vibración o se rompe por exceso de carga; un centro de masa fuera de rango desvía la nave en el despliegue. La decisión central: ¿qué par de apriete garantiza que la unión no se separe ni se plastifique, y el conjunto queda dentro de los límites de masa?
- 🔗 **Se estudia junto con:** Precarga, Coeficiente de par K, Factor de carga φ, Margen de separación.

📘 **Dónde se aprende:** [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md).

### CHNOPS

- Los elementos CHNOPS (carbono, hidrógeno, nitrógeno, oxígeno, fósforo, azufre) forman la mayor parte de la materia viva conocida.

💡 **Cómo se explica en la clase [B56-C02](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md):**
- Ejercicio 8. Balancea `N₂ + 3 H₂ → 2 NH₃` y di qué elementos de CHNOPS intervienen.
- Ejercicio 10 · transferencia. ¿Por qué la química de CHNOPS no demuestra que toda vida use esos elementos?
- ⚠️ **Error frecuente:** Generalizar CHNOPS a toda la vida posible. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Para buscar vida hay que saber qué hace la vida conocida con la materia: qué elementos usa y de dónde saca energía. La decisión central: dada una reacción metabólica, ¿está balanceada y cuánta energía libre libera o consume por mol?
- 🔗 **Se estudia junto con:** metabolismo, energía libre de Gibbs, energía libre de formación estándar, balance atómico.

📘 **Dónde se aprende:** [B56-C02 · Bioquímica y metabolismo terrestre](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md).

### CI

- Una condrita es un meteorito formado por materiales que no se fundieron del todo; las condritas carbonáceas son ricas en carbono, y las CI son las más primitivas en cuanto a su composición.

💡 **Cómo se explica en la clase [B06-C20](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md):**
- Las CI son las que menos se han modificado, aunque sufrieron alteración por agua y calentamiento, y se les considera una buena aproximación al material no volátil del que se formó el Sistema Solar (S1).
- No se puede concluir que Bennu sea «más rico en carbono que las CI» con tanta seguridad: la comparación mezcla un valor medido en porciones de una muestra (S2) con un cálculo propio a partir de abundancias promedio (S1), con omisiones y sin incertidumbre propagada.
- ⚠️ **Error frecuente:** Tratar la «CI media» como un dato medido. Se corrige con la sección 8.4 y el ejercicio 9.
- 🎯 **Por qué importa:** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.
- 🔗 **Se estudia junto con:** meteorito, condrita, condritas carbonáceas, dex.

📘 **Dónde se aprende:** [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### CIP

- El CIP es el polo de referencia que separa el movimiento del eje en precesión-nutación y en movimiento polar (S1, glosario).

💡 **Contexto en la clase [B13-C22](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md):**
- **Idea central (modelo mental):** Piensa en tres engranajes encadenados: el primero (`W`) mueve el eje dentro de la Tierra, el segundo (`R`) gira la Tierra alrededor de ese eje, el tercero (`Q`) mueve el eje respecto de las estrellas. El orden importa; cada engranaje tiene su propia incertidumbre y su propio periodo.
- 🎯 **Por qué importa:** Una estación terrestre apunta a una nave en el sistema celeste. Para ello debe saber cuánto ha girado la Tierra, hacia dónde apunta su eje en el cielo y dónde está ese eje dentro de la corteza.
- 🔗 **Se estudia junto con:** parámetros de orientación terrestre (EOP), movimiento polar, UT1 − UTC, precesión-nutación.

📘 **Dónde se aprende:** [B13-C22 · Parámetros de orientación terrestre: precesión, nutación, UT1 y movimiento polar](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md).

### CK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- Por tipo: SPK, CK, PCK, IK, FK, LSK, SCLK.
- Un CK (actitud de la nave) junto con IK y FK.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, PCK, IK.

📘 **Dónde se aprende:** [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### CLEAN

- El CLEAN de Högbom resta el haz sucio desplazado, con ganancia, en el pico del residuo.
- La imagen sucia y el haz sucio. CLEAN (Högbom): resta iterativa de componentes puntuales.

💡 **Cómo se explica en la clase [B46-C19](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md):**
- CLEAN supone fuentes puntuales; las extensas requieren escalas múltiples.
- B["haz sucio"] --> L["CLEAN: pico y resta"]
- 🎯 **Por qué importa:** La imagen sucia no se puede interpretar por los lóbulos del haz. La decisión central: ¿cuándo detener la deconvolución para no ajustar ruido?
- 🔗 **Se estudia junto con:** imagen sucia, componente CLEAN, ganancia del lazo, residuo.

📘 **Dónde se aprende:** [B46-C19 · Imágenes de radio y CLEAN](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md); [B51-C06 · Autocalibración iterativa con modelo de cielo](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md).

### CMB

- **Significa:** fondo cósmico de microondas (CMB).
- El fondo cósmico de microondas (CMB) es la radiación térmica relicta.

💡 **Contexto en la clase [B26-C15](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md):**
- **Idea central (modelo mental):** El universo temprano fue un horno en equilibrio térmico. Cuando se enfrió y se hizo transparente, la radiación quedó con la forma del cuerpo negro y desde entonces solo cambia su temperatura.
- 🎯 **Por qué importa:** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.
- 🔗 **Se estudia junto con:** función de Planck, densidad numérica de fotones, frecuencia del máximo, energía media.

📘 **Dónde se aprende:** [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### CNR

- La CNR (relación contraste-ruido) es `contraste × SNR × MTF`.

💡 **Cómo se explica en la clase [B83-C17](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md):**
- La CNR es `0,08 × SNR × 0,614`; con SNR de 105 (albedo 0,3) da 5,15, apenas sobre el umbral 5, y con albedo 0,05 (costa oscura) la SNR baja a `105·√(0,05/0,3)` y la CNR a 2,10: no se detecta.
- Paso 3 · CNR. `0,08 × 42,9 × 0,614 = 2,10`.
- 🎯 **Por qué importa:** Un proyecto puede pasar todas las pruebas de requisitos y fracasar en el uso. La decisión central: ¿además de cumplir los requisitos, el sistema satisface la necesidad en las condiciones reales de uso?
- 🔗 **Se estudia junto con:** Verificación, Validación, MTF, umbral de detección.

📘 **Dónde se aprende:** [B83-C17 · Verificación frente a validación](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md).

### CONOPS

- **Significa:** ConOps.
- Un CONOPS describe fases, modos, actores y escenarios de operación.
- ConOps: descripción de cómo se opera la misión.

💡 **Cómo se explica en la clase [B83-C03](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md):**
- El CONOPS de ejemplo tiene cuatro fases: lanzamiento y primeras órbitas (7 d), puesta en servicio (30 d), operaciones nominales (3 años) y fin de vida (90 d).
- *Descripción textual:* las fases y modos del CONOPS definen la órbita y la estación; la simulación de visibilidad da pases, duraciones y huecos, de los que sale el tiempo de enlace diario; la cota analítica del pase cenital sirve de comprobación.
- ⚠️ **Error frecuente:** Escribir un CONOPS sin números. Añade pases, huecos y latencias
- 🎯 **Por qué importa:** Los requisitos de datos, energía y operaciones dependen de cuántas veces al día se puede hablar con el satélite y por cuánto tiempo. La decisión central: ¿cuánto contacto real ofrece la órbita y cómo se reparte en las fases de la misión?
- 🔗 **Se estudia junto con:** fases, modo, pase, hueco.

📘 **Dónde se aprende:** [B83-C03 · Concepto de operaciones CONOPS](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md); [B96-C02 · Concepto de operaciones de misión](../programa/clases/B96/B96-C02-concepto-de-operaciones-de-mision/CLASE.md).

### COPUOS

- COPUOS es la Comisión sobre la Utilización del Espacio Ultraterrestre con Fines Pacíficos.

💡 **Cómo se explica en la clase [B119-C06](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md):**
- *Descripción textual:* la Asamblea crea COPUOS; este tiene dos subcomités y una secretaría; decide por consenso, lo que da poder de bloqueo a cada miembro.
- Según el resumen de búsqueda de las páginas de UNOOSA (2026-11-11), la Asamblea General creó COPUOS como órgano ad hoc con 18 miembros por la res. 1348 (XIII) del 13-12-1958 y lo hizo permanente por la res. 1472 (XIV) del 12-12-1959; tiene un Subcomité Científico y Técnico y un Subcomité Jurídico, y UNOOSA es su secretaría.
- ⚠️ **Error frecuente:** Atribuir la decisión a UNOOSA y no a COPUOS. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** Quien estudia el derecho espacial necesita saber dónde se negocia y cómo se decide; ninguna clase anterior trata los organismos. La decisión central: ¿cómo cambia la probabilidad de bloqueo cuando crece el número de miembros que deben consentir?
- 🔗 **Se estudia junto con:** UNOOSA, consenso, Bloqueo.

📘 **Dónde se aprende:** [B119-C06 · Organismos UNOOSA y COPUOS](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md).

### COTS

- El COTS (*commercial off-the-shelf*) es un componente comercial no diseñado para el espacio.

💡 **Contexto en la clase [B95-C02](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md):**
- 🎯 **Por qué importa:** Un componente comercial puede funcionar bien en tierra y degradarse o fallar en órbita. La decisión central: ¿qué componente comercial se puede usar en esta misión, con qué margen de radiación y con qué fiabilidad del conjunto?
- 🔗 **Se estudia junto con:** TID, SEU, SEL, RDM.

📘 **Dónde se aprende:** [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### CPI

- El CPI es `EV/AC`; el SPI, `EV/PV`.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- `CPI = 0,7950` (se gasta más de lo que se gana) y `SPI = 0,8368` (hay atraso).
- Si el rendimiento de costo se mantiene, `EAC = BAC/CPI = 100,63` Mum (ETC `40,63`, VAC `-20,63`), idéntico a `AC + (BAC − EV)/CPI` (error `0,0e+00`).
- ⚠️ **Error frecuente:** Confundir gastar con avanzar. Se corrige con 8.2: el CPI compara lo ganado con lo gastado.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, EV, AC.

📘 **Dónde se aprende:** [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### CPIF

- **Significa:** Costo más incentivo (CPIF).
- Precio fijo (FFP): el pago no depende del costo real. Costo más incentivo (CPIF): se paga el costo real más un honorario que baja cuando el costo supera el objetivo.

💡 **Cómo se explica en la clase [B124-C10](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md):**
- Ninguno es mejor en sí: depende de qué tan bien se conoce el costo, y el modelo no incluye incentivos a ocultar costos ni renegociaciones.
- Describir un contrato de precio fijo y uno de costo más honorario con incentivo.
- 🎯 **Por qué importa:** El tipo de contrato reparte el riesgo de sobrecosto entre quien compra y quien vende. La decisión central: ¿cuánto riesgo asume cada parte con cada tipo de contrato y cuánto cuesta ese reparto en promedio?
- 🔗 **Se estudia junto con:** Precio fijo (FFP), honorario objetivo, razón de reparto, techo.

📘 **Dónde se aprende:** [B124-C10 · Contratos y compras espaciales](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md).

### CR3BP

- El CR3BP estudia una masa despreciable bajo la gravedad de dos cuerpos masivos en órbita circular mutua.

💡 **Cómo se explica en la clase [B73-C01](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md):**
- Escribir las ecuaciones del CR3BP adimensional con el parámetro de masa `μ`.
- La evidencia es la ficha del CR3BP Tierra–Luna con control de conservación del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Con tres cuerpos no hay solución cerrada, pero sí una cantidad conservada que organiza todo lo demás: puntos de equilibrio, regiones prohibidas y transferencias de bajo costo. La decisión central: ¿cuándo basta el modelo de tres cuerpos restringido, y cómo sé que mi integración no inventa dinámica?
- 🔗 **Se estudia junto con:** parámetro de masa, marco sinódico, constante de Jacobi, unidades adimensionales.

📘 **Dónde se aprende:** [B73-C01 · Problema restringido de tres cuerpos](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md).

### CRC

- Prueba de extremo a extremo: prueba de un hilo operativo completo entre elementos e interfaces externas. CRC: código de redundancia cíclica.

💡 **Cómo se explica en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- CCSDS publica protocolos de datos espaciales, pero sus recomendaciones no se consultaron; el CRC-16/CCITT-FALSE (polinomio 0x1021, valor inicial 0xFFFF) y su valor de comprobación 0x29B1 son datos de uso general no consultados en una fuente concreta.
- El laboratorio calcula `CRC("123456789") = 0x29B1`, igual al valor de comprobación.
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?
- 🔗 **Se estudia junto con:** Prueba de extremo a extremo, BER, FER, Ráfaga.

📘 **Dónde se aprende:** [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### CRC-15

- El CRC-15 usa el polinomio `0x4599`.

💡 **Cómo se explica en la clase [B88-C07](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md):**
- Implementar el CRC-15 del CAN y el relleno.
- Ejercicio 10 · transferencia. Transferencia. ¿Qué cambia si el CRC-15 se calcula con un polinomio distinto?
- 🎯 **Por qué importa:** El bus fija cuánta telemetría y cuántos comandos caben y con qué retardo. La decisión central: ¿cuál es el caudal útil y el peor tiempo de trama de cada bus para mi carga?
- 🔗 **Se estudia junto con:** trama CAN 2.0A, relleno de bits, carácter de datos.

📘 **Dónde se aprende:** [B88-C07 · Buses I2C SPI CAN y SpaceWire](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md).

### CRC-16

- El CRC-16 con polinomio `0x1021` e inicio `0xFFFF` da `0x29B1` para la cadena `123456789`.
- El CRC-16 valida el registro.
- El CRC-16 usa el polinomio `x¹⁶ + x¹² + x⁵ + 1` (0x1021).

💡 **Cómo se explica en la clase [B88-C08](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md):**
- El CRC-16 de `123456789` es `0x29B1` (valor de comprobación del propio laboratorio).
- Con CRC-16, un error de un byte (ráfaga ≤ 16 bits) siempre se detecta; esto lo comprueba el laboratorio, no una norma.
- 🎯 **Por qué importa:** Sin telemetría no se ve la salud de la nave; con demasiada, se satura el enlace. La decisión central: ¿qué parámetros, a qué frecuencia y con qué protección caben en el enlace sin perder los críticos?
- 🔗 **Se estudia junto con:** sincronía, volumen, ocupación, perfil.

📘 **Dónde se aprende:** [B88-C08 · Telemetría interna](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md); [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md); [B89-C12 · Telecomandos CCSDS](../programa/clases/B89/B89-C12-telecomandos-ccsds/CLASE.md).

### CRC-32

- SHA-256: hash criptográfico de 256 bits. CRC-32: código cíclico de 32 bits.

💡 **Cómo se explica en la clase [B48-C17](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md):**
- El CRC-32 detecta con seguridad cualquier cambio de un bit, pero no protege de una alteración deliberada; para eso se usa SHA-256.
- El SHA-256 de «abc» es ba7816bf8f01cfea…, y el CRC-32 de «123456789» es 0xcbf43926.
- 🎯 **Por qué importa:** Un archivo que se corrompe en silencio contamina todos los análisis posteriores. La decisión central: ¿qué suma de verificación y con cuántos bits detecta la corrupción?
- 🔗 **Se estudia junto con:** Suma de verificación, SHA-256, Colisión, Problema del cumpleaños.

📘 **Dónde se aprende:** [B48-C17 · Gestión de archivos observacionales](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md).

### CRC-8

- El CRC-8 con polinomio `0x07` da `0xF4` para `123456789`.

💡 **Cómo se explica en la clase [B88-C09](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md):**
- Ejercicio 6 · autónomo. Calcula el CRC-8 de un solo byte `0x00` con polinomio `0x07`.
- El script [telecomandos_modos.py](telecomandos_modos.py) imprime la matriz estado–comando, ejecuta un guion de nueve telecomandos con CRC y secuencia y comprueba 11 celdas aceptadas, el modo final `SAFE` y el CRC-8 de prueba `0xF4`.
- 🎯 **Por qué importa:** Un telecomando aceptado en el estado equivocado puede dañar la nave; uno rechazado en el estado correcto puede perderla. La decisión central: ¿qué comando es válido en cada modo y qué comprobaciones lo protegen?
- 🔗 **Se estudia junto con:** modo, transición, matriz estado–comando, contador de secuencia.

📘 **Dónde se aprende:** [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md).

### CSI

- El POD es la fracción de eventos detectados, el FAR la de alertas falsas y el CSI la de aciertos sobre todos los casos relevantes.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- Calcular POD, FAR, CSI y la puntuación de Heidke por dos fórmulas.
- El script [alerta.py](alerta.py) clasifica un año sintético, arma la tabla de contingencia y calcula POD, FAR, CSI y Heidke por dos fórmulas (comprueba que las dos fórmulas de Heidke coinciden a `10⁻¹²`).
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?
- 🔗 **Se estudia junto con:** escala, acierto, falsa alarma, fallo.

📘 **Dónde se aprende:** [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md).

### CSTR

- **Significa:** Mezcla completa (CSTR).
- Biorreactor: tanque con microorganismos que consumen materia orgánica. Mezcla completa (CSTR): tanque uniforme.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- Cuatro personas con 20 L/día de agua gris (80 L/día) y DBO de 300 mg/L, con `k = 0,5 h⁻¹` (ilustrativo): una remoción del 90 % exige en mezcla completa `τ = 18,0 h` y 60 L; en flujo pistón, 4,6 h y 15 L; con 3 tanques, 6,9 h y 23 L.
- Para el 99 % la mezcla completa necesita 660 L y 3 tanques solo 73 L.
- ⚠️ **Error frecuente:** Dimensionar con la mezcla completa sin considerar etapas. Compara (8.2).
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?
- 🔗 **Se estudia junto con:** Aguas grises, Biorreactor, Flujo pistón (PFR), Chick–Watson.

📘 **Dónde se aprende:** [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### CSV

- Un archivo CSV (*comma-separated values*) guarda una tabla como líneas de texto con campos separados por un delimitador, normalmente la coma.

💡 **Cómo se explica en la clase [B07-C08](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md):**
- Un CSV sin procedencia no es un dato científico.
- Para `planetas_nssdc.csv` se declara en la cabecera del script y en la sección 11: quién publicó cada valor (NASA NSSDC), qué páginas, cuándo se consultaron y cuáles valores están redondeados (la densidad y la gravedad vienen de la tabla comparativa, con precisión menor).
- 🎯 **Por qué importa:** Un archivo CSV parece trivial y por eso engaña: todo se lee como texto, un decimal con coma rompe una columna, una línea vacía pasa inadvertida, y una codificación equivocada convierte «Júpiter» en símbolos raros. Un análisis hecho sobre datos mal leídos puede ser plausible y erróneo a la vez.
- 🔗 **Se estudia junto con:** delimitador, encabezado, entre comillas, codificación.

📘 **Dónde se aprende:** [B07-C08 · Lectura de archivos CSV](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md).

### CT

- Chick–Watson: inactivación proporcional a `C·t`. CT: concentración por tiempo.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- Una desinfección de 4 log exige `CT = 8 mg·min/L`.
- Ejercicio 6 · autónomo. ¿Qué `CT` da 3 log?
- ⚠️ **Error frecuente:** Olvidar la desinfección. Añade CT (8.3).
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?
- 🔗 **Se estudia junto con:** Aguas grises, Biorreactor, Mezcla completa (CSTR), Flujo pistón (PFR).

📘 **Dónde se aprende:** [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### CTE

- La CTE es la fracción de carga que pasa de un píxel al siguiente.

💡 **Cómo se explica en la clase [B44-C02](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md):**
- Con `1000 e⁻`, `CTE = 0,9999` y `400` transferencias, el valor analítico es `960,79 e⁻` y el simulado (300 repeticiones, semilla 20261109) `960,75 e⁻`, con error estándar de la media `0,35 e⁻`.
- *Descripción textual:* la carga inicial atraviesa `n` transferencias; la fracción restante es `CTE^n` y la simulación lo confirma.
- ⚠️ **Error frecuente:** Creer que la CTE es irrelevante por ser casi 1. Se corrige con 8.4.
- 🎯 **Por qué importa:** Cada transferencia pierde una pequeña fracción de carga, y un píxel lejano se transfiere miles de veces. La decisión central: ¿qué CTE hace aceptable un sensor de 2048 × 2048?
- 🔗 **Se estudia junto con:** ineficiencia, registro de salida, transferencia.

📘 **Dónde se aprende:** [B44-C02 · Sensores CCD](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md).

### CUSUM

- El CUSUM inferior es `S_t = máx(0, S_{t−1} − z_t − k)` con alarma si `S_t > h` (`k = 0,5`).
- Puntuación robusta: desvío en unidades de MAD. CUSUM: suma acumulada de desvíos.
- El CUSUM acumula `(μ₀ − x)/σ − k` y se reinicia en 0.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B96-C13](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md):**
- (3) CUSUM: `S = max(0, S + (x − μ)/σ − 0,5)` y alarma si `S > 5`, con reinicio.
- CUSUM acumula el exceso y detecta la deriva en 7 muestras, a costa de falsas alarmas y de necesitar μ y σ de referencia.
- 🎯 **Por qué importa:** Un detector que no ve una deriva lenta avisa cuando ya es tarde, y uno que alarma por todo se ignora. La decisión central: ¿qué detector ve cada tipo de anomalía, con qué retraso y a qué costo en falsas alarmas?
- 🔗 **Se estudia junto con:** Anomalía, Límite fijo, Puntuación robusta, Falsa alarma.

📘 **Dónde se aprende:** [B96-C13 · Detección de anomalías](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md); [B97-C22 · Detección autónoma de eventos científicos](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md); [B104-C18 · Aislamiento y convivencia](../programa/clases/B104/B104-C18-aislamiento-y-convivencia/CLASE.md); [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md); [B107-C10 · Indicadores de rehabilitación y seguimiento](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md).

### CVCM

- **Significa:** volátiles condensables (CVCM).
- RML `= TML − WVR`; CVCM (*collected volatile condensable material*) es la masa condensada en el colector, en % de la masa inicial.
- La masa perdida total (TML) y los volátiles condensables (CVCM) miden la desgasificación de un material.
- TML: pérdida total de masa, `100 (mᵢ − m_f)/mᵢ`. CVCM: volátiles condensables recogidos, `100 m_col/mᵢ`.

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- La silicona B pasa en `TML` y falla en `CVCM`: por eso se exigen ambos criterios.
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?
- 🔗 **Se estudia junto con:** TML, WVR, RML, bakeout.

📘 **Dónde se aprende:** [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md); [B85-C12 · Entorno de vacío](../programa/clases/B85/B85-C12-entorno-de-vacio/CLASE.md); [B90-C04 · Control de contaminación](../programa/clases/B90/B90-C04-control-de-contaminacion/CLASE.md).

### CW

- **Significa:** ecuaciones de Clohessy–Wiltshire (CW).
- Las ecuaciones de Clohessy–Wiltshire (CW) lo describen linealizado alrededor de una órbita circular.

💡 **Contexto en la clase [B97-C11](../programa/clases/B97/B97-C11-robots-de-inspeccion-orbital/CLASE.md):**
- 🎯 **Por qué importa:** Una inspección segura se diseña de modo que, si falla el empuje, el robot no se acerque ni se aleje: la elipse sin deriva lo garantiza. Con una condición inicial mal elegida, el robot se aleja decenas de veces la distancia deseada en una órbita.
- 🔗 **Se estudia junto con:** movimiento relativo, condición sin deriva, sistema local (LVLH), órbita de inspección.

📘 **Dónde se aprende:** [B97-C11 · Robots de inspección orbital](../programa/clases/B97/B97-C11-robots-de-inspeccion-orbital/CLASE.md).

### D10

- La D10 es la dosis con `S = 0,1`.

💡 **Cómo se explica en la clase [B64-C01](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md):**
- La D10 sintética es de 332,6 Gy para el sensible y de 10 434 Gy para el tolerante, un cociente de 31,4.
- En la D10 el sensible tiene 5,3 DSB de media y el tolerante 166,9: la D10 corresponde a una media de roturas mayor que la capacidad de reparación porque la distribución de Poisson tiene dispersión.
- ⚠️ **Error frecuente:** Usar la media como umbral. La D10 corresponde a más DSB que la capacidad por la dispersión de Poisson (sección 8.3).
- 🎯 **Por qué importa:** La radiación ionizante rompe el ADN, y una célula muere cuando el daño supera su capacidad de reparación. La pregunta motivadora: ¿por qué dos organismos con el mismo daño inicial por gray sobreviven a dosis tan distintas?
- 🔗 **Se estudia junto con:** dosis absorbida, rotura de doble cadena (DSB), rendimiento, capacidad de reparación.

📘 **Dónde se aprende:** [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md).

### DAG

- **Significa:** grafo acíclico dirigido (DAG).
- Un grafo acíclico dirigido (DAG) representa las dependencias sin ciclos.

💡 **Contexto en la clase [B14-C30](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md):**
- **Idea central (modelo mental):** Cada etapa recibe un dato con su huella, calcula la clave del resultado, y si ya existe lo reutiliza; si no, lo calcula, y si falla lo reintenta; si el control de calidad lo rechaza, detiene el lote. Todo queda en un registro.
- 🎯 **Por qué importa:** Cada madrugada llegan datos nuevos. Si un humano debe lanzar cada paso, tarde o temprano se olvida uno; si un lote corrupto atraviesa la cadena, contamina el producto final; si un fallo de red detiene todo y al reiniciar se repite desde cero, se pierde tiempo.
- 🔗 **Se estudia junto con:** cadena, orden topológico, idempotencia, lote.

📘 **Dónde se aprende:** [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md).

### DCL

- **Significa:** diagrama de cuerpo libre (DCL).
- Un diagrama de cuerpo libre (DCL) es un esquema que muestra un cuerpo aislado y todas las fuerzas externas que actúan sobre él, como flechas desde el cuerpo.

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- Dibujar un diagrama de cuerpo libre con ejes y ángulos declarados.
- python programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/equilibrio_de_fuerzas.py
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?
- 🔗 **Se estudia junto con:** peso, normal, tensión, empuje.

📘 **Dónde se aprende:** [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md).

### DCM

- CCM es la conducción continua y DCM la discontinua.

💡 **Cómo se explica en la clase [B86-C08](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md):**
- Inductancia critica CCM/DCM = 5.04 uH (L = 22 uH: conduccion continua)
- ⚠️ **Error frecuente:** Ignorar CCM/DCM. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un convertidor que reduce la tensión con un interruptor y una bobina puede ser mucho más eficiente que un regulador lineal, pero introduce rizado, ruido y pérdidas de conmutación que hay que dimensionar. La decisión central: ¿qué ciclo de trabajo, bobina y condensador dan `5 V` desde `28 V` con rizado y eficiencia aceptables?
- 🔗 **Se estudia junto con:** ciclo de trabajo, rizado, CCM, inductancia crítica.

📘 **Dónde se aprende:** [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### DDOR

- El DDOR resta los retardos de una señal de la nave y de un cuásar medidos en dos estaciones lejanas; da un ángulo con precisión `cσ_τ/B`.

💡 **Cómo se explica en la clase [B74-C17](../programa/clases/B74/B74-C17-navegacion-en-espacio-profundo/CLASE.md):**
- Al sumar la información del DDOR en la dirección de la declinación, la incertidumbre combinada es `3,75 nrad` a 0° (frente a la ausencia de información del Doppler), y `3,68 nrad` a 60°.
- *Descripción textual:* el Doppler de una estación rotante da información sobre la ascensión recta y, según la declinación, sobre la declinación; el DDOR añade un ángulo; ambas informaciones se suman y dan la covarianza angular.
- 🎯 **Por qué importa:** El Doppler apenas distingue la declinación cuando la nave está cerca del ecuador celeste: la firma de la rotación terrestre depende de `sin δ`. La decisión central: ¿qué observable cubre la dirección que los demás no ven?
- 🔗 **Se estudia junto con:** velocidad de alcance por rotación terrestre, ambigüedad de declinación, información de Fisher.

📘 **Dónde se aprende:** [B74-C17 · Navegación en espacio profundo](../programa/clases/B74/B74-C17-navegacion-en-espacio-profundo/CLASE.md).

### DDREF

- El DDREF (factor de efectividad de dosis y tasa de dosis) divide el riesgo de dosis altas y tasas altas para obtener el de dosis bajas;

💡 **Cómo se explica en la clase [B112-C04](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md):**
- ICRP 103 mantiene la hipótesis de respuesta lineal a dosis bajas para cáncer y efectos hereditables y estima un detrimento nominal de alrededor del 5 % por Sv, con un DDREF de 2 para cánceres sólidos (extracto consultado).
- Cucinotta, Kim y Ren (NASA NTRS) señalan que las incertidumbres provienen de los coeficientes epidemiológicos, el DDREF, los factores de calidad y la física del campo y que el cociente entre el nivel del 95 % y la estimación puntual es de unas 4 veces para misiones lunares y a Marte.
- 🎯 **Por qué importa:** Ninguna clase cubre riesgo de cáncer y efectos tardíos. Los límites de carrera de una misión se expresan como riesgo, no como umbral, y sin entender cómo se estima y cuán incierta es esa estimación, un límite en mSv parece más preciso de lo que es.
- 🔗 **Se estudia junto con:** modelo lineal sin umbral, riesgo de exceso, detrimento, efecto estocástico.

📘 **Dónde se aprende:** [B112-C04 · Efectos crónicos y carcinogénesis por radiación](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md).

### DFT

- **Significa:** transformada discreta de Fourier (DFT).
- La transformada discreta de Fourier (DFT) de `N` muestras es `X[k] = Σ_{n=0}^{N−1} x[n] e^{−2π i k n/N}`, para `k = 0, …, N − 1`; es la convención usada en NumPy y en esta clase.
- La DFT es la transformada de Fourier discreta.

💡 **Cómo se explica en la clase [B15-C04](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md):**
- Definir la transformada discreta de Fourier (DFT) y calcular una de 4 muestras a mano.
- 🎯 **Por qué importa:** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.
- 🔗 **Se estudia junto con:** número complejo, módulo, fórmula de Euler, transformada de Fourier continua.

📘 **Dónde se aprende:** [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md); [B31-C04 · Principio de incertidumbre](../programa/clases/B31/B31-C04-principio-de-incertidumbre/CLASE.md).

### DIET

- La DIET (desorción inducida por transiciones electrónicas) es el mecanismo en que la excitación electrónica de una molécula de la superficie provoca su salida;

💡 **Contexto en la clase [B68-C02](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md):**
- **Idea central (modelo mental):** Piensa en una lluvia de granizo (fotones) sobre una superficie de arena (hielo): cada impacto lanza algunos granos fuera (desorción), y los impactos más profundos rompen granos sin lanzarlos (fotólisis). Pocas veces el granizo lanza algo, pero la lluvia es larga.
- 🎯 **Por qué importa:** Si un hielo de CO a 15 K es estable térmicamente durante millones de años, la presencia de CO gaseoso en regiones frías exige otro mecanismo. La decisión central: ¿cuántas moléculas expulsa cada fotón y de qué depende ese número?
- 🔗 **Se estudia junto con:** fotodesorción, rendimiento, fluencia, fotólisis.

📘 **Dónde se aprende:** [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md).

### DIMM

- Parámetro de Fried `r₀`: diámetro de coherencia de la turbulencia. DIMM: monitor de movimiento diferencial de imagen.

💡 **Contexto en la clase [B48-C12](../programa/clases/B48/B48-C12-monitorizacion-de-seeing/CLASE.md):**
- **Idea central (modelo mental):** Dos corchos en el oleaje: lo que importa no es cuánto sube cada uno sino cuánto cambia su distancia; más turbulencia, más cambio.
- 🎯 **Por qué importa:** Sin medir el seeing, no se sabe si una noche sirve para un programa. La decisión central: ¿cuántas medidas hacen falta para que `r₀` tenga una incertidumbre aceptable?
- 🔗 **Se estudia junto con:** Parámetro de Fried, Varianza longitudinal, Seeing, Kolmogorov.

📘 **Dónde se aprende:** [B48-C12 · Monitorización de seeing](../programa/clases/B48/B48-C12-monitorizacion-de-seeing/CLASE.md).

### DITL

- Fit check: ajuste con el dispensador. DITL: prueba de «día en la vida».

💡 **Cómo se explica en la clase [B90-C20](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md):**
- *CubeSat 101* (F7) añade la prueba DITL, el mínimo contenido de los informes (procedimientos con marcas de tiempo, fotos, gráficas, prueba de que la unidad sobrevivió) y que el integrador debe aprobar el procedimiento antes de la prueba.
- *Descripción textual:* los ensayos se encadenan de la inspección al DITL; cada uno puede fallar y entonces se hace retrabajo y se repite el mismo ensayo antes de pasar al siguiente.
- 🎯 **Por qué importa:** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?
- 🔗 **Se estudia junto con:** Campaña de calificación, Flujo de ensayos, Fit check, Contingencia.

📘 **Dónde se aprende:** [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### DLI

- **Significa:** integral diaria de luz (DLI).
- La integral diaria de luz (DLI) es su suma en un día (mol m⁻² d⁻¹).
- PPFD: flujo de fotones útiles. DLI: mol de fotones por m² y día.

💡 **Cómo se explica en la clase [B106-C12](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md):**
- Paso 1. DLI: `300·10⁻⁶·16·3600 = 17,28 mol/(m² día)`.
- Con 300 µmol/(m² s) durante 16 h, la DLI es 17,28 mol/(m² día) y las lámparas consumen 80 W/m² en promedio.
- 🎯 **Por qué importa:** Cultivar reduce la masa de alimento a lanzar y devuelve oxígeno, pero cuesta mucha área y electricidad. La decisión central: ¿qué fracción de la dieta compensa cultivar dado el costo en área y energía?
- 🔗 **Se estudia junto con:** PPFD, Eficacia de la lámpara, Eficiencia de uso de la luz, Fracción comestible.

📘 **Dónde se aprende:** [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md); [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### DM

- **Significa:** discernibilidad (DM).
- La discernibilidad (DM) mide la pérdida de información.

💡 **Contexto en la clase [B124-C13](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md):**
- 🎯 **Por qué importa:** Abrir datos sin proteger a las personas es un daño, y proteger sin medir es una promesa vacía. La decisión central: ¿cuánto generalizar los datos para que ninguna persona sea identificable y cuánta información se pierde?
- 🔗 **Se estudia junto con:** k-anonimato, generalización, supresión, reticulado.

📘 **Dónde se aprende:** [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md).

### DO

- **Significa:** oxígeno disuelto (DO).
- El oxígeno disuelto (DO) es el que pueden respirar las raíces.

💡 **Cómo se explica en la clase [B115-C01](../programa/clases/B115/B115-C01-cultivos-hidroponicos-para-habitats/CLASE.md):**
- Estimar el oxígeno disuelto de entrada y la caída producida por la respiración de las raíces.
- Oxigeno disuelto en la entrada (saturacion empirica, nivel del mar, aire 20.9 % O2)
- 🎯 **Por qué importa:** Un cultivo sin suelo depende por completo de que el caudal, el oxígeno y el nivel del depósito no fallen. La decisión central: ¿qué caudal y qué volumen hacen falta para que las raíces reciban oxígeno y agua sin que el sistema se vacíe o se inunde, y cómo se comprueba?
- 🔗 **Se estudia junto con:** hidroponía, película de nutrientes (NFT), ecuación de Manning, número de Froude.

📘 **Dónde se aprende:** [B115-C01 · Cultivos hidropónicos para hábitats](../programa/clases/B115/B115-C01-cultivos-hidroponicos-para-habitats/CLASE.md).

### DOP

- El DOP (*dilution of precision*) amplifica el error: `PDOP = √(Q₁₁+Q₂₂+Q₃₃)` con `Q = (GᵀG)⁻¹`.

💡 **Cómo se explica en la clase [B57-C10](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md):**
- El error 3D simulado coincide con `PDOP × σ` en ambos casos: el DOP resume cuánto amplifica la geometría el ruido de medición.
- Paso 1 · DOP. `PDOP = 2,80` con ocho satélites repartidos.
- ⚠️ **Error frecuente:** Creer que más satélites siempre mejora el DOP. Depende de la distribución (8.2).
- 🎯 **Por qué importa:** La geodesia con GNSS mide posiciones de estaciones con precisión de milímetros a centímetros y sirve para ver cómo se mueve la corteza. Pero la precisión depende de la geometría de los satélites.
- 🔗 **Se estudia junto con:** pseudodistancia, matriz de geometría, HDOP, VDOP.

📘 **Dónde se aprende:** [B57-C10 · Geodesia mediante GNSS](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md).

### DRO

- Una DRO es una órbita periódica retrógrada y plana alrededor de la Luna.

💡 **Cómo se explica en la clase [B76-C06](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md):**
- Una DRO de `70.000 km` supera el radio de Hill (`61.274 km`) y permanece ligada porque es periódica y retrógrada.
- Una DRO que cruza `y = 0` a `70.000 km` de la Luna tiene `vy0 = 0,519364` (adimensional), periodo `13,916 d` y `C = 2,92852`; su máxima separación al otro lado es `73.434 km`.
- ⚠️ **Error frecuente:** Buscar la DRO sin continuación. Se corrige con 8.2.
- 🎯 **Por qué importa:** La NRHO es inestable y exige mantenimiento; la DRO es estable. La decisión central: ¿qué se gana y qué se paga al elegir una órbita estable y lejana frente a una NRHO cercana?
- 🔗 **Se estudia junto con:** amplitud, continuación, monodromia plana, par doble en 1.

📘 **Dónde se aprende:** [B76-C06 · Órbitas DRO — Dinámica cislunar y operaciones de proximidad](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md).

### DSB

- **Significa:** rotura de doble cadena (DSB).
- Una rotura de doble cadena (DSB) corta las dos hebras del ADN.

💡 **Contexto en la clase [B64-C01](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md):**
- **Idea central (modelo mental):** El modelo trata cada genoma irradiado como una urna: la dosis decide cuántos cortes caen, y la reparación decide cuántos puede asumir.
- 🎯 **Por qué importa:** La radiación ionizante rompe el ADN, y una célula muere cuando el daño supera su capacidad de reparación. La pregunta motivadora: ¿por qué dos organismos con el mismo daño inicial por gray sobreviven a dosis tan distintas?
- 🔗 **Se estudia junto con:** dosis absorbida, rendimiento, capacidad de reparación, supervivencia.

📘 **Dónde se aprende:** [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md).

### DSK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Contexto en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, CK, PCK.

📘 **Dónde se aprende:** [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### DTE

- **Significa:** Enlace directo a la Tierra (DTE).
- Rango oblicuo: distancia estación–satélite según la elevación. Enlace directo a la Tierra (DTE): comunicación sin relé.

💡 **Contexto en la clase [B96-C01](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md):**
- 🎯 **Por qué importa:** Quien opera una nave no puede tratarla como un equipo de laboratorio: cada comando viaja a la velocidad de la luz y cada contacto dura minutos. La decisión central: ¿qué segmento hace qué y cuánto tardan en comunicarse?
- 🔗 **Se estudia junto con:** Segmento espacial, Segmento terrestre, MOC/SOC, Retardo de propagación.

📘 **Dónde se aprende:** [B96-C01 · Segmento espacial y segmento terrestre](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md).

### EAC

- El EAC es la estimación del costo final; el ETC, lo que falta gastar; el VAC, `BAC − EAC`.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- Si el rendimiento de costo se mantiene, `EAC = BAC/CPI = 100,63` Mum (ETC `40,63`, VAC `-20,63`), idéntico a `AC + (BAC − EV)/CPI` (error `0,0e+00`).
- Si el resto se hace según lo presupuestado, `EAC = AC + (BAC − EV) = 92,30`; si el costo depende de CPI y SPI juntos, `108,55`.
- ⚠️ **Error frecuente:** Usar un solo EAC sin explicar su supuesto. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, EV, AC.

📘 **Dónde se aprende:** [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### EC

- **Significa:** conductividad eléctrica (EC).
- La conductividad eléctrica (EC) es una medida global de las sales.

💡 **Contexto en la clase [B115-C03](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md):**
- 🎯 **Por qué importa:** Una solución nutritiva que se repone «por conductividad» puede parecer estable y estar desequilibrada. La decisión central: ¿qué se mide, cada cuánto y qué se repone para que cada ion se mantenga cerca de su objetivo, y cuándo conviene renovar la solución?
- 🔗 **Se estudia junto con:** solución nutritiva, macronutrientes, micronutrientes, solución madre.

📘 **Dónde se aprende:** [B115-C03 · Control de nutrientes y solución nutritiva](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md).

### ECEF

- La latitud geodésica `φ` es el ángulo de la normal al elipsoide con el plano ecuatorial; la longitud `λ`, el ángulo desde el meridiano origen; la altura elipsoidal `h`, la distancia a lo largo de la normal. ECEF (*Earth-centered, Earth-fixed*) designa coordenadas cartesianas terrestres.

💡 **Cómo se explica en la clase [B13-C11](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md):**
- A["(φ, λ, h)<br/>geodésicas"] -->|"N = a/√(1−e² sen²φ)"| B["(X, Y, Z)<br/>cartesianas ECEF"]
- 🎯 **Por qué importa:** Una estación terrestre transmite a un satélite; el software de seguimiento necesita su posición en X, Y, Z. El técnico de campo tiene su posición en latitud, longitud y altura.
- 🔗 **Se estudia junto con:** sistema de referencia terrestre geocéntrico (GTRS), Sistema Internacional de Referencia Terrestre (ITRS), realización, ITRF.

📘 **Dónde se aprende:** [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### ECI/ECEF

- Elevación máxima: pico de la pasada. ECI/ECEF: marcos inercial y fijo a la Tierra.

💡 **Cómo se explica en la clase [B96-C04](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md):**
- Se rota a ECEF con `θ = ωₑ t` y se calcula la elevación con el vector hacia arriba de la estación.
- O["Orbita circular ECI"] --> R["Rotacion a ECEF"]
- ⚠️ **Error frecuente:** Olvidar la rotación terrestre. Pasa de ECI a ECEF (8.2)
- 🎯 **Por qué importa:** Un contacto perdido por mala planificación no se recupera hasta la siguiente pasada, que puede estar a horas. La decisión central: ¿qué ventanas hay, cuánto duran y cuáles merece la pena usar?
- 🔗 **Se estudia junto con:** Ventana, Elevación máxima, Semiángulo central, Cota.

📘 **Dónde se aprende:** [B96-C04 · Planificación de contactos](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md).

### ECLSS

- zona de desempeño: el más estrecho en el que el trabajo rutinario no se degrada por estrés térmico. ECLSS: sistema de control ambiental y soporte vital.
- ECLSS: sistema de control ambiental y soporte vital.

💡 **Cómo se explica en la clase [B106-C01](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md):**
- H --> E["ECLSS repone, recicla, evacua"]
- *Descripción textual:* la persona toma oxígeno, agua y alimento y emite CO₂, vapor, calor y residuos a la cabina; el ECLSS cierra el lazo reponiendo o reciclando.
- 🎯 **Por qué importa:** Un hábitat se diseña de adentro hacia afuera: primero lo que consume y emite la tripulación, después la máquina que lo repone. Si el balance humano está mal, todo el ECLSS queda mal dimensionado.
- 🔗 **Se estudia junto con:** Consumo específico de oxígeno, Cociente respiratorio (RQ), Normoxia, Zona de salud.

📘 **Dónde se aprende:** [B106-C01 · Requisitos de habitabilidad](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md); [B106-C09 · Sistemas ECLSS](../programa/clases/B106/B106-C09-sistemas-eclss/CLASE.md).

### ECM

- El ECM es el error cuadrático medio.

💡 **Cómo se explica en la clase [B74-C10](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md):**
- Ejercicio 4 · autónomo. ¿Por qué el ECM de los tres es casi igual?
- Ejercicio 12 · integrador. Integrador. Elabora tu *comparación EKF frente a UKF*: ECM y NEES de EKF, UKF y Bayes, explicación de la diferencia y límites, rotulando lo sintético.
- 🎯 **Por qué importa:** Un filtro puede dar una estimación aceptable y una covarianza falsa. La decisión central: ¿cuándo basta el EKF y cuándo la covarianza obliga a usar un filtro no lineal, y cómo lo verifico con una referencia?
- 🔗 **Se estudia junto con:** transformada unscented, puntos sigma, UKF, muestreo de importancia.

📘 **Dónde se aprende:** [B74-C10 · Filtro de Kalman no lineal](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md).

### EDF

- La cota de Liu y Layland `U ≤ n(2^(1/n) − 1)` es suficiente para RM con plazos iguales a los períodos y tiende a `ln 2 = 0,6931`. EDF es óptimo para una CPU con tareas expulsables y plazo igual al período: cumple si `U ≤ 1`.
- La holgura es `plazo − hora de término`. EDF es la regla del plazo más cercano.

💡 **Cómo se explica en la clase [B88-C06](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md):**
- Es armónico con `U = 1,0000`: RM y EDF cumplen, con 7 cambios cada una.
- EDF es una fila donde pasa primero quien tiene la cita más próxima.
- ⚠️ **Error frecuente:** Creer que EDF no puede fallar. Falla si `U > 1` (ejercicio 9)
- 🎯 **Por qué importa:** Elegir la política determina cuánta CPU se puede usar con garantías. La decisión central: ¿RM basta, o se necesita EDF para el conjunto de tareas?
- 🔗 **Se estudia junto con:** cota de Liu y Layland, cambio de contexto.

📘 **Dónde se aprende:** [B88-C06 · Planificación de tareas RTOS](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md); [B110-C04 · Priorización y decisiones bajo emergencia](../programa/clases/B110/B110-C04-priorizacion-y-decisiones-bajo-emergencia/CLASE.md).

### EDO

- **Significa:** ecuación diferencial ordinaria (EDO).
- Una ecuación diferencial ordinaria (EDO) relaciona una función de una variable con sus derivadas.
- Una ecuación diferencial ordinaria (EDO) relaciona una función con sus derivadas.

💡 **Contexto en la clase [B14-C03](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md):**
- **Idea central (modelo mental):** Un algoritmo numérico es una máquina con perillas (método, tolerancias) y una salida. El árbitro es la verificación: una solución exacta o una cantidad conservada. Giras las perillas hasta que el árbitro queda satisfecho, y entonces registras el valor de las perillas junto con el resultado.
- 🎯 **Por qué importa:** Un integrador devuelve un número aunque sea malo. Con las tolerancias por defecto, una órbita circular puede no cerrarse después de una vuelta y el programa no se queja.
- 🔗 **Se estudia junto con:** problema de valor inicial, paso, paso adaptativo, error local.

📘 **Dónde se aprende:** [B14-C03 · Análisis numérico con SciPy](../programa/clases/B14/B14-C03-analisis-numerico-con-scipy/CLASE.md); [B17-C03 · Redes neuronales informadas por la física (PINN)](../programa/clases/B17/B17-C03-redes-neuronales-informadas-por-la-fisica-pinn/CLASE.md).

### EDP

- Una EDP relaciona una función de varias variables con sus derivadas parciales.

💡 **Cómo se explica en la clase [B11-C13](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md):**
- Escribir las EDP del calor, de la onda, de Laplace y de la advección.
- Clasificar una EDP lineal de segundo orden con `B² − 4AC`.
- ⚠️ **Error frecuente:** Confundir EDO y EDP. Se corrige con el ejercicio 1 y el vocabulario (sección 6).
- 🎯 **Por qué importa:** El calor que atraviesa un escudo, las ondas en una estructura, el potencial gravitatorio de un cuerpo extenso, el transporte de partículas en un plasma: todos son EDP. Antes de discretizar hay que saber *qué tipo de problema es* (qué datos pide, cómo viaja la información) porque de ello depende el método.
- 🔗 **Se estudia junto con:** parabólica, hiperbólica, elíptica, advección.

📘 **Dónde se aprende:** [B11-C13 · Ecuaciones en derivadas parciales](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md).

### EIRP

- La EIRP es la potencia isotrópica equivalente radiada.
- La EIRP es `P_tx − L + G`.

💡 **Cómo se explica en la clase [B56-C16](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md):**
- Paso 1 · Datos. `S_min = 4,88 × 10⁻²⁶ W/m²`, `EIRP = 2 × 10¹³ W`.
- El ejemplo conductor sintético es un receptor de radio con `T_sis = 25 K`, `A_ef = 5000 m²`, `Δν = 1 Hz`, `τ = 100 s`, dos polarizaciones y `SNR = 10`, frente a un transmisor de `EIRP = 2 × 10¹³ W`.
- ⚠️ **Error frecuente:** Confundir EIRP y potencia del transmisor. Se corrige con el vocabulario.
- 🎯 **Por qué importa:** Buscar tecnología exige saber qué flujo mínimo detecta un receptor y qué potencia debería tener un transmisor a una distancia dada. La decisión central: dados la temperatura del sistema, el área efectiva, el ancho de banda y el tiempo de integración, ¿qué flujo mínimo se detecta y hasta qué distancia llega un transmisor dado?
- 🔗 **Se estudia junto con:** tecnofirma, flujo mínimo detectable, ecuación del radiómetro, señal de banda estrecha.

📘 **Dónde se aprende:** [B56-C16 · Tecnofirmas y búsqueda SETI](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md); [B91-C08 · Antenas de gran apertura y estaciones de espacio profundo](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md).

### EKF

- El EKF linealiza la dinámica y la medida alrededor de la estimación actual.

💡 **Cómo se explica en la clase [B74-C09](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md):**
- El ajuste por lotes de los mismos datos, propagado al instante final, difiere del EKF en `1,037 m`: la pequeña diferencia es el efecto de linealizar paso a paso.
- Límite: el EKF usa solo la derivada primera; con errores iniciales grandes la aproximación falla.
- ⚠️ **Error frecuente:** Creer que el EKF siempre es consistente. Comprueba el NEES, como en 8.4.
- 🎯 **Por qué importa:** Una órbita no es lineal en el estado, pero a cortos intervalos y con errores pequeños se comporta casi como tal. La decisión central: ¿hasta cuándo es válida la linealización del EKF y cómo me doy cuenta de que dejó de serlo?
- 🔗 **Se estudia junto con:** matriz de transición, jacobiano de medida, NEES, forma de Joseph.

📘 **Dónde se aprende:** [B74-C09 · Filtro de Kalman extendido](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md).

### ELBO

- El ELBO (*evidence lower bound*) es `E_q[log p(y, θ)] − E_q[log q(θ)]`.

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- En cambio, el ELBO es una esperanza respecto de `q`, que se puede calcular o estimar si `q` es sencilla.
- Maximizar el ELBO sobre `φ` es una optimización.
- ⚠️ **Error frecuente:** Pensar que `ELBO` alto significa aproximación fiel. Ejercicios 7 y 11.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.
- 🔗 **Se estudia junto con:** divergencia de Kullback–Leibler, familia variacional, aproximación variacional, campo medio.

📘 **Dónde se aprende:** [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### EM

- **Significa:** Modelo de ingeniería (EM).
- Prototipo: versión temprana para explorar el diseño. Modelo de ingeniería (EM): modelo funcionalmente representativo para probar el diseño.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- D["Defecto de diseno<br/>q = 0.30"] --> E["Modelo de ingenieria<br/>detecta 0.80"]
- *Descripción textual:* un defecto de diseño pasa por el modelo de ingeniería, que detecta la mayoría y lo corrige a bajo costo; los que escapan pasan a la unidad de vuelo, que detecta parte a mayor costo de corrección; los que escapan de ambas llegan a órbita y cuestan la pérdida.
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?
- 🔗 **Se estudia junto con:** Prototipo, Modelo de calificación (QM), Protovuelo, Unidad de vuelo (FM).

📘 **Dónde se aprende:** [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### EMC

- EMC: capacidad de un equipo de funcionar en su entorno sin perturbarlo ni ser perturbado.

💡 **Cómo se explica en la clase [B90-C13](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md):**
- No: el límite es sintético; el vigente sale de los requisitos de EMC del proyecto.
- python programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/margenes_emc.py
- 🎯 **Por qué importa:** Un convertidor de potencia emite armónicos que viajan por el arnés y pueden perturbar a otro equipo. El margen de 2 dB que pasa hoy puede ser negativo mañana si cambia la incertidumbre.
- 🔗 **Se estudia junto con:** Emisión conducida, dBµV, Límite, Margen.

📘 **Dónde se aprende:** [B90-C13 · Compatibilidad electromagnética EMC](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md).

### EMI

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B90-C14](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Qué medidas reducen la EMI sin cambiar la distancia?
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué la prueba de EMI se hace con el sistema integrado?
- 🎯 **Por qué importa:** Un transmisor de 1 W deja un armónico de −30 dBm; el piso de ruido de un receptor estrecho está cerca de −132 dBm. La diferencia de más de 100 dB se pierde con facilidad en un chasis de 10 cm.
- 🔗 **Se estudia junto con:** Fuente y víctima, Piso de ruido, I/N, Desensibilización.

📘 **Dónde se aprende:** [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md).

### ENBW

- El ENBW es el ancho de un filtro rectangular con el mismo ruido.

💡 **Cómo se explica en la clase [B46-C10](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md):**
- Con `fs = 2,4 MHz` y `N = 1024` la resolución es `2343,75 Hz`; el ENBW de Hann vale `1,5000` bines; la dispersión relativa de un canal pasa de `0,963` con `M = 1` a `0,128` con `M = 64`.
- Ejercicio 4. ENBW en Hz de Hann con `Δf = 2343,75 Hz`.
- ⚠️ **Error frecuente:** Olvidar el ENBW. Se corrige con 8.1.
- 🎯 **Por qué importa:** Promediar espectros es la forma práctica de aplicar la ecuación del radiómetro con un instrumento barato, pero la ventana cambia el ancho de banda efectivo. La decisión central: ¿cuántos espectros promediar para detectar una línea débil?
- 🔗 **Se estudia junto con:** I/Q, FFT, ventana de Hann, promediado.

📘 **Dónde se aprende:** [B46-C10 · Radioastronomía mediante SDR](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md).

### ENL

- El ENL (número equivalente de vistas) mide cuánto speckle queda.

💡 **Cómo se explica en la clase [B69-C03](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md):**
- Al promediar `L` vistas independientes, `CV = 1/√L` y `ENL = L`.
- En la zona de reflectividad 1, el ENL pasa de 1,01 a 21,19; en la de 4, de 0,94 a 16,60; las medias no cambian (0,984 → 0,984 y 4,112 → 4,115).
- 🎯 **Por qué importa:** Un valor de píxel aislado de una imagen SAR no mide la reflectividad de la superficie: es una muestra de una distribución muy ancha. La decisión central: ¿cuánto hay que promediar o filtrar para estimar la reflectividad con una incertidumbre dada, y a qué precio en resolución?
- 🔗 **Se estudia junto con:** speckle, intensidad, contraste, multivista.

📘 **Dónde se aprende:** [B69-C03 · Ruido speckle y filtrado en imágenes SAR](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md).

### ENU

- Velocidad radial: razón de cambio del rango. ENU: marco local este–norte–arriba.

💡 **Cómo se explica en la clase [B96-C05](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md):**
- Con `d = r_sat − r_est` en ECEF y los vectores unitarios ENU `ê`, `n̂`, `û`: `E = d·ê`, `N = d·n̂`, `U = d·û`;
- P["Posicion ECEF del satelite"] --> E["Marco local ENU"]
- 🎯 **Por qué importa:** Para que una antena apunte y un receptor enganche, la estación debe conocer de antemano el azimut, la elevación y el corrimiento de frecuencia. La decisión central: ¿hacia dónde apuntar y qué frecuencia esperar en cada instante?
- 🔗 **Se estudia junto con:** Estación de seguimiento, Azimut/elevación, Rango, Doppler.

📘 **Dónde se aprende:** [B96-C05 · Estaciones de seguimiento](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md).

### EOL

- BOL y EOL son los extremos de la vida.

💡 **Cómo se explica en la clase [B85-C05](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md):**
- Los que mantienen `250–320 K` en BOL y EOL: pintura blanca.
- El coating a medida (`ε ≈ 0,25`, `α ≈ 0,1` según NASA) en estos números se pasa del intervalo en EOL: `340,49 K`.
- ⚠️ **Error frecuente:** Ignorar el EOL. el caso caliente usa EOL (8.4)
- 🎯 **Por qué importa:** Cambiar un recubrimiento es la forma más barata de mover la temperatura de una superficie decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la superficie dentro del intervalo al principio y al final de la vida?
- 🔗 **Se estudia junto con:** cociente α/ε, espejo solar óptico (OSR), envejecimiento, BOL.

📘 **Dónde se aprende:** [B85-C05 · Recubrimientos ópticos térmicos](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md).

### EOP

- **Significa:** parámetros de orientación terrestre (EOP).
- Los parámetros de orientación terrestre (EOP) describen la orientación del Polo Celeste Intermedio (CIP) en el sistema terrestre y en el celeste y la orientación de la Tierra en torno a ese eje (S1, 2.2.2).

💡 **Cómo se explica en la clase [B13-C22](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md):**
- python programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/orientacion_terrestre.py
- 🎯 **Por qué importa:** Una estación terrestre apunta a una nave en el sistema celeste. Para ello debe saber cuánto ha girado la Tierra, hacia dónde apunta su eje en el cielo y dónde está ese eje dentro de la corteza.
- 🔗 **Se estudia junto con:** CIP, movimiento polar, UT1 − UTC, precesión-nutación.

📘 **Dónde se aprende:** [B13-C22 · Parámetros de orientación terrestre: precesión, nutación, UT1 y movimiento polar](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md).

### ERA

- **Significa:** ángulo de rotación terrestre (ERA).
- El ángulo de rotación terrestre (ERA) es el ángulo entre un origen celeste de referencia y un origen terrestre, que describe la rotación de la Tierra en torno a su eje; la convención IERS lo define como una función lineal de `UT1` (S1, ec. 5.14).

💡 **Cómo se explica en la clase [B13-C10](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md):**
- Definir el ángulo de rotación terrestre (ERA) y su fórmula convencional.
- 🎯 **Por qué importa:** Un telescopio en el desierto debe saber cuándo un objeto pasa por su meridiano, que es cuando está más alto y se observa mejor. Esa hora no es la del reloj civil: el cielo se adelanta casi cuatro minutos cada día.
- 🔗 **Se estudia junto con:** UT1, día sidéreo, longitud este, ángulo horario.

📘 **Dónde se aprende:** [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md).

### ESD

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B90-C03](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md):**
- La ESD Association (F11) publica ANSI/ESD S20.20 (versión 2021 citada en su página) y su página indica que el Departamento de Defensa de EE.
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué la ESD es un tema de integración y no solo de diseño?
- 🎯 **Por qué importa:** Un componente electrónico puede quedar con una falla latente tras una descarga que nadie sintió: una persona percibe una chispa solo por encima de unos miles de voltios (orden de magnitud no consultado), por encima de lo que puede dañar a un componente sensible.
- 🔗 **Se estudia junto con:** Modelo de cuerpo humano, Carga triboeléctrica, Resistencia de fuga, Falla latente.

📘 **Dónde se aprende:** [B90-C03 · Protección frente a ESD](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md).

### ES/EF

- Camino crítico: cadena de holgura cero. ES/EF: inicio y fin tempranos.

💡 **Contexto en la clase [B96-C09](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md):**
- 🎯 **Por qué importa:** Una secuencia que no cabe en la ventana deja comandos sin ejecutar o telemetría sin confirmar. La decisión central: ¿qué actividades fijan la duración mínima y cuánta holgura queda?
- 🔗 **Se estudia junto con:** Secuencia, Camino crítico, LS/LF, Holgura.

📘 **Dónde se aprende:** [B96-C09 · Secuencias de misión](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md).

### ETC

- **Significa:** Equivalente a tiempo completo (ETC).
- El EAC es la estimación del costo final; el ETC, lo que falta gastar; el VAC, `BAC − EAC`.
- Turno: bloque de 8 h. Equivalente a tiempo completo (ETC): fracción de una posición 24/7.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- Si el rendimiento de costo se mantiene, `EAC = BAC/CPI = 100,63` Mum (ETC `40,63`, VAC `-20,63`), idéntico a `AC + (BAC − EV)/CPI` (error `0,0e+00`).
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, EV, AC.

📘 **Dónde se aprende:** [B96-C03 · Roles de control de misión](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md); [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### ETL

- El ETL supone que las poblaciones siguen la temperatura local.
- El ETL reparte la población con `(2J+1) exp(−E_J/kT)`.

💡 **Cómo se explica en la clase [B32-C02](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué falla si no hay ETL?
- ⚠️ **Error frecuente:** Aplicar ETL sin discutirlo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Si el ETL falla, las abundancias que se derivan son erróneas. La decisión central: ¿cuánto hidrógeno está ionizado a cada temperatura y densidad?
- 🔗 **Se estudia junto con:** ecuación de Boltzmann, ecuación de Saha, fracción ionizada, desviación no ETL.

📘 **Dónde se aprende:** [B32-C02 · Equilibrio termodinámico local y desviaciones no LTE](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md); [B46-C12 · Emisiones moleculares](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md).

### EV

- El PV es el valor del trabajo planificado a la fecha; el EV, el valor del trabajo logrado; el AC, el costo real.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- La suma de los paquetes coincide con la de los elementos y con el proyecto para BAC, PV, EV y AC (error `0,0e+00`): lo que está en los hijos es todo lo que está en el padre.
- Con `PV = 57,00`, `EV = 47,70` y `AC = 60,00`: `CV = EV − AC = -12,30` y `SV = EV − PV = -9,30` Mum;
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, AC, CPI.

📘 **Dónde se aprende:** [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### EWMA

- La EWMA usa `z_t = λ x̄_t + (1−λ) z_{t−1}`.
- La EWMA pondera con `λ = 2/(N + 1)`.

💡 **Cómo se explica en la clase [B84-C35](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md):**
- Shewhart señala en los subgrupos `22, 29, 31, 32, 34, 36, 37`; la EWMA, de forma sostenida desde el `22`.
- Con `ARL₀` iguales (~370), la EWMA detecta desplazamientos pequeños mucho antes que Shewhart.
- 🎯 **Por qué importa:** Un proceso con `Cpk` de 1,33 puede desplazarse 1σ sin dejar piezas fuera de tolerancia durante semanas si solo se inspecciona el producto; la carta lo detecta en pocos subgrupos. La decisión central: ¿qué carta detecta antes un desplazamiento del proceso y qué capacidad tiene el proceso antes y después?
- 🔗 **Se estudia junto con:** carta X-barra, ARL.

📘 **Dónde se aprende:** [B84-C35 · Control de procesos de fabricación y calidad](../programa/clases/B84/B84-C35-control-de-procesos-de-fabricacion-y-calidad/CLASE.md); [B107-C05 · Prevención de lesiones en entrenamiento y trabajo operativo](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md).

### F1

- La exactitud es `(TP + TN)/total`; la precisión, `TP/(TP + FP)`; la exhaustividad (*recall*), `TP/(TP + FN)`; el F1, la media armónica de las dos últimas.

💡 **Cómo se explica en la clase [B25-C20](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md):**
- G --> H["Exactitud, precisión, recall, F1"]
- Construir la matriz de confusión y calcular exactitud, precisión, exhaustividad y F1.
- 🎯 **Por qué importa:** Clasificar galaxias a gran escala exige algo más que una regla que parezca razonable: hay que decir qué debe cumplir, probarlo contra casos de respuesta conocida y evaluar con honestidad cómo se comporta donde los datos son malos.
- 🔗 **Se estudia junto con:** concentración, descriptor, umbral, matriz de confusión.

📘 **Dónde se aprende:** [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md).

### FAIR

- La semilla fija la secuencia aleatoria. FAIR son las cuatro propiedades de los datos (localizables, accesibles, interoperables, reutilizables).

💡 **Cómo se explica en la clase [B124-C14](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md):**
- Faltan, por ejemplo, el índice en un repositorio, los vocabularios controlados y los enlaces; los criterios son un ejemplo propio de la clase, no la lista oficial de FAIR.
- M["metadatos y licencia"] --> F["lista FAIR"]
- ⚠️ **Error frecuente:** Tomar los 12 criterios como la norma FAIR. Se corrige con 8.4.
- 🎯 **Por qué importa:** «Es reproducible» suele afirmarse sin evidencia. La decisión central: ¿qué hay que fijar y registrar para que un análisis dé el mismo resultado y se pueda comprobar?
- 🔗 **Se estudia junto con:** reproducibilidad, huella, semilla, procedencia.

📘 **Dónde se aprende:** [B124-C14 · Ciencia abierta y reproducibilidad](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md).

### FAR

- El POD es la fracción de eventos detectados, el FAR la de alertas falsas y el CSI la de aciertos sobre todos los casos relevantes.
- El POD, el FAR y el Heidke.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- *Descripción textual:* las medidas se convierten en escalas G, S y R; la regla y lo observado forman la tabla de contingencia, de la que salen POD, FAR y Heidke.
- Calcular POD, FAR, CSI y la puntuación de Heidke por dos fórmulas.
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?
- 🔗 **Se estudia junto con:** escala, acierto, falsa alarma, fallo.

📘 **Dónde se aprende:** [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B33-C13 · Pronóstico de actividad geomagnética](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md).

### FECF

- El FECF es un CRC de 16 bits con polinomio `X¹⁶ + X¹² + X⁵ + 1` y registro inicial a unos.

💡 **Cómo se explica en la clase [B94-C03](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md):**
- El CRC se calcula sobre toda la trama salvo el propio FECF, con registro inicial a unos.
- Al recalcularlo sobre trama + FECF el resultado debe ser cero, y así lo comprueba el receptor.
- 🎯 **Por qué importa:** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?
- 🔗 **Se estudia junto con:** trama de transferencia de telemetría, SCID, VCID, contador de canal maestro.

📘 **Dónde se aprende:** [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### FEFO

- FIFO emite el lote recibido antes; FEFO emite el que caduca antes.

💡 **Cómo se explica en la clase [B100-C01](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md):**
- Caducan `324 u` (15,6 % de lo recibido) en FIFO y `164 u` (7,9 %) en FEFO: 160 u menos, un 49 % menos.
- Para el lote L05 en FEFO hay 26 emisiones, 102 u, entre los días 199 y 262; por consumidor: C1 = 21, C2 = 21, C3 = 23, C4 = 15, C5 = 22 (suma 102).
- ⚠️ **Error frecuente:** Creer que FEFO atiende más demanda. Se corrige con 8.2: atiende la misma y caduca menos
- 🎯 **Por qué importa:** Un inventario que solo sabe «cuántas unidades hay» no puede decir de qué lote vienen, cuándo caducan ni dónde se usaron. La decisión central: ¿qué registro mínimo hace falta para emitir primero lo que caduca antes y para encontrar, si un lote resulta defectuoso, adónde fue?
- 🔗 **Se estudia junto con:** lote, FIFO, Caducado, trazabilidad.

📘 **Dónde se aprende:** [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### FER

- BER: tasa de error de bit. FER: tasa de error de trama, `1 − (1 − p)^n`.

💡 **Cómo se explica en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- Paso 2 · FER. `1 − (1 − 10⁻⁴)^1040 = 1 − e^{−0,104} = 0,0988`.
- Con `BER = 10⁻⁴`, la FER es 0,0988 y cada trama se reintenta en promedio 1,11 veces; con `BER = 10⁻³`, FER 0,647 y 2,83 envíos.
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?
- 🔗 **Se estudia junto con:** Prueba de extremo a extremo, CRC, BER, Ráfaga.

📘 **Dónde se aprende:** [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### FFP

- **Significa:** Precio fijo (FFP).
- Precio fijo (FFP): el pago no depende del costo real.

💡 **Cómo se explica en la clase [B124-C10](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md):**
- El precio fijo da certeza de gasto al comprador pero un precio mayor; el CPIF reparte el desvío (el contratista asume el 20 % hasta el techo) pero deja el gasto expuesto.
- El informe IG-20-005 de la OIG de la NASA (2019) señala que la NASA pasó a un enfoque comercial en que paga un precio fijo por el servicio de transporte de tripulación, como ya hacía con la carga.
- ⚠️ **Error frecuente:** Creer que el precio fijo es siempre el más barato. Se corrige con 8.1 y 8.4.
- 🎯 **Por qué importa:** El tipo de contrato reparte el riesgo de sobrecosto entre quien compra y quien vende. La decisión central: ¿cuánto riesgo asume cada parte con cada tipo de contrato y cuánto cuesta ese reparto en promedio?
- 🔗 **Se estudia junto con:** Costo más incentivo (CPIF), honorario objetivo, razón de reparto, techo.

📘 **Dónde se aprende:** [B124-C10 · Contratos y compras espaciales](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md).

### FFT

- La FFT es una familia de algoritmos que calculan la DFT en `O(N log N)`; la versión más usada se atribuye a Cooley y Tukey, como señala la documentación de NumPy (S1).
- La FFT da el espectro.

💡 **Cómo se explica en la clase [B15-C05](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md):**
- La FFT parte la serie en muestras pares e impares, calcula la DFT de cada mitad (que es más pequeña) y las combina con unos pocos productos.
- Su límite: al ordenar, el orden final es único pero depende de las comparaciones; en la FFT el resultado es exactamente el de la DFT, sin aproximación.
- ⚠️ **Error frecuente:** Aplicar una FFT de base 2 a un `N` que no lo es. La implementación propia debe fallar o rellenar; se declara.
- 🎯 **Por qué importa:** Una curva de luz de 27 días con cadencia de 2 minutos tiene 19 440 muestras. La suma directa de la DFT necesita unos 378 millones de multiplicaciones complejas; una imagen de 1024 × 1024 necesitaría muchísimas más.
- 🔗 **Se estudia junto con:** mariposa, base 2, relleno con ceros, orden estándar.

📘 **Dónde se aprende:** [B15-C05 · Transformada rápida de Fourier](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md); [B46-C10 · Radioastronomía mediante SDR](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md).

### FIFO

- La clase de servicio del protocolo de paquetes es `bulk`, `normal` o `expedited`, con prioridad 0, 1 y 2. FIFO sirve por orden de llegada.
- Un lote es la unidad de trazabilidad. FIFO emite el lote recibido antes;

💡 **Cómo se explica en la clase [B94-C05](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md):**
- FIFO reparte el daño por igual y ni siquiera protege lo urgente.
- S --> P["politica: FIFO,<br/>prioridad estricta,<br/>reparto ponderado"]
- 🎯 **Por qué importa:** Si la demanda supera a la capacidad, alguien espera. La decisión central: ¿qué política de cola garantiza lo urgente sin dejar sin servicio a las demás clases, y a qué coste?
- 🔗 **Se estudia junto con:** clase de servicio, Prioridad estricta, reparto ponderado, inanición.

📘 **Dónde se aprende:** [B94-C05 · Calidad de servicio y prioridades en redes espaciales](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md); [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### FIR

- Un filtro FIR (respuesta finita al impulso) calcula `y[n] = Σ_{m=0}^{M−1} h[m] x[n − m]`; la lista `h[m]` son los coeficientes.

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- Un FIR de coeficientes simétricos y `M` términos retrasa todas las frecuencias por igual, `(M − 1)/2` muestras (en el laboratorio, un pulso con centroide en 150 sale en `165` con `M = 31`: retardo `15,000` exacto).
- (4) retardo del FIR causal (M=31): centroide de 150.000 a 165.000 (retardo 15.000; teoría 15.0)
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.
- 🔗 **Se estudia junto con:** filtro digital, lineal, invariante, coeficientes.

📘 **Dónde se aprende:** [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### FISTA

- La restricción blanda de velocidad se castiga con `ρ max(0, |ω|−ω_max)²`. FISTA es un gradiente proyectado acelerado.

💡 **Cómo se explica en la clase [B87-C21](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md):**
- FISTA con 1500 iteraciones por paso (arranque en caliente) converge: la diferencia máxima entre la solución a 1500 y a 15 000 iteraciones es `0,623 %` del límite y el residuo del gradiente proyectado `7,11e-01`.
- Paso 3 · Solución. FISTA, `0,62 %` de diferencia con la solución casi exacta.
- 🎯 **Por qué importa:** Un PD satura el par y no sabe de límites de velocidad: puede superar el máximo de la rueda o de la carga útil. La decisión central: ¿cómo formular un problema que respete par y velocidad, cuánto cuesta calcularlo y qué se gana?
- 🔗 **Se estudia junto con:** MPC, horizonte, QP condensado, restricción dura.

📘 **Dónde se aprende:** [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md).

### FITS

- FITS: bloques de 2880 bytes con tarjetas de 80 caracteres.

💡 **Cómo se explica en la clase [B40-C14](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md):**
- *Descripción textual:* se escribe y se lee un FITS, se convierten unidades y se evalúa una verosimilitud por bandas.
- Escribir y leer cabeceras FITS de 80 caracteres.
- 🎯 **Por qué importa:** Usar un producto sin leer su cabecera es una fuente clásica de errores de unidades y de orden de pixeles. La decisión central: ¿qué dice la cabecera y cómo se convierte y se compara con un modelo?
- 🔗 **Se estudia junto con:** BINTABLE, Centinela, verosimilitud gaussiana, banda.

📘 **Dónde se aprende:** [B40-C14 · Productos de datos de Planck y misiones del CMB](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md).

### FK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- Por tipo: SPK, CK, PCK, IK, FK, LSK, SCLK.
- Un CK (actitud de la nave) junto con IK y FK.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, CK, PCK.

📘 **Dónde se aprende:** [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### FM

- **Significa:** Unidad de vuelo (FM).
- Protovuelo: calificación aplicada a la unidad de vuelo. Unidad de vuelo (FM): la que vuela.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- La CDS (F8) distingue calificación (con una unidad de ingeniería idéntica a la de vuelo y luego aceptación de la unidad de vuelo) y protovuelo (sobre la unidad de vuelo, que luego no se desmonta ni modifica), y señala que el flujo varía de una misión a otra.
- E -- "escapa 0.20" --> F["Unidad de vuelo<br/>detecta 0.70"]
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?
- 🔗 **Se estudia junto con:** Prototipo, Modelo de ingeniería (EM), Modelo de calificación (QM), Protovuelo.

📘 **Dónde se aprende:** [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### FMA

- La FMA calcula `a·b + c` con un solo redondeo.

💡 **Cómo se explica en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- Con dos redondeos (multiplicar y redondear, luego sumar) el error máximo es `5,96 × 10⁻⁸`; con un solo redondeo (FMA simulado: se calcula exacto en `float64` y se redondea una vez), es `0`.
- Si una GPU usa FMA y la CPU no, sus resultados diferirán aunque ambas sean correctas (S1).
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?
- 🔗 **Se estudia junto con:** GPU, transferencia, intensidad aritmética, reducción.

📘 **Dónde se aprende:** [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md).

### FOV

- **Significa:** Campo de visión (FOV).
- Campo de visión (FOV): ángulo total del cono de la cámara.

💡 **Cómo se explica en la clase [B101-C09](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md):**
- De cuántas cámaras, con qué campo de visión y dónde, no se consultó nada (N7).
- La escena de la clase es sintética: una caja de trabajo de 2 × 2 × 1 m centrada en el origen, una carga esférica de 0,4 m de radio en el centro que ocluye, y tres cámaras de 60° de campo de visión circular.
- 🎯 **Por qué importa:** Si el operador no ve el punto de contacto, depende de la imaginación. La decisión central: ¿qué cámaras necesito y dónde para que la zona de trabajo se vea, con qué resolución y sin puntos ciegos críticos?
- 🔗 **Se estudia junto con:** Eje óptico, Oclusión, Punto ciego, Tamaño de pixel en el objeto (GSD).

📘 **Dónde se aprende:** [B101-C09 · Coordinación visual y cámaras en operaciones con manipulador](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md).

### FPP

- La FPP es la probabilidad de falso positivo.

💡 **Cómo se explica en la clase [B29-C07](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md):**
- Con un solo observable débil, el FPP mínimo es `0,21`: no se puede validar.
- Definir la probabilidad de falso positivo `FPP = 1 − P(planeta)`.
- ⚠️ **Error frecuente:** Dar por validado un FPP alto. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Hay muchos más candidatos que posibilidades de seguimiento. Validar bien exige probabilidades honestas: ni optimistas ni conservadoras en exceso.
- 🔗 **Se estudia junto con:** validación, escenario, prior, calibración.

📘 **Dónde se aprende:** [B29-C07 · Métodos de validación planetaria](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md).

### FS

- **Significa:** Factor de seguridad (FS).
- Esfuerzo de aro: esfuerzo circunferencial `σ = P r/t`. Factor de seguridad (FS): cociente entre límite elástico y esfuerzo.

💡 **Cómo se explica en la clase [B106-C02](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md):**
- Un cilindro de 2 m de radio a 101,325 kPa necesita, con factor de seguridad 2 y una aleación ilustrativa de 276 MPa, un espesor mínimo de 1,468 mm (51,7 kg de pared por metro); a 34,5 kPa bastan 0,500 mm.
- Calcular el esfuerzo de aro de un cilindro de pared delgada y el espesor mínimo con un factor de seguridad.
- 🎯 **Por qué importa:** La presión interior empuja hacia afuera sobre todo el casco; un espesor insuficiente rompe el recinto y un orificio pequeño lo vacía lentamente. La decisión central: ¿qué espesor mínimo y qué tiempo de respuesta hay que garantizar para una presión y un tamaño de orificio dados?
- 🔗 **Se estudia junto con:** Esfuerzo de aro, Flujo estrangulado, Coeficiente de descarga Cd, Constante de tiempo τ.

📘 **Dónde se aprende:** [B106-C02 · Presurización de módulos](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md).

### FSPL

- **Significa:** Pérdida en espacio libre (FSPL).
- La FSPL es la pérdida en espacio libre.
- PIRE: potencia isotrópica radiada equivalente. Pérdida en espacio libre (FSPL): atenuación por distancia y frecuencia.

💡 **Cómo se explica en la clase [B96-C27](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md):**
- *Descripción textual:* la potencia, la ganancia y las pérdidas dan la PIRE; con la pérdida en espacio libre y el ruido del receptor se obtiene `C/N₀`; restando la tasa en dB da `Eb/N₀` y el margen; la PIRE se compara con el límite autorizado.
- Calcular la pérdida en espacio libre y la relación `C/N₀`.
- 🎯 **Por qué importa:** Un transmisor con potencia de más interfiere con otros y viola la licencia; con potencia de menos, no cierra el enlace. La decisión central: ¿qué potencia hace falta para un margen suficiente sin exceder el límite autorizado?
- 🔗 **Se estudia junto con:** PIRE, C/N₀, Eb/N₀, Margen.

📘 **Dónde se aprende:** [B96-C27 · Operación de equipos de radiofrecuencia en la estación](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md); [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md).

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

📘 **Dónde se aprende:** [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md); [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md); [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md) y 1 más.

### FX

- El correlador XF correlaciona en el tiempo y luego transforma; el FX transforma y luego multiplica.

💡 **Cómo se explica en la clase [B46-C15](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md):**
- La diferencia máxima relativa entre el espectro cruzado FX y la FFT de la correlación XF es `5,6 × 10^-16` (error de redondeo).
- F["FX: FFT y producto"] --> EQ["mismo espectro cruzado"]
- ⚠️ **Error frecuente:** Creer que FX y XF difieren. Se corrige con 8.2.
- 🎯 **Por qué importa:** La visibilidad es el dato básico de la imagen, y su ruido determina la sensibilidad. La decisión central: ¿cuántas muestras hay que correlacionar para fijar amplitud y fase con la precisión requerida?
- 🔗 **Se estudia junto con:** visibilidad, ruido de correlación, XF, lag.

📘 **Dónde se aprende:** [B46-C15 · Correladores y visibilidades](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md).

### GCI

- **Significa:** índice de convergencia de malla (GCI).
- El GCI (Roache) es `1,25 |f₃ − f₂|/(|f₃| (r^p − 1))`.
- El índice de convergencia de malla (GCI) estima la incertidumbre numérica a partir de tres mallas.

💡 **Cómo se explica en la clase [B79-C09](../programa/clases/B79/B79-C09-cfd-academico-fundamentos-y-limites/CLASE.md):**
- Calcular un índice de convergencia de malla (GCI).
- 🎯 **Por qué importa:** B11-C14/C15 no construyen simulaciones de flujo ni discuten sus límites. Sin esa discusión, una malla fina y un colorido mapa de campos se confunden con una predicción fiable.
- 🔗 **Se estudia junto con:** verificación, validación, número de Péclet, Péclet de celda.

📘 **Dónde se aprende:** [B79-C09 · CFD académico: fundamentos y límites](../programa/clases/B79/B79-C09-cfd-academico-fundamentos-y-limites/CLASE.md); [B84-C26 · Generación de mallas y convergencia en elementos finitos](../programa/clases/B84/B84-C26-generacion-de-mallas-y-convergencia-en-elementos-finitos/CLASE.md).

### GCM

- **Significa:** cifrado autenticado AES en modo Galois/Counter (GCM).
- Su base de interoperabilidad es el cifrado autenticado AES en modo Galois/Counter (GCM) con clave de 256 bits.

💡 **Contexto en la clase [B89-C25](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md):**
- 🎯 **Por qué importa:** Los comandos son la superficie más sensible de una misión; sin autenticación y sin protección contra repetición, una trama capturada podría reutilizarse, y un CRC solo detecta errores, no ataques (C12). La decisión central: ¿cómo garantizar que una trama es auténtica, íntegra y no repetida, y cuánto cuesta en sobrecarga?
- 🔗 **Se estudia junto con:** protocolo de seguridad de enlace de datos (SDLS), asociación de seguridad (SA), SPI, ventana anti-repetición.

📘 **Dónde se aprende:** [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md).

### GCRS

- El GCRS (sistema celeste geocéntrico) y el ITRS (sistema terrestre internacional) son sistemas de referencia; el IERS los relaciona con `[GCRS] = Q(t) R(t) W(t) [ITRS]`, donde `Q` es el movimiento del polo celeste, `R` la rotación de la Tierra alrededor del eje del polo y `W` el movimiento polar (S1, ec. 5.1).

💡 **Cómo se explica en la clase [B10-C16](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md):**
- C -->|"Q: precesión-nutación<br/>(omitido aquí)"| D["GCRS<br/>(celeste)"]
- Escribir la cadena `[GCRS] = Q(t) R(t) W(t) [ITRS]` y reconocer qué parte se calcula aquí.
- ⚠️ **Error frecuente:** Llamar «GCRS» o «inercial exacto» a un modelo simplificado. Se corrige en las secciones 8.7 y 10.
- 🎯 **Por qué importa:** Una estación terrestre tiene coordenadas fijas en la Tierra. Un satélite se propaga en un sistema inercial, donde las leyes de Newton valen.
- 🔗 **Se estudia junto con:** marco de referencia, inercial, ITRS, ángulo de rotación terrestre.

📘 **Dónde se aprende:** [B10-C16 · Transformación de marcos de referencia](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md).

### GIC

- La GIC es la corriente casi continua inducida en un conductor.

💡 **Cómo se explica en la clase [B30-C19](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. Un compañero afirma que una GIC de 17 A es típica.
- Ejercicio 12. Integrador. Elabora tu *ficha de los impactos del clima espacial*: GIC, niveles de retorno e incertidumbre.
- 🎯 **Por qué importa:** Las infraestructuras se diseñan para eventos raros, que no están en un registro corto. La decisión central: ¿qué corriente induce un campo dado y cuán fiable es extrapolar un nivel de 100 años?
- 🔗 **Se estudia junto con:** campo geoeléctrico, nivel de retorno, índice de la cola, extrapolación.

📘 **Dónde se aprende:** [B30-C19 · Impactos del clima espacial](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md).

### GIL

- El GIL es el bloqueo descrito arriba.
- El GIL (bloqueo global del intérprete) impide que dos hilos ejecuten código Python a la vez.

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Para cálculo puro en Python, los hilos no ayudan por el GIL (S1); los procesos sí, a costa de memoria y de serializar los datos.
- Para bibliotecas que liberan el GIL (como NumPy en muchas operaciones), los hilos pueden servir.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.
- 🔗 **Se estudia junto con:** proceso, hilo, trabajador, aceleración.

📘 **Dónde se aprende:** [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md); [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md).

### GM

- El GM (parámetro gravitacional estándar) es el producto de la constante de gravitación por la masa del cuerpo; para el Sol, 1,32712 × 10¹¹ km³/s² (S1).

💡 **Cómo se explica en la clase [B07-C20](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md):**
- El simulador lee `parametros_tierra.yaml` con `yaml.safe_load` y valida que GM, semieje, período y paso sean números positivos (C16).
- Trabaja en km y s: `GM` en km³/s², `a` en km, `v` en km/s.
- 🎯 **Por qué importa:** Un simulador es la forma de explorar un fenómeno cuya solución no tienes a mano, y de comprobar que entiendes uno cuya solución sí conoces. Aquí conoces la respuesta (una órbita circular se repite con un período dado por una fórmula), así que puedes verificar el simulador antes de confiar en él para casos que no conoces.
- 🔗 **Se estudia junto con:** aceleración gravitatoria, órbita circular, período, energía específica.

📘 **Dónde se aprende:** [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md).

### GMST

- **Significa:** tiempo sidéreo de Greenwich (GMST).
- El tiempo sidéreo de Greenwich (GMST) es el TSL en longitud 0°;

💡 **Contexto en la clase [B08-C05](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md):**
- **Idea central (modelo mental):** La Tierra gira 360° respecto de las estrellas en un día sidéreo. Pero también avanza por su órbita, y para que el Sol vuelva al meridiano debe girar un poco más: casi 1° más. Ese 1° de giro extra toma unos 4 min.
- 🎯 **Por qué importa:** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.
- 🔗 **Se estudia junto con:** día solar, día solar medio, día sidéreo, tiempo sidéreo local (TSL).

📘 **Dónde se aprende:** [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md).

### GP

- Una TLE (*two-line element set*) es un formato de dos líneas con elementos medios. GP son los elementos de perturbaciones generales;

💡 **Contexto en la clase [B118-C02](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md):**
- 🎯 **Por qué importa:** Sin un catálogo no hay conjunciones: cada alerta empieza identificando de qué objeto habla. Los formatos antiguos tienen límites de tamaño y la asociación de observaciones puede equivocarse.
- 🔗 **Se estudia junto con:** catálogo, TLE, OMM, Alpha-5.

📘 **Dónde se aprende:** [B118-C02 · Catálogos de objetos espaciales](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md).

### GPHS

- El GPHS es el módulo que aloja el combustible y aporta `250 W` térmicos.

💡 **Contexto en la clase [B86-C16](../programa/clases/B86/B86-C16-generadores-radioisotopicos/CLASE.md):**
- 🎯 **Por qué importa:** Un generador radioisotópico no depende de la distancia al Sol ni del eclipse, pero su potencia decae con el combustible y con los termopares y su eficiencia es baja. Entender esa curva decide qué misiones lo usan.
- 🔗 **Se estudia junto con:** RTG, vida media, degradación del termopar, eficiencia de sistema.

📘 **Dónde se aprende:** [B86-C16 · Generadores radioisotópicos](../programa/clases/B86/B86-C16-generadores-radioisotopicos/CLASE.md).

### GPU

- Una GPU es un procesador con miles de unidades simples que ejecutan la misma operación sobre muchos datos.

💡 **Cómo se explica en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- Si una GPU usa FMA y la CPU no, sus resultados diferirán aunque ambas sean correctas (S1).
- La GPU suele usarse en `float32` por velocidad y memoria.
- ⚠️ **Error frecuente:** Concluir que la GPU «se equivoca». Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?
- 🔗 **Se estudia junto con:** transferencia, intensidad aritmética, reducción, reducción en árbol.

📘 **Dónde se aprende:** [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md).

### GRS80

- Un elipsoide es una figura matemática de la Tierra con semieje mayor `a` y aplanamiento `f`. GRS80 es el elipsoide con `a = 6 378 137 m` y `1/f = 298,257 222 101` (S1, Tabla 1.2).

💡 **Cómo se explica en la clase [B13-C11](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md):**
- Un punto fijo en el sistema terrestre se mueve respecto del cielo con `v = ω √(X² + Y²)`, con `ω = 7,292 115 × 10⁻⁵ rad/s` (valor nominal de GRS80, S1 Tabla 1.2).
- Convertir latitud, longitud y altura geodésicas a X, Y, Z con GRS80.
- 🎯 **Por qué importa:** Una estación terrestre transmite a un satélite; el software de seguimiento necesita su posición en X, Y, Z. El técnico de campo tiene su posición en latitud, longitud y altura.
- 🔗 **Se estudia junto con:** sistema de referencia terrestre geocéntrico (GTRS), Sistema Internacional de Referencia Terrestre (ITRS), realización, ITRF.

📘 **Dónde se aprende:** [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### GSD

- **Significa:** Tamaño de pixel en el objeto (GSD).
- El GSD es el tamaño de píxel proyectado `H p/f`.
- El GSD (*ground sampling distance*) es la distancia en el suelo entre centros de píxeles contiguos.
- El GSD (*ground sample distance*) es el tamaño sobre el terreno que cubre un píxel.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B47-C25](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md):**
- Paso 2 · Fórmula. `GSD = h p/f = 5 × 10⁵ × 3,45 × 10⁻⁶/0,10`.
- Con la cámara ilustrativa (`h = 500 km`, píxel 3,45 µm, focal 0,10 m) el GSD es `17,25 m` y la franja `35,3 km`.
- 🎯 **Por qué importa:** Muchos CubeSat universitarios fracasan por requisitos sin cifra o sin evidencia. La decisión central: ¿qué requisitos medibles se fijan, cómo se verifican y cuáles cumple un diseño preliminar?
- 🔗 **Se estudia junto con:** carga útil, CubeSat 3U, parámetro Q = λF/p, profundidad de descarga.

📘 **Dónde se aprende:** [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md); [B53-C25 · Corrección geométrica y ortorrectificación de imágenes planetarias](../programa/clases/B53/B53-C25-correccion-geometrica-y-ortorrectificacion-de-imagenes-planetarias/CLASE.md); [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md); [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md); [B101-C09 · Coordinación visual y cámaras en operaciones con manipulador](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md) y 1 más.

### G/T

- La pérdida de espacio libre `FSPL` viene de C04. `G/T` es `G_r − 10 log₁₀ T_sis` (dB/K).
- La temperatura de sistema es `T_sis = T_ant + T_rx`. `G/T` es `G_r − 10 log₁₀ T_sis`.
- Margen: `Eb/N₀` disponible menos requerido. `G/T`: ganancia sobre temperatura de ruido.

💡 **Cómo se explica en la clase [B89-C05](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md):**
- PIRE --> CN0["C/N0 = PIRE - L + G/T - 10 log k"]
- *Descripción textual:* la PIRE, las pérdidas y `G/T` dan `C/N0`; restando la tasa de bits se obtiene `Eb/N0`; comparado con el valor requerido, el margen.
- 🎯 **Por qué importa:** El presupuesto de enlace es el documento donde se decide si una misión puede transmitir; un error de 3 dB equivale a duplicar la potencia o el tamaño de la antena. La decisión central: ¿cuánto margen queda y qué tasa de datos máxima admite este enlace?
- 🔗 **Se estudia junto con:** PIRE, pérdida de espacio libre, C/N0 = PIRE − L_total + G/T − 10 log₁₀ k, Eb/N0 = C/N0 − 10 log₁₀ R_b.

📘 **Dónde se aprende:** [B89-C05 · Presupuesto de enlace](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md); [B89-C07 · Figura de ruido de receptor](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md); [B96-C27 · Operación de equipos de radiofrecuencia en la estación](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md).

### GTRS

- **Significa:** sistema de referencia terrestre geocéntrico (GTRS).
- Un sistema de referencia terrestre geocéntrico (GTRS) tiene su origen en el centro de masas de toda la Tierra, incluidos océanos y atmósfera, y gira con ella (S1, §4.1.4).

💡 **Contexto en la clase [B13-C11](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md):**
- **Idea central (modelo mental):** Un punto se puede nombrar de dos modos equivalentes: por dónde está sobre el elipsoide y a qué altura (φ, λ, h) o por tres distancias a lo largo de ejes fijados a la Tierra (X, Y, Z). La conversión es una función exacta entre ambos modos, una vez fijado el elipsoide.
- 🎯 **Por qué importa:** Una estación terrestre transmite a un satélite; el software de seguimiento necesita su posición en X, Y, Z. El técnico de campo tiene su posición en latitud, longitud y altura.
- 🔗 **Se estudia junto con:** Sistema Internacional de Referencia Terrestre (ITRS), realización, ITRF, elipsoide.

📘 **Dónde se aprende:** [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### HAL

- La HAL es la interfaz.

💡 **Cómo se explica en la clase [B88-C24](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md):**
- APP["Aplicacion: enviar_paquete"] --> HAL["Interfaz HAL"]
- HAL --> R["Controlador de registros (FIFO 4)"]
- ⚠️ **Error frecuente:** Escribir registros en la aplicación. Usa la HAL (8.1)
- 🎯 **Por qué importa:** Si la aplicación toca registros, no se puede probar sin el hardware y cada cambio de componente la rompe. La decisión central: ¿qué interfaz mínima expone el dispositivo para que la aplicación no dependa de él?
- 🔗 **Se estudia junto con:** controlador, mock, reintento, tiempo límite.

📘 **Dónde se aprende:** [B88-C24 · Capa de abstracción de hardware (HAL) y controladores](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md).

### HAZID

- El HAZID identifica peligros con palabras guía sobre nodos.

💡 **Cómo se explica en la clase [B83-C21](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md):**
- Un HAZID real recorre todas las celdas y descarta las no aplicables con justificación.
- El HAZID sintético recorre 6 nodos con 7 palabras guía (42 celdas) y registra 12 peligros (28,6 % de las celdas): 0 altos, 8 medios y 4 bajos.
- ⚠️ **Error frecuente:** Mezclar HAZID con FMEA. El HAZID identifica peligros del sistema; el FMEA, modos de fallo de componentes
- 🎯 **Por qué importa:** Los peligros que no se identifican no se pueden controlar. La decisión central: ¿qué puede salir mal en cada fase, qué tan grave y probable es, y el riesgo para terceros cabe en el umbral que el proyecto adoptó?
- 🔗 **Se estudia junto con:** peligro, riesgo, índice, esperanza de bajas.

📘 **Dónde se aprende:** [B83-C21 · Identificación de peligros en sistemas de lanzamiento (HAZID)](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md).

### HDOP

- El DOP (*dilution of precision*) amplifica el error: `PDOP = √(Q₁₁+Q₂₂+Q₃₃)` con `Q = (GᵀG)⁻¹`. HDOP y VDOP separan lo horizontal de lo vertical.

💡 **Cómo se explica en la clase [B57-C10](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md):**
- Calcular HDOP, VDOP, PDOP y TDOP desde la matriz de geometría.
- Ejercicio 6. ¿Qué mide el VDOP frente al HDOP?
- 🎯 **Por qué importa:** La geodesia con GNSS mide posiciones de estaciones con precisión de milímetros a centímetros y sirve para ver cómo se mueve la corteza. Pero la precisión depende de la geometría de los satélites.
- 🔗 **Se estudia junto con:** pseudodistancia, matriz de geometría, DOP, VDOP.

📘 **Dónde se aprende:** [B57-C10 · Geodesia mediante GNSS](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md).

### HDU

- Un HDU (*Header Data Unit*) es una unidad formada por un encabezado y, normalmente, un bloque de datos; el primero del archivo es el HDU primario.
- Una HDU es una unidad de cabecera y datos.

💡 **Cómo se explica en la clase [B14-C06](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md):**
- Describir la estructura de un archivo FITS (bloques, HDU, encabezado, datos).
- (`info()` también imprime una tabla del HDU con la ruta temporal, que no se reproduce aquí.)
- 🎯 **Por qué importa:** Una imagen astronómica es una matriz de números, pero esos números no significan nada sin su encabezado: ¿qué unidad tienen?, ¿cuánto duró la exposición?, ¿a qué punto del cielo apunta el píxel central? Si el encabezado miente o se pierde, la imagen no sirve.
- 🔗 **Se estudia junto con:** HDU primario, encabezado, tarjetas, WCS.

📘 **Dónde se aprende:** [B14-C06 · Formato FITS y encabezados](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md); [B44-C19 · Formato FITS y metadatos](../programa/clases/B44/B44-C19-formato-fits-y-metadatos/CLASE.md).

### HEPA

- Aerosol: partículas en suspensión. HEPA: filtro de alta eficiencia.

💡 **Cómo se explica en la clase [B106-C23](../programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/CLASE.md):**
- ⚠️ **Error frecuente:** Tomar la definición de HEPA como consultada. Es de manual.
- 🎯 **Por qué importa:** En 1 g las partículas grandes caen al suelo; en microgravedad no, y en gravedad parcial caen más despacio. La decisión central: ¿qué eficiencia de filtro y qué caudal limpian la cabina en un tiempo dado según la gravedad y el tamaño?
- 🔗 **Se estudia junto con:** Velocidad de Stokes, Aerosol, Cambios de aire por hora, Polvo respirable.

📘 **Dónde se aprende:** [B106-C23 · Control de partículas y polvo respirable en cabina](../programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/CLASE.md).

### HFD

- HFD: diámetro de media energía de una estrella.

💡 **Cómo se explica en la clase [B48-C22](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md):**
- Con ruido de 0,15 µm en cada HFD y 4000 repeticiones, la media del mínimo es 1233,999 pasos y la desviación 0,104 pasos (error estándar 0,0016).
- Ajustar el cuadrado del HFD da un estimador sin sesgo apreciable.
- ⚠️ **Error frecuente:** Ajustar una recta al HFD. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un enfoque erróneo pierde resolución en todas las imágenes de la noche. La decisión central: ¿en qué posición del enfocador está el mínimo y con qué incertidumbre?
- 🔗 **Se estudia junto con:** Curva en V, Enfocador, Número f, Ecuaciones normales.

📘 **Dónde se aprende:** [B48-C22 · Control automático del enfocador y autoenfoque](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md).

### HHI

- El HHI es la suma de los cuadrados de las cuotas en %, entre 0 y 10 000.
- El HHI es la suma de cuotas al cuadrado (aquí en puntos, de 0 a 10 000).

💡 **Cómo se explica en la clase [B122-C01](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md):**
- *Descripción textual:* los proveedores abastecen componentes y estos sostienen servicios; del reparto sale el HHI y de la estructura la indisponibilidad con uno o varios proveedores.
- Calcular el HHI de las cuotas de compra de un componente.
- ⚠️ **Error frecuente:** Confundir HHI con la suma de cuotas. Se corrige con 8.1.
- 🎯 **Por qué importa:** B119-C16 solo introduce la infraestructura crítica y no analiza de quién depende. La decisión central: ¿qué proveedor, si cae, daña más servicios, y cuánto baja el riesgo si hay una segunda fuente?
- 🔗 **Se estudia junto con:** concentración, monoabastecimiento, punto único de falla, cadena de suministro.

📘 **Dónde se aprende:** [B122-C01 · Dependencias de proveedores y cadena de suministro de infraestructura espacial](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md); [B124-C03 · Mercados downstream y upstream](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md).

### HIL

- PIL: en el procesador objetivo o en un modelo de su aritmética. HIL: con el hardware real conectado (C19).

💡 **Cómo se explica en la clase [B88-C41](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md):**
- Ejercicio 7 · autónomo. ¿Qué error de otro tipo detecta HIL y no PIL?
- ⚠️ **Error frecuente:** Creer que SIL basta. Hace falta PIL y HIL (8.4)
- 🎯 **Por qué importa:** La aritmética del procesador objetivo puede ser distinta de la del escritorio. La decisión central: ¿cuánto se aparta la respuesta con la precisión del objetivo y cumple la tolerancia?
- 🔗 **Se estudia junto con:** SIL, PIL, épsilon, LSB.

📘 **Dónde se aprende:** [B88-C41 · Pruebas SIL y PIL del software de vuelo](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md).

### HITRAN

- CDMS (Cologne Database for Molecular Spectroscopy) y JPL son catálogos de líneas milimétricas y submilimétricas. HITRAN reúne parámetros por línea para atmósferas y astrofísica, con intensidad en cm⁻¹/(molécula·cm⁻²) a 296 K.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- Para cada banco hay que citar la versión y la fecha de consulta; la portada de HITRAN consultada anuncia HITRAN2024 y recomienda indicar la versión usada.
- L --> HT["HITRAN: ν, S(296 K), γ_air, n_air"]
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.
- 🔗 **Se estudia junto con:** banco de datos espectroscópicos, CDMS, JPL, LAMDA.

📘 **Dónde se aprende:** [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### IA

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- Ejercicio 3 · casi autónomo. Error de `IA` ajustado frente al verdadero.
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?
- 🔗 **Se estudia junto con:** términos, IE, CA, NPAE.

📘 **Dónde se aprende:** [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### IAE

- El IAE es `∫|r − y| dt`, un resumen de la calidad de la respuesta.

💡 **Cómo se explica en la clase [B16-C12](../programa/clases/B16/B16-C12-sintonia-de-controladores-pid/CLASE.md):**
- La respuesta al escalón de este lazo, con filtro derivativo `N = 10`, da un sobreimpulso de 42,7 %, un asentamiento (2 %) de 9,19 y un IAE de 1,76.
- Reducir `Kp` a la mitad (2,4) con los mismos `Ti` y `Td` baja el sobreimpulso a 26,4 % y el asentamiento a 7,85, con un IAE de 1,85 (algo peor).
- ⚠️ **Error frecuente:** Creer que un IAE menor es siempre mejor. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** En un proyecto real, las ganancias iniciales de un lazo se eligen con pocas medidas y bajo presión de calendario: a veces no hay un modelo preciso. Hay reglas que solo piden hacer oscilar el lazo con un controlador proporcional y medir dos números.
- 🔗 **Se estudia junto con:** ganancia última, periodo último, regla de lazo cerrado de Ziegler–Nichols, colocación de polos.

📘 **Dónde se aprende:** [B16-C12 · Sintonía de controladores PID](../programa/clases/B16/B16-C12-sintonia-de-controladores-pid/CLASE.md).

### IAWN

- IAWN es la red internacional de alerta de asteroides, coordinada por NASA, creada por recomendación de un grupo de trabajo de la ONU [S7].

💡 **Cómo se explica en la clase [B58-C18](../programa/clases/B58/B58-C18-marco-internacional-de-defensa-planetaria/CLASE.md):**
- Según [S7], IAWN es una colaboración mundial de astrónomos y modeladores coordinada por NASA, establecida por recomendación del grupo de trabajo sobre objetos cercanos a la Tierra de la subcomisión científica de la COPUOS, endosada en febrero de 2013 y reconocida por la Asamblea General de la ONU.
- Describir qué son IAWN y SMPAG según la fuente consultada.
- ⚠️ **Error frecuente:** Atribuir a IAWN la decisión de desviar. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un umbral de notificación decide cuántos casos entran en el circuito internacional y cuántos tienen tiempo suficiente. La decisión central: ¿qué umbral activa la alerta y qué margen de tiempo deja para actuar?
- 🔗 **Se estudia junto con:** SMPAG, notificación, tiempo de aviso.

📘 **Dónde se aprende:** [B58-C18 · Marco internacional de defensa planetaria](../programa/clases/B58/B58-C18-marco-internacional-de-defensa-planetaria/CLASE.md).

### ICD

- El ICD es el contrato entre productor y consumidor.
- Un ICD (*interface control document*) lo especifica.
- ICD: documento de control de interfaces.

💡 **Cómo se explica en la clase [B83-C08](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md):**
- I["Interfaz"] --> P["Parametros del ICD"]
- Ejercicio 8 · autónomo. ¿Por qué conviene un caso más desfavorable en el ICD?
- 🎯 **Por qué importa:** La mayoría de los fallos de integración aparecen en las interfaces: un conector mal definido, una tensión fuera de rango o una tasa de datos insuficiente. La decisión central: ¿cada interfaz cumple en su caso más desfavorable, con margen, antes de construir?
- 🔗 **Se estudia junto con:** interfaz, caída de tensión, rango de la carga, margen de datos.

📘 **Dónde se aprende:** [B83-C08 · Interfaz entre subsistemas](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md); [B88-C21 · Interfaces y documentos de control de software de vuelo](../programa/clases/B88/B88-C21-interfaces-y-documentos-de-control-de-software-de-vuelo/CLASE.md); [B90-C05 · Documentación de interfaces](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md).

### ICM

- **Significa:** medio intracúmulo (ICM).
- El medio intracúmulo (ICM) es ese gas caliente, ionizado, que emite en rayos X.

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- Definir cúmulo de galaxias, medio intracúmulo, equilibrio hidrostático y perfil beta.
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.
- 🔗 **Se estudia junto con:** cúmulo de galaxias, temperatura, equilibrio hidrostático, perfil beta.

📘 **Dónde se aprende:** [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md).

### ICRF

- **Significa:** Marco Celeste de Referencia Internacional (ICRF).
- El Marco Celeste de Referencia Internacional (ICRF) es su realización: un conjunto de coordenadas precisas de fuentes extragalácticas compactas de radio, medidas con interferometría de línea de base muy larga (VLBI) (S1, 2.2).

💡 **Contexto en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
- **Idea central (modelo mental):** Imagina fijar un mapa a las fuentes más lejanas, que casi no se mueven. Las coordenadas de cada cuásar son las marcas del mapa; los ejes salen de ellas. Cualquier dirección que midas es relativa a esas marcas; cualquier error común de las marcas es un giro de todo el mapa.
- 🎯 **Por qué importa:** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.
- 🔗 **Se estudia junto con:** Sistema Celeste de Referencia Internacional (ICRS), fuente definidora, cuásar, suelo de ruido.

📘 **Dónde se aprende:** [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### ICRS

- **Significa:** Sistema Celeste de Referencia Internacional (ICRS).
- El ICRS es el sistema de referencia celeste de la IAU, que realiza el ecuatorial en la práctica.
- El Sistema Celeste de Referencia Internacional (ICRS) es un sistema cinemático: sus ejes tienen direcciones fijas respecto de la materia distante del universo, con origen en el baricentro del sistema solar; sustituyó oficialmente al sistema FK5 el 1 de enero de 1998 (S1, cap. 2).

💡 **Cómo se explica en la clase [B04-C19](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md):**
- Su límite: los sistemas aquí tratados son fijos en el ICRS; en cuanto el sistema depende del tiempo (precesión) o del observador, se necesitan más piezas.
- Depende de que `(α, δ)` esté en el marco ICRS (hipótesis didáctica: la documentación del archivo no declara el marco) y no incluye movimiento propio.
- 🎯 **Por qué importa:** Un catálogo da las posiciones en ecuatoriales; un estudio de la Vía Láctea necesita galácticas; un análisis del plano del sistema solar usa eclípticas. Cambiar de sistema es rutina, y un error de signo o de matriz mueve el objeto decenas de grados.
- 🔗 **Se estudia junto con:** sistema de coordenadas esféricas, polo, círculo fundamental, origen de longitud.

📘 **Dónde se aprende:** [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md); [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### IE

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?
- 🔗 **Se estudia junto con:** términos, IA, CA, NPAE.

📘 **Dónde se aprende:** [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### IFOV

- El IFOV es el ángulo que subtiende un píxel visto desde el sensor.
- El IFOV es `atan(1/f)`.
- El IFOV es el ángulo que ve un píxel.

💡 **Cómo se explica en la clase [B57-C02](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md):**
- Con `H = 705 km` y `GSD = 30 m`, `IFOV = 42,553 µrad`.
- *Descripción textual:* la altitud y el IFOV fijan el GSD; de él salen los píxeles por línea, el límite de Nyquist y el volumen, mientras el ciclo fija las imágenes por año.
- 🎯 **Por qué importa:** Un satélite con píxeles de 30 m no ve una casa y uno que vuelve cada 16 días no ve una tormenta. La decisión central: ¿qué tamaño de píxel, qué ancho de barrido y qué ciclo de repetición necesita el fenómeno que quiero estudiar?
- 🔗 **Se estudia junto con:** GSD, barrido, resolución temporal, ciclo de repetición.

📘 **Dónde se aprende:** [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md); [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md); [B121-C02 · Licenciamiento de actividades de teledetección](../programa/clases/B121/B121-C02-licenciamiento-de-actividades-de-teledeteccion/CLASE.md).

### IGRF

- El IGRF es el modelo estándar de grado 13 que se usaría en lugar del dipolo.

💡 **Cómo se explica en la clase [B87-C05](../programa/clases/B87/B87-C05-magnetometros/CLASE.md):**
- Y el IGRF (S1) del que saldría el campo de referencia tiene su propio error y se actualiza cada cinco años; aquí el modelo dipolar es sintético y el sensor ve exactamente ese modelo, por lo que no aparece error de modelo.
- IGRF de grado 13: el modelo de referencia real (consultado solo en su descripción).
- ⚠️ **Error frecuente:** Usar el dipolo como si fuese el IGRF. Declara qué modelo usas y su error (8.4)
- 🎯 **Por qué importa:** Un cubesat sin sensores estelares usa el campo magnético para saber hacia dónde apunta y para detumbling (C16). La decisión central: ¿cuánto varía el campo a lo largo de la órbita, cuánto ruido y sesgo tolera la dirección medida y qué parte de la actitud no ve el magnetómetro?
- 🔗 **Se estudia junto con:** campo dipolar, inclinación del dipolo, ruido, sesgo.

📘 **Dónde se aprende:** [B87-C05 · Magnetómetros](../programa/clases/B87/B87-C05-magnetometros/CLASE.md).

### IIR

- Un filtro IIR (respuesta infinita) reutiliza salidas anteriores, como `y[n] = α x[n] + (1 − α) y[n − 1]` (S2 escribe la forma general).

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- Un IIR suele retrasar de forma desigual según la frecuencia pero necesita pocos coeficientes.
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.
- 🔗 **Se estudia junto con:** filtro digital, lineal, invariante, FIR.

📘 **Dónde se aprende:** [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### IK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- Por tipo: SPK, CK, PCK, IK, FK, LSK, SCLK.
- Un CK (actitud de la nave) junto con IK y FK.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, CK, PCK.

📘 **Dónde se aprende:** [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### IMF

- La IMF `ξ(m) = dN/dm`.

💡 **Cómo se explica en la clase [B38-C02](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md):**
- Un cúmulo de 50 estrellas por encima de 1 M☉ da una pendiente con ±0,18 solo por azar: diferencias de ese tamaño entre cúmulos no prueban una IMF distinta.
- Límite: la misma IMF para todas las muestras y estrellas independientes.
- 🎯 **Por qué importa:** Casi todo lo que se infiere de una población (luminosidad, supernovas, masa) depende de la IMF. La decisión central: ¿cuándo una diferencia de pendiente entre dos muestras es real y cuándo es ruido de Poisson?
- 🔗 **Se estudia junto con:** índice, corte, máxima verosimilitud, ruido de Poisson.

📘 **Dónde se aprende:** [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md).

### IMM

- El IMM es el modelo probabilístico de riesgo médico de la NASA.

💡 **Cómo se explica en la clase [B117-C05](../programa/clases/B117/B117-C05-inventario-y-gestion-del-equipo-medico-a-bordo/CLASE.md):**
- Separar lo consultado (el concepto del IMM de la NASA) de lo ilustrativo (todos los artículos y números).
- Datos: solo el concepto del IMM consultado; artículos, tasas, pesos y límites ilustrativos.
- 🎯 **Por qué importa:** Ninguna clase anterior trata el equipo médico de a bordo. La decisión central: ¿qué embarcar bajo un límite de masa y volumen y qué riesgo de quedarse sin él se acepta?
- 🔗 **Se estudia junto con:** demanda, tasa, beneficio, desabastecimiento.

📘 **Dónde se aprende:** [B117-C05 · Inventario y gestión del equipo médico a bordo](../programa/clases/B117/B117-C05-inventario-y-gestion-del-equipo-medico-a-bordo/CLASE.md).

### I/N

- Piso de ruido: `k T B`. I/N: relación interferencia a ruido.

💡 **Cómo se explica en la clase [B90-C14](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md):**
- Con `I/N = −6 dB` la degradación es de solo 1 dB; con `I/N = 0 dB`, 3 dB.
- Para `I/N = −6 dB`, `I ≤ N − 6 = −137,6 dBm`, así que hacen falta `−30 − (−137,6) = 107,6 dB`.
- 🎯 **Por qué importa:** Un transmisor de 1 W deja un armónico de −30 dBm; el piso de ruido de un receptor estrecho está cerca de −132 dBm. La diferencia de más de 100 dB se pierde con facilidad en un chasis de 10 cm.
- 🔗 **Se estudia junto con:** EMI, Fuente y víctima, Piso de ruido, Desensibilización.

📘 **Dónde se aprende:** [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md).

### IP

- **Significa:** Producto iónico (IP).
- Orina pretratada: orina con aditivos que estabilizan. Producto iónico (IP): `[Ca][SO₄]`.

💡 **Cómo se explica en la clase [B106-C27](../programa/clases/B106/B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md):**
- Si la fracción recuperada es `r`, el residuo se concentra `CF = 1/(1 − r)` veces y el producto iónico crece `CF²`.
- *Descripción textual:* la destilación recupera agua y concentra la salmuera; si el producto iónico supera el de solubilidad, la sal precipita y obstruye; una segunda etapa trata la salmuera.
- 🎯 **Por qué importa:** Evaporar la orina concentra sales hasta que precipitan y obstruyen el equipo; el límite lo fija la química, no la termodinámica del agua. La decisión central: ¿hasta qué fracción se puede recuperar el agua antes de precipitar y cómo se supera ese límite?
- 🔗 **Se estudia junto con:** Orina pretratada, K_sp, Salmuera, Compresión de vapor.

📘 **Dónde se aprende:** [B106-C27 · Tratamiento de orina y recuperación de agua](../programa/clases/B106/B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md).

### I/Q

- Las muestras I/Q son la parte real e imaginaria de la señal en banda base.

💡 **Cómo se explica en la clase [B46-C10](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md):**
- Un SDR real tiene pico de continua, desbalance I/Q, ganancia inestable y espurios que el laboratorio no modela.
- IQ["muestras I/Q"] --> W["ventana de Hann"]
- 🎯 **Por qué importa:** Promediar espectros es la forma práctica de aplicar la ecuación del radiómetro con un instrumento barato, pero la ventana cambia el ancho de banda efectivo. La decisión central: ¿cuántos espectros promediar para detectar una línea débil?
- 🔗 **Se estudia junto con:** FFT, ventana de Hann, ENBW, promediado.

📘 **Dónde se aprende:** [B46-C10 · Radioastronomía mediante SDR](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md).

### ISCO

- **Significa:** órbita circular estable más interna (ISCO).
- La órbita circular estable más interna (ISCO) es la más próxima al agujero con órbita estable; en un agujero sin rotación está en `r = 6GM/c²`.
- El ISCO es la órbita circular estable más interna.

💡 **Cómo se explica en la clase [B27-C07](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md):**
- El ISCO es el radio donde `E(r)` es mínimo.
- Con espín prógrado crece la energía liberable y el ISCO baja: `4,2330` (`a = 0,5`), `2,3209` (`0,9`), `1,2370` (`0,998`).
- 🎯 **Por qué importa:** El espín cambia el ISCO y, con él, cuánta energía se libera: de `5,7 %` a más de `30 %` de la masa en reposo. La decisión central: ¿dónde están el horizonte y el ISCO para un espín dado y qué eficiencia implica?
- 🔗 **Se estudia junto con:** radio gravitacional, horizonte de sucesos, espín, órbita prógrada.

📘 **Dónde se aprende:** [B25-C11 · Núcleos activos de galaxias](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md); [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md).

### ISO

- La exposición es el tiempo con el obturador abierto; el ISO es la amplificación de la señal; la apertura relativa del objetivo (f/) controla la luz.

💡 **Cómo se explica en la clase [B08-C19](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md):**
- Ejercicio 12 · integrador. Elabora la ficha de una fotografía: objeto, UT, lugar, cámara y objetivo (con focal y píxel), exposición e ISO, escala, campo y estela calculadas, estado de la imagen (original o procesada), y limitaciones.
- 🎯 **Por qué importa:** Un teléfono o una cámara réflex puede captar la Vía Láctea o la Luna con detalle, pero una exposición demasiado larga convierte las estrellas en rayas. La pregunta motivadora: ¿cuánto puedo exponer y con qué focal para obtener estrellas puntuales, y qué debo anotar para que la foto sirva como dato?
- 🔗 **Se estudia junto con:** distancia focal, tamaño del píxel, escala de placa, campo.

📘 **Dónde se aprende:** [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md).

### ISRU

- **Significa:** utilización de recursos in situ (ISRU).
- La utilización de recursos in situ (ISRU) es el aprovechamiento de los recursos naturales locales del destino, según la definición que usa NASA (S2).

💡 **Cómo se explica en la clase [B59-C01](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md):**
- python programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/apalancamiento.py
- 🎯 **Por qué importa:** Cada kilogramo que se lanza arrastra consigo más propelente para lanzarlo. La decisión central: ¿cuánta masa de planta de producción compensa el oxidante que dejas de llevar?
- 🔗 **Se estudia junto con:** propelente, razón O/F, apalancamiento, masa de equilibrio.

📘 **Dónde se aprende:** [B59-C01 · Concepto de utilización de recursos in situ](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md).

### ISW

- El ISW surge de `dΦ/dη ≠ 0`.

💡 **Cómo se explica en la clase [B40-C09](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md):**
- *Descripción textual:* la integral de Bessel da la meseta de SW; la caída de los potenciales por Λ fija el ISW.
- Descripción larga: los potenciales decaen un 21 % y el ISW se opone a SW.
- ⚠️ **Error frecuente:** Tomar la cota como el ISW real. Se corrige con 8.3.
- 🎯 **Por qué importa:** SW domina las escalas grandes; el ISW es una señal de la energía oscura. La decisión central: ¿qué amplitud tiene la meseta y cuánto decaen los potenciales?
- 🔗 **Se estudia junto con:** potencial, factor de crecimiento, función de Bessel esférica.

📘 **Dónde se aprende:** [B40-C09 · Efecto Sachs-Wolfe y efecto Sachs-Wolfe integrado](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md).

### ITRF

- Una realización del ITRS se llama ITRF (*International Terrestrial Reference Frame*): coordenadas y velocidades de estaciones que materializan el sistema (S1, §4.1.5).

💡 **Cómo se explica en la clase [B13-C11](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md):**
- Explicar qué es el ITRS y qué es una realización (ITRF).
- 🎯 **Por qué importa:** Una estación terrestre transmite a un satélite; el software de seguimiento necesita su posición en X, Y, Z. El técnico de campo tiene su posición en latitud, longitud y altura.
- 🔗 **Se estudia junto con:** sistema de referencia terrestre geocéntrico (GTRS), Sistema Internacional de Referencia Terrestre (ITRS), realización, elipsoide.

📘 **Dónde se aprende:** [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### ITRS

- **Significa:** Sistema Internacional de Referencia Terrestre (ITRS).
- El GCRS (sistema celeste geocéntrico) y el ITRS (sistema terrestre internacional) son sistemas de referencia; el IERS los relaciona con `[GCRS] = Q(t) R(t) W(t) [ITRS]`, donde `Q` es el movimiento del polo celeste, `R` la rotación de la Tierra alrededor del eje del polo y `W` el movimiento polar (S1, ec. 5.1).
- El Sistema Internacional de Referencia Terrestre (ITRS) es el GTRS específico definido por el IERS con cuatro condiciones: es geocéntrico; su unidad de longitud es el metro SI y su escala es coherente con TCG; su orientación inicial es la del BIH en 1984,0; y su evolución temporal no tiene rotación neta respecto de los movimientos tectónicos horizontales (S1, §4.1.4).

💡 **Cómo se explica en la clase [B10-C16](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md):**
- A["ITRS<br/>(fijo a la Tierra)"] -->|"W: movimiento polar<br/>(omitido aquí)"| B["Marco intermedio"]
- Escribir la cadena `[GCRS] = Q(t) R(t) W(t) [ITRS]` y reconocer qué parte se calcula aquí.
- 🎯 **Por qué importa:** Una estación terrestre tiene coordenadas fijas en la Tierra. Un satélite se propaga en un sistema inercial, donde las leyes de Newton valen.
- 🔗 **Se estudia junto con:** marco de referencia, inercial, GCRS, ángulo de rotación terrestre.

📘 **Dónde se aprende:** [B10-C16 · Transformación de marcos de referencia](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md); [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### J2

- Un armónico zonal `J_n` es el coeficiente de un término que solo depende de la latitud. J2 mide el achatamiento dinámico.
- El J2 causa la precesión de la línea de nodos.

💡 **Cómo se explica en la clase [B72-C02](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md):**
- La forma general con `n = 2` coincide con la fórmula cerrada de J2 en `0` (diferencia relativa exacta).
- J2 es unas `300` a `500` veces mayor que J3 y J4.
- ⚠️ **Error frecuente:** Creer que J2 es igual en todas las latitudes. Se corrige con 8.4.
- 🎯 **Por qué importa:** Sin un potencial no hay perturbación gravitatoria que calcular, y los números de la bibliografía (J2, J3, J4) dependen de un convenio de signos y de un radio de referencia. La decisión central: ¿qué términos del potencial incluir y con qué radio y convenio, para que J2 signifique lo mismo en tu código y en la fuente?
- 🔗 **Se estudia junto con:** armónico zonal, polinomio de Legendre, convenio de signos, gradiente.

📘 **Dónde se aprende:** [B72-C02 · Potencial gravitatorio no esférico](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md); [B74-C20 · Validación frente a efemérides de referencia](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md).

### J2000

- Una época es la fecha a la que se refieren las coordenadas; la precesión es el lento giro del eje de la Tierra, que desplaza el sistema entero unos 50″ al año. J2000 es la época del 1 de enero de 2000, 12:00 (D. juliano 2451545,0); el IAU la usa en los datos de límites de las constelaciones (S2).
- La anchura de ventana es el intervalo de fechas que cumple una tolerancia angular. J2000 es el origen de tiempos. «Oportunidad» y «ventana» se usan aquí como sinónimos.

💡 **Cómo se explica en la clase [B08-C03](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md):**
- La AR y la Dec de la tabla están en J2000.
- Para la Luna del 5 de noviembre de 2025 (25,8 años después de J2000), el laboratorio da un cambio de `1272″` en AR y `443″` en Dec: una separación de `0,360°`.
- 🎯 **Por qué importa:** Un catálogo no puede decir «a la izquierda de la Luna», porque eso cambia a cada minuto. Necesita direcciones fijas.
- 🔗 **Se estudia junto con:** declinación, ecuador celeste, ascensión recta, punto vernal.

📘 **Dónde se aprende:** [B08-C03 · Ascensión recta y declinación](../programa/clases/B08/B08-C03-ascension-recta-y-declinacion/CLASE.md); [B75-C03 · Ventanas de lanzamiento](../programa/clases/B75/B75-C03-ventanas-de-lanzamiento/CLASE.md).

### JD

- **Significa:** día juliano (JD).
- El día juliano (JD) es el número de días, con fracción, desde el mediodía de un origen remoto; el JD de J2000 es `2 451 545,0` (S2).

💡 **Cómo se explica en la clase [B13-C09](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md):**
- Convertir una fecha gregoriana en día juliano modificado (MJD) y viceversa.
- 🎯 **Por qué importa:** Una nave graba un evento a las `23:59:59` del 31 de diciembre de 2016 y otro a las `00:00:00` del 1 de enero de 2017. ¿Cuánto tiempo pasó?
- 🔗 **Se estudia junto con:** segundo intercalar, calendario gregoriano, día juliano modificado (MJD), cuenta continua.

📘 **Dónde se aprende:** [B13-C09 · Segundos intercalares y cronología](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md).

### JPL

- CDMS (Cologne Database for Molecular Spectroscopy) y JPL son catálogos de líneas milimétricas y submilimétricas.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- LAMDA da las energías de los niveles; la diferencia entre dos niveles debería reproducir la frecuencia de JPL.
- Las frecuencias de transición que LAMDA lista aparte (`230,5380000` y `345,7959899 GHz`) sí coinciden con JPL: la discrepancia está en la precisión de las energías de nivel, no en las frecuencias de línea.
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.
- 🔗 **Se estudia junto con:** banco de datos espectroscópicos, CDMS, HITRAN, LAMDA.

📘 **Dónde se aprende:** [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### JSON

- JSON es un formato de texto para intercambiar datos entre lenguajes; sus valores son objeto, arreglo, número, texto, `true`, `false` y `null` (S2, S3).

💡 **Cómo se explica en la clase [B07-C16](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md):**
- Las claves son siempre texto: `json.dumps({1: "a"})` da `{"1": "a"}`, y al leerlo vuelve `{'1': 'a'}` (S2).
- `json.dumps(obj, indent=2, ensure_ascii=False)` da una escritura legible con tildes.
- ⚠️ **Error frecuente:** Esperar comentarios en JSON. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** Una simulación tiene decenas de parámetros. Si están enterrados en el código, cambiar uno obliga a editar el programa y es fácil olvidar con qué valores se obtuvo cada resultado.
- 🔗 **Se estudia junto con:** YAML, sangría, comentario, Serializar.

📘 **Dónde se aprende:** [B07-C16 · Formatos JSON y YAML](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md).

### KKT

- Con desigualdad `T(x) ≤ T_max` aparecen las condiciones KKT: estacionariedad `∇Dv + μ ∇T = 0`; factibilidad `T ≤ T_max`;

💡 **Cómo se explica en la clase [B11-C23](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md):**
- KKT: `Δv′ + μ T′ = 0` ⇒ `μ = 7,67 × 10⁻⁵/25,47 = 3,01 × 10⁻⁶ > 0`.
- Tres pruebas: la restricción se cumple a la tolerancia; el gradiente del Lagrangiano se anula (residuo KKT `0` en el laboratorio); y un barrido independiente de la región factible no encuentra nada mejor.
- ⚠️ **Error frecuente:** Aceptar KKT sin barrido de comprobación. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Casi todo problema de diseño de trayectorias tiene límites: tiempo máximo, combustible disponible, distancia mínima a un cuerpo. Un optimizador que ignora las restricciones devuelve un resultado imposible; uno que las trata mal da un resultado que parece factible y no es óptimo.
- 🔗 **Se estudia junto con:** con restricción de igualdad, Lagrangiano, multiplicador de Lagrange, desigualdad.

📘 **Dónde se aprende:** [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md).

### KR-20

- La discriminación es la correlación entre acertar el ítem y el puntaje en los demás. KR-20 y el alfa de Cronbach miden la consistencia interna; para ítems dicotómicos coinciden.
- La discriminación `r` mide si quienes aciertan el ítem puntúan mejor en el resto. KR-20 estima la consistencia interna de una prueba de ítems dicotómicos.

💡 **Cómo se explica en la clase [B130-C05](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md):**
- KR-20 y el alfa de Cronbach dan ambos `0,7295` con diferencia `0` (menor que `1e-12`): son la misma cantidad calculada por dos vías.
- La fórmula de KR-20 no se consultó en una fuente concreta; la comprobación cruzada valida el código, no la fórmula.
- 🎯 **Por qué importa:** Saber si la divulgación funcionó exige medir la comprensión; ninguna otra clase lo trata. La decisión central: ¿qué número resume la mejora del público, y cuánto se puede confiar en que no sea azar?
- 🔗 **Se estudia junto con:** ganancia normalizada de un grupo, dificultad, discriminación, alfa de Cronbach.

📘 **Dónde se aprende:** [B130-C05 · Evaluación de la comprensión del público](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md); [B131-C08 · Evaluación formativa en el aula de astronomía](../programa/clases/B131/B131-C08-evaluacion-formativa-en-el-aula-de-astronomia/CLASE.md).

### KS

- **Significa:** prueba de Kolmogorov–Smirnov (KS).
- La prueba de Kolmogorov–Smirnov (KS) de dos muestras mide `D = máx |F₁(x) − F₂(x)|`, la mayor diferencia entre las distribuciones acumuladas empíricas.

💡 **Contexto en la clase [B17-C07](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md):**
- 🎯 **Por qué importa:** Un modelo se entrena con un catálogo y se despliega sobre otro: otro telescopio, otra época, otro brillo límite. Su exactitud medida en validación cruzada deja de valer, y el modelo no avisa: responde con la misma seguridad.
- 🔗 **Se estudia junto con:** distribución de entrenamiento, despliegue, cambio de covariables, cambio de prevalencia.

📘 **Dónde se aprende:** [B17-C07 · Validación fuera de distribución](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md).

### LAI

- El LAI (índice de área foliar) mide el follaje.

💡 **Cómo se explica en la clase [B57-C06](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md):**
- Entre `LAI 0` y `2` el NDVI gana `0,510`; entre `4` y `6`, solo `0,024`: eso es la saturación.
- Con `LAI = 1`, un suelo claro da `NDVI = 0,544` y uno oscuro `0,622`: diferencia `0,079`.
- 🎯 **Por qué importa:** Un índice facilita comparar fechas y lugares, pero también esconde supuestos. La decisión central: ¿cuándo el NDVI mide de verdad la cantidad de vegetación y cuándo lo engañan la saturación o el suelo?
- 🔗 **Se estudia junto con:** NDVI, SAVI, saturación, suelo de fondo.

📘 **Dónde se aprende:** [B57-C06 · Índices de vegetación](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md).

### LAL

- Los esquemas de datos se nombran LAL (lado–ángulo–lado), LLL (tres lados), ALA (ángulo–lado–ángulo) y LLA (lado–lado–ángulo no incluido).

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- *Descripción textual:* según los datos (LAL o LLL, ALA o LLA) se usa la ley de cosenos, el tercer ángulo y la de senos, o la de senos con posible ambigüedad; todo termina comprobando que los ángulos suman 180°.
- La ley de cosenos es la más segura: no tiene ambigüedad y sirve con LAL y LLL.
- ⚠️ **Error frecuente:** Usar la ley de senos con LAL. Se corrige con la sección 8.1 y el ejercicio 1.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.
- 🔗 **Se estudia junto con:** ley de cosenos, ley de senos, resuelve, LLL.

📘 **Dónde se aprende:** [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### LAMDA

- HITRAN reúne parámetros por línea para atmósferas y astrofísica, con intensidad en cm⁻¹/(molécula·cm⁻²) a 296 K. LAMDA (Leiden Atomic and Molecular Database) da niveles, pesos, coeficientes de Einstein y tasas de colisión para códigos de transferencia radiativa.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- LAMDA da las energías de los niveles; la diferencia entre dos niveles debería reproducir la frecuencia de JPL.
- Las frecuencias de transición que LAMDA lista aparte (`230,5380000` y `345,7959899 GHz`) sí coinciden con JPL: la discrepancia está en la precisión de las energías de nivel, no en las frecuencias de línea.
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.
- 🔗 **Se estudia junto con:** banco de datos espectroscópicos, CDMS, JPL, HITRAN.

📘 **Dónde se aprende:** [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### L-BFGS-B

- El escalado divide cada variable por un valor típico. L-BFGS-B es un método cuasi-Newton con cotas.

💡 **Cómo se explica en la clase [B81-C09](../programa/clases/B81/B81-C09-variables-de-diseno-orbital/CLASE.md):**
- Una explicación probable, que el laboratorio no verifica por separado: la derivada por diferencias finitas usa un paso absoluto pequeño; para `r_b ≈ 10⁹ km` el cambio de la función es del orden del redondeo y el gradiente se ve casi nulo, de modo que L-BFGS-B declara convergencia casi sin moverse.
- *Descripción textual:* las variables pueden pasar al optimizador tal cual o escaladas; el `Δv` total se minimiza con L-BFGS-B y se compara con una rejilla.
- 🎯 **Por qué importa:** Un optimizador que se detiene a la primera iteración no ha encontrado nada: puede ser un problema de escala y no de física. La decisión central: ¿qué variables elegir y cómo escalarlas para que el optimizador haga su trabajo?
- 🔗 **Se estudia junto con:** variables de diseño, escalado.

📘 **Dónde se aprende:** [B81-C09 · Variables de diseño orbital](../programa/clases/B81/B81-C09-variables-de-diseno-orbital/CLASE.md).

### LCOP

- **Significa:** costo nivelado (LCOP).
- El costo nivelado (LCOP) es `(CapEx·CRF + OpEx)/Q`.

💡 **Cómo se explica en la clase [B124-C24](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md):**
- *Descripción textual:* el equipo y su transporte forman el CapEx, que se convierte en anualidad y se suma al OpEx para dar el costo anual y el costo nivelado, que se verifica con valor actual y se compara con traer el producto.
- Descripción larga: el transporte domina el capital y la operación, y el costo nivelado es una pequeña fracción del de traer el producto, siempre que la producción llegue a lo planificado.
- 🎯 **Por qué importa:** B124 estima costos de misión, pero una instalación que opera años necesita separar el capital de la operación y ponerlos en una misma unidad. La decisión central: ¿a qué costo por kilogramo produce la instalación y desde qué producción conviene frente a traer el producto?
- 🔗 **Se estudia junto con:** CapEx, OpEx, factor de recuperación de capital, valor actual.

📘 **Dónde se aprende:** [B124-C24 · CapEx y OpEx de una instalación extraterrestre](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md).

### LDPC

- Un código LDPC (*low-density parity-check*) se define por una matriz de paridad `H` con pocos unos; una palabra es válida si `H·c = 0`.

💡 **Cómo se explica en la clase [B94-C01](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md):**
- Descripción larga: la corrección es todo o nada alrededor de `E`; el LDPC degrada con suavidad al subir el ruido y gasta más iteraciones.
- Describir un LDPC por su matriz de paridad y su decodificador iterativo, y separar el código de juguete del del estándar.
- ⚠️ **Error frecuente:** Presentar el LDPC de juguete como el del estándar. Se corrige con 8.5 y la sección 10.
- 🎯 **Por qué importa:** Un enlace profundo opera con relaciones señal-ruido bajas y no puede reenviar cada trama. La decisión central: ¿cuántos símbolos erróneos tolera una palabra de código, cuánta redundancia cuesta y qué ocurre cuando se supera esa capacidad?
- 🔗 **Se estudia junto con:** código RS(n, k), capacidad, polinomio generador, síndrome.

📘 **Dónde se aprende:** [B94-C01 · Códigos Reed-Solomon y LDPC](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md).

### LE90

- El LE90 es el error lineal al 90 %: el valor bajo el cual está el 90 % de los errores absolutos.

💡 **Cómo se explica en la clase [B57-C31](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md):**
- Con 200 000 errores gaussianos de `σ = 2 m`: RMSE `2,002`, NMAD `2,008` y LE90 `3,298` (teoría `1,645σ = 3,290`).
- Los atípicos inflan el RMSE y casi no mueven el NMAD ni el LE90: el RMSE es la métrica más frágil.
- ⚠️ **Error frecuente:** Mezclar LE90 y desviación estándar. Son métricas distintas (sección 6).
- 🎯 **Por qué importa:** Decir «el MDE tiene 4 m de error» sin definir la métrica ni los puntos de control no significa nada. La decisión central: ¿qué métrica y qué intervalo de confianza reporto para que mi validación sea comparable y honesta?
- 🔗 **Se estudia junto con:** sesgo (ME), RMSE, NMAD, punto de control.

📘 **Dónde se aprende:** [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md).

### LEOP

- Propiedad de seguridad: condición que siempre debe cumplirse. LEOP: fase de lanzamiento y primeras órbitas.

💡 **Cómo se explica en la clase [B96-C08](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md):**
- Búsqueda en anchura desde LEOP: SEGURO y COMISIONADO a 1 paso, NOMINAL a 2, CIENCIA, MANTENIMIENTO y DESORBITANDO a 3, FIN a 4.
- (3) El comando de ciencia solo vale en NOMINAL y CIENCIA: lo rechazan LEOP, SEGURO, COMISIONADO, MANTENIMIENTO, DESORBITANDO y FIN.
- 🎯 **Por qué importa:** Un comando válido en un estado puede ser peligroso en otro; y un modo seguro al que no se puede volver es una trampa. La decisión central: ¿qué transiciones existen y se puede siempre llegar al estado seguro?
- 🔗 **Se estudia junto con:** Estado/modo, Transición, Alcanzabilidad, Sumidero.

📘 **Dónde se aprende:** [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md).

### LET

- El LET (transferencia lineal de energía) es el cociente `dE/dl` entre la energía que una partícula cargada pierde por colisiones y la distancia recorrida; su unidad es J/m, a menudo keV/µm (definición del glosario de ICRP 103, consultado).

💡 **Cómo se explica en la clase [B112-C01](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md):**
- Una traza que cruza el núcleo con la cuerda media `2d/3 = 6,67 µm` deja `E = LET × cuerda`.
- Para el hierro ilustrativo de 150 keV/µm son `1000 keV = 1,6 × 10⁻¹³ J`; sobre la masa del núcleo, `0,306 Gy` por un solo impacto, frente a `1,02 mGy` de un protón de 0,5 keV/µm: un factor 300, el cociente de los LET.
- ⚠️ **Error frecuente:** `D = Φ·LET/ρ` las relaciona (8.3).
- 🎯 **Por qué importa:** B105-C06 introduce la exposición a la radiación espacial como un hecho del entorno, pero no define qué se mide ni en qué unidades. Sin esa definición no se puede leer una tasa de dosis de una misión ni entender por qué los iones pesados preocupan más que los protones.
- 🔗 **Se estudia junto con:** dosis absorbida, fluencia, eficacia biológica relativa, traza.

📘 **Dónde se aprende:** [B112-C01 · Magnitudes dosimétricas: dosis absorbida, LET y eficacia biológica](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md).

### LEU

- TED es la dosis efectiva total. LEU es uranio poco enriquecido (< 20 % de U-235).

💡 **Cómo se explica en la clase [B86-C18](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md):**
- *Descripción textual:* primero se ve si hay fisión (LEU nivel II, otro combustible nivel III); luego la probabilidad de más de 25 rem (nivel III); luego la actividad frente a `100000 × A2` (nivel II) y la probabilidad de 5–25 rem (nivel II); si nada se cumple, es nivel I.
- Tabla de verdad (1 g): sin probabilidades -> 1 ; p(5-25 rem) = 1e-6 -> 2 ; 1e-7 -> 1 ; p(>25 rem) = 1e-6 -> 3 ; fision LEU -> 2 ; fision otro combustible -> 3
- 🎯 **Por qué importa:** Los límites de la energía nuclear en el espacio son tanto jurídicos y de seguridad como técnicos: quién aprueba, con qué análisis y con qué umbrales. Un ingeniero de potencia debe saber que estas decisiones existen y qué datos las gobiernan.
- 🔗 **Se estudia junto con:** NSPM-20, niveles I, II y III, A2, TED.

📘 **Dónde se aprende:** [B86-C18 · Seguridad y licenciamiento energético](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md).

### LLA

- Los esquemas de datos se nombran LAL (lado–ángulo–lado), LLL (tres lados), ALA (ángulo–lado–ángulo) y LLA (lado–lado–ángulo no incluido).

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- B -->|"LLA"| E["Ley de senos: 0, 1 o 2 soluciones"]
- *Descripción textual:* según los datos (LAL o LLL, ALA o LLA) se usa la ley de cosenos, el tercer ángulo y la de senos, o la de senos con posible ambigüedad; todo termina comprobando que los ángulos suman 180°.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.
- 🔗 **Se estudia junto con:** ley de cosenos, ley de senos, resuelve, LAL.

📘 **Dónde se aprende:** [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### LLL

- Los esquemas de datos se nombran LAL (lado–ángulo–lado), LLL (tres lados), ALA (ángulo–lado–ángulo) y LLA (lado–lado–ángulo no incluido).

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- *Descripción textual:* según los datos (LAL o LLL, ALA o LLA) se usa la ley de cosenos, el tercer ángulo y la de senos, o la de senos con posible ambigüedad; todo termina comprobando que los ángulos suman 180°.
- La ley de cosenos es la más segura: no tiene ambigüedad y sirve con LAL y LLL.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.
- 🔗 **Se estudia junto con:** ley de cosenos, ley de senos, resuelve, LAL.

📘 **Dónde se aprende:** [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### LLT

- El LLT es el límite inferior de temperatura de replicación, −28 °C.

💡 **Cómo se explica en la clase [B56-C18](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md):**
- Probabilidad anual media equivalente de acceso a ambientes > LLT: 1.0e-07
- 🎯 **Por qué importa:** La política protege los otros mundos de la contaminación (para no estropear la búsqueda de vida) y la Tierra del material devuelto. Saber en qué categoría cae una misión determina su documentación, su limpieza y sus restricciones.
- 🔗 **Se estudia junto con:** categoría, categoría V, restringida, no restringida.

📘 **Dónde se aprende:** [B56-C18 · Protección planetaria COSPAR](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md).

### LOD

- El LOD es `3 s` y el LOQ `10 s`, con `s` la desviación del blanco.

💡 **Cómo se explica en la clase [B55-C18](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md):**
- Con `s = 1 ng` la neta apenas iguala el LOD.
- Siempre se propaga la incertidumbre y se informa el LOD.
- ⚠️ **Error frecuente:** Informar un valor bajo el LOD como medición. Se informa «< LOD» (trans. 1).
- 🎯 **Por qué importa:** En muestras extraterrestres la cantidad buscada puede ser del orden de la contaminación que entra al manipularlas. La decisión central: ¿la señal neta supera el límite de detección y con qué incertidumbre, una vez restado el blanco?
- 🔗 **Se estudia junto con:** señal neta, incertidumbre neta, LOQ, velocidad de Stokes.

📘 **Dónde se aprende:** [B55-C18 · Contaminación de muestras](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md).

### LOI

- **Significa:** inserción en órbita lunar (LOI).
- La inserción en órbita lunar (LOI) es el impulso en el perilune de la hipérbola.

💡 **Cómo se explica en la clase [B76-C07](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md):**
- Calcular el `Δv` de inserción lunar en función de la altitud de la órbita final.
- 🎯 **Por qué importa:** Un diseño preliminar de misión empieza por el presupuesto de velocidad. La decisión central: ¿cuánto `Δv` cuestan la salida de la Tierra y la captura en la Luna, y cuánto cambia la segunda según la órbita lunar elegida?
- 🔗 **Se estudia junto con:** inyección translunar (TLI), velocidad de llegada, excentricidad hiperbólica, fracción de propergol.

📘 **Dónde se aprende:** [B76-C07 · Maniobras de inserción cislunar](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md).

### LOO

- La densidad predictiva logarítmica esperada (`elpd`) es la suma esperada de `log p(ỹ_i | y)` sobre datos futuros; mayor es mejor. LOO: `elpd_loo = Σ_i log p(y_i | y_{−i})`.

💡 **Cómo se explica en la clase [B19-C07](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md):**
- LOO deja fuera `y_i`, ajusta con los otros `n − 1` datos y evalúa `log p(y_i | y_{−i})`.
- En este modelo normal, la posterior sin `y_i` es normal, y la predictiva es `N(m_{−i}, σ² + v_{−i})`: LOO exacto, sin aproximaciones.
- 🎯 **Por qué importa:** Miras 10 mediciones de la amplitud de una señal y el promedio es 0,57 con ruido conocido 1. ¿Hay señal (`μ ≠ 0`) o solo ruido (`μ = 0`)?
- 🔗 **Se estudia junto con:** evidencia, factor de Bayes, odds posteriores, factor de Occam.

📘 **Dónde se aprende:** [B19-C07 · Comparación de modelos bayesianos](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md).

### LOQ

- El LOD es `3 s` y el LOQ `10 s`, con `s` la desviación del blanco.

💡 **Cómo se explica en la clase [B55-C18](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md):**
- Descripción larga: una recta con las marcas LOD en 1,5, neta en 3,0 y LOQ en 5,0; la neta cae entre el LOD y el LOQ.
- Calcular LOD y LOQ a partir de la desviación del blanco.
- 🎯 **Por qué importa:** En muestras extraterrestres la cantidad buscada puede ser del orden de la contaminación que entra al manipularlas. La decisión central: ¿la señal neta supera el límite de detección y con qué incertidumbre, una vez restado el blanco?
- 🔗 **Se estudia junto con:** señal neta, incertidumbre neta, LOD, velocidad de Stokes.

📘 **Dónde se aprende:** [B55-C18 · Contaminación de muestras](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md).

### LQR

- El LQR es la ley `u = −K x` que minimiza `C`; se obtiene con `K = R⁻¹ Bᵀ P`, donde `P` resuelve la ecuación algebraica de Riccati `AᵀP + PA − P B R⁻¹ Bᵀ P + Q = 0` (S2 la presenta como `X A + AᴴX − X B R⁻¹ Bᴴ X + Q = 0`).

💡 **Cómo se explica en la clase [B16-C15](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md):**
- LQR: con varias entradas y estados, define el compromiso con `Q` y `R`; requiere estado completo.
- MPC (B87-C21): como el LQR, pero con restricciones explícitas.
- ⚠️ **Error frecuente:** Creer que el LQR respeta el par máximo. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Con un PD hay dos perillas, `Kp` y `Kd`, y no es obvio cuánto esfuerzo gasta cada combinación. En un satélite el esfuerzo tiene un costo real: energía de las ruedas, momento almacenado, desgaste.
- 🔗 **Se estudia junto con:** costo cuadrático, ecuación algebraica de Riccati.

📘 **Dónde se aprende:** [B16-C15 · Control óptimo LQR](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md).

### LR

- **Significa:** reducción logarítmica (LR).
- La reducción logarítmica (LR) es cuántos órdenes de magnitud baja un tratamiento.

💡 **Contexto en la clase [B115-C07](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md):**
- 🎯 **Por qué importa:** Una contaminación en un circuito compartido afecta a todos los lotes a la vez. La decisión central: ¿con qué frecuencia se muestrea, qué se mide y qué barreras (desinfección, lavado, temperatura) hacen falta para que una contaminación se detecte antes de llegar a un nivel de acción?
- 🔗 **Se estudia junto con:** inocuidad, bioseguridad, carga microbiana, punto de control.

📘 **Dónde se aprende:** [B115-C07 · Bioseguridad e inocuidad alimentaria en hábitats](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md).

### LSB

- El LSB `= Vref/2ⁿ`.
- El LSB de Q15 con escala 8 vale `8/32768 = 2,44×10⁻⁴`.
- Cuantización: discretización de la amplitud. LSB: escalón del cuantizador.

💡 **Cómo se explica en la clase [B88-C02](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md):**
- Con 12 bits y 3,3 V: `LSB = 0,8057 mV` y error de cuantización máximo `±0,4028 mV`. 1,000 V da el código 1241 (0,9998 V).
- A["Vref y bits"] --> L["LSB y cuantizacion"]
- 🎯 **Por qué importa:** Un error de configuración (un divisor mal calculado, una resolución insuficiente) no se ve en el escritorio y aparece en órbita. La decisión central: ¿qué valores de registro dan la temporización, la velocidad y la resolución que exige el requisito, con qué error?
- 🔗 **Se estudia junto con:** prescaler, cuenta, divisor, error de cuantización.

📘 **Dónde se aprende:** [B88-C02 · Microcontroladores embarcados](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md); [B88-C41 · Pruebas SIL y PIL del software de vuelo](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md); [B90-C23 · Instrumentación y adquisición de datos en ensayos](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md).

### LSK

- **Significa:** núcleo de segundos intercalares (LSK).
- Un núcleo de segundos intercalares (LSK) es el archivo de SPICE con esa tabla (S3).
- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- En el laboratorio se resuelven 6 archivos; todos existen y LSK y SCLK están antes que los SPK (las dos comprobaciones valen 1 = sí: `1` y `1`).
- Por tipo: SPK, CK, PCK, IK, FK, LSK, SCLK.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, CK, PCK.

📘 **Dónde se aprende:** [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md); [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### LS/LF

- ES/EF: inicio y fin tempranos. LS/LF: inicio y fin tardíos.

💡 **Contexto en la clase [B96-C09](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md):**
- 🎯 **Por qué importa:** Una secuencia que no cabe en la ventana deja comandos sin ejecutar o telemetría sin confirmar. La decisión central: ¿qué actividades fijan la duración mínima y cuánta holgura queda?
- 🔗 **Se estudia junto con:** Secuencia, Camino crítico, ES/EF, Holgura.

📘 **Dónde se aprende:** [B96-C09 · Secuencias de misión](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md).

### LTAN

- La LTAN es la hora local del nodo ascendente.

💡 **Cómo se explica en la clase [B72-C13](../programa/clases/B72/B72-C13-orbitas-heliosincronicas/CLASE.md):**
- Por periodo y LTAN. Por altitud máxima. Por deriva: minutos por año por cada décima de grado.
- Ejercicio 6 · autónomo. ¿A cuántos minutos de LTAN equivalen `5°` de longitud del nodo?
- 🎯 **Por qué importa:** La misma hora local de paso significa la misma iluminación en cada imagen: es lo que usan las misiones de observación de la Tierra. La decisión central: ¿qué inclinación corresponde a cada altitud y cuánta deriva de hora local produce un error de inclinación?
- 🔗 **Se estudia junto con:** órbita heliosíncrona, inclinación heliosíncrona, altitud máxima, deriva de LTAN.

📘 **Dónde se aprende:** [B72-C13 · Órbitas heliosincrónicas](../programa/clases/B72/B72-C13-orbitas-heliosincronicas/CLASE.md).

### LTI

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- X["Entrada x[n]<br/>= suma de impulsos<br/>escalados y retrasados"] --> S["Sistema LTI<br/>respuesta h[n]"]
- Ejercicio 8. Un sistema LTI responde al impulso con `h = [0,5; 0,3; 0,2]`.
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.
- 🔗 **Se estudia junto con:** impulso, respuesta impulsional, convolución, lineal.

📘 **Dónde se aprende:** [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md).

### LTV

- El LTV es el margen total que deja un cliente.
- El LTV es el margen total esperado de un cliente.

💡 **Cómo se explica en la clase [B125-C02](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md):**
- Con abandono `c`, la fracción viva tras `k` meses es `(1 − c)^k` y `LTV = Σ ARPU · margen · (1 − c)^k = ARPU · margen / c`.
- Con `ARPU = 1 000`, margen `0,70`, `c = 0,02`: `LTV = 35 000` (la serie simulada da `35 000`).
- ⚠️ **Error frecuente:** Calcular el `LTV` con `c` en lugar de `1/c` como vida media. Se corrige con 8.3.
- 🎯 **Por qué importa:** El modelo de ingresos define cuándo entra el dinero y cuánto vale un cliente; ninguna clase anterior lo trata. La decisión central: ¿cuánto vale un cliente de suscripción, cuándo se reconoce su ingreso y cuánto abandono puede tolerar el negocio?
- 🔗 **Se estudia junto con:** suscripción, ingreso diferido, reconocimiento ratable, hito.

📘 **Dónde se aprende:** [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md); [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### LU

- Una factorización (o descomposición) escribe `A` como producto de factores con estructura. LU: `P A = L U` con `L` triangular inferior de unos en la diagonal, `U` triangular superior y `P` una matriz de permutación (reordena filas) —es la eliminación gaussiana guardada—.

💡 **Cómo se explica en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- Aproximadamente: LU cuesta `2n³/3` operaciones, Cholesky `n³/3` (la mitad, por usar la simetría), QR cerca de `4n³/3` para matrices cuadradas.
- B -->|"cuadrada, general"| C["LU con pivoteo<br/>P A = L U"]
- ⚠️ **Error frecuente:** Confundir `L` de LU con `L` de Cholesky. Se corrige en la sección 10.
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.
- 🔗 **Se estudia junto con:** factorización, matriz de permutación, QR, Cholesky.

📘 **Dónde se aprende:** [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md).

### LVLH

- **Significa:** sistema local (LVLH).
- El sistema local (LVLH) tiene `x` radial hacia fuera e `y` a lo largo de la traza.

💡 **Contexto en la clase [B97-C11](../programa/clases/B97/B97-C11-robots-de-inspeccion-orbital/CLASE.md):**
- 🎯 **Por qué importa:** Una inspección segura se diseña de modo que, si falla el empuje, el robot no se acerque ni se aleje: la elipse sin deriva lo garantiza. Con una condición inicial mal elegida, el robot se aleja decenas de veces la distancia deseada en una órbita.
- 🔗 **Se estudia junto con:** movimiento relativo, ecuaciones de Clohessy–Wiltshire (CW), condición sin deriva, órbita de inspección.

📘 **Dónde se aprende:** [B97-C11 · Robots de inspección orbital](../programa/clases/B97/B97-C11-robots-de-inspeccion-orbital/CLASE.md).

### MAC

- El MAC es `(φᵀψ)²/((φᵀφ)(ψᵀψ))`.

💡 **Cómo se explica en la clase [B84-C30](../programa/clases/B84/B84-C30-correlacion-modelo-ensayo-y-actualizacion-de-modelos/CLASE.md):**
- MAC `1,0000; 0,9998; 0,9996`; fuera de la diagonal `0,0018`.
- El MAC cercano a 1 no distingue estos modelos: es insensible a escalas globales.
- ⚠️ **Error frecuente:** Confiar en el MAC solo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un MAC de 0,999 no basta: puede coexistir con un error de 3,6 % en frecuencia, y actualizar parámetros que no se pueden identificar da un modelo que ajusta pero no es físico. La decisión central: ¿cumple el modelo los criterios de correlación y qué parámetros se pueden actualizar con los datos?
- 🔗 **Se estudia junto con:** ortogonalidad cruzada, actualización.

📘 **Dónde se aprende:** [B84-C30 · Correlación modelo-ensayo y actualización de modelos](../programa/clases/B84/B84-C30-correlacion-modelo-ensayo-y-actualizacion-de-modelos/CLASE.md).

### MAD

- La MAD es la mediana de las desviaciones absolutas respecto de la mediana;
- La MAD (desviación absoluta mediana) es la mediana de `|x − mediana|`; multiplicada por 1,4826 estima la desviación típica de una distribución normal (el factor 1,4826 lo doy como conocido; no lo verifiqué en una fuente en esta clase).
- La MAD es la mediana de las desviaciones absolutas;
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C11](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md):**
- Paso 4 · Diagnóstico. Los residuos de OLS son grandes en los tres puntos y mucho menores en los demás; los residuos de Huber destacan los tres atípicos (`MAD` pequeña).
- Calcular la mediana, la MAD y una desviación robusta `σ̂ = MAD/0,6745`.
- 🎯 **Por qué importa:** Los datos reales traen errores de transmisión, rayos cósmicos en un detector, una lectura perdida o un salto del sensor. Un solo punto muy alejado puede torcer la recta de mínimos cuadrados y producir parámetros y predicciones erróneos con errores típicos pequeños y engañosos.
- 🔗 **Se estudia junto con:** valor atípico, punto de ruptura, pendiente de Theil–Sen, M-estimador.

📘 **Dónde se aprende:** [B12-C11 · Regresión robusta](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md); [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md); [B44-C15 · Píxeles defectuosos](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md); [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md).

### MAE

- `AP50` y `AP75` exigen IoU de 0,50 y 0,75. MAE es el error absoluto medio, RMSE el cuadrático medio, AbsRel la media de `|ẑ − z|/z` y delta1 la fracción de puntos con `máx(z/ẑ, ẑ/z) < 1,25`.

💡 **Cómo se explica en la clase [B33-C12](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md):**
- Ejercicio 2 · con una pista. MAE de `γ`/2.
- Ejercicio 6. Cociente RMSE/MAE de `γ` × 2.
- ⚠️ **Error frecuente:** Confundir sesgo y MAE. Se corrige con 8.1.
- 🎯 **Por qué importa:** Saber cómo falla un modelo orienta su mejora. La decisión central: ¿qué sesgo y qué precisión tiene cada especificación del arrastre?
- 🔗 **Se estudia junto con:** sesgo, RMSE, ventana de acierto, mala especificación.

📘 **Dónde se aprende:** [B33-C12 · Pronóstico de llegada y severidad de CME](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md).

### MAS

- **Significa:** movimiento armónico simple (MAS).
- El movimiento armónico simple (MAS) es el que sigue `x(t) = A cos(ω t + φ)`.

💡 **Contexto en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- **Idea central (modelo mental):** La energía pasa de cinética a potencial y viceversa, como una bola que rueda dentro de un cuenco; si hay roce, cada subida es más baja.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?
- 🔗 **Se estudia junto con:** amplitud, frecuencia angular, fase, fuerza restauradora.

📘 **Dónde se aprende:** [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md).

### MBSE

- Un modelo de sistema reúne parámetros, relaciones y restricciones en un solo lugar. MBSE es la práctica de usarlo como fuente central.

💡 **Cómo se explica en la clase [B83-C12](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md):**
- SysML y herramientas MBSE: añaden bloques, interfaces, requisitos y simulación (no usados aquí).
- 🎯 **Por qué importa:** Cuando los presupuestos viven en hojas distintas, un cambio de requisito se propaga a mano y algo se olvida. La decisión central: ¿qué parámetros cambian si cambia este requisito, y siguen cumpliéndose todos los presupuestos?
- 🔗 **Se estudia junto con:** modelo de sistema, parámetro de entrada, derivado, restricción.

📘 **Dónde se aprende:** [B83-C12 · Model-Based Systems Engineering](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md).

### MCAO

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C18](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md):**
- El modelo es solo una ilustración; un resumen de Rigaut y Neichel (solo resumen) indica que la MCAO busca campos 10 a 20 veces mayores en área que la óptica adaptativa clásica.
- *Descripción textual:* el anisoplanatismo crece como `(θ/θ₀)^{5/3}`; la MCAO lo reduce hasta que la huella queda fuera de las guías.
- ⚠️ **Error frecuente:** Confundir `θ₀` con el campo MCAO. Son conceptos distintos.
- 🎯 **Por qué importa:** Una sola corrección solo vale dentro del ángulo isoplanático (unos segundos de arco). La decisión central: ¿cómo se amplía el campo y qué parte de la turbulencia queda sin restricción?
- 🔗 **Se estudia junto con:** anisoplanatismo, ángulo isoplanático, altura efectiva, huella.

📘 **Dónde se aprende:** [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### MC/DC

- La cobertura de decisión exige `D = V` y `D = F`. MC/DC (condición/decisión modificada) exige para cada condición un par de pruebas que difieran solo en ella y cambien `D`.

💡 **Cómo se explica en la clase [B88-C39](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md):**
- MC/DC mínimo: `4`; el conjunto `{(0,1,0), (0,1,1), (1,0,0), (1,1,0)}` lo cumple.
- `{(1,1,0), (0,0,0)}` y `{(1,1,1), (0,0,0)}` cubren decisión y no MC/DC.
- 🎯 **Por qué importa:** Elegir el nivel de cobertura determina el esfuerzo de prueba. La decisión central: ¿qué cobertura piden los distintos niveles y cuánto cuesta cada una en pruebas?
- 🔗 **Se estudia junto con:** cobertura de decisión, tamaño mínimo, exhaustiva.

📘 **Dónde se aprende:** [B88-C39 · Normas de aseguramiento de software (ECSS, DO-178C)](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md).

### MCU

- **Significa:** movimiento circular uniforme (MCU).
- El movimiento circular uniforme (MCU) recorre una circunferencia con rapidez constante.

💡 **Contexto en la clase [B05-C03](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md):**
- **Idea central (modelo mental):** Ambos movimientos se construyen con la misma idea: sumar efectos pequeños de `a` sobre `v` y de `v` sobre `x`.
- 🎯 **Por qué importa:** Un cohete que enciende su motor un tiempo corto y un satélite que da vueltas son, a primera aproximación, estos dos movimientos. La pregunta motivadora es: ¿qué fórmulas valen cuando la aceleración es constante o cuando la rapidez es constante en un círculo, y hasta dónde son confiables?
- 🔗 **Se estudia junto con:** movimiento rectilíneo uniforme (MRU), movimiento rectilíneo uniformemente acelerado (MRUA), período, frecuencia.

📘 **Dónde se aprende:** [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md).

### M/D/1

- En M/D/1, `W_q = ρS/(2(1 − ρ))`.

💡 **Cómo se explica en la clase [B88-C43](../programa/clases/B88/B88-C43-pruebas-de-carga-y-estres-del-software-de-vuelo/CLASE.md):**
- La espera real es mayor que la de M/D/1.
- El script [carga_estres.py](carga_estres.py) simula una cola M/D/1 con cinco cargas, compara con la teoría y estudia el descarte con cola de 16, y comprueba que el error relativo es menor que 10 % para `ρ < 0,9`.
- 🎯 **Por qué importa:** Un sistema que funciona al 50 % de carga puede volverse inutilizable al 95 %. La decisión central: ¿a qué tasa de llegada se degrada la latencia y qué política de descarte conviene al saturarse?
- 🔗 **Se estudia junto con:** utilización, p99, descarte, saturación.

📘 **Dónde se aprende:** [B88-C43 · Pruebas de carga y estrés del software de vuelo](../programa/clases/B88/B88-C43-pruebas-de-carga-y-estres-del-software-de-vuelo/CLASE.md).

### MDC95

- El MDC95 es `1,96 √2 SEM`: el cambio mínimo que supera el ruido con 95 % de confianza.
- El MDC95 es el cambio mínimo detectable al 95 %.

💡 **Cómo se explica en la clase [B105-C26](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md):**
- Promediar `k` sesiones da `SEM = 4/√k`: 4,00 (1); 2,83 (2) y 2,00 (4); el MDC95 baja a 11,09; 7,84 y 5,54.
- Una medida sintética con variación entre individuos `SD = 10` y variación dentro de individuos `SD = 4`: ICC verdadero `100/(100 + 16) = 0,862`, SEM = 4,00 y MDC95 = 11,09.
- 🎯 **Por qué importa:** Un biomarcador con alta variación interna no detecta cambios pequeños aunque sea «preciso». Con pocos participantes, además, el propio ICC es incierto.
- 🔗 **Se estudia junto con:** ICC(1,1), SEM, límites de acuerdo, Bland–Altman.

📘 **Dónde se aprende:** [B105-C26 · Medidas fisiológicas y biomarcadores en investigación espacial](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md); [B107-C08 · Evaluación funcional posterior al vuelo](../programa/clases/B107/B107-C08-evaluacion-funcional-posterior-al-vuelo/CLASE.md).

### MDS

- Un MDS (modelo digital de superficie) incluye árboles y edificios; un MDT (de terreno) los quita.

💡 **Cómo se explica en la clase [B57-C28](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md):**
- A["arboles y edificios"] --> S["MDS = MDT + objetos"]
- *Descripción textual:* la rejilla y el tamaño de celda alimentan el operador de Horn, que da pendiente y orientación; un paso mayor las subestima, y los objetos sobre el terreno distinguen el MDS del MDT.
- ⚠️ **Error frecuente:** Usar un MDS como MDT. Se corrige con 8.4.
- 🎯 **Por qué importa:** La pendiente decide dónde se produce un deslizamiento, cómo corre el agua o si una antena ve el horizonte. La decisión central: ¿qué resolución y qué tipo de modelo necesito para la pendiente que me importa?
- 🔗 **Se estudia junto con:** MDT, pendiente, orientación, operador de Horn.

📘 **Dónde se aprende:** [B57-C28 · Modelos digitales de elevación](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md).

### MDT

- Un MDS (modelo digital de superficie) incluye árboles y edificios; un MDT (de terreno) los quita.

💡 **Cómo se explica en la clase [B57-C28](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md):**
- A["arboles y edificios"] --> S["MDS = MDT + objetos"]
- *Descripción textual:* la rejilla y el tamaño de celda alimentan el operador de Horn, que da pendiente y orientación; un paso mayor las subestima, y los objetos sobre el terreno distinguen el MDS del MDT.
- ⚠️ **Error frecuente:** Usar un MDS como MDT. Se corrige con 8.4.
- 🎯 **Por qué importa:** La pendiente decide dónde se produce un deslizamiento, cómo corre el agua o si una antena ve el horizonte. La decisión central: ¿qué resolución y qué tipo de modelo necesito para la pendiente que me importa?
- 🔗 **Se estudia junto con:** MDS, pendiente, orientación, operador de Horn.

📘 **Dónde se aprende:** [B57-C28 · Modelos digitales de elevación](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md).

### ME

- **Significa:** sesgo (ME).
- El sesgo (ME) es el error medio.

💡 **Cómo se explica en la clase [B57-C31](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md):**
- El sesgo impuesto es 0,5 m; los 400 puntos lo estiman en `0,21 m` con un error estándar de unos 0,10 m: el propio sesgo estimado tiene incertidumbre.
- Declarar solo la métrica favorable es incorrecto; hay que reportar sesgo, RMSE, NMAD y LE90 y cómo se trataron los atípicos.
- 🎯 **Por qué importa:** Decir «el MDE tiene 4 m de error» sin definir la métrica ni los puntos de control no significa nada. La decisión central: ¿qué métrica y qué intervalo de confianza reporto para que mi validación sea comparable y honesta?
- 🔗 **Se estudia junto con:** RMSE, NMAD, LE90, punto de control.

📘 **Dónde se aprende:** [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md).

### MET

- Un MET equivale a unos 1 kcal/kg/h (aproximación, no consultada).

💡 **Cómo se explica en la clase [B105-C16](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md):**
- Un tripulante sintético de 75 kg hace 2 h/día de resistencia a 6 MET: 900 kcal/día (33,7 % del gasto de 2.668 kcal/día de B105-C12) y 5.400 kcal por semana de 6 días.
- Calcular la energía del ejercicio con `kcal = MET·kg·h`.
- ⚠️ **Error frecuente:** Confundir MET con kcal. Multiplica por kg y h (8.1).
- 🎯 **Por qué importa:** Más ejercicio ayuda, pero con rendimientos decrecientes y con un costo de energía y tiempo. La decisión central: ¿qué parte de la pérdida se evita con una carga dada y cuánta energía extra exige?
- 🔗 **Se estudia junto con:** carga semanal, curva de Hill, reducción relativa, fuerza de reacción.

📘 **Dónde se aprende:** [B105-C16 · Contramedidas de ejercicio](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md).

### MEV

- La reserva de crecimiento es un porcentaje según madurez (comercial 5 %, modificado 10 %, nuevo 20 %, en desarrollo 30 %, valores de ejemplo). MEV (*maximum expected value*) es CBE más reserva.
- La CBE es la mejor estimación actual; la MEV, la masa máxima esperada, que añade el crecimiento por madurez.

💡 **Cómo se explica en la clase [B83-C09](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md):**
- La reserva total es 7,910 kg (13,32 % de la CBE) y el MEV seco es 67,310 kg.
- Masa de lanzamiento MEV = 72,156 kg; margen 7,844 kg = 9,80 %.
- ⚠️ **Error frecuente:** Presentar CBE como valor final. Usa MEV y declara la reserva
- 🎯 **Por qué importa:** La masa crece durante el diseño casi siempre; un presupuesto sin reserva se rompe en la revisión crítica. La decisión central: ¿cuánto margen queda frente al límite si cada elemento crece como su madurez sugiere?
- 🔗 **Se estudia junto con:** masa CBE, reserva de crecimiento, margen, ecuación del cohete.

📘 **Dónde se aprende:** [B83-C09 · Presupuestos de masa](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md); [B124-C19 · Redacción de propuesta de misión](../programa/clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md).

### MIFR

- El MIFR es el registro de frecuencias.
- El MIFR es el Registro Internacional de Frecuencias.

💡 **Cómo se explica en la clase [B119-C09](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md):**
- Describir lo que hace la UIT-R: notificación, coordinación, MIFR e interferencia perjudicial.
- La examina, aplica la coordinación y la inscribe en el MIFR (S4).
- 🎯 **Por qué importa:** Ninguna clase anterior vincula el derecho de telecomunicaciones con el cálculo de interferencia; B120 trata licencias y espectro en detalle y esta clase fija el marco.
- 🔗 **Se estudia junto con:** notificación, coordinación, interferencia perjudicial, FSPL.

📘 **Dónde se aprende:** [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md); [B120-C01 · Licencias satelitales y procedimiento de notificación](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md).

### MIS

- **Significa:** medio interestelar (MIS).
- El medio interestelar (MIS) es la materia (gas y polvo), los rayos cósmicos y el campo magnético entre las estrellas.

💡 **Cómo se explica en la clase [B25-C03](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md):**
- python programa/clases/B25/B25-C03-medio-interestelar-multifasico/fases_ism.py
- 🎯 **Por qué importa:** Las estrellas nacen del gas y devuelven gas enriquecido; el medio interestelar (MIS) es el almacén y el escenario de ese ciclo. Pero «gas» sirve de poco: un volumen del MIS puede estar a `10 K` o a `10⁶ K`, y su densidad variar un factor 10⁷ de un punto a otro.
- 🔗 **Se estudia junto con:** fase, medio neutro frío, medio neutro tibio, medio ionizado tibio.

📘 **Dónde se aprende:** [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md).

### MJD

- **Significa:** día juliano modificado (MJD).
- El día juliano modificado (MJD) es `JD − 2 400 000,5` y empieza a medianoche.

💡 **Cómo se explica en la clase [B13-C09](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md):**
- Convertir una fecha gregoriana en día juliano modificado (MJD) y viceversa.
- 🎯 **Por qué importa:** Una nave graba un evento a las `23:59:59` del 31 de diciembre de 2016 y otro a las `00:00:00` del 1 de enero de 2017. ¿Cuánto tiempo pasó?
- 🔗 **Se estudia junto con:** segundo intercalar, calendario gregoriano, día juliano (JD), cuenta continua.

📘 **Dónde se aprende:** [B13-C09 · Segundos intercalares y cronología](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md).

### ML

- Una ML es una monocapa (por convención `10¹⁵` moléculas cm⁻²).

💡 **Cómo se explica en la clase [B68-C02](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md):**
- Para CO₂ a 15–18 K, Öberg y colaboradores dan `Y(x) = 1,2 × 10⁻³ (1 − e^(−x/2,9)) + 1,1 × 10⁻³ (1 − e^(−x/4,6))`, con `x` en ML: dos términos, uno para el CO₂ que sale tras disociarse y recombinarse y otro para el CO que sale.
- El límite es `2,30 × 10⁻³` y se alcanza el 90 % a `x = 8,63 ML`.
- 🎯 **Por qué importa:** Si un hielo de CO a 15 K es estable térmicamente durante millones de años, la presencia de CO gaseoso en regiones frías exige otro mecanismo. La decisión central: ¿cuántas moléculas expulsa cada fotón y de qué depende ese número?
- 🔗 **Se estudia junto con:** fotodesorción, rendimiento, fluencia, DIET.

📘 **Dónde se aprende:** [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md).

### MLI

- **Significa:** manta multicapa (MLI).
- La manta multicapa (MLI) es un apilado de láminas reflectantes separadas por espaciadores.

💡 **Cómo se explica en la clase [B85-C06](../programa/clases/B85/B85-C06-aislamiento-multicapa/CLASE.md):**
- La evidencia es la ficha de dimensionado de una manta multicapa del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de dimensionado de una manta multicapa*: `q`, `ε_eff` y temperaturas para `N` capas, número de capas para un objetivo, efecto de la compresión y lista de lo consultado e ilustrativo.
- 🎯 **Por qué importa:** Aislar una caja que opera a `300 K` de un entorno a `100 K` con una sola superficie cuesta cientos de W/m²; con unas pocas capas cuesta unidades. La decisión central: ¿cuántas capas y de qué emisividad hacen falta para limitar el flujo, y cuánto se pierde si se comprimen?
- 🔗 **Se estudia junto con:** emisividad efectiva, compresión.

📘 **Dónde se aprende:** [B85-C06 · Aislamiento multicapa](../programa/clases/B85/B85-C06-aislamiento-multicapa/CLASE.md).

### M/M/1

- Incidente: evento que interrumpe la operación normal. M/M/1: cola con llegadas y servicios exponenciales y un servidor.

💡 **Cómo se explica en la clase [B96-C26](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md):**
- Las fórmulas de la teoría de colas (M/M/1 y la de Cobham para prioridad no expropiativa) son estándar y las verifica el laboratorio.
- Calcular la utilización y la espera media de una cola M/M/1.
- 🎯 **Por qué importa:** Sin un procedimiento de priorización, un incidente leve puede retrasar a uno grave. La decisión central: ¿cuánto esperan los incidentes de alta y de baja prioridad y cuánto mejora la priorización al grave sin colapsar al leve?
- 🔗 **Se estudia junto con:** Incidente, Utilización, Espera Wq, Prioridad no expropiativa.

📘 **Dónde se aprende:** [B96-C26 · Gestión de incidentes en la operación de estaciones](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md).

### MOC/SOC

- Segmento terrestre: estaciones, MOC, SOC y redes. MOC/SOC: centros de operaciones de misión y científicas.

💡 **Contexto en la clase [B96-C01](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md):**
- 🎯 **Por qué importa:** Quien opera una nave no puede tratarla como un equipo de laboratorio: cada comando viaja a la velocidad de la luz y cada contacto dura minutos. La decisión central: ¿qué segmento hace qué y cuánto tardan en comunicarse?
- 🔗 **Se estudia junto con:** Segmento espacial, Segmento terrestre, Retardo de propagación, Ida y vuelta (RTT).

📘 **Dónde se aprende:** [B96-C01 · Segmento espacial y segmento terrestre](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md).

### MOCUS

- Un conjunto de corte es una combinación que causa el evento superior; es mínimo si ningún subconjunto propio lo causa. MOCUS expande el árbol a conjuntos de corte.

💡 **Contexto en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?
- 🔗 **Se estudia junto con:** árbol de fallos, eventos básicos, conjunto de corte, mínimo.

📘 **Dónde se aprende:** [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### MOIC

- El MOIC es el múltiplo de lo recibido sobre lo invertido.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- Se reciben `300` Mum y se invierten `140`: MOIC `2,143`.
- El MOIC no dice cuánto tarda; la TIR sí.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?
- 🔗 **Se estudia junto con:** VAN, TIR, pre-money, post-money.

📘 **Dónde se aprende:** [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md).

### MOID

- El MOID es la distancia mínima entre dos órbitas, no entre los cuerpos.

💡 **Cómo se explica en la clase [B58-C05](../programa/clases/B58/B58-C05-orbitas-cercanas-a-la-tierra/CLASE.md):**
- (iii) Circular inclinada de radio `a`: la distancia al cuadrado es `a² − 2ρ + 1`, mínima en el nodo, donde `ρ = a`, así que `MOID = |a−1|`;
- SINT-A (`H = 21`, MOID `0.080`) no es PHA;
- ⚠️ **Error frecuente:** Confundir MOID con distancia de acercamiento. Se corrige con la sección 7.
- 🎯 **Por qué importa:** Dos órbitas pueden cruzarse en proyección sin que los cuerpos coincidan nunca, y pueden no cruzarse y estar a una distancia pequeña. El MOID separa los casos geométricamente.
- 🔗 **Se estudia junto con:** PHA, nodo, sección áurea.

📘 **Dónde se aprende:** [B58-C05 · Órbitas cercanas a la Tierra](../programa/clases/B58/B58-C05-orbitas-cercanas-a-la-tierra/CLASE.md).

### MPC

- El MPC minimiza un costo sobre un horizonte `N` con un modelo.

💡 **Cómo se explica en la clase [B87-C21](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md):**
- El MPC lo respeta con una violación de `1,5 %` (restricción blanda); el PD lo excede en `11 %`.
- MPC con QP (esta clase): restricciones explícitas, mayor cómputo.
- ⚠️ **Error frecuente:** Creer que el MPC garantiza la restricción blanda. Revisa la violación residual (8.4)
- 🎯 **Por qué importa:** Un PD satura el par y no sabe de límites de velocidad: puede superar el máximo de la rueda o de la carga útil. La decisión central: ¿cómo formular un problema que respete par y velocidad, cuánto cuesta calcularlo y qué se gana?
- 🔗 **Se estudia junto con:** horizonte, QP condensado, restricción dura, restricción blanda.

📘 **Dónde se aprende:** [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md).

### MRU

- **Significa:** movimiento rectilíneo uniforme (MRU).
- El movimiento rectilíneo uniforme (MRU) tiene velocidad constante y aceleración cero.

💡 **Contexto en la clase [B05-C03](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md):**
- **Idea central (modelo mental):** Ambos movimientos se construyen con la misma idea: sumar efectos pequeños de `a` sobre `v` y de `v` sobre `x`.
- 🎯 **Por qué importa:** Un cohete que enciende su motor un tiempo corto y un satélite que da vueltas son, a primera aproximación, estos dos movimientos. La pregunta motivadora es: ¿qué fórmulas valen cuando la aceleración es constante o cuando la rapidez es constante en un círculo, y hasta dónde son confiables?
- 🔗 **Se estudia junto con:** movimiento rectilíneo uniformemente acelerado (MRUA), movimiento circular uniforme (MCU), período, frecuencia.

📘 **Dónde se aprende:** [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md).

### MRUA

- **Significa:** movimiento rectilíneo uniformemente acelerado (MRUA).
- El movimiento rectilíneo uniformemente acelerado (MRUA) tiene aceleración constante.

💡 **Contexto en la clase [B05-C03](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md):**
- **Idea central (modelo mental):** Ambos movimientos se construyen con la misma idea: sumar efectos pequeños de `a` sobre `v` y de `v` sobre `x`.
- 🎯 **Por qué importa:** Un cohete que enciende su motor un tiempo corto y un satélite que da vueltas son, a primera aproximación, estos dos movimientos. La pregunta motivadora es: ¿qué fórmulas valen cuando la aceleración es constante o cuando la rapidez es constante en un círculo, y hasta dónde son confiables?
- 🔗 **Se estudia junto con:** movimiento rectilíneo uniforme (MRU), movimiento circular uniforme (MCU), período, frecuencia.

📘 **Dónde se aprende:** [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md).

### MSH

- **Significa:** millonésima de hemisferio (MSH).
- La millonésima de hemisferio (MSH) es la unidad de área de manchas.

💡 **Cómo se explica en la clase [B30-C04](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md):**
- Una mancha ilustrativa de `r = 10 Mm` y `B = 0,3 T` tiene un área de `3,14 × 10¹⁴ m²` (103 millonésimas de hemisferio) y un flujo de `9,42 × 10¹³ Wb`.
- Convertir áreas a millonésimas de hemisferio.
- 🎯 **Por qué importa:** Las manchas son la huella visible del campo magnético y las más fáciles de contar. Cuantificar su presión, su brillo y su flujo permite relacionarlas con la irradiancia.
- 🔗 **Se estudia junto con:** umbra, penumbra, presión magnética, contraste.

📘 **Dónde se aprende:** [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md).

### MTBF

- El MTBF (o MTTF) es `1/λ` en el modelo exponencial.
- Cota superior de confianza: valor que, con probabilidad `CL`, no es inferior a la tasa verdadera. MTBF: tiempo medio entre fallas.
- La tasa de falla `λ` es la probabilidad de fallar por unidad de tiempo; el MTBF es `1/λ` con tasa constante.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C09](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md):**
- M["MTBF, MTTR"] --> A["A = MTBF/(MTBF+MTTR)"]
- Ejercicio 5. `A` con MTBF = 2000 h y MTTR = 24 h.
- 🎯 **Por qué importa:** Una unidad adicional mejora menos que la anterior y las fallas comunes limitan la ganancia. La decisión central: ¿cuántas unidades de respaldo valen la pena?
- 🔗 **Se estudia junto con:** redundancia, causa común, disponibilidad, MTTR.

📘 **Dónde se aprende:** [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B86-C11 · Redundancia eléctrica](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md); [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md); [B93-C04 · Análisis de confiabilidad de electrónica (MTBF y derating)](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md); [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### MTBF/MTTR

- MTBF/MTTR: tiempo medio entre fallas y de reparación.

💡 **Cómo se explica en la clase [B96-C23](../programa/clases/B96/B96-C23-continuidad-y-redundancia-de-las-operaciones-terrestres/CLASE.md):**
- Solo se leyó la parte inicial; no da MTBF ni MTTR.
- Calcular la disponibilidad `A = MTBF/(MTBF + MTTR)` de un componente.
- ⚠️ **Error frecuente:** Usar MTBF sin MTTR. Calcula `A` (8.2)
- 🎯 **Por qué importa:** Redundancia no es solo tener más estaciones: si comparten la causa de falla (red, energía, software) el beneficio desaparece. La decisión central: ¿cuántas estaciones y qué independencia hacen falta para que la probabilidad de perder un contacto sea aceptable?
- 🔗 **Se estudia junto con:** Disponibilidad, Serie, Paralelo, Causa común (β).

📘 **Dónde se aprende:** [B96-C23 · Continuidad y redundancia de las operaciones terrestres](../programa/clases/B96/B96-C23-continuidad-y-redundancia-de-las-operaciones-terrestres/CLASE.md).

### MTD

- El RTO es el tiempo objetivo para restablecer el servicio; el WRT es el tiempo adicional para recuperar el trabajo; el MTD es el tiempo máximo tolerable de interrupción.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- Se esperan `(8760/724) e^(−8/4) = 1,637` cortes por año que superen el MTD.
- *Descripción textual:* desde el fallo corren el RTO y el WRT, cuya suma no debe pasar del MTD, mientras el costo crece; el RPO limita el intervalo entre copias.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?
- 🔗 **Se estudia junto con:** disponibilidad, MTBF, MTTR, RTO.

📘 **Dónde se aprende:** [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### MTF

- La MTF mide el contraste conservado.
- La MTF: su módulo.

💡 **Cómo se explica en la clase [B42-C07](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md):**
- Si la PSF se toma cada 4 píxeles (1 por `λ/D`) la OTF medida suma `MTF(v) + MTF(1 − v)`:
- Paso 1 · Fórmula. `MTF = (2/π)[acos v − v√(1−v²)]`.
- 🎯 **Por qué importa:** La OTF dice qué detalles (frecuencias espaciales) pasan por el sistema y cuáles se pierden; fija el muestreo necesario del detector. La decisión central: ¿hasta qué frecuencia transmite el telescopio y qué muestreo exige?
- 🔗 **Se estudia junto con:** OTF, frecuencia de corte, autocorrelación, muestreo de Nyquist.

📘 **Dónde se aprende:** [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md); [B83-C17 · Verificación frente a validación](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md).

### MTTR

- El MTTR es el tiempo medio de reparación.
- El MTBF es el tiempo medio entre fallas y el MTTR el tiempo medio de reparación.
- El MTBF y el MTTR.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C09](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md):**
- M["MTBF, MTTR"] --> A["A = MTBF/(MTBF+MTTR)"]
- Ejercicio 5. `A` con MTBF = 2000 h y MTTR = 24 h.
- 🎯 **Por qué importa:** Una unidad adicional mejora menos que la anterior y las fallas comunes limitan la ganancia. La decisión central: ¿cuántas unidades de respaldo valen la pena?
- 🔗 **Se estudia junto con:** redundancia, causa común, disponibilidad, MTBF.

📘 **Dónde se aprende:** [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B59-C18 · Fiabilidad de equipos mineros](../programa/clases/B59/B59-C18-fiabilidad-de-equipos-mineros/CLASE.md); [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### MUF

- La MUF (frecuencia máxima utilizable) para un salto de distancia `D` es `foF2/cos φ`, con `φ` el ángulo de incidencia en la capa.

💡 **Cómo se explica en la clase [B89-C22](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md):**
- Con la densidad en `4×10¹¹` la MUF baja a `63 %` de la diurna (misma razón en todas las distancias, `√(N₂/N₁)`): a 2000 km, de `25,3` a `16,0 MHz`.
- *Descripción textual:* la densidad da la frecuencia crítica; la distancia y la altura dan el ángulo de incidencia; juntos dan la MUF; una tormenta cambia la densidad y por tanto la MUF.
- ⚠️ **Error frecuente:** Confundir `foF2` con la MUF. Se corrige con 8.3.
- 🎯 **Por qué importa:** En un apagón de enlaces por satélite o en regiones remotas, el HF sigue siendo un medio de comunicación; saber qué frecuencia usar a cada hora y distancia, y cómo la perturba una tormenta, decide si el enlace existe.
- 🔗 **Se estudia junto con:** frecuencia de plasma, frecuencia crítica, salto.

📘 **Dónde se aprende:** [B89-C22 · Propagación ionosférica y comunicaciones HF](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md).

### MUSD

- La ventana de cobertura es el periodo en que el seguro responde. MUSD son millones de dólares ficticios.

💡 **Cómo se explica en la clase [B127-C01](../programa/clases/B127/B127-C01-seguros-de-lanzamiento/CLASE.md):**
- El Monte Carlo (200 000 lanzamientos, semilla 127) da una pérdida media de `7,103 MUSD`, error relativo `0,75 %`.
- Paso 3 · Prima pura. `200 × 0,03525 = 7,050 MUSD`.
- 🎯 **Por qué importa:** B124-C08 presenta el riesgo y los seguros en general; el seguro de lanzamiento tiene estructura y coberturas propias. La decisión central: ¿qué prima es coherente con la probabilidad de fallo y qué parte de ella es recargo?
- 🔗 **Se estudia junto con:** valor asegurado, tasa, prima pura, recargo.

📘 **Dónde se aprende:** [B127-C01 · Seguros de lanzamiento](../programa/clases/B127/B127-C01-seguros-de-lanzamiento/CLASE.md).

### NCC

- La NCC mide la similitud de dos ventanas sin sensibilidad a brillo y contraste.

💡 **Cómo se explica en la clase [B74-C26](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md):**
- Para cada desplazamiento de `±12 px` se calcula la NCC de la plantilla de 32 × 32 px con la ventana de la imagen; el máximo se refina con una parábola en cada eje.
- PL["plantilla"] --> NCC["NCC en la ventana"]
- 🎯 **Por qué importa:** Un buen pico de correlación no garantiza un buen emparejamiento: en un terreno repetitivo hay dos picos casi iguales. La decisión central: ¿cuánta precisión da la correlación en un terreno rico, y cuándo el emparejamiento es ambiguo y no debe usarse?
- 🔗 **Se estudia junto con:** plantilla, ventana de búsqueda, refinamiento subpíxel, razón pico/segundo pico.

📘 **Dónde se aprende:** [B74-C26 · Navegación por hitos y correlación de terreno](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md).

### NCPA

- Las NCPA: aberraciones fuera del camino común.

💡 **Cómo se explica en la clase [B42-C23](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md):**
- La NCPA tiene `0,1526 rad` rms (desenfoque `0,12`, astigmatismos `0,08` y `−0,05`); el Strehl sin corregir es `0,97732` (Maréchal `0,97697`).
- La NCPA de este tamaño cuesta 2,3 % de Strehl y no la ve el sensor: se mide en la imagen.
- ⚠️ **Error frecuente:** Confundir NCPA con aberración atmosférica. Ver sección 7.
- 🎯 **Por qué importa:** Una matriz mal calibrada degrada el lazo y las aberraciones del camino de ciencia no las ve el sensor. La decisión central: ¿con qué amplitud calibrar y cómo corregir lo que el sensor no ve?
- 🔗 **Se estudia junto con:** matriz de interacción, empuje-tirón, matriz de control, valores singulares.

📘 **Dónde se aprende:** [B42-C23 · Calibración de la matriz de interacción y aberraciones no comunes](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md).

### NDVI

- El NDVI (*índice de vegetación de diferencia normalizada*) es `(NIR − rojo)/(NIR + rojo)`.
- El NDVI es `(NIR − rojo)/(NIR + rojo)` y va de −1 a +1.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- Con las medias ficticias, el NDVI es `−0,20` (agua), `+0,84` (vegetación) y `+0,17` (suelo).
- El NDVI condensa dos bandas en una; no sustituye al clasificador, pero ilustra por qué las bandas separan clases.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, clase, muestras de entrenamiento, muestras de prueba.

📘 **Dónde se aprende:** [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md); [B57-C06 · Índices de vegetación](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md).

### NEES

- El NEES (*normalized estimation error squared*) es `eᵀ P⁻¹ e`, con `e` el error real; si el filtro es coherente, su media es la dimensión del estado.
- El NEES es `eᵀ P⁻¹ e` y vale en promedio la dimensión del estado si el filtro es consistente.
- El NEES es `eᵀP⁻¹e` con `e = x̂ − x` (ν = dimensión del estado).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C17](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md):**
- El NEES medio es `2,066`, cerca del valor ideal 2: el filtro es coherente (su incertidumbre declarada coincide con su error real).
- Si se declara `Q` 10 000 veces menor que la real (se cree que el objeto no acelera), el filtro confía demasiado en su modelo: el RMSE sube a `17,1 m` y el NEES a `5019`, muy por encima de 2.
- ⚠️ **Error frecuente:** No comprobar la coherencia (NEES). Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.
- 🔗 **Se estudia junto con:** estado, matriz de transición, matriz de medida, covarianza del ruido de proceso.

📘 **Dónde se aprende:** [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B74-C09 · Filtro de Kalman extendido](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md); [B74-C23 · Consistencia de filtros: innovaciones y pruebas NEES/NIS](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md); [B80-C08 · Filtrado distribuido y descentralizado](../programa/clases/B80/B80-C08-filtrado-distribuido-y-descentralizado/CLASE.md); [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md).

### NFT

- **Significa:** película de nutrientes (NFT).
- En una película de nutrientes (NFT) una lámina delgada y recirculante moja las raíces en un canal inclinado.

💡 **Cómo se explica en la clase [B115-C01](../programa/clases/B115/B115-C01-cultivos-hidroponicos-para-habitats/CLASE.md):**
- Calcular la profundidad y la velocidad de una película de nutrientes con la ecuación de Manning.
- 🎯 **Por qué importa:** Un cultivo sin suelo depende por completo de que el caudal, el oxígeno y el nivel del depósito no fallen. La decisión central: ¿qué caudal y qué volumen hacen falta para que las raíces reciban oxígeno y agua sin que el sistema se vacíe o se inunde, y cómo se comprueba?
- 🔗 **Se estudia junto con:** hidroponía, ecuación de Manning, número de Froude, oxígeno disuelto (DO).

📘 **Dónde se aprende:** [B115-C01 · Cultivos hidropónicos para hábitats](../programa/clases/B115/B115-C01-cultivos-hidroponicos-para-habitats/CLASE.md).

### NHV

- **Significa:** volumen neto habitable (NHV).
- El volumen neto habitable (NHV) es el que queda libre para la tripulación.

💡 **Cómo se explica en la clase [B109-C07](../programa/clases/B109/B109-C07-asignacion-de-volumenes-habitables-por-tripulante/CLASE.md):**
- El informe de consenso del Human Research Program (2014) define el volumen neto habitable como el volumen que queda disponible para la tripulación tras descontar el equipo desplegado, el almacenamiento, la basura y otras ineficiencias, y recomendó `25 m³` por persona para una misión de `30` meses a Marte.
- Definir el volumen neto habitable según el informe de consenso del HRP.
- 🎯 **Por qué importa:** Una cifra de «metros cúbicos por persona» sin decir qué se descontó no se puede comparar. La decisión central: ¿cuánto volumen utilizable queda por tripulante y qué tan sensible es a lo que se descuenta?
- 🔗 **Se estudia junto con:** volumen bruto, volumen funcional, descuento, huecos.

📘 **Dónde se aprende:** [B109-C07 · Asignación de volúmenes habitables por tripulante](../programa/clases/B109/B109-C07-asignacion-de-volumenes-habitables-por-tripulante/CLASE.md).

### NIEL

- El NIEL es la energía no ionizante depositada por unidad de longitud.

💡 **Contexto en la clase [B85-C24](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md):**
- 🎯 **Por qué importa:** Una celda solar o un polímero no fallan de golpe: pierden prestaciones con la exposición. La decisión central: ¿cuánta potencia queda al final de la misión y cuánto cambia con un blindaje que reduce la fluencia?
- 🔗 **Se estudia junto con:** ley de degradación, dosis total ionizante, umbrales, inversa.

📘 **Dónde se aprende:** [B85-C24 · Efectos de la radiación ionizante en materiales y electrónica](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md).

### NIS

- El NIS es `νᵀS⁻¹ν` con `ν` la innovación y `S` su covarianza (ν = dimensión de la medida).

💡 **Cómo se explica en la clase [B74-C23](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md):**
- Con `N = 100`, `n = 2` los límites del 95 % son `[1,627, 2,411]` (esperado 2), y para el NIS con 1 grado de libertad, `[0,742, 1,296]` (esperado 1).
- Con el `q` verdadero, el NEES medio es `1,997` y el NIS `0,989`; el `0,94` y el `0,94` de los pasos caen dentro de los límites, como se espera para una prueba al 95 % con pasos correlacionados.
- ⚠️ **Error frecuente:** Dar por bueno un filtro por el rms. Aplica NEES/NIS; ver 8.2.
- 🎯 **Por qué importa:** Un filtro optimista presenta covarianzas pequeñas y errores grandes, y no avisa. La decisión central: ¿cómo sé, con una prueba estadística, si mi filtro es consistente y qué estadístico me avisa de qué fallo?
- 🔗 **Se estudia junto con:** NEES, consistente, Optimista, conservador.

📘 **Dónde se aprende:** [B74-C23 · Consistencia de filtros: innovaciones y pruebas NEES/NIS](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md).

### NMAD

- El NMAD es `1,4826` veces la mediana de las desviaciones absolutas respecto de la mediana; es robusto a atípicos.

💡 **Cómo se explica en la clase [B57-C31](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md):**
- Con 200 000 errores gaussianos de `σ = 2 m`: RMSE `2,002`, NMAD `2,008` y LE90 `3,298` (teoría `1,645σ = 3,290`).
- Los atípicos inflan el RMSE y casi no mueven el NMAD ni el LE90: el RMSE es la métrica más frágil.
- 🎯 **Por qué importa:** Decir «el MDE tiene 4 m de error» sin definir la métrica ni los puntos de control no significa nada. La decisión central: ¿qué métrica y qué intervalo de confianza reporto para que mi validación sea comparable y honesta?
- 🔗 **Se estudia junto con:** sesgo (ME), RMSE, LE90, punto de control.

📘 **Dónde se aprende:** [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md).

### NMSUS

- El NMSUS es el cuestionario modificado de usabilidad de NASA (8 ítems, 1 a 5).

💡 **Cómo se explica en la clase [B109-C12](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md):**
- Según la nota técnica de NASA, el NMSUS se puntúa con `NMSUS = 3,125 × ((Q1−1)+(5−Q2)+(Q3−1)+(5−Q4)+(Q5−1)+(5−Q6)+(Q7−1)+(5−Q8))`, con respuestas de `1` a `5`.
- La nota indica que el NMSUS fue tan fiable como el SUS en un estudio con `35` participantes; la nota es un resumen breve que se leyó completo; el estudio completo no se consultó.
- 🎯 **Por qué importa:** Sin medir, «esta distribución es mejor» es una opinión. La decisión central: ¿la diferencia entre dos maquetas es mayor que lo que daría el azar, y las personas que la evalúan coinciden entre sí?
- 🔗 **Se estudia junto con:** evaluación con maqueta, lista de verificación, prueba pareada, kappa de Cohen.

📘 **Dónde se aprende:** [B109-C12 · Evaluación de factores humanos de maquetas y distribuciones](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md).

### NNLS

- **Significa:** mínimos cuadrados no negativos (NNLS).
- Los mínimos cuadrados no negativos (NNLS) buscan las abundancias que mejor ajustan sin salir de `a ≥ 0`.
- Biblioteca: conjunto de espectros de referencia. NNLS: ajuste con pesos no negativos.

💡 **Cómo se explica en la clase [B59-C05](../programa/clases/B59/B59-C05-minerales-marcianos/CLASE.md):**
- Resolver con mínimos cuadrados no negativos y contrastar con SciPy.
- 🎯 **Por qué importa:** Antes de excavar hay que saber qué se excava. La decisión central: ¿qué rendimiento de agua se espera de una mezcla y con qué dispersión por el ruido?
- 🔗 **Se estudia junto con:** miembro extremo, desmezcla lineal, número de condición, rendimiento de agua.

📘 **Dónde se aprende:** [B59-C05 · Minerales marcianos](../programa/clases/B59/B59-C05-minerales-marcianos/CLASE.md); [B106-C22 · Fuentes e identificación de contaminantes del aire de cabina](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md).

### NPAE

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Los errores formales más grandes son los de `CA` y `NPAE`, que están más correlacionados con otros términos.
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?
- 🔗 **Se estudia junto con:** términos, IA, IE, CA.

📘 **Dónde se aprende:** [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### NRHO

- La NRHO es la parte casi rectilínea de la familia halo.

💡 **Cómo se explica en la clase [B76-C05](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md):**
- La evidencia es la ficha de una NRHO en el modelo CR3BP del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de una NRHO en el modelo CR3BP*: estado inicial, periodo, radios, resonancia, monodromia y comparación con la referencia publicada, con fuentes.
- ⚠️ **Error frecuente:** Presentar la NRHO del CR3BP como la de Gateway. Se corrige con 8.5.
- 🎯 **Por qué importa:** La NRHO es la órbita de referencia publicada para la estación Gateway. La decisión central: ¿cómo se calcula una órbita periódica inestable y qué tan cerca queda un modelo simple de la referencia en un modelo de efemérides?
- 🔗 **Se estudia junto con:** perilune, apolune, corrección diferencial, monodromia.

📘 **Dónde se aprende:** [B76-C05 · Órbitas NRHO](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md).

### NSPM-20

- NSPM-20 es la memoria presidencial de 2019 que fija el proceso de autorización de lanzamientos con sistemas nucleares espaciales.

💡 **Cómo se explica en la clase [B86-C18](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md):**
- La memoria presidencial NSPM-20 (2019) fija tres niveles de autorización de lanzamiento.
- Es el ejemplo conductor: la estructura de niveles es de NSPM-20 y los números dependen de un `A2` que no se consultó.
- 🎯 **Por qué importa:** Los límites de la energía nuclear en el espacio son tanto jurídicos y de seguridad como técnicos: quién aprueba, con qué análisis y con qué umbrales. Un ingeniero de potencia debe saber que estas decisiones existen y qué datos las gobiernan.
- 🔗 **Se estudia junto con:** niveles I, II y III, A2, TED, LEU.

📘 **Dónde se aprende:** [B86-C18 · Seguridad y licenciamiento energético](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md).

### OMM

- El OMM es el mensaje de elementos medios de CCSDS 502.0-B-3.
- GP son los elementos de perturbaciones generales; OMM es un mensaje de elementos orbitales por campos.

💡 **Cómo se explica en la clase [B74-C29](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md):**
- El mensaje tipo OMM resultante tiene `14` campos y `458` bytes; sus claves son ilustrativas y no se contrastaron con el estándar.
- *Descripción textual:* los elementos se escriben en un TLE de columnas fijas, se calcula el checksum, se lee por columnas, se obtienen magnitudes de dos cuerpos y un mensaje tipo OMM; el checksum determina qué errores se detectan.
- 🎯 **Por qué importa:** Un TLE mal copiado o mal leído da una órbita equivocada sin avisar. La decisión central: ¿qué errores detecta la suma de verificación, qué resolución tiene cada campo y qué significan realmente esos «elementos medios»?
- 🔗 **Se estudia junto con:** TLE, checksum, movimiento medio, teoría de elementos medios.

📘 **Dónde se aprende:** [B74-C29 · Formatos TLE y OMM de elementos orbitales](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md); [B118-C02 · Catálogos de objetos espaciales](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md).

### OOSM

- Una OOSM llega después de que el filtro avanzó más allá de su sello de tiempo.

💡 **Contexto en la clase [B74-C24](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md):**
- 🎯 **Por qué importa:** Una medida tardía contiene información valiosa pero tratarla mal puede dañar más que descartarla. La decisión central: ¿qué tratamiento de una medida tardía mejora el estimado sin romper la consistencia, y a qué coste?
- 🔗 **Se estudia junto con:** retardo, retrodicción, reprocesado, covarianza cruzada.

📘 **Dónde se aprende:** [B74-C24 · Medidas retardadas y fuera de secuencia en filtros de estimación](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md).

### OPD

- La OPD es la diferencia de camino óptico.

💡 **Cómo se explica en la clase [B43-C21](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md):**
- Una variación de índice `Δn = 2 × 10⁻⁶` en `30 mm` da `OPD = 60 nm`, comparable al presupuesto de un telescopio (C20).
- Estimar la OPD por falta de homogeneidad `Δn t`.
- 🎯 **Por qué importa:** Un telescopio refractor o un corrector necesita vidrios que compensen el color. La decisión central: ¿qué par de vidrios, con qué potencias, anula el cromatismo primario de un doblete y qué error aporta la falta de homogeneidad?
- 🔗 **Se estudia junto con:** ecuación de Sellmeier, número de Abbe, líneas, doblete acromático.

📘 **Dónde se aprende:** [B43-C21 · Selección de vidrios ópticos: catálogos, homogeneidad y diagramas](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md).

### ORU

- **Significa:** unidad reemplazable (ORU).
- La unidad reemplazable (ORU) es la que un robot puede cambiar.

💡 **Contexto en la clase [B97-C12](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR L["n, lambda, T"] --> MU["mu = n lambda T"] MU --> P["Poisson: P(k <= s)"] P --> A["(A) 95 % por tipo"] P --> B["(B) voraz por kg"] A --> C["confianza del conjunto"] B --> C C --> M["Monte Carlo"] ``` *Descripción textual:* de las tasas sale el número esperado de fallas;
- 🎯 **Por qué importa:** Pocos repuestos dejan la misión sin reparación posible; demasiados cargan masa. La confianza del conjunto, no la de cada pieza, es la que importa, y se obtiene con el producto de las probabilidades.
- 🔗 **Se estudia junto con:** tasa de falla, número esperado de fallas, distribución de Poisson, confianza.

📘 **Dónde se aprende:** [B97-C12 · Robots de mantenimiento](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md).

### OSR

- **Significa:** espejo solar óptico (OSR).
- El OSR (*optical solar reflector*) es un vidrio plateado de `α` baja y `ε` alta.
- Un espejo solar óptico (OSR) es un radiador de `α` bajo y `ε` alta.

💡 **Cómo se explica en la clase [B84-C34](../programa/clases/B84/B84-C34-tratamientos-y-recubrimientos-superficiales-de-componentes-espaciales/CLASE.md):**
- Ejercicio 1 · con los pasos indicados Calcula `α/ε` del OSR.
- Pintura blanca u OSR según la carga interna y la degradación.
- 🎯 **Por qué importa:** Cambiar el recubrimiento de una placa de aluminio cambia su temperatura de equilibrio en 400 K; la degradación en órbita lo desplaza decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la temperatura de una superficie en su rango y qué espesor de anodizado se necesita?
- 🔗 **Se estudia junto con:** temperatura de equilibrio, razón, anodizado.

📘 **Dónde se aprende:** [B84-C34 · Tratamientos y recubrimientos superficiales de componentes espaciales](../programa/clases/B84/B84-C34-tratamientos-y-recubrimientos-superficiales-de-componentes-espaciales/CLASE.md); [B85-C05 · Recubrimientos ópticos térmicos](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md).

### OTF

- La OTF: transformada normalizada de la PSF.

💡 **Cómo se explica en la clase [B42-C07](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md):**
- Si la PSF se toma cada 4 píxeles (1 por `λ/D`) la OTF medida suma `MTF(v) + MTF(1 − v)`:
- La OTF de una pupila ideal se anula en `D/λ`; para `D = 8 m` y `λ = 2,2 µm` ese corte es `3,64 × 10⁶ rad⁻¹ = 17,6 ciclos/arcsec`.
- ⚠️ **Error frecuente:** Confundir OTF con PSF. La OTF es su transformada.
- 🎯 **Por qué importa:** La OTF dice qué detalles (frecuencias espaciales) pasan por el sistema y cuáles se pierden; fija el muestreo necesario del detector. La decisión central: ¿hasta qué frecuencia transmite el telescopio y qué muestreo exige?
- 🔗 **Se estudia junto con:** MTF, frecuencia de corte, autocorrelación, muestreo de Nyquist.

📘 **Dónde se aprende:** [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md).

### P10

- P50, la mediana; P10, el que supera con `10 %`.

💡 **Cómo se explica en la clase [B67-C08](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md):**
- El laboratorio genera un texto con cinco secciones (alcance y datos, método, resultado con incertidumbre, qué domina, límites), rotula el bloque como sintético y verifica que `P10 > P50 > P90`.
- Paso 4 · P10 y P90. `147,74 · 1,444 = 213,3 kt`;
- ⚠️ **Error frecuente:** Invertir P90 y P10. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Un informe que da un único número invita a decisiones frágiles; uno que da un intervalo mal calibrado, también. La decisión central: ¿qué cifras y qué advertencias debe llevar un informe de disponibilidad para que quien decide sepa cuánto puede confiar en él?
- 🔗 **Se estudia junto con:** P90, P50, disponibilidad, contribución a la varianza.

📘 **Dónde se aprende:** [B67-C08 · Informe de disponibilidad de volátiles con incertidumbre](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md).

### P50

- P90 es el valor que la masa supera con probabilidad `90 %` (el lado conservador); P50, la mediana;

💡 **Cómo se explica en la clase [B67-C08](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md):**
- El laboratorio genera un texto con cinco secciones (alcance y datos, método, resultado con incertidumbre, qué domina, límites), rotula el bloque como sintético y verifica que `P10 > P50 > P90`.
- Siete factores sintéticos con medianas y sigmas logarítmicas inventadas dan una masa disponible de mediana `147,74 kt` con `σ_ln = 0,2867`: `P90 = 102,3 kt`, `P50 = 147,7 kt`, `P10 = 213,3 kt`; la probabilidad de disponer de al menos `150 kt` es `47,9 %`.
- 🎯 **Por qué importa:** Un informe que da un único número invita a decisiones frágiles; uno que da un intervalo mal calibrado, también. La decisión central: ¿qué cifras y qué advertencias debe llevar un informe de disponibilidad para que quien decide sepa cuánto puede confiar en él?
- 🔗 **Se estudia junto con:** P90, P10, disponibilidad, contribución a la varianza.

📘 **Dónde se aprende:** [B67-C08 · Informe de disponibilidad de volátiles con incertidumbre](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md).

### P90

- P90 es el valor que la masa supera con probabilidad `90 %` (el lado conservador);

💡 **Cómo se explica en la clase [B67-C08](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md):**
- El laboratorio genera un texto con cinco secciones (alcance y datos, método, resultado con incertidumbre, qué domina, límites), rotula el bloque como sintético y verifica que `P10 > P50 > P90`.
- Paso 4 · P10 y P90. `147,74 · 1,444 = 213,3 kt`;
- ⚠️ **Error frecuente:** Invertir P90 y P10. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Un informe que da un único número invita a decisiones frágiles; uno que da un intervalo mal calibrado, también. La decisión central: ¿qué cifras y qué advertencias debe llevar un informe de disponibilidad para que quien decide sepa cuánto puede confiar en él?
- 🔗 **Se estudia junto con:** P50, P10, disponibilidad, contribución a la varianza.

📘 **Dónde se aprende:** [B67-C08 · Informe de disponibilidad de volátiles con incertidumbre](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md).

### PAL

- El PAL multiplica el basal para dar el gasto total.

💡 **Cómo se explica en la clase [B105-C12](../programa/clases/B105/B105-C12-nutricion-espacial/CLASE.md):**
- Con 75 kg, 178 cm, 40 años, hombre: `750 + 1.112,5 − 200 + 5 = 1.667,5 kcal/día`; con `PAL = 1,6`: `2.668 kcal/día`.
- Con `PAL ~ N(1,6; 0,15)`, la masa va de 456 a 623 kg (p5–p95): cubrir el p95 exige 84 kg más (15,6 %).
- 🎯 **Por qué importa:** Cada kilogramo de alimento que se lanza cuesta; cada kilocaloría que falta se paga con masa corporal. La decisión central: ¿cuánto alimento hay que transportar para una misión y con qué margen frente a la incertidumbre del gasto?
- 🔗 **Se estudia junto con:** ecuación de Mifflin–St Jeor, factores de Atwater, factor de empaque.

📘 **Dónde se aprende:** [B105-C12 · Nutrición espacial](../programa/clases/B105/B105-C12-nutricion-espacial/CLASE.md).

### PCK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- Por tipo: SPK, CK, PCK, IK, FK, LSK, SCLK.
- Un meta-kernel sintético carga 6 archivos (LSK, SCLK, PCK y tres SPK) en orden; para el cuerpo «NAVE» dos SPK se solapan entre 400 y 600 s y gana el cargado después; la cobertura efectiva deja un hueco desde el segundo `901`.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, CK, IK.

📘 **Dónde se aprende:** [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### PDF

- Los PDF son láminas de deformación planares en el cuarzo.

💡 **Cómo se explica en la clase [B61-C05](../programa/clases/B61/B61-C05-fusion-por-impacto-y-metamorfismo-de-choque/CLASE.md):**
- Umbrales (de resúmenes de terceros): PDF desde ≈ 10 GPa, vidrio diaplectico ≈ 30–40 GPa, fusión > ≈ 60 GPa; dependen de la temperatura previa.
- P --> K["clasificar: PDF / diaplectico / fusión"]
- 🎯 **Por qué importa:** Las rocas con rasgos de choque son la evidencia de un impacto. La decisión central: ¿qué presión produce cada efecto y cuánta roca se funde?
- 🔗 **Se estudia junto con:** Hugoniot, impedancia, metamorfismo de choque, vidrio diaplectico.

📘 **Dónde se aprende:** [B61-C05 · Fusión por impacto y metamorfismo de choque](../programa/clases/B61/B61-C05-fusion-por-impacto-y-metamorfismo-de-choque/CLASE.md).
