"""B59-C04 · Granulometría lognormal de un regolito: percentiles, coeficientes y porosidad.

Datos SINTÉTICOS (no medidos, generados con semilla fija): 50 000 granos con diámetro lognormal,
mediana EN MASA de 70 µm (la mediana en número sale mucho menor) y desviación geométrica 2,6 (valores ILUSTRATIVOS, no consultados).
Densidad de grano 3000 kg/m^3 y densidad aparente 1500 kg/m^3: ILUSTRATIVAS (no consultadas).
Modelo: ln d ~ Normal(mu, sigma). Percentil p: d_p = exp(mu + z_p sigma) con z de la normal inversa.
La distribución en masa de granos esféricos pesa cada grano con d^3.
Unidades: µm, kg/m^3, adimensional.
Tolerancia: percentiles muestrales frente a analíticos < 2 %; D50 en masa frente a analítico < 25 % (cola gruesa ruidosa).
"""
import math
import platform
import random
from statistics import NormalDist

MEDIANA_MASA, GSD = 70.0, 2.6
RHO_GRANO, RHO_AP = 3000.0, 1500.0
SEMILLA = 20261109
N = 50000


def percentil(orden, p):
    return orden[min(len(orden) - 1, int(p * len(orden)))]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    sg = math.log(GSD)
    mu = math.log(MEDIANA_MASA) - 3 * sg * sg      # mediana en numero = mediana en masa / exp(3 sigma^2)
    print(f"Mediana en numero implicita = {math.exp(mu):.2f} µm ; mediana en masa impuesta = {MEDIANA_MASA:.0f} µm")
    rng = random.Random(SEMILLA)
    d = sorted(math.exp(rng.gauss(mu, sg)) for _ in range(N))
    nd = NormalDist()
    print("percentil  muestral[µm]  analitico[µm]  diferencia[%]")
    p_an = {}
    for p in (0.10, 0.50, 0.90):
        an = math.exp(mu + nd.inv_cdf(p) * sg)
        mu_m = percentil(d, p)
        p_an[p] = an
        print(f"D{int(p*100):02d}      {mu_m:11.2f}  {an:13.2f}  {100*(mu_m-an)/an:12.2f}")
        assert abs(mu_m - an) / an < 0.02
    cu = p_an[0.90] / p_an[0.10]
    print(f"Razon D90/D10 analitica = {cu:.2f} ; con D60/D10 (coeficiente de uniformidad Cu) = {math.exp((nd.inv_cdf(0.6)-nd.inv_cdf(0.1))*sg):.2f}")

    # Distribucion en masa: la mediana en masa de una lognormal es exp(mu + 3 sigma^2)
    w = [x ** 3 for x in d]
    tot = sum(w)
    acum = 0.0
    d50m = None
    for x, wi in zip(d, w):
        acum += wi
        if acum >= 0.5 * tot:
            d50m = x
            break
    d50m_an = math.exp(mu + 3 * sg * sg)
    print(f"D50 en masa: muestral = {d50m:.0f} µm ; analitico = {d50m_an:.0f} µm ")
    assert abs(d50m - d50m_an) / d50m_an < 0.25   # la cola gruesa hace ruidosa la mediana en masa
    # fraccion en masa de granos menores que 20 µm (fino respirable en este modelo): analitica
    z = (math.log(20.0) - (mu + 3 * sg * sg)) / sg
    f20 = nd.cdf(z)
    f20_m = sum(wi for x, wi in zip(d, w) if x < 20.0) / tot
    print(f"Fraccion en masa < 20 µm: analitica = {100*f20:.2f} % ; muestral = {100*f20_m:.2f} %")
    assert abs(f20 - f20_m) < 0.01
    # Porosidad desde densidades
    phi = 1.0 - RHO_AP / RHO_GRANO
    print(f"Porosidad = 1 - rho_ap/rho_grano = {phi:.3f}")
    # Superficie especifica de esferas: 6/(rho_grano d32); d32 = exp(mu + 2.5 sigma^2) para lognormal
    d32 = math.exp(mu + 2.5 * sg * sg)
    s_esp = 6.0 / (RHO_GRANO * d32 * 1e-6)
    print(f"Diametro de Sauter d32 = {d32:.1f} µm ; superficie especifica de esferas = {s_esp:.1f} m^2/kg")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
