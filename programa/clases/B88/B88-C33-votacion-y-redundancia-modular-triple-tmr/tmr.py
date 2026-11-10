"""B88-C33: votacion 2 de 3 (TMR): fiabilidad con y sin votador y votacion bit a bit (SINTETICO, semilla 33)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: fiabilidades por modulo inventadas; canales independientes")

def tmr(r): return 3 * r * r - 2 * r ** 3
print(" r_modulo   R_TMR     R_simple  mejora   R_TMR*R_votador(0.9999)")
for r in (0.50, 0.70, 0.90, 0.95, 0.99, 0.999):
    print(f" {r:7.3f}  {tmr(r):9.6f}  {r:9.6f}  {tmr(r)-r:+.6f}  {tmr(r)*0.9999:.6f}")
# cruce: TMR > simple solo si r > 0.5
for r in (0.40, 0.50, 0.60):
    print(f"r={r:.2f}: TMR - simple = {tmr(r)-r:+.6f}")
random.seed(33)
N = 200000; r = 0.9
ok = sum(1 for _ in range(N) if sum(random.random() < r for _ in range(3)) >= 2)
print(f"Monte Carlo r=0.9, {N} corridas: R = {ok/N:.5f} (teorico {tmr(0.9):.5f})")
assert abs(ok / N - tmr(0.9)) < 0.003

def voto(a, b, c): return (a & b) | (a & c) | (b & c)
# Votacion bit a bit: un canal con un bit invertido se corrige; dos canales con el mismo bit invertido no
dato = 0b10110100
errores = {"un canal con 1 bit": (dato ^ 0b00000100, dato, dato),
           "dos canales, bits distintos": (dato ^ 0b00000001, dato ^ 0b10000000, dato),
           "dos canales, mismo bit": (dato ^ 0b00001000, dato ^ 0b00001000, dato)}
for k, (a, b, c) in errores.items():
    v = voto(a, b, c)
    print(f"{k:30s}: voto = {v:08b} correcto = {v == dato}")
assert voto(*errores["un canal con 1 bit"]) == dato and voto(*errores["dos canales, bits distintos"]) == dato
assert voto(*errores["dos canales, mismo bit"]) != dato
# Cuantos canales fallidos tolera: 1 de 3 ; N-modular generaliza
from math import comb
for n in (3, 5):
    k = n // 2 + 1
    R = sum(comb(n, i) * 0.9 ** i * 0.1 ** (n - i) for i in range(k, n + 1))
    print(f"{n}-modular con r=0.9 (mayoria de {k}): R = {R:.6f}")
print("Pruebas superadas.")
