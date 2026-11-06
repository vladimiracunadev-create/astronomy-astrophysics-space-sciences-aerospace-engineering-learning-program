# ⭐ Astrofísica estelar y galáctica

> Estudias cómo nacen, viven y mueren las estrellas y cómo se organizan en galaxias: conviertes luz y datos en propiedades físicas (temperatura, composición, masa, edad) y las contrastas con modelos.
>
> **Nivel de entrada:** física y matemática de nivel universitario más programación; es un rol de investigación · **Foco:** atmósferas e interiores estelares, evolución, espectroscopía, poblaciones y galaxias · **Entrega:** análisis reproducibles, modelos contrastados con datos con su incertidumbre e informes de investigación

## 🧭 Qué es y por qué importa

La astrofísica estelar y galáctica es la rama que explica **por qué las estrellas brillan como brillan** y **cómo se reparten en el espacio**. Nada de lo que sabemos de una estrella lejana se mide directamente: lo que llega es luz. De su espectro y de su brillo se infieren temperatura, composición, gravedad, velocidad y edad, y esas inferencias se comparan con modelos de su atmósfera, de su interior y de su evolución.

El rol se vive en tres miradas que conviene conocer:

- **Observación y datos.** Trabajas con catálogos, espectros y series de tiempo: los limpias, los cruzas, estimas errores y extraes propiedades. Los grandes sondeos (por ejemplo, Gaia) han convertido esta mirada en un trabajo de ciencia de datos con mucha física detrás.
- **Modelado.** Construyes o usas modelos de atmósferas estelares, de estructura interna y de evolución, y los ajustas a lo observado. Su pregunta es: *¿qué tiene que ser verdad dentro de la estrella para que veamos esto?*
- **Simulación.** Reproduces la formación y la dinámica de poblaciones y de galaxias con código, y comparas el resultado con el cielo. Su pregunta es: *¿este mecanismo basta para producir lo que observamos?*

La investigación independiente en este campo suele requerir formación de posgrado; este programa no la sustituye, pero te da la base y el método para llegar a ella.

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es cosmología.** Quien estudia el universo temprano, la materia oscura y los parámetros cosmológicos trabaja con otras escalas y otros datos ([Cosmología y astrofísica extrema](cosmologia-y-astrofisica-extrema.md)). Los dos roles se tocan en el estudio de las galaxias.
- **No es ingeniería de instrumentos.** Diseñar telescopios y detectores es otro oficio ([Ingeniería óptica y telescopios profesionales](ingenieria-optica-y-telescopios-profesionales.md)); tú los usas y debes entender sus límites, no construirlos.
- **No es ciencia de datos genérica.** El dato astronómico tiene su física (extinción, calibración, selección); un algoritmo potente aplicado sin esa física da respuestas precisas y equivocadas.
- **No es ciencia ficticia ni predicción.** Un modelo estelar no «adivina»: se somete a datos, se corrige y se publica con su incertidumbre.
- **No es un trabajo de observatorio.** Observar con un telescopio es una parte; gran parte del tiempo se dedica a datos ya archivados.

## 🗓️ Un día en el puesto

- **Lectura y contexto:** repasas lo último publicado sobre tu objeto o tu pregunta y lo que ya se sabe.
- **Preparación de datos:** descargas un catálogo o un conjunto de espectros, los cruzas con otro, descartas lo contaminado y registras cómo.
- **Ajuste y modelo:** comparas lo observado con un modelo, exploras parámetros y estimas incertidumbres. La mayoría de las corridas no salen bien la primera vez.
- **Código y reproducibilidad:** guardas el análisis de forma que otra persona lo pueda repetir.
- **Discusión y escritura:** presentas resultados a colegas, recibes críticas y redactas.

Dicho sin adornos: hay **más tiempo frente a un editor y a una gráfica que frente a un telescopio**, y mucha disciplina para no engañarte con un buen ajuste que esconde un sesgo de selección.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Física estelar:** equilibrio, transporte de energía, fusión y evolución ([**B24** · Física y evolución de estrellas](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md)).
- **Radiación y espectros:** formación de líneas, atmósferas, abundancias ([**B32** · Atmósferas estelares y espectroscopía estelar cuantitativa](../../programa/tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md), [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md)).
- **Interiores y oscilaciones:** modelos de estructura y asterosismología ([**B37** · Interiores estelares y asterosismología](../../programa/tronco-comun/B37-interiores-estelares-y-asterosismologia.md)).
- **Galaxias y poblaciones:** estructura, medio interestelar, historia de formación estelar y simulación ([**B25** · Galaxias y medio interestelar](../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md), [**B38** · Poblaciones estelares y simulación de galaxias](../../programa/tronco-comun/B38-poblaciones-estelares-y-simulacion-de-galaxias.md)).
- **Estadística e incertidumbre:** inferencia, ajuste y propagación de errores ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md), [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)).
- **Computación científica:** análisis reproducible y manejo de datos astronómicos ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).

### Herramientas del oficio

```text
Lenguaje y análisis:   Python científico, incluido Astropy
Datos:                catálogos y archivos públicos de grandes sondeos
Modelos:              códigos de estructura y evolución estelar, de atmósferas y de transferencia radiativa
Cómputo:              clústeres de alto rendimiento para simulaciones
Reproducibilidad:     control de versiones y entornos declarados
```

Ninguna herramienta reemplaza la física. Un ajuste que converge no demuestra que el modelo sea correcto: lo que se paga es tu criterio para detectar sesgos y comprobar supuestos.

### Habilidades no técnicas

- **Escritura científica clara:** un resultado que no se explica no existe para los demás.
- **Escepticismo metódico:** buscar el motivo por el que tu resultado podría estar mal antes de que lo haga un revisor.
- **Trabajo en colaboración:** la mayoría de los proyectos reúnen a varias personas y sondeos.
- **Constancia:** los resultados llegan lento y por iteraciones.

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B03** · Matemática elemental para ciencias espaciales](../programa/tronco-comun/B03-matematica-elemental-para-ciencias-espaciales.md) — A01 · 20 clases
2. 📚 [**B04** · Álgebra, trigonometría y geometría espacial](../programa/tronco-comun/B04-algebra-trigonometria-y-geometria-espacial.md) — A01 · 20 clases
3. 📚 [**B05** · Física fundamental para el espacio](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md) — A01 · 20 clases
4. 📚 [**B06** · Química y materia del universo](../programa/tronco-comun/B06-quimica-y-materia-del-universo.md) — A01 · 20 clases
5. 📚 [**B07** · Informática científica desde cero](../programa/tronco-comun/B07-informatica-cientifica-desde-cero.md) — A01 · 20 clases
6. 📚 [**B08** · Observación del cielo y astronomía práctica](../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md) — A01 · 20 clases
7. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
8. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
9. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — A02 · 23 clases
10. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases
11. 📚 [**B26** · Relatividad y cosmología](../programa/tronco-comun/B26-relatividad-y-cosmologia.md) — A03 · 23 clases
12. 📚 [**B28** · Astronomía multimensajero](../programa/tronco-comun/B28-astronomia-multimensajero.md) — A03 · 22 clases

### 🎯 El núcleo del rol

**A01 · Alfabetización científica, astronómica y tecnológica**

1. 📚 [**B01** · El universo y el pensamiento científico](../programa/tronco-comun/B01-el-universo-y-el-pensamiento-cientifico.md) — usa 2 de 20 clases: `B01-` C06–C07

**A02 · Matemática, física computacional y métodos científicos**

2. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — usa 1 de 20 clases: `B09-` C20
3. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 4 de 26 clases: `B12-` C08–C09, C16, C19
4. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 4 de 31 clases: `B14-` C05, C08–C09, C19
5. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — usa 2 de 24 clases: `B15-` C05–C06
6. 📚 [**B20** · Metodología de la investigación científica](../programa/tronco-comun/B20-metodologia-de-la-investigacion-cientifica.md) — usa 4 de 4 clases: `B20-` C01–C04

**A03 · Astrofísica y ciencias fundamentales del universo**

7. 📚 [**B24** · Física y evolución de estrellas](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) — usa 21 de 22 clases: `B24-` C01–C12, C14–C22
8. 📚 [**B25** · Galaxias y medio interestelar](../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md) — usa 9 de 20 clases: `B25-` C01–C02, C06–C08, C12, C15, C17, C19
9. 📚 [**B27** · Objetos compactos y altas energías](../programa/tronco-comun/B27-objetos-compactos-y-altas-energias.md) — usa 3 de 22 clases: `B27-` C02–C03, C15
10. 📚 [**B29** · Astronomía temporal y exoplanetas](../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md) — usa 2 de 20 clases: `B29-` C03, C19
11. 📚 [**B32** · Atmósferas estelares y espectroscopía estelar cuantitativa](../programa/tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md) — usa 12 de 12 clases: `B32-` C01–C12
12. 📚 [**B37** · Interiores estelares y asterosismología](../programa/tronco-comun/B37-interiores-estelares-y-asterosismologia.md) — usa 14 de 14 clases: `B37-` C01–C14
13. 📚 [**B38** · Poblaciones estelares y simulación de galaxias](../programa/tronco-comun/B38-poblaciones-estelares-y-simulacion-de-galaxias.md) — usa 9 de 9 clases: `B38-` C01–C09

**A04 · Óptica, telescopios y observatorios científicos**

14. 📚 [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md) — usa 9 de 24 clases: `B45-` C02, C06–C09, C12, C14, C18–C19

**A06 · Mecánica orbital, navegación y vuelo espacial**

15. 📚 [**B73** · Mecánica celeste, resonancias y caos](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md) — usa 2 de 22 clases: `B73-` C08–C09

**A11 · Economía, industria y gestión de proyectos espaciales**

16. 📚 [**B124** · Industria, economía, ética y proyectos espaciales](../programa/tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) — usa 1 de 24 clases: `B124-` C14

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **análisis reproducible de un problema estelar o galáctico**:

- una pregunta acotada y su justificación;
- datos abiertos con procedencia, y las decisiones de selección documentadas;
- un modelo o un ajuste con incertidumbres propagadas;
- una comparación honesta con la literatura, indicando qué no se pudo concluir;
- el código y el entorno para repetirlo.

Los bloques de su ruta traen ejercicios y laboratorios para cada pieza: guarda la primera versión, la retroalimentación y los cambios, porque el historial de decisiones es parte de la evidencia.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada: la señal de competencia es el trabajo publicado y revisado. Las referencias de trabajo que se consultaron (2026-11-05) son:

- 📘 **Gaia Data Release 3: Summary of the content and survey properties** (Gaia Collaboration, arXiv:2208.00211; DOI 10.1051/0004-6361/202243940): describe el contenido del tercer catálogo de Gaia, entre otros velocidades radiales para más de 33 millones de estrellas y soluciones orbitales para unas 800.000 binarias. Solo se leyó el resumen.
- 📗 **Astropy** — página del proyecto (https://www.astropy.org/about.html): «un esfuerzo comunitario para desarrollar un paquete central para astronomía», con herramientas de uso común.

Los requisitos para publicar, financiar o acceder a tiempo de observación dependen de cada institución y no están verificados aquí.

## 📈 Progresión del rol

Ruta habitual: **formación de grado → posgrado → investigación posdoctoral → posición académica o en una institución de investigación**. Desde el análisis de datos se abren también las carreras de ciencia de datos, de instrumentación y de comunicación científica. No se publican aquí cifras salariales: varían demasiado y no se pudieron verificar.

Roles vecinos con los que se comparte formación: [Cosmología y astrofísica extrema](cosmologia-y-astrofisica-extrema.md), [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md) y [Heliofísica y climatología espacial](heliofisica-y-climatologia-espacial.md).

## ⚠️ Mitos y errores comunes

- **«La astrofísica es solo matemática».** La matemática es el lenguaje, pero lo decisivo es contrastar con datos y entender sus sesgos.
- **«Más datos siempre ayudan».** Más datos con un sesgo de selección sin corregir dan una conclusión más segura de lo que debería.
- **«Un buen ajuste prueba el modelo».** Prueba que el modelo puede reproducir los datos, no que sea el único que puede hacerlo.
- **«Todo se hace en el telescopio».** La mayor parte del trabajo actual usa archivos y cómputo.
- **«El código no importa, importa el resultado».** Un resultado que no se puede reproducir no se puede revisar.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la matemática y la programación que tu diagnóstico pida.
2. Recorre la **física estelar** ([**B24** · Física y evolución de estrellas](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md)) y la **radiación y los espectros** ([**B32** · Atmósferas estelares y espectroscopía estelar cuantitativa](../../programa/tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md)).
3. Aprende a **tratar datos con incertidumbre** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md), [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)) y a hacerlo de forma reproducible ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).
4. Elige una mirada (observación, modelado o simulación) y profundiza: [**B37** · Interiores estelares y asterosismología](../../programa/tronco-comun/B37-interiores-estelares-y-asterosismologia.md) o [**B38** · Poblaciones estelares y simulación de galaxias](../../programa/tronco-comun/B38-poblaciones-estelares-y-simulacion-de-galaxias.md).
5. Reúne tu **análisis reproducible** y guarda su historia.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Cosmología y astrofísica extrema](cosmologia-y-astrofisica-extrema.md) · [Heliofísica y climatología espacial](heliofisica-y-climatologia-espacial.md) · [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R01-astrofisica-estelar-y-galactica/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
