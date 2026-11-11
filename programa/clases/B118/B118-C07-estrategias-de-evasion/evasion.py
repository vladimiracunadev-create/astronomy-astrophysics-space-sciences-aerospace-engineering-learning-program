"""B118-C07 · Estrategias de evasión.

Maniobra tangencial (a lo largo de la traza) de un satélite SINTÉTICO en órbita circular de 550 km; separación a lo largo de la
traza tras k órbitas: fórmula de deriva (s = 3 dv T k) frente a propagación kepleriana exacta en el plano.
Unidades: km, s, m/s. Sistema: plano orbital inercial, burn en t = 0 en x = a. GM = 398600.4418 km^3/s^2 (convencional, no consultado).
Masa 500 kg e Isp 220 s ILUSTRATIVOS. Tolerancia: 2 % entre fórmula lineal y propagación exacta.
"""
import math
import sys

MU = 398600.4418
RE = 6378.137
G0 = 9.80665


def kepler_E(M, e):
    E = M if e < 0.8 else math.pi
    for _ in range(60):
        E -= (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
    return E


def posicion_tras_burn(a0, dv_kms, t):
    """Burn tangencial en el punto (a0, 0): ese punto es perigeo (dv>0) o apogeo (dv<0)."""
    v0 = math.sqrt(MU / a0) + dv_kms
    a = 1.0 / (2.0 / a0 - v0 * v0 / MU)
    h = a0 * v0
    e = math.sqrt(max(0.0, 1.0 - h * h / (MU * a)))
    n = math.sqrt(MU / a ** 3)
    # dv>0: perigeo en el burn (nu0=0); dv<0: apogeo (nu0=pi)
    if dv_kms >= 0:
        M = n * t
        E = kepler_E(M % (2 * math.pi), e)
        x, y = a * (math.cos(E) - e), a * math.sqrt(1 - e * e) * math.sin(E)
    else:
        M = n * t + math.pi
        E = kepler_E(M % (2 * math.pi), e)
        x, y = a * (math.cos(E) - e), a * math.sqrt(1 - e * e) * math.sin(E)
        x, y = -x, -y
    return x, y


def separacion_traza(a0, dv_kms, k):
    """Longitud de arco entre la posición nominal y la maniobrada tras k órbitas nominales."""
    n0 = math.sqrt(MU / a0 ** 3)
    T0 = 2 * math.pi / n0
    t = k * T0
    xn, yn = a0 * math.cos(n0 * t), a0 * math.sin(n0 * t)
    xm, ym = posicion_tras_burn(a0, dv_kms, t)
    ang = math.atan2(xn * ym - yn * xm, xn * xm + yn * ym)
    return a0 * ang, T0


def pc_aprox(miss_m, sx, sy, R):
    return R * R / (2 * sx * sy) * math.exp(-0.5 * (miss_m / sx) ** 2)


def compute():
    v = {}
    a0 = RE + 550.0
    v["a0"] = a0
    dv = 0.0002  # km/s = 0.2 m/s
    s_exacta, T = separacion_traza(a0, dv, 2)
    v["T"] = T
    v["dv_ms"] = dv * 1000
    v["s_exacta"] = abs(s_exacta)
    v["s_lineal"] = 3 * dv * T * 2
    v["rel"] = v["s_exacta"] / v["s_lineal"]
    # dv necesario para 5 km tras 2 órbitas
    v["dv_5km"] = 5.0 / (3 * T * 2) * 1000.0  # m/s
    s5, _ = separacion_traza(a0, v["dv_5km"] / 1000.0, 2)
    v["s5"] = abs(s5)
    # dv de signo contrario da la separación opuesta
    sm, _ = separacion_traza(a0, -dv, 2)
    v["simetria"] = sm / s_exacta
    # combustible
    m0, isp = 500.0, 220.0
    v["dm_g"] = m0 * (1 - math.exp(-(v["dv_5km"]) / (isp * G0))) * 1000
    # beneficio en Pc con un miss inicial pequeño (sintético): sin maniobra 100 m; con maniobra 100 m + 5 km a lo largo (x)
    v["pc_sin"] = pc_aprox(100.0, 300.0, 100.0, 10.0)
    v["pc_con"] = pc_aprox(5000.0, 300.0, 100.0, 10.0)
    # coste en retraso: maniobra más tarde = menos órbitas = más dv
    v["dv_por_k"] = [(k, 5.0 / (3 * T * k) * 1000.0) for k in (0.5, 1, 2, 4)]
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Satelite SINTETICO en orbita circular de 550 km; masa 500 kg e Isp 220 s ILUSTRATIVOS; dos cuerpos sin arrastre.")
    v = compute()
    print(f"Periodo {v['T']:.1f} s; maniobra tangencial de {v['dv_ms']:.2f} m/s")
    print(f"Separacion a lo largo de la traza tras 2 orbitas: exacta {v['s_exacta']:.3f} km; lineal 3 dv T k = {v['s_lineal']:.3f} km; relacion {v['rel']:.4f}")
    print(f"dv necesario para 5 km tras 2 orbitas: {v['dv_5km']:.4f} m/s (comprobado: {v['s5']:.3f} km)")
    print(f"Simetria del signo: {v['simetria']:.4f} (esperado -1)")
    print(f"Combustible (Tsiolkovsky) para ese dv: {v['dm_g']:.2f} g")
    print("dv necesario segun las orbitas disponibles antes del TCA:")
    for k, d in v["dv_por_k"]:
        print(f"  {k:3.1f} orbitas -> {d:.3f} m/s")
    print(f"Pc antes (miss 100 m) = {v['pc_sin']:.3e}; despues (5 km a lo largo) = {v['pc_con']:.3e}")
    assert abs(v["rel"] - 1) < 0.02
    assert abs(v["s5"] - 5.0) < 0.1
    assert abs(v["simetria"] + 1) < 0.02
    print("Pruebas superadas (formula lineal vs Kepler a 2 %; simetria de signo; objetivo de 5 km).")


if __name__ == "__main__":
    main()
