"""B88-C19: lazo cerrado planta-controlador con latencia y jitter (banco HIL SINTETICO, 1 eje)."""
import math, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: inercia I = 1 kg m^2, controlador PD, referencia 1 rad; sin planta real")

I, Kp, Kd = 1.0, 4.0, 4.0     # N m/rad, N m s/rad
dt = 0.001                    # paso de la planta emulada, s
Tc = 0.05                     # periodo del controlador, s (20 Hz)
def simular(latencia, jitter=0.0, T=30.0, semilla=19):
    random.seed(semilla)
    th, w = 0.0, 0.0; u = 0.0; cola = []; t = 0.0; prox = 0.0
    maxv = 0.0; traza = []
    n = int(T / dt)
    for k in range(n):
        t = k * dt
        if t >= prox:
            u_nuevo = Kp * (1.0 - th) - Kd * w
            lat = max(0.0, latencia + random.gauss(0, jitter))
            cola.append((t + lat, u_nuevo)); prox += Tc
        while cola and cola[0][0] <= t:
            u = cola.pop(0)[1]
        w += (u / I) * dt; th += w * dt
        maxv = max(maxv, th); traza.append(th)
        if abs(th) > 1e6: return None, None, None
    sob = max(0.0, (maxv - 1.0) * 100)
    ts = 0.0
    for i in range(n - 1, -1, -1):
        if abs(traza[i] - 1.0) > 0.02: ts = (i + 1) * dt; break
    return sob, ts, traza[-1]
print("latencia  jitter | sobreimpulso  t_asentamiento(2%)  theta final")
res = {}
for lat, jit in ((0.0, 0.0), (0.05, 0.0), (0.1, 0.0), (0.2, 0.0), (0.25, 0.0), (0.3, 0.0), (0.4, 0.0), (0.1, 0.03)):
    s, ts, f = simular(lat, jit)
    res[(lat, jit)] = (s, ts)
    if s is None: print(f"{lat:6.2f} s {jit:5.2f} s | INESTABLE"); continue
    print(f"{lat:6.2f} s {jit:5.2f} s | {s:8.2f} %   {ts:12.2f} s   {f:9.4f}")
assert res[(0.0, 0.0)][0] == 0.0 and res[(0.3, 0.0)][0] > 10.0
print("Pruebas superadas.")
