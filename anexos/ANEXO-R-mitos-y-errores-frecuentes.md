# Anexo R · Mitos y errores frecuentes en astronomía y astronáutica

[⬅️ Anexo Q](ANEXO-Q-derecho-y-politica-espacial.md) · [Índice de anexos](README.md)

**Para qué sirve.** Reúne las ideas equivocadas más comunes —las de la calle, las de las películas y las que se cuelan en los primeros cursos— y las corrige **con un argumento y, cuando se puede, con un cálculo que tú mismo repites**. Un error conceptual que no se desmonta se queda aunque se memorice la fórmula correcta; por eso este anexo es de lectura temprana.

**Cómo está organizado.** Cada ficha tiene: **Mito** · **Realidad** · **Por qué se cree** · **Cómo comprobarlo**. Al final hay un método para detectar mitos nuevos.

> **Estado del texto.** Síntesis propia con cifras redondeadas, pendiente de revisión disciplinar (nivel E0). Comprueba los cálculos con la [calculadora](../herramientas/calculadora_cientifica.py).

---

## 1. La Tierra, el Sol y la Luna

**1. «Hace calor en verano porque la Tierra está más cerca del Sol».**
*Realidad:* las estaciones se deben a la **inclinación del eje (≈ 23,4°)**. La Tierra está más cerca del Sol a comienzos de enero (perihelio, 0,983 UA), en pleno invierno boreal. *Por qué se cree:* es intuitivo que más cerca = más calor. *Cómo comprobarlo:* las estaciones del hemisferio sur son opuestas a las del norte en la misma fecha; si dependiera de la distancia serían iguales.

**2. «Existe un lado oscuro de la Luna».**
*Realidad:* hay una **cara oculta**, que nunca vemos desde la Tierra porque la Luna rota sincronizada, pero recibe luz del Sol igual que la visible (con el mismo promedio). *Por qué se cree:* «oscuro» se confunde con «desconocido». *Cómo comprobarlo:* durante la Luna nueva, la cara oculta está completamente iluminada.

**3. «La Luna solo sale de noche».**
*Realidad:* la Luna se ve de día muchos días del mes, según su fase. *Comprobarlo:* mira el cielo por la tarde, unos días después de la Luna nueva.

**4. «La Luna parece enorme en el horizonte porque está más cerca».**
*Realidad:* es una **ilusión óptica**; la Luna mide el mismo ángulo (≈ 0,5°) en todo el cielo. *Comprobarlo:* sostén un lápiz a brazo extendido y compara su ancho con la Luna cerca del horizonte y alta; no cambia. (De hecho, en el horizonte está algo *más lejos*.)

**5. «El Sol es amarillo».**
*Realidad:* el Sol emite luz de todos los colores y es esencialmente **blanco**; se ve amarillento por la dispersión de la atmósfera. *Comprobarlo:* en el espacio, los astronautas ven un Sol blanco.

**6. «Un eclipse lunar daña los ojos, como el solar».**
*Realidad:* al revés. **Mirar el Sol sin protección durante un eclipse solar daña la retina**; el eclipse lunar es seguro (solo vemos la Luna).

**7. «Un año tiene exactamente 365 días».**
*Realidad:* el año tropical dura **365,2422 días**. Por eso hay años bisiestos: cada 4 años, salvo los múltiplos de 100 que no lo son de 400. *Comprobarlo:* 0,2422 × 4 ≈ 0,97 ≈ 1 día cada 4 años; la corrección de los siglos ajusta el resto. Con `calc "0.25-0.01+0.0025"` obtienes 0,2425, muy cerca de 0,2422.

📘 [B02](../programa/tronco-comun/B02-historia-arqueoastronomia-y-culturas-del-cielo.md "Historia, arqueoastronomía y culturas del cielo"), [B08](../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica").

---

## 2. Planetas y Sistema Solar

**8. «Plutón es un planeta».**
*Realidad:* desde 2006 es un **planeta enano**, porque no ha despejado su órbita. No es un «descenso de categoría» por tamaño, sino un cambio de criterio por el descubrimiento de muchos objetos similares.

**9. «El planeta más caliente es el más cercano al Sol».**
*Realidad:* es **Venus** (≈ 737 K), no Mercurio, por su efecto invernadero (92 bar de CO₂). *Comprobarlo:* con la calculadora, la temperatura de equilibrio de Venus (≈ 230 K) es *menor* que la de Mercurio: la diferencia es la atmósfera.

**10. «Los asteroides del cinturón forman un campo denso que complica el paso».**
*Realidad:* la separación media entre asteroides es de **cientos de miles de km** o más. Las sondas lo han cruzado sin problemas. Las películas lo dibujan abarrotado.

**11. «Júpiter es casi una estrella».**
*Realidad:* para fusionar hidrógeno se necesita ≈ 80 veces la masa de Júpiter (≈ 0,08 M☉). Júpiter está muy lejos de ese umbral.

**12. «Los meteoritos llegan al suelo ardiendo».**
*Realidad:* la parte caliente es la superficie, que se funde y se desprende (ablación), pero el interior sigue frío; al frenar en la atmósfera el meteorito cae a unos cientos de km/h y llega **tibio o frío**.

**13. «Las estrellas fugaces son estrellas que caen».**
*Realidad:* son **meteoros**: granos de polvo o arena (mm a cm) que arden por completo al entrar a ≈ 20–70 km/s.

**14. «La cola de un cometa va detrás, como la estela de un avión».**
*Realidad:* apunta **en dirección opuesta al Sol** (por el viento solar y la presión de radiación). Cuando el cometa se aleja, la cola va *delante* de él.

📘 [B52](../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B54](../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md "Atmósferas y climatología planetaria"), [B58](../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md "Asteroides, cometas y defensa planetaria").

---

## 3. Estrellas y universo

**15. «Las estrellas son todas del mismo tamaño que el Sol».**
*Realidad:* el Sol es una estrella mediana-pequeña. Betelgeuse mide ≈ 700–900 radios solares; las enanas rojas, ≈ 0,1.

**16. «Un año luz es una medida de tiempo».**
*Realidad:* es una **distancia**: lo que recorre la luz en un año (≈ 9,46 × 10¹⁵ m). *Comprobarlo:* `calc "ly"`.

**17. «Polaris es la estrella más brillante del cielo».**
*Realidad:* es de brillo moderado (en torno al puesto 50 del cielo). Su importancia es otra: marca el norte porque está casi en el eje de rotación terrestre (solo visible desde el hemisferio norte).

**18. «El Big Bang fue una explosión en un punto del espacio».**
*Realidad:* fue la **expansión del espacio** en todas partes a la vez. No hay un centro desde el cual todo se aleja: en un globo que se infla, cada punto ve que los demás se alejan.

**19. «Un agujero negro succiona todo a su alrededor».**
*Realidad:* a distancia, su gravedad es la de cualquier masa. Si el Sol fuese reemplazado por un agujero negro de la misma masa, la Tierra seguiría en la misma órbita (aunque a oscuras). *Comprobarlo:* el radio de Schwarzschild del Sol es solo 2,95 km (`calc "2*GM_sol/c**2"`).

**20. «El Sol arde como un fuego».**
*Realidad:* brilla por **fusión nuclear**, no por combustión química; sin oxígeno. Su potencia corresponde a transformar ≈ 4,3 millones de toneladas de masa en energía cada segundo.

**21. «Si una estrella se ve en el cielo, existe ahora mismo».**
*Realidad:* vemos la luz que **salió hace tiempo**: 4,2 años en el caso de Próxima Centauri, miles en el de las estrellas lejanas. Alguna podría haber dejado de existir.

📘 [B24](../programa/tronco-comun/B24-fisica-y-evolucion-de-estrellas.md "Física y evolución de estrellas"), [B26](../programa/tronco-comun/B26-relatividad-y-cosmologia.md "Relatividad y cosmología"), [B27](../programa/tronco-comun/B27-objetos-compactos-y-altas-energias.md "Objetos compactos y altas energías").

---

## 4. Astronáutica y vida en el espacio

**22. «Los astronautas flotan porque no hay gravedad».**
*Realidad:* a 400 km la gravedad es ≈ **90 %** de la de la superficie. Flotan porque, junto con la nave, están en **caída libre** alrededor de la Tierra. *Comprobarlo:* `calc "GM_tierra/(R_tierra+400e3)**2"` da ≈ 8,7 m/s².

**23. «Los satélites no caen porque están fuera de la gravedad».**
*Realidad:* caen continuamente, pero avanzan tan rápido de lado que «fallan» la Tierra. A 400 km necesitan ≈ 7,7 km/s.

**24. «Los cohetes funcionan empujando contra el aire».**
*Realidad:* funcionan por **acción y reacción** de los gases que expulsan, y rinden *mejor* en el vacío. Esto se discutía en 1920 (ver [Anexo K](ANEXO-K-perfiles-a-fondo.md)).

**25. «En el espacio se oyen explosiones y motores».**
*Realidad:* el sonido necesita un medio. En el vacío no se propaga. Dentro de una nave sí hay sonido (aire).

**26. «Sin traje, un astronauta explotaría o se congelaría al instante».**
*Realidad:* el cuerpo no explota; la pérdida de consciencia llega en **≈ 10–15 segundos** por falta de oxígeno, y la congelación es lenta (en el vacío no hay aire que conduzca calor).

**27. «Desde el espacio se ve la Gran Muralla china a simple vista».**
*Realidad:* es larga pero muy estrecha (unos 6–9 m de ancho); desde órbita baja no se distingue a simple vista. Sí se ven ciudades de noche, carreteras con buena luz y aeropuertos. *Comprobarlo:* el ojo resuelve ≈ 1′; a 400 km distingue unos 120 m; la muralla es mucho más angosta.

**28. «La Estación Espacial no se puede ver desde el suelo».**
*Realidad:* es uno de los objetos más brillantes del cielo (hasta magnitud ≈ −5, más que Venus) durante los pasos al amanecer o al atardecer. Hay aplicaciones y webs oficiales que anuncian sus pasos.

**29. «Se puede ver con un telescopio la bandera de Apolo».**
*Realidad:* para resolver 1 m en la Luna haría falta un telescopio de ≈ 260 m de apertura (`calc "1.22*550e-9*384400e3/1"`). Lo que sí se ha hecho es fotografiar los sitios con sondas en órbita lunar (Lunar Reconnaissance Orbiter, ≈ 0,5 m por píxel).

📘 [B05](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md "Física fundamental para el espacio"), [B71](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B105](../programa/tronco-comun/B105-medicina-y-biologia-espacial.md "Medicina y biología espacial").

---

## 5. Ciencia y tecnología

**30. «Más aumento es mejor en un telescopio».**
*Realidad:* lo que cuenta es la **apertura**: recoge luz y fija el detalle posible. El aumento sin apertura solo agranda una imagen borrosa. Un aumento útil máximo ronda 2 × la apertura en mm.

**31. «La Tierra es plana».**
*Realidad:* hay muchas pruebas independientes y verificables por cualquiera: la sombra curva de la Tierra en los eclipses de Luna; los barcos que desaparecen «de abajo hacia arriba»; las constelaciones distintas en cada hemisferio; los husos horarios; los vuelos. Eratóstenes midió en el siglo III a. C. su circunferencia con dos varillas: una diferencia de 7,2° entre dos ciudades distantes ≈ 5 000 estadios daba ≈ 250 000 estadios ≈ 40 000 km. *Comprobarlo:* `calc "360/7.2*800"` (con 800 km entre las ciudades) ≈ 40 000 km.

**32. «La ciencia dice que X es verdad absoluta».**
*Realidad:* la ciencia ofrece **modelos con incertidumbre cuantificada** que mejoran. Cuando una teoría se reemplaza (Newton → relatividad), la anterior sigue siendo válida en su rango.

**33. «Un número más preciso es más correcto».**
*Realidad:* las cifras sin incertidumbre engañan. Decir «384 399,827 km» a la Luna sin decir de qué instante es no aporta más que «384 400 km».

📘 [B01](../programa/tronco-comun/B01-el-universo-y-el-pensamiento-cientifico.md "El universo y el pensamiento científico"), [B12](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md "Probabilidad, estadística e incertidumbre"), [B20](../programa/tronco-comun/B20-metodologia-de-la-investigacion-cientifica.md "Metodología de la investigación científica"), [B41](../programa/tronco-comun/B41-optica-geometrica-y-diseno-de-telescopios.md "Óptica geométrica y diseño de telescopios").

---

## 6. Cómo detectar un mito nuevo

1. **Pregunta qué evidencia se ofrece** y si cualquiera podría comprobarla.
2. **Busca un cálculo de orden de magnitud:** ¿cuadra el número con otras cifras que conoces?
3. **Distingue «no se sabe» de «es imposible»:** muchos mitos convierten una duda en afirmación.
4. **Revisa la fuente:** ¿una agencia, un artículo revisado, un video sin referencias?
5. **Busca la explicación más simple compatible con todos los datos.**

**Ejercicio.** Elige tres creencias que oigas en tu entorno sobre el cielo o el espacio. Para cada una escribe: la afirmación, la evidencia, un cálculo o experimento para comprobarla y tu conclusión.

[⬅️ Anexo Q](ANEXO-Q-derecho-y-politica-espacial.md) · [Índice de anexos](README.md)
