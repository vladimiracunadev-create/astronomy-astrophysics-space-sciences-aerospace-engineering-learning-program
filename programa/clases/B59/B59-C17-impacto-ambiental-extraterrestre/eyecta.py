"""B59-C17 · Impacto ambiental: alcance balístico de eyecta en vacío y fracción que escapa.

Datos ILUSTRATIVOS (no consultados): parámetro gravitatorio GM = 4 902,8 km^3/s^2 y radio R = 1 737,4 km de la Luna
(valores de ejemplo, no consultados); distribución de velocidades de eyecta lognormal con mediana 150 m/s y GSD 3;
ángulo de lanzamiento 45 grados. Contexto de política consultado el 2026-11-09 (COSPAR, página del Panel de
Protección Planetaria): la política es voluntaria; las regiones polares y las sombras permanentes de la Luna
requieren más documentación.
Modelo: partícula puntual en vacío bajo gravedad central 1/r^2, integrada con RK4 en 2D; se compara el alcance
con la fórmula plana v^2 sin(2θ)/g (válida para alcances << R) y se verifica la conservación de energía.
Velocidad de escape v_esc = sqrt(2 GM/R). Unidades SI. Sin atmósfera, sin rotación, sin colisiones entre partículas.
Tolerancias: deriva de energía < 1e-9 relativa; plana frente a RK4 < 1 % para v = 100 m/s.
"""
import math
import platform
import random

GM = 4902.8e9          # m^3/s^2, ILUSTRATIVO
R = 1737.4e3           # m, ILUSTRATIVO
G0 = GM / R ** 2
SEMILLA = 20261109


def alcance_rk4(v, ang_deg, dt=0.5):
    th = math.radians(ang_deg)
    x, y = R, 0.0                      # posicion en el plano; el punto de lanzamiento esta en (R, 0)
    # velocidad: componente radial = v sin(th) (hacia arriba), tangencial = v cos(th)
    vx, vy = v * math.sin(th), v * math.cos(th)
    e0 = 0.5 * (vx * vx + vy * vy) - GM / math.hypot(x, y)

    def acel(px, py):
        r3 = math.hypot(px, py) ** 3
        return -GM * px / r3, -GM * py / r3

    t = 0.0
    while True:
        k1x, k1y = vx, vy
        a1x, a1y = acel(x, y)
        k2x, k2y = vx + 0.5 * dt * a1x, vy + 0.5 * dt * a1y
        a2x, a2y = acel(x + 0.5 * dt * k1x, y + 0.5 * dt * k1y)
        k3x, k3y = vx + 0.5 * dt * a2x, vy + 0.5 * dt * a2y
        a3x, a3y = acel(x + 0.5 * dt * k2x, y + 0.5 * dt * k2y)
        k4x, k4y = vx + dt * a3x, vy + dt * a3y
        a4x, a4y = acel(x + dt * k3x, y + dt * k3y)
        xn = x + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        yn = y + dt / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
        vxn = vx + dt / 6 * (a1x + 2 * a2x + 2 * a3x + a4x)
        vyn = vy + dt / 6 * (a1y + 2 * a2y + 2 * a3y + a4y)
        if math.hypot(xn, yn) <= R and t > dt:
            # interpolacion lineal al radio R
            r0, r1 = math.hypot(x, y), math.hypot(xn, yn)
            f = (r0 - R) / (r0 - r1)
            xc, yc = x + f * (xn - x), y + f * (yn - y)
            ang = math.atan2(yc, xc)
            e1 = 0.5 * (vxn ** 2 + vyn ** 2) - GM / r1
            return R * ang, t + f * dt, abs(e1 - e0) / abs(e0)
        x, y, vx, vy = xn, yn, vxn, vyn
        t += dt
        if t > 1e6:
            raise RuntimeError("no regresa")


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    v_esc = math.sqrt(2 * GM / R)
    print(f"g superficial = {G0:.4f} m/s^2 ; velocidad de escape = {v_esc:.1f} m/s ; velocidad circular = {math.sqrt(GM/R):.1f} m/s")
    print("v [m/s]   alcance RK4 [km]   alcance plano [km]   diferencia   t vuelo [s]   deriva de energia")
    for v in (100.0, 300.0, 800.0, 1200.0):
        rng_, tv, drift = alcance_rk4(v, 45.0)
        plano = v * v * math.sin(math.radians(90.0)) / G0
        print(f"{v:7.0f}   {rng_/1e3:16.3f}   {plano/1e3:18.3f}   {100*(plano-rng_)/rng_:9.2f} %   {tv:10.1f}   {drift:.1e}")
        assert drift < 1e-9
        if v == 100.0:
            assert abs(plano - rng_) / rng_ < 0.01
    # Monte Carlo de velocidades
    rnd = random.Random(SEMILLA)
    N = 20000
    mu, sg = math.log(150.0), math.log(3.0)
    vs = [math.exp(rnd.gauss(mu, sg)) for _ in range(N)]
    esc = sum(1 for v in vs if v >= v_esc) / N
    f_1km = sum(1 for v in vs if v * v / G0 <= 1000.0) / N
    f_100km = sum(1 for v in vs if v * v / G0 > 100e3 and v < v_esc) / N
    print(f"Distribucion lognormal (mediana 150 m/s, GSD 3, {N} particulas): escapan {100*esc:.3f} % ; caen a menos de 1 km {100*f_1km:.1f} % ; caen a mas de 100 km {100*f_100km:.2f} %")
    # analitico: P(v >= v_esc) = 1 - Phi((ln v_esc - mu)/sg)
    from statistics import NormalDist
    pe = 1 - NormalDist().cdf((math.log(v_esc) - mu) / sg)
    print(f"Probabilidad analitica de escape = {100*pe:.3f} % (muestral {100*esc:.3f} %)")
    assert abs(pe - esc) < 0.003
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
