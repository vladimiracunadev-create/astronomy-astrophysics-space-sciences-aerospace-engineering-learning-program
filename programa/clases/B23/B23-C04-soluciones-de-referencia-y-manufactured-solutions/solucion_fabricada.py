#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B23-C04: método de soluciones fabricadas (MMS) en difusión de calor 1D.

Datos: SINTÉTICOS. Capa de material de espesor L = 1 m, difusividad térmica
kappa = 1.0e-7 m^2/s (valor de ejemplo, no medido), T0 = 250 K, dT = 50 K.
Modelo: T_t = kappa T_zz + s(z,t), 0 < z < L, con T(0,t) dada (Dirichlet) y
T_z(L,t) dada (Neumann). z en m, t en s, T en K, s en K/s.
Solución FABRICADA (no es una solución física):
  T*(z,t) = T0 + dT exp(-t/tau) sin(2 z/L + 0.3),  tau = 1.0e6 s.
Fuente derivada a mano: s = T*_t - kappa T*_zz = dT e^{-t/tau} sin(.)(-1/tau + 4 kappa/L^2).
Método: diferencias finitas de 2.º orden en z + Crank-Nicolson en t; Neumann con
nodo fantasma de 2.º orden. Referencia independiente: solve_ivp (Radau) sobre el
mismo sistema semidiscreto.
Supuestos: coeficientes constantes. Validez: z-malla 10..320 celdas; dt = tf/N_t.
Tolerancias: orden observado en ±0.15 del nominal (2); error en K (norma máxima).
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy.linalg import solve_banded
from scipy.integrate import solve_ivp

L, KAPPA, T0, DT, TAU = 1.0, 1.0e-7, 250.0, 50.0, 1.0e6
TF = 1.0e6


def Tex(z, t):
    return T0 + DT*np.exp(-t/TAU)*np.sin(2*z/L + 0.3)


def Tz_ex(z, t):
    return DT*np.exp(-t/TAU)*(2/L)*np.cos(2*z/L + 0.3)


def fuente(z, t):
    return DT*np.exp(-t/TAU)*np.sin(2*z/L + 0.3)*(-1/TAU + 4*KAPPA/L**2)


def sistema(N, neumann_orden=2):
    """dT/dt = A T + b(t) en los nodos 1..N (z_j = j dz). Devuelve dz, z, A (densa), b(t)."""
    dz = L/N
    z = dz*np.arange(1, N + 1)
    c = KAPPA/dz**2
    A = np.zeros((N, N))
    for j in range(N - 1):
        A[j, j] = -2*c
        if j + 1 < N:
            A[j, j + 1] = c
        if j > 0:
            A[j, j - 1] = c
    # último nodo (z = L): Neumann
    if neumann_orden == 2:      # nodo fantasma: T_{N+1} = T_{N-1} + 2 dz g
        A[N-1, N-1] = -2*c
        A[N-1, N-2] = 2*c
    else:                        # defecto: diferencia de 1.er orden, T_N' ≈ (T_N - T_{N-1})/dz
        A[N-1, N-1] = -c
        A[N-1, N-2] = c

    def b(t):
        v = fuente(z, t).copy()
        v[0] += c*Tex(0.0, t)
        g = Tz_ex(L, t)
        v[N-1] += (2*c*dz*g) if neumann_orden == 2 else (KAPPA*g/dz)
        return v
    return dz, z, A, b


def cn(N, Nt, neumann_orden=2, fuente_en_tn=False):
    dz, z, A, b = sistema(N, neumann_orden)
    dt = TF/Nt
    I = np.eye(N)
    M = I - 0.5*dt*A
    ab = np.zeros((3, N))
    ab[0, 1:] = np.diag(M, 1)
    ab[1] = np.diag(M)
    ab[2, :-1] = np.diag(M, -1)
    R = I + 0.5*dt*A
    T = Tex(z, 0.0)
    for k in range(Nt):
        tn, tn1 = k*dt, (k + 1)*dt
        forz = dt*b(tn) if fuente_en_tn else 0.5*dt*(b(tn) + b(tn1))
        T = solve_banded((1, 1), ab, R @ T + forz)
    return z, T


def error_max(N, Nt, **kw):
    z, T = cn(N, Nt, **kw)
    return float(np.max(np.abs(T - Tex(z, TF))))


def orden(errs):
    return [math.log(errs[i]/errs[i+1])/math.log(2) for i in range(len(errs) - 1)]


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  SciPy {scipy.__version__}")

    # 0. La fuente derivada a mano coincide con una derivación numérica de T*
    z0, t0, h = 0.37, 4.0e5, 1e-4
    tt = (Tex(z0, t0 + 1.0) - Tex(z0, t0 - 1.0))/2.0
    zz = (Tex(z0 + h, t0) - 2*Tex(z0, t0) + Tex(z0 - h, t0))/h**2
    s_num = tt - KAPPA*zz
    print(f"fuente: analítica={fuente(z0, t0):.6e} K/s  numérica={s_num:.6e} K/s")
    prueba(abs(s_num - fuente(z0, t0)) < 1e-8*abs(fuente(z0, t0)) + 1e-12, "la fuente derivada coincide")

    # 1. Refinamiento en el espacio (dt muy pequeño)
    Ns = (10, 20, 40, 80, 160)
    Nt_fino = 4000
    e_esp = [error_max(N, Nt_fino) for N in Ns]
    p_esp = orden(e_esp)
    print("\n[espacio] N: " + " ".join(f"{N:>9}" for N in Ns))
    print("          error[K]: " + " ".join(f"{x:9.2e}" for x in e_esp))
    print("          p:        " + " ".join(f"{x:9.2f}" for x in [float('nan')] + p_esp))
    prueba(abs(p_esp[-1] - 2) < 0.15, "orden espacial 2")

    # 2. Refinamiento en el tiempo (malla espacial fina)
    Nts = (10, 20, 40, 80)
    e_t = [error_max(320, Nt) for Nt in Nts]
    p_t = orden(e_t)
    print("\n[tiempo]  Nt: " + " ".join(f"{x:>9}" for x in Nts))
    print("          error[K]: " + " ".join(f"{x:9.2e}" for x in e_t))
    print("          p:        " + " ".join(f"{x:9.2f}" for x in [float('nan')] + p_t))
    prueba(abs(p_t[-1] - 2) < 0.15, "orden temporal 2")

    # 3. Mutantes
    print("\n[mutantes]")
    e1 = [error_max(N, Nt_fino, neumann_orden=1) for N in Ns]
    p1 = orden(e1)
    print(f"  Neumann de 1.er orden  p espacial: " + " ".join(f"{x:.2f}" for x in p1))
    prueba(abs(p1[-1] - 1) < 0.25, "el defecto de frontera baja el orden a 1")
    e2 = [error_max(320, Nt, fuente_en_tn=True) for Nt in Nts]
    p2 = orden(e2)
    print(f"  fuente solo en t_n     p temporal:  " + " ".join(f"{x:.2f}" for x in p2))
    prueba(abs(p2[-1] - 1) < 0.25, "el defecto temporal baja el orden a 1")
    # Si se refina con dt proporcional a dz^2, el defecto temporal (O(dt)) se disfraza de O(dz^2)
    Ng = (10, 20, 40, 80)
    ph = orden([error_max(N, N*N//10, fuente_en_tn=True) for N in Ng])
    pc = orden([error_max(N, 2*N, fuente_en_tn=True) for N in Ng])
    print("  refinando con Nt = N^2/10 (dt ∝ dz^2), el mismo defecto da p = " + " ".join(f"{x:.2f}" for x in ph) + "  <- disfrazado")
    print("  refinando con Nt = 2N (dt ∝ dz),        el mismo defecto da p = " + " ".join(f"{x:.2f}" for x in pc) + "  <- visible")
    prueba(abs(ph[-1] - 2) < 0.3, "con dt ∝ dz^2 el defecto temporal queda disfrazado")

    # 4. Código de referencia independiente: método de líneas con Radau
    N = 40
    dz, z, A, b = sistema(N)
    sol = solve_ivp(lambda t, T: A @ T + b(t), (0.0, TF), Tex(z, 0.0), method="Radau",
                    rtol=1e-10, atol=1e-10)
    T_ref = sol.y[:, -1]
    _, T_cn = cn(N, 2000)
    d_ref = float(np.max(np.abs(T_cn - T_ref)))
    e_sem = float(np.max(np.abs(T_ref - Tex(z, TF))))
    print(f"\n[referencia] N=40: |CN(Nt=2000) - Radau| = {d_ref:.2e} K;  error espacial de Radau vs T* = {e_sem:.2e} K")
    prueba(d_ref < 1e-6, "CN coincide con la referencia sobre el mismo sistema semidiscreto")
    prueba(e_sem > 100*d_ref, "la diferencia con la referencia es mucho menor que el error espacial")
    print("\nPruebas superadas.")


if __name__ == "__main__":
    main()
