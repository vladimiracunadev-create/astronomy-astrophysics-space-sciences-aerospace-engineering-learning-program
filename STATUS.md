# Estado verificable

**Fecha de verificación:** 5 de noviembre de 2026 · **Versión documental:** `0.1.0`

## Resumen

| Superficie | Estado actual | Evidencia |
|---|---:|---|
| Registros del catálogo | 5.120 | `catalogo/clases.jsonl` |
| IDs únicos | 5.120 | `herramientas/validar_catalogo.py` |
| Bloques transversales | 64 | `programa/tronco-comun/` |
| Clases transversales | 1.280 | catálogo |
| Rutas profesionales | 24 | `programa/rutas-profesionales/` |
| Módulos especializados | 192 | catálogo e índices de módulo |
| Clases especializadas | 3.840 | catálogo |
| Clases en E0 · catalogada | 5.120 | campo `estado=solo_titulo_y_referencia_preliminar` |
| Clases en E1–E6 | 0 | catálogo |
| Clases completamente redactadas y verificadas | **0** | catálogo y metadatos |
| Clases con texto redactado (área A01, bloques B01 a B08) | 160 de 160 de A01 (1.280 del tronco común: 160 redactadas); B01-C01 aprobada por el autor; las otras 159 pendientes de aprobación; ninguna con revisión disciplinar | `programa/clases/` |
| Régimen de software | Apache-2.0 | `LICENSE` |
| Régimen de contenido original | CC BY-NC-SA 4.0 | `LICENSE-CONTENT.md` |

## Qué está validado

- cantidades y unicidad de IDs;
- sincronía de IDs y orden entre JSON, JSONL y CSV;
- 20 registros por bloque y por módulo;
- existencia de 64 índices de bloque, 192 índices de módulo y 24 índices de ruta;
- presencia de título, descripción preliminar y tres referencias iniciales por registro;
- conservación del estado preliminar de las 5.120 unidades.
- presencia de una matriz diferenciada para software, contenido, datos, activos, terceros y marcas.

## Qué no está validado

- exactitud científica de las futuras clases;
- lectura completa, vigencia o conformidad de las fuentes preliminares;
- prerrequisitos clase por clase;
- ejercicios, soluciones, laboratorios o simulaciones de las clases aún no redactadas (las 160 de `programa/clases/` tienen ejercicios, soluciones y laboratorio o actividad, sin revisión externa; 144 de 146 scripts de laboratorio se ejecutaron sin error el 2026-11-05 en un equipo sin `astropy` (los otros 2 requieren esa biblioteca o comparan versiones declaradas); las fuentes enciclopédicas y divulgativas de B02, B04 y B08 se reemplazaron o se rotularon (quedan secundarias o divulgativas, por ejemplo en B02-C17, y una fuente académica pendiente sobre el calendario mapuche en B02-C01));
- accesibilidad de contenidos todavía inexistentes;
- equivalencias de horas, créditos, títulos o certificaciones;
- revisión disciplinar externa o pilotaje con estudiantes.

## Reproducción

```bash
python herramientas/validar_catalogo.py
```

Resultado de la línea base:

```text
Catálogo: 5120 clases | 64 bloques | 24 rutas | 192 módulos
VALIDACIÓN DOCUMENTAL APROBADA (no implica clases desarrolladas).
```

Cada incremento futuro deberá actualizar este documento únicamente con hechos medidos. Los hitos históricos se registran en `CHANGELOG.md`; no se reescriben para aparentar un estado actual distinto.
