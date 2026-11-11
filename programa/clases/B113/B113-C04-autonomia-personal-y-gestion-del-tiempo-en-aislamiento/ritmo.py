"""B113-C04: deriva del dia marciano frente al reloj terrestre y rutina con holgura.

Dia solar medio de Marte: 24.6597 h (ficha de Marte, NASA/NSSDC, consultada 2026-11-10).
Reloj terrestre: 24 h. Un reloj marciano ajustado al dia solar de Marte se desplaza respecto del terrestre
(24.6597 - 24) h por dia terrestre. Rutina, duraciones y holgura: SINTETICAS e ILUSTRATIVAS.
Solo biblioteca estandar. Semilla fija.
"""
import random
import sys

SOL_H = 24.6597
DIA_H = 24.0
SEMILLA = 11
TAREAS_PLAN_H = [1.5, 1.0, 1.0, 1.0, 0.75, 0.75]  # plan de una jornada de trabajo, ilustrativo
ENSAYOS = 20000


def deriva_h_por_dia():
    return SOL_H - DIA_H


def dias_ciclo_completo():
    return DIA_H / deriva_h_por_dia()


def reloj_marciano_a_terrestre(n_soles):
    """Hora terrestre (mod 24) a la que empieza el sol n, si el sol 0 empieza a las 00:00."""
    return (n_soles * SOL_H) % DIA_H


def prob_terminar(holgura_h, rng, ensayos=ENSAYOS):
    """Probabilidad de terminar el plan dentro de (suma plan + holgura) con duraciones U(0.8, 1.4)*plan."""
    limite = sum(TAREAS_PLAN_H) + holgura_h
    ok = 0
    suma_total = 0.0
    for _ in range(ensayos):
        tot = sum(t * rng.uniform(0.8, 1.4) for t in TAREAS_PLAN_H)
        suma_total += tot
        if tot <= limite:
            ok += 1
    return ok / ensayos, suma_total / ensayos


def main():
    print("Python %s (biblioteca estandar)" % sys.version.split()[0])
    print("Dia solar de Marte = %.4f h (NASA/NSSDC, 2026-11-10); dia terrestre = %.1f h" % (SOL_H, DIA_H))
    d = deriva_h_por_dia()
    print("Deriva = %.4f h = %.2f min por dia terrestre; ciclo completo en %.2f dias" % (d, d * 60, dias_ciclo_completo()))
    print(" sol n   hora terrestre de inicio [h]")
    for n in (0, 1, 10, 30, 36, 37):
        print(" %5d %12.3f" % (n, reloj_marciano_a_terrestre(n)))
    plan = sum(TAREAS_PLAN_H)
    print("Plan ILUSTRATIVO: %d tareas, %.2f h planificadas; duraciones reales U(0.8, 1.4) x plan (media x1.1), semilla %d" % (
        len(TAREAS_PLAN_H), plan, SEMILLA))
    print(" holgura [h]  P(terminar a tiempo)  duracion media [h]  esperada [h]")
    rng = random.Random(SEMILLA)
    medias = []
    for h in (0.0, 0.5, 1.0, 1.5, 2.0):
        p, m = prob_terminar(h, rng)
        medias.append(m)
        print(" %9.1f %16.3f %19.3f %13.3f" % (h, p, m, 1.1 * plan))
    # ritmo libre de 25 h (valor ilustrativo, cf. un tripulante de Mars-500): desfase frente a 24 h
    print("Ritmo libre ILUSTRATIVO de 25.0 h: desfase de %.1f h tras 10 dias; ciclo completo en %.1f dias" % (10 * 1.0, 24.0 / 1.0))

    assert abs(d - 0.6597) < 1e-9
    assert abs(reloj_marciano_a_terrestre(1) - 0.6597) < 1e-9
    assert abs(dias_ciclo_completo() - 24 / 0.6597) < 1e-12
    for m in medias:
        assert abs(m - 1.1 * plan) < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
