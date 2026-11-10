"""B96-C09: secuencia de pasada SINTETICA: camino critico y holgura frente a la duracion del contacto."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: actividades y duraciones ficticias; contacto de 425 s")
act = {
 "AOS_y_enganche": (20, []), "Verificar_estado": (30, ["AOS_y_enganche"]), "Cargar_tabla": (60, ["Verificar_estado"]),
 "Bajar_TM_historica": (150, ["Verificar_estado"]), "Ajustar_actitud": (45, ["Cargar_tabla"]),
 "Comandar_carga_util": (35, ["Ajustar_actitud"]), "Confirmar_TM": (40, ["Comandar_carga_util", "Bajar_TM_historica"]),
 "LOS_y_cierre": (15, ["Confirmar_TM"]),
}
orden = []; vis = set()
def visita(n):
    if n in vis: return
    for p in act[n][1]: visita(p)
    vis.add(n); orden.append(n)
for n in act: visita(n)
ES, EF = {}, {}
for n in orden:
    d, ps = act[n]; ES[n] = max([EF[p] for p in ps], default=0); EF[n] = ES[n] + d
fin = max(EF.values())
LF, LS = {}, {}
suc = {n: [m for m in act if n in act[m][1]] for n in act}
for n in reversed(orden):
    LF[n] = min([LS[m] for m in suc[n]], default=fin); LS[n] = LF[n] - act[n][0]
print(f"{'Actividad':20s} {'dur':>4s} {'ES':>4s} {'EF':>4s} {'holg':>5s}")
for n in orden:
    print(f"{n:20s} {act[n][0]:4d} {ES[n]:4d} {EF[n]:4d} {LS[n]-ES[n]:5d}")
crit = [n for n in orden if LS[n] - ES[n] == 0]
print("Camino critico:", " -> ".join(crit), f"; duracion = {fin} s")
ini = [n for n in act if not act[n][1]]
def caminos(n):
    if not suc[n]:
        yield [n]; return
    for m in suc[n]:
        for c in caminos(m): yield [n] + c
mejor = max(((sum(act[x][0] for x in c), c) for i in ini for c in caminos(i)), key=lambda t: t[0])
print(f"Camino mas largo por enumeracion = {mejor[0]} s")
assert mejor[0] == fin and set(mejor[1]) == set(crit)
ventana = 425
print(f"Ventana de contacto = {ventana} s ; holgura global = {ventana - fin} s ; cabe: {'SI' if fin <= ventana else 'NO'}")
assert fin <= ventana
for n in crit:
    print(f"  +30 s en {n:20s} -> duracion = {fin + 30} s ; holgura = {ventana - fin - 30} s")
print("Pruebas superadas.")
