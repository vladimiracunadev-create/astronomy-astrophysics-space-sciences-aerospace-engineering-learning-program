#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B100-C01: inventario por lotes con trazabilidad, FIFO frente a FEFO y conciliacion.

DATOS SINTETICOS (generados con semilla 20261110, no medidos): un material con recepciones de 160 unidades cada 30 dias y
vida util aleatoria entre 90 y 150 dias (lotes pares) o entre 30 y 60 dias (lotes impares); demanda diaria entera entre 2 y 6 unidades; 365 dias. Unidades: unidades (u) y dias (d).
Reglas: FIFO emite el lote recibido antes; FEFO emite el lote que caduca antes. Caduca lo no emitido al vencer su vida util.
Trazabilidad: cada emision registra (dia, lote, cantidad, consumidor); se consulta por lote.
Conciliacion: se inyectan 12 errores de conteo sinteticos en 60 posiciones y se mide la exactitud del registro.
Tolerancia: conservacion recibido = emitido + caducado + existencia exacta (0 u de diferencia).
"""
from __future__ import annotations
import platform
import random

SEMILLA = 20261110
DIAS = 365
INTERVALO = 30
QTY = 160


def generar():
    rng = random.Random(SEMILLA)
    lotes = []
    for k, dia in enumerate(range(0, DIAS, INTERVALO)):
        lotes.append({"id": f"L{k + 1:02d}", "llegada": dia, "vida": rng.randint(90, 150) if k % 2 == 0 else rng.randint(30, 60), "qty": QTY})
    demanda = [rng.randint(2, 6) for _ in range(DIAS)]
    return lotes, demanda


def simular(regla, lotes0, demanda):
    lotes = [dict(l, resto=l["qty"]) for l in lotes0]
    emitido = caducado = faltante = 0
    registro = []
    for dia in range(DIAS):
        for l in lotes:
            if l["resto"] > 0 and dia == l["llegada"] + l["vida"]:
                caducado += l["resto"]
                l["resto"] = 0
        disp = [l for l in lotes if l["llegada"] <= dia and l["resto"] > 0]
        clave = (lambda l: l["llegada"]) if regla == "FIFO" else (lambda l: l["llegada"] + l["vida"])
        disp.sort(key=clave)
        pedido = demanda[dia]
        for l in disp:
            if pedido == 0:
                break
            q = min(pedido, l["resto"])
            l["resto"] -= q
            pedido -= q
            emitido += q
            registro.append((dia, l["id"], q, f"C{dia % 5 + 1}"))
        faltante += pedido
    existencia = sum(l["resto"] for l in lotes)
    recibido = sum(l["qty"] for l in lotes)
    assert recibido == emitido + caducado + existencia
    return {"emitido": emitido, "caducado": caducado, "faltante": faltante, "existencia": existencia,
            "recibido": recibido, "registro": registro}


def exactitud(rng):
    n, err = 60, 12
    contado = [100] * n
    for i in rng.sample(range(n), err):
        contado[i] += rng.choice([-3, -2, -1, 1, 2, 3])
    ok = sum(1 for c in contado if c == 100)
    return ok / n, sum(abs(c - 100) for c in contado)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla {SEMILLA}")
    lotes, demanda = generar()
    print(f"Datos SINTETICOS: {len(lotes)} lotes de {QTY} u; demanda total {sum(demanda)} u en {DIAS} d")
    res = {}
    for regla in ("FIFO", "FEFO"):
        res[regla] = simular(regla, lotes, demanda)
        r = res[regla]
        print(f"{regla}: recibido {r['recibido']} u, emitido {r['emitido']} u, caducado {r['caducado']} u, "
              f"faltante {r['faltante']} u, existencia final {r['existencia']} u")
    reg = res["FEFO"]["registro"]
    l5 = [x for x in reg if x[1] == "L05"]
    print(f"Trazabilidad FEFO del lote L05: {len(l5)} emisiones, {sum(x[2] for x in l5)} u, "
          f"del dia {min(x[0] for x in l5)} al dia {max(x[0] for x in l5)}")
    por_cons = {}
    for _, _, q, c in l5:
        por_cons[c] = por_cons.get(c, 0) + q
    print("  por consumidor:", ", ".join(f"{c}={q}" for c, q in sorted(por_cons.items())))
    rng = random.Random(SEMILLA)
    acc, absdif = exactitud(rng)
    print(f"Exactitud del registro (conteo ciclico sintetico): {acc * 100:.1f} % ; diferencia absoluta total {absdif} u")
    assert res["FEFO"]["caducado"] <= res["FIFO"]["caducado"]
    assert res["FEFO"]["emitido"] >= res["FIFO"]["emitido"]
    assert sum(x[2] for x in l5) <= QTY
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
