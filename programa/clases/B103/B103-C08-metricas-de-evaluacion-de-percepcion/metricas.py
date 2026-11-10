#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B103-C08: metricas de percepcion (deteccion, segmentacion, profundidad) sobre salidas SINTETICAS.

Todo es sintetico (semilla 103) y NO procede de ningun algoritmo real: 100 imagenes con cajas verdaderas de 10 a 100 px (log-uniforme,
media de 3 por imagen) y un "detector" simulado cuya probabilidad de acierto crece con el tamano, con cajas desplazadas un 10 % de su
tamano y confianzas generadas por el simulador; mascaras 64 x 64 con una clase rara (1 %); y profundidades de 4 a 40 m con error relativo
sigma_rel = Z * 0.3 / 168 (el modelo de B103-C03) mas un 2 % de valores atipicos (x1.5).
Definiciones usadas (propias, no copiadas de ninguna evaluacion): IoU de cajas = interseccion/union; acierto si IoU >= umbral y la verdad
no estaba ya asignada (asignacion voraz por confianza); precision = TP/(TP+FP); exhaustividad = TP/(TP+FN); F1 = 2PR/(P+R);
AP = area bajo la curva precision-exhaustividad con precision interpolada (envolvente monotona); error de profundidad: MAE, RMSE,
AbsRel = media(|z_hat - z|/z), delta1 = fraccion con max(z/z_hat, z_hat/z) < 1.25. Intervalos: remuestreo bootstrap de las imagenes (500).
Verificacion: un detector perfecto da AP = 1; la exactitud de un segmentador trivial es alta con IoU = 0 en la clase rara; el intervalo
se estrecha al aumentar las imagenes. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

NIMG = 100


def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[0] + a[2], b[0] + b[2]), min(a[1] + a[3], b[1] + b[3])
    inter = max(0.0, x2 - x1) * max(0.0, y2 - y1)
    return inter / (a[2] * a[3] + b[2] * b[3] - inter)


def simular(rng):
    gt, det = [], []
    for _ in range(NIMG):
        n = rng.poisson(3)
        cajas = []
        for _ in range(n):
            s = float(np.exp(rng.uniform(np.log(10), np.log(100))))
            cajas.append((rng.uniform(0, 600 - s), rng.uniform(0, 600 - s), s, s))
        gt.append(cajas)
        d = []
        for c in cajas:
            p = 1 / (1 + np.exp(-(c[2] - 25) / 10))
            if rng.uniform() < p:
                j = rng.normal(0, 0.10 * c[2], 4)
                d.append(((c[0] + j[0], c[1] + j[1], max(c[2] + j[2], 3), max(c[3] + j[3], 3)), float(rng.beta(6, 2))))
        for _ in range(rng.poisson(1.5)):
            s = float(np.exp(rng.uniform(np.log(10), np.log(100))))
            d.append(((rng.uniform(0, 600 - s), rng.uniform(0, 600 - s), s, s), float(rng.beta(2, 5))))
        det.append(d)
    return gt, det


def emparejar(gt, det, umbral, indices=None):
    """Devuelve (confianza, tp) por deteccion y numero de verdades."""
    indices = range(len(gt)) if indices is None else indices
    reg, ntot = [], 0
    for i in indices:
        usado = set()
        ntot += len(gt[i])
        for caja, conf in sorted(det[i], key=lambda x: -x[1]):
            mejor, mj = 0.0, -1
            for j, g in enumerate(gt[i]):
                if j in usado:
                    continue
                v = iou(caja, g)
                if v > mejor:
                    mejor, mj = v, j
            if mj >= 0 and mejor >= umbral:
                usado.add(mj)
                reg.append((conf, 1))
            else:
                reg.append((conf, 0))
    return reg, ntot


def ap(reg, ntot):
    reg = sorted(reg, key=lambda x: -x[0])
    tp = np.cumsum([r[1] for r in reg])
    fp = np.cumsum([1 - r[1] for r in reg])
    prec = tp / (tp + fp)
    rec = tp / ntot
    prec = np.maximum.accumulate(prec[::-1])[::-1]
    rec0 = np.concatenate([[0.0], rec])
    return float(np.sum((rec0[1:] - rec0[:-1]) * prec))


def pr_en_umbral(reg, ntot, c):
    tp = sum(1 for x, t in reg if x >= c and t)
    fp = sum(1 for x, t in reg if x >= c and not t)
    fn = ntot - tp
    p = tp / max(tp + fp, 1)
    r = tp / ntot
    return tp, fp, fn, p, r, 2 * p * r / max(p + r, 1e-12)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print(f"DATOS SINTETICOS (semilla 103): {NIMG} imagenes, detector SIMULADO; ninguna cifra procede de un algoritmo real")
    rng = np.random.default_rng(103)
    gt, det = simular(rng)
    ngt = sum(len(g) for g in gt)
    print(f"Cajas verdaderas = {ngt}; detecciones = {sum(len(d) for d in det)}")
    # Control: detector perfecto
    perfecto = [[(g, 1.0) for g in gs] for gs in gt]
    rp, np_ = emparejar(gt, perfecto, 0.5)
    print(f"Control: detector perfecto -> AP50 = {ap(rp, np_):.3f}")
    r50, n50 = emparejar(gt, det, 0.5)
    r75, n75 = emparejar(gt, det, 0.75)
    print(f"AP50 = {ap(r50, n50):.3f} ; AP75 = {ap(r75, n75):.3f}")
    print("Umbral de confianza  TP   FP   FN   precision  exhaustividad    F1   (IoU >= 0.5)")
    mejor = (0, 0)
    for c in (0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8):
        tp, fp, fn, p, r, f1 = pr_en_umbral(r50, n50, c)
        if f1 > mejor[0]:
            mejor = (f1, c)
        print(f"        {c:4.2f}        {tp:4d} {fp:4d} {fn:4d}   {p:8.3f}   {r:12.3f}   {f1:6.3f}")
    print(f"Mejor F1 = {mejor[0]:.3f} con confianza >= {mejor[1]}")
    # Exhaustividad por tamano (a conf 0.4)
    print("Exhaustividad por tamano de la caja (confianza >= 0.4, IoU >= 0.5):")
    for lo, hi in ((10, 20), (20, 40), (40, 70), (70, 101)):
        tpn, nn = 0, 0
        for i in range(NIMG):
            gs = [g for g in gt[i] if lo <= g[2] < hi]
            nn += len(gs)
            usado = set()
            for caja, conf in sorted(det[i], key=lambda x: -x[1]):
                if conf < 0.4:
                    continue
                for j, g in enumerate(gt[i]):
                    if j not in usado and lo <= g[2] < hi and iou(caja, g) >= 0.5:
                        usado.add(j)
                        tpn += 1
                        break
        print(f"  {lo:3d} - {hi:3d} px: {tpn:3d} de {nn:3d} = {tpn/max(nn,1):.3f}")
    # Bootstrap sobre imagenes
    def ap_boot(n_img, rep=500):
        r = np.random.default_rng(555)
        vals = []
        for _ in range(rep):
            idx = r.integers(0, NIMG, n_img)
            reg, nt = emparejar(gt, det, 0.5, idx)
            vals.append(ap(reg, nt))
        return np.percentile(vals, [2.5, 97.5])
    print("Intervalo bootstrap del 95 % de AP50 segun el numero de imagenes de evaluacion:")
    anchos = {}
    for n in (20, 50, 100):
        lo, hi = ap_boot(n)
        anchos[n] = hi - lo
        print(f"  {n:3d} imagenes: [{lo:.3f}, {hi:.3f}] (ancho {hi-lo:.3f})")
    # Segmentacion: clase rara
    rs = np.random.default_rng(104)
    acc_t, iou_t_rara, acc_m, iou_m_rara = [], [], [], []
    tp_tot = fp_tot = fn_tot = 0
    for _ in range(100):
        v = np.zeros((64, 64), bool)
        x0, y0 = rs.integers(5, 55, 2)
        v[y0:y0 + 6, x0:x0 + 6] = True  # clase rara ~ 0.9 %
        p_t = np.zeros_like(v)  # segmentador trivial
        p_m = np.roll(v, shift=int(rs.integers(-2, 3)), axis=1) & ~(rs.uniform(size=v.shape) < 0.1)  # segmentador razonable
        p_m |= rs.uniform(size=v.shape) < 0.002
        acc_t.append(np.mean(p_t == v))
        acc_m.append(np.mean(p_m == v))
        tp_tot += int(np.sum(p_m & v))
        fp_tot += int(np.sum(p_m & ~v))
        fn_tot += int(np.sum(~p_m & v))
    iou_m = tp_tot / (tp_tot + fp_tot + fn_tot)
    print(f"Segmentacion (clase rara de ~0.9 % de los pixeles): trivial -> exactitud {np.mean(acc_t)*100:.2f} %, IoU de la clase rara = 0.000;"
          f" razonable -> exactitud {np.mean(acc_m)*100:.2f} %, IoU de la clase rara = {iou_m:.3f}")
    # Profundidad
    rz = np.random.default_rng(105)
    z = rz.uniform(4, 40, 5000)
    err = rz.normal(0, z * 0.3 / 168, z.shape)  # error relativo = Z sigma_d / (f B) ; error absoluto = Z^2 sigma_d / (f B)
    zh = z + err * z * 1.0
    atip = rz.uniform(size=z.shape) < 0.02
    zh = np.where(atip, z * 1.5, zh)
    print("Profundidad (5000 puntos, 4-40 m, 2 % de atipicos): metricas globales y por rango")
    print("  rango [m]      MAE [m]   RMSE [m]   AbsRel   delta1")
    for lo, hi in ((4, 40), (4, 10), (10, 20), (20, 40)):
        m = (z >= lo) & (z < hi)
        e = zh[m] - z[m]
        print(f"  {lo:3d} - {hi:3d}   {np.mean(np.abs(e)):9.3f}  {np.sqrt(np.mean(e**2)):9.3f}  {np.mean(np.abs(e)/z[m]):7.4f}  {np.mean(np.maximum(zh[m]/z[m], z[m]/zh[m]) < 1.25):7.4f}")
    assert abs(ap(rp, np_) - 1.0) < 1e-9
    assert np.mean(acc_t) > 0.98 and iou_m > 0.3
    assert anchos[100] < anchos[20]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
