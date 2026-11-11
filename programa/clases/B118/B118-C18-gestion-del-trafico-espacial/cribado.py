"""B118-C18 · Gestión del tráfico espacial.

Cribado en cascada de un catálogo SINTÉTICO de 400 objetos (semilla 118): filtro de apsis (cáscaras radiales disjuntas con margen d)
y verificación de que el filtro es conservador, es decir, que ningún par rechazado se acerca a menos de d (propagación kepleriana en
instantes aleatorios).
Unidades: km, segundos. Sistema: inercial geocéntrico. GM = 398600.4418 km^3/s^2 (convencional, no consultado). Margen d = 20 km (ILUSTRATIVO).
Tolerancia: la distancia mínima muestreada debe ser >= la separación radial de las cáscaras menos 1e-6 km.
"""
import math
import random
import sys

MU = 398600.4418
RE = 6378.137


def catalogo(n=400, semilla=118):
    rng = random.Random(semilla)
    out = []
    for _ in range(n):
        rp = RE + rng.uniform(400.0, 1500.0)
        if rng.random() < 0.3:
            ra = rp + rng.uniform(0.0, 3000.0)  # excéntricas
        else:
            ra = rp + rng.uniform(0.0, 40.0)
        a = 0.5 * (rp + ra)
        e = (ra - rp) / (ra + rp)
        out.append(dict(a=a, e=e, i=math.radians(rng.uniform(0, 100)), O=rng.uniform(0, 2 * math.pi),
                        w=rng.uniform(0, 2 * math.pi), M0=rng.uniform(0, 2 * math.pi), rp=rp, ra=ra))
    return out


def kepler_E(M, e):
    E = M if e < 0.8 else math.pi
    for _ in range(50):
        d = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        E -= d
        if abs(d) < 1e-13:
            break
    return E


def pos(o, t):
    n = math.sqrt(MU / o["a"] ** 3)
    M = (o["M0"] + n * t) % (2 * math.pi)
    E = kepler_E(M, o["e"])
    xp, yp = o["a"] * (math.cos(E) - o["e"]), o["a"] * math.sqrt(1 - o["e"] ** 2) * math.sin(E)
    cw, sw, ci, si, co, so = math.cos(o["w"]), math.sin(o["w"]), math.cos(o["i"]), math.sin(o["i"]), math.cos(o["O"]), math.sin(o["O"])
    x = (co * cw - so * sw * ci) * xp + (-co * sw - so * cw * ci) * yp
    y = (so * cw + co * sw * ci) * xp + (-so * sw + co * cw * ci) * yp
    z = (sw * si) * xp + (cw * si) * yp
    return x, y, z


def separacion_apsis(p, q):
    """Separación radial mínima entre las cáscaras [rp, ra]; 0 si se solapan."""
    return max(0.0, p["rp"] - q["ra"], q["rp"] - p["ra"])


def compute(d=20.0):
    v = {}
    cat = catalogo()
    n = len(cat)
    v["n"], v["pares"] = n, n * (n - 1) // 2
    rech, pasan = [], 0
    for i in range(n):
        for j in range(i + 1, n):
            g = separacion_apsis(cat[i], cat[j])
            if g > d:
                rech.append((i, j, g))
            else:
                pasan += 1
    v["pasan"], v["rechazados"] = pasan, len(rech)
    v["frac_pasan"] = pasan / v["pares"]
    rng = random.Random(1180)
    muestra = rng.sample(rech, 150)
    peor = 1e99
    for i, j, g in muestra:
        for _ in range(300):
            t = rng.uniform(0, 86400.0 * 3)
            p, q = pos(cat[i], t), pos(cat[j], t)
            dist = math.dist(p, q)
            peor = min(peor, dist - g)
    v["peor_exceso"] = peor  # >= 0 si el filtro es conservador
    v["n_muestra"] = len(muestra)
    # trabajo: con el filtro, pares a vigilar; tiempo de cribado ahorrado
    v["ahorro"] = 1.0 - v["frac_pasan"]
    # escalado a un catálogo de 40 000 objetos: pares totales y fracción retenida (misma distribución, ILUSTRATIVO)
    v["pares_40k"] = 40_000 * 39_999 // 2
    v["retenidos_40k"] = v["frac_pasan"] * v["pares_40k"]
    # pares con ambos casi circulares y cáscara solapada: son los que dominan el filtrado
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Catalogo SINTETICO de 400 objetos (semilla 118); margen del filtro de apsis d = 20 km (ILUSTRATIVO).")
    v = compute()
    print(f"Pares totales: {v['pares']}; pasan el filtro: {v['pasan']} ({v['frac_pasan']:.3f}); rechazados: {v['rechazados']}")
    print(f"Verificacion: {v['n_muestra']} pares rechazados x 300 instantes aleatorios; peor (distancia - separacion radial) = {v['peor_exceso']:.3f} km (>= 0 si es conservador)")
    print(f"Con la misma fraccion en 40000 objetos: {v['pares_40k']:.3e} pares -> {v['retenidos_40k']:.3e} retenidos para el cribado fino")
    assert v["peor_exceso"] > -1e-6
    assert 0.0 < v["frac_pasan"] < 1.0
    print("Pruebas superadas (el filtro de apsis no pierde ningun par muestreado).")


if __name__ == "__main__":
    main()
