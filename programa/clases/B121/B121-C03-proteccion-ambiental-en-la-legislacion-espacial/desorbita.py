"""B121-C03 - Vida orbital, plazos de desorbita (25 y 5 anos) y riesgo de reentrada.

DATOS SINTETICOS: satelites y atmosfera exponencial ILUSTRATIVA (no es NRLMSISE-00 ni ninguna
atmosfera normalizada; ignora la actividad solar). Consultados 2026-11-11: IADC Rev. 4 (2025-01, via
A/AC.105/C.1/2025/CRP.9): 25 anos, P(exito) >= 0,9, 1e-4 bajas; 47 CFR 25.114(d)(14)(vii) (eCFR):
5 anos en LEO < 2000 km, P(exito) >= 0,9, riesgo < 1e-4 con energia cinetica > 15 J.
Unidades: km, m, kg, s, anos. mu = 398600,4418 km3/s2. Orbita circular, sin J2.
Solo biblioteca estandar.
"""
import math
import sys

MU = 398600.4418  # km3/s2
RE = 6378.137  # km
ANO = 365.25 * 86400.0
# atmosfera exponencial ILUSTRATIVA: rho(h) = RHO0 * exp(-(h-H0)/HE), por tramos de escala creciente
RHO0, H0 = 3.0e-12, 400.0  # kg/m3 a 400 km (ilustrativo)


def rho(h):
    he = 30.0 + 0.10 * (h - 200.0)  # altura de escala ilustrativa [km]: crece con la altitud
    return RHO0 * math.exp(-(h - H0) / he)


def tasa(h, bc):
    """dh/dt [km/s] (negativa): da/dt = -rho * v * a / bc para orbita circular, con bc = m/(Cd*A)."""
    a = (RE + h) * 1e3
    return -rho(h) * math.sqrt(MU * 1e9 / a) * a / bc / 1e3


def vida(h0, bc, h_fin=150.0, max_anos=400.0):
    """Via 1: Euler con paso adaptativo (dt = min(3600 s, 2 % de la altura de escala / |dh/dt|))."""
    h, t = h0, 0.0
    while h > h_fin and t < max_anos * ANO:
        r = tasa(h, bc)
        dt = min(3600.0, 0.02 * (30.0 + 0.10 * (h - 200.0)) / abs(r))
        h += r * dt
        t += dt
    return t / ANO, h


def vida_rk(h0, bc, h_fin=150.0, n=20000):
    """Via 2: t = integral de dh/|dh/dt| entre h_fin y h0 (cuadratura de Simpson, sin integrar en el tiempo)."""
    dh = (h0 - h_fin) / n
    s = 1 / abs(tasa(h_fin, bc)) + 1 / abs(tasa(h0, bc))
    for i in range(1, n):
        s += (4 if i % 2 else 2) / abs(tasa(h_fin + i * dh, bc))
    return s * dh / 3 / ANO


def p_todos_ok(p, n):
    return p ** n


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Satelites y atmosfera SINTETICOS/ILUSTRATIVOS; plazos y umbrales consultados el 2026-11-11 (IADC Rev.4; 47 CFR 25.114).")
    bc = 60.0 / (2.2 * 0.5)  # 60 kg, Cd 2,2, A 0,5 m2 -> kg/m2
    print(f"Satelite de 60 kg, Cd 2,2, A 0,5 m2 -> m/(CdA) = {bc:.1f} kg/m2")
    print(f"{'h0[km]':>7s}{'vida Euler[a]':>15s}{'vida cuad.[a]':>14s}  <=5 a  <=25 a")
    for h0 in (450, 500, 550, 600, 650, 700):
        v1, _ = vida(h0, bc)
        v2 = vida_rk(h0, bc)
        assert abs(v1 - v2) / v2 < 0.01, (h0, v1, v2)  # tolerancia 1 %
        print(f"{h0:7d}{v1:15.2f}{v2:14.2f}  {str(v1 <= 5):5s}  {str(v1 <= 25):5s}")
    # altitud maxima que cumple 5 y 25 anos (biseccion con la cuadratura)
    for lim in (5.0, 25.0):
        lo, hi = 300.0, 900.0
        for _ in range(40):
            m = (lo + hi) / 2
            if vida_rk(m, bc) <= lim:
                lo = m
            else:
                hi = m
        print(f"Altitud maxima inicial con vida <= {lim:.0f} a: {lo:.1f} km (modelo ilustrativo)")
    # constelacion: probabilidad de que TODOS los satelites se desorbiten con exito
    print("Constelacion de N satelites con P(exito) individual p:")
    for p in (0.90, 0.99):
        print(f"  p={p}: " + ", ".join(f"N={n}: P(todos)={p_todos_ok(p, n):.4f}" for n in (10, 100, 1000)))
    print(f"  fallos esperados con N=100: p=0,90 -> {100*(1-0.90):.0f}; p=0,99 -> {100*(1-0.99):.0f}")
    # riesgo de reentrada: Ec = sum(A_cas,i) * densidad poblacional media (SINTETICO)
    dens = 25.0 / 1e6  # personas/m2 (25 personas/km2, ilustrativo)
    for nombre, areas in (("diseno A", [0.6, 1.1, 0.3]), ("diseno B", [0.6, 1.1, 0.3, 2.4, 1.8, 3.0])):
        ec = sum(areas) * dens
        print(f"{nombre}: A_cas total {sum(areas):.1f} m2 -> Ec = {ec:.2e} ({'< 1e-4 ok' if ec < 1e-4 else '>= 1e-4 no cumple'})")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
