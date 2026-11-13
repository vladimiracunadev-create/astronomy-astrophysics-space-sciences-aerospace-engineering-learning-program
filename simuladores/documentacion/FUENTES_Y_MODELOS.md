# Fuentes, modelos y límites

## Constantes físicas

| Magnitud | Valor | Fuente |
|---|---|---|
| Unidad astronómica | 149 597 870,7 km | IAU 2012, Resolución B2 |
| Radio solar | 695 700 km | IAU 2015, Resolución B3 |
| Radio ecuatorial: Mercurio, Venus, Tierra, Marte | 2 439,4 · 6 051,8 · 6 378,1366 · 3 396,19 km | IAU/NASA (Archinal et al. 2018) |
| Radio ecuatorial a 1 bar: Júpiter, Saturno, Urano, Neptuno | 71 492 · 60 268 · 25 559 · 24 764 km | IAU/NASA (Archinal et al. 2018) |
| Radio de Luna, Plutón y Ceres | 1 737,4 · 1 188,3 · 469,7 km | NASA/JPL |
| Achatamiento | Tierra 1/298,257 · Marte 1/169,8 · Júpiter 0,0649 · Saturno 0,0980 · Urano 0,0229 · Neptuno 0,0171 | NASA (hojas de datos planetarias) |
| GM (km³/s²) | Sol 132 712 440 041,94 · Tierra 398 600,435 · Marte 42 828,375 · Júpiter 126 686 534,9 · Saturno 37 931 207,8 · Urano 5 793 951,3 · Neptuno 6 835 099,5 | JPL SSD (DE440) |
| Radios de lunas | Radio medio del bloque «Satellite physical properties» de Horizons; si Horizons no lo publica se muestra «no publicado» y el cuerpo se dibuja como punto | NASA/JPL Horizons |
| Anillos (radios interior/exterior) | Valores orientativos de las hojas de datos de NASA/JPL para Júpiter, Saturno, Urano y Neptuno; opacidad **ilustrativa** | NASA/JPL |

El archivo [`motor/cuerpos.js`](../motor/cuerpos.js) contiene cada valor. Ninguna masa o radio se usa para calcular una posición: las posiciones salen **sólo** de las efemérides.

## Orientación de los cuerpos

El polo norte y el meridiano origen de cada planeta siguen el informe del grupo de trabajo IAU WGCCRS (Archinal et al., 2018) con los **términos seculares** de ascensión recta, declinación y rotación; se omiten los términos periódicos (nutación, libración), salvo el principal de Neptuno. Para la **Tierra** se usa el ángulo de rotación terrestre ERA (IERS 2003) con UT1 ≈ UTC, más preciso que la expresión de la IAU; la precesión-nutación se omite (error de orientación ≤ ~0,7°, ~3 min en la hora local del punto subsolar). La **Luna** gira en modo síncrono *medio* (sin libración): su cara mira a la Tierra.

## Qué es dato y qué es ilustración

| Elemento | Naturaleza |
|---|---|
| Posición de planetas y lunas | **Dato oficial** (JPL Horizons), interpolado con error medido |
| Distancias, velocidades, ángulos, fases, iluminación | Calculados a partir de las posiciones |
| Tamaños | Reales (el factor de ampliación es explícito y visible) |
| Elementos osculadores (a, e, i, periodo) | Calculados del estado instantáneo respecto del planeta (o del Sol); **osculadores**, no medios |
| Eclipses | Cálculo propio de conos de sombra, validado contra el catálogo de la NASA (véase [Tierra, Sol y Luna](tierra-sol-luna.md)) |
| Sombras de un planeta sobre sus lunas | Cono de umbra (radio del planeta y Sol extenso); sin penumbra ni atmósfera |
| Texturas de superficie | **Ilustrativas**: procedurales; la Tierra usa la máscara tierra/mar de Natural Earth 1:110m (dominio público) y la Luna sus mares principales en coordenadas aproximadas. No son fotografías |
| Fondo de estrellas | Decorativo (posiciones aleatorias con semilla fija); no es un catálogo |
| Anillos | Radios orientativos de NASA, opacidad ilustrativa |

## Límites conocidos

- El simulador **no propaga órbitas**: sólo evalúa tablas. No sirve para planificar misiones ni para efemérides de precisión sub-kilométrica de lunas pequeñas.
- La aberración, la refracción y el paralaje de un observador en la superficie **no** se modelan; los eclipses se calculan geocéntricamente.
- Las lunas con efemérides parciales se ocultan tras su fecha final de cobertura.
- Los datos reflejan los ajustes de Horizons a 13 de noviembre de 2026.

## Licencias de los datos

Los datos de Horizons son productos del JPL/NASA; la información de la NASA es en general de dominio público (condiciones de uso de NASA). Natural Earth es de dominio público. El código es Apache-2.0 y la documentación CC BY-NC-SA 4.0, como el resto del repositorio. Véase [DATA_LICENSES.md](../../DATA_LICENSES.md) y [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).
