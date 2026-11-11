"""B121-C02 - Resolucion de un sensor optico y umbrales de licenciamiento (ilustrativos).

DATOS SINTETICOS: cinco sensores inventados. Los UMBRALES de resolucion (0,25 / 0,5 / 1 / 5 m) son
ILUSTRATIVOS (no se consulto ninguna norma que los fije); solo el marco de principios (A/RES/41/65,
adoptada el 1986-12-03, metadatos consultados 2026-11-11) y el proposito de 15 CFR 960.1 se consultaron.
Unidades: m, rad, um. Geometria nadir sobre esfera, sin curvatura ni rotacion terrestre.
Solo biblioteca estandar.
"""
import math
import sys

# nombre: (altitud m, paso de pixel um, focal m, apertura m, longitud de onda um)  SINTETICOS
SENSORES = {
    "S1_microsat": (500e3, 6.5, 1.00, 0.20, 0.55),
    "S2_pequeno": (550e3, 8.0, 3.50, 0.50, 0.55),
    "S3_alta_res": (480e3, 10.0, 9.60, 1.10, 0.55),
    "S4_media_res": (700e3, 9.0, 1.20, 0.25, 0.55),
    "S5_baja_res": (800e3, 20.0, 0.45, 0.10, 0.55),
}
UMBRALES = [0.25, 0.5, 1.0, 5.0]  # m, ILUSTRATIVOS


def gsd(h, p_um, f):
    """GSD = h * p / f (m)."""
    return h * p_um * 1e-6 / f


def gsd_ifov(h, p_um, f):
    """Segunda via: IFOV = p/f (rad); GSD = 2 h tan(IFOV/2)."""
    ifov = p_um * 1e-6 / f
    return 2 * h * math.tan(ifov / 2)


def limite_difraccion(h, d, lam_um):
    """Radio de Airy proyectado: 1,22 * lambda * h / D (m)."""
    return 1.22 * lam_um * 1e-6 * h / d


def tramo(res):
    """Primer umbral ilustrativo que la resolucion efectiva alcanza (<=)."""
    for u in UMBRALES:
        if res <= u:
            return u
    return None


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Sensores SINTETICOS; umbrales", UMBRALES, "m ILUSTRATIVOS (no consultados en una norma).")
    print(f"{'sensor':14s}{'GSD[m]':>9s}{'Airy[m]':>9s}{'efec.[m]':>10s}  tramo ilustrativo")
    for n, (h, p, f, d, lam) in SENSORES.items():
        g = gsd(h, p, f)
        assert abs(g - gsd_ifov(h, p, f)) / g < 1e-9, n  # tolerancia relativa 1e-9
        a = limite_difraccion(h, d, lam)
        ef = max(g, a)
        t = tramo(ef)
        print(f"{n:14s}{g:9.3f}{a:9.3f}{ef:10.3f}  {'<= %.2f m' % t if t else 'sin tramo (> 5 m)'}")
    # prueba de coherencia: a mayor altitud, peor GSD
    h0, p, f, d, lam = SENSORES["S3_alta_res"]
    gs = [gsd(h, p, f) for h in (400e3, 500e3, 600e3)]
    assert gs == sorted(gs)
    print("S3 a 400/500/600 km: GSD =", ", ".join(f"{x:.3f}" for x in gs), "m")
    # altitud maxima de S3 para seguir en el tramo 0,5 m (limitada por GSD y por difraccion)
    h_gsd = 0.5 * f / (p * 1e-6)
    h_dif = 0.5 * d / (1.22 * lam * 1e-6)
    print(f"S3: altitud maxima para <= 0,5 m: por GSD {h_gsd/1e3:.1f} km, por difraccion {h_dif/1e3:.1f} km -> {min(h_gsd, h_dif)/1e3:.1f} km")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
