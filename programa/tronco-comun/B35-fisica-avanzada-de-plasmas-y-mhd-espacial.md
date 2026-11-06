# B35 — Física avanzada de plasmas y MHD espacial

> **Bloque nuevo de la estructura `0.2.0`.** Sus 10 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A03 — Astrofísica y ciencias fundamentales del universo  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 10 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Funciones de distribución de velocidades en plasmas» hasta «Condiciones de frontera en modelos MHD». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B35-C01 — Funciones de distribución de velocidades en plasmas

*Programada, sin redactar.* Introduce la función de distribución (Maxwell, kappa) como objeto central de la física de plasmas; B30 trata partículas cargadas y Debye pero no describe el plasma mediante distribuciones.

### B35-C02 — Ondas de Alfvén y ondas magnetosónicas

*Programada, sin redactar.* B30-C08 cubre ondas de plasma electrostáticas y B30-C09 la MHD en general, pero ninguna clase desarrolla la dispersión y propagación de ondas de Alfvén.

### B35-C03 — Inestabilidades de plasma: cinéticas y de fluido

*Programada, sin redactar.* Ninguna clase del tronco trata la estabilidad lineal de plasmas (two-stream, Kelvin-Helmholtz, tearing); es base para turbulencia, reconexión y choques.

### B35-C04 — Colisiones, régimen cinético y ecuación de Vlasov

*Programada, sin redactar.* Se necesita el criterio fluido frente a cinético y la ecuación de Vlasov; B30 asume el plasma como fluido sin establecer cuándo falla esa descripción.

### B35-C05 — Simulación de plasmas por partículas (PIC)

*Programada, sin redactar.* El método particle-in-cell no aparece en B11 ni B14; es la herramienta estándar para plasmas no colisionales en heliofísica.

### B35-C06 — Mediciones in situ de plasmas espaciales

*Programada, sin redactar.* Enseña a interpretar mediciones de naves (distribuciones, campos, momentos) y sus sesgos; B47-C09 trata el detector pero no el análisis del plasma medido.

### B35-C07 — Congelamiento del flujo magnético y conservación en MHD ideal

*Programada, sin redactar.* Teorema de Alfvén y conservación de flujo y helicidad; B30-C09 presenta las ecuaciones MHD sin desarrollar las leyes de conservación que sostienen el resto del módulo.

### B35-C08 — Flujos de plasma estacionarios y balance de presiones

*Programada, sin redactar.* Flujos, equilibrio de presiones y Bernoulli magnético; no están en B30 ni en B09-B11.

### B35-C09 — Turbulencia en plasmas y MHD

*Programada, sin redactar.* Cascadas, espectros e intermitencia en el viento solar; ninguna clase actual trata turbulencia de plasmas.

### B35-C10 — Condiciones de frontera en modelos MHD

*Programada, sin redactar.* Cómo imponer fronteras físicas y numéricas en simulaciones heliosféricas; B11-C12 trata fronteras de forma genérica, sin el caso MHD.

## Roles que lo usan

- [Heliofísica y climatología espacial](../../rutas/heliofisica-y-climatologia-espacial.md)
