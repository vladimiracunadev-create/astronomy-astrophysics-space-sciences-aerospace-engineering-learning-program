# Ampliación del tronco común

El tronco común de la línea base `0.1.0` tiene 8 áreas, 64 bloques y 1.280 clases. Los [recorridos por rol](GUIA_DE_RECORRIDOS_POR_ROL.md) muestran que no bastan: cada rol necesita temas que el tronco no cubre o cubre solo con un título. Este documento fija cómo se amplía **sin romper nada**.

## Principios

1. **La línea base no se toca.** Los 5.120 IDs, sus títulos y su significado siguen igual. Las 160 clases del área A01 (B01 a B08), que son el conocimiento básico, se conservan íntegras.
2. **La ampliación es aditiva y versionada.** Se registra aparte, con una versión (`0.2.0` y siguientes) y una matriz de compatibilidad, según los [convenios de identificación](CONVENIOS_DE_IDENTIFICACION_Y_AMPLIACION.md).
3. **La demanda sale de los roles.** Cada hueco registrado en `metadatos/recorridos.json` es una necesidad documentada. Los huecos de los 24 roles se consolidan antes de crear unidades.
4. **Una unidad nueva debe ganarse su lugar.** Solo se añade si no puede resolverse profundizando o conectando una existente.
5. **Las áreas crecen, no se renumeran.** El área es un atributo, no parte del ID: las clases y bloques nuevos declaran a qué área pertenecen.

## Cómo se identifican las unidades nuevas

| Qué se añade | ID | Ejemplo |
|---|---|---|
| Bloque nuevo | continúa la numeración: `B65`, `B66`, … con su `area` declarada en los metadatos de ampliación | `B65-C01` |
| Clases nuevas en un bloque existente | continúan: `B49-C21`, `B49-C22`, … | `B49-C21` |
| Módulo nuevo en una ruta | `R12-M09`, con clases `R12-M09-C01…` | `R12-M09-C01` |

Un bloque nuevo no tiene por qué tener exactamente 20 clases; el tamaño se justifica por la capacidad que enseña. Los bloques y módulos existentes conservan sus 20 clases originales; las ampliadas se identifican como «extensión» y no cambian el significado de las anteriores.

## Dónde se registran

```text
catalogo/ampliaciones/v0.2.0/
  bloques.json                 # bloques nuevos: id, nombre, area, justificación, roles que lo requieren
  clases.jsonl                 # clases nuevas con la misma estructura que catalogo/clases.jsonl
  matriz_compatibilidad.json   # qué IDs de la línea base permanecen idénticos
```

Los archivos `catalogo/clases.*` de la línea base no se editan. Los validadores actuales (`validar_catalogo.py`) siguen comprobando la línea base; un validador de ampliaciones comprobará que ningún ID nuevo colisione ni desplace a uno antiguo.

## Propuesta de unidad nueva

Toda propuesta incluye: necesidad y roles que la requieren (con enlace a su `hueco`), público, fuentes localizadas, nivel N0–N5, dependencias por capacidad, evidencia de aprendizaje y un análisis antirrepetición contra el catálogo existente. Sin ese contraste, no se incorpora.

## Orden de trabajo

1. Definir el recorrido de los 24 roles (`pendiente` → `definido`).
2. Consolidar los `huecos` por tema y por frecuencia entre roles.
3. Agrupar en propuestas (bloques nuevos, clases en bloques existentes, módulos de ruta).
4. Registrar la ampliación `0.2.0` y su matriz de compatibilidad.
5. Redactar las clases nuevas con la [guía de redacción](GUIA_DE_REDACCION_DE_CLASES.md).

## Conteo

La cifra de 5.120 clases es la línea base `0.1.0` y se mantiene como tal ([estructura y conteo](ESTRUCTURA_Y_CONTEO_DEL_CATALOGO.md)). Cuando exista la ampliación se informará «5.120 de la línea base más N de ampliación», nunca una cifra única que oculte el origen.
