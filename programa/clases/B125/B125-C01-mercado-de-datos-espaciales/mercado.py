#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B125-C01: mercado de un dato espacial con un sustituto gratuito (modelo SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de inversion.
Datos consultados (2026-11-11): ninguno numerico entra al calculo. Se consulto que el Reglamento (UE) 377/2014, art. 23, fija un acceso
gratuito y abierto a los datos de Copernicus con limites, y que el USGS ofrece los productos Landsat sin cargo (desde 2008 segun su pagina).
Ambos son el CONTEXTO del modelo (existe un sustituto gratuito); ningun precio, cuota ni volumen de mercado fue consultado.
ILUSTRATIVOS (sinteticos): disposicion a pagar (DAP) uniforme en [0, W] con W = 100 unidades monetarias (u.m.) por escena-equivalente al mes;
fraccion del valor que cubre el sustituto gratuito s; 10 000 clientes sinteticos (semilla 125); costo marginal de servir 0.
Modelo: un cliente con DAP v compra el dato de pago a precio P si v - P >= s v (valor del sustituto gratuito), es decir P <= (1 - s) v.
Unidades: u.m. por cliente y mes. Tolerancias: precio optimo de la rejilla frente al analitico (1 - s) W / 2 dentro de 3 u.m. (la curva de ingreso es plana cerca del maximo y el ruido de muestreo mueve el argmax);
ingreso simulado frente al analitico dentro de 2 %.
"""
from __future__ import annotations
import platform, random

W, N, SEMILLA = 100.0, 10000, 125


def ingreso_analitico(p, s):
    """Ingreso por cliente: P * Prob(v >= P / (1 - s)) con v ~ U(0, W)."""
    umbral = p / (1.0 - s)
    return p * max(0.0, 1.0 - umbral / W)


def optimo_analitico(s):
    return (1.0 - s) * W / 2.0, (1.0 - s) * W / 4.0


def ingreso_simulado(p, s, vs):
    compra = sum(1 for v in vs if p <= (1.0 - s) * v)
    return p * compra / len(vs)


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Mercado SINTETICO; DAP ~ U(0, 100) u.m./mes; s = fraccion de valor cubierta por el sustituto gratuito; sin cifras de mercado consultadas.")
    rng = random.Random(SEMILLA)
    vs = [rng.uniform(0, W) for _ in range(N)]
    print("  s     P* analit  R* analit  P* rejilla  R* simulado  compradores a P*")
    for s in (0.0, 0.3, 0.6, 0.8):
        pa, ra = optimo_analitico(s)
        mejor_p, mejor_r = 0.0, -1.0
        p = 0.0
        while p <= W:
            r = ingreso_simulado(p, s, vs)
            if r > mejor_r:
                mejor_p, mejor_r = p, r
            p += 0.5
        comp = sum(1 for v in vs if mejor_p <= (1 - s) * v) / N
        print(f"{s:4.1f}  {pa:9.2f}  {ra:9.2f}  {mejor_p:10.1f}  {mejor_r:11.2f}  {comp:8.3f}")
        assert abs(mejor_p - pa) <= 3.0, "precio optimo fuera de tolerancia"
        assert abs(mejor_r - ra) / ra <= 0.02, "ingreso fuera de tolerancia"
    # Cadena de valor: el dato crudo gratuito reduce el ingreso del crudo; el producto elaborado se cobra por el valor agregado.
    print("Cadena de valor SINTETICA (por cliente y mes, u.m.): crudo gratuito (s = 0.8) frente a producto elaborado")
    ingreso_crudo = optimo_analitico(0.8)[1]
    # Producto elaborado: ahorra al cliente un costo de procesamiento c ~ U(0, 40); el cliente paga hasta c; el sustituto no lo ofrece.
    cp = 40.0
    ingreso_elaborado = cp / 4.0
    print(f"  ingreso optimo del dato crudo de pago      = {ingreso_crudo:.2f}")
    print(f"  ingreso optimo del producto elaborado      = {ingreso_elaborado:.2f}   (DAP ~ U(0, {cp:.0f}); precio {cp/2:.1f})")
    assert abs(ingreso_crudo - 5.0) < 1e-12 and abs(ingreso_elaborado - 10.0) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
