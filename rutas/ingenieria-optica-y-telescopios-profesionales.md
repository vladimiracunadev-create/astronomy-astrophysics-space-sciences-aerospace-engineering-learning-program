# 🔭 Ingeniería óptica y telescopios profesionales

> Diseñas, construyes y pruebas telescopios e instrumentos ópticos: de la óptica y las tolerancias a la mecánica de precisión, la fotometría instrumental y la automatización del observatorio.
>
> **Nivel de entrada:** física y matemática, buen manejo de óptica y de mecánica, y programación; es un rol de ingeniería · **Foco:** diseño óptico, aberraciones y tolerancias, fabricación y pruebas, monturas, óptica adaptativa y operación · **Entrega:** un diseño óptico y mecánico con presupuesto de errores, planes de prueba y la evidencia de que cumple su desempeño

## 🧭 Qué es y por qué importa

Un telescopio es un instrumento de medida: su desempeño se define por cuánta luz recoge, con qué nitidez y con qué fidelidad. La ingeniería óptica lleva ese objetivo a **diseño, fabricación, montaje y prueba**. Se trabaja con presupuestos: de aberraciones, de tolerancias, de estabilidad mecánica y de calibración, y cada decisión se justifica con un número que se puede comprobar.

El rol incluye varias miradas:

- **Diseño óptico.** Eliges formas y disposición de espejos y lentes, evalúas aberraciones y fijas tolerancias con herramientas computacionales. Su pregunta es: *¿qué diseño cumple el desempeño con la menor sensibilidad a errores?*
- **Fabricación y pruebas.** Pulido, medición de superficies y colimación. Su pregunta es: *¿cómo demuestro que la superficie y el alineamiento están dentro de tolerancia?*
- **Mecánica y control.** Monturas, estructura, seguimiento y, en telescopios grandes, óptica adaptativa. Su pregunta es: *¿cómo mantengo la óptica alineada y estable en condiciones reales?*
- **Instrumento y operación.** Detectores, calibración fotométrica y automatización del observatorio. Su pregunta es: *¿el dato que sale es el que se necesita y se puede confiar en él?*

Los grandes proyectos reúnen a muchas de estas especialidades: por ejemplo, la página del Extremely Large Telescope de ESO menciona sistemas de espejos, óptica adaptativa, una estación prefocal y varios instrumentos de primera luz.

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es el astrónomo observador.** Quien usa el telescopio define qué observar; tú haces que el instrumento pueda medirlo ([Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md)).
- **No es radioastronomía.** Comparte conceptos (aperturas, interferometría) pero trabaja con antenas y receptores distintos ([Radioastronomía e interferometría](radioastronomia-e-interferometria.md)).
- **No es ingeniería de satélites.** Un telescopio espacial comparte óptica, pero su plataforma es otro problema ([Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md)).
- **No es «comprar un telescopio».** Un instrumento científico se diseña con un presupuesto de errores, no se elige de un catálogo.
- **No es solo software de diseño.** El programa calcula; la fabricación, el alineamiento y la prueba lo hacen real.

## 🗓️ Un día en el puesto

- **Diseño y análisis:** corres un trazado de rayos, revisas aberraciones y compruebas cómo una tolerancia afecta al desempeño.
- **Taller y pruebas:** mides una superficie, registras resultados y comparas con la especificación.
- **Mecánica y alineamiento:** ajustas una montura, colimas y revisas la estabilidad.
- **Instrumento y calibración:** verificas la respuesta de un detector y su calibración.
- **Documentación y revisión de diseño:** escribes y defiendes tus decisiones ante un equipo.

Dicho sin adornos: casi todo trabajo consiste en **convertir una tolerancia en un procedimiento de medida** y registrar el resultado.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Óptica geométrica y diseño de telescopios:** formación de imagen, aberraciones, configuraciones ([**B41** · Óptica geométrica y diseño de telescopios](../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md), [**B50** · Diseño óptico computacional y tolerancias](../programa/tronco-comun/B50-diseno-optico-computacional-y-tolerancias.md)).
- **Óptica física y adaptativa:** difracción, frente de onda, corrección en tiempo real ([**B42** · Óptica física y óptica adaptativa](../programa/tronco-comun/B42-optica-fisica-y-optica-adaptativa.md)).
- **Construcción y mecánica de telescopios:** monturas, pulido, colimación, pruebas ([**B43** · Construcción y mecánica de telescopios](../programa/tronco-comun/B43-construccion-y-mecanica-de-telescopios.md)).
- **Detectores y adquisición:** sensores, calibración, ruido ([**B44** · Detectores y adquisición astronómica](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md)).
- **Espectroscopía y fotometría:** instrumentos de medida y su calibración ([**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md)).
- **Operación de observatorios:** automatización y calidad de datos ([**B48** · Operaciones de observatorios científicos](../programa/tronco-comun/B48-operaciones-de-observatorios-cientificos.md)).
- **Ingeniería de sistemas y ensayos:** presupuestos y pruebas de integración ([**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md), [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md)).

### Herramientas del oficio

```text
Diseño óptico:        programas de trazado de rayos y análisis de tolerancias
Mecánica:             diseño asistido y análisis estructural
Medición:             interferometría de superficies y pruebas de frente de onda
Control y datos:      Python para análisis y automatización
Documentación:        especificaciones, planes de prueba y registro de resultados
```

El software de diseño produce resultados precisos para el modelo que le das. Lo que se paga es tu criterio para saber si ese modelo representa el instrumento real.

### Habilidades no técnicas

- **Pensamiento en presupuestos:** repartir el error disponible entre piezas.
- **Meticulosidad:** una colimación a medias es peor que ninguna.
- **Comunicación con astrónomos y fabricantes:** traducir una necesidad científica en una tolerancia y viceversa.
- **Trabajo en equipo multidisciplinar.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B04** · Álgebra, trigonometría y geometría espacial](../programa/tronco-comun/B04-algebra-trigonometria-y-geometria-espacial.md) — A01 · 20 clases
2. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
3. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
4. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
5. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — A02 · 31 clases
6. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
7. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases
8. 📚 [**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md) — A04 · 20 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 1 de 26 clases: `B12-` C16
2. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 3 de 23 clases: `B13-` C17, C19–C20

**A03 · Astrofísica y ciencias fundamentales del universo**

3. 📚 [**B29** · Astronomía temporal y exoplanetas](../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md) — usa 3 de 20 clases: `B29-` C02, C14, C19

**A04 · Óptica, telescopios y observatorios científicos**

4. 📚 [**B41** · Óptica geométrica y diseño de telescopios](../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md) — usa 11 de 20 clases: `B41-` C04–C06, C08–C09, C13–C17, C20
5. 📚 [**B42** · Óptica física y óptica adaptativa](../programa/tronco-comun/B42-optica-fisica-y-optica-adaptativa.md) — usa 12 de 24 clases: `B42-` C11–C18, C21–C24
6. 📚 [**B43** · Construcción y mecánica de telescopios](../programa/tronco-comun/B43-construccion-y-mecanica-de-telescopios.md) — usa 24 de 26 clases: `B43-` C01–C07, C09–C10, C12–C26
7. 📚 [**B44** · Detectores y adquisición astronómica](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md) — usa 8 de 20 clases: `B44-` C04–C05, C12–C14, C17–C18, C20
8. 📚 [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md) — usa 9 de 24 clases: `B45-` C02–C03, C09, C17, C19, C21–C24
9. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — usa 1 de 25 clases: `B47-` C11
10. 📚 [**B48** · Operaciones de observatorios científicos](../programa/tronco-comun/B48-operaciones-de-observatorios-cientificos.md) — usa 12 de 23 clases: `B48-` C04, C07–C10, C13–C15, C20–C23
11. 📚 [**B50** · Diseño óptico computacional y tolerancias](../programa/tronco-comun/B50-diseno-optico-computacional-y-tolerancias.md) — usa 15 de 15 clases: `B50-` C01–C15

**A07 · Ingeniería y construcción de sistemas espaciales**

12. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 6 de 24 clases: `B83-` C04, C07, C13–C14, C16–C17
13. 📚 [**B84** · Estructuras, materiales y fabricación espacial](../programa/tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) — usa 4 de 38 clases: `B84-` C11, C16, C18–C19
14. 📚 [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md) — usa 1 de 44 clases: `B88-` C17
15. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 2 de 24 clases: `B90-` C08, C16

**A11 · Economía, industria y gestión de proyectos espaciales**

16. 📚 [**B124** · Industria, economía, ética y proyectos espaciales](../programa/tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) — usa 1 de 24 clases: `B124-` C05

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes aplicar la ley de Snell y trazar rayos por una lente delgada?
- ¿Sabes qué es una aberración esférica y cómo se mide?
- ¿Manejas álgebra lineal básica (matrices) para describir sistemas ópticos?
- ¿Sabes leer un plano mecánico con tolerancias?

#### R03-M01 · Diseño óptico computacional

1. **Trazado paraxial** — [`B41-C05`](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md), [`B41-C06`](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md), [`B41-C08`](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md)
2. **Trazado no paraxial** — [`B50-C01`](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md)
3. **Optimización de superficies** — [`B50-C02`](../programa/clases/B50/B50-C02-optimizacion-de-superficies-funcion-de-merito-y-restricciones/CLASE.md)
4. **Sistemas reflectivos** — [`B41-C04`](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md), [`B41-C16`](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md), [`B41-C17`](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md)
5. **Sistemas refractivos** — [`B41-C05`](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md), [`B41-C15`](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md)
6. **Sistemas catadióptricos** — [`B50-C03`](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md)
7. **Diseño de pupilas** — [`B41-C09`](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md)
8. **Telecentricidad y campo** — [`B50-C04`](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md)
9. **Análisis de rayos dispersos** — [`B50-C05`](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md)
10. **Software de diseño óptico** — [`B50-C06`](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md)

✅ **Checkpoint R03-M01.** Sin mirar el material, explica cómo se relacionan «Trazado paraxial», «Sistemas catadióptricos» y «Software de diseño óptico», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R03-M02 · Aberraciones y tolerancias ópticas

1. **Aberración cromática** — [`B41-C14`](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md), [`B41-C15`](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md)
2. **Coma y astigmatismo** — [`B41-C13`](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md), [`B41-C14`](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md)
3. **Curvatura de campo** — [`B50-C07`](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md)
4. **Distorsión geométrica** — [`B50-C08`](../programa/clases/B50/B50-C08-distorsion-geometrica-y-su-calibracion/CLASE.md)
5. **Balance de tolerancias** — [`B50-C09`](../programa/clases/B50/B50-C09-asignacion-y-balance-de-tolerancias-opticas/CLASE.md)
6. **Errores de centrado** — [`B50-C10`](../programa/clases/B50/B50-C10-errores-de-centrado-y-su-efecto-en-el-desempeno/CLASE.md)
7. **Errores de inclinación** — [`B50-C11`](../programa/clases/B50/B50-C11-errores-de-inclinacion-de-elementos-y-superficies/CLASE.md)
8. **Sensibilidad a temperatura** — [`B50-C12`](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md)
9. **Análisis de Monte Carlo óptico** — [`B50-C13`](../programa/clases/B50/B50-C13-analisis-monte-carlo-de-tolerancias-opticas/CLASE.md)
10. **Criterios de aceptación** — [`B50-C14`](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md)

✅ **Checkpoint R03-M02.** Sin mirar el material, explica cómo se relacionan «Aberración cromática», «Errores de centrado» y «Criterios de aceptación», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R03-M03 · Fabricación y pruebas ópticas

1. **Selección de vidrio** — [`B43-C21`](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md)
2. **Sustratos de espejos** — [`B43-C03`](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md)
3. **Esmerilado controlado** — [`B43-C04`](../programa/clases/B43/B43-C04-fabricacion-y-desbaste-de-espejos/CLASE.md)
4. **Pulido de precisión** — [`B43-C05`](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md)
5. **Interferometría de superficie** — [`B43-C22`](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md)
6. **Medición de rugosidad** — [`B43-C23`](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md)
7. **Recubrimientos reflectantes** — [`B43-C07`](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md)
8. **Recubrimientos antirreflectantes** — [`B43-C24`](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md)
9. **Metrología en taller** — [`B43-C06`](../programa/clases/B43/B43-C06-pruebas-de-ronchi-y-foucault/CLASE.md), [`B13-C20`](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md)
10. **Inspección de piezas** — [`B84-C16`](../programa/clases/B84/B84-C16-tolerancias-de-fabricacion/CLASE.md), [`B84-C18`](../programa/clases/B84/B84-C18-control-dimensional/CLASE.md), [`B84-C19`](../programa/clases/B84/B84-C19-inspeccion-no-destructiva/CLASE.md)

✅ **Checkpoint R03-M03.** Sin mirar el material, explica cómo se relacionan «Selección de vidrio», «Medición de rugosidad» y «Inspección de piezas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R03-M04 · Monturas y mecánica de precisión

1. **Diseño de montura altacimutal** — [`B43-C13`](../programa/clases/B43/B43-C13-montura-altacimutal/CLASE.md)
2. **Diseño de montura ecuatorial** — [`B43-C12`](../programa/clases/B43/B43-C12-montura-ecuatorial/CLASE.md), [`B43-C17`](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md)
3. **Rodamientos de precisión** — [`B43-C25`](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md)
4. **Transmisiones y holguras** — [`B43-C14`](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md)
5. **Motores y servos** — [`B43-C15`](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md)
6. **Encoders absolutos** — [`B43-C16`](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md)
7. **Modelo de flexiones** — [`B43-C26`](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md)
8. **Alineación y apuntado** — [`B43-C17`](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md), [`B43-C18`](../programa/clases/B43/B43-C18-colimacion-instrumental/CLASE.md)
9. **Aislamiento de vibraciones** — [`B84-C11`](../programa/clases/B84/B84-C11-vibraciones-y-resonancias/CLASE.md), [`B47-C11`](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md)
10. **Mantenimiento preventivo** — [`B43-C19`](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md), [`B48-C14`](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md)

✅ **Checkpoint R03-M04.** Sin mirar el material, explica cómo se relacionan «Diseño de montura altacimutal», «Encoders absolutos» y «Mantenimiento preventivo», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R03-M05 · Óptica adaptativa profesional

1. **Sensores de frente de onda** — [`B42-C13`](../programa/clases/B42/B42-C13-medicion-de-frente-de-onda/CLASE.md), [`B42-C14`](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md)
2. **Estrellas guía naturales** — [`B42-C21`](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md)
3. **Estrellas guía láser** — [`B42-C17`](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md)
4. **Espejos deformables** — [`B42-C15`](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md)
5. **Control en lazo cerrado** — [`B42-C16`](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md)
6. **Turbulencia atmosférica** — [`B42-C11`](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md), [`B42-C12`](../programa/clases/B42/B42-C12-parametro-de-fried/CLASE.md)
7. **Reconstrucción de fase** — [`B42-C22`](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md)
8. **Arquitectura multiconjugada** — [`B42-C18`](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md)
9. **Calibración del sistema** — [`B42-C23`](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md)
10. **Métricas de corrección** — [`B42-C24`](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md)

✅ **Checkpoint R03-M05.** Sin mirar el material, explica cómo se relacionan «Sensores de frente de onda», «Turbulencia atmosférica» y «Métricas de corrección», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R03-M06 · Fotometría instrumental avanzada

1. **Calibración fotométrica** — [`B45-C09`](../programa/clases/B45/B45-C09-calibracion-de-respuesta-instrumental/CLASE.md), [`B13-C17`](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md)
2. **Filtros astronómicos** — [`B45-C02`](../programa/clases/B45/B45-C02-magnitudes-y-sistemas-de-filtros/CLASE.md), [`B45-C03`](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md)
3. **Estándares fotométricos** — [`B45-C21`](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md)
4. **Corrección de extinción** — [`B45-C22`](../programa/clases/B45/B45-C22-extincion-atmosferica-masa-de-aire-y-coeficientes-de-color/CLASE.md)
5. **Fotometría de apertura** — [`B45-C23`](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md)
6. **Fotometría por PSF** — [`B45-C24`](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md)
7. **Selección de comparación** — [`B45-C17`](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md)
8. **Propagación de incertidumbre** — [`B12-C16`](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md), [`B45-C19`](../programa/clases/B45/B45-C19-reduccion-e-incertidumbre-instrumental/CLASE.md)
9. **Detección de variabilidad** — [`B29-C14`](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md), [`B29-C19`](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md)
10. **Construcción de curvas de luz** — [`B29-C02`](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md)

✅ **Checkpoint R03-M06.** Sin mirar el material, explica cómo se relacionan «Calibración fotométrica», «Fotometría por PSF» y «Construcción de curvas de luz», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R03-M07 · Automatización de observatorios

1. **Planificador astronómico** — [`B48-C04`](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md), [`B48-C20`](../programa/clases/B48/B48-C20-diseno-de-una-campana-observacional-profesional/CLASE.md)
2. **Protocolos de control instrumental** — [`B48-C21`](../programa/clases/B48/B48-C21-protocolos-estandar-de-control-instrumental-ascom-e-indi/CLASE.md)
3. **Control de cúpula** — [`B48-C08`](../programa/clases/B48/B48-C08-automatizacion-de-cupulas/CLASE.md)
4. **Control de enfocador** — [`B48-C22`](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md)
5. **Adquisición automatizada** — [`B48-C09`](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md), [`B44-C18`](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md)
6. **Secuencias de calibración** — [`B48-C13`](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md), [`B44-C12`](../programa/clases/B44/B44-C12-calibracion-con-bias/CLASE.md), [`B44-C13`](../programa/clases/B44/B44-C13-calibracion-con-dark/CLASE.md), [`B44-C14`](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md)
7. **Observatorio remoto** — [`B48-C07`](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md), [`B48-C09`](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md), [`B48-C10`](../programa/clases/B48/B48-C10-redes-de-instrumentos/CLASE.md)
8. **Manejo de fallas** — [`B48-C15`](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md)
9. **Observabilidad del software** — [`B48-C23`](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md)
10. **Seguridad operacional** — [`B48-C07`](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md), [`B88-C17`](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md)

✅ **Checkpoint R03-M07.** Sin mirar el material, explica cómo se relacionan «Planificador astronómico», «Secuencias de calibración» y «Seguridad operacional», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R03-M08 · Proyecto completo de instrumentación óptica

1. **Definición de requisitos ópticos** — [`B43-C01`](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md), [`B83-C04`](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md)
2. **Selección de arquitectura** — [`B43-C02`](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md), [`B83-C07`](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md)
3. **Presupuesto de errores** — [`B50-C15`](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md)
4. **Modelo óptico detallado** — [`B41-C08`](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md), [`B41-C20`](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md)
5. **Diseño mecánico de soporte** — [`B43-C09`](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md), [`B43-C10`](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md), [`B43-C20`](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md)
6. **Diseño de sensado** — [`B44-C04`](../programa/clases/B44/B44-C04-eficiencia-cuantica-espectral/CLASE.md), [`B44-C05`](../programa/clases/B44/B44-C05-pozo-lleno-y-rango-dinamico/CLASE.md), [`B44-C17`](../programa/clases/B44/B44-C17-escala-de-imagen-y-muestreo/CLASE.md)
7. **Plan de calibración** — [`B44-C20`](../programa/clases/B44/B44-C20-pipeline-inicial-de-calibracion-de-imagenes/CLASE.md), [`B13-C19`](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md), [`B13-C20`](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md)
8. **Plan de pruebas** — [`B83-C17`](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md), [`B90-C08`](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md), [`B90-C16`](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md)
9. **Evaluación de costo y riesgo** — [`B83-C16`](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md), [`B124-C05`](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md)
10. **Revisión final de diseño** — [`B83-C13`](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md), [`B83-C14`](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md)

✅ **Checkpoint R03-M08.** Sin mirar el material, explica cómo se relacionan «Definición de requisitos ópticos», «Diseño de sensado» y «Revisión final de diseño», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Diseño y tolerancia de un telescopio de 40 cm.** Diseña un telescopio reflector con su cámara, evalúa su calidad óptica y define el presupuesto de tolerancias de fabricación y alineación.

Entregables:

- Diseño óptico con diagramas de puntos y curvas MTF
- Presupuesto de tolerancias por elemento
- Plan de pruebas de fabricación y de alineación
- Especificación de la montura y del control de apuntado

Criterios de evaluación:

- El desempeño se verifica con trazado de rayos reproducible
- Las tolerancias cumplen el requisito con margen declarado
- El plan de pruebas es ejecutable con instrumentos reales
- Las suposiciones térmicas y mecánicas están explícitas

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes diseñar un sistema óptico y demostrar con simulación que cumple su requisito.
- Puedes asignar tolerancias y explicar su costo y su riesgo.
- Puedes planear la prueba y la alineación de un telescopio real.

<!-- /recorrido -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **expediente de diseño de un instrumento óptico**:

- requisitos de desempeño y su justificación científica;
- diseño óptico con análisis de aberraciones y de tolerancias;
- diseño mecánico preliminar y plan de alineamiento;
- plan de pruebas con criterios de aceptación y de calibración;
- registro de resultados, desviaciones y decisiones.

Los bloques de la ruta traen ejercicios y laboratorios para cada pieza; guarda la primera versión y sus cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada. Referencia de trabajo consultada (2026-11-05):

- 📘 **Extremely Large Telescope** — página de ESO (https://elt.eso.org/): presenta al telescopio como «World's Biggest Eye on the Sky» (un telescopio terrestre gigante) y sus sistemas: espejos, óptica adaptativa, estación prefocal e instrumentos (HARMONI, MICADO, MORFEO, METIS, ANDES y MOSAIC). Es un ejemplo de la escala del oficio.

Las normas de óptica, de fabricación y de ensayo dependen del proyecto y de la versión vigente, y no están verificadas aquí.

## 📈 Progresión del rol

Rutas habituales: **ingeniero/a óptico o mecánico de instrumento → líder de subsistema → ingeniero/a de sistemas de un instrumento o jefe de proyecto**. Se abren también la instrumentación espacial y la metrología. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Radioastronomía e interferometría](radioastronomia-e-interferometria.md), [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) y [Observación terrestre y geointeligencia científica](observacion-terrestre-y-geointeligencia-cientifica.md).

## ⚠️ Mitos y errores comunes

- **«El diseño perfecto en el programa funciona en la realidad».** Las tolerancias de fabricación y de alineamiento lo degradan; por eso se calculan.
- **«Más apertura es siempre mejor».** También exige más estructura, más estabilidad y más presupuesto de errores.
- **«La colimación es un detalle».** Es lo que decide la nitidez final.
- **«La automatización sustituye al criterio».** Automatiza lo repetible; el diagnóstico sigue siendo humano.
- **«Un buen instrumento no necesita calibración».** Sin calibración no hay medida.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la matemática y la física de tu diagnóstico.
2. Estudia **óptica geométrica y diseño de telescopios** ([**B41** · Óptica geométrica y diseño de telescopios](../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md)) y **óptica física y adaptativa** ([**B42** · Óptica física y óptica adaptativa](../programa/tronco-comun/B42-optica-fisica-y-optica-adaptativa.md)).
3. Aprende **construcción y mecánica de telescopios** ([**B43** · Construcción y mecánica de telescopios](../programa/tronco-comun/B43-construccion-y-mecanica-de-telescopios.md)) y **detectores** ([**B44** · Detectores y adquisición astronómica](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md)).
4. Profundiza en **diseño óptico computacional y tolerancias** ([**B50** · Diseño óptico computacional y tolerancias](../programa/tronco-comun/B50-diseno-optico-computacional-y-tolerancias.md)).
5. Reúne tu **expediente de diseño** y guarda su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Radioastronomía e interferometría](radioastronomia-e-interferometria.md) · [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) · [Observación terrestre y geointeligencia científica](observacion-terrestre-y-geointeligencia-cientifica.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R03-ingenieria-optica-y-telescopios-profesionales/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
