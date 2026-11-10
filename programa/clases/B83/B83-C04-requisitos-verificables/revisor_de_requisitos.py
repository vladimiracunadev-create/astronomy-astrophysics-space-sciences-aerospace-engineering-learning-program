#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C04: revisor automatico de calidad de requisitos (reglas verificables).

Datos: doce requisitos SINTETICOS de la mision de ejemplo ESTRELLA-S, algunos con defectos plantados a proposito.
Reglas (de ejemplo, no de una norma): (R1) modal «deberá» unico; (R2) sin palabras ambiguas; (R3) atomico (una sola obligacion);
(R4) valor medible con unidad o referencia a un estandar; (R5) metodo de verificacion A/I/D/T asignado.
Segunda via: un oraculo escrito a mano con los defectos plantados; el revisor debe encontrar exactamente esos.
Sin constantes fisicas ni sistema de referencia.
"""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

REQ = {
    "R01": ("El sistema deberá obtener imágenes con un GSD no mayor de 5 m desde 550 km de altura.", "T"),
    "R02": ("El sistema deberá tener una resolución adecuada.", ""),
    "R03": ("La masa de lanzamiento deberá ser menor o igual que 120 kg.", "A"),
    "R04": ("El sistema deberá ser fácil de operar y deberá usar baja potencia.", "D"),
    "R05": ("La carga útil deberá bajar 2 Gbit por día.", "A"),
    "R06": ("El enlace descendente deberá ser rápido.", "T"),
    "R07": ("El satélite deberá funcionar 3 años en órbita.", "A"),
    "R08": ("La potencia media consumida no deberá superar 40 W.", "T"),
    "R09": ("El sistema podrá almacenar datos aproximadamente 8 Gbit.", "I"),
    "R10": ("La telemetría deberá transmitirse según CCSDS 131.0-B-5.", "I"),
    "R11": ("El software deberá ser robusto, etc.", ""),
    "R12": ("El sistema deberá comandarse desde la estación en cada pase.", "D"),
}
AMBIGUAS = ["adecuad", "fácil", "rápid", "robust", "aproximadamente", "etc.", "baja ", "suficiente", "óptim"]
UNIDADES = r"(m|km|kg|W|Gbit|Mbit/s|años|min|h|d|V|°)"
# Oraculo manual: reglas que cada requisito DEBE incumplir (defectos plantados)
ORACULO = {"R02": {"R2", "R4", "R5"}, "R04": {"R2", "R3", "R4"}, "R06": {"R2", "R4"}, "R09": {"R1", "R2"},
           "R11": {"R2", "R4", "R5"}, "R12": {"R4"}}


def revisar(texto, metodo):
    f = set()
    n_deb = len(re.findall(r"\bdeberá\b", texto))
    if n_deb == 0: f.add("R1")
    if n_deb > 1: f.add("R3")
    if any(p in texto for p in AMBIGUAS): f.add("R2")
    if not (re.search(r"\d+(,\d+)?\s*" + UNIDADES + r"\b", texto) or re.search(r"CCSDS|ECSS|ISO", texto)): f.add("R4")
    if metodo not in {"A", "I", "D", "T"}: f.add("R5")
    return f


def calcular():
    res = {k: revisar(t, m) for k, (t, m) in REQ.items()}
    por_regla = {r: sum(1 for v in res.values() if r in v) for r in ["R1", "R2", "R3", "R4", "R5"]}
    ok = [k for k, v in res.items() if not v]
    V = dict(res=res, n=len(REQ), n_ok=len(ok), pct_ok=100.0 * len(ok) / len(REQ), ok=ok,
             f1=por_regla["R1"], f2=por_regla["R2"], f3=por_regla["R3"], f4=por_regla["R4"], f5=por_regla["R5"],
             n_defectos=sum(len(v) for v in res.values()))
    V["coincide"] = all(res[k] == ORACULO.get(k, set()) for k in REQ)
    return V


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 12 requisitos de ESTRELLA-S con defectos plantados; reglas R1-R5 de ejemplo")
    for k, (t, m) in REQ.items():
        d = ",".join(sorted(V["res"][k])) or "-"
        print(f"  {k} [{m or ' '}] defectos: {d:10s} {t}")
    print(f"Requisitos sin defectos: {V['n_ok']} de {V['n']} ({V['pct_ok']:.1f} %) -> {', '.join(V['ok'])}")
    print(f"Incumplimientos por regla: R1 {V['f1']}, R2 {V['f2']}, R3 {V['f3']}, R4 {V['f4']}, R5 {V['f5']} ; defectos totales {V['n_defectos']}")
    comprobar(V["coincide"], "el revisor coincide con el oraculo de defectos plantados")
    comprobar(V["n_ok"] + sum(1 for v in V["res"].values() if v) == V["n"], "cuentas consistentes")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
