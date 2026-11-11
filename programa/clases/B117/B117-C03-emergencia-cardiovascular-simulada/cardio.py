#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B117-C03: emergencia cardiovascular SIMULADA con un modelo concentrado (gasto, presion, indice de shock, paro).

CONTENIDO EDUCATIVO: no es un criterio diagnostico ni consejo medico; no sustituye formacion ni supervision profesional.
Datos consultados (2026-11-10): ninguno numerico. El resumen del Integrated Medical Model de la NASA (NTRS 20140016998) describe que modela
la probabilidad de eventos medicos en mision; no aporta parametros fisiologicos usados aqui. Las relaciones (GC = FC x VS; PAM = GC x RVS + PVC;
Windkessel de dos elementos; indice de shock = FC / PAS) son relaciones fisiologicas estandar NO consultadas en una fuente concreta.
ILUSTRATIVOS (sinteticos, no medidos): FC = 70 lpm, VS = 70 mL, RVS = 18 mmHg min/L, PVC = 4 mmHg, compliance arterial C = 1.5 mL/mmHg,
presion media de llenado circulatorio Pmcf = 7 mmHg, fraccion de gasto durante compresiones 0.25, umbral de alerta del indice de shock 0.9,
dispersion basal 8 lpm y 8 mL (normal, semilla fija). Presiones en mmHg, flujos en L/min, tiempo en s.
Modelo de paro: C dP/dt = -(P - Pmcf)/R con R en mmHg s/mL (R = RVS x 0.06). Sin reflejos, sin presion venosa dinamica.
Tolerancias: Euler (dt = 1e-5 s) frente a analitico < 1e-3 mmHg; recuperacion de RVS a partir de la PAM < 1e-9 relativa.
"""
from __future__ import annotations
import math, platform, random

FC0, VS0, RVS, PVC, COMP, PMCF = 70.0, 70.0, 18.0, 4.0, 1.5, 7.0
FRAC_CPR, UMBRAL_SI = 0.25, 0.9


def gasto(fc, vs):             # L/min
    return fc * vs / 1000.0


def pam(gc, rvs=RVS, pvc=PVC):  # mmHg
    return gc * rvs + pvc


def presiones(fc, vs):
    gc = gasto(fc, vs)
    m = pam(gc)
    pp = vs / COMP
    dbp = m - pp / 3.0
    sbp = dbp + pp
    return gc, m, sbp, dbp


def indice_shock(fc, sbp):
    return fc / sbp


def decaimiento_analitico(t, p0):
    tau = RVS * 0.06 * COMP
    return PMCF + (p0 - PMCF) * math.exp(-t / tau)


def decaimiento_euler(t_fin, p0, dt=1e-5):
    r = RVS * 0.06
    p = p0
    for _ in range(int(round(t_fin / dt))):
        p += dt * (-(p - PMCF) / (r * COMP))
    return p


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Escenarios SINTETICOS con parametros ILUSTRATIVOS; sin datos fisiologicos consultados.")
    esc = {"basal": (70, 70), "hemorragia": (120, 40), "taquiarritmia": (160, 35), "bradicardia": (35, 80)}
    print(" escenario        FC   VS[mL]  GC[L/min]  PAM[mmHg]  PAS   PAD    IS    alerta")
    res = {}
    for nom, (fc, vs) in esc.items():
        gc, m, s, d = presiones(fc, vs)
        si = indice_shock(fc, s)
        res[nom] = (gc, m, s, si)
        print(f"{nom:14s} {fc:5.0f} {vs:7.0f} {gc:10.2f} {m:10.1f} {s:6.1f} {d:5.1f} {si:6.2f}  {'si' if si > UMBRAL_SI else 'no'}")
    # paro cardiaco
    p0 = res["basal"][1]
    tau = RVS * 0.06 * COMP
    t40 = tau * math.log((p0 - PMCF) / (40.0 - PMCF))
    print(f"Paro: tau = R C = {tau:.3f} s ; P(0) = {p0:.1f} mmHg ; tiempo hasta 40 mmHg = {t40:.2f} s ; P(10 s) = {decaimiento_analitico(10, p0):.2f} mmHg")
    err = max(abs(decaimiento_euler(t, p0) - decaimiento_analitico(t, p0)) for t in (1.0, 3.0))
    print(f"Error maximo Euler - analitico = {err:.2e} mmHg")
    gc_cpr = FRAC_CPR * gasto(FC0, VS0)
    print(f"Compresiones simuladas (fraccion {FRAC_CPR}): GC = {gc_cpr:.3f} L/min ; PAM estacionaria = {pam(gc_cpr):.1f} mmHg")
    # verificacion de la relacion PAM = GC RVS + PVC
    rvs_rec = (res["basal"][1] - PVC) / res["basal"][0]
    print(f"RVS recuperada desde la PAM basal = {rvs_rec:.6f} mmHg min/L (original {RVS})")
    # barrido de perdida de volumen con dispersion basal
    print("Perdida de volumen sintetica: VS = 70 (1 - f) mL, FC = 70 + 100 f lpm; 1000 tripulantes sinteticos (semilla 117)")
    print("  f      IS medio   fraccion con IS > 0.9")
    rng = random.Random(117)
    fr_prev = -1.0
    ok_mono = True
    for f in (0.0, 0.1, 0.2, 0.3, 0.4):
        sis = []
        for _ in range(1000):
            fc = rng.gauss(70, 8) + 100 * f
            vs = rng.gauss(70, 8) * (1 - f)
            _, _, s, _ = presiones(fc, vs)
            sis.append(indice_shock(fc, s))
        fr = sum(1 for x in sis if x > UMBRAL_SI) / len(sis)
        ok_mono = ok_mono and fr >= fr_prev
        fr_prev = fr
        print(f"  {f:.1f}   {sum(sis) / len(sis):8.3f}   {fr:8.3f}")
    assert err < 1e-3
    assert abs(rvs_rec - RVS) / RVS < 1e-9
    assert res["hemorragia"][3] > UMBRAL_SI > res["basal"][3]
    assert ok_mono
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
