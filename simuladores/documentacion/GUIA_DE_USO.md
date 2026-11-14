# Guía de uso de los simuladores

Todos los simuladores comparten los mismos controles.

## Tiempo

| Control | Qué hace |
|---|---|
| ▶ / ⏸ (o barra espaciadora) | Reproduce o pausa. Empieza en pausa. |
| ◀ y ▶\| (o las teclas `,` y `.`) | Retroceden o avanzan un **paso** (selector «Paso»: 1 minuto a 1 año). |
| ⏮ y ⏭ | Van al 1 de enero de 2027 o al 31 de diciembre de 2050. |
| ⇄ | Invierte el sentido del tiempo. |
| «Velocidad» | Segundos simulados por segundo real (tiempo real hasta 1 año por segundo). |
| «Fecha UTC» + Ir | Salta a una fecha y hora UTC entre 2027 y 2050. |

Las lunas más rápidas (algunas dan una vuelta en 7 horas) parecen moverse a saltos a velocidades altas: es *aliasing* temporal de la animación, no un error de datos. Baje la velocidad para verlas girar.

## Cámara

- **Arrastrar** gira alrededor del objetivo; **rueda** o **pellizco** acerca y aleja; flechas y `+`/`−` con el teclado.
- **Clic** en un cuerpo lo selecciona; **doble clic** lo enfoca. También se puede elegir en la lista lateral (con buscador y orden por distancia, tamaño o nombre).
- Los botones de acceso rápido de cada simulador llevan la cámara a vistas útiles.

## Escala

El aviso bajo «Tamaño de los cuerpos» indica siempre qué se está viendo. **Real (×1)** dibuja cada cuerpo con su radio verdadero; los muy pequeños se marcan con un punto de pocos píxeles. Los factores ×10, ×100… amplían los cuerpos (no las distancias) para poder verlos. La barra de escala inferior indica a cuántos kilómetros equivale la regla **a la distancia del objetivo**.

## Datos del cuerpo seleccionado

Radio; distancia al Sol (UA y tiempo luz); distancia al planeta (km y radios planetarios); velocidad; elementos osculadores (a, e, i, periodo); longitud y latitud eclípticas; iluminación vista desde el planeta; estado de eclipse; y el **error máximo de interpolación medido contra JPL** de ese cuerpo. Los elementos son *osculadores*: varían en el tiempo por las perturbaciones, y por eso no coinciden con los valores «medios» de tablas.

## Enlaces compartibles

La dirección se actualiza con `#o=<id>&f=<fecha UTC>`. Por ejemplo, [el eclipse total del 2 de agosto de 2027](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/simuladores/tierra-sol-luna.html#o=301&f=2027-08-02T10:07).

## Simuladores de cielo

Elija un **lugar** (lista, o latitud y longitud este), arrastre para **girar la vista** y use la rueda para el **campo** (de 4° a 170°). Los botones «Norte, Este, Sur, Oeste y Cénit» orientan la vista; un clic en un astro muestra su altura, acimut, ascensión recta y declinación (J2000), distancia, magnitud, tamaño angular e iluminación. «Sobre el horizonte» lista lo visible y centra la vista al hacer clic. Constelaciones, nombres, cuadrículas, eclíptica, ecuador celeste y refracción (en la Tierra) se activan en «Vista».

## Trayectorias

Elija **Desde** y **Hacia**, la ventana de salida y los tiempos de vuelo, y pulse **Calcular** (o un ejemplo). En el gráfico porkchop **un clic** elige cualquier transferencia; el círculo blanco es el mínimo de la métrica elegida. Las altitudes de las órbitas de salida y llegada cambian el Δv. En la vista 3D, el control «Instante del viaje» (o ▶) recorre el viaje.

## Misiones, calendario, cometas y asistencias

- **[Misiones espaciales](misiones.md)**: elija la misión en la lista de arriba y pulse ▶. El mapa muestra cada encuentro con un planeta (anillo vacío = futuro, lleno = ya ocurrió) y lo que ganó o perdió de velocidad (▲ / ▼); un clic en el gráfico de velocidad o en un encuentro salta a esa fecha; ⏪ y ⏩ saltan al encuentro anterior y siguiente; «Cámara lenta en los encuentros» frena el tiempo al acercarse a cada planeta; «Escala lineal» muestra las proporciones reales (por defecto se comprime la distancia para ver a la vez los planetas interiores y los exteriores). El detalle del encuentro, en la barra lateral, muestra el planeta a escala.
- **[Calendario planetario](calendario.md)**: filtre por año, planeta y tipo de fenómeno, elija uno en la lista (o ⏪ ⏩) y vea la geometría Sol–Tierra–planeta con el ángulo de elongación; el gráfico inferior es la longitud del planeta menos la del Sol, y se puede descargar la lista filtrada en CSV.
- **[Cometas](cometas.md)**: elija el cometa, la vista (desde el polo norte o de canto) y pulse ▶; los hitos (perihelio, afelio y acercamientos a la Tierra y Júpiter) son clicables.
- **[Asistencias gravitatorias](asistencias.md)**: cargue un caso real o mueva v∞, la altura del paso y los ángulos θ y γ; «Máxima ganancia» y «Máximo frenado» buscan la mejor geometría.
- Los enlaces de misiones y cometas se comparten con `#m=<id de la nave>` y `#c=<designación>`.

## Accesibilidad

Los controles se manejan con teclado y tienen etiquetas; el escenario puede enfocarse con Tab y manejarse con flechas. Los colores cumplen contraste sobre fondo oscuro. Los simuladores no reproducen nada solos ni usan sonido. La información visual relevante (fase, distancia, iluminación) también aparece como texto en el panel.

## Si algo no carga

Los datos se descargan con `fetch`: abra el sitio publicado en GitHub Pages o sirva la carpeta con `python -m http.server` (los navegadores no permiten `fetch` desde `file://`). Se necesita un navegador con módulos ES y Canvas 2D (cualquiera actual).
