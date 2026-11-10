"""B88-C25: nucleos en paso cerrado (lockstep) con inyeccion de fallos (SINTETICO, semilla fija)."""
import random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: un 'programa' de 8 registros de 16 bit y fallos inyectados por el script")

M = 0xFFFF
def paso(reg, k):
    # programa fijo de 16 instrucciones ciclicas sobre 4 registros
    a, b, c, d = reg
    i = k % 4
    if i == 0: a = (a + b) & M
    elif i == 1: b = (b ^ (c << 1)) & M
    elif i == 2: c = (c + a + 1) & M
    else: d = (d ^ a ^ b) & M
    return [a, b, c, d]
def correr(N, fallo=None, K=1):
    A = [1, 2, 3, 4]; B = [1, 2, 3, 4]; det = None
    for k in range(N):
        A = paso(A, k); B = paso(B, k)
        if fallo and k == fallo[0]:
            B[fallo[1]] ^= 1 << fallo[2]
        if det is None and (k + 1) % K == 0 and A != B:
            det = k
    # al final del programa se comparan tambien las salidas
    if det is None and A != B: det = N - 1
    return det, A == B
random.seed(25)
N = 200
for K in (1, 4, 16):
    n = 4000; det = 0; enmasc = 0; lat = []
    for _ in range(n):
        f = (random.randrange(N), random.randrange(4), random.randrange(16))
        d, igual = correr(N, f, K)
        if d is None: enmasc += 1
        else: det += 1; lat.append(d - f[0])
    print(f"Comparacion cada {K:2d} ciclos: detectados={det:4d} enmascarados={enmasc:4d} latencia media={sum(lat)/len(lat):5.2f} ciclos max={max(lat)}")
# Falla comun: ambos nucleos reciben el mismo fallo -> no se detecta
def correr_comun(N, f):
    A = [1, 2, 3, 4]; B = [1, 2, 3, 4]; det = False
    for k in range(N):
        A = paso(A, k); B = paso(B, k)
        if k == f[0]: A[f[1]] ^= 1 << f[2]; B[f[1]] ^= 1 << f[2]
        if A != B: det = True
    return det
comunes = sum(correr_comun(N, (random.randrange(N), random.randrange(4), random.randrange(16))) for _ in range(500))
print(f"Falla comun (identica en ambos nucleos): detectadas = {comunes} de 500")
assert comunes == 0
print("Pruebas superadas.")
