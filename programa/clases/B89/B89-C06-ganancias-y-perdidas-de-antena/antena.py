#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C06. Ganancias y perdidas de antena: ganancia de apertura, haz, apuntamiento y error de superficie (Ruze).
Parametros de la antena SINTETICOS. c: NIST CODATA 2022 (consultada)."""
import math, sys

C = 299_792_458.0

def db(x):
    return 10 * math.log10(x)

def ganancia_db(d, f, eta, sigma=0.0):
    lam = C / f
    ruze = math.exp(-(4 * math.pi * sigma / lam) ** 2)
    return db(eta * ruze * (math.pi * d / lam) ** 2)

def haz(d, f):
    return 70.0 * (C / f) / d   # grados, aproximacion ILUSTRATIVA

def perd_punt_db(err, th3):
    return 12.0 * (err / th3) ** 2   # modelo gaussiano del lobulo principal

def calcular():
    d, eta, sigma = 2.0, 0.65, 0.3e-3
    R = {"d": d, "eta": eta, "sigma": sigma}
    R["g_x"] = ganancia_db(d, 8.4e9, eta)
    R["g_x_ruze"] = ganancia_db(d, 8.4e9, eta, sigma)
    R["g_ka"] = ganancia_db(d, 32e9, eta)
    R["g_ka_ruze"] = ganancia_db(d, 32e9, eta, sigma)
    R["ruze_x"] = R["g_x_ruze"] - R["g_x"]
    R["ruze_ka"] = R["g_ka_ruze"] - R["g_ka"]
    R["th_x"], R["th_ka"] = haz(d, 8.4e9), haz(d, 32e9)
    R["punt"] = {e: perd_punt_db(e, R["th_x"]) for e in (0.1, 0.5, 1.0)}
    R["punt_ka"] = {e: perd_punt_db(e, R["th_ka"]) for e in (0.1, 0.5, 1.0)}
    R["f_opt"] = C / (4 * math.pi * sigma)
    # segunda via: busqueda numerica del maximo de G(f)
    mejor = max(range(10_000_000, 200_000_000_000, 10_000_000), key=lambda f: ganancia_db(d, f, eta, sigma))
    R["f_opt_num"] = mejor
    R["g_opt"] = ganancia_db(d, R["f_opt"], eta, sigma)
    R["g_dec"] = ganancia_db(d, 8.4e9, eta) - ganancia_db(1.0, 8.4e9, eta)
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("SINTETICO: parabola D = 2 m, eficiencia 0.65, error de superficie rms 0.3 mm")
    print(f"  G(X 8.4 GHz) = {R['g_x']:.2f} dBi ; con Ruze = {R['g_x_ruze']:.2f} dBi (perdida {R['ruze_x']:.3f} dB)")
    print(f"  G(Ka 32 GHz) = {R['g_ka']:.2f} dBi ; con Ruze = {R['g_ka_ruze']:.2f} dBi (perdida {R['ruze_ka']:.3f} dB)")
    print(f"  Haz X = {R['th_x']:.3f} deg ; haz Ka = {R['th_ka']:.3f} deg")
    for e in R["punt"]:
        print(f"  error de apuntamiento {e:.1f} deg: perdida X = {R['punt'][e]:6.3f} dB ; Ka = {R['punt_ka'][e]:7.3f} dB")
    print(f"  frecuencia de ganancia maxima (Ruze) = {R['f_opt']/1e9:.2f} GHz ; busqueda numerica = {R['f_opt_num']/1e9:.2f} GHz")
    print(f"  G en el maximo = {R['g_opt']:.2f} dBi ; duplicar D suma {R['g_dec']:.3f} dB")
    assert abs(R["f_opt_num"] - R["f_opt"]) / R["f_opt"] < 1e-3
    assert abs(R["g_dec"] - 6.0206) < 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
