"""B123-C04 - Comparacion SINTETICA de vias de resolucion y reglas de arbitraje.

Datos SINTETICOS (duraciones y costos son ilustrativos). Solo biblioteca estandar. Semilla fija.
Normativa (leida en resumen, ver CLASE.md): Reglas Opcionales de la CPA para controversias
relacionadas con actividades espaciales (2011), arts. 1, 6-10, 17, 26, 29; Convenio de 1972, arts. XIV-XX.
"""
import random
import statistics
import sys
from datetime import date, timedelta

SEMILLA = 123
random.seed(SEMILLA)


def numero_arbitros(acuerdo_en_30_dias, acordado=None):
    """art. 7(1): tres arbitros salvo acuerdo sobre uno solo en 30 dias desde la notificacion."""
    if acordado is not None:
        return acordado
    return 1 if acuerdo_en_30_dias else 3


def medida_provisional(prob_dano_irreparable, prob_exito):
    """art. 26(3): para ciertas medidas, dano irreparable probable y posibilidad razonable de exito.
    Umbrales 0,5 y 0,3 son CONVENCION DIDACTICA, no del texto."""
    return prob_dano_irreparable > 0.5 and prob_exito > 0.3


def duraciones(n, media, sigma):
    return sorted(random.lognormvariate(0.0, sigma) * media for _ in range(n))


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Datos SINTETICOS; duraciones en meses; semilla", SEMILLA)
    print("Arbitros (art. 7(1)): sin acuerdo ->", numero_arbitros(False), "; con acuerdo en 30 dias ->", numero_arbitros(True))
    notif = date(2027, 2, 1)
    print("Notificacion", notif, "-> fin del plazo de 30 dias:", notif + timedelta(days=30))
    for pi, pe in [(0.7, 0.5), (0.7, 0.2), (0.3, 0.9)]:
        print(f"Medida provisional con P(irreparable)={pi}, P(exito)={pe}: {'procede (convencion)' if medida_provisional(pi, pe) else 'no procede (convencion)'}")
    res = {}
    for nombre, media, sigma, costo in [("Comision de reclamaciones", 18.0, 0.30, 1.0),
                                         ("Arbitraje CPA (3 arbitros)", 24.0, 0.35, 2.4),
                                         ("Arbitraje CPA (1 arbitro)", 14.0, 0.35, 1.3)]:
        d = duraciones(10000, media, sigma)
        res[nombre] = (statistics.median(d), d[int(0.9 * len(d))], costo)
        print(f"  {nombre:<28s} mediana={res[nombre][0]:5.1f} P90={res[nombre][1]:5.1f} meses  costo relativo={costo:.1f}")
    assert res["Arbitraje CPA (1 arbitro)"][0] < res["Arbitraje CPA (3 arbitros)"][0]
    assert numero_arbitros(False) == 3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
