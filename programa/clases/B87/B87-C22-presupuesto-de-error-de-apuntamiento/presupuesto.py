#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C22: presupuesto de error de apuntamiento por eje con contribuyentes SINTETICOS (arcsec, 1 sigma, de ejemplo): combinacion por
suma cuadratica (RSS) frente a la suma lineal y verificacion por Monte Carlo (100 000 sorteos por eje, semilla 20260525), con un termino
uniforme acotado; error radial de dos ejes (Rayleigh). Requisito de ejemplo: 30 arcsec (3 sigma, por eje). Ningun valor es de una mision."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

# (nombre, tipo, sigma_arcsec, distribucion)  ; 'unif' se define por su semiancho a con sigma = a/sqrt(3)
CONTR = [
    ("ruido del rastreador estelar (aleatorio)", 3.0, "gauss"),
    ("alineamiento rastreador-carga (sesgo)", 5.0, "gauss"),
    ("distorsion termica de la estructura (sesgo lento)", 4.0, "gauss"),
    ("error de control residual (aleatorio)", 2.5, "gauss"),
    ("vibracion de ruedas, jitter (aleatorio)", 1.5, "gauss"),
    ("retardo y sincronizacion (acotado uniforme +-a)", 2.0, "unif"),
]
REQ_3SIG = 30.0


def calcular(n=100000, seed=20260525):
    rng = np.random.default_rng(seed)
    sig = np.array([c[1] for c in CONTR])
    muestras = []
    for (nm, s, dist) in CONTR:
        if dist == "gauss":
            muestras.append(s * rng.standard_normal(n))
        else:
            a = s * math.sqrt(3)
            muestras.append(rng.uniform(-a, a, n))
    tot = np.sum(muestras, axis=0)
    rss = math.sqrt(np.sum(sig ** 2))
    lin = float(np.sum(sig))
    mc_sd = float(tot.std())
    q997 = float(np.percentile(np.abs(tot), 99.73))
    # radial de dos ejes independientes
    tot2 = np.sum([s * rng.standard_normal(n) if d == "gauss" else rng.uniform(-s * math.sqrt(3), s * math.sqrt(3), n) for (_, s, d) in CONTR], axis=0)
    rad = np.hypot(tot, tot2)
    q_rad = float(np.percentile(rad, 99.73))
    contrib = 100 * sig ** 2 / np.sum(sig ** 2)
    sin_mayor = math.sqrt(np.sum(sig ** 2) - sig.max() ** 2)
    return dict(sig=sig, rss=rss, lin=lin, mc_sd=mc_sd, q997=q997, q_rad=q_rad, teo_rad=rss * math.sqrt(-2 * math.log(1 - 0.9973)),
                contrib=contrib, margen=REQ_3SIG - 3 * rss, sin_mayor=sin_mayor, n=n)


def main():
    banner("B87-C22 presupuesto de apuntamiento | contribuyentes SINTETICOS (arcsec 1 sigma), Monte Carlo de 100000 sorteos (semilla 20260525)")
    d = calcular()
    print("contribuyente                                          sigma [arcsec]   aporte a la varianza [%]")
    for (nm, s, dist), c in zip(CONTR, d['contrib']):
        print(f"{nm:52s} {s:10.2f} {c:16.1f}")
    print(f"suma cuadratica (RSS, 1 sigma) = {d['rss']:.3f} arcsec ; suma lineal (peor caso) = {d['lin']:.2f} arcsec")
    print(f"Monte Carlo: desviacion total = {d['mc_sd']:.3f} arcsec ; percentil 99.73 de |error| = {d['q997']:.2f} arcsec (3 RSS = {3*d['rss']:.2f})")
    print(f"requisito {REQ_3SIG:.0f} arcsec (3 sigma): margen = {d['margen']:.2f} arcsec ; sin el mayor contribuyente RSS = {d['sin_mayor']:.3f} arcsec")
    print(f"error radial de dos ejes, percentil 99.73 = {d['q_rad']:.2f} arcsec (teoria Rayleigh {d['teo_rad']:.2f})")
    assert abs(d['mc_sd'] - d['rss']) / d['rss'] < 0.01 and abs(d['q997'] - 3 * d['rss']) / (3 * d['rss']) < 0.03
    assert abs(d['q_rad'] - d['teo_rad']) / d['teo_rad'] < 0.04 and d['lin'] > d['rss']
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
