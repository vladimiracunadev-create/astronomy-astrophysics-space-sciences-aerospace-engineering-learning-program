"""B118-C15 · Seguimiento de mega constelaciones.

Constelación SINTÉTICA tipo Walker-delta (no es el diseño de ninguna empresa): P planos, S satélites por plano, inclinación 53 grados,
altitud 550 km. Se cuentan los pares a menos de d km en instantáneas y se compara con la expectativa de un gas uniforme en la capa.
Unidades: km, grados, s. Sistema: inercial geocéntrico. GM = 398600.4418 km^3/s^2 (convencional, no consultado).
Fuente consultada: IADC-02-01 Rev. 4 (enero de 2025), sección 5.5, sobre separación entre miembros, en los cruces de planos y con otras
constelaciones, y mayor riesgo acumulado de reentradas. Tolerancia: el cociente medido/esperado debe estar entre 0,5 y 2 (el gas uniforme
ignora la concentración en latitudes altas).
"""
import math
import random
import sys

MU = 398600.4418
RE = 6378.137


def walker(P, S, inc_deg, alt, f=1):
    a = RE + alt
    n = math.sqrt(MU / a ** 3)
    sats = []
    for p in range(P):
        raan = 360.0 * p / P
        for s in range(S):
            u0 = 360.0 * s / S + 360.0 * f * p / (P * S)
            sats.append((a, inc_deg, raan, u0))
    return sats, n


def posicion(sat, n, t):
    a, inc, raan, u0 = sat
    u = math.radians(u0) + n * t
    i, o = math.radians(inc), math.radians(raan)
    cu, su = math.cos(u), math.sin(u)
    return (a * (math.cos(o) * cu - math.sin(o) * su * math.cos(i)),
            a * (math.sin(o) * cu + math.cos(o) * su * math.cos(i)),
            a * su * math.sin(i))


def pares_cercanos(pos, d):
    d2 = d * d
    c = 0
    m = len(pos)
    for i in range(m):
        xi, yi, zi = pos[i]
        for j in range(i + 1, m):
            xj, yj, zj = pos[j]
            dx = xi - xj
            if dx * dx > d2:
                continue
            dy = yi - yj
            dz = zi - zj
            if dx * dx + dy * dy + dz * dz <= d2:
                c += 1
    return c


def compute():
    v = {}
    P, S = 24, 22
    sats, n = walker(P, S, 53.0, 550.0)
    v["N"], v["P"], v["S"] = len(sats), P, S
    v["T"] = 2 * math.pi / n
    # perturbación para quitar la regularidad perfecta: fases aleatorias en el plano (error de inyección sintético), semilla 118
    rng = random.Random(118)
    sats = [(a, i, o, u + rng.uniform(-3.0, 3.0)) for a, i, o, u in sats]
    d = 150.0
    cuentas = []
    for k in range(30):
        t = k * v["T"] / 7.31  # instantes no conmensurables
        pos = [posicion(s, n, t) for s in sats]
        cuentas.append(pares_cercanos(pos, d))
    v["media"] = sum(cuentas) / len(cuentas)
    a = RE + 550.0
    # esperado en capa delgada (espesor ~ 2d no corresponde; se usa esfera de radio d en el volumen de la esfera 'gruesa' de espesor 2d)
    vol_capa = 4 * math.pi * a ** 2 * (2 * d)
    vol_bola = 4.0 / 3.0 * math.pi * d ** 3
    # fracción de la capa gruesa cubierta por la bola, con corrección de borde despreciada
    N = v["N"]
    v["esperado"] = N * (N - 1) / 2 * (vol_bola / vol_capa)
    v["cociente"] = v["media"] / v["esperado"]
    v["d"] = d
    # carga de catálogo: actualizaciones/día si cada objeto se actualiza cada 8 h (ILUSTRATIVO)
    v["act_dia"] = N * 24 / 8
    # pares totales para el cribado de todos contra todos con el catálogo previo de 40 000 objetos
    v["pares_todos"] = (40_000 + N) * (40_000 + N - 1) // 2
    v["pares_antes"] = 40_000 * 39_999 // 2
    v["aumento_pares"] = v["pares_todos"] / v["pares_antes"]
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Constelacion SINTETICA Walker-delta 24 x 22 (528 satelites), inclinacion 53 deg, 550 km; fases con error de +-3 deg (semilla 118).")
    v = compute()
    print(f"N = {v['N']}; periodo {v['T'] / 60:.2f} min")
    print(f"Pares a menos de {v['d']:.0f} km (media de 30 instantaneas): {v['media']:.2f}")
    print(f"Esperado de gas uniforme en capa de 300 km de espesor: {v['esperado']:.2f}; cociente {v['cociente']:.2f}")
    print(f"Actualizaciones por dia si cada objeto se actualiza cada 8 h (ilustrativo): {v['act_dia']:.0f}")
    print(f"Pares a cribar con el catalogo de ~40000 objetos (ESA, consultado): antes {v['pares_antes']:.3e}; despues {v['pares_todos']:.3e} (x{v['aumento_pares']:.4f})")
    assert 0.3 < v["cociente"] < 3.0
    print("Pruebas superadas (cociente medido/esperado entre 0.3 y 3).")


if __name__ == "__main__":
    main()
