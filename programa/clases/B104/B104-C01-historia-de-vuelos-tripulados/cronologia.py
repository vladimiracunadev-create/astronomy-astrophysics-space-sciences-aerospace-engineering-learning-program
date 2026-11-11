#!/usr/bin/env python3
"""B104-C01: periodo orbital de Kepler y vueltas por dia para leer una cronologia de vuelos tripulados.
Modelo SINTETICO/ILUSTRATIVO: orbitas de ejemplo; mu y radio son constantes estandar (no consultadas en una fuente concreta)."""
import sys
import numpy as np

MU = 3.986004418e14      # m^3/s^2, parametro gravitacional de la Tierra (estandar)
RE = 6378.137e3          # m, radio ecuatorial (estandar)


def periodo(a):
    return 2 * np.pi * np.sqrt(a**3 / MU)


def vis_viva(r, a):
    return np.sqrt(MU * (2 / r - 1 / a))


print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO: orbitas de ejemplo (no son datos de una mision); mu y RE estandar")
casos = [
    ("circular 320 km (cota inferior de altitud de la ISS segun la pagina de NASA consultada)", 320e3, 320e3),
    ("circular 400 km (ilustrativa)", 400e3, 400e3),
    ("elipse 181 x 327 km (clase Vostok; valores NO consultados)", 181e3, 327e3),
    ("circular 35786 km (geoestacionaria, referencia)", 35786e3, 35786e3),
]
print("Caso | semieje a [km] | periodo [min] | vueltas/dia | v perigeo [km/s] | v apogeo [km/s]")
res = []
for nombre, hp, ha in casos:
    rp, ra = RE + hp, RE + ha
    a = (rp + ra) / 2
    T = periodo(a)
    res.append(T)
    print(f"{nombre}\n   {a/1e3:9.1f} | {T/60:8.2f} | {86400/T:8.3f} | {vis_viva(rp,a)/1e3:7.3f} | {vis_viva(ra,a)/1e3:7.3f}")

# Duracion total frente a periodo (clase Vostok): cociente ilustrativo con 108 min (valor NO consultado)
T_v = res[2] / 60
print(f"Cociente 108 min / periodo clase Vostok = {108 / T_v:.3f} (ilustrativo; la duracion de 108 min no se consulto)")
# Vueltas en 180 dias a 400 km
n180 = 180 * 86400 / res[1]
print(f"Vueltas en 180 dias a 400 km: {n180:.0f}")

# Pruebas
assert 90.0 < res[0] / 60 < 92.0, "periodo a 320 km fuera de 90-92 min"
assert res[0] < res[1] < res[3], "el periodo debe crecer con la altitud"
assert abs(res[3] / 3600 - 23.934) < 0.01, "geoestacionaria debe dar 23,93 h (dia sideral)"
r = RE + 400e3
assert abs(vis_viva(r, r) - 2 * np.pi * r / res[1]) < 1e-6, "vis-viva circular = 2 pi r / T"
assert 1.1 < 108 / T_v < 1.3
print("Pruebas superadas.")
