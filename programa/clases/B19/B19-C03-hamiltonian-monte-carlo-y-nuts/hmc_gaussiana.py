#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B19-C03: Hamiltonian Monte Carlo frente a Metropolis de paso aleatorio.

Datos: SIMULADOS. No hay datos observados; el objetivo es una gaussiana
bidimensional con media 0 y covarianza Sigma = [[1, 0.95], [0.95, 1]] (unidades
arbitrarias), de modo que media, covarianza y densidad se conocen exactamente.
Modelo: U(q) = -log pi(q) = 0.5 q^T Sigma^-1 q; K(p) = 0.5 p^T p (masa unidad).
Integrador: salto de rana (leapfrog), paso eps, L pasos.
Supuestos: objetivo suave y unimodal, gradiente exacto.
Validez: es un banco de pruebas; no mide el rendimiento de NUTS completo
(este script NO implementa NUTS: solo comprueba su criterio de giro en U).
Nota: el estimador de ESS (Geyer) puede dar N cuando las autocorrelaciones
iniciales son negativas o nulas; es un limite del estimador, no una ganancia infinita.
Tolerancia: error de energia ∝ eps^2 (cociente 4 +- 1 al dividir eps entre 2);
reversibilidad 1e-10; criterio de giro en U en t = pi/2 (+-0.02);
media 0 +- 0.05 y covarianza +- 0.1 con 20 000 iteraciones.
Solo numpy; ASCII en la salida.
"""
from __future__ import annotations
import math
import platform
import sys

import numpy as np

SIG = np.array([[1.0, 0.95], [0.95, 1.0]])
PREC = np.linalg.inv(SIG)


def U(q):
    return 0.5 * q @ PREC @ q


def gradU(q):
    return PREC @ q


def leapfrog(q, p, eps, L):
    q, p = q.copy(), p.copy()
    p -= 0.5 * eps * gradU(q)
    for i in range(L):
        q += eps * p
        if i != L - 1:
            p -= eps * gradU(q)
    p -= 0.5 * eps * gradU(q)
    return q, p


def H(q, p):
    return U(q) + 0.5 * p @ p


def hmc(n, eps, L, rng, q0=np.zeros(2)):
    q = q0.copy()
    out = np.empty((n, 2))
    acc = 0
    for i in range(n):
        p = rng.normal(size=2)
        qn, pn = leapfrog(q, p, eps, L)
        if math.log(rng.uniform()) < H(q, p) - H(qn, pn):
            q = qn
            acc += 1
        out[i] = q
    return out, acc / n


def rwm(n, paso, rng, q0=np.zeros(2)):
    q = q0.copy()
    out = np.empty((n, 2))
    acc = 0
    for i in range(n):
        prop = q + paso * rng.normal(size=2)
        if math.log(rng.uniform()) < U(q) - U(prop):
            q = prop
            acc += 1
        out[i] = q
    return out, acc / n


def ess(x):
    """Tamano efectivo (Geyer, secuencia positiva inicial) de una serie 1D."""
    x = x - x.mean()
    n = len(x)
    f = np.fft.rfft(x, 2 * n)
    ac = np.fft.irfft(f * np.conj(f))[:n]
    rho = ac / ac[0]
    s = 0.0
    for k in range(1, n - 1, 2):
        pair = rho[k] + rho[k + 1]
        if pair < 0:
            break
        s += pair
    tau = 1.0 + 2.0 * s
    return n / tau


def pruebas():
    rng = np.random.default_rng(7)
    q0, p0 = np.array([1.0, -0.5]), np.array([0.3, 0.8])
    # 1) reversibilidad
    q1, p1 = leapfrog(q0, p0, 0.1, 25)
    q2, p2 = leapfrog(q1, -p1, 0.1, 25)
    assert np.max(np.abs(q2 - q0)) < 1e-10 and np.max(np.abs(-p2 - p0)) < 1e-10
    # 2) error de energia ∝ eps^2 a tiempo total fijo T = 1
    errs = []
    for eps in (0.1, 0.05):
        q1, p1 = leapfrog(q0, p0, eps, int(round(1.0 / eps)))
        errs.append(abs(H(q1, p1) - H(q0, p0)))
    assert 3.0 < errs[0] / errs[1] < 5.0, errs
    # 3) muestras HMC reproducen media y covarianza exactas
    x, _ = hmc(20_000, 0.25, 10, rng)
    assert np.max(np.abs(x.mean(axis=0))) < 0.05
    assert np.max(np.abs(np.cov(x.T) - SIG)) < 0.1
    # 4) criterio de giro en U (NUTS) en oscilador armonico: N(0,1) 1D
    eps, qm, pm = 0.005, 0.0, 1.0
    q, p = qm, pm
    t_stop = None
    for i in range(1, 2000):
        p -= 0.5 * eps * q
        q += eps * p
        p -= 0.5 * eps * q
        if (q - qm) * p < 0 or (q - qm) * pm < 0:
            t_stop = i * eps
            break
    assert t_stop is not None and abs(t_stop - math.pi / 2) < 0.02, t_stop
    return errs, t_stop


def main():
    print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.platform())
    errs, t_stop = pruebas()
    print(f"Pruebas: OK (errores de energia {errs[0]:.2e} y {errs[1]:.2e}; cociente {errs[0]/errs[1]:.2f}; "
          f"giro en U en t = {t_stop:.3f} vs pi/2 = {math.pi/2:.3f})\n")
    rng = np.random.default_rng(2026)
    N = 20_000
    xh, ah = hmc(N, 0.25, 10, rng)
    xr, ar = rwm(N, 0.5, rng)
    print(f"{'metodo':<26}{'acept.':>8}{'ESS q1':>9}{'ESS q2':>9}{'evals/iter':>12}{'ESS(min)/eval':>15}")
    for nom, x, a, ev in (("HMC eps=0.25, L=10", xh, ah, 10), ("Metropolis paso 0.5", xr, ar, 1)):
        e = min(ess(x[:, 0]), ess(x[:, 1]))
        print(f"{nom:<26}{a:8.2f}{ess(x[:,0]):9.0f}{ess(x[:,1]):9.0f}{ev:12d}{e/(N*ev):15.4f}")
    print("\nmedia HMC:", np.round(xh.mean(axis=0), 3), "| cov HMC:", np.round(np.cov(xh.T).ravel(), 3))
    print("media RWM:", np.round(xr.mean(axis=0), 3), "| cov RWM:", np.round(np.cov(xr.T).ravel(), 3))
    # barrido de eps con T = eps*L fijo
    eps_crit = 2.0 / math.sqrt(np.linalg.eigvalsh(PREC).max())
    print(f"\nLimite de estabilidad del salto de rana: eps < 2/sqrt(lambda_max(Sigma^-1)) = {eps_crit:.3f}")
    print("Paso eps (T = 2.5 fijo): aceptacion de HMC")
    for eps in (0.1, 0.25, 0.5, 1.0, 1.5):
        L = max(1, int(round(2.5 / eps)))
        _, a = hmc(4000, eps, L, np.random.default_rng(1))
        print(f"  eps={eps:<5} L={L:<3} aceptacion {a:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
