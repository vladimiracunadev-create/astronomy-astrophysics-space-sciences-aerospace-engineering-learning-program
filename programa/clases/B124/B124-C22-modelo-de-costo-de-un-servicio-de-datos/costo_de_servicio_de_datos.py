#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C22: modelo de costo de un servicio de datos (fijos, variables y escalones de capacidad), punto de equilibrio y precio, SINTETICO.

CONTENIDO EDUCATIVO: no es asesoria financiera ni de precios. Costos, volumenes y margenes son SINTETICOS.
Costo mensual: C(Q) = F + v Q + S ceil(Q / cap), con F = 50000 um de costos fijos (equipo, nube base, licencias), v = 5 um por producto entregado (computo, almacenamiento,
soporte) y S = 4000 um por servidor adicional de cap = 2000 productos por mes (costo escalonado).
Precio con margen sobre precio m = 25 %: p(Q) = C(Q) / Q / (1 - m). Punto de equilibrio con precio fijo p0 = 40 um: menor Q entero con p0 Q >= C(Q); la forma suave
(escalon amortizado en v' = v + S/cap) da Q'* = F / (p0 - v'). Demanda incierta Q ~ Normal(2500, 600) truncada a enteros >= 0:
P(utilidad > 0) por integracion de la funcion de masa discreta frente a Monte Carlo (200000, semilla 124).
Unidades: um por mes; productos por mes. Tolerancias: equilibrio exacto dentro de un escalon de la forma suave; probabilidad dentro de 0.005.
"""
import math, platform, random

F, V, S, CAP, M, P0 = 50000.0, 5.0, 4000.0, 2000, 0.25, 40.0
MU, SIG = 2500.0, 600.0


def costo(q):
    return F + V * q + S * math.ceil(q / CAP) if q > 0 else F


def utilidad(q, p=P0):
    return p * q - costo(q)


def precio(q):
    return costo(q) / q / (1 - M)


def equilibrio(p=P0):
    for q in range(1, 100000):
        if p * q >= costo(q):
            return q
    return None


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def prob_utilidad_positiva_integral():
    q0 = equilibrio()
    # utilidad(q) > 0 para q >= q0 si es monotona creciente en el rango; se verifica por conteo explicito
    ok = [q for q in range(0, 6000) if utilidad(q) > 0]
    masa = lambda q: phi((q + 0.5 - MU) / SIG) - phi((q - 0.5 - MU) / SIG)
    tot = sum(masa(q) for q in range(0, 6000))
    return sum(masa(q) for q in ok) / tot


def prob_utilidad_positiva_mc(rng, n=200000):
    cuenta = 0
    for _ in range(n):
        q = int(round(rng.gauss(MU, SIG)))
        if q < 0:
            q = 0
        if utilidad(q) > 0:
            cuenta += 1
    return cuenta / n


def run():
    q_ex = equilibrio()
    q_suave = F / (P0 - (V + S / CAP))
    rng = random.Random(124)
    p_int, p_mc = prob_utilidad_positiva_integral(), prob_utilidad_positiva_mc(rng)
    R = {"c_2500": costo(2500), "p_2500": precio(2500), "cm_2500": costo(2500) / 2500, "q_ex": q_ex, "q_suave": q_suave, "dif_q": abs(q_ex - q_suave),
         "u_2500": utilidad(2500), "p_int": p_int, "perd": 1 - p_int, "p_mc": p_mc, "dif_p": abs(p_int - p_mc), "p_1000": precio(1000), "p_5000": precio(5000), "p_1999": precio(1999), "p_2001": precio(2001),
         "salto": costo(2001) - costo(2000), "cm_1000": costo(1000) / 1000, "cm_5000": costo(5000) / 5000, "frac_fijo_2500": F / costo(2500), "margen_u_2500": utilidad(2500) / (P0 * 2500)}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"Servicio de datos SINTETICO: F = {F:.0f} um/mes, v = {V} um/producto, escalon S = {S:.0f} um por cada {CAP} productos, margen sobre precio = {100 * M:.0f} %, p0 = {P0} um")
    print(" Q (productos/mes)   costo total     costo medio   precio con margen")
    for q in (500, 1000, 1999, 2001, 2500, 5000):
        print(f" {q:15d} {costo(q):14.0f} {costo(q) / q:13.2f} {precio(q):13.2f}")
    print(f"Salto de costo al pasar de 2000 a 2001 productos = {R['salto']:.0f} um")
    print(f"Equilibrio con p0 = {P0}: exacto = {R['q_ex']} productos/mes ; forma suave F/(p0 - v - S/cap) = {R['q_suave']:.1f} ; diferencia = {R['dif_q']:.1f}")
    print(f"Q = 2500: costo medio = {R['cm_2500']:.2f} ; utilidad con p0 = {R['u_2500']:.0f} um/mes ({100 * R['margen_u_2500']:.1f} % del ingreso) ; fraccion de costo fijo = {100 * R['frac_fijo_2500']:.1f} %")
    print(f"P(utilidad > 0) con demanda Normal(2500, 600): integral = {R['p_int']:.4f} ; Monte Carlo = {R['p_mc']:.4f} ; diferencia = {R['dif_p']:.4f}")
    assert abs(R["q_ex"] - R["q_suave"]) < CAP and R["dif_p"] < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
