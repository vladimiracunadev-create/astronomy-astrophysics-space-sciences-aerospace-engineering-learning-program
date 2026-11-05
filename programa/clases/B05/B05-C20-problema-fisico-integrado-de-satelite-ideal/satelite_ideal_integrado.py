#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C20: problema integrado del satélite ideal (órbita, energía, transferencia).

Datos PUBLICADOS: GM = 3,9860e14 m³/s² y radio ecuatorial 6 378 137 m (NASA NSSDC, Earth Fact Sheet,
act. 15-nov-2024); c = 299 792 458 m/s (BIPM, SI); g_n = 9,806 65 m/s² (NIST CODATA 2022);
luminosidad solar 382,8e24 W y semieje mayor terrestre 149,598e6 km (NASA NSSDC, Sun y Earth Fact Sheets).
SINTÉTICOS: masa 1000 kg, altura inicial 400 km, altura final 2000 km, velocidad de escape de gases 3000 m/s.
Modelo: dos cuerpos con la Tierra puntual, órbitas circulares coplanares, impulsos instantáneos tangenciales
(transferencia de Hohmann deducida con conservación de energía y momento angular), integración velocity-Verlet.
Supuestos: sin atmósfera, achatamiento, Sol ni Luna; empuje impulsivo; masa constante entre impulsos.
Dominio de validez: ilustrativo; NO es un cálculo de misión ni certifica vuelo o seguridad.
Tolerancias: la integración alcanza el radio final analítico a 1e-4 relativa; E se conserva a 1e-7 y L a 1e-9
entre impulsos.
"""
from __future__ import annotations
import math
import sys

GM = 3.9860e14
R = 6_378_137.0
C = 299_792_458.0
GN = 9.80665
M = 1000.0
H1, H2 = 400e3, 2000e3
VE = 3000.0
L_SOL, A_TIERRA = 382.8e24, 149.598e9

def vis_viva(r: float, a: float) -> float:
    return math.sqrt(GM * (2 / r - 1 / a))

def acc(x, y):
    r3 = (x * x + y * y) ** 1.5
    return -GM * x / r3, -GM * y / r3

def propagar(x, y, vx, vy, t_total, n):
    dt = t_total / n
    ax, ay = acc(x, y)
    rmin = rmax = math.hypot(x, y)
    e0 = 0.5 * (vx * vx + vy * vy) - GM / math.hypot(x, y)
    l0 = x * vy - y * vx
    de = dl = 0.0
    for _ in range(n):
        vx += 0.5 * ax * dt; vy += 0.5 * ay * dt
        x += vx * dt; y += vy * dt
        ax, ay = acc(x, y)
        vx += 0.5 * ax * dt; vy += 0.5 * ay * dt
        r = math.hypot(x, y)
        rmin, rmax = min(rmin, r), max(rmax, r)
        de = max(de, abs(0.5 * (vx * vx + vy * vy) - GM / r - e0) / abs(e0))
        dl = max(dl, abs((x * vy - y * vx) - l0) / l0)
    return x, y, vx, vy, rmin, rmax, de, dl

def main() -> int:
    r1, r2 = R + H1, R + H2
    at = 0.5 * (r1 + r2)
    v1, v2 = math.sqrt(GM / r1), math.sqrt(GM / r2)
    vp, va = vis_viva(r1, at), vis_viva(r2, at)
    dv1, dv2 = vp - v1, v2 - va
    t_tr = math.pi * math.sqrt(at**3 / GM)
    # 1) fórmula de Hohmann cerrada
    dv1_h = v1 * (math.sqrt(2 * r2 / (r1 + r2)) - 1)
    assert abs(dv1 - dv1_h) < 1e-9
    # 2) integración: tras el primer impulso, a t_tr el satélite está en r2 con velocidad va
    x, y, vx, vy, rmin, rmax, de, dl = propagar(r1, 0.0, 0.0, vp, t_tr, 20_000)
    r_fin = math.hypot(x, y)
    assert abs(r_fin - r2) / r2 < 1e-4, r_fin
    assert de < 1e-7 and dl < 1e-9, (de, dl)
    assert abs(math.hypot(vx, vy) - va) / va < 1e-4
    # 3) segundo impulso: órbita circular en r2 (radio constante durante una vuelta)
    ux, uy = vx / math.hypot(vx, vy), vy / math.hypot(vx, vy)
    vx2, vy2 = vx + dv2 * ux, vy + dv2 * uy
    t2 = 2 * math.pi * math.sqrt(r2**3 / GM)
    *_, rmin2, rmax2, _, _ = propagar(x, y, vx2, vy2, t2, 20_000)
    assert (rmax2 - rmin2) / r2 < 1e-3, (rmin2, rmax2)
    m_prop = M * (1 - math.exp(-(dv1 + dv2) / VE))
    T1 = 2 * math.pi * r1 / v1
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Órbita inicial (400 km): r = {r1:.0f} m; v = {v1:.2f} m/s; T = {T1:.1f} s = {T1/60:.2f} min; a_c = {v1*v1/r1:.4f} m/s²")
    print(f"  F gravitatoria = {M*GM/r1**2:.1f} N ({M*GM/r1**2/(M*GN):.3f} del peso con g_n); L = {M*r1*v1:.4e} kg m²/s; E = {-GM*M/(2*r1):.4e} J")
    print(f"Órbita final (2000 km): r = {r2:.0f} m; v = {v2:.2f} m/s; T = {2*math.pi*r2/v2:.1f} s; E = {-GM*M/(2*r2):.4e} J")
    print(f"Transferencia: semieje a_t = {at:.0f} m; v_perigeo = {vp:.2f} m/s; v_apogeo = {va:.2f} m/s")
    print(f"  dv1 = {dv1:.2f} m/s; dv2 = {dv2:.2f} m/s; dv total = {dv1+dv2:.2f} m/s; duración = {t_tr:.1f} s = {t_tr/60:.2f} min")
    print(f"  Integración: radio alcanzado = {r_fin:.0f} m (analítico {r2:.0f}); deriva E = {de:.1e}; deriva L = {dl:.1e}")
    print(f"  Órbita final integrada: rmin = {rmin2:.0f} m; rmax = {rmax2:.0f} m")
    print(f"  Propelente (v_e = {VE:.0f} m/s sintética): {m_prop:.2f} kg de {M:.0f} kg ({m_prop/M*100:.2f} %)")
    print(f"  Energía añadida a la órbita: {-GM*M/(2*r2) + GM*M/(2*r1):.4e} J")
    s = L_SOL / (4 * math.pi * A_TIERRA**2)
    teq = (s / (4 * 5.670374419e-8)) ** 0.25
    f1 = math.asin(R / r1) / math.pi
    print(f"Contexto: flujo solar {s:.1f} W/m²; T eq. esfera negra {teq:.1f} K; eclipse a 400 km {f1:.4f} de la órbita; luz vertical 400 km: {H1/C*1e3:.4f} ms")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
