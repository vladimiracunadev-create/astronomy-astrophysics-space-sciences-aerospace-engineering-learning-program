"""B114-C05 - Despresurizacion de un habitat SINTETICO por un orificio.

Unidades: Pa, K, m3, kg, s. Datos SINTETICOS e ILUSTRATIVOS. Solo stdlib.
R = 8.314462618 J/(mol K) (CODATA 2022, NIST). Umbrales consultados en
NASA OCHMO-TB-003 (2026-11-10): 34.5 kPa (limite inferior de exposicion
indefinida, [V2 6006]) y 6.27 kPa (vaporizacion de fluidos corporales a 37 C).
El tiempo de respuesta de la tripulacion es ILUSTRATIVO.
"""
import math
import sys

R = 8.314462618
M_AIRE = 0.028965
RS = R / M_AIRE
GAMMA = 1.4
CD = 0.8
V = 100.0
T0 = 293.15
P0 = 101325.0
PSI = (2 / (GAMMA + 1)) ** ((GAMMA + 1) / (2 * (GAMMA - 1)))
T_RESP = 300.0          # s, respuesta ilustrativa (colocarse proteccion y sellar)
UMBRALES = (("34.5 kPa", 34500.0), ("6.27 kPa", 6270.0))


def tau_iso(area):
    """Isotermico: P = P0 exp(-t/tau)."""
    return V / (CD * area * math.sqrt(GAMMA * RS * T0) * PSI)


def t_iso(area, p):
    return tau_iso(area) * math.log(P0 / p)


def rk4_iso(area, p_objetivo, dt=0.05):
    """Segunda via: integracion numerica de dP/dt = -P/tau."""
    tau = tau_iso(area)
    f = lambda p: -p / tau
    p, t = P0, 0.0
    while p > p_objetivo:
        k1 = f(p)
        k2 = f(p + 0.5 * dt * k1)
        k3 = f(p + 0.5 * dt * k2)
        k4 = f(p + dt * k3)
        p_nuevo = p + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if p_nuevo <= p_objetivo:
            t += dt * (p - p_objetivo) / (p - p_nuevo)
            return t
        p, t = p_nuevo, t + dt
    return t


def t_adiabatico(area, p_objetivo, dt=0.05):
    """Adiabatico: rho' = -CD A rho sqrt(gamma Rs T) PSI / V con T = T0 (rho/rho0)^(g-1);
    P = rho Rs T."""
    rho0 = P0 / (RS * T0)
    rho, t = rho0, 0.0

    def f(r):
        T = T0 * (r / rho0) ** (GAMMA - 1)
        return -CD * area * r * math.sqrt(GAMMA * RS * T) * PSI / V

    def presion(r):
        return r * RS * T0 * (r / rho0) ** (GAMMA - 1)

    while presion(rho) > p_objetivo:
        k1 = f(rho)
        k2 = f(rho + 0.5 * dt * k1)
        k3 = f(rho + 0.5 * dt * k2)
        k4 = f(rho + dt * k3)
        rho += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += dt
    return t


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Habitat SINTETICO: V = %.0f m3, T0 = %.2f K, P0 = %.0f Pa, Cd = %.1f, "
          "respuesta = %.0f s (ilustrativa)" % (V, T0, P0, CD, T_RESP))
    print("Flujo estrangulado hacia vacio: coeficiente PSI = %.4f" % PSI)
    print(" d [mm]   tau [s]   t->34.5 kPa [s]  t->6.27 kPa [s]  margen resp. [s]")
    for d in (1.0, 5.0, 20.0, 100.0):
        a = math.pi * (d * 1e-3) ** 2 / 4
        tau = tau_iso(a)
        t1 = t_iso(a, UMBRALES[0][1])
        t2 = t_iso(a, UMBRALES[1][1])
        print("%7.1f %9.1f %16.1f %16.1f %16.1f" % (d, tau, t1, t2, t1 - T_RESP))
    # Verificacion por segunda via (RK4) para d = 20 mm
    a20 = math.pi * (20e-3) ** 2 / 4
    t_an = t_iso(a20, 34500.0)
    t_nu = rk4_iso(a20, 34500.0)
    print("d = 20 mm hasta 34.5 kPa: analitico %.3f s ; RK4 %.3f s ; dif rel = %.2e"
          % (t_an, t_nu, abs(t_an - t_nu) / t_an))
    assert abs(t_an - t_nu) / t_an < 1e-6
    # Isotermico frente a adiabatico
    t_ad = t_adiabatico(a20, 34500.0)
    print("d = 20 mm hasta 34.5 kPa: adiabatico %.1f s (isotermico %.1f s) ; cociente = %.3f"
          % (t_ad, t_an, t_ad / t_an))
    assert t_ad < t_an
    # Diametro maximo para tener 600 s hasta 34.5 kPa
    objetivo = 600.0
    lo, hi = 1e-4, 0.5
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if t_iso(math.pi * mid ** 2 / 4, 34500.0) > objetivo:
            lo = mid
        else:
            hi = mid
    print("Diametro maximo de orificio para disponer de %.0f s hasta 34.5 kPa: %.1f mm"
          % (objetivo, hi * 1e3))
    # Escala con el volumen
    print("Escala con el volumen (d = 20 mm, hasta 34.5 kPa):")
    for v in (50.0, 100.0, 400.0):
        t = v / V * t_an
        print("  V = %5.0f m3 -> %.1f s" % (v, t))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
