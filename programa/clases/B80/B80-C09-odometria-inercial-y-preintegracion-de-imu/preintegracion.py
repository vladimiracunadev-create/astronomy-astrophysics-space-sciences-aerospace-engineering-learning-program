#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B80-C09: preintegracion de IMU entre fotogramas clave (caso plano) y deriva de la odometria inercial.

Datos: SINTETICOS e ILUSTRATIVOS (semilla fija 80009); no proceden de ningun robot ni sensor real.
Modelo plano: estado (x, y, vx, vy, psi) en un sistema de navegacion fijo (gravedad ignorada en el plano horizontal); la IMU da la velocidad angular wz
y la fuerza especifica en el cuerpo (fx, fy) a 100 Hz. Entre dos fotogramas clave (1 s, 100 muestras) se calculan las variaciones relativas en el cuerpo del
primer fotograma (Forster et al., 2015-2016, preintegracion; idea consultada en el resumen de arXiv 1512.02363, 2026-11-10, y formulada aqui para el plano):
  dpsi = sum (w_k - bg) dt ; dv = sum R(psi_k - psi_0) (f_k - ba) dt ; dp = sum [dv_k dt + 0.5 R(...) (f_k - ba) dt^2].
Propagacion al mundo: psi_j = psi_i + dpsi ; v_j = v_i + R(psi_i) dv ; p_j = p_i + v_i T + R(psi_i) dp.
Verificaciones:
 (1) Independencia: integrar de nuevo con otro estado inicial (psi_i, v_i, p_i) da el mismo resultado que reusar (dpsi, dv, dp) sin recalcular la IMU.
 (2) Correccion de primer orden del sesgo del giroscopio: dv(bg + d) ~ dv(bg) + J d con J = d dv/d bg por diferencia finita; el error residual escala con d^2. Para ba la dependencia es lineal y la correccion es exacta.
 (3) Deriva de odometria inercial: con sesgo constante de giroscopio y de acelerometro, el error de posicion tras 10 s se compara con la cota cuadratica.
Tolerancias: (1) 1e-12; (2) cociente de errores residuales entre d y d/2 debe ser cercano a 4 (entre 3 y 5); el residuo de la correccion de ba debe ser < 1e-6.
"""
from __future__ import annotations
import math, platform, random

DT, M = 0.01, 100   # 1 s por intervalo
BG0, BA0 = 0.002, (0.01, -0.02)   # sesgos usados en la preintegracion (ilustrativos)


def R(a):
    c, s = math.cos(a), math.sin(a)
    return [[c, -s], [s, c]]


def rv(a, v):
    r = R(a)
    return (r[0][0] * v[0] + r[0][1] * v[1], r[1][0] * v[0] + r[1][1] * v[1])


def genera(seed=80009, n=M):
    rnd = random.Random(seed)
    w = [0.3 + 0.1 * math.sin(2 * math.pi * k * DT) + rnd.gauss(0, 0.002) for k in range(n)]
    f = [(0.5 + rnd.gauss(0, 0.02), 0.1 * math.cos(2 * math.pi * k * DT) + rnd.gauss(0, 0.02)) for k in range(n)]
    return w, f


def preint(w, f, bg, ba):
    dpsi = 0.0
    dv = [0.0, 0.0]
    dp = [0.0, 0.0]
    for k in range(len(w)):
        a = rv(dpsi, (f[k][0] - ba[0], f[k][1] - ba[1]))
        dp[0] += dv[0] * DT + 0.5 * a[0] * DT * DT
        dp[1] += dv[1] * DT + 0.5 * a[1] * DT * DT
        dv[0] += a[0] * DT
        dv[1] += a[1] * DT
        dpsi += (w[k] - bg) * DT
    return dpsi, tuple(dv), tuple(dp)


def propaga_mundo(psi_i, v_i, p_i, dpsi, dv, dp, T):
    dvw = rv(psi_i, dv)
    dpw = rv(psi_i, dp)
    return psi_i + dpsi, (v_i[0] + dvw[0], v_i[1] + dvw[1]), (p_i[0] + v_i[0] * T + dpw[0], p_i[1] + v_i[1] * T + dpw[1])


def directo(psi_i, v_i, p_i, w, f, bg, ba):
    psi, v, p = psi_i, list(v_i), list(p_i)
    for k in range(len(w)):
        a = rv(psi, (f[k][0] - ba[0], f[k][1] - ba[1]))
        p[0] += v[0] * DT + 0.5 * a[0] * DT * DT
        p[1] += v[1] * DT + 0.5 * a[1] * DT * DT
        v[0] += a[0] * DT
        v[1] += a[1] * DT
        psi += (w[k] - bg) * DT
    return psi, tuple(v), tuple(p)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    w, f = genera()
    print("Datos SINTETICOS (semilla 80009): 100 muestras a 100 Hz, intervalo de 1 s")
    pre = preint(w, f, BG0, BA0)
    print(f"Preintegracion (ba = {BA0}, bg = {BG0}): dpsi = {pre[0]:.6f} rad ; dv = ({pre[1][0]:.6f}, {pre[1][1]:.6f}) m/s ; dp = ({pre[2][0]:.6f}, {pre[2][1]:.6f}) m")
    # (1) independencia del estado inicial
    dmax = 0.0
    for psi_i, v_i, p_i in ((0.0, (0.0, 0.0), (0.0, 0.0)), (1.1, (2.0, -1.0), (10.0, 5.0)), (-2.0, (-3.0, 0.5), (-4.0, 7.0))):
        a = propaga_mundo(psi_i, v_i, p_i, *pre, 1.0)
        b = directo(psi_i, v_i, p_i, w, f, BG0, BA0)
        dmax = max(dmax, abs(a[0] - b[0]), *(abs(a[1][i] - b[1][i]) for i in range(2)), *(abs(a[2][i] - b[2][i]) for i in range(2)))
    print(f"(1) Diferencia maxima entre reutilizar la preintegracion y reintegrar con estados iniciales distintos = {dmax:.2e}")
    # (2) correccion de primer orden por cambio de sesgo del giroscopio (dv depende de forma no lineal de bg) y exactitud para ba (lineal)
    h = 1e-6
    base = preint(w, f, BG0, BA0)
    J = [(preint(w, f, BG0 + h, BA0)[1][i] - preint(w, f, BG0 - h, BA0)[1][i]) / (2 * h) for i in range(2)]
    print(f"(2) Jacobiano d(dv)/d(bg) = ({J[0]:.6f}, {J[1]:.6f}) m/s por rad/s")
    print("    delta bg [rad/s]   error sin correccion [m/s]   error con correccion lineal [m/s]")
    res = []
    for d in (0.08, 0.04, 0.02):
        nuevo = preint(w, f, BG0 + d, BA0)[1]
        e0 = math.hypot(nuevo[0] - base[1][0], nuevo[1] - base[1][1])
        e1 = math.hypot(nuevo[0] - (base[1][0] + J[0] * d), nuevo[1] - (base[1][1] + J[1] * d))
        res.append(e1)
        print(f"    {d:15.2f} {e0:28.6f} {e1:31.3e}")
    ratio = res[0] / res[1]
    print(f"    cociente de errores residuales (d = 0.08 frente a 0.04) = {ratio:.2f} (cuadratico: 4)")
    # para el sesgo del acelerometro dv es lineal: la correccion es exacta
    Ja = [(preint(w, f, BG0, (BA0[0] + h, BA0[1]))[1][i] - preint(w, f, BG0, (BA0[0] - h, BA0[1]))[1][i]) / (2 * h) for i in range(2)]
    nuevo_a = preint(w, f, BG0, (BA0[0] + 0.4, BA0[1]))[1]
    ea = math.hypot(nuevo_a[0] - (base[1][0] + Ja[0] * 0.4), nuevo_a[1] - (base[1][1] + Ja[1] * 0.4))
    print(f"    Para delta ba_x = 0.4 m/s2 la correccion lineal deja un residuo de {ea:.2e} m/s (dv es lineal en ba)")
    # (3) deriva de odometria inercial a 10 s con sesgos constantes (sin ruido) y sin correccion
    T = 10.0
    ba_err, bg_err = 0.02, 0.002
    # error de posicion por sesgo de acelerometro: 0.5 ba T^2 ; el de giroscopio gira la aceleracion: orden 0.5 a bg T^3/3 con a = 0.5 m/s2 (cota)
    cota_a = 0.5 * ba_err * T ** 2
    cota_g = 0.5 * 0.5 * bg_err * T ** 3 / 3.0
    print(f"(3) Con ba = {ba_err} m/s2 y bg = {bg_err} rad/s: deriva por acelerometro {cota_a:.3f} m ; por giroscopio (cota, a = 0.5 m/s2) {cota_g:.3f} m tras {T:.0f} s")
    assert dmax < 1e-12
    assert 3.0 < ratio < 5.0
    assert ea < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
