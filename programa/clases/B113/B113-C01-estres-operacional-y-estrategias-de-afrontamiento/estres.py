"""B113-C01: estres operacional como acumulacion y recuperacion (modelo ILUSTRATIVO).

Modelo discreto diario: x[n+1] = (1 - r) * x[n] + a * d[n]
  x: carga de estres (unidades arbitrarias, u.a.), r: tasa de recuperacion diaria,
  a: factor de valoracion (cuanto de la demanda se vive como carga), d: demanda diaria (u.a./dia).
Todos los datos son SINTETICOS. No mide a ninguna persona. Solo biblioteca estandar.
"""
import math
import random
import sys

SEMILLA = 42
D = 10.0  # demanda diaria constante ilustrativa [u.a./dia]
ESTRATEGIAS = {
    # nombre: (r, a)  ilustrativos
    "sin estrategia": (0.20, 1.00),
    "centrada en el problema": (0.20, 0.70),
    "centrada en la recuperacion": (0.35, 1.00),
    "combinada": (0.35, 0.70),
}


def simular(r, a, demanda, x0=0.0):
    x = x0
    serie = []
    for d in demanda:
        x = (1 - r) * x + a * d
        serie.append(x)
    return serie


def estacionario(r, a, d):
    return a * d / r


def cerrada(r, a, d, n):
    # solucion analitica con x0 = 0 tras n dias
    return estacionario(r, a, d) * (1 - (1 - r) ** n)


def dias_hasta(fraccion, r):
    return math.log(1 - fraccion) / math.log(1 - r)


def main():
    print("Python %s (biblioteca estandar)" % sys.version.split()[0])
    print("Datos SINTETICOS e ILUSTRATIVOS: demanda d = %.1f u.a./dia, 60 dias, semilla %d" % (D, SEMILLA))
    print(" estrategia                     r     a   x*(u.a.)  x(60) sim  x(60) analitica  dias al 80%")
    maxdif = 0.0
    for nombre, (r, a) in ESTRATEGIAS.items():
        s = simular(r, a, [D] * 60)
        xa = cerrada(r, a, D, 60)
        maxdif = max(maxdif, abs(s[-1] - xa))
        print(" %-28s %.2f  %.2f  %8.3f  %9.3f  %14.3f  %9.2f" % (
            nombre, r, a, estacionario(r, a, D), s[-1], xa, dias_hasta(0.8, r)))
    print("Diferencia maxima simulacion-analitica en x(60) = %.2e" % maxdif)

    rng = random.Random(SEMILLA)
    demanda = [max(0.0, rng.gauss(D, 3.0)) for _ in range(400)]
    print("Con demanda ruidosa (media %.2f, sd 3.0; 400 dias), media de x en los ultimos 200 dias:" % D)
    medias = {}
    for nombre, (r, a) in ESTRATEGIAS.items():
        s = simular(r, a, demanda)
        m = sum(s[200:]) / 200
        medias[nombre] = m
        print("  %-28s media = %7.3f ; x* = %7.3f ; cociente = %.3f" % (
            nombre, m, estacionario(r, a, D), m / estacionario(r, a, D)))
    # pulso: tras 10 dias de demanda doble, dias para volver al 105 % de x*
    r, a = ESTRATEGIAS["sin estrategia"]
    x = estacionario(r, a, D)
    for _ in range(10):
        x = (1 - r) * x + a * 2 * D
    pico = x
    n = 0
    while x > 1.05 * estacionario(r, a, D):
        x = (1 - r) * x + a * D
        n += 1
    print("Pulso (10 dias con demanda doble, sin estrategia): pico = %.2f u.a.; %d dias para volver al 105%% de x*" % (pico, n))

    assert maxdif < 1e-9
    assert abs(estacionario(0.20, 1.0, D) - 50.0) < 1e-12
    for nombre, (r, a) in ESTRATEGIAS.items():
        assert abs(medias[nombre] / estacionario(r, a, D) - 1) < 0.05
    assert abs(dias_hasta(0.5, 0.2) - math.log(2) / -math.log(0.8)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
