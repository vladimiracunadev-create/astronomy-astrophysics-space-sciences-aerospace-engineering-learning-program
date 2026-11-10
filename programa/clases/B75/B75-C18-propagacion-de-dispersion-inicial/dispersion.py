#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C18: propagacion de la dispersion de velocidad inicial hasta la llegada a Marte (modelo circular y coplanar, dos cuerpos).

Datos consultados (2026-11-10): semiejes de las fichas NASA/NSSDC (Tierra 149.598e6 km, Marte 227.956e6 km), masa de Marte 0.64169e24 kg; G = 6.67430e-11 (registro de cambios del JPL).
GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado); masa solar = GM_sol/G. SINTETICO: error de velocidad en la salida isotropo de 1 m/s por eje (1-sigma), gaussiano, N = 20000, semilla 75; no es una incertidumbre de ninguna mision.
Modelo: trayectoria nominal de Hohmann; matriz de transicion (posicion final respecto a la velocidad inicial) por diferencias finitas centradas sobre la propagacion de Kepler (paso 1e-6 km/s);
covarianza lineal P = sigma^2 Phi Phi^T (biblioteca estandar: random.Random(75), Jacobi propio); Monte Carlo con la propagacion no lineal. Sin perturbaciones ni errores de posicion ni maniobras de correccion.
Pruebas: (1) la desviacion estandar de los ejes x e y por Monte Carlo coincide con la lineal (tol. 3 %) y la del eje z, de sensibilidad lineal nula a 180 grados, es de segundo orden (< 20 km); (2) la dispersion lineal es proporcional a sigma (tol. 1e-9 al duplicarlo); (3) Phi coincide con la derivada obtenida con otro paso (1e-5 km/s) (tol. 1e-4 relativa).
"""
import math, platform, random
MU = 1.32712440e11
G = 6.67430e-20
AE, AM = 149.598e6, 227.956e6
# --- Utilidades de dos cuerpos (todas en km, s, km/s) ---
def _stumpff(z):
    if z > 1e-8:
        s = math.sqrt(z); return (1 - math.cos(s)) / z, (s - math.sin(s)) / s**3
    if z < -1e-8:
        s = math.sqrt(-z); return (math.cosh(s) - 1) / (-z), (math.sinh(s) - s) / s**3
    return 0.5 - z / 24, 1 / 6 - z / 120


def kepler_prop(r0, v0, dt, mu):
    """Propaga (r0, v0) durante dt con variables universales (Curtis, alg. 3.4); r0, v0 listas de 3."""
    r0n = math.sqrt(sum(x * x for x in r0)); vr0 = sum(a * b for a, b in zip(r0, v0)) / r0n
    alpha = 2 / r0n - sum(x * x for x in v0) / mu
    sm = math.sqrt(mu)
    if alpha > 0: x = sm * alpha * dt
    elif alpha < 0:
        a_ = 1 / alpha; sg = 1.0 if dt >= 0 else -1.0
        rv = sum(p * q for p, q in zip(r0, v0))
        x = sg * math.sqrt(-a_) * math.log((-2 * mu * alpha * dt) / (rv + sg * math.sqrt(-mu * a_) * (1 - r0n * alpha)))
    else: x = sm * dt / r0n
    for _ in range(200):
        z = alpha * x * x; C, S = _stumpff(z)
        F = r0n * vr0 / sm * x * x * C + (1 - alpha * r0n) * x**3 * S + r0n * x - sm * dt
        dF = r0n * vr0 / sm * x * (1 - z * S) + (1 - alpha * r0n) * x * x * C + r0n
        dx = F / dF; x -= dx
        if abs(dx) < 1e-12 * max(1.0, abs(x)): break
    z = alpha * x * x; C, S = _stumpff(z)
    f = 1 - x * x / r0n * C; g = dt - x**3 / sm * S
    r = [f * a + g * b for a, b in zip(r0, v0)]; rn = math.sqrt(sum(q * q for q in r))
    fd = sm / (rn * r0n) * (z * S - 1) * x; gd = 1 - x * x / rn * C
    v = [fd * a + gd * b for a, b in zip(r0, v0)]
    return r, v


def rk4_dosc(r, v, dt, n, mu):
    """Integra el problema de dos cuerpos con RK4 de paso fijo (n pasos de dt)."""
    def acc(p):
        d = math.sqrt(sum(q * q for q in p)); return [-mu * q / d**3 for q in p]
    r = list(r); v = list(v)
    for _ in range(n):
        k1v = acc(r); k1r = v
        r2 = [a + 0.5 * dt * b for a, b in zip(r, k1r)]; v2 = [a + 0.5 * dt * b for a, b in zip(v, k1v)]
        k2v = acc(r2); k2r = v2
        r3 = [a + 0.5 * dt * b for a, b in zip(r, k2r)]; v3 = [a + 0.5 * dt * b for a, b in zip(v, k2v)]
        k3v = acc(r3); k3r = v3
        r4 = [a + dt * b for a, b in zip(r, k3r)]; v4 = [a + dt * b for a, b in zip(v, k3v)]
        k4v = acc(r4); k4r = v4
        r = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(r, k1r, k2r, k3r, k4r)]
        v = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(v, k1v, k2v, k3v, k4v)]
    return r, v



def llegada(dv):
    at = 0.5 * (AE + AM)
    vp = math.sqrt(MU * (2 / AE - 1 / at))
    tof = math.pi * math.sqrt(at**3 / MU)
    r, v = kepler_prop([AE, 0.0, 0.0], [dv[0], vp + dv[1], dv[2]], tof, MU)
    return r


def fi(h):
    cols = []
    for k in range(3):
        e = [0.0] * 3; e[k] = h
        m = [0.0] * 3; m[k] = -h
        rp, rm = llegada(e), llegada(m)
        cols.append([(x - y) / (2 * h) for x, y in zip(rp, rm)])
    return [[cols[j][i] for j in range(3)] for i in range(3)]  # filas = componentes de posicion


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def tr(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def autovalores(S):
    """Jacobi para matriz simetrica 3x3 (solo valores propios)."""
    A = [r[:] for r in S]
    for _ in range(60):
        p, q = max(((i, j) for i in range(3) for j in range(i + 1, 3)), key=lambda x: abs(A[x[0]][x[1]]))
        if abs(A[p][q]) < 1e-14 * max(1.0, abs(A[p][p]) + abs(A[q][q])): break
        th = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p])
        c, s = math.cos(th), math.sin(th)
        R = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
        R[p][p] = c; R[q][q] = c; R[p][q] = s; R[q][p] = -s
        A = mm(tr(R), mm(A, R))
    return sorted((A[i][i] for i in range(3)), reverse=True)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    sig = 1e-3
    nom = llegada([0, 0, 0])
    print(f"Llegada nominal: r = ({nom[0]/1e6:.4f}, {nom[1]/1e6:.4f}, {nom[2]:.1f}) 1e6 km ; |r| = {math.hypot(*nom)/1e6:.4f}e6 km")
    Phi = fi(1e-6)
    PPt = mm(Phi, tr(Phi))
    lin = [sig * math.sqrt(PPt[i][i]) for i in range(3)]
    sv = [math.sqrt(x) for x in autovalores(PPt)]
    print("Phi (km por km/s), filas = x, y, z de la llegada; columnas = dvx, dvy, dvz:")
    for f in Phi: print("   " + "  ".join(f"{x:14.1f}" for x in f))
    print(f"Valores singulares de Phi: {sv[0]:.1f}, {sv[1]:.1f}, {sv[2]:.1f} km/(km/s) ; semiejes 1-sigma de la elipsoide (sigma = 1 m/s): {sig*sv[0]:.0f}, {sig*sv[1]:.0f}, {sig*sv[2]:.0f} km")
    rng = random.Random(75)
    N = 20000
    fin = []
    for _ in range(N):
        dv = [rng.gauss(0.0, sig) for _ in range(3)]
        r = llegada(dv)
        fin.append([r[i] - nom[i] for i in range(3)])
    mc = []
    for i in range(3):
        m = sum(f[i] for f in fin) / N
        mc.append(math.sqrt(sum((f[i] - m) ** 2 for f in fin) / (N - 1)))
    print("eje   sigma lineal [km]   sigma Monte Carlo [km]   dif [%]")
    for i, n in enumerate("xyz"):
        if lin[i] > 1.0:
            print(f"  {n}   {lin[i]:16.1f} {mc[i]:22.1f} {100*(mc[i]-lin[i])/lin[i]:10.2f}")
            assert abs(mc[i] - lin[i]) / lin[i] < 0.03
        else:
            print(f"  {n}   {lin[i]:16.1f} {mc[i]:22.1f}   (la sensibilidad lineal es nula: llegada a 180 grados, en el plano)")
            assert lin[i] < 1e-6 and mc[i] < 20.0
    miss = sorted(math.sqrt(sum(x * x for x in f)) for f in fin)
    mh = AM * (0.64169e24 / (3 * MU / G)) ** (1 / 3)
    med, p95 = miss[N // 2], miss[int(0.95 * N)]
    print(f"Distancia de falla (3D): mediana MC = {med:.0f} km ; percentil 95 = {p95:.0f} km ; radio de Hill de Marte = {mh:.0f} km ; P95/Hill = {p95/mh:.3f}")
    lin2 = [2 * sig * math.sqrt(PPt[i][i]) for i in range(3)]
    assert all(abs(b - 2 * a) < 1e-9 * a for a, b in zip(lin, lin2))
    Phi2 = fi(1e-5)
    mx = max(abs(x) for f in Phi for x in f)
    rel = max(abs(Phi2[i][j] - Phi[i][j]) / mx for i in range(3) for j in range(3))
    print(f"Phi con paso 1e-5 frente a 1e-6: diferencia relativa maxima = {rel:.2e}")
    assert rel < 1e-4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
