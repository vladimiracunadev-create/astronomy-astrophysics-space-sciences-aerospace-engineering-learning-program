"""B88-C38: jerarquia de claves, derivacion HKDF y limites de uso por contador (BANCO SINTETICO, claves de juguete)."""
import hashlib, hmac, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: clave maestra de juguete; NUNCA usar claves reales en codigo ni en banco compartido")

MAESTRA = b"maestra-de-juguete-C38-0123456789abcdef"
def extract(sal, ikm): return hmac.new(sal, ikm, hashlib.sha256).digest()
def expand(prk, info, n):
    t = b""; ok = b""; i = 1
    while len(ok) < n:
        t = hmac.new(prk, t + info + bytes([i]), hashlib.sha256).digest(); ok += t; i += 1
    return ok[:n]
def derivar(maestra, contexto, epoca, n=32):
    prk = extract(b"sal-del-banco", maestra)
    return expand(prk, contexto + b"|epoca=" + str(epoca).encode(), n)
print("Claves derivadas (primeros 8 hex):")
ks = {}
for ctx in (b"TC-auth", b"TM-auth", b"firmware-firma"):
    for ep in (1, 2):
        k = derivar(MAESTRA, ctx, ep); ks[(ctx, ep)] = k
        print(f"  {ctx.decode():15s} epoca {ep}: {k.hex()[:8]}  longitud={len(k)} B")
assert len(set(ks.values())) == 6, "separacion de claves"
print("Todas las claves derivadas son distintas:", len(set(ks.values())) == 6)
assert derivar(MAESTRA, b"TC-auth", 1) == ks[(b"TC-auth", 1)]
print("Derivacion determinista: dos llamadas iguales = True")
k64 = derivar(MAESTRA, b"TC-auth", 1, 64)
print(f"HKDF-Expand de 64 B: longitud = {len(k64)} ; primeros 32 B == derivacion de 32 B: {k64[:32] == ks[(b'TC-auth', 1)]}")
# Limite de uso por contador: contador de 32 bit y tasa de comandos
for tasa in (0.1, 1, 10, 1000):
    anios = 2 ** 32 / tasa / 86400 / 365
    print(f"Contador de 32 bit a {tasa:6.1f} comandos/s: se agota en {anios:12.2f} anios")
# Rotacion: epoca cada N dias; claves a custodiar durante 5 anios
mision = 5 * 365
for per in (30, 90, 365):
    print(f"Rotacion cada {per:3d} dias: epocas durante 5 anios = {mision // per + 1}")
# Efecto de comprometer una clave derivada
print("Comprometer la clave de TC-auth epoca 1 no da la de TM-auth ni la maestra (por diseno de HKDF): claves distintas =", ks[(b'TC-auth', 1)] != ks[(b'TM-auth', 1)])
print("Pruebas superadas.")
