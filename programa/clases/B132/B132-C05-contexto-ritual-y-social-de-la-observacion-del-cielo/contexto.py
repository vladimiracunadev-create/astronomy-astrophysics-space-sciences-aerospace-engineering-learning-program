"""B132-C05: combinar estadistica y contexto para valorar una alineacion (casos SINTETICOS).

Las cuatro categorias de credibilidad (aceptada, debatida entre especialistas, no probada, refutada) son las que
describen Cotte y Ruggles en la conclusion del Estudio Tematico ICOMOS-IAU (consultada). Los umbrales numericos
que las separan aqui son una convencion DIDACTICA de esta clase, no de esos autores.
La cota de Sellke, Bayarri y Berger (2001), BF <= 1/(-e p ln p), esta recordada de la literatura y NO se consulto;
el laboratorio comprueba su monotonia. Sociedades, sitios y razones de verosimilitud SINTETICOS.
Solo biblioteca estandar.
"""
import math
import sys


def bf_maximo(p):
    """Cota superior del factor de Bayes a favor de H1 dado un valor p < 1/e."""
    return 1.0 / (-math.e * p * math.log(p))


def prob_posterior(prior_prob, razones):
    odds = prior_prob / (1.0 - prior_prob)
    for r in razones:
        odds *= r
    return odds / (1.0 + odds)


# casos SINTETICOS: p de la estadistica, razones de verosimilitud contextuales (SINTETICAS) y su dependencia
CASOS = [
    # nombre, p, [lineas contextuales], factor_dependencia (0..1: cuanto cuenta cada linea adicional), evidencia en contra
    ("Sitio S1: eje a salida solsticial, registro historico propio y practica ritual coincidente", 0.004, [6.0, 4.0], 0.8, 1.0),
    ("Sitio S2: eje compatible, sin registro de la sociedad, analogia lejana", 0.020, [1.5], 0.8, 1.0),
    ("Sitio S3: efecto de luz espectacular, sin evidencia de intencion", 0.300, [1.0], 0.8, 1.0),
    ("Sitio S4: lectura astronomica de un simbolo; el contexto cultural apunta a otro uso", 0.040, [0.5, 0.2], 0.8, 0.2),
]


def categoria(post, en_contra):
    if en_contra < 0.5 and post < 0.1:
        return "refutada"
    if post >= 0.9:
        return "aceptada"
    if post >= 0.5:
        return "debatida entre especialistas"
    return "no probada"


def valorar(p, lineas, dep, contra, prior):
    razones = []
    if p < 1.0 / math.e:
        razones.append(bf_maximo(p))        # cota: la mejor evidencia estadistica posible
    for i, r in enumerate(lineas):
        razones.append(r ** (dep ** i))     # lineas adicionales cuentan menos (dependencia)
    razones.append(contra)
    return prob_posterior(prior, razones), razones


def main():
    print("Python %d.%d.%d (biblioteca estandar)" % sys.version_info[:3])
    print("Cota del factor de Bayes a favor de la intencion segun p (Sellke y otros 2001, no consultada):")
    previo = None
    for p in (0.2, 0.05, 0.01, 0.004, 0.001):
        b = bf_maximo(p)
        print("  p = %.3f  ->  BF <= %.2f" % (p, b))
        assert previo is None or b > previo
        previo = b
    assert abs(bf_maximo(0.05) - 2.46) < 0.01
    prior = 0.10
    print("Casos SINTETICOS, probabilidad previa de intencion = %.2f (convencion didactica)" % prior)
    print(" caso  p       razones            post   categoria")
    for i, (nom, p, lineas, dep, contra) in enumerate(CASOS, 1):
        post, razones = valorar(p, lineas, dep, contra, prior)
        print("  S%d  %.3f  %-18s %.3f  %s" % (i, p, ",".join("%.2f" % r for r in razones), post, categoria(post, contra)))
    print("Sensibilidad al previo (0.05 / 0.10 / 0.30) para S1 y S2:")
    for idx in (0, 1):
        _, p, lineas, dep, contra = CASOS[idx]
        fila = [valorar(p, lineas, dep, contra, pr)[0] for pr in (0.05, 0.10, 0.30)]
        print("  S%d: %s" % (idx + 1, "  ".join("%.3f" % x for x in fila)))
    # dependencia: sin descuento, S1 sobreestima
    _, p, lineas, _, contra = CASOS[0]
    con = valorar(p, lineas, 0.8, contra, prior)[0]
    sin = valorar(p, lineas, 1.0, contra, prior)[0]
    print("Descuento por dependencia en S1: con = %.3f ; sin descuento = %.3f" % (con, sin))
    assert sin > con
    assert categoria(valorar(*CASOS[0][1:4], CASOS[0][4], prior)[0], CASOS[0][4]) == "aceptada"
    assert categoria(valorar(*CASOS[1][1:4], CASOS[1][4], prior)[0], CASOS[1][4]) == "no probada"
    assert valorar(CASOS[2][1], CASOS[2][2], 0.8, 1.0, prior)[0] < 0.2
    assert valorar(CASOS[3][1], CASOS[3][2], 0.8, 0.2, prior)[0] < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
