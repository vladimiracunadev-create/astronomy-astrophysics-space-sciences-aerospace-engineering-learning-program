#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B61-C06: edad de modelo por conteo de craters, con craters SINTETICOS.

Datos: coeficientes de la funcion de produccion lunar (polinomio en log10 D, D en km) y de la cronologia
  N1(T) = Cexp (exp(T/tau) - 1) + Clin T  (T en Ga, N1 en km^-2: craters con D > 1 km), con Cexp = 5.44e-14,
  tau = 1/6.93 Ga, Clin = 10**a0 = 8.17e-4. Se leyeron en el codigo fuente del paquete cratermaker (documentacion
  en linea, consultada el 2026-11-09), que cita a Neukum et al. (2001) / Ivanov et al. (2001); el articulo original
  NO se leyo y el propio codigo anota una errata en el termino lineal del articulo (8.38e-4 impreso).
  Es una fuente secundaria: los valores se usan como INSUMO ILUSTRATIVO de la forma funcional.
  Normalizacion del laboratorio (supuesto propio): N(>D, T) = N1(T) * 10**(P(log10 D) - a0), de modo que N(>1 km) = N1.
Craters observados: NO hay observaciones; se generan SINTETICAMENTE desde la propia funcion (edad verdadera conocida,
  semilla 20261109), de modo que el ajuste solo comprueba el metodo, nunca una superficie real.
Metodo: maxima verosimilitud de Poisson sobre el conteo acumulado N(>=Dmin) en un area A, edad invertida por biseccion
  de la cronologia; incertidumbre 1-sigma por la raiz del conteo propagada (delta T = T * sqrt(N)/N / elasticidad).
Tolerancias: monotonia de la funcion de produccion; N(>1 km) = N1 a 1e-12; cobertura del intervalo 1-sigma 0.55-0.80 en 400 simulaciones.
Limites: sin saturacion, resurfacing, craters secundarios, ni degradacion; solo el rango D = 0.1-100 km del polinomio.
"""
from __future__ import annotations
import math, platform, random

A_COEF = [-3.0876, -3.557528, 0.781027, 1.021521, -0.156012, -0.444058, 0.019977, 0.086850, -0.005874, -0.006809, 8.25e-4, 5.54e-5]
CEXP, TAU = 5.44e-14, 1 / 6.93
CLIN = 10 ** A_COEF[0]


def log_p(D_km):
    x = math.log10(D_km)
    return sum(a * x**j for j, a in enumerate(A_COEF))


def n1(T):
    return CEXP * (math.exp(T / TAU) - 1) + CLIN * T


def n_acum(D_km, T):
    return n1(T) * 10 ** (log_p(D_km) - A_COEF[0])


def edad_desde_n1(N1):
    lo, hi = 0.0, 4.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if n1(mid) < N1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def poisson(rng, lam):
    if lam > 500:
        return max(0, int(round(rng.gauss(lam, math.sqrt(lam)))))
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def muestrear_D(rng, dmin, dmax, T, n):
    """Inversa de la acumulada normalizada en [dmin, dmax] por biseccion en log10 D."""
    f0, f1 = n_acum(dmin, T), n_acum(dmax, T)
    out = []
    for _ in range(n):
        u = rng.random()
        objetivo = f0 - u * (f0 - f1)
        lo, hi = math.log10(dmin), math.log10(dmax)
        for _ in range(60):
            mid = (lo + hi) / 2
            if n_acum(10**mid, T) > objetivo:
                lo = mid
            else:
                hi = mid
        out.append(10 ** ((lo + hi) / 2))
    return out


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Funcion de produccion (coeficientes de fuente SECUNDARIA; craters de los ensayos SINTETICOS)")
    ds = [0.1 * 1.25**k for k in range(0, 31)]
    ds = [d for d in ds if d <= 100]
    vals = [log_p(d) for d in ds]
    assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
    print(f"log10 N(>D) decrece de {vals[0]:.3f} (D={ds[0]:.2f} km) a {vals[-1]:.3f} (D={ds[-1]:.1f} km): monotona")
    assert abs(n_acum(1.0, 3.0) - n1(3.0)) < 1e-12
    print("Cronologia N1(T) [km^-2, D>1 km]:")
    for T in (0.5, 1.0, 2.0, 3.0, 3.5, 3.9):
        print(f"  T={T:.1f} Ga  N1={n1(T):.4e}  N(>0.5 km)={n_acum(0.5,T):.4e}  N(>10 km)={n_acum(10,T):.4e}")
    print(f"Razon N1(3.5)/N1(1.0) = {n1(3.5)/n1(1.0):.2f}  (la tasa NO es constante; decae hacia el presente)")
    # ensayo unico
    rng = random.Random(20261109)
    Tv, A, Dmin = 3.2, 5000.0, 0.5
    lam = n_acum(Dmin, Tv) * A
    n = poisson(rng, lam)
    D = muestrear_D(rng, Dmin, 100.0, Tv, n)
    N1_est = len(D) / A / (n_acum(Dmin, 1.0) / n1(1.0))
    Test = edad_desde_n1(N1_est)
    sig = Test / 1 * (1 / math.sqrt(len(D))) * (n1(Test) / (Test * (CEXP * math.exp(Test / TAU) / TAU + CLIN)))
    print(f"Ensayo unico (SINTETICO): T_verdadera={Tv} Ga, area={A:.0f} km2, D>={Dmin} km, esperados={lam:.1f}, observados={len(D)}")
    print(f"  Edad de modelo = {Test:.3f} +- {sig:.3f} Ga (1 sigma Poisson) ; dif. con la verdadera = {Test-Tv:+.3f} Ga")
    print(f"  D maximo del ensayo = {max(D):.1f} km")
    # cobertura
    hit, errs, N_tr = 0, [], 400
    for _ in range(N_tr):
        lam = n_acum(Dmin, Tv) * A
        k = poisson(rng, lam)
        if k < 5:
            continue
        N1e = k / A / (n_acum(Dmin, 1.0) / n1(1.0))
        Te = edad_desde_n1(N1e)
        s = Te * (1 / math.sqrt(k)) * (n1(Te) / (Te * (CEXP * math.exp(Te / TAU) / TAU + CLIN)))
        errs.append(Te - Tv)
        if abs(Te - Tv) <= s:
            hit += 1
    cov = hit / len(errs)
    media = sum(errs) / len(errs)
    print(f"Cobertura del intervalo 1-sigma en {len(errs)} ensayos sinteticos = {cov:.3f} (esperado ~0.68) ; sesgo medio = {media:+.4f} Ga")
    assert 0.55 < cov < 0.80
    # efecto del area
    print("Incertidumbre relativa de la edad frente al area (T=3.2 Ga, D>=0.5 km):")
    for a in (500.0, 5000.0, 50000.0):
        k = n_acum(Dmin, Tv) * a
        print(f"  A={a:8.0f} km2  N esperado={k:8.1f}  1/sqrt(N)={1/math.sqrt(k):.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
