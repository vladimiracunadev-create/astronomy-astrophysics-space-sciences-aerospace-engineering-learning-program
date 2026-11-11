#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C32: interpretacion de tratados: ambiguedad de una clausula SINTETICA medida con entropia y efecto del contexto (lecturas de un panel ficticio).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no interpreta ningun tratado real.
Texto consultado (2026-11-11): pagina de UNOOSA del Acuerdo sobre la Luna, art. 11: "patrimonio comun de la humanidad", "regimen internacional" y "reparto equitativo" (parafraseado) como terminos cuyo alcance requiere interpretacion.
NO consultado: la Convencion de Viena sobre el Derecho de los Tratados (arts. 31-33), jurisprudencia ni doctrina; la regla general (buena fe, sentido corriente de los terminos en su contexto y a la luz del objeto y fin)
se menciona como CONOCIMIENTO GENERAL no verificado.
Modelo: una clausula SINTETICA ("el operador cooperara de manera razonable") con 4 lecturas posibles (L1 a L4). 40 lectores ficticios eligen una lectura bajo tres condiciones:
solo el texto, texto + contexto, texto + contexto + objeto y fin. Medida de ambiguedad: entropia de Shannon H = -sum p log2 p, en bits; maxima log2(4) = 2 bits.
Verificaciones: H(uniforme) = 2; H(degenerada) = 0; H(X|condicion) <= H(X) (la informacion adicional no aumenta la entropia).
"""
import json, math, platform

LECTURAS = ["L1 obligacion estricta", "L2 obligacion de medios", "L3 deber de informar", "L4 mera cortesia"]
CONDICIONES = {
    "solo el texto": [10, 12, 8, 10],
    "texto + contexto": [6, 18, 10, 6],
    "texto + contexto + objeto y fin": [3, 26, 9, 2],
}
def H(c):
    n = sum(c)
    return -sum((x / n) * math.log2(x / n) for x in c if x > 0)
assert abs(H([10, 10, 10, 10]) - 2.0) < 1e-12 and H([40, 0, 0, 0]) == 0
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Panel de 40 lectores FICTICIOS, clausula SINTETICA; art. 11 de la Luna consultado (2026-11-11); Convencion de Viena (arts. 31-33) y jurisprudencia NO consultadas.")
print(f"{'condicion':36s}" + "".join(f"{l[:2]:>5s}" for l in LECTURAS) + "   H [bits]   H/2")
res = {}
for k, c in CONDICIONES.items():
    assert sum(c) == 40
    res[k] = H(c)
    print(f"{k:36s}" + "".join(f"{x:5d}" for x in c) + f"   {res[k]:8.3f}  {res[k] / 2:5.3f}")
# entropia marginal (mezcla de las tres condiciones con el mismo peso) vs condicional
tot = [sum(CONDICIONES[k][i] for k in CONDICIONES) for i in range(4)]
Hm = H(tot)
Hc = sum(res.values()) / len(res)
print(f"Entropia marginal H(X) = {Hm:.3f} bits ; entropia condicional H(X|condicion) = {Hc:.3f} bits ; informacion mutua I = {Hm - Hc:.3f} bits")
assert Hc <= Hm + 1e-12
mayoritaria = {k: max(range(4), key=lambda i: c[i]) for k, c in CONDICIONES.items()}
print("Lectura mayoritaria por condicion:", {k: LECTURAS[i][:2] for k, i in mayoritaria.items()})
share = {k: max(c) / 40 for k, c in CONDICIONES.items()}
print("Peso de la lectura mayoritaria:", {k: round(v, 3) for k, v in share.items()})
print("CLAVES " + json.dumps({"h1": "%.3f" % res["solo el texto"], "h2": "%.3f" % res["texto + contexto"], "h3": "%.3f" % res["texto + contexto + objeto y fin"], "hm": "%.3f" % Hm, "hc": "%.3f" % Hc, "mi": "%.3f" % (Hm - Hc), "s3": "%.3f" % share["texto + contexto + objeto y fin"], "s1": "%.3f" % share["solo el texto"]}))
print("Pruebas superadas.")
