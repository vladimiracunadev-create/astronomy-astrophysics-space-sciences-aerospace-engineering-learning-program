"""B96-C16: gestion de datos cientificos SINTETICA: huecos por numero de secuencia, retransmision y niveles de procesamiento."""
import math, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: 10000 paquetes de 1 kB; perdida aleatoria; semilla 96")
random.seed(96)
N = 10000; PL = 1024      # paquetes y bytes por paquete
p = 0.03                  # probabilidad de perdida por paquete y por pasada
def huecos(recibidos):
    faltan = [i for i in range(N) if i not in recibidos]
    rangos = []
    for i in faltan:
        if rangos and rangos[-1][1] == i - 1: rangos[-1][1] = i
        else: rangos.append([i, i])
    return faltan, rangos
recibidos = set(i for i in range(N) if random.random() > p)
print("Pasada  recibidos  faltan  rangos_de_hueco  completitud")
historial = []
for k in range(1, 5):
    faltan, rangos = huecos(recibidos)
    historial.append(len(faltan))
    print(f"{k:6d} {len(recibidos):10d} {len(faltan):7d} {len(rangos):16d} {100*len(recibidos)/N:11.3f} %")
    for i in faltan:
        if random.random() > p: recibidos.add(i)
print(f"Faltantes por pasada = {historial}")
# esperado: N p^k tras k pasadas
esperado = [N*p**k for k in range(1, 5)]
print("Faltantes esperados N p^k =", [round(e, 2) for e in esperado])
assert abs(historial[0] - esperado[0]) < 4*math.sqrt(esperado[0])
assert abs(historial[1] - esperado[1]) < 4*math.sqrt(esperado[1]) + 1
assert historial[0] > historial[1] >= historial[2] >= historial[3]
# comprobacion independiente de los rangos: suma de longitudes = faltantes
f1, r1 = huecos(set(i for i in range(N) if i % 7 != 0))
assert sum(b - a + 1 for a, b in r1) == len(f1) and len(r1) == len(f1)
print(f"Prueba de huecos con paquetes multiplos de 7 perdidos: {len(f1)} faltantes en {len(r1)} rangos")
# niveles de procesamiento: volumen por nivel
vol0 = N*PL/1e6
niv = [("L0 (paquetes brutos)", 1.0), ("L1 (calibrado, sin duplicados)", 0.96), ("L2 (producto derivado)", 0.30)]
print("Nivel                           volumen [MB]")
for nom, f in niv:
    print(f"{nom:32s}{vol0*f:10.3f}")
print(f"Volumen bruto = {vol0:.3f} MB ({N} x {PL} B)")
assert abs(vol0 - N*PL/1e6) < 1e-12
print("Pruebas superadas.")
