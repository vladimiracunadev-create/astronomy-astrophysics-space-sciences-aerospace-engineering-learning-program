"""B118-C11 · Diseño para mitigación de desechos.

Presupuesto de fiabilidad de la disposición post-misión (PMD) de un satélite SINTÉTICO: cadena en serie de cuatro funciones
(energía, actitud, propulsión, comunicaciones) con tasas de fallo exponenciales ILUSTRATIVAS.
Referencia consultada (2026-11-11, IADC-02-01 Rev. 4, enero de 2025, vía UNOOSA A/AC.105/C.1/2025/CRP.9): probabilidad de disposición
exitosa al menos 90 % con objetivo de 99 % o más.
Unidades: años, 1/año, adimensional. Semilla Monte Carlo 118. Tolerancia: 3 errores estándar binomiales.
"""
import math
import random
import sys

TASAS = {"energia": 0.010, "actitud": 0.015, "propulsion": 0.012, "comunicaciones": 0.008}  # 1/año, ILUSTRATIVAS


def r_serie(tasas, t):
    return math.exp(-sum(tasas.values()) * t)


def r_paralelo(r, n):
    return 1.0 - (1.0 - r) ** n


def requerida_por_bloque(meta, n_bloques):
    return meta ** (1.0 / n_bloques)


def monte_carlo(tasas, t, n=200_000, semilla=118, redundancia=None):
    rng = random.Random(semilla)
    ok = 0
    for _ in range(n):
        bien = True
        for nombre, lam in tasas.items():
            copias = 1 if not redundancia else redundancia.get(nombre, 1)
            if not any(rng.random() < math.exp(-lam * t) for _ in range(copias)):
                bien = False
                break
        ok += bien
    return ok / n, math.sqrt(max(ok / n * (1 - ok / n), 1e-12) / n)


def compute():
    v = {}
    t = 7.0  # años de operación antes de disponer
    v["R_serie"] = r_serie(TASAS, t)
    v["R_bloque"] = {k: math.exp(-lam * t) for k, lam in TASAS.items()}
    v["req90"] = requerida_por_bloque(0.90, 4)
    v["req99"] = requerida_por_bloque(0.99, 4)
    v["mc"], v["mc_err"] = monte_carlo(TASAS, t)
    red = {"propulsion": 2, "actitud": 2}
    r_red = 1.0
    for k, lam in TASAS.items():
        r = math.exp(-lam * t)
        r_red *= r_paralelo(r, red.get(k, 1))
    v["R_red"] = r_red
    v["mc_red"], v["mc_red_err"] = monte_carlo(TASAS, t, redundancia=red)
    # tiempo de operación máximo para cumplir 0,90 con la cadena en serie
    v["t_max90"] = -math.log(0.90) / sum(TASAS.values())
    # separar «llegar al fin de misión» de «poder disponer»: la PMD debe diseñarse para el fallo (reserva)
    v["lam_total"] = sum(TASAS.values())
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Tasas de fallo ILUSTRATIVAS (1/anio): " + ", ".join(f"{k} {l}" for k, l in TASAS.items()) + "; meta IADC Rev.4 (consultada): >= 0.90, objetivo 0.99.")
    v = compute()
    print("Fiabilidad por funcion a 7 anios: " + ", ".join(f"{k} {r:.4f}" for k, r in v["R_bloque"].items()))
    print(f"Cadena en serie a 7 anios: {v['R_serie']:.4f}; Monte Carlo (2e5): {v['mc']:.4f} +- {v['mc_err']:.4f}")
    print(f"Fiabilidad por funcion requerida para 0.90 con 4 funciones iguales: {v['req90']:.4f}; para 0.99: {v['req99']:.4f}")
    print(f"Con propulsion y actitud duplicadas: formula {v['R_red']:.4f}; Monte Carlo {v['mc_red']:.4f} +- {v['mc_red_err']:.4f}")
    print(f"Tiempo maximo de operacion para cumplir 0.90 sin redundancia: {v['t_max90']:.2f} anios")
    assert abs(v["R_serie"] - v["mc"]) < 3 * v["mc_err"] + 1e-4
    assert abs(v["R_red"] - v["mc_red"]) < 3 * v["mc_red_err"] + 1e-4
    assert abs(r_serie(TASAS, v["t_max90"]) - 0.90) < 1e-12
    print("Pruebas superadas (formula en serie y paralelo contra Monte Carlo a 3 errores estandar).")


if __name__ == "__main__":
    main()
