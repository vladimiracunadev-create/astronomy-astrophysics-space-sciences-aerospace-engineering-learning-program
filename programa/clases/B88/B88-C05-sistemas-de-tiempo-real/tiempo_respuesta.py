"""B88-C05: tiempo de respuesta en prioridades fijas, verificado con simulacion (SINTETICO)."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: conjunto de tres tareas de ejemplo (unidades: ms)")
# (nombre, C, T, D), prioridad por periodo (RM): menor T = mayor prioridad
tareas = [("t1", 1, 4, 4), ("t2", 2, 6, 6), ("t3", 3, 13, 13)]
U = sum(c / t for _, c, t, _ in tareas)
print(f"U = {U:.4f}")

def rta(i):
    c = tareas[i][1]
    r = c
    while True:
        nuevo = c + sum(math.ceil(r / tareas[j][2]) * tareas[j][1] for j in range(i))
        if nuevo == r: return r
        if nuevo > tareas[i][3]: return nuevo
        r = nuevo

for i, (n, c, t, d) in enumerate(tareas):
    r = rta(i)
    print(f"{n}: C={c} T={t} D={d}  R(analitico)={r}  {'cumple' if r <= d else 'FALLA'}")

# Simulacion discreta (paso 1 ms) sobre 3 hiperperiodos
H = math.lcm(*[t for _, _, t, _ in tareas])
jobs = []; maxr = {n: 0 for n, *_ in tareas}; fallos = 0
pend = []  # [prio, restante, liberacion, nombre, deadline]
for t in range(3 * H):
    for p, (n, c, T, d) in enumerate(tareas):
        if t % T == 0: pend.append([p, c, t, n, t + d])
    if pend:
        pend.sort()
        j = pend[0]; j[1] -= 1
        if j[1] == 0:
            r = t + 1 - j[2]
            maxr[j[3]] = max(maxr[j[3]], r)
            if t + 1 > j[4]: fallos += 1
            pend.pop(0)
print(f"Hiperperiodo = {H} ms ; simulado 3 hiperperiodos ({3*H} ms)")
for n, c, T, d in tareas:
    print(f"{n}: R max simulado = {maxr[n]}")
print(f"Plazos incumplidos = {fallos}")
for i, (n, *_ ) in enumerate(tareas):
    assert maxr[n] == rta(i), (n, maxr[n], rta(i))
print("Pruebas superadas.")
