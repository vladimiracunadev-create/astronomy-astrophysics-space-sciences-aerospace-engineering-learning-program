"""B88-C08: paquete de telemetria interna con CRC-16 y presupuesto de volumen (SINTETICO)."""
import random, struct, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: formato de paquete propio de la clase (NO es CCSDS ni PUS)")

def crc16(data, crc=0xFFFF):
    for b in data:
        crc ^= b << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) & 0xFFFF if crc & 0x8000 else (crc << 1) & 0xFFFF
    return crc
chk = crc16(b"123456789")
print(f"CRC-16 (poly 0x1021, init 0xFFFF) de '123456789' = 0x{chk:04X}")
assert chk == 0x29B1

# Cabecera: sync(2) tipo(1) seq(2) longitud(2) tiempo(4); cuerpo de n parametros de 16 bit; CRC(2)
def empaquetar(tipo, seq, t, params):
    cuerpo = struct.pack(f">{len(params)}H", *params)
    cab = struct.pack(">HBHHI", 0xEB90, tipo, seq & 0xFFFF, len(cuerpo), t)
    return cab + cuerpo + struct.pack(">H", crc16(cab + cuerpo))
def validar(p):
    return crc16(p[:-2]) == struct.unpack(">H", p[-2:])[0]
random.seed(11)
params = [random.randrange(65536) for _ in range(20)]
p = empaquetar(1, 7, 1_000_000, params)
print(f"Paquete HK de 20 parametros: {len(p)} bytes = {len(p)*8} bits ; valido={validar(p)}")

# Deteccion: 1 byte alterado, rafaga de 16 bit, 2 bits
det = {"1 byte": 0, "2 bits": 0}
N = 20000
for _ in range(N):
    q = bytearray(p); i = random.randrange(len(q)); q[i] ^= random.randrange(1, 256)
    det["1 byte"] += not validar(bytes(q))
    q = bytearray(p)
    for pos in random.sample(range(len(q) * 8), 2): q[pos // 8] ^= 1 << (pos % 8)
    det["2 bits"] += not validar(bytes(q))
print(f"Deteccion en {N} casos: 1 byte = {det['1 byte']}, 2 bits = {det['2 bits']}")

# Presupuesto: perfiles (nombre, parametros, periodo s)
perfiles = [("HK basico", 20, 1.0), ("Energia", 12, 0.5), ("Actitud", 30, 0.25)]
total = 0
for n, k, T in perfiles:
    L = 11 + 2 * k + 2
    bps = 8 * L / T
    total += bps
    print(f"{n:10s}: paquete {L:3d} B cada {T:4.2f} s -> {bps:7.1f} bit/s")
enlace = 4000.0
print(f"Total = {total:.1f} bit/s ; enlace interno de ejemplo = {enlace:.0f} bit/s ; ocupacion = {100*total/enlace:.1f} %")
assert det["1 byte"] == N
print("Pruebas superadas.")
