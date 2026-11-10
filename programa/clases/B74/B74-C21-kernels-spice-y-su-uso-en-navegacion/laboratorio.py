#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C21: meta-kernels SPICE (analisis didactico), prioridad de carga y segmentos tipo Chebyshev.

NO usa SPICE ni lee kernels reales. Todo SINTETICO: se escribe en un directorio temporal un meta-kernel de texto con la estructura descrita por NAIF
(identificador KPL/MK, KERNELS_TO_LOAD, PATH_VALUES y PATH_SYMBOLS; consultada el 2026-11-10) y archivos vacios con nombres INVENTADOS, se analiza con un lector minimo
(didactico, no es el analizador de NAIF) y se comprueba: (1) que los archivos existen, (2) que el kernel de segundos intercalares (LSK) y el de reloj de nave (SCLK) se
cargan antes que los SPK, (3) que ante dos SPK que cubren el mismo cuerpo y tiempo gana el cargado despues (regla de NAIF), y (4) se calcula la cobertura efectiva y sus huecos.
Segunda parte: un 'segmento' de posicion representado por polinomios de Chebyshev (idea del tipo 2 de SPK) para una trayectoria sintetica (arco de Kepler de 4 h) con 1, 2 y 4
registros de 1 h; se mide el error de interpolacion en 1000 instantes frente a la funcion exacta.
Tolerancias: con 4 registros de 1 h y grado 12 el error debe ser < 0.1 m; la prioridad se resuelve por orden de carga.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, os, platform, re, sys, tempfile
import numpy as np

META = """KPL/MK

Meta-kernel SINTETICO para la clase B74-C21 (nombres inventados)

\\begindata
PATH_VALUES  = ( '{base}' )
PATH_SYMBOLS = ( 'KERNELS' )
KERNELS_TO_LOAD = (
   '$KERNELS/lsk_sintetico.tls',
   '$KERNELS/sclk_sintetico.tsc',
   '$KERNELS/pck_sintetico.tpc',
   '$KERNELS/spk_planetas_sint.bsp',
   '$KERNELS/spk_nave_v1_sint.bsp',
   '$KERNELS/spk_nave_v2_sint.bsp'
)
\\begintext
"""

# cobertura SINTETICA en segundos desde una epoca arbitraria
COBERTURA = {
    "spk_planetas_sint.bsp": [("PLANETA", 0, 1000)],
    "spk_nave_v1_sint.bsp": [("NAVE", 0, 600)],
    "spk_nave_v2_sint.bsp": [("NAVE", 400, 900)],
}


def analiza(texto):
    datos = re.search(r"\\begindata(.*?)\\begintext", texto, re.S).group(1)
    pv = re.search(r"PATH_VALUES\s*=\s*\(\s*'([^']*)'", datos).group(1)
    ps = re.search(r"PATH_SYMBOLS\s*=\s*\(\s*'([^']*)'", datos).group(1)
    lista = re.search(r"KERNELS_TO_LOAD\s*=\s*\((.*?)\)", datos, re.S).group(1)
    nombres = re.findall(r"'([^']*)'", lista)
    return [n.replace("$" + ps, pv) for n in nombres]


def cobertura_efectiva(orden, cuerpo, t0, t1):
    """Para cada segundo entero, devuelve el kernel que gana (el cargado despues). Resume tramos."""
    tramos = []
    previo = None
    ini = t0
    for t in range(t0, t1 + 1):
        ganador = None
        for k in orden:
            nom = os.path.basename(k)
            for (c, a, b) in COBERTURA.get(nom, []):
                if c == cuerpo and a <= t <= b:
                    ganador = nom
        if ganador != previo:
            if t > t0:
                tramos.append((previo, ini, t - 1))
            ini, previo = t, ganador
    tramos.append((previo, ini, t1))
    return tramos


def chebyshev_ajuste(f, a, b, grado):
    n = grado + 1
    k = np.arange(n)
    x = np.cos(np.pi * (k + 0.5) / n)
    t = 0.5 * (b - a) * x + 0.5 * (b + a)
    coef = np.polynomial.chebyshev.chebfit(x, f(t), grado)
    return coef


def main():
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (meta-kernel y arco SINTETICOS; NO se usa SPICE)"]
    res = {}
    with tempfile.TemporaryDirectory() as base:
        base = base.replace("\\", "/")
        texto = META.format(base=base)
        lista = analiza(texto)
        for k in lista:
            open(k, "w").close()
        existen = all(os.path.exists(k) for k in lista)
        nomb = [os.path.basename(k) for k in lista]
        out.append("Orden de carga resuelto desde el meta-kernel:")
        for i, n in enumerate(nomb, 1):
            out.append(f"  {i}. {n}")
        i_lsk = nomb.index("lsk_sintetico.tls"); i_sclk = nomb.index("sclk_sintetico.tsc")
        i_spk = min(i for i, n in enumerate(nomb) if n.endswith(".bsp"))
        orden_ok = i_lsk < i_spk and i_sclk < i_spk
        out.append(f"Archivos existentes: {existen} ; LSK y SCLK antes que los SPK: {orden_ok}")
        res.update(n=len(nomb), existen=int(existen), orden_ok=int(orden_ok))
        tramos = cobertura_efectiva(lista, "NAVE", 0, 1000)
        out.append("Cobertura efectiva de NAVE (0-1000 s), gana el cargado despues:")
        for (g, a, b) in tramos:
            out.append(f"  {a:5d}-{b:5d} s : {g if g else 'SIN COBERTURA (hueco)'}")
        huecos = [(a, b) for (g, a, b) in tramos if g is None]
        res["huecos"] = len(huecos)
        res["hueco_ini"] = huecos[0][0] if huecos else -1
        gana_v2 = [g for (g, a, b) in tramos if a <= 500 <= b][0]
        out.append(f"En t = 500 s (solapamiento) los datos vienen de {gana_v2}")
        res["gana500"] = gana_v2
    # Chebyshev
    mu = 3.986004e14
    a_, e_ = 7.2e6, 0.01
    n_ = math.sqrt(mu / a_**3)
    def pos(t):
        M = n_ * t; E = M
        for _ in range(50): E = E - (E - e_ * np.sin(E) - M) / (1 - e_ * np.cos(E))
        return a_ * (np.cos(E) - e_), a_ * math.sqrt(1 - e_**2) * np.sin(E)
    out.append("Segmento tipo Chebyshev de una trayectoria de 4 h (sintetica): error maximo de la posicion en 1000 instantes")
    out.append("registros   grado    error max [m]")
    ok = True
    Tm = 4 * 3600.0
    ts = np.linspace(0, Tm, 1000)
    for nreg, grado in ((1, 12), (2, 12), (4, 12), (4, 6)):
        w = Tm / nreg; err = 0.0
        cf = [(chebyshev_ajuste(lambda t: pos(t)[0], r * w, (r + 1) * w, grado), chebyshev_ajuste(lambda t: pos(t)[1], r * w, (r + 1) * w, grado)) for r in range(nreg)]
        for t in ts:
            r = min(int(t // w), nreg - 1); a, b = r * w, (r + 1) * w
            x = (2 * t - (a + b)) / (b - a)
            ex = np.polynomial.chebyshev.chebval(x, cf[r][0]); ey = np.polynomial.chebyshev.chebval(x, cf[r][1])
            px, py = pos(t)
            err = max(err, math.hypot(ex - px, ey - py))
        out.append(f"{nreg:5d}   {grado:8d}   {err:12.3e}")
        res[f"ch{nreg}_{grado}"] = float(err)
        if grado == 12 and nreg == 4:
            ok &= err < 0.1
    ok &= existen and orden_ok and res["gana500"] == "spk_nave_v2_sint.bsp" and res["huecos"] == 1
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
