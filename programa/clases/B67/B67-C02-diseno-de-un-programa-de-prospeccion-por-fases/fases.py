"""B67-C02: programa de prospeccion por fases con actualizacion bayesiana (SINTETICO).

Una celda de 1 km2 tiene hielo explotable con probabilidad previa p0. Tres fases de
costo creciente (reconocimiento orbital, muestreo con rover, perforacion de
confirmacion); cada una da un resultado positivo/negativo con sensibilidad y tasa
de falsos positivos propias. Solo las celdas positivas pasan a la fase siguiente.
Se compara la formula analitica con una simulacion Monte Carlo (semilla fija).
Costos en unidades monetarias arbitrarias (UM) por celda: ilustrativos.
Requiere solo numpy.
"""
import sys
import numpy as np

P0 = 0.10
# (nombre, sensibilidad, tasa de falsos positivos, costo UM por celda)
FASES = [
    ("F1 reconocimiento orbital", 0.85, 0.20, 0.1),
    ("F2 muestreo con rover", 0.90, 0.10, 2.0),
    ("F3 perforacion de confirmacion", 0.95, 0.02, 10.0),
]
VALOR = 60.0  # UM por celda con deposito confirmado (ilustrativo)


def posterior(p, sens, fpr):
    """P(hielo | positivo) por Bayes."""
    return p * sens / (p * sens + (1 - p) * fpr)


def analitico():
    p = P0
    surv_h, surv_n = 1.0, 1.0  # prob. conjunta de llegar a la fase k con/sin hielo
    filas = []
    costo = 0.0
    for nombre, se, fp, c in FASES:
        llega = P0 * surv_h + (1 - P0) * surv_n  # fraccion de celdas que entran a la fase
        costo += llega * c
        surv_h *= se
        surv_n *= fp
        p = posterior(p, se, fp)
        filas.append((nombre, llega, p))
    pasan = P0 * surv_h + (1 - P0) * surv_n
    return filas, costo, pasan, P0 * surv_h


def main():
    print(f"Python {sys.version.split()[0]} ; numpy {np.__version__}")
    print("DATOS SINTETICOS: sensibilidades, costos y valor inventados para la clase")
    filas, costo, pasan, verd = analitico()
    print("fase                             entran    P(hielo|positivo)")
    for n, ll, p in filas:
        print(f"  {n:32s} {ll:7.4f}   {p:.4f}")
    print(f"Fraccion que supera las 3 fases: {pasan:.5f} ; de ellas con hielo real: {verd / pasan:.4f}")
    print(f"Costo esperado por celda con fases: {costo:.4f} UM")
    c_dir = FASES[2][3]
    print(f"Costo por celda perforando todo directamente: {c_dir:.4f} UM")
    vn_fases = VALOR * verd - costo  # verd ya incluye la sensibilidad de F3
    vn_dir = VALOR * P0 * FASES[2][1] - c_dir
    print(f"Valor neto esperado por celda: con fases = {vn_fases:.4f} UM ; perforar todo = {vn_dir:.4f} UM")
    print(f"Hielo hallado por celda: con fases = {verd:.5f} ; perforar todo = {P0 * FASES[2][1]:.5f}")

    # Monte Carlo
    rng = np.random.default_rng(6702)
    N = 400000
    hielo = rng.random(N) < P0
    vivo = np.ones(N, bool)
    costo_mc = 0.0
    for _, se, fp, c in FASES:
        costo_mc += vivo.sum() * c
        u = rng.random(N)
        pos = np.where(hielo, u < se, u < fp)
        vivo &= pos
    f_mc = vivo.mean()
    pr_mc = hielo[vivo].mean()
    print(f"Monte Carlo (N={N}, semilla 6702): fraccion que pasa = {f_mc:.5f} ; con hielo real = {pr_mc:.4f} ; costo/celda = {costo_mc / N:.4f}")
    sd = np.sqrt(pasan * (1 - pasan) / N)
    assert abs(f_mc - pasan) < 4 * sd, "fraccion fuera de 4 sigma"
    assert abs(costo_mc / N - costo) < 0.01
    sd2 = np.sqrt(verd / pasan * (1 - verd / pasan) / vivo.sum())
    assert abs(pr_mc - verd / pasan) < 4 * sd2
    # posterior secuencial = posterior con razon de verosimilitud conjunta
    lr = np.prod([se / fp for _, se, fp, _ in FASES])
    odds = P0 / (1 - P0) * lr
    assert abs(odds / (1 + odds) - verd / pasan) < 1e-12
    print(f"Razon de verosimilitud conjunta = {lr:.1f} ; posterior por cuotas = {odds / (1 + odds):.4f} (coincide)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
