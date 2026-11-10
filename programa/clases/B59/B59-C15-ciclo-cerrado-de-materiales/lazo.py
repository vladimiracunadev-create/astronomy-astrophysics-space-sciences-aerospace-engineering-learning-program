"""B59-C15 · Ciclo cerrado de materiales: reposición, serie geométrica e inventario de un lazo con retardo.

Datos ILUSTRATIVOS (no consultados): demanda de agua D = 25 kg/día (tripulación hipotética), etapas de
recuperación en serie con eficiencias 0,90 · 0,98 · 0,99 (la fracción global es su producto), retardo de
recuperación de 3 días, misión de 500 días, inventario inicial D*retardo.
Modelo: cada día se usan D kg; una fracción rho vuelve tras 'retardo' días; la reposición cubre el resto.
Resultados analíticos: reposición de régimen = D (1 - rho); reposición total = D*T - rho*D*(T - retardo);
ciclos por kg de reposición = 1/(1 - rho) (suma de la serie geométrica sum rho^k).
Unidades: kg, días. Sin fugas variables, sin acumulación de contaminantes.
Tolerancia: simulación diaria frente a analítica < 1e-9 relativo.
"""
import platform

D = 25.0
ETAPAS = (0.90, 0.98, 0.99)
RETARDO = 3
T = 500


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rho = 1.0
    for e in ETAPAS:
        rho *= e
    print(f"Recuperacion global = {ETAPAS[0]} x {ETAPAS[1]} x {ETAPAS[2]} = {rho:.5f}")
    # Regimen estacionario: la cola de retorno empieza ya con rho*D por dia
    def simular2(rho_):
        cola = [rho_ * D] * RETARDO
        total = 0.0
        for dia in range(T):
            vuelve = cola.pop(0)
            cola.append(rho_ * D)
            total += D - vuelve
        return total
    sim = simular2(rho)
    an = D * (1 - rho) * T
    print(f"Reposicion de regimen = {D*(1-rho):.4f} kg/dia ; total en {T} dias: simulada = {sim:.4f} kg ; analitica = {an:.4f} kg")
    assert abs(sim - an) / an < 1e-9
    # Arranque sin recuperacion previa (la cola empieza vacia)
    def simular_arranque(rho_):
        cola = [0.0] * RETARDO
        total = 0.0
        for dia in range(T):
            vuelve = cola.pop(0)
            cola.append(rho_ * D)
            total += D - vuelve
        return total
    sim2 = simular_arranque(rho)
    an2 = D * T - rho * D * (T - RETARDO)
    print(f"Con arranque en frio (cola vacia): total simulado = {sim2:.4f} kg ; analitico D T - rho D (T - retardo) = {an2:.4f} kg")
    assert abs(sim2 - an2) / an2 < 1e-9
    sin_lazo = D * T
    print(f"Sin lazo: {sin_lazo:.0f} kg ; con lazo: {sim2:.0f} kg ; ahorro = {sin_lazo - sim2:.0f} kg ({100*(1-sim2/sin_lazo):.1f} %)")
    # Serie geometrica
    s = sum(rho ** k for k in range(0, 100000))
    print(f"Ciclos por kg de reposicion: 1/(1 - rho) = {1/(1-rho):.3f} ; suma de la serie = {s:.3f}")
    assert abs(s - 1 / (1 - rho)) < 1e-6
    # Sensibilidad a cada etapa
    print("Efecto de mejorar una etapa a 0,999:")
    for i, e in enumerate(ETAPAS):
        r2 = rho / e * 0.999
        print(f"  etapa {i+1} ({e} -> 0,999): rho = {r2:.5f} ; reposicion = {D*(1-r2):.4f} kg/dia")
    # Fugas: un 0,5 %/dia de perdida del inventario en circulacion
    print(f"Inventario en transito (retardo {RETARDO} d) = {D*RETARDO:.0f} kg ; reposicion de fugas 0,5 %/dia = {0.005*D*RETARDO:.3f} kg/dia")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
