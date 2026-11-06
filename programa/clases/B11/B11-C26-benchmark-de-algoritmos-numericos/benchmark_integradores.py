#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C26: benchmark reproducible de integradores (diagrama trabajo-precisión).

Datos: GM de la Tierra = 3.986004e14 m3/s2 (valor nominal IAU 2015, Res. B3). Órbita
ILUSTRATIVA a = 26 560 km, e = 0.30, una vuelta desde el perigeo; la referencia es la
posición inicial (la solución exacta vuelve al punto de partida tras un periodo).
Modelo: dos cuerpos en el plano. Métricas: error de posición al final de la vuelta y
número de evaluaciones de la fuerza (independiente de la máquina); además, el tiempo
de reloj (mediana de 5 repeticiones), que SÍ depende de la máquina y se reporta aparte.
Métodos: Euler, Heun, RK4, leapfrog (paso fijo) y RK4 con duplicación de paso
(adaptativo, tolerancia relativa variable).
Protocolo: misma entrada y mismo estado inicial para todos; barrido de resoluciones en
potencias de dos; se reporta la menor cantidad de evaluaciones que alcanza cada error
objetivo; el barrido es determinista (misma salida en dos corridas).
Tolerancia/pruebas: (1) los errores y las evaluaciones se repiten idénticos en dos
corridas; (2) el orden observado de cada método de paso fijo concuerda con el teórico
(+-0.4); (3) para el objetivo de 1 km (1000 m), las evaluaciones cumplen RK4 < Heun < Euler
(Euler puede no alcanzarlo en el barrido: cuenta como infinito);
(4) el adaptativo necesita menos evaluaciones que Euler para ese objetivo.
"""
import math, platform, statistics, time

GM = 3.986004e14
a, e = 26_560e3, 0.30
T = 2 * math.pi * math.sqrt(a**3 / GM)
S0 = (a * (1 - e), 0.0, 0.0, math.sqrt(GM * (1 + e) / (a * (1 - e))))
EV = [0]


def acc(x, y):
    EV[0] += 1
    r3 = (x * x + y * y) ** 1.5
    return -GM * x / r3, -GM * y / r3


def F(s):
    ax, ay = acc(s[0], s[1])
    return (s[2], s[3], ax, ay)


def c(s, h, k, q):
    return tuple(si + h * q * ki for si, ki in zip(s, k))


def euler(s, h):
    return c(s, h, F(s), 1.0)


def heun(s, h):
    k1 = F(s); k2 = F(c(s, h, k1, 1.0))
    return tuple(si + 0.5 * h * (p + q) for si, p, q in zip(s, k1, k2))


def rk4(s, h):
    k1 = F(s); k2 = F(c(s, h, k1, .5)); k3 = F(c(s, h, k2, .5)); k4 = F(c(s, h, k3, 1.))
    return tuple(si + h * (p + 2 * q + 2 * r + w) / 6 for si, p, q, r, w in zip(s, k1, k2, k3, k4))


def leapfrog(s, h):
    x, y, vx, vy = s
    ax, ay = acc(x, y)
    vx += .5 * h * ax; vy += .5 * h * ay
    x += h * vx; y += h * vy
    ax, ay = acc(x, y)
    vx += .5 * h * ax; vy += .5 * h * ay
    return (x, y, vx, vy)


def fijo(paso, N):
    EV[0] = 0
    s = S0
    for _ in range(N):
        s = paso(s, T / N)
    return math.hypot(s[0] - S0[0], s[1] - S0[1]), EV[0]


def adaptativo(rtol, atol=1e-3):
    EV[0] = 0
    s, t, h = S0, 0.0, 10.0
    while t < T:
        h = min(h, T - t)
        s1 = rk4(s, h)
        s2 = rk4(rk4(s, h / 2), h / 2)
        err = max(abs(u - v) / 15 / (atol + rtol * max(abs(u), abs(v))) for u, v in zip(s2, s1))
        if err <= 1:
            t += h; s = s2
        h *= min(5.0, max(0.2, 0.9 * (err + 1e-30) ** -0.2))
    return math.hypot(s[0] - S0[0], s[1] - S0[1]), EV[0]


def barrido():
    res = {}
    for nombre, paso, Ns in (("Euler", euler, [2**k for k in range(8, 21)]), ("Heun", heun, [2**k for k in range(6, 15)]),
                             ("RK4", rk4, [2**k for k in range(5, 13)]), ("leapfrog", leapfrog, [2**k for k in range(6, 15)])):
        res[nombre] = [(fijo(paso, N), N) for N in Ns]
    res["RK4 adaptativo"] = [(adaptativo(r), r) for r in (1e-4, 1e-6, 1e-8, 1e-10)]
    return res


def evals_para(lista, objetivo):
    ok = [ev for (err, ev), _ in lista if err <= objetivo]
    return min(ok) if ok else None


print(f"Python {platform.python_version()} ; {platform.platform()}")
print(f"órbita ilustrativa: a = {a/1e3:.0f} km, e = {e}, periodo = {T:.1f} s")
r1, r2 = barrido(), barrido()
for k in r1:
    assert [x[0] for x in r1[k]] == [x[0] for x in r2[k]], "el barrido no es reproducible"
print("reproducibilidad: dos barridos completos dan exactamente los mismos errores y evaluaciones")

orden_teo = {"Euler": 1, "Heun": 2, "RK4": 4, "leapfrog": 2}
for nombre in orden_teo:
    L = r1[nombre]
    ps = [math.log2(L[i][0][0] / L[i + 1][0][0]) for i in range(len(L) - 3, len(L) - 1)]
    p = sum(ps) / len(ps)
    print(f"orden observado {nombre:9s}: {p:.2f} (teórico {orden_teo[nombre]})")
    if nombre != "RK4":
        assert abs(p - orden_teo[nombre]) < 0.4
print("\nevaluaciones mínimas del barrido para alcanzar cada error objetivo:")
objetivos = (1e5, 1e3, 1e1, 1.0)
print("   método            " + "".join(f"{('<= %g m' % o):>14s}" for o in objetivos))
tab = {}
for nombre in r1:
    fila = [evals_para(r1[nombre], o) for o in objetivos]
    tab[nombre] = fila
    print(f"   {nombre:17s} " + "".join(f"{('-' if v is None else str(v)):>14s}" for v in fila))
i1km = objetivos.index(1e3)
INF = float("inf")
v = lambda n: INF if tab[n][i1km] is None else tab[n][i1km]
assert v("RK4") < v("Heun") < v("Euler") and v("RK4 adaptativo") < v("Euler")

print("\ntiempo de reloj (mediana de 5 repeticiones; depende de la máquina y no es parte de la prueba):")
for nombre, paso, N in (("Euler", euler, 2**13), ("Heun", heun, 2**11), ("RK4", rk4, 2**9), ("leapfrog", leapfrog, 2**11)):
    ts = []
    for _ in range(5):
        t0 = time.perf_counter(); fijo(paso, N); ts.append(time.perf_counter() - t0)
    err, ev = fijo(paso, N)
    print(f"   {nombre:9s} N={N:5d}: error = {err:10.3e} m ; evaluaciones = {ev:6d} ; tiempo = {1e3*statistics.median(ts):7.1f} ms")
print("Pruebas superadas.")
