#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B23-C03: casos analíticos y orden observado de convergencia.

Datos: SINTÉTICOS. Órbita kepleriana a = 1 au, e = 0.0167, inicio en el perihelio.
mu = GM_sol nominal (IAU 2015 B3, 1.3271244e20 m^3/s^2) en au^3/d^2 con
1 au = 149597870700 m (IAU 2012 B2) y 1 d = 86400 s.
Modelo: dos cuerpos, Sol fijo. Solución EXACTA por la ecuación de Kepler:
  M = n t, n = sqrt(mu/a^3);  M = E - e sin E;
  x = a (cos E - e), y = a sqrt(1-e^2) sin E,
  vx = -a n sin E / (1 - e cos E), vy = a n sqrt(1-e^2) cos E / (1 - e cos E).
Supuestos: sin otros cuerpos. Validez: un período, pasos h = T/N con N = 25..800.
Tolerancias: orden observado p dentro de ±0.15 del nominal; casos exactos a 1e-12 au.
Prueba adicional: oscilador armónico x = cos(w t) como caso aún más simple.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np

AU = 149597870700.0
MU = 1.3271244e20 * 86400.0**2 / AU**3
A, E_ORB = 1.0, 0.0167
N_MED = math.sqrt(MU / A**3)
T_ORB = 2*math.pi/N_MED


def kepler_E(M, e):
    M = math.fmod(M, 2*math.pi)
    E = M if e < 0.8 else math.pi
    for _ in range(60):
        dE = (E - e*math.sin(E) - M)/(1 - e*math.cos(E))
        E -= dE
        if abs(dE) < 1e-15:
            break
    return E


def exacto(t, mu=MU):
    n = math.sqrt(mu/A**3)
    E = kepler_E(n*t, E_ORB)
    s, c = math.sin(E), math.cos(E)
    q = math.sqrt(1 - E_ORB**2)
    d = 1 - E_ORB*c
    return (np.array([A*(c - E_ORB), A*q*s]),
            np.array([-A*n*s/d, A*n*q*c/d]))


def acel(r, mu=MU):
    return -mu*r/np.hypot(r[0], r[1])**3


def euler(r, v, h, f=acel):
    return r + h*v, v + h*f(r)


def verlet(r, v, h, f=acel):
    vm = v + 0.5*h*f(r)
    rn = r + h*vm
    return rn, vm + 0.5*h*f(rn)


def rk4(r, v, h, f=acel):
    k1r, k1v = v, f(r)
    k2r, k2v = v + 0.5*h*k1v, f(r + 0.5*h*k1r)
    k3r, k3v = v + 0.5*h*k2v, f(r + 0.5*h*k2r)
    k4r, k4v = v + h*k3v, f(r + h*k3r)
    return (r + h/6*(k1r + 2*k2r + 2*k3r + k4r), v + h/6*(k1v + 2*k2v + 2*k3v + k4v))


def rk4_mutante(r, v, h, f=acel):      # defecto: k3 usa k1 en lugar de k2
    k1r, k1v = v, f(r)
    k2r, k2v = v + 0.5*h*k1v, f(r + 0.5*h*k1r)
    k3r, k3v = v + 0.5*h*k1v, f(r + 0.5*h*k2r)
    k4r, k4v = v + h*k3v, f(r + h*k3r)
    return (r + h/6*(k1r + 2*k2r + 2*k3r + k4r), v + h/6*(k1v + 2*k2v + 2*k3v + k4v))


def error_final(paso, N, f=acel, tf=None):
    tf = T_ORB if tf is None else tf
    h = tf/N
    r, v = exacto(0.0)
    for _ in range(N):
        r, v = paso(r, v, h, f)
    rex, _ = exacto(tf)
    return float(np.hypot(*(r - rex)))


def orden_observado(paso, f=acel, Ns=(50, 100, 200, 400)):
    e = [error_final(paso, N, f) for N in Ns]
    ps = [math.log(e[i]/e[i+1])/math.log(2) for i in range(len(e)-1)]
    return e, ps


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}")
    print(f"mu={MU:.10e} au^3/d^2  T={T_ORB:.4f} d  n={N_MED:.8f} rad/d")

    # 1. Casos exactos de la propia solución analítica
    r0, v0 = exacto(0.0)
    prueba(abs(r0[0] - A*(1 - E_ORB)) < 1e-15 and r0[1] == 0.0, "perihelio en t=0")
    rT, vT = exacto(T_ORB)
    prueba(np.hypot(*(rT - r0)) < 1e-12 and np.hypot(*(vT - v0)) < 1e-14, "regresa tras un período")
    rH, _ = exacto(T_ORB/2)
    prueba(abs(rH[0] + A*(1 + E_ORB)) < 1e-12 and abs(rH[1]) < 1e-12, "afelio en T/2")
    # la solución analítica cumple la conservación de energía y L
    r1, v1 = exacto(100.0)
    e0 = 0.5*(v0@v0) - MU/np.hypot(*r0)
    e1 = 0.5*(v1@v1) - MU/np.hypot(*r1)
    prueba(abs((e1 - e0)/e0) < 1e-13, "la solución exacta conserva la energía")
    prueba(abs((r1[0]*v1[1] - r1[1]*v1[0]) - (r0[0]*v0[1])) < 1e-15, "y el momento angular")
    print(f"solución exacta: perihelio, período T y afelio en T/2 coinciden (afelio x = {rH[0]:.6f} au)")

    # 2. Oscilador armónico: x'' = -w^2 x, x(0)=1, v(0)=0, solución cos(w t).
    #    Trampa: en t = 1 (un período) el error de fase de Verlet entra al cuadrado.
    w = 2*math.pi
    for tf in (1.0, 0.3):
        for nombre, paso, p_nom in (("Verlet", verlet, 2), ("RK4", rk4, 4)):
            err = []
            for N in (20, 40, 80):
                h = tf/N
                r, v = np.array([1.0]), np.array([0.0])
                for _ in range(N):
                    r, v = paso(r, v, h, lambda x: -w*w*x)
                err.append(abs(r[0] - math.cos(w*tf)))
            p = math.log(err[0]/err[1])/math.log(2)
            print(f"oscilador t={tf} {nombre}: errores {['%.2e' % x for x in err]}  p ≈ {p:.2f} (nominal {p_nom})")
            if tf == 0.3:
                prueba(abs(p - p_nom) < 0.15, f"orden del oscilador con {nombre}")

    # 3. Orden observado en la órbita de Kepler
    print("\norden observado (error de posición tras un período) (N = 50..400; Euler: 1600..12800)")
    esperado = {"Euler": 1, "Verlet": 2, "RK4": 4}
    for nombre, paso in (("Euler", euler), ("Verlet", verlet), ("RK4", rk4)):
        e, ps = orden_observado(paso, Ns=(1600, 3200, 6400, 12800) if nombre == 'Euler' else (50, 100, 200, 400))
        print(f"  {nombre:<7} errores [au]: " + "  ".join(f"{x:.2e}" for x in e)
              + "  p: " + " ".join(f"{x:.2f}" for x in ps))
        prueba(abs(ps[-1] - esperado[nombre]) < 0.15,
               f"orden de {nombre} dentro de la tolerancia")

    # 4. Mutantes
    print("\nmutantes (orden observado y tamaño del error)")
    e, ps = orden_observado(rk4_mutante)
    print(f"  RK4 con k3 mal      errores: " + "  ".join(f"{x:.2e}" for x in e)
          + "  p: " + " ".join(f"{x:.2f}" for x in ps))
    prueba(ps[-1] < 3.5, "el orden delata el defecto de RK4")
    f_gm = lambda r: acel(r, MU*1.01)
    Ns = (50, 100, 200, 400, 800)
    eg = [error_final(rk4, N, f_gm) for N in Ns]
    print("  GM +1 % en RK4      errores: " + "  ".join(f"{x:.2e}" for x in eg)
          + "  (no tienden a 0: error de modelo)")
    prueba(eg[-1] > 1e-3 and eg[-1]/eg[-2] > 0.9, "el error se estanca lejos de cero")
    ec = [error_final(rk4, N) for N in Ns]
    print("  RK4 correcto        errores: " + "  ".join(f"{x:.2e}" for x in ec))
    prueba(ec[-1] < 1e-8, "RK4 correcto llega a 1e-8 au")
    print("\nPruebas superadas.")


if __name__ == "__main__":
    main()
