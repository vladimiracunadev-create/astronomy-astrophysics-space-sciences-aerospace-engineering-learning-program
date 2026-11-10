"""B67-C08: disponibilidad de volatiles con incertidumbre y generacion del informe (SINTETICO).

Masa disponible  M = A h rho w f_acc f_rec f_ret   [kg ; se informa en kt]
  A area [m2] ; h espesor [m] ; rho densidad aparente [kg/m3] ; w fraccion masica de hielo [-]
  f_acc fraccion accesible [-] ; f_rec recuperacion de la extraccion [-]
  f_ret fraccion retenida tras perdidas por sublimacion en manipulacion [-]
Cada factor es lognormal (mediana, sigma_ln) INVENTADA para la clase. Como el producto de
lognormales independientes es lognormal, hay solucion analitica:
  ln M ~ N(sum ln med_i , sum sigma_i^2)
Convencion del curso: P90 = valor superado con probabilidad 90 % (el lado conservador);
P10 = superado con probabilidad 10 %. (Convencion DIDACTICA; ninguna norma consultada.)
Requiere solo numpy y la biblioteca estandar.
"""
import math
import sys
import numpy as np

FACTORES = [
    # nombre, mediana, sigma_ln, unidad
    ("A", 4.0e6, 0.02, "m2"),
    ("h", 2.0, 0.15, "m"),
    ("rho", 1500.0, 0.05, "kg/m3"),
    ("w", 0.027, 0.20, "-"),
    ("f_acc", 0.60, 0.10, "-"),
    ("f_rec", 0.80, 0.08, "-"),
    ("f_ret", 0.95, 0.02, "-"),
]
Z = {10: 1.2815515655446004, 50: 0.0, 90: -1.2815515655446004}  # z de P10, P50, P90 (superacion)


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def parametros():
    mu = sum(math.log(m) for _, m, _, _ in FACTORES)
    sg = math.sqrt(sum(s * s for _, _, s, _ in FACTORES))
    return mu, sg


def cuantil_kt(p, mu, sg):
    return math.exp(mu + Z[p] * sg) / 1e6


def informe(mu, sg, demanda):
    p10, p50, p90 = (cuantil_kt(p, mu, sg) for p in (10, 50, 90))
    disp = 1 - phi((math.log(demanda * 1e6) - mu) / sg)
    comp = {n: s * s / sg ** 2 for n, _, s, _ in FACTORES}
    top = sorted(comp.items(), key=lambda kv: -kv[1])[:3]
    lines = [
        "# Informe de disponibilidad de volatiles - BLOQUE SINTETICO",
        "## 1. Alcance y datos",
        "Datos SINTETICOS inventados; no describen ningun sitio real. Unidades: kt de hielo disponible.",
        "## 2. Metodo",
        f"Producto de {len(FACTORES)} factores lognormales independientes; solucion analitica y Monte Carlo.",
        "## 3. Resultado con incertidumbre",
        f"P90 = {p90:.1f} kt ; P50 = {p50:.1f} kt ; P10 = {p10:.1f} kt (superacion con 90 %, 50 %, 10 %).",
        f"Probabilidad de disponer de al menos {demanda:.0f} kt: {100 * disp:.1f} %.",
        "## 4. Que domina la incertidumbre",
        "; ".join(f"{n}: {100 * v:.1f} %" for n, v in top) + " de la varianza de ln M.",
        "## 5. Limites",
        "Factores independientes y lognormales; sin correlacion espacial; sin costo ni calendario.",
    ]
    return "\n".join(lines), (p10, p50, p90, disp, comp)


def main():
    print(f"Python {sys.version.split()[0]} ; numpy {np.__version__}")
    print("DATOS SINTETICOS: medianas e incertidumbres inventadas para la clase")
    mu, sg = parametros()
    print(f"mu(ln M[kg]) = {mu:.4f} ; sigma_ln = {sg:.4f} ; mediana = {math.exp(mu) / 1e6:.2f} kt")
    rng = np.random.default_rng(6708)
    N = 400000
    lnM = np.zeros(N)
    ln_in = {}
    for n, m, s, _ in FACTORES:
        x = rng.normal(math.log(m), s, N)
        ln_in[n] = x
        lnM += x
    M = np.exp(lnM) / 1e6
    print("percentil   analitico [kt]   Monte Carlo [kt]   diferencia relativa")
    for p, q in ((10, 90), (50, 50), (90, 10)):
        an = cuantil_kt(p, mu, sg)
        mc = float(np.percentile(M, q))   # P90 (superacion 90 %) = percentil 10 de la distribucion
        print(f"  P{p}        {an:9.2f}        {mc:9.2f}          {100 * abs(an - mc) / an:.3f} %")
        assert abs(an - mc) / an < 0.01
    demanda = 150.0
    texto, (p10, p50, p90, disp, comp) = informe(mu, sg, demanda)
    mc_disp = float((M >= demanda).mean())
    print(f"Disponibilidad para {demanda:.0f} kt: analitica {100 * disp:.2f} % ; Monte Carlo {100 * mc_disp:.2f} %")
    assert abs(disp - mc_disp) < 0.005
    print("Contribucion a la varianza de ln M (analitica / correlacion^2 con ln M en MC):")
    for n, _, _, _ in FACTORES:
        r2 = float(np.corrcoef(ln_in[n], lnM)[0, 1] ** 2)
        print(f"  {n:6s} {100 * comp[n]:6.2f} %  /  {100 * r2:6.2f} %")
        assert abs(comp[n] - r2) < 0.01
    assert abs(sum(comp.values()) - 1) < 1e-12
    # calibracion: el intervalo [P90, P10] debe contener la verdad ~80 % de las veces
    # (verdad ~ distribucion de arriba; observacion = verdad con error lognormal sigma_o)
    sigma_o = 0.30
    n_rep = 100000
    verdad = rng.normal(0.0, 1.0, n_rep)          # en unidades de ln (centrado, escala libre)
    obs = verdad + rng.normal(0.0, sigma_o, n_rep)
    lo, hi = obs - 1.2815515655446004 * sigma_o, obs + 1.2815515655446004 * sigma_o
    cob = float(np.mean((verdad >= lo) & (verdad <= hi)))
    print(f"Calibracion del intervalo central al 80 % con error de medida sigma_ln = {sigma_o}: cobertura = {100 * cob:.2f} %")
    assert abs(cob - 0.80) < 0.01
    # el intervalo ingenuo con sigma subestimada (la mitad) no cubre
    lo2, hi2 = obs - 1.2815515655446004 * sigma_o / 2, obs + 1.2815515655446004 * sigma_o / 2
    cob2 = float(np.mean((verdad >= lo2) & (verdad <= hi2)))
    print(f"Con la incertidumbre declarada a la mitad, la cobertura cae a {100 * cob2:.2f} %")
    assert cob2 < 0.6
    # comprobaciones del texto del informe
    for sec in ("## 1. Alcance y datos", "## 2. Metodo", "## 3. Resultado con incertidumbre", "## 4.", "## 5. Limites"):
        assert sec in texto, sec
    assert "SINTETIC" in texto and "kt" in texto and p10 > p50 > p90
    print("---- informe generado ----")
    print(texto)
    print("---- fin del informe ----")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
