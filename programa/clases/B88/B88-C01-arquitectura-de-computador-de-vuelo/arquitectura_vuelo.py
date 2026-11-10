"""B88-C01: presupuesto de un computador de vuelo SINTETICO (CPU, memoria, fiabilidad)."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: no describen un computador real")

# Tareas: (nombre, periodo ms, WCET ms)
tareas = [("AOCS", 100, 12.0), ("TM", 500, 20.0), ("TC", 250, 6.0), ("FDIR", 1000, 40.0), ("Energia", 1000, 25.0)]
U = sum(c / p for _, p, c in tareas)
print(f"Utilizacion de CPU = {U:.4f} ({U*100:.1f} %) ; criterio de margen <= 70 %: {'cumple' if U <= 0.70 else 'NO cumple'}")

# Memoria en KiB: (region, usado, capacidad)
mem = [("ROM", 1480, 2048), ("RAM", 610, 1024), ("NVRAM", 96, 256)]
for r, u, c in mem:
    print(f"{r:6s} usado={u:5d} KiB cap={c:5d} KiB margen={100*(1-u/c):5.1f} %")

# Fiabilidad con tasa de fallo constante (sintetica)
lam = 2.0e-6      # 1/h
T = 5 * 8760.0    # h, 5 anios
r = math.exp(-lam * T)
R_hot = 1 - (1 - r) ** 2                      # paralelo, conmutacion perfecta
R_cold = math.exp(-lam * T) * (1 + lam * T)   # reserva fria perfecta
print(f"lambda={lam:.1e}/h  T={T:.0f} h  lambda*T={lam*T:.4f}")
print(f"R simple = {r:.6f}")
print(f"R caliente (2 unidades, conmutacion perfecta) = {R_hot:.8f}")
print(f"R fria (reserva sin fallo en espera)        = {R_cold:.8f}")
# conmutador imperfecto con cobertura c
for c in (1.0, 0.99, 0.9):
    Rc = r + c * lam * T * r
    print(f"R fria con cobertura c={c:4.2f}: {Rc:.8f}")
assert abs(R_cold - (r + lam * T * r)) < 1e-15
assert R_hot > r and R_cold > r
print("Pruebas superadas.")
