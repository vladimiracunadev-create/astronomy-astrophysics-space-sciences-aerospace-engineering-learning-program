"""B96-C27: radiofrecuencia de estacion SINTETICA: PIRE, perdida en espacio libre, Eb/N0 y margen; conversion dB <-> lineal."""
import math, sys
print("Python", sys.version.split()[0])
print("Datos SINTETICOS: potencias, ganancias, tasas y limite de PIRE ficticios; c = 299792458 m/s; k = 1.380649e-23 J/K (exacta en el SI)")
c = 299792458.0; k_B = 1.380649e-23; RE = 6378.137
def dB(x): return 10*math.log10(x)
def lin(d): return 10**(d/10)
# --- ENLACE DE SUBIDA (estacion -> satelite), UHF/S sintetico
f = 2.0e9                 # Hz
Pt_W = 5.0                # W
Gt_dBi = 22.0             # antena de estacion
Lt_dB = 1.5               # perdidas de linea
Gr_dBi = 3.0              # antena del satelite
Ts_K = 600.0              # temperatura de ruido del receptor del satelite
R = 256e3                  # bit/s
EbN0_req = 6.0            # dB (sintetico, con codificacion ficticia)
L_otras = 2.0             # dB (atmosfera, polarizacion, apuntamiento)
EIRP_lim = 55.0           # dBW limite de licencia (sintetico)
EIRP = dB(Pt_W) + Gt_dBi - Lt_dB
print(f"PIRE = {dB(Pt_W):.2f} dBW + {Gt_dBi} - {Lt_dB} = {EIRP:.2f} dBW ; limite = {EIRP_lim} dBW ; cumple: {EIRP <= EIRP_lim}")
assert EIRP <= EIRP_lim
def rango(h, el_deg):
    el = math.radians(el_deg); r = RE + h
    return (-RE*math.sin(el) + math.sqrt((RE*math.sin(el))**2 + r*r - RE*RE))*1e3
print("elev[gr]  d[km]   FSPL[dB]  C/N0[dB-Hz]  Eb/N0[dB]  margen[dB]")
res = []
for el in (10.0, 30.0, 90.0):
    d = rango(550.0, el)
    fspl = 20*math.log10(4*math.pi*d*f/c)
    GT = Gr_dBi - dB(Ts_K)
    CN0 = EIRP - fspl - L_otras + GT - dB(k_B)
    EbN0 = CN0 - dB(R)
    marg = EbN0 - EbN0_req
    res.append((el, d, fspl, CN0, EbN0, marg))
    print(f"{el:7.1f} {d/1e3:7.1f} {fspl:9.2f} {CN0:12.2f} {EbN0:10.2f} {marg:10.2f}")
    # comprobacion en lineal
    cn0_lin = (lin(EIRP)*lin(Gr_dBi)/(lin(fspl)*lin(L_otras)*k_B*Ts_K))
    assert abs(dB(cn0_lin) - CN0) < 1e-9
    # comprobacion de FSPL por la formula (4 pi d / lambda)^2
    lam = c/f
    assert abs(dB((4*math.pi*d/lam)**2) - fspl) < 1e-9
# margenes: el peor es el de menor elevacion
assert res[0][5] < res[1][5] < res[2][5]
print(f"Margen peor caso (elevacion 10 grados) = {res[0][5]:.2f} dB ; el capitulo de la NASA cita ~3 dB como margen tipico en LEO a 1500 km: {'cumple' if res[0][5] >= 3 else 'no cumple'} el criterio de lectura")
# potencia minima para margen de 3 dB en el peor caso
Pmin = Pt_W*lin(3.0 - res[0][5])
print(f"Potencia de transmisor para margen exactamente 3 dB a 10 grados = {Pmin:.3f} W (actual {Pt_W} W)")
assert abs((res[0][5] + dB(Pmin/Pt_W)) - 3.0) < 1e-9
# conversion: 3 dB duplica, 10 dB multiplica por 10
print(f"3 dB = x{lin(3.0):.4f} ; 10 dB = x{lin(10.0):.1f} ; 20 dB = x{lin(20.0):.0f}")
assert abs(lin(dB(123.0)) - 123.0) < 1e-9
print("Pruebas superadas.")
