# Reglas para agentes de desarrollo

- Este repositorio se llama `astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program` y su nombre académico formal aparece en `README.md`; no usar siglas para renombrarlo.
- Es UN programa independiente, no 24 programas independientes.
- `catalogo/clases.jsonl` es el catálogo legible por máquinas, sincronizado con `catalogo/clases.csv` y `catalogo/clases.json`.
- `catalogo/clases.*` es la línea base `0.1.0` (5.120 registros) y no se edita. La estructura vigente del programa es la `0.2.0` (`catalogo/v0.2.0/` y `PROGRAMA_ACADEMICO_COMPLETO.md`): todo el contenido vive en áreas y bloques, las rutas son recorridos y los módulos `Rxx-Mxx` se conservan como equivalencias.
- Las 2.077 clases del programa (A01 a A12) tienen texto redactado y están pendientes de revisión; ninguna está impartida, revisada ni verificada: no marcarlas como tales. Las clases programadas se citan con su necesidad y no se redactan sin orden expresa del autor.
- La reorganización `0.2.0` fue autorizada por el autor (2026-11-05): reubica bloques en otras áreas, programa clases nuevas y numera los bloques de forma consecutiva (B01–B133, en orden de área; `catalogo/v0.2.0/numeracion_bloques.json` guarda el ID anterior de cada uno). Autorizó el cambio del prefijo de bloque en `catalogo/clases.*` (cada clase conserva su número `Cnn`); no se borró ninguna clase.
- Desde la `0.2.0` la numeración de bloques es consecutiva y no se vuelve a cambiar sin orden expresa del autor. No borrar IDs; cambios aditivos y con auditoría de dependencia.
- Antes de cambios, leer el estándar de clase y correr `python herramientas/validar_catalogo.py`.
- No reproducir documentación protegida completa. Fuentes iniciales son orientativas, no pruebas de conformidad.
- Cualquier fórmula o simulación futura debe señalar unidades, sistema de referencia, datos, versiones y tolerancias.
- No modificar proyectos ajenos. Integrar con ellos mediante manifiestos/metadatos.
- Mantener estructura pedagógica, accesibilidad y controles de calidad.
