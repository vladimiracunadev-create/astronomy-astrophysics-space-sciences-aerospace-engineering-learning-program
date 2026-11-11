#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B120-C02: zona de coordinacion de una estacion terrena SINTETICA y plazos de respuesta.

CONTENIDO EDUCATIVO: no es asesoria legal ni regulatoria ni un calculo de coordinacion valido.
CONSULTADO (2026-11-11), documento UIT «ITU Radio Regulatory Framework for Space Services» (PDF creado 2018-01-10; Reglamento hasta CMR-15):
 - coordinacion estacion terrena / estacion terrenal (Nos. 9.15-9.19): la condicion se basa en la zona de coordinacion de la estacion terrena que cubre
   el territorio de otra administracion (Apendice 5); la administracion que recibe la solicitud tiene 30 dias para acusar recibo;
 - ante una solicitud publicada por la Oficina, la administracion afectada tiene 4 meses para dar su acuerdo o su desacuerdo con datos tecnicos
   (Nos. 9.50-9.52); si no responde, se la considera no afectada en los casos de Nos. 9.11-9.14 y 9.21 (No. 9.52C).
NO CONSULTADO: el metodo reglamentario de la zona de coordinacion (Apendice 7), los modos de propagacion, los umbrales del Apendice 5.
ILUSTRATIVO (sintetico): perdida de espacio libre L = 92.45 + 20 log10(f/GHz) + 20 log10(d/km) [dB], PIRE hacia el horizonte 40 dBW,
ganancia del receptor afectado 0 dBi, potencia permisible -110 dBW en la banda de referencia, f = 6 GHz; las estaciones vecinas son inventadas.
Sistema de referencia: esfera de radio 6371 km (valor de uso comun, no consultado); latitud/longitud en grados; fechas AAAA-MM-DD.
Tolerancias: nivel recibido en la distancia de coordinacion = permisible a 1e-9 dB; distancia de gran circulo con dos formulas a 0.01 km.
"""
from __future__ import annotations
import calendar, math, platform
from datetime import date, timedelta

R = 6371.0


def distancia_coordinacion(pire_dbw, g_rx_dbi, p_perm_dbw, f_ghz):
    """Distancia [km] a la que la perdida de espacio libre reduce la senal al nivel permisible."""
    L = pire_dbw + g_rx_dbi - p_perm_dbw
    return 10 ** ((L - 92.45 - 20 * math.log10(f_ghz)) / 20)


def nivel_recibido(pire_dbw, g_rx_dbi, f_ghz, d_km):
    return pire_dbw + g_rx_dbi - (92.45 + 20 * math.log10(f_ghz) + 20 * math.log10(d_km))


def haversine(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dl = math.radians(lon2 - lon1)
    a = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


def coseno_esferico(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    c = math.sin(p1) * math.sin(p2) + math.cos(p1) * math.cos(p2) * math.cos(math.radians(lon2 - lon1))
    return R * math.acos(max(-1.0, min(1.0, c)))


def add_months(d, n):
    m = d.year * 12 + d.month - 1 + n
    y, mo = divmod(m, 12)
    return date(y, mo + 1, min(d.day, calendar.monthrange(y, mo + 1)[1]))


EST = (-33.00, -70.00)  # estacion terrena sintetica
VECINAS = [  # (nombre, administracion sintetica, lat, lon, respuesta: dias tras publicacion o None, tipo)
    ("T1", "ADM-X", -33.50, -69.60, 45, "acuerdo"),
    ("T2", "ADM-X", -34.20, -70.30, 100, "desacuerdo"),
    ("T3", "ADM-Y", -32.60, -69.50, None, "silencio"),
    ("T4", "ADM-Y", -36.50, -72.00, 30, "acuerdo"),
    ("T5", "ADM-Z", -31.00, -64.50, None, "silencio"),
    ("T6", "ADM-Z", -33.45, -70.66, 150, "desacuerdo"),
]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("ZONA DE COORDINACION ILUSTRATIVA (espacio libre); plazos de 30 dias y 4 meses del documento UIT 2018-01-10, consultado 2026-11-11. No es asesoria.")
    f, pire, g, perm = 6.0, 40.0, 0.0, -110.0
    d0 = distancia_coordinacion(pire, g, perm, f)
    print(f"Distancia de coordinacion a {f} GHz: {d0:.1f} km (area = {math.pi * d0 ** 2:.0f} km2)")
    for ff in (3.0, 6.0, 12.0):
        print(f"  f = {ff:4.1f} GHz -> d = {distancia_coordinacion(pire, g, perm, ff):7.1f} km")
    err = abs(nivel_recibido(pire, g, f, d0) - perm)
    print(f"Verificacion inversa |nivel recibido - permisible| = {err:.1e} dB")
    print(f"Razon d(3 GHz)/d(6 GHz) = {distancia_coordinacion(pire, g, perm, 3.0) / d0:.4f} (esperada 2.0000)")
    pub = date(2028, 1, 31)
    limite = add_months(pub, 4)
    print(f"Solicitud publicada {pub}; plazo de 4 meses hasta {limite}; acuse de recibo en 30 dias hasta {pub + timedelta(days=30)}")
    print("Est  Adm    dist[km]  dentro  respuesta      estado")
    dentro_adm = set()
    max_dif = 0.0
    for n, adm, la, lo, dias, tipo in VECINAS:
        d = haversine(EST[0], EST[1], la, lo)
        max_dif = max(max_dif, abs(d - coseno_esferico(EST[0], EST[1], la, lo)))
        dentro = d <= d0
        if dentro:
            dentro_adm.add(adm)
        if not dentro:
            est, resp = "fuera de la zona", "-"
        elif dias is None:
            est, resp = "no afectada por silencio", "ninguna"
        else:
            fecha = pub + timedelta(days=dias)
            resp = str(fecha)
            est = f"{tipo}" + (" (fuera de plazo)" if fecha > limite else "")
        print(f"{n:3s}  {adm:6s} {d:8.1f}  {'si' if dentro else 'no':6s}  {resp:13s}  {est}")
    print(f"Administraciones a coordinar: {sorted(dentro_adm)}")
    print(f"Maxima diferencia haversine - coseno esferico = {max_dif:.1e} km")
    assert err < 1e-9 and abs(distancia_coordinacion(pire, g, perm, 3.0) / d0 - 2.0) < 1e-9
    assert abs(haversine(0, 0, 0, 1) - 2 * math.pi * R / 360) < 0.01
    assert max_dif < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
