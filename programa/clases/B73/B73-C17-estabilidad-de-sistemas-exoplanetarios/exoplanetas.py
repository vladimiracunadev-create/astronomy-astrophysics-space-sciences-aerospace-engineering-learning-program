#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C17: estabilidad de un sistema de dos planetas frente a su separacion en radios de Hill mutuos.

Datos: el SISTEMA es SINTETICO (no es ningun exoplaneta catalogado; el Archivo de Exoplanetas de la NASA no se pudo consultar el 2026-11-10: respondio 503).
Estrella: GM = 132 712 x 10^6 km3/s2 (Sol, NASA/NSSDC, Sun Fact Sheet, 2024-05-09) usado como estrella de ejemplo.
Planetas SINTETICOS: cocientes de masa m1/M = m2/M = 3e-4 (equivalentes a ~0.3 veces la masa de Jupiter si M es el Sol; 'Jupiter/Sol' publicado: GM_J/GM_Sol = 9.55e-4),
orbitas circulares coplanares, a1 = 1 (unidades de longitud), GM_estrella = 1 -> periodo interior 2 pi; fases iniciales 0, 90 y 180 grados (sinteticas).
Modelo: tres masas puntuales newtonianas en el baricentro; leapfrog kick-drift-kick (orden 2, simplectico), 200 pasos por periodo interior; hasta 2000 orbitas interiores.
Separacion: Delta = (a2 - a1) / R_H,mutuo con R_H,mutuo = ((m1+m2)/(3 M))^(1/3) (a1+a2)/2. Criterio de Gladman (1993) para dos planetas en orbitas circulares: Delta > 2 sqrt(3) = 3.46
(NO consultado; se contrasta con las simulaciones). Evento de inestabilidad: separacion planeta-planeta < R_H,mutuo o distancia a la estrella > 3 a2.
Escala ilustrativa: con a1 = 0.1 UA (1 UA = 149.6 x 10^6 km, NASA/NSSDC) alrededor de GM del Sol, el periodo interior es de unos 11.5 d.
Segunda via: (a) conservacion de energia y de momento angular de la integracion; (b) a2 recalculada a partir de Delta debe reproducir Delta.
Tolerancias: energia < 1e-4 y momento angular < 1e-10 (relativo, sistemas estables); tiempo de cruce monotono creciente con Delta (en media sobre fases).
"""
from __future__ import annotations
import json, math, platform, sys

MU = 3e-4  # m/M de cada planeta
K = ((2 * MU) / 3) ** (1 / 3)
PASOS = 200
NORB = 2000
DT = 2 * math.pi / PASOS


def a2_de(delta):
    c = delta * K / 2
    return (1 + c) / (1 - c)


def delta_de(a2):
    return (a2 - 1) / (K * (1 + a2) / 2)


def simular(delta, fase2):
    a2 = a2_de(delta)
    m = [1.0, MU, MU]
    pos, vel = [[0.0, 0.0], [1.0, 0.0], [a2 * math.cos(fase2), a2 * math.sin(fase2)]], [[0.0, 0.0], [0.0, 1.0], [-math.sin(fase2) / math.sqrt(a2), math.cos(fase2) / math.sqrt(a2)]]
    # baricentro
    M = sum(m)
    for arr in (pos, vel):
        cx = sum(m[i] * arr[i][0] for i in range(3)) / M
        cy = sum(m[i] * arr[i][1] for i in range(3)) / M
        for i in range(3):
            arr[i][0] -= cx
            arr[i][1] -= cy

    def acel():
        a = [[0.0, 0.0] for _ in range(3)]
        for i in range(3):
            for j in range(i + 1, 3):
                dx, dy = pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]
                d3 = (dx * dx + dy * dy) ** 1.5
                a[i][0] += m[j] * dx / d3
                a[i][1] += m[j] * dy / d3
                a[j][0] -= m[i] * dx / d3
                a[j][1] -= m[i] * dy / d3
        return a

    def energia():
        e = 0.0
        for i in range(3):
            e += 0.5 * m[i] * (vel[i][0] ** 2 + vel[i][1] ** 2)
            for j in range(i + 1, 3):
                e -= m[i] * m[j] / math.hypot(pos[i][0] - pos[j][0], pos[i][1] - pos[j][1])
        return e

    def L():
        return sum(m[i] * (pos[i][0] * vel[i][1] - pos[i][1] * vel[i][0]) for i in range(3))

    e0, L0 = energia(), L()
    rh = K * (1 + a2) / 2
    a = acel()
    t_cruce = None
    emax = 0.0
    for paso in range(1, NORB * PASOS + 1):
        for i in range(3):
            vel[i][0] += 0.5 * DT * a[i][0]
            vel[i][1] += 0.5 * DT * a[i][1]
            pos[i][0] += DT * vel[i][0]
            pos[i][1] += DT * vel[i][1]
        a = acel()
        for i in range(3):
            vel[i][0] += 0.5 * DT * a[i][0]
            vel[i][1] += 0.5 * DT * a[i][1]
        d12 = math.hypot(pos[1][0] - pos[2][0], pos[1][1] - pos[2][1])
        r2 = math.hypot(pos[2][0] - pos[0][0], pos[2][1] - pos[0][1])
        if d12 < rh or r2 > 3 * a2:
            t_cruce = paso / PASOS
            break
        if paso % 2000 == 0:
            emax = max(emax, abs(energia() / e0 - 1))
    return t_cruce, emax, abs(L() / L0 - 1), a2, rh


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    print(f"m/M = {MU:g} por planeta ; R_H mutuo = {K:.5f} (a1+a2)/2 ; 2 sqrt(3) = {2 * math.sqrt(3):.4f}")
    print(f"Escala ilustrativa: a1 = 0.1 UA -> periodo interior = {2 * math.pi * math.sqrt((0.1 * 149.6e6) ** 3 / 132712e6) / 86400:.2f} d")
    print(" Delta   a2/a1   delta_calc  t_cruce(fase 0)  t_cruce(90)  t_cruce(180)  [orbitas interiores]   dE max (estables)  dL")
    deltas = (2.0, 3.0, 3.5, 4.0, 5.0, 6.0)
    medias = []
    emax_global = 0.0
    Lmax = 0.0
    for d in deltas:
        res = [simular(d, f) for f in (0.0, math.pi / 2, math.pi)]
        a2 = res[0][3]
        ts = [r[0] for r in res]
        txt = "  ".join(f"{(str(round(t, 1)) if t else '>2000'):>12s}" for t in ts)
        estables = [r for r in res if r[0] is None]
        emax = max((r[1] for r in estables), default=float("nan"))
        Lm = max((r[2] for r in estables), default=float("nan"))
        if estables:
            emax_global = max(emax_global, emax)
            Lmax = max(Lmax, Lm)
        eff = [t if t else NORB for t in ts]
        medias.append(sum(eff) / 3)
        print(f" {d:5.1f}  {a2:7.4f}  {delta_de(a2):8.3f}  {txt}      " + (f"{emax:10.2e}  {Lm:9.1e}" if estables else "         -          -"))
        out[f"a2_{int(d * 10)}"] = a2
        out[f"t0_{int(d * 10)}"], out[f"t1_{int(d * 10)}"], out[f"t2_{int(d * 10)}"] = ts
    out.update(emax=emax_global, Lmax=Lmax, K=K, g=2 * math.sqrt(3))
    assert all(medias[i] <= medias[i + 1] + 1e-9 for i in range(len(medias) - 1)), medias
    assert abs(delta_de(a2_de(3.7)) - 3.7) < 1e-12
    assert Lmax < 1e-10 and emax_global < 1e-4
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
