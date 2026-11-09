"""Alertas de observabilidad: regla k de m, falsas alarmas y retardo de detección; métricas desde registros.

Datos: SINTÉTICOS. Métrica normal (0, 1) en régimen sano; umbral en 2,0 sigmas; avería que desplaza la media
+3,0 sigmas; regla 3 de 5. Registros de texto generados con el formato 'clave=valor'. No se consultó ninguna
fuente externa ni se modela un sistema real de monitorización.
Modelo: probabilidad de superar el umbral p = 1 - Phi(u - desplazamiento); alarma si en una ventana de m muestras
al menos k superan: P = suma_{j>=k} C(m,j) p^j (1-p)^(m-j) (ventanas disjuntas); retardo medio por simulación.
Segunda vía: simulación de 300000 ventanas disjuntas y de 20000 averías con semilla 20261109.
Supuestos: muestras independientes y gaussianas; la regla se evalúa sobre ventanas deslizantes en el retardo.
Tolerancia: 4 desviaciones binomiales; el recuento de registros debe ser exacto.
"""
import math
import random
import re
from statistics import NormalDist

U, DES = 2.0, 3.0
K, M = 3, 5


def p_ventana(p):
    return sum(math.comb(M, j) * p ** j * (1 - p) ** (M - j) for j in range(K, M + 1))


def retardo(rng):
    cola = []
    n = 0
    while True:
        n += 1
        cola.append(rng.gauss(DES, 1) > U)
        cola = cola[-M:]
        if sum(cola) >= K:
            return n


def registros(rng, n=1000):
    lineas, niveles = [], ["INFO", "WARN", "ERROR"]
    cuenta = {k: 0 for k in niveles}
    for i in range(n):
        nv = rng.choices(niveles, weights=[90, 8, 2])[0]
        cuenta[nv] += 1
        lineas.append(f"t={i} nivel={nv} modulo=domo latencia_ms={rng.randint(1, 50)}")
    pat = re.compile(r"nivel=(\w+)")
    cont = {k: 0 for k in niveles}
    for l in lineas:
        cont[pat.search(l).group(1)] += 1
    return cuenta, cont


def calc():
    rng = random.Random(20261109)
    nd = NormalDist()
    p0 = 1 - nd.cdf(U)
    p1 = 1 - nd.cdf(U - DES)
    fa_teo, det_teo = p_ventana(p0), p_ventana(p1)
    n = 300000
    fa_sim = sum(1 for _ in range(n) if sum(rng.gauss(0, 1) > U for _ in range(M)) >= K) / n
    det_sim = sum(1 for _ in range(n) if sum(rng.gauss(DES, 1) > U for _ in range(M)) >= K) / n
    ret = [retardo(rng) for _ in range(20000)]
    cuenta, cont = registros(rng)
    return dict(p0=p0, p1=p1, fa_teo=fa_teo, fa_sim=fa_sim, det_teo=det_teo, det_sim=det_sim, n=n, ret=sum(ret) / len(ret), ret_max=max(ret), cuenta=cuenta, cont=cont,
                una_teo=p0, una_ret=1 / p1)


def main():
    Q = calc()
    print(f"p sano = {Q['p0']:.5f}; p con avería = {Q['p1']:.5f}")
    print(f"Falsa alarma por ventana de 5: analítica {Q['fa_teo']:.3e} | simulada {Q['fa_sim']:.3e}")
    print(f"Detección por ventana de 5: analítica {Q['det_teo']:.5f} | simulada {Q['det_sim']:.5f}")
    print(f"Retardo medio de detección (ventana deslizante) = {Q['ret']:.3f} muestras (máximo {Q['ret_max']}); regla de 1 muestra = {Q['una_ret']:.3f}")
    print(f"Registros: generados {Q['cuenta']} | contados {Q['cont']}")
    sig = math.sqrt(Q["det_teo"] * (1 - Q["det_teo"]) / Q["n"])
    assert abs(Q["det_teo"] - Q["det_sim"]) < 4 * sig
    assert abs(Q["fa_teo"] - Q["fa_sim"]) < 4 * math.sqrt(Q["fa_teo"] / Q["n"]) + 1e-9
    assert Q["cuenta"] == Q["cont"]
    assert 3 <= Q["ret"] < 5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
