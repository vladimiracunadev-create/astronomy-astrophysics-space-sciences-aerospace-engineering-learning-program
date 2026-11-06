#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B23-C02: pruebas de propiedades físicas de un integrador orbital.

Datos: SINTÉTICOS. Órbita tipo Tierra: semieje a = 1 au, excentricidad e = 0.0167,
inicio en el perihelio. GM_sol nominal IAU 2015 B3 = 1.3271244e20 m^3 s^-2;
1 au = 149597870700 m exactos (IAU 2012 B2); 1 d = 86400 s.
Modelo: problema de dos cuerpos (Sol fijo en el origen), plano (x, y).
Unidades: au, d, au/d. Energía específica eps = v^2/2 - mu/r [au^2 d^-2];
momento angular específico L = x*vy - y*vx [au^2 d^-1].
Integradores: RK4 clásico y velocity-Verlet (salto de rana).
Supuestos: sin otros cuerpos, sin relatividad; órbita cerrada.
Validez: pasos h entre 0.25 y 4 d; horizonte de 10 años.
Tolerancias: la de energía se DERIVA del método (c*h^2 con c estimado en h=2 d y
comprobado en h=1 y 0.5 d); L y la rotación, pocos u*N; reversibilidad, ver código.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np

AU = 149597870700.0
GM_SI = 1.3271244e20
MU = GM_SI * 86400.0**2 / AU**3          # au^3 d^-2
U = np.finfo(float).eps
E_ORB, A_ORB = 0.0167, 1.0


def acel(r, mu=MU, p=2.0):
    n = np.hypot(r[0], r[1])
    return -mu * r / n**(p + 1.0)


def rk4(r, v, h, f=acel):
    k1r, k1v = v, f(r)
    k2r, k2v = v + 0.5*h*k1v, f(r + 0.5*h*k1r)
    k3r, k3v = v + 0.5*h*k2v, f(r + 0.5*h*k2r)
    k4r, k4v = v + h*k3v, f(r + h*k3r)
    return (r + h/6*(k1r + 2*k2r + 2*k3r + k4r),
            v + h/6*(k1v + 2*k2v + 2*k3v + k4v))


def verlet(r, v, h, f=acel):
    vm = v + 0.5*h*f(r)
    rn = r + h*vm
    return rn, vm + 0.5*h*f(rn)


def verlet_mutante_doble_kick(r, v, h, f=acel):   # defecto: aceleración vieja dos veces
    a = f(r)
    rn = r + h*(v + 0.5*h*a)
    return rn, v + h*a


def inicial(theta=0.0, mu=MU):
    rp = A_ORB*(1 - E_ORB)
    vp = math.sqrt(mu*(1 + E_ORB)/(A_ORB*(1 - E_ORB)))
    c, s = math.cos(theta), math.sin(theta)
    R = np.array([[c, -s], [s, c]])
    return R @ np.array([rp, 0.0]), R @ np.array([0.0, vp])


def energia(r, v, mu=MU):
    return 0.5*(v @ v) - mu/np.hypot(r[0], r[1])


def mom_ang(r, v):
    return r[0]*v[1] - r[1]*v[0]


def propagar(paso, h, n, r0, v0, f=acel, mu=MU):
    r, v = r0.copy(), v0.copy()
    emax, lmax = 0.0, 0.0
    e0, l0 = energia(r, v, mu), mom_ang(r, v)
    for _ in range(n):
        r, v = paso(r, v, h, f)
        emax = max(emax, abs((energia(r, v, mu) - e0)/e0))
        lmax = max(lmax, abs((mom_ang(r, v) - l0)/l0))
    return r, v, emax, lmax


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}")
    print(f"mu = {MU:.10e} au^3/d^2   T_kepler(a=1) = {2*math.pi/math.sqrt(MU):.4f} d")
    r0, v0 = inicial()
    dias = 3652.5

    # 1. Energía: la tolerancia se deriva de h^2 (Verlet, orden 2)
    print("\n[Energía] error relativo máximo en 10 años")
    err = {}
    for h in (2.0, 1.0, 0.5):
        n = round(dias/h)
        _, _, em_v, lm_v = propagar(verlet, h, n, r0, v0)
        _, _, em_r, lm_r = propagar(rk4, h, n, r0, v0)
        err[h] = (em_v, em_r, lm_v, lm_r)
        print(f"  h={h:>4} d  Verlet: dE/E={em_v:.2e}  dL/L={lm_v:.2e} | RK4: dE/E={em_r:.2e}  dL/L={lm_r:.2e}")
    c = err[2.0][0]/2.0**2                      # constante estimada en h = 2 d
    print(f"  constante c = dE/E / h^2 estimada en h=2 d: {c:.3e}")
    for h in (1.0, 0.5):
        prueba(err[h][0] <= 1.5*c*h**2, f"Verlet: energía acotada por 1.5*c*h^2 en h={h}")
    razon = err[2.0][0]/err[1.0][0]
    print(f"  razón de errores h=2 / h=1 (esperada ≈ 4): {razon:.2f}")
    prueba(3.0 < razon < 5.0, "la energía de Verlet escala como h^2")
    prueba(err[1.0][1] < 1e-8, "RK4 conserva energía a 1e-8 con h=1 d")

    # 1b. Horizonte largo: RK4 deriva, Verlet queda acotado (h = 5 d)
    print("\n[Horizonte largo] máximo de |dE/E| hasta 10, 100 y 500 años, h = 5 d")
    h5, e0 = 5.0, energia(r0, v0)
    largo = {}
    for nombre, paso in (("Verlet", verlet), ("RK4", rk4)):
        r, v, emax, fila = r0.copy(), v0.copy(), 0.0, []
        pasos_ano = 365.25/h5
        marcas = {round(10*pasos_ano), round(100*pasos_ano), round(500*pasos_ano)}
        for k in range(1, round(500*pasos_ano) + 1):
            r, v = paso(r, v, h5)
            emax = max(emax, abs((energia(r, v) - e0)/e0))
            if k in marcas:
                fila.append(emax)
        largo[nombre] = fila
        print(f"  {nombre:<7}: " + "  ".join(f"{x:.2e}" for x in fila))
    prueba(largo["RK4"][2] > 20*largo["RK4"][0], "RK4: la deriva de energía crece con el tiempo")
    prueba(largo["Verlet"][2] < 1.5*largo["Verlet"][0], "Verlet: el error de energía permanece acotado")

    # 2. Momento angular: exacto (a redondeo) en Verlet, no en RK4
    prueba(err[1.0][2] < 1e-12, "Verlet conserva L a redondeo")
    print(f"  L en Verlet h=1 d: {err[1.0][2]:.2e} (cota 1e-12); en RK4: {err[1.0][3]:.2e}")

    # 3. Reversibilidad temporal
    n = 3653
    print("\n[Reversibilidad] ida N pasos, v -> -v, vuelta N pasos")
    rev = {}
    for nombre, paso in (("Verlet", verlet), ("RK4", rk4)):
        r, v, _, _ = propagar(paso, 1.0, n, r0, v0)
        rr, vv, _, _ = propagar(paso, 1.0, n, r, -v)
        rev[nombre] = np.hypot(*(rr - r0))
        print(f"  {nombre}: |r_final - r_0| = {rev[nombre]:.2e} au")
    prueba(rev["Verlet"] < 1e-10, "Verlet es reversible a redondeo acumulado")

    # 4. Simetría de rotación
    th = math.radians(37.0)
    c_, s_ = math.cos(th), math.sin(th)
    R = np.array([[c_, -s_], [s_, c_]])
    ra, va, _, _ = propagar(verlet, 1.0, n, r0, v0)
    rb, vb, _, _ = propagar(verlet, 1.0, n, *inicial(th))
    dif = np.hypot(*(rb - R @ ra))
    print(f"\n[Rotación] |r(R·ic) - R·r(ic)| = {dif:.2e} au")
    prueba(dif < 1e-11, "el integrador es equivariante ante rotaciones")

    # 5. Qué mutantes detectan las propiedades
    print("\n[Mutantes] ¿qué propiedad falla? (cotas: dE/E<=1.5*c*h^2, dL/L<1e-12, rev<1e-10, rot<1e-11)")
    MU2 = MU*1.01                                             # GM 1 % mal, de forma coherente
    f_gm = lambda r: acel(r, mu=MU2)
    f_exp = lambda r: acel(r, p=2.01)                        # exponente 2.01
    def f_asim(r):                                            # defecto solo si x < 0
        a = acel(r)
        return a if r[0] >= 0 else np.array([a[0], -a[1]])
    casos = [("correcto", verlet, acel, MU), ("GM +1 % (coherente)", verlet, f_gm, MU2),
             ("exponente 2.01", verlet, f_exp, MU), ("fuerza asimétrica", verlet, f_asim, MU),
             ("doble kick", verlet_mutante_doble_kick, acel, MU)]
    resumen = {}
    for nombre, paso, f, mu in casos:
        i0 = inicial(0.0, mu)
        r, v, em, lm = propagar(paso, 1.0, n, *i0, f, mu)
        rr, vv, _, _ = propagar(paso, 1.0, n, r, -v, f, mu)
        rev_ = np.hypot(*(rr - i0[0]))
        ra, _, _, _ = propagar(paso, 1.0, n, *i0, f, mu)
        rb, _, _, _ = propagar(paso, 1.0, n, *inicial(th, mu), f, mu)
        rot = np.hypot(*(rb - R @ ra))
        falla = {"energía": em > 1.5*c*1.0**2, "L": lm >= 1e-12,
                 "reversib.": rev_ >= 1e-10, "rotación": rot >= 1e-11}
        resumen[nombre] = falla
        print(f"  {nombre:<20} dE/E={em:.1e}  falla: {[k for k, x in falla.items() if x] or ('— (pasa)' if nombre == 'correcto' else '— (sobrevive)')}")
    prueba(not any(resumen["correcto"].values()), "la versión correcta pasa todas")
    prueba(not any(resumen["GM +1 % (coherente)"].values()), "GM mal escalado pasa las propiedades (ciego)")
    prueba(not any(resumen["exponente 2.01"].values()), "el exponente 2.01 sobrevive a las propiedades")
    prueba(resumen["fuerza asimétrica"]["L"] and resumen["fuerza asimétrica"]["rotación"],
           "la asimetría rompe L y rotación")
    prueba(resumen["doble kick"]["reversib."] or resumen["doble kick"]["energía"],
           "el doble kick rompe energía o reversibilidad")
    print("\nPruebas superadas.")


if __name__ == "__main__":
    main()
