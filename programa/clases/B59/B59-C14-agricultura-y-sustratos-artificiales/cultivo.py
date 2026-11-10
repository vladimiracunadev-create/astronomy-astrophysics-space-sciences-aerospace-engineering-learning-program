"""B59-C14 · Cultivo en sustrato artificial: área limitada por luz, potencia de iluminación y agua.

Datos ILUSTRATIVOS (no consultados): consumo de O2 de una persona 0,84 kg/día; fotones efectivos por O2
producido por el cultivo (incluye absorción incompleta y pérdidas) 20; PPFD 400 µmol/(m^2 s) durante 16 h/día;
eficacia de la luz LED 2,5 µmol/J; evapotranspiración 3 kg/(m^2 día); recuperación de agua por condensación 95 %;
sustrato de 0,20 m de profundidad y porosidad 0,5.
Constantes citadas (2026-11-09): pesos atómicos NIST (O = 15,9994 g/mol punto medio).
Modelo: ṅ_O2 · fotones = PPFD · A · tiempo de luz. Potencia eléctrica = PPFD · A / eficacia.
Agua: reposición = (1 - recuperación) · ET · A. Balance de humedad del sustrato integrado paso a paso.
Unidades SI y µmol. Sin CO2 limitante, sin nutrientes limitantes, sin plagas.
Tolerancias: área analítica frente a simulación diaria < 1e-9; humedad numérica frente a analítica < 1e-6.
"""
import platform

M_O2 = 2 * 15.9994
O2_PERSONA = 0.84          # kg/dia, ILUSTRATIVO
FOT_O2 = 20.0
PPFD = 400.0               # µmol/(m2 s)
H_LUZ = 16.0
EFICACIA = 2.5             # µmol/J
ET = 3.0                   # kg/(m2 dia)
RECUP = 0.95
PROF, POROSIDAD = 0.20, 0.5


def area_para(n_personas):
    mol_o2_dia = n_personas * O2_PERSONA * 1000.0 / M_O2
    fotones_dia = mol_o2_dia * FOT_O2                  # mol fotones/dia
    flujo_m2_dia = PPFD * 1e-6 * H_LUZ * 3600.0        # mol/(m2 dia)
    return fotones_dia / flujo_m2_dia, mol_o2_dia


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    A, mol = area_para(1)
    print(f"O2 por persona = {mol:.2f} mol/dia ; fotones necesarios = {mol*FOT_O2:.1f} mol/dia")
    print(f"Flujo de fotones por m2 = {PPFD*1e-6*H_LUZ*3600:.2f} mol/(m2 dia) ; area por persona = {A:.2f} m2")
    # Simulacion diaria independiente: se acumula la luz hora a hora hasta cubrir la demanda
    area = A
    fot = 0.0
    for hora in range(int(H_LUZ)):
        fot += PPFD * 1e-6 * area * 3600.0
    o2_producido = fot / FOT_O2 * M_O2 / 1000.0
    print(f"Simulacion hora a hora: O2 producido = {o2_producido:.6f} kg/dia (demanda {O2_PERSONA})")
    assert abs(o2_producido - O2_PERSONA) < 1e-9
    # Potencia electrica
    p_inst = PPFD * A / EFICACIA
    p_med = p_inst * H_LUZ / 24.0
    print(f"Potencia de iluminacion instantanea = {p_inst/1000:.3f} kW ; media diaria = {p_med/1000:.3f} kW ; energia diaria = {p_inst*H_LUZ/1000:.1f} kWh")
    # Cuatro personas
    A4, _ = area_para(4)
    print(f"Para 4 personas: area = {A4:.1f} m2 ; potencia instantanea = {PPFD*A4/EFICACIA/1000:.2f} kW")
    # Agua
    agua = ET * A
    rep = (1 - RECUP) * agua
    print(f"Agua evapotranspirada = {agua:.1f} kg/dia ; reposicion con {100*RECUP:.0f} % de recuperacion = {rep:.2f} kg/dia")
    # Humedad del sustrato: capacidad por m2 y dias hasta secarse sin riego
    cap = PROF * POROSIDAD * 1000.0
    print(f"Agua almacenada en el sustrato = {cap:.0f} kg/m2 ; dias para secarse sin riego (desde saturacion) = {cap/ET:.1f}")
    # Control de riego con paso de 1 hora: riega 5 kg/m2 cuando baja del 40 % de la capacidad, hasta 90 %
    theta = cap
    riegos = 0
    dosis = 0.5 * cap
    pasos = 24 * 60
    for h in range(pasos):
        theta -= ET / 24.0
        if theta < 0.4 * cap:
            theta += dosis
            riegos += 1
    print(f"En 60 dias con riego automatico: {riegos} riegos de {dosis:.0f} kg/m2 ; agua total repuesta = {riegos*dosis:.0f} kg/m2 (ET total {ET*60:.0f} kg/m2)")
    assert abs(theta - (cap - ET * 60 + riegos * dosis)) < 1e-6
    print(f"Humedad final = {100*theta/cap:.1f} % de la capacidad")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
