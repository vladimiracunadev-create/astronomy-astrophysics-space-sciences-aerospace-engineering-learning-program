"""B88-C23: capas del software de vuelo, dependencias y ejecutivo ciclico (SINTETICO)."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: modulos y dependencias inventados")

CAPA = {"hw": 0, "hal": 1, "so": 2, "servicios": 3, "aplicacion": 4}
MOD = {"uart_hw": "hw", "adc_hw": "hw", "hal_uart": "hal", "hal_adc": "hal", "rtos": "so", "tm_tc": "servicios", "fdir": "servicios",
       "aocs": "aplicacion", "energia": "aplicacion"}
DEP = [("hal_uart", "uart_hw"), ("hal_adc", "adc_hw"), ("rtos", "hal_uart"), ("tm_tc", "rtos"), ("tm_tc", "hal_uart"), ("fdir", "rtos"),
       ("aocs", "tm_tc"), ("aocs", "hal_adc"), ("energia", "fdir"), ("rtos", "tm_tc")]  # ultima: dependencia hacia arriba (defecto)
print(f"Modulos = {len(MOD)} ; dependencias = {len(DEP)}")
viol = [(a, b) for a, b in DEP if CAPA[MOD[a]] < CAPA[MOD[b]]]
saltos = [(a, b) for a, b in DEP if CAPA[MOD[a]] - CAPA[MOD[b]] > 1]
print("Dependencias hacia arriba (violan la capa):", viol)
print("Saltos de mas de una capa (a vigilar):", saltos)
# Ciclos
def hay_ciclo(dep):
    g = {}
    for a, b in dep: g.setdefault(a, []).append(b)
    est = {}
    def vis(n):
        est[n] = 1
        for m in g.get(n, []):
            if est.get(m) == 1: return True
            if est.get(m) is None and vis(m): return True
        est[n] = 2; return False
    return any(est.get(n) is None and vis(n) for n in MOD)
print("Hay ciclo de dependencias:", hay_ciclo(DEP))
DEP_OK = [d for d in DEP if d not in viol]
print("Tras quitar la dependencia hacia arriba: ciclo =", hay_ciclo(DEP_OK))
# Nivel topologico (profundidad desde el hardware)
niv = {}
def nivel(n):
    if n in niv: return niv[n]
    ds = [b for a, b in DEP_OK if a == n]
    niv[n] = 0 if not ds else 1 + max(nivel(d) for d in ds)
    return niv[n]
for n in MOD: nivel(n)
print("Nivel topologico:", dict(sorted(niv.items(), key=lambda x: x[1])))

# Ejecutivo ciclico: tareas (nombre, periodo ms, WCET ms)
T = [("AOCS", 100, 12), ("energia", 200, 10), ("tm_tc", 200, 15), ("fdir", 400, 25)]
menor = math.gcd(*[p for _, p, _ in T]); mayor = math.lcm(*[p for _, p, _ in T])
print(f"Ciclo menor = {menor} ms ; ciclo mayor = {mayor} ms ; tramas = {mayor//menor}")
carga = [0] * (mayor // menor)
for n, p, c in T:
    for k in range(mayor // menor):
        if (k * menor) % p == 0: carga[k] += c
for k, c in enumerate(carga): print(f"  trama {k}: carga = {c:2d} ms ({100*c/menor:5.1f} %)")
assert max(carga) <= menor and viol == [("rtos", "tm_tc")] and not hay_ciclo(DEP_OK)
print("Pruebas superadas.")
