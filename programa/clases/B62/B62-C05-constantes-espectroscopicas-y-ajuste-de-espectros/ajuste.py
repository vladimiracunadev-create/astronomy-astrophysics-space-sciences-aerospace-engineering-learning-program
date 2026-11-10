#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B62-C05: ajuste de constantes espectroscopicas (B, D, H) por minimos cuadrados ponderados.

Datos:
  (A) REALES, consultados el 2026-11-09: seis frecuencias del 12C16O del catalogo JPL (c028001.cat), TAG negativo = medidas en laboratorio,
      error declarado 0.0005 MHz. S4. Constantes del WebBook (NIST) para comparar: Be, alpha_e, De. S2. c de CODATA 2022. S1.
  (B) SINTETICOS: lineas generadas con B = 57635.96 MHz, D = 0.1835 MHz, H = 0 y ruido gaussiano de sigma = 0.01 MHz, semilla 20261109.
Modelo: E(J) = B J(J+1) - D [J(J+1)]^2 + H [J(J+1)]^3 ; nu(n) = E(n) - E(n-1), n = J superior (MHz).
Ajuste: minimos cuadrados con pesos 1/sigma^2; covarianza = (A^T W A)^-1 ; chi2 reducido = chi2 / (N - p).
Pruebas: (i) sinteticos sin ruido recuperan B, D exactos (1e-9 relativo); (ii) con ruido, el valor ajustado esta dentro de 4 sigma y
  la cobertura de 1 sigma sobre 2000 repeticiones esta entre 0.64 y 0.72 (valor nominal 0.683).
Supuestos: errores independientes y gaussianos; el catalogo no da correlaciones. Validez: ilustrativa, 6 lineas.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np

C = 299792458.0
CM1_MHZ = C * 100.0 / 1e6                     # 1 cm^-1 en MHz
JPL = np.array([115271.2018, 230538.0000, 345795.9899, 461040.7682, 576267.9305, 691473.0763])
SIG_JPL = 0.0005
BE, AE, DE_WB = 1.93128087, 0.01750441, 6.12147e-06   # WebBook, cm^-1


def disenio(n: np.ndarray, p: int) -> np.ndarray:
    """Matriz de diseno para (B, D, H) con p parametros."""
    xs, xi = n * (n + 1.0), (n - 1.0) * n
    cols = [xs - xi, -(xs ** 2 - xi ** 2), (xs ** 3 - xi ** 3)]
    return np.column_stack(cols[:p])


def ajustar(n, nu, sig, p):
    A = disenio(n, p)
    # escalado de columnas para condicionar el sistema
    s = np.sqrt((A ** 2).sum(axis=0))
    As = A / s
    W = 1.0 / sig
    sol, *_ = np.linalg.lstsq(As * W[:, None], nu * W, rcond=None)
    cov_s = np.linalg.inv((As * W[:, None]).T @ (As * W[:, None]))
    par = sol / s
    cov = cov_s / np.outer(s, s)
    res = nu - A @ par
    chi2 = float(((res / sig) ** 2).sum())
    return par, cov, res, chi2


def main() -> int:
    print(f"Python {platform.python_version()}, numpy {np.__version__}")
    n = np.arange(1, 7, dtype=float)
    sig = np.full(6, SIG_JPL)
    print("(A) Datos REALES: 6 frecuencias de 12C16O del catalogo JPL (consultadas 2026-11-09), sigma = 0.0005 MHz")
    B0wb = (BE - AE / 2) * CM1_MHZ
    for p, nombre in ((2, "B, D"), (3, "B, D, H")):
        par, cov, res, chi2 = ajustar(n, JPL, sig, p)
        err = np.sqrt(np.diag(cov))
        print(f" Ajuste con {nombre}: chi2 = {chi2:.2f} ; grados de libertad = {6-p} ; chi2 reducido = {chi2/(6-p):.2f}")
        print(f"   B = {par[0]:.5f} +- {err[0]:.5f} MHz ({par[0]/CM1_MHZ:.8f} cm^-1) ; D = {par[1]:.6f} +- {err[1]:.6f} MHz ({par[1]/CM1_MHZ:.4e} cm^-1)", end="")
        print(f" ; H = {par[2]:.3e} +- {err[2]:.1e} MHz" if p == 3 else "")
        print("   residuos [MHz]:", ", ".join(f"{r:+.4f}" for r in res))
        if p == 2:
            chi2_2 = chi2
    print(f" Referencia WebBook: B0 = Be - alpha_e/2 = {B0wb:.5f} MHz ; De = {DE_WB*CM1_MHZ:.6f} MHz (diferencia de B: {abs(ajustar(n, JPL, sig, 3)[0][0]-B0wb):.4f} MHz)")
    par3 = ajustar(n, JPL, sig, 3)[0]
    assert abs(par3[0] - B0wb) / B0wb < 1e-6
    assert abs(par3[1] - DE_WB * CM1_MHZ) / (DE_WB * CM1_MHZ) < 0.02
    # (B) sinteticos
    B_t, D_t = 57635.96, 0.1835
    modelo = lambda nn: disenio(nn, 3) @ np.array([B_t, D_t, 0.0])
    par0, _, res0, chi0 = ajustar(n, modelo(n), np.full(6, 0.01), 2)
    print("(B) SINTETICOS (B = 57635.96 MHz, D = 0.1835 MHz, sigma = 0.01 MHz, semilla 20261109)")
    print(f" Sin ruido: B = {par0[0]:.8f} ; D = {par0[1]:.8f} ; chi2 = {chi0:.2e}")
    assert abs(par0[0] - B_t) / B_t < 1e-9 and abs(par0[1] - D_t) / D_t < 1e-6
    rng = np.random.default_rng(20261109)
    sg = np.full(6, 0.01)
    y = modelo(n) + rng.normal(0, 0.01, 6)
    par, cov, res, chi2 = ajustar(n, y, sg, 2)
    err = np.sqrt(np.diag(cov))
    print(f" Con ruido (una realizacion): B = {par[0]:.5f} +- {err[0]:.5f} ; D = {par[1]:.5f} +- {err[1]:.5f} ; chi2 reducido = {chi2/4:.2f}")
    print(f"   desvio en sigmas: B {abs(par[0]-B_t)/err[0]:.2f} ; D {abs(par[1]-D_t)/err[1]:.2f}")
    assert abs(par[0] - B_t) < 4 * err[0] and abs(par[1] - D_t) < 4 * err[1]
    cub = 0
    chis = []
    for _ in range(2000):
        yy = modelo(n) + rng.normal(0, 0.01, 6)
        pp, cc, _, c2 = ajustar(n, yy, sg, 2)
        ee = np.sqrt(np.diag(cc))
        cub += abs(pp[0] - B_t) < ee[0]
        chis.append(c2 / 4)
    cob = cub / 2000
    print(f" Monte Carlo (2000 repeticiones): cobertura de 1 sigma para B = {cob:.3f} (nominal 0.683) ; media de chi2 reducido = {np.mean(chis):.3f} (esperado 1)")
    assert 0.64 < cob < 0.72
    print("Pruebas superadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
