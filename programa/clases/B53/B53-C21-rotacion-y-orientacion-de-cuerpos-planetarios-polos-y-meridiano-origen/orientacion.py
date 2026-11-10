#!/usr/bin/env python3
"""B53-C21: orientacion de un cuerpo con elementos ILUSTRATIVOS (no los de la IAU). Rotaciones activas, grados, dias.
alfa0 = 100 + 0.05 T, delta0 = 60 - 0.03 T (T en siglos julianos de 36525 d), W = 30 + 350.9 d.
Tolerancias: R R^T = I a 1e-12; W a 1e-9 grados."""
import math, platform

def Rx(a):
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    return [[1, 0, 0], [0, c, -s], [0, s, c]]

def Rz(a):
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]

def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def mv(a, v):
    return [sum(a[i][k] * v[k] for k in range(3)) for i in range(3)]

def orient(d):
    T = d / 36525.0
    a0, d0, w = 100 + 0.05 * T, 60 - 0.03 * T, 30 + 350.9 * d
    return mm(Rz(a0 + 90), mm(Rx(90 - d0), Rz(w))), a0, d0, w

def det(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

def compute():
    R, a0, d0, w = orient(0.0)
    Rt = [[R[j][i] for j in range(3)] for i in range(3)]
    p = mm(R, Rt)
    orth = max(abs(p[i][j] - (1 if i == j else 0)) for i in range(3) for j in range(3))
    z = mv(R, [0, 0, 1])
    polo = [math.cos(math.radians(d0)) * math.cos(math.radians(a0)), math.cos(math.radians(d0)) * math.sin(math.radians(a0)), math.sin(math.radians(d0))]
    pole = max(abs(a - b) for a, b in zip(z, polo))
    d = 2.75
    R2, _, _, w2 = orient(d)
    R0 = mm(Rz(100 + 90), mm(Rx(90 - 60), Rz(0)))  # W = 0 para referencia a d = 0 (polo casi fijo)
    Rw = lambda W: mm(Rz(100 + 0.05 * d / 36525 + 90), mm(Rx(90 - (60 - 0.03 * d / 36525)), Rz(W)))
    x0 = mv(Rw(0.0), [1, 0, 0]); y0 = mv(Rw(0.0), [0, 1, 0])
    x1 = mv(Rw(350.9 * d + 30), [1, 0, 0])
    ang = math.degrees(math.atan2(sum(a * b for a, b in zip(x1, y0)), sum(a * b for a, b in zip(x1, x0)))) % 360
    esperado = (350.9 * d + 30) % 360
    w_err = abs((ang - esperado + 180) % 360 - 180)
    _, a1, d1, _ = orient(36525.0)
    u0 = [math.cos(math.radians(60)) * math.cos(math.radians(100)), math.cos(math.radians(60)) * math.sin(math.radians(100)), math.sin(math.radians(60))]
    u1 = [math.cos(math.radians(d1)) * math.cos(math.radians(a1)), math.cos(math.radians(d1)) * math.sin(math.radians(a1)), math.sin(math.radians(d1))]
    prec_num = math.degrees(math.acos(max(-1.0, min(1.0, sum(a * b for a, b in zip(u0, u1))))))
    prec_ana = math.hypot(0.03, 0.05 * math.cos(math.radians(60)))
    return dict(orth=orth, det=det(R), pole=pole, P_d=360 / 350.9, P_h=360 / 350.9 * 24, w_err=w_err, w_ade=(350.9 * d) % 360,
                prec_num=prec_num, prec_ana=prec_ana, km01=math.radians(0.1) * 1000.0)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"ortogonalidad max|R R^T - I| = {r['orth']:.2e} ; det = {r['det']:.12f} ; error del eje frente al polo = {r['pole']:.2e}")
    print(f"periodo = {r['P_d']:.6f} d = {r['P_h']:.4f} h ; error de W tras 2.75 d = {r['w_err']:.2e} grados")
    print(f"precesion en un siglo: numerica {r['prec_num']:.6f} grados ; analitica {r['prec_ana']:.6f} grados")
    assert r["orth"] < 1e-12 and abs(r["det"] - 1) < 1e-12 and r["pole"] < 1e-12 and r["w_err"] < 1e-9 and abs(r["prec_num"] - r["prec_ana"]) < 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
