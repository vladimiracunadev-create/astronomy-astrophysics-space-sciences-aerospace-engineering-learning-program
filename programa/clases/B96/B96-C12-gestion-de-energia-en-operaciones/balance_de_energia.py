"""B96-C12: balance de energia operativo SINTETICO de un satelite en LEO con eclipse."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: paneles, bateria y cargas ficticios; eclipse de beta = 0 en orbita de 550 km")
MU = 398600.4418; RE = 6378.137; h = 550.0; a = RE + h
P = 2*math.pi*math.sqrt(a**3/MU)
t_ecl = P*math.acos(math.sqrt(h*h + 2*RE*h)/a)/math.pi
t_sol = P - t_ecl
print(f"Periodo = {P/60:.2f} min ; eclipse = {t_ecl/60:.2f} min ; luz = {t_sol/60:.2f} min")
P_arr = 45.0        # W en luz (media orbital de generacion, ya con factor de apuntamiento)
P_base = 16.0       # W carga base
P_pay = 14.0        # W carga util cuando opera
CAP = 40.0          # Wh de bateria
eta = 0.92          # eficiencia de carga
def simula(min_pay_luz, min_pay_ecl, n_orb=30, dt=10.0, soc0=1.0):
    soc = soc0*CAP; dod_min = CAP; pasos = int(P/dt); hist = []
    for o in range(n_orb):
        dod_orb = 0.0
        for k in range(pasos):
            t = k*dt
            en_luz = t >= t_ecl
            t_rel = (t - t_ecl) if en_luz else t
            pay = (t_rel < min_pay_luz*60) if en_luz else (t_rel < min_pay_ecl*60)
            carga = P_base + (P_pay if pay else 0.0)
            if en_luz: dE = (P_arr*eta - carga)*dt/3600
            else: dE = -carga*dt/3600
            soc = min(CAP, soc + dE)
            dod_min = min(dod_min, soc)
        hist.append(soc)
    return hist, 1 - dod_min/CAP
casos = [("solo base", 0, 0), ("carga 20 min en luz", 20, 0), ("carga 20 min en eclipse", 0, 20), ("carga 30 min en eclipse", 0, 30)]
print(f"{'Caso':26s} {'SOC fin orbita 30':>18s} {'DoD maxima':>11s}")
res = {}
for nom, ml, me in casos:
    hist, dod = simula(ml, me)
    res[nom] = (hist, dod)
    print(f"{nom:26s} {hist[-1]/CAP*100:17.1f}% {dod*100:10.1f}%")
# comprobacion analitica de la DoD de un solo eclipse partiendo de bateria llena
for nom, ml, me in casos:
    e_ecl = (P_base*t_ecl + P_pay*me*60)/3600
    dod_a = e_ecl/CAP
    dod_s = res[nom][1]
    print(f"  {nom:26s} DoD analitica = {dod_a*100:5.1f}% ; simulada = {dod_s*100:5.1f}%")
    assert abs(dod_a - dod_s) < 0.01
# balance orbital neto
E_in = P_arr*eta*t_sol/3600
for nom, ml, me in casos:
    E_out = (P_base*P + P_pay*(ml + me)*60)/3600
    print(f"  {nom:26s} entrada = {E_in:5.2f} Wh ; salida = {E_out:5.2f} Wh ; neto = {E_in - E_out:+5.2f} Wh/orbita")
print(f"Criterio sintetico DoD <= 30 %: " + ", ".join(f"{n}: {'cumple' if res[n][1] <= 0.30 else 'NO'}" for n in res))
assert all(res[n][1] <= 0.5 for n in res)
print("Pruebas superadas.")
