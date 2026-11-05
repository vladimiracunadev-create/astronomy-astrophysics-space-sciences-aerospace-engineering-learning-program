#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C20: primer simulador de un movimiento celeste (la Tierra alrededor del Sol).

Datos PUBLICADOS: parametros_tierra.yaml (clase B07-C16): GM del Sol 1,32712e11 km³/s²,
semieje mayor de la Tierra 1,49598e8 km y período sidéreo 365,256 d (NASA NSSDC, fichas
Sun y Earth, consultadas el 2026-11-05). El paso de tiempo (3600 s) es ELEGIDO.
Modelo: problema de dos cuerpos reducido a un punto de masa que se mueve en el plano
alrededor del Sol, fijo en el origen de un sistema inercial heliocéntrico 2D, con
aceleración a = −GM r / |r|³. Condición inicial: órbita circular, r = (a, 0) y
v = (0, sqrt(GM/a)). Sin otros planetas, sin la Luna, sin relatividad. Resultados SIMULADOS.
Integradores: Euler explícito (orden 1) y leapfrog / velocity Verlet (orden 2).
Referencia analítica: período T = 2π sqrt(a³/GM), energía específica E = v²/2 − GM/r y
momento angular específico L = x vy − y vx constantes.
Supuestos: masa de la Tierra despreciable; órbita circular (excentricidad real ≈ 0,017: la
Tierra real no es circular, por eso se compara solo el período). Unidades: km, s, km³/s².
Dominio de validez: una sola partícula de prueba en campo central; pasos con
paso ≪ período. Tolerancias: ver pruebas().
Requiere: numpy 2.4.4, matplotlib 3.10.8, pyyaml 6.0.3 (Python 3.12.9).
"""

from __future__ import annotations

import hashlib
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import yaml

AQUI = Path(__file__).resolve().parent
YAML = AQUI.parent / "B07-C16-formatos-json-y-yaml" / "parametros_tierra.yaml"
FIGURA = AQUI / "orbita_tierra.png"


def cargar_parametros(ruta: Path) -> dict:
    """Lee y valida los parámetros YAML (números positivos); lanza ValueError si no."""
    p = yaml.safe_load(ruta.read_text(encoding="utf-8"))
    for seccion, campo in [("cuerpo_central", "gm_km3_s2"), ("planeta", "semieje_km"),
                           ("planeta", "periodo_sidereo_d"), ("simulacion", "paso_s")]:
        valor = p[seccion][campo]
        if isinstance(valor, bool) or not isinstance(valor, (int, float)) or not valor > 0:
            raise ValueError(f"{seccion}.{campo} debe ser un número positivo, llegó {valor!r}")
    return p


def aceleracion(x: float, y: float, gm: float) -> tuple[float, float]:
    """Aceleración gravitatoria (km/s²) en (x, y) km por un cuerpo de parámetro gm en el origen."""
    r3 = (x * x + y * y) ** 1.5
    return -gm * x / r3, -gm * y / r3


def energia(x, y, vx, vy, gm):
    """Energía específica (km²/s²): v²/2 − GM/r."""
    return 0.5 * (vx * vx + vy * vy) - gm / math.hypot(x, y)


def momento_angular(x, y, vx, vy):
    """Momento angular específico (km²/s): x·vy − y·vx."""
    return x * vy - y * vx


def simular(metodo: str, gm: float, a: float, dt: float, pasos: int) -> np.ndarray:
    """Devuelve un arreglo (pasos+1, 4) con (x, y, vx, vy) en cada instante; metodo 'euler' o 'leapfrog'."""
    if metodo not in ("euler", "leapfrog"):
        raise ValueError(f"método desconocido: {metodo!r}")
    x, y, vx, vy = a, 0.0, 0.0, math.sqrt(gm / a)
    estados = np.empty((pasos + 1, 4))
    estados[0] = (x, y, vx, vy)
    ax, ay = aceleracion(x, y, gm)
    for i in range(pasos):
        if metodo == "euler":
            x, y = x + vx * dt, y + vy * dt
            vx, vy = vx + ax * dt, vy + ay * dt
            ax, ay = aceleracion(x, y, gm)
        else:
            vx += 0.5 * dt * ax
            vy += 0.5 * dt * ay
            x += vx * dt
            y += vy * dt
            ax, ay = aceleracion(x, y, gm)
            vx += 0.5 * dt * ax
            vy += 0.5 * dt * ay
        estados[i + 1] = (x, y, vx, vy)
    return estados


def periodo_analitico_s(gm: float, a: float) -> float:
    """Período de una órbita de semieje a alrededor de un cuerpo de parámetro gm: 2π sqrt(a³/GM)."""
    return 2.0 * math.pi * math.sqrt(a ** 3 / gm)


def metricas(est: np.ndarray, gm: float, a: float) -> dict:
    """Devuelve deriva relativa de energía, de radio y error de cierre (distancia final al inicio, / a)."""
    e0 = energia(*est[0], gm)
    ef = energia(*est[-1], gm)
    return {"dE": (ef - e0) / abs(e0), "dr": math.hypot(est[-1][0], est[-1][1]) / a - 1.0,
            "cierre": math.hypot(est[-1][0] - est[0][0], est[-1][1] - est[0][1]) / a}


def dibujar(gm: float, a: float, ruta: Path) -> None:
    """Guarda una figura con tres órbitas de 60 pasos cada una, con Euler y con leapfrog."""
    t = periodo_analitico_s(gm, a)
    n = 60
    fig, ax = plt.subplots(figsize=(5.4, 5.4), constrained_layout=True)
    for metodo, estilo in (("euler", "-"), ("leapfrog", "--")):
        est = simular(metodo, gm, a, t / n, 3 * n)
        ax.plot(est[:, 0] / 1e6, est[:, 1] / 1e6, estilo, label=f"{metodo} (simulado)")
    ax.plot([0], [0], "o", color="gold", markeredgecolor="k", label="Sol (origen)")
    ax.set_aspect("equal")
    ax.set_xlabel("x (10⁶ km), marco heliocéntrico inercial 2D")
    ax.set_ylabel("y (10⁶ km)")
    ax.set_title("Tres órbitas con 60 pasos por órbita")
    ax.legend(loc="upper right", fontsize=8)
    fig.savefig(ruta, dpi=110)
    plt.close(fig)


def pruebas() -> None:
    """Detiene el programa si el simulador no cumple las referencias analíticas y publicadas."""
    p = cargar_parametros(YAML)
    gm, a, dt = p["cuerpo_central"]["gm_km3_s2"], p["planeta"]["semieje_km"], p["simulacion"]["paso_s"]
    t = periodo_analitico_s(gm, a)
    assert abs(t / 86400.0 / p["planeta"]["periodo_sidereo_d"] - 1.0) < 1e-4            # T analítico vs publicado (0,01 %)
    assert abs(periodo_analitico_s(1.0, 1.0) - 2 * math.pi) < 1e-15                      # caso analítico GM = a = 1
    n = round(t / dt)
    leap = simular("leapfrog", gm, a, dt, n)
    eul = simular("euler", gm, a, dt, n)
    ml, me = metricas(leap, gm, a), metricas(eul, gm, a)
    assert abs(ml["dE"]) < 1e-9 and abs(ml["dr"]) < 1e-9                                 # leapfrog conserva
    assert abs(me["dE"]) > 100 * abs(ml["dE"]) and me["dE"] > 0                          # Euler gana energía
    l0 = momento_angular(*leap[0])
    assert max(abs(momento_angular(*s) / l0 - 1.0) for s in leap) < 1e-9                 # L conservado (leapfrog)
    cierres = []
    for k in (500, 1000, 2000):                                                          # dt = T/k exacto
        cierres.append(metricas(simular("leapfrog", gm, a, t / k, k), gm, a)["cierre"])
    assert 3.5 < cierres[0] / cierres[1] < 4.5 and 3.5 < cierres[1] / cierres[2] < 4.5   # orden 2: ×1/4 al dividir dt por 2
    errores_e = [metricas(simular("euler", gm, a, t / k, k), gm, a)["cierre"] for k in (500, 1000, 2000)]
    assert 1.8 < errores_e[0] / errores_e[1] < 2.2                                       # orden 1: ×1/2
    try:
        simular("rk4", gm, a, dt, 10)
    except ValueError:
        pass
    else:
        raise AssertionError("debía rechazar un método desconocido")
    dibujar(gm, a, FIGURA)
    assert FIGURA.exists() and FIGURA.stat().st_size > 10_000


def main() -> int:
    """Ejecuta las pruebas e imprime las métricas de la simulación."""
    pruebas()
    p = cargar_parametros(YAML)
    gm, a, dt = p["cuerpo_central"]["gm_km3_s2"], p["planeta"]["semieje_km"], p["simulacion"]["paso_s"]
    t = periodo_analitico_s(gm, a)
    n = round(t / dt)
    print(f"python {sys.version.split()[0]} | numpy {np.__version__} | matplotlib {matplotlib.__version__} | pruebas OK")
    print(f"Parámetros: {YAML.name} (sha256 {hashlib.sha256(YAML.read_bytes()).hexdigest()[:12]}…)")
    print(f"Velocidad circular v = {math.sqrt(gm / a):.4f} km/s | T analítico = {t / 86400:.4f} d | "
          f"T publicado = {p['planeta']['periodo_sidereo_d']} d | diferencia = {100 * (t / 86400 / p['planeta']['periodo_sidereo_d'] - 1):+.5f} %")
    print(f"Un año con paso {dt:.0f} s: {n} pasos")
    for metodo in ("euler", "leapfrog"):
        m = metricas(simular(metodo, gm, a, dt, n), gm, a)
        print(f"  {metodo:<9} deriva de energía {m['dE']:+.3e} | deriva de radio {m['dr']:+.3e} | cierre/a {m['cierre']:.3e}")
    print("Convergencia con dt = T/k (error de cierre / a):")
    print(f"  {'k':>5}{'euler':>12}{'leapfrog':>12}")
    for k in (10, 500, 1000, 2000):
        e = metricas(simular("euler", gm, a, t / k, k), gm, a)["cierre"]
        lf = metricas(simular("leapfrog", gm, a, t / k, k), gm, a)["cierre"]
        print(f"  {k:>5}{e:>12.3e}{lf:>12.3e}")
    print(f"Figura guardada: {FIGURA.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
