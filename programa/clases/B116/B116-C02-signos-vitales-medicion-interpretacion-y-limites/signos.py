#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B116-C02: signos vitales sinteticos, ruido de medida y rango poblacional frente a linea base personal.

Todo es sintetico (semilla 117) y NO describe a ninguna persona. Rangos poblacionales de reposo del adulto sano tomados de la pagina de
MedlinePlus (consultada 2026-11-10): pulso 60-100 lpm, frecuencia respiratoria 12-18 resp/min, temperatura 36,5-37,3 C, presion
90/60 a 120/80 mmHg. La pagina advierte que los valores normales cambian con la edad, el sexo, el peso y la salud. Unidades: lpm, resp/min,
C, mmHg. Relaciones estandar (no consultadas en una fuente concreta, las verifica el laboratorio): presion de pulso = PAS - PAD; presion
arterial media aproximada PAM = PAD + (PAS - PAD)/3; probabilidad de marca falsa por ruido gaussiano con la funcion de error (math.erf).
Se calcula: (1) probabilidad analitica y de Monte Carlo de que el ruido de un sensor saque de rango un valor normal; (2) una serie de 30
dias con un cambio verdadero de +12 lpm a partir del dia 20: el rango poblacional (60-100) no lo detecta, la linea base personal
(media +/- 3 DE de los 14 primeros dias) si. Verificacion: Monte Carlo y analitica coinciden dentro de 0,01. Numpy requerido.
"""
from __future__ import annotations
import math
import platform
import numpy as np

RANGOS = {"pulso [lpm]": (60.0, 100.0), "resp [resp/min]": (12.0, 18.0), "temp [C]": (36.5, 37.3)}


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def p_fuera(valor, sigma, lo, hi):
    """Probabilidad de que valor + ruido N(0, sigma) quede fuera de [lo, hi]."""
    return phi((lo - valor) / sigma) + 1 - phi((hi - valor) / sigma)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 117): signos simulados; no describen a ninguna persona")
    rng = np.random.default_rng(117)
    print("Presion de pulso y PAM para 120/80 mmHg: PP = %d mmHg, PAM = %.1f mmHg" % (120 - 80, 80 + (120 - 80) / 3))
    print("Probabilidad de marca falsa (valor verdadero normal, ruido gaussiano del sensor):")
    print("  signo            verdadero   sigma   analitica   Monte Carlo (1e5)")
    casos = [("pulso [lpm]", 98.0, 3.0), ("pulso [lpm]", 80.0, 3.0), ("resp [resp/min]", 17.0, 1.5), ("temp [C]", 37.2, 0.2), ("temp [C]", 37.2, 0.05)]
    mxd = 0.0
    for nombre, v, s in casos:
        lo, hi = RANGOS[nombre]
        pa = p_fuera(v, s, lo, hi)
        x = v + rng.normal(0, s, 100000)
        pm = float(np.mean((x < lo) | (x > hi)))
        mxd = max(mxd, abs(pa - pm))
        print(f"  {nombre:16s} {v:7.1f}   {s:5.2f}   {pa:8.4f}    {pm:8.4f}")
    print(f"Diferencia maxima analitica - Monte Carlo = {mxd:.4f}")
    assert mxd < 0.01
    print("Marcas por dia con medidas cada 5 min (288/dia) de un valor normal 98 lpm con sigma 3 lpm, sin filtrar: %.1f" % (288 * p_fuera(98, 3, 60, 100)))
    # serie de 30 dias: pulso en reposo; cambio verdadero de +12 lpm desde el dia 20
    dias = np.arange(30)
    base_persona = 52.0  # lpm, linea base de esta persona sintetica (bajo el rango poblacional medio)
    verdadero = np.where(dias >= 20, base_persona + 12.0, base_persona)
    medido = verdadero + rng.normal(0, 1.5, dias.size)
    lo_p, hi_p = RANGOS["pulso [lpm]"]
    mu, sd = medido[:14].mean(), medido[:14].std(ddof=1)
    z = (medido - mu) / sd
    print("Serie de 30 dias (pulso de reposo): base verdadera 52 lpm, +12 lpm desde el dia 20 (sintetico)")
    print(f"  linea base personal (dias 0-13): media = {mu:.1f} lpm, DE = {sd:.2f} lpm; umbral personal = media +/- 3 DE = [{mu - 3 * sd:.1f}, {mu + 3 * sd:.1f}]")
    pob = [(int(d), float(m)) for d, m in zip(dias, medido) if m < lo_p or m > hi_p]
    per = [int(d) for d, v in zip(dias, z) if abs(v) > 3]
    print(f"  rango poblacional 60-100: dias marcados = {[d for d, _ in pob][:6]} ... ({len(pob)} dias)")
    print(f"  linea base personal: primer dia marcado = {per[0] if per else None}; dias marcados desde el 20 = {sum(1 for d in per if d >= 20)} de 10")
    print("  nota: la persona sintetica vive por debajo de 60 lpm todo el tiempo, asi que el rango poblacional marca TODOS los dias normales (falsa alarma permanente)")
    print("Prueba del cambio con una persona sintetica en 75 lpm (+12 lpm desde el dia 20): el rango poblacional no lo detecta")
    v2 = np.where(dias >= 20, 75.0 + 12.0, 75.0) + rng.normal(0, 1.5, dias.size)
    mu2, sd2 = v2[:14].mean(), v2[:14].std(ddof=1)
    per2 = [int(d) for d, v in zip(dias, (v2 - mu2) / sd2) if abs(v) > 3]
    pob2 = [int(d) for d, v in zip(dias, v2) if v < lo_p or v > hi_p]
    print(f"  poblacional: dias marcados = {pob2}; personal: primer dia marcado = {per2[0] if per2 else None}")
    assert not pob2 and per2 and per2[0] >= 20
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
