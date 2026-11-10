"""B88-C37: fuzzing en banco de un analizador SINTETICO propio con errores sembrados (semilla 37)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: analizador de mensajes inventado, ejecutado en proceso; solo objetivo propio del banco")

cobertura = set()
def objetivo(d):
    """Mensaje: [0xA5][tipo][longitud][carga...][suma]. Tres errores sembrados."""
    c = cobertura.add
    if len(d) < 4: c(1); return "corto"
    if d[0] != 0xA5: c(2); return "sync"
    c(3)
    tipo, n = d[1], d[2]
    if tipo == 1:
        c(4)
        if n > len(d) - 4: c(5); raise IndexError("BUG1: longitud mayor que el mensaje (lectura fuera de limites)")
        c(6); return "ok1"
    if tipo == 2:
        c(7)
        if n == 0: c(8); raise ZeroDivisionError("BUG2: division por longitud cero")
        c(9); return 255 // n
    if tipo == 3:
        c(10)
        if d[3] == 0x7F and n == 3: c(11); raise RuntimeError("BUG3: combinacion rara de campos")
        c(12); return "ok3"
    c(13); return "tipo?"
def ejecutar(d):
    try: objetivo(d); return None
    except Exception as e: return str(e).split(":")[0]
SEM = [bytes([0xA5, 1, 2, 9, 9, 0]), bytes([0xA5, 2, 1, 5, 0]), bytes([0xA5, 3, 1, 9, 0])]
def mutar(d, rnd):
    d = bytearray(d)
    for _ in range(rnd.randint(1, 3)):
        o = rnd.randrange(3)
        if o == 0 and d: d[rnd.randrange(len(d))] = rnd.getrandbits(8)
        elif o == 1 and d: d[rnd.randrange(len(d))] ^= 1 << rnd.randrange(8)
        elif o == 2: d.insert(rnd.randrange(len(d) + 1), rnd.getrandbits(8))
    return bytes(d)
def campana(guiada, N, semilla):
    global cobertura
    cobertura = set(); rnd = random.Random(semilla); corpus = list(SEM); bugs = {}; vista = set()
    for i in range(N):
        d = mutar(rnd.choice(corpus), rnd) if guiada else bytes(rnd.getrandbits(8) for _ in range(rnd.randint(0, 8)))
        antes = len(cobertura); r = ejecutar(d)
        if r and r not in bugs: bugs[r] = i
        if guiada and len(cobertura) > antes: corpus.append(d)
    return bugs, len(cobertura)
N = 20000
for guiada in (False, True):
    res = [campana(guiada, N, s) for s in range(10)]
    hall = [len(b) for b, _ in res]
    cov = [c for _, c in res]
    prim = [min(b.values()) for b, _ in res if b]
    print(f"{'guiado por cobertura' if guiada else 'aleatorio puro':22s}: bugs distintos por campana (10 semillas) = {hall} ; ramas medias = {sum(cov)/10:.1f}/13 ; primer hallazgo medio = {sum(prim)/len(prim) if prim else float('nan'):.0f} ejecuciones")
b0 = sum(len(campana(False, N, s)[0]) for s in range(10)); b1 = sum(len(campana(True, N, s)[0]) for s in range(10))
print(f"Total de hallazgos: aleatorio = {b0}, guiado = {b1}")
assert b1 >= b0
print("Pruebas superadas.")
