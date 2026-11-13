# 🧭 Navegación guiado y autonomía espacial

> Haces que un vehículo sepa dónde está y hacia dónde va, y decida qué hacer: estimación de estado, fusión de sensores, guiado y autonomía a bordo.
>
> **Nivel de entrada:** matemática, control y programación de nivel universitario; rol técnico de ingeniería · **Foco:** navegación inercial, filtros de estimación, fusión multisensorial, guiado, control, autonomía y decisión a bordo · **Entrega:** un estimador o un lazo de guiado simulado y verificado, con su análisis de error y su comportamiento ante fallas de sensores

## 🧭 Qué es y por qué importa

Un vehículo espacial rara vez puede preguntarle a alguien dónde está. Debe **estimarlo** combinando sensores imperfectos: acelerómetros y giroscopios que derivan, cámaras, mediciones de seguimiento. La estimación de estado convierte esas mediciones ruidosas en una posición, una velocidad y una actitud con incertidumbre conocida.

Con esa estimación, el guiado decide qué maniobra corresponde y el control la ejecuta. Cuando el retardo de comunicación impide la teleoperación, parte de la decisión pasa **a bordo**, y ahí entra la autonomía.

Las miradas del rol son:

- **Estimación.** Filtros y fusión de sensores. Su pregunta es: *¿qué sé del estado, y con cuánta incertidumbre?*
- **Guiado y control.** Cierre del lazo. Su pregunta es: *¿qué acción lleva al vehículo a donde debe, de forma estable?*
- **Autonomía.** Decisión sin intervención. Su pregunta es: *¿qué debe decidir el vehículo solo y qué no?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es diseño de trayectorias.** Esa define la ruta nominal ([Astrodinámica interplanetaria](astrodinamica-interplanetaria.md)); tú haces que el vehículo la siga con lo que mide.
- **No es aviónica.** La aviónica es la plataforma de cómputo y software donde esto corre ([Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md)).
- **No es robótica general.** Comparte algoritmos, pero con restricciones de espacio, retardo y fiabilidad.
- **No es «aplicar un filtro de libro».** El filtro correcto depende de las no linealidades y del modelo de error.

## 🗓️ Un día en el puesto

- **Modelo de sensores:** caracterizas el ruido y la deriva de cada sensor.
- **Estimador:** ajustas un filtro y revisas su consistencia.
- **Simulación:** pruebas el lazo completo con fallas de sensores inyectadas.
- **Análisis de error:** acotas la incertidumbre del estado resultante.
- **Revisión con aviónica y con operaciones:** acuerdas qué se decide a bordo.

Dicho sin adornos: **un filtro que reporta poca incertidumbre y se equivoca mucho** es peor que uno modesto y honesto.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Estimación de órbitas y navegación** ([**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md)); **navegación inercial y fusión multisensorial** ([**B80** · Navegación inercial y fusión multisensorial](../programa/tronco-comun/B80-navegacion-inercial-y-fusion-multisensorial.md)).
- **Sistemas dinámicos y control** ([**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md)); **sensores y control de actitud** ([**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md)).
- **Autonomía y teleoperación** ([**B98** · Autonomía y teleoperación espacial](../programa/tronco-comun/B98-autonomia-y-teleoperacion-espacial.md)); **localización y mapeo** ([**B99** · Localización y mapeo robótico](../programa/tronco-comun/B99-localizacion-y-mapeo-robotico.md)).
- **Probabilidad y estadística** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)); **señales e imágenes** ([**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)).
- **Simulación numérica** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)).

### Herramientas del oficio

```text
Simulación:           Python científico y entornos de simulación de dinámica
Estimación:           filtros de Kalman y variantes, filtros de partículas
Pruebas:              inyección de fallas y casos de borde
Código:               lenguaje compilado para el lazo en tiempo real
Documentación:        registro de modelos de sensores y de parámetros
```

Un estimador probado solo con ruido ideal falla con ruido real. Prueba con errores de modelo y con sensores degradados.

### Habilidades no técnicas

- **Pensar en modos de falla.**
- **Comunicación con diseñadores de trayectoria y de software de vuelo.**
- **Documentación rigurosa de supuestos.**
- **Prudencia con lo que se delega a la autonomía.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
2. 📚 [**B73** · Mecánica celeste, resonancias y caos](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md) — A06 · 22 clases
3. 📚 [**B75** · Trayectorias y misiones interplanetarias](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md) — A06 · 30 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — usa 1 de 20 clases: `B10-` C16
2. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — usa 2 de 26 clases: `B11-` C09, C19
3. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 7 de 26 clases: `B12-` C07, C11, C14, C16–C19
4. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 5 de 23 clases: `B13-` C04, C08, C11, C13, C16
5. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 1 de 31 clases: `B14-` C10
6. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — usa 5 de 24 clases: `B15-` C03, C12, C14, C17–C18
7. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — usa 4 de 20 clases: `B16-` C01–C02, C13, C19

**A04 · Óptica, telescopios y observatorios científicos**

8. 📚 [**B44** · Detectores y adquisición astronómica](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md) — usa 1 de 20 clases: `B44-` C06
9. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — usa 2 de 25 clases: `B47-` C10, C14

**A06 · Mecánica orbital, navegación y vuelo espacial**

10. 📚 [**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md) — usa 1 de 20 clases: `B71-` C02
11. 📚 [**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md) — usa 1 de 21 clases: `B72-` C02
12. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 23 de 30 clases: `B74-` C01–C04, C06–C10, C12–C20, C23–C27
13. 📚 [**B76** · Dinámica cislunar y operaciones de proximidad](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md) — usa 10 de 20 clases: `B76-` C09–C14, C16–C18, C20
14. 📚 [**B80** · Navegación inercial y fusión multisensorial](../programa/tronco-comun/B80-navegacion-inercial-y-fusion-multisensorial.md) — usa 8 de 9 clases: `B80-` C01–C08

**A07 · Ingeniería y construcción de sistemas espaciales**

15. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 1 de 24 clases: `B83-` C17
16. 📚 [**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md) — usa 10 de 22 clases: `B87-` C03–C09, C15, C19, C21
17. 📚 [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md) — usa 5 de 44 clases: `B88-` C05, C11–C12, C14, C16
18. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 1 de 25 clases: `B89-` C15
19. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 1 de 24 clases: `B90-` C16

**A08 · Operaciones de misión y robótica espacial**

20. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 6 de 30 clases: `B96-` C03, C05, C07–C08, C13, C15
21. 📚 [**B97** · Robótica y construcción extraterrestre](../programa/tronco-comun/B97-robotica-y-construccion-extraterrestre.md) — usa 3 de 27 clases: `B97-` C07, C16–C17
22. 📚 [**B98** · Autonomía y teleoperación espacial](../programa/tronco-comun/B98-autonomia-y-teleoperacion-espacial.md) — usa 2 de 8 clases: `B98-` C01–C02

**A10 · Entorno orbital, derecho y seguridad espacial**

23. 📚 [**B118** · Tráfico espacial y sostenibilidad orbital](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md) — usa 1 de 24 clases: `B118-` C07

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Sabes qué mide un giróscopo y qué un acelerómetro, y cómo derivan?
- ¿Puedes aplicar un filtro de promedio móvil y explicar su retardo?
- ¿Manejas rotaciones en 3D (matrices y cuaterniones)?
- ¿Entiendes el concepto de covarianza?

#### R10-M01 · Sensores de orientación

1. **Sensores solares** — [`B87-C03`](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md)
2. **Sensores de horizonte** — [`B87-C04`](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md)
3. **Magnetómetros triaxiales** — [`B87-C05`](../programa/clases/B87/B87-C05-magnetometros/CLASE.md)
4. **Giroscopios** — [`B87-C06`](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md)
5. **Star trackers** — [`B87-C07`](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md), [`B74-C14`](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md)
6. **Errores de alineación** — [`B87-C08`](../programa/clases/B87/B87-C08-calibracion-de-sensores/CLASE.md), [`B13-C04`](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md)
7. **Sesgos térmicos** — [`B13-C16`](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md), [`B87-C08`](../programa/clases/B87/B87-C08-calibracion-de-sensores/CLASE.md)
8. **Calibración de orientación** — [`B87-C08`](../programa/clases/B87/B87-C08-calibracion-de-sensores/CLASE.md)
9. **Modelado de mediciones** — [`B74-C01`](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md), [`B87-C09`](../programa/clases/B87/B87-C09-estimacion-de-actitud/CLASE.md)
10. **Presupuesto de error angular** — [`B13-C13`](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md), [`B87-C15`](../programa/clases/B87/B87-C15-apuntamiento-de-alta-precision/CLASE.md), [`B47-C10`](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md)

✅ **Checkpoint R10-M01.** Sin mirar el material, explica cómo se relacionan «Sensores solares», «Errores de alineación» y «Presupuesto de error angular», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R10-M02 · Navegación inercial espacial

1. **Navegación inercial** — [`B80-C01`](../programa/clases/B80/B80-C01-principios-de-navegacion-inercial-espacial/CLASE.md)
2. **Modelo de acelerómetros** — [`B80-C02`](../programa/clases/B80/B80-C02-modelo-de-error-de-acelerometros/CLASE.md)
3. **Integración strapdown** — [`B80-C03`](../programa/clases/B80/B80-C03-mecanizacion-strapdown-e-integracion-de-actitud-y-velocidad/CLASE.md)
4. **Deriva de giroscopios** — [`B87-C06`](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md), [`B13-C04`](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md)
5. **Marcos de navegación** — [`B10-C16`](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md), [`B13-C11`](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md)
6. **Modelos de gravedad** — [`B72-C02`](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md), [`B71-C02`](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md)
7. **Corrección de sesgos** — [`B87-C08`](../programa/clases/B87/B87-C08-calibracion-de-sensores/CLASE.md), [`B74-C07`](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md)
8. **Fusión con otras mediciones** — [`B80-C04`](../programa/clases/B80/B80-C04-fusion-inercial-con-mediciones-externas-acoplamiento-debil-y-fuerte/CLASE.md)
9. **Navegación sin GPS** — [`B74-C13`](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md), [`B74-C14`](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md), [`B74-C17`](../programa/clases/B74/B74-C17-navegacion-en-espacio-profundo/CLASE.md), [`B74-C18`](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md)
10. **Evaluación de deriva acumulada** — [`B74-C19`](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md), [`B13-C13`](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md)

✅ **Checkpoint R10-M02.** Sin mirar el material, explica cómo se relacionan «Navegación inercial», «Modelos de gravedad» y «Evaluación de deriva acumulada», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R10-M03 · Filtrado y estimación de estado

1. **Estado dinámico y covarianza** — [`B16-C01`](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md), [`B16-C02`](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md), [`B12-C18`](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md)
2. **Filtro de Kalman** — [`B15-C17`](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md), [`B74-C08`](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md)
3. **Filtro de Kalman extendido** — [`B74-C09`](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md), [`B74-C10`](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md)
4. **Filtro unscented** — [`B74-C10`](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md)
5. **Filtro de partículas** — [`B15-C18`](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md)
6. **Observabilidad** — [`B16-C13`](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md), [`B74-C01`](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md)
7. **Consistencia estadística** — [`B74-C23`](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md)
8. **Procesamiento fuera de secuencia** — [`B74-C24`](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md)
9. **Manejo de fallos de sensores** — [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md), [`B12-C19`](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md)
10. **Validación con datos sintéticos** — [`B12-C14`](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md), [`B74-C20`](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md), [`B14-C10`](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md)

✅ **Checkpoint R10-M03.** Sin mirar el material, explica cómo se relacionan «Estado dinámico y covarianza», «Observabilidad» y «Validación con datos sintéticos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R10-M04 · Determinación orbital de precisión

1. **Medidas Doppler** — [`B74-C04`](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md), [`B89-C15`](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md)
2. **Medidas de rango** — [`B74-C03`](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md)
3. **Ángulos observados** — [`B74-C02`](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md)
4. **Determinación orbital inicial** — [`B74-C06`](../programa/clases/B74/B74-C06-determinacion-inicial-de-orbita/CLASE.md)
5. **Estimación por lotes** — [`B74-C07`](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md)
6. **Estabilidad numérica** — [`B11-C09`](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md), [`B11-C19`](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md)
7. **Estimación de parámetros dinámicos** — [`B74-C07`](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md), [`B12-C07`](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md)
8. **Seguimiento de estaciones** — [`B74-C15`](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md), [`B96-C05`](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md)
9. **Métricas de residual** — [`B74-C07`](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md), [`B74-C19`](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md)
10. **Comparación de órbitas estimadas** — [`B74-C20`](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md), [`B74-C12`](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md)

✅ **Checkpoint R10-M04.** Sin mirar el material, explica cómo se relacionan «Medidas Doppler», «Estabilidad numérica» y «Comparación de órbitas estimadas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R10-M05 · Navegación óptica autónoma

1. **Navegación por imágenes** — [`B74-C13`](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md)
2. **Detección de bordes planetarios** — [`B74-C25`](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md)
3. **Localización de hitos** — [`B74-C26`](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md)
4. **Navegación estelar** — [`B74-C14`](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md), [`B87-C07`](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md)
5. **Navegación por pulsar como investigación** — [`B74-C27`](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md)
6. **Pose relativa** — [`B76-C13`](../programa/clases/B76/B76-C13-sensores-de-proximidad/CLASE.md), [`B76-C17`](../programa/clases/B76/B76-C17-sistemas-de-referencia-relativos/CLASE.md)
7. **Cámaras de navegación** — [`B74-C13`](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md), [`B74-C14`](../programa/clases/B74/B74-C14-navegacion-con-camaras-estelares/CLASE.md)
8. **Matching de características** — [`B15-C14`](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md), [`B15-C12`](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md)
9. **Errores de iluminación** — [`B76-C18`](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md), [`B74-C13`](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md)
10. **Verificación de soluciones ópticas** — [`B74-C19`](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md), [`B74-C20`](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md), [`B83-C17`](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md)

✅ **Checkpoint R10-M05.** Sin mirar el material, explica cómo se relacionan «Navegación por imágenes», «Pose relativa» y «Verificación de soluciones ópticas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R10-M06 · Fusión multisensorial

1. **Sincronización multisensor** — [`B74-C16`](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md), [`B13-C08`](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md)
2. **Manejo de latencia** — [`B88-C05`](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md), [`B97-C07`](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md)
3. **Sensores redundantes** — [`B80-C05`](../programa/clases/B80/B80-C05-redundancia-de-sensores-y-arbitraje-de-mediciones/CLASE.md)
4. **Modelos de ruido** — [`B15-C03`](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md), [`B44-C06`](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md), [`B13-C04`](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md)
5. **Fusión IMU-cámara** — [`B80-C06`](../programa/clases/B80/B80-C06-fusion-imu-camara/CLASE.md)
6. **Fusión radio-óptica** — [`B80-C07`](../programa/clases/B80/B80-C07-fusion-radio-optica-en-navegacion-de-espacio-profundo/CLASE.md)
7. **Detección de discrepancias** — [`B96-C13`](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md), [`B12-C19`](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md)
8. **Filtrado distribuido** — [`B80-C08`](../programa/clases/B80/B80-C08-filtrado-distribuido-y-descentralizado/CLASE.md)
9. **Estimación robusta** — [`B12-C11`](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md), [`B12-C19`](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md)
10. **Evaluación de degradación sensorial** — [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md), [`B87-C08`](../programa/clases/B87/B87-C08-calibracion-de-sensores/CLASE.md), [`B47-C14`](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md)

✅ **Checkpoint R10-M06.** Sin mirar el material, explica cómo se relacionan «Sincronización multisensor», «Fusión radio-óptica» y «Evaluación de degradación sensorial», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R10-M07 · Control autónomo de vehículos

1. **Autonomía a bordo** — [`B74-C18`](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md), [`B97-C16`](../programa/clases/B97/B97-C16-autonomia-de-exploracion/CLASE.md)
2. **Planificación por objetivos** — [`B98-C01`](../programa/clases/B98/B98-C01-planificacion-por-objetivos-a-bordo/CLASE.md)
3. **Control predictivo** — [`B87-C21`](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md)
4. **Restricciones de seguridad** — [`B88-C16`](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md), [`B97-C17`](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md)
5. **Sistemas de decisión** — [`B98-C02`](../programa/clases/B98/B98-C02-sistemas-de-decision-autonomos-y-maquinas-de-estados-de-comportamiento/CLASE.md)
6. **Diagnóstico automático** — [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md), [`B96-C13`](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md)
7. **Gestión de incertidumbre** — [`B12-C16`](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md), [`B12-C17`](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md)
8. **Estados seguros** — [`B88-C11`](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md), [`B96-C08`](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md), [`B96-C15`](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md)
9. **Supervisión desde Tierra** — [`B96-C07`](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md), [`B96-C03`](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md), [`B97-C07`](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md)
10. **Verificación de control autónomo** — [`B87-C19`](../programa/clases/B87/B87-C19-verificacion-de-ley-de-control/CLASE.md), [`B16-C19`](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md), [`B88-C14`](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md)

✅ **Checkpoint R10-M07.** Sin mirar el material, explica cómo se relacionan «Autonomía a bordo», «Diagnóstico automático» y «Verificación de control autónomo», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R10-M08 · Encuentro y operaciones de proximidad

1. **Cinemática de movimiento relativo** — [`B76-C09`](../programa/clases/B76/B76-C09-dinamica-relativa-de-hill-clohessy-wiltshire/CLASE.md), [`B76-C17`](../programa/clases/B76/B76-C17-sistemas-de-referencia-relativos/CLASE.md)
2. **Guiado de encuentro** — [`B76-C10`](../programa/clases/B76/B76-C10-encuentro-orbital/CLASE.md), [`B76-C12`](../programa/clases/B76/B76-C12-guiado-relativo/CLASE.md)
3. **Sensores de proximidad** — [`B76-C13`](../programa/clases/B76/B76-C13-sensores-de-proximidad/CLASE.md)
4. **Control de distancia** — [`B76-C11`](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md), [`B76-C12`](../programa/clases/B76/B76-C12-guiado-relativo/CLASE.md)
5. **Conos de aproximación** — [`B76-C11`](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md)
6. **Planificación evasiva** — [`B76-C14`](../programa/clases/B76/B76-C14-evasion-de-colision/CLASE.md), [`B118-C07`](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md)
7. **Restricciones de contacto** — [`B76-C16`](../programa/clases/B76/B76-C16-acoplamiento-y-captura/CLASE.md), [`B76-C18`](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md)
8. **Acoplamiento simulado** — [`B76-C16`](../programa/clases/B76/B76-C16-acoplamiento-y-captura/CLASE.md), [`B76-C20`](../programa/clases/B76/B76-C20-simulacion-de-encuentro-seguro/CLASE.md)
9. **Fallas de navegación relativa** — [`B76-C12`](../programa/clases/B76/B76-C12-guiado-relativo/CLASE.md), [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md)
10. **Prueba de misión de rendezvous** — [`B76-C20`](../programa/clases/B76/B76-C20-simulacion-de-encuentro-seguro/CLASE.md), [`B90-C16`](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md)

✅ **Checkpoint R10-M08.** Sin mirar el material, explica cómo se relacionan «Cinemática de movimiento relativo», «Planificación evasiva» y «Prueba de misión de rendezvous», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Navegador autónomo para un encuentro orbital simulado.** Implementa un filtro de estimación que fusione sensores para guiar una nave a un blanco, con detección de fallos de un sensor.

Entregables:

- Modelo de sensores con ruidos realistas
- Filtro de estimación con su afinado
- Controlador de aproximación con límites de seguridad
- Pruebas de Monte Carlo con fallos introducidos

Criterios de evaluación:

- El filtro es consistente (errores dentro de su covarianza)
- El encuentro cumple la precisión en el 99 % de los casos
- Un sensor fallado se detecta y se aísla
- El código está probado y documentado

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes diseñar un estimador de estado y probar su consistencia.
- Puedes planear y simular una aproximación segura entre dos vehículos.
- Puedes explicar los modos de fallo de un sistema de navegación.

<!-- /recorrido -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **estimador o lazo de guiado verificado en simulación**:

- un modelo de sensores con sus errores;
- un filtro con su análisis de consistencia;
- una simulación con fallas inyectadas y su respuesta;
- un presupuesto de error del estado estimado;
- el código para repetirlo.

Los bloques de la ruta aportan ejercicios y laboratorios; guarda la primera versión y sus cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada, y para esta guía no se consultó una fuente externa específica (2026-11-05). Por eso no se citan normas, requisitos de acceso ni cifras: cuando se necesiten, deben consultarse en la fuente oficial vigente de la institución, agencia o empresa correspondiente.

## 📈 Progresión del rol

Rutas habituales: **ingeniero/a de navegación o de GNC → responsable de un subsistema de guiado → liderazgo técnico de navegación y autonomía**. Se abren la robótica y los sistemas autónomos. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Astrodinámica interplanetaria](astrodinamica-interplanetaria.md), [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md) y [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md).

## ⚠️ Mitos y errores comunes

- **«Más sensores es siempre mejor».** Mal fusionados, empeoran la estimación.
- **«El filtro de Kalman sirve para todo».** Supone linealidad y ruido gaussiano que no siempre se cumplen.
- **«La autonomía elimina a los operadores».** Redefine qué decide cada parte.
- **«Si el simulador funciona, el vuelo funcionará».** Depende de cuán fiel sea el simulador.
- **«La navegación es solo GPS».** Fuera de la Tierra casi nunca existe esa opción.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la matemática de tu diagnóstico.
2. Estudia **estadística** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)), **sistemas dinámicos y control** ([**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md)) y **estimación de órbitas** ([**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md)).
3. Profundiza en **navegación inercial y fusión** ([**B80** · Navegación inercial y fusión multisensorial](../programa/tronco-comun/B80-navegacion-inercial-y-fusion-multisensorial.md)) y **sensores y actitud** ([**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md)).
4. Avanza a **autonomía** ([**B98** · Autonomía y teleoperación espacial](../programa/tronco-comun/B98-autonomia-y-teleoperacion-espacial.md)) y **localización y mapeo** ([**B99** · Localización y mapeo robótico](../programa/tronco-comun/B99-localizacion-y-mapeo-robotico.md)).
5. Reúne tu **estimador verificado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrodinámica interplanetaria](astrodinamica-interplanetaria.md) · [Robótica espacial y sistemas autónomos](robotica-espacial-y-sistemas-autonomos.md) · [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R10-navegacion-guiado-y-autonomia-espacial/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
