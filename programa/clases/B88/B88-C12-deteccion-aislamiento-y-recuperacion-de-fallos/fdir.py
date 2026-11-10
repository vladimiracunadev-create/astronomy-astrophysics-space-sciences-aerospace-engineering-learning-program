"""B88-C12: monitores FDIR con persistencia, latencia de deteccion y falsas alarmas (SINTETICO)."""
import math, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: sensor de temperatura con ruido gaussiano inventado")
random.seed(12)
mu, sigma, lim, dt = 20.0, 1.0, 22.0, 1.0   # grados C, grados C, limite, periodo de muestreo (s)
q = 0.5 * math.erfc((lim - mu) / (sigma * math.sqrt(2)))
print(f"P(muestra > limite) por ruido = {q:.5f}")

def corrida(N, n_muestras=400000):
    cnt = 0; alarmas = 0; ant = False
    for _ in range(n_muestras):
        x = random.gauss(mu, sigma)
        cnt = cnt + 1 if x > lim else 0
        a = cnt >= N
        if a and not ant: alarmas += 1
        ant = a
    return alarmas
print("Persistencia N -> falsas alarmas (simulado vs aprox. teorica q^N*(1-q))*muestras")
for N in (1, 2, 3, 4):
    sim = corrida(N)
    teo = 400000 * (q ** N) * (1 - q)
    print(f"  N={N}: simuladas={sim:6d}  teoricas~{teo:9.1f}")

# Latencia de deteccion para una falla (salto a 25 C) que empieza en un instante aleatorio
def latencia(N):
    cnt = 0; k = 0
    while True:
        k += 1
        x = random.gauss(25.0, sigma)
        cnt = cnt + 1 if x > lim else 0
        if cnt >= N: return k * dt
for N in (1, 2, 3, 4):
    L = [latencia(N) for _ in range(5000)]
    print(f"  N={N}: latencia media = {sum(L)/len(L):.3f} s ; maxima = {max(L):.0f} s (muestreo {dt:.0f} s)")

# Tabla de respuesta: monitor -> accion
TAB = [("TEMP_ALTA", "aislar el calentador", "N=3"), ("BUS_SIN_RESP", "conmutar al bus B", "N=2"), ("TENSION_BAJA", "desconectar cargas no esenciales", "N=1")]
for m, a, n in TAB: print(f"  {m:13s} -> {a:34s} ({n})")
assert corrida(3) < corrida(1)
print("Pruebas superadas.")
