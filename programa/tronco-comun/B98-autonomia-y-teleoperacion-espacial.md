# B98 — Autonomía y teleoperación espacial

> **Bloque nuevo de la estructura `0.2.0`.** Sus 8 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A08 — Operaciones de misión y robótica espacial  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 8 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Planificación por objetivos a bordo» hasta «Protocolos de relevo de control entre operadores». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B98-C01 — Planificación por objetivos a bordo

*Programada.* Cubre cómo el vehículo selecciona y secuencia acciones para cumplir objetivos sin intervención de Tierra; B96-C04/C09 planifican desde Tierra y ninguna clase trata la planificación a bordo.

### B98-C02 — Sistemas de decisión autónomos y máquinas de estados de comportamiento

*Programada.* Enseña la arquitectura de decisión a bordo (reglas, máquinas de estados, árboles de comportamiento); B07-C04 solo introduce condicionales.

### B98-C03 — Control supervisado y autonomía compartida

*Programada.* B97-C07 trata teleoperación con latencia; falta el paradigma de control supervisado donde el operador da metas y el robot ejecuta.

### B98-C04 — Interfaces humano-robot para operación remota

*Programada.* B106-C16 trata ergonomía física; ninguna clase diseña interfaces y visualización para operar robots a distancia.

### B98-C05 — Autonomía de bajo nivel y comportamientos reactivos

*Programada.* No existe clase sobre comportamientos autónomos de bajo nivel (seguridad, parada, reflejos) que sostienen la operación con retardo.

### B98-C06 — Simulación de teleoperación con retardo

*Programada.* B96-C20 simula una jornada de control; falta simular retardo, pérdida de paquetes y operación supervisada de un robot.

### B98-C07 — Arquitectura de autonomía a bordo (percepción-decisión-acción)

*Programada.* B83-C07 trata arquitecturas de sistema en general; falta la arquitectura de software de autonomía (capas, planificador, ejecutivo).

### B98-C08 — Protocolos de relevo de control entre operadores

*Programada.* Ninguna clase trata el traspaso seguro del control robótico entre operadores y entre tripulación y tierra.

## Roles que lo usan

- [Navegación guiado y autonomía espacial](../../rutas/navegacion-guiado-y-autonomia-espacial.md)
- [Robótica espacial y sistemas autónomos](../../rutas/robotica-espacial-y-sistemas-autonomos.md)
- [Astronáutica tripulada y entrenamiento de astronautas](../../rutas/astronautica-tripulada-y-entrenamiento-de-astronautas.md)
