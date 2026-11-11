# Anexo O · Órbitas y trayectorias: guía conceptual con números

[⬅️ Anexo N](ANEXO-N-exoplanetas-y-astrobiologia.md) · [Índice de anexos](README.md)

**Para qué sirve.** Es el anexo que conecta la intuición con las fórmulas de mecánica orbital: por qué existen tipos de órbitas distintos, qué elegir según la misión y cuánto cuesta cambiar de una a otra. Está pensado para leerse **antes** de los bloques B71 a B77 y para consultarse después como mapa.

> **Estado del texto.** Síntesis propia con cifras redondeadas, pendiente de revisión disciplinar (nivel E0). Los cálculos suponen el problema de dos cuerpos, órbitas ideales e impulsos instantáneos, salvo que se indique otra cosa; no sirven para planificar maniobras reales. Comprueba cada número con la [calculadora](../herramientas/calculadora_cientifica.py).

---

## 1. La idea en una página

Una órbita es una **caída continua**: el cuerpo avanza tan rápido de lado que, mientras cae hacia el planeta, el planeta «se curva» bajo él. De esa idea salen tres consecuencias:

1. **Velocidad y altura van juntas:** a más altura, menor velocidad y mayor período.
2. **Para cambiar de órbita hay que cambiar la velocidad** (con un impulso), no «empujar» en la dirección deseada.
3. **Cambiar de órbita cuesta combustible (Δv):** el presupuesto de Δv decide qué misiones son posibles.

### Las seis cantidades que describen una órbita

| Símbolo | Nombre | Qué dice |
|---|---|---|
| a | Semieje mayor | Tamaño de la elipse; fija el período |
| e | Excentricidad | Forma: 0 círculo, <1 elipse |
| i | Inclinación | Cuánto se inclina respecto del ecuador |
| Ω | Ascensión del nodo ascendente | Orientación del plano en el espacio |
| ω | Argumento del periapsis | Hacia dónde apunta la elipse en su plano |
| ν | Anomalía verdadera | Dónde está el cuerpo en la elipse ahora |

📘 [B71](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental").

---

## 2. Los tipos de órbita y para qué sirve cada uno

| Órbita | Altura típica | Período | Para qué se usa | Por qué ahí |
|---|---|---|---|---|
| **LEO** (baja) | 300–2 000 km | 90–127 min | ISS, observación, constelaciones | Cerca (poco Δv, buena resolución, baja latencia) |
| **MEO** (media) | 2 000–35 000 km | 2–24 h | Navegación (GPS ≈ 20 200 km) | Cobertura global con pocos satélites |
| **GEO** (geoestacionaria) | 35 786 km | 23 h 56 min | Comunicaciones, meteorología | Parece fija sobre un punto |
| **SSO** (heliosíncrona) | 600–800 km, i ≈ 98° | ≈ 100 min | Observación de la Tierra | Siempre pasa a la misma hora solar |
| **Molniya** | Perigeo ≈ 500 km, apogeo ≈ 40 000 km, i = 63,4° | 12 h | Comunicaciones en altas latitudes | Permanece horas sobre el hemisferio norte |
| **HEO / Tundra** | Muy elíptica | 24 h | Cobertura regional en altas latitudes | Pasa mucho tiempo en el apogeo |
| **Órbitas lunares y halo** | Alrededor de L1/L2 | Variable | Observatorios, relevos | Puntos de equilibrio gravitatorio |

### Por qué la geoestacionaria está a 35 786 km
Se pide un período igual al día sidéreo (86 164 s). De T = 2π √(a³/GM) se obtiene a = (GM T² / 4π²)^⅓ = 42 164 km del centro (35 786 km de altura). Solo hay un valor que cumple la condición.

### Por qué la órbita heliosíncrona tiene ~98° de inclinación
El achatamiento de la Tierra (J₂) hace girar el plano orbital. Con i ≈ 98° la rotación del plano es 0,9856° al día, igual al avance del Sol en el cielo. Resultado: las imágenes se toman siempre a la misma hora local, con sombras comparables.

### Por qué Molniya tiene 63,4°
A esa inclinación la rotación del argumento del periapsis por J₂ se anula, y el apogeo permanece sobre el mismo hemisferio.

**Ejercicio.** Calcula el radio de la órbita geoestacionaria. *Solución:* (3,986 × 10¹⁴ × 86 164² / (4π²))^⅓ ≈ **4,216 × 10⁷ m**. Comprobación: `calc "(GM_tierra*86164**2/(4*pi**2))**(1/3)"`.

📘 [B71](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B72](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md "Perturbaciones y evolución de órbitas"), [B89](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital").

---

## 3. Velocidades que conviene memorizar

| Situación | Velocidad | Cómo se obtiene |
|---|---|---|
| Órbita circular a 400 km (ISS) | 7,67 km/s | √(GM / r) |
| Velocidad circular en la superficie terrestre (ideal) | 7,91 km/s | √(GM / R) |
| Velocidad de escape desde la superficie | 11,19 km/s | √2 × la circular |
| Órbita geoestacionaria | 3,07 km/s | √(GM / r) con r = 42 164 km |
| Órbita de la Luna | 1,02 km/s | √(GM / 384 400 km) |
| Tierra alrededor del Sol | 29,8 km/s | √(GM☉ / 1 UA) |
| Velocidad de escape del Sol (a 1 UA) | 42,1 km/s | √2 × la circular |

**Lección:** el escape siempre es √2 veces la velocidad circular a la misma distancia.

---

## 4. Cambiar de órbita: el costo en Δv

### 4.1 Transferencia de Hohmann
Entre dos órbitas circulares coplanares, la transferencia de menor energía usa dos impulsos sobre una elipse que toca ambas.

| Maniobra | Δv₁ (km/s) | Δv₂ (km/s) | Total | Tiempo |
|---|---|---|---|---|
| LEO (400 km) → GEO | 2,43 | 1,47 | ≈ 3,9 km/s | ≈ 5,3 h |
| Tierra → Marte (heliocéntrico, aprox.) | 2,9 | 2,6 | ≈ 5,6 km/s relativo a las órbitas planetarias | ≈ 259 d |

Para la Tierra a LEO, a estas cifras hay que sumar el costo de llegar a LEO (≈ 9,4 km/s).

### 4.2 Cambio de plano
Girar el plano orbital un ángulo Δi cuesta Δv = 2 v sen(Δi/2). Es **muy caro** a velocidades altas:

- Cambiar 28,5° (Cabo Cañaveral) a 0° (ecuatorial) en LEO (v = 7,67 km/s): Δv = 2 × 7,67 × sen(14,25°) ≈ **3,78 km/s**.
- Hacerlo en GEO (v = 3,07 km/s): ≈ **1,51 km/s**.
- Por eso se combina con otra maniobra y se hace donde la velocidad es menor.

### 4.3 Transferencia bielíptica
Para razones de radios grandes (> 11,94) puede costar menos que Hohmann, pero tarda mucho más.

### 4.4 Asistencia gravitatoria
En lugar de gastar combustible, una nave utiliza el movimiento de un planeta para cambiar su velocidad heliocéntrica. Ver el [caso de Voyager 2](ANEXO-J-estudios-de-caso-a-fondo.md).

### 4.5 Ejercicios
1. Calcula el Δv total de una transferencia Hohmann LEO (6 678 km) → GEO. *Solución:* ≈ **3,89 km/s**. Comprobación: `hohmann --r1 6678e3 --r2 42164e3`.
2. ¿Cuánto cuesta cambiar 10° de plano en LEO? *Solución:* 2 × 7,67 × sen 5° ≈ **1,34 km/s**. Comprobación: `calc "2*7.67*sin(radians(5))"`.
3. ¿Por qué se prefiere lanzar desde Kourou (5° N) para ir a GEO? *Respuesta:* porque el cambio de plano que falta es menor (5° vs 28,5°) y la rotación terrestre aporta más velocidad.

📘 [B71](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B75](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias"), [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B82](../programa/tronco-comun/B82-problema-de-lambert-y-transferencias-de-dos-puntos.md "Problema de Lambert y transferencias de dos puntos").

---

## 5. Lo que desvía una órbita real

| Perturbación | Origen | Efecto | Quién la sufre más |
|---|---|---|---|
| **J₂** (achatamiento) | La Tierra no es esférica | Giro del plano y del periapsis | Órbitas bajas |
| **Arrastre atmosférico** | Aire residual | Baja la órbita | < 600 km |
| **Presión de radiación solar** | Fotones del Sol | Empuje suave | Satélites ligeros con paneles grandes |
| **Tercer cuerpo** | Sol y Luna | Cambios lentos de inclinación y excentricidad | Órbitas altas (GEO) |
| **Mareas y campo irregular** | Distribución de masa | Pequeñas derivas | Todas |

**Mantenimiento en estación (GEO):** el satélite deriva en longitud y en inclinación (≈ 0,8° al año por Sol y Luna); consume ≈ 50 m/s al año de Δv, que define su vida útil.

**Reentrada natural:** un satélite en LEO a 400 km con alto arrastre puede tardar años; a 300 km, meses.

📘 [B72](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md "Perturbaciones y evolución de órbitas"), [B118](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md "Tráfico espacial y sostenibilidad orbital").

---

## 6. Problemas de tres cuerpos y puntos de Lagrange

Cuando hay dos cuerpos masivos (Tierra-Sol) y uno pequeño (una nave) aparecen cinco puntos donde el pequeño permanece en reposo respecto de los dos:

- **L1 (Sol-Tierra, ≈ 1,5 millones de km hacia el Sol):** vigilancia solar (SOHO).
- **L2 (≈ 1,5 millones de km del lado opuesto):** telescopios (Webb, Gaia).
- **L3:** al otro lado del Sol (no se usa).
- **L4 y L5:** estables si la relación de masas es mayor que ≈ 25; asteroides troyanos de Júpiter.

L1, L2 y L3 son inestables: hace falta corregir la posición cada pocas semanas con pequeñas cantidades de combustible. Las **órbitas halo** alrededor de L1 y L2 evitan eclipses y se mantienen con poco Δv.

📘 [B73](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md "Mecánica celeste, resonancias y caos"), [B76](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md "Dinámica cislunar y operaciones de proximidad").

---

## 7. Cómo elegir una órbita: un método de cuatro preguntas

1. **¿Qué necesito ver o cubrir?** (todo el globo, una región, un punto fijo, el Sol).
2. **¿Con qué resolución y latencia?** (más bajo = más detalle y menor retardo).
3. **¿Cuánta vida útil y cuánto Δv tengo?** (arrastre, estación).
4. **¿Qué restricciones de seguridad y normativa aplican?** (basura espacial, desorbitado en 25 años, espectro).

**Ejercicio de diseño.** Elige una órbita para (a) un satélite que cartografía la vegetación de Chile cada pocos días, (b) un satélite de telecomunicaciones para toda Sudamérica, (c) un observatorio solar continuo. *Respuestas posibles:* (a) SSO a ≈ 700 km; (b) GEO sobre el ecuador; (c) halo en L1.

📘 [B57](../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md "Observación terrestre y geociencias orbitales"), [B71](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B83](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md "Ingeniería de sistemas y diseño de misiones"), [B118](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md "Tráfico espacial y sostenibilidad orbital").

---

## 8. Preguntas para estudiar

1. ¿Por qué los astronautas «flotan» si la gravedad a 400 km es casi la de la superficie?
2. ¿Qué pasa con la velocidad de un satélite si se le da un impulso en la dirección del movimiento? (Sube de órbita y *disminuye* la velocidad media.)
3. ¿Por qué un cambio de plano es caro en LEO y más barato en GEO?
4. ¿Cuándo tiene sentido pagar tiempo para ahorrar Δv?

[⬅️ Anexo N](ANEXO-N-exoplanetas-y-astrobiologia.md) · [Índice de anexos](README.md)
