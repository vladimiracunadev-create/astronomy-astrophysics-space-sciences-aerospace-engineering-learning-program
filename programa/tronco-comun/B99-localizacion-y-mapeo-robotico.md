# B99 — Localización y mapeo robótico

> **Bloque nuevo de la estructura `0.2.0`.** Sus 7 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A08 — Operaciones de misión y robótica espacial  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 7 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Odometría visual» hasta «Robustez del mapeo ante entornos degradados». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B99-C01 — Odometría visual

*Programada.* B97-C05 menciona SLAM; ninguna clase desarrolla la estimación de movimiento a partir de secuencias de imágenes.

### B99-C02 — Detección y descriptores de características

*Programada.* B15-C12 detecta fuentes astronómicas; no cubre características locales robustas para correspondencia entre imágenes.

### B99-C03 — SLAM basado en grafos de poses

*Programada.* B97-C05 ofrece solo una introducción; el SLAM gráfico con optimización no lineal necesita su clase.

### B99-C04 — Cierre de bucles y consistencia global

*Programada.* Ninguna clase trata el reconocimiento de lugares visitados y la corrección global del mapa.

### B99-C05 — Mapas de ocupación y rejillas de elevación

*Programada.* El tronco no contiene representaciones de mapa para navegación autónoma.

### B99-C06 — Evaluación de deriva y error de trayectoria

*Programada.* B74-C19 evalúa precisión de navegación orbital; falta la evaluación de error de trayectoria (ATE/RPE) en localización de robots.

### B99-C07 — Robustez del mapeo ante entornos degradados

*Programada.* B12-C11 y C19 dan regresión robusta y valores atípicos, pero no su aplicación a mapeo con texturas pobres, polvo y cambios de iluminación.

## Roles que lo usan

- [Robótica espacial y sistemas autónomos](../../rutas/robotica-espacial-y-sistemas-autonomos.md)
