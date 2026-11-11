#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B120-C01: linea de tiempo regulatoria de una red satelital SINTETICA.

CONTENIDO EDUCATIVO: no es asesoria legal ni regulatoria. Plazos tomados de «ITU Radio Regulatory Framework for Space Services»
(UIT, PDF con fecha de creacion 2018-01-10, refleja el Reglamento de Radiocomunicaciones hasta la CMR-15; consultado 2026-11-11):
 - publicacion anticipada (API): no antes de 7 anios y preferentemente no despues de 2 anios antes de la puesta en servicio (BIU);
 - la coordinacion puede iniciarse no antes de 6 meses despues de recibida la API; si no se recibe la solicitud de coordinacion en 24 meses
   desde la API, la API se cancela (No. 9.5D);
 - la notificacion no debe llegar a la Oficina antes de 3 anios previos a la BIU;
 - la BIU notificada no puede ser posterior a 7 anios desde la recepcion de la API (No. 11.44);
 - satelite GSO en servicio: desplegado y mantenido 90 dias continuos en la posicion notificada, e informar en 30 dias (No. 11.44B).
No se consulto el texto vigente del Reglamento (ediciones posteriores a la CMR-15 pueden diferir).
Los CASOS (fechas, redes) son SINTETICOS, no corresponden a ninguna red real. Calendario gregoriano, fechas en AAAA-MM-DD, sin zona horaria.
Tolerancia: las dos aritmeticas de fechas deben coincidir exactamente (0 dias de diferencia).
"""
from __future__ import annotations
import calendar, platform
from datetime import date, timedelta


def add_months(d: date, n: int) -> date:
    """Via A: suma n meses recortando el dia al ultimo del mes."""
    m = d.year * 12 + (d.month - 1) + n
    y, mo = divmod(m, 12)
    return date(y, mo + 1, min(d.day, calendar.monthrange(y, mo + 1)[1]))


def meses_hasta(a: date, b: date) -> int:
    """Via B: meses enteros completos de a a b (independiente de add_months)."""
    n = (b.year - a.year) * 12 + (b.month - a.month)
    return n - 1 if b.day < a.day and not (b.day == calendar.monthrange(b.year, b.month)[1] and a.day > b.day) else n


def evaluar(c: dict) -> list[str]:
    """Devuelve la lista de plazos incumplidos (via A, con add_months)."""
    api, cr, noti, biu = c["api"], c["cr"], c["notif"], c["biu"]
    v = []
    if cr is not None and cr < add_months(api, 6):
        v.append("coordinacion antes de 6 meses desde la API")
    if cr is None or cr > add_months(api, 24):
        v.append("sin solicitud de coordinacion en 24 meses: API cancelada")
    if noti < add_months(biu, -36):
        v.append("notificacion antes de 3 anios de la BIU")
    if biu > add_months(api, 84):
        v.append("BIU mas de 7 anios despues de la API")
    if c["dias_en_posicion"] < 90:
        v.append("menos de 90 dias continuos en la posicion")
    if c["informe"] > c["biu"] + timedelta(days=c["dias_en_posicion"] + 30):
        v.append("informe a la Oficina despues de 30 dias del fin del periodo")
    return v


def evaluar_b(c: dict) -> list[str]:
    """Via B: mismas reglas con meses enteros (sin add_months). Para la verificacion cruzada."""
    api, cr, noti, biu = c["api"], c["cr"], c["notif"], c["biu"]
    v = []
    if cr is not None and meses_hasta(api, cr) < 6:
        v.append("coordinacion antes de 6 meses desde la API")
    if cr is None or meses_hasta(api, cr) > 24 or (meses_hasta(api, cr) == 24 and cr > add_months(api, 24)):
        v.append("sin solicitud de coordinacion en 24 meses: API cancelada")
    if meses_hasta(noti, biu) > 36 or (meses_hasta(noti, biu) == 36 and noti < add_months(biu, -36)):
        v.append("notificacion antes de 3 anios de la BIU")
    if meses_hasta(api, biu) > 84 or (meses_hasta(api, biu) == 84 and biu > add_months(api, 84)):
        v.append("BIU mas de 7 anios despues de la API")
    if c["dias_en_posicion"] < 90:
        v.append("menos de 90 dias continuos en la posicion")
    if (c["informe"] - c["biu"]).days > c["dias_en_posicion"] + 30:
        v.append("informe a la Oficina despues de 30 dias del fin del periodo")
    return v


D = date
CASOS = {
    "A conforme": dict(api=D(2027, 3, 1), cr=D(2027, 11, 15), notif=D(2031, 1, 10), biu=D(2032, 6, 1), dias_en_posicion=95, informe=D(2032, 6, 1) + timedelta(days=100)),
    "B coordinacion temprana": dict(api=D(2027, 3, 1), cr=D(2027, 6, 1), notif=D(2031, 1, 10), biu=D(2032, 6, 1), dias_en_posicion=95, informe=D(2032, 6, 1) + timedelta(days=100)),
    "C coordinacion tardia": dict(api=D(2027, 3, 1), cr=D(2029, 7, 1), notif=D(2031, 1, 10), biu=D(2032, 6, 1), dias_en_posicion=95, informe=D(2032, 6, 1) + timedelta(days=100)),
    "D BIU fuera de 7 anios": dict(api=D(2027, 3, 1), cr=D(2027, 11, 15), notif=D(2031, 1, 10), biu=D(2034, 3, 2), dias_en_posicion=95, informe=D(2034, 3, 2) + timedelta(days=100)),
    "E notificacion temprana": dict(api=D(2027, 3, 1), cr=D(2027, 11, 15), notif=D(2028, 6, 1), biu=D(2032, 6, 1), dias_en_posicion=95, informe=D(2032, 6, 1) + timedelta(days=100)),
    "F 80 dias y informe tardio": dict(api=D(2027, 3, 1), cr=D(2027, 11, 15), notif=D(2031, 1, 10), biu=D(2032, 6, 1), dias_en_posicion=80, informe=D(2032, 6, 1) + timedelta(days=130)),
    "G limite exacto 7 anios": dict(api=D(2027, 3, 1), cr=D(2027, 11, 15), notif=D(2031, 3, 1), biu=D(2034, 3, 1), dias_en_posicion=90, informe=D(2034, 3, 1) + timedelta(days=120)),
}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("REDES SINTETICAS; plazos del documento UIT 2018-01-10 (Reglamento hasta CMR-15), consultado 2026-11-11. No es asesoria.")
    api = D(2027, 3, 1)
    print("Fechas limite para API recibida 2027-03-01:")
    print(f"  coordinacion no antes de {add_months(api, 6)}; API cancelada si no hay solicitud al {add_months(api, 24)}; BIU limite {add_months(api, 84)}")
    print("Caso                          incumplimientos")
    discrepancias = 0
    for nombre, c in CASOS.items():
        va, vb = evaluar(c), evaluar_b(c)
        if sorted(va) != sorted(vb):
            discrepancias += 1
        print(f"{nombre:28s}  {len(va)}  {'; '.join(va) if va else 'ninguno'}")
    print(f"Discrepancias entre las dos aritmeticas de fechas: {discrepancias}")
    assert evaluar(CASOS["A conforme"]) == []
    assert len(evaluar(CASOS["G limite exacto 7 anios"])) == 0
    assert add_months(D(2027, 1, 31), 1) == D(2027, 2, 28)
    assert discrepancias == 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
