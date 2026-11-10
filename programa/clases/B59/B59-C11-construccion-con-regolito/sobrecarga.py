"""B59-C11 · Construcción con regolito: sobrecarga, equilibrio con la presión interna y blindaje.

Datos ILUSTRATIVOS (no consultados): gravedad superficial 1,62 m/s², densidad aparente del regolito
rho(z) = 1300 + 600 z/(z + 0,5) kg/m^3 (z = profundidad en m, aumenta con la profundidad), longitud de
atenuación de la radiación lambda = 80 g/cm^2 (modelo exponencial), recipiente cilíndrico de radio 2 m y
pared de 3 mm de acero con tensión admisible 150 MPa. Presión interna 60 kPa.
Modelo: presión de sobrecarga P(h) = g * integral_0^h rho dz; el regolito equilibra la presión interna cuando
P(h) = P_int. Transmisión de la radiación T = exp(-x/lambda) con x = masa por área atravesada (g/cm^2).
Unidades SI salvo x en g/cm^2. Sin sismos, sin cargas térmicas, sin cohesión del regolito.
Tolerancias: integral numérica frente a analítica < 1e-8 relativo; bisección frente a h analítico (densidad
constante) < 1e-9.
"""
import math
import platform

G = 1.62                  # m/s^2, ILUSTRATIVA
RS, RD, Z0 = 1300.0, 1900.0, 0.5
LAM = 80.0                # g/cm^2, ILUSTRATIVA
P_INT = 60e3              # Pa
R_REC, T_PARED, S_ADM = 2.0, 3e-3, 150e6


def rho(z):
    return RS + (RD - RS) * z / (z + Z0)


def masa_por_area(h):
    """Integral analitica de rho de 0 a h [kg/m^2]."""
    return RS * h + (RD - RS) * (h - Z0 * math.log(1 + h / Z0))


def trapecio(f, a, b, n=200000):
    d = (b - a) / n
    return d * (0.5 * f(a) + sum(f(a + i * d) for i in range(1, n)) + 0.5 * f(b))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for h in (0.5, 2.0, 5.0):
        num = trapecio(rho, 0.0, h)
        an = masa_por_area(h)
        print(f"h = {h:4.1f} m: masa por area numerica = {num:10.3f} kg/m^2 ; analitica = {an:10.3f} ; error {abs(num-an)/an:.1e}")
        assert abs(num - an) / an < 1e-8
    # Profundidad que equilibra P_int
    lo, hi = 0.0, 200.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if G * masa_por_area(mid) < P_INT:
            lo = mid
        else:
            hi = mid
    h_eq = 0.5 * (lo + hi)
    h_const = P_INT / (G * 1500.0)
    print(f"Profundidad de equilibrio con rho(z) variable = {h_eq:.2f} m ; con rho = 1500 constante = {h_const:.2f} m")
    # Prueba: bisección con densidad constante recupera P/(rho g)
    lo, hi = 0.0, 200.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if G * 1500.0 * mid < P_INT:
            lo = mid
        else:
            hi = mid
    assert abs(0.5 * (lo + hi) - h_const) < 1e-9
    # Con presion de 101 kPa
    for p in (60e3, 101e3):
        lo, hi = 0.0, 500.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if G * masa_por_area(mid) < p:
                lo = mid
            else:
                hi = mid
        print(f"Profundidad para equilibrar {p/1e3:.0f} kPa = {0.5*(lo+hi):.1f} m ({masa_por_area(0.5*(lo+hi))/1e3:.1f} t/m^2)")
    # Esfuerzo de aro del recipiente
    sig = P_INT * R_REC / T_PARED
    print(f"Esfuerzo de aro P r / t = {sig/1e6:.1f} MPa (admisible {S_ADM/1e6:.0f} MPa) ; margen = {S_ADM/sig:.2f}")
    t_min = P_INT * R_REC / S_ADM
    print(f"Espesor minimo de pared = {t_min*1e3:.2f} mm")
    # Blindaje: x = rho h, 1 kg/m^2 = 0,1 g/cm^2
    print()
    print("Espesor de regolito [m]   masa por area [g/cm^2]   transmision exp(-x/lambda)")
    for h in (0.5, 1.0, 2.0, 3.0):
        x = masa_por_area(h) * 0.1
        print(f"{h:22.1f}   {x:20.1f}   {math.exp(-x/LAM):24.2e}")
    # espesor para reducir a 10 %
    x10 = LAM * math.log(10.0)
    lo, hi = 0.0, 50.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if masa_por_area(mid) * 0.1 < x10:
            lo = mid
        else:
            hi = mid
    print(f"Para transmitir el 10 %: x = lambda ln10 = {x10:.1f} g/cm^2 -> espesor = {0.5*(lo+hi):.2f} m")
    assert abs(math.exp(-x10 / LAM) - 0.1) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
