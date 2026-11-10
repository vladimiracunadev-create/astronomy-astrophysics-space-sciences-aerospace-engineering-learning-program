"""B88-C21: tabla de interfaz de mensajes (ICD) y consistencia productor-consumidor (SINTETICO)."""
import struct, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: dos mensajes inventados entre el computador y un sensor estelar")

# Campo: (nombre, tipo struct, unidad, escala) ; orden de bytes big-endian ('>')
ICD = {
  "ATT_QUAT": [("q0", "h", "-", 1/32767), ("q1", "h", "-", 1/32767), ("q2", "h", "-", 1/32767), ("q3", "h", "-", 1/32767), ("estado", "B", "enum", 1), ("t_ms", "I", "ms", 1)],
}
def tam(msg): return struct.calcsize(">" + "".join(c[1] for c in ICD[msg]))
def empaquetar(msg, valores):
    return struct.pack(">" + "".join(c[1] for c in ICD[msg]), *valores)
def desempaquetar(msg, b, fmt=None):
    f = fmt or ">" + "".join(c[1] for c in ICD[msg])
    return struct.unpack(f, b)
print(f"Mensaje ATT_QUAT: {tam('ATT_QUAT')} bytes = {8*tam('ATT_QUAT')} bit")
q = [0.5, -0.5, 0.5, 0.5]
cod = [round(v * 32767) for v in q]
paq = empaquetar("ATT_QUAT", cod + [2, 123456])
print("Bytes (hex):", paq.hex())
dec = desempaquetar("ATT_QUAT", paq)
q2 = [d * ICD["ATT_QUAT"][i][3] for i, d in enumerate(dec[:4])]
print("Cuaternion recuperado:", [round(v, 5) for v in q2], "; norma =", round(sum(v * v for v in q2) ** 0.5, 5))
print(f"Cuantizacion: LSB = {1/32767:.3e} ; error maximo = {0.5/32767:.3e}")

# Consumidor con orden de bytes equivocado (little-endian)
mal = desempaquetar("ATT_QUAT", paq, "<hhhhBI")
print("Consumidor little-endian lee:", mal[:4], "estado", mal[4], "t_ms", mal[5])
# Consumidor con campo de tiempo de 16 bit (solapa el tiempo)
mal2 = struct.unpack(">hhhhBH", paq[:11])
print(f"Consumidor con t_ms de 16 bit: t_ms = {mal2[5]} (se pierde el valor {123456})")
# Comprobacion de consistencia por mapa de bits
def mapa(msg, fmt=None):
    f = fmt or ">" + "".join(c[1] for c in ICD[msg]); off = 0; r = []
    for ch in f[1:]:
        s = struct.calcsize(">" + ch); r.append((off, off + s - 1)); off += s
    return r
a, b = mapa("ATT_QUAT"), mapa("ATT_QUAT", ">hhhhBH")
print("Mapa productor:", a); print("Mapa consumidor:", b)
disc = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
print("Campos con desfase de bytes:", disc if disc else "ninguno", "; longitudes:", a[-1][1] + 1, "vs", b[-1][1] + 1)
assert dec == tuple(cod + [2, 123456]) and mal[:4] != dec[:4] and mal2[5] != 123456
print("Pruebas superadas.")
