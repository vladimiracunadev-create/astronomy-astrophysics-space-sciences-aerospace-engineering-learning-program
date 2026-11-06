#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B23-C06: pruebas metamórficas de un propagador con J2 (sin solución exacta).

Datos: SINTÉTICOS. Satélite en órbita baja: r0 = (7000, 0, 0) km, v0 = (0, 5.3, 5.95) km/s
(inclinación del orden de 48°; valores de ejemplo, no un satélite real).
Constantes: mu = 3.986004e14 m^3/s^2 (IAU 2015 B3, nominal terrestre) = 398600.4 km^3/s^2;
R = 6378.137 km y J2 = 1082.63e-6 (NASA NSSDC Earth Fact Sheet, actualizada 2024-11-15).
Modelo: gravedad central + J2 (Tierra axisimétrica, eje z); integración DOP853.
Unidades del programa: km, s, km/s.
Supuestos: sin atmósfera, sin Luna ni Sol, sin armónicos superiores.
Validez: arcos de horas a un día. No hay solución exacta: se usan relaciones entre ejecuciones.
Tolerancia: se ESTIMA del propio integrador (diferencia entre rtol 1e-11 y 1e-13) y se
multiplica por un factor de seguridad declarado (x50).
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp

MU, RE, J2 = 398600.4, 6378.137, 1082.63e-6


def aceleracion(r, mu=MU, re=RE, j2=J2, defecto=None):
    x, y, z = r
    n = np.linalg.norm(r)
    k = -1.5*j2*mu*re**2/n**5
    zz = 5*z*z/n**2
    fx, fy, fz = (1 - zz), (1 - zz), (3 - zz)
    if defecto == "signo":
        k = -k
    elif defecto == "az":
        fz = (1 - zz)                      # factor de a_z mal (debe ser 3 - 5z²/r²)
    elif defecto == "unid":
        k = -1.5*j2*mu*RE**2/n**5           # defecto: R fijo en km aunque el programa trabaje en m
    elif defecto == "asim" and x < 0:
        fx = -fx                           # error solo para x < 0
    a = -mu*r/n**3 + k*np.array([x*fx, y*fy, z*fz])
    return a


def propagar(r0, v0, T, rtol=1e-11, defecto=None, mu=MU, re=RE, reloj=False, t0=0.0):
    def f(t, y):
        d = defecto
        a = aceleracion(y[:3], mu, re, J2, d)
        if d == "reloj":                   # defecto: reloj que ignora el instante inicial t0
            a = a*(1 + 1e-6*t/21600.0)
        return np.concatenate([y[3:], a])
    s = solve_ivp(f, (0.0, T), np.concatenate([r0, v0]), method="DOP853", rtol=rtol, atol=rtol*1e-3)
    return s.y[:3, -1], s.y[3:, -1]


def rot(eje, ang):
    c, s = math.cos(ang), math.sin(ang)
    if eje == "z":
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
    return np.array([[1.0, 0, 0], [0, c, -s], [0, s, c]])


def dist(a, b):
    return float(np.linalg.norm(a - b))


def relaciones(defecto, ruido):
    r0 = np.array([7000.0, 0.0, 0.0]); v0 = np.array([0.0, 5.3, 5.95])
    T = 21600.0
    tol = 50*ruido
    P = lambda r, v, T_, **k: propagar(r, v, T_, defecto=defecto, **k)
    rb, vb = P(r0, v0, T)
    out = {}
    # MR1 composición: propagar T/3 y luego 2T/3 = propagar T
    r1, v1 = P(r0, v0, T/3)
    r2, _ = P(r1, v1, 2*T/3, t0=T/3)
    out["composición"] = dist(r2, rb)
    # MR2 giro alrededor de z (simetría de J2)
    R = rot("z", math.radians(37))
    rr, _ = P(R @ r0, R @ v0, T)
    out["giro z"] = dist(rr, R @ rb)
    # MR3 giro alrededor de x (NO es simetría de J2)
    Rx = rot("x", math.radians(37))
    rx, _ = P(Rx @ r0, Rx @ v0, T)
    out["giro x (no vale)"] = dist(rx, Rx @ rb)
    # MR4 reflexión z -> -z (simetría ecuatorial)
    S = np.diag([1.0, 1.0, -1.0])
    rs, _ = P(S @ r0, S @ v0, T)
    out["reflexión z"] = dist(rs, S @ rb)
    # MR5 unidades: km -> m (mu en m^3/s^2, R en m)
    rm, _ = propagar(r0*1e3, v0*1e3, T, defecto=defecto, mu=MU*1e9, re=RE*1e3)
    out["unidades km->m"] = dist(rm, rb*1e3)/1e3        # error en km
    
    # MR6 reversibilidad
    rv, _ = P(rb, -vb, T, t0=T) if False else P(*(rb, -vb), T)
    out["reversibilidad"] = dist(rv, r0)
    # propiedad de C02 (no metamórfica): deriva de energía con el potencial de J2
    def en(r, v):
        n = np.linalg.norm(r)
        return 0.5*(v @ v) - MU/n*(1 - J2*(RE/n)**2*(3*r[2]**2/n**2 - 1)/2)
    out["energía (C02)"] = abs(en(rb, vb) - en(r0, v0))/abs(en(r0, v0))
    return out, tol


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  SciPy {scipy.__version__}")
    r0 = np.array([7000.0, 0.0, 0.0]); v0 = np.array([0.0, 5.3, 5.95])
    ra, _ = propagar(r0, v0, 21600.0, rtol=1e-11)
    rb_, _ = propagar(r0, v0, 21600.0, rtol=1e-13)
    ruido = dist(ra, rb_)
    print(f"ruido del integrador (rtol 1e-11 vs 1e-13) tras 6 h: {ruido:.2e} km; tolerancia = 50 x ruido = {50*ruido:.2e} km")
    ra0, _ = propagar(r0, v0, 21600.0, rtol=1e-11)
    # J2 -> 0 : se recupera el movimiento kepleriano (relación límite)
    def kep(rtol=1e-11):
        f = lambda t, y: np.concatenate([y[3:], -MU*y[:3]/np.linalg.norm(y[:3])**3])
        s = solve_ivp(f, (0, 21600.0), np.concatenate([r0, v0]), method="DOP853", rtol=rtol, atol=rtol*1e-3)
        return s.y[:3, -1]
    d_j2 = dist(ra0, kep())
    print(f"efecto de J2 en 6 h: {d_j2:.3f} km de diferencia con dos cuerpos")

    casos = ["ninguno", "signo", "az", "asim", "reloj", "unid"]
    nombres = None
    tabla = {}
    for c in casos:
        res, tol = relaciones(None if c == "ninguno" else c, ruido)
        if c == "reloj":
            pass
        tabla[c] = (res, tol)
        nombres = list(res)
    print(f"\ndistancia entre las dos ejecuciones comparadas [km] (tolerancia {tabla['ninguno'][1]:.1e} km)")
    print(f"{'versión':<10}" + "".join(f"{n:>18}" for n in nombres))
    for c in casos:
        res, tol = tabla[c]
        print(f"{c:<10}" + "".join(f"{res[n]:>18.2e}" for n in nombres))
    tol = tabla["ninguno"][1]
    TOL_E = 1e-9
    umbral = lambda n: TOL_E if n.startswith("energía") else tol
    print(f"\ndetecta (distancia > tolerancia; energía: > {TOL_E:.0e} relativo):")
    for c in casos:
        res, _ = tabla[c]
        det = [n for n in nombres if n != "giro x (no vale)" and res[n] > umbral(n)]
        print(f"  {c:<10}: {det or '— (sobrevive)'}")
    ok = tabla["ninguno"][0]
    for n in nombres:
        if n != "giro x (no vale)":
            prueba(ok[n] <= umbral(n), f"la versión correcta cumple {n}")
    prueba(ok["giro x (no vale)"] > 1.0, "el giro alrededor de x NO es simetría: debe fallar en la versión correcta")
    metam = [n for n in nombres if n not in ("giro x (no vale)", "energía (C02)", "reversibilidad")]
    for c in ("signo", "az"):
        prueba(all(tabla[c][0][n] <= tol for n in metam), f"{c} sobrevive a las relaciones")
        prueba(tabla[c][0]["energía (C02)"] > TOL_E, f"{c} lo detecta la energía")
    prueba(tabla["asim"][0]["giro z"] > tol, "la asimetría rompe el giro alrededor de z")
    prueba(tabla["reloj"][0]["composición"] > tol, "el reloj reiniciado rompe la composición")
    prueba(tabla["unid"][0]["unidades km->m"] > tol, "el defecto de unidades lo ve la relación de unidades")
    print("\nPruebas superadas.")


if __name__ == "__main__":
    main()
