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

- **Ecuaciones diferenciales y simulación** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)); **métodos numéricos para EDP** ([**B69** · Métodos numéricos para EDP y fluidos computacionales](../PROGRAMA_ACADEMICO_COMPLETO.md#b69--métodos-numéricos-para-edp-y-fluidos-computacionales)).
- **Álgebra lineal** ([**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md)); **probabilidad y estadística** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)).
- **Inferencia bayesiana** ([**B67** · Inferencia bayesiana y computación probabilística](../PROGRAMA_ACADEMICO_COMPLETO.md#b67--inferencia-bayesiana-y-computación-probabilística)); **problemas inversos** ([**B70** · Problemas inversos y estimación de modelos](../PROGRAMA_ACADEMICO_COMPLETO.md#b70--problemas-inversos-y-estimación-de-modelos)).
- **Aprendizaje automático científico** ([**B65** · Aprendizaje automático científico](../PROGRAMA_ACADEMICO_COMPLETO.md#b65--aprendizaje-automático-científico)).
- **Computación de alto rendimiento** ([**B66** · Computación de alto rendimiento](../PROGRAMA_ACADEMICO_COMPLETO.md#b66--computación-de-alto-rendimiento)).
- **Verificación y validación** ([**B71** · Verificación y validación de software científico](../PROGRAMA_ACADEMICO_COMPLETO.md#b71--verificación-y-validación-de-software-científico)); **computación científica y ciencia abierta** ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).

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
7. 📚 [**B65** · Aprendizaje automático científico](../PROGRAMA_ACADEMICO_COMPLETO.md#b65--aprendizaje-automático-científico) — usa 9 de 12 clases: `B65-` C01–C09
8. 📚 [**B66** · Computación de alto rendimiento](../PROGRAMA_ACADEMICO_COMPLETO.md#b66--computación-de-alto-rendimiento) — usa 5 de 5 clases: `B66-` C01–C05
9. 📚 [**B67** · Inferencia bayesiana y computación probabilística](../PROGRAMA_ACADEMICO_COMPLETO.md#b67--inferencia-bayesiana-y-computación-probabilística) — usa 8 de 8 clases: `B67-` C01–C08
10. 📚 [**B69** · Métodos numéricos para EDP y fluidos computacionales](../PROGRAMA_ACADEMICO_COMPLETO.md#b69--métodos-numéricos-para-edp-y-fluidos-computacionales) — usa 4 de 5 clases: `B69-` C02–C05
11. 📚 [**B70** · Problemas inversos y estimación de modelos](../PROGRAMA_ACADEMICO_COMPLETO.md#b70--problemas-inversos-y-estimación-de-modelos) — usa 5 de 5 clases: `B70-` C01–C05
12. 📚 [**B71** · Verificación y validación de software científico](../PROGRAMA_ACADEMICO_COMPLETO.md#b71--verificación-y-validación-de-software-científico) — usa 8 de 8 clases: `B71-` C01–C08

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

13. 📚 [**B34** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B34-astrogeologia-y-geodesia-planetaria.md) — usa 1 de 30 clases: `B34-` C28

**A06 · Mecánica orbital, navegación y vuelo espacial**

14. 📚 [**B44** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B44-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 1 de 30 clases: `B44-` C01

**A11 · Economía, industria y gestión de proyectos espaciales**

15. 📚 [**B64** · Industria, economía, ética y proyectos espaciales](../programa/tronco-comun/B64-industria-economia-etica-y-proyectos-espaciales.md) — usa 2 de 24 clases: `B64-` C09, C14

<!-- /ruta -->

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
3. Profundiza en **métodos numéricos para EDP** ([**B69** · Métodos numéricos para EDP y fluidos computacionales](../PROGRAMA_ACADEMICO_COMPLETO.md#b69--métodos-numéricos-para-edp-y-fluidos-computacionales)) y **problemas inversos** ([**B70** · Problemas inversos y estimación de modelos](../PROGRAMA_ACADEMICO_COMPLETO.md#b70--problemas-inversos-y-estimación-de-modelos)).
4. Avanza a **inferencia bayesiana** ([**B67** · Inferencia bayesiana y computación probabilística](../PROGRAMA_ACADEMICO_COMPLETO.md#b67--inferencia-bayesiana-y-computación-probabilística)) y **aprendizaje automático científico** ([**B65** · Aprendizaje automático científico](../PROGRAMA_ACADEMICO_COMPLETO.md#b65--aprendizaje-automático-científico)).
5. Cierra con **cómputo de alto rendimiento** ([**B66** · Computación de alto rendimiento](../PROGRAMA_ACADEMICO_COMPLETO.md#b66--computación-de-alto-rendimiento)) y **verificación y validación** ([**B71** · Verificación y validación de software científico](../PROGRAMA_ACADEMICO_COMPLETO.md#b71--verificación-y-validación-de-software-científico)).

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md) · [Cosmología y astrofísica extrema](cosmologia-y-astrofisica-extrema.md) · [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R08-matematica-y-computacion-cientifica-espacial/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
