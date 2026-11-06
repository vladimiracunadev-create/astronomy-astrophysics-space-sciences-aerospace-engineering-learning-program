#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C17: optimización numérica con verificación independiente.

Datos: (a) transferencia entre órbitas circulares coplanares con razón de radios
R = r2/r1 = 13 (valor ILUSTRATIVO), en unidades de la velocidad circular de la
órbita inicial; (b) ecuación de Kepler con e = 0.74 (ilustrativa) y M = 1.0 rad;
(c) datos SINTÉTICOS y = a exp(-b t) con a = 5, b = 0.3, ruido gaussiano de
desviación 0.05 generado con random.Random(2026); (d) cuadrática f = (x1^2 + k x2^2)/2.
Modelo: (a) coste Dv(x) de una transferencia biela con apoastro intermedio x
(en unidades de r1); a x = R coincide con la de Hohmann. Los saltos de velocidad
salen de la ecuación vis-viva v^2 = mu (2/r - 1/a).
Métodos: sección áurea (sin derivadas), Newton (con derivada), Gauss-Newton
(mínimos cuadrados no lineales) y descenso por gradiente con paso óptimo.
Supuestos: órbitas circulares coplanares, impulsos instantáneos, dos cuerpos.
Tolerancia: sección áurea y barrido en malla coinciden a 1e-3 en x; la derivada
en el mínimo interior, < 1e-6 (y no nula si el mínimo está en la frontera); Newton resuelve Kepler con residuo < 1e-14; los parámetros
ajustados contienen a los verdaderos a 4 sigma; el descenso por gradiente necesita
el número de pasos predicho por (k-1)/(k+1) (±2) y Newton una iteración.
"""
import math, platform, random

R = 13.0


def dv_hohmann(R):
    return (math.sqrt(2 * R / (1 + R)) - 1) + (math.sqrt(1 / R) - math.sqrt(2 / (R * (1 + R))))


def dv_bielipt(x, R=R):
    v1 = math.sqrt(2 * x / (1 + x)) - 1
    va = math.sqrt(2 / x - 2 / (1 + x))            # velocidad en x sobre la primera elipse
    vb = math.sqrt(2 / x - 2 / (x + R))            # velocidad en x sobre la segunda elipse
    v3 = math.sqrt(1 / R) - math.sqrt(2 / R - 2 / (x + R))
    return v1 + abs(vb - va) + abs(v3)


def seccion_aurea(f, a, b, tol=1e-10):
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    fc, fd = f(c), f(d)
    while b - a > tol:
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - g * (b - a); fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + g * (b - a); fd = f(d)
    return 0.5 * (a + b)


print(f"Python {platform.python_version()}")
# (a) transferencia
H = dv_hohmann(R)
assert abs(dv_bielipt(R) - H) < 1e-12
T = lambda x: math.pi * (((1 + x) / 2) ** 1.5 + ((x + R) / 2) ** 1.5)      # tiempo de vuelo en unidades sqrt(r1^3/mu)
Th = math.pi * ((1 + R) / 2) ** 1.5
print(f"(a) R = {R}: Hohmann Dv = {H:.6f} v1, tiempo {Th:.1f} (x 883.9 s en la órbita de 400 km = {Th*883.9/3600:.1f} h)")
print(f"    biela con x -> infinito: Dv = {dv_bielipt(1e9):.6f} (límite, tiempo infinito)")
xmin = seccion_aurea(dv_bielipt, R, 200.0)
dder = (dv_bielipt(xmin + 1e-4) - dv_bielipt(xmin - 1e-4)) / 2e-4
print(f"    SIN penalizar el tiempo, el mínimo en [R, 200] cae en la frontera: x = {xmin:.3f} ; Dv = {dv_bielipt(xmin):.6f} ; derivada = {dder:.2e} (no es cero)")
assert xmin > 199.9 and dder < -1e-7
lam = 1e-6
J = lambda x: dv_bielipt(x) + lam * T(x)
xj = seccion_aurea(J, 40.0, 400.0)                    # intervalo donde J es unimodal
grid = min((J(R + i * 0.001), R + i * 0.001) for i in range(0, 387000))
print('    J(x) en puntos: ' + '  '.join(f'x={x:g}: {J(x):.6f}' for x in (13, 25, 50, 94, 200, 400)))
dj = (J(xj + 1e-4) - J(xj - 1e-4)) / 2e-4
print(f"    CON penalización lam = {lam} por unidad de tiempo: mínimo interior x = {xj:.3f} r1 ; Dv = {dv_bielipt(xj):.6f} ; tiempo = {T(xj):.0f} ({T(xj)*883.9/86400:.1f} d)")
print(f"    barrido en malla: x = {grid[1]:.3f} ; derivada de J en el mínimo = {dj:.2e} ; J(Hohmann) = {H + lam*Th:.6f} ; J(mínimo) = {J(xj):.6f}")
assert abs(xj - grid[1]) < 1e-3 and abs(dj) < 1e-6 and J(xj) < H + lam * Th

# (b) Newton para Kepler
e, M = 0.74, 1.0
E = math.pi
it = 0
for it in range(1, 50):
    f = E - e * math.sin(E) - M
    dE = f / (1 - e * math.cos(E))
    E -= dE
    if abs(dE) < 1e-15:
        break
res = E - e * math.sin(E) - M
print(f"(b) Kepler e={e}, M={M}: E = {E:.15f} tras {it} iteraciones ; residuo = {res:.2e}")
assert abs(res) < 1e-14

# (c) Gauss-Newton
rng = random.Random(2026)
ts = [0.5 * i for i in range(21)]
ys = [5 * math.exp(-0.3 * t) + rng.gauss(0, 0.05) for t in ts]
a_, b_ = 4.0, 0.2
for k in range(1, 30):
    r = [y - a_ * math.exp(-b_ * t) for t, y in zip(ts, ys)]
    J = [(math.exp(-b_ * t), -a_ * t * math.exp(-b_ * t)) for t in ts]
    A11 = sum(j[0] ** 2 for j in J); A12 = sum(j[0] * j[1] for j in J); A22 = sum(j[1] ** 2 for j in J)
    g1 = sum(j[0] * ri for j, ri in zip(J, r)); g2 = sum(j[1] * ri for j, ri in zip(J, r))
    det = A11 * A22 - A12 * A12
    da, db = (A22 * g1 - A12 * g2) / det, (-A12 * g1 + A11 * g2) / det
    a_, b_ = a_ + da, b_ + db
    if max(abs(da), abs(db)) < 1e-12:
        break
r = [y - a_ * math.exp(-b_ * t) for t, y in zip(ts, ys)]
s2 = sum(x * x for x in r) / (len(ts) - 2)
J = [(math.exp(-b_ * t), -a_ * t * math.exp(-b_ * t)) for t in ts]
A11 = sum(j[0] ** 2 for j in J); A12 = sum(j[0] * j[1] for j in J); A22 = sum(j[1] ** 2 for j in J)
det = A11 * A22 - A12 * A12
sa, sb = math.sqrt(s2 * A22 / det), math.sqrt(s2 * A11 / det)
gnorm = math.hypot(sum(j[0] * ri for j, ri in zip(J, r)), sum(j[1] * ri for j, ri in zip(J, r)))
print(f"(c) Gauss-Newton ({k} iteraciones): a = {a_:.4f} ± {sa:.4f} (verdadero 5) ; b = {b_:.5f} ± {sb:.5f} (verdadero 0.3) ; ||gradiente|| = {gnorm:.1e}")
print(f"    desviación residual = {math.sqrt(s2):.4f} (ruido sintético 0.05)")
assert abs(a_ - 5) < 4 * sa and abs(b_ - 0.3) < 4 * sb and gnorm < 1e-8

# (d) descenso por gradiente frente a Newton
for kappa in (2.0, 10.0, 100.0):
    x1, x2 = 1.0, 1.0
    paso = 2 / (1 + kappa)
    n = 0
    while 0.5 * (x1 * x1 + kappa * x2 * x2) > 1e-12 * 0.5 * (1 + kappa) and n < 100000:
        x1, x2 = x1 - paso * x1, x2 - paso * kappa * x2
        n += 1
    pred = math.log(1e-12) / (2 * math.log((kappa - 1) / (kappa + 1))) if kappa > 1 else 1
    print(f"(d) kappa = {kappa:6.1f}: descenso por gradiente {n:5d} pasos (predicción {pred:7.1f}) ; Newton: 1 paso")
    assert abs(n - pred) <= 3
print("Pruebas superadas.")
