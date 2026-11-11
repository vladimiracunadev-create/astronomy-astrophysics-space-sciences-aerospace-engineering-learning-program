"""B118-C21 · Calidad, latencia y trazabilidad de datos de vigilancia.

Flujo SINTÉTICO de observaciones (semilla 118): cada observación pasa por cuatro etapas (sensor, procesamiento, catálogo, entrega) con
retardos lognormales ILUSTRATIVOS. Se calcula la latencia total, la edad de los elementos al usarlos, el error de posición que crece con la edad
(a lo largo de la traza: 1,5 n t sigma_a) y una cadena de huellas SHA-256 que detecta alteraciones.
Fuente consultada (2026-11-11): Space-Track publica GP/OMM/TLE, SATCAT, CDM y avisa de que los TLE públicos son elementos medios que no
deben usarse para la predicción de conjunciones. Los valores numéricos NO provienen de ninguna fuente.
Unidades: s, h, km. GM = 398600.4418 km^3/s^2 (convencional). Tolerancia: percentiles por interpolación lineal; huellas exactas.
"""
import hashlib
import json
import math
import random
import sys

MU = 398600.4418
RE = 6378.137
ETAPAS = {"sensor": (6.0, 0.6), "procesamiento": (7.5, 0.7), "catalogo": (8.5, 0.5), "entrega": (5.5, 0.4)}  # (mu, sigma) de ln(s)


def percentil(xs, p):
    s = sorted(xs)
    k = (len(s) - 1) * p
    f = int(math.floor(k))
    c = min(f + 1, len(s) - 1)
    return s[f] + (s[c] - s[f]) * (k - f)


def error_posicion(edad_s, a=RE + 550.0, sig_a=0.02):
    n = math.sqrt(MU / a ** 3)
    return 1.5 * n * edad_s * sig_a


def cadena(registros):
    prev = "0" * 64
    out = []
    for r in registros:
        cuerpo = json.dumps(r, sort_keys=True, separators=(",", ":"))
        h = hashlib.sha256((prev + cuerpo).encode()).hexdigest()
        out.append((r, h))
        prev = h
    return out


def verificar(cad):
    prev = "0" * 64
    for r, h in cad:
        cuerpo = json.dumps(r, sort_keys=True, separators=(",", ":"))
        if hashlib.sha256((prev + cuerpo).encode()).hexdigest() != h:
            return False
        prev = h
    return True


def compute(n=5000, semilla=118):
    rng = random.Random(semilla)
    v = {}
    por_etapa = {k: [] for k in ETAPAS}
    total = []
    for _ in range(n):
        s = 0.0
        for k, (mu, sg) in ETAPAS.items():
            d = math.exp(rng.gauss(mu, sg))
            por_etapa[k].append(d)
            s += d
        total.append(s)
    v["n"] = n
    v["medianas"] = {k: percentil(x, 0.5) for k, x in por_etapa.items()}
    v["p50"], v["p95"], v["p99"] = percentil(total, 0.5), percentil(total, 0.95), percentil(total, 0.99)
    v["media"] = sum(total) / n
    v["suma_medianas"] = sum(v["medianas"].values())
    # edad de los elementos: actualización cada 8 h; edad al uso uniforme en [0, 8 h] + latencia
    edades = [rng.uniform(0, 8 * 3600) + rng.choice(total) for _ in range(n)]
    v["edad_p50"], v["edad_p95"] = percentil(edades, 0.5), percentil(edades, 0.95)
    v["err_p50"], v["err_p95"] = error_posicion(v["edad_p50"]), error_posicion(v["edad_p95"])
    v["completitud"] = sum(1 for t in total if t <= 3600.0) / n  # entregado en menos de 1 h
    regs = [dict(id=i, norad_sint=90000 + i, epoca_s=i * 60, edad_s=round(edades[i], 1)) for i in range(5)]
    cad = cadena(regs)
    v["cadena_ok"] = verificar(cad)
    cad_mal = [(dict(r, edad_s=r["edad_s"] + 1.0) if k == 2 else r, h) for k, (r, h) in enumerate(cad)]
    v["cadena_alterada_ok"] = verificar(cad_mal)
    v["huellas"] = [h[:12] for _, h in cad]
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Flujo SINTETICO de 5000 observaciones; retardos lognormales ILUSTRATIVOS (semilla 118); Space-Track consultado solo para los tipos de datos.")
    v = compute()
    print("Mediana por etapa [s]: " + ", ".join(f"{k} {m:.0f}" for k, m in v["medianas"].items()) + f"; suma de medianas {v['suma_medianas']:.0f} s")
    print(f"Latencia total: p50 = {v['p50']:.0f} s; p95 = {v['p95']:.0f} s; p99 = {v['p99']:.0f} s; media {v['media']:.0f} s (la suma de medianas subestima)")
    print(f"Edad de los elementos al usarlos: p50 = {v['edad_p50'] / 3600:.2f} h; p95 = {v['edad_p95'] / 3600:.2f} h")
    print(f"Error de posicion a lo largo de la traza (sigma_a = 0.02 km): p50 = {v['err_p50']:.3f} km; p95 = {v['err_p95']:.3f} km")
    print(f"Fraccion entregada en menos de 1 h: {v['completitud']:.4f}")
    print("Cadena de huellas (12 primeros hex): " + " ".join(v["huellas"]))
    print(f"Verificacion de la cadena intacta: {v['cadena_ok']}; con un registro alterado: {v['cadena_alterada_ok']}")
    assert v["cadena_ok"] and not v["cadena_alterada_ok"]
    assert v["p99"] > v["p95"] > v["p50"] and v["media"] > v["p50"]
    print("Pruebas superadas (cadena detecta la alteracion; percentiles ordenados; la cola pesa mas que la mediana).")


if __name__ == "__main__":
    main()
