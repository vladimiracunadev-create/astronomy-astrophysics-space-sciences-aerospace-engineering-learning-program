"""B118-C12 · Disposición al fin de vida.

(1) LEO: vida residual de una órbita circular por arrastre, con atmósfera exponencial ILUSTRATIVA rho(h) = rho0 exp(-(h - 400)/H),
rho0 = 3e-12 kg/m^3, H = 60 km (NO es un modelo de atmósfera real ni se consultó ninguno). B = Cd A/m = 2.2 x 0.01 m^2/kg.
(2) GEO: elevación mínima del perigeo 235 km + 1000 CR A/m y e <= 0,003 (IADC-02-01 Rev. 4, enero de 2025, consultada el 2026-11-11 vía
UNOOSA A/AC.105/C.1/2025/CRP.9). Región protegida GEO: +-200 km, +-15 grados de latitud; región LEO hasta 2000 km (misma fuente).
Unidades: km, s, años, m/s. GM = 398600.4418 km^3/s^2 (convencional, no consultado). Tolerancia: 10 % entre la vida numérica y la analítica.
"""
import math
import sys

MU = 398600.4418
RE = 6378.137
RHO0, H0, H = 3e-12, 400.0, 60.0
B = 2.2 * 0.01
ANIO = 365.25 * 86400.0


def rho(h_km):
    return RHO0 * math.exp(-(h_km - H0) / H)


def tasa_decaimiento_kms(h_km, b=B):
    a_m = (RE + h_km) * 1000.0
    dadt = -rho(h_km) * b * math.sqrt(MU * 1e9 * a_m)  # m/s
    return dadt / 1000.0  # km/s


def vida_numerica(h_ini, h_fin=200.0, b=B, n=200000):
    """Integra dt = dh / |dh/dt| con regla del punto medio."""
    dh = (h_ini - h_fin) / n
    t = 0.0
    for i in range(n):
        h = h_fin + (i + 0.5) * dh
        t += dh / abs(tasa_decaimiento_kms(h, b))
    return t / ANIO


def vida_analitica(h_ini, b=B):
    a_km = RE + h_ini
    v = math.sqrt(MU * 1e9 * a_km * 1000.0) / 1000.0  # km/s * ... factor mu a
    k = RHO0 * b * v  # km/s a h = 400
    return H / k * math.exp((h_ini - H0) / H) / ANIO  # sobre-aproxima (v constante, límite inferior ignorado)


def altura_para_vida(anios, b=B):
    lo, hi = 300.0, 1200.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if vida_numerica(mid, b=b, n=20000) > anios:
            hi = mid
        else:
            lo = mid
    return lo


def delta_v_hohmann(r1_km, r2_km):
    a = 0.5 * (r1_km + r2_km)
    v1, v2 = math.sqrt(MU / r1_km), math.sqrt(MU / r2_km)
    va = math.sqrt(MU * (2 / r1_km - 1 / a))
    vb = math.sqrt(MU * (2 / r2_km - 1 / a))
    return (va - v1) + (v2 - vb)


def compute():
    v = {}
    v["vidas"] = [(h, vida_numerica(h), vida_analitica(h)) for h in (450, 500, 550, 600, 650, 700)]
    v["h25"] = altura_para_vida(25.0)
    v["h5"] = altura_para_vida(5.0)
    v["h25_b2"] = altura_para_vida(25.0, b=2 * B)  # A/m doble
    CR = 1.3
    r_geo = RE + 35786.0
    v["geo"] = []
    for am in (0.005, 0.01, 0.02, 0.05):
        dh = 235.0 + 1000.0 * CR * am
        v["geo"].append((am, dh, delta_v_hohmann(r_geo, r_geo + dh) * 1000.0))
    v["a_geo"] = r_geo
    v["dif_apogeo_perigeo"] = 2 * r_geo * 0.003
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Atmosfera exponencial ILUSTRATIVA (rho0 = 3e-12 kg/m^3 a 400 km, H = 60 km); B = 0.022 m^2/kg. Elevacion GEO segun IADC Rev.4 (consultada).")
    v = compute()
    print(" h [km]   vida numerica [anios]   vida analitica [anios]")
    for h, n, a in v["vidas"]:
        print(f" {h:5.0f}   {n:20.3f}   {a:20.3f}")
        assert abs(n - a) / n < 0.10
    print(f"Altitud inicial con vida residual de 25 anios: {v['h25']:.1f} km; de 5 anios: {v['h5']:.1f} km; con B doble (25 anios): {v['h25_b2']:.1f} km")
    print("GEO: elevacion minima del perigeo 235 + 1000 CR A/m (CR = 1.3) y dv de dos impulsos:")
    for am, dh, dv in v["geo"]:
        print(f"  A/m = {am:5.3f} m^2/kg -> {dh:6.1f} km ; dv = {dv:5.2f} m/s")
    print(f"Con e <= 0.003, apogeo - perigeo <= {v['dif_apogeo_perigeo']:.0f} km (a = {v['a_geo']:.0f} km)")
    assert v["h25"] > v["h5"] and v["h25_b2"] > v["h25"]
    assert abs(v["geo"][1][1] - 248.0) < 1e-9
    print("Pruebas superadas (vida numerica = analitica a 10 %; mayor B permite disponer desde mas arriba; formula GEO 248 km).")


if __name__ == "__main__":
    main()
