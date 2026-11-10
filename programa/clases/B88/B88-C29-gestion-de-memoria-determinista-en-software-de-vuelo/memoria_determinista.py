"""B88-C29: reserva estatica frente a montón (fragmentacion), fugas y pila maxima (SINTETICO, semilla fija)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: secuencias aleatorias de asignaciones con semilla 29")

TAM = 4096
class Monton:
    def __init__(self): self.libres = [(0, TAM)]; self.vivos = {}
    def alloc(self, n, id_):
        for i, (o, l) in enumerate(self.libres):
            if l >= n:
                self.vivos[id_] = (o, n)
                if l == n: self.libres.pop(i)
                else: self.libres[i] = (o + n, l - n)
                return True
        return False
    def free(self, id_):
        o, n = self.vivos.pop(id_)
        self.libres.append((o, n)); self.libres.sort()
        m = []
        for o, l in self.libres:
            if m and m[-1][0] + m[-1][1] == o: m[-1] = (m[-1][0], m[-1][1] + l)
            else: m.append((o, l))
        self.libres = m
    def frag(self):
        tot = sum(l for _, l in self.libres)
        return 0.0 if tot == 0 else 1 - max(l for _, l in self.libres) / tot
class Pool:
    def __init__(self, bloque, n): self.b = bloque; self.libres = list(range(n)); self.vivos = {}
    def alloc(self, n, id_):
        if n > self.b or not self.libres: return False
        self.vivos[id_] = self.libres.pop(); return True
    def free(self, id_): self.libres.append(self.vivos.pop(id_))
random.seed(29)
fallos = {"monton": 0, "pool": 0}; frag_max = 0.0
H, P = Monton(), Pool(64, 40)   # el pool: 40 bloques de 64 B = 2560 B
vivos = []; id_ = 0; pasos = 5000
for _ in range(pasos):
    if len(vivos) < 25 and random.random() < 0.55 or not vivos:
        n = random.choice([16, 24, 40, 56, 64]); id_ += 1
        if not H.alloc(n, id_): fallos["monton"] += 1
        if not P.alloc(n, id_): fallos["pool"] += 1
        vivos.append(id_)
    else:
        v = vivos.pop(random.randrange(len(vivos)))
        if v in H.vivos: H.free(v)
        if v in P.vivos: P.free(v)
    frag_max = max(frag_max, H.frag())
print(f"Pasos = {pasos} ; max objetos vivos = 25")
print(f"Montón (primer ajuste, {TAM} B): asignaciones fallidas = {fallos['monton']} ; fragmentacion externa maxima = {frag_max:.3f}")
print(f"Pool ({len(P.libres)+len(P.vivos)} bloques de 64 B): asignaciones fallidas = {fallos['pool']}")
# Fuga: el contador de bloques vivos crece
leak = Pool(64, 40); perdidos = 0
for i in range(100):
    if leak.alloc(16, i):
        if i % 3: leak.free(i)      # cada 3 no se libera (defecto)
    else: perdidos += 1
print(f"Pool con fuga: tras 100 ciclos quedan {len(leak.libres)} bloques libres ; fallos = {perdidos}")
# Pila maxima: grafo de llamadas sin recursion con marcos
MARCO = {"main": 32, "tarea": 64, "leer": 48, "formatear": 96, "crc": 24, "isr": 40}
LLAM = {"main": ["tarea"], "tarea": ["leer", "formatear"], "leer": ["crc"], "formatear": ["crc"], "crc": [], "isr": []}
def pila(n): return MARCO[n] + max([pila(m) for m in LLAM[n]] or [0])
print(f"Pila maxima desde main = {pila('main')} B (camino main->tarea->formatear->crc) ; + isr = {pila('main') + MARCO['isr']} B")
assert fallos["pool"] == 0 and pila("main") == 216
print("Pruebas superadas.")
