#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C06: variedades invariantes estable e inestable de L1 (Tierra-Luna) en el CR3BP plano.

Datos consultados (2026-11-10): GM de la Luna 4902.800 km3/s2, semieje 384 400 km, periodo 27.322 d (JPL SSD);
GM de la Tierra ~ 398 600 km3/s2 (aproximado, deducido de la masa del JPL); radio medio de la Luna 1737.4 km (JPL SSD).
SINTETICO: desplazamiento inicial eps = 1e-6 (adimensional, 0.38 km) a lo largo del autovector; tiempo maximo de 8 unidades (34.8 d).
Metodo: autovector del autovalor real +-a de la linealizacion en L1; rama inestable = L1 +- eps v_u integrada hacia adelante;
rama estable = L1 +- eps v_s (reflejo de la inestable; no se integra).
Segunda via: solucion lineal eps e^{a t} v_u frente a la integracion no lineal en t = 2 (consistencia del autovector).
Nota: la rama estable es el reflejo exacto de la inestable por la simetria (x, y, vx, vy; t) -> (x, -y, -vx, vy; -t) del CR3BP; no se usa como prueba porque la aritmetica es identica.
Tolerancias: lineal-no lineal < 1 % ; deriva de Jacobi < 1e-8 ; tiempo de crecimiento medido dentro del 2 % del lineal (separacion 1e-4).
"""
from __future__ import annotations
import json, math, platform, sys

GM_L, GM_T, A_KM, P_L, R_LUNA = 4902.800, 398600.0, 384400.0, 27.322, 1737.4
MU = GM_L / (GM_T + GM_L)
U_D = P_L / (2 * math.pi)


def f(s):
    x, y, vx, vy = s
    r1 = math.hypot(x + MU, y)
    r2 = math.hypot(x - 1 + MU, y)
    return [vx, vy, 2 * vy + x - (1 - MU) * (x + MU) / r1**3 - MU * (x - 1 + MU) / r2**3,
            -2 * vx + y - (1 - MU) * y / r1**3 - MU * y / r2**3]


def paso(s, h):
    k1 = f(s)
    k2 = f([a + 0.5 * h * b for a, b in zip(s, k1)])
    k3 = f([a + 0.5 * h * b for a, b in zip(s, k2)])
    k4 = f([a + h * b for a, b in zip(s, k3)])
    return [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]


def jacobi(s):
    x, y, vx, vy = s
    r1 = math.hypot(x + MU, y)
    r2 = math.hypot(x - 1 + MU, y)
    return x * x + y * y + 2 * (1 - MU) / r1 + 2 * MU / r2 - vx * vx - vy * vy


def L1x():
    g = lambda x: x - (1 - MU) * (x + MU) / abs(x + MU) ** 3 - MU * (x - 1 + MU) / abs(x - 1 + MU) ** 3
    a, b = -MU + 1e-9, 1 - MU - 1e-9
    for _ in range(200):
        m = 0.5 * (a + b)
        if g(a) * g(m) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def trayectoria(s0, dt, T, cada=100):
    s, pts, dC, C0 = list(s0), [(0.0, list(s0))], 0.0, jacobi(s0)
    n = int(round(abs(T / dt)))
    for i in range(1, n + 1):
        s = paso(s, dt)
        dC = max(dC, abs(jacobi(s) - C0))
        if i % cada == 0:
            pts.append((i * dt, list(s)))
    return pts, dC


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    xl = L1x()
    r1, r2 = xl + MU, xl - 1 + MU
    xx = 1 + (1 - MU) * (3 * r1**2 / abs(r1) ** 5 - 1 / abs(r1) ** 3) + MU * (3 * r2**2 / abs(r2) ** 5 - 1 / abs(r2) ** 3)
    yy = 1 - (1 - MU) / abs(r1) ** 3 - MU / abs(r2) ** 3
    B, D = 4 - xx - yy, xx * yy
    a = math.sqrt((-B + math.sqrt(B * B - 4 * D)) / 2)
    ky = (a * a - xx) / (2 * a)
    vu = [1.0, ky, a, a * ky]
    vs = [1.0, -ky, -a, a * ky]
    nrm = math.hypot(*vu[:2])
    vu = [c / nrm for c in vu]
    vs = [c / nrm for c in vs]
    print(f"L1: x = {xl:.8f} ; a = {a:.5f} ; y/x del autovector = {ky:.5f} ; C(L1) = {jacobi([xl, 0, 0, 0]):.6f}")
    eps, dt = 1e-6, 2e-4
    res = {}
    for nombre, signo in (("hacia la Tierra (-)", -1), ("hacia la Luna (+)", 1)):
        s0 = [xl + signo * eps * vu[0], signo * eps * vu[1], signo * eps * vu[2], signo * eps * vu[3]]
        pts, dC = trayectoria(s0, dt, 8.0, 50)
        # tiempo para que la separacion de L1 llegue a 1e-3
        t_med = next(t for t, s in pts if math.hypot(s[0] - xl, s[1]) >= 1e-4)
        t_teo = math.log(1e-4 / eps) / a
        dTierra = min(math.hypot(s[0] + MU, s[1]) for t, s in pts if t > 0.5) * A_KM
        dLuna = min(math.hypot(s[0] - 1 + MU, s[1]) for t, s in pts if t > 0.5) * A_KM
        tL = min([p for p in pts if p[0] > 0.5], key=lambda p: math.hypot(p[1][0] - 1 + MU, p[1][1]))[0]
        print(f"Rama inestable {nombre}: separacion 1e-4 en t = {t_med:.3f} (lineal {t_teo:.3f}, dif {abs(t_med - t_teo) / t_teo:.2%}) ; deriva de C = {dC:.1e}")
        print(f"   minima distancia a la Tierra = {dTierra:,.0f} km ; a la Luna = {dLuna:,.0f} km (en t = {tL:.2f} = {tL * U_D:.1f} d)")
        res[signo] = dict(t_med=t_med, t_teo=t_teo, dC=dC, dT=dTierra, dL=dLuna, tL=tL, pts=pts)
    # segunda via: la solucion lineal eps e^{a t} v_u frente a la no lineal (pequena separacion)
    lin = 0.0
    for signo in (-1, 1):
        s0 = [xl + signo * eps * vu[0], signo * eps * vu[1], signo * eps * vu[2], signo * eps * vu[3]]
        sn = list(s0)
        for _ in range(int(round(2.0 / dt))):
            sn = paso(sn, dt)
        pred = [xl + signo * eps * math.exp(a * 2.0) * vu[0], signo * eps * math.exp(a * 2.0) * vu[1], signo * eps * math.exp(a * 2.0) * vu[2], signo * eps * math.exp(a * 2.0) * vu[3]]
        dev_n = [p - q for p, q in zip(sn, [xl, 0, 0, 0])]
        dev_l = [p - q for p, q in zip(pred, [xl, 0, 0, 0])]
        lin = max(lin, max(abs(p - q) for p, q in zip(dev_n, dev_l)) / max(abs(p) for p in dev_l))
    sim = lin
    print(f"Lineal frente a no lineal en t = 2 (autovector): diferencia relativa maxima = {sim:.2e}")
    print(f"Radio medio de la Luna = {R_LUNA} km (JPL SSD) ; unidad de longitud = {A_KM:.0f} km")
    assert sim < 1e-2 and all(r["dC"] < 1e-8 for r in res.values())
    assert all(abs(r["t_med"] - r["t_teo"]) / r["t_teo"] < 0.02 for r in res.values())
    print("Pruebas superadas.")
    out = {"python": platform.python_version(), "xl": xl, "a": a, "ky": ky, "CL1": jacobi([xl, 0, 0, 0]), "sim": sim}
    for tag, sg in (("t", -1), ("l", 1)):
        r = res[sg]
        out.update({f"{tag}_tmed": r["t_med"], f"{tag}_tteo": r["t_teo"], f"{tag}_dC": r["dC"], f"{tag}_dT": r["dT"], f"{tag}_dL": r["dL"],
                    f"{tag}_tL": r["tL"], f"{tag}_rel": abs(r["t_med"] - r["t_teo"]) / r["t_teo"]})
    out["t_efd"] = 1 / a * U_D
    out["t_tteo_d"] = out["t_tteo"] * U_D
    out["l_tL_d"] = out["l_tL"] * U_D
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
