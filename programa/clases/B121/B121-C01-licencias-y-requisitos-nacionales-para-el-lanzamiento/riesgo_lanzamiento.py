"""B121-C01 - Riesgo colectivo de un lanzamiento frente a un criterio de licencia.

DATOS SINTETICOS (ilustrativos): zonas de impacto, poblaciones, probabilidades de falla.
Solo se CONSULTAN los umbrales numericos de 14 CFR 450.101(a) (eCFR, consultado 2026-11-11).
Unidades: personas/km2, km2, esperado de bajas (adimensional), probabilidad (adimensional).
Sistema de referencia: no aplica (modelo de zonas discretas, sin geodesia).
Solo biblioteca estandar. Semilla fija 121.
"""
import math
import random
import sys

EC_PUBLICO = 1e-4      # 14 CFR 450.101(a): bajas esperadas, publico (consultado)
PC_PUBLICO = 1e-6      # 14 CFR 450.101(a): probabilidad individual por lanzamiento (consultado)
A_CAS = 0.004          # km2, area de baja por fragmento (SINTETICO)
P_FALLA = 0.03         # prob. de falla del vehiculo en vuelo (SINTETICO)

# zona: (densidad personas/km2, area km2) SINTETICAS
ZONAS = {"oceano": (0.0, 5.0e5), "isla": (40.0, 800.0), "costa": (600.0, 120.0), "ciudad": (4000.0, 60.0)}
# opciones de trayectoria: fraccion condicional de la falla que cae en cada zona (suman 1)
OPCIONES = {
    "A_mar_abierto": {"oceano": 0.9990, "isla": 0.0008, "costa": 0.0002, "ciudad": 0.0000},
    "B_costera": {"oceano": 0.9900, "isla": 0.0050, "costa": 0.0049, "ciudad": 0.0001},
    "C_sobre_zona_poblada": {"oceano": 0.9800, "isla": 0.0100, "costa": 0.0095, "ciudad": 0.0005},
}


def ec_analitico(f):
    """Ec = P_falla * sum_z f_z * rho_z * A_cas  (bajas esperadas)."""
    return P_FALLA * sum(f[z] * ZONAS[z][0] * A_CAS for z in f)


def pc_individual(f):
    """Prob. de baja de una persona en la zona mas expuesta: P_falla * f_z * A_cas / A_z."""
    return max(P_FALLA * f[z] * A_CAS / ZONAS[z][1] for z in f if ZONAS[z][0] > 0)


def poisson(rng, lam):
    if lam == 0:
        return 0
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def ec_montecarlo(f, n, rng):
    """Condicional a la falla; se escala por P_falla (verificacion independiente)."""
    zs = list(f)
    pesos = [f[z] for z in zs]
    total = 0
    for _ in range(n):
        z = rng.choices(zs, pesos)[0]
        total += poisson(rng, ZONAS[z][0] * A_CAS)
    return P_FALLA * total / n


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Zonas, poblaciones y probabilidades SINTETICAS; umbrales de 14 CFR 450.101(a) consultados 2026-11-11.")
    print(f"Umbrales: Ec <= {EC_PUBLICO:.0e}, Pc individual <= {PC_PUBLICO:.0e}; P_falla = {P_FALLA}, A_cas = {A_CAS} km2")
    rng = random.Random(121)
    print(f"{'opcion':24s}{'Ec':>11s}{'Ec MC':>11s}{'Pc ind.':>11s}  Ec ok  Pc ok")
    for nombre, f in OPCIONES.items():
        assert abs(sum(f.values()) - 1) < 1e-12
        ec = ec_analitico(f)
        mc = ec_montecarlo(f, 400000, rng)
        pc = pc_individual(f)
        # tolerancia: 10 % relativo o 2e-5 absoluto (MC con 400 mil muestras)
        assert abs(mc - ec) <= max(0.10 * ec, 2e-5), (nombre, ec, mc)
        print(f"{nombre:24s}{ec:11.3e}{mc:11.3e}{pc:11.3e}  {str(ec <= EC_PUBLICO):5s}  {str(pc <= PC_PUBLICO):5s}")
    # sensibilidad: cuanto debe bajar P_falla para que C cumpla Ec
    f = OPCIONES["C_sobre_zona_poblada"]
    por_falla = ec_analitico(f) / P_FALLA
    print(f"Ec condicional a la falla (C) = {por_falla:.4f} bajas; P_falla maxima admisible = {EC_PUBLICO / por_falla:.2e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
