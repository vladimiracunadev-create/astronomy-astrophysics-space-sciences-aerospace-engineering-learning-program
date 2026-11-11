"""B114-C04 - Refugio contra una tormenta solar SINTETICA.

Unidades: mSv (dosis equivalente), h, g/cm2 (densidad areal de blindaje).
TODOS los parametros son ILUSTRATIVOS; la tormenta es SINTETICA, no un evento
observado. El objetivo de 150 mSv es la cifra de diseno que la Health Physics
Society atribuye al refugio de Orion en Artemis I (respuesta del 2026-02-23,
consultada 2026-11-10). Solo stdlib. Python 3.12.
"""
import math
import sys

H0 = 600.0        # mSv, dosis total en espacio libre de la tormenta sintetica
TAU = 6.0         # h, escala de tiempo del perfil
T_FIN = 72.0      # h, fin de la ventana
F1, L1 = 0.7, 8.0     # fraccion y longitud de atenuacion componente blanda (g/cm2)
F2, L2 = 0.3, 40.0    # componente penetrante
X_CABINA = 5.0    # g/cm2, estructura de la cabina (ilustrativo)
OBJETIVO = 150.0  # mSv (HPS, Orion, Artemis I)


def atenuacion(x):
    """Fraccion de dosis que pasa un blindaje de x g/cm2 (modelo de dos
    componentes exponenciales, ILUSTRATIVO)."""
    return F1 * math.exp(-x / L1) + F2 * math.exp(-x / L2)


def acumulada(t):
    """Dosis en espacio libre acumulada hasta t [mSv]: integral analitica de
    r(t) = H0 t exp(-t/TAU) / TAU^2."""
    return H0 * (1 - math.exp(-t / TAU) * (1 + t / TAU))


def acumulada_numerica(t, n=20000):
    h = t / n
    r = lambda s: H0 * s * math.exp(-s / TAU) / TAU ** 2
    return h * (sum(r(i * h) for i in range(1, n)) + 0.5 * (r(0) + r(t)))


def dosis_total(t_entrada, t_salida, x_refugio):
    f = acumulada
    fuera = f(t_entrada) + (f(T_FIN) - f(t_salida))
    dentro = f(t_salida) - f(t_entrada)
    return atenuacion(X_CABINA) * fuera + atenuacion(x_refugio) * dentro


def x_minimo(t_entrada, t_salida, objetivo):
    lo, hi = X_CABINA, 400.0
    if dosis_total(t_entrada, t_salida, hi) > objetivo:
        return None
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if dosis_total(t_entrada, t_salida, mid) > objetivo:
            lo = mid
        else:
            hi = mid
    return hi


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Tormenta SINTETICA: H0 = %.0f mSv en espacio libre, tau = %.1f h, ventana %.0f h"
          % (H0, TAU, T_FIN))
    print("Atenuacion ILUSTRATIVA de dos componentes (L1 = %.0f, L2 = %.0f g/cm2)" % (L1, L2))
    print("Fraccion transmitida por blindaje [g/cm2]:")
    for x in (0, 5, 10, 20, 40):
        print("  x = %3d  ->  %.4f" % (x, atenuacion(x)))
    # verificacion por segunda via: integral numerica frente a analitica
    a = acumulada(10.0)
    b = acumulada_numerica(10.0)
    print("Dosis libre acumulada en 10 h: analitica %.4f mSv ; numerica %.4f mSv ; dif = %.2e"
          % (a, b, abs(a - b) / a))
    assert abs(a - b) / a < 1e-6
    print("Dosis total [mSv] con refugio de 30 g/cm2 y salida a las 24 h:")
    print("  t_entrada [h]   dosis [mSv]   cumple 150 mSv")
    prev = -1.0
    for te in (0.5, 1.0, 2.0, 4.0, 8.0):
        d = dosis_total(te, 24.0, 30.0)
        assert d > prev
        prev = d
        print("  %8.1f %14.1f   %s" % (te, d, "si" if d <= OBJETIVO else "no"))
    sin_refugio = atenuacion(X_CABINA) * acumulada(T_FIN)
    print("Sin refugio (solo cabina, 5 g/cm2): %.1f mSv" % sin_refugio)
    print("Densidad areal minima del refugio para %.0f mSv:" % OBJETIVO)
    for te in (0.5, 1.0, 2.0, 4.0):
        xm = x_minimo(te, 24.0, OBJETIVO)
        print("  entrada a las %.1f h -> %s" %
              (te, "no alcanzable (<400 g/cm2)" if xm is None else "%.1f g/cm2" % xm))
    # sensibilidad al tiempo de permanencia
    print("Efecto del tiempo de salida (entrada 1 h, refugio 30 g/cm2):")
    for ts in (6.0, 12.0, 24.0, 48.0):
        print("  salida a las %4.0f h -> %.1f mSv" % (ts, dosis_total(1.0, ts, 30.0)))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
