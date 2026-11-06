# 🌀 Cosmología y astrofísica extrema

> Estudias el universo a gran escala y sus fenómenos más extremos: relatividad, universo temprano, radiación cósmica de fondo, objetos compactos, mensajeros múltiples y los parámetros que describen el cosmos.
>
> **Nivel de entrada:** física y matemática avanzadas; es un rol de investigación que se apoya en cómputo y estadística · **Foco:** relatividad, cosmología, estructuras cósmicas, altas energías y astronomía multimensajero · **Entrega:** modelos y análisis de datos con inferencia estadística, comparados con observaciones y con su incertidumbre

## 🧭 Qué es y por qué importa

La cosmología y la astrofísica extrema se ocupan de lo más grande y lo más violento: la historia y la forma del universo, la formación de sus estructuras, los agujeros negros, las estrellas de neutrones y las ondas que producen. Aquí las preguntas dependen de **modelos** (la relatividad general, el modelo cosmológico estándar) y de **inferencia estadística**: casi ningún parámetro cosmológico se mide directamente, se infiere comparando modelos con datos.

El rol se reparte en tres miradas:

- **Teoría y modelado.** Resuelves o analizas las ecuaciones que describen la expansión, el crecimiento de estructuras y los objetos compactos. Su pregunta es: *¿qué predice el modelo y en qué se diferencia de sus alternativas?*
- **Datos e inferencia.** Estimas parámetros con datos de la radiación de fondo, de galaxias o de ondas gravitacionales y cuantificas su incertidumbre. Su pregunta es: *¿qué valores permiten los datos, y con qué confianza?*
- **Multimensajero.** Combinas luz, partículas y ondas gravitacionales de un mismo evento. Su pregunta es: *¿qué cuenta cada mensajero que los demás no pueden contar?*

Un ejemplo de por qué la inferencia importa: la constante de Hubble medida con la radiación de fondo y con distancias locales da valores distintos con incertidumbres declaradas (la «tensión de Hubble», que se explica en la primera clase del programa). Entender esa discrepancia es entender cómo se construye una cifra cosmológica.

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es astrofísica estelar y galáctica.** Aquella estudia las estrellas y las galaxias una por una ([Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md)); esta usa poblaciones enteras y el universo como sistema.
- **No es divulgación.** Se apoya en la comunicación, pero su trabajo es inferir con datos y modelos revisables.
- **No es física de partículas.** Comparte con ella ideas (materia oscura, partículas), pero parte de datos astronómicos.
- **No es especulación.** Una teoría se evalúa por sus predicciones contrastables, no por su elegancia.

## 🗓️ Un día en el puesto

- **Modelo y predicción:** derivas o ajustas una predicción de un modelo para un observable.
- **Datos y errores:** preparas un conjunto de datos, entiendes sus covarianzas y verificas que el análisis no introduzca sesgos.
- **Inferencia:** corres cadenas o ajustes, revisas convergencia y examinas la sensibilidad a tus supuestos.
- **Código y cómputo:** mucho análisis numérico, a veces en clústeres.
- **Discusión y escritura:** presentas con claridad qué se concluye y qué no.

Dicho sin adornos: **la estadística es el oficio**. Una curva bonita sin intervalos de confianza no es un resultado.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Relatividad y cosmología:** expansión, geometría, componentes del universo ([**B26** · Relatividad y cosmología](../programa/tronco-comun/B26-relatividad-y-cosmologia.md), [**B39** · Relatividad general avanzada](../../programa/tronco-comun/B39-relatividad-general-avanzada.md)).
- **Universo temprano y radiación de fondo:** física de la época primitiva y su huella ([**B40** · Universo temprano y radiación cósmica de fondo](../../programa/tronco-comun/B40-universo-temprano-y-radiacion-cosmica-de-fondo.md)).
- **Estructuras y materia oscura:** formación de galaxias y cúmulos ([**B36** · Formación de estructuras cósmicas y materia oscura](../../programa/tronco-comun/B36-formacion-de-estructuras-cosmicas-y-materia-oscura.md), [**B25** · Galaxias y medio interestelar](../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md)).
- **Objetos compactos y altas energías:** agujeros negros, estrellas de neutrones, estallidos ([**B27** · Objetos compactos y altas energías](../programa/tronco-comun/B27-objetos-compactos-y-altas-energias.md)).
- **Multimensajero:** neutrinos, ondas gravitacionales y luz ([**B28** · Astronomía multimensajero](../programa/tronco-comun/B28-astronomia-multimensajero.md)).
- **Inferencia estadística y cómputo:** parámetros, covarianzas y análisis reproducible ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md), [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).

### Herramientas del oficio

```text
Cálculo y análisis:   Python científico, bibliotecas de álgebra y estadística
Inferencia:           ajuste por máxima verosimilitud y métodos bayesianos con muestreo
Modelos:              códigos de evolución de perturbaciones cosmológicas y de simulación de estructuras
Datos:                archivos públicos de misiones y de sondeos
Reproducibilidad:     control de versiones, entornos declarados y semillas fijas
```

Las herramientas calculan; la conclusión es tuya. Un resultado cosmológico sin un análisis de sensibilidad a los supuestos no está terminado.

### Habilidades no técnicas

- **Rigor estadístico y honestidad intelectual:** declarar qué supuestos sostienen tu resultado.
- **Paciencia con la escala:** los datos son pocos y las inferencias, delicadas.
- **Comunicación a públicos mixtos:** explicar un resultado abstracto sin exagerarlo.
- **Trabajo colaborativo:** los grandes proyectos reúnen a cientos de personas.

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
2. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
3. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — A02 · 23 clases
4. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — A02 · 31 clases
5. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
6. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases
7. 📚 [**B17** · Aprendizaje automático científico](../programa/tronco-comun/B17-aprendizaje-automatico-cientifico.md) — A02 · 12 clases
8. 📚 [**B18** · Computación de alto rendimiento](../programa/tronco-comun/B18-computacion-de-alto-rendimiento.md) — A02 · 5 clases
9. 📚 [**B19** · Inferencia bayesiana y computación probabilística](../programa/tronco-comun/B19-inferencia-bayesiana-y-computacion-probabilistica.md) — A02 · 8 clases
10. 📚 [**B20** · Metodología de la investigación científica](../programa/tronco-comun/B20-metodologia-de-la-investigacion-cientifica.md) — A02 · 4 clases
11. 📚 [**B21** · Métodos numéricos para EDP y fluidos computacionales](../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md) — A02 · 5 clases
12. 📚 [**B22** · Problemas inversos y estimación de modelos](../programa/tronco-comun/B22-problemas-inversos-y-estimacion-de-modelos.md) — A02 · 5 clases
13. 📚 [**B23** · Verificación y validación de software científico](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md) — A02 · 8 clases
14. 📚 [**B24** · Física y evolución de estrellas](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) — A03 · 22 clases
15. 📚 [**B29** · Astronomía temporal y exoplanetas](../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md) — A03 · 20 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — usa 2 de 20 clases: `B10-` C17–C18
2. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 6 de 26 clases: `B12-` C12–C13, C18, C21–C23

**A03 · Astrofísica y ciencias fundamentales del universo**

3. 📚 [**B25** · Galaxias y medio interestelar](../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md) — usa 5 de 20 clases: `B25-` C08, C13–C15, C18
4. 📚 [**B26** · Relatividad y cosmología](../programa/tronco-comun/B26-relatividad-y-cosmologia.md) — usa 13 de 23 clases: `B26-` C04, C08, C10, C14–C23
5. 📚 [**B27** · Objetos compactos y altas energías](../programa/tronco-comun/B27-objetos-compactos-y-altas-energias.md) — usa 14 de 22 clases: `B27-` C02–C03, C05, C07–C12, C17–C19, C21–C22
6. 📚 [**B28** · Astronomía multimensajero](../programa/tronco-comun/B28-astronomia-multimensajero.md) — usa 13 de 22 clases: `B28-` C03, C05–C06, C09–C13, C16–C18, C21–C22
7. 📚 [**B30** · Heliofísica y física de plasmas](../programa/tronco-comun/B30-heliofisica-y-fisica-de-plasmas.md) — usa 1 de 23 clases: `B30-` C14
8. 📚 [**B31** · Física cuántica, nuclear y astropartículas](../programa/tronco-comun/B31-fisica-cuantica-nuclear-y-astroparticulas.md) — usa 5 de 20 clases: `B31-` C13–C14, C16–C18
9. 📚 [**B36** · Formación de estructuras cósmicas y materia oscura](../programa/tronco-comun/B36-formacion-de-estructuras-cosmicas-y-materia-oscura.md) — usa 11 de 11 clases: `B36-` C01–C11
10. 📚 [**B39** · Relatividad general avanzada](../programa/tronco-comun/B39-relatividad-general-avanzada.md) — usa 6 de 6 clases: `B39-` C01–C06
11. 📚 [**B40** · Universo temprano y radiación cósmica de fondo](../programa/tronco-comun/B40-universo-temprano-y-radiacion-cosmica-de-fondo.md) — usa 15 de 15 clases: `B40-` C01–C15

**A04 · Óptica, telescopios y observatorios científicos**

12. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — usa 2 de 25 clases: `B47-` C05–C06

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

13. 📚 [**B55** · Astroquímica y geoquímica extraterrestre](../programa/tronco-comun/B55-astroquimica-y-geoquimica-extraterrestre.md) — usa 1 de 20 clases: `B55-` C02

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es una **inferencia de parámetros reproducible**:

- un modelo y sus parámetros, con la justificación de cada supuesto;
- un conjunto de datos con su covarianza y los criterios de selección;
- un ajuste con incertidumbres y diagnóstico de convergencia;
- una prueba de sensibilidad a los supuestos y una comparación con resultados publicados;
- el código y el entorno para repetirlo.

Cada bloque de la ruta aporta ejercicios y laboratorios; conserva la primera versión y los cambios como parte de la evidencia.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada: la competencia se demuestra con trabajo revisado. Referencias de trabajo consultadas (2026-11-05):

- 📘 **Planck 2018 results. VI. Cosmological parameters** (Planck Collaboration; A&A 641, A6, 2020; arXiv:1807.06209): fuente de los parámetros del modelo estándar usados en este programa. Se leyeron el resumen y la Tabla 1 del manuscrito.
- 📗 **Riess et al. 2022** (arXiv:2112.04510): medida local de la constante de Hubble, que ilustra la discrepancia con la anterior. Se leyeron el resumen y el texto del manuscrito.

Los requisitos de acceso a datos, tiempo de cómputo o publicación dependen de cada colaboración y no están verificados aquí.

## 📈 Progresión del rol

Ruta habitual: **grado → posgrado → investigación posdoctoral → posición académica o en una institución de investigación**; desde el análisis estadístico se abren carreras en ciencia de datos y modelado. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md), [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md) y [Heliofísica y climatología espacial](heliofisica-y-climatologia-espacial.md).

## ⚠️ Mitos y errores comunes

- **«Cosmología es filosofía».** Es una ciencia de predicciones cuantitativas contrastadas con datos.
- **«Basta con una teoría bonita».** Se evalúa por sus predicciones, no por su belleza.
- **«Los parámetros se miden directamente».** Se infieren con modelos; cambiar el modelo cambia la cifra.
- **«Dos mediciones distintas, una está mal».** Puede haber sistemáticos en ambas, o un modelo incompleto: la discrepancia es información.
- **«La estadística es un trámite».** Es el núcleo del oficio.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la matemática (cálculo y álgebra lineal) de tu diagnóstico.
2. Estudia **relatividad y cosmología** ([**B26** · Relatividad y cosmología](../programa/tronco-comun/B26-relatividad-y-cosmologia.md)) y **objetos compactos** ([**B27** · Objetos compactos y altas energías](../programa/tronco-comun/B27-objetos-compactos-y-altas-energias.md)).
3. Aprende **inferencia y manejo de incertidumbre** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)) y análisis reproducible ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).
4. Profundiza en **universo temprano** ([**B40** · Universo temprano y radiación cósmica de fondo](../../programa/tronco-comun/B40-universo-temprano-y-radiacion-cosmica-de-fondo.md)) o en **estructuras y materia oscura** ([**B36** · Formación de estructuras cósmicas y materia oscura](../../programa/tronco-comun/B36-formacion-de-estructuras-cosmicas-y-materia-oscura.md)).
5. Reúne tu **inferencia reproducible** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md) · [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md) · [Heliofísica y climatología espacial](heliofisica-y-climatologia-espacial.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R02-cosmologia-y-astrofisica-extrema/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
