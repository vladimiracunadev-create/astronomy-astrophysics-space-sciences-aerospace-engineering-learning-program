"""B118-C23 · Cobertura, sesgos y límites de las redes de vigilancia.

Población SINTÉTICA de 20000 objetos con N(>d) proporcional a d^-b (b = 1,38, pendiente de B118-C01 derivada de dos cifras de la ESA 2025) entre
0,05 m y 50 m, y una red HIPOTÉTICA cuyo alcance crece como d^(1/2) (régimen óptico: sigma ~ d^2 y R ~ sigma^(1/4)). Un objeto se detecta si
el alcance >= distancia mínima del paso, h / sin(e) con e uniforme entre 20 y 90 grados (semilla 118). El resultado es un SESGO DE SELECCIÓN:
el ajuste de la pendiente con solo lo detectado no recupera b.
Unidades: m, km. Estimador de máxima verosimilitud de Pareto: b = n / sum ln(d_i/d_min). Tolerancia: error de MLE = b/sqrt(n) (1 sigma).
"""
import math
import random
import sys

B_VERDAD = 1.38
R_REF, D_REF = 1500.0, 0.10  # km a 0,10 m (ILUSTRATIVO)


def alcance(d):
    return R_REF * math.sqrt(d / D_REF)


def poblacion(n=20000, semilla=118):
    rng = random.Random(semilla)
    d_lo, d_hi = 0.05, 50.0
    objs = []
    for _ in range(n):
        u = rng.random()
        d = (d_lo ** (-B_VERDAD) - u * (d_lo ** (-B_VERDAD) - d_hi ** (-B_VERDAD))) ** (-1.0 / B_VERDAD)
        h = rng.uniform(500.0, 1500.0)
        e = math.radians(rng.uniform(20.0, 90.0))
        objs.append((d, h, h / math.sin(e)))
    return objs


def mle(ds, dmin):
    s = [d for d in ds if d >= dmin]
    return len(s) / sum(math.log(d / dmin) for d in s), len(s)


def compute():
    v = {}
    objs = poblacion()
    det = [o for o in objs if alcance(o[0]) >= o[2]]
    v["n"], v["n_det"] = len(objs), len(det)
    v["frac_det"] = len(det) / len(objs)
    bins = [(0.05, 0.1), (0.1, 0.2), (0.2, 0.5), (0.5, 1.0), (1.0, 50.0)]
    v["compl"] = []
    for lo, hi in bins:
        t = [o for o in objs if lo <= o[0] < hi]
        k = [o for o in t if alcance(o[0]) >= o[2]]
        v["compl"].append((lo, hi, len(t), len(k), len(k) / len(t) if t else float("nan")))
    v["d_completo"] = D_REF * (1500.0 / math.sin(math.radians(20.0)) / R_REF) ** 2
    ds_true = [o[0] for o in objs]
    ds_det = [o[0] for o in det]
    v["b_verdad_est"], v["n_v"] = mle(ds_true, 0.05)
    v["b_det_05"], v["n_d05"] = mle(ds_det, 0.05)
    v["b_det_30"], v["n_d30"] = mle(ds_det, 1.0)
    v["b_true_1m"], v["n_t1"] = mle(ds_true, 1.0)
    v["err_b_true"] = v["b_verdad_est"] / math.sqrt(v["n_v"])
    v["err_b_1m"] = v["b_true_1m"] / math.sqrt(v["n_t1"])
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Poblacion SINTETICA de 20000 objetos (b = 1.38, 0.05-50 m) y red HIPOTETICA con alcance 1500 km a 0.10 m; semilla 118.")
    v = compute()
    print(f"Detectados {v['n_det']} de {v['n']} ({v['frac_det']:.3f})")
    print(" intervalo d [m]       total   detectados   completitud")
    for lo, hi, t, k, c in v["compl"]:
        print(f" {lo:5.2f} - {hi:4.2f}   {t:9d}   {k:9d}   {c:9.3f}")
    print(f"Diametro a partir del cual la red es completa (peor paso a 20 deg): {v['d_completo']:.3f} m")
    print(f"Pendiente verdadera: {B_VERDAD}; MLE con toda la poblacion (d >= 0.05): {v['b_verdad_est']:.3f} +- {v['err_b_true']:.3f}")
    print(f"MLE con lo detectado (d >= 0.05): {v['b_det_05']:.3f} (SESGADO, n = {v['n_d05']}); con d >= 1 m: {v['b_det_30']:.3f} (n = {v['n_d30']}); verdad con d >= 1 m: {v['b_true_1m']:.3f} +- {v['err_b_1m']:.3f}")
    assert abs(v["b_verdad_est"] - B_VERDAD) < 3 * v["err_b_true"]
    assert v["b_det_05"] < B_VERDAD - 0.3
    assert abs(v["b_det_30"] - v["b_true_1m"]) < 1e-9 or abs(v["b_det_30"] - B_VERDAD) < 3 * v["err_b_1m"] + 0.15
    print("Pruebas superadas (el MLE recupera b con la poblacion completa; la muestra detectada lo subestima).")


if __name__ == "__main__":
    main()
