#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C12: modos mixtos de una gigante roja con la relacion asintotica de acoplamiento p-g.

Datos: ninguna constante fisica. Todo es SINTETICO (ilustrativo): Delta nu = 9,0 uHz, nu_p = 100 uHz (un modo de presion dipolar), epsilon_g = 0,25, coeficiente de acoplamiento q = 0,15
y espaciados de periodos Delta Pi_1 = 80 s (rama de gigantes con capa de hidrogeno) o 300 s (nucleo de helio). Los ordenes de magnitud 50-100 s frente a 100-300 s solo se conocen del resumen de
Bedding et al. (2011, Nature 471, 608), obtenido por busqueda el 2026-11-09; no se leyo el articulo y las cifras del laboratorio no se atribuyen a el.
Modelo: relacion asintotica de modos mixtos tan(pi (nu - nu_p)/Delta nu) = q tan(pi (1/(nu Delta Pi_1) - eps_g)); se hallan las raices por biseccion en cada rama de la tangente.
Contraste independiente: numero de modos mixtos por orden p, N_g = (1/Delta Pi_1)(1/nu_min - 1/nu_max) (modos g puros dentro de la ventana de un orden p), de modo que las raices deben ser N_g + 1 (el modo p); limites q -> 0 (modos puros p y g) y espaciado de periodos
de los modos mixtos, que es menor que Delta Pi_1 y alcanza su minimo cerca de nu_p.
Supuestos: forma asintotica de Shibahashi (1979) en la formulacion habitual, acoplamiento constante, sin rotacion. Validez: orientativa.
Tolerancia: recuento de raices dentro de +/- 1,5 de N_g + 1; con q = 1e-4 cada raiz cae a 0,02 uHz de una frecuencia pura; espaciado minimo cerca de nu_p (dentro de 1,5 uHz) y siempre menor que Delta Pi_1.
"""
from __future__ import annotations
import math, platform, sys

DNU, NUP, EPSG, Q = 9.0, 100.0, 0.25, 0.15


def F(nu, dPi, q):
    """F(nu) = tan(theta_p) - q tan(theta_g); las raices son los modos. nu en uHz, dPi en s."""
    tp = math.pi * (nu - NUP) / DNU
    tg = math.pi * (1e6 / (nu * dPi) - EPSG)
    return math.sin(tp) * math.cos(tg) - q * math.sin(tg) * math.cos(tp)


def raices(dPi, q, lo, hi, n=40000):
    xs = [lo + (hi - lo) * i / n for i in range(n + 1)]
    out = []
    fv = [F(x, dPi, q) for x in xs]
    for i in range(n):
        if fv[i] * fv[i + 1] < 0:
            a, b, fa = xs[i], xs[i + 1], fv[i]
            for _ in range(60):
                m = 0.5 * (a + b)
                fm = F(m, dPi, q)
                if fm * fa > 0:
                    a, fa = m, fm
                else:
                    b = m
            out.append(0.5 * (a + b))
    return out


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    lo, hi = NUP - DNU / 2, NUP + DNU / 2
    print(f"{'DeltaPi1 [s]':>12} {'N_g en la ventana':>18} {'raices':>7} {'espaciado de periodos min / max [s]':>38}")
    resumen = {}
    for dPi in (80.0, 300.0):
        r = raices(dPi, Q, lo, hi)
        N = 1e6 / dPi * (1 / lo - 1 / hi)
        per = [1e6 / x for x in r]
        per.sort()
        esp = [b - a for a, b in zip(per, per[1:])]
        resumen[dPi] = (len(r), N, min(esp), max(esp))
        print(f"{dPi:12.0f} {N:18.2f} {len(r):7d} {min(esp):17.2f} / {max(esp):.2f}")
        assert abs(len(r) - (N + 1)) <= 1.5
        assert min(esp) > 0
    for dPi, (n, N, emin, emax) in resumen.items():
        assert emin < dPi and emax < dPi * 1.0001
    # limite q -> 0: las raices se agrupan en los modos puros
    r0 = raices(80.0, 1e-4, lo, hi)
    puros_g = [1e6 / (80.0 * (k + 0.5 + EPSG)) for k in range(1, 4000)]
    puros_g = [x for x in puros_g if lo < x < hi]
    puros_p = [NUP + DNU * k for k in (-1, 0, 1) if lo < NUP + DNU * k < hi] or [NUP]
    cerca = 0
    for x in r0:
        dmin = min(abs(x - y) for y in puros_g + puros_p)
        cerca += dmin < 0.02
    print(f"q = 1e-4: {len(r0)} raices, {cerca} a menos de 0,02 uHz de un modo puro p o g")
    assert cerca == len(r0)
    # el espaciado minimo (modos apretados) ocurre cerca del modo de presion
    r = raices(80.0, Q, lo, hi)
    per = sorted(1e6 / x for x in r)
    esp = [(b - a, 0.5 * (a + b)) for a, b in zip(per, per[1:])]
    emin, pmed = min(esp)
    print(f"espaciado minimo = {emin:.1f} s en el periodo {pmed:.0f} s (nu = {1e6 / pmed:.2f} uHz, nu_p = {NUP})")
    assert abs(1e6 / pmed - NUP) < 1.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
