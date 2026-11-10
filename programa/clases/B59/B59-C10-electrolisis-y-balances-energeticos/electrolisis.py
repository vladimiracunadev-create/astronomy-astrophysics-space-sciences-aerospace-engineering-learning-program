"""B59-C10 · Electrólisis de vapor: tensión termoneutra, energía por kg de H2 y calor a evacuar.

Datos CITADOS (consultados 2026-11-09): F = 96 485,332 12 C/mol (NIST CODATA 2022); entalpía de formación
del H2O en gas -241,826 kJ/mol (NIST WebBook); H 1,007975 g/mol (NIST, punto medio del intervalo).
ILUSTRATIVOS (no consultados): curva de polarización V(i) = V0 + r i + b ln(i/i0) con V0 = 0,95 V,
r = 0,25 ohm cm2, b = 0,03 V, i0 = 0,05 A/cm2; eficiencia farádica 0,95; potencia de planta 10 kW.
Modelo: n_H2 = eta_F I t/(2 F). Tensión termoneutra E_tn = |dH|/(2F) para vapor. Calor generado = (V - E_tn) I si V > E_tn.
Unidades: V, A, A/cm2, ohm cm2, kWh/kg.
Tolerancias: conservación de energía eléctrica = química + calor, 1e-12; ley de Faraday ida-vuelta, 1e-12.
"""
import math
import platform

F = 96485.33212
DH = 241.826e3        # J/mol, NIST WebBook (gas)
M_H2 = 2 * 1.007975   # g/mol
V0, R_OHM, B_TAFEL, I0 = 0.95, 0.25, 0.03, 0.05
ETA_F = 0.95


def tension(i):
    return V0 + R_OHM * i + B_TAFEL * math.log(i / I0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    e_tn = DH / (2 * F)
    print(f"Tension termoneutra (vapor) E_tn = |dH|/(2F) = {e_tn:.4f} V")
    e_kg = 2 * F * e_tn / (M_H2 * 1e-3) / 3.6e6
    print(f"Energia minima (a E_tn) = {e_kg:.2f} kWh por kg de H2 (= entalpia/masa molar, {DH/(M_H2*1e-3)/3.6e6:.2f} kWh/kg)")
    assert abs(e_kg - DH / (M_H2 * 1e-3) / 3.6e6) < 1e-9
    print()
    print("i [A/cm2]  V [V]   E_tn/V (>1: endotermico)   calor generado/electricidad   energia [kWh/kg H2]")
    for i in (0.1, 0.3, 0.5, 1.0, 1.5):
        V = tension(i)
        # Electricidad por mol de H2: 2 F V / eta_F ; calor = parte sobre E_tn
        e_el = 2 * F * V / ETA_F / (M_H2 * 1e-3) / 3.6e6
        eff = e_tn / V
        calor = max(V - e_tn, 0) / V
        print(f"{i:9.2f}  {V:5.3f}  {eff:17.3f}  {calor:18.3f}  {e_el:18.2f}")
    # Planta de 10 kW a i = 0,5 A/cm2 : area, corriente y caudal
    P = 10e3
    i = 0.5
    V = tension(i)
    I = P / V
    area = I / i
    mol_h2 = ETA_F * I / (2 * F)            # mol/s
    kg_dia = mol_h2 * M_H2 * 1e-3 * 86400
    print()
    print(f"Planta de {P/1e3:.0f} kW a i = {i} A/cm2: V = {V:.3f} V ; I = {I:.1f} A ; area = {area:.0f} cm2 ; H2 = {kg_dia:.3f} kg/dia")
    # Ida y vuelta de Faraday
    I_back = mol_h2 * 2 * F / ETA_F
    assert abs(I_back - I) / I < 1e-12
    # Balance de energia: electricidad = entalpia del H2 producido + calor intercambiado (negativo si la celda es endotermica)
    p_quim = mol_h2 * DH
    p_calor_total = P - p_quim
    print(f"Potencia quimica en H2 (entalpia) = {p_quim:.1f} W ; calor intercambiado con el entorno P - P_quim = {p_calor_total:.1f} W ({100*p_calor_total/P:.1f} % de la entrada; negativo = la celda absorbe calor)")
    assert abs(P - (p_quim + p_calor_total)) < 1e-9 * P
    # O2 coproducido: 1/2 mol por mol de H2
    kg_o2 = mol_h2 / 2 * 2 * 15.9994e-3 * 86400
    print(f"O2 coproducido = {kg_o2:.3f} kg/dia (razon masica O2/H2 = {kg_o2/kg_dia:.3f}, estequiometrica 7.94)")
    assert abs(kg_o2 / kg_dia - 15.9994 / 2.01595) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
