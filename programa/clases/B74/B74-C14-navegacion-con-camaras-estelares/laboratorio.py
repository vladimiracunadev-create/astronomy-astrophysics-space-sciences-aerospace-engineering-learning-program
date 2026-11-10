#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C14: actitud a partir de vectores de estrellas (TRIAD y problema de Wahba por SVD).

Todo SINTETICO: estrellas simuladas (direcciones unitarias aleatorias dentro de un campo de vision circular de 8 grados de semiangulo centrado en
el eje optico), actitud verdadera aleatoria. Cada vector medido se perturba con ruido transversal de 5 arcsec por eje (ILUSTRATIVO). Metodos: TRIAD
con las dos primeras estrellas, y Wahba por descomposicion en valores singulares (Markley) con todas. 2000 realizaciones por caso (semilla 47).
Se reporta la desviacion estandar (arcsec) del error de actitud sobre los ejes transversales al eje optico (x, y) y sobre el eje optico (z, giro).
Tolerancias: con N estrellas el error transversal escala como 1/sqrt(N) (cociente a N=20 vs N=5 entre 0.45 y 0.55 de su valor 0.5);
el error de giro alrededor del eje optico es mas de 3 veces el transversal con N=20 en un campo estrecho. Con N=2 las desviaciones estandar estan dominadas por pares casi colineales (colas pesadas) y no se imponen tolerancias.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

SIG = 5.0 / 206264.806  # rad
FOV = math.radians(8.0)


def rot_aleatoria(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    w, x, y, z = q
    return np.array([[1 - 2*(y*y+z*z), 2*(x*y-z*w), 2*(x*z+y*w)],
                     [2*(x*y+z*w), 1 - 2*(x*x+z*z), 2*(y*z-x*w)],
                     [2*(x*z-y*w), 2*(y*z+x*w), 1 - 2*(x*x+y*y)]])


def estrellas_cuerpo(rng, n):
    """Vectores unitarios en el marco de la camara (eje optico = z) dentro del FOV circular."""
    cost = rng.uniform(math.cos(FOV), 1.0, n); ph = rng.uniform(0, 2*math.pi, n)
    s = np.sqrt(1 - cost**2)
    return np.column_stack([s*np.cos(ph), s*np.sin(ph), cost])


def triad(b1, b2, r1, r2):
    def terna(a, c):
        t1 = a; t2 = np.cross(a, c); t2 /= np.linalg.norm(t2); t3 = np.cross(t1, t2)
        return np.column_stack([t1, t2, t3])
    return terna(b1, b2) @ terna(r1, r2).T


def wahba(B, R):
    M = B.T @ R  # suma b_i r_i^T
    U, S, Vt = np.linalg.svd(M)
    d = np.linalg.det(U) * np.linalg.det(Vt)
    return U @ np.diag([1, 1, d]) @ Vt


def err_angulos(Aest, A):
    dA = Aest @ A.T
    v = np.array([dA[1, 2] - dA[2, 1], dA[2, 0] - dA[0, 2], dA[0, 1] - dA[1, 0]]) / 2
    return v


def main():
    rng = np.random.default_rng(47)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (estrellas y actitud SINTETICAS, semilla 47)",
           f"ruido = 5 arcsec por eje transversal ; FOV = {math.degrees(FOV):.0f} grados de semiangulo ; 2000 realizaciones por caso"]
    res = {}
    out.append("metodo   N    sigma_x [arcsec]  sigma_y [arcsec]  sigma_giro z [arcsec]")
    tab = {}
    for metodo, n in (("TRIAD", 2), ("SVD", 2), ("SVD", 5), ("SVD", 20)):
        e = []
        for _ in range(2000):
            A = rot_aleatoria(rng)  # inercial -> cuerpo
            bt = estrellas_cuerpo(rng, n)           # vectores 'verdaderos' en el cuerpo
            rI = (A.T @ bt.T).T                      # catalogo (inercial)
            bm = []
            for b in bt:
                t1 = np.cross(b, [1, 0, 0] if abs(b[0]) < 0.9 else [0, 1, 0]); t1 /= np.linalg.norm(t1); t2 = np.cross(b, t1)
                v = b + SIG * (rng.normal()*t1 + rng.normal()*t2); bm.append(v/np.linalg.norm(v))
            bm = np.array(bm)
            Aest = triad(bm[0], bm[1], rI[0], rI[1]) if metodo == "TRIAD" else wahba(bm, rI)
            e.append(err_angulos(Aest, A))
        e = np.array(e) * 206264.806
        sd = e.std(axis=0, ddof=1)
        tab[(metodo, n)] = sd
        out.append(f"{metodo:6s} {n:3d}  {sd[0]:15.2f}  {sd[1]:15.2f}  {sd[2]:18.2f}")
        res[f"{metodo}{n}_xy"] = float((sd[0] + sd[1]) / 2); res[f"{metodo}{n}_z"] = float(sd[2])
    r_ = (tab[("SVD", 20)][:2].mean()) / (tab[("SVD", 5)][:2].mean())
    out.append(f"Cociente de error transversal N=20 / N=5 = {r_:.3f} (esperado 0.500)")
    out.append(f"Cociente giro/transversal con N=20 = {tab[('SVD', 20)][2] / tab[('SVD', 20)][:2].mean():.2f} (campo estrecho: el giro alrededor del eje optico es peor)")
    res.update(razon=float(r_), razon_giro=float(tab[("SVD", 20)][2] / tab[("SVD", 20)][:2].mean()))
    ok = 0.45 < r_ < 0.55 and res["razon_giro"] > 3.0
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
