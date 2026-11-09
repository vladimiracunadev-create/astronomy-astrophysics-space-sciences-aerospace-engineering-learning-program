"""Cielo oscuro: suma de brillos en magnitudes y su efecto en el tiempo de exposición.

Datos: brillo natural del cielo 21,6 mag/arcsec^2 y contribución artificial 22,0 mag/arcsec^2; fuente de
50 e-/s, cielo natural de 20 e-/s y ruido de lectura de 5 e-: ILUSTRATIVOS. No se consultó ninguna fuente externa.
Modelo: los flujos se suman, m = -2,5 log10(suma 10^(-0,4 m_i)); el cielo en e-/s escala como 10^(0,4 (m_nat - m)).
Tiempo para una relación señal-ruido S: t = [S^2 (s + b) + sqrt(S^4 (s + b)^2 + 4 s^2 S^2 rn^2)] / (2 s^2).
Segunda vía: simulación de 40000 exposiciones por caso con semilla 20261109 (disparo con normal de varianzas iguales).
Supuestos: cielo conocido y restado sin error; sin gradientes ni nubes; aproximación gaussiana del disparo.
Tolerancia: relación señal-ruido simulada a menos del 1,5 % de la objetivo.
"""
import math
import random

M_NAT, M_ART = 21.6, 22.0
S_E, B_NAT, RN = 50.0, 20.0, 5.0
SNR = 10.0


def suma(*ms):
    return -2.5 * math.log10(sum(10 ** (-0.4 * m) for m in ms))


def tiempo(b, s=S_E, rn=RN, snr=SNR):
    a = snr ** 2 * (s + b)
    return (a + math.sqrt(a * a + 4 * s * s * snr ** 2 * rn ** 2)) / (2 * s * s)


def snr_sim(t, b, rng, n=40000):
    xs = []
    for _ in range(n):
        tot = rng.gauss((S_E + b) * t, math.sqrt((S_E + b) * t + RN ** 2))
        xs.append(tot - b * t)
    m = sum(xs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    return m / sd


def calc():
    rng = random.Random(20261109)
    m_tot = suma(M_NAT, M_ART)
    b_tot = B_NAT * 10 ** (0.4 * (M_NAT - m_tot))
    out = {}
    for nombre, b in (("natural", B_NAT), ("con luz artificial", b_tot)):
        t = tiempo(b)
        out[nombre] = dict(b=b, t=t, snr=snr_sim(t, b, rng))
    return dict(m_tot=m_tot, dm=M_NAT - m_tot, b_tot=b_tot, casos=out, factor=out["con luz artificial"]["t"] / out["natural"]["t"])


def main():
    Q = calc()
    print(f"Brillo total = {Q['m_tot']:.4f} mag/arcsec^2 (más brillante en {Q['dm']:.4f} mag); cielo = {Q['b_tot']:.3f} e-/s")
    for k, v in Q["casos"].items():
        print(f"{k}: cielo {v['b']:.3f} e-/s | tiempo para S/N = {SNR:.0f}: {v['t']:.3f} s | S/N simulada {v['snr']:.3f}")
    print(f"Factor de tiempo por la luz artificial = {Q['factor']:.4f}")
    for v in Q["casos"].values():
        assert abs(v["snr"] / SNR - 1) < 0.015
    assert abs(suma(21.6, 21.6) - (21.6 - 2.5 * math.log10(2))) < 1e-12
    assert Q["factor"] > 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
