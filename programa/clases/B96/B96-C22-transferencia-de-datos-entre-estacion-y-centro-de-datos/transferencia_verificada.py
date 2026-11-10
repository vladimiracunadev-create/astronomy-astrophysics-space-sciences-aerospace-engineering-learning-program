"""B96-C22: transferencia estacion -> centro de datos SINTETICA: trozos, perdida, hash SHA-256 y plazo."""
import hashlib, random, statistics, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: archivo de 8 MiB pseudoaleatorio, enlace ficticio; semilla 96")
rng = random.Random(96)
datos = bytes(rng.getrandbits(8) for _ in range(8*1024*1024))
H0 = hashlib.sha256(datos).hexdigest()
CH = 64*1024
trozos = [datos[i:i+CH] for i in range(0, len(datos), CH)]
n = len(trozos)
print(f"Archivo = {len(datos)} B ; trozos = {n} de {CH} B ; SHA-256 = {H0[:16]}...")
# --- transferencia con corrupcion de bits; cada trozo lleva su hash
p_c = 0.02
def intento(t):
    if rng.random() < p_c:
        b = bytearray(t); b[rng.randrange(len(b))] ^= 1 << rng.randrange(8); return bytes(b)
    return t
recibido = []; reenvios = 0; detectados = 0
hash_trozo = [hashlib.sha256(t).hexdigest() for t in trozos]
for k, t in enumerate(trozos):
    while True:
        r = intento(t)
        if hashlib.sha256(r).hexdigest() == hash_trozo[k]: recibido.append(r); break
        detectados += 1; reenvios += 1
H1 = hashlib.sha256(b"".join(recibido)).hexdigest()
print(f"Reenvios por hash de trozo = {reenvios} ; trozos corruptos detectados = {detectados}")
print(f"SHA-256 del archivo reconstruido = {H1[:16]}... ; coincide: {H1 == H0}")
assert H1 == H0
# sin verificacion el archivo habria quedado corrupto
rng2 = random.Random(7)
sin = []
corruptos = 0
for t in trozos:
    if rng2.random() < p_c:
        b = bytearray(t); b[rng2.randrange(len(b))] ^= 1; sin.append(bytes(b)); corruptos += 1
    else: sin.append(t)
print(f"Sin verificacion: trozos corruptos = {corruptos} ; hash final coincide: {hashlib.sha256(b''.join(sin)).hexdigest() == H0}")
assert hashlib.sha256(b"".join(sin)).hexdigest() != H0
# --- plazo: volumen grande, enlace de 100 Mbit/s con eficiencia 0.9, perdida p por trozo de 4 MiB
V = 20e9*8          # bits (20 GB)
bw = 100e6*0.9      # bit/s utiles
ch_bits = 4*1024*1024*8
n_ch = V/ch_bits
t_ch = ch_bits/bw
for p in (0.0, 0.01, 0.05):
    esp = n_ch*t_ch/(1 - p)
    print(f"p = {p:4.2f}: tiempo esperado = {esp/3600:.3f} h ; ({n_ch:.0f} trozos de {t_ch:.3f} s)")
# Monte Carlo del tiempo con p = 5 %, 200 trozos
rr = random.Random(96); M = 4000; nn = 200
tt = []
for _ in range(M):
    ints = 0
    for _ in range(nn):
        ints += 1
        while rr.random() < 0.05: ints += 1
    tt.append(ints)
esp_i = nn/(1 - 0.05)
print(f"Intentos para {nn} trozos con p = 5 %: media simulada = {statistics.mean(tt):.2f} ; esperada = {esp_i:.2f}")
assert abs(statistics.mean(tt) - esp_i) < 0.5
plazo = 6.5*3600
print(f"Plazo = {plazo/3600:.1f} h ; transferencia con p = 5 % = {n_ch*t_ch/0.95/3600:.2f} h ; cumple: {n_ch*t_ch/0.95 <= plazo}")
print("Pruebas superadas.")
