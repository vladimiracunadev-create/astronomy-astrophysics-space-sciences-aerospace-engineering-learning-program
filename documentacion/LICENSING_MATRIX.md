# Matriz de licenciamiento

**Revisión:** 5 de noviembre de 2026.

| Ruta o tipo | Código | Contenido original | Datos o terceros | Tratamiento |
|---|---|---|---|---|
| `herramientas/*.py` | Apache-2.0 | no aplica | Python conserva su licencia | mantener aviso SPDX |
| `.github/workflows/*.yml` | Apache-2.0 | no aplica | cada Action conserva MIT | mantener aviso SPDX y versiones |
| `visor/index.html` | Apache-2.0 | CC BY-NC-SA 4.0 | catálogo embebido conserva su régimen | separar lógica, interfaz y datos al reutilizar |
| `README.md`, `documentacion/*.md`, `STATUS.md`, `ROADMAP.md` | fragmentos funcionales separables: Apache-2.0 | CC BY-NC-SA 4.0 | citas y enlaces excluidos | atribuir contenido; no relicenciar citas |
| `PROGRAMA_ACADEMICO_COMPLETO.md`, fichas y mapas curriculares | no aplica | CC BY-NC-SA 4.0 | referencias externas excluidas | reconocer selección y estructura original |
| `catalogo/*` | formato y herramientas: Apache-2.0 | selección, títulos y redacción: CC BY-NC-SA 4.0 | hechos y localizadores no se relicencian | aplicar reglas por campo de `DATA_LICENSES.md` |
| `metadatos/*` | esquemas funcionales separables: Apache-2.0 | taxonomía y redacción: CC BY-NC-SA 4.0 | nombres, URLs y obras externas conservan derechos | registrar procedencia |
| `MANIFIESTO_SHA256.txt` | salida técnica redistribuible | no concede derechos sobre archivos listados | no aplica | acompañar al conjunto, no usar como licencia |
| futuros activos | según código incorporado | CC BY-NC-SA 4.0 si son originales | licencia individual si son externos | inventariar antes de publicar |

## Archivos mixtos

Una licencia no absorbe automáticamente a la otra. En un archivo mixto se separan, en la medida razonable, lógica ejecutable, expresión educativa, datos y componentes externos. Si la separación no es clara, debe documentarse antes de redistribuir o adaptar.

## Precedencia

Un aviso específico y válido incluido junto a un componente prevalece para ese componente. Los textos legales de Apache-2.0 y CC BY-NC-SA 4.0 prevalecen sobre los resúmenes de este repositorio.
