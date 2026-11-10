#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C15: aerofrenado conceptual en Marte (pasadas sucesivas por una atmosfera exponencial).

Datos consultados (2026-11-10): masa de Marte 0.64169e24 kg, radio ecuatorial 3396.2 km, densidad de superficie ~0.016 kg/m3 (+/- 0.006) y altura de escala 11.0 km (ficha NASA/NSSDC);
G = 6.67430e-11 (registro de cambios del JPL); GM_Marte = G M.
ILUSTRATIVO / SINTETICO: la atmosfera se extiende de forma exponencial rho = rho0 exp(-h/H) con los valores de la ficha (extrapolada a 100-200 km de altitud, donde el modelo real difiere);
coeficiente balistico beta = m/(Cd A) = 100 kg/m2; orbita inicial 110 x 20000 km de altitud; la atmosfera no rota ni hay vientos; sin estacion ni tormentas de polvo.
Modelo: dos cuerpos con arrastre -0.5 rho v^2 / beta en el sentido opuesto a la velocidad inercial, RK4 con paso de 0.5 s dentro de la atmosfera (altitud < 200 km), propagacion analitica de Kepler fuera.
Pruebas: (1) el cambio de energia especifica por pasada, calculado con los elementos, iguala la integral -int(rho v^3/(2 beta)) dt acumulada en la integracion (tol. 1e-3 relativa);
(2) el periapsis cambia menos de 1 km por pasada; (3) el apoapsis decrece monotonicamente.
"""
import math, platform
G = 6.67430e-20
MU = G * 0.64169e24
R = 3396.2
RHO0, H, BETA = 0.016, 11.0, 100.0


def rho(h):
    return RHO0 * math.exp(-h / H)


def acc(r, v):
    rn = math.hypot(*r); vn = math.hypot(*v)
    d = 0.5 * rho(rn - R) * (vn * 1e3) ** 2 / BETA / 1e3
    return [-MU * r[0] / rn**3 - d * v[0] / vn, -MU * r[1] / rn**3 - d * v[1] / vn]


def paso(r, v, dt):
    k1v = acc(r, v); k1r = v
    r2 = [a + 0.5 * dt * b for a, b in zip(r, k1r)]; v2 = [a + 0.5 * dt * b for a, b in zip(v, k1v)]
    k2v = acc(r2, v2); k2r = v2
    r3 = [a + 0.5 * dt * b for a, b in zip(r, k2r)]; v3 = [a + 0.5 * dt * b for a, b in zip(v, k2v)]
    k3v = acc(r3, v3); k3r = v3
    r4 = [a + dt * b for a, b in zip(r, k3r)]; v4 = [a + dt * b for a, b in zip(v, k3v)]
    k4v = acc(r4, v4); k4r = v4
    return ([a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(r, k1r, k2r, k3r, k4r)],
            [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(v, k1v, k2v, k3v, k4v)])


def elems(r, v):
    rn = math.hypot(*r); eps = 0.5 * (v[0] ** 2 + v[1] ** 2) - MU / rn
    a = -MU / (2 * eps); h = r[0] * v[1] - r[1] * v[0]
    e = math.sqrt(max(0.0, 1 + 2 * eps * h * h / MU**2))
    return a, e, eps


def potencia(r, v):
    """potencia disipada por el arrastre por unidad de masa [km2/s3] (positiva)."""
    vn = math.hypot(*v)
    return 0.5 * rho(math.hypot(*r) - R) * (vn * 1e3) ** 2 / BETA / 1e3 * vn


def pasada(a, e):
    rin = R + 200.0
    p = a * (1 - e * e); nu = -math.acos((p / rin - 1) / e)
    r = [rin * math.cos(nu), rin * math.sin(nu)]
    v = [-math.sqrt(MU / p) * math.sin(nu), math.sqrt(MU / p) * (e + math.cos(nu))]
    eps0 = elems(r, v)[2]
    trabajo = 0.0; dt = 0.5
    while True:
        p0 = potencia(r, v)
        r, v = paso(r, v, dt)
        trabajo += 0.5 * (p0 + potencia(r, v)) * dt
        if math.hypot(*r) >= rin and r[0] * v[0] + r[1] * v[1] > 0:
            break
    a2, e2, eps1 = elems(r, v)
    return a2, e2, eps1 - eps0, -trabajo


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rp0, ra0 = R + 110.0, R + 20000.0
    a = 0.5 * (rp0 + ra0); e = (ra0 - rp0) / (ra0 + rp0)
    vp0 = math.sqrt(MU * (1 + e) / rp0)
    print("Pasadas por la atmosfera (densidad exponencial ILUSTRATIVA, beta = 100 kg/m2):")
    print(" pasada   apoapsis [alt, km]   periapsis [alt, km]   periodo [h]   dE por pasada [km2/s2]   trabajo del arrastre [km2/s2]")
    n = 0; prev_ra = ra0; max_drp = 0.0
    print(f"{n:6d} {ra0 - R:19.0f} {rp0 - R:21.2f} {2*math.pi*math.sqrt(a**3/MU)/3600:13.2f}")
    while a * (1 + e) - R > 2000.0 and n < 400:
        rp_ant = a * (1 - e)
        a, e, dE, W = pasada(a, e)
        n += 1
        ra = a * (1 + e); rp = a * (1 - e)
        max_drp = max(max_drp, abs(rp - rp_ant))
        assert ra < prev_ra
        assert abs(dE - W) / abs(W) < 1e-3, (dE, W)
        prev_ra = ra
        if n % 5 == 0 or ra - R <= 2000.0:
            print(f"{n:6d} {ra - R:19.0f} {rp - R:21.2f} {2*math.pi*math.sqrt(a**3/MU)/3600:13.2f} {dE:24.5f} {W:30.5f}")
    vpf = math.sqrt(MU * (1 + e) / (a * (1 - e)))
    print(f"Pasadas necesarias para bajar el apoapsis a menos de 2000 km de altitud: {n}")
    print(f"Delta-v propulsivo equivalente (v_periapsis inicial - final) = {vp0 - vpf:.4f} km/s (v_p inicial {vp0:.4f}, final {vpf:.4f} km/s)")
    print(f"Maximo cambio del periapsis en una pasada = {max_drp:.3f} km")
    assert max_drp < 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
