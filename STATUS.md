# Estado verificable

**Fecha de verificación:** 11 de noviembre de 2026 · **Publicación:** `0.1.2`

## Resumen

| Superficie | Estado actual | Evidencia |
|---|---:|---|
| Línea base inicial: registros del catálogo | 5.120 (1.280 de tronco + 3.840 de rutas), todos en E0 | `catalogo/clases.jsonl` |
| Línea base: IDs únicos | 5.120 | `herramientas/validar_catalogo.py` |
| Programa vigente (aprobado por el autor): áreas | 12 | `catalogo/estructura/estructura.json` |
| Programa vigente: bloques | 133 (64 de la línea base + 69 nuevos) | `catalogo/estructura/estructura.json` |
| Programa vigente: clases | 2.077 (1.280 de la línea base + 797 programadas) | `PROGRAMA_ACADEMICO_COMPLETO.md` |
| Módulos de ruta ubicados en áreas y bloques | 192 módulos, 1.920 temas: 1.101 en clases existentes y 819 en clases programadas | `catalogo/estructura/colocacion/` |
| Rutas profesionales (recorridos sobre áreas y bloques) | 24 con sus 192 módulos ubicados en áreas y bloques; 12 con recorrido por fases heredado (R12, R14 a R24) y 12 pendientes (R01 a R11 y R13) | `catalogo/estructura/colocacion/`, `metadatos/recorridos/` |
| Clases en E0 | todas las del programa | catálogo |
| Clases con texto redactado (A01, B01–B08) | 160 de 160; B01-C01 aprobada por el autor, las otras 159 pendientes de aprobación; ninguna con revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A02, B09–B23) | 237 de 237 (160 de la línea base y 77 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A03, B24–B40) | 272 de 272 (160 de la línea base y 112 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A04, B41–B51) | 222 de 222 (160 de la línea base y 62 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A05, B52–B70) | 257 de 257 (160 de la línea base y 97 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A06, B71–B82) | 237 de 237 (160 de la línea base y 77 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A07, B83–B95) | 259 de 259 (160 de la línea base y 99 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A08, B96–B103) | 105 de 105 (40 de la línea base y 65 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A09, B104–B117) | 153 de 153 (60 de la línea base y 93 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A10, B118–B123) | 85 de 85 (40 de la línea base y 45 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A11, B124–B127) | 44 de 44 (20 de la línea base y 24 antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (A12, B128–B133) | 46 de 46 (todas antes programadas); todas pendientes de aprobación y de revisión disciplinar | `programa/clases/` |
| Clases con texto redactado (total) | 2.077 de 2.077 (1.280 de la línea base y 797 antes programadas); ninguna con revisión disciplinar | `programa/clases/` |
| Talleres de misión | 10 de 10 redactados (T01 a T10), con laboratorio en Python, figuras SVG y diez capítulos cada uno; todos en E0, con datos de referencia pública marcados ⚠ para contrastar con la fuente | `talleres/`, `herramientas/validar_talleres.py` |
| Publicación `v0.1.2` | 47 PDF verificados (general, 12 áreas, 24 roles y 10 talleres), con los diagramas dibujados; APK de Android y ZIP portable de Windows; contenido en E0 | `herramientas/publicacion/verificar.py` |
| Clases programadas (citadas y ubicadas) | 797: las 797 ya tienen texto | `catalogo/estructura/clases_programadas.jsonl` | `catalogo/estructura/clases_programadas.jsonl` |
| Clases completamente redactadas y verificadas | **0** | catálogo y metadatos |
| Régimen de software | Apache-2.0 | `LICENSE` |
| Régimen de contenido original | CC BY-NC-SA 4.0 | `LICENSE-CONTENT.md` |

## Qué está validado

- cantidades y unicidad de IDs;
- sincronía de IDs y orden entre JSON, JSONL y CSV;
- 20 registros por bloque y por módulo;
- existencia de 64 índices de bloque, 192 índices de módulo y 24 índices de ruta;
- presencia de título, descripción preliminar y tres referencias iniciales por registro;
- conservación del estado preliminar de las 5.120 unidades de la línea base;
- que cada uno de los 1.920 temas de los módulos de ruta tenga una ubicación en áreas y bloques (`herramientas/validar_colocacion.py`).
- presencia de una matriz diferenciada para software, contenido, datos, activos, terceros y marcas.

## Qué no está validado

- exactitud científica de las futuras clases;
- lectura completa, vigencia o conformidad de las fuentes preliminares;
- prerrequisitos clase por clase;
- ejercicios, soluciones, laboratorios o simulaciones con revisión externa (las 2.077 de A01 a A12 en `programa/clases/` tienen ejercicios, soluciones y laboratorio o actividad, sin revisión externa; los laboratorios de A02 a A12 se ejecutaron según los informes de sus sesiones de redacción y no se ha repetido esa ejecución de forma independiente; 144 de 146 scripts de laboratorio de A01 y A02 se ejecutaron sin error el 2026-11-05 en un equipo sin `astropy` (los otros 2 requieren esa biblioteca o comparan versiones declaradas); las fuentes enciclopédicas y divulgativas de B02, B04 y B08 se reemplazaron o se rotularon (quedan secundarias o divulgativas, por ejemplo en B02-C17, y una fuente académica pendiente sobre el calendario mapuche en B02-C01));
- fuentes primarias en todas las clases: algunas citan páginas de Wikipedia como fuente (B45 en parte, B46 y B50 de A04) y quedan pendientes de reemplazar por fuentes primarias; lo no consultado está rotulado «no consultado» en cada clase;
- accesibilidad de contenidos todavía inexistentes;
- equivalencias de horas, créditos, títulos o certificaciones;
- revisión disciplinar externa o pilotaje con estudiantes;
- la pertinencia pedagógica de la ubicación de cada tema en áreas y bloques y de las 797 clases programadas.

## Reproducción

```bash
python herramientas/validar_catalogo.py
```

Resultado de la línea base:

```text
Catálogo: 5120 clases | 64 bloques | 24 rutas | 192 módulos   (línea base inicial)
VALIDACIÓN DOCUMENTAL APROBADA (no implica clases desarrolladas).
```

Cada incremento futuro deberá actualizar este documento únicamente con hechos medidos. Los hitos históricos se registran en `CHANGELOG.md`; no se reescriben para aparentar un estado actual distinto.
