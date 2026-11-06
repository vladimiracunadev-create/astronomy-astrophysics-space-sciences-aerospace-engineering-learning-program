# B80 — Navegación inercial y fusión multisensorial

> **Bloque nuevo de la estructura `0.2.0`.** Sus 9 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A06 — Mecánica orbital, navegación y vuelo espacial  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 9 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Principios de navegación inercial espacial» hasta «Odometría inercial y preintegración de IMU». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B80-C01 — Principios de navegación inercial espacial

*Programada.* El rol necesita comprender cómo se propaga posición y velocidad a partir de una IMU; B87 solo trata el giroscopio como sensor de actitud y B74 estima órbita con observaciones externas, por lo que ninguna clase actual cubre la navegación inercial.

### B80-C02 — Modelo de error de acelerómetros

*Programada.* Aporta el modelado de sesgo, factor de escala y ruido de acelerómetros, necesario para predecir el error de navegación; B87 solo cubre sensores de actitud y ninguna clase trata acelerómetros.

### B80-C03 — Mecanización strapdown e integración de actitud y velocidad

*Programada.* Enseña la integración de las mediciones de una IMU fija al vehículo para obtener actitud, velocidad y posición; B10-C12..C15 dan las rotaciones y cuaterniones, pero ninguna clase construye la mecanización.

### B80-C04 — Fusión inercial con mediciones externas (acoplamiento débil y fuerte)

*Programada.* Cubre cómo se corrige la deriva inercial con mediciones externas; B74-C08..C10 dan los filtros, pero ninguna clase los aplica al acoplamiento inercial/externo.

### B80-C05 — Redundancia de sensores y arbitraje de mediciones

*Programada.* Enseña a combinar y arbitrar sensores redundantes para mantener la solución de navegación; B88-C12 trata FDIR general, no el arbitraje de mediciones.

### B80-C06 — Fusión IMU-cámara

*Programada.* Aporta la fusión visual-inercial que complementa a cada sensor; ni B74 ni B87 acoplan IMU y cámara en una sola solución de navegación.

### B80-C07 — Fusión radio-óptica en navegación de espacio profundo

*Programada.* Combina Doppler/rango con imágenes ópticas para reducir incertidumbre; B74-C04 y C13 las tratan por separado.

### B80-C08 — Filtrado distribuido y descentralizado

*Programada.* Cubre arquitecturas de estimación repartidas entre nodos o plataformas; B74-C08..C10 tratan filtros centralizados.

### B80-C09 — Odometría inercial y preintegración de IMU

*Programada.* B87-C06 trata giroscopios; falta la integración de acelerómetros y giróscopos para estimar movimiento de un robot y su deriva.

## Roles que lo usan

- [Navegación guiado y autonomía espacial](../../rutas/navegacion-guiado-y-autonomia-espacial.md)
- [Robótica espacial y sistemas autónomos](../../rutas/robotica-espacial-y-sistemas-autonomos.md)
