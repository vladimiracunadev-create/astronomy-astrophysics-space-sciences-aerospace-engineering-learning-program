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

- **Óptica geométrica y diseño de telescopios:** formación de imagen, aberraciones, configuraciones ([**B41** · Óptica geométrica y diseño de telescopios](../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md), [**B50** · Diseño óptico computacional y tolerancias](../PROGRAMA_ACADEMICO_COMPLETO.md#b50--diseño-óptico-computacional-y-tolerancias)).
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
11. 📚 [**B50** · Diseño óptico computacional y tolerancias](../PROGRAMA_ACADEMICO_COMPLETO.md#b50--diseño-óptico-computacional-y-tolerancias) — usa 15 de 15 clases: `B50-` C01–C15

**A07 · Ingeniería y construcción de sistemas espaciales**

12. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 6 de 24 clases: `B83-` C04, C07, C13–C14, C16–C17
13. 📚 [**B84** · Estructuras, materiales y fabricación espacial](../programa/tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) — usa 4 de 38 clases: `B84-` C11, C16, C18–C19
14. 📚 [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md) — usa 1 de 44 clases: `B88-` C17
15. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 2 de 24 clases: `B90-` C08, C16

**A11 · Economía, industria y gestión de proyectos espaciales**

16. 📚 [**B124** · Industria, economía, ética y proyectos espaciales](../programa/tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) — usa 1 de 24 clases: `B124-` C05

<!-- /ruta -->

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
4. Profundiza en **diseño óptico computacional y tolerancias** ([**B50** · Diseño óptico computacional y tolerancias](../PROGRAMA_ACADEMICO_COMPLETO.md#b50--diseño-óptico-computacional-y-tolerancias)).
5. Reúne tu **expediente de diseño** y guarda su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Radioastronomía e interferometría](radioastronomia-e-interferometria.md) · [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) · [Observación terrestre y geointeligencia científica](observacion-terrestre-y-geointeligencia-cientifica.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R03-ingenieria-optica-y-telescopios-profesionales/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
