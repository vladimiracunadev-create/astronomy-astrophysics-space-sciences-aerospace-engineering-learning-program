#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C14: deriva del semieje por empuje termico tangencial (Yarkovsky) y barrera de rotacion de un cumulo de escombros.

Datos: asteroide SINTETICO en orbita circular de a = 1.3 au con una aceleracion tangencial CONSTANTE de 3e-10 au/dia^2 (valor ilustrativo EXAGERADO unas 10^4 veces respecto del fisico, para que el efecto
sea medible en 50 anios). Constantes (k de Gauss, G = 6.674e-11, c, luminosidad solar, 1 au) del autor, NO consultadas. Para la tabla fisica: eficiencia termica eta = 0.03, densidad 2000 kg/m^3 y radios de
50, 100 y 500 m, todos ILUSTRATIVOS. La forma de la aceleracion F/m = eta (S/c)(3/(4 R rho)) es un modelo simple del autor, no la teoria completa de Yarkovsky.
Modelo: ecuacion de Gauss para orbita circular da/dt = 2 a_T / n ; desplazamiento angular acumulado Dtheta = -(3/4)(n/a)(da/dt) t^2. Se contrasta con la integracion leapfrog de la orbita con
la aceleracion tangencial (paso 0.1 d, 50 anios). Barrera de rotacion: centrifuga = gravedad en el ecuador de una esfera: P_min = sqrt(3 pi / (G rho)). Unidades: au, dia, SI en la tabla fisica.
Supuestos: orbita circular, aceleracion constante y pequeña, sin otras perturbaciones. Validez: ilustrativa.
Tolerancia: da numerico frente a Gauss 2 %; Dtheta numerico frente a la formula 5 %; P_min(2000 kg/m3) = 2.33 +- 0.01 h.
"""
import math, platform

K = 0.01720209895
GM = K * K
AU = 1.495978707e11
G = 6.674e-11
C = 299792458.0
L_SOL = 3.828e26

def integrar(a0, aT, dias, dt):
    x, y = a0, 0.0
    vx, vy = 0.0, math.sqrt(GM / a0)
    th, thp = 0.0, 0.0
    t = 0.0
    n = int(round(dias / dt))
    def acc(x, y, vx, vy):
        r3 = (x * x + y * y) ** 1.5
        v = math.hypot(vx, vy)
        return -GM * x / r3 + aT * vx / v, -GM * y / r3 + aT * vy / v
    ax, ay = acc(x, y, vx, vy)
    for _ in range(n):
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        x += dt * vx; y += dt * vy
        ax, ay = acc(x, y, vx, vy)
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        ang = math.atan2(y, x)
        d = (ang - thp + math.pi) % (2 * math.pi) - math.pi
        th += d; thp = ang
    r = math.hypot(x, y); v2 = vx * vx + vy * vy
    a_f = -GM / (2 * (0.5 * v2 - GM / r))
    return a_f, th

def calcular():
    a0, aT, dias = 1.3, 3e-10, 50 * 365.25
    n = K / a0 ** 1.5
    af, th = integrar(a0, aT, dias, 0.1)
    dadt = 2 * aT / n
    da_ana = dadt * dias
    dth_ana = -0.75 * (n / a0) * dadt * dias ** 2
    dth_num = th - n * dias
    # tabla fisica
    tabla = []
    for R in (50.0, 100.0, 500.0):
        S = L_SOL / (4 * math.pi * (1.3 * AU) ** 2)
        a_T = 0.03 * (S / C) * 3.0 / (4 * R * 2000.0)           # m/s^2
        a_T_au = a_T * 86400.0 ** 2 / AU                        # au/dia^2
        dadt_ = 2 * a_T_au / n * 365.25 * 1e6                   # au/Myr
        dth = 0.75 * (n / a0) * (2 * a_T_au / n) * (100 * 365.25) ** 2
        tabla.append((R, a_T, dadt_, dth * a0 * AU / 1e3))
    barrera = [(rho, math.sqrt(3 * math.pi / (G * rho)) / 3600.0) for rho in (1000.0, 2000.0, 3000.0)]
    P0 = 4 * 3600.0; w0 = 2 * math.pi / P0
    tau = w0 / (1e-3 / (365.25 * 86400.0) ** 2) / (365.25 * 86400.0) / 1e6
    return {"da_num": af - a0, "da_ana": da_ana, "err_a": abs((af - a0) / da_ana - 1), "dth_num": dth_num, "dth_ana": dth_ana,
            "err_t": abs(dth_num / dth_ana - 1), "tabla": tabla, "barrera": barrera, "tau": tau, "n": n}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Aceleracion tangencial de prueba 3e-10 au/dia^2 durante 50 anios, a0 = 1.3 au")
    print("  Delta a: integrado = %.4e au ; Gauss = %.4e au ; diferencia = %.2f %%" % (r["da_num"], r["da_ana"], 100 * r["err_a"]))
    print("  Delta theta - n t: integrado = %.4e rad ; formula = %.4e rad ; diferencia = %.2f %%" % (r["dth_num"], r["dth_ana"], 100 * r["err_t"]))
    print("Tabla fisica ilustrativa (eta = 0.03, rho = 2000 kg/m3, a = 1.3 au):")
    for R, aT, dadt, dx in r["tabla"]:
        print("  R = %5.0f m : a_T = %.2e m/s^2 ; da/dt = %.2e au/Myr ; desplazamiento a lo largo de la orbita en 100 anios = %.1f km" % (R, aT, dadt, dx))
    for rho, P in r["barrera"]:
        print("Barrera de rotacion (rho = %.0f kg/m3): P_min = %.3f h" % (rho, P))
    print("Tiempo para duplicar la velocidad angular con 1e-3 rad/anio^2 desde P = 4 h: %.2f Manios (valor ilustrativo)" % r["tau"])
    assert r["err_a"] < 0.02 and r["err_t"] < 0.05
    assert abs(r["barrera"][1][1] - 2.33) < 0.01
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
