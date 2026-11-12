# Capítulo 7 · Fiabilidad, fallos y contingencias

## Por qué existe este capítulo

La misión tuvo **dos riesgos que casi nadie había enfrentado a esa escala**: la hibernación de una nave de 3 toneladas durante más de dos años y medio, y un aterrizaje con una sonda que no podía anclarse.

## Hibernación: el riesgo de despertar

Entre junio de 2011 y enero de 2014 (≈ 957 días, ≈ 2,6 años) la nave estuvo en **hibernación profunda**: casi todo apagado, girando para mantenerse estable. El riesgo:

- **No despertar:** un temporizador que falle, una batería agotada o un componente congelado pierden la misión entera.
- **Despertar mal:** el encendido con un sistema calentado desigualmente puede dañar piezas.

**Mitigación:** un temporizador **redundante** y probado, un calentamiento previo **progresivo**, un procedimiento de arranque **ensayado** y una **ventana de contacto** definida. El 20 de enero de 2014 la nave envió la señal de que estaba viva (en la hora prevista) y el equipo respiró.

El laboratorio (sección 6) muestra una **cadena en serie** ilustrativa de siete grandes eventos: la probabilidad de éxito conjunta es ≈ 0,75, y el eslabón más débil, el aterrizaje de la sonda, pesa más que el resto.

## Las fallas de Philae

El aterrizaje tuvo **dos fallos de los mecanismos de anclaje** (⚠ confirma en el informe oficial): el propulsor de gas frío y los arpones no actuaron como se esperaba. La sonda **rebotó** y quedó a la sombra.

**Lo que hizo la misión resistente:**

- Los instrumentos se **ordenaron por prioridad** y las primeras horas se dedicaron a los datos esenciales.
- La sonda había sido **probada en muchos escenarios** de aterrizaje, aunque no ese.
- **Redundancia de operación:** el orbitador podía **recibir y retransmitir** los datos con una agenda flexible.

**Lecciones sobre análisis de fallos:**

- Un mecanismo **de anclaje con dos sistemas** (arpones y propulsor) solo es redundante si **no tienen modos de falla comunes**: ambos dependían de una misma cadena de activación (⚠ verifica en la fuente).
- La **incertidumbre sobre el terreno** (dureza del suelo, inclinación) debe estar en los **márgenes** del diseño.

## Capas de protección

1. **Diseño** pensado para fallos conocidos.
2. **Redundancia** de lo crítico (temporizadores, computadores, motores).
3. **Pruebas** de hibernación y de despertar con piezas reales.
4. **Procedimientos ensayados** de recuperación.
5. **Contingencias** para el aterrizaje, por ejemplo, un orden de ciencia por prioridad.

## Márgenes

- **Combustible:** el sobrante permitió **extender** la misión y practicar un final controlado.
- **Tiempo:** el calendario del aterrizaje tuvo holgura para escoger el sitio con calma.
- **Energía:** a 3 UA ya sobraba, pero había que gestionarla cerca del cometa activo.

## Ejercicio del capítulo

1. Haz un **FMEA** del despertar tras una hibernación de dos años: cinco filas con efecto, detección y mitigación.
2. Diseña un **sistema de anclaje** en el que no haya modos de falla comunes; ¿qué señalarías como el punto débil restante?
3. Con el laboratorio, calcula la probabilidad de éxito global si la sonda pasa de 0,85 a 0,95.
4. Propón una **secuencia de ciencia por prioridad** para una sonda con 60 horas de batería.

Anterior: [capítulo 6](06-operaciones-y-comunicaciones.md) · Siguiente: [capítulo 8](08-seguridad-y-proteccion.md)
