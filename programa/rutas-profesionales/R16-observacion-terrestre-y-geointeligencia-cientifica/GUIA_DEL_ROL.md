# R16 — Guía del rol: analista de observación terrestre y geointeligencia científica

> Esta guía describe el rol para quien decide si es para sí. No es un temario ni una promesa de empleo, habilitación o título. El orden de clases está en [RECORRIDO.md](RECORRIDO.md).

## Qué es

Es la persona que transforma lo que miden los satélites que miran la Tierra (imagen óptica, térmica, radar, altimetría) en **información que alguien puede usar**: un mapa de deformación del terreno, una serie de cambio de cobertura, una alerta de inundación, un modelo de elevación. Su trabajo es la cadena completa entre el sensor y el usuario: calibrar, corregir la atmósfera y la geometría, clasificar o medir, validar con datos de referencia y publicar con metadatos y una incertidumbre honesta.

«Geointeligencia científica» aquí significa **análisis geoespacial con método científico** (reproducible, con incertidumbre y fuentes), no inteligencia de seguridad ni vigilancia de personas.

## Qué NO es (y con qué se confunde)

- **No es ciencia planetaria** ([R05](../R05-ciencias-planetarias-y-astrogeologia/INDICE.md)): usa técnicas parecidas (cartografía, altimetría) sobre la Tierra y con verificación en terreno posible.
- **No es heliofísica ni clima espacial** ([R07](../R07-heliofisica-y-climatologia-espacial/INDICE.md)), aunque «clima» aparezca en los dos nombres.
- **No es ingeniería de satélites** ([R12](../R12-ingenieria-y-construccion-de-satelites-y-cubesats/INDICE.md)): consume el instrumento y especifica qué necesita; no integra el satélite.
- **No es vigilancia espacial ni defensa** ([R22](../R22-seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales/INDICE.md)): no analiza objetos orbitales ni opera con fines militares.
- **No es un rol de desarrollo de software puro**: programa, pero cada cifra debe tener sentido físico y una cota de error.

## Un día de trabajo

Se parte de una pregunta del usuario («¿se hundió esta ladera?», «¿cuánta superficie se quemó?»). Se elige el sensor y la fecha según resolución y nubes; se descarga y se comprueba el nivel de procesado; se corrige o se verifica la corrección atmosférica y radiométrica; se genera el producto (índice, interferograma, clasificación); se compara con datos de referencia y se estima el error; se escribe un informe que diga qué se puede concluir y qué no. Parte del día son tareas de datos: catálogos, formatos, versiones, reproducibilidad.

## Qué decide y qué entrega

**Decide:** qué sensor, qué corrección y qué método responden la pregunta, y cuándo el resultado no es suficientemente fiable como para decidir algo con él.

**Entrega:** productos con metadatos y trazabilidad, informes de calidad y de incertidumbre, mapas reproducibles, catálogos y servicios de datos, y propuestas técnicas de servicio.

## Conocimientos y herramientas

- Resoluciones espacial, espectral, radiométrica y temporal, y sus compromisos.
- Radiometría y calibración; corrección atmosférica; índices espectrales.
- Radar de apertura sintética e interferometría; altimetría y LiDAR.
- Estadística aplicada: muestreo, incertidumbre, validación y falsos positivos.
- Coordenadas, proyecciones, formatos geoespaciales, catálogos y servicios estándar.
- Programación y entornos reproducibles. Los programas y bibliotecas concretos son una decisión del equipo; el recorrido no recomienda marcas.

## Qué dicen las fuentes consultadas

La divulgación de datos de observación de la Tierra de NASA Earthdata (consultada el 2026-11-05; el sitio indica actualización el 3 de noviembre de 2026) distingue sensores activos, que emiten su propia energía, de pasivos, que detectan la que emite o refleja el entorno, y enumera cuatro resoluciones (radiométrica, espacial, espectral y temporal); la página no define las resoluciones radiométrica y espectral, de modo que el recorrido las apoya en B57-C02 y C03. El Comité de Satélites de Observación de la Tierra (CEOS), en su página de datos listos para análisis (consultada el 2026-11-05), define esos productos como datos satelitales procesados con un conjunto mínimo de requisitos para facilitar el análisis, y lista familias como reflectancia de superficie, temperatura de superficie, reflectancia acuática, luz nocturna y radar combinado, cada una con su versión de especificación.

Fuentes:

- NASA Earthdata, «Earth Observation Data Basics», <https://www.earthdata.nasa.gov/learn/backgrounders/remote-sensing> — consultado 2026-11-05.
- CEOS, «Analysis Ready Data», <https://ceos.org/ard/> — consultado 2026-11-05.

No se citan salarios, cifras de empleo ni certificaciones: no se verificaron.

## Evidencias y portafolio

Un mapa multiespectral reproducible (código, datos, versiones, unidades y proyección declaradas) con matriz de error; un interferograma con su evaluación de coherencia y una lectura prudente del desplazamiento; un modelo de elevación validado con puntos de control; un informe de calidad radiométrica; un catálogo de escenas con metadatos; y un caso de desastre analizado con su tasa de falsos positivos.

## Progresión

Se empieza ejecutando cadenas de procesado y validando productos; después se diseñan métodos y se asumen incertidumbres; finalmente se especifican servicios o instrumentos. Los niveles y requisitos dependen de cada organización.

## Límites éticos y de seguridad

- La resolución espacial puede revelar a personas y propiedades: privacidad, consentimiento y uso dual se consideran antes de publicar; el recorrido no autoriza vigilancia.
- Las alertas de desastre afectan a comunidades: un falso positivo o negativo tiene costo; se comunica la incertidumbre y se deriva la decisión a las autoridades competentes.
- Un modelo entrenado en una región no se traslada a otra sin validarlo.
- Se respetan licencias de datos y se citan las fuentes.
