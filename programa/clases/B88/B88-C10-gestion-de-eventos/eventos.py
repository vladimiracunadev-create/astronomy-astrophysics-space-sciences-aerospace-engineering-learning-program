"""B88-C10: gestion de eventos con severidad y supresion de tormentas (SINTETICO, semilla fija)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: eventos generados con semilla 10")

random.seed(10)
# (id, nombre, severidad 1=info..4=critico)
EV = {1: ("TEMP_ALTA", 2), 2: ("BUS_ERR", 3), 3: ("RESET_WDG", 4), 4: ("TM_LISTO", 1), 5: ("SENSOR_PARPADEO", 2)}
# Tormenta: id 5 a 50/s durante 20 s; resto esporadico
eventos = []
for t in range(60):
    if 20 <= t < 40:
        eventos += [(t + k / 50, 5) for k in range(50)]
    for i in (1, 2, 4):
        if random.random() < 0.15: eventos.append((t + random.random(), i))
    if t in (25, 50): eventos.append((t + 0.5, 3))
eventos.sort()
print(f"Eventos generados = {len(eventos)}")

def gestor(limitar):
    cubo = {}  # id -> [fichas, ultimo]
    reg = []; supr = {}
    for t, i in eventos:
        sev = EV[i][1]
        if limitar and sev < 4:
            fichas, ult = cubo.get(i, [3.0, t])
            fichas = min(3.0, fichas + (t - ult) * 1.0)   # 1 evento/s sostenido, rafaga 3
            if fichas >= 1: fichas -= 1; cubo[i] = [fichas, t]; reg.append((t, i))
            else: cubo[i] = [fichas, t]; supr[i] = supr.get(i, 0) + 1
        else: reg.append((t, i))
    return reg, supr
for lim in (False, True):
    reg, supr = gestor(lim)
    crit = sum(1 for _, i in reg if EV[i][1] == 4)
    print(f"Limitador {'si' if lim else 'no'}: registrados = {len(reg):4d} ; suprimidos = {sum(supr.values()):4d} ; criticos registrados = {crit}")
    if lim: print("  suprimidos por ID:", dict(sorted(supr.items())))
crit_total = sum(1 for _, i in eventos if EV[i][1] == 4)
reg, supr = gestor(True)
assert sum(1 for _, i in reg if EV[i][1] == 4) == crit_total
assert 3 not in supr
print(f"Eventos criticos generados = {crit_total} ; ninguno suprimido")
print("Pruebas superadas.")
