# B102 — Movilidad de robots planetarios

> **Bloque nuevo de la estructura `0.2.0`.** Sus 8 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A08 — Operaciones de misión y robótica espacial  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 8 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Dinámica multicuerpo de rovers y manipuladores» hasta «Traversabilidad y evaluación de riesgo de terreno». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B102-C01 — Dinámica multicuerpo de rovers y manipuladores

*Programada, sin redactar.* B05 y B84 dan mecánica y análisis estructural, pero ninguna clase formula la dinámica de sistemas de cuerpos articulados con contactos.

### B102-C02 — Terramecánica: tracción y hundimiento en suelos sueltos

*Programada, sin redactar.* B97-C06 introduce la movilidad sobre regolito; falta el modelo de interacción rueda-suelo (presión, cizalladura, hundimiento) que sostiene la tracción.

### B102-C03 — Deslizamiento y estimación de patinaje

*Programada, sin redactar.* Ninguna clase trata el deslizamiento de ruedas sobre suelo suelto ni cómo estimarlo para corregir odometría y control.

### B102-C04 — Suspensión rocker-bogie y mecánica de rovers

*Programada, sin redactar.* El tronco no contiene una clase sobre arquitecturas de suspensión de rovers ni su efecto en la adaptación al terreno.

### B102-C05 — Distribución de cargas y estabilidad ante vuelco

*Programada, sin redactar.* B05-C05 da los diagramas de cuerpo libre, pero falta aplicarlos al reparto de carga por rueda y a márgenes de estabilidad en pendiente.

### B102-C06 — Dinamometría y medición de fuerzas de tracción

*Programada, sin redactar.* B13 cubre metrología general; falta la medición de tracción y resistencia al avance con bancos y celdas de carga para validar modelos de locomoción.

### B102-C07 — Simulación de movilidad sobre pendientes y terreno

*Programada, sin redactar.* Ninguna clase simula la dinámica de un rover sobre pendientes y terrenos deformables para evaluar tracción y estabilidad.

### B102-C08 — Traversabilidad y evaluación de riesgo de terreno

*Programada, sin redactar.* B53 describe geología de superficies, pero ninguna clase convierte pendiente, rugosidad y rocas en riesgo de navegación.

## Roles que lo usan

- [Robótica espacial y sistemas autónomos](../../rutas/robotica-espacial-y-sistemas-autonomos.md)
