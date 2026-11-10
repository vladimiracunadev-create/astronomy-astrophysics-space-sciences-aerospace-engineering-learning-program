# SPDX-License-Identifier: Apache-2.0
"""B85-C13: erosión por oxígeno atómico en órbita baja: flujo, fluencia y espesor perdido.

Consultado: G_E y R_E (NASA/NSSDC) para GM = g R^2. ILUSTRATIVO y NO CONSULTADO: densidad numérica de O por altitud,
reactividad de Kapton y de un recubrimiento de SiOx, ciclo solar, espesores.
Segunda vía: integral de la densidad variable en el ciclo solar por trapecios frente a la forma cerrada.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

GM = G_E * R_E ** 2                 # m3/s2 (derivado de g y R consultados)
N_O = {300: 5e15, 400: 1e15, 500: 2e14}   # m^-3 ILUSTRATIVO
RE_KAPTON = 3.0e-30                 # m3/atomo (3.0e-24 cm3/atomo) ILUSTRATIVO
RE_SIOX = 3.0e-34                   # m3/atomo ILUSTRATIVO
ESP_KAPTON = 25e-6                  # m
ESP_SIOX = 100e-9                   # m


def v_orbital(h_km):
    return math.sqrt(GM / (R_E + h_km * 1e3))


def flujo_ram(h_km, cos_inc=1.0):
    return N_O[h_km] * v_orbital(h_km) * cos_inc          # atomos/(m2 s)


def calcular():
    r = {"filas": []}
    for h in (300, 400, 500):
        v = v_orbital(h)
        phi = flujo_ram(h)
        flu = phi * YEAR
        perdida = RE_KAPTON * flu
        r["filas"].append((h, v, N_O[h], phi, flu, perdida))
    f4 = [f for f in r["filas"] if f[0] == 400][0]
    r["f400"] = f4
    r["meses_kapton"] = ESP_KAPTON / (RE_KAPTON * f4[3]) / (YEAR / 12)
    r["meses_siox"] = ESP_SIOX / (RE_SIOX * f4[3]) / (YEAR / 12)
    r["perdida_cos60"] = RE_KAPTON * flujo_ram(400, 0.5) * YEAR
    # ciclo solar sintetico: n(t) = n0 (1 + a sin(2 pi t/T)), T = 11 anios, a = 0.6
    a, T = 0.6, 11.0 * YEAR
    n_pasos = 20000
    tf = 5.5 * YEAR            # medio ciclo
    h = tf / n_pasos
    s = 0.0
    for i in range(n_pasos + 1):
        t = i * h
        f = N_O[400] * (1 + a * math.sin(2 * math.pi * t / T)) * v_orbital(400)
        s += f * (0.5 if i in (0, n_pasos) else 1.0) * h
    r["flu_trap"] = s
    r["flu_cerrada"] = N_O[400] * v_orbital(400) * (tf + a * T / (2 * math.pi) * (1 - math.cos(2 * math.pi * tf / T)))
    r["perdida_medio_ciclo"] = RE_KAPTON * r["flu_trap"]
    r["relacion_400_300"] = r["filas"][1][5] / r["filas"][0][5]
    return r


def main():
    r = calcular()
    cabecera()
    print(f"GM = g R^2 = {GM:.5e} m3/s2 (de g = {G_E} m/s2 y R = {R_E/1e3:.0f} km consultados)")
    print("Densidad de O por altitud: ILUSTRATIVA y no consultada; reactividades: ILUSTRATIVAS")
    print(f"{'h [km]':>7}{'v [m/s]':>10}{'n_O [m-3]':>12}{'flujo [m-2 s-1]':>18}{'fluencia/anio [m-2]':>21}{'Kapton/anio [um]':>18}")
    for h, v, n, phi, flu, per in r["filas"]:
        print(f"{h:>7}{v:>10.1f}{n:>12.1e}{phi:>18.3e}{flu:>21.3e}{per*1e6:>18.1f}")
    print(f"A 400 km, Kapton de 25 um dura {r['meses_kapton']:.2f} meses en cara ram; SiOx de 100 nm dura {r['meses_siox']:.2f} meses (reactividades ILUSTRATIVAS)")
    print(f"Con incidencia a 60 grados (cos = 0.5) la perdida anual en Kapton baja a {r['perdida_cos60']*1e6:.1f} um")
    print(f"Fluencia en medio ciclo solar sintetico: trapecios = {r['flu_trap']:.5e} ; cerrada = {r['flu_cerrada']:.5e} m-2")
    print(f"Perdida en medio ciclo = {r['perdida_medio_ciclo']*1e6:.1f} um ; cociente 400/300 km = {r['relacion_400_300']:.3f}")
    comprobar(abs(r["flu_trap"] - r["flu_cerrada"]) / r["flu_cerrada"] < 1e-8, "integral del ciclo solar")
    comprobar(abs(v_orbital(400) - 7668.6) < 5, "velocidad orbital a 400 km")
    fin()


if __name__ == "__main__":
    main()
