"""B96-C13: deteccion de anomalias SINTETICA en telemetria: limite fijo, puntuacion robusta y CUSUM."""
import math, random, statistics, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: serie de 3000 muestras N(10, 0.5); tres anomalias inyectadas; semilla 96")
random.seed(96)
N = 3000; mu0, s0 = 10.0, 0.5
x = [random.gauss(mu0, s0) for _ in range(N)]
# anomalias: (inicio, longitud, tipo)
iny = [(800, 40, "pico +4 sigma"), (1600, 400, "deriva +0.8 sigma"), (2500, 1, "dato aislado +6 sigma")]
for ini, L, tipo in iny:
    for k in range(L):
        if tipo.startswith("pico"): x[ini+k] += 4*s0
        elif tipo.startswith("deriva"): x[ini+k] += 0.8*s0
        else: x[ini+k] += 6*s0
def en_anomalia(k):
    return any(ini <= k < ini + L for ini, L, _ in iny)
# 1) limite fijo +-3 sigma (mu0, s0 conocidos)
def lim(x): return [abs(v - mu0) > 3*s0 for v in x]
# 2) puntuacion robusta con ventana de 200 muestras previas (mediana/MAD)
def robusta(x, W=200, z=4.0):
    out = [False]*len(x)
    for k in range(W, len(x)):
        w = x[k-W:k]; m = statistics.median(w)
        mad = statistics.median([abs(v - m) for v in w])*1.4826
        out[k] = abs(x[k] - m) > z*mad
    return out
# 3) CUSUM unilateral con k = 0.5 sigma, h = 5 sigma
def cusum(x, k=0.5, h=5.0):
    S = 0.0; out = []
    for v in x:
        S = max(0.0, S + (v - mu0)/s0 - k)
        out.append(S > h)
        if S > h: S = 0.0
    return out
def evalua(nombre, alarmas):
    falsas = sum(1 for k, a in enumerate(alarmas) if a and not en_anomalia(k))
    lat = []
    for ini, L, tipo in iny:
        hit = [k for k in range(ini, min(N, ini + L + 60)) if alarmas[k]]
        lat.append(hit[0] - ini if hit else None)
    print(f"{nombre:18s} alarmas = {sum(alarmas):4d} ; falsas = {falsas:3d} ; latencias (muestras) = {lat}")
    return falsas, lat
fa1, l1 = evalua("limite 3 sigma", lim(x))
fa2, l2 = evalua("robusta z=4", robusta(x))
fa3, l3 = evalua("CUSUM k=.5 h=5", cusum(x))
sano = N - sum(L for _, L, _ in iny)
p3 = math.erfc(3/math.sqrt(2))
print(f"Falsas esperadas del limite 3 sigma = {p3*sano:.1f} (p = {p3:.5f}) ; observadas = {fa1}")
assert abs(fa1 - p3*sano) < 4*math.sqrt(p3*sano) + 1
assert l1[0] == 0 and l1[2] == 0           # pico y dato aislado detectados al instante
assert l1[1] is None or l1[1] > 50         # el limite no ve la deriva de 0.8 sigma
assert l3[1] is not None and l3[1] < 60    # CUSUM si la detecta
print(f"Deriva: limite fijo la detecta? {'no' if l1[1] is None else 'si, tarde'} ; CUSUM la detecta en {l3[1]} muestras")
print("Pruebas superadas.")
