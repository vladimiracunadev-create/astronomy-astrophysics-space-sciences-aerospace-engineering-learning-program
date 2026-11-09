"""Autonomía de un respaldo de energía y probabilidad de cortes más largos que ella.

Datos: banco de baterías 12 V, 100 Ah, profundidad de descarga permitida 0,5 y rendimiento 0,9; carga
crítica 150 W; cortes de duración media 2,0 h y 6 cortes por año; TODO ILUSTRATIVO. No se consultó
ninguna fuente externa ni se dan normas de seguridad eléctrica.
Modelo: autonomía = V Ah DoD eta / P; duraciones exponenciales: P(D > t) = exp(-t/mu);
cortes que superan la autonomía por año ~ Poisson(lambda p).
Segunda vía: simulación con semilla 20261109.
Supuestos: carga constante, batería nueva y llena, sin generador; cortes independientes.
Tolerancia: 4 sigmas de muestreo.
"""
import math
import random

V, AH, DOD, ETA, P = 12.0, 100.0, 0.5, 0.9, 150.0
MU, LAM = 2.0, 6.0
SEMILLA = 20261109


def autonomia(v=V, ah=AH, dod=DOD, eta=ETA, p=P):
    return v * ah * dod * eta / p


def poisson(rng, lam):
    L = math.exp(-lam)
    k, x = 0, 1.0
    while True:
        x *= rng.random()
        if x <= L:
            return k
        k += 1


def calc():
    t = autonomia()
    p = math.exp(-t / MU)
    esp = LAM * p
    p_algun = 1 - math.exp(-LAM * p)
    rng = random.Random(SEMILLA)
    n = 200000
    exc = sum(1 for _ in range(n) if rng.expovariate(1 / MU) > t)
    p_sim = exc / n
    sig = math.sqrt(p * (1 - p) / n)
    anios = 50000
    alguno = 0
    total = 0
    for _ in range(anios):
        k = poisson(rng, LAM)
        c = sum(1 for _ in range(k) if rng.expovariate(1 / MU) > t)
        total += c
        alguno += c > 0
    # batería para cubrir el 95 % de los cortes: t95 = -mu ln 0,05
    t95 = -MU * math.log(0.05)
    ah95 = t95 * P / (V * DOD * ETA)
    return dict(t=t, p=p, p_sim=p_sim, sig=sig, esp=esp, esp_sim=total / anios, p_algun=p_algun, alguno=alguno / anios, t95=t95, ah95=ah95)


def main():
    R = calc()
    print(f"Energía útil = {V * AH * DOD * ETA:.1f} Wh; autonomía = {R['t']:.2f} h")
    print(f"P(corte > autonomía): analítica {R['p']:.4f} | simulada {R['p_sim']:.4f} (sigma {R['sig']:.4f})")
    print(f"Cortes largos por año: esperados {R['esp']:.3f} | simulados {R['esp_sim']:.3f}")
    print(f"P(al menos uno en el año): analítica {R['p_algun']:.4f} | simulada {R['alguno']:.4f}")
    print(f"Para cubrir el 95 % de los cortes: {R['t95']:.2f} h, o sea {R['ah95']:.0f} Ah")
    assert abs(R["p"] - R["p_sim"]) < 4 * R["sig"]
    assert abs(R["esp"] - R["esp_sim"]) < 0.02
    assert abs(R["p_algun"] - R["alguno"]) < 0.006
    assert abs(math.exp(-R["t95"] / MU) - 0.05) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
