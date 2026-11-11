"""B118-C05 · Conjunciones orbitales.

Propagación kepleriana (dos cuerpos) de dos satélites SINTÉTICOS en órbitas circulares de 700 km; búsqueda del instante de
máxima aproximación (TCA) y comparación con la expresión analítica.
Unidades: km, s, km/s, grados. Sistema: inercial geocéntrico (ECI) con el plano ecuatorial como referencia.
GM = 398600.4418 km^3/s^2 (valor convencional, no consultado en esta clase). Tolerancia: 1e-3 km en la distancia; 1e-6 relativa en v_rel.
"""
import math
import sys

MU = 398600.4418
RE = 6378.137


def estado_circular(a, inc_deg, raan_deg, u0_deg, t):
    n = math.sqrt(MU / a ** 3)
    u = math.radians(u0_deg) + n * t
    i, o = math.radians(inc_deg), math.radians(raan_deg)
    cu, su, ci, si, co, so = math.cos(u), math.sin(u), math.cos(i), math.sin(i), math.cos(o), math.sin(o)
    r = (a * (co * cu - so * su * ci), a * (so * cu + co * su * ci), a * su * si)
    vc = a * n
    v = (vc * (-co * su - so * cu * ci), vc * (-so * su + co * cu * ci), vc * cu * si)
    return r, v


def dist(t, e1, e2):
    r1, _ = estado_circular(*e1, t)
    r2, _ = estado_circular(*e2, t)
    return math.dist(r1, r2)


def tca(e1, e2, t0, t1, paso=1.0):
    mejor_t, mejor_d = t0, 1e99
    t = t0
    while t <= t1:
        d = dist(t, e1, e2)
        if d < mejor_d:
            mejor_t, mejor_d = t, d
        t += paso
    a, b = mejor_t - paso, mejor_t + paso
    g = (math.sqrt(5) - 1) / 2
    for _ in range(80):
        c, d_ = b - g * (b - a), a + g * (b - a)
        if dist(c, e1, e2) < dist(d_, e1, e2):
            b = d_
        else:
            a = c
    t = (a + b) / 2
    return t, dist(t, e1, e2)


def compute():
    v = {}
    a = RE + 700.0
    n = math.sqrt(MU / a ** 3)
    v["T"] = 2 * math.pi / n
    v["vc"] = a * n
    # sat 1: inc 98, RAAN 0; sat 2: inc 82, RAAN 0 -> se cruzan en los nodos (u = 0)
    e1 = (a, 98.0, 0.0, 0.0)
    # sat 2 llega al nodo ascendente con un retraso dt (fase negativa -> pasa después)
    dt = 2.0  # s
    e2 = (a, 82.0, 0.0, -math.degrees(n * dt))
    # relativa en el nodo (t ~ dt/2)
    r1, v1 = estado_circular(*e1, 0.0)
    r2, v2 = estado_circular(*e2, dt)
    v["vrel_analitica"] = 2 * v["vc"] * math.sin(math.radians(98.0 - 82.0) / 2.0)
    v["vrel_num"] = math.dist(v1, v2)
    t_star, d_star = tca(e1, e2, -60.0, 60.0)
    v["tca"], v["miss"] = t_star, d_star
    # geometría lineal: P1(t) = vc t u1, P2(t) = vc (t - dt) u2 con u1.u2 = cos(theta), theta = 16 grados.
    # |P1 - P2|^2 / vc^2 = t^2 + (t - dt)^2 - 2 t (t - dt) cos(theta); su mínimo está en t = dt/2 y vale (dt^2/2)(1 + cos theta),
    # es decir miss = vc dt cos(theta/2).
    theta = math.radians(98.0 - 82.0)
    c = math.cos(theta)
    t_opt = dt / 2.0
    d2 = t_opt ** 2 + (t_opt - dt) ** 2 - 2 * t_opt * (t_opt - dt) * c
    v["miss_plano"] = v["vc"] * math.sqrt(d2)
    v["miss_cos"] = v["vc"] * dt * math.cos(theta / 2.0)
    # incremento de la distancia con el retraso: duplicar dt duplica el miss (lineal)
    e2b = (a, 82.0, 0.0, -math.degrees(n * 2 * dt))
    v["miss_doble"] = tca(e1, e2b, -60.0, 60.0)[1]
    v["cociente_miss"] = v["miss_doble"] / v["miss"]
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Dos satelites SINTETICOS en orbita circular de 700 km (inc 98 y 82 grados, mismo RAAN); dos cuerpos, sin perturbaciones.")
    v = compute()
    print(f"Periodo {v['T'] / 60:.2f} min; velocidad circular {v['vc']:.4f} km/s")
    print(f"Velocidad relativa en el nodo: analitica 2 v sin(di/2) = {v['vrel_analitica']:.4f} km/s; numerica {v['vrel_num']:.4f} km/s")
    print(f"TCA (retraso de 2 s): t = {v['tca']:.3f} s respecto al nodo; distancia de paso = {v['miss']:.4f} km")
    print(f"Distancia de paso por geometria de rectas: {v['miss_plano']:.4f} km")
    print(f"Con retraso de 4 s: {v['miss_doble']:.4f} km (cociente {v['cociente_miss']:.4f}; esperado 2 en el limite lineal)")
    assert abs(v["vrel_analitica"] - v["vrel_num"]) < 1e-6 * v["vrel_analitica"]
    assert abs(v["miss_plano"] - v["miss_cos"]) < 1e-9 * v["miss_cos"]
    assert abs(v["miss"] - v["miss_plano"]) < 0.01 * v["miss_plano"]
    assert abs(v["cociente_miss"] - 2.0) < 0.01
    print("Pruebas superadas (v_rel analitica = numerica; TCA numerico = geometria lineal a 1 %).")


if __name__ == "__main__":
    main()
