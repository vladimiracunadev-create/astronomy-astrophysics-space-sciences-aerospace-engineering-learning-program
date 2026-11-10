#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C18: transferencia de Hohmann, su minimo en una familia de transferencias y comparacion con la bieliptica.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14, (GM)Sol = 1.3271244e20 m3/s2 y R ecuatorial = 6.3781e6 m (IAU 2015 B3);
fichas NASA/NSSDC: Tierra a = 149.598e6 km; Marte a = 227.956e6 km, periodo sidereo 686.980 d; Tierra periodo sidereo 365.256 d. La pagina de NASA Basics of Space Flight (cap. 4-1)
describe la orbita de Hohmann Tierra-Marte (perihelio en la orbita terrestre, afelio en la de Marte).
SINTETICO/ILUSTRATIVO: circular inicial de 400 km de altitud y final geoestacionaria (r = 42164.2 km); orbitas planetarias CIRCULARES y coplanares con radio igual al
semieje de la ficha (aproximacion); relaciones de radios 20 y 50 de la comparacion bieliptica (ilustrativas).
Sistema: marco inercial del cuerpo central, SI; impulsos instantaneos tangentes; dos cuerpos.
Segunda via: (1) se barre una familia de transferencias con perigeo r1 y apogeo rA >= r2 con circularizacion en r2 (impulso vectorial con el angulo de trayectoria); el minimo debe ser rA = r2;
(2) el tiempo de vuelo se comprueba con la semi-vuelta de una integracion RK4; (3) el umbral de relacion de radios 11.94 se busca por biseccion.
Tolerancias: minimo del barrido en rA = r2 con 1e-3 relativa; tiempo RK4 frente a pi sqrt(a^3/mu) 1e-6; umbral frente a 11.94 dentro de 5e-3.
"""
from __future__ import annotations
import math, platform

MU_T, MU_S, RE = 3.986004e14, 1.3271244e20, 6.3781e6
DIA = 86400.0


def hohmann(mu, r1, r2):
    a = 0.5 * (r1 + r2)
    v1 = math.sqrt(mu / r1)
    v2 = math.sqrt(mu / r2)
    vp = math.sqrt(mu * (2 / r1 - 1 / a))
    va = math.sqrt(mu * (2 / r2 - 1 / a))
    dv1, dv2 = vp - v1, v2 - va
    return dict(dv1=dv1, dv2=dv2, dv=abs(dv1) + abs(dv2), tof=math.pi * math.sqrt(a ** 3 / mu), a=a, vp=vp, va=va)


def dv_familia(mu, r1, r2, rA):
    """Transferencia con perigeo r1 y apogeo rA >= r2; circulariza en r2 con impulso vectorial."""
    a = 0.5 * (r1 + rA)
    vp = math.sqrt(mu * (2 / r1 - 1 / a))
    dv1 = vp - math.sqrt(mu / r1)
    h = r1 * vp
    vt = math.sqrt(mu * (2 / r2 - 1 / a))
    cosg = min(1.0, h / (r2 * vt))
    vc = math.sqrt(mu / r2)
    dv2 = math.sqrt(vt * vt + vc * vc - 2 * vt * vc * cosg)
    return dv1 + dv2


def bielip(mu, r1, r2, rb):
    a1 = 0.5 * (r1 + rb)
    a2 = 0.5 * (r2 + rb)
    v1 = math.sqrt(mu / r1)
    dv1 = math.sqrt(mu * (2 / r1 - 1 / a1)) - v1
    dv2 = math.sqrt(mu * (2 / rb - 1 / a2)) - math.sqrt(mu * (2 / rb - 1 / a1))
    dv3 = abs(math.sqrt(mu * (2 / r2 - 1 / a2)) - math.sqrt(mu / r2))
    return dv1 + dv2 + dv3


def tof_rk4(mu, a, rp):
    vp = math.sqrt(mu * (2 / rp - 1 / a))
    s = (rp, 0.0, 0.0, vp)
    ra = 2 * a - rp
    dt = 2.0 if a < 1e9 else 3600.0
    t = 0.0
    def f(s):
        d3 = (s[0] ** 2 + s[1] ** 2) ** 1.5
        return (s[2], s[3], -mu * s[0] / d3, -mu * s[1] / d3)
    while True:
        k1 = f(s); k2 = f(tuple(s[i] + 0.5 * dt * k1[i] for i in range(4)))
        k3 = f(tuple(s[i] + 0.5 * dt * k2[i] for i in range(4))); k4 = f(tuple(s[i] + dt * k3[i] for i in range(4)))
        sn = tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4))
        if s[1] > 0 and sn[1] <= 0:  # cruce del eje x por el apoapsis
            frac = s[1] / (s[1] - sn[1])
            return t + frac * dt, math.hypot(*s[:2])
        s = sn
        t += dt


def calcular():
    R = {}
    r1, r2 = RE + 400e3, 42164.2e3
    h = hohmann(MU_T, r1, r2)
    R.update({f"leo_{k}": v for k, v in h.items()})
    R["leo_tof_h"] = h["tof"] / 3600.0
    R["leo_ratio"] = r2 / r1
    tr, rap = tof_rk4(MU_T, h["a"], r1)
    R["leo_tof_rk4_h"] = tr / 3600.0
    R["leo_tof_dif"] = abs(tr - h["tof"]) / h["tof"]
    # barrido
    best = None
    vals = []
    for k in range(0, 61):
        rA = r2 * (1 + 0.05 * k)
        d = dv_familia(MU_T, r1, r2, rA)
        vals.append((rA / r2, d))
        if best is None or d < best[1]:
            best = (rA / r2, d)
    R["barrido_min_rA"] = best[0]
    R["barrido_min_dv"] = best[1]
    R["barrido_dv_x2"] = vals[20][1]
    R["barrido_dv_x4"] = vals[60][1]
    R["barrido_dif"] = abs(best[1] - h["dv"]) / h["dv"]
    # Tierra-Marte (circulares y coplanares, radio = semieje de la ficha)
    re_, rm = 149.598e9, 227.956e9
    hm = hohmann(MU_S, re_, rm)
    R.update({f"mars_{k}": v for k, v in hm.items()})
    R["mars_tof_d"] = hm["tof"] / DIA
    R["mars_ratio"] = rm / re_
    n_mars = 2 * math.pi / (686.980 * DIA)
    R["mars_fase_deg"] = math.degrees(math.pi - n_mars * hm["tof"])
    R["mars_v_t"] = math.sqrt(MU_S / re_)
    # bieliptica
    for rr, etiq in ((20.0, "20"), (50.0, "50")):
        rr1 = 1.0
        hh = hohmann(1.0, rr1, rr)
        R[f"h_{etiq}"] = hh["dv"]
        R[f"b_{etiq}"] = min(bielip(1.0, rr1, rr, rb) for rb in [rr * (1 + 0.2 * k) for k in range(1, 400)])
    lo, hi = 5.0, 30.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        dh = hohmann(1.0, 1.0, mid)["dv"]
        db = bielip(1.0, 1.0, mid, 1e8)
        if db < dh:
            hi = mid
        else:
            lo = mid
    R["umbral"] = 0.5 * (lo + hi)
    # Hohmann con ratio 15.58 (Tierra -> Saturno no se usa); comparar con ratio de Marte: Hohmann < bieliptica
    R["mars_bi"] = min(bielip(1.0, 1.0, R["mars_ratio"], rb) for rb in [R["mars_ratio"] * (1 + 0.2 * k) for k in range(1, 400)])
    R["mars_h_norm"] = hohmann(1.0, 1.0, R["mars_ratio"])["dv"]
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(f"LEO SINTETICA 400 km -> GEO (r1 = 6778.1 km, r2 = 42164.2 km, razon {R['leo_ratio']:.4f}):")
    print(f"  a_transf = {R['leo_a'] / 1e3:.3f} km ; v_p = {R['leo_vp']:.3f} m/s ; v_a = {R['leo_va']:.3f} m/s")
    print(f"  dv1 = {R['leo_dv1']:.3f} m/s ; dv2 = {R['leo_dv2']:.3f} m/s ; total = {R['leo_dv']:.3f} m/s")
    print(f"  tiempo de vuelo = {R['leo_tof_h']:.4f} h ; RK4 (semivuelta) = {R['leo_tof_rk4_h']:.4f} h ; dif = {R['leo_tof_dif']:.1e}")
    print(f"  barrido de apogeos rA/r2 en [1, 4]: minimo en rA/r2 = {R['barrido_min_rA']:.2f} con {R['barrido_min_dv']:.3f} m/s (dif con Hohmann {R['barrido_dif']:.1e}) ; rA = 2 r2: {R['barrido_dv_x2']:.1f} ; rA = 4 r2: {R['barrido_dv_x4']:.1f} m/s")
    print("Tierra -> Marte (orbitas CIRCULARES coplanares con radio = semieje de la ficha; aproximacion):")
    print(f"  razon de radios = {R['mars_ratio']:.4f} ; dv1 = {R['mars_dv1']:.1f} m/s ; dv2 = {R['mars_dv2']:.1f} m/s ; tiempo de vuelo = {R['mars_tof_d']:.2f} d")
    print(f"  angulo de fase Marte-Tierra a la salida = {R['mars_fase_deg']:.2f} grados (Marte por delante)")
    print("Comparacion con la bieliptica (unidades de r1 = 1, mu = 1, v_c1 = 1):")
    print(f"  razon 20: Hohmann {R['h_20']:.5f} ; bieliptica minima {R['b_20']:.5f}")
    print(f"  razon 50: Hohmann {R['h_50']:.5f} ; bieliptica minima {R['b_50']:.5f}")
    print(f"  razon de Marte {R['mars_ratio']:.3f}: Hohmann {R['mars_h_norm']:.5f} ; bieliptica minima {R['mars_bi']:.5f}")
    print(f"  umbral (bieliptica con r_b -> infinito = Hohmann) en razon = {R['umbral']:.3f}")
    assert R["barrido_min_rA"] == 1.0 and R["barrido_dif"] < 1e-3
    assert R["leo_tof_dif"] < 1e-6
    assert abs(R["umbral"] - 11.94) < 5e-3 * 11.94
    assert R["b_50"] < R["h_50"] and R["b_20"] < R["h_20"] and R["mars_bi"] > R["mars_h_norm"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
