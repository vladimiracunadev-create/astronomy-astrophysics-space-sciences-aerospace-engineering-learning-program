"""B88-C34: campana de inyeccion de fallos con intervalo de Wilson (SINTETICO, semilla 34)."""
import math, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: un objetivo con 12 bytes protegidos por CRC-8, 1 byte de CRC y 3 bytes sin proteccion")

def crc8(d):
    c = 0
    for b in d:
        c ^= b
        for _ in range(8): c = ((c << 1) ^ 0x07) & 0xFF if c & 0x80 else (c << 1) & 0xFF
    return c
random.seed(34)
def nuevo():
    prot = bytes(random.getrandbits(8) for _ in range(12))
    return bytearray(prot + bytes([crc8(prot)]) + bytes(random.getrandbits(8) for _ in range(3)))
def chequeo(est):  # FDIR del objetivo: solo valida el CRC de los 12 primeros bytes
    return crc8(bytes(est[:12])) == est[12]
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h
for N in (100, 1000, 10000):
    det = sil = 0
    for _ in range(N):
        e = nuevo(); b = random.randrange(16 * 8)
        e[b // 8] ^= 1 << (b % 8)
        if not chequeo(e): det += 1
        else: sil += 1
    lo, hi = wilson(det, N)
    print(f"N={N:6d}: detectados={det:6d} silenciosos={sil:6d} cobertura={det/N:.4f} IC95%=[{lo:.4f}, {hi:.4f}] ancho={hi-lo:.4f}")
print(f"Cobertura teorica = 13/16 = {13/16:.4f} (el CRC detecta todo error de un bit en 13 bytes; 3 bytes sin proteccion)")
# Dos bits: el CRC-8 detecta casi todos
N = 10000; det = 0
for _ in range(N):
    e = nuevo(); a, b = random.sample(range(13 * 8), 2)
    for x in (a, b): e[x // 8] ^= 1 << (x % 8)
    det += not chequeo(e)
print(f"Dos bits dentro de los 13 bytes protegidos: detectados = {det}/{N}")
assert det > 0.99 * N
# Proteger los 3 bytes restantes
def chequeo2(est): return crc8(bytes(est[:12] + est[13:])) == est[12]
N = 5000; det = 0
for _ in range(N):
    prot = bytes(random.getrandbits(8) for _ in range(15)); e = bytearray(prot[:12] + bytes([crc8(prot[:12] + prot[12:])]) + prot[12:])
    b = random.randrange(16 * 8); e[b // 8] ^= 1 << (b % 8)
    det += not chequeo2(e)
print(f"Con los 15 bytes protegidos: cobertura de un bit = {det}/{N} = {det/N:.4f}")
assert det == N
print("Pruebas superadas.")
