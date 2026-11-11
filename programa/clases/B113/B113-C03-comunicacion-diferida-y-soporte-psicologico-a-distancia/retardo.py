"""B113-C03: retardo de comunicacion Tierra-Marte y ritmo de una sesion de apoyo a distancia.

Retardo de ida L = d / c. Marco: distancia Tierra-Marte (centro a centro, valor de ficha), en km; c en m/s.
Una sesion de duracion T con turnos de s segundos por lado dura 2 s + 2 L por intercambio (A habla,
llega tras L; B responde, llega tras L). Datos: distancias de la ficha de Marte de la NASA/NSSDC
(consultada 2026-11-10) y c exacta (NIST, CODATA 2022). Duracion de sesion y turnos: ILUSTRATIVOS.
Solo biblioteca estandar.
"""
import sys

C = 299_792_458.0  # m/s, exacta
DIST_MIN_KM = 54.6e6  # ficha de Marte, NASA/NSSDC
DIST_MAX_KM = 401.4e6
T_SESION = 50 * 60.0  # s, ilustrativo
TURNO = 60.0  # s por turno de habla, ilustrativo


def retardo_ida(dist_km):
    return dist_km * 1000.0 / C


def intercambios_formula(T, s, L):
    return int(T // (2 * s + 2 * L))


def intercambios_simulados(T, s, L):
    """Simulacion por eventos: devuelve cuantos intercambios completos caben en T."""
    t, n = 0.0, 0
    while True:
        t_llegada_a_b = t + s + L      # A termina de hablar y su mensaje llega a B
        t_llegada_a_a = t_llegada_a_b + s + L  # B responde y su mensaje llega a A
        if t_llegada_a_a > T:
            return n
        n += 1
        t = t_llegada_a_a


def main():
    print("Python %s (biblioteca estandar)" % sys.version.split()[0])
    print("c = %d m/s (exacta); distancias de la ficha de Marte (NASA/NSSDC, 2026-11-10)" % C)
    casos = [
        ("minima", DIST_MIN_KM),
        ("20 min de ida (cifra del informe HRP)", 20 * 60 * C / 1000.0),
        ("maxima", DIST_MAX_KM),
    ]
    print("Sesion ILUSTRATIVA: T = %.0f min, turno = %.0f s por lado" % (T_SESION / 60, TURNO))
    print(" caso                                    dist [10^6 km]  L ida [min]  ida y vuelta [min]  intercambios (formula/sim)")
    res = []
    for nombre, d in casos:
        L = retardo_ida(d)
        nf = intercambios_formula(T_SESION, TURNO, L)
        ns = intercambios_simulados(T_SESION, TURNO, L)
        res.append((L, nf, ns))
        print(" %-38s %12.1f %12.3f %17.3f %12d /%d" % (nombre, d / 1e6, L / 60, 2 * L / 60, nf, ns))
    n0 = intercambios_formula(T_SESION, TURNO, 0.0)
    print("Sin retardo (referencia): %d intercambios en la misma sesion" % n0)
    print("Mensajes asincronos (un mensaje de %.0f s cada sentido): primera respuesta posible tras %.2f min con retardo maximo" % (
        TURNO, (TURNO + 2 * res[2][0] + TURNO) / 60))

    assert abs(retardo_ida(DIST_MIN_KM) - 182.13) < 0.01
    assert abs(retardo_ida(149_597_870.7) - 499.0048) < 1e-3  # 1 UA, valor de comprobacion
    assert all(nf == ns for _, nf, ns in res)
    assert res[0][1] >= res[1][1] >= res[2][1]
    assert n0 == 25
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
