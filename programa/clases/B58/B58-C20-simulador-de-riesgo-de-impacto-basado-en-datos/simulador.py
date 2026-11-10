#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C20: simulador de riesgo de impacto basado en datos: catalogo sintetico con campos tipo SBDB, clasificacion, ranking por Palermo e impactos de fondo por Poisson.

Datos: catalogo SINTETICO de 300 objetos con los campos a, e, i, q, ad, H y moid (nombres de la documentacion de la API SBDB de JPL, consultada el 2026-11-09; los valores son inventados, semilla 20261109).
Criterio NEO (q < 1.3 au), grupos y PHA (MOID <= 0.05 au y H <= 22) segun la pagina NEO Groups de CNEOS/JPL (consultada); formula de Palermo y frecuencia de fondo fB = 0.03 E^(-4/5) segun la pagina de
la escala de Palermo (consultada). Albedo 0.14, densidad 2600 kg/m^3, velocidad 20 km/s: ILUSTRATIVOS. Probabilidades y tiempos de impacto de los PHA: SINTETICOS.
Modelo: (1) lectura del catalogo por JSON; (2) clasificacion y diametro; (3) energia, Palermo y ranking; (4) impactos de fondo: llegadas de Poisson con tasa fB(E_min) y energias con N(>E) ~ E^-0.8.
Supuestos: independencia, ley de fondo exacta, sin catalogo real. Validez: ilustrativa; no evalua ningun objeto real.
Tolerancia: numero de impactos en 100 000 anios dentro de 3 desviaciones de Poisson de fB(1 Mt) x 1e5; fraccion con E > 10 Mt dentro de 3 errores binomiales de 10^-0.8.
"""
import json, math, platform, random

MT = 4.184e15

def generar(rng, n=300):
    cat = []
    for k in range(n):
        a = rng.uniform(0.8, 3.5)
        e = rng.uniform(0.0, 0.75)
        e = min(e, 0.95)
        cat.append({"des": "SINT-%03d" % k, "a": round(a, 4), "e": round(e, 4), "i": round(rng.uniform(0, 35), 2),
                    "q": round(a * (1 - e), 4), "ad": round(a * (1 + e), 4), "H": round(rng.uniform(17, 28), 2),
                    "moid": round(rng.expovariate(1 / 0.10), 4)})
    return cat

def grupo(a, q, ad):
    if q >= 1.3: return "no NEO"
    if a < 1.0: return "Atira" if ad < 0.983 else "Aten"
    return "Apollo" if q < 1.017 else "Amor"

def diametro(H, p=0.14):
    return 1329e3 / math.sqrt(p) * 10 ** (-H / 5.0)   # metros

def energia_mt(D, rho=2600.0, v=20e3):
    return 0.5 * rho * math.pi * D ** 3 / 6 * v * v / MT

def palermo(PI, E, DT):
    return math.log10(PI / (0.03 * E ** -0.8 * DT))

def calcular():
    rng = random.Random(20261109)
    cat = json.loads(json.dumps(generar(rng)))       # ida y vuelta por JSON
    cuentas = {}
    pha = []
    for o in cat:
        g = grupo(o["a"], o["q"], o["ad"])
        cuentas[g] = cuentas.get(g, 0) + 1
        o["D"] = diametro(o["H"])
        if g != "no NEO" and o["moid"] <= 0.05 and o["H"] <= 22.0:
            o["PI"] = 10 ** rng.uniform(-8, -4)
            o["DT"] = rng.randint(3, 50)
            o["E"] = energia_mt(o["D"])
            o["PS"] = palermo(o["PI"], o["E"], o["DT"])
            pha.append(o)
    pha.sort(key=lambda o: -o["PS"])
    # impactos de fondo
    T, Emin = 100000.0, 1.0
    lam = 0.03 * Emin ** -0.8
    t, n, e10 = 0.0, 0, 0
    while True:
        t += rng.expovariate(lam)
        if t > T: break
        n += 1
        E = Emin * rng.random() ** (-1 / 0.8)
        e10 += E > 10.0
    return {"cuentas": cuentas, "pha": pha, "n_cat": len(cat), "n_imp": n, "esp": lam * T, "f10": e10 / n, "f10_esp": 10 ** -0.8}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Catalogo sintetico: %d objetos ; grupos: %s" % (r["n_cat"], ", ".join("%s=%d" % kv for kv in sorted(r["cuentas"].items()))))
    print("PHA sinteticos (MOID <= 0.05 au y H <= 22): %d" % len(r["pha"]))
    print("%-9s %6s %7s %10s %5s %10s %8s" % ("objeto", "H", "D[m]", "PI", "DT", "E[Mt]", "Palermo"))
    for o in r["pha"][:5]:
        print("%-9s %6.1f %7.0f %10.1e %5d %10.1f %8.2f" % (o["des"], o["H"], o["D"], o["PI"], o["DT"], o["E"], o["PS"]))
    print("Impactos de fondo en 100 000 anios con E >= 1 Mt: simulados = %d ; esperados = %.0f +- %.0f" % (r["n_imp"], r["esp"], math.sqrt(r["esp"])))
    print("Fraccion con E > 10 Mt: simulada = %.4f ; analitica 10^-0.8 = %.4f" % (r["f10"], r["f10_esp"]))
    assert abs(r["n_imp"] - r["esp"]) < 3 * math.sqrt(r["esp"])
    assert abs(r["f10"] - r["f10_esp"]) < 3 * math.sqrt(r["f10_esp"] * (1 - r["f10_esp"]) / r["n_imp"])
    assert all(r["pha"][i]["PS"] >= r["pha"][i + 1]["PS"] for i in range(len(r["pha"]) - 1))
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
