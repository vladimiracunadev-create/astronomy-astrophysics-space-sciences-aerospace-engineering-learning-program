"""B67-C05: variograma y kriging ordinario sobre un campo SINTETICO de hielo.

Campo verdadero w(x,y) [fraccion masica, adimensional] generado con covarianza
exponencial conocida:  C(h) = s2 * exp(-h/a)  (s2 en [adim^2], a en [m]),
sobre una malla de 20 x 20 celdas de 100 m (2 km x 2 km), media constante m.
Variograma teorico: gamma(h) = c0 + (s2 - c0)(1 - exp(-h/a)) para h>0, gamma(0)=0.
Kriging ordinario: sistema [[Gamma, 1],[1^T, 0]] [lambda, mu]^T = [gamma0, 1]^T.
Varianza de kriging: s2_K = lambda^T gamma0 + mu.
Requiere solo numpy.
"""
import sys
import numpy as np

S2, RANGO, M0, NUGGET = 1.0e-4, 400.0, 0.03, 0.0   # sigma2 = (1 %)^2 ; a = 400 m
N = 20
PASO = 100.0


def gamma(h, s2=S2, a=RANGO, c0=NUGGET):
    h = np.asarray(h, float)
    g = c0 + (s2 - c0) * (1 - np.exp(-h / a))
    return np.where(h > 0, g, 0.0)


def malla():
    xs = (np.arange(N) + 0.5) * PASO
    X, Y = np.meshgrid(xs, xs)
    return np.column_stack([X.ravel(), Y.ravel()])


def dist(P, Q):
    return np.sqrt(((P[:, None, :] - Q[None, :, :]) ** 2).sum(-1))


def campo(rng):
    P = malla()
    C = S2 * np.exp(-dist(P, P) / RANGO)
    L = np.linalg.cholesky(C + 1e-12 * np.eye(len(P)))
    return P, M0 + L @ rng.standard_normal(len(P))


def krig(Pm, zm, Pn, s2=S2, a=RANGO, c0=NUGGET):
    n = len(Pm)
    G = np.zeros((n + 1, n + 1))
    G[:n, :n] = gamma(dist(Pm, Pm), s2, a, c0)
    G[:n, n] = G[n, :n] = 1.0
    g0 = gamma(dist(Pm, Pn), s2, a, c0)
    rhs = np.vstack([g0, np.ones((1, len(Pn)))])
    sol = np.linalg.solve(G, rhs)
    lam, mu = sol[:n], sol[n]
    est = lam.T @ zm
    var = (lam * g0).sum(0) + mu
    return est, np.maximum(var, 0.0), lam


def idw(Pm, zm, Pn, p=2.0):
    d = dist(Pn, Pm)
    d = np.maximum(d, 1e-9)
    w = 1 / d ** p
    return (w * zm).sum(1) / w.sum(1)


def main():
    print(f"Python {sys.version.split()[0]} ; numpy {np.__version__}")
    print("DATOS SINTETICOS: campo generado con covarianza exponencial conocida (semilla 6705)")
    rng = np.random.default_rng(6705)
    P, z = campo(rng)
    print(f"Campo verdadero: media = {100 * z.mean():.3f} %, desviacion = {100 * z.std():.3f} % (teorico {100 * np.sqrt(S2):.1f} %)")
    idx = rng.choice(len(P), size=40, replace=False)
    mask = np.zeros(len(P), bool)
    mask[idx] = True
    Pm, zm = P[mask], z[mask]
    Pn, zn = P[~mask], z[~mask]
    est, var, lam = krig(Pm, zm, Pn)
    # propiedades del kriging ordinario
    assert np.allclose(lam.sum(0), 1.0, atol=1e-9), "pesos no suman 1"
    e0, v0, _ = krig(Pm, zm, Pm[:5])
    assert np.allclose(e0, zm[:5], atol=1e-7) and np.all(v0 < 1e-9), "no es exacto en los datos"
    print("Pesos suman 1 (maximo |suma-1| = %.1e) ; exacto en los puntos de dato (varianza 0)" % np.abs(lam.sum(0) - 1).max())
    rmse_k = np.sqrt(np.mean((est - zn) ** 2))
    rmse_i = np.sqrt(np.mean((idw(Pm, zm, Pn) - zn) ** 2))
    rmse_m = np.sqrt(np.mean((zm.mean() - zn) ** 2))
    print(f"RMSE sobre 360 celdas no muestreadas [fraccion masica]: kriging = {rmse_k:.5f} ; IDW p=2 = {rmse_i:.5f} ; media global = {rmse_m:.5f}")
    cov = np.mean(np.abs(zn - est) <= 1.6449 * np.sqrt(var))
    print(f"Cobertura del intervalo al 90 % de kriging: {100 * cov:.1f} % ; desviacion media de kriging = {100 * np.sqrt(var).mean():.3f} %")
    assert rmse_k < rmse_m
    # validacion cruzada dejando uno fuera (sobre los 40 datos)
    err = []
    for i in range(len(Pm)):
        keep = np.arange(len(Pm)) != i
        e, v, _ = krig(Pm[keep], zm[keep], Pm[i:i + 1])
        err.append(((e[0] - zm[i]) ** 2) / max(v[0], 1e-12))
    print(f"Validacion cruzada (dejar uno fuera): media del error estandarizado al cuadrado = {np.mean(err):.2f} (ideal ~ 1)")
    # el variograma empirico recupera sigma2 y el rango
    d = dist(P, P)
    iu = np.triu_indices(len(P), 1)
    dif2 = 0.5 * (z[:, None] - z[None, :]) ** 2
    print("lag [m]  gamma empirico  gamma teorico")
    for h in (100.0, 200.0, 400.0, 800.0, 1200.0):
        sel = np.abs(d[iu] - h) < 1e-6
        if sel.sum() == 0:
            sel = np.abs(d[iu] - h) < 50
        print(f"  {h:6.0f}   {dif2[iu][sel].mean():.3e}     {float(gamma(h)):.3e}")
    # efecto del nugget mal especificado
    for c0 in (0.0, 0.5 * S2):
        e, v, _ = krig(Pm, zm, Pn, c0=c0)
        print(f"nugget={c0:.1e}: RMSE = {np.sqrt(np.mean((e - zn) ** 2)):.5f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
