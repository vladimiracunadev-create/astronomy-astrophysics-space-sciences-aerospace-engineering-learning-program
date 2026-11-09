"""B59-C21 · Almacenamiento criogénico: fuga de calor por radiación, evaporación y refrigerador.

Datos: constante de Stefan–Boltzmann 5,670 374 419e-8 W/(m² K⁴) (NIST CODATA 2022, consultada 2026-11-09).
Todo lo demás es ILUSTRATIVO (no consultado): tanque esférico de radio 1,0 m con oxígeno líquido a 90 K,
densidad 1 141 kg/m³, calor latente de evaporación 213 kJ/kg, emisividad efectiva del aislamiento multicapa
0,005, ambiente sintético T(t) = 250 + 100 sin(2π t/P) K con P = 29,5 días, fracción de Carnot del
refrigerador 0,20 y rechazo de calor a 250 K.
Modelo: Q(t) = eps*sigma*A*(T_amb^4 - T_t^4); pérdida de masa m_dot = Q/L; el refrigerador de cero evaporación
extrae Q con potencia eléctrica P_e = Q (T_h - T_c)/(T_c * f_Carnot). Sin conducción por soportes ni tuberías.
Unidades SI. Sistema: tanque en la superficie, un ciclo día–noche.
Tolerancia: media numérica de T^4 frente a la fórmula analítica < 1e-6 relativo.
"""
import math
import platform

SIGMA = 5.670374419e-8      # W/(m^2 K^4), NIST CODATA 2022
R = 1.0                     # m, ILUSTRATIVO
T_T = 90.0                  # K
RHO = 1141.0                # kg/m^3, ILUSTRATIVO
L_V = 213e3                 # J/kg, ILUSTRATIVO
EPS = 0.005                 # ILUSTRATIVA
T0, AMP, P_DIAS = 250.0, 100.0, 29.5
F_CARNOT, T_H = 0.20, 250.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    A = 4 * math.pi * R ** 2
    V = 4 / 3 * math.pi * R ** 3
    m_lox = RHO * V
    print(f"Area = {A:.3f} m^2 ; volumen = {V:.3f} m^3 ; masa de liquido = {m_lox:.0f} kg")
    P = P_DIAS * 86400.0
    n = 200000
    dt = P / n
    s4 = 0.0
    q_int = 0.0
    for i in range(n):
        t = (i + 0.5) * dt
        Ta = T0 + AMP * math.sin(2 * math.pi * t / P)
        s4 += Ta ** 4
        q_int += EPS * SIGMA * A * (Ta ** 4 - T_T ** 4) * dt
    media4_num = s4 / n
    media4_an = T0 ** 4 + 3 * T0 ** 2 * AMP ** 2 + 3 * AMP ** 4 / 8
    err = abs(media4_num - media4_an) / media4_an
    print(f"<T^4> numerica = {media4_num:.6e} K^4 ; analitica = {media4_an:.6e} K^4 ; error relativo = {err:.1e}")
    assert err < 1e-6
    q_med = q_int / P
    q_an = EPS * SIGMA * A * (media4_an - T_T ** 4)
    print(f"Fuga media Q = {q_med:.4f} W (analitica {q_an:.4f} W)")
    assert abs(q_med - q_an) / q_an < 1e-6
    perd_kg_dia = q_med / L_V * 86400
    print(f"Evaporacion media = {perd_kg_dia:.4f} kg/dia ; en un ciclo de {P_DIAS} dias = {perd_kg_dia*P_DIAS:.2f} kg ({100*perd_kg_dia*P_DIAS/m_lox:.2f} % del liquido)")
    # Extremos: noche (T = 150 K) y dia (350 K)
    for nombre, Ta in (("noche 150 K", 150.0), ("dia 350 K", 350.0)):
        q = EPS * SIGMA * A * (Ta ** 4 - T_T ** 4)
        print(f"Fuga en {nombre}: {q:.4f} W ({q/L_V*86400:.4f} kg/dia)")
    # Refrigerador de cero evaporacion
    cop_carnot = T_T / (T_H - T_T)
    p_el = q_med / (cop_carnot * F_CARNOT)
    print(f"COP de Carnot = {cop_carnot:.4f} ; potencia electrica para cero evaporacion = {p_el:.3f} W (media)")
    # Pico: para dimensionar, con la fuga maxima del dia
    qmax = EPS * SIGMA * A * ((T0 + AMP) ** 4 - T_T ** 4)
    print(f"Fuga maxima (T = {T0+AMP:.0f} K) = {qmax:.4f} W ; potencia de dimensionado = {qmax/(cop_carnot*F_CARNOT):.3f} W")
    # Vida de almacenamiento sin refrigerador hasta perder 10 %
    t10 = 0.10 * m_lox / (q_med / L_V) / 86400
    print(f"Tiempo para perder el 10 % sin refrigerador = {t10:.0f} dias")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
