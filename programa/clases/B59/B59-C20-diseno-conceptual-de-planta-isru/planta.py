"""B59-C20 · Diseño conceptual de una planta ISRU de agua lunar: dimensionado de extremo a extremo.

Integra, con los mismos supuestos, los modelos de C02, C06, C07, C10, C21 y C19.
OBSERVADO (consultado 2026-11-09): abundancia de hielo 5,6 ± 2,9 % en masa en un sitio (Colaprete et al. 2010, resumen).
Constantes citadas: F y entalpía del vapor (NIST); masas molares NIST. TODO LO DEMÁS ES ILUSTRATIVO (no consultado):
objetivo de 10 000 kg/año de agua procesada, recuperación de hielo 0,90, energía de extracción de C06
(6,030 MJ por kg de agua con x = 5,6 %, eficiencia de captura 0,5, dividida por la recuperación), purificación 0,339 MJ/kg, electrólisis a 0,5 A/cm2 de C10
(32,02 kWh/kg H2 con eficiencia farádica 0,95), enfriamiento de dos tanques (182 W cada uno), excavación 0,05 kWh
por kg de regolito, disponibilidad 0,85, masa específica de la potencia 30 kg/kW, masas de equipos ilustrativas.
Balance: agua -> H2 + O2 (estequiométrico). Cierre de masa y de energía; sensibilidades por barrido.
Unidades: kg, kWh, kW, año de 8 760 h. Sin operación nocturna lunar, sin degradación, sin transporte.
Tolerancias: cierre de masa < 1e-12; energías en kWh consistentes con las clases citadas.
"""
import platform

M_H2, M_O, M_H2O = 2 * 1.007975, 15.9994, 2 * 1.007975 + 15.9994
X = 0.056
REC = 0.90
AGUA_ANO = 10000.0                 # kg/año de agua producida
ETA_CAPT = 0.5                     # eficiencia de captura de calor (C06)


def e_ext_kwh_kg(x, rec):
    """kWh de electricidad por kg de agua recuperada (modelo de C06: regolito 100->350 K, hielo 100->250 K, L = 2,83 MJ/kg)."""
    q = (1 - x) / x * (150.0 * 250.0 + 1.25 * (350.0 ** 2 - 100.0 ** 2)) + 3.75 * (250.0 ** 2 - 100.0 ** 2) + 2.83e6
    return q / 3.6e6 / ETA_CAPT / rec

E_PUR = 0.339 / 3.6                # kWh/kg
E_ELEC = 32.02                     # kWh/kg H2 (C10, 0,5 A/cm2)
E_EXC = 0.05                       # kWh/kg de regolito, ILUSTRATIVO
P_FRIO = 2 * 0.182                 # kW (dos tanques)
DISP = 0.85
ESP_POT = 30.0                     # kg/kW
HORAS = 8760.0


def diseno(x=X, rec=REC, e_elec=E_ELEC, disp=DISP, agua=AGUA_ANO):
    regolito = agua / (x * rec)                     # kg/año
    h2 = agua * M_H2 / M_H2O
    o2 = agua - h2
    e_extr = agua * e_ext_kwh_kg(x, rec)
    e_pur = agua * E_PUR
    e_el = h2 * e_elec
    e_exc = regolito * E_EXC
    e_frio = P_FRIO * HORAS
    e_tot = e_extr + e_pur + e_el + e_exc + e_frio
    p_medio = e_tot / HORAS
    p_dis = p_medio / disp
    m_pot = p_dis * ESP_POT
    m_equipos = 400 + 300 + 100 + 100 + 300     # excavadora, secador, purificador, electrolizador, tanques (ILUSTRATIVO)
    return dict(regolito=regolito, h2=h2, o2=o2, e_extr=e_extr, e_pur=e_pur, e_el=e_el, e_exc=e_exc, e_frio=e_frio,
                e_tot=e_tot, p_medio=p_medio, p_dis=p_dis, m_pot=m_pot, m_equipos=m_equipos, m_tot=m_equipos + m_pot)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    d = diseno()
    print(f"Agua producida = {AGUA_ANO:.0f} kg/año -> H2 = {d['h2']:.1f} kg ; O2 = {d['o2']:.1f} kg ; cierre de masa {AGUA_ANO - d['h2'] - d['o2']:.1e}")
    assert abs(AGUA_ANO - d['h2'] - d['o2']) < 1e-9
    print(f"Regolito a procesar = {d['regolito']/1000:.1f} t/año ({d['regolito']/8760:.1f} kg/h)")
    print("Partida de energia             kWh/año   fraccion")
    for k, n in (("e_extr", "extraccion termica"), ("e_pur", "purificacion"), ("e_el", "electrolisis"), ("e_exc", "excavacion"), ("e_frio", "enfriamiento de tanques")):
        print(f"  {n:26s}  {d[k]:9.0f}  {100*d[k]/d['e_tot']:7.1f} %")
    print(f"Energia total = {d['e_tot']:.0f} kWh/año ; potencia media = {d['p_medio']:.2f} kW ; de diseno (disponibilidad {DISP}) = {d['p_dis']:.2f} kW")
    print(f"Masa: equipos {d['m_equipos']:.0f} kg + potencia {d['m_pot']:.0f} kg = {d['m_tot']:.0f} kg")
    # Cierre de energia: suma de partidas = total
    s = d['e_extr'] + d['e_pur'] + d['e_el'] + d['e_exc'] + d['e_frio']
    assert abs(s - d['e_tot']) < 1e-9 * s
    kwh_por_kg = d['e_tot'] / AGUA_ANO
    print(f"Energia especifica = {kwh_por_kg:.2f} kWh por kg de agua producida")
    # Amortizacion (a la manera de C19) con G igual para planta y producto
    t_dias = d['m_tot'] / (AGUA_ANO / 365.25)     # la produccion anual ya incluye las paradas
    print(f"Amortizacion de la masa de la planta en masa de producto (misma G para planta y producto): {t_dias:.0f} dias")
    # Sensibilidades
    base = d['m_tot']
    print("Sensibilidades (masa total de la planta):")
    for nombre, kw in (("abundancia 2,7 %", dict(x=0.027)), ("abundancia 8,5 %", dict(x=0.085)), ("recuperacion 0,70", dict(rec=0.70)),
                       ("electrolisis 39,94 kWh/kg", dict(e_elec=39.94)), ("disponibilidad 0,70", dict(disp=0.70)), ("produccion x2", dict(agua=2 * AGUA_ANO))):
        r = diseno(**kw)
        print(f"  {nombre:26s}: regolito {r['regolito']/1000:7.1f} t/año ; potencia diseno {r['p_dis']:6.2f} kW ; masa {r['m_tot']:7.0f} kg ({100*(r['m_tot']/base-1):+6.1f} %)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
