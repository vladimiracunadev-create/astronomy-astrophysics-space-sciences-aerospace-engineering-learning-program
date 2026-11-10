"""B59-C23 · Subproductos de procesos ISRU: balance estequiométrico por kilogramo de oxígeno.

Datos CITADOS (consultados 2026-11-09): pesos atómicos NIST (C 12,0106 ; O 15,9994 ; Fe 55,845 ; Ti 47,867 ;
H 1,007975; punto medio cuando NIST da un intervalo); masa molar del CO2 44,0095 g/mol (NIST WebBook).
MOXIE: 2 CO2 -> 2 CO + O2 (NASA, nota del 2022-12-22; la nota indica que el CO y el CO2 sin reaccionar salen por un segundo puerto).
ILUSTRATIVO (no consultado): reducción de ilmenita con hidrógeno FeTiO3 + H2 -> Fe + TiO2 + H2O como proceso
de ejemplo; fracción másica de ilmenita en el regolito = 0,10 (sintética).
Modelo: balance de elementos por reacción; flujos por kg de O2 producido (como O2 o como O del agua).
Unidades: kg, g/mol. Tolerancia: conservación de elementos < 1e-12 relativo.
"""
import platform

M = {"H": 1.007975, "C": 12.0106, "O": 15.9994, "Fe": 55.845, "Ti": 47.867}
FORM = {
    "CO2": {"C": 1, "O": 2}, "CO": {"C": 1, "O": 1}, "O2": {"O": 2},
    "FeTiO3": {"Fe": 1, "Ti": 1, "O": 3}, "Fe": {"Fe": 1}, "TiO2": {"Ti": 1, "O": 2},
    "H2": {"H": 2}, "H2O": {"H": 2, "O": 1},
}


def mm(s):
    return sum(n * M[e] for e, n in FORM[s].items())


def elementos(coefs):
    t = {}
    for s, c in coefs.items():
        for e, n in FORM[s].items():
            t[e] = t.get(e, 0.0) + c * n
    return t


def comprobar(izq, der):
    a, b = elementos(izq), elementos(der)
    for e in set(a) | set(b):
        assert abs(a.get(e, 0) - b.get(e, 0)) < 1e-12, f"no balancea {e}"


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1) MOXIE
    comprobar({"CO2": 2}, {"CO": 2, "O2": 1})
    co2 = 2 * mm("CO2") / mm("O2")
    co = 2 * mm("CO") / mm("O2")
    print(f"MOXIE por kg de O2: CO2 consumido = {co2:.4f} kg ; CO producido = {co:.4f} kg ; cierre {co2 - co - 1:.1e}")
    assert abs(co2 - co - 1.0) < 1e-12
    g_h = 10.56
    print(f"A 10,56 g/h de O2 el CO coproducido es {co*g_h:.2f} g/h")
    # 2) Ilmenita
    comprobar({"FeTiO3": 1, "H2": 1}, {"Fe": 1, "TiO2": 1, "H2O": 1})
    print()
    print("Reduccion de ilmenita con H2 (ejemplo ilustrativo): FeTiO3 + H2 -> Fe + TiO2 + H2O")
    for s in ("FeTiO3", "Fe", "TiO2", "H2", "H2O"):
        print(f"  M({s}) = {mm(s):.4f} g/mol")
    m_o = M["O"]
    # 1 kg de O = 1000 g / M_O mol de atomos; cada mol de ilmenita libera 1 mol de O (como agua)
    n_reac = 1000.0 / m_o
    kg = lambda s, n=n_reac: n * mm(s) / 1000.0
    print(f"Por kg de O (como agua, luego electrolizada a O2): ilmenita = {kg('FeTiO3'):.3f} kg ; Fe = {kg('Fe'):.3f} kg ; TiO2 = {kg('TiO2'):.3f} kg ; H2 = {kg('H2'):.4f} kg ; agua = {kg('H2O'):.3f} kg")
    masa_in = kg("FeTiO3") + kg("H2")
    masa_out = kg("Fe") + kg("TiO2") + kg("H2O")
    print(f"Cierre de masa: entra {masa_in:.6f} kg ; sale {masa_out:.6f} kg ; diferencia {masa_in-masa_out:.1e}")
    assert abs(masa_in - masa_out) < 1e-12 * masa_in
    f_ilm = 0.10
    reg = kg("FeTiO3") / f_ilm
    colas = reg - kg("FeTiO3")
    print(f"Con {100*f_ilm:.0f} % de ilmenita en el regolito (sintetico): regolito procesado = {reg:.1f} kg ; colas (sin ilmenita) = {colas:.1f} kg por kg de O")
    # Subproductos por kg de producto: razon subproducto/producto
    print(f"Razon masica metal + oxido / oxigeno = {(kg('Fe')+kg('TiO2')):.3f} kg por kg de O ; colas/O = {colas:.1f}")
    # Agua del lazo: se electroliza -> H2 se recicla; O2 como producto
    n_h2o = n_reac
    o2_prod = n_h2o / 2 * mm("O2") / 1000.0
    print(f"Electrolisis del agua: O2 = {o2_prod:.4f} kg (1 kg de O del agua) ; H2 reciclable = {n_h2o*mm('H2')/1000:.4f} kg")
    assert abs(o2_prod - (n_reac * m_o / 1000.0)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
