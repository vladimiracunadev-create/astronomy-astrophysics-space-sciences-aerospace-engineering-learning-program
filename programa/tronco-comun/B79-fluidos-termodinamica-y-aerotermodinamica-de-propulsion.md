# B79 — Fluidos, termodinámica y aerotermodinámica de propulsión

> **Bloque nuevo de la estructura `0.2.0`.** Sus 16 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A06 — Mecánica orbital, navegación y vuelo espacial  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 16 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Conservación de masa en fluidos» hasta «Eficiencias termodinámicas de motores». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B79-C01 — Conservación de masa en fluidos

*Programada.* Ninguna clase del tronco trata la mecánica de fluidos; B05-C14 solo ve gases y presión. Es la base para toberas y aerodinámica.

### B79-C02 — Ecuaciones de Euler para flujo no viscoso

*Programada.* Aporta las ecuaciones de flujo ideal base del análisis de toberas; el tronco no incluye mecánica de fluidos.

### B79-C03 — Ecuaciones de Navier-Stokes

*Programada.* Aporta el modelo general de flujo viscoso; ninguna clase del tronco lo trata.

### B79-C04 — Regímenes laminar y turbulento

*Programada.* Enseña a distinguir regímenes y su efecto en arrastre y calor; no existe en el tronco.

### B79-C05 — Dinámica de fluidos compresibles

*Programada.* Cubre el flujo con densidad variable necesario para propulsión; B77-C03 trata fuerzas aerodinámicas sin flujo compresible.

### B79-C06 — Flujos supersónicos

*Programada.* Aporta el comportamiento del flujo a Mach>1 en toberas y vehículos; ninguna clase lo trata.

### B79-C07 — Ondas de choque normales y oblicuas

*Programada.* Enseña saltos de propiedades en choques, clave en reentrada y toberas; B30-C14 trata choques astrofísicos, no gasdinámicos.

### B79-C08 — Flujo en toberas convergente-divergentes

*Programada.* Aporta la teoría de expansión en toberas; B78-C03 trata la cámara pero no el flujo por la tobera.

### B79-C09 — CFD académico: fundamentos y límites

*Programada.* Aplica B11-C14/C15 a flujos; ninguna clase construye una simulación CFD ni discute sus límites.

### B79-C10 — Primera ley de la termodinámica en sistemas abiertos

*Programada.* B05-C13 ve temperatura y energía térmica, pero no la formulación de volumen de control usada en propulsión.

### B79-C11 — Segunda ley y entropía

*Programada.* Ninguna clase del tronco trata entropía ni irreversibilidad, necesarias para eficiencias propulsivas.

### B79-C12 — Procesos adiabáticos e isentrópicos

*Programada.* Aporta las relaciones isentrópicas usadas en toberas; no existe en el tronco.

### B79-C13 — Entalpía de flujo y entalpía total

*Programada.* Concepto de energía de flujo para el análisis de motores; ninguna clase lo trata.

### B79-C14 — Propiedades de gases calientes

*Programada.* Aporta propiedades termofísicas de gases de combustión a alta temperatura; B06-C09 trata gases en general.

### B79-C15 — Ciclos termodinámicos de propulsión

*Programada.* Enseña ciclos de motores térmicos; B85-C11 trata ciclos térmicos de ensayo, no termodinámicos.

### B79-C16 — Eficiencias termodinámicas de motores

*Programada.* Cuantifica la conversión de energía en propulsión; no cubierta por ninguna clase.

## Roles que lo usan

- [Ingeniería de lanzadores y propulsión](../../rutas/ingenieria-de-lanzadores-y-propulsion.md)
