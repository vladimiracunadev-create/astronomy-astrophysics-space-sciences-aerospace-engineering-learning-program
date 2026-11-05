# Reglas para agentes de desarrollo

- Este repositorio se llama `astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program` y su nombre académico formal aparece en `README.md`; no usar siglas para renombrarlo.
- Es UN programa independiente, no 24 programas independientes.
- `catalogo/clases.jsonl` es el catálogo legible por máquinas, sincronizado con `catalogo/clases.csv` y `catalogo/clases.json`.
- `catalogo/clases.*` es la línea base `0.1.0` (5.120 registros) y no se edita. La estructura vigente del programa es la `0.2.0` (`catalogo/v0.2.0/` y `PROGRAMA_ACADEMICO_COMPLETO.md`): todo el contenido vive en áreas y bloques, las rutas son recorridos y los módulos `Rxx-Mxx` se conservan como equivalencias.
- Salvo las 160 clases de A01 (con texto redactado y pendientes de revisión), ninguna clase está redactada, impartida o verificada: no marcarlas como tales. Las clases programadas se citan con su necesidad y no se redactan sin orden expresa del autor.
- La reorganización `0.2.0` fue autorizada por el autor (2026-11-05): reubica los bloques B57–B64 en otras áreas y programa clases nuevas, pero no borra ni renumera ningún ID.
- No borrar ni renumerar IDs existentes. Cambios aditivos y con auditoría de dependencia.
- Antes de cambios, leer el estándar de clase y correr `python herramientas/validar_catalogo.py`.
- No reproducir documentación protegida completa. Fuentes iniciales son orientativas, no pruebas de conformidad.
- Cualquier fórmula o simulación futura debe señalar unidades, sistema de referencia, datos, versiones y tolerancias.
- No modificar proyectos ajenos. Integrar con ellos mediante manifiestos/metadatos.
- Mantener estructura pedagógica, accesibilidad y controles de calidad.
