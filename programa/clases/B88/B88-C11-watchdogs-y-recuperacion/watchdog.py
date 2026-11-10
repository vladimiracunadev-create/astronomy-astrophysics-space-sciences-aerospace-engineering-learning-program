"""B88-C11: watchdog de ventana y escalera de recuperacion (SINTETICO, semilla fija)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: lazo de 100 ms con fluctuacion inventada")

T = 100.0          # ms, periodo del lazo que patea el watchdog
VENT = (60.0, 140.0)   # ventana: patear entre 60 y 140 ms despues de la ultima patada
def simular(jit_sigma, n=200000, semilla=3, colgar_en=None):
    random.seed(semilla)
    ult = 0.0; t = 0.0; resets = 0; tempranos = 0; tardios = 0
    for k in range(n):
        t += T + random.gauss(0, jit_sigma)
        if colgar_en is not None and k >= colgar_en: break
        d = t - ult
        if d < VENT[0]: resets += 1; tempranos += 1; ult = t
        elif d > VENT[1]: resets += 1; tardios += 1; ult = t
        else: ult = t
    return resets, tempranos, tardios
print(f"Ventana = [{VENT[0]:.0f}, {VENT[1]:.0f}] ms ; periodo = {T:.0f} ms ; margen = +-{T-VENT[0]:.0f}/{VENT[1]-T:.0f} ms")
for s in (5, 10, 20, 30):
    r, e, l = simular(s)
    print(f"jitter sigma={s:2d} ms: resets falsos en 200000 ciclos = {r:5d} (tempranos {e}, tardios {l}) -> {r/200000:.2e} por ciclo")
# Probabilidad teorica de una patada fuera de ventana: P(|N(0,s)| > 40) = erfc(40/(s sqrt2))
import math
for s in (10, 20, 30):
    p = math.erfc(40 / (s * math.sqrt(2)))
    print(f"  teorico sigma={s}: P(fuera de ventana) = {p:.3e}")
# Colgado: el watchdog debe disparar
r, e, l = simular(5, n=1000, colgar_en=500)
print("Software colgado en el ciclo 500: el watchdog expira tras", VENT[1], "ms sin patada -> reset (1 vez)")

# Escalera de recuperacion: resets en ventana de 10 min
def escalera(tiempos_reset):
    nivel = 0; hist = []; acc = []
    for t in tiempos_reset:
        hist = [x for x in hist if t - x < 600]; hist.append(t)
        nivel = 1 if len(hist) == 1 else 2 if len(hist) == 2 else 3
        acc.append((t, nivel))
    return acc
names = {1: "reinicio de la tarea", 2: "reinicio del computador", 3: "modo seguro y espera a tierra"}
for t, n in escalera([100, 300, 450, 2000]):
    print(f"reset a t={t:4d} s -> nivel {n}: {names[n]}")
assert simular(5)[0] == 0
assert simular(30)[0] > 1000
print("Pruebas superadas.")
