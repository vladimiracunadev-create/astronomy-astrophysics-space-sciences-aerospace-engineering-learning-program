# Registro de cambios

Todos los cambios relevantes de este programa se documentan aquí. Las referencias históricas se conservan; el estado actual se mantiene en `STATUS.md`.

> La versión de la publicación está en el archivo `VERSION` y en la etiqueta `vX.Y.Z` de GitHub. La carpeta `catalogo/estructura/` conserva su nombre histórico: contiene la estructura vigente (12 áreas, 133 bloques, 2.077 clases).

## [Sin publicar]

### Añadido

- **Talleres integradores de misión** (`talleres/`): diez talleres, uno por misión real, con la misma estructura de diez capítulos, laboratorio en Python y esquemas SVG generados con el mismo modelo. Misiones: Mars 2020 (T01), Artemis I (T02), New Horizons (T03), telescopio James Webb (T04), Cassini-Huygens (T05), Rosetta y Philae (T06), Parker Solar Probe (T07), OSIRIS-REx (T08), Crew Dragon Demo-2 (T09) y DART (T10). Estado E0; las cifras inciertas llevan ⚠.
- `herramientas/validar_talleres.py` (en la integración continua) y `talleres/_comun/` (utilidades y verificador de figuras).
- `documentacion/ESTANDAR_DE_TALLERES_DE_MISION.md` y la sección «Talleres integradores de misión» del README, antes de los anexos.
- Integración en el sitio (menú «Talleres», búsqueda), en los PDF (un volumen por taller y un bloque en el PDF general) y en la página de descargas.

## [0.1.1] — 2026-11-12 · diagramas dibujados

### Cambiado

- Los 2.211 diagramas Mermaid de las clases, las guías de bloque y los glosarios se dibujan como SVG vectorial en el sitio, las aplicaciones (Android y Windows) y los PDF; antes aparecían como texto. Los diagramas anchos de izquierda a derecha se dibujan de arriba abajo y con letra más grande para que se lean. Los `.md` no cambian: GitHub los sigue dibujando.
- README: nuevo orden (descripción, áreas y bloques, anexos, roles, descargas e índice de todos los documentos), lista completa de PDF en `documentacion/DESCARGAS_Y_PDF.md` y avisos redundantes retirados.
- Las etiquetas «línea base 0.1.0» pasan a «línea base inicial»: la única versión numerada es la de la publicación.

## [0.1.0] — 2026-11-11 · primera publicación

### Añadido

- Primera publicación: 37 PDF (general con anexos y glosarios, 12 por área y 24 por rol, con marcadores y numeración), aplicación sin conexión para Windows (ZIP portable) y Android (APK) con búsqueda, y `SHA256SUMS.txt`. Los archivos se adjuntan a la página de la versión, no al repositorio.
- Sitio de documentación y de lectura en GitHub Pages: navegación por árbol, índice de cada página, búsqueda, tema claro/oscuro, página de inicio con descargas y progreso local, y aplicación web instalable.
- `herramientas/publicacion/`: sitio, PDF por unidades y volúmenes, APK, lanzador de Windows y verificador de artefactos.
- Documentos nuevos en `documentacion/`: estándar para generar los contenidos, resolución por etapas, mapa del repositorio y mapa de áreas y bloques (antes ocupaban el README).
- 20 anexos históricos, pedagógicos y de cálculo (`anexos/`), glosarios (`glosario/`) y calculadora científica (`herramientas/calculadora_cientifica.py`).
- `.github/workflows/pages.yml` genera y publica el sitio completo (2.077 páginas de clase) en cada cambio de `main`.

### Cambiado

- README: las secciones «Estándar para generar los contenidos», «Resolución de contenidos por etapas» y «Qué contiene hoy» pasan a `documentacion/`; el resto de la portada conserva su estructura y se corrigen las incoherencias de datos (2.077 clases con texto en E0).
- Versión única: el programa tiene una sola versión, la `0.1.0` (archivo `VERSION`). La carpeta `catalogo/v0.2.0/` pasa a `catalogo/estructura/` y la estructura y la línea base dejan de llevar número de versión («estructura vigente» y «línea base inicial»).


## Reorganización del programa en áreas y bloques — 2026-11-05

### Cambiado

- Estructura unificada: todo el contenido vive en áreas y bloques. Los 192 módulos de las rutas se ubicaron en el tronco (1.920 temas: 1.101 en clases existentes y 819 en clases programadas).
- Programa de 12 áreas, 133 bloques y 2.077 clases (1.280 de la línea base y 797 programadas; al cierre de A12, las 797 tienen texto). `PROGRAMA_ACADEMICO_COMPLETO.md` y el README se reescribieron.
- Los bloques de la línea base B57–B64 pasan a las áreas A08 a A11 y todos los bloques se numeran de forma consecutiva (B01–B133) siguiendo el orden de las áreas, por autorización del autor (2026-11-05). El prefijo de bloque cambia en las clases (por ejemplo, B17-C01 pasa a ser B24-C01); la tabla anterior→nuevo está en `catalogo/estructura/numeracion_bloques.json`. Ninguna clase se borra; los IDs `Rxx-Mxx-Cnn` se conservan como equivalencias.
- Las rutas profesionales son recorridos sobre áreas y bloques (`metadatos/recorridos/`).

### Añadido

- `glosario/`: glosario alfabético generado de las clases (términos, siglas, símbolos y unidades, vocabulario por área) y `glosario/esencial/` con unas 145 entradas explicadas a fondo (intuición, fórmula, ejemplo numérico, error frecuente); generador `herramientas/generar_glosario.py`.
- `anexos/`: once anexos históricos y pedagógicos (agencias, misiones, científicos, astronautas, satélites, telescopios, lanzadores, cronología, escalas y fórmulas, estudios de caso, perfiles) y `herramientas/calculadora_cientifica.py` con autoprueba.
- 160 clases redactadas del área A01 (B01–B08), con fichas, ejercicios y laboratorios; pendientes de revisión disciplinar.
- 237 clases redactadas del área A02 (B09–B23), 160 de la línea base y 77 antes programadas, con fichas, ejercicios, laboratorios y guía de cada bloque; pendientes de revisión disciplinar.
- 272 clases redactadas del área A03 (B24–B40), 222 del área A04 (B41–B51) y 257 del área A05 (B52–B70), con fichas, ejercicios, laboratorios ejecutados y guía de cada bloque en formato de bloque; pendientes de revisión disciplinar. Con ellas hay 1.148 clases con texto (A01 a A05).
- 237 clases del área A06 (B71–B82), 259 de A07 (B83–B95), 105 de A08 (B96–B103), 153 de A09 (B104–B117), 85 de A10 (B118–B123), 44 de A11 (B124–B127) y 46 de A12 (B128–B133), con fichas, ejercicios, laboratorios ejecutados y guía de cada bloque; pendientes de revisión disciplinar. Con ellas las 2.077 clases del programa tienen texto (A01 a A12).
- `catalogo/estructura/` (colocación, estructura, clases programadas, equivalencias) y herramientas de validación y generación.

### Estado honesto

- Todas las clases del programa siguen en E0 en el catálogo; clases redactadas y verificadas: 0.

## Línea base inicial del catálogo — 2026-11-05

### Añadido

- Línea base de 5.120 registros: 1.280 clases transversales y 3.840 de especialización.
- 64 bloques, 24 rutas profesionales y 192 módulos con IDs permanentes.
- Catálogo sincronizado en JSONL, JSON y CSV, programa legible y visor estático.
- Validador de cantidad, unicidad, orden, estructura y estado preliminar.
- Estándar `clase-profunda-cientifica` de 22 funciones.
- Resolución editorial E0–E6 y niveles pedagógicos N0–N5.
- Documentación pública, estado verificable, roadmap y guía de contribución.
- Licenciamiento diferenciado: Apache-2.0 para software y CC BY-NC-SA 4.0 para contenido educativo original.
- Políticas separadas para datos, activos, terceros, marcas, uso comercial e historial de licencias.
- Guías profesionales de syllabus, carga, fuentes, verificación, dependencias, portafolio, seguridad, soporte y conducta.
- Mapas navegables en el README principal para las 8 áreas, 64 bloques, 1.280 clases transversales, 24 rutas y 192 módulos todavía en E0.
- Cierre visual del README con alcance, exclusiones, idea fuerza, licencias diferenciadas y firma del autor.

### Estado honesto

- Las 5.120 unidades permanecen en E0, con título y referencia preliminar.
- Clases completamente redactadas y verificadas: 0.
