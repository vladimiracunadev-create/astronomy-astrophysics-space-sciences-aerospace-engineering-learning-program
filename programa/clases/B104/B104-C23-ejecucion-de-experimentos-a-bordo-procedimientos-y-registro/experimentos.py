#!/usr/bin/env python3
"""B104-C23: asignacion de horas de tripulacion a experimentos (mochila) y registro encadenado con hash.
DATOS SINTETICOS (semilla 104); horas y valores ILUSTRATIVOS. No describe experimentos reales."""
import sys
import hashlib
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("DATOS SINTETICOS (semilla 104): 12 experimentos ficticios con horas de tripulacion y valor cientifico inventado; capacidad 20 h")
rng = np.random.default_rng(104)
horas = rng.integers(2, 9, 12)
valor = np.round(rng.uniform(1, 10, 12) * horas ** 0.7, 1)
CAP = 20
print("\nexperimento | horas | valor | valor por hora")
for i in range(12):
    print(f"{i:11d} {horas[i]:5d} {valor[i]:6.1f} {valor[i]/horas[i]:14.2f}")


def mochila(horas, valor, cap):
    n = len(horas)
    dp = np.zeros((n + 1, cap + 1))
    for i in range(1, n + 1):
        for c in range(cap + 1):
            dp[i, c] = dp[i - 1, c]
            if horas[i - 1] <= c:
                dp[i, c] = max(dp[i, c], dp[i - 1, c - horas[i - 1]] + valor[i - 1])
    sel, c = [], cap
    for i in range(n, 0, -1):
        if dp[i, c] != dp[i - 1, c]:
            sel.append(i - 1)
            c -= horas[i - 1]
    return dp[n, cap], sorted(sel)


def voraz(horas, valor, cap):
    orden = np.argsort(-valor / horas)
    t, v, sel = 0, 0.0, []
    for i in orden:
        if t + horas[i] <= cap:
            t += horas[i]; v += valor[i]; sel.append(int(i))
    return v, sorted(sel)


vo, so = mochila(horas, valor, CAP)
vg, sg = voraz(horas, valor, CAP)
print(f"\nOptimo (programacion dinamica): valor {vo:.1f}; experimentos {so}; horas {int(horas[so].sum())}")
print(f"Voraz por valor/hora:           valor {vg:.1f}; experimentos {sg}; horas {int(horas[sg].sum())}")
print(f"Brecha del voraz respecto del optimo: {100*(vo-vg)/vo:.1f} %")

# Registro encadenado con hash (SHA-256): cada entrada incluye el hash de la anterior
def construir(registros):
    cadena, previo = [], "0" * 64
    for r in registros:
        h = hashlib.sha256((previo + r).encode()).hexdigest()
        cadena.append((r, h))
        previo = h
    return cadena


def verificar(cadena):
    previo = "0" * 64
    for i, (r, h) in enumerate(cadena):
        if hashlib.sha256((previo + r).encode()).hexdigest() != h:
            return i
        previo = h
    return -1


mediciones = rng.normal(5.00, 0.05, 5)
registros = [f"exp {so[0]}; paso {k+1}; lectura {m:.3f} unidad; operador A" for k, m in enumerate(mediciones)]
cad = construir(registros)
print(f"\nRegistro de {len(cad)} entradas; primer hash {cad[0][1][:16]}...; ultimo {cad[-1][1][:16]}...")
print(f"Verificacion de la cadena integra: primera entrada rota = {verificar(cad)} (-1 = sin rotura)")
adulterada = list(cad)
adulterada[2] = (registros[2].replace("lectura", "lectura(editada)"), cad[2][1])
print(f"Tras editar la entrada 2: primera entrada rota = {verificar(adulterada)}")
print(f"Lecturas: media {mediciones.mean():.4f}; desviacion tipica muestral {mediciones.std(ddof=1):.4f}; incertidumbre de la media {mediciones.std(ddof=1)/np.sqrt(5):.4f}")

assert vo >= vg - 1e-9
assert horas[so].sum() <= CAP and horas[sg].sum() <= CAP
assert verificar(cad) == -1 and verificar(adulterada) == 2
print("Pruebas superadas.")
