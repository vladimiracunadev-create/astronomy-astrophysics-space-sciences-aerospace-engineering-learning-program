"""B88-C14: pruebas unitarias, cobertura de lineas y puntuacion de mutacion (SINTETICO)."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: una funcion de vigilancia de limites inventada")

FUENTE = '''def vigilar(x, lo, hi, n_max):
    if x < lo:
        estado = "BAJO"
    elif x > hi:
        estado = "ALTO"
    else:
        estado = "OK"
    if estado != "OK":
        n_max = n_max - 1
        if n_max <= 0:
            estado = "ALARMA"
    return estado, n_max
'''
PRUEBAS = [
    (lambda f: f(5, 0, 10, 3) == ("OK", 3)),
    (lambda f: f(-1, 0, 10, 3) == ("BAJO", 2)),
    (lambda f: f(11, 0, 10, 3) == ("ALTO", 2)),
    (lambda f: f(11, 0, 10, 1) == ("ALARMA", 0)),
    (lambda f: f(0, 0, 10, 3) == ("OK", 3)),
    (lambda f: f(10, 0, 10, 3) == ("OK", 3)),
]
def cargar(src):
    ns = {}; exec(compile(src, "<vigilar>", "exec"), ns); return ns["vigilar"]
def correr(src, pruebas):
    f = cargar(src); ok = 0
    for p in pruebas:
        try: ok += bool(p(f))
        except Exception: pass
    return ok
print(f"Pruebas que pasan en el original: {correr(FUENTE, PRUEBAS)}/{len(PRUEBAS)}")

# Cobertura de lineas con settrace
def cobertura(pruebas):
    vistas = set()
    def tr(frame, ev, arg):
        if frame.f_code.co_filename == "<vigilar>" and ev == "line": vistas.add(frame.f_lineno)
        return tr
    f = cargar(FUENTE)
    sys.settrace(tr)
    for p in pruebas: p(f)
    sys.settrace(None)
    return vistas
lineas_ejec = {i for i, l in enumerate(FUENTE.split("\n"), 1) if l.strip() and not l.startswith("def")}
for k in (1, 3, len(PRUEBAS)):
    v = cobertura(PRUEBAS[:k]) & lineas_ejec
    print(f"Con {k} pruebas: lineas cubiertas {len(v)}/{len(lineas_ejec)} = {100*len(v)/len(lineas_ejec):.0f} %")

# Mutacion: cambiar un operador a la vez
MUT = [("<", "<="), (">", ">="), ("<=", "<"), ("!=", "=="), ("- 1", "+ 1"), ("<= 0", "< 0"), ('"ALTO"', '"BAJO"'), ('"OK"', '"ALARMA"')]
vivos = 0; total = 0; detalle = []
for a, b in MUT:
    pos = 0
    while True:
        i = FUENTE.find(a, pos)
        if i < 0: break
        m = FUENTE[:i] + b + FUENTE[i + len(a):]
        pos = i + len(a)
        if m == FUENTE: continue
        try: ok = correr(m, PRUEBAS) == len(PRUEBAS)
        except SyntaxError: continue
        total += 1; vivos += ok
        if ok: detalle.append(f"{a!r}->{b!r} en pos {i}")
print(f"Mutantes = {total} ; muertos = {total-vivos} ; vivos = {vivos} ; puntuacion de mutacion = {100*(total-vivos)/total:.1f} %")
for d in detalle: print("  vivo:", d)
# Sin las pruebas de frontera (5 y 6) la puntuacion cae
def punt(pr):
    v = t = 0
    for a, b in MUT:
        pos = 0
        while True:
            i = FUENTE.find(a, pos)
            if i < 0: break
            m = FUENTE[:i] + b + FUENTE[i + len(a):]; pos = i + len(a)
            if m == FUENTE: continue
            try: ok = correr(m, pr) == len(pr)
            except SyntaxError: continue
            t += 1; v += ok
    return 100 * (t - v) / t
print(f"Puntuacion sin pruebas de frontera = {punt(PRUEBAS[:4]):.1f} % ; con todas = {punt(PRUEBAS):.1f} %")
assert correr(FUENTE, PRUEBAS) == len(PRUEBAS)
assert punt(PRUEBAS) > punt(PRUEBAS[:4])
print("Pruebas superadas.")
