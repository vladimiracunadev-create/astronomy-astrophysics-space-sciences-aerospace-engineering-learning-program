"""B118-C02 · Catálogos de objetos espaciales.

Datos SINTÉTICOS (semilla 118): catálogo de 400 objetos con elementos (a, i, RAAN), pistas con ruido y 40 objetos no catalogados.
Consultado (2026-11-11, página de documentación de Space-Track): una TLE tiene dos líneas de 69 caracteres, el último es un
checksum módulo 10; Alpha-5 sustituye el primer dígito por una letra (A=10, sin I ni O) hasta el número 339 999.
Unidades: km, grados. Tolerancia de asociación: puerta chi-cuadrado de 3 g.l. al 99 % (11,345).
"""
import math
import random
import sys

LETRAS = "ABCDEFGH" + "JKLMN" + "PQRSTUVWXYZ"  # A=10 ... sin I ni O
assert len(LETRAS) == 24


def alpha5_codificar(n):
    if not 0 <= n <= 339_999:
        raise ValueError("fuera de rango Alpha-5")
    if n < 100_000:
        return f"{n:05d}"
    g, resto = divmod(n, 10_000)
    return LETRAS[g - 10] + f"{resto:04d}"


def alpha5_decodificar(s):
    if s[0].isdigit():
        return int(s)
    return (LETRAS.index(s[0]) + 10) * 10_000 + int(s[1:])


def checksum(linea68):
    return sum(int(c) if c.isdigit() else (1 if c == "-" else 0) for c in linea68) % 10


def tle_sintetica(numero=99999):
    # línea 1 sintética (campos en cero) con la columna de longitud fija de 68 + checksum
    l1 = f"1 {numero:05d}U 24999A   24001.00000000  .00000000  00000-0  00000-0 0  999"
    l1 = l1[:68]
    return l1 + str(checksum(l1))


def asociacion(semilla=118, n_cat=400, n_pistas_cat=360, n_desc=40):
    rng = random.Random(semilla)
    cat = [(rng.uniform(6700, 7500), rng.uniform(30, 100), rng.uniform(0, 360)) for _ in range(n_cat)]
    sig = (2.0, 0.05, 0.1)  # sigma de a [km], i [deg], RAAN [deg]
    pistas = []
    for k in rng.sample(range(n_cat), n_pistas_cat):
        a, i, o = cat[k]
        pistas.append((k, (a + rng.gauss(0, sig[0]), i + rng.gauss(0, sig[1]), o + rng.gauss(0, sig[2]))))
    for _ in range(n_desc):
        pistas.append((-1, (rng.uniform(6700, 7500), rng.uniform(30, 100), rng.uniform(0, 360))))
    ok = mal = sin_par = 0
    for verdad, p in pistas:
        mejor, md = None, 1e99
        for k, c in enumerate(cat):
            d2 = sum(((p[j] - c[j]) / sig[j]) ** 2 for j in range(3))
            if d2 < md:
                mejor, md = k, d2
        if md <= 11.345:
            if mejor == verdad:
                ok += 1
            else:
                mal += 1
        else:
            sin_par += 1
    return ok, mal, sin_par, len(pistas)


def compute():
    v = {}
    v["casos"] = [(n, alpha5_codificar(n)) for n in (99_999, 100_000, 123_456, 339_999)]
    v["tle"] = tle_sintetica()
    v["ok"], v["mal"], v["sin_par"], v["n_pistas"] = asociacion()
    return v


def main():
    print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
    print("Catalogo y pistas SINTETICOS (semilla 118); formatos segun Space-Track (consultado); no son datos reales.")
    v = compute()
    for n, s in v["casos"]:
        print(f"Alpha-5: {n:6d} -> {s} -> {alpha5_decodificar(s)}")
        assert alpha5_decodificar(s) == n
    for n in range(0, 339_999, 997):
        assert alpha5_decodificar(alpha5_codificar(n)) == n
    print("TLE sintetica L1:", v["tle"], "| longitud", len(v["tle"]))
    assert len(v["tle"]) == 69 and checksum(v["tle"][:68]) == int(v["tle"][68])
    try:
        alpha5_codificar(340_000)
        raise SystemExit("debia fallar")
    except ValueError:
        print("340000 rechazado: Alpha-5 termina en 339999")
    print(f"Asociacion de {v['n_pistas']} pistas (360 catalogadas + 40 no catalogadas), puerta 11.345:")
    print(f"  correctas {v['ok']}, equivocadas {v['mal']}, sin pareja {v['sin_par']}")
    assert v["ok"] + v["mal"] + v["sin_par"] == v["n_pistas"]
    print("Pruebas superadas (ida y vuelta Alpha-5, checksum, conteos).")


if __name__ == "__main__":
    main()
