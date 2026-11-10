"""B96-C21: diagnostico bayesiano EXPLICABLE (SINTETICO): posterior y aporte de cada sintoma."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: hipotesis, sintomas y probabilidades ficticios")
H = ["Nominal", "Panel degradado", "Bateria degradada", "Sensor de corriente sesgado", "Carga extra no prevista"]
prior = {"Nominal": 0.90, "Panel degradado": 0.03, "Bateria degradada": 0.03, "Sensor de corriente sesgado": 0.02, "Carga extra no prevista": 0.02}
S = ["Generacion baja en luz", "Tension de bateria cae en eclipse", "SOC baja de orbita en orbita", "Corriente medida no cuadra con la suma de cargas"]
# P(sintoma presente | hipotesis)
P = {
 "Nominal":                      [0.02, 0.03, 0.02, 0.02],
 "Panel degradado":              [0.90, 0.10, 0.60, 0.05],
 "Bateria degradada":            [0.05, 0.85, 0.50, 0.05],
 "Sensor de corriente sesgado":  [0.05, 0.05, 0.10, 0.90],
 "Carga extra no prevista":      [0.10, 0.20, 0.80, 0.10],
}
obs = [1, 0, 1, 0]       # sintomas observados
def lik(h, obs):
    p = 1.0
    for pj, o in zip(P[h], obs): p *= pj if o else (1 - pj)
    return p
unnorm = {h: prior[h]*lik(h, obs) for h in H}
Z = sum(unnorm.values()); post = {h: unnorm[h]/Z for h in H}
print("Observado:", {s: bool(o) for s, o in zip(S, obs)})
print("Hipotesis                      prior   verosimilitud  posterior")
for h in H: print(f"{h:30s} {prior[h]:6.3f} {lik(h, obs):14.6f} {post[h]:10.5f}")
top = max(H, key=lambda h: post[h])
print(f"Diagnostico = {top} (posterior {post[top]:.4f})")
# explicacion: aporte de cada sintoma al log-odds frente a Nominal
print(f"Explicacion de '{top}' frente a 'Nominal' (log10 de razon de verosimilitud por sintoma):")
tot = math.log10(prior[top]/prior["Nominal"])
print(f"  prior log10-odds = {tot:+.4f}")
contribs = []
for j, (s, o) in enumerate(zip(S, obs)):
    a = P[top][j] if o else 1 - P[top][j]; b = P["Nominal"][j] if o else 1 - P["Nominal"][j]
    c = math.log10(a/b); contribs.append((c, s, o)); tot += c
    print(f"  {s:50s} presente={o}  aporte = {c:+.4f}")
lo_post = math.log10(post[top]/post["Nominal"])
print(f"  suma = {tot:+.4f} ; log10-odds posterior = {lo_post:+.4f}")
assert abs(tot - lo_post) < 1e-12
assert abs(sum(post.values()) - 1) < 1e-12
# contrafactual: quitar el sintoma de mayor aporte
mayor = max(contribs)
j = S.index(mayor[1]); obs2 = list(obs); obs2[j] = 0
un2 = {h: prior[h]*lik(h, obs2) for h in H}; Z2 = sum(un2.values()); post2 = {h: un2[h]/Z2 for h in H}
top2 = max(H, key=lambda h: post2[h])
print(f"Sin el sintoma '{mayor[1]}': diagnostico = {top2} (posterior {post2[top2]:.4f})")
assert top2 != top
# calibracion de la incertidumbre: segundo mejor
orden = sorted(H, key=lambda h: -post[h])
print(f"Segundo candidato = {orden[1]} ({post[orden[1]]:.4f}) ; razon = {post[orden[0]]/post[orden[1]]:.1f}")
print("Pruebas superadas.")
