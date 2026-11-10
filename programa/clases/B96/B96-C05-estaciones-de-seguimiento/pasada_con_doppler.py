"""B96-C05: azimut, elevacion, distancia y Doppler de una pasada (SINTETICO). Biblioteca comun: ../b96_comun.py."""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from b96_comun import *
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: orbita circular de 550 km, i = 97.6 grados; estacion en 40 N, 0 E; portadora 437.0 MHz; c = 299792.458 km/s")
h, inc, lat, lon, elmin, f0 = 550.0, 97.6, 40.0, 0.0, 10.0, 437.0e6
c = 299792.458
ps = pasadas(h, inc, lat, lon, elmin, dt=5.0)
mejor = max(ps, key=lambda p: p[2])
ini, fin, em = mejor
print(f"Pasada elegida: inicio = {ini:.0f} s ; fin = {fin:.0f} s ; elevacion maxima = {em:.1f} grados")
st = estacion(lat, lon)
def estado(t):
    return az_el_rng(eci_to_ecef(sat_eci(t, h, inc), t), st, lat, lon)
print("t[s]   az[gr]  el[gr]  d[km]   v_r[m/s]  Doppler[kHz]")
vs = []
t = ini
while t <= fin + 1e-9:
    az, el, r = estado(t)
    r2 = estado(t + 0.5)[2]; r1 = estado(t - 0.5)[2]
    vr = (r2 - r1)/1.0           # km/s (positivo = se aleja)
    dop = -f0*vr/c
    vs.append((t, az, el, r, vr, dop))
    if int(round(t - ini)) % 60 == 0 or t == fin:
        print(f"{t:6.0f} {az:7.1f} {el:7.1f} {r:7.1f} {vr*1e3:9.1f} {dop/1e3:9.2f}")
    t += 5.0
dmax = max(v[5] for v in vs); dmin = min(v[5] for v in vs)
print(f"Doppler: maximo = {dmax/1e3:.2f} kHz ; minimo = {dmin/1e3:.2f} kHz ; |variacion| = {(dmax-dmin)/1e3:.2f} kHz")
# comprobacion 1: el Doppler cruza cero cerca del minimo de distancia
tmin = min(vs, key=lambda v: v[3])
cruce = min(vs, key=lambda v: abs(v[5]))
print(f"Distancia minima = {tmin[3]:.1f} km en t = {tmin[0]:.0f} s ; cruce de Doppler en t = {cruce[0]:.0f} s")
assert abs(tmin[0] - cruce[0]) <= 10.0
# comprobacion 2: cota |Doppler| <= f0 * v_orbital / c
v = math.sqrt(MU/(RE+h))
cota = f0*v/c
print(f"Cota |Doppler| <= f0 v/c = {cota/1e3:.2f} kHz (v = {v:.3f} km/s)")
assert max(abs(dmax), abs(dmin)) <= cota
# comprobacion 3: el rango oblicuo en el borde coincide con la formula cerrada
d_borde = vs[0][3]; el_b = vs[0][2]
el = math.radians(el_b); r = RE + h
d_f = -RE*math.sin(el) + math.sqrt((RE*math.sin(el))**2 + r*r - RE*RE)
print(f"Distancia en el borde: simulada = {d_borde:.2f} km ; formula = {d_f:.2f} km")
assert abs(d_borde - d_f) < 0.5
print("Pruebas superadas.")
