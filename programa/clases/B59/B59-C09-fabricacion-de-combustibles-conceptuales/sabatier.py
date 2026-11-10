"""B59-C09 · Combustible conceptual O2/CH4: reacción de Sabatier, lazo de agua y balance de hidrógeno.

Datos CITADOS (consultados 2026-11-09): entalpías de formación en gas, NIST WebBook (kJ/mol):
CO2 -393,51 ; CH4 -74,87 ; H2O -241,826. Masas molares NIST WebBook: H2O 18,0153 ; CO2 44,0095 ; CH4 16,0425.
Pesos atómicos NIST (punto medio del intervalo): H 1,007975 ; O 15,9994.
ILUSTRATIVO (no consultado): razón de mezcla O/F = 3,5; propelente objetivo 1 000 kg.
Reacciones: Sabatier CO2 + 4 H2 -> CH4 + 2 H2O ; electrólisis 2 H2O -> 2 H2 + O2.
Se verifica la conservación de elementos con una matriz y se compara el hidrógeno importado con la
fórmula analítica. Entalpía de reacción con agua en estado gas (no incluye cambio de fase).
Unidades: mol, kg, kJ, kWh. Tolerancia: conservación de elementos < 1e-9 relativo.
"""
import platform

HF = {"CO2": -393.51, "CH4": -74.87, "H2O": -241.826}      # kJ/mol, NIST WebBook (gas)
M = {"H": 1.007975, "C": 12.0106, "O": 15.9994}
FORM = {"CO2": {"C": 1, "O": 2}, "CH4": {"C": 1, "H": 4}, "H2O": {"H": 2, "O": 1}, "H2": {"H": 2}, "O2": {"O": 2}}


def masa_molar(esp):
    return sum(n * M[e] for e, n in FORM[esp].items())


def elementos(coefs):
    tot = {"C": 0.0, "H": 0.0, "O": 0.0}
    for esp, c in coefs.items():
        for e, n in FORM[esp].items():
            tot[e] += c * n
    return tot


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for e in ("CO2", "CH4", "H2O", "H2", "O2"):
        print(f"M({e}) = {masa_molar(e):.4f} g/mol")
    assert abs(masa_molar("CH4") - 16.0425) < 5e-3 and abs(masa_molar("H2O") - 18.0153) < 5e-3 and abs(masa_molar("CO2") - 44.0095) < 5e-3
    # Sabatier: conservacion de elementos (reactivos - productos)
    izq = elementos({"CO2": 1, "H2": 4})
    der = elementos({"CH4": 1, "H2O": 2})
    print(f"Sabatier: elementos izquierda {izq} ; derecha {der}")
    assert izq == der
    dH = HF["CH4"] + 2 * HF["H2O"] - HF["CO2"]
    print(f"Entalpia de la reaccion de Sabatier (agua en gas) = {dH:.2f} kJ/mol de CH4 (exotermica)")
    assert abs(dH - (-165.01)) < 0.01
    # Propelente objetivo
    prop, OF = 1000.0, 3.5
    ch4 = prop / (1 + OF)
    o2 = prop - ch4
    n_ch4 = ch4 * 1000 / masa_molar("CH4")
    print(f"Propelente {prop:.0f} kg con O/F = {OF}: CH4 = {ch4:.1f} kg ({n_ch4:.0f} mol) ; O2 = {o2:.1f} kg")
    # Sabatier
    n_co2, n_h2, n_h2o = n_ch4, 4 * n_ch4, 2 * n_ch4
    kg = lambda n, e: n * masa_molar(e) / 1000
    print(f"Sabatier consume CO2 = {kg(n_co2,'CO2'):.1f} kg y H2 = {kg(n_h2,'H2'):.1f} kg ; produce H2O = {kg(n_h2o,'H2O'):.1f} kg")
    # Electrolisis del agua del lazo
    n_h2_rec, n_o2_el = n_h2o, n_h2o / 2
    print(f"Electrolisis del agua del lazo: H2 recuperado = {kg(n_h2_rec,'H2'):.1f} kg ; O2 = {kg(n_o2_el,'O2'):.1f} kg")
    h2_imp = n_h2 - n_h2_rec
    print(f"Hidrogeno a importar = {kg(h2_imp,'H2'):.1f} kg ({100*h2_imp/n_h2:.0f} % del que consume Sabatier)")
    assert abs(h2_imp - 2 * n_ch4) < 1e-6 * n_ch4
    # Balance global de elementos del lazo: entran CO2 + H2 importado ; salen CH4 + O2 (de la electrolisis)
    entra = elementos({"CO2": n_co2, "H2": h2_imp})
    sale = elementos({"CH4": n_ch4, "O2": n_o2_el})
    print(f"Lazo cerrado: entran {entra} ; salen {sale}")
    for e in "CHO":
        assert abs(entra[e] - sale[e]) / entra[e] < 1e-9
    o2_falta = o2 - kg(n_o2_el, "O2")
    print(f"O2 del lazo = {kg(n_o2_el,'O2'):.1f} kg ; falta para O/F = {o2_falta:.1f} kg que debe venir de otro proceso (C08)")
    calor = -dH * n_ch4
    print(f"Calor de Sabatier a evacuar = {calor/1e6:.3f} GJ = {calor/3600:.0f} kWh termicos")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
