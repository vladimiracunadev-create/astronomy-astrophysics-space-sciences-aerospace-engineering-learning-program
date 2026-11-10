"""B88-C13: actualizacion segura con imagenes A/B, hash, MAC y reversion (SINTETICO)."""
import hashlib, hmac, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: imagenes de bytes inventados y una clave de juguete (NO usar en un sistema real)")

CLAVE = b"clave-de-juguete-solo-para-la-clase"
def firmar(img): return hmac.new(CLAVE, img, hashlib.sha256).digest()
def hash_(img): return hashlib.sha256(img).hexdigest()

class Equipo:
    def __init__(self):
        self.slots = {"A": b"firmware v1.0 " * 40, "B": b""}
        self.firmas = {"A": firmar(self.slots["A"]), "B": b""}
        self.activo = "A"; self.intentos = 0; self.version = "1.0"
    def actualizar(self, imagen, hash_esperado, firma, arranca_bien=True, bits_corruptos=0):
        otro = "B" if self.activo == "A" else "A"
        recibida = bytearray(imagen)
        for i in range(bits_corruptos): recibida[i * 7] ^= 1
        recibida = bytes(recibida)
        if hash_(recibida) != hash_esperado: return "RECHAZO: hash distinto (descarga corrupta)"
        if not hmac.compare_digest(firmar(recibida), firma): return "RECHAZO: firma invalida"
        self.slots[otro] = recibida; self.firmas[otro] = firma
        prev = self.activo; self.activo = otro; self.intentos = 0
        for _ in range(3):
            if arranca_bien: return f"OK: activo = {self.activo} (arranque correcto)"
            self.intentos += 1
        self.activo = prev
        return f"REVERSION: tras {3} arranques fallidos vuelve a {prev}"

img2 = b"firmware v2.0 " * 40
h2, f2 = hash_(img2), firmar(img2)
casos = [
    ("actualizacion buena", dict(imagen=img2, hash_esperado=h2, firma=f2)),
    ("descarga corrupta (3 bits)", dict(imagen=img2, hash_esperado=h2, firma=f2, bits_corruptos=3)),
    ("imagen modificada con hash recalculado", dict(imagen=img2 + b"X", hash_esperado=hash_(img2 + b"X"), firma=f2)),
    ("imagen buena pero no arranca", dict(imagen=img2, hash_esperado=h2, firma=f2, arranca_bien=False)),
]
res = {}
for nombre, kw in casos:
    e = Equipo()
    r = e.actualizar(**kw)
    res[nombre] = (r, e.activo)
    print(f"{nombre:42s} -> {r}")
assert res["actualizacion buena"][1] == "B"
assert res["descarga corrupta (3 bits)"][1] == "A"
assert res["imagen modificada con hash recalculado"][0].startswith("RECHAZO: firma")
assert res["imagen buena pero no arranca"][1] == "A"
print(f"SHA-256 de la imagen v2.0 = {h2[:16]}...  longitud = {len(img2)} B")
print("Pruebas superadas.")
