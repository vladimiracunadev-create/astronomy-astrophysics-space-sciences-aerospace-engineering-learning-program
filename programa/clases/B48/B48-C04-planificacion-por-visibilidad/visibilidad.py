"""Visibilidad de un objeto: altitud, masa de aire y horas por encima de un límite.

Datos: latitud del sitio -30,0° y límite de altitud 30° (masa de aire 2), ILUSTRATIVOS; declinaciones
de tres objetos ficticios. No se consultó ninguna fuente externa.
Modelo: sen(h) = sen(phi) sen(delta) + cos(phi) cos(delta) cos(H); masa de aire X = sec z = 1/sen(h)
(capa plana, válida hasta ~60° de distancia cenital). Horas por encima del límite: 2 H0 / 15
con cos(H0) = (sen(h0) - sen(phi) sen(delta)) / (cos(phi) cos(delta)); H en horas siderales.
Segunda vía: barrido numérico de H cada minuto sidéreo.
Supuestos: sin refracción, sin horizonte local, sin Luna; el objeto no cambia de declinación esa noche.
Tolerancia: 1/60 h (un minuto) entre la vía analítica y el barrido.
"""
import math

PHI = math.radians(-30.0)
H0 = math.radians(30.0)
OBJETOS = [("Objeto A", -20.0), ("Objeto B", -60.0), ("Objeto C", 20.0), ("Objeto D", 60.0)]


def alt(H_rad, dec):
    s = math.sin(PHI) * math.sin(dec) + math.cos(PHI) * math.cos(dec) * math.cos(H_rad)
    return math.asin(s)


def analitico(dec):
    c = (math.sin(H0) - math.sin(PHI) * math.sin(dec)) / (math.cos(PHI) * math.cos(dec))
    if c <= -1.0:
        return 24.0, "circumpolar sobre el límite"
    if c >= 1.0:
        return 0.0, "nunca alcanza el límite"
    return 2 * math.degrees(math.acos(c)) / 15.0, "sube y baja"


def barrido(dec):
    n = 0
    paso = 24 * 60
    for i in range(paso):
        H = math.radians(-180.0 + 360.0 * i / paso)
        if alt(H, dec) >= H0:
            n += 1
    return n / 60.0


def calc():
    filas = []
    for nombre, d in OBJETOS:
        dec = math.radians(d)
        h_tr = math.degrees(alt(0.0, dec))
        X = 1 / math.sin(math.radians(h_tr)) if h_tr > 1.0 else float("inf")
        horas, tipo = analitico(dec)
        filas.append(dict(nombre=nombre, dec=d, h_tr=h_tr, X=X, horas=horas, bar=barrido(dec), tipo=tipo))
    return filas


def main():
    for f in calc():
        xs = "—" if math.isinf(f["X"]) else f"{f['X']:.3f}"
        print(f"{f['nombre']}: dec {f['dec']:+.0f}°  altitud en el tránsito {f['h_tr']:.2f}°  X = {xs}  horas analítico {f['horas']:.3f}  barrido {f['bar']:.3f}  ({f['tipo']})")
    for f in calc():
        assert abs(f["horas"] - f["bar"]) < 1 / 60 + 1e-9
    a = calc()[0]
    assert abs(a["h_tr"] - (90 - abs(-30 - (-20)))) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
