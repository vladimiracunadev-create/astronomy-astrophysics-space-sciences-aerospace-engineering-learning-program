# 🧮 Matemática y computación científica espacial

> Construyes los métodos matemáticos y el software con que se resuelven problemas espaciales: simulación, estimación, aprendizaje automático y cómputo de alto rendimiento, con resultados verificables.
>
> **Nivel de entrada:** matemática y programación de nivel universitario; rol técnico y de investigación · **Foco:** métodos numéricos, inferencia, problemas inversos, aprendizaje automático científico, cómputo de alto rendimiento, verificación y validación · **Entrega:** un código científico con sus pruebas, su verificación frente a casos conocidos y la cuantificación de su incertidumbre

## 🧭 Qué es y por qué importa

Casi todo problema espacial termina en un cálculo: resolver ecuaciones diferenciales, ajustar un modelo a datos, estimar un parámetro desde mediciones ruidosas o entrenar un modelo con observaciones. Este rol **construye y valida esas herramientas** en vez de limitarse a usarlas.

Su rasgo propio es la **confianza en el resultado**. Un número calculado no es una respuesta mientras no se sepa cuánto error numérico trae, cuánta incertidumbre hereda de los datos y si el código realmente resuelve la ecuación que se pretendía.

Las miradas del rol son:

- **Métodos numéricos.** Discretización, estabilidad y convergencia. Su pregunta es: *¿converge a la solución correcta y a qué costo?*
- **Inferencia y estimación.** Bayes, problemas inversos, aprendizaje. Su pregunta es: *¿qué dicen los datos y con cuánta incertidumbre?*
- **Software y cómputo.** Verificación, validación y alto rendimiento. Su pregunta es: *¿puedo confiar en este código y repetir la corrida?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es desarrollo de software genérico.** Se comparte la ingeniería, pero el criterio de corrección es físico y numérico.
- **No es ciencia de datos sin física.** El aprendizaje automático aquí se contrasta con modelos y leyes conocidas.
- **No es astrofísica de objetos.** Provees el método a quien estudia el objeto ([Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md)).
- **No es «correr un paquete».** Cuando el paquete falla o se aplica donde no corresponde, hay que entender por qué.

## 🗓️ Un día en el puesto

- **Diseño de un método:** eliges un esquema numérico y estimas su error esperado.
- **Pruebas:** verificas con una solución conocida y revisas convergencia.
- **Ajuste y estimación:** estimas parámetros con su incertidumbre.
- **Rendimiento:** perfilas el código y decides qué paralelizar.
- **Revisión con quien usa el código:** discutes qué supuestos asume.

Dicho sin adornos: **un código que corre no es un código correcto**, y distinguirlos es el trabajo.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Ecuaciones diferenciales y simulación** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)); **métodos numéricos para EDP** ([**B21** · Métodos numéricos para EDP y fluidos computacionales](../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md)).
- **Álgebra lineal** ([**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md)); **probabilidad y estadística** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)).
- **Inferencia bayesiana** ([**B19** · Inferencia bayesiana y computación probabilística](../programa/tronco-comun/B19-inferencia-bayesiana-y-computacion-probabilistica.md)); **problemas inversos** ([**B22** · Problemas inversos y estimación de modelos](../programa/tronco-comun/B22-problemas-inversos-y-estimacion-de-modelos.md)).
- **Aprendizaje automático científico** ([**B17** · Aprendizaje automático científico](../programa/tronco-comun/B17-aprendizaje-automatico-cientifico.md)).
- **Computación de alto rendimiento** ([**B18** · Computación de alto rendimiento](../programa/tronco-comun/B18-computacion-de-alto-rendimiento.md)).
- **Verificación y validación** ([**B23** · Verificación y validación de software científico](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md)); **computación científica y ciencia abierta** ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).

### Herramientas del oficio

```text
Lenguajes:            Python y un lenguaje compilado para el cálculo intensivo
Control de versiones: Git y revisión de código
Pruebas:              pruebas unitarias y de convergencia
Cómputo:              entornos de cálculo paralelo y de aceleración
Datos:                formatos abiertos y registro de procedencia
```

Un resultado sin semilla, versión ni entorno registrados no se puede reproducir. Fija y documenta lo que pueda cambiar.

### Habilidades no técnicas

- **Escepticismo con los propios resultados.**
- **Escritura técnica clara.**
- **Colaboración con quienes usan el código.**
- **Disciplina de ingeniería** en pruebas y revisión.

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B07** · Informática científica desde cero](../programa/tronco-comun/B07-informatica-cientifica-desde-cero.md) — A01 · 20 clases
2. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
3. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — usa 2 de 20 clases: `B10-` C05, C10
2. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — usa 14 de 26 clases: `B11-` C08–C09, C11–C15, C19, C21–C26
3. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 5 de 26 clases: `B12-` C07, C10, C12–C13, C16
4. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 2 de 23 clases: `B13-` C02, C19
5. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 14 de 31 clases: `B14-` C04, C06, C09–C16, C19–C20, C23–C24
6. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — usa 1 de 24 clases: `B15-` C19
7. 📚 [**B17** · Aprendizaje automático científico](../programa/tronco-comun/B17-aprendizaje-automatico-cientifico.md) — usa 9 de 12 clases: `B17-` C01–C09
8. 📚 [**B18** · Computación de alto rendimiento](../programa/tronco-comun/B18-computacion-de-alto-rendimiento.md) — usa 5 de 5 clases: `B18-` C01–C05
9. 📚 [**B19** · Inferencia bayesiana y computación probabilística](../programa/tronco-comun/B19-inferencia-bayesiana-y-computacion-probabilistica.md) — usa 8 de 8 clases: `B19-` C01–C08
10. 📚 [**B21** · Métodos numéricos para EDP y fluidos computacionales](../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md) — usa 4 de 5 clases: `B21-` C02–C05
11. 📚 [**B22** · Problemas inversos y estimación de modelos](../programa/tronco-comun/B22-problemas-inversos-y-estimacion-de-modelos.md) — usa 5 de 5 clases: `B22-` C01–C05
12. 📚 [**B23** · Verificación y validación de software científico](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md) — usa 8 de 8 clases: `B23-` C01–C08

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

13. 📚 [**B53** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md) — usa 1 de 30 clases: `B53-` C28

**A06 · Mecánica orbital, navegación y vuelo espacial**

14. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 1 de 30 clases: `B74-` C01

**A11 · Economía, industria y gestión de proyectos espaciales**

15. 📚 [**B124** · Industria, economía, ética y proyectos espaciales](../programa/tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) — usa 2 de 24 clases: `B124-` C09, C14

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes resolver un sistema lineal y estimar el error numérico?
- ¿Sabes aplicar el teorema de Bayes a un ejemplo concreto?
- ¿Escribes código reproducible con control de versiones?
- ¿Entiendes la complejidad de un algoritmo?

#### R08-M01 · Algoritmos numéricos avanzados

1. **Integración de alta precisión** — [`B11-C21`](../programa/clases/B11/B11-C21-integracion-numerica-de-alta-precision/CLASE.md)
2. **Integradores simplécticos** — [`B11-C11`](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md)
3. **Métodos implícitos** — [`B11-C22`](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md)
4. **Tolerancias adaptativas** — [`B11-C08`](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md)
5. **Resolución de sistemas lineales** — [`B10-C05`](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md), [`B10-C10`](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md)
6. **Optimización restringida** — [`B11-C23`](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md)
7. **Métodos espectrales** — [`B11-C24`](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md)
8. **Errores de redondeo** — [`B11-C25`](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md)
9. **Benchmark de algoritmos** — [`B11-C26`](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md)
10. **Pruebas de convergencia** — [`B11-C19`](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md)

✅ **Checkpoint R08-M01.** Sin mirar el material, explica cómo se relacionan «Integración de alta precisión», «Optimización restringida» y «Pruebas de convergencia», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R08-M02 · Computación de alto rendimiento

1. **Arquitecturas HPC** — [`B14-C16`](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md)
2. **Procesamiento multinúcleo** — [`B14-C13`](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md)
3. **Ejecución por procesos** — [`B18-C01`](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md)
4. **MPI conceptual** — [`B18-C02`](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md)
5. **Programación GPU** — [`B14-C15`](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md)
6. **Estructuras de memoria** — [`B18-C03`](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md)
7. **Vectorización** — [`B14-C14`](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md)
8. **Paralelismo de datos** — [`B14-C13`](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md)
9. **Perfilado de rendimiento** — [`B18-C04`](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md)
10. **Experimentos de escalabilidad** — [`B18-C05`](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md)

✅ **Checkpoint R08-M02.** Sin mirar el material, explica cómo se relacionan «Arquitecturas HPC», «Estructuras de memoria» y «Experimentos de escalabilidad», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R08-M03 · Métodos para ecuaciones en derivadas parciales

1. **Ecuación de calor** — [`B11-C13`](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md), [`B11-C14`](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md)
2. **Ecuación de onda** — [`B21-C02`](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md)
3. **Ecuaciones de Poisson** — [`B21-C03`](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md)
4. **Ecuaciones de Navier-Stokes** — [`B21-C04`](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md)
5. **Discretización espacial** — [`B11-C14`](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md), [`B11-C15`](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md)
6. **Condiciones de contorno** — [`B11-C12`](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md)
7. **Mallas regulares** — [`B11-C14`](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md)
8. **Mallas adaptativas** — [`B21-C05`](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md)
9. **Estabilidad CFL** — [`B11-C09`](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md)
10. **Comparación de soluciones** — [`B11-C19`](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md)

✅ **Checkpoint R08-M03.** Sin mirar el material, explica cómo se relacionan «Ecuación de calor», «Condiciones de contorno» y «Comparación de soluciones», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R08-M04 · Problemas inversos astronómicos

1. **Problemas directos e inversos** — [`B22-C01`](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md)
2. **Regularización de Tikhonov** — [`B22-C02`](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md)
3. **Máxima verosimilitud** — [`B12-C07`](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md)
4. **Modelos de observación** — [`B74-C01`](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md)
5. **Identificabilidad** — [`B22-C03`](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md)
6. **Reconstrucción tomográfica** — [`B15-C19`](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md)
7. **Inversión espectral** — [`B22-C04`](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md)
8. **Inversión gravimétrica** — [`B53-C28`](../programa/clases/B53/B53-C28-inversion-gravimetrica-y-modelos-de-densidad/CLASE.md)
9. **Cuantificación de incertidumbre** — [`B12-C16`](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md)
10. **Pruebas con datos sintéticos** — [`B22-C05`](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md)

✅ **Checkpoint R08-M04.** Sin mirar el material, explica cómo se relacionan «Problemas directos e inversos», «Reconstrucción tomográfica» y «Pruebas con datos sintéticos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R08-M05 · Modelos bayesianos científicos

1. **Regla de Bayes** — [`B12-C12`](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md)
2. **Priors físicos** — [`B19-C01`](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md)
3. **Modelos jerárquicos** — [`B19-C02`](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md)
4. **MCMC** — [`B12-C13`](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md)
5. **Hamiltonian Monte Carlo conceptual** — [`B19-C03`](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md)
6. **Diagnóstico de convergencia** — [`B19-C04`](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md)
7. **Inferencia variacional** — [`B19-C05`](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md)
8. **Predicción posterior** — [`B19-C06`](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md)
9. **Comparación de modelos** — [`B19-C07`](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md)
10. **Calibración probabilística** — [`B19-C08`](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md)

✅ **Checkpoint R08-M05.** Sin mirar el material, explica cómo se relacionan «Regla de Bayes», «Diagnóstico de convergencia» y «Calibración probabilística», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R08-M06 · Aprendizaje automático científico

1. **Ingeniería de características científicas** — [`B17-C01`](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md)
2. **Aprendizaje supervisado** — [`B17-C02`](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md)
3. **Regresión no lineal** — [`B12-C10`](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md)
4. **Redes neuronales físicas PINN** — [`B17-C03`](../programa/clases/B17/B17-C03-redes-neuronales-informadas-por-la-fisica-pinn/CLASE.md)
5. **Modelos sustitutos** — [`B17-C04`](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md)
6. **Detección de anomalías** — [`B17-C05`](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md)
7. **Aprendizaje no supervisado** — [`B17-C06`](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md)
8. **Validación fuera de distribución** — [`B17-C07`](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md)
9. **Interpretabilidad física** — [`B17-C08`](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md)
10. **Prevención de fuga de datos** — [`B17-C09`](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md)

✅ **Checkpoint R08-M06.** Sin mirar el material, explica cómo se relacionan «Ingeniería de características científicas», «Detección de anomalías» y «Prevención de fuga de datos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R08-M07 · Verificación y validación computacional

1. **Pruebas unitarias numéricas** — [`B23-C01`](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md)
2. **Pruebas de propiedades físicas** — [`B23-C02`](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md)
3. **Casos analíticos** — [`B23-C03`](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md)
4. **Soluciones de referencia** — [`B23-C04`](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md)
5. **Validación por conjuntos oficiales** — [`B23-C05`](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md)
6. **Análisis dimensional automatizado** — [`B14-C04`](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md), [`B13-C02`](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md)
7. **Pruebas metamórficas** — [`B23-C06`](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md)
8. **Pruebas de regresión** — [`B14-C10`](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md)
9. **Trazabilidad científica** — [`B23-C07`](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md)
10. **Informe de verificación** — [`B23-C08`](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md)

✅ **Checkpoint R08-M07.** Sin mirar el material, explica cómo se relacionan «Pruebas unitarias numéricas», «Análisis dimensional automatizado» y «Informe de verificación», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R08-M08 · Publicación de investigación reproducible

1. **Protocolo preregistrado** — [`B14-C23`](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md)
2. **Gestión de datos FAIR** — [`B14-C19`](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md), [`B124-C14`](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md)
3. **Versionado de experimentos** — [`B14-C11`](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md)
4. **Repositorios de código** — [`B14-C19`](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md)
5. **Entornos reproducibles uv** — [`B14-C12`](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md)
6. **Metadatos científicos** — [`B13-C19`](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md), [`B14-C06`](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md)
7. **Documentación de hipótesis** — [`B14-C24`](../programa/clases/B14/B14-C24-documentacion-de-hipotesis-y-decisiones-de-analisis/CLASE.md)
8. **Notebooks auditables** — [`B14-C09`](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md)
9. **Licencias de datos** — [`B124-C09`](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md)
10. **Paquete de reproducibilidad completo** — [`B14-C20`](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md), [`B14-C19`](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md)

✅ **Checkpoint R08-M08.** Sin mirar el material, explica cómo se relacionan «Protocolo preregistrado», «Metadatos científicos» y «Paquete de reproducibilidad completo», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Pipeline reproducible de inferencia con datos astronómicos.** Implementa un problema inverso (por ejemplo, ajustar una curva de luz) con verificación contra una solución conocida y publica el estudio con todo lo necesario para reproducirlo.

Entregables:

- Código con pruebas automatizadas
- Verificación contra un caso con solución analítica
- Análisis de sensibilidad y de convergencia
- Repositorio con datos, entorno y documentación

Criterios de evaluación:

- Un tercero reproduce los resultados sin ayuda
- Las pruebas cubren los casos límite
- Se separan verificación (¿resuelvo bien las ecuaciones?) y validación (¿son las ecuaciones correctas?)
- Se reportan los costos de cómputo

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes elegir, implementar y verificar un método numérico para un problema científico.
- Puedes hacer inferencia bayesiana con diagnósticos de convergencia.
- Puedes publicar un estudio computacional reproducible.

<!-- /recorrido -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **código científico verificado**:

- un problema con solución conocida y el código que lo resuelve;
- pruebas de convergencia y comparación con la solución de referencia;
- una cuantificación de incertidumbre;
- la documentación del entorno para repetir la corrida;
- un caso aplicado a un problema espacial.

Los bloques de la ruta aportan ejercicios y laboratorios; guarda la primera versión y sus cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada, y para esta guía no se consultó una fuente externa específica (2026-11-05). Por eso no se citan normas, requisitos de acceso ni cifras: cuando se necesiten, deben consultarse en la fuente oficial vigente de la institución, agencia o empresa correspondiente.

## 📈 Progresión del rol

Rutas habituales: **científico/a o ingeniero/a de software científico → responsable de un código o de una plataforma de simulación → liderazgo técnico de cómputo**. Se abren el análisis de datos y la ingeniería de simulación en otras áreas del programa. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md), [Heliofísica y climatología espacial](heliofisica-y-climatologia-espacial.md) y [Astrodinámica interplanetaria](astrodinamica-interplanetaria.md).

## ⚠️ Mitos y errores comunes

- **«Más cómputo arregla un método malo».** Un esquema inestable sigue siéndolo.
- **«El aprendizaje automático reemplaza al modelo físico».** Se complementan, y se debe validar contra la física.
- **«Si coincide con el dato, es correcto».** Puede coincidir por compensación de errores.
- **«Las pruebas son un lujo».** En código científico son la única evidencia de corrección.
- **«Reproducible es lo mismo que correcto».** Es condición necesaria, no suficiente.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la matemática de tu diagnóstico.
2. Estudia **ecuaciones diferenciales** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)), **álgebra lineal** ([**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md)) y **estadística** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)).
3. Profundiza en **métodos numéricos para EDP** ([**B21** · Métodos numéricos para EDP y fluidos computacionales](../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md)) y **problemas inversos** ([**B22** · Problemas inversos y estimación de modelos](../programa/tronco-comun/B22-problemas-inversos-y-estimacion-de-modelos.md)).
4. Avanza a **inferencia bayesiana** ([**B19** · Inferencia bayesiana y computación probabilística](../programa/tronco-comun/B19-inferencia-bayesiana-y-computacion-probabilistica.md)) y **aprendizaje automático científico** ([**B17** · Aprendizaje automático científico](../programa/tronco-comun/B17-aprendizaje-automatico-cientifico.md)).
5. Cierra con **cómputo de alto rendimiento** ([**B18** · Computación de alto rendimiento](../programa/tronco-comun/B18-computacion-de-alto-rendimiento.md)) y **verificación y validación** ([**B23** · Verificación y validación de software científico](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md)).

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md) · [Cosmología y astrofísica extrema](cosmologia-y-astrofisica-extrema.md) · [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R08-matematica-y-computacion-cientifica-espacial/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
