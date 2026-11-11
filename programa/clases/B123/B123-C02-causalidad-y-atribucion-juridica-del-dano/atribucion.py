"""B123-C02 - Atribucion de un dano SINTETICO: posterior por candidato, regimen y reparto.

Datos SINTETICOS (ningun caso real). Solo biblioteca estandar. Sin unidades fisicas salvo kg y UMF.
Normativa (leida en resumen, ver CLASE.md): Convenio de 1972, arts. II, III, IV.
La verosimilitud de cada candidato es una convencion didactica, NO una prueba juridica.
"""
import sys

# Candidatos sinteticos: (nombre, prior por trafico orbital, coincidencia de material 0..1, coincidencia de masa 0..1)
CANDIDATOS = [
    ("objeto A (Estado de lanzamiento X)", 0.30, 0.90, 0.80),
    ("objeto B (Estado de lanzamiento Y)", 0.50, 0.30, 0.50),
    ("objeto C (Estado de lanzamiento Z)", 0.20, 0.60, 0.40),
]


def posterior(candidatos):
    pesos = [p * m * k for _, p, m, k in candidatos]
    s = sum(pesos)
    return [w / s for w in pesos]


def regimen(lugar):
    """art. II: superficie terrestre o aeronave en vuelo -> absoluta; art. III: fuera de la superficie -> culpa."""
    return "absoluta (art. II)" if lugar in ("superficie", "aeronave") else "por culpa (art. III)"


def reparto(cuantia, culpas):
    """art. IV: solidaridad frente al tercero; entre los Estados, segun culpa o por partes iguales si no se prueba."""
    if culpas is None or sum(culpas.values()) == 0:
        n = 2
        return {"X": cuantia / n, "Y": cuantia / n}
    s = sum(culpas.values())
    return {k: cuantia * v / s for k, v in culpas.items()}


def contrafactual(con_objeto, sin_objeto):
    """Prueba 'sin el objeto, no hay dano': probabilidad de dano con y sin el objeto (SINTETICA)."""
    return con_objeto - sin_objeto


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Datos SINTETICOS; UMF = unidad monetaria ficticia")
    post = posterior(CANDIDATOS)
    for (n, p, m, k), q in zip(CANDIDATOS, post):
        print(f"  {n:<38s} prior={p:.2f} material={m:.2f} masa={k:.2f} -> posterior={q:.4f}")
    print(f"Suma de posteriores = {sum(post):.6f}")
    for lugar in ("superficie", "aeronave", "orbita"):
        print(f"Dano en {lugar:<10s}: regimen {regimen(lugar)}")
    print("Reparto de 1 000 000 UMF entre X e Y (art. IV):")
    for nombre, culpas in [("culpa 70/30", {"X": 70, "Y": 30}), ("sin culpa probada", None)]:
        r = reparto(1_000_000.0, culpas)
        print(f"  {nombre:<18s} X = {r['X']:,.0f} ; Y = {r['Y']:,.0f}")
    delta = contrafactual(0.95, 0.05)
    print(f"Contrafactual (SINTETICO): P(dano | con objeto) - P(dano | sin objeto) = {delta:.2f}")
    assert abs(sum(post) - 1.0) < 1e-12
    assert max(post) == post[0]
    assert abs(sum(reparto(1_000_000.0, {"X": 70, "Y": 30}).values()) - 1_000_000.0) < 1e-6
    assert abs(sum(reparto(1_000_000.0, None).values()) - 1_000_000.0) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
