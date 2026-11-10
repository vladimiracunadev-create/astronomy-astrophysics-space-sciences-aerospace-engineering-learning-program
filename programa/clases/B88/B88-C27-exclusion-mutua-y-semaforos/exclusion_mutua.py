"""B88-C27: condicion de carrera, exclusion mutua y semaforo contador (SINTETICO, planificador aleatorio con semilla)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: tareas cooperativas simuladas con generadores")

class Mutex:
    def __init__(self): self.dueno = None
def tarea_incremento(nombre, comp, n, mutex=None):
    for _ in range(n):
        if mutex:
            while mutex.dueno is not None: yield
            mutex.dueno = nombre
        v = comp["x"]; yield        # lectura y expulsion posible
        comp["x"] = v + 1; yield    # escritura
        if mutex: mutex.dueno = None; yield
def ejecutar(tareas, semilla):
    rnd = random.Random(semilla); vivas = list(tareas)
    while vivas:
        t = rnd.choice(vivas)
        try: next(t)
        except StopIteration: vivas.remove(t)
for usar in (False, True):
    perdidas = []
    for s in range(200):
        c = {"x": 0}; m = Mutex() if usar else None
        ejecutar([tarea_incremento("A", c, 50, m), tarea_incremento("B", c, 50, m)], s)
        perdidas.append(100 - c["x"])
    print(f"{'con' if usar else 'sin'} mutex: corridas={len(perdidas)} con perdida={sum(1 for p in perdidas if p>0)} perdida media={sum(perdidas)/len(perdidas):.2f} de 100")
assert all(p == 0 for p in perdidas)

# Semaforo contador: productor-consumidor con buffer de capacidad 4
def prod(buf, vacio, lleno, n):
    for i in range(n):
        while vacio[0] == 0: yield
        vacio[0] -= 1; buf.append(i); lleno[0] += 1; yield
def cons(buf, vacio, lleno, n, out):
    for _ in range(n):
        while lleno[0] == 0: yield
        lleno[0] -= 1; out.append(buf.pop(0)); vacio[0] += 1; yield
for s in range(3):
    buf = []; out = []; vacio = [4]; lleno = [0]; maxbuf = [0]
    def vigilante():
        while True:
            maxbuf[0] = max(maxbuf[0], len(buf)); yield
    ts = [prod(buf, vacio, lleno, 1000), cons(buf, vacio, lleno, 1000, out), vigilante()]
    rnd = random.Random(s); vivas = ts[:2]
    while vivas:
        t = rnd.choice(vivas)
        next(vigilante.__call__()) if False else None
        try: next(t)
        except StopIteration: vivas.remove(t)
        maxbuf[0] = max(maxbuf[0], len(buf))
    print(f"semilla {s}: items entregados={len(out)} en orden={out == list(range(1000))} maximo en buffer={maxbuf[0]} (capacidad 4)")
    assert out == list(range(1000)) and maxbuf[0] <= 4
print("Pruebas superadas.")
