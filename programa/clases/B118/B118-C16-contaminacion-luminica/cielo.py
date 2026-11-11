"""B118-C16 · Contaminación lumínica.

(1) Geometría de iluminación: un satélite sobre el cenit de un observador está al sol si h > R (sec d - 1) para una depresión solar d.
(2) Brillo: esfera difusa de diámetro D y albedo p (misma fotometría que B118-C03), magnitud solar -26,74 (convención, no consultada).
(3) Trazas: número esperado de trazas en una exposición, rho (D L + pi D^2/4), verificado por Monte Carlo en un parche plano (semilla 118).
Constelación de 5000 satélites a 550 km, diámetro equivalente 2 m, albedo 0,25: ILUSTRATIVOS (no es un sistema real).
Unidades: km, grados, magnitudes, deg^2. Tolerancia: 4 % entre la fórmula y el Monte Carlo.
"""
import math
import random
import sys

R = 6371.0   # km, radio medio terrestre (convencional, no consultado)
M_SOL = -26.74


def delta_max(h):
    return math.degrees(math.acos(R / (R + h)))


def h_sombra(d_deg):
    return R * (1.0 / math.cos(math.radians(d_deg)) - 1.0)


def rango_oblicuo(h, elev_deg):
    e = math.radians(elev_deg)
    return math.sqrt((R + h) ** 2 - (R * math.cos(e)) ** 2) - R * math.sin(e)


def fase_lambert(alfa):
    return (2.0 / (3.0 * math.pi)) * ((math.pi - alfa) * math.cos(alfa) + math.sin(alfa))


def magnitud(d_m, rango_km, fase_deg, albedo):
    r = d_m / 2.0
    c = albedo * r * r * fase_lambert(math.radians(fase_deg)) / ((rango_km * 1000.0) ** 2)
    return M_SOL - 2.5 * math.log10(c)


def casquete(h, elev_min_deg):
    psi = math.acos(R * math.cos(math.radians(elev_min_deg)) / (R + h)) - math.radians(elev_min_deg)
    frac = (1 - math.cos(psi)) / 2.0
    omega_sr = 2 * math.pi * (1 - math.sin(math.radians(elev_min_deg)))  # ángulo sólido del cielo sobre elev_min
    return psi, frac, math.degrees(1) ** 2 * omega_sr


def mc_trazas(rho, D, L, semilla=118, ensayos=3000, lado=40.0):
    rng = random.Random(semilla)
    n_p = rho * lado * lado
    tot = 0
    for _ in range(ensayos):
        n = 0
        k = int(n_p)
        if rng.random() < n_p - k:
            k += 1
        for _ in range(k):
            x, y = rng.uniform(-lado / 2, lado / 2), rng.uniform(-lado / 2, lado / 2)
            th = rng.uniform(0, 2 * math.pi)
            ux, uy = math.cos(th), math.sin(th)
            # distancia del origen al segmento (x,y) -> (x+L ux, y+L uy)
            t = max(0.0, min(L, -(x * ux + y * uy)))
            px, py = x + t * ux, y + t * uy
            if px * px + py * py <= (D / 2) ** 2:
                n += 1
        tot += n
    return tot / ensayos


def compute():
    v = {}
    v["dmax_550"] = delta_max(550.0)
    v["hs"] = [(d, h_sombra(d)) for d in (6, 12, 18)]
    v["dmax_1200"] = delta_max(1200.0)
    v["min_crepusculo_550"] = v["dmax_550"] * 4.0  # minutos a 15 grados/hora en el ecuador
    v["rango_zenit"] = rango_oblicuo(550.0, 90.0)
    v["rango_30"] = rango_oblicuo(550.0, 30.0)
    v["m_zenit"] = magnitud(2.0, v["rango_zenit"], 90.0, 0.25)
    v["m_30"] = magnitud(2.0, v["rango_30"], 90.0, 0.25)
    v["m_osc"] = magnitud(2.0, v["rango_zenit"], 90.0, 0.125)
    v["dm_osc"] = v["m_osc"] - v["m_zenit"]
    N = 5000
    psi, frac, omega_deg2 = casquete(550.0, 20.0)
    v["psi"], v["frac_casq"] = math.degrees(psi), frac
    soleados = 0.5
    v["n_vis"] = N * frac * soleados
    v["omega_deg2"] = omega_deg2
    v["rho"] = v["n_vis"] / omega_deg2
    omega_ang = 0.5  # grados/s, velocidad angular media ILUSTRATIVA
    D = 3.0  # grados, diámetro del campo
    v["traza_L"] = omega_ang * 30.0
    v["trazas_formula"] = v["rho"] * (D * v["traza_L"] + math.pi * D * D / 4.0)
    # MC con la densidad real (valor pequeño) es ruidoso: se usa una densidad 100 veces mayor y se reescala
    rho_mc = v["rho"] * 100
    v["trazas_mc"] = mc_trazas(rho_mc, D, v["traza_L"]) / 100.0
    v["trazas_formula_mc"] = rho_mc * (D * v["traza_L"] + math.pi * D * D / 4.0) / 100.0
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Constelacion ILUSTRATIVA: 5000 satelites a 550 km, D equivalente 2 m, albedo 0.25; magnitud solar convencional (no consultada).")
    v = compute()
    print(f"Profundidad solar maxima para un satelite en el cenit: 550 km -> {v['dmax_550']:.2f} deg; 1200 km -> {v['dmax_1200']:.2f} deg")
    print("Altura de la sombra sobre el cenit: " + "; ".join(f"d = {d} deg -> {h:.0f} km" for d, h in v["hs"]))
    print(f"Duracion de la ventana de iluminacion en el ecuador (15 deg/h): {v['min_crepusculo_550']:.0f} min a 550 km")
    print(f"Rango: cenit {v['rango_zenit']:.0f} km; elevacion 30 deg {v['rango_30']:.0f} km")
    print(f"Magnitud (fase 90 deg): cenit {v['m_zenit']:.2f}; 30 deg {v['m_30']:.2f}; con albedo a la mitad {v['m_osc']:.2f} (diferencia {v['dm_osc']:.3f} = 2.5 log10 2)")
    print(f"Casquete visible (elevacion > 20 deg): angulo central {v['psi']:.2f} deg, fraccion de la capa {v['frac_casq']:.4f}; satelites iluminados visibles {v['n_vis']:.1f}")
    print(f"Densidad {v['rho']:.5f} /deg^2; trazas esperadas en 30 s, campo de 3 deg: {v['trazas_formula']:.3f}")
    print(f"Verificacion Monte Carlo (densidad x100, reescalada): formula {v['trazas_formula_mc']:.4f}; MC {v['trazas_mc']:.4f}")
    assert abs(v["dm_osc"] - 2.5 * math.log10(2)) < 1e-9
    assert abs(v["trazas_mc"] - v["trazas_formula_mc"]) / v["trazas_formula_mc"] < 0.04
    print("Pruebas superadas (2.5 log10 2 exacto; trazas MC vs formula a 4 %).")


if __name__ == "__main__":
    main()
