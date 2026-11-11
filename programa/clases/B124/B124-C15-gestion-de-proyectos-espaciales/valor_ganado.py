#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C15: estructura de desglose del trabajo (WBS) y valor ganado (EVM) de un proyecto SINTETICO.

CONTENIDO EDUCATIVO: no es asesoria de gestion ni financiera. Presupuestos, avances y costos reales son SINTETICOS.
Consultado (2026-11-11): NASA Systems Engineering Handbook (SP-6105 Rev 2): fases del ciclo de vida de Pre-Fase A a Fase F y el uso de una estructura de desglose
del trabajo (WBS) para definir y comunicar que hay que hacer; ninguna cifra de este laboratorio viene de el.
Definiciones: PV = BAC x % planificado; EV = BAC x % logrado; AC = costo real. CV = EV - AC ; SV = EV - PV ; CPI = EV/AC ; SPI = EV/PV.
EAC = BAC/CPI (supone que el rendimiento de costo se mantiene); ETC = EAC - AC ; VAC = BAC - EAC ; TCPI = (BAC - EV)/(BAC - AC).
Verificacion: (1) la suma de los paquetes de trabajo coincide con la de los elementos de nivel 2 y con el proyecto (regla del 100 %);
(2) EAC = AC + (BAC - EV)/CPI (identidad algebraica); (3) tendencia mensual del CPI acumulado.
Unidades: Mum (millones de unidades monetarias sinteticas). Tolerancias: sumas e identidad < 1e-9.
"""
import platform

# (id, nombre, elemento de nivel 2, BAC, % planificado, % logrado, AC)
PAQ = [
    ("1.1.1", "estructura", "1.1 plataforma", 12.0, 1.00, 1.00, 13.0),
    ("1.1.2", "potencia", "1.1 plataforma", 10.0, 1.00, 0.90, 11.0),
    ("1.2.1", "instrumento", "1.2 carga util", 25.0, 0.80, 0.60, 20.0),
    ("1.2.2", "calibracion", "1.2 carga util", 8.0, 0.50, 0.40, 4.0),
    ("1.3.1", "software de tierra", "1.3 segmento terrestre", 15.0, 0.60, 0.50, 9.0),
    ("1.3.2", "operaciones", "1.3 segmento terrestre", 10.0, 0.20, 0.10, 3.0),
]
MENSUAL = {"PV": [5, 12, 22, 35, 47, 57.0], "EV": [4, 10, 18, 29, 39, 47.7], "AC": [5, 12, 23, 38, 50, 60.0]}


def metricas(bac, pv, ev, ac):
    cpi, spi = ev / ac, ev / pv
    eac = bac / cpi
    return dict(bac=bac, pv=pv, ev=ev, ac=ac, cv=ev - ac, sv=ev - pv, cpi=cpi, spi=spi, eac=eac, etc=eac - ac, vac=bac - eac, tcpi=(bac - ev) / (bac - ac))


def run():
    filas = [(p[0], p[1], p[2], p[3], p[3] * p[4], p[3] * p[5], p[6]) for p in PAQ]
    total = metricas(sum(f[3] for f in filas), sum(f[4] for f in filas), sum(f[5] for f in filas), sum(f[6] for f in filas))
    n2 = {}
    for f in filas:
        a = n2.setdefault(f[2], [0.0, 0.0, 0.0, 0.0])
        for i in range(4):
            a[i] += f[3 + i]
    suma_n2 = [sum(v[i] for v in n2.values()) for i in range(4)]
    dif_roll = max(abs(suma_n2[0] - total["bac"]), abs(suma_n2[1] - total["pv"]), abs(suma_n2[2] - total["ev"]), abs(suma_n2[3] - total["ac"]))
    ident = abs(total["eac"] - (total["ac"] + (total["bac"] - total["ev"]) / total["cpi"]))
    eac_b = total["ac"] + (total["bac"] - total["ev"])
    eac_c = total["ac"] + (total["bac"] - total["ev"]) / (total["cpi"] * total["spi"])
    cpi_mes = [MENSUAL["EV"][i] / MENSUAL["AC"][i] for i in range(6)]
    spi_mes = [MENSUAL["EV"][i] / MENSUAL["PV"][i] for i in range(6)]
    elem = {k: metricas(v[0], v[1], v[2], v[3]) for k, v in n2.items()}
    peor = min(filas, key=lambda f: f[5] / f[6])
    R = {"bac": total["bac"], "pv": total["pv"], "ev": total["ev"], "ac": total["ac"], "cv": total["cv"], "sv": total["sv"], "cpi": total["cpi"], "spi": total["spi"],
         "eac": total["eac"], "etc": total["etc"], "vac": total["vac"], "tcpi": total["tcpi"], "dif_roll": dif_roll, "ident": ident, "eac_b": eac_b, "eac_c": eac_c,
         "cpi_min": min(cpi_mes), "cpi_m1": cpi_mes[0], "cpi_m6": cpi_mes[-1], "spi_m6": spi_mes[-1], "peor_cpi": peor[5] / peor[6], "peor_nombre": peor[1], "filas": filas, "elem": elem,
         "cpi_mes": cpi_mes, "cpi_plat": elem["1.1 plataforma"]["cpi"], "cpi_carga": elem["1.2 carga util"]["cpi"], "cpi_tierra": elem["1.3 segmento terrestre"]["cpi"],
         "pct_gastado": total["ac"] / total["bac"], "pct_logrado": total["ev"] / total["bac"]}
    return R


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Proyecto SINTETICO (Mum); WBS de 3 elementos y 6 paquetes de trabajo")
    print(" paquete  nombre               BAC     PV      EV      AC     CPI    SPI")
    for f in R["filas"]:
        print(f" {f[0]}   {f[1]:<18} {f[3]:6.2f} {f[4]:7.2f} {f[5]:7.2f} {f[6]:7.2f} {f[5] / f[6]:6.3f} {f[5] / f[4]:6.3f}")
    print(f"Proyecto: BAC = {R['bac']:.1f} ; PV = {R['pv']:.2f} ; EV = {R['ev']:.2f} ; AC = {R['ac']:.2f} ; CV = {R['cv']:.2f} ; SV = {R['sv']:.2f}")
    print(f"  CPI = {R['cpi']:.4f} ; SPI = {R['spi']:.4f} ; EAC = BAC/CPI = {R['eac']:.2f} ; ETC = {R['etc']:.2f} ; VAC = {R['vac']:.2f} ; TCPI = {R['tcpi']:.4f}")
    print(f"  otras EAC: AC + (BAC - EV) = {R['eac_b']:.2f} ; AC + (BAC - EV)/(CPI SPI) = {R['eac_c']:.2f}")
    for k, m in R["elem"].items():
        print(f"  elemento {k:<24} CPI = {m['cpi']:.3f} ; SPI = {m['spi']:.3f} ; EAC = {m['eac']:.2f}")
    print("  CPI acumulado por mes:", " ".join(f"{x:.3f}" for x in R["cpi_mes"]))
    print(f"Regla del 100 % (paquetes = elementos = proyecto), error = {R['dif_roll']:.1e} ; identidad EAC, error = {R['ident']:.1e}")
    assert R["dif_roll"] < 1e-9 and R["ident"] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
