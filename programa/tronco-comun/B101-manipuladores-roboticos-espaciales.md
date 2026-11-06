# B101 — Manipuladores robóticos espaciales

> **Bloque nuevo de la estructura `0.2.0`.** Sus 10 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A08 — Operaciones de misión y robótica espacial  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 10 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Transformaciones homogéneas y parametrización de eslabones (Denavit-Hartenberg)» hasta «Simulación de una tarea tripulada con manipulador». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B101-C01 — Transformaciones homogéneas y parametrización de eslabones (Denavit-Hartenberg)

*Programada, sin redactar.* B10 enseña rotaciones y cambio de marcos, pero ninguna clase une rotación y traslación en una transformación homogénea ni parametriza la cadena de eslabones de un brazo.

### B101-C02 — Cinemática inversa y redundancia de manipuladores

*Programada, sin redactar.* B97-C02 presenta la cinemática de manipuladores en una sola clase; resolver la cinemática inversa (soluciones múltiples, redundancia, métodos numéricos) exige su propia clase.

### B101-C03 — Singularidades y manipulabilidad de brazos robóticos

*Programada, sin redactar.* B10-C11 (SVD) da la herramienta matemática, pero ninguna clase analiza singularidades y pérdida de movilidad de un brazo ni su evasión.

### B101-C04 — Límites articulares, espacio de trabajo y evitación de colisiones

*Programada, sin redactar.* Ninguna clase del tronco trata las restricciones articulares, el espacio de trabajo alcanzable ni la evitación de autocolisiones de un manipulador.

### B101-C05 — Calibración cinemática de manipuladores

*Programada, sin redactar.* B13-C05 trata calibración instrumental general; no existe una clase sobre identificar parámetros cinemáticos reales de un brazo a partir de mediciones.

### B101-C06 — Simulación de un brazo robótico espacial

*Programada, sin redactar.* B97-C20 integra una misión completa y B16-C20 un simulador de orientación; falta la simulación específica de cinemática y dinámica de un brazo.

### B101-C07 — Control de fuerza e impedancia en manipulación

*Programada, sin redactar.* B16 trata control clásico; falta el control de contacto (fuerza, impedancia) para manipular componentes en microgravedad.

### B101-C08 — Gemelo digital para ensayo de reparaciones robóticas

*Programada, sin redactar.* B97-C20 simula una misión; falta construir y usar un gemelo digital de un satélite y su brazo para ensayar reparaciones.

### B101-C09 — Coordinación visual y cámaras en operaciones con manipulador

*Programada, sin redactar.* Ninguna clase trata las vistas y cámaras disponibles para el operador, los puntos ciegos y la referencia visual en operaciones con brazo.

### B101-C10 — Simulación de una tarea tripulada con manipulador

*Programada, sin redactar.* B97-C20 integra una misión robótica; falta simular una tarea con operador humano (captura, ensamblaje).

## Roles que lo usan

- [Robótica espacial y sistemas autónomos](../../rutas/robotica-espacial-y-sistemas-autonomos.md)
- [Astronáutica tripulada y entrenamiento de astronautas](../../rutas/astronautica-tripulada-y-entrenamiento-de-astronautas.md)
