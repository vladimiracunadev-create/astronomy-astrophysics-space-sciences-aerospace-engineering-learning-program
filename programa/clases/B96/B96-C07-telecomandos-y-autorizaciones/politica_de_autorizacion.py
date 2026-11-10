"""B96-C07: politica de autorizacion de telecomandos (rol x criticidad x aprobaciones), SINTETICA; prueba exhaustiva."""
import sys, itertools
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: roles, niveles de criticidad y reglas ficticios")
ROLES = ["operador", "ingeniero", "director"]
CRIT = ["rutina", "sensible", "critico", "peligroso"]
def autorizado(rol, crit, aprob_roles, armado):
    """aprob_roles: roles de OTRAS personas distintas que aprobaron."""
    r = ROLES.index(rol); c = CRIT.index(crit)
    if c == 0: return True
    if c == 1: return r >= 1
    if c == 2: return r >= 2 and len(aprob_roles) >= 1
    return r >= 2 and ("ingeniero" in aprob_roles or "director" in aprob_roles) and armado
MIN_ROL = {"rutina": 0, "sensible": 1, "critico": 2, "peligroso": 2}
MIN_APROB = {"rutina": 0, "sensible": 0, "critico": 1, "peligroso": 1}
def referencia(rol, crit, aprob_roles, armado):
    if ROLES.index(rol) < MIN_ROL[crit]: return False
    validas = [a for a in aprob_roles if ROLES.index(a) >= (1 if crit == "peligroso" else 0)]
    if len(validas) < MIN_APROB[crit]: return False
    if crit == "peligroso" and not armado: return False
    return True
combos = 0; permitidos = 0; dif = 0
aprob_opts = [(), ("operador",), ("ingeniero",), ("director",), ("operador", "ingeniero")]
tabla = {c: 0 for c in CRIT}
for rol, crit, ap, arm in itertools.product(ROLES, CRIT, aprob_opts, (False, True)):
    a = autorizado(rol, crit, ap, arm); b = referencia(rol, crit, ap, arm)
    combos += 1; permitidos += a; dif += (a != b)
    if a: tabla[crit] += 1
print(f"Combinaciones evaluadas = {combos} ; permitidas = {permitidos} ; discrepancias con la referencia = {dif}")
print("Permitidas por criticidad:", tabla)
assert dif == 0
assert not any(autorizado(r, "peligroso", ap, False) for r in ROLES for ap in aprob_opts)
assert not any(autorizado(r, "critico", (), arm) for r in ROLES for arm in (False, True))
mono = all((not autorizado(ROLES[i], c, ap, arm)) or autorizado(ROLES[i+1], c, ap, arm)
           for i in range(2) for c in CRIT for ap in aprob_opts for arm in (False, True))
print(f"Monotonia por rol = {mono}")
assert mono
print("Pruebas superadas.")
