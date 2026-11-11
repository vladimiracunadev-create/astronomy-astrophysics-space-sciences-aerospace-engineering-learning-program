"""B118-C10 · Síndrome de Kessler como escenario.

Modelo de cero dimensiones, ESCENARIO ILUSTRATIVO (no predicción): dN/dt = S + a N^2 - N/tau.
N objetos en una capa; S fuente anual (lanzamientos + fragmentos de otras fuentes); a N^2 fragmentos por colisiones; tau vida orbital.
Parámetros ILUSTRATIVOS: tau = 25 años, a = 5e-7 por objeto y año. El artículo de Kessler y Cour-Palais (1978) NO se consultó.
Unidades: objetos, años. Integración: Runge-Kutta 4 con paso 0,05 años; tope de seguridad 1e7. Tolerancia: 0,5 % frente al equilibrio analítico.
"""
import math
import sys

TAU = 25.0
A = 5e-7


def f(N, S):
    return S + A * N * N - N / TAU


def rk4(N0, S, anios=300.0, dt=0.05, tope=1e7):
    N, t = N0, 0.0
    t_tope = None
    while t < anios:
        k1 = f(N, S)
        k2 = f(N + 0.5 * dt * k1, S)
        k3 = f(N + 0.5 * dt * k2, S)
        k4 = f(N + dt * k3, S)
        N += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        t += dt
        if N >= tope:
            t_tope = t
            N = tope
            break
        if N < 0:
            N = 0.0
    return N, t_tope


def equilibrios(S):
    disc = 1.0 / TAU ** 2 - 4.0 * A * S
    if disc < 0:
        return None
    r = math.sqrt(disc)
    return (1.0 / TAU - r) / (2 * A), (1.0 / TAU + r) / (2 * A)


def compute():
    v = {}
    v["Sc"] = 1.0 / (4 * A * TAU ** 2)
    v["N_crit"] = 1.0 / (2 * A * TAU)  # equilibrio en la bifurcación
    v["esc"] = []
    for S in (300.0, 700.0, v["Sc"], 1000.0):
        eq = equilibrios(S) if S <= v["Sc"] + 1e-9 else None
        N_fin, t_tope = rk4(10_000.0, S)
        v["esc"].append((S, eq, N_fin, t_tope))
    # dependencia de las condiciones iniciales con S = 300
    eq = equilibrios(300.0)
    v["eq300"] = eq
    v["umbral_inestable"] = eq[1]
    v["ci"] = [(N0, rk4(N0, 300.0)) for N0 in (60_000.0, 0.99 * eq[1], 1.01 * eq[1])]
    # sin colisiones (a = 0): N = S tau
    v["N_sin_col"] = 300.0 * TAU
    # reducción de la fuente a la mitad: recuperación
    v["N_mitad"] = equilibrios(150.0)[0]
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("ESCENARIO ILUSTRATIVO: dN/dt = S + a N^2 - N/tau con tau = 25 anios, a = 5e-7 /(objeto anio); no es una prediccion.")
    v = compute()
    print(f"Fuente critica S_c = 1/(4 a tau^2) = {v['Sc']:.1f} objetos/anio; poblacion en la bifurcacion = {v['N_crit']:.0f}")
    print(" S [obj/anio]  equilibrios (estable, inestable)       N(300 anios) desde 10000   tiempo al tope")
    for S, eq, N_fin, tt in v["esc"]:
        e = "no hay" if eq is None else f"{eq[0]:.0f}, {eq[1]:.0f}"
        t = "-" if tt is None else f"{tt:.1f} anios"
        print(f" {S:11.1f}  {e:34s}  {N_fin:14.0f}   {t}")
    print(f"Sin colisiones (a = 0) con S = 300: N = S tau = {v['N_sin_col']:.0f}; con colisiones el equilibrio estable es {v['eq300'][0]:.0f}")
    print(f"Umbral inestable con S = 300: {v['umbral_inestable']:.0f} objetos")
    for N0, (Nf, tt) in v["ci"]:
        print(f"  N0 = {N0:9.0f} -> N(300 anios) = {Nf:10.0f}" + ("" if tt is None else f" (tope en {tt:.1f} anios)"))
    print(f"Si la fuente baja a 150 obj/anio, el equilibrio estable es {v['N_mitad']:.0f}")
    S, eq, N_fin, tt = v["esc"][0]
    assert abs(N_fin - eq[0]) / eq[0] < 0.005
    assert v["esc"][3][3] is not None
    assert v["ci"][0][1][1] is None and v["ci"][1][1][1] is None and v["ci"][2][1][1] is not None
    print("Pruebas superadas (convergencia al equilibrio analitico a 0.5 %; fuga por encima del umbral).")


if __name__ == "__main__":
    main()
