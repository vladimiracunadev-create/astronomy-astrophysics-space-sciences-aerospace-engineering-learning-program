# Estado verificable

**Fecha de verificación:** 5 de noviembre de 2026 · **Versión documental:** `0.1.0`

## Resumen

| Superficie | Estado actual | Evidencia |
|---|---:|---|
| Línea base `0.1.0`: registros del catálogo | 5.120 (1.280 de tronco + 3.840 de rutas), todos en E0 | `catalogo/clases.jsonl` |
| Línea base: IDs únicos | 5.120 | `herramientas/validar_catalogo.py` |
| Programa `0.2.0` (aprobado por el autor): áreas | 12 | `catalogo/v0.2.0/estructura.json` |
| Programa `0.2.0`: bloques | 133 (64 de la línea base + 69 nuevos) | `catalogo/v0.2.0/estructura.json` |
| Programa `0.2.0`: clases | 2.077 (1.280 de la línea base + 797 programadas) | `PROGRAMA_ACADEMICO_COMPLETO.md` |
| Módulos de ruta ubicados en áreas y bloques | 192 módulos, 1.920 temas: 1.101 en clases existentes y 819 en clases programadas | `catalogo/v0.2.0/colocacion/` |
| Rutas profesionales (recorridos sobre áreas y bloques) | 24 | `metadatos/recorridos/` |
| Clases en E0 | todas las del programa | catálogo |
| Clases con texto redactado (A01, B01–B08) | 160 de 160; B01-C01 aprobada por el autor, las otras 159 pendientes de aprobación; ninguna con revisión disciplinar | `programa/clases/` |
| Clases programadas (citadas, ubicadas, sin redactar) | 797 | `catalogo/v0.2.0/clases_programadas.jsonl` |
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
- ejercicios, soluciones, laboratorios o simulaciones de las clases aún no redactadas (las 160 de `programa/clases/` tienen ejercicios, soluciones y laboratorio o actividad, sin revisión externa; 144 de 146 scripts de laboratorio se ejecutaron sin error el 2026-11-05 en un equipo sin `astropy` (los otros 2 requieren esa biblioteca o comparan versiones declaradas); las fuentes enciclopédicas y divulgativas de B02, B04 y B08 se reemplazaron o se rotularon (quedan secundarias o divulgativas, por ejemplo en B02-C17, y una fuente académica pendiente sobre el calendario mapuche en B02-C01));
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
Catálogo: 5120 clases | 64 bloques | 24 rutas | 192 módulos   (línea base 0.1.0)
VALIDACIÓN DOCUMENTAL APROBADA (no implica clases desarrolladas).
```

Cada incremento futuro deberá actualizar este documento únicamente con hechos medidos. Los hitos históricos se registran en `CHANGELOG.md`; no se reescriben para aparentar un estado actual distinto.
