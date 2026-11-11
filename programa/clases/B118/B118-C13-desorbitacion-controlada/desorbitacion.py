"""B118-C13 · Desorbitación controlada.

Impulso tangencial en el apogeo de una órbita circular SINTÉTICA para bajar el perigeo; ángulo de trayectoria de reentrada (flight-path
angle) en la interfaz de 120 km y dispersión por error de impulso (Monte Carlo, semilla 118). Dos cuerpos, sin arrastre previo.
Unidades: km, km/s, m/s, grados, kg. Masa 800 kg e Isp 300 s ILUSTRATIVOS. GM = 398600.4418 km^3/s^2 (convencional, no consultado).
Interfaz atmosférica de 120 km: ILUSTRATIVA. Tolerancias: 1e-9 en la energía; 5 % linealización vs Monte Carlo.
"""
import math
import random
import sys

MU = 398600.4418
RE = 6378.137
G0 = 9.80665
H_IF = 120.0


def dv_para_perigeo(h0, h_p):
    r0, rp = RE + h0, RE + h_p
    a = 0.5 * (r0 + rp)
    va = math.sqrt(MU * (2 / r0 - 1 / a))
    return math.sqrt(MU / r0) - va  # km/s (frenado)


def gamma_interfaz(h0, dv):
    r0 = RE + h0
    va = math.sqrt(MU / r0) - dv
    h = r0 * va  # momento angular específico
    E = 0.5 * va ** 2 - MU / r0
    ri = RE + H_IF
    v = math.sqrt(2 * (E + MU / ri))
    cosg = h / (ri * v)
    return math.degrees(math.acos(max(-1.0, min(1.0, cosg)))), E, h, v


def masa_combustible(m0, dv_ms, isp):
    return m0 * (1 - math.exp(-dv_ms / (isp * G0)))


def compute():
    v = {}
    h0 = 500.0
    v["filas"] = []
    for hp in (300.0, 150.0, 100.0, 50.0, 0.0):
        dv = dv_para_perigeo(h0, hp)
        g = gamma_interfaz(h0, dv)[0] if hp < H_IF else float("nan")
        v["filas"].append((hp, dv * 1000.0, g, masa_combustible(800.0, dv * 1000.0, 300.0)))
    # controlada: perigeo a 0 km (dentro de la Tierra) da gamma ~ 1.5-2 grados; compara con vida natural
    dv_obj = dv_para_perigeo(h0, 0.0)
    v["dv_obj"] = dv_obj * 1000.0
    g0, E, h, vi = gamma_interfaz(h0, dv_obj)
    v["g0"] = g0
    v["v_if"] = vi
    # conservación: energía en la interfaz
    a_el = -MU / (2 * E)
    e_el = math.sqrt(1 + 2 * E * h * h / MU ** 2)
    v["E_chk"] = a_el * (1 - e_el) - (RE + 0.0)  # el perigeo recuperado de (E, h) debe ser el objetivo
    # error de impulso
    rng = random.Random(118)
    sig = 0.5e-3  # km/s = 0.5 m/s
    gs = []
    for _ in range(4000):
        gs.append(gamma_interfaz(h0, dv_obj + rng.gauss(0, sig))[0])
    m = sum(gs) / len(gs)
    sd = math.sqrt(sum((x - m) ** 2 for x in gs) / (len(gs) - 1))
    v["g_media"], v["g_sd"] = m, sd
    eps = 1e-6
    v["dgdv"] = (gamma_interfaz(h0, dv_obj + eps)[0] - gamma_interfaz(h0, dv_obj - eps)[0]) / (2 * eps)  # grados por km/s
    v["g_sd_lin"] = abs(v["dgdv"]) * sig
    # desplazamiento a lo largo de la traza del punto de impacto por un error de gamma (aproximación geométrica)
    v["dx_km_por_grado"] = None
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Satelite SINTETICO de 800 kg, orbita circular de 500 km; Isp 300 s e interfaz de 120 km ILUSTRATIVOS; dos cuerpos.")
    v = compute()
    print(" perigeo objetivo [km]   dv [m/s]   gamma interfaz [deg]   combustible [kg]")
    for hp, dv, g, m in v["filas"]:
        gs = "     -      " if math.isnan(g) else f"{g:10.3f}"
        print(f" {hp:18.0f}   {dv:8.2f}   {gs:>14s}   {m:12.2f}")
    print(f"Objetivo (perigeo 0 km): dv = {v['dv_obj']:.2f} m/s; gamma = {v['g0']:.3f} deg; v en la interfaz = {v['v_if']:.4f} km/s")
    print(f"Perigeo recuperado desde (E, h) menos el objetivo: {v['E_chk']:.2e} km")
    print(f"Con error de impulso de 0.5 m/s (4000 muestras): gamma = {v['g_media']:.3f} +- {v['g_sd']:.3f} deg; linealizacion {v['g_sd_lin']:.3f} deg")
    assert abs(v["E_chk"]) < 1e-6
    assert abs(v["g_sd"] - v["g_sd_lin"]) / v["g_sd_lin"] < 0.05
    assert v["filas"][-1][2] > v["filas"][3][2] > v["filas"][2][2]
    print("Pruebas superadas (perigeo recuperado a 1e-6 km; sigma de gamma por Monte Carlo = linealizacion a 5 %).")


if __name__ == "__main__":
    main()
