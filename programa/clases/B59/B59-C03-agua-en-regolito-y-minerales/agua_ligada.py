"""B59-C03 · Agua en regolito y minerales: pérdida de masa por etapas (TGA sintética).

Datos SINTÉTICOS (generados aquí con semilla fija, no medidos): curva de pérdida de masa de una
muestra de regolito simulado con tres reservorios de agua: hielo (se pierde en la rampa 100-300 K), agua de hidrato (400-600 K) e hidroxilo (800-1100 K).
Constantes consultadas (2026-11-09): masa molar del agua 18,0153 g/mol (NIST WebBook, CAS 7732-18-5).
Masa molar del mineral anhidro: ILUSTRATIVA.
Modelo: cada reservorio pierde su masa con una sigmoide logística en temperatura (T0, ancho).
Se recuperan las fracciones por (a) diferencia de los escalones de la curva y (b) ajuste de mínimos cuadrados.
Unidades: K, fracción másica adimensional, g/mol.
Tolerancia: las fracciones recuperadas coinciden con las sembradas a menos de 0,05 puntos porcentuales.
"""
import math
import platform
import random

M_H2O = 18.0153          # g/mol, NIST WebBook
SEMILLA = 20261109
RESERV = {               # fraccion masica del agua sembrada, centro T0 [K], ancho [K]
    "hielo":     (0.0300, 190.0, 18.0),
    "hidrato":   (0.0200, 500.0, 35.0),
    "hidroxilo": (0.0050, 950.0, 60.0),
}
SIGMA_RUIDO = 2.0e-4     # ruido de la balanza sintetica (fraccion de masa)


def sig(T, T0, w):
    return 1.0 / (1.0 + math.exp(-(T - T0) / w))


def masa(T):
    m = 1.0
    for f, T0, w in RESERV.values():
        m -= f * sig(T, T0, w)
    return m


def hidrato_estequiometrico(M_anhidro, n):
    """Fraccion masica de agua de un hidrato M·nH2O."""
    return n * M_H2O / (M_anhidro + n * M_H2O)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(SEMILLA)
    Ts = [100 + 5 * i for i in range(0, 201)]          # 100..1100 K
    datos = [(T, masa(T) + rng.gauss(0, SIGMA_RUIDO)) for T in Ts]

    # (a) escalones: masa en mesetas entre reservorios (T = 300, 700, 1100 K)
    def meseta(T):
        return min(datos, key=lambda d: abs(d[0] - T))[1]
    m100, m300, m700, m1100 = meseta(100), meseta(300), meseta(700), meseta(1100)
    est = {"hielo": m100 - m300, "hidrato": m300 - m700, "hidroxilo": m700 - m1100}
    print("Reservorio   sembrado[%]  recuperado[%]  diferencia[pp]")
    for k, (f, _, _) in RESERV.items():
        print(f"{k:10s}  {100*f:10.3f}  {100*est[k]:12.3f}  {100*(est[k]-f):13.3f}")
        assert abs(est[k] - f) < 5e-4, f"escalon {k} fuera de tolerancia"
    total = sum(est.values())
    print(f"Agua total recuperada = {100*total:.3f} % en masa (sembrada {100*sum(v[0] for v in RESERV.values()):.3f} %)")

    # (b) ajuste de minimos cuadrados de las tres amplitudes con T0 y ancho conocidos (sistema lineal 3x3)
    cols = [[sig(T, T0, w) for T, _ in datos] for (_, T0, w) in RESERV.values()]
    y = [1.0 - m for _, m in datos]
    A = [[sum(ci * cj for ci, cj in zip(cols[i], cols[j])) for j in range(3)] for i in range(3)]
    b = [sum(ci * yi for ci, yi in zip(cols[i], y)) for i in range(3)]
    # Eliminacion gaussiana
    n = 3
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[p] = A[p], A[i]
        b[i], b[p] = b[p], b[i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= f * A[i][c]
            b[r] -= f * b[i]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (b[i] - sum(A[i][c] * x[c] for c in range(i + 1, n))) / A[i][i]
    for (k, (f, _, _)), xi in zip(RESERV.items(), x):
        print(f"Ajuste {k:10s}: {100*xi:.3f} % (sembrado {100*f:.3f} %)")
        assert abs(xi - f) < 5e-4

    # Estequiometria de un hidrato sintetico de masa anhidra 172 g/mol (ILUSTRATIVA) con n = 2 y n = 7
    for n_h in (2, 7):
        print(f"Hidrato M=172 g/mol, n={n_h}: agua = {100*hidrato_estequiometrico(172.0, n_h):.2f} % en masa")
    assert abs(hidrato_estequiometrico(172.0, 2) - 2 * M_H2O / (172.0 + 2 * M_H2O)) < 1e-15
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
