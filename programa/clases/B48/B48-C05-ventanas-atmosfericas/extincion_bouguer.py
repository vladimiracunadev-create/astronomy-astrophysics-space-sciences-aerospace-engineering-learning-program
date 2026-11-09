"""Recta de Bouguer: extinción atmosférica a partir de medidas a distintas masas de aire.

Datos: SINTÉTICOS. Coeficiente verdadero k = 0,20 mag por masa de aire y magnitud fuera de la atmósfera
m0 = 12,000 (ilustrativos); 12 masas de aire entre 1,0 y 2,5; ruido gaussiano de 0,01 mag.
Bandas de absorción (centros y anchos) INVENTADAS para la parte de ventanas; no son las de la atmósfera real.
No se consultó ninguna fuente externa.
Modelo: m(X) = m0 + k X (Bouguer); mínimos cuadrados cerrados; sigma_k = sigma / sqrt(Sxx).
Ventana: transmisión T(L) = exp(-suma tau_i / (1 + ((L - c_i)/w_i)^2)); se cuenta la fracción de banda con T > 0,8.
Supuestos: extinción constante durante la serie, sin término de color.
Tolerancia: desviación de k simulada a menos del 5 % de la analítica (4000 repeticiones, semilla 20261109).
"""
import math
import random
import statistics

K = 0.20
M0 = 12.0
SIG = 0.01
XS = [1.0 + 1.5 * i / 11 for i in range(12)]
BANDAS = [(0.76, 0.012, 3.0), (0.94, 0.025, 2.0), (1.13, 0.03, 1.5), (1.38, 0.06, 4.0)]


def ols(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    k = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    return k, my - k * mx, sxx


def trans(lam):
    t = 0.0
    for c, w, tau in BANDAS:
        t += tau / (1 + ((lam - c) / w) ** 2)
    return math.exp(-t)


def fraccion(n, lo=0.70, hi=1.50):
    ok = 0
    for i in range(n):
        lam = lo + (hi - lo) * (i + 0.5) / n
        if trans(lam) > 0.8:
            ok += 1
    return ok / n


def calc():
    rng = random.Random(20261109)
    ks, ms = [], []
    for _ in range(4000):
        ys = [M0 + K * x + rng.gauss(0, SIG) for x in XS]
        k, m0, sxx = ols(XS, ys)
        ks.append(k)
        ms.append(m0)
    _, _, sxx = ols(XS, [0.0] * len(XS)) if False else (0, 0, sum((x - sum(XS) / len(XS)) ** 2 for x in XS))
    sk = SIG / math.sqrt(sxx)
    xbar = sum(XS) / len(XS)
    s0 = SIG * math.sqrt(1 / len(XS) + xbar ** 2 / sxx)
    return dict(k_med=statistics.fmean(ks), k_sd=statistics.stdev(ks), sk=sk, m_med=statistics.fmean(ms), m_sd=statistics.stdev(ms), s0=s0,
                sxx=sxx, f1=fraccion(1000), f2=fraccion(20000))


def main():
    R = calc()
    print(f"Sxx = {R['sxx']:.4f}")
    print(f"k medio simulado = {R['k_med']:.5f} (verdadero {K}); desviación simulada {R['k_sd']:.5f}; analítica {R['sk']:.5f}")
    print(f"m0 medio simulado = {R['m_med']:.5f} (verdadero {M0}); desviación simulada {R['m_sd']:.5f}; analítica {R['s0']:.5f}")
    print(f"Fracción de banda útil (T > 0,8): {R['f1']:.4f} con 1000 puntos y {R['f2']:.4f} con 20000")
    assert abs(R["k_med"] - K) < 4 * R["sk"] / math.sqrt(4000)
    assert abs(R["k_sd"] / R["sk"] - 1) < 0.05
    assert abs(R["m_sd"] / R["s0"] - 1) < 0.05
    assert abs(R["f1"] - R["f2"]) < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
