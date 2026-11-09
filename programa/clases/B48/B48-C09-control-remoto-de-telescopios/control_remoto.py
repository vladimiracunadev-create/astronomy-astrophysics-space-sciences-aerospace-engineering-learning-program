"""Control remoto: retardo de propagación, tiempo de parada y falsos disparos del vigilante.

Datos: c = 299 792 458 m/s (valor exacto, NIST CODATA 2022, tabla local consultada el 2026-11-09). Distancia
de enlace 1200 km, índice de grupo de la fibra 1,468, pérdida de latidos 0,10, latido cada 1 s: ILUSTRATIVOS.
Modelo: retardo unidireccional = d n / c; el vigilante dispara tras k latidos perdidos seguidos; tasa de
disparos por latido = (1 - p) p^k (arranque de una racha de k pérdidas tras un latido recibido).
Segunda vía: simulación de 2 000 000 de latidos con semilla 20261109.
Supuestos: pérdidas independientes; sin congestión ni reintentos; tiempo de procesamiento nulo.
Tolerancia: 4 desviaciones de Poisson sobre el conteo esperado de disparos.
"""
import math
import random

C = 299_792_458.0
D = 1_200_000.0
N_FIBRA = 1.468
P = 0.10
LATIDOS = 2_000_000


def retardo(d=D, n=N_FIBRA):
    return d * n / C


def disparos(rng, p, k, n):
    racha = 0
    cuenta = 0
    for _ in range(n):
        if rng.random() < p:
            racha += 1
            if racha == k:
                cuenta += 1
        else:
            racha = 0
    return cuenta


def calc():
    t1 = retardo()
    rng = random.Random(20261109)
    out = {}
    for k in (3, 4):
        esp = LATIDOS * (1 - P) * P ** k
        sim = disparos(rng, P, k, LATIDOS)
        out[k] = dict(esp=esp, sim=sim, sig=math.sqrt(esp), parada=k * 1.0 + 2 * t1)
    return dict(t1=t1, rtt=2 * t1, k=out)


def main():
    R = calc()
    print(f"Retardo unidireccional = {R['t1'] * 1e3:.4f} ms; ida y vuelta = {R['rtt'] * 1e3:.4f} ms")
    for k, v in R["k"].items():
        print(f"k = {k}: disparos esperados {v['esp']:.1f} | simulados {v['sim']} (sigma {v['sig']:.1f}) | parada tras {v['parada']:.3f} s")
    for v in R["k"].values():
        assert abs(v["sim"] - v["esp"]) < 4 * v["sig"]
    assert abs(R["t1"] - 1_200_000 * 1.468 / C) < 1e-15
    assert R["k"][4]["esp"] < R["k"][3]["esp"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
