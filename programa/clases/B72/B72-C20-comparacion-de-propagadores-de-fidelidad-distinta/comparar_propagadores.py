#!/usr/bin/env python3
"""B72-C20 — Comparacion de propagadores de fidelidad distinta.

Escalera de fidelidad sobre una orbita baja SINTETICA: (A) dos cuerpos, (B) J2 secular analitico,
(C) numerico con J2, (D) numerico con J2 y arrastre, frente a una "verdad sintetica" numerica con
J2, J3, J4 y arrastre. La verdad NO es una observacion. Atmosfera exponencial ILUSTRATIVA.
Unidades SI; marco inercial del ecuador de la fecha. Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14
RE = 6378137.0
J = {2: 1082.63e-6, 3: -2.53881e-6, 4: -1.65597e-6}   # J2 NSSDC; J3 y J4 WGS-72 (Spacetrack Report 3)
OM_T = 2 * math.pi / (23.9345 * 3600.0)
RHO_REF, H_REF, ESC = 3.0e-12, 400e3, 60e3             # ILUSTRATIVOS
B = 45.0                                               # kg/m2, ILUSTRATIVO
DIA = 86400.0


def zonal(r, terminos):
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    s = z / d
    a = [0.0, 0.0, 0.0]
    for n in terminos:
        p = [1.0, s]; dp = [0.0, 1.0]
        for k in range(2, n + 1):
            p.append(((2 * k - 1) * s * p[k - 1] - (k - 1) * p[k - 2]) / k)
            dp.append(dp[k - 2] + (2 * k - 1) * p[k - 1])
        c = MU * J[n] * RE ** n
        for i, comp in enumerate((x, y, z)):
            gr = -(n + 1) * p[n] * comp / d ** (n + 3)
            gz = dp[n] / d ** (n + 2) * ((1.0 if i == 2 else 0.0) - s * comp / d)
            a[i] += -c * (gr + gz)
    return a


def drag(r, v):
    vr = [v[0] + OM_T * r[1], v[1] - OM_T * r[0], v[2]]
    vm = math.sqrt(vr[0] ** 2 + vr[1] ** 2 + vr[2] ** 2)
    d = math.sqrt(r[0] ** 2 + r[1] ** 2 + r[2] ** 2)
    k = -0.5 * RHO_REF * math.exp(-(d - RE - H_REF) / ESC) * vm / B
    return [k * c for c in vr]


def modelo(terminos, con_arrastre):
    def acel(r, v):
        d = math.sqrt(r[0] ** 2 + r[1] ** 2 + r[2] ** 2)
        a = [-MU * r[i] / d ** 3 for i in range(3)]
        z = zonal(r, terminos)
        for i in range(3):
            a[i] += z[i]
        if con_arrastre:
            ad = drag(r, v)
            for i in range(3):
                a[i] += ad[i]
        return a
    return acel


def propaga(acel, r, v, tiempos, dt=20.0):
    out, t, n_ev = {}, 0.0, 0
    for T in tiempos:
        for _ in range(int(round((T - t) / dt))):
            a1 = acel(r, v)
            r2 = [r[i] + .5 * dt * v[i] for i in range(3)]; v2 = [v[i] + .5 * dt * a1[i] for i in range(3)]
            a2 = acel(r2, v2)
            r3 = [r[i] + .5 * dt * v2[i] for i in range(3)]; v3 = [v[i] + .5 * dt * a2[i] for i in range(3)]
            a3 = acel(r3, v3)
            r4 = [r[i] + dt * v3[i] for i in range(3)]; v4 = [v[i] + dt * a3[i] for i in range(3)]
            a4 = acel(r4, v4)
            r, v = ([r[i] + dt / 6 * (v[i] + 2 * v2[i] + 2 * v3[i] + v4[i]) for i in range(3)],
                    [v[i] + dt / 6 * (a1[i] + 2 * a2[i] + 2 * a3[i] + a4[i]) for i in range(3)])
            n_ev += 4
        t = T
        out[T] = list(r)
    return out, n_ev


def kepler_pos(a, e, inc, Om, w, M):
    E = M % (2 * math.pi)
    for _ in range(60):
        E -= (E - e * math.sin(E) - (M % (2 * math.pi))) / (1 - e * math.cos(E))
    nu = 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))
    p = a * (1 - e * e); r = p / (1 + e * math.cos(nu))
    rp = [r * math.cos(nu), r * math.sin(nu), 0.0]
    cO, sO, ci, si, cw, sw = math.cos(Om), math.sin(Om), math.cos(inc), math.sin(inc), math.cos(w), math.sin(w)
    R = [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
         [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
         [sw * si, cw * si, ci]]
    return [sum(R[i][j] * rp[j] for j in range(3)) for i in range(3)]


a0, e0, i0 = 6878.137e3, 0.01, math.radians(51.6)
Om0, w0, M0 = math.radians(40.0), math.radians(30.0), 0.0
# estado inicial (en M = 0: perigeo)
rp0 = kepler_pos(a0, e0, i0, Om0, w0, M0)
# velocidad en el perigeo
vp = math.sqrt(MU * (1 + e0) / (a0 * (1 - e0)))
cO, sO, ci, si, cw, sw = math.cos(Om0), math.sin(Om0), math.cos(i0), math.sin(i0), math.cos(w0), math.sin(w0)
R = [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
     [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
     [sw * si, cw * si, ci]]
v0 = [R[i][1] * vp for i in range(3)]
r0 = rp0
tiempos = [1 * DIA, 3 * DIA, 7 * DIA]

print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print(f"Orbita SINTETICA a = {a0 / 1e3:.3f} km, e = {e0}, i = 51.6 deg ; B = {B} kg/m2 y atmosfera ILUSTRATIVOS ; RK4 paso 20 s")

verdad, ev_v = propaga(modelo((2, 3, 4), True), r0, v0, tiempos)
C_, ev_c = propaga(modelo((2,), False), r0, v0, tiempos)
D_, ev_d = propaga(modelo((2,), True), r0, v0, tiempos)

# A: dos cuerpos ; B: J2 secular analitico
n = math.sqrt(MU / a0 ** 3)
p = a0 * (1 - e0 * e0)
f = n * J[2] * (RE / p) ** 2
dOm = -1.5 * f * math.cos(i0)
dw = 0.75 * f * (5 * math.cos(i0) ** 2 - 1)
dM = n + 0.75 * f * math.sqrt(1 - e0 * e0) * (3 * math.cos(i0) ** 2 - 1)
A_, B_ = {}, {}
for T in tiempos:
    A_[T] = kepler_pos(a0, e0, i0, Om0, w0, M0 + n * T)
    B_[T] = kepler_pos(a0, e0, i0, Om0 + dOm * T, w0 + dw * T, M0 + dM * T)

print("\nError de posicion respecto a la verdad sintetica (J2+J3+J4+arrastre) [km]")
print(f"{'propagador':<36}{'1 dia':>10}{'3 dias':>10}{'7 dias':>10}{'evaluaciones':>16}")
filas = [("A  dos cuerpos (analitico)", A_, 0), ("B  J2 secular (analitico)", B_, 0), ("C  numerico J2", C_, ev_c), ("D  numerico J2 + arrastre", D_, ev_d)]
for nombre, sol, ev in filas:
    print(f"{nombre:<36}" + "".join(f"{math.dist(sol[T], verdad[T]) / 1e3:>10.3f}" for T in tiempos) + f"{ev:>16}")
print(f"{'verdad: numerico J2+J3+J4+arrastre':<36}{'-':>10}{'-':>10}{'-':>10}{ev_v:>16}")
eA, eB, eC, eD = (math.dist(s[tiempos[2]], verdad[tiempos[2]]) for _, s, _ in filas)
print(f"\nOrden de fidelidad a 7 dias: A {eA / 1e3:.1f} km > B {eB / 1e3:.1f} km > C {eC / 1e3:.1f} km > D {eD / 1e3:.2f} km")
assert eA > eB > eC > eD
print("Pruebas superadas.")
