"""B88-C02: temporizador, baudios, ADC y consumo de un microcontrolador SINTETICO."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: un microcontrolador generico, sin hoja de datos de fabricante")

f_clk = 16_000_000  # Hz
# Temporizador: interrupcion cada 1 ms con prescaler 64 -> cuenta
for presc in (8, 64, 256):
    cuentas = f_clk / presc * 1e-3
    ent = round(cuentas)
    err = (ent - cuentas) / cuentas * 100
    print(f"prescaler {presc:3d}: cuentas={cuentas:10.3f} -> {ent:6d}  error={err:+.4f} %  (cabe en 16 bit: {ent < 65536})")

# Baudios UART: divisor = f/(16*baud)
for baud in (9600, 115200, 230400, 460800):
    div = round(f_clk / (16 * baud))
    real = f_clk / (16 * div)
    print(f"baud {baud:6d}: divisor={div:4d} real={real:10.1f} error={100*(real-baud)/baud:+.2f} %")

# ADC de 12 bit, referencia 3.3 V
nb, vref = 12, 3.3
lsb = vref / 2**nb
print(f"LSB = {lsb*1e3:.4f} mV ; error de cuantizacion max = +-{lsb/2*1e3:.4f} mV")
for v in (0.0, 1.000, 1.6500, 3.2999):
    cod = min(2**nb - 1, int(v / lsb))
    print(f"V={v:6.4f} -> codigo {cod:4d} -> {cod*lsb:.4f} V")

# Consumo con ciclo de trabajo (mA a 3.3 V)
I_act, I_sleep, duty = 12.0, 0.005, 0.02
I_med = duty * I_act + (1 - duty) * I_sleep
print(f"I media = {I_med:.4f} mA ; potencia = {I_med*3.3:.4f} mW ; energia/dia = {I_med*3.3*24:.3f} mWh")
assert abs(round(f_clk / 64 * 1e-3) - 250) == 0
print("Pruebas superadas.")
