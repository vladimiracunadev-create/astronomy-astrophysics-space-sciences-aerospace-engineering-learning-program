"""B132-C02: datacion por intervalos compatibles y precision de un gnomon SINTETICO.

Parte A: intervalos de datacion (150-100 a. C. por la forma de las letras y ~80-60 a. C. para el
naufragio, ambos de Freeth et al. 2006) combinados con una fecha radiometrica SINTETICA.
Parte B: gnomon sintetico; propagacion de errores y sesgo del limbo solar.
Solo biblioteca estandar. Unidades: anios (astronomicos, 1 a. C. = 0), metros, grados.
"""
import math
import random
import sys

SEMILLA = 20261112


def anio_ac(n):
    """Convierte 'n a. C.' al numero de anio astronomico (1 a. C. = 0)."""
    return 1 - n


def grilla(a, b, paso=0.5):
    n = int(round((b - a) / paso))
    return [a + i * paso for i in range(n + 1)]


def datacion():
    lo_let, hi_let = anio_ac(150), anio_ac(100)      # forma de las letras: 150-100 a. C. (Freeth 2006)
    naufragio_min, naufragio_max = anio_ac(80), anio_ac(60)   # naufragio hacia 80-60 a. C. (Freeth 2006)
    # el objeto existia antes del naufragio: terminus ante quem = limite mas antiguo del naufragio
    intervalo_compatible = (lo_let, min(hi_let, naufragio_max))
    # fecha radiometrica SINTETICA: gaussiana en 120 a. C. +- 25 a
    mu, sg = anio_ac(120), 25.0
    xs = grilla(anio_ac(250), anio_ac(0))
    post = []
    for x in xs:
        in_let = 1.0 if lo_let <= x <= hi_let else 0.0
        in_wr = 1.0 if x <= naufragio_max else 0.0
        post.append(in_let * in_wr * math.exp(-0.5 * ((x - mu) / sg) ** 2))
    z = sum(post)
    post = [p / z for p in post]
    media = sum(x * p for x, p in zip(xs, post))
    var = sum((x - media) ** 2 * p for x, p in zip(xs, post))
    # intervalo central del 95 %
    acum, i95lo, i95hi = 0.0, None, None
    for x, p in zip(xs, post):
        acum += p
        if i95lo is None and acum >= 0.025:
            i95lo = x
        if i95hi is None and acum >= 0.975:
            i95hi = x
    return intervalo_compatible, media, math.sqrt(var), i95lo, i95hi


# Parte B: gnomon sintetico
LAT = 36.0          # grados N, ILUSTRATIVA
EPS = 23.7          # grados, oblicuidad ILUSTRATIVA
H = 1.000           # m
SIGMA_L = 0.002     # m, error aleatorio de lectura de la sombra
SEMIDIAM = 0.2667   # grados, semidiametro solar medio (estandar, no consultado)


def refraccion(z_grados):
    """Refraccion aproximada en grados: 58,3'' * tan z (estandar, no consultada; valida para z < 70)."""
    return (58.3 / 3600.0) * math.tan(math.radians(z_grados))


def sombra(z_centro, con_limbo=True):
    """Largo de la sombra. La punta la marca el limbo superior del Sol, que esta 'SEMIDIAM' mas alto."""
    z_ap = z_centro - refraccion(z_centro)
    if con_limbo:
        z_ap -= SEMIDIAM
    return H * math.tan(math.radians(z_ap))


def oblicuidad_desde(l_ver, l_inv, corregir):
    z_ver = math.degrees(math.atan2(l_ver, H))
    z_inv = math.degrees(math.atan2(l_inv, H))
    if corregir:
        z_ver += SEMIDIAM + refraccion(z_ver)
        z_inv += SEMIDIAM + refraccion(z_inv)
    return 0.5 * (z_inv - z_ver)


def main():
    print("Python %d.%d.%d (biblioteca estandar)" % sys.version_info[:3])
    inter, media, sd, a, b = datacion()
    print("Parte A. Datacion (anios astronomicos; 1 a. C. = 0). Fecha radiometrica SINTETICA: 120 a. C. +- 25 a")
    print("  Intervalo compatible letras (150-100 a. C.) y naufragio (<= 60 a. C.): %d a %d (= %d a %d a. C.)" % (inter[0], inter[1], 1 - inter[0], 1 - inter[1]))
    print("  Posterior combinada: media = %.1f (%.1f a. C.), sd = %.1f a, 95 %% central = [%.1f, %.1f]" % (media, 1 - media, sd, a, b))
    assert inter == (-149, -99)
    assert -149 <= media <= -99

    phi = math.radians(LAT)
    z_ver = LAT - EPS
    z_inv = LAT + EPS
    l_ver = sombra(z_ver)
    l_inv = sombra(z_inv)
    print("Parte B. Gnomon SINTETICO: h = %.3f m, latitud ilustrativa %.1f N, oblicuidad ilustrativa %.2f" % (H, LAT, EPS))
    print("  Distancia cenital solsticio verano = %.2f, invierno = %.2f" % (z_ver, z_inv))
    print("  Sombra (limbo superior): verano = %.4f m, invierno = %.4f m" % (l_ver, l_inv))
    e_sin = oblicuidad_desde(l_ver, l_inv, corregir=False)
    e_con = oblicuidad_desde(l_ver, l_inv, corregir=True)
    print("  Oblicuidad recuperada SIN corregir limbo/refraccion = %.4f (sesgo %.4f)" % (e_sin, e_sin - EPS))
    print("  Oblicuidad recuperada CON correccion              = %.4f (sesgo %.2e)" % (e_con, e_con - EPS))
    assert abs(e_con - EPS) < 1e-3
    zv = math.degrees(math.atan2(l_ver, H)); zi = math.degrees(math.atan2(l_inv, H))
    lat_sin = 0.5 * (zv + zi)
    lat_con = 0.5 * ((zv + SEMIDIAM + refraccion(zv)) + (zi + SEMIDIAM + refraccion(zi)))
    print("  Latitud recuperada SIN corregir = %.4f (sesgo %.4f) ; CON correccion = %.4f (sesgo %.2e)" % (lat_sin, lat_sin - LAT, lat_con, lat_con - LAT))
    assert abs(lat_con - LAT) < 1e-3 and abs(lat_sin - LAT) > 0.2

    # propagacion lineal frente a Monte Carlo, con correccion
    d = 1e-6
    f = lambda lv, li: oblicuidad_desde(lv, li, True)
    dv = (f(l_ver + d, l_inv) - f(l_ver - d, l_inv)) / (2 * d)
    di = (f(l_ver, l_inv + d) - f(l_ver, l_inv - d)) / (2 * d)
    sig_lin = math.sqrt((dv * SIGMA_L) ** 2 + (di * SIGMA_L) ** 2)
    rng = random.Random(SEMILLA)
    vals = []
    n = 20000
    for _ in range(n):
        vals.append(f(l_ver + rng.gauss(0, SIGMA_L), l_inv + rng.gauss(0, SIGMA_L)))
    m = sum(vals) / n
    sig_mc = math.sqrt(sum((v - m) ** 2 for v in vals) / (n - 1))
    print("  Error aleatorio (sigma_L = %.1f mm): lineal = %.4f ; Monte Carlo (semilla %d, %d sorteos) = %.4f" % (SIGMA_L * 1e3, sig_lin, SEMILLA, n, sig_mc))
    assert abs(sig_lin - sig_mc) / sig_lin < 0.03
    print("  El limbo desplaza ambas sombras en el mismo sentido: se cancela casi todo en la oblicuidad (%.4f) pero no en la latitud (%.4f)" % (abs(e_sin - EPS), abs(lat_sin - LAT)))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
