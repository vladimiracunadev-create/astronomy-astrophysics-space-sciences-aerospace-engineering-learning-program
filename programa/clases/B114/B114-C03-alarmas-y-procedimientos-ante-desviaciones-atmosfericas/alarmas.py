"""B114-C03 - Alarmas de atmosfera en un habitat SINTETICO.

Unidades: mmHg (ppCO2), kg, m3, K, min. Datos SINTETICOS (semilla fija). Solo stdlib.
R = 8.314462618 J/(mol K) (CODATA 2022). Umbral de 3 mmHg de ppCO2: valor de
NASA-STD-3001 Vol. 2 [V2 6004] citado en OCHMO-TB-004 (consultada 2026-11-10);
los demas umbrales y parametros son ILUSTRATIVOS.
"""
import random
import sys

R = 8.314462618
M_CO2 = 0.04401          # kg/mol
MMHG = 133.322368        # Pa por mmHg
T = 295.15               # K, ilustrativo
V = 100.0                # m3, ilustrativo
GEN = 1.0 / 86400.0      # kg/s por persona (1 kg/dia, ilustrativo)
SIGMA = 0.15             # mmHg, ruido del sensor (sintetico)
UMBRAL = 3.0             # mmHg (NASA OCHMO-TB-004, V2 6004)
UMBRAL_BAJO = 2.7        # mmHg, histeresis (ilustrativo)


def pp_desde_masa(m):
    """ppCO2 [mmHg] de una masa m [kg] de CO2 en V a T (gas ideal)."""
    return m / M_CO2 * R * T / V / MMHG


def alarma(serie, umbral, bajo, n_conf, m_conf):
    """Alarma con confirmacion m de n e histeresis. Devuelve indice del primer
    disparo y numero de disparos (activaciones)."""
    activa = False
    disp = 0
    primero = None
    ventana = []
    for i, x in enumerate(serie):
        ventana.append(x > umbral)
        ventana = ventana[-n_conf:]
        if not activa and sum(ventana) >= m_conf:
            activa = True
            disp += 1
            if primero is None:
                primero = i
        elif activa and x < bajo:
            activa = False
    return primero, disp


def main():
    print("Python", sys.version.split()[0], "(biblioteca estandar)")
    print("Habitat SINTETICO: V = %.0f m3, T = %.2f K, %.1f kg CO2/dia/persona (ilustrativo)"
          % (V, T, GEN * 86400))
    # 1. Acumulacion sin eliminacion
    print("ppCO2 por persona y hora sin eliminacion:")
    for n in (1, 4):
        dm = n * GEN * 3600
        print("  %d persona(s): +%.4f mmHg/h ; 3 mmHg en %.1f h"
              % (n, pp_desde_masa(dm), UMBRAL / pp_desde_masa(dm)))
    pph = pp_desde_masa(4 * GEN * 3600)
    # Verificacion por segunda via: ppCO2 = fraccion molar * P (1 atm)
    n_mol = 4 * GEN * 3600 / M_CO2
    n_aire = 101325.0 * V / (R * T)
    pp2 = n_mol / n_aire * 760.0
    print("  segunda via (fraccion molar x 760 mmHg), 4 personas, 1 h: %.4f mmHg" % pp2)
    assert abs(pph - pp2) / pph < 0.01
    # 2. Falsos positivos en regimen nominal (ppCO2 media 2.6 mmHg), 30 dias, 1 muestra/min
    rng = random.Random(114)
    nom = [2.6 + rng.gauss(0, SIGMA) for _ in range(30 * 1440)]
    print("Regimen nominal 30 dias (sintetico), ppCO2 media 2.6 mmHg, sigma = %.2f:" % SIGMA)
    for (n, m, nombre) in ((1, 1, "simple (1 de 1)"), (5, 3, "confirmada (3 de 5)")):
        _, d = alarma(nom, UMBRAL, UMBRAL_BAJO, n, m)
        print("  %-22s falsas alarmas = %d" % (nombre, d))
    # 3. Retraso de deteccion ante una rampa (fallo del eliminador de CO2)
    rampa = []
    rng2 = random.Random(115)
    pend = pph / 60.0     # mmHg por minuto con 4 personas
    for i in range(600):
        rampa.append(2.2 + pend * i + rng2.gauss(0, SIGMA))
    cruce = (UMBRAL - 2.2) / pend
    print("Rampa (4 personas, sin eliminacion): cruce teorico a los %.1f min" % cruce)
    resultados = {}
    for (n, m, nombre) in ((1, 1, "simple"), (5, 3, "3 de 5")):
        i, _ = alarma(rampa, UMBRAL, UMBRAL_BAJO, n, m)
        resultados[nombre] = i
        print("  alarma %-7s dispara en el minuto %d (desfase = %d min; negativo = antes del cruce, por ruido)"
              % (nombre, i, i - round(cruce)))
    # 4. Histeresis: senal oscilando alrededor del umbral
    osc = [UMBRAL + 0.12 * ((-1) ** i) + rng.gauss(0, 0.05) for i in range(200)]
    _, d_sin = alarma(osc, UMBRAL, UMBRAL, 1, 1)
    _, d_con = alarma(osc, UMBRAL, UMBRAL_BAJO, 1, 1)
    print("Senal oscilante en el umbral: activaciones sin histeresis = %d ; con = %d"
          % (d_sin, d_con))
    assert d_con < d_sin
    assert resultados["3 de 5"] >= resultados["simple"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
