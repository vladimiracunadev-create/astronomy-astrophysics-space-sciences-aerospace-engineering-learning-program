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

La dirección se actualiza con `#o=<id>&f=<fecha UTC>`. Por ejemplo, [el eclipse total del 2 de agosto de 2027](../tierra-sol-luna.html#o=301&f=2027-08-02T10:07).

## Accesibilidad

Los controles se manejan con teclado y tienen etiquetas; el escenario puede enfocarse con Tab y manejarse con flechas. Los colores cumplen contraste sobre fondo oscuro. Los simuladores no reproducen nada solos ni usan sonido. La información visual relevante (fase, distancia, iluminación) también aparece como texto en el panel.

## Si algo no carga

Los datos se descargan con `fetch`: abra el sitio publicado en GitHub Pages o sirva la carpeta con `python -m http.server` (los navegadores no permiten `fetch` desde `file://`). Se necesita un navegador con módulos ES y Canvas 2D (cualquiera actual).
