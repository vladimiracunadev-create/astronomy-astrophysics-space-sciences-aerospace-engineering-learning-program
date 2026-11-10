"""B88-C26: latencia de interrupcion y jitter con secciones criticas (SINTETICO, semilla fija)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: modelo de latencia inventado (unidades: us)")

random.seed(26)
BASE = 2.0            # entrada a la rutina (hardware + guardar contexto)
CRIT_MAX = 15.0       # duracion maxima de una seccion critica con interrupciones enmascaradas
P_CRIT = 0.30         # probabilidad de que la interrupcion llegue durante una seccion critica
ISR_ALTA = 8.0        # una rutina de mayor prioridad puede estar corriendo
P_ALTA = 0.10
N = 200000
lat = []
for _ in range(N):
    l = BASE
    if random.random() < P_CRIT: l += random.uniform(0, CRIT_MAX)   # espera restante de la seccion critica
    if random.random() < P_ALTA: l += random.uniform(0, ISR_ALTA)   # espera a una rutina mayor
    lat.append(l)
lat.sort()
def pct(p): return lat[int(p * (N - 1))]
mean = sum(lat) / N
print(f"Muestras = {N} ; minima = {lat[0]:.3f} us ; media = {mean:.3f} us ; mediana = {pct(0.5):.3f} us")
print(f"p99 = {pct(0.99):.3f} us ; p99.9 = {pct(0.999):.3f} us ; maxima observada = {lat[-1]:.3f} us")
cota = BASE + CRIT_MAX + ISR_ALTA
print(f"Cota analitica de peor caso = {BASE} + {CRIT_MAX} + {ISR_ALTA} = {cota:.1f} us")
print(f"Jitter (max - min) observado = {lat[-1]-lat[0]:.3f} us ; teorico = {cota-BASE:.1f} us")
# histograma
bins = [2, 3, 5, 8, 12, 17, 26]
hist = [0] * (len(bins) - 1)
for l in lat:
    for i in range(len(bins) - 1):
        if bins[i] <= l < bins[i + 1]: hist[i] += 1; break
    else:
        if l >= bins[-1]: pass
print("Histograma (us):")
for i in range(len(hist)):
    print(f"  [{bins[i]:2d}, {bins[i+1]:2d}) {hist[i]:7d} {100*hist[i]/N:6.2f} %")
# fraccion de interrupciones que superan un requisito
req = 10.0
exc = sum(1 for l in lat if l > req) / N
print(f"Fraccion con latencia > {req:.0f} us = {exc:.4f} ; veces por hora a 1 kHz = {exc*3.6e6:.0f}")
assert lat[-1] <= cota and lat[0] >= BASE
print("Pruebas superadas.")
