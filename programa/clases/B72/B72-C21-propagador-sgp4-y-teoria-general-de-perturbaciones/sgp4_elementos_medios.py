#!/usr/bin/env python3
"""B72-C21 — Propagador SGP4 y teoria general de perturbaciones.

NO es una implementacion de SGP4 completo. Reproduce las etapas de inicializacion que dan el sentido
de la teoria general de perturbaciones: formato de dos lineas (con un TLE SINTETICO construido aqui),
suma de comprobacion, conversion de movimiento medio de Kozai a Brouwer con las constantes WGS-72 de
Spacetrack Report 3, tasas seculares de J2 con esas constantes y clasificacion cercana/espacio profundo
(periodo menor o igual a 225 min). Unidades indicadas. Solo biblioteca estandar.
"""
import math
import sys

# Constantes WGS-72 del programa de Spacetrack Report No. 3 (Hoots y Roehrich, 1980)
XKE = 0.0743669161           # (radios terrestres)^(3/2) / min
XJ2 = 1.082616e-3
XKMPER = 6378.135            # km
AE = 1.0
K2 = 0.5 * XJ2 * AE ** 2
MIN_DIA = 1440.0


def suma_comprobacion(linea):
    s = 0
    for ch in linea[:68]:
        if ch.isdigit():
            s += int(ch)
        elif ch == "-":
            s += 1
    return s % 10


def construye_tle():
    """TLE SINTETICO (no es un objeto real): numero de catalogo 99999."""
    l1 = "1 99999U 26001A   26310.50000000  .00001000  00000-0  10000-4 0  999"
    l2 = (f"2 {99999:05d} {51.6:8.4f} {247.0:8.4f} {6000:07d} {130.0:8.4f} {325.0:8.4f} "
          f"{15.5:11.8f}{12345:5d}")
    assert len(l1) == 68 and len(l2) == 68, (len(l1), len(l2))
    return l1 + str(suma_comprobacion(l1)), l2 + str(suma_comprobacion(l2))


def lee_linea2(l2):
    """Campos de la linea 2 por columnas (formato descrito por Kelso, 1998)."""
    return dict(
        inc=float(l2[8:16]), raan=float(l2[17:25]), ecc=float("0." + l2[26:33].strip()),
        argp=float(l2[34:42]), M=float(l2[43:51]), n=float(l2[52:63]), rev=int(l2[63:68]))


def brouwer(n0_rad_min, e, inc):
    """Inicializacion de SGP4: de movimiento medio de Kozai (n0) a Brouwer (n0'', a0'')."""
    theta = math.cos(inc)
    a1 = (XKE / n0_rad_min) ** (2.0 / 3.0)
    d1 = 1.5 * K2 * (3 * theta ** 2 - 1) / (a1 ** 2 * (1 - e * e) ** 1.5)
    a0 = a1 * (1 - d1 / 3 - d1 ** 2 - 134.0 / 81.0 * d1 ** 3)
    d0 = 1.5 * K2 * (3 * theta ** 2 - 1) / (a0 ** 2 * (1 - e * e) ** 1.5)
    return n0_rad_min / (1 + d0), a0 / (1 - d0), a1


def tasas_j2(n, a, e, inc):
    """Tasas seculares de primer orden en J2 [rad/min] con la notacion de SGP4 (k2 = J2/2)."""
    theta, b = math.cos(inc), math.sqrt(1 - e * e)
    dM = n * (1 + 3 * K2 * (3 * theta ** 2 - 1) / (2 * a ** 2 * b ** 3))
    dw = -3 * K2 * n * (1 - 5 * theta ** 2) / (2 * a ** 2 * b ** 4)
    dO = -3 * K2 * n * theta / (a ** 2 * b ** 4)
    return dM, dw, dO


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("TLE SINTETICO (objeto 99999 inexistente); constantes WGS-72 de Spacetrack Report No. 3")
l1, l2 = construye_tle()
print(l1); print(l2)
assert suma_comprobacion(l1) == int(l1[68]) and suma_comprobacion(l2) == int(l2[68])
print(f"Suma de comprobacion: linea 1 = {l1[68]} ; linea 2 = {l2[68]} (verificadas)")

c = lee_linea2(l2)
print(f"\nCampos de la linea 2: i = {c['inc']} deg ; RAAN = {c['raan']} deg ; e = {c['ecc']} ; omega = {c['argp']} deg ; M = {c['M']} deg ; n = {c['n']} rev/dia ; revoluciones = {c['rev']}")
assert (c["inc"], c["raan"], c["ecc"], c["argp"], c["M"], c["n"]) == (51.6, 247.0, 0.0006, 130.0, 325.0, 15.5)

inc = math.radians(c["inc"])
n0 = c["n"] * 2 * math.pi / MIN_DIA          # rad/min (Kozai)
n2, a2, a1 = brouwer(n0, c["ecc"], inc)
print("\nConversion de movimiento medio (inicializacion de SGP4)")
print(f"  n0 (publicado, Kozai)   = {n0:.10f} rad/min = {c['n']:.8f} rev/dia")
print(f"  a1 = (ke/n0)^(2/3)      = {a1 * XKMPER:.4f} km")
print(f"  a0'' (Brouwer)          = {a2 * XKMPER:.4f} km ; diferencia a1 - a0'' = {(a1 - a2) * XKMPER:.4f} km")
print(f"  n0'' (Brouwer)          = {n2:.10f} rad/min = {n2 * MIN_DIA / (2 * math.pi):.8f} rev/dia")
dM, dw, dO = tasas_j2(n2, a2, c["ecc"], inc)
# Comprobacion: el n0 publicado corresponde a la tasa de anomalia media con J2 aplicada a n0''
err_n = abs(dM - n0) / n0
print(f"  Mdot(J2) con n0'' = {dM:.10f} rad/min ; n0 publicado = {n0:.10f} ; dif. relativa = {err_n:.2e} (del orden de J2^2)")
assert err_n < 1e-5

T = 2 * math.pi / n2
print(f"\nPeriodo nodal-kepleriano = {T:.3f} min -> {'espacio profundo (SDP4)' if T >= 225 else 'cercano a la Tierra (SGP4)'} (umbral 225 min)")
print(f"  semieje {a2 * XKMPER:.1f} km ; perigeo {(a2 * (1 - c['ecc']) - 1) * XKMPER:.1f} km de altitud sobre 6378.135 km")
print("\nClasificacion de otros periodos (SINTETICOS): n [rev/dia] -> periodo [min] -> modelo")
for nn in (15.5, 6.4, 6.3, 2.0057, 1.0027):
    t = MIN_DIA / nn
    print(f"  {nn:>8.4f} -> {t:>8.1f} -> {'SDP4' if t >= 225 else 'SGP4'}")

print("\nTasas seculares de primer orden en J2 (con las constantes de SGP4)")
print(f"  dOmega/dt = {math.degrees(dO) * MIN_DIA:.4f} deg/dia ; domega/dt = {math.degrees(dw) * MIN_DIA:.4f} deg/dia ; dM/dt = {math.degrees(dM) * MIN_DIA:.4f} deg/dia")
# Comparacion con las formulas de C03 (J2 y mu de otras fuentes)
mu = 3.986004e14; re_ = 6378137.0; j2 = 1082.63e-6
a_m = a2 * XKMPER * 1000.0
nn_ = math.sqrt(mu / a_m ** 3)
f = nn_ * j2 * (re_ / (a_m * (1 - c["ecc"] ** 2))) ** 2
dO_c03 = -1.5 * f * math.cos(inc) * 86400 * 180 / math.pi
print(f"  C03 con J2 NSSDC y mu IAU: dOmega/dt = {dO_c03:.4f} deg/dia ; diferencia con SGP4 = {abs(dO_c03 - math.degrees(dO) * MIN_DIA):.4f} deg/dia")
assert abs(dO_c03 - math.degrees(dO) * MIN_DIA) < 0.02
print("Este laboratorio NO propaga con SGP4: faltan arrastre (B*), terminos de J3/J4, correcciones de corto periodo y lunisolares de SDP4.")
print("Pruebas superadas.")
