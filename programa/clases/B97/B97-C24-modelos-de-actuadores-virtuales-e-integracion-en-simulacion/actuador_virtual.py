#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C24: actuador virtual de una articulacion (saturacion, retardo y holgura) dentro de un lazo de control de posicion.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): inercia 2.0 kg m2, ganancias Kp = 50 N m/rad y Kd = 6 N m s/rad, escalon de 0.5 rad,
par maximo 10 N m, retardo de 20 ms, holgura modelada como zona muerta del par de +-1.0 N m, paso de simulacion 1 ms (semi-implicito), 8 s simulados.
Ningun valor corresponde a un motor ni a un reductor real. La 'holgura' es una zona muerta del par transmitido: es una simplificacion, no un modelo de engranajes con juego.
Modelo: J theta'' = tau_efectivo; tau_cmd = Kp (r - theta) - Kd theta'. tau_efectivo = zona_muerta(saturacion(tau_cmd retrasado)).
Segunda via: el caso ideal (sin saturacion, retardo ni holgura) frente a la solucion analitica de segundo orden: wn = sqrt(Kp/J), zeta = Kd/(2 sqrt(Kp J)),
sobreimpulso exp(-pi zeta/sqrt(1 - zeta^2)) y tiempo de pico pi/(wn sqrt(1 - zeta^2)) (tolerancias 1 % y 0.5 %).
Unidades SI y radianes. Una articulacion, sin carga variable ni friccion.
"""
from __future__ import annotations
import collections, math, platform

J, KP, KD, R = 2.0, 50.0, 6.0, 0.5                    # ILUSTRATIVOS
TAU_MAX, RETARDO, ZONA, DT, T_FIN = 10.0, 0.020, 1.0, 0.001, 8.0


def simular(sat=False, retardo=0.0, zona=0.0):
    n_ret = int(round(retardo / DT))
    cola = collections.deque([0.0] * n_ret)
    th, om, t = 0.0, 0.0, 0.0
    tr, pico, t_pico = [], 0.0, 0.0
    while t < T_FIN:
        cmd = KP * (R - th) - KD * om
        if n_ret:
            cola.append(cmd)
            cmd = cola.popleft()
        if sat:
            cmd = max(-TAU_MAX, min(TAU_MAX, cmd))
        if abs(cmd) <= zona:
            cmd = 0.0
        else:
            cmd -= math.copysign(zona, cmd)
        om += DT * cmd / J
        th += DT * om
        t += DT
        tr.append((t, th))
        if th > pico:
            pico, t_pico = th, t
    sobre = max(0.0, pico - R) / R
    # tiempo de establecimiento al 2 %: ultimo instante fuera de la banda
    t_est = 0.0
    for tt, x in tr:
        if abs(x - R) > 0.02 * R:
            t_est = tt
    return dict(sobre=sobre, t_pico=t_pico, t_est=t_est, final=tr[-1][1], err_final=abs(tr[-1][1] - R))


def calc():
    wn = math.sqrt(KP / J)
    zeta = KD / (2 * math.sqrt(KP * J))
    sobre_a = math.exp(-math.pi * zeta / math.sqrt(1 - zeta ** 2))
    tp_a = math.pi / (wn * math.sqrt(1 - zeta ** 2))
    casos = {"ideal": simular(), "saturacion": simular(sat=True), "retardo": simular(retardo=RETARDO), "holgura": simular(zona=ZONA),
             "los tres": simular(sat=True, retardo=RETARDO, zona=ZONA)}
    ideal = casos["ideal"]
    return dict(wn=wn, zeta=zeta, sobre_a=sobre_a, tp_a=tp_a, casos=casos, d_sobre=abs(ideal["sobre"] - sobre_a), d_tp=abs(ideal["t_pico"] - tp_a) / tp_a,
                s_id=ideal["sobre"], s_sat=casos["saturacion"]["sobre"], s_ret=casos["retardo"]["sobre"], s_hol=casos["holgura"]["sobre"], s_tres=casos["los tres"]["sobre"],
                e_id=ideal["t_est"], e_sat=casos["saturacion"]["t_est"], e_ret=casos["retardo"]["t_est"], e_hol=casos["holgura"]["t_est"], e_tres=casos["los tres"]["t_est"], tp_sat=casos["saturacion"]["t_pico"],
                err_hol=casos["holgura"]["err_final"], err_tres=casos["los tres"]["err_final"], err_id=ideal["err_final"], tau0=KP * R, cero_hol=ZONA / KP)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Lazo ILUSTRATIVO: J = {J} kg m2; Kp = {KP}; Kd = {KD}; escalon {R} rad; wn = {r['wn']:.3f} rad/s; zeta = {r['zeta']:.3f}")
    print(f"Analitico: sobreimpulso = {100*r['sobre_a']:.3f} %; tiempo de pico = {r['tp_a']:.4f} s")
    print(" caso         sobreimpulso [%]   t pico [s]   t establecimiento 2 % [s]   error final [rad]")
    for n, c in r["casos"].items():
        print(f"{n:11s} {100*c['sobre']:14.2f} {c['t_pico']:12.3f} {c['t_est']:22.3f} {c['err_final']:21.5f}")
    print(f"Ideal frente a analitico: diferencia de sobreimpulso = {100*r['d_sobre']:.3f} puntos; de tiempo de pico = {100*r['d_tp']:.3f} %")
    print(f"Par inicial pedido = {r['tau0']:.1f} N m (limite {TAU_MAX} N m); error de zona muerta esperado ~ zona/Kp = {r['cero_hol']:.3f} rad")
    assert r["d_sobre"] < 0.01 and r["d_tp"] < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
