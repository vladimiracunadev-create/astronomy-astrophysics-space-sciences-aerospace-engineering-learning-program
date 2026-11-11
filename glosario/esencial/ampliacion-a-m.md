# Glosario esencial (ampliación) · A – M

[⬅️ Índice del glosario esencial](README.md) · [Glosario completo](../README.md)

Ampliación centrada en ingeniería, operaciones y entorno espacial. Mismo esquema: **en una frase**, **cómo pensarlo**, **fórmula y unidades**, **ejemplo con números**, **error frecuente**, **relacionados**. Valores redondeados y orientativos.

---

### Aerofrenado

**En una frase.** Maniobra que usa el roce con la parte alta de la atmósfera de un planeta para reducir la velocidad de una sonda y bajar su órbita sin gastar combustible.

**Cómo pensarlo.** En cada pasada por el periapsis la sonda roza el aire y pierde un poco de energía; el apoapsis baja poco a poco. Se repite durante meses, con cuidado para no sobrecalentar los paneles. Se ahorra del orden de cientos de kilogramos de propelente a cambio de tiempo y de un riesgo térmico y operativo.

**Ejemplo.** Mars Global Surveyor, Mars Odyssey, Mars Reconnaissance Orbiter y ExoMars TGO llegaron a su órbita científica con aerofrenado.

**Error frecuente.** Confundirlo con la reentrada: la sonda no desciende a la superficie, solo roza la atmósfera superior.

**Relacionados:** arrastre atmosférico, periapsis, delta-v.
📘 [B77](../../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B75](../../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias").

---

### Agujero negro

**En una frase.** Región del espacio-tiempo de la que nada, ni la luz, puede escapar, delimitada por el horizonte de sucesos.

**Cómo pensarlo.** Si una masa se comprime dentro de su radio de Schwarzschild, la velocidad de escape supera a *c*. El horizonte no es una superficie material, sino un límite de no retorno. Se detecta por su efecto gravitacional (órbitas, ondas gravitacionales) o por el gas que lo rodea.

**Fórmula.** r_s = 2GM / c² ≈ 2,95 km × (M / M☉).

**Ejemplo.** Un agujero de 10 M☉: r_s ≈ 30 km. Sagitario A* (≈ 4,3 × 10⁶ M☉): r_s ≈ 1,3 × 10⁷ km ≈ 0,085 UA. M87* (≈ 6,5 × 10⁹ M☉): ≈ 128 UA.

**Error frecuente.** Imaginarlo como un "aspirador": a gran distancia, su gravedad es la de cualquier masa igual.

**Relacionados:** relatividad general, estrella de neutrones, ondas gravitacionales.
📘 [B27](../../programa/tronco-comun/B27-objetos-compactos-y-altas-energias.md "Objetos compactos y altas energías"), [B39](../../programa/tronco-comun/B39-relatividad-general-avanzada.md "Relatividad general avanzada").

---

### Ancho de banda y capacidad de un canal

**En una frase.** El ancho de banda (B) es el rango de frecuencias que ocupa una señal; con la relación señal-ruido fija el máximo de datos que se puede transmitir.

**Cómo pensarlo.** Más ancho de banda y menos ruido permiten más bits por segundo. Shannon demostró que hay un límite teórico que ningún código puede superar.

**Fórmula.** C = B log₂(1 + SNR). Unidades: bit/s (B en Hz, SNR lineal).

**Ejemplo.** B = 1 MHz, SNR = 15 (11,8 dB): C = 10⁶ · log₂(16) = **4 Mbit/s**.

**Error frecuente.** Dar la SNR en dB dentro de la fórmula: hay que convertirla a lineal (SNR = 10^(dB/10)).

**Relacionados:** decibelio, balance de enlace, codificación.
📘 [B94](../../programa/tronco-comun/B94-modulacion-codificacion-y-protocolos-de-enlace.md "Modulación, codificación y protocolos de enlace"), [B89](../../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital").

---

### Arrastre atmosférico

**En una frase.** Fuerza de frenado que ejerce el aire residual sobre un satélite en órbita baja.

**Cómo pensarlo.** Aun a 400 km queda aire muy tenue; a 7,7 km/s ese roce se acumula, baja la órbita y, si no se corrige, termina en reentrada. La densidad varía varios órdenes de magnitud con la actividad solar.

**Fórmula.** F = ½ ρ v² C_d A. Unidades: N (ρ en kg/m³, A en m²).

**Ejemplo.** ρ = 3 × 10⁻¹² kg/m³, v = 7 670 m/s, C_d = 2,2, A = 1 m²: F ≈ 1,9 × 10⁻⁴ N; en un satélite de 100 kg, a ≈ 1,9 × 10⁻⁶ m/s².

**Error frecuente.** Despreciarlo porque "no hay aire" en el espacio.

**Relacionados:** perturbación orbital, reentrada, ciclo solar.
📘 [B72](../../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md "Perturbaciones y evolución de órbitas"), [B118](../../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md "Tráfico espacial y sostenibilidad orbital").

---

### Basura espacial y síndrome de Kessler

**En una frase.** La basura espacial son objetos artificiales sin función en órbita; el síndrome de Kessler es una reacción en cadena de colisiones que aumentaría su cantidad.

**Cómo pensarlo.** A velocidades relativas de hasta ≈ 15 km/s, un fragmento de un centímetro tiene la energía de una granada. Cada choque genera más fragmentos, que causan más choques. El riesgo crece en altitudes donde hay mucha población de objetos.

**Ejemplo.** En 2009 chocaron el satélite Iridium 33 y el Kosmos 2251; en 2007 y 2021 pruebas antisatélite generaron miles de fragmentos rastreables.

**Error frecuente.** Pensar que "el espacio es enorme" y no hay riesgo: las órbitas útiles son capas estrechas y muy usadas.

**Relacionados:** tráfico espacial, mitigación, órbita cementerio.
📘 [B118](../../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md "Tráfico espacial y sostenibilidad orbital"), [B119](../../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md "Derecho, seguridad y geopolítica espacial").

---

### Constelación satelital

**En una frase.** Conjunto coordinado de satélites que juntos dan cobertura continua.

**Cómo pensarlo.** Un satélite en órbita baja ve una región pequeña y pasa rápido; para cubrir todo el planeta sin interrupción se necesitan muchos, repartidos en planos orbitales. A cambio, la latencia es baja (decenas de milisegundos) frente a la de un satélite geoestacionario (≈ 0,5 s entre emisor y receptor, pasando por el satélite).

**Ejemplo.** Una constelación de altura 550 km: señal ida y vuelta mínima 2 · 550 km / c ≈ 3,7 ms. En órbita geoestacionaria: 2 · 35 786 km / c ≈ 239 ms solo de propagación.

**Error frecuente.** Olvidar que más satélites aumenta la complejidad de coordinación, el riesgo de colisión y la contaminación lumínica.

**Relacionados:** latencia, GEO, tráfico espacial.
📘 [B89](../../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital"), [B118](../../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md "Tráfico espacial y sostenibilidad orbital"), [B120](../../programa/tronco-comun/B120-espectro-licencias-y-regulacion-satelital.md "Espectro, licencias y regulación satelital").

---

### Contaminación lumínica

**En una frase.** Luz artificial excesiva que aclara el cielo nocturno y oculta los astros.

**Cómo pensarlo.** Es luz hacia arriba o dispersa que se suma al brillo natural del cielo. Reduce el contraste de objetos débiles, afecta a la fauna y al ciclo de sueño y exige proteger los observatorios con normas de iluminación.

**Ejemplo.** Un cielo oscuro natural ≈ 21,9 mag/arcsec²; el de una ciudad ≈ 18: es ≈ 40 veces más brillante.

**Error frecuente.** Creer que sólo importa la cantidad de luz: importan su dirección y su color (el azul se dispersa más).

**Relacionados:** brillo superficial, escala de Bortle, observatorio.
📘 [B48](../../programa/tronco-comun/B48-operaciones-de-observatorios-cientificos.md "Operaciones de observatorios científicos"), [B130](../../programa/tronco-comun/B130-comunicacion-y-divulgacion-cientifica.md "Comunicación y divulgación científica").

---

### Control térmico

**En una frase.** Diseño y operación que mantiene cada parte de una nave dentro de su rango de temperatura.

**Cómo pensarlo.** En el vacío no hay convección: el calor se intercambia solo por radiación y conducción. La temperatura de equilibrio depende de cuánto absorbe (α) y cuánto emite (ε) la superficie. Se usan mantas aislantes, radiadores, pinturas, calentadores y tuberías de calor.

**Fórmula.** Esfera aislada: T = [α S / (4 ε σ)]^¼. Unidades: K.

**Ejemplo.** α/ε = 1 y S = 1 361 W/m²: T ≈ 278 K (5 °C). Con un recubrimiento de α/ε = 0,25, T ≈ 197 K (−76 °C).

**Error frecuente.** Olvidar los eclipses y la disipación interna de la electrónica.

**Relacionados:** cuerpo negro, albedo, radiador.
📘 [B85](../../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md "Gestión térmica y entorno espacial").

---

### Decibelio (dB)

**En una frase.** Unidad logarítmica que expresa razones de potencia.

**Cómo pensarlo.** Convierte multiplicaciones en sumas, lo cual es cómodo cuando las razones abarcan muchos órdenes de magnitud (señales de potencia casi nula frente a la transmitida). +3 dB ≈ ×2; +10 dB = ×10; +20 dB = ×100.

**Fórmula.** dB = 10 log₁₀(P₂/P₁) (potencias); 20 log₁₀ para tensiones o amplitudes.

**Ejemplo.** Una señal que cae de 100 W a 1 µW perdió 10 log₁₀(10⁸) = **80 dB**.

**Error frecuente.** Sumar dB y vatios en la misma cuenta, o usar 10 en vez de 20 para amplitudes.

**Relacionados:** balance de enlace, ganancia de antena, señal-ruido.
📘 [B89](../../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital"), [B91](../../programa/tronco-comun/B91-antenas-y-propagacion-para-enlaces-espaciales.md "Antenas y propagación para enlaces espaciales").

---

### Dosis de radiación (gray y sievert)

**En una frase.** El gray (Gy) mide la energía absorbida por kilogramo; el sievert (Sv) pondera esa dosis según el daño biológico.

**Cómo pensarlo.** No toda radiación daña igual: los iones pesados son más dañinos que los fotones. El factor de ponderación convierte gray en sievert. En el espacio hay tres fuentes: rayos cósmicos galácticos, partículas de erupciones solares y cinturones de Van Allen.

**Ejemplo.** Radiación natural en la Tierra ≈ 2,4 mSv/año. En la ISS ≈ 0,5 mSv/día. En tránsito a Marte se midió ≈ 1,8 mSv/día; en la superficie marciana ≈ 0,64 mSv/día.

**Error frecuente.** Confundir gray con sievert, o comparar la dosis de un examen puntual con la dosis acumulada.

**Relacionados:** rayos cósmicos, protección radiológica, ALARA.
📘 [B112](../../programa/tronco-comun/B112-radiobiologia-y-proteccion-radiologica-espacial.md "Radiobiología y protección radiológica espacial"), [B33](../../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md "Clima espacial: impactos, pronóstico y riesgo").

---

### Eclipse

**En una frase.** Oscurecimiento de un astro porque otro se interpone o porque entra en su sombra.

**Cómo pensarlo.** En un eclipse **solar** la Luna se interpone entre el Sol y la Tierra; en uno **lunar**, la Tierra proyecta su sombra sobre la Luna. El Sol es ≈ 400 veces mayor que la Luna y está ≈ 400 veces más lejos: por eso los discos se ven casi iguales y hay eclipses totales. Los satélites también pasan por eclipses de la Tierra, con consecuencias térmicas y de energía.

**Ejemplo.** La totalidad de un eclipse solar dura como máximo ≈ 7 min 32 s. Un satélite en órbita baja puede pasar hasta unos 35 de cada 92 minutos en sombra.

**Error frecuente.** Pensar que hay eclipse solar cada mes: la órbita lunar está inclinada ≈ 5° y solo se alinea en ciertas fechas.

**Relacionados:** nodos orbitales, sombra, ciclo de energía.
📘 [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica"), [B86](../../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md "Sistemas de potencia y energía espacial").

---

### Energía solar espacial (paneles fotovoltaicos)

**En una frase.** Producción de electricidad a bordo con celdas que convierten la luz solar.

**Cómo pensarlo.** La potencia disponible es el flujo solar por el área y la eficiencia, y cae como 1/d² al alejarse del Sol. Más allá de Júpiter es inviable y se usan generadores de radioisótopos.

**Fórmula.** P = S · A · η · cos θ. Unidades: W.

**Ejemplo.** A 1 UA con η = 30 %: ≈ 400 W/m². A 5,2 UA (Júpiter): ≈ 15 W/m². La sonda Juno usa ≈ 60 m² de paneles y obtiene cerca de 500 W en Júpiter.

**Error frecuente.** Olvidar la degradación por radiación y por la inclinación de los paneles.

**Relacionados:** potencia, RTG, batería.
📘 [B86](../../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md "Sistemas de potencia y energía espacial").

---

### Filtro de Kalman

**En una frase.** Algoritmo que combina un modelo de predicción con mediciones ruidosas para estimar un estado con la menor incertidumbre posible.

**Cómo pensarlo.** Predices dónde está la nave, mides y comparas. La *ganancia* decide cuánto fiarse de la medición frente al modelo: si la medición es muy ruidosa, se confía en el modelo. Así se obtiene una estimación mejor que cada fuente por separado. Es la base de la navegación de naves y de los GPS.

**Fórmula (escalar).** K = P / (P + R); x̂ = x̂⁻ + K (z − x̂⁻), con P la incertidumbre del modelo y R la del sensor.

**Ejemplo.** P = 4 y R = 1: K = 0,8, se confía en la medición al 80 %. Con P = 1 y R = 4: K = 0,2.

**Error frecuente.** Suponer ruido gaussiano sin comprobarlo, o fijar mal las covarianzas.

**Relacionados:** estimación de órbita, navegación inercial, mínimos cuadrados.
📘 [B74](../../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md "Estimación de órbitas y navegación espacial"), [B80](../../programa/tronco-comun/B80-navegacion-inercial-y-fusion-multisensorial.md "Navegación inercial y fusión multisensorial"), [B22](../../programa/tronco-comun/B22-problemas-inversos-y-estimacion-de-modelos.md "Problemas inversos y estimación de modelos").

---

### Geoestacionaria (órbita)

**En una frase.** Órbita circular ecuatorial con período igual al de rotación de la Tierra, de modo que el satélite parece fijo sobre un punto.

**Cómo pensarlo.** A una sola altura el período orbital coincide con el sidéreo (23 h 56 min 4 s). Sirve para comunicaciones y meteorología porque la antena apunta fija. Cada satélite necesita su "espacio" para no interferir.

**Fórmula.** r = (GM T² / 4π²)^(1/3).

**Ejemplo.** r = 42 164 km, altitud 35 786 km, v = 3,07 km/s. Dos satélites separados 2° se hallan a ≈ 1 470 km uno de otro.

**Error frecuente.** Creer que el satélite "no se mueve": orbita a 3 km/s; sólo está quieto respecto del suelo.

**Relacionados:** período sidéreo, ranuras orbitales, UIT.
📘 [B71](../../programa/tronco-comun/B71-mecanica-orbital-fundamental.md "Mecánica orbital fundamental"), [B120](../../programa/tronco-comun/B120-espectro-licencias-y-regulacion-satelital.md "Espectro, licencias y regulación satelital").

---

### Heliosíncrona (órbita)

**En una frase.** Órbita casi polar cuyo plano gira con el Sol, de modo que el satélite pasa siempre a la misma hora local.

**Cómo pensarlo.** El achatamiento terrestre (J₂) hace precesar el plano orbital. Con la inclinación adecuada (≈ 98° a 700–800 km) esa precesión es 0,9856° por día, igual a lo que el Sol "avanza" en el cielo. Así las imágenes se toman con iluminación comparable cada vez.

**Ejemplo.** Landsat y Sentinel-2 cruzan el ecuador a las ≈ 10:30 hora local.

**Error frecuente.** Pensar que "sincronizada con el Sol" significa fija respecto de él.

**Relacionados:** J₂, precesión, observación de la Tierra.
📘 [B72](../../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md "Perturbaciones y evolución de órbitas"), [B57](../../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md "Observación terrestre y geociencias orbitales").

---

### Ionosfera

**En una frase.** Capas de la atmósfera superior (≈ 60–1 000 km) donde el gas está parcialmente ionizado.

**Cómo pensarlo.** La radiación solar ioniza el gas y crea electrones libres que reflejan ondas cortas (permitiendo comunicaciones lejanas) y retrasan las señales de satélites. El retraso depende del contenido total de electrones (TEC) y de la frecuencia.

**Fórmula.** Retraso ≈ 40,3 · TEC / f². Unidades: m (TEC en electrones/m², f en Hz).

**Ejemplo.** TEC = 5 × 10¹⁷ el/m² (50 TECU) y f = 1,575 GHz (GPS L1): retraso ≈ 8 m. Por eso los receptores usan dos frecuencias.

**Error frecuente.** Confundir ionosfera con la capa de ozono o con la estratosfera.

**Relacionados:** clima espacial, navegación por satélite, auroras.
📘 [B33](../../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md "Clima espacial: impactos, pronóstico y riesgo"), [B89](../../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md "Comunicaciones y navegación satelital").

---

### Latencia

**En una frase.** El tiempo que tarda una señal en llegar de un punto a otro.

**Cómo pensarlo.** La luz viaja a una velocidad finita, por eso hay demoras que ninguna tecnología evita. En misiones lejanas obliga a la autonomía: no se puede manejar un rover a control remoto.

**Ejemplo.** Luna: 1,28 s por trayecto. Marte: de 3 a 22 minutos según su posición. Voyager 1: más de 22 horas.

**Error frecuente.** Confundir latencia con ancho de banda: una conexión puede ser rápida (alta tasa) pero con gran demora.

**Relacionados:** autonomía, teleoperación, operaciones.
📘 [B98](../../programa/tronco-comun/B98-autonomia-y-teleoperacion-espacial.md "Autonomía y teleoperación espacial"), [B96](../../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md "Control y operación de misiones espaciales").

---

### Límite de Roche

**En una frase.** Distancia dentro de la cual las fuerzas de marea de un cuerpo desintegran a un satélite sostenido solo por su gravedad.

**Cómo pensarlo.** La diferencia de gravedad entre el lado cercano y el lejano estira al satélite. Si supera la atracción interna, se rompe. Explica los anillos de los planetas gigantes.

**Fórmula (fluido).** d ≈ 2,44 R_p (ρ_p / ρ_s)^⅓.

**Ejemplo.** Saturno (ρ = 687 kg/m³, R = 60 268 km) y partículas de hielo (ρ ≈ 900): d ≈ 2,23 R_p ≈ 134 000 km; los anillos principales terminan cerca de esa distancia.

**Error frecuente.** Pensar que un cuerpo sólido pequeño se destruye: la cohesión del material ayuda a resistir.

**Relacionados:** marea, anillos, esfera de Hill.
📘 [B52](../../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B73](../../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md "Mecánica celeste, resonancias y caos").

---

### Margen de diseño

**En una frase.** Reserva deliberada entre lo que un sistema necesita y lo que puede entregar.

**Cómo pensarlo.** Al inicio de un proyecto se desconocen masas, consumos y rendimientos reales; el margen protege contra esas incertidumbres. Suele ser grande al principio (20–30 %) y se va reduciendo según maduran los datos.

**Ejemplo.** Si el presupuesto de masa de un satélite es 100 kg y el diseño preliminar pesa 80 kg, el margen es 25 % respecto de lo estimado.

**Error frecuente.** Gastar el margen "porque está disponible"; los márgenes son para lo imprevisto.

**Relacionados:** presupuesto de masa y potencia, TRL, riesgo.
📘 [B83](../../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md "Ingeniería de sistemas y diseño de misiones").

---

### Marea

**En una frase.** Deformación de un cuerpo por la diferencia de gravedad de otro entre sus partes.

**Cómo pensarlo.** La fuerza de marea depende de M/d³, no de M/d²; por eso la Luna, aunque tiene mucha menos masa que el Sol, produce una marea ≈ 2,2 veces mayor. Las mareas frenan la rotación terrestre, alejan la Luna ≈ 3,8 cm por año y calientan lunas como Ío.

**Fórmula.** Aceleración de marea ≈ 2GM r / d³.

**Ejemplo.** Ío recibe un calentamiento por mareas que genera cientos de volcanes activos.

**Error frecuente.** Creer que las mareas oceánicas dependen del Sol y la Luna por igual: la Luna domina.

**Relacionados:** límite de Roche, resonancia orbital, vulcanismo.
📘 [B52](../../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md "Formación y dinámica de sistemas planetarios"), [B70](../../programa/tronco-comun/B70-vulcanismo-planetario.md "Vulcanismo planetario").

---

[← M – Z del glosario esencial](esencial-m-z.md) · [Índice](README.md) · [Siguiente: ampliación N – Z →](ampliacion-n-z.md)
