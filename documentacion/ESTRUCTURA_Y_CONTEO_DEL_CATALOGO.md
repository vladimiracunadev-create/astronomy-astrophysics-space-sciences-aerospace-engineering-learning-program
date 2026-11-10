# Estructura y conteo del catálogo

> **Este documento describe la línea base `0.1.0`.** La estructura vigente (`0.2.0`) tiene 12 áreas, 133 bloques y 2.077 clases: las 1.280 del tronco más 797 programadas, porque los 192 módulos de las rutas se integraron en áreas y bloques. Ver el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md) y `catalogo/v0.2.0/`. Lo que sigue explica de dónde sale la cifra de 5.120 de la línea base.

El catálogo tiene **5.120 clases**. Este documento explica de dónde sale esa cifra, porque una lectura rápida («8 bloques de 20 clases por área») lleva a otro número.

## Dos estructuras independientes

```text
Tronco común        8 áreas × 8 bloques × 20 clases   = 1.280 clases
Rutas profesionales 24 rutas × 8 módulos × 20 clases  = 3.840 clases
                                              Total   = 5.120 clases
```

- **Tronco común.** Cada área (A01–A08) agrupa 8 bloques (64 bloques en la línea base `0.1.0`; en la estructura `0.2.0` se numeran de forma consecutiva dentro de B01–B133) y cada bloque tiene 20 clases. Un área tiene 8 × 20 = 160 clases; las 8 áreas suman 1.280.
- **Rutas profesionales.** Cada ruta (R01–R24) tiene 8 módulos (192 módulos en total) y cada módulo tiene 20 clases. Una ruta tiene también 160 clases; las 24 rutas suman 3.840.
- Las rutas **no** son parte de las áreas: son un segundo eje que reutiliza el tronco y lo profundiza.

## Tabla de comprobación

| Concepto | Cantidad | Cuenta |
|---|---:|---|
| Áreas | 8 | A01–A08 |
| Bloques | 64 | 8 áreas × 8 bloques |
| Clases del tronco común | 1.280 | 64 bloques × 20 |
| Rutas | 24 | R01–R24 |
| Módulos | 192 | 24 rutas × 8 módulos |
| Clases de rutas | 3.840 | 192 módulos × 20 |
| **Clases del catálogo** | **5.120** | 1.280 + 3.840 |

`herramientas/validar_catalogo.py` comprueba estas cifras (20 clases por bloque y por módulo, 64 bloques, 192 módulos, 1.280 + 3.840 registros) en cada commit.

## Cómo recorrerlo

Nadie necesita cursar las 5.120 clases. El diagnóstico indica qué partes del tronco común hacen falta y qué rutas conviene seguir (ver el [mapa de rutas](MAPA_DE_RUTAS_PROFESIONALES.md)). Las 160 clases de un área y las 160 de una ruta pesan lo mismo en el conteo, pero no tienen la misma duración ni dificultad: la carga se medirá con uso real.

## Estado de la redacción

Todos los registros siguen en E0 en el catálogo. El texto de 1.148 clases está redactado y pendiente de revisión (las de las áreas A01 a A05: 160, 237, 272, 222 y 257); las demás solo tienen título, descripción y referencias preliminares, o son clases programadas sin redactar. El recuento vigente está en [`STATUS.md`](../STATUS.md).
