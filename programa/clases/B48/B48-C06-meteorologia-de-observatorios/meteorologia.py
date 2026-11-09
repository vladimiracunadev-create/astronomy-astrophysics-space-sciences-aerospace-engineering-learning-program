"""Meteorología de un observatorio: punto de rocío, viento de Ornstein-Uhlenbeck y cierre con histéresis.

Datos: coeficientes de Magnus a = 17,62 y b = 243,12 °C (forma de libro; NO se verificaron contra la
fuente primaria). Viento SINTÉTICO: media 6 m/s, desviación estacionaria 2,5 m/s, tiempo de correlación
30 min; umbrales de cierre 12 m/s y reapertura 9 m/s INVENTADOS (no son los de ningún observatorio).
Modelo: e_s(T) ~ exp(a T / (b + T)); Td = b g / (a - g) con g = ln(RH/100) + a T / (b + T).
Viento: AR(1) exacto con paso de 1 min; P(v > 12) = 1 - Phi((12 - 6)/2,5).
Cierre: se cierra tras 3 min seguidos sobre 12 m/s y se abre tras 20 min seguidos bajo 9 m/s.
Supuestos: viento gaussiano estacionario (en la realidad es sesgado); sin ráfagas ni dirección.
Tolerancia: fracciones simuladas a menos de 0,002 de las analíticas; rocío a menos de 0,3 °C del valor de tablas.
"""
import math
import random
from statistics import NormalDist

A, B = 17.62, 243.12
MU, SD, TAU = 6.0, 2.5, 30.0
V_HI, V_LO = 12.0, 9.0
N = 1_000_000


def es(T):
    return math.exp(A * T / (B + T))


def rocio(T, rh):
    g = math.log(rh / 100.0) + A * T / (B + T)
    return B * g / (A - g)


def viento(n, seed=20261109):
    rng = random.Random(seed)
    phi = math.exp(-1.0 / TAU)
    s = SD * math.sqrt(1 - phi * phi)
    v = rng.gauss(MU, SD)
    out = []
    for _ in range(n):
        v = MU + phi * (v - MU) + rng.gauss(0, s)
        out.append(v)
    return out


def cierre(v, con_hist=True):
    abierto = True
    arriba = abajo = 0
    cambios = 0
    min_abierto = 0
    for x in v:
        if abierto:
            arriba = arriba + 1 if x > V_HI else 0
            if arriba >= 3:
                abierto, arriba, abajo = False, 0, 0
                cambios += 1
        else:
            lim = V_LO if con_hist else V_HI
            abajo = abajo + 1 if x < lim else 0
            if abajo >= (20 if con_hist else 1):
                abierto, arriba, abajo = True, 0, 0
                cambios += 1
        min_abierto += abierto
    return cambios, min_abierto / len(v)


def calc():
    v = viento(N)
    nd = NormalDist(MU, SD)
    p_teo = 1 - nd.cdf(V_HI)
    p_sim = sum(1 for x in v if x > V_HI) / N
    m = sum(v) / N
    var = sum((x - m) ** 2 for x in v) / N
    c1 = sum((v[i] - m) * (v[i + TAU.__int__()] - m) for i in range(0, 200000)) / 200000 / var
    ch_h, ab_h = cierre(v, True)
    ch_s, ab_s = cierre(v, False)
    return dict(td=rocio(20.0, 50.0), td_ida=es(rocio(20.0, 50.0)) / es(20.0) * 100, p_teo=p_teo, p_sim=p_sim, m=m, sd=math.sqrt(var),
                rho=c1, rho_teo=math.exp(-1), ch_h=ch_h, ab_h=ab_h, ch_s=ch_s, ab_s=ab_s)


def main():
    R = calc()
    print(f"Punto de rocío a 20 °C y 50 % HR = {R['td']:.2f} °C; humedad recuperada = {R['td_ida']:.3f} %")
    print(f"P(v > {V_HI:.0f} m/s): analítica {R['p_teo']:.5f} | simulada {R['p_sim']:.5f}")
    print(f"Media {R['m']:.3f} m/s, desviación {R['sd']:.3f} m/s; autocorrelación a 30 min {R['rho']:.3f} (teórica {R['rho_teo']:.3f})")
    print(f"Con histéresis: {R['ch_h']} cambios de estado, abierto {R['ab_h']:.4f} del tiempo")
    print(f"Sin histéresis: {R['ch_s']} cambios de estado, abierto {R['ab_s']:.4f} del tiempo")
    assert abs(R["td"] - 9.3) < 0.3 and abs(R["td_ida"] - 50.0) < 1e-9
    assert abs(R["p_teo"] - R["p_sim"]) < 0.002
    assert abs(R["rho"] - R["rho_teo"]) < 0.03
    assert R["ch_h"] < R["ch_s"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
