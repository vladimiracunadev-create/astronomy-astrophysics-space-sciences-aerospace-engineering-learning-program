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
- **Radiación y espectros:** formación de líneas, atmósferas, abundancias ([**B32** · Atmósferas estelares y espectroscopía estelar cuantitativa](../programa/tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md), [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md)).
- **Interiores y oscilaciones:** modelos de estructura y asterosismología ([**B37** · Interiores estelares y asterosismología](../programa/tronco-comun/B37-interiores-estelares-y-asterosismologia.md)).
- **Galaxias y poblaciones:** estructura, medio interestelar, historia de formación estelar y simulación ([**B25** · Galaxias y medio interestelar](../programa/tronco-comun/B25-galaxias-y-medio-interestelar.md), [**B38** · Poblaciones estelares y simulación de galaxias](../programa/tronco-comun/B38-poblaciones-estelares-y-simulacion-de-galaxias.md)).
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

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes derivar la luminosidad de una estrella a partir de su radio y su temperatura efectiva, con unidades?
- ¿Sabes leer un diagrama de Hertzsprung-Russell y ubicar en él una estrella de 1 y de 10 masas solares?
- ¿Puedes ajustar una recta a datos con incertidumbres y reportar el error del ajuste?
- ¿Escribes un script que lea un espectro y mida la posición de una línea?

#### R01-M01 · Atmósferas estelares

1. **Transferencia radiativa** — [`B32-C01`](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md)
2. **Modelos LTE y no LTE** — [`B32-C02`](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md)
3. **Opacidad continua** — [`B32-C03`](../programa/clases/B32/B32-C03-opacidad-continua-ligado-libre-libre-libre-y-h/CLASE.md)
4. **Opacidad de líneas** — [`B32-C04`](../programa/clases/B32/B32-C04-opacidad-de-lineas-ensanchamiento-y-perfil-de-voigt/CLASE.md)
5. **Equilibrio radiativo** — [`B24-C05`](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md), [`B24-C09`](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md)
6. **Estructura de temperatura** — [`B32-C05`](../programa/clases/B32/B32-C05-relacion-t-y-estructura-termica-de-la-fotosfera/CLASE.md)
7. **Turbulencia atmosférica estelar** — [`B32-C06`](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md)
8. **Campos magnéticos superficiales** — [`B24-C11`](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md), [`B24-C12`](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md)
9. **Modelos de atmósferas 1D y 3D** — [`B32-C07`](../programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/CLASE.md)
10. **Inversión de perfiles espectrales** — [`B32-C08`](../programa/clases/B32/B32-C08-sintesis-espectral-e-inversion-de-perfiles/CLASE.md)

✅ **Checkpoint R01-M01.** Sin mirar el material, explica cómo se relacionan «Transferencia radiativa», «Estructura de temperatura» y «Inversión de perfiles espectrales», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R01-M02 · Modelos de interiores estelares

1. **Ecuaciones de estructura estelar** — [`B24-C04`](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md), [`B24-C05`](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md), [`B24-C20`](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md)
2. **Equilibrio hidrostático** — [`B24-C04`](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md)
3. **Gradientes radiativos** — [`B24-C05`](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md)
4. **Transporte convectivo** — [`B37-C01`](../programa/clases/B37/B37-C01-conveccion-longitud-de-mezcla-y-criterios-de-schwarzschild-y-ledoux/CLASE.md)
5. **Ecuaciones de estado** — [`B37-C02`](../programa/clases/B37/B37-C02-ecuaciones-de-estado-estelares-gas-ideal-radiacion-y-degeneracion/CLASE.md)
6. **Generación de energía nuclear** — [`B24-C06`](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md), [`B24-C07`](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md), [`B24-C08`](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md)
7. **Opacidades estelares** — [`B37-C03`](../programa/clases/B37/B37-C03-opacidad-media-de-rosseland-y-tablas-de-opacidad-en-interiores/CLASE.md)
8. **Condiciones de frontera** — [`B37-C04`](../programa/clases/B37/B37-C04-condiciones-de-frontera-centrales-y-superficiales-en-modelos-estelares/CLASE.md)
9. **Códigos evolutivos estelares** — [`B37-C05`](../programa/clases/B37/B37-C05-codigos-de-evolucion-estelar-configuracion-verificacion-y-limites/CLASE.md)
10. **Calibración por observaciones** — [`B37-C06`](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md)

✅ **Checkpoint R01-M02.** Sin mirar el material, explica cómo se relacionan «Ecuaciones de estructura estelar», «Generación de energía nuclear» y «Calibración por observaciones», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R01-M03 · Evolución estelar avanzada

1. **Presecuencia principal** — [`B24-C01`](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md), [`B24-C02`](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md)
2. **Secuencia principal** — [`B24-C03`](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md), [`B24-C06`](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md), [`B24-C07`](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md)
3. **Subgigantes y gigantes** — [`B24-C15`](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md), [`B24-C16`](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md)
4. **Rama asintótica de gigantes** — [`B24-C21`](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md)
5. **Pérdida de masa** — [`B24-C17`](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md)
6. **Estrellas masivas** — [`B24-C17`](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md), [`B27-C15`](../programa/clases/B27/B27-C15-supernovas-de-colapso/CLASE.md)
7. **Binariedad y transferencia de masa** — [`B24-C22`](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md)
8. **Remanentes estelares** — [`B24-C18`](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md), [`B27-C02`](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md), [`B27-C03`](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md)
9. **Metallicidad y evolución** — [`B25-C17`](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md)
10. **Isocronas y edades** — [`B24-C19`](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md)

✅ **Checkpoint R01-M03.** Sin mirar el material, explica cómo se relacionan «Presecuencia principal», «Estrellas masivas» y «Isocronas y edades», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R01-M04 · Espectroscopía estelar avanzada

1. **Medición de perfiles de línea** — [`B32-C09`](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md)
2. **Resolución y dispersión espectral** — [`B45-C06`](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md), [`B45-C07`](../programa/clases/B45/B45-C07-resolucion-espectral/CLASE.md)
3. **Modelado de continua** — [`B32-C10`](../programa/clases/B32/B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md)
4. **Abundancias químicas** — [`B45-C14`](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md), [`B24-C10`](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md)
5. **Velocidades radiales** — [`B29-C03`](../programa/clases/B29/B29-C03-velocidad-radial-estelar/CLASE.md), [`B45-C12`](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md)
6. **Rotación y ensanchamiento** — [`B32-C11`](../programa/clases/B32/B32-C11-ensanchamiento-rotacional-y-v-sin-i/CLASE.md)
7. **Efecto Zeeman** — [`B32-C12`](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md)
8. **Calibraciones espectroscópicas** — [`B45-C08`](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md), [`B45-C09`](../programa/clases/B45/B45-C09-calibracion-de-respuesta-instrumental/CLASE.md)
9. **Espectros de alta resolución** — [`B45-C06`](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md), [`B45-C07`](../programa/clases/B45/B45-C07-resolucion-espectral/CLASE.md), [`B45-C18`](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md)
10. **Evaluación de incertidumbre química** — [`B45-C19`](../programa/clases/B45/B45-C19-reduccion-e-incertidumbre-instrumental/CLASE.md), [`B12-C16`](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md)

✅ **Checkpoint R01-M04.** Sin mirar el material, explica cómo se relacionan «Medición de perfiles de línea», «Rotación y ensanchamiento» y «Evaluación de incertidumbre química», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R01-M05 · Asterosismología

1. **Modos de oscilación** — [`B24-C14`](../programa/clases/B24/B24-C14-asterosismologia-inicial/CLASE.md)
2. **Oscilaciones radiales** — [`B37-C07`](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md)
3. **Oscilaciones no radiales** — [`B37-C08`](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md)
4. **Transformadas de series temporales** — [`B15-C05`](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md), [`B15-C06`](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md), [`B29-C19`](../programa/clases/B29/B29-C19-analisis-de-series-temporales-irregularmente-muestreadas/CLASE.md)
5. **Frecuencias características** — [`B37-C09`](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md)
6. **Inversión del interior estelar** — [`B37-C10`](../programa/clases/B37/B37-C10-inversion-asterosismica-de-perfiles-internos/CLASE.md)
7. **Rotación interna** — [`B37-C11`](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md)
8. **Gigantes rojas oscilantes** — [`B37-C12`](../programa/clases/B37/B37-C12-gigantes-rojas-oscilantes-y-modos-mixtos/CLASE.md)
9. **Datos de misiones fotométricas** — [`B37-C13`](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md)
10. **Ajuste de modelos sísmicos** — [`B37-C14`](../programa/clases/B37/B37-C14-ajuste-de-modelos-estelares-a-frecuencias-sismicas/CLASE.md)

✅ **Checkpoint R01-M05.** Sin mirar el material, explica cómo se relacionan «Modos de oscilación», «Inversión del interior estelar» y «Ajuste de modelos sísmicos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R01-M06 · Poblaciones estelares

1. **Diagramas color-magnitud** — [`B24-C03`](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md), [`B24-C19`](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md), [`B45-C02`](../programa/clases/B45/B45-C02-magnitudes-y-sistemas-de-filtros/CLASE.md)
2. **Funciones de luminosidad** — [`B38-C01`](../programa/clases/B38/B38-C01-funciones-de-luminosidad-estelar/CLASE.md)
3. **Funciones iniciales de masa** — [`B38-C02`](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md)
4. **Metallicidad poblacional** — [`B25-C17`](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md)
5. **Poblaciones de disco** — [`B25-C01`](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md), [`B25-C07`](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md)
6. **Poblaciones de halo** — [`B25-C01`](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md), [`B25-C07`](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md), [`B25-C15`](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md)
7. **Cúmulos globulares** — [`B25-C06`](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md), [`B24-C19`](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md)
8. **Cúmulos abiertos** — [`B25-C06`](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md), [`B24-C19`](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md)
9. **Cinemática estelar Gaia** — [`B38-C03`](../programa/clases/B38/B38-C03-cinematica-estelar-con-gaia-movimientos-propios-y-espacio-de-fase/CLASE.md)
10. **Reconstrucción de historia estelar** — [`B38-C04`](../programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/CLASE.md)

✅ **Checkpoint R01-M06.** Sin mirar el material, explica cómo se relacionan «Diagramas color-magnitud», «Poblaciones de halo» y «Reconstrucción de historia estelar», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R01-M07 · Simulación de galaxias

1. **Potenciales gravitatorios galácticos** — [`B38-C05`](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md)
2. **Distribuciones de masa** — [`B25-C08`](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md), [`B25-C15`](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md), [`B09-C20`](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md)
3. **Modelos de discos** — [`B25-C01`](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md), [`B25-C02`](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md)
4. **Halos de materia oscura** — [`B25-C15`](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md)
5. **Simulación de N cuerpos** — [`B73-C08`](../programa/clases/B73/B73-C08-sistemas-de-n-cuerpos/CLASE.md), [`B73-C09`](../programa/clases/B73/B73-C09-integracion-de-largo-plazo/CLASE.md)
6. **Simulación hidrodinámica** — [`B38-C06`](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md)
7. **Formación estelar submalla** — [`B38-C07`](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md)
8. **Interacciones de galaxias** — [`B25-C12`](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md)
9. **Postprocesamiento observacional** — [`B38-C08`](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md)
10. **Validación de galaxias simuladas** — [`B38-C09`](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md)

✅ **Checkpoint R01-M07.** Sin mirar el material, explica cómo se relacionan «Potenciales gravitatorios galácticos», «Simulación hidrodinámica» y «Validación de galaxias simuladas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R01-M08 · Investigación estelar y galáctica

1. **Preguntas de investigación** — [`B01-C06`](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md)
2. **Búsqueda sistemática bibliográfica** — [`B20-C01`](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md)
3. **Selección de catálogos** — [`B25-C19`](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md), [`B14-C05`](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md)
4. **Curación de datos** — [`B14-C08`](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md), [`B12-C19`](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md)
5. **Definición de hipótesis** — [`B01-C07`](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md), [`B12-C09`](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md)
6. **Diseño de análisis** — [`B20-C02`](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md)
7. **Estadística de resultados** — [`B12-C08`](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md), [`B12-C09`](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md), [`B12-C16`](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md)
8. **Reproducibilidad de código** — [`B14-C09`](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md), [`B14-C19`](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md), [`B124-C14`](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md)
9. **Revisión por pares** — [`B20-C03`](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md)
10. **Redacción de artículo científico** — [`B20-C04`](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md)

✅ **Checkpoint R01-M08.** Sin mirar el material, explica cómo se relacionan «Preguntas de investigación», «Diseño de análisis» y «Redacción de artículo científico», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Modelo y diagnóstico de un cúmulo estelar.** Construye un modelo simplificado de interior estelar para tres masas y confróntalo con datos públicos de un cúmulo: su edad se infiere del punto de desvío de la secuencia principal.

Entregables:

- Cuaderno reproducible con el modelo y sus supuestos
- Diagrama color-magnitud del cúmulo con isócronas superpuestas
- Estimación de edad y metalicidad con su incertidumbre
- Informe de dos páginas con límites del modelo

Criterios de evaluación:

- Cada cifra con unidad, fuente y versión de los datos
- La edad se justifica con al menos dos indicadores independientes
- El código se ejecuta desde cero sin editar rutas
- Se discuten explícitamente las degeneraciones edad-metalicidad-enrojecimiento

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes explicar y calcular la estructura y evolución de una estrella de masa dada, y decir dónde falla tu modelo.
- Puedes interpretar un espectro estelar y obtener temperatura, gravedad y abundancias con su incertidumbre.
- Puedes defender por escrito la edad de una población estelar con datos públicos.

<!-- /recorrido -->

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
2. Recorre la **física estelar** ([**B24** · Física y evolución de estrellas](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md)) y la **radiación y los espectros** ([**B32** · Atmósferas estelares y espectroscopía estelar cuantitativa](../programa/tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md)).
3. Aprende a **tratar datos con incertidumbre** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md), [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)) y a hacerlo de forma reproducible ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).
4. Elige una mirada (observación, modelado o simulación) y profundiza: [**B37** · Interiores estelares y asterosismología](../programa/tronco-comun/B37-interiores-estelares-y-asterosismologia.md) o [**B38** · Poblaciones estelares y simulación de galaxias](../programa/tronco-comun/B38-poblaciones-estelares-y-simulacion-de-galaxias.md).
5. Reúne tu **análisis reproducible** y guarda su historia.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Cosmología y astrofísica extrema](cosmologia-y-astrofisica-extrema.md) · [Heliofísica y climatología espacial](heliofisica-y-climatologia-espacial.md) · [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R01-astrofisica-estelar-y-galactica/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
