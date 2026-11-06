# B49 — Antenas y receptores de radioastronomía

> **Bloque nuevo de la estructura `0.2.0`.** Sus 11 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A04 — Óptica, telescopios y observatorios científicos  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 11 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Antenas de hilo: dipolo, monopolo e impedancia de radiación» hasta «Mezcladores de frecuencia: pérdida de conversión y productos espurios». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B49-C01 — Antenas de hilo: dipolo, monopolo e impedancia de radiación

*Programada.* B46 arranca en antenas parabólicas (C03); ninguna clase del tronco enseña antenas de hilo, resistencia de radiación ni su uso como elemento de arreglo o de banda baja.

### B49-C02 — Adaptación de impedancias y líneas de transmisión en antenas

*Programada.* B89 trata presupuesto de enlace y ganancias, pero ninguna clase enseña impedancia característica, ROE ni redes de adaptación entre antena y receptor.

### B49-C03 — Apuntamiento y seguimiento de radiotelescopios: modelos de apuntado y errores

*Programada.* B43 cubre monturas y encoders de telescopios ópticos; ningún bloque trata modelos de apuntado, errores por flexión y calibración de apuntado de grandes antenas de radio.

### B49-C04 — Arreglos de antenas: factor de arreglo y formación de haz

*Programada.* B46-C14 trata líneas de base interferométricas, pero no el factor de arreglo, el control de lóbulos ni la formación de haz de arreglos de fase.

### B49-C05 — Medición y calibración de patrones de antena

*Programada.* B46-C04 enseña a interpretar diagramas de radiación; falta la competencia de medirlos (campo lejano, fuentes celestes, drones) y calibrarlos.

### B49-C06 — Amplificadores de bajo ruido (LNA): tecnología, ganancia y adaptación

*Programada.* B46-C07 describe la cadena superheterodina de forma general; ninguna clase trata el diseño ni la caracterización de amplificadores de bajo ruido HEMT/SiGe.

### B49-C07 — Criogenia y refrigeración de receptores de radio

*Programada.* B44-C08 y B47-C13 tratan enfriamiento de detectores ópticos y de instrumentos orbitales; ninguna cubre criostatos, cabezas frías y ruido físico de receptores de radio.

### B49-C08 — Estabilidad de ganancia de receptores y variaciones de ganancia

*Programada.* B46-C08 trata estabilidad de osciladores; ninguna clase enseña deriva de ganancia, varianza de Allan de radiómetros ni técnicas de conmutación tipo Dicke.

### B49-C09 — Linealidad, compresión e intermodulación de receptores de RF

*Programada.* B44-C10 trata no linealidad de detectores ópticos; no hay clase sobre punto de compresión, productos de intermodulación y rango dinámico de receptores de RF.

### B49-C10 — Filtros de radiofrecuencia pasabanda y rechazo de banda imagen

*Programada.* Ninguna clase del tronco enseña diseño ni selección de filtros pasabanda de RF; B15-C07 trata solo filtrado digital.

### B49-C11 — Mezcladores de frecuencia: pérdida de conversión y productos espurios

*Programada.* B46-C07 presenta la conversión de modo general; falta la competencia específica de mezcladores (pérdida de conversión, aislamiento, espurios, mezcladores SIS/HEB).

## Roles que lo usan

- [Radioastronomía e interferometría](../../rutas/radioastronomia-e-interferometria.md)
