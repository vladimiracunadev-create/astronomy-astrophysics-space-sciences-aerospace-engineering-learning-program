"""B59-C22 · Beneficio de un regolito: curva de partición, tamaño de corte, recuperación y ley.

Datos SINTÉTICOS / ILUSTRATIVOS (no consultados): distribución lognormal en masa (mediana 70 µm, GSD 2,6,
la misma de B59-C04), curva de partición con tamaño de corte d50 = 75 µm y agudeza k = 4,
y una ley de mineral objetivo g(d) enriquecida en los finos. No describen un regolito real.
Modelo: P_f(d) = 1/(1 + (d/d50)^k) es la probabilidad de que un grano de tamaño d vaya al producto fino.
Integrales en ln d sobre la densidad normal en masa; se contrastan con Monte Carlo (semilla fija) y con
el límite de corte nítido (k grande), cuyo resultado analítico es Phi((ln d50 - mu_m)/sigma).
Unidades: µm, fracciones másicas adimensionales.
Tolerancia: cuadratura frente a Monte Carlo < 0,5 pp; límite nítido frente a Phi < 1e-3.
"""
import math
import platform
import random
from statistics import NormalDist

MU_M = math.log(70.0)          # mediana en masa de ln d
SIG = math.log(2.6)
D50, K = 75.0, 4.0
SEMILLA = 20261109


def pf(d, d50=D50, k=K):
    z = k * math.log(d / d50)
    return 0.0 if z > 700 else 1.0 / (1.0 + math.exp(z))


def ley(d):
    return 0.02 + 0.18 / (1.0 + (d / 40.0) ** 2)    # ILUSTRATIVA, enriquecida en finos


def integra(f, n=40000):
    """Cuadratura del punto medio en u = (ln d - mu)/sigma con peso normal."""
    a, b = -8.0, 8.0
    h = (b - a) / n
    tot = 0.0
    for i in range(n):
        u = a + (i + 0.5) * h
        w = math.exp(-0.5 * u * u) / math.sqrt(2 * math.pi)
        tot += f(math.exp(MU_M + SIG * u)) * w * h
    return tot


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    nd = NormalDist()
    # 1) Corte nitido: k grande
    sharp = integra(lambda d: pf(d, D50, 400.0))
    an = nd.cdf((math.log(D50) - MU_M) / SIG)
    print(f"Fraccion en masa al producto fino con corte nitido: cuadratura = {sharp:.5f} ; analitica Phi = {an:.5f}")
    assert abs(sharp - an) < 1e-3

    # 2) Corte real (k = 4)
    y_f = integra(pf)                         # rendimiento masico del producto fino
    y_g = 1.0 - y_f
    g_alim = integra(ley)
    num = integra(lambda d: ley(d) * pf(d))
    g_fino = num / y_f
    g_grueso = (g_alim - num) / y_g
    rec = num / g_alim
    print(f"Tamano de corte d50 = {D50:.0f} µm ; agudeza k = {K:.0f}")
    print(f"Rendimiento masico: fino = {100*y_f:.2f} % ; grueso = {100*y_g:.2f} % (suma {100*(y_f+y_g):.2f} %)")
    print(f"Ley de alimentacion = {100*g_alim:.2f} % ; ley del fino = {100*g_fino:.2f} % ; ley del grueso = {100*g_grueso:.2f} %")
    print(f"Recuperacion del mineral objetivo en el fino = {100*rec:.2f} % ; razon de enriquecimiento = {g_fino/g_alim:.3f}")
    # balance de masa de mineral
    cierre = y_f * g_fino + y_g * g_grueso - g_alim
    print(f"Cierre del balance de mineral (alim - productos) = {cierre:.2e}")
    assert abs(cierre) < 1e-12

    # 3) Monte Carlo con el mismo modelo (muestras en masa)
    rng = random.Random(SEMILLA)
    n = 300000
    s_f = s_num = s_g = 0.0
    for _ in range(n):
        d = math.exp(rng.gauss(MU_M, SIG))
        p = pf(d)
        g = ley(d)
        s_f += p
        s_num += g * p
        s_g += g
    print(f"Monte Carlo ({n} granos): rendimiento fino = {100*s_f/n:.2f} % ; recuperacion = {100*s_num/s_g:.2f} %")
    assert abs(s_f / n - y_f) < 5e-3 and abs(s_num / s_g - rec) < 5e-3

    # 4) Imperfeccion: d25 y d75 de la curva de particion (probabilidad al grueso 0,25 y 0,75)
    d25 = D50 * (0.75 / 0.25) ** (1 / K)       # pf = 0,25 -> (d/d50)^k = 3
    d75 = D50 * (0.25 / 0.75) ** (1 / K)
    imp = (d25 - d75) / (2 * D50)
    print(f"d25 = {d25:.1f} µm ; d75 = {d75:.1f} µm ; imperfeccion I = (d25 - d75)/(2 d50) = {imp:.3f}")
    # 5) sensibilidad al tamano de corte
    for d50 in (50.0, 75.0, 100.0):
        yf = integra(lambda d: pf(d, d50, K))
        nu = integra(lambda d: ley(d) * pf(d, d50, K))
        print(f"d50 = {d50:5.0f} µm: fino = {100*yf:5.2f} % ; ley del fino = {100*nu/yf:5.2f} % ; recuperacion = {100*nu/g_alim:5.2f} %")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
