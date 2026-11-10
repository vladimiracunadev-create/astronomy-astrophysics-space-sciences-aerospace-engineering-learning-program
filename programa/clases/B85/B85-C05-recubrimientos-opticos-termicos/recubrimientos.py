# SPDX-License-Identifier: Apache-2.0
"""B85-C05: recubrimientos ópticos térmicos: α/ε, temperatura de equilibrio de una placa y envejecimiento.

Consultado: SIGMA (NIST), S0 (NASA/NSSDC) y de NASA SST-SoA Thermal Control: coatings a medida con ε ≈ 0.25 y α ≈ 0.1,
cinta de plata/FEP con α inicial desde 0.08, y que los recubrimientos se oscurecen en órbita (usar valores de fin de vida
para el caso caliente). Todo lo demás (tabla de α, ε, α_EOL por recubrimiento) es ILUSTRATIVO y sintético.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

# nombre: (alfa_BOL, eps, alfa_EOL)  ILUSTRATIVOS
TABLA = {
    "pintura blanca": (0.20, 0.90, 0.35),
    "pintura negra": (0.95, 0.90, 0.95),
    "espejo solar OSR": (0.08, 0.80, 0.15),
    "aluminio pulido": (0.15, 0.05, 0.20),
    "oro": (0.25, 0.03, 0.25),
    "coating a medida": (0.10, 0.25, 0.14),
}


def t_placa(alfa, eps, cos=1.0, q_int=0.0):
    """Placa de area unitaria, una cara al Sol e insulada por detras; q_int [W/m2] disipado hacia esa cara."""
    return ((alfa * S0 * cos + q_int) / (eps * SIGMA)) ** 0.25


def calcular():
    r = {"filas": []}
    for n, (a, e, ae) in TABLA.items():
        r["filas"].append((n, a, e, ae, a / e, ae / e, t_placa(a, e), t_placa(ae, e)))
    # recubrimientos que mantienen la placa entre 250 y 320 K, BOL y EOL, con 1 Sol
    r["validos"] = [f[0] for f in r["filas"] if 250.0 <= f[6] <= 320.0 and 250.0 <= f[7] <= 320.0]
    # control: placa con carga interna de 100 W/m2 a la sombra (cos = 0)
    r["t_blanca_oscura"] = t_placa(0.20, 0.90, 0.0, 100.0)
    # alfa/eps necesario para 293.15 K con 1 Sol
    r["cociente_objetivo"] = SIGMA * 293.15 ** 4 / S0
    # segunda via: balance residual
    f = [f for f in r["filas"] if f[0] == "pintura blanca"][0]
    r["residuo"] = f[1] * S0 - f[2] * SIGMA * f[6] ** 4
    r["dt_envejecimiento_blanca"] = f[7] - f[6]
    r["t_osr"], r["t_osr_eol"] = [(x[6], x[7]) for x in r["filas"] if x[0] == "espejo solar OSR"][0]
    return r


def main():
    r = calcular()
    cabecera()
    print("Tabla ILUSTRATIVA (alfa_BOL, eps, alfa_EOL) y placa unitaria con una cara a 1 Sol (S0 = 1361.0 W/m2), reverso aislado")
    print(f"{'recubrimiento':<18}{'a_BOL':>7}{'eps':>6}{'a_EOL':>7}{'a/e BOL':>9}{'a/e EOL':>9}{'T BOL[K]':>10}{'T EOL[K]':>10}")
    for n, a, e, ae, c1, c2, t1, t2 in r["filas"]:
        print(f"{n:<18}{a:>7.2f}{e:>6.2f}{ae:>7.2f}{c1:>9.3f}{c2:>9.3f}{t1:>10.2f}{t2:>10.2f}")
    print(f"Recubrimientos que mantienen 250-320 K en BOL y EOL: {', '.join(r['validos']) if r['validos'] else 'ninguno'}")
    print(f"alfa/eps necesario para 293.15 K con 1 Sol = {r['cociente_objetivo']:.4f}")
    print(f"Pintura blanca: envejecimiento +{r['dt_envejecimiento_blanca']:.2f} K ; residuo del balance = {r['residuo']:.2e} W/m2")
    print(f"Placa de pintura blanca a la sombra con 100 W/m2 internos: T = {r['t_blanca_oscura']:.2f} K")
    comprobar(abs(r["residuo"]) < 1e-9, "balance")
    comprobar(all(f[7] >= f[6] for f in r["filas"]), "EOL >= BOL")
    fin()


if __name__ == "__main__":
    main()
