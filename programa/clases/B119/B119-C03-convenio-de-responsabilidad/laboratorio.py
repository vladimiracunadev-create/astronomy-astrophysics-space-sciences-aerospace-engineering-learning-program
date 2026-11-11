#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C03: reparto de una indemnizacion bajo responsabilidad absoluta (superficie) y por culpa (espacio). Datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Resumen de busqueda consultado (2026-11-11, pagina de UNOOSA del Convenio de Responsabilidad; lectura directa 404): art. II, el Estado de lanzamiento responde
de modo absoluto por danos en la superficie terrestre o a aeronaves en vuelo; art. III, danos en el espacio: responsabilidad por culpa; objetos de dos Estados
que dañan a un tercero: responsabilidad solidaria. NO consultados: texto completo, plazo de reclamacion, Comision de Reclamaciones.
SINTETICO: dano D = 100 unidades monetarias sinteticas (u.m.); culpas 0.7 y 0.3; Estados A y B inventados.
Reparto interno de una responsabilidad solidaria: proporcional a la culpa; si no se puede determinar, por partes iguales.
Tolerancia: suma de pagos == D (1e-9).
"""
import json, platform

D = 100.0

def reparto(culpa, solvente):
    """Pago de cada Estado frente a la victima (solidaridad: si uno no paga, el otro cubre) y reparto interno final."""
    total = sum(culpa.values())
    interno = {k: D * v / total for k, v in culpa.items()}
    pago = dict.fromkeys(culpa, 0.0)
    pendiente = D
    for k in culpa:
        if solvente[k] and pendiente > 0:
            pago[k] = pendiente
            pendiente = 0.0
    return pago, interno

print("Python", platform.python_version(), "(biblioteca estandar)")
print("Datos SINTETICOS (D = 100 u.m.); texto del convenio solo por resumen de busqueda; plazo de reclamacion NO consultado.")
casos = {
    "superficie, A y B solventes (culpa 0.7/0.3)": ({"A": 0.7, "B": 0.3}, {"A": True, "B": True}),
    "superficie, A insolvente": ({"A": 0.7, "B": 0.3}, {"A": False, "B": True}),
    "culpa indeterminada (partes iguales)": ({"A": 1.0, "B": 1.0}, {"A": True, "B": True}),
}
res = {}
for nombre, (culpa, sol) in casos.items():
    pago, interno = reparto(culpa, sol)
    assert abs(sum(pago.values()) - D) < 1e-9 and abs(sum(interno.values()) - D) < 1e-9
    res[nombre] = (pago, interno)
    print(f"{nombre}\n   victima cobra de: {pago}   reparto interno final: " + str({k: round(v, 1) for k, v in interno.items()}))

# Regimen por culpa en el espacio: la victima recibe segun la culpa del demandado
culpa_demandado = 0.6
indem_espacio = D * culpa_demandado
print(f"En el espacio (responsabilidad por culpa): demandado con culpa {culpa_demandado} paga {indem_espacio:.1f} u.m. de {D:.0f}")
# Regreso: A paga todo (B insolvente) y repite contra B por su cuota interna
pago, interno = res["superficie, A insolvente"]
print(f"Regreso: B paga {pago['B']:.1f}; su cuota interna es {interno['B']:.1f}; B reclama a A {pago['B'] - interno['B']:.1f} u.m.")
assert abs((pago['B'] - interno['B']) - 70.0) < 1e-9
print("CLAVES " + json.dumps({"c1_pagoA": "%.1f" % res[list(res)[0]][0]["A"], "intA": "%.1f" % res[list(res)[0]][1]["A"], "intB": "%.1f" % res[list(res)[0]][1]["B"], "paga_B": "%.1f" % pago["B"], "regreso": "%.1f" % (pago["B"] - interno["B"]), "esp": "%.1f" % indem_espacio, "iguales": "%.1f" % res[list(res)[2]][1]["A"]}))
print("Pruebas superadas.")
