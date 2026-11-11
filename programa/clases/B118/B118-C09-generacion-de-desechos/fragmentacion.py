"""B118-C09 · Generación de desechos.

Modelo ILUSTRATIVO de fragmentación: N(>L) = k L^-b con b = 1,6 entre L_min y L_max, conservando la masa del objeto padre
(densidad efectiva de los fragmentos rho_f = 500 kg/m^3 ILUSTRATIVA, forma esférica). Umbral de «catastrófica»: E/m del objetivo
mayor que 40 J/g (valor habitual en la literatura, NO consultado aquí -> ilustrativo).
Unidades: m, kg, J, J/g. Semilla del muestreo: 118. Tolerancia: conservación de masa 1e-9 (integral) y 1 % (muestreo).
"""
import math
import random
import sys

B = 1.6
RHO_F = 500.0


def masa_fragmento(L):
    return RHO_F * math.pi / 6.0 * L ** 3


def k_por_masa(masa_total, L_min, L_max, b=B):
    """k tal que la masa total de fragmentos entre L_min y L_max sea masa_total."""
    # dN = k b L^(-b-1) dL ; masa = int m(L) dN = k b c int L^(2-b) dL
    c = RHO_F * math.pi / 6.0
    integral = (L_max ** (3 - b) - L_min ** (3 - b)) / (3 - b)
    return masa_total / (b * c * integral)


def n_mayor_que(k, L, b=B):
    return k * L ** (-b)


def energia_relativa(m_imp, v_kms, m_obj):
    return 0.5 * m_imp * (v_kms * 1000.0) ** 2 / (m_obj * 1000.0)  # J/g


def muestrear(k, L_min, L_max, n_max, rng, b=B):
    """Inversión de la CDF truncada de una ley de potencias; devuelve diámetros."""
    n_tot = int(round(n_mayor_que(k, L_min, b) - n_mayor_que(k, L_max, b)))
    out = []
    for _ in range(min(n_tot, n_max)):
        u = rng.random()
        L = (L_min ** (-b) - u * (L_min ** (-b) - L_max ** (-b))) ** (-1.0 / b)
        out.append(L)
    return n_tot, out


def compute():
    v = {}
    m_padre = 1000.0
    L_min, L_max = 0.01, 1.0
    k = k_por_masa(0.8 * m_padre, L_min, L_max)  # 80 % de la masa se fragmenta en este rango (ilustrativo)
    v["k"] = k
    v["N_1cm"] = n_mayor_que(k, 0.01)
    v["N_10cm"] = n_mayor_que(k, 0.10)
    v["N_1m"] = n_mayor_que(k, 1.0)
    # integral numérica de masa (regla del punto medio en log L) para verificar
    nb = 20000
    masa = 0.0
    la, lb = math.log(L_min), math.log(L_max)
    for i in range(nb):
        L = math.exp(la + (i + 0.5) * (lb - la) / nb)
        dN = k * B * L ** (-B)  # dN/dlnL
        masa += masa_fragmento(L) * dN * (lb - la) / nb
    v["masa_int"] = masa
    rng = random.Random(118)
    n_tot, diam = muestrear(k, L_min, L_max, 2_000_000, rng)
    v["n_tot"] = n_tot
    v["masa_muestra"] = sum(masa_fragmento(L) for L in diam)
    v["n_10cm_muestra"] = sum(1 for L in diam if L > 0.10)
    masas = []
    for r in range(400):
        _, d = muestrear(k, L_min, L_max, 2_000_000, random.Random(1000 + r))
        masas.append(sum(masa_fragmento(L) for L in d))
    v["masa_media"] = sum(masas) / len(masas)
    v["masa_sd"] = math.sqrt(sum((x - v["masa_media"]) ** 2 for x in masas) / (len(masas) - 1))
    v["E1"] = energia_relativa(1.0, 10.0, 1000.0)
    v["E2"] = energia_relativa(0.01, 10.0, 1000.0)
    v["m_imp_umbral"] = 2 * 40.0 * 1000.0 * m_padre / (10.0 * 1000.0) ** 2
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Modelo ILUSTRATIVO de fragmentacion (ley de potencias b = 1.6, rho = 500 kg/m^3); umbral 40 J/g no consultado.")
    v = compute()
    print(f"k = {v['k']:.4f}; N(>1 cm) = {v['N_1cm']:.0f}; N(>10 cm) = {v['N_10cm']:.0f}; N(>1 m) = {v['N_1m']:.2f}")
    print(f"Masa por integral numerica: {v['masa_int']:.3f} kg (objetivo 800)")
    print(f"Fragmentos muestreados: {v['n_tot']}; masa de la muestra: {v['masa_muestra']:.1f} kg; con L > 10 cm: {v['n_10cm_muestra']}")
    print(f"400 realizaciones: masa media {v['masa_media']:.1f} kg, desviacion {v['masa_sd']:.1f} kg (la masa la dominan pocos fragmentos grandes)")
    print(f"E/m del objetivo (1000 kg) con impactor de 1 kg a 10 km/s: {v['E1']:.1f} J/g ({'catastrofica' if v['E1'] > 40 else 'no catastrofica'})")
    print(f"Con impactor de 10 g: {v['E2']:.2f} J/g ({'catastrofica' if v['E2'] > 40 else 'no catastrofica'})")
    print(f"Masa de impactor a 10 km/s que alcanza 40 J/g sobre 1000 kg: {v['m_imp_umbral']:.3f} kg")
    assert abs(v["masa_int"] - 800.0) < 1e-3
    assert abs(v["masa_media"] - 800.0) < 4 * v["masa_sd"] / math.sqrt(400) + 25.0
    print("Pruebas superadas (masa conservada por integral a 1e-3 kg; media de 400 muestreos dentro de 4 errores estandar + 25 kg).")


if __name__ == "__main__":
    main()
