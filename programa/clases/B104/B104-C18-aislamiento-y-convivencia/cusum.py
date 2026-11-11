#!/usr/bin/env python3
"""B104-C18: seguimiento del animo de una tripulacion aislada con una carta CUSUM.
DATOS SINTETICOS (semilla 104); no son datos de Mars-500 ni de ninguna persona. Parametros k y h estandar de la carta (no consultados)."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("DATOS SINTETICOS (semilla 104): puntajes de animo diarios estandarizados; baja de nivel = deterioro; k = 0,5; h = 4")
K, H = 0.5, 4.0
rng = np.random.default_rng(104)


def corrida(delta, max_dias=20000):
    """Dias hasta la primera alarma de una carta CUSUM inferior con un desplazamiento medio -delta (desv. est.)."""
    s = 0.0
    for t in range(1, max_dias + 1):
        x = -delta + rng.standard_normal()
        s = max(0.0, s - x - K)
        if s > H:
            return t
    return max_dias


def arl(delta, reps):
    return np.mean([corrida(delta) for _ in range(reps)])


b = H + 1.166


def siegmund(delta):
    d = delta - K
    if abs(d) < 1e-12:
        return (b**2) / 1.0
    return (np.exp(-2 * d * b) + 2 * d * b - 1) / (2 * d**2)


print("\ndesplazamiento [desv. est.] | ARL Monte Carlo [dias] | ARL aproximado de Siegmund [dias]")
r0 = arl(0.0, 1500)
r1 = arl(1.0, 6000)
r2 = arl(2.0, 6000)
print(f"{0.0:27.1f} {r0:22.1f} {siegmund(0.0):30.1f}")
print(f"{1.0:27.1f} {r1:22.1f} {siegmund(1.0):30.1f}")
print(f"{2.0:27.1f} {r2:22.1f} {siegmund(2.0):30.1f}")

# Escenario: 520 dias (duracion del estudio Mars500 consultado), 6 personas, deterioro gradual desde el dia 200 en una persona
print("\nEscenario sintetico: 520 dias, deterioro gradual de 0,01 desv. est. por dia desde el dia 200 en 1 de 6 personas")
N = 2000
detecta = []
falsa = 0
for _ in range(N):
    s = 0.0
    dia_alarma = None
    for t in range(1, 521):
        mu = -0.01 * max(0, t - 200)
        x = mu + rng.standard_normal()
        s = max(0.0, s - x - K)
        if s > H and dia_alarma is None:
            dia_alarma = t
    if dia_alarma is None:
        continue
    if dia_alarma < 200:
        falsa += 1
    else:
        detecta.append(dia_alarma - 200)
print(f"  alarmas falsas antes del dia 200: {falsa/N:.3f}; detecciones tras el inicio: {len(detecta)/N:.3f}; demora mediana desde el inicio: {np.median(detecta):.0f} dias")

assert abs(r0 - siegmund(0.0)) / siegmund(0.0) < 0.12, "ARL0 debe coincidir con la aproximacion"
assert abs(r1 - siegmund(1.0)) / siegmund(1.0) < 0.06
assert r0 > 20 * r1 > 0
print("Pruebas superadas.")
