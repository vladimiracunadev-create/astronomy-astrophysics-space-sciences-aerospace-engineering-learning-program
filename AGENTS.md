# Reglas para agentes de desarrollo

- Este repositorio se llama `astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program` y su nombre académico formal aparece en `README.md`; no usar siglas para renombrarlo.
- Es UN programa independiente, no 24 programas independientes.
- `catalogo/clases.jsonl` es el catálogo legible por máquinas, sincronizado con `catalogo/clases.csv` y `catalogo/clases.json`.
- Los 5.120 registros están solo descritos por título y referencia preliminar: no marcar clases como redactadas, impartidas o verificadas.
- No borrar ni renumerar IDs existentes. Cambios aditivos y con auditoría de dependencia.
- Antes de cambios, leer el estándar de clase y correr `python herramientas/validar_catalogo.py`.
- No reproducir documentación protegida completa. Fuentes iniciales son orientativas, no pruebas de conformidad.
- Cualquier fórmula o simulación futura debe señalar unidades, sistema de referencia, datos, versiones y tolerancias.
- No modificar proyectos ajenos. Integrar con ellos mediante manifiestos/metadatos.
- Mantener estructura pedagógica, accesibilidad y controles de calidad.
