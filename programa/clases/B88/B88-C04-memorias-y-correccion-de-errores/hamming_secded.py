"""B88-C04: Hamming SECDED (72,64) con inyeccion de errores y barrido (semilla fija)."""
import random, sys, math
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: palabras aleatorias de 64 bit; errores inyectados por el propio script")

K, P = 64, 7              # 64 datos, 7 bits de paridad Hamming + 1 paridad global = 72
N = K + P                 # posiciones 1..71 del codigo Hamming
datapos = [i for i in range(1, N + 1) if i & (i - 1)]  # no potencias de 2
assert len(datapos) == K

def encode(d):
    w = [0] * (N + 1)
    for i, pos in enumerate(datapos): w[pos] = (d >> i) & 1
    for j in range(P):
        p = 1 << j
        w[p] = sum(w[q] for q in range(1, N + 1) if q & p and q != p) & 1
    g = sum(w[1:]) & 1
    return w, g

def decode(w, g):
    w = w[:]
    s = 0
    for j in range(P):
        p = 1 << j
        if sum(w[q] for q in range(1, N + 1) if q & p) & 1: s |= p
    gp = (sum(w[1:]) + g) & 1
    if s == 0 and gp == 0: estado = "ok"
    elif gp == 1:
        if 1 <= s <= N: w[s] ^= 1
        estado = "corregido"
    else: estado = "doble"
    d = sum(w[pos] << i for i, pos in enumerate(datapos))
    return d, estado

random.seed(4)
cnt = {"ok": 0, "corregido": 0, "doble": 0, "mal": 0}
N1 = 2000
for _ in range(N1):
    d = random.getrandbits(64); w, g = encode(d)
    k = random.randrange(1, N + 1); w[k] ^= 1
    d2, e = decode(w, g)
    cnt["corregido" if (e == "corregido" and d2 == d) else "mal"] += 1
print(f"Un error en {N1} palabras: corregidos={cnt['corregido']} mal={cnt['mal']}")
cnt2 = {"doble": 0, "mal": 0}
for _ in range(N1):
    d = random.getrandbits(64); w, g = encode(d)
    a, b = random.sample(range(1, N + 1), 2); w[a] ^= 1; w[b] ^= 1
    _, e = decode(w, g)
    cnt2["doble" if e == "doble" else "mal"] += 1
print(f"Dos errores en {N1} palabras: detectados={cnt2['doble']} no detectados={cnt2['mal']}")
print(f"Sobrecarga: 72/64 = {72/64:.4f} ({100*(72/64-1):.1f} %)")

# Barrido: palabras con tasa de inversion q por bit y hora; ocurre doble error si 2 llegan antes de barrer
q = 1e-9      # /bit/h (sintetico)
words = 2**20
for scrub_h in (1, 24, 24 * 30, 24 * 365):
    lam = 72 * q * scrub_h
    p2 = 1 - math.exp(-lam) * (1 + lam)           # >=2 inversiones en la misma palabra
    print(f"barrido cada {scrub_h:5d} h: P(>=2 en una palabra) = {p2:.3e} ; palabras esperadas con doble = {p2*words:.3e}")
assert cnt["mal"] == 0 and cnt2["mal"] == 0
print("Pruebas superadas.")
