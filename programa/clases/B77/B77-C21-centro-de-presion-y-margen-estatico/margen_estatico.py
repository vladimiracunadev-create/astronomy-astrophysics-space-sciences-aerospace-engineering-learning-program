#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C21: centro de presion y margen estatico de un lanzador SINTETICO.

Datos consultados (2026-11-10): criterio de estabilidad de la NASA Glenn (Rocket Stability): estable cuando el centro de presion esta por detras del centro de gravedad
(en la pagina, 'por debajo' en el dibujo vertical); el centro de presion es el punto donde actuan sustentacion y arrastre; el centro de gravedad es el punto alrededor del cual rota el cohete.
La formula de Barrowman y las posiciones de centro de presion por forma de ojiva NO se consultaron: se usan valores de componente INVENTADOS.
SINTETICOS / ILUSTRATIVOS (inventados): vehiculo de 20 m y diametro de referencia d = 1.5 m; coordenada x desde la punta hacia atras (m); componentes aerodinamicos con su pendiente de fuerza normal
CN_alfa (1/rad, referida al area de referencia) y su posicion x_cp: ojiva (2.0 en 1.40 m), cuerpo cilindrico (0 en 10 m), 4 aletas (6.0 en 18.2 m); masas y posiciones para el centro de gravedad.
Datos de tunel sinteticos (semilla 21, sigma = 0.01 en CN y en Cm, alfa de -4 a +4 grados).
Sistema: plano de cabeceo, x desde la punta, margen estatico en calibres = (x_cp - x_cg)/d positivo si el centro de presion esta detras del centro de gravedad; SI.
Modelo: x_cp = sum(CN_i x_i)/sum(CN_i); x_cg = sum(m_i x_i)/sum(m_i); Cm_alfa (respecto del CG) = -CN_alfa (x_cp - x_cg)/d.
Segunda via: ajuste por minimos cuadrados de CN(alfa) y Cm(alfa) a los datos de tunel sinteticos; margen estatico = -Cm_alfa/CN_alfa; barrido del tamano de aletas.
Tolerancias: margen ajustado frente al exacto dentro de 3 sigma; Cm_alfa por componentes frente al de diferencias finitas 1e-9.
"""
import math, platform, random

D = 1.5
COMP = [("ojiva", 2.0, 1.40), ("cuerpo", 0.0, 10.0), ("aletas", 6.0, 18.2)]
MASAS = [("carga util y ojiva", 1500.0, 2.0), ("tanque superior", 9000.0, 7.0), ("tanque inferior", 30000.0, 14.0), ("motor y estructura", 6000.0, 19.0)]


def cp(comp):
    return sum(c * x for _, c, x in comp) / sum(c for _, c, _ in comp)


def cg(masas):
    return sum(m * x for _, m, x in masas) / sum(m for _, m, _ in masas)


def momento_cg(alfa, comp, xcg):
    """Cm respecto del CG a partir de las fuerzas normales de cada componente: CN_i = CN_alfa_i alfa; momento = -CN_i (x_i - xcg)/d."""
    return sum(-c * alfa * (x - xcg) / D for _, c, x in comp)


def ajuste(x, y):
    n = len(x)
    sx, sy = sum(x), sum(y)
    sxx, sxy = sum(a * a for a in x), sum(a * b for a, b in zip(x, y))
    b = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    a = (sy - b * sx) / n
    s2 = sum((yi - (a + b * xi)) ** 2 for xi, yi in zip(x, y)) / (n - 2)
    return b, math.sqrt(s2 * n / (n * sxx - sx * sx))


def calcular():
    r = {}
    r["xcp"], r["xcg"] = cp(COMP), cg(MASAS)
    r["cna"] = sum(c for _, c, _ in COMP)
    r["sm"] = (r["xcp"] - r["xcg"]) / D
    r["cma"] = -r["cna"] * r["sm"]
    h = 1e-4
    r["cma_fd"] = (momento_cg(h, COMP, r["xcg"]) - momento_cg(-h, COMP, r["xcg"])) / (2 * h)
    r["err_fd"] = abs(r["cma_fd"] - r["cma"]) / abs(r["cma"])
    rnd = random.Random(21)
    al = [math.radians(a) for a in range(-4, 5)]
    cn = [r["cna"] * a + rnd.gauss(0, 0.01) for a in al]
    cm = [r["cma"] * a + rnd.gauss(0, 0.01) for a in al]
    cna_f, s_cn = ajuste(al, cn)
    cma_f, s_cm = ajuste(al, cm)
    r["cna_fit"], r["s_cn"], r["cma_fit"], r["s_cm"] = cna_f, s_cn, cma_f, s_cm
    r["sm_fit"] = -cma_f / cna_f
    # incertidumbre del margen por propagacion de primer orden
    r["s_sm"] = abs(r["sm_fit"]) * math.sqrt((s_cm / cma_f) ** 2 + (s_cn / cna_f) ** 2)
    r["ok_sm"] = abs(r["sm_fit"] - r["sm"]) < 3 * r["s_sm"]
    # barrido de aletas
    r["barrido"] = []
    for cn_f in (0.0, 1.0, 2.0, 4.0, 6.0, 8.0):
        comp = [COMP[0], COMP[1], ("aletas", cn_f, COMP[2][2])]
        r["barrido"].append((cn_f, cp(comp), (cp(comp) - r["xcg"]) / D))
    # CG durante el quemado: se retira propelente del tanque inferior
    r["cg_fin"] = cg([MASAS[0], MASAS[1], ("tanque inferior vacio", 1500.0, 14.0), MASAS[3]])
    r["sm_fin"] = (r["xcp"] - r["cg_fin"]) / D
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Vehiculo SINTETICO: d = {D} m; componentes (CN_alfa [1/rad], x_cp [m]): " + "; ".join(f"{n} {c} en {x}" for n, c, x in COMP))
    print(f"CN_alfa total = {r['cna']:.3f} /rad; centro de presion x_cp = {r['xcp']:.4f} m; centro de gravedad x_cg = {r['xcg']:.4f} m")
    print(f"Margen estatico = {r['sm']:.4f} calibres; Cm_alfa = {r['cma']:.4f} /rad (por componentes) y {r['cma_fd']:.4f} (diferencias finitas, error {r['err_fd']:.1e})")
    print(f"Ajuste a datos SINTETICOS de tunel (semilla 21): CN_alfa = {r['cna_fit']:.3f} +- {r['s_cn']:.3f}; Cm_alfa = {r['cma_fit']:.3f} +- {r['s_cm']:.3f}; margen = {r['sm_fit']:.3f} +- {r['s_sm']:.3f} calibres")
    print("Barrido del CN_alfa de las aletas -> x_cp [m], margen [calibres]: " + "; ".join(f"{c:.0f} -> {x:.2f}, {m:+.2f}" for c, x, m in r["barrido"]))
    print(f"Con el propelente del tanque inferior consumido (queda 1500 kg de estructura): x_cg = {r['cg_fin']:.3f} m; margen = {r['sm_fin']:.3f} calibres")
    assert r["err_fd"] < 1e-9 and r["ok_sm"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
