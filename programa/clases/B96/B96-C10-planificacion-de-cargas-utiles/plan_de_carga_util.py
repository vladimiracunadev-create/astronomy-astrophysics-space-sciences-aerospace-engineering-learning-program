"""B96-C10: planificacion de carga util SINTETICA con presupuesto de energia y datos (mochila 2D)."""
import sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: observaciones, valores y consumos ficticios")
obs = [("O1", 8, 12, 40), ("O2", 5, 7, 25), ("O3", 9, 15, 60), ("O4", 4, 6, 15), ("O5", 7, 10, 35), ("O6", 3, 4, 10),
       ("O7", 6, 9, 50), ("O8", 10, 14, 45), ("O9", 2, 3, 5), ("O10", 6, 8, 30), ("O11", 5, 11, 20), ("O12", 4, 5, 45)]
E_MAX, D_MAX = 40, 160
def coste(o): return o[2]/E_MAX + o[3]/D_MAX
def voraz(clave):
    sel = []; e = d = 0
    for o in sorted(obs, key=clave, reverse=True):
        if e + o[2] <= E_MAX and d + o[3] <= D_MAX:
            sel.append(o); e += o[2]; d += o[3]
    return sel, e, d
sel_g, e, d = voraz(lambda o: o[1]/coste(o))
vg = sum(o[1] for o in sel_g)
print(f"Voraz por valor/coste: {[o[0] for o in sel_g]} ; valor = {vg} ; energia = {e}/{E_MAX} Wh ; datos = {d}/{D_MAX} MB")
sel_v, e2, d2 = voraz(lambda o: o[1])
vv2 = sum(o[1] for o in sel_v)
print(f"Voraz por valor:       {[o[0] for o in sel_v]} ; valor = {vv2} ; energia = {e2}/{E_MAX} Wh ; datos = {d2}/{D_MAX} MB")
def opt(em):
    dp = [[0]*(D_MAX+1) for _ in range(em+1)]
    for _, v, we, wd in obs:
        for a in range(em, we-1, -1):
            for b in range(D_MAX, wd-1, -1):
                dp[a][b] = max(dp[a][b], dp[a-we][b-wd] + v)
    return dp[em][D_MAX]
vdp = opt(E_MAX)
mejor = 0; sel_b = None
for mask in range(1 << len(obs)):
    ee = dd = vv = 0
    for i, o in enumerate(obs):
        if mask >> i & 1: ee += o[2]; dd += o[3]; vv += o[1]
    if ee <= E_MAX and dd <= D_MAX and vv > mejor:
        mejor, sel_b = vv, [o[0] for i, o in enumerate(obs) if mask >> i & 1]
print(f"Optimo por programacion dinamica = {vdp} ; por fuerza bruta (4096 subconjuntos) = {mejor} ; seleccion = {sel_b}")
print(f"Brecha del voraz por valor/coste = {vdp - vg} ({100*(vdp-vg)/vdp:.1f} %) ; del voraz por valor = {vdp - vv2} ({100*(vdp-vv2)/vdp:.1f} %)")
assert vdp == mejor and vg <= vdp and vv2 <= vdp
for em in (40, 35, 30, 25, 20):
    print(f"  energia {em:2d} Wh -> valor optimo = {opt(em)}")
print("Pruebas superadas.")
