#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B126-C06: auditor de cifras de un anexo financiero SINTETICO.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de inversion; no es un prospecto ni una oferta de valores.
Consultado (2026-11-11): pagina de ofertas exentas de la SEC (revisada por la SEC el 2026-01-26): Regla 506(b) limita las ventas a no mas
de 35 inversionistas no acreditados en 90 dias y prohibe la solicitacion general; la 506(c) permite solicitacion general si todos los
compradores son acreditados y verificados; Regulation Crowdfunding hasta 5 M USD; Regulation A hasta 75 M USD; Form D en 15 dias.
Circular A-94 de la OMB (2023-11-09): recalcular resultados para ver su sensibilidad a supuestos principales y reportar la incertidumbre.
NO se leyeron las normas completas (solo esas paginas descriptivas).
ILUSTRATIVOS (sinteticos): todas las cifras de la empresa del ejemplo (las mismas de B126-C03 a C05) y las distribuciones triangulares.
Modelo del auditor: cada cifra de una diapositiva se recalcula desde sus entradas; se marca OK si coincide dentro de la tolerancia, ERROR si no;
y toda cifra debe tener un rotulo (consultada, sintetica, calculada) y una fuente. Se planta UN error a proposito para comprobar que el
auditor lo detecta. El rango de incertidumbre del VPN se obtiene con Monte Carlo (20000 corridas, semilla 126).
"""
from __future__ import annotations
import platform, random

ENTRADAS = {
    "gasto_captacion_trim": (240_000.0, "sintetica"),
    "clientes_nuevos_trim": (60, "sintetica"),
    "arpa_mensual": (900.0, "sintetica"),
    "margen_bruto": (0.70, "sintetica"),
    "abandono_mensual": (0.02, "sintetica"),
}
FLUJOS = [-21.00, -17.00, -8.75, 6.75, 20.875, 31.375, 39.25, 44.5, 47.125, 48.4375]


def vpn(f, r):
    return sum(x / (1 + r) ** t for t, x in enumerate(f))


# diapositiva: (cifra, valor mostrado, rotulo, fuente, tolerancia)
def calcular():
    e = {k: v[0] for k, v in ENTRADAS.items()}
    cac = e["gasto_captacion_trim"] / e["clientes_nuevos_trim"]
    ltv = e["arpa_mensual"] * e["margen_bruto"] / e["abandono_mensual"]
    return {"CAC": cac, "LTV": ltv, "LTV/CAC": ltv / cac, "VPN a 10 %": vpn(FLUJOS, 0.10),
            "financiamiento necesario": -min(sum(FLUJOS[: t + 1]) for t in range(10))}


SLIDES = [
    ("CAC", 4000.0, "calculada", "B126-C04 (entradas sinteticas)", 0.5),
    ("LTV", 31500.0, "calculada", "B126-C04 (entradas sinteticas)", 0.5),
    ("LTV/CAC", 8.9, "calculada", "B126-C04 (entradas sinteticas)", 0.05),     # error plantado: correcto 7,875
    ("VPN a 10 %", 82.64, "calculada", "B126-C05 (flujos sinteticos)", 0.1),
    ("financiamiento necesario", 46.75, "calculada", "B126-C03 (flujos sinteticos)", 0.01),
    ("tope de la Regulation Crowdfunding", 5.0, "consultada", "SEC, ofertas exentas (rev. 2026-01-26), M USD", 0.0),
    ("tamano del mercado espacial", 500.0, "", "", 0.0),                        # sin rotulo ni fuente: debe fallar
]


def tri(rnd, a, m, b):
    return rnd.triangular(a, b, m)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS (ilustrativos); de la SEC solo se consulto la pagina de ofertas exentas (rev. 2026-01-26); de la A-94, sensibilidad e incertidumbre.")
    calc = calcular()
    print(" cifra                                 mostrado   recalculado  estado")
    errores, sin_rotulo = [], []
    for nombre, mostrado, rotulo, fuente, tol in SLIDES:
        if not rotulo or not fuente:
            sin_rotulo.append(nombre)
            print(f" {nombre:<36} {mostrado:10.2f}   {'-':>10}   SIN ROTULO/FUENTE")
            continue
        if nombre in calc:
            r = calc[nombre]
            ok = abs(r - mostrado) <= tol
            print(f" {nombre:<36} {mostrado:10.2f}   {r:10.3f}   {'OK' if ok else 'ERROR'}")
            if not ok:
                errores.append(nombre)
        else:
            print(f" {nombre:<36} {mostrado:10.2f}   {'-':>10}   OK (consultada, con fuente)")
    print(f"Errores de calculo detectados: {errores} ; cifras sin rotulo o fuente: {sin_rotulo}")
    assert errores == ["LTV/CAC"] and sin_rotulo == ["tamano del mercado espacial"]
    # incertidumbre del VPN: factor de ingresos triangular(0.6, 1.0, 1.2), tasa triangular(0.08, 0.10, 0.14), capex x triangular(0.9,1.0,1.4)
    ing = [c * 0.35 for c in (0, 0, 20, 60, 110, 150, 180, 200, 210, 215)]
    capex = [20.0, 15.0, 10.0, 4.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]
    fijo = [1.0, 2.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    rnd = random.Random(126)
    vs = []
    for _ in range(20000):
        k = tri(rnd, 0.6, 1.0, 1.2)
        r = tri(rnd, 0.08, 0.10, 0.14)
        kc = tri(rnd, 0.9, 1.0, 1.4)
        f = [0.75 * i * k - fx - cx * kc for i, fx, cx in zip(ing, fijo, capex)]
        vs.append(vpn(f, r))
    vs.sort()
    n = len(vs)
    p10, p50, p90 = vs[int(.1 * n)], vs[int(.5 * n)], vs[int(.9 * n)]
    pneg = sum(1 for v in vs if v < 0) / n
    print(f"VPN con incertidumbre (M USD): P10 = {p10:.1f} ; P50 = {p50:.1f} ; P90 = {p90:.1f} ; P(VPN < 0) = {pneg:.3f}")
    # via 2: caso central determinista cae dentro del rango
    central = vpn([0.75 * i - fx - cx for i, fx, cx in zip(ing, fijo, capex)], 0.10)
    print(f"Caso central determinista (factor 1, tasa 10 %, capex x1) = {central:.1f} M USD")
    assert p10 < central < p90 + 1e-9 and abs(central - calc["VPN a 10 %"]) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
