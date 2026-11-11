"""B118-C01 · Población de objetos orbitales.

Datos: (a) cifras de la ESA Space Environment Report 2025 (página consultada el 2026-11-11);
(b) una población SINTÉTICA de 5000 objetos en LEO (semilla 118), no observada.
Unidades: km, objetos/km^3. Sistema de referencia: altitud sobre el radio ecuatorial 6378,137 km.
Tolerancia de las pruebas: 1e-9 relativa para identidades algebraicas.
"""
import math
import random
import sys

RE = 6378.137  # km, radio ecuatorial (valor convencional, no consultado en esta clase)
ESA_10CM = 50_000      # objetos > 10 cm ("más de 50 000", ESA 2025)
ESA_1CM = 1_200_000    # objetos > 1 cm ("más de 1,2 millones", ESA 2025)
ESA_SEGUIDOS = 40_000  # objetos seguidos ("unos 40 000")
ESA_ACTIVOS = 11_000   # cargas útiles activas ("unas 11 000")


def exponente(n_a, d_a, n_b, d_b):
    """Pendiente b de N(>d) = k d^-b a partir de dos puntos."""
    return math.log(n_b / n_a) / math.log(d_a / d_b)


def poblacion_sintetica(n=5000, semilla=118):
    rng = random.Random(semilla)
    picos = [(550.0, 40.0, 0.45), (800.0, 30.0, 0.30), (1000.0, 60.0, 0.25)]
    alturas = []
    while len(alturas) < n:
        u = rng.random()
        acum = 0.0
        for mu, sg, w in picos:
            acum += w
            if u <= acum:
                break
        h = rng.gauss(mu, sg)
        if 300.0 <= h < 2000.0:
            alturas.append(h)
    return alturas


def densidad_por_capa(alturas, paso=100.0, h0=300.0, h1=2000.0):
    nb = int(round((h1 - h0) / paso))
    cuentas = [0] * nb
    for h in alturas:
        cuentas[min(int((h - h0) / paso), nb - 1)] += 1
    filas = []
    for k, c in enumerate(cuentas):
        ha, hb = h0 + k * paso, h0 + (k + 1) * paso
        vol = 4.0 / 3.0 * math.pi * ((RE + hb) ** 3 - (RE + ha) ** 3)  # km^3
        filas.append((ha, hb, c, c / vol))
    return filas


def compute():
    v = {}
    b = exponente(ESA_10CM, 10.0, ESA_1CM, 1.0)
    v["b"] = b
    v["n_1mm"] = ESA_1CM * 10.0 ** b  # extrapolación ilustrativa
    v["frac_activos"] = ESA_ACTIVOS / ESA_SEGUIDOS
    alturas = poblacion_sintetica()
    v["n"] = len(alturas)
    filas = densidad_por_capa(alturas)
    v["filas"] = filas
    k = max(range(len(filas)), key=lambda i: filas[i][3])
    v["pico"] = filas[k]
    v["suma_vol"] = sum(f[3] * (4.0 / 3.0 * math.pi * ((RE + f[1]) ** 3 - (RE + f[0]) ** 3)) for f in filas)
    v["frac_bajo_600"] = sum(1 for h in alturas if h < 600.0) / len(alturas)
    v["h_media"] = sum(alturas) / len(alturas)
    # comprobación: la ley de potencias reproduce los dos puntos
    v["n_10_pred"] = ESA_1CM * (10.0 / 1.0) ** (-b)
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Cifras ESA 2025 (consultadas): >10 cm: 50000; >1 cm: 1200000; seguidos: ~40000; activos: ~11000")
    print("Poblacion LEO SINTETICA (semilla 118); no es observada.")
    v = compute()
    print(f"Pendiente b de N(>d) = k d^-b entre 1 cm y 10 cm: {v['b']:.4f}")
    print(f"Extrapolacion ILUSTRATIVA a >1 mm: {v['n_1mm']:.3e} objetos (no es una cifra de la ESA)")
    print(f"Fraccion de activos entre los seguidos: {v['frac_activos']:.3f}")
    print(f"Objetos sinteticos: {v['n']}; altura media {v['h_media']:.1f} km; fraccion bajo 600 km: {v['frac_bajo_600']:.3f}")
    print(" capa [km]        N    densidad [1e-9 /km^3]")
    for ha, hb, c, d in v["filas"]:
        print(f" {ha:6.0f}-{hb:5.0f}  {c:6d}   {d * 1e9:10.3f}")
    ha, hb, c, d = v["pico"]
    print(f"Capa de mayor densidad: {ha:.0f}-{hb:.0f} km ({d * 1e9:.3f} e-9 /km^3)")
    assert abs(v["suma_vol"] - v["n"]) < 1e-6 * v["n"], "densidad x volumen debe devolver N"
    assert abs(v["n_10_pred"] - ESA_10CM) < 1e-9 * ESA_10CM, "la ley debe reproducir el punto de 10 cm"
    print("Pruebas superadas (densidad x volumen = N; ley reproduce el punto de 10 cm).")


if __name__ == "__main__":
    main()
