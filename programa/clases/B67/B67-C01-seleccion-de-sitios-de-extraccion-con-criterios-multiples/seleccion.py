"""B67-C01: seleccion multicriterio de sitios de extraccion (datos SINTETICOS).

Siete sitios inventados con cuatro criterios. Se normalizan (min-max), se pondera,
se busca el frente de Pareto y se mide la robustez del orden frente a pesos
aleatorios (Monte Carlo con semilla fija).
Unidades: reserva [kt de agua equivalente], pendiente [grados], iluminacion
[% del ano con sol], riesgo [indice adimensional 0-10].
Requiere solo numpy.
"""
import sys
import numpy as np

SITIOS = ["S1", "S2", "S3", "S4", "S5", "S6", "S7"]
# columnas: reserva (max), pendiente (min), iluminacion (max, energia), riesgo (min)
X = np.array([
    [120.0, 12.0, 20.0, 6.0],
    [ 80.0,  4.0, 55.0, 3.0],
    [200.0, 18.0, 10.0, 8.0],
    [ 95.0,  6.0, 40.0, 4.0],
    [ 60.0,  5.0, 60.0, 5.0],
    [150.0, 10.0, 30.0, 7.0],
    [ 90.0,  7.0, 35.0, 5.0],
])
SENTIDO = np.array([+1, -1, +1, -1])  # +1: mas es mejor
NOMBRES = ["reserva", "pendiente", "iluminacion", "riesgo"]
W0 = np.array([0.40, 0.20, 0.20, 0.20])


def normalizar(x):
    """min-max a [0,1] con 1 = mejor."""
    lo, hi = x.min(axis=0), x.max(axis=0)
    z = (x - lo) / (hi - lo)
    return np.where(SENTIDO > 0, z, 1.0 - z)


def puntaje(x, w):
    return normalizar(x) @ w


def pareto(z):
    """indices no dominados (z: mayor es mejor)."""
    n = len(z)
    res = []
    for i in range(n):
        dom = any(np.all(z[j] >= z[i]) and np.any(z[j] > z[i]) for j in range(n) if j != i)
        if not dom:
            res.append(i)
    return res


def main():
    print(f"Python {sys.version.split()[0]} ; numpy {np.__version__}")
    print("DATOS SINTETICOS (inventados para la clase; no son sitios reales)")
    z = normalizar(X)
    s = puntaje(X, W0)
    orden = np.argsort(-s)
    print("Pesos base:", {k: float(v) for k, v in zip(NOMBRES, W0)})
    print("sitio  puntaje  rango")
    rango = np.empty(len(s), int)
    rango[orden] = np.arange(1, len(s) + 1)
    for i, n in enumerate(SITIOS):
        print(f"  {n}    {s[i]:.4f}    {rango[i]}")
    fp = pareto(z)
    print("Frente de Pareto:", [SITIOS[i] for i in fp])

    # invariancia afin: cambiar unidades (reserva en t, pendiente en rad) no cambia el orden
    X2 = X * np.array([1000.0, np.pi / 180, 1.0, 1.0]) + np.array([0, 0, 5.0, 0])
    assert np.array_equal(np.argsort(-puntaje(X2, W0)), orden), "el orden depende de las unidades"
    print("Invariancia a cambios de unidades: orden identico (comprobado)")

    # el ganador por suma ponderada pertenece al frente de Pareto
    assert orden[0] in fp
    # Monte Carlo de pesos (Dirichlet(1,1,1,1)), semilla fija
    rng = np.random.default_rng(67)
    N = 20000
    W = rng.dirichlet(np.ones(4), size=N)
    S = z @ W.T  # (sitios, N)
    primero = np.argmax(S, axis=0)
    frec = np.bincount(primero, minlength=len(SITIOS)) / N
    print(f"Monte Carlo de pesos (N={N}, semilla 67): frecuencia de ser el primero")
    for n, f in zip(SITIOS, frec):
        print(f"  {n}: {f:.3f}")
    assert abs(frec.sum() - 1) < 1e-12
    # sitios dominados nunca pueden ser primeros
    dom = [i for i in range(len(SITIOS)) if i not in fp]
    assert all(frec[i] == 0 for i in dom)
    print("Sitios dominados:", [SITIOS[i] for i in dom], "-> frecuencia 0 (comprobado)")
    # sensibilidad: peso de la reserva que hace cambiar de ganador
    barrido = np.linspace(0, 1, 101)
    gan = []
    for a in barrido:
        w = np.array([a] + [(1 - a) / 3] * 3)
        gan.append(SITIOS[int(np.argmax(z @ w))])
    cambios = [(round(float(barrido[k]), 2), gan[k - 1], gan[k]) for k in range(1, 101) if gan[k] != gan[k - 1]]
    print("Cambios de ganador al subir el peso de la reserva (resto repartido igual):", cambios)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
