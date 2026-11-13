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

- **Relatividad y cosmología:** expansión, geometría, componentes del universo ([**B26** · Relatividad y cosmología](../programa/tronco-comun/B26-relatividad-y-cosmologia.md), [**B39** · Relatividad general avanzada](../programa/tronco-comun/B39-relatividad-general-avanzada.md)).
- **Universo temprano y radiación de fondo:** física de la época primitiva y su huella ([**B40** · Universo temprano y radiación cósmica de fondo](../programa/tronco-comun/B40-universo-temprano-y-radiacion-cosmica-de-fondo.md)).
- **Estructuras y materia oscura:** formación de galaxias y cúmulos ([**B36** · Formación de estructuras cósmicas y materia oscura](../programa/tronco-comun/B36-formacion-de-estructuras-cosmicas-y-materia-oscura.md), [**B25** · Galaxias y medio interestelar](../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md)).
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
7. 📚 [**B24** · Física y evolución de estrellas](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) — A03 · 22 clases
8. 📚 [**B29** · Astronomía temporal y exoplanetas](../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md) — A03 · 20 clases

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

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes calcular la dilatación del tiempo y la contracción de longitudes en un caso de relatividad especial?
- ¿Sabes qué mide el corrimiento al rojo y cómo se relaciona con la distancia en un universo en expansión?
- ¿Puedes integrar numéricamente una ecuación diferencial y comprobar la convergencia?
- ¿Distingues una medida de una inferencia y un modelo?

#### R02-M01 · Relatividad avanzada

1. **Cálculo tensorial relativista** — [`B10-C17`](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md), [`B10-C18`](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md), [`B26-C04`](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md)
2. **Geometría diferencial** — [`B39-C01`](../programa/clases/B39/B39-C01-variedades-tensor-metrico-y-geometria-diferencial/CLASE.md)
3. **Conexión afín** — [`B39-C02`](../programa/clases/B39/B39-C02-conexion-afin-y-simbolos-de-christoffel/CLASE.md)
4. **Geodésicas** — [`B26-C08`](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md)
5. **Curvatura de Riemann** — [`B39-C03`](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md)
6. **Tensor energía-momento** — [`B39-C04`](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md)
7. **Ecuaciones de Einstein** — [`B39-C05`](../programa/clases/B39/B39-C05-ecuaciones-de-campo-de-einstein-y-limite-newtoniano/CLASE.md)
8. **Métricas estacionarias** — [`B27-C07`](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md), [`B27-C08`](../programa/clases/B27/B27-C08-horizonte-de-sucesos/CLASE.md)
9. **Relatividad numérica inicial** — [`B39-C06`](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md)
10. **Predicciones observacionales** — [`B26-C10`](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md), [`B27-C09`](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md), [`B28-C05`](../programa/clases/B28/B28-C05-ondas-gravitacionales/CLASE.md)

✅ **Checkpoint R02-M01.** Sin mirar el material, explica cómo se relacionan «Cálculo tensorial relativista», «Tensor energía-momento» y «Predicciones observacionales», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R02-M02 · Universo temprano

1. **Inflación cósmica** — [`B40-C01`](../programa/clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md)
2. **Recalentamiento** — [`B40-C02`](../programa/clases/B40/B40-C02-recalentamiento-y-transicion-a-la-era-de-radiacion/CLASE.md)
3. **Era de radiación** — [`B26-C14`](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md)
4. **Desacoplamiento de neutrinos** — [`B40-C03`](../programa/clases/B40/B40-C03-desacoplamiento-de-neutrinos-y-fondo-cosmico-de-neutrinos/CLASE.md)
5. **Nucleosíntesis primordial** — [`B26-C16`](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md), [`B55-C02`](../programa/clases/B55/B55-C02-nucleosintesis-y-elementos/CLASE.md)
6. **Recombinación cósmica** — [`B26-C14`](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md), [`B26-C15`](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md)
7. **Horizonte y planitud** — [`B40-C04`](../programa/clases/B40/B40-C04-problemas-del-horizonte-y-de-la-planitud/CLASE.md)
8. **Perturbaciones primordiales** — [`B40-C05`](../programa/clases/B40/B40-C05-perturbaciones-primordiales-y-espectro-escalar/CLASE.md)
9. **Campos escalares cosmológicos** — [`B40-C06`](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md)
10. **Restricciones de teorías tempranas** — [`B26-C20`](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md), [`B31-C18`](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md)

✅ **Checkpoint R02-M02.** Sin mirar el material, explica cómo se relacionan «Inflación cósmica», «Recombinación cósmica» y «Restricciones de teorías tempranas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R02-M03 · Radiación cósmica de fondo

1. **Anisotropías del fondo** — [`B26-C15`](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md)
2. **Espectro angular de potencias** — [`B40-C07`](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md)
3. **Polarización E y B** — [`B40-C08`](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md)
4. **Efecto Sachs-Wolfe** — [`B40-C09`](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md)
5. **Foregrounds galácticos** — [`B40-C10`](../programa/clases/B40/B40-C10-emisiones-de-primer-plano-galacticas-y-su-separacion/CLASE.md)
6. **Efecto Sunyaev-Zeldovich** — [`B40-C11`](../programa/clases/B40/B40-C11-efecto-sunyaev-zeldovich-termico-y-cinematico/CLASE.md)
7. **Análisis de mapas** — [`B40-C12`](../programa/clases/B40/B40-C12-analisis-de-mapas-del-cmb-pixelizacion-esferica-y-mascaras/CLASE.md)
8. **Covarianza instrumental** — [`B40-C13`](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md)
9. **Datos de Planck** — [`B40-C14`](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md)
10. **Limitaciones observacionales** — [`B40-C15`](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md)

✅ **Checkpoint R02-M03.** Sin mirar el material, explica cómo se relacionan «Anisotropías del fondo», «Efecto Sunyaev-Zeldovich» y «Limitaciones observacionales», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R02-M04 · Formación de estructuras cósmicas

1. **Fluctuaciones de densidad** — [`B26-C17`](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md), [`B25-C18`](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md)
2. **Crecimiento lineal** — [`B36-C01`](../programa/clases/B36/B36-C01-crecimiento-lineal-de-perturbaciones-de-densidad/CLASE.md)
3. **Transferencia de materia** — [`B36-C02`](../programa/clases/B36/B36-C02-funcion-de-transferencia-y-espectro-de-materia/CLASE.md)
4. **Funciones de correlación** — [`B36-C03`](../programa/clases/B36/B36-C03-funciones-de-correlacion-de-galaxias/CLASE.md)
5. **Espectro de potencia** — [`B36-C04`](../programa/clases/B36/B36-C04-espectro-de-potencia-de-materia/CLASE.md)
6. **Simulaciones cosmológicas** — [`B36-C05`](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md)
7. **Halos de materia** — [`B36-C06`](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md)
8. **Formación de cúmulos** — [`B25-C13`](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md)
9. **Oscilaciones acústicas bariónicas** — [`B36-C07`](../programa/clases/B36/B36-C07-oscilaciones-acusticas-barionicas-como-regla-estandar/CLASE.md)
10. **Sesgos de trazadores** — [`B36-C08`](../programa/clases/B36/B36-C08-sesgo-de-galaxias-y-trazadores-de-la-materia/CLASE.md)

✅ **Checkpoint R02-M04.** Sin mirar el material, explica cómo se relacionan «Fluctuaciones de densidad», «Simulaciones cosmológicas» y «Sesgos de trazadores», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R02-M05 · Materia oscura

1. **Evidencia de materia no luminosa** — [`B26-C18`](../programa/clases/B26/B26-C18-materia-oscura-y-evidencias/CLASE.md)
2. **Curvas de rotación** — [`B25-C08`](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md)
3. **Lentes gravitacionales** — [`B25-C14`](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md)
4. **Cúmulos en colisión** — [`B36-C09`](../programa/clases/B36/B36-C09-cumulos-en-colision-como-prueba-de-materia-oscura/CLASE.md)
5. **Modelos de halo** — [`B25-C15`](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md)
6. **Candidatos de partículas** — [`B31-C17`](../programa/clases/B31/B31-C17-materias-oscuras-candidatas/CLASE.md)
7. **Búsqueda directa** — [`B36-C10`](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md)
8. **Búsqueda indirecta** — [`B31-C16`](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md), [`B27-C19`](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md)
9. **Modelos modificados como alternativas** — [`B36-C11`](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md)
10. **Restricciones conjuntas** — [`B31-C18`](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md), [`B26-C20`](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md)

✅ **Checkpoint R02-M05.** Sin mirar el material, explica cómo se relacionan «Evidencia de materia no luminosa», «Candidatos de partículas» y «Restricciones conjuntas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R02-M06 · Astrofísica de altas energías

1. **Procesos de acreción** — [`B27-C10`](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md)
2. **Radiación sincrotrón** — [`B27-C12`](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md)
3. **Compton inverso** — [`B27-C21`](../programa/clases/B27/B27-C21-dispersion-compton-inversa-y-emision-de-alta-energia/CLASE.md)
4. **Partículas aceleradas** — [`B30-C14`](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md), [`B31-C13`](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md)
5. **Estrellas compactas** — [`B27-C02`](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md), [`B27-C03`](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md), [`B27-C05`](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md)
6. **Explosiones gamma** — [`B27-C17`](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md)
7. **Chorros relativistas** — [`B27-C11`](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md)
8. **Fuentes de rayos X** — [`B27-C19`](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md), [`B47-C05`](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md)
9. **Detectores de alta energía** — [`B27-C19`](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md), [`B47-C05`](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md), [`B47-C06`](../programa/clases/B47/B47-C06-instrumentos-de-rayos-gamma/CLASE.md), [`B31-C14`](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md)
10. **Análisis espectral energético** — [`B27-C22`](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md)

✅ **Checkpoint R02-M06.** Sin mirar el material, explica cómo se relacionan «Procesos de acreción», «Explosiones gamma» y «Análisis espectral energético», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R02-M07 · Astronomía multimensajero

1. **Formas de onda gravitacional** — [`B28-C21`](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md)
2. **Fuentes de neutrinos** — [`B28-C03`](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md), [`B27-C18`](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md)
3. **Alertas electromagnéticas** — [`B28-C09`](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md), [`B28-C16`](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md)
4. **Kilonovas** — [`B28-C18`](../programa/clases/B28/B28-C18-interpretacion-de-kilonovas/CLASE.md)
5. **Redes de interferómetros** — [`B28-C06`](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md), [`B28-C16`](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md)
6. **Significancia de coincidencias** — [`B28-C13`](../programa/clases/B28/B28-C13-estadistica-de-significancia/CLASE.md)
7. **Localización de eventos** — [`B28-C10`](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md)
8. **Modelos multiobservatorio** — [`B28-C11`](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md), [`B28-C12`](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md)
9. **Datos de eventos públicos** — [`B28-C17`](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md)
10. **Inferencia de fuente conjunta** — [`B28-C22`](../programa/clases/B28/B28-C22-inferencia-bayesiana-conjunta-de-parametros-de-fuente-multimensajero/CLASE.md)

✅ **Checkpoint R02-M07.** Sin mirar el material, explica cómo se relacionan «Formas de onda gravitacional», «Significancia de coincidencias» y «Inferencia de fuente conjunta», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R02-M08 · Inferencia y parámetros cosmológicos

1. **Parámetros de modelo Lambda-CDM** — [`B26-C19`](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md)
2. **Verosimilitud cosmológica** — [`B26-C21`](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md)
3. **Covarianzas de datos** — [`B12-C18`](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md)
4. **Muestreo MCMC** — [`B12-C13`](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md)
5. **Priors científicos** — [`B12-C12`](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md)
6. **Inferencia jerárquica** — [`B12-C21`](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md)
7. **Degeneraciones de parámetros** — [`B26-C22`](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md)
8. **Comparación de modelos** — [`B12-C22`](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md)
9. **Tensiones observacionales** — [`B26-C23`](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md)
10. **Reproducibilidad de cadenas** — [`B12-C23`](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md)

✅ **Checkpoint R02-M08.** Sin mirar el material, explica cómo se relacionan «Parámetros de modelo Lambda-CDM», «Inferencia jerárquica» y «Reproducibilidad de cadenas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Estimación de parámetros cosmológicos con datos públicos.** Ajusta un modelo de universo plano a un catálogo público de supernovas y compara con otra prueba independiente, informando con honestidad la tensión entre ambas.

Entregables:

- Código de inferencia con priors declarados
- Cadenas y gráficos de contorno de los parámetros
- Comparación con una segunda prueba (por ejemplo, oscilaciones acústicas)
- Memoria con la discusión de sesgos y sistemáticos

Criterios de evaluación:

- Los priors y el modelo están justificados y versionados
- La convergencia de las cadenas está demostrada
- Se explica qué datos se usan y cuáles se excluyen y por qué
- Las conclusiones no superan lo que permiten los errores

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes plantear y resolver un modelo cosmológico sencillo y estimar sus parámetros con incertidumbre.
- Puedes explicar la evidencia de la expansión, la radiación de fondo y la materia oscura sin sobreafirmar.
- Puedes criticar un resultado de la literatura identificando sus supuestos.

<!-- /recorrido -->

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
4. Profundiza en **universo temprano** ([**B40** · Universo temprano y radiación cósmica de fondo](../programa/tronco-comun/B40-universo-temprano-y-radiacion-cosmica-de-fondo.md)) o en **estructuras y materia oscura** ([**B36** · Formación de estructuras cósmicas y materia oscura](../programa/tronco-comun/B36-formacion-de-estructuras-cosmicas-y-materia-oscura.md)).
5. Reúne tu **inferencia reproducible** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md) · [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md) · [Heliofísica y climatología espacial](heliofisica-y-climatologia-espacial.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R02-cosmologia-y-astrofisica-extrema/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
