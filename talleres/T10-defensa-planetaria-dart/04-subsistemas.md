# Capítulo 4 · Subsistemas

## Por qué existe este capítulo

La nave es un **proyectil guiado** con pocos subsistemas, pero los que tiene deben funcionar perfecto en los últimos minutos: **ver, decidir y apuntar** sin ayuda.

## La cámara DRACO

Una cámara de **alta resolución** con un telescopio de ≈ 20 cm que cumple **tres funciones**:

1. **Detectar** el sistema Didymos desde lejos.
2. **Navegar:** da la posición del blanco para el guiado autónomo.
3. **Documentar:** las imágenes del acercamiento son ciencia (forma, rocas, superficie).

En los últimos minutos, cada imagen muestra a Dimorphos cada vez mayor, hasta que llena el campo. La última imagen se tomó unos **segundos** antes del impacto.

## Navegación autónoma terminal

Un software (llamado **SMART Nav**, ⚠ verifica el nombre) que, con las imágenes de la cámara:

1. Distingue **dos objetos** (Didymos y Dimorphos) cuando aún son puntos de luz.
2. **Elige el blanco** (el más pequeño).
3. Calcula la **trayectoria** y ordena **correcciones** con los propulsores.
4. **Sigue corrigiendo** hasta unos 2 minutos antes del impacto; después, solo apunta.

El laboratorio (sección 4) muestra por qué es autónomo: a 6,1 km/s, en los últimos 4 minutos la nave recorre ≈ 1.460 km; en los últimos 20 segundos, ≈ 120 km. La señal tarda ≈ 37 segundos en llegar a la Tierra: **el control en tierra no puede participar**.

## Propulsión

- **Propulsores de hidrazina** para las correcciones finas de trayectoria y la orientación.
- **Propulsor iónico (xenón)** para el crucero y como demostración tecnológica. Su empuje es mínimo (decenas de milinewton) pero su eficiencia es muy alta.

## Potencia

Dos **paneles solares enrollables**, que se despliegan en el espacio. Con ellos la nave produce unos **kilovatios** a 1 UA, suficientes para el propulsor iónico y la cámara.

## Comunicaciones

Antena de alta ganancia (banda X) y antenas de respaldo; la telemetría se transmite durante el acercamiento hasta el último instante posible.

## Cómputo

Computadores redundantes y un **software de vuelo** con reglas de **protección ante fallos** que **no pueden detener la secuencia terminal** una vez iniciada (por qué: un modo seguro en los últimos minutos perdería la misión).

## Ejercicio del capítulo

1. Con el laboratorio, calcula cuánto recorre la nave en 2 minutos y en 10 segundos. ¿Qué resolución necesita la cámara a esa distancia para ver a Dimorphos como 10 píxeles?
2. Diseña el **algoritmo de elección del blanco**: qué datos usa y cómo evita elegir el cuerpo equivocado.
3. Explica por qué las reglas de protección ante fallos deben **relajarse** en la secuencia terminal.

Anterior: [capítulo 3](03-lanzador-masas-y-vehiculo.md) · Siguiente: [capítulo 5](05-los-ultimos-minutos.md)
