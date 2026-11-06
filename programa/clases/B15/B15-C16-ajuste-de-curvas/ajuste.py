#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C16: mínimos cuadrados lineales y no lineales.

Datos: (a) NIST StRD, conjunto Misra1a (datos REALES de investigación dental,
adsorción monomolecular; 14 observaciones; modelo y = b1 (1 - exp(-b2 x)))
con los valores CERTIFICADOS del NIST como referencia independiente;
(b) SINTÉTICOS (semilla fija): serie de la clase B15-C01 con tendencia y una
oscilación, ajustada de forma conjunta (modelo lineal en los parámetros).
Referencias: valores certificados de b1, b2, sus desviaciones, suma de
cuadrados residual y desviación residual (NIST StRD Misra1a); solución exacta
de una recta con ruido nulo.
Supuestos: ruido independiente de varianza constante.
Tolerancias: 1e-6 relativa a los valores certificados (parámetros),
1e-4 en las desviaciones; 1e-10 en la recta exacta.
"""
import platform
import sys

import numpy as np
import scipy
from scipy.optimize import curve_fit


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "|", platform.system())

# (1) Recta exacta
x = np.arange(10.0)
A = np.vstack([np.ones_like(x), x]).T
c, *_ = np.linalg.lstsq(A, 3.0 - 0.5 * x, rcond=None)
print(f"(1) recta sin ruido: {c[0]:.12f} + {c[1]:.12f} x (real 3 y -0.5)")
prueba(np.allclose(c, [3.0, -0.5], atol=1e-10), "recta exacta")

# (2) NIST StRD Misra1a
y = np.array([10.07, 14.73, 17.94, 23.93, 29.61, 35.18, 40.02, 44.82, 50.76, 55.05, 61.01, 66.40, 75.47, 81.78])
xm = np.array([77.6, 114.9, 141.1, 190.8, 239.9, 289.0, 332.8, 378.4, 434.8, 477.3, 536.8, 593.1, 689.1, 760.0])
cert = dict(b1=2.3894212918e2, b2=5.5015643181e-4, sb1=2.7070075241e0, sb2=7.2668688436e-6,
            rss=1.2455138894e-1, sres=1.0187876330e-1)


def modelo(x, b1, b2):
    return b1 * (1 - np.exp(-b2 * x))


def modelo_esc(x, b1, c2):          # b2 = c2 * 1e-4: parámetros de magnitud parecida
    return modelo(x, b1, c2 * 1e-4)


def ajustar(x, y, p0):
    p, cov = curve_fit(modelo_esc, x, y, p0=[p0[0], p0[1] * 1e4], maxfev=5000)
    return np.array([p[0], p[1] * 1e-4]), cov * np.outer([1, 1e-4], [1, 1e-4])


for nombre, p0 in (("inicio 1 (500, 1e-4)", [500, 1e-4]), ("inicio 2 (250, 5e-4)", [250, 5e-4])):
    p, cov = ajustar(xm, y, p0)
    r = y - modelo(xm, *p)
    rss = float(r @ r)
    sres = np.sqrt(rss / (len(y) - 2))
    sd = np.sqrt(np.diag(cov))
    print(f"(2) Misra1a, {nombre}: b1 = {p[0]:.8f} (cert. {cert['b1']:.8f}); b2 = {p[1]:.10e} (cert. {cert['b2']:.10e})")
    print(f"    sd(b1) = {sd[0]:.7f} (cert. {cert['sb1']:.7f}); sd(b2) = {sd[1]:.6e} (cert. {cert['sb2']:.6e}); "
          f"RSS = {rss:.8f} (cert. {cert['rss']:.8f}); s = {sres:.8f} (cert. {cert['sres']:.8f})")
    prueba(abs(p[0] / cert["b1"] - 1) < 1e-6 and abs(p[1] / cert["b2"] - 1) < 1e-6, "parámetros certificados")
    prueba(abs(sd[0] / cert["sb1"] - 1) < 1e-4 and abs(sd[1] / cert["sb2"] - 1) < 1e-4, "desviaciones certificadas")
    prueba(abs(rss / cert["rss"] - 1) < 1e-6, "suma de cuadrados certificada")
print(f"    residuos (unidades de volumen del conjunto): mín {r.min():+.3f}, máx {r.max():+.3f}; correlación de signos consecutivos: "
      f"{int(np.sum(np.sign(r[1:]) == np.sign(r[:-1])))} de {len(r)-1} pares con el mismo signo")

# (3) Cobertura de las incertidumbres (Monte Carlo con el modelo certificado)
rng = np.random.default_rng(15016)
pc = np.array([cert["b1"], cert["b2"]])
cubre = np.zeros(2)
R = 1000
for _ in range(R):
    yy = modelo(xm, *pc) + cert["sres"] * rng.standard_normal(len(xm))
    p, cov = ajustar(xm, yy, [250, 5e-4])
    cubre += np.abs(p - pc) < np.sqrt(np.diag(cov))
print(f"(3) cobertura de ±1 sd en {R} simulaciones: b1 {cubre[0]/R:.3f}, b2 {cubre[1]/R:.3f} (teoría 0.683 para modelo lineal; "
      f"menor o mayor en modelos no lineales con N = 14)")
prueba(all(0.60 < cubre / R) and all(cubre / R < 0.76), "cobertura cercana a 68 %")

# (4) Ajuste conjunto de tendencia y oscilación (serie de B15-C01)
rng = np.random.default_rng(15001)
n = 7 * 720
td = np.arange(n) * 120.0 / 86400.0
xs = 1 + 2e-3 * np.sin(2 * np.pi * td / 2.5) - 1e-4 * td + 5e-4 * rng.standard_normal(n)
ok = ~((td >= 3.0) & (td < 3.5))
t_, x_ = td[ok], xs[ok]
rec = np.polyfit(t_, x_, 1)[0]
Aj = np.vstack([np.ones_like(t_), t_, np.sin(2 * np.pi * t_ / 2.5), np.cos(2 * np.pi * t_ / 2.5)]).T
co, *_ = np.linalg.lstsq(Aj, x_, rcond=None)
res = x_ - Aj @ co
s2 = res @ res / (len(x_) - 4)
cov = s2 * np.linalg.inv(Aj.T @ Aj)
sd = np.sqrt(np.diag(cov))
print(f"(4) pendiente: solo recta {rec*1e4:+.3f}e-4/d; ajuste conjunto {co[1]*1e4:+.3f}e-4 ± {sd[1]*1e4:.3f}e-4 (real -1.000e-4); "
      f"amplitud {np.hypot(co[2], co[3])*1e3:.3f}e-3 (real 2.000e-3); desviación residual {np.sqrt(s2)*1e4:.3f}e-4 (real 5.0e-4)")
prueba(abs(co[1] + 1e-4) < 3 * sd[1] and abs(rec + 1e-4) > 5 * sd[1], "el ajuste conjunto recupera la tendencia")
print("Pruebas superadas.")
