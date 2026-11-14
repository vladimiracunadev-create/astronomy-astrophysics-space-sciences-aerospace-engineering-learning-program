---
name: consultar-el-programa
description: Localiza en el programa de este repositorio (2 077 clases, 133 bloques, 12 áreas) qué clases y bloques responden una pregunta y las cita con su ruta. Úselo siempre que haga falta fundamentar una respuesta con el programa, o cuando el usuario pregunte «dónde se estudia X».
---

# Consultar el programa

1. Reduzca la pregunta a 1–3 términos (con y sin acento; sinónimos).
2. Ejecute `python herramientas/consulta_programa.py tema "<término>" -n 12` (títulos) y, si hay pocos resultados, repita con `--texto` (contenido de las clases).
3. Para un bloque: `python herramientas/consulta_programa.py bloque B75`; para un área: `area A06`; todas las áreas: `areas`.
4. Abra con Read las 1–3 clases más pertinentes (`programa/clases/Bxx/.../CLASE.md`) y la guía del bloque (`programa/tronco-comun/Bxx-*.md`).
5. Responda con el resultado y cite las rutas. Recuerde que las clases están **pendientes de revisión**: no las llame verificadas; las cifras sin fuente pública se marcan con ⚠.
