"""B88-C06: RM frente a EDF por simulacion y cota de Liu-Layland (SINTETICO)."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: conjuntos de tareas de ejemplo (unidades: ticks)")

def sim(tareas, pol):
    H = math.lcm(*[t for c, t in tareas])
    pend = []; fallos = 0; cambios = 0; ultimo = None
    for t in range(H):
        for i, (c, T) in enumerate(tareas):
            if t % T == 0: pend.append([0, c, t, i, t + T])
        for j in pend:
            j[0] = tareas[j[3]][1] if pol == "RM" else j[4]
        # plazo vencido
        for j in pend[:]:
            if j[4] <= t and j[1] > 0:
                fallos += 1; pend.remove(j)
        if pend:
            pend.sort(key=lambda j: (j[0], j[2]))
            j = pend[0]
            if ultimo is not None and ultimo is not j: cambios += 1
            ultimo = j
            j[1] -= 1
            if j[1] == 0: pend.remove(j)
    return H, fallos, cambios

print("Cota de Liu-Layland n(2^(1/n)-1):")
for n in range(1, 6):
    print(f"  n={n}: {n*(2**(1/n)-1):.4f}")
print(f"  limite n->inf: {math.log(2):.4f}")

casos = {"A: (2,5),(4,7)": [(2, 5), (4, 7)],
         "B: armonico (1,2),(1,4),(2,8)": [(1, 2), (1, 4), (2, 8)],
         "C: (1,4),(2,6),(3,13)": [(1, 4), (2, 6), (3, 13)]}
res = {}
for k, ts in casos.items():
    U = sum(c / t for c, t in ts)
    for pol in ("RM", "EDF"):
        H, f, ch = sim(ts, pol)
        res[(k[0], pol)] = f
        print(f"{k:32s} U={U:.4f} {pol:3s} hiperperiodo={H:3d} plazos perdidos={f} cambios de contexto={ch}")
assert res[("A", "RM")] > 0 and res[("A", "EDF")] == 0
assert res[("B", "RM")] == 0 and res[("C", "RM")] == 0 and res[("C", "EDF")] == 0
print("Pruebas superadas.")
