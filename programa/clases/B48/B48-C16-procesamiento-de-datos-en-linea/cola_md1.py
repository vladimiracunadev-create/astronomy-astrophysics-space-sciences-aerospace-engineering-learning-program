"""Reducción en línea como cola M/D/1 y tasa de datos de la cámara.

Datos: cuadro de 4096 x 4096 píxeles de 2 bytes cada 30 s; reducción de 20 s por cuadro: ILUSTRATIVOS
(no son los de ninguna cámara). No se consultó ninguna fuente externa.
Modelo: llegadas de Poisson (tasa lambda = 1/30 s^-1) y servicio determinista D = 20 s; ocupación rho = lambda D;
espera en cola Wq = rho D / (2 (1 - rho)); tiempo total W = Wq + D.
Segunda vía: recursión de Lindley con 600000 trabajos y semilla 20261109.
Supuestos: un solo procesador, sin prioridades; llegadas aleatorias (en un programa real la cadencia es fija).
Tolerancia: espera media simulada a menos del 3 % de la analítica.
"""
import random

PIX = 4096 * 4096
BYTES = 2
CAD = 30.0
D = 20.0
N = 600000


def wq(rho, d=D):
    return rho * d / (2 * (1 - rho))


def simula(lam, d=D, n=N):
    rng = random.Random(20261109)
    w = 0.0
    tot = 0.0
    for _ in range(n):
        tot += w
        a = rng.expovariate(lam)
        w = max(0.0, w + d - a)
    return tot / n


def calc():
    lam = 1 / CAD
    rho = lam * D
    out = {}
    for fac, nombre in ((1.0, "base"), (1.4, "carga alta")):
        l = lam * fac
        r = l * D
        out[nombre] = dict(rho=r, teo=wq(r), sim=simula(l))
    mb = PIX * BYTES / 1e6
    return dict(rho=rho, mb=mb, tasa=mb / CAD, noche=mb * 36000 / CAD / 1000, casos=out)


def main():
    Q = calc()
    print(f"Cuadro = {Q['mb']:.3f} MB; tasa = {Q['tasa']:.4f} MB/s; en 10 h = {Q['noche']:.2f} GB")
    for k, v in Q["casos"].items():
        print(f"{k}: rho = {v['rho']:.4f} | espera en cola analítica {v['teo']:.3f} s | simulada {v['sim']:.3f} s")
    for v in Q["casos"].values():
        assert abs(v["sim"] / v["teo"] - 1) < 0.03
    assert abs(Q["rho"] - 2 / 3) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
