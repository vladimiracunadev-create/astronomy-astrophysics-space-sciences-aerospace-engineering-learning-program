"""B118-C03 · Detección y seguimiento óptico.

Modelo: esfera difusa (albedo p), fase de Lambert, telescopio de apertura D con ruido de Poisson + fondo.
Datos: 100 % ILUSTRATIVOS (ningún instrumento real). Constantes convencionales NO consultadas: magnitud solar V = -26.74,
flujo de fotones de V=0 ~ 1.0e6 fotones/(s cm^2) en la banda V.
Unidades: m, km, grados, segundos, magnitudes. Sistema: ángulo de fase entre Sol y observador vistos desde el objeto.
Tolerancia: SNR por fórmula frente a Monte Carlo (semilla 118): 5 %.
"""
import math
import random
import sys

M_SOL = -26.74       # magnitud aparente del Sol (convención, no consultada)
F0 = 1.0e6           # fotones / (s cm^2) para V = 0 (ilustrativo)


def fase_lambert(alfa):
    return (2.0 / (3.0 * math.pi)) * ((math.pi - alfa) * math.cos(alfa) + math.sin(alfa))


def magnitud(diametro_m, rango_km, fase_deg, albedo=0.1):
    r = diametro_m / 2.0
    cociente = albedo * r * r * fase_lambert(math.radians(fase_deg)) / ((rango_km * 1000.0) ** 2)
    return M_SOL - 2.5 * math.log10(cociente)


def snr(mag, apertura_m, t_s, eficiencia=0.3, fondo_e=400.0, ruido_lectura=5.0, npix=9):
    area_cm2 = math.pi * (apertura_m * 100.0 / 2.0) ** 2
    senal = F0 * 10.0 ** (-0.4 * mag) * area_cm2 * eficiencia * t_s
    var = senal + npix * (fondo_e + ruido_lectura ** 2)
    return senal / math.sqrt(var), senal


def diametro_minimo(rango_km, fase_deg, apertura_m, t_s, albedo=0.1, umbral=5.0):
    lo, hi = 0.001, 100.0
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if snr(magnitud(mid, rango_km, fase_deg, albedo), apertura_m, t_s)[0] >= umbral:
            hi = mid
        else:
            lo = mid
    return hi


def longitud_traza_arcsec(v_perp_kms, rango_km, t_s):
    return math.degrees(v_perp_kms / rango_km * t_s) * 3600.0


def compute():
    v = {}
    v["m10_1000"] = magnitud(0.10, 1000.0, 60.0)
    v["m10_36000"] = magnitud(0.10, 36000.0, 60.0)
    v["dm"] = v["m10_36000"] - v["m10_1000"]
    v["dm_esp"] = 5.0 * math.log10(36.0)
    v["snr_ej"], v["senal_ej"] = snr(v["m10_1000"], 0.5, 2.0)
    v["dmin_leo"] = diametro_minimo(1000.0, 60.0, 0.5, 2.0)
    v["dmin_geo"] = diametro_minimo(36000.0, 60.0, 0.5, 2.0)
    v["dmin_geo_1m"] = diametro_minimo(36000.0, 60.0, 1.0, 2.0)
    v["traza_leo"] = longitud_traza_arcsec(7.3, 1000.0, 2.0)
    v["traza_geo"] = longitud_traza_arcsec(0.0, 36000.0, 2.0)
    # Monte Carlo del SNR (Poisson aprox. normal) con semilla 118
    rng = random.Random(118)
    area_cm2 = math.pi * (50.0 / 2.0) ** 2
    s_med = v["senal_ej"]
    b_med = 9 * (400.0 + 25.0)
    muestras = []
    for _ in range(20000):
        s = rng.gauss(s_med, math.sqrt(s_med))
        b = rng.gauss(b_med, math.sqrt(b_med))
        muestras.append((s, b))
    # estimador: señal medida (neta de fondo conocido) / sigma teórica
    est = sum(m[0] for m in muestras) / len(muestras)
    var = sum((m[0] - est) ** 2 for m in muestras) / (len(muestras) - 1)
    v["snr_mc"] = est / math.sqrt(var + b_med)
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Todos los parametros del telescopio y del albedo son ILUSTRATIVOS; magnitud solar y flujo V=0 son convenciones no consultadas.")
    v = compute()
    print(f"Magnitud de una esfera de 10 cm, albedo 0.1, fase 60 deg: {v['m10_1000']:.2f} a 1000 km; {v['m10_36000']:.2f} a 36000 km")
    print(f"Diferencia {v['dm']:.2f} mag (esperada 5 log10(36) = {v['dm_esp']:.2f})")
    print(f"SNR (apertura 0.5 m, 2 s) del objeto de 10 cm a 1000 km: {v['snr_ej']:.1f}")
    print(f"Diametro minimo con SNR >= 5 (0.5 m, 2 s): LEO 1000 km {v['dmin_leo'] * 100:.1f} cm; GEO 36000 km {v['dmin_geo'] * 100:.1f} cm")
    print(f"Con apertura 1.0 m en GEO: {v['dmin_geo_1m'] * 100:.1f} cm")
    print(f"Traza de un objeto LEO (v_perp 7.3 km/s, 1000 km, 2 s): {v['traza_leo']:.0f} arcsec; GEO sin movimiento propio: {v['traza_geo']:.0f} arcsec")
    print(f"SNR Monte Carlo (20000 ensayos): {v['snr_mc']:.1f}")
    assert abs(v["dm"] - v["dm_esp"]) < 1e-9
    assert abs(v["snr_mc"] - v["snr_ej"]) / v["snr_ej"] < 0.05
    assert v["dmin_geo"] > v["dmin_leo"] > 0
    print("Pruebas superadas (ley de rango 5 log10, SNR formula vs Monte Carlo a 5 %).")


if __name__ == "__main__":
    main()
