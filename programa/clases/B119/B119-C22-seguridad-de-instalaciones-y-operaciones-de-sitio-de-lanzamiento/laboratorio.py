#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C22: seguridad de un sitio de lanzamiento: alcance de fragmentos y radio de exclusion para un riesgo colectivo ilustrativo (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no sustituye un analisis de seguridad de rango ni la normativa de ninguna autoridad.
Texto consultado (2026-11-11): art. VI del tratado de 1967 (nota legal.un.org): el Estado responde por las actividades privadas y exige autorizacion y supervision continua; arts. II-III de la Convencion
de Responsabilidad (resumen de busqueda UNOOSA): responsabilidad absoluta por danos en la superficie. NO consultado: ninguna norma de seguridad de rango ni criterio de riesgo publicado;
el umbral de 1e-4 de esperanza de bajas es ILUSTRATIVO.
Modelo (no consultado en una fuente concreta; verificado por Monte Carlo): fragmento lanzado a 45 grados sin resistencia del aire (cota superior): alcance R = v^2 / g, g = 9.80665 m/s^2;
velocidad v lognormal de mediana 70 m/s y sigma_ln = 0.4. Esperanza de bajas Ec = N_f * P(R > r) * (A_c * rho), con N_f = 200 fragmentos, A_c = 0.5 m^2 de area expuesta por persona
y rho = 1e-4 personas/m^2 (100 por km^2) fuera del radio de exclusion r. SINTETICO. Semilla 119; N = 400000.
Tolerancia: P(R > r) analitica (erf) vs Monte Carlo a 3 sigma.
"""
import json, math, platform, random

G = 9.80665
MED, SIG = 70.0, 0.4
NF, AC, RHO = 200, 0.5, 1e-4
UMBRAL = 1e-4

def p_supera(r):
    """P(R > r) con R = v^2/g y v lognormal."""
    v = math.sqrt(G * r)
    z = (math.log(v) - math.log(MED)) / SIG
    return 0.5 * math.erfc(z / math.sqrt(2))
def ec(r):
    return NF * p_supera(r) * AC * RHO
rng = random.Random(119)
N = 400000
rs = [(rng.lognormvariate(math.log(MED), SIG)) ** 2 / G for _ in range(N)]
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Fragmentos y poblacion SINTETICOS; art. VI y Convencion de Responsabilidad consultados (2026-11-11); ninguna norma de rango consultada; umbral 1e-4 ILUSTRATIVO.")
print(f"Alcance mediano (sin resistencia): {MED ** 2 / G:.0f} m")
print("  r [m]    P(R>r) analitica   Monte Carlo     Ec")
for r in (1000.0, 2500.0, 5000.0, 8000.0, 12000.0):
    mc = sum(1 for x in rs if x > r) / N
    an = p_supera(r)
    sg = math.sqrt(max(an * (1 - an), 1e-12) / N)
    assert abs(mc - an) < 3 * sg + 1e-5, r
    print(f"{r:7.0f} {an:16.5f} {mc:12.5f} {ec(r):11.2e}")
lo, hi = 100.0, 100000.0
for _ in range(80):
    mid = math.sqrt(lo * hi)
    if ec(mid) > UMBRAL: lo = mid
    else: hi = mid
r_ex = hi
print(f"Radio de exclusion que da Ec <= {UMBRAL:.0e}: {r_ex:.0f} m = {r_ex / 1000:.2f} km")
assert abs(ec(r_ex) - UMBRAL) / UMBRAL < 1e-6
# si la poblacion alrededor se duplica
rho2 = 2 * RHO
def ec2(r): return NF * p_supera(r) * AC * rho2
lo, hi = 100.0, 100000.0
for _ in range(80):
    mid = math.sqrt(lo * hi)
    if ec2(mid) > UMBRAL: lo = mid
    else: hi = mid
print(f"Con el doble de poblacion: radio {hi:.0f} m (+{100 * (hi / r_ex - 1):.1f} %)")
print("CLAVES " + json.dumps({"med": "%.0f" % (MED ** 2 / G), "rex": "%.0f" % r_ex, "rexk": "%.2f" % (r_ex / 1000), "r2": "%.0f" % hi, "inc": "%.1f" % (100 * (hi / r_ex - 1)), "p5": "%.5f" % p_supera(5000.0), "ec5": "%.2e" % ec(5000.0)}))
print("Pruebas superadas.")
