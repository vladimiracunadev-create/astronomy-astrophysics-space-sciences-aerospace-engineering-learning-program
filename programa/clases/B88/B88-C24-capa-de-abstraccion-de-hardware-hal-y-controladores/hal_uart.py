"""B88-C24: capa HAL con dos implementaciones de un mismo dispositivo y pruebas (SINTETICO)."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: UART virtual de 4 bytes de FIFO; sin hardware real")

# Interfaz de la HAL: enviar(byte) -> bool ; estado_tx_libre() ; leer()
class UartRegistros:
    """Implementacion 'de registros': modela un dispositivo con FIFO y bit de estado."""
    FIFO = 4
    def __init__(self): self.fifo = []; self.salida = []; self.accesos = 0
    def tx_libre(self): self.accesos += 1; return len(self.fifo) < self.FIFO
    def escribir(self, b):
        self.accesos += 1
        if len(self.fifo) >= self.FIFO: return False
        self.fifo.append(b); return True
    def avanzar(self, n=1):
        for _ in range(n):
            if self.fifo: self.salida.append(self.fifo.pop(0))
class UartMock:
    """Implementacion 'mock': registra las llamadas, sin FIFO."""
    def __init__(self): self.salida = []; self.llamadas = []; self.accesos = 0
    def tx_libre(self): self.accesos += 1; return True
    def escribir(self, b): self.accesos += 1; self.llamadas.append(b); self.salida.append(b); return True
    def avanzar(self, n=1): pass

# Aplicacion: no conoce el dispositivo, solo la interfaz de la HAL
def enviar_paquete(hal, datos, max_reintentos=20):
    enviados = 0; reint = 0
    for b in datos:
        while not hal.tx_libre():
            hal.avanzar(1); reint += 1
            if reint > max_reintentos: return enviados, reint, "TIMEOUT"
        if hal.escribir(b): enviados += 1
    return enviados, reint, "OK"

datos = list(range(10, 22))  # 12 bytes
for nombre, cls in (("registros (FIFO 4)", UartRegistros), ("mock", UartMock)):
    h = cls()
    n, r, est = enviar_paquete(h, datos)
    h.avanzar(10)
    print(f"{nombre:20s}: enviados={n} reintentos={r} estado={est} salida_ok={h.salida == datos} accesos={h.accesos}")
# Prueba de falla: el dispositivo nunca avanza (dispositivo colgado)
class Colgada(UartRegistros):
    def avanzar(self, n=1): pass
h = Colgada(); n, r, est = enviar_paquete(h, datos)
print(f"{'dispositivo colgado':20s}: enviados={n} reintentos={r} estado={est}")
assert est == "TIMEOUT" and n == 4
h1 = UartRegistros(); enviar_paquete(h1, datos); h1.avanzar(10)
h2 = UartMock(); enviar_paquete(h2, datos)
assert h1.salida == h2.salida == datos and h2.llamadas == datos
print("Pruebas superadas.")
