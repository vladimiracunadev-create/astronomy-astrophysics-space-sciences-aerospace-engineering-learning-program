"""B67-C03: presupuesto de perdida de hielo de una muestra expuesta al vacio.

Presion de vapor del hielo: Murphy y Koop (2005), ec. (7), T > 110 K, T en K, p en Pa:
    p = exp(9.550426 - 5723.265/T + 3.53068 ln T - 0.00728332 T)
Flujo de sublimacion al vacio (Hertz-Knudsen, coeficiente de evaporacion alpha = 1,
es decir, COTA SUPERIOR):  J = m alpha p / sqrt(2 pi m kB T)   [kg m-2 s-1]
Constantes: kB = 1,380649e-23 J/K y R = 8,314462618 J/(mol K) (valores del SI);
m(H2O) = 18,01528 u con u = 1,66053907e-27 kg y densidad del hielo 917 kg/m3
(valores de referencia estandar, NO consultados para esta clase).
Granos esfericos de hielo puro (SINTETICO). Requiere solo numpy.
"""
import sys
import numpy as np

KB = 1.380649e-23
R_GAS = 8.314462618
M = 18.01528 * 1.66053907e-27
RHO = 917.0


def p_hielo(T):
    T = np.asarray(T, float)
    return np.exp(9.550426 - 5723.265 / T + 3.53068 * np.log(T) - 0.00728332 * T)


def flujo(T, alpha=1.0):
    return M * alpha * p_hielo(T) / np.sqrt(2 * np.pi * M * KB * T)


def tiempo_perdida(T, r0, frac=0.01):
    """tiempo [s] para perder la fraccion 'frac' de la masa de un grano de radio r0 [m]."""
    r1 = r0 * (1 - frac) ** (1 / 3)
    return (r0 - r1) * RHO / flujo(T)


def perdida_en(T, r0, t):
    """fraccion de masa perdida tras t [s] a T constante (analitica, flujo constante)."""
    r = max(r0 - flujo(T) * t / RHO, 0.0)
    return 1 - (r / r0) ** 3


def main():
    print(f"Python {sys.version.split()[0]} ; numpy {np.__version__}")
    print("DATOS SINTETICOS: granos de hielo puro de 100 um de radio (ilustrativo, no es una muestra real)")
    p_tp = float(p_hielo(273.16))
    print(f"p_hielo(273,16 K) = {p_tp:.3f} Pa (punto triple de referencia ~ 611,657 Pa, no consultado)")
    assert abs(p_tp - 611.657) / 611.657 < 0.005
    print("T [K]   p [Pa]        J [kg m-2 s-1]   t(1 % masa, r=100 um)")
    r0 = 100e-6
    for T in (110.0, 130.0, 150.0, 170.0, 200.0, 250.0):
        t = tiempo_perdida(T, r0)
        if t > 3.15e7 * 1e3:
            ts = ">1e3 anios"
        elif t > 3.15e7:
            ts = f"{t / 3.15e7:.3g} anios"
        elif t > 3600:
            ts = f"{t / 3600:.3g} h"
        else:
            ts = f"{t:.3g} s"
        print(f"{T:5.0f}  {float(p_hielo(T)):.3e}  {float(flujo(T)):.3e}      {ts}")
    # monotonia
    Ts = np.linspace(110, 270, 200)
    assert np.all(np.diff(flujo(Ts)) > 0)
    # entalpia de sublimacion implicita
    for T in (150.0, 200.0, 250.0):
        L = R_GAS * (5723.265 + 3.53068 * T - 0.00728332 * T ** 2)
        print(f"Entalpia de sublimacion implicita a {T:.0f} K = {L / 1e3:.2f} kJ/mol")
    # derivada numerica vs analitica a 200 K
    h = 1e-3
    d_num = (np.log(p_hielo(200 + h)) - np.log(p_hielo(200 - h))) / (2 * h)
    d_ana = 5723.265 / 200 ** 2 + 3.53068 / 200 - 0.00728332
    assert abs(d_num - d_ana) / d_ana < 1e-6
    # integracion numerica del encogimiento (pasos) frente a la formula analitica
    T, t_tot, n = 150.0, 3 * 86400.0, 3000
    r = r0
    dt = t_tot / n
    for _ in range(n):
        r -= flujo(T) * dt / RHO
    f_num = 1 - (r / r0) ** 3
    f_ana = perdida_en(T, r0, t_tot)
    print(f"Perdida en 3 d a 150 K: numerica {100 * f_num:.4f} % ; analitica {100 * f_ana:.4f} %")
    assert abs(f_num - f_ana) < 1e-9
    # temperatura maxima para perder <= 1 % en 1 h (biseccion)
    lo, hi = 110.0, 270.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if perdida_en(mid, r0, 3600.0) > 0.01:
            hi = mid
        else:
            lo = mid
    print(f"Temperatura maxima de manipulacion (1 h, perdida <= 1 %, r=100 um): {lo:.2f} K")
    # efecto del tamano: granos mas finos pierden mas rapido en proporcion
    for rr in (10e-6, 100e-6, 1e-3):
        print(f"  radio {rr * 1e6:7.0f} um: perdida en 1 h a 170 K = {100 * perdida_en(170.0, rr, 3600.0):.3f} %")
    assert perdida_en(170.0, 10e-6, 3600) > perdida_en(170.0, 1e-3, 3600)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
