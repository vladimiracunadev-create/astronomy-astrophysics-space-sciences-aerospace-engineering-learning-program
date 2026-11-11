"""B114-C02 - Fuga de presion en un habitat SINTETICO.

Unidades: Pa, K, m3, kg, s. Datos SINTETICOS (semilla fija). Solo stdlib.
R = 8.314462618 J/(mol K) (CODATA 2022, NIST, consultada 2026-11-10).
"""
import math
import random
import sys

R = 8.314462618          # J/(mol K), exacta en el SI
M_AIRE = 0.028965        # kg/mol, aire seco (valor tipico, no consultado)
GAMMA = 1.4
T = 293.15               # K, ilustrativo
V = 100.0                # m3, ilustrativo
P0 = 101325.0            # Pa (1 atm = 101,3 kPa; NASA OCHMO-TB-003)
CD = 0.8                 # coeficiente de descarga, ilustrativo
RS = R / M_AIRE          # J/(kg K)
RNG = random.Random(114)


def flujo_masico_estrangulado(area, p):
    """mdot [kg/s] por un orificio con descarga a vacio (flujo estrangulado)."""
    f = math.sqrt(GAMMA / (RS * T)) * (2 / (GAMMA + 1)) ** ((GAMMA + 1) / (2 * (GAMMA - 1)))
    return CD * area * p * f


def tau_fuga(area):
    """Presion P = P0 exp(-t/tau) con T constante: tau = V / (CD A c)."""
    f = math.sqrt(GAMMA / (RS * T)) * (2 / (GAMMA + 1)) ** ((GAMMA + 1) / (2 * (GAMMA - 1)))
    return V / (CD * area * f * RS * T)


def ajuste_log(ts, ps):
    """Regresion lineal de ln P frente a t: pendiente = -1/tau."""
    n = len(ts)
    y = [math.log(p) for p in ps]
    mt, my = sum(ts) / n, sum(y) / n
    sxx = sum((t - mt) ** 2 for t in ts)
    sxy = sum((t - mt) * (yy - my) for t, yy in zip(ts, y))
    b = sxy / sxx
    sres = math.sqrt(sum((yy - (my + b * (t - mt))) ** 2 for t, yy in zip(ts, y)) / (n - 2))
    return b, sres / math.sqrt(sxx)


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Habitat SINTETICO: V = %.0f m3, T = %.2f K, P0 = %.0f Pa, Cd = %.1f"
          % (V, T, P0, CD))
    # 1. Fuga verdadera (oculta al analisis): orificio de 0.3 mm de diametro
    d_real = 0.3e-3
    a_real = math.pi * d_real ** 2 / 4
    tau = tau_fuga(a_real)
    print("Orificio real: d = %.1f mm; tau = %.4e s = %.1f dias"
          % (d_real * 1e3, tau, tau / 86400))
    # 2. Serie sintetica con ruido de sensor (sigma = 5 Pa), 1 muestra/h, 48 h
    sigma = 5.0
    ts = [3600.0 * k for k in range(49)]
    ps = [P0 * math.exp(-t / tau) + RNG.gauss(0, sigma) for t in ts]
    b, sb = ajuste_log(ts, ps)
    tau_est = -1 / b
    print("Caida observada en 48 h (sintetica): %.1f Pa (%.4f %%)"
          % (ps[0] - ps[-1], 100 * (ps[0] - ps[-1]) / ps[0]))
    print("tau estimado = %.4e s (verdadero %.4e); error relativo = %.2f %%"
          % (tau_est, tau, 100 * abs(tau_est - tau) / tau))
    # 3. Tasa de fuga y area equivalente
    dpdt = P0 / tau_est
    mdot = dpdt * V / (RS * T)
    a_est = V / (CD * tau_est * RS * T * math.sqrt(GAMMA / (RS * T)) *
                 (2 / (GAMMA + 1)) ** ((GAMMA + 1) / (2 * (GAMMA - 1))))
    d_est = 2 * math.sqrt(a_est / math.pi)
    print("Tasa de fuga inicial = %.3e Pa/s = %.2f Pa/h ; masa = %.3e kg/s = %.3f kg/dia"
          % (dpdt, dpdt * 3600, mdot, mdot * 86400))
    print("Diametro equivalente estimado = %.2f mm (verdadero %.2f mm)"
          % (d_est * 1e3, d_real * 1e3))
    # Segunda via: masa total frente a la caida de presion (ley del gas ideal)
    dm = (ps[0] - ps[-1]) * V / (RS * T)
    print("Masa perdida en 48 h = %.4f kg (ley del gas ideal)" % dm)
    # 4. Localizacion por amplitud ultrasonica A = k / r^2 con 5 sensores
    sensores = [(0.0, 0.0), (10.0, 0.0), (10.0, 6.0), (0.0, 6.0), (5.0, 3.0)]
    real = (7.2, 1.8)
    k = 50.0
    amp = []
    for (x, y) in sensores:
        r2 = (x - real[0]) ** 2 + (y - real[1]) ** 2 + 0.04
        amp.append(k / r2 * (1 + RNG.gauss(0, 0.03)))
    mejor = None
    gx = 0.0
    while gx <= 10.0 + 1e-9:
        gy = 0.0
        while gy <= 6.0 + 1e-9:
            # k se ajusta analiticamente: minimiza sum (A - k g)^2
            g = [1 / ((x - gx) ** 2 + (y - gy) ** 2 + 0.04) for (x, y) in sensores]
            kk = sum(a * gi for a, gi in zip(amp, g)) / sum(gi * gi for gi in g)
            c = sum((a - kk * gi) ** 2 for a, gi in zip(amp, g))
            if mejor is None or c < mejor[0]:
                mejor = (c, gx, gy, kk)
            gy += 0.05
        gx += 0.05
    err = math.hypot(mejor[1] - real[0], mejor[2] - real[1])
    print("Origen real (%.2f, %.2f) m ; estimado (%.2f, %.2f) m ; error = %.2f m"
          % (real[0], real[1], mejor[1], mejor[2], err))
    # 5. Tiempo hasta umbrales de presion (consultados: 34.5 kPa limite inferior
    #    de exposicion indefinida, NASA OCHMO-TB-003) con la fuga estimada
    for nombre, pu in (("90 kPa (alerta ilustrativa)", 90000.0),
                       ("34.5 kPa (limite inferior NASA-STD-3001)", 34500.0)):
        tu = tau_est * math.log(P0 / pu)
        print("t hasta %-42s = %.1f dias" % (nombre, tu / 86400))
    assert abs(tau_est - tau) / tau < 0.05
    dm_modelo = P0 * (1 - math.exp(-48 * 3600 / tau_est)) * V / (RS * T)
    print("Masa perdida segun el modelo exponencial = %.4f kg" % dm_modelo)
    assert abs(dm - dm_modelo) / dm < 0.05
    assert err < 0.3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
