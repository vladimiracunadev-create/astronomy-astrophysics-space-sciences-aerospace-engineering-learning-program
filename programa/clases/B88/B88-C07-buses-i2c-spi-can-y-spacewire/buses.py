"""B88-C07: tiempos de trama de I2C, SPI, CAN (con relleno de bits y CRC-15) y SpaceWire (SINTETICO)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: cargas y velocidades de ejemplo")

# I2C: inicio + direccion(7+R/W) + ACK + n bytes (8+ACK) + parada ~ 9*(1+n) bits + 2
def i2c(n, f=400e3):
    bits = 9 * (1 + n) + 2
    t = bits / f
    return bits, t, 8 * n / t
# SPI: 8 bits por byte, sin direccion ni ACK; 2 bits de reloj de guarda
def spi(n, f=10e6):
    bits = 8 * n + 2
    t = bits / f
    return bits, t, 8 * n / t
for n in (1, 4, 16):
    b, t, r = i2c(n); b2, t2, r2 = spi(n)
    print(f"n={n:2d} B  I2C@400k: {b:3d} bit {t*1e6:7.1f} us util {r/1e3:7.1f} kb/s | SPI@10M: {b2:3d} bit {t2*1e6:6.2f} us util {r2/1e6:5.2f} Mb/s")

# CAN 2.0A: CRC-15 y relleno
def crc15(bits):
    reg = 0
    for b in bits:
        nx = b ^ ((reg >> 14) & 1)
        reg = (reg << 1) & 0x7FFF
        if nx: reg ^= 0x4599
    return reg
def stuff(bits):
    out = []; run = 0; prev = None
    for b in bits:
        out.append(b)
        run = run + 1 if b == prev else 1
        prev = b
        if run == 5:
            s = 1 - b; out.append(s); prev = s; run = 1
    return out
def frame(idv, data):
    bits = [0] + [(idv >> (10 - i)) & 1 for i in range(11)] + [0, 0, 0] + [(len(data) >> (3 - i)) & 1 for i in range(4)]
    for byte in data: bits += [(byte >> (7 - i)) & 1 for i in range(8)]
    c = crc15(bits)
    bits += [(c >> (14 - i)) & 1 for i in range(15)]
    return bits
random.seed(7)
n = 8
base = 34 + 8 * n + 13
cota = (34 + 8 * n - 1) // 4
mx = 0; tot = 0; N = 5000
for _ in range(N):
    f = frame(random.randrange(2048), bytes(random.getrandbits(8) for _ in range(n)))
    assert len(f) == 34 + 8 * n
    s = len(stuff(f)) - len(f)
    mx = max(mx, s); tot += s
# peor caso construido: ID=0 y datos 0 -> muchos rellenos
f0 = frame(0, bytes(n)); s0 = len(stuff(f0)) - len(f0)
print(f"CAN n=8: bits sin relleno (con IFS) = {base}; cota de relleno = {cota}; maximo aleatorio = {mx}; medio = {tot/N:.2f}; ceros = {s0}")
for nn in (1, 4, 8):
    b = 34 + 8 * nn + 13
    w = b + (34 + 8 * nn - 1) // 4
    print(f"CAN n={nn}: {b} bit sin relleno ({b} us a 1 Mb/s) ; peor caso {w} bit ({w} us) ; util min {8*nn/w:.3f} Mb/s")
# SpaceWire: caracter de datos = 10 bit (supuesto del laboratorio), EOP = 4 bit
v = 100e6
for n in (8, 64, 1024):
    bits = (2 + n) * 10 + 4
    t = bits / v
    print(f"SpaceWire@100M n={n:4d} B (+2 B de ruta): {bits:5d} bit {t*1e6:7.2f} us util {8*n/t/1e6:6.2f} Mb/s")
assert mx <= cota and crc15([0] * 10) == 0 and s0 <= cota
print("Pruebas superadas.")
