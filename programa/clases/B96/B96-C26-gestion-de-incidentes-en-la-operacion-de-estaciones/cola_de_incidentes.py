"""B96-C26: gestion de incidentes de estacion SINTETICA: cola M/M/1 con prioridades frente a la teoria."""
import heapq, random, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: llegadas de incidentes y tiempos de atencion ficticios; semilla 96")
lam1, lam2, mu = 0.15, 0.45, 1.0      # incidentes/h (alta, baja prioridad) y tasa de servicio /h
rho1, rho2 = lam1/mu, lam2/mu
rho = rho1 + rho2
print(f"lambda1 = {lam1}/h (alta) ; lambda2 = {lam2}/h (baja) ; mu = {mu}/h ; rho = {rho:.2f}")
# teoria M/M/1 FIFO
Wq_fifo = rho/(mu - (lam1 + lam2))
# teoria de prioridad no expropiativa (Cobham), servicio exponencial: W0 = sum(lam_i)/mu^2
W0 = (lam1 + lam2)/mu**2
Wq1 = W0/(1 - rho1); Wq2 = W0/((1 - rho1)*(1 - rho))
print(f"Teoria: FIFO Wq = {Wq_fifo:.4f} h ; prioridad: alta Wq1 = {Wq1:.4f} h ; baja Wq2 = {Wq2:.4f} h")
# conservacion de Kleinrock: sum(rho_i Wq_i) = rho * Wq_fifo
print(f"Conservacion: sum(rho_i Wq_i) = {rho1*Wq1 + rho2*Wq2:.5f} ; rho Wq_fifo = {rho*Wq_fifo:.5f}")
assert abs(rho1*Wq1 + rho2*Wq2 - rho*Wq_fifo) < 1e-12
def simula(prior, N=400000, seed=96):
    rng = random.Random(seed)
    # generar llegadas
    t = 0.0; llegadas = []
    for _ in range(N):
        t += rng.expovariate(lam1 + lam2)
        clase = 1 if rng.random() < lam1/(lam1 + lam2) else 2
        llegadas.append((t, clase, rng.expovariate(mu)))
    cola = []; reloj = 0.0; i = 0; esperas = {1: [], 2: []}; seq = 0; servidor_libre = 0.0
    while i < N or cola:
        if not cola and i < N and llegadas[i][0] > servidor_libre:
            servidor_libre = llegadas[i][0]
        while i < N and llegadas[i][0] <= servidor_libre:
            a = llegadas[i]; seq += 1
            heapq.heappush(cola, ((a[1] if prior else 0), seq, a)); i += 1
        if not cola: continue
        _, _, a = heapq.heappop(cola)
        esperas[a[1]].append(servidor_libre - a[0]); servidor_libre += a[2]
    return esperas
for nom, pr in (("FIFO", False), ("Prioridad", True)):
    e = simula(pr)
    m1 = sum(e[1])/len(e[1]); m2 = sum(e[2])/len(e[2]); mt = (sum(e[1]) + sum(e[2]))/(len(e[1]) + len(e[2]))
    print(f"{nom:10s} simulado: Wq alta = {m1:.4f} h ; baja = {m2:.4f} h ; global = {mt:.4f} h")
    if pr:
        assert abs(m1 - Wq1)/Wq1 < 0.08 and abs(m2 - Wq2)/Wq2 < 0.08
    else:
        assert abs(mt - Wq_fifo)/Wq_fifo < 0.08
# indicadores de gestion: tiempo hasta resolver = espera + servicio
print(f"Tiempo medio hasta resolver (alta prioridad) = {Wq1 + 1/mu:.4f} h = {(Wq1 + 1/mu)*60:.1f} min")
print(f"Tiempo medio hasta resolver (baja prioridad) = {Wq2 + 1/mu:.4f} h = {(Wq2 + 1/mu)*60:.1f} min")
assert Wq1 < Wq_fifo < Wq2
print("Pruebas superadas.")
