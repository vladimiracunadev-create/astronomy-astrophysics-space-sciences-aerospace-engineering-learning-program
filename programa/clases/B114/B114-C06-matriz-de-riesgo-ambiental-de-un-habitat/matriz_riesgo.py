"""B114-C06 - Matriz de riesgo ambiental de un habitat SINTETICO.

Escalas ordinales 1-5 de probabilidad (P) y severidad (S). TODAS las
calificaciones, medidas y reducciones son SINTETICAS/ILUSTRATIVAS: no proceden
de ningun analisis de riesgo real ni de una norma. Semilla fija. Solo stdlib.
"""
import random
import sys

# (peligro, P, S, medida, reduccion de P, reduccion de S)
PELIGROS = [
    ("Fuga lenta de presion",          3, 3, "deteccion de tendencia (C02)",       1, 0),
    ("Brecha por impacto",             2, 5, "compartimentos y cierre rapido",     0, 1),
    ("Tormenta de particulas solares", 3, 4, "refugio y aviso (C04)",              0, 2),
    ("Exceso de CO2",                  3, 3, "alarma y eliminacion redundante",    1, 1),
    ("Incendio",                       2, 5, "deteccion y supresion",              1, 1),
    ("Polvo en el habitat",            4, 2, "filtracion y limpieza",              1, 0),
    ("Fallo de salida de emergencia",  1, 4, "rutas alternativas (C01)",           0, 1),
]
# Clasificacion por producto P x S (ILUSTRATIVA)
def clase(r):
    if r >= 15:
        return "ALTO"
    if r >= 8:
        return "MEDIO"
    return "BAJO"


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Matriz SINTETICA: P y S ordinales 1-5; ALTO >= 15, MEDIO 8-14, BAJO < 8")
    print("%-32s %2s %2s %4s %-5s | %2s %2s %4s %-5s" %
          ("peligro", "P", "S", "R", "clase", "P'", "S'", "R'", "clase'"))
    tot0 = tot1 = 0
    iniciales = []
    for nombre, p, s, _m, dp, ds in PELIGROS:
        r0 = p * s
        p1, s1 = max(1, p - dp), max(1, s - ds)
        r1 = p1 * s1
        tot0 += r0
        tot1 += r1
        iniciales.append((r0, nombre))
        assert r1 <= r0
        print("%-32s %2d %2d %4d %-5s | %2d %2d %4d %-5s" %
              (nombre, p, s, r0, clase(r0), p1, s1, r1, clase(r1)))
    print("Suma de riesgos: inicial %d ; residual %d ; reduccion %.1f %%"
          % (tot0, tot1, 100 * (tot0 - tot1) / tot0))
    orden = sorted(iniciales, reverse=True)
    print("Orden de prioridad inicial:")
    for i, (r, n) in enumerate(orden, 1):
        print("  %d. %-32s R = %d" % (i, n, r))
    # Sensibilidad: perturbar cada calificacion en -1, 0 o +1 (semilla 114)
    rng = random.Random(114)
    n_mc = 20000
    cambia = {n: 0 for n, *_ in PELIGROS}
    cambia_top = 0
    top0 = orden[0][1]
    for _ in range(n_mc):
        vals = []
        for nombre, p, s, *_ in PELIGROS:
            pp = min(5, max(1, p + rng.choice((-1, 0, 1))))
            ss = min(5, max(1, s + rng.choice((-1, 0, 1))))
            vals.append((pp * ss, nombre, p * s))
        for r, nombre, r0 in vals:
            if clase(r) != clase(r0):
                cambia[nombre] += 1
        if max(vals)[1] != top0:
            cambia_top += 1
    print("Sensibilidad (+-1 en P y S, %d muestras): fraccion que cambia de clase" % n_mc)
    for nombre, c in cambia.items():
        print("  %-32s %5.1f %%" % (nombre, 100 * c / n_mc))
    print("El peligro de mayor riesgo cambia en el %.1f %% de las muestras" %
          (100 * cambia_top / n_mc))
    # Segunda via: conteo directo de la clase de cada celda de la matriz
    cuenta = {"ALTO": 0, "MEDIO": 0, "BAJO": 0}
    for p in range(1, 6):
        for s in range(1, 6):
            cuenta[clase(p * s)] += 1
    print("Celdas de la matriz 5x5: %s" % cuenta)
    assert sum(cuenta.values()) == 25
    assert tot1 < tot0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
