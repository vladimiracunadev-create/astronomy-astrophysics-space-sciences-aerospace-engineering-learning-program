"""B96-C04: ventanas de visibilidad (planificacion de contactos), SINTETICO. Biblioteca comun: ../b96_comun.py."""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from b96_comun import *
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: orbita circular de 550 km, inclinacion 97.6 grados; estacion en 40 N, 0 E; Tierra esferica que rota")
h, inc, lat, lon, elmin = 550.0, 97.6, 40.0, 0.0, 10.0
ps = pasadas(h, inc, lat, lon, elmin, dt=5.0)
a = RE + h; P = 2*math.pi*math.sqrt(a**3/MU)
lam = math.acos(RE/a*math.cos(math.radians(elmin))) - math.radians(elmin)
dmax = P*lam/math.pi
print(f"Periodo = {P/60:.2f} min ; duracion maxima analitica (cenital, Tierra fija) = {dmax/60:.2f} min")
print("Pasada  inicio[s]   fin[s]  dur[min]  elev_max[grados]")
for k, (i, f, em) in enumerate(ps, 1):
    print(f"{k:4d} {i:10.0f} {f:9.0f} {(f-i)/60:9.2f} {em:10.1f}")
tot = sum(f-i for i, f, _ in ps)
print(f"Pasadas = {len(ps)} ; contacto total = {tot/60:.1f} min ; tiempo medio entre inicios = {(ps[-1][0]-ps[0][0])/(len(ps)-1)/60:.1f} min")
# comprobacion independiente 1: ninguna duracion supera la cota analitica (+5 % por rotacion terrestre y rejilla de 5 s)
assert all((f-i) <= dmax*1.05 for i, f, _ in ps)
# comprobacion 2: paso fino (1 s) reproduce el numero de pasadas
ps1 = pasadas(h, inc, lat, lon, elmin, dt=1.0)
print(f"Con paso de 1 s: pasadas = {len(ps1)} ; contacto total = {sum(f-i for i, f, _ in ps1)/60:.1f} min")
assert len(ps1) == len(ps) and abs(sum(f-i for i, f, _ in ps1) - tot) < 10*len(ps)
# planificacion: se conservan solo pasadas con elevacion maxima >= 25 grados
utiles = [p for p in ps if p[2] >= 25.0]
print(f"Pasadas con elevacion maxima >= 25 grados = {len(utiles)} ; contacto = {sum(f-i for i, f, _ in utiles)/60:.1f} min")
print("Pruebas superadas.")
