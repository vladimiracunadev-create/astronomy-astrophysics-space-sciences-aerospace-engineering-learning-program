"""B59-C06 · Energía de extraer agua de un regolito con hielo por calentamiento.

Datos: abundancia de hielo 5,6 % en masa (OBSERVADA por LCROSS en un sitio; Colaprete et al. 2010, resumen,
consultada 2026-11-09). Todo lo demás es ILUSTRATIVO (no consultado): calor específico del regolito
cp = 150 + 2,5 T [J/(kg K)], del hielo cp = 7,5 T, calor latente de sublimación L = 2,83 MJ/kg,
temperaturas inicial 100 K, del hielo 250 K y del regolito 350 K, eficiencia de captura de calor 50 %.
Modelo: balance de energía por kilogramo de agua extraída: calentar el regolito seco, calentar el hielo
hasta la temperatura de sublimación y sublimarlo. Sin pérdidas de vapor, sin conducción en el lecho.
Se compara la fórmula cerrada (integral de un polinomio) con la regla del trapecio.
Unidades: J, kg, K; energía final en kWh (1 kWh = 3,6 MJ exactos).
Tolerancia: fórmula cerrada frente a trapecio < 1e-6 relativo.
"""
import platform

X = 0.056                      # fraccion masica de hielo, observada (S1)
T0, T_ICE, T_REG = 100.0, 250.0, 350.0
L_SUB = 2.83e6                 # J/kg, ILUSTRATIVO
ETA = 0.5                      # ILUSTRATIVA


def cp_reg(T): return 150.0 + 2.5 * T
def cp_ice(T): return 7.5 * T


def trapecio(f, a, b, n=20000):
    h = (b - a) / n
    return h * (0.5 * f(a) + sum(f(a + i * h) for i in range(1, n)) + 0.5 * f(b))


def energia_por_kg_agua(x, t_reg=T_REG, rec=1.0):
    """Joules de calor en el material por kg de agua RECUPERADA."""
    m_reg = (1.0 - x) / x                          # kg de regolito seco por kg de hielo
    q_reg = m_reg * (150.0 * (t_reg - T0) + 1.25 * (t_reg ** 2 - T0 ** 2))
    q_ice = 3.75 * (T_ICE ** 2 - T0 ** 2)
    q_sub = L_SUB
    return (q_reg + q_ice + q_sub) / rec, q_reg, q_ice, q_sub


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    q, qr, qi, qs = energia_por_kg_agua(X)
    print(f"Regolito seco por kg de hielo = {(1-X)/X:.2f} kg")
    print(f"Calor al regolito = {qr/1e6:.3f} MJ ; al hielo = {qi/1e6:.3f} MJ ; sublimacion = {qs/1e6:.3f} MJ ; total = {q/1e6:.3f} MJ por kg de agua")
    print(f"Reparto: regolito {100*qr/q:.1f} % ; hielo {100*qi/q:.1f} % ; sublimacion {100*qs/q:.1f} %")
    # Prueba: trapecio
    m_reg = (1 - X) / X
    q_num = m_reg * trapecio(cp_reg, T0, T_REG) + trapecio(cp_ice, T0, T_ICE) + L_SUB
    err = abs(q_num - q) / q
    print(f"Total por trapecio = {q_num/1e6:.6f} MJ ; error relativo = {err:.1e}")
    assert err < 1e-6
    kwh_calor = q / 3.6e6
    kwh_el = kwh_calor / ETA
    print(f"Energia termica = {kwh_calor:.3f} kWh/kg ; con eficiencia de captura {100*ETA:.0f} % = {kwh_el:.3f} kWh/kg de agua")
    # Sensibilidad a la abundancia y a la temperatura del regolito
    print("abundancia x [%]   regolito seco [kg/kg]   energia total [MJ/kg agua]")
    for x in (0.027, 0.056, 0.085, 0.15):
        qx = energia_por_kg_agua(x)[0]
        print(f"{100*x:12.1f}   {(1-x)/x:18.2f}   {qx/1e6:22.3f}")
    # Recuperacion parcial: si solo se libera el 90 % del hielo, la energia por kg recuperado sube
    q90 = energia_por_kg_agua(X, rec=0.9)[0]
    print(f"Con 90 % de recuperacion: {q90/1e6:.3f} MJ por kg de agua recuperada ({100*(q90/q-1):+.1f} %)")
    assert abs(q90 / q - 1 / 0.9) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
