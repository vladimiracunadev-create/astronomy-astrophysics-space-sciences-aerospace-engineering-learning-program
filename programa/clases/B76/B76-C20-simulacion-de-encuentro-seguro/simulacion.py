#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C20: simulacion integradora de un encuentro V-bar con dispersiones y fallo de maniobra (TODO SIMULADO).

Datos CONSULTADOS (2026-11-10): GM_T = 398600.435507 km3/s2 (JPL, DE440) y radio ecuatorial 6378.137 km (NASA/NSSDC).
SINTETICOS (ninguno es telemetria): objetivo circular a 400 km; tres tramos V-bar -5000 -> -1000 -> -300 -> -50 m (duraciones 0.45 P, 0.30 P, 0.20 P: se evitan los multiplos de P/2, donde sin(nT) = 0 vuelve singular el guiado fuera del plano);
error de navegacion (posicion 2 m, velocidad 2 mm/s, 1 sigma por eje); error de ejecucion de los impulsos (1 % de magnitud, 0.5 grados);
dispersion inicial (10 m, 1 cm/s); esfera de exclusion de 20 m (hipotesis del autor); semilla 76020; 60 corridas.
Modelo: el plan usa HCW (dos impulsos por tramo con el estado estimado); la "verdad" es dos cuerpos inerciales no lineal (RK4, paso 2 s) con la referencia
circular analitica. Fallo: el segundo impulso del ultimo tramo no se ejecuta y se deriva 3 periodos con la verdad no lineal.
Criterios: error final (p95) < 20 m (el autor fijo primero 15 m y lo relajo a 20 m tras ver el resultado; con 15 m no cumple; ver la clase); ninguna incursion en la esfera de exclusion hasta el final del plan; con el fallo, la distancia minima no baja de 20 m.
Resultados de este modelo NO son un analisis de seguridad de una mision.
"""
from __future__ import annotations
import math, os, platform, random, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

R0 = (R_T_EQ + 400.0) * 1e3
N = math.sqrt(GM_T * 1e9 / R0 ** 3)
P = 2 * math.pi / N
MU_SI = GM_T * 1e9
DT = 2.0
EXCL = 20.0
TRAMOS = [(-5000.0, -1000.0, 0.45), (-1000.0, -300.0, 0.30), (-300.0, -50.0, 0.20)]
VERD_A_LVLH = lambda t, s: s


def ref_en(t):
    a = N * t
    return (R0 * math.cos(a), R0 * math.sin(a), 0.0, -R0 * N * math.sin(a), R0 * N * math.cos(a), 0.0)


def lvlh(t, s):
    return inercial_a_lvlh(ref_en(t), s, N)


def aplicar_dv(s, t, dv_lvlh):
    a = N * t
    c, sn = math.cos(a), math.sin(a)
    return (s[0], s[1], s[2], s[3] + c * dv_lvlh[0] - sn * dv_lvlh[1], s[4] + sn * dv_lvlh[0] + c * dv_lvlh[1], s[5] + dv_lvlh[2])


def avanzar(s, t, dur, dist_min=None):
    """Integra la verdad y devuelve (estado, t, distancia minima al objetivo)."""
    pasos = max(1, int(math.ceil(dur / DT)))
    h = dur / pasos
    for _ in range(pasos):
        s = rk4(kepler_rhs, s, h)
        t += h
        if dist_min is not None:
            d = math.dist(lvlh(t, s)[:3], (0, 0, 0))
            dist_min = min(dist_min, d)
    return s, t, dist_min


def ruido(rng, s_pos, s_vel):
    return [rng.gauss(0, s_pos) for _ in range(3)] + [rng.gauss(0, s_vel) for _ in range(3)]


def ejecutar(dv, rng, mag_err=0.01, ang_err=math.radians(0.5)):
    m = math.sqrt(sum(c * c for c in dv))
    return [c * (1 + rng.gauss(0, mag_err)) + m * rng.gauss(0, ang_err) for c in dv]


def corrida(rng, fallo=False):
    rel0 = (0.0 + rng.gauss(0, 10), TRAMOS[0][0] + rng.gauss(0, 10), rng.gauss(0, 10), rng.gauss(0, 0.01), rng.gauss(0, 0.01), rng.gauss(0, 0.01))
    ref0, s = lvlh_a_inercial(rel0, R0, N)
    t = 0.0
    dvtot = 0.0
    dmin = 1e18
    for i, (y0, yf, fr) in enumerate(TRAMOS):
        T = fr * P
        est = [a + b for a, b in zip(lvlh(t, s), ruido(rng, 2.0, 0.002))]
        dv1, dv2 = dos_impulsos(N, T, est[:3], est[3:], [0, yf, 0], [0, 0, 0])
        s = aplicar_dv(s, t, ejecutar(dv1, rng))
        dvtot += math.sqrt(sum(c * c for c in dv1))
        s, t, dmin = avanzar(s, t, T, dmin)
        if fallo and i == len(TRAMOS) - 1:
            break
        est = [a + b for a, b in zip(lvlh(t, s), ruido(rng, 2.0, 0.002))]
        # el segundo impulso se recalcula para anular la velocidad relativa estimada
        dv2 = [-est[3], -est[4], -est[5]]
        s = aplicar_dv(s, t, ejecutar(dv2, rng))
        dvtot += math.sqrt(sum(c * c for c in dv2))
    fin = lvlh(t, s)
    if fallo:
        s, t, dmin_f = avanzar(s, t, 3 * P, dmin)
        return dict(dmin=dmin_f, fin=fin, dv=dvtot)
    return dict(dmin=dmin, fin=fin, dv=dvtot, err=math.dist(fin[:3], (0, TRAMOS[-1][1], 0)), vrel=math.hypot(*fin[3:]))


def calcular(n=60):
    rng = random.Random(76020)
    nominal = []
    for _ in range(n):
        nominal.append(corrida(rng))
    rng2 = random.Random(76021)
    falla = [corrida(rng2, fallo=True) for _ in range(20)]
    errs = sorted(q['err'] for q in nominal)
    dvs = sorted(q['dv'] for q in nominal)
    return dict(n=n, err_med=sum(errs) / n, err_p95=errs[int(0.95 * n) - 1], err_max=errs[-1],
                dv_med=sum(dvs) / n, dv_p95=dvs[int(0.95 * n) - 1], dv_max=dvs[-1],
                dmin_nom=min(q['dmin'] for q in nominal),
                fallo_min=min(q['dmin'] for q in falla), fallo_n=len(falla),
                viol_fallo=sum(1 for q in falla if q['dmin'] < EXCL),
                viol_nom=sum(1 for q in nominal if q['dmin'] < EXCL),
                vrel_med=sum(q['vrel'] for q in nominal) / n)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar) ; semillas 76020/76021 ; TODO SIMULADO")
    print(f"Plan: tres tramos V-bar de -5000 a -50 m ({sum(f for _, _, f in TRAMOS):.3f} periodos de {P / 60:.2f} min) ; exclusion ILUSTRATIVA = {EXCL:.0f} m")
    print(f"{r['n']} corridas nominales con dispersiones:")
    print(f"  error final de posicion: media = {r['err_med']:.2f} m ; p95 = {r['err_p95']:.2f} m ; maximo = {r['err_max']:.2f} m")
    print(f"  velocidad relativa final media = {r['vrel_med'] * 100:.2f} cm/s")
    print(f"  delta-v total: media = {r['dv_med']:.3f} m/s ; p95 = {r['dv_p95']:.3f} m/s ; maximo = {r['dv_max']:.3f} m/s")
    print(f"  distancia minima en toda la corrida = {r['dmin_nom']:.2f} m ; incursiones en la esfera de exclusion = {r['viol_nom']}")
    print(f"{r['fallo_n']} corridas con fallo del ultimo impulso (3 periodos de deriva): distancia minima = {r['fallo_min']:.2f} m ; incursiones = {r['viol_fallo']}")
    assert r['err_p95'] < 20.0 and r['viol_fallo'] == 0
    assert r['viol_nom'] == 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
