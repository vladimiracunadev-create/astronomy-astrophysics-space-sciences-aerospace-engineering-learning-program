"""B88-C15: analisis estatico por AST con reglas inspiradas en Power of Ten (SINTETICO; analogo en Python)."""
import ast, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: dos fragmentos de codigo inventados (uno con defectos sembrados, uno corregido)")

MALO = '''
def leer(n):
    return n * 2

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def esperar(sensor):
    while True:
        if sensor():
            pass

def procesar(x):
    leer(x)
    y = x + 1
    return y
'''
BUENO = '''
def leer(n):
    assert n >= 0
    assert n < 1000
    return n * 2

def factorial(n):
    assert n >= 0
    assert n <= 20
    r = 1
    for i in range(2, n + 1):
        r = r * i
    return r

def esperar(sensor, max_iter):
    assert max_iter > 0
    assert callable(sensor)
    for _ in range(max_iter):
        if sensor():
            return True
    return False

def procesar(x):
    assert x >= 0
    assert x < 1000
    v = leer(x)
    return v + 1
'''
def analizar(src, max_lineas=60, min_asert=2):
    t = ast.parse(src); hall = []
    funcs = {f.name: f for f in ast.walk(t) if isinstance(f, ast.FunctionDef)}
    for n, f in funcs.items():
        llamadas = {c.func.id for c in ast.walk(f) if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)}
        if n in llamadas: hall.append((n, "R1 recursion directa"))
        for w in ast.walk(f):
            if isinstance(w, ast.While) and isinstance(w.test, ast.Constant) and w.test.value is True:
                if not any(isinstance(b, (ast.Break, ast.Return)) for b in ast.walk(w)):
                    hall.append((n, "R2 bucle sin cota"))
        nas = sum(isinstance(a, ast.Assert) for a in ast.walk(f))
        if nas < min_asert: hall.append((n, f"R5 aserciones {nas} < {min_asert}"))
        if f.end_lineno - f.lineno + 1 > max_lineas: hall.append((n, "R4 funcion larga"))
        for s in ast.walk(f):
            if isinstance(s, ast.Expr) and isinstance(s.value, ast.Call) and isinstance(s.value.func, ast.Name):
                if s.value.func.id in funcs and any(isinstance(r, ast.Return) and r.value is not None for r in ast.walk(funcs[s.value.func.id])):
                    hall.append((n, f"R7 valor devuelto de {s.value.func.id}() ignorado"))
    return hall
for nombre, src in (("MALO", MALO), ("BUENO", BUENO)):
    h = analizar(src)
    print(f"{nombre}: {len(h)} hallazgos")
    for n, r in h: print(f"   {n}: {r}")
assert len(analizar(MALO)) == 7
assert len(analizar(BUENO)) == 0
# falso negativo: una regla no ve un bucle acotado por una variable que nunca cambia
FN = "def f(s):\n    assert s\n    assert s\n    while s:\n        pass\n"
print(f"Falso negativo: while s sin cambio -> {len(analizar(FN))} hallazgos (la regla R2 solo ve 'while True')")
print("Pruebas superadas.")
