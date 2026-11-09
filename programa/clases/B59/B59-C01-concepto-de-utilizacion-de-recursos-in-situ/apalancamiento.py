"""B59-C01 · Apalancamiento de masa de la utilización de recursos in situ (ISRU).

Datos: gravedad estándar g0 = 9,80665 m/s² (NIST, CODATA 2022, exacta). Todo lo demás es
ILUSTRATIVO (no consultado): Isp, delta-v, masas y razón de apalancamiento.
Modelo: ecuación del cohete de Tsiolkovsky, empuje de un solo tramo, sin pérdidas por gravedad
ni por arrastre incluidas en el delta-v (se da el delta-v efectivo). Unidades SI.
Sistema de referencia: masas en la superficie de destino (cuerpo genérico) y en órbita terrestre baja (LEO).
Dominio de validez: masas secas fijas; mezcla O/F constante; sin evaporación.
Tolerancia: 0,1 % entre la fórmula cerrada y la integración numérica.
Prueba que detiene la ejecución: la integración paso a paso reproduce el delta-v con 0,1 %.
"""
import math
import platform

G0 = 9.80665          # m/s^2, NIST CODATA 2022 (exacta)
ISP = 360.0           # s, ILUSTRATIVO (motor O2/CH4 en vacío)
DV = 4100.0           # m/s, ILUSTRATIVO (ascenso de superficie a órbita baja del destino)
M_FINAL = 2500.0      # kg, ILUSTRATIVO (etapa seca + carga útil)
OF = 3.5              # razón masa oxidante / masa combustible, ILUSTRATIVA
GEAR = 6.0            # kg en LEO por kg aterrizado en destino, ILUSTRATIVO
M_PLANTA = 1200.0     # kg, ILUSTRATIVO (masa de la planta que produce el oxidante)


def propelente(dv, isp, m_final):
    return m_final * (math.exp(dv / (isp * G0)) - 1.0)


def delta_v_numerico(m_final, m_prop, isp, pasos=200000):
    """Integra dv = Isp g0 dm/m quemando m_prop en 'pasos' trozos (regla del punto medio)."""
    dm = m_prop / pasos
    m = m_final + m_prop
    dv = 0.0
    for _ in range(pasos):
        dv += isp * G0 * dm / (m - dm / 2.0)
        m -= dm
    return dv


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    mp = propelente(DV, ISP, M_FINAL)
    m_ox = mp * OF / (1.0 + OF)
    m_fu = mp - m_ox
    print(f"Razon de masas exp(dv/(Isp g0)) = {math.exp(DV/(ISP*G0)):.4f}")
    print(f"Propelente total = {mp:.1f} kg ; oxidante = {m_ox:.1f} kg ({100*m_ox/mp:.1f} %) ; combustible = {m_fu:.1f} kg")

    dv_num = delta_v_numerico(M_FINAL, mp, ISP)
    err = abs(dv_num - DV) / DV
    print(f"Delta-v por integracion numerica = {dv_num:.2f} m/s ; error relativo = {err:.2e}")
    assert err < 1e-3, "la integracion no reproduce el delta-v"

    # Masa aterrizada y masa en LEO: llevar todo frente a producir el oxidante en destino
    aterrizada_todo = M_FINAL + mp
    aterrizada_isru = M_FINAL + m_fu + M_PLANTA
    leo_todo = GEAR * aterrizada_todo
    leo_isru = GEAR * aterrizada_isru
    print(f"Masa aterrizada: todo desde la Tierra = {aterrizada_todo:.0f} kg ; con ISRU = {aterrizada_isru:.0f} kg")
    print(f"Masa en LEO    : todo desde la Tierra = {leo_todo:.0f} kg ; con ISRU = {leo_isru:.0f} kg")
    ahorro = leo_todo - leo_isru
    print(f"Ahorro en LEO por un ascenso = {ahorro:.0f} kg ({100*ahorro/leo_todo:.1f} %)")

    # Masa de planta que anula el ahorro (punto de equilibrio) y numero de ascensos que amortizan la planta
    m_planta_eq = m_ox
    print(f"Masa de planta de equilibrio para un solo ascenso = {m_planta_eq:.0f} kg")
    n_asc = M_PLANTA / m_ox
    print(f"Ascensos para amortizar la planta (si se reutiliza) = {n_asc:.2f}")

    # Comprobacion cruzada: bisecando el propelente que da el delta-v pedido
    lo, hi = 0.0, 100.0 * M_FINAL
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if M_FINAL * 0 + ISP * G0 * math.log((M_FINAL + mid) / M_FINAL) < DV:
            lo = mid
        else:
            hi = mid
    print(f"Propelente por biseccion = {0.5*(lo+hi):.3f} kg (formula cerrada {mp:.3f} kg)")
    assert abs(0.5 * (lo + hi) - mp) < 1e-6
    # sensibilidad: +-10 % en el Isp
    for f in (0.9, 1.1):
        mp2 = propelente(DV, ISP * f, M_FINAL)
        print(f"Isp x{f:.1f}: propelente = {mp2:.0f} kg ({100*(mp2-mp)/mp:+.1f} %)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
