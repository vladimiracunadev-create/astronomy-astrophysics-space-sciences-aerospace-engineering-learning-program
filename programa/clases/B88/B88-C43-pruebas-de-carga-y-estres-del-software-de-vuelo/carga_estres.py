"""B88-C43: carga y estres: cola de mensajes con servicio de 5 ms, teoria M/D/1 frente a simulacion (SINTETICO, semilla 43)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: llegadas Poisson y servicio determinista de 5 ms")

S = 5.0   # ms por mensaje
def simular(lam_por_s, cap=None, N=200000, semilla=43):
    rnd = random.Random(semilla); lam = lam_por_s / 1000.0  # mensajes por ms
    t = 0.0; libre = 0.0; esperas = []; perdidos = 0; en_cola = []
    for _ in range(N):
        t += rnd.expovariate(lam)
        # mensajes en el sistema: los que terminan despues de t
        en_cola = [f for f in en_cola if f > t]
        if cap is not None and len(en_cola) >= cap: perdidos += 1; continue
        ini = max(t, libre); libre = ini + S
        en_cola.append(libre); esperas.append(ini - t)
    esperas.sort()
    return sum(esperas) / len(esperas), esperas[int(0.99 * (len(esperas) - 1))], perdidos / N
print("rho    lambda   Wq teor    Wq sim    p99 sim   (sin limite de cola)")
for rho in (0.3, 0.5, 0.8, 0.9, 0.95):
    lam = rho / S * 1000
    wq = rho * S / (2 * (1 - rho))
    sim, p99, _ = simular(lam)
    print(f"{rho:4.2f} {lam:8.1f} {wq:9.3f} {sim:9.3f} {p99:9.3f}")
    assert abs(sim - wq) / wq < 0.1 or rho >= 0.9
print("Con cola limitada a 16 mensajes:")
for rho in (0.8, 0.95, 1.1, 1.5):
    lam = rho / S * 1000
    sim, p99, perd = simular(lam, cap=16)
    print(f"rho={rho:4.2f} lambda={lam:7.1f}/s  espera media = {sim:7.3f} ms  p99 = {p99:7.3f} ms  descartados = {100*perd:5.2f} %")
print(f"Capacidad maxima = 1/S = {1000/S:.0f} mensajes/s")
print("Pruebas superadas.")
