# Capítulo 1 · Objetivo y requisitos

## Por qué existe este capítulo

Un observatorio no «explora» un lugar: **responde preguntas con luz**. Cada requisito técnico (el tamaño del espejo, la temperatura, la longitud de onda) sale de qué se quiere ver. Aquí se aprende a bajar una pregunta científica hasta una tolerancia de nanómetros.

## Las preguntas

1. **¿Cuándo y cómo se formaron las primeras estrellas y galaxias?** La luz de los objetos más lejanos se ha estirado por la expansión del universo y llega en el **infrarrojo**.
2. **¿Cómo nacen y evolucionan las galaxias, las estrellas y los sistemas planetarios?** El polvo oculta la luz visible; el infrarrojo lo atraviesa.
3. **¿Cómo son las atmósferas de los planetas fuera del sistema solar?** El infrarrojo revela moléculas como agua, metano y dióxido de carbono.

## De la pregunta al requisito

| Pregunta | Requisito derivado | Consecuencia de diseño |
|---|---|---|
| Galaxias muy lejanas y tenues | Gran área colectora (≈ 25 m²) | Espejo de 6,5 m en segmentos |
| Infrarrojo cercano y medio (≈ 0,6 a 28 µm) | Instrumentos infrarrojos y telescopio frío | Escudo solar y refrigeración |
| Imágenes nítidas | Superficie del espejo con error de decenas de nanómetros | Alineación activa con motores |
| Observación continua | Sin Tierra ni Luna que la cieguen | Órbita en el punto L2 |
| Años de operación | Combustible y fiabilidad por ≥ 10 años | Reserva de combustible y diseño robusto |

Los números vienen del laboratorio (`laboratorio_T04.py`): el área colectora es **6,2 veces** la del telescopio espacial Hubble, y la resolución teórica a 2 µm, de 0,077 segundos de arco.

## Por qué el infrarrojo manda el diseño

Todo cuerpo emite luz según su temperatura. A 300 K (el ambiente terrestre) el pico de emisión está en ≈ 9,7 µm, **justo en el infrarrojo que se quiere observar**: un telescopio caliente se vería a sí mismo. Para que su brillo propio deje de molestar hay que enfriarlo hasta ≈ 40 K, donde el pico pasa a ≈ 72 µm (laboratorio, sección 3). **De ahí salen el escudo solar, la distancia y el nuevo tipo de órbita.**

## Niveles de éxito

- **Mínimo:** desplegar y alinear el observatorio y obtener ciencia en la banda principal.
- **Completo:** cumplir las 5 grandes metas durante 5 años.
- **Extendido:** operar más de una década. Gracias a la precisión del lanzamiento, el combustible alcanza para unos **20 años** (⚠ verifica en la fuente).

## Restricciones

- **El cohete:** un espejo de 6,5 m no cabe en una cofia de 5 m: **debe plegarse**.
- **La imposibilidad de reparar:** a 1,5 millones de km no hay misión de servicio (Hubble se reparó cinco veces, JWST no puede).
- **El costo y el calendario:** capítulo 9.

## Ejercicio del capítulo

1. Elige una pregunta científica distinta (por ejemplo, observar exoplanetas en la zona habitable) y derívala hasta cinco requisitos con unidad.
2. Con el laboratorio, calcula el límite de difracción para un espejo de 4 m a 1 µm y a 10 µm.
3. Explica con la ley de Wien por qué observar a 20 µm exige un telescopio más frío que observar a 2 µm.

Siguiente: [capítulo 2 · Ventana y trayectoria](02-ventana-y-trayectoria.md) · [índice](README.md)
