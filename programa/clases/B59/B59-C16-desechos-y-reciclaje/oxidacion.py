"""B59-C16 · Reciclaje de residuos: balance elemental de la oxidación completa y oxígeno necesario.

Datos citados (consultados 2026-11-09): pesos atómicos NIST, punto medio del intervalo cuando se da uno
(H 1,007975 ; C 12,0106 ; N 14,006855 ; O 15,9994).
ILUSTRATIVOS (no consultados): fórmula empírica del residuo seco CH1.8 O0.6 N0.1 (sintética), 0,5 kg de
residuo seco por persona y día, humedad del residuo húmedo 70 % en masa, tripulación de 4.
Reacción: CHaObNc + (1 + a/4 - b/2) O2 -> CO2 + (a/2) H2O + (c/2) N2.
Se verifica la fórmula resolviendo el sistema de balance de elementos (4 ecuaciones, 4 incógnitas: O2, CO2, H2O, N2)
por eliminación gaussiana, de forma independiente.
Unidades: mol, kg. Tolerancia: fórmula frente a sistema lineal < 1e-12; cierre de masa < 1e-12.
"""
import platform

M = {"H": 1.007975, "C": 12.0106, "N": 14.006855, "O": 15.9994}
A_H, B_O, C_N = 1.8, 0.6, 0.1
KG_SECO_PERSONA = 0.5
HUMEDAD = 0.70
N_TRIP = 4


def mm_residuo():
    return M["C"] + A_H * M["H"] + B_O * M["O"] + C_N * M["N"]


def resolver(A, b):
    n = len(b)
    A = [fila[:] for fila in A]
    b = b[:]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[p] = A[p], A[i]
        b[i], b[p] = b[p], b[i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= f * A[i][c]
            b[r] -= f * b[i]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (b[i] - sum(A[i][c] * x[c] for c in range(i + 1, n))) / A[i][i]
    return x


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    mm = mm_residuo()
    print(f"Residuo seco CH{A_H}O{B_O}N{C_N}: masa molar por 'atomo de C' = {mm:.4f} g/mol")
    # Formula
    o2 = 1 + A_H / 4 - B_O / 2
    co2, h2o, n2 = 1.0, A_H / 2, C_N / 2
    print(f"Por mol de CHaObNc: O2 = {o2:.4f} mol ; CO2 = {co2:.4f} ; H2O = {h2o:.4f} ; N2 = {n2:.4f}")
    # Sistema lineal independiente. Incognitas x=(O2, CO2, H2O, N2); ecuaciones C, H, O, N:
    # C: CO2 = 1 ; H: 2 H2O = a ; O: 2 O2 + b = 2 CO2 + H2O ; N: 2 N2 = c
    A = [[0, 1, 0, 0], [0, 0, 2, 0], [2, -2, -1, 0], [0, 0, 0, 2]]
    b = [1.0, A_H, -B_O, C_N]
    x = resolver(A, b)
    print(f"Sistema lineal: O2 = {x[0]:.4f} ; CO2 = {x[1]:.4f} ; H2O = {x[2]:.4f} ; N2 = {x[3]:.4f}")
    for u, v in zip(x, (o2, co2, h2o, n2)):
        assert abs(u - v) < 1e-12
    # Masas por kg de residuo seco
    n = 1000.0 / mm
    kg = lambda m_molar, coef: n * coef * m_molar / 1000.0
    m_o2 = kg(2 * M["O"], o2)
    m_co2 = kg(M["C"] + 2 * M["O"], co2)
    m_h2o = kg(2 * M["H"] + M["O"], h2o)
    m_n2 = kg(2 * M["N"], n2)
    print(f"Por kg de residuo seco: O2 = {m_o2:.4f} kg ; CO2 = {m_co2:.4f} ; H2O = {m_h2o:.4f} ; N2 = {m_n2:.4f}")
    cierre = 1.0 + m_o2 - (m_co2 + m_h2o + m_n2)
    print(f"Cierre de masa: entra {1.0 + m_o2:.6f} kg ; sale {m_co2 + m_h2o + m_n2:.6f} kg ; diferencia {cierre:.1e}")
    assert abs(cierre) < 1e-12
    # Tripulacion
    seco = N_TRIP * KG_SECO_PERSONA
    humedo = seco / (1 - HUMEDAD)
    agua_humedad = humedo - seco
    print(f"Tripulacion de {N_TRIP}: residuo seco = {seco:.2f} kg/dia ; residuo humedo (70 % de agua) = {humedo:.2f} kg/dia ; agua de humedad = {agua_humedad:.2f} kg/dia")
    print(f"Oxidar el seco consume O2 = {seco*m_o2:.3f} kg/dia ; produce CO2 = {seco*m_co2:.3f} ; H2O = {seco*m_h2o:.3f} ; N2 = {seco*m_n2:.3f} kg/dia")
    print(f"Agua total recuperable (humedad + reaccion) = {agua_humedad + seco*m_h2o:.3f} kg/dia")
    print(f"Fraccion del residuo humedo que se recupera como agua = {100*(agua_humedad + seco*m_h2o)/humedo:.1f} %")
    # Carbono: toda la masa de carbono pasa a CO2
    c_in = seco * M["C"] / mm
    c_out = seco * m_co2 * M["C"] / (M["C"] + 2 * M["O"])
    print(f"Carbono: entra {c_in:.4f} kg/dia ; sale en CO2 {c_out:.4f} kg/dia")
    assert abs(c_in - c_out) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
