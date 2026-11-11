"""B118-C17 · Interferencia radioastronómica.

Sensibilidad de un radiotelescopio HIPOTÉTICO (antena de 25 m, eficiencia 0,6, Tsys = 25 K, B = 1 MHz, 1 h) y densidad de flujo de un
satélite SINTÉTICO con emisiones no deseadas ILUSTRATIVAS. Criterio de daño: nivel de interferencia > 10 % del ruido rms (idea del criterio de
pérdida de sensibilidad de la Rec. ITU-R RA.769, conocida solo por el resumen de una búsqueda del 2026-11-11; la Recomendación NO se abrió
y no se reproducen sus umbrales).
Unidades: W, m, Hz, K, Jy (1 Jy = 1e-26 W m^-2 Hz^-1). k = 1,380649e-23 J/K (CODATA, no consultado aquí).
Semilla Monte Carlo 118. Tolerancia: 3 % en la reducción por promediado.
"""
import math
import random
import sys

KB = 1.380649e-23
JY = 1e-26
C = 299_792_458.0


def delta_T(tsys, b_hz, t_s):
    return tsys / math.sqrt(b_hz * t_s)


def delta_S(tsys, a_eff, b_hz, t_s, npol=2):
    return 2.0 * KB * tsys / (a_eff * math.sqrt(npol * b_hz * t_s))


def pfd_espectral(eirp_dens_w_hz, d_m):
    return eirp_dens_w_hz / (4.0 * math.pi * d_m ** 2)


def mc_radiometro(n_efectivo, repeticiones=2000, semilla=118):
    rng = random.Random(semilla)
    medias = []
    for _ in range(repeticiones):
        medias.append(sum(rng.expovariate(1.0) for _ in range(n_efectivo)) / n_efectivo)
    m = sum(medias) / len(medias)
    sd = math.sqrt(sum((x - m) ** 2 for x in medias) / (len(medias) - 1))
    return sd / m


def compute():
    v = {}
    D, eta = 25.0, 0.6
    a_eff = eta * math.pi * (D / 2) ** 2
    tsys, b, t = 25.0, 1e6, 3600.0
    f = 1.42e9
    lam = C / f
    v["a_eff"], v["lam"] = a_eff, lam
    v["dT"] = delta_T(tsys, b, t)
    v["dS_jy"] = delta_S(tsys, a_eff, b, t) / JY
    v["dS_4h"] = delta_S(tsys, a_eff, b, 4 * t) / JY
    v["cociente_4h"] = v["dS_jy"] / v["dS_4h"]
    # satélite sintético: EIRP espectral de emisión no deseada -70 dBW/Hz a 1000 km
    eirp = 10 ** (-70 / 10)
    pfd = pfd_espectral(eirp, 1.0e6)
    v["pfd"] = pfd
    v["pfd_jy"] = pfd / JY
    # lóbulo lateral de 0 dBi: área efectiva lambda^2/(4 pi)
    a_sl = lam ** 2 / (4 * math.pi)
    p_int = pfd * a_sl  # W/Hz recibidos
    p_umbral = 0.1 * KB * v["dT"]
    v["p_int"], v["p_umbral"] = p_int, p_umbral
    v["exceso_db"] = 10 * math.log10(p_int / p_umbral)
    # distancia a la que el nivel cae al umbral (ley 1/d^2)
    v["d_umbral_km"] = 1000.0 * math.sqrt(p_int / p_umbral)
    # reducción de EIRP necesaria
    v["reduccion_db"] = v["exceso_db"]
    # verificación MC de la reducción por promediado: sd/m = 1/sqrt(N)
    v["mc_100"] = mc_radiometro(100)
    v["mc_10000"] = mc_radiometro(10000)
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Radiotelescopio HIPOTETICO (25 m, eta 0.6, Tsys 25 K, B 1 MHz, 1 h, 1.42 GHz) y satelite SINTETICO; RA.769 no abierta (solo resumen de busqueda).")
    v = compute()
    print(f"A_eff = {v['a_eff']:.1f} m^2; lambda = {v['lam'] * 100:.2f} cm; DT_rms = {v['dT'] * 1000:.3f} mK")
    print(f"Sensibilidad DS_rms (1 h) = {v['dS_jy'] * 1000:.3f} mJy; a 4 h = {v['dS_4h'] * 1000:.3f} mJy; cociente {v['cociente_4h']:.4f}")
    print(f"Satelite a 1000 km, EIRP espectral -70 dBW/Hz: pfd = {v['pfd']:.3e} W m^-2 Hz^-1 = {v['pfd_jy']:.3e} Jy")
    print(f"Por el lobulo lateral de 0 dBi: P = {v['p_int']:.3e} W/Hz; umbral 10 % del rms = {v['p_umbral']:.3e} W/Hz; exceso {v['exceso_db']:.1f} dB")
    print(f"Distancia a la que cae al umbral (ley 1/d^2): {v['d_umbral_km']:.0f} km; reduccion de EIRP necesaria a 1000 km: {v['reduccion_db']:.1f} dB")
    print(f"Radiometro Monte Carlo: sd/media con N = 100: {v['mc_100']:.4f} (1/sqrt(N) = 0.1000); N = 10000: {v['mc_10000']:.5f} (0.01000)")
    assert abs(v["cociente_4h"] - 2.0) < 1e-12
    assert abs(v["mc_100"] - 0.1) / 0.1 < 0.03 and abs(v["mc_10000"] - 0.01) / 0.01 < 0.03
    print("Pruebas superadas (promediado 1/sqrt(Bt) exacto y por Monte Carlo a 3 %).")


if __name__ == "__main__":
    main()
