"""B96-C17: coordinacion de dos estaciones SINTETICA: asignacion de pasadas con optimo por enumeracion frente a voraz."""
import itertools, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: 12 pasadas ficticias; estaciones A y B; semilla 96")
random.seed(96)
# (id, satelite, inicio min, fin min, peso, estaciones que la ven)
tareas = []
for i in range(12):
    ini = random.randint(0, 120); dur = random.randint(8, 16)
    vis = random.choice([("A",), ("B",), ("A", "B")])
    tareas.append((f"P{i+1:02d}", f"S{random.randint(1, 3)}", ini, ini + dur, random.randint(1, 9), vis))
print("id   sat inicio fin peso estaciones")
for t in tareas: print(f"{t[0]} {t[1]:>4s} {t[2]:6d} {t[3]:4d} {t[4]:4d}  {','.join(t[5])}")
def solapa(a, b): return a[2] < b[3] and b[2] < a[3]
def valido(asig):
    for est in ("A", "B"):
        l = [t for t, e in zip(tareas, asig) if e == est]
        for a, b in itertools.combinations(l, 2):
            if solapa(a, b): return False
    return True
def peso(asig): return sum(t[4] for t, e in zip(tareas, asig) if e)
# optimo por enumeracion: cada tarea -> None o una estacion que la ve
mejor = (-1, None); n_eval = 0
opciones = [(None,) + t[5] for t in tareas]
for asig in itertools.product(*opciones):
    n_eval += 1
    if peso(asig) > mejor[0] and valido(asig): mejor = (peso(asig), asig)
print(f"Optimo por enumeracion ({n_eval} asignaciones): peso = {mejor[0]} ; atendidas = {sum(1 for e in mejor[1] if e)} de {len(tareas)}")
# voraz por peso
asig_v = [None]*len(tareas)
for idx in sorted(range(len(tareas)), key=lambda i: -tareas[i][4]):
    for est in tareas[idx][5]:
        trial = list(asig_v); trial[idx] = est
        if valido(trial): asig_v = trial; break
print(f"Voraz por peso: peso = {peso(asig_v)} ; atendidas = {sum(1 for e in asig_v if e)} ; brecha = {mejor[0]-peso(asig_v)}")
# una sola estacion (A) frente a las dos
def mejor_solo(est):
    best = 0
    for mask in range(1 << len(tareas)):
        sel = [tareas[i] for i in range(len(tareas)) if mask >> i & 1 and est in tareas[i][5]]
        ok = all(not solapa(a, b) for a, b in itertools.combinations(sel, 2))
        if ok: best = max(best, sum(t[4] for t in sel))
    return best
pa = mejor_solo("A"); pb = mejor_solo("B")
print(f"Optimo con solo A = {pa} ; solo B = {pb} ; con A y B = {mejor[0]} ; peso total = {sum(t[4] for t in tareas)}")
assert mejor[0] >= max(pa, pb) and peso(asig_v) <= mejor[0] and valido(list(mejor[1])) and valido(asig_v)
assert mejor[0] <= sum(t[4] for t in tareas)
print("Pruebas superadas.")
