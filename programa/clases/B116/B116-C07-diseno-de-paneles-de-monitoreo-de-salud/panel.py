#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B116-C07: logica de un panel de salud SINTETICO: antiguedad del dato, prioridad y contraste accesible.

Todo es sintetico (semilla 121): tripulacion ficticia de 4 personas ("S1"-"S4"), valores simulados, umbrales ILUSTRATIVOS. Sirve para
probar reglas de diseno; no es un panel operativo ni da criterio clinico. Contraste (WCAG 2.2, criterio 1.4.3 Nivel AA, consultado
2026-11-10 en w3.org): razon = (L1 + 0,05) / (L2 + 0,05), con L1 la luminancia relativa del color mas claro y L2 la del mas oscuro;
luminancia relativa L = 0,2126 R + 0,7152 G + 0,0722 B con cada canal sRGB linealizado (c/12,92 si c <= 0,04045; si no, ((c + 0,055)/1,055)^2,4);
minimos de 4,5:1 para texto normal y 3:1 para texto grande; los umbrales no se redondean. Antiguedad del dato = instante actual -
instante efectivo de la observacion (el retardo de comunicaciones ya esta incluido en ese desfase); estado "obsoleto" si supera el
limite propio de cada signo. Prioridad = categoria (alta, media, baja) y luego antiguedad. Retardo unidireccional de 4 a 24 min segun la
pagina del Centro Goddard de la NASA (consultada 2026-11-10). Solo numpy.
"""
from __future__ import annotations
import platform
import numpy as np


def lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(rgb):
    r, g, b = (lin(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


FONDO = (255, 255, 255)
PAL = {
    "texto negro": (0, 0, 0),
    "gris oscuro 595959": (0x59, 0x59, 0x59),
    "gris medio 767676": (0x76, 0x76, 0x76),
    "gris claro 949494": (0x94, 0x94, 0x94),
    "rojo B00020": (0xB0, 0x00, 0x20),
    "ambar FFC107": (0xFF, 0xC1, 0x07),
    "ambar oscuro 8A5A00": (0x8A, 0x5A, 0x00),
    "verde 2E7D32": (0x2E, 0x7D, 0x32),
    "verde claro 66BB6A": (0x66, 0xBB, 0x6A),
}
LIMITE_MIN = {"fc": 10, "spo2": 10, "temp": 30}  # limite de antiguedad [min] por signo (ilustrativo)
VALORES = {"fc": ("FC", "lpm"), "spo2": ("SpO2", "%"), "temp": ("T", "C")}


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 121): tripulacion ficticia; umbrales ilustrativos; no es un panel operativo")
    c = contraste((0, 0, 0), (255, 255, 255))
    print(f"Control: contraste negro sobre blanco = {c:.2f}:1 (esperado 21.00:1)")
    assert abs(c - 21.0) < 1e-9
    print("Contraste de colores de texto sobre fondo blanco (minimo 4.5:1 normal; 3:1 grande):")
    print("  color                    razon    texto normal  texto grande")
    for n, rgb in PAL.items():
        r = contraste(rgb, FONDO)
        print(f"  {n:22s} {r:6.2f}:1     {'cumple' if r >= 4.5 else 'NO cumple':10s}   {'cumple' if r >= 3.0 else 'NO cumple'}")
    assert contraste(PAL["gris medio 767676"], FONDO) >= 4.5 > contraste(PAL["gris claro 949494"], FONDO)
    rng = np.random.default_rng(121)
    ahora = 3600  # s
    filas = []
    for s in ("S1", "S2", "S3", "S4"):
        for code, (mu, sd) in {"fc": (72, 6), "spo2": (97, 1), "temp": (36.8, 0.2)}.items():
            retardo_s = float(rng.choice([2 * 60, 8 * 60, 24 * 60, 50 * 60]))  # desfase por enlace/retardo
            valor = float(rng.normal(mu, sd))
            filas.append({"s": s, "code": code, "valor": valor, "edad_min": retardo_s / 60.0})
    # fuerzo dos casos para la demostracion
    filas[0]["valor"] = 118.0  # S1 FC alta
    filas[3 * 1 + 1]["valor"] = 91.0  # S2 SpO2 baja
    cat = []
    for f in filas:
        v, c_ = f["valor"], f["code"]
        alta = (c_ == "fc" and (v >= 110 or v <= 45)) or (c_ == "spo2" and v <= 92) or (c_ == "temp" and v >= 39.0)
        media = (c_ == "fc" and v >= 100) or (c_ == "spo2" and v <= 95) or (c_ == "temp" and v >= 38.0)
        f["cat"] = 2 if alta else (1 if media else 0)
        f["obsoleto"] = f["edad_min"] > LIMITE_MIN[c_]
    orden = sorted(filas, key=lambda f: (-f["cat"], -f["edad_min"]))
    print("Panel de texto ordenado por prioridad (categoria y luego antiguedad); estado en TEXTO ademas del color:")
    print("  persona  signo   valor      edad [min]  categoria   estado del dato")
    nombres = {0: "baja", 1: "media", 2: "ALTA"}
    for f in orden:
        nm, un = VALORES[f["code"]]
        print(f"   {f['s']}     {nm:5s}  {f['valor']:6.1f} {un:3s}   {f['edad_min']:6.1f}     {nombres[f['cat']]:5s}      {'OBSOLETO (> %d min)' % LIMITE_MIN[f['code']] if f['obsoleto'] else 'vigente'}")
    n_alta = sum(f["cat"] == 2 for f in filas)
    n_obs = sum(f["obsoleto"] for f in filas)
    print(f"Indicadores totales = {len(filas)}; en categoria alta = {n_alta}; obsoletos = {n_obs}")
    print("Un valor en categoria baja pero OBSOLETO no debe mostrarse como 'normal': se muestra atenuado con la etiqueta 'obsoleto'.")
    cegados = [f for f in filas if f["cat"] == 2 and f["obsoleto"]]
    print(f"Casos de categoria alta con dato obsoleto (se muestran con la antiguedad): {len(cegados)}")
    print("Carga visual: numero de indicadores que parpadean o estan resaltados a la vez, con una politica de maximo 3:")
    resaltados = [f for f in orden if f["cat"] >= 1][:3]
    print(f"  resaltados = {len(resaltados)} (maximo 3); resto en lista")
    assert len(resaltados) <= 3
    print("Efecto de la antiguedad: con retardo unidireccional de 4 a 24 min el dato mas fresco ya tiene 4-24 min cuando llega:")
    for d in (4, 12, 24):
        n_vig = [code for code, lim in LIMITE_MIN.items() if d <= lim]
        print(f"   retardo {d:2d} min: signos con limite de antiguedad aun vigentes = {n_vig if n_vig else 'ninguno'}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
