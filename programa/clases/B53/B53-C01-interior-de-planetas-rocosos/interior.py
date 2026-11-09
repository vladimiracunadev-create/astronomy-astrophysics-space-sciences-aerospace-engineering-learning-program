#!/usr/bin/env python3
"""B53-C01: interior de un planeta rocoso SINTETICO de dos capas.
Unidades SI. Marco: esfera sin rotacion. G de NIST CODATA 2022. Python estandar.
Tolerancias: 1e-4 relativo en ambos casos."""
import math, platform
G = 6.67430e-11

def integra(R, capas, n=200000, rc=None):
    dr = R / n
    def rho(r):
        for rex, d in capas:
            if r <= rex:
                return d
        return capas[-1][1]
    m = inercia = 0.0
    ms, rs = [], []
    for i in range(n):
        r = (i + 0.5) * dr
        dm = 4 * math.pi * r * r * rho(r) * dr
        m += dm
        inercia += (2.0 / 3.0) * dm * r * r
        ms.append(m); rs.append(r)
    p, pc = 0.0, None
    for i in range(n - 1, -1, -1):
        r = rs[i]
        p += G * ms[i] / (r * r) * rho(r) * dr
        if rc is not None and pc is None and r <= rc:
            pc = p
    return m, inercia, p, pc

def compute():
    R, rn, dn, dm_ = 6.0e6, 3.0e6, 11000.0, 4500.0
    m, c, pcen, pcmb = integra(R, [(rn, dn), (R, dm_)], rc=rn)
    m_ana = 4 * math.pi / 3 * (dn * rn ** 3 + dm_ * (R ** 3 - rn ** 3))
    c_ana = 8 * math.pi / 15 * (dn * rn ** 5 + dm_ * (R ** 5 - rn ** 5))
    rho_u = 5000.0
    mu, cu, pu, _ = integra(R, [(R, rho_u)])
    mu_ana = 4 * math.pi / 3 * rho_u * R ** 3
    pu_ana = 3 * G * mu_ana ** 2 / (8 * math.pi * R ** 4)
    return dict(M=m, M_ana=m_ana, rho_mean=m_ana / (4 * math.pi / 3 * R ** 3),
                k_num=c / (m * R * R), k_two=c_ana / (m_ana * R * R), Pc=pcen, Pcmb=pcmb,
                Pu_num=pu, Pu_ana=pu_ana, err_pu=abs(pu - pu_ana) / pu_ana,
                err_m=abs(m - m_ana) / m_ana, err_k=abs(c / (m * R * R) - c_ana / (m_ana * R * R)) / (c_ana / (m_ana * R * R)))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"masa: numerica {r['M']:.5e} kg ; analitica {r['M_ana']:.5e} kg ; densidad media {r['rho_mean']:.1f} kg/m3")
    print(f"C/(M R^2): numerico {r['k_num']:.5f} ; analitico {r['k_two']:.5f}")
    print(f"presion central: dos capas {r['Pc']:.4e} Pa ; limite nucleo-manto {r['Pcmb']:.4e} Pa")
    print(f"esfera uniforme: P numerica {r['Pu_num']:.4e} ; analitica {r['Pu_ana']:.4e} ; error relativo {r['err_pu']:.2e}")
    assert r["err_m"] < 1e-4 and r["err_k"] < 1e-4 and r["err_pu"] < 1e-4 and r["k_two"] < 0.4
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
