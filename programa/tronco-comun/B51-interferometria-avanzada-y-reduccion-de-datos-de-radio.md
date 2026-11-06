# B51 — Interferometría avanzada y reducción de datos de radio

> **Bloque nuevo de la estructura `0.2.0`.** Sus 14 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A04 — Óptica, telescopios y observatorios científicos  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 14 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Calibración de amplitud y escala de flujo con calibradores primarios» hasta «Calibración de banda en la reducción de datos de síntesis». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B51-C01 — Calibración de amplitud y escala de flujo con calibradores primarios

*Programada.* B46-C17 trata solo calibración de fase; ninguna clase enseña escala de flujo, calibradores primarios ni el bootstrap de flujos.

### B51-C02 — Cantidades de cierre: fase y amplitud de cierre

*Programada.* Las cantidades de cierre son la base de la imagen sin fase y de la autocalibración; B46-C17 no las trata.

### B51-C03 — Ganancias complejas por antena y soluciones de calibración

*Programada.* Ninguna clase formula la ecuación de medida interferométrica ni resuelve ganancias complejas por antena/base (matrices de Jones).

### B51-C04 — Respuesta de banda y errores dependientes de la frecuencia

*Programada.* B46-C15 trata correladores y visibilidades; no hay clase sobre respuesta de banda (bandpass) ni sus errores en observaciones espectrales.

### B51-C05 — Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección

*Programada.* B30-C17 trata auroras y corrientes ionosféricas, no los efectos de la ionosfera sobre fase y polarización de señales de radio ni su corrección.

### B51-C06 — Autocalibración iterativa con modelo de cielo

*Programada.* Ninguna clase enseña self-cal (modelo, solución de ganancias, convergencia y sesgos).

### B51-C07 — Evaluación de residuos y diagnóstico de calidad de calibración

*Programada.* B13-C20 valida cadenas de medida en general; falta el diagnóstico de residuos de visibilidad y de calidad de la calibración interferométrica.

### B51-C08 — Compensación de retardo y alineación temporal de flujos de antenas

*Programada.* B74-C16 sincroniza tiempo de navegación; ninguna clase trata el seguimiento de retardo y la alineación de flujos digitales en un correlador.

### B51-C09 — Fringe stopping y rotación de fase por retardo geométrico

*Programada.* B46-C14 define la línea de base; no se enseña la rotación de fase que detiene las franjas ni la tasa de franjas.

### B51-C10 — Retardo troposférico e ionosférico en VLBI y su modelado

*Programada.* B89-C04 trata pérdidas de propagación de enlaces; no hay clase sobre retardo húmedo/seco y funciones de mapeo en geodesia por VLBI.

### B51-C11 — Búsqueda de franjas VLBI: ajuste de retardo y tasa

*Programada.* B46-C18 presenta VLBI de forma general; falta el ajuste de franjas (fringe fitting) sobre retardo y tasa de retardo.

### B51-C12 — Formatos de datos VLBI y geodésicos

*Programada.* B14-C06 y B14-C07 tratan FITS y HDF5 genéricos; no hay clase sobre formatos de grabación y de producto de VLBI (VDIF, FITS-IDI, vgosDB).

### B51-C13 — Marcado de datos espurios e interferencia en visibilidades

*Programada.* B12-C19 trata atípicos en general; falta el flagging específico de RFI y fallos de antena en visibilidades.

### B51-C14 — Calibración de banda en la reducción de datos de síntesis

*Programada.* Aplicación operativa de la respuesta de banda en el flujo de reducción (soluciones, interpolación, validación) que ninguna clase actual cubre.

## Roles que lo usan

- [Radioastronomía e interferometría](../../rutas/radioastronomia-e-interferometria.md)
