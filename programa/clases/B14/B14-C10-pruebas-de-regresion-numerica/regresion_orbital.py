#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C10: pruebas de regresión numérica con tolerancias justificadas.

Datos: GM de la Tierra = 3.986004e14 m3/s2 (valor nominal de la documentación
de astropy.constants) y radio ecuatorial 6378.137 km (NASA NSSDC Earth Fact
Sheet 2024). La órbita (circular a 400 km de altitud) es SINTÉTICA.
Modelo: período analítico T = 2*pi*sqrt(a^3/GM) y, con scipy.integrate
.solve_ivp (DOP853, rtol=1e-12, atol=1e-9), el error de cierre de la órbita
tras un período y la deriva de energía específica.
Un "valor de referencia" (golden) se guarda en un archivo JSON y las
versiones posteriores se comparan con numpy.testing.assert_allclose
(criterio |actual - desired| <= atol + rtol*|desired|).
Supuestos: dos cuerpos, sin perturbaciones.
Validez: demostración de la técnica de regresión; los valores de cierre y
deriva dependen de las versiones de SciPy y NumPy impresas.
Tolerancia: período con rtol=1e-9 (variaciones inocuas pasan); error de
cierre con atol=1e-3 m; el error de GM de 1e-6 relativo DEBE ser detectado
con rtol=1e-7 y NO con rtol=1e-3.
"""
from __future__ import annotations
import json, math, os, platform, sys, tempfile
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from numpy.testing import assert_allclose

GM = 3.986004e14
R_T = 6378.137e3


def periodo(a, gm):
    return 2.0 * math.pi * math.sqrt(a**3 / gm)


def periodo_reordenado(a, gm):
    """Misma fórmula escrita de otro modo: cambio inocuo de redondeo."""
    return 2.0 * math.pi * a**1.5 / math.sqrt(gm)


def cierre_y_energia(a, gm):
    v = math.sqrt(gm / a)
    T = periodo(a, gm)

    def f(t, y):
        r3 = (y[0] ** 2 + y[1] ** 2) ** 1.5
        return [y[2], y[3], -gm * y[0] / r3, -gm * y[1] / r3]

    y0 = [a, 0.0, 0.0, v]
    sol = solve_ivp(f, (0, T), y0, method="DOP853", rtol=1e-12, atol=1e-9)
    yf = sol.y[:, -1]
    cierre = math.hypot(yf[0] - a, yf[1])
    e = lambda y: 0.5 * (y[2] ** 2 + y[3] ** 2) - gm / math.hypot(y[0], y[1])
    return cierre, abs(e(yf) - e(y0)) / abs(e(y0))


def pasa(actual, desired, rtol=0.0, atol=0.0):
    try:
        assert_allclose(actual, desired, rtol=rtol, atol=atol)
        return True
    except AssertionError:
        return False


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  SciPy {scipy.__version__}")
    a = R_T + 400e3
    T0 = periodo(a, GM)
    cierre0, deriva0 = cierre_y_energia(a, GM)

    with tempfile.TemporaryDirectory() as td:
        ruta = os.path.join(td, "referencia.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump({"periodo_s": T0, "cierre_m": cierre0, "deriva_energia": deriva0,
                       "version_scipy": scipy.__version__, "nota": "valor de referencia sintético"}, f)
        with open(ruta, encoding="utf-8") as f:
            ref = json.load(f)
    print(f"referencia guardada: T = {ref['periodo_s']:.9f} s; cierre = {ref['cierre_m']:.3e} m; deriva = {ref['deriva_energia']:.2e}")
    prueba(ref["periodo_s"] == T0, "ida y vuelta de JSON exacta")

    # 1) cambio inocuo de redondeo: debe pasar con rtol=1e-9 y puede no ser idéntico bit a bit
    T1 = periodo_reordenado(a, GM)
    dif = abs(T1 - T0) / T0
    print(f"reescritura inocua: diferencia relativa = {dif:.2e}; idéntico bit a bit: {T1 == T0}")
    prueba(pasa(T1, ref["periodo_s"], rtol=1e-9), "variación inocua debe pasar con rtol=1e-9")

    # 2) error real: GM con un dígito cambiado (1e-6 relativo)
    GM_mal = 3.986008e14
    T2 = periodo(a, GM_mal)
    dif2 = abs(T2 - T0) / T0
    print(f"GM erróneo (3.986008e14): diferencia relativa en T = {dif2:.2e}")
    prueba(not pasa(T2, ref["periodo_s"], rtol=1e-7), "con rtol=1e-7 el error debe detectarse")
    prueba(pasa(T2, ref["periodo_s"], rtol=1e-3), "con rtol=1e-3 el error pasa sin ser visto")
    print("rtol=1e-7: detectado;  rtol=1e-3: NO detectado (tolerancia demasiado floja)")

    # 3) la tolerancia sobre el cierre debe ser absoluta (la referencia es ~1e-5, casi 0)
    cierre1, deriva1 = cierre_y_energia(a, GM)
    print(f"repetición: cierre = {cierre1:.3e} m; deriva = {deriva1:.2e}")
    prueba(pasa(cierre1, ref["cierre_m"], atol=1e-3), "cierre con atol=1e-3 m")
    prueba(not pasa(1e-3 * 5, ref["cierre_m"], rtol=1e-6), "una tolerancia solo relativa sobre un valor casi 0 es injusta")
    prueba(deriva1 < 1e-10, "deriva de energía por debajo de 1e-10")

    # 4) asimetría de assert_allclose
    print(f"asimetría: (1.0 vs 1.102, rtol=0.1) pasa = {pasa(1.0, 1.102, rtol=0.1)}; "
          f"(1.102 vs 1.0, rtol=0.1) pasa = {pasa(1.102, 1.0, rtol=0.1)}")
    prueba(pasa(1.0, 1.102, rtol=0.1) and not pasa(1.102, 1.0, rtol=0.1), "asimetría documentada")

    # 5) el orden de suma cambia el último dígito
    rng = np.random.default_rng(20261105)
    x = rng.normal(1.0, 0.01, 100_000)
    def secuencial(v):                                  # acumulación simple (sin compensar)
        s = 0.0
        for t in v:
            s += t
        return s
    s1 = secuencial(x.tolist())                         # orden original
    s2 = secuencial(x[rng.permutation(x.size)].tolist())  # otro orden
    print(f"suma en dos órdenes: diferencia relativa = {abs(s1 - s2) / s1:.2e}; idéntico bit a bit: {s1 == s2}")
    prueba(s1 != s2 and abs(s1 - s2) / s1 < 1e-12, "reordenar cambia el redondeo, y solo eso")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
