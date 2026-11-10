#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C14. Estaciones terrestres: geometria de pasadas de un satelite en orbita circular sobre una Tierra esferica.
Constantes ILUSTRATIVAS (mu, radio medio, velocidad angular terrestre), no consultadas en esta clase. Orbita, estacion y tasa SINTETICAS."""
import math, sys

MU = 398600.4418      # km3/s2 (valor usual, ILUSTRATIVO, no consultado)
RE = 6371.0           # km (radio medio, ILUSTRATIVO)
WE = 7.2921159e-5     # rad/s (ILUSTRATIVO)

def periodo(alt):
    a = RE + alt
    return 2 * math.pi * math.sqrt(a ** 3 / MU)

def semi_angulo(alt, el_deg):
    """Angulo central maximo (rad) para que el satelite se vea por encima de la mascara de elevacion."""
    el = math.radians(el_deg)
    return math.acos(RE * math.cos(el) / (RE + alt)) - el

def duracion_cenital(alt, el_deg):
    n = 2 * math.pi / periodo(alt)
    return 2 * semi_angulo(alt, el_deg) / n

def elevacion(sat, est):
    """sat y est: vectores (km) en el mismo sistema; elevacion en grados sobre el horizonte local de la estacion."""
    rho = [sat[i] - est[i] for i in range(3)]
    d = math.sqrt(sum(x * x for x in rho))
    up = [x / RE for x in est]
    s = sum(rho[i] * up[i] for i in range(3)) / d
    return math.degrees(math.asin(max(-1.0, min(1.0, s))))

def posicion_sat(t, alt, inc_deg, fase0=0.0):
    a = RE + alt
    n = math.sqrt(MU / a ** 3)
    u = fase0 + n * t
    i = math.radians(inc_deg)
    return [a * math.cos(u), a * math.sin(u) * math.cos(i), a * math.sin(u) * math.sin(i)]

def posicion_est(t, lat_deg, lon_deg, we=WE):
    la, lo = math.radians(lat_deg), math.radians(lon_deg) + we * t
    return [RE * math.cos(la) * math.cos(lo), RE * math.cos(la) * math.sin(lo), RE * math.sin(la)]

def pasadas(alt, inc, lat, lon, mascara, dur=86400.0, paso=5.0, we=WE, fase0=0.0):
    res, en_pasada, ini, emax = [], False, 0.0, -90.0
    t = 0.0
    while t <= dur:
        el = elevacion(posicion_sat(t, alt, inc, fase0), posicion_est(t, lat, lon, we))
        if el >= mascara:
            if not en_pasada:
                en_pasada, ini, emax = True, t, el
            emax = max(emax, el)
        elif en_pasada:
            res.append((ini, t, emax))
            en_pasada = False
        t += paso
    if en_pasada:
        res.append((ini, dur, emax))
    return res

def calcular():
    R = {"alt": 600.0}
    R["T"] = periodo(600.0)
    R["cenital"] = {m: duracion_cenital(600.0, m) for m in (0, 5, 10, 20)}
    # verificacion: orbita ecuatorial, Tierra sin rotacion, estacion en el ecuador: pasada cenital
    n = 2 * math.pi / R["T"]
    fase0 = -semi_angulo(600.0, 10.0) - 0.5  # empieza antes de la pasada
    p = pasadas(600.0, 0.0, 0.0, 0.0, 10.0, dur=2000.0, paso=0.5, we=0.0, fase0=fase0)
    R["num"] = p[0][1] - p[0][0] if p else None
    R["ana"] = R["cenital"][10]
    R["emax_num"] = p[0][2] if p else None
    # un dia real: SSO 97.8 deg, estacion a 40 N, 10 grados de mascara
    ps = pasadas(600.0, 97.8, 40.0, 0.0, 10.0, dur=86400.0, paso=5.0)
    R["pasadas"] = ps
    R["contacto_total"] = sum(b - a for a, b, _ in ps)
    R["volumen_gbit"] = 2e6 * R["contacto_total"] / 1e9
    R["max_duracion"] = max(b - a for a, b, _ in ps)
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print(f"ILUSTRATIVO: mu = {MU} km3/s2, Re = {RE} km ; SINTETICO: orbita circular de {R['alt']:.0f} km")
    print(f"Periodo = {R['T']/60:.2f} min")
    print("Duracion de una pasada cenital segun la mascara de elevacion:")
    for m, d in R["cenital"].items():
        print(f"  mascara {m:2d} grados: {d/60:6.2f} min")
    print(f"Verificacion (orbita ecuatorial, sin rotacion, mascara 10): numerica = {R['num']:.1f} s ; analitica = {R['ana']:.1f} s")
    print(f"Un dia, SSO 97.8 grados, estacion 40 N 0 E, mascara 10 grados, paso 5 s: {len(R['pasadas'])} pasadas")
    for a, b, em in R["pasadas"]:
        print(f"  inicio {a/3600:6.3f} h ; duracion {(b-a)/60:5.2f} min ; elevacion maxima {em:5.1f} grados")
    print(f"Contacto total = {R['contacto_total']/60:.1f} min ; volumen a 2 Mbit/s = {R['volumen_gbit']:.2f} Gbit")
    assert abs(R["num"] - R["ana"]) < 1.0 and R["emax_num"] > 89.0
    assert R["max_duracion"] <= R["cenital"][10] + 10
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
