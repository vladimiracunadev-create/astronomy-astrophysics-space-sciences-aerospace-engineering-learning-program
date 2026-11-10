"""B88-C39: cobertura de sentencia, decision y MC/DC de una funcion booleana (SINTETICO)."""
import itertools, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: la decision (a and b) or c; los niveles de exigencia son DIDACTICOS (no consultados en DO-178C)")

def decision(a, b, c): return (a and b) or c
combos = list(itertools.product([False, True], repeat=3))
print("Tabla de verdad (a, b, c -> D):")
for t in combos: print("  ", t, "->", decision(*t))
def cubre_decision(tests):
    r = {decision(*t) for t in tests}; return r == {True, False}
def pares_mcdc(tests, i):
    # par independiente para la condicion i: dos tests que difieren solo en la condicion i y dan distinto resultado
    p = []
    for t1, t2 in itertools.combinations(tests, 2):
        dif = [k for k in range(3) if t1[k] != t2[k]]
        if dif == [i] and decision(*t1) != decision(*t2): p.append((t1, t2))
    return p
def cubre_mcdc(tests): return all(pares_mcdc(tests, i) for i in range(3))
# Conjunto minimo MC/DC por busqueda exhaustiva
mejor = None
for n in range(2, 9):
    for sub in itertools.combinations(combos, n):
        if cubre_mcdc(sub): mejor = sub; break
    if mejor: break
print(f"Tamano minimo de un conjunto MC/DC = {len(mejor)} (n+1 = {3+1} para n = 3 condiciones)")
print("  Conjunto:", mejor)
# Cuantos conjuntos minimos existen
cnt = sum(1 for sub in itertools.combinations(combos, len(mejor)) if cubre_mcdc(sub))
print(f"Numero de conjuntos MC/DC de ese tamano = {cnt} de {len(list(itertools.combinations(combos, len(mejor))))}")
# Conjuntos que cubren sentencia / decision pero no MC/DC
T1 = [(True, True, False), (False, False, False)]
print(f"Conjunto {T1}: decision={cubre_decision(T1)} MC/DC={cubre_mcdc(T1)}")
T2 = [(True, True, True), (False, False, False)]
print(f"Conjunto {T2}: decision={cubre_decision(T2)} MC/DC={cubre_mcdc(T2)}")
print("Cobertura de condiciones exhaustiva (todas las combinaciones) =", len(combos), "pruebas ; MC/DC =", len(mejor))
# Crecimiento: n condiciones
for n in (3, 5, 8, 12):
    print(f"  n = {n:2d}: exhaustiva = {2**n:5d} ; MC/DC minimo = n+1 = {n+1}")
assert len(mejor) == 4 and cubre_decision(T1) and not cubre_mcdc(T1)
print("Pruebas superadas.")
