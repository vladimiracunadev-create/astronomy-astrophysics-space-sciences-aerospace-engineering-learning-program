"""Curva de transferencia de fotones: ganancia y ruido de lectura a partir de pares de planos.

Datos: SINTÉTICOS. Ganancia verdadera 1,80 e-/ADU y ruido de lectura 6,0 e- (ilustrativos); 12 niveles de
señal entre 200 y 30000 ADU; 4000 píxeles por cuadro; pares de cuadros. No se consultó ninguna fuente externa.
Modelo: var(ADU) = ADU / g + (RN / g)^2; la varianza se estima como var(A - B) / 2 y la media como la de A y B.
El ruido de disparo se simula con una normal de media y varianza iguales (válido para más de ~100 e-).
Segunda vía: ajuste de mínimos cuadrados con fórmula cerrada y comparación con los parámetros verdaderos.
Supuestos: sin no linealidad, sin patrón fijo, sin cuantización, sin rayos cósmicos.
Tolerancia: ganancia a menos del 2 % y ruido de lectura a menos del 15 % del verdadero.
"""
import math
import random

G = 1.80
RN = 6.0
NIV = [200 * (150 ** (i / 11)) for i in range(12)]
NPIX = 4000


def par(rng, adu):
    e = adu * G
    a = [(rng.gauss(e, math.sqrt(e)) + rng.gauss(0, RN)) / G for _ in range(NPIX)]
    b = [(rng.gauss(e, math.sqrt(e)) + rng.gauss(0, RN)) / G for _ in range(NPIX)]
    return a, b


def ols(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    m = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    return m, my - m * mx


def calc():
    rng = random.Random(20261109)
    medias, varis = [], []
    for adu in NIV:
        a, b = par(rng, adu)
        d = [x - y for x, y in zip(a, b)]
        md = sum(d) / NPIX
        v = sum((t - md) ** 2 for t in d) / (NPIX - 1) / 2
        medias.append((sum(a) + sum(b)) / (2 * NPIX))
        varis.append(v)
    # ajuste ponderado con pesos 1/var^2 aproximados por la teoría
    w = [1 / (2 * (m / G + (RN / G) ** 2) ** 2 / (NPIX - 1)) for m in medias]
    sw = sum(w)
    mx = sum(wi * x for wi, x in zip(w, medias)) / sw
    my = sum(wi * y for wi, y in zip(w, varis)) / sw
    sxx = sum(wi * (x - mx) ** 2 for wi, x in zip(w, medias))
    pend = sum(wi * (x - mx) * (y - my) for wi, x, y in zip(w, medias, varis)) / sxx
    inter = my - pend * mx
    g_est = 1 / pend
    rn_est = G * math.sqrt(max(inter, 0.0)) if inter > 0 else 0.0
    # ajuste no ponderado como segunda vía
    p2, i2 = ols(medias, varis)
    return dict(medias=medias, varis=varis, g=g_est, rn=rn_est, g2=1 / p2, rn2=G * math.sqrt(max(i2, 0.0)), pend=pend, inter=inter)


def main():
    R = calc()
    for m, v in list(zip(R["medias"], R["varis"]))[::3]:
        print(f"media {m:9.1f} ADU | varianza {v:9.2f} ADU^2 | teoría {m / G + (RN / G) ** 2:9.2f}")
    print(f"Ajuste ponderado: g = {R['g']:.4f} e-/ADU, RN = {R['rn']:.3f} e-")
    print(f"Ajuste simple:    g = {R['g2']:.4f} e-/ADU, RN = {R['rn2']:.3f} e-")
    assert abs(R["g"] / G - 1) < 0.02
    assert abs(R["rn"] / RN - 1) < 0.15
    assert abs(R["g2"] / G - 1) < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
