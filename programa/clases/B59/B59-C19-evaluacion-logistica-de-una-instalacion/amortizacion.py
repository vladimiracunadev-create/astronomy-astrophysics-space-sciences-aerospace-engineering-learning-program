"""B59-C19 · Evaluación logística: tiempo de amortización de la masa de una planta con paradas.

Datos ILUSTRATIVOS (no consultados): masa de la planta 2 000 kg (sin potencia), potencia 12 kW con masa
específica de 30 kg/kW, producción nominal 10 kg/día de producto, apalancamiento de lanzamiento G = 6 kg en
LEO por kg aterrizado (el mismo para planta y para el producto evitado), MTBF 600 h y MTTR 48 h (exponenciales).
Modelo: la planta se amortiza cuando la masa evitada iguala la masa lanzada: t* = M_total/(q u), con
u = MTBF/(MTBF + MTTR) la disponibilidad. Se contrasta con una simulación de procesos de renovación
(exponenciales) y se obtienen percentiles de t*.
Unidades: kg, días, horas. Sin reposición de piezas, sin degradación de la producción, sin costes de operación.
Tolerancias: disponibilidad simulada frente a analítica < 1 %; t* mediano simulado frente a analítico < 3 %.
"""
import math
import platform
import random

M_PLANTA, P_KW, ESP = 2000.0, 12.0, 30.0
Q = 10.0
G = 6.0
MTBF, MTTR = 600.0, 48.0
SEMILLA = 20261109


def amortizacion_dia(m_total, q, u):
    return m_total / (q * u)


def simular(m_total, q, rng, horizonte_dias=4000):
    """Devuelve el dia en que la masa acumulada de producto iguala a m_total (con paradas)."""
    t = 0.0           # horas
    prod = 0.0
    en_marcha = True
    while True:
        dur = rng.expovariate(1 / (MTBF if en_marcha else MTTR))
        if en_marcha:
            horas_req = (m_total - prod) / q * 24.0
            if dur >= horas_req:
                return (t + horas_req) / 24.0
            prod += q * dur / 24.0
        t += dur
        en_marcha = not en_marcha
        if t / 24.0 > horizonte_dias:
            return float("inf")


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m_pot = P_KW * ESP
    m_tot = M_PLANTA + m_pot
    u = MTBF / (MTBF + MTTR)
    print(f"Masa total = planta {M_PLANTA:.0f} + potencia {m_pot:.0f} = {m_tot:.0f} kg ; disponibilidad u = {u:.4f}")
    t_ideal = m_tot / Q
    t_an = amortizacion_dia(m_tot, Q, u)
    print(f"Amortizacion ideal (u = 1) = {t_ideal:.0f} dias ; con paradas = {t_an:.0f} dias ({t_an/365.25:.2f} anos)")
    print(f"Masa lanzada en LEO equivalente = {G*m_tot:.0f} kg ; masa en LEO evitada por dia = {G*Q*u:.1f} kg")
    rng = random.Random(SEMILLA)
    n = 6000
    ts = sorted(simular(m_tot, Q, rng) for _ in range(n))
    p10, p50, p90 = ts[int(0.1 * n)], ts[int(0.5 * n)], ts[int(0.9 * n)]
    print(f"Simulacion ({n} corridas): P10 = {p10:.0f} ; P50 = {p50:.0f} ; P90 = {p90:.0f} dias")
    assert abs(p50 - t_an) / t_an < 0.03
    # Disponibilidad simulada
    rng2 = random.Random(SEMILLA + 7)
    horas = 0.0
    marcha = 0.0
    estado = True
    while horas < 5e6:
        d = rng2.expovariate(1 / (MTBF if estado else MTTR))
        horas += d
        if estado:
            marcha += d
        estado = not estado
    u_sim = marcha / horas
    print(f"Disponibilidad simulada = {u_sim:.4f} (analitica {u:.4f})")
    assert abs(u_sim - u) / u < 0.01
    # Sensibilidad
    print("Sensibilidad del tiempo de amortizacion (analitica):")
    for nombre, mt, q, uu in (("MTTR x2 (96 h)", m_tot, Q, MTBF / (MTBF + 2 * MTTR)),
                              ("produccion -30 %", m_tot, 0.7 * Q, u),
                              ("masa de potencia +50 %", M_PLANTA + 1.5 * m_pot, Q, u)):
        print(f"  {nombre:24s}: {amortizacion_dia(mt, q, uu):6.0f} dias")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
