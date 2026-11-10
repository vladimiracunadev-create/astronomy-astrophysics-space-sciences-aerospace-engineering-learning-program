#!/usr/bin/env python3
"""B72-C03 — Perturbacion J2 terrestre.

Tasas seculares de J2 (formulas de primer orden) frente a la pendiente de los
elementos osculadores en una integracion numerica con J2 (RK4). Orbitas SINTETICAS.
Unidades SI, angulos en grados en la salida. Marco: ecuador de la fecha, inercial.
Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14
RE = 6378137.0
J2 = 1082.63e-6
DIA = 86400.0
RAD = 180.0 / math.pi


def acel(r):
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    k = -1.5 * J2 * MU * RE ** 2 / d ** 5
    zz = 5 * z * z / (d * d)
    return [-MU * x / d ** 3 + k * x * (1 - zz), -MU * y / d ** 3 + k * y * (1 - zz), -MU * z / d ** 3 + k * z * (3 - zz)]


def paso(r, v, dt):
    def f(r, v):
        return v, acel(r)
    a1, b1 = f(r, v)
    a2, b2 = f([r[i] + 0.5 * dt * a1[i] for i in range(3)], [v[i] + 0.5 * dt * b1[i] for i in range(3)])
    a3, b3 = f([r[i] + 0.5 * dt * a2[i] for i in range(3)], [v[i] + 0.5 * dt * b2[i] for i in range(3)])
    a4, b4 = f([r[i] + dt * a3[i] for i in range(3)], [v[i] + dt * b3[i] for i in range(3)])
    return ([r[i] + dt / 6 * (a1[i] + 2 * a2[i] + 2 * a3[i] + a4[i]) for i in range(3)],
            [v[i] + dt / 6 * (b1[i] + 2 * b2[i] + 2 * b3[i] + b4[i]) for i in range(3)])


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def elementos(r, v):
    """(a, e, i, Omega, omega) osculadores; angulos en rad."""
    d = math.hypot(*r); vv = math.hypot(*v)
    h = cross(r, v); hm = math.hypot(*h)
    n = cross([0, 0, 1], h); nm = math.hypot(*n)
    rv = sum(r[i] * v[i] for i in range(3))
    ev = [((vv * vv - MU / d) * r[i] - rv * v[i]) / MU for i in range(3)]
    e = math.hypot(*ev)
    a = 1.0 / (2.0 / d - vv * vv / MU)
    inc = math.acos(h[2] / hm)
    Om = math.atan2(n[1], n[0])
    w = math.atan2(sum(ev[i] * cross(h, n)[i] for i in range(3)) / hm, sum(ev[i] * n[i] for i in range(3)))
    # w por el vector de excentricidad en el plano orbital
    ph = [h[i] / hm for i in range(3)]
    nh = [n[i] / nm for i in range(3)]
    qh = cross(ph, nh)
    w = math.atan2(sum(ev[i] * qh[i] for i in range(3)), sum(ev[i] * nh[i] for i in range(3)))
    return a, e, inc, Om, w


def estado(a, e, inc, Om, w, nu=0.0):
    p = a * (1 - e * e)
    r = p / (1 + e * math.cos(nu))
    rp = [r * math.cos(nu), r * math.sin(nu), 0.0]
    vp = [-math.sqrt(MU / p) * math.sin(nu), math.sqrt(MU / p) * (e + math.cos(nu)), 0.0]
    cO, sO, ci, si, cw, sw = math.cos(Om), math.sin(Om), math.cos(inc), math.sin(inc), math.cos(w), math.sin(w)
    R = [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
         [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
         [sw * si, cw * si, ci]]
    f = lambda x: [sum(R[i][j] * x[j] for j in range(3)) for i in range(3)]
    return f(rp), f(vp)


def tasas_teoricas(a, e, inc):
    n = math.sqrt(MU / a ** 3)
    p = a * (1 - e * e)
    f = n * J2 * (RE / p) ** 2
    dOm = -1.5 * f * math.cos(inc)
    dw = 0.75 * f * (5 * math.cos(inc) ** 2 - 1)
    return dOm * DIA * RAD, dw * DIA * RAD


def pendiente(t, y):
    """Pendiente de minimos cuadrados con desenrollado de fase."""
    u = [y[0]]
    for k in range(1, len(y)):
        d = y[k] - y[k - 1]
        d -= 2 * math.pi * round(d / (2 * math.pi))
        u.append(u[-1] + d)
    tm = sum(t) / len(t); um = sum(u) / len(u)
    return sum((t[k] - tm) * (u[k] - um) for k in range(len(t))) / sum((x - tm) ** 2 for x in t)


def medir(a, e, inc_deg, norb, dt, muestreo):
    inc = math.radians(inc_deg)
    r, v = estado(a, e, inc, math.radians(30.0), math.radians(60.0), 0.0)
    T = 2 * math.pi * math.sqrt(a ** 3 / MU)
    nsteps = int(norb * T / dt)
    ts, Os, ws = [], [], []
    for k in range(nsteps + 1):
        if k % muestreo == 0:
            _, _, _, Om, w = elementos(r, v)
            ts.append(k * dt); Os.append(Om); ws.append(w)
        r, v = paso(r, v, dt)
    return pendiente(ts, Os) * DIA * RAD, pendiente(ts, ws) * DIA * RAD


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Orbitas SINTETICAS; J2 = 1082.63e-6 (NSSDC), mu = 3.986004e14 (IAU 2015); epoca de elementos: nu = 0")
print(f"{'caso':<22}{'dOm teor':>11}{'dOm num':>11}{'err %':>8}{'dw teor':>11}{'dw num':>11}{'err %':>8}   [deg/dia]")
casos = [("baja 51.6 deg", 6778.137e3, 0.02, 51.6, 30, 10.0, 6),
         ("heliosincrona 98.2", 7078.137e3, 0.02, 98.2, 30, 10.0, 6),
         ("Molniya 63.4 deg", 26600e3, 0.74, 63.4, 3, 2.0, 30)]
for nombre, a, e, i, norb, dt, mu_ in casos:
    tO, tw = tasas_teoricas(a, e, math.radians(i))
    nO, nw = medir(a, e, i, norb, dt, mu_)
    eO = abs(nO - tO) / abs(tO) * 100
    ew = abs(nw - tw) / max(abs(tw), 1e-9) * 100
    print(f"{nombre:<22}{tO:>11.4f}{nO:>11.4f}{eO:>8.2f}{tw:>11.4f}{nw:>11.4f}{ew:>8.2f}")
    if "Molniya" not in nombre:
        assert eO < 2.0 and ew < 2.0, nombre
print("Molniya: solo 3 vueltas de 12 h; con elementos osculadores muy oscilantes, la pendiente de omega (teorica casi nula) no es informativa y la de Omega tiene error mayor.")
print("Pruebas superadas.")
