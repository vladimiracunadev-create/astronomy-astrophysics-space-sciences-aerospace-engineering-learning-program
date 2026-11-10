#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C24. Recepcion de telemetria debil: umbral de seguimiento de un lazo de portadora, ancho de banda de lazo minimo frente a Doppler y
deteccion de una portadora por integracion coherente (FFT) con falsa alarma controlada. Senal y ruido SINTETICOS, semilla 89.
Los umbrales de lazo y las relaciones de deteccion son estandar, no consultados."""
import cmath, math, random, sys

def fft(x):
    n = len(x)
    if n == 1:
        return x
    par, impar = fft(x[0::2]), fft(x[1::2])
    t = [cmath.exp(-2j * math.pi * k / n) * impar[k] for k in range(n // 2)]
    return [par[k] + t[k] for k in range(n // 2)] + [par[k] - t[k] for k in range(n // 2)]

def snr_lazo_db(cn0_dbhz, bl):
    return cn0_dbhz - 10 * math.log10(bl)

def cn0_umbral(bl, snr_umbral_db=10.0):
    return snr_umbral_db + 10 * math.log10(bl)

def bl_min_doppler(fdot, err_max_rad, zeta=0.7071):
    """B_L minimo tal que el error por rampa 2 pi fdot / wn^2 <= err_max (wn = 8 zeta B_L / (4 zeta^2 + 1))."""
    wn = math.sqrt(2 * math.pi * fdot / err_max_rad)
    return wn * (4 * zeta ** 2 + 1) / (8 * zeta)

def detectar(cn0_dbhz, n, fs, rng, con_senal=True, bin_senal=None):
    cn0 = 10 ** (cn0_dbhz / 10)
    sigma = math.sqrt(fs / cn0 / 2)
    k0 = bin_senal if bin_senal is not None else rng.randrange(n)
    x = []
    for i in range(n):
        s = cmath.exp(2j * math.pi * k0 * i / n) if con_senal else 0j
        x.append(s + complex(rng.gauss(0, sigma), rng.gauss(0, sigma)))
    X = fft(x)
    pot = [abs(v) ** 2 for v in X]
    pico = max(range(n), key=lambda k: pot[k])
    return pot[pico], pico, k0, sigma ** 2 * 2 * n   # potencia del pico, indice, indice real, media del ruido por bin

def calcular():
    R = {}
    R["lazo"] = {bl: snr_lazo_db(30.0, bl) for bl in (0.1, 1.0, 10.0)}
    R["umbral"] = {bl: cn0_umbral(bl) for bl in (0.1, 1.0, 10.0)}
    R["bl_min"] = {(fd, er): bl_min_doppler(fd, er) for fd, er in ((0.01, 0.3), (0.1, 0.3), (1.0, 0.3))}
    n, fs, T = 1024, 16.0, 1024 / 16.0
    pfa_obj = 1e-3
    pb = 1 - (1 - pfa_obj) ** (1 / n)
    R["n"], R["T"] = n, T
    rng = random.Random(89)
    # falsa alarma: solo ruido, umbral para Pfa total 1e-3 con media de ruido por bin = media_ruido
    cn0_ref = 0.0
    sigma2 = fs / (10 ** (cn0_ref / 10))      # varianza compleja total por muestra
    media_bin = sigma2 * n
    umbral = -media_bin * math.log(pb)
    R["umbral_pot"] = umbral
    ensayos = 400
    fa = 0
    for _ in range(ensayos):
        p, _, _, _ = detectar(cn0_ref, n, fs, rng, con_senal=False)
        fa += p > umbral
    R["pfa_sim"], R["pfa_obj"], R["ens_fa"] = fa / ensayos, pfa_obj, ensayos
    R["pd"] = {}
    for cn0_db in (-12.0, -10.0, -8.0, -6.0, -4.0):
        sigma2c = fs / (10 ** (cn0_db / 10))
        # el umbral se fija con el ruido de ese C/N0 para mantener la misma Pfa
        umb = -(sigma2c * n) * math.log(pb)
        det = 0
        N_ = 150
        for _ in range(N_):
            p, pico, k0, _ = detectar(cn0_db, n, fs, rng, True)
            det += (p > umb) and pico == k0
        R["pd"][cn0_db] = det / N_
    R["snr_bin"] = {c: 10 * math.log10(n / (fs / (10 ** (c / 10)))) for c in R["pd"]}
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar), random.Random(89)")
    print("SNR del lazo = C/N0 - 10 log10(B_L) con C/N0 = 30 dB-Hz:", ", ".join(f"B_L = {b} Hz: {v:.1f} dB" for b, v in R["lazo"].items()))
    print("C/N0 minimo para SNR de lazo de 10 dB:", ", ".join(f"B_L = {b} Hz: {v:.1f} dB-Hz" for b, v in R["umbral"].items()))
    print("B_L minimo para seguir una rampa (error <= 0.3 rad):")
    for (fd, er), v in R["bl_min"].items():
        print(f"  rampa {fd} Hz/s: B_L >= {v:.3f} Hz")
    print(f"Deteccion por FFT de {R['n']} muestras (T = {R['T']:.0f} s), Pfa objetivo {R['pfa_obj']:.0e}")
    print(f"  falsas alarmas simuladas = {R['pfa_sim']:.4f} en {R['ens_fa']} ensayos (solo ruido)")
    for c, p in R["pd"].items():
        print(f"  C/N0 = {c:+.0f} dB-Hz: SNR en el bin = {R['snr_bin'][c]:5.1f} dB ; P_deteccion = {p:.3f}")
    assert R["pfa_sim"] < 0.02
    pds = list(R["pd"].values())
    assert pds == sorted(pds) and pds[-1] > 0.95 and pds[0] < 0.6
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
