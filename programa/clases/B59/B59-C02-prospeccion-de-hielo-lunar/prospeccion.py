"""B59-C02 · Abundancia de hielo a partir de una detección y propagación de su incertidumbre.

Datos OBSERVADOS (citados, consultados el 2026-11-09): Colaprete et al., Science 330 (2010) 463-468,
DOI 10.1126/science.1186986, resumen: vapor + hielo de agua máximo en el campo de visión 155 ± 12 kg;
abundancia de hielo en el sitio de impacto 5,6 ± 2,9 % en masa (Cabeus, cerca del polo sur lunar).
ILUSTRATIVO (no consultado): densidad aparente del regolito, espesor y área del depósito hipotético.
Modelo: abundancia = m_agua / m_regolito. Se despeja la masa de regolito proyectada y se propaga la
incertidumbre por (a) la fórmula lineal de primer orden y (b) Monte Carlo con semilla fija.
Supuestos: errores gaussianos e independientes (supuesto del ejercicio, no de la fuente).
Unidades: kg, fracción másica adimensional, m, m^3.
Tolerancia: la fórmula de primer orden y Monte Carlo coinciden en la desviación a menos de 5 %.
"""
import math
import platform
import random
import statistics

M_AGUA, S_AGUA = 155.0, 12.0     # kg, observado (Colaprete et al. 2010)
X, S_X = 0.056, 0.029            # fraccion masica, observada (5,6 +- 2,9 %)
RHO = 1500.0                     # kg/m^3, ILUSTRATIVO (densidad aparente del regolito)
AREA, ESPESOR = 1.0e6, 1.0       # m^2 y m, ILUSTRATIVOS (1 km^2 y 1 m)
SEMILLA = 20261109
N = 200000


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m_reg = M_AGUA / X
    # Primer orden: m_reg = m_agua / x -> (s_m/m)^2 = (s_a/m_a)^2 + (s_x/x)^2
    rel = math.hypot(S_AGUA / M_AGUA, S_X / X)
    s_m = m_reg * rel
    print(f"Regolito proyectado m_reg = m_agua/x = {m_reg:.0f} kg ; incertidumbre de primer orden = {s_m:.0f} kg ({100*rel:.1f} %)")

    rng = random.Random(SEMILLA)
    muestras = []
    while len(muestras) < N:
        a = rng.gauss(M_AGUA, S_AGUA)
        x = rng.gauss(X, S_X)
        if x > 0.005 and a > 0:       # se descartan abundancias no fisicas (truncamiento)
            muestras.append(a / x)
    media = statistics.fmean(muestras)
    sd = statistics.pstdev(muestras)
    muestras.sort()
    p16, p50, p84 = (muestras[int(q * N)] for q in (0.16, 0.50, 0.84))
    print(f"Monte Carlo ({N} sorteos, semilla {SEMILLA}): media = {media:.0f} kg ; desv. = {sd:.0f} kg ; mediana = {p50:.0f} kg")
    print(f"Percentiles 16/50/84 % del regolito: {p16:.0f} ; {p50:.0f} ; {p84:.0f} kg (distribucion asimetrica)")
    print(f"Cociente de primer orden / Monte Carlo (desviacion) = {s_m/sd:.3f}")
    # Hallazgo: con s_x/x = 52 % la relacion a/x es muy no lineal y el primer orden SUBESTIMA la dispersion.
    # La mediana, en cambio, se mantiene cerca del valor central (tolerancia 5 %).
    assert s_m / sd < 0.6, "se esperaba que el primer orden subestimara la dispersion"
    assert abs(p50 - m_reg) / m_reg < 0.05

    # Prueba analitica independiente del extremo bajo/alto de la abundancia
    lo_x, hi_x = X - S_X, X + S_X
    print(f"Con x = {100*lo_x:.1f} % el regolito seria {M_AGUA/lo_x:.0f} kg ; con x = {100*hi_x:.1f} %, {M_AGUA/hi_x:.0f} kg")
    assert abs(M_AGUA / X - 2767.857) < 0.01

    # Recurso hipotetico: deposito de 1 km^2 x 1 m con la misma abundancia (ILUSTRATIVO; no es un dato de Cabeus)
    m_dep = RHO * AREA * ESPESOR
    for nombre, f in (("central", X), ("inferior", lo_x), ("superior", hi_x)):
        print(f"Deposito hipotetico {nombre}: agua = {f*m_dep/1000:.0f} t")
    # Fraccion del campo de visión que el instrumento 'vio': agua observada / agua del deposito
    print(f"El agua observada ({M_AGUA:.0f} kg) es {100*M_AGUA/(X*m_dep):.4f} % del agua del deposito hipotetico central")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
