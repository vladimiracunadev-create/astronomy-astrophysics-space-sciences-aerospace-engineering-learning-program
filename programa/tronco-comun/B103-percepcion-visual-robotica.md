# B103 — Percepción visual robótica

> **Bloque nuevo de la estructura `0.2.0`.** Sus 8 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A08 — Operaciones de misión y robótica espacial  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 8 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Calibración intrínseca de cámaras» hasta «Métricas de evaluación de percepción». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B103-C01 — Calibración intrínseca de cámaras

*Programada, sin redactar.* B44 trata detectores astronómicos, no el modelo geométrico de cámara (focal, distorsión) necesario para visión robótica.

### B103-C02 — Calibración extrínseca y registro multisensor

*Programada, sin redactar.* Ninguna clase cubre la pose relativa cámara-robot ni entre sensores, base de la visión estéreo y la fusión.

### B103-C03 — Mapas de profundidad y correspondencia estéreo

*Programada, sin redactar.* B97-C04 introduce el estéreo; falta la clase de cálculo de disparidad y mapas de profundidad con sus errores.

### B103-C04 — Detección de obstáculos y mapas de traversabilidad

*Programada, sin redactar.* B97-C03 es una visión general de sensores; ninguna clase construye detección de obstáculos y traversabilidad a partir de percepción.

### B103-C05 — Segmentación semántica de superficies planetarias

*Programada, sin redactar.* B15-C13 trata segmentación clásica de imágenes; no hay una clase de segmentación semántica con aprendizaje automático (no existe bloque de aprendizaje automático).

### B103-C06 — Detección y catalogación de rocas en imágenes de superficie

*Programada, sin redactar.* Ningún bloque trata la detección de rocas como peligro de navegación y objetivo científico en imágenes de rovers.

### B103-C07 — Estimación de pose de objetos y objetivos por visión

*Programada, sin redactar.* B87-C09 estima actitud de satélites con sensores específicos; falta la estimación de pose de objetos por visión (PnP, marcadores).

### B103-C08 — Métricas de evaluación de percepción

*Programada, sin redactar.* Ninguna clase define métricas (precisión, recall, IoU, error de profundidad) para validar algoritmos de percepción.

## Roles que lo usan

- [Robótica espacial y sistemas autónomos](../../rutas/robotica-espacial-y-sistemas-autonomos.md)
