# Capítulo 1 · Objetivo y requisitos

## Por qué existe este capítulo

Si un día se descubre un asteroide en curso de colisión con la Tierra, no habrá tiempo para improvisar. La técnica más madura es el **impacto cinético**: golpearlo con una nave para cambiar su velocidad un poco, y con suficiente antelación. DART lo probó **antes** de necesitarlo.

## La pregunta

¿Puede una nave **cambiar de forma medible** la órbita de un asteroide, cuánto, y cómo se predice ese cambio con los datos de una prueba?

## Por qué un asteroide doble

Se eligió el sistema **Didymos-Dimorphos** por una razón de **medición**:

- Cambiar la **órbita de un asteroide alrededor del Sol** es un efecto tan pequeño que tardaría años en detectarse.
- Cambiar la **órbita de una luna alrededor de su asteroide** es un efecto de **minutos** en un período de ≈ 12 horas, **medible en semanas** con telescopios en la Tierra.
- **Sin riesgo:** el impacto no podía poner en peligro a nadie, ni cambiar el curso del sistema respecto a la Tierra.

## Objetivos (con palabras propias)

1. **Demostrar** que una nave puede dirigirse de forma autónoma y chocar con un asteroide pequeño.
2. **Medir** el cambio del período orbital de Dimorphos.
3. **Estimar** la eficacia del impacto con el factor β.
4. **Caracterizar** el blanco: tamaño, forma y composición.

## Del objetivo al requisito

| Objetivo | Requisito (ejemplo) | Consecuencia de diseño |
|---|---|---|
| Impactar un blanco de 160 m | Navegación autónoma terminal con precisión de pocos metros | Cámara y software de guiado en el propio vehículo |
| Medir el período | Observaciones desde tierra con precisión de minutos | Campaña de telescopios por varias semanas |
| Determinar β | Conocer la masa de Dimorphos y la forma del cráter | Imágenes del impacto y una misión de seguimiento |
| Un blanco pequeño | Resolución de la cámara que lo distinga a tiempo | Cámara de alta resolución y cálculo a bordo |

## El requisito que manda: un solo intento

No hay maniobra de reserva ni segunda oportunidad: **la nave se destruye** en el impacto. Todo se juega en **los últimos minutos**.

## Niveles de éxito

- **Mínimo:** impactar a Dimorphos.
- **Completo:** además, medir un cambio de período significativo (el requisito era un cambio de al menos unos 73 segundos, ⚠ verifica) y estimar β.
- **Extendido:** una misión europea de seguimiento (**Hera**) que mida el cráter y la masa del sistema.

## Ejercicio del capítulo

1. Redacta **objetivos y requisitos** de una misión que pruebe otra técnica de defensa (por ejemplo, un «tractor gravitatorio»).
2. Explica por qué un **sistema doble** es un buen banco de pruebas y qué límites tiene frente a un caso real.
3. Define el **umbral de éxito** del cambio de período y justifícalo con tus propios criterios de medición.

Siguiente: [capítulo 2 · Ventana y trayectoria](02-ventana-y-trayectoria.md) · [índice](README.md)
