"""B132-C04: estadistica de orientaciones axiales (datos SINTETICOS, semilla fija).

Prueba de Rayleigh sobre angulos duplicados (datos axiales), prueba binomial exacta y comparaciones multiples.
Hipotesis nula de Rayleigh: distribucion uniforme en el circulo (astropy.stats.rayleightest, consultada).
La aproximacion de p de Zar (1999) y la formula de la binomial se verifican por Monte Carlo (no consultadas).
Solo biblioteca estandar. Unidades: grados; p y R adimensionales.
"""
import math
import random
import sys

SEMILLA = 20261113


def rayleigh_axial(angulos):
    """Datos axiales (theta ~ theta+180): se duplican los angulos. Devuelve R, z y p."""
    n = len(angulos)
    c = sum(math.cos(math.radians(2 * a)) for a in angulos) / n
    s = sum(math.sin(math.radians(2 * a)) for a in angulos) / n
    r = math.hypot(c, s)
    z = n * r * r
    p = math.exp(math.sqrt(1 + 4 * n + 4 * (n * n - (n * r) ** 2)) - (1 + 2 * n))   # aproximacion de Zar
    media = (math.degrees(math.atan2(s, c)) / 2.0) % 180.0
    return r, z, min(1.0, p), media


def binomial_cola(k, n, p0):
    """P(X >= k) para X ~ Binomial(n, p0), exacta."""
    return sum(math.comb(n, j) * p0 ** j * (1 - p0) ** (n - j) for j in range(k, n + 1))


def cuenta_ventana(angulos, centro, semi):
    return sum(1 for a in angulos if abs(((a - centro + 90.0) % 180.0) - 90.0) <= semi)


def main():
    print("Python %d.%d.%d (biblioteca estandar)" % sys.version_info[:3])
    rng = random.Random(SEMILLA)
    n = 30
    uniforme = [rng.uniform(0.0, 180.0) for _ in range(n)]
    agrupada = [(rng.gauss(95.0, 12.0)) % 180.0 for _ in range(n)]
    print("Muestras SINTETICAS de n = %d ejes (semilla %d): A uniforme; B agrupada en 95 grados con sigma 12 grados" % (n, SEMILLA))
    for nom, m in (("A uniforme", uniforme), ("B agrupada", agrupada)):
        r, z, p, med = rayleigh_axial(m)
        print("  %-11s R = %.3f  z = nR^2 = %.2f  p(Rayleigh, Zar) = %.4g  eje medio = %.1f" % (nom, r, z, p, med))

    # verificacion de la aproximacion de p por Monte Carlo bajo H0
    rng2 = random.Random(SEMILLA + 1)
    r_obs, z_obs, p_obs, _ = rayleigh_axial(agrupada)
    r_a, z_a, p_a, _ = rayleigh_axial(uniforme)
    sims = 20000
    ge = 0
    for _ in range(sims):
        r_s, _, _, _ = rayleigh_axial([rng2.uniform(0.0, 180.0) for _ in range(n)])
        if r_s >= r_a:
            ge += 1
    p_mc = ge / sims
    print("Verificacion de p para la muestra A: Zar = %.3f ; Monte Carlo (%d sorteos, semilla %d) = %.3f" % (p_a, sims, SEMILLA + 1, p_mc))
    assert abs(p_a - p_mc) < 0.03
    assert p_obs < 1e-6 and p_a > 0.05

    # prueba binomial para una ventana a priori
    centro, semi = 95.0, 5.0
    p0 = 2 * semi / 180.0
    for nom, m in (("A uniforme", uniforme), ("B agrupada", agrupada)):
        k = cuenta_ventana(m, centro, semi)
        print("  Binomial %s: ventana %.0f +- %.0f -> k = %d de %d ; p0 = %.4f ; P(X>=k) = %.4g" % (nom, centro, semi, k, n, p0, binomial_cola(k, n, p0)))
    k_b = cuenta_ventana(agrupada, centro, semi)
    assert abs(binomial_cola(0, 10, 0.3) - 1.0) < 1e-12
    assert binomial_cola(k_b, n, p0) < 1e-4

    # comparaciones multiples: elegir la mejor de m ventanas DESPUES de ver los datos
    m_vent = 8
    nn = 20
    rng3 = random.Random(SEMILLA + 2)
    falsos_libre = falsos_fija = 0
    sims = 4000
    for _ in range(sims):
        d = [rng3.uniform(0.0, 180.0) for _ in range(nn)]
        mejor = min(binomial_cola(cuenta_ventana(d, 180.0 * j / m_vent, semi), nn, p0) for j in range(m_vent))
        if mejor < 0.05:
            falsos_libre += 1
        if binomial_cola(cuenta_ventana(d, 90.0, semi), nn, p0) < 0.05:
            falsos_fija += 1
    print("Falsos positivos al nivel 0.05 con muestras uniformes de n = %d (%d sorteos, semilla %d):" % (nn, sims, SEMILLA + 2))
    print("  ventana fijada antes de ver los datos = %.3f ; mejor de %d ventanas elegida despues = %.3f ; Bonferroni (0.05/%d) = nivel %.4f" % (falsos_fija / sims, m_vent, falsos_libre / sims, m_vent, 0.05 / m_vent))
    assert falsos_libre / sims > 2 * falsos_fija / sims
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
