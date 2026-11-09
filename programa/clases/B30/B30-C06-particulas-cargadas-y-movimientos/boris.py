#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C06: movimiento de una particula cargada con el integrador de Boris: giro, deriva E x B y espejo magnetico.

Datos: e, m_p, m_e, c (NIST CODATA 2022), consultados 2026-11-09. Los campos (B = 1e-7 T, E = 1e-3 V/m), la energia del proton (1 keV) y la razon de espejo (1.5)
son ILUSTRATIVOS (sinteticos).
Modelo: integrador de Boris (conserva |v| en un campo magnetico puro): v^- = v + (q E/m)(dt/2); rotacion con t = (q B/m)(dt/2), s = 2t/(1 + t^2); v^+ = v^- + (v^- + v^- x t) x s;
v = v^+ + (q E/m)(dt/2). Comparacion con: radio de Larmor r_L = m v_perp/(|q| B), frecuencia de giro omega = |q| B/m, deriva v_E = E x B/B^2 y la condicion del espejo
sen^2(alpha_0) = B_0/B_m (conservacion del momento magnetico mu = m v_perp^2/(2B)).
Supuestos: no relativista, campos uniformes (salvo el espejo con B(z) = B_0 (1 + z^2/L^2)). Validez: v << c.
Tolerancia: radio de giro dentro de 1e-3 y variacion relativa menor que 1e-3; periodo dentro de 1 %; deriva E x B dentro de 1e-3; |v| conservado a 1e-12 en B puro; reflexion del espejo cuando sen^2 alpha_0 > B_0/B_m.
"""
from __future__ import annotations
import math
import platform
import sys

Q, MP, ME, C = 1.602176634e-19, 1.67262192595e-27, 9.1093837139e-31, 299792458.0


def boris(x, v, q, m, e_f, b_f, dt):
    qm = q / m
    vm = [v[i] + qm * e_f[i] * dt / 2 for i in range(3)]
    t = [qm * b_f[i] * dt / 2 for i in range(3)]
    t2 = sum(a * a for a in t)
    s = [2 * a / (1 + t2) for a in t]
    cross = lambda a, b: [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
    vp = [vm[i] + c for i, c in enumerate(cross(vm, t))]
    vq = [vm[i] + c for i, c in enumerate(cross(vp, s))]
    vn = [vq[i] + qm * e_f[i] * dt / 2 for i in range(3)]
    xn = [x[i] + vn[i] * dt for i in range(3)]
    return xn, vn


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    b0 = 1e-7
    ek = 1e3 * Q
    v = math.sqrt(2 * ek / MP)
    omega = Q * b0 / MP
    r_l = MP * v / (Q * b0)
    t_g = 2 * math.pi / omega
    print(f"proton de 1 keV en B = {b0:g} T: v = {v / 1e3:.2f} km/s ; omega = {omega:.4f} rad/s ; periodo = {t_g:.3f} s ; radio de Larmor = {r_l / 1e3:.2f} km")
    print(f"electron de 1 keV: v = {math.sqrt(2 * ek / ME) / 1e3:.0f} km/s (beta = {math.sqrt(2 * ek / ME) / C:.4f}) ; radio de Larmor = {ME * math.sqrt(2 * ek / ME) / (Q * b0) / 1e3:.2f} km")
    # giro en B puro
    dt = t_g / 200
    x, vv = [r_l, 0.0, 0.0], [0.0, v, 0.0]
    v_ini = math.sqrt(sum(a * a for a in vv))
    max_r, cruces = 0.0, 0
    prev = vv[0]
    t_cruce = None
    for i in range(1, 200 * 10 + 1):
        x, vv = boris(x, vv, Q, MP, [0, 0, 0], [0, 0, b0], dt)
        if i % 200 == 0:
            pass
    modulo = math.sqrt(sum(a * a for a in vv))
    assert abs(modulo / v_ini - 1) < 1e-12, "|v| conservado"
    # radio de la trayectoria: distancia al centro de giro (0, 0)? el centro esta en (r_l*0, ...) con v = +y, B = +z, carga +: el centro esta en x = +r_l - r_l.. ver abajo
    x, vv = [0.0, 0.0, 0.0], [v, 0.0, 0.0]
    _, vv = boris(x, vv, Q, MP, [0, 0, 0], [0, 0, b0], -dt / 2)      # velocidad a t = -dt/2 (salto de rana)
    pts = []
    for i in range(200 * 3):
        x, vv = boris(x, vv, Q, MP, [0, 0, 0], [0, 0, b0], dt)
        pts.append(x[:])
    # centro del circulo: para carga positiva con v = +x y B = +z, la fuerza es q v x B = -y: centro en (0, -r_l)
    rad = [math.hypot(p[0], p[1] + r_l) for p in pts]
    print(f"3 giros con 200 pasos por giro: radio medio = {sum(rad) / len(rad) / 1e3:.4f} km (r_L = {r_l / 1e3:.4f} km) ; variacion relativa = {(max(rad) - min(rad)) / r_l:.2e}")
    assert abs(sum(rad) / len(rad) / r_l - 1) < 1e-3 and (max(rad) - min(rad)) / r_l < 1e-3
    # periodo de giro: tiempo de regreso a la direccion inicial
    x, vv = [0.0, 0.0, 0.0], [v, 0.0, 0.0]
    ang0, giro, prev_ang = 0.0, 0.0, 0.0
    n = 0
    while giro < 2 * math.pi and n < 100000:
        x, vv = boris(x, vv, Q, MP, [0, 0, 0], [0, 0, b0], dt)
        ang = math.atan2(vv[1], vv[0])
        d = ang - prev_ang
        if d > math.pi:
            d -= 2 * math.pi
        if d < -math.pi:
            d += 2 * math.pi
        giro += abs(d)
        prev_ang = ang
        n += 1
    print(f"periodo numerico = {n * dt:.4f} s ; analitico = {t_g:.4f} s")
    assert abs(n * dt / t_g - 1) < 1e-2
    # deriva E x B
    e_f = [0.0, 1e-3, 0.0]
    x, vv = [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]
    n_g = 20
    for i in range(200 * n_g):
        x, vv = boris(x, vv, Q, MP, e_f, [0, 0, b0], dt)
    t_tot = 200 * n_g * dt
    v_deriva = x[0] / t_tot
    esp = e_f[1] / b0            # E x B / B^2 = (E_y)(+x)/B para B en z
    print(f"deriva E x B: velocidad media en x = {v_deriva / 1e3:.4f} km/s ; analitica E/B = {esp / 1e3:.4f} km/s ; cociente = {v_deriva / esp:.5f}")
    assert abs(v_deriva / esp - 1) < 1e-3
    # espejo magnetico: B(z) = B0 [1 + (Rm - 1)(z/z_m)^2] para |z| <= z_m y B_m = Rm B0 mas alla
    rm = 1.5
    z_m = 1e7
    print(f"{'alpha_0 [deg]':>13} {'sen^2 alpha_0':>14} {'1/R_m':>8} {'reflejada (numerico)':>21} {'reflejada (teoria)':>19}")
    for ang in (30.0, 40.0, 50.0, 54.0, 56.0, 60.0):
        a = math.radians(ang)

        def campo(xx):
            zz, r = xx[2], math.hypot(xx[0], xx[1])
            if abs(zz) <= z_m:
                bz = b0 * (1 + (rm - 1) * (zz / z_m) ** 2)
                dbz = 2 * b0 * (rm - 1) * zz / z_m ** 2
            else:
                bz, dbz = b0 * rm, 0.0
            br = -0.5 * dbz * r
            if r > 0:
                return [br * xx[0] / r, br * xx[1] / r, bz]
            return [0.0, 0.0, bz]
        x, vv = [0.0, 0.0, 0.0], [v * math.sin(a), 0.0, v * math.cos(a)]
        reflejada = False
        paso = t_g / 100
        _, vv = boris(x, vv, Q, MP, [0, 0, 0], campo(x), -paso / 2)
        for i in range(120000):
            x, vv = boris(x, vv, Q, MP, [0, 0, 0], campo(x), paso)
            if x[2] > 1.2 * z_m:
                break
            if vv[2] < 0 and x[2] > 0.1 * z_m:
                reflejada = True
                break
        teoria = math.sin(a) ** 2 > 1 / rm
        print(f"{ang:13.1f} {math.sin(a) ** 2:14.4f} {1 / rm:8.4f} {str(reflejada):>21} {str(teoria):>19}")
        assert reflejada == teoria, f"espejo en alpha_0 = {ang}"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
