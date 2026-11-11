#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B129-C04: control de calidad de un lote SINTETICO de contribuciones voluntarias de magnitudes.

Todo SINTETICO: 400 registros de la variable VS-S (m = 10.00 + 0.50 sin(2 pi t/37)) con ruido gaussiano sigma = 0.05 mag, 20 observadores
inventados; un 12 % de registros recibe un error SEMBRADO de tipo conocido (desplazamiento decimal, error de varios decimos de magnitud,
duplicado exacto, fecha futura, campo ausente, filtro invalido). Fecha de referencia fija: dia 400 de la serie (NO la fecha real).
Etapas: (1) esquema y rangos; (2) duplicados por (observador, dia, filtro); (3) valores atipicos robustos frente a la mediana de otros
observadores en +/-2 dias: |m - mediana| / max(1.4826*MAD, 0.10) > k (k = 4).
Metricas con etiquetas conocidas: precision = TP/(TP+FP), exhaustividad = TP/(TP+FN). Segunda via: calculo con conjuntos frente a conteo por
bucle (deben coincidir exactamente). Tolerancias declaradas: exhaustividad >= 0.80 con k = 4; fraccion de registros limpios retenidos >= 0.97.
Semilla 129. Unidades: dias, mag.
"""
from __future__ import annotations
import math, platform, random, statistics

M0, AMP, PER, SIG = 10.00, 0.50, 37.0, 0.05
HOY = 400.0
FILTROS = {"V", "B", "R", "I"}


def verdadera(t):
    return M0 + AMP * math.sin(2 * math.pi * t / PER)


def generar(rng, n=400):
    regs, tipos = [], {}
    for i in range(n):
        t = float(rng.randint(0, 399))
        obs = f"O{rng.randint(1, 20):02d}"
        f = rng.choice(["V", "V", "V", "B", "R"])
        m = round(verdadera(t) + rng.gauss(0, SIG), 2)
        regs.append({"id": i, "obs": obs, "dia": t, "filtro": f, "mag": m})
    # errores sembrados: 12 % de los registros
    idx = list(range(n))
    rng.shuffle(idx)
    n_err = int(0.12 * n)
    for j, i in enumerate(idx[:n_err]):
        r = regs[i]
        tipo = ["decimal", "desplazado", "duplicado", "futuro", "ausente", "filtro"][j % 6]
        if tipo == "decimal":
            r["mag"] = round(r["mag"] * 10, 2)
        elif tipo == "desplazado":
            r["mag"] = round(r["mag"] + rng.choice([-1, 1]) * rng.uniform(0.8, 2.5), 2)
        elif tipo == "duplicado":
            r["obs"], r["dia"], r["filtro"], r["mag"] = regs[i - 1]["obs"], regs[i - 1]["dia"], regs[i - 1]["filtro"], regs[i - 1]["mag"]
            tipos[i] = tipo
            continue
        elif tipo == "futuro":
            r["dia"] = HOY + rng.randint(5, 60)
        elif tipo == "ausente":
            r["mag"] = None
        elif tipo == "filtro":
            r["filtro"] = "X"
        tipos[i] = tipo
    return regs, tipos


def esquema(r):
    if r["mag"] is None or r["filtro"] not in FILTROS:
        return False
    if not (0.0 < r["mag"] < 25.0):
        return False
    if r["dia"] > HOY:
        return False
    return True


def depurar(regs, k):
    marca = {}
    # 1) esquema
    for r in regs:
        if not esquema(r):
            marca[r["id"]] = "esquema"
    # 2) duplicados (se conserva el primero)
    vistos = set()
    for r in regs:
        if r["id"] in marca:
            continue
        clave = (r["obs"], r["dia"], r["filtro"])
        if clave in vistos:
            marca[r["id"]] = "duplicado"
        vistos.add(clave)
    # 3) atipicos robustos frente a otros observadores en +/-2 dias
    for r in regs:
        if r["id"] in marca:
            continue
        vec = [x["mag"] for x in regs if x["id"] not in marca and x["obs"] != r["obs"] and abs(x["dia"] - r["dia"]) <= 2.0 and x["id"] != r["id"]]
        if len(vec) < 3:
            continue
        med = statistics.median(vec)
        mad = statistics.median(abs(v - med) for v in vec)
        escala = max(1.4826 * mad, 0.10)
        if abs(r["mag"] - med) / escala > k:
            marca[r["id"]] = "atipico"
    return marca


def main():
    rng = random.Random(129)
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla 129")
    regs, tipos = generar(rng)
    print(f"DATOS SINTETICOS: {len(regs)} registros, {len(tipos)} con error sembrado (12 %); fecha de referencia = dia {HOY:.0f}")
    cont = {}
    for t in tipos.values():
        cont[t] = cont.get(t, 0) + 1
    print("  errores sembrados: " + ", ".join(f"{a}={b}" for a, b in sorted(cont.items())))
    print("  k    marcados  TP  FP  FN  precision  exhaustividad  limpios retenidos")
    res = {}
    for k in (2, 3, 4, 5, 6):
        marca = depurar(regs, k)
        real = set(tipos)
        mar = set(marca)
        tp, fp, fn = len(real & mar), len(mar - real), len(real - mar)
        # segunda via: conteo por bucle
        tp2 = fp2 = fn2 = 0
        for r in regs:
            e, m = r["id"] in tipos, r["id"] in marca
            tp2 += e and m
            fp2 += (not e) and m
            fn2 += e and (not m)
        assert (tp, fp, fn) == (tp2, fp2, fn2)
        prec = tp / (tp + fp) if tp + fp else float("nan")
        rec = tp / (tp + fn)
        limpios = len(regs) - len(real)
        ret = (limpios - fp) / limpios
        res[k] = (prec, rec, ret, marca)
        print(f" {k:2d}  {len(mar):8d}  {tp:2d}  {fp:2d}  {fn:2d}  {prec:9.3f}  {rec:13.3f}  {ret:17.3f}")
    prec, rec, ret, marca = res[4]
    # desglose por tipo con k = 4
    print("Con k = 4, detectados por tipo sembrado:")
    for t in sorted(cont):
        tot = cont[t]
        det = sum(1 for i, tt in tipos.items() if tt == t and i in marca)
        print(f"   {t:11s} {det}/{tot}")
    omitidos = [i for i in tipos if i not in marca]
    if omitidos:
        print("   no detectados: " + ", ".join(f"id{i}({tipos[i]}, m={regs[i]['mag']})" for i in omitidos[:6]))
    # sensibilidad: que tan grande debe ser un desplazamiento para detectarse (k = 4)
    print("Sensibilidad (k = 4): fraccion detectada al desplazar 100 registros limpios una cantidad fija")
    limpios_ids = [r["id"] for r in regs if r["id"] not in tipos and r["id"] not in marca]
    rng2 = random.Random(1290)
    muestra = rng2.sample(limpios_ids, 100)
    evaluables = sum(1 for i in limpios_ids if len([x for x in regs if x["id"] not in marca and x["obs"] != regs[i]["obs"] and abs(x["dia"] - regs[i]["dia"]) <= 2.0 and x["id"] != i]) >= 3)
    print(f"   registros limpios con al menos 3 vecinos de otros observadores (evaluables): {evaluables}/{len(limpios_ids)}")
    for d in (0.1, 0.2, 0.3, 0.5, 0.8, 1.2):
        copia = [dict(r) for r in regs]
        for i in muestra:
            copia[i]["mag"] = round(copia[i]["mag"] + d, 2)
        mk = depurar(copia, 4)
        det = sum(1 for i in muestra if mk.get(i) == "atipico")
        print(f"   desplazamiento {d:.1f} mag -> detectados {det}/100")
    assert rec >= 0.80 and ret >= 0.97, "el filtro no cumple las tolerancias declaradas"
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
