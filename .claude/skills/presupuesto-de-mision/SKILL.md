---
name: presupuesto-de-mision
description: Construye un presupuesto de misión con márgenes: delta-v y masa por la ecuación del cohete, energía/potencia, enlace y datos, y consumibles de tripulación, con la calculadora del repositorio. Úselo para dimensionar y comprobar si «cierra» una misión o un CubeSat.
---

# Presupuesto de misión

1. Enumere fases y maniobras (salida, correcciones, captura, aterrizaje, regreso) con su delta-v (`planificador_de_misiones.py`, `calculadora_cientifica.py hohmann`).
2. Masa: `python herramientas/calculadora_cientifica.py cohete --isp <s> --m0 <kg> --mf <kg>` por etapa; aplique margen (≥ 10–20 % del delta-v y 20–30 % de masa en fases tempranas) y rotúlelo.
3. Potencia: genere y almacene (eclipses, distancia al Sol: flujo ∝ 1/r²); enlace: pérdida de espacio libre y velocidad de datos con el retardo real.
4. Tripulación (si aplica): oxígeno, agua, alimento y CO₂ por persona y día × duración, más reserva.
5. Cierre: tabla requisito → presupuesto → margen → estado (cierra / no cierra). Marque con ⚠ cada cifra supuesta.
