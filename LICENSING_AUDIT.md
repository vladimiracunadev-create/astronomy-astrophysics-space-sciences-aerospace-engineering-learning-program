# Auditoría de licenciamiento

**Corte:** 5 de noviembre de 2026

**Alcance:** archivos versionados del programa; no es dictamen jurídico.

## Resultado

| Control | Estado | Evidencia |
|---|---|---|
| licencia de software explícita | conforme | `LICENSE` · Apache-2.0 canónica |
| licencia educativa explícita | conforme | `LICENSE-CONTENT.md` · CC BY-NC-SA 4.0 |
| reglas de datos y catálogos | conforme | `DATA_LICENSES.md` |
| inventario y política de activos | conforme | `ASSET_LICENSES.md` |
| avisos de herramientas y fuentes externas | conforme | `THIRD_PARTY_NOTICES.md` |
| separación de marcas | conforme | `TRADEMARKS.md` |
| resolución de archivos mixtos | conforme | `documentacion/LICENSING_MATRIX.md` |
| historia no retroactiva | conforme | `documentacion/LICENSING_HISTORY.md` |
| permiso comercial diferenciado | documentado | `documentacion/COMMERCIAL_USE.md` |

## Inventario actual

- 5.120 registros curriculares preliminares de la línea base y su reorganización en el programa `0.2.0`, cuya selección, estructura y redacción original quedan bajo la licencia de contenido.
- 25 referencias institucionales preliminares, enlazadas pero no relicenciadas.
- 832 relaciones preliminares de trazabilidad, que no prueban verificación de las fuentes.
- ningún activo visual, audiovisual, tipográfico o 3D externo redistribuido en la revisión auditada.
- Python y cinco GitHub Actions utilizados como herramientas o automatizaciones externas.

## Controles permanentes

Cada aporte debe acreditar derecho de contribución. Todo dataset o activo nuevo requiere inventario individual. Cada dependencia nueva exige registrar nombre, versión o referencia, licencia y uso. Las revisiones de fuentes no pueden convertir una referencia en evidencia verificada sin localizador y evaluación de alcance.

## Pendientes aceptados

El catálogo aún no tiene fuentes verificadas clase por clase porque ninguna clase ha avanzado más allá de E0. Esa condición es editorial, no una falla de la política de licencias, y debe mantenerse visible hasta completar E2 para cada unidad.
