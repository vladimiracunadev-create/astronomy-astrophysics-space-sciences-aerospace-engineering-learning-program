#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C12: radar planetario: ancho Doppler de un asteroide en rotacion, resolucion en distancia y ley 1/R^4.

Datos: asteroide SINTETICO esferico de D = 500 m, periodo de rotacion P = 4 h, latitud subradar 30 deg; longitud de onda 0.035 m y ancho de banda de transmision 2 MHz: valores ILUSTRATIVOS (no se
consultaron especificaciones de ningun radar; la pagina de radar de CNEOS dio 404). c = 299792458 m/s exacto (SI).
Modelo: la velocidad en la linea de vision de un punto del cuerpo es v = (omega z x r) . k con k hacia el radar; el desplazamiento Doppler es 2 v / lambda y el ancho total se obtiene de los extremos
sobre una malla de 720 x 360 puntos de la mitad visible; analitico B = 4 pi D cos(delta) / (lambda P). Resolucion en distancia = c / (2 B_tx). Ecuacion del radar: SNR ~ D^2 / R^4 (seccion eficaz ~ D^2).
Supuestos: esfera lisa, sin retardo de luz, sin ruido; el eco real depende de la superficie. Validez: ilustrativa.
Tolerancia: ancho Doppler numerico frente al analitico 0.3 %; cocientes de SNR exactos con 1e-12.
"""
import math, platform

C = 299792458.0

def ancho_analitico(D, P, lam, delta_deg):
    return 4 * math.pi * D * math.cos(math.radians(delta_deg)) / (lam * P)

def ancho_numerico(D, P, lam, delta_deg, nlon=720, nlat=360):
    R, w, d = D / 2, 2 * math.pi / P, math.radians(delta_deg)
    k = (math.cos(d), 0.0, math.sin(d))
    vmin, vmax = 1e9, -1e9
    for i in range(nlon):
        lon = 2 * math.pi * i / nlon
        for j in range(nlat + 1):
            lat = math.pi * j / nlat - math.pi / 2
            x, y, z = R * math.cos(lat) * math.cos(lon), R * math.cos(lat) * math.sin(lon), R * math.sin(lat)
            if x * k[0] + y * k[1] + z * k[2] < -1e-9:
                continue
            v = w * (-y * k[0] + x * k[1])   # (z x r) . k con k_y = 0
            f = 2 * v / lam
            vmin, vmax = min(vmin, f), max(vmax, f)
    return vmax - vmin

def snr_rel(D, R_au):
    return D ** 2 / R_au ** 4

def calcular():
    D, P, lam, dl = 500.0, 4 * 3600.0, 0.035, 30.0
    Ba, Bn = ancho_analitico(D, P, lam, dl), ancho_numerico(D, P, lam, dl)
    B0 = ancho_analitico(D, P, lam, 0.0)
    res = C / (2 * 2e6)
    return {"Ba": Ba, "Bn": Bn, "B0": B0, "res": res, "npix": D / res, "q_R": snr_rel(500.0, 0.02) / snr_rel(500.0, 0.04),
            "q_D": snr_rel(500.0, 0.02) / snr_rel(250.0, 0.02)}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Ancho Doppler (D = 500 m, P = 4 h, lambda = 3.5 cm, latitud subradar 30 deg): analitico = %.3f Hz ; numerico = %.3f Hz ; diferencia = %.3f %%" % (r["Ba"], r["Bn"], 100 * abs(r["Bn"] / r["Ba"] - 1)))
    print("Ancho Doppler con latitud subradar 0 deg = %.3f Hz (cociente 30 deg / 0 deg = %.4f ; cos 30 = %.4f)" % (r["B0"], r["Ba"] / r["B0"], math.cos(math.radians(30))))
    print("Resolucion en distancia con 2 MHz = %.1f m ; elementos de distancia a lo largo de D = %.1f" % (r["res"], r["npix"]))
    print("SNR relativa: R de 0.02 a 0.04 au -> factor %.1f ; D de 250 a 500 m -> factor %.1f" % (r["q_R"], r["q_D"]))
    assert abs(r["Bn"] / r["Ba"] - 1) < 0.003
    assert abs(r["q_R"] - 16.0) < 1e-12 and abs(r["q_D"] - 4.0) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
