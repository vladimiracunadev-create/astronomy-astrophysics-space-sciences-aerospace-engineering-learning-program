#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C02: del pixel al angulo, incertidumbre del centroide y aberracion anual.

Datos SINTETICOS: imagen de una estrella gaussiana (FWHM 2.5 px) con ruido de Poisson, 2000 realizaciones, semilla 11.
Camara ILUSTRATIVA: pixel de 9 um, focal 1.2 m. c = 299 792 458 m/s (NIST CODATA, consultado 2026-11-10);
la unidad astronomica 1.495978707e11 m (valor IAU 2012, NO consultado en esta sesion) y el ano de 365.25 d se usan solo para la
velocidad orbital media de la Tierra (aberracion anual). Unidades: px, arcsec, m.
Modelo: centroide por momentos; sigma teorica = sigma_psf / sqrt(N_fotones) por eje. Tolerancia: 5 % entre el valor
empirico y el teorico; aberracion = v/c con 1e-12 relativa frente al calculo directo en radianes.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, platform, sys
import numpy as np

C = 299792458.0
AU = 1.495978707e11
YEAR = 365.25 * 86400.0
RAD2AS = 180 / np.pi * 3600


def main():
    rng = np.random.default_rng(11)
    fwhm = 2.5
    sg = fwhm / 2.3548200450309493
    n = 15
    xs = np.arange(n) - (n - 1) / 2
    X, Y = np.meshgrid(xs, xs)
    psf = np.exp(-((X - 0.31) ** 2 + (Y + 0.22) ** 2) / (2 * sg**2))
    psf /= psf.sum()
    out = []
    res = {}
    out.append(f"Python {platform.python_version()}, NumPy {np.__version__} (imagen SINTETICA, semilla 11)")
    pix, foc = 9e-6, 1.2
    escala = pix / foc * RAD2AS
    out.append(f"Escala de placa = {escala:.4f} arcsec/px (pixel 9 um, focal 1.2 m, ILUSTRATIVOS)")
    out.append(" N_fot    sigma_emp[px]  sigma_teo[px]  sigma[arcsec]")
    ok = True
    for N in (1e3, 1e4, 1e5):
        cx = []
        cy = []
        for _ in range(2000):
            img = rng.poisson(psf * N).astype(float)
            s = img.sum()
            cx.append((img * X).sum() / s)
            cy.append((img * Y).sum() / s)
        emp = float(np.sqrt((np.var(cx, ddof=1) + np.var(cy, ddof=1)) / 2))
        teo = sg / np.sqrt(N)
        out.append(f"{N:6.0f}   {emp:12.5f}  {teo:12.5f}  {emp*escala:12.5f}")
        ok &= abs(emp / teo - 1) < 0.05
        res[f"emp{int(N)}"] = emp
        res[f"teo{int(N)}"] = float(teo)
        res[f"as{int(N)}"] = float(emp * escala)
    v = 2 * np.pi * AU / YEAR
    kappa = v / C
    ab_as = kappa * RAD2AS
    ok &= abs(kappa - (2 * np.pi * AU / YEAR) / C) < 1e-12 * kappa
    out.append(f"Velocidad orbital media de la Tierra = {v/1e3:.4f} km/s ; aberracion maxima v/c = {ab_as:.3f} arcsec")
    d = 1.0e9  # m, distancia ilustrativa
    out.append(f"Un error de 0.01 arcsec a 1.0e6 km equivale a {0.01/RAD2AS*d:.1f} m transversales")
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        raise SystemExit(1)
    res.update(escala=float(escala), v=float(v / 1e3), ab=float(ab_as), err_m=float(0.01 / RAD2AS * d))
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
