#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C15. Rastreo y Doppler: curva Doppler de una pasada de LEO en banda X, tasa de Doppler y razon de transpondedor coherente.
Geometria esferica sin rotacion terrestre; constantes ILUSTRATIVAS (mu, radio); razon 880/749 ILUSTRATIVA (no consultada). c: NIST (consultada)."""
import math, sys

C = 299_792.458     # km/s (NIST CODATA 2022: 299 792 458 m/s, consultada)
MU = 398600.4418    # km3/s2 ILUSTRATIVO
RE = 6371.0         # km ILUSTRATIVO
ALT = 600.0
A = RE + ALT
N = math.sqrt(MU / A ** 3)
LAT = math.radians(3.0)        # estacion a 3 grados de latitud: pasada casi cenital
EST = (RE * math.cos(LAT), 0.0, RE * math.sin(LAT))

def sat(t):
    u = N * t
    return (A * math.cos(u), A * math.sin(u), 0.0)

def rango(t):
    s = sat(t)
    return math.sqrt(sum((s[i] - EST[i]) ** 2 for i in range(3)))

def vel_radial(t, h=0.01):
    return (rango(t + h) - rango(t - h)) / (2 * h)      # km/s, derivada numerica

def vel_radial_analitica(t):
    s = sat(t)
    v = (-A * N * math.sin(N * t), A * N * math.cos(N * t), 0.0)
    rho = [s[i] - EST[i] for i in range(3)]
    d = math.sqrt(sum(x * x for x in rho))
    return sum(v[i] * rho[i] for i in range(3)) / d

def elevacion(t):
    s = sat(t)
    rho = [s[i] - EST[i] for i in range(3)]
    d = math.sqrt(sum(x * x for x in rho))
    up = [x / RE for x in EST]
    return math.degrees(math.asin(sum(rho[i] * up[i] for i in range(3)) / d))

def calcular():
    R = {"f_x": 8.4e9, "razon": 880 / 749}
    # tiempo de paso por el cenit: la estacion esta en (RE cos lat, 0, RE sin lat); el satelite en el plano ecuatorial pasa en t = 0
    t_pasada = [t / 2.0 for t in range(-500 * 2, 500 * 2 + 1)]   # segundos, de -500 a 500 en pasos de 0.5
    vis = [t for t in t_pasada if elevacion(t) >= 10.0]
    R["aos"], R["los"] = vis[0], vis[-1]
    f = {}
    for nombre, t in (("AOS", R["aos"]), ("TCA", 0.0), ("LOS", R["los"])):
        rr = vel_radial(t)
        f[nombre] = (rr, -R["f_x"] * rr / C)       # Doppler de ida
    R["doppler"] = f
    R["rmin"] = rango(0.0)
    R["emax"] = elevacion(0.0)
    # tasa de Doppler en el TCA
    h = 0.5
    dop = lambda t: -R["f_x"] * vel_radial(t) / C
    R["tasa_tca"] = (dop(h) - dop(-h)) / (2 * h)
    v = A * N
    R["tasa_recta"] = R["f_x"] * v * v / (C * R["rmin"])              # modelo de vuelo rectilineo
    R["tasa_corr"] = R["f_x"] * (v * v / R["rmin"] - MU / A ** 2) / C  # con la aceleracion centripeta
    R["chk_vel"] = max(abs(vel_radial(t) - vel_radial_analitica(t)) for t in range(-400, 401, 50))
    R["dop_dos_vias"] = {k: R["razon"] * 2 * (-vel_radial_analitica(t)) / C * 7.19e9 for k, t in (("AOS", R["aos"]), ("TCA", 0.0), ("LOS", R["los"]))}
    # estimacion de la distancia minima a partir de la pendiente (inversion del modelo corregido)
    R["rmin_est"] = None
    lo, hi = 100.0, 5000.0
    for _ in range(100):
        mid = (lo + hi) / 2
        pend = R["f_x"] * (v * v / mid - MU / A ** 2) / C
        if pend > abs(R["tasa_tca"]):
            lo = mid
        else:
            hi = mid
    R["rmin_est"] = (lo + hi) / 2
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print(f"ILUSTRATIVO/SINTETICO: orbita ecuatorial de {ALT:.0f} km, estacion a 3 grados de latitud, banda X 8.4 GHz, mascara 10 grados")
    print(f"AOS = {R['aos']:.1f} s ; LOS = {R['los']:.1f} s ; duracion = {(R['los']-R['aos'])/60:.2f} min ; elevacion maxima = {R['emax']:.2f} grados ; rango minimo = {R['rmin']:.2f} km")
    for k, (rr, fd) in R["doppler"].items():
        print(f"  {k}: velocidad radial = {rr:+8.4f} km/s ; Doppler de ida = {fd/1e3:+8.3f} kHz")
    print(f"Tasa de Doppler en el TCA = {R['tasa_tca']:.2f} Hz/s")
    print(f"  modelo rectilineo f v^2/(c rho) = {R['tasa_recta']:.2f} Hz/s ; con aceleracion centripeta = {R['tasa_corr']:.2f} Hz/s")
    print(f"  rango minimo recuperado desde la pendiente = {R['rmin_est']:.2f} km (real {R['rmin']:.2f} km)")
    print(f"Razon de transpondedor 880/749 = {R['razon']:.5f} ; Doppler de ida y vuelta (ascendente 7.19 GHz) en TCA = {R['dop_dos_vias']['TCA']/1e3:+.3f} kHz")
    print(f"Diferencia derivada numerica frente a analitica = {R['chk_vel']:.2e} km/s")
    assert R["chk_vel"] < 1e-6 and abs(abs(R["tasa_tca"]) - R["tasa_corr"]) / abs(R["tasa_tca"]) < 0.02
    assert abs(R["rmin_est"] - R["rmin"]) < 15.0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
