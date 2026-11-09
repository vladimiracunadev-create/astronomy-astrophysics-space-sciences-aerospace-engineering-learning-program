"""B59-C07 · Purificación de agua por destilación: balance de sales, recuperación y energía.

Datos: masa molar del agua 18,0153 g/mol (NIST WebBook, consultada 2026-11-09; se usa solo para la
estequiometría del ejercicio). Todo lo demás es ILUSTRATIVO (no consultado): salinidad de alimentación
2 g/kg, límite de solubilidad 250 g/kg, calor latente de vaporización 2,26 MJ/kg, arrastre de salmuera
en el vapor 1e-4, efectividad de recuperación de calor 0,85.
Modelo: destilación por lotes (Rayleigh) y en régimen continuo con recuperación r.
 - Continuo: c_b = c0/(1 - r + r*phi); c_d = phi*c_b; balance de sal c0 = r c_d + (1 - r) c_b.
 - Lote: c_b(M) = c0 (M0/M)^(1-phi) integrando paso a paso y comparando con la fórmula cerrada.
 - Energía térmica específica: E = L (1 - eps_hx) por kg de destilado (calor latente neto tras recuperación).
Unidades: g/kg, kg, MJ/kg. Sin incrustación, sin compuestos volátiles, sin la energía de bombeo.
Tolerancia: lote numérico frente a cerrado < 1e-4 relativo; cierre de sales < 1e-12.
"""
import math
import platform

C0, C_MAX = 2.0, 250.0
L_V = 2.26             # MJ/kg, ILUSTRATIVO
PHI = 1e-4
EPS_HX = 0.85


def continuo(r, c0=C0, phi=PHI):
    c_b = c0 / (1 - r + r * phi)
    c_d = phi * c_b
    return c_b, c_d


def lote_numerico(frac_final, c0=C0, phi=PHI, pasos=200000):
    """Evapora una fraccion del lote; devuelve la concentracion final de salmuera."""
    M = 1.0
    sal = c0 * M                      # g de sal por kg inicial (masa de liquido = 1 kg)
    dM = (1.0 - frac_final) / pasos
    for _ in range(pasos):
        c = sal / M
        sal -= phi * c * dM           # el vapor arrastra una fraccion phi de la concentracion
        M -= dM
    return sal / M


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(" r [%]   c_salmuera [g/kg]   c_destilado [g/kg]   cierre de sal [g/kg]")
    for r in (0.5, 0.9, 0.99):
        cb, cd = continuo(r)
        cierre = r * cd + (1 - r) * cb - C0
        print(f"{100*r:6.1f}   {cb:16.2f}   {cd:17.4f}   {cierre:19.2e}")
        assert abs(cierre) < 1e-12
    r_max = 1 - C0 / C_MAX       # sin arrastre
    print(f"Recuperacion maxima por solubilidad (phi = 0): r_max = 1 - c0/c_max = {100*r_max:.2f} %")
    cb, _ = continuo(r_max, phi=0.0)
    assert abs(cb - C_MAX) < 1e-9

    # Lote
    for f in (0.5, 0.1, 0.01):
        cn = lote_numerico(f)
        cc = C0 * (1.0 / f) ** (1 - PHI)
        err = abs(cn - cc) / cc
        print(f"Lote: queda {100*f:.0f} % del liquido -> salmuera numerica {cn:.3f} g/kg ; cerrada {cc:.3f} g/kg ; error {err:.1e}")
        assert err < 1e-4
    # Energia
    e_neta = L_V * (1 - EPS_HX)
    print(f"Calor latente bruto = {L_V:.2f} MJ/kg ; neto con recuperacion {EPS_HX:.2f} = {e_neta:.3f} MJ/kg = {e_neta/3.6:.4f} kWh/kg de destilado")
    # Energia por kg de ALIMENTACION segun recuperacion
    for r in (0.5, 0.9, 0.99):
        print(f"r = {100*r:.0f} %: {r*e_neta:.3f} MJ por kg de alimentacion ; salmuera a desechar = {1-r:.2f} kg/kg")
    # Estequiometria: moles de agua en 1 kg de destilado
    print(f"Moles de agua en 1 kg = {1000/18.0153:.2f} mol")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
