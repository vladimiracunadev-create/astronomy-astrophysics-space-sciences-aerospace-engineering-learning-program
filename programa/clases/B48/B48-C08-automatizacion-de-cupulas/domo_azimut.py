"""Azimut de cúpula para un telescopio descentrado del centro de la cúpula.

Datos: radio de cúpula 3,0 m y telescopio en (0,5 m; 0 m; 1,0 m) respecto del centro, ILUSTRATIVOS
(no es la geometría de ninguna cúpula real). No se consultó ninguna fuente externa.
Modelo: el eje óptico parte de P con dirección u(A, h); la ranura debe estar donde la recta corta la esfera:
t = -b + sqrt(b^2 - c), b = P.u, c = |P|^2 - R^2; azimut de cúpula = atan2(x, y) (desde el norte hacia el este).
Segunda vía: bisección sobre f(t) = |P + t u|^2 - R^2 en [0, 2R].
Supuestos: cúpula esférica, ejes de la montura concurrentes en P, sin desplazamiento del punto de pivote con la altitud.
Tolerancia: 1e-9 grados entre la cuadrática y la bisección; error de seguimiento máximo sin corrección calculado en el barrido.
"""
import math

R = 3.0
P = (0.5, 0.0, 1.0)


def dirvec(az, alt):
    a, h = math.radians(az), math.radians(alt)
    return (math.sin(a) * math.cos(h), math.cos(a) * math.cos(h), math.sin(h))


def punto_cuadratica(u):
    b = sum(p * q for p, q in zip(P, u))
    c = sum(p * p for p in P) - R * R
    t = -b + math.sqrt(b * b - c)
    return t, tuple(p + t * q for p, q in zip(P, u))


def punto_biseccion(u):
    def f(t):
        return sum((p + t * q) ** 2 for p, q in zip(P, u)) - R * R
    lo, hi = 0.0, 2 * R
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    t = 0.5 * (lo + hi)
    return t, tuple(p + t * q for p, q in zip(P, u))


def az_cupula(pt):
    return math.degrees(math.atan2(pt[0], pt[1])) % 360.0


def dif(a, b):
    return (a - b + 180.0) % 360.0 - 180.0


def calc():
    filas = []
    peor = 0.0
    maximo = (0, 0)
    for alt in (20.0, 45.0, 70.0):
        for az in range(0, 360, 5):
            u = dirvec(az, alt)
            t1, p1 = punto_cuadratica(u)
            t2, p2 = punto_biseccion(u)
            a1, a2 = az_cupula(p1), az_cupula(p2)
            peor = max(peor, abs(dif(a1, a2)))
            e = dif(a1, az)
            if alt == 45.0 and abs(e) > abs(maximo[0]):
                maximo = (e, az)
            if alt == 45.0 and az in (0, 90, 180, 270):
                filas.append((az, a1, e, math.sqrt(sum(x * x for x in p1))))
    return dict(filas=filas, peor=peor, maximo=maximo)


def main():
    R_ = calc()
    for az, a1, e, r in R_["filas"]:
        print(f"Telescopio az {az:3d}° alt 45°: cúpula {a1:8.4f}°, diferencia {e:+8.4f}°, |punto| = {r:.6f} m")
    print(f"Diferencia máxima cuadrática-bisección: {R_['peor']:.2e}°")
    print(f"Error máximo sin corrección a 45°: {R_['maximo'][0]:+.3f}° en az {R_['maximo'][1]}°")
    assert R_["peor"] < 1e-9
    assert all(abs(r - R) < 1e-9 for *_, r in R_["filas"])
    assert abs(R_["filas"][0][2]) > 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
