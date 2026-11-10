#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C19. Coordinacion del espectro: interferencia de una estacion terrena hacia un satelite geoestacionario vecino,
razon I/N, Delta T/T y separacion orbital minima. Envolvente de antena y criterio de 6 % ILUSTRATIVOS (no se consultaron
las recomendaciones UIT-R ni el Apendice 8 del Reglamento). Datos SINTETICOS. k y c: NIST CODATA 2022 (consultadas)."""
import math, sys

C = 299_792_458.0
K = 1.380649e-23
RGEO = 42_164e3     # m, ILUSTRATIVO
RE = 6_371e3        # m, ILUSTRATIVO

def angulo_visto(delta_deg):
    """Angulo en una estacion ecuatorial (lon 0) entre dos satelites GEO separados delta grados de longitud."""
    st = (RE, 0.0, 0.0)
    a = (RGEO, 0.0, 0.0)
    d = math.radians(delta_deg)
    b = (RGEO * math.cos(d), RGEO * math.sin(d), 0.0)
    va = [a[i] - st[i] for i in range(3)]
    vb = [b[i] - st[i] for i in range(3)]
    cos = sum(va[i] * vb[i] for i in range(3)) / (math.sqrt(sum(x * x for x in va)) * math.sqrt(sum(x * x for x in vb)))
    return math.degrees(math.acos(max(-1.0, min(1.0, cos))))

def angulo_aprox(delta_deg):
    return delta_deg * RGEO / (RGEO - RE)     # aproximacion de angulos pequenos

def gan_fuera_eje(theta_deg, gmax_dbi=50.0):
    """Envolvente ILUSTRATIVA 32 - 25 log10(theta) dBi para theta >= 1 grado, limitada por el maximo."""
    if theta_deg < 1.0:
        return min(gmax_dbi, 32 - 25 * math.log10(max(theta_deg, 0.1)))
    return 32 - 25 * math.log10(theta_deg)

def interferencia(delta, f=14e9, eirp_dbw=60.0, g_sat_dbi=30.0, t_sis=500.0, bw=36e6):
    th = angulo_visto(delta)
    g_ee = gan_fuera_eje(th)
    g_eje = 50.0
    eirp_fuera = eirp_dbw - g_eje + g_ee
    d = RGEO - RE
    fspl = 20 * math.log10(4 * math.pi * d * f / C)
    i_dbw = eirp_fuera - fspl + g_sat_dbi
    n_dbw = 10 * math.log10(K * t_sis * bw)
    return {"th": th, "g_ee": g_ee, "i": i_dbw, "n": n_dbw, "in_db": i_dbw - n_dbw, "dtt": 10 ** ((i_dbw - n_dbw) / 10)}

def separacion_minima(umbral=0.06):
    lo, hi = 0.5, 30.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if interferencia(mid)["dtt"] > umbral:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def calcular():
    R = {"filas": {}}
    for d in (2.0, 3.0, 5.0, 8.0):
        R["filas"][d] = interferencia(d)
    R["sep6"] = separacion_minima(0.06)
    R["sep1"] = separacion_minima(0.01)
    R["umbral_in_db"] = 10 * math.log10(0.06)
    R["chk_ang"] = max(abs(angulo_visto(d) - angulo_aprox(d)) / angulo_visto(d) for d in (1.0, 2.0, 4.0))
    R["chk_mon"] = all(interferencia(a)["dtt"] > interferencia(b)["dtt"] for a, b in ((2, 3), (3, 5), (5, 8)))
    R["dtt_en_sep"] = interferencia(R["sep6"])["dtt"]
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("SINTETICO/ILUSTRATIVO: enlace ascendente 14 GHz, PIRE 60 dBW (antena de 50 dBi), G_sat 30 dBi, T_sis 500 K, B 36 MHz, GEO 42 164 km")
    print(f"{'sep [deg]':>10s}{'angulo [deg]':>14s}{'G fuera eje':>13s}{'I [dBW]':>10s}{'N [dBW]':>10s}{'I/N [dB]':>10s}{'DeltaT/T':>10s}")
    for d, r in R["filas"].items():
        print(f"{d:10.1f}{r['th']:14.3f}{r['g_ee']:13.2f}{r['i']:10.2f}{r['n']:10.2f}{r['in_db']:10.2f}{r['dtt']:10.4f}")
    print(f"Umbral Delta T/T = 6 % equivale a I/N = {R['umbral_in_db']:.2f} dB")
    print(f"Separacion minima para 6 %: {R['sep6']:.2f} grados ; para 1 %: {R['sep1']:.2f} grados")
    print(f"Delta T/T en la separacion minima = {R['dtt_en_sep']:.4f}")
    assert R["chk_mon"] and abs(R["dtt_en_sep"] - 0.06) < 1e-6 and R["chk_ang"] < 0.15
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
