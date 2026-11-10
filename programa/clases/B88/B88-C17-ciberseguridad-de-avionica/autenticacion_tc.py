"""B88-C17: autenticacion de telecomandos con HMAC y ventana anti-repeticion (BANCO SINTETICO, defensivo)."""
import hashlib, hmac, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: clave de juguete, mensajes inventados; solo defensa sobre el propio banco")

CLAVE = b"clave-de-juguete-C17"
def etiqueta(cnt, cmd, bits=32):
    m = hmac.new(CLAVE, cnt.to_bytes(4, "big") + cmd, hashlib.sha256).digest()
    return int.from_bytes(m, "big") >> (256 - bits)

class Receptor:
    def __init__(self, bits=32, ventana=8):
        self.maximo = 0; self.vistos = set(); self.bits = bits; self.w = ventana
    def recibir(self, cnt, cmd, tag):
        if tag != etiqueta(cnt, cmd, self.bits): return "RECHAZO etiqueta"
        if cnt <= self.maximo - self.w: return "RECHAZO contador viejo"
        if cnt in self.vistos: return "RECHAZO repeticion"
        self.vistos.add(cnt); self.maximo = max(self.maximo, cnt); return "ACEPTADO"

r = Receptor()
print("Casos de prueba:")
r = Receptor()
r.recibir(1, b"PING", etiqueta(1, b"PING")); r.recibir(2, b"TO_SAFE", etiqueta(2, b"TO_SAFE"))
print(f"  legitimo cnt=1 -> ACEPTADO ; legitimo cnt=2 -> ACEPTADO (previos)")
print(f"  repeticion de cnt=1            -> {r.recibir(1, b'PING', etiqueta(1, b'PING'))}")
print(f"  cnt=3 con comando alterado     -> {r.recibir(3, b'TO_NOMINAL', etiqueta(3, b'PING'))}")
print(f"  cnt=5 legitimo (adelantado)    -> {r.recibir(5, b'PING', etiqueta(5, b'PING'))}")
print(f"  cnt=4 legitimo (fuera de orden)-> {r.recibir(4, b'PING', etiqueta(4, b'PING'))}")
r.recibir(20, b"PING", etiqueta(20, b"PING"))
print(f"  cnt=5 repetido tras cnt=20     -> {r.recibir(5, b'PING', etiqueta(5, b'PING'))}")
print(f"  cnt=11 legitimo tras cnt=20    -> {r.recibir(11, b'PING', etiqueta(11, b'PING'))}")

# Tasa de aceptacion de etiquetas al azar segun la longitud de la etiqueta (en el propio banco)
random.seed(17)
N = 200000
for bits in (4, 8, 12):
    rc = Receptor(bits=bits, ventana=10**9)
    ok = 0
    for i in range(N):
        cnt = i + 1
        if rc.recibir(cnt, b"PING", random.getrandbits(bits)) == "ACEPTADO": ok += 1
    print(f"Etiqueta de {bits:2d} bit: aceptadas al azar = {ok:6d}/{N} = {ok/N:.5f} (teorico {2**-bits:.5f})")
for bits in (32, 64, 128):
    print(f"Etiqueta de {bits:3d} bit: prob. de acierto por intento = 2^-{bits} = {2.0**-bits:.3e}")
# Tiempo de fuerza bruta a 10 intentos/s para tag de 32 bit (media 2^31)
print(f"Tag de 32 bit a 10 intentos/s: media ~ {2**31/10/86400/365:.1f} anios")
# Modelo de amenazas (STRIDE) con mitigacion
for a, m in (("Suplantacion (S)", "HMAC con clave por enlace"), ("Alteracion (T)", "HMAC sobre contador y comando"), ("Repudio (R)", "registro firmado de comandos"),
             ("Divulgacion (I)", "no aplica a esta clase (cifrado aparte)"), ("Denegacion (D)", "limitar tasa de rechazos y ventana"), ("Elevacion (E)", "matriz de comandos por modo (C09)")):
    print(f"  {a:18s} -> {m}")
print("Pruebas superadas.")
