"""B96-C30: registro y auditoria de operaciones SINTETICO: bitacora con cadena de hashes y deteccion de manipulacion."""
import hashlib, json, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: operadores, acciones y marcas de tiempo ficticios (UTC fijo); semilla 96")
rng = random.Random(96)
OPS = ["op_ana", "op_beto", "ing_cris", "dir_dana"]
ACC = ["AOS", "LOS", "COMANDO", "APROBACION", "CAMBIO_DE_MODO", "NOTA"]
def encadena(entradas):
    prev = "0"*64; out = []
    for i, e in enumerate(entradas):
        cuerpo = {"n": i, "ts": e["ts"], "actor": e["actor"], "accion": e["accion"], "detalle": e["detalle"], "prev": prev}
        h = hashlib.sha256(json.dumps(cuerpo, sort_keys=True, ensure_ascii=True).encode()).hexdigest()
        out.append({**cuerpo, "hash": h}); prev = h
    return out
def verifica(reg):
    prev = "0"*64
    for i, r in enumerate(reg):
        if r["n"] != i or r["prev"] != prev: return False, i
        cuerpo = {k: r[k] for k in ("n", "ts", "actor", "accion", "detalle", "prev")}
        if hashlib.sha256(json.dumps(cuerpo, sort_keys=True, ensure_ascii=True).encode()).hexdigest() != r["hash"]: return False, i
        prev = r["hash"]
    return True, None
N = 60
t0 = 1_700_000_000
entradas = []
for i in range(N):
    entradas.append({"ts": t0 + 90*i + rng.randrange(60), "actor": rng.choice(OPS), "accion": rng.choice(ACC), "detalle": f"paso {i}"})
reg = encadena(entradas)
ok, pos = verifica(reg)
print(f"Registro de {N} entradas ; verificacion = {ok} ; hash final = {reg[-1]['hash'][:16]}...")
assert ok
# manipulaciones: modificar cada campo de cada entrada, borrar, reordenar, insertar
detectadas = 0; total = 0
for i in range(N):
    for campo, nuevo in (("actor", "intruso"), ("accion", "NOTA"), ("detalle", "otro"), ("ts", reg[i]["ts"] + 1)):
        r2 = [dict(x) for x in reg]
        if r2[i][campo] == nuevo: continue
        r2[i][campo] = nuevo; total += 1
        ok2, p2 = verifica(r2); detectadas += (not ok2)
for i in range(N - 1):                          # borrados (el ultimo se trata aparte)
    r2 = reg[:i] + reg[i+1:]; total += 1; detectadas += (not verifica(r2)[0])
for i in range(N - 1):                          # reordenados
    r2 = list(reg); r2[i], r2[i+1] = r2[i+1], r2[i]; total += 1; detectadas += (not verifica(r2)[0])
print(f"Manipulaciones probadas = {total} ; detectadas = {detectadas}")
assert detectadas == total
# el borrado de la ultima entrada NO se detecta con la cadena sola: se necesita el hash final anclado aparte
r2 = reg[:-1]
print(f"Borrar la ultima entrada: cadena valida = {verifica(r2)[0]} ; hash final distinto del anclado = {r2[-1]['hash'] != reg[-1]['hash']}")
assert verifica(r2)[0] and r2[-1]["hash"] != reg[-1]["hash"]
# consultas de auditoria
cmds = [r for r in reg if r["accion"] == "COMANDO"]
aprob = [r for r in reg if r["accion"] == "APROBACION"]
print(f"Comandos = {len(cmds)} ; aprobaciones = {len(aprob)} ; actores distintos = {len({r['actor'] for r in reg})}")
tiempos_ok = all(reg[i]["ts"] <= reg[i+1]["ts"] for i in range(N - 1))
print(f"Marcas de tiempo no decrecientes = {tiempos_ok}")
assert tiempos_ok
# muestreo de auditoria: tamano de muestra para detectar una tasa de defecto d con confianza 95 %
import math
for d in (0.10, 0.05, 0.02):
    nn = math.ceil(math.log(0.05)/math.log(1 - d))
    print(f"  defecto {d*100:4.1f} % -> muestra minima = {nn} entradas")
print("Pruebas superadas.")
