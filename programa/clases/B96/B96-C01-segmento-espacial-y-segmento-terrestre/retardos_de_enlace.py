"""B96-C01: retardos de propagacion y ciclo comando-respuesta (distancias tipicas, SINTETICAS/redondeadas)."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: distancias redondeadas, sin efemerides reales")
c = 299792.458  # km/s (valor exacto del SI)
casos = [("LEO 550 km, cenit", 550.0), ("LEO 550 km, elev 10 grados", None), ("GEO 35786 km, subsatelite", 35786.0),
         ("Luna 384400 km", 384400.0), ("Marte cercano 5.5e7 km", 5.5e7), ("Marte lejano 4.0e8 km", 4.0e8)]
RE = 6378.137
def rango_oblicuo(h, el_deg):
    el = math.radians(el_deg); r = RE + h
    return -RE*math.sin(el) + math.sqrt((RE*math.sin(el))**2 + r*r - RE*RE)
res = []
for nom, d in casos:
    if d is None:
        d = rango_oblicuo(550.0, 10.0)
    t = d / c
    res.append((nom, d, t))
    print(f"{nom:30s} d = {d:14.1f} km ; ida = {t*1e3:12.3f} ms ; ida y vuelta = {2*t:10.3f} s")
# comprobacion independiente del rango oblicuo por ley de cosenos
d10 = rango_oblicuo(550.0, 10.0)
# angulo central lambda = acos(RE/(RE+h) cos el) - el
lam = math.acos(RE/(RE+550.0)*math.cos(math.radians(10.0))) - math.radians(10.0)
d_cos = math.sqrt(RE**2 + (RE+550.0)**2 - 2*RE*(RE+550.0)*math.cos(lam))
print(f"Rango oblicuo a 10 grados: cuadratica = {d10:.3f} km ; ley de cosenos = {d_cos:.3f} km")
assert abs(d10 - d_cos) < 1e-6
# volumen enlazable: tasa x tiempo
tasa = 9600.0; dur = 8*60.0  # bit/s, s (sintetico)
vol = tasa*dur/8/1e3
print(f"Pasada de {dur:.0f} s a {tasa:.0f} bit/s = {vol:.1f} kB (sin sobrecarga)")
# ciclo: comando en GEO con 2 s de procesamiento y 3 s de espera de operador
rtt_geo = 2*35786.0/c
ciclo = rtt_geo + 2.0 + 3.0
print(f"Ciclo comando-respuesta GEO con 2 s de proceso y 3 s de operador = {ciclo:.3f} s")
assert abs(res[2][2]*2 - rtt_geo) < 1e-12
assert 0.23 < res[2][2]*2 < 0.25 and res[4][2] > 180
print("Pruebas superadas.")
