# SPDX-License-Identifier: Apache-2.0
"""B85-C18: modelado térmico por nodos: red de cuatro nodos con conducción y radiación, solución estacionaria y transitoria.

Consultado: SIGMA (NIST), S0 (NASA/NSSDC). ILUSTRATIVO y SINTÉTICO: nodos, conductancias, capacidades, áreas, cargas, propiedades ópticas.
Segunda vía: caso de dos nodos con solución analítica; cierre de energía; transitorio implícito frente al estacionario.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

NOMBRES = ["panel", "estructura", "electronica", "radiador"]
# conductancias [W/K] entre nodos (i, j, G)
G = [(0, 1, 2.0), (1, 2, 1.5), (1, 3, 3.0), (2, 3, 1.0)]
# radiacion al espacio: eps*sigma*A por nodo [W/K^4 * sigma incluido en el producto]; 0 => no radia
EA = [0.8 * 0.5, 0.0, 0.0, 0.85 * 0.4]      # eps*A [m2]
CAP = [400.0, 1500.0, 900.0, 600.0]          # J/K
Q = [0.3 * S0 * 0.5, 0.0, 30.0, 0.0]         # W: panel absorbe alfa S A; electronica disipa 30 W


def residuo(T, q=Q, ea=EA, g=G, t_sink=0.0):
    n = len(T)
    r = [q[i] - SIGMA * ea[i] * (T[i] ** 4 - t_sink ** 4) for i in range(n)]
    for i, j, gij in g:
        r[i] -= gij * (T[i] - T[j])
        r[j] -= gij * (T[j] - T[i])
    return r


def jacobiano(T, ea=EA, g=G):
    n = len(T)
    J = [[0.0] * n for _ in range(n)]
    for i in range(n):
        J[i][i] -= 4 * SIGMA * ea[i] * T[i] ** 3
    for i, j, gij in g:
        J[i][i] -= gij; J[j][j] -= gij
        J[i][j] += gij; J[j][i] += gij
    return J


def estacionario(q=Q, ea=EA, g=G, T0=None):
    T = T0[:] if T0 else [280.0] * len(q)
    for it in range(60):
        r = residuo(T, q, ea, g)
        if max(abs(x) for x in r) < 1e-10:
            break
        dT = resolver_lineal(jacobiano(T, ea, g), [-x for x in r])
        T = [T[i] + dT[i] for i in range(len(T))]
    return T, it


def transitorio(T0, dt=10.0, t_fin=20000.0, q=Q):
    """Euler implicito linealizado: (C/dt - J) dT = r."""
    T = T0[:]
    n = len(T)
    hist = [(0.0, T[:])]
    for k in range(int(t_fin / dt)):
        r = residuo(T, q)
        J = jacobiano(T)
        A = [[-J[i][j] + (CAP[i] / dt if i == j else 0.0) for j in range(n)] for i in range(n)]
        dT = resolver_lineal(A, r)
        T = [T[i] + dT[i] for i in range(n)]
        hist.append(((k + 1) * dt, T[:]))
    return hist


def dos_nodos():
    """Q entra en A, conduce a B (G) y B radia (eps A): T_B = (Q/(eps sigma A))^0.25, T_A = T_B + Q/G."""
    q, gg, ea = 20.0, 4.0, 0.3
    T, _ = estacionario([q, 0.0], [0.0, ea], [(0, 1, gg)], [300.0, 300.0])
    tb = (q / (SIGMA * ea)) ** 0.25
    return T, [tb + q / gg, tb]


def calcular():
    r = {}
    r["T"], r["iter"] = estacionario()
    r["res"] = max(abs(x) for x in residuo(r["T"]))
    r["rad_total"] = sum(SIGMA * EA[i] * r["T"][i] ** 4 for i in range(4))
    r["q_total"] = sum(Q)
    r["dos_num"], r["dos_ana"] = dos_nodos()
    h = transitorio([250.0] * 4)
    r["T_fin_trans"] = h[-1][1]
    r["tiempo_90"] = next(t for t, T in h if max(abs(T[i] - r["T"][i]) for i in range(4)) < 0.1 * max(abs(250.0 - r["T"][i]) for i in range(4)))
    q2 = Q[:]; q2[2] = 60.0
    r["T_60W"], _ = estacionario(q2)
    ea2 = EA[:]; ea2[3] = 0.85 * 0.8
    r["T_rad_doble"], _ = estacionario(Q, ea2)
    g2 = [(0, 1, 2.0), (1, 2, 1.5), (1, 3, 3.0), (2, 3, 4.0)]
    r["T_g23_alta"], _ = estacionario(Q, EA, g2)
    return r


def main():
    r = calcular()
    cabecera()
    print("Modelo ILUSTRATIVO de 4 nodos (panel, estructura, electronica, radiador), sumidero a 0 K, panel absorbe 0.3*S0*0.5 m2, electronica disipa 30 W")
    print(f"Estacionario (Newton, {r['iter']} iteraciones): " + "; ".join(f"{n} {t:.2f} K" for n, t in zip(NOMBRES, r["T"])))
    print(f"Residuo maximo = {r['res']:.2e} W ; potencia radiada = {r['rad_total']:.4f} W ; potencia de entrada = {r['q_total']:.4f} W")
    print(f"Caso de dos nodos (analitico): numerico T_A = {r['dos_num'][0]:.4f} K, T_B = {r['dos_num'][1]:.4f} K ; analitico T_A = {r['dos_ana'][0]:.4f} K, T_B = {r['dos_ana'][1]:.4f} K")
    print(f"Transitorio implicito desde 250 K (paso 10 s, 20000 s): " + "; ".join(f"{t:.2f}" for t in r["T_fin_trans"]) + f" K ; 90 % del cambio a los {r['tiempo_90']:.0f} s")
    print(f"Electronica a 60 W: " + "; ".join(f"{n} {t:.2f}" for n, t in zip(NOMBRES, r["T_60W"])) + " K")
    print(f"Radiador de area doble: electronica {r['T_rad_doble'][2]:.2f} K ; G(electronica-radiador) = 4 W/K: electronica {r['T_g23_alta'][2]:.2f} K")
    comprobar(abs(r["rad_total"] - r["q_total"]) < 1e-8, "cierre de energia")
    comprobar(all(abs(a - b) < 1e-6 for a, b in zip(r["dos_num"], r["dos_ana"])), "dos nodos")
    comprobar(max(abs(a - b) for a, b in zip(r["T_fin_trans"], r["T"])) < 0.05, "transitorio -> estacionario")
    fin()


if __name__ == "__main__":
    main()
