"""B123-C01 - Expediente de dano SINTETICO: cuantia, incertidumbre y plazo.

Todos los datos son SINTETICOS (no describen ningun caso real). Solo biblioteca estandar.
Unidades: monedas en unidades monetarias ficticias (UMF); fechas calendario ISO 8601.
Referencia normativa (leida en resumen, ver CLASE.md): Convenio de 1972, arts. I(a), X, XII, XIII.
"""
import random
import statistics
import sys
from datetime import date

SEMILLA = 123
random.seed(SEMILLA)

# Partidas del expediente sintetico: (descripcion, monto en UMF-reclamante, grado de prueba 0..1)
# El grado de prueba es una convencion didactica, NO una regla juridica.
PARTIDAS = [
    ("reparacion de cubierta de una nave industrial", 180_000.0, 0.95),
    ("sustitucion de maquinaria dañada", 420_000.0, 0.85),
    ("limpieza y descontaminacion del terreno", 300_000.0, 0.60),
    ("lucro cesante de tres meses", 250_000.0, 0.40),
]
TASA_UMF_B_A_A = 0.80  # SINTETICA: 1 UMF-B = 0,80 UMF-A (moneda del reclamante)


def cuantia_esperada(partidas):
    """Suma ponderada por grado de prueba (convencion didactica)."""
    return sum(m * g for _, m, g in partidas)


def monte_carlo(n=20000):
    """Incertidumbre del costo de limpieza: lognormal con mediana 300000 y sigma 0.25 (SINTETICO)."""
    base = sum(m * g for d, m, g in PARTIDAS if not d.startswith("limpieza"))
    xs = []
    for _ in range(n):
        limpieza = 300_000.0 * 0.60 * random.lognormvariate(0.0, 0.25)
        xs.append(base + limpieza)
    xs.sort()
    return statistics.median(xs), xs[int(0.05 * n)], xs[int(0.95 * n)]


def dentro_de_plazo(dano, reclamacion, dias=365):
    """Un ano desde el dano (art. X). Aproximacion: 365 dias corridos; no cubre la identificacion del Estado."""
    return (reclamacion - dano).days <= dias, (reclamacion - dano).days


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Datos SINTETICOS; UMF = unidad monetaria ficticia; semilla", SEMILLA)
    total_bruto = sum(m for _, m, _ in PARTIDAS)
    esperada = cuantia_esperada(PARTIDAS)
    print(f"Total reclamado (bruto) = {total_bruto:,.0f} UMF")
    for d, m, g in PARTIDAS:
        print(f"  {d:<48s} {m:>10,.0f}  prueba={g:.2f}  ponderado={m*g:>10,.0f}")
    print(f"Cuantia ponderada por prueba = {esperada:,.0f} UMF")
    en_a = esperada * TASA_UMF_B_A_A
    print(f"Convertida a la moneda del reclamante (tasa sintetica {TASA_UMF_B_A_A}) = {en_a:,.0f} UMF-A")
    med, p5, p95 = monte_carlo()
    print(f"Monte Carlo (20000 sorteos): mediana = {med:,.0f}; P5 = {p5:,.0f}; P95 = {p95:,.0f} UMF")
    for dano, recl in [(date(2026, 3, 1), date(2027, 1, 15)), (date(2026, 3, 1), date(2027, 4, 1))]:
        ok, dd = dentro_de_plazo(dano, recl)
        print(f"Dano {dano} -> reclamacion {recl}: {dd} dias; dentro del plazo de un ano: {ok}")
    # Comprobaciones
    assert abs(total_bruto - 1_150_000.0) < 1e-9
    assert esperada <= total_bruto
    assert p5 < med < p95
    assert abs(en_a / TASA_UMF_B_A_A - esperada) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
