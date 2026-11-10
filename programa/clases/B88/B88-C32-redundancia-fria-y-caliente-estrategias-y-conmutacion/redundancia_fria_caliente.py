"""B88-C32: redundancia fria y caliente con cobertura de conmutacion: formulas y Monte Carlo (SINTETICO, semilla 32)."""
import math, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: lambda y T inventados; fallos exponenciales independientes")

lam = 2.0e-5     # 1/h
T = 20000.0      # h
x = lam * T
r = math.exp(-x)
print(f"lambda*T = {x:.3f} ; r = {r:.6f}")
def hot(c):   # ambas unidades encendidas desde t=0; si falla la primaria, la reserva toma el control con prob. c si sigue viva
    return r + (1 - r) * r * c
def cold(c):  # reserva apagada, sin desgaste; conmuta con prob. c
    return r + c * x * r
random.seed(32)
N = 200000
def mc(c, tipo):
    ok = 0
    for _ in range(N):
        t1 = random.expovariate(lam)
        if t1 >= T: ok += 1; continue
        conmuta = random.random() < c
        if not conmuta: continue
        if tipo == "cold":
            t2 = random.expovariate(lam)      # reserva nueva: vive desde t1
            ok += (t1 + t2 >= T)
        else:
            t2 = random.expovariate(lam)      # reserva vivio desde 0
            ok += (t2 >= T)
    return ok / N
print(f"R simple = {r:.6f}")
print(f"{'c':>5s} | {'caliente teor':>13s} {'MC':>9s} | {'fria teor':>9s} {'MC':>9s}")
for c in (1.0, 0.99, 0.95, 0.90, 0.80):
    h, cf = hot(c), cold(c)
    mh, mcf = mc(c, "hot"), mc(c, "cold")
    print(f"{c:5.2f} | {h:13.6f} {mh:9.6f} | {cf:9.6f} {mcf:9.6f}")
    assert abs(h - mh) < 0.004 and abs(cf - mcf) < 0.004
# cobertura de cruce: frio = caliente
cs = [c / 1000 for c in range(1, 1001)]
cruce = None
for c in cs:
    if cold(c) <= hot(c): cruce = c
# la fria gana siempre si x > 1-r? comparar a c igual
print(f"A igual cobertura, fria - caliente = {cold(1.0)-hot(1.0):+.6f} (x*r - (1-r)*r)")
# Cobertura de la fria necesaria para igualar a la caliente perfecta
c_req = (hot(1.0) - r) / (x * r)
print(f"Cobertura de la fria para igualar a la caliente perfecta: c = {c_req:.4f}")
print("Pruebas superadas.")
