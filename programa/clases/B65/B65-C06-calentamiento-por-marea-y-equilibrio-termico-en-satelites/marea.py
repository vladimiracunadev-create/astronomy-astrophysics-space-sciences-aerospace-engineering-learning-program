#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B65-C06: calentamiento por marea de un satelite sincrono en orbita excentrica.

Datos consultados (consulta 2026-11-09): G = 6.67430e-11 m^3 kg^-1 s^-2 y sigma_SB = 5.670374419e-8 W m^-2 K^-4 (NIST, CODATA 2022);
masa de Jupiter 1898.13e24 kg (NASA/GSFC NSSDC, Jupiter Fact Sheet, 2024-10-02); masa, diametro, semieje, periodo y excentricidad de Io, Europa, Ganymede y Callisto
(NASA/GSFC NSSDC, Jovian Satellite Fact Sheet, 2023-12-06; las excentricidades de la hoja estan redondeadas a 0.001).
Datos ILUSTRATIVOS (sinteticos, no medidos): k2 = 1.5 y Q = 100 iguales para los cuatro satelites (k2/Q = 0.015).
Modelo: (1) formula de Peale, E = (21/2) (k2/Q) G Mp^2 R^5 n e^2 / a^6 (la expresion NO se consulto en una fuente; se verifica numericamente aqui);
(2) integracion numerica: tensor de cuadrupolo Q_ij del satelite en su sistema fijo, que relaja hacia el equilibrio con retardo tau = 1/(Q n):
dQ/dt = (Q_eq - Q)/tau, Q_eq = k2 R^5/(3G) (G Mp / r^3)(3 r r - I), rigidez K = 3G/(2 k2 R^5), potencia disipada P = K tau <|dQ/dt|^2> (suma de los cuadrados de todas las componentes);
orbita kepleriana con rotacion sincrona constante n. Se comprueba tambien P = <F:dQ/dt>.
(3) equilibrio: flujo = P/(4 pi R^2) y temperatura T = (flujo/sigma)^(1/4) si todo el calor se irradiara.
Sistema de referencia: el del satelite (un eje hacia el pericentro); unidades SI. Supuestos: rotacion sincrona exacta sin libracion fisica, un solo parametro de respuesta, orbita fija.
Validez: ilustrativa; no se ajusta ningun satelite. Tolerancia: integracion frente a la formula < 1 % para e = 0.004 y Q = 100.
"""
from __future__ import annotations
import math, platform

G, SIG_SB = 6.67430e-11, 5.670374419e-8
MP = 1898.13e24
K2, QF = 1.5, 100.0
CUERPOS = {  # masa [kg], diametro [km], semieje [km], periodo [d], excentricidad (hoja, redondeada)
    "Io": (893.2e20, 3643.0, 421.8e3, 1.769138, 0.004),
    "Europa": (480.0e20, 3121.6, 671.1e3, 3.551181, 0.009),
    "Ganymede": (1481.9e20, 5262.4, 1070.4e3, 7.154553, 0.001),
    "Callisto": (1075.9e20, 4820.6, 1882.7e3, 16.689017, 0.007),
}

def peale(ms, R, a, e):
    n = math.sqrt(G * (MP + ms) / a**3)
    return 10.5 * (K2 / QF) * G * MP**2 * R**5 * n * e * e / a**6, n

def kepler(M, e):
    E = M if e < 0.8 else math.pi
    for _ in range(50):
        d = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        E -= d
        if abs(d) < 1e-14:
            break
    return E

def potencia_numerica(ms, R, a, e, pasos=20000, periodos_transitorio=4, periodos_medida=2):
    n = math.sqrt(G * (MP + ms) / a**3)
    T = 2 * math.pi / n
    tau = 1.0 / (QF * n)
    Kr = 3 * G / (2 * K2 * R**5)
    c = K2 * R**5 / (3 * G)
    dt = T / pasos

    def eq(t):
        M = n * t
        E = kepler(M % (2 * math.pi), e)
        f = 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))
        r = a * (1 - e * math.cos(E))
        phi = f - M                       # direccion del planeta en el sistema fijo al satelite
        cx, sy = math.cos(phi), math.sin(phi)
        s = c * G * MP / r**3
        # componentes (xx, xy, yy, zz) de s (3 r r - I)
        return (s * (3 * cx * cx - 1), s * 3 * cx * sy, s * (3 * sy * sy - 1), -s), r, (cx, sy)

    def deriv(t, q):
        qe, _, _ = eq(t)
        return tuple((qe[i] - q[i]) / tau for i in range(4))

    q = eq(0.0)[0]
    t = 0.0
    suma_p, suma_w, cuenta = 0.0, 0.0, 0
    total = (periodos_transitorio + periodos_medida) * pasos
    for paso in range(total):
        k1 = deriv(t, q)
        k2 = deriv(t + dt / 2, tuple(q[i] + dt / 2 * k1[i] for i in range(4)))
        k3 = deriv(t + dt / 2, tuple(q[i] + dt / 2 * k2[i] for i in range(4)))
        k4 = deriv(t + dt, tuple(q[i] + dt * k3[i] for i in range(4)))
        if paso >= periodos_transitorio * pasos:
            qd = deriv(t, q)
            _, r, (cx, sy) = eq(t)
            suma_p += Kr * tau * (qd[0]**2 + 2 * qd[1]**2 + qd[2]**2 + qd[3]**2)
            fpref = 3 * G * MP / (2 * r**3)
            suma_w += fpref * (cx * cx * qd[0] + 2 * cx * sy * qd[1] + sy * sy * qd[2])
            cuenta += 1
        q = tuple(q[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4))
        t += dt
    return suma_p / cuenta, suma_w / cuenta

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Formula de Peale con k2/Q = 0.015 ilustrativo:")
    print(" cuerpo     R [km]   n [rad/s]   periodo calc. [d] (hoja)       e      E [TW]   flujo [mW/m^2]   T_eq [K]")
    for nom, (ms, d_km, a_km, p_d, e) in CUERPOS.items():
        R, a = d_km * 500.0, a_km * 1e3
        E, n = peale(ms, R, a, e)
        per = 2 * math.pi / n / 86400.0
        fl = E / (4 * math.pi * R**2)
        teq = (fl / SIG_SB) ** 0.25
        print(f" {nom:9s} {R/1e3:7.1f} {n:11.4e} {per:8.4f} ({p_d:.4f}) {e:8.3f} {E/1e12:9.3f} {fl*1e3:14.2f} {teq:9.1f}")
    ms, d_km, a_km, p_d, e = CUERPOS["Io"]
    R, a = d_km * 500.0, a_km * 1e3
    Ef, _ = peale(ms, R, a, e)
    Pn, Pw = potencia_numerica(ms, R, a, e)
    print(f"\nIo (e = {e}): formula = {Ef/1e12:.4f} TW ; integracion numerica P = {Pn/1e12:.4f} TW ; <F:dQ/dt> = {Pw/1e12:.4f} TW")
    print(f"  cociente numerico/formula = {Pn/Ef:.5f} ; diferencia entre las dos formas de la potencia = {abs(Pn-Pw)/Pn:.2e}")
    for ee in (0.002, 0.008):
        Ee, _ = peale(ms, R, a, ee)
        Pe, _ = potencia_numerica(ms, R, a, ee)
        print(f"  e = {ee}: formula = {Ee/1e12:.4f} TW ; numerico = {Pe/1e12:.4f} TW ; cociente = {Pe/Ee:.5f}")
    ok = abs(Pn / Ef - 1) < 0.01 and abs(Pn - Pw) / Pn < 1e-2
    assert ok
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
