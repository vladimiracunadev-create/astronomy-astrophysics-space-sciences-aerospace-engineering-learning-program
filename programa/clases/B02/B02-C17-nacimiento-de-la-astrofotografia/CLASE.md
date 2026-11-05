# B02-C17 — Nacimiento de la astrofotografía

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B02](../../../tronco-comun/B02-historia-arqueoastronomia-y-culturas-del-cielo.md) · [← Anterior: B02-C16 — Historia de la espectroscopía astronómica](../B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md) · [Siguiente: B02-C18 — Expansión de la astronomía en Chile →](../B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Decimoséptima clase del bloque B02. El ojo humano olvida; una placa fotográfica no. Aquí ves cuándo y cómo la fotografía se convirtió en un instrumento científico para registrar el cielo, y qué problemas técnicos tuvo que resolver. Nivel N1.

Verás los primeros hitos (la Luna, el Sol, Vega, los espectros, la nebulosa de Orión), el problema del seguimiento durante exposiciones largas, que cuantificarás, y la colección de placas de Harvard como archivo científico. No verás procesamiento de imágenes ni detectores modernos (bloques B15 y B28).

## 2. Por qué esta clase existe

Un dibujo depende de quien lo hace; una placa registra lo que llegó. La pregunta motivadora es: **¿qué cambia cuando la observación puede guardarse, compararse años después y medirse?** Cambia que el cielo se vuelve un archivo, y que se ven cosas que el ojo no ve.

Al terminar sabrás ordenar los hitos con sus fuentes y matices, calcular cuánto se mueve el cielo durante una exposición y entender por qué el seguimiento fue una necesidad técnica.

## 3. Lo que podrás hacer al terminar

1. Ordenar cronológicamente cinco hitos de la astrofotografía temprana.
2. Explicar por qué una exposición larga requiere seguir el cielo.
3. Calcular el desplazamiento angular durante una exposición.
4. Explicar la ventaja de la placa seca y de la exposición larga para ver lo débil.
5. Reconocer el valor de un archivo de placas para estudios de largo plazo.
6. Redactar una ficha de un hito con su atribución cuidadosa.

La evidencia es la **ficha de un hito fotográfico** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas B01-C04 (día sidéreo) y C13. Cinco preguntas:

1. ¿Cuántas horas tiene el día sidéreo?
2. ¿Cuántos grados gira la Tierra en una hora, aproximadamente?
3. ¿Qué es una exposición?
4. ¿Qué es la magnitud límite de un instrumento?
5. ¿Qué diferencia hay entre un descubrimiento y su atribución?

<details>
<summary>Ver respuestas</summary>

1. 23,9345 h. 2. `360/23,9345 = 15,04°`. 3. El tiempo durante el cual la placa o el sensor recibe luz. 4. El brillo mínimo que se puede registrar. 5. El descubrimiento es el hecho; la atribución es a quién se le reconoce.
</details>

Con cuatro o cinco aciertos, sigue. Con tres o menos, repasa B01-C04.

## 5. Un caso real: Vega en una placa

Según un artículo enciclopédico sobre astrofotografía, William Cranch Bond y John Adams Whipple obtuvieron una daguerrotipia de Vega el 16–17 de julio de 1850 con el refractor de 15 pulgadas de Harvard, considerada la primera fotografía de una estrella distinta del Sol; John William Draper habría hecho el 23 de marzo de 1840 un daguerrotipo de la Luna de 20 minutos de exposición, y Daguerre había intentado una Luna en 1839 con un resultado borroso por falta de seguimiento (S1). El mismo artículo advierte que la palabra «primero» varía de un pasaje a otro y que varios logros se atribuyen a personas que trabajaron bajo instrucciones de otras (S1).

Es útil como ejemplo de cuidado con la atribución. Límite: S1 es enciclopédico y secundario; no leímos las fuentes originales ni los registros de Harvard.

## 6. Vocabulario

La **astrofotografía** es el registro fotográfico de objetos celestes. El **daguerrotipo** es una imagen sobre una placa metálica sensibilizada, de los primeros procedimientos fotográficos. La **placa de colodión húmedo** es una placa de vidrio sensibilizada que debe exponerse húmeda; la **placa seca** se prepara con antelación y se conserva, lo que facilita exposiciones largas (S1). La **exposición** es el tiempo de captura. El **seguimiento** (guiado) es mover el instrumento para compensar el giro de la Tierra. El **espectrograma** es la fotografía de un espectro (C16). Una **colección de placas** es un archivo de negativos de vidrio del cielo, como los más de 550 000 de Harvard (S2).

## 7. Modelo mental: luz acumulada y cielo que se mueve

La placa acumula luz mientras el cielo gira; si el instrumento no sigue el giro, cada estrella se convierte en una raya.

```mermaid
flowchart LR
    A["Exposición larga<br/>acumula luz débil"] --> B["El cielo gira<br/>15,04° por hora"]
    B --> C{"¿El instrumento<br/>sigue el cielo?"}
    C -->|"No"| D["Rayas: imagen borrosa"]
    C -->|"Sí"| E["Puntos: imagen nítida<br/>y objetos más débiles"]
    E --> F["Archivo: la placa se guarda<br/>y se compara en el tiempo"]
```

*Descripción textual:* una exposición larga acumula luz débil, pero el cielo gira a unos 15 grados por hora; si el instrumento no lo sigue, las estrellas son rayas; si lo sigue, son puntos, se ven objetos más débiles y la placa queda como archivo comparable.

Analogía: fotografiar a un corredor con obturador lento. El límite: aquí el «corredor» se mueve con regularidad perfecta, así que se puede compensar con un mecanismo de relojería.

## 8. La explicación, paso a paso

### 8.1 Los primeros hitos

S1 recoge: 1840, la Luna (20 minutos, J. W. Draper); 1845, el Sol (Foucault y Fizeau); 1850, Vega (Bond y Whipple); 1851, la corona solar en un eclipse (Berkowski, siguiendo instrucciones de Busch); 1863, el primer espectrograma fotográfico de estrellas (Miller y Huggins, con colodión húmedo); 1872, el espectro de Vega con líneas de absorción (Henry Draper); 1876, uso de placas secas en espectroscopía por los Huggins; 1880, la nebulosa de Orión con 51 minutos (Henry Draper); 1883, exposiciones de hasta 60 minutos con un reflector de 36 pulgadas (Common), las primeras en mostrar estrellas invisibles al ojo (S1). Son afirmaciones del artículo, con las cautelas de S1.

### 8.2 El problema del giro

La Tierra gira una vez respecto de las estrellas en 23,9345 h (B01-C04), es decir, `360°/23,9345 h = 15,04° por hora = 0,2507° por minuto = 15,04″ por segundo de tiempo` (cerca del ecuador celeste). En 20 minutos: `5,01°`; en 51 minutos: `12,8°`; en 60 minutos: `15,0°`. Sin seguimiento, cada estrella dibuja un arco de esa longitud. En los casos de S1 las exposiciones largas tuvieron que hacerse con el instrumento siguiendo el cielo; no sabemos cómo lo hizo cada autor, porque S1 no lo detalla.

### 8.3 Más luz acumulada

En una exposición, lo que se acumula es luz: un objeto de la mitad de brillo necesita el doble de tiempo para dejar la misma marca (aproximación válida mientras la placa responda de forma lineal, lo que no siempre ocurre con las emulsiones antiguas). Por eso las exposiciones de decenas de minutos de S1 revelaron lo que el ojo no veía: el ojo no acumula (B01-C10).

### 8.4 De la imagen al dato

Una fotografía es un dato si se registran fecha, hora, instrumento, exposición y placa. Con ello se pueden medir posiciones y brillos y comparar años después. La colección de placas del Observatorio de Harvard supera las 550 000 placas de vidrio, y el proyecto DASCH las digitalizó (finalizado en 2024) para estudiar el cielo en escalas de 100 años (S2). Los observatorios chilenos (C18) tuvieron también sus archivos de placas.

### 8.5 La espectrofotografía

Con la placa, los espectros de C16 se pudieron guardar, medir y comparar: S1 recoge la fotografía espectral de estrellas desde 1863 y las líneas de Vega en 1872. La combinación de espectro y archivo prepara la astronomía física del siglo XX.

### 8.6 Atribución cuidadosa

S1 muestra que los hitos tienen matices: la Luna de Draper se califica de «primera exitosa»; el hito de la nebulosa se describe de dos maneras en el mismo artículo; Whipple trabajó bajo Bond; Berkowski siguió instrucciones de Busch, ausente. Por eso redactamos «según S1» y evitamos «el primero» sin matiz.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor o nota |
|---|---|---|---|
| `ω` | velocidad de giro respecto de las estrellas | °/h | 15,04 |
| `t_exp` | tiempo de exposición | min | 20; 51; 60 (S1) |
| `Δθ` | desplazamiento durante la exposición | grados | `ω·t_exp` |
| placas de Harvard | cantidad | — | > 550 000 (S2) |

## 10. Convenciones y referencias

El desplazamiento se da cerca del ecuador celeste; para objetos próximos al polo celeste el arco angular es menor. Las fechas son las de S1, con sus matices. No tratamos la sensibilidad de las emulsiones.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | «Astrophotography», artículo enciclopédico (Wikipedia, en) | https://en.wikipedia.org/wiki/Astrophotography | Hitos de 1839–1883, exposiciones, atribuciones y sus cautelas | Primeros ~100 000 caracteres, 2026-11-05; **fuente secundaria** |
| S2 | Harvard College Observatory, DASCH | https://dasch.cfa.harvard.edu/ | Más de 550 000 placas de vidrio; digitalización terminada en 2024; escalas de 100 años | Consultada el 2026-11-05 |
| S3 | NASA NSSDC, *Earth Fact Sheet* | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html | Rotación sidérea 23,9345 h | Consultada el 2026-11-05 |

Límites: S1 es enciclopédica y no sustituye fuentes primarias (Draper, Bond, Huggins); no consultamos la página de línea de tiempo de las placas de Harvard (no abrió) ni sobre los orígenes del archivo. El detalle de cómo se logró el seguimiento en cada hito queda pendiente.

## 12. Cómo ver la cronología

Esta tabla es la versión accesible de una línea de tiempo.

| Año | Hito (según S1) | Exposición | Desplazamiento del cielo |
|---|---|---|---|
| 1840 | Luna (J. W. Draper) | 20 min | 5,0° |
| 1850 | Vega (Bond y Whipple) | no indicada | — |
| 1863 | Espectro estelar (Miller y Huggins) | no indicada | — |
| 1880 | Nebulosa de Orión (H. Draper) | 51 min | 12,8° |
| 1883 | Imágenes de estrellas invisibles (Common) | hasta 60 min | 15,0° |

Si lo dibujas, usa una línea de tiempo con puntos de forma distinta y rotula cada año. Descripción larga: cinco hitos a lo largo de 43 años; las exposiciones crecen de 20 a 60 minutos.

## 13. Ejemplo trabajado: ¿cuánto se mueve el cielo en 51 minutos?

**Paso 1.** `ω = 360/23,9345 = 15,041 °/h`.

**Paso 2.** `51 min = 0,85 h`.

**Paso 3.** `Δθ = 15,041 × 0,85 = 12,78°`.

**Paso 4. Incertidumbre.** La exposición de 51 min es una cifra de S1 (secundaria); el resultado supone un objeto cerca del ecuador celeste.

**Sentido físico.** En 51 minutos, el cielo gira una distancia equivalente a unos 25 diámetros de la Luna llena (que mide unos 0,5°, dato de ejemplo): sin seguimiento no habría imagen.

## 14. Comparación de técnicas

El **daguerrotipo** daba imágenes finas pero era poco sensible; el **colodión húmedo** era más sensible pero debía usarse húmedo; la **placa seca** se preparaba antes y permitía exposiciones largas (S1). Cada técnica cambió qué se podía registrar.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `ω` en °/h. *Pasos:* `360/23,9345`.

<details><summary>Solución comentada</summary>

`15,041 °/h`.
</details>

**Ejercicio 2 · con una pista.** Convierte `ω` a ″/s. *Pista:* `15,041 × 3600/3600`.

<details><summary>Solución comentada</summary>

`15,041″` por segundo de tiempo (15,041° × 3 600″/° ÷ 3 600 s).
</details>

**Ejercicio 3 · casi autónomo.** ¿Cuántos grados se mueve el cielo en 20 minutos?

<details><summary>Solución comentada</summary>

`15,041 × 20/60 = 5,01°`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Calcula `Δθ` para 60 minutos.

<details><summary>Solución comentada</summary>

`15,04°`.
</details>

**Ejercicio 5.** ¿Qué exposición máxima sin seguimiento mantiene el arco por debajo de 1 minuto de arco (cerca del ecuador)?

<details><summary>Solución comentada</summary>

`1′ = 0,01667°`; `t = 0,01667/15,041 h = 0,00111 h = 4,0 s`.
</details>

**Ejercicio 6.** Si un objeto tiene la mitad de brillo, ¿cuánto debe durar la exposición para dejar la misma marca (placa lineal)?

<details><summary>Solución comentada</summary>

El doble; la linealidad es una aproximación.
</details>

**Ejercicio 7.** ¿Por qué una placa seca favorecía exposiciones largas?

<details><summary>Solución comentada</summary>

Porque se preparaba con antelación y no debía exponerse húmeda como el colodión (S1).
</details>

**Ejercicio 8.** ¿Qué metadatos necesita una placa para ser dato científico?

<details><summary>Solución comentada</summary>

Fecha y hora con escala de tiempo, lugar, instrumento, exposición, emulsión, dirección apuntada y operador.
</details>

**Ejercicio 9 · transferencia.** Un compañero dice: «Draper hizo la primera foto de la Luna». Reescríbelo con las cautelas de S1.

<details><summary>Solución comentada</summary>

«Según un artículo enciclopédico, J. W. Draper hizo en 1840 un daguerrotipo de la Luna de 20 minutos que se considera el primer logro exitoso; Daguerre lo había intentado en 1839 sin éxito.»
</details>

**Ejercicio 10 · transferencia.** Whipple trabajó bajo Bond y Berkowski siguió instrucciones de Busch. ¿Qué lección da para dar crédito?

<details><summary>Solución comentada</summary>

Que el crédito suele ser colectivo y debe nombrar a todas las personas involucradas con su rol, en lugar de asignarlo a una sola.
</details>

**Ejercicio 11 · transferencia.** Diseña un cuaderno para fotografiar la Luna con tu teléfono sin dañar nada. ¿Qué anotarías?

<details><summary>Solución comentada</summary>

Fecha y hora, lugar, aparato, exposición y sensibilidad, condiciones del cielo y el nombre del archivo. No apuntes al Sol.
</details>

**Ejercicio 12 · integrador.** Elabora la *ficha de un hito fotográfico* (sección 20): elige un hito de la tabla, calcula el desplazamiento del cielo si hay exposición conocida, di qué fuentes lo respaldan y qué cautelas de atribución aplican.

<details><summary>Solución modelo</summary>

Sigue la sección 13: cálculo de `Δθ`, tabla de fuentes, atribución matizada y lista de lo pendiente.
</details>

## 17. Actividad sin código: tabla de giro

Esta clase no usa script. En una hoja de cálculo calcula `Δθ` para exposiciones de 1 s, 10 s, 1 min, 20 min, 51 min y 60 min. **Qué observar:** el desplazamiento es proporcional al tiempo y en solo 4 segundos ya supera 1 minuto de arco (ejercicio 5). **Resultado esperado:** 0,004°; 0,042°; 0,25°; 5,01°; 12,78°; 15,04°.

## 18. Errores frecuentes y cómo corregirlos

**Olvidar que el cielo gira.** Ejercicios 3 y 4.

**Usar 24 h en lugar de 23,9345 h.** Ejercicio 1.

**Atribuir un logro a una sola persona.** Ejercicios 9 y 10.

**Asumir linealidad de la emulsión.** Ejercicio 6.

**Tratar el archivo como solo estético.** Ejercicio 8.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿calculas el giro sin mirar? Ejercicio 3. Tras 8.6: ¿atribuyes con cuidado? Ejercicio 9. Al final: ¿qué metadatos hacen científica una foto? Ejercicio 8.

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de un hito fotográfico**.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Cálculo del giro | Ausente | Con errores | Correcto con unidades | Con sensibilidad a la latitud celeste |
| Atribución | Una persona | Dos | Todas con su rol | Con fuente primaria |
| Fuentes | Sin fuente | Con fuente | Con tipo y estado | Contrasta fuentes |
| Metadatos | Ausentes | Algunos | Los principales | Completos |

**Condiciones críticas:** no afirmar «el primero» sin matiz; citar solo lo consultado; no apuntar la cámara al Sol sin filtro certificado.

## 21. Ética, seguridad y límites

Los archivos de placas son patrimonio científico; su digitalización y acceso abierto (S2) es un ejemplo de ciencia abierta. No fotografíes el Sol sin filtros certificados (riesgo para la vista y el equipo). Accesibilidad: cálculos en texto, diagrama descrito, tablas equivalentes.

## 22. Para cerrar y seguir

La fotografía convirtió el cielo en un archivo y mostró lo que el ojo no ve, a costa de resolver el problema del seguimiento; los hitos se cuentan con cuidado de atribución. En C18 vemos cómo esta astronomía se asentó en Chile.

**Glosario español–inglés.** astrofotografía · *astrophotography*; daguerrotipo · *daguerreotype*; placa seca · *dry plate*; exposición · *exposure*; seguimiento · *tracking/guiding*; placa de vidrio · *glass plate*.

**Continuidad.** B02-C18 usa tu capacidad de **calcular efectos de la rotación** para situar la expansión de los observatorios en Chile. B28 retomará los detectores.

**Referencias:** ver sección 11. S1 es enciclopédica.

<!-- nav:bottom -->
---

[← Anterior: B02-C16 — Historia de la espectroscopía astronómica](../B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md) · [📚 Bloque B02](../../../tronco-comun/B02-historia-arqueoastronomia-y-culturas-del-cielo.md) · [Siguiente: B02-C18 — Expansión de la astronomía en Chile →](../B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md)
<!-- /nav -->
