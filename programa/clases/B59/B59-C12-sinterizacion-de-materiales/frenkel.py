"""B59-C12 · Sinterización viscosa de Frenkel y ley de Arrhenius: ajuste de la energía de activación.

Datos: constante molar de los gases R = 8,314 462 618 J/(mol K) (NIST CODATA 2022, consultada 2026-11-09).
SINTÉTICOS / ILUSTRATIVOS (no consultados): tensión superficial gamma = 0,3 J/m^2, radio de partícula
a = 20 µm, viscosidad eta(T) = eta0 exp(Ea/(R T)) con Ea = 300 kJ/mol y eta = 1e8 Pa s a 1400 K,
ruido logarítmico del 3 %, calor específico medio 1 200 J/(kg K).
Modelo (Frenkel): (x/a)^2 = 3 gamma t / (2 eta a): tiempo para alcanzar una razón de cuello x/a dada
t = (x/a)^2 * 2 eta a/(3 gamma). Se ajusta ln t = c + (Ea/R)(1/T) por mínimos cuadrados.
Unidades SI, tiempo en s y h. Sin cristalización, sin porosidad cerrada, sin atmósfera.
Tolerancia: Ea recuperada a menos de 3 % de la sembrada; ajuste frente a regresión de dos pasos < 1e-9.
"""
import math
import platform
import random

R = 8.314462618
GAMMA, A = 0.3, 20e-6
EA = 300e3
ETA_REF, T_REF = 1e8, 1400.0
RATIO = 0.4
CP = 1200.0
SEMILLA = 20261109


def eta(T):
    return ETA_REF * math.exp(EA / R * (1 / T - 1 / T_REF))


def tiempo(T, ratio=RATIO):
    return ratio ** 2 * 2 * eta(T) * A / (3 * GAMMA)


def regresion(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return b, my - b * mx


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(SEMILLA)
    Ts = [1250.0, 1300.0, 1350.0, 1400.0, 1450.0, 1500.0, 1550.0]
    print("T [K]   eta [Pa s]   t exacto [h]   t con ruido [h]")
    datos = []
    for T in Ts:
        t_ex = tiempo(T)
        t_ru = t_ex * math.exp(rng.gauss(0, 0.03))
        datos.append((T, t_ru))
        print(f"{T:6.0f}  {eta(T):10.3e}  {t_ex/3600:12.3f}  {t_ru/3600:14.3f}")
    # Prueba 1: el tiempo exacto cumple Frenkel (x/a)^2 = 3 gamma t/(2 eta a)
    T = 1400.0
    chk = 3 * GAMMA * tiempo(T) / (2 * eta(T) * A)
    assert abs(chk - RATIO ** 2) < 1e-12
    print(f"Comprobacion de Frenkel a {T:.0f} K: (x/a)^2 = {chk:.4f} (esperado {RATIO**2:.4f})")
    # Ajuste
    x = [1 / T for T, _ in datos]
    y = [math.log(t) for _, t in datos]
    b, c = regresion(x, y)
    ea_aj = b * R
    err = abs(ea_aj - EA) / EA
    print(f"Energia de activacion ajustada = {ea_aj/1e3:.1f} kJ/mol (sembrada {EA/1e3:.0f}) ; error relativo = {100*err:.2f} %")
    assert err < 0.03
    # Ajuste con datos sin ruido: debe recuperar exactamente
    b0, _ = regresion(x, [math.log(tiempo(T)) for T in Ts])
    assert abs(b0 * R - EA) / EA < 1e-9
    print(f"Sin ruido el ajuste recupera Ea exactamente: {b0*R/1e3:.6f} kJ/mol")
    # Sensibilidad: cuanto sube el tiempo por cada 50 K
    print(f"Factor de tiempo entre 1400 y 1350 K = {tiempo(1350.0)/tiempo(1400.0):.2f} ; entre 1400 y 1450 K = {tiempo(1450.0)/tiempo(1400.0):.3f}")
    # Energia para calentar 1 kg de 300 K a T
    for T in (1350.0, 1400.0, 1450.0):
        e = CP * (T - 300.0)
        print(f"Calentar 1 kg de 300 a {T:.0f} K: {e/1e6:.3f} MJ = {e/3.6e6:.3f} kWh ; mantener {tiempo(T)/3600:.2f} h")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
