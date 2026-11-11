#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C24: limites de la experimentacion educativa con cohetes pequenos: impulso, apogeo con y sin resistencia y distancia de seguridad (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no sustituye la reglamentacion aeronautica ni el codigo de seguridad de ninguna asociacion ni autoridad. No es una guia para construir motores.
Texto consultado (2026-11-11): art. VI del tratado de 1967 (nota legal.un.org): las actividades de entidades no gubernamentales requieren autorizacion y supervision continua del Estado.
NO consultado: reglamentacion de aeronautica civil de ningun pais, codigos de seguridad de cohetes aficionados ni clasificacion oficial de motores; la clasificacion por impulso total
(cada letra duplica el rango: A <= 2.5 N s, B <= 5, C <= 10, D <= 20, E <= 40 ...) es una convencion conocida NO verificada en esta sesion. La regla "distancia de seguridad = 0.5 x apogeo" es ILUSTRATIVA.
Modelo: cohete de masa m = 0.10 kg al despegue, empuje constante F = I/t_b durante t_b = 1.0 s (motor representado solo por su impulso total I y tiempo de combustion; masa constante, simplificacion),
resistencia 0.5 rho Cd A v^2 con rho = 1.225 kg/m^3, A = 3.0e-3 m^2, Cd = 0.5; g = 9.80665 m/s^2; integracion RK4 con paso 1e-3 s.
Verificacion: con Cd = 0 el apogeo numerico debe igualar el analitico (error relativo < 0.1 % (el salto de empuje en t = 1 s limita la precision de RK4)).
"""
import json, math, platform

G, RHO, AREA, M, TB = 9.80665, 1.225, 3.0e-3, 0.10, 1.0

def apogeo(impulso, cd, dt=1e-3):
    F = impulso / TB
    def acel(t, v):
        emp = F if t < TB else 0.0
        return (emp - 0.5 * RHO * cd * AREA * abs(v) * v) / M - G
    t, y, v = 0.0, 0.0, 0.0
    ymax = 0.0
    while True:
        k1v = acel(t, v);               k1y = v
        k2v = acel(t + dt / 2, v + dt / 2 * k1v); k2y = v + dt / 2 * k1v
        k3v = acel(t + dt / 2, v + dt / 2 * k2v); k3y = v + dt / 2 * k2v
        k4v = acel(t + dt, v + dt * k3v);  k4y = v + dt * k3v
        v += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        y += dt / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
        t += dt
        ymax = max(ymax, y)
        if t > TB and v <= 0:
            return ymax, t

def analitico_sin_arrastre(impulso):
    a = impulso / TB / M - G                # aceleracion neta durante la combustion
    vb = a * TB; yb = 0.5 * a * TB ** 2
    return yb + vb ** 2 / (2 * G)

print("Python", platform.python_version(), "(biblioteca estandar)")
print("Cohete SINTETICO de 0.10 kg; art. VI consultado (2026-11-11); reglamentacion y clasificacion de motores NO consultadas.")
print("  clase  impulso [N s]  apogeo sin arrastre [m]  numerico Cd=0   apogeo con Cd=0.5 [m]  distancia de seguridad ilustrativa [m]")
res = {}
for clase, imp in (("A", 2.5), ("B", 5.0), ("C", 10.0), ("D", 20.0)):
    a0, _ = apogeo(imp, 0.0)
    an = analitico_sin_arrastre(imp)
    assert abs(a0 - an) < 1e-3 * an, (clase, a0, an)
    a1, _ = apogeo(imp, 0.5)
    res[clase] = (an, a1)
    print(f"{clase:6s} {imp:12.1f} {an:24.1f} {a0:14.1f} {a1:20.1f} {0.5 * a1:30.1f}")
# autorizacion: un experimento que supera una altura de 150 m exige revisar la reglamentacion (umbral ILUSTRATIVO)
UMBRAL = 150.0
excede = [c for c, (an, a1) in res.items() if a1 > UMBRAL]
print(f"Clases cuyo apogeo con arrastre supera {UMBRAL:.0f} m (umbral ILUSTRATIVO): {excede}")
print("CLAVES " + json.dumps({"aB": "%.1f" % res["B"][1], "aC": "%.1f" % res["C"][1], "aD": "%.1f" % res["D"][1], "anD": "%.1f" % res["D"][0], "sD": "%.1f" % (0.5 * res["D"][1]), "ex": ",".join(excede), "aA": "%.1f" % res["A"][1], "anA": "%.1f" % res["A"][0]}))
print("Pruebas superadas.")
