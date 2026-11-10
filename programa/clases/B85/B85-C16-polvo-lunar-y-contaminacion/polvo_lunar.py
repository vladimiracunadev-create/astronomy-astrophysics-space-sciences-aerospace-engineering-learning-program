# SPDX-License-Identifier: Apache-2.0
"""B85-C16: polvo lunar sobre un radiador: cobertura, absortividad efectiva y temperatura.

Consultado: SIGMA (NIST), S0 (NASA/NSSDC). ILUSTRATIVO y NO CONSULTADO: flujo másico de polvo, densidad y diámetro de grano,
α y ε del polvo y del radiador, geometría de iluminación, temperatura del suelo, carga térmica.
Segunda vía: simulación de Monte Carlo (semilla fija) de discos aleatorios frente a la cobertura analítica 1 - exp(-λ).
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

RHO_G, D_G = 3000.0, 20e-6          # kg/m3, m (ilustrativos)
ALFA_R, EPS_R = 0.10, 0.85          # radiador limpio
ALFA_D, EPS_D = 0.85, 0.90          # polvo
Q_INT = 150.0                       # W/m2 de carga (ilustrativo)
COS_SOL, F_SUELO, T_SUELO = 0.5, 0.3, 380.0
SEMILLA = 20261110


def cobertura(masa_m2):
    """Fraccion cubierta si el polvo se deposita en monocapa sin apilarse: modelo de Boole 1 - exp(-lambda), lambda = N * area proyectada."""
    n = masa_m2 / (RHO_G * math.pi * D_G ** 3 / 6)
    lam = n * math.pi * D_G ** 2 / 4
    return 1 - math.exp(-lam), lam


def propiedades(f):
    return ALFA_R * (1 - f) + ALFA_D * f, EPS_R * (1 - f) + EPS_D * f


def temperatura(f):
    a, e = propiedades(f)
    q_abs = a * S0 * COS_SOL + e * F_SUELO * SIGMA * T_SUELO ** 4
    # balance: e sigma T^4 = Q_int + q_abs  (radiador al espacio de fondo ~0 K)
    return ((Q_INT + q_abs) / (e * SIGMA)) ** 0.25


def monte_carlo(lam, n_pts=40000, lado=40.0):
    """Discos de diametro 1 en un cuadrado periodico de lado 'lado'; devuelve la fraccion cubierta."""
    rng = random.Random(SEMILLA)
    area_disco = math.pi / 4
    n_d = int(round(lam * lado * lado / area_disco))
    cx = [rng.random() * lado for _ in range(n_d)]
    cy = [rng.random() * lado for _ in range(n_d)]
    celdas = {}
    for i, (x, y) in enumerate(zip(cx, cy)):
        celdas.setdefault((int(x), int(y)), []).append(i)
    cubiertos = 0
    for _ in range(n_pts):
        x, y = rng.random() * lado, rng.random() * lado
        gx, gy = int(x), int(y)
        hit = False
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for i in celdas.get(((gx + dx) % int(lado), (gy + dy) % int(lado)), []):
                    ddx = abs(x - cx[i]); ddx = min(ddx, lado - ddx)
                    ddy = abs(y - cy[i]); ddy = min(ddy, lado - ddy)
                    if ddx * ddx + ddy * ddy <= 0.25:
                        hit = True
                        break
                if hit:
                    break
            if hit:
                break
        cubiertos += hit
    return cubiertos / n_pts


def calcular():
    r = {"filas": []}
    for m_g in (0.0, 0.5, 2.0, 5.0, 14.0, 40.0):
        f, lam = cobertura(m_g * 1e-3)
        a, e = propiedades(f)
        r["filas"].append((m_g, f, a, e, temperatura(f)))
    r["t_limpio"] = r["filas"][0][4]
    r["t_sucio"] = r["filas"][4][4]
    r["grano_masa"] = RHO_G * math.pi * D_G ** 3 / 6
    r["monte_carlo"] = monte_carlo(0.5)
    r["analitico"] = 1 - math.exp(-0.5)
    r["dias_14g"] = 14.0e-3 / 0.5e-3        # ilustrativo: 0.5 g/m2 por dia -> dias hasta 14 g/m2
    r["m_para_30"] = -math.log(1 - 0.30) / (math.pi * D_G ** 2 / 4) * RHO_G * math.pi * D_G ** 3 / 6
    r["dt_100"] = r["t_sucio"] - r["t_limpio"]
    # contaminacion molecular (ILUSTRATIVA): material con CVCM sobre un radiador de 1 m2 con un factor de vista
    masa_mat, cvcm, f_vista, rho_c, k_alfa = 2.0, 0.001, 0.05, 1000.0, 0.5   # kg, -, -, kg/m3, delta_alfa por um
    r["m_cond"] = masa_mat * cvcm * f_vista
    r["esp_um"] = r["m_cond"] / rho_c * 1e6
    r["dalfa_cont"] = k_alfa * r["esp_um"]
    a_c, e_c = ALFA_R + r["dalfa_cont"], EPS_R
    q_abs = a_c * S0 * COS_SOL + e_c * F_SUELO * SIGMA * T_SUELO ** 4
    r["t_contam"] = ((Q_INT + q_abs) / (e_c * SIGMA)) ** 0.25
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Grano ILUSTRATIVO: d = {D_G*1e6:.0f} um, rho = {RHO_G:.0f} kg/m3, masa = {r['grano_masa']:.3e} kg ; radiador alfa/eps = {ALFA_R}/{EPS_R}; polvo {ALFA_D}/{EPS_D}")
    print(f"Radiador con {Q_INT:.0f} W/m2 de carga, cos(sol) = {COS_SOL}, suelo a {T_SUELO:.0f} K con F = {F_SUELO}")
    print(f"{'masa [g/m2]':>13}{'cobertura':>11}{'alfa_ef':>9}{'eps_ef':>9}{'T [K]':>9}")
    for m, f, a, e, t in r["filas"]:
        print(f"{m:>13.1f}{f:>11.4f}{a:>9.4f}{e:>9.4f}{t:>9.2f}")
    print(f"Masa para cubrir el 30 % = {r['m_para_30']*1e3:.2f} g/m2 ; con 14 g/m2 la temperatura sube {r['dt_100']:.2f} K")
    print(f"Con un deposito ILUSTRATIVO de 0.5 g/m2/dia, 14 g/m2 se alcanzan en {r['dias_14g']:.0f} dias")
    print(f"Contaminacion molecular ILUSTRATIVA: {r['m_cond']*1e3:.2f} g condensables llegan al radiador -> espesor {r['esp_um']:.3f} um ; delta alfa = {r['dalfa_cont']:.4f} ; T = {r['t_contam']:.2f} K")
    print(f"Cobertura para lambda = 0.5: Monte Carlo = {r['monte_carlo']:.4f} ; analitica = {r['analitico']:.4f}")
    comprobar(abs(r["monte_carlo"] - r["analitico"]) < 0.01, "Monte Carlo frente a analitica")
    comprobar(all(r["filas"][i][4] <= r["filas"][i + 1][4] + 1e-9 for i in range(len(r["filas"]) - 1)), "T creciente con el polvo")
    fin()


if __name__ == "__main__":
    main()
