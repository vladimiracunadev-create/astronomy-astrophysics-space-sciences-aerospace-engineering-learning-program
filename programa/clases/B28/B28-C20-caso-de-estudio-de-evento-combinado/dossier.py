#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C20: dossier de un evento combinado (GW170817 / GRB 170817A) con coherencia entre mensajeros.

Datos: G, c (NIST CODATA 2022), GM_sol (IAU 2015 B3), 1 au (IERS TN36), consultados 2026-11-09. Cifras del evento tomadas de resumenes
consultados el 2026-11-09:
  - arXiv:1710.05833 (observaciones multimensajero): fusion a las 12:41:04 UTC del 2017-08-17; destello gamma ~1.7 s despues;
    31 grados cuadrados; 40 (+8, -8) Mpc; masas de componentes entre 0.86 y 2.26 Msol.
  - arXiv:1710.05446 (Fermi-GBM): disparo del destello a las 12:41:06 UTC; ~1.7 s despues del disparo de LIGO.
  - arXiv:1710.05834: retardo 1.74 +/- 0.05 s; probabilidad fortuita 5e-8.
  - arXiv:1710.05832: masa total 2.74 Msol (a la distancia de 40 Mpc).
Las masas iguales de 1.37 Msol (para calcular magnitudes derivadas) son ILUSTRATIVAS; otras cifras del evento (corrimiento al rojo,
magnitudes de la kilonova, constante de Hubble) NO se consultaron y no se usan.
Modelo: coherencia aritmetica del dossier y magnitudes derivadas con las formulas de las clases anteriores (retardo de viaje, cota de
velocidad, masa de chirrido, frecuencia ISCO, amplitud, sigmas, fraccion del cielo). La huella SHA-256 sigue la convencion de B28-C17.
Supuestos: orden de cuadrupolo; masas iguales para las magnitudes derivadas. Validez: ilustrativa.
Tolerancia: diferencia entre los tiempos publicados (2 s) y el retardo citado (1.74 s) menor que 1 s; masa total dentro del rango de componentes.
"""
from __future__ import annotations
import hashlib
import json
import math
import platform
import sys
from datetime import datetime, timezone

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
AU = 1.49597870700e11
MPC = 1e6 * 648000 / math.pi * AU


def sigma_de_p(p):
    lo, hi = 0.0, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if 0.5 * math.erfc(mid / math.sqrt(2)) > p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    t_gw = datetime(2017, 8, 17, 12, 41, 4, tzinfo=timezone.utc)
    t_grb = datetime(2017, 8, 17, 12, 41, 6, tzinfo=timezone.utc)
    dt_ts = (t_grb - t_gw).total_seconds()
    dt_cit = 1.74
    assert abs(dt_ts - dt_cit) < 1.0, "marcas de tiempo frente al retardo citado"
    print(f"marcas de tiempo (resolucion de 1 s): GW {t_gw:%H:%M:%S}, GRB {t_grb:%H:%M:%S} -> {dt_ts:.0f} s ; retardo citado = {dt_cit} +/- 0.05 s ; diferencia = {abs(dt_ts - dt_cit):.2f} s")
    m_tot, m_min, m_max = 2.74, 0.86, 2.26
    assert 2 * m_min < m_tot < 2 * m_max, "masa total dentro del rango de componentes"
    m = m_tot / 2 * M_SOL
    mc = (m * m) ** 0.6 / (2 * m) ** 0.2
    d = 40 * MPC
    t_viaje = d / C
    cota = dt_cit / t_viaje
    f_isco = C ** 3 / (6 ** 1.5 * math.pi * G * (2 * m))
    h100 = 4 * (G * mc) ** (5 / 3) * (math.pi * 100.0) ** (2 / 3) / (C ** 4 * d)
    t30 = 5 / 256 * (math.pi * 30.0) ** (-8 / 3) * (G * mc / C ** 3) ** (-5 / 3)
    fcielo = 31.0 / (4 * math.pi * (180 / math.pi) ** 2)
    sig = sigma_de_p(5e-8)
    filas = [
        ("tiempo de la fusion (UTC)", "2017-08-17T12:41:04Z", "S1"),
        ("destello gamma tras la fusion", "~1.7 s ; 1.74 +/- 0.05 s", "S1, S3"),
        ("localizacion inicial", "31 grados cuadrados (7.5e-4 del cielo)", "S1"),
        ("distancia", "40 (+8, -8) Mpc", "S1"),
        ("masa total", "2.74 Msol ; componentes 0.86-2.26 Msol", "S1, S4"),
        ("probabilidad fortuita", f"5e-8 ({sig:.3f} sigma, una cola)", "S3"),
        ("tiempo de viaje de la luz (derivado)", f"{t_viaje:.4e} s = {t_viaje / (365.25 * 86400) / 1e6:.1f} Ma", "calculo"),
        ("cota |v_g - c|/c (derivada)", f"{cota:.2e}", "calculo"),
        ("masa de chirrido, masas iguales (derivada, ilustrativa)", f"{mc / M_SOL:.4f} Msol", "calculo"),
        ("frecuencia ISCO (derivada, ilustrativa)", f"{f_isco:.1f} Hz", "calculo"),
        ("deformacion a 100 Hz (derivada, ilustrativa)", f"{h100:.3e}", "calculo"),
        ("tiempo restante desde 30 Hz (derivado, ilustrativo)", f"{t30:.1f} s", "calculo"),
    ]
    ancho = max(len(f[0]) for f in filas)
    print(f"{'magnitud':<{ancho}}  {'valor':<48}  fuente")
    for a, b, c in filas:
        print(f"{a:<{ancho}}  {b:<48}  {c}")
    assert abs(sig - 5.327) < 1e-3
    assert abs(t_viaje - 4.1171e15) / 4.1171e15 < 1e-4
    dossier = {"evento": "GW170817/GRB170817A", "filas": filas, "no_consultado": ["corrimiento al rojo", "curva de luz de la kilonova", "constante de Hubble"]}
    s = json.dumps(dossier, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    h = hashlib.sha256(s.encode("utf-8")).hexdigest()
    h2 = hashlib.sha256(json.dumps(json.loads(s), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()
    assert h == h2, "huella estable"
    print(f"huella SHA-256 del dossier: {h[:16]}... ; cifras no consultadas y excluidas: {', '.join(dossier['no_consultado'])}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
