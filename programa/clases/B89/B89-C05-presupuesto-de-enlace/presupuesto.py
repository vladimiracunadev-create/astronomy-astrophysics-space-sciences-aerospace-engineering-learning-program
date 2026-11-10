#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C05. Presupuesto de enlace de bajada, banda X, en decibelios. Todos los parametros del equipo son SINTETICOS.
k: NIST CODATA 2022 (consultada); c: NIST CODATA 2022 (consultada)."""
import math, sys

C = 299_792_458.0
K = 1.380649e-23   # J/K
UA = 1.495978707e11  # m, redondeado, ILUSTRATIVO

def db(x):
    return 10 * math.log10(x)

def ebn0_req_bpsk(ber):
    """Eb/N0 [dB] requerido por BPSK coherente: BER = 0.5 erfc(sqrt(Eb/N0)); biseccion."""
    lo, hi = 0.0, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if 0.5 * math.erfc(math.sqrt(mid)) > ber:
            lo = mid
        else:
            hi = mid
    return db(lo)

def presupuesto(d, f, rb, **p):
    r = {}
    r["pire"] = db(p["pt_w"]) - p["perd_tx"] + p["gt_dbi"]
    r["fspl"] = 20 * math.log10(4 * math.pi * d * f / C)
    r["perd_otras"] = p["atm"] + p["punt"] + p["pol"]
    r["gt"] = p["gr_dbi"] - db(p["tsis"])
    r["k_db"] = db(K)
    r["cn0"] = r["pire"] - r["fspl"] - r["perd_otras"] + r["gt"] - r["k_db"]
    r["ebn0"] = r["cn0"] - db(rb)
    r["req"] = ebn0_req_bpsk(p["ber"]) + p["perd_impl"] - p["gan_cod"]
    r["margen"] = r["ebn0"] - r["req"]
    r["rb_max"] = 10 ** ((r["cn0"] - r["req"] - p["margen_obj"]) / 10)
    return r

PARAM = dict(pt_w=20.0, perd_tx=1.0, gt_dbi=40.0, atm=0.3, punt=0.5, pol=0.2, gr_dbi=68.0, tsis=25.0,
             ber=1e-5, perd_impl=1.0, gan_cod=0.0, margen_obj=3.0)

def calcular():
    R = {"sin_cod": presupuesto(1.0 * UA, 8.4e9, 100e3, **PARAM)}
    R["con_cod"] = presupuesto(1.0 * UA, 8.4e9, 100e3, **{**PARAM, "gan_cod": 6.0})
    R["req_bpsk"] = ebn0_req_bpsk(1e-5)
    # segunda via: mismo balance en unidades lineales
    s = R["sin_cod"]
    lin = (PARAM["pt_w"] * 10 ** (-PARAM["perd_tx"] / 10) * 10 ** (PARAM["gt_dbi"] / 10) * 10 ** (PARAM["gr_dbi"] / 10)
           / (10 ** (s["fspl"] / 10) * 10 ** (s["perd_otras"] / 10) * K * PARAM["tsis"]))
    R["chk_lineal"] = abs(db(lin) - s["cn0"])
    R["dist_dobla"] = presupuesto(2.0 * UA, 8.4e9, 100e3, **PARAM)["margen"] - s["margen"]
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("SINTETICO: 20 W, Gt 40 dBi, Gr 68 dBi, Tsis 25 K, 100 kbit/s, d = 1 UA, banda X 8.4 GHz")
    for nombre in ("sin_cod", "con_cod"):
        r = R[nombre]
        print(f"--- {nombre} ---")
        print(f"  PIRE = {r['pire']:.2f} dBW ; FSPL = {r['fspl']:.2f} dB ; otras perdidas = {r['perd_otras']:.2f} dB")
        print(f"  G/T = {r['gt']:.2f} dB/K ; 10log k = {r['k_db']:.2f} dBW/K/Hz ; C/N0 = {r['cn0']:.2f} dB-Hz")
        print(f"  Eb/N0 = {r['ebn0']:.2f} dB ; requerido = {r['req']:.2f} dB ; margen = {r['margen']:.2f} dB")
        print(f"  tasa maxima con 3 dB de margen = {r['rb_max']/1e3:.1f} kbit/s")
    print(f"Eb/N0 de BPSK para BER 1e-5 = {R['req_bpsk']:.3f} dB")
    print(f"Margen al duplicar la distancia: {R['dist_dobla']:+.3f} dB")
    assert R["chk_lineal"] < 1e-9 and abs(R["req_bpsk"] - 9.59) < 0.01
    assert abs(R["dist_dobla"] + 6.0206) < 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
