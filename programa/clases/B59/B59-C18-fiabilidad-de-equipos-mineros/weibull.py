"""B59-C18 · Fiabilidad de equipos mineros: Weibull, MTBF, disponibilidad y repuestos.

Datos SINTÉTICOS / ILUSTRATIVOS (no consultados): tiempo hasta la falla Weibull con forma beta = 1,8 y escala
eta = 800 h (desgaste abrasivo por regolito), tiempo medio de reparación MTTR = 24 h, misión de 8 760 h,
flota de 6 excavadoras. Ningún dato procede de equipos reales.
Modelo: R(t) = exp(-(t/eta)^beta); MTBF = eta Gamma(1 + 1/beta); disponibilidad A = MTBF/(MTBF + MTTR);
número de fallas en la misión ~ Poisson de media N T/(MTBF + MTTR) (aproximación de renovación); repuestos
para el cuantil 95 % de Poisson. Se contrasta con una simulación Monte Carlo de procesos de renovación.
Unidades: horas. Sin fallas dependientes, sin reparaciones imperfectas, sin mantenimiento preventivo.
Tolerancias: MTBF muestral frente a analítico < 1 %; fallas medias simuladas frente a Poisson < 3 %.
"""
import math
import platform
import random

BETA, ETA = 1.8, 800.0
MTTR = 24.0
T = 8760.0
N = 6
SEMILLA = 20261109


def sorteo(rng):
    return ETA * (-math.log(1 - rng.random())) ** (1 / BETA)


def poisson_cuantil(mu, q):
    k, p, acc = 0, math.exp(-mu), 0.0
    acc = p
    while acc < q:
        k += 1
        p *= mu / k
        acc += p
    return k


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    mtbf = ETA * math.gamma(1 + 1 / BETA)
    print(f"MTBF analitico = eta Gamma(1 + 1/beta) = {mtbf:.2f} h")
    rng = random.Random(SEMILLA)
    ms = [sorteo(rng) for _ in range(200000)]
    mtbf_m = sum(ms) / len(ms)
    print(f"MTBF muestral (200 000 sorteos) = {mtbf_m:.2f} h ; diferencia = {100*(mtbf_m-mtbf)/mtbf:+.2f} %")
    assert abs(mtbf_m - mtbf) / mtbf < 0.01
    print("t [h]   R(t) analitica   R(t) muestral")
    for t in (200.0, 500.0, 800.0, 1500.0):
        r = math.exp(-(t / ETA) ** BETA)
        rm = sum(1 for x in ms if x > t) / len(ms)
        print(f"{t:6.0f}  {r:14.4f}  {rm:13.4f}")
        assert abs(r - rm) < 0.005
    A = mtbf / (mtbf + MTTR)
    print(f"Disponibilidad A = MTBF/(MTBF + MTTR) = {A:.4f}")
    # Fallas esperadas en la mision por maquina y para la flota
    ciclo = mtbf + MTTR
    f_maq = T / ciclo
    mu = N * f_maq
    print(f"Fallas esperadas por maquina en {T:.0f} h = {f_maq:.2f} ; flota de {N} = {mu:.2f}")
    # Simulacion de renovacion
    rng2 = random.Random(SEMILLA + 1)
    n_sim = 4000
    tot = []
    for _ in range(n_sim):
        fallas = 0
        for _m in range(N):
            t = 0.0
            while True:
                t += sorteo(rng2)
                if t >= T:
                    break
                fallas += 1
                t += MTTR
        tot.append(fallas)
    media = sum(tot) / n_sim
    print(f"Simulacion de renovacion ({n_sim} misiones): fallas medias de la flota = {media:.2f} (Poisson {mu:.2f}) ; diferencia {100*(media-mu)/mu:+.2f} %")
    assert abs(media - mu) / mu < 0.03
    k95 = poisson_cuantil(mu, 0.95)
    k95_sim = sorted(tot)[int(0.95 * n_sim)]
    print(f"Repuestos para 95 % de confianza: Poisson = {k95} ; simulacion (percentil 95) = {k95_sim}")
    cobertura = sum(1 for x in tot if x <= k95) / n_sim
    print(f"Cobertura real de {k95} repuestos = {100*cobertura:.1f} %")
    # Efecto de beta: misma MTBF con beta = 1 (fallas aleatorias) frente a 1,8
    eta1 = mtbf / math.gamma(2.0)
    print(f"Con beta = 1 y la misma MTBF, eta = {eta1:.1f} h ; R(200 h) = {math.exp(-200/eta1):.4f} (frente a {math.exp(-(200/ETA)**BETA):.4f} con beta = 1,8)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
