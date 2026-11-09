"""Adaptador común sobre dos estilos de protocolo de control instrumental y latencia del sondeo.

Datos: MODELO DE JUGUETE. Un estilo basado en propiedades con estados (Idle, Ok, Busy, Alert) y otro basado
en métodos con una propiedad booleana de movimiento; ninguno implementa ASCOM ni INDI reales: solo
reproducen la IDEA de cada familia (interfaces por tipo de dispositivo; propiedades expuestas por drivers). Las páginas
oficiales consultadas el 2026-11-09 NO confirmaron los nombres de estados Idle/Ok/Busy/Alert: se usan como convención del juguete.
Montura simulada con velocidad de 3,0 grados/s y azimut inicial 10,0 grados; reloj simulado (sin esperas).
Modelo: ambos estilos exponen slew_to(az) y devuelven la posición final y el tiempo simulado; el sondeo con
periodo T detecta un evento uniforme con retardo medio T/2 y máximo T.
Segunda vía: simulación de 200000 eventos con semilla 20261109.
Supuestos: sin red, sin concurrencia, sin errores de hardware salvo el rango inválido.
Tolerancia: resultados idénticos entre estilos (1e-9) y retardo medio a 4 errores estándar de T/2.
"""
import math
import random

VEL = 3.0
AZ0 = 10.0


class MontajeSim:
    def __init__(self):
        self.az = AZ0
        self.t = 0.0

    def mover(self, objetivo):
        d = abs(objetivo - self.az)
        self.t += d / VEL
        self.az = objetivo


class EstiloPropiedades:
    """Escribe una propiedad 'objetivo' y consulta su estado hasta que deja de estar Busy."""
    def __init__(self):
        self.m = MontajeSim()
        self.estado = "Idle"
        self.pend = None

    def set_prop(self, nombre, valor):
        if nombre != "objetivo" or not 0.0 <= valor <= 360.0:
            self.estado = "Alert"
            return
        self.estado = "Busy"
        self.pend = valor

    def get_estado(self):
        if self.estado == "Busy":
            self.m.mover(self.pend)
            self.estado = "Ok"
        return self.estado


class EstiloMetodos:
    """Llama a un método de movimiento y consulta una propiedad booleana de 'moviéndose'."""
    def __init__(self):
        self.m = MontajeSim()
        self._mov = False
        self._dest = None

    def slew_async(self, az):
        if not 0.0 <= az <= 360.0:
            raise ValueError("fuera de rango")
        self._mov, self._dest = True, az

    @property
    def slewing(self):
        if self._mov:
            self.m.mover(self._dest)
            self._mov = False
            return True
        return False


class Adaptador:
    def __init__(self, dispositivo):
        self.d = dispositivo

    def slew_to(self, az):
        if isinstance(self.d, EstiloPropiedades):
            self.d.set_prop("objetivo", az)
            if self.d.estado == "Alert":
                return None
            while self.d.get_estado() == "Busy":
                pass
            return self.d.m.az, self.d.m.t
        try:
            self.d.slew_async(az)
        except ValueError:
            return None
        while self.d.slewing:
            pass
        return self.d.m.az, self.d.m.t


def latencia(T, n=200000):
    rng = random.Random(20261109)
    xs = [T - (rng.random() * T) for _ in range(n)]  # el sondeo llega en T - fase
    m = sum(xs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    return m, sd, max(xs), n


def calc():
    res = {}
    for az in (100.0, 250.0, 400.0):
        a = Adaptador(EstiloPropiedades()).slew_to(az)
        b = Adaptador(EstiloMetodos()).slew_to(az)
        res[az] = (a, b)
    return dict(res=res, lat={T: latencia(T) for T in (1.0, 5.0)})


def main():
    Q = calc()
    for az, (a, b) in Q["res"].items():
        if a is None:
            print(f"Destino {az:.0f}°: ambos estilos rechazan: propiedades {a}, métodos {b}")
        else:
            print(f"Destino {az:.0f}°: propiedades -> az {a[0]:.1f}°, t = {a[1]:.3f} s | métodos -> az {b[0]:.1f}°, t = {b[1]:.3f} s")
    for T, (m, sd, mx, n) in Q["lat"].items():
        print(f"Sondeo cada {T:.0f} s: latencia media {m:.4f} s (teórica {T / 2:.4f}), máxima {mx:.4f} s")
    for az, (a, b) in Q["res"].items():
        if a is None:
            assert b is None
        else:
            assert abs(a[0] - b[0]) < 1e-9 and abs(a[1] - b[1]) < 1e-9
    assert abs(Q["res"][100.0][0][1] - 30.0) < 1e-9
    for T, (m, sd, mx, n) in Q["lat"].items():
        assert abs(m - T / 2) < 4 * sd / math.sqrt(n) and mx <= T
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
