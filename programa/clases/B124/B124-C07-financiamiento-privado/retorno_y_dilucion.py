#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B124-C07: valor actual neto, tasa interna de retorno y dilucion en rondas, con datos SINTETICOS.

CONTENIDO EDUCATIVO: no es asesoria financiera ni de inversion. Flujos, valoraciones y rondas son SINTETICOS; ningun numero viene de un mercado real.
Parte 1: flujos de caja anuales F_t (t = 0..5) en millones de unidades monetarias sinteticas (Mum). VAN(r) = sum F_t / (1 + r)^t.
La TIR es la tasa con VAN = 0; se calcula por biseccion y se contrasta con el metodo de Newton. MOIC = suma de entradas / suma de salidas.
Parte 2: tabla de capitalizacion con acciones. Fundadores: 1 000 000 de acciones. Semilla: 2.0 Mum con pre-money 8.0. Serie A: 10.0 Mum con
pre-money 40.0 y bolsa de opciones del 10 % del total posterior (creada antes de la ronda, la diluyen los accionistas existentes).
Tolerancias: |VAN(TIR)| < 1e-9; biseccion frente a Newton < 1e-9; participacion por acciones frente al producto de factores < 1e-12;
precio por accion x acciones posteriores = valoracion posterior (< 1e-6).
"""
import platform

FLUJOS = [-100.0, -40.0, 30.0, 70.0, 90.0, 110.0]
TASA = 0.12


def van(r, f=FLUJOS):
    return sum(x / (1 + r) ** t for t, x in enumerate(f))


def dvan(r, f=FLUJOS):
    return sum(-t * x / (1 + r) ** (t + 1) for t, x in enumerate(f))


def tir_biseccion(lo=-0.9, hi=5.0):
    for _ in range(200):
        mid = (lo + hi) / 2
        if van(lo) * van(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def tir_newton(r=0.1):
    for _ in range(100):
        r = r - van(r) / dvan(r)
    return r


def captabla():
    fund = 1_000_000.0
    pre1, inv1 = 8.0, 2.0
    precio1 = pre1 * 1e6 / fund  # um por accion
    nuevas1 = inv1 * 1e6 / precio1
    e = fund + nuevas1
    pre2, inv2, pool = 40.0, 10.0, 0.10
    post2 = pre2 + inv2
    p_inv2, p_pool = inv2 / post2, pool
    s_post = e / (1 - p_inv2 - p_pool)
    nuevas2, nuevas_pool = p_inv2 * s_post, p_pool * s_post
    precio2 = post2 * 1e6 / s_post
    return dict(fund=fund, semilla=nuevas1, e=e, s_post=s_post, A=nuevas2, pool=nuevas_pool, precio1=precio1, precio2=precio2, post2=post2,
                pre_efectivo=(1 - p_inv2 - p_pool) * post2)


def run():
    tb, tn = tir_biseccion(), tir_newton()
    ent = sum(x for x in FLUJOS if x > 0)
    sal = -sum(x for x in FLUJOS if x < 0)
    c = captabla()
    f_fund = c["fund"] / c["s_post"]
    f_formula = (8.0 / 10.0) * (1 - 10.0 / 50.0 - 0.10)
    f_semilla = c["semilla"] / c["s_post"]
    f_A = c["A"] / c["s_post"]
    f_pool = c["pool"] / c["s_post"]
    acum, pb = 0.0, None
    for t, x in enumerate(FLUJOS):
        antes = acum
        acum += x
        if pb is None and acum >= 0 and t > 0:
            pb = t - 1 + (-antes) / x
    return {"van12": van(TASA), "tir_b": tb, "tir_n": tn, "van_tir": abs(van(tb)), "dif_tir": abs(tb - tn), "moic": ent / sal, "ent": ent, "sal": sal,
            "payback": pb if pb is not None else -1.0, "f_fund": f_fund, "f_formula": f_formula, "dif_part": abs(f_fund - f_formula),
            "f_semilla": f_semilla, "f_A": f_A, "f_pool": f_pool, "suma_f": f_fund + f_semilla + f_A + f_pool, "precio1": c["precio1"], "precio2": c["precio2"],
            "post_chk": abs(c["precio2"] * c["s_post"] / 1e6 - c["post2"]), "pre_ef": c["pre_efectivo"], "s_post": c["s_post"], "e": c["e"],
            "tir_pct": 100 * tb, "tirn_pct": 100 * tn, "fund_pct": 100 * f_fund, "semilla_pct": 100 * f_semilla, "A_pct": 100 * f_A,
            "pool_pct": 100 * f_pool, "form_pct": 100 * f_formula}


def main():
    R = run()
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Parte 1 - flujos SINTETICOS (Mum) t = 0..5:", FLUJOS)
    print(f"  VAN al {100 * TASA:.0f} % = {R['van12']:.4f} Mum ; TIR (biseccion) = {100 * R['tir_b']:.4f} % ; TIR (Newton) = {100 * R['tir_n']:.4f} % ; diferencia = {R['dif_tir']:.1e}")
    print(f"  |VAN(TIR)| = {R['van_tir']:.1e} ; MOIC = {R['ent']:.0f}/{R['sal']:.0f} = {R['moic']:.3f} ; recuperacion simple = {R['payback']:.3f} anios")
    print("Parte 2 - tabla de capitalizacion SINTETICA")
    print(f"  precio semilla = {R['precio1']:.2f} um/accion ; acciones tras semilla = {R['e']:.0f}")
    print(f"  serie A: acciones posteriores = {R['s_post']:.1f} ; precio = {R['precio2']:.4f} um/accion ; pre-money efectivo para los existentes = {R['pre_ef']:.1f} Mum")
    print(f"  participaciones: fundadores {100 * R['f_fund']:.2f} % ; semilla {100 * R['f_semilla']:.2f} % ; serie A {100 * R['f_A']:.2f} % ; bolsa {100 * R['f_pool']:.2f} % ; suma = {R['suma_f']:.6f}")
    print(f"  fundadores por producto de factores = {100 * R['f_formula']:.2f} % ; diferencia = {R['dif_part']:.1e} ; precio x acciones - valoracion posterior = {R['post_chk']:.1e}")
    assert R["van_tir"] < 1e-9 and R["dif_tir"] < 1e-9
    assert R["dif_part"] < 1e-12 and R["post_chk"] < 1e-6 and abs(R["suma_f"] - 1) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
