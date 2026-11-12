# Capítulo 4 · Subsistemas

## Por qué existe este capítulo

Los subsistemas de una cápsula tripulada son los de un satélite más **una cabina habitable** y **sistemas de emergencia**. Cada uno debe tener un modo seguro que no dependa de otro.

## Soporte vital

Debe mantener un ambiente respirable a presión y temperatura adecuadas, y retirar el dióxido de carbono y la humedad. Valores típicos (⚠ verifica) por persona y día: ≈ 0,84 kg de oxígeno, ≈ 2,5 kg de agua y ≈ 1,0 kg de CO₂ producido. El laboratorio (sección 5) calcula, para **2 personas, 4 días y 30 % de margen**: ≈ 8,7 kg de oxígeno, ≈ 26 kg de agua y ≈ 10,4 kg de CO₂ a absorber.

**Decisión de diseño:** la cápsula puede **volar libre** unos días por sí sola (por si no se acopla o debe volver), así que su soporte vital es independiente del de la estación.

## Trajes de presión

Cada astronauta lleva un **traje presurizado** que **protege si la cabina pierde presión**, con conexión al sistema de aire, de comunicaciones y de refrigeración. Es la **última capa** de seguridad, útil sobre todo en el ascenso y en la reentrada.

## Potencia

Paneles solares en el **maletero** (que no se usa en la reentrada) y baterías en la cápsula para el **tramo final**. La energía es suficiente para algunos días de vuelo libre.

## Control térmico

Radiadores en el maletero y **circuitos de líquido** que sacan el calor de la cabina y de la electrónica. En la reentrada, la protección térmica se encarga del resto.

## Aviónica y software

- **Computadores redundantes** con votación; software desarrollado con reglas estrictas y revisión independiente.
- **Pantallas táctiles** como interfaz principal, con **controles físicos** para funciones críticas (por ejemplo, abortar o presurizar).
- **Modo manual** para el acoplamiento si falla el automático.

## Navegación y acoplamiento

Sensores relativos (cámaras, láser y GPS) para medir distancia y velocidad respecto a la estación. Un **corredor de aproximación** con puntos de comprobación y reglas de aborto.

## Comunicaciones

Enlaces con la Tierra a través de satélites de retransmisión y de estaciones de tierra, con **voz** casi continua con el control de vuelo.

## Propulsión

- **Draco (16):** maniobras orbitales y de actitud.
- **SuperDraco (8):** aborto de ascenso.
- La cápsula **no** usa los SuperDraco para el aterrizaje habitual.

## Ejercicio del capítulo

1. Dimensiona el **soporte vital** para 4 personas y 7 días de vuelo libre con 30 % de margen.
2. Haz el **presupuesto de energía** de un día de vuelo libre con sus cargas principales.
3. Describe la **arquitectura de control** de una función crítica (por ejemplo, presurizar la cabina) con un respaldo independiente.

Anterior: [capítulo 3](03-lanzador-masas-y-vehiculo.md) · Siguiente: [capítulo 5](05-abortos-acoplamiento-y-retorno.md)
