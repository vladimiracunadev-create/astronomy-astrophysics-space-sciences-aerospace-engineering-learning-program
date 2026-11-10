#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C11: ventanas de lanzamiento para entrar en un plano orbital objetivo.

Datos consultados (2026-11-10): periodo de rotacion sideral de la Tierra 23.9345 h y radio ecuatorial 6378.137 km (NASA/NSSDC Earth Fact Sheet).
SINTETICOS / ILUSTRATIVOS: sitio de lanzamiento a latitud geocentrica 28.5 grados (no corresponde a ninguna base real), plano objetivo con inclinacion 51.6 grados
y ascension recta del nodo ascendente (RAAN) 120 grados, ambos inventados; angulos en grados salvo indicacion. Tierra esferica y sin precesion ni J2.
Sistema de referencia: inercial ecuatorial (eje x hacia el equinoccio, z hacia el polo); theta = tiempo sideral local en grados (angulo entre x y el meridiano del sitio).
Modelo: el sitio esta en el plano cuando r_s . n = 0 con n = (sin O sin i, -cos O sin i, cos i); acimut de lanzamiento sin(Az) = cos i / cos(phi).
Segunda via: se construye la velocidad orbital como n x r_s y se mide su acimut en el horizonte local; ademas se lanza con retraso dt y mismo acimut y se mide la
ascension recta del nodo alcanzada.
Tolerancias: producto escalar r_s.n < 1e-12; acimut por dos vias 1e-9 grados.
"""
import math, platform

PHI, INC, RAAN = 28.5, 51.6, 120.0
T_SID_H, R_EQ = 23.9345, 6378.137e3
OMEGA = 2 * math.pi / (T_SID_H * 3600.0)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def unit(a):
    n = math.sqrt(dot(a, a))
    return tuple(x / n for x in a)


def normal(inc, raan):
    i, o = math.radians(inc), math.radians(raan)
    return (math.sin(o) * math.sin(i), -math.cos(o) * math.sin(i), math.cos(i))


def sitio(phi, theta):
    p, t = math.radians(phi), math.radians(theta)
    return (math.cos(p) * math.cos(t), math.cos(p) * math.sin(t), math.sin(p))


def acimut(r, v, phi, theta):
    p, t = math.radians(phi), math.radians(theta)
    este = (-math.sin(t), math.cos(t), 0.0)
    norte = (-math.sin(p) * math.cos(t), -math.sin(p) * math.sin(t), math.cos(p))
    return math.degrees(math.atan2(dot(v, este), dot(v, norte))) % 360.0


def plano_de(r, az, phi, theta):
    p, t, a = math.radians(phi), math.radians(theta), math.radians(az)
    este = (-math.sin(t), math.cos(t), 0.0)
    norte = (-math.sin(p) * math.cos(t), -math.sin(p) * math.sin(t), math.cos(p))
    v = tuple(math.cos(a) * n + math.sin(a) * e for n, e in zip(norte, este))
    n = unit(cross(r, v))
    inc = math.degrees(math.acos(n[2]))
    raan = math.degrees(math.atan2(n[0], -n[1])) % 360.0
    return inc, raan


def calcular():
    res = {}
    n = normal(INC, RAAN)
    u0 = math.degrees(math.asin(math.sin(math.radians(PHI)) / math.sin(math.radians(INC))))
    az_f = math.degrees(math.asin(math.cos(math.radians(INC)) / math.cos(math.radians(PHI))))
    ventanas = []
    for nombre, u, az_ana in (("ascendente (hacia el norte)", u0, az_f), ("descendente (hacia el sur)", 180.0 - u0, 180.0 - az_f)):
        ur = math.radians(u)
        d_alpha = math.degrees(math.atan2(math.cos(math.radians(INC)) * math.sin(ur), math.cos(ur)))
        theta = (RAAN + d_alpha) % 360.0
        r = sitio(PHI, theta)
        v = cross(n, r)
        az_num = acimut(r, unit(v), PHI, theta)
        ventanas.append(dict(nombre=nombre, theta=theta, dot=abs(dot(r, n)), az_ana=az_ana, az_num=az_num, err_az=abs(az_num - az_ana)))
    res["v"] = ventanas
    res["dif_theta"] = (ventanas[1]["theta"] - ventanas[0]["theta"]) % 360.0
    res["dif_t_min"] = res["dif_theta"] / math.degrees(OMEGA) / 60.0
    res["omega_deg_h"] = math.degrees(OMEGA) * 3600.0
    t_sid_s = T_SID_H * 3600.0
    res["desfase_diario_s"] = 86400.0 - t_sid_s
    res["v_rot"] = OMEGA * R_EQ * math.cos(math.radians(PHI))
    res["ganancia_v"] = res["v_rot"] * math.sin(math.radians(ventanas[0]["az_ana"]))
    # retraso con el mismo acimut: cambio del nodo alcanzado
    w = ventanas[0]
    r0 = sitio(PHI, w["theta"])
    filas = []
    for dt_min in (0.0, 1.0, 5.0, 10.0):
        th = w["theta"] + math.degrees(OMEGA) * dt_min * 60.0
        i2, o2 = plano_de(sitio(PHI, th), w["az_ana"], PHI, th)
        filas.append((dt_min, i2, o2, (o2 - RAAN + 180) % 360 - 180))
    res["retraso"] = filas
    return res


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Sitio SINTETICO a {PHI} grados de latitud; plano objetivo i = {INC} grados, RAAN = {RAAN} grados (inventados)")
    print(f"Velocidad angular de la Tierra = {r['omega_deg_h']:.4f} grados/h (T sideral {T_SID_H} h)")
    for w in r["v"]:
        print(f"Ventana {w['nombre']}: tiempo sideral local = {w['theta']:.4f} grados; |r.n| = {w['dot']:.1e}; acimut analitico = {w['az_ana']:.4f}; por velocidad = {w['az_num']:.4f}")
    print(f"Separacion entre las dos ventanas = {r['dif_theta']:.3f} grados = {r['dif_t_min']:.2f} min sidereos")
    print(f"Desfase diario de la ventana = {r['desfase_diario_s']:.1f} s (24 h - T sideral)")
    print(f"Velocidad de rotacion en el sitio = {r['v_rot']:.1f} m/s; ganancia hacia el acimut de lanzamiento = {r['ganancia_v']:.1f} m/s")
    print("Retraso con el mismo acimut -> plano alcanzado:")
    for dt, i2, o2, d in r["retraso"]:
        print(f"  {dt:5.1f} min: i = {i2:.4f} grados, RAAN = {o2:.4f} grados (error de RAAN = {d:+.4f} grados)")
    for w in r["v"]:
        assert w["dot"] < 1e-12 and w["err_az"] < 1e-9
    assert abs(r["retraso"][0][3]) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
