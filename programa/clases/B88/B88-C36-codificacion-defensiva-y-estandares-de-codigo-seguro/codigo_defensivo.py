"""B88-C36: codificacion defensiva: enteros de ancho fijo, saturacion y analisis de entradas (SINTETICO, semilla 36)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: funciones inventadas; aritmetica de ancho fijo emulada")

def envolver(x, bits, signo):
    m = 1 << bits; x &= m - 1
    return x - m if signo and x >= m // 2 else x
def suma_wrap(a, b, bits=16, signo=True): return envolver(a + b, bits, signo)
def suma_sat(a, b, bits=16, signo=True):
    lo, hi = (-(1 << (bits - 1)), (1 << (bits - 1)) - 1) if signo else (0, (1 << bits) - 1)
    return max(lo, min(hi, a + b))
print("Casos de desbordamiento (int16):")
for a, b in ((30000, 5000), (-30000, -5000), (100, 200)):
    print(f"  {a:6d} + {b:6d}: envolvente = {suma_wrap(a, b):6d} ; saturada = {suma_sat(a, b):6d} ; exacta = {a+b}")
print("uint8: 250 + 10 ->", suma_wrap(250, 10, 8, False), "(envuelve) /", suma_sat(250, 10, 8, False), "(satura)")
# Propiedades con entradas aleatorias
random.seed(36)
N = 100000
viol = {"rango": 0, "monotonia": 0, "conmut": 0}
for _ in range(N):
    a = random.randint(-32768, 32767); b = random.randint(-32768, 32767); c = random.randint(-32768, 32767)
    s = suma_sat(a, b)
    if not -32768 <= s <= 32767: viol["rango"] += 1
    if b <= c and suma_sat(a, b) > suma_sat(a, c): viol["monotonia"] += 1
    if suma_sat(a, b) != suma_sat(b, a): viol["conmut"] += 1
print(f"Propiedades de la suma saturada en {N} casos aleatorios (violaciones): {viol}")
envol = sum(1 for _ in range(N) if suma_wrap(*(random.randint(-32768, 32767) for _ in range(2))) != 0 and False)
# la suma envolvente viola la monotonia
vm = 0
for _ in range(N):
    a = random.randint(-32768, 32767); b = random.randint(-32768, 32767); c = random.randint(b, 32767)
    if suma_wrap(a, b) > suma_wrap(a, c): vm += 1
print(f"La suma envolvente viola la monotonia en {vm} de {N} casos ({100*vm/N:.1f} %)")
assert all(v == 0 for v in viol.values()) and vm > 0
# Acceso con limites: indice y longitud validados
def leer(buf, i, n):
    if not (0 <= i and 0 <= n and i + n <= len(buf)): return None
    return buf[i:i + n]
buf = bytes(range(16))
casos = [(0, 16), (15, 1), (15, 2), (-1, 4), (4, -2), (16, 0), (8, 8), (8, 9)]
for i, n in casos: print(f"  leer(buf16, {i:3d}, {n:3d}) -> {'rechazado' if leer(buf, i, n) is None else 'ok'}")
assert leer(buf, 15, 2) is None and leer(buf, 8, 8) is not None
# Division: protegida
def div_seg(a, b, defecto=0): return defecto if b == 0 else a // b
print("div_seg(7, 0) =", div_seg(7, 0), "; div_seg(7, 2) =", div_seg(7, 2))
print("Pruebas superadas.")
