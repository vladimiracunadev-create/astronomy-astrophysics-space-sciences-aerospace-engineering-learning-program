"""B88-C30: cota de peor caso de tiempo de ejecucion (WCET) por camino mas largo, frente a medicion (SINTETICO)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: un grafo de flujo de control inventado; costes en ciclos")

# Funcion: for i in range(N<=8): if cond(i): A (30 ciclos) else B (12 ciclos); luego C (20); prologo 10
PRO, A, B, C, CMP, BUCLE = 10, 30, 12, 20, 3, 4   # CMP: coste de la comparacion; BUCLE: control de bucle por iteracion
NMAX = 8
def costo(entradas):
    c = PRO
    for x in entradas:
        c += BUCLE + CMP + (A if x % 3 == 0 else B)
    return c + C
# Cota estatica: camino mas largo con cota de bucle NMAX y tomando siempre la rama mas cara
wcet_est = PRO + NMAX * (BUCLE + CMP + max(A, B)) + C
print(f"Cota estatica = {PRO} + {NMAX}x({BUCLE}+{CMP}+{max(A,B)}) + {C} = {wcet_est} ciclos")
# Mejor caso estatico
bcet_est = PRO + 0 + C
print(f"Mejor caso estatico (0 iteraciones) = {bcet_est} ciclos")
random.seed(30)
muestras = []
for _ in range(100000):
    n = random.randint(0, NMAX)
    muestras.append(costo([random.randrange(30) for _ in range(n)]))
print(f"Medicion con 100000 entradas aleatorias: min={min(muestras)} media={sum(muestras)/len(muestras):.1f} max={max(muestras)}")
print(f"Pesimismo de la cota sobre el maximo medido = {wcet_est - max(muestras)} ciclos ({100*(wcet_est/max(muestras)-1):.1f} %)")
peor = costo([0] * NMAX)
print(f"Entrada de peor caso (todas las ramas caras, 8 iteraciones) = {peor} ciclos")
assert peor == wcet_est and max(muestras) <= wcet_est
# Efecto de la cache: factor de fallo de cache sobre la cota
for fallo in (1.0, 1.5, 2.0):
    print(f"  Factor de fallos de cache {fallo:.1f} -> WCET = {wcet_est*fallo:.0f} ciclos = {wcet_est*fallo/100e6*1e6:.2f} us a 100 MHz")
# Presupuesto de CPU: tarea periodica de 1 ms
for f in (50e6, 100e6):
    print(f"  A {f/1e6:.0f} MHz: WCET = {wcet_est/f*1e6:.2f} us ; utilizacion en 1 ms = {100*wcet_est/f/1e-3:.2f} %")
print("Pruebas superadas.")
