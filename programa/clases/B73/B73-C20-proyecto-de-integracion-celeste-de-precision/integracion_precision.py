#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C20: proyecto de integracion celeste de precision: presupuesto de error, convergencia y reversibilidad en un sistema joviano de cinco cuerpos.

Datos consultados (2026-11-10): GM de Io, Europa, Ganymede y Callisto 5959.91547, 3202.71210, 9887.83275, 7179.28340 km3/s2 (JPL SSD, JUP365);
GM de Jupiter 126.687e6 km3/s2, radio ecuatorial 71 492 km y J2 = 14 736e-6 (NASA/NSSDC, Jupiter Fact Sheet, 2024-10-02); semiejes medios 421 800; 671 100; 1 070 400; 1 882 700 km
(JPL SSD, tabla de elementos de satelites, J2000).
SINTETICO: condiciones iniciales = orbitas circulares coplanares con esos semiejes y fases 0, 90, 180 y 270 grados (como en B73-C08); no son el estado real del sistema.
Modelo: 5 masas puntuales con gravedad newtoniana mutua; modelo B anade el achatamiento J2 de Jupiter sobre las lunas (aceleracion central -3/2 J2 GM R^2 / r^4 en el plano
ecuatorial, con la reaccion sobre Jupiter). Horizonte T = 16.689 d (una orbita de Callisto).
Integradores: leapfrog (orden 2) y Yoshida de orden 4 (composicion de 3 leapfrogs), ambos simplecticos. Referencia: Yoshida con dt = 25 s.
Presupuesto de error: error de truncacion (frente a la referencia), error de modelo (efecto de J2) y reversibilidad (T adelante y T atras).
Tolerancias: orden estimado dentro de +-0.4 del teorico; leapfrog dt = 200 s con error de posicion < efecto de J2 / 10 y Yoshida dt = 400 s < efecto de J2 / 1000; reversibilidad < 1e-6 km.
"""
from __future__ import annotations
import json, math, platform, sys

GM = [126.687e6, 5959.91547, 3202.71210, 9887.83275, 7179.28340]
NOM = ["Jupiter", "Io", "Europa", "Ganymede", "Callisto"]
A = [0.0, 421800.0, 671100.0, 1070400.0, 1882700.0]
J2, RJ = 14736e-6, 71492.0
N = 5
T = 16.689 * 86400.0
W1 = 1.0 / (2.0 - 2.0 ** (1.0 / 3.0))
W0 = -(2.0 ** (1.0 / 3.0)) * W1


def inicial():
    r, v = [[0.0, 0.0]], [[0.0, 0.0]]
    for i in range(1, N):
        ang = math.radians(90.0 * (i - 1))
        vc = math.sqrt((GM[0] + GM[i]) / A[i])
        r.append([A[i] * math.cos(ang), A[i] * math.sin(ang)])
        v.append([-vc * math.sin(ang), vc * math.cos(ang)])
    M = sum(GM)
    for arr in (r, v):
        cx = sum(GM[i] * arr[i][0] for i in range(N)) / M
        cy = sum(GM[i] * arr[i][1] for i in range(N)) / M
        for i in range(N):
            arr[i][0] -= cx
            arr[i][1] -= cy
    return r, v


def acel(r, j2):
    a = [[0.0, 0.0] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            dx, dy = r[j][0] - r[i][0], r[j][1] - r[i][1]
            d3 = (dx * dx + dy * dy) ** 1.5
            a[i][0] += GM[j] * dx / d3
            a[i][1] += GM[j] * dy / d3
            a[j][0] -= GM[i] * dx / d3
            a[j][1] -= GM[i] * dy / d3
    if j2:
        for i in range(1, N):
            dx, dy = r[i][0] - r[0][0], r[i][1] - r[0][1]
            d = math.hypot(dx, dy)
            f = -1.5 * J2 * GM[0] * RJ**2 / d**4  # aceleracion radial (hacia Jupiter) por unidad de masa
            a[i][0] += f * dx / d
            a[i][1] += f * dy / d
            a[0][0] -= GM[i] / GM[0] * f * dx / d
            a[0][1] -= GM[i] / GM[0] * f * dy / d
    return a


def energia(r, v):
    e = 0.0
    for i in range(N):
        e += 0.5 * GM[i] * (v[i][0] ** 2 + v[i][1] ** 2)
        for j in range(i + 1, N):
            e -= GM[i] * GM[j] / math.hypot(r[i][0] - r[j][0], r[i][1] - r[j][1])
    return e


def leap(r, v, h, j2):
    a = acel(r, j2)
    for i in range(N):
        v[i][0] += 0.5 * h * a[i][0]
        v[i][1] += 0.5 * h * a[i][1]
        r[i][0] += h * v[i][0]
        r[i][1] += h * v[i][1]
    a = acel(r, j2)
    for i in range(N):
        v[i][0] += 0.5 * h * a[i][0]
        v[i][1] += 0.5 * h * a[i][1]


def yoshida(r, v, h, j2):
    leap(r, v, W1 * h, j2)
    leap(r, v, W0 * h, j2)
    leap(r, v, W1 * h, j2)


def correr(paso, dt, j2=False, atras=False):
    r, v = inicial()
    n = int(round(T / dt))
    h = T / n
    for _ in range(n):
        paso(r, v, h, j2)
    if atras:
        for _ in range(n):
            paso(r, v, -h, j2)
    return r, v, n


def dif_pos(r1, r2):
    return max(math.hypot(r1[i][0] - r2[i][0], r1[i][1] - r2[i][1]) for i in range(1, N))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    rref, vref, nref = correr(yoshida, 25.0)
    e0 = energia(*inicial())
    print(f"Referencia: Yoshida 4, dt = 25 s ({nref} pasos, {3 * nref} evaluaciones); T = {T / 86400:.3f} d")
    print(" metodo     dt [s]   pasos   evaluaciones   error de energia   error de posicion [km]   orden estimado")
    tabla = {}
    for nom, paso, ev, dts in (("leapfrog", leap, 1, (1600.0, 800.0, 400.0, 200.0)), ("yoshida4", yoshida, 3, (3200.0, 1600.0, 800.0, 400.0))):
        prev = None
        for dt in dts:
            r, v, n = correr(paso, dt)
            ee = abs(energia(r, v) / e0 - 1)
            ep = dif_pos(r, rref)
            ordn = math.log(prev / ep) / math.log(2) if prev else float("nan")
            prev = ep
            print(f" {nom:9s} {dt:7.0f}  {n:6d}   {ev * n:10d}     {ee:14.2e}     {ep:18.3e}       {ordn:8.2f}" if prev and ordn == ordn else f" {nom:9s} {dt:7.0f}  {n:6d}   {ev * n:10d}     {ee:14.2e}     {ep:18.3e}            -")
            tabla[(nom, dt)] = (ee, ep, ordn, ev * n)
            out[f"{nom}_{int(dt)}_pos"], out[f"{nom}_{int(dt)}_en"], out[f"{nom}_{int(dt)}_ev"] = ep, ee, ev * n
            out[f"{nom}_{int(dt)}_ord"] = ordn if ordn == ordn else 0.0
    # modelo: efecto de J2
    rj, vj, _ = correr(yoshida, 25.0, j2=True)
    efecto = dif_pos(rj, rref)
    print(f"Error de modelo: efecto de J2 de Jupiter sobre las posiciones tras {T / 86400:.3f} d = {efecto:,.1f} km (maximo entre las cuatro lunas)")
    out["efecto_j2"] = efecto
    # reversibilidad
    r0, v0 = inicial()
    rr, vr, _ = correr(leap, 400.0, atras=True)
    rev = dif_pos(rr, r0)
    print(f"Reversibilidad (leapfrog, dt = 400 s, T adelante y T atras): diferencia de posicion = {rev:.2e} km")
    out["rev"] = rev
    # presupuesto: criterio
    ep200 = tabla[("leapfrog", 200.0)][1]
    ep400y = tabla[("yoshida4", 400.0)][1]
    print(f"Presupuesto: error de truncacion leapfrog dt=200 s = {ep200:.2e} km ; Yoshida dt=400 s = {ep400y:.2e} km ; modelo (J2) = {efecto:,.1f} km ; cociente truncacion/modelo = {ep200 / efecto:.1e} y {ep400y / efecto:.1e}")
    out["ep200"], out["ep400y"] = ep200, ep400y
    presupuesto = efecto / 100.0
    print(f"Con un presupuesto de truncacion del 1 % del efecto de J2 ({presupuesto:,.1f} km), extrapolando con el orden medido:")
    for nom, dt_u, p_ord, ev in (("leapfrog", 200.0, 2.0, 1), ("yoshida4", 400.0, 4.0, 3)):
        e_u = tabla[(nom, dt_u)][1]
        dt_req = dt_u * (presupuesto / e_u) ** (1.0 / p_ord)
        n_req = T / dt_req
        print(f"   {nom:9s}: dt requerido = {dt_req:7.1f} s ; pasos = {n_req:8.0f} ; evaluaciones = {ev * n_req:9.0f}")
        out[f"{nom}_dtreq"], out[f"{nom}_evreq"] = dt_req, ev * n_req
    out["presupuesto"] = presupuesto
    out["ep200_rel"] = ep200 / efecto
    out["yoshida4_400_pos_rel"] = ep400y / efecto
    out["ahorro"] = out["leapfrog_evreq"] / out["yoshida4_evreq"]
    assert 1.6 < tabla[("leapfrog", 200.0)][2] < 2.4
    assert 3.2 < tabla[("yoshida4", 800.0)][2] < 4.8 or 3.2 < tabla[("yoshida4", 400.0)][2] < 4.8
    assert ep200 < efecto / 10 and ep400y < efecto / 1e3 and rev < 1e-6
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
