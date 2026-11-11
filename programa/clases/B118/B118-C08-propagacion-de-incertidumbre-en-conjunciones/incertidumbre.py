"""B118-C08 · Propagación de incertidumbre en conjunciones.

Incertidumbre inicial SINTÉTICA de un objeto en órbita circular de 550 km: sigma a lo largo de la traza s0 y sigma del semieje a.
Crecimiento lineal: sigma_s(t) = sqrt(s0^2 + (1.5 n t sigma_a)^2). Comparación con Monte Carlo (semilla 118) que propaga la diferencia
exacta de movimiento medio y mide la curvatura (banana) en el sistema radial-transversal (RTN) del punto nominal.
Unidades: km, s, días. GM = 398600.4418 km^3/s^2 (convencional, no consultado). Tolerancia: 3 % en sigma_s; curvatura = a sigma_theta^2/2.
"""
import math
import random
import sys

MU = 398600.4418
RE = 6378.137


def compute(n_mc=40000, semilla=118):
    v = {}
    a = RE + 550.0
    n = math.sqrt(MU / a ** 3)
    s0, sa = 0.1, 0.02  # km
    rng = random.Random(semilla)
    muestras = [(rng.gauss(0, s0), rng.gauss(0, sa)) for _ in range(n_mc)]
    v["n"] = n
    v["T"] = 2 * math.pi / n
    filas = []
    for dias in (0.5, 1, 3, 7, 14):
        t = dias * 86400.0
        lineal = math.sqrt(s0 ** 2 + (1.5 * n * t * sa) ** 2)
        along, radial = [], []
        for ds0, da in muestras:
            na = math.sqrt(MU / (a + da) ** 3)
            dth = ds0 / a + (na - n) * t  # desfase angular respecto al nominal
            along.append(a * math.sin(dth))
            radial.append(a * math.cos(dth) - a)
        m = sum(along) / len(along)
        sd = math.sqrt(sum((x - m) ** 2 for x in along) / (len(along) - 1))
        sag = sum(radial) / len(radial)
        sig_th = lineal / a
        filas.append((dias, lineal, sd, sag, -a * sig_th ** 2 / 2))
    v["filas"] = filas
    # tiempo hasta que la curvatura media supera 1 km (en sigma lineal)
    sig_1km = math.sqrt(2 * 1.0 / a) * a  # sigma_s tal que a sigma_th^2/2 = 1 km
    t_crit = math.sqrt(max(0.0, sig_1km ** 2 - s0 ** 2)) / (1.5 * n * sa) / 86400.0
    v["sig_1km"], v["t_crit_dias"] = sig_1km, t_crit
    # el exceso: una covarianza lineal diagonal en RTN subestima la probabilidad de estar en el arco
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Incertidumbre SINTETICA: s0 = 0.1 km a lo largo, sigma_a = 0.02 km, orbita circular de 550 km; 40000 muestras, semilla 118.")
    v = compute()
    print(f"Movimiento medio n = {v['n']:.6e} rad/s; periodo {v['T']:.1f} s")
    print(" dias   sigma_s lineal [km]  sigma_s MC [km]  radial medio MC [km]  -a sig^2/2 [km]")
    for d, l, m, sag, teo in v["filas"]:
        print(f" {d:4.1f}   {l:15.3f}   {m:14.3f}   {sag:18.4f}   {teo:14.4f}")
        assert abs(l - m) / l < 0.03, "sigma lineal debe coincidir con MC a 3 %"
        if abs(teo) > 0.05:
            assert abs(sag - teo) / abs(teo) < 0.1
    print(f"Una sigma a lo largo de {v['sig_1km']:.0f} km hace que la curvatura media llegue a 1 km: ocurre a los {v['t_crit_dias']:.1f} dias")
    print("Pruebas superadas (crecimiento lineal vs Monte Carlo a 3 %; curvatura = a sigma^2/2 a 10 %).")


if __name__ == "__main__":
    main()
