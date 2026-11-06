# B50 — Diseño óptico computacional y tolerancias

> **Bloque nuevo de la estructura `0.2.0`.** Sus 15 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A04 — Óptica, telescopios y observatorios científicos  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 15 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Trazado exacto de rayos y aberraciones de orden superior» hasta «Presupuesto de error de frente de onda de un instrumento». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B50-C01 — Trazado exacto de rayos y aberraciones de orden superior

*Programada.* B41-C08 enseña trazado en aproximación paraxial; falta el trazado exacto de rayos que cuantifica las aberraciones reales.

### B50-C02 — Optimización de superficies: función de mérito y restricciones

*Programada.* B11-C17 da optimización numérica general; falta definir funciones de mérito y variables de diseño ópticas.

### B50-C03 — Sistemas catadióptricos: Schmidt y Maksutov

*Programada.* B41 trata refractores y reflectores por separado; ninguna clase combina ambos tipos de elementos.

### B50-C04 — Telecentricidad, viñeteo y diseño del campo

*Programada.* B41-C11 trata campo y escala; falta la telecentricidad y el viñeteo como criterios de diseño.

### B50-C05 — Luz parásita y análisis de rayos dispersos

*Programada.* Ninguna clase trata la luz difusa, reflexiones fantasma y deflectores que limitan el contraste de un instrumento.

### B50-C06 — Software de diseño óptico: modelos reproducibles y verificación

*Programada.* Falta usar herramientas de diseño óptico con archivos de modelo versionados y verificados contra cálculos analíticos.

### B50-C07 — Curvatura de campo y aplanadores

*Programada.* B41-C13 y B41-C14 cubren otras aberraciones; ninguna trata la curvatura de campo ni los elementos que la corrigen.

### B50-C08 — Distorsión geométrica y su calibración

*Programada.* Ninguna clase mide ni modela la distorsión del campo, relevante para astrometría y mosaicos.

### B50-C09 — Asignación y balance de tolerancias ópticas

*Programada.* Falta repartir tolerancias entre elementos para cumplir un desempeño objetivo con costo razonable.

### B50-C10 — Errores de centrado y su efecto en el desempeño

*Programada.* Ninguna clase cuantifica el efecto del descentramiento de elementos sobre la calidad de imagen.

### B50-C11 — Errores de inclinación de elementos y superficies

*Programada.* Ninguna clase trata la sensibilidad a inclinación de espejos y lentes ni su compensación.

### B50-C12 — Sensibilidad térmica del desempeño óptico y atermalización

*Programada.* B43-C11 trata dilatación mecánica; falta su efecto en foco y aberraciones y el diseño atérmico.

### B50-C13 — Análisis Monte Carlo de tolerancias ópticas

*Programada.* B12-C14 enseña Monte Carlo en general; falta aplicarlo a conjuntos de tolerancias y a la distribución del desempeño.

### B50-C14 — Criterios de aceptación: Strehl, error de frente de onda y especificaciones

*Programada.* B42-C06 y B42-C07 definen PSF y OTF; falta traducirlos en criterios de aceptación y especificaciones verificables.

### B50-C15 — Presupuesto de error de frente de onda de un instrumento

*Programada.* B13-C13 y B83-C09 trazan presupuestos de incertidumbre y masa; falta repartir el error de frente de onda entre diseño, fabricación y alineación.

## Roles que lo usan

- [Ingeniería óptica y telescopios profesionales](../../rutas/ingenieria-optica-y-telescopios-profesionales.md)
