"""B132-C03: azimut, altura de horizonte y declinacion; compatibilidad solar de un eje SINTETICO.

Formulas esfericas estandar (no consultadas en una fuente concreta; se verifican con ida y vuelta).
Oblicuidad: polinomio de Laskar (1986) recordado de la literatura, NO consultado; se verifica contra
el valor J2000 y contra una aproximacion lineal. Monumento y mediciones SINTETICOS.
Unidades: grados, anios (astronomicos: 2500 a. C. = -2499).
"""
import math
import sys

LAT = 50.0            # grados N, SINTETICA
SEMIDIAM = 0.2667     # grados (estandar)


def oblicuidad(anio):
    """Oblicuidad media en grados; polinomio de Laskar (1986) en U = T/100 (T en siglos julianos desde J2000)."""
    u = ((anio - 2000.0) / 100.0) / 100.0
    c = [84381.448, -4680.93, -1.55, 1999.25, -51.38, -249.67, -39.05, 7.12, 27.87, 5.79, 2.45]
    seg = sum(ci * u ** i for i, ci in enumerate(c))
    return seg / 3600.0


def oblicuidad_lineal(anio):
    t = (anio - 2000.0) / 100.0
    return 23.4393 - 0.0130042 * t


def refraccion(h_ap):
    """Refraccion de Bennett (1982) en grados para altura aparente h_ap (grados); formula estandar, no consultada."""
    return (1.0 / math.tan(math.radians(h_ap + 7.31 / (h_ap + 4.4)))) / 60.0


def declinacion(az, h_verd, lat=LAT):
    a, h, p = map(math.radians, (az, h_verd, lat))
    s = math.sin(p) * math.sin(h) + math.cos(p) * math.cos(h) * math.cos(a)
    return math.degrees(math.asin(s))


def azimut(dec, h_verd, lat=LAT):
    d, h, p = map(math.radians, (dec, h_verd, lat))
    c = (math.sin(d) - math.sin(p) * math.sin(h)) / (math.cos(p) * math.cos(h))
    return math.degrees(math.acos(c))


def main():
    print("Python %d.%d.%d (biblioteca estandar)" % sys.version_info[:3])
    e2000 = oblicuidad(2000.0)
    print("Oblicuidad: Laskar J2000 = %.4f ; lineal J2000 = %.4f" % (e2000, oblicuidad_lineal(2000.0)))
    assert abs(e2000 - 23.4393) < 1e-3
    print(" anio     Laskar   lineal   dif")
    for y in (-3499, -2999, -2499, -1999, 0, 2000):
        print(" %5d   %.4f   %.4f  %+.4f" % (y, oblicuidad(y), oblicuidad_lineal(y), oblicuidad_lineal(y) - oblicuidad(y)))
    assert abs(oblicuidad_lineal(-2499) - oblicuidad(-2499)) < 0.1

    # ida y vuelta
    maxerr = 0.0
    for az in (30.0, 49.3, 90.0, 120.0):
        for h in (0.0, 0.5, 2.0):
            maxerr = max(maxerr, abs(azimut(declinacion(az, h), h) - az))
    print("Ida y vuelta azimut-declinacion: error maximo = %.2e grados" % maxerr)
    assert maxerr < 1e-9
    assert abs(declinacion(90.0, 0.0)) < 1e-12      # este verdadero, horizonte plano: declinacion 0

    # monumento SINTETICO: eje medido
    az_eje, s_az = 50.6, 0.5          # grados, SINTETICO
    h_ap, s_h = 0.5, 0.3              # altura aparente del horizonte, SINTETICO
    h_verd = h_ap - refraccion(h_ap)
    print("Monumento SINTETICO: lat = %.1f N ; eje azimut = %.1f +- %.1f ; horizonte aparente = %.1f +- %.1f" % (LAT, az_eje, s_az, h_ap, s_h))
    print("  refraccion en el horizonte aparente = %.3f ; altura verdadera = %.3f" % (refraccion(h_ap), h_verd))
    dec_eje = declinacion(az_eje, h_verd)
    d_dec_daz = (declinacion(az_eje + 1e-4, h_verd) - declinacion(az_eje - 1e-4, h_verd)) / 2e-4
    d_dec_dh = (declinacion(az_eje, h_verd + 1e-4) - declinacion(az_eje, h_verd - 1e-4)) / 2e-4
    s_dec = math.sqrt((d_dec_daz * s_az) ** 2 + (d_dec_dh * s_h) ** 2)
    print("  declinacion del eje (centro del objeto) = %+.3f +- %.3f" % (dec_eje, s_dec))
    print("Compatibilidad con el Sol solsticial (centro del disco a la altura aparente del horizonte; semidiametro %.4f):" % SEMIDIAM)
    print(" anio     eps    dec_Sol   dif    n_sigma   compatible(<2 sigma)")
    res = {}
    for y in (-3499, -2999, -2499, -1999):
        eps = oblicuidad(y)
        dif = dec_eje - eps
        ns = abs(dif) / s_dec
        res[y] = ns
        print(" %5d  %.3f  %+8.3f  %+6.3f  %6.2f    %s" % (y, eps, eps, dif, ns, "si" if ns < 2 else "no"))
    print("Azimut de salida del Sol solsticial con horizonte aparente %.1f (Laskar):" % h_ap)
    for y in (-3499, -2499, -1499):
        print("  anio %5d: %.3f" % (y, azimut(oblicuidad(y), h_verd)))
    assert res[-2499] < 2 and res[-1999] < res[-3499] + 5
    # el azimut cambia con el anio: la oblicuidad decrece con el tiempo
    assert azimut(oblicuidad(-3499), h_verd) < azimut(oblicuidad(-1499), h_verd)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
