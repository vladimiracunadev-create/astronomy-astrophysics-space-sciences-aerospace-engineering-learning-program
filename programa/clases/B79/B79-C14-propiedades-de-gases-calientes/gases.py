#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C14: propiedades termofisicas de gases calientes con polinomios de Shomate (NIST Chemistry WebBook).

Consultado (2026-11-10): NIST Chemistry WebBook, fichas de CO2 (C124389), H2O (C7732185) y N2 (C7727379), "Gas phase thermochemistry":
masas molares 44.0095, 18.0153 y 28.0134 g/mol y coeficientes de Shomate A-H por rango (Chase 1998) transcritos abajo.
  Cp = A + B t + C t^2 + D t^3 + E / t^2 [J/(mol K)], t = T/1000 K; H - H298 = A t + B t^2/2 + C t^3/3 + D t^4/4 - E/t + F - H [kJ/mol].
ESTANDAR (no consultado): mezcla ideal por fracciones molares; gamma = cp/(cp - R_u/M); velocidad del sonido a = sqrt(gamma R T).
ILUSTRATIVOS (sinteticos, no medidos): composicion de productos de una combustion estequiometrica de metano con aire:
  CH4 + 2 O2 + 7.52 N2 -> CO2 + 2 H2O + 7.52 N2 (relacion 1 : 2 : 7.52, de la ecuacion balanceada; no es un calculo de equilibrio ni incluye disociacion).
Rangos de validez: CO2 298-6000 K, H2O 500-6000 K, N2 100-6000 K; se usa T >= 500 K.
Via 2: H(T2) - H(T1) por integral numerica de Cp frente al polinomio de entalpia.
Via 3: expansion isentropica de 3000 K con relacion de presiones 1/50: integral de dT/T = (R/cp) dp/p frente a gamma constante.
Tolerancias: entalpia por integral frente a polinomio < 1e-8 relativa dentro de un rango y < 1e-4 cruzando un empalme (los ajustes de NIST no son exactamente continuos en H); salto de Cp en el empalme reportado.
"""
import math, platform

RU = 8.314462618  # J/(mol K); constante molar del gas (CODATA 2018; no consultada en esta clase)

COEF = {
    "CO2": [(298.0, 1200.0, (24.99735, 55.18696, -33.69137, 7.948387, -0.136638, -403.6075, 228.2431, -393.5224)),
            (1200.0, 6000.0, (58.16639, 2.720074, -0.492289, 0.038844, -6.447293, -425.9186, 263.6125, -393.5224))],
    "H2O": [(500.0, 1700.0, (30.09200, 6.832514, 6.793435, -2.534480, 0.082139, -250.8810, 223.3967, -241.8264)),
            (1700.0, 6000.0, (41.96426, 8.622053, -1.499780, 0.098119, -11.15764, -272.1797, 219.7809, -241.8264))],
    "N2": [(100.0, 500.0, (28.98641, 1.853978, -9.647459, 16.63537, 0.000117, -8.671914, 226.4168, 0.0)),
           (500.0, 2000.0, (19.50583, 19.88705, -8.598535, 1.369784, 0.527601, -4.935202, 212.3900, 0.0)),
           (2000.0, 6000.0, (35.51872, 1.128728, -0.196103, 0.014662, -4.553760, -18.97091, 224.9810, 0.0))],
}
MOLAR = {"CO2": 44.0095, "H2O": 18.0153, "N2": 28.0134}  # g/mol
FRAC_N = {"CO2": 1.0, "H2O": 2.0, "N2": 7.52}
TOT = sum(FRAC_N.values())
X = {k: v / TOT for k, v in FRAC_N.items()}


def coef(sp, T):
    for lo, hi, c in COEF[sp]:
        if lo <= T <= hi:
            return c
    raise ValueError(f"{sp}: {T} K fuera de rango")


def cp_mol(sp, T):
    A, B, C, D, E, F, G, H = coef(sp, T)
    t = T / 1000.0
    return A + B * t + C * t * t + D * t ** 3 + E / (t * t)


def h_mol(sp, T):
    """H - H298 en J/mol."""
    A, B, C, D, E, F, G, H = coef(sp, T)
    t = T / 1000.0
    return 1000.0 * (A * t + B * t * t / 2 + C * t ** 3 / 3 + D * t ** 4 / 4 - E / t + F - H)


def mezcla_cp(T):
    return sum(X[s] * cp_mol(s, T) for s in X)


def masa_molar():
    return sum(X[s] * MOLAR[s] for s in X)


def gamma_mezcla(T):
    cp = mezcla_cp(T)
    return cp / (cp - RU)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    M = masa_molar()
    Rm = RU / (M / 1000.0)
    print("Mezcla ILUSTRATIVA (CH4 + 2 O2 + 7.52 N2 -> CO2 + 2 H2O + 7.52 N2): " + ", ".join(f"x_{s} = {X[s]:.4f}" for s in X))
    print(f"M = {M:.4f} g/mol ; R = {Rm:.2f} J/(kg K)")
    print("   T [K]   cp CO2   cp H2O   cp N2    cp mezcla [J/(mol K)]   cp [J/(kg K)]   gamma    a [m/s]")
    for T in (500.0, 1000.0, 1500.0, 2000.0, 3000.0):
        cpm = mezcla_cp(T)
        cpk = cpm / (M / 1000.0)
        g = gamma_mezcla(T)
        a = math.sqrt(g * Rm * T)
        print(f" {T:7.0f}  {cp_mol('CO2', T):7.3f}  {cp_mol('H2O', T):7.3f}  {cp_mol('N2', T):7.3f}     {cpm:9.3f}           {cpk:9.1f}      {g:.4f}  {a:7.1f}")
    # empalmes
    print("Discontinuidad de cp en los empalmes de rangos [J/(mol K)]:")
    peor_salto = 0.0
    for sp, T in (("CO2", 1200.0), ("H2O", 1700.0), ("N2", 2000.0)):
        lo = [c for c in COEF[sp] if c[1] == T][0][2]
        hi = [c for c in COEF[sp] if c[0] == T][0][2]
        def cp_c(c):
            A, B, C, D, E = c[:5]
            t = T / 1000.0
            return A + B * t + C * t * t + D * t ** 3 + E / (t * t)
        salto = cp_c(hi) - cp_c(lo)
        peor_salto = max(peor_salto, abs(salto))
        print(f"  {sp} en {T:.0f} K: salto = {salto:+.4f}")
    # via 2: entalpia por integral numerica (dentro de un solo rango y cruzando el empalme)
    peor = 0.0
    peor_cruce = 0.0
    tramos = {"CO2": (1300.0, 2500.0, 800.0), "H2O": (600.0, 1600.0, 1000.0), "N2": (600.0, 1900.0, 1000.0)}
    for sp, (ta, tb, t0) in tramos.items():
        n = 100000
        h = (tb - ta) / n
        s = sum(cp_mol(sp, ta + (i + 0.5) * h) * h for i in range(n))
        ref = h_mol(sp, tb) - h_mol(sp, ta)
        peor = max(peor, abs(s - ref) / ref)
        # cruzando el empalme
        t1, t2 = t0, 2500.0
        h2 = (t2 - t1) / n
        s2 = sum(cp_mol(sp, t1 + (i + 0.5) * h2) * h2 for i in range(n))
        ref2 = h_mol(sp, t2) - h_mol(sp, t1)
        peor_cruce = max(peor_cruce, abs(s2 - ref2) / ref2)
        print(f"  {sp}: un solo rango {ta:.0f}-{tb:.0f} K: polinomio = {ref / 1e3:.4f} kJ/mol ; integral de cp = {s / 1e3:.4f} kJ/mol ; cruzando el empalme {t1:.0f}-{t2:.0f} K: {ref2 / 1e3:.4f} frente a {s2 / 1e3:.4f}")
    print(f"Diferencia relativa maxima: un rango = {peor:.2e} ; cruzando el empalme = {peor_cruce:.2e}")
    # via 3: expansion de 3000 K con razon de presiones 1/50
    T = 3000.0
    n = 20000
    lnr = math.log(1 / 50.0) / n
    for _ in range(n):
        cpk = mezcla_cp(T) / (M / 1000.0)
        T *= math.exp(Rm / cpk * lnr)
    gm = gamma_mezcla(3000.0)
    t_const = 3000.0 * (1 / 50.0) ** ((gm - 1) / gm)
    t_14 = 3000.0 * (1 / 50.0) ** (0.4 / 1.4)
    print(f"Expansion isentropica 3000 K, p2/p1 = 1/50: cp(T) variable -> T2 = {T:.1f} K ; gamma constante a 3000 K ({gm:.4f}) -> {t_const:.1f} K ; gamma = 1.4 -> {t_14:.1f} K")
    v_var = math.sqrt(2 * (sum(X[s] * (h_mol(s, 3000.0) - h_mol(s, T)) for s in X) / (M / 1000.0)))
    v_const = math.sqrt(2 * mezcla_cp(3000.0) / (M / 1000.0) * (3000.0 - t_const))
    print(f" velocidad de escape de esa expansion: cp(T) variable = {v_var:.1f} m/s ; gamma y cp constantes a 3000 K = {v_const:.1f} m/s ; diferencia = {100 * (v_const - v_var) / v_var:.1f} %")
    assert peor < 1e-8 and peor_cruce < 1e-4
    assert peor_salto < 0.2
    assert abs(sum(X.values()) - 1.0) < 1e-12
    print("Pruebas superadas.")


main()
