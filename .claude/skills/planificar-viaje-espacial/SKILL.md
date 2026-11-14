---
name: planificar-viaje-espacial
description: Planifica un viaje o misión espacial de primera aproximación: destino, ventana de lanzamiento 2027–2050, delta-v, C3, duración, retardo de señal y cronograma, con las herramientas y simuladores del repositorio. Úselo para «cuándo salir, cuánto delta-v y cuánto tarda» a cualquier planeta.
---

# Planificar un viaje espacial

1. Fije destino, tipo (robótico/tripulado), masa útil, y si hay regreso. Rotule lo que suponga.
2. Resumen de energía: `python herramientas/planificador_de_misiones.py resumen` y, para el destino, `hohmann --destino <venus|marte|jupiter|saturno|urano|neptuno|mercurio> --h-salida 300 [--h-captura 400]`.
3. Ventanas: `python herramientas/planificador_de_misiones.py ventanas --destino <d> --desde 2027 --hasta 2050`. Son de primera aproximación (Hohmann circular coplanar): confirme el óptimo con el simulador de trayectorias (Lambert, gráfico porkchop) y, para diseño, con JPL Horizons.
4. Casos reales comparables: simulador de misiones (encuentros y asistencias gravitatorias) y talleres `talleres/T01…T10`. Posiciones y oposiciones: calendario planetario.
5. Añada: retardo de señal (distancia ÷ c) con la distancia real de los simuladores, presupuesto de delta-v con margen (`calculadora_cientifica.py cohete --isp … --m0 … --mf …`), radiación y duración, soporte vital si es tripulado y plan de regreso/aborto.
6. Entregue un cronograma con hitos y una tabla supuestos→resultado. Todo con unidades; ⚠ en lo no verificable. Apoyo didáctico: no es para decisiones de vuelo.
