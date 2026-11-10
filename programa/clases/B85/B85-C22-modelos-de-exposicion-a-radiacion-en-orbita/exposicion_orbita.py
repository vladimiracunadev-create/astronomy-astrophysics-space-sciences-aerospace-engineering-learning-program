# SPDX-License-Identifier: Apache-2.0
"""B85-C22: exposición a radiación en órbita con un mapa de flujo SINTÉTICO (no es AE9/AP9 ni ninguna herramienta real).

Consultado: R_E (NASA/NSSDC); de ESA SPENVIS solo su página de presentación (modelos de cinturones, plasmas, etc.).
SINTÉTICO: anomalía del Atlántico Sur como una gaussiana en (lon, lat), flujo creciente con la altitud, curva dosis-profundidad, órbitas.
Segunda vía: promedio por muestreo uniforme fino frente a muestreo aleatorio (semilla fija).
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

OMEGA_T = 2 * math.pi / 86164.1          # rad/s, rotacion terrestre (dia sideral, aritmetica)
GM = G_E * R_E ** 2
LON0, LAT0, SIG_LON, SIG_LAT = -45.0, -25.0, 30.0, 15.0     # grados, SINTETICOS
D_REF = 5.0e-3                           # Gy/dia a 500 km y 1 mm Al en el centro de la anomalia (SINTETICO)
ESC_ALT = 250.0                          # km, escala de crecimiento con la altitud (SINTETICA)
X0, P_DEPTH = 0.5, 1.5                   # mm Al, exponente de la curva dosis-profundidad (SINTETICOS)
BACKGROUND = 1.0e-5                      # Gy/dia fuera de la anomalia a 1 mm (SINTETICO)


def tasa_local(lon, lat, h_km, x_mm=1.0):
    dl = (lon - LON0 + 180.0) % 360.0 - 180.0
    g = math.exp(-0.5 * ((dl / SIG_LON) ** 2 + ((lat - LAT0) / SIG_LAT) ** 2))
    alt = math.exp((h_km - 500.0) / ESC_ALT)
    prof = ((1 + x_mm / X0) / (1 + 1.0 / X0)) ** (-P_DEPTH)
    return (D_REF * g * alt + BACKGROUND) * prof


def posicion(t, h_km, inc_deg):
    a = R_E + h_km * 1e3
    n = math.sqrt(GM / a ** 3)
    u = n * t
    i = math.radians(inc_deg)
    lat = math.degrees(math.asin(math.sin(i) * math.sin(u)))
    lon_i = math.atan2(math.cos(i) * math.sin(u), math.cos(u))
    lon = math.degrees(lon_i - OMEGA_T * t)
    return (lon + 180.0) % 360.0 - 180.0, lat, 2 * math.pi / n


def dosis_dia(h_km, inc_deg, x_mm=1.0, muestras=86400, aleatorio=False):
    rng = random.Random(20261110)
    s = 0.0
    for k in range(muestras):
        t = rng.random() * 86400.0 if aleatorio else (k + 0.5) * 86400.0 / muestras
        lon, lat, _ = posicion(t, h_km, inc_deg)
        s += tasa_local(lon, lat, h_km, x_mm)
    return s / muestras


def calcular():
    r = {"filas": []}
    for h, inc in ((500, 28.5), (500, 51.6), (500, 97.4), (800, 51.6), (1200, 51.6)):
        d = dosis_dia(h, inc, muestras=20000)
        r["filas"].append((h, inc, d, d * 365.25))
    r["periodo_500"] = posicion(0.0, 500, 51.6)[2] / 60.0
    r["profundidad"] = [(x, tasa_local(LON0, LAT0, 500, x) / tasa_local(LON0, LAT0, 500, 1.0)) for x in (0.5, 1.0, 2.0, 5.0)]
    r["fino"] = dosis_dia(500, 51.6, muestras=40000)
    r["grueso"] = dosis_dia(500, 51.6, muestras=10000)
    r["mc"] = dosis_dia(500, 51.6, muestras=40000, aleatorio=True)
    r["anual_2mm"] = dosis_dia(500, 51.6, x_mm=2.0, muestras=20000) * 365.25
    r["anual_1mm"] = dosis_dia(500, 51.6, x_mm=1.0, muestras=20000) * 365.25
    return r


def main():
    r = calcular()
    cabecera()
    print("Mapa de flujo SINTETICO (anomalia gaussiana en lon -45, lat -25; crece con exp(h/250 km)); NO es AE9/AP9 ni SPENVIS")
    print(f"Periodo a 500 km = {r['periodo_500']:.2f} min ; dosis de referencia {D_REF:.0e} Gy/dia en el centro, 1 mm Al")
    print(f"{'h [km]':>7}{'inc [deg]':>11}{'dosis [Gy/dia]':>16}{'dosis [Gy/anio]':>17}")
    for h, inc, d, a in r["filas"]:
        print(f"{h:>7}{inc:>11.1f}{d:>16.3e}{a:>17.3e}")
    print("Curva dosis-profundidad (centro de la anomalia, relativa a 1 mm): " + ", ".join(f"{x} mm: {v:.3f}" for x, v in r["profundidad"]))
    print(f"Convergencia a 500 km, 51.6 grados: 10000 muestras {r['grueso']:.4e} ; 40000 {r['fino']:.4e} ; Monte Carlo {r['mc']:.4e} Gy/dia")
    print(f"Con 2 mm Al en vez de 1 mm la dosis anual baja de {r['anual_1mm']:.3e} a {r['anual_2mm']:.3e} Gy/anio")
    comprobar(abs(r["fino"] - r["grueso"]) / r["fino"] < 0.02, "convergencia")
    comprobar(abs(r["mc"] - r["fino"]) / r["fino"] < 0.05, "Monte Carlo")
    comprobar(r["anual_2mm"] < r["anual_1mm"], "blindaje")
    fin()


if __name__ == "__main__":
    main()
