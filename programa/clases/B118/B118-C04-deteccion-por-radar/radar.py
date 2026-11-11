"""B118-C04 · Detección por radar.

Ecuación del radar monoestática: Pr = Pt G^2 lambda^2 sigma / ((4 pi)^3 R^4); SNR = Pr / (k T B).
Datos: radar HIPOTÉTICO e ILUSTRATIVO (ningún sistema real). Constante de Boltzmann CODATA (no consultada aquí).
Sección eficaz de una esfera: aproximación de dos regímenes (Rayleigh sigma = 9 pi r^2 (k r)^4 si k r < 0,5; óptica sigma = pi r^2
si k r >= 2; interpolación log-log entre ambos) -> ILUSTRATIVA.
Unidades: W, m, Hz, K, km. Tolerancia: 1e-9 relativa en las identidades de escala.
"""
import math
import sys

KB = 1.380649e-23


def sigma_esfera(d_m, lam_m):
    r = d_m / 2.0
    k = 2.0 * math.pi / lam_m
    x = k * r
    ray = lambda x_: 9.0 * math.pi * r * r * x_ ** 4
    opt = math.pi * r * r
    if x < 0.5:
        return 9.0 * math.pi * r * r * x ** 4
    if x >= 2.0:
        return opt
    # interpolación log-log entre x=0.5 (Rayleigh) y x=2 (óptica)
    s0, s1 = ray(0.5) * (r / r), opt
    t = (math.log(x) - math.log(0.5)) / (math.log(2.0) - math.log(0.5))
    return math.exp(math.log(s0) + t * (math.log(s1) - math.log(s0)))


def snr(pt_w, g_dbi, f_hz, sigma_m2, rango_m, t_sist=100.0, b_hz=1e3, t_int=1.0):
    lam = 299_792_458.0 / f_hz
    g = 10.0 ** (g_dbi / 10.0)
    pr = pt_w * g * g * lam * lam * sigma_m2 / ((4.0 * math.pi) ** 3 * rango_m ** 4)
    # integración coherente de t_int s sobre ancho de banda b_hz: ganancia b*t
    return pr / (KB * t_sist * b_hz) * (b_hz * t_int)


def rango_max(pt_w, g_dbi, f_hz, sigma_m2, snr_min=13.0, **kw):
    lo, hi = 1.0, 1e9
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if snr(pt_w, g_dbi, f_hz, sigma_m2, mid, **kw) >= snr_min:
            lo = mid
        else:
            hi = mid
    return lo


def compute():
    v = {}
    f = 1.3e9
    lam = 299_792_458.0 / f
    v["lam"] = lam
    v["sig_10cm"] = sigma_esfera(0.10, lam)
    v["sig_1cm"] = sigma_esfera(0.01, lam)
    v["sig_1m"] = sigma_esfera(1.0, lam)
    v["x_10cm"] = 2.0 * math.pi / lam * 0.05
    kw = dict(pt_w=1.0e5, g_dbi=40.0, f_hz=f)
    v["r10"] = rango_max(sigma_m2=v["sig_10cm"], **kw) / 1000.0
    v["r1"] = rango_max(sigma_m2=v["sig_1cm"], **kw) / 1000.0
    v["r1m"] = rango_max(sigma_m2=v["sig_1m"], **kw) / 1000.0
    v["cociente_r"] = v["r10"] / v["r1"]
    v["esperado_r"] = (v["sig_10cm"] / v["sig_1cm"]) ** 0.25
    v["snr_1000"] = snr(1.0e5, 40.0, f, v["sig_10cm"], 1.0e6)
    v["snr_2000"] = snr(1.0e5, 40.0, f, v["sig_10cm"], 2.0e6)
    v["cociente_snr"] = v["snr_1000"] / v["snr_2000"]
    # diámetro mínimo a 1000 km con SNR >= 13
    lo, hi = 1e-4, 10.0
    for _ in range(100):
        mid = math.sqrt(lo * hi)
        if snr(1.0e5, 40.0, f, sigma_esfera(mid, lam), 1.0e6) >= 13.0:
            hi = mid
        else:
            lo = mid
    v["dmin_1000"] = hi
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Radar HIPOTETICO: Pt = 100 kW, G = 40 dBi, f = 1.3 GHz, T = 100 K, B = 1 kHz, integracion 1 s; todo ILUSTRATIVO.")
    v = compute()
    print(f"Longitud de onda: {v['lam'] * 100:.2f} cm; k r de una esfera de 10 cm: {v['x_10cm']:.2f}")
    print(f"Seccion eficaz (modelo de dos regimenes): 1 cm {v['sig_1cm']:.3e} m^2; 10 cm {v['sig_10cm']:.3e} m^2; 1 m {v['sig_1m']:.3e} m^2")
    print(f"Rango maximo para SNR >= 13: 1 cm {v['r1']:.0f} km; 10 cm {v['r10']:.0f} km; 1 m {v['r1m']:.0f} km")
    print(f"Cociente de rangos 10 cm / 1 cm = {v['cociente_r']:.4f}; esperado (sigma ratio)^(1/4) = {v['esperado_r']:.4f}")
    print(f"SNR del objeto de 10 cm a 1000 km: {10 * math.log10(v['snr_1000']):.1f} dB; a 2000 km: {10 * math.log10(v['snr_2000']):.1f} dB; cociente {v['cociente_snr']:.3f}")
    print(f"Diametro minimo a 1000 km con SNR >= 13: {v['dmin_1000'] * 100:.2f} cm")
    assert abs(v["cociente_snr"] - 16.0) < 1e-9 * 16, "SNR debe caer como R^-4"
    assert abs(v["cociente_r"] - v["esperado_r"]) / v["esperado_r"] < 1e-6
    print("Pruebas superadas (R^-4 exacto; rango ~ sigma^(1/4)).")


if __name__ == "__main__":
    main()
