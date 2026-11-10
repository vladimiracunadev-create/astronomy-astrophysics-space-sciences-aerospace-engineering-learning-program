"""B96-C19: error de unidades (lbf*s frente a N*s) SINTETICO y su defensa con magnitudes etiquetadas."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: nave de 600 kg y 10 impulsos de 2 N*s a lo largo de 270 dias; NO reproduce los datos de una mision real")
LBF_S_EN_NS = 4.4482216152605        # 1 lbf*s en N*s (definicion: 1 lbf = 4.4482216152605 N)
masa = 600.0
n_imp = 10
I_real = 2.0                            # N*s por evento (valor verdadero)
dias = 270.0
# la salida del software de tierra viene en lbf*s pero el consumidor la lee como N*s
I_reportado_lbf = I_real/LBF_S_EN_NS    # numero que escribe el software de tierra (en lbf*s)
I_leido = I_reportado_lbf               # el consumidor lo interpreta como N*s
dv_real = n_imp*I_real/masa
dv_leido = n_imp*I_leido/masa
print(f"Impulso verdadero por evento = {I_real:.4f} N*s ; numero entregado = {I_reportado_lbf:.4f} (lbf*s) ; leido como N*s = {I_leido:.4f}")
print(f"Delta-v verdadero = {dv_real*1000:.2f} mm/s ; Delta-v modelado = {dv_leido*1000:.2f} mm/s ; error = {(dv_real-dv_leido)*1000:.2f} mm/s ({(1-dv_leido/dv_real)*100:.1f} %)")
# error de posicion acumulado si el error de velocidad actua durante el resto del viaje (aproximacion: deriva lineal)
t_resto = dias*86400/2
err_pos = (dv_real - dv_leido)*t_resto/1000.0     # km
print(f"Error de posicion por deriva lineal durante {t_resto/86400:.0f} dias = {err_pos:.1f} km")
assert abs(I_reportado_lbf*LBF_S_EN_NS - I_real) < 1e-12
assert abs(dv_leido*LBF_S_EN_NS - dv_real) < 1e-12
# defensa: cantidades con unidad; mezclar unidades distintas sin convertir lanza error
class Impulso:
    FACTOR = {"N*s": 1.0, "lbf*s": LBF_S_EN_NS}
    def __init__(self, valor, unidad):
        if unidad not in self.FACTOR: raise ValueError(f"unidad desconocida: {unidad}")
        self.valor, self.unidad = valor, unidad
    def en(self, unidad): return Impulso(self.valor*self.FACTOR[self.unidad]/self.FACTOR[unidad], unidad)
    def __add__(self, otro):
        if self.unidad != otro.unidad: raise TypeError(f"unidades distintas: {self.unidad} y {otro.unidad}")
        return Impulso(self.valor + otro.valor, self.unidad)
a = Impulso(I_reportado_lbf, "lbf*s")
b = Impulso(I_real, "N*s")
try:
    a + b; mezcla = "SIN error (mal)"
except TypeError as e:
    mezcla = f"rechazado: {e}"
print("Sumar lbf*s con N*s ->", mezcla)
suma = a.en("N*s") + b
print(f"Con conversion explicita: {a.en('N*s').valor:.4f} N*s + {b.valor:.4f} N*s = {suma.valor:.4f} {suma.unidad}")
assert mezcla.startswith("rechazado") and abs(suma.valor - 2*I_real) < 1e-12
# prueba de aceptacion en la interfaz: el valor entregado debe incluir la unidad y coincidir con la esperada
def acepta(valor, unidad, esperado_Ns, tol=1e-9):
    return abs(Impulso(valor, unidad).en("N*s").valor - esperado_Ns) < tol
print("Interfaz con unidad correcta acepta:", acepta(I_reportado_lbf, "lbf*s", I_real))
print("Interfaz que entrega lbf*s pero declara N*s rechaza:", not acepta(I_reportado_lbf, "N*s", I_real))
assert acepta(I_reportado_lbf, "lbf*s", I_real) and not acepta(I_reportado_lbf, "N*s", I_real)
print("Pruebas superadas.")
