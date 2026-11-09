#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C13: parametros de Stokes, rotacion de Faraday y sintesis de RM (semilla fija).

Datos: e, m_e, epsilon_0, c de NIST CODATA 2022 (consultada 2026-11-09). La definicion RM de la rotacion (beta = RM lambda^2) se consulto en
Wikipedia (Rotation measure) el 2026-11-09. La fuente (RM = +60 rad/m^2, p = 0,3, angulo intrinseco 30 grados), el ruido y los canales son SINTETICOS
(semilla 20261109).
Modelo: P(lambda^2) = p exp(2i(chi0 + RM lambda^2)); Q = Re P, U = Im P. Coeficiente RM = e^3/(8 pi^2 eps0 m^2 c^3) (SI) convertido a 0,812 rad/m^2 por
cm^-3 microgauss pc. Sintesis de RM: F(phi) = (1/N) suma P exp(-2i phi lambda^2). Ajuste directo del angulo con desenrollado (dos vias).
Supuestos: una sola componente de Faraday, pantalla delgada. Validez: orientativa.
Tolerancia: RM recuperado dentro de 1 rad/m^2 por ambas vias; coeficiente 0,812 dentro del 0,2 %.
"""
from __future__ import annotations
import cmath, math, platform, random
E, ME, EPS0, C = 1.602176634e-19, 9.1093837139e-31, 8.8541878188e-12, 299792458.0
PC = 3.0856775814913673e16

def coef():
    k = E ** 3 / (8 * math.pi ** 2 * EPS0 * ME ** 2 * C ** 3)       # rad m^-2 por (m^-3 T m)
    return k * 1e6 * 1e-10 * PC                                       # cm^-3, microgauss (1e-10 T), pc

def calc():
    rng = random.Random(20261109)
    RM0, p0, chi0 = 60.0, 0.3, math.radians(30.0)
    nu = [1.1e9 + i * 0.05e9 for i in range(24)]
    l2 = [(C / v) ** 2 for v in nu]
    sg = 0.01
    P = [p0 * cmath.exp(2j * (chi0 + RM0 * x)) + complex(rng.gauss(0, sg), rng.gauss(0, sg)) for x in l2]
    # sintesis
    fis = [i * 0.5 - 300 for i in range(1201)]
    mean_l2 = sum(l2) / len(l2)
    F = [abs(sum(Pi * cmath.exp(-2j * f * (x - mean_l2)) for Pi, x in zip(P, l2)) / len(P)) for f in fis]
    kmax = max(range(len(F)), key=lambda k: F[k])
    # ajuste directo del angulo con desenrollado en lambda^2 ascendente
    orden = sorted(range(len(l2)), key=lambda i: l2[i])
    ang = [0.5 * cmath.phase(P[i]) for i in orden]
    xs = [l2[i] for i in orden]
    un, prev = [], None
    for a in ang:
        if prev is not None:
            while a - prev > math.pi / 2:
                a -= math.pi
            while a - prev < -math.pi / 2:
                a += math.pi
        un.append(a)
        prev = a
    mx, my = sum(xs) / len(xs), sum(un) / len(un)
    RM_fit = sum((x - mx) * (y - my) for x, y in zip(xs, un)) / sum((x - mx) ** 2 for x in xs)
    # sesgo de la polarizacion lineal con baja S/N
    sesgo = []
    for snr in (1.0, 3.0, 10.0):
        v = []
        for _ in range(4000):
            q = snr + rng.gauss(0, 1)
            u = rng.gauss(0, 1)
            v.append(math.hypot(q, u))
        sesgo.append((snr, sum(v) / len(v)))
    # ancho de la funcion de transferencia RMSF
    dl2 = max(l2) - min(l2)
    return dict(coef=coef(), RM_synth=fis[kmax], RM_fit=RM_fit, Fpk=F[kmax], rmsf=2 * math.sqrt(3) / dl2, sesgo=sesgo, RM0=RM0,
                p_est=F[kmax], Q0=P[0].real, U0=P[0].imag)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"coeficiente RM = {r['coef']:.4f} rad m^-2 por (cm^-3 microgauss pc)")
    print(f"RM verdadero = {r['RM0']:.1f} ; sintesis de RM: pico en {r['RM_synth']:.1f} rad/m^2 (amplitud {r['Fpk']:.3f}) ; ajuste del angulo: {r['RM_fit']:.2f} rad/m^2")
    print(f"anchura de la RMSF = {r['rmsf']:.1f} rad/m^2")
    print(f"{'S/N verdadera':>13} {'media de sqrt(Q^2+U^2)':>23}")
    for s, m in r["sesgo"]:
        print(f"{s:13.1f} {m:23.3f}")
    assert abs(r["coef"] / 0.812 - 1) < 2e-3
    assert abs(r["RM_synth"] - 60) < 1.0 and abs(r["RM_fit"] - 60) < 1.0
    assert abs(r["Fpk"] - 0.3) < 0.02
    assert r["sesgo"][0][1] > 1.2 and abs(r["sesgo"][2][1] - 10) < 0.2
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
