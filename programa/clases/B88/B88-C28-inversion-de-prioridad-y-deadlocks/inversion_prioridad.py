"""B88-C28: inversion de prioridad, herencia y bloqueo mutuo (SINTETICO; escenario inspirado en el relato de Jones sobre Pathfinder)."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: tres tareas inventadas (unidades: ticks); no es la nave Pathfinder")

def simular(herencia, T=80):
    # prioridades: A (alta)=3, M (media)=2, B (baja)=1
    # B toma el mutex en t=0 y necesita 6 ticks dentro de la seccion critica.
    # A llega en t=2 y necesita el mutex (2 ticks dentro). M llega en t=3 y calcula 10 ticks.
    est = {"B": {"rest": 6, "prio": 1, "lleg": 0, "fase": "crit"}, "A": {"rest": 2, "prio": 3, "lleg": 2, "fase": "esp"}, "M": {"rest": 10, "prio": 2, "lleg": 3, "fase": "norm"}}
    dueno = None; bloqueo_A = 0; fin = {}; cron = []
    for t in range(T):
        # B toma el mutex en t=0
        if t == 0: dueno = "B"
        listos = []
        for n, e in est.items():
            if e["rest"] == 0 or t < e["lleg"]: continue
            if n == "A" and e["fase"] == "esp" and dueno not in (None, "A"):
                continue
            listos.append(n)
        if "A" in est and est["A"]["fase"] == "esp" and t >= 2 and dueno is None: dueno = "A"; est["A"]["fase"] = "crit"
        def prio(n):
            p = est[n]["prio"]
            if herencia and n == dueno and est["A"]["fase"] == "esp" and t >= est["A"]["lleg"]: p = max(p, est["A"]["prio"])
            return p
        if t >= 2 and est["A"]["fase"] == "esp" and dueno == "B": bloqueo_A += 1
        if not listos: cron.append("-"); continue
        n = max(listos, key=prio)
        e = est[n]; e["rest"] -= 1; cron.append(n)
        if e["rest"] == 0:
            fin[n] = t + 1
            if dueno == n: dueno = None
    return fin, bloqueo_A, "".join(cron)
for her in (False, True):
    fin, blq, cron = simular(her)
    print(f"Herencia {'si' if her else 'no':2s}: fin A={fin['A']:3d} fin M={fin['M']:3d} fin B={fin['B']:3d} ; ticks que A espera el mutex = {blq}")
    print(f"   cronograma: {cron}")
fin0, b0, _ = simular(False); fin1, b1, _ = simular(True)
assert b0 > b1 and fin1["A"] < fin0["A"]
print(f"A termina {fin0['A'] - fin1['A']} ticks antes con herencia de prioridad")

# Bloqueo mutuo: grafo de espera
def ciclo(espera):
    for ini in espera:
        vis = set(); n = ini
        while n in espera:
            if n in vis: return True
            vis.add(n); n = espera[n]
        if n == ini: return True
    return False
# T1 tiene R1 y pide R2; T2 tiene R2 y pide R1
tiene = {"R1": "T1", "R2": "T2"}; pide = {"T1": "R2", "T2": "R1"}
espera = {t: tiene[r] for t, r in pide.items()}
print("Espera T1->T2, T2->T1 :", espera, "| bloqueo mutuo =", ciclo(espera))
# Orden total de recursos: ambos toman R1 y luego R2
espera2 = {"T2": "T1"}  # T2 espera a T1 en R1; T1 sigue y libera
print("Con orden total R1<R2 :", espera2, "| bloqueo mutuo =", ciclo(espera2))
assert ciclo(espera) and not ciclo(espera2)
print("Pruebas superadas.")
