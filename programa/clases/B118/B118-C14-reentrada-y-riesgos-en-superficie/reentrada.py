"""B118-C14 · Reentrada y riesgos en superficie.

Número esperado de víctimas E_c = sum(A_c) x densidad media de población expuesta, con
A_c_i = (sqrt(A_h) + sqrt(A_i))^2 (área de víctima de un fragmento de área A_i; A_h = 0,36 m^2 por persona, forma habitual NO consultada
aquí). Fragmentos y densidades de población SINTÉTICOS e ILUSTRATIVOS (no son datos de ningún evento ni de ningún país).
Límite consultado: 10^-4 como máximo esperado de víctimas por reentrada (IADC-02-01 Rev. 4, enero de 2025, vía UNOOSA
A/AC.105/C.1/2025/CRP.9, consultada el 2026-11-11).
Unidades: m^2, km^2, personas/km^2. Latitud del punto de impacto por la traza de una órbita de inclinación 51,6 grados (circular).
Tolerancia: 2 % del promedio por muestreo uniforme del argumento de latitud.
"""
import math
import sys

A_H = 0.36
BANDAS = [(0, 10, 45.0), (10, 20, 70.0), (20, 30, 110.0), (30, 40, 80.0), (40, 50, 50.0), (50, 60, 20.0)]  # personas/km^2 SINTÉTICAS


def area_victima(a_i):
    return (math.sqrt(A_H) + math.sqrt(a_i)) ** 2


def densidad_en(lat_abs):
    for lo, hi, d in BANDAS:
        if lo <= lat_abs < hi:
            return d
    return BANDAS[-1][2]


def densidad_media(inc_deg, n=200000):
    s = math.sin(math.radians(inc_deg))
    tot = 0.0
    for k in range(n):
        u = 2 * math.pi * (k + 0.5) / n
        lat = math.degrees(math.asin(s * math.sin(u)))
        tot += densidad_en(abs(lat))
    return tot / n


def compute():
    v = {}
    frag = [0.30, 0.15, 0.10, 0.10, 0.06, 0.05, 0.04, 0.03, 0.02, 0.02, 0.01, 0.01]  # m^2 sintéticos
    v["n"] = len(frag)
    v["Ac_i"] = [area_victima(a) for a in frag]
    v["Ac_m2"] = sum(v["Ac_i"])
    v["rho"] = densidad_media(51.6)
    v["rho_n_doble"] = densidad_media(51.6, n=400000)
    v["Ec"] = v["Ac_m2"] * 1e-6 * v["rho"]
    v["Ec_oceano"] = v["Ec"] * 0.29  # si se confina el 71 % del riesgo al océano (ilustrativo: fracción terrestre 0,29)
    v["Ac_max"] = 1e-4 / (v["rho"] * 1e-6)
    # sin la tabla de bandas, usar una densidad uniforme de 45 /km^2 (control)
    v["Ec_uniforme"] = v["Ac_m2"] * 1e-6 * 45.0
    # un fragmento de 0,01 m^2 vs uno de 0,30 m^2: el término sqrt(A_h) domina en los pequeños
    v["ratio_pequeno"] = area_victima(0.01) / 0.01
    v["ratio_grande"] = area_victima(0.30) / 0.30
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Fragmentos y densidades de poblacion SINTETICOS; A_h = 0.36 m^2 ILUSTRATIVO; limite 1e-4 consultado (IADC Rev.4).")
    v = compute()
    print(f"{v['n']} fragmentos sobrevivientes sinteticos; area de victima total A_c = {v['Ac_m2']:.3f} m^2")
    print(f"Densidad media expuesta (inclinacion 51.6 deg): {v['rho']:.2f} personas/km^2 (con el doble de puntos: {v['rho_n_doble']:.2f})")
    print(f"E_c = {v['Ec']:.3e}; limite 1e-4 -> {'SUPERA' if v['Ec'] > 1e-4 else 'cumple'}")
    print(f"Si el riesgo se confinara al oceano (fraccion terrestre 0.29, ILUSTRATIVA): E_c = {v['Ec_oceano']:.3e}")
    print(f"Area de victima maxima que cumple 1e-4: {v['Ac_max']:.2f} m^2")
    print(f"Control con densidad uniforme de 45 /km^2: E_c = {v['Ec_uniforme']:.3e}")
    print(f"A_c/A: fragmento de 0.01 m^2 -> {v['ratio_pequeno']:.1f}; de 0.30 m^2 -> {v['ratio_grande']:.2f}")
    assert abs(v["rho"] - v["rho_n_doble"]) / v["rho"] < 0.02
    assert v["ratio_pequeno"] > v["ratio_grande"] > 1.0
    print("Pruebas superadas (promedio de densidad estable a 2 %; area de victima mayor que el area geometrica).")


if __name__ == "__main__":
    main()
