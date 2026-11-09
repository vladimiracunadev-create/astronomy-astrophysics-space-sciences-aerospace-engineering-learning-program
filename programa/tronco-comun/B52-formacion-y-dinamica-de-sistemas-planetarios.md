# B52 — Formación y dinámica de sistemas planetarios

> **Bloque de la malla `0.2.0`.** Ver el [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md).

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial
**Área:** A05 — Ciencias planetarias, astroquímica y habitabilidad
**Nivel:** N3 (fundamentos disciplinares) · **Clases:** 20 · **Carga:** por calibrar con el uso
**Estado:** guía pedagógica del bloque (resumen de qué se aprende en cada clase). Las clases enlazadas en la tabla ya están redactadas; todas conservan el estado E0 en el catálogo hasta registrar revisión disciplinar.

## 🎯 Propósito del bloque

Enseña **cómo se forma un sistema planetario y cómo evoluciona su dinámica** con cálculos que se pueden comprobar: el colapso de la nebulosa y el disco que deja, el crecimiento del polvo hasta planetesimales y embriones, la captura de gas de los gigantes y la dispersión del disco, la migración y las resonancias, la arquitectura de los sistemas, los satélites y los anillos, los cuerpos remanentes (asteroides, Kuiper, Oort), el calor de las colisiones y la diferenciación, y por último la estabilidad a largo plazo y una simulación completa simplificada. Cada clase cierra con un laboratorio en Python que contrasta con un caso analítico, dos vías independientes o una simulación con semilla fija, y distingue lo consultado de lo ilustrativo y lo simulado de lo observado.

## 📚 Al terminar el bloque podrás

1. Decidir si una nube colapsa y qué radio centrífugo tendrá el disco, y describir un disco con perfiles de densidad, temperatura y espesor.
2. Seguir el crecimiento de sólidos: deriva radial, condición de colapso gravitacional, masa de aislamiento y captura de gas.
3. Calcular escalas de tiempo de migración y reconocer resonancias de movimiento medio con datos publicados.
4. Estimar la dispersión viscosa del disco y confrontarla con una solución de semejanza.
5. Situar satélites, anillos, asteroides, objetos del Kuiper y cometas de Oort con el radio de Hill, el límite de Roche y las resonancias.
6. Estimar el enfriamiento y el calentamiento radiactivo de un cuerpo y la energía que libera la diferenciación.
7. Integrar un sistema de N cuerpos con un esquema simpléctico, medir su estabilidad y armar una simulación de formación sencilla con comprobaciones de conservación.

## 🧭 Secuencia del bloque

```mermaid
flowchart LR
    A["C01-C05<br/>Del colapso a los embriones"]
    B["C06-C10<br/>Gas, migración y arquitectura"]
    C["C11-C16<br/>Satélites, anillos y remanentes"]
    D["C17-C20<br/>Calor, estabilidad y simulación"]
    A --> B --> C --> D
```

**Descripción textual.** Cuatro tramos encadenados: del colapso a los embriones (C01–C05), gas, migración y arquitectura (C06–C10), satélites, anillos y cuerpos remanentes (C11–C16) y calor, estabilidad y simulación (C17–C20).

## 🗂️ Las 20 clases en resumen

**Navegación:** cada clase desarrollada enlaza a la anterior, a la siguiente y a este bloque; mientras una clase siga solo programada, su enlace lleva a su fila en esta tabla.

La columna «Evidencia» indica el producto que demostrará el aprendizaje. Los laboratorios usan datos **sintéticos** o **ilustrativos** (rotulados) o valores publicados con fuente y fecha.

### Tramo 1 · Del colapso a los embriones

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b52-c01"></a>[B52-C01](../clases/B52/B52-C01-colapso-de-nebulosa-protosolar/CLASE.md) | Colapso de nebulosa protosolar | Masa de Jeans, tiempo de caída libre y radio centrífugo. | Ficha del colapso protosolar |
| <a id="b52-c02"></a>[B52-C02](../clases/B52/B52-C02-discos-protoplanetarios/CLASE.md) | Discos protoplanetarios | Perfiles de densidad superficial, temperatura y escala de altura, y estabilidad de Toomre. | Ficha del disco |
| <a id="b52-c03"></a>[B52-C03](../clases/B52/B52-C03-granulacion-de-polvo-y-acrecion/CLASE.md) | Granulación de polvo y acreción | Número de Stokes, deriva radial y crecimiento por colisiones. | Ficha de la deriva y el crecimiento del polvo |
| <a id="b52-c04"></a>[B52-C04](../clases/B52/B52-C04-formacion-de-planetesimales/CLASE.md) | Formación de planetesimales | Densidad crítica de Hill y masa de un cúmulo de partículas que colapsa. | Ficha del colapso de partículas |
| <a id="b52-c05"></a>[B52-C05](../clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md) | Crecimiento de embriones planetarios | Enfoque gravitacional, crecimiento descontrolado y masa de aislamiento. | Ficha del crecimiento de embriones |

### Tramo 2 · Gas, migración y arquitectura

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b52-c06"></a>[B52-C06](../clases/B52/B52-C06-migracion-de-planetas/CLASE.md) | Migración de planetas | Par de torsión, escala de tiempo de migración y evolución del semieje. | Ficha de la migración |
| <a id="b52-c07"></a>[B52-C07](../clases/B52/B52-C07-resonancias-orbitales/CLASE.md) | Resonancias orbitales | Resonancia de Laplace de los satélites galileanos con periodos de la NASA. | Ficha de la resonancia de Laplace |
| <a id="b52-c08"></a>[B52-C08](../clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md) | Formación de gigantes gaseosos | Masa térmica, radios de Bondi y de Hill y límite de captura de gas. | Ficha de la captura de gas |
| <a id="b52-c09"></a>[B52-C09](../clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md) | Dispersión de discos de gas | Evolución viscosa del disco frente a la solución de semejanza. | Ficha de la dispersión del disco |
| <a id="b52-c10"></a>[B52-C10](../clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md) | Arquitecturas de sistemas exoplanetarios | Espaciado en radios de Hill mutuos y razones de periodos. | Ficha de la arquitectura de un sistema |

### Tramo 3 · Satélites, anillos y cuerpos remanentes

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b52-c11"></a>[B52-C11](../clases/B52/B52-C11-formacion-de-satelites-naturales/CLASE.md) | Formación de satélites naturales | Esfera de Hill y ubicación de los satélites galileanos. | Ficha de los satélites en la esfera de Hill |
| <a id="b52-c12"></a>[B52-C12](../clases/B52/B52-C12-anillos-planetarios/CLASE.md) | Anillos planetarios | Límite de Roche con un modelo de dos esferas. | Ficha del límite de Roche |
| <a id="b52-c13"></a>[B52-C13](../clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md) | Pequeños cuerpos remanentes | Distribución de tamaños en ley de potencias y su estimación. | Ficha de la distribución de tamaños |
| <a id="b52-c14"></a>[B52-C14](../clases/B52/B52-C14-cinturones-de-asteroides/CLASE.md) | Cinturones de asteroides | Lagunas de Kirkwood como resonancias con Júpiter. | Ficha de las lagunas de Kirkwood |
| <a id="b52-c15"></a>[B52-C15](../clases/B52/B52-C15-cinturon-de-kuiper/CLASE.md) | Cinturón de Kuiper | Resonancias con Neptuno y temperatura de equilibrio a 40 ua. | Ficha del cinturón de Kuiper |
| <a id="b52-c16"></a>[B52-C16](../clases/B52/B52-C16-nube-de-oort/CLASE.md) | Nube de Oort | Energía de ligadura, periodo y perturbación por el paso de una estrella. | Ficha de las perturbaciones de la nube de Oort |

### Tramo 4 · Calor, estabilidad y simulación

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b52-c17"></a>[B52-C17](../clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md) | Colisiones y evolución térmica | Calentamiento por impacto y enfriamiento por conducción de una esfera. | Ficha del enfriamiento de un cuerpo |
| <a id="b52-c18"></a>[B52-C18](../clases/B52/B52-C18-diferenciacion-planetaria/CLASE.md) | Diferenciación planetaria | Calentamiento por decaimiento radiactivo y energía gravitatoria de la diferenciación. | Ficha del calor y la energía de diferenciación |
| <a id="b52-c19"></a>[B52-C19](../clases/B52/B52-C19-estabilidad-a-largo-plazo-de-sistemas/CLASE.md) | Estabilidad a largo plazo de sistemas | Integración simpléctica, conservación y sensibilidad a las condiciones iniciales. | Ficha de la estabilidad de un sistema |
| <a id="b52-c20"></a>[B52-C20](../clases/B52/B52-C20-simulacion-de-formacion-planetaria-simplificada/CLASE.md) | Simulación de formación planetaria simplificada | Fusión de embriones con comprobaciones de masa, momento angular y energía. | Ficha de la simulación de formación |

## 🧵 Hilos que atraviesan el bloque

- **Escalas de tiempo:** caída libre (C01), deriva (C03), migración (C06), viscosa (C09), conductiva (C17) y de Lyapunov (C19) se comparan siempre con la vida del disco de gas.
- **Radio de Hill:** C04, C05, C08, C10, C11 y C19 reutilizan la misma esfera de influencia, cada vez con otra pregunta.
- **Resonancias:** C06, C07, C14 y C15 sitúan el semieje donde el cociente de periodos es racional.
- **Observado frente a simulado:** los datos del Sistema Solar proceden de fichas de la NASA con fecha; los discos, los sistemas y las simulaciones son sintéticos o ilustrativos y se rotulan.
- **Conservación:** C19 y C20 comprueban energía, momento angular y masa antes de interpretar nada.

## 📝 Evaluación del bloque (propuesta, por calibrar)

- Fichas y ejercicios por clase, con retroalimentación y recuperación con evidencia distinta.
- Portafolio: ficha de la dispersión del disco (C09) y ficha de la simulación de formación (C20).
- Las condiciones críticas (rotular lo sintético e ilustrativo, no presentar lo simulado como observado y citar solo lo consultado) no se compensan con promedio.

## ⚠️ Seguridad y límites

El bloque es educativo. Los modelos son simplificados (discos de ley de potencias, coeficientes ilustrativos, integraciones cortas) y no sustituyen a los códigos de formación planetaria ni a la literatura primaria; no se predice la evolución de ningún sistema real. Los valores del Sistema Solar proceden de fichas de la NASA consultadas el 2026-11-09 y los demás parámetros se rotulan como ilustrativos.

## 📖 Fuentes consultadas en el bloque (resumen)

Fecha de consulta: 2026-11-09. Las constantes proceden de NIST (CODATA 2022, listado completo) y de la IAU 2015 (Resolución B3, texto del PDF extraído con PyMuPDF). Los periodos de los satélites galileanos y los datos de los planetas son de las fichas de la NASA/NSSDC. De los artículos citados (Kley y Nelson 2012; Morbidelli y Raymond 2016; Youdin y Goodman 2005; Chiang y Youdin 2010; Lambrechts y Johansen 2012; Nesvorný 2018; Vokrouhlický, Nesvorný y Dones 2019) solo se leyó el resumen, a través de la página de arXiv; de Laskar y Gastineau (2009), Crida y Charnoz (2012) y Gladman y Volk (2021) solo se consultó una descripción obtenida con un buscador, sin el texto. Los perfiles de disco, los coeficientes de migración, las leyes de colisión y las abundancias radiactivas son ilustrativos y **no se consultaron**. Cada clase detalla en su sección 11 qué respalda cada fuente.

## Roles que lo usan

- [Ciencias planetarias y astrogeología](../../rutas/ciencias-planetarias-y-astrogeologia.md)

## Fuentes de orientación preliminar

- **[NASA-PDS]** [NASA Planetary Data System](https://pds.nasa.gov/) — Archivo de datos de misiones y ciencias planetarias.
- **[USGS]** [USGS Astrogeology Science Center](https://www.usgs.gov/centers/astrogeology-science-center) — Cartografía, geología y sistemas de referencia de superficies planetarias.
- **[COSPAR]** [Committee on Space Research](https://cosparhq.cnes.fr/) — Protección planetaria y cooperación en investigación espacial.
- **[NASA-EO]** [NASA Earthdata](https://www.earthdata.nasa.gov/) — Datos abiertos de observación de la Tierra.

> La asociación de estas fuentes es orientativa por bloque. Las fuentes realmente consultadas para cada afirmación se registran en la sección 11 de cada clase.

[🏠 Volver al programa](../../README.md) · [➡️ B53 — Astrogeología y geodesia planetaria](./B53-astrogeologia-y-geodesia-planetaria.md)
