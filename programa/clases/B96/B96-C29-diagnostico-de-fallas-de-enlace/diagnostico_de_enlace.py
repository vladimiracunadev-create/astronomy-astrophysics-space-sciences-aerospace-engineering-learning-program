"""B96-C29: diagnostico de fallas de enlace SINTETICO: diccionario de firmas y clasificacion por minima distancia (Monte Carlo)."""
import math, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: firmas y ruidos ficticios; semilla 96")
# firma = desviaciones respecto al enlace nominal: [dC/N0 (dB), desajuste de polarizacion (dB), residuo de frecuencia (kHz), varianza extra de ruido (dB)]
sig = {
 "Nominal":                    [0.0, 0.0, 0.0, 0.0],
 "Error de apuntamiento":      [-6.0, 0.0, 0.0, 0.0],
 "Desajuste de polarizacion":  [-3.0, -3.0, 0.0, 0.0],
 "Corrimiento de frecuencia":  [-2.0, 0.0, 8.0, 0.0],
 "Interferencia":              [-4.0, 0.0, 0.0, 5.0],
 "Potencia de transmision baja": [-8.0, 0.0, 0.0, 0.0],
}
sd = [1.0, 1.0, 1.5, 1.0]                  # desviacion del ruido de medicion por componente
nombres = list(sig)
def dist(x, f):
    return math.sqrt(sum(((a - b)/s)**2 for a, b, s in zip(x, f, sd)))
def clasifica(x):
    return min(nombres, key=lambda k: dist(x, sig[k]))
rng = random.Random(96)
M = 20000
conf = {a: {b: 0 for b in nombres} for a in nombres}
for a in nombres:
    for _ in range(M):
        x = [m + rng.gauss(0, s) for m, s in zip(sig[a], sd)]
        conf[a][clasifica(x)] += 1
print("Matriz de confusion (filas = verdadera; porcentaje clasificado como...):")
print(f"{'':30s}" + "".join(f"{n[:9]:>10s}" for n in nombres))
acc = {}
for a in nombres:
    fila = [100*conf[a][b]/M for b in nombres]
    acc[a] = conf[a][a]/M
    print(f"{a:30s}" + "".join(f"{v:10.2f}" for v in fila))
print(f"Exactitud media = {sum(acc.values())/len(acc)*100:.2f} %")
# comprobacion analitica: acierto >= 1 - sum_j Q(d_ij/2) (cota de union) para cada clase
def Q(x): return 0.5*math.erfc(x/math.sqrt(2))
for a in nombres:
    cota = 1 - sum(Q(dist(sig[a], sig[b])/2) for b in nombres if b != a)
    print(f"  {a:30s} acierto simulado = {acc[a]:.4f} ; cota inferior de union = {cota:.4f}")
    assert acc[a] >= cota - 0.01
# par mas parecido (menor distancia entre firmas)
par = min(((dist(sig[a], sig[b]), a, b) for i, a in enumerate(nombres) for b in nombres[i+1:]), key=lambda t: t[0])
print(f"Par de fallas mas dificil de distinguir: {par[1]} y {par[2]} (distancia = {par[0]:.2f} sigma)")
# efecto de una medicion adicional: bajar la desviacion de la polarizacion a 0.3
print("Si se mide mejor la polarizacion (sd 0.3 dB):")
sd[1] = 0.3
rng = random.Random(96); ok = 0
for _ in range(M):
    x = [m + rng.gauss(0, s) for m, s in zip(sig["Desajuste de polarizacion"], sd)]
    ok += clasifica(x) == "Desajuste de polarizacion"
print(f"  acierto del desajuste de polarizacion = {ok/M:.4f} (antes {acc['Desajuste de polarizacion']:.4f})")
assert ok/M >= acc["Desajuste de polarizacion"]
print("Pruebas superadas.")
