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

- **Estimación de órbitas y navegación** ([**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md)); **navegación inercial y fusión multisensorial** ([**B80** · Navegación inercial y fusión multisensorial](../PROGRAMA_ACADEMICO_COMPLETO.md#b80--navegación-inercial-y-fusión-multisensorial)).
- **Sistemas dinámicos y control** ([**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md)); **sensores y control de actitud** ([**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md)).
- **Autonomía y teleoperación** ([**B98** · Autonomía y teleoperación espacial](../PROGRAMA_ACADEMICO_COMPLETO.md#b98--autonomía-y-teleoperación-espacial)); **localización y mapeo** ([**B99** · Localización y mapeo robótico](../PROGRAMA_ACADEMICO_COMPLETO.md#b99--localización-y-mapeo-robótico)).
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
14. 📚 [**B80** · Navegación inercial y fusión multisensorial](../PROGRAMA_ACADEMICO_COMPLETO.md#b80--navegación-inercial-y-fusión-multisensorial) — usa 8 de 9 clases: `B80-` C01–C08

**A07 · Ingeniería y construcción de sistemas espaciales**

15. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 1 de 24 clases: `B83-` C17
16. 📚 [**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md) — usa 10 de 22 clases: `B87-` C03–C09, C15, C19, C21
17. 📚 [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md) — usa 5 de 44 clases: `B88-` C05, C11–C12, C14, C16
18. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 1 de 25 clases: `B89-` C15
19. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 1 de 24 clases: `B90-` C16

**A08 · Operaciones de misión y robótica espacial**

20. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 6 de 30 clases: `B96-` C03, C05, C07–C08, C13, C15
21. 📚 [**B97** · Robótica y construcción extraterrestre](../programa/tronco-comun/B97-robotica-y-construccion-extraterrestre.md) — usa 3 de 27 clases: `B97-` C07, C16–C17
22. 📚 [**B98** · Autonomía y teleoperación espacial](../PROGRAMA_ACADEMICO_COMPLETO.md#b98--autonomía-y-teleoperación-espacial) — usa 2 de 8 clases: `B98-` C01–C02

**A10 · Entorno orbital, derecho y seguridad espacial**

23. 📚 [**B118** · Tráfico espacial y sostenibilidad orbital](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md) — usa 1 de 24 clases: `B118-` C07

<!-- /ruta -->

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
3. Profundiza en **navegación inercial y fusión** ([**B80** · Navegación inercial y fusión multisensorial](../PROGRAMA_ACADEMICO_COMPLETO.md#b80--navegación-inercial-y-fusión-multisensorial)) y **sensores y actitud** ([**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md)).
4. Avanza a **autonomía** ([**B98** · Autonomía y teleoperación espacial](../PROGRAMA_ACADEMICO_COMPLETO.md#b98--autonomía-y-teleoperación-espacial)) y **localización y mapeo** ([**B99** · Localización y mapeo robótico](../PROGRAMA_ACADEMICO_COMPLETO.md#b99--localización-y-mapeo-robótico)).
5. Reúne tu **estimador verificado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrodinámica interplanetaria](astrodinamica-interplanetaria.md) · [Robótica espacial y sistemas autónomos](robotica-espacial-y-sistemas-autonomos.md) · [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R10-navegacion-guiado-y-autonomia-espacial/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
