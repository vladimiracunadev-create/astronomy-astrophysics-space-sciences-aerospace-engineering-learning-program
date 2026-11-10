"""B88-C22: interrupciones anidadas, latencia y pila (SINTETICO, simulacion por eventos de 1 us)."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: tres interrupciones inventadas (unidades: us)")

# (nombre, prioridad (mayor = mas urgente), instante de llegada, duracion, bytes de pila por marco)
INT = [("TIMER", 3, 100, 40, 32), ("UART", 2, 110, 60, 48), ("ADC", 1, 120, 30, 40), ("TIMER2", 3, 160, 20, 32)]
def simular(anidar):
    t = 0; pila = []; fin = {}; inicio = {}; maxpila = 0; pend = sorted(INT, key=lambda x: x[2])
    activas = []  # [nombre, prio, restante, bytes]
    llegadas = {n: a for n, p, a, d, b in INT}
    cola = []
    for t in range(0, 600):
        for n, p, a, d, b in INT:
            if a == t: cola.append([n, p, d, b])
        # elegir quien corre
        candidatos = cola + activas
        if not candidatos: continue
        if activas and not anidar:
            actual = activas[-1]
        else:
            lista = cola + (activas[-1:] if activas else [])
            actual = max(lista, key=lambda x: (x[1], -llegadas[x[0]]))
        if actual in cola:
            cola.remove(actual); activas.append(actual); inicio.setdefault(actual[0], t)
            maxpila = max(maxpila, sum(x[3] for x in activas))
        elif actual is not activas[-1]:
            activas.remove(actual); activas.append(actual)
        actual[2] -= 1
        if actual[2] == 0:
            activas.remove(actual); fin[actual[0]] = t + 1
    return inicio, fin, maxpila
for anid in (True, False):
    ini, fin, mp = simular(anid)
    print(f"Anidamiento {'permitido' if anid else 'prohibido':10s}: pila maxima = {mp:3d} B")
    for n, p, a, d, b in INT:
        print(f"   {n:6s} prio {p} llega {a:3d} inicia {ini[n]:3d} fin {fin[n]:3d} latencia = {ini[n]-a:3d} us respuesta = {fin[n]-a:3d} us")
ini, fin, mp = simular(True)
lat_max = {n: ini[n] - a for n, p, a, d, b in INT}
assert lat_max["TIMER"] == 0 and lat_max["ADC"] > 0
# Cota de pila: suma de los marcos de una prioridad de cada nivel
cota = 32 + 48 + 40
print(f"Cota de pila (un marco por nivel) = {cota} B ; observada con anidamiento = {mp} B")
assert mp <= cota
print("Pruebas superadas.")
