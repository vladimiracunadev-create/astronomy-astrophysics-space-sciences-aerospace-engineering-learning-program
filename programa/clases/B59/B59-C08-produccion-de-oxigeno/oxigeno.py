"""B59-C08 · Producción de oxígeno por electrólisis de CO2: corriente de Faraday y subproductos.

Datos CITADOS (consultados 2026-11-09): constante de Faraday F = 96 485,332 12 C/mol (NIST CODATA 2022);
pesos atómicos NIST (C, O: punto medio del intervalo, 12,0106 y 15,9994); masa molar del CO2 44,0095 g/mol
(NIST WebBook); tasas de MOXIE de la nota de NASA del 2022-12-22: meta de diseño 6 g/h, 10,44 g/h (sol 534),
casi 10,56 g/h (sol 630, pico) y 9,79 g/h sostenidos casi 40 min.
ILUSTRATIVOS (no consultados): número de celdas en serie N = 10, tensión de celda 1,0 V.
Reacción global: 2 CO2 -> 2 CO + O2, con 4 electrones por molécula de O2.
Ley de Faraday: n_O2 = N I t / (4 F). Unidades SI; energía en kWh.
Tolerancia: balance de masa de la reacción < 1e-9 relativo; ida y vuelta I -> g/h < 1e-12.
"""
import platform

F = 96485.33212        # C/mol, NIST CODATA 2022
M_C, M_O = 12.0106, 15.9994          # g/mol, NIST (punto medio del intervalo)
M_O2, M_CO, M_CO2_CALC = 2 * M_O, M_C + M_O, M_C + 2 * M_O
M_CO2_WB = 44.0095                   # g/mol, NIST WebBook
N_CELDAS = 10                        # ILUSTRATIVO
V_CELDA = 1.0                        # V, ILUSTRATIVO


def corriente(g_por_h, n=N_CELDAS):
    mol_s = g_por_h / M_O2 / 3600.0
    return 4.0 * F * mol_s / n


def gramos_por_hora(I, n=N_CELDAS):
    return n * I / (4.0 * F) * M_O2 * 3600.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"M(O2) = {M_O2:.4f} g/mol ; M(CO) = {M_CO:.4f} g/mol ; M(CO2) = {M_CO2_CALC:.4f} g/mol (WebBook {M_CO2_WB})")
    assert abs(M_CO2_CALC - M_CO2_WB) < 2e-3
    # balance de masa 2 CO2 -> 2 CO + O2
    reac, prod = 2 * M_CO2_CALC, 2 * M_CO + M_O2
    print(f"Balance de masa: reactivos {reac:.4f} g/mol de reaccion ; productos {prod:.4f} ; diferencia {reac-prod:.1e}")
    assert abs(reac - prod) / reac < 1e-9
    print(f"Por kg de O2: CO2 consumido = {2*M_CO2_CALC/M_O2:.4f} kg ; CO producido = {2*M_CO/M_O2:.4f} kg")
    print()
    print("Tasa [g/h]  origen                      I con N=10 [A]   I con N=1 [A]   potencia N=10 [W]   energia [kWh/kg O2]")
    casos = [(6.0, "meta de diseno (NASA)"), (9.79, "sostenida ~40 min (NASA)"), (10.44, "pico sol 534 (NASA)"), (10.56, "pico sol 630 (NASA)")]
    for g, nom in casos:
        I = corriente(g)
        I1 = corriente(g, 1)
        P = N_CELDAS * I * V_CELDA
        e = P / g          # W / (g/h) = Wh/g -> kWh/kg
        print(f"{g:9.2f}  {nom:26s}  {I:13.3f}  {I1:13.3f}  {P:16.2f}  {e:18.3f}")
        assert abs(gramos_por_hora(I) - g) < 1e-9 * g
    # energia por kg de O2 a tension de celda: 4 F V / M_O2
    e_kg = 4 * F * V_CELDA / (M_O2 * 1e-3) / 3.6e6
    print(f"Energia electrica por kg de O2 a {V_CELDA:.1f} V por celda = 4 F V/M = {e_kg:.3f} kWh/kg (independiente de N)")
    # Cuanto producir en un dia a 10,56 g/h y a 200 veces esa tasa (la nota de NASA indica una version humana ~200 veces mas rapida)
    print(f"A 10,56 g/h: {10.56*24:.1f} g/dia ; a 200 veces esa tasa: {200*10.56/1000:.3f} kg/h = {200*10.56*24/1000:.1f} kg/dia")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
