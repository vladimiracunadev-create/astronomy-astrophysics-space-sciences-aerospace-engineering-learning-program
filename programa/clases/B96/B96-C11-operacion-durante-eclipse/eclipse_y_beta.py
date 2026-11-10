"""B96-C11: eclipse de una orbita circular SINTETICA: formula analitica (sombra cilindrica) frente a muestreo numerico."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: orbita circular de 550 km; Sol a distancia infinita (rayos paralelos); sombra cilindrica; sin penumbra")
MU = 398600.4418; RE = 6378.137
h = 550.0; a = RE + h
P = 2*math.pi*math.sqrt(a**3/MU)
beta_c = math.degrees(math.asin(RE/a))
print(f"Periodo = {P/60:.3f} min ; beta critico = {beta_c:.2f} grados")
def fraccion(beta_deg):
    b = math.radians(beta_deg)
    if abs(beta_deg) >= beta_c: return 0.0
    return math.acos(math.sqrt(h*h + 2*RE*h)/(a*math.cos(b)))/math.pi
def numerico(beta_deg, N=200000):
    b = math.radians(beta_deg); s = (math.cos(b), 0.0, math.sin(b)); n = 0
    for k in range(N):
        u = 2*math.pi*(k+0.5)/N
        r = (a*math.cos(u), a*math.sin(u), 0.0)
        rs = r[0]*s[0] + r[1]*s[1] + r[2]*s[2]
        if rs < 0:
            perp2 = (r[0]-rs*s[0])**2 + (r[1]-rs*s[1])**2 + (r[2]-rs*s[2])**2
            if perp2 < RE*RE: n += 1
    return n/N
print("beta[gr]  fraccion_analitica  fraccion_numerica  eclipse[min]  luz[min]")
maxdif = 0.0
for beta in (0, 20, 40, 60, 66, 70, 75):
    fa = fraccion(beta); fn = numerico(beta)
    maxdif = max(maxdif, abs(fa - fn))
    print(f"{beta:7d} {fa:18.5f} {fn:18.5f} {fa*P/60:13.2f} {(1-fa)*P/60:9.2f}")
print(f"Diferencia maxima analitica/numerica = {maxdif:.2e}")
assert maxdif < 1e-4
assert fraccion(0) > fraccion(40) > fraccion(60) >= 0 and fraccion(80) == 0
print("Pruebas superadas.")
