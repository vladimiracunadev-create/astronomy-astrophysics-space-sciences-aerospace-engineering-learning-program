#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C19: base de datos de telemetria, calibraciones, limites y criterios de aceptacion y transferencia a operaciones.

Datos: SINTETICOS (seis parametros de telemetria de ESTRELLA-S con calibracion polinomica cuentas -> unidades de ingenieria, limites
amarillo/rojo, ocho comandos con rangos de argumento, tres operadores con horas de entrenamiento). Tres defectos plantados: un parametro sin
calibracion, un parametro con limites invertidos y un identificador duplicado. Modelo: eng = c0 + c1 x + c2 x^2 (Horner); fuera de limites
(OOL) si eng fuera de [lo, hi]. Segunda via: numpy.polyval frente a Horner. Tolerancia: 1e-9. Telemetria sintetica: 2000 muestras por
parametro con ruido gaussiano (semilla 83019). Criterios de aceptacion (reglas del ejemplo): base de datos sin defectos, 100 % de comandos
probados de extremo a extremo, todos los operadores con >= 32 h de entrenamiento. Sin constantes fisicas.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

# id, nombre, unidad, coeficientes (c0, c1, c2) o None, limites (rojo_lo, amarillo_lo, amarillo_hi, rojo_hi), media de cuentas, sigma de cuentas
TM = [(101, "BATT_V", "V", (0.0, 0.002441, 0.0), (6.0, 6.5, 8.4, 8.8), 3300.0, 40.0),
      (102, "BATT_T", "degC", (-40.0, 0.0488, 0.0), (-5.0, 0.0, 35.0, 45.0), 1500.0, 60.0),
      (103, "PANEL_I", "A", (0.0, 0.0012, 0.0), (0.0, 0.0, 9.0, 10.0), 2000.0, 300.0),
      (104, "CPU_T", "degC", (-40.0, 0.0488, 0.0), (-10.0, 0.0, 70.0, 85.0), 2200.0, 120.0),
      (105, "PL_T", "degC", None, (-10.0, 0.0, 40.0, 50.0), 2000.0, 100.0),
      (101, "RW_RPM", "rpm", (-6000.0, 2.9304, 0.0), (6000.0, 5000.0, -5000.0, -6000.0), 2048.0, 400.0)]
CMD = [("SET_MODE", True), ("CAPTURE", True), ("DOWNLINK", True), ("SET_TIME", True), ("RESET_OBC", True), ("SAFE_MODE", True),
       ("DEPLOY_PANEL", False), ("FIRE_THRUSTER", False)]
HORAS = [40.0, 32.0, 24.0]
HORAS_MIN = 32.0


def horner(c, x):
    return c[0] + x * (c[1] + x * c[2])


def revisar_db():
    defectos = []
    ids = [t[0] for t in TM]
    for i in sorted({x for x in ids if ids.count(x) > 1}): defectos.append(f"identificador duplicado {i}")
    for (i, n, u, c, l, m, s) in TM:
        if c is None: defectos.append(f"{n}: sin calibracion")
        if not (l[0] <= l[1] <= l[2] <= l[3]) and not (l[0] >= l[1] >= l[2] >= l[3]) or (l[0] > l[3]):
            defectos.append(f"{n}: limites invertidos o no ordenados")
    return defectos


def calcular():
    defectos = revisar_db()
    rng = np.random.default_rng(83019)
    amarillo = rojo = total = 0
    por_param = {}
    dif = 0.0
    for (i, n, u, c, l, m, s) in TM:
        if c is None or l[0] > l[3]: continue
        x = rng.normal(m, s, 2000)
        e = horner(c, x)
        dif = max(dif, float(np.max(np.abs(e - np.polyval(c[::-1], x)))))
        r = int(((e < l[0]) | (e > l[3])).sum()); a = int((((e < l[1]) | (e > l[2])) & ~((e < l[0]) | (e > l[3]))).sum())
        por_param[n] = (a, r); amarillo += a; rojo += r; total += len(e)
    cmd_ok = sum(1 for _, ok in CMD if ok)
    horas_ok = sum(1 for h in HORAS if h >= HORAS_MIN)
    crit = {"base de datos sin defectos": len(defectos) == 0, "comandos probados de extremo a extremo": cmd_ok == len(CMD),
            "operadores entrenados": horas_ok == len(HORAS)}
    return dict(defectos=defectos, n_def=len(defectos), amarillo=amarillo, rojo=rojo, total=total, por_param=por_param, dif=dif,
                cmd_ok=cmd_ok, n_cmd=len(CMD), cmd_pct=100 * cmd_ok / len(CMD), horas_ok=horas_ok, n_oper=len(HORAS), crit=crit,
                aceptada=all(crit.values()), n_crit_ok=sum(crit.values()), pct_amarillo=100 * amarillo / max(total, 1),
                pct_rojo=100 * rojo / max(total, 1), sin_probar=[n for n, ok in CMD if not ok])


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 6 parametros de telemetria, 8 comandos, 3 operadores; reglas de aceptacion del ejemplo")
    print(f"Defectos de la base de datos: {V['n_def']}")
    for d in V["defectos"]: print("  -", d)
    print(f"Telemetria sintetica evaluada: {V['total']} muestras ; amarillo {V['amarillo']} ({V['pct_amarillo']:.2f} %) ; rojo {V['rojo']} ({V['pct_rojo']:.2f} %)")
    for n, (a, r) in V["por_param"].items(): print(f"  {n:8s} amarillo {a:5d} rojo {r:5d}")
    print(f"Diferencia maxima Horner - numpy.polyval = {V['dif']:.2e}")
    print(f"Comandos probados de extremo a extremo: {V['cmd_ok']} de {V['n_cmd']} ; sin probar: {', '.join(V['sin_probar'])}")
    print(f"Operadores con >= {HORAS_MIN:.0f} h: {V['horas_ok']} de {V['n_oper']}")
    for k, ok in V["crit"].items(): print(f"  Criterio '{k}': {'CUMPLE' if ok else 'NO CUMPLE'}")
    print(f"Aceptacion para transferir a operaciones: {'ACEPTADA' if V['aceptada'] else 'NO ACEPTADA'} ({V['n_crit_ok']} de {len(V['crit'])} criterios)")
    comprobar(V["dif"] < 1e-9, "Horner y polyval coinciden")
    comprobar(V["n_def"] == 3, "los tres defectos plantados se detectan")
    comprobar(not V["aceptada"], "con defectos no se acepta")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
