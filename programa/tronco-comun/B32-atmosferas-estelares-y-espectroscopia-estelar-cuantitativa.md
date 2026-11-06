# B32 — Atmósferas estelares y espectroscopía estelar cuantitativa

> **Bloque nuevo de la estructura `0.2.0`.** Sus 12 clases están programadas y ninguna está redactada: se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  
**Área:** A03 — Astrofísica y ciencias fundamentales del universo  
**Estado:** programado; no contiene clases desarrolladas.  
**Total:** 12 clases programadas.

## Alcance

Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. Cubre desde «Ecuación de transferencia radiativa en atmósferas estelares» hasta «Efecto Zeeman y diagnóstico de campos magnéticos estelares». El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.

## Clases programadas

### B32-C01 — Ecuación de transferencia radiativa en atmósferas estelares

*Programada.* El rol necesita resolver la ecuación de transferencia (profundidad óptica, función fuente); B24 solo introduce opacidades y B54 trata atmósferas planetarias, no la estelar.

### B32-C02 — Equilibrio termodinámico local y desviaciones no LTE

*Programada.* Ninguna clase del tronco trata cuándo vale el LTE ni las poblaciones atómicas fuera de equilibrio, base de la interpretación de espectros estelares.

### B32-C03 — Opacidad continua: ligado-libre, libre-libre y H-

*Programada.* B24-C09 solo menciona opacidades; falta la física de los procesos continuos que dominan la opacidad de la fotosfera estelar.

### B32-C04 — Opacidad de líneas: ensanchamiento y perfil de Voigt

*Programada.* B45 describe líneas observadas, pero no el coeficiente de absorción ni los mecanismos de ensanchamiento que determinan su perfil.

### B32-C05 — Relación T-τ y estructura térmica de la fotosfera

*Programada.* Ninguna clase deriva la estratificación de temperatura de una atmósfera gris o no gris; es el insumo de todo modelo de atmósfera.

### B32-C06 — Micro y macroturbulencia y granulación estelar

*Programada.* B42-C11 trata turbulencia terrestre para óptica adaptativa; falta la turbulencia convectiva de la fotosfera estelar y su efecto en las líneas.

### B32-C07 — Modelos de atmósferas estelares 1D y 3D hidrodinámicos

*Programada.* Ninguna clase compara rejillas de modelos plano-paralelos con simulaciones 3D ni discute sus consecuencias en abundancias derivadas.

### B32-C08 — Síntesis espectral e inversión de perfiles

*Programada.* Falta el método inverso que ajusta perfiles de línea (incluidos Stokes) para recuperar la estructura de la atmósfera; B45-C18 solo extrae espectros.

### B32-C09 — Medición de perfiles de línea: ancho equivalente y ajuste

*Programada.* B45-C10 y B45-C11 presentan líneas de emisión y absorción cualitativamente; falta medir anchos equivalentes y ajustar perfiles con incertidumbre.

### B32-C10 — Normalización y modelado del continuo espectral

*Programada.* Ninguna clase enseña a normalizar el continuo, paso previo a medir líneas y derivar parámetros estelares.

### B32-C11 — Ensanchamiento rotacional y v sin i

*Programada.* B24-C11 describe la rotación estelar físicamente; falta medir su efecto en el perfil de línea y separarlo de otros ensanchamientos.

### B32-C12 — Efecto Zeeman y diagnóstico de campos magnéticos estelares

*Programada.* B05-C17 y B24-C11 no cubren el desdoblamiento Zeeman ni su uso como diagnóstico espectropolarimétrico del campo estelar.

## Roles que lo usan

- [Astrofísica estelar y galáctica](../../rutas/astrofisica-estelar-y-galactica.md)
