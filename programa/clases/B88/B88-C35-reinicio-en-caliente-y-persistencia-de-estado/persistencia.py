"""B88-C35: estado persistente con doble bufer y CRC ante corte de energia en cualquier byte (SINTETICO)."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: memoria no volatil virtual de dos ranuras de 12 bytes")

def crc16(d, c=0xFFFF):
    for b in d:
        c ^= b << 8
        for _ in range(8): c = ((c << 1) ^ 0x1021) & 0xFFFF if c & 0x8000 else (c << 1) & 0xFFFF
    return c
def registro(seq, datos):  # [seq(2) | datos(8) | crc(2)] = 12 bytes
    cuerpo = seq.to_bytes(2, "big") + bytes(datos)
    return cuerpo + crc16(cuerpo).to_bytes(2, "big")
def valido(r): return len(r) == 12 and crc16(r[:10]) == int.from_bytes(r[10:], "big")
def recuperar(nvm):
    cand = [(int.from_bytes(s[:2], "big"), s) for s in nvm if valido(s)]
    return max(cand)[1] if cand else None
# estado inicial: seq 1 en ranura 0, nada en la 1
viejo = registro(1, b"AAAAAAAA"); nuevo = registro(2, b"BBBBBBBB")
VAC = bytes([0xFF] * 12)
casos = 0; ok_viejo = 0; ok_nuevo = 0; mal = 0
# Esquema correcto: escribir el nuevo en la ranura inactiva (1), byte a byte, y cortar en cualquier punto
for corte in range(0, 13):
    s1 = bytearray(VAC); s1[:corte] = nuevo[:corte]
    est = recuperar([viejo, bytes(s1)])
    casos += 1
    if est == viejo: ok_viejo += 1
    elif est == nuevo: ok_nuevo += 1
    else: mal += 1
print(f"Doble bufer, corte en cada byte (0..12): casos={casos} recupera el viejo={ok_viejo} recupera el nuevo={ok_nuevo} sin estado valido={mal}")
assert mal == 0 and ok_nuevo == 1
# Esquema ingenuo: sobrescribir la unica ranura
mal2 = 0
for corte in range(0, 13):
    s = bytearray(viejo); s[:corte] = nuevo[:corte]
    e = recuperar([bytes(s)])
    if e not in (viejo, nuevo): mal2 += 1
print(f"Ranura unica sobrescrita, corte en cada byte: sin estado valido en {mal2} de 13 casos")
assert mal2 > 0
# Corte durante el borrado? segunda escritura: sobre la ranura 0 (la mas vieja)
s0 = bytearray(viejo); tercero = registro(3, b"CCCCCCCC")
mal3 = 0
for corte in range(0, 13):
    s0 = bytearray(viejo); s0[:corte] = tercero[:corte]
    e = recuperar([bytes(s0), nuevo])
    if e not in (nuevo, tercero): mal3 += 1
print(f"Segunda escritura sobre la ranura vieja, corte en cada byte: sin estado valido en {mal3} de 13 casos")
assert mal3 == 0
# Probabilidad de que un registro corrupto pase el CRC-16 por azar
print(f"Probabilidad de CRC valido por azar = 2^-16 = {2**-16:.3e}")
print("Pruebas superadas.")
