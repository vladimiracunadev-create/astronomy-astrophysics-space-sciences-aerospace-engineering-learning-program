# 🌌 Astrodinámica interplanetaria

> Diseñas trayectorias para llegar a otros cuerpos del sistema solar: transferencias, asistencias gravitatorias y ventanas de lanzamiento, con optimización y análisis de robustez.
>
> **Nivel de entrada:** matemática, física y programación de nivel universitario; rol técnico de diseño de misión · **Foco:** mecánica orbital, problema de Lambert, transferencias, asistencias gravitatorias, optimización de trayectorias, robustez · **Entrega:** un diseño de trayectoria reproducible, con su presupuesto de velocidad, sus ventanas y su análisis de sensibilidad

## 🧭 Qué es y por qué importa

Llegar a Marte, a Júpiter o a un asteroide exige elegir una trayectoria entre infinitas posibles. El diseñador busca la que cumple las restricciones de la misión con el **menor costo de propulsante, tiempo o riesgo**, y que además resista errores reales de lanzamiento y de navegación.

El oficio combina mecánica orbital con optimización numérica. Las trayectorias interplanetarias se construyen por tramos: se resuelven transferencias entre dos puntos, se encadenan con encuentros planetarios que aportan velocidad gratis y se refinan con un optimizador hasta cumplir todas las restricciones.

Las miradas del rol son:

- **Mecánica de transferencias.** Lambert, cónicas empalmadas, asistencias. Su pregunta es: *¿qué trayectoria base conecta origen y destino?*
- **Optimización.** Trayectorias de bajo empuje o impulsivas, restricciones. Su pregunta es: *¿cuál es el mejor diseño y cuán sensible es?*
- **Robustez.** Errores de ejecución y de navegación. Su pregunta es: *¿sigue funcionando si las cosas salen mal?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es navegación a bordo.** Esa estima el estado real del vehículo ([Navegación guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md)); tú diseñas la trayectoria nominal.
- **No es propulsión.** Usas las capacidades del motor como restricción; diseñarlo es otro rol ([Ingeniería de lanzadores y propulsión](ingenieria-de-lanzadores-y-propulsion.md)).
- **No es solo teoría orbital.** Exige optimización numérica y software.
- **No es «copiar la trayectoria de una misión anterior».** Cada misión cambia fechas, masas y restricciones.

## 🗓️ Un día en el puesto

- **Diseño preliminar:** calculas transferencias candidatas y comparas su costo.
- **Optimización:** refinas una trayectoria con un optimizador y verificas restricciones.
- **Ventanas:** exploras fechas de lanzamiento y arribo.
- **Robustez:** simulas errores y evalúas la corrección necesaria.
- **Documentación:** dejas el diseño reproducible para el equipo.

Dicho sin adornos: **un buen diseño se reconoce porque se sabe dónde falla**.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Mecánica orbital** ([**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md)); **perturbaciones** ([**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md)); **mecánica celeste y caos** ([**B73** · Mecánica celeste, resonancias y caos](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md)).
- **Estimación de órbitas** ([**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md)).
- **Trayectorias y misiones interplanetarias** ([**B75** · Trayectorias y misiones interplanetarias](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md)); **problema de Lambert** ([**B82** · Problema de Lambert y transferencias de dos puntos](../programa/tronco-comun/B82-problema-de-lambert-y-transferencias-de-dos-puntos.md)).
- **Optimización de trayectorias y diseño robusto** ([**B81** · Optimización de trayectorias y diseño robusto](../programa/tronco-comun/B81-optimizacion-de-trayectorias-y-diseno-robusto.md)).
- **Dinámica cislunar** ([**B76** · Dinámica cislunar y operaciones de proximidad](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md)).
- **Simulación numérica** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)).

### Herramientas del oficio

```text
Cálculo:              Python científico y propagadores orbitales
Optimización:         optimizadores no lineales con restricciones
Efemérides:           datos de posición de los cuerpos del sistema solar
Pruebas:              casos conocidos para verificar el código
Documentación:        registro de versión de datos, modelos y parámetros
```

Un optimizador devuelve una solución aunque el problema esté mal planteado. Verifica con casos conocidos antes de confiar.

### Habilidades no técnicas

- **Pensar en restricciones reales.**
- **Comunicación con ingeniería de sistemas y con operaciones.**
- **Documentación clara de supuestos.**
- **Paciencia con la convergencia.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
2. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases

### 🎯 El núcleo del rol

**A01 · Alfabetización científica, astronómica y tecnológica**

1. 📚 [**B07** · Informática científica desde cero](../programa/tronco-comun/B07-informatica-cientifica-desde-cero.md) — usa 1 de 20 clases: `B07-` C17

**A02 · Matemática, física computacional y métodos científicos**

2. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — usa 1 de 20 clases: `B09-` C07
3. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — usa 1 de 20 clases: `B10-` C16
4. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — usa 3 de 26 clases: `B11-` C08, C17, C19
5. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 1 de 26 clases: `B12-` C16
6. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 2 de 23 clases: `B13-` C08, C11
7. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 1 de 31 clases: `B14-` C10

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

8. 📚 [**B53** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md) — usa 1 de 30 clases: `B53-` C03

**A06 · Mecánica orbital, navegación y vuelo espacial**

9. 📚 [**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md) — usa 4 de 20 clases: `B71-` C09, C18–C20
10. 📚 [**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md) — usa 8 de 21 clases: `B72-` C02, C06, C08–C10, C18–C20
11. 📚 [**B73** · Mecánica celeste, resonancias y caos](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md) — usa 6 de 22 clases: `B73-` C08, C10–C12, C21–C22
12. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 8 de 30 clases: `B74-` C07, C11–C12, C15, C19–C22
13. 📚 [**B75** · Trayectorias y misiones interplanetarias](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md) — usa 26 de 30 clases: `B75-` C01–C14, C17–C18, C21–C30
14. 📚 [**B76** · Dinámica cislunar y operaciones de proximidad](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md) — usa 1 de 20 clases: `B76-` C18
15. 📚 [**B77** · Dinámica de lanzamiento y reentrada](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md) — usa 1 de 25 clases: `B77-` C11
16. 📚 [**B81** · Optimización de trayectorias y diseño robusto](../programa/tronco-comun/B81-optimizacion-de-trayectorias-y-diseno-robusto.md) — usa 15 de 15 clases: `B81-` C01–C15
17. 📚 [**B82** · Problema de Lambert y transferencias de dos puntos](../programa/tronco-comun/B82-problema-de-lambert-y-transferencias-de-dos-puntos.md) — usa 7 de 7 clases: `B82-` C01–C07

**A07 · Ingeniería y construcción de sistemas espaciales**

18. 📚 [**B86** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) — usa 1 de 23 clases: `B86-` C04
19. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 1 de 25 clases: `B89-` C14

**A08 · Operaciones de misión y robótica espacial**

20. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 1 de 30 clases: `B96-` C11

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes calcular una transferencia de Hohmann y su delta-v?
- ¿Sabes qué es el parámetro gravitacional y la energía orbital?
- ¿Resuelves la ecuación de Kepler numéricamente?
- ¿Manejas vectores y cambios de sistema de referencia?

#### R09-M01 · Transferencias orbitales avanzadas

1. **Transferencia de Hohmann generalizada** — [`B71-C18`](../programa/clases/B71/B71-C18-maniobra-de-hohmann/CLASE.md), [`B75-C01`](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md)
2. **Transferencias bi-elípticas** — [`B75-C05`](../programa/clases/B75/B75-C05-transferencias-bi-elipticas/CLASE.md)
3. **Transferencias no coplanares** — [`B75-C13`](../programa/clases/B75/B75-C13-cambios-de-plano-interplanetarios/CLASE.md)
4. **Maniobras con delta-v limitado** — [`B75-C09`](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md), [`B75-C10`](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md)
5. **Transferencias con cambios de plano** — [`B71-C19`](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md), [`B75-C13`](../programa/clases/B75/B75-C13-cambios-de-plano-interplanetarios/CLASE.md)
6. **Intersección de cónicas** — [`B75-C21`](../programa/clases/B75/B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md)
7. **Modelos de primer impulso** — [`B75-C22`](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md)
8. **Métricas de energía C3** — [`B75-C23`](../programa/clases/B75/B75-C23-energia-caracteristica-c3-y-exceso-hiperbolico/CLASE.md)
9. **Sensibilidad a ventana** — [`B75-C03`](../programa/clases/B75/B75-C03-ventanas-de-lanzamiento/CLASE.md)
10. **Comparación de soluciones óptimas** — [`B75-C12`](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md)

✅ **Checkpoint R09-M01.** Sin mirar el material, explica cómo se relacionan «Transferencia de Hohmann generalizada», «Intersección de cónicas» y «Comparación de soluciones óptimas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R09-M02 · Problemas de Lambert

1. **Definición de Lambert** — [`B75-C04`](../programa/clases/B75/B75-C04-ecuacion-de-lambert/CLASE.md)
2. **Transferencias de arco corto** — [`B82-C01`](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md)
3. **Transferencias de arco largo** — [`B82-C02`](../programa/clases/B82/B82-C02-lambert-de-arco-largo/CLASE.md)
4. **Solución universal** — [`B82-C03`](../programa/clases/B82/B82-C03-formulacion-de-variables-universales/CLASE.md)
5. **Solución multirrevolución** — [`B82-C04`](../programa/clases/B82/B82-C04-lambert-multirrevolucion/CLASE.md)
6. **Tratamiento de singularidades** — [`B82-C05`](../programa/clases/B82/B82-C05-singularidades-del-problema-de-lambert/CLASE.md)
7. **Métodos iterativos** — [`B82-C06`](../programa/clases/B82/B82-C06-algoritmos-iterativos-para-lambert-gooding-izzo/CLASE.md)
8. **Sensibilidad temporal** — [`B72-C19`](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md)
9. **Validación por integración** — [`B72-C18`](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md), [`B71-C20`](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md)
10. **Benchmark entre métodos** — [`B82-C07`](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md)

✅ **Checkpoint R09-M02.** Sin mirar el material, explica cómo se relacionan «Definición de Lambert», «Tratamiento de singularidades» y «Benchmark entre métodos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R09-M03 · Dinámica interplanetaria de N cuerpos

1. **Efemérides de N cuerpos** — [`B73-C08`](../programa/clases/B73/B73-C08-sistemas-de-n-cuerpos/CLASE.md)
2. **Campos gravitatorios planetarios** — [`B72-C02`](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md), [`B53-C03`](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md)
3. **Perturbaciones de terceros cuerpos** — [`B72-C09`](../programa/clases/B72/B72-C09-perturbaciones-solares/CLASE.md), [`B72-C10`](../programa/clases/B72/B72-C10-perturbaciones-lunares/CLASE.md)
4. **Perturbación no gravitacional** — [`B72-C06`](../programa/clases/B72/B72-C06-arrastre-atmosferico/CLASE.md), [`B72-C08`](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md)
5. **Integración adaptativa** — [`B11-C08`](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md), [`B72-C18`](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md)
6. **Paso cercano de satélites** — [`B73-C21`](../programa/clases/B73/B73-C21-pasos-cercanos-a-satelites-naturales-en-integracion-de-n-cuerpos/CLASE.md)
7. **Capturas temporales** — [`B73-C22`](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md)
8. **Dinámica de resonancias** — [`B73-C10`](../programa/clases/B73/B73-C10-resonancias-de-movimiento-medio/CLASE.md), [`B73-C11`](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md), [`B73-C12`](../programa/clases/B73/B73-C12-captura-y-escape-resonante/CLASE.md)
9. **Covarianza en N cuerpos** — [`B74-C11`](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md), [`B74-C12`](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md)
10. **Pruebas frente a SPICE** — [`B74-C20`](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md)

✅ **Checkpoint R09-M03.** Sin mirar el material, explica cómo se relacionan «Efemérides de N cuerpos», «Paso cercano de satélites» y «Pruebas frente a SPICE», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R09-M04 · Asistencias gravitacionales múltiples

1. **Geometría de sobrevuelo** — [`B75-C07`](../programa/clases/B75/B75-C07-sobrevuelos-planetarios/CLASE.md)
2. **Parámetro de impacto B-plane** — [`B75-C24`](../programa/clases/B75/B75-C24-plano-b-y-parametro-de-impacto/CLASE.md)
3. **Ángulo de deflexión** — [`B75-C07`](../programa/clases/B75/B75-C07-sobrevuelos-planetarios/CLASE.md), [`B71-C09`](../programa/clases/B71/B71-C09-orbitas-parabolicas-e-hiperbolicas/CLASE.md)
4. **Cambio de energía heliocéntrica** — [`B75-C06`](../programa/clases/B75/B75-C06-asistencias-gravitacionales/CLASE.md)
5. **Resonancias para sobrevuelos** — [`B75-C25`](../programa/clases/B75/B75-C25-resonancias-para-sobrevuelos/CLASE.md)
6. **Encadenamiento de asistencias** — [`B75-C08`](../programa/clases/B75/B75-C08-secuencias-multiples-de-sobrevuelos/CLASE.md)
7. **Sobrevuelos de lunas** — [`B75-C26`](../programa/clases/B75/B75-C26-sobrevuelos-de-lunas-y-tours-de-sistemas-planetarios/CLASE.md)
8. **Restricciones de iluminación** — [`B75-C17`](../programa/clases/B75/B75-C17-oportunidades-cientificas-de-sobrevuelo/CLASE.md), [`B76-C18`](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md)
9. **Optimización de secuencias** — [`B75-C12`](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md)
10. **Márgenes de maniobra** — [`B75-C09`](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md), [`B75-C18`](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md)

✅ **Checkpoint R09-M04.** Sin mirar el material, explica cómo se relacionan «Geometría de sobrevuelo», «Encadenamiento de asistencias» y «Márgenes de maniobra», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R09-M05 · Trayectorias de bajo empuje

1. **Propulsión de bajo empuje** — [`B75-C11`](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md)
2. **Ecuaciones variacionales** — [`B81-C01`](../programa/clases/B81/B81-C01-ecuaciones-variacionales-y-matriz-de-transicion-de-estados/CLASE.md)
3. **Método de disparo** — [`B81-C02`](../programa/clases/B81/B81-C02-metodo-de-disparo-para-control-optimo/CLASE.md)
4. **Métodos directos** — [`B81-C03`](../programa/clases/B81/B81-C03-metodos-directos-de-transcripcion/CLASE.md)
5. **Trayectorias de espirales** — [`B81-C04`](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md)
6. **Optimización de empuje** — [`B75-C12`](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md)
7. **Limitaciones de energía** — [`B81-C05`](../programa/clases/B81/B81-C05-limitaciones-de-potencia-en-propulsion-electrica/CLASE.md)
8. **Restricciones de orientación** — [`B81-C06`](../programa/clases/B81/B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md)
9. **Modelos de aceleración** — [`B81-C07`](../programa/clases/B81/B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md)
10. **Validación de trayectoria continua** — [`B81-C08`](../programa/clases/B81/B81-C08-validacion-de-trayectorias-de-empuje-continuo/CLASE.md)

✅ **Checkpoint R09-M05.** Sin mirar el material, explica cómo se relacionan «Propulsión de bajo empuje», «Optimización de empuje» y «Validación de trayectoria continua», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R09-M06 · Ventanas y oportunidades de misión

1. **Geometría de ventanas** — [`B75-C03`](../programa/clases/B75/B75-C03-ventanas-de-lanzamiento/CLASE.md)
2. **Fases heliocéntricas** — [`B75-C02`](../programa/clases/B75/B75-C02-angulos-de-fase-planetaria/CLASE.md)
3. **Sincronía de lanzamiento** — [`B77-C11`](../programa/clases/B77/B77-C11-ventanas-de-lanzamiento-dinamica-de-lanzamiento-y-reentrada/CLASE.md)
4. **Duración de misión** — [`B75-C27`](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md)
5. **Restricciones de eclipses** — [`B86-C04`](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md), [`B96-C11`](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md)
6. **Operaciones de destino** — [`B75-C14`](../programa/clases/B75/B75-C14-captura-en-destino/CLASE.md)
7. **Disponibilidad de seguimiento** — [`B74-C15`](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md), [`B89-C14`](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md)
8. **Restricciones de radiación** — [`B75-C28`](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md)
9. **Análisis de calendario** — [`B75-C29`](../programa/clases/B75/B75-C29-analisis-de-calendario-con-graficos-pork-chop/CLASE.md)
10. **Trade-offs tiempo y combustible** — [`B75-C09`](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md), [`B75-C12`](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md)

✅ **Checkpoint R09-M06.** Sin mirar el material, explica cómo se relacionan «Geometría de ventanas», «Operaciones de destino» y «Trade-offs tiempo y combustible», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R09-M07 · Optimización e incertidumbre orbital

1. **Variables de diseño orbital** — [`B81-C09`](../programa/clases/B81/B81-C09-variables-de-diseno-orbital/CLASE.md)
2. **Funciones objetivo** — [`B81-C10`](../programa/clases/B81/B81-C10-funciones-objetivo-de-diseno-de-trayectorias/CLASE.md)
3. **Optimización multicriterio** — [`B81-C11`](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md)
4. **Restricciones dinámicas** — [`B81-C12`](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md)
5. **Métodos de gradiente** — [`B11-C17`](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md), [`B09-C07`](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md)
6. **Optimización heurística** — [`B81-C13`](../programa/clases/B81/B81-C13-optimizacion-heuristica-algoritmos-geneticos-y-enjambres/CLASE.md)
7. **Dispersiones iniciales** — [`B75-C18`](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md)
8. **Propagación de incertidumbres** — [`B74-C12`](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md), [`B12-C16`](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md)
9. **Presupuestos de corrección** — [`B81-C14`](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md)
10. **Robustez ante fallas** — [`B81-C15`](../programa/clases/B81/B81-C15-robustez-de-trayectoria-ante-fallas/CLASE.md)

✅ **Checkpoint R09-M07.** Sin mirar el material, explica cómo se relacionan «Variables de diseño orbital», «Optimización heurística» y «Robustez ante fallas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R09-M08 · Verificación de trayectorias interplanetarias

1. **Modelos keplerianos de control** — [`B71-C20`](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md)
2. **Horizons como referencia** — [`B74-C20`](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md)
3. **Kernels SPICE** — [`B74-C21`](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md)
4. **Marcos y escalas temporales** — [`B13-C08`](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md), [`B13-C11`](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md), [`B10-C16`](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md)
5. **Comparación de integradores** — [`B72-C20`](../programa/clases/B72/B72-C20-comparacion-de-propagadores-de-fidelidad-distinta/CLASE.md), [`B11-C19`](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md)
6. **Verificación de residuales** — [`B74-C07`](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md), [`B74-C20`](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md)
7. **Validación de maniobras** — [`B75-C30`](../programa/clases/B75/B75-C30-validacion-de-maniobras-por-reintegracion/CLASE.md)
8. **Métricas de error** — [`B74-C19`](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md)
9. **Automatización de pruebas** — [`B14-C10`](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md), [`B07-C17`](../programa/clases/B07/B07-C17-pruebas-de-funciones-matematicas/CLASE.md)
10. **Informe de navegación verificable** — [`B74-C22`](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md)

✅ **Checkpoint R09-M08.** Sin mirar el material, explica cómo se relacionan «Modelos keplerianos de control», «Verificación de residuales» y «Informe de navegación verificable», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Diseño de una trayectoria interplanetaria con asistencias.** Diseña una trayectoria a un planeta exterior con al menos una asistencia gravitatoria, elige la ventana y verifica el resultado con un método independiente.

Entregables:

- Mapa de ventanas con C3 y tiempos de vuelo
- Secuencia de asistencias con geometría de cada sobrevuelo
- Presupuesto de delta-v con correcciones y márgenes
- Verificación cruzada con otro método o herramienta

Criterios de evaluación:

- Las fechas están en UTC y el sistema de referencia declarado
- El presupuesto incluye correcciones de trayectoria
- La verificación independiente coincide dentro de la tolerancia
- Se analiza la sensibilidad a errores de navegación

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes diseñar y verificar una trayectoria interplanetaria preliminar con asistencias.
- Puedes justificar una ventana de lanzamiento y su plan B.
- Puedes cuantificar la incertidumbre de una trayectoria.

<!-- /recorrido -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **diseño de trayectoria documentado**:

- una misión de ejemplo con sus restricciones;
- una trayectoria base y su refinamiento optimizado;
- un presupuesto de velocidad y una exploración de ventanas;
- un análisis de sensibilidad frente a errores;
- el código y las efemérides para repetirlo.

Los bloques de la ruta aportan ejercicios y laboratorios; guarda la primera versión y sus cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada, y para esta guía no se consultó una fuente externa específica (2026-11-05). Por eso no se citan normas, requisitos de acceso ni cifras: cuando se necesiten, deben consultarse en la fuente oficial vigente de la institución, agencia o empresa correspondiente.

## 📈 Progresión del rol

Rutas habituales: **analista de misión o de trayectorias → responsable del diseño de trayectoria de una misión → liderazgo de análisis de misión**. Se abren la dinámica de vuelo y la navegación. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Navegación guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md), [Ingeniería de lanzadores y propulsión](ingenieria-de-lanzadores-y-propulsion.md) y [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md).

## ⚠️ Mitos y errores comunes

- **«La trayectoria más corta es la mejor».** Suele no serlo en costo ni en riesgo.
- **«La asistencia gravitatoria es gratis».** Cuesta tiempo y restricciones de geometría.
- **«Una solución del optimizador es la óptima».** Puede ser un óptimo local.
- **«Una vez diseñada, no cambia».** Se rediseña cuando cambian masas y fechas.
- **«Es solo matemática».** Es matemática al servicio de restricciones de ingeniería.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la matemática de tu diagnóstico.
2. Estudia **mecánica orbital** ([**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md)) y **perturbaciones** ([**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md)).
3. Avanza a **trayectorias interplanetarias** ([**B75** · Trayectorias y misiones interplanetarias](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md)) y al **problema de Lambert** ([**B82** · Problema de Lambert y transferencias de dos puntos](../programa/tronco-comun/B82-problema-de-lambert-y-transferencias-de-dos-puntos.md)).
4. Profundiza en **optimización y robustez** ([**B81** · Optimización de trayectorias y diseño robusto](../programa/tronco-comun/B81-optimizacion-de-trayectorias-y-diseno-robusto.md)).
5. Reúne tu **diseño documentado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Navegación guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md) · [Ingeniería de lanzadores y propulsión](ingenieria-de-lanzadores-y-propulsion.md) · [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R09-astrodinamica-interplanetaria/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
