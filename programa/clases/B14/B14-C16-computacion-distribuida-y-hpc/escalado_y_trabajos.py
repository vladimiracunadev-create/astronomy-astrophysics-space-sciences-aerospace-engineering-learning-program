#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C16: escalado fuerte y débil con un modelo, y un guion de Slurm.

AVISO: no hay clúster; los números son de un MODELO ANALÍTICO con parámetros
SINTÉTICOS, no mediciones. Sirve para razonar sobre el escalado y verificar
identidades.
Modelo (escalado fuerte, problema fijo de tamaño W): T(p) = W*(s + (1-s)/p)
+ c*log2(p) (c = coste de comunicación por etapa de árbol, sintético).
Aceleración S = T(1)/T(p); eficiencia E = S/p. Escalado débil (trabajo por
proceso constante): T(p) = W*(s + (1-s)) + c*log2(p); eficiencia débil = T(1)/T(p).
Ley de Gustafson (escalado débil ideal sin comunicación): S(p) = s + (1-s)*p.
Parámetros sintéticos: s = 0.02, c = 0.005*W.
Guion de Slurm: se genera como texto con las directivas habituales de sbatch
(--job-name, --nodes, --ntasks, --time, --partition) y se comprueba que cada
directiva está presente; NO se envía a ningún planificador.
Tolerancia: identidades con 1e-12.
"""
from __future__ import annotations
import math, platform, sys


def T_fuerte(p, W=1.0, s=0.02, c=0.005):
    return W * (s + (1 - s) / p) + c * W * math.log2(p)


def T_debil(p, W=1.0, s=0.02, c=0.005):
    return W + c * W * math.log2(p)


def guion_slurm(nombre, nodos, tareas, tiempo, particion, orden):
    return "\n".join([
        "#!/bin/bash",
        f"#SBATCH --job-name={nombre}",
        f"#SBATCH --nodes={nodos}",
        f"#SBATCH --ntasks={tareas}",
        f"#SBATCH --time={tiempo}",
        f"#SBATCH --partition={particion}",
        f"srun {orden}",
    ])


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  (modelo sintético, sin clúster)")
    print("escalado fuerte: p, T(p), S, E")
    mejor_p, mejor_T = 1, T_fuerte(1)
    for p in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
        T = T_fuerte(p)
        S = T_fuerte(1) / T
        print(f"  p={p:5d}: T = {T:.4f}, S = {S:6.2f}, E = {S/p:.3f}")
        if T < mejor_T:
            mejor_p, mejor_T = p, T
    print(f"el tiempo mínimo del modelo está en p = {mejor_p} (más procesos empeoran por la comunicación)")
    prueba(T_fuerte(1) == 1.0, "T(1) = W*(s + 1 - s) = 1 sin comunicación (log2(1)=0)")
    prueba(mejor_p < 1024, "con comunicación, hay un óptimo finito")
    prueba(all(T_fuerte(p) / 1 > 0 for p in (1, 2, 4)), "tiempos positivos")

    s = 0.02
    # sin comunicación, Amdahl: S(p) -> 1/s
    amd = lambda p: 1.0 / (s + (1 - s) / p)
    prueba(abs(amd(10**12) - 1 / s) < 1e-6, "Amdahl tiende a 1/s")
    print(f"Amdahl sin comunicación con s={s}: S(64) = {amd(64):.2f}; límite 1/s = {1/s:.0f}")

    print("escalado débil: p, T(p), eficiencia débil T(1)/T(p), Gustafson ideal")
    for p in (1, 8, 64, 512):
        ew = T_debil(1) / T_debil(p)
        g = s + (1 - s) * p
        print(f"  p={p:4d}: T = {T_debil(p):.4f}, eficiencia = {ew:.3f}, Gustafson S = {g:.1f}")
    prueba(abs((s + (1 - s) * 1) - 1.0) < 1e-12, "Gustafson con p=1")
    prueba(T_debil(512) > T_debil(1), "la comunicación cuesta incluso en escalado débil")

    texto = guion_slurm("transito", 2, 64, "00:30:00", "general", "python analisis.py")
    print("guion de sbatch generado:")
    print(texto)
    for d in ("--job-name=transito", "--nodes=2", "--ntasks=64", "--time=00:30:00", "--partition=general"):
        prueba(f"#SBATCH {d}" in texto, f"directiva {d}")
    prueba(texto.startswith("#!/bin/bash"), "línea shebang")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
