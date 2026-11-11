"""B132-C06: informe de un sitio arqueoastronomico SINTETICO.

Propaga incertidumbres (lineal y Monte Carlo, semilla fija), compara con objetivos solares y lunares con
correccion por el numero de objetivos y verifica la estructura de un informe.
Formulas esfericas estandar (no consultadas). Inclinacion de la orbita lunar 5,145 grados: valor estandar,
no consultado. Sitio, estructuras y mediciones SINTETICOS. Unidades: grados.
"""
import math
import random
import re
import sys

SEMILLA = 20261116
LAT = 40.0          # grados N, SINTETICA
EPS = 23.9          # grados, oblicuidad ilustrativa de la epoca del sitio sintetico
INCL_LUNAR = 5.145  # grados (estandar)
D_MAG, S_D_MAG = 1.5, 0.5   # declinacion magnetica SINTETICA y su incertidumbre (grados)

# estructuras: id, azimut magnetico medido (brujula), sigma instrumento, altura aparente del horizonte, sigma
ESTRUCTURAS = [
    ("E1", 52.0, 0.5, 1.0, 0.3),
    ("E2", 125.5, 0.5, 0.5, 0.3),
    ("E3", 90.8, 0.5, 0.3, 0.2),
    ("E4", 71.0, 0.5, 2.0, 0.4),
    ("E5", 300.0, 0.5, 1.5, 0.3),
]


def refraccion(h_ap):
    return (1.0 / math.tan(math.radians(h_ap + 7.31 / (h_ap + 4.4)))) / 60.0


def dec(az, h_ap):
    h = h_ap - refraccion(max(h_ap, 0.0)) if h_ap >= 0 else h_ap
    a, hh, p = map(math.radians, (az, h, LAT))
    return math.degrees(math.asin(math.sin(p) * math.sin(hh) + math.cos(p) * math.cos(hh) * math.cos(a)))


OBJETIVOS = [
    ("Sol solsticio de verano", +EPS), ("Sol solsticio de invierno", -EPS), ("Sol equinoccio", 0.0),
    ("Luna parada mayor norte", +(EPS + INCL_LUNAR)), ("Luna parada mayor sur", -(EPS + INCL_LUNAR)),
    ("Luna parada menor norte", +(EPS - INCL_LUNAR)), ("Luna parada menor sur", -(EPS - INCL_LUNAR)),
]


def procesar(est):
    _, am, s_i, h, s_h = est
    az = am + D_MAG
    s_az = math.hypot(s_i, S_D_MAG)
    # el azimut de la brujula es de una direccion de salida: se toma el hemisferio de salida (az < 180)
    azc = az % 360.0
    azs = azc if azc <= 180.0 else 360.0 - azc
    d0 = dec(azs, h)
    d_az = (dec(azs + 1e-4, h) - dec(azs - 1e-4, h)) / 2e-4
    d_h = (dec(azs, h + 1e-4) - dec(azs, h - 1e-4)) / 2e-4
    s_lin = math.hypot(d_az * s_az, d_h * s_h)
    rng = random.Random(SEMILLA)
    v = [dec(azs + rng.gauss(0, s_az), h + rng.gauss(0, s_h)) for _ in range(20000)]
    m = sum(v) / len(v)
    s_mc = math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1))
    return azs, d0, s_lin, s_mc


def informe_estructura(secciones_requeridas, texto):
    faltan = [s for s in secciones_requeridas if ("## " + s) not in texto]
    numeros = re.findall(r"(\d+[.,]\d+)\s*(?:grados|°)", texto)
    sin_inc = [n for n in re.findall(r"(\d+[.,]\d+)\s*grados(?!\s*\+-)", texto)]
    return faltan, len(numeros), len(sin_inc)


def main():
    print("Python %d.%d.%d (biblioteca estandar)" % sys.version_info[:3])
    print("Sitio SINTETICO: lat = %.1f N ; oblicuidad ilustrativa = %.1f ; declinacion magnetica = %.1f +- %.1f" % (LAT, EPS, D_MAG, S_D_MAG))
    print(" est  az_verd   dec     s_lin   s_MC   objetivo mas cercano (n_sigma)       compatible<2s   P(azar)")
    m_obj = len(OBJETIVOS)
    dmax = EPS + INCL_LUNAR
    filas = []
    for e in ESTRUCTURAS:
        azs, d0, sl, sm = procesar(e)
        assert abs(sl - sm) / sl < 0.08
        mejor = min(OBJETIVOS, key=lambda o: abs(d0 - o[1]))
        ns = abs(d0 - mejor[1]) / sl
        # probabilidad de que una declinacion al azar en [-dmax, +dmax] caiga a menos de 2 sigma de ALGUN objetivo
        paso = 0.001
        n_pts = int(2 * dmax / paso)
        cubiertos = 0
        for i in range(n_pts):
            x = -dmax + (i + 0.5) * paso
            if any(abs(x - o[1]) <= 2.0 * sl for o in OBJETIVOS):
                cubiertos += 1
        p_azar = cubiertos / n_pts
        filas.append((e[0], ns, p_azar))
        print(" %s  %7.2f  %+6.2f  %5.2f  %5.2f   %-26s (%.2f)     %-3s          %.3f" % (e[0], azs, d0, sl, sm, mejor[0], ns, "si" if ns < 2 else "no", p_azar))
    print("Objetivos comparados por estructura = %d ; P(azar) = fraccion de declinaciones posibles a menos de 2 sigma de algun objetivo" % m_obj)
    assert all(f[2] > 0.2 for f in filas)
    assert sum(1 for f in filas if f[1] < 2) >= 1

    secciones = ["Resumen", "Sitio y contexto", "Metodo y mediciones", "Resultados", "Interpretacion y credibilidad", "Limites", "Fuentes"]
    bueno = "\n".join("## " + s for s in secciones) + "\nEje E1: azimut 55.5 grados +- 0.7 grados\n"
    malo = "## Resumen\n## Resultados\nEje E1: azimut 55.5 grados\n"
    f1, n1, s1 = informe_estructura(secciones, bueno)
    f2, n2, s2 = informe_estructura(secciones, malo)
    print("Verificador de estructura: informe completo -> faltan %d secciones ; informe incompleto -> faltan %d secciones, %d cifra(s) angular(es) sin incertidumbre" % (len(f1), len(f2), s2))
    assert len(f1) == 0 and len(f2) == 5 and s2 == 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
