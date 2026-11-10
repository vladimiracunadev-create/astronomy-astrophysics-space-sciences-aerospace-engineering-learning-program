#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C11: presupuesto de datos (generacion, compresion, codificacion CCSDS y enlace descendente).

Constantes consultadas el 2026-11-10: RE y GM de NASA/NSSDC; CCSDS 131.0-B-5 (septiembre de 2023): codigo LDPC (8160, 7136) de tasa
223/255 con marcador de sincronizacion (ASM) de 32 bits por palabra de codigo (se leyo la seccion 7.3 y 7.2.1.1 con PyMuPDF).
SINTETICOS: camara de barrido de 6000 pixeles, 12 bits, 4 bandas, 40 s de toma por orbita, compresion 3:1, enlace de 100 Mbit/s,
eficiencia de tramas 0.97, 1 min de adquisicion por pase. El tiempo de contacto diario, los pases y el hueco maximo se toman del
laboratorio de B83-C03 (simulacion sintetica de una estacion a 40 N). Sistema: sin sistema de referencia (datos); suelo esferico para la
velocidad en tierra. Segunda via: conteo discreto de palabras de codigo por pase frente a la formula continua; el residuo debe ser
menor que una palabra de codigo por pase. Tolerancias: 1e-6 relativo en las tasas.
"""
import importlib.util
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

PIX, BITS, BANDAS, T_TOMA_S, COMPRESION = 6000, 12, 4, 40.0, 3.0
GSD_M = 5.0
R_ENLACE, EFIC_TRAMA, ADQ_MIN = 100e6, 0.97, 1.0
K_INFO, N_COD, ASM = 7136, 8160, 32            # CCSDS 131.0-B-5, LDPC (8160, 7136) y ASM de 32 bits
ALMACEN_GBIT = 256.0


def contactos():
    ruta = Path(__file__).resolve().parents[1] / "B83-C03-concepto-de-operaciones-conops" / "contactos_conops.py"
    sp = importlib.util.spec_from_file_location("contactos_conops", ruta)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m.calcular()


def calcular():
    c = contactos()
    T = periodo_s(); orbitas_dia = 86400.0 / T
    v_suelo = RE_KM * 2 * math.pi / T * 1000.0                     # m/s
    lineas_s = v_suelo / GSD_M
    tasa_bruta = PIX * lineas_s * BITS * BANDAS                     # bit/s
    bruto_orbita = tasa_bruta * T_TOMA_S
    comp_orbita = bruto_orbita / COMPRESION
    prod_dia = comp_orbita * orbitas_dia
    ef_cod = K_INFO / (N_COD + ASM)                                  # informacion / simbolos de canal
    t_util_s = (c["cont_dia"] - c["pases_dia"] * ADQ_MIN) * 60.0
    cap_dia = t_util_s * R_ENLACE * ef_cod * EFIC_TRAMA
    # segunda via: conteo discreto de palabras de codigo por pase medio
    t_pase = t_util_s / c["pases_dia"]
    palabras = math.floor(t_pase * R_ENLACE / (N_COD + ASM))
    cap_pase_discreto = palabras * K_INFO * EFIC_TRAMA
    cap_pase_cont = t_pase * R_ENLACE * ef_cod * EFIC_TRAMA
    prod_gap = prod_dia / 86400.0 * c["gap_max"] * 3600.0
    almacen_req = prod_gap * 1.3
    r_comp_min = bruto_orbita * orbitas_dia / cap_dia
    return dict(T_min=T / 60, orbitas_dia=orbitas_dia, v_suelo=v_suelo / 1000, lineas_s=lineas_s, tasa_bruta=tasa_bruta / 1e6,
                bruto_orbita=bruto_orbita / 1e9, comp_orbita=comp_orbita / 1e9, prod_dia=prod_dia / 1e9, ef_cod=ef_cod,
                cont_dia=c["cont_dia"], pases_dia=c["pases_dia"], gap_max=c["gap_max"], t_util=t_util_s / 60, cap_dia=cap_dia / 1e9,
                margen=100 * (cap_dia - prod_dia) / prod_dia, razon=cap_dia / prod_dia, cap_pase=cap_pase_cont / 1e9,
                dif_pase=(cap_pase_cont - cap_pase_discreto), palabra_bits=K_INFO * EFIC_TRAMA, prod_gap=prod_gap / 1e9,
                almacen_req=almacen_req / 1e9, almacen_ok=almacen_req / 1e9 <= ALMACEN_GBIT, r_comp_min=r_comp_min,
                ef_total=100 * ef_cod * EFIC_TRAMA, ef_cod_pct=100 * ef_cod, pct_alm=100 * almacen_req / 1e9 / ALMACEN_GBIT)


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 6000 px x 12 bit x 4 bandas, GSD 5 m, 40 s/orbita, compresion 3:1, enlace 100 Mbit/s; CCSDS 131.0-B-5 (LDPC 8160,7136; ASM 32 bit)")
    print(f"Periodo = {V['T_min']:.2f} min ; orbitas por dia = {V['orbitas_dia']:.3f} ; velocidad en tierra = {V['v_suelo']:.3f} km/s ; lineas/s = {V['lineas_s']:.1f}")
    print(f"Tasa bruta del sensor = {V['tasa_bruta']:.2f} Mbit/s ; por orbita = {V['bruto_orbita']:.3f} Gbit bruto, {V['comp_orbita']:.3f} Gbit comprimido")
    print(f"Produccion por dia = {V['prod_dia']:.2f} Gbit")
    print(f"Eficiencia del codigo = 7136/(8160+32) = {V['ef_cod']:.6f} ; eficiencia total con tramas = {V['ef_total']:.3f} %")
    print(f"Contacto (de B83-C03): {V['cont_dia']:.2f} min/dia en {V['pases_dia']:.2f} pases ; util = {V['t_util']:.2f} min/dia ; hueco maximo = {V['gap_max']:.2f} h")
    print(f"Capacidad de bajada = {V['cap_dia']:.2f} Gbit/dia ; margen = {V['margen']:.2f} % ; razon capacidad/produccion = {V['razon']:.3f}")
    print(f"Capacidad por pase medio: formula {V['cap_pase']:.4f} Gbit ; diferencia con conteo discreto = {V['dif_pase']:.1f} bit (< {V['palabra_bits']:.0f} bit)")
    print(f"Registrador: se producen {V['prod_gap']:.2f} Gbit en el hueco maximo ; con margen 1.3 -> {V['almacen_req']:.2f} Gbit de {ALMACEN_GBIT:.0f} ({V['pct_alm']:.1f} %)")
    print(f"Compresion minima para cerrar el balance = {V['r_comp_min']:.3f}:1")
    comprobar(0 <= V["dif_pase"] < V["palabra_bits"] * 1.0001, "residuo discreto menor que una palabra de codigo")
    comprobar(V["razon"] > 1.0, "la capacidad supera a la produccion")
    comprobar(V["almacen_ok"], "el registrador cubre el hueco maximo")
    comprobar(abs(V["ef_cod"] - 7136 / 8192) < 1e-12, "eficiencia del codigo con ASM")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
