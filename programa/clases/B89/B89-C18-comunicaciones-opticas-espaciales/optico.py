#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C18. Comunicaciones opticas espaciales: banda optica de CCSDS 141.0-B-1, fotones por bit y error de PPM con deteccion de fotones.
Enlace SINTETICO (potencia, aperturas, distancia), semilla 89. c: NIST CODATA 2022 (consultada); h = 6.62607015e-34 J s es la constante exacta del SI (no consultada en esta sesion)."""
import math, random, sys

C = 299_792_458.0
H = 6.62607015e-34   # J s, exacta (SI); no consultada en esta sesion

def poisson(lam, rng):
    if lam > 30:
        return max(0, int(round(rng.gauss(lam, math.sqrt(lam)))))
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1

def sim_ppm(m, ns, nb, simbolos, rng):
    err = 0
    for _ in range(simbolos):
        pos = rng.randrange(m)
        cuentas = [poisson(nb + (ns if i == pos else 0.0), rng) for i in range(m)]
        mx = max(cuentas)
        cand = [i for i, c in enumerate(cuentas) if c == mx]
        err += rng.choice(cand) != pos
    return err / simbolos

def calcular():
    R = {}
    # banda optica de CCSDS 141.0-B-1: 191.3 a 195.9 THz
    R["lam_ini"], R["lam_fin"] = C / 195.9e12, C / 191.3e12
    R["f_1550"] = C / 1550e-9
    R["foton_1550"] = H * R["f_1550"]
    # presupuesto sintetico a la Luna
    pt, d = 0.5, 384_400e3
    lam = 1550e-9
    dt, dr = 0.10, 0.40
    gt = (math.pi * dt / lam) ** 2
    gr = (math.pi * dr / lam) ** 2
    pr = pt * gt * gr * (lam / (4 * math.pi * d)) ** 2
    R["gt_db"], R["gr_db"] = 10 * math.log10(gt), 10 * math.log10(gr)
    R["perd_db"] = -10 * math.log10((lam / (4 * math.pi * d)) ** 2)
    R["pr_w"] = pr
    R["fot_s"] = pr / R["foton_1550"]
    # tasa con 16-PPM y ranuras de 1 ns
    m, ranura = 16, 1e-9
    R["bits_simbolo"] = math.log2(m)
    R["periodo_s"] = 4 * 0 + 32 * ranura     # 16 ranuras + 16 de guarda (ilustrativo)
    R["tasa"] = R["bits_simbolo"] / R["periodo_s"]
    R["fot_por_simbolo"] = R["fot_s"] * R["periodo_s"]
    R["fot_por_bit"] = R["fot_por_simbolo"] / R["bits_simbolo"]
    # PPM sin fondo: P = e^-ns (M-1)/M
    rng = random.Random(89)
    R["ppm"] = {}
    for ns in (1.0, 3.0, 6.0):
        sim = sim_ppm(16, ns, 0.0, 60000, rng)
        teo = math.exp(-ns) * (16 - 1) / 16
        R["ppm"][ns] = (sim, teo)
    R["fondo"] = {}
    for nb in (0.0, 0.1, 0.5):
        R["fondo"][nb] = sim_ppm(16, 6.0, nb, 20000, rng)
    R["chk"] = max(abs(s - t) / math.sqrt(max(t, 1e-9) * (1 - t) / 60000) for s, t in R["ppm"].values())
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print(f"Banda C optica CCSDS 141.0-B-1: 191.3-195.9 THz -> {R['lam_ini']*1e9:.2f} a {R['lam_fin']*1e9:.2f} nm (vacio)")
    print(f"1550 nm: f = {R['f_1550']/1e12:.3f} THz ; energia del foton = {R['foton_1550']:.4e} J")
    print("SINTETICO: Pt = 0.5 W, aperturas 10 cm (Tx) y 40 cm (Rx), d = 384 400 km, 1550 nm")
    print(f"  Gt = {R['gt_db']:.1f} dBi ; Gr = {R['gr_db']:.1f} dBi ; perdida de espacio libre = {R['perd_db']:.1f} dB")
    print(f"  Pr = {R['pr_w']:.3e} W = {R['fot_s']:.3e} fotones/s")
    print(f"  16-PPM, ranura 1 ns, 16 ranuras de guarda: {R['bits_simbolo']:.0f} bit/simbolo ; tasa = {R['tasa']/1e6:.1f} Mbit/s")
    print(f"  fotones por simbolo = {R['fot_por_simbolo']:.3e} ; por bit = {R['fot_por_bit']:.3e}")
    print("Error de simbolo 16-PPM sin fondo (60000 simbolos): simulado frente a e^-ns (M-1)/M")
    for ns, (s, t) in R["ppm"].items():
        print(f"  ns = {ns:.1f}: simulado = {s:.4f} ; teorico = {t:.4f}")
    print("Con ns = 6 y fondo nb por ranura (20000 simbolos):")
    for nb, v in R["fondo"].items():
        print(f"  nb = {nb:.1f}: P_error = {v:.4f}")
    assert R["chk"] < 4.0
    assert abs(R["lam_ini"] * 1e9 - 1530.33) < 0.01 and abs(R["lam_fin"] * 1e9 - 1567.13) < 0.01
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
