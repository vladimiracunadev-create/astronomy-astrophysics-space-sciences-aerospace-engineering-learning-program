# Anexo P · Propulsión y cohetes a fondo

[⬅️ Anexo O](ANEXO-O-orbitas-y-trayectorias.md) · [Índice de anexos](README.md)

**Para qué sirve.** Responde tres preguntas que cualquier persona se hace ante un cohete: *¿cómo empuja si no hay aire?, ¿por qué hay motores tan distintos? y ¿qué se puede hacer con cada uno?* Complementa el [Anexo G](ANEXO-G-lanzadores-y-estaciones.md) (historia de los lanzadores) con la **física y el diseño de los motores**, y el [Anexo O](ANEXO-O-orbitas-y-trayectorias.md) (cuánto Δv se necesita) con **qué motor lo entrega**.

> **Estado del texto.** Síntesis propia con cifras redondeadas, pendiente de revisión disciplinar (nivel E0). Los empujes e impulsos específicos varían con la versión del motor y la altitud: confirma en la hoja técnica del fabricante. Comprueba los cálculos con la [calculadora](../herramientas/calculadora_cientifica.py).

---

## 1. La física en tres ideas

1. **Acción y reacción (momento):** el cohete expulsa masa hacia atrás a velocidad v_e y recibe un empuje igual hacia adelante. No necesita aire; en el vacío funciona mejor.
2. **Empuje:** F = ṁ v_e + (p_e − p_a) A_e, donde ṁ es el gasto de masa, v_e la velocidad de salida, p_e la presión en la salida de la tobera, p_a la ambiente y A_e el área de salida. El segundo término cambia con la altitud.
3. **Eficiencia:** el impulso específico Isp = F / (ṁ g₀) = v_e / g₀ (en segundos) mide cuánto empuje se obtiene por cada kilo de propelente que se gasta. A mayor Isp, menos propelente para el mismo Δv (ecuación del cohete).

**Ejercicio.** Un motor expulsa 300 kg/s a 3 000 m/s. ¿Empuje e Isp? *Solución:* F = 300 × 3 000 = **900 kN**; Isp = 3 000 / 9,81 ≈ **306 s**. Comprobación: `calc "3000/g0"`.

📘 [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial"), [B79](../programa/tronco-comun/B79-fluidos-termodinamica-y-aerotermodinamica-de-propulsion.md "Fluidos, termodinámica y aerotermodinámica de propulsión").

---

## 2. Cohetes químicos

Calientan y aceleran gases producto de una reacción química.

| Tipo | Propelentes | Isp vacío (s) | Ventajas | Inconvenientes |
|---|---|---|---|---|
| **Sólido** | Combustible y oxidante mezclados en una pasta | 250–290 | Simples, almacenables, gran empuje | No se pueden apagar ni regular |
| **Líquido, queroseno** | RP-1 y oxígeno líquido | 310–350 | Densos, baratos, buen empuje | Isp moderado; hollín |
| **Líquido, hidrógeno** | Hidrógeno y oxígeno líquidos | 440–460 | Mayor Isp químico | Hidrógeno poco denso: tanques enormes y fríos |
| **Líquido, metano** | Metano y oxígeno líquidos | 360–380 | Buen Isp, reutilizable, producible en Marte | Tecnología menos madura |
| **Hipergólico** | Hidracinas y tetróxido de nitrógeno | 300–335 | Encienden al contacto; ideales para maniobras | Tóxicos |
| **Híbrido** | Combustible sólido y oxidante líquido | 280–320 | Regulables y más seguros | Combustión menos eficiente |

### Anatomía de un motor líquido
1. **Tanques** de combustible y oxidante.
2. **Turbobombas** que inyectan el propelente a alta presión (en una cámara de ~100–300 bar).
3. **Cámara de combustión** (≈ 3 500 K en motores de hidrógeno-oxígeno).
4. **Tobera** en forma de campana que expande los gases y los convierte en velocidad.
5. **Refrigeración regenerativa:** el propio combustible rodea la cámara antes de quemarse.

### Ciclos de potencia
- **Generador de gas:** una parte del propelente alimenta la turbina y se descarta (sencillo; pierde Isp).
- **Combustión por etapas:** los gases de la turbina se queman en la cámara principal (más eficiente, más complejo).
- **Expansor:** el calor de la cámara mueve la turbina (para motores de hidrógeno de menor empuje).

### Algunos motores históricos y actuales (empuje al nivel del mar, aprox.)
| Motor | Empuje | Uso |
|---|---|---|
| F-1 | 6,8 MN | Primera etapa del Saturn V (cinco motores ≈ 34 MN) |
| RS-25 | 1,86 MN | Transbordador espacial y cohete SLS |
| Merlin 1D | 0,85 MN | Falcon 9 |
| Raptor | ≈ 2,3 MN | Starship |

### La tobera y la altitud
Una tobera con área de salida grande es óptima en el vacío, pero al nivel del mar el flujo se separa de la pared y puede dañar el motor. Por eso las **etapas superiores** usan toberas largas y las primeras etapas, cortas; algunos diseños usan toberas con extensión desplegable.

📘 [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial"), [B79](../programa/tronco-comun/B79-fluidos-termodinamica-y-aerotermodinamica-de-propulsion.md "Fluidos, termodinámica y aerotermodinámica de propulsión").

---

## 3. Propulsión eléctrica

Aceleran un propelente (casi siempre xenón) con campos eléctricos.

| Tipo | Cómo acelera | Isp (s) | Empuje | Uso |
|---|---|---|---|---|
| **Iónico (rejillas)** | Campo eléctrico entre rejillas | 2 500–4 000 | 20–250 mN | Sondas de espacio profundo (Dawn) |
| **Hall** | Campo magnético y eléctrico en un canal anular | 1 500–2 500 | 10–1 000 mN | Mantenimiento de satélites, constelaciones |
| **Magnetoplasmadinámico** | Corriente intensa en plasma | 2 000–5 000 | Alto, con mucha potencia | Experimental |

**Relación potencia-empuje:** P = F v_e / (2η). Es decir, el empuje está limitado por la **potencia eléctrica** disponible.

**Ejercicio.** ¿Qué potencia necesita un motor iónico de 90 mN y Isp 3 000 s con eficiencia 60 %? *Solución:* v_e = 3 000 × 9,81 = 29 430 m/s; P = 0,09 × 29 430 / (2 × 0,6) ≈ **2,2 kW**. Esto exige ≈ 5,5 m² de paneles a 1 UA (≈ 400 W/m²). Comprobación: `calc "0.09*3000*g0/(2*0.6)"`.

**Cuándo conviene.** Para misiones largas y suaves: gasta muy poco propelente (ecuación del cohete) pero tarda meses. Una sonda de 1 000 kg con 90 mN gana ≈ 7,8 m/s por día (≈ 2,8 km/s al año).

📘 [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial").

---

## 4. Otras tecnologías

| Tecnología | Principio | Estado | Observación |
|---|---|---|---|
| **Nuclear térmico** | Un reactor calienta hidrógeno que se expulsa | Probado en tierra (programa NERVA, años 60) | Isp ≈ 800–900 s, duplica la eficiencia química |
| **Nuclear eléctrico** | Un reactor alimenta propulsión eléctrica | En estudio | Potencia alta para misiones lejanas |
| **Vela solar** | Presión de la radiación solar | Demostrada (IKAROS 2010, LightSail 2) | Fuerza ≈ 9 µN/m² para una vela reflectante a 1 UA |
| **Vela magnética o eléctrica** | Interacción con el viento solar | Concepto | Sin propelente |
| **Ascensor espacial** | Cable anclado a la Tierra | Teórico | Requiere materiales que no existen |
| **Cohetes de fusión o antimateria** | Altas energías | Conceptual | Fuera de alcance actual |

**Presión de radiación.** P = S / c = 1 361 / 3 × 10⁸ ≈ **4,5 µN/m²** (superficie absorbente); el doble si refleja. Una vela de 1 000 m² ejerce ≈ 9 mN: similar a un motor iónico pequeño, pero **sin gastar propelente**.

📘 [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial").

---

## 5. Del motor al presupuesto de Δv

Cuánto Δv requiere cada meta (valores aproximados, desde una órbita baja de 300 km, sin pérdidas):

| Meta | Δv (km/s) |
|---|---|
| Alcanzar LEO desde la superficie | ≈ 9,4 |
| Órbita de transferencia geoestacionaria (desde LEO) | ≈ 2,4 |
| Geoestacionaria completa (desde LEO) | ≈ 3,9 |
| Inyección translunar (TLI) | ≈ 3,1 |
| Captura en órbita lunar | ≈ 0,9 |
| Alunizaje desde órbita lunar | ≈ 1,9 |
| Inyección hacia Marte (desde LEO) | ≈ 3,6 |
| Escapar del Sol desde la órbita terrestre (velocidad extra respecto de la Tierra, sin contar salir de su gravedad) | ≈ 12,3 |

**Cómo se usa.** Se suman los Δv de las fases y se calcula la masa de propelente con la ecuación del cohete, fase a fase, empezando por la última.

**Ejercicio de etapas.** Una nave debe dar 3,1 km/s (TLI) con un motor de Isp = 450 s y una masa final (carga + estructura) de 5 000 kg. ¿Cuánto propelente? *Solución:* m₀/m_f = e^(3100/(450·9,81)) = e^0,702 ≈ 2,02; m₀ ≈ 10 100 kg; propelente ≈ **5 100 kg**. Comprobación: `calc "5000*(exp(3100/(450*g0))-1)"`.

📘 [B77](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md "Dinámica de lanzamiento y reentrada"), [B78](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md "Tecnologías de propulsión espacial"), [B75](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias").

---

## 6. Seguridad y límites

- **Propelentes peligrosos:** criogénicos (hidrógeno, oxígeno), tóxicos (hidracina), explosivos (sólidos).
- **Fallos de motor:** inestabilidad de la combustión, fugas, fallos de turbobomba. La mayoría de los fallos de lanzamiento tuvo origen en propulsión.
- **Sólidos:** una vez encendidos no se pueden apagar; el fallo de uno de ellos fue la causa del [accidente del Challenger](ANEXO-J-estudios-de-caso-a-fondo.md).
- **Sostenibilidad:** hay debate sobre las emisiones del transporte espacial (alúmina de sólidos, hollín de queroseno, vapor de agua en la alta atmósfera).

📘 [B110](../programa/tronco-comun/B110-emergencias-y-seguridad-de-tripulacion.md "Emergencias y seguridad de tripulación"), [B84](../programa/tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md "Estructuras, materiales y fabricación espacial").

---

## 7. Preguntas para estudiar

1. ¿Por qué un motor iónico no puede despegar de la Tierra, aunque tenga un Isp altísimo?
2. ¿Por qué el hidrógeno tiene mayor Isp pero se usa poco en primeras etapas?
3. ¿Qué pasa con el empuje de un motor al subir en la atmósfera?
4. ¿En qué misión elegirías propulsión eléctrica y en cuál química?
5. ¿Por qué se calcula el propelente empezando por la última etapa?

[⬅️ Anexo O](ANEXO-O-orbitas-y-trayectorias.md) · [Índice de anexos](README.md)
