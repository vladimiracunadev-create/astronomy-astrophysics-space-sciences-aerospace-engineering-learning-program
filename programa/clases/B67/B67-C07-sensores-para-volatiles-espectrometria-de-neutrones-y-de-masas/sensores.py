"""B67-C07: sensores de volatiles, ambos con datos SINTETICOS y modelo ilustrativo.

A) Espectrometro de neutrones: tasa de neutrones epitermicos
       C(w) = C0 / (1 + a w)          [cuentas/s], w = hidrogeno equivalente en agua [% masa]
   C0 = 20 cuentas/s y a = 0,05 por % son INVENTADOS (relacion monotona decreciente
   con la forma cualitativa publicada: menos neutrones epitermicos donde hay mas hidrogeno).
   Cuentas ~ Poisson. Se invierte  w = (C0/C - 1)/a  y se propaga la incertidumbre.
B) Espectrometro de masas: espectro = A @ x + ruido, con A matriz de patrones de
   fragmentacion INVENTADOS (columnas = especies, filas = canales m/z). Se resuelve por
   minimos cuadrados ponderados con peso 1/varianza de Poisson.
Requiere solo numpy.
"""
import sys
import numpy as np

C0, A_N = 20.0, 0.05


def tasa(w):
    return C0 / (1 + A_N * np.asarray(w, float))


def invertir(c):
    return (C0 / c - 1) / A_N


def sigma_w(w, t):
    """propagacion: sigma_C = sqrt(C/t) ; dw/dC = -C0/(a C^2)."""
    c = tasa(w)
    return (C0 / (A_N * c ** 2)) * np.sqrt(c / t)


ESPECIES = ["H2O", "CO2", "CH4", "NH3", "H2S"]
CANALES = [16, 17, 18, 32, 34, 44]
# patron de cada especie en cada canal (normalizado a 1 en su canal principal); INVENTADO
A_MS = np.array([
    # H2O   CO2   CH4   NH3   H2S
    [0.01, 0.00, 1.00, 0.80, 0.00],   # m/z 16
    [0.23, 0.00, 0.10, 1.00, 0.00],   # 17
    [1.00, 0.00, 0.00, 0.02, 0.00],   # 18
    [0.00, 0.00, 0.00, 0.00, 0.44],   # 32
    [0.00, 0.00, 0.00, 0.00, 1.00],   # 34
    [0.00, 1.00, 0.00, 0.00, 0.00],   # 44
])


def main():
    print(f"Python {sys.version.split()[0]} ; numpy {np.__version__}")
    print("DATOS SINTETICOS: modelos de respuesta inventados; no son de un instrumento real")
    rng = np.random.default_rng(6707)
    print("A) Neutrones epitermicos")
    print("w [%]   C [cuentas/s]  depresion [%]  sigma_w a 1 h [%]  sigma_w MC [%]  sesgo MC [%]")
    for w in (0.5, 1.0, 3.0, 10.0):
        t = 3600.0
        c = float(tasa(w))
        dep = 100 * (1 - c / C0)
        sim = invertir(rng.poisson(c * t, size=200000) / t)
        print(f"{w:5.1f}   {c:8.4f}       {dep:6.2f}        {float(sigma_w(w, t)):7.4f}           {sim.std():7.4f}        {sim.mean() - w:+.4f}")
        assert abs(sim.std() - float(sigma_w(w, t))) / float(sigma_w(w, t)) < 0.03
    # tiempo para detectar w con 3 sigma sobre w=0
    print("Tiempo de integracion para detectar w con 3 sigma sobre el fondo seco (w=0):")
    for w in (0.5, 1.0, 2.0):
        # depresion C0 - C(w) >= 3 sqrt(C0 / t)  -> t = 9 C0 / (C0 - C)^2
        t = 9 * C0 / (C0 - float(tasa(w))) ** 2
        print(f"  w = {w:3.1f} %  ->  t = {t:8.1f} s ({t / 3600:.2f} h)")
    assert abs(9 * C0 / (C0 - float(tasa(1.0))) ** 2 - 9 * C0 / (C0 * (1 - 1 / 1.05)) ** 2) < 1e-6
    # la relacion es no lineal: saturacion
    s = [float(tasa(w)) for w in (0, 10, 20, 40)]
    assert all(s[i] > s[i + 1] for i in range(3))
    print("B) Espectrometria de masas: desmezcla de 5 especies en 6 canales")
    cond = np.linalg.cond(A_MS)
    print(f"Numero de condicion de la matriz de patrones: {cond:.1f}")
    x_true = np.array([800.0, 120.0, 60.0, 25.0, 15.0])  # cuentas por canal principal (SINTETICO)
    y0 = A_MS @ x_true
    W = 1 / np.maximum(y0, 1.0)
    cov = np.linalg.inv(A_MS.T @ (W[:, None] * A_MS))
    sd = np.sqrt(np.diag(cov))
    est = np.empty((20000, 5))
    est2 = np.empty((20000, 5))
    M0 = np.linalg.solve(A_MS.T @ (W[:, None] * A_MS), A_MS.T * W)   # pesos fijados con el modelo
    for k in range(20000):
        y = rng.poisson(y0)
        Wk = 1 / np.maximum(y, 1.0)                                     # pesos tomados de lo observado
        est[k] = np.linalg.solve(A_MS.T @ (Wk[:, None] * A_MS), A_MS.T @ (Wk * y))
        est2[k] = M0 @ y
    print("especie  verdadero  media(pesos observados)  media(pesos del modelo)  sigma predicha  sigma MC")
    for i, e in enumerate(ESPECIES):
        print(f"  {e:4s}    {x_true[i]:7.1f}     {est[:, i].mean():9.2f}               {est2[:, i].mean():9.2f}            {sd[i]:7.2f}       {est2[:, i].std():7.2f}")
        assert abs(est2[:, i].mean() - x_true[i]) < 4 * sd[i] / np.sqrt(20000)   # insesgado
        assert abs(est2[:, i].std() - sd[i]) / sd[i] < 0.05
        assert abs(est[:, i].mean() - x_true[i]) < 0.06 * x_true[i]            # sesgo acotado
    # sin el canal m/z 17 no se separan CH4 y NH3: la matriz pierde rango
    A2 = np.delete(A_MS, 1, axis=0)
    r1, r2 = np.linalg.matrix_rank(A_MS), np.linalg.matrix_rank(A2)
    print(f"Rango de la matriz de patrones: {r1} con los 6 canales ; {r2} sin el canal m/z 17 (5 especies)")
    assert r1 == 5 and r2 == 4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
