"""B88-C40: muestreo de evidencia de auditoria y cadena de hashes de registros (SINTETICO, semilla 40)."""
import hashlib, math, random, sys
from math import comb
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: poblacion de 200 registros de evidencia inventados")

# Tamano de muestra para confianza 95 % de detectar al menos un defecto si la tasa es >= p
for p in (0.10, 0.05, 0.02):
    n = math.ceil(math.log(0.05) / math.log(1 - p))
    print(f"Tasa de desviacion tolerable {p:.2f}: muestra (sin defectos) n = {n}")
# Muestreo sin reemplazo (hipergeometrica) en poblacion finita N=200
N = 200
def p_detectar(D, n): return 1 - comb(N - D, n) / comb(N, n)
print("Probabilidad de detectar al menos un registro defectuoso (N=200):")
for D in (4, 10, 20):
    print("  defectuosos =", D, " ".join(f"n={n}: {p_detectar(D, n):.3f}" for n in (10, 30, 60)))
# Verificacion Monte Carlo
random.seed(40)
D, n = 10, 30; ok = 0; M = 100000
pop = [1] * D + [0] * (N - D)
for _ in range(M):
    ok += any(random.sample(pop, n))
print(f"Monte Carlo D=10, n=30: detectado = {ok/M:.4f} (hipergeometrica {p_detectar(10,30):.4f})")
assert abs(ok / M - p_detectar(10, 30)) < 0.01
# Cadena de hashes de un registro de auditoria
def encadenar(entradas):
    h = b"\x00" * 32; cadena = []
    for e in entradas:
        h = hashlib.sha256(h + e.encode()).digest(); cadena.append(h.hex())
    return cadena
log = [f"{i:03d}|revision de requisito R{i%16+1:02d}|ok" for i in range(10)]
c = encadenar(log)
print("Cadena original, ultimos 8 hex:", c[-1][:8])
alt = list(log); alt[3] = alt[3].replace("ok", "NOK")
c2 = encadenar(alt)
primera = next(i for i in range(10) if c[i] != c2[i])
print(f"Alterar la entrada 3: la cadena difiere desde la entrada {primera} y en las {10-primera} siguientes")
assert primera == 3 and c[-1] != c2[-1]
# Clasificacion de hallazgos (sintetica)
H = {"mayor": 2, "menor": 7, "observacion": 11}
print("Hallazgos:", H, "; total =", sum(H.values()), "; proporcion de mayores =", round(H["mayor"] / sum(H.values()), 3))
print("Pruebas superadas.")
