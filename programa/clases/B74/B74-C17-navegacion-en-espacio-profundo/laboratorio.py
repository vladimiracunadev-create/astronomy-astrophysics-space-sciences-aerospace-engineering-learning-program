#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C17: observabilidad angular en espacio profundo con Doppler de una estacion y con DDOR.

Constante consultada (NIST, 2026-11-10): c = 299 792 458 m/s. La velocidad angular de rotacion terrestre 7.2921159e-5 rad/s y el radio ecuatorial
6 378 137 m NO se consultaron en esta sesion (valores ilustrativos). Todo lo demas SINTETICO. Modelo: la nave esta lejos y su direccion (alfa, delta) es
fija; la estacion, a latitud 35 grados, gira con la Tierra; la velocidad de alcance por rotacion es
 rr(t) = -omega R cos(phi) cos(delta) sin(omega t + lam - alfa)   (signo convencional).
Se calcula la informacion de Fisher para (alfa, delta) con 8 horas de datos Doppler de velocidad de alcance (sigma 0.1 mm/s por muestra cada 60 s)
para declinaciones 0, 10, 30 y 60 grados. DDOR: una medida con sigma de retardo 0.1 ns (ILUSTRATIVO) sobre una linea de base B = 8 000 km
da sigma de angulo c sigma_tau / B (en el plano del cielo, a lo largo de la proyeccion de la linea de base). Tolerancia: sigma_delta
aumenta al disminuir |delta|; con DDOR en la direccion de la declinacion, la sigma combinada es menor que la del Doppler solo para delta = 0 (en mas de un factor 10).
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

C = 299792458.0
OM = 7.2921159e-5
R = 6378137.0
PHI = math.radians(35.0)
SIGV = 1e-4  # m/s


def rr(t, al, de, lam=0.0):
    return -OM * R * math.cos(PHI) * math.cos(de) * np.sin(OM * t + lam - al)


def fisher_doppler(de, al=1.0):
    t = np.arange(-4 * 3600, 4 * 3600, 60.0)
    eps = 1e-7
    J = np.column_stack([
        (rr(t, al + eps, de) - rr(t, al - eps, de)) / (2 * eps),
        (rr(t, al, de + eps) - rr(t, al, de - eps)) / (2 * eps)])
    return J.T @ J / SIGV**2


def main():
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (geometria y ruido SINTETICOS)",
           f"Doppler de una estacion (latitud 35 grados, 8 h, sigma_v = {SIGV*1e3:.1f} mm/s) ; DDOR: sigma_retardo = 0.1 ns, B = 8000 km"]
    res = {}
    out.append("delta [deg]   sigma_alfa [nrad]   sigma_delta [nrad]   cociente delta/alfa   sigma_delta con DDOR [nrad]")
    sd_ddor = C * 0.1e-9 / 8.0e6  # rad
    res["ddor_nrad"] = sd_ddor * 1e9
    out_sd = []
    for d in (0.0, 10.0, 30.0, 60.0):
        F = fisher_doppler(math.radians(d))
        # el Doppler de una estacion puede ser casi singular en delta = 0 si sigma_delta es muy grande; se regulariza con una previa muy debil (1 rad)
        Fp = F + np.diag([1.0, 1.0]) / 1.0**2
        P = np.linalg.inv(Fp)
        sa, sd = math.sqrt(P[0, 0]), math.sqrt(P[1, 1])
        # DDOR en la direccion de delta (informacion adicional)
        Fc = Fp + np.diag([0.0, 1 / sd_ddor**2])
        sdc = math.sqrt(np.linalg.inv(Fc)[1, 1])
        txt_d = "sin informacion" if sd > 0.5 else f"{sd*1e9:.2f}"
        txt_r = "--" if sd > 0.5 else f"{sd/sa:.1f}"
        out.append(f"{d:9.0f}   {sa*1e9:15.2f}   {txt_d:>16s}   {txt_r:>17s}   {sdc*1e9:21.2f}")
        res[f"sa{int(d)}"] = sa * 1e9; res[f"sd{int(d)}"] = sd * 1e9; res[f"sdc{int(d)}"] = sdc * 1e9
        out_sd.append(sd)
    out.append(f"Angulo DDOR = c sigma_tau / B = {res['ddor_nrad']:.2f} nrad ; a 1.0e8 km equivale a {sd_ddor*1e8:.2f} km")
    res["ddor_km"] = sd_ddor * 1e8
    ok = out_sd[0] > out_sd[1] > out_sd[2] > out_sd[3] and res["sd0"] / res["sdc0"] > 10
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
