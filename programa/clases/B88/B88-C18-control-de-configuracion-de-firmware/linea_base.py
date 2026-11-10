"""B88-C18: linea base de firmware con hashes, diferencias y reproducibilidad (SINTETICO)."""
import hashlib, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: archivos fuente inventados en memoria")

def sha(b): return hashlib.sha256(b).hexdigest()
fuentes_v1 = {"main.c": b"int main(){return run();}\n", "aocs.c": b"/* AOCS v1 */ float kp=4.0;\n", "tm.c": b"/* TM */ int rate=1;\n", "cfg.h": b"#define VER 100\n"}
fuentes_v2 = dict(fuentes_v1); fuentes_v2["aocs.c"] = b"/* AOCS v1 */ float kp=4.5;\n"; fuentes_v2["cfg.h"] = b"#define VER 101\n"; fuentes_v2["nuevo.c"] = b"/* nuevo */\n"

def manifiesto(f): return {k: sha(v) for k, v in sorted(f.items())}
def linea_base(f):
    m = manifiesto(f)
    return sha("".join(f"{k}:{h}\n" for k, h in m.items()).encode())
m1, m2 = manifiesto(fuentes_v1), manifiesto(fuentes_v2)
print("Manifiesto v1:")
for k, h in m1.items(): print(f"  {k:8s} {h[:12]}")
print(f"ID de linea base v1 = {linea_base(fuentes_v1)[:16]} ; v2 = {linea_base(fuentes_v2)[:16]}")
# Diferencias
anad = sorted(set(m2) - set(m1)); quit_ = sorted(set(m1) - set(m2)); camb = sorted(k for k in m1 if k in m2 and m1[k] != m2[k])
print(f"Diferencias v1->v2: anadidos={anad} eliminados={quit_} modificados={camb}")
assert camb == ["aocs.c", "cfg.h"] and anad == ["nuevo.c"]

# Reproducibilidad de la compilacion: una "compilacion" determinista frente a una que incrusta la fecha
def compilar(f, incrustar_fecha=None):
    out = b"".join(f[k] for k in sorted(f))
    if incrustar_fecha is not None: out += f"BUILD:{incrustar_fecha}".encode()
    return out
a = sha(compilar(fuentes_v1)); b = sha(compilar(fuentes_v1))
c = sha(compilar(fuentes_v1, "2026-11-10T10:00")); d = sha(compilar(fuentes_v1, "2026-11-10T10:01"))
print(f"Compilacion determinista: dos corridas iguales = {a == b}")
print(f"Compilacion con fecha incrustada: dos corridas iguales = {c == d}")
# Sensibilidad: un bit cambiado en un archivo cambia la linea base
mod = dict(fuentes_v1); mod["tm.c"] = bytes([mod["tm.c"][0] ^ 1]) + mod["tm.c"][1:]
print(f"Un bit cambiado en tm.c: linea base distinta = {linea_base(mod) != linea_base(fuentes_v1)}")
# Cuantos bits difieren entre los dos hash (efecto avalancha)
x = int(sha(fuentes_v1["tm.c"]), 16) ^ int(sha(mod["tm.c"]), 16)
print(f"Bits distintos entre los SHA-256 antes/despues: {bin(x).count('1')} de 256")
assert a == b and c != d
print("Pruebas superadas.")
