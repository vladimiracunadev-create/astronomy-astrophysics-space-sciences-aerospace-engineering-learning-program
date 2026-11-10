"""B96-C23: continuidad y redundancia de operaciones terrestres SINTETICA: disponibilidad en serie y paralelo."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: MTBF, MTTR y fracciones de causa comun ficticios; semilla 96")
# componentes de una estacion en serie: (nombre, MTBF h, MTTR h)
comp = [("Antena y rotor", 4000.0, 24.0), ("Cadena RF", 8000.0, 8.0), ("Equipo de banda base", 10000.0, 6.0),
        ("Red y energia", 2000.0, 4.0), ("Software de control", 1500.0, 1.0)]
def disp(mtbf, mttr): return mtbf/(mtbf + mttr)
A_i = [disp(m, r) for _, m, r in comp]
A_est = 1.0
for (n, m, r), a in zip(comp, A_i):
    A_est *= a; print(f"{n:24s} MTBF = {m:7.0f} h ; MTTR = {r:5.1f} h ; A = {a:.6f}")
print(f"Disponibilidad de una estacion (serie) = {A_est:.6f} ; indisponible = {(1 - A_est)*8760:.1f} h/anio")
# N estaciones independientes: P(ninguna disponible) = (1 - A)^N
print("N  P(ninguna disponible)  disponibilidad del conjunto")
for N in (1, 2, 3):
    pn = (1 - A_est)**N
    print(f"{N}  {pn:.3e}  {1 - pn:.9f}")
# con causa comun: fraccion beta de la indisponibilidad afecta a todas
beta = 0.10
for N in (2, 3):
    pn = beta*(1 - A_est) + ((1 - beta)*(1 - A_est))**N
    print(f"N = {N}, causa comun beta = {beta}: P(ninguna) = {pn:.3e}  (sin causa comun: {(1 - A_est)**N:.3e})")
# probabilidad de perder un contacto irrepetible = P(ninguna estacion capaz) en ese instante
# Monte Carlo: simula estados disponibles/no en 1e6 instantes con N = 2
rng = random.Random(96)
M = 1_000_000; q = 1 - A_est
perd = 0; perd_cc = 0
for _ in range(M):
    if rng.random() < q and rng.random() < q: perd += 1
    cc = rng.random() < beta*q
    if cc or (rng.random() < (1 - beta)*q and rng.random() < (1 - beta)*q): perd_cc += 1
print(f"Monte Carlo (N=2, 1e6 instantes): perdidas = {perd} ({perd/M:.3e}) ; teoria = {q**2*M:.1f} ({q**2:.3e})")
print(f"Monte Carlo con causa comun: perdidas = {perd_cc} ({perd_cc/M:.3e}) ; teoria = {(beta*q + ((1 - beta)*q)**2)*M:.1f}")
esp = q*q*M
assert abs(perd - esp) < 4*(esp**0.5) + 1
esp2 = (beta*q + ((1 - beta)*q)**2)*M
assert abs(perd_cc - esp2) < 4*(esp2**0.5) + 1
assert 0 < A_est < 1 and all(A_est <= a for a in A_i)
print("Pruebas superadas.")
