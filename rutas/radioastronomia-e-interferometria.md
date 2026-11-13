# 📡 Radioastronomía e interferometría

> Observas el universo con ondas de radio: diseñas antenas y receptores de bajo ruido, combinas varias antenas como un interferómetro y reduces los datos para obtener imágenes y espectros.
>
> **Nivel de entrada:** física de ondas, electromagnetismo y procesamiento de señales, más programación; rol técnico y de investigación · **Foco:** antenas y receptores, radiofrecuencia, interferometría, calibración, correlación y reducción de datos · **Entrega:** un sistema de recepción o un análisis interferométrico con su calibración, su presupuesto de ruido y datos reducidos reproducibles

## 🧭 Qué es y por qué importa

La radioastronomía observa el cielo en longitudes de onda largas, desde el decímetro hasta el milímetro. La señal que llega es extremadamente débil: el trabajo consiste en **recogerla con una antena, amplificarla con poco ruido, digitalizarla y, si hay varias antenas, correlacionarlas** para lograr imágenes de alta resolución. Un interferómetro consigue así la resolución de una antena de tamaño mucho mayor que cada plato individual.

ALMA ilustra la escala del oficio: según su propia página, está en la meseta de Chajnantor, en el desierto de Atacama, en Chile, y se compone de 66 antenas de alta precisión que operan como un solo instrumento, con separaciones entre 150 metros y 16 kilómetros y longitudes de onda de 0,32 a 3,6 mm.

El rol se reparte en tres miradas:

- **Hardware de recepción.** Antenas, receptores de bajo ruido, osciladores estables y cadena de radiofrecuencia. Su pregunta es: *¿cuánto ruido agrego y cómo lo mido?*
- **Interferometría.** Calibración de fase, correlación y síntesis de apertura. Su pregunta es: *¿qué errores de fase y de amplitud limitan mi imagen?*
- **Reducción de datos.** Del dato crudo a la imagen calibrada, con su incertidumbre. Su pregunta es: *¿qué le debo a la calibración y qué es señal real?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es óptica.** Comparte la teoría de aperturas, pero trabaja con antenas, receptores y electrónica distinta ([Ingeniería óptica y telescopios profesionales](ingenieria-optica-y-telescopios-profesionales.md)).
- **No es telecomunicaciones.** Una estación de comunicaciones busca transmitir información; tú buscas medir una señal natural muy débil ([Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md)).
- **No es astrofísica de objetos.** Interpretar la fuente es el trabajo de quien estudia ese objeto ([Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md)); tú aseguras que el dato sea confiable.
- **No es «usar un radiotelescopio».** Observar con un instrumento ya construido es una parte; este rol llega hasta su diseño y su calibración.

## 🗓️ Un día en el puesto

- **Cadena de recepción:** mides ruido y ganancia de un receptor, ajustas y documentas.
- **Calibración:** estimas errores de fase y amplitud con una fuente conocida y verificas que la calibración se mantiene.
- **Reducción de datos:** corres un flujo de procesamiento, revisas artefactos y repites con otro criterio de edición.
- **Código:** mucho análisis y automatización en Python o similar.
- **Revisión con el equipo:** discutes qué datos se descartan y por qué.

Dicho sin adornos: la mayor parte del tiempo se va en **separar señal de error**, y casi todos los errores se parecen a una señal.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Radioastronomía y propagación:** espectro radio, antenas, ruido de sistema y radiometría ([**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md)).
- **Antenas y receptores:** diseño, ganancia, temperatura de ruido ([**B49** · Antenas y receptores de radioastronomía](../programa/tronco-comun/B49-antenas-y-receptores-de-radioastronomia.md)).
- **Interferometría y reducción de datos:** líneas de base, correladores, calibración y síntesis ([**B51** · Interferometría avanzada y reducción de datos de radio](../programa/tronco-comun/B51-interferometria-avanzada-y-reduccion-de-datos-de-radio.md), [**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md)).
- **Señales e imágenes:** procesamiento, transformadas y estimación ([**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)).
- **Metrología y tiempo:** estabilidad de frecuencia y sincronización ([**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)).
- **Computación científica:** reducción de datos reproducible ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).

### Herramientas del oficio

```text
Instrumentación:       analizadores de espectro, generadores de señal, radios definidas por software
Cálculo y datos:      Python científico y paquetes de reducción de datos interferométricos
Calibración:          fuentes de referencia y procedimientos de calibración de fase y amplitud
Control:              sistemas de adquisición y sincronización de tiempo y frecuencia
Documentación:        registros de calibración y bitácoras
```

Una cadena de radiofrecuencia mal caracterizada produce datos precisos y falsos. Lo que se paga es tu capacidad de medir tus propios errores.

### Habilidades no técnicas

- **Meticulosidad experimental:** registrar cada ajuste y cada condición.
- **Paciencia ante la depuración:** encontrar la fuente de una interferencia puede llevar días.
- **Comunicación con astrónomos e ingenieros.**
- **Trabajo en equipos internacionales y multilingües.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B05** · Física fundamental para el espacio](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md) — A01 · 20 clases
2. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
3. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
4. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
5. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases
6. 📚 [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md) — A04 · 24 clases
7. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — A04 · 25 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 2 de 26 clases: `B12-` C05, C16
2. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 10 de 23 clases: `B13-` C05, C07, C11–C12, C17–C22
3. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 8 de 31 clases: `B14-` C05–C06, C10, C12–C14, C16, C19
4. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — usa 8 de 24 clases: `B15-` C02, C05–C08, C11–C12, C16

**A03 · Astrofísica y ciencias fundamentales del universo**

5. 📚 [**B30** · Heliofísica y física de plasmas](../programa/tronco-comun/B30-heliofisica-y-fisica-de-plasmas.md) — usa 1 de 23 clases: `B30-` C21

**A04 · Óptica, telescopios y observatorios científicos**

6. 📚 [**B42** · Óptica física y óptica adaptativa](../programa/tronco-comun/B42-optica-fisica-y-optica-adaptativa.md) — usa 1 de 24 clases: `B42-` C08
7. 📚 [**B44** · Detectores y adquisición astronómica](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md) — usa 1 de 20 clases: `B44-` C19
8. 📚 [**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md) — usa 17 de 20 clases: `B46-` C03–C11, C13–C20
9. 📚 [**B48** · Operaciones de observatorios científicos](../programa/tronco-comun/B48-operaciones-de-observatorios-cientificos.md) — usa 1 de 23 clases: `B48-` C17
10. 📚 [**B49** · Antenas y receptores de radioastronomía](../programa/tronco-comun/B49-antenas-y-receptores-de-radioastronomia.md) — usa 11 de 11 clases: `B49-` C01–C11
11. 📚 [**B51** · Interferometría avanzada y reducción de datos de radio](../programa/tronco-comun/B51-interferometria-avanzada-y-reduccion-de-datos-de-radio.md) — usa 14 de 14 clases: `B51-` C01–C14

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

12. 📚 [**B53** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md) — usa 1 de 30 clases: `B53-` C04
13. 📚 [**B57** · Observación terrestre y geociencias orbitales](../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md) — usa 1 de 34 clases: `B57-` C10

**A06 · Mecánica orbital, navegación y vuelo espacial**

14. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 2 de 30 clases: `B74-` C01, C07

**A07 · Ingeniería y construcción de sistemas espaciales**

15. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 2 de 25 clases: `B89-` C06–C07
16. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 2 de 24 clases: `B90-` C13–C14

**A10 · Entorno orbital, derecho y seguridad espacial**

17. 📚 [**B118** · Tráfico espacial y sostenibilidad orbital](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md) — usa 1 de 24 clases: `B118-` C17

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes calcular la ganancia y el ancho de haz de una antena de apertura circular?
- ¿Sabes qué es la temperatura de ruido de un receptor?
- ¿Entiendes la transformada de Fourier y su relación con el muestreo?
- ¿Programas un filtro digital sencillo sobre una señal?

#### R04-M01 · Ingeniería de antenas

1. **Antenas dipolo y monopolo** — [`B49-C01`](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md)
2. **Antenas parabólicas** — [`B46-C03`](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md)
3. **Diagramas de radiación** — [`B46-C04`](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md)
4. **Ganancia y apertura efectiva** — [`B46-C05`](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md), [`B89-C06`](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md)
5. **Polarización de antenas** — [`B46-C13`](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md), [`B42-C08`](../programa/clases/B42/B42-C08-polarizacion-de-la-luz/CLASE.md)
6. **Temperatura de ruido** — [`B46-C05`](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md), [`B46-C06`](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md)
7. **Impedancias y adaptación** — [`B49-C02`](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md)
8. **Apuntado de antenas** — [`B49-C03`](../programa/clases/B49/B49-C03-apuntamiento-y-seguimiento-de-radiotelescopios-modelos-de-apuntado-y-errores/CLASE.md)
9. **Arreglos de antenas** — [`B49-C04`](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md)
10. **Calibración de patrones** — [`B49-C05`](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md)

✅ **Checkpoint R04-M01.** Sin mirar el material, explica cómo se relacionan «Antenas dipolo y monopolo», «Temperatura de ruido» y «Calibración de patrones», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R04-M02 · Receptores de bajo ruido

1. **Ruido térmico** — [`B46-C06`](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md)
2. **Amplificadores LNA** — [`B49-C06`](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md)
3. **Criogenia de receptores** — [`B49-C07`](../programa/clases/B49/B49-C07-criogenia-y-refrigeracion-de-receptores-de-radio/CLASE.md)
4. **Figura de ruido** — [`B89-C07`](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md), [`B46-C06`](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md)
5. **Estabilidad de ganancia** — [`B49-C08`](../programa/clases/B49/B49-C08-estabilidad-de-ganancia-de-receptores-y-variaciones-de-ganancia/CLASE.md)
6. **Ancho de banda efectivo** — [`B46-C06`](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md)
7. **Linealidad de receptor** — [`B49-C09`](../programa/clases/B49/B49-C09-linealidad-compresion-e-intermodulacion-de-receptores-de-rf/CLASE.md)
8. **Calibración de temperatura** — [`B13-C17`](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md), [`B46-C06`](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md)
9. **Interferencias de radiofrecuencia** — [`B118-C17`](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md), [`B90-C14`](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md)
10. **Evaluación de sensibilidad** — [`B46-C06`](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md), [`B46-C20`](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md)

✅ **Checkpoint R04-M02.** Sin mirar el material, explica cómo se relacionan «Ruido térmico», «Ancho de banda efectivo» y «Evaluación de sensibilidad», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R04-M03 · Radiofrecuencia y cadenas de recepción

1. **Amplificación en radiofrecuencia** — [`B46-C07`](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md)
2. **Filtros pasabanda** — [`B49-C10`](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md)
3. **Conversión de frecuencia** — [`B46-C07`](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md)
4. **Osciladores locales** — [`B46-C08`](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md)
5. **Relojes y fase** — [`B46-C08`](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md), [`B13-C07`](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md)
6. **Mezcladores de frecuencia** — [`B49-C11`](../programa/clases/B49/B49-C11-mezcladores-de-frecuencia-perdida-de-conversion-y-productos-espurios/CLASE.md)
7. **Digitalización de IF** — [`B46-C09`](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md), [`B15-C02`](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md)
8. **Blindaje electromagnético** — [`B90-C13`](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md), [`B90-C14`](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md)
9. **Compatibilidad RF** — [`B90-C13`](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md), [`B118-C17`](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md)
10. **Ensayo de cadena de recepción** — [`B13-C20`](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md), [`B13-C17`](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md)

✅ **Checkpoint R04-M03.** Sin mirar el material, explica cómo se relacionan «Amplificación en radiofrecuencia», «Mezcladores de frecuencia» y «Ensayo de cadena de recepción», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R04-M04 · Radioastronomía con SDR

1. **Plataformas de radio definida por software** — [`B46-C10`](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md)
2. **Ganancia y muestreo SDR** — [`B46-C10`](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md), [`B15-C02`](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md), [`B46-C09`](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md)
3. **Calibración de frecuencias** — [`B46-C08`](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md), [`B13-C05`](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md)
4. **Espectrogramas astronómicos** — [`B15-C06`](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md), [`B46-C10`](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md)
5. **Observación de radio solar** — [`B30-C21`](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md)
6. **Recepción de hidrógeno neutral** — [`B46-C11`](../programa/clases/B46/B46-C11-observacion-de-hidrogeno-a-21-centimetros/CLASE.md)
7. **Interferencias locales** — [`B118-C17`](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md)
8. **Filtrado de señales** — [`B15-C07`](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md), [`B15-C06`](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md)
9. **Registro de observaciones** — [`B48-C17`](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md), [`B13-C19`](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md)
10. **Validación de observaciones caseras** — [`B46-C20`](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md), [`B13-C18`](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md)

✅ **Checkpoint R04-M04.** Sin mirar el material, explica cómo se relacionan «Plataformas de radio definida por software», «Recepción de hidrógeno neutral» y «Validación de observaciones caseras», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R04-M05 · Calibración de interferómetros

1. **Visibilidades interferométricas** — [`B46-C15`](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md)
2. **Calibradores de fase** — [`B46-C17`](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md)
3. **Calibradores de amplitud** — [`B51-C01`](../programa/clases/B51/B51-C01-calibracion-de-amplitud-y-escala-de-flujo-con-calibradores-primarios/CLASE.md)
4. **Cierre de fase** — [`B51-C02`](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md)
5. **Ganancias complejas** — [`B51-C03`](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md)
6. **Errores de banda** — [`B51-C04`](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md)
7. **Corrección ionosférica** — [`B51-C05`](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md)
8. **Auto calibración** — [`B51-C06`](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md)
9. **Evaluación de residuos** — [`B51-C07`](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md)
10. **Validación de imágenes calibradas** — [`B46-C19`](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md), [`B13-C18`](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md)

✅ **Checkpoint R04-M05.** Sin mirar el material, explica cómo se relacionan «Visibilidades interferométricas», «Errores de banda» y «Validación de imágenes calibradas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R04-M06 · Correlación de señales astronómicas

1. **Muestreo de señales** — [`B15-C02`](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md), [`B46-C09`](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md)
2. **Alineación temporal** — [`B51-C08`](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md)
3. **Correlación cruzada** — [`B46-C15`](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md), [`B12-C05`](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md)
4. **Correladores FX** — [`B46-C15`](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md), [`B15-C05`](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md)
5. **Correladores XF** — [`B46-C15`](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md), [`B15-C08`](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md)
6. **Geometría de líneas de base** — [`B46-C14`](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md)
7. **Fringe stopping** — [`B51-C09`](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md)
8. **Canalización espectral** — [`B15-C05`](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md), [`B15-C06`](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md)
9. **Capacidad de procesamiento** — [`B14-C13`](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md), [`B14-C14`](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md), [`B14-C16`](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md)
10. **Prueba numérica de correlador** — [`B14-C10`](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md)

✅ **Checkpoint R04-M06.** Sin mirar el material, explica cómo se relacionan «Muestreo de señales», «Geometría de líneas de base» y «Prueba numérica de correlador», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R04-M07 · VLBI y geodesia

1. **Redes de antenas geodésicas** — [`B46-C18`](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md), [`B13-C11`](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md)
2. **Relojes atómicos de estación** — [`B13-C07`](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md), [`B46-C08`](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md)
3. **Retardos geométricos** — [`B46-C14`](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md), [`B46-C18`](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md)
4. **Retardos atmosféricos** — [`B51-C10`](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md)
5. **Fringes VLBI** — [`B51-C11`](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md)
6. **Sistemas de referencia celestes** — [`B13-C21`](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md)
7. **Rotación terrestre** — [`B13-C22`](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md)
8. **Análisis de observaciones VLBI** — [`B46-C18`](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md), [`B74-C07`](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md), [`B74-C01`](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md)
9. **Geodesia de alta precisión** — [`B57-C10`](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md), [`B46-C18`](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md), [`B53-C04`](../programa/clases/B53/B53-C04-geoides-y-elipsoides/CLASE.md)
10. **Estándares de archivos VLBI** — [`B51-C12`](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md)

✅ **Checkpoint R04-M07.** Sin mirar el material, explica cómo se relacionan «Redes de antenas geodésicas», «Sistemas de referencia celestes» y «Estándares de archivos VLBI», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R04-M08 · Reducción profesional de datos de radio

1. **Importación de visibilidades** — [`B46-C15`](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md), [`B14-C05`](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md)
2. **Inspección de metadatos** — [`B44-C19`](../programa/clases/B44/B44-C19-formato-fits-y-metadatos/CLASE.md), [`B14-C06`](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md)
3. **Marcado de datos espurios** — [`B51-C13`](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md)
4. **Calibración de banda** — [`B51-C14`](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md)
5. **Síntesis de apertura** — [`B46-C16`](../programa/clases/B46/B46-C16-sintesis-de-apertura/CLASE.md)
6. **Algoritmo CLEAN** — [`B46-C19`](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md)
7. **Restauración de imágenes** — [`B15-C11`](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md), [`B46-C19`](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md)
8. **Medición de flujo** — [`B15-C12`](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md), [`B15-C16`](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md), [`B13-C17`](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md)
9. **Incertidumbre de imágenes** — [`B12-C16`](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md), [`B13-C12`](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md)
10. **Archivo científico reproducible** — [`B14-C19`](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md), [`B14-C12`](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md), [`B48-C17`](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md)

✅ **Checkpoint R04-M08.** Sin mirar el material, explica cómo se relacionan «Importación de visibilidades», «Algoritmo CLEAN» y «Archivo científico reproducible», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Observación de la línea de 21 cm con un receptor propio.** Diseña, calibra y opera una cadena de recepción de bajo costo para detectar la línea de hidrógeno neutro y estima la rotación de la galaxia con tus datos.

Entregables:

- Diagrama de la cadena con presupuesto de ruido
- Procedimiento de calibración con patrón conocido
- Espectros reducidos con su incertidumbre
- Curva de velocidad con la interpretación y sus límites

Criterios de evaluación:

- El presupuesto de ruido concuerda con lo medido
- La calibración es reproducible por otra persona
- La interferencia se identifica y se trata
- Se declara la resolución y la sensibilidad obtenidas

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes dimensionar una cadena de recepción de radio y verificar su sensibilidad.
- Puedes reducir datos de radio y de interferometría con calibración documentada.
- Puedes explicar cómo la correlación de señales produce imágenes.

<!-- /recorrido -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **sistema o un análisis radioastronómico documentado**:

- un presupuesto de ruido de una cadena de recepción con mediciones;
- una observación o simulación interferométrica con calibración explícita;
- datos reducidos con sus incertidumbres y un registro de decisiones de edición;
- una comparación con una fuente o un resultado de referencia;
- el código y los datos para repetirlo.

Los bloques de la ruta aportan ejercicios y laboratorios para cada pieza; guarda la primera versión y los cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada. Referencia de trabajo consultada (2026-11-05):

- 📘 **ALMA Observatory** — página «About ALMA» (https://www.almaobservatory.org/en/about-alma/): describe el observatorio en la meseta de Chajnantor, construido por ESO, NRAO y NAOJ con la República de Chile; 66 antenas de alta precisión, longitudes de onda de 0,32 a 3,6 mm.

Las normas de protección del espectro y de acceso a tiempo de observación dependen de cada observatorio y de la regulación vigente, y no están verificadas aquí.

## 📈 Progresión del rol

Rutas habituales: **ingeniero/a o científico/a de datos de radio → especialista en calibración o en receptores → responsable de un instrumento o de un flujo de reducción**. Se abren la instrumentación de telecomunicaciones y la metrología de tiempo y frecuencia. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Ingeniería óptica y telescopios profesionales](ingenieria-optica-y-telescopios-profesionales.md), [Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md) y [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md).

## ⚠️ Mitos y errores comunes

- **«El radiotelescopio solo escucha».** Mide potencia, fase y polarización, y su análisis es tan exigente como el óptico.
- **«Más antenas es siempre mejor imagen».** Sin buena calibración y cobertura de líneas de base, la imagen se degrada.
- **«La interferencia es un detalle».** Es uno de los límites principales del oficio.
- **«El dato calibrado es la verdad».** Es la mejor estimación posible con los errores que no se pudieron eliminar.
- **«Es solo electrónica».** Es electrónica, física de ondas, estadística y programación juntas.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la física de ondas de tu diagnóstico.
2. Estudia **radioastronomía** ([**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md)) y **señales e imágenes** ([**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)).
3. Profundiza en **antenas y receptores** ([**B49** · Antenas y receptores de radioastronomía](../programa/tronco-comun/B49-antenas-y-receptores-de-radioastronomia.md)).
4. Avanza a **interferometría y reducción de datos** ([**B51** · Interferometría avanzada y reducción de datos de radio](../programa/tronco-comun/B51-interferometria-avanzada-y-reduccion-de-datos-de-radio.md)).
5. Reúne tu **análisis documentado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ingeniería óptica y telescopios profesionales](ingenieria-optica-y-telescopios-profesionales.md) · [Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md) · [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R04-radioastronomia-e-interferometria/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
