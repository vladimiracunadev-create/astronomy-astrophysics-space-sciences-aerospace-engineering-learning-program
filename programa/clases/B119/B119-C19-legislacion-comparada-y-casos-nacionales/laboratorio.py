#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C19: legislacion comparada: matriz de rasgos de cinco regimenes SINTETICOS y similitud de Jaccard.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, nota de legal.un.org): art. VI del Tratado del Espacio Ultraterrestre: las actividades privadas requieren autorizacion y supervision continua del Estado;
Convenio de Registro (UNOOSA), art. II: el contenido del registro nacional lo fija cada Estado. NO consultada: la legislacion de ningun Estado real.
Los regimenes "Alfa" a "Epsilon" son INVENTADOS: no corresponden a ningun pais ni representan ninguna ley real. Doce rasgos binarios (1 = el regimen lo exige).
Metrica: similitud de Jaccard J(a,b) = |a AND b| / |a OR b|; distancia d = 1 - J.
Verificaciones: J(a,a) = 1; simetria; desigualdad triangular de d en todas las ternas (la distancia de Jaccard es una metrica).
"""
import itertools, json, platform

RASGOS = ["licencia_previa", "seguro_obligatorio", "tope_de_responsabilidad", "registro_nacional", "plan_de_desechos", "supervision_continua",
          "evaluacion_ambiental", "control_de_exportacion", "cooperacion_con_regulador_extranjero", "inspecciones", "garantia_financiera", "reglas_de_datos"]
R = {
    "Alfa":    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    "Beta":    [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    "Gamma":   [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    "Delta":   [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    "Epsilon": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
}
def jac(a, b):
    inter = sum(x & y for x, y in zip(a, b)); uni = sum(x | y for x, y in zip(a, b))
    return inter / uni
N = list(R)
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Regimenes INVENTADOS (Alfa a Epsilon), 12 rasgos binarios; art. VI y art. II del Convenio de Registro consultados 2026-11-11; ninguna ley real consultada.")
print("          " + "".join(f"{n:>9s}" for n in N))
for a in N:
    print(f"{a:9s} " + "".join(f"{jac(R[a], R[b]):9.3f}" for b in N))
for a in N: assert jac(R[a], R[a]) == 1
for a, b in itertools.combinations(N, 2): assert jac(R[a], R[b]) == jac(R[b], R[a])
for a, b, c in itertools.permutations(N, 3):
    assert (1 - jac(R[a], R[c])) <= (1 - jac(R[a], R[b])) + (1 - jac(R[b], R[c])) + 1e-12
par = max(itertools.combinations(N, 2), key=lambda p: jac(R[p[0]], R[p[1]]))
lejos = min(itertools.combinations(N, 2), key=lambda p: jac(R[p[0]], R[p[1]]))
print(f"Par mas parecido: {par[0]}-{par[1]} (J = {jac(R[par[0]], R[par[1]]):.3f}) ; par mas distinto: {lejos[0]}-{lejos[1]} (J = {jac(R[lejos[0]], R[lejos[1]]):.3f})")
# rasgos comunes a todos y rasgos presentes en un solo regimen
comun = [r for i, r in enumerate(RASGOS) if all(R[n][i] for n in N)]
unico = [(r, [n for n in N if R[n][i]][0]) for i, r in enumerate(RASGOS) if sum(R[n][i] for n in N) == 1]
print("Rasgos exigidos por todos:", comun or "ninguno")
print("Rasgos exigidos por un solo regimen:", unico)
cuenta = {n: sum(R[n]) for n in N}
print("Numero de rasgos por regimen:", cuenta)
print("CLAVES " + json.dumps({"jmax": "%.3f" % jac(R[par[0]], R[par[1]]), "par": par[0] + "-" + par[1], "jmin": "%.3f" % jac(R[lejos[0]], R[lejos[1]]), "lej": lejos[0] + "-" + lejos[1], "nu": len(unico), "nA": cuenta["Alfa"], "nE": cuenta["Epsilon"], "ab": "%.3f" % jac(R["Alfa"], R["Beta"])}))
print("Pruebas superadas.")
