#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C35: gobernanza de datos espaciales: politica de acceso por niveles y compromiso privacidad-utilidad con el mecanismo de Laplace (datos SINTETICOS).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no sustituye una politica de datos ni la normativa de proteccion de datos.
Texto consultado (2026-11-11): Convenio de Registro (UNOOSA), art. III: el registro central de la ONU es de acceso abierto; art. XI del tratado de 1967 (nota legal.un.org): informar al publico y a la comunidad
cientifica en la mayor medida posible. NO consultado: ninguna norma de proteccion de datos, politica de datos de agencia ni control de exportacion.
Mecanismo de Laplace (no consultado en una fuente concreta; verificado por Monte Carlo): para una consulta de conteo con sensibilidad 1, ruido Laplace(0, 1/eps) da privacidad diferencial eps; el error absoluto medio es 1/eps.
SINTETICO: 5000 registros de acceso a estaciones terrenas con una caracteristica binaria "acceso fuera de horario" (prevalencia 0.08); semilla 119; N = 20000 repeticiones por eps.
Politica: 3 roles (publico, socio, operador) x 3 niveles de datos (abierto, restringido, reservado); permitido si nivel_del_rol >= nivel_del_dato.
Tolerancia: error absoluto medio del ruido == 1/eps a 3 %.
"""
import json, math, platform, random

rng = random.Random(119)
NIV = {"abierto": 0, "restringido": 1, "reservado": 2}
ROLES = {"publico": 0, "socio": 1, "operador": 2}
permit = {(r, d): ROLES[r] >= NIV[d] for r in ROLES for d in NIV}
n_ok = sum(permit.values())
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Datos SINTETICOS; art. III del Convenio de Registro y art. XI consultados 2026-11-11; normas de proteccion de datos NO consultadas.")
print("Politica de acceso (filas: rol; columnas: abierto, restringido, reservado):")
for r in ROLES:
    print(f"   {r:9s}", [int(permit[(r, d)]) for d in NIV])
print(f"Pares permitidos: {n_ok} de 9")
assert n_ok == 6
N_REG = 5000
datos = [1 if rng.random() < 0.08 else 0 for _ in range(N_REG)]
verdad = sum(datos)
def laplace(b):
    u = rng.random() - 0.5
    return -b * math.copysign(1.0, u) * math.log(1 - 2 * abs(u))
print(f"Conteo verdadero de accesos fuera de horario: {verdad} de {N_REG}")
print("  eps    error abs. medio   1/eps    error relativo medio del conteo")
res = {}
for eps in (0.05, 0.1, 0.5, 1.0, 2.0):
    errs = [abs(laplace(1.0 / eps)) for _ in range(20000)]
    m = sum(errs) / len(errs)
    assert abs(m - 1.0 / eps) / (1.0 / eps) < 0.03, eps
    res[eps] = m
    print(f"{eps:5.2f} {m:14.3f} {1.0 / eps:8.3f} {100 * m / verdad:14.2f} %")
# eps minimo para que el error medio sea <= 1 % del conteo
eps_min = 1.0 / (0.01 * verdad)
print(f"eps minimo para error medio <= 1 % del conteo ({verdad}): {eps_min:.3f}")
print("CLAVES " + json.dumps({"ok": n_ok, "v": verdad, "e01": "%.3f" % res[0.1], "e1": "%.3f" % res[1.0], "e005": "%.3f" % res[0.05], "r1": "%.2f" % (100 * res[1.0] / verdad), "emin": "%.3f" % eps_min, "r005": "%.2f" % (100 * res[0.05] / verdad)}))
print("Pruebas superadas.")
