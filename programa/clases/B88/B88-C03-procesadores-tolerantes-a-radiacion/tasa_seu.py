"""B88-C03: tasa de SEU, margen de dosis y Monte Carlo con semilla fija (todo SINTETICO)."""
import math, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: secciones eficaces, flujos y dosis inventados; NO son de un componente real")

sigma_bit = 1.0e-14       # cm^2/bit (sintetico)
bits = 64 * 1024 * 8      # 64 KiB
flux = 1.0e2             # particulas/cm^2/s con LET sobre umbral (sintetico)
rate = sigma_bit * bits * flux   # eventos/s
print(f"bits={bits}  tasa SEU = {rate:.3e} /s = {rate*86400:.6f} /dia = {rate*86400*365:.2f} /anio")

# Weibull de seccion eficaz vs LET (parametros sinteticos)
def sigma_let(L, s_sat=1e-14, L0=1.0, W=20.0, s=1.5):
    return 0.0 if L <= L0 else s_sat * (1 - math.exp(-(((L - L0) / W) ** s)))
for L in (0.5, 2, 5, 15, 40, 80):
    print(f"LET={L:5.1f} MeV cm2/mg  sigma/bit={sigma_let(L):.3e} cm2")

# TID: margen de diseno de dosis (RDM)
dosis_mision, dosis_fallo = 20.0, 60.0   # krad(Si)
print(f"RDM = {dosis_fallo/dosis_mision:.2f}  (criterio sintetico RDM >= 2: {'cumple' if dosis_fallo/dosis_mision>=2 else 'NO'})")

# Monte Carlo: eventos Poisson en 1 anio, 2000 corridas
random.seed(88)
lam_y = rate * 86400 * 365
def poisson(l):
    L, k, p = math.exp(-l), 0, 1.0
    while True:
        p *= random.random()
        if p <= L: return k
        k += 1
N = 2000
xs = [poisson(lam_y) for _ in range(N)]
m = sum(xs) / N
v = sum((x - m) ** 2 for x in xs) / (N - 1)
print(f"Monte Carlo (semilla 88, {N} corridas): media={m:.3f} (teoria {lam_y:.3f})  varianza={v:.3f} (Poisson: igual a la media)")
assert abs(m - lam_y) < 0.2 * lam_y
print("Pruebas superadas.")
