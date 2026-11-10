"""B88-C09: modos de mision y aceptacion de telecomandos (maquina de estados SINTETICA)."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: modos, comandos y secuencia inventados")

MODOS = ["SAFE", "STANDBY", "NOMINAL", "SCIENCE"]
# comando -> (modos donde se acepta, modo resultante o None)
CMD = {
    "PING": ({"SAFE", "STANDBY", "NOMINAL", "SCIENCE"}, None),
    "TO_STANDBY": ({"SAFE"}, "STANDBY"),
    "TO_NOMINAL": ({"STANDBY"}, "NOMINAL"),
    "START_SCI": ({"NOMINAL"}, "SCIENCE"),
    "STOP_SCI": ({"SCIENCE"}, "NOMINAL"),
    "TO_SAFE": ({"STANDBY", "NOMINAL", "SCIENCE"}, "SAFE"),
}
print("Matriz estado x comando (A = aceptado, - = rechazado):")
print(f"{'':12s}" + " ".join(f"{m:8s}" for m in MODOS))
tot = 0
for c, (ok, _) in CMD.items():
    fila = ["A" if m in ok else "-" for m in MODOS]
    tot += fila.count("A")
    print(f"{c:12s}" + " ".join(f"{x:8s}" for x in fila))
print(f"Celdas aceptadas = {tot} de {len(CMD)*len(MODOS)}")

def crc8(data, poly=0x07):
    c = 0
    for b in data:
        c ^= b
        for _ in range(8): c = ((c << 1) ^ poly) & 0xFF if c & 0x80 else (c << 1) & 0xFF
    return c

class Nave:
    def __init__(self): self.modo = "SAFE"; self.seq = 0; self.reg = []
    def tc(self, nombre, seq, crc_ok=True):
        if not crc_ok: r = "RECHAZO crc"
        elif seq != (self.seq + 1) % 256 and nombre != "TO_SAFE": r = f"RECHAZO secuencia (esperada {(self.seq+1)%256})"
        elif self.modo not in CMD[nombre][0]: r = f"RECHAZO estado {self.modo}"
        else:
            if CMD[nombre][1]: self.modo = CMD[nombre][1]
            self.seq = seq; r = f"ACEPTADO -> {self.modo}"
        self.reg.append((nombre, seq, r)); return r

n = Nave()
guion = [("START_SCI", 1, True), ("TO_STANDBY", 1, True), ("TO_NOMINAL", 2, True), ("TO_NOMINAL", 2, True),
         ("TO_NOMINAL", 3, False), ("TO_NOMINAL", 3, True), ("START_SCI", 4, True), ("TO_SAFE", 200, True), ("PING", 1, True)]
print("Guion de telecomandos:")
for c, s, ok in guion:
    print(f"  {c:10s} seq={s:3d} crc={'ok' if ok else 'MAL':3s} -> {n.tc(c, s, ok)}")
assert n.modo == "SAFE" and tot == 11
assert crc8(b"123456789") == 0xF4
print(f"CRC-8 (poly 0x07) de '123456789' = 0x{crc8(b'123456789'):02X}")
print("Pruebas superadas.")
