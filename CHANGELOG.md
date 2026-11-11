# Registro de cambios

Todos los cambios relevantes de este programa se documentan aquí. Las referencias históricas se conservan; el estado actual se mantiene en `STATUS.md`.

## [0.2.0] — 2026-11-05

### Cambiado

- Estructura unificada: todo el contenido vive en áreas y bloques. Los 192 módulos de las rutas se ubicaron en el tronco (1.920 temas: 1.101 en clases existentes y 819 en clases programadas).
- Programa de 12 áreas, 133 bloques y 2.077 clases (1.280 de la línea base y 797 programadas; al cierre de A12, las 797 tienen texto). `PROGRAMA_ACADEMICO_COMPLETO.md` y el README se reescribieron.
- Los bloques de la línea base B57–B64 pasan a las áreas A08 a A11 y todos los bloques se numeran de forma consecutiva (B01–B133) siguiendo el orden de las áreas, por autorización del autor (2026-11-05). El prefijo de bloque cambia en las clases (por ejemplo, B17-C01 pasa a ser B24-C01); la tabla anterior→nuevo está en `catalogo/v0.2.0/numeracion_bloques.json`. Ninguna clase se borra; los IDs `Rxx-Mxx-Cnn` se conservan como equivalencias.
- Las rutas profesionales son recorridos sobre áreas y bloques (`metadatos/recorridos/`).

### Añadido

- 160 clases redactadas del área A01 (B01–B08), con fichas, ejercicios y laboratorios; pendientes de revisión disciplinar.
- 237 clases redactadas del área A02 (B09–B23), 160 de la línea base y 77 antes programadas, con fichas, ejercicios, laboratorios y guía de cada bloque; pendientes de revisión disciplinar.
- 272 clases redactadas del área A03 (B24–B40), 222 del área A04 (B41–B51) y 257 del área A05 (B52–B70), con fichas, ejercicios, laboratorios ejecutados y guía de cada bloque en formato de bloque; pendientes de revisión disciplinar. Con ellas hay 1.148 clases con texto (A01 a A05).
- 237 clases del área A06 (B71–B82), 259 de A07 (B83–B95), 105 de A08 (B96–B103), 153 de A09 (B104–B117), 85 de A10 (B118–B123), 44 de A11 (B124–B127) y 46 de A12 (B128–B133), con fichas, ejercicios, laboratorios ejecutados y guía de cada bloque; pendientes de revisión disciplinar. Con ellas las 2.077 clases del programa tienen texto (A01 a A12).
- `catalogo/v0.2.0/` (colocación, estructura, clases programadas, equivalencias) y herramientas de validación y generación.

### Estado honesto

- Todas las clases del programa siguen en E0 en el catálogo; clases redactadas y verificadas: 0.

## [0.1.0] — 2026-11-05

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
