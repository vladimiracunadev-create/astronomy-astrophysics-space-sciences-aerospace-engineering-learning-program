"""B88-C16: arbol de fallos, conjuntos minimos de corte e importancia (SINTETICO)."""
import itertools, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: probabilidades por mision inventadas; eventos independientes")

# Evento tope: PERDIDA DE CONTROL = (FALLO_COMPUTADOR) OR (FALLO_ACTUADORES)
# FALLO_COMPUTADOR = A AND B (dos computadores); FALLO_ACTUADORES = C OR (D AND E)
P = {"A": 1e-2, "B": 1e-2, "C": 1e-4, "D": 5e-2, "E": 5e-2}
def top(est):
    comp = est["A"] and est["B"]
    act = est["C"] or (est["D"] and est["E"])
    return comp or act
ev = list(P)
def prob_exacta(p):
    tot = 0.0
    for bits in itertools.product([0, 1], repeat=len(ev)):
        est = dict(zip(ev, bits))
        pr = 1.0
        for k in ev: pr *= p[k] if est[k] else 1 - p[k]
        if top(est): tot += pr
    return tot
Pt = prob_exacta(P)
print(f"P(evento tope) exacta = {Pt:.6e}")

# Conjuntos minimos de corte por enumeracion
cortes = []
for r in range(1, len(ev) + 1):
    for c in itertools.combinations(ev, r):
        est = {k: (k in c) for k in ev}
        if top(est) and not any(set(m) <= set(c) for m in cortes): cortes.append(c)
print("Conjuntos minimos de corte:", [list(c) for c in cortes])
ap = 0.0
for c in cortes:
    pc = 1.0
    for k in c: pc *= P[k]
    ap += pc
    print(f"  {'+'.join(c):4s}: P = {pc:.3e}")
print(f"Aproximacion por suma de cortes = {ap:.6e} (cota superior; exacta {Pt:.6e})")
assert ap >= Pt

# Importancia de Birnbaum: P(top | k fallado) - P(top | k bueno)
print("Importancia de Birnbaum:")
imp = {}
for k in ev:
    a = dict(P); a[k] = 1.0; b = dict(P); b[k] = 0.0
    imp[k] = prob_exacta(a) - prob_exacta(b)
    print(f"  {k}: {imp[k]:.4f}")
# Matriz severidad-probabilidad (clasificacion sintetica)
def clase(sev, p):
    nivel = 1 if p < 1e-6 else 2 if p < 1e-4 else 3 if p < 1e-2 else 4
    return "ALTO" if sev * nivel >= 12 else "MEDIO" if sev * nivel >= 6 else "BAJO"
for nom, sev, p in (("perdida de control", 4, Pt), ("perdida de un instrumento", 2, 3e-3), ("dato degradado", 1, 5e-2)):
    print(f"  {nom:26s} severidad {sev}, P={p:.1e} -> riesgo {clase(sev, p)}")
assert len(cortes) == 3
print("Pruebas superadas.")
