"""Reemplazo preventivo por edad: intervalo que minimiza el costo por unidad de tiempo.

Datos: vida Weibull con forma 2,5 y escala 1000 h; costo preventivo 1 y costo por falla 10 (unidades
relativas). TODO ILUSTRATIVO; no son datos de un componente real. No se consultó ninguna fuente externa.
Modelo: C(T) = [cp R(T) + cf (1 - R(T))] / integral_0^T R(t) dt, con R(t) = exp(-(t/eta)^beta).
Dos vías para el óptimo: búsqueda en rejilla y sección áurea. Tercera: simulación de ciclos de renovación
(semilla 20261109), con razón recompensa/tiempo.
Supuestos: reemplazo perfecto e instantáneo; vidas independientes; costos constantes.
Tolerancia: óptimo de ambas vías a menos de 1 h; costo simulado a menos de 4 errores estándar.
"""
import math
import random

BETA, ETA = 2.5, 1000.0
CP, CF = 1.0, 10.0


def R(t):
    return math.exp(-((t / ETA) ** BETA))


def integral(T, n=4000):
    h = T / n
    s = R(0) + R(T)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * R(i * h)
    return s * h / 3


def costo(T):
    r = R(T)
    return (CP * r + CF * (1 - r)) / integral(T)


def rejilla():
    mejor = min(range(100, 3001), key=lambda t: costo(float(t)))
    return float(mejor)


def aurea(a=100.0, b=3000.0):
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    while b - a > 1e-6:
        if costo(c) < costo(d):
            b, d = d, c
            c = b - g * (b - a)
        else:
            a, c = c, d
            d = a + g * (b - a)
    return 0.5 * (a + b)


def simula(T, ciclos=300000):
    rng = random.Random(20261109)
    tiempo = 0.0
    gasto = 0.0
    cs = []
    for _ in range(ciclos):
        x = rng.weibullvariate(ETA, BETA)
        if x < T:
            tiempo += x
            gasto += CF
            cs.append((x, CF))
        else:
            tiempo += T
            gasto += CP
            cs.append((T, CP))
    return gasto / tiempo, cs


def calc():
    t_r = rejilla()
    t_a = aurea()
    sin_prev = CF / (ETA * math.gamma(1 + 1 / BETA))
    c_opt = costo(t_a)
    c_sim, cs = simula(t_a)
    # error estándar de la razón por linealización
    n = len(cs)
    mt = sum(c[0] for c in cs) / n
    mc = sum(c[1] for c in cs) / n
    r = mc / mt
    var = sum((c[1] - r * c[0]) ** 2 for c in cs) / (n - 1)
    se = math.sqrt(var / n) / mt
    return dict(t_r=t_r, t_a=t_a, c_opt=c_opt, sin=sin_prev, c_sim=c_sim, se=se, int_inf=integral(6000.0), gam=ETA * math.gamma(1 + 1 / BETA),
                ahorro=1 - c_opt / sin_prev)


def main():
    Q = calc()
    print(f"Óptimo por rejilla = {Q['t_r']:.0f} h; por sección áurea = {Q['t_a']:.2f} h")
    print(f"Costo por hora en el óptimo = {Q['c_opt']:.6f}; solo correctivo = {Q['sin']:.6f}; ahorro = {100 * Q['ahorro']:.1f} %")
    print(f"Simulación a ese T: {Q['c_sim']:.6f} (error estándar {Q['se']:.6f})")
    print(f"Integral de R hasta 6000 h = {Q['int_inf']:.3f}; eta Gamma(1 + 1/beta) = {Q['gam']:.3f}")
    assert abs(Q["t_r"] - Q["t_a"]) < 1.0
    assert abs(Q["c_sim"] - Q["c_opt"]) < 4 * Q["se"]
    assert abs(Q["int_inf"] - Q["gam"]) < 0.01
    assert Q["c_opt"] < Q["sin"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
