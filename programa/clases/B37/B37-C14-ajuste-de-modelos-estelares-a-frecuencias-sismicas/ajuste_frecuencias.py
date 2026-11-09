#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C14: ajuste de una rejilla de modelos a frecuencias sismicas con y sin correccion del efecto de superficie.

Datos: ninguna constante fisica externa. Todo es SINTETICO (ilustrativo): la "rejilla" de modelos (masa M y edad relativa tau) usa las frecuencias asintoticas
nu_{n,l} = Delta nu (n + l/2 + eps) - l(l+1) D0 con Delta nu = 135,1 sqrt(M) R^-3/2 uHz (valor solar de referencia ADOPTADO, no consultado), R = M^0,8 (1 + 0,3 tau), D0 = 1,5 (1 - 0,7 tau) uHz,
eps = 1,4. La "estrella observada" es el modelo de M = 1,05 y tau = 0,45 con un desplazamiento de superficie a (nu/nu_max)^4 con a = -2,0 uHz y ruido de 0,3 uHz (semilla 20261109).
La forma de ley de potencias del efecto de superficie es la de uso habitual en la literatura, no consultada para esta clase; aqui el exponente se supone conocido (b = 4).
Modelo: chi^2(M, tau) = sum ((obs - mod - a (nu/nu_max)^b)/sigma)^2 con a resuelto analiticamente en cada punto de la rejilla (minimos cuadrados lineales); se compara con el ajuste sin correccion.
Rejilla gruesa de 61 x 101 puntos, refinada localmente (41 x 41 puntos de 0,0005 en M y 0,001 en tau); incertidumbres por perfil de chi^2 (Delta chi^2 = 1); sesgo con y sin correccion en 30 realizaciones de ruido.
Supuestos: sigma conocida e independiente, exponente b conocido, modelos asintoticos (sin modos mixtos). Validez: orientativa.
Tolerancia: con correccion el ajuste recupera (M, tau) dentro de 3 sigma y chi^2 reducido entre 0,5 y 1,8; sin correccion el chi^2 reducido supera 10; a recuperada dentro de 3 sigma.
"""
from __future__ import annotations
import math, platform, random, sys

SIG = 0.3
EPS = 1.4
B = 4.0
LS = (0, 1, 2)
NS = range(16, 28)


def dnu(M, tau):
    R = M**0.8 * (1 + 0.3 * tau)
    return 135.1 * math.sqrt(M) * R**-1.5, R


def modelo(M, tau):
    d, R = dnu(M, tau)
    D0 = 1.5 * (1 - 0.7 * tau)
    numax = 3090.0 * M * R**-2
    return [(n, l, d * (n + l / 2 + EPS) - l * (l + 1) * D0) for l in LS for n in NS], numax


def chi2_punto(obs, M, tau, superficie):
    mod, numax = modelo(M, tau)
    r = [o - m[2] for o, m in zip(obs, mod)]
    if not superficie:
        return sum((x / SIG) ** 2 for x in r), 0.0
    f = [(m[2] / numax) ** B for m in mod]
    a = sum(x * g for x, g in zip(r, f)) / sum(g * g for g in f)
    return sum(((x - a * g) / SIG) ** 2 for x, g in zip(r, f)), a


def rejilla():
    Ms = [0.90 + 0.005 * i for i in range(61)]
    ts = [0.01 * j for j in range(101)]
    return Ms, ts


def mejor(obs, superficie):
    Ms, ts = rejilla()
    best = (1e300, None, None, 0.0)
    tabla = {}
    for M in Ms:
        for t in ts:
            c, a = chi2_punto(obs, M, t, superficie)
            tabla[(M, t)] = c
            if c < best[0]:
                best = (c, M, t, a)
    return best, tabla


def intervalo(tabla, eje, c_min):
    # perfil: minimo de chi^2 sobre el otro parametro; Delta chi^2 = 1
    perfil = {}
    for (M, t), c in tabla.items():
        k = M if eje == 0 else t
        perfil[k] = min(perfil.get(k, 1e300), c)
    ok = [k for k, c in perfil.items() if c <= c_min + 1.0]
    return min(ok), max(ok)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    Mt, tt, at = 1.05, 0.45, -2.0
    mod, numax = modelo(Mt, tt)
    obs = [m[2] + at * (m[2] / numax) ** B + rng.gauss(0, SIG) for m in mod]
    npar = 3
    ndat = len(obs)
    print(f"{ndat} frecuencias (l = 0, 1, 2; n = {NS.start}..{NS.stop - 1}); numax del modelo verdadero = {numax:.1f} uHz")
    (c1, M1, t1, a1), tab1 = mejor(obs, True)
    (c0, M0, t0, a0), tab0 = mejor(obs, False)
    red1 = c1 / (ndat - npar)
    red0 = c0 / (ndat - 2)
    tabf = {}
    for i in range(-20, 21):
        for j in range(-20, 21):
            M, t = M1 + 0.0005 * i, t1 + 0.001 * j
            tabf[(M, t)] = chi2_punto(obs, M, t, True)[0]
    cf = min(tabf.values())
    lo1, hi1 = intervalo(tabf, 0, cf)
    tl1, th1 = intervalo(tabf, 1, cf)
    M1, t1 = min(tabf, key=tabf.get)
    c1 = cf
    a1 = chi2_punto(obs, M1, t1, True)[1]
    red1 = c1 / (ndat - npar)
    print(f"con superficie: M = {M1:.3f} [{lo1:.3f}, {hi1:.3f}] ; tau = {t1:.2f} [{tl1:.2f}, {th1:.2f}] ; a = {a1:.3f} uHz ; chi2 = {c1:.1f} ; chi2 reducido = {red1:.2f}")
    print(f"sin superficie: M = {M0:.3f} ; tau = {t0:.2f} ; chi2 = {c0:.1f} ; chi2 reducido = {red0:.1f}")
    print(f"verdadero: M = {Mt} ; tau = {tt} ; a = {at}")
    sM, st = (hi1 - lo1) / 2, (th1 - tl1) / 2
    assert abs(M1 - Mt) < 3 * max(sM, 0.005) and abs(t1 - tt) < 3 * max(st, 0.01)
    assert 0.5 < red1 < 1.8 and red0 > 10
    # a por el ajuste lineal frente a su error: sigma_a = SIG / sqrt(sum f^2)
    f = [(m[2] / modelo(M1, t1)[1]) ** B for m in modelo(M1, t1)[0]]
    sa = SIG / math.sqrt(sum(g * g for g in f))
    print(f"a = {a1:.3f} +/- {sa:.3f} uHz (verdadero {at})")
    assert abs(a1 - at) < 3 * sa
    # Monte Carlo del sesgo con y sin superficie (30 realizaciones, rejilla gruesa en torno al optimo)
    errs1, errs0 = [], []
    for _ in range(30):
        o = [m[2] + at * (m[2] / numax) ** B + rng.gauss(0, SIG) for m in mod]
        bests = {}
        for sup in (True, False):
            b = (1e300, None, None)
            for i in range(31):
                M = 1.02 + 0.002 * i
                for j in range(31):
                    t = 0.375 + 0.005 * j
                    c, _ = chi2_punto(o, M, t, sup)
                    if c < b[0]:
                        b = (c, M, t)
            bests[sup] = b
        errs1.append(bests[True][1] - Mt)
        errs0.append(bests[False][1] - Mt)
    m1, m0 = sum(errs1) / 30, sum(errs0) / 30
    print(f"sesgo medio en M (30 realizaciones): con superficie = {m1:+.4f} ; sin superficie = {m0:+.4f}")
    assert abs(m0) > abs(m1)
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
